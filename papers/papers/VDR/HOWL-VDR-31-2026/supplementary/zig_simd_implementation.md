# VDR-Zig CPU SIMD Implementation Vectors

## Scope

This report identifies the implementation vectors for a Zig CPU SIMD implementation of the VDR fixed-basis arithmetic system described in HOWL-VDR-29-2026. Each vector is a self-contained line of work that produces a testable artifact. Vectors are ordered by dependency — each one unlocks the next, but lateral vectors can be parallelized where noted.

---

## Vector 1: Scalar Kernel Primitives

The foundation. Every subsequent vector calls these.

The core operation is basis multiply: two V slots in, one V and one R out. At Q16 (D=2^16), this is `i16 × i16 → i32`, then split: upper 16 bits are the new V, lower 16 bits are R. In Zig this is a widening multiply, a right shift by 16, and a bitwise AND with 0xFFFF. Three operations, no branching.

The full set of scalar kernels:

- **basis_mul_q16**: i16 × i16 → (i16 V, i16 R). The workhorse for activation-activation operations.
- **basis_mul_q8_q16**: i8 × i16 → (i16 V, i16 R). Weight × activation. The widening multiply produces i24 effective, which fits i32. Split point depends on target basis — if accumulating into Q32, shift by 16 after the full dot product, not per element.
- **basis_mul_q32**: i32 × i32 → (i32 V, i32 R). Schedule constants, accumulator operations.
- **basis_mul_q64**: i64 × i64 → (i64 V, i64 R). Gradient accumulation. Needs `@mulWithOverflow` or u128 intermediate.
- **basis_add_q16**: i16 + i16 with carry detection. If the addition overflows i16, the overflow goes to R. This is the one operation where float is simpler (single add vs add-check-carry), but it's less than 0.1% of pipeline compute.
- **basis_div_barrett_q16**: Division via precomputed multiplicative inverse. One multiply, one shift. The inverse is computed once per divisor at init time.
- **rebase_q32_to_q16**: Right shift 16, mask low 16. Produces V and R at Q16 from a Q32 accumulator. This is the matmul epilogue operation.
- **rebase_q16_to_q64**: Sign extension. One instruction. This is the backward pass entry point.

Each kernel gets a test that round-trips against a Python VDR reference or against the mathematical definition (product = V×D + R, exactly). These tests are the ground truth for everything else.

---

## Vector 2: SIMD Vectorization of Scalar Kernels

Zig exposes SIMD via `@Vector(N, T)`. On AVX-512, N=32 for i16, N=64 for i8, N=16 for i32.

The key insight from the paper (P6) is deinterleaved layout. V values are contiguous in one array, R values contiguous in another. A single `vmovdqu16` loads 32 activation V values into one ZMM register. No gather, no shuffle, no permute.

The critical SIMD kernel is the matmul inner loop. The paper (OC1) identifies `vpmaddwd` as the core instruction: it takes 32 i16 values from each of two registers, multiplies pairwise, and adds adjacent pairs to produce 16 i32 results. This is the fused multiply-accumulate for VDR. Accumulate in i32 across the reduction dimension K, then apply the shift-and-mask epilogue (rebase Q32→Q16) once per output element.

The vectorization order follows compute dominance:

1. **GEMM inner loop** (vpmaddwd path). This is 70%+ of forward pass compute. The i8 weight × i16 activation path uses `vpmaddubsw` (unsigned×signed byte multiply-add to word) if weights are stored unsigned-offset, or widening to i16 first. The paper assumes the latter for clarity but the former is one instruction.
2. **Softmax** (table gather). Load logits as i16, find max via horizontal reduce, subtract (shift), use the shifted value as index into a lookup table stored in memory. The table maps i16 input → i16 output (V and R). The gather is `vpgatherdd` or, for sequential access patterns, just indexed loads. Barrett division for the normalization denominator.
3. **GeLU/SiLU** (table lookup). Same pattern as softmax but simpler — one table, no normalization. The paper estimates 5-10× over float because you replace a polynomial chain with a single load.
4. **Layer norm** (integer reduction + table rsqrt). Sum and sum-of-squares via integer reduction. Mean via right shift if hidden dim is power of two (it almost always is — 4096, 8192). Reciprocal square root via table lookup on the variance. The table is larger (~40KB at Q16) but fits L2 comfortably.
5. **Residual add**. Vectorized add with carry propagation. Lowest priority because it's trivial compute.

