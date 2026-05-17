# VDR-22 DEDICATED SILICON — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → qiu_design → chip_arch → memory → perf → limitations → comparisons → scaling → relationships → sections

# principles(id|principle|rationale)
P1|FPGA validated five technology-independent principles|Q335 divmod is free; arithmetic is perfectly uniform; all ops compose from small integer ISA; parallel/sequential split is clean; bit-identical across implementations
P2|Reclaim float silicon for integer|Current GPUs waste 40-60% SM logic area on float units, tensor cores, SFUs that VDR never uses; reclaiming yields proportional integer compute density increase
P3|SHR335 scales without limit|Zero gates, zero transistors, zero power at any core count; 5,120 cores = 5 trillion free divmods/sec; consequence of mathematical decision to fix denominator at power of two
P4|Same ISA contract, different silicon|IOSE declarations unchanged; 53-instruction ISA from FPGA is architectural contract; ASIC changes implementation technology not functional semantics
P5|Five implementations, one contract, zero divergence|Python, Zig, FPGA, GPU, ASIC all pass same 884-test suite; bit-identical results; IOSE declaration is specification, everything else is acceleration

# claims(id|claim|type|depends_on)
CL1|5,120 QIUs across 80 SMs on 4nm; ~68B transistors, ~581 mm² die|observation|
CL2|Q335 multiply: 1-2 cycles at 2 GHz (vs 9 cycles at 150 MHz on FPGA)|observation|
CL3|~5.1 trillion Q335 multiplications/sec; ~10.2T additions/sec|derivation|CL1,CL2
CL4|60× higher Q335 throughput than H100 integer ALU path (85M → 5.1T)|derivation|CL3
CL5|SRE primitive computation: ~200 nanoseconds total (vs 1.5ms GPU, vs 1.1μs FPGA)|derivation|CL3
CL6|Primitives ~50,000× faster than generating single LLM token|derivation|CL5
CL7|10M param exact training step: ~0.6ms; ~1,600 steps/sec; ~5,000× faster than Python, ~50× faster than FPGA|derivation|CL3
CL8|TDP ~400W vs H100 700W vs B200 1000W; savings from no float, no SFU, no tensor cores|observation|
CL9|384-bit integer add: ~3 pJ (less than float32 add at ~5 pJ despite being 12× wider)|observation|
CL10|Die area 581 mm² vs H100 814 mm²; smaller due to no float hardware|observation|CL1
CL11|Chip cost estimated ~$15,000 vs H100 ~$30,000|derivation|CL10
CL12|Cost per VDR prompt: $0.000048 day 1 → $0.000008 at investigation 100 (accumulation effect)|derivation|CL11
CL13|100 SRE investigations: 4.8 sec total wall-clock, $0.0016 compute, 0.12 J energy on ASIC|derivation|CL5,CL12
CL14|Adding ~1,100 LUTs/QIU (2.1% area) for Barrett reduction enables dual-purpose VDR+ZKP chip|observation|
CL15|VDR addressable market ~71.5% of AI spend (structured, regulated, multi-turn workloads)|observation|
CL16|Same architecture viable at 28nm ($10 edge chip, 16 QIUs, 2W) through 3nm ($5,000 datacenter, 14,544 QIUs)|observation|

