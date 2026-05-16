# VDR-LLM-Prolog FPGA Acceleration Technical Specification

## Document Purpose

This specification defines the hardware acceleration subsystem for VDR-LLM-Prolog, targeting the Xilinx Zynq-7020 SoC (Zybo Z7-20 development board) as the proof-of-concept platform. The FPGA accelerates data-plane operations — Prolog fact matching, Q335 batch arithmetic, attention score computation, constraint checking, and softmax normalization — while the host Zig software retains all control-plane operations. Every accelerated operation produces results identical to the software path. The IOSE declarations, builtin contracts, and VDR-14 system specification are unchanged.

---

## 1. System Architecture

### 1.1 Host-FPGA Division

The Zynq-7020 contains a dual-core ARM Cortex-A9 (processing system, PS) and programmable logic (PL) on the same die, sharing DDR3 memory. The VDR-LLM-Prolog Zig runtime executes on the ARM cores as bare-metal software. The FPGA fabric implements VDR arithmetic cores with a batch dispatcher.

The host is responsible for: the orchestrated inference loop (assess, formalize, execute, store), KB tree management (create, delete, scope, mount, connect), session management (snapshot, clone, kill), grammar parsing and generation, command token parsing and dispatch, LLM forward and backward pass orchestration, remainder tree operations beyond depth 4, functional remainder resolution (Newton, Taylor, series), all control flow decisions.

The FPGA is responsible for: parallel Prolog fact matching across KB partitions, Q335 batch arithmetic (parameter add, subtract, multiply, divmod), row-parallel attention score computation (QKᵀ), parallel constraint evaluation, parallel denominator budget checking, softmax surrogate computation (map-reduce), VDR fraction cross-multiply comparison for unification.

### 1.2 Communication

Two AXI interfaces connect PS to PL. AXI GP0 (general purpose, 32-bit) provides register-mapped control for small queries and configuration. AXI HP0 (high performance, 64-bit) provides DMA for bulk data transfer between DDR3 and core BRAMs.

For small operations (single Prolog query, single constraint check), the host writes query parameters directly to control registers and reads results from status registers — no DMA overhead. For bulk operations (batch parameter update, attention matrix computation, full KB scan), the host sets DDR3 source and destination addresses in registers, triggers DMA, and polls for completion.

### 1.3 Memory Map

```
DDR3 (512 MB, shared PS/PL):
  0x0000_0000 - 0x00FF_FFFF: Zig kernel + stack + heap (16 MB)
  0x0100_0000 - 0x08FF_FFFF: KB fact store, partitioned (128 MB)
  0x0900_0000 - 0x10FF_FFFF: Model parameters, Q335 format (128 MB)
  0x1100_0000 - 0x18FF_FFFF: Gradient storage (128 MB)
  0x1900_0000 - 0x1CFF_FFFF: Attention matrices + working buffers (64 MB)
  0x1D00_0000 - 0x1FFF_FFFF: DMA transfer buffers, double-buffered (48 MB)

PL register space (AXI GP0):
  0x4000_0000 - 0x4000_00FF: Control and status registers (64 registers)
  0x4000_0100 - 0x4000_01FF: Fast-path query registers (64 registers)

PL BRAM space (shared, read-only during operation):
  Internal to PL, not memory-mapped to PS.
  Loaded via DMA before operation begins.
```

---

## 2. VDR-Q335 Core Design

### 2.1 Working Width

All arithmetic operates on 384-bit integers. This covers Q335 numerators (approximately 340 bits) with 44 bits of margin for intermediate overflow during multiply-accumulate. The denominator D = 2^335 is never stored — it is implicit in the Q335 convention. Division by D is a right-shift by 335 bits. Multiplication results (768 bits) split at bit 335: upper bits become V, lower 335 bits become R.

### 2.2 Register File

Each core contains:

Eight V registers (V0-V7), each 384 bits wide. These hold VDR value components, Q335 numerators, intermediate arithmetic results, and accumulator values.

Eight R registers (R0-R7), each 384 bits wide. These hold remainder values, comparison operands, and temporary storage during multi-step operations. In Q335 mode, R holds the divmod remainder.

