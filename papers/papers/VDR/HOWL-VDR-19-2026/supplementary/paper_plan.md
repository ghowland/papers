# VDR-19 PLAN — SELF-EXTENDING ARCHITECTURE

## Paper scope

VDR-19 describes how a VDR system bootstraps from an initial seed, extends itself through normal usage, and accumulates capability monotonically over time. It covers the bootstrap pipeline, the operational lifecycle, the compaction format as a bridge between conventional LLM prose and VDR's typed storage, and the LM's role as a runtime programmer — writing Prolog rules and Python scripts that become permanent infrastructure.

This paper introduces no new primitives, builtins, struct fields, or modules. Everything described uses existing VDR-1 through VDR-18 components.

---

## Section plan

### Section 1 — What self-extending means

Brief introduction for new readers. VDR is a hybrid architecture where an LLM generates only judgment and prose while exact primitives handle computation, state, formatting, and deduction at integer addresses. The LM emits structured command tokens (~8 tokens each) that invoke primitives over data it references by path or ID but never processes through its token stream.

Self-extending: the system's knowledge base, rule set, and executable capabilities grow as a natural byproduct of usage. The LM writes Prolog rules, Python scripts, and KB facts while doing work. Those persist, compose with prior state, and are available to all future sessions within scope. Using the system trains the system.