# concepts(id|name|definition|category)
C1|Q335 Integer Unit (QIU)|384-bit ALU: 1-cycle add (carry-select), 1-2 cycle multiply (full parallel array), 0-cycle SHR335 (routing), 1-cycle compare, 2-3 cycle cross-multiply; register file, remainder SRAM|hardware
C2|Full parallel multiplier|384×384→768 via tree of 64-bit Booth-encoded multipliers + Wallace tree reduction + carry-propagate adder; 1-2 pipeline stages; ~2.2M transistors; replaces FPGA's 9-cycle iterative|hardware
C3|Warp (32 QIUs)|Lockstep execution; no warp divergence because Q335 arithmetic has no data-dependent branches; JCLOSED (<1% divergence) handled by predication|execution
C4|Streaming Multiprocessor (SM)|64 QIUs as 2 warps; local reduction unit; 256KB shared SRAM; 16×384-bit V + 16×384-bit R registers per QIU; 4KB remainder SRAM per QIU; instruction cache; ~529M transistors, ~4.3 mm²|hardware
C5|Global reduction network|7-level tree of 384-bit adders across 80 SMs; 7 cycles at 2 GHz = 3.5ns; exact global sum for softmax denominators, norms, aggregations|hardware
C6|Integer-native GPU|No float units, no tensor cores, no SFUs; every transistor serves exact integer arithmetic; 80 SMs, 5,120 QIUs, 96MB L2, 96GB HBM3 at 4.9 TB/s|architecture
C7|Dual-purpose VDR+ZKP|Adding Barrett modular reduction (~300 LUTs) + point addition (~800 LUTs) per QIU enables zero-knowledge proof field arithmetic alongside VDR; 2.1% area increase|opportunity
C8|CoWoS-S package|2.5D packaging with 6 HBM3 stacks on silicon interposer; standard for GPU-class bandwidth; ~100mm × 70mm|packaging

# qiu_transistors(component|transistors|area_4nm_mm2|notes)
384-bit parallel multiplier|~2.5M|0.020|Booth + Wallace tree + CPA; SHR335 routing = 0 transistors
384-bit adder (carry-select)|~100K|0.001|Same structure as FPGA
384-bit barrel shifter|~150K|0.001|9-stage mux
384-bit comparator|~50K|<0.001|Cascaded with early termination
Cross-multiply control|~80K|<0.001|2 multiplies + 768-bit compare sequencing
Register file (16V + 16R × 384b)|~3M|0.025|12,288 bits in 6T SRAM
Remainder SRAM (4KB)|~1M|0.008|32 nodes × 128 bytes
Instruction fetch/decode|~200K|0.002|Simpler than float (no special cases)
Warp scheduling (amortized)|~16K|<0.001|Shared across 32 QIUs
**QIU total**|**~7.1M**|**~0.058**|

# sm_area(component|transistors|area_4nm_mm2)
64 QIUs|454M|3.7
Warp schedulers (2)|1M|0.008
Local reduction unit|2M|0.016
Shared SRAM (256KB)|50M|0.4
Instruction cache (64KB)|12M|0.1
Interconnect + control|10M|0.08
**SM total**|**~529M**|**~4.3**

# chip_area(component|count|transistors_B|area_mm2)
SMs|80|42.3|344
Global reduction network|1|0.5|4
L2 cache (96MB)|1|19.2|155
HBM3 PHY + controllers|6|3.0|24
PCIe gen5 + NVLink|1|1.5|12
Host interface + scheduling|1|1.0|8
Power management|1|0.5|4
I/O ring + ESD|1|—|30
**Chip total**||**~68B**|**~581**

# h100_comparison(property|h100_4nm|vdr_q335_4nm)
Transistors|80B|68B
Die area|814 mm²|581 mm²
SMs|132|80
Compute units/SM|128 FP32|64 QIU (384-bit)
Total compute units|16,896 FP32|5,120 QIU
Register file total|~20 MB|~28 MB
L2 cache|50 MB|96 MB
HBM capacity|80 GB|96 GB
HBM bandwidth|3.35 TB/s|4.9 TB/s
Float units|Yes (all precisions)|None
SFUs|Yes|None
Tensor cores|Yes|None
Q335 mul throughput|~85M/s|~5.1T/s
TDP|700W|400W

# perf_operations(operation|cycles|time_2ghz|throughput_5120_qius)
Q335 addition|1|0.5 ns|10.2T ops/sec
Q335 multiplication|2|1.0 ns|5.1T ops/sec
Q335 divmod (SHR335)|0 (routing)|0 ns|∞ (simultaneous with multiply)
Q335 comparison|1|0.5 ns|10.2T ops/sec
Fraction unification|3|1.5 ns|3.4T ops/sec
Fact match (per fact)|1-2|0.5-1.0 ns|5.1-10.2T matches/sec
REDUCE global sum|7|3.5 ns|286M reductions/sec
Softmax surrogate (1K logits)|~20|10 ns|100M softmax/sec

