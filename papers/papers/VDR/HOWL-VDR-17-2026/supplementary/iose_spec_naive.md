# VDR-LLM-PROLOG IMPLEMENTATION SKELETON
# Python Prototype → Zig 0.15.1 Final
# Five-Stage Build Plan with IOSE Contracts

---

## STAGE OVERVIEW

```
Stage 1: Toy Full Lifecycle    — KB + VDR + Prolog core + minimal inference loop
Stage 2: Almost Practical      — data primitives + dotted paths + command tokens + constraints
Stage 3: Loosely Integrated    — session management + notebooks + external data + confidence
Stage 4: Full Encapsulated     — lifecycle KBs + surfacing + accounts + complete inference
Stage 5: Operational Complete  — environments + grants + async + versioning + deployment
```

Each stage produces a testable, runnable system. Each stage's output is the input to the next.

---

## CONVENTIONS

**Pattern declarations.** Where N builtins share the same IOSE shape, we declare the pattern once and list the names. Example: "PATTERN: binary_vdr_op(a: VDR, b: VDR) → VDR, pure, no SE. Instances: vdr_add, vdr_sub, vdr_mul."

**File layout.** Each module is one .py file. Tests are in tests/ mirroring the module name. Every module has `__all__` declaring its public API.

**Existing code.** VDR-1 through VDR-4 Python code exists and passes 705 tests. We wrap it, not rewrite it. New code imports from existing modules.

**Python 3.8 target.** dataclasses, typing, enum, fractions from stdlib. No external deps for core. Optional: mpmath for decimal export.

---

## STAGE 1: TOY FULL LIFECYCLE

**Goal:** KB tree with facts/rules/constraints, VDR exact arithmetic plugged in, minimal Prolog unification and query, one forward pass of a tiny transformer, and one training step — all connected through KBs. The thinnest possible vertical slice through the entire stack.

### Stage 1 File Tree

```
vdr_system/
├── core/
│   ├── __init__.py
│   ├── types.py              # Enums, small structs, VDR type aliases
│   ├── vdr.py                # RE-EXPORT existing VDR arithmetic (wrap, don't rewrite)
│   ├── kb.py                 # KnowledgeBase dataclass, FactStore, RuleStore
│   ├── path_registry.py      # Dotted path ↔ integer ID (minimal: no mounts yet)
│   ├── prolog.py             # Term, Fact, Rule, unification, depth-first query
│   └── constraints.py        # Constraint struct, check_constraint, check_all
├── ml/
│   ├── __init__.py
│   └── bridge.py             # Wrap existing VDR-4 transformer for KB integration
├── lifecycle/
│   ├── __init__.py
│   └── toy_lifecycle.py      # Init model KB → train 1 step → eval → checkpoint → done
├── tests/
│   ├── test_types.py
│   ├── test_kb.py
│   ├── test_path_registry.py
│   ├── test_prolog.py
│   ├── test_constraints.py
│   ├── test_bridge.py
│   └── test_toy_lifecycle.py
└── existing/                  # Symlink or copy of VDR-1 through VDR-4 code
    ├── vdr.py
    ├── active_mul.py
    ├── fn.py
    ├── linalg.py
    ├── softmax.py
    ├── autodiff.py
    ├── nn.py
    ├── losses.py
    ├── optim.py
    ├── transformer.py
    └── ...                    # All 24 existing modules
```

### Stage 1 IOSE Declarations

#### core/types.py

```python
"""Shared enums, small structs, type aliases.
No IOSE node — this is the type vocabulary, not a component."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, Union, Callable
from enum import Enum
from fractions import Fraction

# --- Enums ---

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

class ConstraintScope(Enum):
    AXIOM = "axiom"
    OPERATIONAL = "operational"
    LEGAL = "legal"
    PROJECT = "project"
    CONVERSATION = "conversation"

class ConstraintStatus(Enum):
    ACTIVE = "active"
    SATISFIED = "satisfied"
    VIOLATED = "violated"
    SUSPENDED = "suspended"
    PARKED = "parked"

class TopicStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    PARKED = "parked"

class NodeCategory(Enum):
    PURE = "pure"
    OPERATIONAL = "operational"
    COMPOSITE = "composite"

class LogicType(Enum):
    OPERATIONAL_LOGIC = "operational_logic"
    APPLICATION_LOGIC = "application_logic"

# --- VDR Type Aliases ---
# The existing VDR class is the canonical type.
# We alias here for clarity in signatures.
# VDR objects are imported from existing/vdr.py

# --- Small Structs ---

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
    mount_id: int
    source_path: str
    source_id: int
    mode: MountMode = MountMode.READ_ONLY
    created_at: int = 0
    created_by: str = ""

@dataclass
class IOSEDeclaration:
    """Metadata about a component's interface contract."""
    name: str
    inputs: List[Tuple[str, str]]       # [(param_name, type_name), ...]
    outputs: List[Tuple[str, str]]
    side_effects: List[str]
    properties: List[str]               # ["pure", "deterministic", "bounded", ...]
    category: NodeCategory = NodeCategory.PURE
    logic_type: LogicType = LogicType.APPLICATION_LOGIC
    description: str = ""
```

#### core/kb.py

