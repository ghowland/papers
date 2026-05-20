# How the System Design Maps to TensorProlog Functions

## The architecture in one sentence

The 23 modules are the API surface of the entire system described across all prior documents. Every struct, every invariant, every data flow path from the 20 papers, the integration spec, the cookbook, the runtime engine, and the turn plan terminates at one of these ~580 functions.

## Module-by-module mapping to system design

### Module 1: TensorProlog_core — The bootstrap

This is the entry point. `TensorPrologInit` sets the global init flag that every other function checks. `DeviceGetProperties` returns the capability struct that determines which code paths are available — `max_q_basis` tells you Q16/Q32/Q335 support, `has_fru` tells you whether Module 21's functions work in hardware or need software fallback. `DeviceSetCurrent` binds a host thread to a device — all subsequent calls on that thread target that device.

The error codes are the `VlpStatus` enum from document 5 (`src/vdr/types.zig`), mapped to a C-style enum. No NaN/Inf/precision-mismatch errors because those failure categories don't exist in integer arithmetic. `ERR_DETERMINISM_VIOLATION` is the canary — if this ever fires, something is fundamentally broken, not drifted.

`DeviceReset` force-snapshots active sessions before destroying them. This connects to Module 4's snapshot system — even a hard reset preserves state.

### Module 2: TensorProlog_memory — Typed allocation

Three allocation functions, not one. `MallocTyped` is the key one — it takes a `qbasis` parameter and the compiler tracks the tag on the pointer. Passing a Q16-allocated pointer to a Q32 kernel is a compile error, not a runtime mismatch. Element sizes: Q16=8 bytes (`{v:i32, r0:i16, _pad:i16}`), Q32=16 bytes, Q335=240 bytes. These match the struct definitions from document 1 section 3.1.

`MallocKB` allocates contiguous arrays of the 26-field KB struct from document 1 section 3.1 (`vlp_kb`, padded to 256 bytes). `Memcpy` is bit-exact — this is the property that makes checkpoint portability work (document 2 section 1.1) and snapshot restore work (document 1 section 5.1).

`MemGetInfo` reports counts not fragmentation metrics because KB structs are fixed-size, so fragmentation is structurally minimal. This is a consequence of the "everything is a fixed-size struct at a fixed offset" design from document 1 section 4.

### Module 3: TensorProlog_stream — Session-aware execution

`StreamCreateWithSession` is the critical function. It binds a GPU stream to a session, and all kernels launched on that stream inherit the session's `kb_root_id`, `user_id`, and `visibility_level`. This is where document 1's access control (section 5.5) meets the GPU — the hardware enforces session credentials, not a software guard. KB queries on a session-bound stream only see KBs reachable from that session's scope. This implements the "absent not filtered" property from document 16 (VDR-16).

`StreamWaitEvent` enables the concurrent stream model from document 14 (VDR-18, section 10): five streams (LLM forward, KB query, VDR primitives, grammar mask, provenance compact) can overlap because events express dependencies between them. The integration spec's `vlp_cycle` (document 3 section 1) dispatches work across these streams.

`EventElapsedTime` is noted as the one place a float exists — host-side timing. The implementation note suggests integer nanoseconds instead. This is the level of float-avoidance the system maintains.

### Module 4: TensorProlog_session — The operational model

This module implements the session lifecycle from document 1 section 5.1, the disposable clone pattern from document 20 (VDR-8), and the drift management from document 8 (VDR-24).

`SessionCreate` takes a `SessionConfig` with `kb_root_id`, `user_id`, `visibility_level`, `max_kb_count`, `max_live_memory_bytes`, `max_turns`. These map directly to the `vlp_session` struct from document 5 (`src/session/types.zig`). The session is the unit of isolation — everything in document 16 (VDR-16) about structural safety rests on session boundaries.

`SessionSnapshot` produces the "deployable binary" from document 8 (VDR-24). The snapshot captures all persistent KBs, all live state (the 7 data primitives from Module 10), the rule base, and the grammar cache. The checksum is integer CRC — deterministic. `SessionRestore` overwrites all state from the snapshot with checksum validation. "Bit-identical" means bit-identical because integers.

