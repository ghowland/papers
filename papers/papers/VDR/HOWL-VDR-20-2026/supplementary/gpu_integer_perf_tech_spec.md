# GPU Tech Spec for VDR + Prolog + LLM Orchestration

Version: draft 1  
Scope: mechanical mapping of the VDR-LLM-Prolog architecture onto GPU hardware using integer-first execution, with host-managed orchestration and pipelined execution.

## 1. Purpose

This specification defines a GPU-oriented runtime for:

- VDR exact arithmetic
- KB tree storage and retrieval
- Prolog-style fact/rule querying
- builtin primitive execution
- grammar-constrained LLM orchestration
- session/live-state management
- provenance and confidence propagation

It assumes the original architectural premises are accepted and focuses only on implementation mechanics.

## 2. Design goals

The runtime shall:

- execute exact arithmetic using integer kernels
- keep common-case values in fixed-width GPU-native representations
- spill irregular active/remainder structures into append-only arenas
- represent KB, facts, terms, rules, and provenance in flat GPU-resident tables
- execute Prolog query evaluation as batched candidate filtering and joins
- pipeline LLM decode with query/compute/store phases
- minimize host-device transfer
- preserve deterministic execution order where declared
- allow exact or explicitly logged lossy reprojection only

The runtime shall not:

- depend on floating point for internal exact computation paths
- represent terms or KB objects as host-language pointer graphs on device
- implement arbitrary closures on GPU for functional remainders
- rely on recursive per-thread control flow for mainline query evaluation

## 3. High-level architecture

The runtime is split into control plane and data plane.

### 3.1 Control plane

Runs on CPU.

Responsibilities:

- user input handling
- path parsing and path-to-ID resolution
- session orchestration
- grant verification
- environment and external operations
- kernel scheduling and batch formation
- deterministic ordering policy
- memory compaction and arena lifecycle
- handling irregular backtracking decisions
- final response assembly

### 3.2 Data plane

Runs on GPU.

Responsibilities:

- fixed-width integer arithmetic
- Q-basis arithmetic
- active remainder spill processing
- KB scans and indexed retrieval
- term matching and unification
- rule-body frontier expansion
- confidence propagation
- grammar masking
- dense LLM forward/decode
- live-state bulk mutation

## 4. Execution classes

The runtime defines 6 execution classes.

### EC1: Fixed-width integer arithmetic

Used for:

- int32/int64 fast path
- Q335 numerators
- counters
- bitsets
- IDs and interned symbols

### EC2: Big integer / limb arithmetic

Used for:

- multi-limb numerators
- multi-limb denominators
- exact matrix accumulation
- normalization
- cross-multiplication comparisons

### EC3: Graph / relational kernels

Used for:

- KB traversal
- scope filtering
- connection queries
- fact candidate scans
- predicate bucket retrieval

### EC4: Prolog kernels

Used for:

- term compatibility filtering
- unification
- binding extension
- join-based rule evaluation
- contradiction checks

### EC5: LLM kernels

Used for:

- embedding lookup
- attention
- feedforward
- decode
- grammar-constrained masking

### EC6: Host-only operational tasks

Used for:

- file, process, network, environment operations
- path parsing
- grants
- mount lifecycle mutation
- OS integration

## 5. Core numeric model

## 5.1 Numeric classes

The GPU runtime shall support the following numeric classes.

### NC0: Small integer

Representation:
- signed 32-bit or 64-bit immediate

Use:
- IDs
- counters
- small exact values
- term payloads

### NC1: Fixed-frame closed VDR

Representation:
- fixed denominator frame, implicit denominator
- numerator in fixed-width limb vector

Primary instance:
- Q335 with implicit denominator \(2^{335}\)

### NC2: General closed rational

Representation:
- numerator limb ref
- denominator limb ref

Use:
- values outside common frame
- parsed exact fractions
- outputs of cross-frame operations

### NC3: Active VDR

Representation:
- top-level value/denominator refs
- remainder tag and payload ref

Use:
- overflow or unresolved exact structure
- composite remainder trees
- functional remainder descriptors

## 5.2 Q335 fixed layout

Preferred device representation:

```text
Q335 = signed integer numerator over implicit denominator 2^335
```

Storage options:

- 11 x 32-bit limbs = 352 bits
- 6 x 64-bit limbs = 384 bits

Normative recommendation:
- portable backend: 11 x 32-bit limbs
- optimized backend: 6 x 64-bit limbs where int64 throughput is acceptable

Example device struct:

```cpp
struct Q335_32 {
  uint32_t limb[11];
};
```

Alternative:

```cpp
struct Q335_64 {
  uint64_t limb[6];
};
```

Sign shall be two’s-complement within the limb vector or a separate sign bit. Two’s-complement is preferred for add/sub and comparison regularity.

