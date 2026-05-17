# VDR-24 LLM SOFTWARE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → execution_levels → dev_lifecycle → runner_types → data_primitives → topologies → security → economics → relationships → sections

# principles(id|principle|rationale)
P1|Applications are configured LLM sessions, not compiled code|Developed through conversation, deployed as snapshots, improved by usage through rule accumulation
P2|LLM is runtime, KB tree is address space, Prolog is programming language, snapshots are binaries|Every component of conventional software has a structural equivalent in VDR
P3|Three execution levels|Level 1: full LLM judgment (50-500 tokens); Level 2: LLM invokes stored Prolog (8 tokens); Level 3: pure Prolog batch (0 LLM tokens); applications mature from L1 toward L3
P4|KBs are machines not containers|Each KB has state (counters, queues, stacks, rings, bitsets, LRU, locks), logic (Prolog rules), data (provenanced facts), constraints, connections, visibility, grants
P5|Usage improves the application without rebuilding|Each session deposits reusable Prolog rules; future sessions are cheaper and more capable; accumulation curve flattens but never reaches zero for diverse inputs
P6|Security is structure not configuration|Scope walk never traverses siblings; visibility is integer comparison; grants default deny; constraints tighten downward; audit is append-only axiom-protected
P7|Updates are fact changes, not deployments|Policy change = one retraction + one assertion; immediate effect on all future clones; no retraining, no redeployment

# claims(id|claim|type|depends_on)
CL1|Customer support chatbot: 4-8 hours development vs 4-8 weeks conventional|observation|P1
CL2|File processing pipeline: 8-16 hours development vs 8-16 weeks conventional|observation|P1
CL3|SRE accumulation: investigation 1 = 329 tokens; investigation 100 = 55 tokens (83% reduction); 93% auto-triage|observation|P5
CL4|Snapshot sizes typically 10-500 KB because snapshots capture state not knowledge|observation|P2
CL5|Cross-customer data leakage structurally impossible — sibling clones cannot see each other's session KBs|derivation|P6
CL6|Hallucinated facts structurally impossible for KB-sourced data — LLM phrases results from known integer addresses|derivation|P2
CL7|Rule formalization: 25-40 tokens; replaces 150-300 tokens conventional reasoning per use; break-even on first use|observation|P3
CL8|Every builtin (448 total) is a Prolog predicate callable from user-written rules|observation|P2
CL9|Clone isolation guaranteed by scope walk algorithm — goes up to ancestors, down to children, never sideways|derivation|P6
CL10|Stale knowledge detectable (LRU timestamps), retractable (clean removal), verifiable (provenance chain) — unlike weight-based systems|derivation|P5

# concepts(id|name|definition|category)
C1|LLM Software|Software developed by configuring LLM sessions with structured state, encoding logic as Prolog rules over exact arithmetic primitives, deploying as snapshots, improving by usage|category
C2|Snapshot|Atomic capture of all live state: loaded rules, mounted KBs, scope config, data primitive states, working data bindings; typically 10-500 KB; the deployable binary|artifact
C3|Clone|Independent instance forked from snapshot; shares persistent KBs read-only; independent live state; killed at drift threshold and replaced from same snapshot|execution
C4|Drift management|Counters track turns, context saturation, denominator drift, error rate; threshold breach kills clone and spawns fresh from frozen snapshot; freshness guaranteed by policy|mechanism
C5|Development through conversation|User interacts with LLM session, loads data, tests scenarios, encodes correct judgments as Prolog rules; conversation is the IDE|process
C6|Three execution levels|L1: full LLM judgment (50-500 tokens); L2: LLM invokes stored Prolog (8 tokens); L3: pure Prolog batch (0 tokens); maturity = increasing L3 percentage|model
C7|Rule accumulation|Each session deposits reusable Prolog rules at appropriate scope; future sessions cheaper; per-use cost approaches zero at organizational scope|mechanism
C8|Negative accumulation / hygiene|Rules go stale; detected via LRU timestamps + fire/success counters; automated retraction when staleness, failure rate, or grant-orphan thresholds exceeded; clean removal via provenance|mechanism
C9|KB as machine|KB has state (7 data primitives), logic (Prolog rules), data (provenanced facts), constraints (4 types), connections, visibility, grants — wiring machines together = application architecture|model
C10|Clone destination governance|Where clone is placed determines lifecycle, visibility, governance; rules at appropriate scope enforce placement policies structurally|mechanism
C11|Semantic tuple pipeline|LLM emits language-independent semantic tuple (~8 tokens) → Prolog matches sentence template → grammar fills structural tokens → complete prose; deterministic after LLM judgment|mechanism

