# VDRProlog Module & Function Specification

## Complete Implementation Reference

---

## Module 1: VDRProlog_core

Runtime lifecycle, device management, error handling.

```
VDRPrologInit(flags: u32) -> VDRPrologStatus_t
  First call. Initializes driver, enumerates devices, allocates host-side
  session table. No device memory touched yet. Idempotent — second call
  returns OK without work. Sets global init flag checked by all other calls.

VDRPrologDeviceGetCount(count: *i32) -> VDRPrologStatus_t
  Writes number of VDRProlog-capable devices. Filters to integer-native only
  if Phase 2+ hardware present, falls back to INT8-capable for Phase 1.

VDRPrologDeviceGet(device: *VDRPrologDevice_t, ordinal: i32) -> VDRPrologStatus_t
  Returns device handle by index. Validates ordinal against count.

VDRPrologDeviceGetProperties(props: *VDRPrologDeviceProps_t, device: VDRPrologDevice_t) -> VDRPrologStatus_t
  Populates: n_compute_units, max_q_basis (Q16/Q32/Q335), has_fru (bool),
  kb_cache_size_bytes, max_shared_mem_per_block, max_registers_per_block,
  max_concurrent_sessions, global_mem_bytes, mem_bandwidth_bytes_sec,
  clock_rate_hz, warp_size (always 32). No float fields.

VDRPrologDeviceSetCurrent(device: VDRPrologDevice_t) -> VDRPrologStatus_t
  Binds calling host thread to device. All subsequent calls target this device.

VDRPrologDeviceGetCurrent(device: *VDRPrologDevice_t) -> VDRPrologStatus_t
  Returns currently bound device for calling thread.

VDRPrologDeviceSynchronize() -> VDRPrologStatus_t
  Blocks until all kernels on all streams of current device complete.

VDRPrologDeviceReset() -> VDRPrologStatus_t
  Destroys all allocations, streams, sessions on current device. Returns
  device to post-init state. Active sessions are force-snapshotted first.

VDRPrologGetErrorString(status: VDRPrologStatus_t) -> *const u8
  Returns static string for error code. No allocation.

VDRPrologGetLastError() -> VDRPrologStatus_t
  Returns and clears last error on calling thread. Thread-local storage.

VDRPrologPeekLastError() -> VDRPrologStatus_t
  Returns last error without clearing.
```

### Error codes (VDRPrologStatus_t enum):

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

## Module 2: VDRProlog_memory

Device memory allocation, host-device transfer. All allocations are typed.

```
VDRPrologMalloc(ptr: **void, size_bytes: u64) -> VDRPrologStatus_t
  Allocates device global memory. Untyped — caller casts. For raw buffers
  and scratch space. Aligned to 256 bytes.

VDRPrologMallocTyped(ptr: **void, qbasis: VDRPrologQBasis_t, count: u64) -> VDRPrologStatus_t
  Allocates array of count VDR elements at declared qbasis. Compiler tracks
  qbasis tag on the pointer. Passing to mismatched-qbasis kernel = compile error.
  Element size derived from qbasis: Q16=8, Q32=16, Q335=240 bytes.

VDRPrologMallocKB(ptr: **VDRPrologKBStruct_t, count: u32) -> VDRPrologStatus_t
  Allocates contiguous array of KB structs. Fixed size per struct (paper's
  26-field layout). Count is max KBs this allocation holds. Zeroed on alloc.

VDRPrologFree(ptr: *void) -> VDRPrologStatus_t
  Frees device allocation. All three Malloc variants free through this.

VDRPrologMemcpy(dst: *void, src: *const void, size_bytes: u64, kind: VDRPrologMemcpyKind_t) -> VDRPrologStatus_t
  Synchronous copy. Kind: HostToDevice, DeviceToHost, DeviceToDevice.
  Bit-exact — integer data is identical after copy on every platform.

VDRPrologMemcpyAsync(dst: *void, src: *const void, size_bytes: u64, kind: VDRPrologMemcpyKind_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Asynchronous copy on stream. Completion visible after stream sync.

VDRPrologMemset(ptr: *void, value: i32, size_bytes: u64) -> VDRPrologStatus_t
  Sets bytes. Primarily for zeroing buffers.

VDRPrologMemGetInfo(free: *u64, total: *u64) -> VDRPrologStatus_t
  Reports device memory. Counts only — no fragmentation metrics needed
  because KB structs are fixed-size so fragmentation is minimal.

VDRPrologMallocHost(ptr: **void, size_bytes: u64) -> VDRPrologStatus_t
  Page-locked host memory for async transfer overlap.

VDRPrologFreeHost(ptr: *void) -> VDRPrologStatus_t
  Frees page-locked host allocation.

VDRPrologMemPrefetchAsync(ptr: *void, size_bytes: u64, device: VDRPrologDevice_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Hints unified memory migration. Used for KB preloading — prefetch
  KB subtree to device before kernel launch.
```

---

## Module 3: VDRProlog_stream

Execution streams and synchronization. Streams are session-aware.

```
VDRPrologStreamCreate(stream: *VDRPrologStream_t) -> VDRPrologStatus_t
  Creates default stream. No session binding — for non-session work
  (memory ops, diagnostics). Kernels on unbound streams cannot access KBs.

VDRPrologStreamCreateWithSession(stream: *VDRPrologStream_t, session: VDRPrologSession_t) -> VDRPrologStatus_t
  Creates stream bound to session. All kernels inherit session's kb_root_id,
  user_id, visibility_level. The hardware enforces access — not a software guard.
  KB queries on this stream only see KBs reachable from session scope.

VDRPrologStreamDestroy(stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Waits for pending work, then destroys. Does not destroy session.

VDRPrologStreamSynchronize(stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Blocks until all kernels on this stream complete.

VDRPrologStreamQuery(stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Non-blocking check. Returns OK if complete, ERR_STREAM_BUSY if not.

VDRPrologStreamWaitEvent(stream: VDRPrologStream_t, event: VDRPrologEvent_t) -> VDRPrologStatus_t
  Stream waits for event before executing subsequent kernels.
  Used for cross-stream dependencies (e.g., Prolog query depends on
  MAC kernel completing attention computation).

VDRPrologEventCreate(event: *VDRPrologEvent_t) -> VDRPrologStatus_t
  Creates event for timing and synchronization.

VDRPrologEventRecord(event: VDRPrologEvent_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Records event at current point in stream.

VDRPrologEventSynchronize(event: VDRPrologEvent_t) -> VDRPrologStatus_t
  Blocks until event completes.

VDRPrologEventElapsedTime(ms: *f32, start: VDRPrologEvent_t, end: VDRPrologEvent_t) -> VDRPrologStatus_t
  NOTE: the one place a float exists — host-side timing measurement.
  Could be integer nanoseconds instead. Implementation choice.

VDRPrologEventDestroy(event: VDRPrologEvent_t) -> VDRPrologStatus_t
  Frees event.
```

---

## Module 4: VDRProlog_session

Session lifecycle, snapshots, clones. The operational model from paper Section 4.6.

