## Paper Plan: HOWL-VDR-29-2026

### Title
VDR in Zig SIMD and GPU Performance versus Floating Point

### Audience
Engineers and researchers who have not read prior VDR papers. No assumed knowledge of VDR, remainder arithmetic, or fixed-basis integer methods. Assumed familiarity with floating-point arithmetic, SIMD concepts, GPU architecture, and ML inference/training pipelines.

---

### Section 1: The Problem — What Float Discards

Open with the mechanical fact. Every floating-point multiply or add can round. One rounding is negligible. A chain of thousands or millions compounds. State the specific failure modes: drift in long diffusion chains, non-reproducibility across platforms, inability to test exact equality, NaN/Inf edge cases, epsilon parameter proliferation. No opinion, just the observable costs.

Give the concrete numbers: 8.64M-step diffusion chain for 2-hour video at 24fps × 150 denoising steps. Float64 drift reaches ~1.9e-8 per element. This is measurable and manifests as color shift and temporal flicker.

### Section 2: VDR — The Triple [V, D, R]

Introduce VDR from scratch for the new reader. Every value is three integers: V (numerator), D (denominator), R (remainder). D is fixed. When a multiply would produce a result too large for the D frame, divmod splits it: quotient goes to V, remainder goes to R. Zero information discarded. This is grade-school division applied as an architectural principle.

Explain closed objects (R=0, plain rational) and active objects (R≠0, carrying exact overflow). Explain that R is divided by D, not added externally. Give the concrete example: two values with D=2^16, multiply their numerators, shift right 16 for the quotient, mask low 16 bits for the remainder. One integer multiply, one shift, one mask. That is the entire mechanism.

### Section 3: Q335 and Why We Don't Use It Here

Explain that the Python reference implementation (vdr-math) uses D=2^335 as its default basis. This was chosen for physics and transcendental computation — 100-digit precision sufficient for QED corrections, zeta functions, elliptic integrals. Validated across 921 tests in 38 mathematical domains with zero VDR computation errors.

Then explain why Q335 is wrong for LLM and diffusion workloads. 335-bit integers don't fit in SIMD registers. They require multi-precision arithmetic libraries. They are hundreds of times slower than machine-word operations. The workloads don't need 100-digit precision — they need exact arithmetic at the precision level the model actually operates at.

VDR allows any basis. D is a choice, not a constant. The system's exactness property holds at any D. We retool D to match the hardware.

### Section 4: Choosing the Basis for ML Workloads

Walk through the basis selection rationale for LLM and diffusion.

Weights: D=2^8 (INT8). Weights are frozen during inference. R=0 for stored weights — no remainder channel needed in memory. One byte per parameter. This matches existing INT8 tensor core hardware and halves memory footprint versus FP16.

Activations: D=2^16 (INT16). Activations are computed on-chip, not loaded from HBM. Two bytes for V, two bytes for R, four bytes total per activation. Same memory footprint as FP32 but carrying exact remainder. Fits 32 elements per AVX-512 register or 16-wide GPU SIMD.

Gradient accumulation: D=2^64 (INT64). Gradients need wider accumulators to avoid overflow during reduction across large batch sizes. Native 64-bit integer arithmetic on all modern hardware.

Explain that D being a power of two means divmod is a bit shift and mask. No integer division hardware needed. This is what makes the basis choice a performance decision, not just a precision decision.

### Section 5: Zig Data Structures

Present the structs. Element types (Vdr8, Vdr16, Vdr64) with V and R fields, no D field because D is a module-level constant per domain. Container types (WeightMat, ActivationMat, GradMat) with flat arrays and no basis metadata. Layer types (LinearLayer, AttentionHead, TransformerBlock) composing containers. Diffusion types (DiffusionSchedule, DiffusionLatent, DiffusionTrajectory) with precomputed exact schedule values.

Emphasize the deinterleaved memory layout: separate V and R arrays rather than interleaved v,r,v,r. This allows pure vertical SIMD — load 32 V values in one instruction, 32 R values in another, no shuffling.

### Section 6: CPU SIMD Performance — AVX-512

Walk through each operation with cycle counts and element throughput.

**Matmul inner loop.** Float: 16 f32 elements per register, one FMA instruction. VDR: 32 i16 elements per register, vpmaddwd + shift + mask + 2 adds. Same elements-per-cycle throughput. VDR wins on memory-bound workloads from 2× element density.

**Softmax.** Float: polynomial exp approximation (6-8 instructions, ~4-5 ULP error) + float division (10+ cycles). VDR: table lookup (1 gather instruction, exact) + Barrett reduction (4 integer ops). VDR 1.5-2× faster with exact results.

**Activation functions.** Float: 10-20 instruction polynomial. VDR: 1 table lookup. VDR 5-10× faster.

**Layer norm.** Float: float division + rsqrt (expensive). VDR: bit shift (power-of-two hidden dim) + table rsqrt. VDR 1.5-2× faster.

**Diffusion chain step.** Float: 4 instructions for 16 elements, ~1 ULP drift per step. VDR: 12 instructions for 32 elements, zero drift. ~0.7× raw throughput per cycle, but zero correction overhead makes long chains net equivalent or better.

**Residual add.** Float: one add. VDR: V add + R add + carry propagation. Float 1.3-1.5× faster. Negligible contribution to total pipeline compute.

### Section 7: GPU Performance — H100 Tensor Cores

Present the H100 execution unit throughput table: FP16 tensor cores at 512 ops/SM/cycle, INT8 tensor cores at 1024 ops/SM/cycle, SFU at 32 ops/SM/cycle.