Four index registers (I0-I3), each 32 bits. These hold KB IDs, fact indices, batch positions, and loop counters.

Batch control registers: BF (16 bits, batch format/predicate ID), BC (32 bits, batch count), BD (8 bits, batch depth), BI (32 bits, batch index).

Flags: EQ (equal), LT (less than), GT (greater than), OV (overflow), DONE (batch complete), CLOSED (R is zero).

One memory address register MA (32 bits) for BRAM addressing.

**Total register storage per core:** 8 × 384 + 8 × 384 + 4 × 32 + 88 + 32 = 6,264 bits = 783 bytes. Implemented in distributed RAM (LUTs), not BRAM.

### 2.3 ALU

The ALU is the computational engine of each core. It is pipelined internally but presents a single-cycle interface for simple operations and a multi-cycle interface for multiplication.

**384-bit adder/subtractor.** Carry-select architecture: 384 bits divided into 6 × 64-bit blocks. Each block computes sum assuming carry-in of 0 and 1 simultaneously. Multiplexer selects correct result as carry propagates. Latency: 1 cycle. Resources: approximately 400 LUTs.

**128-bit iterative multiplier.** Computes 384 × 384 → 768-bit product by tiling into 3 × 3 = 9 partial products of 128 × 128 → 256 bits. Each partial product uses DSP48E1 cascade (5 DSP48 slices per 128-bit multiply, chaining 25×18 primitives). Nine iterations with accumulation into a 768-bit result register. Latency: 9 cycles. Resources: 5 DSP48E1 slices (time-multiplexed across 9 iterations), approximately 200 LUTs for accumulation and control.

**384-bit barrel shifter.** Shifts by 0-383 positions in a single cycle via 9 stages of 2:1 multiplexers (shift by 1, 2, 4, 8, 16, 32, 64, 128, 256). Special-case SHR335 instruction uses a fixed wiring extraction — bits [334:0] to one register, bits [767:335] to another — requiring no multiplexers. Latency: 1 cycle for barrel shift, 0 additional logic for SHR335. Resources: approximately 350 LUTs for the barrel shifter.

**384-bit comparator.** Cascaded 64-bit comparisons with early termination. Sets EQ, LT, GT flags. Latency: 1 cycle. Resources: approximately 100 LUTs.

**Cross-multiply unit.** For VDR fraction unification: computes A.V × B.D and B.V × A.D using the iterative multiplier (two invocations, 18 cycles total), then compares the two 768-bit products. Sets EQ flag if equal. Latency: 19 cycles (18 multiply + 1 compare). Invoked by CROSS_MUL instruction.

**Q335 divmod.** Dedicated instruction SHR335 that extracts the quotient and remainder of division by 2^335 in zero additional cycles — it is a fixed wiring of the 768-bit multiply result into two 384-bit registers. The upper bits [767:335] are the quotient (new V), the lower bits [334:0] are the remainder (new R, zero-extended to 384 bits). This is the core VDR nesting operation and it is free in hardware.

### 2.4 Remainder BRAM

Each core has a dedicated 2KB BRAM region for remainder tree storage. Organized as 16 nodes of 128 bytes each:

```
Node structure (128 bytes):
  V:      384 bits = 48 bytes
  D:      384 bits = 48 bytes  (typically 2^335, stored for generality)
  R_idx:  16 bits  = 2 bytes   (index of child node, 0xFFFF = no child = closed)
  depth:  8 bits   = 1 byte
  flags:  8 bits   = 1 byte    (closed, active, functional marker)
  pad:    28 bytes             (alignment to 128-byte boundary)
```

Maximum depth: 16 levels, matching the VDR-8 scope chain limit and sufficient for any Q335 operation chain encountered in training (Q335 multiply chains rarely exceed depth 10 per VDR-13 DC1-DC7).

Free-list pointer (4 bits) tracks the next available node. Allocation is push/pop on a 16-entry stack stored in a 64-bit register.

Instructions NEST (allocate child node, set parent R_idx), UNNEST (deallocate child, set parent R_idx to 0xFFFF), and DEPTH (read current depth counter) manage the tree.

