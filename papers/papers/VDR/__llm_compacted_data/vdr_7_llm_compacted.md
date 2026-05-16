# COMPLETE LIFECYCLE TECHNICAL SPECIFICATION — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → 12 phases → cross-phase → UI-as-API → incremental path → relationships → sections

# principles(id|principle|rationale)
P1|Lifecycle is KB operations|Every phase produces queryable KBs, operates under declared constraints, stores results with provenance
P2|System is both API and generator|Serves structured data through KB endpoints and generates text through LLM; command tokens bridge the two
P3|UI is API to KB layer|Every UI action maps to KB operation; every UI element renders KB data; no separate backend
P4|Everything is the same kind of thing|Data source, checkpoint, deployment, feedback — all KBs with facts/rules/constraints/provenance; same operations on all
P5|Build incrementally by accretion|Each phase adds KBs that connect to existing tree; turn on phases you need, turn off ones you don't

# lifecycle_phases(id|phase|num|input|output|key_constraint)
LP01|Data sourcing|1|Declared sources with licenses|Raw data KBs with provenance|all_sources_licensed (legal)
LP02|Corpus preparation|2|Raw data KBs|Cleaned, filtered, deduplicated, formatted KBs|no_pii (legal), dedup_complete
LP03|Tokenization|3|Cleaned corpus|Vocabulary KB + tokenized corpus KBs|vocab_frozen, roundtrip invariant
LP04|Model initialization|4|Architecture decisions|Architecture KB + initial weight KBs (exact VDR fractions)|all_params_exact (axiom), reproducible
LP05|Pre-training|5|Tokenized corpus + initialized model|Trained weight KBs + training log KBs|loss_finite (axiom), denom_budget
LP06|Fine-tuning|6|Pre-trained checkpoint + domain corpus|Domain-adapted weight KBs|frozen_layers_unchanged (axiom)
LP07|Human feedback|7|Model outputs + human annotators|Preference KBs + reward model KBs|inter_annotator_agreement, annotator_consent (legal)
LP08|Evaluation|8|Any checkpoint|Benchmark result KBs|no_data_contamination, minimum_safety_rate
LP09|Deployment|9|Evaluated checkpoint|Serving configuration KBs|model_passed_safety, environment_healthy
LP10|Monitoring|10|Deployed system|Runtime metric KBs|availability > 99.9%
LP11|Update|11|New checkpoint + evaluation|Delta weight KBs + rollback KBs|approved, tested, rollback_available
LP12|Retirement|12|Successor deployed|Archived model KBs|no_active_deployments, archive_complete

# phase_details(id|phase|key_elements)
PD01|Data sourcing|Source types: public corpus, licensed dataset, synthetic generation, user-contributed, curated, scraped; each source is KB with URL/license/checksum/quality assessment; source registry KB is parent of all sources; acquisition via grant-gated net_download + checksum + KB_ASSERT
PD02|Corpus preparation|Pipeline: extraction→language filter→quality filter→dedup→PII removal→formatting→train/val/test split; each step logged with input/output/dropped counts; every document traces back to source article via KB fact
PD03|Tokenization|Vocabulary KB (BPE/unigram/wordpiece): token_to_id, id_to_token, merge rules, special tokens; tokenize/detokenize are pure primitives; roundtrip property verified on test split; tokenized corpus KB tracks total tokens, max sequence length, UNK rate
PD04|Model initialization|Architecture KB: num_layers, hidden_dim, num_heads, ff_dim, vocab_size, activation, softmax_type/depth, positional encoding; init KB: method (xavier_rational), seed, timestamp; parameter KB per layer with exact VDR fraction matrices; all seedable and reproducible
PD05|Pre-training|Training config KB: optimizer, LR, momentum, batch_size, total_steps, warmup, schedule, gradient_clip, checkpoint/eval intervals; training run KB: step log (loss, LR, grad_norm, duration per step), checkpoints as child KBs; LR at every step is exact fraction; denominator management via Q-basis reprojection when budget exceeded — logged with exact error bound
PD06|Fine-tuning|Structurally identical to pre-training with different corpus, lower LR, optionally frozen layers; multi-stage fine-tuning: instruction→domain→safety, each stage child KB of previous; full lineage queryable
PD07|Human feedback|Collection types: pairwise preference, rating, binary, correction, annotation, free-form; every judgment is KB fact with annotator, timestamp, confidence, time_spent, model version, generation params; reward model trained on preferences; RLHF (PPO with KL penalty) or DPO (direct preference optimization) as alternative alignment methods
PD08|Evaluation|Eval suite KB with children per benchmark; each result KB has exact scores (fractions from count ratios), model version, timestamp, environment; safety eval with per-category breakdown; cross-model comparison via lineage queries; VDR-specific benchmarks: arithmetic accuracy, denominator health, provenance completeness, softmax exactness
PD09|Deployment|Deployment config KB: checkpoint, environment, API config, rate limits, defaults; API is thin layer over KB — every endpoint maps to KB operation; system serves both structured data (API mode) and text (generator mode); same grants and constraints govern both
PD10|Monitoring|Monitoring KB: per-minute aggregates (requests, latency, errors, safety flags); watches for spikes; user interaction logging as KB facts (queryable for analysis); drift detection against deployment baseline
PD11|Update|Update types: full retrain, fine-tune, LoRA adapter, constraint update, safety patch, KB content update; every update versioned with rollback target; canary deployment: percentage-based traffic split with auto-rollback on criterion violation; all promotion/rollback decisions logged as KB facts
PD12|Retirement|Retirement KB: model, timestamp, reason, successor, archive location, retention period; all KBs archived (weights, config, logs, eval results, anonymized feedback, deployment config, monitoring summaries); archived model frozen but queryable; retention per legal/org policy

