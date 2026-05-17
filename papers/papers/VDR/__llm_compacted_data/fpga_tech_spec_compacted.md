# VDR FPGA ACCELERATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → core_design → isa → microprograms → system_arch → register_map → relationships → sections

# principles(id|principle|rationale)
P1|Host control plane, FPGA data plane|Zig runtime on ARM handles orchestration, KB tree mgmt, sessions, grammar, LLM passes; FPGA handles parallel numeric/matching ops
P2|Bit-identical results|Every accelerated operation produces results identical to software path; IOSE declarations, builtin contracts, VDR-14 spec unchanged
P3|Q335 divmod is free in hardware|SHR335 is fixed wiring extracting bits [767:335] as quotient and [334:0] as remainder; zero additional logic
P4|Two communication paths|AXI GP0 (32-bit) for register-mapped small queries; AXI HP0 (64-bit DMA) for bulk transfers
P5|Shared die architecture|Zynq-7020 has ARM Cortex-A9 (PS) and FPGA fabric (PL) on same die sharing DDR3; minimal transfer latency

# claims(id|claim|type|depends_on)
CL1|10 VDR-Q335 cores fit on Zynq-7020 at 54.2% LUT, 73.4% FF utilization|observation|
CL2|384-bit addition: 1 cycle; multiplication: 9 cycles; cross-multiply unification: 19 cycles|observation|
CL3|Fast-path single Prolog query on 200 facts: ~200ns at 150 MHz|derivation|CL2
CL4|Dot product for H=64 attention: ~896 cycles = 5.97μs per element|derivation|CL2
CL5|Softmax surrogate on 100 logits across 10 cores: ~500 cycles = 3.3μs|derivation|CL2
CL6|Q335 SGD parameter update: ~15 cycles per element (dominated by 9-cycle WMUL)|derivation|CL2
CL7|45.8% LUT headroom remains for timing closure, debug, future additions|derivation|CL1
CL8|FF utilization is limiting factor at 73.4%|observation|CL1

# concepts(id|name|definition|category)
C1|VDR-Q335 core|Custom processor with 384-bit registers, pipelined ALU, remainder BRAM, instruction BRAM, batch interface; 10 instantiated on Zynq-7020|hardware
C2|384-bit working width|Covers Q335 numerators (~340 bits) with 44-bit margin for intermediate overflow during multiply-accumulate|design
C3|Carry-select adder|384 bits divided into 6×64-bit blocks; each computes sum for carry-in 0 and 1 simultaneously; mux selects as carry propagates; 1 cycle|alu
C4|Iterative multiplier|384×384→768-bit via 3×3=9 partial products of 128×128; each uses 5 DSP48E1 slices time-multiplexed; 9 cycles|alu
C5|Remainder BRAM|2KB per core; 16 nodes × 128 bytes (V:384b, D:384b, R_idx:16b, depth:8b, flags:8b); free-list via 4-bit pointer|storage
C6|Batch dispatcher|FSM partitioning work across cores, managing DMA, collecting results; 11 states; loads operation-specific microprograms|control
C7|Reduction network|Binary tree of 384-bit adders; 5 levels reduce 10 core outputs to one sum; 5 cycles; for softmax denominator, norms|hardware
C8|Fast-path query|Single Prolog query via register writes without DMA; ~10 + (fact_count/10) cycles latency|interface
C9|Shared BRAM|3×18Kb tiles; read-only during operation; holds Q335 constants (22×48B), predicate lookup (256 entries), grammar enums, config|storage
C10|SHR335 instruction|Fixed wiring: bits [767:335]→Vd (quotient), bits [334:0]→Rd (remainder); Q335 divmod in 1 cycle, no mux logic|instruction
C11|Cross-multiply unit|VDR fraction unification: A.V×B.D and B.V×A.D via two WMUL invocations; 19 cycles; sets EQ if products equal|alu
C12|Four-stage pipeline|Fetch→Decode→Execute→Writeback; in-order, no hazard detection; software schedules around latencies; 150 MIPS per core|pipeline

