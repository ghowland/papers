# COMPUTATIONAL PRIMITIVES AND OPERATIONAL ENVIRONMENTS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → pure primitives → operational primitives → grants → command tokens → environments → async → versioning → download → relationships → sections

# principles(id|principle|rationale)
P1|Separation of concerns|LLM understands intent; primitives compute; environments execute; KBs store; constraints authorize; surfacing presents; no component does another's job
P2|Pure primitives are infallible|Same inputs → same outputs; no side effects; terminates in bounded time; operates on exact VDR types; no authorization required
P3|Operational primitives require positive credential grants|Default is denial; grant must explicitly authorize operation class, specific operations, target location, and be currently valid
P4|Command tokens separate computation from generation|LLM issues structured operations instead of generating text for computation; primitives execute, LLM frames results
P5|Everything is logged and queryable|Every operational execution produces KB fact with timestamp, duration, exit code, grant, environment

# pure_primitives_summary(id|category|num|count|examples)
PP01|String operations|1|17|reverse, length, concat, slice, contains, split, join, trim, upper/lower, replace, starts/ends_with, pad, char_at, to/from_chars
PP02|List operations|2|34|length, append/prepend, concat, reverse, sort/sort_by_key, unique, flatten, zip/unzip, head/tail/last/init/nth, take/drop/slice, filter/map/reduce, any/all/count, index_of/contains, min/max, enumerate, chunk, interleave, partition, group_by, frequencies
PP03|VDR arithmetic|3|26|add/sub/mul/div/neg/abs/pow, gcd/lcm/mod, floor/ceil/round, numerator/denominator, is_integer, simplify, compare/min/max, sum/product/mean, factorial/binomial/fibonacci
PP04|Set operations|4|14|from_list/to_list, union/intersection/difference/symmetric_diff, is_subset/superset/disjoint, size/contains/add/remove, power_set
PP05|Dictionary operations|5|15|new/from_pairs, get/get_or/set/remove, contains_key, keys/values/pairs, size, merge, filter_keys/map_values/invert
PP06|Linear algebra|6|16|vec add/sub/scale/dot/norm_sq; mat add/mul/scale/transpose/det/inv/solve/rank/identity/trace/matvec
PP07|Statistics and probability|7|16|mean/variance/median/mode/percentile, normalize/is_valid/entropy_terms/cdf/expected, bayes/joint/marginal/conditional, softmax/softmax_surrogate
PP08|Conversion and formatting|8|14|to_string/number/fraction, fraction_to_decimal, format table/json/csv, parse json/csv, number_to_roman/words, format fraction/percentage/scientific
PP09|Date and time|9|10|from/to_ymd, diff/add_days, day_of_week, is_leap_year, days_in_month, from/to_hms, duration_between
PP10|Hashing and encoding|10|8|hash_string/combine, base64 encode/decode, hex encode/decode, crc32, uuid_from_seed
PP11|Graph operations|11|13|from_edges, neighbors, shortest_path (unweighted+weighted), connected_components, is_connected, topological_sort, cycle_detect, bfs/dfs, degree, mst, pagerank
PP12|Logic and control|12|11|if_then_else, case_match, for_each, repeat_n, while_loop, try_catch, assert_that, type_check, is_bound, findall, aggregate
PP13|KB and constraint operations|13|15|kb_assert/retract/query/query_in/query_across/list_facts/list_rules/active_scope/switch_topic, constraint_check/check_all/add/remove/enable/suspend
# Pattern matching (regex) removed per Addendum: unbounded computation risk (ReDoS), violates finite-termination contract
# String primitives cover majority of practical pattern matching; structured parsers (JSON, CSV) for data formats
# Total pure: 211 (after regex removal)

# operational_primitives_summary(id|category|num|count|class|examples)
OP01|Filesystem|14|15|filesystem|read/write/append, exists, list_dir/create_dir/delete/move/copy, file_size/modified, glob/tree, diff, checksum
OP02|Code compilation|15|4|compile|compile_python_check, compile_zig, compile_c, compile_rust
OP03|Script execution|16|5|execute|exec_python, exec_shell, exec_zig_test, exec_pytest, exec_script
OP04|Linting and analysis|17|8|lint|lint_python/zig/json/markdown, analyze_imports/complexity/dependencies, count_lines
OP05|Network|18|5|network|download, fetch, post, ping, dns_resolve
OP06|Process management|19|7|process|start/poll/wait/kill, stdout/stderr, list
# Total operational: 44; all require positive grant; all executions logged as KB facts

