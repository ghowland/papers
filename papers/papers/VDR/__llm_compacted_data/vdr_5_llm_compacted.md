# EXACT ARITHMETIC MEETS LOGICAL PROVENANCE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → three layers → prolog → scoped KBs → working data → constraints → topics → surfacing → accounts → memory → relationships → sections

# principles(id|principle|rationale)
P1|Provenance, constraints, and conversational state are architectural requirements not afterthought features|Bolting them on after the fact creates drift between system and metadata
P2|Exact arithmetic makes provenance meaningful|Recorded derivation chain is exact, not approximate; verification is exact comparison not tolerance
P3|Scoped knowledge eliminates cross-contamination|Lexical scoping applied to knowledge; out-of-scope KBs are not searched, not deprioritized
P4|KB data is retrieved not generated|Data surfaced from KBs cannot be hallucinated because it bypasses LLM token generation
P5|Constraints belong inside the KB they govern|Separating constraints from KB creates same drift as separating docs from code (Addendum A1)
P6|User accounts are KBs|Identity, preferences, permissions, conversation state are facts in account KB; org hierarchy is KB tree (Addendum A2)

# three_layers(id|layer|provides|foundation)
TL1|Arithmetic (VDR)|Every number exact fraction; zero drift; zero silent truncation|VDR-1 through VDR-3, 507 tests, 0 errors
TL2|Logic (Prolog)|Every value has derivation chain; every constraint declared and verified; every dependency queryable|Custom Prolog-style KB engine for LLM provenance
TL3|Conversation (Scoped KBs + Working Data + Topics + Constraints)|Knowledge scoped to topics; variables persist in working data; topics have lifecycle; constraints activate/deactivate with scope|Structured memory surviving topic switches

# three_deficiencies(id|deficiency|why_unfixable_by_scale)
TD1|Values without provenance|Computation is opaque float tensor chain; no systematic way to tell correct from hallucinated
TD2|Approximate arithmetic|Every number 16/32-bit float; every op silently truncates; platform-dependent rounding makes runs non-reproducible
TD3|Stateless conversation|No structured memory; no scoped variables; facts from different topics mixed in flat token sequence; context window overflow

# prolog_engine(id|component|detail)
PE1|Terms|Core Prolog (atom, variable, list) + VDR arithmetic (fraction, fraction_vec, fraction_mat) + Q-basis (qbasis, qbasis_vec, qbasis_mat) + references (parameter, layer, token, token_seq) + provenance (derivation, constraint, checkpoint, gradient, loss, step) + conversation (topic, binding, scope, constraint_set)
PE2|Facts|Predicate with typed args; carries kb_source, asserted_at turn/step, optional derivation; e.g. parameter_value("layer.1.weight[0][0]", step(0), fraction(1,4))
PE3|Rules|Head :- Body implications; e.g. depends_on(X,Y) :- derived_from(X,_,Sources), member(Y,Sources) with transitive closure
PE4|Knowledge bases|Named collection of facts+rules+constraints; organized in tree mirroring topic structure; child KBs inherit from parent; active topic determines search scope
PE5|Unification|Standard Prolog unification extended with exact rational comparison (cross-multiplication of exact integers); fraction(1,2) unifies with fraction(2,4)
PE6|Query engine|Depth-first search with backtracking; scoped KB search (current→parent→...→global); first in-scope match wins (cut); cross-scope via query_in() or query_across() with tagged results

# scoped_kbs(id|aspect|detail)
SK1|Scoping principle|Query searches only in-scope KBs: active topic's KB, ancestor KBs, global KB; out-of-scope KBs invisible, not deprioritized
SK2|Automatic disambiguation|Ambiguous terms resolve by scope; "bank" in finance KB = institution, in geography KB = river edge; scope is disambiguator, no heuristics
SK3|KB activation|Topic switch deactivates old KB tree, activates new; parent chain to global stays; deactivation preserves facts, just removes from scope
SK4|Cross-scope queries|Explicit: query_in(kb_name, pred, args) for specific KB; query_across(pred, args) for all KBs with tagged results; no silent mixing
SK5|KB search order|Active topic KB → parent → grandparent → ... → global → secondary scopes (if explicit); cut on first match

