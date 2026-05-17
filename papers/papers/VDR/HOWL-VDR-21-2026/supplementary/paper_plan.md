# VDR-20 PLAN — OPERATIONAL DEPLOYMENT

## Paper scope

VDR-20 describes how to deploy a VDR system as a running service — the prompt runner architecture, the owner's local interface, the coverage-driven self-training loop, and the practical on-ramp from local filesystem to autonomous knowledge accumulation. Where VDR-19 established that the architecture self-extends through usage, VDR-20 specifies who drives that usage, how the threads are structured, how the owner interacts, and how the system transitions from inert seed to autonomous operation.

This paper introduces no new primitives, builtins, struct fields, or modules. Everything described uses existing VDR-1 through VDR-19 components.

---

## Section plan

### Section 1 — From Architecture to Running System

Brief introduction for new readers. VDR is a hybrid architecture where an LLM generates only judgment and prose (~5–20% of conventional token cost) while exact integer primitives handle computation, state, formatting, and logical deduction. Data lives in knowledge bases at integer addresses. The LLM references data by typed paths and identifiers, never processing it through its token stream. VDR-19 established that this architecture self-extends — each session leaves behind Prolog rules, Python scripts, and provenanced facts that persist and compose.

VDR-20 answers the operational question: how does a deployed VDR system actually run? What are the threads, what triggers them, how does the owner interact, and how does the system go from a seeded but empty installation to an autonomous knowledge system?

The core insight: the system runs multiple LLM instances with the same VDR architecture — same command tokens, same primitives, same scoped KB access, same grant model — differentiated only by trigger pattern and lifecycle. The same security, audit, and provenance guarantees from VDR-16 apply identically to every instance type because they all operate through the same primitive pipeline.

### Section 2 — Prompt Runner Architecture

Brief intro: a prompt runner is an LLM instance bound to a VDR session with scope access to relevant KBs, a grant set appropriate to its role, and a trigger pattern that determines when it activates. All runners share the same architecture. The differentiation is purely operational.

**Interactive runners.** Human-facing instances. One per user session. Activated by user input — chat messages, document uploads, queries, project commands. The user types, the runner reads, the runner responds. Standard request-response pattern. Each interaction deposits facts and rules into the user's project KBs through the normal VDR pipeline. These are reactive — they wake on input and produce output.

**Polling runners.** Timer-driven instances. Activated every N seconds, where N is configurable per poller — could be milliseconds for high-frequency monitoring, could be hours for daily maintenance tasks. On each cycle the poller checks queues, counters, trigger conditions, and directory watch lists. If a queue has items, dequeue and process. If a counter crossed a threshold, fire associated rules. If a scheduled task is due, initiate it. If a watched directory has new files, enqueue compaction tasks. Pollers are the system's heartbeat. They don't wait for humans. They find work and do it.

**Processor runners.** Persistent-connection instances. Maintain open streams — API subscriptions, webhook listeners, file watchers on streaming sources. Data arrives continuously and the processor compacts and stores it in real time. A processor watching a metrics stream deposits time-series facts continuously. A processor connected to a news or data feed compacts entries as they arrive. These are long-lived and data-driven.

**Internal processing runners.** Self-directed instances. Activated on their own schedule to examine internal KB state. They evaluate rule sets across KBs, run consistency checks, compute derived facts from newly accumulated data, identify coverage gaps, flag contradictions, compute coverage metrics. These are the system's self-reflection. They don't respond to external events — they examine what the system knows and improve it.

Specify the threading model: how runners are spawned, how they share KB access through the standard scope and visibility model, how grants are scoped per runner type (interactive runners get user-level grants, pollers get system-level grants for queue management, processors get credential grants for external connections, internal processors get read grants across project KBs plus write grants for derived facts and coverage metrics).

Specify the clone lifecycle for runners: each runner is a disposable VDR clone with fresh LLM state inheriting accumulated KB knowledge at integer addresses. Long-running processors periodically snapshot and respawn to stay in the LLM's optimal attention window. Pollers and internal processors are naturally short-lived — they run one cycle and terminate, spawning fresh for the next cycle.

### Section 3 — The Owner-Local Interface

Brief intro: the owner is the person or team who deploys and directs the VDR system. The owner-local interface is the filesystem and directory structure through which the owner provides data, tasks, configuration, and organizational decisions.

**Directory conventions.** The owner's local filesystem has designated directories that the system watches.

