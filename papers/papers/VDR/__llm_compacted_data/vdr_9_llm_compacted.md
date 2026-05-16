# ORCHESTRATED INFERENCE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → loop → notebooks → modes → external data → provenance → boundary → relationships → sections

# principles(id|principle|rationale)
P1|LLM orchestrates, tools compute and deduce|LLM selects and sequences exact tools; neither can conduct multi-step investigation alone; composition covers what each lacks
P2|Orchestrated Inference is a reasoning exoskeleton|External structure compensating for LLM computational unreliability while leveraging its pattern recognition and intent mapping
P3|LLM does not reason — it orchestrates a reasoning process|Token prediction produces orchestration decisions; deterministic tools produce computation and deduction; KB records everything
P4|Conclusions are traceable not guaranteed|Deductive conclusions from correct premises are guaranteed by Prolog; premises might be wrong; evidence might be incomplete; provenance chain makes failures detectable, not preventable
P5|No new primitives, struct fields, or modules|VDR-9 specifies patterns of use over existing VDR-5 through VDR-8 capabilities, not new capabilities

# orchestrated_loop(id|phase|description|who_acts)
OL1|Assess|Read current state (KB, data primitives, pending goals); determine what step is needed next (more evidence? formalize? query? backtrack? conclude?)|LLM (pattern matching over structured state)
OL2|Formalize|Translate needed step into executable form: Prolog rules, Python script, primitive chain, operational command|LLM (creative act — small targeted program for one step)
OL3|Execute|Run the formalized step: Prolog evaluates, Python runs in sandbox, primitive computes, API returns data|Tools (deterministic or logged/grant-gated)
OL4|Store|Result goes into KB location (working data, LRU, Prolog fact, counter, ring buffer) with provenance|System (addressable by dotted path, available for subsequent steps)
OL5|Assess again|Loop returns to assessment with new state including result just stored|LLM

# loop_termination(id|condition|mechanism)
LT1|Goal satisfaction|Prolog query for declared goal succeeds (e.g. root_cause(X, Confidence) where Confidence > 80/100); checked at every assessment
LT2|Budget exhaustion|Counter reaches limit (max steps, max queries, max scripts, max time); transitions to conclude-partial or halt
LT3|Stall detection|Counter tracks iterations since last new evidence; exceeds threshold (default 5) → backtrack or forced conclusion
LT4|User intervention|User cancels, redirects, or requests premature conclusion; overrides loop state

# loop_resource_management(id|counter|purpose|constraint_action)
LR1|steps_executed|Total loop iterations|conclude_partial on budget
LR2|queries_issued|External API/DB queries|no_more_external on budget
LR3|scripts_executed|Python script runs|primitives-only on budget
LR4|hypotheses_tested|Distinct hypotheses evaluated|stop generating, rank existing
LR5|evidence_count|Evidence pieces accumulated|minimum_evidence warns before conclude
LR6|steps_since_evidence|Stall detector; reset on new evidence, increment otherwise|backtrack_or_conclude on threshold

# backtracking(id|aspect|detail)
BT1|Investigation path|Stack (VDR-8) records current exploration direction; backtrack pops stack
BT2|Attempted approaches|LRU (VDR-8) stores abandoned paths with reasons; checked before formalizing new approach to prevent duplicate work
BT3|Triggers|Execution failure, contradictory evidence, hypothesis eliminated, stall detection, confidence collapse, budget approaching, user redirect
BT4|Procedure|Record failure reason → push to attempted LRU → pop investigation stack → check for alternatives at branch point → push new approach or recursive backtrack → log event
BT5|State preservation|Confirmed evidence preserved; path-specific speculation retracted; domain rules preserved; external data reused; step queue cleared

# branching(id|aspect|detail)
BR1|Mechanism|Assessment identifies separable sub-problem → spawn child notebook KB inheriting parent's persistent facts
BR2|Budget allocation|Child draws from parent's remaining budget: >80% remaining → 40% allocation; 50-80% → 25%; <50% → 15%; <20% → no child allowed
BR3|Return|Child investigates independently, returns conclusion to parent; parent loop resumes at assessment with child result as new fact

# inference_notebooks(id|aspect|detail)
NB1|Definition|KB subtree with declared schema housing one inference process; uses existing KB struct without modification
NB2|Contents|Problem statement, inference type, goal, status; step_queue (queue), investigation_path (stack); findings/sources/attempted_steps (LRUs); budget counters; investigation lock; evidence_dimensions (bitset); metric_snapshots (ring); Prolog rules populated during investigation; conclusion facts with derivation; constraints; connections to evidence sources
NB3|Lifecycle|active (loop cycling, primitives mutating) → concluded (conclusions asserted with provenance, lock released) → halted (stopped without conclusion, partial findings preserved) → archived (frozen read-only under root.archive.inference)
NB4|Templates|Pre-defined schemas for common investigation types stored as KBs under root.templates.inference; LLM instantiates template and customizes for specific problem

