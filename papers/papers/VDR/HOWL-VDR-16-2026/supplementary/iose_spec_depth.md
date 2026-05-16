# VDR-LLM-Prolog Implementation Technical Specification
## Five-Stage Build Plan from Toy to Production

**Document:** implementation_tech_spec.md
**Version:** 1.0
**Date:** May 2026
**Scope:** Complete build plan for VDR-LLM-Prolog system
**Language:** Python 3.8 prototype → Zig 0.15.1 production

---

## 1. Build Philosophy

### 1.1 Comprehensive Then Incremental

The specification is comprehensive — VDR-1 through VDR-10 define the whole system. The build is incremental — five stages, each producing a testable, runnable system that does more than the last. At no stage is the system incomplete in the aggregated sense — each stage is a complete, internally consistent system that handles a full lifecycle at its level of capability.

### 1.2 Python First, Zig Final

Python 3.8 is the prototype language. It has the existing VDR-1 through VDR-4 codebase (vdr.py, active_mul.py, fn.py, linalg.py, export.py, softmax.py, autodiff.py, nn.py, losses.py, optim.py, rng.py, init.py, sampling.py, datasets.py, metrics.py, checkpoint.py, basis.py, tensor.py, attention.py, transformer.py, trainer.py, exp.py, logarithm.py). The prototype validates every design decision. The final implementation in Zig 0.15.1 is a port of the validated prototype — same interfaces, same tests, better performance and memory characteristics.

Python dataclasses map cleanly to Zig structs. Python dicts map to Zig HashMaps. Python lists map to Zig ArrayLists. Python enums map to Zig enums. The prototype is designed for portability from the start.

### 1.3 IOSE Throughout

Every module, every class, every function is an IOSE node. Inputs, outputs, side effects declared. This discipline starts at Stage 1 and never relaxes. The IOSE declarations ARE the test specifications — test each node by providing declared inputs, verifying declared outputs, confirming declared side effects.

---

## 2. Module Map

The complete system has 40 modules organized in 10 layers. Each module is listed with its stage of introduction and its IOSE summary.

```
vdr_llm_prolog/
├── core/                          # Stage 1: Foundation
│   ├── vdr.py                     # [EXISTS] VDR triple, closed arithmetic, normalization
│   ├── active_mul.py              # [EXISTS] Active multiplication/division
│   ├── fn.py                      # [EXISTS] Functional remainders, discrete calculus
│   ├── linalg.py                  # [EXISTS] Vec, Mat, det, inv, solve
│   ├── types.py                   # [STAGE 1] Number type hierarchy, dispatch
│   └── errors.py                  # [STAGE 1] Error types, result wrapper
│
├── kb/                            # Stage 1: Knowledge Base
│   ├── knowledge_base.py          # [STAGE 1] KB struct with all fields
│   ├── fact_store.py              # [STAGE 1] Fact assertion, retraction, query
│   ├── rule_engine.py             # [STAGE 1] Prolog-style unification, backtracking
│   ├── constraint_engine.py       # [STAGE 2] Constraint checking, enforcement
│   ├── scope_resolver.py          # [STAGE 2] Scope chain walking, inheritance
│   └── working_data.py            # [STAGE 1] Scoped variable bindings
│
├── path/                          # Stage 2: Addressing
│   ├── registry.py                # [STAGE 2] Path-to-ID mapping, slot IDs
│   ├── resolver.py                # [STAGE 2] Dotted path resolution, relative paths
│   └── mount.py                   # [STAGE 3] Mount system, cycle detection
│
├── primitives/                    # Stage 1-3: Builtins
│   ├── text.py                    # [STAGE 1] 17 string operations
│   ├── collections.py             # [STAGE 1] 36 list operations
│   ├── arithmetic.py              # [STAGE 1] VDR closed arithmetic builtins (wraps core/vdr.py)
│   ├── active_arithmetic.py       # [STAGE 2] VDR active arithmetic builtins
│   ├── structure_ops.py           # [STAGE 2] Lift, rebase, scalar projection
│   ├── comparison.py              # [STAGE 1] VDR comparison and ordering
│   ├── rounding.py                # [STAGE 1] Floor, ceil, round, extraction
│   ├── number_theory.py           # [STAGE 2] GCD, LCM, modular ops, combinatorics
│   ├── list_aggregates.py         # [STAGE 1] Sum, product, mean, dot product
│   ├── qbasis.py                  # [STAGE 3] Q335 transcendental operations
│   ├── functional.py              # [STAGE 3] sqrt, exp, log, sin, cos, resolve
│   ├── discrete_calculus.py       # [STAGE 3] Derivative, integral, finite difference
│   ├── sets.py                    # [STAGE 1] 14 set operations
│   ├── mappings.py                # [STAGE 1] 15 dict operations
│   ├── linalg_builtins.py         # [STAGE 2] Linear algebra builtins (wraps core/linalg.py)
│   ├── statistics.py              # [STAGE 2] Mean, variance, percentile, softmax
│   ├── probability.py             # [STAGE 2] Bayes, normalize, CDF, joint
│   ├── conversion.py              # [STAGE 1] Type conversion, parse_json, format
│   ├── time_ops.py                # [STAGE 2] Date arithmetic, day-of-week
│   ├── identity.py                # [STAGE 2] Hash, base64, hex, CRC32, UUID
│   ├── graphs.py                  # [STAGE 2] BFS, DFS, shortest path, PageRank
│   ├── logic.py                   # [STAGE 1] if/case/for_each/try_catch/findall
│   ├── integer_ops.py             # [STAGE 1] Fast integer path, bit operations
│   ├── denom_mgmt.py              # [STAGE 3] Denominator tracking, reprojection
│   ├── polynomial.py              # [STAGE 3] Horner, poly arithmetic, Lagrange
│   ├── finite_field.py            # [STAGE 3] GF(p) operations
│   ├── markov.py                  # [STAGE 3] Steady state, step, n-step
│   └── graph_math.py              # [STAGE 3] Adjacency power, exact PageRank
│
├── data_primitives/               # Stage 1-2: Runtime State
│   ├── counter.py                 # [STAGE 1] Bounded counter
│   ├── lock.py                    # [STAGE 1] Non-blocking lock
│   ├── lru.py                     # [STAGE 2] LRU cache
│   ├── queue.py                   # [STAGE 1] Bounded FIFO queue
│   ├── stack.py                   # [STAGE 1] Bounded LIFO stack
│   ├── ring_buffer.py             # [STAGE 2] Fixed-size circular buffer
│   └── bitset.py                  # [STAGE 2] Fixed-width bit array
│
├── command/                       # Stage 2-3: Command Tokens
│   ├── token_types.py             # [STAGE 2] CommandToken, CommandType enums
│   ├── parser.py                  # [STAGE 2] Parse command token stream
│   ├── executor.py                # [STAGE 2] Dispatch to primitives
│   └── scratchpad.py              # [STAGE 2] Internal computation channel
│
├── session/                       # Stage 3: Session Management
│   ├── snapshot.py                # [STAGE 3] Capture/restore live state
│   ├── clone.py                   # [STAGE 3] Fork independent sessions
│   └── lifecycle.py               # [STAGE 3] Reset, kill, drift detection
│
├── inference/                     # Stage 3-4: Orchestrated Inference
│   ├── notebook.py                # [STAGE 3] Inference notebook KB schema
│   ├── loop.py                    # [STAGE 3] Assess/formalize/execute/store loop
│   ├── modes.py                   # [STAGE 4] Deductive, inductive, abductive, analogical
│   ├── confidence.py              # [STAGE 3] Confidence propagation
│   └── provenance.py              # [STAGE 3] Derivation chain, challenge mechanism
│
├── env/                           # Stage 4-5: Operational Environments
│   ├── base.py                    # [STAGE 4] Unified environment interface
│   ├── docker.py                  # [STAGE 5] Docker container management
│   ├── local.py                   # [STAGE 4] Local execution (dev/test)
│   ├── ssh.py                     # [STAGE 5] SSH remote execution
│   └── vm.py                      # [STAGE 5] VM management
│
├── ops/                           # Stage 4-5: Operational Primitives
│   ├── filesystem.py              # [STAGE 4] 15 file operations
│   ├── compilation.py             # [STAGE 5] Compile Python/Zig/C/Rust
│   ├── execution.py               # [STAGE 4] Run scripts
│   ├── linting.py                 # [STAGE 5] Lint, analyze, count
│   ├── network.py                 # [STAGE 4] fetch, post, download
│   ├── process.py                 # [STAGE 4] Background process management
│   └── grants.py                  # [STAGE 4] Positive credential grant system
│
├── lifecycle/                     # Stage 4-5: Model Lifecycle
│   ├── data_pipeline.py           # [STAGE 4] Source registry, corpus prep
│   ├── training.py                # [STAGE 4] Training orchestration (wraps VDR-4 trainer)
│   ├── feedback.py                # [STAGE 5] Collection, reward model, alignment
│   ├── evaluation.py              # [STAGE 4] Benchmark running, result KB
│   ├── deployment.py              # [STAGE 5] Serving config, API layer
│   └── monitoring.py              # [STAGE 5] Runtime metrics, watches, drift
│
├── iose/                          # Stage 1: IOSE Infrastructure
│   ├── registry.py                # [STAGE 1] IOSE declaration storage and query
│   ├── validator.py               # [STAGE 2] Type checking, SE preview, contract verify
│   └── principles.py              # [STAGE 1] OSO principles KB loading
│
└── tests/                         # All stages
    ├── test_stage1/               # Stage 1 tests
    ├── test_stage2/               # Stage 2 tests
    ├── test_stage3/               # Stage 3 tests
    ├── test_stage4/               # Stage 4 tests
    └── test_stage5/               # Stage 5 tests
```

