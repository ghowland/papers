# VDR-11 TECH SPEC — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → module_map → data_structures → fields → enums → registration → stages → stage_modules → builtin_counts → invariants → zig_mapping → falsification → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Comprehensive Then Incremental|10 papers define whole system top-down; 5-stage build each producing complete testable system; never aggregated
P2|Python First Zig Final|Python 3.8 prototype validates; Zig 0.15.1 port mechanical via IOSE contracts; dataclass→struct, dict→HashMap, list→ArrayList
P3|IOSE Throughout|every module/class/function is IOSE node; declarations ARE test specs; starts S1 never relaxes
P4|Existing Code Wrapped|VDR-1–4 codebase (~5000 lines, 23 modules) wrapped not rewritten; core math untouched

# module_map(id|path|stage|status|lines_est|description)
M01|core/vdr.py|exists|exists|~800|VDR triple, closed arithmetic, normalization
M02|core/active_mul.py|exists|exists|~400|active multiplication/division
M03|core/fn.py|exists|exists|~500|functional remainders, discrete calculus
M04|core/linalg.py|exists|exists|~600|Vec, Mat, det, inv, solve
M05|core/types.py|S1|new|~200|number type hierarchy, VDRFraction wrapper, dispatch
M06|core/errors.py|S1|new|~50|Result type, error codes
M07|kb/knowledge_base.py|S1|new|~150|KB struct with all 25 fields
M08|kb/fact_store.py|S1|new|~200|assert, retract, query by predicate scan
M09|kb/rule_engine.py|S1|new|~400|Prolog unification, depth-first search, backtracking
M10|kb/working_data.py|S1|new|~100|scoped key-value bindings
M11|kb/constraint_engine.py|S2|new|~250|constraint checking, enforcement, on_violation dispatch
M12|kb/scope_resolver.py|S2|new|~200|scope chain walking, inheritance, shadowing
M13|path/registry.py|S2|new|~200|path-to-ID mapping, slot IDs
M14|path/resolver.py|S2|new|~150|dotted path resolution, relative paths
M15|path/mount.py|S3|new|~200|mount system, cycle detection, mode enforcement
M16|primitives/text.py|S1|new|~200|17 string operations
M17|primitives/collections.py|S1|new|~400|36 list operations
M18|primitives/arithmetic.py|S1|new|~150|wraps vdr.py: add/sub/mul/div/neg/abs/pow/reciprocal
M19|primitives/active_arithmetic.py|S2|new|~100|wraps active_mul.py
M20|primitives/structure_ops.py|S2|new|~120|lift, rebase, scalar projection
M21|primitives/comparison.py|S1|new|~100|compare, equal, lt, le, min, max, sign, is_zero
M22|primitives/rounding.py|S1|new|~80|floor, ceil, round, truncate, numerator, denominator, simplify
M23|primitives/number_theory.py|S2|new|~250|GCD, LCM, modular ops, combinatorics
M24|primitives/list_aggregates.py|S1|new|~80|sum, product, mean, dot_product
M25|primitives/qbasis.py|S3|new|~200|Q335 transcendental operations
M26|primitives/functional.py|S3|new|~250|sqrt, exp, log, sin, cos, resolve
M27|primitives/discrete_calculus.py|S3|new|~200|derivative, integral, finite difference
M28|primitives/sets.py|S1|new|~150|14 set operations
M29|primitives/mappings.py|S1|new|~150|15 dict operations
M30|primitives/linalg_builtins.py|S2|new|~200|wraps linalg.py with IOSE
M31|primitives/statistics.py|S2|new|~200|mean, variance, percentile, softmax
M32|primitives/probability.py|S2|new|~200|Bayes, normalize, CDF, joint
M33|primitives/conversion.py|S1|new|~200|type conversion, parse_json, format
M34|primitives/time_ops.py|S2|new|~150|date arithmetic, day-of-week
M35|primitives/identity.py|S2|new|~120|hash, base64, hex, CRC32, UUID
M36|primitives/graphs.py|S2|new|~300|BFS, DFS, shortest path, PageRank
M37|primitives/logic.py|S1|new|~150|if/case/for_each/try_catch/findall
M38|primitives/integer_ops.py|S1|new|~150|fast integer path, bit operations
M39|primitives/denom_mgmt.py|S3|new|~100|denominator tracking, reprojection
M40|primitives/polynomial.py|S3|new|~250|Horner, poly arithmetic, Lagrange
M41|primitives/finite_field.py|S3|new|~100|GF(p) operations
M42|primitives/markov.py|S3|new|~150|steady state, step, n-step
M43|primitives/graph_math.py|S3|new|~100|adjacency power, exact PageRank
M44|data_primitives/counter.py|S1|new|~40|bounded counter
M45|data_primitives/lock.py|S1|new|~40|non-blocking lock
M46|data_primitives/lru.py|S2|new|~80|LRU cache
M47|data_primitives/queue.py|S1|new|~50|bounded FIFO
M48|data_primitives/stack.py|S1|new|~50|bounded LIFO
M49|data_primitives/ring_buffer.py|S2|new|~60|fixed-size circular buffer
M50|data_primitives/bitset.py|S2|new|~60|fixed-width bit array
M51|command/token_types.py|S2|new|~80|CommandToken, CommandType enums
M52|command/parser.py|S2|new|~200|parse text+command stream
M53|command/executor.py|S2|new|~250|dispatch to primitives via IOSE registry
M54|command/scratchpad.py|S2|new|~60|RingBuffer-based internal channel
M55|session/snapshot.py|S3|new|~200|capture/restore live state
M56|session/clone.py|S3|new|~150|fork independent sessions
M57|session/lifecycle.py|S3|new|~150|reset, kill, drift detection
M58|inference/notebook.py|S3|new|~200|inference notebook KB schema
M59|inference/loop.py|S3|new|~300|assess/formalize/execute/store loop
M60|inference/modes.py|S4|new|~400|deductive, inductive, abductive, analogical
M61|inference/confidence.py|S3|new|~150|confidence propagation
M62|inference/provenance.py|S3|new|~200|derivation chain, challenge mechanism
M63|env/base.py|S4|new|~200|unified environment interface (10 methods)
M64|env/local.py|S4|new|~300|local execution (dev/test)
M65|env/docker.py|S5|new|~400|Docker container management
M66|env/ssh.py|S5|new|~300|SSH remote execution
M67|env/vm.py|S5|new|~200|VM management
M68|ops/filesystem.py|S4|new|~300|15 file operations
M69|ops/compilation.py|S5|new|~150|compile Python/Zig/C/Rust
M70|ops/execution.py|S4|new|~200|run scripts
M71|ops/linting.py|S5|new|~200|lint, analyze, count
M72|ops/network.py|S4|new|~200|fetch, post, download
M73|ops/process.py|S4|new|~250|background process management
M74|ops/grants.py|S4|new|~200|positive credential grant system
M75|lifecycle/data_pipeline.py|S4|new|~300|source registry, corpus prep
M76|lifecycle/training.py|S4|new|~400|training orchestration (wraps VDR-4 trainer)
M77|lifecycle/feedback.py|S5|new|~350|collection, reward model, alignment
M78|lifecycle/evaluation.py|S4|new|~250|benchmark running, result KB
M79|lifecycle/deployment.py|S5|new|~400|serving config, canary, rollback
M80|lifecycle/monitoring.py|S5|new|~400|runtime metrics, watches, drift
M81|iose/registry.py|S1|new|~150|IOSE declaration storage and query
M82|iose/validator.py|S2|new|~200|type checking, SE preview, contract verify
M83|iose/principles.py|S1|new|~200|OSO axioms, core facts, priority rules