# four_modes(id|mode|description|tool_signature|confidence_rule)
FM1|Deductive|Given premises and rules, derive what must be true|KB_ASSERT(facts) → KB_ASSERT(rules) → KB_QUERY → exact conclusion|confidence = min(premise confidences); weakest link
FM2|Inductive|Given observations, propose what hypothesis best explains the data|External data → KB_ASSERT(evidence) → Prolog scoring rules → list_sort_by_key → ranked hypotheses|confidence = evidence_coverage × mean(source confidences)
FM3|Abductive|Given observation, infer most likely cause (diagnosis)|KB_ASSERT(observations+causal rules) → KB_QUERY(explanations) → external probes → re-query → Python correlation → ranked causes|confidence = (explained_symptoms/total_symptoms) × min(evidence confidences)
FM4|Analogical|Given known domain and unfamiliar domain, identify structural parallels and transfer conclusions|KB_ASSERT(source structure) → KB_ASSERT(target structure) → Prolog structural matching → strength score → transferred conclusions|confidence = analogy_strength × source_domain_confidence

# mode_composition(id|pattern|flow|use_case)
MC1|Abductive → Deductive|Generate hypotheses → derive implications of each|Diagnosis then prediction
MC2|Abductive → Inductive|Generate hypotheses → score against evidence|Diagnosis with ranking
MC3|Inductive → Deductive|Observe pattern → derive consequences|Discovery then application
MC4|Deductive → Inductive|Derive predictions → check empirically|Theory testing
MC5|Analogical → Deductive|Map structure from known domain → deduce in new domain|Knowledge transfer
MC6|Abductive → Inductive → Deductive|Full investigation cycle|SRE incident: hypothesize → score → derive remediation

# external_data_integration(id|stage|description|tools)
ED1|Acquire|Operational primitive retrieves raw data; grant-gated and logged|net_fetch, ENV_EXEC, fs_read
ED2|Parse|Pure primitives extract structure from raw response|parse_json, parse_csv, string_split
ED3|Convert|Pure primitives convert external values to exact VDR types; conversion boundary declared and logged|to_fraction, to_number
ED4|Store|KB_ASSERT places structured converted data at dotted path in notebook|KB_ASSERT
ED5|Index|Data primitives make data accessible for fast lookup|lru_push, ring_write, bitset_set, counter_inc
ED6|Process|Pure primitives or Python perform analytical operations; derived values stored back|stat_mean, list_filter, ENV_EXEC(Python), list_sort

# conversion_boundary(id|aspect|detail)
CB1|Definition|Declared point where approximate external data enters exact internal system; KB fact asserting source type, original value, converted value, method, max_error
CB2|Exact decimals|Terminating decimals convert exactly (max_error = 0/1)
CB3|Bounded precision|Repeating decimals or declared-precision values have bounded recorded max_error
CB4|Provenance guarantee|Every point where external imprecision enters is declared; provenance chain never silently introduces approximation

# source_confidence(id|source_type|default_confidence|rationale)
SC1|Exact VDR computation|1/1|Mathematically guaranteed
SC2|Prolog derivation (exact premises)|1/1|Logically guaranteed
SC3|Database query result|98/100|Direct read from source of truth
SC4|Prometheus metric (live)|95/100|Instrumentation can have gaps or lag
SC5|Python script output|95/100|Script could have bugs
SC6|Prometheus metric (historical)|90/100|Retention and aggregation may lose detail
SC7|REST API response|85/100|Depends on API reliability and staleness
SC8|Peer-reviewed paper claim|80/100|Peer review provides some verification
SC9|User-stated fact|70/100|Not independently verified
SC10|Web search result|50/100|Unverified, potentially outdated
SC11|LLM-generated content|30/100|Token prediction, not computation

# confidence_propagation(id|step_type|formula|rationale)
CP1|Exact VDR computation|fraction(1,1)|Math is exact
CP2|Prolog derivation|min(C₁,...,Cₙ)|Weakest premise determines chain strength
CP3|Single source evidence|Cs (inherited)|Data carries source reliability
CP4|Multiple sources agree|1 - ∏(1-Cᵢ)|Independent confirmation increases confidence
CP5|Sources conflict|max(Cᵢ) - conflict_penalty|Conflict degrades even strongest source
CP6|Inductive scoring|coverage × mean(Cᵢ)|Partial evidence gives partial confidence
CP7|Abductive ranking|evidence_ratio × min(Cᵢ)|Coverage weighted by evidence quality
CP8|Analogical transfer|strength × Csource|Weaker analogy degrades transferred knowledge
CP9|Python computation|min(inputs) × 95/100|Script could have bugs
CP10|LLM assessment step|30/100 (fixed floor)|LLM judgment is unreliable
CP11|Multi-mode chain|min across mode transitions|Each mode junction is potential weakness

