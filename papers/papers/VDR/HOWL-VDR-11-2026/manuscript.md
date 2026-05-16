# Implementation Blueprint
## Five-Stage Build Plan for VDR-LLM-Prolog

**Registry:** [@HOWL-VDR-11-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → [@HOWL-VDR-3-2026] → [@HOWL-VDR-4-2026] → [@HOWL-LLM-1-2026] → [@HOWL-VDR-5-2026] → [@HOWL-VDR-6-2026] → [@HOWL-VDR-7-2026] → [@HOWL-VDR-8-2026] → [@HOWL-VDR-9-2026] → [@HOWL-VDR-10-2026] → [@HOWL-VDR-11-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** May 2026

**Domain:** Applied Philosophy / Systems Engineering / Implementation Planning

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

**Supplementary Materials:**
- `supplementary/function_iose_5_stages_spec.md` — Complete function-level IOSE specification for all 65 modules across 5 stages, with inputs, outputs, side effects, and properties declared for every function.
- `supplementary/iose_spec_depth.md` — Full data structure definitions (dataclasses, enums), module map, file layout, line count estimates, Zig port strategy, and stage deliverable tables.

---

## Abstract

Ten papers specified the VDR-LLM-Prolog system. VDR-10 provided the engineering foundation — the IOSE system model, operational principles, and comprehensive numeric builtins. This paper specifies how to build it.

The system is built in five stages, each producing a complete, testable, runnable system that handles a full lifecycle at its level of capability. Stage 1 is a toy that can create knowledge bases, assert and query facts, run Prolog rules, perform exact arithmetic, and demonstrate one training-evaluation cycle. Stage 2 adds command tokens, path addressing, scope resolution, constraints, and the scratchpad. Stage 3 adds session management, inference notebooks, Q-basis transcendentals, functional remainders, and domain-specific mathematics. Stage 4 adds operational environments, grants, filesystem and network operations, all four inference modes, and the lifecycle pipeline. Stage 5 completes the system with Docker and SSH environments, compilation, linting, feedback collection, deployment, monitoring, canary deployment, and retirement.

The build uses Python 3.8 as the prototype language, leveraging the existing VDR-1 through VDR-4 codebase (~5,000 lines of tested exact arithmetic, linear algebra, and ML stack code). New code is approximately 15,500 lines across 65 modules. Every function has an IOSE declaration — inputs, outputs, side effects, and properties — which simultaneously serves as the test specification, the documentation, and the interface contract for the eventual Zig 0.15.1 production port.

The central claim is that a system specified by ten papers, governed by operational engineering principles, and built in disciplined stages with IOSE declarations at every function is not a research prototype — it is an engineering project with a concrete, executable build plan.

---

## 1. Context: From Specification to Construction

### 1.1 What Has Been Specified

The VDR-LLM-Prolog system has been specified across ten papers:

**Exact arithmetic** (VDR-1 through VDR-4). Every number is an integer triple [V, D, R] — value, denominator, remainder. 705 tests across 23 mathematical domains, zero VDR computation errors. A working transformer with exact softmax, exact autodiff, and exact training.

**Knowledge architecture** (VDR-5). Everything stored in Knowledge Bases — facts, rules, constraints organized in a scoped tree. User accounts as KBs. Organizational hierarchy as the tree structure.

**Execution layer** (VDR-6). 255 deterministic primitives invoked through compact command tokens. Sandboxed operational environments. Positive credential grants.

**Lifecycle** (VDR-7). The complete model lifecycle — data sourcing through retirement — as KB operations.

**Runtime state** (VDR-8). Data primitives (LRU caches, counters, locks, queues, stacks, ring buffers, bitsets) as fields on the KB struct. Universal dotted-path addressing with integer ID acceleration. Session snapshots and disposable cloning.

**Orchestrated Inference** (VDR-9). The pattern by which the LLM composes tools into multi-step investigations with four inference modes, notebooks, provenance, and confidence propagation.

**Engineering foundation** (VDR-10). The IOSE system model for all components. Fifteen operational engineering principles as enforceable Prolog rules. 448 comprehensive builtins with full VDR-1 through VDR-3 mathematical capability.

### 1.2 What This Paper Provides

A build plan. Not a wish list — a concrete, staged, module-by-module, function-by-function plan for constructing the system. Every module has a stage assignment. Every function has an IOSE declaration. Every stage has a test count target and a defined capability level.

The complete function-level specification lives in the supplementary materials. This paper describes the architecture, the staging strategy, the key design decisions, and the integration points. It does not reproduce the supplementary specifications — it explains them.

---

## 2. Build Philosophy

### 2.1 Comprehensive Then Incremental

The specification is comprehensive — ten papers define the whole system top-down. The build is incremental — five stages, each producing a testable system. At no stage is the system aggregated in the OSO sense (C18). Each stage is a complete, internally consistent system that handles a full lifecycle at its level of capability. Stage 1 handles a toy lifecycle. Stage 5 handles production. But even Stage 1 has KB creation, fact assertion, rule evaluation, exact arithmetic, and a training-evaluation loop.

### 2.2 Python First, Zig Final

Python 3.8 is the prototype language. It has the existing VDR-1 through VDR-4 codebase — vdr.py, active_mul.py, fn.py, linalg.py, and nineteen other modules totaling approximately 5,000 lines of tested, working code. The prototype validates every design decision in a language where iteration is fast and debugging is straightforward.

The production implementation will be Zig 0.15.1. The port is mechanical because the IOSE declarations define the interfaces — same inputs, same outputs, same side effects, same properties. Python dataclasses map to Zig structs. Python dicts map to Zig HashMaps. Python lists map to Zig ArrayLists. Python enums map to Zig enums. The prototype is designed for portability from the start.

The Zig port happens after Stage 5 validates the complete system in Python. The IOSE declarations serve simultaneously as: the Python function signatures, the test specifications, the documentation, and the Zig interface contracts.

### 2.3 IOSE At Every Function

Every function in the system — from `vdr_add` to `create_deployment` to `session_clone` — has an IOSE declaration before it has an implementation. The declaration states what goes in, what comes out, and what else changes. This discipline starts at Stage 1 and never relaxes.

The IOSE declaration is the test specification. To test a function: provide the declared inputs, verify the declared outputs, confirm the declared side effects occurred, and verify the declared properties hold (determinism by running twice and comparing, idempotency by running the output through the function again, commutativity by swapping arguments).

### 2.4 Existing Code Integration

The VDR-1 through VDR-4 codebase is not rewritten. It is wrapped. The existing `VDR` class in `vdr.py` becomes the implementation behind the `vdr_add`, `vdr_mul`, `vdr_div` builtins. The existing `Vec` and `Mat` classes in `linalg.py` become the implementation behind the linear algebra builtins. The existing `softmax` function becomes the implementation behind `vdr_softmax`. The wrapping layer adds IOSE declarations, type dispatch, and error handling via the Result type. The core mathematics is proven — 705 tests — and is not touched.

---

## 3. Module Architecture

### 3.1 Ten Layers

The system organizes into ten layers, each a directory containing related modules:

**core/** — The existing VDR arithmetic library plus new type dispatch and error handling. This is the mathematical foundation. Five existing modules (vdr.py, active_mul.py, fn.py, linalg.py, export.py) plus two new modules (types.py, errors.py).

**kb/** — The Knowledge Base engine. KB struct, fact storage, Prolog-style rule engine with unification and backtracking, constraint checking, scope resolution, working data bindings. Six modules.

**path/** — The universal addressing system. Path-to-integer registry, dotted path resolution with relative paths, mount system with cycle detection. Three modules.

**primitives/** — All 448 builtins as IOSE-declared functions. Organized by category: text, collections, arithmetic, comparison, rounding, number theory, linear algebra, statistics, probability, conversion, time, identity, graphs, logic, integer operations, active arithmetic, structure operations, Q-basis, functional remainder, discrete calculus, denominator management, polynomial, finite field, Markov, graph math. Twenty-eight modules.

**data_primitives/** — Runtime state data structures. Counter, lock, queue, stack, LRU cache, ring buffer, bitset. Each module provides the IOSE-declared functions that operate on the corresponding data structure within a KB. Seven modules.

**command/** — Command token parsing and execution. Token type definitions, stream parser, dispatch executor, scratchpad. Four modules.

**session/** — Session state management. Snapshot capture and restore, clone creation and destruction, lifecycle operations (reset, diff, info). Three modules.

**inference/** — Orchestrated Inference. Notebook creation and templating, the assess-formalize-execute-store loop, the four inference modes (deductive, inductive, abductive, analogical), confidence propagation, provenance tracking and challenge mechanism. Five modules.

**env/** — Operational environments. Abstract base interface, local execution, Docker container management, SSH remote execution, VM management. Five modules.

**ops/** — Operational primitives. Filesystem operations, script execution, compilation, linting, network operations, process management, grant verification. Seven modules.

**lifecycle/** — Model lifecycle management. Data pipeline (source registry, corpus preparation, tokenization), training orchestration, evaluation, feedback collection, deployment, monitoring. Six modules.

**iose/** — IOSE infrastructure. Declaration registry, chain validation, and OSO principle loading. Three modules.

Total: 65 modules across 12 directories (including tests/).

### 3.2 Dependency Flow

The layers have a strict dependency order. Lower layers never import from higher layers.

```
core (no dependencies)
  ↓
kb (depends on core)
  ↓
path (depends on kb)
  ↓
data_primitives (depends on kb)
  ↓
primitives (depends on core, kb)
  ↓
command (depends on primitives, path, kb)
  ↓
iose (depends on kb, primitives)
  ↓
session (depends on kb, data_primitives, path)
  ↓
inference (depends on kb, primitives, command, session)
  ↓
env (depends on kb, command)
  ↓
ops (depends on env, kb, command)
  ↓
lifecycle (depends on ops, kb, primitives, inference)
```

This ordering means Stage 1 (core + kb + primitives + data_primitives + iose) has no upward dependencies. Each subsequent stage adds layers that depend only on layers from the current or earlier stages. No circular dependencies. No forward references.

---

## 4. The Five Stages

### 4.1 Stage 1: Toy Full Lifecycle

**Capability:** Create KBs, assert and query facts, run Prolog rules with unification and backtracking, perform exact VDR arithmetic, use counters/locks/queues/stacks, and demonstrate one complete lifecycle pass: initialize model → train one step → checkpoint → evaluate → report. Everything works. Nothing is fast. Nothing scales. The full loop exists.

**Modules:** 24 total.

The core layer copies in the existing VDR-4 codebase (vdr.py, active_mul.py, fn.py, linalg.py) and adds types.py for the number type hierarchy and dispatch, and errors.py for the Result wrapper.

The kb layer introduces the KB struct with all 25 fields from VDR-10, the fact store with idempotent assertion and retraction, the Prolog rule engine with unification over atoms, variables, VDR fractions, and lists, and working data bindings with parent-chain inheritance.

The primitives layer introduces the first wave of builtins: closed arithmetic (8 builtins wrapping vdr.py), comparison (10), rounding and extraction (7), list aggregates (8), text operations (17), collection operations (36), set operations (14), mapping operations (15), conversion operations (14 including the critical conversion boundaries), logic operations (11), and integer fast path with bit operations (21). Approximately 150 builtins active.

The data_primitives layer introduces counter, lock, queue, and stack — the four simplest runtime state structures. Each has a module with IOSE-declared functions for create, read, write, and query operations.

The iose layer introduces the builtin registry (register, lookup by ID and name, category listing) and the OSO principles KB loader (15 axioms, core knowability facts, priority rules).

**The toy lifecycle:**

```python
# 1. Create KB tree
root = create_kb("root", "root")
model = create_kb("model", "root.model", parent_id=root.id)
train = create_kb("train", "root.train", parent_id=root.id)

# 2. Assert architecture
assert_fact(model, Fact("hidden_dim", [2]))
assert_fact(model, Fact("vocab_size", [3]))

# 3. Initialize weights (wrapping VDR-4 init.py)
weights = initialize_model(model, seed=42)

# 4. Train one step (wrapping VDR-4 trainer.py)
train.counters["step"] = Counter(min_value=0)
loss = train_step(model, train, batch, lr=VDRFraction(1, 1000, 0))
train.counters["step"].inc()

# 5. Checkpoint
checkpoint = create_checkpoint(model, train, step=1)

# 6. Evaluate
accuracy = evaluate(model, test_data)
eval_kb = create_kb("eval", "root.eval", parent_id=root.id)
assert_fact(eval_kb, Fact("accuracy", [accuracy]))

# 7. Query result
result = query_facts(eval_kb, "accuracy", [None])
```

Every value is an exact VDR fraction. Every fact is in a KB. Every step is logged. The lifecycle is toy-sized but structurally complete.

**Tests:** 150 target. Core arithmetic (30), KB operations (30), data primitives (20), text/collections/sets/mappings (40), lifecycle integration (10), IOSE registry (10), OSO principles (10).

### 4.2 Stage 2: Upgraded Toy

**Capability:** Command tokens replace direct API calls. The system can parse a mixed stream of text and CMD: tokens, dispatch each command to the appropriate builtin, and return results. Path addressing gives every KB a dotted path with integer ID acceleration. Scope resolution enables topic switching — activating a topic makes its KB chain visible and deactivates others. Constraints fire on violations. The scratchpad provides an internal computation channel.

**New modules:** 13 (cumulative 37).

The kb layer gains the constraint engine (evaluate Prolog conditions, enforce violation actions) and the scope resolver (build scope chains by walking parent IDs, scoped query with first-match-wins semantics, scoped binding resolution with inheritance).

The path layer introduces the path registry (assign integer IDs, resolve dotted paths) and the path resolver (parent, children, ancestors, depth, common ancestor).

The command layer introduces command token types, the stream parser (split text from CMD: lines), the executor (resolve paths to IDs, validate types against IOSE declarations, dispatch to builtins), and the scratchpad (a RingBuffer-based internal workspace).

The primitives layer gains the second wave: active arithmetic (5), structure operations (3 — lift, rebase, projection), number theory (13), linear algebra (24 wrapping linalg.py), statistics (16), probability (included in statistics), time operations (10), identity operations (8), and graph algorithms (13). Total builtins reaches approximately 300.

The data_primitives layer gains LRU cache, ring buffer, and bitset — the three remaining runtime state structures.

The iose layer gains the validator (type compatibility checking across chains, side effect preview, post-execution contract verification).

**What changes architecturally:**

The system moves from Python API calls to structured command tokens. The LLM (or test harness) emits `CMD: vdr_add(root.train.loss_step_0, 1/10)` and the executor resolves the path, looks up the data, invokes the builtin, and returns the result. The scratchpad holds intermediate computations. The scope resolver ensures that switching from the training topic to the evaluation topic changes which facts are visible.

Constraints become active. A constraint like `loss_finite` with condition `loss < 1000` is checked after each training step. If violated, the on_violation action fires — which might halt training, log a warning, or escalate.

**Tests:** +200 (cumulative 350). Command token parsing and execution (40), path registry and resolution (30), scope resolver (30), constraint engine (20), new builtins (60), new data primitives (20).

### 4.3 Stage 3: Capacity Building

**Capability:** Session snapshots capture all live state atomically. Clones fork independent sessions from snapshots. Inference notebooks house structured investigations with the assess-formalize-execute-store loop. Q-basis operations manipulate transcendental constants. Functional remainders compute sqrt, exp, log, sin, cos at arbitrary depth. Discrete calculus provides exact derivatives and integrals. Domain-specific math covers polynomials, finite fields, Markov chains, and graph mathematics. Denominator management tracks and controls growth. The mount system allows cross-branch KB references.

**New modules:** 12 (cumulative 49).

The path layer gains the mount system — create mounts with cycle detection, resolve queries through mounts respecting read-only/read-write/snapshot/mirror modes.

The primitives layer gains the third wave: Q-basis operations (7), functional remainder operations (8), discrete calculus (6), denominator management (5), polynomial operations (8), finite field operations (4), Markov chain operations (3), and graph math (2). Total builtins reaches approximately 400.

The session layer introduces snapshot capture and restore, clone creation and destruction, and lifecycle operations (reset, diff, info, list).

The inference layer introduces notebook creation (with template support for common investigation types), the inference loop (assess → formalize → execute → store with budget management and stall detection), confidence propagation (deductive, inductive, abductive, analogical formulas), and provenance tracking (evidence recording, conclusion recording, derivation tracing, challenge mechanism).

**What changes architecturally:**

The system gains memory and recovery. Before Stage 3, a bad state required starting over. Now the system can snapshot a known-good state, experiment, and restore if things go wrong. The disposable clone pattern becomes available — snapshot a stable operator, launch workers from it, kill them when they drift, launch fresh ones.

The system gains investigation capability. An inference notebook formalizes a multi-step investigation with declared goals, resource budgets, and progress tracking. The loop cycles through assessment (what do I know? what's missing?), formalization (write Prolog rules, assemble primitive chains), execution (run the formalized step), and storage (persist results to KB). Budget constraints prevent runaway investigations. Stall detection forces backtracking or conclusion when progress stops.

The system gains the full VDR-1 through VDR-3 mathematical capability. Q-basis lets the system add π + e with one integer addition. Functional remainders let it compute √2 to 150 digits. Discrete calculus lets it take exact derivatives and integrals. Denominator management lets it monitor and control the growth that accumulates through arithmetic operations.

**Tests:** +250 (cumulative 600). Session management (30), inference notebook and loop (40), confidence (20), Q-basis (20), functional remainder (30), discrete calculus (20), domain math (40), mount system (20), denominator management (15), integration (15).

### 4.4 Stage 4: Full Integration

**Capability:** The system can execute code in sandboxed environments (local first), fetch external data via network operations, manage files, run background processes, and authorize everything through positive credential grants. All four inference modes are implemented with their characteristic tool signatures. The lifecycle pipeline handles data sourcing, corpus preparation, tokenization, model initialization, training, checkpointing, and evaluation. The system is functionally complete except for remote environments and production deployment features.

**New modules:** 9 (cumulative 58).

The env layer introduces the abstract environment interface (10 methods that every environment implements) and the local environment (execute via Python subprocess on the host machine, for development and testing).

The ops layer introduces filesystem operations (15 builtins), script execution (5), network operations (5), process management (7), and the grant system (store, verify, use, list effective grants through KB hierarchy).

The inference layer gains the mode implementations — deductive (assert premises and rules, query Prolog for derivation), inductive (gather evidence, write scoring rules, rank hypotheses), abductive (assert observations and causal rules, query for explanations), and analogical (assert source and target domain structures, query for structural mappings).

The lifecycle layer introduces the data pipeline (source registration, corpus preparation with filters, tokenization with vocabulary freezing), training orchestration (model initialization, train step wrapping VDR-4 trainer, checkpoint creation and restoration), and evaluation (benchmark running, eval suite, cross-checkpoint comparison).

**What changes architecturally:**

The system gains hands. Before Stage 4, it could compute and reason but could not interact with the outside world. Now it can read and write files, execute scripts in a sandboxed environment, fetch data from HTTP endpoints, and manage background processes. Every external operation requires a grant — no operation executes without explicit authorization.

The inference system gains its full power. The four modes compose: an investigation might start with abductive inference (what could cause these symptoms?), switch to inductive (score hypotheses against evidence), then deductive (derive implications of the leading hypothesis). The external data integration pipeline from VDR-9 — acquire, parse, convert, store, index, process — is now executable because the network and filesystem operations exist.

The lifecycle pipeline means the system can manage its own training. Initialize a model from a KB architecture specification, train it with exact gradients and exact parameter updates, checkpoint the exact state, and evaluate against benchmarks. The entire pipeline from data source to evaluation result is one KB tree.

**Tests:** +300 (cumulative 900). Grant system (20), filesystem (30), script execution (20), network (15), process management (15), inference modes (40), lifecycle pipeline (60), local environment (20), integration (40), IOSE contract verification (40).

### 4.5 Stage 5: Production Completion

**Capability:** The system is complete. Docker and SSH environments provide production-grade sandboxing and remote execution. Compilation primitives build code in Zig, C, and Rust. Linting primitives analyze code quality. The feedback system collects human preferences and trains reward models. The deployment system manages serving configuration, canary deployment, and rollback. The monitoring system tracks runtime metrics, detects drift, and triggers alerts. The retirement system archives model KBs for long-term audit. Every feature specified in VDR-1 through VDR-10 is implemented.

**New modules:** 7 (cumulative 65).

The env layer gains Docker (container creation, start, stop, destroy), SSH (remote command execution via key authentication), and VM (virtual machine management) environments. All implement the same 10-method interface — the command token executor does not change.

The ops layer gains compilation (4 builtins) and linting (8 builtins).

The lifecycle layer gains feedback collection (pairwise judgment storage, agreement computation, reward model training, DPO alignment), deployment (deployment configuration, canary creation, promotion, rollback), and monitoring (watch creation, metric recording, drift detection).

**What changes architecturally:**

The system gains production readiness. Docker isolation means user-generated Python scripts run in containers, not on the host. SSH means training can happen on GPU clusters. Canary deployment means model updates roll out gradually with automatic rollback on regression. Monitoring means the system tracks its own health.

The feedback loop closes. The deployed model generates responses. Humans judge them. The judgments train a reward model or feed DPO directly. The aligned model is evaluated, canary-deployed, monitored, and — when superseded — retired with its complete KB lineage preserved for audit.

**Tests:** +350 (cumulative 1,250). Docker (40), SSH (30), VM (20), compilation (15), linting (20), feedback (30), deployment (30), monitoring (30), canary and rollback (25), retirement (15), full lifecycle integration (40), end-to-end (25), Zig port preparation (30).

---

## 5. Cross-Stage Invariants

These hold at every stage. They are tested at every stage. They are never relaxed.

**IOSE declared.** Every function has an IOSE declaration before it has an implementation. The declaration is written first. The implementation satisfies it. The test verifies it.

**Exact arithmetic.** Every numeric operation uses VDR fractions or exact integers. No floats anywhere in the computation path. The only place floats appear is at the declared conversion boundary when external data enters the system — and that conversion is logged with an exact error bound.

**KB is truth.** All persistent state lives in KBs. No module globals holding state. No hidden caches. The KB tree is the single source of truth. The OSO principle: the KB is the model for control (C39), not a model for understanding (C38).

**Data primitives bounded.** Every counter, queue, stack, ring buffer, LRU cache, and bitset has a declared maximum capacity. No unbounded growth. The capacity is set at creation and enforced at every mutation.

**No silent truncation.** Every precision reduction is declared with an exact error bound. The VDR system never silently discards information. If a denominator is too large and must be reprojected to Q-basis, the reprojection logs the exact error. If a fraction is displayed as a decimal, the display function is marked lossy and the generating fraction is always available.

**Tests pass.** All tests from the current stage and all prior stages pass. The test suite is cumulative. Stage 3's tests include all of Stage 1's and Stage 2's tests, unchanged and passing.

**OSO principles loaded.** The root.system.oso KB is loaded at startup with all 15 axioms, approximately 80 facts, approximately 60 rules, and 21 constraints. The principles are not documentation — they are active Prolog rules that the inference loop queries and the constraint system enforces.

**Idempotent where declared.** Every operation tagged with the idempotent property verifies f(f(x)) = f(x) in its test suite. Session restore, bitset set, counter set, KB assert of existing fact, lock release on free lock — all tested for idempotency.

**One canonical method.** Each task category has exactly one canonical builtin. There is one way to sort a list, one way to assert a fact, one way to execute code in an environment. The builtin registry enforces uniqueness — no two builtins in the same category perform the same task.

---

## 6. The Existing Codebase

The build does not start from zero. VDR-1 through VDR-4 produced a working Python codebase of approximately 5,000 lines across 24 modules:

**Arithmetic (5 modules):** vdr.py (core triple, closed arithmetic, normalization, equality), active_mul.py (active multiplication and division), fn.py (functional remainders, discrete calculus), linalg.py (Vec, Mat, determinant, inverse, solve), export.py (lossy boundary to float/decimal).

**Transcendental (3 modules):** exp.py (exact fraction exponential), logarithm.py (exact fraction logarithm), basis.py (Q335 shared denominator).

**ML stack (4 modules):** softmax.py (exact softmax, rational surrogate), autodiff.py (reverse-mode exact differentiation), nn.py (linear layers, ReLU, sequential), losses.py (MSE, L1, hinge).

**Infrastructure (8 modules):** optim.py (SGD, momentum), rng.py (deterministic PRNG), init.py (rational initialization), sampling.py (categorical, top-k, nucleus), datasets.py (tokenization, batching), metrics.py (accuracy, denominator tracking), checkpoint.py (exact save/load), tensor.py (batched operations).

**Architecture (4 modules):** attention.py (scores, masking, weighting), transformer.py (embedding, blocks, LM head), trainer.py (training loops).

This code has 705 passing tests with zero VDR computation errors. It is not rewritten. It is wrapped in IOSE-declared builtin functions at Stage 1, then progressively exposed through the command token system at Stage 2.

---

## 7. New Code Estimates

Excluding the existing VDR-4 codebase, the new code breaks down by stage:

**Stage 1: ~2,800 lines.** KB struct and fact store (~350), Prolog rule engine with unification (~400), working data (~100), type hierarchy and dispatch (~200), error types (~50), primitive wrappers for arithmetic, comparison, rounding, aggregates (~400), text/collections/sets/mappings primitives (~900), conversion primitives (~200), logic primitives (~150), integer and bit operations (~150), data primitive functions (~200), IOSE registry (~150), OSO principles loader (~200).

**Stage 2: ~3,200 lines.** Constraint engine (~250), scope resolver (~200), path registry (~200), path resolver (~150), command token types (~80), command parser (~200), command executor (~250), scratchpad (~60), IOSE validator (~200), active arithmetic and structure ops (~220), number theory (~250), linalg builtins (~200), statistics and probability (~400), time operations (~150), identity operations (~120), graph algorithms (~300), LRU/ring/bitset data primitives (~200).

**Stage 3: ~3,000 lines.** Mount system (~200), Q-basis operations (~200), functional remainder operations (~250), discrete calculus (~200), denominator management (~100), polynomial operations (~250), finite field operations (~100), Markov operations (~150), graph math (~100), session snapshot (~200), session clone (~150), session lifecycle (~150), inference notebook (~200), inference loop (~300), confidence propagation (~150), provenance (~200).

**Stage 4: ~3,500 lines.** Environment base interface (~200), local environment (~300), filesystem operations (~300), script execution (~200), network operations (~200), process management (~250), grant system (~200), inference modes (~400), data pipeline (~300), training orchestration (~400), evaluation (~250).

**Stage 5: ~3,000 lines.** Docker environment (~400), SSH environment (~300), VM environment (~200), compilation (~150), linting (~200), feedback collection (~350), deployment (~400), monitoring (~400), retirement (included in deployment).

**Total new code: ~15,500 lines.** Combined with the ~5,000 lines of existing VDR-4 code: approximately 20,500 lines for the complete Python prototype.

---

## 8. The Builtin Registration Pattern

Every primitive module follows the same pattern. This uniformity is deliberate — it makes bulk registration mechanical and ensures no builtin escapes without an IOSE declaration.

The pattern: define a table of (id, name, inputs, outputs, side_effects, properties, description, implementation). Call a registration helper that creates the IOSEDeclaration and BuiltinDef, then adds it to the global registry. One table per module. One registration call per module.

Categories that share identical structure — pure functions with no side effects, same input/output shape — use the same table format. The 17 text builtins, the 36 collection builtins, the 14 set builtins, the 15 mapping builtins, the 10 comparison builtins, and the 8 identity builtins all use the same registration pattern with different tables. The implementation details differ. The registration is uniform.

Categories with KB-internal side effects — data primitives (53 builtins), KB operations (15), path and mount (17), session (8) — use a variant that declares the side effects. The pattern is the same table-driven registration with an additional side_effects column.

Categories wrapping the existing VDR-4 code — closed arithmetic (8), linear algebra (24), statistics (16) — delegate to the existing Python classes. The builtin function is a thin wrapper that converts between VDRFraction dataclasses and the existing VDR class instances.

The operational categories — filesystem (15), compilation (4), execution (5), linting (8), network (5), process (7) — use a pattern that includes grant verification before dispatch. Each function first calls `grant_store.verify_grant(operation_class, operation_type, location, user)` and only proceeds if a valid grant is returned.

---

## 9. The Prolog Rule Engine

The rule engine is the most complex new module in Stage 1. It implements Prolog-style depth-first search with backtracking, supporting unification over five term types:

**Atoms** (strings) unify by equality. "softmax" unifies with "softmax" and nothing else.

**Variables** (strings starting with "?") unify with anything and bind to the matched value. "?X" unifies with "softmax" and binds ?X = "softmax".

**VDR fractions** unify by normalized value equality. [1, 2, 0] unifies with [2, 4, 0] because both equal 1/2. The comparison uses cross-multiplication of exact integers — no floats.

**Lists** unify element-wise. [1, ?X, 3] unifies with [1, 2, 3] binding ?X = 2. Different-length lists do not unify.

**Facts** (predicate + args) unify if predicates match and all arguments unify recursively.

The engine evaluates a goal against a KB's facts and rules. For each fact matching the goal's predicate, it attempts unification. If unification succeeds, the bindings are returned. For each rule whose head matches the goal, the engine recursively evaluates the body goals, threading bindings through. Backtracking occurs when a body goal fails — the engine undoes the most recent choice and tries the next alternative.

The engine has a depth limit (default 100) to prevent infinite recursion. It supports `findall` (collect all solutions) and first-solution-only semantics (cut after first match, used for scoped queries where the first in-scope match wins).

---

## 10. Key Design Decisions

### 10.1 The Result Type

Every function that can fail returns a `Result` — either `Ok(value)` or `Err(VDRError)`. No exceptions for expected failures. Division by zero, missing key, empty list, out of range — these are not exceptional. They are `Err` results with descriptive error codes.

This is an OSO principle in practice: operational logic handles failure explicitly (D4, C31). The Result type makes every failure path visible in the function signature. No hidden exception that might propagate unhandled.

### 10.2 The KB Store

All KBs live in a global store — a dictionary mapping integer IDs to KnowledgeBase instances. The store is the single source of truth. Every function that needs a KB takes the store as a parameter (or accesses it through a well-known path). No KBs exist outside the store.

This is the OSO "model for control" principle (C39). The KB store is the control model. The LLM's context window is the understanding model. When they disagree, the store wins.

### 10.3 Turn Counter

A global turn counter increments with each user interaction. Every mutation (fact assertion, counter increment, lock acquisition) records the turn number. Every snapshot records the turn count. Every evidence record includes the turn when the evidence was acquired. The turn counter is the system clock — it provides total ordering of events without relying on wall-clock time, which may not be deterministic across platforms.

### 10.4 Deep Copy for Snapshots

Session snapshots deep-copy all live state. A snapshot is completely independent of the source — modifying the source after snapshot does not affect the snapshot, and restoring the snapshot does not reference the source. This is essential for the disposable clone pattern: clones must be independent. Python's `copy.deepcopy` handles this in the prototype. The Zig port uses explicit allocation and copy.

### 10.5 Functional Remainder Resolution

Functional remainders (FnRemainder) are not automatically resolved. They sit as callable objects in the remainder slot until `fn_resolve(fn_remainder, depth)` is explicitly called. This is because resolution at different depths produces different exact rationals, and the appropriate depth depends on the application. The LLM or the calling code chooses the depth. The system never silently resolves at an arbitrary depth.

---

## 11. Integration Points Between Stages

### 11.1 Stage 1 → Stage 2

The primitives registered in Stage 1 become dispatchable through command tokens in Stage 2. The executor looks up builtins by name in the registry, resolves path arguments via the path registry, and calls the implementation. No primitive code changes — only the invocation mechanism changes from Python API to command token.

### 11.2 Stage 2 → Stage 3

The scope resolver from Stage 2 gains mount-awareness in Stage 3. When walking the scope chain, if a mount point is encountered, the resolver follows the mount to the source KB (respecting mode restrictions). The query interface does not change — scoped_query still returns facts, but now it can find facts through mounts as well as through the parent chain.

The command executor from Stage 2 gains scratchpad integration in Stage 3. Internal computation results are automatically written to the scratchpad ring buffer. The inference loop reads the scratchpad to see what has been computed in the current turn.

### 11.3 Stage 3 → Stage 4

The inference loop from Stage 3 gains real tool execution in Stage 4. In Stage 3, the `formalize` step is a hook that accepts a callable — test code provides the formalized artifact directly. In Stage 4, the formalize step can generate command tokens that invoke operational primitives — fetch data from a URL, read a file, execute a script. The loop structure does not change. The tool vocabulary expands.

### 11.4 Stage 4 → Stage 5

The local environment from Stage 4 is joined by Docker, SSH, and VM environments in Stage 5. The executor does not change — it calls the same 10-method interface regardless of environment type. The environment selection is a configuration fact in the deployment KB. Switching from local to Docker is a fact change, not a code change.

---

## 12. Test Strategy

### 12.1 Test Layers

**Unit tests** verify individual functions against their IOSE declarations. Input the declared inputs, check the declared outputs, verify the declared side effects, confirm the declared properties. Every builtin has at least 3 unit tests (normal case, edge case, property verification).

**Integration tests** verify multi-function chains. A scoped query that walks the parent chain exercises the fact store, the scope resolver, and the KB store together. An inference loop iteration exercises the notebook, the loop, the command executor, the primitive registry, and the KB.

**Lifecycle tests** verify end-to-end scenarios. The toy lifecycle in Stage 1 (init → train → checkpoint → evaluate → report). The full lifecycle in Stage 5 (source → corpus → tokenize → train → fine-tune → align → evaluate → deploy → monitor → update → retire). Each lifecycle test verifies that the complete chain of KB operations produces the expected KB tree.

**Invariant tests** verify the cross-stage invariants from Section 5. Run at every stage. Confirm IOSE declarations exist for all registered builtins. Confirm no floats in computation paths. Confirm all data primitives respect their capacity bounds. Confirm idempotent operations satisfy f(f(x)) = f(x).

### 12.2 Test Count Targets

| Stage | Unit | Integration | Lifecycle | Invariant | Total | Cumulative |
|-------|------|------------|-----------|-----------|-------|-----------|
| 1 | 120 | 15 | 5 | 10 | 150 | 150 |
| 2 | 160 | 25 | 5 | 10 | 200 | 350 |
| 3 | 200 | 30 | 10 | 10 | 250 | 600 |
| 4 | 230 | 40 | 20 | 10 | 300 | 900 |
| 5 | 260 | 50 | 30 | 10 | 350 | 1,250 |

---

## 13. The Zig Port

The Zig 0.15.1 port happens after Stage 5 validates the complete system in Python. The port strategy:

**Struct mapping.** Every Python dataclass maps to a Zig struct. VDRFraction → `const VDRFraction = struct { v: i128, d: i128, r: Remainder }`. KnowledgeBase → `const KnowledgeBase = struct { ... }` with all 25 fields. The field types map directly: `Dict[str, Counter]` → `std.StringHashMap(Counter)`, `List[int]` → `std.ArrayList(i32)`, `Optional[int]` → `?i32`.

**Enum mapping.** Every Python Enum maps to a Zig enum. `Visibility` → `const Visibility = enum { public, internal, owner_only }`.

**Function mapping.** Every Python function maps to a Zig function with the same IOSE declaration. `def vdr_add(a: VDRFraction, b: VDRFraction) -> VDRFraction` → `fn vdr_add(a: VDRFraction, b: VDRFraction) VDRFraction`. The Result type maps to Zig's error unions: `Result[VDRFraction]` → `fn vdr_div(a: VDRFraction, b: VDRFraction) !VDRFraction`.

**Arbitrary precision.** Python's arbitrary-precision integers map to either Zig's `i128` (sufficient for most operations) with overflow to a BigInt library for operations that exceed 128 bits (Hilbert matrix determinants, Q335 numerators). The overflow boundary is detected and handled explicitly — not silently truncated.

**Test mapping.** Every Python test maps to a Zig test. `test "vdr_add commutative"` verifies the same property with the same inputs and expected outputs. The IOSE declarations are the test specifications — they are language-independent.

The port is mechanical because the IOSE declarations define the interfaces. The Zig implementation satisfies the same contracts. The same tests verify the same behavior. The Zig version runs faster, uses less memory, and has no garbage collection pauses — but it computes the same exact fractions and produces the same results.

---

## 14. Falsification Criteria

**F1.** If any stage produces a system that cannot execute its declared lifecycle capability end-to-end — the toy lifecycle fails in Stage 1, the full lifecycle fails in Stage 5 — the stage is incomplete.

**F2.** If any function is implemented without an IOSE declaration, the IOSE discipline has been violated. Every function must have its declaration before its implementation.

**F3.** If any cross-stage invariant fails at any stage — a float appears in the computation path, a data primitive exceeds its capacity, an idempotent operation is not idempotent — the invariant enforcement has a gap.

**F4.** If the test count at any stage falls below the target, the test coverage is insufficient for the claims made at that stage.

**F5.** If the Zig port of any function produces a different result from the Python prototype for the same inputs, the port has a correctness bug and the IOSE declaration did not adequately specify the behavior.

**F6.** If two stages' tests are incompatible — a Stage 2 change breaks a Stage 1 test — the incremental build discipline has been violated. Tests are cumulative and must never regress.

**F7.** If the supplementary function IOSE specification and the actual implementation disagree on inputs, outputs, or side effects for any function, the specification is the authority and the implementation has a bug.

---

## 15. Conclusion

Ten papers specified what the VDR-LLM-Prolog system does. This paper specifies how to build it.

Five stages. Stage 1 creates a toy with exact arithmetic, knowledge bases, Prolog rules, and a lifecycle loop. Stage 2 upgrades it with command tokens, paths, scoping, and constraints. Stage 3 adds sessions, inference, transcendentals, and domain mathematics. Stage 4 integrates operational environments, grants, external data access, all inference modes, and the lifecycle pipeline. Stage 5 completes the system with Docker, SSH, feedback, deployment, monitoring, and retirement.

65 modules. 448 builtins. Approximately 15,500 new lines of Python, plus 5,000 lines of existing tested VDR-4 code. Every function has an IOSE declaration. Every stage produces a testable, runnable system. Every cross-stage invariant is verified at every stage.

The build is comprehensive (OSO C17) — the whole system is specified before any part is built. The build is incremental (OSO C3) — each stage removes a class of limitation. The build is disciplined (OSO C33) — one canonical method per task, one registration pattern per builtin, one test pattern per function.

The complete function-level IOSE specification is in the supplementary materials. The data structures, enums, and class definitions are in the supplementary materials. This paper is the map. The supplementary materials are the territory.

Build it in stages. Test it at every stage. Port it to Zig when the Python prototype validates every decision. The specification is complete. The plan is concrete. The system is buildable.

---

**END HOWL-VDR-11-2026**

**Registry:** [@HOWL-VDR-11-2026]
**Status:** Specification complete
**Domain:** Applied Philosophy / Systems Engineering / Implementation Planning
**Central Result:** Five-stage build plan from toy to production. 65 modules, 448 builtins, ~20,500 total lines. Every function IOSE-declared. Python 3.8 prototype leveraging existing VDR-4 codebase, with mechanical port to Zig 0.15.1. Supplementary materials contain complete function-level specifications.
**Foundation:** VDR-1 through VDR-10
**Key Principles:** (1) Comprehensive specification before incremental build. (2) IOSE declaration before implementation. (3) Each stage is a complete, testable system. (4) Tests are cumulative and never regress. (5) The Python prototype validates; the Zig port performs.
**Falsification:** Seven criteria covering lifecycle completeness, IOSE discipline, invariant enforcement, test coverage, port correctness, regression prevention, and specification authority.
**Supplementary Materials:**
- `supplementary/function_iose_5_stages_spec.md`
- `supplementary/iose_spec_depth.md`

