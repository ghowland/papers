# HOWL-VDR-29-2026 — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → core_concept → basis_assignments → operations_cpu → operations_gpu → pipeline_workloads → costs → hardware_units → kernel_roadmap → lookup_tables → overflow_analysis → error_model → rebase_ops → quantization_comparison → reproducibility → float_special_values → relationships → section_index

# principles(id|principle|rationale)
P1|VDR triple [V, D, R] represents exact rational (V+R)/D|R is remainder within D frame, not external addend; R=0 is closed, R≠0 is active
P2|divmod rule: product>>bits gives V, product&mask gives R|when D is power-of-two, integer division reduces to shift+mask — one instruction each
P3|exactness guarantee: V+R always equals true integer numerator|no operation discards any portion of any intermediate; chain length irrelevant to error
P4|D is configuration choice not system constant|exactness holds at any D; choice affects dynamic range and hardware efficiency only
P5|Q335 is wrong for ML workloads|335-bit integers require multi-precision libraries (50-200× overhead); ML needs modest precision used exactly
P6|deinterleaved memory layout: separate V and R arrays|enables pure vertical SIMD — no shuffle/permute; one register load fills entirely with V or R values
P7|no D field stored per element|D is module-level constant per domain, known at compile time; type encodes domain
P8|lookup tables replace transcendental functions|bounded integer inputs have finite domain; precompute exact results at Q335, project to target basis via divmod
P9|Barrett reduction replaces float division|precompute multiplicative inverse of divisor; per-element cost is one multiply + one shift instead of 10-14 cycle vdivps
P10|schedule values precomputed at Q335 then projected to inference basis|projection via divmod is exact — remainder captures what target basis cannot absorb

# basis_assignments(id|stage|D|element_type|bytes_per_element|remainder_stored|rationale)
B1|weights (inference)|2^8|i8 V only|1|no (R=0 for frozen weights)|matches INT8 tensor cores; half FP16 memory
B2|activations (inference)|2^16|i16 V + i16 R|4|yes|wider dynamic range for accumulated contributions; 32 i16 per AVX-512 register
B3|gradient accumulation|2^64|i64 V + i64 R|16|yes|prevents overflow at any practical batch size
B4|diffusion schedule|2^32|i32 V + i32 R|8|yes|schedule constants need ~10 decimal digits
B5|diffusion latent|2^16|i16 V + i16 R|4|yes|matches activation basis

# zig_structures(id|name|description|key_fields)
Z1|Vdr16|activation element|v: i16, r: i16
Z2|Vdr32|schedule/accumulator element|v: i32, r: i32
Z3|Vdr64|gradient element|v: i64, r: i64
Z4|WeightMat|weight matrix, V only|rows: i32, cols: i32, stride: i32, data: [*]i8
Z5|ActivationMat|activation matrix, deinterleaved|rows: i32, cols: i32, stride: i32, v_data: [*]i16, r_data: [*]i16
Z6|LinearLayer|weight + bias|weight: WeightMat, bias_v: [*]i32, bias_r: [*]i32, bias_len: i32
Z7|AttentionHead|QKV + output projections|wq/wk/wv/wo: WeightMat, head_dim: i32
Z8|TransformerBlock|full block|heads: [*]AttentionHead, num_heads: i32, ffn_up/gate/down: LinearLayer, norm1/2 gamma/beta: [*]i16
Z9|DiffusionSchedule|precomputed schedule constants|timesteps: i32, betas/sqrt_alpha_bars/sqrt_one_minus/posterior_variance as v+r i32 pairs
Z10|DiffusionLatent|latent tensor, deinterleaved|channels/height/width: i32, v_data/r_data: [*]i16

# h100_hardware(id|unit|throughput_ops_per_SM_per_cycle|notes)
HW1|FP32 CUDA cores|128|float multiply, add, FMA
HW2|FP16 Tensor Cores|512|float matrix multiply-accumulate
HW3|INT32 CUDA cores|64|integer multiply, add, shift, bitwise
HW4|INT8 Tensor Cores|1024|integer matrix multiply-accumulate — 2× FP16 rate
HW5|Special Function Unit (SFU)|32|exp, log, rsqrt, sin, cos, division — 1/16 tensor core rate; bottleneck for all float transcendentals