## 5.3 General VDR node layout

All device-side VDR values shall be stored by handle.

```cpp
enum VdrTag : uint8_t {
  VDR_SMALL_INT = 0,
  VDR_QFRAME = 1,
  VDR_RATIONAL = 2,
  VDR_ACTIVE = 3
};

struct VdrRef {
  uint32_t id;
};
```

Backing tables:

```cpp
struct VdrNode {
  uint8_t tag;
  uint8_t flags;
  uint16_t depth;
  uint32_t v_ref;
  uint32_t d_ref;
  uint32_t r_ref;
};
```

Meaning:
- `v_ref`: numerator or frame-value reference
- `d_ref`: denominator reference or implicit-frame code
- `r_ref`: 0 for closed, otherwise remainder payload reference

## 5.4 Remainder payload layout

```cpp
enum RTag : uint8_t {
  R_ZERO = 0,
  R_ATOMIC = 1,
  R_COMPOSITE = 2,
  R_FUNCTIONAL = 3
};

struct AtomicR {
  uint32_t int_ref;
};

struct CompositeR {
  uint32_t base_ref;
  uint32_t child_begin;
  uint32_t child_count;
};

struct FunctionalR {
  uint16_t fn_id;
  uint16_t arity;
  uint32_t param_begin;
  uint32_t param_count;
};
```

All child lists and params shall live in append-only pools.

## 6. Arithmetic kernels

## 6.1 Required kernel set

The arithmetic subsystem shall provide:

- limb add
- limb subtract
- limb compare
- limb shift left/right
- limb schoolbook multiply
- optional Karatsuba/Toom thresholds
- power-of-two divmod split
- exact sign normalization
- GCD reduction for closed rationals
- Q-frame reprojection
- scalar projection
- active merge / child merge
- canonical sort support for child descriptors

## 6.2 Q335 addition

Operation:
- limbwise add
- detect overflow
- if no overflow: return closed Q335
- if overflow beyond representable frame policy: spill into active form or widened internal temp then normalize

Example kernel sketch:

```cpp
__device__ Q335_32 q335_add(const Q335_32& a, const Q335_32& b) {
  Q335_32 out;
  uint64_t carry = 0;
  #pragma unroll
  for (int i = 0; i < 11; ++i) {
    uint64_t s = (uint64_t)a.limb[i] + b.limb[i] + carry;
    out.limb[i] = (uint32_t)s;
    carry = s >> 32;
  }
  return out;
}
```

## 6.3 Q335 multiplication

Because denominator is implicit \(2^{335}\):

Given numerators \(A\) and \(B\):

- compute full product \(P = A \cdot B\)
- split product at bit 335
- quotient/high part becomes current-level value
- low 335-bit part becomes exact remainder payload if nonzero

Mechanical output:

- if low part is zero: closed node
- else: active node with atomic/composite remainder

Example split concept:

```text
P = Q * 2^335 + Rem
Result = [Q, 2^335, Rem]
```

Kernel sketch:

```cpp
struct MulSplitResult {
  Q335_32 q;
  Q335_32 rem_low;
  bool has_rem;
};

__device__ MulSplitResult q335_mul_split(const Q335_32& a, const Q335_32& b);
```

## 6.4 Comparison

Preferred order:

1. same-tag fast path
2. same-frame lexicographic compare
3. small-int immediate compare
4. rational cross-multiply
5. active compare via normalized projection or declared comparison policy

Cross-multiplication comparison:

```text
a/b ? c/d  =>  a*d ? c*b
```

Kernel shall use widened accumulators or limb multiplication.

## 6.5 Normalization

Normalization passes shall execute bottom-up where active trees are involved.

Required steps:

- denominator sign normalization
- GCD reduction for closed nodes
- atomic remainder consolidation
- child normalization
- child ordering
- same-denominator child merge
- zero-remainder collapse

Suggested pipeline:
- mark active subtree roots
- parallel normalize leaves
- upward compaction pass
- canonical ordering via segmented sort

## 6.6 Reprojection

Declared lossy reduction into target frame:

Inputs:
- value ref
- target exponent/frame

Outputs:
- projected closed value
- exact error bound
- provenance event

Kernel signature:

```cpp
struct ReprojectOut {
  VdrRef projected;
  VdrRef error_bound;
  uint32_t event_id;
};

__global__ void vdr_reproject_qbasis_batch(
  const VdrRef* in_vals,
  int count,
  int target_exp,
  ReprojectOut* out
);
```

## 7. Dense exact ML path

## 7.1 Tensor storage classes

Three storage classes are defined.

### T0: Shared-frame dense tensor

- all entries use same implicit denominator frame
- numerators stored densely
- highest throughput

### T1: Dense tensor with spill tags

- main tensor stores fixed-width values
- per-entry tag indicates closed vs spill
- spill entries reference active pool