```
VDRPrologSessionCreate(session: *VDRPrologSession_t, config: *VDRPrologSessionConfig_t) -> VDRPrologStatus_t
  Config contains: kb_root_id (root of this session's KB tree), user_id (i32),
  visibility_level (enum: public/internal/owner_only), max_kb_count (u32),
  max_live_memory_bytes (u64), max_turns (u32, 0=unlimited).
  Allocates session state on device. Initializes all bounded data primitives
  to empty/min. Session is the unit of isolation.

VDRPrologSessionDestroy(session: VDRPrologSession_t) -> VDRPrologStatus_t
  Snapshots if auto_snapshot enabled, then frees all session device memory.
  Persistent KB facts survive in the global KB store. Live state is gone.

VDRPrologSessionGetInfo(session: VDRPrologSession_t, info: *VDRPrologSessionInfo_t) -> VDRPrologStatus_t
  Reports: current_turn, kb_count, live_memory_bytes, n_rules_fired,
  n_facts_asserted, n_prolog_queries. All i32/i64. No approximate values.

VDRPrologSessionSnapshot(session: VDRPrologSession_t, snapshot: *VDRPrologSnapshot_t) -> VDRPrologStatus_t
  Atomic capture of all session state: persistent KBs, live state (LRUs,
  counters, queues, stacks, ring buffers, bitsets), rule base, grammar cache.
  Snapshot is a device memory blob with a host-readable header (size, checksum,
  session config). Checksum is integer CRC — deterministic.
  The snapshot IS the factory. Bit-identical restore guaranteed.

VDRPrologSessionRestore(session: VDRPrologSession_t, snapshot: *VDRPrologSnapshot_t) -> VDRPrologStatus_t
  Overwrites all session state from snapshot. Validates checksum first.
  After restore, session is in exactly the state at snapshot time.
  "Exactly" means bit-identical because integers.

VDRPrologSessionClone(parent: VDRPrologSession_t, child: *VDRPrologSession_t, config: *VDRPrologCloneConfig_t) -> VDRPrologStatus_t
  Creates new session sharing parent's persistent KBs (read-through)
  with independent live state (initialized from parent's current live state,
  or from empty if config says fresh_live=true). Clone's writes to persistent
  KBs are copy-on-write — parent doesn't see them until explicit merge.
  Clone config: fresh_live (bool), inherit_rules (bool), max_turns (u32).

VDRPrologSessionMerge(parent: VDRPrologSession_t, child: VDRPrologSession_t, policy: VDRPrologMergePolicy_t) -> VDRPrologStatus_t
  Merges child's persistent KB changes back to parent. Policy: OURS (parent
  wins conflicts), THEIRS (child wins), FAIL_ON_CONFLICT. Conflict = same
  kb_id + slot_id modified by both. After merge, child can be destroyed.

VDRPrologSessionKill(session: VDRPrologSession_t) -> VDRPrologStatus_t
  Immediate termination. No snapshot. Live state gone. Persistent KBs
  that were copy-on-write are discarded. This is the drift-kill from the paper:
  clone drifted, kill it, reclone from snapshot.

VDRPrologSnapshotSave(snapshot: *VDRPrologSnapshot_t, path: *const u8) -> VDRPrologStatus_t
  Writes snapshot to host filesystem. The "deployable binary."
  Format: header + raw integer data. No float serialization.
  Portable across devices — integers are platform-independent.

VDRPrologSnapshotLoad(snapshot: *VDRPrologSnapshot_t, path: *const u8) -> VDRPrologStatus_t
  Reads snapshot from host filesystem. Validates header and checksum.
  Bit-identical to what was saved. Always, on every platform.
```

---

## Module 5: VDRProlog_launch

Kernel launch configuration and execution.

```
VDRPrologLaunchKernel(kernel: *const void, grid: VDRPrologDim3_t, block: VDRPrologDim3_t, args: **void, shared_mem: u64, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Standard kernel launch. Grid/block dimensions as dim3 (x,y,z integer).
  Shared_mem is additional shared memory beyond static declarations.
  If stream is session-bound, kernel inherits session credentials.

VDRPrologLaunchMACKernel(kernel: *const void, grid: VDRPrologDim3_t, block: VDRPrologDim3_t, args: **void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Hint to scheduler: this kernel is pure MAC. Scheduler allocates maximum
  integer ALUs, maximum memory bandwidth, minimum shared memory.
  No functional difference from LaunchKernel — just scheduling priority.

VDRPrologLaunchPrologKernel(kernel: *const void, grid: VDRPrologDim3_t, block: VDRPrologDim3_t, args: **void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Hint to scheduler: this kernel does KB-heavy work. Scheduler allocates
  maximum shared memory for KB cache, moderate ALU, moderate bandwidth.

VDRPrologLaunchPrimKernel(kernel: *const void, grid: VDRPrologDim3_t, block: VDRPrologDim3_t, args: **void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Hint to scheduler: lightweight primitive. Minimum resource allocation,
  fastest dispatch latency.

VDRPrologOccupancyMaxPotentialBlockSize(min_grid: *i32, block_size: *i32, kernel: *const void, shared_mem_per_block: u64, max_block_size: i32) -> VDRPrologStatus_t
  Calculates optimal launch config. Simpler than CUDA equivalent because
  no divergence means occupancy is almost always near-maximum.
  The primary constraint is shared memory for KB cache, not warp scheduling.
```

---

## Module 6: VDRProlog_vdr_math

Core VDR arithmetic operations on device arrays. Replaces cuBLAS, cuDNN math.

```
VDRPrologVdrGemm(qbasis: VDRPrologQBasis_t, transa: VDRPrologOp_t, transb: VDRPrologOp_t, m: i32, n: i32, k: i32, alpha: *const void, A: *const void, lda: i32, B: *const void, ldb: i32, beta: *const void, C: *void, ldc: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  General matrix multiply: C = alpha*op(A)*op(B) + beta*C.
  Alpha, beta are VDR scalars at declared qbasis. All elements same qbasis.
  Dispatches to integer MMA tiles internally. Result is exact — no
  accumulation error regardless of matrix size.
  Op: NO_TRANS, TRANS. No conjugate-transpose (no complex floats).

VDRPrologVdrGemmBatched(qbasis: VDRPrologQBasis_t, transa: VDRPrologOp_t, transb: VDRPrologOp_t, m: i32, n: i32, k: i32, alpha: *const void, A_array: **const void, lda: i32, B_array: **const void, ldb: i32, beta: *const void, C_array: **void, ldc: i32, batch_count: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Batched GEMM for multi-head attention. batch_count = n_heads.
  Each batch is independent — trivially parallel across SMs.

VDRPrologVdrGemmStridedBatched(qbasis: VDRPrologQBasis_t, transa: VDRPrologOp_t, transb: VDRPrologOp_t, m: i32, n: i32, k: i32, alpha: *const void, A: *const void, lda: i32, stride_a: i64, B: *const void, ldb: i32, stride_b: i64, beta: *const void, C: *void, ldc: i32, stride_c: i64, batch_count: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Strided variant — contiguous memory, stride between batches.
  Preferred for attention where Q,K,V are packed sequentially per head.

VDRPrologVdrSoftmax(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Quadratic surrogate: shift inputs so min=0, square each, divide by sum.
  Output sum = D exactly. Every call. Guaranteed by construction.
  No exp, no SFU, no data-dependent divergence.

VDRPrologVdrExpSoftmax(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, n: i32, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact exp-softmax via FRU recurrence. Depth bounds the iteration count.
  Returns ERR_FRU_NOT_AVAILABLE on Phase 1 hardware.
  Output sum = D exactly at sufficient depth. Depth insufficient = remainder
  in last R slot tells you how far off.

VDRPrologVdrLayerNorm(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, gamma: *const void, beta: *const void, n: i32, eps_unused: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Integer layer normalization. Mean and variance computed exactly.
  eps_unused is placeholder for API compat — always ignored because
  integer variance is never zero unless all inputs identical, which is
  detectable by exact comparison, not epsilon.

VDRPrologVdrAdd(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Elementwise add. Same D — straight integer add on V, handle R carry.

VDRPrologVdrSub(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Elementwise subtract.

VDRPrologVdrMul(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Elementwise multiply. Widening mul, shift, remainder extraction.

VDRPrologVdrDiv(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Elementwise divide. a * reciprocal(b). Reciprocal is D²/b_v with
  remainder tracking. Active division caveat from paper Section 15 applies
  if b has nonzero remainder — scalar projection, logged.

VDRPrologVdrDot(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, result: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Dot product. Widening MAC across n elements. Single VDR scalar result.

VDRPrologVdrScale(qbasis: VDRPrologQBasis_t, input: *const void, scalar: *const void, output: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Multiply every element by scalar. Used for learning rate application.

VDRPrologVdrCompare(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, result: *i32, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Elementwise cross-multiply comparison. Result array: -1, 0, +1.
  Exact — no tolerance, no epsilon. Equal means equal.

VDRPrologVdrReproject(src_qbasis: VDRPrologQBasis_t, dst_qbasis: VDRPrologQBasis_t, input: *const void, output: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Change Q-basis. Exact when dst_D is multiple of src_D. Remainder-tracked
  otherwise. This is the only operation that changes D.

VDRPrologVdrNormalize(qbasis: VDRPrologQBasis_t, data: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Compact remainders: if R0 >= D, roll into V. Reduces remainder depth.
  In-place. Idempotent — calling twice gives same result as once.

VDRPrologVdrRemainderMagnitude(qbasis: VDRPrologQBasis_t, data: *const void, magnitudes: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Reports magnitude of remainder per element. For monitoring precision
  budget. If all magnitudes are zero, computation was exact at depth 0.
```

---

## Module 7: VDRProlog_attention

Fused attention kernels. The hot path for LLM inference and training.

```
VDRPrologAttentionForward(config: *VDRPrologAttentionConfig_t, Q: *const void, K: *const void, V: *const void, output: *void, attn_weights: *void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Config: qbasis, seq_len, d_model, n_heads, d_head, causal_mask (bool),
  softmax_type (QUADRATIC or EXP_FRU), fru_depth (if EXP_FRU).
  Fused: QK^T matmul → scale → mask → softmax → AV matmul.
  attn_weights output optional (NULL to skip). When written, every row
  sums to D exactly. Verifiable by caller.
  Causal mask is integer comparison: if col > row, weight = 0. Not
  approximate masking — exact zero.

VDRPrologAttentionBackward(config: *VDRPrologAttentionConfig_t, grad_output: *const void, Q: *const void, K: *const void, V: *const void, attn_weights: *const void, grad_Q: *void, grad_K: *void, grad_V: *void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact gradients via reverse-mode autodiff on the fused attention graph.
  Chain rule and quotient rule are exact in VDR. No gradient clipping
  needed — integer gradients don't explode from accumulation.

VDRPrologAttentionVerifySoftmaxSum(attn_weights: *const void, qbasis: VDRPrologQBasis_t, seq_len: i32, n_heads: i32, violations: *i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Checks every softmax row sums to D. Writes count of violations.
  Expected: always 0. If nonzero, something is broken — not drifted, broken.
  This check is free in production because it's integer equality,
  not tolerance comparison.
```

