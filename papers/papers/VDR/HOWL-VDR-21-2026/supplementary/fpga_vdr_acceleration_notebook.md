# VDR-LLM-Prolog Hardware Acceleration Notebook

## Status and Context

The CKS-MATH-145/148 specifications describe an FPGA implementation for an earlier system called VFR (Value-Fragment-Remainder, using [V:i32, R:i8]) running Prolog verification and LLM inference on a Xilinx Zynq-7020. The CKS framework was invalidated — the math didn't compile, all papers in the series were falsified. However, the hardware architecture patterns are real engineering that was designed, resource-estimated, and timing-analyzed for a concrete FPGA target. The question is: what transfers to VDR-LLM-Prolog, what changes, and where does hardware acceleration actually help?

---

## 1. What Changed: VFR → VDR

### 1.1 The Type Widened

VFR used [V:i32, R:i8] — a 5-byte pair. The remainder was 8 bits, essentially a quantization residual. This was compact but limited: R could only hold a small correction factor, not arbitrary structure.

VDR uses [V:int, D:int, R:Any] where V and D are arbitrary-precision integers and R can be atomic (integer), composite (base + child VDR triples), or functional (callable). The remainder is not a byte — it's a recursive structure of unbounded depth carrying exact unresolved computation.

**Hardware implication:** VFR's fixed 5-byte format mapped directly to registers and BRAM — 38 entities at depth 48 fit in 9KB per core. VDR's arbitrary-precision integers and recursive remainder do not fit in fixed-width registers. A hardware VDR core needs either:

- A fixed working precision (i128 for V and D covers 99% of cases per VDR-11 ZM2, with BigInt overflow to software) and a depth-limited remainder tree stored in BRAM
- Or a hybrid where the ALU operates on fixed-width integers and remainder tree management is handled by a microcontroller or software layer

The Q335 frame simplifies this significantly. When operating in Q335 mode, V is a ~102-digit integer (~340 bits), D is fixed at 2^335 (never stored, implicit), and R nests one level per multiply via divmod. If we fix the working width at 384 bits (covering Q335 numerators with margin), the core becomes fixed-width again — wider than VFR but structurally similar.

### 1.2 The Denominator Is New

VFR had no denominator — it was integer-plus-small-remainder. VDR has D as a first-class component. But in Q335 mode, D is constant (2^335) and division by D is a right-shift by 335 bits. This means:

- Q335 addition: one 384-bit integer add
- Q335 multiplication: one 384-bit multiply, one 384-bit divmod (which is a right-shift + mask for power-of-two D), remainder goes to R
- Q335 division by integer k: one 384-bit divmod

The divmod-by-power-of-two is free in hardware — it's bit extraction. The multiply is the expensive operation, requiring a wide multiplier. A 384×384 multiply produces a 768-bit result. The top 384 bits (after shift) become V, the bottom 335 bits become R. This is exactly the nesting mechanism from VDR-13.

### 1.3 Prolog Terms Changed

VFR terms had types: atom, variable, number, list, vector2, rectangle, circle, entity, transform. These were game-domain types.

VDR-LLM-Prolog terms have types: atom, variable, vdr_fraction, integer, list, kb_ref, fact_ref, constraint_ref, connection_ref, path_ref. These are KB-structural types.

**Hardware implication:** The term type enum changes but the unification mechanism is the same — compare type tags, then compare values based on type. VDR fraction unification requires cross-multiplication (a.V × b.D == b.V × a.D), which is two wide multiplies and a compare. This is more expensive than VFR's i32 comparison but still deterministic and parallelizable.

---

## 2. What Transfers Directly

### 2.1 The Batch Processing Model

VFR processed entities in batches: load entity data from DDR3 to core BRAM, process, write results back. The batch dispatcher distributed work across 30 cores via an 11-state FSM with DMA coordination.

VDR-LLM-Prolog has the same pattern for several operations:

