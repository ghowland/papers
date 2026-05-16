# COMPUTATIONAL STATE PRIMITIVES, UNIVERSAL DATA PATHING, AND SESSION MANAGEMENT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → data primitives → dotted paths → command tokens → sessions → revised KB struct → relationships → sections

# principles(id|principle|rationale)
P1|Data primitives belong in the KB struct|Same pattern as constraints-in-KB (VDR-5 addendum); the thing being described holds its own description
P2|Dotted path is human API; integer ID is machine API|Both coexist; LLM and users work with paths, runtime works with integers for O(1) access
P3|Command tokens are reference selection not text generation|LLM picks primitive name from known vocabulary + points at data by dotted path; generative burden is minimal
P4|Live state is capturable, restorable, cloneable, disposable|Session snapshots capture working memory atomically; clones fork independent copies; drift triggers recycling
P5|Three capabilities depend on each other|Data primitives create state worth snapshotting; dotted paths give snapshots efficient references; session management provides lifecycle for drift-prone state

# data_primitives(id|type|description|capacity_range|key_operations)
DP1|LRU cache|Named bounded least-recently-used cache; multiple channels for separate concerns|1-1000|create, push, get, peek, contains, size, clear, evict
DP2|Counter|Named exact i32 counter with min/max bounds; clamps at bounds, no wraparound|min/max i32|create, inc, dec, add, get, reset, set
DP3|Lock|Named non-blocking flag; acquire/check/release; coordination signal, never blocks|single state|create, acquire, release, check, holder, force_release
DP4|Queue|Named bounded FIFO; push to back, pop from front; push returns false if full|1-1000|create, push, pop, peek, size, is_empty, is_full, clear, to_list
DP5|Stack|Named bounded LIFO; push to top, pop from top; push returns false if full|1-1000|create, push, pop, peek, size, is_empty, clear, to_list
DP6|Ring buffer|Named fixed-size circular buffer; write overwrites oldest when full|1-1000|create, write, read_all, read_last, size, clear
DP7|Bitset|Named fixed-size bit array; track completion of numbered items, feature flags|1-10000|create, set, clear_bit, test, count, all_set, any_set, reset, to_list

# data_primitive_classification(id|aspect|detail)
DC1|Classification|Data primitives are live state, not persistent knowledge
DC2|Persistent|Facts, rules, constraints, connections — survives reset, not captured by snapshot (always present)
DC3|Live|Data primitives, scratchpad, working data, active scope — cleared by reset, captured by snapshot
DC4|Growth limits|Every primitive has declared maximum capacity at creation; no unbounded growth
DC5|Mutation logging|All mutations logged as provenance facts: kb_path, primitive_type, name, operation, old_value, new_value, turn, source
DC6|Inheritance|Data primitives inherit by name through KB tree like working data bindings; child values shadow parent values; lookup walks current KB to root, first match wins
DC7|Scratchpad formalized|Scratchpad is a ring buffer on root.sessions.active.scratchpad; auto-created on session start, auto-written by command executor

# dotted_paths(id|aspect|detail)
DP_PATH1|Structure|root.segment.segment... where each dot-separated segment names one level; parent-child encoded in path
DP_PATH2|Segment rules|Lowercase alphanumeric + underscore; no trailing dot; no empty segments; max depth 16; max segment length 64
DP_PATH3|Integer ID registry|HashMap path→i32 and array i32→path; IDs assigned sequentially on KB creation; never reused after deletion; stable across sessions
DP_PATH4|Runtime access|All internal operations use integer IDs; scope chains become i32 arrays; walking scope = iterating short array, no string parsing
DP_PATH5|Slot IDs|Data primitive names within KB also receive i32 slot IDs; full access is two integers: kb_id + slot_id → O(1)
DP_PATH6|Resolution|LLM emits dotted paths in command tokens; executor resolves to integer ID once; downstream operations use integer; resolution cached per turn
DP_PATH7|Relative addressing|.name (child), .. (parent), ..name (sibling), @root, @self, @mount.name; resolved to absolute before ID lookup; convenience only, never stored

# mounts(id|aspect|detail)
MT1|Mechanism|KB from one branch appears at path in another branch; resolves to source KB's integer ID
MT2|Modes|read_only (live, no writes), read_write (live, requires grant), snapshot (frozen at mount time), mirror (live automatic sync, no writes)
MT3|Cycle detection|Before creating mount, trace source's mount chain; reject if mount_path appears anywhere in chain
MT4|Connections|Mount creates a connection of relationship "mounted_from" on the mount point KB
MT5|Scope impact|When mount point is in active scope chain, queries resolve through mount to source KB

