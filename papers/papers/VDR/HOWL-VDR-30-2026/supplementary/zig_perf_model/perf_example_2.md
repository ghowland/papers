## H100 Architecture — The Relevant Numbers

**H100 SMs have separate execution units:**

| Unit | Throughput per SM per cycle | What it does |
|---|---|---|
| FP32 CUDA cores | 128 ops | float multiply-add |
| FP16 Tensor Cores | 512 ops (4× FP32) | matrix multiply-accumulate |
| INT32 cores | 64 ops | integer arithmetic |
| INT8 Tensor Cores | 1024 ops (8× FP32) | integer matrix multiply-accumulate |

This is critical. The INT8 tensor core throughput is 8× the FP32 throughput. And INT8 tensor cores already exist because the quantization crowd demanded them. VDR runs on exactly this hardware.

## The Tensor Core Angle

Tensor cores do small matrix multiplies in one operation. On H100:

**FP16 tensor core:** 16×16×16 matmul, accumulate into FP32. 512 FMAs per cycle per SM. This is what transformers currently run on.

**INT8 tensor core:** 16×16×32 matmul, accumulate into INT32. 1024 multiply-adds per cycle per SM. Twice the throughput of FP16 in raw operations, because the elements are half the width.

VDR i16 weights × i16 activations → i32 accumulator maps directly onto INT8 tensor core paths. Two i8 pairs per i16, or use the INT16 mode where available. The key point: the tensor cores already do integer multiply-accumulate with widening into i32. That's exactly the VDR inner product.

## Matmul on Tensor Cores — Float vs VDR

**FP16 path (current production):**
```
// Per SM per cycle:
// Load 16×16 FP16 tile A from shared memory
// Load 16×16 FP16 tile B from shared memory
// Tensor core: 16×16×16 FMA → FP32 accumulator
// 512 FMAs per cycle
// Precision: FP16 inputs (5-bit mantissa), FP32 accumulation
// Error per element: truncation from FP16 representation
//   plus rounding in FP32 accumulation
```

**VDR INT8 path on same tensor cores:**
```
// Per SM per cycle:
// Load 16×16 INT8 tile A_v from shared memory (V values of weights)
// Load 16×32 INT8 tile B_v from shared memory (V values of activations)
// Tensor core: 16×16×32 integer multiply-accumulate → INT32
// 1024 integer multiply-adds per cycle
// This gives us the raw products accumulated into i32

// The i32 accumulator IS the divmod input.
// After tile completes:
// acc_v = accumulator >> BITS    (one shift per output element)
// acc_r = accumulator & MASK     (one mask per output element)

// Throughput: 1024 ops/cycle vs 512 for FP16
// Precision: exact
```

**2× throughput on the dominant operation, with exact results.** Not because VDR is clever — because the INT8 tensor cores are already there, already 2× FP16, and VDR's fixed-basis arithmetic maps directly onto them.

## Warp Execution — No Divergence

A warp is 32 threads executing the same instruction in lockstep. Divergence happens when threads take different branches.

**Float warp hazards:**

Denormals: if any thread in the warp produces a denormal, the SM either flushes to zero (losing information) or takes a slow path. CUDA defaults to flush-to-zero mode for exactly this reason — the alternative is divergence or stall. FTZ loses information silently.

NaN propagation: if any thread produces NaN (0/0, inf-inf), NaN propagates through all subsequent operations for that thread. The computation is dead but the thread keeps executing garbage. No divergence, but wasted work.

Infinity: overflow to inf. Subsequent operations produce inf or NaN. Same problem.

Conditional normalization: softmax, layer norm, batch norm all require reduction operations that can trigger special-case handling for extreme values. Not divergence per se, but pipeline stalls and edge cases.

**VDR warp — zero hazards:**