- **Fact queries across KBs:** load fact batches from DDR, match predicate IDs across cores in parallel, collect results
- **Constraint checking:** load constraint set, evaluate each constraint against KB state — independent per constraint, parallelizable
- **Softmax normalization:** compute exp (or surrogate) for each logit independently, then reduce — classic parallel map-reduce
- **Matrix operations:** row-parallel or tile-parallel matrix multiply for attention scores and feedforward layers

The batch dispatcher architecture (DMA load → distribute to cores → process → DMA store) transfers directly. The entity becomes a KB node or a batch of facts. The processing becomes predicate matching, constraint evaluation, or arithmetic.

### 2.2 The AXI Interface Pattern

Memory-mapped registers for control (start, poll status, read results) with DMA for bulk data transfer. This is standard SoC practice and transfers unchanged. The register map grows (more configuration for VDR operations) but the pattern is identical.

### 2.3 The Shared BRAM Pattern

Read-only lookup tables loaded once, read by all cores. VFR used this for Perlin tables, UtilityAI curves, and state machine data. VDR-LLM-Prolog uses it for:

- Q335 constant table (22 transcendental constants, each ~48 bytes at 384-bit width = ~1056 bytes)
- Twiddle factor tables for FFT (precomputed cos/sin as Q335 pairs)
- Predicate ID → fact batch address lookup table
- Grammar template structures (column types, enum value sets)

Same mechanism, different contents.

### 2.4 The Core Pipeline Structure

4-stage in-order pipeline: fetch → decode → execute → writeback. For VDR, the execute stage widens (384-bit ALU instead of 32-bit) and the instruction set changes, but the pipeline structure is sound. The VFR ISA had 6-bit opcodes with categories for arithmetic, bitwise, shift, VFR-specific, compare, load/store, batch, and transfer. The VDR ISA would have similar categories with different specific operations.

---

## 3. What Needs New Design

### 3.1 Wide Multiplier

The critical new hardware: a 384×384 bit multiplier producing a 768-bit result. Options:

**Option A: DSP48 cascade.** The Zynq-7020 has 220 DSP48E1 slices, each capable of 25×18 multiply. A 384-bit multiply requires tiling: 384/25 ≈ 16 tiles wide, 384/18 ≈ 22 tiles tall, with partial product accumulation. This consumes significant DSP resources but produces a result in a fixed number of cycles (pipelined).

**Option B: Iterative multiplier.** A 64-bit multiplier iterated 36 times (6×6 tiles of 64-bit products) with accumulation. Uses fewer DSPs but takes 36+ cycles per multiply. At 150MHz, that's 240ns per multiply — still fast enough for Q335 operations where multiplies are infrequent (one per divmod).

**Option C: Hybrid.** 128-bit multiplier (manageable in DSPs) iterated 9 times. Balances resource usage and latency. ~60ns per multiply at 150MHz.

For VDR-LLM-Prolog, Option C is likely optimal: Q335 multiplications aren't the bottleneck (they happen once per divmod, not per cycle), so trading latency for resource savings makes sense.

### 3.2 Remainder Tree Management

VFR had no recursive remainder. VDR does. A hardware core processing Q335 arithmetic needs to:

1. Perform divmod (multiply + shift + mask)
2. Store the remainder in a tree structure in BRAM
3. Track tree depth (counter, bounded by policy)
4. Optionally traverse the tree for scalar projection

**Design approach:** Each core has a remainder BRAM region (e.g., 4KB) organized as a flat array of VDR nodes: [V:384bits, D:384bits, R_index:16bits, depth:8bits]. R_index points to the child node in the same array (0 = no remainder = closed). Maximum depth bounded by policy (e.g., 16 levels as per VDR-8 scope chain limit). This gives each core capacity for 16 levels of nesting × ~96 bytes per node ≈ 1.5KB per active computation, fitting comfortably in BRAM.

### 3.3 Prolog Unification Engine

VFR's Prolog was simple: match predicate IDs (i16 comparison) and argument values (i32 comparison). VDR-LLM-Prolog unification requires:

