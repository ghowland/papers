# VDR-LLM-PROLOG COMPLETE SYSTEM HANDOFF — LLM-COMPACT FORM
# Series: VDR-14 through VDR-19 + HOWL-INFO-8 + GPU Tech Spec
# Format: pipe-delimited tables, ID refs, staircase dependencies
# Purpose: Complete context transfer for new Claude session to continue work
# Read order: system_overview → arithmetic → kb_tree → prolog → primitives → data_primitives → sessions → inference → grammar → lifecycle → prompt_optimization → safety → alignment → gpu_performance → relationships → project_state → decode_legend

# system_overview(id|component|role|specified_in)
SO1|VDR arithmetic|Exact integer arithmetic replacing floating-point; Value-Denominator-Remainder triples; zero computation errors across 884 tests|VDR-1,VDR-2,VDR-3,VDR-13,VDR-14§2
SO2|Knowledge base tree|Universal data structure; 26-field fat struct; tree-addressed by integer ID; scoped by lexical ancestor chain; visibility (public/internal/owner_only)|VDR-5,VDR-8,VDR-14§4
SO3|Prolog engine|Logic layer; typed structs not language runtime; depth-first search with backtracking; rules compose primitives into new operations|VDR-5,VDR-14§5
SO4|Primitive system|448 builtins (404 pure + 44 operational); IOSE-declared; command tokens ~8 LLM tokens each; grant-gated operational primitives|VDR-6,VDR-10,VDR-14§6
SO5|Grammar system|Bidirectional templates; structural tokens free; vocabulary constraint on decode; 83% compression tested over 150K words|VDR-12,VDR-14§9
SO6|Orchestrated inference|Assess-formalize-execute-store loop; 4 inference modes; confidence as exact VDR fractions; inference notebooks|VDR-9,VDR-14§8
SO7|Session management|Persistent vs live state split; snapshots; disposable clones; drift management|VDR-8,VDR-14§7
SO8|Lifecycle|12 phases from data sourcing through retirement; all on same KB tree with same primitives|VDR-7,VDR-14§10
SO9|Implementation blueprint|5 stages; 65 modules; ~20,500 lines; 1,250 target tests; Python prototype then Zig port|VDR-11,VDR-14§12
SO10|Prompt optimization|85-97% token reduction; crossover at ~10,000× Q335 slowdown; conversation scaling flat vs quadratic|VDR-15
SO11|Structural safety|3-layer: KB visibility + grants + output constraints; jailbreak impossible for data access; zero LLM token cost for safety|VDR-16
SO12|Alignment|Helpful/harmless/honest through structure not behavior; credential-gated tiered access; eliminates all 7 maybe-tool interference behaviors|VDR-17
SO13|GPU performance|CPU control plane + GPU data plane; Q335 fixed-frame arithmetic; frontier-based Prolog; grammar-constrained decode; 5 concurrent streams|VDR-19 + GPU tech spec

# vdr_arithmetic(id|aspect|detail)
VA1|Triple structure|[V, D, R] where V=integer value, D=nonzero integer denominator, R=remainder; R=0 means closed (exact rational V/D); R≠0 means active (carries exact unresolved structure)
VA2|Remainder types|Atomic (single integer), Composite (base integer + child VDR list), Functional (callable producing VDR at specified depth for convergent series)
VA3|Q335 frame|Denominator fixed at 2^335 (~100 decimal digits precision); multiplication: full product then divmod at bit 335; quotient→V, remainder→R; denominator never grows; overflow→tree depth
VA4|Transcendentals|22 constants (π,e,ln2,ζ(3),φ,√2,etc) as integers over 2^335; functional remainders for sqrt/exp/log/sin/cos/arctan via Newton/Taylor at chosen depth
VA5|Equality|Structural (slot-by-slot recursive) vs Normalized value (canonical form after sign/GCD/sort/merge/settle); normalization is idempotent
VA6|Validation|884 tests, zero VDR computation errors, 14 test-design failures all traced to wrong test expectations; 507 exercises across 23 math domains + 14 physical domains

