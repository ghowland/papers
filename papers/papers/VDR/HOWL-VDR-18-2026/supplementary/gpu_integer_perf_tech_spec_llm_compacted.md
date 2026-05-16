# GPU TECH SPEC FOR VDR-LLM-PROLOG — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → architecture → execution_classes → numeric_model → q335_gpu → vdr_node → arithmetic_kernels → ml_path → kb_storage → scope → prolog_execution → primitives → live_state → sessions → provenance → confidence → grammar_decode → orchestration → fn_remainder → memory → indexing → operational_boundary → error_handling → determinism → performance → phases → relationships → section_index → decode_legend

# principles(id|principle|detail)
P1|Integer-first execution|exact arithmetic via integer kernels; no floating point in internal exact computation paths
P2|Common case fixed-width, irregular spills to arenas|most values in Q335 fixed-frame closed form; active/remainder structures in append-only arenas
P3|Flat GPU-resident tables|KB, facts, terms, rules, provenance in columnar SoA form; no host-language pointer graphs on device
P4|Prolog as batched joins not recursive DFS|frontier-based execution; candidate filtering and joins; no recursive per-thread control flow for mainline query
P5|Control plane on CPU, data plane on GPU|CPU: paths, grants, sessions, scheduling, external ops, ordering; GPU: arithmetic, KB scans, unification, confidence, grammar masking, LLM decode, live-state mutation
P6|Minimize host-device transfer|path parsing host-side; only integer IDs to GPU; strings interned host-side; device compares only integer symbols
P7|Exact or explicitly logged lossy|reprojection produces exact error bound + provenance event; no silent truncation

# architecture(id|plane|responsibilities)
AR1|Control plane (CPU)|user input, path parsing, path→ID resolution, session orchestration, grant verification, environment/external ops, kernel scheduling, batch formation, deterministic ordering, memory compaction, backtracking decisions, response assembly
AR2|Data plane (GPU)|fixed-width integer arithmetic, Q-basis arithmetic, active remainder spill, KB scans/indexed retrieval, term matching/unification, rule-body frontier expansion, confidence propagation, grammar masking, dense LLM forward/decode, live-state bulk mutation

# execution_classes(id|class|used_for)
EC1|Fixed-width integer arithmetic|int32/int64 fast path, Q335 numerators, counters, bitsets, IDs, interned symbols
EC2|Big integer / limb arithmetic|multi-limb numerators/denominators, exact matrix accumulation, normalization, cross-multiplication comparisons
EC3|Graph / relational kernels|KB traversal, scope filtering, connection queries, fact candidate scans, predicate bucket retrieval
EC4|Prolog kernels|term compatibility filtering, unification, binding extension, join-based rule evaluation, contradiction checks
EC5|LLM kernels|embedding lookup, attention, feedforward, decode, grammar-constrained masking
EC6|Host-only operational|file/process/network/environment ops, path parsing, grants, mount lifecycle, OS integration

# numeric_classes(id|class|representation|use)
NC0|Small integer|signed 32/64-bit immediate|IDs, counters, small exact values, term payloads
NC1|Fixed-frame closed VDR (Q335)|implicit denominator 2³³⁵; numerator in fixed-width limb vector (11×u32=352 bits or 6×u64=384 bits)|common-case exact arithmetic; highest throughput
NC2|General closed rational|numerator limb ref + denominator limb ref|values outside common frame; parsed exact fractions; cross-frame outputs
NC3|Active VDR|top-level value/denominator refs + remainder tag + payload ref|overflow/unresolved exact structure; composite trees; functional remainder descriptors

# q335_gpu(id|aspect|detail)
QG1|Storage|11×u32 limbs (portable) or 6×u64 limbs (optimized); sign via two's-complement for add/sub/compare regularity
QG2|Addition|limbwise add with carry propagation; overflow beyond frame policy → spill to active form
QG3|Multiplication|compute full product A×B; split at bit 335; high part = quotient (V), low 335 bits = remainder; zero remainder → closed, nonzero → active node
QG4|Comparison|same-tag fast path → same-frame lexicographic → small-int immediate → rational cross-multiply → active normalized projection
QG5|Reprojection|inputs: value ref + target exponent; outputs: projected closed value + exact error bound + provenance event ID

