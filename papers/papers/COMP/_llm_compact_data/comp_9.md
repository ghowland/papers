# BUILDING APPLICATIONS WITH OPSDB — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → artifacts → dev_sequence → domain_analysis → schema → policies → runners → frontend → patterns → ai_methods → decisions → vocabulary → constraints → evolution

# principles(id|principle|rationale)
P1|Zero application-domain types in compiled infrastructure|All domain knowledge lives in YAML schema files and data rows interpreted by fixed mechanisms. Binary contains no domain nouns
P2|Security derives from structural limitation|Closed constraint vocabulary: 9 types, 3 modifiers, 6 constraints, 16 operations, 10 gate steps. What cannot be expressed cannot be exploited
P3|Marginal cost of new behavior approaches zero|New application behavior = new schema YAML + new data rows. No endpoint handlers, validation code, authorization logic, or audit infrastructure
P4|Data primacy|Schema is data, policies are data, business rules are data, runner configs are data. Code is fixed infrastructure or small runners. Schema is the long-lived artifact
P5|Comprehensive over aggregated|Build from the whole, subdivide preserving completeness. Domain analysis before any YAML. No information loss in decomposition
P6|Get-act-set pattern|Every runner: read from OpsDB/external (get), perform domain computation (act), write results back through API (set). Library suite handles all infrastructure

# artifacts(id|type|description|typical_size)
AR1|Schema YAML files|Declare every entity type, field, constraint, relationship, governance config. Source of truth for what data exists and what rules govern it|20-80 entity files, 2-4K lines
AR2|Runner specifications|OpsDB entities with typed JSON payloads declaring what each runner does, accesses, and bounds. Governed data — versioned, change-managed, auditable|Per runner spec entity
AR3|Runner code|Small programs following get-act-set via shared library suite. Handles one domain concern each|150-300 lines each, 3-8 runners typical
AR4|Frontend code|Thin API consumer. SSO auth, translates actions to API calls, renders responses. No database, no validation, no authorization logic|Conventional web/mobile size

# dev_sequence(id|step|action|output)
DS1|Domain analysis|Decompose domain into entities, relationships, lifecycles, policies, schedules, external integrations, hot paths|Domain map — structured inventory
DS2|Architecture position|Determine where OpsDB sits: primary backend, split backend, or operational wrapper|Position selection with hot path plan if needed
DS3|Schema design|Translate domain map into YAML files. Hours to days, not weeks|Entity YAML files
DS4|Loader run|Parse, validate, check conventions, verify FK targets, generate DDL, create tables, populate metadata|Database structure + API serving all entities with full properties
DS5|API verification|Write seed data, create entities, search, update via change sets, verify constraints reject invalid data|Confirmed schema correctness
DS6|Runner design|For each backend logic need: identify inputs, outputs, gating mode, trigger, bounds, idempotency|Runner specs as OpsDB entities
DS7|Runner implementation|Write each runner using library suite. Only domain decision logic — library handles auth, retry, circuit breaking, logging, correlation, scope|Runner code (150-300 lines each)
DS8|Frontend integration|Connect to OpsDB API. SSO, map actions to operations, render approval status, handle draft mode|Working frontend

# domain_analysis_methods(id|name|action|output)
DA1|Entity enumeration|List every noun with identity, attributes, lifecycle. Test: own identity? Attributes beyond parent reference? Independent existence?|Entity list with identity/attribute analysis
DA2|Field enumeration|For each entity, list attributes. Determine type (from 9), constraints, modifiers. Closed vocabulary constrains productively|Field list with types, constraints, modifiers
DA3|Relationship classification|Classify: direct ownership (mandatory FK), optional reference (nullable FK), many-to-many bridge, polymorphic bridge (one table per target), self-referential hierarchy|Classified relationships
DA4|Lifecycle identification|Which entities progress through states? Enumerate states and valid transitions. States → enum field, transitions → policy rows, computed rules → runner logic|State enums + transition graphs
DA5|Policy enumeration|Approval rules (from stakes not structure), access control (from data sensitivity outward), retention (regulatory first), change management|Governance requirements per entity
DA6|Schedule enumeration|Recurring operations (cron/rate/calendar), deadlines (datetime fields), event-triggered schedules|Schedule entities with typed payloads
DA7|External integration enumeration|Authorities (sources of truth), puller targets (what data to import), push targets (systems consuming config)|Authority entities + runner plans
DA8|Hot path identification|Processing that cannot tolerate gate pipeline latency? Verify through measurement not assumption. Most applications have no hot path|Hot path boundary + runner bridge plan