`SessionClone` implements COW from document 1 section 6.2. The child shares parent's persistent KBs read-through, gets independent live state (configurable: copy parent's current or start fresh). Writes to persistent KBs are copy-on-write — parent doesn't see them until `SessionMerge`. This is the clone-per-connection pattern from document 7 (VDR-25) and the clone-per-task pattern from document 3 section 2.5.

`SessionMerge` with its three policies (OURS/THEIRS/FAIL_ON_CONFLICT) implements the merge mechanism from document 1 section 5.1. `SessionKill` is the drift-kill — no snapshot, live state gone, COW pages discarded. This is the kill side of the "build → snapshot → clone → monitor drift → kill → reclone" cycle from document 8.

`SnapshotSave`/`SnapshotLoad` to filesystem make snapshots portable across devices. The format is header + raw integers — no float serialization. This is why document 25 (VDR-4) claims bit-identical checkpoints across platforms.

### Module 5: TensorProlog_launch — Kernel dispatch

Four launch variants with scheduling hints: `LaunchKernel` (generic), `LaunchMACKernel` (maximum integer ALUs for matrix multiply), `LaunchPrologKernel` (maximum shared memory for KB cache), `LaunchPrimKernel` (minimum resources, fastest dispatch). These hints map to the GPU stream model from document 14 (VDR-18 section 10) where different workloads have different resource profiles.

`OccupancyMaxPotentialBlockSize` is simpler than CUDA's equivalent because no warp divergence means occupancy is almost always near-maximum. The primary constraint is shared memory for KB cache (document 1 section 4.3: 67 KB of 228 KB used), not warp scheduling.

### Module 6: TensorProlog_vdr_math — The arithmetic engine

This replaces cuBLAS (~200+ functions) with 17 functions. Every function takes `qbasis` as the first parameter — the type tag that flows through the entire system.

`VdrGemm` is the workhorse. C = alpha×op(A)×op(B) + beta×C with exact integer multiply-accumulate. No accumulation error regardless of matrix size. This is what document 2 section 1.2 calls for each transformer layer: QKV projection, output projection, MLP up/down projections — all GEMMs. The batched and strided-batched variants handle multi-head attention (batch_count = n_heads).

`VdrSoftmax` implements the quadratic surrogate from document 24 (VDR-1) and document 25 (VDR-4): shift inputs so min=0, square each, divide by sum. Output sum = D exactly. Every call. This is invariant 1 from document 1 section 16.2. `VdrExpSoftmax` is the FRU-based exact exponential softmax from document 9 (VDR-23) — returns `ERR_FRU_NOT_AVAILABLE` on Phase 1 hardware, which is when you fall back to the surrogate.

`VdrLayerNorm` takes an `eps_unused` parameter — placeholder for API compatibility, always ignored because integer variance is never zero unless all inputs identical, which is detectable exactly. This implements the "rational scaling" adaptation from document 21 (VDR-7 section VA2).

`VdrCompare` does elementwise cross-multiply comparison producing -1/0/+1. This is the exact comparison from document 11 (VDR-21, CROSS_MUL instruction) — no tolerance, no epsilon. Equal means equal. This is what Prolog unification (Module 11) uses for VDR value comparison.

`VdrReproject` changes Q-basis — the only operation that changes D. This is the denominator management from document 21 (VDR-7 section DM2): when denominators exceed budget, reproject with exact error tracking.

`VdrNormalize` compacts remainders in-place. Idempotent. This maintains the normalization rules from document 24 (VDR-1 section N1-N7).

`VdrRemainderMagnitude` is the precision budget dashboard from document 2 section 1.14 — monitors whether Q-basis is sufficient.

### Module 7: TensorProlog_attention — The LLM hot path

Three functions replacing cuDNN's ~50+ attention functions. `AttentionForward` is fused: QKᵀ → scale → causal mask → softmax → AV in one kernel. The config includes `softmax_type` (QUADRATIC or EXP_FRU) — this is the choice between document 9's surrogate and exact exp softmax. Causal mask is exact zero via integer comparison (col > row), not approximate masking.

`AttentionBackward` produces exact gradients. No gradient clipping needed because integer gradients don't explode from accumulation — they can only grow from actual signal, not arithmetic noise. This eliminates the entire gradient clipping infrastructure from conventional training.

