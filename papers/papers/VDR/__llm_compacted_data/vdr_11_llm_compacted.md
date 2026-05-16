# VDR-11 IMPLEMENTATION BLUEPRINT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → stages → modules → layers → builtins → invariants → design_decisions → integration → test_targets → zig_mapping → falsification → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Comprehensive Then Incremental|whole system specified top-down before incremental 5-stage build; each stage complete+testable, never aggregated (C18)
P2|Python First Zig Final|Python 3.8 prototype validates decisions; Zig 0.15.1 port is mechanical via IOSE interface contracts
P3|IOSE At Every Function|declaration before implementation; declaration = test spec + docs + Zig interface contract
P4|Existing Code Wrapped Not Rewritten|VDR-1–4 codebase (~5500 lines, 705 tests) wrapped in IOSE-declared builtins; core math untouched
P5|Stage Completeness|each stage produces runnable system handling full lifecycle at its capability level

# stages(id|name|capability_summary|new_modules|cumulative_modules|new_builtins|cumulative_builtins|new_lines|test_target|cumulative_tests)
S1|Toy Full Lifecycle|create KBs, assert/query facts, Prolog rules w/ unification+backtracking, exact VDR arithmetic, counters/locks/queues/stacks, one lifecycle pass: init→train→checkpoint→evaluate→report|24|24|~161|~161|~2800|150|150
S2|Upgraded Toy|command tokens replace API calls, path addressing w/ integer ID acceleration, scope resolution w/ topic switching, constraints fire on violations, scratchpad|13|37|~139|~300|~3200|200|350
S3|Capacity Building|session snapshots+clones, inference notebooks w/ assess-formalize-execute-store loop, Q-basis transcendentals, functional remainders, discrete calculus, domain math (polynomial/finite field/Markov/graph), denominator management, mount system|12|49|~100|~400|~3000|250|600
S4|Full Integration|sandboxed environments (local), filesystem/network/process ops, positive credential grants, all 4 inference modes, lifecycle pipeline (source→corpus→tokenize→train→checkpoint→evaluate)|9|58|~37|~437|~3500|300|900
S5|Production Completion|Docker+SSH+VM environments, compilation+linting, feedback collection+reward models+DPO, deployment+canary+rollback, monitoring+drift detection, retirement+audit archival|7|65|~11|~448|~3000|350|1250

# layers(id|name|directory|depends_on|description)
L1|Core|core/|stdlib only|existing VDR arithmetic + new type dispatch (types.py) + error handling (errors.py); 5 existing + 2 new modules
L2|Knowledge Base|kb/|L1|KB struct (25 fields), fact store, Prolog rule engine, constraint engine, scope resolver, working data bindings; 6 modules
L3|Path|path/|L2|path-to-integer registry, dotted path resolution, mount system w/ cycle detection; 3 modules
L4|Data Primitives|data_primitives/|L2|counter, lock, queue, stack, LRU cache, ring buffer, bitset; 7 modules
L5|Primitives|primitives/|L1,L2|all 448 builtins as IOSE-declared functions across 28 category modules
L6|Command|command/|L5,L3,L2|token types, stream parser, dispatch executor, scratchpad; 4 modules
L7|IOSE|iose/|L2,L5|declaration registry, chain validator, OSO principle loader; 3 modules
L8|Session|session/|L2,L4,L3|snapshot capture/restore, clone create/destroy, lifecycle ops; 3 modules
L9|Inference|inference/|L2,L5,L6,L8|notebook+templates, assess-formalize-execute-store loop, 4 inference modes, confidence propagation, provenance+challenge; 5 modules
L10|Environment|env/|L2,L6|abstract base (10 methods), local, Docker, SSH, VM; 5 modules
L11|Operations|ops/|L10,L2,L6|filesystem, script execution, compilation, linting, network, process mgmt, grant verification; 7 modules
L12|Lifecycle|lifecycle/|L11,L2,L5,L9|data pipeline, training orchestration, evaluation, feedback, deployment, monitoring; 6 modules

