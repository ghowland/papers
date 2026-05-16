# VDR-LLM-Prolog Implementation — Function IOSE Specification
## Five Stages: Data Structures and Function Interfaces

---

## Shared Data Structures (All Stages)

### Enums

```python
class RemainderForm(Enum):
    ZERO = "zero"
    ATOMIC = "atomic"
    COMPOSITE = "composite"
    FUNCTIONAL = "functional"

class Visibility(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    OWNER_ONLY = "owner_only"

class MountMode(Enum):
    READ_ONLY = "read_only"
    READ_WRITE = "read_write"
    SNAPSHOT = "snapshot"
    MIRROR = "mirror"

class Direction(Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

class IOSECategory(Enum):
    PURE = "pure"
    OPERATIONAL = "operational"
    COMPOSITE = "composite"

class LogicType(Enum):
    OPERATIONAL = "operational"
    APPLICATION = "application"

class CommandType(Enum):
    PURE_FN = "pure_fn"
    OP_FN = "op_fn"
    KB_ASSERT = "kb_assert"
    KB_RETRACT = "kb_retract"
    KB_QUERY = "kb_query"
    ENV_EXEC = "env_exec"
    ENV_UPLOAD = "env_upload"
    ENV_DOWNLOAD = "env_download"
    CTX_ACTIVATE = "ctx_activate"
    CTX_DEACTIVATE = "ctx_deactivate"
    CTX_SNAPSHOT = "ctx_snapshot"
    VERSION_CREATE = "version_create"
    STORE_RESULT = "store_result"
    DIRECT_OUTPUT = "direct_output"
    ATTACHMENT = "attachment"

class ArgType(Enum):
    PATH_REF = "path_ref"
    LITERAL_INT = "literal_int"
    LITERAL_TEXT = "literal_text"
    LITERAL_BOOL = "literal_bool"
    LITERAL_FRACTION = "literal_fraction"

class InferenceMode(Enum):
    DEDUCTIVE = "deductive"
    INDUCTIVE = "inductive"
    ABDUCTIVE = "abductive"
    ANALOGICAL = "analogical"

class NotebookStatus(Enum):
    ACTIVE = "active"
    CONCLUDED = "concluded"
    HALTED = "halted"
    ARCHIVED = "archived"

class LoopPhase(Enum):
    ASSESS = "assess"
    FORMALIZE = "formalize"
    EXECUTE = "execute"
    STORE = "store"
    BRANCH = "branch"
    BACKTRACK = "backtrack"
    CONCLUDE = "conclude"
    HALT = "halt"

class GrantStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    EXHAUSTED = "exhausted"

class EnvType(Enum):
    LOCAL = "local"
    DOCKER = "docker"
    SSH = "ssh"
    VM = "vm"

class EnvStatus(Enum):
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    ERROR = "error"

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    KILLED = "killed"
```

### Core Value Types

```python
@dataclass
class VDRFraction:
    v: int
    d: int
    r: Any = 0  # 0, int, CompositeRemainder, or FnRemainder

@dataclass
class CompositeRemainder:
    base: int
    children: List['VDRFraction'] = field(default_factory=list)

@dataclass
class FnRemainder:
    name: str
    fn: Callable[[int], 'VDRFraction']
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class QBasis:
    numerator: int
    exponent: int

@dataclass
class Vec:
    elements: List[VDRFraction]

@dataclass
class Mat:
    rows: List[Vec]
```

### KB Structures

```python
@dataclass
class Fact:
    predicate: str
    args: List[Any]
    kb_source: str = ""
    asserted_at: int = 0
    derivation: Optional[Dict] = None

@dataclass
class Rule:
    head: Fact
    body: List[Fact]
    kb_source: str = ""

@dataclass
class Constraint:
    name: str
    scope: str = "operational"
    status: str = "active"
    condition: str = ""
    on_violation: str = "warn"
    source: str = ""

@dataclass
class Connection:
    target_id: int
    target_path: str
    relationship: str
    direction: Direction
    phase: str = ""
    created_at: int = 0
    notes: str = ""

@dataclass
class Mount:
    mount_path: str
    source_path: str
    source_id: int = 0
    mode: MountMode = MountMode.READ_ONLY
    created_at: int = 0
    created_by: str = ""
```

### Data Primitives

```python
@dataclass
class Counter:
    value: int = 0
    min_value: int = 0
    max_value: int = 2**31 - 1
    created_at: int = 0

@dataclass
class LockState:
    held: bool = False
    holder: Optional[str] = None
    acquired_at: Optional[int] = None
    notes: str = ""

@dataclass
class BoundedQueue:
    capacity: int = 50
    items: List[Any] = field(default_factory=list)
    created_at: int = 0

@dataclass
class BoundedStack:
    capacity: int = 30
    items: List[Any] = field(default_factory=list)
    created_at: int = 0

@dataclass
class RingBuffer:
    capacity: int = 100
    items: List[Any] = field(default_factory=list)
    write_pos: int = 0
    count: int = 0
    created_at: int = 0

@dataclass
class LRUCache:
    capacity: int = 50
    entries: Dict[str, Any] = field(default_factory=dict)
    access_order: List[str] = field(default_factory=list)
    created_at: int = 0

@dataclass
class Bitset:
    width: int = 100
    bits: List[bool] = field(default_factory=list)
    created_at: int = 0
```

### The KB Struct

```python
@dataclass
class KnowledgeBase:
    name: str
    path: str
    id: int
    facts: List[Fact] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)
    working_data: Dict[str, Any] = field(default_factory=dict)
    lrus: Dict[str, LRUCache] = field(default_factory=dict)
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)
    queues: Dict[str, BoundedQueue] = field(default_factory=dict)
    stacks: Dict[str, BoundedStack] = field(default_factory=dict)
    buffers: Dict[str, RingBuffer] = field(default_factory=dict)
    bitsets: Dict[str, Bitset] = field(default_factory=dict)
    parent_id: Optional[int] = None
    children_ids: List[int] = field(default_factory=list)
    mounts: List[Mount] = field(default_factory=list)
    visibility: Visibility = Visibility.PUBLIC
    frozen: bool = False
    owner: Optional[str] = None
    created_at: int = 0
    last_modified: int = 0
```

### IOSE Infrastructure

```python
@dataclass
class IOSEProperty:
    name: str
    value: Any = True

@dataclass
class IOSEDeclaration:
    name: str
    inputs: List[str]
    outputs: List[str]
    side_effects: List[str]
    properties: List[IOSEProperty] = field(default_factory=list)
    category: IOSECategory = IOSECategory.PURE
    logic_type: LogicType = LogicType.OPERATIONAL
    description: str = ""

@dataclass
class BuiltinDef:
    id: int
    name: str
    category: str
    iose: IOSEDeclaration
    implementation: Callable
```

### Command Token Structures

```python
@dataclass
class CommandArg:
    arg_type: ArgType
    value: Any

@dataclass
class CommandToken:
    cmd_type: CommandType
    primitive_name: str = ""
    args: List[CommandArg] = field(default_factory=list)
    env: str = ""
    grant: str = ""
    store_result: str = ""
    await_result: bool = False
```

### Session Structures

```python
@dataclass
class KBLiveState:
    kb_id: int
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)
    lrus: Dict[str, LRUCache] = field(default_factory=dict)
    queues: Dict[str, BoundedQueue] = field(default_factory=dict)
    stacks: Dict[str, BoundedStack] = field(default_factory=dict)
    buffers: Dict[str, RingBuffer] = field(default_factory=dict)
    bitsets: Dict[str, Bitset] = field(default_factory=dict)
    working_data: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SessionSnapshot:
    name: str
    path: str
    created_at: int = 0
    active_scope: List[int] = field(default_factory=list)
    active_topic: int = 0
    scratchpad: Optional[RingBuffer] = None
    kb_states: Dict[int, KBLiveState] = field(default_factory=dict)
    turn_count: int = 0
    notes: str = ""
```

### Inference Structures

```python
@dataclass
class InferenceConclusion:
    statement: Fact
    mode: InferenceMode
    confidence: VDRFraction
    derived_from: List[str] = field(default_factory=list)
    via_rules: List[str] = field(default_factory=list)
    via_tools: List[str] = field(default_factory=list)
    alternatives: List[Dict] = field(default_factory=list)
    steps_taken: int = 0
    backtracks: int = 0

@dataclass
class InferenceNotebook:
    kb: KnowledgeBase
    problem_statement: str = ""
    mode: InferenceMode = InferenceMode.ABDUCTIVE
    goal: str = ""
    status: NotebookStatus = NotebookStatus.ACTIVE
    conclusion: Optional[InferenceConclusion] = None
    max_steps: int = 50
    max_queries: int = 20
    stall_threshold: int = 5
```

### Environment and Grant Structures

```python
@dataclass
class ResourceLimits:
    max_cpu_seconds: int = 3600
    max_memory_mb: int = 2048
    max_disk_mb: int = 10240
    max_processes: int = 100

@dataclass
class OperationalEnv:
    id: str
    env_type: EnvType
    status: EnvStatus = EnvStatus.STOPPED
    working_dir: str = "/workspace"
    env_vars: Dict[str, str] = field(default_factory=dict)
    resource_limits: ResourceLimits = field(default_factory=ResourceLimits)
    kb_path: str = ""
    docker_image: str = ""
    ssh_host: str = ""
    ssh_port: int = 22
    ssh_user: str = ""

@dataclass
class Grant:
    name: str
    operation_class: str
    allowed_operations: List[str]
    location: str
    issued_by: str = ""
    issued_at: int = 0
    expires_at: int = 2**31 - 1
    max_uses: int = 0
    uses_remaining: int = 0
    status: GrantStatus = GrantStatus.ACTIVE

@dataclass
class Task:
    id: str
    operation: str
    args: List[Any]
    env: str
    grant: str
    status: TaskStatus = TaskStatus.PENDING
    submitted_at: int = 0
    completed_at: int = 0
    result: Any = None
    stdout: str = ""
    stderr: str = ""

@dataclass
class ExecResult:
    exit_code: int
    stdout: str
    stderr: str
    duration_ms: int = 0
```

---

## Stage 1: Toy Full Lifecycle

### core/types.py

#### promote_integer
**Purpose:** Convert Python int to VDRFraction. Lossless. The fundamental upward conversion.