# types(id|type|purpose|constraints|notes)
TY1|int|Counts, quantities, priorities, ratings, sequence numbers, years, currency in minor units|min, max (always declare both)|Prefer over float for non-fractional values
TY2|float|Measurements, percentages, coordinates, rates|min, max (always declare both)|Avoid for exact financial arithmetic
TY3|varchar|Names, titles, identifiers, short descriptions, codes, slugs|length (always declare)|63 for identifiers, 255 for names, 1024 for descriptions/URLs
TY4|text|Long-form content, descriptions, notes, markdown, prose|none|Use sparingly — most strings have natural bounds
TY5|boolean|Present state (is_ prefix) or past event (was_ prefix)|none|is_active, is_published, was_approved, was_escalated
TY6|datetime|Event times, deadlines, schedule times|none|Suffix _time. Stored UTC. Timezone handling in runners
TY7|date|Due dates, birth dates, effective dates|none|Suffix _date. Use when time component meaningless
TY8|json|Typed payloads where subtypes have different field sets|validated by discriminator-selected JSON schema|Always pair with discriminator enum. Not catch-all for unstructured data
TY9|enum|Status fields, type discriminators, classifications, categories|values[] (explicit, can add never remove)|Plan initial set carefully — values are permanent
TY10|foreign_key|Ownership, membership, reference, hierarchy|references (target table)|Name as referenced_table_id or role_referenced_table_id

# constraint_mechanisms(id|type|applies_to|enforcement|evolution_rule)
CM1|Numeric range (min/max)|int, float|Gate step 4|Can widen (lower min or raise max), never narrow
CM2|String length|varchar|Gate step 4|Can widen, never narrow
CM3|Enum value set|enum|Gate step 4|Can add values, never remove
CM4|Foreign key reference|foreign_key|Gate step 4 (existence check)|Target must exist; FK permanent
CM5|Nullable|all types|Gate step 3|Can change not-null→nullable, never reverse
CM6|Unique|all except text/json|Gate step 4|Can add to empty table, cannot add with existing duplicates, cannot remove

# schema_patterns(id|name|description|when_to_use)
SP1|Standard entity|Single entity type with typed fields and constraints|Most entities — one identity, one set of attributes
SP2|Discriminator entity|Entity with subtype-specific typed JSON payload. Discriminator enum selects JSON schema for validation|Entity has variants with different field sets sharing common structure. Replaces inheritance
SP3|Many-to-many bridge|Join table with two mandatory FKs + optional relationship metadata|Many-to-many relationships
SP4|Polymorphic bridge set|One bridge table per source-target pair. Every FK is real FK to real table|One entity type attaches to several different entity types. No polymorphic FK columns
SP5|Hierarchical entity|Nullable self-FK + depth field + hierarchy runner|Tree structures: org units, categories, task/subtask
SP6|Governance scoped|_requires_group (entity visibility), _access_classification (field-level)|Per-row access control needed
SP7|Draft mode|_autoversion_disabled + _edit_latest_version + _audit_logs_disabled. Auth/validation always run. Weakens recording not security|Interactive editing where per-keystroke versioning creates noise. Never for compliance/financial data
SP8|Observation cache|versioned: false. Written by scoped runners with freshness timestamps|Imported external data, metrics, AI summaries, computed caches
SP9|Evidence record|Discriminator for evidence type + result enum + evidence_data_json|Scheduled checks producing pass/fail with supporting data
SP10|Schedule entity|Discriminator for schedule type + schedule_data_json + last/next execution|Anything recurring, expiring, or deadline-driven
SP11|Policy entity|Discriminator for policy type + policy_data_json|Approval rules, transition rules, invariants, retention, access control
SP12|Authority entity|Discriminator for authority type + authority_data_json + connection params|External system connections
SP13|Runner spec entity|Discriminator for runner type + runner_data_json with bounds, scope, trigger|Every runner in the system
SP14|Generic collection|collection_type enum + item_data_json + tags. Graduate to proper schema when friction warrants|Personal AppDB, early-stage domain exploration