# kb_structure(id|field|type|purpose)
KS1|name|Text|Unique identifier
KS2|facts|FactSet|Stored facts
KS3|rules|RuleSet|Logical rules
KS4|constraints|[]Constraint|Local constraints (Addendum: moved from separate system into KB)
KS5|parent|?Text|Parent KB for inheritance
KS6|children|[]Text|Child KB names
KS7|topic|?Text|Associated topic
KS8|working_data|?WorkingDataSet|Scoped variable bindings
KS9|visibility|enum(public,internal,owner_only)|Access control level
KS10|frozen|bool|Read-only flag (snapshot)
KS11|owner|?Text|Owning user/group (Addendum)

# working_data(id|aspect|detail)
WD1|Scoped variable storage|Named collection of bindings attached to topic; nested dict with exact VDR terms; scope determines visibility
WD2|Assertion|User says "Bob is 32" → binding(kb_characters_a, "bob_age", number(32)) stored in correct scope
WD3|Inheritance and shadowing|Lookup walks current dataset up to root like lexical scoping; parent value inherited if not overridden locally
WD4|History|Every binding logged with turn number; "when did we decide Bob was 32?" has exact answer
WD5|Snapshots and diffs|Frozen copy at point in time; structured comparison: added/removed/changed bindings with exact values
WD6|Type discipline|Bindings carry exact VDR types; schema enforcement prevents type errors (number vs atom)
WD7|Operations|set, get, delete, list, list_local, snapshot, restore, diff, merge, clear — all logged

# constraint_system(id|aspect|detail)
CS1|First-class objects|Structured object in KB with name, scope, status, condition, violation policy, activation time, source
CS2|Four domains|Operational (system-level, always on), axioms (mathematical invariants, cannot suspend), legal/policy (external requirements, activatable), project (user preferences and rules)
CS3|Constraint sets|Named groups; enable/disable/intersect/union/diff as group operations
CS4|Exact verification|Because every value is exact VDR fraction, constraint checking is exact; sum-to-one is 1/1 or it isn't; no epsilon
CS5|KB-local (Addendum)|Constraints live inside the KB they govern; activate/deactivate with KB; snapshot with KB; portable with KB
CS6|Constraint inheritance|Inherit through KB tree like facts; child KB constraints add to parent's; same-name constraint in child overrides parent; override logged with provenance
CS7|Effective constraints|Union of local + inherited constraints at any point; merge rule: local same-name overrides parent version for that child and descendants

# constraint_types(id|type|domain|can_suspend|verification)
CT1|sum_to_one|axiom|No|Exact fraction sum == 1/1
CT2|non_negative|axiom|No|Every fraction >= 0/1
CT3|gradient_consistent|axiom|No|w_new == w_old - lr*grad exactly
CT4|denominator_bounded|operational|Yes|Denominator <= declared bound
CT5|exact_arithmetic|operational|No|No float operations
CT6|rate_limit|operational|Yes|Queries per hour <= bound
CT7|gdpr_compliance|legal|Yes|No PII in specified outputs
CT8|code_review|policy|Yes|Changes have review approval
CT9|approved_languages|project|Yes|Code uses approved language set
CT10|character_consistent|conversation|Yes|Character facts match declared values

# constraint_status_transitions(id|from|to|trigger)
CST1|active|satisfied|Verification passes
CST2|active|violated|Verification fails
CST3|active|suspended|User or system suspends
CST4|active|parked|Topic parked
CST5|suspended|active|Reactivated
CST6|parked|active|Topic resumed
CST7|violated|active|Issue fixed, reverified
# All transitions logged with turn, source, reason

