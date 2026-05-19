# VDR-LLM-Prolog Build Specification

## What To Write, How To Test, How To Deploy

---

## Part 1: What Needs To Be Written

---

### 1.1 Build Order

Everything depends on the arithmetic. The arithmetic depends on nothing. Build bottom-up.

```
Phase 1: Arithmetic + KB Store          → can test locally, no GPU
Phase 2: Prolog + Grammar + Session     → can test locally, no GPU
Phase 3: Inference Loop + Builtins      → needs CPU LLM (toy model)
Phase 4: Runners + Server               → needs CPU, network
Phase 5: TensorProlog GPU Kernels              → needs GCP GPU instance
Phase 6: Production Integration         → needs GCP, multi-instance
```

Each phase produces a testable system. Each phase's tests remain valid for all subsequent phases. Nothing gets rewritten — later phases add modules, not replace them.

---

### 1.2 Phase 1: Arithmetic + KB Store

This is the VDR-32 Zig implementation extended with KB storage. The arithmetic already exists. The KB store is new code.

#### 1.2.1 Files to Write

```
src/
├── vdr/
│   ├── q16.zig              # VDR Q16 type and operations
│   ├── q32.zig              # VDR Q32 type and operations
│   ├── q335.zig             # VDR Q335 type and operations (Phase 3, stub now)
│   ├── reproject.zig        # Q-basis conversion
│   └── types.zig            # shared type definitions, vlp_qbasis enum
│
├── kb/
│   ├── store.zig            # KB store: create, destroy, get, list
│   ├── fact.zig             # fact store: assert, query, retract, search
│   ├── tree.zig             # parent/child relationships, ancestor walk
│   ├── path_index.zig       # dotted path → kb_id hash map
│   ├── visibility.zig       # access check: scope walk + integer comparison
│   ├── text_store.zig       # append-only text blob store
│   └── types.zig            # vlp_kb, vlp_fact, vlp_provenance, vlp_fact_tag
│
├── test/
│   ├── test_q16.zig         # arithmetic tests (port from existing 884-test suite)
│   ├── test_kb_store.zig    # KB CRUD
│   ├── test_fact_store.zig  # fact assert/query/retract
│   ├── test_tree.zig        # parent/child/ancestor walk
│   ├── test_path_index.zig  # path resolution
│   └── test_visibility.zig  # access control
│
└── build.zig                # Zig build file
```

#### 1.2.2 Module Specifications

**vdr/q16.zig** (~400 lines)

```
pub const Q16 = struct {
    v: i32,
    r0: i16,

    pub const D: i32 = 65536;

    pub fn add(a: Q16, b: Q16) -> Q16
    // Same D: v = a.v + b.v. Carry: if r0 sum >= D, increment v.
    // No branching on overflow — i32 addition cannot overflow from two
    // Q16 values because max v is bounded by application (model weights
    // are initialized in range, gradients are bounded by learning rate).
    // For safety: add with overflow detection as debug-mode assertion.

    pub fn sub(a: Q16, b: Q16) -> Q16
    // v = a.v - b.v. Borrow from r0 if needed.

    pub fn mul(a: Q16, b: Q16) -> Q16
    // Widening multiply: product = @as(i64, a.v) * @as(i64, b.v)
    // v = @intCast(i32, product >> 16)  — quotient
    // r0 = @intCast(i16, product & 0xFFFF)  — remainder
    // This is THE instruction. The paper's entire hardware argument
    // rests on this being a widening multiply + shift.

    pub fn div(a: Q16, b: Q16) -> Q16
    // a * reciprocal(b). reciprocal(b) = D*D / b.v with remainder.
    // Active division caveat: if b.r0 != 0, scalar projection.
    // Logged. Not silent.

    pub fn compare(a: Q16, b: Q16) -> i32
    // Cross-multiply: a.v * Q16.D vs b.v * Q16.D.
    // Since both use same D, simplifies to: a.v vs b.v.
    // Returns -1, 0, or 1. Exact.

    pub fn compact(self: *Q16) -> void
    // If r0 >= D: impossible at i16 with D=65536 (i16 max is 32767).
    // So compact is a no-op for Q16. Relevant for Q32/Q335.

    pub fn remainderMagnitude(self: Q16) -> i32
    // Returns absolute value of r0. For precision monitoring.

    pub fn fromFraction(num: i32, den: i32) -> Q16
    // v = (num * D) / den. r0 = (num * D) % den mapped to i16.

    pub fn toFraction(self: Q16) -> struct { num: i32, den: i32 }
    // num = v, den = D. Exact representation.

    pub fn eql(a: Q16, b: Q16) -> bool
    // a.v == b.v and a.r0 == b.r0. Integer equality.

    pub fn zero() -> Q16
    // v=0, r0=0.

    pub fn one() -> Q16
    // v=D, r0=0. Represents 1/1.
};
```

**kb/store.zig** (~500 lines)

```
pub const KBStore = struct {
    kbs: []VlpKB,              // contiguous array, indexed by kb_id
    kb_count: i32,
    kb_capacity: i32,

    facts: []VlpFact,          // contiguous fact store
    fact_count: i64,
    fact_capacity: i64,

    text: TextStore,           // append-only text blob
    path_index: PathIndex,     // dotted path → kb_id

    pub fn init(config: KBStoreConfig) -> KBStore
    // Allocates arrays. Zeroes everything.
    // Sets all fact slots to TAG_EMPTY.

    pub fn createKB(self: *KBStore, config: KBCreateConfig) -> i32
    // Allocates next KB struct. Assigns sequential id.
    // Allocates fact slots (contiguous chunk).
    // Registers dotted path in path_index.
    // Adds to parent's children list.
    // Returns kb_id.

    pub fn destroyKB(self: *KBStore, kb_id: i32) -> VlpStatus
    // Reparents children. Marks KB as destroyed.
    // Facts remain in fact store but tagged EMPTY.

    pub fn getKB(self: *KBStore, kb_id: i32) -> ?*VlpKB
    // Bounds check. Returns pointer or null.

    pub fn resolvePath(self: *KBStore, path: []const u8) -> ?i32
    // Hash lookup. Returns kb_id or null.
};
```

**kb/fact.zig** (~350 lines)

```
pub const FactStore = struct {

    pub fn assert(store: *KBStore, kb_id: i32, slot_id: i32, fact: *const VlpFact) -> VlpStatus
    // Validates kb_id, slot_id, frozen flag. All integer checks.
    // Computes physical offset: kb.facts_offset + slot_id.
    // Writes fact. Updates kb.last_modified.

    pub fn query(store: *KBStore, kb_id: i32, slot_id: i32) -> ?VlpFact
    // Computes offset. Reads. Returns null if TAG_EMPTY.
    // O(1). Two integer operations to get the address.

    pub fn retract(store: *KBStore, kb_id: i32, slot_id: i32) -> VlpStatus
    // Sets tag to TAG_EMPTY at offset.

    pub fn search(store: *KBStore, kb_id: i32, tag: VlpFactTag, results: []VlpFact) -> i32
    // Linear scan of kb's fact slots. Returns matches up to results.len.
    // Returns count found.

    pub fn scopedSearch(store: *KBStore, start_kb_id: i32, tag: VlpFactTag, results: []VlpFact) -> i32
    // Walk from start_kb_id up parent chain.
    // At each KB: search for tag. If found, return.
    // This is lexical scoping.
};
```