---

## Module 8: VDRProlog_training

Training loop primitives. SGD, gradient computation, checkpoint.

```
VDRPrologTrainSGDUpdate(qbasis: VDRPrologQBasis_t, params: *void, grads: *const void, lr: *const void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  params -= lr * grads. Exact. LR is a VDR scalar (e.g., 1/1000 at Q16
  is V=65, D=65536 — exact representation of ~0.001). Update is exact
  multiply and exact subtract. No momentum, no Adam — those are separate
  functions below. This is raw SGD.

VDRPrologTrainSGDMomentumUpdate(qbasis: VDRPrologQBasis_t, params: *void, grads: *const void, velocity: *void, lr: *const void, momentum: *const void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  velocity = momentum * velocity + grads. params -= lr * velocity.
  Both operations exact.

VDRPrologTrainAdamUpdate(qbasis: VDRPrologQBasis_t, params: *void, grads: *const void, m: *void, v_adam: *void, lr: *const void, beta1: *const void, beta2: *const void, step: i32, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Adam optimizer in exact integer arithmetic. m and v_adam are first/second
  moment estimates. Bias correction uses exact integer division.
  No epsilon in denominator — if second moment is zero, the gradient
  was zero and the update is zero. Detectable exactly.

VDRPrologTrainComputeLoss(qbasis: VDRPrologQBasis_t, logits: *const void, targets: *const i32, loss: *void, n_classes: i32, batch_size: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Cross-entropy loss. Uses fn_log builtin for exact logarithm via FRU
  when available, rational approximation otherwise. Loss is a single
  VDR scalar. Monotonic decrease observable as integer comparison
  between epochs — the toy data confirms this works.

VDRPrologTrainBackwardPass(graph: *VDRPrologComputeGraph_t, loss: *const void, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Reverse-mode autodiff over recorded compute graph. Every node stores
  exact forward values. Chain rule produces exact partial derivatives.
  Quotient rule for softmax backprop is exact. No gradient clipping
  because exact gradients don't diverge from accumulation error.

VDRPrologTrainCheckpointSave(params: *const void, optimizer_state: *const void, qbasis: VDRPrologQBasis_t, n_params: i64, path: *const u8, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Writes all parameters and optimizer state as raw integers.
  Checkpoint is bit-identical across saves, loads, platforms.
  No precision loss on save. No precision loss on restore. Ever.

VDRPrologTrainCheckpointLoad(params: *void, optimizer_state: *void, qbasis: VDRPrologQBasis_t, n_params: i64, path: *const u8, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Restores from checkpoint. Bit-identical to state at save time.

VDRPrologTrainComputeGraphCreate(graph: *VDRPrologComputeGraph_t) -> VDRPrologStatus_t
  Creates empty compute graph for recording forward pass operations.
  Used by backward pass to trace exact gradients.

VDRPrologTrainComputeGraphDestroy(graph: VDRPrologComputeGraph_t) -> VDRPrologStatus_t
  Frees graph. Forward values freed with it.

VDRPrologTrainComputeGraphRecord(graph: VDRPrologComputeGraph_t, enabled: bool) -> VDRPrologStatus_t
  Toggles recording. When enabled, all VDRPrologVdr* calls on the active
  stream append nodes to the graph with exact intermediate values.
```

---

## Module 9: VDRProlog_kb

Knowledge Base operations. The data layer from paper Sections 4.1, 4.6.

```
VDRPrologKBCreate(kb_store: *VDRPrologKBStore_t, kb_id: *i32, config: *VDRPrologKBConfig_t) -> VDRPrologStatus_t
  Config: name (text), parent_id (i32, -1 for root), visibility (enum),
  owner (text), max_facts (u32), max_rules (u32), max_children (u32).
  Allocates fixed-size KB struct in kb_store. Returns assigned kb_id
  (sequential integer). Initializes all live fields to empty/zero.
  Adds kb_id to parent's children_ids list.

VDRPrologKBDestroy(kb_store: *VDRPrologKBStore_t, kb_id: i32) -> VDRPrologStatus_t
  Removes KB. Reparents children to destroyed KB's parent.
  Persistent facts are gone. This is permanent deletion, not reset.

VDRPrologKBReset(kb_store: *VDRPrologKBStore_t, kb_id: i32) -> VDRPrologStatus_t
  Clears all live state: LRUs, counters, queues, stacks, ring buffers,
  bitsets, working data. Persistent fields (facts, rules, constraints,
  connections, grammars) untouched. This is the "kill drift" operation.

VDRPrologKBFreeze(kb_store: *VDRPrologKBStore_t, kb_id: i32) -> VDRPrologStatus_t
  Sets frozen=true. No further modifications to persistent fields.
  Live fields still writable (they're session-scoped).
  Frozen KBs are safe to share across clones without COW.

VDRPrologKBUnfreeze(kb_store: *VDRPrologKBStore_t, kb_id: i32) -> VDRPrologStatus_t
  Clears frozen flag. Requires owner match on session user_id.

VDRPrologKBGetInfo(kb_store: *VDRPrologKBStore_t, kb_id: i32, info: *VDRPrologKBInfo_t) -> VDRPrologStatus_t
  Reads: name, path, id, parent_id, n_children, n_facts, n_rules,
  visibility, frozen, owner, created_at, last_modified. All integers/enums.

VDRPrologKBResolvePath(kb_store: *VDRPrologKBStore_t, path: *const u8, kb_id: *i32) -> VDRPrologStatus_t
  Dotted path string → integer kb_id via hash map lookup. One-time cost.
  All subsequent operations use the integer directly.

VDRPrologKBFactAssert(kb_store: *VDRPrologKBStore_t, kb_id: i32, slot_id: i32, fact: *const VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Writes fact at kb_id + slot_id. Fact struct: tag (i32 enum), value (VDR),
  provenance (source_kb_id, source_slot_id, confidence VDR, timestamp i32).
  Checks: session visibility, frozen flag, slot bounds. Integer checks, all.
  Side effect: updates last_modified timestamp.

VDRPrologKBFactQuery(kb_store: *VDRPrologKBStore_t, kb_id: i32, slot_id: i32, fact: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Reads fact at kb_id + slot_id. O(1) — two integer indices.
  Checks session visibility via ancestor walk (integer comparisons up
  the parent chain). If KB not visible from session scope, returns
  ERR_KB_ACCESS_DENIED. The fact is never exposed — not redacted, absent.

VDRPrologKBFactRetract(kb_store: *VDRPrologKBStore_t, kb_id: i32, slot_id: i32) -> VDRPrologStatus_t
  Removes fact. Slot becomes empty. Provenance of retraction logged
  as separate audit fact if audit KB configured.

VDRPrologKBFactSearch(kb_store: *VDRPrologKBStore_t, kb_id: i32, tag: i32, results: *VDRPrologVdrFact_t, max_results: i32, n_found: *i32) -> VDRPrologStatus_t
  Linear scan of facts in kb_id matching tag. Returns up to max_results.
  Scoped — only searches this KB, not ancestors (use ScopedSearch for walk).

VDRPrologKBFactScopedSearch(kb_store: *VDRPrologKBStore_t, start_kb_id: i32, tag: i32, results: *VDRPrologVdrFact_t, max_results: i32, n_found: *i32) -> VDRPrologStatus_t
  Walks from start_kb_id up parent chain to root. Returns first match(es).
  This is lexical scoping — "bank" resolves differently depending on
  which KB you start from.

VDRPrologKBChildList(kb_store: *VDRPrologKBStore_t, kb_id: i32, children: *i32, max_children: i32, n_children: *i32) -> VDRPrologStatus_t
  Lists child kb_ids. Integer array.

VDRPrologKBMount(kb_store: *VDRPrologKBStore_t, kb_id: i32, mount_target_id: i32, mount_name: *const u8) -> VDRPrologStatus_t
  Cross-branch reference. Makes mount_target accessible as if it were
  a child of kb_id, without changing the tree structure. Used for
  shared resources (e.g., mount a common grammar KB into multiple scopes).

VDRPrologKBUnmount(kb_store: *VDRPrologKBStore_t, kb_id: i32, mount_name: *const u8) -> VDRPrologStatus_t
  Removes mount point.
```

