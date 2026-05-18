Let's walk through the actual operations.

## Matmul — the dominant cost

**Float32 path:**
```
accumulator = 0.0
for each k:
    accumulator += a[k] * b[k]    // fmul + fadd, or FMA
```
One FMA per element. That's the baseline.

**VDR i16 weight × i32 activation path:**
```
for each k:
    product = @as(i64, a[k].v) * @as(i64, b[k].v)   // integer multiply, widening
    acc_v += product >> ACTIVATION_BITS                 // shift = quotient
    acc_r += product & ACTIVATION_MASK                  // mask = remainder
```

That's one integer multiply, one shift, one mask, two adds. No division anywhere. The shift and mask are the divmod — free on any hardware.

**Comparison:** Float FMA is one cycle on modern hardware. The VDR path is roughly 4-5 integer ops. But integer multiply throughput on modern SIMD is comparable to float FMA. And i16 × i32 packs tighter than f32 × f32 — you fit more elements per cache line, more per register.

So matmul is maybe 2-3× integer ops but with better memory density. Depending on whether you're compute-bound or memory-bound, VDR could actually be faster for weight-limited inference. Current INT8 inference already beats FP32 for exactly this reason — smaller elements, more throughput per byte loaded.

## Softmax

**Float path:**
```
max = find_max(logits)
for each i:
    out[i] = exp(logits[i] - max)      // transcendental function
sum = reduce_add(out)
for each i:
    out[i] /= sum                       // float divide
```

exp() is expensive. 10-20 cycles or a lookup table approximation. The division at the end is another 10+ cycles. And the sum is not exactly 1.

**VDR path:**
```
for each i:
    out[i].v = exp_table[logits[i].v]   // table lookup, precomputed exact
    out[i].r = exp_remainder[logits[i].v]
sum_v = reduce_add(out.v)
sum_r = reduce_add(out.r)
// normalize: each out[i] / sum
// this is integer divmod against the sum
```

The exp becomes a table lookup because the inputs are bounded integers at fixed precision. You precompute the exact VDR expansion of exp for every possible input value in the Q16 or Q32 range. No transcendental function at runtime. The table fits in cache for Q16 — 65536 entries × 4 bytes = 256KB.

That's potentially much faster than float softmax. The transcendental disappears entirely.

## Accumulation over long chains — where VDR wins outright

**Float path for diffusion (1000 steps):**
```
for each step:
    x = sqrt_alpha_bar[t] * x + sqrt_one_minus[t] * eps
    // each multiply: ~0.5 ULP error
    // each add: ~0.5 ULP error
    // after 1000 steps: ~1000 ULP accumulated drift
```

**VDR path:**
```
for each step:
    prod = @as(i64, sqrt_ab[t].v) * @as(i64, x.v)
    x.v = @intCast(i32, prod >> DIFFUSION_BITS)
    x.r = @intCast(i32, prod & DIFFUSION_MASK)
    // remainder from step N feeds into step N+1
    // zero information lost, zero drift, forever
```

Same number of operations. Same throughput. But after a million steps the float version has drifted measurably and the VDR version has not drifted at all. The per-step cost is identical — the correctness comes free.

## Memory bandwidth

This is where VDR might actually win on net performance.

| Type | Bytes per element | Elements per cache line |
|---|---|---|
| f32 | 4 | 16 |
| Vdr16 (v+r) | 4 | 16 |
| Vdr32 (v+r) | 8 | 8 |
| f16 | 2 | 32 |

Vdr16 is the same density as f32. You get exact arithmetic at the same memory bandwidth. Vdr32 is 2× f32 but carries the remainder — so you're comparing against f32 that silently drops information vs Vdr32 that keeps it.

For memory-bound workloads (which most inference is), Vdr16 weights at f32-equivalent bandwidth with zero precision loss is a strict improvement.

## The summary

| Operation | Float | VDR fixed-basis | VDR cost |
|---|---|---|---|
| Multiply | 1 FMA | 1 imul + shift + mask + 2 add | ~2-3× ops, but tighter packing |
| Softmax exp | 10-20 cycles transcendental | table lookup | faster |
| Accumulation drift | grows with chain length | zero, forever | same cost |
| Memory per weight | 4 bytes (f32) or 2 (f16) | 4 bytes (Vdr16) | same as f32 |
| Normalization check | approximate (hope sum ≈ 1) | exact (sum_v == D) | free |
| Division | 10+ cycle fdiv | shift + mask | faster |

The honest answer: per-op arithmetic is roughly 2-3× more integer operations than float FMA. But transcendentals become table lookups (faster), division becomes bit shifts (faster), memory density at Q16 matches f32 (same), and accumulated error over chains is zero (free correctness).

For inference — memory-bound, weight-dominated, long-chain diffusion — VDR on fixed power-of-two basis in Zig might not just be competitive with float. It might be faster, because the expensive float operations (exp, div, sqrt) all collapse into integer operations or precomputed tables, while the cheap float operation (FMA) becomes a slightly more expensive but still cheap integer sequence.

The Python 50-200× overhead was never about the math. It was about Python.