Every thread does the same sequence: integer multiply, shift right, bitwise AND, integer add. There is no value of i16 or i32 that causes a special case. No denormals (integers don't have them). No NaN (integers don't have it). No infinity (integers overflow deterministically via wrapping, and with proper bit width selection they don't overflow at all). No flush-to-zero because there's nothing to flush.

Every thread in the warp executes identical instructions on different data. The instruction stream is:

```
IMAD    Rd, Ra, Rb, Rc    // integer multiply-add (tensor core or CUDA core)
SHR     Rd, Ra, IMM       // right shift by constant
AND     Rd, Ra, IMM       // mask by constant
IADD    Rd, Ra, Rb        // integer add
```

No predication. No branch. No special case. Every cycle, all 32 threads do useful work. Occupancy is perfect because there are no register pressure surprises from exception handling.

## Shared Memory and Tiling

**Float tiling for transformer matmul:**
```
// Typical: 128×128 tile in shared memory
// FP16: 128 × 128 × 2 bytes = 32KB per tile
// Two tiles (A and B): 64KB — exactly fills H100 shared memory config
```

**VDR tiling:**
```
// V values only for the multiply (R is computed, not loaded for weights)
// INT8 V values: 128 × 128 × 1 byte = 16KB per tile
// Two tiles: 32KB — half the shared memory pressure
// Room for double-buffering: load next tile while computing current
// Or: 256×256 tiles at same memory footprint — better arithmetic intensity
```

Smaller elements mean either better double-buffering (hiding latency) or larger tiles (better compute-to-memory ratio). Both improve effective throughput.

## Softmax on GPU — Float vs VDR

**Float softmax — the standard pain:**
```
// Phase 1: find max across sequence (warp reduce)
// Phase 2: subtract max, compute exp() per element
//   exp() on GPU: ~20 instructions of polynomial approximation (SFU or software)
//   SFU throughput: 1/4 of CUDA core throughput — this is the bottleneck
// Phase 3: sum (warp reduce again)
// Phase 4: divide each element by sum
//   float divide: ~10 cycles on SFU, again 1/4 throughput

// Two warp reduces + SFU-bottlenecked exp + SFU-bottlenecked div
// SFU is the limiter: 32 ops/cycle vs 128 for FP32 cores
```

**VDR softmax — table lookup:**
```
// Phase 1: find max (same warp reduce, integer version)
// Phase 2: table lookup for exp
//   inputs are bounded i16 or i8 — finite table
//   table lives in shared memory or L1: 64KB for i16 inputs easily
//   one load per element, full throughput, no SFU
// Phase 3: sum (same warp reduce, integer version)
// Phase 4: normalize by integer division or Barrett reduction
//   if sum is near power of two: shift + correct
//   if not: Barrett reduction is ~4 integer ops, full throughput

// No SFU dependency at all. Entire softmax runs on integer cores at full rate.
```

Float softmax is SFU-bottlenecked at 1/4 core throughput. VDR softmax runs entirely on integer cores and shared memory at full throughput. This alone could be a 3-4× speedup on softmax, which is a significant fraction of attention compute.

## Global Memory Bandwidth — H100

H100 has ~3.35 TB/s HBM bandwidth. For memory-bound workloads (inference, long-sequence attention), this is the ceiling.

**Float16 inference:** each weight is 2 bytes. 3.35 TB/s ÷ 2 bytes = 1.675 trillion weights per second loadable.

**VDR INT8 weights (V only, R computed):** each weight is 1 byte. 3.35 TB/s ÷ 1 byte = 3.35 trillion weights per second loadable. 2× float16.

For memory-bound inference, VDR INT8 doubles the throughput ceiling. And during the matmul those bytes hit INT8 tensor cores at 1024 ops/SM/cycle instead of FP16 tensor cores at 512. The memory bandwidth advantage and the compute throughput advantage stack.

## Full Transformer Forward Pass — Pipelined

```
Embedding lookup:     INT8 table → i16 VDR activations. Pure memory.
Layer norm:           Integer mean/variance over i16. No float division.
Q/K/V projection:     INT8 weight × i16 activation → i32 accumulator.
                      Tensor core path. 2× FP16 throughput.
Attention scores:     i16 × i16 → i32. Tensor core path.
Softmax:              Table lookup + integer reduce + Barrett. No SFU.
Attention output:     i16 × i16 → i32. Tensor core path.
Output projection:    INT8 × i16 → i32. Tensor core path.
Residual add:         Integer add. Trivial.
FFN up:               INT8 × i16 → i32. Tensor core path.
Activation (GeLU):    Table lookup, same as exp. No SFU.
FFN down:             INT8 × i16 → i32. Tensor core path.
Layer norm:           Integer. No SFU.
```

Every SFU-dependent operation in the float path (exp, gelu, rsqrt for layer norm, division) becomes a table lookup or integer operation in the VDR path. The SFU is completely bypassed. The entire forward pass runs on integer cores and tensor cores at full throughput.

## The Scoreboard

| Metric | FP16 Tensor Core | VDR INT8 Tensor Core |
|---|---|---|
| Ops per SM per cycle | 512 | 1024 |
| Bytes per weight | 2 | 1 |
| Weights loadable per second | 1.675T | 3.35T |
| Softmax bottleneck | SFU at 1/4 rate | table lookup at full rate |
| GeLU/activation | SFU at 1/4 rate | table lookup at full rate |
| Layer norm rsqrt | SFU at 1/4 rate | integer Newton or table |
| Warp divergence risk | denormal/NaN/inf edge cases | zero |
| Precision drift per step | ~0.5-1 ULP | zero |
| Drift after 1M steps | measurable | zero |
| Correction passes needed | periodic renorm | never |

## Net Assessment on H100

For compute-bound training with large batches, FP16 tensor cores are mature and well-optimized. The software ecosystem (cuBLAS, cuDNN, Flash Attention) is built for them. VDR would need its own kernel library to match the engineering polish.

For inference — memory-bound, single-batch or small-batch — VDR INT8 on tensor cores has a structural advantage. 2× throughput on tensor cores, 2× memory bandwidth utilization, no SFU bottleneck on softmax/activation, zero warp divergence, zero drift. The hardware already supports it because the quantization community already demanded INT8 tensor cores.

The irony is that the GPU industry built INT8 tensor cores to run approximate quantized models faster. VDR uses the same hardware to run exact integer models at the same speed. The infrastructure is already there. It just needs someone to write the kernels with the divmod-into-R discipline instead of the truncate-and-pray discipline.