---

## Module 10: VDRProlog_kb_primitives

Bounded data primitives within KBs. The working memory layer.

```
// --- LRU Cache ---

VDRPrologLRUCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> VDRPrologStatus_t
  Creates named LRU in kb_id's live state. Capacity fixed forever.
  1 <= capacity <= 1000.

VDRPrologLRUGet(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, key: i32, value: *VDRPrologVdrFact_t, found: *bool) -> VDRPrologStatus_t
  Lookup by integer key. Promotes to most-recent on hit. O(1).

VDRPrologLRUPut(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, key: i32, value: *const VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Insert or update. If at capacity, evicts oldest entry. Cannot exceed capacity.

VDRPrologLRUEvictOldest(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Manual eviction. Returns the evicted entry for inspection if needed.

VDRPrologLRUSize(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> VDRPrologStatus_t
  Current entry count. Always <= capacity.

VDRPrologLRUClear(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Empties cache. Capacity unchanged.

// --- Counter ---

VDRPrologCounterCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, min_val: i32, max_val: i32, initial: i32) -> VDRPrologStatus_t
  Bounded integer counter. Clamps at min/max — never wraps, never overflows.

VDRPrologCounterGet(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *i32) -> VDRPrologStatus_t
  Reads current value.

VDRPrologCounterIncrement(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, amount: i32) -> VDRPrologStatus_t
  Adds amount (can be negative for decrement). Clamps at bounds.
  Side effect: if clamped, sets internal clamped flag queryable.

VDRPrologCounterReset(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Sets to initial value.

VDRPrologCounterAtBound(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, at_min: *bool, at_max: *bool) -> VDRPrologStatus_t
  Checks if counter is at either bound.

// --- Lock ---

VDRPrologLockCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Non-blocking coordination signal. Not a mutex — no blocking.

VDRPrologLockAcquire(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, acquired: *bool) -> VDRPrologStatus_t
  Attempts to acquire. Returns immediately with acquired=true or false.

VDRPrologLockRelease(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Releases. Error if not held.

VDRPrologLockQuery(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, held: *bool) -> VDRPrologStatus_t
  Check without acquiring.

// --- Queue (FIFO) ---

VDRPrologQueueCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> VDRPrologStatus_t
  Bounded FIFO. 1 <= capacity <= 1000.

VDRPrologQueuePush(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *const VDRPrologVdrFact_t, pushed: *bool) -> VDRPrologStatus_t
  Enqueue. If full, pushed=false. Queue does not grow.

VDRPrologQueuePop(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *VDRPrologVdrFact_t, popped: *bool) -> VDRPrologStatus_t
  Dequeue oldest. If empty, popped=false.

VDRPrologQueuePeek(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *VDRPrologVdrFact_t, found: *bool) -> VDRPrologStatus_t
  Read oldest without removing.

VDRPrologQueueSize(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> VDRPrologStatus_t
  Current count.

VDRPrologQueueClear(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
  Empty the queue.

// --- Stack (LIFO) ---

VDRPrologStackCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> VDRPrologStatus_t
  Bounded LIFO. 1 <= capacity <= 1000.

VDRPrologStackPush(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *const VDRPrologVdrFact_t, pushed: *bool) -> VDRPrologStatus_t
  Push. If full, pushed=false.

VDRPrologStackPop(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *VDRPrologVdrFact_t, popped: *bool) -> VDRPrologStatus_t
  Pop top. If empty, popped=false.

VDRPrologStackPeek(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *VDRPrologVdrFact_t, found: *bool) -> VDRPrologStatus_t
  Read top without removing.

VDRPrologStackSize(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> VDRPrologStatus_t
VDRPrologStackClear(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t

// --- Ring Buffer ---

VDRPrologRingCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, capacity: i32) -> VDRPrologStatus_t
  Fixed-size sliding window. Oldest overwritten when full.

VDRPrologRingWrite(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, value: *const VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Always succeeds. If full, overwrites oldest. No pushed flag needed.

VDRPrologRingRead(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, index: i32, value: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Read by index relative to oldest (0 = oldest current, size-1 = newest).

VDRPrologRingSize(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, size: *i32) -> VDRPrologStatus_t
VDRPrologRingClear(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t

// --- Bitset ---

VDRPrologBitsetCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, n_bits: i32) -> VDRPrologStatus_t
  Fixed size. 1 <= n_bits <= 10000. Initialized all-clear.

VDRPrologBitsetSet(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, bit: i32) -> VDRPrologStatus_t
VDRPrologBitsetClear(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, bit: i32) -> VDRPrologStatus_t
VDRPrologBitsetGet(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, bit: i32, set: *bool) -> VDRPrologStatus_t
VDRPrologBitsetPopcount(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8, count: *i32) -> VDRPrologStatus_t
  Number of set bits. For tracking completion percentage as exact fraction:
  popcount / n_bits.
VDRPrologBitsetClearAll(kb_store: *VDRPrologKBStore_t, kb_id: i32, name: *const u8) -> VDRPrologStatus_t
```

---

## Module 11: VDRProlog_prolog

Prolog engine on GPU. Parallel unification over fact tables.

```
VDRPrologPrologRuleAssert(kb_store: *VDRPrologKBStore_t, kb_id: i32, rule: *const VDRPrologPrologRule_t) -> VDRPrologStatus_t
  Adds rule to KB's rule set. Rule struct: head (term), body (array of
  term conditions), action (array of term assertions/retractions).
  Terms are typed: atom (i32 tag), variable (i32 binding slot), vdr_value,
  list, compound (functor + args). All integer representations.
  Side effect: rule is persistent — survives reset, participates in snapshots.

VDRPrologPrologRuleRetract(kb_store: *VDRPrologKBStore_t, kb_id: i32, rule_id: i32) -> VDRPrologStatus_t
  Removes rule by ID.

VDRPrologPrologQuery(kb_store: *VDRPrologKBStore_t, start_kb_id: i32, query: *const VDRPrologPrologTerm_t, bindings: *VDRPrologPrologBindings_t, max_results: i32, n_results: *i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Depth-first search with backtracking, depth limit 100.
  Scoped: starts at start_kb_id, walks ancestors.
  Unification: cross-multiply comparison on VDR values. Exact.
  Parallelized: candidate facts loaded into shared memory, cross-multiply
  comparisons distributed across warps. Filter, collect.
  Bindings: array of variable→value pairs for each result.

VDRPrologPrologFireAll(kb_store: *VDRPrologKBStore_t, kb_id: i32, fired: *VDRPrologPrologFired_t, max_fired: i32, n_fired: *i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Evaluates all rules in kb_id against current fact state. Returns list
  of rules that fired and their resulting assertions/retractions.
  Does NOT apply the results — caller decides whether to commit.
  This is the L3 auto-fire mechanism: call this on a schedule,
  commit the results, zero LLM tokens.

VDRPrologPrologFireAndCommit(kb_store: *VDRPrologKBStore_t, kb_id: i32, n_fired: *i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  FireAll + automatically commit results (assert new facts, retract matched).
  For polling runners where human review isn't needed.
  Side effect: KB facts modified.

VDRPrologPrologUnify(a: *const VDRPrologPrologTerm_t, b: *const VDRPrologPrologTerm_t, bindings: *VDRPrologPrologBindings_t, unified: *bool) -> VDRPrologStatus_t
  Low-level single unification. Device-callable for custom kernels.
  Compares terms structurally. VDR values compared by cross-multiply.

VDRPrologPrologRuleStats(kb_store: *VDRPrologKBStore_t, kb_id: i32, rule_id: i32, stats: *VDRPrologPrologRuleStats_t) -> VDRPrologStatus_t
  Returns: fire_count, last_fired_timestamp, success_rate_numerator,
  success_rate_denominator. For hygiene: stale = not fired in 90 days,
  failing = success_rate < 20/100.

VDRPrologPrologHygiene(kb_store: *VDRPrologKBStore_t, kb_id: i32, stale_days: i32, min_success_rate_num: i32, min_success_rate_den: i32, candidates: *i32, max_candidates: i32, n_candidates: *i32) -> VDRPrologStatus_t
  Identifies rules that are stale, failing, or orphaned (reference
  retracted facts). Returns rule_ids for review/pruning. Does not
  auto-delete — returns candidates for caller decision.
```

---

## Module 12: VDRProlog_grammar

Grammar-directed structural token generation.

