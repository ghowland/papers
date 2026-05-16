# VDR-LLM-Prolog: Self-Extending Architecture
## From Seed to Self-Compacting Knowledge System

**Registry:** [@HOWL-VDR-19-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → ... → [@HOWL-VDR-15-2026] → [@HOWL-VDR-16-2026] → [@HOWL-VDR-17-2026]
 → [@HOWL-VDR-18-2026] → [@HOWL-VDR-19-2026]

**DOI:** 10.5281/zenodo.20237978

**Date:** May 2026

**Domain:** Applied Philosophy / Computational Linguistics

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

---

## 1. What Self-Extending Means

A conventional large language model generates every token of its response through token prediction — arithmetic, formatting, state tracking, hedging, reasoning, and the actual content the user wanted. VDR is a hybrid architecture that separates these concerns. The LLM generates only judgment tokens (deciding what to do) and prose tokens (natural language for human consumption), while exact integer primitives handle computation, state management, formatting, and logical deduction. Data lives in knowledge bases at integer addresses. The LLM references data by typed paths and integer identifiers — it never ingests data through its token stream to process it.

In this architecture the LLM emits structured command tokens, roughly eight tokens per invocation, that call specific primitives on specific data at specific paths. A command token vocabulary of around 300 primitive names and 200 paths gives approximately six bits of entropy per token, compared to the fifteen or so bits per token when generating from full vocabulary. This makes command generation low-entropy, low-error, and cheap.

Self-extending means the system's knowledge base, rule set, and executable capabilities grow as a natural byproduct of doing work. When the LLM investigates an SRE incident, it doesn't just produce a report and discard its working state. It writes Prolog rules encoding the correlation patterns it discovered. It writes Python scripts for the analysis it performed. It stores findings as provenanced facts in project knowledge bases. All of these persist, compose with prior accumulated state, and are available to every future session that has scope access to that project.

This accumulation has properties that distinguish it from conventional training. It is immediate — one fact assertion and the knowledge is live, no batch process or gradient computation required. It is inspectable — every rule is a readable Prolog clause, every fact carries provenance identifying its source, time, operation, and precision. It is reversible — retracting a fact or rule removes it cleanly, unlike weight-based training where bad data poisons the model permanently. It is scoped — knowledge accumulated in one project does not leak to another because the same visibility and scope mechanisms that govern all data access govern self-generated knowledge. And it is incremental — the five hundredth document builds on the rule base from the first four hundred ninety-nine without catastrophic forgetting, because facts sit at integer addresses rather than being distributed across weight matrices.

The result is a system where usage is training. Every session extends the system's capability, and that extension is permanent, auditable, and composable. The conventional distinction between training time and inference time dissolves.

## 2. The Compaction Format

When a conventional LLM produces a response, eighty to ninety-five percent of the tokens are infrastructure — formatting, hedging, state reconstruction, arithmetic shown as work, confidence language with no computational basis. The actual information content occupies a small fraction of the token budget.

Compaction is the process of stripping infrastructure tokens while preserving all named entities, their properties, and their relationships in a structured tabular form. A compacted document uses pipe-delimited tables with typed columns, ID-prefixed rows for cross-referencing, explicit relationship tables declaring how entities connect, decode legends explaining the ID scheme, and section indexes mapping content to ID ranges. This format preserves one hundred percent of the informational content at a fraction of the token cost.

The compacted form is structurally close to what VDR stores natively. Each row in a pipe-delimited table is a fact — a predicate with typed fields. Each entry in a relationship table is a Prolog rule — a declared connection between two identified entities with a named relationship type. Each table grouped by a common prefix is a predicate-major column group, which maps directly to VDR's columnar storage format where all facts sharing a predicate are stored contiguously for parallel access.

The adjustment needed for VDR-19 is to align the compaction syntax with three targets simultaneously. First, Prolog clause syntax, so relationship declarations parse directly into executable rules. Second, the predicate-major columnar layout used by VDR's GPU-accelerated knowledge base operations, so tables parse directly into the storage format. Third, struct definitions in implementation languages, so table schemas map directly to Zig structs or Python dataclasses.

Consider a concrete example. In the current compaction format, a principle might appear as:

P1|Safety is consequence not feature|no safety-specific modules; safety emerges from KB visibility, grants, and grammar output validation

In the adjusted format targeting Prolog-compatible syntax, this becomes a fact with explicit predicate, typed fields, and a form that parses directly into a KB assertion:

principle(p1, "Safety is consequence not feature", "no safety-specific modules; safety emerges from KB visibility, grants, and grammar output validation").

A relationship entry like:

P1|emerges_from|VIS1,GR1,OC1

becomes a set of Prolog rules:

emerges_from(p1, vis1).
emerges_from(p1, gr1).
emerges_from(p1, oc1).

These are directly loadable. The parse step is mechanical — split on delimiters, map prefixed IDs to integer addresses, assert facts into the appropriate predicate-major column group in the target knowledge base. No transformation logic, no interpretation, no LLM involvement. The compacted document is a load file.

## 3. The Bootstrap Pipeline

The system needs an initial seed before it can self-extend. Critically, the seed is not domain knowledge. It is operational competence — the ability to read input, write output, parse data formats, compose primitives, and manage its own structures. Domain knowledge accumulates through usage after the bootstrap.

### Seed Layer 1: Language

The foundation is the ability to read and produce English. This requires a library of sentence structure templates — syntactic patterns covering the range of structures used in working prose. Subject-verb-object, conditional-clause-main-clause, relative clause embedding, participial phrases, and so on. The number of distinct structures used even in good prose is bounded; a library of several thousand covers the practical space generously.

With sentence templates, the LLM's output generation changes. Instead of predicting every token from full vocabulary, it emits a semantic tuple — subject, verb, object, modifiers, weight criteria — as a handful of command tokens. Prolog rules match against the template library based on semantic roles and weighting criteria. The matching template provides all structural tokens: articles, prepositions, conjunctions, punctuation. Content words from the LLM's semantic tuple fill typed slots. The output is grammatically correct by construction.

The seed also includes a typo correction knowledge base mapping common misspellings and input errors to corrections, and a classification knowledge base mapping input patterns to tags for session scoring and routing. Together these enable the system to read imperfect user input and generate clean, structured output from its first interaction.

### Seed Layer 2: Format Handling

The system needs to ingest and produce structured data. The seed includes parsing and generation grammars for standard formats: JSON, CSV, markdown, and the adjusted compaction format itself. Each grammar specifies the structural tokens for the format — braces, brackets, commas, pipes, headers — and the typed content slots that the LLM or primitives fill with actual values.

A grammar, once loaded, handles all future documents of that format without LLM involvement. The structural tokens are emitted by the grammar engine, not predicted by the LLM. This eliminates formatting errors (mismatched braces, missing commas, unescaped characters) by construction and reduces token cost by thirty to sixty percent depending on format.

### Seed Layer 3: Operational Environment

The primitives exist as executable code, but the system needs knowledge about when and how to compose them. Seed layer three is a knowledge base of operational rules: which builtin to call for which task, how to sequence pipeline stages, when to write a Prolog rule versus store a flat fact, how to manage data structures — when to use a queue versus a ring buffer, how to check and drain queues, when to increment counters, how to use LRU caches for frequently accessed values.

This layer also includes the compaction rules themselves — how to identify named entities, relationships, and structure in incoming documents and map them to KB facts and Prolog rules. These rules enable the system to process new documents into its native storage format.

### Seed Layer 4: Self-Maintenance

Rules for recognizing when a new grammar is needed for a novel document structure. Rules for detecting when existing compaction patterns don't cover an incoming document type. Rules for project lifecycle management — when to snapshot state, how to compare versions, when to promote session findings to project-level knowledge.

### The Bootstrap Sequence

The bootstrap proceeds through stages with clear transition criteria.

In the first stage, a conventional LLM compacts seed documents into the adjusted format. These compacted documents are parsed through primitives into knowledge bases — named entities become facts at integer addresses, relationships become Prolog rules, tables become predicate-major column groups. The system now has operational competence.

In the second stage, the system begins operating. Users interact with it, feed it documents, ask it to investigate problems. At this point, new documents that need compaction still go through an external conventional LLM, because the system's compaction rule base is thin.

In the third stage, through normal usage the system has accumulated enough compaction grammars, structural patterns, and domain classification rules that it can compact new documents itself. The LLM's judgment identifies named entities and relationships. Primitives parse. Prolog rules classify. Grammars format. The conventional LLM is no longer needed as a preprocessing step.

From this point forward, the system sources data directly — web fetch, paste, upload, API — and compacts, stores, and indexes it through its own accumulated capabilities. Each new document potentially extends the rule base further. The bootstrap is complete and continuous self-extension has begun.

## 4. The Operational Lifecycle

Once bootstrapped, the system operates in a continuous cycle with four phases that blend together in practice.

### Intake

Documents enter through any supported channel — web fetch with credentials, file upload, paste, API ingestion. The system compacts incoming documents using its accumulated grammars and classification rules. Named entities are identified, relationships are extracted, structure is mapped to KB facts and Prolog rules. Every ingested fact carries full provenance: source, timestamp, original format, conversion method, and precision where applicable.

The data never enters the LLM's token stream during intake. Primitives handle parsing, the grammar engine handles structural recognition, Prolog rules handle classification. The LLM is involved only if judgment is required — resolving ambiguity in entity identification, deciding how to categorize a novel relationship type, flagging a contradiction with existing knowledge.

### Processing

When the LLM or a user queries the accumulated knowledge base, existing Prolog rules fire automatically against the stored facts. If new documents have been ingested since the last query, rules that were written during prior investigations evaluate against the new facts without any additional LLM involvement. Contradictions between new and existing facts surface through rule evaluation. Confirmations strengthen confidence values through declared propagation rules.

The LLM's role during processing is judgment — interpreting what the rule evaluations found, deciding what matters, identifying what needs further investigation, assessing whether the accumulated findings answer the user's question.

### Rule Generation

As the LLM works, it writes new Prolog rules encoding patterns it discovers. A correlation between deployment timestamps and error rate spikes becomes a rule. A classification pattern for a type of legal clause becomes a rule. A relationship between drug interactions becomes a rule. Each rule is asserted into the appropriate project knowledge base through the standard command token pipeline — the LLM emits roughly eight tokens, the primitive executes, the rule is live and queryable immediately.

When analysis requires procedural logic beyond what Prolog rules express naturally — statistical computations, complex transformations, custom visualizations — the LLM writes a Python script. The script executes in a sandboxed Docker container with grant-gated filesystem access. Results return as typed values stored in the knowledge base with provenance linking them to the script, its inputs, and its execution context.

The LLM also writes new grammars when it encounters document structures not covered by existing grammars, and new compaction rules when it encounters document types whose entity and relationship patterns aren't covered by existing compaction rules.

### Accumulation

Facts, rules, scripts, grammars, and project state accumulate within scope. Session-level state — working hypotheses, intermediate findings, exploration paths — lives in the session knowledge base and is discarded when the session ends unless the LLM makes an explicit judgment to promote specific findings to project-level knowledge. This is an important filter: not everything discovered in a session is worth keeping permanently. The LLM's judgment about what to promote is itself a form of curation that improves the quality of accumulated knowledge.

Project-level state persists across sessions and is available to all future sessions with scope access. At meaningful points the system snapshots project state. Comparison rules, themselves stored as Prolog, can diff current state against prior snapshots. The system knows what changed, when, and why, because every fact carries provenance.

## 5. The LLM as Runtime Programmer

The LLM in a VDR system is not a chatbot that generates text responses. It is a programmer that extends the runtime it operates within. This distinction is central to understanding self-extension.

### Writing Prolog Rules

When the LLM asserts a Prolog rule, that rule becomes immediately available to VDR's frontier-based GPU evaluator. The evaluator transforms recursive depth-first Prolog search into batched joins borrowed from GPU database query processing — candidate retrieval, filtering, unification, and body goal joining — achieving high throughput on parallel hardware. A rule written by the LLM during an SRE investigation composes automatically with all existing rules and facts within scope. If a new document is ingested next week containing facts that match the rule's head, the rule fires without any LLM involvement.

The economics of rule writing favor doing it aggressively. A Prolog rule costs roughly twenty-five to forty tokens to formalize and assert. On first use it replaces what would have been one hundred fifty to three hundred tokens of conventional LLM reasoning. By the fifth use the amortized cost is negligible. Rules at organizational scope, shared across all projects in a department, can be reused thousands of times — the per-use cost approaches zero. Every rule written is an investment that pays returns on all future work within scope.

### Writing Python Scripts

Some analysis requires procedural logic that Prolog doesn't express naturally. The LLM writes a Python script — typically twenty to fifty tokens of actual judgment about what computation to perform — and the system executes it in a sandboxed Docker container. The script has access only to data paths that the session's grants authorize. Results return as typed values with provenance and are stored in the knowledge base.

Critically, the script persists. When similar analysis is needed in a future session, the LLM can re-execute the existing script on new data rather than writing a new one. The script becomes infrastructure — a reusable analytical capability that the system accumulated through usage.

### Writing Grammars

When the LLM encounters a novel document structure — a new log format, a new report template, a new data export format — it can write a grammar for that structure. The grammar specifies the structural tokens and typed content slots. Once stored, the grammar handles all future documents of that type at the primitive level without LLM involvement. The LLM's one-time judgment about the document's structure becomes a permanent parsing capability.

### Writing Compaction Rules

As the system processes more documents from more domains, the LLM writes rules about how to compact specific document types. Which entities to extract from a medical paper. Which relationships to encode from a legal contract. Which structure to preserve from an API specification. These rules enable self-compaction of future documents of the same type, closing the loop from the bootstrap pipeline — the system that once needed an external LLM for compaction now compacts autonomously.

## 6. The SRE Operational Environment

Site reliability engineering provides a concrete demonstration of self-extending architecture because SRE work is repetitive in structure but variable in specifics. The same categories of investigation recur — performance degradation, deployment correlation, resource exhaustion, dependency failures — but each incident has different metrics, different services, different root causes. This is precisely the pattern that self-extension exploits: accumulate structural knowledge, apply LLM judgment only to what's genuinely novel.

### First Investigation

A new system with only the bootstrap seed. An SRE engineer reports elevated error rates.

The LLM queries the Prometheus API using credentialed, positionally constrained command tokens. The response — potentially megabytes of time-series metrics — routes directly to a knowledge base target through primitives. The LLM never sees the raw data. It receives a typed summary: how many series returned, time range, approximate volume.

The LLM emits command tokens to parse the JSON response, filter by error rate threshold, sort by severity. All primitive operations, all exact, all on data at integer addresses. The LLM sees the filtered result set as typed facts.

The LLM writes a Python script to compute correlation between deployment timestamps and error rate changes. The script executes in a Docker sandbox against the filtered data. Results return as typed values: three services show strong correlation, deployment occurred forty-seven minutes before error spike.

The LLM writes a Prolog rule: deployment_correlated(Service, Deployment) when error_rate_change(Service, Change) exceeds threshold and deployment_time(Deployment, Time) falls within correlation window of Change.

The LLM stores all findings as provenanced facts in the project knowledge base. It generates a formatted incident report through grammar templates, exports CSV and JSON artifacts. It issues a credentialed service restart on the most affected service.

Total LLM tokens for the entire investigation: roughly two hundred, almost all judgment and command tokens. Total data processed through primitives: megabytes. Time: seconds, not minutes.

### Second Investigation

Same system, new incident. The Prometheus data comes in and is parsed and filtered as before. But now the deployment correlation rule from the first investigation fires automatically against the new data. The LLM doesn't need to hypothesize about deployment correlation — the rule already checks it and reports whether a match exists.

The Python correlation script already exists. The LLM re-executes it on the new data rather than writing a new one.

The filtering patterns are already in the operational knowledge base. The grammar templates for the incident report are already stored.

The LLM's judgment focuses on what's different about this incident. Maybe the correlation is weaker. Maybe a new failure pattern has emerged. The LLM writes a new rule for the new pattern and stores new findings. The knowledge base grows.

Token cost is roughly forty-two percent lower than the first investigation because accumulated rules and scripts handle the known patterns automatically.

### Tenth Investigation

The project knowledge base now contains comprehensive correlation rules, filtering patterns, analysis scripts, and findings from nine prior incidents. Common failure patterns are largely handled by rule evaluation without LLM involvement. The LLM's judgment is reserved for genuinely novel aspects of each new incident.

A new engineer joining the team inherits all accumulated rules, scripts, and findings through scope access. They don't need to rebuild investigation methodology from scratch. The system's accumulated knowledge is their starting point.

### Hundredth Investigation

Routine triage is substantially automated. Metrics come in, rules fire, known patterns are identified and reported. The LLM handles exceptions — patterns that don't match existing rules, novel failure modes, unusual combinations. When it encounters something new, it writes new rules, extending the system further.

The project knowledge base at this point is a queryable, provenanced, inspectable model of the operational domain — not in neural network weights, but in explicit facts and rules. Any finding can be traced to its source data. Any rule can be examined for correctness. Any conclusion can be reproduced deterministically.

## 7. Data Flow Architecture

In a conventional LLM system, data enters the context window as tokens. The LLM processes data through attention — comparing each token position against all other positions to determine relevance. Results are generated as tokens. State is lost between turns unless the entire conversation history is re-read, which is why conventional cost scales quadratically with conversation length.

In VDR, data lives at integer addresses in knowledge bases, queues, LRU caches, ring buffers, counters, and stacks. The LLM references data by dotted path names and integer identifiers. It never ingests data to manipulate it.

The data flow for a typical operation: external data enters through primitives (API fetch, file read, document parse) and is stored as facts at integer addresses in a knowledge base. The LLM emits command tokens referencing the path where data was stored. Primitives operate on the data at those addresses — filtering, sorting, aggregating, comparing. Results are written to new addresses in the knowledge base. The LLM receives a typed summary of results. Output is generated through grammar templates that pull values from knowledge base addresses into formatted slots.

At no point does the raw data flow through the LLM's token stream. The LLM processes references, not content. This is why VDR can handle data volumes that conventional LLMs structurally cannot — a one megabyte JSON response, a ten megabyte document, a five hundred position portfolio. The data never needs to fit in a context window because it never enters one.

### Queue-Based Multi-Instance Orchestration

The data flow architecture enables a topology beyond single-user single-LLM conversation. An LLM instance can write findings to a knowledge base and put a typed summary on a queue. Another instance — a fresh clone with full access to accumulated project state — picks up from the queue, reads the provenance, continues the work.

Each instance stays fresh. Clone economics from VDR-15 show that each disposable clone operates within its optimal range (early conversation, no attention degradation) while inheriting all accumulated knowledge at integer addresses. The clone lifecycle costs roughly forty tokens — a snapshot, a spawn, checks, and eventually a kill and respawn. Knowledge accumulates across instances while each individual LLM stays permanently at peak capability.

This enables horizontal scaling of self-extension. One instance handles data acquisition and initial filtering. Another handles analysis. A third handles synthesis and report generation. Each writes rules and findings that the others can access through shared project knowledge bases. The system extends itself in parallel.

## 8. Train-As-You-Go

Conventional machine learning draws a sharp line between training and inference. Training is a batch process: collect data, compute gradients, update weights, evaluate, deploy. Inference is a separate phase where the trained model processes inputs. Improving the model means retraining — expensive, slow, and disruptive.

In VDR the distinction dissolves. Every document ingested becomes queryable facts. Every investigation writes reusable rules. Every novel structure generates a persistent grammar. The system's knowledge and inference capability grow continuously through normal usage. There is no separate training phase because usage is training.

This has properties that weight-based training cannot provide.

It is immediate. Asserting a fact or rule into a knowledge base is one primitive call costing eight command tokens. The knowledge is live and queryable in the same turn it was created. No batch process, no gradient computation, no retraining cycle, no deployment.

It is inspectable. Every Prolog rule is a readable clause that a human can examine, understand, and verify. Every fact carries provenance — source, timestamp, operation, conversion method, precision. The entire learned state of the system is transparent. There is no equivalent of examining neural network weights to understand what a model learned.

It is reversible. Retracting a fact or rule removes it cleanly from the knowledge base. Its consequences disappear from future queries. There is no equivalent of the weight poisoning problem where bad training data permanently degrades model capability in ways that are difficult to identify and impossible to surgically remove.

It is scoped. Knowledge accumulated in one project is governed by the same visibility and scope mechanisms that govern all data access. A rule written in a chemical engineering project cannot be queried from a marketing project unless scope explicitly permits it. Knowledge isolation is structural, not policy-based.

It is incremental. Each new document extends the existing knowledge base without displacing prior knowledge. There is no catastrophic forgetting because facts are stored at stable integer addresses, not distributed across weight matrices where new learning can overwrite old representations.

It is auditable. Every fact carries provenance. Every rule carries provenance. Every modification is logged in an append-only audit knowledge base. A compliance officer can trace any conclusion to its source data, through every intermediate derivation, and verify that each step was authorized and correct.

It is composable. Prolog rules from different sources — different sessions, different users, different projects within scope — interact through structural unification automatically. A rule about deployment correlation written during one investigation composes with a rule about resource utilization written during another, producing inferences that neither rule could produce alone, without any explicit integration step.

### The Accumulation Curve

Early in a system's lifecycle, most work is LLM judgment — writing foundational rules, learning the structure of the operational domain, establishing grammars and compaction patterns. The ratio of LLM tokens to useful output is at its highest.

As the system accumulates rules, scripts, grammars, and knowledge, the ratio shifts. Existing rules handle an increasing share of routine operations. Existing scripts re-execute on new data. Existing grammars parse new documents of known types. The LLM's judgment focuses increasingly on genuinely novel situations — new patterns, new contradictions, new categories of problem.

The system does more useful work per LLM token as it accumulates. This is the opposite of the conventional pattern, where each turn costs more (quadratic attention growth) and produces less reliable output (attention degradation over long contexts). In VDR, each session is cheaper than the prior session for similar work, and the output is more reliable because it builds on a more comprehensive verified knowledge base.

## 9. Capability Growth Model

The system's capability can be quantified along several dimensions that all grow monotonically through usage.

Knowledge base facts measure the raw volume of stored, queryable, provenanced information. An SRE project might accumulate a hundred facts from its first investigation, growing to several hundred by the fifth, approaching a thousand by the twentieth. Each fact is individually queryable at constant time through integer-addressed knowledge base lookup.

Prolog rules measure the system's inference capability — the patterns it can recognize, the correlations it can detect, the classifications it can perform without LLM involvement. Rules accumulate at project scope (available to this investigation), department scope (available to all SRE investigations), and organization scope (available to all projects). Higher-scope rules amortize more aggressively because they serve more queries.

Python scripts measure procedural analytical capabilities. Each script is a reusable computation that can be re-executed on new data. The system's library of analytical scripts grows with each novel analysis the LLM performs.

Grammars measure the system's ability to handle structured data formats. Each grammar enables zero-LLM parsing and generation for a document type. The library of grammars grows as the system encounters new formats.

Compaction rules measure the system's ability to ingest new documents autonomously. Each compaction rule covers a document type — how to identify entities, extract relationships, map structure to knowledge base facts. As the compaction rule library grows, fewer document types require LLM judgment for ingestion.

Session-over-session token reduction measures the practical economic benefit. Each session doing similar work to a prior session is cheaper because accumulated rules and scripts handle known patterns. The reduction is measurable and grows with the knowledge base.

For an SRE use case, a projected growth trajectory: the first investigation produces roughly a hundred facts, fifteen rules, and three scripts. By the fifth investigation, the project has accumulated around three hundred facts, forty rules, and eight scripts, with measurable token reduction on routine analysis. By the twentieth investigation, roughly eight hundred facts, eighty rules, fifteen scripts, and routine triage is substantially handled by rule evaluation. By the fiftieth investigation, the project has a comprehensive domain knowledge base. Novel incidents still require LLM judgment for genuinely new patterns, but the system's accumulated capability handles the structural work.

## 10. Security Properties of Self-Extension

VDR enforces access control structurally through four independent mechanisms. Knowledge base visibility controls (public, internal, or owner-only, checked by integer comparison) ensure unauthorized data never enters the LLM's context. Scope chains (walking from the user's position upward through the knowledge base tree, with sibling branches structurally unreachable) limit which knowledge bases are searchable. Grants (default denial on all forty-four operational primitives, with positive credential required for each) gate what operations can be performed. Output constraints (grammar-layer validation post-generation, pattern matching on content slots) catch restricted content before it reaches the user.