# topic_management(id|aspect|detail)
TM1|Topics as structured objects|Name, status (open/closed/parked/branched), timestamps, parent/children, pending items, associated constraint set and working data
TM2|Lifecycle|open → work → close; or open → interrupted → park → resume → work → close; tracked explicitly with rules
TM3|Auto-close rule|Topic should close when no pending items and no open children
TM4|Auto-park rule|Topic should park when open many turns with no recent activity
TM5|Wrap (park)|Summarize current state, deactivate constraint set, preserve working data
TM6|Unwrap (resume)|Restore state, activate constraints, list pending items; conversation continues from where parked with full context
TM7|Triggered actions|on_open: activate KB tree + load constraints + restore working data; on_close: verify no pending + summarize + freeze; on_park: snapshot + deactivate; on_resume: restore + activate + list pending

# surfacing(id|mode|description|llm_involvement|data_source)
SF1|Narrative|LLM text with embedded KB references (default)|LLM generates framing|KB provides data
SF2|Table|Structured dump of KB or query result|None (direct)|KB dump
SF3|Tree|KB hierarchy showing active/inactive scopes|None (direct)|KB structure
SF4|Provenance|Complete derivation chain for specific value|Optional summary|KB derivation facts
SF5|Constraint|Active constraints with verification status|None (direct)|Constraint facts
SF6|Diff|Structured comparison between two points/scopes|Optional summary|KB comparison
SF7|Query|Prolog query results|None (direct)|Query engine
SF8|History|Binding change log|None (direct)|Binding history
SF9|Pending|Open items list|None (direct)|Topic pending lists
SF10|Context|Active scope summary|Optional summary|KB tree + topic state
# KB data blocks cannot be hallucinated — retrieved not generated
# Addressable references: live links that resolve to current value; LLM text is static, references are dynamic

# permission_model(id|role|sees_llm|sees_public|sees_internal|sees_owner_only|sees_reasoning)
PM1|Owner|Yes|Yes|Yes|Yes|Yes
PM2|Operator|Yes|Yes|Yes|No|Optional
PM3|End user|Yes|Yes|No|No|No
PM4|Auditor|Yes|Yes|Yes (read-only)|Yes (read-only)|Yes (read-only)

# accounts_as_kbs(id|aspect|detail)
AK1|Insight|User account is collection of facts (identity, preferences), rules (permissions), constraints (limits) — this is what a KB is; account should be a KB
AK2|Account KB contents|user_name, role, preferences, personal constraints, working_data (session state), children (project KBs, story KBs)
AK3|Group accounts as parent KBs|Group KB is parent; user KBs are children; group constraints apply to all members through inheritance
AK4|Nested hierarchy|org → department → team → user; each level is KB with constraints propagating downward; constraint set determined entirely by position in KB tree
AK5|Override at lower levels|Child KB declares same-name constraint with different config; merge rule handles: local overrides parent; override logged with provenance and reason
AK6|Per-user customization|Constraints from self (preferences), admin (access grants), automated systems (training requirements); all are facts in user KB with provenance
AK7|Querying hierarchy|effective_constraints(user), constraint_source(user, constraint), users_with_constraint(c), constraints_from_level(user, level)
AK8|Session state in account KB|Active topics, parked topics, working data all inside user KB; login loads KB; multi-session shares KB as single source of truth
AK9|Portable accounts|Export user KB (facts+rules+constraints+working_data); personal constraints travel; company-specific constraints stripped on detach from parent
AK10|Testable configurations|hypothetical_add(kb, new_constraint, affected); hypothetical_override(team, constraint, new_condition, conflicts) — all queryable before deployment

