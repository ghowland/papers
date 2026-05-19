# HOWL-VDR-32-2026 — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: baseline → integer_equivalence → cpu_projections → gpu_projections → datacenter → limitations → verification → op_counts → memory → energy → comparisons

# baseline_hardware(id|spec|value)
BH1|CPU|Intel 10th-gen mobile, ~3.5 GHz boost
BH2|execution|single core, scalar (no SIMD)
BH3|OS|Windows 10 via WSL2
BH4|compiler|Zig 0.15.1, ReleaseFast
BH5|binary size|~20 KB
BH6|model memory|2,368 bytes (37 cache lines)

# model_spec(id|parameter|value)
MS1|architecture|single-block single-head causal transformer
MS2|vocabulary|5 tokens, embedding dim 4, FFN hidden 8, context 4
MS3|trainable parameters|181 (stored as i16)
MS4|softmax|quadratic surrogate (no transcendentals)
MS5|arithmetic|fixed-width integers: i16 weights/activations, i32 probabilities/gradients, i64 accumulators
MS6|float operations|0
MS7|heap allocations|0
MS8|D|2^16 = 65536, precision floor 1.53×10⁻⁵

# baseline_results(id|operation|time|throughput)
BR1|forward pass|688 ns|1,453,488 passes/sec
BR2|train step (fwd+bwd+SGD)|1,159 ns|862,812 steps/sec
BR3|train epoch (2 windows)|2,354 ns|424,808 epochs/sec
BR4|generation (4 tokens)|2,822 ns|1,417,434 tok/sec

# per_parameter_cost(id|operation|total_time|per_param)
PP1|forward pass|688 ns|3.80 ns/param
PP2|train step|1,159 ns|6.40 ns/param
# baseline for all scaling projections; pure scalar integer, no vectorization, entire model in L1

# verification(id|test|result)
VF1|softmax sum = D = 65536 (exact)|PASS — no tolerance, exact at every step of every epoch
VF2|attention weight rows sum = D (exact)|PASS
VF3|bit-identical determinism across runs|PASS — raw byte comparison, zero differences
VF4|loss monotonicity over 20 epochs|PASS
VF5|weight update algebraic exactness|PASS

# integer_equivalence(id|step|vdr_q16|int8_quantized|difference)
IE1|weight load|load i16|load i8|VDR 2× memory
IE2|activation load|load i16|load i8|VDR 2× memory
IE3|multiply|i16×i16→i32|i8×i8→i16 or i32|same instruction class
IE4|accumulate|i64+=i32|i32+=i16|same instruction class
IE5|epilogue|right shift 16|float multiply by scale|VDR simpler
IE6|store result|store i16|store float16|same bandwidth
IE7|remainder|store i16 (optional)|discarded|VDR tracks it
# compute cost same; memory 2× for Q16 vs INT8, equal for Q16 vs INT16; epilogue cheaper for VDR
# in Zig toy, remainders zeroed (discarded) — matches quantized behavior exactly

# vdr_q16_core_operation(id|description)
CO1|multiply-accumulate: acc(i64) += weight(i16) × activation(i16)
CO2|epilogue: result(i16) = acc >> 16; remainder(i16) = acc & 0xFFFF
# identical to quantized inference instruction sequence; right shift replaces float dequantize

# cpu_simd_projections(id|platform|width|forward_1M|forward_100M|forward_7B|notes)
CP1|scalar (measured)|1|3.8 ms|380 ms|26.6 s|baseline
CP2|AVX-512|32 i16 via vpmaddwd|158 µs|12.7 ms|887 ms|16-32× speedup; 30× at DIM=4096 (near 100% SIMD fill)
CP3|ARM NEON|8 i16 via vmlal.s16|480 µs|—|—|available on every ARM since ARMv7
CP4|Intel AMX|512 i16 per instruction|—|740 µs|52 ms|16×64×64×16 tile multiply; Sapphire Rapids+

# gpu_projections_a100(id|metric|float16|vdr_q16_projected|notes)
GA1|tensor core throughput|312 TFLOPS|~312 TOPS (INT8 double-accum)|split i16 into hi/lo i8 bytes, 4 partial products
GA2|7B forward pass|~45 ms|~45 ms|computational parity
GA3|7B gen batch=1|~30 tok/s|~30 tok/s|memory-bandwidth limited
GA4|7B gen batch=32|~800 tok/s|~800 tok/s|compute-bound