# vdr_node_layout(id|struct|fields|notes)
VN1|VdrRef|id:u32|handle to backing table
VN2|VdrNode|tag:u8(SMALL_INT/QFRAME/RATIONAL/ACTIVE), flags:u8, depth:u16, v_ref:u32, d_ref:u32, r_ref:u32|v_ref=numerator, d_ref=denominator or implicit-frame code, r_ref=0 for closed else remainder payload
VN3|AtomicR|int_ref:u32|single integer remainder
VN4|CompositeR|base_ref:u32, child_begin:u32, child_count:u32|children in append-only pool
VN5|FunctionalR|fn_id:u16, arity:u16, param_begin:u32, param_count:u32|no device-side arbitrary callables; evaluated by specialized kernel per fn_id

# arithmetic_kernels(id|kernel|description)
AK1|Limb add/sub/compare/shift|basic multi-precision operations
AK2|Schoolbook multiply|with optional Karatsuba/Toom thresholds for large operands
AK3|Power-of-two divmod split|Q335 multiply split at bit 335; quotient + exact remainder
AK4|Sign normalization|ensure canonical sign placement
AK5|GCD reduction|for closed rationals
AK6|Q-frame reprojection batch|batch input values → projected closed + error bound + provenance events
AK7|Active merge / child merge|combine remainder children; same-denominator merge
AK8|Canonical sort|segmented sort for child descriptors in normalization
AK9|Normalization pipeline|mark active roots → parallel normalize leaves → upward compaction → canonical ordering via segmented sort

# ml_path(id|aspect|detail)
ML1|Tensor storage T0|shared-frame dense: all entries same implicit denominator; numerators stored densely; highest throughput
ML2|Tensor storage T1|dense with spill tags: per-entry tag closed/spill; spill entries reference active pool
ML3|Tensor storage T2|sparse active: only when active density >10%; sparse coordinates or tile-local spill lists
ML4|Embedding lookup|embedding tables as shared-frame dense tensors; token IDs index into Q335 matrix
ML5|Exact attention|Q·Kᵀ → causal mask → normalization (rational surrogate preferred for GPU) → weight/value mix → residual add
ML6|Rational surrogate softmax|sᵢ = (zᵢ−m+c)² / Σ(zⱼ−m+c)²; GPU: row max/shift → square → row sum reduction → division; sum exactly 1
ML7|ReLU|piecewise linear; exact zero or exact passthrough; recommended activation for GPU path
ML8|Gradient path|backward graph as flat GradNode records (op, arity, input_begin, output_ref, aux_ref); topologically sorted; batched by op type; exact per-op kernels

# kb_storage(id|aspect|detail)
KB1|KB metadata|SoA: parent, first_child, child_count, visibility, frozen, owner, created_at, modified_at
KB2|Path handling|dotted path parsing CPU-side; tokenize → resolve segment chain to KB ID → cache; GPU receives only integer IDs
KB3|Fact storage|predicate-major columnar: pred_bucket_offset/count → fact_kb_id, fact_pred_id, fact_arg_begin, fact_arity, fact_turn, fact_confidence_ref, fact_derivation_ref
KB4|Term pool|SoA: tag(atom/var/int/vdr/list/kbref) + payload0 + payload1; atom=atom_id, var=local_var_id, int=small/int_ref, vdr=vdr_ref, list=element_begin+count, kbref=kb_id
KB5|Symbol interning|all strings interned host-side before device use; domains: predicate names, atom values, path segments, grammar nonterminals, builtin names, relation types, source types; device compares only integer symbols

# scope(id|aspect|detail)
SC1|Scope chain|host constructs per request: uint32_t ids[16] + len; if depth >16 use device buffer
SC2|Interval acceleration|DFS in/out interval per KB subtree; "visible in subtree" or "descendant of" = interval check; enables fast scope filtering
SC3|Scope filter kernel|inputs: fact_kb_id array + visible_kbs; output: bitmask; strategies: binary search, bitset membership, interval test + shadow-resolution pass

# prolog_execution(id|aspect|detail)
PG1|Strategy|frontier-based: candidate retrieval by predicate → term compatibility filter → unification producing binding frontier → rule-body joins → solution emission → optional host-driven backtracking
PG2|Query representation|QueryGoal(pred_id, arg_begin, arity) + QueryPlan(goal_begin, goal_count, mode:find-all/first, scope_ref)
PG3|Binding representation|BindingRow(var_begin, var_count, flags) + BindingValue(var_id, term_ref); small maps, registers/shared memory with spill to global
PG4|Unification kernel|inputs: goal + candidate fact range + term pool + existing frontier bindings; outputs: success mask + extended binding rows; rules: atom=atom by symbol ID, int=int by value, kbref=kbref by ID, VDR=VDR by value equality policy, var binds if unbound else must match, lists require equal length + recursive element match
PG5|Rule evaluation as joins|rule body goals = chained joins over frontiers; strategies: hash join (equality keys), sort-merge (large frontiers), bitmap semijoin (unary filters)
PG6|Rule storage|rule_head_pred, rule_head_arg_begin, rule_head_arity, rule_body_begin, rule_body_count, rule_kb_id; indexed by head predicate ID
PG7|Deterministic ordering|if first-solution declared: host imposes canonical ordering on candidate facts, rules, join results; GPU computes all, CPU selects first by canonical order