# confidence_thresholds(id|range|label|action)
CT1|95/100 — 1/1|High|Act on conclusion directly
CT2|80/100 — 94/100|Moderate|Act with monitoring, note uncertainty
CT3|60/100 — 79/100|Low|Gather more evidence before acting
CT4|40/100 — 59/100|Speculative|Present as hypothesis, not conclusion
CT5|<40/100|Unreliable|Do not present as conclusion, flag for investigation

# llm_contributions(id|task|description)
LC1|Intent recognition|Read problem, determine investigation type (debugging, research, decision, diagnosis)
LC2|Mode selection|Assess state, determine which inference mode appropriate for next step
LC3|Formalization|Translate problem structure into formal representations (Prolog rules, Python scripts, primitive chains)
LC4|Assessment|Read results from KB, determine meaning (supports hypothesis? stalled? backtrack?)
LC5|Framing|Generate natural language to present results to user

# llm_does_not(id|what|who_does)
LD1|Sort lists|list_sort primitive
LD2|Compute statistics|stat_mean, stat_percentile, vdr_* primitives
LD3|Evaluate logical rules|Prolog engine
LD4|Execute code|Sandboxed operational environments
LD5|Fetch external data|Operational primitives with grants
LD6|Hold complete investigation state|KB at dotted paths; stack, LRU, counters, bitsets

# contradiction_detection(id|type|detection_method|resolution)
CD1|Direct factual|Two facts assert different values for same predicate+args in same scope|Compare provenance — trust more reliable source
CD2|Logical|Prolog derives both P and not(P)|Inspect rule set for over-broad rules
CD3|Statistical|Two sources give significantly different values for same metric|Investigate measurement methodology difference
CD4|Temporal|Fact true at T1 but false at T2|Not contradiction — state change; record transition
CD5|Cross-notebook|Two notebooks reach opposite conclusions from overlapping evidence|Compare evidence sets and reasoning chains

# challenge_mechanism(id|aspect|detail)
CH1|User asserts counter-fact|KB_ASSERT counter-evidence into notebook
CH2|System re-evaluates|Re-runs affected Prolog queries with expanded fact set
CH3|Outcome|Conclusion may survive (rules account for counter-fact), be retracted, or have confidence degraded
CH4|Recording|Challenge and its impact recorded in notebook provenance

# notebook_templates(id|template|inference_type|goal|key_primitives)
NT1|SRE incident|abductive|root_cause with confidence >80/100|counters (queries, hypotheses), LRUs (findings, sources), bitset (deps_checked), lock (investigating), ring (metrics), queue (remediation)
NT2|Bug investigation|abductive|root_cause + fix_verified|LRU (recent_failures), stacks (undo, fix_steps), bitset (resolved), lock (editing), counter (retries)
NT3|Research compilation|inductive|ranked_approaches with coverage >70/100|LRU (papers, sources), counters (found, analyzed), queue (to_analyze), bitset (themes), ring (methodology_notes)
NT4|Decision matrix|deductive|ranked_options with sensitivity_analysis|counters (scored, criteria), ring (discussion), LRU (sources)
NT5|Argument construction|deductive+inductive|valid structure + zero unsupported claims|queue (argument_order), LRU (sources), counters (unsupported, objections_addressed), bitset (evidence_dims)

# falsification_criteria(id|criterion|test_method)
FC1|Prolog deductive conclusion incorrect|Independent verification of derivation from asserted premises and rules
FC2|Provenance chain gap|Conclusion references evidence not present in notebook KB
FC3|Confidence score wrong|Exact VDR fraction comparison against declared propagation rules applied to input confidences
FC4|Missing conversion boundary|External data value in inference system without declared conversion fact
FC5|Challenge not re-evaluated|Assert counter-fact, verify affected derivation chain parts re-evaluated
FC6|Budget exceeded without constraint trigger|Loop exceeds declared budget counter without constraint firing
FC7|Undetectable cross-notebook contradiction|Two notebooks produce contradictory conclusions from same evidence, not detectable by querying both

# claims(id|claim|type)
CL1|LLM does not reason — it orchestrates tools that compute and deduce|core_thesis
CL2|Composition of LLM orchestration + exact tools produces structured inferences neither could produce alone|structural
CL3|Every conclusion carries complete queryable derivation chain with exact confidence scores|provenance
CL4|Confidence is exact VDR fraction computed from declared propagation rules, not vague label|exactness
CL5|Four inference modes compose naturally because they all operate on same KB with same tools|composability
CL6|Failure modes are detectable through provenance chain, not preventable by architecture|honesty
CL7|No new primitives, struct fields, or modules — patterns of use over existing capabilities|architectural_discipline