# data_structures(id|name|category|fields_summary|stage)
DS1|VDRFraction|number|v:int, d:int, r:Any(0/int/CompositeRemainder/FnRemainder); methods: is_closed, is_active, is_integer, to_fraction|S1
DS2|CompositeRemainder|number|base:int, children:List[VDRFraction]|S1
DS3|FnRemainder|number|name:str, fn:Callable[[int],VDRFraction], metadata:Dict|S1
DS4|QBasis|number|numerator:int, exponent:int; to_vdr() produces VDRFraction(numerator, 2^exponent, 0)|S3
DS5|IOSEDeclaration|iose|name, inputs:List[str], outputs:List[str], side_effects:List[str], properties:List[IOSEProperty], category:IOSECategory, logic_type:LogicType, description|S1
DS6|IOSEProperty|iose|name:str, value:Any=True|S1
DS7|BuiltinDef|registry|id:int, name:str, category:str, iose:IOSEDeclaration, implementation:Callable|S1
DS8|BuiltinRegistry|registry|_by_id:Dict[int,BuiltinDef], _by_name:Dict[str,BuiltinDef]; methods: register, get_by_id, get_by_name, all_in_category, count|S1
DS9|Fact|kb|predicate:str, args:List[Any], kb_source:str, asserted_at:int, derivation:Optional|S1
DS10|Rule|kb|head:Fact, body:List[Fact], kb_source:str|S1
DS11|Constraint|kb|name, scope(axiom/operational/legal/project/conversation), status(active/suspended/violated/satisfied), condition:str(Prolog), on_violation(warn/block/error/escalate), source|S1
DS12|Connection|kb|target_id:int, target_path:str, relationship:str, direction:Direction, phase, created_at, notes|S1
DS13|Mount|kb|mount_path, source_path, source_id, mode:MountMode, created_at, created_by|S3
DS14|Counter|data_prim|value, min_value, max_value, created_at; methods: inc, dec, add, reset, set (all clamp to bounds)|S1
DS15|LockState|data_prim|held:bool, holder:Optional[str], acquired_at:Optional[int], notes; methods: acquire(→bool), release, force_release|S1
DS16|BoundedQueue|data_prim|capacity:int=50, items:List; methods: push(→bool), pop(→Optional), peek, size, is_empty, is_full, clear, to_list|S1
DS17|BoundedStack|data_prim|capacity:int=30, items:List; methods: push(→bool), pop(→Optional), peek, size, is_empty, clear, to_list(reversed)|S1
DS18|RingBuffer|data_prim|capacity:int=100, items:List, write_pos:int, count:int; methods: write(overwrites oldest), read_all(ordered), read_last(n), size, clear|S2
DS19|Bitset|data_prim|width:int=100, bits:List[bool]; methods: set, clear_bit, test(→bool), count, all_set, any_set, reset, to_list(→indices)|S2
DS20|KnowledgeBase|kb|25 fields across 4 groups: identity(name,path,id), persistent(facts,rules,constraints,connections), live(working_data,lrus,counters,locks,queues,stacks,buffers,bitsets), structural(parent_id,children_ids,mounts), metadata(visibility,frozen,owner,created_at,last_modified,iose_declaration)|S1
DS21|KBLiveState|session|kb_id:int + all 8 live-state dicts deep-copied from KB; persistent facts NOT included|S3
DS22|SessionSnapshot|session|name, path, created_at, active_scope:List[int], active_topic:int, scratchpad:Optional[RingBuffer], kb_states:Dict[int,KBLiveState], turn_count, notes|S3
DS23|CommandToken|command|cmd_type:CommandType, primitive_name, args:List[CommandArg], env, grant, store_result, await_result:bool|S2
DS24|CommandArg|command|arg_type:ArgType, value:Any|S2
DS25|InferenceNotebook|inference|kb:KnowledgeBase + problem_statement, mode:InferenceMode, goal, status:NotebookStatus, conclusion:Optional[InferenceConclusion], max_steps:int=50, max_queries:int=20, stall_threshold:int=5|S3
DS26|InferenceConclusion|inference|statement:Fact, mode, confidence:VDRFraction, derived_from:List, via_rules:List, via_tools:List, alternatives:List, steps_taken, backtracks|S3
DS27|Grant|ops|name, operation_class(filesystem/compile/execute/network/process), allowed_operations:List, location(path prefix or URL pattern), issued_by, issued_at, expires_at, max_uses(0=unlimited), uses_remaining, status:GrantStatus; methods: is_valid, use(→bool, decrements+exhausts)|S4

