**VDR-14 Plan: "You Are Here" — Complete System Specification**

**Purpose:** A single document that tells a new reader what this system is, why it exists, how every piece fits together, and where to go for depth. No prior knowledge required. References previous papers but never depends on having read them.

**Audience:** An engineer who will build this system, or an evaluator deciding whether it's worth building.

**Document character:** Specification (components, concepts, builtins, constraints, boundaries, claims).

**Organizing principle:** Staircase. Each section builds on the one before it. No forward references. A reader who stops at any section has a complete understanding up to that level.

---

**Section 1: The Problem**

What's wrong with current LLMs. Three deficiencies: values without provenance (computation is opaque float tensor chain, no way to tell correct from hallucinated), approximate arithmetic (every number is 16/32-bit float, every operation silently truncates, platform-dependent rounding makes runs non-reproducible), stateless conversation (no structured memory, no scoped variables, facts from different topics mixed in flat token sequence, context window overflow). Brief, concrete, no VDR concepts yet. The reader understands what we're solving before we introduce any solution.

*References: VDR-5 TD1-TD3*

---

**Section 2: The Arithmetic Foundation — VDR**

What VDR is mechanically. The triple [V, D, R]. V is an integer, D is a nonzero integer, R is the remainder — the exact unresolved structure that every other system discards. Closed objects (R=0) behave as rationals. Active objects (R≠0) carry structure. Remainder is not error — it's part of the value.

How operations work. Divmod splits results into what the current D-frame holds (V) and what it doesn't (R). Denominator never grows because overflow nests into R. Depth replaces denominator growth. The Q335 mechanism — 22 transcendental constants as integers over 2³³⁵, addition is one integer add, multiplication is divmod with exact remainder nesting, 100-digit precision floor.

Functional remainders — functions in R producing exact rationals at chosen depth. Newton √2 doubling digits per step. Taylor series for exp, sin, cos, ln. Each depth is a complete exact value, not an approximation.

What this means: no floats, no drift, no silent truncation. Every value is integers. Every operation is exact. Decimals are import/export format, never used in computation.

Proof: 507 tests across 23 mathematical domains (number theory, polynomial algebra, matrix decomposition, cryptography, quantum mechanics, signal processing, control theory, wavelets, algebraic topology, game theory, coding theory, etc.), zero VDR computation errors. All 11 failures traced to wrong test expectations.

*References: VDR-1 (core arithmetic), VDR-2 (15-domain gym), VDR-3 (8 more domains + Q335), VDR-13 (physical computation + 40 builtins + complex/FFT/modular)*

---

**Section 3: Exact LLM Components**

Every component of a language model expressed in exact VDR arithmetic. The complete path: tokenization → embedding lookup → attention scores (exact matrix multiply) → causal masking → softmax (truncated Taylor or rational surrogate, sum exactly 1) → value mixing → residual addition → feedforward (Linear → ReLU → Linear) → logits → loss → exact gradients (reverse-mode autodiff) → exact optimizer update (SGD/momentum) → exact checkpoint (zero precision loss on save/load).

Architecture adaptations for VDR: ReLU not GELU (piecewise linear, no erf), rational scaling not LayerNorm (no sqrt), learned embeddings not sinusoidal (no sin/cos), no dropout, single exact precision.

Denominator management during training: growth pattern from ~2¹⁰ at init to ~2⁴⁵ plateau, Q-basis reprojection when budget exceeded with exact error bound logged. The key distinction: float silently truncates at every step, VDR reprojection is a declared auditable precision decision.

Proof: 198 tests, 196 passed, 2 test-expectation errors, zero VDR computation errors. Attention weights sum to exactly 1. Every intermediate value is an inspectable fraction. Bit-identical reproducibility across platforms.

*References: VDR-4 (complete LLM path), VDR-7 (lifecycle and denominator management)*

---

**Section 4: The Knowledge Base Tree**