### T2: Sparse active tensor

- only used when active density exceeds threshold
- stored as sparse coordinates or tile-local spill lists

The runtime should default to T0 and spill into T1 only when necessary.

## 7.2 Embedding lookup

Embedding tables shall be stored as shared-frame dense tensors where possible.

Inputs:
- token IDs
- embedding matrix handle

Outputs:
- dense tensor slice in shared frame

Kernel:

```cpp
__global__ void embedding_lookup_qframe(
  const uint32_t* token_ids,
  const Q335_32* table,
  int vocab_size,
  int dim,
  Q335_32* out
);
```

## 7.3 Exact attention

Attention score pipeline:

1. exact Q·K^T
2. exact causal mask application
3. normalization:
   - Taylor-exp softmax, or
   - rational surrogate
4. exact weight/value mix
5. residual add

Normative recommendation for GPU:
- use rational surrogate for primary path
- reserve truncated transcendental path for special mode

### Rational surrogate example

For row logits \(z_i\), shift \(m\), constant \(c\):

$$
s_i = \frac{(z_i - m + c)^2}{\sum_j (z_j - m + c)^2}
$$

Mechanical GPU decomposition:
- row max/shift kernel
- square kernel
- row sum reduction
- division kernel

Pseudo-kernels:

```cpp
__global__ void attn_shift_square(
  const Q335_32* logits,
  const Q335_32* row_shift,
  Q335_32 c,
  int rows,
  int cols,
  Q335_32* numerators
);

__global__ void row_sum_qframe(
  const Q335_32* in,
  int rows,
  int cols,
  Q335_32* out_sums
);

__global__ void normalize_by_row_sum(
  const Q335_32* numerators,
  const Q335_32* sums,
  int rows,
  int cols,
  VdrRef* out_weights
);
```

## 7.4 Feedforward and activations

Recommended activation:
- ReLU
- or rational piecewise polynomial if later extended

ReLU kernel:

```cpp
__global__ void relu_qframe(
  const Q335_32* in,
  int n,
  Q335_32* out
);
```

## 7.5 Gradient path

For exact training, the backward graph shall be represented as flat op records.

```cpp
enum GradOp : uint16_t {
  G_ADD,
  G_MUL,
  G_MATMUL,
  G_RELU,
  G_SUM,
  G_DIV,
  G_NEG
};

struct GradNode {
  uint16_t op;
  uint16_t arity;
  uint32_t input_begin;
  uint32_t output_ref;
  uint32_t aux_ref;
};
```

Backward execution:
- topologically sorted node ranges
- batched by op type
- exact per-op kernels

## 8. KB storage model

## 8.1 Device-resident KB metadata

KB metadata shall be stored in SoA form.

```cpp
struct KbMetaSoA {
  uint32_t* parent;
  uint32_t* first_child;
  uint32_t* child_count;
  uint8_t* visibility;
  uint8_t* frozen;
  uint32_t* owner;
  uint32_t* created_at;
  uint32_t* modified_at;
};
```

## 8.2 Path handling

Dotted path parsing shall be host-side.

The CPU shall:
- tokenize dotted path
- resolve segment chain to KB ID
- cache path->ID
- pass only integer IDs to GPU kernels

No GPU kernel shall depend on dotted string parsing in mainline execution.

## 8.3 Fact storage

Facts shall be stored in predicate-major columnar form.

```cpp
struct FactTable {
  uint32_t* fact_ids_by_pred;
  uint32_t* pred_bucket_offset;
  uint32_t* pred_bucket_count;

  uint32_t* fact_kb_id;
  uint32_t* fact_pred_id;
  uint32_t* fact_arg_begin;
  uint16_t* fact_arity;
  uint32_t* fact_turn;
  uint32_t* fact_confidence_ref;
  uint32_t* fact_derivation_ref;
};
```

Arguments are stored in a term pool.

## 8.4 Term pool

```cpp
enum TermTag : uint8_t {
  TERM_ATOM = 0,
  TERM_VAR = 1,
  TERM_INT = 2,
  TERM_VDR = 3,
  TERM_LIST = 4,
  TERM_KBREF = 5
};

struct TermSoA {
  uint8_t* tag;
  uint32_t* payload0;
  uint32_t* payload1;
};
```

Interpretation:
- atom: `payload0 = atom_id`
- var: `payload0 = local_var_id`
- int: `payload0 = small-int or int_ref`
- vdr: `payload0 = vdr_ref`
- list: `payload0 = element_begin`, `payload1 = element_count`
- kbref: `payload0 = kb_id`

## 8.5 Atom and symbol interning

All strings shall be interned host-side before device use.

Interned domains:
- predicate names
- atom values
- path segments
- grammar nonterminals
- builtin names
- relation types
- source types