# sfu_operations(id|operation|instruction|latency_cycles|throughput_ops_SM_cycle|used_by)
SFU1|exp2|MUFU.EX2|22|32|softmax
SFU2|log2|MUFU.LG2|22|32|cross-entropy loss
SFU3|rsqrt|MUFU.RSQ|22|32|layer norm
SFU4|rcp (1/x)|MUFU.RCP|22|32|softmax normalize, general division
SFU5|sin|MUFU.SIN|22|32|positional encoding
SFU6|cos|MUFU.COS|22|32|positional encoding
SFU7|tanh (via exp)|2× MUFU.EX2 + arith|~50|~16|GeLU, SiLU
# All replaced by table lookup or integer arithmetic in VDR at INT32 core rate (64 ops/SM/cycle) or full shared memory bandwidth

# operations_cpu_avx512(id|operation|float32_method|vdr_method|float_cycles_per_16elem|vdr_cycles_per_16elem|vdr_vs_float|advantage_source)
OC1|matmul inner loop|vfmadd231ps, 16 f32/reg, 3 instr/16 elem|vpmaddwd 32 i16/reg + shift + mask + 2 adds, 7 instr/32 elem|3 instr/16 elem|7 instr/32 elem|parity|2× element density offsets 2× instruction count
OC2|softmax|polynomial exp (6-8 instr, 4-5 ULP), horizontal reduce, vdivps 10-14 cyc|integer max reduce, table gather for exp (exact), integer sum reduce, Barrett (4 int ops)|39-47 cycles|43-48 cycles (but 2× packing)|1.5-2× faster|table lookup replaces polynomial; Barrett replaces float div
OC3|activation (GeLU)|polynomial tanh approx, 10-20 instr/elem|table lookup, 1 load/elem (256KB table fits L2)|10-20 instr|1 load|5-10× faster|table replaces polynomial chain
OC4|layer norm|float reduction + division (10+ cyc), rsqrt via hardware approx or Newton|integer sum + right shift (power-of-two hidden dim), rsqrt via table|15-25 cycles|8-12 cycles|1.5-2× faster|bit shift replaces float div; table replaces rsqrt
OC5|diffusion step|2 fmul + 1 fadd, 4 instr/16 elem|2 imul + 2 shift + 2 mask + 2 iadd, 12 instr/32 elem|~2 cyc/elem|~2-3 cyc/elem|0.7× raw; parity net after correction passes|correction pass elimination for chains >1000 steps
OC6|residual add|1 vaddps, 16 elem|V add + R add + carry check, 6 ops/32 elem|~1 cyc/elem|~1.3-1.5 cyc/elem|0.7× (float wins)|<0.1% of pipeline compute
# CPU full forward pass: VDR 1.3-1.6× faster; memory-bound regime favors 2× element density

# operations_gpu_h100(id|operation|fp16_method|vdr_method|fp16_rate|vdr_rate|vdr_vs_float|bottleneck_eliminated)
OG1|GEMM|FP16 tensor 16×16×16 tile, FP32 accum, 512 ops/SM/cyc|INT8 tensor 16×16×32 tile, INT32 accum (exact), 1024 ops/SM/cyc + shift+mask epilogue|~990 TFLOPS peak, 85-95% util|~1980 TOPS peak, 75-85% util (new kernels)|1.6-1.8× (effective)|memory bandwidth (INT8 weights half size)
OG2|softmax|SFU exp (32 ops/SM/cyc) + SFU div — bottleneck|shared memory table lookup (full BW) + Barrett (INT32 rate)|SFU-bottlenecked|full bandwidth|3-4×|SFU eliminated
OG3|activation (GeLU/SiLU)|SFU tanh/sigmoid, 32 ops/SM/cyc|table lookup shared memory, full BW|SFU-bottlenecked|full bandwidth|4-6×|SFU eliminated
OG4|layer norm|SFU rsqrt, 32 ops/SM/cyc|table or integer Newton + bit shift for division|SFU-bottlenecked|full rate|2-3×|SFU eliminated
OG5|warp divergence|denormals trigger FTZ or slow-path; NaN/Inf propagate; data-dependent masking|no special cases — no denormal, NaN, Inf, -0; every thread identical instructions every cycle|data-dependent|zero divergence|qualitative|entire category of edge-case handling eliminated