# execution_levels(level|description|tokens_per_task|llm_role|example)
L1|Full LLM judgment|50-500|Decides every step at runtime|First encounter with novel question type
L2|LLM invoking stored Prolog|8|Recognizes situation matches stored rule, invokes it|Command token to fire return_eligible rule
L3|Pure Prolog batch|0|Not involved; rules fire on triggers/schedules|Automated queue drain, constraint evaluation

# dev_lifecycle(id|phase|mechanism|conventional_equivalent)
DL1|Development|Interactive conversation: load data, write rules, test scenarios|Write code in IDE
DL2|Testing|Run scenarios, verify outputs, inspect provenance chains|Unit tests, integration tests
DL3|Building|Snapshot session atomically|Compile, package
DL4|Deployment|Clone snapshot; clone-per-request, clone-per-task, or long-lived|Container orchestration
DL5|Monitoring|Polling runners reading counters, queue depths, bitsets|External dashboards
DL6|Updating|Change fact or rule; immediate effect on future clones|Code change, rebuild, redeploy
DL7|Scaling|More clones from same snapshot|More containers, load balancers
DL8|Rollback|Clone from earlier snapshot|Redeploy previous container
DL9|Retirement|Archive snapshot KB; queryable indefinitely|Decommission infrastructure

# runner_types(id|type|trigger|tokens_per_activation|lifecycle|grant_scope|conventional_equiv)
RT1|Interactive|User input|50-500|Session duration|User's grants|Web application
RT2|Polling|Timer|10-50|Single cycle, fresh each|System monitoring|Cron job
RT3|Processor|Data arrival|8-30 per item|Long-lived, respawned at drift|Data pipeline|Stream consumer
RT4|Internal processing|Schedule|20-100|Single cycle, fresh each|Read-broad, write-derived|Background service

# data_primitives(id|primitive|mechanism|coordination_role|typical_sizing)
DP1|Counter|Signed integer with min/max clamp; atomic increment/decrement/add/get/reset|Pool management, throughput monitoring, drift detection, rate limiting|min=0 max=10000 throughput; min=-1000 max=1000 drift
DP2|Queue|Bounded FIFO; atomic push/pop; separate read/write positions|Message passing, task distribution; push returns false when full (backpressure)|100-1000 task queues
DP3|Stack|Bounded LIFO; atomic push/pop|Investigation paths, backtracking|16-64 investigation; 8-16 backtracking
DP4|Ring buffer|Fixed-size circular; write overwrites oldest|Rolling metrics, time-series windows|60 per-minute; 24 per-hour
DP5|Bitset|Fixed-width bit array; set/clear/test|Barrier synchronization, progress tracking, feature flags|200 endpoints; 64 feature flags
DP6|LRU cache|Bounded key-value with timestamps; auto-evict least recently used|Memoization, deduplication, failed-approach memory|50-200 approach memo; 1000-5000 dedup
DP7|Lock|Non-blocking binary flag; acquire/release/check; never blocks|Batch consistency signaling, cooperative access|One per KB needing batch writes

