# CKS-MATH-148 + CKS-MATH-145: LLM-PROLOG ON VFR HARDWARE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Source: CKS-MATH-148 (Inline Intelligence Spec) + CKS-MATH-145 (FPGA Implementation Spec)
# Status: CKS framework invalidated. Math does not compile. All papers in series falsified.
# Read order: status → principles → vfr_types → pipeline → llm_inference → prolog → verification → kb → domain_eating → fpga_arch → modules → isa_opcodes → resource → timing → zig_interface → boot → milestones → relationships → section_index → decode_legend

# status(id|aspect|detail)
S1|Framework status|CKS has been invalidated; math does not compile; all papers in series falsified
S2|Next steps|@CKS-NEXT-1-2026
S3|Registries|CKS-MATH-148 (Inline Intelligence), CKS-MATH-145 (FPGA Implementation)

# principles(id|principle|detail)
P1|LLM is a batch operation|not a service/API; runs inline in frame pipeline on same FPGA cores; produces VFR data that feeds next batch pass
P2|Everything is VFR|every data type is [V:i32, R:i8]; text, terms, facts, rules, weights, activations, pixels, audio — one format, one ISA
P3|LLM produces data not code|generates integer tuples (predicate IDs, action IDs) describing rules; never generates executable instructions; no injection risk
P4|No hallucination by construction|Prolog verification structurally between LLM generation and entity behavior; invalid rules rejected; entity falls back to existing behavior
P5|Intelligence is a pipeline transform|not a separate phase; same as fact generation or behavior scoring; occurs in Pass 4 of 9-pass frame pipeline
P6|KB grows without retraining|new domains added by loading new fact batches; no neural network weight updates; parse→validate→load→query

# vfr_types(id|type|v_meaning|r_meaning|depth|notes)
VT1|Character|Unicode codepoint|script family (0=Latin,1=CJK,2=Hiragana,...up to 127)|1|fixed 5 bytes/char; O(1) indexing; script detection = 1 byte read
VT2|Term|type+value|0|5|depth carries provenance: type, value, source_id, offset, version
VT3|Fact|predicate args|0|6|F=predicate_id; depth carries provenance + confidence (0=speculative,1=inferred,2=stated,3=verified)
VT4|Rule|head+body refs|0|3|head_predicate_id, body_batch_addr, body_count; body is separate batch of predicate refs
VT5|LLM Weight|trained weight|quantization remainder|1|forward pass = MUL, ADD, SHR on integer batches
VT6|Activation|layer output|quantization remainder|1|same ops as weights
VT7|Entity field|field value|field remainder|per entity depth|entity IS set of facts in KB
VT8|Pixel|packed RGB|alpha|1|
VT9|Audio sample|PCM amplitude|channel ID|1|
VT10|Instruction|encoded opcode+ops|(same format as data)|1|
VT11|Session|session_id|session_type (0=game,1=editor,2=network,3=debug)|1|KB view filter
VT12|Batch header|[F:i16, count:u32, depth:u8] = 7 bytes|-|-|precedes every batch

# term_types(id|value|meaning)
TT0|0|container (function, struct, sentence)
TT1|1|delimiter_open
TT2|2|delimiter_close
TT3|3|separator
TT4|4|name (identifier)
TT5|5|kind (category)
TT6|6|type_ref
TT7|7|keyword
TT8|8|operator
TT9|9|number
TT10|10|text_literal
TT11|11|predicate (Prolog)
TT12|12|rule
TT13|13|fact
TT14|14|variable (Prolog unification)
TT15|15|reference
TT16|16|vector2
TT17|17|rectangle
TT18|18|entity
TT19|19|transform

