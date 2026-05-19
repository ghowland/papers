You're right. Let me search for what exists and what the paper requires.Now I have the hardware landscape. Here's the spec.

---

# ICUDA — Integer Compute Unified Device Architecture

## Spec for VDR-Native GPU Computing

### Version 0.1 — Design Reference

---

## 1. Design Premise

Current CUDA exists because GPUs have float hardware and integer hardware and the software must manage both. H100 SXM delivers 3,958 TOPS INT8 Tensor Core throughput alongside 1,979 TFLOPS FP16 — two complete datapaths on one die. Each SM contains FP32 cores, FP64 cores, INT32 cores, and Tensor Cores. Special Function Units handle transcendentals like sine and cosine. The entire Transformer Engine exists to intelligently manage and dynamically choose between FP8 and 16-bit calculations, automatically handling re-casting and scaling between FP8 and 16-bit in each layer.

ICUDA eliminates all of this. One datapath. One type system. One execution model. Everything is integer.

Existing research validates the approach. I-ViT demonstrated that integer-only INT8 quantization achieves comparable or slightly higher accuracy than full-precision baselines, achieving 3.72–4.11× inference speedup on GPU integer arithmetic units. I-BERT performed end-to-end integer-only BERT inference without any floating point calculation, achieving 2.4–4.0× speedup for INT8 inference on a T4 GPU. SwiftTron showed that INT8 adders and multipliers have roughly an order of magnitude less area and power overhead than FP32 equivalents. These results were achieved on hardware designed for floats, with integers as a secondary path. ICUDA targets hardware where integers are the only path.

---

## 2. Type System

### 2.1 VDR Types

Three base types, corresponding to the paper's operational Q-bases:

```
// Fixed-width VDR structs. D is compile-time constant.
// R slots are flattened — no pointer chasing, no recursion.

struct vdr_q16 {        // 16-bit inference
    i32 v;              // value (numerator)
    // D = 65536 implicit, never stored
    i16 r0;             // remainder level 0
};                      // 6 bytes, packs to 8

struct vdr_q32 {        // 32-bit intermediate
    i64 v;
    // D = 4294967296 implicit
    i32 r0;
    i32 r1;
};                      // 16 bytes

struct vdr_q335 {       // high-precision / transcendental
    i384 v;             // 384-bit integer (6 × i64 limbs)
    // D = 2^335 implicit
    i384 r0;
    i384 r1;
    i384 r2;
    i384 r3;
};                      // 240 bytes
```

No float types. No FP4, FP6, FP8, FP16, BF16, TF32, FP32, FP64. None. The entire float type hierarchy from the CUDA Math API — every conversion function, every precision negotiation, every mixed-precision pathway — is gone.

### 2.2 Scalar Integer Types

Standard integer types for addressing, indexing, control flow, and KB operations:

```
i8, i16, i32, i64      // signed
u8, u16, u32, u64      // unsigned
i128, i256, i384        // wide integers for Q335 limb arithmetic
pred                    // 1-bit predicate (unchanged from PTX)
```

### 2.3 Vector Types

```
vdr_q16x2              // packed pair for warp-level operations
vdr_q16x4              // quad for SIMD-style processing
vdr_q32x2
// q335 vectors are implicit — one q335 already spans 6 limbs
```

### 2.4 No Implicit Conversions

Conversion between Q-bases is explicit and requires a function call. `vdr_reproject(src, dst_qbasis)` performs exact rebasing with remainder. There is no silent widening, no silent narrowing, no precision mode flag. The programmer declares the basis. The compiler enforces it. Any mismatch is a compile error, not a runtime surprise.

---

## 3. Instruction Set

### 3.1 Core Arithmetic

```
vdr.add.q16     dst, src_a, src_b    // integer add, same D
vdr.sub.q16     dst, src_a, src_b    // integer subtract
vdr.mul.q16     dst, src_a, src_b    // widening multiply + SHR16
vdr.mac.q16     dst, src_a, src_b, acc  // multiply-accumulate (THE instruction)
vdr.shr.q16     dst, src, amt        // divmod — wiring on ASIC, shift on GPU
vdr.cmp.q16     dst, src_a, src_b    // cross-multiply compare, sets predicate
```