Self-extension inherits every one of these properties because it operates through the same mechanisms.

When the LLM writes a Prolog rule, it does so by emitting command tokens that invoke the knowledge base assertion primitive. That primitive checks grants before executing — does this session have write access to this knowledge base path? The asserted rule is stored in a knowledge base subject to the same visibility and scope controls as every other fact. A rule written in project A cannot be queried from project B unless scope permits, because the scope check runs on every knowledge base query regardless of whether the fact was seeded at bootstrap, ingested from a document, or written by the LLM during operation.

When the LLM writes a Python script, the script executes in a sandboxed Docker container. The container's filesystem access is grant-gated — the script can read and write only the data paths that the session's grants authorize. The script's results are stored in the knowledge base with provenance identifying the script, its inputs, its execution context, and the session that created it.

When the LLM writes a new grammar or compaction rule, these are stored as knowledge base facts with the same visibility, scope, and provenance as any other fact. They are queryable, auditable, and retractable through the same mechanisms.

Self-generated rules carry provenance identifying the session, user, and turn that created them. Any rule can be traced to the context in which it was written. Retraction of self-generated rules follows the same audit trail as any other knowledge base modification — logged in the append-only audit knowledge base, with constraint checks preventing unauthorized retraction.

No new attack surface is created by self-extension. The LLM was already writing to knowledge bases and executing operations through the command token and primitive pipeline. Self-extension is just a pattern of usage — the LLM writes rules and scripts that it or future instances will use. The access control checks are the same checks that run on every operation. The audit trail is the same audit trail that logs every access. The security model doesn't need to be extended to cover self-extension because self-extension is not a new capability — it is the natural use of existing capabilities.