# frame_pipeline(id|pass|operation|data_flow|all_integer)
FP1|Pass 1|Fact generation|entity batch → predicate-keyed fact batches|yes
FP2|Pass 2|State machine evaluation|fact batches + transition batch → state updates|yes
FP3|Pass 3|Prolog rule evaluation|fact batches filtered by rule batch → valid candidates; check LLM triggers (zero path coverage)|yes
FP4a|Pass 4a|LLM inference (triggered entities only, may span frames)|entity context batch → candidate rule batch; matrix multiply-accumulate on weight batches|yes
FP4b|Pass 4b|Prolog verification of LLM output|candidate rules checked against KB; Triveritas L/M/E; Scales materiality gate|yes
FP5|Pass 5|UtilityAI scoring|fact batches + behavior batches + verified rules → winning behaviors|yes
FP6|Pass 6|Logic block execution|winning behaviors → entity field modifications|yes
FP7|Pass 7|Envelopes + traces|time-bounded modifiers + decision recording|yes
FP8|Pass 8|Beam-casting + rendering|SVDAG drill + Gouraud + Perlin → pixel buffer|yes
FP9|Pass 9|Upscale + UI composite|edge-aware upscale + Clay layout → final framebuffer|yes

# llm_triggers(id|condition|description)
LT1|Rule gap|Prolog evaluation found no matching rule for entity's current state
LT2|Designer flag|entity's behavior set includes "generate" behavior that won UtilityAI scoring
LT3|Novel situation|entity's fact set has combination no existing rule covers; zero path coverage
LT4|Periodic refresh|entity scheduled for behavior update every N frames (configurable)
# Typical frame: 0-10 entities out of 100,000 trigger LLM

# llm_batch_format(id|direction|structure|depth)
LB1|Input|entity_id, current_state, fact_0..fact_15 (up to 16 relevant facts), goal_type, context_hash|depth=20
LB2|Output|entity_id, new_rule_head, body_pred_0..body_pred_3 (up to 4 body predicates), action_id, confidence, source_pattern, verification_status|depth=10
# Output = integer tuples: predicate IDs and action IDs, not strings, not code

# llm_inference_hw(id|aspect|detail)
LI1|Forward pass|embedding lookup → attention (Q×Kᵀ, scale, integer softmax LUT, ×V) → feedforward (2 matmuls + activation) → layer norm (integer mean/variance) → repeat per layer → final projection|all MUL,ADD,SHR
LI2|Model size|100M params at i32 = 400MB; fits DDR3 with room for everything else
LI3|Performance (Zynq-7020)|30M integer MACs per token; 30 cores × 150MHz = 4.5 GMACs/s; ~6.67ms/token; <1 token/frame
LI4|Multi-frame strategy|new rule ~8 tokens; spread across ~3 frames (53ms); entity uses existing behavior during generation; imperceptible at 60fps
LI5|Scaling|Zynq-7045(130 cores): 1.54ms/token; Zynq-7100(270): 0.74ms; UltraScale+(400): 0.50ms; linear with core count

# verification(id|check|mechanism)
VR1|Predicate existence|for each body_pred, check if F=body_pred batch exists with count>0 in KB
VR2|Logical consistency|new rule's head+body doesn't contradict existing rules
VR3|Action validity|action_id valid for entity's current state and behavior set
VR4|Confidence threshold|confidence ≥ minimum_confidence_threshold
VR5|Gate|all pass → verification_status=1 (verified); any fail → verification_status=0 (rejected, rule discarded)

# triveritas(id|dimension|mechanism|result_on_fail)
TV1|Logical validity (L)|scan KB for contradictions with same predicate; integer comparison|L=fail, store contradicting fact ID
TV2|Mathematical coherence (M)|check argument values against known valid ranges per predicate position|M=fail
TV3|Empirical anchoring (E)|count source IDs, check verification levels of each source|E=fail (no provenance) or E=weak
# Classification: 3-bit bitmask [L,M,E]; all pass→knowledge; 2/3→strong opinion; L+M no E→rationalist trap; E no L→empiricist trap

# scales_method(id|aspect|mechanism)
SC1|Materiality gate|scope = (affected_entities×256)/total_entities; <5%→skip LLM; 5-20%→low budget; 20-50%→normal; >50%→critical priority
SC2|Fruit of the Plant|after rule active 60+ frames: compare entity state before/after; improved→increase confidence; worsened→decrease, may remove; flag for new generation