# memory_bandwidth(id|metric|fp16|vdr_int8)
MB1|bytes per weight|2|1
MB2|model size 7B params|14 GB|7 GB
MB3|minimum HBM load time (3.35 TB/s)|4.2 ms|2.1 ms
MB4|effective bandwidth utilization|1×|2×

# shared_memory_h100(id|metric|fp16|vdr_int8)
SM1|weight tile A (128×32)|8 KB|4 KB
SM2|activation tile B (32×128)|8 KB (f16)|8 KB (i16 V)
SM3|double buffer total|32 KB|24 KB
SM4|remaining for tables|32 KB|40 KB
SM5|typical table allocation (exp+gelu+rsqrt bounded)|0 (uses SFU)|10-36 KB
SM6|headroom after all|32 KB|4-30 KB

# forward_pass_7B(id|component|fp16_ms_per_layer|vdr_int8_ms_per_layer|speedup)
FP1|QKV projection|0.83|0.42|2.0×
FP2|attention GEMM|0.55|0.28|2.0×
FP3|softmax|0.036|0.009|4.0×
FP4|attention output projection|0.28|0.14|2.0×
FP5|FFN up + gate|1.10|0.55|2.0×
FP6|GeLU activation|0.008|0.002|4.0×
FP7|FFN down projection|0.55|0.28|2.0×
FP8|layer norm (×2)|0.008|0.004|2.0×
FP9|residual add (×2)|0.002|0.003|0.7×
FP10|per-layer total|3.37|1.69|2.0×
FP11|full forward (32 layers + embed/head)|~110 ms|~55 ms|2.0×

# pipeline_workloads(id|workload|fp16_perf|vdr_perf|vdr_advantage|notes)
PW1|inference single-batch 7B|~175 tok/s, 5.7 ms/tok|~323 tok/s, 3.1 ms/tok|1.85×|memory-bandwidth bound; 2× from half-size weights
PW2|inference batch=8 7B|~580 tok/s|~1050 tok/s|1.8×|transitioning to compute-bound
PW3|inference full-saturation (batch 64+)|baseline, 85-95% util|1.8× baseline, 75-85% util|1.8×|compute-bound; narrows slightly due to kernel maturity gap
PW4|diffusion single image (50 steps)|~755 ms|~380 ms|2.0×|chain too short for float drift correction; pure throughput advantage
PW5|diffusion 2-hour video (25.9M steps)|~113-117 hrs (incl 5-8% correction overhead)|~54 hrs|2.1×|VDR eliminates ~25,920 correction passes; bit-identical reproduction; zero color shift/flicker
PW6|training 7B|baseline (FP16 mixed precision)|1.5-1.7× baseline|1.5-1.7×|backward pass uses wider types reducing tensor core advantage; eliminates loss scaling, gradient clipping, epsilon params

# drift_model(id|chain_length|float64_drift_per_element|vdr_drift|context)
DR1|1|~1×10^-15|0|single step
DR2|50|~5×10^-14|0|single image generation
DR3|1,000|~1×10^-12|0|short video clip
DR4|10,000|~1×10^-11|0|7 min at 24fps
DR5|100,000|~1×10^-10|0|1.2 hours
DR6|1,000,000|~1×10^-9|0|4.6 days continuous
DR7|8,640,000|~1.9×10^-8|0|2-hour film (24fps × 150 steps)
DR8|25,920,000|~2.6×10^-7|0|2-hour film 3 cycles
# VDR drift is structurally zero — mathematical property of integer arithmetic, not empirical measurement

# qualitative_properties(id|property|float_fp16_fp32|vdr_int8_16_64)
QP1|per-operation precision loss|up to 0.5 ULP|zero
QP2|accumulated drift over chain|grows with chain length|zero at any length
QP3|deterministic reproduction|no (operation-order dependent)|yes (bit-identical)
QP4|NaN possible|yes|no
QP5|Inf possible|yes|no
QP6|denormals|yes (FTZ or slow path)|no (not representable)
QP7|warp divergence from special values|possible|impossible
QP8|epsilon parameters required|many (layer norm, optimizer, etc.)|zero
QP9|correction passes for long chains|periodic|never
QP10|loss scaling for training|required|not needed
QP11|gradient clipping for stability|required|not needed
QP12|probability distribution sums|≈ 1|= 1
QP13|cross-platform consistency|no guarantee|guaranteed