# enums(id|name|values|used_by)
E1|RemainderForm|zero, atomic, composite, functional|DS1
E2|IOSECategory|pure, operational, composite|DS5
E3|LogicType|operational, application|DS5
E4|Visibility|public, internal, owner_only|DS20
E5|MountMode|read_only, read_write, snapshot, mirror|DS13
E6|Direction|inbound, outbound|DS12
E7|CommandType|pure_fn, op_fn, kb_assert, kb_retract, kb_query, env_exec, env_upload, env_download, ctx_activate, ctx_deactivate, ctx_snapshot, version_create, store_result, direct_output, attachment|DS23
E8|ArgType|path_ref, literal_int, literal_text, literal_bool, literal_fraction|DS24
E9|InferenceMode|deductive, inductive, abductive, analogical|DS25
E10|NotebookStatus|active, concluded, halted, archived|DS25
E11|GrantStatus|active, expired, revoked, exhausted|DS27

# registration_patterns(id|pattern|categories|description)
RP1|pure table-driven, no side effects|text(17), collections(36), sets(14), mappings(15), comparison(10), rounding(7), integer_ops(21), conversion(14), time(10), identity(8), logic(11)|table of (id,name,inputs,outputs,properties,desc,impl); register_builtin helper
RP2|table-driven, KB-internal side effects|kb_ops(15), data_primitives(53), path_mount(17), session(8)|same table + side_effects column
RP3|VDR arithmetic wrapping|closed_arithmetic(8), active_arithmetic(5), structure_ops(3), list_aggregates(8), number_theory(13)|delegate to existing VDR/active_mul classes via thin adapter
RP4|linalg wrapping|linalg_builtins(24)|delegate to existing linalg.py Vec/Mat
RP5|ML wrapping|statistics(16)|delegate to existing softmax.py etc.
RP6|grant-gated operational|filesystem(15), compilation(4), execution(5), linting(8), network(5), process(7)|grant_store.verify_grant before dispatch
RP7|domain-specific|qbasis(7), functional(8), discrete_calculus(6), polynomial(8), finite_field(4), markov(3), graph_math(2), denom_mgmt(5)|slightly different construction per domain

