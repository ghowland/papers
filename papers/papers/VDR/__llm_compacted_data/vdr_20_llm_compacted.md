# VDR-20 OPERATIONAL DEPLOYMENT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → runner_types → directories → coverage → task_lifecycle → concurrency → scaling → relationships → sections

# principles(id|principle|rationale)
P1|Runners differ only in trigger and grants|All four runner types share identical VDR infrastructure — same primitives, same KB access model, same audit; differentiation is trigger pattern and grant scope only
P2|Fresh LLM every cycle|Pollers and internal processors terminate after each cycle; processors respawn at threshold; no attention degradation; accumulated knowledge at integer addresses
P3|Owner directs, system executes|Owner uses any tool for planning; every decision becomes facts and rules that runners execute; planning tool irrelevant, output format irrelevant
P4|Coverage Remainder is operational|Coverage gap is not a percentage — it is a typed, decomposable, actionable description of specific missing items; queryable like knowledge
P5|Local first|Local directories as bootstrap path: zero external dependencies, validates pipeline in isolation, builds owner confidence on known material
P6|Directory interface as control surface|Owner drops files in designated directories; pollers detect and route; no API keys, no authentication complexity for owner interaction
P7|All security from VDR-16|Multi-runner deployment introduces no new access paths; every runner operates through same primitive pipeline with same visibility, scope, grants, audit
P8|Knowledge efficiency increases monotonically|Compaction rules, classification rules, meta-rules accumulate; LLM judgment per document decreases; cost per ingestion falls over system lifetime

# claims(id|claim|type|depends_on)
CL1|Four runner types cover all operational patterns: human-driven, timer-driven, stream-driven, self-directed|observation|P1
CL2|No runner can escalate its own grants; grant modification requires admin grants no runner holds|observation|P7
CL3|Coverage loop is standard task chains — no special mechanism; tasks trigger tasks through template instantiation|derivation|P4
CL4|After 200+ owner hierarchy corrections, proposal accuracy reaches ~99%|observation|P3
CL5|Avg tokens per compaction: 180 at hour 2 → 18 at day 30 → 8 at year 1|observation|P8
CL6|Rule-handled percentage: 15% day 1 → 88% month 1 → 97% year 1|observation|P8
CL7|Owner time investment: 2-4 hrs/week initial → 0.25-0.5 hrs/week at month 6+|observation|P3
CL8|Cross-runner collusion cannot bypass security; per-session visibility checks on every fact access regardless of initiation path|observation|P7
CL9|Concurrent KB access requires no locking — append-only arenas, atomic queue ops, snapshot consistency|observation|
CL10|Query latency <1ms up to 1M facts; <5ms at 50M facts|observation|
CL11|Meta-rules about document structure in general accelerate every future ingestion regardless of domain|derivation|P8

# concepts(id|name|definition|category)
C1|Prompt runner|LLM instance bound to VDR session; has session identity, scope position, grants; differentiated by trigger pattern and grant scope|architecture
C2|Interactive runner|Human-facing; activates on user input; inherits authenticated user grants; reactive; idle between interactions|runner_type
C3|Polling runner|Timer-driven; spawns fresh each cycle; checks queues, counters, triggers, directory watch lists; routes work; terminates after cycle|runner_type
C4|Processor runner|Maintains persistent data connection (stream, webhook, file watcher); long-lived with periodic respawn; compacts and stores data in real time|runner_type
C5|Internal processing runner|Self-directed; evaluates KB state on schedule; consistency checks, derived facts, coverage gaps, coverage metrics; read-broad, write-derived-only|runner_type
C6|Owner-local interface|Filesystem directory conventions watched by pollers: ingress, tasks, config, output, review|interface
C7|Coverage loop|Topic specification → coverage evaluation → Remainder as gap descriptions → gap-to-task conversion → fetch → compact → re-evaluate; continues until targets met|mechanism
C8|Coverage Remainder|Typed decomposable list of specific gaps (not percentage); each gap is queryable fact with enough specificity to become fetch task|mechanism
C9|Meta-rules|Rules about document structure in general — how reference material differs from narrative, how cross-referencing works, how hierarchies map to KB trees; accelerate all future ingestion|capability
C10|Task chaining|Completed task triggers follow-up tasks via template instantiation; coverage loop implemented as standard task chains|mechanism
C11|Manifest|Processing record per file: path, hash, type, compaction rule used, target KB, facts extracted, timestamp, processor session|tracking
C12|Hierarchy convergence|System proposes KB hierarchy from classification rules; owner corrects; corrections become rules; proposals improve: ~40% accuracy initial → ~99% after 200 corrections|process
C13|Gap-to-task conversion|Pollers read coverage metrics, find Remainders with actionable content, convert each gap into fetch task with metadata: which gap, priority, success criteria|mechanism
C14|Processor respawn|At configurable turn threshold, processor snapshots connection + session state as KB facts, terminates; fresh clone reads snapshot, re-establishes connection, resumes|mechanism

