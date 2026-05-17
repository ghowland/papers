# HOWL-VDR-24-2026: LM Software
## Configuration and Cloning as Application Development

**Thesis:** LM Software is a new category of software where users develop applications by configuring LLM sessions with structured KB state, encoding logic as Prolog rules over system builtins, validating behavior interactively, snapshotting working state as deployable artifacts, and cloning those artifacts on demand as running instances. The LLM is the runtime. The KB tree is the address space. Prolog is the programming language. Snapshots are the binaries. Usage improves the application without rebuilding it.

---

**Section 1 — The Category**

Define LM Software as distinct from conventional software, AI tooling, and conventional LLM applications. Conventional software is compiled code executing on a CPU — static, requires developers, updated through releases. AI tooling wraps an LLM in conventional software — RAG, LangChain, function calling — where the orchestration is code and the LLM is a component. LM Software is the LLM as the runtime executing structured state that users developed through interaction.

Three defining properties: developed through conversation not code, deployed as snapshots not containers, improved by usage not releases.

**Section 2 — The Development Lifecycle**

Map the conventional software lifecycle onto LM Software. Development is interactive sessions where the user shapes KB state, writes rules, tests against inputs, iterates. Testing is running the session against known cases and verifying outputs. Building is snapshotting the validated session. Deployment is placing the snapshot on a scheduler, trigger, or clone-on-demand system. Monitoring is polling runners checking counters, queue depths, drift metrics. Updating is modifying facts or rules in persistent KBs that all future clones inherit. Retirement is archiving the snapshot KB with full provenance.

No compiler. No IDE. No deployment pipeline. The conversation is the IDE. The snapshot is the binary. The KB tree is the infrastructure.

**Section 3 — KBs as Machines**

Each KB is a machine with 26 typed fields. State: counters, queues, stacks, bitsets, ring buffers, LRU caches, locks. Logic: Prolog rules that fire on conditions. Data: facts at integer addresses with provenance. Constraints: invariants that enforce bounds. Connections: typed relationships to other machines. Visibility: who can interact. Grants: what operations are permitted.

The user wires machines together by placing KBs at paths in the tree and writing rules that reference those paths. A queue at path A, a processor watching path A, results written to path B, a downstream runner watching path B. The topology is the application architecture. The tree is the wiring diagram.

**Section 4 — Prolog as the Programming Language**

Builtins are Prolog predicates. All 448 of them. The user writes Prolog rules that chain builtins into workflows. This is programming — control flow, conditionals, data transformation, I/O — expressed as logic rules over typed predicates with exact arithmetic.

Three execution levels. Full LLM judgment: 50-500 tokens, every step decided at runtime. LLM invoking stored Prolog: 8 tokens per invocation, Prolog executes the chain. Pure Prolog batch: zero LLM tokens, rules fire on triggers, builtins execute, results land at known addresses. The application moves from level one toward level three as rules accumulate.

Dynamic arguments: rules take KB paths as arguments. The logic is static. The data is dynamic. One rule reused across dozens of workflows by pointing it at different KBs. The LLM provides arguments at invocation, or a data KB holds arguments as facts that the rule queries at runtime.

**Section 5 — Snapshots as Binaries**

A snapshot captures all live state atomically. 10-500 KB typically. The persistent KBs it references are not in the snapshot — they're in the tree, shared read-only. The snapshot is the executable. It encodes what the session learned, what rules it wrote, what scope it's configured for, what grammars it has loaded.

Snapshot properties: deterministic (same snapshot produces identical clones), lightweight (state not knowledge), versioned (multiple snapshots of the same application at different development stages), composable (mount additional KBs onto a clone to extend capabilities without modifying the snapshot).

**Section 6 — Cloning as Deployment**

Cloning is instantiation. Each clone is an independent process with identical starting state and independent live state. Clone-per-request for stateless services — customer support, document processing, query handling. Clone-per-task for batch work — file processing pools, data pipeline stages. Long-lived clones with drift thresholds for persistent services — stream processors, webhook handlers.

Drift management: counters track turns, context saturation, denominator drift, error rate. When any threshold fires, kill and reclone from the frozen snapshot. The snapshot never degrades. Clones are disposable. Freshness is guaranteed by policy.

Cross-clone isolation: sibling clones cannot see each other's live state. Structural impossibility, not access control. Each clone's session KB is a separate branch. The scope walk never traverses siblings.

**Section 7 — Runner Types as Application Classes**

Interactive runners are user-facing applications — chatbots, assistants, investigation tools. Polling runners are monitoring and routing applications — health checks, queue managers, schedulers. Processor runners are data pipeline applications — stream processors, file handlers, webhook responders. Internal processing runners are self-maintenance applications — consistency checkers, coverage evaluators, derived fact generators.

Each class maps to conventional software categories. Interactive is a web application. Polling is a cron job. Processor is a stream consumer. Internal is a background service. Same lifecycle, different substrate.

**Section 8 — Inter-App Communication**