# grant_system(id|aspect|detail)
GR1|Grant structure|name, operation_class, allowed_operations, location (path/URL), credential ref, issued_by, issued_at, expires_at, max_uses, uses_remaining, constraints, status
GR2|Verification rules|grant_valid (active + not expired + uses remaining) AND grant_covers (class + operation type + location within grant path) AND grant_constraints_ok → authorize + decrement + log
GR3|Default denial|If no valid grant covers requested operation, operation rejected before execution; rejection logged with operation, location, timestamp, reason
GR4|Grant hierarchy|Grants follow KB hierarchy; user inherits grants from group/department/organization same as constraints (VDR-5 Addendum A2)
GR5|Grant lifecycle|new→active; active→expired (time), exhausted (uses=0), revoked (explicit); revocation is permanent; all transitions logged
GR6|Grant classes|filesystem (read/write/delete), compile (syntax check/build), execute (run scripts — highest risk), lint (read-only analysis), network (HTTP/DNS), process (start/kill/monitor)

# command_tokens(id|aspect|detail)
CT1|Mechanism|LLM output stream contains text tokens (rendered as conversation) and command tokens (executed by primitive system); structured invocation with primitive name, args, env, grant, store_result, await flag
CT2|Command types|PURE_FN (no grant, sync), OP_FN (grant, optional async), KB_ASSERT/RETRACT/QUERY (scoped), ENV_EXEC/UPLOAD/DOWNLOAD (grant, async recommended), CTX_ACTIVATE/DEACTIVATE/SNAPSHOT, VERSION_CREATE/TAG, STORE_RESULT, DIRECT_OUTPUT, ATTACHMENT
CT3|Output stream|Interleaves text and commands; user sees text + command outcomes; commands optionally shown/hidden per user preference (show_commands setting)
CT4|Scratchpad|Internal channel for intermediate computation; LLM issues pure primitive calls and KB queries without surfacing in user output; owner can inspect via /show scratchpad
CT5|Ordering rules|Scratchpad before output; text frames data; commands in causal order (upload before execute); notifications at end; attachments at end

# environments(id|aspect|detail)
EN1|Types|Docker (strong isolation, default sandbox), VM (strongest isolation, untrusted code), Local (no isolation, trusted dev), SSH (remote, GPU servers)
EN2|Unified interface|All 4 types implement same 10 operations: env_exec, env_upload, env_download, env_shell, env_file_read/write, env_list_dir, env_proc_start/poll/output
EN3|Environment as KB|Each env has own KB tracking: type, image, status, installed packages, execution log (every command), uploaded files, active tasks
EN4|Lifecycle|create (KB created) → start (container/VM launching) → running (startup script executed) → stop (graceful shutdown) → destroy (container removed, KB archived)
EN5|Resource limits|max_cpu_seconds, max_memory_mb, max_disk_mb, max_network_bytes, max_processes — all configurable per environment

# async_tasks(id|aspect|detail)
AT1|Task structure|id, operation, args, env, grant, status (pending/running/completed/failed/killed), timestamps, result, output_chunks, topic, notify_on_complete, acknowledged
AT2|Lifecycle|submitted→pending→running→completed/failed/killed; output captured in chunks as it arrives
AT3|Turn-based notification|On each turn, check for completed tasks in active topic; surface at end of response; user can acknowledge, view full results, or ignore
AT4|Chunked I/O|Output chunks processed as they arrive: classify (stdout/stderr/progress/error), check against watches, check constraints, store in task KB
AT5|Streaming vs polling|Streaming (/watch task_id) shows live output interleaved with conversation; polling (default) shows summary on next turn after completion

# versioning(id|aspect|detail)
VR1|Version as KB fact|project, artifact, version_num, content_ref, timestamps, created_by, parent_version, tags, test_result, notes
VR2|Operations|VERSION_CREATE (new version), VERSION_TAG (add tag), KB_QUERY (retrieve), PURE_FN(diff) (compare), rollback (create new with old content)
VR3|Queryable|Which versions had all tests passing? Which artifacts have latest with failures? Which versions tagged "release"? Full diff chain from latest to v1