```
VDRPrologGrammarCreate(grammar: *VDRPrologGrammar_t, template: *const u8, template_len: i32) -> VDRPrologStatus_t
  Parses template string with typed slot markers: {slot_name:type}.
  Types: vdr_value, text, integer, enum(val1|val2|val3).
  Template is the structural frame — every byte outside {} is literal.
  Validation: template must be syntactically valid with all slots filled
  by any valid value of declared type.

VDRPrologGrammarDestroy(grammar: VDRPrologGrammar_t) -> VDRPrologStatus_t
  Frees grammar.

VDRPrologGrammarStoreInKB(kb_store: *VDRPrologKBStore_t, kb_id: i32, grammar_slot: i32, grammar: VDRPrologGrammar_t) -> VDRPrologStatus_t
  Persists grammar in KB. Survives reset, participates in snapshots.
  Inherited by children KBs through tree walk.

VDRPrologGrammarLoadFromKB(kb_store: *VDRPrologKBStore_t, kb_id: i32, grammar_slot: i32, grammar: *VDRPrologGrammar_t) -> VDRPrologStatus_t
  Loads grammar from KB. Walks ancestors if not found in target KB.

VDRPrologGrammarRender(grammar: VDRPrologGrammar_t, fills: *const VDRPrologGrammarFill_t, n_fills: i32, output: *u8, output_capacity: i32, output_len: *i32) -> VDRPrologStatus_t
  Fills slots with provided values, produces output bytes.
  Every structural byte comes from the template — deterministic, 100% correct.
  Fills are validated against declared slot types. Type mismatch = error,
  not silent coercion.
  LLM contribution: the fill values. Grammar contribution: everything else.

VDRPrologGrammarRenderFromKB(grammar: VDRPrologGrammar_t, kb_store: *VDRPrologKBStore_t, slot_kb_mappings: *const VDRPrologGrammarKBMapping_t, n_mappings: i32, output: *u8, output_capacity: i32, output_len: *i32) -> VDRPrologStatus_t
  Fills slots directly from KB facts. Mapping: slot_name → kb_id + slot_id.
  Data goes from KB to output without entering any token stream.

VDRPrologGrammarValidate(grammar: VDRPrologGrammar_t, valid: *bool, error_msg: *u8, error_msg_capacity: i32) -> VDRPrologStatus_t
  Checks template is structurally valid. Run at creation time.
  If valid=true, every possible rendering is syntactically correct by construction.

VDRPrologGrammarListSlots(grammar: VDRPrologGrammar_t, slots: *VDRPrologGrammarSlotInfo_t, max_slots: i32, n_slots: *i32) -> VDRPrologStatus_t
  Enumerates slots with their names and types. For tooling and introspection.

VDRPrologGrammarCompose(outer: VDRPrologGrammar_t, inner: VDRPrologGrammar_t, slot_name: *const u8, composed: *VDRPrologGrammar_t) -> VDRPrologStatus_t
  Nests inner grammar into a slot of outer. For building complex output
  from simple templates. Composed grammar inherits validity from both.
```

---

## Module 13: VDRProlog_runner

Autonomous execution loops. The daemon layer.

```
VDRPrologRunnerCreatePoller(runner: *VDRPrologRunner_t, config: *VDRPrologPollerConfig_t) -> VDRPrologStatus_t
  Config: interval_ms (i32), session (VDRPrologSession_t),
  poll_fn (callback: session → status), max_consecutive_errors (i32).
  Spawns host thread that calls poll_fn every interval_ms.
  Each invocation gets a fresh LLM context (no attention degradation).
  poll_fn checks queues, evaluates counters, fires rules.

VDRPrologRunnerCreateProcessor(runner: *VDRPrologRunner_t, config: *VDRPrologProcessorConfig_t) -> VDRPrologStatus_t
  Config: session, source_type (enum: PROMETHEUS, DEPLOY_API, ALERT_STREAM,
  CUSTOM), connection_params (opaque bytes), ingest_fn (callback: data → status),
  max_turns_before_recycle (i32, default 200).
  Maintains persistent connection to external source. Calls ingest_fn on
  each incoming data item to compact into KB facts. At max_turns: snapshot
  connection state, kill, reclone, restore connection. Continuous data,
  always-fresh LLM.

VDRPrologRunnerCreateInternal(runner: *VDRPrologRunner_t, config: *VDRPrologInternalConfig_t) -> VDRPrologStatus_t
  Config: session, interval_ms, compute_fn (callback: session → status).
  Scheduled internal computation. Derives facts: rolling averages as
  exact fractions, trend directions as exact comparisons, coverage gaps.
  No external connections.

VDRPrologRunnerCreateBatch(runner: *VDRPrologRunner_t, config: *VDRPrologBatchConfig_t) -> VDRPrologStatus_t
  Config: session, task_queue_kb_id (i32), task_queue_name (text),
  process_fn (callback: task → status), max_concurrent (i32).
  Pulls tasks from KB queue, processes each with fresh session clone.
  Clone-per-task isolation. Results written to parent session KB.

VDRPrologRunnerStart(runner: VDRPrologRunner_t) -> VDRPrologStatus_t
  Begins execution loop. Non-blocking — returns immediately.

VDRPrologRunnerStop(runner: VDRPrologRunner_t) -> VDRPrologStatus_t
  Signals stop. Current iteration completes. Blocks until stopped.

VDRPrologRunnerKill(runner: VDRPrologRunner_t) -> VDRPrologStatus_t
  Immediate termination. No cleanup. For drift-kill scenarios.

VDRPrologRunnerGetStatus(runner: VDRPrologRunner_t, status: *VDRPrologRunnerStatus_t) -> VDRPrologStatus_t
  Reports: state (RUNNING/STOPPED/ERROR), iterations_completed,
  errors_consecutive, last_iteration_ms, session_turn_count.

VDRPrologRunnerRecycle(runner: VDRPrologRunner_t) -> VDRPrologStatus_t
  Manual recycle: snapshot session, kill, reclone from snapshot.
  Resets turn count. Drift dies. Knowledge persists.

VDRPrologRunnerDestroy(runner: VDRPrologRunner_t) -> VDRPrologStatus_t
  Stop if running, destroy session if owned, free resources.
```

---

## Module 14: VDRProlog_safety

Structural access control. Integer comparisons, not behavioral guardrails.

```
VDRPrologSafetyCheckAccess(kb_store: *VDRPrologKBStore_t, session: VDRPrologSession_t, kb_id: i32, access: *bool) -> VDRPrologStatus_t
  The core check. Walks from kb_id up parent chain. At each ancestor:
  is ancestor visible from session's visibility_level? Is session's
  user_id in the authorized set? Two integer comparisons per ancestor.
  If any ancestor fails, access=false. KB is absent from session scope.
  This runs BEFORE any data is read — not a filter on results, a gate
  on access.

VDRPrologSafetyGrantCreate(kb_store: *VDRPrologKBStore_t, kb_id: i32, grant: *const VDRPrologGrant_t) -> VDRPrologStatus_t
  Grant struct: grant_class (enum: FILESYSTEM, COMPILE, EXECUTE, LINT,
  NETWORK, PROCESS), target_pattern (text), max_uses (i32, -1=unlimited),
  expires_at (i32 timestamp, 0=never), holder_user_id (i32).
  Stored as KB fact in the grant KB. Only admin-level sessions can create.

VDRPrologSafetyGrantCheck(kb_store: *VDRPrologKBStore_t, session: VDRPrologSession_t, grant_class: VDRPrologGrantClass_t, target: *const u8, granted: *bool) -> VDRPrologStatus_t
  Checks if session's user_id holds an active grant matching class+target.
  Active = not expired AND uses_remaining > 0 AND not revoked.
  Integer comparisons throughout.
  Side effect: if granted, decrements uses_remaining.

VDRPrologSafetyGrantRevoke(kb_store: *VDRPrologKBStore_t, grant_id: i32) -> VDRPrologStatus_t
  Permanent revocation. Logged with timestamp and revoker user_id.
  No unrevoke. Create a new grant instead.

VDRPrologSafetyGrantList(kb_store: *VDRPrologKBStore_t, user_id: i32, grants: *VDRPrologGrant_t, max_grants: i32, n_grants: *i32) -> VDRPrologStatus_t
  Lists all grants for user_id. For audit.

VDRPrologSafetyAuditLog(kb_store: *VDRPrologKBStore_t, audit_kb_id: i32, entry: *const VDRPrologAuditEntry_t) -> VDRPrologStatus_t
  Writes audit entry: timestamp, user_id, action (enum), target_kb_id,
  target_slot_id, grant_used, result (allowed/denied). All integers.
  Append-only to audit KB's ring buffer.

VDRPrologSafetyAuditQuery(kb_store: *VDRPrologKBStore_t, audit_kb_id: i32, filter: *const VDRPrologAuditFilter_t, entries: *VDRPrologAuditEntry_t, max_entries: i32, n_entries: *i32) -> VDRPrologStatus_t
  Filter by user_id, time range, action type. Integer comparisons.
```

---

## Module 15: VDRProlog_confidence

