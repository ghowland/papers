# ICUDA Module & Function Specification

## Complete Implementation Reference

---

## Module 1: icuda_core

Runtime lifecycle, device management, error handling.

```
icudaInit(flags: u32) -> icudaStatus_t
  First call. Initializes driver, enumerates devices, allocates host-side
  session table. No device memory touched yet. Idempotent — second call
  returns OK without work. Sets global init flag checked by all other calls.

icudaDeviceGetCount(count: *i32) -> icudaStatus_t
  Writes number of ICUDA-capable devices. Filters to integer-native only
  if Phase 2+ hardware present, falls back to INT8-capable for Phase 1.

icudaDeviceGet(device: *icudaDevice_t, ordinal: i32) -> icudaStatus_t
  Returns device handle by index. Validates ordinal against count.

icudaDeviceGetProperties(props: *icudaDeviceProps_t, device: icudaDevice_t) -> icudaStatus_t
  Populates: n_compute_units, max_q_basis (Q16/Q32/Q335), has_fru (bool),
  kb_cache_size_bytes, max_shared_mem_per_block, max_registers_per_block,
  max_concurrent_sessions, global_mem_bytes, mem_bandwidth_bytes_sec,
  clock_rate_hz, warp_size (always 32). No float fields.

icudaDeviceSetCurrent(device: icudaDevice_t) -> icudaStatus_t
  Binds calling host thread to device. All subsequent calls target this device.

icudaDeviceGetCurrent(device: *icudaDevice_t) -> icudaStatus_t
  Returns currently bound device for calling thread.

icudaDeviceSynchronize() -> icudaStatus_t
  Blocks until all kernels on all streams of current device complete.

icudaDeviceReset() -> icudaStatus_t
  Destroys all allocations, streams, sessions on current device. Returns
  device to post-init state. Active sessions are force-snapshotted first.

icudaGetErrorString(status: icudaStatus_t) -> *const u8
  Returns static string for error code. No allocation.

icudaGetLastError() -> icudaStatus_t
  Returns and clears last error on calling thread. Thread-local storage.

icudaPeekLastError() -> icudaStatus_t
  Returns last error without clearing.
```

### Error codes (icudaStatus_t enum):

```
OK, ERR_NOT_INITIALIZED, ERR_INVALID_DEVICE, ERR_OUT_OF_MEMORY,
ERR_INVALID_QBASIS, ERR_QBASIS_MISMATCH, ERR_KB_NOT_FOUND,
ERR_KB_ACCESS_DENIED, ERR_KB_FULL, ERR_SLOT_OUT_OF_RANGE,
ERR_GRANT_DENIED, ERR_SESSION_LIMIT, ERR_STREAM_BUSY,
ERR_INVALID_KERNEL, ERR_LAUNCH_FAILURE, ERR_PROLOG_DEPTH_EXCEEDED,
ERR_REMAINDER_OVERFLOW, ERR_FRU_NOT_AVAILABLE, ERR_GRAMMAR_INVALID,
ERR_PRIMITIVE_BOUNDS, ERR_SNAPSHOT_FAILED, ERR_CLONE_FAILED,
ERR_DETERMINISM_VIOLATION
```

No NaN, no Inf, no loss-scale, no precision-mismatch errors. Those categories don't exist.

---

## Module 2: icuda_memory

Device memory allocation, host-device transfer. All allocations are typed.

```
icudaMalloc(ptr: **void, size_bytes: u64) -> icudaStatus_t
  Allocates device global memory. Untyped — caller casts. For raw buffers
  and scratch space. Aligned to 256 bytes.

icudaMallocTyped(ptr: **void, qbasis: icudaQBasis_t, count: u64) -> icudaStatus_t
  Allocates array of count VDR elements at declared qbasis. Compiler tracks
  qbasis tag on the pointer. Passing to mismatched-qbasis kernel = compile error.
  Element size derived from qbasis: Q16=8, Q32=16, Q335=240 bytes.

icudaMallocKB(ptr: **icudaKBStruct_t, count: u32) -> icudaStatus_t
  Allocates contiguous array of KB structs. Fixed size per struct (paper's
  26-field layout). Count is max KBs this allocation holds. Zeroed on alloc.

icudaFree(ptr: *void) -> icudaStatus_t
  Frees device allocation. All three Malloc variants free through this.

icudaMemcpy(dst: *void, src: *const void, size_bytes: u64, kind: icudaMemcpyKind_t) -> icudaStatus_t
  Synchronous copy. Kind: HostToDevice, DeviceToHost, DeviceToDevice.
  Bit-exact — integer data is identical after copy on every platform.

icudaMemcpyAsync(dst: *void, src: *const void, size_bytes: u64, kind: icudaMemcpyKind_t, stream: icudaStream_t) -> icudaStatus_t
  Asynchronous copy on stream. Completion visible after stream sync.

icudaMemset(ptr: *void, value: i32, size_bytes: u64) -> icudaStatus_t
  Sets bytes. Primarily for zeroing buffers.

icudaMemGetInfo(free: *u64, total: *u64) -> icudaStatus_t
  Reports device memory. Counts only — no fragmentation metrics needed
  because KB structs are fixed-size so fragmentation is minimal.

icudaMallocHost(ptr: **void, size_bytes: u64) -> icudaStatus_t
  Page-locked host memory for async transfer overlap.

icudaFreeHost(ptr: *void) -> icudaStatus_t
  Frees page-locked host allocation.

icudaMemPrefetchAsync(ptr: *void, size_bytes: u64, device: icudaDevice_t, stream: icudaStream_t) -> icudaStatus_t
  Hints unified memory migration. Used for KB preloading — prefetch
  KB subtree to device before kernel launch.
```

---

## Module 3: icuda_stream

Execution streams and synchronization. Streams are session-aware.

```
icudaStreamCreate(stream: *icudaStream_t) -> icudaStatus_t
  Creates default stream. No session binding — for non-session work
  (memory ops, diagnostics). Kernels on unbound streams cannot access KBs.

icudaStreamCreateWithSession(stream: *icudaStream_t, session: icudaSession_t) -> icudaStatus_t
  Creates stream bound to session. All kernels inherit session's kb_root_id,
  user_id, visibility_level. The hardware enforces access — not a software guard.
  KB queries on this stream only see KBs reachable from session scope.

icudaStreamDestroy(stream: icudaStream_t) -> icudaStatus_t
  Waits for pending work, then destroys. Does not destroy session.

icudaStreamSynchronize(stream: icudaStream_t) -> icudaStatus_t
  Blocks until all kernels on this stream complete.

icudaStreamQuery(stream: icudaStream_t) -> icudaStatus_t
  Non-blocking check. Returns OK if complete, ERR_STREAM_BUSY if not.

icudaStreamWaitEvent(stream: icudaStream_t, event: icudaEvent_t) -> icudaStatus_t
  Stream waits for event before executing subsequent kernels.
  Used for cross-stream dependencies (e.g., Prolog query depends on
  MAC kernel completing attention computation).

icudaEventCreate(event: *icudaEvent_t) -> icudaStatus_t
  Creates event for timing and synchronization.

icudaEventRecord(event: icudaEvent_t, stream: icudaStream_t) -> icudaStatus_t
  Records event at current point in stream.

icudaEventSynchronize(event: icudaEvent_t) -> icudaStatus_t
  Blocks until event completes.

icudaEventElapsedTime(ms: *f32, start: icudaEvent_t, end: icudaEvent_t) -> icudaStatus_t
  NOTE: the one place a float exists — host-side timing measurement.
  Could be integer nanoseconds instead. Implementation choice.

icudaEventDestroy(event: icudaEvent_t) -> icudaStatus_t
  Frees event.
```

---

## Module 4: icuda_session

Session lifecycle, snapshots, clones. The operational model from paper Section 4.6.