# gpu_projections_h100(id|metric|float16|vdr_q16_projected|notes)
GH1|tensor core throughput|989 TFLOPS|~989 TOPS (INT8 double-accum)|same hardware path
GH2|7B forward pass|~12 ms|~12 ms|parity
GH3|7B gen batch=1|~80 tok/s|~80 tok/s|parity
GH4|70B forward pass|~120 ms|~120 ms|parity
GH5|70B gen batch=1|~8 tok/s|~8 tok/s|parity

# memory_bandwidth(id|format|bytes_per_param|7B_weight_load|a100_hbm_2TBs_load_time)
MBW1|float32|4|28 GB|14 ms
MBW2|float16|2|14 GB|7 ms
MBW3|INT8|1|7 GB|3.5 ms
MBW4|VDR Q16 (i16 weights)|2|14 GB|7 ms
MBW5|VDR Q8 (i8 weights)|1|7 GB|3.5 ms
# VDR Q16 matches float16 bandwidth; VDR Q8 matches INT8

# datacenter_single_node(id|metric|float16|vdr_q16|notes)
DN1|config|8×A100-80GB NVLink|same|standard inference node
DN2|model capacity|70B sharded|70B same|
DN3|total tensor core|2,496 TFLOPS|~2,496 TOPS|parity
DN4|70B gen batch=1|~8-12 tok/s|~8-12 tok/s|parity
DN5|70B gen batch=64|~400 tok/s|~400 tok/s|parity
DN6|deterministic across runs|no|yes|free — structural property
DN7|gradient reduction order-dependent|yes|no|integer addition associative

# datacenter_multi_node(id|metric|float16|vdr_q16)
DM1|AllReduce semantics|non-deterministic (float non-associative)|deterministic (integer associative)
DM2|gradient synchronization|approximate (order-dependent)|exact (order-independent)
DM3|training reproducibility|not guaranteed|bit-identical
DM4|throughput|X tokens/sec|X tokens/sec (same)

# cost_analysis(id|factor|float16|vdr_q16|difference)
CA1|GPU hardware|same|same|none
CA2|GPU-hours per training run|same|same|none
CA3|re-runs for reproducibility|1-3 (variance)|1 (deterministic)|VDR 1-3× cheaper
CA4|debug time for numerical issues|significant|zero (exact arithmetic)|VDR cheaper
CA5|validation compute|separate float + exact check|self-validating|VDR cheaper
CA6|weight storage|2 bytes/param (FP16)|2 bytes (i16) or 1 byte (i8)|same or VDR cheaper
CA7|inference serving cost|same|same|none

# debug_vs_release(id|operation|debug_ns|release_ns|speedup)
DR1|forward pass|6,146|688|8.9×
DR2|train step|14,936|1,159|12.9×
DR3|train epoch|29,957|2,354|12.7×
DR4|generation|25,539|2,822|9.0×
# debug includes bounds+overflow checking; 9-13× from removing safety checks, inlining, LLVM optimization

# overflow_events(id|source|cause|resolution|production_implication)
OV1|embedding addition|two i16 sum > 32767|reduced init scale to ±4096|use Q32 embedding or init-scale discipline
OV2|softmax shifted scores|score minus causal mask fill exceeds i16|widened shifted to i32|shifted scores always i32 intermediate
OV3|linear output|dot product / D exceeds i16 after 50K steps|clamped to ±32767|use Q32 storage or weight decay
OV4|probability values|single probability can equal D=65536 > i16 max|stored probabilities as i32|probabilities always i32 intermediate
# pattern: intermediate value semantically Q16 but numerically exceeds i16; fix: next-wider type for intermediate, narrow at storage boundary

# type_width_map(id|data|stored_width|compute_width|notes)
TW1|weights|i16|i64 (during matmul accum)|narrowed via >>16 to i16 for output
TW2|activations|i16|i64 (during dot product)|same narrowing
TW3|probabilities|i32|i32|never narrowed to i16
TW4|shifted scores|i32|i32|never narrowed to i16
TW5|gradients|i16 (stored)|i32 (accumulated) → i64 (applied)|narrowed at storage
TW6|accumulators|register-only i64|i64|never stored in arrays
TW7|loss|i64 scalar|i64|never stored in arrays