# kb_structure(id|aspect|detail)
KB1|Entity state IS KB|entity at position(100,200) health 80 = facts F=position, F=health, F=state; regenerated from entity batch every frame (Pass 1)
KB2|Persistent facts|survive across frames: has_item, knows_about, allied_with; live in DDR3 separate from per-frame facts; ARM manages lifecycle
KB3|LLM rules persist|generated once, verified once, active until superseded; entity doesn't know if rules from designer or LLM
KB4|KB growth|accumulates facts + persistent facts + designer rules + LLM rules + provenance; ARM manages hot/warm/cold via LRU eviction to SD card; nothing deleted
KB5|No degradation|no context window overflow; no attention degradation; Prolog matches on predicate IDs not token position; fact from frame 1 = fact from frame 100000
KB6|Sessions|session = filter on KB; V=session_id, R=session_type; multiple sessions read/write same KB simultaneously

# domain_eating(id|aspect|detail)
DE1|Process|obtain source → run domain parser (Zig on ARM) → parser outputs VFR fact batches with provenance → validate via Prolog (FPGA) → load into KB DDR3 → immediately queryable
DE2|Parser output|every parser produces same format: predicate-keyed fact batches [F=predicate_id, count=N, depth=D] with provenance (source hash, byte offset, version)
DE3|Cross-domain queries|all domains share VFR batch format + Prolog evaluation; game facts and medical facts both integer batches with different F values; Prolog unifies via shared argument values
DE4|No retraining|KB grows; new predicates get new F values; new rules reference new predicates; FPGA processes identically

# path_coverage(id|path_count|meaning)
PC1|0 paths|no rules cover this situation; LLM trigger
PC2|1 path|one rule applies; fragile, flag for review
PC3|3+ paths|multiple rules agree; high confidence
# Integer count of matching entries in rule batch. System counts, doesn't guess.

# fpga_architecture(id|aspect|detail)
FA1|Target|Xilinx Zynq-7020 (Zybo Z7-20 board)
FA2|Design language|Verilog; ~1650 lines RTL + ~1000 lines testbench = ~2650 total
FA3|Clock|150 MHz target
FA4|Cores|30 VFR cores, identical, each with 9KB local BRAM (2 BRAM tiles)
FA5|Entities per core|38 at depth 48 (240 bytes/entity)
FA6|Shared BRAM|24KB (3 BRAM tiles); read-only during frame; Perlin tables, UtilityAI curves, state machine data, behavior sets
FA7|ARM interface|AXI GP slave (control registers) + AXI HP master (DDR3 DMA)
FA8|Core pipeline|4-stage in-order: fetch → decode → execute → writeback

# module_hierarchy(id|module|lines_est|purpose)
MH1|fpga_top.v|~200|top-level instantiation; wires all components
MH2|axi_registers.v|~200|ARM control/status register bank; AXI4-Lite slave; 18 registers at 0x00-0x44
MH3|batch_dispatcher.v|~400|work partitioning; 11-state FSM; DMA coordination; distributes entities to cores
MH4|shared_bram.v|~50|dual-port BRAM; port A write (DMA load), port B read (all cores)
MH5|vfr_core.v|~300|integrates submodules; pipeline control; load/store; batch control; jump evaluation
MH6|vfr_fetch.v|~50|program counter + instruction read from local BRAM
MH7|vfr_decode.v|~150|opcode extraction; control signal generation (is_alu/load/store/jump/batch/transfer/halt)
MH8|vfr_alu.v|~200|purely combinational; no clock; opcode+operands in, result out same cycle
MH9|vfr_registers.v|~100|16 V regs (i32) + 16 R regs (i8) + batch control (BF,BC,BD,BI) + flags (EQ,LT,GT,OV,DONE) + MA