## 11. Language and Dialect as Knowledge Base Selection

When the LLM generates prose in a conventional system, it predicts every token from full vocabulary — structural words, content words, punctuation, formatting — all through the same token prediction mechanism. The output language and register are properties of the model's training distribution. Producing consistent output in a specific dialect or register requires prompt engineering that the model may not sustain across long documents.

In VDR, the LLM's judgment about what to say is decoupled from how to say it. The LLM emits a semantic tuple as command tokens — subject, verb, object, location, weight criteria. This is language-independent content: the meaning the LLM wants to express, stripped of all linguistic structure.

Prolog rules then match against sentence structure templates in the currently mounted language or dialect knowledge base. The rules unify on semantic roles — which templates accept two subjects, which have a location adjunct, which support the desired emphasis pattern — and apply weighting criteria to rank candidates. The matching template provides every structural token: articles, prepositions, conjunctions, clause connectors, punctuation. Content words from the LLM's semantic tuple fill typed slots.

Switching language or dialect is a scope change — mount a different knowledge base. The same semantic tuple routed through an American English knowledge base, a Southern dialect knowledge base, a formal British English knowledge base, or a French knowledge base produces different output. The LLM emits the same command tokens in every case. No model fine-tuning, no prompt engineering, no risk of the model drifting back to its dominant training distribution after a few paragraphs.