# data_flows(id|flow|description)
DF1|Forward pass|User input → tokenization → embedding → attention scores → softmax → value mixing → feedforward → logits → output probs → sampling; every arrow exact VDR; every step asserts provenance fact; constraints checked at normalization points
DF2|Training flow|Forward → loss (exact fraction) → backward (exact gradients) → optimizer step (exact update) → checkpoint; every step asserts provenance; weight_consistent and denominator_bound verified
DF3|Conversation flow|User speaks → topic identification → scoped KBs activated → working data available → constraints loaded → intent: KB query (direct surfacing) or generation (LLM with KB references) → new bindings asserted → topic state updated

# memory_tiers(id|tier|contents|lifetime|pruning)
MT1|Persistent|Architecture, rules, axioms, accounts, org structure|Never pruned|—
MT2|Checkpoint|Parameter snapshots at declared steps|Until explicitly deleted|Keep every Nth + anomaly steps
MT3|Step-transient|Gradients, updates, intermediate state|Until step committed|Prune unless retain_step rule matches
MT4|Batch-transient|Per-batch inference provenance|Until batch processed|Prune unless retain_batch rule matches
MT5|Conversation-transient|Per-turn working state, drafts, reasoning|Until turn complete|Prune unless flagged
# Retention policies are Prolog rules: declarative, inspectable, modifiable without code change

# new_modules(id|module|layer|purpose)
NM1|prolog.py|Logic|KB engine, unification, query, constraints, provenance
NM2|conversation.py|Logic|Topics, working data, scoping, lifecycle
NM3|surfacing.py|Logic|Direct output, addressable references, surfacing modes
# 24 existing modules + 3 new = 27 total

# implementation_roadmap(id|phase|deliverable)
IR1|Phase 1: Core Prolog|Term, Fact, Rule, KB structures; unification with exact VDR comparison; depth-first search with backtracking; scoped KB search
IR2|Phase 2: Constraints|Constraint structure; exact checking against VDR values; constraint sets with enable/disable; verification on softmax outputs and weight consistency
IR3|Phase 3: VDR-ML Integration|Instrument transformer forward pass to assert provenance facts; instrument backward pass and optimizer; verify provenance chain consistent with exact values
IR4|Phase 4: Working Data + Topics|WorkingDataSet with scoped bindings and inheritance; Topic with lifecycle; wrap/unwrap; topic switches preserve working data exactly
IR5|Phase 5: Surfacing|Direct KB data output; addressable references; surfacing modes (table, tree, provenance, constraint, diff); permission model
IR6|Phase 6: Integration Testing|End-to-end: raw text → tokenization → forward pass → provenance → constraint verification → output with KB surfacing → topic tracking → working data update

# falsification_criteria(id|criterion|test_method)
FC1|VDR computation error|Any test producing incorrect exact rational from correct inputs|Exact comparison; 705 tests have not produced one
FC2|Provenance inconsistency|Recorded derivation chain does not match recorded values under exact arithmetic|Recompute from recorded inputs, compare
FC3|Constraint false satisfaction|Constraint marked "satisfied" but exact values violate exact condition|Re-verify condition against values
FC4|Scope leak|Scoped KB query returns results from out-of-scope KB without explicit cross-scope request|Assert fact in out-of-scope KB, query from active scope
FC5|Working data corruption|Binding lost or changed during topic park/resume cycle|Snapshot before park, compare after resume

# claims(id|claim|type)
CL1|Data provenance, constraint enforcement, and conversational state are architectural requirements|design_thesis
CL2|Exact arithmetic makes provenance meaningful and constraint checking exact|structural
CL3|Scoped KBs eliminate cross-topic contamination without heuristics|structural
CL4|KB data surfacing bypasses LLM generation, preventing hallucination of retrieved facts|structural
CL5|Constraints belong inside KBs they govern for portability and consistency|design (Addendum)
CL6|User accounts as KBs unifies identity, permissions, and state in one queryable structure|design (Addendum)
CL7|The KB tree is the access control structure; no separate ACL needed|derived (Addendum)