---

## 3. Core Data Structures

These dataclasses are the foundation. Everything builds on them. They are introduced in Stage 1 and never change shape — only gain methods in later stages.

### 3.1 Number Types

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Callable, Tuple, Any
from enum import Enum
from fractions import Fraction


# VDR triple — the ground truth numeric type
# Wraps the existing VDR class from core/vdr.py
# This dataclass is the IOSE-declared interface layer

class RemainderForm(Enum):
    ZERO = "zero"           # Closed object, R=0
    ATOMIC = "atomic"       # Single integer remainder
    COMPOSITE = "composite" # Base integer + child VDR list
    FUNCTIONAL = "functional" # Callable f(depth)->VDR


@dataclass
class VDRFraction:
    """Exact rational number as VDR triple [V, D, R].
    Primary numeric type. Ground truth for all computation."""
    v: int                              # Numerator (arbitrary precision)
    d: int                              # Denominator (nonzero, arbitrary precision)
    r: Any = 0                          # Remainder: 0, int, CompositeRemainder, or FnRemainder

    def is_closed(self) -> bool:
        return self.r == 0

    def is_active(self) -> bool:
        return self.r != 0

    def is_integer(self) -> bool:
        return self.r == 0 and self.d == 1

    def to_fraction(self) -> Fraction:
        """Scalar projection for closed objects."""
        if self.is_closed():
            return Fraction(self.v, self.d)
        raise ValueError("Cannot project active object without resolving remainder")


@dataclass
class CompositeRemainder:
    """Integer base plus finite list of child VDR triples."""
    base: int
    children: List['VDRFraction'] = field(default_factory=list)


@dataclass
class FnRemainder:
    """Callable producing exact VDR at each depth."""
    name: str
    fn: Callable[[int], 'VDRFraction']
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class QBasis:
    """Single integer over shared power-of-two denominator."""
    numerator: int      # Arbitrary precision integer
    exponent: int       # The k in 2^k denominator

    def to_vdr(self) -> VDRFraction:
        return VDRFraction(v=self.numerator, d=2**self.exponent, r=0)
```

### 3.2 IOSE Declaration

```python
class IOSECategory(Enum):
    PURE = "pure"
    OPERATIONAL = "operational"
    COMPOSITE = "composite"


class LogicType(Enum):
    OPERATIONAL = "operational"
    APPLICATION = "application"


@dataclass
class IOSEProperty:
    """A named property with optional value."""
    name: str                   # deterministic, bounded, idempotent, etc.
    value: Any = True


@dataclass
class IOSEDeclaration:
    """Input/Output/Side-Effect declaration for any component."""
    name: str
    inputs: List[str]           # Type names
    outputs: List[str]          # Type names
    side_effects: List[str]     # Declared effect names
    properties: List[IOSEProperty] = field(default_factory=list)
    category: IOSECategory = IOSECategory.PURE
    logic_type: LogicType = LogicType.OPERATIONAL
    description: str = ""

    def is_pure(self) -> bool:
        return self.category == IOSECategory.PURE

    def has_property(self, name: str) -> bool:
        return any(p.name == name for p in self.properties)
```

### 3.3 KB Struct

```python
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