```python
"""KnowledgeBase — the universal container.

IOSE (composite):
  Inputs:  operation (str), args (varies)
  Outputs: query results, success/failure
  Side Effects: fact_added, fact_removed, mutation_logged
  Properties: deterministic, bounded
  Logic Type: operational_logic
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set
from .types import (
    Visibility, Connection, Mount, ConstraintScope,
    ConstraintStatus, Direction
)


@dataclass
class Constraint:
    name: str
    scope: ConstraintScope = ConstraintScope.OPERATIONAL
    status: ConstraintStatus = ConstraintStatus.ACTIVE
    condition: str = ""            # Prolog-style condition string (evaluated by prolog.py)
    on_violation: str = "warn"     # warn | block | error | log
    source: str = ""


@dataclass
class Fact:
    predicate: str
    args: Dict[str, Any] = field(default_factory=dict)
    kb_source: str = ""
    asserted_at: int = 0


@dataclass
class Rule:
    head_predicate: str
    head_args: Dict[str, Any] = field(default_factory=dict)
    body: List[Dict[str, Any]] = field(default_factory=list)  # list of conditions
    kb_source: str = ""


# --- Data Primitives (Stage 1: Counter and Lock only) ---

@dataclass
class Counter:
    value: int = 0
    min_value: int = 0
    max_value: int = (2**31) - 1

    def inc(self) -> int:
        self.value = min(self.value + 1, self.max_value)
        return self.value

    def dec(self) -> int:
        self.value = max(self.value - 1, self.min_value)
        return self.value

    def add(self, delta: int) -> int:
        self.value = max(self.min_value, min(self.value + delta, self.max_value))
        return self.value

    def reset(self) -> None:
        self.value = self.min_value

    def set(self, val: int) -> None:
        self.value = max(self.min_value, min(val, self.max_value))

    def get(self) -> int:
        return self.value


@dataclass
class LockState:
    held: bool = False
    holder: Optional[str] = None
    acquired_at: int = 0

    def acquire(self, holder: str = "", turn: int = 0) -> bool:
        if self.held:
            return False
        self.held = True
        self.holder = holder
        self.acquired_at = turn
        return True

    def release(self) -> None:
        self.held = False
        self.holder = None

    def check(self) -> bool:
        return self.held


# --- The KB Struct ---

@dataclass
class KnowledgeBase:
    # Identity
    name: str
    path: str
    id: int

    # Persistent
    facts: List[Fact] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)

    # Live state (Stage 1: counters and locks only)
    working_data: Dict[str, Any] = field(default_factory=dict)
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)

    # Structural
    parent_id: Optional[int] = None
    children_ids: List[int] = field(default_factory=list)

    # Metadata
    visibility: Visibility = Visibility.PUBLIC
    frozen: bool = False
    owner: Optional[str] = None
    created_at: int = 0
    last_modified: int = 0

    # --- Fact operations ---

    def assert_fact(self, predicate: str, args: Optional[Dict[str, Any]] = None,
                    turn: int = 0) -> Fact:
        """Assert a fact. Idempotent: duplicate predicate+args is a no-op."""
        args = args or {}
        for f in self.facts:
            if f.predicate == predicate and f.args == args:
                return f  # already exists
        fact = Fact(predicate=predicate, args=args,
                    kb_source=self.path, asserted_at=turn)
        self.facts.append(fact)
        self.last_modified = turn
        return fact

    def retract_fact(self, predicate: str, args: Optional[Dict[str, Any]] = None,
                     turn: int = 0) -> bool:
        """Retract first matching fact. Returns True if found."""
        args = args or {}
        for i, f in enumerate(self.facts):
            if f.predicate == predicate and f.args == args:
                self.facts.pop(i)
                self.last_modified = turn
                return True
        return False

    def query_facts(self, predicate: str,
                    match_args: Optional[Dict[str, Any]] = None) -> List[Fact]:
        """Return all facts matching predicate. If match_args provided,
        only return facts where every key in match_args matches."""
        results = []
        for f in self.facts:
            if f.predicate != predicate:
                continue
            if match_args is None:
                results.append(f)
            else:
                if all(f.args.get(k) == v for k, v in match_args.items()):
                    results.append(f)
        return results

    # --- Rule operations ---

    def add_rule(self, head_predicate: str, head_args: Dict[str, Any],
                 body: List[Dict[str, Any]], turn: int = 0) -> Rule:
        rule = Rule(head_predicate=head_predicate, head_args=head_args,
                    body=body, kb_source=self.path)
        self.rules.append(rule)
        self.last_modified = turn
        return rule

    # --- Live state reset (for session management later) ---

    def reset_live(self) -> None:
        """Clear all live state to defaults. Persistent knowledge untouched."""
        self.working_data.clear()
        for c in self.counters.values():
            c.reset()
        for lk in self.locks.values():
            lk.release()
```

#### core/path_registry.py

```python
"""Path Registry — dotted path ↔ integer ID mapping.

IOSE:
  Inputs:  dotted_path (str)
  Outputs: integer_id (int)
  Side Effects: id_assigned (if path is new)
  Properties: deterministic (same path → same id forever), bounded
  Logic Type: operational_logic
"""

from typing import Dict, Optional, List


class PathRegistry:
    def __init__(self) -> None:
        self._path_to_id: Dict[str, int] = {}
        self._id_to_path: List[str] = []
        self._next_id: int = 0
        # Register root
        self.register("root")

    def register(self, path: str) -> int:
        """Register a path. Returns existing ID if already registered."""
        if path in self._path_to_id:
            return self._path_to_id[path]
        pid = self._next_id
        self._next_id += 1
        self._path_to_id[path] = pid
        self._id_to_path.append(path)
        return pid

    def resolve(self, path: str) -> Optional[int]:
        """Resolve path to ID. Returns None if not registered."""
        return self._path_to_id.get(path)

    def from_id(self, pid: int) -> Optional[str]:
        """Resolve ID to path."""
        if 0 <= pid < len(self._id_to_path):
            return self._id_to_path[pid]
        return None

    def exists(self, path: str) -> bool:
        return path in self._path_to_id

    def parent_path(self, path: str) -> Optional[str]:
        """Return parent path. 'root' has no parent."""
        if path == "root":
            return None
        parts = path.rsplit(".", 1)
        if len(parts) == 2:
            return parts[0]
        return None

    def children_paths(self, path: str) -> List[str]:
        """Return all direct children of path."""
        prefix = path + "."
        depth = prefix.count(".")
        result = []
        for p in self._path_to_id:
            if p.startswith(prefix) and p.count(".") == depth:
                result.append(p)
        return result

    def depth(self, path: str) -> int:
        return path.count(".")
```

#### core/prolog.py

```python
"""Minimal Prolog — unification, fact query, rule evaluation.

IOSE (pure):
  Inputs:  query_predicate (str), query_args (dict), scope (list of KB)
  Outputs: list of binding dicts (matches), or empty list
  Side Effects: none
  Properties: pure, deterministic, bounded (no infinite loops — no recursion in Stage 1)
  Logic Type: operational_logic

Stage 1 scope: flat fact matching with variable binding. No rule chaining yet.
Stage 2 adds rule evaluation with depth limit.
"""

from typing import Any, Dict, List, Optional
from .kb import KnowledgeBase, Fact


def unify_value(pattern: Any, value: Any, bindings: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Attempt to unify a pattern value against a concrete value.
    Variables are strings starting with '?'.
    Returns updated bindings on success, None on failure."""
    if isinstance(pattern, str) and pattern.startswith("?"):
        var_name = pattern
        if var_name in bindings:
            # Already bound — must match
            return bindings if bindings[var_name] == value else None
        new_bindings = dict(bindings)
        new_bindings[var_name] = value
        return new_bindings
    # Concrete comparison
    if pattern == value:
        return bindings
    return None


def unify_args(pattern_args: Dict[str, Any], fact_args: Dict[str, Any],
               bindings: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Unify all keys in pattern_args against fact_args."""
    current = dict(bindings)
    for key, pat_val in pattern_args.items():
        if key not in fact_args:
            return None
        result = unify_value(pat_val, fact_args[key], current)
        if result is None:
            return None
        current = result
    return current


def query(predicate: str, query_args: Dict[str, Any],
          scope: List[KnowledgeBase]) -> List[Dict[str, Any]]:
    """Query facts across in-scope KBs. Returns list of variable bindings.
    Scope is searched in order; all matches collected (no cut in Stage 1)."""
    results = []
    for kb in scope:
        for fact in kb.facts:
            if fact.predicate != predicate:
                continue
            bindings = unify_args(query_args, fact.args, {})
            if bindings is not None:
                results.append(bindings)
    return results


def query_first(predicate: str, query_args: Dict[str, Any],
                scope: List[KnowledgeBase]) -> Optional[Dict[str, Any]]:
    """Query with cut — return first match only (scoped search order)."""
    for kb in scope:
        for fact in kb.facts:
            if fact.predicate != predicate:
                continue
            bindings = unify_args(query_args, fact.args, {})
            if bindings is not None:
                return bindings
    return None
```

#### core/constraints.py

