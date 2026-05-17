# VDR-21 FPGA 10-CORE Q335 PROCESSOR — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → core_design → isa → microprograms → system → scaling → dev_phases → relationships → sections

# principles(id|principle|rationale)
P1|Q335 divmod is free in hardware|Denominator 2^335 is fixed power of two; division is bit extraction — bits above 335 are quotient, bits below are remainder; fixed wiring, zero logic cells, zero power
P2|Host control plane, FPGA data plane|ARM runs Zig runtime (orchestration, KB tree, sessions, grammar, LLM passes); FPGA runs parallel numeric ops (fact matching, batch arithmetic, attention, constraints, softmax)
P3|Bit-identical results required|Every FPGA operation must match software path exactly; verified against 884-test suite across 37 domains with zero errors; integer arithmetic is deterministic — no rounding modes, no platform dependence
P4|Same core scales linearly|Same core, dispatcher, ISA, microprograms on any device; more cores = proportionally more throughput; reduction network grows logarithmically
P5|Shared die minimizes transfer|Zynq-7020 puts ARM + FPGA on same die sharing DDR3; AXI GP0 (32-bit registers) for control, AXI HP0 (64-bit DMA) for bulk

# claims(id|claim|type|depends_on)
CL1|10 cores fit Zynq-7020: 54.2% LUT, 73.4% FF, 25% BRAM, 22.7% DSP48|observation|
CL2|384-bit add: 1 cycle; multiply: 9 cycles; divmod: 1 cycle (free); cross-mul unification: 19 cycles; all at 150 MHz|observation|
CL3|Prolog fact query across 200 facts: ~200ns (1.1μs with AXI overhead)|derivation|CL2
CL4|Attention dot product H=64: ~896 cycles = 5.97μs|derivation|CL2
CL5|Softmax surrogate 100 logits across 10 cores: ~500 cycles = 3.3μs; result sums to exactly one|derivation|CL2
CL6|SGD parameter update: ~15 cycles/element (9-cycle WMUL dominant); 100K params in ~1ms|derivation|CL2
CL7|Active spill rate expected below 1%; Q335 frame provides 290 orders of magnitude headroom over typical training denominators (~2^45)|observation|
CL8|Design resource-estimated but not yet synthesized; utilization and timing are pre-synthesis estimates|observation|CL1
CL9|100M parameter model needs ~4.8 GB; exceeds Zynq-7020 DDR3 (512 MB); limits to thousands-tens of thousands params|observation|
CL10|150 MHz clock is 10-20× slower than GPU (1.5-2.5 GHz); FPGA compensates with architectural advantages not raw speed|observation|
CL11|FPGA targets embedded, edge, dev platforms, power-constrained — not datacenter GPU competition|observation|CL10
CL12|Shadow mode enables real-time FPGA vs software comparison at 2× compute cost|observation|P3

# concepts(id|name|definition|category)
C1|VDR-Q335 core|Custom 384-bit processor: 8 V-regs + 8 R-regs + 4 index regs, pipelined ALU, 2KB remainder BRAM (16 nodes), 4KB instruction BRAM, batch interface; 2,090 LUTs, 7,314 FFs, 3 BRAM, 5 DSP48 per core|hardware
C2|384-bit working width|Q335 numerators ~340 bits + 44-bit overflow margin; divisible into 6×64-bit (adder) and 3×128-bit (multiplier)|design
C3|Carry-select adder|6×64-bit blocks each computing sum for carry-in 0 and 1 simultaneously; mux selects as carry propagates; 1 cycle, ~400 LUTs|alu
C4|Iterative multiplier|384×384→768 via 3×3=9 partial products of 128×128; 5 DSP48E1 slices time-multiplexed; 9 cycles, ~200 LUTs|alu
C5|SHR335|Fixed wiring: bits [767:335]→Vd (quotient), [334:0]→Rd (remainder); zero LUTs, zero switching power; 1 pipeline cycle|instruction
C6|Cross-multiply unit|VDR fraction unification: A.V×B.D and B.V×A.D via two WMUL + 768-bit compare; 19 cycles; exact rational equality|alu
C7|Remainder BRAM|2KB per core; 16 nodes × 128 bytes (V:48B, D:48B, R_idx:2B, depth:1B, flags:1B, pad:28B); free-list via 4-bit pointer|storage
C8|Batch dispatcher|11-state FSM: IDLE→CALC→LOAD_PROG→LOAD_DATA→LOAD_WAIT→START→WAIT→STORE→STORE_WAIT→NEXT→DONE; partitions work, manages DMA, collects results|control
C9|Reduction network|Binary tree of 384-bit adders; 5 levels for 10 cores; 5 cycles; ~1,200 LUTs; for softmax denominator, norms, global dot products|hardware
C10|Fast-path query|Register-mapped single Prolog query without DMA; host writes predicate + args to registers, polls result; ~10+(facts/10) cycles|interface
C11|Shared BRAM|3×18Kb tiles; read-only; 22 Q335 constants (1,056B), predicate lookup (512B), grammar enums (2,048B), config (512B)|storage
C12|Four-stage pipeline|Fetch→Decode→Execute→Writeback; in-order, no hazard detection; software schedules around latencies; 150 MIPS/core|pipeline
C13|Shadow mode|Both software and FPGA paths execute same operation; results compared automatically; 2× cost but real-time verification|verification