# topology_patterns(id|pattern|structure|use_case)
TP1|Waterfall|Queue A → Runner B → Queue C → Runner D|Sequential pipeline, fully decoupled stages
TP2|Fan-out|One queue, multiple consumers (atomic pop)|Work distribution without load balancer
TP3|Fan-in|Multiple producers, one queue, one consumer|Result aggregation
TP4|Peer|Shared queue, any push, any pop|Collaborative processing
TP5|Supervisor|One runner monitors counters/bitsets, spawns/kills workers|Managed pool with auto-scaling

# security_model(id|mechanism|enforcement|attack_prevented)
SM1|Scope walk|Goes up to ancestors, down to children, never sideways; sibling branches structurally unreachable|Cross-customer data leakage; cross-clone contamination
SM2|Visibility|public/internal/owner-only; integer comparison inside query primitive|Unauthorized KB access
SM3|Grants|Default deny on all 44 operational primitives; positive credential required; monotonic state transitions (active→expired/exhausted/revoked, never re-increment)|Privilege escalation; unauthorized operations
SM4|Constraints|Axiom (unsuspendable), operational (suspendable with logging), legal, project; children tighten never loosen|Policy bypass; constraint relaxation
SM5|Audit|Append-only KB protected by axiom constraint against retraction; every query attempt logged|Audit trail tampering
SM6|Self-generated rule safety|Same pipeline: grant check, scope check, constraint eval, provenance; cannot self-elevate grants (admin-only); out-of-scope queries return empty|Rule-based privilege escalation; data exfiltration via rules

# security_scenarios(attack|mechanism|structural_result|reason)
Clone reads sibling session|Scope walk|Empty result|Siblings unreachable by walk algorithm
Runner elevates grants|Grant assertion|Denied|Requires admin grant runner doesn't possess
Rule queries out-of-scope|Rule fires normally|Empty result set|Scope check at query time per fact
Malicious input injects rule|Compaction + assertion|Blocked by constraint|Axiom constraints evaluate rule content
Cross-customer data in chatbot|Session fact query|Empty result|Each clone's session KB is independent branch
Data copy to public KB|Read + write|Denied|Both read grant (source) and write grant (target) checked independently

# accumulation_curve(investigation|l1_tokens|l2_tokens|l3_tokens|total|l3_pct|rules_available)
1|280|49|0|329|0%|15
2|78|41|8|127|6%|19
5|55|40|15|110|14%|34
10|30|32|30|92|33%|64
20|18|22|38|78|49%|95
50|10|12|43|65|66%|140
100|6|8|41|55|75%|185
200|4|5|39|48|81%|220
500|3|4|36|43|84%|260

# accumulation_by_app(application|inv1_tokens|inv10|inv50|inv100|auto_triage_100)
SRE triage|329|92|65|55|93%
Support chatbot|200|80|50|40|85%
Document processing|150|60|35|25|92%
Compliance review|250|100|55|45|88%

# dev_time_estimates(application|data_loading|rule_writing|testing|edge_cases|total|conventional_equiv)
Simple FAQ bot|1 hr|1 hr|1 hr|1 hr|4 hrs|2-4 weeks
Full support chatbot|2 hrs|3 hrs|2 hrs|3 hrs|10 hrs|4-8 weeks
Document processor (single type)|1 hr|2 hrs|1 hr|1 hr|5 hrs|2-4 weeks
Document processor (5 types)|3 hrs|6 hrs|3 hrs|4 hrs|16 hrs|8-16 weeks
SRE triage assistant|2 hrs|4 hrs|3 hrs|3 hrs|12 hrs|6-12 weeks
Monitoring poller|0.5 hrs|1 hr|0.5 hrs|0.5 hrs|2.5 hrs|1-2 weeks

# snapshot_sizes(application|typical_rules|typical_grammars|live_state|est_snapshot_size)
Simple chatbot|30-50|5-10|Minimal|20-50 KB
Full support bot|100-200|15-25|Moderate|50-150 KB
File processor|50-100|10-20|Queue refs, counters|30-80 KB
SRE investigator|150-300|20-30|Investigation state|80-200 KB
Monitoring poller|10-20|2-5|Counter refs|10-20 KB