### 2.5 Instruction BRAM

Each core has 4KB of instruction BRAM, holding up to 1024 × 32-bit instructions. Programs are loaded by the dispatcher via DMA before core execution begins. Different programs are loaded for different operation types (fact matching, parameter update, attention dot product, constraint evaluation).

### 2.6 Pipeline

Four stages, in-order, no hazard detection (software/microcode schedules around latencies):

**Fetch:** Read instruction from instruction BRAM at program counter. Increment PC. 1 cycle.

**Decode:** Extract opcode (6 bits), register operands (4 bits each), immediate (18 bits). Generate control signals: is_alu, is_load, is_store, is_jump, is_batch, is_transfer, is_vdr, is_unify, is_halt, mul_start. 1 cycle.

**Execute:** For single-cycle operations (ADD, SUB, CMP, SHIFT, logic): compute result, set flags. For multi-cycle operations (MUL, CROSS_MUL): stall pipeline for 9 or 19 cycles while iterative multiplier completes. For memory operations: compute address. For jumps: evaluate condition from flags, update PC if taken. 1-19 cycles.

**Writeback:** Write result to destination register or BRAM. 1 cycle.

**Total single-cycle instruction throughput:** 1 instruction per cycle at 150 MHz = 150 MIPS per core (excluding multi-cycle stalls).

### 2.7 Resource Summary per Core

| Component | LUTs | FFs | BRAM (18Kb tiles) | DSP48E1 |
|-----------|------|-----|-------------------|---------|
| Register file (distributed) | 400 | 6,264 | 0 | 0 |
| Adder/subtractor (384-bit) | 400 | 50 | 0 | 0 |
| Iterative multiplier (128-bit) | 200 | 600 | 0 | 5 |
| Barrel shifter (384-bit) | 350 | 0 | 0 | 0 |
| Comparator (384-bit) | 100 | 10 | 0 | 0 |
| Cross-multiply control | 80 | 40 | 0 | 0 |
| Remainder BRAM | 30 | 10 | 1 | 0 |
| Instruction BRAM | 30 | 10 | 2 | 0 |
| Pipeline control | 200 | 150 | 0 | 0 |
| Unification micro-sequencer | 200 | 100 | 0 | 0 |
| Batch interface | 100 | 80 | 0 | 0 |
| **Core total** | **2,090** | **7,314** | **3** | **5** |

---

## 3. System-Level Architecture

### 3.1 Core Count

Target: 10 VDR-Q335 cores on Zynq-7020.

| Component | LUTs | FFs | BRAM | DSP48 |
|-----------|------|-----|------|-------|
| 10 × VDR core | 20,900 | 73,140 | 30 | 50 |
| Batch dispatcher | 2,500 | 1,800 | 0 | 0 |
| AXI register bank | 600 | 500 | 0 | 0 |
| AXI DMA engine | 2,000 | 1,200 | 0 | 0 |
| Shared BRAM controller | 150 | 80 | 3 | 0 |
| Interconnect and infrastructure | 1,500 | 800 | 2 | 0 |
| Reduction network (tree adder) | 1,200 | 600 | 0 | 0 |
| **System total** | **28,850** | **78,120** | **35** | **50** |
| **Available (Zynq-7020)** | **53,200** | **106,400** | **140** | **220** |
| **Utilization** | **54.2%** | **73.4%** | **25.0%** | **22.7%** |

Margin: 45.8% LUT headroom for timing closure, debug infrastructure, and future additions. FF utilization is the limiting factor at 73.4%, but Zynq-7020 FFs are abundant relative to LUTs.

### 3.2 Batch Dispatcher

The dispatcher is an FSM that partitions work across cores, manages DMA transfers, and collects results. It implements 11 states adapted from the VFR dispatcher.