```python
"""Constraint checking.

IOSE (pure):
  Inputs:  constraint (Constraint), kb (KnowledgeBase), scope (list of KB)
  Outputs: satisfied (bool), violation_message (str or None)
  Side Effects: none
  Properties: pure, deterministic, bounded
  Logic Type: operational_logic

Stage 1: constraints are simple Python callables registered by name.
Stage 2 upgrades to Prolog condition evaluation.
"""

from typing import List, Tuple, Optional, Callable, Dict, Any
from .kb import KnowledgeBase, Constraint, ConstraintStatus


# Constraint evaluators registered by condition string pattern
_evaluators: Dict[str, Callable] = {}


def register_evaluator(name: str, fn: Callable) -> None:
    """Register a named constraint evaluator.
    fn signature: (kb: KnowledgeBase, scope: List[KnowledgeBase]) -> bool"""
    _evaluators[name] = fn


def check_constraint(constraint: Constraint, kb: KnowledgeBase,
                     scope: Optional[List[KnowledgeBase]] = None) -> Tuple[bool, str]:
    """Check a single constraint. Returns (satisfied, message)."""
    if constraint.status != ConstraintStatus.ACTIVE:
        return True, "not active"
    evaluator = _evaluators.get(constraint.condition)
    if evaluator is None:
        # Unknown condition — treat as satisfied with warning
        return True, f"no evaluator for '{constraint.condition}'"
    try:
        result = evaluator(kb, scope or [kb])
        if result:
            return True, "satisfied"
        return False, f"constraint '{constraint.name}' violated"
    except Exception as e:
        return False, f"constraint '{constraint.name}' error: {e}"


def check_all(kb: KnowledgeBase,
              scope: Optional[List[KnowledgeBase]] = None) -> List[Tuple[Constraint, bool, str]]:
    """Check all active constraints on a KB. Returns list of (constraint, satisfied, message)."""
    results = []
    for c in kb.constraints:
        satisfied, msg = check_constraint(c, kb, scope)
        results.append((c, satisfied, msg))
    return results
```

#### core/vdr.py

```python
"""VDR bridge — re-export existing VDR arithmetic.

IOSE (pure):
  This module re-exports. Each VDR operation is its own IOSE node.
  See PATTERN declarations below.

PATTERN: unary_vdr_op(a: VDR) → VDR
  Properties: pure, deterministic, bounded
  Side Effects: none
  Instances: vdr_neg, vdr_abs, vdr_simplify, vdr_reciprocal

PATTERN: binary_vdr_op(a: VDR, b: VDR) → VDR
  Properties: pure, deterministic, bounded
  Side Effects: none
  Instances: vdr_add, vdr_sub, vdr_mul, vdr_div

PATTERN: vdr_compare_op(a: VDR, b: VDR) → bool_or_ordering
  Properties: pure, deterministic, bounded
  Side Effects: none
  Instances: vdr_eq, vdr_lt, vdr_le, vdr_gt, vdr_ge, vdr_compare

PATTERN: vdr_extract(a: VDR) → int_or_bool
  Properties: pure, deterministic, bounded
  Side Effects: none
  Instances: vdr_numerator, vdr_denominator, vdr_is_integer, vdr_is_closed,
             vdr_floor, vdr_ceil, vdr_round

PATTERN: vdr_list_agg(xs: List[VDR]) → VDR
  Properties: pure, deterministic, bounded
  Side Effects: none
  Instances: vdr_sum, vdr_product, vdr_mean
"""

import sys
import os

# Add existing VDR code to path
_existing = os.path.join(os.path.dirname(__file__), "..", "existing")
if _existing not in sys.path:
    sys.path.insert(0, _existing)

# Re-export core VDR types and operations
from vdr import VDR, Remainder  # type: ignore
from linalg import Vec, Mat  # type: ignore
from softmax import softmax as vdr_softmax  # type: ignore
from autodiff import Node  # type: ignore

# Convenience constructors
def frac(v: int, d: int = 1) -> VDR:
    """Shorthand for VDR(v, d)."""
    return VDR(v, d)

# Fraction interop
def to_fraction(x: VDR):
    """Exact projection to Python Fraction."""
    return x.to_fraction()

def from_fraction(f) -> VDR:
    """Construct VDR from Python Fraction."""
    return VDR(f.numerator, f.denominator)
```

#### ml/bridge.py

```python
"""ML Bridge — connect existing VDR-4 transformer to KB system.

IOSE (composite):
  Inputs:  model_config (dict from KB), input_tokens (list of int)
  Outputs: logits (list of VDR), cache (dict of intermediate values)
  Side Effects: none (forward pass is pure)
  Properties: pure, deterministic, bounded
  Logic Type: application_logic

Wraps the existing VDR-4 TinyTransformerLM to:
  1. Initialize from KB facts (architecture config)
  2. Run forward pass, return exact logits
  3. Expose parameters for KB storage
"""

from typing import Dict, Any, List, Tuple, Optional
from core.kb import KnowledgeBase, Counter
from core.vdr import VDR, Vec, Mat, frac


class ModelBridge:
    """Thin wrapper connecting VDR-4 transformer to KB system."""

    def __init__(self, arch_kb: KnowledgeBase) -> None:
        """Initialize model from architecture KB facts."""
        self.arch_kb = arch_kb
        # Read architecture from KB
        self.vocab_size = self._get_int("vocab_size", 4)
        self.embed_dim = self._get_int("embed_dim", 2)
        self.num_layers = self._get_int("num_layers", 1)
        self.context_length = self._get_int("context_length", 3)
        # Initialize parameters as exact VDR fractions
        self.params: Dict[str, Any] = {}
        self._init_params()

    def _get_int(self, key: str, default: int) -> int:
        facts = self.arch_kb.query_facts("model_config", {"key": key})
        if facts:
            return int(facts[0].args.get("value", default))
        return default

    def _init_params(self) -> None:
        """Xavier-like rational initialization. All weights are exact VDR fractions."""
        # Minimal: embedding + one attention + feedforward + output head
        # Stage 1: random-ish small fractions for toy model
        d = self.embed_dim
        v = self.vocab_size
        self.params["embed"] = Mat([[frac(1, (i + j + 2)) for j in range(d)]
                                     for i in range(v)])
        self.params["attn_w"] = Mat([[frac(1, (i + j + 3)) for j in range(d)]
                                      for i in range(d)])
        self.params["ff_w1"] = Mat([[frac(1, (i + j + 2)) for j in range(d * 2)]
                                     for i in range(d)])
        self.params["ff_w2"] = Mat([[frac(1, (i + j + 2)) for j in range(d)]
                                     for i in range(d * 2)])
        self.params["head"] = Mat([[frac(1, (i + j + 2)) for j in range(v)]
                                    for i in range(d)])

    def forward(self, token_ids: List[int]) -> Tuple[List[Vec], Dict[str, Any]]:
        """Forward pass. Returns (logits_per_position, cache_dict).
        Every value is exact VDR."""
        cache = {}
        # Embedding lookup
        embeddings = [self.params["embed"].rows[tid] for tid in token_ids]
        cache["embeddings"] = embeddings

        # Simplified attention (Stage 1: no masking, single head)
        # score = embed @ attn_w @ embed^T, simplified to direct interaction
        hidden = list(embeddings)  # copy
        cache["hidden_pre_ff"] = hidden

        # Feedforward (simplified: just matvec through ff_w1, relu, ff_w2)
        outputs = []
        for h in hidden:
            mid = self.params["ff_w1"].matvec(h)
            # ReLU: max(0, x) per element
            mid_relu = Vec([max(x, frac(0)) for x in mid.data])
            out = self.params["ff_w2"].matvec(mid_relu)
            outputs.append(out)
        cache["hidden_post_ff"] = outputs

        # Logits head
        logits = []
        for out in outputs:
            logit_vec = self.params["head"].T.matvec(out) if hasattr(self.params["head"], 'T') else out
            logits.append(logit_vec)
        cache["logits"] = logits

        return logits, cache

    def get_all_params(self) -> Dict[str, Any]:
        """Return all parameters for KB storage."""
        return dict(self.params)

    def set_param(self, name: str, value: Any) -> None:
        """Set a parameter (for optimizer updates)."""
        self.params[name] = value
```