Exact confidence propagation. Replaces hedging language.

```
VDRPrologConfidenceFromSource(source_type: VDRPrologSourceType_t, confidence: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Returns the declared confidence for a source type per the knowability
  spectrum (Appendix F): VDR_COMPUTATION=1/1, PROLOG_DERIVATION=1/1,
  DATABASE=98/100, PROMETHEUS=95/100, SCRIPT=95/100, REST_API=85/100,
  PUBLISHED=80/100, USER_STATED=70/100, WEB_SEARCH=50/100,
  LLM_GENERATED=30/100, UNKNOWN=0/1. All exact VDR fractions.

VDRPrologConfidenceCombineAgreeing(sources: *const VDRPrologVdrFact_t, n_sources: i32, combined: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Formula: 1 - product(1 - C_i). Exact VDR arithmetic.
  Two sources at 85/100 → 1 - (15/100 * 15/100) = 1 - 225/10000 = 9775/10000.
  Exact fraction, not 0.9775.

VDRPrologConfidenceCombineConflicting(sources: *const VDRPrologVdrFact_t, n_sources: i32, penalty: *const VDRPrologVdrFact_t, combined: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Agreeing formula with penalty multiplier applied per conflict.
  Penalty is configurable VDR fraction.

VDRPrologConfidenceChain(per_link: *const VDRPrologVdrFact_t, n_links: i32, chained: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Chain of N links: C^N. Exact VDR exponentiation.
  3 links at 85/100 → 614125/1000000. Exact.

VDRPrologConfidencePropagate(provenance: *const VDRPrologProvenance_t, result: *VDRPrologVdrFact_t) -> VDRPrologStatus_t
  Full propagation from provenance chain. Walks the derivation tree,
  applies combine/chain rules based on structure. Result is a single
  exact VDR fraction with full provenance traceable.
```

---

## Module 16: VDRProlog_distributed

Multi-GPU and multi-node communication. Replaces NCCL.

```
VDRPrologDistAllReduce(sendbuf: *const void, recvbuf: *void, count: i64, qbasis: VDRPrologQBasis_t, op: VDRPrologReduceOp_t, comm: VDRPrologComm_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Op: SUM, MAX, MIN. Integer operations. SUM is associative and commutative
  regardless of reduction order. Result is deterministic across all
  reduction topologies — ring, tree, butterfly, anything.
  This single property eliminates non-deterministic distributed training.

VDRPrologDistBroadcast(buf: *void, count: i64, root: i32, comm: VDRPrologComm_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Root sends, all receive. Bit-identical at all ranks.

VDRPrologDistAllGather(sendbuf: *const void, recvbuf: *void, sendcount: i64, comm: VDRPrologComm_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Each rank sends, all ranks receive concatenated result.

VDRPrologDistReduceScatter(sendbuf: *const void, recvbuf: *void, recvcount: i64, qbasis: VDRPrologQBasis_t, op: VDRPrologReduceOp_t, comm: VDRPrologComm_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Reduce + scatter. Each rank gets a chunk of the reduced result.

VDRPrologDistCommCreate(comm: *VDRPrologComm_t, n_ranks: i32, rank: i32) -> VDRPrologStatus_t
  Creates communicator. Standard MPI-like setup.

VDRPrologDistCommDestroy(comm: VDRPrologComm_t) -> VDRPrologStatus_t

VDRPrologDistCommGetRank(comm: VDRPrologComm_t, rank: *i32) -> VDRPrologStatus_t
VDRPrologDistCommGetSize(comm: VDRPrologComm_t, size: *i32) -> VDRPrologStatus_t

VDRPrologDistKBSync(kb_store: *VDRPrologKBStore_t, kb_id: i32, comm: VDRPrologComm_t, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Synchronizes KB facts across ranks. Deterministic merge — same
  facts at same slots produce same result regardless of arrival order
  because integer comparison resolves conflicts identically everywhere.

VDRPrologDistSnapshotBroadcast(snapshot: *VDRPrologSnapshot_t, root: i32, comm: VDRPrologComm_t) -> VDRPrologStatus_t
  Broadcast a session snapshot to all ranks. For distributed clone:
  all ranks start from bit-identical state.
```

---

## Module 17: VDRProlog_transform

Signal processing, DFT, convolution — all exact integer.

```
VDRPrologTransformDFT(qbasis: VDRPrologQBasis_t, input_real: *const void, input_imag: *const void, output_real: *void, output_imag: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact DFT. Twiddle factors are exact VDR fractions (rational
  approximations of roots of unity at declared precision).
  Roundtrip: DFT → IDFT returns original values exactly (paper Appendix H).
  Complex represented as real/imag pair, both VDR.

VDRPrologTransformIDFT(qbasis: VDRPrologQBasis_t, input_real: *const void, input_imag: *const void, output_real: *void, output_imag: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Inverse DFT. Exact roundtrip with DFT.

VDRPrologTransformConv1D(qbasis: VDRPrologQBasis_t, input: *const void, kernel: *const void, output: *void, input_len: i32, kernel_len: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  1D convolution via direct multiply-accumulate. Exact.

VDRPrologTransformConv2D(qbasis: VDRPrologQBasis_t, input: *const void, kernel: *const void, output: *void, in_h: i32, in_w: i32, k_h: i32, k_w: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  2D convolution. For image processing layers that use VDR.
```

---

## Module 18: VDRProlog_linalg

Linear algebra. Replaces cuSOLVER, cuSPARSE for VDR types.

```
VDRPrologLinalgMatVecMul(qbasis: VDRPrologQBasis_t, A: *const void, x: *const void, y: *void, m: i32, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  y = A*x. Exact integer MAC.

VDRPrologLinalgTranspose(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, m: i32, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Matrix transpose. Data movement only, no arithmetic — exact trivially.

VDRPrologLinalgGaussianElim(qbasis: VDRPrologQBasis_t, A: *void, b: *void, x: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Solve Ax=b. Gaussian elimination with exact VDR division.
  No pivoting heuristics for numerical stability — not needed because
  there's no numerical instability. Pivot for zero-avoidance only.

VDRPrologLinalgInverse(qbasis: VDRPrologQBasis_t, A: *const void, A_inv: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact matrix inverse. Works where float64 fails (Hilbert matrix,
  paper Appendix H). Via Gaussian elimination on [A|I].

VDRPrologLinalgDeterminant(qbasis: VDRPrologQBasis_t, A: *const void, det: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact determinant via elimination. Single VDR scalar result.

VDRPrologLinalgGramSchmidt(qbasis: VDRPrologQBasis_t, vectors: *const void, orthogonal: *void, n_vectors: i32, dim: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact orthogonalization. Dot products exact, projections exact,
  subtraction exact. No drift in the orthogonalized basis.

VDRPrologLinalgEigenvalues(qbasis: VDRPrologQBasis_t, A: *const void, eigenvalues_real: *void, eigenvalues_imag: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Eigenvalue computation. Real and imaginary parts as VDR.
  Iterative methods with exact convergence detection (equality, not tolerance).

VDRPrologLinalgSVD(qbasis: VDRPrologQBasis_t, A: *const void, U: *void, S: *void, Vt: *void, m: i32, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Singular value decomposition. Exact factors.
```

---

## Module 19: VDRProlog_stats

Statistics and probability. Exact fractions throughout.

```
VDRPrologStatsMean(qbasis: VDRPrologQBasis_t, data: *const void, result: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact mean: sum / n. Both exact.

VDRPrologStatsVariance(qbasis: VDRPrologQBasis_t, data: *const void, result: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact variance: sum((x_i - mean)^2) / n. All exact.

VDRPrologStatsMedian(qbasis: VDRPrologQBasis_t, data: *const void, result: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact median via integer sort.

VDRPrologStatsBayes(qbasis: VDRPrologQBasis_t, prior: *const void, likelihood: *const void, evidence: *const void, posterior: *void, n_hypotheses: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact Bayesian update: posterior = (prior * likelihood) / evidence.
  All VDR fractions. Posterior sums to exactly 1/1.

VDRPrologStatsNormalize(qbasis: VDRPrologQBasis_t, data: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Divides each element by sum so elements sum to D exactly.
  Same guarantee as softmax: exact normalization.

VDRPrologStatsHistogram(qbasis: VDRPrologQBasis_t, data: *const void, bins: *const void, counts: *i32, n_data: i32, n_bins: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact bin assignment via integer comparison. No bin-boundary ambiguity.

VDRPrologStatsCorrelation(qbasis: VDRPrologQBasis_t, x: *const void, y: *const void, result: *void, n: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact Pearson correlation as VDR fraction.
```

---

## Module 20: VDRProlog_numbertheory

Number theory primitives from paper Appendix L.

