# VDR-19 SELF-EXTENDING ARCHITECTURE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → seed_layers → bootstrap_stages → lifecycle_phases → capability_growth → relationships → sections

# principles(id|principle|rationale)
P1|Usage is training|Every session extends KB facts, Prolog rules, scripts, grammars; no separate training phase; immediate, inspectable, reversible, scoped, incremental
P2|LLM as runtime programmer|LLM writes Prolog rules, Python scripts, grammars, compaction rules that persist and compose; extends the runtime it operates within
P3|Accumulation curve|System does more useful work per LLM token as it accumulates; opposite of conventional quadratic attention growth
P4|Self-extension inherits all security|Self-generated rules use same command token + primitive pipeline; same grants, visibility, scope, audit as all other KB facts
P5|Data never enters token stream|External data routes to KB through primitives; LLM processes references not content; handles arbitrary data volumes
P6|Compaction is the native load format|Pipe-delimited tables map to Prolog facts, predicate-major columns, and implementation structs; compacted doc is a load file
P7|Seed is operational competence not domain knowledge|Bootstrap provides language, format handling, operational rules, self-maintenance; domain knowledge accumulates through usage
P8|Command tokens are low-entropy|~300 primitive names + ~200 paths = ~6 bits/token vs ~15 bits full vocab; low-error, cheap

# claims(id|claim|type|depends_on)
CL1|Rule formalization costs 25-40 tokens; replaces 150-300 tokens of conventional reasoning per use|observation|
CL2|By 5th reuse amortized rule cost is under 10 tokens; at org scope with thousands of reuses approaches zero|derivation|CL1
CL3|Investigation 2 token cost 42% lower than investigation 1 from accumulated rules and scripts|observation|
CL4|Investigation 10 token cost ~72% lower than investigation 1|observation|CL3
CL5|Investigation 50: 88% of routine triage automated by rule evaluation|observation|CL4
CL6|Total seed size ~23,398 entries, ~1.5 MB, loads in <620ms|observation|
CL7|Clone lifecycle costs ~40 tokens total (snapshot, spawn, checks, kill)|observation|
CL8|Self-compaction reaches ~98% fact parity with external LLM after 200+ documents|observation|
CL9|Each new document potentially extends rule base further; bootstrap is complete when system compacts autonomously|derivation|P1,P6
CL10|Composability is free — Rule A + Rule B produce inference C with no explicit integration step|observation|P2

# concepts(id|name|definition|category)
C1|Self-extension|System's KB, rule set, and executable capabilities grow as byproduct of doing work; persistent, auditable, composable|architecture
C2|Compaction|Stripping infrastructure tokens while preserving all named entities, properties, relationships in pipe-delimited tabular form|process
C3|Adjusted compaction format|Syntax aligned with Prolog clause parsing, predicate-major columnar layout, and Zig struct / Python dataclass mapping simultaneously|format
C4|Sentence structure templates|Syntactic patterns with semantic role slots, structural token sequences, weight attributes; LLM emits semantic tuple, Prolog matches template, grammar fills structural tokens|mechanism
C5|Semantic tuple|Language-independent content: subject, verb, object, modifiers, weight criteria; emitted by LLM as command tokens; decoupled from linguistic structure|mechanism
C6|Language KB mounting|Switching language/dialect is a scope change; same semantic tuple through different mounted KB produces different language output; deterministic dialect consistency|mechanism
C7|Queue-based multi-instance orchestration|Instance writes findings to KB, pushes typed summary to queue; fresh clone picks up, continues work; each instance disposable, knowledge accumulates|topology
C8|Accumulation curve|Early: mostly LLM judgment; later: existing rules handle routine ops; LLM focuses on genuinely novel situations; cost per unit of useful output decreases monotonically|property
C9|Train-as-you-go|Immediate (one primitive call), inspectable (readable clauses + provenance), reversible (clean retraction), scoped (visibility governs), incremental (no catastrophic forgetting), auditable (append-only log), composable (structural unification)|property
C10|Compaction rules|Per-document-type specifications: type signature, entity extraction patterns, relationship patterns, structure mapping, provenance template; themselves KB facts that accumulate|mechanism
C11|Self-compaction|System compacts new documents using accumulated grammars and classification rules without external LLM; closing the bootstrap loop|capability
C12|Operational lifecycle|Continuous cycle: intake → processing → rule generation → accumulation; phases blend in practice|process
C13|Runtime programming artifacts|Prolog rules, Python scripts, grammars, compaction rules — four categories of persistent executable capability the LLM creates|category