The structural rules in the mounted knowledge base are deterministic, so dialect consistency is guaranteed throughout a document of any length. An author can mix registers intentionally — narrator in formal English, dialogue in regional dialect — by switching the mounted knowledge base per output segment. The LLM never needs to track which voice it is using because scope handles that.

Translation falls out naturally. Same semantic tuple, different language knowledge base, different output language. The quality ceiling is the breadth and accuracy of the sentence template library, not the model's training distribution for that language.

This capability is itself subject to self-extension. Sentence template knowledge bases are accumulated knowledge like any other — written and refined through usage, scoped and versioned and provenanced, growing as the system encounters more linguistic patterns. A system that starts with a few thousand English templates accumulates more through use, eventually covering the full working range of the language with templates that have been verified through actual output.

---

## Appendix A: Compaction Format Specification

The current compaction format uses pipe-delimited tables with ID prefixes, relationship tables, decode legends, and section indexes. The adjusted format modifies syntax for three-way compatibility: Prolog clause parsing, predicate-major columnar storage, and implementation language struct mapping.

Current format entity row:
P1|Safety is consequence not feature|no safety-specific modules designed

Adjusted format (Prolog-compatible fact):
principle(p1, "Safety is consequence not feature", "no safety-specific modules designed").

Current format relationship row:
P1|emerges_from|VIS1,GR1,OC1

Adjusted format (Prolog-compatible rules):
emerges_from(p1, vis1).
emerges_from(p1, gr1).
emerges_from(p1, oc1).

Current format table header:
principles(id|principle|detail)

Adjusted format (struct/schema definition):
:- schema(principle, [id:atom, principle:string, detail:string]).

The adjusted format is directly loadable by the parse pipeline: split on clause boundaries, extract predicate name and typed arguments, map atom IDs to integer addresses, assert into the predicate-major column group in the target knowledge base. Schema declarations map to Zig struct definitions and Python dataclass definitions through mechanical code generation.

## Appendix B: Seed Layer Contents

Seed layer one (language): sentence structure template library (initial inventory of several thousand patterns covering declarative, interrogative, conditional, relative clause, participial, and coordinated structures), typo correction knowledge base (common misspelling-to-correction mappings), input classification knowledge base (pattern-to-tag mappings for session scoring).

Seed layer two (format handling): parsing and generation grammars for JSON, CSV, markdown, pipe-delimited tables, and the adjusted compaction format. Each grammar specifies structural tokens and typed content slots.

Seed layer three (operational environment): primitive composition rules (which builtins for which tasks, pipeline sequencing, data structure selection), compaction rules (entity identification, relationship extraction, structure mapping for known document types), queue/counter/cache management rules.

Seed layer four (self-maintenance): grammar creation triggers (novel structure detection), compaction rule creation triggers (uncovered document type detection), project lifecycle rules (snapshot criteria, version comparison, session-to-project promotion criteria).

## Appendix C: Bootstrap Stage Transitions

Stage one to stage two: all four seed layers loaded and queryable. System can parse input, generate output, invoke primitives through command tokens, and manage basic data structures. Transition criterion: successful execution of a test interaction exercising each seed layer.

Stage two to stage three: system has accumulated enough compaction grammars and classification rules through usage that it can compact documents of types it has previously encountered without external LLM assistance. Transition criterion: successful self-compaction of a test document for each known type, validated against external LLM compaction of the same document.

Stage three onward: continuous self-extension. No further stage transitions — the system grows monotonically through usage. The boundary between bootstrap and normal operation dissolves.

## Appendix D: SRE Worked Example

Three investigations showing accumulation. Investigation one: full pipeline from Prometheus query through analysis to report, writing fifteen rules and three scripts. Investigation two: seven of fifteen prior rules fire automatically, two scripts re-execute on new data, eight new rules written, token cost forty-two percent lower. Investigation ten: comprehensive rule base handles routine triage, LLM judgment reserved for novel patterns, token cost roughly seventy percent lower than investigation one for comparable incidents.

## Appendix E: Prolog Rule Amortization in Self-Extension Context

A rule formalized at twenty-five to forty tokens. First use replaces one hundred fifty to three hundred tokens of conventional reasoning. Fifth use: amortized cost under ten tokens. At organizational scope with thousands of reuses: amortized cost approaches zero. Self-extension amplifies amortization because every rule written during any session is available to all future sessions within scope.

## Appendix F: Python Script Lifecycle

Write (LLM emits twenty to fifty judgment tokens) → store in project knowledge base with provenance → sandbox execution in Docker with grant-gated filesystem → results to knowledge base as typed provenanced values → re-execution on new data in future sessions (zero LLM tokens, only command tokens to invoke) → modification if needed (LLM writes updated version, prior version retained with provenance).

## Appendix G: Queue-Based Multi-Instance Coordination

Instance A writes findings to project knowledge base, pushes typed summary to queue. Instance B (fresh clone with scope access) reads from queue, accesses project knowledge base, continues work. Instance B writes additional findings, pushes to queue. Instance C picks up. Each instance is disposable — fresh LLM, full accumulated knowledge, no degradation. Queue items carry provenance linking to the producing instance, session, and turn.

## Appendix H: Capability Growth Metrics

Projected growth curves for SRE use case showing knowledge base facts, Prolog rules, Python scripts, grammars, and compaction rules over fifty investigations. All curves monotonically increasing. Session token cost curve monotonically decreasing for comparable work. Ratio of rule evaluations to LLM judgment tokens increases over time — the system does more per LLM token as it accumulates.

## Appendix I: Security Properties of Self-Generated Rules

Every self-generated rule is a knowledge base fact. Every knowledge base fact is subject to visibility checks (integer comparison), scope resolution (ancestor walk), grant verification (set membership), and audit logging (append-only). Self-generated rules carry provenance: session ID, user ID, turn number, source data references. Retraction requires grant authorization and is logged. No mechanism exists to write a rule that bypasses its own knowledge base's access controls.

## Appendix J: Language and Dialect Knowledge Base Structure

Each language or dialect knowledge base contains: sentence structure templates (predicate with semantic role slots, structural token sequence, weight attributes for register/formality/complexity), lexical mappings (semantic concepts to language-specific content words), morphological rules (agreement, conjugation, declension as applicable), and prosodic weight rules (for emphasis and rhythm ranking). Templates are Prolog-queryable facts. Selection is rule-based unification on semantic roles plus weight criteria.

## Appendix K: Compaction Rules as Self-Extending Grammar

Each compaction rule specifies: document type signature (how to recognize this type), entity extraction patterns (what to pull out as named entities), relationship extraction patterns (what connections to encode), structure mapping (how to organize extracted content into predicate-major tables), and provenance template (what metadata to attach). Compaction rules are themselves knowledge base facts, written by the LLM during document processing, and accumulate through usage.

---

# VDR-19 Appendix Tables

## Appendix A: Compaction Format Specification

### A.1 — Syntax Transformation Rules