@dataclass
class Constraint:
    name: str
    scope: str = "operational"      # axiom, operational, legal, project, conversation
    status: str = "active"          # active, suspended, violated, satisfied
    condition: str = ""             # Prolog condition as string
    on_violation: str = "warn"      # warn, block, error, escalate
    source: str = ""


@dataclass
class Counter:
    value: int = 0
    min_value: int = 0
    max_value: int = 2**31 - 1
    created_at: int = 0

    def inc(self) -> int:
        self.value = min(self.value + 1, self.max_value)
        return self.value

    def dec(self) -> int:
        self.value = max(self.value - 1, self.min_value)
        return self.value

    def add(self, delta: int) -> int:
        self.value = max(self.min_value, min(self.value + delta, self.max_value))
        return self.value

    def reset(self):
        self.value = self.min_value

    def set(self, value: int):
        self.value = max(self.min_value, min(value, self.max_value))


@dataclass
class LockState:
    held: bool = False
    holder: Optional[str] = None
    acquired_at: Optional[int] = None
    notes: str = ""

    def acquire(self, holder: str, turn: int = 0, notes: str = "") -> bool:
        if self.held:
            return False
        self.held = True
        self.holder = holder
        self.acquired_at = turn
        self.notes = notes
        return True

    def release(self):
        self.held = False
        self.holder = None
        self.acquired_at = None
        self.notes = ""

    def force_release(self):
        self.release()


@dataclass
class BoundedQueue:
    capacity: int = 50
    items: List[Any] = field(default_factory=list)
    created_at: int = 0

    def push(self, item: Any) -> bool:
        if len(self.items) >= self.capacity:
            return False
        self.items.append(item)
        return True

    def pop(self) -> Optional[Any]:
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self) -> Optional[Any]:
        if not self.items:
            return None
        return self.items[0]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) >= self.capacity

    def clear(self):
        self.items.clear()

    def to_list(self) -> List[Any]:
        return list(self.items)


@dataclass
class BoundedStack:
    capacity: int = 30
    items: List[Any] = field(default_factory=list)
    created_at: int = 0

    def push(self, item: Any) -> bool:
        if len(self.items) >= self.capacity:
            return False
        self.items.append(item)
        return True

    def pop(self) -> Optional[Any]:
        if not self.items:
            return None
        return self.items.pop()

    def peek(self) -> Optional[Any]:
        if not self.items:
            return None
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def clear(self):
        self.items.clear()

    def to_list(self) -> List[Any]:
        return list(reversed(self.items))


@dataclass
class RingBuffer:
    capacity: int = 100
    items: List[Any] = field(default_factory=list)
    write_pos: int = 0
    count: int = 0
    created_at: int = 0

    def write(self, item: Any):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.write_pos] = item
        self.write_pos = (self.write_pos + 1) % self.capacity
        self.count = min(self.count + 1, self.capacity)

    def read_all(self) -> List[Any]:
        if self.count < self.capacity:
            return list(self.items)
        start = self.write_pos
        return self.items[start:] + self.items[:start]

    def read_last(self, n: int) -> List[Any]:
        all_items = self.read_all()
        return all_items[-n:] if n < len(all_items) else all_items

    def size(self) -> int:
        return self.count

    def clear(self):
        self.items.clear()
        self.write_pos = 0
        self.count = 0


@dataclass
class Bitset:
    width: int = 100
    bits: List[bool] = field(default_factory=list)
    created_at: int = 0

    def __post_init__(self):
        if not self.bits:
            self.bits = [False] * self.width

    def set(self, index: int):
        if 0 <= index < self.width:
            self.bits[index] = True

    def clear_bit(self, index: int):
        if 0 <= index < self.width:
            self.bits[index] = False

    def test(self, index: int) -> bool:
        if 0 <= index < self.width:
            return self.bits[index]
        return False

    def count(self) -> int:
        return sum(self.bits)

    def all_set(self) -> bool:
        return all(self.bits)

    def any_set(self) -> bool:
        return any(self.bits)

    def reset(self):
        self.bits = [False] * self.width

    def to_list(self) -> List[int]:
        return [i for i, b in enumerate(self.bits) if b]


# --- Fact and Rule structures for the Prolog engine ---

@dataclass
class Fact:
    predicate: str
    args: List[Any]
    kb_source: str = ""
    asserted_at: int = 0
    derivation: Optional[Any] = None


@dataclass
class Rule:
    head: Fact
    body: List[Fact]
    kb_source: str = ""


# --- The KB struct ---

@dataclass
class KnowledgeBase:
    # Identity
    name: str
    path: str
    id: int

    # Persistent knowledge
    facts: List[Fact] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)

    # Live state
    working_data: Dict[str, Any] = field(default_factory=dict)
    lrus: Dict[str, Any] = field(default_factory=dict)
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)
    queues: Dict[str, BoundedQueue] = field(default_factory=dict)
    stacks: Dict[str, BoundedStack] = field(default_factory=dict)
    buffers: Dict[str, RingBuffer] = field(default_factory=dict)
    bitsets: Dict[str, Bitset] = field(default_factory=dict)

    # Structural
    parent_id: Optional[int] = None
    children_ids: List[int] = field(default_factory=list)
    mounts: List[Mount] = field(default_factory=list)

    # Metadata
    visibility: Visibility = Visibility.PUBLIC
    frozen: bool = False
    owner: Optional[str] = None
    created_at: int = 0
    last_modified: int = 0
    iose_declaration: Optional[IOSEDeclaration] = None
```

### 3.4 Session Snapshot

```python
@dataclass
class KBLiveState:
    """Captured live state of one KB. Persistent facts NOT included."""
    kb_id: int
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)
    lrus: Dict[str, Any] = field(default_factory=dict)
    queues: Dict[str, BoundedQueue] = field(default_factory=dict)
    stacks: Dict[str, BoundedStack] = field(default_factory=dict)
    buffers: Dict[str, RingBuffer] = field(default_factory=dict)
    bitsets: Dict[str, Bitset] = field(default_factory=dict)
    working_data: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SessionSnapshot:
    """Atomic capture of all live state."""
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

### 3.5 Command Token

```python
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

### 3.6 Inference Notebook

```python
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
    """An inference notebook is a KB with additional schema fields.
    The notebook IS a KnowledgeBase — these fields are stored as
    facts and data primitives within the KB."""
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

### 3.7 Grant