```
VDRPrologNTGCD(a: *const void, b: *const void, result: *void, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
  Euclidean GCD. Exact.

VDRPrologNTLCM(a: *const void, b: *const void, result: *void, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
VDRPrologNTModPow(base: *const void, exp: *const void, modulus: *const void, result: *void, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
  Modular exponentiation. For cryptographic operations.

VDRPrologNTCRT(remainders: *const void, moduli: *const void, result: *void, n: i32, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
  Chinese Remainder Theorem.

VDRPrologNTEulerTotient(n: *const void, result: *void, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
VDRPrologNTIsPrime(n: *const void, result: *bool, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
  Deterministic primality for bounded inputs.

VDRPrologNTFactorize(n: *const void, factors: *void, max_factors: i32, n_factors: *i32, qbasis: VDRPrologQBasis_t) -> VDRPrologStatus_t
  Trial division up to sqrt(n). For bounded inputs.
```

---

## Module 21: VDRProlog_functional_remainder

FRU operations for transcendental computation.

```
VDRPrologFRUSqrt(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact sqrt via Newton recurrence to declared depth. Remainder carries
  the residual. Depth 4-6 typically sufficient for Q335.

VDRPrologFRUExp(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact exp via Taylor/Padé recurrence. Range-reduced first.

VDRPrologFRULog(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Exact log via recurrence.

VDRPrologFRUSin(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
VDRPrologFRUCos(qbasis: VDRPrologQBasis_t, input: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t

VDRPrologFRUAtan2(qbasis: VDRPrologQBasis_t, y: *const void, x: *const void, output: *void, depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t

VDRPrologFRUResolve(qbasis: VDRPrologQBasis_t, data: *void, n: i32, target_depth: i32, stream: VDRPrologStream_t) -> VDRPrologStatus_t
  Batch remainder resolution. Takes array of VDR values, resolves
  remainders to target_depth via FRU recurrence. In-place.
  Used for continuous resolution in processor runners.

VDRPrologFRUAvailable(available: *bool) -> VDRPrologStatus_t
  Reports whether current device has FRU hardware. Phase 1: false.
  Phase 2: maybe. Phase 3: true. Callers fall back to software
  recurrence on host CPU when FRU unavailable.
```

---

## Module 22: VDRProlog_builtins

The 448 deterministic primitives, exposed as host-callable functions that dispatch to device kernels. Organized by paper Appendix L categories.