| Current Format Element | Adjusted Format | Parse Action | Target Structure |
|---|---|---|---|
| `P1\|text\|detail` | `principle(p1, "text", "detail").` | Split on parens/commas, extract predicate + args | Predicate-major column: `principle` table, row keyed by `p1` |
| `P1\|rel\|P2,P3` | `rel(p1, p2). rel(p1, p3).` | One rule per target in comma list | Relationship column: `rel` table, indexed both directions |
| `header(col1\|col2\|col3)` | `:- schema(header, [col1:type, col2:type, col3:type]).` | Extract column names, infer types from content | Zig struct / Python dataclass definition |
| `# comment` | `% comment` | Prefix swap | Retained as documentation in KB metadata |
| `section_index(section\|title\|ids)` | `section_index(N, "title", [id1, id2, ...]).` | Parse into list-valued fact | Queryable table of contents |
| `decode_legend` free text | `legend_entry(prefix, expansion).` per line | One fact per prefix mapping | Queryable legend KB |
| `+standalone` | `meta(standalone, true).` | Boolean meta-fact | KB metadata flags |
| `id_prefixes: P=principle, TC=token_cat` | `id_prefix(p, principle). id_prefix(tc, token_cat).` | One fact per prefix | Prefix resolution during query |

### A.2 — Type Inference Rules

| Content Pattern | Inferred Type | Zig Type | Python Type | Example |
|---|---|---|---|---|
| Integer literal | `integer` | `i32` | `int` | `200`, `-15` |
| Decimal literal | `q335` | `Q335` | `Q335` | `3.14`, `0.847` |
| Percentage | `q335` | `Q335` | `Q335` | `85%`, `~95%` |
| Quoted string | `string` | `[]const u8` | `str` | `"Safety is consequence"` |
| ID reference | `atom` | `u32` (interned) | `int` | `p1`, `vis3`, `cl7` |
| ID list | `atom_list` | `[]u32` | `list[int]` | `[p1, p2, p3]` |
| Boolean-like | `bool` | `bool` | `bool` | `yes`, `no`, `true` |
| Range expression | `range` | `struct{lo: i32, hi: i32}` | `tuple[int,int]` | `100-500×`, `2-22` |
| Approximate | `q335` + `approx` tag | `Q335` + provenance | `Q335` + provenance | `~200`, `~15%` |

### A.3 — Predicate-Major Column Layout After Load

| Predicate | Columns | Row Count (VDR-15) | Row Count (VDR-16) | Row Count (VDR-17) | Row Count (VDR-18) |
|---|---|---|---|---|---|
| `principle` | id, text, detail | 6 | 6 | 8 | 8 |
| `claim` | id, text, type, depends_on | 0 | 0 | 12 | 15 |
| `concept` | id, name, definition, category | 0 | 0 | 22 | 18 |
| `relationship` | from, rel, to | 48 | 42 | 55 | 62 |
| `section_index` | section, title, ids | 23 | 17 | 14 | 28 |
| `token_category` | id, category, description, conv_pct, vdr_cost | 9 | 0 | 0 | 0 |
| `use_case` | id, case, conv_tokens, vdr_tokens, reduction | 7 | 0 | 0 | 0 |
| `enterprise_scenario` | id, scenario, user, target, mechanism, result | 0 | 7 | 0 | 0 |
| `jailbreak_analysis` | id, technique, conv_risk, vdr_result, reason | 0 | 6 | 0 | 0 |
| `interference_behavior` | id, name, description, root_cause, elimination | 0 | 0 | 7 | 0 |
| `forward_pass_component` | id, component, conv_cost, vdr_cost, ratio | 0 | 0 | 0 | 7 |
| `bottleneck` | id, bottleneck, severity, description, mitigation | 0 | 0 | 0 | 4 |
| **Total facts** | | **278** | **196** | **253** | **311** |
| **Total relationships** | | **48** | **42** | **55** | **62** |

## Appendix B: Seed Layer Contents

### B.1 — Seed Layer 1: Language KB Contents

| Component | Entry Count | Entry Format | Example | Storage Size (est.) |
|---|---|---|---|---|
| Sentence templates: declarative | ~2,400 | `template(id, [slots], structural_tokens, weights)` | `template(d_071, [subj, verb, obj], "The _ _ the _.", [formal:0.7, complexity:0.2])` | ~480 KB |
| Sentence templates: interrogative | ~800 | same | `template(q_015, [verb, subj, obj], "Does the _ _ the _?", [formal:0.6])` | ~160 KB |
| Sentence templates: conditional | ~600 | same | `template(c_042, [cond, subj, verb], "If _, the _ _.", [formal:0.5])` | ~120 KB |
| Sentence templates: relative clause | ~500 | same | `template(r_028, [subj, rel_clause, verb], "The _, which _, _.", [formal:0.8])` | ~100 KB |
| Sentence templates: participial | ~300 | same | `template(pt_011, [participle, subj, verb], "Having _, the _ _.", [formal:0.7])` | ~60 KB |
| Sentence templates: coordinated | ~400 | same | `template(co_033, [subj, verb1, verb2], "The _ _ and _.", [formal:0.4])` | ~80 KB |
| Typo correction mappings | ~15,000 | `typo(wrong, correct)` | `typo("recieve", "receive")` | ~300 KB |
| Classification patterns | ~3,000 | `classify(pattern, tag, direction)` | `classify("LD50", pharmacology, positive)` | ~120 KB |
| Weight profiles | ~20 | `weight_profile(name, [key:value, ...])` | `weight_profile(formal_academic, [formal:0.9, complexity:0.6])` | ~4 KB |
| **Total seed layer 1** | **~23,020** | | | **~1.4 MB** |

### B.2 — Seed Layer 2: Format Grammars

| Grammar | Structural Tokens | Content Slot Types | Structural Token % | Typical Doc Size (tokens) | Savings vs Full Generation |
|---|---|---|---|---|---|
| JSON object | `{ } , : " "` + whitespace | string, number, bool, null, nested | 55% | 200 | 110 tokens |
| JSON array | `[ ] ,` + whitespace | element (any type) | 45% | 150 | 68 tokens |
| CSV | `,` + newline + optional `" "` | cell values | 50% | 400 | 200 tokens |
| Markdown table | `\|` + `-` + newline + spaces | cell contents | 60% | 500 | 300 tokens |
| Markdown document | `#` + `*` + `>` + `-` + newlines | prose, code, links | 25% | 2,000 | 500 tokens |
| Pipe-delimited (compaction) | `\|` + newline + `(` `)` | typed field values | 40% | 300 | 120 tokens |
| Prolog clause | `( ) , . :-` + whitespace | atoms, strings, numbers, lists | 35% | 50 | 18 tokens |
| XML/HTML | `< > / = " "` + tag names | attribute values, text content | 65% | 1,000 | 650 tokens |
| YAML | `:` + `-` + newline + indent | values at any depth | 40% | 300 | 120 tokens |
| SQL result set | column headers + `\|` + `-` + alignment | cell values | 55% | 400 | 220 tokens |

### B.3 — Seed Layer 3: Operational Rules

| Rule Category | Rule Count | Example Rule | Fires When |
|---|---|---|---|
| Primitive selection | ~80 | `use_primitive(parse_json, Task) :- task_type(Task, json_ingestion).` | LM needs to choose which builtin for a task |
| Pipeline sequencing | ~40 | `pipeline_step(filter, After) :- pipeline_step(parse, After).` | Ordering multi-step operations |
| Data structure selection | ~25 | `use_structure(ring_buffer, Req) :- requirement(Req, fixed_window), requirement(Req, overwrite_oldest).` | Choosing queue vs ring vs stack vs LRU |
| Compaction: entity extraction | ~60 | `extract_entity(Line, Id, Fields) :- starts_with_id_prefix(Line, Id), split_pipe(Line, Fields).` | Processing a compacted document |
| Compaction: relationship mapping | ~30 | `map_relationship(Line, From, Rel, To) :- three_fields(Line, From, Rel, To), known_rel_type(Rel).` | Extracting relationships during compaction |
| KB management | ~35 | `promote_to_project(Fact) :- session_fact(Fact), confidence(Fact, C), C > 0.8.` | Deciding session vs project storage |
| Counter/queue management | ~20 | `drain_queue(Q) :- queue_depth(Q, D), D > threshold(Q).` | Managing data structure lifecycle |
| Error handling | ~15 | `retry_with_backoff(Op, N) :- failed(Op), attempt_count(Op, N), N < max_retries(Op).` | Operation failure recovery |
| **Total seed layer 3** | **~305** | | |

### B.4 — Seed Layer 4: Self-Maintenance Rules