```python
class GrantStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    EXHAUSTED = "exhausted"


@dataclass
class Grant:
    name: str
    operation_class: str        # filesystem, compile, execute, network, process
    allowed_operations: List[str]
    location: str               # path prefix or URL pattern
    issued_by: str = ""
    issued_at: int = 0
    expires_at: int = 2**31 - 1
    max_uses: int = 0           # 0 = unlimited
    uses_remaining: int = 0
    status: GrantStatus = GrantStatus.ACTIVE

    def is_valid(self) -> bool:
        return (self.status == GrantStatus.ACTIVE and
                (self.max_uses == 0 or self.uses_remaining > 0))

    def use(self) -> bool:
        if not self.is_valid():
            return False
        if self.max_uses > 0:
            self.uses_remaining -= 1
            if self.uses_remaining <= 0:
                self.status = GrantStatus.EXHAUSTED
        return True
```

---

## 4. Builtin Registration Pattern

Every builtin follows the same pattern. Define once, apply to all 448.

```python
# --- The Builtin Registry ---

@dataclass
class BuiltinDef:
    """Definition of a single builtin primitive."""
    id: int
    name: str
    category: str
    iose: IOSEDeclaration
    implementation: Callable      # The actual function
    

class BuiltinRegistry:
    """Global registry of all builtins. Loaded at startup."""

    def __init__(self):
        self._by_id = {}          # int -> BuiltinDef
        self._by_name = {}        # str -> BuiltinDef

    def register(self, builtin_def: BuiltinDef):
        self._by_id[builtin_def.id] = builtin_def
        self._by_name[builtin_def.name] = builtin_def

    def get_by_id(self, builtin_id: int) -> Optional[BuiltinDef]:
        return self._by_id.get(builtin_id)

    def get_by_name(self, name: str) -> Optional[BuiltinDef]:
        return self._by_name.get(name)

    def all_in_category(self, category: str) -> List[BuiltinDef]:
        return [b for b in self._by_id.values() if b.category == category]

    def count(self) -> int:
        return len(self._by_id)


# --- Registration macro pattern ---
# Every primitive module uses this pattern:

REGISTRY = BuiltinRegistry()


def register_builtin(builtin_id, name, category, inputs, outputs,
                     side_effects, properties, description, impl):
    """Helper to register a builtin with full IOSE declaration."""
    iose = IOSEDeclaration(
        name=name,
        inputs=inputs,
        outputs=outputs,
        side_effects=side_effects,
        properties=[IOSEProperty(p) for p in properties],
        category=IOSECategory.PURE if not side_effects or
                 all(se.startswith("kb_") or se.startswith("counter_") or
                     se.startswith("lru_") or se.startswith("queue_") or
                     se.startswith("stack_") or se.startswith("ring_") or
                     se.startswith("lock_") or se.startswith("bitset_") or
                     se.startswith("mutation_") or se.startswith("primitive_") or
                     se.startswith("scope_") or se.startswith("constraint_") or
                     se.startswith("connection_") or se.startswith("mount_") or
                     se.startswith("id_") or se.startswith("live_") or
                     se.startswith("clone_") or se.startswith("snapshot_")
                     for se in side_effects)
                 else IOSECategory.OPERATIONAL,
        description=description,
    )
    REGISTRY.register(BuiltinDef(
        id=builtin_id,
        name=name,
        category=category,
        iose=iose,
        implementation=impl,
    ))


# --- Example: registering text builtins ---
# All 17 text builtins follow this exact pattern:

def _string_reverse(s: str) -> str:
    return s[::-1]

def _string_length(s: str) -> int:
    return len(s)

def _string_concat(a: str, b: str) -> str:
    return a + b

# ... etc for all 17 ...

def register_text_builtins(registry: BuiltinRegistry):
    """Register all 17 text builtins. Same pattern for each."""

    TEXT_BUILTINS = [
        # (id, name, inputs, outputs, properties, description, impl)
        (1, "string_reverse", ["atom"], ["atom"],
         ["pure", "deterministic", "bounded", "invertible"],
         "Reverse character order", _string_reverse),
        (2, "string_length", ["atom"], ["number"],
         ["pure", "deterministic", "bounded"],
         "Character count", _string_length),
        (3, "string_concat", ["atom", "atom"], ["atom"],
         ["pure", "deterministic", "bounded", "associative"],
         "Concatenation", _string_concat),
        # ... 14 more entries ...
    ]

    for bid, name, inputs, outputs, props, desc, impl in TEXT_BUILTINS:
        register_builtin(bid, name, "text", inputs, outputs,
                        [], props, desc, impl)


# --- Pattern declaration for bulk registration ---
# Categories that follow the exact same registration pattern:
#
# SAME PATTERN (table-driven registration, pure, no side effects):
#   text (17), collections (36), sets (14), mappings (15),
#   comparison (10), rounding (4), extraction (7),
#   integer_ops (13), bit_ops (8), conversion (14+11),
#   time_ops (10), identity (8), logic (11)
#
# SAME PATTERN (table-driven, pure, KB-internal side effects):
#   kb_ops (15), data_primitives (53), path_mount (17), session (8)
#
# SAME PATTERN (table-driven, VDR arithmetic wrapping core/vdr.py):
#   closed_arithmetic (8), active_arithmetic (5), structure_ops (3),
#   list_aggregates (8), number_theory (13)
#
# SAME PATTERN (table-driven, wrapping core/linalg.py):
#   linalg_builtins (24)
#
# SAME PATTERN (table-driven, wrapping existing ML modules):
#   statistics (16), probability (included in statistics)
#
# SAME PATTERN (table-driven, operational, require grant):
#   filesystem (15), compilation (4), execution (5),
#   linting (8), network (5), process (7)
#
# DOMAIN-SPECIFIC (slightly different construction):
#   qbasis (7), functional (8), discrete_calculus (6),
#   polynomial (8), finite_field (4), markov (3),
#   graph_math (2), denom_mgmt (5)
```

---

## 5. The Five Stages

### 5.1 Stage 1: Toy Full Lifecycle

**Goal:** A system that can create KBs, assert and query facts, run basic Prolog rules, use data primitives, execute VDR arithmetic, and demonstrate one complete lifecycle pass (initialize model → train 1 step → checkpoint → evaluate → report). Everything works. Nothing is fast. Nothing scales. But the full loop exists.

**Modules activated:**