# costs_limitations(id|limitation|description|mitigation)
CL1|residual add slower|1.3-1.5× float advantage from single-add vs add-add-carry|<0.1% of total pipeline compute; immaterial
CL2|kernel maturity gap|cuBLAS/cuDNN decades of optimization; VDR kernels unbuilt|projections assume 75-85% util (Phase 3); hardware headroom to 95%
CL3|Q16 lookup table size|65536 entries × 4B = 256KB exceeds 64KB shared memory|restrict to bounded input range (4-16KB) or use L2; Q8 tables trivially fit (1KB)
CL4|basis selection is new engineering decision|D too small → saturation; D too large → overflow risk|validate per model family at load time; one-time cost analogous to quantization param selection
CL5|activation memory doubled|V+R = 4 bytes per element vs 2 bytes FP16|equals FP32; inference activations on-chip only; training depends on checkpoint strategy
CL6|ecosystem absent|no PyTorch/JAX/TF/ONNX/TensorRT support|multi-year engineering investment independent of arithmetic properties

# overflow_analysis(id|context|max_single_product|reduction_dim_K|worst_case_accumulation|fits_i32|mitigation)
OV1|matmul (i8×i16→i32)|127×32767=4,161,409|4096|17,045,131,264|no|tile reduction K=512 fits i32 (2,130,641,408); sum tiles in i64
OV2|softmax sum (i16)|32767|seq=2048|67,138,816|yes|i32 sufficient for seq≤~65K; i64 for 128K+
OV3|gradient accum (i32)|2^31|batch=4096|~8.8×10^12|no (needs i64)|i64 range ~9.2×10^18; safe for batch ≤ 2^32

# rebase_operations(id|source|destination|direction|operation|exact|cost)
RB1|weight Q8|accumulator Q32|forward matmul|widening multiply i8×i16→i32, inherent in tensor core|yes|zero
RB2|accumulator Q32|activation Q16|post-matmul epilogue|right shift 16, mask low 16|yes|2 instr/elem
RB3|activation Q16|attention score Q16|QK^T matmul|i16×i16→i32, shift+mask back|yes|part of matmul+epilogue
RB4|activation Q16|gradient Q64|backward pass|sign extension i16→i64|yes|1 instr/elem
RB5|gradient Q64|weight update Q8|optimizer step|right shift 56, mask low 8|yes|2 instr/elem
RB6|schedule Q32|latent Q16|diffusion step|right shift 16, mask low 16|yes|2 instr/elem
# every rebase is shift+mask (divmod); remainder captures exactly what target basis cannot absorb

# remainder_propagation(id|boundary|remainder_width_bits|decimal_digits|treatment)
RP1|Q32→Q16 (accum to activation)|16|5|stored in R channel of activation
RP2|Q64→Q8 (gradient to weight)|56|17|accumulated over updates via stochastic rounding or explicit remainder tracking
RP3|Q32→Q16 (schedule to latent)|16|5|stored in R channel of latent

# quantization_comparison(id|property|PTQ|QAT|VDR_fixed_basis)
QC1|representation|integer (typically i8)|integer (typically i8)|integer (i8/i16/i64)
QC2|scale factor|float (per-tensor or per-channel)|float (learned)|fixed power-of-two (implicit, no storage)
QC3|zero point|integer offset|integer offset (learned)|zero (symmetric, no offset)
QC4|remainder handling|truncated (lost)|truncated (trained to tolerate)|stored exactly in R channel
QC5|arithmetic during inference|integer matmul + float rescale|integer matmul + float rescale|integer matmul + integer shift/mask
QC6|float operations required|yes (rescale, softmax, norm)|yes (rescale, softmax, norm)|no (all-integer pipeline)
QC7|accumulated error|yes (truncation per layer)|yes (smaller)|zero
QC8|requires calibration data|yes|no (uses training data)|no (basis is hardware-determined)
QC9|requires retraining|no|yes|no
QC10|cross-layer error propagation|yes|yes (smaller)|zero
# fundamental difference: existing quantization truncates what doesn't fit; VDR stores it in R