# seed_layers(id|layer|contents|entry_count|storage_size)
SL1|Language|Sentence templates (~5,000: declarative, interrogative, conditional, relative, participial, coordinated), typo corrections (~15,000), classification patterns (~3,000), weight profiles (~20)|~23,020|~1.4 MB
SL2|Format handling|Parsing + generation grammars for JSON, CSV, markdown, pipe-delimited, Prolog clause, XML/HTML, YAML, SQL result set|~10 grammars|~40 KB
SL3|Operational environment|Primitive selection (~80), pipeline sequencing (~40), data structure selection (~25), compaction entity extraction (~60), relationship mapping (~30), KB management (~35), counter/queue mgmt (~20), error handling (~15)|~305 rules|~60 KB
SL4|Self-maintenance|Novel structure detection (~15), compaction gap detection (~10), snapshot triggers (~8), version comparison (~12), promotion criteria (~10), grammar quality monitoring (~8)|~63 rules|~12 KB
# Total seed: ~23,398 entries, ~1.5 MB, <620ms load time

# bootstrap_stages(id|stage|criterion|capabilities_gained|typical_duration)
BS1|Seeded|All four seed layers loaded and passing self-test|Parse input, generate output, invoke primitives, manage structures|Minutes (one-time)
BS2|Operating|First successful user interaction producing stored findings|Store findings in KB, write Prolog rules, write Python scripts, queue-based multi-instance|First session
BS3|Self-compacting|System compacts known document types without external LLM; 95% fact parity|Compact known doc types autonomously|10-50 sessions
BS4|Self-extending|System creates new grammars for novel document structures without guidance|Create new grammars, compact novel doc types|Continuous from BS3
BS5|Mature|Compaction rules cover >90% incoming types; operational rules cover >80% routine tasks|Routine triage mostly automated|Months of active usage

# lifecycle_phases(id|phase|description|llm_role)
LP1|Intake|Documents enter via web fetch, upload, paste, API; compacted using accumulated grammars and classification rules; facts carry full provenance|Judgment only if ambiguity in entity identification or novel relationship type
LP2|Processing|Existing Prolog rules fire against stored facts; new ingested facts matched by prior rules automatically; contradictions surface; confirmations strengthen confidence|Interpreting rule evaluation results; deciding what matters
LP3|Rule generation|LLM writes Prolog rules (patterns), Python scripts (procedural logic), grammars (novel structures), compaction rules (new doc types)|All four artifact types through command token pipeline at ~8 tokens each
LP4|Accumulation|Session-level state discarded unless LLM promotes to project; project state persists across sessions; snapshots at meaningful points; comparison rules diff state|Judgment on what to promote from session to project

# runtime_artifacts(id|artifact|write_cost|reuse_cost|persistence|amortization)
RA1|Prolog rule|25-40 tokens formalization|0 (fires automatically)|Project/dept/org scope|By 5th use: <10 tokens/use; at org scope: approaches zero
RA2|Python script|20-50 tokens judgment|8 tokens (command to re-execute)|Project KB with provenance|Break-even on 2nd use
RA3|Grammar|Variable (structure analysis)|0 (fires at primitive level)|Project/org scope|Every future doc of that type at zero LLM cost
RA4|Compaction rule|Variable|0 (fires during intake)|Project/org scope|Every future doc of that type compacted autonomously

# sre_accumulation(inv|kb_facts|prolog_rules|python_scripts|cmd_tokens|rules_auto_firing|auto_triage_pct|scripts_reused_vs_written)
1|255|15|3|329|0|0%|0:3
2|325|19|3|127|7|25%|3:0
5|510|34|5|110|18|45%|4:1
10|780|64|8|92|47|65%|7:1
20|1,200|95|12|78|72|78%|10:1
50|2,400|140|18|65|115|88%|16:1
100|4,200|185|24|55|150|93%|22:1

# format_grammars(id|format|structural_token_pct|typical_savings)
FG1|JSON object|55%|110 tokens per 200-token doc
FG2|CSV|50%|200 tokens per 400-token doc
FG3|Markdown table|60%|300 tokens per 500-token doc
FG4|Markdown document|25%|500 tokens per 2,000-token doc
FG5|Pipe-delimited compaction|40%|120 tokens per 300-token doc
FG6|Prolog clause|35%|18 tokens per 50-token doc
FG7|XML/HTML|65%|650 tokens per 1,000-token doc
FG8|YAML|40%|120 tokens per 300-token doc