# register_file(id|name|count|width_bits|purpose)
RF1|V registers|8|384|VDR values, Q335 numerators, intermediates, accumulators
RF2|R registers|8|384|Remainders, comparison operands, temporaries
RF3|Index registers|4|32|KB IDs, fact indices, batch positions, loop counters
RF4|Batch control (BF,BC,BD,BI)|4|16+32+8+32|Format/predicate, count, depth, index
RF5|Flags (EQ,LT,GT,OV,DONE,CLOSED)|6|1 each|Comparison and status results
RF6|Memory address (MA)|1|32|BRAM addressing
# Total per core: 6,264 bits = 783 bytes in distributed RAM

# core_resources(component|luts|ffs|bram_18k|dsp48)
Register file|400|6,264|0|0
Adder/subtractor|400|50|0|0
Iterative multiplier|200|600|0|5
Barrel shifter|350|0|0|0
Comparator|100|10|0|0
Cross-multiply control|80|40|0|0
Remainder BRAM|30|10|1|0
Instruction BRAM|30|10|2|0
Pipeline control|200|150|0|0
Unification micro-sequencer|200|100|0|0
Batch interface|100|80|0|0
**Core total**|2,090|7,314|3|5

# system_resources(component|luts|ffs|bram|dsp48)
10 × VDR core|20,900|73,140|30|50
Batch dispatcher|2,500|1,800|0|0
AXI register bank|600|500|0|0
AXI DMA engine|2,000|1,200|0|0
Shared BRAM controller|150|80|3|0
Interconnect + infrastructure|1,500|800|2|0
Reduction network|1,200|600|0|0
**System total**|28,850|78,120|35|50
**Zynq-7020 available**|53,200|106,400|140|220
**Utilization**|54.2%|73.4%|25.0%|22.7%

# memory_map(id|address_range|size|contents)
MM1|0x0000_0000–0x00FF_FFFF|16 MB|Zig kernel + stack + heap
MM2|0x0100_0000–0x08FF_FFFF|128 MB|KB fact store, partitioned for parallel access
MM3|0x0900_0000–0x10FF_FFFF|128 MB|Model parameters, Q335 format
MM4|0x1100_0000–0x18FF_FFFF|128 MB|Gradient storage
MM5|0x1900_0000–0x1CFF_FFFF|64 MB|Attention matrices + working buffers
MM6|0x1D00_0000–0x1FFF_FFFF|48 MB|DMA transfer buffers, double-buffered
MM7|0x4000_0000–0x4000_00FF|256 B|Control + status registers
MM8|0x4000_0100–0x4000_01FF|256 B|Fast-path query registers