**kb/visibility.zig** (~200 lines)

```
pub fn checkAccess(store: *KBStore, user_id: i32, user_visibility: i8, kb_id: i32) -> bool
// The gate. Makes data absent, not filtered.
// Algorithm:
//   1. Load KB. Check visibility field.
//   2. PUBLIC → true.
//   3. INTERNAL → user_visibility <= INTERNAL.
//   4. OWNER_ONLY → user_id == kb.owner_id.
//   5. Walk parent chain. Repeat at each ancestor.
//   6. Any ancestor fails → false.
// Every step: integer load + integer compare.
// This function is called before every fact read in the command processor.
// It is the structural safety boundary.

pub fn resolveVisibleKBs(store: *KBStore, user_id: i32, user_visibility: i8, scope_kb_id: i32, visible: []i32) -> i32
// Enumerates all KBs visible from scope. Prunes subtrees on failure.
// Returns count of visible kb_ids.
```

#### 1.2.3 Tests for Phase 1

```
test_q16.zig:
  - add: 0+0, 1+1, max+max, positive+negative, remainder carry
  - sub: inverse of add cases
  - mul: 0×anything, 1×anything, D/2 × D/2, remainder extraction
  - div: 1/3, 2/7, division by 1, division producing remainder
  - compare: less, equal, greater, negative values
  - fromFraction: 1/3, 1/2, 3/4, 99/100, all confidence table values
  - roundtrip: fromFraction → toFraction → fromFraction = original
  - softmax: sum of [shifted²/total²] = D for various input sets
  - determinism: same inputs → same outputs, 1000 iterations, memcmp

test_kb_store.zig:
  - create KB, verify id sequential
  - create child, verify parent/child relationship
  - destroy KB, verify children reparented
  - resolve dotted path, verify kb_id returned
  - create 1000 KBs, verify all addressable

test_fact_store.zig:
  - assert and query: value roundtrip exact
  - retract: slot becomes EMPTY
  - search by tag: correct matches returned
  - scoped search: finds fact in ancestor, not in sibling
  - assert to frozen KB: returns error
  - assert to full KB: returns error

test_visibility.zig:
  - PUBLIC KB: accessible by any user
  - INTERNAL KB: accessible by internal, not by owner_only-limited user
  - OWNER_ONLY KB: accessible only by owner
  - nested visibility: PUBLIC child under OWNER_ONLY parent → invisible
  - 10-level deep tree: visibility check at each level
```

**Estimated lines:** ~2,500
**Estimated time:** 1-2 weeks for an experienced Zig developer

---

### 1.3 Phase 2: Prolog + Grammar + Session

Builds on Phase 1. Adds deduction, formatting, and lifecycle.

#### 1.3.1 Files to Write

```
src/
├── prolog/
│   ├── term.zig             # term representation and construction
│   ├── unify.zig            # unification algorithm
│   ├── query.zig            # depth-first search with backtracking
│   ├── rule.zig             # rule storage, fire, apply actions
│   ├── hygiene.zig          # stale/failing/orphan detection
│   └── types.zig            # vlp_term, vlp_rule, vlp_binding, etc.
│
├── grammar/
│   ├── compile.zig          # template parsing and slot extraction
│   ├── render.zig           # fill slots, produce output bytes
│   ├── validate.zig         # structural validity check
│   ├── inherit.zig          # walk KB tree for grammar lookup
│   └── types.zig            # vlp_grammar, vlp_grammar_slot, vlp_grammar_fill
│
├── session/
│   ├── lifecycle.zig        # create, destroy, snapshot, restore, clone, merge, kill
│   ├── cow.zig              # copy-on-write page management
│   ├── snapshot.zig         # binary serialization/deserialization
│   └── types.zig            # vlp_session, vlp_snapshot_header
│
├── primitives/
│   ├── lru.zig              # bounded LRU cache
│   ├── counter.zig          # bounded clamping counter
│   ├── lock.zig             # non-blocking coordination signal
│   ├── queue.zig            # bounded FIFO
│   ├── stack.zig            # bounded LIFO
│   ├── ring.zig             # fixed-size ring buffer
│   ├── bitset.zig           # fixed-size bit array
│   └── types.zig            # shared primitive types
│
├── safety/
│   ├── grant.zig            # grant create, check, revoke, cleanup
│   ├── audit.zig            # append-only audit ring buffer
│   └── types.zig            # vlp_grant, vlp_audit_entry
│
├── confidence/
│   ├── propagate.zig        # confidence assignment, combination, chain
│   └── types.zig            # confidence table, source type enum
│
└── test/
    ├── test_prolog_unify.zig
    ├── test_prolog_query.zig
    ├── test_prolog_rules.zig
    ├── test_prolog_hygiene.zig
    ├── test_grammar_compile.zig
    ├── test_grammar_render.zig
    ├── test_grammar_inherit.zig
    ├── test_session_lifecycle.zig
    ├── test_session_snapshot.zig
    ├── test_session_clone.zig
    ├── test_primitives_all.zig
    ├── test_grant.zig
    ├── test_audit.zig
    └── test_confidence.zig
```

#### 1.3.2 Key Module Specifications

**prolog/unify.zig** (~300 lines)

```
pub fn unify(a: *const VlpTerm, b: *const VlpTerm, bindings: *BindingSet, depth: i32) -> bool
// Recursive unification with depth limit (100).
// Cases:
//   ATOM-ATOM: atom_id equality. Integer comparison.
//   VARIABLE-anything: check occurs check (variable doesn't appear in term).
//     If clear: bind variable to term.
//   VDR-VDR: cross-multiply.
//     a.vdr.v * Q16.D vs b.vdr.v * Q16.D.
//     Since same D, just a.vdr.v == b.vdr.v AND a.vdr.r0 == b.vdr.r0.
//     Exact. No tolerance.
//   COMPOUND-COMPOUND: functor_id match, then unify each arg pair.
//   LIST-LIST: unify heads, then unify tails.
//   Mismatched types: fail.
// Every comparison is integer. No float anywhere in unification.
```

**prolog/query.zig** (~400 lines)

```
pub fn query(store: *KBStore, start_kb_id: i32, goal: *const VlpTerm, config: QueryConfig, results: *QueryResults) -> VlpStatus
// Depth-first search with backtracking.
// 1. Collect candidate facts from KB (scoped search up parent chain).
// 2. For each candidate: attempt unification with goal.
// 3. If goal is a rule head: collect body goals, query each recursively.
// 4. Backtrack on failure: undo bindings from this branch.
// 5. Collect successful binding sets into results.
// Depth limit: config.max_depth (default 100).
// Max results: config.max_results (default 100).
// All comparison via integer unification. No approximation.
```

**grammar/render.zig** (~250 lines)