**Inputs:** value (int).

**Outputs:** VDRFraction with v=value, d=1, r=0.

**Side effects:** None. Pure conversion.

#### promote_qbasis
**Purpose:** Convert QBasis to VDRFraction. Lossless.

**Inputs:** qb (QBasis).

**Outputs:** VDRFraction with v=qb.numerator, d=2**qb.exponent, r=0.

**Side effects:** None. Pure conversion.

#### dispatch_arithmetic
**Purpose:** Determine which arithmetic path to use based on operand types. Returns a tag indicating integer fast path, VDR path, or Q-basis path. Promotes operands as needed.

**Inputs:** left (Any numeric), right (Any numeric), operation (str).

**Outputs:** Tuple of (path_tag: str, promoted_left: VDRFraction, promoted_right: VDRFraction).

**Side effects:** None. Pure dispatch.

#### is_closed
**Purpose:** Test if a VDRFraction has zero remainder.

**Inputs:** frac (VDRFraction).

**Outputs:** bool.

**Side effects:** None.

#### is_integer
**Purpose:** Test if a VDRFraction has d=1 and r=0.

**Inputs:** frac (VDRFraction).

**Outputs:** bool.

**Side effects:** None.

---

### core/errors.py

#### VDRError (class)
**Purpose:** Base error type for all VDR-LLM-Prolog errors. Carries error code, message, and context.

**Fields:** code (str), message (str), context (Dict[str, Any]).

#### Result (class)
**Purpose:** Rust-style Result wrapper. Either Ok(value) or Err(VDRError). Every function that can fail returns this instead of raising exceptions.

**Fields:** value (Optional[Any]), error (Optional[VDRError]), ok (bool).

**Methods:**
- `unwrap() -> Any` — returns value or raises if error.
- `unwrap_or(default) -> Any` — returns value or default.
- `map(fn) -> Result` — apply fn to value if ok.

---

### kb/knowledge_base.py

#### create_kb
**Purpose:** Create a new KnowledgeBase instance and register it in the KB store. Assigns the next available ID.

**Inputs:** name (str), path (str), parent_id (Optional[int]), owner (Optional[str]).

**Outputs:** KnowledgeBase instance.

**Side effects:** KB added to global KB store. ID assigned. If parent_id is provided, parent's children_ids list updated.

#### get_kb
**Purpose:** Retrieve a KB by ID or by path.

**Inputs:** identifier (int or str).

**Outputs:** Optional[KnowledgeBase].

**Side effects:** None. Read-only lookup.

#### delete_kb
**Purpose:** Remove a KB from the store. Detaches from parent. Does not cascade to children — they become orphans (which the orphan constraint will catch).

**Inputs:** kb_id (int).

**Outputs:** bool (success).

**Side effects:** KB removed from store. Parent's children_ids updated. ID retired (never reused).

---

### kb/fact_store.py

#### assert_fact
**Purpose:** Add a fact to a KB's fact list. If a structurally identical fact already exists, this is idempotent — no duplicate added.

**Inputs:** kb (KnowledgeBase), fact (Fact).

**Outputs:** bool (True if new fact added, False if already existed).

**Side effects:** kb.facts modified. kb.last_modified updated.

#### retract_fact
**Purpose:** Remove a fact from a KB's fact list. If fact not present, idempotent — no error.

**Inputs:** kb (KnowledgeBase), predicate (str), args (List[Any]).

**Outputs:** bool (True if fact was present and removed, False if not found).

**Side effects:** kb.facts modified. kb.last_modified updated.

#### query_facts
**Purpose:** Find all facts in a KB matching a predicate and argument pattern. Arguments may contain None as wildcard (matches anything).

**Inputs:** kb (KnowledgeBase), predicate (str), args (List[Optional[Any]]).

**Outputs:** List[Fact] — all matching facts.

**Side effects:** None. Read-only.

#### fact_exists
**Purpose:** Test if a structurally identical fact exists in the KB.

**Inputs:** kb (KnowledgeBase), fact (Fact).

**Outputs:** bool.

**Side effects:** None.

---

### kb/rule_engine.py

#### Binding (class)
**Purpose:** A set of variable bindings accumulated during unification. Maps variable names to their bound values.

**Fields:** bindings (Dict[str, Any]).

**Methods:**
- `get(var_name) -> Optional[Any]`
- `bind(var_name, value) -> Binding` — returns new Binding with added binding.
- `merge(other) -> Optional[Binding]` — combines two bindings; None if conflict.

#### unify
**Purpose:** Attempt to unify two terms. Returns bindings if successful, None if terms cannot unify. Handles: atoms (string equality), variables (bind to anything), VDRFractions (cross-multiplication equality), lists (element-wise recursive), facts (predicate + args recursive).

**Inputs:** term_a (Any), term_b (Any), bindings (Binding).

**Outputs:** Optional[Binding] — updated bindings if unification succeeds, None if fails.

**Side effects:** None. Pure.

#### substitute
**Purpose:** Apply bindings to a term, replacing all bound variables with their values.

**Inputs:** term (Any), bindings (Binding).

**Outputs:** Any — term with variables replaced.

**Side effects:** None. Pure.

#### query_rules
**Purpose:** Evaluate a query against a KB's facts and rules using depth-first search with backtracking. Produces all satisfying variable bindings.

**Inputs:** kb (KnowledgeBase), goal (Fact), max_depth (int, default 100).

**Outputs:** List[Binding] — all satisfying bindings.

**Side effects:** None. Read-only query over KB state.

#### query_rules_first
**Purpose:** Like query_rules but returns only the first satisfying binding (cut semantics).

**Inputs:** kb (KnowledgeBase), goal (Fact), max_depth (int).

**Outputs:** Optional[Binding].

**Side effects:** None.

---

### kb/working_data.py

#### set_binding
**Purpose:** Set a key-value binding in a KB's working_data dict.

**Inputs:** kb (KnowledgeBase), key (str), value (Any), turn (int).

**Outputs:** None.

**Side effects:** kb.working_data modified. kb.last_modified updated.

#### get_binding
**Purpose:** Look up a binding by key. Walks parent chain for inheritance if not found locally.

**Inputs:** kb (KnowledgeBase), key (str), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** Optional[Any] — value if found, None if not found in entire chain.

**Side effects:** None. Read-only.

#### get_binding_local
**Purpose:** Look up a binding by key in this KB only, no inheritance.

**Inputs:** kb (KnowledgeBase), key (str).

**Outputs:** Optional[Any].

**Side effects:** None.

#### delete_binding
**Purpose:** Remove a binding from a KB's working_data.

**Inputs:** kb (KnowledgeBase), key (str).

**Outputs:** bool (True if was present).

**Side effects:** kb.working_data modified.

#### list_visible_bindings
**Purpose:** Collect all bindings visible from a KB, including inherited ones from parent chain. Local bindings shadow parent bindings with the same key.

**Inputs:** kb (KnowledgeBase), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** Dict[str, Any] — complete visible binding set.

**Side effects:** None. Read-only.

---

### primitives/arithmetic.py

**Purpose:** Wraps core/vdr.py functions as IOSE-declared builtins. Each function takes VDRFraction inputs and returns VDRFraction outputs. All pure, deterministic, bounded.

**Pattern:** All 8 functions follow identical pattern:

```
Function: vdr_{op}(a: VDRFraction, b: VDRFraction) -> VDRFraction
Inputs: Two VDRFractions (or one for unary ops).
Outputs: One VDRFraction.
Side effects: None.
Properties: pure, deterministic, bounded.
Delegates to: core/vdr.py VDR class methods.
```

#### vdr_add
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction. **Delegates:** VDR.__add__. **Properties:** commutative, associative.

#### vdr_sub
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction. **Delegates:** VDR.__sub__.

#### vdr_mul
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction. **Delegates:** VDR.__mul__. **Properties:** commutative, associative.

#### vdr_div
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** Result[VDRFraction]. **Delegates:** VDR.__truediv__. **Properties:** partial (fails if b.v == 0).

#### vdr_neg
**Inputs:** a (VDRFraction). **Outputs:** VDRFraction. **Delegates:** VDR.__neg__. **Properties:** invertible.

#### vdr_abs
**Inputs:** a (VDRFraction). **Outputs:** VDRFraction. **Delegates:** abs(VDR). **Properties:** idempotent.

#### vdr_pow
**Inputs:** a (VDRFraction), n (int). **Outputs:** VDRFraction. **Delegates:** VDR.__pow__.

#### vdr_reciprocal
**Inputs:** a (VDRFraction). **Outputs:** Result[VDRFraction]. **Properties:** partial (fails if a.v == 0), invertible.

---

### primitives/comparison.py

**Purpose:** Exact comparison operations on VDRFractions. All use cross-multiplication for closed objects, scalar projection for active objects. All pure.

**Pattern:** Same pattern — VDRFraction inputs, simple output, no side effects.

#### vdr_compare
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** str ("less", "equal", "greater").

#### vdr_equal
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** bool. **Properties:** commutative.

#### vdr_less_than
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** bool.

#### vdr_less_equal
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** bool.

#### vdr_min
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction. **Properties:** commutative, associative, idempotent.

#### vdr_max
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction. **Properties:** commutative, associative, idempotent.

#### vdr_sign
**Inputs:** a (VDRFraction). **Outputs:** int (-1, 0, 1).

#### vdr_is_zero
**Inputs:** a (VDRFraction). **Outputs:** bool.

#### vdr_is_positive
**Inputs:** a (VDRFraction). **Outputs:** bool.

#### vdr_is_negative
**Inputs:** a (VDRFraction). **Outputs:** bool.

---

### primitives/rounding.py

**Pattern:** VDRFraction in, int or VDRFraction out, no side effects.

#### vdr_floor
**Inputs:** a (VDRFraction). **Outputs:** int.

#### vdr_ceil
**Inputs:** a (VDRFraction). **Outputs:** int.

#### vdr_round
**Inputs:** a (VDRFraction). **Outputs:** int.

#### vdr_truncate
**Inputs:** a (VDRFraction). **Outputs:** int.

#### vdr_numerator
**Inputs:** a (VDRFraction). **Outputs:** int. After normalization.

#### vdr_denominator
**Inputs:** a (VDRFraction). **Outputs:** int. After normalization.