```
core/vdr.py              [EXISTS]
core/active_mul.py       [EXISTS]
core/linalg.py           [EXISTS]
core/types.py            [NEW — type hierarchy, VDRFraction wrapper, dispatch]
core/errors.py           [NEW — Result type, error codes]

kb/knowledge_base.py     [NEW — KB struct with all fields]
kb/fact_store.py         [NEW — assert, retract, query by predicate scan]
kb/rule_engine.py        [NEW — basic unification, depth-first search, backtracking]
kb/working_data.py       [NEW — scoped key-value bindings]

primitives/arithmetic.py     [NEW — wraps vdr.py: add, sub, mul, div, neg, abs, pow, reciprocal]
primitives/comparison.py     [NEW — compare, equal, lt, le, min, max, sign, is_zero]
primitives/rounding.py       [NEW — floor, ceil, round, truncate, numerator, denominator, simplify]
primitives/list_aggregates.py [NEW — sum, product, mean, dot_product]
primitives/text.py           [NEW — 17 string ops]
primitives/collections.py   [NEW — 36 list ops]
primitives/sets.py           [NEW — 14 set ops]
primitives/mappings.py       [NEW — 15 dict ops]
primitives/conversion.py    [NEW — to_string, parse_json, format_json, parse_csv, to/from fraction]
primitives/logic.py          [NEW — if_then_else, for_each, try_catch, findall, assert_that]
primitives/integer_ops.py    [NEW — int add/sub/mul/div/mod, range, bit ops]

data_primitives/counter.py       [NEW]
data_primitives/lock.py          [NEW]
data_primitives/queue.py         [NEW]
data_primitives/stack.py         [NEW]

iose/registry.py         [NEW — IOSE declaration storage]
iose/principles.py       [NEW — OSO axioms, core facts, priority rules]
```

**IOSE for Stage 1 as a whole:**

```
Inputs: Python API calls (no command tokens yet)
Outputs: Query results, computation results, checkpoint data
Side Effects: KB mutations, file writes (checkpoint)
Properties: deterministic, exact arithmetic, basic lifecycle
```

**What the toy lifecycle does:**

```python
# 1. Create root KB and model KB
root_kb = create_kb("root", "root", 0)
model_kb = create_kb("model", "root.model", 1, parent_id=0)

# 2. Assert architecture facts
assert_fact(model_kb, Fact("model_type", ["transformer_decoder"]))
assert_fact(model_kb, Fact("hidden_dim", [2]))
assert_fact(model_kb, Fact("vocab_size", [3]))

# 3. Initialize tiny model (wrapping VDR-4 existing code)
# 2-dim, 3-vocab, 1-layer, 1-head
weights = initialize_xavier(model_kb, seed=42)

# 4. Create training KB
train_kb = create_kb("train", "root.train", 2, parent_id=0)
train_kb.counters["step"] = Counter(min_value=0, max_value=100)

# 5. One training step (wrapping VDR-4 trainer)
loss = train_step(model_kb, train_kb, batch)
train_kb.counters["step"].inc()
assert_fact(train_kb, Fact("loss_at", [0, loss]))

# 6. Checkpoint (serialize VDR fractions to dict)
checkpoint = snapshot_model(model_kb, step=1)
assert_fact(train_kb, Fact("checkpoint", [1, checkpoint]))

# 7. Evaluate (run forward pass on test input)
result = evaluate(model_kb, test_input)
eval_kb = create_kb("eval", "root.eval", 3, parent_id=0)
assert_fact(eval_kb, Fact("accuracy", [result.accuracy]))

# 8. Report
query_result = query_facts(eval_kb, "accuracy")
print("Accuracy:", query_result)

# Full lifecycle: init → train → checkpoint → evaluate → report
# Every value is exact. Every fact is in a KB. Every step is logged.
```

**Test count target:** 150 tests
- Core arithmetic: 30 (wrapping existing, verifying IOSE interface)
- KB operations: 30 (assert, retract, query, rules, unification)
- Data primitives: 20 (counter, lock, queue, stack)
- Text/collections/sets/mappings: 40 (3 per builtin minimum)
- Lifecycle integration: 10 (the full loop)
- IOSE registry: 10 (registration, lookup, declaration query)
- OSO principles: 10 (priority rules, knowability facts)

---

### 5.2 Stage 2: Upgraded Toy

**Goal:** Add command tokens, path addressing, constraint engine, scope resolution, the full comparison and statistics builtins, and a scratchpad. The system can now process command token streams instead of just Python API calls. It has real scoping — switching topics activates and deactivates KBs. It has constraints that fire on violations. Still toy-sized data, but the architecture is real.

**New modules activated:**

```
kb/constraint_engine.py  [NEW — check constraints, enforce on_violation]
kb/scope_resolver.py     [NEW — scope chain walking, inheritance, shadowing]

path/registry.py         [NEW — path-to-ID, slot IDs]
path/resolver.py         [NEW — dotted path resolution, relative paths]

command/token_types.py   [NEW — CommandToken, CommandType]
command/parser.py        [NEW — parse text+command stream]
command/executor.py      [NEW — dispatch to primitives via IOSE registry]
command/scratchpad.py    [NEW — RingBuffer-based scratchpad]

primitives/active_arithmetic.py  [NEW — wraps active_mul.py]
primitives/structure_ops.py      [NEW — lift, rebase, projection]
primitives/number_theory.py      [NEW — GCD, LCM, mod, factorial, binomial, etc.]
primitives/linalg_builtins.py    [NEW — wraps linalg.py with IOSE]
primitives/statistics.py         [NEW — mean, variance, softmax, normalize]
primitives/probability.py        [NEW — Bayes, CDF, joint, conditional]
primitives/time_ops.py           [NEW — date arithmetic]
primitives/identity.py           [NEW — hash, base64, hex, CRC32]
primitives/graphs.py             [NEW — BFS, DFS, shortest path, components]

data_primitives/lru.py           [NEW]
data_primitives/ring_buffer.py   [NEW]
data_primitives/bitset.py        [NEW]

iose/validator.py        [NEW — type check chains, SE preview, contract verify]
```

**What Stage 2 adds to the lifecycle:**