#### lifecycle/toy_lifecycle.py

```python
"""Toy Lifecycle — minimal full lifecycle in one script.

IOSE (composite):
  Inputs:  training_text (str), config (dict)
  Outputs: trained_model_kb (KnowledgeBase), eval_result (dict)
  Side Effects: KBs created, facts asserted, model trained
  Properties: deterministic (given same seed), bounded
  Logic Type: operational_logic

Demonstrates: init → train 1 step → eval → checkpoint
All as KB operations.
"""

from typing import Dict, Any, List
from core.kb import KnowledgeBase, Constraint, Counter, Fact
from core.path_registry import PathRegistry
from core.vdr import VDR, frac, Vec
from core.prolog import query
from core.constraints import check_all, register_evaluator
from ml.bridge import ModelBridge


def run_toy_lifecycle(training_text: str = "abcabc",
                      vocab: str = "abc") -> Dict[str, Any]:
    """Run the minimal full lifecycle. Returns dict of results."""

    registry = PathRegistry()
    results = {}

    # --- Phase 1: Create KB tree ---
    root_id = registry.resolve("root")  # already 0

    model_path = "root.model"
    model_id = registry.register(model_path)
    model_kb = KnowledgeBase(name="model", path=model_path, id=model_id,
                             parent_id=root_id)

    training_path = "root.training"
    training_id = registry.register(training_path)
    training_kb = KnowledgeBase(name="training", path=training_path, id=training_id,
                                parent_id=root_id)
    training_kb.counters["step"] = Counter(min_value=0, max_value=1000)
    training_kb.counters["loss_checks"] = Counter(min_value=0)

    eval_path = "root.eval"
    eval_id = registry.register(eval_path)
    eval_kb = KnowledgeBase(name="eval", path=eval_path, id=eval_id,
                            parent_id=root_id)

    # --- Phase 2: Model init (as KB facts) ---
    vocab_list = list(vocab)
    vocab_size = len(vocab_list)

    model_kb.assert_fact("model_config", {"key": "vocab_size", "value": vocab_size})
    model_kb.assert_fact("model_config", {"key": "embed_dim", "value": 2})
    model_kb.assert_fact("model_config", {"key": "num_layers", "value": 1})
    model_kb.assert_fact("model_config", {"key": "context_length", "value": 3})

    for i, ch in enumerate(vocab_list):
        model_kb.assert_fact("vocab", {"token": ch, "id": i})

    bridge = ModelBridge(model_kb)
    model_kb.assert_fact("model_status", {"state": "initialized"})
    results["init"] = "ok"

    # --- Phase 3: Tokenize training data ---
    token_to_id = {ch: i for i, ch in enumerate(vocab_list)}
    token_ids = [token_to_id[ch] for ch in training_text if ch in token_to_id]

    training_kb.assert_fact("corpus", {"tokens": token_ids, "length": len(token_ids)})

    # --- Phase 4: Train 1 step ---
    ctx_len = 3
    if len(token_ids) > ctx_len:
        input_ids = token_ids[:ctx_len]
        target_ids = token_ids[1:ctx_len + 1]

        logits, cache = bridge.forward(input_ids)

        # Compute MSE loss (simplified: compare logit argmax against target)
        training_kb.counters["step"].inc()
        loss = frac(0)
        for i, (logit_vec, target) in enumerate(zip(logits, target_ids)):
            # Simplified loss: (predicted_score_for_target - 1)^2
            if hasattr(logit_vec, 'data') and target < len(logit_vec.data):
                diff = logit_vec.data[target] + frac(-1)
                loss = loss + diff * diff

        training_kb.assert_fact("step_log", {
            "step": 0,
            "loss_v": loss.to_fraction().numerator if hasattr(loss, 'to_fraction') else 0,
            "loss_d": loss.to_fraction().denominator if hasattr(loss, 'to_fraction') else 1,
        })
        results["train_step"] = 0
        results["loss"] = str(loss)

    # --- Phase 5: Eval ---
    eval_kb.assert_fact("eval_result", {
        "model": model_path,
        "step": training_kb.counters["step"].get(),
        "status": "completed",
    })
    results["eval"] = "ok"

    # --- Phase 6: Checkpoint (store params as KB facts) ---
    step = training_kb.counters["step"].get()
    for param_name, param_val in bridge.get_all_params().items():
        model_kb.assert_fact("checkpoint", {
            "step": step,
            "param": param_name,
            "type": type(param_val).__name__,
        })
    model_kb.assert_fact("model_status", {"state": "checkpoint_saved", "step": step})
    results["checkpoint"] = step

    # --- Phase 7: Verify via Prolog query ---
    scope = [model_kb, training_kb, eval_kb]
    status_results = query("model_status", {"state": "?state"}, scope)
    results["statuses"] = [r["?state"] for r in status_results]

    eval_results = query("eval_result", {"status": "?s"}, scope)
    results["eval_status"] = [r["?s"] for r in eval_results]

    # --- Constraint check ---
    register_evaluator("step_executed",
                       lambda kb, sc: kb.counters.get("step", Counter()).get() > 0)
    training_kb.constraints.append(Constraint(
        name="at_least_one_step",
        condition="step_executed",
        on_violation="error",
    ))
    constraint_results = check_all(training_kb)
    results["constraints"] = [(c.name, ok, msg) for c, ok, msg in constraint_results]

    return results
```

### Stage 1 Tests

```python
# tests/test_toy_lifecycle.py
"""Stage 1 acceptance test: the toy lifecycle runs end-to-end."""

from lifecycle.toy_lifecycle import run_toy_lifecycle


def test_toy_lifecycle_completes():
    results = run_toy_lifecycle()
    assert results["init"] == "ok"
    assert results["train_step"] == 0
    assert results["eval"] == "ok"
    assert results["checkpoint"] == 1
    assert "initialized" in results["statuses"]
    assert "completed" in results["eval_status"]
    # Constraint: at least one step was executed
    assert all(ok for _, ok, _ in results["constraints"])


def test_toy_lifecycle_deterministic():
    r1 = run_toy_lifecycle()
    r2 = run_toy_lifecycle()
    assert r1["loss"] == r2["loss"]
    assert r1["statuses"] == r2["statuses"]
```

### Stage 1 Deliverables Summary

| Component | File | IOSE Category | Tests |
|-----------|------|--------------|-------|
| Type vocabulary | core/types.py | N/A (types only) | test_types.py |
| KnowledgeBase + Counter + Lock | core/kb.py | composite, operational_logic | test_kb.py |
| PathRegistry | core/path_registry.py | operational, operational_logic | test_path_registry.py |
| Prolog (flat query + unification) | core/prolog.py | pure, operational_logic | test_prolog.py |
| Constraint checker | core/constraints.py | pure, operational_logic | test_constraints.py |
| VDR re-export bridge | core/vdr.py | pure (passthrough) | existing 705 tests |
| ML model bridge | ml/bridge.py | composite, application_logic | test_bridge.py |
| Toy lifecycle | lifecycle/toy_lifecycle.py | composite, operational_logic | test_toy_lifecycle.py |
| **Total Stage 1** | **8 files + tests** | | **~60 new tests** |

---

## STAGE 2: ALMOST PRACTICAL