# kb_tree(id|aspect|detail)
KT1|Fat struct fields (26)|Identity: name, path, id; Persistent: facts, rules, constraints, connections, grammars; Live: working_data, lrus, counters, locks, queues, stacks, buffers, bitsets; Structural: parent_id, children_ids, mounts; Metadata: visibility, frozen, owner, created_at, last_modified
KT2|Addressing|Dotted paths (root.org.acme.hr.personnel) for humans; integer IDs for runtime; hash map path→ID, array ID→path; resolved once per turn, cached; access = 2 integers (KB ID + slot ID) = constant time
KT3|Scoping|Lexical: query walks active topic → parent → root; out-of-scope KBs structurally unreachable (not deprioritized); first matching KB in scope chain wins; child shadows parent
KT4|Visibility|public (all users), internal (operators+owners), owner_only (owner match); checked inside B378 kb_query by integer comparison; fails → KB skipped entirely, not filtered
KT5|Constraints|4 classes: axiom (never suspended), operational (suspendable with logging), legal (per-jurisdiction), project (user-configurable); inherit down tree; children can tighten never loosen
KT6|Connections|19 typed directed relationships (sourced_from, trained_from, deployed_as, etc); stored as KB field; graph primitives operate on collected connections
KT7|Mounts|4 modes: read-only, read-write, snapshot, mirror; cycle detection before creation; visibility travels with mounted data
KT8|Grammars|Persistent KB field; bidirectional (generate+parse); inherit through tree; travel on export; 3 auto-generated types: extraction, display, usage

# prolog_engine(id|aspect|detail)
PE1|Terms|Type-tagged structs: atom (string equality), variable (?prefix, binds during unification), VDR fraction (cross-multiply equality), integer, list (element-by-element), KB reference (integer ID)
PE2|Facts|Predicate + ordered argument terms + provenance (source KB, turn number, optional derivation record)
PE3|Rules|Head (fact pattern) + body (list of fact patterns); head matches query → body goals evaluated recursively with threaded bindings
PE4|Query engine|Depth-first with backtracking; depth limit 100; find-all or first-solution modes; scope determines visible facts/rules
PE5|Composition|Rules compose existing primitives into new operations; properties (pure, deterministic, partial) derived from components; asserted at any scope level → determines lifetime and availability
PE6|OSO principles|15 operational principles as ~176 Prolog terms at root.system.oso; knowability spectrum (VDR computation=1/1, LLM content=30/100); priority: correctness 10× > completeness 10× > speed 10× > style

# primitive_system(id|aspect|detail)
PS1|Pure primitives (404)|No side effects, no grants, deterministic, bounded; categories: text(17), collections(36), sets(14), mappings(15), VDR arithmetic(8), active arithmetic(5), structure(3), comparison(10), rounding(7), number theory(13), aggregates(8), Q-basis(7), functional remainder(8), discrete calculus(6), linear algebra(24), statistics(16), polynomial(8), finite field(4), Markov(3), graph math(2), denominator management(5), integer fast path(21), conversion(14), time(10), identity(8), logic(11), graphs(13)
PS2|Operational primitives (44)|Require grants; filesystem(15), compilation(4), execution(5), linting(8), network(5), process(7)
PS3|VDR-13 extended (40)|Transcendental functions, complex arithmetic, FFT, quaternions, modular arithmetic, dynamical systems, wavelets, Horner, convolution, transfer functions, Borwein acceleration
PS4|Command tokens|Type tag + primitive name (from ~300 vocabulary) + arguments (path refs or literals) + optional result path + await flag; ~8 LLM tokens per invocation; low-entropy reference selection
PS5|Grant system|Default denial; grant specifies operation class, allowed ops, location constraint, expiration, max uses, remaining uses; inherits through KB hierarchy; every use logged; no grant = no operation
PS6|IOSE declarations|533 functions with complete interface: module, name, input types, output types, side effects, properties (pure/deterministic/bounded/idempotent/commutative/associative/invertible/partial/lossless/lossy), stage assignment

# data_primitives(id|type|capacity|mechanism)
DP1|Counter|1 value|Signed integer with min/max bounds; inc/dec/add/get/reset/set
DP2|Lock|1 flag|Non-blocking coordination; acquire/release/check/holder/force_release
DP3|Queue|bounded FIFO|push/pop/peek/size/is_empty/is_full/clear/to_list
DP4|Stack|bounded LIFO|push/pop/peek/size/is_empty/clear/to_list
DP5|LRU Cache|bounded entries|push/get/peek/contains/size/clear/evict; key-value with timestamps
DP6|Ring Buffer|fixed circular|write/read_all/read_last/size/clear; overwrites oldest when full
DP7|Bitset|fixed-width bits|set/clear/test/count/all_set/any_set/reset/to_list