# primitive_model(id|aspect|detail)
PM1|Classes|pure GPU-eligible (VDR ops, list aggregates, graph ops, prob normalization, confidence, KB query, bitset/counter); pure host-only; operational host-only (filesystem/network/process/env); hybrid host/GPU
PM2|Descriptors|PrimitiveDesc: opcode, input_count, output_count, effect_mask, property_mask, exec_class(GPU/CPU/HYBRID)
PM3|Command token lowering|LLM emits structured command → host resolves paths to IDs → lower to Cmd(opcode, argc, arg_begin, result_slot, await) → GPU receives only integers and term refs
PM4|IOSE mapping|IoseDesc per primitive: opcode, inputs, outputs, side_effect_mask, property_mask, exec_class, deterministic flag, exact flag

# live_state(id|primitive|gpu_mechanism)
LS1|Counters|dense arrays of signed integers; batch add kernel with atomic increment; violation flags
LS2|Bitsets|packed u64 words; batch set/clear/test kernels
LS3|Ring buffers|fixed capacity array + atomic write position; optional sequence numbers
LS4|Queues/stacks|batched push/pop only; single-item contended ops host-assisted or block-local
LS5|LRU caches|host-managed exact LRU preferred; device approximate LRU or batched timestamped cache with periodic host reorder

# sessions(id|aspect|detail)
SN1|State split|persistent (facts, rules, constraints, connections, grammars) vs live (counters, locks, queues, stacks, rings, bitsets, scratchpad, working data, scope)
SN2|Snapshot format|SnapshotHeader: session_id + begin/count for each live-state type
SN3|Clone model|copy-on-write over persistent state; duplicate live-state refs; create new delta arenas; share persistent stores
SN4|Reset|discard live-state deltas; restore snapshot baseline refs
SN5|Kill|invalidate live-state refs; keep persistent assertions already committed

# provenance(id|aspect|detail)
PV1|Event log|append-only SoA: event_type, tool_id, subject_ref, input_begin, input_count, output_ref, confidence_ref, turn
PV2|Event emission|every primitive/rule derivation declaring provenance appends event row; device: global atomic append or block-local buffers with later compaction
PV3|Deterministic ordering|append in canonical batch order, or sort appended ranges by (turn, batch_seq, item_seq)

# confidence(id|aspect|detail)
CN1|Representation|VDR refs or fixed-frame rational (denominator 100 or 10000 for bounded sources; exact VDR for arbitrary rule combinations)
CN2|Core formulas as GPU reductions|Prolog derivation: min(C₁..Cₙ); agreement: 1−∏(1−Cᵢ); script: min(inputs)×95/100
CN3|Agreement kernel|inputs: confidence ranges per group; output: combined VDR confidence per group

# grammar_decode(id|aspect|detail)
GD1|Grammar state per decode stream|grammar_id, state_id, slot_type, candidate_begin, candidate_count
GD2|Candidate sources|fixed punctuation tokens, enum values, KB IDs/names, builtin opcodes, relation types, free-text tokens when grammar permits
GD3|Mask generation|GPU kernel builds vocab mask from candidates; OR decode over compact candidate buffer when slot domain small (preferred)
GD4|Example|visibility enum slot → candidates [tok_public, tok_internal, tok_owner_only]; full vocab mask unnecessary

# orchestration(id|aspect|detail)
OR1|Concurrent streams|stream 0: LLM forward/decode; stream 1: KB query/predicate scan; stream 2: VDR primitive execution; stream 3: grammar mask/candidate prep; stream 4: provenance/event compaction; CPU: dependency graph, launch order, external ops, path resolution
OR2|Turn pipeline|1. host parses request → 2. resolve paths/scope → 3. GPU prefetch scoped facts/rules → 4. LLM begins decode → 5. command token emitted → host lowers to opcode batch → 6. GPU executes pure queries/primitives → 7. results to scratchpad/KB → 8. grammar masks updated → 9. LLM continues with structured state → 10. provenance committed → 11. response assembled