# drift_thresholds(metric|measured_by|typical_threshold|action)
Turn count|Counter per turn|200|Kill clone, spawn fresh
Context saturation|Counter cumulative tokens|90% model capacity|Kill clone, spawn fresh
Denominator drift|Counter max denom bits|2^48|Kill clone, spawn fresh
Error rate|Counter ratio errors/total|5%|Kill clone, spawn fresh; flag if persistent
Stall detection|Counter turns since new evidence|5 consecutive|Backtrack or kill
Queue backlog|Counter intake depth|Configurable|Spawn additional workers

# rule_lifecycle(state|entry|exit|provenance)
Draft|LLM writes in session scope|Promoted or session ends|Author, turn, session
Active|Promoted to project/org scope|Flagged or retracted|Promotion author, timestamp
Firing|Query matches head|Body evaluation completes|Per-invocation log
Stale|Last-fired exceeds threshold|Review or retraction|Flagged timestamp
Failing|Success rate below threshold|Retraction|Failure counts, threshold
Grant-orphaned|Zero grant successes since creation|Retraction or new grant|Denial counts
Retracted|Manual or automated hygiene|Terminal|Retraction reason, downstream impact

# hygiene_rules(id|rule|detects|action)
HY1|stale_rule(R) :- last_fired(R,T), days_since(T,D), D > 90|Rules not fired in 90 days|Flag for review; retract if not promoted within window
HY2|failing_rule(R) :- fire_count(R,F), F>10, success_count(R,S), S/F < 20/100|Rules with <20% success rate|Retract immediately
HY3|permission_orphan(R) :- grant_denial_count(R,D), D>0, grant_success_count(R,S), S=0|Rules that never successfully execute|Flag; retract if no grant forthcoming

# conventional_mapping(conventional|llm_software|implementation|addressing)
Executable binary|Snapshot|Frozen live state|root.apps.myapp.snapshots.v3
Process|Clone|Independent instance from snapshot|root.sessions.sess_NNNN
Thread pool|Worker clone set|Multiple clones from same snapshot|Polled via counter
Message queue|Queue primitive|Bounded FIFO on KB|root.projects.X.intake
Semaphore|Counter with bounds|Signed integer min/max clamp|root.projects.X.metrics.active_workers
Mutex|Lock primitive|Non-blocking acquire/release|root.projects.X.locks.batch_write
Shared memory|Persistent KB (read-only)|Facts at integer addresses|Any persistent KB path
Process-local memory|Session KB (live state)|Independent per clone|root.sessions.sess_NNNN.*
Config file|Configuration KB|Facts with provenance|root.products.myapp.config
Database|KB subtree|Facts, rules, constraints, grammars|root.data.*
Cron job|Polling runner|Timer-spawned, fresh each cycle|Snapshot + schedule
Daemon|Processor runner|Long-lived, respawned at drift|Snapshot + data connection
Log file|Append-only audit KB|Every operation logged with provenance|root.system.audit
Version control|Snapshot versioning|Multiple snapshots as sibling KBs|v1, v2, v3 siblings
Load balancer|Atomic queue pop|Multiple workers pop from same queue|Queue at shared path
Container|Clone with grants|Isolation via scope + visibility + grants|Session KB + grant set

# failure_mode_comparison(failure|conventional_llm|llm_software|detection_diff)
Hallucinated fact|Occurs silently; undetectable|Structurally impossible for KB-sourced data|Conventional: human spot-check; LM: provenance chain
Wrong arithmetic|Common (digit-by-digit prediction)|Impossible (exact integer primitives)|Conventional: compare calculator; LM: error rate = 0
Policy misapplication|LLM paraphrases incorrectly from RAG|Prolog evaluates rule exactly; LLM phrases result|Conventional: manual audit; LM: rule eval logged
Cross-user data leak|Possible via shared context|Structurally impossible (sibling isolation)|Conventional: pen test; LM: structural proof
Stale information|Permanent in weights; undetectable|Detectable via LRU; retractable|Conventional: unknown until reported; LM: automated detection
Context overflow|Information lost silently|Impossible; state in KBs not context window|Conventional: truncation happens; LM: N/A
Catastrophic forgetting|Fine-tuning damages prior knowledge|Impossible; facts at independent addresses|Conventional: discover after damage; LM: N/A