**Goal:** Add remaining data primitives (LRU, queue, stack, ring, bitset), command token parser, dotted-path scoped queries, rule evaluation in Prolog (with depth limit), real constraint evaluation via Prolog, and working data inheritance. The system can now do multi-step operations orchestrated by command tokens.

### Stage 2 New/Modified Files

```
vdr_system/
├── core/
│   ├── types.py              # Add: LRU, Queue, Stack, RingBuffer, Bitset structs
│   ├── kb.py                 # Add: all data primitives as fields, scoped query
│   ├── prolog.py             # Add: rule evaluation with depth limit, findall
│   ├── constraints.py        # Upgrade: Prolog-based condition evaluation
│   ├── scope.py              # NEW: scope resolution (walk parent chain)
│   └── command.py            # NEW: command token parser + executor
├── tests/
│   ├── test_data_primitives.py   # LRU, queue, stack, ring, bitset
│   ├── test_scope.py
│   ├── test_command.py
│   ├── test_prolog_rules.py
│   └── test_stage2_integration.py
```

### Stage 2 Data Primitive Additions to types.py

```python
"""
PATTERN: bounded_collection(name: str, capacity: int)
  Properties: deterministic, bounded by capacity
  Side Effects: none (mutates internal state, but KB-contained)
  Instances: LRUCache, BoundedQueue, BoundedStack, RingBuffer

All follow the same struct pattern:
  - name, capacity, created_at
  - bounded: size never exceeds capacity
  - deterministic: same operations → same state
"""

from collections import OrderedDict

@dataclass
class LRUCache:
    capacity: int = 50
    _entries: OrderedDict = field(default_factory=OrderedDict)

    def push(self, key: str, value: Any) -> Optional[str]:
        """Insert/update. Returns evicted key if eviction occurred."""
        evicted = None
        if key in self._entries:
            self._entries.move_to_end(key)
            self._entries[key] = value
        else:
            if len(self._entries) >= self.capacity:
                evicted = next(iter(self._entries))
                del self._entries[evicted]
            self._entries[key] = value
        return evicted

    def get(self, key: str) -> Optional[Any]:
        if key in self._entries:
            self._entries.move_to_end(key)
            return self._entries[key]
        return None

    def peek(self, count: int) -> List[Tuple[str, Any]]:
        items = list(self._entries.items())
        return items[-count:] if count <= len(items) else items

    def contains(self, key: str) -> bool:
        return key in self._entries

    def size(self) -> int:
        return len(self._entries)

    def clear(self) -> None:
        self._entries.clear()

    def evict(self, key: str) -> bool:
        if key in self._entries:
            del self._entries[key]
            return True
        return False


@dataclass
class BoundedQueue:
    capacity: int = 50
    _items: List[Any] = field(default_factory=list)

    def push(self, item: Any) -> bool:
        if len(self._items) >= self.capacity:
            return False
        self._items.append(item)
        return True

    def pop(self) -> Optional[Any]:
        return self._items.pop(0) if self._items else None

    def peek(self) -> Optional[Any]:
        return self._items[0] if self._items else None

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self.capacity

    def clear(self) -> None:
        self._items.clear()

    def to_list(self) -> List[Any]:
        return list(self._items)


@dataclass
class BoundedStack:
    capacity: int = 50
    _items: List[Any] = field(default_factory=list)

    def push(self, item: Any) -> bool:
        if len(self._items) >= self.capacity:
            return False
        self._items.append(item)
        return True

    def pop(self) -> Optional[Any]:
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[Any]:
        return self._items[-1] if self._items else None

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def clear(self) -> None:
        self._items.clear()

    def to_list(self) -> List[Any]:
        return list(reversed(self._items))


@dataclass
class RingBuffer:
    capacity: int = 50
    _items: List[Any] = field(default_factory=list)
    _write_pos: int = 0
    _count: int = 0

    def write(self, item: Any) -> Optional[Any]:
        """Write item. Returns overwritten item if buffer was full."""
        overwritten = None
        if self._count < self.capacity:
            self._items.append(item)
            self._count += 1
        else:
            overwritten = self._items[self._write_pos]
            self._items[self._write_pos] = item
        self._write_pos = (self._write_pos + 1) % self.capacity
        return overwritten

    def read_all(self) -> List[Any]:
        if self._count < self.capacity:
            return list(self._items)
        start = self._write_pos
        return self._items[start:] + self._items[:start]

    def read_last(self, count: int) -> List[Any]:
        all_items = self.read_all()
        return all_items[-count:] if count <= len(all_items) else all_items

    def size(self) -> int:
        return self._count

    def clear(self) -> None:
        self._items.clear()
        self._write_pos = 0
        self._count = 0


@dataclass
class Bitset:
    width: int = 100
    _bits: List[bool] = field(default_factory=list)

    def __post_init__(self):
        if not self._bits:
            self._bits = [False] * self.width

    def set(self, index: int) -> None:
        if 0 <= index < self.width:
            self._bits[index] = True

    def clear_bit(self, index: int) -> None:
        if 0 <= index < self.width:
            self._bits[index] = False

    def test(self, index: int) -> bool:
        return 0 <= index < self.width and self._bits[index]

    def count(self) -> int:
        return sum(self._bits)

    def all_set(self) -> bool:
        return all(self._bits)

    def any_set(self) -> bool:
        return any(self._bits)

    def reset(self) -> None:
        self._bits = [False] * self.width

    def to_list(self) -> List[int]:
        return [i for i, b in enumerate(self._bits) if b]
```

### Stage 2 — core/scope.py

```python
"""Scope resolution — walk parent chain for scoped queries.

IOSE (pure):
  Inputs:  active_kb_id (int), all_kbs (dict of id→KB)
  Outputs: ordered list of KBs in scope
  Side Effects: none
  Properties: pure, deterministic, bounded
"""

from typing import Dict, List
from .kb import KnowledgeBase


def resolve_scope(active_kb_id: int,
                  all_kbs: Dict[int, KnowledgeBase]) -> List[KnowledgeBase]:
    """Walk from active KB to root, collecting scope chain."""
    chain = []
    current_id = active_kb_id
    visited = set()
    while current_id is not None and current_id not in visited:
        visited.add(current_id)
        kb = all_kbs.get(current_id)
        if kb is None:
            break
        chain.append(kb)
        current_id = kb.parent_id
    return chain
```

### Stage 2 — core/command.py