```
icudaSessionCreate(session: *icudaSession_t, config: *icudaSessionConfig_t) -> icudaStatus_t
  Config contains: kb_root_id (root of this session's KB tree), user_id (i32),
  visibility_level (enum: public/internal/owner_only), max_kb_count (u32),
  max_live_memory_bytes (u64), max_turns (u32, 0=unlimited).
  Allocates session state on device. Initializes all bounded data primitives
  to empty/min. Session is the unit of isolation.

icudaSessionDestroy(session: icudaSession_t) -> icudaStatus_t
  Snapshots if auto_snapshot enabled, then frees all session device memory.
  Persistent KB facts survive in the global KB store. Live state is gone.

icudaSessionGetInfo(session: icudaSession_t, info: *icudaSessionInfo_t) -> icudaStatus_t
  Reports: current_turn, kb_count, live_memory_bytes, n_rules_fired,
  n_facts_asserted, n_prolog_queries. All i32/i64. No approximate values.

icudaSessionSnapshot(session: icudaSession_t, snapshot: *icudaSnapshot_t) -> icudaStatus_t
  Atomic capture of all session state: persistent KBs, live state (LRUs,
  counters, queues, stacks, ring buffers, bitsets), rule base, grammar cache.
  Snapshot is a device memory blob with a host-readable header (size, checksum,
  session config). Checksum is integer CRC — deterministic.
  The snapshot IS the factory. Bit-identical restore guaranteed.

icudaSessionRestore(session: icudaSession_t, snapshot: *icudaSnapshot_t) -> icudaStatus_t
  Overwrites all session state from snapshot. Validates checksum first.
  After restore, session is in exactly the state at snapshot time.
  "Exactly" means bit-identical because integers.

icudaSessionClone(parent: icudaSession_t, child: *icudaSession_t, config: *icudaCloneConfig_t) -> icudaStatus_t
  Creates new session sharing parent's persistent KBs (read-through)
  with independent live state (initialized from parent's current live state,
  or from empty if config says fresh_live=true). Clone's writes to persistent
  KBs are copy-on-write — parent doesn't see them until explicit merge.
  Clone config: fresh_live (bool), inherit_rules (bool), max_turns (u32).

icudaSessionMerge(parent: icudaSession_t, child: icudaSession_t, policy: icudaMergePolicy_t) -> icudaStatus_t
  Merges child's persistent KB changes back to parent. Policy: OURS (parent
  wins conflicts), THEIRS (child wins), FAIL_ON_CONFLICT. Conflict = same
  kb_id + slot_id modified by both. After merge, child can be destroyed.

icudaSessionKill(session: icudaSession_t) -> icudaStatus_t
  Immediate termination. No snapshot. Live state gone. Persistent KBs
  that were copy-on-write are discarded. This is the drift-kill from the paper:
  clone drifted, kill it, reclone from snapshot.

icudaSnapshotSave(snapshot: *icudaSnapshot_t, path: *const u8) -> icudaStatus_t
  Writes snapshot to host filesystem. The "deployable binary."
  Format: header + raw integer data. No float serialization.
  Portable across devices — integers are platform-independent.

icudaSnapshotLoad(snapshot: *icudaSnapshot_t, path: *const u8) -> icudaStatus_t
  Reads snapshot from host filesystem. Validates header and checksum.
  Bit-identical to what was saved. Always, on every platform.
```

---

## Module 5: icuda_launch

Kernel launch configuration and execution.

```
icudaLaunchKernel(kernel: *const void, grid: icudaDim3_t, block: icudaDim3_t, args: **void, shared_mem: u64, stream: icudaStream_t) -> icudaStatus_t
  Standard kernel launch. Grid/block dimensions as dim3 (x,y,z integer).
  Shared_mem is additional shared memory beyond static declarations.
  If stream is session-bound, kernel inherits session credentials.

icudaLaunchMACKernel(kernel: *const void, grid: icudaDim3_t, block: icudaDim3_t, args: **void, stream: icudaStream_t) -> icudaStatus_t
  Hint to scheduler: this kernel is pure MAC. Scheduler allocates maximum
  integer ALUs, maximum memory bandwidth, minimum shared memory.
  No functional difference from LaunchKernel — just scheduling priority.

icudaLaunchPrologKernel(kernel: *const void, grid: icudaDim3_t, block: icudaDim3_t, args: **void, stream: icudaStream_t) -> icudaStatus_t
  Hint to scheduler: this kernel does KB-heavy work. Scheduler allocates
  maximum shared memory for KB cache, moderate ALU, moderate bandwidth.

icudaLaunchPrimKernel(kernel: *const void, grid: icudaDim3_t, block: icudaDim3_t, args: **void, stream: icudaStream_t) -> icudaStatus_t
  Hint to scheduler: lightweight primitive. Minimum resource allocation,
  fastest dispatch latency.

icudaOccupancyMaxPotentialBlockSize(min_grid: *i32, block_size: *i32, kernel: *const void, shared_mem_per_block: u64, max_block_size: i32) -> icudaStatus_t
  Calculates optimal launch config. Simpler than CUDA equivalent because
  no divergence means occupancy is almost always near-maximum.
  The primary constraint is shared memory for KB cache, not warp scheduling.
```

---

## Module 6: icuda_vdr_math

Core VDR arithmetic operations on device arrays. Replaces cuBLAS, cuDNN math.

```
icudaVdrGemm(qbasis: icudaQBasis_t, transa: icudaOp_t, transb: icudaOp_t, m: i32, n: i32, k: i32, alpha: *const void, A: *const void, lda: i32, B: *const void, ldb: i32, beta: *const void, C: *void, ldc: i32, stream: icudaStream_t) -> icudaStatus_t
  General matrix multiply: C = alpha*op(A)*op(B) + beta*C.
  Alpha, beta are VDR scalars at declared qbasis. All elements same qbasis.
  Dispatches to integer MMA tiles internally. Result is exact — no
  accumulation error regardless of matrix size.
  Op: NO_TRANS, TRANS. No conjugate-transpose (no complex floats).

icudaVdrGemmBatched(qbasis: icudaQBasis_t, transa: icudaOp_t, transb: icudaOp_t, m: i32, n: i32, k: i32, alpha: *const void, A_array: **const void, lda: i32, B_array: **const void, ldb: i32, beta: *const void, C_array: **void, ldc: i32, batch_count: i32, stream: icudaStream_t) -> icudaStatus_t
  Batched GEMM for multi-head attention. batch_count = n_heads.
  Each batch is independent — trivially parallel across SMs.

icudaVdrGemmStridedBatched(qbasis: icudaQBasis_t, transa: icudaOp_t, transb: icudaOp_t, m: i32, n: i32, k: i32, alpha: *const void, A: *const void, lda: i32, stride_a: i64, B: *const void, ldb: i32, stride_b: i64, beta: *const void, C: *void, ldc: i32, stride_c: i64, batch_count: i32, stream: icudaStream_t) -> icudaStatus_t
  Strided variant — contiguous memory, stride between batches.
  Preferred for attention where Q,K,V are packed sequentially per head.

icudaVdrSoftmax(qbasis: icudaQBasis_t, input: *const void, output: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Quadratic surrogate: shift inputs so min=0, square each, divide by sum.
  Output sum = D exactly. Every call. Guaranteed by construction.
  No exp, no SFU, no data-dependent divergence.

icudaVdrExpSoftmax(qbasis: icudaQBasis_t, input: *const void, output: *void, n: i32, depth: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact exp-softmax via FRU recurrence. Depth bounds the iteration count.
  Returns ERR_FRU_NOT_AVAILABLE on Phase 1 hardware.
  Output sum = D exactly at sufficient depth. Depth insufficient = remainder
  in last R slot tells you how far off.

icudaVdrLayerNorm(qbasis: icudaQBasis_t, input: *const void, output: *void, gamma: *const void, beta: *const void, n: i32, eps_unused: i32, stream: icudaStream_t) -> icudaStatus_t
  Integer layer normalization. Mean and variance computed exactly.
  eps_unused is placeholder for API compat — always ignored because
  integer variance is never zero unless all inputs identical, which is
  detectable by exact comparison, not epsilon.

icudaVdrAdd(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Elementwise add. Same D — straight integer add on V, handle R carry.

icudaVdrSub(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Elementwise subtract.

icudaVdrMul(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Elementwise multiply. Widening mul, shift, remainder extraction.

icudaVdrDiv(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Elementwise divide. a * reciprocal(b). Reciprocal is D²/b_v with
  remainder tracking. Active division caveat from paper Section 15 applies
  if b has nonzero remainder — scalar projection, logged.

icudaVdrDot(qbasis: icudaQBasis_t, a: *const void, b: *const void, result: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Dot product. Widening MAC across n elements. Single VDR scalar result.

icudaVdrScale(qbasis: icudaQBasis_t, input: *const void, scalar: *const void, output: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Multiply every element by scalar. Used for learning rate application.

icudaVdrCompare(qbasis: icudaQBasis_t, a: *const void, b: *const void, result: *i32, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Elementwise cross-multiply comparison. Result array: -1, 0, +1.
  Exact — no tolerance, no epsilon. Equal means equal.

icudaVdrReproject(src_qbasis: icudaQBasis_t, dst_qbasis: icudaQBasis_t, input: *const void, output: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Change Q-basis. Exact when dst_D is multiple of src_D. Remainder-tracked
  otherwise. This is the only operation that changes D.

icudaVdrNormalize(qbasis: icudaQBasis_t, data: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Compact remainders: if R0 >= D, roll into V. Reduces remainder depth.
  In-place. Idempotent — calling twice gives same result as once.

icudaVdrRemainderMagnitude(qbasis: icudaQBasis_t, data: *const void, magnitudes: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Reports magnitude of remainder per element. For monitoring precision
  budget. If all magnitudes are zero, computation was exact at depth 0.
```

---

## Module 7: icuda_attention

Fused attention kernels. The hot path for LLM inference and training.

```
icudaAttentionForward(config: *icudaAttentionConfig_t, Q: *const void, K: *const void, V: *const void, output: *void, attn_weights: *void, stream: icudaStream_t) -> icudaStatus_t
  Config: qbasis, seq_len, d_model, n_heads, d_head, causal_mask (bool),
  softmax_type (QUADRATIC or EXP_FRU), fru_depth (if EXP_FRU).
  Fused: QK^T matmul → scale → mask → softmax → AV matmul.
  attn_weights output optional (NULL to skip). When written, every row
  sums to D exactly. Verifiable by caller.
  Causal mask is integer comparison: if col > row, weight = 0. Not
  approximate masking — exact zero.

icudaAttentionBackward(config: *icudaAttentionConfig_t, grad_output: *const void, Q: *const void, K: *const void, V: *const void, attn_weights: *const void, grad_Q: *void, grad_K: *void, grad_V: *void, stream: icudaStream_t) -> icudaStatus_t
  Exact gradients via reverse-mode autodiff on the fused attention graph.
  Chain rule and quotient rule are exact in VDR. No gradient clipping
  needed — integer gradients don't explode from accumulation.

icudaAttentionVerifySoftmaxSum(attn_weights: *const void, qbasis: icudaQBasis_t, seq_len: i32, n_heads: i32, violations: *i32, stream: icudaStream_t) -> icudaStatus_t
  Checks every softmax row sums to D. Writes count of violations.
  Expected: always 0. If nonzero, something is broken — not drifted, broken.
  This check is free in production because it's integer equality,
  not tolerance comparison.
```