```
pub fn render(grammar: *const VlpGrammar, fills: []const VlpGrammarFill, output: []u8) -> RenderResult
// Walk template bytes:
//   Literal range → memcpy to output.
//   Slot marker → lookup fill by slot_index → render value to text → copy.
// Rendering:
//   VDR_VALUE → decimal string via integer division loop.
//   TEXT → copy bytes.
//   INTEGER → i32 to decimal string.
//   ENUM → copy enum value string (validated against declared set).
//   KB_REF → load fact from KB, render its value.
//   GRAMMAR → recursive render of nested grammar.
// Returns: bytes written, or error (capacity exceeded, type mismatch).
// Every structural byte came from the template. Not from LLM generation.
```

**session/snapshot.zig** (~350 lines)

```
pub fn save(session: *VlpSession, store: *KBStore) -> VlpSnapshot
// 1. Collect all KBs in session's subtree.
// 2. Collect all facts for those KBs.
// 3. Collect all rules.
// 4. Collect all terms referenced by rules.
// 5. Collect all text referenced by facts/rules/KBs.
// 6. Collect all grammars.
// 7. Collect all live state (primitives).
// 8. Collect all grants for session's user_id.
// 9. Pack into contiguous buffer: header + regions.
// 10. Compute CRC32 checksum over data regions.
// Result: host memory blob. Portable. Bit-identical restore guaranteed.

pub fn restore(snapshot: *const VlpSnapshot, session: *VlpSession, store: *KBStore) -> VlpStatus
// 1. Validate magic, version, checksum. Hard fail on mismatch.
// 2. Overwrite session's KB subtree from snapshot data.
// 3. Overwrite fact store region.
// 4. Overwrite rule store region.
// 5. Overwrite term store region.
// 6. Overwrite text store region.
// 7. Overwrite grammar store region.
// 8. Overwrite live state region.
// 9. Reset session metadata to snapshot values.
// After restore: session state == snapshot state. Every byte.

pub fn diff(a: *const VlpSnapshot, b: *const VlpSnapshot) -> SnapshotDiff
// Byte-by-byte comparison of each region.
// Reports: which facts differ, which rules differ, which live state differs.
// Every difference is a real change. Not float noise. Real.
```

**session/cow.zig** (~300 lines)

```
pub const COWPageTable = struct {
    // Page size: 4096 bytes (one page ≈ 100 facts at 40 bytes each).
    // Clone's page table: array of page entries.
    // Each entry: { source_page_ptr, private_page_ptr, dirty: bool }
    // Initially: all source_page_ptr point to parent's pages. dirty = false.
    // On first write to a page:
    //   1. Allocate private page.
    //   2. Copy parent's page to private page.
    //   3. Set private_page_ptr, set dirty = true.
    //   4. Write goes to private page.
    // Subsequent reads: if dirty, read from private. Otherwise read from parent.
    // Merge: iterate dirty pages, apply to parent.

    pages: []COWPage,
    n_pages: i32,

    pub fn read(self: *COWPageTable, page_id: i32) -> *const u8
    // If dirty: return private. Else: return source.

    pub fn writeBegin(self: *COWPageTable, page_id: i32) -> *u8
    // If not dirty: copy source to private, mark dirty.
    // Return private page pointer for writing.

    pub fn dirtyPages(self: *COWPageTable) -> []i32
    // List of page_ids that were modified. For merge.

    pub fn resolve(self: *COWPageTable) -> void
    // Copy all source pages to private. After resolve, no shared pages.
    // Used before snapshot to make snapshot self-contained.
};
```

#### 1.3.3 Tests for Phase 2

```
test_prolog_unify.zig:
  - atom-atom: same → succeed, different → fail
  - variable-atom: binds correctly
  - variable-variable: binds to each other
  - VDR-VDR: equal values succeed, different fail. Cross-multiply exact.
  - compound: matching functor+arity → unify args. Mismatch → fail.
  - list: [1,2,3] unifies with [1|[2,3]]. Recursive.
  - depth limit: deeply nested term hits limit, returns failure not crash.
  - occurs check: X = f(X) fails.

test_prolog_query.zig:
  - simple fact query: parent(tom, bob) matches parent(tom, X) with X=bob
  - scoped query: finds fact in ancestor KB, not in sibling
  - rule query: grandparent rule fires from parent facts
  - backtracking: multiple solutions collected
  - no match: returns zero results
  - depth limit: recursive rule stops at limit

test_prolog_rules.zig:
  - assert rule, fire, verify action executed
  - fire_and_commit: facts modified in KB
  - rule statistics: fire_count increments, last_fired updated
  - multiple rules: all matching rules fire

test_prolog_hygiene.zig:
  - stale rule (last_fired > 90 days ago): detected
  - failing rule (success_rate < 20%): detected
  - orphan rule (references revoked grant): detected
  - healthy rule: not detected

test_grammar_compile.zig:
  - simple template: "hello {name:text}" → 1 slot, type TEXT
  - multi-slot: "{a:integer} + {b:integer} = {c:integer}" → 3 slots
  - enum slot: "{status:enum(ok|error|pending)}" → validates values
  - nested braces in literal: escaped correctly
  - invalid template: mismatched braces → error
  - VDR slot: "{value:vdr_value}" → SLOT_VDR_VALUE type

test_grammar_render.zig:
  - fill text slot: "hello {name:text}" + name="world" → "hello world"
  - fill integer slot: renders as decimal string
  - fill VDR slot: renders as decimal fraction
  - fill enum slot: valid value → renders. Invalid → error.
  - capacity exceeded: returns error, partial output not written
  - JSON template: every brace, colon, comma from template

test_session_lifecycle.zig:
  - create, assert fact, query fact, destroy → fact accessible until destroy
  - snapshot + restore: state identical after restore (byte compare)
  - snapshot + modify + restore: modifications reverted exactly
  - clone: child sees parent's facts via COW
  - clone + modify child: parent unchanged
  - clone + modify parent: child unchanged (COW isolation)
  - merge: child's changes applied to parent
  - merge conflict: detected and reported
  - kill: immediate, no snapshot, clean

test_primitives_all.zig:
  - LRU: insert up to capacity → all present. Insert one more → oldest evicted.
  - Counter: increment, decrement, clamp at min, clamp at max, no wrap.
  - Lock: acquire → true. Acquire again → false. Release → acquire succeeds.
  - Queue: push/pop FIFO order. Push when full → false. Pop when empty → false.
  - Stack: push/pop LIFO order. Same bounds.
  - Ring: write past capacity → oldest overwritten. Read by index.
  - Bitset: set, clear, get, popcount. Fixed size.

test_grant.zig:
  - create grant, check → allowed
  - check wrong class → denied
  - check wrong user → denied
  - use limited grant: remaining decrements. At zero → denied.
  - expired grant: denied after expiry timestamp
  - revoked grant: permanently denied

test_confidence.zig:
  - assign from each source type: matches table
  - combine agreeing: two 95/100 → 9975/10000 (exact Q16)
  - combine conflicting: lower than agreeing
  - chain: 3 links at 85/100 → exact product
  - propagate through derivation: derived fact confidence = source confidence
```

**Estimated lines:** ~5,500
**Estimated time:** 2-3 weeks