Key properties to establish: accumulation is immediate (no batch retraining), inspectable (readable rules and provenanced facts), reversible (retract removes cleanly), scoped (knowledge doesn't leak across visibility boundaries), and incremental (no catastrophic forgetting — facts at integer addresses, not distributed across weights).

### Section 2 — The compaction format

Brief intro: conventional LLM output is 80–95% infrastructure tokens — formatting, hedging, state reconstruction, arithmetic. Compaction strips infrastructure while preserving all named entities, properties, and relationships in a structured tabular form.

Describe the current compaction format: pipe-delimited tables, ID-prefixed rows, typed relationship tables, decode legends, section indexes. Show how this is structurally close to KB facts and Prolog rules — each row is a fact, each relationship entry is a rule, each table is a predicate-major column group.

Introduce the adjusted compaction format: modifications to align with Prolog clause syntax, columnar storage layout (predicate-major as specified in VDR-18 C4), and direct parseability into Zig/Python structs. The adjusted format is a direct load file — parse and store, no transformation.

Provide a worked example: one section from a VDR paper in current compaction format, then the same section in adjusted format, then the resulting KB facts and Prolog rules after loading.

### Section 3 — The bootstrap pipeline

Brief intro: the system needs an initial seed of operational competence before it can self-extend. The seed is not domain knowledge — it is the ability to read, write, parse, compose, and manage its own structures.

**Seed layer 1 — Language.** English sentence structure templates (grammar library for output generation). Typo correction KB (pattern-to-correction mappings). Input classification KB (pattern-to-tag mappings for session scoring and routing). These enable the system to read user input and generate grammatically correct output without full-vocabulary token prediction for structural tokens.

**Seed layer 2 — Format handling.** Grammars for JSON, CSV, markdown, pipe-delimited tables, the compaction format itself. Input parsing grammars and output generation grammars for every standard data format. These enable data ingestion and export.

**Seed layer 3 — Operational environment.** Rules for primitive composition — which builtins to call for which tasks, how to sequence pipeline stages, when to write a Prolog rule versus store a flat fact, how to manage queues, counters, LRU caches, ring buffers, stacks. The primitives exist as executable code; the operational KB is the knowledge of how and when to compose them. Includes rules for the compaction process itself — how to identify named entities, relationships, and structure in incoming documents and map them to KB facts and Prolog rules.

**Seed layer 4 — Self-maintenance.** Rules for grammar creation when encountering novel structure. Rules for detecting when a new compaction pattern is needed. Rules for project lifecycle management — snapshot, clone, version, compare.

Describe the staged bootstrap: conventional LLM compacts seed documents → parsed into KBs → system begins operating → initially depends on external LLM for new document compaction → accumulates enough compaction rules to self-compact → conventional LLM no longer needed.

### Section 4 — The operational lifecycle

Brief intro: once bootstrapped, the system operates in a continuous cycle of intake, processing, rule generation, and accumulation.

**Intake.** Documents enter through web fetch, paste, upload, or API. The system compacts them using accumulated grammars and classification rules — identifying named entities, relationships, structure, mapping to KB facts and Prolog rules. Each document is stored with full provenance (source, time, original format, conversion method).

**Processing.** The LM queries existing KBs, existing Prolog rules fire against new facts, contradictions and confirmations surface automatically through rule evaluation. The LM makes judgment calls — what matters, what to investigate, what to flag.

**Rule generation.** The LM writes new Prolog rules encoding discovered relationships, classifications, patterns. It writes Python scripts for analysis that primitives can't handle directly. Both persist in project KBs with provenance.

**Accumulation.** Facts, rules, scripts, grammars, and project state accumulate monotonically within scope. Session state promotes to project state through explicit LM judgment (this finding is worth keeping). Project state is available to all future sessions with scope access.

**Versioning.** Project state snapshots at meaningful points. Comparison rules (written by LM, stored as Prolog) can diff current state against prior snapshots. Second run on similar work is cheaper because accumulated rules and scripts already exist (VDR-18 CL10 — 42% cheaper on second run).

### Section 5 — The LM as runtime programmer

Brief intro: the LM doesn't just call primitives. It writes new rules and scripts that extend the system's capability. This is the mechanism behind self-extension.

**Writing Prolog rules.** The LM emits command tokens to assert new Prolog rules into KBs. These rules are immediately available to the frontier-based GPU evaluator (VDR-18 C6). They compose with all existing rules and facts within scope. Examples: correlation rules from an SRE investigation, classification rules from document analysis, constraint rules from legal review.

Prolog rule amortization: rules written once, reused across all future queries within scope. Cost approaches zero with use (VDR-15 PC1–PC5). Rules at organizational scope reused across all projects.

**Writing Python scripts.** The LM writes Python scripts for analysis that requires procedural logic beyond what Prolog rules express naturally. Scripts execute in sandboxed Docker containers. Results return as typed values stored in KB with provenance. Scripts persist in project KBs and can be re-executed on new data.

**Writing grammars.** When the LM encounters a novel document structure, it can write a new grammar for that format. The grammar persists and handles all future documents of that type without LM involvement.

**Writing compaction rules.** As the system processes more documents, the LM writes rules about how to compact specific document types — which entities to extract, which relationships to encode, which structure to preserve. These rules enable self-compaction of future documents of the same type.

### Section 6 — The SRE operational environment

Brief intro: SRE incident investigation as a concrete demonstration of self-extending architecture. References VDR-15 UC1 and VDR-18 CS1–CS7 for token economics and performance data.

Walk through a first SRE investigation on a fresh system:
- LM queries Prometheus API (credentialed, positionally constrained)
- Response routes to KB target, never through LM token stream
- LM commands JSON parsing, filtering, sorting via primitives
- LM writes Python script for anomaly analysis, runs in Docker, results to KB
- LM writes Prolog correlation rules encoding discovered patterns
- LM stores project state with versioning
- LM generates formatted output via grammar templates

Walk through the second investigation on the same system:
- Prior correlation rules fire automatically against new data
- Prior Python scripts re-execute on new metrics
- Prior filtering and sorting patterns already in operational KB
- LM judgment focuses on what's new/different, not rebuilding infrastructure
- 42% fewer tokens (VDR-18 CL10) because accumulated rules and scripts handle known patterns

Walk through the tenth investigation:
- Comprehensive rule base covers common failure patterns
- Novel incidents still require LM judgment but routine triage is largely automated
- Project KB contains full history, queryable, provenanced
- New engineer on the team inherits all accumulated rules and scripts through scope access

### Section 7 — Data flow architecture

Brief intro: in VDR the LM orchestrates by reference. Data stays at integer addresses in KBs, queues, caches, buffers. The LM points at data with dotted paths and IDs. It never ingests data to manipulate it.

Describe the zero-copy data flow:
- External data → primitives → KB facts at integer addresses
- LM emits command tokens referencing paths/IDs
- Primitives operate on data at those addresses
- Results written to KB at new addresses
- LM receives typed summaries, not raw data
- Output generated via grammar templates pulling values from KB addresses

Contrast with conventional: data enters context window as tokens, LM processes by attention, results generated as tokens, state lost between turns. VDR: data enters through primitives, lives at addresses, LM orchestrates by reference, state persists indefinitely.

Queue-based multi-instance orchestration: one LM instance writes findings to KB, puts summary on queue. Another instance picks up from queue with full provenance, continues work. Each instance stays fresh (clone economics from VDR-15 CL1–CL4). Knowledge accumulates across instances.

### Section 8 — Train-as-you-go

Brief intro: the conventional distinction between training and inference dissolves. Using the system extends its knowledge and inference capability continuously.

Properties of live training vs weight-based training:
- Immediate (no batch process, no gradient computation — one kb_assert and it's live)
- Inspectable (every rule is a readable Prolog clause, every fact has provenance)
- Reversible (retract removes cleanly — no weight poisoning)
- Scoped (knowledge in one project doesn't leak to another — visibility and scope gates apply)
- Incremental (document 500 builds on documents 1–499 — no catastrophic forgetting)
- Auditable (full provenance chain on every fact and rule)
- Composable (rules from different sources interact through Prolog unification automatically)

Describe the accumulation curve: early sessions are mostly LM judgment writing foundational rules. Later sessions increasingly trigger existing rules with LM judgment focused on novel cases. The ratio of LM tokens to accumulated-rule evaluations shifts over time — the system does more per LM token as it accumulates.

### Section 9 — Capability growth model

Brief intro: quantify how the system's capability grows with usage.

Metrics:
- KB facts (total stored, queryable)
- Prolog rules (total, by scope level — project, department, organization)
- Python scripts (total, re-execution count)
- Grammars (total, documents parsed per grammar)
- Compaction rules (total, documents compacted per rule)
- Session-over-session token reduction (each session cheaper than prior for similar work)

Project illustrative growth curves for SRE use case:
- Investigation 1: ~100 facts, ~15 rules, ~3 scripts
- Investigation 5: ~300 facts, ~40 rules, ~8 scripts, measurable token reduction
- Investigation 20: ~800 facts, ~80 rules, ~15 scripts, routine triage largely automated
- Investigation 50: comprehensive domain KB, novel incidents only require LM judgment for genuinely new patterns

### Section 10 — Security properties of self-extension

Brief intro for new readers: VDR enforces access control structurally through KB visibility (public/internal/owner_only), scope chains (sibling branches unreachable), grants (default denial on all operations), and output constraints (grammar validation post-generation). These are described fully in VDR-16.

Self-extension inherits all security properties:
- Rules written by LM are stored in KBs subject to the same visibility and scope controls as any other fact
- A rule in project A cannot reference or query facts in project B unless scope permits
- Python scripts execute in sandboxed containers with grant-gated filesystem access
- Accumulated knowledge respects the same access boundaries as seeded knowledge
- Self-generated rules carry provenance identifying the session, user, and turn that created them
- Retraction of self-generated rules follows the same audit trail as any other KB modification

No new attack surface: the LM writes rules and scripts through the same command token → primitive → grant check pipeline as every other operation. Self-extension doesn't bypass access control because it uses the same access-controlled mechanisms.

### Section 11 — Language and dialect as KB selection

Brief intro: the LM's judgment about what to say is decoupled from how to say it in a particular language or register.

The LM emits a semantic tuple — subject, verb, object, location, weight criteria — as command tokens. Prolog rules match against sentence structure templates in the mounted language/dialect KB. The template provides all structural tokens. Content words fill typed slots.

Switching language or dialect is a scope change — mount a different KB. No model fine-tuning, no prompt engineering. Consistent dialect throughout a document because structural rules are deterministic. Mix dialects intentionally by switching mounted KB per output segment (narrator vs dialogue).

This falls out of self-extension naturally: sentence template KBs are just another accumulated knowledge base, written and refined through usage, scoped and versioned like everything else.

### Appendices plan

- AppA: Compaction format specification (current → adjusted → load format)
- AppB: Seed layer contents (itemized per layer)
- AppC: Bootstrap stage transitions (criteria for advancing from stage N to N+1)
- AppD: SRE worked example (three investigations showing accumulation)
- AppE: Prolog rule amortization curves (from VDR-15 PC1–PC5 contextualized for self-extension)
- AppF: Python script lifecycle (write → sandbox → execute → store → re-execute)
- AppG: Queue-based multi-instance coordination
- AppH: Capability growth metrics (projected curves per use case)
- AppI: Security properties of self-generated rules
- AppJ: Language/dialect KB structure
- AppK: Compaction rules as self-extending grammar

---

## Dependencies

References VDR-15 for token economics, primitive patterns, clone model, Prolog rule amortization. References VDR-16 for security model (visibility, scope, grants, constraints, audit). References VDR-17 for alignment properties (credential model, session scoring, clean denial). References VDR-18 for GPU implementation (forward pass, concurrent streams, SRE case study performance data). Each reference introduced briefly for readers who haven't read the referenced paper.

## Key claims to establish

1. Self-extension is a consequence of the architecture, not a feature added to it
2. The compaction format bridges conventional LLM prose and VDR typed storage
3. The bootstrap requires only operational competence, not domain knowledge
4. Usage is training — the conventional distinction dissolves
5. Capability growth is monotonic, inspectable, reversible, and scoped
6. Self-extension inherits all security and alignment properties from the underlying architecture
7. The LM's role shifts from doing work to programming the system that does work
8. Multi-instance orchestration through queues enables horizontal scaling of self-extension