# policy_types(id|type|evaluated_at|purpose)
PT1|Approval rule|Gate step 7|Which changes require human approval, from whom. Match on entity type, fields, namespace, classification, zone, proposer role
PT2|State transition|Gate step 5|Valid state machine transitions. Reject invalid, audit attempted
PT3|Semantic invariant|Gate step 5|Cross-field conditional constraints. "If status active then start_date must be set"
PT4|Retention|Reaper runner|Per-entity-type retention horizons for versions, observations, audit. Regulatory first, operational second, storage cost third
PT5|Access control|Gate step 2 layer 1|Role-to-entity-type read/write permissions
PT6|Change management|Gate step 7|Emergency review windows, segregation of duties
PT7|Security zone|Gate step 2 layer 5|Environment-level access by zone, role, time, tenure
PT8|Data classification|Gate step 2 layer 3|Sensitivity levels and field visibility grants per role

# runner_kinds(id|kind|purpose|reads|writes|gating|trigger|typical_lines)
RK1|Puller|Import external data|External API + runner spec + authority|observation_cache|Direct write|Scheduled|200-400
RK2|Reconciler|Compare desired vs observed, correct drift|Governed entities + observation_cache|change_set or entity rows|Auto-approve or approval-required|Scheduled|200-350
RK3|Verifier|Check conditions, produce evidence|Schedule + targets + prior evidence|evidence_record|Direct write|Scheduled|150-250
RK4|Notification|Detect transitions, dispatch messages|change_sets + schedules + on_call + authority|observation_cache + external channels|Direct write|Scheduled/event|200-350
RK5|Config push|Push governed state to external system|Governed entities + runner spec|External system + observation_cache|Direct write|Scheduled/on-change|200-350
RK6|Observation pull|Pull results from external system|External API + runner spec + authority|observation_cache|Direct write|Scheduled|200-300
RK7|AI observation|Generate LLM-derived summaries|Governed entities + context traversal|observation_cache (AI summaries)|Direct write|Scheduled/on-change|200-350
RK8|Custom domain|Domain-specific computation|Governed entities + domain rules|Computed results as entities or observations|Varies|Varies|150-300
RK9|Change-set executor|Apply approved change sets|Approved change_sets|Entity rows + version rows|Post-approval direct|Event-driven|150-250
RK10|Reaper|Enforce retention policies|retention_policy rows|Soft-deletes on expired rows|Direct write|Scheduled|150-200

# runner_design_questions(id|question|determines)
RD1|What does it read?|Every OpsDB entity type and external source consulted
RD2|What does it write?|Every OpsDB table and external system modified
RD3|What is the gating mode?|Direct write (observation-like), auto-approve (low-risk governed), approval-required (high-risk governed)
RD4|What triggers execution?|Scheduled (cron/rate), event-driven (state change), long-running (continuous loop)
RD5|What are the bounds?|Retry budget, execution time limit, scope per cycle, memory bounds
RD6|What does idempotency mean?|If runner runs twice on same input, what happens? Track via observation cache keys
RD7|What report keys can it write?|Declared observation cache tables and fields. API + library suite validate against declarations

# gating_modes(id|mode|change_set|approval|audit|version|use_when)
GM1|Direct write|No|No|Yes|No|Observation cache, evidence records, metrics, AI observations
GM2|Auto-approve|Yes|Auto-transitions|Yes|Yes if versioned|Low-risk governed changes, routine automated updates, personal AppDB
GM3|Approval-required|Yes|Routes to humans|Yes|Yes on apply|High-risk, financial, access control, compliance, AI-proposed governed changes
GM4|Post-approval direct|No (already approved)|Already completed|Yes|Yes|Change-set executor applying previously approved changes
GM5|Emergency|Yes (reduced)|Reduced count + mandatory flag|Yes (emergency flag)|Yes|Break-glass with mandatory post-incident review