Device code shall compare only integer symbols.

## 9. Scope model on GPU

## 9.1 Scope chain

The host shall construct scope chain vectors per request.

```cpp
struct ScopeChain {
  uint32_t ids[16];
  uint8_t len;
};
```

If tree depth may exceed fixed local length, a device buffer may be used.

## 9.2 Interval acceleration

Recommended optimization:
- assign DFS in/out interval to each KB subtree

Then “fact visible in subtree” or “descendant of” becomes interval check.

```cpp
struct KbInterval {
  uint32_t in;
  uint32_t out;
};
```

This enables fast scope filtering kernels.

## 9.3 Scope filter kernel

```cpp
__global__ void filter_facts_by_scope(
  const uint32_t* fact_kb_id,
  int fact_count,
  const uint32_t* visible_kbs,
  int visible_count,
  uint8_t* out_mask
);
```

Alternative:
- binary search visible IDs
- bitset membership
- interval test plus shadow-resolution pass

## 10. Prolog execution model

## 10.1 Execution strategy

The GPU Prolog subsystem shall use frontier-based execution.

It shall not require recursive per-thread DFS for mainline rule evaluation.

A query is evaluated as:

- candidate fact retrieval by predicate
- term compatibility filter
- unification to produce binding frontier
- rule-body joins
- solution emission
- optional host-driven backtracking refinement

## 10.2 Query representation

```cpp
struct QueryGoal {
  uint32_t pred_id;
  uint32_t arg_begin;
  uint16_t arity;
};

struct QueryPlan {
  uint32_t goal_begin;
  uint16_t goal_count;
  uint16_t mode; // find-all / first
  uint32_t scope_ref;
};
```

## 10.3 Binding representation

Bindings shall be fixed small maps where possible.

```cpp
struct BindingRow {
  uint32_t var_begin;
  uint16_t var_count;
  uint16_t flags;
};

struct BindingValue {
  uint32_t var_id;
  uint32_t term_ref;
};
```

For most rules, local variables are small. Device kernels may keep temporary bindings in registers/shared memory, then spill rows to global buffers.

## 10.4 Unification kernel

Inputs:
- query goal
- candidate fact range
- term pool
- existing frontier bindings

Outputs:
- success mask
- extended binding rows

Kernel sketch:

```cpp
__global__ void unify_goal_candidates(
  QueryGoal goal,
  const uint32_t* candidate_fact_ids,
  int candidate_count,
  TermSoA terms,
  FactTable facts,
  const BindingRow* in_rows,
  int in_row_count,
  BindingRow* out_rows,
  uint32_t* out_count
);
```

Unification rules:
- atom == atom by symbol ID
- int == int by exact value
- KB ref == KB ref by ID
- VDR == VDR by value equality policy
- var binds if unbound, else must match existing binding
- lists require equal length and recursive element match

## 10.5 Rule evaluation as joins

A rule body with multiple goals becomes chained joins.

Example rule:

```prolog
root_cause(X) :- symptom(X, S), confirmed(S), active(X).
```

Execution:
- frontier0 = candidates for `symptom(X, S)`
- frontier1 = join `confirmed(S)`
- frontier2 = join `active(X)`
- emit `X`

Recommended join strategies:
- hash join for equality keys
- sort-merge for large frontiers
- bitmap semijoin for unary filters

## 10.6 Deterministic ordering

If the system declares deterministic first-solution semantics, the host shall impose canonical ordering on:
- candidate fact order
- rule order
- join result order

GPU kernels may compute all candidates; CPU selects first by canonical order.

## 11. Rule indexing

## 11.1 Rule storage

```cpp
struct RuleTable {
  uint32_t* rule_head_pred;
  uint32_t* rule_head_arg_begin;
  uint16_t* rule_head_arity;
  uint32_t* rule_body_begin;
  uint16_t* rule_body_count;
  uint32_t* rule_kb_id;
};
```

## 11.2 Head index

Rules shall be indexed by head predicate ID.

This allows:
- query predicate -> candidate facts + candidate rules

## 12. Primitive execution model

## 12.1 Primitive classes

Primitives are divided into:

- pure GPU-eligible
- pure host-only
- operational host-only
- hybrid host/GPU

Pure GPU-eligible examples:
- VDR add/mul/div
- list aggregates
- graph ops
- probability normalization
- confidence propagation
- KB query helpers
- bitset/counter ops

Operational host-only:
- filesystem
- network
- process
- environment management

## 12.2 Primitive descriptors

All primitives shall have opcode descriptors.

```cpp
struct PrimitiveDesc {
  uint16_t opcode;
  uint16_t input_count;
  uint16_t output_count;
  uint16_t effect_mask;
  uint16_t property_mask;
  uint8_t exec_class; // GPU/CPU/HYBRID
};
```