# connections(id|aspect|detail)
CN1|Structure|target_id (i32), target_path (Text), relationship (Text), direction (inbound/outbound), phase, created_at, notes
CN2|Location|Each KB holds its own connections list as a field on the struct; connections travel with KB on export
CN3|Graph operations|VDR-6 graph primitives operate on collected connections using integer IDs as nodes; topology queries (reachability, shortest path, components) are standard graph operations
CN4|Standard relationships|sourced_from, tokenized_into, trained_from, checkpointed_at, finetuned_from, feedback_for, aligned_by, evaluated_by, deployed_as, monitored_by, updated_by, superseded_by, retired_as, references, mounted_from, cloned_from

# compact_command_tokens(id|aspect|detail)
CC1|Reference selection|255 primitives + data primitive ops are facts in root KB (always in scope); LLM selects reference from known finite vocabulary, not generating novel syntax
CC2|Arguments are addresses|For data in KB, command passes dotted-path reference, not value through token stream; data stays in KB, primitive reads directly via integer ID
CC3|Token structure revised|CommandToken: type, primitive_id (i32), args ([]CommandArg where CommandArg = path_ref | literal_i32 | literal_text | literal_bool | literal_fraction), store_result (?path), await
CC4|Size comparison|Freeform JSON ~30 tokens; standard function calling ~15 tokens; VDR-8 reference-based ~8 tokens; post-resolution ~5 integer values
CC5|Reliability|Low-entropy task (select from 300 known names + point at known paths) vs high-entropy task (generate novel syntax); components are validated references not generated text

# session_management(id|aspect|detail)
SM1|Snapshot structure|Captures all live state atomically: active_scope ([]i32), active_topic (i32), secondary_scopes, scratchpad (ring buffer), all KB live states (counters, locks, LRUs, queues, stacks, buffers, bitsets, working_data per KB), turn_count, total_commands
SM2|Core operations|session_snapshot (capture), session_restore (restore), session_reset (clear all live to defaults), session_clone (fork independent copy), session_kill (destroy clone), session_list, session_diff, session_info
SM3|Snapshot is small|Captures state not knowledge; typical 10KB-100KB; even 100 active KBs with 1500 primitives → under 500KB
SM4|Reset semantics|Counters→min_value, locks→released, queues/stacks/LRUs/rings→empty, bitsets→cleared, scratchpad→cleared; persistent KB contents untouched
SM5|Clone isolation|Clones share persistent KBs (facts, rules, constraints, connections); each clone has independent live state (counters, locks, caches, queues, stacks, buffers, bitsets, working data, scratchpad)
SM6|Work preservation|When clone killed, only live state destroyed; any KB_ASSERT commits to persistent KBs survive; work product persists, working memory discarded

# disposable_clones(id|aspect|detail)
CL1|Pattern|Build session to verified stable state → snapshot → run disposable workers from snapshot → kill on drift → launch fresh from same frozen baseline
CL2|Drift constraints|max_session_turns (<200), context_saturation (<90%), denominator_drift (<2^48), error_rate (<5%); when any fires → kill_and_reclone
CL3|Snapshot is factory|Snapshot never degrades (frozen state); clones are disposable workers; the work persists in persistent KBs, the drift dies with the clone
CL4|Versioned operators|Stable operator snapshots can be versioned (v1, v2...); roll back to earlier version if later one has problems; mirrors checkpoint lineage from VDR-7

# revised_kb_struct(id|field|source|type|classification)
KB01|name|VDR-5|Text|Identity
KB02|path|VDR-8|Text|Identity
KB03|id|VDR-8|i32|Identity
KB04|facts|VDR-5|FactSet|Persistent
KB05|rules|VDR-5|RuleSet|Persistent
KB06|constraints|VDR-5 addendum|[]Constraint|Persistent
KB07|connections|VDR-8|[]Connection|Persistent
KB08|working_data|VDR-5|?WorkingDataSet|Live
KB09|lrus|VDR-8|HashMap(Text,LRU)|Live
KB10|counters|VDR-8|HashMap(Text,Counter)|Live
KB11|locks|VDR-8|HashMap(Text,LockState)|Live
KB12|queues|VDR-8|HashMap(Text,BoundedQueue)|Live
KB13|stacks|VDR-8|HashMap(Text,BoundedStack)|Live
KB14|buffers|VDR-8|HashMap(Text,RingBuffer)|Live
KB15|bitsets|VDR-8|HashMap(Text,Bitset)|Live
KB16|parent_id|VDR-5/8|?i32|Structural
KB17|children_ids|VDR-5/8|[]i32|Structural
KB18|mounts|VDR-8|[]Mount|Structural
KB19|visibility|VDR-5|enum(public,internal,owner_only)|Metadata
KB20|frozen|VDR-5|bool|Metadata
KB21|owner|VDR-5 addendum|?Text|Metadata
KB22|created_at|VDR-5|i32|Metadata
KB23|last_modified|VDR-5|i32|Metadata
# 23 fields total: 5 persistent, 8 live, 3 structural (identity), 2 structural (tree), 5 metadata