# error_model(id|error_type|float_behavior|vdr_behavior)
ER1|representation error|rounds to nearest representable|exactly represented as V+R over D
ER2|arithmetic error|rounds per IEEE 754|exactly represented via divmod
ER3|accumulation error|grows with chain length|zero (no per-step error)
ER4|cancellation error|catastrophic precision loss possible|exact (integer subtraction exact)
ER5|method error|present (inherent to algorithm)|present (same — VDR is exact arithmetic not exact mathematics)
ER6|model error|present|present
ER7|quantization error|mantissa truncation|basis-width truncation captured in R
# VDR eliminates ER1-ER4 entirely; ER5-ER6 unchanged; ER7 captured not lost

# error_depth_composition(id|metric|fp16|fp32|vdr_q16)
ED1|error per operation|≤5×10^-4|≤6×10^-8|0
ED2|error per layer (~10 ops)|~1.6×10^-3|~1.9×10^-7|0
ED3|error after 32 layers|~9×10^-3|~1.1×10^-6|0
ED4|error after 128 layers|~1.8×10^-2|~2.1×10^-6|0

# precision_equivalence(id|float_format|mantissa_bits|vdr_basis_equiv|vdr_int_type|bytes_V_plus_R)
PE1|FP8 (E4M3)|3|D=2^4|i8|2
PE2|FP8 (E5M2)|2|D=2^3|i8|2
PE3|FP16|10|D=2^11|i16|4
PE4|BF16|7|D=2^8|i16|4
PE5|FP32|23|D=2^24|i32|8
PE6|FP64|52|D=2^53|i64|16
PE7|Q335 (VDR physics)|n/a (~101 decimal)|D=2^335|multi-precision|~84 per V
# float allocates bits to mantissa+exponent; VDR integer uses all bits for value precision within fixed range

# float_special_values(id|value|how_it_arises|effect|vdr_equivalent)
FS1|denormal|gradients near zero, weight decay products|10-100× slower or FTZ (silent precision loss)|impossible — no subnormal representation
FS2|+Inf|overflow in exp(), large accumulations|propagates through multiply, poisons sums|impossible
FS3|-Inf|log(0), negative overflow|same propagation|impossible
FS4|NaN|0/0, Inf-Inf, Inf×0|propagates through everything, silent corruption|impossible
FS5|-0|rounding, sign preservation|comparison anomaly: -0==+0 but 1/-0=-Inf|impossible — integers have one zero

# float_mitigations(id|event|frequency|mitigation|mitigation_cost|vdr_status)
FM1|gradient underflow to denormal|every batch|FTZ or loss scaling|FTZ: silent loss; scaling: extra multiply per op|impossible
FM2|gradient overflow to Inf|rare but catastrophic|gradient clipping|comparison + conditional per param per step|impossible
FM3|NaN from unstable softmax|occasional|max subtraction trick|extra reduction pass per softmax|impossible
FM4|NaN from log(0)|occasional|epsilon addition to probabilities|extra add per element|impossible
FM5|Inf from exp() overflow|occasional|max subtraction trick|extra reduction pass|impossible

# float_nonreproducibility_sources(id|source|mechanism|affected_by)
NR1|operation reordering|float add not associative: (a+b)+c ≠ a+(b+c)|thread scheduling, compiler optimization
NR2|warp scheduling|different warps reduce partial sums in different order|GPU workload, thermal state
NR3|cuBLAS algorithm selection|different tiling strategies per problem size|library version, GPU model
NR4|FMA availability|FMA gives different result than separate mul+add|compiler flags, target arch
NR5|denormal handling mode|FTZ on vs off changes results near zero|CUDA driver config
NR6|cross-platform differences|different intermediate precision|GPU model