## 12.3 Command token lowering

The LLM emits structured commands logically equivalent to:

```json
{
  "prim": "kb_query",
  "args": ["root.session.nb1", "symptom", ["?x"]],
  "store": "root.session.scratch.q1",
  "await": true
}
```

Host lowers to:

```cpp
struct Cmd {
  uint16_t opcode;
  uint16_t argc;
  uint32_t arg_begin;
  uint32_t result_slot;
  uint8_t await;
};
```

Path args are resolved before dispatch.

## 12.4 Example lowered command

Input:
- `kb_query(root.session.nb1, symptom, [?x])`

Lowered:
- `opcode = OP_KB_QUERY`
- `arg0 = kb_id 471`
- `arg1 = pred_id 88`
- `arg2 = term_range 1200..1201`

GPU receives only integers and term refs.

## 13. Live-state primitives

## 13.1 Counters

Stored as dense arrays of signed integers or VDR refs depending on exactness requirement.

Kernel example:

```cpp
__global__ void counter_add_batch(
  const uint32_t* counter_ids,
  const int64_t* deltas,
  int n,
  int64_t* counter_values,
  uint8_t* violation_flags
);
```

## 13.2 Bitsets

Use packed words.

```cpp
__global__ void bitset_set_batch(
  uint64_t* words,
  const uint32_t* positions,
  int n
);
```

## 13.3 Ring buffers

Stored as:
- fixed capacity array
- atomic write position
- optional sequence numbers

```cpp
struct RingBuffer {
  uint32_t head;
  uint32_t capacity;
  uint32_t elem_begin;
};
```

## 13.4 Queues and stacks

Implement batched push/pop only.
Single-item highly contended operations should be host-assisted or block-local.

## 13.5 LRU caches

Exact LRU is not recommended as a GPU mainline primitive under high contention.

Allowed strategies:
- host-managed exact LRU
- device approximate LRU
- batched timestamped cache with periodic host reorder

## 14. Session and clone model

## 14.1 State split

Persistent:
- facts
- rules
- constraints
- connections
- grammars

Live:
- counters
- locks
- queues
- stacks
- ring buffers
- bitsets
- scratchpad
- working data
- active scope

## 14.2 Snapshot format

A snapshot captures live-state handles and live buffers.

```cpp
struct SnapshotHeader {
  uint32_t session_id;
  uint32_t counter_begin;
  uint32_t counter_count;
  uint32_t queue_begin;
  uint32_t queue_count;
  uint32_t stack_begin;
  uint32_t stack_count;
  uint32_t ring_begin;
  uint32_t ring_count;
  uint32_t bitset_begin;
  uint32_t bitset_count;
};
```

## 14.3 Clone model

A clone is copy-on-write over persistent state.

```cpp
struct SessionHeader {
  uint32_t session_id;
  uint32_t persistent_root_kb;
  uint32_t live_state_ref;
  uint32_t parent_snapshot_ref;
  uint8_t status;
};
```

Clone creation:
- duplicate live-state refs or shallow copy immutable buffers
- create new delta arenas
- share persistent stores

Reset:
- discard live-state deltas
- restore snapshot baseline refs

Kill:
- invalidate live-state refs
- keep persistent assertions already committed

## 15. Provenance model

## 15.1 Event log storage

Provenance shall be append-only.

```cpp
struct ProvEventSoA {
  uint16_t* event_type;
  uint16_t* tool_id;
  uint32_t* subject_ref;
  uint32_t* input_begin;
  uint16_t* input_count;
  uint32_t* output_ref;
  uint32_t* confidence_ref;
  uint32_t* turn;
};
```

## 15.2 Event emission

Every primitive or rule derivation that declares provenance shall append an event row.

Device-side event append may use:
- global atomic append pointer
- block-local buffers with later compaction

## 15.3 Determinism

If deterministic event ordering is required:
- append in canonical batch order
- or sort appended ranges after kernel completion by `(turn, batch_seq, item_seq)`

## 16. Confidence propagation

## 16.1 Representation

Confidence values shall be VDR refs or fixed-frame rational values.

Preferred common case:
- denominator 100 or 10000 for bounded source confidences
- exact VDR when combining arbitrary rules

## 16.2 Core formulas

Examples:
- Prolog derivation: `min(C1..Cn)`
- agreement: `1 - product(1 - Ci)`
- script output: `min(inputs) * 95/100`

These are GPU-friendly reduction kernels.

Example agreement kernel:

```cpp
__global__ void confidence_agree(
  const VdrRef* in_conf,
  const uint32_t* ranges_begin,
  const uint32_t* ranges_count,
  int m,
  VdrRef* out
);
```

## 17. Grammar-constrained decode

## 17.1 Grammar automaton state

Each decode stream shall maintain a grammar state.