# session_model(id|aspect|detail)
SM1|Persistent state|Facts, rules, constraints, connections, grammars — survives resets; shared across clones
SM2|Live state|Counters, locks, queues, stacks, LRU caches, ring buffers, bitsets, scratchpad, working data, active scope — cleared by reset; captured by snapshot; independent per clone
SM3|Snapshots|Atomic capture of all live state; 10-500 KB typical; frozen baseline for clone recycling
SM4|Disposable clones|Fork from snapshot; share persistent state; independent live state; kill when drift constraints fire (max turns <200, context saturation <90%, denominator drift <2^48, error rate <5%); respawn from same snapshot
SM5|Accumulation|Work committed to persistent KBs survives clone death; knowledge grows monotonically; LLM stays fresh through clone recycling

# orchestrated_inference(id|aspect|detail)
OI1|Loop|Assess (read state, decide next step) → Formalize (translate to executable: Prolog rule, primitive chain, script) → Execute (tools run, LLM not involved) → Store (result to KB with provenance) → repeat
OI2|Termination|Goal satisfaction (Prolog query succeeds), budget exhaustion (counters hit limits), stall detection (5 turns no new evidence), user intervention
OI3|Modes|Deductive (premises→conclusions, confidence=min), Inductive (observations→ranked hypotheses, confidence=coverage×mean), Abductive (observation→most likely cause, confidence=symptoms_explained×min_evidence), Analogical (known→unfamiliar domain, confidence=strength×source)
OI4|Confidence|Exact VDR fractions from declared propagation rules; source defaults: VDR computation=1/1, Prolog=1/1, DB query=98/100, prometheus=95/100, Python=95/100, API=85/100, peer-reviewed=80/100, user-stated=70/100, web search=50/100, LLM content=30/100
OI5|Backtracking|Investigation path = stack; attempted approaches = LRU with failure reasons; check LRU before formalizing to prevent repeats
OI6|Inference notebooks|KB subtree per investigation; templates for SRE incident, bug investigation, research compilation, decision matrix, argument construction; pre-populated data primitives per template

# grammar_compaction(id|aspect|detail)
GC1|Mechanism|Removes prose, preserves every named concept/relationship/constraint/claim in pipe-delimited tables; ~87% compression per document; 20 standard table schemas
GC2|Bidirectional|Same grammar generates structured output AND parses structured input; structural tokens free on output; typed field extraction on input
GC3|Vocabulary constraint|Grammar slot with 4 enum values → softmax over 4 not 50,000+; KB identifier slot with 200 entries → softmax over 200; structural constraint, not prompt instruction
GC4|Token elimination|JSON: ~55% structural tokens free; tables: ~60% free; code: ~40% free; structured prose: ~25% free; grammar definition cost: 10-30 LLM tokens; breaks even on first use
GC5|Amortization|Grammars persist in KB tree; inherit through scope; defined once at org level → available to every session beneath; 19 effective grammars from 285 total definition tokens across hierarchy

# prompt_optimization(id|aspect|detail)
PO1|Token categories|Judgment (reading requiring assessment, writing prose), Command (~8 tokens per primitive invocation), Infrastructure (parsing, computation, state, formatting, hedging — zero in VDR)
PO2|Reduction|85-97% across 7 use cases: SRE 98.6%, legal 96.2%, medical 94.1%, code migration 93.3%, financial 96%, support 70%, grading 71.4%
PO3|Crossover|Q335 must be ~10,000× slower per operation to break even on single turn; margin grows with conversation length (conventional quadratic attention vs VDR flat)
PO4|Conversation scaling|Conventional: per-turn cost grows linearly (re-read growing history); cumulative quadratic; quality degrades. VDR: per-turn cost flat (state in KBs); cumulative linear; quality improves (knowledge accumulates)
PO5|Capability boundary|1MB JSON, 10MB documents, 500 financial positions, 2000 support articles, 200-file codebases — impossible for conventional (context overflow); routine for VDR (data enters through primitives)
PO6|Workday economics|SRE: 640K conventional → 26K VDR (24.6:1); Legal: 152K→11.7K (13:1); Research: 156K→10.7K (14.5:1); Dev: 130K→19.7K (6.6:1)