```
State machine:
  S_IDLE          → S_CALC on go signal
  S_CALC          → S_LOAD_PROG (compute work partition)
  S_LOAD_PROG     → S_LOAD_DATA (DMA program to core instruction BRAMs)
  S_LOAD_DATA     → S_LOAD_WAIT (DMA data to core BRAMs/registers)
  S_LOAD_WAIT     → S_START (wait for DMA complete)
  S_START         → S_WAIT (assert start to all active cores)
  S_WAIT          → S_STORE (poll core done bits)
  S_STORE         → S_STORE_WAIT (DMA results from cores to DDR3)
  S_STORE_WAIT    → S_NEXT (wait for DMA complete)
  S_NEXT          → S_CALC or S_DONE (more chunks → loop; else → done)
  S_DONE          → S_IDLE (set done flag)
```

**Work partitioning.** The dispatcher divides the total work item count by the core count (10). Each core receives its start index and count. For fact matching, work items are fact indices. For parameter updates, work items are parameter indices. For attention computation, work items are matrix row indices.

**Program selection.** The dispatcher loads a different microprogram into core instruction BRAMs depending on the operation type. Six programs are stored in DDR3:

| Program | Purpose | Instruction Count (est.) |
|---------|---------|------------------------|
| prog_fact_match | Scan facts by predicate ID, collect matches | ~40 |
| prog_q335_add | Batch Q335 addition (parameter update) | ~20 |
| prog_q335_mul | Batch Q335 multiply with divmod and nesting | ~50 |
| prog_dot_product | 384-bit dot product accumulation for attention | ~35 |
| prog_constraint_eval | Evaluate Prolog condition against fact set | ~60 |
| prog_softmax_surr | Compute (z-m+c)² for each logit, accumulate sum | ~30 |

### 3.3 Shared BRAM

Three 18Kb BRAM tiles (6,144 bytes usable) holding read-only data loaded once before operation begins:

```
Offset    Size    Content
0x0000    1,056   Q335 constant table: 22 constants × 48 bytes (384-bit numerators)
0x0420    512     Predicate ID lookup table: 256 entries × 2 bytes (predicate → fact partition index)
0x0620    2,048   Grammar enum value tables: up to 128 enums × 16 entries × 1 byte
0x0E20    512     Configuration: budget thresholds, confidence defaults, operational parameters
0x1020    1,016   Reserved for future use (twiddle tables, etc.)
```

Port A: write-only, connected to DMA engine for loading. Port B: read-only, broadcast to all cores.

### 3.4 Reduction Network

A binary tree of 384-bit adders connecting core outputs for operations that require global aggregation (softmax denominator sum, norm computation, global dot product). Five levels of adders reduce 10 core outputs to one 384-bit sum. Latency: 5 cycles. Resources: approximately 1,200 LUTs, 600 FFs.

The reduction network is optional — results can alternatively be collected by DMA and reduced in software. Hardware reduction is faster for operations where the reduction is on the critical path (softmax).

---

## 4. Register Map

### 4.1 Control Registers (0x4000_0000 - 0x4000_007F)