# frontend_patterns(id|pattern|api_operation|description)
FP1|List views|search|Filters, projection, ordering, cursor pagination. Results pre-filtered by authorization. Hidden fields indicated with metadata
FP2|Detail views|get_entity|Single entity + optional join paths for related entities in one request
FP3|Activity feeds|get_entity_history|Version chain with full state, change set, proposer, approver, timestamp per version
FP4|Point-in-time|get_entity_at_time|Reconstruct state at any prior timestamp. Single row lookup, not chain replay
FP5|Standard writes|submit_change_set|Proposed field changes + reason. Old values enable optimistic concurrency
FP6|Approval-required writes|submit_change_set|Routes to pending_approval. Frontend shows pending state + approver controls
FP7|Bulk operations|bulk_submit|Multiple entity changes atomically — all succeed or all fail
FP8|Draft mode|direct write + version commit|Autosave (debounced, skips versioning/audit) + explicit commit (full governance)
FP9|Multi-tenancy|implicit|Frontend passes identity, API returns only accessible data. No tenant filters needed. Field omissions indicated

# architecture_positions(id|position|governed_ratio|hot_path|opsdb_role|effort_focus)
AP1|Primary backend|95-100%|None|Full backend|Schema design 60%, runners 30%, policy 10%
AP2|Split backend|70-90%|Bounded specific path|Governance + catalog|Hot path 40-50%, schema 20-25%, bridges 15-20%
AP3|Operational wrapper|10-30%|Dominant|Config + accounts + policies + audit|Specialized system 60-70%, schema 10%, bridges 10%
AP4|Personal|99%|None|Full backend on personal hardware|Schema 40%, runners 30%, frontend 30%
AP5|Distributed|Matches inner|Matches inner|Prototype + per-deployment instances|Release packaging + schema versioning + per-deployment policy

# ai_methods(id|method|input|output|containment)
AI1|Schema generation|Domain description + conventions|Loader-verifiable YAML. Cannot hallucinate new types (only 9) or constraints (only 6). Loader catches structural violations|Worst case: structurally valid but domain-incorrect YAML, visible and correctable
AI2|Runner generation|Runner spec + library suite API|150-300 lines of Go. Small enough for complete human review. Only domain logic — library handles infrastructure|Scope declaration limits damage even from incorrect code
AI3|Change proposer|AI runner reading governed state, proposing change sets|Change sets through standard gate pipeline. Service account with declared capabilities and targets|Same gate pipeline as humans. Approval rules match on AI identity. Audit trail records every proposal
AI4|Observation generation|Governed entities + context traversal + prompt template|Observation cache rows with freshness, model ID, source refs, prompt hash|Never governed state. Hallucination overwrites on next regeneration. Source refs enable verification

# decision_trees(id|question|yes|no)
DT1|Processing that cannot tolerate gate pipeline latency?|→DT2|→DT3
DT2|70%+ governed state?|Split backend AP2|10-70%→Wrapper AP3. <10%→OpsDB may not fit
DT3|Personal/single-user?|Personal AP4|→DT4
DT4|Intended for distribution?|Distributed AP5 with AP1|Primary backend AP1
DT5|Entity has subtypes with different field sets?|Discriminator SP2|→DT6
DT6|Polymorphic attachment to multiple entity types?|Polymorphic bridge SP4|→DT7
DT7|Parent-child hierarchy?|Hierarchical SP5|Standard entity SP1
DT8|Runner imports external data?|Puller RK1|→DT9
DT9|Compares desired vs observed?|Reconciler RK2|→DT10
DT10|Verifies conditions, produces evidence?|Verifier RK3|→DT11
DT11|Dispatches notifications?|Notification RK4|→DT12
DT12|Pushes config to external system?|Config push RK5|→DT13
DT13|Pulls results from external system?|Observation pull RK6|→DT14
DT14|LLM-derived summaries?|AI observation RK7|Custom domain RK8

# evolution_rules(id|change|allowed|conditions|risk)
SE1|Add nullable field|Yes|Must be nullable|None — existing rows unaffected
SE2|Add entity type|Yes|Naming conventions|None
SE3|Add enum value|Yes|Appended to set|None
SE4|Widen numeric range|Yes|New min ≤ old min AND new max ≥ old max|None
SE5|Widen string length|Yes|New length ≥ old length|None
SE6|Delete field|Forbidden|Never|Breaks version history, audit, consumers
SE7|Rename field/entity|Forbidden|Never|Breaks every consumer by name
SE8|Change field type|Forbidden|Use six-step duplication pattern|Breaks consumers expecting prior type
SE9|Narrow range|Forbidden|Never|Existing rows may violate
SE10|Remove enum value|Forbidden|Never|Existing rows may hold value
SE11|Add not-null field|Forbidden|Unless empty table|Breaks if existing rows lack default