# template_selection_pipeline(step|input|operation|llm_involved)
TS1|Semantic tuple from LLM|Parse slot types → typed slot set|No
TS2|Typed slot set|Filter templates by slot compatibility → candidate set (20-100)|No (Prolog unification)
TS3|Weight criteria from LLM|Rank candidates by weight match → ranked list|No (Q335 arithmetic)
TS4|Ranked candidates|Select top candidate → one template|No
TS5|Template + content words|Fill slots → complete sentence|No
# Total LLM cost for prose generation: semantic tuple only (~8 tokens)

# multi_instance_topologies(id|topology|pattern|use_case|token_distribution)
MT1|Pipeline|A→Q1→B→Q2→C (3 serial)|Acquire → Analyze → Synthesize|A:40% B:35% C:25%
MT2|Fan-out|A→Q→{B1..Bn}|One source, parallel analysis|A:10%, each Bi:90%/N
MT3|Fan-in|{A1..An}→Q→B|Multiple sources, one synthesizer|Ai:variable, B:synthesis
MT4|Peer|Shared Q, any→any|Collaborative investigation|Even
MT5|Supervisor|S↔Q↔{W1..Wn}|Managed work distribution|S:5% (judgment), Wi:95%/N

# train_as_you_go_properties(id|property|mechanism|conventional_equivalent)
TG1|Immediate|One primitive call (8 tokens); live same turn|Batch retrain cycle
TG2|Inspectable|Readable Prolog clauses + provenance|Opaque weight matrices
TG3|Reversible|Clean retraction removes fact and consequences|Weight poisoning is permanent and diffuse
TG4|Scoped|Same visibility/scope as all data access|No knowledge isolation
TG5|Incremental|Facts at stable integer addresses; no displacement|Catastrophic forgetting
TG6|Auditable|Append-only audit log; every modification traced|No equivalent
TG7|Composable|Rules from different sources interact through structural unification automatically|No automatic composition

# security_attack_scenarios(id|attack|structural_result|reason)
SA1|LLM writes rule granting itself elevated access|Rejected — grant assertion requires admin-level grant|Grants are admin-only writable
SA2|LLM writes rule querying out-of-scope KB|Rule stores but fires with empty results on out-of-scope data|Scope check at query time per fact, not at rule definition time
SA3|LLM writes rule leaking data via side channel|Assert to public KB requires write grant; copy needs read grant on restricted KB|Both grants checked independently
SA4|Malicious document injects harmful rules during compaction|Axiom constraints block prohibited content at assertion time|Constraint evaluation runs on rule content
SA5|LLM accumulates rules that collectively bypass security|Each rule fires against visibility-filtered fact sets independently|Visibility is per-fact at access time, not at rule composition time

# self_compaction_accuracy(stage|docs_processed|fact_parity_vs_external_llm|llm_judgment_needed)
Stage 2|0-20|N/A (external LLM)|N/A
Early stage 3|20-50|~85%|~40% of entities
Mid stage 3|50-100|~92%|~20% of entities
Late stage 3|100-200|~96%|~8% of entities
Stage 4+|200+|~98%|~3% (novel structures only)

# compaction_rule_coverage(domain|rules_at_10_docs|rules_at_50|rules_at_200|coverage_at_200)
SRE incident reports|3|8|14|~95%
Medical papers|4|12|25|~90%
Legal contracts|5|15|30|~85%
API documentation|2|6|12|~92%
Financial reports|3|10|20|~88%
Code repositories|4|11|22|~90%

# dialect_switching(operation|mechanism|token_cost|latency)
Mount dialect KB|Scope change: B359 mount_create|8|<1 ms
Unmount previous|B360 mount_remove|8|<1 ms
Mixed-dialect document|Mount/unmount per segment|16 per switch|<1 ms per switch
Translation (full swap)|Mount target language KB|8|<1 ms
LLM semantic output|Unchanged across all languages|0 additional|0