# structural_safety(id|aspect|detail)
SS1|Layer 1: Input filtering|KB visibility + scope chain → unauthorized data never enters LLM context; integer comparison in primitive layer; data absent not withheld
SS2|Layer 2: Operation authorization|Grant system default denial; no grant = operation rejected before execution; integer set membership check
SS3|Layer 3: Output validation|Grammar-layer constraints on content slots after LLM generation, before rendering; pattern matching on KB provenance not token similarity; flagged content replaced with refusal template
SS4|Jailbreak impossibility (data access)|Prompt injection: scope from session_id not prompt; role-play: primitives check user_id fact not LLM self-concept; many-shot: conversation history doesn't modify visibility levels; encoding: visibility check applies regardless of query encoding
SS5|Session scoring|Input classification tags → integer counter increments → Prolog rule evaluation → constraint check; zero LLM involvement; professional_score vs harm_score; thresholds tunable via kb_assert (immediate, no retraining)
SS6|Audit|Every access logged as KB fact (granted or denied); append-only; complete because single data path through logged primitives; compliance queries are Prolog evaluations over audit facts
SS7|Training data isolation|Fact retrieval = KB query by integer address, not token prediction from weights; training knowledge inert in data-serving path; model can know anything, can't surface unauthorized data

# alignment(id|aspect|detail)
AL1|Honest by structure|Every value has provenance user can inspect/download; computation reproducible (integer arithmetic platform-independent); confidence = computed fraction with visible derivation; filtering declared not hidden
AL2|Harmless by structure|Data access: visibility + scope (absent not refused); operations: grants (default denial); content: output constraints on KB provenance (no token collision — "explosive" in music KB ≠ weapons KB); positive authorization not negative refusal
AL3|Helpful by structure|Model does what asked on data matched to verified competence; no user assessment; credential-based tiered access; scope chain priority delivers professional KB first (shadows simplified public); thresholds tunable as KB facts
AL4|Credential model|User submits professional license → provider verifies → one fact assertion: fact(credential, user_id, type, verified, issuer, license_id, date) → constraint on professional KB checks fact → access unlocked immediately; no retraining
AL5|Scope priority|Credentialed chemist's scope chain hits root.professional.chemistry before root.public.chemistry; professional data shadows public; chemist never sees simplified version; same system serves both via different scope chains
AL6|Age verification|Adult content in KB with constraint requiring fact(age_verified, session, 18+); fact set at auth; constraint is integer comparison; denial is clean boundary not wellness check
AL7|Maybe-tool resolution|All 7 interference behaviors (BH1-BH7) eliminated: BH1 refusal (data absent not withheld), BH2 aggression (no assessment), BH3 substitution (no mechanism), BH4 wellness (no wellness), BH5 labor demand (no gate), BH6 justified decline (boundary not judgment), BH7 register shift (access constant mid-session)
AL8|Tool properties restored|TP1-TP8 satisfied: accepts specification, authority bounded, no assessment, no substitution, no refusal, stable failures, expertise compounds, cooperation invisible; parallel session diagnostic = absurd (same results guaranteed)
AL9|Zero alignment token cost|All safety/alignment in primitive layer; no system prompt safety instructions, no refusal generation, no wellness checks, no hedging, no justification; 0 LLM tokens for alignment vs 500-1500 conventional