| Offset | Name | Width | Access | Description |
|--------|------|-------|--------|-------------|
| 0x00 | CONTROL | 32 | W | [0] go, [1] abort, [4:2] operation type (0=fact_match, 1=q335_add, 2=q335_mul, 3=dot_product, 4=constraint, 5=softmax), [7:5] reserved. Auto-clears go on start. |
| 0x04 | STATUS | 32 | R | [0] busy, [1] done, [2] error, [3] dma_active, [13:4] core_done bits (10 cores), [31:14] reserved |
| 0x08 | SRC_ADDR | 32 | R/W | DDR3 source address for input data |
| 0x0C | SRC_COUNT | 32 | R/W | Number of input work items |
| 0x10 | SRC_STRIDE | 32 | R/W | Bytes per work item (48 for single Q335, 96 for pair, variable for facts) |
| 0x14 | DST_ADDR | 32 | R/W | DDR3 destination address for output data |
| 0x18 | DST_STRIDE | 32 | R/W | Bytes per output item |
| 0x1C | PARAM_0 | 32 | R/W | Operation-specific parameter 0 (e.g., target predicate ID for fact_match) |
| 0x20 | PARAM_1 | 32 | R/W | Operation-specific parameter 1 (e.g., learning rate V[11:0] for q335_add) |
| 0x24 | PARAM_2 | 32 | R/W | Operation-specific parameter 2 (e.g., learning rate V[31:12]) |
| 0x28 | PARAM_3 | 32 | R/W | Operation-specific parameter 3 |
| 0x2C | PROG_SEL | 32 | R/W | Program index (0-5) to load into core instruction BRAMs |
| 0x30 | PROG_ADDR | 32 | R/W | DDR3 address of program binary (if PROG_SEL = 0xFF, load custom) |
| 0x34 | SHARED_SRC | 32 | R/W | DDR3 source for shared BRAM load |
| 0x38 | SHARED_SIZE | 32 | R/W | Bytes to load into shared BRAM |
| 0x3C | SHARED_GO | 32 | W | Write 1 to trigger shared BRAM load; STATUS[3] indicates DMA active |
| 0x40 | CYCLE_COUNT | 32 | R | Clock cycles for last operation |
| 0x44 | MATCH_COUNT | 32 | R | Number of matches found (fact_match) or items processed |
| 0x48 | ERROR_CODE | 32 | R | Error detail: [7:0] error type, [15:8] core that errored, [31:16] instruction PC |
| 0x4C | CORE_COUNT | 32 | R | Number of VDR cores (hardwired to 10) |
| 0x50 | VERSION | 32 | R | Hardware version (hardwired, major.minor.patch in 8.8.16 format) |
| 0x54 | RESULT_LO | 32 | R | Low 32 bits of scalar result (for fast-path operations) |
| 0x58 | RESULT_HI | 32 | R | Next 32 bits of scalar result |
| 0x5C-0x7C | RESULT_2-9 | 32 | R | Remaining 256 bits of 384-bit scalar result (12 registers × 32 bits = 384 bits total via RESULT_LO through RESULT_9) |

### 4.2 Fast-Path Query Registers (0x4000_0100 - 0x4000_01FF)

For single Prolog queries without DMA:

| Offset | Name | Width | Access | Description |
|--------|------|-------|--------|-------------|
| 0x100 | FP_PREDICATE | 32 | R/W | Predicate ID to match (16-bit, upper 16 reserved) |
| 0x104 | FP_ARG0_LO | 32 | R/W | First argument, low 32 bits |
| 0x108 | FP_ARG0_HI | 32 | R/W | First argument, bits [63:32] |
| 0x10C | FP_ARG_COUNT | 32 | R/W | Number of arguments to match (0 = predicate only) |
| 0x110 | FP_GO | 32 | W | Trigger fast-path query |
| 0x114 | FP_STATUS | 32 | R | [0] busy, [1] done, [15:2] match count |
| 0x118 | FP_MATCH_0 | 32 | R | Index of first matching fact |
| 0x11C | FP_MATCH_1 | 32 | R | Index of second matching fact |
| 0x120 | FP_MATCH_2 | 32 | R | Index of third matching fact |
| 0x124 | FP_MATCH_3 | 32 | R | Index of fourth matching fact |
| 0x128-0x1FC | Reserved | — | — | Expansion for multi-argument queries |

Fast-path latency: approximately 10 + (fact_count / 10) cycles. For 200 facts: approximately 30 cycles = 200ns at 150 MHz.

---

## 5. Instruction Set Architecture

### 5.1 Instruction Format

All instructions are 32 bits fixed width.

```
Type R (register-register):
  [31:26] opcode (6 bits)
  [25:22] Vd / Rd destination (4 bits, selects V0-V7 or R0-R7)
  [21:18] Vs1 / Rs1 source 1 (4 bits)
  [17:14] Vs2 / Rs2 source 2 (4 bits)
  [13:0]  reserved / sub-function

Type I (register-immediate):
  [31:26] opcode (6 bits)
  [25:22] Vd / Rd destination (4 bits)
  [21:18] Vs1 / Rs1 source (4 bits)
  [17:0]  immediate (18 bits, sign-extended to 32 for index ops)

Type J (jump):
  [31:26] opcode (6 bits)
  [25:0]  target address (26 bits, word-addressed = 256M instruction space, far more than needed)

Type B (batch):
  [31:26] opcode (6 bits)
  [25:22] register (4 bits)
  [21:0]  reserved / batch parameters
```