---

## Module 8: icuda_training

Training loop primitives. SGD, gradient computation, checkpoint.

```
icudaTrainSGDUpdate(qbasis: icudaQBasis_t, params: *void, grads: *const void, lr: *const void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  params -= lr * grads. Exact. LR is a VDR scalar (e.g., 1/1000 at Q16
  is V=65, D=65536 — exact representation of ~0.001). Update is exact
  multiply and exact subtract. No momentum, no Adam — those are separate
  functions below. This is raw SGD.

icudaTrainSGDMomentumUpdate(qbasis: icudaQBasis_t, params: *void, grads: *const void, velocity: *void, lr: *const void, momentum: *const void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  velocity = momentum * velocity + grads. params -= lr * velocity.
  Both operations exact.

icudaTrainAdamUpdate(qbasis: icudaQBasis_t, params: *void, grads: *const void, m: *void, v_adam: *void, lr: *const void, beta1: *const void, beta2: *const void, step: i32, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Adam optimizer in exact integer arithmetic. m and v_adam are first/second
  moment estimates. Bias correction uses exact integer division.
  No epsilon in denominator — if second moment is zero, the gradient
  was zero and the update is zero. Detectable exactly.

icudaTrainComputeLoss(qbasis: icudaQBasis_t, logits: *const void, targets: *const i32, loss: *void, n_classes: i32, batch_size: i32, stream: icudaStream_t) -> icudaStatus_t
  Cross-entropy loss. Uses fn_log builtin for exact logarithm via FRU
  when available, rational approximation otherwise. Loss is a single
  VDR scalar. Monotonic decrease observable as integer comparison
  between epochs — the toy data confirms this works.

icudaTrainBackwardPass(graph: *icudaComputeGraph_t, loss: *const void, stream: icudaStream_t) -> icudaStatus_t
  Reverse-mode autodiff over recorded compute graph. Every node stores
  exact forward values. Chain rule produces exact partial derivatives.
  Quotient rule for softmax backprop is exact. No gradient clipping
  because exact gradients don't diverge from accumulation error.

icudaTrainCheckpointSave(params: *const void, optimizer_state: *const void, qbasis: icudaQBasis_t, n_params: i64, path: *const u8, stream: icudaStream_t) -> icudaStatus_t
  Writes all parameters and optimizer state as raw integers.
  Checkpoint is bit-identical across saves, loads, platforms.
  No precision loss on save. No precision loss on restore. Ever.

icudaTrainCheckpointLoad(params: *void, optimizer_state: *void, qbasis: icudaQBasis_t, n_params: i64, path: *const u8, stream: icudaStream_t) -> icudaStatus_t
  Restores from checkpoint. Bit-identical to state at save time.

icudaTrainComputeGraphCreate(graph: *icudaComputeGraph_t) -> icudaStatus_t
  Creates empty compute graph for recording forward pass operations.
  Used by backward pass to trace exact gradients.

icudaTrainComputeGraphDestroy(graph: icudaComputeGraph_t) -> icudaStatus_t
  Frees graph. Forward values freed with it.

icudaTrainComputeGraphRecord(graph: icudaComputeGraph_t, enabled: bool) -> icudaStatus_t
  Toggles recording. When enabled, all icudaVdr* calls on the active
  stream append nodes to the graph with exact intermediate values.
```

---

## Module 9: icuda_kb

Knowledge Base operations. The data layer from paper Sections 4.1, 4.6.

```
icudaKBCreate(kb_store: *icudaKBStore_t, kb_id: *i32, config: *icudaKBConfig_t) -> icudaStatus_t
  Config: name (text), parent_id (i32, -1 for root), visibility (enum),
  owner (text), max_facts (u32), max_rules (u32), max_children (u32).
  Allocates fixed-size KB struct in kb_store. Returns assigned kb_id
  (sequential integer). Initializes all live fields to empty/zero.
  Adds kb_id to parent's children_ids list.

icudaKBDestroy(kb_store: *icudaKBStore_t, kb_id: i32) -> icudaStatus_t
  Removes KB. Reparents children to destroyed KB's parent.
  Persistent facts are gone. This is permanent deletion, not reset.

icudaKBReset(kb_store: *icudaKBStore_t, kb_id: i32) -> icudaStatus_t
  Clears all live state: LRUs, counters, queues, stacks, ring buffers,
  bitsets, working data. Persistent fields (facts, rules, constraints,
  connections, grammars) untouched. This is the "kill drift" operation.

icudaKBFreeze(kb_store: *icudaKBStore_t, kb_id: i32) -> icudaStatus_t
  Sets frozen=true. No further modifications to persistent fields.
  Live fields still writable (they're session-scoped).
  Frozen KBs are safe to share across clones without COW.

icudaKBUnfreeze(kb_store: *icudaKBStore_t, kb_id: i32) -> icudaStatus_t
  Clears frozen flag. Requires owner match on session user_id.

icudaKBGetInfo(kb_store: *icudaKBStore_t, kb_id: i32, info: *icudaKBInfo_t) -> icudaStatus_t
  Reads: name, path, id, parent_id, n_children, n_facts, n_rules,
  visibility, frozen, owner, created_at, last_modified. All integers/enums.

icudaKBResolvePath(kb_store: *icudaKBStore_t, path: *const u8, kb_id: *i32) -> icudaStatus_t
  Dotted path string → integer kb_id via hash map lookup. One-time cost.
  All subsequent operations use the integer directly.

icudaKBFactAssert(kb_store: *icudaKBStore_t, kb_id: i32, slot_id: i32, fact: *const icudaVdrFact_t) -> icudaStatus_t
  Writes fact at kb_id + slot_id. Fact struct: tag (i32 enum), value (VDR),
  provenance (source_kb_id, source_slot_id, confidence VDR, timestamp i32).
  Checks: session visibility, frozen flag, slot bounds. Integer checks, all.
  Side effect: updates last_modified timestamp.

icudaKBFactQuery(kb_store: *icudaKBStore_t, kb_id: i32, slot_id: i32, fact: *icudaVdrFact_t) -> icudaStatus_t
  Reads fact at kb_id + slot_id. O(1) — two integer indices.
  Checks session visibility via ancestor walk (integer comparisons up
  the parent chain). If KB not visible from session scope, returns
  ERR_KB_ACCESS_DENIED. The fact is never exposed — not redacted, absent.

icudaKBFactRetract(kb_store: *icudaKBStore_t, kb_id: i32, slot_id: i32) -> icudaStatus_t
  Removes fact. Slot becomes empty. Provenance of retraction logged
  as separate audit fact if audit KB configured.

icudaKBFactSearch(kb_store: *icudaKBStore_t, kb_id: i32, tag: i32, results: *icudaVdrFact_t, max_results: i32, n_found: *i32) -> icudaStatus_t
  Linear scan of facts in kb_id matching tag. Returns up to max_results.
  Scoped — only searches this KB, not ancestors (use ScopedSearch for walk).

icudaKBFactScopedSearch(kb_store: *icudaKBStore_t, start_kb_id: i32, tag: i32, results: *icudaVdrFact_t, max_results: i32, n_found: *i32) -> icudaStatus_t
  Walks from start_kb_id up parent chain to root. Returns first match(es).
  This is lexical scoping — "bank" resolves differently depending on
  which KB you start from.

icudaKBChildList(kb_store: *icudaKBStore_t, kb_id: i32, children: *i32, max_children: i32, n_children: *i32) -> icudaStatus_t
  Lists child kb_ids. Integer array.

icudaKBMount(kb_store: *icudaKBStore_t, kb_id: i32, mount_target_id: i32, mount_name: *const u8) -> icudaStatus_t
  Cross-branch reference. Makes mount_target accessible as if it were
  a child of kb_id, without changing the tree structure. Used for
  shared resources (e.g., mount a common grammar KB into multiple scopes).

icudaKBUnmount(kb_store: *icudaKBStore_t, kb_id: i32, mount_name: *const u8) -> icudaStatus_t
  Removes mount point.
```

---

## Module 10: icuda_kb_primitives

Bounded data primitives within KBs. The working memory layer.