# new_primitives(id|category|count|type|examples)
NP1|Data primitive operations|53|Pure|lru_create/push/get/peek/contains/size/clear/evict (8), counter_create/inc/dec/add/get/reset/set (7), lock_create/acquire/release/check/holder/force_release (6), queue_create/push/pop/peek/size/is_empty/is_full/clear/to_list (9), stack_create/push/pop/peek/size/is_empty/clear/to_list (8), ring_create/write/read_all/read_last/size/clear (6), bitset_create/set/clear_bit/test/count/all_set/any_set/reset/to_list (9)
NP2|Path and mount operations|17|Pure|path_resolve/from_id/parent/children/ancestors/depth/exists/common_ancestor (8), kb_mount/unmount/mount_info/list_mounts (4), connection_add/remove/list/query/graph (5)
NP3|Session management|8|Pure|session_snapshot/restore/reset/clone/kill/list/diff/info

# revised_primitive_counts(id|source|pure|operational|total)
RC1|VDR-6 (post regex removal)|211|44|255
RC2|VDR-8 data primitives|53|0|53
RC3|VDR-8 path and mount|17|0|17
RC4|VDR-8 session management|8|0|8
RC5|Combined total|289|44|333

# new_modules(id|module|purpose)
NM1|data_primitives.py|LRU, counter, lock, queue, stack, ring buffer, bitset implementations
NM2|pathing.py|Dotted-path registry, integer ID assignment, mount system, connection operations
NM3|sessions.py|Snapshot capture, restore, reset, clone, kill, diff
# 34 existing + 3 new = 37 total modules

# falsification_criteria(id|criterion|test_method)
FC1|Data primitive non-determinism|Replay same operation sequence, compare state
FC2|Snapshot lossiness|Snapshot, modify, restore, compare every live state field
FC3|Clone persistent visibility|Assert fact in clone A, query from clone B
FC4|Clone live isolation|Modify live state in clone A, verify clone B and snapshot unchanged
FC5|Path registry inconsistency|Record path→ID mappings, restart, verify
FC6|Mount mode violation|Attempt write through read-only mount
FC7|Growth bound violation|Fill to capacity, add one more
FC8|Export incompleteness|Export KB, import to fresh system, compare all fields including connections and data primitives
FC9|Mount cycle creation|Attempt A→B→A mount chain
FC10|Path cache inconsistency|Compare cached vs fresh resolution of same path

# claims(id|claim|type)
CL1|Data primitives give LLM structured working memory adapted to turn-based execution|structural
CL2|Dotted paths with integer acceleration provide O(1) runtime access to any KB or data primitive|performance
CL3|Command tokens as reference assemblies reduce generative burden 2-4× vs standard function calling|reliability
CL4|Session snapshots are small (10KB-500KB) because they capture state not knowledge|efficiency
CL5|Disposable clone pattern maintains system stability through controlled recycling|operational
CL6|Work product persists in persistent KBs while drift dies with the clone|architectural
CL7|Everything is a KB — sessions, snapshots, paths, mounts stored as KBs in the tree|consistency