# duplication_pattern(id|step|action)
DP1|Add new field alongside old|New field nullable, old unchanged
DP2|Begin writing to both fields|All writers update both
DP3|Migrate readers to new field|Readers switch from old to new
DP4|Mark old field deprecated|Document in notes
DP5|Continue writing both for safety period|Ensure all readers migrated
DP6|Stop writing to old field|Old field becomes permanent tombstone

# forbidden_patterns(id|pattern|why|alternative)
FB1|Regex in schema|Catastrophic backtracking, dialect variation|Enum sets, length bounds, anchored patterns at gate step 5
FB2|Embedded logic in schema|Non-deterministic validation|All values literals; computed values via runners
FB3|Conditional constraints in schema|Cross-field logic belongs in policy|Semantic invariant policy rows PT3
FB4|Inheritance in schema|Coupling between entity types|Independent declarations; reserved fields via opt-in
FB5|Field deletion|Breaks version history, audit, consumers|Deprecate; field remains forever
FB6|Runner invoking runner|Orchestrator coupling, cascading failure|Coordination through shared OpsDB state
FB7|Persistent state outside OpsDB|Invisible to other runners and queries|Persistent in OpsDB; in-memory for one cycle only
FB8|Side tables/channels|First step toward fragmentation; bypasses governance|Absorb into schema; API is only path
FB9|AI writing governed state directly|Bypasses human oversight|AI proposes change sets; humans approve; AI writes observations directly
FB10|Draft mode on compliance data|Creates audit gap on regulated entities|Full governance for compliance-relevant tables
FB11|Secrets in OpsDB|Not designed for need-to-know + audit-on-read|Authority pointers to vault; library accesses at runtime

# naming_conventions(id|element|convention|examples)
NC1|Entity name|Singular lowercase underscore|task, project_member, cloud_resource
NC2|Field name|Lowercase underscore|title, start_date, is_active
NC3|Foreign key|referenced_table_id|project_id, assignee_user_id
NC4|Role-disambiguated FK|role_table_id|vendor_company_id, client_company_id
NC5|Datetime|*_time suffix|created_time, approved_time, expires_time
NC6|Date|*_date suffix|due_date, birth_date, effective_date
NC7|Boolean present|is_* prefix|is_active, is_published, is_billable
NC8|Boolean past|was_* prefix|was_approved, was_escalated
NC9|Governance field|_ prefix|_requires_group, _access_classification
NC10|Bridge table|source_target singular|task_label, project_member
NC11|Discriminator enum|*_type|cloud_resource_type, monitor_type
NC12|Discriminator payload|*_data_json|cloud_data_json, monitor_data_json
NC13|Version sibling|*_version (auto-generated)|task_version, policy_version

# library_suite_categories(id|library|purpose|calls)
LS1|opsdb-api|Query and write governed/observation data|search, get_entity, get_entity_at_time, get_entity_history, submit_change_set, bulk_submit, write_observation, emergency_apply
LS2|k8s|Kubernetes resource management|list_resources, apply_manifest, watch_events
LS3|cloud-aws|AWS resource queries and changes|describe_resources, apply_change
LS4|cloud-gcp|GCP resource queries and changes|describe_resources, apply_change
LS5|secrets|Vault secret access and rotation|read_secret, rotate_secret
LS6|notification|Multi-channel dispatch|send_email, send_webhook, send_chat
LS7|logging|Structured logging and metrics|structured_log, metric
LS8|git|Repository operations|clone_repo, commit_and_push
LS9|template|Variable substitution (no logic)|render
LS10|llm|LLM API calls|generate (with retry, timeout, token budget, circuit breaking)
LS11|lifecycle|Runner thread management|heartbeat, claim_work, release_work

# effort_estimates(id|app_type|position|schema_lines|runners|backend_days|conventional_days|ratio)
EE1|Project management|AP1|2000|4|15|120|8:1
EE2|CRM|AP1|3000|5|20|180|9:1
EE3|Inventory management|AP1|2000|3|12|105|9:1
EE4|Recipe app|AP1|1000|1|4|45|11:1
EE5|E-commerce|AP2|3000|6|30+hot path|240|Varies
EE6|Chat platform|AP3|2000|4|15+specialized|210|Mostly specialized