```
// --- LRU Cache ---

icudaLRUCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> icudaStatus_t
  Creates named LRU in kb_id's live state. Capacity fixed forever.
  1 <= capacity <= 1000.

icudaLRUGet(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, key: i32, value: *icudaVdrFact_t, found: *bool) -> icudaStatus_t
  Lookup by integer key. Promotes to most-recent on hit. O(1).

icudaLRUPut(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, key: i32, value: *const icudaVdrFact_t) -> icudaStatus_t
  Insert or update. If at capacity, evicts oldest entry. Cannot exceed capacity.

icudaLRUEvictOldest(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Manual eviction. Returns the evicted entry for inspection if needed.

icudaLRUSize(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> icudaStatus_t
  Current entry count. Always <= capacity.

icudaLRUClear(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Empties cache. Capacity unchanged.

// --- Counter ---

icudaCounterCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, min_val: i32, max_val: i32, initial: i32) -> icudaStatus_t
  Bounded integer counter. Clamps at min/max — never wraps, never overflows.

icudaCounterGet(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *i32) -> icudaStatus_t
  Reads current value.

icudaCounterIncrement(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, amount: i32) -> icudaStatus_t
  Adds amount (can be negative for decrement). Clamps at bounds.
  Side effect: if clamped, sets internal clamped flag queryable.

icudaCounterReset(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Sets to initial value.

icudaCounterAtBound(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, at_min: *bool, at_max: *bool) -> icudaStatus_t
  Checks if counter is at either bound.

// --- Lock ---

icudaLockCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Non-blocking coordination signal. Not a mutex — no blocking.

icudaLockAcquire(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, acquired: *bool) -> icudaStatus_t
  Attempts to acquire. Returns immediately with acquired=true or false.

icudaLockRelease(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Releases. Error if not held.

icudaLockQuery(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, held: *bool) -> icudaStatus_t
  Check without acquiring.

// --- Queue (FIFO) ---

icudaQueueCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> icudaStatus_t
  Bounded FIFO. 1 <= capacity <= 1000.

icudaQueuePush(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *const icudaVdrFact_t, pushed: *bool) -> icudaStatus_t
  Enqueue. If full, pushed=false. Queue does not grow.

icudaQueuePop(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *icudaVdrFact_t, popped: *bool) -> icudaStatus_t
  Dequeue oldest. If empty, popped=false.

icudaQueuePeek(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *icudaVdrFact_t, found: *bool) -> icudaStatus_t
  Read oldest without removing.

icudaQueueSize(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> icudaStatus_t
  Current count.

icudaQueueClear(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
  Empty the queue.

// --- Stack (LIFO) ---

icudaStackCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> icudaStatus_t
  Bounded LIFO. 1 <= capacity <= 1000.

icudaStackPush(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *const icudaVdrFact_t, pushed: *bool) -> icudaStatus_t
  Push. If full, pushed=false.

icudaStackPop(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *icudaVdrFact_t, popped: *bool) -> icudaStatus_t
  Pop top. If empty, popped=false.

icudaStackPeek(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *icudaVdrFact_t, found: *bool) -> icudaStatus_t
  Read top without removing.

icudaStackSize(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> icudaStatus_t
icudaStackClear(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t

// --- Ring Buffer ---

icudaRingCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> icudaStatus_t
  Fixed-size sliding window. Oldest overwritten when full.

icudaRingWrite(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, value: *const icudaVdrFact_t) -> icudaStatus_t
  Always succeeds. If full, overwrites oldest. No pushed flag needed.

icudaRingRead(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, index: i32, value: *icudaVdrFact_t) -> icudaStatus_t
  Read by index relative to oldest (0 = oldest current, size-1 = newest).

icudaRingSize(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> icudaStatus_t
icudaRingClear(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t

// --- Bitset ---

icudaBitsetCreate(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, n_bits: i32) -> icudaStatus_t
  Fixed size. 1 <= n_bits <= 10000. Initialized all-clear.

icudaBitsetSet(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, bit: i32) -> icudaStatus_t
icudaBitsetClear(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, bit: i32) -> icudaStatus_t
icudaBitsetGet(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, bit: i32, set: *bool) -> icudaStatus_t
icudaBitsetPopcount(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8, count: *i32) -> icudaStatus_t
  Number of set bits. For tracking completion percentage as exact fraction:
  popcount / n_bits.
icudaBitsetClearAll(kb_store: *icudaKBStore_t, kb_id: i32, name: *const u8) -> icudaStatus_t
```

---

## Module 11: icuda_prolog

Prolog engine on GPU. Parallel unification over fact tables.

```
icudaPrologRuleAssert(kb_store: *icudaKBStore_t, kb_id: i32, rule: *const icudaPrologRule_t) -> icudaStatus_t
  Adds rule to KB's rule set. Rule struct: head (term), body (array of
  term conditions), action (array of term assertions/retractions).
  Terms are typed: atom (i32 tag), variable (i32 binding slot), vdr_value,
  list, compound (functor + args). All integer representations.
  Side effect: rule is persistent — survives reset, participates in snapshots.

icudaPrologRuleRetract(kb_store: *icudaKBStore_t, kb_id: i32, rule_id: i32) -> icudaStatus_t
  Removes rule by ID.

icudaPrologQuery(kb_store: *icudaKBStore_t, start_kb_id: i32, query: *const icudaPrologTerm_t, bindings: *icudaPrologBindings_t, max_results: i32, n_results: *i32, stream: icudaStream_t) -> icudaStatus_t
  Depth-first search with backtracking, depth limit 100.
  Scoped: starts at start_kb_id, walks ancestors.
  Unification: cross-multiply comparison on VDR values. Exact.
  Parallelized: candidate facts loaded into shared memory, cross-multiply
  comparisons distributed across warps. Filter, collect.
  Bindings: array of variable→value pairs for each result.

icudaPrologFireAll(kb_store: *icudaKBStore_t, kb_id: i32, fired: *icudaPrologFired_t, max_fired: i32, n_fired: *i32, stream: icudaStream_t) -> icudaStatus_t
  Evaluates all rules in kb_id against current fact state. Returns list
  of rules that fired and their resulting assertions/retractions.
  Does NOT apply the results — caller decides whether to commit.
  This is the L3 auto-fire mechanism: call this on a schedule,
  commit the results, zero LLM tokens.

icudaPrologFireAndCommit(kb_store: *icudaKBStore_t, kb_id: i32, n_fired: *i32, stream: icudaStream_t) -> icudaStatus_t
  FireAll + automatically commit results (assert new facts, retract matched).
  For polling runners where human review isn't needed.
  Side effect: KB facts modified.

icudaPrologUnify(a: *const icudaPrologTerm_t, b: *const icudaPrologTerm_t, bindings: *icudaPrologBindings_t, unified: *bool) -> icudaStatus_t
  Low-level single unification. Device-callable for custom kernels.
  Compares terms structurally. VDR values compared by cross-multiply.

icudaPrologRuleStats(kb_store: *icudaKBStore_t, kb_id: i32, rule_id: i32, stats: *icudaPrologRuleStats_t) -> icudaStatus_t
  Returns: fire_count, last_fired_timestamp, success_rate_numerator,
  success_rate_denominator. For hygiene: stale = not fired in 90 days,
  failing = success_rate < 20/100.

icudaPrologHygiene(kb_store: *icudaKBStore_t, kb_id: i32, stale_days: i32, min_success_rate_num: i32, min_success_rate_den: i32, candidates: *i32, max_candidates: i32, n_candidates: *i32) -> icudaStatus_t
  Identifies rules that are stale, failing, or orphaned (reference
  retracted facts). Returns rule_ids for review/pruning. Does not
  auto-delete — returns candidates for caller decision.
```

---

## Module 12: icuda_grammar

Grammar-directed structural token generation.

```
icudaGrammarCreate(grammar: *icudaGrammar_t, template: *const u8, template_len: i32) -> icudaStatus_t
  Parses template string with typed slot markers: {slot_name:type}.
  Types: vdr_value, text, integer, enum(val1|val2|val3).
  Template is the structural frame — every byte outside {} is literal.
  Validation: template must be syntactically valid with all slots filled
  by any valid value of declared type.

icudaGrammarDestroy(grammar: icudaGrammar_t) -> icudaStatus_t
  Frees grammar.

icudaGrammarStoreInKB(kb_store: *icudaKBStore_t, kb_id: i32, grammar_slot: i32, grammar: icudaGrammar_t) -> icudaStatus_t
  Persists grammar in KB. Survives reset, participates in snapshots.
  Inherited by children KBs through tree walk.

icudaGrammarLoadFromKB(kb_store: *icudaKBStore_t, kb_id: i32, grammar_slot: i32, grammar: *icudaGrammar_t) -> icudaStatus_t
  Loads grammar from KB. Walks ancestors if not found in target KB.

icudaGrammarRender(grammar: icudaGrammar_t, fills: *const icudaGrammarFill_t, n_fills: i32, output: *u8, output_capacity: i32, output_len: *i32) -> icudaStatus_t
  Fills slots with provided values, produces output bytes.
  Every structural byte comes from the template — deterministic, 100% correct.
  Fills are validated against declared slot types. Type mismatch = error,
  not silent coercion.
  LLM contribution: the fill values. Grammar contribution: everything else.

icudaGrammarRenderFromKB(grammar: icudaGrammar_t, kb_store: *icudaKBStore_t, slot_kb_mappings: *const icudaGrammarKBMapping_t, n_mappings: i32, output: *u8, output_capacity: i32, output_len: *i32) -> icudaStatus_t
  Fills slots directly from KB facts. Mapping: slot_name → kb_id + slot_id.
  Data goes from KB to output without entering any token stream.

icudaGrammarValidate(grammar: icudaGrammar_t, valid: *bool, error_msg: *u8, error_msg_capacity: i32) -> icudaStatus_t
  Checks template is structurally valid. Run at creation time.
  If valid=true, every possible rendering is syntactically correct by construction.

icudaGrammarListSlots(grammar: icudaGrammar_t, slots: *icudaGrammarSlotInfo_t, max_slots: i32, n_slots: *i32) -> icudaStatus_t
  Enumerates slots with their names and types. For tooling and introspection.

icudaGrammarCompose(outer: icudaGrammar_t, inner: icudaGrammar_t, slot_name: *const u8, composed: *icudaGrammar_t) -> icudaStatus_t
  Nests inner grammar into a slot of outer. For building complex output
  from simple templates. Composed grammar inherits validity from both.
```