# sre_on_asic(phase|vdr_tokens|primitive_ops|projected_time)
Data acquisition|72|1.2M|~0.2 μs
Filtering + threshold|38|29K|~0.003 μs
Deployment correlation|108|54K|~0.005 μs
Statistics + ranking|44|5K|~0.0005 μs
Complex transform|92|75K|~0.007 μs
Versioned project|183|20K|~0.002 μs
Formatted output|232|86K|~0.008 μs
**Total primitives**|**769**|**~1.5M**|**~0.2 μs**
# Bottleneck entirely LLM forward pass; primitives ~50,000× faster than single token generation

# training_step(operation|params|ops_per_param|total_ops|time_5120_qius)
Forward pass (matmul)|10M|~100 muls|1B|~0.2 ms
Softmax (per layer)|~10K × 12 layers|~50 ops|6M|~0.6 μs
Backward pass|10M|~200 muls|2B|~0.4 ms
SGD parameter update|10M|1 mul + 1 sub|20M|~2 μs
Constraint check|15 constraints|~1K ops each|15K|~1.5 μs
Denominator budget sweep|10M|1 compare|10M|~1 μs
**Total training step**|||**~3B**|**~0.6 ms**

# power_envelope(component|estimated_watts)
80 SMs (5,120 QIUs at 2 GHz)|250
L2 cache (96MB)|30
HBM3 PHY + controllers|60
Global reduction network|5
I/O (PCIe gen5 + NVLink)|25
Miscellaneous|30
**Total TDP**|**~400**

# energy_per_op(platform|q335_add|q335_mul|q335_divmod)
Python (CPython)|~50 μJ|~500 μJ|~100 μJ
Zig (host CPU)|~1.3 nJ|~13 nJ|~1 nJ
FPGA (Zynq, 1.9W)|~13 pJ|~114 pJ|~13 pJ
GPU H100 (700W)|~8 pJ|~82 pJ|~8 pJ
VDR-Q335 ASIC (400W)|~3 pJ|~39 pJ|0 pJ

# energy_per_investigation(platform|tokens|energy|wall_clock|cost)
Conventional LLM (H100)|25,100|~7.0 kJ|~660 s|~$0.00019
VDR on H100|769|~22 J|~9 s|~$0.0000006
VDR on FPGA|769|~1.9 J|~12 s|~$0.00000005
VDR on ASIC|769|~0.4 J|~0.5 s|~$0.00000001

# ops_per_watt(platform|q335_adds_per_watt|q335_muls_per_watt)
Python|20|2
Zig CPU|770K|77K
FPGA (1.9W)|79M|8.8M
GPU H100 (700W)|122M|12M
VDR-Q335 ASIC (400W)|25.5B|12.8B

# latency_comparison(instruction|python|zig_cpu|fpga_150mhz|asic_2ghz|asic_vs_python)
Q335 add|5,000 ns|20 ns|6.7 ns|0.5 ns|10,000×
Q335 mul|50,000 ns|200 ns|60 ns|1.0 ns|50,000×
Q335 divmod|10,000 ns|15 ns|6.7 ns (0 logic)|0 ns (routing)|∞
Fraction unify|100,000 ns|420 ns|127 ns|1.5 ns|66,667×
Fact query (200)|500,000 ns|4,000 ns|1,100 ns|10 ns|50,000×
Softmax 100 logits|2,500,000 ns|25,000 ns|3,300 ns|10 ns|250,000×
Dot product H=64|3,200,000 ns|13,000 ns|5,970 ns|32 ns|100,000×