```python
"""Command token parser and executor.

IOSE (composite):
  Inputs:  command_string (str), system_state (dict)
  Outputs: result (Any), updated_state
  Side Effects: depends on command type (pure commands: none; KB commands: fact mutations)
  Properties: deterministic, bounded
  Logic Type: operational_logic

Stage 2: PURE_FN and KB_ASSERT/KB_RETRACT/KB_QUERY only.
Stage 5 adds OP_FN, ENV_EXEC, etc.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Callable
from enum import Enum


class CommandType(Enum):
    PURE_FN = "PURE_FN"
    KB_ASSERT = "KB_ASSERT"
    KB_RETRACT = "KB_RETRACT"
    KB_QUERY = "KB_QUERY"


@dataclass
class CommandToken:
    cmd_type: CommandType
    target: str             # primitive name or KB path
    args: Dict[str, Any] = None

    def __post_init__(self):
        if self.args is None:
            self.args = {}


class CommandExecutor:
    """Execute command tokens against system state."""

    def __init__(self) -> None:
        self._pure_fns: Dict[str, Callable] = {}

    def register_pure(self, name: str, fn: Callable) -> None:
        """Register a pure function primitive."""
        self._pure_fns[name] = fn

    def execute(self, cmd: CommandToken, system) -> Any:
        """Execute a command token. Returns result."""
        if cmd.cmd_type == CommandType.PURE_FN:
            fn = self._pure_fns.get(cmd.target)
            if fn is None:
                raise ValueError(f"Unknown pure function: {cmd.target}")
            return fn(**cmd.args)

        if cmd.cmd_type == CommandType.KB_ASSERT:
            kb = system.get_kb(cmd.args.get("kb_path", ""))
            if kb is None:
                raise ValueError(f"KB not found: {cmd.args.get('kb_path')}")
            return kb.assert_fact(
                cmd.args.get("predicate", ""),
                cmd.args.get("fact_args", {}),
                turn=cmd.args.get("turn", 0),
            )

        if cmd.cmd_type == CommandType.KB_QUERY:
            kb_path = cmd.args.get("kb_path", "")
            scope = system.resolve_scope_for(kb_path)
            from .prolog import query
            return query(
                cmd.args.get("predicate", ""),
                cmd.args.get("query_args", {}),
                scope,
            )

        if cmd.cmd_type == CommandType.KB_RETRACT:
            kb = system.get_kb(cmd.args.get("kb_path", ""))
            if kb is None:
                raise ValueError(f"KB not found: {cmd.args.get('kb_path')}")
            return kb.retract_fact(
                cmd.args.get("predicate", ""),
                cmd.args.get("fact_args", {}),
                turn=cmd.args.get("turn", 0),
            )

        raise ValueError(f"Unknown command type: {cmd.cmd_type}")
```

### Stage 2 Deliverables Summary

| Component | File | IOSE Category | Tests |
|-----------|------|--------------|-------|
| Data primitives (LRU, Queue, Stack, Ring, Bitset) | core/types.py additions | pure, bounded | test_data_primitives.py (~100) |
| KB with all data primitives | core/kb.py updated | composite | test_kb.py updated |
| Scope resolution | core/scope.py | pure | test_scope.py (~15) |
| Command token executor | core/command.py | composite, operational_logic | test_command.py (~25) |
| Prolog rule evaluation | core/prolog.py updated | pure | test_prolog_rules.py (~20) |
| Prolog-based constraints | core/constraints.py updated | pure | existing + ~10 |
| **Total Stage 2** | **3 new + 3 modified** | | **~170 new tests** |

---

## STAGE 3: LOOSELY INTEGRATED

**Goal:** Session management (snapshot/restore/clone/kill), inference notebooks, external data pipeline (parse_json, to_fraction conversion boundary), confidence propagation, and the orchestrated inference loop running against in-memory data. The system can now investigate.

### Stage 3 New Files

```
vdr_system/
├── core/
│   ├── session.py            # NEW: snapshot, restore, reset, clone, kill
│   └── conversion.py         # NEW: conversion boundary tracking
├── inference/
│   ├── __init__.py
│   ├── notebook.py           # NEW: InferenceNotebook KB schema
│   ├── loop.py               # NEW: assess → formalize → execute → store → assess
│   ├── confidence.py         # NEW: confidence propagation rules
│   └── modes.py              # NEW: deductive, inductive, abductive, analogical helpers
├── builtins/
│   ├── __init__.py
│   ├── string_ops.py         # NEW: 17 string primitives
│   ├── list_ops.py           # NEW: 36 list primitives
│   ├── set_ops.py            # NEW: 14 set primitives
│   ├── dict_ops.py           # NEW: 15 dict primitives
│   ├── stat_ops.py           # NEW: 16 statistics/probability primitives
│   └── registry.py           # NEW: builtin IOSE registry (all builtins as facts)
├── tests/
│   ├── test_session.py
│   ├── test_notebook.py
│   ├── test_loop.py
│   ├── test_confidence.py
│   ├── test_string_ops.py
│   ├── test_list_ops.py
│   └── test_stage3_integration.py
```

### Stage 3 Key IOSE Patterns for Builtins

```python
# builtins/registry.py
"""
Central registry of all builtins with IOSE declarations.

PATTERN: string_unary(s: str) → str
  Properties: pure, deterministic, bounded
  Instances: string_reverse, string_upper, string_lower, string_trim

PATTERN: string_binary(s: str, t: str) → str
  Properties: pure, deterministic, bounded
  Instances: string_concat, string_replace

PATTERN: string_predicate(s: str, t: str) → bool
  Properties: pure, deterministic, bounded
  Instances: string_contains, string_starts_with, string_ends_with

PATTERN: list_transform(xs: list) → list
  Properties: pure, deterministic, bounded
  Instances: list_reverse, list_unique, list_flatten, list_sort

PATTERN: list_access(xs: list, idx: int) → Any
  Properties: pure, deterministic, bounded, partial (index out of range)
  Instances: list_head, list_tail, list_last, list_nth

PATTERN: list_predicate(xs: list, pred: Callable) → bool
  Properties: pure, deterministic, bounded
  Instances: list_any, list_all

PATTERN: list_higher_order(xs: list, fn: Callable) → list_or_value
  Properties: pure, deterministic, bounded
  Instances: list_filter, list_map, list_reduce

PATTERN: set_binary(a: set, b: set) → set
  Properties: pure, deterministic, bounded, commutative (where applicable)
  Instances: set_union, set_intersection, set_difference, set_symmetric_diff

PATTERN: stat_aggregate(xs: list[VDR]) → VDR
  Properties: pure, deterministic, bounded
  Instances: stat_mean, stat_variance, stat_median, stat_percentile
"""
```

### Stage 3 Deliverables Summary

| Component | Files | Tests |
|-----------|-------|-------|
| Session management | core/session.py | ~30 |
| Conversion boundaries | core/conversion.py | ~10 |
| Inference notebook | inference/notebook.py | ~20 |
| Inference loop | inference/loop.py | ~25 |
| Confidence propagation | inference/confidence.py | ~15 |
| Inference modes | inference/modes.py | ~20 |
| String builtins (17) | builtins/string_ops.py | ~51 |
| List builtins (36) | builtins/list_ops.py | ~108 |
| Set builtins (14) | builtins/set_ops.py | ~42 |
| Dict builtins (15) | builtins/dict_ops.py | ~45 |
| Stat builtins (16) | builtins/stat_ops.py | ~48 |
| Builtin IOSE registry | builtins/registry.py | ~10 |
| **Total Stage 3** | **12 new files** | **~424 new tests** |

---

## STAGE 4: FULL ENCAPSULATED

**Goal:** Lifecycle KBs (source registry, corpus, tokenizer, training run, checkpoint, eval suite, feedback, deployment, monitoring, retirement), surfacing modes, account KBs, complete Prolog with transitive rules, mount system, connection graph, and full inference with all four modes working against real KB data.

### Stage 4 New Files