`AttentionVerifySoftmaxSum` is the runtime invariant check. Counts rows where sum ≠ D. Expected: always 0. If nonzero, something is broken — this is a hard failure, not drift. The check is free in production because it's integer equality. This function directly verifies invariant 1 from document 1 section 16.2.

### Module 8: TensorProlog_training — Exact training

`TrainSGDUpdate` is `params -= lr × grads`. Exact. The learning rate is a VDR scalar (e.g., 1/1000 at Q16 is V=65, D=65536). `TrainAdamUpdate` does full Adam in exact integer arithmetic — no epsilon in the denominator because if the second moment is zero, the gradient was zero and the update is zero, detectable exactly.

`TrainComputeLoss` uses `fn_log` (Module 21) for cross-entropy when FRU is available, rational approximation otherwise. The loss is a single VDR scalar. Monotonic decrease is observable as integer comparison between epochs — document 25 (VDR-4) confirms this works on toy data.

`TrainBackwardPass` traces the recorded compute graph (from `TrainComputeGraphRecord`) and produces exact partial derivatives via chain rule. No loss scaling needed. No NaN detection. No "training diverged, try lower learning rate." If training diverges, the cause is the learning rate or the data, not arithmetic instability.

`TrainCheckpointSave`/`Load` write raw integers. Bit-identical across saves, loads, platforms. Resume on a different machine produces an identical training trajectory — this is the property document 2 section 1.3 demonstrates.

### Module 9: TensorProlog_kb — The data layer

This module implements the KB store engine from document 1 section 6.2 and the KB struct from document 1 section 3.1.

`KBCreate` takes a config with name, parent_id, visibility, owner, max_facts, max_rules, max_children. Returns a sequential integer kb_id. This maps to `KBStore.createKB` from document 5 (`src/kb/store.zig`). The fixed-size KB struct (256 bytes) means allocation is O(1) bump-pointer.

`KBResolvePath` converts dotted path strings to integer kb_ids via hash map — the one-time cost from document 20 (VDR-8). All subsequent operations use the integer directly. This is the `PathIndex.lookup` from document 5.

`KBFactAssert` writes a fact at kb_id + slot_id. The fact struct has tag (from the `VlpFactTag` enum), value (Q16/Q32/Q335), and provenance (source_kb_id, source_slot_id, confidence as VDR, timestamp). The checks — session visibility, frozen flag, slot bounds — are all integer comparisons. This implements the "every access check is integer comparison" property from document 16 (VDR-16).

`KBFactQuery` reads a fact at kb_id + slot_id. O(1) via two integer indices. The visibility check walks the parent chain — if any ancestor fails the visibility check, the function returns `ERR_KB_ACCESS_DENIED`. The fact is never exposed — absent, not redacted. This is invariant 6 from document 1 section 16.2.

`KBFactScopedSearch` walks from start_kb_id up the parent chain to root, returning first matches. This is lexical scoping from document 23 (VDR-5) — "bank" resolves differently depending on which KB you start from.

`KBMount`/`KBUnmount` implement cross-branch references from document 20 (VDR-8). Makes a KB accessible as if it were a child of another KB without changing the tree structure.

### Module 10: TensorProlog_kb_primitives — Working memory

30 functions implementing the 7 bounded data primitives from document 20 (VDR-8): LRU cache, counter, lock, queue, stack, ring buffer, bitset. These are the live state fields on the KB struct (fields KB09-KB15 from document 20).

Every primitive is bounded at creation. LRU capacity 1-1000, queue/stack 1-1000, bitset 1-10000. Counter clamps at min/max, never wraps. Queue push returns false when full. These bounds enforce invariant 3 from document 1 section 16.2.

These primitives implement the coordination patterns from document 8 (VDR-24): counters for drift detection and rate limiting, queues for task distribution (waterfall/fan-out topologies), locks for batch coordination, ring buffers for rolling metrics, bitsets for progress tracking.

The primitives live inside the KB struct, which means `SessionSnapshot` captures them, `SessionRestore` restores them, `SessionClone` copies or initializes them. This is the "data primitives create state worth snapshotting" dependency from document 20 (VDR-8 principle P4).

### Module 11: TensorProlog_prolog — Logic on GPU

8 functions implementing the Prolog engine from document 1 section 6.3.