# instruction_set(opcode|mnemonic|format|cycles|description)
0x00|HALT|—|1|Stop core, set DONE
0x01|NOP|—|1|No operation
0x02-0x09|JMP,JEQ,JLT,JGT,JOV,JCLOSED,JDONE,JNE|J|1|Conditional/unconditional jumps
0x0A|WADD|R|1|Vd = Vs1 + Vs2 (384-bit); sets OV
0x0B|WSUB|R|1|Vd = Vs1 − Vs2; sets OV,EQ,LT,GT
0x0C|WMUL|R|9|[Vd,Rd] = Vs1 × Vs2 (384→768); stalls pipeline
0x0D|WCMP|R|1|Compare; sets EQ,LT,GT
0x0E|WABS|R|1|Absolute value
0x0F|WNEG|R|1|Two's complement negate
0x10-0x13|AND,OR,XOR,NOT|R|1|Bitwise 384-bit
0x14-0x15|SHR,SHL|I|1|Barrel shift 0-383 positions
0x16|SHR335|R|1|Q335 divmod: [767:335]→Vd, [334:0]→Rd; fixed wiring, zero logic
0x17|SHRN|I|1|General divmod by 2^N
0x18-0x19|NEST,UNNEST|R|2|Allocate/deallocate remainder node; depth++/--
0x1A|RDEPTH|R|1|Read remainder depth
0x1B-0x1C|RLOAD,RSTORE|R|2|Load/store remainder node
0x1D|PROJECT|R|var|Scalar projection Π; 3×depth cycles
0x1E|NORMALIZE|R|var|Normalize VDR triple; sets CLOSED
0x1F|CROSS_MUL|R|19|Two WMUL + 768-bit compare; fraction unification
0x20|UATOM|R|1|Atom unification via interned ID compare
0x21-0x26|LDV,LDR,STV,STR,LDVR,STVR|I|2|Load/store 384-bit values from/to BRAM
0x27|LDI|I|1|Load immediate to index register
0x28|SETMA|I|1|Set memory address
0x29-0x2C|BLOAD,BNEXT,BADDR,BMATCH|B/R|1-3|Batch processing
0x2D|LDSHARED|I|2|Read from shared BRAM
0x2E-0x31|TSEND,TRECV,TWAIT,TDONE|R/—|1-var|Inter-core transfer
0x32|REDUCE_ADD|R|5|Global sum via reduction network
0x33-0x34|MOVI,MOVHI|I|1|Move immediate to Vd[17:0] or [35:18]
# Total: 53 instructions, 10 categories; 32-bit fixed width; 4 formats (R, I, J, B)

# microprograms(id|program|purpose|est_instructions|cycles_per_item|key_metric)
MP1|prog_fact_match|Scan partition for predicate match; return indices|~40|8 (no match) / 12 (match)|200 facts across 10 cores: ~1.1μs
MP2|prog_q335_add|SGD: W ← W − lr×grad; WMUL+SHR335+WSUB per element|~20|~15|100K params: ~1.0ms
MP3|prog_q335_mul|Batch multiply with remainder handling; WMUL+SHR335+NEST|~50|~12+|+6 cycles per nesting level
MP4|prog_dot_product|QKT row: WMUL+SHR335+WADD per dimension; REDUCE_ADD|~35|~14/dim|H=64: ~896 cycles = 5.97μs
MP5|prog_constraint_eval|Evaluate Prolog constraint via BMATCH+WCMP+CROSS_MUL|~60|variable|15 constraints: 2 passes on 10 cores
MP6|prog_softmax_surr|(z−m+c)² map + REDUCE_ADD + normalize; exact sum-to-one|~30/phase|~500 total for 100 logits|3.3μs across 10 cores

# parallelism_classification(id|category|operations)
PA1|Embarrassingly parallel|Q335 bulk add, constraint checking, softmax map, budget check, reprojection, fact query by partition, bitset ops
PA2|Parallel with reduction|Softmax normalization, matrix-vector multiply, dot product, determinant row ops, list aggregates
PA3|Sequential (limited)|Prolog backtracking, Newton iteration, remainder tree traversal, scope chain resolution

# host_responsibilities(id|responsibility)
HR1|Orchestrated inference loop (assess, formalize, execute, store)
HR2|KB tree management (create, delete, scope, mount, connect)
HR3|Session management (snapshot, clone, kill)
HR4|Grammar parsing and generation
HR5|Command token parsing and dispatch
HR6|LLM forward/backward pass orchestration
HR7|Remainder tree operations beyond depth 4
HR8|Functional remainder resolution (Newton, Taylor, series)
HR9|All control flow decisions