---

### 1.4 Phase 3: Inference Loop + Builtins

The system becomes operational. The universal cycle runs on CPU with a toy model.

#### 1.4.1 Files to Write

```
src/
├── engine/
│   ├── cycle.zig            # the universal cycle (vlp_cycle)
│   ├── context.zig          # context builder
│   ├── command_parse.zig    # command token parser
│   ├── command_exec.zig     # command dispatcher
│   ├── scratchpad.zig       # per-turn scratchpad management
│   ├── auto_resolve.zig     # pre-LLM resolution check
│   ├── token_classify.zig   # classify generated token (command/prose/direct/end)
│   └── level_stats.zig      # L1/L2/L3 tracking
│
├── llm/
│   ├── model.zig            # model weight loading and storage
│   ├── forward.zig          # forward pass (CPU, Q16)
│   ├── attention.zig        # attention mechanism with exact softmax
│   ├── softmax.zig          # quadratic surrogate softmax
│   ├── generate.zig         # autoregressive token generation
│   ├── kv_cache.zig         # KV-cache in KB
│   └── sampling.zig         # greedy, top-k, top-p, temperature
│
├── builtins/
│   ├── dispatch.zig         # builtin_id → function dispatch table
│   ├── text.zig             # 17 text builtins
│   ├── collections.zig      # 36 collection builtins
│   ├── sets.zig             # 14 set builtins
│   ├── mappings.zig         # 15 mapping builtins
│   ├── arithmetic.zig       # 8 closed + 10 comparison + 7 rounding
│   ├── conversion.zig       # 14 conversion builtins (parse_json, to_csv, etc.)
│   ├── linalg.zig           # 24 linear algebra builtins
│   ├── stats.zig            # 16 statistics builtins
│   ├── graph.zig            # 13 graph builtins
│   ├── integer_ops.zig      # 21 integer/bit builtins
│   └── time.zig             # 10 time builtins
│
├── seed/
│   ├── init.zig             # seed layer initialization
│   ├── oso_rules.zig        # 15 engineering principles as Prolog terms
│   ├── hygiene_rules.zig    # self-maintenance rules
│   ├── confidence_table.zig # confidence values as KB facts
│   └── command_vocab.zig    # command token vocabulary
│
└── test/
    ├── test_cycle.zig       # end-to-end cycle with toy model
    ├── test_context.zig     # context assembly
    ├── test_command_parse.zig
    ├── test_command_exec.zig
    ├── test_auto_resolve.zig
    ├── test_forward.zig     # forward pass correctness
    ├── test_softmax.zig     # sum = D, always
    ├── test_generate.zig    # deterministic generation
    ├── test_kv_cache.zig    # cache in KB, snapshot/restore
    ├── test_builtins_text.zig
    ├── test_builtins_collections.zig
    ├── test_builtins_conversion.zig
    ├── test_builtins_linalg.zig
    ├── test_seed.zig
    └── test_sre_scenario.zig  # full SRE walkthrough from paper Section 10
```

#### 1.4.2 Key Module Specifications

**engine/cycle.zig** (~500 lines)

The universal cycle from Section 1 of this document. The game loop. Every runner, server handler, and interactive session calls this function.

**llm/forward.zig** (~400 lines)

```
pub fn forward(model: *const Model, input_ids: []const i32, kv_cache: *KVCache, logits: []Q16) -> void
// Full transformer forward pass in Q16. CPU scalar.
// Same code as the TensorProlog Cookbook 1.2, but calling Q16.mul/Q16.add
// instead of TensorPrologVdrGemm.
//
// For Phase 3 testing: use the VDR-32 toy model (181 params, 5-token vocab).
// The forward pass is verified correct by the existing 688ns benchmark.
// Scaling to larger models is Phase 5 (GPU).
//
// The point of Phase 3 is: the full cycle works end-to-end on CPU.
// The model is tiny but the system is complete.
```

**builtins/dispatch.zig** (~100 lines)

```
pub const BuiltinTable = struct {
    entries: [448]BuiltinEntry,

    pub fn dispatch(self: *const BuiltinTable, id: i32, args: *BuiltinArgs) -> BuiltinResult
    // Lookup by id. Validate args against IOSE declaration.
    // Call function pointer. Return result.
    // Every pure builtin is infallible on valid inputs.
};

// Phase 3 implements ~200 builtins (text, collections, sets, mappings,
// arithmetic, comparison, conversion, linalg, stats, graph, integer/bit, time).
// Remaining ~248 (operational, advanced math, FRU) are Phase 4 and Phase 5.
```

#### 1.4.3 Tests for Phase 3

The critical test is `test_sre_scenario.zig`: a scripted replay of the SRE investigation from paper Section 10.1, using the toy model for LLM judgment. The test verifies:

- KB facts created correctly at each step
- Prolog rule fires on matching pattern
- Grammar renders findings table correctly
- Confidence propagation produces exact values
- Total token count matches paper's claim (~570 for fresh system)
- Entire scenario is deterministic: run twice, identical output

**Estimated lines:** ~7,000
**Estimated time:** 3-4 weeks

---

### 1.5 Phase 4: Runners + Server

The system becomes autonomous and network-accessible.

#### 1.5.1 Files to Write

```
src/
├── runner/
│   ├── pool.zig             # thread pool management
│   ├── poller.zig           # polling runner
│   ├── processor.zig        # processor runner with recycle
│   ├── internal.zig         # internal computation runner
│   ├── batch.zig            # batch task runner
│   └── types.zig            # vlp_runner, vlp_runner_task, etc.
│
├── server/
│   ├── listener.zig         # accept loop, connection management
│   ├── handler.zig          # connection handler: clone, auth, serve
│   ├── auth.zig             # credential issue, check, revoke, cleanup
│   ├── rate_limit.zig       # exact integer rate limiting
│   ├── health.zig           # health check and metrics endpoint
│   ├── reaper.zig           # idle connection reaper
│   ├── shutdown.zig         # graceful shutdown
│   └── types.zig            # vlp_server, vlp_server_connection, vlp_credential
│
├── protocol/
│   ├── http.zig             # HTTP request/response parsing and rendering
│   ├── websocket.zig        # WebSocket frame handling
│   ├── smtp.zig             # SMTP command/response (stub, Phase 6 full)
│   ├── mqtt.zig             # MQTT packet handling (stub, Phase 6 full)
│   └── grammars.zig         # protocol grammar templates
│
├── ops/
│   ├── filesystem.zig       # grant-gated fs operations
│   ├── network.zig          # grant-gated HTTP fetch
│   ├── execute.zig          # grant-gated script execution (subprocess)
│   ├── compile.zig          # grant-gated compilation
│   └── process.zig          # grant-gated process management
│
├── config/
│   ├── system_config.zig    # vlp_system_config struct and defaults
│   ├── cli.zig              # command-line argument parsing
│   └── config_file.zig      # YAML/JSON config file parsing via builtins
│
└── test/
    ├── test_runner_poller.zig
    ├── test_runner_processor.zig
    ├── test_runner_batch.zig
    ├── test_server_http.zig
    ├── test_server_websocket.zig
    ├── test_server_auth.zig
    ├── test_server_rate_limit.zig
    ├── test_server_shutdown.zig
    ├── test_ops_filesystem.zig
    ├── test_ops_network.zig
    └── test_integration_full.zig  # full system: server + runners + client
```