```python
# Command tokens instead of direct API calls
tokens = [
    CommandToken(CommandType.KB_ASSERT, "kb_assert",
        args=[CommandArg(ArgType.PATH_REF, "root.model"),
              CommandArg(ArgType.LITERAL_TEXT, "hidden_dim(2)")]),
    CommandToken(CommandType.PURE_FN, "vdr_add",
        args=[CommandArg(ArgType.PATH_REF, "root.train.loss_step_0"),
              CommandArg(ArgType.LITERAL_FRACTION, (1, 10))]),
    CommandToken(CommandType.KB_QUERY, "kb_query",
        args=[CommandArg(ArgType.PATH_REF, "root.eval"),
              CommandArg(ArgType.LITERAL_TEXT, "accuracy")]),
]

# Scratchpad for intermediate computation
scratchpad = RingBuffer(capacity=100)

# Scope resolution
activate_scope("root.model")  # model KB in scope
result = scoped_query("hidden_dim")  # finds it in model KB
activate_scope("root.train")  # switch scope
result = scoped_query("hidden_dim")  # NOT found (different scope)

# Constraints fire
constraint = Constraint("loss_finite", "axiom", "active",
    "loss_at(_, L), L < 1000", "halt_training")
add_constraint(train_kb, constraint)
violations = check_all_constraints(train_kb)
```

**Test count target:** +200 (cumulative 350)
- Command token parsing and execution: 40
- Path registry and resolution: 30
- Scope resolver with inheritance: 30
- Constraint engine: 20
- New builtins (active arith, number theory, linalg, stats, probability, time, identity, graphs): 60
- New data primitives (LRU, ring, bitset): 20

---

### 5.3 Stage 3: Capacity Building

**Goal:** Add session management, inference notebooks, Q-basis and functional remainder operations, discrete calculus, domain-specific math, denominator management, the mount system, and basic inference loop. The system can now snapshot and clone sessions, conduct simple orchestrated inference, manage transcendental constants, and track denominator growth. Still running locally, no Docker, no network ops.

**New modules activated:**

```
path/mount.py                [NEW]

primitives/qbasis.py         [NEW]
primitives/functional.py     [NEW]
primitives/discrete_calculus.py [NEW]
primitives/denom_mgmt.py     [NEW]
primitives/polynomial.py     [NEW]
primitives/finite_field.py   [NEW]
primitives/markov.py         [NEW]
primitives/graph_math.py     [NEW]

session/snapshot.py          [NEW]
session/clone.py             [NEW]
session/lifecycle.py         [NEW]

inference/notebook.py        [NEW]
inference/loop.py            [NEW]
inference/confidence.py      [NEW]
inference/provenance.py      [NEW]
```

**What Stage 3 adds:**

```python
# Session snapshot and clone
session_snapshot("stable_operator_v1", notes="verified working state")
session_clone("stable_operator_v1", "worker_001")
# ... worker does investigation ...
session_kill("worker_001")
session_clone("stable_operator_v1", "worker_002")

# Inference notebook
notebook = create_inference_notebook(
    path="root.inference.test_001",
    problem="Why did loss increase at step 50?",
    mode=InferenceMode.ABDUCTIVE,
    goal="root_cause(_, confidence > 80/100)")

# Basic inference loop
while notebook.status == NotebookStatus.ACTIVE:
    step = assess(notebook)       # read KB state, decide next action
    artifact = formalize(step)    # write Prolog rules or primitive chain
    result = execute(artifact)    # run the formalized step
    store(notebook, result)       # persist to KB
    # Budget and stall checks happen automatically

# Q-basis operations
pi = qbasis_get_constant("pi")    # Q335 representation
e = qbasis_get_constant("e")
pi_plus_e = qbasis_add(pi, e)     # one integer addition

# Functional remainder
sqrt2 = fn_sqrt(VDRFraction(2, 1, 0), depth=7)  # ~150 digits

# Denominator management
bits = vdr_denom_bits(some_weight)
if bits > 48:
    reprojected, error = vdr_reproject_qbasis(some_weight, 48)
```

**Test count target:** +250 (cumulative 600)
- Session snapshot/restore/clone/kill: 30
- Inference notebook and loop: 40
- Confidence propagation: 20
- Q-basis operations: 20
- Functional remainder (sqrt, exp, log, sin, cos): 30
- Discrete calculus: 20
- Domain math (polynomial, finite field, Markov, graph math): 40
- Mount system: 20
- Denominator management: 15
- Integration (inference + session + math): 15

---

### 5.4 Stage 4: Full Integration

**Goal:** Add operational environments (local first), grants, filesystem operations, script execution, process management, network operations, the complete inference mode system (deductive, inductive, abductive, analogical), and the lifecycle pipeline (data sources, corpus, training orchestration, evaluation). The system can now execute code in sandboxes, fetch external data, manage the full model lifecycle, and conduct multi-mode orchestrated inference.

**New modules activated:**

```
env/base.py              [NEW]
env/local.py             [NEW]

ops/filesystem.py        [NEW]
ops/execution.py         [NEW]
ops/network.py           [NEW]
ops/process.py           [NEW]
ops/grants.py            [NEW]

inference/modes.py       [NEW — all four modes with tool signatures]

lifecycle/data_pipeline.py [NEW]
lifecycle/training.py      [NEW — wraps VDR-4 trainer with KB integration]
lifecycle/evaluation.py    [NEW]
```

**What Stage 4 adds:**

```python
# Grants
grant = Grant("dev_fs", "filesystem", ["read", "write"],
    location="/workspace/", issued_by="admin")
grant_store.add(grant)

# Filesystem operations (local env)
content = fs_read("/workspace/test.py", grant="dev_fs")
fs_write("/workspace/output.txt", "results here", grant="dev_fs")

# Script execution
result = exec_python("/workspace/test.py", env="local", grant="dev_exec")

# Network (fetch Prometheus data)
raw = net_fetch("http://prometheus:9090/api/v1/query?...", grant="monitoring")
parsed = parse_json(raw)
metric = vdr_from_decimal_string(dict_get(parsed, "value"))

# Four inference modes
notebook.mode = InferenceMode.ABDUCTIVE
# ... LLM writes causal rules, queries for explanations ...
notebook.mode = InferenceMode.INDUCTIVE
# ... scores hypotheses against gathered evidence ...
notebook.mode = InferenceMode.DEDUCTIVE
# ... derives implications of leading hypothesis ...

# Full lifecycle pipeline
source_kb = register_data_source("wikipedia", url, license="CC-BY-SA")
corpus_kb = prepare_corpus(source_kb, filters=[language, quality, dedup])
tokenized_kb = tokenize_corpus(corpus_kb, vocab_size=32000)
model_kb = initialize_model(arch_config)
training_kb = train(model_kb, tokenized_kb, config)
eval_kb = evaluate(training_kb.latest_checkpoint, benchmarks)
```

