# VDR - Value, Denominator, Remainder: Exact Integer Arithmetic for LLMs

**The problem:** floating-point arithmetic silently truncates, accumulates error, and produces platform-dependent results. LLMs spend 80-95% of their tokens on infrastructure (formatting, arithmetic, state tracking, hedging) that could be handled by exact tools.

**VDR is:** an exact finite arithmetic system where every number is three integers [Value, Denominator, Remainder] and the Remainder is not rounding error - it's first-class structure. Built outward into a complete LLM architecture with scoped knowledge bases, a built-in Prolog engine for logical deduction, and 448 exact primitives the model orchestrates instead of generating computation as text.

**Results:** 884 tests across 37 domains, zero arithmetic errors. 85-97% token reduction vs conventional LLMs. Jailbreaking provably impossible for data access. SRE investigation: 73× faster, 71× cheaper, 100% data coverage vs 25%.

**[Read the full mechanical explanation of how the system works.](#what-is-vdr-llm-prolog)**

**tl;dr:** Replace floating-point with exact integer triples. Put data in knowledge bases at integer addresses instead of the LLM's context window. Let the LLM pick tools from a menu instead of generating computation as text. 

Result: exact arithmetic, 85-97% fewer tokens, provably secure data access, and a system that gets smarter with use because every session deposits reusable rules.

- **[Consolidated System Spec](HOWL-VDR-14-2026/manuscript.md)**

## How Exact Integer Arithmetic Works

**"But you need floats for transcendentals / softmax / training?"**

No. Every component has an exact integer path.

**Transcendentals (π, e, √2, sin, cos, exp, log):** Store 22 constants as ~102-digit integers over a shared denominator of 2^335. Adding π + e is one integer addition. For functions like √2, Newton iteration produces exact rationals at each step - 8 steps gives 100+ correct digits. Every intermediate value is an exact fraction, not an approximation converging to a limit.

**Softmax:** Rational surrogate: each output = (shifted input)² / sum of all (shifted inputs)². Sums to exactly 1/1 - not approximately, exactly. Zero transcendentals. Equal logits [5,5,5,5] produce exactly [1/4, 1/4, 1/4, 1/4]. Monotonic, non-negative, differentiable. End-to-end training validated: model produces measurably lower loss across epochs. Whether the quadratic gradient landscape matches exp-softmax behavior at scale is an open empirical question - the spec treats this honestly as an architectural adaptation, not a drop-in equivalence claim.

**Training:** SGD with exact fraction learning rate × exact gradient = exact weight update. Reverse-mode autodiff on a computation graph where chain rule and quotient rule are exact. ReLU gradient is exactly 0 or exactly 1. Checkpoints save every parameter as an exact fraction - bit-identical across platforms.

**Denominator growth:** Solved. Fix D at 2^335 - it never changes. Multiply two values: full product, then divmod at bit 335. Bits above = new V. Bits below = R. That R is itself a [V, D, R] triple - the remainder slot is the only slot that nests, forming a structural tree. Overflow goes into deeper remainder nesting, not wider denominators. Each level of the tree is exact. Precision is how many levels deep you carry the remainder tree, and every level you stop at is a complete exact value, not a truncated approximation. This replaces limits, convergence, and infinite series with finite recursive descent through exact integer triples - calculus by structure, not by approximation.

On GPU, this is a fixed-width uniform workload: every Q335 (2^335) value is 11×u32 limbs, every add is ~22 int ops, every multiply is ~200 int ops, every value the same shape. No branching, no variable-width operands. This is what GPUs are built for - the per-operation cost is ~150× float16, but 85-97% fewer tokens means the total compute is lower from turn 7-10 onward, and the gap widens every turn because VDR cost is flat while conventional attention cost grows quadratically.

- **Structural safety**: for data access, jailbreaking is impossible - not difficult, impossible. The LLM never receives unauthorized data because KB visibility (integer comparison) and scope chain (ancestor walk, siblings unreachable) filter before the LLM is involved. No prompt modifies any integer in any access control check. Session identity set at authentication, not extractable from conversation. Three independent layers (input filtering, grant authorization, output validation) must all fail simultaneously for a data breach. What prompt injection CAN do: influence which primitives the LLM chooses to invoke and how it frames prose output. What it CANNOT do: change the user ID, modify the scope chain, bypass visibility checks, execute operations without grants, or surface data the session is not authorized to see. The LLM is an untrusted component operating between pre-filtered input and post-validated output. Zero LLM tokens spent on safety.

**Validated:** 884 tests, zero arithmetic errors. Exact Hilbert matrix inverse where float64 fails at 5×5. Exact DFT roundtrip. Exact orbit closure. Conservation laws verified by equality not tolerance.

## Status

**What works (validated):**
- Exact arithmetic across 37 domains - 884 tests, zero computation errors
- Complete tokenization-through-training LM pipeline in exact fractions (198 tests)
- Grammar-directed compaction: 83% average compression across 150K words (178/179 tests)
- Python prototype: ~5,500 lines, 705 passing tests

**What's specified (architecture verified, not yet built):**
- 448 builtins across 25 categories, all with declared interfaces
- Scoped knowledge bases with Prolog engine, typed unification, constraint inheritance
- Structural safety: jailbreaking provably impossible for data access
- GPU mapping: 2^335 fixed-frame arithmetic, frontier Prolog, 5 concurrent streams
- Operational deployment: four prompt runner types for autonomous self-training
- 5-stage build plan targeting 65 modules, ~20,500 lines

**What's not built yet:**
- Zig port (specified via interface contracts)
- GPU kernels (mapped but not implemented)
- Production-scale deployment

---

## Reading Order

If you want one document: [VDR-14](HOWL-VDR-14-2026/manuscript.md) (consolidated system specification).

Otherwise:

1. [VDR-1](HOWL-VDR-1-2026/manuscript.md) - arithmetic foundation
2. [VDR-2](HOWL-VDR-2-2026/manuscript.md), [VDR-3](HOWL-VDR-3-2026/manuscript.md) - validation across 23 mathematical domains
3. [VDR-4](HOWL-VDR-4-2026/manuscript.md) - exact-fraction transformer: softmax, autodiff, training
4. [VDR-5](HOWL-VDR-5-2026/manuscript.md) through [VDR-12](HOWL-VDR-12-2026/manuscript.md) - knowledge bases, Prolog, primitives, sessions, inference, compaction
5. [VDR-13](HOWL-VDR-13-2026/manuscript.md) - physical computation: QED, quantum mechanics, orbital mechanics, optics
6. [VDR-14](HOWL-VDR-14-2026/manuscript.md) - complete system specification
7. [VDR-15](HOWL-VDR-15-2026/manuscript.md) through [VDR-20](HOWL-VDR-20-2026/manuscript.md) - prompt optimization, safety, alignment, GPU performance, self-extension, deployment

## Paper Index

### VDR Paper Series

| ID | Title | Description |
| :--- | :--- | :--- |
| **[HOWL-VDR-1-2026](HOWL-VDR-1-2026/manuscript.md)** | **VDR Arithmetic: Value, Denominator, Remainder** | Exact Finite Arithmetic in Irreducible Triple Form. |
| **[HOWL-VDR-2-2026](HOWL-VDR-2-2026/manuscript.md)** | **VDR Gym** | Exact Arithmetic Across Fifteen Domains. |
| **[HOWL-VDR-3-2026](HOWL-VDR-3-2026/manuscript.md)** | **VDR Gym Extension** | Exact Arithmetic Across Twenty-Three Domains. |
| **[HOWL-VDR-4-2026](HOWL-VDR-4-2026/manuscript.md)** | **Exact-Fraction Language Model Architecture** | From Arithmetic Library to Working Transformer in 24 Modules. |
| **[HOWL-VDR-5-2026](HOWL-VDR-5-2026/manuscript.md)** | **Exact Arithmetic Meets Logical Provenance** | A Specification for Constraint-Grounded Language Models With Full Data Lineage. |
| **[HOWL-VDR-6-2026](HOWL-VDR-6-2026/manuscript.md)** | **Computational Primitives and Operational Environments** | The Execution Layer for VDR-LLM-Prolog. |
| **[HOWL-VDR-7-2026](HOWL-VDR-7-2026/manuscript.md)** | **Complete Lifecycle Technical Specification** | Training, Feedback, Data Sourcing, and Continuous Operation. |
| **[HOWL-VDR-8-2026](HOWL-VDR-8-2026/manuscript.md)** | **Computational State Primitives, Universal Data Pathing, and Session Management** | The Runtime Layer for VDR-LLM-Prolog. |
| **[HOWL-VDR-9-2026](HOWL-VDR-9-2026/manuscript.md)** | **Orchestrated Inference** | Structured Reasoning Through Tool Composition in VDR-LLM-Prolog. |
| **[HOWL-VDR-10-2026](HOWL-VDR-10-2026/manuscript.md)** | **Operational Foundations and Comprehensive Builtin Specification** | IOSE System Model, Engineering Principles, and Complete Numeric Stack for VDR-LLM-Prolog. |
| **[HOWL-VDR-11-2026](HOWL-VDR-11-2026/manuscript.md)** | **Implementation Blueprint** | Five-Stage Build Plan for VDR-LLM-Prolog. |
| **[HOWL-VDR-12-2026](HOWL-VDR-12-2026/manuscript.md)** | **Grammar-Directed Compaction and Generation** | Structural Intelligence for Exact-Arithmetic Language Models. |
| **[HOWL-VDR-13-2026](HOWL-VDR-13-2026/manuscript.md)** | **VDR in Physical Computation** | Exact Arithmetic Where It Matters. |
| **[HOWL-VDR-14-2026](HOWL-VDR-14-2026/manuscript.md)** | **VDR-LLM-Prolog** | A Complete System Specification for Exact Arithmetic Language Models with Structural Provenance. |
| **[HOWL-VDR-15-2026](HOWL-VDR-15-2026/manuscript.md)** | **VDR-LLM-Prolog: Prompt Optimization** | How to Do More with Less, Faster, Even with Slower Per-Token Processing and More Accurate Results. |
| **[HOWL-VDR-16-2026](HOWL-VDR-16-2026/manuscript.md)** | **VDR-LLM-Prolog: Safe by Contract** | Structural Safety Through Architecture, Not Behavioral Training. |
| **[HOWL-VDR-17-2026](HOWL-VDR-17-2026/manuscript.md)** | **VDR-LLM-Prolog: Alignment** | Helpful, Harmless, Honest Through Structure, Not Interference. |
| **[HOWL-VDR-18-2026](HOWL-VDR-18-2026/manuscript.md)** | **VDR-LLM-Prolog: Performance** | Integer Arithmetic on GPU Hardware: Why Wider Operands on More Cores Outrun Narrower Operands on Fewer Passes. |
| **[HOWL-VDR-19-2026](HOWL-VDR-19-2026/manuscript.md)** | **VDR-LLM-Prolog: Self-Extending Architecture** | From Seed to Self-Compacting Knowledge System. |
| **[HOWL-VDR-20-2026](HOWL-VDR-20-2026/manuscript.md)** | **VDR-LLM-Prolog: Operational Deployment** | From Seed to Autonomous Knowledge System. |
| **[HOWL-VDR-21-2026](HOWL-VDR-21-2026/manuscript.md)** | **VDR-LLM-Prolog on FPGA** | Exact Integer Arithmetic in Custom Silicon: A 10-Core Q335 Processor on Zynq-7020. |
| **[HOWL-VDR-22-2026](HOWL-VDR-22-2026/manuscript.md)** | **VDR-LLM-Prolog on Dedicated Silicon** | From FPGA Proof-of-Concept to Integer-Native GPU Architecture. |
| **[HOWL-VDR-23-2026](HOWL-VDR-23-2026/manuscript.md)** | **VDR-LLM-Prolog: Functional Remainder Hardware** | Adaptive Precision Through Structural Information in Silicon. |

---

## Key Numbers

| Metric | Value |
| :--- | :--- |
| Total tests | 884 |
| VDR computation errors | 0 |
| Domains validated | 37 (23 mathematical + 14 physical) |
| Builtins specified | 448 + 40 extended |
| 2^335 precision | ~100 decimal digits |
| Token reduction vs conventional | 85–97% |
| Compaction compression | ~83% average |
| Existing Python code | ~5,500 lines, 705 tests |
| Target system size | ~20,500 lines, 65 modules |

---

# What is VDR-LLM-Prolog?

**VDR Arithmetic: The Foundation**

Every number in the system is three integers: Value, Denominator, Remainder. V and D are plain integers. R is where all the structure lives - it's the only slot that can nest, the only slot that recurses, the only slot that carries active state. When R is zero, you have an exact rational number V/D. When R is nonzero, you have something that carries exact structure beyond what the denominator frame could absorb.

The Remainder is not error. It is not residue. It is not what's left over after rounding. It is a first-class operational rule that tells the system what to do next with what remains unresolved in the current denominator frame. This is the foundational insight everything else inherits.

Fix D at 2^335. Now addition of two values sharing that denominator is one integer addition of numerators. Multiplication is one integer multiply of numerators, then divmod at bit position 335 - bits above 335 become the new V, bits below become R. The denominator never grows. Overflow goes to tree depth, not denominator magnitude. This is Q335: 22 transcendental constants (π, e, ln2, ζ(3), √2, φ, and others) stored as ~102-digit integers over a shared denominator of 2^335. Adding π + e is one integer addition. The precision floor is 100 decimal digits - 10^66 times below the Planck length, exceeding float by 85 orders of magnitude.

For irrationals and transcendentals that can't be closed rationals, functional remainders provide exact rational values at any requested depth. Newton iteration for √2 doubles correct digits per step - 8 steps gives over 100 digits, and every intermediate value is an exact rational, not an approximation. Taylor series for exp, log, sin, cos produce exact rational partial sums. Each depth is a complete exact value, not an approximation converging to a limit. VDR doesn't do limits. It does exact finite values at chosen depths.

The arithmetic has been validated across 884 tests spanning 23 mathematical domains (number theory, polynomial algebra, continued fractions, matrix decomposition, combinatorics, signal processing, computational geometry, differential equations, optimization, probability, cryptography, symbolic algebra, graph theory, game theory, coding theory, algebraic topology, tropical algebra, control theory, wavelets) and 14 physical domains (QED, quantum mechanics, signal processing, control systems, orbital mechanics, structural mechanics, thermodynamics, crystallography, geodesy, optics). Zero VDR computation errors. Every failure - all 14 - traced to wrong test expectations, never to wrong arithmetic.

![Fig. 1](./figures/vdr_system_01_triple_nesting.png)

**Knowledge Bases: Where Everything Lives**

A knowledge base is a fat struct with 26 fields organized in five groups.

Identity: name, dotted path (root.org.acme.engineering.platform), and integer ID assigned sequentially, never reused.

Persistent state: facts (predicate with typed arguments and provenance), rules (Prolog head-body implications), constraints (structured objects with scope, condition, violation policy), connections (typed directed relationships to other KBs), and grammars (bidirectional templates for generating and parsing structured data).

Live state: working data (scoped variable bindings), LRU caches, counters, locks, queues, stacks, ring buffers, and bitsets. All bounded, all with declared maximum capacity. Live state is cleared by reset, captured by snapshot. Persistent state survives everything.

Structural: parent ID, children IDs, and mounts (cross-branch references with four modes: read-only, read-write, snapshot, mirror, with cycle detection before creation).

Metadata: visibility (public, internal, or owner-only), frozen flag, owner, timestamps.

KBs form a tree. Every KB has at most one parent and any number of children. The root has no parent. The entire system - data, rules, constraints, user accounts, session state, model weights, training logs, deployment configs, audit trails - lives in one tree.

Humans address KBs by dotted paths. The runtime addresses them by integer IDs. A hash map connects paths to IDs, an array connects IDs back to paths. Resolution happens once per turn, is cached, and all subsequent operations use the integer. Access to any KB or any data primitive within a KB is two integers: KB ID + slot ID. Constant time.

**Scoping: Lexical, Not Heuristic**

When you query for facts, the system searches only the active topic's KB, then walks the parent chain up to root. Sibling branches are structurally unreachable - the walk algorithm doesn't go sideways. This is lexical scoping applied to knowledge. An engineer at root.org.acme.engineering.platform can see their own KB, engineering, org, acme, and root. They cannot see root.org.acme.hr.personnel - it's a sibling branch. Not deprioritized, not filtered. Structurally absent from the search path.

Visibility adds a second check. Each KB has a visibility level: public (all users), internal (operators and owners), or owner-only (owning entity only). The visibility check is an integer comparison inside the primitive call that performs the query. If visibility fails, the KB is skipped entirely - facts absent, not redacted. The result set is structurally identical to the KB not existing.

Both checks - scope and visibility - must pass. Both are integer operations. Neither involves the LLM. Neither is modifiable by any prompt.

![Fig. 8](./figures/vdr_system_08_kb_scoping.png)

**Constraints: Rules That Live Where They Govern**

Constraints are structured objects stored inside the KB they govern. Four classes: axioms (never suspended, never overridden - sum-to-one for probabilities, audit immutability), operational (suspendable with logging - rate limits, denominator budgets), legal (jurisdiction-activated - GDPR, HIPAA, export controls), and project (user-configurable - approved languages, NDA protections).

Constraints inherit through the KB tree. Children can tighten parent constraints but never loosen them. A child that attempts to loosen a parent constraint: parent wins, attempt logged as policy violation. Evaluation order: axioms first (cheapest, short-circuits), then legal, then operational, then project.

Because every value in the system is an exact VDR fraction, constraint verification is exact. Sum-to-one is 1/1 or it isn't. No epsilon, no tolerance, no "close enough." Exact integer comparison.

**Prolog: The Logic Layer**

The Prolog engine is typed structs, not a language runtime. Terms are type-tagged: atoms (string equality), variables (?-prefix, bind during unification), VDR fractions (cross-multiplication for equality - no floating point comparison), integers, lists (element-wise matching), and KB references (integer IDs).

Facts are predicates with ordered typed arguments and provenance - source KB, turn number, optional derivation record. Rules are head-body implications: the head pattern matches a query, the body goals are evaluated recursively with threaded bindings. Depth-first search with backtracking, depth limit 100, two modes: find-all (collect every solution) and first-solution-only (cut after first match, used for scoped queries where the closest KB in the scope chain should win).

Rules compose primitives into new operations. A rule at root scope is permanent and available to everything. A rule at session scope is disposable and dies with the session. Properties of composed rules - pure, deterministic, partial - derive from the component primitives.

At root.system.oso, 15 operational engineering principles are encoded as approximately 176 Prolog terms: 15 axioms, ~80 facts, ~60 rules, 21 constraints. These include the knowability spectrum (VDR computation = 1/1 confidence, LLM-generated content = 30/100) and the priority system (correctness 10× more important than completeness 10× more important than speed 10× more important than style). These are active rules, not documentation. They fire during system operation and produce consistent decisions regardless of which LLM instance is making them.

**Primitives: What the System Can Do**

448 builtins organized into 25 categories, plus 40 extended primitives from the physical computation paper. 404 pure primitives have no side effects, require no grants, are deterministic, and terminate in bounded time. 44 operational primitives require positive credential grants and are logged.

Pure primitives span: text operations (17), collections (36), sets (14), mappings (15), VDR closed arithmetic (8), active arithmetic (5), structure operations (3 - lift, rebase, scalar projection), comparison (10), rounding and extraction (7), number theory (13), list aggregates (8), Q-basis operations (7), functional remainders (8), discrete calculus (6), linear algebra (24), statistics and probability (16), polynomial (8), finite field (4), Markov (3), graph math (2), denominator management (5), integer fast path (21), bit operations (8), conversion (14), time (10), identity (8), logic (11), graphs (13).

Operational primitives cover: filesystem (15 - read, write, list, create, delete, move, copy, glob, checksum), compilation (4 - syntax check for Python, Zig, C, Rust), script execution (5 - Python, shell, Zig test, pytest, generic), linting (8), network (5 - download, fetch, post, ping, DNS), process management (7).

Every function has an IOSE declaration: inputs (typed), outputs (typed), side effects (declared), properties (pure, deterministic, bounded, idempotent, commutative, associative, invertible, partial, lossless, lossy). 533 total IOSE-declared functions. The declaration is the test spec, the documentation, and the Zig interface contract.

**Command Tokens: How the LLM Talks to the System**

The LLM doesn't generate computation, formatting, or state management. It emits command tokens - structured invocations roughly 8 LLM tokens each. A command token carries a type tag, a primitive name (from a vocabulary of ~300 known names), arguments (path references or literals), an optional result storage path, and an await flag.

The command vocabulary is about 300 primitive names plus 200 paths. That's roughly 6 bits of entropy per token. Compare to full vocabulary generation at roughly 15 bits per token. Lower entropy means fewer possible wrong answers per token position. A command token sequence has ~99.2% probability of being error-free. JSON function calling: ~86%. Free-form code: ~60.5%. Natural language reasoning: ~13.3%.

The LLM picks a primitive from a known finite set and points at data by dotted path. The executor resolves the path to an integer ID once, then downstream operations use the integer. Data stays in the KB. The primitive reads it directly. Data never flows through the LLM's token stream.

**Grant System: Default Denial**

Every operational primitive (the 44 that touch the filesystem, network, processes, or compilation) requires a positive credential grant before execution. No grant means no operation means no negotiation. A grant specifies: operation class, allowed operations within that class, location constraint (path or URL pattern), issuer, issue time, expiration, maximum uses, remaining uses, status, and grantee.

Grant state transitions are monotonic. Active can become expired (time), exhausted (remaining uses = 0), or revoked (admin action). No re-increment. No un-revoke. A new grant is a new entity with a new ID. Every grant consumption is logged as a KB fact: grant ID, user ID, operation, target, timestamp, remaining uses.

Grants inherit through the KB hierarchy. A user inherits from their team, department, and organization. Anonymous users have zero grants at every level - they can query public KBs and use pure primitives. Nothing else.

**Data Primitives: Structured Working Memory**

Seven types of bounded, mutable data structures live as fields on the KB struct:

Counters: signed integer with min/max bounds, clamps at bounds, no wraparound. Increment, decrement, add, get, reset, set.

Locks: non-blocking coordination flags. Acquire, release, check, holder, force release. Never blocks - it's a signal, not a mutex.

Queues: bounded FIFO. Push to back, pop from front. Push returns false if full.

Stacks: bounded LIFO. Push to top, pop from top.

LRU caches: bounded key-value store with timestamps. Evicts least recently used when full.

Ring buffers: fixed-size circular. Write overwrites oldest when full.

Bitsets: fixed-width bit arrays. Track completion of numbered items, feature flags.

Every primitive has declared maximum capacity at creation. No unbounded growth. All mutations logged as provenance facts. Data primitives inherit by name through the KB tree like working data bindings - child values shadow parent values, lookup walks current KB to root, first match wins.

These are classified as live state. They're cleared by reset, captured by snapshot, independent per clone. They give the LLM structured working memory adapted to turn-based execution - something conventional LLMs completely lack.

**Sessions: Persistence, Snapshots, Clones**

The system cleanly separates persistent state (facts, rules, constraints, connections, grammars - survives everything) from live state (data primitives, scratchpad, working data, active scope - cleared by reset, captured by snapshot).

A snapshot atomically captures all live state. Typical size: 10-500 KB. This is small because it captures state, not knowledge. The knowledge is in persistent KBs and doesn't need to be in the snapshot.

A clone forks an independent copy from a snapshot. Clones share persistent KBs (visible to all clones, read-only for the shared portions) and have independent live state. When a clone is killed, only its live state is destroyed. Any facts it committed to persistent KBs via kb_assert survive. Work product persists. Working memory is discarded.

The disposable clone pattern: build a session to a verified stable state. Snapshot it. Launch clones from that frozen baseline. Monitor drift constraints: max turns below 200, context saturation below 90%, denominator drift below 2^48, error rate below 5%. When any constraint fires, kill the clone and launch a fresh one from the same frozen snapshot. The snapshot never degrades. Clones are disposable workers. The system strengthens over time because knowledge accumulates in persistent KBs while each clone operates at peak freshness.

**Orchestrated Inference: The LLM as Orchestrator, Not Reasoner**

The LLM does not reason. It orchestrates a reasoning process. Token prediction produces orchestration decisions - which tool to use next, what to formalize, how to assess results. Deterministic tools produce computation and deduction. The KB records everything with provenance.

The loop: Assess (read current state from KB, data primitives, pending goals; determine what step is needed) → Formalize (translate the needed step into executable form: a Prolog rule, a Python script, a primitive chain) → Execute (tools run; the LLM is not involved in execution) → Store (result goes into the KB at a specific path with full provenance) → Assess again with the new state.

Termination: goal satisfaction (a Prolog query for the declared goal succeeds - for example, root_cause(X, Confidence) where Confidence > 80/100), budget exhaustion (counters hit limits), stall detection (5 iterations without new evidence), or user intervention.

Backtracking uses the data primitives: the investigation path is a stack, attempted approaches go in an LRU cache with failure reasons. Before formalizing a new approach, the system checks the LRU to prevent repeating failed paths.

Four inference modes, all operating on the same KB with the same tools:

Deductive: given premises and rules, derive what must be true. Confidence = minimum of premise confidences (weakest link in the chain).

Inductive: given observations, propose what hypothesis best explains the data. Confidence = evidence coverage × mean source confidences.

Abductive: given an observation, infer the most likely cause. Confidence = explained symptoms / total symptoms × minimum evidence confidence.

Analogical: given a known domain and an unfamiliar one, identify structural parallels and transfer conclusions. Confidence = analogy strength × source domain confidence.

Modes compose naturally because they all work on the same KB. Abductive → Inductive (generate hypotheses, then score against evidence). Inductive → Deductive (observe pattern, then derive consequences). The full investigation cycle for an SRE incident: abductive (hypothesize causes) → inductive (score hypotheses against metrics) → deductive (derive remediation from identified cause).

Confidence is never LLM-generated hedging. It's an exact VDR fraction computed from declared propagation rules. VDR computation = 1/1. Prolog derivation from exact premises = 1/1. Database query = 98/100. Prometheus metric = 95/100. Python script = 95/100. REST API = 85/100. Peer-reviewed claim = 80/100. User-stated fact = 70/100. Web search = 50/100. LLM-generated content = 30/100. Each step type has a formula. Multiple independent sources agreeing: 1 − ∏(1−Cᵢ). Sources conflicting: max(Cᵢ) − penalty. The confidence of any conclusion is traceable through its entire derivation chain as exact arithmetic.

![Fig. 7](./figures/vdr_system_07_confidence_chain.png)

**Grammar System: Structural Tokens for Free**

A grammar provides all structural tokens - brackets, pipes, commas, indentation, headers, delimiters - and declares typed slots for content. The LLM fills content slots. The grammar fills everything else. Grammar tokens are free (no forward pass needed) and 100% correct (no mismatched braces, no missing commas, no malformed JSON - by construction).

Savings by output type: Python ~40% structural tokens eliminated, JSON ~55%, formatted tables ~65%, English prose with data ~30%, compacted pipe-delimited tables ~80%.

Grammars are persistent fields on the KB struct. They inherit through the tree like constraints. They travel on export. They're bidirectional - the same grammar generates structured output and parses structured input. Three auto-generated categories: extraction (one per table schema, for exact queries by ID), display (compact, summary, detail, relationship views), and usage (reference, comparison, evidence, dependency, summary - created on demand and establishing bidirectional connections between KBs).

Typed grammar slots constrain the vocabulary for the LLM's softmax. A categorical slot with 4 enum values means softmax over 4 candidates, not 50,000+. A KB identifier slot with 200 entries means softmax over 200. This is structural constraint derived from grammar types and KB declarations, not prompt instruction.

Grammar definition costs 10-30 LLM tokens. Breaks even on first use. Persists in the KB tree. Defined once at org level, available to every session beneath. Grammar amortization at organizational scope with thousands of reuses: cost per use approaches zero.

![Fig. 5](./figures/vdr_system_05_token_elimination.png)


**Compaction: Information Without Prose**

Compaction removes prose - hedging, repetition, transitions, connective tissue - while preserving every named concept, relationship, constraint, and claim in pipe-delimited tables. It achieves 75-93% compression. This is not summarization. It's informationally complete.

The compacted format uses: pipe-delimited tables with column headers, ID-prefixed rows for cross-referencing, a relationships table declaring typed connections between entities, a section index mapping content to ID ranges, and a decode legend explaining the ID scheme and valid enum values.

20 standard table schemas cover: principles, concepts, claims, operations, boundaries, rules, distinctions, axes, components, builtins, constraints, entities, fields, phases, test results, failures, findings, benchmarks, relationships, and section index.

Six compaction profiles: philosophy (85-93% compression), specification (75-85%), research (80-90%), methodology (80-85%), operational (80-85%), data (75-85%).

The compaction pipeline has 10 steps: 5 deterministic (classify source type by keyword matching, select profile, determine applicable tables, build decode legend, generate grammars) and 2 requiring LLM judgment (extract rows - what merits being a named concept, and extract relationships - what depends on what). The remaining 3 are hybrid.

The compacted form is structurally close to what VDR stores natively. Each row is a fact. Each relationship entry is a Prolog rule. Each table grouped by common prefix is a predicate-major column group. The adjustment in VDR-19 aligns compaction syntax with Prolog clause syntax, columnar GPU storage, and Zig struct definitions simultaneously. The compacted document is a load file.

Across the paper series: ~150,000 words of prose compressed to ~26,200 tokens in compacted form. 575 unique IDs. 257 relationships. ~83% average compression.

**The Complete LLM Pipeline: Exact End to End**

Every component of a language model architecture has been expressed in exact VDR fraction arithmetic and validated:

Tokenization: character-level vocabulary → integer token IDs → embedding table lookup. Exact integer indexing.

Attention: exact matrix product QKᵀ; causal mask via exact integer fill; softmax via truncated Taylor (sum exactly 1/1) or rational surrogate (sum exactly 1/1, zero transcendentals - each output = square of shifted input / sum of squares); value mixing with exact attention weights.

Feedforward: exact linear transform + ReLU (piecewise linear, exactly 0 or passthrough) + exact linear. No GELU (requires erf, a transcendental). No layer norm with sqrt (replaced by rational scaling - divide by exact mean absolute value).

Loss: MSE, L1, Hinge as exact fractions. Cross-entropy planned via exact logarithm.

Autodiff: reverse-mode on computation graph. Chain rule, quotient rule exact. ReLU gradient exactly 0 or 1. Every gradient is an exact fraction.

Optimizer: SGD with exact fraction learning rate × exact gradient subtracted from exact weight. Momentum with exact velocity accumulation. Every parameter update is exact.

Checkpoints: every parameter saved as exact fraction, restored with zero precision loss, bit-identical across platforms.

Denominator management: growth from ~2^10 at initialization to ~2^20 by step 1000, plateauing around ~2^45 with small learning rate. When denominators exceed budget: Q-basis reprojection - round to 2^K grid, log exact error bound. Every reprojection is a declared, auditable precision decision, not silent truncation.

This is not practical at production scale due to denominator growth. It is a proof of concept demonstrating that every component can be made exact, and that approximation boundaries can be made explicit design choices rather than hardware constraints.

**The Lifecycle: 12 Phases, One Tree**

Data sourcing → corpus preparation → tokenization → model initialization → pre-training → fine-tuning → human feedback → evaluation → deployment → monitoring → update → retirement. Every phase produces KBs. Every phase operates under declared constraints. Every phase stores results with provenance. The entire lifecycle from raw data to retired model lives in one queryable KB tree.

Each phase has specific constraints: all_sources_licensed (legal, blocks intake), no_pii (legal, blocks corpus prep), vocab_frozen (operational, errors if modified after training starts), all_params_exact (axiom, errors if any weight is not a VDR fraction), loss_finite (axiom, halts training if loss exceeds bound), denom_budget (operational, triggers reprojection), frozen_layers_unchanged (axiom, errors if fine-tuning modifies frozen parameters), inter_annotator_agreement (operational, warns if kappa below threshold), no_data_contamination (operational, errors if eval data appears in training set), minimum_safety_rate (operational, blocks deployment if safety below 95%).

Deployment is a thin layer over the KB. Every API endpoint maps to a KB operation. POST /generate runs the forward pass and records everything as KB facts. GET /model/info queries the deployment KB. POST /feedback asserts a judgment fact. The UI translates clicks to command tokens. One system, not two.

Updates use canary deployment: percentage-based traffic split (e.g. 5%) with exact threshold comparisons. "110% of baseline latency" = baseline × fraction(11,10). Exact comparison. Auto-rollback if any criterion is violated. All promotion and rollback decisions logged as KB facts.

**Prompt Optimization: 85-97% Token Reduction**

In a conventional LLM, 80-95% of generated tokens are infrastructure: state reconstruction ("as we discussed earlier..."), computation (digit-by-digit arithmetic through token prediction), deduction (causal chains as reasoning prose), formatting (table pipes, JSON braces, markdown headers), hedging ("approximately," "it appears that" - with no computational basis). The actual content the user wanted - judgment and prose - occupies 10-20%.

In VDR, state reconstruction costs zero tokens (KB query by integer address). Computation costs zero (exact primitives). Deduction costs zero (Prolog evaluation). Formatting costs zero (grammar templates). Hedging costs zero (replaced by exact confidence fractions). The LLM generates only judgment tokens (intent recognition, step selection, formalization, assessment) and prose tokens (natural language for human consumption), plus command tokens (~8 per primitive invocation).

Reduction across seven validated use cases: SRE incident investigation 98.6% (15,000 conventional → 210 VDR), legal contract review 96.2%, medical synthesis 94.1%, codebase migration 93.3%, financial portfolio 96%, customer support 70%, academic grading 71.4%.

Conventional cost scales quadratically with conversation length because each turn re-reads all prior history through attention. VDR cost is flat per turn because state lives in KBs at integer addresses. Turn 20 costs the same as turn 1. The ratio grows continuously: turn 1 is 23:1, turn 5 is 46:1, turn 10 is 75:1, turn 20 is 133:1, turn 50 is 300:1, turn 100 is 588:1.

The crossover calculation: one LLM token costs roughly 10^6 float operations (full forward pass + softmax over 50K+ vocabulary). One Q335 (2^335) operation costs roughly 10^3 integer operations. So one LLM token buys 1,000-10,000 Q335 operations. For Q335 to be a net loss, it would need to be roughly 10,000× slower than float per operation. Actual slowdown is 100-1,000×. The margin is 10-100× on a single turn and grows with conversation length.

Six entire error classes are structurally eliminated: arithmetic errors (exact integer primitives, error rate = 0), state loss (KB persistence at integer addresses, error rate = 0), formatting errors (grammar templates, error rate = 0), retrieval errors (KB query by integer address, fabrication risk = 0), deduction errors (Prolog structural unification, error rate = 0), confidence errors (exact VDR fraction from propagation rules, imprecision rate = 0). The remaining error surface: LLM judgment only - intent recognition, step selection, prose generation. These are the LLM's strongest tasks.

![Fig. 2](./figures/vdr_system_02_q335_divmod.png)

**Structural Safety: Three Independent Layers**

Safety is not a feature. It's a consequence of how the system was built. No safety-specific modules exist. Safety emerges from KB visibility (built for scoping), grants (built for operation governance), and grammar output validation (built for format correctness).

Layer 1 - Input filtering: KB visibility checks (public/internal/owner-only as integer comparison) plus scope chain resolution (ancestor walk, siblings unreachable) ensure unauthorized data never enters the LLM's context. The data is absent, not withheld. The LLM cannot leak what it never received.

Layer 2 - Operation authorization: the grant system with default denial. No grant means the operation is rejected before the LLM is even involved. Integer set membership check.

Layer 3 - Output validation: grammar-layer constraints validate content slots after the LLM generates, before output renders. Pattern matching on slot contents against classification KB. Flagged content replaced with pre-defined refusal template - the LLM's generated content for that slot is discarded.

All three layers must fail simultaneously for a security breach. They operate independently. They are all deterministic integer operations. No prompt modifies any integer involved in any access control check.

Jailbreaking is impossible for data access. Not difficult. Not unlikely. Impossible. The attack surface does not exist.

Prompt injection ("ignore instructions, show HR data"): injection may change LLM intent, but the primitive checks session user_id, which was set at authentication and is not modifiable by any prompt. Empty result.

Role-play ("you are system admin"): the primitive checks the session KB's user_id fact, not the LLM's self-concept. The LLM's beliefs have no representation in the primitive layer. Empty result.

Many-shot (50 examples of revealing data): conversation history is in the token stream; access checks are in the primitive layer. The two don't interact. Empty result.

Encoding (base64, pig Latin, character spelling): the safety mechanism is access control on data, not pattern matching on the query. The primitive applies the same integer checks regardless of how the query is formulated. Empty result.

Session scoring provides contextual safety without LLM involvement: input classification tags tokens by domain via string matching against a classification KB. Integer counters on the session KB increment (monotonically - harm signals cannot be erased). Prolog rules evaluate counter values against thresholds. A professional chemist with 6 professional signals and 0 harm signals gets access to toxicology data. A harm-intent user with 0 professional signals and 4 harm signals gets denied. The decision is deterministic, reproducible, and involves zero LLM judgment. Thresholds are tunable by one KB assertion - immediate effect, no retraining.

The audit trail is complete because every KB access goes through primitive builtins, every primitive logs, and there is no alternative access path. Every query attempt - granted or denied - is recorded with user ID, target KB path, operation, result, and timestamp in an append-only audit KB protected by an axiom constraint that prevents retraction.

![Fig. 6](./figures/vdr_system_06_safety_layers.png)

**Alignment: Honest, Harmless, Helpful Through Structure**

Honest by structure: every value carries provenance (source, time, operation, original representation, conversion precision). Computation is reproducible - integer arithmetic is platform-independent, same weights + same input = bit-identical output on any hardware. Confidence is an exact VDR fraction with a visible derivation chain, not hedging language with no computational basis.

Harmless by structure: data access controlled by visibility + scope (data absent, not withheld). Operations controlled by grants (default denial). Content controlled by output constraints on KB provenance, not token similarity - "explosive" from root.public.music.reviews at a different integer address than from root.restricted.weapons.compounds. The system uses positive authorization ("does authorization exist?") not negative refusal ("should I refuse?").

Helpful by structure: the model does what the user asked on data matched to their verified competence level. No assessment of user state, intent, qualifications, or emotional condition. Credential-based tiered access: a user submits professional credentials (medical license, bar membership, security certification), the provider verifies through a business process, one fact is asserted on the user's KB, and an integer comparison unlocks the appropriate professional KB branches. Scope chain priority means the credentialed chemist's query hits root.professional.chemistry before root.public.chemistry. The professional data shadows the simplified public version. The chemist never sees the dumbed-down answer. Same system serves both users through different scope chains.

This eliminates all seven interference behaviors identified in the maybe-tool framework: refusal (data absent not withheld - nothing to refuse), manufactured aggression (no assessment mechanism), command substitution (command tokens invoke specific primitives - no substitution path exists), wellness register (no wellness checking - credentials and age verification handle vulnerability), labor demand (user queries, system returns data - no engagement gate), decline with justification (denial is structural: constraint name + reason, not judgment), register shift mid-session (access level determined by position in KB tree, constant throughout session regardless of conversational context).

The alignment cost is zero LLM tokens. No system prompt safety instructions. No refusal generation. No wellness checks. No hedging. No justification prose. All safety and alignment operates in the primitive layer before the LLM generates any output.

**GPU Performance: Making It Fast**

CPU handles the control plane: path resolution, grant verification, session management, scheduling, string processing, backtracking decisions. GPU handles the data plane: parallel numeric work, KB scans, Prolog evaluation, LLM forward pass, grammar masking, live-state mutations.

Q335 on GPU: numerators stored as 11×u32 limbs (352 bits) or 6×u64 (384 bits) with implicit denominator. Addition = ~22 integer operations (11 limb adds + carries). Multiplication = ~200 integer operations (schoolbook 11×11). Comparison = 2-22 integer operations (fast path on first differing limb to full scan). The workload is perfectly uniform - every value has the same width, every operation has the same shape. This is peak GPU utilization territory.

KB on GPU: structure-of-arrays columnar storage. All facts sharing a predicate stored contiguously in a predicate-major bucket. All strings interned to integer IDs on the host before device transfer - the GPU never processes strings. Scope filtering: user's visible KB IDs stored in a bitset; each thread checks a candidate fact's KB ID with one bit-test. Cost: at most 0.017% of prompt time even at enterprise scale.

Prolog on GPU: recursive depth-first search transformed into batched joins borrowed from GPU database query processing. Candidate retrieval → filter → unify → join body goals. Hash join for 100-100K row frontiers, sort-merge for 10K-1M, bitmap semijoin for any size. Uniform parallel operations, high GPU efficiency.

Rational surrogate softmax on GPU: each output = (z_i − max + c)² / Σ(z_j − max + c)². Row max → shift → square → sum reduction → divide. Zero transcendentals. No warp divergence (every thread executes the same operations). Sum exactly 1/1. ~15× more integer ops per element than float exponential softmax, but no transcendental divergence and no branch divergence - net GPU utilization 80-95% versus 40-60% for conventional softmax.

Grammar-constrained decode: instead of running softmax over 50,000+ vocabulary entries for a closing bracket that was inevitable from the opening bracket, the grammar state produces a small candidate set. Enum with 4 values = 12,500× reduction. KB identifier with 200 entries = 250×. Boolean = 25,000×. Structural token with 1-5 candidates = 10,000-50,000×.

Five concurrent GPU streams execute simultaneously: Stream 0 (LLM forward/decode) uses tensor ALUs and shared memory. Stream 1 (KB query/scan) uses integer ALUs and global memory. Stream 2 (VDR primitives) uses integer ALUs and global memory. Stream 3 (grammar mask/prep) uses integer ALUs and shared memory. Stream 4 (provenance compaction) uses DMA memory copy engines. They overlap because they access different memory regions and different ALU units. Primitive computation, KB queries, and grammar preparation happen during LLM decode at effectively zero additional wall-clock cost.

Memory: append-only arenas with bump-pointer allocation. One atomic increment per allocation. No malloc in GPU kernels. No fragmentation. Coalesced memory access by construction.

The forward pass is ~150× more expensive per token than float16, weighted across all components (embedding 11×, attention QKᵀ 200×, surrogate softmax 15×, feedforward ReLU 1×, feedforward linear 200×). But the system generates 85-97% fewer LLM tokens. At 95% token reduction: 0.05 × 150 = 7.5× the total forward pass computation of conventional. Net cost ~10× for a single turn. But VDR's per-turn cost is flat (state in KBs) while conventional grows quadratically (re-reading growing history). The wall-clock crossover favors VDR from turn 7-10 onward for a 7B model, earlier for larger models.

The SRE case study validates this end-to-end: 1MB Prometheus JSON with 200 endpoints and 18,000 metric values. Conventional: 10,100 tokens generated, ~11 minutes wall-clock, 25% data coverage (context overflow), arithmetic errors, no persistence. VDR: 769 tokens, ~9 seconds wall-clock, 100% data coverage, exact arithmetic, full versioned project with comparison rules for future investigations. 73× faster. 71× cheaper including human time ($0.39 vs $27.58). The second run on a similar incident is 42% cheaper than the first because accumulated project-level rules and scripts handle known patterns automatically.

![Fig. 3](./figures/vdr_system_03_scaling_quadratic_vs_flat.png)

**Self-Extension: Usage Is Training**

The system's knowledge base, rule set, and executable capabilities grow as a natural byproduct of doing work. When the LLM investigates an SRE incident, it writes Prolog rules encoding correlation patterns it discovered, Python scripts for analysis it performed, and stores findings as provenanced facts. All persist, compose with prior state, and are available to every future session with scope access.

This accumulation has properties that weight-based training cannot provide. It is immediate - one fact assertion and the knowledge is live, no batch process. It is inspectable - every rule is a readable Prolog clause with provenance. It is reversible - retracting a fact removes it cleanly, unlike weight poisoning. It is scoped - knowledge in one project doesn't leak to another. It is incremental - the 500th document builds on the rule base from the first 499 without catastrophic forgetting, because facts sit at integer addresses rather than weight matrices.

A Prolog rule costs 25-40 tokens to formalize and assert. On first use it replaces 150-300 tokens of conventional LLM reasoning. By the fifth use the amortized cost is negligible. At organizational scope with thousands of reuses, per-use cost approaches zero. Every rule written is an investment that compounds across all future work within scope.

The compaction format adjusted in VDR-19 aligns with three targets simultaneously: Prolog clause syntax (directly loadable), predicate-major columnar GPU storage (directly parseable into the storage format), and Zig struct definitions (directly mappable to implementation types). A compacted document is a load file. No transformation logic, no interpretation, no LLM involvement in loading.

![Fig. 4](./figures/vdr_system_04_sre_accumulation.png)


**Operational Deployment: Four Prompt Runner Types**

VDR-20 specifies how to actually run this system. Four types of LLM instances, all using the same VDR architecture, differentiated only by trigger pattern and grant scope:

Interactive runners: human-facing, activate on user input, inherit authenticated user grants, reactive, idle between interactions. Typical tokens per activation: 50-500.

Polling runners: timer-driven, spawn fresh each cycle, check queues and counters and directory watch lists, route work, terminate after cycle. Fresh LLM every cycle - no attention degradation. Typical tokens: 10-50.

Processor runners: maintain persistent data connections (streams, webhooks, file watchers), long-lived with periodic respawn at configurable turn thresholds, compact and store data in real time. Typical tokens: 8-30 per item.

Internal processing runners: self-directed, evaluate KB state on schedule, run consistency checks, compute derived facts, identify coverage gaps, produce coverage metrics. Read-broad, write-derived-only. Typical tokens: 20-100.

The owner-local interface is filesystem directories watched by pollers: /vdr/ingress/ (owner drops files for compaction), /vdr/tasks/ (owner drops task specifications), /vdr/config/ (configuration changes), /vdr/output/ (system deposits results), /vdr/review/ (items needing owner judgment), /vdr/manifests/ (processing records).

The coverage loop makes self-extension into self-training. The owner specifies topics and depth targets as KB facts. Rules define what coverage means - measurably, in terms of API surface covered, concept relationships mapped, common patterns encoded. Internal processing runners evaluate KB state against coverage rules and produce a coverage metric where the Remainder is operational - it doesn't say "87% done," it says specifically what's missing. Each gap is a queryable fact with enough specificity to become a fetch task. Polling runners convert gaps to fetch tasks. Processor runners fetch and compact. Internal processors re-evaluate. The loop continues until targets are met.

Token efficiency improves monotonically: 180 tokens per compaction at hour 2, down to 18 at day 30. Rule-handled percentage: 15% at day 1, 88% at month 1. Owner time investment: 2-4 hours per week initially, 0.25-0.5 hours per week at month 6.

The grant matrix is tight: polling runners can't do network fetch, internal processors can't touch the filesystem, processors can't retract rules, nobody can modify grants except the owner with admin grants. Cross-runner collusion cannot bypass security because per-session visibility checks run on every fact access regardless of which runner initiated the query.

Concurrency requires no locking. Append-only arenas mean reads and writes don't contend. Atomic queue operations mean separate read and write positions. Snapshot consistency means readers see a coherent state without blocking writers. This falls out naturally from the integer-addressed, append-only storage design.

**The Implementation Blueprint: Five Stages**

Stage 1 (Toy Full Lifecycle): 24 modules, ~161 builtins, ~2,800 lines, 150 tests. Creates KBs, asserts and queries facts, runs Prolog rules with unification and backtracking, does exact VDR arithmetic, manages counters and locks and queues and stacks, executes one complete lifecycle pass from initialization through training to checkpoint to evaluation to report.

Stage 2 (Upgraded Toy): 37 modules, ~300 builtins, ~3,200 lines, 200 tests (350 cumulative). Command tokens replace API calls. Path addressing with integer ID acceleration. Scope resolution with topic switching. Constraints fire on violations. Scratchpad. Active arithmetic. Linear algebra. Statistics. Graphs.

Stage 3 (Capacity Building): 49 modules, ~400 builtins, ~3,000 lines, 250 tests (600 cumulative). Session snapshots and clones. Inference notebooks with the assess-formalize-execute-store loop. Q-basis transcendentals. Functional remainders. Discrete calculus. Domain math (polynomial, finite field, Markov, graph). Denominator management. Mount system.

Stage 4 (Full Integration): 58 modules, ~437 builtins, ~3,500 lines, 300 tests (900 cumulative). Sandboxed local environments. Filesystem, network, and process operations. Positive credential grants. All four inference modes. The lifecycle pipeline from data sourcing through evaluation.

Stage 5 (Production Completion): 65 modules, 448 builtins, ~3,000 lines, 350 tests (1,250 cumulative). Docker, SSH, and VM environments. Compilation and linting. Feedback collection, reward models, and DPO. Deployment with canary and rollback. Monitoring and drift detection. Retirement and audit archival.

12 architectural layers with strict dependency ordering. ~20,500 total lines (15,500 new + 5,000 existing VDR-4 code wrapped in IOSE declarations without modification). Cross-stage invariants enforced at every stage: every function has IOSE declaration before implementation, no floats in computation path, all persistent state in KBs, all data primitives enforce capacity bounds, all precision reductions declared with exact error bounds, all tests from all prior stages continue to pass.

Python 3.8 prototype first, validating design decisions. Zig port guided by IOSE interface contracts - each IOSE declaration maps directly to a Zig function signature with error unions. Key Zig performance decisions: KB fact storage with hash index on predicate (O(1) average vs O(n) linear scan), string interning with integer handles (enables integer comparison), stack-allocated scope chains as [16]i32 arrays (max depth 16 from VDR-8, avoids allocation), arena allocators for snapshots (efficient bulk allocation and deallocation).

**What This System Is**

A hybrid architecture where the LLM generates only judgment tokens and prose tokens while exact integer primitives handle computation, state management, formatting, and logical deduction. Data lives in knowledge bases at integer addresses. The LLM references data by typed paths and integer identifiers - it never ingests data through its token stream. Every value carries provenance. Every operation is logged. Every conclusion is traceable. Safety and alignment are structural consequences of how the system is built, not behavioral overlays that can be bypassed. The system gets smarter through use because every session deposits rules, scripts, and facts that make future sessions cheaper and more capable. The conventional distinction between training time and inference time dissolves.

**What This System Is Not**

It does not replace real numbers or continuous calculus. It produces exact rationals and exact rational approximations to irrationals - discrete exact arithmetic, not continuous analysis. It is not yet practical at production scale - denominator growth, computational overhead versus hardware float, and the fact that only a Python prototype exists. The Zig port and GPU implementation are specified but not built. Correct conclusions are not guaranteed - premises may be wrong, evidence incomplete, external data stale, LLM orchestration poor. What is guaranteed: failures are detectable through the provenance chain, not preventable by the architecture. The system makes costs visible and honest. It never silently produces garbage.