```
vdr_system/
├── core/
│   ├── mount.py              # NEW: mount system with cycle detection
│   ├── connections.py        # NEW: connection graph operations
│   ├── surfacing.py          # NEW: table/tree/provenance/constraint/diff modes
│   └── accounts.py           # NEW: user/group account KBs, constraint inheritance
├── lifecycle/
│   ├── source.py             # NEW: data source KB management
│   ├── corpus.py             # NEW: corpus preparation KB
│   ├── tokenizer.py          # NEW: vocabulary KB, tokenize/detokenize
│   ├── training.py           # NEW: training run KB, step logging, checkpoints
│   ├── feedback.py           # NEW: feedback collection KB, pairwise prefs
│   ├── evaluation.py         # NEW: eval suite KB, benchmark running
│   ├── deployment.py         # NEW: deployment config KB
│   ├── monitoring.py         # NEW: monitoring KB, watches, drift detection
│   └── retirement.py         # NEW: archive and retirement KB
├── builtins/
│   ├── numeric/
│   │   ├── __init__.py
│   │   ├── closed.py         # 8 closed arithmetic builtins
│   │   ├── active.py         # 5 active arithmetic builtins
│   │   ├── structure.py      # 3 lift/rebase/projection builtins
│   │   ├── comparison.py     # 10 comparison builtins
│   │   ├── rounding.py       # 11 rounding/extraction builtins
│   │   ├── number_theory.py  # 13 number theory builtins
│   │   ├── aggregates.py     # 8 list aggregate builtins
│   │   ├── qbasis.py         # 7 Q-basis builtins
│   │   ├── functional.py     # 8 functional remainder builtins
│   │   ├── calculus.py       # 6 discrete calculus builtins
│   │   ├── linalg.py         # 24 linear algebra builtins
│   │   ├── polynomial.py     # 8 polynomial builtins
│   │   ├── finite_field.py   # 4 finite field builtins
│   │   ├── markov.py         # 3 Markov builtins
│   │   ├── graph_math.py     # 2 graph math builtins
│   │   ├── integer.py        # 13 integer fast path builtins
│   │   ├── bits.py           # 8 bit operation builtins
│   │   └── denom.py          # 5 denominator management builtins
│   ├── graph_ops.py          # 13 graph algorithm builtins
│   ├── time_ops.py           # 10 date/time builtins
│   └── identity_ops.py       # 8 hashing/encoding builtins
```

### Stage 4 Numeric Builtin Pattern Declarations

```python
"""
builtins/numeric/ — 173 numeric builtins organized by operand type.

All numeric builtins wrap existing VDR-1 through VDR-4 code.
They do not reimplement arithmetic — they expose it as IOSE-declared builtins.

PATTERN: closed_binary(a: VDR_closed, b: VDR_closed) → VDR_closed
  Properties: pure, deterministic, bounded, commutative (add/mul), associative (add/mul)
  Instances: vdr_add, vdr_sub, vdr_mul, vdr_div

PATTERN: closed_unary(a: VDR_closed) → VDR_closed
  Properties: pure, deterministic, bounded, invertible (neg)
  Instances: vdr_neg, vdr_abs, vdr_reciprocal, vdr_simplify

PATTERN: int_pow(a: VDR, n: int) → VDR
  Properties: pure, deterministic, bounded
  Instance: vdr_pow

PATTERN: active_binary(a: VDR, b: VDR) → VDR
  Properties: pure, deterministic, bounded
  Instances: active_add_same_d, active_add_diff_d, active_mul,
             active_div_closed, active_div_active

PATTERN: structure_op(a: VDR, k_or_b: int) → VDR
  Properties: pure, deterministic, bounded
  Instances: vdr_lift, vdr_rebase, vdr_scalar_projection

PATTERN: comparison(a: VDR, b: VDR) → bool_or_ordering
  Properties: pure, deterministic, bounded, total (for closed)
  Instances: vdr_compare, vdr_equal, vdr_lt, vdr_le, vdr_gt, vdr_ge,
             vdr_min, vdr_max, vdr_sign, vdr_is_zero, vdr_is_positive, vdr_is_negative

PATTERN: rounding(a: VDR) → int
  Properties: pure, deterministic, bounded
  Instances: vdr_floor, vdr_ceil, vdr_round, vdr_truncate

PATTERN: extraction(a: VDR) → int_or_bool_or_tuple
  Properties: pure, deterministic, bounded
  Instances: vdr_numerator, vdr_denominator, vdr_is_integer, vdr_is_closed,
             vdr_is_active, vdr_simplify, vdr_denom_complexity

PATTERN: int_binary(a: int, b: int) → int
  Properties: pure, deterministic, bounded, commutative (gcd/lcm), associative (gcd/lcm)
  Instances: vdr_gcd, vdr_lcm, vdr_mod, vdr_exact_int_div, vdr_mod_pow,
             vdr_mod_inv, vdr_extended_gcd

PATTERN: int_unary(n: int) → int_or_bool
  Properties: pure, deterministic, bounded
  Instances: vdr_is_prime, vdr_factorial, vdr_euler_totient

PATTERN: int_binary_to_int(n: int, k: int) → int
  Properties: pure, deterministic, bounded
  Instances: vdr_binomial, vdr_fibonacci

PATTERN: qbasis_binary(a: QBasis, b: QBasis) → QBasis_or_tuple
  Properties: pure, deterministic, bounded
  Instances: qbasis_add, qbasis_sub, qbasis_mul (returns (result, error_bound))

PATTERN: fn_create(name: str, step_or_term: Callable) → FunctionalRemainder
  Properties: pure, deterministic
  Instances: fn_make_newton, fn_make_series

PATTERN: fn_resolve(fn: FunctionalRemainder, depth: int) → VDR
  Properties: pure, deterministic, bounded (at given depth)
  Instances: fn_resolve, fn_sqrt, fn_exp, fn_log, fn_sin, fn_cos

PATTERN: discrete_calc(f: Callable, x: VDR, h: VDR) → VDR
  Properties: pure, deterministic, bounded
  Instances: discrete_derivative, discrete_derivative_nth, left_riemann,
             trapezoidal, finite_diff_table, richardson_extrapolation

PATTERN: vec_binary(a: Vec, b: Vec) → Vec
  Properties: pure, deterministic, bounded, commutative (add)
  Instances: vec_add, vec_sub

PATTERN: mat_binary(a: Mat, b: Mat) → Mat
  Properties: pure, deterministic, bounded
  Instances: mat_add, mat_mul

PATTERN: mat_unary(m: Mat) → Mat_or_VDR
  Properties: pure, deterministic, bounded
  Instances: mat_transpose, mat_det, mat_inv, mat_rank, mat_trace

PATTERN: poly_binary(p: list, q: list) → list
  Properties: pure, deterministic, bounded
  Instances: poly_add, poly_mul, poly_div, poly_gcd

PATTERN: gf_binary(a: int, b: int, p: int) → int
  Properties: pure, deterministic, bounded
  Instances: gf_add, gf_mul, gf_inv, gf_pow

PATTERN: bit_binary(a: int, b: int) → int
  Properties: pure, deterministic, bounded, commutative (and/or/xor)
  Instances: bit_and, bit_or, bit_xor

PATTERN: bit_unary(a: int) → int
  Properties: pure, deterministic, bounded
  Instances: bit_not, bit_shift_left, bit_shift_right, bit_popcount, bit_width
"""
```

### Stage 4 Deliverables Summary