### 5.2 Opcode Table

| Opcode | Mnemonic | Format | Cycles | Description |
|--------|----------|--------|--------|-------------|
| 0x00 | HALT | — | 1 | Stop core, set DONE flag |
| 0x01 | NOP | — | 1 | No operation |
| 0x02 | JMP | J | 1 | Unconditional jump to address |
| 0x03 | JEQ | J | 1 | Jump if EQ flag set |
| 0x04 | JLT | J | 1 | Jump if LT flag set |
| 0x05 | JGT | J | 1 | Jump if GT flag set |
| 0x06 | JOV | J | 1 | Jump if OV flag set |
| 0x07 | JCLOSED | J | 1 | Jump if CLOSED flag set (R = 0) |
| 0x08 | JDONE | J | 1 | Jump if batch DONE flag set |
| 0x09 | JNE | J | 1 | Jump if EQ flag clear |
| 0x0A | WADD | R | 1 | Vd = Vs1 + Vs2 (384-bit); sets OV |
| 0x0B | WSUB | R | 1 | Vd = Vs1 - Vs2 (384-bit); sets OV, EQ, LT, GT |
| 0x0C | WMUL | R | 9 | [Vd, Rd] = Vs1 × Vs2 (384×384→768, upper→Vd, lower→Rd); pipeline stalls |
| 0x0D | WCMP | R | 1 | Compare Vs1, Vs2; sets EQ, LT, GT flags |
| 0x0E | WABS | R | 1 | Vd = |Vs1| (384-bit) |
| 0x0F | WNEG | R | 1 | Vd = -Vs1 (384-bit, two's complement) |
| 0x10 | AND | R | 1 | Vd = Vs1 & Vs2 (384-bit) |
| 0x11 | OR | R | 1 | Vd = Vs1 \| Vs2 (384-bit) |
| 0x12 | XOR | R | 1 | Vd = Vs1 ^ Vs2 (384-bit) |
| 0x13 | NOT | R | 1 | Vd = ~Vs1 (384-bit) |
| 0x14 | SHR | I | 1 | Vd = Vs1 >> imm (barrel shift, 0-383) |
| 0x15 | SHL | I | 1 | Vd = Vs1 << imm (barrel shift, 0-383) |
| 0x16 | SHR335 | R | 1 | Vd = [Vs1:Rs1][767:335], Rd = [Vs1:Rs1][334:0] (Q335 divmod, fixed wiring) |
| 0x17 | SHRN | I | 1 | Vd = Vs1 >> imm, Rd = Vs1 & ((1<<imm)-1) (general divmod by 2^N) |
| 0x18 | NEST | R | 2 | Allocate remainder node; store Vs1→child.V, Rs1→child.R_idx=0xFFFF; Rd = child index; depth++ |
| 0x19 | UNNEST | R | 2 | Deallocate node at Vs1 index; depth--; parent.R_idx = 0xFFFF |
| 0x1A | RDEPTH | R | 1 | Id = current remainder depth counter |
| 0x1B | RLOAD | R | 2 | Load node at index Vs1: Vd = node.V, Rd = node.R_idx |
| 0x1C | RSTORE | R | 2 | Store to node at index Id: node.V = Vs1, node.R_idx = Rs1 |
| 0x1D | PROJECT | R | var | Scalar projection Π: walk R tree, accumulate (V + Π(R))/D recursively; result in Vd. Cycles = 3 × depth |
| 0x1E | NORMALIZE | R | var | Normalize VDR triple in Vd/Rd: sign convention, GCD reduction, closed-form check. Sets CLOSED flag |
| 0x1F | CROSS_MUL | R | 19 | Cross-multiply: compute Vs1×Rs2, Vs2×Rs1 via two WMUL invocations; set EQ if products equal (VDR fraction unification) |
| 0x20 | UATOM | R | 1 | Compare Id (index reg) vs Is (index reg); set EQ (atom unification via interned integer IDs) |
| 0x21 | LDV | I | 2 | Vd = BRAM[MA + imm] (load 384-bit value from data BRAM) |
| 0x22 | LDR | I | 2 | Rd = BRAM[MA + imm] (load 384-bit remainder) |
| 0x23 | STV | I | 2 | BRAM[MA + imm] = Vs1 (store 384-bit value) |
| 0x24 | STR | I | 2 | BRAM[MA + imm] = Rs1 (store 384-bit remainder) |
| 0x25 | LDVR | I | 2 | Vd = BRAM[MA + imm], Rd = BRAM[MA + imm + 48] (load V and R together) |
| 0x26 | STVR | I | 2 | BRAM[MA + imm] = Vs1, BRAM[MA + imm + 48] = Rs1 (store V and R together) |
| 0x27 | LDI | I | 1 | Id = imm (load immediate to index register) |
| 0x28 | SETMA | I | 1 | MA = Id + imm (set memory address from index register plus offset) |
| 0x29 | BLOAD | B | 3 | Read 7-byte batch header from BRAM[MA]: BF = header.F, BC = header.count, BD = header.depth; MA += 7 |
| 0x2A | BNEXT | B | 1 | BI += 1; if BI == BC then set DONE flag |
| 0x2B | BADDR | R | 1 | Vd(low 32) = MA + BI × BD × 48 (address of current batch element, 48 bytes per 384-bit value) |
| 0x2C | BMATCH | R | 1 | Compare BF against Id (predicate match); set EQ if match |
| 0x2D | LDSHARED | I | 2 | Vd = shared_BRAM[imm] (read from shared read-only BRAM) |
| 0x2E | TSEND | R | 1 | Write Vs1 to inter-core transfer register; assert send_ready |
| 0x2F | TRECV | R | 1 | Vd = inter-core transfer register; wait for send_ready |
| 0x30 | TWAIT | — | var | Stall until transfer complete |
| 0x31 | TDONE | — | 1 | Signal transfer complete |
| 0x32 | REDUCE_ADD | R | 5 | Send Vs1 to reduction network; receive global sum in Vd (5-cycle tree reduction across 10 cores) |
| 0x33 | MOVI | I | 1 | Vd[17:0] = imm (move immediate to low 18 bits, zero-extend) |
| 0x34 | MOVHI | I | 1 | Vd[35:18] = imm (move immediate to bits 35:18) |

### 5.3 Instruction Count Summary

Total: 53 instructions across 10 categories (control, jump, wide arithmetic, bitwise, shift, VDR remainder, unification, load/store, batch, transfer/reduce).

---

## 6. Microprogram Specifications

### 6.1 prog_fact_match

**Purpose:** Scan a partition of facts, return indices of all facts matching a target predicate ID.

**Inputs:** SRC_ADDR = fact partition base address in DDR3. SRC_COUNT = facts in this partition. PARAM_0 = target predicate ID. DST_ADDR = match index output buffer.

**Algorithm:**
```
  LDI I0, 0              ; match count = 0
  LDI I1, 0              ; fact index = 0
  SETMA I1, 0            ; MA = start of fact data
loop:
  BLOAD                   ; read batch header: BF, BC, BD
  BMATCH I2              ; compare BF against target predicate (in I2, loaded from PARAM_0)
  JNE skip
  ; Match found: store fact index to output
  SETMA I0, output_base  ; MA = output buffer + match_count
  STV I1                  ; store matching fact index
  LDI I0, I0+1           ; match_count++
skip:
  ; Advance to next fact: MA += 7 + BC * BD * 48
  BADDR V0               ; compute next fact address
  SETMA V0, 0
  LDI I1, I1+1
  ; Check if done
  WCMP I1, SRC_COUNT
  JLT loop
  HALT
```

**Estimated length:** 40 instructions. **Cycles per fact:** approximately 8 (no match) or 12 (match).

### 6.2 prog_q335_add

**Purpose:** Batch addition of Q335 values: result[i] = a[i] + b[i], or result[i] = a[i] - lr × grad[i] for SGD.

**Inputs:** SRC_ADDR = parameter array base. PARAM_0/1/2 = learning rate as 384-bit value (loaded to V7 via three MOVHI/MOVI sequences). DST_ADDR = output array base. SRC_COUNT = parameter count.

**Algorithm per element:**
```
  LDVR V0, R0            ; load parameter a[i] (V and R)
  LDVR V1, R1            ; load gradient grad[i]
  WMUL V2, V7, V1        ; lr * grad → V2 (9 cycles), remainder in R2
  SHR335 V3, R3          ; Q335 divmod: V3 = quotient, R3 = remainder
  WSUB V4, V0, V3        ; a[i] - lr*grad[i] → V4
  STVR V4, R3            ; store result with remainder
```

**Estimated length:** 20 instructions per element. **Cycles per element:** approximately 15 (dominated by 9-cycle WMUL).

### 6.3 prog_dot_product

**Purpose:** Compute one row of QKᵀ attention matrix. Each element is a dot product of 384-bit Q335 values.

**Inputs:** SRC_ADDR = Q row base. PARAM_0 = K matrix base. PARAM_1 = hidden dimension H. DST_ADDR = output score.

**Algorithm:**
```
  LDI I0, 0              ; dimension index
  MOVI V6, 0             ; accumulator = 0
  MOVI R6, 0             ; remainder accumulator = 0
dim_loop:
  LDV V0, q_offset       ; load Q[row][dim]
  LDV V1, k_offset       ; load K[col][dim]
  WMUL V2, V0, V1        ; Q*K product (9 cycles)
  SHR335 V3, R3          ; divmod
  WADD V6, V6, V3        ; accumulate quotient
  WADD R6, R6, R3        ; accumulate remainder
  LDI I0, I0+1
  WCMP I0, PARAM_1       ; check if all dimensions done
  JLT dim_loop
  STV V6, result_offset  ; store dot product
  STR R6, result_offset  ; store remainder
  HALT
```

**Estimated length:** 35 instructions. **Cycles per dimension:** approximately 14 (dominated by WMUL). For H=64: approximately 896 cycles per dot product = 5.97 μs at 150 MHz.

### 6.4 prog_softmax_surr

**Purpose:** Compute SM2 quadratic surrogate softmax: s_i = (z_i - m + c)² / Σ(z_j - m + c)².

**Inputs:** SRC_ADDR = logit array. SRC_COUNT = number of logits. PARAM_0 = shift constant c. DST_ADDR = output probability array.

**Algorithm:**
```
Phase 1: Find max (sequential scan)
  LDV V0, logits[0]      ; max = first logit
  ; loop: WCMP each logit against max, update if greater

Phase 2: Compute squares (parallel across cores, each core handles a slice)
  ; For each logit in slice:
  WSUB V1, V_logit, V_max   ; z_i - m
  WADD V1, V1, V_c          ; z_i - m + c
  WMUL V2, V1, V1           ; (z_i - m + c)² (9 cycles)
  SHR335 V3, R3             ; divmod
  STV V3, output[i]         ; store numerator
  WADD V6, V6, V3           ; accumulate local sum

Phase 3: Global sum via reduction network
  REDUCE_ADD V7, V6         ; V7 = global sum of all squares (5 cycles)

Phase 4: Divide each by sum
  ; For each numerator in slice:
  ; Division by V7 requires iterative approach or reciprocal approximation
  ; Use Newton reciprocal: x_{n+1} = x_n(2 - V7*x_n)
  ; Or: ship numerators and sum to host for division (simpler, fast enough)
```

**Estimated length:** 30 instructions per phase. **Cycles for 100 logits across 10 cores:** Phase 1: ~200 (sequential). Phase 2: ~14 per logit × 10 per core = ~140. Phase 3: 5. Phase 4: host or ~30 per logit. Total: approximately 500 cycles = 3.3 μs.

### 6.5 prog_constraint_eval

**Purpose:** Evaluate a single Prolog constraint condition against the fact store. Each core evaluates one constraint from the active constraint set.

**Inputs:** SRC_ADDR = constraint batch (predicate ID + expected args). Constraint loaded to registers. Fact store scanned for matching facts.