`PrologRuleAssert` adds a rule with head, body conditions, and actions (assert/retract). Terms are typed: atom (i32 tag), variable (i32 binding slot), vdr_value, list, compound. All integer representations. Rules are persistent — survive reset, participate in snapshots. This implements `RuleStore.assertRule` from document 5.

`PrologQuery` runs depth-first search with backtracking, depth limit 100, scoped from start_kb_id walking ancestors. Unification uses cross-multiply comparison on VDR values — invariant 9 from document 1. The parallelization model: candidate facts loaded into shared memory, cross-multiply comparisons distributed across warps. This is the frontier-based Prolog from document 14 (VDR-18 section 7).

`PrologFireAll` evaluates all rules against current facts, returns fired list with bindings and proposed actions, does NOT commit. `PrologFireAndCommit` does both. This is the L3 execution path from document 1 section 8.3 — zero LLM tokens, pure Prolog over integers. The runtime engine's Phase 0 (document 3 section 1) calls `PrologFireAll` before the LLM ever sees anything.

`PrologHygiene` identifies stale (>N days unfired), failing (<20% success), or orphaned (reference retracted facts) rules. Returns candidate rule_ids for review. This implements the hygiene rules from document 1 section 11.2 and document 13 (VDR-19 concepts C8, HY1-HY3).

### Module 12: TensorProlog_grammar — Structural tokens

7 functions implementing the grammar engine from document 1 section 6.4 and document 19 (VDR-12).

`GrammarCreate` parses a template with typed slot markers (`{name:type}`). Types: vdr_value, text, integer, enum. Validation ensures the template is syntactically valid with any valid slot fill. If `GrammarValidate` returns valid=true, every possible rendering is structurally correct by construction. This is the "grammar cannot produce malformed output" property from document 7 (VDR-25 principle P1).

`GrammarRender` fills slots with provided values. Every structural byte comes from the template. LLM contribution: the fill values. Grammar contribution: everything else. This is the token elimination from document 17 (VDR-15): Python ~40%, JSON ~55%, tables ~65% of tokens are structural and come from the grammar at zero LLM cost.

`GrammarRenderFromKB` fills slots directly from KB facts via slot→(kb_id, slot_id) mappings. Data flows from KB to output without entering any token stream. This is the "data never enters token stream" property from document 13 (VDR-19 principle P5).

`GrammarStoreInKB`/`GrammarLoadFromKB` make grammars persistent KB fields that inherit through the tree. `GrammarCompose` nests grammars for complex output from simple templates.

### Module 13: TensorProlog_runner — Autonomous operation

8 functions implementing the four runner types from document 1 section 5.2 and document 12 (VDR-20).

`RunnerCreatePoller` spawns a host thread calling `poll_fn` every `interval_ms`. Fresh LLM context each cycle. This is the poller from document 3 section 2.2 — fires rules, checks queues, routes work.

`RunnerCreateProcessor` maintains a persistent external connection. `max_turns_before_recycle` (default 200) triggers the recycle dance: snapshot connection state → snapshot session → kill → reclone → restore connection. This is the processor from document 3 section 2.3 — continuous data, always-fresh LLM.

`RunnerCreateInternal` runs scheduled computation. Derives facts from existing facts — rolling averages as exact fractions, trend detection via exact integer comparison. This is the internal runner from document 3 section 2.4.

`RunnerCreateBatch` pulls tasks from a KB queue, processes each with a fresh session clone. Clone-per-task isolation. This is the batch runner from document 3 section 2.5.

`RunnerRecycle` is the manual version of the processor's automatic recycle: snapshot → kill → reclone. Drift dies, knowledge persists.

### Module 14: TensorProlog_safety — Structural access control

6 functions implementing the three-layer safety model from document 16 (VDR-16).

`SafetyCheckAccess` is the core gate. Walks from kb_id up the parent chain, checking visibility at each ancestor via integer comparison. If any ancestor fails, access=false. This runs BEFORE any data is read — it's a gate, not a filter. This implements layer L1 from document 16.

`SafetyGrantCreate`/`SafetyGrantCheck`/`SafetyGrantRevoke` implement layer L2. Grants have class (FILESYSTEM, COMPILE, EXECUTE, LINT, NETWORK, PROCESS), target pattern, max uses, expiry. The check is four integer comparisons: not expired AND uses remaining AND not revoked AND target matches. `SafetyGrantCheck` decrements uses_remaining on success — monotonic state transition from document 22 (VDR-6 section GR5).