# isa_opcodes(id|range|category|opcodes)
OP1|0x00|Control|HALT
OP2|0x01-0x05|Jump|JMP, JEQ, JLT, JGT, JDONE
OP3|0x08-0x0C|Arithmetic|ADD, SUB, MUL, ADDR, SUBR
OP4|0x10-0x13|Bitwise|AND, OR, XOR, NOT
OP5|0x18-0x1B|Shift|SHR, SHL, SHR5, SHL5
OP6|0x20-0x24|VFR|DECOMP(V>>5→Vd, V&0x1F→Rd), RECOMP((V<<5)|R→Vd), RNORM, RACCUM, SCALE
OP7|0x28-0x29|Compare|CMP, CMPR
OP8|0x30-0x35|Load/Store|LDV, LDR, STV, STR, LDVR, STVR
OP9|0x38-0x3A|Batch|BLOAD(read 7-byte header), BNEXT(BI+=1, set DONE if BI==BC), BADDR(Vd=MA+7+BI*BD*5)
OP10|0x3C-0x3F|Transfer|TSEND, TRECV, TWAIT, TDONE
# Instruction width: 32 bits fixed. Opcode: 6 bits. Registers: 4-bit indices. Immediate: 18 bits.

# dispatcher_states(id|state|action)
DS1|S_IDLE|wait for go signal; compute total_chunks = ceil(entity_count/(NUM_CORES×ENTITIES_PER_CORE))
DS2|S_CALC_CHUNKS|compute chunk entity range: start, count
DS3|S_DMA_LOAD|issue AXI read burst from entity_addr+offset
DS4|S_DMA_LOAD_WAIT|distribute arriving data to core BRAMs: entities 0-37→core 0, 38-75→core 1, etc.
DS5|S_START_CORES|assert core_start for all cores with data; start cycle counter
DS6|S_WAIT_CORES|poll core_done bits; increment cycle counter
DS7|S_DMA_STORE|read render fields from core BRAMs; issue AXI write burst (25 bytes/entity: position, sprite, anim)
DS8|S_DMA_STORE_WAIT|wait for AXI write complete
DS9|S_NEXT_CHUNK|increment chunk; if more chunks → S_CALC_CHUNKS; else → S_DONE
DS10|S_DONE|set done flag; accumulate cycle_count

# register_map(id|addr|name|access|description)
RM1|0x00|CONTROL|W|write 1 to start, auto-clears
RM2|0x04|STATUS|R|[0]=busy, [1]=done, [2]=error
RM3|0x08|ENTITY_ADDR|R/W|DDR3 address of entity batch
RM4|0x0C|ENTITY_COUNT|R/W|number of entities
RM5|0x10|ENTITY_DEPTH|R/W|fields per entity
RM6|0x14|RENDER_ADDR|R/W|DDR3 address for render output
RM7|0x18|RENDER_FIELDS|R/W|fields to write back
RM8|0x1C|SM_ADDR|R/W|state machine batch address
RM9|0x20|BEHAVIOR_ADDR|R/W|behavior set batch address
RM10|0x24|FACT_SCHEMA_ADDR|R/W|fact generation rules address
RM11|0x28|ENVELOPE_ADDR|R/W|envelope batch address
RM12|0x2C-0x34|SHARED_LOAD|R/W+W|shared BRAM load: source addr, size, go trigger
RM13|0x38|CORE_COUNT|R|number of VFR cores (hardwired)
RM14|0x3C|CORE_STATUS|R|per-core done/busy bits
RM15|0x40|CYCLE_COUNT|R|cycles for last batch
RM16|0x44|CHUNK_COUNT|R|chunks processed

# resource_utilization(id|component|luts|ffs|bram|dsp48)
RU1|vfr_core × 30|42000|42000|60|30
RU2|batch_dispatcher|2000|1500|0|0
RU3|axi_registers|500|400|0|0
RU4|shared_bram|100|50|3|0
RU5|axi_dma_engine|1500|1000|0|0
RU6|interconnect+infra|1000|600|2|0
RU7|TOTAL|47100|45550|65|30
RU8|Available (Zynq-7020)|53200|106400|140|220
RU9|Utilization|88.5%|42.8%|46.4%|13.6%
# LUTs are limiting resource. If timing needs space, reduce to 28 cores.