- Atom comparison: string equality → integer comparison if using string interning (VDR-11 ZP2 specifies StringPool with integer handles for Zig). With interning, atom unification is i32 comparison — same as VFR
- Variable binding: same mechanism — bind on first match, check consistency on subsequent
- VDR fraction comparison: cross-multiplication. Two 384-bit multiplies + one 384-bit compare. Expensive but deterministic
- List unification: element-by-element recursive — handled by microcode loop, not single-cycle
- KB reference comparison: i32 comparison — same as VFR entity comparison

**Design approach:** A dedicated unification coprocessor per core (or shared across 4-8 cores) with a small instruction sequencer for recursive list/composite unification. Simple cases (atom, integer, KB ref) are single-cycle. VDR fraction comparison takes the multiply latency (e.g., 9 cycles for Option C multiplier). List unification is iterative.

### 3.4 LLM Inference Adaptation

VFR specified LLM inference as integer matrix multiply-accumulate on i32 weight batches. VDR-LLM-Prolog uses exact VDR fractions for weights, which changes the computation significantly:

**The honest assessment:** Full exact VDR arithmetic for LLM inference on FPGA is impractical at useful model sizes. A 100M parameter model at 384 bits per parameter is ~4.8GB — exceeding DDR3 on the Zynq-7020. The 384-bit multiply for every MAC operation would make inference orders of magnitude slower than quantized integer inference.

**The practical approach:** Use the FPGA for acceleration of specific VDR operations, not for full LLM inference. The LLM runs on a host processor (CPU/GPU) in exact VDR arithmetic (Python prototype or Zig port). The FPGA accelerates:

1. **Prolog evaluation** — batch fact matching, rule evaluation, constraint checking. This is the "verification" pass that VFR already implemented. Highly parallelizable across KB partitions
2. **Softmax computation** — the surrogate softmax (SM2: quadratic kernel) is pure integer arithmetic: square, sum, divide. Perfect for parallel hardware
3. **Q335 batch operations** — bulk addition of Q335 constants (used in QED coefficient computation, FFT twiddle generation). Each is one wide integer add — embarrassingly parallel
4. **Matrix operations on small exact matrices** — exact determinant, inverse, solve for matrices up to ~50×50 (the Gaussian elimination from VDR-13 GS1-GS7). Each row operation is independent after pivot selection
5. **Attention score computation** — the QKᵀ matrix multiply for exact attention. This is the most compute-intensive LLM operation and benefits most from parallelism
6. **Denominator management** — batch budget checking and reprojection. Each parameter checked independently — embarrassingly parallel

---

## 4. Parallelism Analysis

### 4.1 Embarrassingly Parallel (No Dependencies Between Units)

| Operation | Data Unit | Independence | Cores Useful | Notes |
|-----------|-----------|-------------|-------------|-------|
| Q335 addition (bulk) | Pair of numerators | Complete | All | One wide add per core per cycle |
| Constraint checking | Individual constraint | Complete | All | Each constraint evaluated independently |
| Softmax surrogate | Individual logit | Complete (map phase) | All | Square and sum independently; reduce at end |
| Denominator budget check | Individual parameter | Complete | All | Compare denom bits against budget |
| Q335 reprojection | Individual parameter | Complete | All | Round + compute error bound |
| Fact query by predicate | KB partition | Complete across partitions | All | Each core searches its partition |
| Bitset operations | Individual bits | Complete | All | Set/test/count parallelizable |

### 4.2 Parallel with Reduction

| Operation | Parallel Phase | Reduction Phase | Notes |
|-----------|---------------|----------------|-------|
| Softmax normalization | Compute each term | Sum all terms, divide each | Map-reduce pattern |
| Matrix-vector multiply | Each row independently | Collect results | Row-parallel |
| Dot product | Partial products | Sum partials | Tree reduction |
| Determinant (Gaussian) | Row operations within step | Pivot selection between steps | Step-sequential, within-step parallel |
| List aggregates (sum, product, mean) | Partial aggregates | Combine | Tree reduction |

### 4.3 Sequential (Limited Parallelism)