```cpp
struct GrammarState {
  uint32_t grammar_id;
  uint32_t state_id;
  uint32_t slot_type;
  uint32_t candidate_begin;
  uint32_t candidate_count;
};
```

## 17.2 Candidate domains

Candidate sources:
- fixed punctuation tokens
- enum values
- KB IDs / names
- builtin opcodes
- relation types
- free-text tokens when grammar permits

## 17.3 Mask generation

Mask generation shall occur on GPU.

```cpp
__global__ void build_vocab_mask(
  GrammarState state,
  const uint32_t* candidate_token_ids,
  int candidate_count,
  uint8_t* mask,
  int vocab_size
);
```

Alternative:
- decode over compact candidate buffer instead of full vocab

This is preferred when slot domain is small.

## 17.4 Example

If grammar slot expects one of:
- `public`
- `internal`
- `owner_only`

Then candidate token IDs are looked up once and reused; full vocab mask is unnecessary.

## 18. LLM orchestration pipeline

## 18.1 Streamed execution

Recommended concurrent streams:

- Stream 0: LLM forward/decode
- Stream 1: KB query and predicate scan
- Stream 2: VDR primitive execution
- Stream 3: grammar mask and candidate prep
- Stream 4: provenance/event compaction

CPU:
- dependency graph
- launch order
- external ops
- path resolution

## 18.2 Turn pipeline

Per turn:

1. host parses user request
2. host resolves paths and active scope
3. GPU prefetches scoped facts/rules
4. LLM begins decode
5. when command token emitted, host lowers to opcode batch
6. GPU executes pure queries/primitives
7. results stored into scratchpad or KB live slots
8. grammar masks updated
9. LLM continues decode using returned structured state
10. provenance committed
11. final response assembled

## 18.3 Example request flow

User asks:
- “Find the likely root cause from notebook N1 and summarize.”

Execution:
- host resolves notebook path to KB ID
- GPU scans `symptom/2`, `metric/3`, `dependency/2`
- GPU runs abductive candidate joins
- GPU computes confidence for each cause
- GPU sorts/ranks
- GPU writes findings into notebook scratch/ring
- grammar state constrains summary format
- LLM emits framed explanation referencing exact result rows

## 19. Functional remainder execution

## 19.1 Functional opcode model

Functional remainders shall be stored as opcode plus parameters.

```cpp
enum FnId : uint16_t {
  FN_SQRT = 1,
  FN_EXP = 2,
  FN_LOG = 3,
  FN_SIN = 4,
  FN_COS = 5,
  FN_ARCTAN = 6,
  FN_ZETA = 7
};
```

## 19.2 Evaluation model

Each functional remainder is evaluated by a specialized kernel at a requested depth.

Example:

```cpp
struct FnEvalReq {
  uint16_t fn_id;
  uint16_t depth;
  uint32_t param_begin;
  uint16_t param_count;
};
```

## 19.3 Newton example

For sqrt:
- initialize seed
- iterate depth times
- output exact rational/VDR value at that depth

```cpp
__global__ void fn_sqrt_batch(
  const FnEvalReq* reqs,
  int n,
  VdrRef* out
);
```

No device-side arbitrary callable semantics are permitted.

## 20. Memory management

## 20.1 Arena model

All irregular objects shall live in append-only arenas:

- limb arena
- VDR node arena
- remainder arena
- child list arena
- term arena
- binding arena
- provenance arena
- live-state delta arena

## 20.2 Allocation

Device allocation mechanisms:
- global bump allocator
- per-block suballocator
- prefix-sum allocation for predictable output sizes

Direct general-purpose `malloc` in kernels is prohibited in mainline execution.

## 20.3 Compaction

The host or dedicated maintenance kernels shall periodically:
- compact dead/live ranges
- rebuild indexes
- remap handles if moving GC is used

Stable handles are preferred for externally visible objects. Internal temporary buffers may be movable.

## 21. Indexing

Required indexes:

- predicate -> fact range
- rule-head predicate -> rule range
- KB subtree intervals
- connection source -> edge range
- term symbol dictionary
- grammar slot -> candidate set
- primitive opcode table

Optional indexes:
- fact `(kb_id, pred_id)` composite
- atom occurrence lists
- confidence source type ranges
- mount source/target maps

## 22. Operational primitives boundary

Operational primitives remain host-side.

GPU participation is limited to:
- preparing pure argument material
- analyzing fetched results after host retrieval
- converting boundary values into VDR forms

Example host flow for `network_fetch`:
1. LLM emits command
2. host verifies grant
3. host executes network op
4. host receives payload
5. host parses or transfers raw bytes
6. GPU/CPU pure conversion stores exact values and provenance facts

## 23. IOSE mapping

Each GPU or host primitive shall have a descriptor that includes:

- opcode
- input type list
- output type list
- side effect mask
- properties
- exec class
- deterministic flag
- exactness flag

Example:

```cpp
struct IoseDesc {
  uint16_t opcode;
  uint16_t inputs_begin;
  uint16_t inputs_count;
  uint16_t outputs_begin;
  uint16_t outputs_count;
  uint32_t side_effect_mask;
  uint32_t property_mask;
  uint8_t exec_class;
  uint8_t deterministic;
  uint8_t exact;
};
```

## 24. Error handling

## 24.1 Result encoding

All partial ops shall return status.

```cpp
enum StatusCode : uint16_t {
  ST_OK = 0,
  ST_DIV_ZERO = 1,
  ST_DOMAIN = 2,
  ST_OOB = 3,
  ST_GRANT_DENIED = 4,
  ST_CONSTRAINT = 5,
  ST_ALLOC = 6
};

struct ResultRef {
  uint16_t status;
  uint16_t flags;
  uint32_t value_ref;
};
```

## 24.2 Constraint violations

Constraint violations shall:
- set status
- optionally emit event
- optionally write violation row
- not silently disappear

## 25. Determinism requirements

Where a primitive or query is declared deterministic, the runtime shall ensure:

- canonical input order
- stable candidate ordering
- stable reduction order if exact arithmetic requires it
- stable provenance/event ordering
- stable session-visible IDs

GPU nondeterminism from atomics shall be isolated to areas where order is explicitly irrelevant or later canonicalized.

## 26. Performance strategy

## 26.1 Mainline optimization assumptions

The runtime depends on these assumptions for viability:

- most values remain in fixed-frame closed form
- active spills are minority cases
- most KB access is via indexed predicate scans, not full scans
- most rule evaluation can be expressed as joins over moderate frontiers
- path parsing stays on CPU
- strings are interned
- grammar narrows decode candidate sets substantially

## 26.2 Active spill thresholding

A tensor or query working set should switch representation when active density exceeds threshold.

Suggested thresholds:
- `< 1%`: dense closed with sparse spill
- `1% - 10%`: tile-local spill tables
- `> 10%`: sparse active mode or host intervention

## 27. Security and isolation

GPU runtime shall not directly execute external code.
All external execution remains through host-managed environments.

Data visibility checks shall be enforced before GPU query launch where possible.
GPU kernels operate only on already-authorized views or filtered scopes.

## 28. Example: fact query

### Query
Find all `age(bob, X)` in active scope.

### Lowered goal

```text
pred_id = P_AGE
args = [ATOM_BOB, VAR_X]
scope = [kb17, kb4, kb1]
```

### Device flow
1. host gets predicate bucket for `P_AGE`
2. GPU scope-filters facts in bucket
3. GPU unifies arg0 with `ATOM_BOB`
4. GPU binds arg1 to `X`
5. result rows emitted

### Sketch

```cpp
// Candidate facts:
// age(bob, 32)
// age(alice, 27)
// age(bob, 67) in different scope

// After scope filter + unify:
// result = [X = 32]
```

## 29. Example: rule join

Rule:

```prolog
eligible(X) :- active(X), score(X, S), above(S, 80).
```

### Device plan

- bucket scan `active/1`
- join with `score/2` on X
- join with `above/2` or evaluate builtin compare
- emit `eligible(X)`

### Pseudocode

```cpp
frontier0 = unify(active(X))
frontier1 = join(frontier0, score(X,S))
frontier2 = filter(frontier1, S > 80)
emit(X)
```

## 30. Example: exact surrogate attention row

Given logits:
- 1
- 2
- 3

Choose:
- `m = 0`
- `c = 1`

Numerators:
- \((1+1)^2 = 4\)
- \((2+1)^2 = 9\)
- \((3+1)^2 = 16\)

Sum:
- \(29\)

Weights:
- \(4/29\)
- \(9/29\)
- \(16/29\)

This maps to:
- elementwise exact square
- exact row reduction
- exact per-element divide

## 31. Example: command execution pipeline

LLM emits logical command:
- `counter_inc(root.nb.steps_executed)`

Host lowers:
- resolve path -> `kb_id=471`, `counter_slot=3`
- opcode -> `OP_COUNTER_INC`

GPU executes:
- atomic increment `counter[session_live_base + slot]`

Provenance emits:
- event type `SE07`
- subject `counter_ref`
- tool `OP_COUNTER_INC`

## 32. Example: active spill on multiply

Suppose two Q335 numerators multiply and product low bits are nonzero.

Result:
- current frame quotient in Q335
- low 335 bits become atomic remainder or normalized composite child

Device output:
- dense tensor entry stores `tag = spill`
- spill table row stores `VdrNode(tag=ACTIVE, ...)`

This lets dense compute continue while exact overflow is preserved structurally.