# llm_app_comparison(property|rag_app|langchain_agent|llm_software)
Orchestration|Developer-written code|Developer-written Python|Prolog rules in KB
State management|External database|External state store|KB facts at integer addresses
Memory across sessions|None (or developer-built)|None (or developer-built)|Automatic via rule accumulation
Policy enforcement|Prompt instructions|Code logic|Prolog rules + constraints
Factual accuracy|Depends on retrieval quality|Depends on tool output|Exact: facts at known addresses
Security|Application-level code|Application-level code|Structural: scope + visibility + grants
Improvement over time|Requires developer|Requires developer|Automatic via usage
Deployment|Application pipeline|Application pipeline|Clone snapshot
Update|Re-index, redeploy|Code change, redeploy|Change fact
Audit trail|If developer built one|If developer built one|Automatic: every operation logged
Developer required|Yes|Yes|No

# not_appropriate_for(id|workload|reason)
NA1|Compute-intensive numerical work|Exact arithmetic slower per-op than float; conventional compiled software provides deterministic performance
NA2|Real-time control|LLM judgment latency incompatible with hard real-time constraints
NA3|Hardware interfacing|Direct hardware access requires conventional drivers
NA4|Graphics|No graphics pipeline
NA5|Domains with too much variety|Accumulation curve may not reach high L3 percentage; diminishing returns on rule investment

# relationships(from|rel|to)
P1|defines|C1
P1|enables|C5
P2|implements|C9
P2|implements|C2
P2|implements|C3
P3|implements|C6
P4|enables|C9
P5|implements|C7
P5|enables|accumulation_curve
P6|implements|SM1
P6|implements|SM2
P6|implements|SM3
P6|implements|SM4
P6|implements|SM5
P7|enables|DL6
C1|contains|C2
C1|contains|C3
C1|contains|C5
C1|contains|C6
C1|contains|C7
C2|enables|C3
C2|enables|DL3
C3|uses|C4
C4|maintains|C3
C5|produces|C2
C6|contains|L1
C6|contains|L2
C6|contains|L3
C7|opposes|C8
C8|maintains|C7
C9|contains|DP1
C9|contains|DP2
C9|contains|DP3
C9|contains|DP4
C9|contains|DP5
C9|contains|DP6
C9|contains|DP7
C10|constrains|C3
C11|implements|P2
RT1|instance_of|C3
RT2|instance_of|C3
RT3|instance_of|C3
RT4|instance_of|C3
TP1|uses|DP2
TP2|uses|DP2
TP3|uses|DP2
TP5|uses|DP1
TP5|uses|DP5
SM1|prevents|CL5
SM6|constrains|C7
CL6|derives_from|P2
CL9|derives_from|SM1
CL10|derives_from|C8
HY1|implements|C8
HY2|implements|C8
HY3|implements|C8