`SafetyAuditLog`/`SafetyAuditQuery` implement the append-only audit trail — invariant 10 from document 1. Every access check, every grant check, every fact assertion writes an audit entry. The audit KB is a ring buffer of integer entries.

### Module 15: TensorProlog_confidence — Exact provenance

5 functions implementing the confidence propagation from document 1 section 9 and document 18 (VDR-14 Appendix G).

`ConfidenceFromSource` returns the declared confidence for each source type from the knowability spectrum: VDR computation = 1/1, Prolog derivation = 1/1, database = 98/100, Prometheus = 95/100, ... LLM-generated = 30/100, unknown = 0/1. These are the 11 values in `CONFIDENCE_TABLE` from document 5 (`src/confidence/types.zig`).

`ConfidenceCombineAgreeing` computes `1 - ∏(1 - Cᵢ)` — exact VDR arithmetic. Two sources at 85/100 gives 9775/10000, not 0.9775. `ConfidenceChain` computes C^N — three links at 85/100 gives 614125/1000000. `ConfidencePropagate` walks the full derivation tree applying combine/chain rules. This replaces hedging language ("approximately," "it appears that") with exact fractions.

### Module 16: TensorProlog_distributed — Deterministic multi-GPU

10 functions replacing NCCL (~100+ functions). The key property: `DistAllReduce` with SUM is associative and commutative for integers regardless of reduction order. Ring reduce, tree reduce, butterfly reduce — all produce bit-identical results. This single property eliminates non-deterministic distributed training (document 2 section 1.5).

`DistKBSync` synchronizes KB facts across ranks via deterministic merge. `DistSnapshotBroadcast` sends a session snapshot to all ranks so all start from bit-identical state.

### Module 17: TensorProlog_transform — Exact signal processing

4 functions. DFT/IDFT with exact twiddle factors (rational approximations of roots of unity). Roundtrip DFT → IDFT returns original values exactly. Conv1D/Conv2D via exact integer MAC. These are used for image processing and audio processing layers in the diffusion workflows from document 2 section 2.

### Module 18: TensorProlog_linalg — Exact linear algebra

8 functions replacing cuSOLVER (~200+ functions). `GaussianElim` solves Ax=b with exact VDR division — no pivoting for numerical stability because there's no numerical instability. Pivot only for zero-avoidance. `Inverse` works where float64 fails (Hilbert matrix from document 24 VDR-1 section LA7). `GramSchmidt` produces exact orthogonalization with no drift in the basis.

### Module 19: TensorProlog_stats — Exact statistics

8 functions. `Bayes` does exact posterior update: posterior sums to exactly 1/1. `Normalize` divides each element by sum so elements sum to D exactly — same guarantee as softmax. `Correlation` produces exact Pearson as a VDR fraction. These feed the confidence propagation system (Module 15).

### Module 20: TensorProlog_numbertheory — Crypto primitives

7 functions. `ModPow` for modular exponentiation. `CRT` for Chinese Remainder Theorem. `IsPrime` deterministic for bounded inputs. These support the dual-purpose VDR+ZKP capability from document 10 (VDR-22 section C7) where adding Barrett reduction enables zero-knowledge proof field arithmetic alongside VDR.

### Module 21: TensorProlog_functional_remainder — FRU operations

8 functions implementing the FRU from document 9 (VDR-23). `FRUSqrt`, `FRUExp`, `FRULog`, `FRUSin`, `FRUCos`, `FRUAtan2` — each takes a depth parameter controlling iteration count. `FRUResolve` does batch remainder resolution for continuous training. `FRUAvailable` reports whether the current device has FRU hardware — callers fall back to software recurrence on host CPU when unavailable.

These functions are what make exact exponential softmax (Module 6 `VdrExpSoftmax`) and exact cross-entropy loss (Module 8 `TrainComputeLoss`) work. Without FRU, the system uses the quadratic surrogate softmax and rational approximation losses — still exact sum-to-one, just with different ranking properties.

### Module 22: TensorProlog_builtins — The 448 primitives