# limitations(id|limitation|mitigation)
LM1|Closed vocabulary is real constraint — 9 types, 6 constraints, 3 modifiers|Cross-field invariants → policy rows. Complex validation → runner logic
LM2|Schema evolution additive only — cannot delete, rename, or change types|Six-step duplication pattern. Schemas accumulate deprecated fields over years
LM3|Gate pipeline adds latency on every write (10 steps)|Observation cache for high-frequency. Hot-path service for sub-millisecond
LM4|Not a compute platform|Heavy computation in specialized systems. OpsDB governs config, collects results
LM5|Discovery-phase prototyping costly under additive-only rules|Graduated formalization (generic collection → proper schema). Or prototype elsewhere, migrate when stable
LM6|Frontend is developer's responsibility|OpsDB reduces backend 8-15x. Frontend work unchanged

# relationships(from|rel|to)
P1|grounds|AR1,AR3
P2|grounds|CM1-CM6
P3|derives_from|P1,P2
P4|grounds|AR1
P5|grounds|DA1-DA8
P6|grounds|AR3,RK1-RK10
AR1|consumed_by|DS4
AR2|governs|AR3
AR3|uses|LS1-LS11
DS1|produces_input_for|DS3
DS3|consumed_by|DS4
DS4|enables|DS5
DS6|produces|AR2
DS7|produces|AR3
SP2|replaces|inheritance
SP7|weakens|versioning+audit, preserves validation+authorization
PT1|evaluated_at|gate step 7
PT2|evaluated_at|gate step 5
PT3|evaluated_at|gate step 5
GM1|provides|5/10 governance properties
GM3|provides|10/10 governance properties
AI3|constrained_by|gate pipeline + scope + approval rules
AI4|writes_only|observation cache (never governed state)
SE6|forbidden|breaks version history + audit + consumers
FB9|prevented_by|approval rules matching AI service account

# section_index(section|title|ids)
1|Development Lifecycle|DS1-DS8,AR1-AR4
2|Domain Analysis|DA1-DA8
3|Schema Construction|TY1-TY10,CM1-CM6,SP1-SP14,NC1-NC13
4|Policy Construction|PT1-PT8
5|Runner Construction|RK1-RK10,RD1-RD7,GM1-GM5,P6
6|Frontend Integration|FP1-FP9
7|Application Patterns|AP1-AP5
8|AI-Assisted Construction|AI1-AI4
9|Construction Catalog|47 methods total
10|Decision Trees|DT1-DT14
11|Taxonomy Cross-Reference|—
12|Boundaries and Limitations|LM1-LM6
13|Summary|P1-P6

# decode_legend
gate_steps: 1=auth|2=authz(5 layers)|3=schema validation|4=bound validation|5=policy evaluation|6=versioning|7=change management|8=audit|9=execution|10=response
types: int|float|varchar|text|boolean|datetime|date|json|enum|foreign_key (9 base + FK)
constraints: numeric range|string length|enum values|FK reference|nullable|unique
modifiers: nullable|default|unique
architecture_positions: AP1=primary backend|AP2=split backend|AP3=operational wrapper|AP4=personal|AP5=distributed
gating_modes: direct write (5/10 properties)|auto-approve (8/10)|approval-required (10/10)|post-approval|emergency
runner_pattern: get (read) → act (domain logic) → set (write back)
evolution: additive only. Add nullable fields, add entities, add enum values, widen ranges/lengths. Never delete, rename, change type, narrow, remove
id_prefixes: P=principle|AR=artifact|DS=dev_sequence|DA=domain_analysis|TY=type|CM=constraint|SP=schema_pattern|PT=policy_type|RK=runner_kind|RD=runner_design_question|GM=gating_mode|FP=frontend_pattern|AP=architecture_position|AI=ai_method|DT=decision_tree|SE=evolution_rule|DP=duplication_step|FB=forbidden_pattern|NC=naming_convention|LS=library_suite|EE=effort_estimate|LM=limitation
spec_counts: 47 construction methods|9 domain analysis|9 schema construction|5 policy construction|10 runner construction|5 frontend integration|5 application patterns|4 AI methods|14 runner kinds|5 gating modes|13 evolution rules|11 forbidden patterns|13 naming conventions|11 library categories