| Operation | Why Sequential | Acceleration Strategy |
|-----------|---------------|----------------------|
| Prolog backtracking | Each binding depends on previous | Pipeline different queries; parallelize across independent goals |
| Newton iteration | Each step depends on previous | Accelerate each step's arithmetic |
| Remainder tree traversal | Parent-child dependency | Depth-first hardware walker |
| Scope chain resolution | Walk parent pointers | Short chain (max 16); pipeline with prefetch |
| Training step (forward+backward) | Layer dependencies | Layer-parallel where possible; pipeline across batches |

---

## 5. Proposed VDR FPGA Architecture

### 5.1 Core Design: VDR-Q335 Arithmetic Core

```
VDR_CORE (one of N):
├── Instruction memory (BRAM, 4KB)
├── Register file
│   ├── 8 × 384-bit V registers
│   ├── 8 × 384-bit R registers  
│   ├── 4 × 16-bit index registers (KB addressing)
│   └── Flags: EQ, LT, GT, OV, DONE, CLOSED
├── ALU (384-bit)
│   ├── ADD/SUB: 384-bit ripple/carry-select
│   ├── MUL: 128-bit iterative (9 cycles for 384×384)
│   ├── SHIFT: barrel shifter (for divmod by 2^335)
│   ├── CMP: 384-bit compare
│   └── DIVMOD: shift + mask (for power-of-two D)
├── Remainder BRAM (2KB)
│   ├── 16 nodes × [V:384, D:384, R_idx:16, depth:8]
│   └── Free-list pointer
├── Unification unit
│   ├── Atom compare (i32)
│   ├── Cross-multiply (2 × MUL + CMP for VDR fractions)
│   └── List walker (microcode sequencer)
└── Batch interface
    ├── DMA read port
    ├── DMA write port
    └── Batch control registers (F, count, depth, index)
```

### 5.2 Resource Estimate per Core

| Component | LUTs | FFs | BRAM (18Kb) | DSP48 |
|-----------|------|-----|-------------|-------|
| 384-bit ALU (add/sub/cmp) | 800 | 400 | 0 | 0 |
| 128-bit iterative multiplier | 300 | 600 | 0 | 8 |
| Barrel shifter (384-bit) | 400 | 0 | 0 | 0 |
| Register file (8×384 V + 8×384 R) | 200 | 6144 | 2 | 0 |
| Remainder BRAM | 50 | 20 | 1 | 0 |
| Instruction BRAM | 50 | 20 | 2 | 0 |
| Unification unit | 400 | 200 | 0 | 2 |
| Control/pipeline | 300 | 300 | 0 | 0 |
| **Per core total** | **2500** | **7684** | **5** | **10** |

### 5.3 System Scaling

| Platform | LUTs | DSP48 | BRAM | Max Cores | Notes |
|----------|------|-------|------|-----------|-------|
| Zynq-7020 | 53,200 | 220 | 140 | 12 | LUT-limited (need ~10K for infra) |
| Zynq-7045 | 218,600 | 900 | 545 | 60 | Comfortable fit |
| Zynq-7100 | 444,000 | 2020 | 1090 | 120 | DSP-limited |
| UltraScale+ ZU7EV | 504,000 | 1728 | 1080 | 130 | Production target |
| UltraScale+ ZU19EG | 1,143,000 | 1968 | 1968 | 200+ | High-end |

### 5.4 Dispatcher Adaptation

The VFR batch dispatcher FSM transfers with modifications:

- **S_IDLE:** Same — wait for go signal
- **S_CALC_CHUNKS:** Changed — chunks are now KB partitions or parameter blocks, not entity ranges
- **S_DMA_LOAD:** Changed — loads 384-bit values instead of 5-byte VFR pairs; burst width adapts
- **S_DMA_LOAD_WAIT:** Same pattern, wider data
- **S_START_CORES:** Same — assert start for all cores with data
- **S_WAIT_CORES:** Same — poll done bits
- **S_DMA_STORE:** Changed — writes 384-bit results; for Prolog queries, writes matching fact indices
- **S_DMA_STORE_WAIT:** Same
- **S_NEXT_CHUNK:** Same
- **S_DONE:** Same

### 5.5 ISA for VDR Cores

