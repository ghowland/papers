# VDR-Zig Minimal Toy LLM Technical Specification

## Scope

A single-file Zig implementation of the toy LLM from HOWL-VDR-31-2026, targeting CPU SIMD. Same architecture: single-block, single-head causal transformer, 5-token vocabulary, 4-dimensional embeddings, trained on "the cat sat on the mat." All arithmetic in fixed-basis VDR at Q16 (D = 2^16 = 65536). No floating-point anywhere.

The goal is the smallest possible Zig program that trains a transformer and generates text using integer-only VDR arithmetic, producing bit-identical results across platforms.

---

## 1. Basis Frame: Q16

The Python toy uses Q32 (D = 2^32). The Zig toy uses Q16 (D = 2^16) because:

- `i16 × i16` → `i32` fits a single widening multiply instruction
- `divmod` by 2^16 is a right shift by 16 and a bitwise AND with 0xFFFF
- Accumulation in `i32` gives 16 bits of headroom for dot products of length 4-8
- The full V+R pair fits in a single `i32` (upper 16 = V, lower 16 = R)
- Precision floor: 1/65536 ≈ 1.5 × 10^-5, sufficient for a toy model with 20 training epochs

All values in the system are `i16` V slots. Remainders are `i16` R slots. Accumulators are `i32`. Gradients are `i32` accumulated, rebased to `i16` for weight update.

---

## 2. Core Types

### 2.1 VDR16

The fundamental value type. Two `i16` fields.

```
VDR16 {
    v: i16    // value slot — settled numerator in D=65536 frame
    r: i16    // remainder slot — exact overflow from last operation
}
```

Construction from rational: `VDR16.from_rational(num, den)` computes `divmod(num * 65536, den)`, stores quotient as `v`, remainder as `r`. Example: `1/3` → `v = 21845`, `r = 21845` (since `65536/3 = 21845 remainder 1`, but scaled: `1 * 65536 / 3 = 21845 r 1`).

### 2.2 Vec16

Fixed-length vector of VDR16 values. For this toy, all vectors are length 4 (DIM), 5 (VOCAB_SIZE), or 8 (FFN_DIM). Use comptime-known length.

```
Vec16(comptime N: usize) {
    v: [N]i16    // deinterleaved: V values contiguous
    r: [N]i16    // R values contiguous
}
```

Deinterleaved layout from Vector 3 of the SIMD report. V array and R array stored separately. A SIMD load reads N consecutive V values into one register, N consecutive R values into another. No interleaving overhead.

### 2.3 Mat16

Fixed-size matrix of `i16` V values. Weights are closed (R = 0) so only V is stored. Activations carry R.

```
WeightMat(comptime ROWS: usize, comptime COLS: usize) {
    v: [ROWS][COLS]i8    // weight storage at i8 precision
}

ActMat(comptime ROWS: usize, comptime COLS: usize) {
    v: [ROWS][COLS]i16   // activation V
    r: [ROWS][COLS]i16   // activation R
}
```

Weights stored at `i8` following the SIMD report (weight Q8 × activation Q16 path). For the toy model dimensions (4×4, 4×8, 8×4, 4×5), these are small enough to live entirely in L1.

---

## 3. Scalar Kernel Primitives

These are the operations from Vector 1 of the SIMD report, specialized to Q16.

### 3.1 basis_mul