This is the largest module. It exposes all 448 builtins from document 26 (VDR-10) and document 22 (VDR-6) as host-callable functions that dispatch to device kernels. Organized by the categories from the paper: text (17), collections (36), sets (14), mappings (15), conversion (14), graph (13), integer/bit ops (21), plus the remaining categories.

Each builtin has a specific function signature. `BuiltinParseJson` is a compiled state machine that writes to KB facts at integer addresses — zero LLM tokens, cannot fail on valid JSON. `BuiltinSort` uses exact integer comparison — no tolerance ambiguity at sort boundaries. `BuiltinGraphShortestPath` runs Dijkstra with exact VDR weights — no floating point distance accumulation.

The conversion builtins (`ParseJson`, `ParseCsv`, `ToJson`, `ToCsv`) are the data ingestion pipeline from document 12 (VDR-20): external data enters through these primitives, gets stored as KB facts, and is processed without ever entering the token stream.

The `PageRankExact` and `MarkovSteady` functions produce exact steady-state distributions as VDR fractions — these are the graph math builtins from document 25 (VDR-25 graph.zig).

### Module 23: TensorProlog_profiling — Simplified diagnostics

4 functions. `ProfileGetKernelStats` returns integer metrics only — no float utilization, no SFU utilization, no tensor-core breakdown. One compute type (integer), so profiling is simpler. `warp_occupancy_percent` is always near 100 because no divergence.

`ProfileVerifyDeterminism` runs a kernel N times and bit-compares all outputs. Expected: always identical. If false, hardware fault. This test is meaningful only because integer arithmetic is deterministic — on float CUDA this test would always fail due to thread scheduling affecting reduction order. This implements the determinism verification from document 1 section 14.1.

`ProfileGetSessionStats` reports exact operational metrics including `auto_triage_percentage` as an exact VDR fraction — this is the L3 percentage from document 1 section 8.4.

## How the data flows through these modules

The universal cycle from document 3 maps to these modules as follows:

**Phase 0** (pre-LLM rule evaluation): Module 11 `PrologFireAll` → Module 11 `PrologFireAndCommit`. If auto-resolved, Module 12 `GrammarRenderFromKB` produces output directly. Zero tokens. Modules 9 and 10 provide KB data and primitive state.

**Phase 1** (context assembly): Module 9 `KBFactQuery` reads system prompt, scope reference, scratchpad contents. Module 10 counter/ring reads for state summaries.

**Phase 2** (LLM generation + command dispatch): Module 6 `VdrGemm`/`VdrSoftmax` for forward pass. Module 7 `AttentionForward` for attention. For each generated command token: Module 14 `SafetyCheckAccess` (access gate), Module 14 `SafetyGrantCheck` (grant gate), then dispatch to Module 9 (KB ops), Module 11 (Prolog), Module 22 (builtins), or Module 12 (grammar render).

**Phase 3** (post-cycle): Module 4 `SessionSnapshot` if auto-snapshot interval hit. Module 10 counter increments for session stats.

**Training**: Module 8 `TrainComputeGraphRecord` during forward, `TrainBackwardPass` for gradients, `TrainSGDUpdate`/`TrainAdamUpdate` for parameter update, `TrainCheckpointSave` for persistence.

**Runner operation**: Module 13 `RunnerCreatePoller`/`Processor`/`Internal`/`Batch` set up the loop. Each iteration calls the cycle. Module 4 `SessionClone`/`SessionKill` for the recycle dance. Module 4 `SessionSnapshot` for persistence.

**Server operation**: Module 4 `SessionClone` from template snapshot per connection. Module 14 `SafetyCheckAccess` + `SafetyGrantCheck` per request. Module 12 `GrammarRender` for protocol response formatting. Module 4 `SessionKill` on disconnect.

## What's structurally eliminated

The summary table at the end of document 27 shows what these 580 functions replace: ~3,400+ CUDA API functions for float precision variants, mixed-precision management, NaN handling, loss scaling, Transformer Engine, TensorRT calibration. Gone because those failure categories don't exist in integer arithmetic.

What's new (~90 functions across modules 4, 9, 10, 11, 12, 13, 14, 15): session lifecycle, KB operations, bounded data primitives, Prolog engine, grammar engine, runner management, structural safety, exact confidence. These enable the capabilities the papers describe — autonomous operation, persistent state, structural safety, exact provenance — none of which exist in any form in CUDA.