```
// --- Text (17 functions) ---
VDRPrologBuiltinTextReverse(input: *const u8, len: i32, output: *u8) -> VDRPrologStatus_t
VDRPrologBuiltinTextSplit(input: *const u8, len: i32, delimiter: u8, parts: *VDRPrologTextSlice_t, max_parts: i32, n_parts: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextContains(haystack: *const u8, h_len: i32, needle: *const u8, n_len: i32, found: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinTextReplace(input: *const u8, len: i32, old: *const u8, old_len: i32, new: *const u8, new_len: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextJoin(parts: *const VDRPrologTextSlice_t, n_parts: i32, separator: *const u8, sep_len: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextTrim(input: *const u8, len: i32, output: *u8, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextUpper(input: *u8, len: i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextLower(input: *u8, len: i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextStartsWith(input: *const u8, len: i32, prefix: *const u8, p_len: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinTextEndsWith(input: *const u8, len: i32, suffix: *const u8, s_len: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinTextIndexOf(haystack: *const u8, h_len: i32, needle: *const u8, n_len: i32, index: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextSubstring(input: *const u8, len: i32, start: i32, end: i32, output: *u8, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextRepeat(input: *const u8, len: i32, count: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTextPadLeft(input: *const u8, len: i32, width: i32, pad_char: u8, output: *u8) -> VDRPrologStatus_t
VDRPrologBuiltinTextPadRight(input: *const u8, len: i32, width: i32, pad_char: u8, output: *u8) -> VDRPrologStatus_t
VDRPrologBuiltinTextCharAt(input: *const u8, len: i32, index: i32, ch: *u8) -> VDRPrologStatus_t
VDRPrologBuiltinTextLength(input: *const u8, len: *i32) -> VDRPrologStatus_t

// --- Collections (36 functions) ---
VDRPrologBuiltinSort(qbasis: VDRPrologQBasis_t, data: *void, n: i32) -> VDRPrologStatus_t
  In-place integer comparison sort. O(n log n). Exact ordering — no
  tolerance ambiguity at sort boundaries.
VDRPrologBuiltinSortBy(qbasis: VDRPrologQBasis_t, data: *void, keys: *const void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinFilter(qbasis: VDRPrologQBasis_t, data: *const void, mask: *const bool, output: *void, n: i32, n_out: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinMap(qbasis: VDRPrologQBasis_t, data: *const void, op: VDRPrologUnaryOp_t, output: *void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinReduce(qbasis: VDRPrologQBasis_t, data: *const void, op: VDRPrologBinaryOp_t, initial: *const void, result: *void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinGroupBy(qbasis: VDRPrologQBasis_t, data: *const void, keys: *const void, groups: *VDRPrologGroup_t, n: i32, max_groups: i32, n_groups: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinFrequencies(qbasis: VDRPrologQBasis_t, data: *const void, values: *void, counts: *i32, n: i32, max_unique: i32, n_unique: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinDistinct(qbasis: VDRPrologQBasis_t, data: *const void, output: *void, n: i32, n_distinct: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinFlatten(data: **const void, lengths: *const i32, n_arrays: i32, output: *void, total: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinChunk(data: *const void, n: i32, chunk_size: i32, chunks: **void, n_chunks: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinZip(a: *const void, b: *const void, output: *VDRPrologPair_t, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinUnzip(pairs: *const VDRPrologPair_t, a: *void, b: *void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinReverse(data: *void, elem_size: i32, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinRotate(data: *void, elem_size: i32, n: i32, amount: i32) -> VDRPrologStatus_t
VDRPrologBuiltinTakeFirst(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> VDRPrologStatus_t
VDRPrologBuiltinTakeLast(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> VDRPrologStatus_t
VDRPrologBuiltinDropFirst(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> VDRPrologStatus_t
VDRPrologBuiltinDropLast(data: *const void, output: *void, elem_size: i32, n: i32, count: i32) -> VDRPrologStatus_t
VDRPrologBuiltinPartition(qbasis: VDRPrologQBasis_t, data: *const void, pred: *const bool, true_out: *void, false_out: *void, n: i32, n_true: *i32, n_false: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinInterleave(a: *const void, b: *const void, output: *void, elem_size: i32, n_a: i32, n_b: i32) -> VDRPrologStatus_t
VDRPrologBuiltinEnumerate(data: *const void, output: *VDRPrologIndexed_t, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinMinBy(qbasis: VDRPrologQBasis_t, data: *const void, keys: *const void, result: *void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinMaxBy(qbasis: VDRPrologQBasis_t, data: *const void, keys: *const void, result: *void, n: i32) -> VDRPrologStatus_t
VDRPrologBuiltinScan(qbasis: VDRPrologQBasis_t, data: *const void, op: VDRPrologBinaryOp_t, output: *void, n: i32) -> VDRPrologStatus_t
  Prefix scan. Exact integer accumulation — no drift across n elements.
VDRPrologBuiltinAll(predicates: *const bool, n: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinAny(predicates: *const bool, n: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinNone(predicates: *const bool, n: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinCount(predicates: *const bool, n: i32, count: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinFindFirst(qbasis: VDRPrologQBasis_t, data: *const void, target: *const void, n: i32, index: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinFindLast(qbasis: VDRPrologQBasis_t, data: *const void, target: *const void, n: i32, index: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinFindAll(qbasis: VDRPrologQBasis_t, data: *const void, target: *const void, n: i32, indices: *i32, max_indices: i32, n_found: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinBinarySearch(qbasis: VDRPrologQBasis_t, sorted_data: *const void, target: *const void, n: i32, index: *i32, found: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinMerge(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, output: *void, n_a: i32, n_b: i32) -> VDRPrologStatus_t
  Merge two sorted arrays. Exact comparison at merge boundaries.
VDRPrologBuiltinDeduplicate(qbasis: VDRPrologQBasis_t, sorted_data: *void, n: i32, n_deduped: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinWindow(data: *const void, elem_size: i32, n: i32, window_size: i32, windows: **void, n_windows: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinCartesianProduct(a: *const void, b: *const void, output: *VDRPrologPair_t, n_a: i32, n_b: i32) -> VDRPrologStatus_t

// --- Sets (14 functions) ---
VDRPrologBuiltinSetUnion(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetIntersection(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetDifference(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetSymmetricDiff(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, out: *void, n_a: i32, n_b: i32, n_out: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetIsSubset(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetIsSuperset(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetIsDisjoint(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetContains(qbasis: VDRPrologQBasis_t, set: *const void, element: *const void, n: i32, result: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetAdd(qbasis: VDRPrologQBasis_t, set: *void, element: *const void, n: *i32, max_n: i32, added: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetRemove(qbasis: VDRPrologQBasis_t, set: *void, element: *const void, n: *i32, removed: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetSize(n: i32, size: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetEqual(qbasis: VDRPrologQBasis_t, a: *const void, b: *const void, n_a: i32, n_b: i32, equal: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinSetPowerSet(qbasis: VDRPrologQBasis_t, set: *const void, n: i32, output: **void, n_subsets: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinSetFromArray(qbasis: VDRPrologQBasis_t, data: *const void, n: i32, set: *void, n_unique: *i32) -> VDRPrologStatus_t

// --- Mappings (15 functions) ---
VDRPrologBuiltinMapGet(map: *const VDRPrologMap_t, key: i32, value: *VDRPrologVdrFact_t, found: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinMapSet(map: *VDRPrologMap_t, key: i32, value: *const VDRPrologVdrFact_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapDelete(map: *VDRPrologMap_t, key: i32, deleted: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinMapContainsKey(map: *const VDRPrologMap_t, key: i32, found: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinMapKeys(map: *const VDRPrologMap_t, keys: *i32, max_keys: i32, n_keys: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinMapValues(map: *const VDRPrologMap_t, values: *VDRPrologVdrFact_t, max_values: i32, n_values: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinMapSize(map: *const VDRPrologMap_t, size: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinMapMerge(a: *const VDRPrologMap_t, b: *const VDRPrologMap_t, out: *VDRPrologMap_t, policy: VDRPrologMergePolicy_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapFilterKeys(map: *const VDRPrologMap_t, pred: *const bool, out: *VDRPrologMap_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapFilterValues(qbasis: VDRPrologQBasis_t, map: *const VDRPrologMap_t, pred: *const bool, out: *VDRPrologMap_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapMapValues(qbasis: VDRPrologQBasis_t, map: *const VDRPrologMap_t, op: VDRPrologUnaryOp_t, out: *VDRPrologMap_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapInvert(map: *const VDRPrologMap_t, out: *VDRPrologMap_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapClear(map: *VDRPrologMap_t) -> VDRPrologStatus_t
VDRPrologBuiltinMapEqual(a: *const VDRPrologMap_t, b: *const VDRPrologMap_t, equal: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinMapFromArrays(keys: *const i32, values: *const VDRPrologVdrFact_t, n: i32, map: *VDRPrologMap_t) -> VDRPrologStatus_t

// --- Conversion (14 functions) ---
VDRPrologBuiltinParseJson(input: *const u8, len: i32, kb_store: *VDRPrologKBStore_t, target_kb_id: i32) -> VDRPrologStatus_t
  Compiled JSON parser. Output goes to KB facts at integer addresses.
  Zero LLM tokens. Cannot fail on valid JSON.
VDRPrologBuiltinParseCsv(input: *const u8, len: i32, kb_store: *VDRPrologKBStore_t, target_kb_id: i32, delimiter: u8) -> VDRPrologStatus_t
VDRPrologBuiltinParseXml(input: *const u8, len: i32, kb_store: *VDRPrologKBStore_t, target_kb_id: i32) -> VDRPrologStatus_t
VDRPrologBuiltinParseYaml(input: *const u8, len: i32, kb_store: *VDRPrologKBStore_t, target_kb_id: i32) -> VDRPrologStatus_t
VDRPrologBuiltinToJson(kb_store: *VDRPrologKBStore_t, kb_id: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinToCsv(kb_store: *VDRPrologKBStore_t, kb_id: i32, output: *u8, out_cap: i32, out_len: *i32, delimiter: u8) -> VDRPrologStatus_t
VDRPrologBuiltinToFraction(qbasis: VDRPrologQBasis_t, numerator: i64, denominator: i64, result: *void) -> VDRPrologStatus_t
VDRPrologBuiltinFromFraction(qbasis: VDRPrologQBasis_t, value: *const void, numerator: *i64, denominator: *i64) -> VDRPrologStatus_t
VDRPrologBuiltinFormatNumber(qbasis: VDRPrologQBasis_t, value: *const void, format: *const u8, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinParseNumber(qbasis: VDRPrologQBasis_t, input: *const u8, len: i32, result: *void) -> VDRPrologStatus_t
VDRPrologBuiltinVdrToDecimalString(qbasis: VDRPrologQBasis_t, value: *const void, precision: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinDecimalStringToVdr(qbasis: VDRPrologQBasis_t, input: *const u8, len: i32, result: *void) -> VDRPrologStatus_t
VDRPrologBuiltinBaseConvert(value: i64, from_base: i32, to_base: i32, output: *u8, out_cap: i32, out_len: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinTimestampToFields(timestamp: i32, year: *i32, month: *i32, day: *i32, hour: *i32, minute: *i32, second: *i32) -> VDRPrologStatus_t

// --- Graph Operations (13 functions) ---
VDRPrologBuiltinGraphCreate(graph: *VDRPrologGraph_t, max_nodes: i32, max_edges: i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphAddNode(graph: *VDRPrologGraph_t, node_id: i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphAddEdge(graph: *VDRPrologGraph_t, from: i32, to: i32, weight: *const void) -> VDRPrologStatus_t
VDRPrologBuiltinGraphRemoveNode(graph: *VDRPrologGraph_t, node_id: i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphRemoveEdge(graph: *VDRPrologGraph_t, from: i32, to: i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphBFS(graph: *const VDRPrologGraph_t, start: i32, visited: *i32, n_visited: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphDFS(graph: *const VDRPrologGraph_t, start: i32, visited: *i32, n_visited: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphShortestPath(qbasis: VDRPrologQBasis_t, graph: *const VDRPrologGraph_t, from: i32, to: i32, path: *i32, max_path: i32, path_len: *i32, distance: *void) -> VDRPrologStatus_t
  Dijkstra with exact VDR weights. No floating point distance accumulation.
VDRPrologBuiltinGraphTopologicalSort(graph: *const VDRPrologGraph_t, sorted: *i32, n: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphConnectedComponents(graph: *const VDRPrologGraph_t, components: *i32, n_components: *i32) -> VDRPrologStatus_t
VDRPrologBuiltinGraphCycleDetect(graph: *const VDRPrologGraph_t, has_cycle: *bool) -> VDRPrologStatus_t
VDRPrologBuiltinGraphPageRankExact(qbasis: VDRPrologQBasis_t, graph: *const VDRPrologGraph_t, ranks: *void, n_iterations: i32) -> VDRPrologStatus_t
  Exact PageRank as VDR fractions. Converges to exact steady state.
VDRPrologBuiltinGraphMarkovSteady(qbasis: VDRPrologQBasis_t, transition: *const void, steady: *void, n: i32) -> VDRPrologStatus_t
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

## Module 23: VDRProlog_profiling

Profiling and diagnostics. Simplified by absence of float complexity.

```
VDRPrologProfileStart(profiler: *VDRPrologProfiler_t) -> VDRPrologStatus_t
VDRPrologProfileStop(profiler: VDRPrologProfiler_t) -> VDRPrologStatus_t

VDRPrologProfileGetKernelStats(profiler: VDRPrologProfiler_t, kernel_id: i32, stats: *VDRPrologKernelStats_t) -> VDRPrologStatus_t
  Stats: elapsed_ns (i64), integer_ops (i64), memory_bytes_read (i64),
  memory_bytes_written (i64), warp_occupancy_percent (i32 — always near 100),
  kb_cache_hits (i64), kb_cache_misses (i64), remainder_overflows (i64).
  No float utilization metrics. No SFU utilization. No tensor-core-vs-cuda-core
  breakdown. One compute type.

VDRPrologProfileGetSessionStats(session: VDRPrologSession_t, stats: *VDRPrologSessionStats_t) -> VDRPrologStatus_t
  Stats: total_turns, total_facts_asserted, total_rules_fired,
  total_prolog_queries, total_kb_accesses, total_primitive_calls,
  total_grammar_renders, total_llm_tokens (from external LLM integration),
  total_command_tokens, auto_triage_percentage (exact VDR fraction).

VDRPrologProfileVerifyDeterminism(kernel: *const void, args: **void, grid: VDRPrologDim3_t, block: VDRPrologDim3_t, n_runs: i32, identical: *bool) -> VDRPrologStatus_t
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
| core | 11 | VDRProlog Runtime init/device |
| memory | 10 | VDRProlog memory management |
| stream | 10 | VDRProlog streams/events |
| session | 10 | Nothing — new capability |
| launch | 5 | VDRProlog kernel launch |
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

**What's new:** ~90 functions across session/KB/Prolog/grammar/runner/safety/confidence that enable the architectural capabilities the paper describes — autonomous operation, persistent state, structural safety, exact provenance — none of which exist in any form in CUDA.