# stages(id|name|new_modules|cumul_modules|builtins_active|new_lines|tests|cumul_tests|capability)
S1|Toy Full Lifecycle|24|24|~150|~2800|150|150|KB+facts+rules+basic arithmetic+data primitives+toy lifecycle loop (init→train→checkpoint→evaluate→report)
S2|Upgraded Toy|13|37|~300|~3200|200|350|command tokens+paths+scope+constraints+statistics+graphs+scratchpad
S3|Capacity Building|12|49|~400|~3000|250|600|sessions+inference notebooks+Q-basis+functional+discrete calc+domain math+mounts
S4|Full Integration|9|58|~420|~3500|300|900|local env+grants+filesystem+network+execution+all 4 inference modes+lifecycle pipeline
S5|Production|7|65|448|~3000|350|1250|Docker+SSH+VM+compilation+linting+feedback+deployment+monitoring+canary+retirement

# invariants(id|invariant|verified_by)
INV1|IOSE declared — every function has declaration before implementation|registry check at startup
INV2|Exact arithmetic — every numeric op uses VDR fractions or exact ints, no floats|type system enforcement
INV3|KB is truth — all persistent state in KBs, no module globals|module state audit
INV4|Data primitives bounded — declared capacity enforced at every mutation|constructor enforcement
INV5|No silent truncation — every precision reduction declared with exact error bound|conversion boundary logging
INV6|Tests cumulative — all current + prior stage tests pass|CI run
INV7|OSO principles loaded — root.system.oso KB active at startup|startup check
INV8|Idempotent where declared — f(f(x))=f(x) tested|dedicated idempotency tests
INV9|One canonical method per task category|registry uniqueness check

# zig_mapping(id|python|zig|difficulty)
ZM1|dataclass|struct|direct
ZM2|Dict[str,T]|std.StringHashMap(T)|direct
ZM3|List[T]|std.ArrayList(T)|direct
ZM4|Optional[T]|?T|direct
ZM5|Enum|enum|direct
ZM6|int (arbitrary)|i128 w/ overflow to BigInt|medium
ZM7|str|[]const u8 or std.ArrayList(u8)|direct
ZM8|bool|bool|direct
ZM9|Callable|fn pointer or interface|slightly different
ZM10|try/except|error union w/ errdefer|different pattern same semantics
ZM11|dict/list comprehension|loop w/ put/append|mechanical