# direct_download(id|aspect|detail)
DD1|Principle|If data exists at known address (KB fact, file, task output, checkpoint), user downloads directly without LLM regenerating as tokens; data served from source
DD2|Address schemes|kb:// (facts), wd:// (working data), fs:// (env files), task:// (stdout/stderr/result), ckpt:// (checkpoints), ver:// (versions), diff:// (computed diffs), export:// (KB export), ctx:// (snapshots), log:// (execution logs)
DD3|Authorization|KB resources governed by KB visibility; file resources require filesystem read grant; both KB access and appropriate grant needed for env files
DD4|LLM-initiated|LLM can issue DIRECT_OUTPUT to serve KB data or ATTACHMENT to serve files; data block is retrieved not generated — cannot hallucinate

# primitive_invariants(id|primitive|invariant|type)
PI1|list_sort|output length = input length; output sorted; output is permutation of input|axiom
PI2|vdr_add|commutative: a+b = b+a; associative: (a+b)+c = a+(b+c)|axiom
PI3|prob_normalize|output sums to exactly 1|axiom
PI4|softmax|output sums to exactly 1; preserves input ordering; all outputs positive|axiom
PI5|mat_inv|M * inv(M) = identity|axiom
PI6|fs_read/write|write then read returns written content|operational
PI7|compile|success implies output file exists|operational

# regex_removal(id|detail)
RR1|Category 12 (Pattern Matching, 7 primitives) removed from specification
RR2|Rationale: regex allows catastrophic backtracking (ReDoS); violates finite-termination contract for pure primitives; determining worst-case behavior is itself computationally hard
RR3|Replacement: string primitives (contains, split, starts/ends_with, replace) cover majority of needs; structured parsers (parse_json, parse_csv) for data formats
RR4|If regex needed future: must be operational primitive (not pure) with CPU time limit, positive grant required

# revised_counts(id|metric|value)
RC1|Pure primitives|211 (218 minus 7 regex)
RC2|Pure categories|13 (14 minus pattern matching)
RC3|Operational primitives|44
RC4|Operational categories|6
RC5|Total primitives|255
RC6|Total categories|19
RC7|New modules specified|3 (primitives.py, operational.py, command.py)
RC8|Total system modules|30 (24 existing + 3 VDR-5 + 3 VDR-6)

# implementation_priority(id|phase|component|dependencies|effort)
IP1|1|Pure primitives categories 1-5 (string, list, arithmetic, set, dict)|VDR core|Medium total
IP2|2|KB/constraint primitives (category 13)|VDR-Prolog KB from VDR-5|Medium
IP3|3|Command token parser and executor|Primitives from phases 1-2|Medium
IP4|4|Docker environment manager|Docker API|Medium
IP5|5|Filesystem operational primitives|Docker env|Low
IP6|6|Execution and compilation primitives|Docker env|Low
IP7|7|Async task manager|Environment from phase 4|Medium
IP8|8|Grant and credential system|KB from VDR-5|Medium
IP9|9|Versioning system|KB from VDR-5|Low
IP10|10|Direct download serving|KB + environments|Low
IP11|11|Pure primitives categories 6-13|VDR core|Medium total
IP12|12|Network and process primitives|Environment|Low
IP13|13|Scratchpad and notification system|Task manager|Medium
IP14|14|Integration testing|All above|High

# falsification_criteria(id|criterion|test_method)
FC1|Pure primitive incorrect result|Invariant constraints enable automatic detection on every invocation
FC2|Operational primitive executes without valid grant|Authorization bypass vulnerability
FC3|Command token executed without KB log|Audit trail incomplete
FC4|Task result in KB differs from actual process output|Result capture mechanism bug
FC5|Direct download content differs from source data|Serving corruption bug
FC6|VERSION_CREATE content not retrievable by subsequent query|Versioning storage/retrieval bug
FC7|Docker operation affects host filesystem outside container mount|Isolation broken

# claims(id|claim|type)
CL1|LLM should not compute — primitives should|design_thesis
CL2|216 pure primitives are always available, always correct, always terminate|specification (revised to 211 after regex removal)
CL3|44 operational primitives are always authorized, always logged, always auditable|specification
CL4|Command tokens separate what LLM does well (language) from what primitives do well (computation)|structural
CL5|Positive credential gating with default denial prevents unauthorized side effects|security
CL6|Environments provide sandboxed execution with unified interface|operational
CL7|Direct data download bypasses LLM token generation, preventing hallucination of retrieved data|structural