| Range | Category | Opcodes | Notes |
|-------|----------|---------|-------|
| 0x00 | Control | HALT, NOP | Same as VFR |
| 0x01-0x07 | Jump | JMP, JEQ, JLT, JGT, JOV, JCLOSED, JDONE | JCLOSED is new (test if R=0) |
| 0x08-0x0E | Wide Arith | WADD, WSUB, WMUL, WDIVMOD, WABS, WNEG, WCMP | 384-bit operations |
| 0x10-0x13 | Bitwise | AND, OR, XOR, NOT | 384-bit |
| 0x18-0x1D | Shift | SHR, SHL, SHR335, SHL335, SHRN, SHLN | SHR335 = Q335 divmod |
| 0x20-0x25 | VDR | NEST (create R child), UNNEST (pop R), DEPTH (read depth), PROJECT (scalar Π), NORMALIZE, CROSS_MUL (for unification) | New: remainder tree ops |
| 0x28-0x2B | Unify | UATOM, UFRAC, ULIST_START, ULIST_NEXT | Unification micro-ops |
| 0x30-0x37 | Load/Store | LDV, LDR, STV, STR, LDVR, STVR, LDBATCH, STBATCH | Wider loads for 384-bit |
| 0x38-0x3B | Batch | BLOAD, BNEXT, BADDR, BMATCH | BMATCH = predicate match |
| 0x3C-0x3F | Transfer | TSEND, TRECV, TWAIT, TDONE | Inter-core communication |

---

## 6. Acceleration Priorities

Ordered by impact on VDR-LLM-Prolog system performance:

### Priority 1: Prolog Fact Matching (Highest Impact)

**Why:** Every KB query scans facts by predicate. With 50,000 facts (VDR-11 ME6 large deployment), linear scan is the bottleneck. VDR-11 specifies hash indexing for Zig, but hardware parallel scan is faster.

**How:** Each core loads a partition of the fact table. BMATCH instruction compares predicate ID (i16) against target. Matching facts flagged. Results collected via reduction.

**Speedup:** N cores scan simultaneously. 12 cores on Zynq-7020 → 12× speedup over sequential scan. 120 cores on Zynq-7100 → 120×.

**Integration:** Zig host issues "query predicate P with args" via AXI registers. FPGA scans, returns matching fact indices via DMA. Host retrieves actual facts from DDR.

### Priority 2: Q335 Batch Arithmetic (High Impact)

**Why:** Training involves bulk parameter updates (SGD: W ← W - lr×grad). Each update is a Q335 subtraction. With millions of parameters, this dominates training time.

**How:** Each core processes a slice of the parameter vector. WADD/WSUB on 384-bit values. DMA streams parameters through cores.

**Speedup:** Linear with core count. Each core handles 384-bit add in 1-2 cycles.

**Integration:** Host prepares parameter and gradient vectors in DDR. FPGA processes batch update. Host reads back updated parameters.

### Priority 3: Attention Score Computation (High Impact for Inference)

**Why:** QKᵀ is the most compute-intensive operation in transformer inference. For exact VDR, each element is a dot product of exact fractions — multiple wide multiplies and adds.

**How:** Row-parallel: each core computes one row of the attention matrix. Within each row, iterative dot product using WMUL and WADD.

**Speedup:** For a sequence length of S and hidden dimension H, the attention matrix is S×S requiring S×H multiplies per row. With N cores processing N rows simultaneously, speedup is min(N, S).

**Integration:** Host loads Q, K matrices to DDR. FPGA computes score matrix. Host applies softmax (could also be FPGA-accelerated) and value mixing.

### Priority 4: Constraint Batch Checking (Medium Impact)

**Why:** At every normalization point (softmax output, weight update), constraints must be checked. With 15+ constraints per lifecycle phase, this adds latency to every step.

**How:** Each core evaluates one constraint against the current state. Constraints are Prolog conditions — the unification unit handles evaluation.

**Speedup:** Number of constraints × evaluation time → single evaluation time (all parallel).

### Priority 5: Denominator Budget Sweep (Medium Impact)