# falsification(id|criterion)
F1|IOSE declarations don't match actual behavior at any stage → IOSE model is decorative
F2|any builtin introduced without IOSE declaration → comprehensive discipline violated
F3|any stage cannot execute declared lifecycle capability end-to-end → stage incomplete
F4|Zig port produces different results from Python for same inputs → port correctness bug
F5|cumulative test count below target at any stage → insufficient coverage

# relationships(from|rel|to)
P1|governs|S1,S2,S3,S4,S5
P2|governs|S1,S5
P3|governs|S1,S2,S3,S4,S5
P4|governs|S1
S1|prereq_of|S2
S2|prereq_of|S3
S3|prereq_of|S4
S4|prereq_of|S5
DS1|used_by|DS2,DS3,DS4,DS20,DS26
DS5|used_by|DS7,DS20
DS7|stored_in|DS8
DS9|stored_in|DS20
DS10|stored_in|DS20
DS11|stored_in|DS20
DS14|stored_in|DS20
DS15|stored_in|DS20
DS16|stored_in|DS20
DS17|stored_in|DS20
DS18|stored_in|DS20
DS19|stored_in|DS20
DS20|captured_by|DS21
DS21|stored_in|DS22
DS23|parsed_by|M52
DS23|executed_by|M53
DS25|uses|DS20,DS26
DS27|gates|RP6
M09|implements|DS9,DS10
M08|implements|DS9
M07|implements|DS20
M53|dispatches_via|DS8
M55|produces|DS22
M56|consumes|DS22
M59|uses|DS25,M53
M60|specializes|M59
M63|implemented_by|M64,M65,M66,M67
RP1|registers_into|DS8
RP2|registers_into|DS8
RP3|registers_into|DS8
RP4|registers_into|DS8
RP5|registers_into|DS8
RP6|registers_into|DS8
RP7|registers_into|DS8
INV1|validates|P3
INV2|enforces|DS1
INV3|enforces|DS20
INV4|enforces|DS14,DS15,DS16,DS17,DS18,DS19
INV6|enforces|S1,S2,S3,S4,S5
F1|validates|INV1
F2|validates|P3
F3|validates|P1,S1,S2,S3,S4,S5
F4|validates|P2
F5|validates|INV6

# section_index(section|title|ids)
1|Build Philosophy|P1,P2,P3,P4
2|Module Map|M01-M83
3.1|Number Types|DS1,DS2,DS3,DS4,E1
3.2|IOSE Declaration|DS5,DS6,E2,E3
3.3|KB Struct|DS7-DS20,E4,E5,E6,DS9,DS10,DS11,DS12,DS14-DS19
3.4|Session Snapshot|DS21,DS22
3.5|Command Token|DS23,DS24,E7,E8
3.6|Inference Notebook|DS25,DS26,E9,E10
3.7|Grant|DS27,E11
4|Builtin Registration Pattern|RP1-RP7,DS7,DS8
5.1|Stage 1|S1
5.2|Stage 2|S2
5.3|Stage 3|S3
5.4|Stage 4|S4
5.5|Stage 5|S5
6|Stage Deliverables Summary|S1-S5
7|Cross-Stage Invariants|INV1-INV9
8|Zig Port Strategy|ZM1-ZM11
9|File Listing per Stage|M01-M83
10|Total Estimates|S1-S5
11|Falsification Criteria|F1-F5

# decode_legend
id_prefixes: P=principle, M=module, DS=data_structure, E=enum, RP=registration_pattern, S=stage, INV=invariant, ZM=zig_mapping, F=falsification
stage_values: exists=VDR-4 code, S1-S5=build stage
status_values: exists=already written, new=to be written
rel_types: governs|prereq_of|used_by|stored_in|captured_by|parsed_by|executed_by|uses|gates|implements|dispatches_via|produces|consumes|specializes|implemented_by|registers_into|validates|enforces
line_counts: approximate, from spec estimates
builtin_counts: ~markers indicate rounding
test_counts: targets not actuals
module_count: 83 rows but includes existing VDR-4 modules; 65 new modules per VDR-11 paper count; difference is existing code + __init__.py files not counted separately
total_code: ~15500 new + ~5000 existing = ~20500 lines