#### vdr_simplify
**Inputs:** a (VDRFraction). **Outputs:** VDRFraction. **Properties:** idempotent.

---

### primitives/list_aggregates.py

**Pattern:** List[VDRFraction] in, VDRFraction out.

#### vdr_sum
**Inputs:** items (List[VDRFraction]). **Outputs:** VDRFraction. Empty returns [0,1,0]. **Properties:** commutative, associative.

#### vdr_product
**Inputs:** items (List[VDRFraction]). **Outputs:** VDRFraction. Empty returns [1,1,0]. **Properties:** commutative, associative.

#### vdr_mean
**Inputs:** items (List[VDRFraction]). **Outputs:** Result[VDRFraction]. **Properties:** partial (fails on empty).

#### vdr_dot_product
**Inputs:** a (List[VDRFraction]), b (List[VDRFraction]). **Outputs:** Result[VDRFraction]. **Properties:** partial (fails if different lengths), commutative.

#### vdr_sum_of_squares
**Inputs:** items (List[VDRFraction]). **Outputs:** VDRFraction.

#### vdr_weighted_sum
**Inputs:** weights (List[VDRFraction]), values (List[VDRFraction]). **Outputs:** Result[VDRFraction]. Partial (fails if different lengths).

#### vdr_harmonic_sum
**Inputs:** n (int). **Outputs:** VDRFraction. H_n = 1 + 1/2 + ... + 1/n.

#### vdr_alternating_sum
**Inputs:** items (List[VDRFraction]). **Outputs:** VDRFraction.

---

### primitives/text.py

**Purpose:** 17 string operations. All pure, deterministic, bounded.

**Pattern:** All follow identical structure — string inputs, string or bool or int or list output, no side effects. Listing by group:

**Construction:** string_concat(a, b) → str. string_join(items, delim) → str. string_pad_left(s, width, fill) → str. chars_to_string(chars) → str.

**Decomposition:** string_split(s, delim) → List[str]. string_slice(s, start, end) → str. string_char_at(s, idx) → Result[str] (partial). string_to_chars(s) → List[str]. string_length(s) → int.

**Search:** string_contains(s, sub) → bool. string_starts_with(s, prefix) → bool. string_ends_with(s, suffix) → bool.

**Transformation:** string_reverse(s) → str. string_upper(s) → str. string_lower(s) → str. string_trim(s) → str. string_replace(s, old, new) → str.

---

### primitives/collections.py

**Purpose:** 36 list operations. All pure.

**Pattern:** All follow standard input/output, no side effects.

**Construction (4):** list_append(lst, item) → list. list_prepend(item, lst) → list. list_concat(a, b) → list. list_enumerate(lst) → List[Tuple].

**Access (9):** list_length(lst) → int. list_head(lst) → Result[Any]. list_tail(lst) → Result[list]. list_last(lst) → Result[Any]. list_init(lst) → Result[list]. list_nth(lst, n) → Result[Any]. list_take(lst, n) → list. list_drop(lst, n) → list. list_slice(lst, start, end) → list.

**Transformation (6):** list_reverse(lst) → list. list_map(lst, fn) → list. list_flatten(lst) → list. list_unique(lst) → list. list_chunk(lst, n) → List[list]. list_interleave(a, b) → list.

**Search (6):** list_contains(lst, item) → bool. list_index_of(lst, item) → Result[int]. list_filter(lst, pred) → list. list_any(lst, pred) → bool. list_all(lst, pred) → bool. list_count(lst, pred) → int.

**Sorting (5):** list_sort(lst, key_fn) → list. list_sort_reverse(lst, key_fn) → list. list_sort_by_key(lst, key_fn) → list. list_min(lst) → Result[Any]. list_max(lst) → Result[Any].

**Partitioning (3):** list_partition(lst, pred) → Tuple[list, list]. list_group_by(lst, key_fn) → Dict. list_frequencies(lst) → Dict.

**Aggregation (1):** list_reduce(lst, fn, init) → Any.

**Combination (2):** list_zip(a, b) → List[Tuple]. list_unzip(pairs) → Tuple[list, list].

---

### primitives/sets.py

**Purpose:** 14 set operations. All pure.

**Pattern:** set or list input, set or bool or int output, no side effects.

**Construction (4):** set_from_list(lst) → set. set_to_list(s) → list. set_add(s, item) → set. set_remove(s, item) → set.

**Membership (2):** set_contains(s, item) → bool. set_size(s) → int.

**Algebra (5):** set_union(a, b) → set. set_intersection(a, b) → set. set_difference(a, b) → set. set_symmetric_diff(a, b) → set. set_power(s) → set.

**Comparison (3):** set_is_subset(a, b) → bool. set_is_superset(a, b) → bool. set_is_disjoint(a, b) → bool.

---

### primitives/mappings.py

**Purpose:** 15 dict operations. All pure.

**Pattern:** dict input, dict or value or list output, no side effects.

**Construction (2):** dict_new() → dict. dict_from_pairs(pairs) → dict.

**Access (4):** dict_get(d, key) → Result[Any]. dict_get_or(d, key, default) → Any. dict_contains_key(d, key) → bool. dict_size(d) → int.

**Mutation (3):** dict_set(d, key, val) → dict. dict_remove(d, key) → dict. dict_merge(a, b) → dict.

**Iteration (4):** dict_keys(d) → list. dict_values(d) → list. dict_pairs(d) → List[Tuple]. dict_filter_keys(d, pred) → dict.

**Transform (2):** dict_map_values(d, fn) → dict. dict_invert(d) → Result[dict] (partial if values not unique).

---

### primitives/conversion.py

**Purpose:** Type conversion and format parsing. Stage 1 includes the critical conversion boundaries.

#### to_string
**Inputs:** value (Any). **Outputs:** str. Pure.

#### to_number
**Inputs:** s (str). **Outputs:** Result[int]. Partial.

#### to_fraction
**Inputs:** s (str). **Outputs:** Result[VDRFraction]. Partial. **THIS IS THE PRIMARY CONVERSION BOUNDARY.**

#### format_json
**Inputs:** d (dict). **Outputs:** str. Pure.

#### parse_json
**Inputs:** s (str). **Outputs:** Result[dict]. Partial.

#### format_csv
**Inputs:** rows (List[List[str]]), delimiter (str). **Outputs:** str. Pure.

#### parse_csv
**Inputs:** s (str), delimiter (str). **Outputs:** List[List[str]]. Pure.

#### format_table
**Inputs:** rows (List[List[str]]). **Outputs:** str. Pure.

#### format_fraction
**Inputs:** f (VDRFraction). **Outputs:** str. Pure. Lossless.

#### fraction_to_decimal
**Inputs:** f (VDRFraction), digits (int). **Outputs:** str. Lossy.

#### format_percentage
**Inputs:** f (VDRFraction), decimal_places (int). **Outputs:** str. Lossy.

#### format_scientific
**Inputs:** f (VDRFraction), sig_digits (int). **Outputs:** str. Lossy.

#### vdr_from_decimal_string
**Inputs:** s (str). **Outputs:** Result[VDRFraction]. Exact for terminating decimals. Conversion boundary entry point.

#### vdr_from_ratio_string
**Inputs:** s (str). **Outputs:** Result[VDRFraction]. Exact. Lossless.

---

### primitives/logic.py

**Purpose:** 11 control flow and meta operations.

#### if_then_else
**Inputs:** condition (bool), true_fn (Callable), false_fn (Callable). **Outputs:** Any.

#### case_match
**Inputs:** value (Any), cases (List[Tuple[Any, Callable]]). **Outputs:** Result[Any]. Partial.

#### for_each
**Inputs:** items (list), fn (Callable). **Outputs:** None.

#### repeat_n
**Inputs:** n (int), fn (Callable). **Outputs:** list.

#### while_loop
**Inputs:** predicate (Callable), fn (Callable), state (Any). **Outputs:** Any.

#### try_catch
**Inputs:** fn (Callable), handler (Callable). **Outputs:** Any.

#### assert_that
**Inputs:** condition (bool), message (str). **Outputs:** Result[None]. Partial.

#### type_check
**Inputs:** value (Any), expected_type (str). **Outputs:** bool.

#### is_bound
**Inputs:** var_name (str), bindings (Binding). **Outputs:** bool.

#### findall
**Inputs:** kb (KnowledgeBase), goal (Fact). **Outputs:** List[Binding]. Delegates to rule_engine.query_rules.

#### aggregate
**Inputs:** kb (KnowledgeBase), goal (Fact), fn (Callable), init (Any). **Outputs:** Any.

---

### primitives/integer_ops.py

**Purpose:** 13 fast integer operations + 8 bit operations. All pure.

**Integer pattern:** int inputs, int output, no side effects.

**Arithmetic (7):** int_add(a, b) → int. int_sub(a, b) → int. int_mul(a, b) → int. int_div(a, b) → Result[int] (partial). int_mod(a, b) → Result[int] (partial). int_pow(a, b) → int. int_abs(a) → int.

**Comparison/utility (4):** int_sign(a) → int. int_min(a, b) → int. int_max(a, b) → int. int_clamp(val, lo, hi) → int.

**Range (2):** int_range(start, end) → List[int]. int_range_step(start, end, step) → List[int].

**Bit operations (8):** bit_and(a, b) → int. bit_or(a, b) → int. bit_xor(a, b) → int. bit_not(a) → int. bit_shift_left(a, n) → int. bit_shift_right(a, n) → int. bit_count(a) → int. bit_width(a) → int.

---

### data_primitives/counter.py

**Purpose:** Standalone functions that operate on Counter instances within a KB. The Counter dataclass is defined in shared structures. These functions provide the IOSE-declared builtin interface.

#### counter_create
**Inputs:** kb (KnowledgeBase), name (str), min_value (int), max_value (int). **Outputs:** None. **Side effects:** kb.counters[name] created.

#### counter_inc
**Inputs:** kb (KnowledgeBase), name (str). **Outputs:** Result[int]. **Side effects:** counter value mutated.

#### counter_dec
**Inputs:** kb (KnowledgeBase), name (str). **Outputs:** Result[int]. **Side effects:** counter value mutated.

#### counter_add
**Inputs:** kb (KnowledgeBase), name (str), delta (int). **Outputs:** Result[int]. **Side effects:** counter value mutated.

#### counter_get
**Inputs:** kb (KnowledgeBase), name (str). **Outputs:** Result[int]. **Side effects:** None. Read-only.