# runner_comparison(id|property|interactive|polling|processor|internal)
RC1|Trigger|User input|Timer interval|Data arrival on stream|Scheduler interval
RC2|Lifecycle|Session duration|One cycle|Long-lived with respawn|One cycle
RC3|LLM freshness|Fresh per session|Fresh per cycle|Fresh per respawn|Fresh per cycle
RC4|Compute priority|Highest|Lowest|Medium|Lowest
RC5|Session identity|Authenticated user|System poller|Service identity|System evaluator
RC6|Typical tokens per activation|50-500|10-50|8-30 per item|20-100
RC7|KB read|User's visible scope|System queues + manifests|Designated source KBs|Broad project read scope
RC8|KB write|User's writable scope|Queue + manifest|Designated target KBs|Derived facts + metrics only
RC9|External access|Via user grants|Filesystem watch paths|Credentialed connections|None
RC10|Grant escalation|No|No|No|No

# directories(id|directory|purpose|watched_by|write_access|read_access)
D1|/vdr/ingress/|Owner drops files for compaction|Ingress poller|Owner (external)|Ingress poller
D2|/vdr/tasks/|Owner drops task specifications|Task poller|Owner (external)|Task poller
D3|/vdr/config/|Owner drops configuration changes|Config poller|Owner (external)|Config poller
D4|/vdr/output/|System deposits results|Output processor|Designated runners|Owner (external)
D5|/vdr/review/|System deposits items needing owner judgment|Review processor|Designated runners|Owner (external)
D6|/vdr/manifests/|Processing records|Manifest writer|Pollers + processors|All runners (read)

# file_routing(id|extension|detected_type|default_target|pipeline)
FR1|.txt|Plain text|Classification-dependent|Classify → route → compact
FR2|.md|Markdown|Classification-dependent|Markdown grammar → extract → classify → route
FR3|.json|JSON data|Classification-dependent|JSON grammar → parse → classify → route
FR4|.csv|Tabular data|Classification-dependent|CSV grammar → parse → classify → route
FR5|.py|Python source|root.programming.python|Python compaction rules → extract
FR6|.zig|Zig source|root.programming.zig|Zig compaction rules → extract
FR7|.c/.h|C source/header|Classification-dependent|C compaction rules → extract → cross-ref
FR8|.pdf|PDF document|Classification-dependent|PDF extract → text → classify → route
FR9|.pl/.pro|Prolog source|Direct load|Parse as Prolog clauses → assert directly
FR10|.task|Task specification|Task queue|Parse → validate → enqueue
FR11|.config|Configuration|System config KB|Parse → validate → assert

# coverage_metric_schema(field|type|description)
topic|path|KB path for the topic
depth_target|atom|Specified depth level
total_target_items|integer|Items needed for target
covered_items|integer|Items with sufficient facts
coverage_value|Q335|Covered/total as exact fraction
remainder_count|integer|Number of specific gaps
remainder_items|list(ref)|References to gap descriptions
evaluated_at|integer|Timestamp
evaluator_session|integer|Which internal processor