# relationships(from|rel|to)
P1|enables|C1
P1|enables|C8
P1|enables|C9
P2|enables|C13
P2|produces|RA1
P2|produces|RA2
P2|produces|RA3
P2|produces|RA4
P3|derives_from|P1
P3|implements|C8
P4|constrains|C1
P5|enables|C1
P5|enables|C7
P6|enables|C2
P6|enables|C3
P7|defines|SL1
P7|defines|SL2
P7|defines|SL3
P7|defines|SL4
P8|enables|P2
C1|implements|P1
C1|requires|P4
C2|produces|C3
C3|enables|P6
C4|component_of|SL1
C4|uses|C5
C5|enables|C4
C5|enables|C6
C6|uses|C4
C7|uses|C10
C7|enables|P3
C8|derives_from|C1
C9|opposes|TG5
C10|enables|C11
C11|completes|BS3
C12|composes|LP1
C12|composes|LP2
C12|composes|LP3
C12|composes|LP4
C13|contains|RA1
C13|contains|RA2
C13|contains|RA3
C13|contains|RA4
RA1|amortizes_across|CL2
RA2|enables|CL3
RA3|enables|FG1
RA4|enables|C11
SL1|enables|BS1
SL2|enables|BS1
SL3|enables|BS1
SL4|enables|BS1
BS1|enables|BS2
BS2|enables|BS3
BS3|enables|BS4
BS4|enables|BS5
LP1|feeds|LP2
LP2|feeds|LP3
LP3|feeds|LP4
LP4|feeds|LP1
SA1|prevented_by|P4
SA2|prevented_by|P4
SA3|prevented_by|P4
SA4|prevented_by|P4
SA5|prevented_by|P4
TG1|opposes|TG5
TG3|opposes|TG5
TG5|distinguishes_from|C9

# section_index(section|title|ids)
1|What Self-Extending Means|C1,P1,P5,P8,C9
2|The Compaction Format|C2,C3,P6
3|The Bootstrap Pipeline|P7,SL1,SL2,SL3,SL4,BS1,BS2,BS3
4|The Operational Lifecycle|C12,LP1,LP2,LP3,LP4
5|The LLM as Runtime Programmer|P2,C13,RA1,RA2,RA3,RA4,CL1,CL2
6|The SRE Operational Environment|CL3,CL4,CL5
7|Data Flow Architecture|P5,C7,CL7,MT1-MT5
8|Train-As-You-Go|C9,TG1-TG7,C8,P3
9|Capability Growth Model|C8
10|Security Properties|P4,SA1-SA5
11|Language and Dialect|C4,C5,C6
A|Compaction Format Specification|C3
B|Seed Layer Contents|SL1-SL4,CL6
C|Bootstrap Stage Transitions|BS1-BS5
D|SRE Worked Example|CL3,CL4
E|Rule Amortization|CL1,CL2,RA1
F|Python Script Lifecycle|RA2
G|Queue-Based Coordination|C7,MT1-MT5,CL7
H|Capability Growth Metrics|C8,CL5
I|Security of Self-Generated Rules|P4,SA1-SA5
J|Language KB Structure|C4,C5,C6
K|Compaction Rules as Self-Extending Grammar|C10,C11,CL8

# decode_legend
format: pipe-delimited tables, ID-based cross-references
claim_types: observation|derivation
concept_categories: architecture|process|format|mechanism|property|capability|category|topology
seed_layers: SL1 language|SL2 format|SL3 operational|SL4 self-maintenance
bootstrap_stages: BS1 seeded|BS2 operating|BS3 self-compacting|BS4 self-extending|BS5 mature
lifecycle_phases: LP1 intake|LP2 processing|LP3 rule generation|LP4 accumulation
runtime_artifacts: RA1 Prolog rule|RA2 Python script|RA3 grammar|RA4 compaction rule
train_properties: TG1 immediate|TG2 inspectable|TG3 reversible|TG4 scoped|TG5 incremental|TG6 auditable|TG7 composable
multi_instance: MT1 pipeline|MT2 fan-out|MT3 fan-in|MT4 peer|MT5 supervisor
attack_scenarios: SA1-SA5; all prevented by P4 (security inheritance)
rel_types: enables|derives_from|implements|produces|constrains|requires|defines|component_of|uses|opposes|completes|composes|contains|amortizes_across|feeds|prevented_by|distinguishes_from
+standalone: no cross-references to other compact docs
+no_new_primitives: paper introduces no new primitives; all mechanisms use existing VDR-1 through VDR-18 components