# relationships(from|rel|to)
OL1-OL5|form|orchestrated inference loop
OL1|uses|VDR-8 data primitives (read state), VDR-5 KB queries
OL2|uses|LLM formalization (Prolog rules, Python, primitive chains)
OL3|uses|VDR-6 primitives + operational environments
OL4|uses|VDR-8 data primitives (store state), VDR-5 KB_ASSERT
FM1|uses|Prolog engine (VDR-5)
FM2|uses|external data (VDR-6 ops) + scoring rules + list_sort
FM3|uses|causal rules + external probes + Python correlation
FM4|uses|structural matching via Prolog
MC1-MC6|compose|FM1-FM4 (modes compose naturally)
ED1-ED6|pipeline|external data into exact system
CB1-CB4|declare|approximation entry points
SC1-SC11|feed|CP1-CP11 (confidence propagation)
CP1-CP11|produce|CT1-CT5 (actionable confidence levels)
BT1-BT5|use|VDR-8 stack + LRU for exploration memory
BR1-BR3|use|VDR-5 KB scoping for child notebooks
NB1-NB4|use|VDR-8 KB struct (all fields, no modifications)
CD1-CD5|detectable_by|Prolog queries over notebook facts
CH1-CH4|trigger|re-evaluation of derivation chains
NT1-NT5|instantiate|NB1-NB4 (notebooks from templates)
CL7|confirms|P5 (no new capabilities added)

# section_index(section|title|ids)
1|What Orchestrated Inference Is and Is Not|P1-P4
2|The Orchestrated Inference Loop|OL1-OL5,LT1-LT4,LR1-LR6,BT1-BT5,BR1-BR3
3|Inference Notebooks|NB1-NB4,NT1-NT5
4|The Four Inference Modes|FM1-FM4,MC1-MC6
5|External Data Integration|ED1-ED6,CB1-CB4,SC1-SC11
6|Inference Provenance|CP1-CP11,CT1-CT5,CH1-CH4
7|Worked Example: SRE Incident|full 7-iteration investigation through all phases
8|Worked Example: Bug Investigation|common dependency via Prolog, instrumented trace, fix verification, permanent code smell rule
9|Worked Example: Research Compilation|gather→score→gap analysis→combination analysis with coverage tracking
10|Worked Example: Argument Construction|evidence gathering with source strength tracking, Prolog validation of argument structure, objection/rebuttal management
11|Worked Example: Email Thread Analysis|structural parsing → Prolog rules for resolved/contested/unanswered → exact analysis not summarization
12|Boundary Between Orchestration and Reasoning|LC1-LC5,LD1-LD6
13|Falsification Criteria|FC1-FC7
A|Loop State Machine|8 states, transitions, invariants
B|Notebook Schema|required fields, required primitives, optional fields, lifecycle states
C|Mode Tool Signatures|detailed tool chains per mode, composition patterns, mode selection heuristics, source confidence table
D|External Data Pipeline|per-source-type pipeline stages, conversion boundary records, freshness tracking
E|Confidence Propagation Rules|per-step-type formulas, computation examples, action thresholds
F|Backtracking Reference|triggers, procedure, state preservation rules
G|Notebook Templates|5 templates (SRE, bug, research, decision, argument) with pre-populated schemas
H|Contradiction Detection|5 types, detection rules, 7 resolution strategies
I|Provenance Schema|conclusion record, evidence reference, 9 provenance query patterns
J|Resource Budget|8 budget parameters, sub-notebook allocation rules
K|Cross-Domain Pattern Comparison|tool usage frequency, data primitive usage, complexity estimates across 11 domains
L|Session Management Interaction|inference across session boundaries, inference in disposable clones, concurrent notebooks
M|LLM Failure Modes|10 orchestration errors with detection and mitigation, error detection by loop phase, recovery patterns
N|Cumulative Statistics|unchanged from VDR-8: 333 primitives, 37 modules, 24 KB struct fields; VDR-9 adds ~80-120 tests

# decode_legend
loop_phases: assess | formalize | execute | store | (back to assess)
loop_exits: goal_satisfaction | budget_exhaustion | stall_detection | user_intervention | backtrack | branch | conclude | halt
inference_modes: deductive | inductive | abductive | analogical
notebook_states: active | concluded | halted | archived
confidence: exact VDR fraction computed from declared propagation rules; not vague labels
conversion_boundary: declared point where external approximate data enters exact internal system
exoskeleton: external structure compensating for LLM unreliability while leveraging its strengths
claim_types: core_thesis | structural | provenance | exactness | composability | honesty | architectural_discipline
rel_types: form | uses | compose | pipeline | declare | feed | produce | detectable_by | trigger | instantiate | confirms
unchanged_from_vdr8: 333 primitives (289 pure + 44 operational), 37 modules, 24 KB struct fields; VDR-9 adds patterns not capabilities
