## SIMD Cache Line Layout

A cache line is 64 bytes. Let's pack it.

**Float32 — 16 elements per cache line:**
```
| f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 | f32 |
  4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B    4B
```

**Vdr16 — 16 elements per cache line (same count):**
```
| v0 r0 | v1 r1 | v2 r2 | v3 r3 | v4 r4 | v5 r5 | v6 r6 | v7 r7 | v8 r8 | v9 r9 | v10 r10 | v11 r11 | v12 r12 | v13 r13 | v14 r14 | v15 r15 |
  2B 2B   2B 2B   2B 2B   2B 2B   2B 2B   2B 2B   2B 2B   2B 2B   2B 2B   2B 2B    2B  2B     2B  2B     2B  2B     2B  2B     2B  2B     2B  2B
```

Same element count. Same bandwidth. But now consider the SIMD register view.

## Deinterleaved Layout — Separate V and R Lanes

Interleaved v,r,v,r forces shuffle operations to separate them for arithmetic. Better layout:

```
Cache line 0 (V lane): | v0  | v1  | v2  | ... | v31 |   // 32 × i16 = 64 bytes
Cache line 1 (R lane): | r0  | r1  | r2  | ... | r31 |   // 32 × i16 = 64 bytes
```

Now a 512-bit AVX-512 register loads 32 V values in one instruction. Another register loads 32 R values. No shuffling. Pure vertical SIMD.

**Float32 on AVX-512:** 16 elements per register. One `vfmadd231ps` per cycle.

**VDR i16 on AVX-512:** 32 elements per register. That's 2× the lane count.

## Matmul — One Cache Line at a Time

**Float32 AVX-512 path:**
```
vmovaps      zmm0, [weight_ptr]         // load 16 f32 weights
vmovaps      zmm1, [activation_ptr]     // load 16 f32 activations
vfmadd231ps  zmm2, zmm0, zmm1          // 16 FMAs in one cycle
// throughput: 16 elements per cycle
```

**VDR i16 AVX-512 path:**
```
vmovdqu16    zmm0, [weight_v_ptr]       // load 32 i16 weight V values
vmovdqu16    zmm1, [activ_v_ptr]        // load 32 i16 activation V values
vpmaddwd     zmm2, zmm0, zmm1          // 32 i16×i16 → 16 i32 with pairwise add
// zmm2 now holds 16 i32 products
// these are full products — no information lost yet

// divmod: D is power of two, so:
vpsrad       zmm3, zmm2, BITS          // arithmetic right shift = quotient (V)
vpandd       zmm4, zmm2, zmm_mask      // AND with constant mask = remainder (R)

// accumulate V and R separately
vpaddd       zmm_acc_v, zmm_acc_v, zmm3
vpaddd       zmm_acc_r, zmm_acc_r, zmm4

// throughput: 32 elements per cycle (2× float lane count)
// 6 instructions vs 3, but 2× elements
```

**Per-element throughput comparison:**

| | Float32 | VDR i16 |
|---|---|---|
| Elements per register | 16 | 32 |
| Instructions per batch | 3 | 6 |
| Cycles per batch | ~1-2 | ~3-4 |
| Elements per cycle | ~8-16 | ~8-16 |
| Precision lost per op | ~0.5 ULP | zero |

Roughly the same throughput. But VDR is exact.

## Now Widen to Activation Accumulation

The matmul inner loop accumulates into i32. After the full dot product, the accumulator V and R lanes hold the exact result. No reduction error — integer add is exact, there is no rounding.

Float32 accumulation over a 4096-element dot product (typical hidden dim):

```
4096 FMAs, each with up to 0.5 ULP rounding
worst case: ~sqrt(4096) × 0.5 ULP ≈ 32 ULP accumulated error
typical: ~10-20 ULP
```

VDR accumulation over the same 4096 elements:

```
4096 integer multiply-shift-mask-add sequences
accumulated error: zero
the V accumulator holds the exact quotient sum
the R accumulator holds the exact remainder sum
if R overflows its lane, one more shift+mask propagates carry into V
still zero error
```

## Softmax — Where VDR Pulls Ahead

**Float32 path (AVX-512):**
```
// Step 1: find max (horizontal reduce, expensive)
vmovaps      zmm0, [logits]
vreduceps    zmm1, zmm0, max            // or manual tree reduce

// Step 2: subtract max and compute exp
vsubps       zmm2, zmm0, zmm1
// exp() — no native instruction. Options:
//   a) vex polynomial approximation: 6-8 instructions, ~4-5 ULP error
//   b) table + interpolation: memory access + multiply
//   c) call libm: branch out of SIMD entirely

// Step 3: sum (horizontal reduce again)
// Step 4: divide each element
vdivps       zmm4, zmm3, zmm_sum        // vdivps: 10-14 cycle latency

// total: ~20-30 cycles per 16 elements
// precision: approximate exp, approximate divide, sum ≈ 1
```