# timing(id|path|estimate|notes)
TM1|ALU multiply|~4ns|DSP48 handles
TM2|BRAM read|~2ns|single-cycle synchronous
TM3|Register file read|~1ns|small LUT-based RAM
TM4|Instruction decode|~1.5ns|combinational case
TM5|Worst pipeline stage (execute)|~5ns|ALU+mux
TM6|Period at 150MHz|6.67ns|margin: 1.67ns slack
# Fallbacks: 125MHz (safe), add pipeline reg (keeps 150MHz), reduce cores

# zig_interface(id|aspect|detail)
ZI1|Base address|FPGA_BASE = 0x4000_0000
ZI2|Access pattern|memory-mapped volatile register writes; poll STATUS for completion
ZI3|Dispatch function|set ENTITY_ADDR, ENTITY_COUNT, ENTITY_DEPTH, RENDER_ADDR; write CONTROL=1; poll STATUS bit 1
ZI4|Shared BRAM load|set source addr + size; write SHARED_LOAD_GO=1; poll STATUS bit 2

# boot(id|aspect|detail)
BT1|SD card|single BOOT.bin on FAT32 partition
BT2|Contents|FSBL (init DDR3, clocks, MIO, program FPGA) + fpga_top.bit (VFR design) + silo_kernel.elf (Zig bare-metal)
BT3|Build|bootgen -image boot.bif -o BOOT.bin -w
BT4|Entry|kernel at 0x00100000; Zynq boot ROM reads BOOT.bin automatically on power-up

# milestones(id|weeks|milestone|deliverable)
ML1|1-2|ALU verified|vfr_alu.v + tb_alu.v (simulation)
ML2|3-4|Single core verified|vfr_core.v + tb_core.v (simulation)
ML3|5-6|1 core on hardware|fpga_top.bit + ARM C test
ML4|7-8|Dispatcher + 4 cores|batch_dispatcher.v + ARM test batch
ML5|9-10|Scale to 30 cores|full fpga_top + performance profiling
ML6|11-12|Port to Zig bare-metal|silo_kernel.elf + UART output
ML7|13-14|Shared BRAM + entity pipeline|lookup tables + entity processing verified
ML8|15-16|Beam-casting + rendering|SVDAG + pixels on HDMI
ML9|17-20|Full integration + optimization|complete system at 60fps

# simulation_tests(id|testbench|test_count|description)
ST1|tb_alu.v (~300 lines)|~200 vectors|every opcode with edge cases (zero, negative, overflow)
ST2|tb_core.v (~300 lines)|1 program|load program into BRAM; verify batch processing of 4 entities with add
ST3|tb_dispatcher.v (~200 lines)|1 scenario|100 entities across 4 cores; verify DMA load/store and chunk processing
ST4|tb_system.v (~200 lines)|1 scenario|full fpga_top with mock AXI; ARM register writes; verify end-to-end

# shared_bram_contents(id|addr_range|content|size)
SB1|0x0000-0x00FF|Perlin permutation table|1024 bytes
SB2|0x0100-0x01FF|Perlin fade table|1024 bytes
SB3|0x0200-0x09FF|UtilityAI curve tables (8 curves × 256 entries)|8192 bytes
SB4|0x0A00-0x0FFF|State machine data|~6144 bytes
SB5|0x1000-0x17FF|Behavior set data|~8192 bytes
# Total: ~24576 bytes (3 BRAM tiles)