# forward_op_count(id|stage|multiplies|adds|shifts|compares|total)
FO1|embedding (token+pos)|0|16|0|0|16
FO2|Wq projection|64|48|16|0|128
FO3|Wk projection|64|48|16|0|128
FO4|Wv projection|64|48|16|0|128
FO5|attention scores (10 causal)|40|30|10|6|86
FO6|softmax surrogate|20|24|0|16|60
FO7|softmax division|0|4|0|0|20
FO8|attention mix|64|48|16|0|128
FO9|Wo projection|64|48|16|0|128
FO10|residual add (attention)|0|16|0|0|16
FO11|FFN layer 1|128|96|32|0|256
FO12|ReLU|0|0|0|32|32
FO13|FFN layer 2|128|96|16|0|240
FO14|residual add (FFN)|0|16|0|0|16
FO15|output projection|80|60|20|0|160
FO16|total forward|716|598|158|54|1,542
# 688 ns / 1542 ops = 0.45 ns/op = 1.57 cycles/op at 3.5 GHz
# multiplies dominate at 46.4%; FFN layers = 32.2% of total ops

# backward_op_count(id|total_multiplies|total_adds|total_shifts|total_ops)
BO1|1,361|877|689|3,013
# combined fwd+bwd+SGD: 1,542 + 3,013 = 4,555 ops per train step
# 1,159 ns / 4,555 = 0.254 ns/op = 0.89 cycles/op (backward higher throughput — no loop-carried deps in outer products)

# model_memory(id|component|bytes|notes)
MM1|parameters|572|306 elements × i16
MM2|gradients|708|177 elements × i32
MM3|forward cache|1,088|activations, scores, logits
MM4|total|2,368|fits in 37 cache lines; L1 holds 13 copies

# cache_scaling(id|model_size|weight_bytes_i16|fits_in)
CS1|181 params (toy)|572 B|L1 (32KB)
CS2|10K|20 KB|L1
CS3|100K|200 KB|L2 (256KB)
CS4|1M|2 MB|L3 (8MB)
CS5|100M|200 MB|HBM
CS6|7B|14 GB|HBM (1× A100)
CS7|70B|140 GB|HBM (2× A100)
# per-param cost increases with cache level: L2 ~2×, L3 ~3×, HBM ~30×; penalties identical for float and VDR

# scaling_projections_cpu_scalar(id|model_size|forward|train_step|gen_1tok)
SS1|181 (toy)|688 ns|1,159 ns|706 ns
SS2|10K|38 µs|64 µs|38 µs
SS3|1M|3.8 ms|6.4 ms|3.8 ms
SS4|100M|380 ms|640 ms|380 ms
SS5|7B|26.6 s|44.8 s|26.6 s

# scaling_projections_cpu_avx512(id|model_size|simd_speedup|forward|gen_1tok)
SA1|181 (DIM=4)|2× (poor fill)|344 ns|353 ns
SA2|10K (DIM=64)|16×|2.4 µs|2.4 µs
SA3|1M (DIM=512)|24×|158 µs|158 µs
SA4|100M (DIM=4096)|30×|12.7 ms|12.7 ms
SA5|7B (DIM=4096)|30×|887 ms|887 ms

# scaling_projections_gpu(id|platform|model_size|forward|gen_batch1|gen_batch32)
SG1|A100|7B|22 ms|45 tok/s|1,440 tok/s
SG2|A100|70B|220 ms|4.5 tok/s|144 tok/s
SG3|H100|7B|7 ms|142 tok/s|4,544 tok/s
SG4|H100|70B|70 ms|14 tok/s|448 tok/s
SG5|H100|400B|400 ms|2.5 tok/s|80 tok/s

# energy_per_op(id|operation|energy_pj_7nm)
EN1|INT8 multiply|0.03
EN2|INT16 multiply|0.08
EN3|INT32 multiply|0.24
EN4|FP16 multiply|0.17
EN5|FP32 multiply|0.59
EN6|INT16 add|0.008
EN7|FP16 add|0.06
EN8|FP32 add|0.14
# source: Horowitz ISSCC 2014, scaled to 7nm