# builtin_categories(id|category|count|stage|registration_pattern)
BC1|VDR closed arithmetic|8|S1|wrap vdr.py class methods
BC2|Comparison|10|S1|pure, VDRFraction→simple
BC3|Rounding/extraction|7|S1|pure, VDRFraction→int/bool
BC4|List aggregates|8|S1|pure, List[VDRFraction]→VDRFraction
BC5|Text|17|S1|pure, string→string/bool/int/list
BC6|Collections|36|S1|pure, list→list/item/bool/int
BC7|Sets|14|S1|pure, set→set/bool/int
BC8|Mappings|15|S1|pure, dict→dict/value/list
BC9|Conversion|14|S1|pure (some partial), mixed
BC10|Logic|11|S1|pure, mixed
BC11|Integer + bit ops|21|S1|pure, int→int/bool/list
BC12|Active arithmetic|5|S2|wrap active_mul.py
BC13|Structure ops|3|S2|lift, rebase, projection
BC14|Number theory|13|S2|pure, int→int
BC15|Linear algebra|24|S2|wrap linalg.py
BC16|Statistics + probability|16|S2|pure, list/fraction→fraction/list
BC17|Time|10|S2|pure, int→int/str
BC18|Identity|8|S2|pure, deterministic
BC19|Graphs|13|S2|pure, graph→list/bool/int
BC20|KB operations|15|S2|KB-internal side effects
BC21|Data primitives (LRU+ring+bitset)|21|S2|KB-internal side effects
BC22|Path operations|8|S2|pure
BC23|Q-basis|7|S3|transcendental constant manipulation
BC24|Functional remainder|8|S3|sqrt/exp/log/sin/cos at arbitrary depth
BC25|Discrete calculus|6|S3|exact derivatives and integrals
BC26|Denominator management|5|S3|growth tracking and control
BC27|Polynomial|8|S3|eval/add/mul/div/gcd/derivative/integral/lagrange
BC28|Finite field|4|S3|GF arithmetic
BC29|Markov|3|S3|steady state, step, n-step
BC30|Graph math|2|S3|adjacency power, exact pagerank
BC31|Filesystem|15|S4|grant-gated, env-dispatched
BC32|Execution|5|S4|grant-gated, env-dispatched
BC33|Network|5|S4|grant-gated
BC34|Process|7|S4|grant-gated
BC35|Grant operations|5|S4|store/verify/use/list/expire
BC36|Compilation|4|S5|Zig/C/Rust/Python syntax check
BC37|Linting|8|S5|lint+validate+complexity+import analysis

# invariants(id|invariant|enforcement)
INV1|IOSE declared|every function has declaration before implementation; invariant tests verify all registered builtins have declarations
INV2|Exact arithmetic|every numeric op uses VDR fractions or exact ints; no floats in computation path; conversion boundary logged with exact error bound
INV3|KB is truth|all persistent state in KBs; no module globals holding state; KB store is single source of truth (C39 model for control)
INV4|Data primitives bounded|every counter/queue/stack/ring/LRU/bitset has declared max capacity enforced at every mutation
INV5|No silent truncation|every precision reduction declared with exact error bound; reprojection logs exact error; lossy display marks generating fraction available
INV6|Tests cumulative|all tests from current + all prior stages pass; never regress
INV7|OSO principles loaded|root.system.oso KB loaded at startup: 15 axioms, ~80 facts, ~60 rules, 21 constraints; active Prolog rules, not documentation
INV8|Idempotent where declared|f(f(x))=f(x) tested for all idempotent-tagged operations

# design_decisions(id|decision|mechanism|rationale)
DD1|Result type|every failable function returns Ok(value) or Err(VDRError); no exceptions for expected failures|OSO D4/C31: operational logic handles failure explicitly; every failure path visible in signature
DD2|KB Store|global dict mapping int IDs to KnowledgeBase instances; every function takes store as parameter|C39 model for control; single source of truth
DD3|Turn counter|global int incremented per user interaction; every mutation/snapshot/evidence records turn number|total ordering without wall-clock; deterministic across platforms
DD4|Deep copy for snapshots|snapshot deep-copies all live state; completely independent of source|essential for disposable clone pattern; clones must be independent
DD5|Functional remainder deferred resolution|FnRemainder sits as callable until fn_resolve(fn_remainder, depth) explicitly called|resolution at different depths produces different exact rationals; system never silently resolves at arbitrary depth
DD6|Wrapping pattern|accept VDRFraction dataclass→convert to VDR class→call existing→convert back→return Result|adapter copies values, does not transform; fields identical between VDRFraction and VDR