# gap_schema(field|type|description)
gap_id|integer|Unique identifier
topic|path|Parent topic
missing_item|string|What's absent
gap_type|atom|api_coverage / examples / cross_reference / error_handling
priority|integer|Derived from depth target and gap type
suggested_source|path or URL|Where to find it
blocking|list(ref)|Other gaps this blocks
addressed_by|ref or null|Task created to fill this gap

# task_states(from|to|trigger|action)
—|created|File in tasks dir or runner enqueue|Raw task exists
created|parsed|System compacts task spec|Typed task facts in KB
parsed|validated|Grant check passes|Cleared for execution
parsed|rejected|Grant check fails|Logged with missing grant; review item
validated|queued|Priority assigned|In priority queue
queued|assigned|Scheduler selects runner|Runner bound to task
assigned|executing|Runner begins work|Primitives invoked
executing|completed|Work finished|Results stored; follow-ups triggered
executing|failed|Error during execution|Logged; retry or escalate
failed|queued|Retry rule fires|Re-enters queue with retry count incremented
failed|abandoned|Max retries exceeded|Logged; review item if configured

# task_chain_templates(trigger_type|followup_type|instantiation)
fetch|compact|Target = fetched file path
compact|coverage_evaluate|Target = affected KB branch
coverage_evaluate|fetch (per gap)|One task per gap with priority
reorganize|coverage_evaluate|Target = reorganized branch
compact|cross_reference|Target = newly compacted KB + related KBs

# task_action_types(id|type|target|description)
TA1|fetch|Path or URL|Retrieve content from source
TA2|compact|Document|Process into KB facts
TA3|reorganize|KB path|Move facts between branches, update scope
TA4|analyze|KB scope|Coverage evaluation, consistency checks
TA5|report|Query spec|Generate formatted output from KB queries
TA6|export|Output path + format|Write KB content to files

# concurrency_model(resource|read_pattern|write_pattern|contention)
KB fact table|Non-blocking snapshot read|Atomic bump-pointer append|Zero — reads and writes independent
KB predicate index|Non-blocking lookup|Append on new fact|Minimal — atomic update
Task queue|Atomic dequeue|Atomic enqueue|Zero — separate read/write positions
Counter|Atomic read|Atomic increment|Zero — single instruction
Coverage metrics KB|Non-blocking read|Periodic bulk write by internal processor|Minimal — infrequent writes
Manifest KB|Non-blocking read|Append per processed file|Zero — append-only
Audit KB|Non-blocking read (rare)|Append per operation|Zero — append-only
Arena allocator|N/A|Atomic bump pointer|Zero — one instruction

# local_sources(id|source|volume|file_count|format_uniformity|cross_ref_density|compaction_rules_needed)
LS1|Project Gutenberg|5-50 GB|60,000+|High (standard headers)|Medium (author/period/theme)|2-3 base + literary extraction
LS2|Unix man pages|50-200 MB|5,000-15,000|Very high (standard sections)|High (SEE ALSO explicit)|1-2
LS3|Linux kernel source|1-2 GB|50,000+|Low (many file types)|Very high (code cross-refs)|8-12
LS4|Python source + docs|200-500 MB|10,000+|Medium|High (module cross-refs)|4-6
LS5|Zig source + docs|100-300 MB|5,000+|Medium|High|4-6

# hierarchy_convergence(corrections|proposal_accuracy|new_rules|cumulative_org_rules)
0|~40% (filesystem-derived)|0|Seed layer 3 only
5|~55%|8|Seed + 8
10|~70%|14|Seed + 14
20|~82%|22|Seed + 22
50|~93%|35|Seed + 35
100|~97%|42|Seed + 42
200+|~99%|45 (plateau)|Seed + 45

# token_efficiency(time|avg_tokens_per_compaction|llm_judgment_pct|rule_handled_pct|meta_rules)
Hour 2|180|85%|15%|0
Hour 8|95|55%|45%|2
Hour 24|52|30%|70%|8
Day 3|38|20%|75%|15
Day 7|28|12%|82%|22
Day 14|22|8%|85%|28
Day 30|18|5%|88%|32