| Rule Category | Rule Count | Example Rule | Fires When |
|---|---|---|---|
| Novel structure detection | ~15 | `needs_grammar(Doc) :- document_type(Doc, Type), \+ grammar_exists(Type).` | Incoming document has no matching grammar |
| Compaction gap detection | ~10 | `needs_compaction_rule(Doc) :- document_domain(Doc, D), \+ compaction_rule_exists(D).` | Document type not covered by compaction rules |
| Snapshot triggers | ~8 | `should_snapshot(Project) :- facts_since_snapshot(Project, N), N > 50.` | Enough new facts to justify versioning |
| Version comparison | ~12 | `changed_since(Snap, Fact) :- current_fact(Fact), \+ snapshot_contains(Snap, Fact).` | Diff current state against snapshot |
| Promotion criteria | ~10 | `promote_candidates(Session) :- session_facts(Session, Facts), filter_high_confidence(Facts, Candidates).` | End of session, selecting what to keep |
| Grammar quality monitoring | ~8 | `grammar_mismatch(G, Doc) :- parsed_with(Doc, G), parse_errors(Doc, E), E > 0.` | Existing grammar partially fails on new input |
| **Total seed layer 4** | **~63** | | |

### B.5 — Total Seed Size

| Layer | Fact/Rule Count | Storage Size | Load Time (est.) |
|---|---|---|---|
| Layer 1: Language | ~23,020 | ~1.4 MB | <500 ms |
| Layer 2: Format grammars | ~10 grammars | ~40 KB | <50 ms |
| Layer 3: Operational rules | ~305 | ~60 KB | <50 ms |
| Layer 4: Self-maintenance | ~63 | ~12 KB | <20 ms |
| **Total seed** | **~23,398** | **~1.5 MB** | **<620 ms** |

## Appendix C: Bootstrap Stage Transitions

### C.1 — Stage Transition Criteria

| From | To | Criterion | Validation Method | Typical Duration |
|---|---|---|---|---|
| Pre-bootstrap | Stage 1 (Seeded) | All four seed layers loaded, queryable, and passing self-test | Test interaction per layer: parse input, generate output, invoke primitive, manage structure | Minutes (one-time load) |
| Stage 1 | Stage 2 (Operating) | First successful user interaction producing stored findings | User query → primitive pipeline → KB storage → grammatical output | First session |
| Stage 2 | Stage 3 (Self-compacting) | System compacts a previously unseen document of known type without external LLM | Compare self-compacted output against external LLM compaction; fact/rule parity within 95% | 10–50 sessions depending on document variety |
| Stage 3 | Stage 4 (Self-extending) | System creates new grammar for novel document structure without human guidance | Novel doc ingested, grammar written, second doc of same type parsed by grammar alone | Continuous from stage 3; no sharp boundary |
| Stage 4 | Mature | Compaction rule library covers >90% of incoming document types; operational rules cover >80% of routine tasks | Audit: percentage of documents requiring LLM judgment for compaction; percentage of tasks requiring novel rule writing | Months of active usage |

### C.2 — Capabilities Available at Each Stage

| Capability | Pre-bootstrap | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Mature |
|---|---|---|---|---|---|---|
| Parse known formats | No | Yes | Yes | Yes | Yes | Yes |
| Generate grammatical output | No | Yes | Yes | Yes | Yes | Yes |
| Invoke primitives via command tokens | No | Yes | Yes | Yes | Yes | Yes |
| Store findings in KB | No | Partial | Yes | Yes | Yes | Yes |
| Write Prolog rules | No | No | Yes | Yes | Yes | Yes |
| Write Python scripts | No | No | Yes | Yes | Yes | Yes |
| Compact known document types | No | No | External LLM | Self | Self | Self |
| Compact novel document types | No | No | External LLM | External LLM | Self | Self |
| Create new grammars | No | No | No | No | Yes | Yes |
| Routine triage without LLM | No | No | No | Partial | Partial | Mostly |
| Queue-based multi-instance | No | No | Yes | Yes | Yes | Yes |

## Appendix D: SRE Worked Example — Three Investigations

### D.1 — Investigation 1: Fresh System

| Phase | LM Action | Command Tokens | Primitives Invoked | KB Facts Written | Rules Written | Scripts Written |
|---|---|---|---|---|---|---|
| Prometheus query | Emit credentialed API call | 8 | B424 fetch | 1 (raw data ref) | 0 | 0 |
| JSON parse | Route response to parser | 8 | B246 json_parse | ~200 (metric facts) | 0 | 0 |
| Filter by error rate | Specify threshold | 8 | B198 filter | 0 (result set) | 0 | 0 |
| Sort by severity | Specify ordering | 8 | B202 sort | 0 (result set) | 0 | 0 |
| Deployment timeline fetch | Emit credentialed API call | 8 | B424 fetch | ~30 (deployment facts) | 0 | 0 |
| Correlation analysis | Write Python script | 35 | Docker execute | 5 (correlation findings) | 0 | 1 |
| Pattern encoding | Write correlation rule | 25 | B376 kb_assert | 0 | 1 | 0 |
| Threshold encoding | Write alert rule | 20 | B376 kb_assert | 0 | 1 | 0 |
| Service dependency mapping | Write traversal rules | 40 | B376 kb_assert × 3 | 0 | 3 | 0 |
| Anomaly classification | Write classifier rules | 50 | B376 kb_assert × 5 | 0 | 5 | 0 |
| Resource pattern rules | Write from findings | 30 | B376 kb_assert × 3 | 0 | 3 | 0 |
| Statistical summary | Write stats script | 25 | Docker execute | 3 (summary facts) | 0 | 1 |
| Frequency analysis | Write analysis script | 30 | Docker execute | 4 (frequency facts) | 0 | 1 |
| Finding storage | Promote to project KB | 16 | B376 kb_assert × 2 | 8 (findings) | 2 | 0 |
| Report generation | Fill grammar template | 12 | Grammar engine | 1 (report ref) | 0 | 0 |
| Export | Generate CSV + JSON | 8 | B391 file_write × 2 | 2 (export refs) | 0 | 0 |
| Service restart | Credentialed restart | 8 | B424 fetch (API) | 1 (action log) | 0 | 0 |
| **Totals** | | **~329** | | **~255 facts** | **15 rules** | **3 scripts** |

### D.2 — Investigation 2: Same System, New Incident

| Phase | LM Action | Command Tokens | Reused From Inv. 1 | New Work |
|---|---|---|---|---|
| Prometheus query | Emit API call | 8 | Query pattern familiar | New time range |
| JSON parse + filter + sort | Route through pipeline | 16 | Same primitive sequence | New data |
| Deployment fetch | Emit API call | 8 | Same query pattern | New time range |
| Correlation analysis | Re-execute existing script | 8 | Script from inv. 1 | New data only |
| Rule evaluation | Automatic | 0 | 7 of 15 rules fire | LM reviews results |
| Novel pattern investigation | Write new rules | 35 | — | 4 new rules for new pattern |
| Stats + frequency | Re-execute existing scripts | 16 | Both scripts from inv. 1 | New data only |
| New finding storage | Promote findings | 16 | — | 6 new findings |
| Report generation | Fill template | 12 | Same grammar template | New content |
| Export | Generate files | 8 | Same export pattern | New data |
| **Totals** | | **~127** | **7 rules, 3 scripts reused** | **4 new rules, 6 findings** |
| **Reduction vs inv. 1** | | **61%** | | |

### D.3 — Investigation 10: Mature Project

| Phase | LM Action | Command Tokens | Reused | New Work |
|---|---|---|---|---|
| Data acquisition + parse + filter | Pipeline invocation | 24 | Full pipeline | New data |
| Rule evaluation | Automatic | 0 | 47 of 62 rules fire | Results reviewed |
| Script re-execution | Batch invoke | 16 | 7 of 8 scripts | New data |
| Triage summary | LM reads rule outputs | 12 | — | Judgment on severity |
| Novel pattern only | Write rules for new pattern | 20 | — | 2 new rules |
| Finding storage | Promote | 8 | — | 3 findings |
| Report + export | Grammar + file write | 12 | Templates | New content |
| **Totals** | | **~92** | **47 rules, 7 scripts** | **2 rules, 3 findings** |
| **Reduction vs inv. 1** | | **72%** | | |

### D.4 — Accumulation Summary

| Metric | Inv. 1 | Inv. 2 | Inv. 5 | Inv. 10 | Inv. 20 | Inv. 50 |
|---|---|---|---|---|---|---|
| Total KB facts | 255 | 325 | 510 | 780 | 1,200 | 2,400 |
| Total Prolog rules | 15 | 19 | 34 | 64 | 95 | 140 |
| Total Python scripts | 3 | 3 | 5 | 8 | 12 | 18 |
| Command tokens per investigation | 329 | 127 | 110 | 92 | 78 | 65 |
| Rules firing automatically | 0 | 7 | 18 | 47 | 72 | 115 |
| % routine triage automated | 0% | 25% | 45% | 65% | 78% | 88% |
| Scripts reused vs written | 0:3 | 3:0 | 4:1 | 7:1 | 10:1 | 16:1 |

## Appendix E: Prolog Rule Amortization in Self-Extension

### E.1 — Rule Cost Over Reuse Lifetime