# rule_engine(id|aspect|detail)
RE1|Term types|5: atoms (string equality), variables (?-prefix, bind on match), VDR fractions (normalized value equality via cross-multiplication), lists (element-wise, length must match), facts (predicate match + recursive arg unification)
RE2|Evaluation|depth-first search w/ backtracking; for each fact matching goal predicate attempt unification; for each rule whose head matches, recursively evaluate body threading bindings
RE3|Depth limit|default 100; prevents infinite recursion
RE4|Modes|findall (collect all solutions) and first-solution-only (cut after first match; used for scoped queries)

# integration_points(id|from_stage|to_stage|what_changes)
IP1|S1|S2|S1 primitives become dispatchable via command tokens; executor looks up by name in registry, resolves paths, calls impl; no primitive code changes
IP2|S2|S3|scope resolver gains mount-awareness; follows mounts respecting mode restrictions; query interface unchanged
IP3|S2|S3|command executor gains scratchpad integration; internal results auto-written to ring buffer; inference loop reads scratchpad
IP4|S3|S4|inference loop formalize step gains real tool execution; can generate command tokens invoking operational primitives (fetch URL, read file, execute script); loop structure unchanged
IP5|S4|S5|local environment joined by Docker/SSH/VM; executor unchanged (same 10-method interface); environment selection is a configuration fact in deployment KB

# test_targets(id|stage|unit|integration|lifecycle|invariant|total|cumulative)
TT1|S1|120|15|5|10|150|150
TT2|S2|160|25|5|10|200|350
TT3|S3|200|30|10|10|250|600
TT4|S4|230|40|20|10|300|900
TT5|S5|260|50|30|10|350|1250

# test_layers(id|layer|description)
TL1|Unit|individual functions against IOSE declarations: input declared inputs, check outputs, verify side effects, confirm properties
TL2|Integration|multi-function chains: scoped query exercises fact store + scope resolver + KB store together
TL3|Lifecycle|end-to-end scenarios: toy lifecycle (S1) through full lifecycle (S5)
TL4|Invariant|cross-stage invariants from INV1-INV8; run at every stage

# zig_mapping(id|python_type|zig_type|notes)
ZM1|int (small)|i32 or i64|counter values, IDs, indices
ZM2|int (arbitrary)|i128 w/ BigInt overflow|VDR numerator/denominator, Q335; 99% fit i128
ZM3|str|[]const u8 or std.ArrayList(u8)|immutable vs mutable
ZM4|Optional[T]|?T|direct
ZM5|List[T]|std.ArrayList(T)|dynamic array
ZM6|Dict[str,T]|std.StringHashMap(T)|string-keyed map
ZM7|Dict[int,T]|std.AutoHashMap(i32,T)|integer-keyed map
ZM8|Enum|const MyEnum = enum { ... }|direct
ZM9|@dataclass|const MyStruct = struct { ... }|direct
ZM10|Result[T]|MyError!T|Zig-native error union
ZM11|copy.deepcopy|arena allocator + structured copy|arenas make bulk alloc/dealloc efficient
ZM12|Scope chain List[int]|[16]i32 stack-allocated|max depth 16 from VDR-8; avoids allocation
ZM13|List[bool] bitset|std.StaticBitSet or DynamicBitSet|native packed bit ops
ZM14|Callable[[A],B]|fn(A) B or *const fn(A) B|function pointer

# zig_perf_decisions(id|area|python_approach|zig_approach|rationale)
ZP1|KB fact storage|List[Fact] linear scan|ArrayList(Fact) + hash index on predicate|O(1) avg vs O(n) per query
ZP2|String predicates|no interning|StringPool w/ integer handles|reduces memory, enables integer comparison
ZP3|Ring buffer|list w/ modular indexing|fixed-size array w/ write_pos|stack-allocated for small capacity
ZP4|Snapshots|copy.deepcopy|arena allocator + structured copy|efficient bulk alloc/dealloc