**Estimated lines:** ~6,000
**Estimated time:** 3-4 weeks

---

### 1.6 Phase 5: TensorProlog GPU Kernels

The system moves to GPU. This is the first phase that requires GCP.

#### 1.6.1 Files to Write

```
src/
├── gpu/
│   ├── device.zig           # TensorProlog device init, memory layout, stream management
│   ├── kernel_mac.zig       # Q16 matrix multiply-accumulate kernel
│   ├── kernel_softmax.zig   # quadratic softmax surrogate kernel
│   ├── kernel_attention.zig # fused attention kernel
│   ├── kernel_layernorm.zig # exact layer norm kernel
│   ├── kernel_elementwise.zig # add, sub, mul, div, scale, compare
│   ├── kernel_prolog.zig    # parallel unification over fact tables
│   ├── kernel_sort.zig      # parallel sort for builtins
│   ├── kb_device.zig        # KB store on device memory
│   ├── transfer.zig         # host-device data transfer
│   └── profiling.zig        # performance counters
│
└── test/
    ├── test_gpu_q16_ops.zig      # arithmetic correctness on GPU
    ├── test_gpu_softmax.zig      # softmax sum = D on GPU
    ├── test_gpu_attention.zig    # attention weights correct on GPU
    ├── test_gpu_determinism.zig  # same input → same output, 100 runs
    ├── test_gpu_forward.zig      # toy model forward pass on GPU
    ├── test_gpu_prolog.zig       # parallel unification on GPU
    └── test_gpu_benchmark.zig    # throughput measurement
```

For Phase 5 on GCP: the Zig code emits PTX inline assembly or uses CUDA C kernels called via Zig's C interop. The kernels use the INT8 tensor core path on H100.

**Estimated lines:** ~4,000 (Zig) + ~2,000 (CUDA C kernels)
**Estimated time:** 4-6 weeks

---

### 1.7 Phase 6: Production Integration

Full system on GCP. Multi-instance. Real workloads.

#### 1.7.1 Files to Write

```
src/
├── deploy/
│   ├── gcp_setup.zig        # GCP instance provisioning helpers
│   ├── multi_device.zig     # model parallelism across GPUs
│   ├── distributed.zig      # multi-node allreduce (integer, deterministic)
│   ├── load_balancer.zig    # request routing across instances
│   └── monitoring.zig       # prometheus-compatible metrics export
│
├── protocol/
│   ├── smtp_full.zig        # full SMTP implementation
│   ├── mqtt_full.zig        # full MQTT implementation
│   └── dns.zig              # DNS server
│
└── test/
    ├── test_multi_gpu.zig
    ├── test_distributed.zig
    ├── test_load_test.zig   # sustained load testing
    └── test_chaos.zig       # kill instances, verify recovery
```

**Estimated lines:** ~3,000
**Estimated time:** 3-4 weeks

---

### 1.8 Total Build Summary

```
Phase 1: Arithmetic + KB Store         ~2,500 lines    1-2 weeks
Phase 2: Prolog + Grammar + Session    ~5,500 lines    2-3 weeks
Phase 3: Inference Loop + Builtins     ~7,000 lines    3-4 weeks
Phase 4: Runners + Server              ~6,000 lines    3-4 weeks
Phase 5: TensorProlog GPU Kernels             ~6,000 lines    4-6 weeks
Phase 6: Production Integration        ~3,000 lines    3-4 weeks

Total:                                 ~30,000 lines   16-23 weeks
```

Paper estimated ~20,500 lines across 65 modules. The difference is server infrastructure, protocol handlers, GCP integration, and CUDA-like kernels that the paper's build plan didn't include (it specified the architecture, not the deployment).

---

## Part 2: How To Test

### 2.1 Local Testing (Phases 1-4)

All of Phases 1-4 run on your local machine. No GPU required. No cloud.

```
# Build and test Phase 1
cd vlp-system
zig build test-phase1

# Expected output:
# test_q16: 68 tests passed, 0 failed
# test_kb_store: 12 tests passed, 0 failed
# test_fact_store: 15 tests passed, 0 failed
# test_tree: 8 tests passed, 0 failed
# test_path_index: 6 tests passed, 0 failed
# test_visibility: 10 tests passed, 0 failed
# Total: 119 tests passed, 0 failed

# Build and test Phase 2 (includes Phase 1 tests)
zig build test-phase2

# Expected output:
# Phase 1: 119 tests passed
# test_prolog_unify: 18 tests passed
# test_prolog_query: 14 tests passed
# test_prolog_rules: 10 tests passed
# test_grammar_compile: 12 tests passed
# test_grammar_render: 15 tests passed
# test_session_lifecycle: 14 tests passed
# test_session_snapshot: 8 tests passed
# test_session_clone: 10 tests passed
# test_primitives_all: 28 tests passed
# test_grant: 12 tests passed
# test_confidence: 10 tests passed
# Total: 270 tests passed, 0 failed

# Build and test Phase 3
zig build test-phase3

# Expected output (includes prior phases):
# Phase 1-2: 270 tests passed
# test_cycle: 8 tests passed
# test_forward: 12 tests passed (including softmax_sum = 65536 every time)
# test_generate: 6 tests passed (determinism: 1000 runs, identical output)
# test_builtins_*: 180 tests passed
# test_sre_scenario: 1 test passed (full investigation, 570 tokens)
# Total: 477 tests passed, 0 failed

# Build and test Phase 4
zig build test-phase4

# This starts a local HTTP server and tests against it.
# Expected output:
# Phase 1-3: 477 tests passed
# test_server_http: 20 tests passed (request/response, auth, rate limit)
# test_server_websocket: 12 tests passed (message loop, credential expiry)
# test_runner_poller: 8 tests passed (fires rules, zero LLM tokens for known patterns)
# test_runner_processor: 6 tests passed (ingest, recycle, reconnect)
# test_runner_batch: 8 tests passed (clone-per-task, merge results)
# test_integration_full: 1 test passed (server + runners + client)
# Total: 532 tests passed, 0 failed
```

### 2.2 Performance Baselines (Local)

```
# Run benchmarks on local machine (CPU only)
zig build bench

# Expected output:
# Q16 forward pass (181 params):    ~688 ns/iter (matches paper)
# Q16 softmax (5 logits):           <1 ns/iter
# Q16 dot product (d=4):            <1 ns/iter
# KB fact query:                     ~50 ns/iter
# Prolog unify (simple):             ~200 ns/iter
# Prolog query (20 facts):           ~2,000 ns/iter
# Grammar render (5 slots):          ~500 ns/iter
# Session snapshot (100 KB):         ~50,000 ns
# Session restore (100 KB):          ~30,000 ns
# Full cycle (toy model, L1):        ~5,000 ns
# Full cycle (toy model, L3):        ~3,000 ns (no LLM involved)
```

### 2.3 Determinism Verification (Local)