**Why:** Periodic budget checks across all parameters. Each check is independent: read denom bits, compare against budget.

**How:** Each core processes a slice of parameters. WDENOM instruction extracts bit width. Compare against budget register. Flag violations.

**Speedup:** Linear with core count.

### Priority 6: Grammar-Directed Parsing (Lower Impact, High Value)

**Why:** Parsing compacted input through grammar rules is pattern matching on typed fields — similar to Prolog fact matching.

**How:** Grammar rules loaded to shared BRAM. Input stream distributed to cores. Each core matches rules against input segments.

**Speedup:** Depends on grammar complexity; typically modest (grammars are small) but constant-time per input token.

---

## 7. Integration Architecture

### 7.1 Host + FPGA Division

```
HOST (CPU, running Zig VDR-LLM-Prolog):
├── LLM forward/backward pass (exact VDR arithmetic)
├── Orchestrated inference loop (assess/formalize/execute/store)
├── KB tree management (create/delete/scope/mount)
├── Session management (snapshot/clone/kill)
├── Grammar system (parse/generate/match)
└── Command token parsing and dispatch

FPGA (VDR acceleration):
├── Prolog fact matching (parallel scan)
├── Q335 batch arithmetic (parameter updates)
├── Attention score computation (row-parallel)
├── Constraint batch checking (parallel evaluation)
├── Denominator budget sweep (parallel check)
├── Softmax surrogate (parallel map-reduce)
└── Unification engine (for complex Prolog queries)
```

### 7.2 Communication Protocol

1. Host writes operation type to CONTROL register
2. Host writes data addresses (DDR pointers) to configuration registers
3. Host writes GO bit
4. FPGA dispatcher loads data via DMA, distributes to cores
5. Cores process in parallel
6. Results written back via DMA
7. FPGA sets DONE flag
8. Host reads results

For latency-sensitive operations (single Prolog query during inference loop), a fast-path register interface bypasses DMA: host writes query predicate and args directly to registers, FPGA returns match count and first match in registers. No DMA overhead for small queries.

### 7.3 Memory Map

```
0x0000_0000 - 0x1FFF_FFFF: DDR3 (512MB)
  0x0000_0000: KB fact store (partitioned for parallel access)
  0x0800_0000: Parameter storage (Q335 format)
  0x1000_0000: Gradient storage
  0x1800_0000: Attention matrices
  0x1C00_0000: Working buffers

0x4000_0000 - 0x4000_00FF: FPGA control registers (AXI-Lite)
0x4001_0000 - 0x4001_FFFF: FPGA shared BRAM (AXI-Lite)
```

---

## 8. What Does NOT Belong on FPGA

### 8.1 Remainder Tree Deep Operations

Remainder trees beyond depth 4-5 are rare in practice (Q335 multiply chains stay shallow by design). Deep tree operations (full scalar projection through 16+ levels) are complex recursive traversals better handled in software.

### 8.2 Functional Remainder Resolution

fn_resolve calls a function at a declared depth. The function could be Newton iteration, Taylor series, or arbitrary composition. These are inherently sequential (each iteration depends on the previous) and involve variable-length computation. Software handles these.

### 8.3 KB Tree Structure Management

Creating, deleting, mounting, and scoping KBs involves pointer management, hash table updates, and complex state transitions. This is control-plane work, not data-plane work. Software handles this.

### 8.4 Grammar Matching and Scoring

Grammar scoring involves Prolog pattern matching (could be FPGA-accelerated) but also LLM assessment for the "best-when" relevance component (10% of score). The scoring is inherently mixed deterministic/probabilistic. Keep in software unless profiling shows it's a bottleneck.

### 8.5 Session Snapshot/Restore

Deep-copying live state across KBs is memory management. Arena allocators in Zig (VDR-11 ZP4) handle this efficiently in software.

---

## 9. Development Path

### Phase 1: Prolog Accelerator (Weeks 1-8)

Build the minimum useful accelerator: parallel fact matching.