# memory_estimates(id|scenario|kbs|facts|python_mem|zig_mem)
ME1|Toy lifecycle (S1)|5|50|~200 KB|~30 KB
ME2|Upgraded toy (S2)|15|200|~1 MB|~150 KB
ME3|Active inference (S3)|30|500|~3 MB|~500 KB
ME4|Full lifecycle (S4)|100|2000|~15 MB|~3 MB
ME5|Production w/ history (S5)|500|10000|~80 MB|~15 MB
ME6|Large deployment (post-S5)|2000|50000|~400 MB|~80 MB
# Python overhead ~5-6× Zig for same logical content

# code_estimates(id|stage|lines|biggest_components)
CE1|S1|~2800|text/collections/sets/mappings primitives (~900), Prolog rule engine (~400), KB struct+fact store (~350)
CE2|S2|~3200|statistics+probability (~400), graph algorithms (~300), number theory (~250), constraint+scope+command (~700)
CE3|S3|~3000|inference loop (~300), functional remainder (~250), polynomial (~250), Q-basis (~200), session (~500)
CE4|S4|~3500|training orchestration (~400), inference modes (~400), data pipeline (~300), filesystem (~300), local env (~300)
CE5|S5|~3000|Docker env (~400), monitoring (~400), deployment (~400), feedback (~350), SSH env (~300)
# Total new: ~15500. Existing VDR-4: ~5500. Grand total: ~21000

# existing_codebase(id|category|modules|lines_est|wrapped_at_stage)
EC1|Arithmetic|vdr.py, active_mul.py|~1200|S1 (vdr), S2 (active_mul)
EC2|Transcendental|fn.py, exp.py, logarithm.py, basis.py|~1200|S3
EC3|Linear algebra|linalg.py, tensor.py|~800|S2
EC4|ML stack|softmax.py, autodiff.py, nn.py, losses.py|~1050|S2 (softmax), S4 (rest)
EC5|Infrastructure|optim.py, rng.py, init.py, sampling.py, datasets.py, metrics.py, checkpoint.py|~1150|S1 (rng), S4 (rest)
EC6|Architecture|attention.py, transformer.py, trainer.py|~1000|S4
EC7|Export|export.py|~150|S1

# risks(id|risk|impact|likelihood|mitigation|stage)
RK1|Rule engine slow for large KBs|query latency scales w/ fact count|medium|add predicate index (hash map) at S2; linear scan ok for S1 toy sizes|S2+
RK2|Denominator growth exceeds memory during training|OOM on long runs|medium|denominator management builtins (S3); budget constraints trigger reprojection|S3+
RK3|Python prototype too slow for realistic training|exact fractions orders of magnitude slower than float|high (expected)|prototype validates correctness not performance; toy models only; Zig port for production|all
RK4|Scope creep at any stage|stage never completes|medium|fixed module list + test count per stage; done when all tests pass; no mid-stage additions|all
RK5|IOSE becomes decorative|tests pass but contracts not verified|medium|invariant tests check all builtins have declarations; IOSE validator (S2) checks contracts|S2+
RK6|Zig port reveals Python-specific assumptions|some idioms don't translate|medium|avoid Python-specific patterns from start: no operator overloading in builtins, no exceptions (use Result), no global state (pass KB store)|all

# falsification(id|criterion)
F1|any stage cannot execute its declared lifecycle capability end-to-end → stage incomplete
F2|any function implemented without IOSE declaration → IOSE discipline violated
F3|any cross-stage invariant fails at any stage (float in computation, unbounded primitive, non-idempotent idempotent-tagged op) → enforcement gap
F4|test count at any stage below target → insufficient coverage for claims
F5|Zig port of any function produces different result from Python for same inputs → port correctness bug; IOSE declaration inadequately specified
F6|Stage N change breaks Stage N-1 test → incremental build discipline violated; cumulative tests must never regress
F7|supplementary IOSE spec and implementation disagree on inputs/outputs/side effects → spec is authority, implementation has bug