Everything is a KB. A KB is a fat struct with 26 fields: identity (name, path, integer ID), persistent (facts, rules, constraints, connections, grammars), live (working data, LRUs, counters, locks, queues, stacks, ring buffers, bitsets), structural (parent ID, children IDs, mounts), metadata (visibility, frozen, owner, timestamps).

The tree structure. Every KB has a parent. Every KB has children. The entire system — data sources, corpora, models, checkpoints, training logs, feedback, evaluations, deployments, monitoring, user accounts, conversations, inference notebooks — is one tree of KBs addressable by integer.

Dotted paths for humans, integer IDs for machines. `root.models.v3.checkpoint_5000` is the human form. `[0][12][47][203]` is the machine form. Resolution happens once per turn, cached, all operations use integers. Two-integer addressing (kb_id + slot_id) for O(1) access to any data primitive anywhere.

Scoped knowledge. Active topic determines which subtree is in scope. Out-of-scope KBs are invisible, not deprioritized. "Bob" in conversation 1 is integer address `[0][conv][1][chars][3]`. "Bob" in conversation 2 is `[0][conv][2][chars][7]`. Different integers, no ambiguity possible.

Constraints inside the KB they govern. Inherit through the tree. Child overrides parent. Four domains: axiom (can't suspend), operational, legal, project. Because arithmetic is exact, constraint checking is exact — sum-to-one is 1/1 or it isn't.

Connections between KBs. Typed, directed, integer-addressed. 19 standard relationship types covering the full lifecycle. Graph primitives operate on connections for topology queries.

Mounts for cross-branch references. Four modes: read-only, read-write, snapshot, mirror. Cycle detection before creation.

Safety is the tree, not the LLM. User access determined by position in KB tree and visibility levels (public, internal, owner_only). The LLM doesn't decide what's safe — the tree structure decides. KB data surfaced directly from the KB bypasses LLM token generation — cannot be hallucinated because it's retrieved, not generated.

Grammars as KB field. Persistent, inheritable, self-describing. The KB knows how to present itself. Grammars parse input and generate output — same structure, both directions. Auto-generated extraction, display, and usage grammars. LLM creates new grammars by asserting facts.

*References: VDR-5 (Prolog + scoped KBs + constraints + topics), VDR-8 (data primitives + dotted paths + sessions), VDR-12 (grammars + compaction)*

---

**Section 5: The Prolog Engine**

Logic as struct data. Terms: atoms (string equality), variables (?-prefix, bind on match), VDR fractions (cross-multiplication comparison), integers, lists, KB references. Facts: predicate + typed args + provenance (source KB, assertion turn, derivation chain). Rules: head :- body. Depth-first search with backtracking, depth limit 100.

Unification uses exact VDR comparison. fraction(1,2) unifies with fraction(2,4) because 1×4 == 2×2. No tolerance, no epsilon.

Prolog compositions as new builtins. A rule chaining existing builtins IS a new operation. Assertable at any scope — root for permanent, session for temporary, project for project-scoped. IOSE properties derivable from composed parts. The system extends itself through use without new code or retraining.

Operational principles encoded as ~176 Prolog terms (15 axioms, ~80 facts, ~60 rules, 21 constraints) at root.system.oso, always in scope. Knowability spectrum, 90/9/0.9 priorities, data primacy, idempotency, one canonical method — all queryable and enforceable.

*References: VDR-5 (Prolog engine spec), VDR-10 (operational principles as Prolog)*

---

**Section 6: Primitives and Command Tokens**

448 builtins across 25 categories. Two classes: pure (404 — no side effects, no grant required, same inputs always produce same outputs, bounded termination) and operational (44 — side effects, positive credential grant required, every execution logged).

Pure primitives cover: text (17), collections (36), sets (14), mappings (15), VDR arithmetic (8 closed + 5 active + 3 structure), comparison (10), rounding/extraction (7), number theory (13), list aggregates (8), linear algebra (24), statistics/probability (16), conversion (14), time (10), identity/hashing (8), graphs (13), logic/control (11), integer fast path + bit ops (21), Q-basis (7), functional remainder (8), discrete calculus (6), polynomial (8), finite field (4), Markov (3), graph math (2), denominator management (5), data primitive operations (53), path/mount (17), session (8).

Operational primitives cover: filesystem (15), compilation (4), execution (5), linting (8), network (5), process management (7). All grant-gated with default denial.

The grant system. A grant is a structured object: operation class, allowed operations, location, issuer, expiration, max uses. Default is denial. No grant, no execution. Grants follow the KB hierarchy. Every use logged.

Command tokens. The LLM's output contains text tokens (rendered as conversation) and command tokens (executed by primitives). A command token is roughly 8 tokens — primitive name from known vocabulary + dotted path references to data. Data stays in the KB, never serialized through the token stream. The LLM selects from ~300 known names and points at known paths. Low-entropy reference selection, not high-entropy syntax generation.

The scratchpad. Internal ring buffer for LLM intermediate computation. Primitives and KB queries without surfacing in user output. Owner can inspect.

IOSE model. Every component declares inputs, outputs, side effects, and properties. Declarations are contracts — they're the test spec, the Zig interface contract, and the documentation. Validated before execution (type compatibility, side effect preview) and after (contract verification).

*References: VDR-6 (primitives + grants + command tokens + environments), VDR-8 (data primitives + paths + sessions), VDR-10 (IOSE + operational principles + numeric builtins), VDR-13 notebook (40 additional builtins for transcendentals/complex/FFT)*

---

**Section 7: Sessions and Drift Management**

Live state versus persistent state. Persistent: facts, rules, constraints, connections, grammars — survives reset, always present. Live: data primitives, scratchpad, working data, active scope — cleared by reset, captured by snapshot.

Session snapshots. Capture all live state atomically. Small (10KB-500KB) because they capture state not knowledge. Restore is atomic. Reset clears live to defaults, persistent untouched.

Disposable clones. Build to verified stable state → snapshot → run disposable workers from snapshot → monitor drift constraints (max turns < 200, context saturation < 90%, denominator drift < 2⁴⁸, error rate < 5%) → kill on drift → launch fresh from same frozen baseline. The snapshot never degrades. Work committed via KB_ASSERT survives. Drift dies with the clone.

The system improves over conversation length instead of degrading. Every fact asserted is permanent. Every connection is traversable. Every grammar is reusable. Every prior result is integer-addressable. Current LLMs degrade. This system accumulates.

*References: VDR-8 (session management + disposable clones)*

---

**Section 8: Orchestrated Inference**

The LLM does not reason — it orchestrates tools that compute and deduce. Token prediction produces orchestration decisions. Deterministic tools produce computation and deduction. The KB records everything.

The loop. Assess (LLM reads state, decides next step) → Formalize (LLM translates step into executable form — Prolog rule, Python script, primitive chain) → Execute (tools run it — Prolog evaluates, Python runs sandboxed, primitives compute) → Store (result into KB with provenance) → Assess again.

Termination: goal satisfaction (Prolog query succeeds), budget exhaustion (counter reaches limit), stall detection (no new evidence for 5 iterations), user intervention.

Backtracking via VDR-8 stack (investigation path) and LRU (attempted approaches with failure reasons). Branching spawns child notebooks with allocated budget.

Four inference modes. Deductive (premises + rules → conclusions, confidence = min of premise confidences). Inductive (observations → ranked hypotheses, confidence = coverage × mean source confidences). Abductive (observation → most likely cause, confidence = explained fraction × min evidence confidences). Analogical (known domain → unfamiliar domain, confidence = analogy strength × source confidence). Modes compose naturally because they operate on the same KB with the same tools.

Confidence as exact VDR fractions. Source confidences: exact VDR computation 1/1, Prolog derivation 1/1, database 98/100, live metrics 95/100, Python script 95/100, REST API 85/100, user-stated 70/100, web search 50/100, LLM-generated 30/100. Propagation rules computed by arithmetic primitives, not LLM judgment.

Inference notebooks. KB subtree with declared schema housing one inference process. Uses existing KB struct. Step queue, investigation stack, findings LRU, budget counters, evidence bitset, metric ring buffer. Templates for common investigation types.

No new primitives, struct fields, or modules. VDR-9 specifies patterns of use over existing capabilities. If the underlying layers are valid, patterns over them are valid by construction.

*References: VDR-9 (orchestrated inference)*

---

**Section 9: Grammar-Directed Compaction**

The compaction problem. Raw prose wastes context. A 300-word concept description compresses to one table row (~40 words, 87% compression) preserving every named concept, relationship, and claim. Across 13 papers: ~150k words → ~26k tokens, ~83% compression.

The grammar solution. Structural tokens (pipes, headers, ID prefixes, enum values) provided by grammars for free with 100% correctness. The LLM generates only content tokens — definitions, descriptions, rationale. Roughly 50% of compacted output is grammar-providable, 35% requires LLM judgment.

Grammars are bidirectional. The same grammar that generates a table row parses one. Output and input use the same structure. Grammar-matched input gives the LLM discrete typed data instead of raw text to interpret.

Self-describing KBs. A KB with grammars knows its own data (facts), logic (rules), constraints, connections, and presentation. Everything about a KB lives inside the KB.

Column types with VDR integration. Fraction columns convert losslessly to VDR. Integer columns promote losslessly. Categorical columns constrain to declared enums. The type system constrains both generation and parsing.

20 standard table schemas, 6 compaction profiles, 12 source character types, 10-step pipeline (5 deterministic, 2 LLM judgment, 3 hybrid).

Data as dicts. A table row is a dict with keys from column headers. Full primitive treatment — filter, sort, map, reduce. Stored as JSON/JSONB for persistence. Grammar defines schema, schema generates struct, struct validates data, data stored as dicts in KB, addressable by integer path.

Proof: 178/179 tests pass. Roundtrip fidelity verified — compacted doc → KB → compacted doc preserves all tables, rows, relationships exactly.

*References: VDR-12 (grammar-directed compaction + universal compaction system)*

---

**Section 10: The Complete Lifecycle**

12 phases, all KB operations: data sourcing → corpus preparation → tokenization → model initialization → pre-training → fine-tuning → human feedback → evaluation → deployment → monitoring → updates → retirement.

Every phase produces KBs that feed the next. The entire lifecycle from raw data to retired model is one queryable tree. Lineage queries span the whole lifecycle: what data influenced this deployment, what feedback changed this model.

Canary deployment with exact thresholds. Latency < baseline × 11/10, compared as exact fraction. Auto-rollback on criterion violation. All decisions logged as KB facts.

UI as API to KB layer. Every UI component is a KB query. Every UI action is a command token. Same grants govern both. One system.

*References: VDR-7 (lifecycle specification)*

---

**Section 11: Physical Computation Domains**

14 physical domains demonstrated exact: QED coefficients, quantum mechanics, signal processing, control systems, orbital mechanics, structural mechanics, thermodynamics, crystallography, geodesy, optics, DFT/FFT, IIR filters, transfer functions, state-space evolution.

12 float failure points where VDR produces zero error. 10 conservation laws verified by exact equality. Complex numbers as VDR pairs. FFT as integer butterflies with depth ≤ 10 for N=1024. Modular arithmetic as remainder structure.

40 additional builtins for transcendentals, complex arithmetic, FFT, SLERP, quaternions, modular operations, dynamics, wavelets, lazy computation.

*References: VDR-13 (physical computation), VDR-13 notebook (Q335 nesting + builtins + 35 gym exercises)*

---

**Section 12: Implementation Blueprint**

5 stages, each producing a complete testable system.

Stage 1 — Toy Full Lifecycle: 24 modules, ~150 builtins, ~2800 lines, 150 tests. KBs, facts, Prolog rules, exact arithmetic, data primitives, toy lifecycle loop.

Stage 2 — Upgraded Toy: 37 cumulative modules, ~300 builtins, 350 cumulative tests. Command tokens, paths, scope, constraints, statistics, graphs, scratchpad.

Stage 3 — Capacity Building: 49 modules, ~400 builtins, 600 tests. Sessions, inference notebooks, Q-basis, functional remainders, discrete calculus, domain math, mounts.

Stage 4 — Full Integration: 58 modules, ~437 builtins, 900 tests. Local environment, grants, filesystem, network, execution, all 4 inference modes, lifecycle pipeline.

Stage 5 — Production: 65 modules, 448 builtins, 1250 tests. Docker/SSH/VM, compilation, linting, feedback, deployment, monitoring, canary, retirement.

12 layers with explicit dependencies. Cross-stage invariants: IOSE declared on every function, exact arithmetic throughout, KB is single source of truth, data primitives bounded, no silent truncation, tests cumulative.

533 functions with full IOSE declarations — inputs, outputs, side effects, properties. Each declaration is the test spec, the Zig interface contract, and the documentation.

Python first (validates decisions), Zig final (mechanical port via IOSE contracts). Type mappings: dataclass → struct, Dict → HashMap, List → ArrayList, Optional → ?T, Result → error union, int → i128 with BigInt overflow.

~20,500 total lines (15,500 new + 5,000 existing). 705 existing tests + 1,250 planned = ~1,955 total.

*References: VDR-11 (implementation blueprint + IOSE function spec + tech spec)*

---

**Section 13: The Work Reduction**

What the LLM no longer does: arithmetic (primitives compute exactly), sorting/filtering/counting (list primitives), logical deduction (Prolog engine), state tracking (KB with integer addressing), backtracking memory (stack + LRU), confidence assessment (exact fraction propagation), data transformation (parse/format primitives), structural token generation (grammars provide free), structural token interpretation (grammars parse mechanically).

What the LLM still does: intent recognition, mode selection, formalization (translating intent into executable form), assessment (reading results and deciding next step), natural language framing.

The compound effect: the LLM does ~5% of the work at ~95% of the quality. The other 95% is exact, free, and provenance-tracked. Effective context window dramatically larger because it's not filled with computation working and state recaps. The safest token is the one that was never generated.

*References: VDR-9 (orchestrated inference), VDR-12 (grammar economics)*

---

**Section 14: What This System Is and Is Not**

Is: an exact arithmetic computational substrate with structural provenance, scoped knowledge management, deterministic primitives, grammar-directed I/O, and orchestrated inference — where the LLM orchestrates but does not compute.

Is not: a replacement for real numbers or continuous calculus. Not practical at production LLM scale yet (denominator growth, Zig port needed). Not a guarantee of correct conclusions (premises might be wrong, evidence might be incomplete — provenance makes failures detectable, not preventable).

Cumulative validation: 705 tests, zero VDR computation errors, 13 test-design failures, 23 mathematical domains, 14 physical domains, complete LLM pipeline demonstrated, 178/179 compaction tests passing.

*References: all papers*

---

**Appendices:**

A — Complete KB struct (26 fields with source paper, type, classification)
B — Complete builtin index (448 + 40 from VDR-13 notebook, by category with stage assignment)
C — Complete IOSE function list (533 functions, by stage and module)
D — Operational principles reference (15 principles with Prolog encoding summary)
E — Confidence propagation rules (source confidences + propagation formulas)
F — Compaction profile reference (6 profiles + 20 table schemas)
G — Zig type mapping reference
H — Paper cross-reference (VDR-1 through VDR-13 with paper topic, key contribution, test count)
I — Glossary (every term defined without forward references)

---

**Estimated size:** ~8,000-10,000 compacted tokens. Roughly 40-50 tables. Comprehensive but not exhaustive — depth is in the referenced papers, breadth and explanatory clarity is here.

**Validation approach:** A new reader with no prior context should be able to read sections 1-14 sequentially and understand what the system is, why each piece exists, how they fit together, and where to look for implementation detail. If they can't, the document failed.