# owner_time(phase|duration|hours_per_week|activities)
Initial setup|Day 1|2-4|Hierarchy design, coverage targets, directory config
Active bootstrap|Days 2-7|3-5|Hierarchy corrections, coverage adjustments, review items
Guided growth|Weeks 2-4|1-2|Audit spot-checks, priority adjustments, new topics
Autonomous operation|Month 2+|0.5-1|Periodic audits, occasional corrections, new sources
Mature system|Month 6+|0.25-0.5|Rare corrections, strategic direction changes only

# scaling(dimension|metric|value)
100K facts|Storage|~50 MB
100K facts|Query latency|<1 ms
1M facts|Storage|~500 MB
1M facts|Query latency|<1 ms
10M facts|Storage|~5 GB
10M facts|Query latency|<2 ms
50M facts|Query latency|<5 ms
5 runners|Hardware|1 GPU + CPU
10 runners|Throughput|~500 tasks/hr, ~50K facts/hr
25 runners|Hardware|2-4 GPU + CPU
100+ runners|Throughput|~10K+ tasks/hr, ~1M+ facts/hr

# health_monitoring(metric|normal_range|alert_threshold|alert_rule)
Poller cycle time|<5 sec|>30 sec|poller_slow(P) :- cycle_time(P,T), T > 30
Task queue depth|0-50|>200|queue_backlog(Q) :- depth(Q,D), D > 200
Processor throughput|Source-dependent|<50% stream rate|processor_behind(P) :- rate(P,R), stream_rate(P,S), R < S*0.5
Internal processor cycle|<60 sec|>300 sec|evaluator_slow(E) :- cycle_time(E,T), T > 300
KB growth rate|Source-dependent|Zero for >2 hrs during ingestion|ingestion_stalled :- growth_rate(0), active_tasks > 0
Compaction error rate|<5%|>15%|compaction_degraded :- error_rate(R), R > 0.15

# security_attacks(id|vector|target|structural_defense)
ATK1|Malicious file in ingress|Compaction pipeline|LLM bounded by grants; command tokens validated; no escalation
ATK2|Crafted task file|Task execution|Validated against requester grants before execution
ATK3|Coverage gap manipulation|Fetch unauthorized data|Fetch task validated against processor grants; restricted KBs unreachable
ATK4|Cross-runner collusion|Collective access escalation|Per-session visibility on every fact access; composition cannot bypass
ATK5|Queue poisoning|Inject unauthorized tasks|Tasks validated at execution not creation; executor grants checked
ATK6|Processor credential theft|Use API credentials|Credentials in processor grant set only; other runners lack access
ATK7|Health metric spoofing|Hide problems|Evaluator cross-checks multiple sources; anomalies flagged

# grant_matrix(operation|interactive|polling|processor|internal|owner)
KB query own scope|Granted|System scope|Designated KBs|Evaluation scope|Full
KB query cross-scope|Denied|Denied|Denied|Read across projects|Denied
KB assert own scope|Granted|Manifest only|Designated KBs|Derived facts only|Full
KB retract|Own facts|Denied|Denied|Denied|Full
Queue enqueue|Task queue|Task dispatch|Result queue|Gap queue|Full
Queue dequeue|Denied|Task + coverage queues|Task queue|Denied|Denied
Filesystem read|User grant|Watch paths|Source paths|Denied|Full
Filesystem write|User grant|Manifest dir|Denied|Denied|Full
Network fetch|User grant|Denied|Credentialed|Denied|Owner grant
Docker execute|User grant|Denied|Denied|Denied|Full
Rule assert|Own scope|Denied|Designated KB|Derived rules|Full
Rule retract|Own scope|Denied|Denied|Denied|Full
Coverage metric write|Denied|Denied|Denied|Granted|Denied
Grant modification|Denied|Denied|Denied|Denied|Admin grant required