# vdr_reproducibility_guarantees(id|property|guarantee|mechanism)
VR1|associativity of accumulation|order does not matter|mathematical property of integers
VR2|cross-run consistency|identical outputs every run|no data-dependent rounding, no scheduling sensitivity
VR3|cross-platform consistency|identical outputs on any hardware|integer arithmetic identical on all platforms
VR4|cross-library consistency|no algorithm selection variability|fixed kernel, no heuristic dispatch
VR5|deterministic seeding|identical generation given same seed|integer comparison for sampling
VR6|bit-identical checkpoints|model state serializes/deserializes identically|integers round-trip exactly
# unconditional guarantees from mathematical properties, not configuration-dependent

# lookup_tables(id|function|q8_entries|q8_size|q16_bounded_entries|q16_bounded_size|storage)
LT1|exponential (softmax)|128 (bounded)|256 B|2048|8 KB|shared memory
LT2|GeLU|128 (practical)|256 B|8192|32 KB|shared memory or L1
LT3|reciprocal sqrt (layer norm)|n/a|n/a|9900 (practical)|~40 KB|shared memory; Q32 uses Newton instead
# construction: define input grid → compute at Q335 → project to target basis via divmod → store V and R arrays → validate roundtrip
# tables are immutable read-only artifacts computed once per basis choice

# basis_selection_by_architecture(id|architecture|weight_basis|activation_basis|notes)
BA1|GPT/LLaMA (decoder-only)|2^8|2^16|standard transformer, well-bounded activations
BA2|BERT/encoder models|2^8|2^16|same structure, shorter sequences
BA3|Vision Transformer (ViT)|2^8|2^16|patch embeddings may need wider activation basis
BA4|U-Net (diffusion backbone)|2^8|2^16|skip connections accumulate — monitor for overflow
BA5|DiT (diffusion transformer)|2^8|2^16|standard transformer structure
BA6|Mixture of Experts|2^8|2^16|router softmax benefits from exact sum=1
BA7|State Space Models (Mamba)|2^8|2^32|recurrent accumulation may need wider basis
BA8|RWKV/linear attention|2^8|2^32|long-range accumulation, wider basis safer

# basis_selection_by_hardware(id|hardware|register_width|weight_D|activation_D|tensor_core_mode)
BH1|AVX-512 (Intel/AMD)|512 bits|2^8 (64/reg)|2^16 (32/reg)|n/a (SIMD only)
BH2|AVX2|256 bits|2^8 (32/reg)|2^16 (16/reg)|n/a
BH3|NEON (ARM)|128 bits|2^8 (16/reg)|2^16 (8/reg)|n/a
BH4|H100 tensor cores|INT8 native|2^8|2^16|INT8 mma.sync
BH5|H100 INT32 cores|32-bit|n/a|2^16|scalar integer
BH6|Apple M-series AMX|INT8/INT16 native|2^8|2^16|AMX tiles
BH7|TPU v5|INT8 native|2^8|2^16|INT8 systolic

# hardware_availability(id|unit|first_available|notes)
HA1|INT8 multiply-accumulate|2017 (Volta V100)|all NVIDIA GPUs since
HA2|INT8 tensor cores|2020 (Ampere A100)|A100, H100, B100, successors
HA3|INT32 CUDA cores|2006 (Tesla/G80)|all NVIDIA GPUs
HA4|AVX-512 integer|2017 (Skylake-X)|Intel Xeon, some consumer
HA5|AVX-512 VNNI|2019 (Cascade Lake)|Intel Xeon 2nd gen+
HA6|ARM NEON integer|2011 (ARMv8)|all modern ARM
HA7|Apple AMX INT8|2020 (M1)|all Apple Silicon
HA8|TPU INT8 systolic|2018 (TPU v3)|Google Cloud
# no hardware development required; every unit VDR targets has been in production 6+ years

# kernel_roadmap(id|phase|scope|duration|target_utilization|precedent)
KR1|Phase 1: functional correctness|all 8 kernel types, verified vs Python ref|3-4 months|40-60%|CUTLASS initial
KR2|Phase 2: basic optimization|tiling, double-buffering, occupancy|2-3 months|65-75%|CUTLASS 2.x
KR3|Phase 3: competitive performance|warp scheduling, register alloc, table co-residency|3-6 months|75-85%|this paper's projections
KR4|Phase 4: near-peak|arch-specific tuning, autotuning, operator fusion|6-12 months|85-95%|cuBLAS maturity