# fpga_responsibilities(id|responsibility)
FP1|Parallel Prolog fact matching across KB partitions
FP2|Q335 batch arithmetic (add, subtract, multiply, divmod)
FP3|Row-parallel attention score computation (QKT)
FP4|Parallel constraint evaluation
FP5|Parallel denominator budget checking
FP6|Softmax surrogate computation (map-reduce)
FP7|VDR fraction cross-multiply comparison for unification

# not_on_fpga(id|operation|reason)
NF1|Deep remainder traversal (>depth 4)|Sequential parent-child dependency; rare; software handles without perf impact
NF2|Functional remainder resolution|Newton/Taylor inherently sequential; FPGA accelerates per-step arithmetic but not iteration control
NF3|KB tree structure management|Irregular pointer-chasing; hash tables, arena allocators better in software
NF4|Grammar matching + scoring|Mixed deterministic-probabilistic; unsuitable for pure HW unless profiling shows bottleneck
NF5|Session snapshot/restore|Bulk memory copies; infrequent; Zig arena allocators efficient
NF6|LLM pass orchestration|Layer sequencing, residual connections, loss computation — control flow on host

# scaling(platform|luts_avail|dsp48_avail|bram_avail|max_cores|limiting_resource)
Zynq-7020|53,200|220|140|10|FF (73.4%)
Zynq-7045|218,600|900|545|60|LUT (71%)
Zynq-7100|444,000|2,020|1,090|120|DSP (30%)
UltraScale+ ZU7EV|504,000|1,728|1,080|130|DSP (38%)
UltraScale+ ZU19EG|1,143,000|1,968|1,968|200+|Balanced

# scaling_perf(platform|cores|fact_query_200|sgd_100k|softmax_100)
Zynq-7020|10|~1.1μs|~1.0ms|~3.3μs
Zynq-7045|60|~0.18μs|~170μs|~0.6μs
Zynq-7100|120|~0.09μs|~83μs|~0.3μs
UltraScale+ ZU19EG|200|~0.05μs|~50μs|~0.17μs

# q335_constants(index|constant|symbol|numerator_bits)
0|Pi|π|337
1|Euler's number|e|337
2|Natural log 2|ln(2)|335
3|Square root 2|√2|336
4|Golden ratio|φ|336
5|Pi squared|π²|339
6|Pi cubed|π³|340
7|Pi to the fourth|π⁴|342
8|e to the pi|eᵖ|340
9|ln²(2)|ln(2)²|334
10|ln⁴(2)|ln(2)⁴|333
11|Natural log 3|ln(3)|336
12|Natural log 5|ln(5)|336
13|Natural log 10|ln(10)|337
14|Square root 3|√3|336
15|Square root 5|√5|337
16|Square root 7|√7|337
17|Zeta(2)|ζ(2)|336
18|Zeta(3)|ζ(3)|336
19|Zeta(5)|ζ(5)|336
20|Li₄(1/2)|Li₄(1/2)|335
21|Catalan's constant|G|335
# All share implicit denominator 2^335; stored as 384-bit numerators in shared BRAM

# dev_phases(id|phase|weeks|contents|deliverable)
DP1|Prolog accelerator|1-8|Core pipeline 384-bit; WADD,WSUB,WCMP,WABS,WNEG,BMATCH; dispatcher FSM; AXI registers; Zig host interface|Fact queries on FPGA matching software exactly
DP2|Q335 arithmetic|9-14|128-bit iterative multiplier (DSP48E1); WMUL,SHR335,SHRN,barrel shifter; NEST,UNNEST,RLOAD,RSTORE,RDEPTH; prog_q335_add,prog_q335_mul|Batch Q335 with remainder, validated vs software
DP3|Attention acceleration|15-20|Reduction network; REDUCE_ADD; prog_dot_product; prog_softmax_surr; attention weights sum-to-exactly-one verified|Exact attention + softmax integrated with host transformer
DP4|Unification engine|21-26|CROSS_MUL,UATOM; unification micro-sequencer; prog_constraint_eval; variable binding in BRAM|Complete Prolog query eval for common term types
DP5|Integration + profiling|27-32|Full Zig runtime integration; DMA double-buffering; end-to-end profiling; VDR-11 Stage 4 lifecycle|Benchmarked system with perf comparison vs software-only