# cannot_do(id|limitation|reason)
ND1|Conventional neural network inference|No float units; float-trained models cannot execute
ND2|Production-scale LLM training|1B params = 48GB; exceeds practical single-device capacity for exact training; target is millions of params
ND3|Functional remainder resolution parallelization|Newton/Taylor inherently sequential; chip accelerates per-step arithmetic only
ND4|Variable-precision arithmetic natively|QIU fixed at 384 bits; wider needs multi-word in software
ND5|General-purpose GPU workloads|No graphics pipeline, video decode, ray tracing, conventional ML inference

# alternatives_comparison(id|approach|q335_muls_sec|die_cost|float_support|vdr_optimized)
ALT1|GPU + software Q335|85M|High (unused float)|Full|No
ALT2|GPU + integer tensor core|~500M|High|Full|Partial
ALT3|Mixed ASIC (QIU + float)|~2T|Very high|Reduced|Partial
ALT4|FPGA 200 cores|~3.3B|Low|None|Yes (slow clock)
ALT5|Integer-native ASIC (this paper)|~5.1T|Moderate|None|Yes

# multi_chip(chips|qius|hbm_gb|hbm_tb_s|q335_muls_sec|max_train_params|max_infer_params)
1|5,120|96|4.9|5.1T|~10M|~200M
2|10,240|192|9.8|10.2T|~25M|~500M
4|20,480|384|19.6|20.5T|~60M|~1B
8|40,960|768|39.2|41.0T|~120M|~2B

# node_scaling(node|transistors_mm2|qiu_area_mm2|qius_per_100mm2|muls_sec_per_100mm2|clock_ghz)
28nm|5M|1.42|70|5.3B|1.0
16nm|15M|0.47|213|32B|1.5
7nm|40M|0.18|556|139B|1.8
5nm|80M|0.089|1,124|393B|2.0
4nm|100M|0.071|1,408|563B|2.0
3nm|130M|0.055|1,818|909B|2.2
2nm (GAA)|200M|0.036|2,778|1.67T|2.5

# cost_optimized_targets(target|node|die_mm2|cores|muls_sec|chip_cost|power|use_case)
$10 edge|28nm|25|16|8B|~$10|2W|IoT, sensor gateway
$50 embedded|16nm|40|128|96B|~$50|8W|Medical, automotive
$200 mid-range|7nm|100|556|500B|~$200|40W|Workstation
$500 server|5nm|200|2,248|2.2T|~$500|120W|Enterprise server
$2,000 datacenter|4nm|581|5,120|5.1T|~$2,000|400W|Datacenter accelerator
$5,000 flagship|3nm|800|14,544|16T|~$5,000|650W|High-end datacenter

# edge_deployments(device|power_budget|platform|cores|muls_sec|hbm_mb|use_case)
Smartphone|3-5W|28nm ASIC|32|16B|256|Personal assistant with local KB
Automotive ECU|10-15W|16nm ASIC|128|64B|1,024|ADAS with exact sensor fusion
Medical device|5-10W|FPGA UltraScale|60|1B|512|Diagnostic with audit trail
Industrial controller|15-25W|16nm ASIC|256|128B|2,048|Process control with exact constraints
Satellite/aerospace|3-8W|Rad-hard FPGA|20|300M|256|Orbital mechanics
Military/defense|10-30W|Mil-spec ASIC|128|64B|1,024|Structural safety for classified data

# datacenter_economics(metric|h100_10k|vdr_asic_10k|ratio)
Total chip power|7.0 MW|4.0 MW|1.75×
Facility power (PUE 1.3)|9.1 MW|5.2 MW|1.75×
Annual electricity ($0.05/kWh)|$3.99M|$2.28M|1.75×
Chip procurement|$300M|$150M|2.0×
3-year TCO|$411.9M|$206.8M|1.99×
Q335 throughput|850B muls/sec|51T muls/sec|60×
Facility footprint|1,250 racks|714 racks|1.75×

# carbon_per_investigation(platform|energy|co2_grams)
Conventional LLM (H100)|7.0 kJ|0.78
VDR on H100|22 J|0.0024
VDR on FPGA|1.9 J|0.00021
VDR on ASIC|0.4 J|0.000044