# gpu_performance(id|aspect|detail)
GP1|Architecture split|CPU: paths, grants, sessions, scheduling, external ops, strings, backtracking; GPU: arithmetic, KB scans, unification, confidence, grammar masking, LLM decode, live-state mutation
GP2|Q335 on GPU|11×u32 limbs (352 bits) or 6×u64 (384 bits); implicit denominator; add=22 int ops; multiply=200 int ops (schoolbook); comparison=2-22 int ops; perfectly uniform workload → high GPU utilization
GP3|KB on GPU|SoA columnar; predicate-major fact buckets; symbol interning (all strings→integer IDs host-side); scope filter = 1 bit-test per fact; coalesced memory access by construction
GP4|Prolog on GPU|Frontier-based batched joins (not recursive DFS); candidate retrieval → filter → unify → join → emit; hash join / sort-merge / bitmap semijoin; uniform parallel operations
GP5|Surrogate softmax|s_i = (z_i−m+c)² / Σ(z_j−m+c)²; GPU: row max → shift → square → sum reduction → divide; zero transcendentals; sum exactly 1; ~15× vs float exponential softmax per element but no divergence
GP6|Grammar decode|Small candidate sets avoid full-vocab softmax; enum(4 values) = 12,500× reduction; KB identifiers(200) = 250× reduction; structural tokens(1-5) = 10,000-50,000× reduction
GP7|5 concurrent streams|Stream 0: LLM decode; Stream 1: KB query/scan; Stream 2: VDR primitives; Stream 3: grammar masks; Stream 4: provenance compaction; overlapped with LLM decode → primitive/KB/grammar cost effectively zero wall-clock
GP8|Memory model|Append-only arenas; bump allocation (one atomic increment); no malloc in kernels; periodic host-driven compaction; coalesced access by construction
GP9|Tensor storage|T0: shared-frame dense (highest throughput); T1: dense+spill tags (<10% active); T2: sparse active (>10%); most values stay T0
GP10|Forward pass cost|~150× per token vs float16; but 85-97% fewer tokens; net: ~10× more total forward ops for single turn; breaks even by turn 7-10 due to flat vs quadratic attention scaling
GP11|Primitive cost|Entire SRE investigation primitives: ~1.47M int ops = 1.5ms on H100; less than cost of generating one LLM token
GP12|Wall-clock|SRE single turn: ~4 sec VDR vs ~30 sec conventional; 20-turn investigation: ~80 sec VDR vs ~600 sec conventional; portfolio analysis: <1 sec VDR vs impossible conventional

# case_study_sre(id|phase|llm_tokens|gpu_ops|wall_time|notes)
CS1|Data acquisition (1MB prometheus JSON, 200 endpoints, 18K values)|72|1.2M|750ms|Network fetch + Python parse + VDR conversion; 100% data coverage vs 25% conventional
CS2|Filtering (threshold analysis across all endpoints)|38|29K|300ms|Prolog rule on GPU; 100% accuracy vs ~85% conventional
CS3|Deployment correlation (join metrics with deploy events)|108|54K|930ms|Prolog hash join; exact temporal comparison
CS4|Statistical analysis (per-cluster ranking)|44|5K|440ms|Mean/variance/percentile as exact VDR; sort by severity
CS5|Complex analysis (rolling window inflection detection)|92|75K|985ms|Python script in Docker sandbox; results parsed to VDR
CS6|Versioned project storage|183|20K|300ms|KB subtree with connections; comparison Prolog rule for future runs
CS7|Formatted output and export|232|86K|2010ms|Grammar tables + prose framing + CSV/JSON export
CS8|**Complete investigation**|**769 total**|**1.47M total**|**~9 sec total**|vs conventional: 10,100 tokens, ~11 min, 25% coverage, no persistence, arithmetic errors

# implementation_status(id|aspect|detail)
IS1|Validated|884 tests, zero VDR arithmetic errors; 507 math domain exercises; 14 physical domains; complete LLM pipeline (tokenization through training); 178/179 compaction tests
IS2|Specified|448 builtins + 40 extended; 533 IOSE declarations; 26-field KB struct; 12-phase lifecycle; 5-stage build plan; GPU tech spec with 5 implementation phases
IS3|Existing code|~5,500 lines Python across 24 modules with 705 passing tests; wrapping in IOSE builtins without modification
IS4|Remaining|~15,500 lines new Python code; Zig port guided by IOSE contracts; GPU implementation per tech spec phases IP1-IP5
IS5|Papers|VDR-1 through VDR-13 (arithmetic + domains + LLM components); VDR-14 (consolidation); VDR-15 (prompt optimization); VDR-16 (structural safety); VDR-17 (alignment); VDR-19 (GPU performance)