Each SIMD kernel gets tested against the scalar kernel on the same inputs. Bit-identical results required — this is the whole point.

---

## Vector 3: Memory Layout and Tile Management

The deinterleaved layout means a matrix of activations is stored as two separate row-major arrays: one for V, one for R. A `WeightMat` (Z4) stores only V (i8), no R, because frozen inference weights are closed (R=0).

The tiling strategy for GEMM follows cache hierarchy. On a typical CPU with 32KB L1d, 256KB-1MB L2:

- Weight tile: 128×32 at i8 = 4KB. Fits L1.
- Activation tile: 32×128 at i16 = 8KB for V. Fits L1 alongside weight tile.
- Accumulator: 128×128 at i32 = 64KB. Lives in L2 during accumulation, written back as Q16 (V+R) after epilogue.

The R array for activations is read during backward pass and during any operation that needs the full precision chain. During forward inference, some operations (GEMM accumulation) only read V and produce new R — the old R is consumed only if you're tracking remainder propagation through the full chain. For inference without remainder tracking, the R array is write-only during GEMM, which halves the read bandwidth for activations.

The tile sizes above give the paper's SM1-SM3 numbers adapted for CPU cache instead of GPU shared memory. The key constraint is: weight tile + activation tile + lookup tables must fit L1+L2 simultaneously. At the sizes above, ~12KB for tiles leaves ~20KB+ in L1 for the hot lookup table (softmax exp or GeLU), with the full 256KB table in L2 for cold entries.

This vector produces the `ActivationMat` and `WeightMat` structs, allocation functions, and the tiling iterator that walks the matrix in cache-friendly order.

---

## Vector 4: Lookup Table Construction and Validation

The tables are computed once, offline. The construction pipeline:

1. Define the input domain. For softmax exp at Q16 with bounded input range [-8, 8] in fixed point, that's roughly 2048-8192 entries depending on how fine the grid is.
2. Compute exact output at Q335 (arbitrary precision). The Python VDR library already does this.
3. Project Q335 result to target basis via divmod. This produces the V and R values that go in the table.
4. Store as two arrays: V table and R table (deinterleaved, matching the activation layout convention).
5. Validate roundtrip: for every entry, verify that V×D + R equals the Q335 numerator projected to the target frame.

The tables are immutable compile-time artifacts. In Zig, they're `comptime` arrays or embedded read-only data. No runtime computation, no initialization cost.

Three tables needed for a minimal transformer:

- Exponential (softmax): ~8KB at Q16 bounded. The paper (LT1) gives 2048 entries × 4 bytes = 8KB.
- GeLU: ~32KB at Q16 bounded (LT2). This is the largest and may need to live in L2 rather than L1.
- Reciprocal square root (layer norm): ~40KB at Q16 (LT3). The paper notes Q32 should use Newton iteration instead.

Barrett reduction constants are also precomputed here. For each possible divisor (sequence length for softmax normalization, hidden dim for mean), precompute the multiplicative inverse as a Q32 or Q64 value. There are very few unique divisors in a given model — sequence length, hidden dim, number of heads, vocabulary size. A handful of constants.

---

## Vector 5: Forward Pass Assembly

This vector composes the kernels from Vectors 1-4 into a complete forward pass for a single transformer layer.

The operation sequence for one layer, following the paper's architecture:

1. **Layer norm 1**: integer mean (sum + shift), integer variance (sum-of-squares + shift - mean²), rsqrt table lookup, scale and shift by gamma/beta. Input and output are Q16 activation matrices.
2. **QKV projection**: three GEMMs, weight Q8 × activation Q16 → accumulator Q32, epilogue rebase to Q16. Produces Q, K, V matrices.
3. **Attention scores**: Q × K^T, both Q16. This is i16×i16→i32 GEMM, rebase to Q16. Apply causal mask (set future positions to minimum i16 value before softmax).
4. **Softmax**: per-row max reduce, subtract, table lookup for exp, sum reduce, Barrett divide. Output Q16, guaranteed sum to 1 by the last-element correction (compute N-1 elements, last = D - sum of others).
5. **Attention output**: softmax weights × V matrix, Q16×Q16→Q32→Q16.
6. **Output projection**: GEMM Q8×Q16→Q32→Q16.
7. **Residual add**: input + attention output, Q16 with carry.
8. **Layer norm 2**: same as step 1.
9. **FFN up + gate**: two GEMMs Q8×Q16→Q32→Q16.
10. **GeLU**: table lookup on the gate output.
11. **FFN down**: GEMM Q8×Q16→Q32→Q16.
12. **Residual add**: input + FFN output.