**Test count target:** +300 (cumulative 900)
- Grant system: 20
- Filesystem ops: 30
- Script execution: 20
- Network ops: 15
- Process management: 15
- Inference modes (all four): 40
- Lifecycle pipeline (source → corpus → tokenize → train → eval): 60
- Local environment: 20
- Integration (inference + ops + lifecycle): 40
- IOSE contract verification across all components: 40

---

### 5.5 Stage 5: Production Completion

**Goal:** Add Docker and SSH environments, compilation primitives, linting, feedback collection, reward modeling, deployment configuration, monitoring, canary deployment, rollback, retirement. The system is complete — every feature specified in VDR-1 through VDR-10 is implemented.

**New modules activated:**

```
env/docker.py            [NEW]
env/ssh.py               [NEW]
env/vm.py                [NEW]

ops/compilation.py       [NEW]
ops/linting.py           [NEW]

lifecycle/feedback.py    [NEW]
lifecycle/deployment.py  [NEW]
lifecycle/monitoring.py  [NEW]
```

**What Stage 5 adds:**

```python
# Docker environment
env = create_docker_env("test_env", image="python:3.8-slim",
    startup_script="pip install pytest")
env_exec(env, "python3 test.py")

# SSH remote
env = create_ssh_env("gpu_01", host="gpu01.lab.example.com",
    username="alice", key_ref="ssh_key_alice")
env_exec(env, "python3 train.py --config finetune_v2")

# Compilation
result = compile_zig("src/main.zig", "build/main")

# Linting
issues = lint_python("src/module.py")
complexity = analyze_complexity("src/module.py")

# Feedback collection
feedback_kb = create_feedback_round(model_version="checkpoint_safe_v1")
add_pairwise_judgment(feedback_kb, prompt, response_a, response_b,
    preferred="a", annotator="human_42")

# Deployment
deploy_config = create_deployment(checkpoint="checkpoint_safe_v1",
    env="prod_cluster", rate_limit=100)

# Canary
canary = create_canary(deploy_config, percentage=5, duration_hours=24,
    promotion_criteria={"latency_delta": "<10%", "error_delta": "<1%"})

# Monitoring
monitor_kb = create_monitoring(deploy_config)
add_watch(monitor_kb, "latency_spike", "p99_latency > 5000", "alert")

# Rollback
rollback(deploy_config, target="previous_deployment")

# Retirement
retire_model("checkpoint_safe_v1", reason="superseded by v3",
    successor="checkpoint_safe_v3")
```

**Test count target:** +350 (cumulative 1250)
- Docker environment: 40
- SSH environment: 30
- VM environment: 20
- Compilation: 15
- Linting: 20
- Feedback collection: 30
- Deployment: 30
- Monitoring: 30
- Canary and rollback: 25
- Retirement: 15
- Full lifecycle integration: 40
- End-to-end: raw data → trained → deployed → monitored → updated → retired: 25
- Zig port preparation: type mapping verification: 30

---

## 6. Stage Deliverables Summary

| Stage | Name | Modules | Builtins Active | Tests | Key Capability |
|-------|------|---------|----------------|-------|---------------|
| 1 | Toy Full Lifecycle | 24 | ~150 | 150 | KB + facts + rules + basic arithmetic + data primitives + toy lifecycle loop |
| 2 | Upgraded Toy | 37 | ~300 | 350 | Command tokens + paths + scope + constraints + statistics + graphs + scratchpad |
| 3 | Capacity Building | 49 | ~400 | 600 | Sessions + inference notebooks + Q-basis + functional + discrete calc + domain math + mounts |
| 4 | Full Integration | 58 | ~420 | 900 | Local environments + grants + filesystem + network + execution + all inference modes + lifecycle pipeline |
| 5 | Production | 65 | 448 | 1250 | Docker + SSH + compilation + linting + feedback + deployment + monitoring + canary + retirement |

---

## 7. Cross-Stage Invariants

These hold at every stage. They are never relaxed.

| Invariant | Description | Verified By |
|-----------|-------------|-------------|
| IOSE declared | Every function has an IOSE declaration before implementation | Registry check at startup |
| Exact arithmetic | Every numeric operation uses VDR fractions or exact integers | Type system enforcement |
| KB is truth | All persistent state lives in KBs, not in module globals | Audit of module state |
| Data primitives bounded | Every counter, queue, stack, ring, LRU, bitset has declared capacity | Constructor enforcement |
| No silent truncation | Every precision reduction is declared with exact error bound | Conversion boundary logging |
| Tests pass | All tests from current and prior stages pass | CI run |
| OSO principles loaded | The root.system.oso KB is loaded and constraints are active | Startup check |
| Idempotent where declared | Operations tagged idempotent verify f(f(x)) = f(x) | Dedicated idempotency tests |
| One way | Each task category has one canonical builtin | Registry uniqueness check |

---

## 8. Zig Port Strategy

The Python prototype is designed for Zig portability:

| Python Construct | Zig Equivalent | Mapping Difficulty |
|-----------------|---------------|-------------------|
| dataclass | struct | Direct |
| Dict[str, T] | std.StringHashMap(T) | Direct |
| List[T] | std.ArrayList(T) | Direct |
| Optional[T] | ?T | Direct |
| Enum | enum | Direct |
| int (arbitrary precision) | Custom BigInt or i128 with overflow to BigInt | Medium |
| Fraction | VDR [V, D, R] with i128 or BigInt | The core of the system |
| str | []const u8 or std.ArrayList(u8) | Direct |
| bool | bool | Direct |
| Callable | fn pointer or interface | Slightly different pattern |
| try/except | error union with errdefer | Different pattern, same semantics |
| dict comprehension | loop with put | Mechanical translation |
| list comprehension | loop with append | Mechanical translation |

The Zig port happens after Stage 5 validates the complete system in Python. The port is mechanical — same IOSE interfaces, same tests, same behavior. The IOSE declarations serve as the Zig interface specifications.

---

## 9. File Listing per Stage

### Stage 1 Files (24 files)