# relationships(from|rel|to)
P1|enables|C1
P1|constrains|C2
P1|constrains|C3
P1|constrains|C4
P1|constrains|C5
P2|implements|C3
P2|implements|C5
P2|implements|C14
P3|enables|C6
P3|implements|C12
P4|enables|C7
P4|enables|C8
P4|enables|C13
P5|enables|LS1
P5|enables|LS2
P5|enables|LS3
P5|enables|LS4
P5|enables|LS5
P6|implements|C6
P6|implements|D1
P6|implements|D2
P6|implements|D3
P6|implements|D4
P6|implements|D5
P7|constrains|C1
P7|constrains|ATK1
P7|constrains|ATK2
P7|constrains|ATK3
P7|constrains|ATK4
P7|constrains|ATK5
P7|constrains|ATK6
P8|enables|C9
P8|implements|CL5
P8|implements|CL6
C1|supertype_of|C2
C1|supertype_of|C3
C1|supertype_of|C4
C1|supertype_of|C5
C6|uses|C3
C6|contains|D1
C6|contains|D2
C6|contains|D3
C6|contains|D4
C6|contains|D5
C7|uses|C5
C7|uses|C3
C7|uses|C4
C7|uses|C8
C7|uses|C10
C7|uses|C13
C8|enables|C13
C9|derives_from|P8
C10|implements|C7
C11|uses|D6
C12|requires|P3
C13|enables|C7
C14|enables|P2
CL1|derives_from|P1
CL2|derives_from|P7
CL3|implements|C10
CL4|implements|C12
CL5|derives_from|P8
CL8|derives_from|P7
CL9|enables|C1
CL11|derives_from|C9

# section_index(section|title|ids)
1|From Architecture to Running System|P1,C1
2|Prompt Runner Architecture|C1,C2,C3,C4,C5,P1,P2,CL1
3|The Owner-Local Interface|C6,P6,D1-D6,C11,C12
4|The Interactive Interface|C2,P3
5|The Coverage Loop|C7,C8,P4,C13,C10,C9,CL3
6|Local Directory Bootstrap|P5,LS1-LS5,C12
7|The Owner's Role|P3,CL4,CL7
8|Thread Specification|C14,P2,CL9
9|Task Specification Format|TA1-TA6,C10
10|Worked Example|CL5
11|Security in Multi-Runner Deployment|P7,CL2,CL8,ATK1-ATK7
12|Scaling|CL10
A|Runner Specification|RC1-RC10
B|Directory Interface|D1-D6,FR1-FR11
C|Coverage Metrics|C8
D|Task Lifecycle|TA1-TA6
E|Concurrency Model|CL9
F|Worked Example Timeline|CL5,CL6
G|Local Data Sources|LS1-LS5
H|Hierarchy Convergence|C12,CL4
I|Health Monitoring|
J|Security Matrix|ATK1-ATK7
K|Scaling Projections|CL10
L|API Interface|
M|Owner Workflow Patterns|P3,CL7

# decode_legend
format: pipe-delimited tables, ID-based cross-references
claim_types: observation|derivation
concept_categories: architecture|runner_type|interface|mechanism|capability|process|tracking
runner_types: C2 interactive|C3 polling|C4 processor|C5 internal processing
directories: D1 ingress|D2 tasks|D3 config|D4 output|D5 review|D6 manifests
task_types: TA1 fetch|TA2 compact|TA3 reorganize|TA4 analyze|TA5 report|TA6 export
task_states: created→parsed→validated→queued→assigned→executing→completed|failed→queued(retry)|abandoned
local_sources: LS1 Gutenberg|LS2 man pages|LS3 Linux kernel|LS4 Python|LS5 Zig
attack_vectors: ATK1-ATK7; all defended by structural grant/visibility checks
health_alerts: Prolog rules on KB facts; fire as standard rule evaluation
coverage_loop: topic spec → evaluate → Remainder as gaps → gap-to-task → fetch → compact → re-evaluate
concurrency: append-only arenas, atomic queue ops, snapshot consistency; zero locking
rel_types: enables|constrains|implements|uses|contains|supertype_of|derives_from|requires|enables
+standalone: no cross-references to other compact docs
+no_new_primitives: paper introduces no new primitives, builtins, struct fields, or modules; all mechanisms use existing VDR-1 through VDR-19 components