---

## Module 13: icuda_runner

Autonomous execution loops. The daemon layer.

```
icudaRunnerCreatePoller(runner: *icudaRunner_t, config: *icudaPollerConfig_t) -> icudaStatus_t
  Config: interval_ms (i32), session (icudaSession_t),
  poll_fn (callback: session → status), max_consecutive_errors (i32).
  Spawns host thread that calls poll_fn every interval_ms.
  Each invocation gets a fresh LLM context (no attention degradation).
  poll_fn checks queues, evaluates counters, fires rules.

icudaRunnerCreateProcessor(runner: *icudaRunner_t, config: *icudaProcessorConfig_t) -> icudaStatus_t
  Config: session, source_type (enum: PROMETHEUS, DEPLOY_API, ALERT_STREAM,
  CUSTOM), connection_params (opaque bytes), ingest_fn (callback: data → status),
  max_turns_before_recycle (i32, default 200).
  Maintains persistent connection to external source. Calls ingest_fn on
  each incoming data item to compact into KB facts. At max_turns: snapshot
  connection state, kill, reclone, restore connection. Continuous data,
  always-fresh LLM.

icudaRunnerCreateInternal(runner: *icudaRunner_t, config: *icudaInternalConfig_t) -> icudaStatus_t
  Config: session, interval_ms, compute_fn (callback: session → status).
  Scheduled internal computation. Derives facts: rolling averages as
  exact fractions, trend directions as exact comparisons, coverage gaps.
  No external connections.

icudaRunnerCreateBatch(runner: *icudaRunner_t, config: *icudaBatchConfig_t) -> icudaStatus_t
  Config: session, task_queue_kb_id (i32), task_queue_name (text),
  process_fn (callback: task → status), max_concurrent (i32).
  Pulls tasks from KB queue, processes each with fresh session clone.
  Clone-per-task isolation. Results written to parent session KB.

icudaRunnerStart(runner: icudaRunner_t) -> icudaStatus_t
  Begins execution loop. Non-blocking — returns immediately.

icudaRunnerStop(runner: icudaRunner_t) -> icudaStatus_t
  Signals stop. Current iteration completes. Blocks until stopped.

icudaRunnerKill(runner: icudaRunner_t) -> icudaStatus_t
  Immediate termination. No cleanup. For drift-kill scenarios.

icudaRunnerGetStatus(runner: icudaRunner_t, status: *icudaRunnerStatus_t) -> icudaStatus_t
  Reports: state (RUNNING/STOPPED/ERROR), iterations_completed,
  errors_consecutive, last_iteration_ms, session_turn_count.

icudaRunnerRecycle(runner: icudaRunner_t) -> icudaStatus_t
  Manual recycle: snapshot session, kill, reclone from snapshot.
  Resets turn count. Drift dies. Knowledge persists.

icudaRunnerDestroy(runner: icudaRunner_t) -> icudaStatus_t
  Stop if running, destroy session if owned, free resources.
```

---

## Module 14: icuda_safety

Structural access control. Integer comparisons, not behavioral guardrails.

```
icudaSafetyCheckAccess(kb_store: *icudaKBStore_t, session: icudaSession_t, kb_id: i32, access: *bool) -> icudaStatus_t
  The core check. Walks from kb_id up parent chain. At each ancestor:
  is ancestor visible from session's visibility_level? Is session's
  user_id in the authorized set? Two integer comparisons per ancestor.
  If any ancestor fails, access=false. KB is absent from session scope.
  This runs BEFORE any data is read — not a filter on results, a gate
  on access.

icudaSafetyGrantCreate(kb_store: *icudaKBStore_t, kb_id: i32, grant: *const icudaGrant_t) -> icudaStatus_t
  Grant struct: grant_class (enum: FILESYSTEM, COMPILE, EXECUTE, LINT,
  NETWORK, PROCESS), target_pattern (text), max_uses (i32, -1=unlimited),
  expires_at (i32 timestamp, 0=never), holder_user_id (i32).
  Stored as KB fact in the grant KB. Only admin-level sessions can create.

icudaSafetyGrantCheck(kb_store: *icudaKBStore_t, session: icudaSession_t, grant_class: icudaGrantClass_t, target: *const u8, granted: *bool) -> icudaStatus_t
  Checks if session's user_id holds an active grant matching class+target.
  Active = not expired AND uses_remaining > 0 AND not revoked.
  Integer comparisons throughout.
  Side effect: if granted, decrements uses_remaining.

icudaSafetyGrantRevoke(kb_store: *icudaKBStore_t, grant_id: i32) -> icudaStatus_t
  Permanent revocation. Logged with timestamp and revoker user_id.
  No unrevoke. Create a new grant instead.

icudaSafetyGrantList(kb_store: *icudaKBStore_t, user_id: i32, grants: *icudaGrant_t, max_grants: i32, n_grants: *i32) -> icudaStatus_t
  Lists all grants for user_id. For audit.

icudaSafetyAuditLog(kb_store: *icudaKBStore_t, audit_kb_id: i32, entry: *const icudaAuditEntry_t) -> icudaStatus_t
  Writes audit entry: timestamp, user_id, action (enum), target_kb_id,
  target_slot_id, grant_used, result (allowed/denied). All integers.
  Append-only to audit KB's ring buffer.

icudaSafetyAuditQuery(kb_store: *icudaKBStore_t, audit_kb_id: i32, filter: *const icudaAuditFilter_t, entries: *icudaAuditEntry_t, max_entries: i32, n_entries: *i32) -> icudaStatus_t
  Filter by user_id, time range, action type. Integer comparisons.
```

---

## Module 15: icuda_confidence

Exact confidence propagation. Replaces hedging language.

```
icudaConfidenceFromSource(source_type: icudaSourceType_t, confidence: *icudaVdrFact_t) -> icudaStatus_t
  Returns the declared confidence for a source type per the knowability
  spectrum (Appendix F): VDR_COMPUTATION=1/1, PROLOG_DERIVATION=1/1,
  DATABASE=98/100, PROMETHEUS=95/100, SCRIPT=95/100, REST_API=85/100,
  PUBLISHED=80/100, USER_STATED=70/100, WEB_SEARCH=50/100,
  LLM_GENERATED=30/100, UNKNOWN=0/1. All exact VDR fractions.

icudaConfidenceCombineAgreeing(sources: *const icudaVdrFact_t, n_sources: i32, combined: *icudaVdrFact_t) -> icudaStatus_t
  Formula: 1 - product(1 - C_i). Exact VDR arithmetic.
  Two sources at 85/100 → 1 - (15/100 * 15/100) = 1 - 225/10000 = 9775/10000.
  Exact fraction, not 0.9775.

icudaConfidenceCombineConflicting(sources: *const icudaVdrFact_t, n_sources: i32, penalty: *const icudaVdrFact_t, combined: *icudaVdrFact_t) -> icudaStatus_t
  Agreeing formula with penalty multiplier applied per conflict.
  Penalty is configurable VDR fraction.

icudaConfidenceChain(per_link: *const icudaVdrFact_t, n_links: i32, chained: *icudaVdrFact_t) -> icudaStatus_t
  Chain of N links: C^N. Exact VDR exponentiation.
  3 links at 85/100 → 614125/1000000. Exact.

icudaConfidencePropagate(provenance: *const icudaProvenance_t, result: *icudaVdrFact_t) -> icudaStatus_t
  Full propagation from provenance chain. Walks the derivation tree,
  applies combine/chain rules based on structure. Result is a single
  exact VDR fraction with full provenance traceable.
```

---

## Module 16: icuda_distributed

Multi-GPU and multi-node communication. Replaces NCCL.

```
icudaDistAllReduce(sendbuf: *const void, recvbuf: *void, count: i64, qbasis: icudaQBasis_t, op: icudaReduceOp_t, comm: icudaComm_t, stream: icudaStream_t) -> icudaStatus_t
  Op: SUM, MAX, MIN. Integer operations. SUM is associative and commutative
  regardless of reduction order. Result is deterministic across all
  reduction topologies — ring, tree, butterfly, anything.
  This single property eliminates non-deterministic distributed training.

icudaDistBroadcast(buf: *void, count: i64, root: i32, comm: icudaComm_t, stream: icudaStream_t) -> icudaStatus_t
  Root sends, all receive. Bit-identical at all ranks.

icudaDistAllGather(sendbuf: *const void, recvbuf: *void, sendcount: i64, comm: icudaComm_t, stream: icudaStream_t) -> icudaStatus_t
  Each rank sends, all ranks receive concatenated result.

icudaDistReduceScatter(sendbuf: *const void, recvbuf: *void, recvcount: i64, qbasis: icudaQBasis_t, op: icudaReduceOp_t, comm: icudaComm_t, stream: icudaStream_t) -> icudaStatus_t
  Reduce + scatter. Each rank gets a chunk of the reduced result.

icudaDistCommCreate(comm: *icudaComm_t, n_ranks: i32, rank: i32) -> icudaStatus_t
  Creates communicator. Standard MPI-like setup.

icudaDistCommDestroy(comm: icudaComm_t) -> icudaStatus_t

icudaDistCommGetRank(comm: icudaComm_t, rank: *i32) -> icudaStatus_t
icudaDistCommGetSize(comm: icudaComm_t, size: *i32) -> icudaStatus_t

icudaDistKBSync(kb_store: *icudaKBStore_t, kb_id: i32, comm: icudaComm_t, stream: icudaStream_t) -> icudaStatus_t
  Synchronizes KB facts across ranks. Deterministic merge — same
  facts at same slots produce same result regardless of arrival order
  because integer comparison resolves conflicts identically everywhere.

icudaDistSnapshotBroadcast(snapshot: *icudaSnapshot_t, root: i32, comm: icudaComm_t) -> icudaStatus_t
  Broadcast a session snapshot to all ranks. For distributed clone:
  all ranks start from bit-identical state.
```

