# VDR-LLM-Prolog: Functional Remainder Hardware
## Adaptive Precision Through Structural Information in Silicon

**Registry:** [@HOWL-VDR-23-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → ... → [@HOWL-VDR-14-2026] → ... → [@HOWL-VDR-21-2026] → [@HOWL-VDR-22-2026] → [@HOWL-VDR-23-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** May 2026

**Domain:** Computer Architecture / Adaptive Precision Arithmetic

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

---

## Abstract

The VDR arithmetic system represents every value as a triple [Value, Denominator, Remainder] where the Remainder slot can hold a callable function that produces exact rational values at any requested depth. This functional remainder mechanism — specified in [@HOWL-VDR-1-2026] and used throughout the system for transcendental evaluation — has implications for hardware that prior papers in the series did not explore. On the VDR-22 integer-native ASIC [@HOWL-VDR-22-2026], each Q335 Integer Unit already contains a 384-bit ALU with 1-2 cycle multiply and free power-of-two division via fixed wiring. This paper specifies a Functional Remainder Unit (FRU) that extends each QIU to evaluate functional remainders — Taylor recurrences, Newton iterations, and series summations — in hardware using the existing ALU, without round-tripping to the host processor. The FRU adds approximately 500,000 transistors per QIU (3.4% die area increase across 5,120 units) and enables three capabilities that the base VDR-22 chip cannot provide: hardware-native exact exponential softmax at competitive latency with float implementations (25-40 nanoseconds for 1,024 logits versus host-bound milliseconds without the FRU), continuous per-step remainder resolution during training that replaces periodic Q-basis reprojection stalls with microsecond-level maintenance, and complete Prolog unification over active VDR values carrying nonzero remainders. At single-query scale, the FRU does not change wall-clock latency — the language model forward pass at approximately 30 microseconds per command token dominates primitive execution at 1-100 nanoseconds by 300-30,000×. At datacenter scale with millions of concurrent sessions, the FRU eliminates host round-trips for remainder resolution, keeping the entire rule-driven execution path on the data-plane chip and removing the serialization bottleneck that would otherwise limit throughput as accumulated Prolog rules handle an increasing fraction of work autonomously. The paper specifies the FRU microarchitecture, traces the full inference chain with adaptive precision, analyzes the datacenter throughput implications, and identifies the boundary between what the FRU changes (capability and throughput at scale) and what it does not (single-query latency).

---

## 1. The Remainder Slot as Precision Control Surface

The VDR triple [V, D, R] has been the foundation of this system since its first specification. V and D are integers forming a rational fraction. R carries exact unresolved structure — the portion of a computation's result that the current denominator frame could not absorb. R is the only slot that nests, the only slot that recurses, and the only slot that carries active computational state.

When R is zero, the triple is closed — it behaves as the rational number V/D. Arithmetic on closed triples is standard rational arithmetic, and the Q335 fixed frame (D = 2^335) makes this efficient: addition is one integer add, multiplication is one integer multiply followed by bit extraction at position 335, and the bit extraction is free in hardware because it is fixed wiring.

When R is nonzero, the triple is active — it carries information beyond what the Q335 frame absorbed. R can take three forms: an atomic integer, a composite structure (integer base plus child VDR triples), or a functional remainder — a callable function that produces an exact VDR triple at any requested depth.

The functional remainder is where the VDR system differs most fundamentally from every other arithmetic system. A float value has no concept of "what precision I could achieve if asked." It has a fixed mantissa width and rounding error that is unknown and unrecoverable. An arbitrary-precision rational has exact precision but no mechanism for deferred computation — the value is either computed or it is not. A VDR functional remainder carries a recipe for computing exact rational values to arbitrary depth, where each depth produces a complete exact value (not an approximation converging to a limit), and the choice of depth is a runtime decision.

Square root of 2 via Newton iteration: each depth doubles the number of correct digits. Depth 8 gives over 100 digits. Exponential via Taylor series: each additional term refines the exact rational partial sum. Sine, cosine, logarithm — all expressible as functional remainders producing exact rationals at any requested depth. The convergence rates vary (Newton is quadratic, Taylor for exp is super-geometric, Taylor for ln is geometric) but the mechanism is uniform: call the function with a depth parameter, receive an exact rational.

On the VDR-22 ASIC without functional remainder hardware, when a computation produces an active value with a functional remainder in the R slot, the QIU stores the remainder metadata in its 4KB SRAM and either carries it forward as unevaluated metadata or signals the host processor to resolve it in software. For the Q335 workloads specified in VDR-22 — batch arithmetic, attention scores, fact matching — this rarely matters. The Q335 frame provides 100 digits of precision, and typical computations produce closed results. The expected active spill rate is below 1%.

The question this paper addresses is what happens when the hardware can evaluate functional remainders natively, without host involvement. Not because the base chip lacks adequate precision — Q335's 100 digits exceed any practical need. But because the functional remainder is a structural information channel that the hardware can act on, and acting on it enables capabilities the base chip cannot provide.

---

## 2. What the FRU Is

### 2.1 Architecture

The Functional Remainder Unit is a small sequencer attached to each QIU that drives the QIU's existing ALU through a recurrence loop. It does not contain its own multiplier or adder. It reuses the QIU's 384-bit carry-select adder (1 cycle) and 384-bit parallel multiplier (1-2 cycles). What it adds is the control logic to execute iterative computations — Taylor term recurrences, Newton iterations, and convergent series — as hardware-managed loops rather than host-orchestrated instruction sequences.

The FRU contains four components.

A recurrence register file holds four 384-bit values: the current term in the series or iteration, the accumulated sum or iterate, the input value x, and a divisor or scaling factor. These are dedicated registers separate from the QIU's general register file, avoiding contention when the FRU operates concurrently with the QIU's normal instruction stream.

A small-integer reciprocal table stores the reciprocals of integers 1 through 64 as Q335 values. This table occupies 64 × 48 bytes = 3,072 bytes in dedicated SRAM. Its purpose is to replace Q335 division-by-k (which would require a full divmod operation) with Q335 multiplication-by-reciprocal (1-2 cycles using the existing multiplier). For Taylor series, each term involves division by the term index k: term_k = term_{k-1} × x / k. The reciprocal table turns this into two multiplies: term_{k-1} × x, then × reciprocal[k].

A convergence comparator is a single 384-bit magnitude comparison (identical to the QIU's existing WCMP instruction) that checks whether the current term is below a configurable precision threshold stored in a dedicated threshold register. This determines when the FRU stops iterating — when the next term's contribution would not change the result at the required precision level.

A loop controller is an 8-bit counter, a function tag decoder (reading the function type from the R slot's flags field), and a depth limit register. The function tag identifies which recurrence to execute (exp, sqrt, log, sin, cos, or generic series). The depth limit caps the maximum number of iterations regardless of convergence. The total loop controller logic is approximately 2,000 transistors.

### 2.2 Resource Cost

| Component | Transistors | Area at 4nm (mm²) |
|-----------|-------------|-------------------|
| Recurrence registers (4 × 384-bit) | 36,864 | 0.0003 |
| Reciprocal table (3 KB SRAM) | 147,456 | 0.0012 |
| Convergence comparator | 50,000 | 0.0004 |
| Loop controller + tag decoder | 2,000 | <0.0001 |
| Interconnect to QIU ALU | ~260,000 | 0.0021 |
| **Per-FRU total** | **~496,320** | **~0.004** |
| **5,120 FRUs (full chip)** | **~2.54B** | **~20.5** |

The FRU increases the per-QIU transistor count from approximately 7.1M to approximately 7.6M — a 7% increase per unit. At the full-chip level, the increase is from 68B to 70.5B transistors, and from 581 mm² to 601 mm² die area. This is a 3.4% area increase.

### 2.3 New Instruction

The FRU adds one instruction to the VDR-22 ISA:

| Opcode | Mnemonic | Format | Cycles | Description |
|--------|----------|--------|--------|-------------|
| 0x35 | FEVAL | R | Variable | Evaluate functional remainder in R slot to depth specified in Id register, using function tag from R flags |

FEVAL reads the function tag from the active remainder's flags field, loads the input value x from the remainder's V field into the FRU's recurrence registers, and executes the corresponding recurrence loop using the QIU's ALU. When the loop terminates (convergence threshold met or depth limit reached), the FRU writes the accumulated result back to the destination V register and the residual remainder (if any) back to the destination R register.

The instruction is variable-latency because different functions require different numbers of iterations and each function's iteration count depends on the input value and depth parameter. The QIU pipeline stalls during FEVAL execution, the same way it stalls during WMUL. No other instruction issues until the FEVAL completes.

### 2.4 Recurrence Patterns

The FRU supports six function tags, each corresponding to a specific recurrence:

| Tag | Function | Recurrence | Cycles per Term | Depth for 100 Digits |
|-----|----------|-----------|-----------------|---------------------|
| 0x01 | exp(x) | term_k = term_{k-1} × x × reciprocal[k] | 3-4 (2 muls + 1 add) | ~45 |
| 0x02 | sqrt(a) | x_{n+1} = (x_n + a × reciprocal_of(x_n)) × reciprocal[2] | ~4 (1 mul + 1 reciprocal mul + 1 add + 1 shift) | ~8 |
| 0x03 | ln(1+x) | term_k = -term_{k-1} × x; sum += term_k × reciprocal[k] | 3-4 (1 mul + 1 reciprocal mul + 1 add) | ~340 at x=1; ~33 with argument reduction |
| 0x04 | sin(x) | term_k = -term_{k-1} × x² × reciprocal[2k] × reciprocal[2k+1] | 5-6 (3 muls + 1 add + sign) | ~45 |
| 0x05 | cos(x) | term_k = -term_{k-1} × x² × reciprocal[2k-1] × reciprocal[2k] | 5-6 (3 muls + 1 add + sign) | ~45 |
| 0x06 | generic | term_k = f(term_{k-1}, x, k) via microcode in instruction BRAM | Variable | Variable |

The generic tag (0x06) reads a short microcode sequence from the QIU's instruction BRAM that defines the recurrence step. This enables Borwein acceleration for zeta, hypergeometric series for elliptic integrals, and any other convergent computation expressible as a fixed-step recurrence. The microcode is loaded by the batch dispatcher alongside the main microprogram.

---

## 3. Adaptive Precision in the Inference Chain

The functional remainder gives every value in the system a precision dial. The FRU gives the hardware the ability to turn that dial. This section traces what this means through the transformer inference path — not as a fixed pipeline, but as operations the language model may select through command tokens, executed by primitives on the QIU array.

### 3.1 The Common Path: R = 0

For the vast majority of Q335 operations in a transformer forward pass, the Remainder is zero. Multiplication of two Q335 values produces a 768-bit product; SHR335 extracts the quotient (bits above 335) and remainder (bits below 335). When the remainder bits are all zero — which happens whenever the product's lower 335 bits are zero — the result is closed. No nesting, no FRU involvement, no overhead.

The expected closed rate depends on the values being multiplied. For Q335 constant arithmetic (π + e, 3×ζ(3)), the rate is effectively 100% for addition and varies for multiplication. For trained model parameters, which start as small rationals and accumulate through gradient updates, the closed rate is above 99% at typical denominator growth levels.

On the common path, the VDR-22 + FRU chip behaves identically to the base VDR-22. The FRU adds zero overhead for closed values. The convergence comparator checks the CLOSED flag in 1 cycle as part of the normal pipeline — the same check the base chip already performs via the JCLOSED instruction.

### 3.2 Attention Score Computation

The language model may emit command tokens requesting Q × Kᵀ computation for attention. This is a matrix of dot products, each involving d_k multiplications and additions.

Each Q335 multiplication in the dot product produces a quotient and a remainder. The QIU checks whether the remainder is zero (1 cycle). If zero, the QIU accumulates the quotient into the running sum and continues. If nonzero, the QIU has a decision point — and this is where adaptive precision operates.

For attention scores that will feed into softmax, the absolute precision of each score matters less than the relative ordering. A remainder of magnitude 2^(-100) on a score of magnitude 2^(10) is irrelevant to the ranking. The convergence comparator checks the remainder magnitude against a context-dependent threshold. For attention score intermediates, the threshold is set to the minimum score difference that would change the softmax ranking — a value the host configures before the computation based on the model's characteristics.

When the remainder is below threshold, the QIU discards it and continues with the closed quotient. No SRAM allocation, no nesting overhead. When the remainder exceeds threshold — rare for well-conditioned attention — the QIU stores it in remainder SRAM and the FEVAL instruction is available if downstream operations need the additional precision.

The result: attention scores computed at full Q335 throughput (1-2 cycle multiply, free divmod) with per-value precision certificates. Each score carries either a zero remainder (exact within the Q335 frame) or a stored remainder with known magnitude (exact within a quantified bound). No float system provides this information.

### 3.3 Softmax: Surrogate and Exact Exponential

The VDR system specifies five softmax implementations (VDR-14 Appendix E). The two most relevant for hardware are the rational surrogate (SM2: quadratic kernel, zero transcendentals) and the truncated Taylor exponential (SM1: exact rational partial sums).

**Rational surrogate on VDR-22 + FRU:** unchanged from the base chip. Each output = (z_i − max + c)² / Σ(z_j − max + c)². Two multiplies (square and normalization) plus a reduction for the denominator sum. Approximately 20 cycles per row of 1,024 logits across 5,120 QIUs. At 2 GHz: approximately 10 nanoseconds. The FRU is not involved. This remains the lowest-latency path and produces exact sum-to-one with zero transcendentals.

**Exact exponential softmax on VDR-22 + FRU:** this is the new capability. Each logit passes through the FRU's exp recurrence. The FRU evaluates Taylor terms until the convergence comparator determines sufficient precision for the softmax context.

The adaptive depth per element is the key property. After subtracting the row maximum, shifted logits range from 0 to large negative values. The FRU handles each case differently:

Shifted logit of 0: exp(0) = 1 exactly. The FRU recognizes the zero input and returns 1 in 1 cycle. No iteration.

Shifted logit of -1: the Taylor series converges quickly. The FRU evaluates approximately 6 terms at 3-4 cycles each: approximately 20 cycles.

Shifted logit of -5: approximately 12 terms: approximately 45 cycles.

Shifted logit of -10: approximately 18 terms: approximately 70 cycles.

Shifted logit of -20: this value contributes negligibly to the softmax sum. The FRU evaluates 4-5 terms, confirms the contribution is below the ranking threshold, and stops. Approximately 16 cycles. The remainder carries a functional remainder recording exactly what precision was achieved.

Float hardware computes the same polynomial approximation for every logit regardless of its magnitude. The FRU does less work for values that need less precision and more work for values that need more, directed by the structural information in the remainder.

After all exp evaluations complete, the QIU array performs a global reduction (7 cycles for the exact sum across all QIUs), computes the reciprocal of the sum via FRU Newton iteration (8 iterations × 4 cycles = 32 cycles, computed once and broadcast), and multiplies each exp value by the reciprocal (1-2 cycles per element).

Total latency for exact exp-softmax over 1,024 logits: the critical path is the longest single exp evaluation (approximately 70 cycles for the most negative shifted logit) plus the reduction (7 cycles) plus the reciprocal (32 cycles) plus normalization (2 cycles). Approximately 111 cycles at 2 GHz: approximately 56 nanoseconds. This is competitive with float exp-softmax on current GPUs (100-200 nanoseconds on H100 including warp divergence from the special function unit), and the result sums to exactly 1/1.

The language model does not choose between surrogate and exact exp-softmax at the instruction level. Both are primitives in the 448-builtin vocabulary (B116 vdr_softmax_surrogate and B115 vdr_softmax). The LLM emits a command token for whichever the orchestration logic selects. The QIU array executes whichever it receives. The FRU enables the exact exp path to execute natively rather than falling back to software.

### 3.4 Feedforward and Activation

Linear transforms (matrix multiply) follow the same pattern as attention: Q335 multiplication with per-value remainder checking, FRU available for resolution when needed, threshold filtering for intermediates.

ReLU activation is the simplest operation in the chain: compare the value to zero, output the value if positive, output zero if negative. This is one cycle on the QIU comparator. The FRU is relevant only in the edge case where V = 0 and the sign depends on the remainder. The QIU checks: V > 0? Output V with R. V < 0? Output zero. V = 0? The FEVAL instruction resolves one level of the remainder tree to determine the sign. Expected frequency of the V = 0 case: below 0.01% of values. The FRU adds exact ReLU behavior at the decision boundary at negligible average cost.

Rational scaling (the VDR replacement for layer normalization) requires computing the mean absolute value and dividing each element by it. The mean absolute value is a reduction (exact sum via the reduction network, 7 cycles) followed by division by the element count (exact, since the count is an integer). The reciprocal of the mean absolute value is computed by the FRU via Newton iteration: 8 iterations at 4 cycles each = 32 cycles, computed once and broadcast to all elements. Each element is then multiplied by the reciprocal: 1-2 cycles. Total: approximately 40 cycles for the normalization, less than 20 nanoseconds. No square root. No approximation. Exact.

### 3.5 What Adaptive Precision Is Not

Adaptive precision via the FRU is not mixed-precision training as practiced in float systems. Float mixed-precision selects a precision level (FP16, FP32, BF16) per tensor or per operation, statically, based on empirically determined heuristics about which layers tolerate lower precision. The selection is coarse-grained (entire tensors), predetermined (before training begins), and uninformed (the system does not know how much precision was lost at any point).

FRU adaptive precision operates per value, per operation, dynamically, directed by exact structural information that each value carries. The granularity is individual scalar values. The timing is runtime, after each operation produces its result. The information source is the remainder itself — a precise description of what the Q335 frame did not absorb. The decision (resolve further or accept current precision) is a 1-cycle hardware comparison of known quantities, not a heuristic.

The FRU does not make VDR approximate. Every value at every point is exact: V/D plus the structural information in R. The FRU determines whether to evaluate the structural information further based on what the next operation requires. The value does not become more or less exact — it is always exact. The question is whether the evaluated precision is sufficient for the current computational context.

---

## 4. Training with Continuous Remainder Resolution

### 4.1 The Remainder Accumulation Problem

During training, each parameter undergoes repeated multiply-accumulate operations: gradient computation (chain rule through the computation graph) and parameter updates (SGD: W ← W − lr × grad). Each multiplication potentially produces a nonzero remainder. Over hundreds of training steps, remainders can accumulate — each step's remainder nesting on top of the previous step's.

On the base VDR-22 without FRUs, remainder accumulation is managed by periodic Q-basis reprojection: when a parameter's denominator exceeds the declared budget, the system rounds the value to the nearest Q335 representable value, records the exact error bound, and resets the remainder to zero. This is the mechanism specified in VDR-14 (B136 vdr_reproject_qbasis). Reprojection is correct — the error bound is exact and recorded — but it is a full-tensor operation that must process every parameter. For a 10-million parameter model, reprojection costs milliseconds when it triggers.

VDR-4 observed that denominators grow from approximately 2^10 at initialization to approximately 2^45 after thousands of steps. The Q335 frame at 2^335 provides 290 orders of magnitude of headroom. Reprojection triggers are infrequent. But when they do trigger, the stall is noticeable — a millisecond-scale pause in an otherwise microsecond-per-step training loop.

### 4.2 FRU Continuous Resolution

With FRUs, the remainder from each multiplication can be resolved immediately — in the same pipeline cycle sequence as the multiplication itself. After WMUL produces a 768-bit result and SHR335 extracts quotient and remainder, the QIU checks whether the remainder is nonzero. If nonzero, FEVAL resolves it: the FRU evaluates the remainder value against the Q335 frame and either determines it is negligible (below the precision threshold, discard) or folds it back into the quotient as an exact correction.

The folding operation is a Q335 addition of the resolved remainder contribution to the quotient: 1 additional cycle. The total cost of a Q335 multiply with continuous remainder resolution is: 1-2 cycles (multiply) + 0 cycles (SHR335) + 1 cycle (check) + 0-2 cycles (resolve if nonzero) = 2-5 cycles. At the expected spill rate below 1%, the average cost is approximately 2.02 cycles — negligibly more than the base multiply.

The result: remainder nesting never accumulates. Each multiply's remainder is resolved inline. The parameter denominators stay within the Q335 frame indefinitely. Q-basis reprojection never triggers because there is nothing to reproject. Training throughput is smooth — no periodic stalls, no full-tensor sweeps, no checkpoint-dependent performance variation.

For 10 million parameters across 5,120 QIUs at approximately 2 cycles per multiply: 10M × 2 / 5,120 = approximately 3,906 cycles per training step for the forward pass multiplications. At 2 GHz: approximately 2 microseconds. With continuous remainder resolution adding approximately 0.02 cycles per multiply on average: approximately 39 additional cycles total, approximately 20 nanoseconds. The remainder resolution cost is below measurement noise.

### 4.3 Exact Gradient Information at Truncation Boundaries

When the FRU truncates a functional remainder evaluation at a chosen depth (because the convergence comparator determined sufficient precision), the residual remainder is itself a functional remainder — it carries the recipe for computing additional precision on demand. For inference, this additional precision is never needed. For training, it contains exact information about the gradient at the truncation boundary.

The gradient of a truncated Taylor series with respect to its input is the truncated derivative series — also a functional remainder, also exact at every depth. The FRU's truncation does not introduce gradient error in the way that float rounding introduces gradient error. The truncation boundary is a precise, inspectable, reproducible computational decision, and the gradient through that boundary is exactly computable. This is a property no float system can provide: exact gradients through precision boundaries.

Whether this property has practical consequences for training dynamics at scale is an open empirical question — one that can only be investigated with exact arithmetic, which is the point.

---

## 5. Prolog Unification Over Active Values

### 5.1 The Completeness Problem

Prolog unification of two VDR fractions tests equality by cross-multiplication: a/b = c/d if and only if a × d = c × b. On the base VDR-22, the CROSS_MUL instruction handles this in 2-3 cycles for closed values (R = 0 on both sides). For active values (R ≠ 0 on either side), the cross-multiplication of the V/D components may produce equal products even when the full values (including remainders) differ, or unequal products when the full values are actually equal after remainder resolution.

Without FRUs, active-value unification falls back to the host: the host resolves both remainders in software, producing closed values, then the QIU performs CROSS_MUL on the closed results. This is correct but requires a host round-trip per unification involving active values.

### 5.2 FRU-Enabled Active Unification

With FRUs, the QIU can resolve active values inline. When CROSS_MUL detects that one or both operands are active (checking the CLOSED flag), it triggers FEVAL on each active operand to resolve the remainder to the current precision threshold. The resolved values are then cross-multiplied. If the cross-products are equal, the fractions are equal to the resolved precision. If unequal, the fractions are definitively unequal (the difference exceeds the resolved remainder).

The edge case — cross-products equal but remainders might distinguish the values at greater depth — is handled by the convergence comparator. If the remainder magnitudes after resolution are below the threshold where their contribution could change the cross-product comparison, the equality is definitive. If not, the FRU resolves one additional depth level and retries. In practice, Q335 precision (100 digits) makes this edge case vanishingly rare — two values would need to agree to 100 digits and differ only in the 101st for the edge case to activate.

The result: Prolog unification is complete over the entire VDR value space, not just the closed subspace. Constraint evaluation (does the sum of these probabilities equal exactly 1?), fact matching (does this metric value match the threshold?), and rule firing (does this condition hold?) all work correctly on active values without host involvement.

### 5.3 Impact on the Accumulation Curve

The VDR-19 SRE accumulation curve shows that by investigation 50, 115 Prolog rules auto-fire and 88% of routine work is automated. Each rule firing involves fact matching and unification — comparing stored facts against rule head patterns. If any fact or pattern contains an active VDR value (a measurement with a remainder from sensor conversion, a computed statistic with a remainder from aggregation), the unification must handle active values.

Without FRUs, each active-value unification during rule evaluation requires a host round-trip. At investigation 50 with 115 rules firing, this could mean dozens of host round-trips per investigation — individually fast (microseconds each) but collectively creating control-plane contention at scale.

With FRUs, every rule evaluation completes entirely on the QIU array. The rules fire, facts are matched, active values are resolved inline, and the evaluation result is available without crossing the host-device boundary. The rule-driven execution path stays entirely in the data plane.

---

## 6. Single-Query Performance Analysis

At single-query scale, the FRU does not change wall-clock latency for any VDR-LLM-Prolog workload. This section explains why, with specific numbers.

### 6.1 The Bottleneck Ratio

The language model forward pass generates approximately 8 tokens per command token. For a 1-billion parameter model at Q335 on the VDR-22 chip, with approximately 50 tokens of active context (state is in knowledge bases, not the context window), each forward pass takes approximately 30 microseconds.

Primitive execution takes 1-100 nanoseconds depending on the operation: fact query across 200 facts at 10 nanoseconds, Q335 multiply at 1 nanosecond, softmax over 100 logits at 10 nanoseconds, dot product for H=64 at 32 nanoseconds.

The ratio: each command token costs 30,000 nanoseconds of LLM forward pass and 1-100 nanoseconds of primitive execution. The primitives are 300-30,000× faster than the LLM's decision to invoke them.

### 6.2 FRU Impact on Single-Query

Without FRU, a primitive involving remainder resolution round-trips to the host: add approximately 1-10 microseconds per host round-trip. This is still 3-30× faster than the LLM forward pass. The host round-trip is invisible at single-query scale.

With FRU, the same operation completes in 10-100 nanoseconds on the QIU. This is faster than the host round-trip by 10-100×. But since both are faster than the LLM forward pass, the improvement is invisible to the user. The investigation that takes 23 milliseconds of LLM time with the base chip takes 23 milliseconds with the FRU chip.

### 6.3 Where Single-Query FRU Value Exists

The FRU's value at single-query scale is not latency. It is capability.

Without FRUs, some computations fall back to software: exact exp-softmax, exact logarithm for cross-entropy loss, exact square root for distance computations, and remainder resolution for active-value Prolog unification. These software fallbacks work correctly but require the host CPU to participate in the data path. The system is functionally complete but architecturally impure — the data plane cannot execute all primitives independently.

With FRUs, every primitive in the 448-builtin vocabulary executes natively on the QIU array. The host CPU manages orchestration (the control plane) and never touches the data path. This is architectural completeness: the silicon can execute everything the specification defines.

Whether this architectural completeness matters at single-query scale is debatable. What it enables at scale is not.

---

## 7. Datacenter-Scale Throughput Analysis

At datacenter scale with millions of concurrent sessions, the FRU's elimination of host round-trips changes the throughput ceiling.

### 7.1 The Serialization Problem Without FRU

The VDR-19 accumulation curve shows that mature systems handle 93% of work through automated Prolog rule evaluation without LLM involvement. Each rule evaluation is a chain of primitive calls — fact matching, unification, arithmetic operations, constraint checks — executing on the QIU array.

Without FRUs, when a rule-driven primitive chain encounters a functional remainder that needs resolution (a transcendental evaluation, an active-value comparison, a remainder that affects the computation outcome), the chain pauses. The QIU signals the host. The host resolves the remainder in software. The host returns the result. The chain resumes.

At single-query scale, this round-trip is invisible — microseconds against a 30-millisecond investigation. At millions of concurrent sessions, each generating hundreds of rule-driven primitive chains per second, the host CPU becomes a serialization point. Millions of round-trips per second compete for host CPU cycles, host memory bandwidth, and host-device communication bandwidth.

### 7.2 The Data-Plane Solution With FRU

With FRUs, the rule-driven execution path never leaves the QIU array. The FEVAL instruction resolves any functional remainder inline. Prolog unification over active values completes on-chip. Transcendental evaluations for constraint checking complete on-chip. The entire rule evaluation — from fact match through unification through arithmetic through constraint check through result storage — executes as a continuous stream of QIU instructions with no host involvement.

The host CPU handles only LLM forward passes (for the 7% of work requiring LLM judgment), KB tree management (creating and scoping knowledge bases), session orchestration (snapshots, clones), and command token parsing. The data plane is self-sufficient for all numeric computation including transcendentals and remainder resolution.

### 7.3 Throughput Projections

One VDR-22 + FRU chip at 2 GHz with 5,120 QIUs:

| Workload | Compute Limit | Memory Limit (4.9 TB/s) | Effective Throughput |
|----------|-------------|------------------------|---------------------|
| Rule evaluations (100 ops each) | 51B/sec | 24.5B/sec (at 200 B/fact) | ~24B/sec (memory-bound) |
| SRE investigations (1,500 ops each) | 3.4B/sec | 16.3B/sec | ~3.4B/sec (compute-bound) |
| Concurrent sessions with 93% automation | — | — | See below |

For concurrent sessions with 93% rule automation: each session generates approximately 55 LLM tokens (7% of 769) requiring LLM forward passes, plus approximately 500 rule-driven primitive operations (the 93% handled by accumulated rules). The LLM tokens are the bottleneck per session — 55 forward passes at 30 microseconds each = 1.65 milliseconds of LLM time per investigation. The 500 rule-driven operations at approximately 2 nanoseconds average = 1 microsecond total primitive time. The LLM dominates by 1,650×.

But the LLM forward passes and the rule-driven primitives execute on different hardware. The LLM cluster generates command tokens. The QIU chip executes rule-driven chains independently. At 1,000 concurrent sessions, the QIU chip is at approximately 0.001% utilization for rule-driven work. At 1,000,000 concurrent sessions, the QIU chip is at approximately 1% utilization.

The QIU chip reaches meaningful utilization only when the LLM cluster is large enough to generate millions of concurrent investigation streams. At that scale, one QIU chip serves the rule-driven primitive work for approximately 3 million concurrent investigations per second. The limiting factor is HBM bandwidth for KB fact access, not compute for arithmetic or remainder resolution.

### 7.4 LLM Cluster Reduction

The accumulation curve's deepest economic impact at datacenter scale is reducing the LLM cluster size. Without rule accumulation, every command in every investigation requires an LLM forward pass. With 93% rule automation, only 7% of commands require LLM involvement.

For a datacenter serving 10 million investigations per hour: without accumulation, the LLM cluster processes approximately 2.14 billion command tokens per hour (769 per investigation × 2.78M/hour). With 93% accumulation, the LLM cluster processes approximately 150 million command tokens per hour. The LLM cluster is 14× smaller for the same throughput.

The QIU chip handles the rule-driven 93% at negligible compute cost relative to its capacity. The FRU ensures this 93% executes entirely on-chip without host serialization. The economic result: the expensive resource (LLM compute) shrinks by 14×, the inexpensive resource (QIU compute) absorbs the difference, and the system gets cheaper as rules accumulate further.

---

## 8. Exp-Softmax vs Surrogate: An Engineering Choice, Not a Forced Compromise

Previous papers in this series presented the rational surrogate softmax as the primary path and the truncated Taylor exponential as an alternative with tradeoffs. With FRU hardware, the tradeoff profile changes enough that both are viable first-class options.

### 8.1 Comparison on VDR-22 + FRU

| Property | Surrogate (SM2) | Exact Exp (SM1 + FRU) |
|----------|----------------|---------------------|
| Transcendentals | None | Taylor exp via FRU |
| Sum-to-one | Exact (1/1) | Exact (1/1) |
| Monotonicity | Yes | Yes |
| Equal logits → equal outputs | Yes (1/n each) | Yes (1/n each) |
| Gradient shape | Quadratic landscape | Exponential landscape |
| Latency (1,024 logits, VDR-22 + FRU) | ~10 ns | ~56 ns |
| FRU required | No | Yes |
| Adaptive depth | N/A | Yes — less work for well-separated logits |
| Per-value precision information | No (closed computation) | Yes (R slot carries truncation metadata) |
| Empirical training validation | Validated at toy scale (VDR-4) | Not validated at scale |

### 8.2 When Each Is Appropriate

The surrogate is faster, simpler, and validated. For inference where latency matters and the softmax is not the focus of investigation, the surrogate is the correct choice. It requires no FRU hardware and produces exact results.

The exact exponential is appropriate when the gradient landscape matters — specifically, when investigating whether training instabilities are artifacts of approximate softmax gradients. VDR-4 identified this as future work item FW4: "with exact gradients and updates, determine if training instabilities are arithmetic artifacts or algorithmic." The exact exponential with FRU hardware makes this investigation feasible at model scales large enough to exhibit the instabilities in question.

The language model does not need to understand this distinction. Both are primitives in the vocabulary. The orchestration logic (human-configured or rule-driven) selects the appropriate softmax variant based on the context — training investigation versus inference deployment.

---

## 9. Updated Chip Specifications

| Property | VDR-22 Base | VDR-22 + FRU | Change |
|----------|------------|-------------|--------|
| Transistors | 68B | 70.5B | +3.7% |
| Die area | 581 mm² | 601 mm² | +3.4% |
| TDP | 400 W | 410 W | +2.5% |
| Q335 closed arithmetic throughput | 5.1T muls/sec | 5.1T muls/sec | Unchanged |
| Q335 add throughput | 10.2T adds/sec | 10.2T adds/sec | Unchanged |
| SHR335 (free divmod) | 0 gates, 0 power | 0 gates, 0 power | Unchanged |
| exp(x) depth 10 | Host-bound (~μs) | ~640M evals/sec (~25 cycles) | Native |
| exp(x) depth 45 (100 digits) | Host-bound (~ms) | ~36M evals/sec (~180 cycles) | Native |
| sqrt(x) 100 digits | Host-bound | ~1.6B evals/sec (~32 cycles) | Native |
| ln(x) with argument reduction | Host-bound | ~480M evals/sec (~130 cycles) | Native |
| sin(x)/cos(x) depth 45 | Host-bound | ~28M evals/sec (~225 cycles) | Native |
| Softmax surrogate (1,024 logits) | ~10 ns | ~10 ns | Unchanged |
| Softmax exact exp (1,024 logits) | Host-bound | ~56 ns | Native |
| Prolog unification (active values) | Host-bound | ~4-8 cycles on-chip | Native |
| Remainder resolution (per value) | Host-bound | ~2-5 cycles on-chip | Native |
| Training reprojection stalls | Periodic (~ms) | Eliminated (continuous ~ns) | Continuous |

---

## 10. Limitations and Honest Boundaries

The FRU does not change the single-query latency of any VDR-LLM-Prolog investigation. The LLM forward pass dominates primitive execution by 300-30,000× and the FRU makes the already-negligible primitive time marginally more negligible. Users of single-query systems will observe no performance difference between VDR-22 and VDR-22 + FRU.

The FRU's adaptive depth is controlled by a precision threshold that must be configured correctly for each computational context. A threshold set too aggressively (too large) causes the FRU to discard remainders that affect downstream results. A threshold set too conservatively (too small) causes the FRU to evaluate more terms than necessary. The system specification provides default thresholds per operation type (softmax, training update, constraint evaluation), but domain-specific workloads may require tuning. This is analogous to learning rate tuning in conventional training — a configuration decision, not a fundamental limitation.

The FRU's reciprocal table covers integers 1 through 64. Taylor series for functions like log(1+x) at x near 1 converge slowly — approximately 340 terms for 100 digits. The reciprocal table does not cover term indices above 64, meaning terms 65-340 require a different approach (computing the reciprocal via Newton iteration in the FRU, adding approximately 32 cycles per term). With argument reduction (reducing x to a small value before applying the series), the number of terms drops to approximately 33, well within the table's range. Argument reduction is not performed by the FRU — it is a host-orchestrated preprocessing step. For applications requiring log evaluation of arbitrary arguments, the host must preprocess.

The generic function tag (0x06) reads microcode from the QIU's instruction BRAM. The instruction BRAM capacity is 4KB (512 instructions at 32 bits each). Complex recurrences requiring more than approximately 50 instructions per step may exceed the available microcode space when combined with the main microprogram. This limits the complexity of custom functional remainder evaluations to relatively simple recurrences. Borwein acceleration for zeta (the most complex functional remainder in the VDR specification) fits within this budget. More complex functions may require multi-pass evaluation orchestrated by the host.

The FRU adds 3.4% die area and approximately 2.5% TDP. These are small but nonzero costs paid by every QIU regardless of whether it executes FEVAL instructions. For workloads that never encounter functional remainders (pure closed Q335 arithmetic with no transcendental evaluation), the FRU is unused silicon. The cost is mitigated by the small absolute area (0.004 mm² per QIU) and the fact that the FRU's recurrence registers provide additional temporary storage that the QIU can use for non-FRU purposes if desired.

The FRU does not make VDR-LLM-Prolog practical for production-scale language model training. The memory constraint identified in VDR-22 (96 GB HBM3 limiting model size to tens of millions of parameters for exact training) is unchanged. The FRU improves training smoothness (eliminating reprojection stalls) but does not change the fundamental memory-capacity limitation.

---

## 11. The Architectural Thesis in Silicon

The VDR-1 paper stated: "The remainder is not error. It is not residue. It is not what's left over after rounding. It is a first-class operational rule that tells the system what to do next with what remains unresolved in the current denominator frame."

Every subsequent paper in the series applied this principle to a different domain: knowledge bases, Prolog, grammar systems, safety, alignment, performance, deployment, self-extension. The principle remained the same: the remainder carries structural information, and systems that can read and act on structural information outperform systems that discard it.

The FRU is this principle expressed in transistors. The remainder SRAM stores the structural information. The convergence comparator reads it. The recurrence register file acts on it. The loop controller determines when sufficient action has been taken. The QIU's existing ALU does the actual computation. The result is a value that is always exact, with precision determined dynamically by what the computation requires, directed by information the value itself carries.

Float hardware rounds and discards. The information about what was lost is unrecoverable. VDR hardware rounds and remembers. The FRU can recover the information when the computation needs it. This is not a difference of degree — faster rounding or more bits of precision. It is a difference of kind — a value that knows what it does not yet know, and hardware that can compute the answer on demand.

The common path (R = 0, closed, exact within Q335) runs at full throughput with zero FRU overhead. The uncommon path (R ≠ 0, structural information available) runs at near-full throughput with the FRU resolving what's needed in 2-32 cycles depending on the function and depth. The hardware never does unnecessary work because the remainder tells it what is necessary. The hardware always does sufficient work because the remainder tells it what is sufficient.

This is what adaptive precision means in an exact arithmetic system. Not "choose FP16 or FP32." Not "quantize to INT8." Not "mixed precision with loss-scaling heuristics." Per-value, per-operation, hardware-determined precision, directed by exact structural information, producing exact results with known and recoverable residuals. The FRU is a 3.4% area investment that makes this operational.

---

## Links

[@HOWL-VDR-1-2026] VDR Arithmetic: Value, Denominator, Remainder. Exact Finite Arithmetic in Irreducible Triple Form. DOI: 10.5281/zenodo.15302702

[@HOWL-VDR-4-2026] Exact-Fraction Language Model Architecture. From Arithmetic Library to Working Transformer in 24 Modules.

[@HOWL-VDR-13-2026] VDR in Physical Computation. Exact Arithmetic Where It Matters.

[@HOWL-VDR-14-2026] VDR-LLM-Prolog. A Complete System Specification for Exact Arithmetic Language Models with Structural Provenance. DOI: 10.5281/zenodo.20232194

[@HOWL-VDR-18-2026] VDR-LLM-Prolog: Performance. Integer Arithmetic on GPU Hardware.

[@HOWL-VDR-21-2026] VDR-LLM-Prolog on FPGA. Exact Integer Arithmetic in Custom Silicon: A 10-Core Q335 Processor on Zynq-7020.

[@HOWL-VDR-22-2026] VDR-LLM-Prolog on Dedicated Silicon. From FPGA Proof-of-Concept to Integer-Native GPU Architecture.

---