# relationships(from|rel|to)
TL1|enables|P2 (exact provenance)
TL2|enables|PE1-PE6 (logic layer)
TL3|enables|SK1-SK5,WD1-WD7,TM1-TM7 (conversation layer)
P2|requires|TL1 (exact arithmetic)
P3|implemented_by|SK1-SK5
P4|implemented_by|SF1-SF10
P5|revises|VDR-5 original design (constraints separate)
P6|revises|VDR-5 original design (accounts separate)
PE5|uses|VDR exact fraction comparison
CS4|requires|TL1 (exact arithmetic)
CS5|implements|P5
CS6|follows_from|SK1 (KB scoping)
AK1|implements|P6
AK3|uses|CS6 (constraint inheritance)
AK4|uses|SK1 (KB scoping)
DF1|uses|TL1,TL2,TL3
DF2|uses|TL1,TL2
DF3|uses|TL2,TL3
FC1|tests|TL1
FC2|tests|TL2
FC3|tests|CS4
FC4|tests|SK1
FC5|tests|WD1,TM5,TM6
NM1|implements|TL2
NM2|implements|TL3
NM3|implements|SF1-SF10

# section_index(section|title|ids)
1|The Problem|TD1-TD3
2|VDR Exact Arithmetic Foundation|TL1
3|ML Stack (VDR-4)|from VDR-4
4|The Logic Layer: VDR-Prolog|PE1-PE6
5|Scoped Knowledge Bases|SK1-SK5,KS1-KS11
6|Working Data Sets|WD1-WD7
7|The Constraint System|CS1-CS7,CT1-CT10,CST1-CST7
8|Topic and Conversation Tracking|TM1-TM7
9|First-Class Knowledge Surfacing|SF1-SF10,PM1-PM4
10|Integration Architecture|TL1-TL3,DF1-DF3
11|Implementation Specification|PE1-PE6,KS1-KS11 (struct definitions)
12|Memory Management|MT1-MT5
13|What This Provides|CL1-CL4
14|What This Does Not Provide|scale, speed, standard transformer fidelity
15|Falsification Criteria|FC1-FC5
16|Implementation Roadmap|IR1-IR6
17|Conclusion|CL1-CL7
A1|Constraints as KB-Local (Addendum)|P5,CS5-CS7
A2|User Accounts as KBs (Addendum)|P6,AK1-AK10
D|Term Type Reference|PE1 expanded
E|Fact Predicate Reference|PE2 expanded
F|Rule Reference|PE3 expanded
G|Constraint Type Reference|CT1-CT10,CST1-CST7
H|KB Hierarchy Reference|KS1-KS11,SK5
I|Working Data Set Reference|WD1-WD7
J|Topic Lifecycle Reference|TM1-TM7
K|Surfacing Mode Reference|SF1-SF10
L|Account Hierarchy Reference|AK1-AK10
M|Memory Tier Reference|MT1-MT5
N|Query Pattern Reference|example queries for weight archaeology, lineage, constraints, conversation, accounts
O|Falsification Test Matrix|FC1-FC5 expanded with specific test inputs/expected/falsifies-if

# decode_legend
three_layers: TL1=Arithmetic(VDR) | TL2=Logic(Prolog) | TL3=Conversation(Scoped KBs+Working Data+Topics+Constraints)
term_categories: core_prolog | vdr_arithmetic | qbasis | references | provenance | conversation
constraint_domains: operational | axiom | legal | project | conversation
constraint_statuses: active | satisfied | violated | suspended | parked
topic_statuses: open | closed | parked | branched
kb_visibility: public | internal | owner_only
surfacing_modes: narrative | table | tree | provenance | constraint | diff | query | history | pending | context
memory_tiers: persistent | checkpoint | step-transient | batch-transient | conversation-transient
claim_types: design_thesis | structural | design | derived
rel_types: enables|requires|implemented_by|revises|uses|follows_from|implements|tests
module_count: 24 existing + 3 new (prolog.py, conversation.py, surfacing.py) = 27 total
cumulative_tests: 705 across VDR-1 through VDR-4; 0 VDR computation errors