The test for this vector is: run the same inputs through the Python VDR reference implementation and the Zig implementation, compare all intermediate activations for bit-identical results. Not approximate. Identical. If they differ anywhere, something is wrong — there's no tolerance in integer arithmetic.

---

## Vector 6: Backward Pass and Gradient Computation

The backward pass mirrors the forward pass in reverse. All gradients are computed in Q64 (i64 V + i64 R) to prevent overflow during accumulation across batch elements.

The key operations:

- **Gradient of GEMM**: outer product of upstream gradient × activation transpose, accumulated in Q64. This produces weight gradients.
- **Gradient of softmax**: the quadratic surrogate backward from the toy paper, or the standard Jacobian-vector product for exponential softmax (both are exact integer operations at Q64).
- **Gradient of GeLU**: table lookup on the input value to get the derivative, multiply by upstream gradient. The derivative table is constructed alongside the forward table in Vector 4.
- **Gradient of layer norm**: standard layer norm backward, all in integer arithmetic. The reciprocal square root and its derivative come from the table.
- **Gradient accumulation**: sum across batch dimension in Q64. The paper (OV3) confirms i64 is safe for batch sizes up to 2^32.

Rebase from Q64 gradient to Q8 weight update (RB5) is a right shift by 56 and mask. The remainder captures the 56 bits that didn't fit — this is where stochastic rounding or explicit remainder tracking across steps would go. For a first implementation, truncate the remainder (equivalent to round-toward-zero). This matches what every existing quantized training system does, except VDR tells you exactly what was truncated.

---

## Vector 7: Optimizer

SGD is trivial: `weight_new = weight_old - lr * gradient`, all in integer arithmetic with appropriate rebasing. The learning rate is a Q8 or Q16 constant, precomputed.

Adam is more interesting. The running mean and variance of gradients (m and v) accumulate in Q32 or Q64. The update rule involves division by (sqrt(v) + epsilon) — but epsilon is zero in VDR (no denormals to protect against) and sqrt is a table lookup or Newton iteration at Q32. The division is Barrett reduction.

The momentum coefficients (beta1, beta2) are Q16 constants projected from their exact rational values at init time. The bias correction terms (1 - beta^t) are precomputed for all t up to max training steps and stored as a Q32 table. This is a few KB for any practical training run.

---

## Vector 8: Diffusion Pipeline

This vector is lateral to Vectors 5-7 (can be built in parallel once Vectors 1-4 are done).

The diffusion schedule (Z9) is precomputed at Q335 and projected to Q32. Every beta, sqrt_alpha_bar, sqrt_one_minus_alpha_bar, and posterior variance is an exact i32 V + i32 R pair. The forward diffusion step is:

`x_t = sqrt_alpha_bar_t * x_0 + sqrt_one_minus_alpha_bar_t * noise`

Two multiplies and one add at Q16 (latent basis), with schedule constants rebased from Q32 to Q16 via shift+mask. The noise is integer noise generated from a deterministic PRNG, projected to Q16.

The reverse step is the same structure. The denoising network is a U-Net or DiT built from the same transformer blocks as Vector 5.

The test for this vector is the drift test: run 25 million chained diffusion steps, verify that the final latent is bit-identical across two runs. This is the test float cannot pass.

---

## Vector Dependencies

```
V1 (scalar) → V2 (SIMD) → V5 (forward)
                ↓              ↓
V3 (memory) → V5          V6 (backward) → V7 (optimizer)
                ↓
V4 (tables) → V5
                ↓
              V8 (diffusion, lateral from V1-V4)
```

V1 through V4 are the foundation. V5 is the first complete artifact that runs inference. V6 and V7 add training. V8 is the diffusion pipeline, buildable once V1-V4 exist.

---

## What's Not Covered

GPU kernels. That's a separate implementation vector set targeting CUDA integer tensor cores. The CPU SIMD path comes first because it's testable without GPU infrastructure, produces the reference implementation that GPU kernels are validated against, and runs real workloads at the throughput numbers from OC1-OC6 in the paper (1.3-1.6× faster than float for a full forward pass on AVX-512).

Multi-node distribution. Not needed for the first implementation. When it matters, VDR's associativity guarantee (VR1) means gradient reduction order is irrelevant — any allreduce topology produces identical results. That's a property you get for free from the arithmetic.

ONNX/framework interop. Irrelevant. The Zig implementation is the framework.