# relationships(from|rel|to)
S1|invalidates|all entries (CKS framework falsified)
P1|governs|FP4a,LI1-LI5
P2|governs|VT1-VT12
P3|enables|P4
P4|implemented_by|VR1-VR5
P5|defines|FP4a(position in pipeline)
P6|enables|DE1-DE4
FP1|prereq_of|FP2
FP2|prereq_of|FP3
FP3|prereq_of|FP4a
FP3|detects|LT1,LT3
FP4a|prereq_of|FP4b
FP4b|prereq_of|FP5
FP4b|implements|VR1-VR5,TV1-TV3,SC1
FP5|prereq_of|FP6
FP6|prereq_of|FP7
FP7|prereq_of|FP8
FP8|prereq_of|FP9
LB2|verified_by|VR1-VR5
VR5|gates|FP5(only verified rules enter scoring)
TV1-TV3|produces|3-bit classification bitmask
SC1|gates|FP4a(skip LLM for negligible scope)
SC2|may_trigger|LT4(periodic refresh)
KB1|regenerated_by|FP1
KB3|produced_by|FP4a
DE2|uniform_format|VT3(all parsers produce same fact batch format)
FA4|instantiated_in|MH1
MH5|contains|MH6,MH7,MH8,MH9
MH3|controls|MH5(start/done signals)
MH3|uses|FA7(AXI HP for DMA)
MH2|uses|FA7(AXI GP for registers)
DS1|prereq_of|DS2
DS2|prereq_of|DS3
DS3|prereq_of|DS4
DS4|prereq_of|DS5
DS5|prereq_of|DS6
DS6|prereq_of|DS7
DS7|prereq_of|DS8
DS8|prereq_of|DS9
DS9|branches_to|DS2(more chunks) or DS10(done)
ZI3|writes_to|RM1-RM6
BT2|contains|FA4(bitstream),ZI1(kernel)

# section_index(section|title|ids)
# CKS-MATH-148 sections:
148.1|Overview|P1,P5
148.2|Everything Is VFR|P2,VT1-VT12,TT0-TT19
148.3|Inline LLM in Game Pipeline|FP1-FP9,LT1-LT4,LB1-LB2
148.4|LLM Inference on VFR Hardware|LI1-LI5
148.5|KB as Live Game State|KB1-KB6
148.6|Triveritas|TV1-TV3
148.7|Scales Method|SC1-SC2
148.8|Domain Eating|DE1-DE4
148.9|No Hallucination by Construction|P3,P4,VR1-VR5,PC1-PC3
148.10|Session Architecture|KB5,KB6
148.11|Complete Data Type Summary|VT1-VT12
148.12|Frame Pipeline Final Form|FP1-FP9
# CKS-MATH-145 sections:
145.1|Overview|FA1-FA8
145.2|Design Parameters|FA1-FA8
145.3|Module Hierarchy|MH1-MH9
145.4|Module Specifications|MH1-MH9,OP1-OP10
145.5|Vivado IP Integrator|FA7,BT1-BT4
145.6|Simulation Plan|ST1-ST4
145.7|Resource Utilization|RU1-RU9
145.8|Timing Targets|TM1-TM6
145.9|ARM Software Interface|ZI1-ZI4
145.10|SD Card Boot|BT1-BT4
145.11|Development Milestones|ML1-ML9
145.12|Files Checklist|MH1-MH9,ST1-ST4

# decode_legend
id_prefixes: S=status, P=principle, VT=vfr_type, TT=term_type, FP=frame_pipeline, LT=llm_trigger, LB=llm_batch, LI=llm_inference_hw, VR=verification, TV=triveritas, SC=scales, KB=kb_structure, DE=domain_eating, PC=path_coverage, FA=fpga_architecture, MH=module_hierarchy, OP=isa_opcode, DS=dispatcher_state, RM=register_map, RU=resource_utilization, TM=timing, ZI=zig_interface, BT=boot, ML=milestone, ST=simulation_test, SB=shared_bram
VFR: [V:i32, R:i8] = value-remainder pair; universal data format
batch_header: [F:i16, count:u32, depth:u8] = 7 bytes preceding every batch
confidence_levels: 0=speculative, 1=inferred, 2=stated, 3=verified
triveritas_bitmask: [L,M,E] 3-bit; 8 combinations mapping to confidence categories
rel_types: invalidates|governs|enables|implemented_by|defines|prereq_of|detects|implements|gates|produces|may_trigger|regenerated_by|produced_by|uniform_format|instantiated_in|contains|controls|uses|branches_to|writes_to
framework_status: INVALIDATED — math does not compile; all CKS papers falsified
target_hardware: Xilinx Zynq-7020 (Zybo Z7-20); 30 VFR cores at 150MHz; ~1650 lines Verilog