```
# Run determinism suite
zig build test-determinism

# This runs every operation 100 times and compares outputs byte-by-byte.
# Expected output:
# Q16 arithmetic determinism:        100/100 identical
# Forward pass determinism:          100/100 identical
# Prolog query determinism:          100/100 identical
# Grammar render determinism:        100/100 identical
# Snapshot roundtrip determinism:    100/100 identical
# Full cycle determinism:            100/100 identical
# Cross-platform determinism:        (verified when same tests pass on GCP)
```

---

## Part 3: GCP Deployment and Testing

### 3.1 GCP Instance Setup

```
# Phase 5 requires GPU. Minimum: 1x NVIDIA T4 for initial testing.
# Production: 1x H100 or A100.

# Create GCP project (if not existing)
gcloud projects create vlp-system-test --name="VLP System Test"
gcloud config set project vlp-system-test

# Enable required APIs
gcloud services enable compute.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable monitoring.googleapis.com

# Create GPU instance for Phase 5 testing
gcloud compute instances create vlp-test-gpu \
  --zone=us-central1-a \
  --machine-type=n1-standard-8 \
  --accelerator=type=nvidia-tesla-t4,count=1 \
  --boot-disk-size=100GB \
  --boot-disk-type=pd-ssd \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --metadata=startup-script='#!/bin/bash
    # Install NVIDIA drivers
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
    sudo apt-get update
    sudo apt-get install -y nvidia-driver-535 nvidia-cuda-toolkit
    # Install Zig
    wget https://ziglang.org/download/0.14.0/zig-linux-x86_64-0.14.0.tar.xz
    tar xf zig-linux-x86_64-0.14.0.tar.xz
    sudo mv zig-linux-x86_64-0.14.0 /opt/zig
    echo "export PATH=/opt/zig:\$PATH" >> /etc/profile
  '

# For H100 testing (when ready for production benchmarks):
gcloud compute instances create vlp-test-h100 \
  --zone=us-central1-a \
  --machine-type=a3-highgpu-1g \
  --accelerator=type=nvidia-h100-80gb,count=1 \
  --boot-disk-size=200GB \
  --boot-disk-type=pd-ssd \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud

# For multi-GPU testing (Phase 6):
gcloud compute instances create vlp-test-multi \
  --zone=us-central1-a \
  --machine-type=a3-highgpu-8g \
  --accelerator=type=nvidia-h100-80gb,count=8 \
  --boot-disk-size=500GB \
  --boot-disk-type=pd-ssd \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

### 3.2 Upload and Build on GCP

```
# From local machine: upload source to GCP instance
gcloud compute scp --recurse ./vlp-system vlp-test-gpu:~/vlp-system \
  --zone=us-central1-a

# SSH into instance
gcloud compute ssh vlp-test-gpu --zone=us-central1-a

# On the instance:
cd ~/vlp-system

# First: run all CPU tests to verify cross-platform determinism
zig build test-phase1
zig build test-phase2
zig build test-phase3
zig build test-phase4
# All tests must pass. Same counts as local.
# If any differ: that's a bug. The system is integer — it must be identical.

# Verify GPU is available
nvidia-smi
# Should show T4 or H100

# Build and run GPU tests (Phase 5)
zig build test-phase5

# Expected output:
# test_gpu_q16_ops:      24 tests passed (arithmetic on GPU matches CPU)
# test_gpu_softmax:      8 tests passed (softmax sum = 65536 on GPU)
# test_gpu_attention:    6 tests passed (attention weights match CPU)
# test_gpu_determinism:  12 tests passed (100 runs, all identical)
# test_gpu_forward:      4 tests passed (toy model, GPU matches CPU bit-for-bit)
# test_gpu_prolog:       6 tests passed (parallel unification matches sequential)
# Total: 60 tests passed, 0 failed

# Cross-platform determinism check:
# Compare GPU output to local CPU output (saved from local testing)
zig build test-cross-platform -- --reference-dir=./reference-outputs/
# Expected: all outputs byte-identical to CPU reference.
# This is the definitive test. Integer arithmetic is platform-independent.
# If GPU and CPU produce different results, it's a kernel bug.
```

### 3.3 GPU Benchmarks on GCP

```
# Run GPU benchmarks
zig build bench-gpu

# Expected output on T4:
# Q16 GEMM (1024x1024):             ~X ms (T4 INT8 throughput)
# Q16 softmax (1024 logits):        ~X μs
# Q16 attention (seq=512, d=64):    ~X ms
# Parallel Prolog (1000 facts):     ~X μs
# Full forward pass (toy model):    ~X ns (should be << CPU)

# Expected output on H100:
# Q16 GEMM (1024x1024):             ~X ms (H100 INT8: 3,958 TOPS)
# Q16 softmax (1024 logits):        ~X μs
# Q16 attention (seq=2048, d=128):  ~X ms
# Parallel Prolog (10000 facts):    ~X μs
# Full forward pass (toy model):    ~X ns

# Compare to paper's predictions:
# Paper claims: 2x FP16 throughput on existing INT8 path.
# H100 FP16 Tensor Core: 1,979 TFLOPS
# H100 INT8 Tensor Core: 3,958 TOPS
# Our GEMM should achieve close to 3,958 TOPS on pure INT8 path.
```

### 3.4 Integration Testing on GCP

```
# Start the full system: server + runners
zig build run -- --config=config/test_gcp.yaml --port=8080

# config/test_gcp.yaml:
# model:
#   checkpoint: ./models/toy-model-q16.ckpt
#   qbasis: Q16
#   n_layers: 1
#   d_model: 4
#   n_heads: 1
#   vocab_size: 5
# server:
#   port: 8080
#   protocol: HTTP
#   max_connections: 100
#   credential_ttl: 3600
# runners:
#   - type: poller
#     interval_ms: 60000
#   - type: internal
#     interval_ms: 300000

# From another terminal (or local machine via SSH tunnel):

# Test HTTP endpoint
curl -X POST http://localhost:8080/api/query \
  -H "Authorization: Bearer test-token-1" \
  -H "Content-Type: application/json" \
  -d '{"input": "check system health"}'

# Expected: JSON response with exact confidence fractions,
# every brace from grammar, content from KB.

# Test health endpoint
curl http://localhost:8080/health

# Expected: JSON with exact integer metrics.
# {"active_connections": 0, "total_requests": 1,
#  "l3_auto_percent": "0/1", "active_sessions": 0,
#  "rules": 15, "facts": 23400, "runners": 2}

# Test credential expiry
# Issue a short-lived credential (10 seconds)
# Make request → succeeds
# Wait 11 seconds
# Make request → returns 401 with "credential expired"
# Integer timestamp comparison. Exact.

# Test rate limiting
# Send 100 requests in 1 second
# Requests beyond limit → 429 with exact remaining count and retry-after

# Test WebSocket
# Connect, send messages, verify session persists across messages
# Let credential expire, verify close frame with code 4001