---

## Module 17: icuda_transform

Signal processing, DFT, convolution — all exact integer.

```
icudaTransformDFT(qbasis: icudaQBasis_t, input_real: *const void, input_imag: *const void, output_real: *void, output_imag: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact DFT. Twiddle factors are exact VDR fractions (rational
  approximations of roots of unity at declared precision).
  Roundtrip: DFT → IDFT returns original values exactly (paper Appendix H).
  Complex represented as real/imag pair, both VDR.

icudaTransformIDFT(qbasis: icudaQBasis_t, input_real: *const void, input_imag: *const void, output_real: *void, output_imag: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Inverse DFT. Exact roundtrip with DFT.

icudaTransformConv1D(qbasis: icudaQBasis_t, input: *const void, kernel: *const void, output: *void, input_len: i32, kernel_len: i32, stream: icudaStream_t) -> icudaStatus_t
  1D convolution via direct multiply-accumulate. Exact.

icudaTransformConv2D(qbasis: icudaQBasis_t, input: *const void, kernel: *const void, output: *void, in_h: i32, in_w: i32, k_h: i32, k_w: i32, stream: icudaStream_t) -> icudaStatus_t
  2D convolution. For image processing layers that use VDR.
```

---

## Module 18: icuda_linalg

Linear algebra. Replaces cuSOLVER, cuSPARSE for VDR types.

```
icudaLinalgMatVecMul(qbasis: icudaQBasis_t, A: *const void, x: *const void, y: *void, m: i32, n: i32, stream: icudaStream_t) -> icudaStatus_t
  y = A*x. Exact integer MAC.

icudaLinalgTranspose(qbasis: icudaQBasis_t, input: *const void, output: *void, m: i32, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Matrix transpose. Data movement only, no arithmetic — exact trivially.

icudaLinalgGaussianElim(qbasis: icudaQBasis_t, A: *void, b: *void, x: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Solve Ax=b. Gaussian elimination with exact VDR division.
  No pivoting heuristics for numerical stability — not needed because
  there's no numerical instability. Pivot for zero-avoidance only.

icudaLinalgInverse(qbasis: icudaQBasis_t, A: *const void, A_inv: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact matrix inverse. Works where float64 fails (Hilbert matrix,
  paper Appendix H). Via Gaussian elimination on [A|I].

icudaLinalgDeterminant(qbasis: icudaQBasis_t, A: *const void, det: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact determinant via elimination. Single VDR scalar result.

icudaLinalgGramSchmidt(qbasis: icudaQBasis_t, vectors: *const void, orthogonal: *void, n_vectors: i32, dim: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact orthogonalization. Dot products exact, projections exact,
  subtraction exact. No drift in the orthogonalized basis.

icudaLinalgEigenvalues(qbasis: icudaQBasis_t, A: *const void, eigenvalues_real: *void, eigenvalues_imag: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Eigenvalue computation. Real and imaginary parts as VDR.
  Iterative methods with exact convergence detection (equality, not tolerance).

icudaLinalgSVD(qbasis: icudaQBasis_t, A: *const void, U: *void, S: *void, Vt: *void, m: i32, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Singular value decomposition. Exact factors.
```

---

## Module 19: icuda_stats

Statistics and probability. Exact fractions throughout.

```
icudaStatsMean(qbasis: icudaQBasis_t, data: *const void, result: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact mean: sum / n. Both exact.

icudaStatsVariance(qbasis: icudaQBasis_t, data: *const void, result: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact variance: sum((x_i - mean)^2) / n. All exact.

icudaStatsMedian(qbasis: icudaQBasis_t, data: *const void, result: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact median via integer sort.

icudaStatsBayes(qbasis: icudaQBasis_t, prior: *const void, likelihood: *const void, evidence: *const void, posterior: *void, n_hypotheses: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact Bayesian update: posterior = (prior * likelihood) / evidence.
  All VDR fractions. Posterior sums to exactly 1/1.

icudaStatsNormalize(qbasis: icudaQBasis_t, data: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Divides each element by sum so elements sum to D exactly.
  Same guarantee as softmax: exact normalization.

icudaStatsHistogram(qbasis: icudaQBasis_t, data: *const void, bins: *const void, counts: *i32, n_data: i32, n_bins: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact bin assignment via integer comparison. No bin-boundary ambiguity.

icudaStatsCorrelation(qbasis: icudaQBasis_t, x: *const void, y: *const void, result: *void, n: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact Pearson correlation as VDR fraction.
```

---

## Module 20: icuda_numbertheory

Number theory primitives from paper Appendix L.

```
icudaNTGCD(a: *const void, b: *const void, result: *void, qbasis: icudaQBasis_t) -> icudaStatus_t
  Euclidean GCD. Exact.

icudaNTLCM(a: *const void, b: *const void, result: *void, qbasis: icudaQBasis_t) -> icudaStatus_t
icudaNTModPow(base: *const void, exp: *const void, modulus: *const void, result: *void, qbasis: icudaQBasis_t) -> icudaStatus_t
  Modular exponentiation. For cryptographic operations.

icudaNTCRT(remainders: *const void, moduli: *const void, result: *void, n: i32, qbasis: icudaQBasis_t) -> icudaStatus_t
  Chinese Remainder Theorem.

icudaNTEulerTotient(n: *const void, result: *void, qbasis: icudaQBasis_t) -> icudaStatus_t
icudaNTIsPrime(n: *const void, result: *bool, qbasis: icudaQBasis_t) -> icudaStatus_t
  Deterministic primality for bounded inputs.

icudaNTFactorize(n: *const void, factors: *void, max_factors: i32, n_factors: *i32, qbasis: icudaQBasis_t) -> icudaStatus_t
  Trial division up to sqrt(n). For bounded inputs.
```

---

## Module 21: icuda_functional_remainder

FRU operations for transcendental computation.

```
icudaFRUSqrt(qbasis: icudaQBasis_t, input: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact sqrt via Newton recurrence to declared depth. Remainder carries
  the residual. Depth 4-6 typically sufficient for Q335.

icudaFRUExp(qbasis: icudaQBasis_t, input: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact exp via Taylor/Padé recurrence. Range-reduced first.

icudaFRULog(qbasis: icudaQBasis_t, input: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t
  Exact log via recurrence.

icudaFRUSin(qbasis: icudaQBasis_t, input: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t
icudaFRUCos(qbasis: icudaQBasis_t, input: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t

icudaFRUAtan2(qbasis: icudaQBasis_t, y: *const void, x: *const void, output: *void, depth: i32, stream: icudaStream_t) -> icudaStatus_t

icudaFRUResolve(qbasis: icudaQBasis_t, data: *void, n: i32, target_depth: i32, stream: icudaStream_t) -> icudaStatus_t
  Batch remainder resolution. Takes array of VDR values, resolves
  remainders to target_depth via FRU recurrence. In-place.
  Used for continuous resolution in processor runners.

icudaFRUAvailable(available: *bool) -> icudaStatus_t
  Reports whether current device has FRU hardware. Phase 1: false.
  Phase 2: maybe. Phase 3: true. Callers fall back to software
  recurrence on host CPU when FRU unavailable.
```

---

## Module 22: icuda_builtins

The 448 deterministic primitives, exposed as host-callable functions that dispatch to device kernels. Organized by paper Appendix L categories.