- Port VFR core to VDR-width (384-bit ALU) — reuse pipeline structure
- Implement BMATCH instruction for predicate ID matching
- Implement batch dispatcher for fact partitions
- Test with VDR-11 Stage 1 KB (5 KBs, 50 facts) → Stage 2 (15 KBs, 200 facts)
- Zig host interface via AXI registers

**Deliverable:** Prolog queries on FPGA returning matching fact indices to Zig host.

### Phase 2: Q335 Arithmetic (Weeks 9-14)

Add wide arithmetic for Q335 operations.

- Implement 128-bit iterative multiplier
- Implement WADD, WSUB, WMUL, WDIVMOD, SHR335
- Implement batch parameter update pipeline
- Test with VDR-4 training step (single exact SGD step on FPGA)

**Deliverable:** Batch Q335 parameter updates on FPGA.

### Phase 3: Attention Acceleration (Weeks 15-20)

Add row-parallel attention score computation.

- Implement dot product accumulation across 384-bit values
- Implement row-parallel QKᵀ computation
- Implement softmax surrogate (SM2 quadratic kernel) in hardware
- Test with VDR-4 TinyTransformerLM forward pass

**Deliverable:** Exact attention scores computed on FPGA, softmax on FPGA, rest on host.

### Phase 4: Unification Engine (Weeks 21-26)

Add hardware Prolog unification for complex queries.

- Implement atom, integer, VDR fraction unification in hardware
- Implement variable binding table in BRAM
- Implement micro-sequencer for multi-goal rule evaluation
- Test with VDR-9 inference notebook Prolog queries

**Deliverable:** Complete Prolog query evaluation on FPGA for common patterns.

### Phase 5: Integration and Profiling (Weeks 27-32)

Full integration with VDR-LLM-Prolog Zig host.

- Profile end-to-end: which operations are FPGA-bound, which are host-bound
- Optimize DMA transfer patterns (double-buffering, prefetch)
- Test with VDR-11 Stage 4 full lifecycle pipeline
- Measure speedup versus pure-software Zig implementation

**Deliverable:** Benchmarked VDR-LLM-Prolog system with FPGA acceleration.

---

## 10. Key Design Decisions to Make

| Decision | Options | Recommendation | Rationale |
|----------|---------|---------------|-----------|
| Working width | 256 / 384 / 512 bits | 384 | Covers Q335 (~340 bits) with margin; 512 wastes resources |
| Multiplier style | Full-width / 128-bit iterative / 64-bit iterative | 128-bit iterative | 9 cycles per multiply; balances resources and latency |
| Cores per Zynq-7020 | 8 / 10 / 12 | 10 | Leaves ~20% LUT margin for infrastructure and timing |
| Remainder depth limit | 8 / 16 / 32 | 16 | Matches VDR-8 scope chain limit; sufficient for training |
| Prolog on FPGA scope | Fact matching only / Full unification / Full rule evaluation | Fact matching first, full unification Phase 4 | Incremental; fact matching gives most speedup with least complexity |
| Host interface | Register-only / DMA-only / Hybrid | Hybrid | Registers for small queries; DMA for bulk operations |
| Target board for development | Zybo Z7-20 / ZCU104 / Custom | Zybo Z7-20 | Cheapest; proves concept; scale to larger FPGAs later |

---

## 11. What This Enables

A VDR-LLM-Prolog system with FPGA acceleration doesn't change the architecture — it accelerates the data-plane operations while the control plane stays in software.

The host Zig system runs the orchestrated inference loop, manages KBs, handles sessions, parses commands, and runs the LLM. When it needs to query facts, update parameters, compute attention scores, or check constraints, it dispatches to the FPGA, which returns exact results in parallel.

The invariants are preserved: every operation is exact integer arithmetic, every result has provenance, every constraint is checked, and no floats appear anywhere. The FPGA just does the integer arithmetic faster by doing more of it simultaneously.

The system specification (VDR-1 through VDR-14) doesn't change. The implementation blueprint (VDR-11) doesn't change. The IOSE declarations don't change. The builtins don't change. A subset of builtins get a hardware-accelerated implementation path that produces identical results to the software path — verifiable by running both and comparing, which is how FPGA designs are validated anyway.