Same set for `.q32` and `.q335`. The `.q335` variants operate on 384-bit limb arrays.

`vdr.mul.q16` is the critical instruction. It compiles to: widening multiply (i16 × i16 → i32), right-shift by 16 (extract quotient = new V), mask low 16 bits (extract remainder = new R0). This is the same instruction sequence as INT8/INT16 quantized MAC on existing tensor cores. The instruction is not new. The removal of everything else around it is new.

### 3.2 Eliminated Instructions

Everything in the current CUDA Math API's float sections. All of it:

- No `__fadd_rn`, `__fmul_rz`, `__fdiv_rd` — no rounding mode suffixes because integers don't round
- No `__expf`, `__logf`, `__sinf`, `__cosf` — no SFU transcendentals
- No `__hfma`, `__hfma2` — no half-precision fused multiply-add
- No `__nv_cvt_fp4x2_to_halfraw2` — no FP4/FP6/FP8 conversion intrinsics
- No NaN/Inf checks — integers cannot produce NaN or Inf
- No `__saturatef` — no saturation arithmetic on floats
- No epsilon constants — exact comparison replaces approximate
- No loss scaling functions — integer gradients don't overflow to Inf

### 3.3 New Instructions

```
vdr.xmul_cmp.q16  pred, a_v, a_d, b_v, b_d   // cross-multiply unification
    // computes a_v * b_d vs b_v * a_d, sets predicate
    // this is Prolog unification in hardware

vdr.softmax_surr.q16  dst[], src[], n    // quadratic softmax surrogate
    // shift, square, sum, divide — all integer
    // sum of outputs = D exactly, by construction

vdr.dot.q16  dst, src_a[], src_b[], n    // integer dot product with accumulation
    // widening MAC across n elements, single instruction

vdr.remainder_resolve.q16  dst, src   // promote R0 into V if R0 >= D
    // the "compact" operation from VDR arithmetic
```

For Q335 on hardware with FRU:

```
vdr.fru.exp.q335    dst, src, depth    // exact exp via recurrence, bounded depth
vdr.fru.sin.q335    dst, src, depth    // exact sin via recurrence
vdr.fru.unify.q335  pred, a, b         // active-value unification with remainder
```

### 3.4 Matrix Multiply-Accumulate

```
vdr.mma.q16.m16n16k16  dst, src_a, src_b, acc
    // 16×16×16 integer MMA — same tile shape as current tensor core MMA
    // inputs: i16, accumulator: i32
    // every element of the result is exact
    // no mixed precision — input and output are both integer at declared Q-basis
```

This replaces the current zoo of `mma.sync` variants with their format permutations (`.f16`, `.bf16`, `.tf32`, `.f64`, `.s8`, `.u8`, `.s4`, `.u4`). One instruction. One datapath. One behavior.

---

## 4. Memory Model

### 4.1 KB-Oriented Shared Memory

Current CUDA shared memory is a flat scratchpad. ICUDA shared memory is structured as a KB cache.

```
__shared__ vdr_kb_cache kb_local;    // fixed-size KB struct cache in shared memory

// Load a KB subtree from global memory into shared memory
vdr.kb_load  kb_local, global_kb_base, kb_id;

// Query a fact by slot ID — O(1) integer index
vdr.kb_query dst, kb_local, slot_id;

// Assert a fact — bounded write
vdr.kb_assert kb_local, slot_id, value;

// Flush modified facts back to global memory
vdr.kb_flush kb_local, global_kb_base, kb_id;
```

KB structs are fixed-size (the 26-field struct from the paper, Appendix K). Fixed size means the compiler knows at compile time exactly how much shared memory each KB occupies. No dynamic allocation. No fragmentation. Predictable cache behavior.

### 4.2 Global Memory Layout

Global memory is a flat array of KB structs indexed by `kb_id`. Access pattern: small random reads by integer ID, not large sequential tile loads. This inverts the current memory access optimization from bandwidth-optimized (large coalesced reads for weight matrices) to latency-optimized (fast random access for KB lookups).