```
// --- Text (17 functions) ---
icudaBuiltinTextReverse(input: *const u8, len: i32, output: *u8) -> icudaStatus_t
icudaBuiltinTextSplit(input: *const u8, len: i32, delimiter: u8, parts: *icudaTextSlice_t, max_parts: i32, n_parts: *i32) -> icudaStatus_t
icudaBuiltinTextContains(haystack: *const u8, h_len: i32, needle: *const u8, n_len: i32, found: *bool) -> icudaStatus_t
icudaBuiltinTextReplace(input: *const u8, len: i32, old: *const u8, old_len: i32, new: *const u8, new_len: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinTextJoin(parts: *const icudaTextSlice_t, n_parts: i32, separator: *const u8, sep_len: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinTextTrim(input: *const u8, len: i32, output: *u8, out_len: *i32) -> icudaStatus_t
icudaBuiltinTextUpper(input: *u8, len: i32) -> icudaStatus_t
icudaBuiltinTextLower(input: *u8, len: i32) -> icudaStatus_t
icudaBuiltinTextStartsWith(input: *const u8, len: i32, prefix: *const u8, p_len: i32, result: *bool) -> icudaStatus_t
icudaBuiltinTextEndsWith(input: *const u8, len: i32, suffix: *const u8, s_len: i32, result: *bool) -> icudaStatus_t
icudaBuiltinTextIndexOf(haystack: *const u8, h_len: i32, needle: *const u8, n_len: i32, index: *i32) -> icudaStatus_t
icudaBuiltinTextSubstring(input: *const u8, len: i32, start: i32, end: i32, output: *u8, out_len: *i32) -> icudaStatus_t
icudaBuiltinTextRepeat(input: *const u8, len: i32, count: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinTextPadLeft(input: *const u8, len: i32, width: i32, pad_char: u8, output: *u8) -> icudaStatus_t
icudaBuiltinTextPadRight(input: *const u8, len: i32, width: i32, pad_char: u8, output: *u8) -> icudaStatus_t
icudaBuiltinTextCharAt(input: *const u8, len: i32, index: i32, ch: *u8) -> icudaStatus_t
icudaBuiltinTextLength(input: *const u8, len: *i32) -> icudaStatus_t

// --- Collections (36 functions) ---
icudaBuiltinSort(qbasis: icudaQBasis_t, data: *void, n: i32) -> icudaStatus_t
  In-place integer comparison sort. O(n log n). Exact ordering — no
  tolerance ambiguity at sort boundaries.
icudaBuiltinSortBy(qbasis: icudaQBasis_t, data: *void, keys: *const void, n: i32) -> icudaStatus_t
icudaBuiltinFilter(qbasis: icudaQBasis_t, data: *const void, mask: *const bool, output: *void, n: i32, n_out: *i32) -> icudaStatus_t
icudaBuiltinMap(qbasis: icudaQBasis_t, data: *const void, op: icudaUnaryOp_t, output: *void, n: i32) -> icudaStatus_t
icudaBuiltinReduce(qbasis: icudaQBasis_t, data: *const void, op: icudaBinaryOp_t, initial: *const void, result: *void, n: i32) -> icudaStatus_t
icudaBuiltinGroupBy(qbasis: icudaQBasis_t, data: *const void, keys: *const void, groups: *icudaGroup_t, n: i32, max_groups: i32, n_groups: *i32) -> icudaStatus_t
icudaBuiltinFrequencies(qbasis: icudaQBasis_t, data: *const void, values: *void, counts: *i32, n: i32, max_unique: i32, n_unique: *i32) -> icudaStatus_t
icudaBuiltinDistinct(qbasis: icudaQBasis_t, data: *const void, output: *void, n: i32, n_distinct: *i32) -> icudaStatus_t
icudaBuiltinFlatten(data: **const void, lengths: *const i32, n_arrays: i32, output: *void, total: *i32) -> icudaStatus_t
icudaBuiltinChunk(data: *const void, n: i32, chunk_size: i32, chunks: **void, n_chunks: *i32) -> icudaStatus_t
icudaBuiltinZip(a: *const void, b: *const void, output: *icudaPair_t, n: i32) -> icudaStatus_t
icudaBuiltinUnzip(pairs: *const icudaPair_t, a: *void, b: *void, n: i32) -> icudaStatus_t
icudaBuiltinReverse(data: *void, elem_size: i32, n: i32) -> icudaStatus_t
icudaBuiltinRotate(data: *void, elem_size: i32, n: i32, amount: i32) -> icudaStatus_t
icudaBuiltinTakeFirst(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> icudaStatus_t
icudaBuiltinTakeLast(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> icudaStatus_t
icudaBuiltinDropFirst(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> icudaStatus_t
icudaBuiltinDropLast(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> icudaStatus_t
icudaBuiltinPartition(qbasis: icudaQBasis_t, data: *const void, pred: *const bool, true_out: *void, false_out: *void, n: i32, n_true: *i32, n_false: *i32) -> icudaStatus_t
icudaBuiltinInterleave(a: *const void, b: *const void, output: *void, elem_size: i32, n_a: i32, n_b: i32) -> icudaStatus_t
icudaBuiltinEnumerate(data: *const void, output: *icudaIndexed_t, n: i32) -> icudaStatus_t
icudaBuiltinMinBy(qbasis: icudaQBasis_t, data: *const void, keys: *const void, result: *void, n: i32) -> icudaStatus_t
icudaBuiltinMaxBy(qbasis: icudaQBasis_t, data: *const void, keys: *const void, result: *void, n: i32) -> icudaStatus_t
icudaBuiltinScan(qbasis: icudaQBasis_t, data: *const void, op: icudaBinaryOp_t, output: *void, n: i32) -> icudaStatus_t
  Prefix scan. Exact integer accumulation — no drift across n elements.
icudaBuiltinAll(predicates: *const bool, n: i32, result: *bool) -> icudaStatus_t
icudaBuiltinAny(predicates: *const bool, n: i32, result: *bool) -> icudaStatus_t
icudaBuiltinNone(predicates: *const bool, n: i32, result: *bool) -> icudaStatus_t
icudaBuiltinCount(predicates: *const bool, n: i32, count: *i32) -> icudaStatus_t
icudaBuiltinFindFirst(qbasis: icudaQBasis_t, data: *const void, target: *const void, n: i32, index: *i32) -> icudaStatus_t
icudaBuiltinFindLast(qbasis: icudaQBasis_t, data: *const void, target: *const void, n: i32, index: *i32) -> icudaStatus_t
icudaBuiltinFindAll(qbasis: icudaQBasis_t, data: *const void, target: *const void, n: i32, indices: *i32, max_indices: i32, n_found: *i32) -> icudaStatus_t
icudaBuiltinBinarySearch(qbasis: icudaQBasis_t, sorted_data: *const void, target: *const void, n: i32, index: *i32, found: *bool) -> icudaStatus_t
icudaBuiltinMerge(qbasis: icudaQBasis_t, a: *const void, b: *const void, output: *void, n_a: i32, n_b: i32) -> icudaStatus_t
  Merge two sorted arrays. Exact comparison at merge boundaries.
icudaBuiltinDeduplicate(qbasis: icudaQBasis_t, sorted_data: *void, n: i32, n_deduped: *i32) -> icudaStatus_t
icudaBuiltinWindow(data: *const void, elem_size: i32, n: i32, window_size: i32, windows: **void, n_windows: *i32) -> icudaStatus_t
icudaBuiltinCartesianProduct(a: *const void, b: *const void, output: *icudaPair_t, n_a: i32, n_b: i32) -> icudaStatus_t

// --- Sets (14 functions) ---
icudaBuiltinSetUnion(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> icudaStatus_t
icudaBuiltinSetIntersection(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> icudaStatus_t
icudaBuiltinSetDifference(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> icudaStatus_t
icudaBuiltinSetSymmetricDiff(qbasis: icudaQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> icudaStatus_t
icudaBuiltinSetIsSubset(qbasis: icudaQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> icudaStatus_t
icudaBuiltinSetIsSuperset(qbasis: icudaQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> icudaStatus_t
icudaBuiltinSetIsDisjoint(qbasis: icudaQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> icudaStatus_t
icudaBuiltinSetContains(qbasis: icudaQBasis_t, set: *const void, element: *const void, n: i32, result: *bool) -> icudaStatus_t
icudaBuiltinSetAdd(qbasis: icudaQBasis_t, set: *void, element: *const void, n: *i32, max_n: i32, added: *bool) -> icudaStatus_t
icudaBuiltinSetRemove(qbasis: icudaQBasis_t, set: *void, element: *const void, n: *i32, removed: *bool) -> icudaStatus_t
icudaBuiltinSetSize(n: i32, size: *i32) -> icudaStatus_t
icudaBuiltinSetEqual(qbasis: icudaQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, equal: *bool) -> icudaStatus_t
icudaBuiltinSetPowerSet(qbasis: icudaQBasis_t, set: *const void, n: i32, output: **void, n_subsets: *i32) -> icudaStatus_t
icudaBuiltinSetFromArray(qbasis: icudaQBasis_t, data: *const void, n: i32, set: *void, n_unique: *i32) -> icudaStatus_t

// --- Mappings (15 functions) ---
icudaBuiltinMapGet(map: *const icudaMap_t, key: i32, value: *icudaVdrFact_t, found: *bool) -> icudaStatus_t
icudaBuiltinMapSet(map: *icudaMap_t, key: i32, value: *const icudaVdrFact_t) -> icudaStatus_t
icudaBuiltinMapDelete(map: *icudaMap_t, key: i32, deleted: *bool) -> icudaStatus_t
icudaBuiltinMapContainsKey(map: *const icudaMap_t, key: i32, found: *bool) -> icudaStatus_t
icudaBuiltinMapKeys(map: *const icudaMap_t, keys: *i32, max_keys: i32, n_keys: *i32) -> icudaStatus_t
icudaBuiltinMapValues(map: *const icudaMap_t, values: *icudaVdrFact_t, max_values: i32, n_values: *i32) -> icudaStatus_t
icudaBuiltinMapSize(map: *const icudaMap_t, size: *i32) -> icudaStatus_t
icudaBuiltinMapMerge(a: *const icudaMap_t, b: *const icudaMap_t, out: *icudaMap_t, policy: icudaMergePolicy_t) -> icudaStatus_t
icudaBuiltinMapFilterKeys(map: *const icudaMap_t, pred: *const bool, out: *icudaMap_t) -> icudaStatus_t
icudaBuiltinMapFilterValues(qbasis: icudaQBasis_t, map: *const icudaMap_t, pred: *const bool, out: *icudaMap_t) -> icudaStatus_t
icudaBuiltinMapMapValues(qbasis: icudaQBasis_t, map: *const icudaMap_t, op: icudaUnaryOp_t, out: *icudaMap_t) -> icudaStatus_t
icudaBuiltinMapInvert(map: *const icudaMap_t, out: *icudaMap_t) -> icudaStatus_t
icudaBuiltinMapClear(map: *icudaMap_t) -> icudaStatus_t
icudaBuiltinMapEqual(a: *const icudaMap_t, b: *const icudaMap_t, equal: *bool) -> icudaStatus_t
icudaBuiltinMapFromArrays(keys: *const i32, values: *const icudaVdrFact_t, n: i32, map: *icudaMap_t) -> icudaStatus_t

// --- Conversion (14 functions) ---
icudaBuiltinParseJson(input: *const u8, len: i32, kb_store: *icudaKBStore_t, target_kb_id: i32) -> icudaStatus_t
  Compiled JSON parser. Output goes to KB facts at integer addresses.
  Zero LLM tokens. Cannot fail on valid JSON.
icudaBuiltinParseCsv(input: *const u8, len: i32, kb_store: *icudaKBStore_t, target_kb_id: i32, delimiter: u8) -> icudaStatus_t
icudaBuiltinParseXml(input: *const u8, len: i32, kb_store: *icudaKBStore_t, target_kb_id: i32) -> icudaStatus_t
icudaBuiltinParseYaml(input: *const u8, len: i32, kb_store: *icudaKBStore_t, target_kb_id: i32) -> icudaStatus_t
icudaBuiltinToJson(kb_store: *icudaKBStore_t, kb_id: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinToCsv(kb_store: *icudaKBStore_t, kb_id: i32, output: *u8, out_cap: i32, out_len: *i32, delimiter: u8) -> icudaStatus_t
icudaBuiltinToFraction(qbasis: icudaQBasis_t, numerator: i64, denominator: i64, result: *void) -> icudaStatus_t
icudaBuiltinFromFraction(qbasis: icudaQBasis_t, value: *const void, numerator: *i64, denominator: *i64) -> icudaStatus_t
icudaBuiltinFormatNumber(qbasis: icudaQBasis_t, value: *const void, format: *const u8, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinParseNumber(qbasis: icudaQBasis_t, input: *const u8, len: i32, result: *void) -> icudaStatus_t
icudaBuiltinVdrToDecimalString(qbasis: icudaQBasis_t, value: *const void, precision: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinDecimalStringToVdr(qbasis: icudaQBasis_t, input: *const u8, len: i32, result: *void) -> icudaStatus_t
icudaBuiltinBaseConvert(value: i64, from_base: i32, to_base: i32, output: *u8, out_cap: i32, out_len: *i32) -> icudaStatus_t
icudaBuiltinTimestampToFields(timestamp: i32, year: *i32, month: *i32, day: *i32, hour: *i32, minute: *i32, second: *i32) -> icudaStatus_t

// --- Graph Operations (13 functions) ---
icudaBuiltinGraphCreate(graph: *icudaGraph_t, max_nodes: i32, max_edges: i32) -> icudaStatus_t
icudaBuiltinGraphAddNode(graph: *icudaGraph_t, node_id: i32) -> icudaStatus_t
icudaBuiltinGraphAddEdge(graph: *icudaGraph_t, from: i32, to: i32, weight: *const void) -> icudaStatus_t
icudaBuiltinGraphRemoveNode(graph: *icudaGraph_t, node_id: i32) -> icudaStatus_t
icudaBuiltinGraphRemoveEdge(graph: *icudaGraph_t, from: i32, to: i32) -> icudaStatus_t
icudaBuiltinGraphBFS(graph: *const icudaGraph_t, start: i32, visited: *i32, n_visited: *i32) -> icudaStatus_t
icudaBuiltinGraphDFS(graph: *const icudaGraph_t, start: i32, visited: *i32, n_visited: *i32) -> icudaStatus_t
icudaBuiltinGraphShortestPath(qbasis: icudaQBasis_t, graph: *const icudaGraph_t, from: i32, to: i32, path: *i32, max_path: i32, path_len: *i32, distance: *void) -> icudaStatus_t
  Dijkstra with exact VDR weights. No floating point distance accumulation.
icudaBuiltinGraphTopologicalSort(graph: *const icudaGraph_t, sorted: *i32, n: *i32) -> icudaStatus_t
icudaBuiltinGraphConnectedComponents(graph: *const icudaGraph_t, components: *i32, n_components: *i32) -> icudaStatus_t
icudaBuiltinGraphCycleDetect(graph: *const icudaGraph_t, has_cycle: *bool) -> icudaStatus_t
icudaBuiltinGraphPageRankExact(qbasis: icudaQBasis_t, graph: *const icudaGraph_t, ranks: *void, n_iterations: i32) -> icudaStatus_t
  Exact PageRank as VDR fractions. Converges to exact steady state.
icudaBuiltinGraphMarkovSteady(qbasis: icudaQBasis_t, transition: *const void, steady: *void, n: i32) -> icudaStatus_t
  Exact Markov steady-state distribution.

// --- Remaining 339 builtins follow same pattern ---
// Integer/bit ops (21): int_add, int_sub, int_mul, int_div, int_mod,
//   int_abs, int_sign, int_min, int_max, int_clamp, int_pow,
//   int_factorial, int_choose, bit_and, bit_or, bit_xor, bit_not,
//   bit_shift_left, bit_shift_right, bit_popcount, bit_reverse
// Time (10): timestamp_now, timestamp_diff, timestamp_add, duration_*
// Identity (8): uuid_generate, hash_*, checksum_*
// Logic (11): and, or, not, xor, implies, iff, mux, demux, decode, encode, match
// Polynomial (8): poly_eval, poly_mul, poly_gcd, poly_lagrange, ...
// Finite field (3): gf_add, gf_mul, gf_inv
// Denominator management (5): reproject_qbasis, budget_check, ...
// Remaining categories per Appendix L.
```