# relationships(from|rel|to)
P1|governs|entire system design
P2|constrains|PP01-PP13 (all pure primitives)
P3|constrains|OP01-OP06 (all operational primitives)
P4|implemented_by|CT1-CT5
P5|implemented_by|execution logging
GR1|gates|OP01-OP06
GR4|uses|VDR-5 Addendum A2 KB hierarchy
CT1|invokes|PP01-PP13,OP01-OP06
CT4|uses|PP01-PP13 for internal computation
EN2|abstracts|EN1 (4 environment types into 1 interface)
EN3|stores_in|VDR-5 KB system
AT3|uses|VDR-5 topic system
VR1|stores_in|VDR-5 KB system
DD1|bypasses|LLM token generation
DD3|uses|GR1 (grant system) + VDR-5 KB visibility
RR1|removes|regex primitives from pure category
RR3|replaced_by|PP01 (string operations) + PP08 (parse_json, parse_csv)
PI1-PI7|verifiable_by|VDR-5 constraint system

# section_index(section|title|ids)
1|Why an Execution Layer|P1
2|Pure Primitives|PP01-PP13,P2,PI1-PI7
3|Operational Primitives|OP01-OP06,P3
4|Positive Credential Grant System|GR1-GR6
5|Command Tokens|CT1-CT5
6|Operational Environments|EN1-EN5
7|Async Task Management|AT1-AT5
8|Direct Data Download|DD1-DD4
9|Versioning|VR1-VR3
10|Integration Example|complete flow: write→upload→execute→poll→store→version
11|Primitive Constraint Invariants|PI1-PI7
12|Execution Logging and Audit|P5
13|Complete Primitive Count|RC1-RC8
14|Falsification Criteria|FC1-FC7
15|Implementation Priority|IP1-IP14
16|Conclusion|CL1-CL7
A1|Regex Removal Addendum|RR1-RR4
A|Complete Primitive Index|PP01-PP13,OP01-OP06
B|Command Token Reference|CT2 expanded
C|Grant Class Reference|GR6 expanded
D|Paper Series|cumulative
E|Environment Configuration|EN1-EN5 expanded
F|Task State Machine|AT1-AT5 expanded
G|Direct Download Address Formats|DD2 expanded
H|Version Management|VR1-VR3 expanded
I|Scratchpad Reference|CT4 expanded
J|Reminder and Watch Reference|from VDR-5 integration
K|Fat Struct KB Entry|all fields per entry type
L|Provenance Weight Propagation|weight assignment and propagation rules
M|Data Weight Management|training data weighting operations
N|Chunked I/O Processing|AT4 expanded
O|Context Assembly|context components and size management
P|Output Stream Token Classification|CT3 expanded
Q|Cross-Paper Integration|how VDR-6 maps to VDR-1 through VDR-5
R|Implementation Test Plan|648 pure + 132 operational + 30+ integration tests planned
S|Cumulative System Statistics|30 modules, 705 existing tests + ~810 planned, 255 primitives

# decode_legend
primitive_types: pure (no side effects, no grant) | operational (side effects, grant required)
grant_statuses: active | expired | exhausted | revoked
command_token_types: PURE_FN | OP_FN | KB_ASSERT | KB_RETRACT | KB_QUERY | ENV_EXEC | ENV_UPLOAD | ENV_DOWNLOAD | CTX_ACTIVATE | CTX_DEACTIVATE | CTX_SNAPSHOT | VERSION_CREATE | VERSION_TAG | STORE_RESULT | DIRECT_OUTPUT | ATTACHMENT
environment_types: docker | vm | local | ssh_remote
task_statuses: pending | running | completed | failed | killed
address_schemes: kb:// | wd:// | fs:// | task:// | ckpt:// | ver:// | diff:// | export:// | ctx:// | log://
invariant_types: axiom (mathematical, never violated) | operational (holds under normal conditions)
claim_types: design_thesis | specification | structural | security | operational
rel_types: governs | constrains | implemented_by | gates | uses | invokes | abstracts | stores_in | bypasses | removes | replaced_by | verifiable_by
revised_totals: 211 pure + 44 operational = 255 primitives across 19 categories; 30 modules total