# fn_remainder(id|aspect|detail)
FR1|Opcode model|stored as fn_id(SQRT/EXP/LOG/SIN/COS/ARCTAN/ZETA) + params; no device-side arbitrary callable semantics
FR2|Evaluation|specialized kernel per fn_id at requested depth; FnEvalReq(fn_id, depth, param_begin, param_count) → VdrRef output
FR3|Newton example|sqrt: initialize seed → iterate depth times → output exact rational VDR value

# memory(id|aspect|detail)
MM1|Arena model|all irregular objects in append-only arenas: limb, VDR node, remainder, child list, term, binding, provenance, live-state delta
MM2|Allocation|global bump allocator; per-block suballocator; prefix-sum for predictable sizes; no general-purpose malloc in mainline kernels
MM3|Compaction|host or maintenance kernels periodically compact dead/live ranges, rebuild indexes, remap handles; stable handles for externally visible objects

# indexing(id|type|required)
IX1|Predicate → fact range|required
IX2|Rule-head predicate → rule range|required
IX3|KB subtree intervals (DFS in/out)|required
IX4|Connection source → edge range|required
IX5|Term symbol dictionary|required
IX6|Grammar slot → candidate set|required
IX7|Primitive opcode table|required
IX8|Fact (kb_id, pred_id) composite|optional
IX9|Atom occurrence lists|optional
IX10|Mount source/target maps|optional

# operational_boundary(id|aspect|detail)
OB1|Operational primitives remain host-side|filesystem, network, process, environment
OB2|GPU participation limited to|preparing pure argument material; analyzing fetched results; converting boundary values into VDR forms
OB3|Example flow|LLM emits command → host verifies grant → host executes network op → host receives payload → host parses → GPU/CPU pure conversion stores exact values + provenance facts

# error_handling(id|aspect|detail)
EH1|Result encoding|StatusCode(OK/DIV_ZERO/DOMAIN/OOB/GRANT_DENIED/CONSTRAINT/ALLOC) + flags + value_ref
EH2|Constraint violations|set status; optionally emit event and violation row; never silently disappear

# determinism(id|requirement|mechanism)
DT1|Canonical input order|stable candidate/rule/join result ordering where declared deterministic
DT2|Stable reduction order|exact arithmetic requires deterministic reduction when order affects result
DT3|Stable provenance ordering|events in canonical batch order or post-sorted by (turn, batch_seq, item_seq)
DT4|Stable IDs|session-visible IDs must be stable
DT5|Atomic isolation|GPU nondeterminism from atomics isolated to areas where order explicitly irrelevant or later canonicalized

# performance(id|assumption|detail)
PF1|Most values fixed-frame closed|active spills are minority; dense closed path is fast path
PF2|Indexed predicate scans not full scans|most KB access via bucket lookup
PF3|Joins over moderate frontiers|most rule evaluation expressible as moderate-size joins
PF4|Strings interned|device compares only integer symbols
PF5|Grammar narrows decode candidates|small candidate sets avoid full-vocab softmax
PF6|Active spill thresholds|<1%: dense closed + sparse spill; 1-10%: tile-local spill tables; >10%: sparse active mode or host intervention

# implementation_phases(id|phase|contents)
IP1|Phase 1|Q335 arithmetic backend; closed dense tensor kernels; surrogate attention; confidence kernels
IP2|Phase 2|KB metadata + fact tables on GPU; scope filtering; interned terms; simple fact queries
IP3|Phase 3|frontier-based unification; rule joins; binding buffers; scratchpad/ring/counter/bitset
IP4|Phase 4|active spill arena; normalization passes; functional remainder opcodes
IP5|Phase 5|full command pipeline; grammar-constrained decode integration; provenance/event subsystem; snapshot/clone runtime

# non_goals(id|item)
NG1|Proof of VDR mathematical correctness
NG2|Semantic evaluation of source architecture
NG3|External environment sandbox implementation details
NG4|Specific GPU vendor API binding
NG5|Tensor-core emulation for exact arithmetic
NG6|Full garbage collector design