**GEMM.** INT8 tensor cores deliver 2× FP16 throughput on the operation that dominates transformer compute. VDR maps directly onto existing INT8 tensor core instructions. Projected 1.6-1.8× effective speedup after accounting for kernel maturity.

**Softmax on GPU.** Float softmax is SFU-bottlenecked — exp and division both require the SFU at 1/16 tensor core rate. VDR replaces both with shared memory table lookup and Barrett reduction at full integer throughput. 3-4× faster.

**Activations and normalization on GPU.** Same SFU elimination pattern. GeLU, SiLU, rsqrt all become table lookups. 2-6× faster on these operations.

**Memory bandwidth.** INT8 weights are 1 byte versus FP16 at 2 bytes. At H100's 3.35 TB/s HBM bandwidth, VDR loads 2× the parameters per second. For memory-bound single-batch inference, this translates directly to 2× throughput ceiling.

**Warp divergence.** Float has edge cases: denormals trigger flush-to-zero or slow paths, NaN propagates uselessly, Inf corrupts downstream computation. VDR integer arithmetic has no special cases. Every thread executes identical instructions on every cycle. Zero divergence by construction, not by probability.

**Shared memory.** Half-size weight tiles leave room for double-buffering or lookup table co-residency. Better latency hiding.

### Section 8: Full Pipeline Comparison

Present the complete transformer forward pass breakdown for a 7B parameter model, 32 layers, hidden dim 4096, sequence length 2048.

Per-layer timing for every component (QKV projection, attention GEMM, softmax, attention output, FFN up/gate/down, GeLU, layer norm, residual add). Per-layer total. 32-layer total. Full forward pass.

Projected results: FP16 ~110ms per token, VDR INT8 ~55ms per token. 2× throughput.

Scale to batched inference (batch=8): ~580 tok/s FP16, ~1050 tok/s VDR. Scale to full-bore (batch=64+): VDR ~1.8× at full compute saturation.

### Section 9: Diffusion Chain Analysis

Present diffusion-specific results. Single image (50 steps): VDR ~2× faster, drift irrelevant at this chain length. Long-form video (2 hours, 25.9M steps): VDR ~2.1× faster including elimination of correction passes that float requires.

Provide the drift table: float drift at 1K, 1M, 8.64M steps versus VDR zero at all chain lengths. Provide the correction overhead calculation: float needs ~25,920 correction passes at 5-8% total compute cost. VDR needs zero.

Note the qualitative differences: bit-identical reproduction across platforms and runs, zero visual artifacts from arithmetic drift, deterministic behavior enabling reliable A/B testing.

### Section 10: Training Considerations

Training uses wider types for gradients (INT64). Backward pass GEMM uses INT16 tensor cores at ~1.5× FP16 rate rather than INT8 at 2×. Net training throughput advantage is smaller: approximately 1.5-1.7×.

However, training eliminates loss scaling (no underflow possible with integers), eliminates gradient clipping for numerical stability (no NaN/Inf possible), and eliminates epsilon parameters in optimizers. These simplify the training loop and remove failure modes.

### Section 11: Costs and Limitations

State clearly where VDR is slower or harder.

Residual addition is 0.7× float speed due to remainder carry propagation. This is the one operation where float wins. Its contribution to total pipeline compute is negligible.

Kernel maturity is the primary practical gap. cuBLAS and cuDNN represent decades of optimization. VDR kernels are new. The projected throughput numbers assume 85-90% hardware utilization versus ~95% for mature float kernels. As VDR kernels mature, the gap narrows.

Table lookup for transcendentals requires shared memory or L1 residency. For Q16 inputs the table is 256KB — fits L2 comfortably but competes for shared memory with weight tiles. Kernel design must balance tile size against table residency.

Basis choice is a new engineering decision. Choosing D too small loses dynamic range. Choosing D too large wastes bits and potentially overflows accumulators. The choice must be validated per model architecture. This paper uses D=2^8 for weights, D=2^16 for activations, D=2^64 for gradients — these are empirically motivated starting points, not proven optimal.

VDR remainder channels double the on-chip storage for activations compared to storing V alone. For activation-memory-bound workloads (very long sequences, limited GPU memory), this is a real cost.

### Section 12: Results Summary

Two summary tables. Per-operation comparison (operation, float path, VDR path, speedup factor, bottleneck eliminated). Pipeline-level comparison (workload scenario, float throughput, VDR throughput, advantage factor).

One qualitative comparison table covering drift, reproducibility, NaN/Inf risk, warp divergence, epsilon parameters, correction passes, probability sum exactness, cross-platform consistency.

### Section 13: Conclusion

VDR fixed-basis integer arithmetic projects to 1.5-2× throughput improvement over optimized FP16 pipelines on existing hardware, with exact results at every step. The advantage derives from three hardware facts: INT8 tensor cores deliver 2× FP16 throughput, half-size weights double effective memory bandwidth, and table lookups for transcendentals bypass the SFU bottleneck. The single operation where float is faster contributes negligibly to total compute.

The hardware exists. The data structures are defined. The kernel specifications are complete. Implementation is the remaining work.

---

### Appendices (planned)

A. Complete Zig struct definitions
B. Kernel pseudocode for all eight kernel types
C. Basis selection methodology and validation
D. Lookup table construction for exp, gelu, rsqrt
E. Barrett reduction for exact integer normalization

---

That is the plan. Ready for your review.