# verification_levels(id|level|method|scope)
VL1|Instruction|Each ISA instruction tested with boundary inputs; bit-by-bit compare vs Python reference|53 instructions × boundary cases
VL2|Microprogram|Each program with representative workloads; FPGA output vs software reference|6 programs × varied KB/param sizes
VL3|System|Full 884-test validation suite; FPGA-accelerated must match software-only|37 domains; zero-error requirement
VL4|Shadow mode|Both paths execute same operation; automatic comparison; selective per operation type|Runtime verification at 2× cost

# relationships(from|rel|to)
P1|implements|C5
P1|enables|CL2
P2|defines|HR1
P2|defines|FP1
P3|constrains|VL1
P3|constrains|VL2
P3|constrains|VL3
P3|enables|C13
P4|enables|scaling
P5|enables|C10
C1|contains|C3
C1|contains|C4
C1|contains|C5
C1|contains|C6
C1|contains|C7
C1|contains|C12
C2|constrains|RF1
C2|constrains|RF2
C3|implements|WADD
C4|implements|WMUL
C5|implements|SHR335
C6|implements|CROSS_MUL
C7|enables|NEST
C8|manages|C1
C8|uses|DMA
C9|implements|REDUCE_ADD
C10|enables|CL3
C11|provides|q335_constants
C12|contains|C1
C13|implements|VL4
MP1|implements|FP1
MP2|implements|FP2
MP3|implements|FP2
MP4|implements|FP3
MP5|implements|FP4
MP6|implements|FP6
DP1|enables|DP2
DP2|enables|DP3
DP2|enables|DP4
DP3|enables|DP5
DP4|enables|DP5
NF1|handled_by|HR7
NF2|handled_by|HR8
NF3|handled_by|HR2
NF6|handled_by|HR6

# section_index(section|title|ids)
1|The System in Brief|P1,P2,C2
2|Why Hardware Acceleration|FP1-FP7,PA1-PA3
3|The Q335 Hardware Opportunity|P1,C3,C4,C5,C6,CL2
4|Core Architecture|C1,C2,C7,C12,RF1-RF6
5|Instruction Set Architecture|53 instructions; C5,C6,REDUCE_ADD
6|System Architecture|CL1,C8,C9,C10,C11,P5,MM1-MM8
7|Register Map|control+fast-path registers
8|Microprograms|MP1-MP6,CL3-CL6
9|Host-FPGA Integration|P2,HR1-HR9,P3,C13
10|What Does Not Belong on FPGA|NF1-NF6
11|Scaling|P4,scaling table
12|Development Path|DP1-DP5
13|Verification Strategy|VL1-VL4,P3
14|Limitations|CL8-CL11
A|Parallelism Classification|PA1-PA3
B|Instruction Encoding|R,I,J,B formats
C|Shared BRAM Contents|C11,q335_constants
D|Performance Projections|CL3-CL6,scaling_perf
E|Remainder Node Layout|C7

# decode_legend
format: pipe-delimited tables, ID-based cross-references
platform: Xilinx Zynq-7020 SoC (XC7Z020); ARM Cortex-A9 (PS) + FPGA (PL); 512MB shared DDR3
clock: 150 MHz target
working_width: 384 bits (Q335 ~340b + 44b margin)
core_count: 10 on Zynq-7020; scales to 200+ on UltraScale+
isa: 53 instructions, 32-bit fixed width, 4 formats (R/I/J/B), 10 categories
pipeline: 4-stage in-order; no hazard detection; 150 MIPS/core single-cycle
key_latencies: add 1c, mul 9c, divmod 1c (free), cross-mul 19c, reduce 5c
microprograms: 6 (fact_match, q335_add, q335_mul, dot_product, constraint_eval, softmax_surr)
dispatcher: 11-state FSM with DMA chunking
axi: GP0 32-bit registers, HP0 64-bit DMA
verification: 884 tests, 37 domains, zero errors, shadow mode
status: pre-synthesis resource estimates; not yet placed/routed
rel_types: implements|enables|constrains|defines|contains|manages|uses|provides|handled_by
+standalone: no cross-references to other compact docs
+no_new_primitives: FPGA accelerates existing VDR operations; IOSE declarations and builtin contracts unchanged