# relationships(from|rel|to)
P1|governs|EC1,EC2,NC0-NC3,QG1-QG5,AK1-AK9,ML1-ML8
P2|governs|NC1,NC3,VN2-VN5,MM1
P3|governs|KB1-KB5,PG6,IX1-IX10
P4|governs|PG1-PG7
P5|splits|AR1(CPU),AR2(GPU)
P6|governs|KB2,KB5,PM3,OB1-OB3
P7|governs|QG5,AK6,PV1-PV3,EH2
NC1|primary_for|QG1-QG3,ML1,ML4
NC3|spills_to|MM1(append-only arenas)
QG3|implements|VDR remainder nesting on GPU
ML5|uses|ML6(rational surrogate preferred)
ML6|guarantees|sum exactly 1
KB3|indexed_by|IX1
PG6|indexed_by|IX2
SC2|enables|SC3(fast scope filtering)
PG1|uses|PG4(unification),PG5(joins)
PG5|strategies|hash join, sort-merge, bitmap semijoin
PM3|lowers|command tokens to integer opcodes
OR1|pipelines|OR2(turn execution)
OR2|coordinates|EC1-EC5(GPU streams) + EC6(CPU)
FR1|evaluated_by|FR2(specialized kernel per fn_id)
SN3|shares|SN1(persistent state)
SN3|copies|SN1(live state)
GD3|constrains|EC5(LLM decode)
GD4|demonstrates|GD3(small candidate set)
IP1|prereq_of|IP2
IP2|prereq_of|IP3
IP3|prereq_of|IP4
IP4|prereq_of|IP5
PF1|assumption_for|ML1(dense closed fast path)
PF6|governs|ML2,ML3(spill thresholds)

# section_index(section|title|ids)
1|Purpose|P1-P7
2|Design Goals|P1-P7
3|Architecture|AR1-AR2
4|Execution Classes|EC1-EC6
5|Numeric Model|NC0-NC3,QG1-QG5
5.3|VDR Node Layout|VN1-VN5
6|Arithmetic Kernels|AK1-AK9
7|Dense Exact ML Path|ML1-ML8
8|KB Storage|KB1-KB5
9|Scope Model|SC1-SC3
10|Prolog Execution|PG1-PG7
11|Rule Indexing|PG6,IX1-IX2
12|Primitive Execution|PM1-PM4
13|Live-State Primitives|LS1-LS5
14|Sessions and Clones|SN1-SN5
15|Provenance|PV1-PV3
16|Confidence Propagation|CN1-CN3
17|Grammar-Constrained Decode|GD1-GD4
18|LLM Orchestration Pipeline|OR1-OR2
19|Functional Remainder Execution|FR1-FR3
20|Memory Management|MM1-MM3
21|Indexing|IX1-IX10
22|Operational Boundary|OB1-OB3
23|IOSE Mapping|PM4
24|Error Handling|EH1-EH2
25|Determinism|DT1-DT5
26|Performance Strategy|PF1-PF6
28-33|Examples|(inline demonstrations, no separate IDs)
36|Implementation Phases|IP1-IP5
38|Non-Goals|NG1-NG6

# decode_legend
id_prefixes: P=principle, AR=architecture, EC=execution_class, NC=numeric_class, QG=q335_gpu, VN=vdr_node, AK=arithmetic_kernel, ML=ml_path, KB=kb_storage, SC=scope, PG=prolog_execution, PM=primitive_model, LS=live_state, SN=session, PV=provenance, CN=confidence, GD=grammar_decode, OR=orchestration, FR=fn_remainder, MM=memory, IX=index, OB=operational_boundary, EH=error_handling, DT=determinism, PF=performance, IP=implementation_phase, NG=non_goal
Q335_gpu: 11×u32 limbs (352 bits) or 6×u64 limbs (384 bits); implicit denominator 2³³⁵; sign via two's-complement
multiplication_split: A×B = Q·2³³⁵ + Rem; Q→V, Rem→R if nonzero
tensor_classes: T0(shared-frame dense, highest throughput), T1(dense+spill tags), T2(sparse active >10%)
prolog_model: frontier-based joins, not recursive DFS; candidate retrieval → filter → unify → join → emit
softmax_gpu: rational surrogate (z−m+c)²/Σ(z−m+c)² preferred; sum exactly 1; no transcendentals
arena_model: all irregular objects in append-only pools; no general malloc in kernels
rel_types: governs|splits|primary_for|spills_to|implements|uses|guarantees|indexed_by|enables|strategies|lowers|pipelines|coordinates|evaluated_by|shares|copies|constrains|demonstrates|prereq_of|assumption_for
status: draft specification; defines mechanical GPU mapping; does not evaluate source architecture validity
