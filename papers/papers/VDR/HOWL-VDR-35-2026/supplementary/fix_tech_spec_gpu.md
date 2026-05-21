## Review

Before rewriting, let me confirm my understanding of the constraints and get one clarification.

From the analysis, the rewrite needs to:

1. Move grammar engine, path resolution, COW management, and KB structural operations to host
2. Rewrite Prolog unification from recursive to iterative with explicit stack in storage buffer
3. Replace dynamic dispatch (function pointers) with static pipeline selection on host
4. Reduce shared memory assumptions to 32KB baseline
5. Express all GPU compute as stateless kernels operating on bound storage buffers
6. Error reporting via status buffer, not return codes
7. Keep LLM forward pass, parallel unification scan, and math builtins on GPU

The data types, memory layout, session model, safety model, invariants, and host-side orchestration (Sections 3, 4.1, 4.2, 5, 7-18) remain unchanged — only Section 4.3 (shared memory), Section 6 (device engines), and the bridge layer need rewriting.

One question before I write: the spec references "VDRProlog Hardware Layer" as a custom silicon concept (integer ALUs, KB Cache, FRU, Warp Scheduler). Should the rewrite target **commodity Vulkan GPU hardware** (T4, L4, H100 — what you'd actually run on GCP today), or should it preserve the aspirational custom hardware path alongside? I'll assume commodity Vulkan as the primary target with a note about future custom silicon, since that's what you're actually building toward with this project. Agree?

Actually — you said write it, so I'll proceed with commodity Vulkan as primary, custom silicon as noted future path.

---

# Section 4.3 — Shared Memory Usage (Per Workgroup) — REVISED

```
// ============================================================
// Shared Memory: sized for Vulkan minimum (32 KB guaranteed).
// Larger allocations available on H100 (228 KB) — detected at
// runtime via vkGetPhysicalDeviceProperties.maxComputeSharedMemorySize.
// Kernels declare their shared memory need. Host selects variant.
// ============================================================

// Baseline profile: 32 KB (all Vulkan 1.2 devices)
struct vlp_shared_baseline {
    // Softmax accumulator — one head's attention scores
    softmax_scratch: [2048]i32,     // 2048 × 4 bytes = 8 KB
    // Covers seq_len up to 2048 per dispatch. Longer sequences
    // require multiple dispatches with host-side accumulation.

    // Fact scan cache — for parallel unification
    fact_cache: [256]vlp_fact,      // 256 facts × 40 bytes = 10 KB
    // One warp scans 32 facts simultaneously. 8 warps = 256 facts.

    // Unification stack — iterative Prolog, per-invocation
    // NOT in shared memory. In per-invocation private storage or
    // in a storage buffer region indexed by global_invocation_id.
    // Shared memory is for data shared ACROSS invocations in a workgroup.

    // Reduction scratch — for parallel reductions (sum, max, argmax)
    reduction_scratch: [1024]i32,   // 1024 × 4 bytes = 4 KB

    // Binding results — unification outputs from parallel scan
    binding_results: [128]vlp_binding, // 128 × 8 bytes = 1 KB

    // Workgroup status — error codes, match counts
    status: [256]i32,               // 256 × 4 bytes = 1 KB

    // Total: 24 KB. Within 32 KB budget. 8 KB headroom.
};

// Extended profile: 64 KB (most discrete GPUs)
struct vlp_shared_extended {
    softmax_scratch: [4096]i32,     // 16 KB — seq_len up to 4096
    fact_cache: [512]vlp_fact,      // 20 KB
    reduction_scratch: [2048]i32,   // 8 KB
    binding_results: [256]vlp_binding, // 2 KB
    status: [256]i32,               // 1 KB
    // Total: 47 KB.
};

// H100 profile: 228 KB (configured via Vulkan device properties)
// Extends with larger fact cache (2048 facts, 80 KB) and
// full KV-cache tile for fused attention kernels.
// Selected at pipeline creation time based on device query.
```

---

# Section 6 — Device Engines — REVISED

The device side is restructured into **compute kernels** dispatched by the host. No engine has autonomous control flow on GPU. The host orchestrates all sequencing. The GPU executes parallel work items.

## 6.0 Device-Side Principles

```
// ============================================================
// GPU Compute Model for VLP
// ============================================================
//
// 1. All GPU code is Vulkan compute shaders (GLCompute execution model).
//    No graphics pipeline. No vertex/fragment shaders.
//
// 2. No recursion. All algorithms iterative with explicit bounds.
//
// 3. No dynamic dispatch on GPU. Host selects pipeline, GPU executes.
//
// 4. No dynamic memory allocation on GPU. All buffers pre-allocated
//    by host as Vulkan storage buffers, bound via descriptor sets.
//
// 5. No string manipulation on GPU. Text operations are host-side.
//    GPU operates on integer indices, offsets, and values only.
//
// 6. Error reporting via status buffer. Kernel writes error code
//    to status_buffer[global_invocation_id]. Host reads after dispatch.
//
// 7. All inter-kernel data flows through storage buffers.
//    No host round-trip between dependent GPU operations unless
//    the host needs to make a branching decision.
//
// 8. Kernels are stateless. All state is in bound storage buffers.
//    Re-dispatching the same kernel with the same buffer contents
//    produces the same results. Always.
//
// 9. Integer arithmetic only. i32 primary. i64 for widening products
//    and address computation. No float types anywhere.
//
// 10. Workgroup shared memory used for intra-workgroup communication
//     only. Cross-workgroup communication via storage buffers with
//     appropriate barriers.
// ============================================================
```

## 6.1 Buffer Binding Architecture

```
// ============================================================
// Every kernel binds a subset of these storage buffers.
// Host creates all buffers at vlp_device_memory_layout init time.
// Descriptor sets organized by update frequency:
//
//   Set 0: Model weights (bound once at model load, never changes)
//   Set 1: KB/fact/rule/term stores (bound per session, changes on COW fault)
//   Set 2: Scratch/intermediate (bound per dispatch, recycled)
//   Set 3: Status/control (bound per dispatch)
//
// This minimizes descriptor set updates between dispatches.
// ============================================================

// Set 0 — Model (read-only)
// binding 0: embedding_table      [vocab_size × d_model] vlp_q16
// binding 1: layer_weights        [n_layers × layer_stride] vlp_q16
// binding 2: lm_head              [vocab_size × d_model] vlp_q16
// binding 3: layer_norm_params    [n_layers × 2 × d_model] vlp_q16

// Set 1 — KB Data (read-write, per session)
// binding 0: kb_store             [max_kbs × 256] bytes (vlp_kb array)
// binding 1: fact_store           [max_facts × 40] bytes (vlp_fact array)
// binding 2: rule_store           [max_rules × 44] bytes (vlp_rule array)
// binding 3: term_store           [max_terms × 24] bytes (vlp_term array)
// binding 4: live_state           [session_live_size] bytes

// Set 2 — Scratch (read-write, per dispatch)
// binding 0: scratch_a            [scratch_size] bytes
// binding 1: scratch_b            [scratch_size] bytes
// binding 2: kv_cache             [kv_cache_size] bytes

// Set 3 — Control (read-write, per dispatch)
// binding 0: dispatch_params      uniform buffer, kernel-specific parameters
// binding 1: status_buffer        [max_invocations] i32
// binding 2: result_counts        [small] i32 — atomic counters for results
```

## 6.2 LLM Kernels

```
// ============================================================
// LLM forward pass decomposed into individual compute dispatches.
// Host orchestrates the sequence. Each kernel is one parallel step.
// ============================================================

// ------------------------------------------------------------
// Kernel: vlp_kernel_embedding_lookup
// ------------------------------------------------------------
// Maps token IDs to embedding vectors.
// Dispatch: (n_tokens, 1, 1), local_size (256, 1, 1)
// Each invocation handles one element of one embedding vector.
//
// Inputs:
//   dispatch_params.n_tokens: i32
//   dispatch_params.d_model: i32
//   Set 0 binding 0: embedding_table (read)
//   Set 2 binding 0 scratch_a: input_token_ids [n_tokens] i32 (read)
// Outputs:
//   Set 2 binding 1 scratch_b: embedded [n_tokens × d_model] vlp_q16 (write)
//
// Algorithm:
//   gid = global_invocation_id.x
//   token_idx = gid / d_model
//   dim_idx = gid % d_model
//   if (token_idx >= n_tokens) return
//   token_id = scratch_a[token_idx]
//   scratch_b[token_idx * d_model + dim_idx] = embedding_table[token_id * d_model + dim_idx]
//
// Pure read + write. No arithmetic. Memory-bound.

// ------------------------------------------------------------
// Kernel: vlp_kernel_layer_norm
// ------------------------------------------------------------
// Applies RMSNorm or LayerNorm over d_model dimension.
// Dispatch: (n_tokens, 1, 1), local_size (256, 1, 1)
// Uses workgroup shared memory for parallel reduction (mean, variance).
//
// Inputs:
//   dispatch_params.n_tokens: i32
//   dispatch_params.d_model: i32
//   dispatch_params.layer_idx: i32
//   dispatch_params.norm_idx: i32  (0 = pre-attention, 1 = pre-MLP)
//   Set 0 binding 3: layer_norm_params (read)
//   Set 2 binding 0: input [n_tokens × d_model] vlp_q16 (read)
// Outputs:
//   Set 2 binding 1: output [n_tokens × d_model] vlp_q16 (write)
//
// Algorithm:
//   Per workgroup (one workgroup per token position):
//   1. Load d_model values into shared memory reduction_scratch.
//   2. Parallel reduction: compute sum of values (for mean).
//      Q16 sum: accumulate i32 values. Overflow to i64 if d_model > 8192.
//   3. Parallel reduction: compute sum of squared deviations.
//      Squared deviation: (v - mean)² computed via integer multiply.
//      Intermediate: i64 to hold i32 × i32 product.
//   4. Compute inverse sqrt of variance via integer Newton-Raphson.
//      Iterative. 4 iterations gives exact Q16 result for typical ranges.
//      No recursion — fixed iteration count.
//   5. Apply: output[i] = gamma[i] * (input[i] - mean) * inv_sqrt + beta[i]
//      All integer multiply + shift.

// ------------------------------------------------------------
// Kernel: vlp_kernel_qkv_project
// ------------------------------------------------------------
// Projects input into Q, K, V for all heads.
// This is a GEMM: [n_tokens × d_model] × [d_model × 3*d_model] → [n_tokens × 3*d_model]
// Dispatch: (n_tokens × n_heads × d_head, 1, 1), local_size (256, 1, 1)
// Or tiled GEMM dispatch for better occupancy.
//
// Inputs:
//   dispatch_params: n_tokens, d_model, n_heads, d_head, layer_idx
//   Set 0 binding 1: layer_weights (read) — QKV weight subregion
//   Set 2 binding 0: input (read)
// Outputs:
//   Set 2 binding 1: qkv_output [n_tokens × 3 × n_heads × d_head] vlp_q16 (write)
//
// Algorithm:
//   Standard tiled integer GEMM.
//   Accumulator: i64 (sum of i32 × i32 products).
//   Final: shift right by Q16 fractional bits, store Q16 result + remainder.
//   Tiles loaded into shared memory for reuse.
//   No recursion. Fixed tile size. Bounded iteration.

// ------------------------------------------------------------
// Kernel: vlp_kernel_attention_scores
// ------------------------------------------------------------
// Computes Q × K^T for one layer, all heads.
// Dispatch: (n_heads, n_tokens, 1), local_size (32, 1, 1)
// Each workgroup computes one row of attention scores for one head.
//
// Inputs:
//   dispatch_params: n_tokens, n_heads, d_head, seq_len, scale_v (attention scale as Q16)
//   Set 2 binding 1: qkv (read) — Q and K subregions
//   Set 2 binding 2: kv_cache (read) — previous K values
// Outputs:
//   Set 2 binding 0: attention_scores [n_heads × n_tokens × seq_len] i32 (write)
//
// Algorithm per workgroup:
//   head_idx = workgroup_id.x
//   query_pos = workgroup_id.y
//   For each key_pos in [0..seq_len):
//     dot = sum(Q[query_pos, head_idx, d] * K[key_pos, head_idx, d] for d in 0..d_head)
//     Accumulator: i64. Product: i32 × i32 → i64. Sum of d_head products.
//     score = (dot * scale_v) >> 16  // apply 1/sqrt(d_head) scaling
//     attention_scores[head_idx][query_pos][key_pos] = score
//   Causal mask: if key_pos > query_pos: score = INT32_MIN (masked out in softmax)

// ------------------------------------------------------------
// Kernel: vlp_kernel_softmax_exact
// ------------------------------------------------------------
// Exact integer softmax. Output sums to D (65536 for Q16). Exactly.
// Dispatch: (n_heads × n_tokens, 1, 1), local_size (256, 1, 1)
// Each workgroup processes one row of attention scores.
//
// Inputs:
//   dispatch_params: seq_len, D (denominator, 65536 for Q16)
//   Set 2 binding 0: attention_scores (read)
// Outputs:
//   Set 2 binding 0: attention_probs (write, in-place)
//
// Algorithm per workgroup:
//   1. Load row into shared memory softmax_scratch. (Coalesced read.)
//   2. Parallel reduction: find max score. (Integer comparison, log2(n) steps.)
//   3. Subtract max from all scores. (Prevents overflow in next step.)
//   4. Compute exp approximation for each score.
//      Integer exp: piecewise polynomial or lookup table in shared memory.
//      Input range bounded by max subtraction. Output: positive i32.
//   5. Parallel reduction: compute sum of all exp values.
//   6. Normalize: prob[i] = (exp[i] * D) / sum.
//      Integer division. Quotient → .v, modulus → .r0.
//   7. Distribute remainder: sum of all prob[i].v may be D-1 or D+1
//      due to individual rounding. Adjust: find the element with largest
//      remainder. Add or subtract 1. Now sum == D. Exactly.
//      This is the FRU (Fixed Remainder Unit) algorithm from the paper.
//   8. Write probabilities back. Sum verified == D by construction.

// ------------------------------------------------------------
// Kernel: vlp_kernel_attention_weighted_sum
// ------------------------------------------------------------
// Computes attention_probs × V for one layer, all heads.
// Dispatch: (n_heads, n_tokens, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params: n_tokens, n_heads, d_head, seq_len
//   Set 2 binding 0: attention_probs (read)
//   Set 2 binding 1: qkv (read) — V subregion
//   Set 2 binding 2: kv_cache (read) — previous V values
// Outputs:
//   Set 2 binding 0: attn_output [n_tokens × n_heads × d_head] vlp_q16 (write)
//
// Algorithm:
//   Weighted sum: output[pos][head][d] = sum(prob[pos][key] * V[key][head][d])
//   Accumulator: i64. Each product: i32 × i32. Sum of seq_len products.
//   Final shift to Q16.

// ------------------------------------------------------------
// Kernel: vlp_kernel_output_project
// ------------------------------------------------------------
// Projects concatenated head outputs through output weight matrix.
// GEMM: [n_tokens × d_model] × [d_model × d_model] → [n_tokens × d_model]
// Same pattern as vlp_kernel_qkv_project.

// ------------------------------------------------------------
// Kernel: vlp_kernel_mlp
// ------------------------------------------------------------
// Two-layer MLP: up-project, activation, down-project.
// Dispatch: two GEMMs with activation between.
//
// Activation (SiLU/GELU): integer approximation.
//   SiLU(x) = x * sigmoid(x).
//   sigmoid(x): piecewise linear or polynomial in integer.
//   5-segment piecewise linear gives <0.5% error at Q16.
//   Or: lookup table (256 entries × 4 bytes = 1 KB in shared memory).
//   No transcendentals. No floats.

// ------------------------------------------------------------
// Kernel: vlp_kernel_lm_head
// ------------------------------------------------------------
// Final projection: hidden → logits over vocabulary.
// GEMM: [1 × d_model] × [d_model × vocab_size] → [1 × vocab_size]
// (For single-token generation. Batched for prefill.)
//
// Output: logits as i32 array. Host reads for sampling.

// ------------------------------------------------------------
// Kernel: vlp_kernel_kv_cache_append
// ------------------------------------------------------------
// Stores K and V vectors for new positions in KV-cache buffer.
// Dispatch: (n_new_tokens × n_heads × d_head, 1, 1), local_size (256, 1, 1)
//
// Each invocation writes one element:
//   cache_offset = layer * max_seq * n_heads * d_head * 2
//                + position * n_heads * d_head * 2
//                + head * d_head * 2
//                + kv_select * d_head  // 0 for K, 1 for V
//                + dim
//   kv_cache[cache_offset] = value
//
// Pure scatter write. O(1) per element. No search.

// ============================================================
// LLM Forward Pass — Host Orchestration
// ============================================================
//
// The host dispatches kernels in sequence for one forward pass:
//
//   1. vlp_kernel_embedding_lookup
//   2. For each layer in 0..n_layers:
//      a. vlp_kernel_layer_norm (pre-attention)
//      b. vlp_kernel_qkv_project
//      c. vlp_kernel_kv_cache_append (K and V for new positions)
//      d. vlp_kernel_attention_scores
//      e. vlp_kernel_softmax_exact
//      f. vlp_kernel_attention_weighted_sum
//      g. vlp_kernel_output_project
//      h. Residual add (trivial kernel or fused with output_project)
//      i. vlp_kernel_layer_norm (pre-MLP)
//      j. vlp_kernel_mlp
//      k. Residual add
//   3. vlp_kernel_layer_norm (final)
//   4. vlp_kernel_lm_head
//
// All dispatches on the same Vulkan command buffer.
// Pipeline barriers between dependent steps.
// No host round-trip between layers — entire forward pass is
// one command buffer submission.
//
// Host reads back logits after final dispatch + fence wait.
// Sampling (argmax, top-k, top-p) is host-side — it's a single
// scan over vocab_size integers. Not worth a GPU dispatch.
```

## 6.3 KB Store Kernels

```
// ============================================================
// KB store management is split: structural operations on host,
// bulk data operations (scans, searches) on GPU.
// ============================================================
//
// HOST-SIDE (not kernels):
//   - KB creation, deletion, tree manipulation
//   - Path index (hash map: dotted path → kb_id)
//   - COW page table management
//   - Fact slot allocation within a KB's region
//   - KB freeze, visibility changes
//   - All operations that modify the KB struct itself
//
// GPU-SIDE (kernels below):
//   - Bulk fact reads and writes
//   - Parallel scoped search (scan facts across KB chain)
//   - Fact tag filtering
//   - Bulk provenance queries
//
// The boundary: host decides WHICH KB and WHERE in the fact store.
// GPU does the parallel work WITHIN the fact store region.
// ============================================================

// ------------------------------------------------------------
// Kernel: vlp_kernel_fact_write_batch
// ------------------------------------------------------------
// Writes multiple facts to fact store in parallel.
// Dispatch: (n_facts, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_facts: i32
//   dispatch_params.base_offset: i32 — starting offset in fact store
//   Set 2 binding 0: facts_to_write [n_facts] vlp_fact (read)
//   Set 2 binding 1: slot_ids [n_facts] i32 (read) — target slot indices
// Outputs:
//   Set 1 binding 1: fact_store (write) — at computed offsets
//   Set 3 binding 1: status_buffer (write)
//
// Algorithm:
//   gid = global_invocation_id.x
//   if (gid >= n_facts) return
//   target = base_offset + slot_ids[gid]
//   // Bounds check
//   if (target >= fact_store_capacity) { status_buffer[gid] = ERR_KB_FULL; return }
//   fact_store[target] = facts_to_write[gid]
//   status_buffer[gid] = 0  // success

// ------------------------------------------------------------
// Kernel: vlp_kernel_fact_read_batch
// ------------------------------------------------------------
// Reads multiple facts from fact store in parallel.
// Dispatch: (n_reads, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_reads: i32
//   Set 2 binding 0: read_offsets [n_reads] i32 (read) — absolute offsets
// Outputs:
//   Set 2 binding 1: facts_out [n_reads] vlp_fact (write)
//
// Algorithm:
//   gid = global_invocation_id.x
//   if (gid >= n_reads) return
//   facts_out[gid] = fact_store[read_offsets[gid]]

// ------------------------------------------------------------
// Kernel: vlp_kernel_fact_scan_by_tag
// ------------------------------------------------------------
// Scans a contiguous range of facts for matching tag.
// Used for: finding all facts of a given type within one KB.
// Dispatch: (scan_length, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.base_offset: i32  — KB's facts_offset
//   dispatch_params.scan_length: i32  — KB's facts_count
//   dispatch_params.target_tag: i32   — vlp_fact_tag to match
//   dispatch_params.max_results: i32
// Outputs:
//   Set 2 binding 0: matching_indices [max_results] i32 (write)
//   Set 3 binding 2: result_counts [1] i32 (atomic write) — number of matches
//
// Algorithm:
//   gid = global_invocation_id.x
//   if (gid >= scan_length) return
//   fact = fact_store[base_offset + gid]
//   if (fact.tag == target_tag) {
//     idx = atomicAdd(result_counts[0], 1)
//     if (idx < max_results) {
//       matching_indices[idx] = gid  // slot_id within KB
//     }
//   }

// ------------------------------------------------------------
// Kernel: vlp_kernel_scoped_search
// ------------------------------------------------------------
// Searches for facts along a KB parent chain.
// The parent chain is PRE-RESOLVED by the host into an array of
// (kb_id, facts_offset, facts_count) tuples. The host walks the
// KB tree and builds this array. The GPU scans facts in parallel.
//
// Dispatch: (total_facts_across_chain, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_chain_entries: i32
//   dispatch_params.total_facts: i32
//   dispatch_params.target_tag: i32
//   dispatch_params.max_results: i32
//   Set 2 binding 0: chain_table [n_chain_entries × 3] i32 (read)
//     Each entry: (kb_id, facts_offset, facts_count)
//     Sorted by priority (deepest first — lexical scoping).
//   Set 2 binding 1: scan_offsets [total_facts] i32 (read)
//     Pre-computed by host: absolute fact_store offset for each fact
//     to scan, ordered by chain priority.
// Outputs:
//   Set 2 binding 0: matching_facts [max_results] vlp_fact (write)
//   Set 2 binding 1: matching_kb_ids [max_results] i32 (write)
//   Set 3 binding 2: result_counts [1] i32 (atomic)
//
// The host pre-computes the scan plan. The GPU executes it.
// This avoids pointer chasing (parent_id traversal) on GPU.
```

## 6.4 Prolog Kernels

```
// ============================================================
// Prolog on GPU: parallel candidate evaluation, iterative search.
//
// The Prolog engine is split:
//   HOST: query planning, search tree management, result collection
//   GPU:  parallel unification of candidates, bulk rule matching
//
// Key insight: unification of one query against N candidate facts
// is embarrassingly parallel. Each unification is independent.
// The sequential part (backtracking, depth-first search) stays on host.
// The parallel part (evaluate all candidates at current search node)
// dispatches to GPU.
// ============================================================

// ------------------------------------------------------------
// Kernel: vlp_kernel_unify_candidates
// ------------------------------------------------------------
// Attempts to unify a single query term against N candidate facts.
// Each invocation handles one candidate.
// Dispatch: (n_candidates, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_candidates: i32
//   dispatch_params.query_term_offset: i32  — offset into term_store
//   dispatch_params.query_term_type: i32
//   dispatch_params.query_atom_id: i32      — for ATOM queries
//   dispatch_params.query_functor_id: i32   — for COMPOUND queries
//   dispatch_params.query_args_count: i32
//   Set 2 binding 0: candidate_offsets [n_candidates] i32 (read)
//     Absolute offsets into fact_store for each candidate.
// Outputs:
//   Set 2 binding 1: unify_results [n_candidates] i32 (write)
//     Per candidate: 1 = unified, 0 = failed
//   Set 2 binding 0: bindings_out [n_candidates × max_bindings_per] vlp_binding (write)
//     Bindings produced by each successful unification.
//   Set 3 binding 2: result_counts [1] i32 (atomic) — number of successes
//
// Algorithm per invocation (ITERATIVE, not recursive):
//   gid = global_invocation_id.x
//   if (gid >= n_candidates) return
//
//   candidate = fact_store[candidate_offsets[gid]]
//
//   // Flat unification — no recursion.
//   // Handles the common cases that cover ~95% of Prolog queries:
//   //   ATOM-ATOM: compare atom_id (integer equality)
//   //   VARIABLE-anything: always succeeds, produces binding
//   //   VDR-VDR: cross-multiply comparison (a.v * b_D == b.v * a_D)
//   //   INTEGER-INTEGER: integer equality
//   //   COMPOUND-COMPOUND: functor match + arg-by-arg comparison
//
//   // For COMPOUND with args, args are compared iteratively:
//   //   for (i = 0; i < query_args_count; i++):
//   //     if (!unify_flat(query_arg[i], candidate_arg[i])): fail
//   //   Bounded by query_args_count (maximum from dispatch_params).
//   //   No recursion. Fixed iteration count.
//
//   // Nested COMPOUND (compound inside compound) is handled by
//   // limiting nesting depth at query planning time (host side).
//   // The host flattens deeply nested queries into multiple
//   // dispatch rounds. Each round handles one nesting level.
//
//   if (unified) {
//     unify_results[gid] = 1
//     // Write bindings at gid * max_bindings_per
//     idx = atomicAdd(result_counts[0], 1)
//   } else {
//     unify_results[gid] = 0
//   }

// ------------------------------------------------------------
// Kernel: vlp_kernel_rule_match_scan
// ------------------------------------------------------------
// Evaluates all rules in a KB against current fact state.
// Each invocation evaluates one rule's HEAD against the query.
// Dispatch: (n_rules, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_rules: i32
//   dispatch_params.rules_base_offset: i32
//   dispatch_params.query_term_offset: i32
// Outputs:
//   Set 2 binding 0: head_match_results [n_rules] i32 (write)
//     1 = head matches query, 0 = no match
//   Set 2 binding 1: matched_rule_ids [max_matches] i32 (write)
//   Set 3 binding 2: result_counts [1] i32 (atomic)
//
// Algorithm per invocation:
//   gid = global_invocation_id.x
//   if (gid >= n_rules) return
//   rule = rule_store[rules_base_offset + gid]
//   head_term = term_store[rule.head]
//   // Flat unify head_term against query_term (same as above)
//   if (matched) {
//     head_match_results[gid] = 1
//     idx = atomicAdd(result_counts[0], 1)
//     if (idx < max_matches) matched_rule_ids[idx] = rule.id
//   }

// ------------------------------------------------------------
// Kernel: vlp_kernel_rule_body_eval
// ------------------------------------------------------------
// For rules whose heads matched, evaluate body conditions.
// Each invocation evaluates one body condition of one matched rule
// against the fact store.
// Dispatch: (n_matched_rules × max_body_conditions, 1, 1)
//
// Inputs:
//   dispatch_params.n_matched: i32
//   dispatch_params.max_body: i32
//   Set 2 binding 0: matched_rule_ids (read)
//   Set 2 binding 1: body_eval_results [n_matched × max_body] i32 (write)
//     Per condition: 1 = satisfied, 0 = not satisfied
//
// Algorithm per invocation:
//   rule_idx = gid / max_body
//   body_idx = gid % max_body
//   if (rule_idx >= n_matched) return
//   rule = rule_store[matched_rule_ids[rule_idx]]
//   if (body_idx >= rule.body_count) { body_eval_results[gid] = 1; return } // vacuously true
//   body_term = term_store[rule.body_offset + body_idx]
//   // Scan fact store for matching fact (reuses fact_scan_by_tag pattern)
//   // If found: body_eval_results[gid] = 1
//   // If not found: body_eval_results[gid] = 0

// ------------------------------------------------------------
// Kernel: vlp_kernel_rule_check_fully_satisfied
// ------------------------------------------------------------
// Reduces body_eval_results per rule: a rule fires iff ALL conditions met.
// Dispatch: (n_matched_rules, 1, 1), local_size (256, 1, 1)
//
// Inputs:
//   dispatch_params.n_matched: i32
//   dispatch_params.max_body: i32
//   Set 2 binding 0: matched_rule_ids (read)
//   Set 2 binding 1: body_eval_results (read)
// Outputs:
//   Set 2 binding 0: firing_rule_ids [max_fires] i32 (write)
//   Set 3 binding 2: result_counts [1] i32 (atomic) — number of firing rules
//
// Algorithm per invocation:
//   gid = global_invocation_id.x
//   if (gid >= n_matched) return
//   rule = rule_store[matched_rule_ids[gid]]
//   all_satisfied = true
//   for (i = 0; i < rule.body_count; i++):
//     if (body_eval_results[gid * max_body + i] == 0):
//       all_satisfied = false; break
//   if (all_satisfied):
//     idx = atomicAdd(result_counts[0], 1)
//     if (idx < max_fires): firing_rule_ids[idx] = matched_rule_ids[gid]

// ============================================================
// Prolog Query — Host Orchestration
// ============================================================
//
// The host drives the Prolog search:
//
//   1. Parse query into vlp_term (host-side, text → integers).
//   2. Determine candidate KB chain via access check (host-side).
//   3. Build scan plan: (kb_id, facts_offset, facts_count) array.
//   4. Dispatch vlp_kernel_unify_candidates.
//   5. Read back results. If any unified:
//      a. For rules with body conditions: dispatch vlp_kernel_rule_body_eval.
//      b. Read back body results.
//      c. Dispatch vlp_kernel_rule_check_fully_satisfied.
//      d. Read back firing rules.
//   6. Collect bindings from successful unifications.
//   7. If depth > 0 and unresolved sub-goals remain:
//      Build new candidate set for sub-goal, goto 4.
//      This is the backtracking loop — iterative on host.
//      Each iteration dispatches parallel GPU work.
//   8. Enforce depth limit (default 100 iterations of this loop).
//   9. Return collected bindings to caller.
//
// The host does O(depth) round-trips to GPU. Each round-trip
// evaluates O(n_candidates) unifications in parallel on GPU.
// For typical queries: depth 3-5, candidates 50-500.
// GPU parallelism pays off when candidates > ~32 (one warp).
// For tiny queries (< 32 candidates), host can run unification
// directly — same integer algorithm, just on CPU.
```

## 6.5 Math Builtin Kernels

```
// ============================================================
// Math builtins that operate on VDR arrays are GPU kernels.
// Each builtin category is one or a few compute shaders.
// Host selects pipeline by builtin_id (integer lookup in host table).
// ============================================================

// The 448 builtins from the paper decompose into kernel groups:

// Group 1: Element-wise unary operations (35 builtins)
//   abs, negate, sign, complement, clz, ctz, popcount, etc.
//   One kernel handles all: dispatch_params.op_code selects operation.
//   Dispatch: (n_elements, 1, 1), local_size (256, 1, 1)
//   switch(op_code) in kernel — static branching, no function pointers.

// Group 2: Element-wise binary operations (40 builtins)
//   add, sub, mul, div, mod, min, max, gcd, lcm, and, or, xor, etc.
//   One kernel, op_code selects.
//   Division: integer division + remainder. Exact.

// Group 3: Reduction operations (25 builtins)
//   sum, product, min, max, mean, variance, median, mode, etc.
//   Parallel reduction in shared memory.
//   One kernel per reduction type (different reduction operators).

// Group 4: Sort and search (15 builtins)
//   sort, reverse, unique, binary_search, rank, percentile.
//   Bitonic sort in shared memory for small arrays.
//   Radix sort via multiple dispatches for large arrays.

// Group 5: Linear algebra (30 builtins)
//   dot, matmul, transpose, trace, determinant (bounded size).
//   matmul: tiled integer GEMM (same pattern as LLM layers).
//   determinant: LU decomposition, integer pivoting.

// Group 6: Statistical (20 builtins)
//   histogram, correlation, covariance, linear_regression.
//   Each is a sequence of reductions and element-wise ops.

// Group 7: Comparison and selection (20 builtins)
//   compare, threshold, clamp, select, where, mask.
//   Element-wise, trivially parallel.

// Group 8: VDR-specific (30 builtins)
//   q16_to_q32, q32_to_q16, remainder_compact, cross_multiply_compare,
//   confidence_combine, confidence_chain.
//   These are the VDR arithmetic foundation operations.

// ============================================================
// Builtin Dispatch — Host Side
// ============================================================
//
// Host maintains: builtin_dispatch_table[448] → pipeline_handle
// Pipeline handle is a Vulkan VkPipeline created at init time.
//
// vlp_builtin_dispatch(builtin_id, args):
//   1. Validate args against IOSE declaration (host, integer checks).
//   2. Load input data from KB to scratch buffer (GPU copy kernel or host copy).
//   3. Select pipeline: pipeline = builtin_dispatch_table[builtin_id]
//   4. Bind descriptor sets with input/output buffers.
//   5. Dispatch compute. Wait on fence.
//   6. Copy result from scratch to target KB address (GPU copy or host).
//   7. Return result reference (kb_id + slot_id).
//
// No function pointers on GPU. No dynamic dispatch on GPU.
// The host does the dispatch. The GPU does the math.
```

## 6.6 Engines That Moved to Host

```
// ============================================================
// The following engines execute entirely on host (CPU).
// They read/write GPU storage buffers via mapped memory or
// staging buffer copies, but their logic is CPU-side.
// ============================================================

// Grammar Engine — HOST ONLY
//   Reason: serial text manipulation (template walking, string
//   concatenation, integer-to-ASCII conversion). Wrong workload
//   for GPU. Typical render time: microseconds on CPU.
//   Data flow: host reads fact values from GPU buffer (mapped or
//   staging copy), renders through template, writes output to
//   session output buffer (host memory).
//   Functions unchanged from original spec Section 6.4.

// Path Index — HOST ONLY
//   Reason: hash map with variable-length string keys.
//   Host maintains the hash map in host memory.
//   On KB creation: host inserts (path_hash, kb_id).
//   On path resolution: host looks up kb_id from dotted path string.
//   GPU never sees dotted path strings — only integer kb_id values.

// COW Page Management — HOST ONLY
//   Reason: page table manipulation, fault handling, and merge
//   are inherently serial control-flow operations.
//   Host tracks which pages are shared vs private per clone.
//   On clone write to shared page: host copies page data
//   (GPU-to-GPU copy via staging or peer copy), updates page table,
//   retries the write. The write itself may be a GPU kernel dispatch,
//   but the COW fault handling is host logic.

// Access Control — HOST ONLY
//   Reason: KB tree walk with branching visibility checks.
//   Typically 3-10 integer comparisons. Nanoseconds on CPU.
//   Not worth a GPU dispatch.

// Grant Checking — HOST ONLY
//   Reason: index lookup + integer comparisons + atomic decrement.
//   The grant store CAN be in GPU memory (for grants checked during
//   GPU-side rule firing). But the check logic is simple enough
//   that host-side checking before dispatch is preferred.
//   The atomic decrement of remaining_uses happens on host.

// Audit Log — HOST ONLY for writes, GPU READABLE
//   Reason: append-only ring buffer writes are serial.
//   Host writes audit entries. GPU can read audit entries for
//   builtins that query audit history (if any).

// Command Parsing — HOST ONLY
//   Reason: token stream parsing with branching. Serial.
//   Host parses command tokens into vlp_command struct.
//   Then dispatches appropriate GPU kernel if needed.

// Sampling (argmax, top-k, top-p) — HOST ONLY
//   Reason: single scan over vocab_size integers.
//   At vocab_size 32K: ~128 KB of data. CPU scans this in
//   microseconds. Not worth GPU dispatch overhead.
//   Exception: if vocab_size > 256K AND batch_size > 1,
//   a GPU top-k kernel may pay off. Decided at runtime.
```

---

# Section 6.7 — Host-Device Bridge (vlp_bridge)

```
// ============================================================
// The bridge manages all data movement between host and device.
// It decides: GPU dispatch or host execution?
// ============================================================

struct vlp_bridge {
    device: VulkanDevice,
    // Pipeline cache — all compute pipelines created at init
    llm_pipelines: vlp_llm_pipeline_set,       // ~12 kernel pipelines
    kb_pipelines: vlp_kb_pipeline_set,          // ~4 kernel pipelines
    prolog_pipelines: vlp_prolog_pipeline_set,  // ~4 kernel pipelines
    builtin_pipelines: [448]VkPipeline,         // one per builtin
    // Descriptor pool and sets
    descriptor_pool: VkDescriptorPool,
    // Staging buffers for host↔device data transfer
    staging_upload: VkBuffer,    // host-visible, for host→device
    staging_download: VkBuffer,  // host-visible, for device→host
    // Mapped pointers for direct access (if device supports)
    kb_store_mapped: ?*anyopaque,     // persistently mapped if possible
    fact_store_mapped: ?*anyopaque,
};

vlp_bridge_init(config: *vlp_system_config) -> vlp_status
  1. Create Vulkan instance, select physical device, create logical device.
  2. Allocate all storage buffers per vlp_device_memory_layout.
  3. Create all compute pipelines (compile all shader modules).
  4. Create descriptor pool, allocate descriptor sets.
  5. Allocate staging buffers.
  6. Attempt persistent mapping of KB/fact stores
     (VK_MEMORY_PROPERTY_HOST_VISIBLE_BIT | HOST_COHERENT_BIT).
     If device supports: direct read/write without staging.
     If not: use staging buffer copies.
  Side effects: Vulkan resources created.

vlp_bridge_dispatch_compute(pipeline: VkPipeline, descriptor_sets: [4]VkDescriptorSet, dispatch_x: i32, dispatch_y: i32, dispatch_z: i32, params: *anyopaque, params_size: i32) -> vlp_status
  1. Update dispatch_params uniform buffer with params.
  2. Record command buffer:
     a. Bind pipeline.
     b. Bind descriptor sets.
     c. Dispatch(dispatch_x, dispatch_y, dispatch_z).
     d. Pipeline barrier (compute write → compute read or host read).
  3. Submit command buffer.
  4. Wait on fence (synchronous) or return fence handle (async).
  Side effects: GPU work submitted.

vlp_bridge_read_results(buffer: VkBuffer, offset: i64, size: i64, dest: *anyopaque) -> vlp_status
  If buffer is persistently mapped: memcpy from mapped pointer.
  If not: record staging copy, submit, fence, memcpy from staging.
  Side effects: data copied to host.

vlp_bridge_should_use_gpu(operation: vlp_operation_type, data_size: i32) -> bool
  Heuristic (integer thresholds, not learned):
    LLM forward pass: always GPU (no question).
    Fact scan: GPU if scan_length > 256, host if <= 256.
    Unification: GPU if n_candidates > 32, host if <= 32.
    Rule matching: GPU if n_rules > 64, host if <= 64.
    Builtin on array: GPU if array_length > 512, host if <= 512.
    Text/grammar: always host.
    Access check: always host.
    Sampling: host unless vocab > 256K and batch > 1.
  Thresholds are configurable. Default values based on:
    GPU dispatch overhead ~10μs. CPU processes ~1 element/10ns.
    Crossover: ~1000 elements for compute-bound, ~256 for memory-bound.
  Returns bool. Caller respects the decision.
```

---

# Section 6.8 — Invariants — REVISED additions

```
// Additional invariants for the GPU compute model:

INVARIANT_11: GPU kernels are stateless.
  The same kernel dispatched with the same buffer contents produces
  the same buffer outputs. No kernel retains state between dispatches.
  All state is in storage buffers managed by the host.

INVARIANT_12: No recursion on GPU.
  Every GPU kernel uses bounded iteration only. Maximum iteration
  count is declared in dispatch_params and enforced by the kernel.
  Stack overflow is impossible because there is no stack.

INVARIANT_13: No dynamic allocation on GPU.
  Every buffer is pre-allocated by the host before any kernel dispatch.
  A kernel that needs temporary storage uses pre-allocated scratch buffers.
  Buffer exhaustion is detected by bounds checks and reported via
  status_buffer, not by runtime allocation failure.

INVARIANT_14: Host-device data is integer-identical.
  Data read back from GPU storage buffers is bit-identical to data
  written by GPU kernels. No format conversion. No precision loss.
  Integer bytes on GPU = integer bytes on host. Always.

INVARIANT_15: Dispatch overhead is bounded.
  Every GPU dispatch completes in bounded time for bounded input.
  No kernel contains an unbounded loop. Every loop has a maximum
  iteration count from dispatch_params or from data structure capacity.
  A kernel that cannot complete within its bounds writes an error
  to status_buffer and returns. It does not spin.
```