# kernel_priority(id|kernel|reason)
KP1|GEMM (INT8 tensor core)|dominates compute, largest throughput advantage
KP2|softmax (table + Barrett)|largest per-op speedup (3-4×), per head per layer
KP3|attention (fused QKV+softmax+output)|combines KP1+KP2, eliminates memory round-trips
KP4|GeLU/activation (table lookup)|simple, large speedup, enables fused FFN
KP5|layer norm (integer)|medium complexity, enables fused transformer block
KP6|diffusion step (scale+add)|simple, critical for video pipeline
KP7|residual add (V+R+carry)|trivial, low priority
KP8|embedding lookup (widening copy)|trivial, memory-bound

# cache_line_packing(id|layout|element_type|elements_per_64B_line)
CP1|Float32|f32|16
CP2|Float16|f16|32
CP3|VDR i16 interleaved (v,r,v,r)|i16 pairs|16
CP4|VDR i16 deinterleaved V line|i16 V only|32
CP5|VDR i16 deinterleaved R line|i16 R only|32
CP6|VDR i8 weights (V only)|i8|64

# avx512_register_utilization(id|load_type|elements_per_zmm|bits_per_element|useful_bits)
RU1|vmovaps (float32)|16|32|23 mantissa + 8 exp + 1 sign
RU2|vmovdqu16 (VDR weight i8→i16)|32|16|16 (all useful, no exponent overhead)
RU3|vmovdqu16 (VDR activation V)|32|16|16
RU4|vmovdqu8 (VDR weight raw)|64|8|8

# Q335_validation
# 921 tests across 38 mathematical/computational domains
# 903 passed, 18 failed — all 18 failures traced to test-design errors
# zero failures from incorrect VDR arithmetic
# Zig implementation targets same arithmetic on same foundations
# fixed-basis ML specialization is simpler subset (closed arithmetic, power-of-two bases only)

# relationships(from|rel|to)
P1|defines|P2
P2|enables|P3
P4|enables|B1
P4|enables|B2
P4|enables|B3
P5|motivates|B1
P5|motivates|B2
P6|optimizes|OC1
P6|optimizes|OG1
P7|reduces|MB1
P8|enables|OC2
P8|enables|OC3
P8|enables|OG2
P8|enables|OG3
P9|enables|OC2
P9|enables|OG2
P10|enables|OC5
B1|used_by|Z4
B1|used_by|Z7
B2|used_by|Z5
B2|used_by|Z1
B3|used_by|Z3
B4|used_by|Z9
B5|used_by|Z10
Z4|component_of|Z6
Z6|component_of|Z8
Z7|component_of|Z8
Z9|uses|Z10
HW4|enables|OG1
HW5|bottlenecks|OG2
HW5|bottlenecks|OG3
HW5|bottlenecks|OG4
OG1|dominates|FP10
OG2|eliminates_bottleneck|HW5
OG3|eliminates_bottleneck|HW5
OG4|eliminates_bottleneck|HW5
MB4|enables|PW1
OG1|enables|PW3
PW5|demonstrates|QP2
PW5|demonstrates|QP3
CL2|limits|OG1
CL3|constrains|LT2
CL3|constrains|LT3
CL6|blocks|PW1
OV1|mitigated_by|RB2
QC4|distinguishes|QC1
QC4|distinguishes|QC2
ER1|eliminated_by|P3
ER2|eliminated_by|P2
ER3|eliminated_by|P3
ER4|eliminated_by|P3
FS1|impossible_in|QP6
FS2|impossible_in|QP5
FS3|impossible_in|QP5
FS4|impossible_in|QP4
RB1|boundary_of|B1
RB2|boundary_of|B2
RB3|boundary_of|B2
RB4|boundary_of|B3
RB5|boundary_of|B1
RB6|boundary_of|B5
KR3|assumed_by|OG1
KR3|assumed_by|PW1
KP1|implements|OG1
KP2|implements|OG2
KP3|composes|KP1
KP3|composes|KP2
VR1|enables|QP3
VR3|enables|QP13
NR1|prevented_by|VR1