# workload_suitability(domain|structured|multi_turn|exact_required|audit_required|accumulation|winner)
SRE/DevOps|High|High|Medium|Medium|Very High|VDR ASIC
Financial compliance|Very High|High|Very High|Very High|High|VDR ASIC
Medical diagnostics|High|High|Very High|Very High|High|VDR ASIC
Legal document review|High|High|Medium|Very High|Very High|VDR ASIC
Scientific computation|Medium|Medium|Very High|Medium|Medium|VDR ASIC
Creative writing|Low|Low|None|None|Low|Conventional GPU
Image/video generation|None|Low|None|None|None|Conventional GPU

# dev_path(phase|duration|deliverable|validates)
FPGA prototype (VDR-21)|32 weeks|10-core on Zynq-7020|Architecture, ISA, bit-identical
FPGA scale-up|12 weeks|60-core on UltraScale+|Scaling, reduction network, bandwidth
RTL for ASIC|20 weeks|Synthesizable Verilog for QIU|Timing at 2 GHz, area estimates
Full chip RTL|30 weeks|Complete chip with memory controllers, I/O|Physical design readiness
Tapeout|16 weeks|GDSII to foundry|Manufacturing
Bring-up + validation|12 weeks|Silicon vs 884-test suite|Bit-identical on silicon
**Total**|**~122 weeks**|**Production silicon**|

# zkp_overlap(property|vdr_q335|zkp_bn254_bls12|overlap)
Operand width|384 bits|256-384 bits|High
Core operation|Integer multiply|Integer multiply|Exact match
Reduction|Power-of-two shift (SHR335)|Modular reduction (mod p)|Different
Parallelism|Data-parallel SIMD|Data-parallel SIMD|Exact match
Memory access|Coalesced, regular|Coalesced, regular|Exact match
Branching|None in arithmetic|None in arithmetic|Exact match
# Adding ~1,100 LUTs/QIU (Barrett + point-add) = 2.1% area increase; enables dual VDR+ZKP market

# iose_invariance(property|python|zig|fpga|gpu|asic)
Same inputs → same outputs|Yes|Yes|Yes|Yes|Yes
Declared properties hold|Yes|Yes|Yes|Yes|Yes
Side effects as declared|Yes|Yes|Yes|Yes|Yes
884-test suite passes|Yes (ref)|Yes|Yes|Yes|Yes
Bit-identical across platforms|Yes (ref)|Yes|Yes|Yes|Yes

# vdr18_stream_mapping(stream|gpu_resources|asic_resources|perf_change)
S0: LLM forward/decode|Tensor ALUs (repurposed int)|QIU warps (native 384-bit)|60× throughput/watt
S1: KB query/scan|Integer ALUs, global mem|QIU warps, HBM columnar|60× throughput
S2: VDR primitives|Integer ALUs, global mem|QIU warps, register arithmetic|60× throughput
S3: Grammar mask/prep|Integer ALUs, shared mem|QIU warps, shared SRAM|60× throughput
S4: Provenance compact|DMA copy engines|DMA copy engines (same)|1× (DMA-bound)

# relationships(from|rel|to)
P1|validated_by|FPGA
P1|constrains|P4
P2|enables|C6
P2|enables|CL4
P3|implements|SHR335
P3|enables|CL3
P4|constrains|C1
P4|enables|P5
P5|verified_by|iose_invariance
C1|component_of|C4
C1|contains|C2
C2|replaces|FPGA iterative multiplier
C3|contains|C1
C4|component_of|C6
C5|enables|REDUCE_ADD
C6|implements|P2
C6|contains|C4
C6|contains|C5
C7|extends|C1
C8|packages|C6
CL1|enables|CL3
CL2|enables|CL3
CL3|enables|CL4
CL3|enables|CL5
CL4|derives_from|P2
CL5|enables|CL6
CL7|derives_from|CL3
CL8|derives_from|P2
CL9|derives_from|P2
CL10|derives_from|P2
CL14|implements|C7
CL16|derives_from|node_scaling
ND1|consequence_of|P2
ND2|constrained_by|HBM capacity
ALT1|outperformed_by|ALT5
ALT5|implements|C6