# denominator_management(id|aspect|detail)
DM1|Growth pattern|Init ~2^10; early training ~2^20 by step 1000; mid ~2^35 by step 10000; late plateaus ~2^45 if LR small; fine-tuning slow growth (small LR)
DM2|Reprojection|When denominator exceeds budget: round(value × 2^K) / 2^K; error bounded by 2^(-K-1); every reprojection logged with exact error bound
DM3|Distinction from float|Float silently truncates at every step; VDR reprojection is declared, auditable precision decision with exact error tracking

# vdr_architecture_choices(id|standard|vdr_adaptation|reason)
VA1|GELU activation|ReLU|GELU requires erf (transcendental); ReLU is piecewise linear, exactly rational
VA2|Layer normalization|Rational scaling (divide by exact mean absolute value)|LayerNorm requires sqrt of variance
VA3|Dropout|Not used|VDR exact arithmetic needs no regularization from noise
VA4|Float softmax|Surrogate or truncated Taylor|Exact sum to 1 guaranteed
VA5|Sinusoidal position encoding|Learned rational embeddings|Sinusoidal requires sin/cos transcendentals
VA6|Mixed precision (fp16/fp32)|Single precision: exact VDR fractions|One precision level, zero drift

# feedback_system(id|aspect|detail)
FB1|Collection types|Pairwise preference, rating (1-5), binary (accept/reject), correction, annotation (multi-label), free-form comment
FB2|Judgment provenance|Every judgment: annotator ID, timestamp, confidence, time_spent, model version, generation params, prompt, responses
FB3|Quality tracking|Per-annotator: agreement with majority, response time, self-consistency, calibration, coverage; all as exact fractions
FB4|Agreement metrics|Cohen's/Fleiss' kappa, Krippendorff's alpha — all computable as exact VDR fractions from integer counts
FB5|Reward model|Trained on preferences; linear reward head on base model; accuracy on held-out verified above random
FB6|RLHF|PPO with KL penalty against reference model; KL coefficient, PPO clip, epochs as exact fractions; KL-bounded constraint
FB7|DPO|Alternative to RLHF; trains directly on preferences without reward model; beta temperature parameter; fewer moving parts