# section_index(section|title|ids)
1|The Problem: What Floating Point Discards|ER1,ER2,ER3,ER4,FS1,FS2,FS3,FS4,FS5,NR1,NR2,QP1,QP4,QP5,QP6,QP8,QP12
2|VDR: The Triple [V, D, R]|P1,P2,P3,P4
2.1|The divmod Rule|P2
2.2|Exactness Guarantee|P3
3|Q335 and Why We Do Not Use It Here|P5
4|Choosing the Basis for ML Workloads|B1,B2,B3,B4,B5
5|Zig Data Structures|Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10,P6,P7
6|CPU SIMD Performance|OC1,OC2,OC3,OC4,OC5,OC6
7|GPU Performance: H100 Tensor Cores|HW1,HW2,HW3,HW4,HW5,OG1,OG2,OG3,OG4,OG5,MB1,MB2,MB3,MB4,SM1,SM2,SM3,SM4,SM5,SM6
7.8|GPU Full Forward Pass|FP1,FP2,FP3,FP4,FP5,FP6,FP7,FP8,FP9,FP10,FP11
8|Full Pipeline: Production Workloads|PW1,PW2,PW3,PW4,PW5,PW6
9|Costs and Limitations|CL1,CL2,CL3,CL4,CL5,CL6
10|Results Summary|all operation and pipeline tables
A|Basis Selection Methodology|PE1,PE2,PE3,PE4,PE5,PE6,PE7
B|Barrett Reduction|P9
C|Lookup Table Construction|LT1,LT2,LT3,P8
D|Diffusion Schedule Precomputation|P10,B4,B5
E|VDR Reference Validation|Q335_validation block
F|Complete Instruction Sequences|SFU1,SFU2,SFU3,SFU4,SFU5,SFU6,SFU7,CP1,CP2,CP3,CP4,CP5,CP6,RU1,RU2,RU3,RU4
G|Memory Layout Diagrams|CP1-CP6,RU1-RU4,SM1-SM6
H|Accumulator Overflow Analysis|OV1,OV2,OV3
I|Precision Equivalence Mapping|PE1-PE7
J|Drift Accumulation Model|DR1-DR8
K|Basis Selection Decision Matrix|BA1-BA8,BH1-BH7
L|Float Special Value Incidence|FS1-FS5,FM1-FM5
M|Cross-Domain Basis Bridging|RB1-RB6,RP1-RP3
N|Comparison with Existing Quantization|QC1-QC10
O|Lookup Table Specifications|LT1-LT3
P|Comparison of Error Models|ER1-ER7,ED1-ED4
Q|Hardware Availability Timeline|HA1-HA8
R|Kernel Development Roadmap|KR1-KR4,KP1-KP8
S|Reproducibility Guarantees|NR1-NR6,VR1-VR6

# decode_legend
# basis: D = 2^n, power-of-two denominator; divmod = shift+mask
# element types: i8|i16|i32|i64 — signed integers at stated width
# V: value slot (quotient in D frame); R: remainder slot (exact residual); D: denominator (never stored per-element)
# closed: R=0; active: R≠0
# throughput units: ops/SM/cycle (GPU), instructions or cycles per N elements (CPU)
# ULP: unit in last place — minimum float precision unit
# FTZ: flush to zero — GPU mode that silences denormals by replacing with 0
# SFU: Special Function Unit — dedicated GPU hardware for transcendentals, 32 ops/SM/cycle on H100
# Barrett reduction: integer division via precomputed multiplicative inverse + shift
# mma.sync: tensor core matrix multiply-accumulate instruction
# vpmaddwd: AVX-512 packed multiply-add word to doubleword (32 i16×i16 → 16 i32 pairwise sums)
# utilization: fraction of peak hardware throughput achieved by kernel implementation
# TOPS: tera operations per second (integer); TFLOPS: tera floating-point operations per second
# Q8/Q16/Q32/Q64/Q335: shorthand for D=2^8/2^16/2^32/2^64/2^335
# rel_types: defines|enables|motivates|optimizes|reduces|used_by|component_of|uses|dominates|eliminates_bottleneck|bottlenecks|demonstrates|limits|constrains|blocks|mitigated_by|distinguishes|eliminated_by|impossible_in|boundary_of|assumed_by|implements|composes|enables|prevented_by