An ingress directory where the owner drops files for compaction. Any file placed here gets picked up by a poller, enqueued for processing, compacted by a processor, and stored in the appropriate KB based on classification rules. The owner drops a PDF, a markdown file, a code repository, a dataset — the system handles each according to its accumulated compaction rules and grammars, or writes new ones if the format is novel.

A tasks directory where the owner drops task specifications. A task is a file describing work the system should do — fetch this URL and compact it, reorganize this KB branch, run coverage analysis on this topic, generate a report from these facts. The poller picks up task files, parses them (they're just structured text the system compacts like any document), and routes them to the appropriate runner.

A config directory where the owner places hierarchy proposals, scope adjustments, coverage targets, grant specifications, and policy changes. These are parsed into KB facts and rules that take effect on the next evaluation cycle.

An output directory where the system deposits results — generated reports, exported data, coverage metrics, hierarchy proposals for review, flagged exceptions needing owner judgment.

A review directory where the system places items needing owner approval — proposed hierarchy changes, novel classifications it's uncertain about, coverage decisions where rules conflict, flagged anomalies.

Specify how directory watching works through polling runners with filesystem grants. Specify how file types are detected and routed. Specify how task files are structured — initially as natural language that the LLM compacts into executable commands, eventually as the adjusted compaction format from VDR-19 that parses directly into Prolog facts.

### Section 4 — The Interactive Interface

Brief intro: in addition to the filesystem interface, the owner and users interact through chat sessions (interactive runners) and programmatic API access.

**Chat interface.** The owner or user connects to an interactive runner through a chat session. They describe what they want in natural language. The LLM does what LLMs are good at — takes natural language description and produces structured commands, hierarchy proposals as Prolog facts, organizational plans as rule sets. The owner reviews, adjusts, approves. Three minutes of conversation produces a set of KB facts and rules ready to execute.

The chat interface is where the owner does planning. "I've got Gutenberg in /data/gutenberg, man pages in /usr/share/man, Linux source in /data/repos/linux. I want programming as one branch, literature as another, OS internals as a third." The LLM proposes a hierarchy. The owner says "move networking out of OS internals into its own branch." The LLM adjusts. The hierarchy becomes Prolog facts. The owner says "run it" and the polling runners start executing.

**API interface.** Programmatic access to the same VDR primitive pipeline. External systems can submit queries, assert facts, enqueue tasks, and read results through a structured API. Each API session has its own identity, scope, and grants — the same security model as every other access path. The API enables integration with external tools, CI/CD pipelines, monitoring systems, and other automated systems.

**Using external LLMs for planning.** The owner can use any tool for thinking and planning — Claude, GPT, a local model, pen and paper. The output becomes a file in the tasks or config directory, or a message in the chat interface. VDR doesn't care how the owner arrived at a decision. It cares that the decision becomes facts and rules it can execute. The planning tool is irrelevant. The execution substrate is VDR.

### Section 5 — The Coverage Loop

Brief intro for new readers: VDR stores exact integer values where every computation preserves a Remainder — the exact leftover from integer division, never discarded, never rounded. In the coverage loop, the Remainder of a coverage metric is operational: it describes specifically what the system doesn't know yet, not just a percentage of completion.

**Topic specification.** The owner specifies topics and depth targets. These become KB facts: `topic(python, programming, intermediate).` Rules define what depth levels mean in terms of measurable coverage — API surface area, concept relationship density, pattern coverage, error handling documentation.

**Coverage evaluation.** Internal processing runners evaluate KB state against coverage rules on their schedule. The evaluation produces a coverage metric as a VDR quantity. The value is what's covered. The Remainder is what's missing — not "13% uncovered" but a typed description: "missing asyncio event loop patterns, typing module generics, dataclass inheritance." The Remainder is queryable, decomposable, and actionable.

**Gap-to-task conversion.** Polling runners read coverage metrics and convert gaps into fetch tasks. Missing Python asyncio coverage becomes a fetch task for asyncio documentation. Missing cross-reference between generators and coroutines becomes a targeted query. The fetch tasks go into queues.

**Fetch and compact.** Processor runners execute fetch tasks — reading from local directories, fetching from URLs (when network access is granted), or picking up files the owner dropped in the ingress directory. Fetched documents are compacted through the standard pipeline and stored as provenanced facts.

**Re-evaluation.** Internal processors run again on their next cycle. Coverage metrics update. Remainders shrink. New gaps may appear as the system discovers connections it didn't know to look for. The cycle continues until coverage targets are met or the owner adjusts targets.

**Meta-rule accumulation.** After processing enough documents in a domain, the system writes generalized rules. After processing Python, Zig, and Rust documentation, it has rules about programming language documentation structure in general. These meta-rules accelerate future domain ingestion. The system gets faster at learning because it accumulated structural knowledge about how knowledge is organized.

### Section 6 — Local Directory Bootstrap

Brief intro: the fastest path from seeded system to useful knowledge base is local directories. No API keys, no rate limits, no network latency, no authentication complexity. Point pollers at directories and let the pipeline run.

**Why local first.** Local directories are the validation path. If the system can't compact a man page from disk, it can't handle a live API stream. Local I/O removes every variable except the compaction pipeline itself. It's also how the owner builds confidence — they can watch the system process familiar documents and verify the output makes sense before pointing it at unfamiliar sources.

**Concrete data sources and what they exercise.**

Project Gutenberg: uniform format, massive volume, deeply cross-referenced. Exercises compaction rule generalization (the Gutenberg header format gets a rule on the first few books, then it's mechanical), entity extraction (characters, locations, events, themes), relationship mapping (character relationships, narrative structure, author influences), and cross-referencing across works.

Unix man pages: highly structured, predictable format (NAME, SYNOPSIS, DESCRIPTION, OPTIONS, EXAMPLES, SEE ALSO). Exercises format grammar creation (one or two pages and the grammar handles all of them), and explicit relationship extraction (SEE ALSO sections are direct relationship data).

Source code repositories (Linux kernel, language implementations, well-structured open source): richest source. Code, comments, commit messages, build files, configuration, documentation directories. Exercises multiple compaction rule types per repository, dense cross-referencing (function in source relates to struct in header relates to man page relates to textbook chapter), and the multi-format handling that validates seed layer 2.

API documentation and language references: structured reference material. Exercises the per-language KB structure, API surface coverage metrics, and cross-language comparison rules.

**The hierarchy problem.** The system generates an initial hierarchy reflecting filesystem layout. But filesystem layout doesn't match how you want to search or how you want security scoped. All C documentation — man pages, kernel source, language spec, tutorials — should be in one search scope even though they came from four filesystem paths. Kernel internals might be owner-only while man pages are public. Programming languages should be siblings so cross-language rules compose, but literature should be in a separate branch.

The system proposes a hierarchy based on classification rules. The owner reviews, approves, rearranges through the chat interface or by dropping a config file. The system updates scope paths, re-indexes, and writes rules encoding the owner's decisions. Next time it encounters a similar classification problem it applies those rules. After enough corrections the system's proposals converge with what the owner wants. The organizational rules are KB facts subject to the same accumulation, amortization, and self-extension as every other rule.

**What you end up with.** After consuming a local library: a knowledge base tree where every fact has provenance tracing to source file and compaction rule. Cross-reference rules connecting concepts across sources. Coverage metrics with operational Remainders. Compaction rules for every format encountered. Meta-rules accelerating future ingestion. And every LLM instance still fresh — knowledge in KBs, not weights.

### Section 7 — The Owner's Role

Brief intro: the owner is not a system administrator babysitting a process. The owner is a director using the full tool stack to shape what the system becomes.

**Planning with any tool.** The owner can use the VDR interactive chat to plan. They can use a conventional LLM outside VDR to brainstorm and export the result as a task file. They can write a markdown hierarchy proposal by hand. They can do web searches and save articles locally for the system to compact. The planning tool doesn't matter. What matters is that every decision becomes facts and rules that the runners execute.

**Judgment at chosen granularity.** The owner can micromanage every KB placement or set high-level policies and let the system fill in details. Both styles produce the same thing — facts and rules in KBs. The system adapts because it doesn't distinguish between an owner-asserted rule and a self-generated rule at the operational level (though provenance tracks the difference).

**Shifting over time.** Initially more active — setting hierarchy, defining coverage targets, approving proposals, correcting organizational mistakes. Over time the system's organizational rules converge with the owner's preferences. The owner shifts from directing to auditing. They can query provenance, examine rules, retract anything wrong, and the system adjusts cleanly because retraction is a first-class operation.

**The owner never loses control.** Every fact, rule, hierarchy decision, and organizational choice is inspectable, retractable, and auditable. The system trains itself but the owner sees exactly what it learned, from what source, and can undo any of it surgically. This isn't trust — it's verifiability through the same provenance and audit mechanisms that govern everything in VDR.

### Section 8 — Thread Specification

Detailed technical specification for how the runner types are implemented as threads or processes.

**Thread lifecycle.** How each runner type is spawned, how it acquires its session and grants, how it accesses KBs, how it terminates. Interactive runners: spawned on user connection, terminated on disconnect or idle timeout. Pollers: spawned by scheduler, run one cycle, terminate, respawned on next interval. Processors: spawned on startup or connection establishment, long-lived with periodic snapshot-and-respawn for LLM freshness. Internal processors: spawned by scheduler like pollers, run one evaluation cycle, terminate.

**Concurrency model.** How runners share KB access. All KB writes go through the primitive pipeline with the standard grant and visibility checks. Concurrent writes to the same KB are serialized by the append-only arena model — bump pointer allocation means no contention on writes, reads see a consistent snapshot. Queue operations use atomic primitives. Counter increments are atomic. The concurrency model inherits from VDR's existing data structure specifications.

**Resource allocation.** How LLM compute is distributed across runner types. Interactive runners get priority (user-facing latency matters). Pollers and internal processors are batch — they can wait for compute availability. Processors are medium priority — they need to keep up with their data streams but can buffer briefly. Specify how the scheduler balances compute across runner types.

**Grant scoping per runner type.** Interactive runners: user-level grants inherited from authenticated user. Pollers: system-level grants for queue management, directory watching, and task dispatch — no user data access beyond what's public. Processors: credential grants for their specific external connections plus write grants for their target KBs. Internal processors: broad read grants across project KBs for coverage evaluation plus write grants for derived facts and metrics. Each runner type has the minimum grants necessary for its function.

**Health monitoring.** How the system monitors its own runners. A dedicated internal processor tracks runner health — are pollers completing their cycles, are processors keeping up with their streams, are queues growing or draining. Health metrics are KB facts, queryable and alertable through the same rule evaluation that handles everything else.

### Section 9 — Task Specification Format

Detailed specification for how tasks are structured — the files the owner drops in the tasks directory and the items that runners enqueue for each other.

**Task as compactable document.** A task file is structured text that the system compacts into executable commands. Initially natural language that the LLM interprets. As the system matures, tasks can use the adjusted compaction format from VDR-19 for direct parsing without LLM involvement.

**Task fields.** What a task specifies: action type (fetch, compact, reorganize, analyze, report, export), target (path, URL, KB reference), parameters (depth, coverage target, format, filters), priority, requester (owner, poller, processor, internal), dependencies (tasks that must complete first), output destination (KB path, output directory, queue).

**Task lifecycle.** Created (file drop or enqueue) → parsed (compacted into KB facts) → validated (grant check on requested operations) → queued (priority-ordered) → assigned (scheduler picks runner) → executing → completed (results stored, task marked done) → or failed (error logged, retry or escalation).

**Task chaining.** A task can specify follow-up tasks triggered by its completion. Fetch task completes → triggers compact task → triggers coverage evaluation task. The chain is declared in the task specification and executed by the polling runners monitoring task completion queues.

### Section 10 — Worked Example: From Empty to Operational

Walk through a complete deployment from fresh seed to operational system.

**Hour 0.** Seed loaded. Four layers operational. System can parse, generate, invoke primitives, manage structures. No domain knowledge.

**Hour 1.** Owner connects via chat. Describes directory layout and organizational goals. LLM proposes hierarchy as Prolog facts. Owner adjusts. Hierarchy asserted. Owner drops coverage targets in config directory. Pollers configured for /data/gutenberg, /usr/share/man, /data/repos/linux.

**Hours 2–6.** Pollers walking directories, enqueuing compaction tasks. Processors compacting. First few documents of each type require LLM judgment for compaction rules. By document ten of each type, compaction rules handle structural extraction mechanically. Internal processors begin coverage evaluation — large Remainders, everything is a gap.

**Hours 6–24.** Bulk ingestion. Thousands of Gutenberg texts, thousands of man pages, Linux source tree being processed. Compaction rules are mature for these formats. Cross-reference rules beginning to accumulate. Coverage Remainders shrinking in well-represented areas, identifying specific gaps in thin areas.

**Day 2–7.** Coverage loop driving targeted ingestion. Gaps identified, fetch tasks generated, documents retrieved and compacted. Meta-rules forming — patterns about documentation structure, about how APIs relate, about how narrative structure works. Owner reviews hierarchy proposals on their schedule, approves or adjusts.

**Week 2+.** System approaching coverage targets. Owner sets new targets, adds new data sources, adjusts depth. The cycle continues. The system's organizational rules have largely converged with owner preferences. New document types are handled by generalized meta-rules with high accuracy. The owner is auditing and directing, not managing.

### Section 11 — Security in Multi-Runner Deployment

Brief intro for new readers: VDR enforces access control through KB visibility (public/internal/owner_only checked by integer comparison), scope chains (sibling branches unreachable), grants (default denial), and output constraints (grammar validation post-generation). Full specification in VDR-16.

All runners operate through the same primitive pipeline with the same security model. Specify how security applies to the multi-runner deployment:

Runner isolation: each runner has its own session with its own grants. A poller cannot access user session data. A processor cannot read KBs outside its granted scope. An internal processor has read grants, not write grants for user project KBs.

Directory interface security: files in the ingress directory are processed through the compaction pipeline with the same provenance and constraint checking as any other input. Malicious content in an ingested file does not bypass access control because compaction routes through primitives, not through the LLM's unconstrained generation.

Task validation: every task is validated against the requesting identity's grants before execution. An enqueued task that requests an operation the requester isn't granted is rejected and logged.

Cross-runner communication: all communication goes through KBs and queues with the same visibility and scope checks. Runners cannot communicate outside the structural mechanisms.

### Section 12 — Scaling

How the system scales across the axes that matter.

**Data volume scaling.** More data means more KB facts at integer addresses. Query time stays constant (indexed lookup). Rule evaluation scales with rule base size but the frontier-based GPU evaluator handles this efficiently. Storage grows linearly.

**Runner scaling.** More runners means more concurrent processing. KB access is naturally concurrent through the append-only arena model. Queues handle work distribution. The scheduler balances compute.

**Knowledge scaling.** More accumulated rules means more automatic processing and less LLM judgment needed per task. Token cost per unit of work decreases over time. The system gets more efficient as it grows.

**Multi-owner scaling.** Multiple owners with separate scope trees sharing common infrastructure. Each owner's KBs are visibility-isolated. Shared public KBs (language documentation, open source code) are readable by all. Organizational rules at the system level apply universally. Each owner's customizations are scoped to their branch.

---

## Appendices plan

- AppA: Prompt Runner Specification Tables (runner types, trigger patterns, grant scopes, lifecycle)
- AppB: Directory Interface Specification (directory conventions, file routing rules, task file format)
- AppC: Coverage Metric Specification (how coverage is computed, Remainder structure, gap-to-task conversion)
- AppD: Task Lifecycle State Machine (states, transitions, validation, chaining)
- AppE: Thread Concurrency Model (KB access serialization, queue atomics, counter atomics, arena allocation)
- AppF: Worked Example Timeline (hour-by-hour from seed to operational, with token counts and KB growth)
- AppG: Local Data Source Characteristics (Gutenberg, man pages, source repos, API docs — format, volume, compaction rule count, cross-reference density)
- AppH: Hierarchy Proposal and Convergence (initial proposals, owner corrections, rule accumulation, convergence metrics)
- AppI: Runner Health Monitoring (metrics, thresholds, alerting rules)
- AppJ: Security Matrix (runner type × operation type × grant requirement)
- AppK: Scaling Projections (data volume, runner count, knowledge base size, token efficiency over time)
- AppL: API Interface Specification (endpoints, authentication, session model, grant model)
- AppM: Owner Workflow Patterns (planning with chat, planning with external LLM, config-file-driven, hybrid)

---

## Dependencies

References VDR-15 for token economics, primitive patterns, clone model, data structure specifications. References VDR-16 for security model (visibility, scope, grants, constraints, audit). References VDR-17 for alignment properties (credential model, session scoring). References VDR-18 for GPU implementation (concurrent streams, performance data). References VDR-19 for self-extension architecture (bootstrap pipeline, compaction format, operational lifecycle, LM as runtime programmer, train-as-you-go). Each reference introduced briefly for readers who haven't read the referenced paper.

## Key claims to establish

1. All runner types share the same VDR architecture — differentiation is trigger pattern and grants only
2. The owner-local interface reduces to directory conventions and polling runners with filesystem grants
3. The coverage loop is self-training driven by Remainder as operational gap description
4. Local directory bootstrap is the practical on-ramp with zero external dependencies
5. The owner's role is judgment at chosen granularity using the full tool stack
6. Multi-runner security inherits entirely from VDR-16 with no additional mechanisms needed
7. The system scales along data, runners, knowledge, and owners using existing primitives
8. Task specification is just another document type the system compacts into executable commands

## Subtitle options

1. Operational Deployment — From Seed to Autonomous Knowledge System
2. Operational Deployment — Prompt Runners, Coverage Loops, and the Owner-Local Interface
3. Operational Deployment — How to Run a Self-Training VDR System
4. Operational Deployment — Threads, Directories, and Autonomous Accumulation
5. Operational Deployment — The Practical On-Ramp to Self-Extending Architecture