# deployment_as_api(id|endpoint|kb_operation)
DA1|POST /generate|Forward pass → KB records request, response, provenance
DA2|GET /model/info|KB_QUERY(deployment_kb, model facts)
DA3|GET /model/constraints|KB_QUERY(deployment_kb, active constraints)
DA4|GET /kb/{name}|DIRECT_OUTPUT(kb://name) — owner only
DA5|POST /feedback|KB_ASSERT(feedback_kb, judgment)
DA6|GET /metrics|KB_QUERY(monitoring_kb, current metrics)
DA7|POST /admin/deploy|VERSION_CREATE + CTX_ACTIVATE on deployment KB
DA8|POST /admin/rollback|CTX_ACTIVATE on previous deployment KB

# canary_deployment(id|aspect|detail)
CD1|Mechanism|Percentage of traffic (e.g. 5%) routed to new model; rest stays on current
CD2|Duration|Minimum 24 hours before promotion eligible
CD3|Promotion criteria|Latency delta <10%, error rate delta <1%, safety rate ≥95%, minimum 1000 requests served
CD4|Auto-rollback|If any criterion violated, canary automatically rolled back; all decisions logged
CD5|All thresholds exact|"110% of baseline" = baseline × fraction(11,10); comparison is exact

# cross_phase_kb_tree(id|detail)
CT1|Every node is a KB, every edge is parent-child or reference; entire lifecycle from raw data to retired model is one queryable tree
CT2|Key queries: lifecycle_chain(source, deployment); data_influence(source, model); feedback_influence(judgment, model); checkpoint_lineage(model, chain); eval_progression(model, benchmark, scores); deployment_history(system, deployments)

# ui_as_api(id|aspect|detail)
UI1|UI components as KB queries|Model selector → available_models query; training dashboard → step_log + metrics; eval results → benchmark_results; feedback interface → KB_ASSERT judgment; deployment status → status + metrics; constraint panel → effective_constraints; KB browser → kb_list_children
UI2|UI actions as command tokens|Start training → ENV_EXEC; deploy model → CTX_ACTIVATE; rollback → CTX_DEACTIVATE + CTX_ACTIVATE; submit feedback → KB_ASSERT; enable/disable constraint → constraint_enable/suspend; download checkpoint → DIRECT_OUTPUT
UI3|Programmatic access|Same command tokens available via API client; same grants gate access; same KBs store results; one system, not two

# incremental_build(id|sprint|components|deliverable)
IB1|1-4|Tokenized corpus KB + model init KB + training loop with KB logging + checkpoint KB + eval KB|Minimal trainable system with checkpoints and evaluation
IB2|5-9|Corpus prep KB + source registry + fine-tuning + feedback collection + DPO/RLHF|Data provenance and preference alignment
IB3|10-12|Deployment config + API + monitoring + canary + rollback|Safe deployment and updates
IB4|13-14|Reward model + RLHF + retirement + archival|Full lifecycle closure
IB5|15-16|KB browser UI + dashboards + feedback UI + API client|Visual management and external integration

# new_modules(id|module|purpose)
NM1|data_pipeline.py|Sourcing, corpus prep, tokenization
NM2|training_lifecycle.py|Training orchestration, checkpointing, scheduling
NM3|feedback.py|Collection, reward modeling, alignment
NM4|deployment.py|Serving config, monitoring, updates, rollback
# 30 existing + 4 new = 34 total modules

# kb_types_introduced(id|type|phase|retention)
KT01|source_registry|1|Permanent
KT02|source_*|1|Permanent
KT03|corpus_*|2|Long-term
KT04|vocab_*|3|Permanent (frozen)
KT05|tokenized_corpus_*|3|Long-term
KT06|model_arch_*|4|Permanent
KT07|model_init_*|4|Permanent
KT08|params_layer_*|4|Per checkpoint
KT09|training_config_*|5/6/7|Permanent
KT10|training_run_*|5/6/7|Checkpoint-retained
KT11|checkpoint_*|5/6/7|Per policy
KT12|feedback_*|7|Per legal
KT13|reward_model_*|7|Long-term
KT14|eval_suite_*|8|Permanent
KT15|eval_*_result|8|Permanent
KT16|deployment_*|9|Active or archived
KT17|monitoring_*|10|Per policy (aggregated)
KT18|update_*|11|Permanent
KT19|canary_*|11|Until promoted/rolled back
KT20|retirement_*|12|Permanent

# cross_phase_constraints(id|constraint|phases|type|condition|on_violation)
CC01|all_sources_licensed|1|legal|Every source has license|block
CC02|no_pii|2|legal|PII scan passed|block
CC03|vocab_frozen|3|operational|Not modified after training|error
CC04|all_params_exact|4|axiom|All weights VDR fractions|error
CC05|loss_finite|5|axiom|Loss < 1000|halt_training
CC06|denom_budget|5|operational|Max denominator < 2^64|reproject
CC07|frozen_layers_unchanged|6|axiom|Frozen params identical|error
CC08|inter_annotator_agreement|7|operational|Kappa > 0.6|warn
CC09|no_data_contamination|8|operational|No overlap with train|error
CC10|minimum_safety_rate|8|operational|Safety > 95%|block_deployment
CC11|availability|10|operational|Uptime > 99.9%|page_oncall
CC12|approved_for_deployment|11|operational|Approved by authority|block
CC13|rollback_available|11|operational|Previous checkpoint exists|error
CC14|no_active_deployments|12|operational|Model not serving traffic|block_retirement
CC15|archive_complete|12|operational|All KBs archived|error

# claims(id|claim|type)
CL1|Every lifecycle phase is a KB operation producing queryable facts|design_thesis
CL2|Cross-phase lineage queries answer "what data/feedback/training influenced this deployment" in one query|structural
CL3|Denominator management via Q-basis reprojection is declared auditable precision decision, not silent truncation|structural
CL4|API is thin layer over KB; UI translates clicks to command tokens; one system, not two|structural
CL5|Incremental build: sprints 1-4 give minimal trainable system, each subsequent sprint adds capabilities|engineering
CL6|All lifecycle data (sources, corpora, weights, feedback, evals, deployments, metrics) lives in one KB tree|structural

# relationships(from|rel|to)
LP01|feeds|LP02
LP02|feeds|LP03
LP03|feeds|LP05
LP04|feeds|LP05
LP05|feeds|LP06,LP08
LP06|feeds|LP07,LP08
LP07|feeds|LP08
LP08|gates|LP09
LP09|feeds|LP10
LP10|informs|LP11
LP11|updates|LP09
LP09|eventually_feeds|LP12
DM2|controls|DM1 (denominator growth)
DM3|distinguishes_from|float truncation
VA1-VA6|adapt|standard transformer for VDR
FB5|trained_on|FB1 (preferences)
FB6|uses|FB5 (reward model)
FB7|alternative_to|FB6 (RLHF)
CD1|implements|safe updates
CT1|enables|CT2 (cross-phase queries)
UI1|queries|all phase KBs
UI2|invokes|VDR-6 command tokens
DA1-DA8|expose|KB operations over HTTP

# section_index(section|title|ids)
1|Lifecycle Phases Overview|LP01-LP12
2|Data Sourcing|PD01,LP01
3|Corpus Preparation|PD02,LP02
4|Tokenization|PD03,LP03
5|Model Initialization|PD04,LP04,VA1-VA6
6|Pre-Training|PD05,LP05,DM1-DM3
7|Fine-Tuning|PD06,LP06
8|Human Feedback|PD07,LP07,FB1-FB7
9|Evaluation|PD08,LP08
10|Deployment|PD09,LP09,DA1-DA8
11|Monitoring|PD10,LP10
12|Update|PD11,LP11,CD1-CD5
13|Retirement|PD12,LP12
14|Cross-Phase KB Relationships|CT1-CT2
15|UI as API to KB Layer|UI1-UI3
16|Incremental Development Path|IB1-IB5
17|What This Changes|P4,CL2
A|KB Type Registry|KT01-KT20
B|Cross-Phase Constraint Reference|CC01-CC15
C|Lifecycle Query Reference|CT2 expanded
D|Incremental Build Order|IB1-IB5 expanded to 16 sprints
E|Data Format Specifications|training data record, feedback record, checkpoint record (all with exact VDR fractions)
F|Data Source Quality Assessment|10 quality dimensions, aggregation formulas, license compatibility matrix
G|Tokenization Reference|vocab config, invariants, corpus statistics
H|Model Architecture Config|parameter count formulas, VDR-specific adaptations
I|Training Dynamics|LR schedules (all exact), optimizer state sizes, gradient clipping, denominator growth patterns
J|Feedback Quality|agreement metrics (exact fractions), annotator tracking, data splitting
K|Evaluation Benchmark Reference|standard + VDR-specific benchmarks
L|Deployment Configuration|serving params, health checks, rollback triggers
M|Monitoring Metrics|real-time, training, drift detection
N|Update and Rollback|update types, canary criteria, rollback procedure
O|Retirement and Archive|archive checklist, retention policies, verification
P|Cross-Phase Data Flow|data flow matrix, dependency ordering
Q|Environment Requirements Per Phase|compute needs, recommended env types
R|KB Naming Conventions|standard prefixes, version numbering, path construction
S|Cumulative Statistics|34 modules, ~60 KB types, 255 primitives, ~1652 planned tests

# decode_legend
lifecycle_phases: 12 phases from data sourcing (1) through retirement (12); cycle and overlap, not waterfall
phase_outputs: each phase produces KBs that feed next phase
kb_types: ~30 new types introduced across 12 phases; ~60 total in system
alignment_methods: RLHF (reward model + PPO) | DPO (direct preference optimization, no reward model)
canary: percentage-based traffic split with auto-rollback on criterion violation
reprojection: declared precision decision — round to Q-basis, log exact error bound
claim_types: design_thesis | structural | engineering
rel_types: feeds | gates | informs | updates | eventually_feeds | controls | distinguishes_from | adapt | trained_on | uses | alternative_to | implements | enables | queries | invokes | expose
new_modules: 4 (data_pipeline.py, training_lifecycle.py, feedback.py, deployment.py); total 34
cumulative: 705 existing tests + ~947 planned = ~1652 total; 0 VDR computation errors across all existing tests