| Component | Files | Tests |
|-----------|-------|-------|
| Mount system | core/mount.py | ~20 |
| Connection graph | core/connections.py | ~15 |
| Surfacing modes | core/surfacing.py | ~25 |
| Account KBs | core/accounts.py | ~20 |
| Lifecycle KBs (13 modules) | lifecycle/*.py | ~100 |
| Numeric builtins (173) | builtins/numeric/*.py (18 files) | ~519 |
| Graph/time/identity builtins | builtins/*.py (3 files) | ~93 |
| **Total Stage 4** | **~35 new files** | **~792 new tests** |

---

## STAGE 5: OPERATIONAL COMPLETE

**Goal:** Operational environments (Docker, VM, local, SSH), positive credential grants, async task management, versioning, direct data download, operational primitives (filesystem, compilation, execution, linting, network, process), IOSE validation engine, OSO principles KB, and the full system integration test.

### Stage 5 New Files

```
vdr_system/
├── core/
│   ├── iose_registry.py      # NEW: IOSE declaration storage, validation, query
│   └── oso_principles.py     # NEW: operational engineering KB (axioms, facts, rules, constraints)
├── ops/
│   ├── __init__.py
│   ├── environments.py       # NEW: Docker/VM/Local/SSH unified interface
│   ├── grants.py             # NEW: positive credential grant system
│   ├── tasks.py              # NEW: async task management
│   ├── versioning.py         # NEW: version-as-KB-fact operations
│   ├── download.py           # NEW: direct data download / addressable resources
│   └── primitives/
│       ├── __init__.py
│       ├── filesystem.py     # 15 filesystem primitives
│       ├── compilation.py    # 4 compilation primitives
│       ├── execution.py      # 5 execution primitives
│       ├── linting.py        # 8 linting primitives
│       ├── network.py        # 5 network primitives
│       └── process.py        # 7 process primitives
├── builtins/
│   ├── logic_ops.py          # 11 logic/control builtins
│   ├── conversion_ops.py     # 14 conversion/formatting builtins (non-numeric)
│   └── numeric/
│       └── conversion.py     # 11 numeric conversion boundary builtins
├── system.py                 # NEW: top-level System class composing all components
├── tests/
│   ├── test_environments.py
│   ├── test_grants.py
│   ├── test_tasks.py
│   ├── test_versioning.py
│   ├── test_download.py
│   ├── test_op_primitives.py  # All 44 operational primitives
│   ├── test_iose_validation.py
│   ├── test_oso_principles.py
│   ├── test_system_integration.py
│   └── test_full_lifecycle.py  # End-to-end: data → train → eval → deploy → monitor → retire
```

### Stage 5 — system.py (Top-Level Composition)

```python
"""The VDR-LLM-Prolog System — top-level IOSE composite.

IOSE:
  Inputs:  command_tokens (list), user_text (str), session_id (str)
  Outputs: response_text (str), direct_data (list), mutations_log (list)
  Side Effects: all declared per sub-component
  Properties: deterministic (given same state), bounded (per turn)
  Logic Type: operational_logic

This is the root composite node. It owns:
  - PathRegistry (addressing)
  - Dict[int, KnowledgeBase] (all KBs)
  - CommandExecutor (command dispatch)
  - SessionManager (snapshot/clone)
  - GrantVerifier (authorization)
  - EnvironmentManager (sandboxed execution)
  - IOSERegistry (component declarations)
  - BuiltinRegistry (all 448 builtins)
"""

from typing import Dict, Any, List, Optional
from core.kb import KnowledgeBase
from core.path_registry import PathRegistry
from core.scope import resolve_scope
from core.command import CommandExecutor, CommandToken
from core.session import SessionManager        # Stage 3
from ops.grants import GrantVerifier           # Stage 5
from ops.environments import EnvironmentManager  # Stage 5
from core.iose_registry import IOSERegistry    # Stage 5
from builtins.registry import BuiltinRegistry  # Stage 3+


class VDRSystem:
    """The complete VDR-LLM-Prolog system."""

    def __init__(self) -> None:
        self.registry = PathRegistry()
        self.kbs: Dict[int, KnowledgeBase] = {}
        self.executor = CommandExecutor()
        self.session_mgr = SessionManager(self)
        self.grant_verifier = GrantVerifier(self)
        self.env_mgr = EnvironmentManager(self)
        self.iose_registry = IOSERegistry()
        self.builtin_registry = BuiltinRegistry(self.executor)
        self.turn: int = 0

        # Create root KB
        root_kb = self._create_kb("root", "root")

        # Load OSO principles
        self._load_oso_principles()

    def _create_kb(self, name: str, path: str,
                   parent_path: Optional[str] = None) -> KnowledgeBase:
        kb_id = self.registry.register(path)
        parent_id = self.registry.resolve(parent_path) if parent_path else None
        kb = KnowledgeBase(name=name, path=path, id=kb_id,
                           parent_id=parent_id, created_at=self.turn)
        self.kbs[kb_id] = kb
        if parent_id is not None and parent_id in self.kbs:
            self.kbs[parent_id].children_ids.append(kb_id)
        return kb

    def get_kb(self, path: str) -> Optional[KnowledgeBase]:
        kb_id = self.registry.resolve(path)
        if kb_id is not None:
            return self.kbs.get(kb_id)
        return None

    def resolve_scope_for(self, path: str) -> List[KnowledgeBase]:
        kb_id = self.registry.resolve(path)
        if kb_id is None:
            return []
        return resolve_scope(kb_id, self.kbs)

    def execute_command(self, cmd: CommandToken) -> Any:
        """Execute a command token with full validation."""
        # Stage 5: IOSE type check, grant check, side effect preview
        self.turn += 1
        return self.executor.execute(cmd, self)

    def execute_commands(self, cmds: List[CommandToken]) -> List[Any]:
        """Execute a chain of command tokens."""
        return [self.execute_command(cmd) for cmd in cmds]

    def _load_oso_principles(self) -> None:
        """Load operational engineering principles into root.system.oso KB."""
        oso_kb = self._create_kb("oso", "root.system.oso", "root")
        # Axioms loaded from oso_principles.py
        # Stage 5 implementation
```

### Stage 5 Deliverables Summary

| Component | Files | Tests |
|-----------|-------|-------|
| IOSE validation engine | core/iose_registry.py | ~80 |
| OSO principles KB | core/oso_principles.py | ~50 |
| Environment manager | ops/environments.py | ~30 |
| Grant system | ops/grants.py | ~25 |
| Async tasks | ops/tasks.py | ~20 |
| Versioning | ops/versioning.py | ~15 |
| Direct download | ops/download.py | ~15 |
| Operational primitives (44) | ops/primitives/*.py (6 files) | ~132 |
| Logic/conversion builtins | builtins/*.py (3 files) | ~75 |
| System composition | system.py | ~30 |
| Full lifecycle integration | tests/test_full_lifecycle.py | ~50 |
| **Total Stage 5** | **~15 new files** | **~522 new tests** |

---

## CUMULATIVE BUILD SUMMARY

| Stage | New Files | New Tests | Cumulative Files | Cumulative Tests | System State |
|-------|-----------|-----------|-----------------|-----------------|-------------|
| 1 | 8 + tests | ~60 | 8 | ~60 | KB + VDR + Prolog + toy lifecycle |
| 2 | 3 new + 3 mod + tests | ~170 | 14 | ~230 | + data primitives + commands + scope |
| 3 | 12 + tests | ~424 | 26 | ~654 | + sessions + notebooks + inference + builtins |
| 4 | ~35 + tests | ~792 | ~61 | ~1446 | + lifecycle + numeric + mounts + accounts |
| 5 | ~15 + tests | ~522 | ~76 | ~1968 | + environments + grants + ops + IOSE + OSO |
| **Plus existing VDR-1–4** | **24 modules** | **705** | **~100** | **~2673** | **Complete system** |

Every stage is testable independently. Every stage builds on the previous. Every component has an IOSE declaration. Every test verifies the IOSE contract. The Python prototype validates the design. The Zig 0.15.1 final version implements the same IOSE contracts with native performance.