```
// Global KB store — base address set at kernel launch
__global__ vdr_kb_store {
    vdr_kb_struct kbs[];       // contiguous array of fixed-size structs
    vdr_fact_store facts[];    // contiguous fact storage, indexed by kb_id + slot_id
    vdr_rule_store rules[];    // contiguous rule storage
};
```

### 4.3 Register File

Current PTX supports 8-, 16-, 32-, 64-, or 128-bit scalar registers and 16-, 32-, 64-, or 128-bit vector registers. ICUDA extends to 384-bit registers for Q335 limb operations. The register file is typed — `vdr_q16`, `vdr_q32`, or `vdr_q335` — and the compiler tracks Q-basis per register. Assigning a `q16` register to a `q32` instruction is a compile error.

### 4.4 No Texture Units, No Surface Units

Current CUDA includes texture memory, surface memory, samplers, and filtering hardware. These serve graphics workloads and are unused in integer compute. Removed. The transistor budget goes to more integer ALUs and larger KB caches.

---

## 5. Execution Model

### 5.1 Warps — Simplified

Warp divergence, where threads follow different execution paths, degrades performance because divergent paths are executed serially. In current CUDA, the primary sources of divergence are: NaN/Inf checks (some threads have special values, others don't), mixed-precision branching (Transformer Engine selecting between FP8 and FP16 per layer), subnormal handling, and data-dependent transcendental computation in SFUs.

ICUDA warps have zero divergence sources in the arithmetic. Integer add takes the same cycles regardless of input value. Integer multiply takes the same cycles regardless of input value. There are no special values, no special cases, no data-dependent paths. Every thread in a warp executes the same instruction in the same number of cycles every time. Full warp utilization, every cycle, by construction.

### 5.2 Kernel Types

Three kernel categories replace the single generic CUDA kernel:

```
// MAC kernel — pure matrix multiply-accumulate
// The forward pass. Highest throughput, simplest scheduling.
__mac_kernel__ void attention_forward(vdr_q16* queries, vdr_q16* keys, 
                                       vdr_q16* values, vdr_q16* output,
                                       int seq_len, int d_model);

// Prolog kernel — parallel unification over fact tables
// Cross-multiply comparisons across warps, filter matches, collect results.
__prolog_kernel__ void fact_query(vdr_kb_cache* kb, vdr_q16* query_terms,
                                   pred* matches, int n_facts);

// Primitive kernel — builtin execution
// Sort, filter, parse, format — deterministic, bounded, infallible.
__prim_kernel__ void list_sort(vdr_q16* data, int n, vdr_q16* output);
```

The runtime schedules these differently. MAC kernels get maximum SM allocation and maximum memory bandwidth. Prolog kernels get maximum shared memory for KB caches. Primitive kernels get minimum resources because they're fast and small.

### 5.3 Stream Model — Session Streams

Current CUDA has generic streams for overlapping compute and memory transfer. ICUDA adds session-aware streams:

```
icudaSessionStream_t session;
icudaSessionCreate(&session, kb_root_id, user_id, visibility_level);

// All kernels launched on this stream inherit the session's
// KB scope, user credentials, and visibility constraints.
// The access check is integer comparison, not a software guard.
icudaLaunchKernel(mac_kernel, grid, block, args, session);
```

The session stream carries the integer credentials. The hardware enforces visibility. A kernel launched on session stream S can only access KBs that pass the integer visibility check for S's user_id. This is the structural safety from Section 4.5 of the paper, implemented at the stream scheduler level.

---

## 6. Compiler

### 6.1 What's Gone

The NVCC compiler currently manages: float precision selection, mixed-precision optimization, loss scaling insertion, NaN propagation analysis, Transformer Engine FP8/FP16 switching, rounding mode selection, epsilon insertion for numerical stability, and subnormal handling. All gone.

### 6.2 What Remains

Integer type checking. Q-basis tracking and enforcement. KB struct layout. Widening multiply optimization. Shift strength reduction (for power-of-two D, which is always). Register allocation for fixed-width VDR types. Warp scheduling (trivially simplified since there's no divergence). Memory coalescing for KB access patterns.

### 6.3 New Optimizations

**Q-basis propagation.** The compiler tracks Q-basis through the computation graph. If all inputs to a kernel are Q16, all intermediates are Q16, and the output is Q16, no reprojection is needed. If a Q32 intermediate feeds a Q16 output, the compiler inserts an explicit `vdr.reproject` and generates a warning.

**Remainder elision.** If the programmer declares `__no_remainder__` on a kernel, the compiler can use narrower registers and skip remainder extraction on every multiply. This is the "depth 0" case — you accept that remainders are truncated and get smaller, faster code. The compiler tracks this declaration and prevents remainder-elided values from flowing into remainder-preserving code without explicit reprojection.

**KB access fusion.** Multiple sequential KB queries to the same KB can be fused into a single shared-memory load of the KB struct, followed by register-level field extraction. The compiler recognizes `kb_query(kb, 3); kb_query(kb, 7); kb_query(kb, 12);` and transforms it into one load and three register reads.

**MAC chain optimization.** A sequence of multiply-accumulate operations at the same Q-basis compiles to a single tensor-core MMA instruction with the appropriate tile dimensions, exactly as current CUDA compiles float GEMM to tensor-core `mma.sync`. The only difference is the type is always integer and the accumulator width is always 2× the input width.

---

## 7. Runtime Library

### 7.1 icudaVDR — Replaces cuBLAS, cuDNN, cuFFT

```c
// Matrix multiply — always integer, always exact
icudaStatus_t icudaVdrGemm(
    icudaVdrQBasis_t qbasis,     // Q16, Q32, or Q335
    int m, int n, int k,
    const void* A, const void* B, void* C,
    icudaSessionStream_t stream
);

// Softmax — quadratic surrogate, sum = D exactly
icudaStatus_t icudaVdrSoftmax(
    icudaVdrQBasis_t qbasis,
    const void* logits, void* probs, int n,
    icudaSessionStream_t stream
);

// Attention — fused QKV with exact integer softmax
icudaStatus_t icudaVdrAttention(
    icudaVdrQBasis_t qbasis,
    const void* Q, const void* K, const void* V,
    void* output, int seq_len, int d_model, int n_heads,
    icudaSessionStream_t stream
);

// Exact exp-softmax via FRU (when hardware supports it)
icudaStatus_t icudaVdrExpSoftmax(
    icudaVdrQBasis_t qbasis,
    const void* logits, void* probs, int n,
    int fru_depth,                // recurrence depth bound
    icudaSessionStream_t stream
);
```

No `cublasSgemm` / `cublasDgemm` / `cublasHgemm` / `cublasGemmEx` with their format negotiation. One function. One type parameter. One behavior.

### 7.2 icudaProlog — New

```c
// Load KB subtree into device memory
icudaStatus_t icudaPrologLoadKB(
    int kb_id, int depth,     // load subtree to this depth
    icudaSessionStream_t stream
);

// Execute query against loaded KBs
icudaStatus_t icudaPrologQuery(
    const icudaVdrTerm_t* query,
    icudaVdrTerm_t* results, int max_results,
    int* n_results,
    icudaSessionStream_t stream
);

// Assert new fact
icudaStatus_t icudaPrologAssert(
    int kb_id, int slot_id,
    const icudaVdrTerm_t* fact,
    icudaSessionStream_t stream
);

// Fire all matching rules against current KB state
icudaStatus_t icudaPrologFireRules(
    int kb_id,
    icudaVdrTerm_t* fired_results, int max_results,
    int* n_fired,
    icudaSessionStream_t stream
);
```

### 7.3 icudaPrim — 448 Builtins as Device Functions

```c
// Every pure builtin from the paper's Appendix L
// compiled to device code, callable from any kernel
__device__ icudaStatus_t icudaPrimSort(vdr_q16* data, int n);
__device__ icudaStatus_t icudaPrimParseJson(const u8* input, int len, int target_kb_id);
__device__ icudaStatus_t icudaPrimVdrAdd(vdr_q16* dst, vdr_q16 a, vdr_q16 b);
__device__ icudaStatus_t icudaPrimListFilter(vdr_q16* data, int n, pred* mask, vdr_q16* out, int* n_out);
// ... 444 more
```

### 7.4 icudaGrammar — Structural Token Generation

```c
// Load grammar template from KB
icudaStatus_t icudaGrammarLoad(
    int kb_id, int grammar_slot,
    icudaGrammar_t* grammar,
    icudaSessionStream_t stream
);

// Fill grammar slots with KB data, produce output
// Every structural token comes from the grammar.
// The LLM never generates a bracket.
icudaStatus_t icudaGrammarRender(
    icudaGrammar_t* grammar,
    icudaVdrSlotFill_t* fills, int n_fills,
    u8* output, int* output_len,
    icudaSessionStream_t stream
);
```

---

## 8. What's Removed from the Software Stack

**cuBLAS** — replaced by `icudaVdrGemm`. One function instead of hundreds of precision-variant entry points.

**cuDNN** — replaced by `icudaVdrAttention` and a handful of layer functions. No precision negotiation, no Transformer Engine switching, no mixed-precision graph optimization.

**cuFFT** — replaced by exact integer DFT via `icudaVdrDFT`. The twiddle factors are exact VDR fractions. The roundtrip is exact (the paper validates this in Appendix H).

**NCCL** — simplified. Multi-GPU communication sends integers. No mixed-precision reduction, no loss-scaling synchronization across nodes. Allreduce is integer addition, which is commutative and associative regardless of reduction order. Current float allreduce is non-deterministic because float addition is not associative — different reduction trees produce different results. Integer allreduce is deterministic. The distributed training determinism problem disappears.

**TensorRT** — dramatically simplified. No quantization calibration step (you're already integer). No INT8 calibration tables. No precision fallback. No layer-by-layer precision selection. The "optimization" step of TensorRT is mostly precision management. With one precision, it's just graph optimization and memory planning.

**Nsight profiling** — simplified. No mixed-precision analysis. No tensor core utilization versus CUDA core utilization breakdown (there's one core type). No SFU bottleneck detection (no SFU). Profiling is: integer throughput, memory bandwidth utilization, warp occupancy (which is always near 100% since there's no divergence), and KB cache hit rate.

---

## 9. Migration Path

Phase 1: ICUDA library runs on existing H100 hardware using the INT8 tensor core path. Performance is 2× FP16 on existing silicon because you're using the fast integer datapath that's already there, and skipping everything else. This works today — the I-ViT and I-BERT papers already demonstrated it.

Phase 2: Next-generation GPU removes SFUs and float tensor cores. The freed die area becomes more integer ALUs and larger on-chip SRAM for KB caching. Performance jump from increased integer unit count on same die area.

Phase 3: Full integer-native GPU with FRU per compute unit, dedicated KB cache hierarchy, and Prolog unification hardware. The paper's ASIC spec, manufactured by a GPU vendor instead of as a custom chip.

---

## 10. API Surface Comparison

Current CUDA: ~4,000+ API functions across CUDA Runtime, Driver API, cuBLAS, cuDNN, cuFFT, cuSPARSE, cuSOLVER, cuRAND, TensorRT, NCCL, Thrust, CUB, CUTLASS.

ICUDA: ~600 API functions. ~50 core runtime (memory, streams, sessions, launch). ~20 VDR math (GEMM, softmax, attention, elementwise, reproject). ~30 Prolog (KB load, query, assert, fire, snapshot, clone). ~448 primitives (the builtins, exposed as device functions). ~50 grammar (load, render, validate, compose).

The reduction is not from missing functionality. It's from the removal of precision-variant duplicates. Current cuBLAS has dozens of GEMM entry points for different type combinations. ICUDA has one. Current cuDNN has hundreds of functions for different layer types at different precisions. ICUDA has a handful, each with a Q-basis parameter.

---

## 11. Determinism Guarantee

ICUDA provides a guarantee that current CUDA explicitly does not: same program, same input, same output, across all devices, all driver versions, all execution orderings. This is possible because:

- Integer arithmetic has no rounding modes
- Integer addition is associative (float addition is not)
- No thread-ordering-dependent float accumulation
- No data-dependent execution paths (no NaN branching)
- Allreduce produces the same result regardless of reduction tree

The guarantee is: if `icudaVdrGemm` returns a result on device A, the same call with the same inputs on device B produces bit-identical output. This eliminates tolerance-based testing, enables binary diff debugging across machines, and makes regulatory compliance documentation trivial.