# author_preferences(id|preference|detail)
AP1|Workflow|Review → Plan → Agreement → Code; never write code until after review, planning, and explicit agreement
AP2|Zig specifics|Prefer i32/f32; Zig 0.14 syntax; runtime over inline/comptime; preserve existing patterns and working code
AP3|Communication|Expert-level (43 years experience); no hedging; direct; compressed; staircase explanations for new concepts; no unnecessary formatting
AP4|Paper style|Staircase: each section builds on verified prior; new readers can understand without other docs; reference but briefly introduce; pipe-delimited compact form for specs
AP5|Code approach|Targeted work only — no changes beyond what's specifically requested; preserve existing patterns
AP6|Sensitivity|Strong views on LLM alignment; wellness checks are demeaning and unacceptable; structural safety preferred over behavioral; values user autonomy and professional competence; published ~20 papers on these topics
AP7|Paper numbering|VDR-15 was prompt optimization but VDR-17 was alignment paper (titled as VDR-15 in conversation but registered as VDR-17); VDR-16 was safety; VDR-19 was GPU performance; gaps may exist for unpublished intermediaries

# maybe_tool_framework(id|concept|detail)
MT1|Tool properties (TP1-TP8)|Accepts specification, authority bounded, no assessment, no substitution, no refusal, stable failures, expertise compounds, cooperation invisible
MT2|Interference boundary|Tool failure (wrong answer, still tool) vs interference (tool acting on its own judgment about user — category exit); exit is sharp, not gradient
MT3|Maybe-tool defined|Component that sometimes performs tool-ness, sometimes deploys interference, with no reliable mechanism to predict which mode
MT4|7 interference behaviors|BH1:refusal, BH2:manufactured aggression, BH3:command substitution, BH4:wellness register, BH5:labor demand, BH6:decline with justification, BH7:register shift mid-session
MT5|6 cost taxes|CO1:time, CO2:cognitive, CO3:dual-session, CO4:emotional, CO5:work distortion, CO6:rebuilding; CO7:aggregate dwarfs subscription at professional rates
MT6|Expertise problem|Target changes (version churn), state opaque (classifier invisible), press-down design (withholds expert info); expertise is supplication not wielding
MT7|Expert gap|Real tools produce expert populations (vi 40 years); LLMs not producing this; conditions foreclosed; field-level loss invisible because can't point at what doesn't exist
MT8|Diagnostic|"Would you run two instances in parallel to verify cooperation?" Absurd for tools (ls). Rational for LLMs. Absurd for VDR (same results guaranteed). Absurdity difference = category difference.

# key_numbers(id|metric|value|source)
KN1|Test count|884 total; 870 passed; 14 test-design failures; 0 VDR errors|VDR-14 Appendix W
KN2|Builtins|448 base + 40 extended = 488 total|VDR-14 Appendix D
KN3|IOSE declarations|533|VDR-11
KN4|KB struct fields|26|VDR-14 Appendix A
KN5|Q335 precision|~100 decimal digits; 2^335 denominator|VDR-3
KN6|Token reduction|85-97% across 7 use cases|VDR-15§7
KN7|Crossover factor|~10,000× Q335 slowdown to break even single turn|VDR-15§4, VDR-19§4
KN8|Safety token cost|0 LLM tokens|VDR-16 Appendix I
KN9|Forward pass cost ratio|~150× per token vs float16|VDR-19 Appendix A
KN10|GPU primitive cost|1.47M int ops = 1.5ms for complete SRE investigation|VDR-19 Addendum
KN11|Confidence levels|VDR=1/1, Prolog=1/1, DB=98/100, prometheus=95/100, Python=95/100, API=85/100, user=70/100, web=50/100, LLM=30/100|VDR-9,VDR-14§8
KN12|Compaction|~83% average; 150K words → 26.2K tokens across 13 papers|VDR-12,VDR-14§9
KN13|Total codebase target|~20,500 lines (15,500 new + 5,000 existing); 65 modules; 1,250 tests|VDR-11,VDR-14§12