#### counter_reset
**Inputs:** kb (KnowledgeBase), name (str). **Outputs:** None. **Side effects:** counter value mutated. Idempotent.

#### counter_set
**Inputs:** kb (KnowledgeBase), name (str), value (int). **Outputs:** None. **Side effects:** counter value mutated. Idempotent.

---

### data_primitives/lock.py

**Pattern:** Same as counter — functions operating on LockState within KB.

#### lock_create
**Inputs:** kb, name. **Side effects:** kb.locks[name] created.

#### lock_acquire
**Inputs:** kb, name, holder (str), notes (str). **Outputs:** bool (True if acquired). **Side effects:** lock state changed if successful.

#### lock_release
**Inputs:** kb, name. **Side effects:** lock state changed. Idempotent.

#### lock_check
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### lock_holder
**Inputs:** kb, name. **Outputs:** Result[str]. Partial.

#### lock_force_release
**Inputs:** kb, name. **Side effects:** lock state changed. Idempotent.

---

### data_primitives/queue.py

**Pattern:** Same — functions operating on BoundedQueue within KB.

#### queue_create
**Inputs:** kb, name, capacity (int). **Side effects:** kb.queues[name] created.

#### queue_push
**Inputs:** kb, name, item (Any). **Outputs:** bool (False if full). **Side effects:** queue mutated.

#### queue_pop
**Inputs:** kb, name. **Outputs:** Result[Any]. Partial (fails if empty). **Side effects:** queue mutated.

#### queue_peek
**Inputs:** kb, name. **Outputs:** Result[Any]. Partial. **Side effects:** None.

#### queue_size
**Inputs:** kb, name. **Outputs:** int. **Side effects:** None.

#### queue_is_empty
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### queue_is_full
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### queue_clear
**Inputs:** kb, name. **Side effects:** queue cleared. Idempotent.

#### queue_to_list
**Inputs:** kb, name. **Outputs:** List[Any]. **Side effects:** None.

---

### data_primitives/stack.py

**Pattern:** Same — functions operating on BoundedStack within KB.

#### stack_create
**Inputs:** kb, name, capacity (int). **Side effects:** kb.stacks[name] created.

#### stack_push
**Inputs:** kb, name, item (Any). **Outputs:** bool (False if full). **Side effects:** stack mutated.

#### stack_pop
**Inputs:** kb, name. **Outputs:** Result[Any]. Partial. **Side effects:** stack mutated.

#### stack_peek
**Inputs:** kb, name. **Outputs:** Result[Any]. Partial. **Side effects:** None.

#### stack_size
**Inputs:** kb, name. **Outputs:** int. **Side effects:** None.

#### stack_is_empty
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### stack_clear
**Inputs:** kb, name. **Side effects:** stack cleared. Idempotent.

#### stack_to_list
**Inputs:** kb, name. **Outputs:** List[Any]. Top-to-bottom order. **Side effects:** None.

---

### iose/registry.py

#### BuiltinRegistry (class)
**Purpose:** Global registry of all builtins. Maps IDs and names to BuiltinDef instances containing IOSE declarations and implementations.

**Methods:**

#### register
**Inputs:** builtin_def (BuiltinDef). **Outputs:** None. **Side effects:** Entry added to both by-ID and by-name maps.

#### get_by_id
**Inputs:** builtin_id (int). **Outputs:** Optional[BuiltinDef]. **Side effects:** None.

#### get_by_name
**Inputs:** name (str). **Outputs:** Optional[BuiltinDef]. **Side effects:** None.

#### all_in_category
**Inputs:** category (str). **Outputs:** List[BuiltinDef]. **Side effects:** None.

#### count
**Inputs:** None. **Outputs:** int. **Side effects:** None.

#### register_builtin (module-level helper)
**Purpose:** Convenience function that creates an IOSEDeclaration and BuiltinDef, then registers.

**Inputs:** builtin_id (int), name (str), category (str), inputs (List[str]), outputs (List[str]), side_effects (List[str]), properties (List[str]), description (str), impl (Callable).

**Outputs:** None. **Side effects:** Builtin registered in global registry.

---

### iose/principles.py

#### load_oso_principles
**Purpose:** Create and populate the root.system.oso KB with all OSO axioms, facts, rules, and constraints. Called at system startup.

**Inputs:** kb_store (the global KB store).

**Outputs:** KnowledgeBase (the populated OSO KB).

**Side effects:** KB created and registered. ~176 Prolog terms asserted (15 axioms, ~80 facts, ~60 rules, 21 constraints).

#### get_knowability
**Purpose:** Look up the knowability level for a source type.

**Inputs:** source_type (str).

**Outputs:** VDRFraction (confidence value).

**Side effects:** None. Reads from OSO KB.

#### get_priority
**Purpose:** Look up the priority weight for a concern.

**Inputs:** concern (str), domain (str — "evidence", "lifecycle", "response").

**Outputs:** VDRFraction (priority weight).

**Side effects:** None. Reads from OSO KB.

#### priority_winner
**Purpose:** Given two competing concerns, determine which wins by the 90/9/0.9 rule.

**Inputs:** concern_a (str), concern_b (str), domain (str).

**Outputs:** str — "a", "b", or "tradeoff_required".

**Side effects:** None. Pure decision.

---

## Stage 2: Upgraded Toy

### kb/constraint_engine.py

#### check_constraint
**Purpose:** Evaluate a single constraint's condition against the current KB state. The condition is a Prolog goal — evaluated by the rule engine.

**Inputs:** kb (KnowledgeBase), constraint (Constraint), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** bool (True if satisfied).

**Side effects:** None. Read-only evaluation.

#### check_all_constraints
**Purpose:** Evaluate all active constraints in a KB. Returns list of violations.

**Inputs:** kb (KnowledgeBase), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** List[Constraint] — constraints that are violated.

**Side effects:** None.

#### enforce_constraint
**Purpose:** After a violation is detected, execute the on_violation action.

**Inputs:** constraint (Constraint), kb (KnowledgeBase).

**Outputs:** str — action taken ("warned", "blocked", "error_raised", "escalated").

**Side effects:** Depends on on_violation: may log a warning fact, may block an operation, may raise error.

#### add_constraint
**Inputs:** kb (KnowledgeBase), constraint (Constraint). **Side effects:** Constraint added to kb.constraints.

#### remove_constraint
**Inputs:** kb (KnowledgeBase), name (str). **Side effects:** Constraint removed. Idempotent.

#### enable_constraint
**Inputs:** kb (KnowledgeBase), name (str). **Side effects:** Constraint status set to "active". Idempotent.

#### suspend_constraint
**Inputs:** kb (KnowledgeBase), name (str). **Side effects:** Constraint status set to "suspended". Idempotent.

---

### kb/scope_resolver.py

#### ScopeChain (class)
**Purpose:** Represents the ordered list of KB IDs in scope for a given active topic.

**Fields:** chain (List[int]) — ordered from current KB to root. secondary (List[int]) — explicitly activated secondary scopes.

#### build_scope_chain
**Purpose:** Given an active topic KB, build the scope chain by walking parent_id links to root, then adding global KB.

**Inputs:** active_kb_id (int), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** ScopeChain.

**Side effects:** None.

#### scoped_query
**Purpose:** Query a predicate across the scope chain. First match wins (cut semantics within scope order).

**Inputs:** scope_chain (ScopeChain), predicate (str), args (List[Optional[Any]]), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** List[Fact] — matches from first KB in scope that has any.

**Side effects:** None.

#### scoped_query_all
**Purpose:** Query across ALL KBs (not just scope). Tags each result with its source KB.

**Inputs:** predicate (str), args (List[Optional[Any]]), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** List[Tuple[str, Fact]] — (kb_path, fact) pairs.

**Side effects:** None.

#### resolve_binding_scoped
**Purpose:** Resolve a working data binding through the scope chain with inheritance.

**Inputs:** scope_chain (ScopeChain), key (str), kb_store (Dict[int, KnowledgeBase]).

**Outputs:** Optional[Any].

**Side effects:** None.

---

### path/registry.py

#### PathRegistry (class)
**Purpose:** Maps dotted paths to integer IDs and back. Assigns sequential IDs. Retired IDs are never reused.

**Fields:** path_to_id (Dict[str, int]), id_to_path (List[str]), next_id (int).

#### register_path
**Inputs:** path (str). **Outputs:** int (assigned ID). **Side effects:** ID assigned if new. If already registered, returns existing ID.

#### resolve
**Inputs:** path (str). **Outputs:** Result[int]. Partial (fails if not registered).

#### from_id
**Inputs:** id (int). **Outputs:** Result[str]. Partial (fails if not registered).

#### exists
**Inputs:** path (str). **Outputs:** bool.

---

### path/resolver.py

#### resolve_dotted_path
**Purpose:** Resolve a dotted path string to an integer ID. Handles absolute paths (start with "root.") and returns the ID from the PathRegistry.

**Inputs:** path (str), registry (PathRegistry).

**Outputs:** Result[int].

**Side effects:** None.

#### path_parent
**Inputs:** path (str). **Outputs:** Result[str]. Fails on "root".

#### path_children
**Inputs:** path (str), registry (PathRegistry). **Outputs:** List[str].

#### path_ancestors
**Inputs:** path (str). **Outputs:** List[str]. From parent to root.

#### path_depth
**Inputs:** path (str). **Outputs:** int. Root is 0.

#### path_common_ancestor
**Inputs:** path_a (str), path_b (str). **Outputs:** str.

---

### command/token_types.py

**Purpose:** Contains the CommandToken, CommandArg, CommandType, and ArgType dataclasses and enums. Already defined in shared structures above. This module just re-exports them.

---

### command/parser.py

#### parse_command_stream
**Purpose:** Parse a mixed stream of text and command tokens. Text tokens are strings. Command tokens are structured invocations.