# relationships(from|rel|to)
P1|follows_pattern_of|VDR-5 addendum (constraints-in-KB)
P2|enables|CC1-CC5 (efficient command tokens)
P3|depends_on|DP_PATH1-DP_PATH7 (paths give references to select)
P4|depends_on|DP1-DP7 (data primitives create state worth snapshotting)
P5|states|mutual dependency of three capabilities
DP1-DP7|stored_in|KB struct (KB09-KB15)
DP1-DP7|classified_as|DC3 (live state)
DP1-DP7|inherit_through|KB tree like working data
DP_PATH3|provides|O(1) access for runtime
DP_PATH5|provides|two-integer addressing for data primitives
MT1|extends|VDR-5 scope resolution
MT3|prevents|circular mount references
CN1-CN4|enables|VDR-6 graph primitives on KB topology
CC1|uses|root KB primitive vocabulary (always in scope)
CC2|avoids|serializing data through token stream
SM1|captures|DC3 (all live state)
SM5|shares|DC2 (persistent knowledge) between clones
SM6|preserves|work committed via KB_ASSERT
CL1-CL7|build_on|VDR-5 through VDR-7 foundations
DC7|formalizes|VDR-6 scratchpad as ring buffer

# section_index(section|title|ids)
1|Context: VDR-LLM-Prolog System|system recap
2|The Problem|no structured working memory, no structured addressing, no session state management, problems interact
3|Runtime Data Primitives|DP1-DP7,DC1-DC7
4|Universal Dotted-Path Addressing|DP_PATH1-DP_PATH7
5|Compact Command Token Construction|CC1-CC5
6|Session Management|SM1-SM6,CL1-CL4
7|Revised KB Struct|KB01-KB23
8|Primitive Additions|NP1-NP3,RC1-RC5
9|Constraint Integration|data primitive constraints, session constraints, path constraints
10|Integration Examples|LRU-tracked error recovery, queue-managed work, lock-coordinated ops, session snapshot/clone, cross-branch mount, bitset gym tracking
11|Falsification Criteria|FC1-FC10
12|Implementation Priority|17 phases from path registry through integration testing
13|Conclusion|CL1-CL7
A|Data Primitive Specifications|DP1-DP7 detailed (capacity, types, edge cases)
B|Dotted-Path Grammar|formal grammar + validation rules
C|Mount System Reference|modes, cycle detection, permission requirements
D|Session Management Reference|snapshot contents, operation semantics, clone isolation, disposable lifecycle
E|Command Token Resolution|6-stage pipeline, cache spec, size comparison
F|Cumulative Statistics|37 modules, 333 primitives, ~1926 planned tests, 23 KB struct fields
G|Data Primitive Interaction Patterns|8 multi-primitive coordination patterns, cross-reference by KB type
H|Integer ID Allocation|assignment rules, slot IDs, capacity estimates
I|Relative Addressing|operators (.name, .., @root, @self), wildcards (*, **)
J|Connection Relationship Taxonomy|19 standard types, constraint patterns, graph queries
K|Mount Use Cases|7 patterns, permission requirements, scope impact
L|Session Snapshot Size Estimates|per-primitive sizes, session complexity tiers, operation timing
M|Clone Drift Detection|8 indicators with healthy/warning/kill thresholds, response actions, lifecycle metrics
N|Command Token Error Handling|8 validation stages, error fact structure, error rate constraints
O|Mutation Log Reference|event types per primitive, retention policy, query patterns
P|Scratchpad Specification|ring buffer formalization, relationship to other primitives
Q|Working Data Reclassification|live state classification, reset modes, promotion path (live→persistent)
R|Scope Resolution with Mounts|full algorithm, examples
S|Data Primitive Test Plan|129 tests across 7 primitives with edge cases and invariant tests
T|Cross-Paper Traceability|VDR-8 features traced to prior foundations + enrichments to prior specs

# decode_legend
data_primitive_types: LRU | counter | lock | queue | stack | ring_buffer | bitset
state_classification: persistent (survives reset, always present) | live (cleared by reset, captured by snapshot)
mount_modes: read_only | read_write | snapshot | mirror
path_format: root.segment.segment... (lowercase alphanumeric + underscore, max depth 16)
addressing: dotted path (human) + integer ID (machine) + slot ID (within-KB primitive)
session_operations: snapshot | restore | reset | clone | kill | list | diff | info
clone_isolation: live state independent per clone; persistent KBs shared
command_arg_types: path_ref | literal_i32 | literal_text | literal_bool | literal_fraction
relative_path_operators: .name (child) | .. (parent) | ..name (sibling) | @root | @self | @mount.name
connection_directions: inbound | outbound
claim_types: structural | performance | reliability | efficiency | operational | architectural | consistency
rel_types: follows_pattern_of | enables | depends_on | states | stored_in | classified_as | inherit_through | provides | extends | prevents | uses | avoids | captures | shares | preserves | build_on | formalizes
revised_totals: 289 pure + 44 operational = 333 primitives; 37 modules; 23 KB struct fields; ~1926 planned tests