# register_file(id|name|count|width|purpose)
RF1|V registers|8 (V0-V7)|384 bits|VDR values, Q335 numerators, intermediates, accumulators
RF2|R registers|8 (R0-R7)|384 bits|Remainders, comparison operands, temporaries
RF3|Index registers|4 (I0-I3)|32 bits|KB IDs, fact indices, batch positions, loop counters
RF4|Batch control|4 regs (BF, BC, BD, BI)|16+32+8+32 bits|Batch format/predicate, count, depth, index
RF5|Flags|6 bits|1 bit each|EQ, LT, GT, OV, DONE, CLOSED
RF6|Memory address|MA|32 bits|BRAM addressing
# Total per core: 6,264 bits = 783 bytes; implemented in distributed RAM (LUTs)

# alu_components(id|component|latency_cycles|luts|ffs|dsp48|description)
ALU1|384-bit adder/subtractor|1|400|50|0|Carry-select, 6×64-bit blocks
ALU2|128-bit iterative multiplier|9|200|600|5|3×3=9 partial products; DSP48E1 cascade time-multiplexed
ALU3|384-bit barrel shifter|1|350|0|0|9 stages of 2:1 mux (1,2,4,...,256); SHR335 is fixed wiring
ALU4|384-bit comparator|1|100|10|0|Cascaded 64-bit with early termination
ALU5|Cross-multiply control|19|80|40|0|Two WMUL invocations + 768-bit compare

# core_resources(component|luts|ffs|bram_18k|dsp48)
Register file|400|6,264|0|0
Adder/subtractor|400|50|0|0
Iterative multiplier|200|600|5|0
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
**Available (Zynq-7020)**|53,200|106,400|140|220
**Utilization**|54.2%|73.4%|25.0%|22.7%

# memory_map(region|address_range|size|contents)
MM1|0x0000_0000-0x00FF_FFFF|16 MB|Zig kernel + stack + heap
MM2|0x0100_0000-0x08FF_FFFF|128 MB|KB fact store, partitioned
MM3|0x0900_0000-0x10FF_FFFF|128 MB|Model parameters, Q335 format
MM4|0x1100_0000-0x18FF_FFFF|128 MB|Gradient storage
MM5|0x1900_0000-0x1CFF_FFFF|64 MB|Attention matrices + working buffers
MM6|0x1D00_0000-0x1FFF_FFFF|48 MB|DMA transfer buffers, double-buffered
MM7|0x4000_0000-0x4000_00FF|256 B|Control and status registers (64 regs)
MM8|0x4000_0100-0x4000_01FF|256 B|Fast-path query registers (64 regs)

# shared_bram_layout(offset|size|contents)
0x0000|1,056 B|Q335 constant table: 22 constants × 48 bytes
0x0420|512 B|Predicate ID lookup: 256 entries × 2 bytes
0x0620|2,048 B|Grammar enum tables: 128 enums × 16 entries × 1 byte
0x0E20|512 B|Config: budget thresholds, confidence defaults, operational params
0x1020|1,016 B|Reserved