**Inputs:** raw_stream (str — the LLM's output with CMD: prefixes).

**Outputs:** List[Union[str, CommandToken]] — interleaved text and commands.

**Side effects:** None. Pure parsing.

#### parse_single_command
**Purpose:** Parse a single CMD: line into a CommandToken.

**Inputs:** line (str).

**Outputs:** Result[CommandToken].

**Side effects:** None.

---

### command/executor.py

#### execute_command
**Purpose:** Dispatch a parsed CommandToken to the appropriate builtin or system operation. Resolves path arguments to integer IDs. Validates types against IOSE declaration. Executes. Returns result.

**Inputs:** token (CommandToken), registry (BuiltinRegistry), path_registry (PathRegistry), kb_store (Dict[int, KnowledgeBase]), scope_chain (ScopeChain).

**Outputs:** Result[Any] — the operation's output.

**Side effects:** Depends on the command. Pure commands: none. KB commands: KB state modified. Op commands: external effects.

#### execute_chain
**Purpose:** Execute a sequence of CommandTokens. Validates type compatibility between steps. Collects accumulated side effects.

**Inputs:** tokens (List[CommandToken]), registry, path_registry, kb_store, scope_chain.

**Outputs:** Result[List[Any]] — results of each step.

**Side effects:** Union of all step side effects.

---

### command/scratchpad.py

#### Scratchpad (class)
**Purpose:** A RingBuffer-based internal computation channel. The LLM's internal workspace. Created at session start.

**Fields:** buffer (RingBuffer), path (str — "root.sessions.active.scratchpad").

#### write_entry
**Inputs:** entry_type (str), content (Any), turn (int). **Side effects:** Entry written to ring buffer.

#### read_recent
**Inputs:** count (int). **Outputs:** List[Dict]. **Side effects:** None.

#### clear
**Side effects:** Buffer cleared.

---

### primitives/active_arithmetic.py

**Purpose:** 5 active arithmetic builtins wrapping core/active_mul.py.

**Pattern:** Same as closed arithmetic — VDRFraction in, VDRFraction out, pure.

#### vdr_active_add_same_d
**Inputs:** a (VDRFraction), b (VDRFraction). Both must share d. **Outputs:** VDRFraction.

#### vdr_active_add_diff_d
**Inputs:** a (VDRFraction), b (VDRFraction). Different d values. **Outputs:** VDRFraction.

#### vdr_active_mul
**Inputs:** a (VDRFraction), b (VDRFraction). **Outputs:** VDRFraction.

#### vdr_active_div_by_closed
**Inputs:** a (VDRFraction), b (VDRFraction). b must be closed. **Outputs:** Result[VDRFraction]. Partial.

#### vdr_active_div_by_active
**Inputs:** a (VDRFraction), b (VDRFraction). Both active. **Outputs:** Result[VDRFraction]. Partial. Divisor remainder lost (v1 compromise).

---

### primitives/structure_ops.py

#### vdr_lift
**Inputs:** remainder (Any — int, CompositeRemainder, or FnRemainder), k (int). **Outputs:** remainder (same type family). Pure.

#### vdr_rebase
**Inputs:** frac (VDRFraction), target_d (int). **Outputs:** VDRFraction. May produce mismatch witness. Pure.

#### vdr_scalar_projection
**Inputs:** frac (VDRFraction). **Outputs:** Result[VDRFraction] (closed). Partial: fails if functional remainder not resolved.

---

### primitives/number_theory.py

**Pattern:** int inputs, int output, pure.

#### vdr_gcd
**Inputs:** a (int), b (int). **Outputs:** int. Commutative, associative.

#### vdr_lcm
**Inputs:** a (int), b (int). **Outputs:** int. Commutative, associative.

#### vdr_mod
**Inputs:** a (int), b (int). **Outputs:** Result[int]. Partial (b=0).

#### vdr_div_exact
**Inputs:** a (int), b (int). **Outputs:** Result[int]. Partial (not evenly divisible).

#### vdr_mod_pow
**Inputs:** base (int), exp (int), modulus (int). **Outputs:** int. Binary exponentiation.

#### vdr_mod_inv
**Inputs:** a (int), m (int). **Outputs:** Result[int]. Partial (gcd(a,m) != 1).

#### vdr_extended_gcd
**Inputs:** a (int), b (int). **Outputs:** Tuple[int, int, int] — (g, x, y) where a*x + b*y = g.

#### vdr_is_prime
**Inputs:** n (int). **Outputs:** bool.

#### vdr_factorial
**Inputs:** n (int). **Outputs:** Result[int]. Partial (n < 0).

#### vdr_binomial
**Inputs:** n (int), k (int). **Outputs:** int.

#### vdr_fibonacci
**Inputs:** n (int). **Outputs:** int. Matrix power method for large n.

#### vdr_euler_totient
**Inputs:** n (int). **Outputs:** int.

#### vdr_chinese_remainder
**Inputs:** remainders (List[int]), moduli (List[int]). **Outputs:** Result[int]. Partial (not pairwise coprime).

---

### primitives/linalg_builtins.py

**Purpose:** 24 linear algebra builtins wrapping core/linalg.py.

**Vector pattern:** Vec inputs, Vec or VDRFraction output, pure.

#### vdr_vec_new
**Inputs:** elements (List[VDRFraction]). **Outputs:** Vec.

#### vdr_vec_dim
**Inputs:** v (Vec). **Outputs:** int.

#### vdr_vec_get
**Inputs:** v (Vec), index (int). **Outputs:** Result[VDRFraction]. Partial.

#### vdr_vec_add
**Inputs:** a (Vec), b (Vec). **Outputs:** Vec. Commutative, associative.

#### vdr_vec_sub
**Inputs:** a (Vec), b (Vec). **Outputs:** Vec.

#### vdr_vec_scale
**Inputs:** scalar (VDRFraction), v (Vec). **Outputs:** Vec.

#### vdr_vec_dot
**Inputs:** a (Vec), b (Vec). **Outputs:** VDRFraction. Commutative.

#### vdr_vec_norm_sq
**Inputs:** v (Vec). **Outputs:** VDRFraction.

#### vdr_vec_neg
**Inputs:** v (Vec). **Outputs:** Vec. Invertible.

**Matrix pattern:** Mat inputs, Mat or VDRFraction or Vec output, pure.

#### vdr_mat_new
**Inputs:** rows (List[Vec]). **Outputs:** Mat.

#### vdr_mat_dims
**Inputs:** m (Mat). **Outputs:** Tuple[int, int].

#### vdr_mat_get
**Inputs:** m (Mat), row (int), col (int). **Outputs:** Result[VDRFraction]. Partial.

#### vdr_mat_add
**Inputs:** a (Mat), b (Mat). **Outputs:** Mat. Commutative, associative.

#### vdr_mat_mul
**Inputs:** a (Mat), b (Mat). **Outputs:** Mat. Associative. NOT commutative.

#### vdr_mat_scale
**Inputs:** scalar (VDRFraction), m (Mat). **Outputs:** Mat.

#### vdr_mat_transpose
**Inputs:** m (Mat). **Outputs:** Mat. Invertible (self-inverse).

#### vdr_mat_matvec
**Inputs:** m (Mat), v (Vec). **Outputs:** Vec.

#### vdr_mat_det
**Inputs:** m (Mat). **Outputs:** VDRFraction.

#### vdr_mat_inv
**Inputs:** m (Mat). **Outputs:** Result[Mat]. Partial (det=0). Invertible.

#### vdr_mat_solve
**Inputs:** a (Mat), b (Vec). **Outputs:** Result[Vec]. Partial (det=0).

#### vdr_mat_rank
**Inputs:** m (Mat). **Outputs:** int.

#### vdr_mat_identity
**Inputs:** size (int). **Outputs:** Mat.

#### vdr_mat_trace
**Inputs:** m (Mat). **Outputs:** VDRFraction.

#### vdr_mat_pow
**Inputs:** m (Mat), n (int). **Outputs:** Mat.

#### vdr_mat_gram_schmidt
**Inputs:** m (Mat). **Outputs:** Result[Mat]. Partial (linearly dependent).

---

### primitives/statistics.py

**Purpose:** 16 statistics and probability builtins. All pure.

**Descriptive (5):** vdr_stat_mean(items) → Result[VDRFraction]. vdr_stat_variance(items) → Result[VDRFraction]. vdr_stat_median(items) → Result[VDRFraction]. vdr_stat_mode(items) → Result[Any]. vdr_stat_percentile(items, p) → Result[VDRFraction].

**Probability (5):** vdr_prob_normalize(items) → List[VDRFraction]. vdr_prob_is_valid(items) → bool. vdr_prob_bayes(p_b_given_a, p_a, p_b) → Result[VDRFraction]. vdr_prob_expected(probs, values) → VDRFraction. vdr_prob_cdf(pmf) → List[VDRFraction].

**Distribution (3):** vdr_prob_joint(marginal_a, marginal_b) → Mat. vdr_prob_marginal(joint, axis) → List[VDRFraction]. vdr_prob_conditional(joint, given_index) → Result[List[VDRFraction]].

**Entropy (1):** vdr_prob_entropy_terms(probs, log_depth) → List[VDRFraction].

**Softmax (2):** vdr_softmax(logits, depth) → List[VDRFraction]. vdr_softmax_surrogate(logits, shift) → List[VDRFraction].

---

### primitives/time_ops.py

**Pattern:** int inputs (day counts, year/month/day), int or str outputs, pure.

**10 builtins:** date_from_ymd, date_to_ymd, date_diff_days, date_add_days, date_day_of_week, date_is_leap_year, date_days_in_month, time_from_hms, time_to_hms, duration_between.

All follow identical IOSE pattern: pure, deterministic, bounded, exact Gregorian calendar algorithms.

---

### primitives/identity.py

**Pattern:** str or int inputs, int or str outputs, pure, deterministic.

**8 builtins:** hash_string, hash_combine, base64_encode, base64_decode (partial), hex_encode, hex_decode (partial), crc32, uuid_from_seed.

---

### primitives/graphs.py

**Purpose:** 13 graph algorithm builtins. All pure.

**Graph representation:** Dict[Any, List[Any]] adjacency list, or List[Tuple] edge list.

#### graph_from_edges
**Inputs:** edges (List[Tuple]). **Outputs:** graph (Dict adjacency).

#### graph_neighbors
**Inputs:** graph, node. **Outputs:** List[node].

#### graph_bfs
**Inputs:** graph, start_node. **Outputs:** List[node].

#### graph_dfs
**Inputs:** graph, start_node. **Outputs:** List[node].

#### graph_shortest_path
**Inputs:** graph, start, end. **Outputs:** Result[List[node]]. Partial (no path).

#### graph_shortest_path_weighted
**Inputs:** graph (with VDRFraction weights), start, end. **Outputs:** Result[Tuple[List[node], VDRFraction]]. Partial.

#### graph_connected_components
**Inputs:** graph. **Outputs:** List[List[node]].

#### graph_is_connected
**Inputs:** graph. **Outputs:** bool.

#### graph_topological_sort
**Inputs:** graph. **Outputs:** Result[List[node]]. Partial (cycle exists).

#### graph_cycle_detect
**Inputs:** graph. **Outputs:** bool.

#### graph_degree
**Inputs:** graph, node. **Outputs:** int.

#### graph_mst
**Inputs:** graph (weighted). **Outputs:** List[Tuple] (edges of MST).

#### graph_pagerank
**Inputs:** graph, damping (VDRFraction). **Outputs:** List[VDRFraction].

---

### data_primitives/lru.py

**Pattern:** Functions operating on LRUCache within KB.

#### lru_create
**Inputs:** kb, name, capacity. **Side effects:** kb.lrus[name] created.

#### lru_push
**Inputs:** kb, name, key (str), value (Any). **Side effects:** Entry added or updated. Oldest evicted if full.

#### lru_get
**Inputs:** kb, name, key. **Outputs:** Result[Any]. Partial. **Side effects:** Access time updated.

#### lru_peek
**Inputs:** kb, name, count (int). **Outputs:** List[Tuple[str, Any]]. **Side effects:** None. No access update.

#### lru_contains
**Inputs:** kb, name, key. **Outputs:** bool. **Side effects:** None.

#### lru_size
**Inputs:** kb, name. **Outputs:** int. **Side effects:** None.

#### lru_clear
**Inputs:** kb, name. **Side effects:** All entries removed. Idempotent.

#### lru_evict
**Inputs:** kb, name, key. **Side effects:** Entry removed. Idempotent.

---

### data_primitives/ring_buffer.py

**Pattern:** Functions operating on RingBuffer within KB.

#### ring_create
**Inputs:** kb, name, capacity. **Side effects:** kb.buffers[name] created.

#### ring_write
**Inputs:** kb, name, item. **Side effects:** Item written. Oldest overwritten if full.

#### ring_read_all
**Inputs:** kb, name. **Outputs:** List[Any]. Chronological. **Side effects:** None.

#### ring_read_last
**Inputs:** kb, name, count. **Outputs:** List[Any]. **Side effects:** None.

#### ring_size
**Inputs:** kb, name. **Outputs:** int. **Side effects:** None.

#### ring_clear
**Inputs:** kb, name. **Side effects:** Buffer reset. Idempotent.

---

### data_primitives/bitset.py

**Pattern:** Functions operating on Bitset within KB.

#### bitset_create
**Inputs:** kb, name, width. **Side effects:** kb.bitsets[name] created.

#### bitset_set
**Inputs:** kb, name, index. **Side effects:** Bit set. Idempotent.

#### bitset_clear_bit
**Inputs:** kb, name, index. **Side effects:** Bit cleared. Idempotent.

#### bitset_test
**Inputs:** kb, name, index. **Outputs:** bool. **Side effects:** None.

#### bitset_count
**Inputs:** kb, name. **Outputs:** int. **Side effects:** None.

#### bitset_all_set
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### bitset_any_set
**Inputs:** kb, name. **Outputs:** bool. **Side effects:** None.

#### bitset_reset
**Inputs:** kb, name. **Side effects:** All bits cleared. Idempotent.

#### bitset_to_list
**Inputs:** kb, name. **Outputs:** List[int]. Sorted indices of set bits. **Side effects:** None.

---

### iose/validator.py

#### validate_type_compatibility
**Purpose:** Check if the output type of one builtin matches the input type of the next in a chain.

**Inputs:** chain (List[BuiltinDef]).

**Outputs:** List[str] — type mismatch descriptions. Empty if all compatible.

**Side effects:** None.

#### preview_side_effects
**Purpose:** Collect all declared side effects of a command chain before execution.

**Inputs:** chain (List[BuiltinDef]).

**Outputs:** List[str] — all side effects that would occur.

**Side effects:** None.

#### verify_contract
**Purpose:** After execution, compare declared side effects against actually observed effects.

**Inputs:** builtin_def (BuiltinDef), declared_effects (List[str]), observed_effects (List[str]).

**Outputs:** List[str] — contract violations (undeclared effects or missing declared effects).

**Side effects:** None.

---

## Stage 3: Capacity Building

### path/mount.py

#### create_mount
**Purpose:** Mount a source KB at a target path. Validates no cycles. Creates mount record.

**Inputs:** mount_path (str), source_path (str), mode (MountMode), registry (PathRegistry), kb_store.

**Outputs:** Result[Mount]. Partial (fails if cycle detected or source not found).

**Side effects:** Mount record added to target KB. Mount path registered.

#### remove_mount
**Inputs:** mount_path (str), kb_store. **Side effects:** Mount removed. Idempotent.

#### check_mount_cycle
**Purpose:** Trace mount chain from source to verify target does not appear. Prevents A→B→A cycles.

**Inputs:** source_path (str), target_path (str), kb_store.

**Outputs:** bool (True if safe, False if cycle detected).

**Side effects:** None.

#### resolve_through_mount
**Purpose:** When a scoped query hits a mount point, resolve through to the source KB respecting mount mode.

**Inputs:** mount (Mount), predicate (str), args, kb_store.

**Outputs:** List[Fact]. Empty if mount mode blocks the operation.

**Side effects:** None.

---

### primitives/qbasis.py

**Purpose:** 7 Q-basis transcendental operations.

#### qbasis_add
**Inputs:** a (QBasis), b (QBasis). **Outputs:** QBasis. Same exponent: integer addition. Different exponent: align first.

#### qbasis_sub
**Inputs:** a (QBasis), b (QBasis). **Outputs:** QBasis.

#### qbasis_mul
**Inputs:** a (QBasis), b (QBasis). **Outputs:** Tuple[QBasis, VDRFraction] — (reprojected result, exact error bound).

#### qbasis_scalar_mul
**Inputs:** scalar (VDRFraction), qb (QBasis). **Outputs:** QBasis.

#### qbasis_to_fraction
**Inputs:** qb (QBasis). **Outputs:** VDRFraction. Lossless.

#### qbasis_get_constant
**Inputs:** name (str). **Outputs:** Result[QBasis]. Partial (name not in basis).

#### qbasis_precision_bits
**Inputs:** qb (QBasis). **Outputs:** int.

---

### primitives/functional.py

**Purpose:** 8 functional remainder operations.

#### fn_sqrt
**Inputs:** value (VDRFraction), depth (int). **Outputs:** VDRFraction. Newton-Raphson.

#### fn_exp
**Inputs:** value (VDRFraction), depth (int). **Outputs:** VDRFraction. Truncated Taylor.

#### fn_log
**Inputs:** value (VDRFraction), depth (int). **Outputs:** Result[VDRFraction]. Partial (value <= 0).

#### fn_sin
**Inputs:** value (VDRFraction), depth (int). **Outputs:** VDRFraction. Taylor series.

#### fn_cos
**Inputs:** value (VDRFraction), depth (int). **Outputs:** VDRFraction. Taylor series.

#### fn_resolve
**Inputs:** fn_remainder (FnRemainder), depth (int). **Outputs:** VDRFraction. Evaluates the callable.

#### fn_make_newton
**Inputs:** name (str), step_fn (Callable). **Outputs:** FnRemainder.

#### fn_make_series
**Inputs:** name (str), term_fn (Callable). **Outputs:** FnRemainder.

---

### primitives/discrete_calculus.py

**Purpose:** 6 discrete calculus builtins.

#### vdr_discrete_derivative
**Inputs:** f (Callable), x (VDRFraction), h (VDRFraction). **Outputs:** VDRFraction.

#### vdr_discrete_derivative_n
**Inputs:** f (Callable), x (VDRFraction), h (VDRFraction), n (int). **Outputs:** VDRFraction.

#### vdr_left_riemann
**Inputs:** f (Callable), a (VDRFraction), b (VDRFraction), n (int). **Outputs:** VDRFraction.

#### vdr_trapezoidal
**Inputs:** f (Callable), a (VDRFraction), b (VDRFraction), n (int). **Outputs:** VDRFraction.

#### vdr_finite_difference_table
**Inputs:** values (List[VDRFraction]). **Outputs:** List[List[VDRFraction]].

#### vdr_richardson_extrapolation
**Inputs:** f (Callable), a (VDRFraction), b (VDRFraction), n1 (int), n2 (int). **Outputs:** VDRFraction.

---

### primitives/denom_mgmt.py

#### vdr_denom_bits
**Inputs:** frac (VDRFraction). **Outputs:** int.

#### vdr_denom_digits
**Inputs:** frac (VDRFraction). **Outputs:** int.

#### vdr_reproject_qbasis
**Inputs:** frac (VDRFraction), exponent (int). **Outputs:** Tuple[VDRFraction, VDRFraction] — (reprojected, error bound).

#### vdr_denom_budget_check
**Inputs:** frac (VDRFraction), budget_bits (int). **Outputs:** bool (True if over budget).

#### vdr_precision_state
**Inputs:** frac (VDRFraction). **Outputs:** Dict — {denom_bits, denom_digits, is_closed, is_active, remainder_depth, node_count}.

---

### primitives/polynomial.py

**Pattern:** Polynomial as List[VDRFraction] (coefficients a_0, a_1, ..., a_n). All pure.

**8 builtins:** poly_eval(coeffs, x), poly_add(a, b), poly_mul(a, b), poly_div(a, b) → Result[Tuple[list, list]], poly_gcd(a, b), poly_derivative(coeffs), poly_integral(coeffs), poly_lagrange_interpolation(xs, ys) → Result[list].

---

### primitives/finite_field.py

**4 builtins:** gf_add(a, b, p), gf_mul(a, b, p), gf_inv(a, p) → Result[int], gf_pow(a, b, p). All int inputs, int output, pure.

---

### primitives/markov.py

**3 builtins:** markov_steady_state(transition_matrix: Mat) → Result[Vec], markov_step(matrix: Mat, state: Vec) → Vec, markov_n_steps(matrix: Mat, state: Vec, n: int) → Vec. All pure.

---

### primitives/graph_math.py

**2 builtins:** adjacency_matrix_power(adj: Mat, n: int) → Mat, pagerank_exact(adj: Mat, damping: VDRFraction) → Vec. All pure.

---

### session/snapshot.py

#### capture_live_state
**Purpose:** Capture all live state from all in-scope KBs into a KBLiveState dict.

**Inputs:** scope_chain (ScopeChain), kb_store. **Outputs:** Dict[int, KBLiveState]. **Side effects:** None. Read-only deep copy.

#### create_snapshot
**Inputs:** name (str), scope_chain, kb_store, scratchpad (RingBuffer), turn (int), notes (str).

**Outputs:** SessionSnapshot.

**Side effects:** Snapshot KB created at root.sessions.{name}.

#### restore_snapshot
**Inputs:** snapshot (SessionSnapshot), kb_store.

**Outputs:** None.

**Side effects:** All live state in all captured KBs overwritten with snapshot values. Scope chain restored.

---

### session/clone.py

#### clone_session
**Purpose:** Create an independent session from a snapshot. The clone gets its own copy of live state but shares persistent KBs.

**Inputs:** source_name (str), clone_name (str), snapshot_store, kb_store.

**Outputs:** None.

**Side effects:** New snapshot created with deep-copied live state. Clone registered.

#### kill_clone
**Purpose:** Destroy a clone's live state. Persistent KB facts asserted by the clone survive.

**Inputs:** clone_name (str), snapshot_store, kb_store.

**Outputs:** None.

**Side effects:** Clone's live state cleared from all its KBs. Clone deregistered.

---

### session/lifecycle.py

#### session_reset
**Purpose:** Clear all live state across all in-scope KBs. Persistent content untouched.

**Inputs:** scope_chain, kb_store.

**Outputs:** None.

**Side effects:** All counters reset, all locks released, all queues/stacks/rings/LRUs/bitsets cleared, scratchpad cleared.

#### session_list
**Inputs:** snapshot_store. **Outputs:** List[str] — snapshot names.

#### session_diff
**Inputs:** name_a (str), name_b (str), snapshot_store. **Outputs:** Dict — added, removed, changed primitives.

#### session_info
**Inputs:** name (str), snapshot_store. **Outputs:** Result[Dict] — metadata. Partial.

---

### inference/notebook.py

#### create_inference_notebook
**Purpose:** Create a new InferenceNotebook (which is a KB with additional schema).

**Inputs:** path (str), problem (str), mode (InferenceMode), goal (str), max_steps (int), max_queries (int), kb_store, registry.

**Outputs:** InferenceNotebook.

**Side effects:** KB created. Standard data primitives (counters, queues, stacks, LRUs, bitsets, lock) initialized per template.

#### notebook_from_template
**Purpose:** Create a notebook from a named template (SRE, bug_investigation, research, decision_matrix, argument, etc.).

**Inputs:** template_name (str), path (str), problem (str), kb_store, registry.

**Outputs:** InferenceNotebook with template-specific schema pre-populated.

**Side effects:** Same as create_inference_notebook.

---

### inference/loop.py

#### assess
**Purpose:** Read the notebook's current state and determine the next action. Checks budget, stall, goal satisfaction.

**Inputs:** notebook (InferenceNotebook), kb_store.

**Outputs:** LoopPhase — the next phase to enter (formalize, conclude, halt, backtrack, branch).

**Side effects:** steps_executed counter incremented. steps_since_evidence incremented.

#### formalize
**Purpose:** Placeholder for the LLM's creative step. In the Python prototype, this is a hook that accepts a callable representing what the LLM would do — write Prolog rules, construct a Python script, or assemble a primitive chain.

**Inputs:** notebook, action_fn (Callable).

**Outputs:** Any — the formalized artifact (list of Facts for rules, str for script, List[CommandToken] for primitives).

**Side effects:** Artifacts may be asserted to notebook KB.

#### execute_step
**Purpose:** Execute the formalized artifact. Delegates to rule_engine (for Prolog), command executor (for primitives), or environment (for scripts).

**Inputs:** artifact (Any), notebook, kb_store, registry, executor.

**Outputs:** Result[Any] — execution result.

**Side effects:** Per the artifact type.

#### store_result
**Purpose:** Persist the execution result into the notebook KB. Update evidence tracking primitives.

**Inputs:** result (Any), notebook, turn (int).

**Outputs:** None.

**Side effects:** KB facts asserted. evidence_count incremented. steps_since_evidence reset. Relevant bitset bits set. LRU updated with finding.

#### run_loop
**Purpose:** Execute the full assess→formalize→execute→store loop until termination. The action_fn parameter is called at each formalize step — in the prototype this is provided by test code, in production it would be the LLM.

**Inputs:** notebook, action_fn (Callable that takes notebook state and returns formalized artifact), kb_store, registry, executor, max_iterations (int).

**Outputs:** InferenceNotebook with conclusion or halt status.

**Side effects:** All loop side effects accumulated.

---

### inference/confidence.py

#### compute_deductive_confidence
**Inputs:** premise_confidences (List[VDRFraction]). **Outputs:** VDRFraction. min(inputs).

#### compute_inductive_confidence
**Inputs:** coverage (VDRFraction), mean_source_confidence (VDRFraction). **Outputs:** VDRFraction. coverage * mean.

#### compute_abductive_confidence
**Inputs:** explained_fraction (VDRFraction), min_evidence_confidence (VDRFraction). **Outputs:** VDRFraction.

#### compute_analogical_confidence
**Inputs:** analogy_strength (VDRFraction), source_confidence (VDRFraction). **Outputs:** VDRFraction. strength * source.

#### propagate_through_chain
**Inputs:** chain (List[Tuple[str, VDRFraction]]) — (step_type, step_confidence) pairs. **Outputs:** VDRFraction — overall chain confidence.

**Side effects:** None. All pure computation.

---

### inference/provenance.py

#### record_evidence
**Purpose:** Create a provenance record for a piece of evidence.

**Inputs:** fact (Fact), source_type (str), confidence (VDRFraction), notebook, turn.

**Outputs:** Dict — the evidence record.

**Side effects:** Evidence record asserted to notebook KB.

#### record_conclusion
**Purpose:** Create the full InferenceConclusion with derivation chain.

**Inputs:** statement (Fact), mode (InferenceMode), confidence (VDRFraction), derived_from (List[str]), via_rules (List[str]), via_tools (List[str]), alternatives (List[Dict]), notebook.

**Outputs:** InferenceConclusion.

**Side effects:** Conclusion asserted to notebook KB.

#### trace_derivation
**Purpose:** Given a conclusion, walk the derivation chain back to raw evidence.

**Inputs:** conclusion_id (str), notebook.

**Outputs:** List[Dict] — ordered chain from evidence to conclusion.

**Side effects:** None. Read-only.

#### challenge_conclusion
**Purpose:** Assert a counter-fact and re-evaluate affected derivation chains.

**Inputs:** counter_fact (Fact), conclusion_id (str), notebook, kb_store.

**Outputs:** Dict — {conclusion_still_holds: bool, new_confidence: VDRFraction, affected_links: List}.

**Side effects:** Counter-fact asserted. Conclusion may be retracted or confidence downgraded.

---

## Stage 4: Full Integration

### env/base.py

#### EnvironmentInterface (abstract class)
**Purpose:** Unified interface for all environment types. Every concrete environment implements these methods.

**Methods:**

#### exec_command
**Inputs:** command (str), args (List[str]). **Outputs:** ExecResult. **Side effects:** Process executed.

#### upload
**Inputs:** content (str), remote_path (str). **Outputs:** bool. **Side effects:** File created in env.

#### download
**Inputs:** remote_path (str). **Outputs:** Result[str]. **Side effects:** None (read-only).

#### file_read
**Inputs:** path (str). **Outputs:** Result[str].

#### file_write
**Inputs:** path (str), content (str). **Outputs:** bool.

#### list_dir
**Inputs:** path (str). **Outputs:** List[str].

#### start_process
**Inputs:** command (str), args (List[str]). **Outputs:** str (task_id).

#### poll_process
**Inputs:** task_id (str). **Outputs:** TaskStatus.

#### get_output
**Inputs:** task_id (str). **Outputs:** Tuple[str, str] (stdout, stderr).

---

### env/local.py

#### LocalEnvironment (implements EnvironmentInterface)
**Purpose:** Execute commands on the local machine. For development and testing. No isolation.

**Fields:** working_dir (str), env_vars (Dict[str, str]), processes (Dict[str, subprocess.Popen]).

All methods delegate to Python subprocess and os modules. Each method logs to the environment's KB.

---

### ops/grants.py

#### GrantStore (class)
**Purpose:** Stores and validates grants. Grants follow the KB hierarchy — inherited from parent KBs.

#### add_grant
**Inputs:** grant (Grant). **Side effects:** Grant stored.

#### verify_grant
**Purpose:** Check if a valid grant covers the requested operation at the requested location.

**Inputs:** operation_class (str), operation_type (str), location (str), user (str).

**Outputs:** Result[Grant] — the matching grant, or error if none found.

**Side effects:** None for check. Grant.use() called on execution.

#### use_grant
**Inputs:** grant (Grant). **Side effects:** uses_remaining decremented. Status may change to EXHAUSTED.

#### list_effective_grants
**Inputs:** user (str), kb_store. **Outputs:** List[Grant] — all grants in user's ancestry chain.

---

### ops/filesystem.py

**Purpose:** 15 filesystem builtins. All operational. All require filesystem grant.

**Pattern:** path (str) input, content or bool or list output, side effects declared, grant verified before execution.

**15 builtins:** fs_read, fs_write, fs_append, fs_exists, fs_list_dir, fs_create_dir, fs_delete, fs_move, fs_copy, fs_file_size, fs_file_modified, fs_glob, fs_tree, fs_diff, fs_checksum.

Each function:
1. Verifies grant via GrantStore.verify_grant.
2. Executes via EnvironmentInterface method.
3. Logs execution to environment KB.
4. Returns Result.

---

### ops/execution.py

**Purpose:** 5 script execution builtins. All operational.

**5 builtins:** exec_python(script_path, env, grant), exec_shell(command, env, grant), exec_zig_test(test_path, env, grant), exec_pytest(test_path, env, grant), exec_script(interpreter, script_path, env, grant).

Each follows same pattern: verify grant, delegate to env.exec_command, log, return ExecResult.

---

### ops/network.py

**Purpose:** 5 network builtins. All operational.

**5 builtins:** net_download(url, local_path, grant), net_fetch(url, grant) → str, net_post(url, body, grant) → str, net_ping(host, grant) → bool, net_dns_resolve(hostname, grant) → str.

Each verifies network grant, executes via Python urllib/socket, logs.

---

### ops/process.py

**Purpose:** 7 process management builtins. All operational.

**7 builtins:** proc_start(command, args, env, grant) → str (task_id), proc_poll(task_id, env) → TaskStatus, proc_wait(task_id, env) → ExecResult, proc_kill(task_id, env, grant), proc_stdout(task_id, env) → str, proc_stderr(task_id, env) → str, proc_list(env) → List[Dict].

---

### inference/modes.py

**Purpose:** Implementations of the four inference mode patterns.

#### run_deductive
**Purpose:** Execute a deductive inference step: assert premises, write rules, query for derivation.

**Inputs:** notebook, premises (List[Fact]), rules (List[Rule]), goal (Fact), kb_store.

**Outputs:** List[Binding] — all satisfying bindings.

**Side effects:** Premises and rules asserted to notebook KB.

#### run_inductive
**Purpose:** Execute an inductive step: gather evidence, write scoring rules, rank hypotheses.

**Inputs:** notebook, evidence (List[Fact]), scoring_rules (List[Rule]), kb_store.

**Outputs:** List[Tuple[str, VDRFraction]] — hypotheses ranked by score.

**Side effects:** Evidence and rules asserted.

#### run_abductive
**Purpose:** Execute an abductive step: assert observations and causal rules, query for explanations.

**Inputs:** notebook, observations (List[Fact]), causal_rules (List[Rule]), kb_store.

**Outputs:** List[str] — possible causes.

**Side effects:** Observations and rules asserted.

#### run_analogical
**Purpose:** Execute an analogical step: assert source and target domain structures, query for mappings.

**Inputs:** notebook, source_facts (List[Fact]), target_facts (List[Fact]), mapping_rules (List[Rule]), kb_store.

**Outputs:** List[Tuple[Fact, VDRFraction]] — transferred conclusions with analogy strength.

**Side effects:** All facts and rules asserted.

---

### lifecycle/data_pipeline.py

#### register_data_source
**Inputs:** name (str), url (str), license (str), source_type (str), kb_store.

**Outputs:** KnowledgeBase (the source KB).

**Side effects:** Source KB created under root.sources.

#### prepare_corpus
**Inputs:** source_kb (KnowledgeBase), filters (List[Callable]), split_ratios (Dict[str, VDRFraction]), kb_store.

**Outputs:** KnowledgeBase (corpus KB).

**Side effects:** Corpus KB created. Transformation log asserted.

#### tokenize_corpus
**Inputs:** corpus_kb (KnowledgeBase), vocab_size (int), kb_store.

**Outputs:** KnowledgeBase (tokenized corpus KB).

**Side effects:** Vocabulary KB created and frozen. Tokenized corpus KB created.

---

### lifecycle/training.py

#### initialize_model
**Inputs:** arch_config (Dict), seed (int), kb_store.

**Outputs:** KnowledgeBase (model KB with initial weights).

**Side effects:** Architecture KB and init KB created. All weights as exact VDR fractions.

#### train_step
**Inputs:** model_kb, train_kb, batch (List), learning_rate (VDRFraction).

**Outputs:** VDRFraction (loss).

**Side effects:** Weights updated. Step logged. Loss asserted. Gradients asserted (if retention policy says so).

#### create_checkpoint
**Inputs:** model_kb, train_kb, step (int), kb_store.

**Outputs:** KnowledgeBase (checkpoint KB).

**Side effects:** Checkpoint KB created with serialized exact weights and optimizer state.

#### restore_checkpoint
**Inputs:** checkpoint_kb, model_kb.

**Outputs:** None.

**Side effects:** Model weights overwritten with checkpoint values. Idempotent.

---

### lifecycle/evaluation.py

#### run_benchmark
**Inputs:** checkpoint_kb, benchmark_name (str), test_data (List), env (EnvironmentInterface), kb_store.

**Outputs:** Dict — {metric_name: VDRFraction} for each measured metric.

**Side effects:** Evaluation KB created with results.

#### run_eval_suite
**Inputs:** checkpoint_kb, suite (List[str] benchmark names), test_data_map (Dict), env, kb_store.

**Outputs:** KnowledgeBase (eval suite KB).

**Side effects:** One eval result KB per benchmark. Suite KB created linking them.

#### compare_checkpoints
**Inputs:** eval_kb_a, eval_kb_b.

**Outputs:** Dict — {benchmark: {metric: (score_a, score_b, delta)}}.

**Side effects:** None.

---

## Stage 5: Production Completion

### env/docker.py

#### DockerEnvironment (implements EnvironmentInterface)
**Purpose:** Manage Docker containers as sandboxed execution environments.

**Additional fields:** image (str), container_id (str), mount_points (List[Tuple[str, str]]), startup_script (str).

**Additional methods:**

#### create_container
**Inputs:** image, working_dir, mounts, env_vars, resource_limits. **Outputs:** str (container_id). **Side effects:** Container created.

#### start_container
**Side effects:** Container started. Startup script executed.

#### stop_container
**Side effects:** Container stopped gracefully.

#### destroy_container
**Side effects:** Container removed. KB archived.

---

### env/ssh.py

#### SSHEnvironment (implements EnvironmentInterface)
**Purpose:** Execute commands on remote machines via SSH.

**Additional fields:** host, port, username, key_ref, connection.

All EnvironmentInterface methods delegate to SSH commands via paramiko or subprocess ssh.

---

### env/vm.py

#### VMEnvironment (implements EnvironmentInterface)
**Purpose:** Manage virtual machines as execution environments.

**Additional fields:** provider (str), vm_id (str), vm_image (str), cpus (int), memory_mb (int).

---

### ops/compilation.py

**4 builtins:** compile_python_check(source, env, grant), compile_zig(source, output, env, grant), compile_c(source, output, env, grant), compile_rust(source, output, env, grant).

Each verifies compile grant, delegates to env.exec_command with the appropriate compiler, logs, returns ExecResult.

---

### ops/linting.py

**8 builtins:** lint_python, lint_zig, lint_json, lint_markdown, analyze_imports, analyze_complexity, analyze_dependencies, count_lines.

Each verifies lint grant (read-only), delegates, logs, returns analysis results.

---

### lifecycle/feedback.py

#### create_feedback_round
**Inputs:** model_version (str), annotator_count (int), kb_store.

**Outputs:** KnowledgeBase (feedback KB).

**Side effects:** Feedback KB created with schema.

#### add_pairwise_judgment
**Inputs:** feedback_kb, prompt (str), response_a (str), response_b (str), preferred (str), annotator (str), confidence (str), time_spent (int).

**Outputs:** None.

**Side effects:** Judgment fact asserted to feedback KB.

#### compute_agreement
**Inputs:** feedback_kb.

**Outputs:** VDRFraction (Cohen's kappa as exact fraction from integer counts).

**Side effects:** None.

#### train_reward_model
**Inputs:** feedback_kb, base_checkpoint_kb, training_config (Dict), kb_store.

**Outputs:** KnowledgeBase (reward model KB).

**Side effects:** Reward model training run KB created.

#### run_dpo
**Inputs:** feedback_kb, base_checkpoint_kb, config (Dict), kb_store.

**Outputs:** KnowledgeBase (aligned checkpoint KB).

**Side effects:** DPO training run KB created.

---

### lifecycle/deployment.py

#### create_deployment
**Inputs:** checkpoint_kb, env (EnvironmentInterface), config (Dict), kb_store.

**Outputs:** KnowledgeBase (deployment KB).

**Side effects:** Deployment KB created. Model loaded into env.

#### create_canary
**Inputs:** deployment_kb, percentage (VDRFraction), duration_hours (int), promotion_criteria (Dict), kb_store.

**Outputs:** KnowledgeBase (canary KB).

**Side effects:** Canary KB created. Traffic splitting configured.

#### promote_canary
**Inputs:** canary_kb, kb_store. **Side effects:** Canary promoted to full deployment. Old deployment deactivated.

#### rollback
**Inputs:** deployment_kb, target_checkpoint (str), kb_store. **Side effects:** Current deployment deactivated. Target checkpoint loaded. Rollback event logged.

#### retire_model
**Inputs:** model_kb, reason (str), successor (str), kb_store. **Side effects:** Retirement KB created. Model KBs archived. Frozen but queryable.

---

### lifecycle/monitoring.py

#### create_monitoring
**Inputs:** deployment_kb, kb_store.

**Outputs:** KnowledgeBase (monitoring KB).

**Side effects:** Monitoring KB created with default watches.

#### add_watch
**Inputs:** monitoring_kb, name (str), condition (str), action (str).

**Side effects:** Watch fact asserted.

#### check_watches
**Purpose:** Evaluate all active watches against current metrics.

**Inputs:** monitoring_kb, kb_store.

**Outputs:** List[Dict] — triggered watches with details.

**Side effects:** Triggered watch facts asserted.

#### record_metric
**Inputs:** monitoring_kb, metric_name (str), value (VDRFraction), timestamp (int).

**Side effects:** Metric fact asserted.

#### detect_drift
**Inputs:** monitoring_kb, baseline_metrics (Dict), current_metrics (Dict).

**Outputs:** List[Dict] — metrics that have drifted beyond thresholds.

**Side effects:** Drift events asserted if detected.

---

## Summary

| Stage | New Functions | Cumulative Functions | New Modules | Cumulative Modules |
|-------|-------------|---------------------|-------------|-------------------|
| 1 | ~180 | ~180 | 24 | 24 |
| 2 | ~160 | ~340 | 13 | 37 |
| 3 | ~90 | ~430 | 12 | 49 |
| 4 | ~70 | ~500 | 9 | 58 |
| 5 | ~50 | ~550 | 7 | 65 |

Every function has declared inputs, outputs, and side effects. Every function is testable by providing declared inputs and verifying declared outputs. Every side effect is observable and loggable. The IOSE declarations are the test specifications and the Zig port specifications simultaneously.

---

**END FUNCTION IOSE SPECIFICATION**