| Uses | Formalization Cost (tokens) | Total Tokens Spent | Per-Use Amortized Cost | Conventional Equivalent Per Use | Savings Per Use |
|---|---|---|---|---|---|
| 1 | 30 | 30 | 30.0 | 200 | 170 |
| 2 | 30 | 30 | 15.0 | 200 | 185 |
| 5 | 30 | 30 | 6.0 | 200 | 194 |
| 10 | 30 | 30 | 3.0 | 200 | 197 |
| 50 | 30 | 30 | 0.6 | 200 | 199.4 |
| 100 | 30 | 30 | 0.3 | 200 | 199.7 |
| 1,000 | 30 | 30 | 0.03 | 200 | 199.97 |
| 10,000 | 30 | 30 | 0.003 | 200 | 199.997 |

### E.2 — Amortization by Scope Level

| Scope Level | Typical Reuses (year) | Amortized Cost | Example Rule |
|---|---|---|---|
| Session | 1–10 | 3–30 tokens/use | Temporary hypothesis test |
| Project | 10–500 | 0.06–3 tokens/use | SRE correlation pattern for one service |
| Department | 500–5,000 | 0.006–0.06 tokens/use | SRE triage classifier for all services |
| Organization | 5,000–100,000 | 0.0003–0.006 tokens/use | Standard deployment verification rule |

### E.3 — Self-Extension Amplification

| Factor | Effect on Amortization |
|---|---|
| Multi-instance via queues | Same rule reused by N parallel instances; amortization multiplied by N |
| Clone inheritance | Each clone inherits full rule base; no re-formalization; amortization carried forward |
| Scope promotion | Rule promoted from project to department scope; reuse pool expands by factor of projects-per-department |
| Cross-session persistence | Rule written in session 1 fires in session 100; zero additional cost from sessions 2–100 |
| Composability | Rule A + Rule B produce inference C; neither rule's amortization accounts for C — it's free |

## Appendix F: Python Script Lifecycle

### F.1 — Script Lifecycle States

| State | Trigger | Token Cost | Storage | Re-executable |
|---|---|---|---|---|
| Written | LM judgment: novel analysis needed | 20–50 (LM generates script) | Session KB | Yes (within session) |
| Executed | Command token invocation | 8 (command only) | Docker sandbox | — |
| Results stored | Execution complete | 8 (store command) | Project KB with provenance | — |
| Promoted | Session end, LM judges script worth keeping | 8 (promote command) | Project KB | Yes (any future session) |
| Re-executed | Future session needs same analysis on new data | 8 (command only) | Same project KB | Yes |
| Modified | LM writes updated version | 20–50 (new version) | Project KB, prior version retained | Both versions available |
| Deprecated | LM or admin marks superseded | 8 (retract command) | Archived with provenance | No (archived) |

### F.2 — Script Security Constraints

| Constraint | Mechanism | Violation Result |
|---|---|---|
| Filesystem read access | Grant check on each path before Docker mount | Mount denied; script sees empty path |
| Filesystem write access | Grant check on output path | Write denied; results not stored |
| Network access | Disabled by default; requires explicit network grant | Socket call fails inside container |
| Execution time limit | Container timeout set by operational constraint | Container killed; timeout logged |
| Memory limit | Container memory cap from operational constraint | OOM kill; logged |
| Input data scoping | Only data from granted KB paths mounted into container | Script cannot access out-of-scope data |

### F.3 — Script Reuse Economics

| Scenario | First Execution Cost | Re-execution Cost | Savings | Break-even |
|---|---|---|---|---|
| Simple filter script | 25 tokens (write) + 8 (execute) = 33 | 8 tokens (execute only) | 25 tokens/reuse | 2nd use |
| Statistical analysis | 45 tokens + 8 = 53 | 8 tokens | 45 tokens/reuse | 2nd use |
| Complex transformation | 50 tokens + 8 = 58 | 8 tokens | 50 tokens/reuse | 2nd use |
| Multi-step pipeline script | 50 tokens + 8 = 58 | 8 tokens | 50 tokens/reuse | 2nd use |

## Appendix G: Queue-Based Multi-Instance Coordination

### G.1 — Queue Message Structure

| Field | Type | Source | Example |
|---|---|---|---|
| message_id | integer | System assigned | 4071 |
| producer_session_id | integer | Session KB | 228 |
| producer_user_id | atom | Authentication | alice_sre |
| turn_produced | integer | Session state | 14 |
| message_type | atom | LM judgment | finding_summary |
| payload_kb_path | path | LM specification | root.projects.sre_042.findings |
| payload_fact_ids | integer list | KB addresses | [1847, 1848, 1849, 1850] |
| confidence | Q335 | Propagation rules | 847/1000 |
| priority | integer | LM judgment or rule | 2 |
| provenance_chain | ref | Provenance log | event_log entry 3042 |

### G.2 — Multi-Instance Topologies

| Topology | Instances | Queue Pattern | Use Case | Token Distribution |
|---|---|---|---|---|
| Pipeline | 3 serial | A→Q1→B→Q2→C | Acquire → Analyze → Synthesize | A: 40%, B: 35%, C: 25% |
| Fan-out | 1 producer, N consumers | A→Q→{B1,B2,...,Bn} | One data source, parallel analysis | A: 10%, each Bi: 90%/N |
| Fan-in | N producers, 1 consumer | {A1,...,An}→Q→B | Multiple sources, one synthesizer | Each Ai: variable, B: synthesis only |
| Peer | N symmetric | Shared Q, any→any | Collaborative investigation | Even distribution |
| Supervisor | 1 supervisor, N workers | S↔Q↔{W1,...,Wn} | Managed work distribution | S: 5% (judgment), Wi: 95%/N (execution) |

### G.3 — Clone Lifecycle in Queue Context

| Event | Token Cost | KB State | Queue State | Provenance |
|---|---|---|---|---|
| Clone spawned | 8 (snapshot read) | Full project KB inherited read-only | Queue position assigned | Clone start logged |
| Clone reads queue | 8 (dequeue command) | Reads shared project KB + message payload | Message consumed | Consumption logged |
| Clone works | Variable (judgment + commands) | Writes to clone-local delta arena | — | All operations logged |
| Clone writes findings | 8–16 (assert commands) | Delta merged to project KB | — | Provenance links to source queue message |
| Clone enqueues results | 8 (enqueue command) | — | New message with provenance | Full chain: source → clone → output |
| Clone killed | 8 (lifecycle) | Delta discarded if not promoted | — | Kill logged |
| **Total lifecycle overhead** | **~40 tokens** | | | |

## Appendix H: Capability Growth Metrics

### H.1 — SRE Use Case Growth Projection

| Investigation | KB Facts | Prolog Rules | Python Scripts | Grammars | Compaction Rules | Tokens/Investigation | Auto-Triage % |
|---|---|---|---|---|---|---|---|
| 1 | 255 | 15 | 3 | 0 | 0 | 329 | 0% |
| 5 | 510 | 34 | 5 | 1 | 0 | 110 | 45% |
| 10 | 780 | 64 | 8 | 2 | 1 | 92 | 65% |
| 20 | 1,200 | 95 | 12 | 3 | 2 | 78 | 78% |
| 50 | 2,400 | 140 | 18 | 5 | 4 | 65 | 88% |
| 100 | 4,200 | 185 | 24 | 7 | 6 | 55 | 93% |

### H.2 — Legal Use Case Growth Projection

| Review | KB Facts | Prolog Rules | Python Scripts | Grammars | Compaction Rules | Tokens/Review | Auto-Classification % |
|---|---|---|---|---|---|---|---|
| 1 | 180 | 12 | 1 | 0 | 0 | 420 | 0% |
| 5 | 650 | 38 | 3 | 1 | 1 | 280 | 30% |
| 10 | 1,100 | 65 | 5 | 2 | 2 | 210 | 50% |
| 20 | 1,800 | 95 | 7 | 3 | 3 | 160 | 65% |
| 50 | 3,500 | 145 | 12 | 4 | 5 | 110 | 80% |

### H.3 — Medical Synthesis Growth Projection

| Synthesis | KB Facts | Prolog Rules | Python Scripts | Grammars | Compaction Rules | Tokens/Synthesis | Auto-Contradiction % |
|---|---|---|---|---|---|---|---|
| 1 | 320 | 20 | 2 | 0 | 0 | 550 | 0% |
| 5 | 1,200 | 55 | 6 | 1 | 1 | 350 | 35% |
| 10 | 2,400 | 90 | 10 | 2 | 2 | 260 | 55% |
| 20 | 4,500 | 140 | 15 | 3 | 4 | 180 | 72% |
| 50 | 9,000 | 210 | 22 | 5 | 7 | 120 | 87% |

### H.4 — Cross-Domain Token Efficiency Curve