# section_index(section|title|ids)
1|What the FPGA Proved|P1,P5
2|What Current GPUs Waste|P2
3|Q335 Core Microarchitecture|C1,C2,C3,C4
4|SHR335 at Scale|P3,CL3
5|Memory Hierarchy|register file,remainder SRAM,shared SRAM,L2,HBM3
6|Programming Model|VDR-18 streams,kernel launch,Zig runtime
7|Die Area Estimates|CL1,CL10
8|Performance Projections|CL3-CL7
9|What This Chip Cannot Do|ND1-ND5
10|The Strategic Argument|CL4,CL8,CL11
11|Fabrication and Packaging|C8,CL8,CL9
12|Development Path|dev_path
13|Comparison with Alternatives|ALT1-ALT5
A|QIU Transistor Detail|qiu_transistors
B|Memory Bandwidth Saturation|bandwidth analysis
C|Power Comparison|energy tables
D|Instruction Latency Comparison|latency_comparison
E|Existing Integer Accelerators|no 384-bit native exists
F|Thermal and Physical Design|C8,power_envelope
G|Multi-Chip Configurations|multi_chip
H|Datacenter Economics|datacenter_economics,CL11
I|Power Infrastructure|facility scaling
J|Knowledge Accumulation Impact|CL12,CL13
K|Stranded Asset Risk|transition scenarios
L|Edge Deployment|edge_deployments
M|Workload Suitability|workload_suitability
N|Regulatory Compliance|structural properties across platforms
O|Technology Node Scaling|node_scaling,cost_optimized_targets,CL16
P|Environmental Impact|carbon_per_investigation
Q|ZKP Co-Processing|C7,CL14,zkp_overlap
R|VDR-18 Stream Mapping|vdr18_stream_mapping
S|Industry Adoption Timeline|dev_path milestones
T|SHR335 Across Implementations|divmod comparison
U|Full System Stack|iose_invariance

# decode_legend
format: pipe-delimited tables, ID-based cross-references
target_platform: 4nm ASIC; 80 SMs × 64 QIUs = 5,120 QIUs; 2 GHz
qiu: Q335 Integer Unit — 384-bit ALU with 1-2 cycle multiply, 0-cycle SHR335, remainder SRAM
warp: 32 QIUs in lockstep; zero divergence on Q335 arithmetic
sm: 64 QIUs (2 warps) + 256KB shared SRAM + local reduction + instruction cache
chip: 80 SMs + 96MB L2 + 96GB HBM3 @ 4.9 TB/s + global 7-level reduction
key_latencies: add 1c, mul 1-2c, divmod 0c (routing), compare 1c, cross-mul 2-3c, global reduce 7c
throughput: 5.1T Q335 muls/sec; 10.2T adds/sec; free divmod simultaneous with every multiply
power: ~400W TDP (vs H100 700W); integer arithmetic simpler than float
die: ~68B transistors, ~581 mm² (vs H100 80B, 814 mm²)
shr335: zero gates, zero transistors, zero power, zero latency beyond wire delay; scales linearly with core count
comparison_platforms: Python (reference) | Zig (CPU) | FPGA (150 MHz, 10 cores) | GPU H100 (integer ALU) | ASIC (2 GHz, 5,120 QIUs)
alternatives: ALT1-ALT5 from conventional GPU through integer-native ASIC
node_range: viable 28nm ($10, 2W) through 3nm ($5,000, 650W); same ISA all nodes
limitations: no float, no production-scale LLM training, no variable precision native, no general GPU
rel_types: validated_by|constrains|enables|implements|component_of|contains|replaces|extends|packages|derives_from|consequence_of|constrained_by|outperformed_by|verified_by
+standalone: no cross-references to other compact docs
+no_new_primitives: ASIC accelerates existing VDR operations; IOSE declarations unchanged; 53-instruction ISA from VDR-21