# relationships(from|rel|to)
P1|governs|S1,S2,S3,S4,S5
P2|governs|S1,S5
P3|governs|S1,S2,S3,S4,S5
P4|governs|S1
P5|governs|S1,S2,S3,S4,S5
S1|prereq_of|S2
S2|prereq_of|S3
S3|prereq_of|S4
S4|prereq_of|S5
L1|depended_on_by|L2,L5
L2|depended_on_by|L3,L4,L5,L6,L7,L8,L9,L10,L11,L12
L3|depended_on_by|L6,L8
L4|depended_on_by|L8
L5|depended_on_by|L6,L7,L12
L6|depended_on_by|L9,L10
L8|depended_on_by|L9
L9|depended_on_by|L12
L10|depended_on_by|L11
L11|depended_on_by|L12
INV1|enforced_by|TL4
INV2|enforced_by|TL4
INV3|enforced_by|DD2
INV4|enforced_by|TL4
INV5|enforced_by|DD5
INV6|enforced_by|TL4
INV7|enforced_by|TL4
INV8|enforced_by|TL4
DD1|implements|INV5
DD2|implements|INV3
DD4|enables|INV8
DD6|implements|P4
RE1|component_of|L2
IP1|connects|S1,S2
IP2|connects|S2,S3
IP3|connects|S2,S3
IP4|connects|S3,S4
IP5|connects|S4,S5
F1|validates|P5
F2|validates|P3
F3|validates|INV1,INV2,INV3,INV4,INV5,INV8
F5|validates|P2
F6|validates|INV6

# section_index(section|title|ids)
1|Context|EC1-EC7
2|Build Philosophy|P1,P2,P3,P4,P5
3|Module Architecture|L1-L12
4.1|Stage 1|S1,RE1-RE4
4.2|Stage 2|S2
4.3|Stage 3|S3
4.4|Stage 4|S4
4.5|Stage 5|S5
5|Cross-Stage Invariants|INV1-INV8
6|Existing Codebase|EC1-EC7
7|New Code Estimates|CE1-CE5
8|Builtin Registration Pattern|BC1-BC37
9|Prolog Rule Engine|RE1-RE4
10|Key Design Decisions|DD1-DD6
11|Integration Points|IP1-IP5
12|Test Strategy|TT1-TT5,TL1-TL4
13|Zig Port|ZM1-ZM14,ZP1-ZP4
14|Falsification Criteria|F1-F7
AppA|Module Dependencies|L1-L12
AppB|VDR-4 Inventory|EC1-EC7,DD6
AppC|Memory Estimates|ME1-ME6
AppD|Test Plan Detail|TT1-TT5
AppE|Builtin Registration|BC1-BC37
AppF|Python 3.8 Compat|(compatibility constraints, no IDs)
AppG|Zig Type Mapping|ZM1-ZM14,ZP1-ZP4
AppH|Risk Registry|RK1-RK6
AppI|Glossary|(term definitions, no IDs)
AppJ|Cumulative Stats|(series summary, no IDs)

# decode_legend
id_prefixes: P=principle, S=stage, L=layer, BC=builtin_category, INV=invariant, DD=design_decision, RE=rule_engine, IP=integration_point, TT=test_target, TL=test_layer, ZM=zig_mapping, ZP=zig_perf, ME=memory_estimate, CE=code_estimate, EC=existing_codebase, RK=risk, F=falsification
rel_types: governs|prereq_of|depended_on_by|enforced_by|implements|enables|component_of|connects|validates
claim_types: not used (paper is engineering spec, not philosophical; all entries are commitments)
stage_status: S1-S5 are planned, not built
line_counts: approximate, from paper estimates
builtin_counts: ~markers indicate rounding; exact counts in appendix tables
test_counts: targets not actuals
memory_estimates: order-of-magnitude from paper Appendix C
existing_code: ~5500 lines across 24 modules, 705 passing tests, zero VDR computation errors
new_code: ~15500 lines across 65 modules
total: ~21000 lines, 448 builtins, 1250 planned tests