# Load test
# Use a simple script to send 1000 concurrent requests
# Verify: all responses valid JSON (grammar-rendered)
# Verify: no 500 errors (deterministic system shouldn't crash on valid input)
# Verify: metrics endpoint shows exact counts matching sent requests
```

### 3.5 Sustained Operation Test

```
# Run the system for 24 hours with simulated SRE workload.
# This tests the accumulation curve and recycle mechanism.

zig build run -- --config=config/sustained_test.yaml

# sustained_test.yaml adds:
# runners:
#   - type: processor
#     source: simulated_prometheus
#     ingest_interval_ms: 1000
#     max_turns_before_recycle: 200
#   - type: poller
#     interval_ms: 60000
#   - type: internal
#     interval_ms: 300000

# The simulated Prometheus source generates metric patterns:
# - 70% known patterns (should be handled by L3 rules after hour 2)
# - 20% variant patterns (should be handled by L2 after seen once)
# - 10% novel patterns (require L1 LLM judgment)

# After 24 hours, check:
curl http://localhost:8080/health

# Expected metrics:
# l3_auto_percent: should be > 80/100 (matching paper's projection)
# rules: should have grown from seed 15 to ~50-80
# facts: should have grown from seed 23,400 to ~30,000-50,000
# runner recycle_count: should be > 0 (processor recycled at 200 turns)
# errors_total: should be 0 (deterministic system, no float instability)

# Check accumulation:
curl http://localhost:8080/api/stats

# Expected:
# investigation_1_tokens: ~300-500 (L1, lots of data acquisition)
# investigation_10_tokens: ~80-120 (L2, rules handling known patterns)
# investigation_50_tokens: ~50-70 (mostly L3)
# This is the paper's accumulation curve in action.

# Check determinism:
# Replay the same 24-hour input sequence again.
# Compare outputs. They must be byte-identical.
# This test takes another 24 hours but proves the system is deterministic
# over sustained operation.
```

### 3.6 GCP Cost Management

```
# T4 instance: ~$0.35/hour (preemptible ~$0.11/hour)
# H100 instance: ~$12-15/hour
# Multi-GPU H100 8x: ~$100/hour

# Testing budget estimate:
# Phase 5 development + testing: ~40 hours T4 = ~$14
# Phase 5 H100 benchmarks: ~8 hours = ~$100
# Phase 6 multi-GPU: ~20 hours = ~$2,000
# Sustained operation test: ~48 hours T4 = ~$17
# Total: ~$2,200

# Cost management:
# Always stop instances when not in use
gcloud compute instances stop vlp-test-gpu --zone=us-central1-a

# Use preemptible instances for development (cheaper, may be terminated)
gcloud compute instances create vlp-dev-gpu \
  --zone=us-central1-a \
  --machine-type=n1-standard-8 \
  --accelerator=type=nvidia-tesla-t4,count=1 \
  --preemptible \
  --boot-disk-size=100GB

# Auto-shutdown after idle:
# Add to instance metadata:
# shutdown-script: 'sudo shutdown -h +30'  # shutdown after 30 min idle
```

---

## Part 4: How To Use The System

After it's built, tested, and deployed.

### 4.1 Starting The System

```
# On your GCP instance:

# Start with configuration file
vlp-system --config=production.yaml

# production.yaml:
model:
  checkpoint: /models/your-model-q16.ckpt
  qbasis: Q16
  n_layers: 32
  d_model: 4096
  n_heads: 32
  vocab_size: 32000
  mlp_dim: 11008

server:
  port: 443
  protocol: HTTP
  tls_cert: /certs/cert.pem
  tls_key: /certs/key.pem
  max_connections: 1000
  credential_ttl: 3600
  idle_timeout: 300
  persistent_sessions: true
  session_storage_path: /data/sessions/

runners:
  - type: poller
    name: triage
    interval_ms: 60000
    scope: root.ops

  - type: processor
    name: prometheus
    source:
      type: prometheus
      url: https://prometheus.internal/api/v1
      auth_token_env: PROMETHEUS_TOKEN
    max_turns_before_recycle: 200

  - type: internal
    name: derived_metrics
    interval_ms: 300000
    scope: root.ops.metrics

  - type: internal
    name: hygiene
    interval_ms: 86400000  # daily
    scope: root.system

auth:
  kb_path: root.system.auth
  admin_token_env: ADMIN_TOKEN

seed:
  snapshot_path: /data/seed/sre_seed.vlps

logging:
  audit_capacity: 1000000
  level: info

# System starts:
# 1. Loads model weights (may take minutes for large models)
# 2. Initializes KB store
# 3. Loads seed snapshot into KB tree
# 4. Starts all runners
# 5. Begins accepting connections on port 443
#
# Output:
# [INFO] Model loaded: 32 layers, 4096 d_model, Q16
# [INFO] KB store initialized: 100000 capacity
# [INFO] Seed loaded: 23400 facts, 15 rules, 12 grammars
# [INFO] Runner 'triage' started: poller, 60s interval
# [INFO] Runner 'prometheus' started: processor, connected
# [INFO] Runner 'derived_metrics' started: internal, 300s interval
# [INFO] Runner 'hygiene' started: internal, daily
# [INFO] Server listening on :443 (HTTPS)
```

### 4.2 Client Interaction

```
# Interactive HTTP API

# Authenticate and get session
curl -X POST https://your-instance.gcp/api/session \
  -H "Authorization: Bearer your-api-key" \
  -d '{"scope": "root.ops.incidents"}'

# Response:
# {"session_id": "s-47", "expires_at": 1716234567,
#  "scope": "root.ops.incidents", "user_id": 12}

# Send a query
curl -X POST https://your-instance.gcp/api/query \
  -H "Authorization: Bearer your-api-key" \
  -H "X-Session-ID: s-47" \
  -d '{"input": "checkout-api returning 503s at ~15% for 20 minutes"}'

# Response:
# (If system is mature and triage rules handle it — L3):
# {"level": "L3", "tokens": 0, "auto_triaged": true,
#  "findings": [
#    {"service": "checkout-api", "error_rate": "152/1000",
#     "confidence": "95/100", "cause": "pool_reduction",
#     "status": "investigating"}
#  ],
#  "recommended": "Run remediation script pool_restore_v3"}
#
# (If system is fresh — L1):
# {"level": "L1", "tokens": 80, "auto_triaged": false,
#  "response": "I've created an investigation for checkout-api 503s...",
#  "commands_executed": 4,
#  "artifacts_created": ["fact:inc_001.service", "fact:inc_001.error_rate"]}

# The JSON in both responses: every brace, colon, comma from grammar.
# The data values: from KB facts at integer addresses.
# The LLM's contribution: judgment about what matters (L1) or nothing (L3).

# Check session state
curl https://your-instance.gcp/api/session/s-47 \
  -H "Authorization: Bearer your-api-key"

# Response:
# {"session_id": "s-47", "turn": 1, "facts_asserted": 4,
#  "rules_fired": 47, "l1_tokens": 80, "l2_tokens": 0, "l3_tokens": 0}

# Snapshot session (for later restoration)
curl -X POST https://your-instance.gcp/api/session/s-47/snapshot \
  -H "Authorization: Bearer your-api-key"

# Response:
# {"snapshot_id": "snap-12", "size_bytes": 45632, "checksum": 2847561923}