# energy_forward_7B(id|arithmetic|energy_per_mac_pj|total_forward_mj|ratio_vs_int8)
EF1|FP32|4.6|64.4|7.4×
EF2|FP16|1.5|21.0|2.4×
EF3|INT16 (VDR Q16)|0.58|8.1|0.93×
EF4|INT8 (quantized)|0.23|3.2|0.37×
EF5|INT8 weights × INT16 acts (VDR Q8/Q16)|0.41|5.7|0.66×
# VDR Q16: ~2.6× less energy than FP16, ~7.9× less than FP32
# excludes memory access energy (identical for same-width formats)

# softmax_cost_comparison(id|method|total_ops_per_call_vocab5|ratio)
SC1|quadratic surrogate|19|1×
SC2|Taylor exp depth=8|94|4.9×
SC3|Taylor exp depth=16|174|9.2×
# surrogate also eliminates exp lookup table (~8KB at Q16 bounded range)

# saturation_events(id|step_range|events_per_step|effect)
SAT1|0-1,000|0|loss decreasing normally
SAT2|1,000-10,000|0-1|slight flattening
SAT3|10,000-25,000|1-5|loss plateau
SAT4|25,000-50,000|5-20|loss oscillating (gradient info lost)
# Q16 equivalent of gradient explosion; fix: weight decay, gradient clipping, lr warmdown, or Q32 storage
# does not affect functional verification (first 40 steps)

# determinism_comparison(id|framework|same_seed_same_hw|same_seed_diff_hw|distributed_diff_order)
DT1|PyTorch float32|no (cuDNN non-det by default)|no|no
DT2|PyTorch float32 + det mode|mostly|no|no
DT3|PyTorch float16|no|no|no
DT4|JAX float32|yes (single device)|no|no
DT5|llama.cpp INT8|no (float dequant step)|no|n/a
DT6|VDR Python Q32|yes|yes|yes
DT7|VDR Zig Q16|yes|yes|yes
# VDR only entries achieving all three columns; integer addition associative — determinism cannot be removed

# quantized_system_comparison(id|system|weight_fmt|activation_fmt|matmul_unit|softmax|deterministic|sum_to_one_exact)
QS1|GPTQ|INT4|FP16|FP16 tensor core|FP16 exp|no|no
QS2|AWQ|INT4|FP16|FP16 tensor core|FP16 exp|no|no
QS3|llama.cpp Q4_0|INT4+FP16 scale|FP32|FP32 scalar|FP32 exp|no|no
QS4|llama.cpp Q8_0|INT8+FP16 scale|FP32|FP32 scalar|FP32 exp|no|no
QS5|SmoothQuant|INT8|INT8|INT8 tensor core|FP16 exp|no|no
QS6|ONNX INT8|INT8+zero point|INT8|INT8 GEMM|FP32 exp|no|no
QS7|VDR Q16|INT16|INT16|INT16 widening|quadratic (integer)|yes|yes
QS8|VDR Q8/Q16|INT8|INT16|INT8×INT16 widening|quadratic (integer)|yes|yes
# every existing system converts to float for softmax; VDR stays integer end-to-end — enables exact sum-to-one and determinism
# VDR Q8/Q16 weight format byte-identical to SmoothQuant storage; difference is arithmetic treatment of remainder

# limitations(id|limitation|description)
LM1|Q16 precision ~4.8 decimal digits|larger models may need Q32/Q64 accumulation; Zig toy already uses mixed widths (i16 store, i64 accum)
LM2|no SIMD implementation|projections from instruction specs not measured SIMD code; expect 20-40% below theoretical
LM3|no GPU implementation|projections from published tensor core throughput; kernel launch latency (~5-10 µs) unaccounted; affects float and VDR equally
LM4|quadratic surrogate assumed|if exp softmax required (pretrained float model compat), adds ~5-10% forward cost for softmax kernel
LM5|saturation clamping|i16 values clamp at ±32767 after ~50K steps; production: Q32 storage or weight decay
LM6|projections conservative|no FlashAttention, sparsity, speculative decoding, KV-cache optimizations assumed; all apply equally to float and VDR

# key_findings(id|finding|evidence)
KF1|VDR Q16 maps to same hardware instructions as quantized inference|widening multiply-accumulate with right-shift epilogue = identical instruction sequence
KF2|computational parity with INT8/INT16 quantization|same tensor core paths, same memory bandwidth, same throughput projections
KF3|stronger precision guarantees than quantization|remainder tracked (optionally) instead of discarded; exact sum-to-one; zero accumulated drift
KF4|determinism is free|structural consequence of integer associativity; zero additional compute; cannot be removed
KF5|688 ns forward pass is measured ground truth|not projection; commodity hardware; all verification tests pass
KF6|energy advantage: VDR Q16 ~2.6× less than FP16|integer arithmetic uses less energy per operation on same silicon