```
basis_mul(a: i16, b: i16) -> VDR16
    wide: i32 = @as(i32, a) * @as(i32, b)
    v: i16 = @truncate(wide >> 16)
    r: i16 = @truncate(wide & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

Three instructions: widening multiply, shift, mask. No branching. This is the entire basis-frame multiply — the operation that took 15 lines of Python with lazy imports and frame detection.

### 3.2 basis_mul_w8

Weight (i8) × activation (i16) path.

```
basis_mul_w8(w: i8, a: i16) -> VDR16
    wide: i32 = @as(i32, w) * @as(i32, a)
    v: i16 = @truncate(wide >> 16)
    r: i16 = @truncate(wide & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

Same code, different input width. The widening multiply handles it.

### 3.3 basis_add

```
basis_add(a: i16, b: i16) -> VDR16
    wide: i32 = @as(i32, a) + @as(i32, b)
    v: i16 = @truncate(wide >> 16)      // overflow into V (will be 0 or ±1)
    r: i16 = @truncate(wide & 0xFFFF)   // remainder
    return VDR16{ .v = v, .r = r }
```

Wait — addition in Q16 doesn't need divmod. Two values in the same frame: `a/D + b/D = (a+b)/D`. The sum stays in frame as long as it fits in `i16`. If it overflows, the carry is the issue. For the toy model with small values, overflow won't happen. But for correctness:

```
basis_add(a: i16, b: i16) -> VDR16
    wide: i32 = @as(i32, a) + @as(i32, b)
    if (wide >= -32768 and wide <= 32767) {
        return VDR16{ .v = @truncate(wide), .r = 0 }
    }
    // overflow: shouldn't happen in toy model
    v: i16 = @truncate(wide >> 16)
    r: i16 = @truncate(wide & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

For the toy, the simple path (truncate, R=0) will always be taken.

### 3.4 basis_div_barrett

Division by precomputed multiplicative inverse.

```
BarrettConst {
    multiplier: i32
    shift: u5
}

precompute_barrett(divisor: i16) -> BarrettConst
    // standard Barrett reduction setup
    // multiplier = ceil(2^(16+shift) / divisor)

basis_div(a: i16, bc: BarrettConst) -> VDR16
    wide: i32 = @as(i32, a) * bc.multiplier
    v: i16 = @truncate(wide >> (16 + bc.shift))
    r: i16 = a - v * @truncate(divisor)   // exact remainder
    return VDR16{ .v = v, .r = r }
```

Used for softmax normalization (divide by sum of exponentials) and mean computation (divide by sequence length).

### 3.5 dot_product

The critical operation: dot product of Vec16 with accumulation in `i32`.

```
dot_q16(a: Vec16(N), b: Vec16(N)) -> VDR16
    acc: i32 = 0
    for (0..N) |i| {
        acc += @as(i32, a.v[i]) * @as(i32, b.v[i])
    }
    // rebase i32 accumulator to Q16
    v: i16 = @truncate(acc >> 16)
    r: i16 = @truncate(acc & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

For weight × activation (i8 × i16):

```
dot_w8_q16(w: [N]i8, a: Vec16(N)) -> VDR16
    acc: i32 = 0
    for (0..N) |i| {
        acc += @as(i32, w[i]) * @as(i32, a.v[i])
    }
    v: i16 = @truncate(acc >> 16)
    r: i16 = @truncate(acc & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

Accumulation in `i32` gives 16 bits of headroom. For dot products of length 4 (DIM=4), the maximum accumulation is `4 × 32767 × 32767 ≈ 4.3 × 10^9`, which fits `i32` (max 2.1 × 10^9)... no, that overflows.

Problem: `4 × 32767^2 = 4,294,443,012` which exceeds `i32` max of `2,147,483,647`. Need `i64` accumulator for i16 × i16 dot products even at length 4.

Corrected:

```
dot_q16(a: Vec16(N), b: Vec16(N)) -> VDR16
    acc: i64 = 0
    for (0..N) |i| {
        acc += @as(i64, a.v[i]) * @as(i64, b.v[i])
    }
    v: i16 = @intCast(acc >> 16)
    r: i16 = @intCast(acc & 0xFFFF)
    return VDR16{ .v = v, .r = r }
```

For i8 × i16 (weight × activation), max is `4 × 127 × 32767 ≈ 16.6 × 10^6`, fits `i32` comfortably. The i8 × i16 path stays in `i32`.

---

## 4. SIMD Vectorization

At DIM=4, SIMD is overkill — scalar loops will autovectorize or just run fast. But the kernels should be written in a form that scales to DIM=128+.

For the toy model, the SIMD path is optional. The scalar kernels above are sufficient. The Zig `@Vector` version for the dot product:

```
dot_q16_simd(a: @Vector(4, i16), b: @Vector(4, i16)) -> VDR16
    wide: @Vector(4, i32) = @as(@Vector(4, i32), a) * @as(@Vector(4, i32), b)
    acc: i64 = @reduce(.Add, @as(@Vector(4, i64), wide))
    return VDR16{ .v = @intCast(acc >> 16), .r = @intCast(acc & 0xFFFF) }
```

This is the pattern. For the toy, scalar is fine. SIMD matters at DIM=4096.

---

## 5. Lookup Tables

### 5.1 Softmax Exponential Table

The Python toy uses a quadratic surrogate. The Zig toy can use either:

**Option A: Quadratic surrogate (no table).** Same as Python toy. `(x - shift)^2 / sum((x - shift)^2)`. Pure integer arithmetic: subtract, widening square, sum, Barrett divide. No table needed. Probabilities sum to 1 by the last-element correction.

**Option B: Exponential table.** Precomputed at Q335 in Python, projected to Q16. ~2048 entries for input range [-4, 4] in Q16 fixed point. Each entry is an `i16` V value. 4KB table, fits L1.

For the toy, Option A (quadratic surrogate) is the right choice: no table construction, no table validation, matches the Python reference, and the backward pass is simpler.

### 5.2 ReLU

Not a table. `relu(x) = if (x > 0) x else 0`. One comparison, one conditional move. The V and R slots are both zeroed for negative inputs.

```
relu_q16(x: VDR16) -> VDR16
    if (x.v > 0 or (x.v == 0 and x.r > 0)) return x
    return VDR16{ .v = 0, .r = 0 }
```

For the toy model where R is typically small or zero, checking just `x.v > 0` is sufficient for correctness in practice. The full check handles edge cases where V=0 but R>0.

---

## 6. Model Architecture

### 6.1 Constants

```
const VOCAB_SIZE = 5;
const DIM = 4;
const SEQ_LEN = 4;
const FFN_DIM = 8;
const N_HEADS = 1;
const D = 65536;          // 2^16
const N_EPOCHS = 20;
const SEED = 42;
```

Learning rate: `1/128` projected to Q16 = `65536 / 128 = 512`. Stored as `i16` value 512.

### 6.2 Model Struct

```
ToyTransformer {
    // Embeddings: i16 V values (closed, R=0)
    token_emb: [VOCAB_SIZE][DIM]i16
    pos_emb: [SEQ_LEN][DIM]i16

    // Attention projections: i8 weights + i16 bias
    wq_w: [DIM][DIM]i8
    wq_b: [DIM]i16
    wk_w: [DIM][DIM]i8
    wk_b: [DIM]i16
    wv_w: [DIM][DIM]i8
    wv_b: [DIM]i16
    wo_w: [DIM][DIM]i8
    wo_b: [DIM]i16

    // FFN: i8 weights + i16 bias
    ffn1_w: [FFN_DIM][DIM]i8
    ffn1_b: [FFN_DIM]i16
    ffn2_w: [DIM][FFN_DIM]i8
    ffn2_b: [DIM]i16

    // Output projection: i8 weights + i16 bias
    out_w: [VOCAB_SIZE][DIM]i8
    out_b: [VOCAB_SIZE]i16

    // Gradient accumulators: i32 (double width of weights)
    wq_w_grad: [DIM][DIM]i32
    wq_b_grad: [DIM]i32
    // ... same pattern for all weight matrices ...
    // Total: 14 gradient arrays mirroring the 14 weight/bias arrays

    // Forward cache for backward pass
    cache: ForwardCache
}
```

### 6.3 ForwardCache

```
ForwardCache {
    // Input
    token_ids: [SEQ_LEN]u8

    // Post-embedding
    embedded: [SEQ_LEN]Vec16(DIM)

    // Attention intermediates
    Q: [SEQ_LEN]Vec16(DIM)
    K: [SEQ_LEN]Vec16(DIM)
    V_proj: [SEQ_LEN]Vec16(DIM)
    scores: [SEQ_LEN][SEQ_LEN]i16        // attention scores, V only
    shifted: [SEQ_LEN][SEQ_LEN]i16       // scores after shift (for surrogate backward)
    weights: [SEQ_LEN][SEQ_LEN]i16       // softmax output, V only
    attn_out: [SEQ_LEN]Vec16(DIM)
    post_attn: [SEQ_LEN]Vec16(DIM)       // after Wo projection
    post_attn_res: [SEQ_LEN]Vec16(DIM)   // after residual add

    // FFN intermediates
    ffn_hidden: [SEQ_LEN]Vec16(FFN_DIM)  // after ffn1 + relu
    ffn_pre_relu: [SEQ_LEN]Vec16(FFN_DIM) // before relu (for backward)
    ffn_out: [SEQ_LEN]Vec16(DIM)         // after ffn2
    post_ffn_res: [SEQ_LEN]Vec16(DIM)    // after residual add

    // Output
    logits: [SEQ_LEN]Vec16(VOCAB_SIZE)
}
```

Total cache size: approximately `4 × 4 × 2 × 15 ≈ 480` bytes for V arrays plus the same for R. Under 1KB total. Entire model + cache + gradients fits in L1.

### 6.4 Weight Initialization

Same LCG as Python toy:

```
lcg_next(state: *u32) -> u32
    state.* = state.* *% 1103515245 +% 12345
    state.* &= 0x7FFFFFFF
    return state.*

init_i8(out: []i8, state: *u32, scale: i8)
    for (out) |*val| {
        raw = lcg_next(state)
        val.* = @intCast(@as(i32, @intCast(raw % (@as(u32, @intCast(2 * scale + 1))))) - scale)
    }

init_i16(out: []i16, state: *u32, scale: i16)
    for (out) |*val| {
        raw = lcg_next(state)
        // project to Q16: val/scale * 65536
        int_val = @intCast(@as(i32, @intCast(raw % (@as(u32, @intCast(2 * scale + 1))))) - scale)
        val.* = @intCast(@as(i32, int_val) * @divTrunc(65536, scale))
    }
```

Scale=4 matches the Python toy. Values in [-4, 4] projected to Q16: `val * 16384`. Fits `i16` since `4 * 16384 = 65536` which is exactly `i16` max + 1... needs clamping or scale=3 to stay in range.

Adjusted: scale=3, values in [-3, 3], projected as `val * 21845` (65536/3). Max is `3 * 21845 = 65535`, fits unsigned `u16` but not signed `i16` (max 32767). Use `val * 8192` (65536/8) with scale=4 instead: max `4 * 8192 = 32768`, just barely overflows. Use `val * 8191`: max `4 * 8191 = 32764`, fits.

For i8 weights: values in [-4, 4], stored directly as `i8`. No projection needed — the i8 values are the numerators, with implicit D=128 or interpreted as Q8 fixed point. When multiplied by Q16 activations, the product is in Q24 effective, rebased to Q16 by shifting right 8.

Simplification for the toy: store weights as `i16` at Q16 like activations. Skip the i8 optimization. This avoids the mixed-precision rebase logic entirely. The toy model has 181 parameters — the memory difference between i8 and i16 storage is 181 bytes. Not worth the complexity.

Revised model: all weights `i16` at Q16, all activations `i16` at Q16, all gradients `i32`, all accumulators `i64`.

---

## 7. Forward Pass

### 7.1 Embedding

```
embed(model: *ToyTransformer, token_ids: [SEQ_LEN]u8) -> void
    for (0..SEQ_LEN) |pos| {
        tid = token_ids[pos]
        for (0..DIM) |d| {
            // token + positional, both Q16
            sum = @as(i32, model.token_emb[tid][d]) + @as(i32, model.pos_emb[pos][d])
            model.cache.embedded[pos].v[d] = @intCast(sum & 0xFFFF)
            model.cache.embedded[pos].r[d] = 0  // clean addition, no remainder expected at toy scale
        }
    }
```

### 7.2 Linear Projection

```
linear_forward(
    weight: [ROWS][COLS]i16,
    bias: [ROWS]i16,
    input: Vec16(COLS),
    output: *Vec16(ROWS),
) -> void
    for (0..ROWS) |i| {
        acc: i64 = 0
        for (0..COLS) |j| {
            acc += @as(i64, weight[i][j]) * @as(i64, input.v[j])
        }
        // rebase i64 accumulator to Q16
        output.v[i] = @intCast((acc >> 16) & 0xFFFF)
        output.r[i] = @intCast(acc & 0xFFFF)
        // add bias
        sum = @as(i32, output.v[i]) + @as(i32, bias[i])
        output.v[i] = @intCast(sum & 0xFFFF)
        // bias remainder discarded at toy scale
    }
```

The `acc >> 16` is the divmod by D. Upper bits are V, lower 16 bits are R. One shift, one mask. This is the entire basis-frame multiply-accumulate epilogue.

### 7.3 Attention Scores

```
attention_scores(Q: [N]Vec16(DIM), K: [N]Vec16(DIM), scores: *[N][N]i16) -> void
    for (0..N) |i| {
        for (0..N) |j| {
            if (j > i) {
                scores[i][j] = -32768  // causal mask: minimum i16
                continue
            }
            acc: i64 = 0
            for (0..DIM) |d| {
                acc += @as(i64, Q[i].v[d]) * @as(i64, K[j].v[d])
            }
            scores[i][j] = @intCast((acc >> 16) & 0xFFFF)
        }
    }
```

### 7.4 Quadratic Softmax Surrogate

```
softmax_surrogate(
    scores: [N]i16,
    probs: *[N]i16,
    shifted_out: *[N]i16,
) -> void
    // find min for shift
    min_val: i16 = scores[0]
    for (1..N) |i| {
        if (scores[i] < min_val) min_val = scores[i]
    }

    // compute (x - shift)^2, accumulate sum
    sum_sq: i64 = 0
    var shifted: [N]i16 = undefined
    var squares: [N]i64 = undefined
    for (0..N) |i| {
        shifted[i] = scores[i] - min_val
        shifted_out[i] = shifted[i]
        sq = @as(i64, shifted[i]) * @as(i64, shifted[i])
        squares[i] = sq
        sum_sq += sq
    }

    if (sum_sq == 0) {
        // uniform: 65536 / N per element
        for (0..N) |i| {
            probs[i] = @intCast(@divTrunc(@as(i64, D), N))
        }
        return
    }

    // compute N-1 probabilities, last = D - sum(first N-1)
    var running: i64 = 0
    for (0..N-1) |i| {
        p = @divTrunc(squares[i] * D, sum_sq)
        probs[i] = @intCast(p)
        running += p
    }
    probs[N-1] = @intCast(D - running)  // guarantees sum = D = 65536 exactly
```

Probabilities stored as `i16` where the value represents `prob / 65536`. Sum of all probs is exactly 65536 (= D), which means the rational probabilities sum to exactly 1. Same last-element correction as the Python toy.

### 7.5 Weighted Sum (Attention Mix)

```
attention_mix(
    weights: [N][N]i16,
    V: [N]Vec16(DIM),
    output: *[N]Vec16(DIM),
) -> void
    for (0..N) |i| {
        for (0..DIM) |d| {
            acc: i64 = 0
            for (0..N) |j| {
                acc += @as(i64, weights[i][j]) * @as(i64, V[j].v[d])
            }
            // rebase to Q16
            output[i].v[d] = @intCast((acc >> 16) & 0xFFFF)
            output[i].r[d] = @intCast(acc & 0xFFFF)
        }
    }
```

### 7.6 ReLU

```
relu(input: *Vec16(N)) -> void
    for (0..N) |i| {
        if (input.v[i] < 0) {
            input.v[i] = 0
            input.r[i] = 0
        }
    }
```

In-place. Negative values zeroed entirely (V and R).

### 7.7 Residual Add

```
residual_add(a: Vec16(N), b: Vec16(N), output: *Vec16(N)) -> void
    for (0..N) |i| {
        sum = @as(i32, a.v[i]) + @as(i32, b.v[i])
        output.v[i] = @intCast(sum & 0xFFFF)
        output.r[i] = 0  // no carry at toy scale
    }
```

### 7.8 Full Forward Pass

```
forward(model: *ToyTransformer, token_ids: [SEQ_LEN]u8) -> void
    embed(model, token_ids)

    // Q, K, V projections
    for (0..SEQ_LEN) |pos| {
        linear_forward(model.wq_w, model.wq_b, model.cache.embedded[pos], &model.cache.Q[pos])
        linear_forward(model.wk_w, model.wk_b, model.cache.embedded[pos], &model.cache.K[pos])
        linear_forward(model.wv_w, model.wv_b, model.cache.embedded[pos], &model.cache.V_proj[pos])
    }

    // Attention scores + softmax
    attention_scores(model.cache.Q, model.cache.K, &model.cache.scores)
    for (0..SEQ_LEN) |i| {
        softmax_surrogate(model.cache.scores[i], &model.cache.weights[i], &model.cache.shifted[i])
    }

    // Attention mix + Wo projection
    attention_mix(model.cache.weights, model.cache.V_proj, &model.cache.attn_out)
    for (0..SEQ_LEN) |pos| {
        linear_forward(model.wo_w, model.wo_b, model.cache.attn_out[pos], &model.cache.post_attn[pos])
        residual_add(model.cache.embedded[pos], model.cache.post_attn[pos], &model.cache.post_attn_res[pos])
    }

    // FFN
    for (0..SEQ_LEN) |pos| {
        linear_forward(model.ffn1_w, model.ffn1_b, model.cache.post_attn_res[pos], &model.cache.ffn_pre_relu[pos])
        model.cache.ffn_hidden[pos] = model.cache.ffn_pre_relu[pos]
        relu(&model.cache.ffn_hidden[pos])
        linear_forward(model.ffn2_w, model.ffn2_b, model.cache.ffn_hidden[pos], &model.cache.ffn_out[pos])
        residual_add(model.cache.post_attn_res[pos], model.cache.ffn_out[pos], &model.cache.post_ffn_res[pos])
    }

    // Output projection
    for (0..SEQ_LEN) |pos| {
        linear_forward(model.out_w, model.out_b, model.cache.post_ffn_res[pos], &model.cache.logits[pos])
    }
```

---

## 8. Backward Pass

### 8.1 Gradient Types

All gradients are `i32` to prevent overflow during accumulation. Weight gradients are the same shape as weights but `i32`. After the backward pass, they are rebased to `i16` for the weight update.

### 8.2 Linear Backward

```
linear_backward(
    weight: [ROWS][COLS]i16,
    weight_grad: *[ROWS][COLS]i32,
    bias_grad: *[ROWS]i32,
    input: Vec16(COLS),
    grad_output: [ROWS]i32,
    grad_input: *[COLS]i32,
) -> void
    // grad_input = W^T @ grad_output
    for (0..COLS) |j| {
        acc: i64 = 0
        for (0..ROWS) |i| {
            acc += @as(i64, weight[i][j]) * @as(i64, grad_output[i])
        }
        grad_input[j] = @intCast(acc >> 16)
    }

    // weight_grad += outer(grad_output, input)
    for (0..ROWS) |i| {
        for (0..COLS) |j| {
            prod = @as(i64, grad_output[i]) * @as(i64, input.v[j])
            weight_grad[i][j] += @intCast(prod >> 16)
        }
    }

    // bias_grad += grad_output
    for (0..ROWS) |i| {
        bias_grad[i] += grad_output[i]
    }
```

### 8.3 Softmax Surrogate Backward

```
softmax_surrogate_backward(
    grad_probs: [N]i32,
    probs: [N]i16,
    shifted: [N]i16,
    grad_scores: *[N]i32,
) -> void
    // sum_sq from shifted values
    sum_sq: i64 = 0
    for (0..N) |i| {
        sum_sq += @as(i64, shifted[i]) * @as(i64, shifted[i])
    }

    if (sum_sq == 0) {
        for (0..N) |i| grad_scores[i] = 0
        return
    }

    // dot(grad_probs, probs)
    dot_gp: i64 = 0
    for (0..N) |i| {
        dot_gp += @as(i64, grad_probs[i]) * @as(i64, probs[i])
    }

    // grad_scores[i] = 2 * shifted[i] / sum_sq * (grad_probs[i] - dot_gp / D)
    for (0..N) |i| {
        diff = @as(i64, grad_probs[i]) * D - dot_gp
        numer = 2 * @as(i64, shifted[i]) * diff
        grad_scores[i] = @intCast(@divTrunc(numer, sum_sq))
    }
```

### 8.4 ReLU Backward

```
relu_backward(pre_relu: Vec16(N), grad_output: [N]i32, grad_input: *[N]i32) -> void
    for (0..N) |i| {
        if (pre_relu.v[i] > 0) {
            grad_input[i] = grad_output[i]
        } else {
            grad_input[i] = 0
        }
    }
```

### 8.5 Full Backward Pass

Mirrors forward in reverse. Starts from gradient of MSE loss on last position logits, backpropagates through output projection, residual, FFN, residual, attention block, embedding. Each `linear_backward` accumulates into the corresponding `weight_grad` and `bias_grad` arrays.

The structure follows the Python toy's `backward_from_last` exactly, but all operations are integer shifts and multiplies instead of VDR object method calls.

---

## 9. Training Loop

### 9.1 MSE Loss

```
mse_loss(pred: [VOCAB_SIZE]i16, target: [VOCAB_SIZE]i16) -> i32
    total: i64 = 0
    for (0..VOCAB_SIZE) |i| {
        diff = @as(i32, pred[i]) - @as(i32, target[i])
        total += @as(i64, diff) * @as(i64, diff)
    }
    return @intCast(@divTrunc(total, VOCAB_SIZE))
```

### 9.2 MSE Gradient

```
mse_grad(pred: [VOCAB_SIZE]i16, target: [VOCAB_SIZE]i16, grad: *[VOCAB_SIZE]i32) -> void
    for (0..VOCAB_SIZE) |i| {
        diff = @as(i32, pred[i]) - @as(i32, target[i])
        grad[i] = @divTrunc(2 * diff, VOCAB_SIZE)
    }
```

### 9.3 SGD Update

```
sgd_step(weight: []i16, grad: []i32, lr: i16) -> void
    for (0..weight.len) |i| {
        // w = w - lr * grad
        // lr is Q16, grad is Q16-scaled i32
        update = @as(i64, lr) * @as(i64, grad[i])
        update_q16 = @intCast(update >> 16)   // rebase to Q16
        weight[i] -= @intCast(update_q16)
    }
```

### 9.4 One-Hot Target

```
one_hot(target_id: u8, out: *[VOCAB_SIZE]i16) -> void
    for (0..VOCAB_SIZE) |i| {
        out[i] = if (i == target_id) D else 0   // D = 65536 = "1.0" in Q16
    }
```

Wait — `D = 65536` overflows `i16` (max 32767). The value "1.0" in Q16 signed is not representable as `i16`. This is a fundamental issue with signed Q16.

Options:

**Option A:** Use `u16` for probabilities and one-hot targets. "1.0" = 65536... still overflows `u16` (max 65535).

**Option B:** Use Q15 interpretation for probabilities: "1.0" = 32768 (or 32767). D = 32768.

**Option C:** Store one-hot targets and probabilities as `i32`. The loss and gradient computation already uses `i32`.

Option C is simplest for the toy:

```
one_hot(target_id: u8, out: *[VOCAB_SIZE]i32) -> void
    for (0..VOCAB_SIZE) |i| {
        out[i] = if (i == target_id) 65536 else 0
    }
```

Probabilities from softmax are `i16` (max 32767 per element, sum = 65536 stored across elements). The MSE compares `i16` probs against `i32` targets, widening the probs to `i32` for the subtraction.

### 9.5 Training Step

```
train_step(model: *ToyTransformer, context: [SEQ_LEN]u8, target_id: u8, lr: i16) -> i32
    // forward
    forward(model, context)

    // softmax on last position logits
    var probs: [VOCAB_SIZE]i16 = undefined
    var shifted: [VOCAB_SIZE]i16 = undefined
    softmax_surrogate(model.cache.logits[SEQ_LEN-1].v, &probs, &shifted)

    // one-hot target
    var target: [VOCAB_SIZE]i32 = undefined
    one_hot(target_id, &target)

    // MSE loss
    loss = mse_loss_i16_i32(probs, target)

    // MSE gradient
    var grad_logits: [VOCAB_SIZE]i32 = undefined
    mse_grad_i16_i32(probs, target, &grad_logits)

    // backward through softmax surrogate
    var grad_scores: [VOCAB_SIZE]i32 = undefined
    softmax_surrogate_backward(grad_logits, probs, shifted, &grad_scores)

    // zero all gradients
    zero_all_grads(model)

    // backward through model
    backward_from_last(model, grad_scores)

    // SGD step on all parameters
    sgd_step_all(model, lr)

    return loss
```

### 9.6 Epoch Loop

```
train_epoch(model: *ToyTransformer, windows: []Window, lr: i16) -> i64
    total_loss: i64 = 0
    for (windows) |w| {
        loss = train_step(model, w.context, w.target, lr)
        total_loss += loss
    }
    return @divTrunc(total_loss, windows.len)
```

---

## 10. Text Generation

### 10.1 Greedy Decoding

```
sample_greedy(probs: [VOCAB_SIZE]i16) -> u8
    best: u8 = 0
    best_val: i16 = probs[0]
    for (1..VOCAB_SIZE) |i| {
        if (probs[i] > best_val) {
            best_val = probs[i]
            best = @intCast(i)
        }
    }
    return best
```

### 10.2 Categorical Sampling

```
sample_categorical(probs: [VOCAB_SIZE]i16, rng: *LCG) -> u8
    // CDF comparison against uniform random in [0, D)
    u = @intCast(lcg_next(rng) & 0xFFFF)  // random i16
    cumsum: i32 = 0
    for (0..VOCAB_SIZE) |i| {
        cumsum += probs[i]
        if (u < cumsum) return @intCast(i)
    }
    return VOCAB_SIZE - 1
```

### 10.3 Generate Loop

```
generate(model: *ToyTransformer, prompt: [SEQ_LEN]u8, max_tokens: usize, output: []u8) -> usize
    var ids: [SEQ_LEN + max_tokens]u8 = undefined
    @memcpy(ids[0..SEQ_LEN], &prompt)
    var len: usize = SEQ_LEN

    for (0..max_tokens) |_| {
        context = ids[len - SEQ_LEN..len]
        forward(model, context[0..SEQ_LEN].*)
        var probs: [VOCAB_SIZE]i16 = undefined
        var shifted: [VOCAB_SIZE]i16 = undefined
        softmax_surrogate(model.cache.logits[SEQ_LEN-1].v, &probs, &shifted)
        next_id = sample_greedy(probs)
        ids[len] = next_id
        len += 1
    }

    @memcpy(output, ids[0..len])
    return len
```

---

## 11. Data Pipeline

### 11.1 Vocabulary

Hardcoded for the toy:

```
const vocab = [_][]const u8{ "the", "cat", "sat", "on", "mat" };
// the=0, cat=1, sat=2, on=3, mat=4

const corpus = [_]u8{ 0, 1, 2, 3, 0, 4 };  // "the cat sat on the mat"
```

### 11.2 Training Windows

```
const Window = struct {
    context: [SEQ_LEN]u8,
    target: u8,
};

const windows = [_]Window{
    .{ .context = .{ 0, 1, 2, 3 }, .target = 0 },  // "the cat sat on" -> "the"
    .{ .context = .{ 1, 2, 3, 0 }, .target = 4 },  // "cat sat on the" -> "mat"
};
```

---

## 12. Verification

### 12.1 Softmax Sum

After every softmax call, verify `sum(probs) == D`:

```
verify_softmax_sum(probs: [N]i16) -> bool
    total: i32 = 0
    for (0..N) |i| total += probs[i]
    return total == D
```

This is exact — no tolerance. The last-element correction guarantees it.

### 12.2 Determinism

Run the full training loop twice from the same seed. Compare all weights byte-by-byte. Must be identical.

### 12.3 Weight Update

Save weight before step, compute step, verify `(w_old - w_new) == (lr * grad) >> 16` exactly.

### 12.4 D Stability

Not applicable in the same sense as Python — there is no D field to check. Every value is an `i16`, and the frame is implicit (always Q16). D stability is guaranteed by construction: the shift-and-mask epilogue always produces `i16` output. There is no path that can produce a different denominator.

---

## 13. Entry Point

```
pub fn main() !void
    var model = ToyTransformer.init(SEED)

    // train
    for (0..N_EPOCHS) |epoch| {
        avg_loss = train_epoch(&model, &windows, LR)
        print("epoch {d}: loss={d}\n", .{epoch + 1, avg_loss})
    }

    // generate
    var output: [20]u8 = undefined
    len = generate(&model, .{0, 1, 2, 3}, 4, &output)
    print_tokens(output[0..len])

    // verify
    assert(verify_determinism())
    assert(verify_softmax_sums())
    print("all checks passed\n")
```

---

## 14. File Structure

Single file: `toy_llm.zig`. Everything above in one compilation unit. No build system beyond `zig build-exe toy_llm.zig`. Target: any CPU, no SIMD required (scalar loops autovectorize where beneficial).

Expected binary size: ~20KB. Expected runtime: under 100ms for full train + generate + verify. Expected memory: under 4KB total (model + cache + gradients).

---

## 15. Validation Against Python Reference

The Zig implementation must produce results that are consistent with the Python toy at the precision boundary. They will not be bit-identical because D = 2^16 (Zig) vs D = 2^32 (Python) gives different precision floors. But:

- Same corpus, same windows, same vocabulary mapping
- Same LCG seed produces same initialization sequence
- Loss should decrease monotonically for 20 epochs in both
- Greedy generation should produce "sat" as dominant prediction in both
- Softmax sums to exactly D in Zig (65536) and within 10^-9 of 1 in Python

The cross-validation test: initialize both implementations with the same seed, run one forward pass on the same input, compare logits at reduced precision (round both to 4 decimal places). They should agree.