# Restore session next week
curl -X POST https://your-instance.gcp/api/session \
  -H "Authorization: Bearer your-api-key" \
  -d '{"restore_snapshot": "snap-12"}'

# Session continues from exact prior state.
# KV-cache restored. KB facts restored. Rules restored.
# Turn 2 picks up exactly where turn 1 left off.
```

### 4.3 WebSocket Interactive Session

```
# For real-time interactive use (chatbot-style)

const ws = new WebSocket('wss://your-instance.gcp/ws');

ws.onopen = () => {
  // Authenticate
  ws.send(JSON.stringify({
    type: 'auth',
    token: 'your-api-key',
    scope: 'root.ops'
  }));
};

ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);

  if (msg.type === 'auth_ok') {
    // Session created. Send queries.
    ws.send(JSON.stringify({
      type: 'query',
      input: 'what incidents are open?'
    }));
  }

  if (msg.type === 'response') {
    console.log(msg.output);    // formatted by grammar
    console.log(msg.level);     // L1, L2, or L3
    console.log(msg.tokens);    // exact count
    console.log(msg.confidence); // exact fraction
  }

  if (msg.type === 'credential_expired') {
    // Re-authenticate
    ws.send(JSON.stringify({
      type: 'auth',
      token: 'your-api-key'
    }));
  }
};

// The WebSocket session persists.
// Message 1 creates KBs and learns patterns.
// Message 10 reuses rules from messages 1-9.
// Message 100: mostly L3, LLM rarely involved.
// The session gets cheaper and more capable over time.
```

### 4.4 Monitoring

```
# Prometheus-compatible metrics endpoint
curl https://your-instance.gcp/metrics

# Output (every value is an exact integer):
# vlp_active_connections 3
# vlp_total_requests 12847
# vlp_active_sessions 3
# vlp_total_facts 34521
# vlp_total_rules 87
# vlp_total_grammars 23
# vlp_l1_count 142
# vlp_l2_count 891
# vlp_l3_count 11814
# vlp_auto_triage_ratio_numerator 11814
# vlp_auto_triage_ratio_denominator 12847
# vlp_runner_triage_iterations 20143
# vlp_runner_triage_errors 0
# vlp_runner_prometheus_iterations 518400
# vlp_runner_prometheus_recycles 2592
# vlp_runner_prometheus_errors 0
# vlp_audit_entries_total 98234

# Key metric: vlp_auto_triage_ratio
# 11814/12847 ≈ 91.9%
# 91.9% of all operations handled without LLM involvement.
# Exact fraction, not sampled approximation.
# This number only goes up over time (accumulation).

# Set up Grafana dashboard pointing at these metrics.
# Every datapoint is exact. No sampling noise. No aggregation error.
# The graph shows the actual system state, not an approximation of it.
```

### 4.5 Administration

```
# Create user accounts
curl -X POST https://your-instance.gcp/admin/users \
  -H "Authorization: Bearer admin-token" \
  -d '{"user_id": 42, "visibility": "internal",
       "grants": [
         {"class": "network", "target": "prometheus.internal/*", "max_uses": -1},
         {"class": "execute", "target": "scripts/remediation/*", "max_uses": 10}
       ]}'

# Response:
# {"user_id": 42, "api_key": "vlp-key-...", "grants_issued": 2}

# Grant is: user 42 can fetch from prometheus.internal unlimited times,
# and can execute remediation scripts up to 10 times.
# After 10 executions: GRANT_DENIED. Need admin to issue new grant.
# No ambiguity. No "well, maybe it was 9 or 11 because of float counting."
# Integer counter. 10 means 10.

# Revoke a grant
curl -X DELETE https://your-instance.gcp/admin/grants/47 \
  -H "Authorization: Bearer admin-token"

# Permanent. Immediate. The integer flips. Next check reads false.

# Review audit log
curl https://your-instance.gcp/admin/audit?user_id=42&limit=100 \
  -H "Authorization: Bearer admin-token"

# Returns 100 most recent audit entries for user 42.
# Every access check, grant check, fact modification, rule firing.
# Complete provenance chain for any action in the system.

# System snapshot (entire KB state)
curl -X POST https://your-instance.gcp/admin/snapshot \
  -H "Authorization: Bearer admin-token"

# Response:
# {"snapshot_id": "sys-snap-1", "size_bytes": 2345678,
#  "checksum": 1923847561, "path": "/data/snapshots/sys-snap-1.vlps"}

# This snapshot is the entire system state.
# Restore it on a different GCP instance: identical system.
# Ship it to a different cloud: identical system.
# Load it next year: identical system.
# Because integers.
```

### 4.6 Upgrading

```
# To update the model:
# 1. Stop the server (graceful shutdown snapshots all sessions)
vlp-system --shutdown

# 2. Replace checkpoint
cp /new-models/improved-model-q16.ckpt /models/your-model-q16.ckpt

# 3. Restart
vlp-system --config=production.yaml

# All sessions restore from their snapshots.
# All KB facts, rules, grammars persist.
# The model changed but the knowledge didn't.
# First few turns: rules fire the same way (L3),
# but LLM judgment (L1) may produce different commands.
# The system adapts because new L1 judgments become new rules.

# To update the system code:
# 1. Build new binary
zig build -Doptimize=ReleaseFast

# 2. Graceful shutdown
vlp-system --shutdown

# 3. Replace binary
cp zig-out/bin/vlp-system /usr/local/bin/vlp-system

# 4. Restart
vlp-system --config=production.yaml

# Same snapshot restore. Same KB state. Same rules.
# Binary changed but state didn't.
# This is what "snapshot is the deployable binary" means in practice.
```

---

## Part 5: File Count and Dependency Summary

```
Total files to write:

src/vdr/          5 files    (~800 lines)
src/kb/           7 files    (~1,700 lines)
src/prolog/       6 files    (~1,500 lines)
src/grammar/      5 files    (~900 lines)
src/session/      4 files    (~1,200 lines)
src/primitives/   8 files    (~1,400 lines)
src/safety/       3 files    (~600 lines)
src/confidence/   2 files    (~300 lines)
src/engine/       8 files    (~2,000 lines)
src/llm/          7 files    (~1,800 lines)
src/builtins/     12 files   (~4,000 lines)
src/seed/         5 files    (~800 lines)
src/runner/       6 files    (~2,000 lines)
src/server/       8 files    (~2,500 lines)
src/protocol/     5 files    (~1,500 lines)
src/ops/          5 files    (~1,000 lines)
src/config/       3 files    (~500 lines)
src/gpu/          11 files   (~6,000 lines)
src/deploy/       5 files    (~1,500 lines)
test/             ~50 files  (~5,000 lines of tests)

Total: ~168 files, ~30,000 lines of code, ~5,000 lines of tests

External dependencies: ZERO for Phases 1-4 (pure Zig).
Phase 5: CUDA-like toolkit (for GPU kernel compilation).
Phase 6: GCP SDK (for deployment automation).

The system has no dependency on PyTorch, TensorFlow, JAX, ONNX,
or any ML framework. It is not built on top of anything.
It is the thing.
```