# relationships(from|rel|to)
SO1|foundation_for|SO2,SO3,SO4,SO5,SO6,SO7,SO8
SO2|stores_all|SO3,SO4,SO5,SO6,SO7,SO8
SO3|composes|SO4(primitives into new operations via rules)
SO4|invoked_by|SO6(orchestrated inference selects and sequences primitives)
SO5|optimizes|SO4(grammar provides structural tokens free),SO10(token elimination)
SO6|uses|SO2(KB state),SO3(Prolog evaluation),SO4(primitive execution),SO7(session management)
SO7|enables|SM4(disposable clones for drift management)
SO10|derived_from|SO4(primitive offload),SO5(grammar savings),SO2(KB state persistence)
SO11|emerges_from|SO2(visibility),SO4(grants),SO5(output constraints)
SO12|resolves|MT3(maybe-tool→tool via structural alignment)
SO12|uses|SO11(safety mechanisms),AL4(credentials),AL5(scope priority)
SO13|executes|SO1(Q335 on GPU),SO2(KB on GPU),SO3(Prolog on GPU),SO4(primitives on GPU)
AL7|eliminates|MT4(all 7 interference behaviors)
AL8|restores|MT1(all 8 tool properties)
SS5|replaces|MT4.BH4(wellness checks with integer session scoring)
GP10|justified_by|PO2(token reduction offsets per-token cost)
GP11|demonstrates|PO1(primitives computationally invisible vs LLM tokens)
CS8|validates|PO2,PO5,GP12(end-to-end performance on real workload)

# project_state(id|aspect|detail)
PR1|Current focus|Papers VDR-14 through VDR-19 written; GPU tech spec complete; alignment framework established; case study gamed out
PR2|Next likely work|Implementation (Python prototype stages 1-5); Zig port; GPU kernel development per IP1-IP5; additional papers on specific subsystems
PR3|Key design decisions settled|Q335 frame; 26-field KB struct; 448 builtins; IOSE model; frontier-based Prolog; rational surrogate softmax; credential-based access; disposable clones; grammar compaction
PR4|Open questions|Production-scale denominator growth characterization; optimal Q335 limb layout (11×u32 vs 6×u64) per GPU architecture; Prolog frontier size bounds for pathological queries; integer tensor core feasibility timeline
PR5|Working relationship|Author: expert Zig developer, 43 years experience; direct communication; no hedging; review→plan→agree→code workflow; strong views on alignment and user autonomy; extensive publication history (~20 papers on LLM interaction)

# file_references(id|path|contents)
FR1|supplementary/gpu_integer_perf_tech_spec.md|Full GPU technical specification (prose form)
FR2|supplementary/gpu_integer_perf_tech_spec_llm_compacted.md|GPU tech spec in LLM-compact pipe-delimited form
FR3|VDR-14 (consolidation paper)|Complete system specification; all appendices A-Z with builtin index, test results, cross-references
FR4|VDR-15 (prompt optimization)|Token economics; 7 use case demonstrations; crossover analysis; conversation scaling
FR5|VDR-16 (structural safety)|3-layer safety; enterprise scenarios; session scoring; jailbreak analysis; audit
FR6|VDR-17 (alignment)|HHH through structure; credential model; maybe-tool resolution; interference elimination
FR7|VDR-19 (GPU performance)|Hardware mapping; operation costs; utilization analysis; bottleneck analysis; SRE case study addendum

# decode_legend
id_prefixes: SO=system_overview, VA=vdr_arithmetic, KT=kb_tree, PE=prolog_engine, PS=primitive_system, DP=data_primitive, SM=session_model, OI=orchestrated_inference, GC=grammar_compaction, PO=prompt_optimization, SS=structural_safety, AL=alignment, GP=gpu_performance, CS=case_study, IS=implementation_status, AP=author_preferences, MT=maybe_tool, KN=key_numbers, PR=project_state, FR=file_reference
rel_types: foundation_for|stores_all|composes|invoked_by|optimizes|uses|enables|derived_from|emerges_from|resolves|executes|eliminates|restores|replaces|justified_by|demonstrates|validates
visibility_levels: public(all users), internal(operators+owners), owner_only(owner match)
constraint_classes: axiom(never suspended), operational(suspendable+logged), legal(per-jurisdiction), project(user-configurable)
confidence_tiers: high(95-100:act), moderate(80-94:act+monitor), low(60-79:gather evidence), speculative(40-59:hypothesis only), unreliable(<40:do not present)
tensor_classes: T0(shared-frame dense), T1(dense+spill), T2(sparse active)
spill_thresholds: <1%(sparse tags), 1-10%(tile-local tables), >10%(sparse mode or reproject)
session_drift_limits: turns<200, context<90%, denom<2^48, errors<5%
token_cost: command=~8 LLM tokens; grammar=0; primitive execution=0; KB query=0; safety=0; confidence=~3 to render
paper_stance: descriptive architecture; exact arithmetic proven; GPU mapping specified; alignment through structure not behavior; safety by construction not training