**VDR i16 path (AVX-512):**
```
// Step 1: table lookup for exp
// inputs are i16, so 65536 possible values
// precomputed table: exp_v[65536] and exp_r[65536]
// table is 256KB each — fits L2 comfortably

vpgatherdd   zmm0, [exp_v_table + zmm_indices * 4]   // gather 16 exp V values
vpgatherdd   zmm1, [exp_r_table + zmm_indices * 4]   // gather 16 exp R values

// Step 2: sum V lane (horizontal reduce, same cost as float)
// Step 3: normalize — integer divmod against sum
// if sum is power of two (often tunable): shift + mask
// if not: one integer divide per output, or Barrett reduction

// total: 2 gathers + reduce + normalize
// precision: exact. sum = D. not approximately D. D.
```

The gathers are expensive — maybe 10-15 cycles for 16 elements. But the float path spends 6-8 instructions on polynomial exp approximation and then 10-14 cycles on vdivps. They're comparable in cycle count.

But VDR produces exact results from the table. Float produces approximate results from the polynomial. Same cost, different correctness.

## The Chain — Diffusion Steps at SIMD Width

This is where the layout pays off most. A diffusion step across a latent vector:

```
x_t = sqrt_alpha_bar * x_{t-1} + sqrt_one_minus * eps
```

**Float32 — 16 elements per cycle:**
```
vmovaps      zmm0, [x_ptr]              // 16 latent values
vmulps       zmm1, zmm0, zmm_sqrt_ab    // scale by sqrt(alpha_bar) — broadcast
vmovaps      zmm2, [eps_ptr]            // 16 noise values
vfmadd231ps  zmm1, zmm2, zmm_sqrt_om   // + sqrt(1-alpha_bar) * eps
vmovaps      [x_ptr], zmm1             // store
// 4 instructions, 16 elements
// error per step per element: ~1 ULP
// after 1000 steps: ~1000 ULP per element
// after 1M steps: ~1M ULP per element — visible drift
```

**VDR i16 — 32 elements per cycle:**
```
vmovdqu16    zmm0, [x_v_ptr]            // 32 latent V values
vpmulld      zmm1, zmm0, zmm_sqrt_ab_v  // multiply by schedule constant
vpsrad       zmm2, zmm1, BITS           // shift = quotient
vpandd       zmm3, zmm1, zmm_mask       // mask = remainder

vmovdqu16    zmm4, [eps_v_ptr]           // 32 noise V values
vpmulld      zmm5, zmm4, zmm_sqrt_om_v  // multiply by other constant
vpsrad       zmm6, zmm5, BITS
vpandd       zmm7, zmm5, zmm_mask

vpaddd       zmm_out_v, zmm2, zmm6      // add quotients
vpaddd       zmm_out_r, zmm3, zmm7      // add remainders

vmovdqu16    [x_v_ptr], zmm_out_v       // store V
vmovdqu16    [x_r_ptr], zmm_out_r       // store R

// 12 instructions, 32 elements
// error per step: zero
// after 1000 steps: zero
// after 1M steps: zero
// after 8.64M steps (2hr video at 24fps × 150 diffusion steps): zero
```

**Per-element comparison on the chain:**

| | Float32 | VDR i16 |
|---|---|---|
| Elements per pass | 16 | 32 |
| Instructions per pass | 4 | 12 |
| Cycles per pass | ~2 | ~6 |
| Elements per cycle | ~8 | ~5-6 |
| Drift after 1K steps | ~1000 ULP | 0 |
| Drift after 1M steps | ~1M ULP | 0 |
| Memory bandwidth | 64B load + 64B store | 128B load + 128B store |

VDR is about 30-40% fewer elements per cycle on the chain step. But it processes 2× elements per register load. Memory-bound workloads (which diffusion is — the latent tensors are large) care about bytes loaded, not instructions issued. VDR loads the same number of meaningful values per cache line.

And the drift column is the whole story for long chains. Float needs periodic renormalization or error correction. VDR doesn't. Those correction passes cost cycles that VDR never spends.

## Conditional Divergence — The GPU Angle

Every VDR operation above is unconditional. There is no branch anywhere. No "if remainder overflows." No "if this value is denormal." No "if we need to renormalize."

Float actually has hidden conditionals: denormal handling, NaN propagation, infinity checks. Hardware handles these in microcode, but they still stall pipelines when triggered. On GPU, denormal flushing modes exist specifically because the alternative is warp divergence from denormal handling.

VDR on fixed power-of-two basis has no special cases. Every value is a valid integer. Shift and mask always produce valid results. There are no denormals, no NaN, no infinity, no special bit patterns. The pipeline never stalls on edge cases because there are no edge cases.

## Net Assessment

For compute-bound operations (pure matmul, large batch), float FMA wins on raw FLOPS. The hardware was literally designed for it.

For memory-bound operations (inference, long-chain diffusion, attention over long sequences), VDR i16 is competitive or faster because it packs 2× elements per cache line and every operation is a cheap integer op.

For correctness-sensitive chains (diffusion, Kalman filters, iterative solvers, video generation), VDR is strictly superior at comparable cost because the drift is zero and no correction passes are needed.

The Python 50-200× overhead was Python. In Zig, targeting SIMD with fixed power-of-two basis and deinterleaved V/R lanes, VDR is within 2× of float on compute-bound work and potentially faster on memory-bound work. With zero precision loss.