Queues for message passing. Counters for coordination and semaphores. Bitsets for barrier synchronization and progress tracking. Locks for signaling. Ring buffers for streaming state. LRU caches for deduplication and memoization. All are KB fields at known addresses. All are accessible through Prolog predicates. All are governed by grants and visibility.

Topology patterns: waterfall (queue chains), fan-out (one queue many consumers), fan-in (many producers one consumer), peer (shared queues), supervisor (counter and bitset monitoring with spawn/kill authority). The user selects the topology by placing data primitives at paths and configuring runners to operate on them.

**Section 9 — The Chatbot as Worked Example**

Walk through the tier 1 support example end to end. Product data loaded into KBs. Runbooks encoded as Prolog rules over builtins. Policies as constraints. Contact information as facts with provenance. Interactive development session testing against customer scenarios. Rule creation for each resolved pattern. Snapshot when behavior is validated. Clone-per-customer deployment. Policy update by changing one fact. No retraining, no redeployment, no prompt engineering.

Contrast with conventional chatbot: prompt template, RAG retrieval, hallucinated details, no state isolation between customers, retraining to update policies, no audit trail, no provenance on answers.

**Section 10 — The File Processing Pipeline as Worked Example**

Walk through the worker pool example. User develops a file processor session. Snapshots it. Deploys 50 worker clones reading from an intake queue. 3 polling clones monitoring queue depth and worker health. Results written to project KB. Accumulated rules improve processing quality over time. Workers killed and recloned at drift threshold. New file types trigger grammar creation that persists for all future workers.

**Section 11 — Copy-on-Write and Versioning**

Clone destinations determine governance. Personal scratch: root.users.jane.scratch — owner-only, full freedom, disposable. Team experiment: root.org.acme.engineering.experiments — team visibility, department constraints inherited. Production deployment: root.products.myapp.deployments.v3 — org constraints, audit requirements, frozen configuration.

Rules governing clone destinations are themselves KB facts at the appropriate scope. The org can require production clones to go under specific paths. The policy is structural, not documented.

Versioned snapshots: v1, v2, v3 of the same application coexisting in the tree. Diff between versions is a structural operation on two sets of facts. Rollback is deploying clones from an earlier snapshot. Canary is running clones from two snapshots simultaneously and comparing results.

**Section 12 — Negative Accumulation and Hygiene**

Rules go stale. Scripts break. Grammars stop matching. LRU tracks rule usage — last fired, hit count, success rate. Prolog rules at operational scope automate hygiene: flag rules that haven't fired in N days, flag rules with zero positive outcomes in M invocations, flag rules that consistently hit grant denials. Flagged rules are reviewed or purged. Retraction is clean — fact removed, downstream derivations identified through provenance chain.

Contrast with conventional systems where stale knowledge in weights is permanent, unidentifiable, and irremediable.

**Section 13 — Security Model for LM Software**

Self-generated rules inherit all security properties. Grant system governs what each runner can do. Scope chain governs what each runner can see. Constraint inheritance governs what invariants hold. Clone isolation prevents cross-instance leakage. Audit trail covers every operation.

The user doesn't configure security separately. Security falls out of where things are placed in the tree and what grants exist. The same model that governs data access governs application behavior. No separate security layer. No security as afterthought.

**Section 14 — Economics**

Rule amortization: 25-40 tokens to create, replaces 150-300 tokens per use, cost approaches zero at organizational scope with thousands of reuses. Application development cost: hours of interactive sessions versus weeks of conventional development. Deployment cost: snapshot clone versus container orchestration. Operational cost: decreasing per task as rules accumulate versus flat or increasing for conventional systems. Update cost: one fact change versus release cycle.

**Section 15 — What LM Software Is Not**

Not a replacement for all conventional software. Compute-intensive, latency-critical, hardware-interfacing software remains conventional. LM Software targets judgment-heavy, data-rich, policy-governed, multi-step workflows where the value is in correctly applying rules to varied inputs — support, compliance, investigation, processing, triage, review. Where conventional software requires a developer to anticipate every case, LM Software handles novel cases through LLM judgment and encodes the resolution for next time.

**Section 16 — Limitations**

LLM judgment quality bounds application quality. Poorly developed sessions produce poor applications. Snapshot size grows with accumulated state. Clone startup time depends on snapshot size. Pure Prolog execution is limited by rule coverage — novel inputs still require LLM tokens. The gap between level one (full LLM) and level three (pure Prolog) is the development investment. Not every workflow reaches level three.

---

**Appendices**

A — Complete development-to-deployment walkthrough for the support chatbot
B — Complete development-to-deployment walkthrough for the file processing pipeline
C — Runner type comparison table (trigger, token budget, grant scope, lifecycle, conventional equivalent)
D — Data primitive usage patterns (which primitive for which coordination need)
E — Topology patterns with KB tree layouts
F — Snapshot format and size estimates
G — Security scenarios for LM Software (attack vectors, structural prevention)
H — Accumulation metrics across application types
I — Comparison with conventional development lifecycle (side-by-side phase mapping)
J — Conventional LLM application comparison (RAG, LangChain, function calling versus LM Software)