# instruction_set(opcode|mnemonic|format|cycles|description)
0x00|HALT|—|1|Stop core, set DONE
0x01|NOP|—|1|No operation
0x02|JMP|J|1|Unconditional jump
0x03|JEQ|J|1|Jump if EQ
0x04|JLT|J|1|Jump if LT
0x05|JGT|J|1|Jump if GT
0x06|JOV|J|1|Jump if OV
0x07|JCLOSED|J|1|Jump if CLOSED (R=0)
0x08|JDONE|J|1|Jump if batch DONE
0x09|JNE|J|1|Jump if not EQ
0x0A|WADD|R|1|Vd = Vs1 + Vs2 (384-bit); sets OV
0x0B|WSUB|R|1|Vd = Vs1 - Vs2; sets OV, EQ, LT, GT
0x0C|WMUL|R|9|[Vd,Rd] = Vs1 × Vs2 (384×384→768); pipeline stalls
0x0D|WCMP|R|1|Compare Vs1 vs Vs2; sets EQ, LT, GT
0x0E|WABS|R|1|Vd = |Vs1|
0x0F|WNEG|R|1|Vd = -Vs1 (two's complement)
0x10|AND|R|1|Vd = Vs1 & Vs2
0x11|OR|R|1|Vd = Vs1 | Vs2
0x12|XOR|R|1|Vd = Vs1 ^ Vs2
0x13|NOT|R|1|Vd = ~Vs1
0x14|SHR|I|1|Vd = Vs1 >> imm (barrel, 0-383)
0x15|SHL|I|1|Vd = Vs1 << imm
0x16|SHR335|R|1|Vd = [Vs1:Rs1][767:335], Rd = [334:0]; Q335 divmod, fixed wiring
0x17|SHRN|I|1|General divmod by 2^N
0x18|NEST|R|2|Allocate remainder child node; depth++
0x19|UNNEST|R|2|Deallocate node; depth--
0x1A|RDEPTH|R|1|Id = current remainder depth
0x1B|RLOAD|R|2|Load node: Vd = node.V, Rd = node.R_idx
0x1C|RSTORE|R|2|Store to node: node.V = Vs1, node.R_idx = Rs1
0x1D|PROJECT|R|var|Scalar projection Π: walk R tree recursively; cycles = 3 × depth
0x1E|NORMALIZE|R|var|Normalize VDR triple; sign, GCD, closed check; sets CLOSED
0x1F|CROSS_MUL|R|19|Two WMUL + 768-bit compare; VDR fraction unification
0x20|UATOM|R|1|Atom unification via interned integer ID comparison
0x21|LDV|I|2|Load 384-bit value from BRAM
0x22|LDR|I|2|Load 384-bit remainder from BRAM
0x23|STV|I|2|Store 384-bit value to BRAM
0x24|STR|I|2|Store 384-bit remainder
0x25|LDVR|I|2|Load V and R together
0x26|STVR|I|2|Store V and R together
0x27|LDI|I|1|Load immediate to index register
0x28|SETMA|I|1|Set memory address from index + offset
0x29|BLOAD|B|3|Read 7-byte batch header from BRAM
0x2A|BNEXT|B|1|Increment batch index; set DONE if complete
0x2B|BADDR|R|1|Compute address of current batch element
0x2C|BMATCH|R|1|Predicate match; set EQ
0x2D|LDSHARED|I|2|Read from shared BRAM
0x2E|TSEND|R|1|Write to inter-core transfer register
0x2F|TRECV|R|1|Read from inter-core transfer register
0x30|TWAIT|—|var|Stall until transfer complete
0x31|TDONE|—|1|Signal transfer complete
0x32|REDUCE_ADD|R|5|Send to reduction network; receive global sum
0x33|MOVI|I|1|Move immediate to Vd[17:0]
0x34|MOVHI|I|1|Move immediate to Vd[35:18]
# Total: 53 instructions, 10 categories

# microprograms(id|program|purpose|est_instructions|cycles_per_item|notes)
MP1|prog_fact_match|Scan facts by predicate ID, collect match indices|~40|8 (no match) / 12 (match)|Parallel across cores by fact partition
MP2|prog_q335_add|Batch Q335 add/SGD update: a[i] - lr×grad[i]|~20|~15|Dominated by 9-cycle WMUL
MP3|prog_q335_mul|Batch Q335 multiply with divmod and nesting|~50|~12+|Includes SHR335 + NEST if remainder nonzero
MP4|prog_dot_product|384-bit dot product for attention QKT row|~35|~14 per dimension|H=64: ~896 cycles = 5.97μs
MP5|prog_constraint_eval|Evaluate Prolog constraint against fact set|~60|Variable|One constraint per core
MP6|prog_softmax_surr|Compute (z-m+c)² per logit, accumulate; uses REDUCE_ADD|~30 per phase|~500 total for 100 logits / 10 cores|3.3μs at 150 MHz

# dispatcher_states(id|state|transition|description)
DS1|S_IDLE|→ S_CALC on go|Waiting for host trigger
DS2|S_CALC|→ S_LOAD_PROG|Compute work partition across cores
DS3|S_LOAD_PROG|→ S_LOAD_DATA|DMA program to core instruction BRAMs
DS4|S_LOAD_DATA|→ S_LOAD_WAIT|DMA data to core BRAMs/registers
DS5|S_LOAD_WAIT|→ S_START|Wait for DMA complete
DS6|S_START|→ S_WAIT|Assert start to all active cores
DS7|S_WAIT|→ S_STORE|Poll core done bits
DS8|S_STORE|→ S_STORE_WAIT|DMA results from cores to DDR3
DS9|S_STORE_WAIT|→ S_NEXT|Wait for DMA complete
DS10|S_NEXT|→ S_CALC or S_DONE|More chunks → loop; else done
DS11|S_DONE|→ S_IDLE|Set done flag

# control_registers(offset|name|width|access|description)
0x00|CONTROL|32|W|[0] go, [1] abort, [4:2] op type (0-5), auto-clears go
0x04|STATUS|32|R|[0] busy, [1] done, [2] error, [3] dma_active, [13:4] core_done (10 bits)
0x08|SRC_ADDR|32|RW|DDR3 source address
0x0C|SRC_COUNT|32|RW|Input work item count
0x10|SRC_STRIDE|32|RW|Bytes per input item (48 single Q335, 96 pair)
0x14|DST_ADDR|32|RW|DDR3 destination address
0x18|DST_STRIDE|32|RW|Bytes per output item
0x1C-0x28|PARAM_0-3|32|RW|Operation-specific parameters
0x2C|PROG_SEL|32|RW|Program index (0-5); 0xFF = custom
0x30|PROG_ADDR|32|RW|DDR3 address of custom program
0x34|SHARED_SRC|32|RW|DDR3 source for shared BRAM load
0x38|SHARED_SIZE|32|RW|Bytes to load
0x3C|SHARED_GO|32|W|Trigger shared BRAM load
0x40|CYCLE_COUNT|32|R|Clock cycles for last operation
0x44|MATCH_COUNT|32|R|Matches found or items processed
0x48|ERROR_CODE|32|R|[7:0] type, [15:8] core, [31:16] PC
0x4C|CORE_COUNT|32|R|Hardwired 10
0x50|VERSION|32|R|Major.minor.patch (8.8.16)
0x54-0x7C|RESULT_LO-9|32|R|384-bit scalar result (12 × 32-bit regs)

# fast_path_registers(offset|name|width|access|description)
0x100|FP_PREDICATE|32|RW|Predicate ID (16-bit)
0x104|FP_ARG0_LO|32|RW|First argument low 32 bits
0x108|FP_ARG0_HI|32|RW|First argument bits [63:32]
0x10C|FP_ARG_COUNT|32|RW|Arguments to match (0 = predicate only)
0x110|FP_GO|32|W|Trigger fast-path query
0x114|FP_STATUS|32|R|[0] busy, [1] done, [15:2] match count
0x118-0x124|FP_MATCH_0-3|32|R|Indices of first 4 matching facts

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

# instruction_format(type|fields|description)
R|[31:26] opcode, [25:22] Vd/Rd, [21:18] Vs1/Rs1, [17:14] Vs2/Rs2, [13:0] reserved/subfunc|Register-register
I|[31:26] opcode, [25:22] Vd/Rd, [21:18] Vs1/Rs1, [17:0] immediate (18-bit)|Register-immediate
J|[31:26] opcode, [25:0] target address (26-bit word-addressed)|Jump
B|[31:26] opcode, [25:22] register, [21:0] batch parameters|Batch

# remainder_node_structure(field|size|description)
V|384 bits (48 bytes)|Value component
D|384 bits (48 bytes)|Denominator (typically 2^335)
R_idx|16 bits (2 bytes)|Child node index; 0xFFFF = no child = closed
depth|8 bits (1 byte)|Current depth
flags|8 bits (1 byte)|closed, active, functional marker
pad|28 bytes|Alignment to 128-byte boundary
# 16 nodes per core; max depth 16; free-list via 4-bit pointer

# relationships(from|rel|to)
P1|defines|HR1
P1|defines|HR2
P1|defines|HR3
P1|defines|HR4
P1|defines|HR5
P1|defines|HR6
P1|defines|HR7
P1|defines|HR8
P1|defines|HR9
P1|defines|FP1
P1|defines|FP2
P1|defines|FP3
P1|defines|FP4
P1|defines|FP5
P1|defines|FP6
P1|defines|FP7
P2|constrains|C1
P3|implements|C10
P4|implements|C8
P4|enables|C6
P5|enables|P4
C1|contains|RF1
C1|contains|RF2
C1|contains|RF3
C1|contains|RF4
C1|contains|RF5
C1|contains|RF6
C1|contains|ALU1
C1|contains|ALU2
C1|contains|ALU3
C1|contains|ALU4
C1|contains|ALU5
C1|contains|C5
C1|contains|C12
C2|constrains|RF1
C2|constrains|RF2
C3|implements|ALU1
C4|implements|ALU2
C6|manages|C1
C6|uses|DS1
C7|enables|MP6
C8|enables|CL3
C9|provides|MP1
C9|provides|MP5
C10|implements|P3
C10|enables|MP2
C10|enables|MP3
C11|implements|FP7
C12|contains|C1
MP1|implements|FP1
MP2|implements|FP2
MP3|implements|FP2
MP4|implements|FP3
MP5|implements|FP4
MP6|implements|FP6

# section_index(section|title|ids)
1|System Architecture|P1,P4,P5
1.1|Host-FPGA Division|HR1-HR9,FP1-FP7
1.2|Communication|P4,C8
1.3|Memory Map|MM1-MM8
2|VDR-Q335 Core Design|C1,C2
2.1|Working Width|C2
2.2|Register File|RF1-RF6
2.3|ALU|ALU1-ALU5,C3,C4,C10,C11
2.4|Remainder BRAM|C5
2.5|Instruction BRAM|
2.6|Pipeline|C12
2.7|Resource Summary|CL1
3|System-Level Architecture|
3.1|Core Count|CL1,CL7,CL8
3.2|Batch Dispatcher|C6,DS1-DS11
3.3|Shared BRAM|C9
3.4|Reduction Network|C7
4|Register Map|
4.1|Control Registers|
4.2|Fast-Path Registers|C8,CL3
5|Instruction Set Architecture|C10,C11,CL2
6|Microprogram Specifications|MP1-MP6,CL4,CL5,CL6

# decode_legend
format: pipe-delimited tables, ID-based cross-references
platform: Xilinx Zynq-7020 SoC (Zybo Z7-20); ARM Cortex-A9 (PS) + FPGA fabric (PL); 512MB shared DDR3
clock: 150 MHz target
working_width: 384 bits (Q335 numerator ~340b + 44b overflow margin)
core_count: 10 VDR-Q335 cores
instruction_width: 32 bits fixed; 4 formats: R (reg-reg), I (reg-imm), J (jump), B (batch)
instruction_count: 53 instructions, 10 categories
pipeline: 4-stage in-order (fetch/decode/execute/writeback); no hazard detection
mul_latency: 9 cycles (iterative 128-bit, 3×3 tiling with DSP48E1)
cross_mul_latency: 19 cycles (2×WMUL + compare)
divmod_q335: 1 cycle (SHR335 fixed wiring)
remainder_depth: max 16 nodes per core in 2KB BRAM
microprogram_count: 6 (fact_match, q335_add, q335_mul, dot_product, constraint_eval, softmax_surr)
dispatcher_states: 11 (IDLE→CALC→LOAD_PROG→LOAD_DATA→LOAD_WAIT→START→WAIT→STORE→STORE_WAIT→NEXT→DONE)
axi_interfaces: GP0 (32-bit register), HP0 (64-bit DMA)
rel_types: defines|constrains|implements|enables|contains|manages|uses|provides
+standalone: no cross-references to other compact docs
+no_new_primitives: FPGA accelerates existing VDR operations; no new builtins, IOSE declarations, or contracts introduced