# section_index(section|title|ids)
1|Why a New Category|C1,P1
1.1|The Conventional LLM Problem|CL6
1.2|What LLM Software Is|P1,P5,P7
1.3|What LLM Software Is Not|NA1-NA5
2|The Structural Foundation|P2
2.1|Exact Arithmetic|VDR triple, Q335
2.2|Knowledge Bases|C9,P4
2.3|Prolog|CL8,P3
2.4|Sessions, Snapshots, Clones|C2,C3,C4,CL4,CL9
3|KBs as Machines|C9,P4,DP1-DP7
4|Prolog as Programming Language|P3,C6,L1,L2,L3,CL7,CL8
5|Development Lifecycle|DL1-DL9,C5,P7
6|Runner Types|RT1-RT4
7|Inter-Application Communication|DP1-DP7,TP1-TP5
8|Worked Example: Customer Support|CL1,CL5,CL6
9|Worked Example: File Processing|CL2
10|Copy-on-Write and Versioning|C10,C2
11|Negative Accumulation|C8,HY1-HY3,CL10
12|Security Model|P6,SM1-SM6
13|Economics|CL1-CL3,CL7
14|Memory and Storage Efficiency|C11,interning,typed enums
15|Limitations|NA1-NA5
A|Customer Support Walkthrough|chatbot KB tree, clone lifecycle, policy update
B|File Processing Walkthrough|pipeline KB tree, worker lifecycle, poller cycle
C|Runner Type Comparison|RT1-RT4
D|Data Primitive Usage|DP1-DP7
E|Topology Patterns|TP1-TP5
F|Snapshot Format|C2,CL4
G|Security Scenarios|SM1-SM6
H|Accumulation Metrics|accumulation_by_app
I|Conventional Lifecycle Comparison|DL1-DL9
J|LLM App Comparison|llm_app_comparison
K|Command Token Economics|CL7
L|Rule Lifecycle|rule_lifecycle
M|Snapshot Contents|C2
N|Clone Isolation|CL9,SM1
O|Drift Thresholds|C4,drift_thresholds
P|Capacity Planning|DP1-DP7 sizing
Q|Grant Matrix|SM3
R|Rule Composition Patterns|sequential, conditional, guard, accumulator, delegation, negation, cut, batch
S|Bootstrap Seed|seed layers
T|KB Tree Depth|max 16 levels, scope walk cost = depth
U|Semantic Tuple Pipeline|C11
V|Development Time|dev_time_estimates
W|Accumulation by Level|accumulation_curve
X|Error Classification|failure_mode_comparison
Y|Persistent vs Live State|snapshot captures live; persistent shared read-only
Z|Multi-Language|KB mounting for language/dialect switching
AA|Conventional Software Mapping|conventional_mapping
BB|Failure Mode Comparison|failure_mode_comparison

# decode_legend
format: pipe-delimited tables, ID-based cross-references
category_definition: LLM Software = applications developed through conversation, deployed as snapshots, improved by usage
three_levels: L1 full LLM judgment (50-500 tokens)|L2 LLM invokes stored Prolog (8 tokens)|L3 pure Prolog batch (0 tokens)
kb_as_machine: 7 data primitives (counter, queue, stack, ring, bitset, LRU, lock) + Prolog rules + provenanced facts + constraints + connections + visibility + grants
runner_types: RT1 interactive|RT2 polling|RT3 processor|RT4 internal
topologies: TP1 waterfall|TP2 fan-out|TP3 fan-in|TP4 peer|TP5 supervisor
security: scope walk (never sideways) + visibility (integer compare) + grants (default deny, monotonic) + constraints (tighten-only) + audit (append-only axiom)
snapshot: atomic live state capture; 10-500 KB typical; the deployable binary
clone: independent instance from snapshot; drift-managed via counter thresholds
accumulation: rules deposit per session; cost per task decreases monotonically; L3% increases
hygiene: LRU timestamps + fire/success counters detect stale/failing/orphaned rules; clean retraction via provenance
development_cost: hours of conversation vs weeks of conventional engineering
conventional_mapping: snapshot=binary, clone=process, queue=message queue, counter=semaphore, lock=mutex, persistent KB=shared memory, audit KB=log file
not_for: compute-intensive, real-time control, hardware interfacing, graphics, extreme input diversity
rel_types: defines|enables|implements|contains|uses|maintains|produces|opposes|constrains|prevents|derives_from|instance_of
+standalone: no cross-references to other compact docs
+no_new_primitives: paper introduces no new primitives; all mechanisms use existing VDR-1 through VDR-23 components