```
vdr_llm_prolog/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── vdr.py                  # [EXISTS — copy from VDR-4]
│   ├── active_mul.py           # [EXISTS — copy from VDR-4]
│   ├── fn.py                   # [EXISTS — copy from VDR-4]
│   ├── linalg.py               # [EXISTS — copy from VDR-4]
│   ├── types.py                # ~200 lines
│   └── errors.py               # ~50 lines
├── kb/
│   ├── __init__.py
│   ├── knowledge_base.py       # ~150 lines (the KB struct)
│   ├── fact_store.py           # ~200 lines
│   ├── rule_engine.py          # ~400 lines (unification + backtracking)
│   └── working_data.py         # ~100 lines
├── primitives/
│   ├── __init__.py
│   ├── arithmetic.py           # ~150 lines (wraps vdr.py)
│   ├── comparison.py           # ~100 lines
│   ├── rounding.py             # ~80 lines
│   ├── list_aggregates.py      # ~80 lines
│   ├── text.py                 # ~200 lines
│   ├── collections.py          # ~400 lines
│   ├── sets.py                 # ~150 lines
│   ├── mappings.py             # ~150 lines
│   ├── conversion.py           # ~200 lines
│   ├── logic.py                # ~150 lines
│   └── integer_ops.py          # ~150 lines
├── data_primitives/
│   ├── __init__.py
│   ├── counter.py              # ~40 lines (already in KB struct)
│   ├── lock.py                 # ~40 lines
│   ├── queue.py                # ~50 lines
│   └── stack.py                # ~50 lines
├── iose/
│   ├── __init__.py
│   ├── registry.py             # ~150 lines
│   └── principles.py           # ~200 lines
└── tests/
    └── test_stage1/
        ├── test_arithmetic.py
        ├── test_kb.py
        ├── test_rules.py
        ├── test_data_primitives.py
        ├── test_text.py
        ├── test_collections.py
        ├── test_sets.py
        ├── test_mappings.py
        ├── test_conversion.py
        ├── test_logic.py
        ├── test_integer_ops.py
        ├── test_lifecycle_toy.py
        ├── test_iose_registry.py
        └── test_principles.py
```

**Estimated new code for Stage 1:** ~2,800 lines (excluding existing VDR-4 code)

### Stage 2 Additions (~3,200 new lines)

```
├── kb/
│   ├── constraint_engine.py    # ~250 lines
│   └── scope_resolver.py       # ~200 lines
├── path/
│   ├── __init__.py
│   ├── registry.py             # ~200 lines
│   └── resolver.py             # ~150 lines
├── primitives/
│   ├── active_arithmetic.py    # ~100 lines
│   ├── structure_ops.py        # ~120 lines
│   ├── number_theory.py        # ~250 lines
│   ├── linalg_builtins.py      # ~200 lines
│   ├── statistics.py           # ~200 lines
│   ├── probability.py          # ~200 lines
│   ├── time_ops.py             # ~150 lines
│   ├── identity.py             # ~120 lines
│   └── graphs.py               # ~300 lines
├── data_primitives/
│   ├── lru.py                  # ~80 lines
│   ├── ring_buffer.py          # ~60 lines
│   └── bitset.py               # ~60 lines
├── command/
│   ├── __init__.py
│   ├── token_types.py          # ~80 lines
│   ├── parser.py               # ~200 lines
│   ├── executor.py             # ~250 lines
│   └── scratchpad.py           # ~60 lines
└── iose/
    └── validator.py            # ~200 lines
```

### Stage 3 Additions (~3,000 new lines)

```
├── path/
│   └── mount.py                # ~200 lines
├── primitives/
│   ├── qbasis.py               # ~200 lines
│   ├── functional.py           # ~250 lines
│   ├── discrete_calculus.py    # ~200 lines
│   ├── denom_mgmt.py           # ~100 lines
│   ├── polynomial.py           # ~250 lines
│   ├── finite_field.py         # ~100 lines
│   ├── markov.py               # ~150 lines
│   └── graph_math.py           # ~100 lines
├── session/
│   ├── __init__.py
│   ├── snapshot.py             # ~200 lines
│   ├── clone.py                # ~150 lines
│   └── lifecycle.py            # ~150 lines
└── inference/
    ├── __init__.py
    ├── notebook.py             # ~200 lines
    ├── loop.py                 # ~300 lines
    ├── confidence.py           # ~150 lines
    └── provenance.py           # ~200 lines
```

### Stage 4 Additions (~3,500 new lines)

```
├── env/
│   ├── __init__.py
│   ├── base.py                 # ~200 lines
│   └── local.py                # ~300 lines
├── ops/
│   ├── __init__.py
│   ├── filesystem.py           # ~300 lines
│   ├── execution.py            # ~200 lines
│   ├── network.py              # ~200 lines
│   ├── process.py              # ~250 lines
│   └── grants.py               # ~200 lines
├── inference/
│   └── modes.py                # ~400 lines
└── lifecycle/
    ├── __init__.py
    ├── data_pipeline.py        # ~300 lines
    ├── training.py             # ~400 lines
    └── evaluation.py           # ~250 lines
```

### Stage 5 Additions (~3,000 new lines)

```
├── env/
│   ├── docker.py               # ~400 lines
│   ├── ssh.py                  # ~300 lines
│   └── vm.py                   # ~200 lines
├── ops/
│   ├── compilation.py          # ~150 lines
│   └── linting.py              # ~200 lines
└── lifecycle/
    ├── feedback.py             # ~350 lines
    ├── deployment.py           # ~400 lines
    └── monitoring.py           # ~400 lines
```

---

## 10. Total Estimates

| Metric | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 | Total |
|--------|---------|---------|---------|---------|---------|-------|
| New code (lines) | 2,800 | 3,200 | 3,000 | 3,500 | 3,000 | 15,500 |
| Existing code reused | ~5,000 | — | — | — | — | ~5,000 |
| New modules | 24 | 13 | 12 | 9 | 7 | 65 |
| Tests | 150 | 200 | 250 | 300 | 350 | 1,250 |
| Builtins active | ~150 | ~300 | ~400 | ~420 | 448 | 448 |
| Cumulative tests | 150 | 350 | 600 | 900 | 1,250 | 1,250 |

The complete Python prototype is approximately 20,500 lines including existing VDR-4 code — a manageable codebase for one or two developers, staged across five increments that each produce a testable, runnable system.

---

## 11. Falsification Criteria

**F1.** If any stage's tests pass but the IOSE declarations do not match actual behavior, the IOSE model is decorative rather than functional.

**F2.** If any stage introduces a builtin without an IOSE declaration, the comprehensive discipline has been violated.

**F3.** If any stage's system cannot execute its declared lifecycle capability end-to-end (toy lifecycle in Stage 1, full lifecycle in Stage 5), the stage is incomplete.

**F4.** If the Zig port of any component produces different results from the Python prototype for the same inputs, the port has a correctness bug.

**F5.** If the cumulative test count at any stage is less than the target, the test coverage is insufficient for the claims made at that stage.

---

**END IMPLEMENTATION TECHNICAL SPECIFICATION**