---

## Module 23: icuda_profiling

Profiling and diagnostics. Simplified by absence of float complexity.

```
icudaProfileStart(profiler: *icudaProfiler_t) -> icudaStatus_t
icudaProfileStop(profiler: icudaProfiler_t) -> icudaStatus_t

icudaProfileGetKernelStats(profiler: icudaProfiler_t, kernel_id: i32, stats: *icudaKernelStats_t) -> icudaStatus_t
  Stats: elapsed_ns (i64), integer_ops (i64), memory_bytes_read (i64),
  memory_bytes_written (i64), warp_occupancy_percent (i32 — always near 100),
  kb_cache_hits (i64), kb_cache_misses (i64), remainder_overflows (i64).
  No float utilization metrics. No SFU utilization. No tensor-core-vs-cuda-core
  breakdown. One compute type.

icudaProfileGetSessionStats(session: icudaSession_t, stats: *icudaSessionStats_t) -> icudaStatus_t
  Stats: total_turns, total_facts_asserted, total_rules_fired,
  total_prolog_queries, total_kb_accesses, total_primitive_calls,
  total_grammar_renders, total_llm_tokens (from external LLM integration),
  total_command_tokens, auto_triage_percentage (exact VDR fraction).

icudaProfileVerifyDeterminism(kernel: *const void, args: **void, grid: icudaDim3_t, block: icudaDim3_t, n_runs: i32, identical: *bool) -> icudaStatus_t
  Runs kernel n_runs times, compares all outputs bit-by-bit.
  Expected: always identical=true. If false, hardware fault.
  This test is meaningful ONLY because integer arithmetic is deterministic.
  On float CUDA this test would always fail due to thread scheduling.
```

---

## Summary

**Total function count: ~580**

| Module | Functions | Replaces |
|--------|-----------|----------|
| core | 11 | CUDA Runtime init/device |
| memory | 10 | CUDA memory management |
| stream | 10 | CUDA streams/events |
| session | 10 | Nothing — new capability |
| launch | 5 | CUDA kernel launch |
| vdr_math | 17 | cuBLAS (~200+ functions) |
| attention | 3 | cuDNN attention (~50+ functions) |
| training | 10 | Custom training loops + AMP |
| kb | 14 | Nothing — new capability |
| kb_primitives | 30 | Nothing — new capability |
| prolog | 8 | Nothing — new capability |
| grammar | 7 | Nothing — new capability |
| runner | 8 | Nothing — new capability |
| safety | 6 | Guardrail frameworks |
| confidence | 5 | Nothing — new capability |
| distributed | 10 | NCCL (~100+ functions) |
| transform | 4 | cuFFT (~80+ functions) |
| linalg | 8 | cuSOLVER (~200+ functions) |
| stats | 8 | Custom code |
| numbertheory | 7 | Custom code |
| functional_remainder | 8 | SFU hardware |
| builtins | 448 | LLM token generation |
| profiling | 4 | Nsight (simplified) |

**What's gone:** ~3,400+ API functions from float precision variants, mixed-precision management, format conversion, NaN handling, loss scaling, Transformer Engine, TensorRT calibration, SFU scheduling.

**What's new:** ~90 functions across session/KB/Prolog/grammar/runner/safety/confidence that enable the architectural capabilities the paper describes — autonomous operation, persistent state, structural safety, exact provenance — none of which exist in any form in current CUDA.