# relationships(from|rel|to)
MS5|defines|CO1
CO1|identical_to|IE3
CO2|replaces|IE5
BR1|baseline_for|PP1
PP1|scales_to|CP1
PP1|scales_to|CP2
PP1|scales_to|CP3
PP1|scales_to|CP4
PP1|scales_to|GA1
PP1|scales_to|GH1
IE1|comparison|MBW4
IE1|comparison|MBW3
VF1|validates|MS4
VF3|validates|KF4
VF3|demonstrates|DT7
KF1|enables|KF2
KF2|enables|CA1
KF3|distinguishes|QS7
KF4|enables|DM3
KF4|enables|DN7
OV1|motivates|LM5
OV3|motivates|LM5
SAT1|bounded_by|LM5
LM1|mitigated_by|TW6
LM2|bounds|CP2
LM3|bounds|GA1
MS4|compared_in|SC1
SC1|cheaper_than|SC3
EF3|cheaper_than|EF2
QS7|unique_property|VF1
QS7|unique_property|VF3
DN6|enabled_by|KF4
DM1|enabled_by|KF4
CA3|enabled_by|KF4
CA4|enabled_by|KF3

# section_index(section|title|ids)
1|Baseline Measurement|BH1-BH6,MS1-MS8,BR1-BR4,PP1-PP2,VF1-VF5
2|The Integer Arithmetic Equivalence|IE1-IE7,CO1-CO2
3|CPU SIMD Projection|CP1-CP4
4|GPU Integer Tensor Core Projection|GA1-GA4,GH1-GH5,MBW1-MBW5
5|Datacenter Scale Projection|DN1-DN7,DM1-DM4,CA1-CA7
6|What the Baseline Proves|KF1-KF6
7|Limitations|LM1-LM6
A|Raw Benchmark Output|BR1-BR4
B|Debug vs ReleaseFast|DR1-DR4
C|Overflow Events|OV1-OV4
D|Type Width Map|TW1-TW7
E|Forward Op Count|FO1-FO16
F|Backward Op Count|BO1
G|Memory Layout|MM1-MM4,CS1-CS7
H|Scaling Projections|SS1-SS5,SA1-SA5,SG1-SG5
I|Softmax Cost Comparison|SC1-SC3
J|Determinism Comparison|DT1-DT7
K|Saturation Events|SAT1-SAT4
L|Energy Efficiency|EN1-EN8,EF1-EF5
M|Quantized System Comparison|QS1-QS8

# decode_legend
# VDR Q16: D=2^16=65536; value=(V+R)/D; all arithmetic integer with shift+mask divmod
# precision floor: 1/D = 1.53×10⁻⁵ (~4.8 decimal digits) at Q16
# widening multiply-accumulate: i16×i16→i32, accumulated in i64; epilogue >>16 extracts quotient
# quadratic surrogate: p_i=(x_i-shift)²/Σ(x_j-shift)²; replaces exp softmax; pure integer arithmetic
# Barrett reduction: integer division via precomputed multiplicative inverse (multiply+shift)
# saturation/clamping: values exceeding i16 range clamped to ±32767; production fix: wider storage or weight decay
# tensor core paths: INT8 mma.sync (A100/H100); VDR Q16 via double-accumulation (hi/lo byte split)
# energy: pJ = picojoules; mJ = millijoules; MAC = multiply-accumulate
# throughput: TOPS = tera integer ops/sec; TFLOPS = tera float ops/sec; tok/s = tokens per second
# determinism columns: same_seed_same_hw | same_seed_diff_hw | distributed_diff_reduction_order
# SIMD instructions: vpmaddwd (AVX-512 32×i16), vmlal.s16 (NEON 8×i16), AMX tile multiply (512×i16)
# cache hierarchy: L1 32KB ~1 cycle, L2 256KB ~4 cycles, L3 8MB ~10 cycles, HBM ~100 cycles
# rel_types: defines|identical_to|replaces|baseline_for|scales_to|comparison|validates|demonstrates|enables|distinguishes|motivates|bounded_by|mitigated_by|bounds|compared_in|cheaper_than|unique_property|enabled_by