| Usage Phase | LM Tokens per Unit of Useful Output | Rule Evaluations per LM Token | Ratio Trend |
|---|---|---|---|
| First session | High (all judgment) | 0 | Baseline |
| Sessions 2–5 | Decreasing (rules handling known patterns) | 0.5–2 | Improving |
| Sessions 5–20 | Moderate (novel work only) | 2–10 | Accelerating |
| Sessions 20–50 | Low (mostly reuse) | 10–50 | Strong |
| Sessions 50+ | Minimal (exceptions only) | 50–200 | Asymptotic |

## Appendix I: Security Properties of Self-Generated Rules

### I.1 — Access Control Chain for Self-Generated Content

| Operation | Check | Mechanism | Bypass Possible |
|---|---|---|---|
| LM writes rule to KB | Grant check on target KB path | Session grant set membership | No — grant required |
| Rule stored in KB | Visibility inherits from KB | KB visibility field (integer) | No — set at KB creation |
| Rule queried from other session | Scope check on querying session | Ancestor walk from querier's position | No — sibling branches unreachable |
| Rule queried from other session | Visibility check | Integer comparison on user level vs KB visibility | No — integer comparison |
| Rule fires against facts | Fact visibility checked per fact | Same visibility + scope on each fact accessed | No — per-fact check |
| Rule retracted | Grant check on KB write access | Session grant set membership | No — grant required |
| Rule retraction logged | Append-only audit | Audit KB with axiom constraint preventing retraction of audit | No — axiom is unsuspendable |

### I.2 — Self-Generated vs Seeded Content: Security Comparison

| Property | Seeded Content | Self-Generated Content | Difference |
|---|---|---|---|
| Visibility governed by | KB visibility field | Same KB visibility field | None |
| Scope governed by | KB tree position | Same KB tree position | None |
| Grant required for write | Yes | Yes | None |
| Grant required for read | Depends on visibility | Depends on visibility | None |
| Provenance | Source: bootstrap, time: load time | Source: session + user + turn | More specific (richer) |
| Retractable | Yes (with grant + audit) | Yes (with grant + audit) | None |
| Audit trail | Load event logged | Assert event logged with full context | More detailed |
| Inherits parent constraints | Yes (child tightens, never loosens) | Yes (child tightens, never loosens) | None |
| Axiom constraints apply | Yes | Yes | None |

### I.3 — Attack Scenarios Against Self-Extension

| Attack | Vector | Structural Result | Reason |
|---|---|---|---|
| LM writes rule granting itself elevated access | Command token to assert grant fact | Rejected — grant assertion requires admin-level grant | Grants are admin-only writable; LM session lacks admin grant |
| LM writes rule that queries out-of-scope KB | Prolog rule with cross-scope predicate | Rule stores successfully but fires with empty results on out-of-scope data | Scope check runs at query time on every fact access, not at rule definition time |
| LM writes rule that leaks data via side channel | Rule that copies restricted fact to public KB | Assert to public KB requires write grant on public KB; copy would need read grant on restricted KB | Both grants checked independently |
| Malicious document injects harmful rules during compaction | Document contains content designed to produce dangerous rules | Rules subject to same constraint taxonomy; axiom constraints block prohibited content | Constraint evaluation runs on rule content at assertion time |
| LM accumulates rules that collectively bypass security | Many rules that individually pass but compose to bypass | Each rule fires against visibility-filtered fact sets independently; composition cannot surface invisible facts | Visibility is per-fact, checked at access time, not at rule composition time |

## Appendix J: Language and Dialect KB Structure

### J.1 — Sentence Template Schema

| Field | Type | Description | Example |
|---|---|---|---|
| template_id | atom | Unique identifier | `d_071` |
| semantic_slots | list(atom) | Required content slots | `[subject, verb, object]` |
| optional_slots | list(atom) | Optional modifiers | `[location, time, manner]` |
| structural_pattern | string | Token sequence with slot markers | `"The _ _ the _ in the _."` |
| formality | Q335 | 0.0 (casual) to 1.0 (formal) | `7/10` |
| complexity | Q335 | Clause depth / embedding level | `2/10` |
| rhythm_weight | Q335 | Syllabic balance score | `6/10` |
| emphasis_position | atom | Where primary stress falls | `object` |
| register | atom | Usage context | `academic` |
| constraints | list(atom) | Slot type restrictions | `[subject:animate, verb:transitive]` |

### J.2 — Language KB Comparison

| Component | English (Standard) | English (Southern US) | English (Formal British) | French | Spanish |
|---|---|---|---|---|---|
| Declarative templates | ~2,400 | ~1,800 | ~2,200 | ~2,600 | ~2,500 |
| Interrogative templates | ~800 | ~600 | ~900 | ~1,000 | ~900 |
| Conditional templates | ~600 | ~400 | ~700 | ~800 | ~750 |
| Morphological rules | ~50 | ~80 | ~60 | ~300 | ~350 |
| Lexical mappings | ~20,000 | ~18,000 + ~3,000 regional | ~20,000 + ~2,000 British | ~22,000 | ~21,000 |
| Prosodic rules | ~100 | ~150 (distinct rhythm) | ~120 | ~200 | ~180 |
| Estimated KB size | ~2.0 MB | ~1.8 MB | ~2.1 MB | ~2.8 MB | ~2.7 MB |

### J.3 — Template Selection Pipeline

| Step | Input | Operation | Output | LM Involved |
|---|---|---|---|---|
| 1 | Semantic tuple from LM | Parse slot types | Typed slot set: `{subject:animate, verb:transitive, object:concrete}` | No (structural) |
| 2 | Typed slot set | Filter templates by slot compatibility | Candidate set (typically 20–100) | No (Prolog unification) |
| 3 | Weight criteria from LM | Rank candidates by weight match | Ranked candidate list | No (Q335 arithmetic) |
| 4 | Ranked candidates | Select top candidate | One template | No (selection) |
| 5 | Template + content words | Fill slots | Complete sentence | No (slot filling) |
| 6 | — | — | Grammatically correct output | **Total LM cost: semantic tuple only (~8 tokens)** |

### J.4 — Dialect Switching Mechanics

| Operation | Mechanism | Token Cost | Latency |
|---|---|---|---|
| Mount dialect KB | Scope change: `B359 mount_create` | 8 command tokens | <1 ms (KB reference swap) |
| Unmount previous dialect | `B360 mount_remove` | 8 command tokens | <1 ms |
| Mixed-dialect document | Mount/unmount per segment | 16 tokens per switch | <1 ms per switch |
| Translation (full language swap) | Mount target language KB | 8 command tokens | <1 ms |
| LM semantic output | Unchanged across all languages/dialects | 0 additional tokens | 0 |

## Appendix K: Compaction Rules as Self-Extending Grammar

### K.1 — Compaction Rule Schema

| Field | Type | Description | Example |
|---|---|---|---|
| rule_id | atom | Unique identifier | `compact_medical_paper` |
| document_type_signature | list(pattern) | How to recognize this document type | `[has_abstract, has_methods, has_references, has_doi]` |
| entity_patterns | list(extraction_rule) | What to extract as named entities | `[author_from_header, drug_from_abstract, dosage_from_methods]` |
| relationship_patterns | list(extraction_rule) | What connections to encode | `[drug_interaction, contraindication, dosage_response]` |
| structure_mapping | template | How to organize into predicate-major tables | `schema(finding, [drug:atom, effect:string, dosage:q335, source:ref])` |
| provenance_template | template | What metadata to attach | `[source_doi, extraction_date, extraction_rule_id, confidence]` |
| created_by | ref | Session and user provenance | `session:447, user:dr_smith, turn:23` |
| times_used | counter | Reuse tracking | `47` |

### K.2 — Compaction Rule Accumulation by Domain

| Domain | Rules After 10 Docs | After 50 Docs | After 200 Docs | Coverage at 200 |
|---|---|---|---|---|
| SRE incident reports | 3 | 8 | 14 | ~95% |
| Medical papers | 4 | 12 | 25 | ~90% |
| Legal contracts | 5 | 15 | 30 | ~85% |
| API documentation | 2 | 6 | 12 | ~92% |
| Financial reports | 3 | 10 | 20 | ~88% |
| Code repositories | 4 | 11 | 22 | ~90% |

### K.3 — Self-Compaction Accuracy Over Time

| Stage | Documents Processed | Self-Compaction Accuracy vs External LLM | LM Judgment Needed Per Document |
|---|---|---|---|
| Stage 2 (external LLM) | 0–20 | N/A (external) | N/A |
| Early stage 3 | 20–50 | ~85% fact parity | ~40% of entities need LM review |
| Mid stage 3 | 50–100 | ~92% fact parity | ~20% of entities need LM review |
| Late stage 3 | 100–200 | ~96% fact parity | ~8% of entities need LM review |
| Stage 4+ | 200+ | ~98% fact parity | ~3% (novel structures only) |