## 33. Example: grammar-constrained decode

Current grammar slot:
- visibility enum

Allowed candidates:
- `public`
- `internal`
- `owner_only`

Device builds compact candidate list:
- `[tok_public, tok_internal, tok_owner_only]`

Decode uses only these candidates, not full vocab.

## 34. Minimal API boundary

Host-to-device requests shall use compact structs.

```cpp
struct QueryRequest {
  uint32_t request_id;
  uint32_t query_plan_ref;
  uint32_t scope_ref;
  uint32_t out_buffer_ref;
};

struct PrimitiveRequest {
  uint32_t request_id;
  uint16_t opcode;
  uint16_t argc;
  uint32_t arg_begin;
  uint32_t out_ref;
};
```

## 35. Testing requirements

The implementation shall include coverage for:

Arithmetic:
- Q-frame add/sub/mul/divmod split
- cross-mul compare
- normalization
- reprojection with logged error

KB:
- path-to-ID resolution correctness
- scope visibility
- shadowing behavior

Prolog:
- atom/int/VDR/list/KBref unification
- multi-goal join correctness
- deterministic first-solution ordering

LLM:
- grammar masking correctness
- command token lowering
- exact surrogate attention sum-to-one

Sessions:
- snapshot/restore
- clone isolation for live state
- persistent fact sharing

Provenance:
- event append correctness
- declared-vs-actual side effect checks

## 36. Recommended implementation phases

### Phase 1
- Q335 arithmetic backend
- closed dense tensor kernels
- surrogate attention
- confidence kernels

### Phase 2
- KB metadata + fact tables on GPU
- scope filtering
- interned terms
- simple fact queries

### Phase 3
- frontier-based unification
- rule joins
- binding buffers
- scratchpad/ring/counter/bitset

### Phase 4
- active spill arena
- normalization passes
- functional remainder opcodes

### Phase 5
- full command pipeline
- grammar-constrained decode integration
- provenance/event subsystem
- snapshot/clone runtime

## 37. Reference snippets

### 37.1 Interned atom comparison

```cpp
__device__ inline bool atom_eq(uint32_t a, uint32_t b) {
  return a == b;
}
```

### 37.2 KB ref comparison

```cpp
__device__ inline bool kbref_eq(uint32_t a, uint32_t b) {
  return a == b;
}
```

### 37.3 Small binding lookup

```cpp
__device__ int find_binding(
  const BindingValue* vals,
  int count,
  uint32_t var_id
) {
  for (int i = 0; i < count; ++i) {
    if (vals[i].var_id == var_id) return i;
  }
  return -1;
}
```

### 37.4 Unary fact filter kernel sketch

```cpp
__global__ void filter_unary_atom_goal(
  uint32_t pred_id,
  uint32_t atom_id,
  const FactTable facts,
  const TermSoA terms,
  const uint32_t* cand_fact_ids,
  int n,
  uint8_t* out_mask
) {
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i >= n) return;

  uint32_t fid = cand_fact_ids[i];
  if (facts.fact_pred_id[fid] != pred_id) {
    out_mask[i] = 0;
    return;
  }
  if (facts.fact_arity[fid] != 1) {
    out_mask[i] = 0;
    return;
  }

  uint32_t t = facts.fact_arg_begin[fid];
  out_mask[i] = (terms.tag[t] == TERM_ATOM && terms.payload0[t] == atom_id);
}
```

### 37.5 Counter increment

```cpp
__global__ void counter_inc(
  int64_t* counters,
  const uint32_t* ids,
  int n
) {
  int i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < n) atomicAdd(&counters[ids[i]], 1LL);
}
```

## 38. Non-goals

This specification does not define:

- proof of mathematical correctness of VDR itself
- semantic evaluation of the source architecture
- external environment sandbox implementation details
- a specific GPU vendor API
- optimized tensor-core emulation for exact arithmetic
- full garbage collector design

## 39. Final implementation guidance

The decisive implementation principle is:

- keep the common path flat, fixed-width, and batchable
- isolate exact irregularity into sparse append-only structures
- compile logic into joins/frontiers instead of recursive interpreters
- keep orchestration and OS-facing operations on CPU
- keep data resident on GPU once resolved into integer handles

In practical terms, the best hardware-shaped form of the system is:

- VDR core as fixed-limb integer kernels plus active spill arena
- KB as columnar GPU graph/relational store
- Prolog as a GPU join/unification engine
- LLM as a grammar-constrained planner over integer-addressed data
- CPU as scheduler, resolver, and external operations bridge

If you want, I can next turn this into one of these:

1. a CUDA-oriented spec with kernel signatures and memory diagrams
2. a Zig/CUDA mixed implementation plan
3. a formal schema for all device structs and buffers
4. an end-to-end example with a toy inference notebook executed across CPU/GPU
