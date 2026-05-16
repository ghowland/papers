# VDR-LLM-Prolog: Performance

## Integer Arithmetic on GPU Hardware: Why Wider Operands on More Cores Outrun Narrower Operands on Fewer Passes

**Registry:** [@HOWL-VDR-18-2026]

**Series Path:** [@HOWL-VDR-1-2026] → [@HOWL-VDR-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026]  → ... → [@HOWL-VDR-15-2026] → [@HOWL-VDR-16-2026] → [@HOWL-VDR-17-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** May 2026

**Domain:** Applied Philosophy / Computational Linguistics

**Supplementary Material:**

- `supplementary/gpu_integer_perf_tech_spec.md` — Full GPU technical specification

- `supplementary/gpu_integer_perf_tech_spec_llm_compacted.md` — LLM-compacted form

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6.

---

## Abstract

The VDR-LLM-Prolog system replaces floating-point arithmetic with exact integer computation. The immediate objection is performance: integer arithmetic on 100-digit numbers must be slower than hardware-accelerated floating-point on 16-bit or 32-bit values. This paper demonstrates that the objection confuses per-operation cost with per-prompt cost. A conventional language model spends thousands of tokens — each requiring a full forward pass through billions of floating-point parameters — on infrastructure work that VDR handles through exact primitive calls costing a few hundred integer operations each. VDR-15 established that the token reduction is 85 to 97 percent. This paper establishes that the integer arithmetic executing those primitives maps efficiently to GPU hardware, that the wider operands are offset by the massive parallelism of modern GPUs, and that several architectural properties of VDR — fixed-frame regularity, grammar-constrained decode, indexed knowledge base scans, and frontier-based Prolog execution — produce GPU utilization patterns that are structurally superior to the irregular, attention-dominated workloads of conventional language model inference. The complete GPU mapping is specified in the supplementary technical specification. This paper explains why it works, what the performance characteristics are, and where the actual bottlenecks lie.

---

## 1. The Performance Objection

Every discussion of exact arithmetic in language models encounters the same objection: it must be too slow. Floating-point arithmetic has decades of hardware acceleration. Modern GPUs contain thousands of cores optimized for 16-bit and 32-bit floating-point operations. Tensor cores perform matrix multiplications at throughputs measured in hundreds of teraflops. The entire hardware ecosystem — from chip design through compiler optimization through library implementation — is built around floating-point.

VDR replaces all of this with integer arithmetic on large numbers. A Q335 value — the standard representation in the VDR system, specified in VDR-1 through VDR-3 — has a numerator of approximately 100 decimal digits stored as a fixed-width vector of 11 unsigned 32-bit integers (352 bits total) or 6 unsigned 64-bit integers (384 bits total), with an implicit denominator of 2 raised to the power 335. Adding two Q335 values requires a limbwise addition with carry propagation across 11 limbs. Multiplying two Q335 values requires a full multi-precision multiplication producing a product of roughly 700 bits, followed by a split at bit 335 to extract the quotient and remainder. This is more work per operation than a single 16-bit floating-point multiply.

The objection is correct at the per-operation level. A single Q335 multiplication is slower than a single float16 multiplication. The question is whether per-operation cost determines per-prompt cost. VDR-15 established that it does not. A conventional language model spends 3,000 to 200,000 tokens on a single prompt, where each token requires a full forward pass through the model — matrix multiplications across every layer, full vocabulary softmax, the entire attention mechanism. VDR-LLM-Prolog spends 150 to 6,700 language model tokens on the same prompts, with the remainder handled by exact primitive calls that cost a few hundred integer operations each.

The relevant comparison is not one Q335 multiply versus one float16 multiply. It is the total computation cost of 210 language model tokens plus 500 primitive calls versus 3,000 language model tokens with no primitive offload. The per-operation cost of Q335 arithmetic is higher. The operation count is dramatically lower. The paper demonstrates that the lower operation count wins.

---

## 2. The GPU Mapping

The complete technical specification for mapping VDR-LLM-Prolog to GPU hardware is provided in the supplementary material. This section introduces the key architectural decisions and explains why they work.

The fundamental split is between a control plane on the CPU and a data plane on the GPU. The CPU handles everything that requires sequencing, string processing, or external interaction: parsing user input, resolving dotted paths to integer IDs, managing sessions, verifying grants, executing filesystem and network operations, scheduling GPU kernels, forming batches, making backtracking decisions, and assembling responses. The GPU handles everything that is parallel and numeric: integer arithmetic, knowledge base scans, term matching, unification, confidence propagation, grammar masking, language model forward pass and decode, and live-state mutation.

The boundary between CPU and GPU is integer IDs. All strings in the system — predicate names, atom values, path segments, grammar nonterminals, builtin names — are interned on the host side before any device transfer. Interning means each unique string is assigned a sequential integer identifier, and a lookup table maps identifiers back to strings. The GPU never processes a string. It compares integer symbol IDs. The string "salary" might be symbol 4,817. The string "bob" might be symbol 12,003. The GPU sees a fact as a tuple of integers: (kb_id: 47, pred_id: 4817, arg0: 12003, arg1: vdr_ref_9281). String resolution happens once on the CPU, is cached, and all subsequent operations use integers exclusively.

This design minimizes host-device transfer. A dotted path like root.org.acme.hr.personnel is parsed and resolved on the CPU to a single integer — say, KB ID 47. That integer is sent to the GPU. The GPU accesses KB 47's data through array indexing at offset 47 in the knowledge base metadata table. The entire path resolution, with all its string processing, happens once on the CPU. The GPU receives one 32-bit integer.

---

## 3. The Numeric Model

The system handles four classes of numeric values, each with its own representation and performance profile on GPU hardware.

The first class is small integers — signed 32-bit or 64-bit immediate values. These are used for knowledge base IDs, counter values, bitset words, term payloads, and any exact value that fits in a machine word. Operations on small integers use the GPU's native integer arithmetic units. There is no performance penalty compared to floating-point for these operations — integer add, multiply, compare, and shift are native GPU instructions at the same throughput as their floating-point counterparts.

The second class is Q335 fixed-frame closed values — the common case for exact arithmetic in the system. The denominator 2^335 is implicit and never stored. The numerator is stored as a fixed-width limb vector: 11 unsigned 32-bit words (352 bits, portable across all GPU architectures) or 6 unsigned 64-bit words (384 bits, optimized for GPUs with native 64-bit integer support). The sign is represented via two's complement, which makes addition, subtraction, and comparison regular operations without special case handling.

The third class is general closed rationals — values with explicit numerator and denominator limb references — used for values that don't fit the Q335 frame. These arise from parsing exact fractions from external sources or from cross-frame operations. They reference limb vectors in an append-only arena.

The fourth class is active VDR values — triples where the remainder is not zero. These carry a top-level value and denominator reference plus a remainder tag and payload reference. The remainder payload can be an atomic integer, a composite structure with child VDR values, or a functional remainder descriptor. Active values are the minority case — the system is designed so that most values stay in Q335 closed form, with active spills occurring only when operations exceed what the frame can represent.

The performance strategy is built on the assumption that Q335 closed values dominate. The supplementary specification defines three spill thresholds: below 1 percent active values, the system uses dense closed storage with sparse spill tags; between 1 and 10 percent, it uses tile-local spill tables; above 10 percent, it switches to sparse active mode or escalates to host intervention. The VDR-14 paper's characterization of denominator growth during training — plateauing around 2^45 with small learning rates — confirms that Q335's 2^335 frame provides enormous headroom. Most values never leave the fast closed path.

---

## 4. Q335 Arithmetic on GPU

The three primary Q335 operations — addition, multiplication, and comparison — each map to efficient GPU execution patterns.

Addition of two Q335 values is limbwise addition with carry propagation. Each of the 11 limbs (in the 32-bit layout) is added with the carry from the previous limb. This is 11 integer additions with 11 carry checks — roughly 22 integer operations total. On a GPU, this executes in a single thread in a few dozen clock cycles. For bulk operations — adding vectors of Q335 values, summing arrays, computing residuals — thousands of additions execute in parallel across GPU cores. The operation is perfectly regular: every addition has exactly the same shape, the same number of limbs, the same carry propagation pattern. GPU hardware achieves peak utilization on regular uniform workloads.

Multiplication of two Q335 values is a multi-precision multiply producing a full product of approximately 700 bits, followed by a split at bit position 335. The split is a fixed-position operation: the bits above position 335 become the quotient (the new V), the bits below become the remainder. If the remainder is zero, the result is closed and stays in the fast Q335 path. If nonzero, the result becomes an active node with the remainder stored in the append-only arena.

The multiplication itself can use schoolbook multiplication (11  $\times$  11 = 121 limb-by-limb multiplies with accumulation) for the standard case, with optional Karatsuba or Toom-Cook algorithms for larger operands. Schoolbook on 11 limbs produces roughly 200 integer operations — multiplies, adds, and carry propagations. This is more expensive than a single float16 multiply (one operation) by a factor of roughly 200. But this factor is the per-operation cost. The relevant question is how many of these multiplications occur per prompt compared to how many float operations a conventional forward pass requires.

A conventional language model forward pass for one token through a model with 7 billion parameters requires roughly 14 billion floating-point operations — two operations per parameter (multiply and accumulate) across the forward pass. Generating 3,000 tokens requires roughly 42 trillion floating-point operations.

A VDR prompt with 210 language model tokens requires roughly 2.94 trillion exact integer operations for the forward passes (same 14 billion per token, but with wider integer operands increasing the per-operation cost by roughly the 200 $\times$  factor, giving approximately 2.8 trillion effective operations for 210 tokens). The 500 primitive calls add perhaps 100,000 Q335 operations — negligible in comparison.

The conventional system does 42 trillion float operations. The VDR system does roughly 2.94 trillion integer operations, where each integer operation is wider but the total operation count is 14 $\times$  lower. The question becomes: can a GPU execute 2.94 trillion wide integer operations faster than 42 trillion narrow float operations? The answer depends on GPU utilization patterns, which the next sections address.

---

## 5. Why GPU Utilization Favors VDR

Modern GPUs achieve peak performance only when their thousands of cores are uniformly occupied with the same operation on different data. Any divergence — threads taking different code paths, threads waiting for memory at different times, threads idle while others work — reduces utilization. The utilization characteristics of VDR workloads are structurally different from conventional language model inference in ways that favor VDR.

Conventional language model inference has an irregular utilization profile. The attention mechanism requires a softmax computation that is inherently sequential within each row — the exponentials must be computed, summed, and normalized before the weighted sum can proceed. The softmax itself requires a max reduction (sequential), exponentiation of each element (parallel but transcendental — requiring multiple operations per element through lookup tables or polynomial approximation), a sum reduction (sequential), and a division (parallel). The transcendental operations are the most expensive: computing exp(x) in floating-point requires a range reduction, polynomial evaluation, and reconstruction, typically costing 10 to 20 floating-point operations per element. For a vocabulary softmax over 50,000 elements, this is 500,000 to 1,000,000 floating-point operations just for the exponentials.

VDR's rational surrogate softmax replaces all of this with integer arithmetic. The formula is: each output equals the square of the shifted input divided by the sum of all squared shifted inputs. The computation is: find the row maximum (parallel reduction on integers), subtract the maximum and add a shift constant (parallel), square each element (one Q335 multiply each, parallel), sum the squares (parallel reduction), divide each squared element by the sum (one Q335 divide each, parallel). Every step is uniform integer arithmetic. There are no transcendentals. No lookup tables. No range reductions. No polynomial approximations. The GPU cores execute the same operation on every element with no divergence.

Knowledge base scans in VDR are structurally regular. Facts are stored in predicate-major columnar form — all facts with the same predicate are contiguous in memory. A query for predicate "salary" with argument "bob" becomes: load the predicate bucket for symbol 4817 (salary), scan the argument column for symbol 12003 (bob), produce a bitmask of matches. This is a parallel filter scan — one of the most efficient operations a GPU can perform. Thousands of facts are checked simultaneously, one per core, with uniform memory access patterns (contiguous reads from columnar arrays) and uniform computation (integer comparison per element).

Conventional language model inference has no equivalent to these bulk scan operations because it has no structured data to scan. Everything is in the weight matrices, accessed through matrix multiplication, which is efficient but serves a different purpose — statistical pattern matching rather than exact indexed lookup.

Grammar-constrained decode in VDR further improves utilization. When a grammar declares that the next token must be one of four enum values, the decode step constrains the vocabulary to those four candidates. The softmax (or rational surrogate) computes over 4 values instead of 50,000 or more. This is a 12,500 $\times$  reduction in decode computation for that token. Conventional language model inference must compute the full vocabulary softmax on every token because it has no structural constraint on what the next token can be. VDR's grammar system provides these constraints as a structural property of the output format, reducing decode cost on every structurally determined token.

---

## 6. Knowledge Base Operations on GPU

The knowledge base is the system's primary data structure — every fact, rule, constraint, connection, and piece of metadata lives in knowledge bases organized as a tree. The GPU mapping stores knowledge base data in structure-of-arrays columnar form, which aligns with how GPU hardware accesses memory.

A GPU accesses memory most efficiently in coalesced patterns — adjacent threads reading adjacent memory locations. Structure-of-arrays achieves this naturally. When 1,000 threads each need to check whether their candidate fact's kb_id is in the visible set, they read 1,000 consecutive kb_id values from a contiguous array. This is one coalesced memory transaction. In an array-of-structures layout, the kb_id fields would be scattered across memory at struct-width intervals, causing multiple memory transactions to fetch the same 1,000 values.

Fact storage is predicate-major. All facts sharing a predicate are stored in a contiguous bucket. The bucket is indexed by predicate ID — an integer lookup that gives the offset and count of facts for that predicate. A query for all salary facts starts with one index lookup to find the salary bucket, then scans within the bucket. If the bucket has 500 facts, 500 GPU threads scan 500 facts in parallel in one memory transaction per column checked.

The scope filter is where VDR's structural access control meets GPU execution. Every query must check that returned facts come from knowledge bases visible in the user's scope chain. The supplementary specification defines three strategies for this filter. The simplest uses a bitset: the user's visible KB IDs are set in a bitset, and each thread checks its candidate fact's kb_id against the bitset with a single bit-test operation. For larger trees, DFS in/out intervals are used: each knowledge base has a pre-computed interval representing its position in a depth-first traversal of the tree, and checking whether a KB is in a subtree is an interval containment test — two integer comparisons. The scope filter adds one or two integer operations per candidate fact per query. Visibility checking — the core of VDR's structural safety — costs almost nothing on GPU hardware.

This is a performance property that directly connects to VDR-16's safety claims. Structural access control through visibility checks and scope filtering is not only more secure than behavioral safety — it is cheaper. A behavioral safety check requires the language model to evaluate the request through its full forward pass, spending tokens on classification and potential refusal. A structural visibility check is one bit-test per candidate fact, executed in parallel across thousands of facts in a single GPU kernel launch.

---

## 7. Prolog on GPU

The Prolog engine is the logic layer of VDR-LLM-Prolog — it evaluates rules, performs unification, and produces derivation results with provenance. Conventional Prolog implementations use recursive depth-first search with backtracking, which is fundamentally incompatible with GPU execution. Recursive control flow causes thread divergence: each thread follows a different branch of the search tree, executing different code at each step, making GPU utilization collapse.

The supplementary specification transforms Prolog execution into frontier-based batched joins — a technique borrowed from GPU database query processing. The transformation works as follows.

A Prolog query starts with a goal: find all facts matching a predicate with certain argument patterns. The first step is candidate retrieval — load the predicate bucket and produce a list of candidate facts. This is a parallel indexed scan, identical to the knowledge base operations described in the previous section.

The second step is term compatibility filtering. Each candidate fact's arguments are checked against the goal's argument patterns. An atom argument in the goal matches only facts with the same atom (integer symbol comparison). A variable argument matches any fact (no check needed). A VDR argument matches facts with equal VDR values (cross-multiplication comparison). This is a parallel filter: each GPU thread evaluates one candidate fact against the goal pattern, producing a pass/fail bitmask.

The third step is unification. For candidates that passed the filter, variable bindings are produced. If the goal had variable ?X in the first argument position and candidate fact 47 has atom "bob" in that position, the binding ?X = bob (symbol 12003) is recorded. The unification kernel takes the goal, the filtered candidate range, the term pool, and any existing bindings from earlier in the query, and produces extended binding rows — one per successful unification. This is parallel: each thread unifies one candidate, producing one binding row or marking failure.

The fourth step is rule body evaluation. If the query matched a rule head rather than a fact, the rule's body goals must be evaluated with the bindings from the head match. This is where the join model applies. Each body goal is another query, and the binding rows from the previous goal become the input for the next. This is a join: the binding frontier from goal one is joined with the candidate facts for goal two, producing an extended frontier for goal three, and so on.

The join strategies from database query processing apply directly. Hash join works when the join key is an equality condition — build a hash table on the smaller frontier, probe with the larger. Sort-merge join works for large frontiers — sort both sides by join key, merge. Bitmap semijoin works for unary filters — build a bitmap from one side, filter the other. Each of these is a well-studied GPU operation with known performance characteristics and optimized implementations.

For deterministic first-solution queries, the GPU computes all solutions in parallel and the CPU selects the first by canonical ordering. This is slightly more work than strictly necessary (a sequential system would stop at the first solution), but it maintains GPU utilization — all threads do useful work, and the selection is a trivial CPU operation on the completed result set.

The performance characteristic of frontier-based Prolog is that it converts recursive branching control flow into flat parallel data operations. The GPU never branches. It scans, filters, unifies, and joins — all uniform parallel operations on arrays of integers. Thread utilization stays high because every thread does the same thing. The work is proportional to the frontier size (number of candidate bindings) times the number of body goals, not to the depth of the search tree.

---

## 8. The Forward Pass

The language model forward pass in VDR uses the same computational structure as a conventional transformer — embedding lookup, attention computation, feedforward blocks, residual connections, and output projection — but with Q335 exact integer arithmetic instead of floating-point.

The supplementary specification defines three tensor storage classes for exact values. The primary class, T0, stores dense shared-frame tensors: all entries share the implicit Q335 denominator, and the numerators are stored as contiguous arrays of limb vectors. This is the highest-throughput path because every entry has the same width and the same implicit denominator, making operations perfectly regular. A matrix multiplication of two T0 tensors is a multi-precision integer matrix multiply where each element accumulation is a sequence of Q335 multiply-and-add operations.

The T1 class adds per-entry spill tags for tensors where some entries have exceeded the Q335 frame and become active values. The dense layout is preserved for the closed entries, with spill entries referencing the active value arena. The T2 class handles the rare case where active values exceed 10 percent of the tensor — sparse active storage with coordinates or tile-local spill lists.

Embedding lookup is an indexed read from a T0 tensor — token IDs index into rows of Q335 limb vectors. This is identical in structure to floating-point embedding lookup, just with wider entries.

Attention uses the rational surrogate softmax rather than the transcendental exponential softmax. The rational surrogate computes each attention weight as the square of a shifted input divided by the sum of all squared shifted inputs. It produces weights that sum to exactly one — not approximately, but exactly, verified by the fraction one over one. It preserves monotonicity: higher logits produce higher weights. It produces exactly equal weights for equal logits. And it uses zero transcendental operations — only integer subtraction, squaring, summing, and division.

The feedforward block uses ReLU activation — piecewise linear, producing exact zero or exact passthrough. No approximations, no lookup tables, no polynomial fits. The computational cost of ReLU is one comparison per element (is it negative?) and one conditional copy. On GPU, this is a single instruction per element with no divergence in the common case.

The gradient path for training stores the backward computation graph as flat GradNode records — each recording the operation type, arity, input references, output reference, and auxiliary data. The records are topologically sorted so that backward propagation is a sequential scan through the sorted array, with each operation's gradient kernel dispatched in batch by operation type. Exact per-operation kernels compute exact gradients — the derivative of x squared at x equals three is exactly six, not 6.0000000001.

---

## 9. Grammar-Constrained Decode

The grammar system's performance impact on decode is substantial and has no equivalent in conventional language model inference.

In conventional inference, every generated token requires a softmax over the full vocabulary — typically 50,000 to 100,000 entries. Each entry requires an exponentiation (10 to 20 floating-point operations), the results must be summed (one reduction), and each entry must be divided by the sum (one division per entry). Total cost per token: roughly 500,000 to 2,000,000 floating-point operations for the softmax alone, on top of the forward pass computation that produced the logits.

In VDR, the grammar system specifies what the next token can be based on the output format structure. When the grammar declares that the current position is an enum slot with four legal values, the decode constrains to those four candidates. The surrogate softmax computes over 4 values: 4 subtractions, 4 squarings (each a Q335 multiply), one sum of 4 values, 4 divisions. Total: roughly 20 Q335 operations, where each Q335 operation is roughly 200 integer operations, giving roughly 4,000 integer operations. Compare to 500,000 to 2,000,000 float operations for the unconstrained softmax.

The supplementary specification describes the mechanism. Each decode stream carries a grammar state: grammar ID, state ID, slot type, and a candidate begin/count pair pointing into a candidate buffer. When the slot type is a categorical enum, the candidates are the enum's token IDs. When the slot type is a KB identifier reference, the candidates are the token IDs of identifiers in the relevant knowledge base. When the slot type is a builtin opcode, the candidates are the roughly 300 opcode name tokens. When the slot type is free text, the full vocabulary is available.

The GPU kernel builds a vocabulary mask from the candidate set. For small candidate sets (the common case for structural tokens), this is trivial — set a few bits in a mask. For KB identifier references where the candidate set might be 200 items, it is still a small fraction of the full vocabulary. The mask is applied to the logit vector before the surrogate softmax, zeroing out impossible candidates.

The savings compound across a response. VDR-15 established that 40 to 60 percent of tokens in structured output are structural — pipes, headers, delimiters, enum values, type tags. Each structural token has a constrained candidate set, typically between 2 and 20 items. If half the tokens in a 200-token response are grammar-constrained to an average of 10 candidates, that is 100 tokens decoded at 10-candidate cost instead of 50,000-candidate cost — a 5,000 $\times$  reduction in decode computation for half the response.

---

## 10. Concurrent Execution

The supplementary specification defines five concurrent GPU streams that execute simultaneously during each conversational turn. The streams are: LLM forward pass and decode (stream 0), knowledge base query and predicate scan (stream 1), VDR primitive execution (stream 2), grammar mask and candidate preparation (stream 3), and provenance and event compaction (stream 4). The CPU manages the dependency graph, launch ordering, external operations, and path resolution.

The turn pipeline has eleven steps. The host parses the request and resolves paths and scope (CPU). The GPU prefetches scoped facts and rules into fast memory (stream 1). The LLM begins decode (stream 0). When a command token is emitted, the host lowers it to an opcode batch (CPU), and the GPU executes pure queries and primitives (streams 1 and 2) while grammar masks update (stream 3). Results flow to the scratchpad or knowledge base. The LLM continues with structured state. Provenance events are committed (stream 4). The host assembles the response.

The concurrent execution model means that knowledge base queries, primitive execution, grammar preparation, and provenance logging happen in parallel with the LLM forward pass. In a conventional system, the language model does everything sequentially — it generates tokens one at a time, with each token requiring the full forward pass before the next can begin. In VDR, the LLM generates a command token (8 tokens), then the GPU executes the commanded operation in parallel with the LLM preparing to assess the result. The primitive execution is overlapped with LLM computation rather than serialized through the token stream.

This concurrency is possible because the operations are independent. A knowledge base query reads from indexed fact tables. A VDR primitive computes on value references. The LLM decode processes its own attention and feedforward computations. These access different memory regions and use different computational units. The GPU's stream model allows them to execute simultaneously on different portions of the GPU's core array.

---

## 11. Memory and Allocation

GPU performance depends critically on memory management. The conventional approach — general-purpose malloc for dynamic allocation — is catastrophic on GPU hardware. Malloc requires synchronization, causes fragmentation, and produces irregular memory access patterns that defeat coalescing.

The supplementary specification uses append-only arenas for all irregular objects. An arena is a contiguous block of GPU memory with a bump pointer. Allocation is one atomic increment of the pointer — no synchronization beyond the atomic, no fragmentation, no free-list traversal. Every irregular structure in the system — limb vectors, VDR nodes, remainder payloads, child lists, term structures, binding rows, provenance events, live-state deltas — allocates from arenas.

The allocation model has two tiers. A global bump allocator handles large arena segments. Per-block suballocators carve small allocations from block-local arena segments using shared memory, which is the fastest memory tier on GPU. For operations where allocation size is predictable — a batch of 1,000 unification results where each produces a fixed-size binding row — a prefix-sum computes the offsets before any allocation occurs, enabling perfectly regular contiguous allocation with no synchronization.

The arena model produces coalesced memory access by construction. Objects allocated in sequence are stored in sequence in memory. When GPU threads process these objects in order — which the frontier-based Prolog execution ensures by construction — adjacent threads access adjacent memory, which is the optimal pattern for GPU memory controllers.

Arenas grow monotonically during a session. Dead objects (retracted facts, expired bindings, superseded provenance entries) are not immediately freed. Periodically — between turns or during idle time — the host or a maintenance kernel compacts arenas: live objects are copied to a fresh arena, dead regions are reclaimed, indexes are rebuilt, and handles are remapped. Session-visible handles (those referenced by user-accessible facts or primitive results) are stable across compaction through an indirection table.

---

## 12. Live State on GPU

The eight data primitive types from VDR-8 — counters, locks, queues, stacks, LRU caches, ring buffers, and bitsets — each have GPU-efficient implementations.

Counters are dense arrays of signed integers, one per counter in the active session. Incrementing a counter is one atomic integer addition. Checking a counter against a bound is one integer comparison. A batch of 100 counter increments — checking 100 dependencies in a codebase migration, for example — is 100 parallel atomic increments in a single kernel launch. The violation flag is set by a parallel comparison kernel after the increment batch.

Bitsets are packed 64-bit words. Setting, clearing, and testing bits are single bitwise operations — OR to set, AND-NOT to clear, AND to test. A bitset representing which of 256 evidence dimensions have been covered is 4 words. Testing all dimensions is 4 parallel word operations.

Ring buffers are fixed-capacity arrays with an atomic write position. Writing a metric snapshot to a 90-entry ring buffer is one atomic increment of the write position followed by one write to the computed index. Reading the full buffer is a contiguous memory read of 90 entries — one coalesced transaction.

Queues and stacks use batched push and pop operations. Single-item contended operations (multiple threads trying to push or pop simultaneously) are host-assisted or block-local, because fine-grained contention defeats GPU parallelism. Batched operations — push 50 items to a queue, pop the top 20 from a stack — are efficient: one prefix-sum for offsets, one bulk copy for the data.

LRU caches are the most complex case. Exact LRU ordering requires tracking access times and evicting the oldest entry, which involves sorting or heap operations. The supplementary specification recommends host-managed exact LRU for correctness-critical caches, with device-side approximate LRU (batched timestamped cache with periodic host reorder) for high-throughput caches where exact ordering is not critical.

---

## 13. Provenance on GPU

Every primitive execution and every rule derivation in the system produces a provenance event. The event records what was computed, by which tool, with what inputs, producing what output, at what confidence, on which turn. The supplementary specification stores these as an append-only structure-of-arrays log: event_type, tool_id, subject_ref, input_begin, input_count, output_ref, confidence_ref, turn.

Appending provenance events is concurrent with the computation that produces them. Each GPU block executing primitive operations appends its provenance events to a block-local buffer. After the kernel completes, the block-local buffers are compacted into the global provenance log with a single parallel copy operation.

The provenance log grows monotonically. It is never edited — events are append-only. This is the structural basis for the audit trail described in VDR-16: every data access, every computation, every primitive execution is logged. The append-only property means the log cannot be retroactively modified. The GPU's append model — atomic bump pointer plus bulk copy — makes this logging essentially free in performance terms. The cost is memory, not computation.

Deterministic ordering of provenance events requires attention. GPU execution is inherently parallel, and the order in which blocks complete is nondeterministic. The supplementary specification addresses this with canonical ordering: events are stamped with (turn, batch_sequence, item_sequence) and either appended in canonical batch order or post-sorted by these keys. The sort is a single parallel radix sort on the event buffer — a well-optimized GPU primitive.

---

## 14. Sessions, Snapshots, and Clones on GPU

The session model from VDR-8 separates persistent state (facts, rules, constraints, connections, grammars) from live state (counters, locks, queues, stacks, caches, ring buffers, bitsets, scratchpad, working data). This separation maps efficiently to GPU memory management.

A session snapshot captures all live state. On GPU, this means capturing the current arena positions for each live-state type and copying the live data to a snapshot buffer. The supplementary specification defines a SnapshotHeader containing the session ID plus begin/count pairs for each live-state type. Snapshot size is small — VDR-16 Appendix I established that a typical incident investigation's complete live state is roughly 21 kilobytes. Copying 21 kilobytes on a GPU with hundreds of gigabytes per second of memory bandwidth takes microseconds.

Cloning a session uses copy-on-write over persistent state and duplicates live-state references with new delta arenas. The persistent stores — fact tables, rule tables, constraint tables — are shared between all clones because they are read-only from the clone's perspective (new assertions go into the clone's delta arena, not into the shared persistent store). The live state — counters, caches, queues — is duplicated because each clone mutates independently.

Reset discards the clone's live-state deltas and restores the snapshot baseline references. Kill invalidates the clone's live-state references but preserves any persistent assertions the clone committed — facts asserted to persistent knowledge bases survive the kill because they are in the shared persistent store, not in the clone's delta arena.

The disposable clone pattern from VDR-8 — spawning worker clones, killing them when they drift, respawning from a frozen snapshot — is cheap on GPU. Clone creation is one arena allocation plus one small memory copy. Clone death is one arena invalidation. The persistent knowledge base grows monotonically across clone lifetimes, accumulating exact provenance-tagged facts while the language model stays fresh.

---

## 15. The Actual Bottlenecks

The system has genuine performance bottlenecks. Identifying them honestly is more useful than claiming universal superiority.

The language model forward pass with Q335 arithmetic is the primary bottleneck. Matrix multiplication with 352-bit operands is wider than float16 matrix multiplication by a factor of 22 in operand width. The actual slowdown depends on the multiplication algorithm and GPU integer throughput, but a reasonable estimate is that Q335 matrix multiplication is 100 to 500 times slower per element than float16 matrix multiplication. For the LLM forward pass, which is dominated by matrix multiplications, this is the main cost.

However, VDR-15 established that the VDR system generates 85 to 97 percent fewer LLM tokens than a conventional system for the same tasks. The forward pass cost per token is higher, but the number of tokens is dramatically lower. At 95 percent token reduction, the VDR system executes 5 percent as many forward passes, each roughly 200 $\times$  more expensive per element, giving a total forward pass cost of roughly 10 $\times$  the conventional system. This is slower in absolute terms for the LLM component.

The offsetting factor is that the conventional system's 3,000 tokens include massive amounts of infrastructure work that produces no value — arithmetic through digit prediction, state reconstruction, formatting, hedging. The VDR system's 210 tokens are almost entirely judgment and prose — the high-value output that the user actually wants. The user waits longer per token but waits for fewer tokens, and every token they receive is useful rather than infrastructure.

The second bottleneck is active value management. When values exceed the Q335 frame and produce active remainders, the append-only arena grows, normalization passes become necessary, and the regular fixed-width computational path is interrupted by irregular remainder structures. The normalization pipeline — mark active roots, normalize leaves in parallel, compact upward, canonically order — is well-designed for GPU execution but still more expensive than closed-value operations. The performance strategy is to keep active spill rates below 1 percent through appropriate Q335 frame sizing and Q-basis reprojection.

The third bottleneck is Prolog execution on large knowledge bases. Frontier-based joins are efficient for moderate frontier sizes, but very large frontiers (thousands of candidate bindings joined across multiple body goals) produce proportionally large intermediate results. The join strategies (hash join, sort-merge, bitmap semijoin) are all proven GPU operations, but the total work scales with the product of frontier sizes across join steps. For typical VDR queries — scoped to a subtree, filtered by predicate bucket, constrained by visibility — frontier sizes are moderate. For pathological queries (unrestricted cross-scope scans with highly variable predicates), frontier explosion is possible.

The fourth bottleneck is host-device synchronization. Every command token the LLM emits requires the host to resolve paths, verify grants, and lower the command to GPU opcodes. This is a round trip across the host-device boundary. The supplementary specification mitigates this by overlapping LLM decode with primitive execution through concurrent GPU streams, but the synchronization points at command token boundaries remain.

---

## 16. Comparative Analysis

The honest comparison between conventional float-based LLM inference and VDR integer-based inference requires separating the workload into components and comparing each.

For the LLM forward pass in isolation, conventional floating-point is faster per token. Float16 tensor cores achieve peak throughput that Q335 integer arithmetic cannot match on current hardware, because the hardware was designed for float16. The VDR system pays a per-token penalty of roughly 100 $\times$  to 500 $\times$  on the forward pass. This is the real cost of exact arithmetic on hardware optimized for approximate arithmetic.

For knowledge base operations, VDR is faster. A conventional LLM has no structured data operations — everything is in the weights, accessed through the forward pass. VDR's indexed predicate scans, scope filters, and connection traversals are standard GPU database operations executing at millions of facts per second. A query that would cost a conventional LLM hundreds of tokens of attention-based "searching" through its context window is one indexed GPU scan in VDR.

For Prolog evaluation, VDR has capability that conventional LLMs lack entirely. Logical deduction through token prediction is unreliable and scales poorly with chain length. Frontier-based Prolog on GPU is exact, provenance-tracked, and scales with frontier size rather than chain depth.

For decode, VDR is dramatically faster on structured output. Grammar-constrained decode over small candidate sets is orders of magnitude cheaper than full-vocabulary softmax. For free-text output, VDR uses the surrogate softmax which avoids transcendentals but still computes over the full vocabulary, giving roughly comparable cost.

For primitive execution, VDR replaces thousands of LLM tokens with hundreds of integer operations. Sorting 500 items is one GPU sort kernel — roughly 500  $\times$  log₂(500)  $\times$  200 integer operations for Q335 comparisons, totaling roughly 900,000 operations, equivalent to less than one LLM token. A conventional LLM generates hundreds of tokens to sort the same list through prose comparison.

For provenance and confidence, VDR adds cost that conventional systems don't have — but the cost is small (one provenance event per operation at append-only arena cost, confidence propagation as parallel integer reductions) and the value is substantial (every result is auditable and carries computed confidence).

The total system comparison depends on the workload. For workloads dominated by free-text generation (writing a novel, composing a poem), the conventional system is faster because the forward pass dominates and grammar constraints provide little benefit. For workloads involving structured data, computation, state management, and multi-turn reasoning (SRE incidents, portfolio analysis, research synthesis, code migration), VDR is faster in total wall-clock time despite the slower forward pass because it generates 85 to 97 percent fewer tokens and replaces the rest with structurally efficient GPU operations.

---

## 17. Hardware Trajectory

Current GPU hardware is optimized for floating-point. Integer throughput is a secondary consideration in GPU design, driven primarily by address computation and index arithmetic rather than computational workloads. The performance gap between Q335 integer arithmetic and float16 tensor core arithmetic reflects this design emphasis, not any fundamental computational limitation.

Integer arithmetic on GPU is not slow in absolute terms. A modern GPU can perform billions of 32-bit integer operations per second. Q335 arithmetic, at roughly 200 integer operations per multiply, achieves millions of Q335 multiplications per second on current hardware. This is sufficient for the VDR workload where the LLM generates 210 tokens per prompt and primitive calls number in the hundreds.

The trajectory favors wider integers. GPU integer ALU widths have expanded with each generation. Support for 64-bit integers is now standard. Specialized instructions for multi-precision arithmetic (carry-propagating adds, wide multiplies) appear in some architectures. If exact arithmetic workloads create market demand, hardware designers can add integer tensor cores — fixed-function units for multi-precision integer matrix multiplication — that would close the per-operation gap with floating-point tensor cores. This is an engineering decision, not a physics limitation.

The more significant trajectory is the token reduction. As the grammar, knowledge base, and primitive systems mature, the fraction of work handled by exact primitives rather than LLM token generation will increase. Every new grammar template, every new Prolog rule composition, every new knowledge base schema reduces future LLM token cost. The system gets more efficient with use because the structural components accumulate while the LLM cost per structural operation stays constant at roughly 8 tokens per command.

---

## 18. What This Means for Real Workloads

For the SRE incident investigation from VDR-15: 210 LLM tokens plus 500 primitive calls. The 210 tokens cost roughly 210  $\times$  200 = 42,000 token-equivalent operations at the Q335 slowdown factor (versus 3,000  $\times$  1 = 3,000 token-equivalent operations for the conventional system). VDR's forward pass is roughly 14 $\times$  more expensive in total. But the primitive calls — fetching metrics, parsing JSON, filtering time series, computing correlations, evaluating Prolog rules, propagating confidence — add roughly 100,000 Q335 operations, equivalent to 0.05 token-equivalent operations at the 2-billion-ops-per-token scale. The primitives are computationally invisible.

Wall-clock time: if the conventional system takes 30 seconds to generate 3,000 tokens, VDR takes roughly 3 seconds for 210 LLM tokens (token generation is roughly proportional to token count, with wider arithmetic partially offset by grammar-constrained decode savings) plus sub-second for all primitive execution. Total roughly 4 seconds versus 30 seconds. The user gets a faster response that is also exact, provenance-tagged, and auditable.

For the 20-turn investigation: the conventional system's per-turn cost escalates because each turn re-processes growing context through attention. By turn 20, context is roughly 60,000 tokens and each turn takes proportionally longer. VDR's per-turn cost is flat — state is in knowledge bases, not the context window. Turn 20 costs the same as turn 1. Over 20 turns, the conventional system's total time might be 10 minutes with degrading quality. VDR's total time might be 80 seconds (20  $\times$  4 seconds) with constant quality and accumulating knowledge.

For the financial portfolio analysis: 500 Q335 multiplications (position values), 500 Q335 additions (portfolio sum), correlation matrix computation (roughly 125,000 Q335 operations for 500  $\times$  500 pairwise correlations). Total: roughly 126,000 Q335 operations. At millions of Q335 operations per second on GPU, this completes in well under one second. The conventional LLM cannot perform the task at all — 500 positions exceed context capacity and digit-by-digit arithmetic through token prediction would take thousands of tokens.

For academic grading: 150 essays, each requiring LLM judgment at 300 tokens per essay. The LLM cost is 45,000 tokens regardless of system because this is irreducible judgment work. But the statistical analysis — computing means, variances, percentiles, standard deviations across 150 students and multiple criteria — is pure Q335 arithmetic. A few thousand Q335 operations, completing in milliseconds on GPU. The conventional system cannot compute these statistics at all.

The pattern across all workloads: the LLM forward pass is slower per token on VDR, but the total LLM workload is 85 to 97 percent smaller, and the primitive and knowledge base workload that replaces it executes at GPU-parallel speed. The workloads where VDR is slower are those dominated by free-text generation with no structural component. The workloads where VDR is faster — often dramatically faster — are those involving data, computation, state management, and structured reasoning, which are precisely the professional workloads where accuracy and provenance matter most.

---

## Appendix A: Q335 Operation Cost

### A.1: Per-Operation Integer Cost

| Operation | Q335 Integer Ops | float16 Ops | Ratio | GPU Parallelism | Effective Throughput Ratio |
|---|---|---|---|---|---|
| Addition | ~22 (11 limb adds + carries) | 1 | 22 $\times$  | Full — uniform work per element | ~22 $\times$  slower per element, same utilization |
| Subtraction | ~22 (11 limb subs + borrows) | 1 | 22 $\times$  | Full | ~22 $\times$  |
| Multiplication | ~200 (schoolbook 11 $\times$ 11 + accumulate) | 1 | 200 $\times$  | Full — uniform work per element | ~200 $\times$  slower per element |
| Comparison | 2-22 (fast path to full limb scan) | 1 | 2-22 $\times$  | Full | 2-22 $\times$  average |
| Division (by Q335) | ~400 (multiply + shift + remainder) | 1 | 400 $\times$  | Full | ~400 $\times$  |
| Surrogate softmax (per element) | ~220 (sub + square + div) | ~15 (exp + div) | 15 $\times$  | Full — no transcendentals | ~15 $\times$  slower but no divergence |
| ReLU | 2 (compare + conditional copy) | 2 | 1 $\times$  | Full | Identical |
| Bit test (scope check) | 1 | N/A | — | Full | No conventional equivalent |
### A.2: Per-Token Forward Pass Cost

| Component | Conventional (float16) | VDR (Q335 integer) | Ratio | Notes |
|---|---|---|---|---|
| Embedding lookup | 1 read per dim | 11 reads per dim (limb width) | 11 $\times$  | Memory-bound; limb width increases bandwidth |
| Attention QK^T | d k multiplies per position pair | d k  $\times$  200 int ops per pair | 200 $\times$  | Dominated by multiplication cost |
| Softmax / Surrogate | ~15 ops per element (transcendental) | ~220 ops per element (integer) | 15 $\times$  | VDR avoids transcendental divergence |
| Value mixing | d v multiplies per position | d v  $\times$  200 int ops per position | 200 $\times$  | Same structure, wider operands |
| Feedforward (ReLU) | 2 ops per element | 2 ops per element | 1 $\times$  | Identical — piecewise linear |
| Feedforward (linear) | d ff multiplies | d ff  $\times$  200 int ops | 200 $\times$  | Dominated by multiplication |
| Layer norm / rational scaling | ~10 ops per element | ~25 ops per element | 2.5 $\times$  | VDR avoids sqrt; uses mean absolute value |
| **Total per token** | **~14B float ops** | **~14B  $\times$  ~150 avg factor** | **~150 $\times$ ** | Weighted average across components |
Per-token cost is roughly 150 $\times$  higher. But token count is 85-97% lower. Net system cost depends on workload composition.

---

## Appendix B: Token Count vs Operation Count

### B.1: SRE Incident Investigation (Single Turn)

| Category | Conventional | VDR | Notes |
|---|---|---|---|
| LLM tokens generated | 3,000 | 210 | 93% reduction |
| Forward pass ops per token | 14B float | 14B  $\times$  150 = 2.1T int | Per-token cost higher |
| Total forward pass ops | 42T float | 441T int | VDR forward pass ~10.5 $\times$  more total ops |
| Primitive call ops | 0 (no primitives) | ~100K Q335 ops = ~20M int | Computationally invisible |
| KB query ops | 0 (attention-based search) | ~50K int ops (scans + filters) | GPU-parallel, sub-millisecond |
| Prolog evaluation ops | 0 (prose reasoning) | ~10K int ops (unification + join) | GPU-parallel, sub-millisecond |
| Formatting ops | 0 (all generated tokens) | 0 (grammar-provided) | VDR: zero cost; conventional: ~600 tokens |
| Confidence computation | 0 (hedging tokens) | ~500 int ops | One VDR multiply per propagation step |
| Provenance logging | 0 (no provenance) | ~5K int ops (append events) | Append-only, negligible |
| **Total computation** | **42T float** | **~441T int + ~25M int** | VDR: more total int ops for forward pass, negligible for everything else |
### B.2: 20-Turn Investigation

| Turn | Conventional Forward Pass Ops | Conventional Attention Ops | VDR Forward Pass Ops | VDR Primitive + KB Ops | VDR Total |
|---|---|---|---|---|---|
| 1 | 42T float | 42T float attention | 441T int | ~25M int | ~441T int |
| 5 | 42T float | 210T float attention | 441T int | ~25M int | ~441T int |
| 10 | 42T float | 420T float attention | 441T int | ~25M int | ~441T int |
| 20 | 42T float | 840T float attention | 441T int | ~25M int | ~441T int |
| **Cumulative** | **840T float gen** | **~8,820T float attn** | **8,820T int** | **~500M int** | **~8,820T int** |
Conventional cumulative: ~9,660T float (generation + attention, growing quadratically). VDR cumulative: ~8,820T int (flat per turn). At 150 $\times$  per-operation cost, VDR's 8,820T int ≈ conventional equivalent of ~59T float in raw per-op terms — but spread across a constant attention window rather than a growing one. The actual wall-clock time favors VDR from roughly turn 5 onward because the conventional system's attention cost grows quadratically while VDR's stays flat.

### B.3: Crossover Turn

| Turn | Conventional Total Ops (float) | VDR Total Ops (int, at 150 $\times$  factor) | VDR Equivalent Float Ops | Ratio (Conv/VDR) |
|---|---|---|---|---|
| 1 | 84T | 441T int = 2.94T float-equiv | 2.94T | 28.6 $\times$  (conventional faster) |
| 3 | 378T | 1,323T int = 8.82T float-equiv | 8.82T | 42.9 $\times$  (conventional faster per-op, but doing more total work) |
| 5 | 840T | 2,205T int = 14.7T float-equiv | 14.7T | 57.1 $\times$  |
| 10 | 2,940T | 4,410T int = 29.4T float-equiv | 29.4T | 100 $\times$  |
| 20 | 9,660T | 8,820T int = 58.8T float-equiv | 58.8T | 164 $\times$  |
The "ratio" column shows that VDR's float-equivalent cost stays roughly proportional to turn count (linear), while conventional cost grows quadratically. The crossover in wall-clock time depends on the per-operation speed difference between Q335 int and float16. At 150 $\times$  per-operation slowdown, VDR breaks even at roughly turn 7-10 for a 7B parameter model. For larger models with larger context windows, the crossover comes earlier because attention cost grows faster.

---

## Appendix C: Grammar Decode Savings

### C.1: Candidate Set Sizes by Slot Type

| Slot Type | Typical Candidates | Full Vocab | Reduction Factor | Example |
|---|---|---|---|---|
| Boolean | 2 | 50,000 | 25,000 $\times$  | yes/no field |
| Visibility enum | 3 | 50,000 | 16,667 $\times$  | public/internal/owner only |
| Constraint class enum | 4 | 50,000 | 12,500 $\times$  | axiom/operational/legal/project |
| Status enum | 5-8 | 50,000 | 6,250-10,000 $\times$  | pending/running/completed/failed/killed |
| Builtin opcode | ~300 | 50,000 | 167 $\times$  | Primitive name selection |
| KB identifier | 50-500 | 50,000 | 100-1,000 $\times$  | Entity reference in scope |
| Relation type | ~20 | 50,000 | 2,500 $\times$  | uses/enables/implements/etc |
| Structural punctuation | 1-5 | 50,000 | 10,000-50,000 $\times$  | Pipe, comma, brace, bracket |
| Free text | 50,000 | 50,000 | 1 $\times$  | Prose content slots |
### C.2: Decode Cost per Token by Slot Type

| Slot Type | Surrogate Softmax Ops (Q335) | Full Vocab Softmax Ops (float16) | Ratio | Notes |
|---|---|---|---|---|
| Boolean (2 candidates) | ~440 int ops | ~750K float ops | 1,700 $\times$  cheaper | 2 squares + 1 sum + 2 divides |
| Enum (4 candidates) | ~880 int ops | ~750K float ops | 850 $\times$  cheaper | 4 squares + 1 sum + 4 divides |
| Builtin opcode (300) | ~66K int ops | ~750K float ops | 11 $\times$  cheaper | Even at Q335 width, small candidate set wins |
| KB identifier (200) | ~44K int ops | ~750K float ops | 17 $\times$  cheaper | — |
| Free text (50K) | ~11M int ops | ~750K float ops | 0.07 $\times$  (15 $\times$  more expensive) | Full vocab VDR more expensive per token |
The per-token cost of constrained decode is dramatically cheaper. The per-token cost of unconstrained free-text decode is roughly 15 $\times$  more expensive due to Q335 width. The net effect depends on the fraction of tokens that are grammar-constrained versus free-text.

### C.3: Net Decode Cost by Response Type

| Response Type | Total Tokens | Grammar-Constrained % | Avg Constrained Candidates | Constrained Token Cost (Q335) | Free-Text Token Cost (Q335) | Total Decode Cost | Conventional Total Decode Cost | Net Ratio |
|---|---|---|---|---|---|---|---|---|
| JSON object (20 fields) | 223 | 74% | ~5 | 165  $\times$  1.1K = 182K | 58  $\times$  11M = 638M | 638M | 223  $\times$  750K = 167M | 3.8 $\times$  (VDR slower) |
| Markdown table (20 $\times$ 5) | 367 | 60% | ~3 | 220  $\times$  660 = 145K | 147  $\times$  11M = 1,617M | 1,617M | 367  $\times$  750K = 275M | 5.9 $\times$  (VDR slower) |
| Incident report | 210 | 50% | ~8 | 105  $\times$  1.8K = 189K | 105  $\times$  11M = 1,155M | 1,155M | 3,000  $\times$  750K = 2,250M | 0.51 $\times$  (VDR faster) |
| SRE metrics table | 80 | 85% | ~4 | 68  $\times$  880 = 60K | 12  $\times$  11M = 132M | 132M | 500  $\times$  750K = 375M | 0.35 $\times$  (VDR faster) |
The critical insight: for VDR responses where the total token count is much lower than conventional (incident report: 210 vs 3,000), VDR is faster even with the per-token Q335 penalty, because the massive token reduction outweighs the per-token cost increase. For responses where VDR and conventional have similar total tokens (pure JSON generation), VDR is slower per token and the grammar savings partially but not fully compensate.

---

## Appendix D: GPU Utilization Comparison

### D.1: Utilization by Operation Type

| Operation | Conventional GPU Utilization | VDR GPU Utilization | Reason for Difference |
|---|---|---|---|
| Matrix multiply | 85-95% (tensor core optimized) | 60-80% (integer, no tensor core) | Hardware optimization gap; integer path uses general ALUs |
| Softmax (exponential) | 40-60% (transcendental divergence, reductions) | 80-95% (integer surrogate, uniform ops) | No transcendentals; pure arithmetic; uniform workload |
| Attention masking | 90%+ (simple fill) | 90%+ (identical operation) | Same operation both systems |
| Embedding lookup | 70-90% (memory-bound) | 60-80% (wider reads, memory-bound) | Q335 entries wider; more bandwidth per lookup |
| KB scan | N/A (no equivalent) | 90%+ (columnar scan, coalesced access) | Standard GPU database operation |
| Scope filter | N/A (no equivalent) | 95%+ (bitset test, trivial per-element) | One bit operation per element |
| Prolog unification | N/A (no equivalent) | 70-85% (frontier-based, some divergence on var/atom paths) | Minor divergence on different term types |
| Grammar-constrained decode | N/A (always full vocab) | 95%+ (tiny candidate set, trivial computation) | Orders of magnitude less work |
| Provenance append | N/A (no logging) | 90%+ (atomic bump, bulk copy) | Append-only; minimal synchronization |
| Counter/bitset mutation | N/A (no live state) | 95%+ (atomic int ops) | Single instruction per element |
### D.2: Aggregate Utilization by Workload Phase

| Phase | Conventional | VDR | Notes |
|---|---|---|---|
| Token generation (forward pass) | 70-85% average | 55-75% average | VDR lower due to integer ALU vs tensor core |
| Data processing | N/A | 85-95% | KB scans, filters, aggregations — GPU sweet spot |
| Logic evaluation | N/A | 70-85% | Frontier-based Prolog; moderate divergence |
| Structural output | Included in token generation at 70-85% | 90%+ for grammar-provided; 55-75% for content slots | Grammar tokens free; content tokens same as forward pass |
| State management | N/A (in context window) | 90%+ | Counter/bitset/ring buffer ops trivial |
| Overall weighted | 70-85% | 65-85% | VDR slightly lower on forward pass, higher on everything else |
---

## Appendix E: Memory Layout

### E.1: Q335 Storage Formats

| Format | Limb Layout | Bits per Value | Memory per 1K Values | Alignment | Coalesced Access Pattern |
|---|---|---|---|---|---|
| 11 $\times$ u32 portable | [limb0..limb10] contiguous | 352 | 44 KB | 4-byte aligned | 11 coalesced u32 reads per thread |
| 6 $\times$ u64 optimized | [limb0..limb5] contiguous | 384 | 48 KB | 8-byte aligned | 6 coalesced u64 reads per thread |
| SoA limb-major | limb0[0..N], limb1[0..N], ... | 352 or 384 | 44 or 48 KB | Vector-width aligned | Perfect coalescing — adjacent threads read adjacent memory |
| T0 dense tensor | SoA limb-major, implicit denominator | 352 or 384 per entry | Row: d model  $\times$  44 bytes | Row-aligned | Standard dense matrix access |
### E.2: KB Fact Storage Layout

| Column | Type | Bytes per Fact | Access Pattern | Index |
|---|---|---|---|---|
| fact kb id | u32 | 4 | Coalesced scan | Predicate bucket offset |
| fact pred id | u32 | 4 | Bucket lookup | Primary: pred id → offset/count |
| fact arg begin | u32 | 4 | Indirect (to term pool) | — |
| fact arity | u16 | 2 | Filter | — |
| fact turn | u32 | 4 | Filter/sort | — |
| fact confidence ref | u32 | 4 | Lookup | — |
| fact derivation ref | u32 | 4 | Lookup (provenance) | — |
| **Total per fact** | — | **26 bytes** | — | — |
1 million facts: ~26 MB. Fits entirely in GPU global memory with room for indexes, terms, and working space. A predicate bucket scan over 10,000 facts is one coalesced read of ~260 KB — well within GPU memory bandwidth for sub-millisecond completion.

### E.3: Arena Allocation Pattern

| Arena | Contents | Typical Growth per Turn | Compaction Trigger |
|---|---|---|---|
| Limb arena | Q335 numerators, general rational limbs | 10-100 KB | After session reset or every 100 turns |
| VDR node arena | VdrNode structs for active/rational values | 1-10 KB | With limb arena |
| Remainder arena | AtomicR, CompositeR, FunctionalR payloads | 1-50 KB | With limb arena |
| Term arena | New terms created during Prolog evaluation | 5-50 KB | After Prolog query completion |
| Binding arena | Binding rows from unification frontiers | 10-100 KB per query | After each query (most bindings are temporary) |
| Provenance arena | Event records | 1-5 KB per turn | Periodically; append-only so less urgent |
| Live-state delta | Counter changes, buffer writes, cache updates | 0.5-5 KB per turn | On session reset/clone kill |
Total GPU memory for a typical active session: 50-500 MB including model weights, KB data, arenas, and working space. Well within modern GPU memory capacity (16-80 GB).

---

## Appendix F: Concurrent Stream Execution

### F.1: Stream Assignment

| Stream | GPU Resources Used | Memory Accessed | Overlap With |
|---|---|---|---|
| Stream 0: LLM forward/decode | Tensor ALUs, shared memory | Weight tensors, activation buffers | Streams 1, 3, 4 (different memory) |
| Stream 1: KB query/scan | Integer ALUs, global memory | Fact tables, term pool, index tables | Streams 0, 2, 3 (different ALU units) |
| Stream 2: VDR primitives | Integer ALUs, global memory | Value arenas, live-state arrays | Streams 0, 3, 4 |
| Stream 3: Grammar mask/prep | Integer ALUs, shared memory | Grammar state, candidate buffers | Streams 0, 1, 2 |
| Stream 4: Provenance compact | Memory copy engines | Provenance arena, event buffers | All (uses DMA, not ALUs) |
### F.2: Turn Pipeline Timing (Estimated, SRE Single Turn)

| Step | Component | Duration | Overlaps With |
|---|---|---|---|
| 1. Parse request | CPU | 0.1 ms | — |
| 2. Resolve paths/scope | CPU | 0.05 ms | — |
| 3. Prefetch scoped facts | GPU stream 1 | 0.2 ms | Step 4 prep |
| 4. LLM decode start | GPU stream 0 | — (continuous) | Steps 5-8 |
| 5. Command token emitted (~every 8 tokens) | CPU detects | 0.01 ms | — |
| 6. Lower to opcode batch | CPU | 0.02 ms | LLM continues on stream 0 |
| 7. Execute primitives | GPU stream 2 | 0.1-1 ms | LLM decode on stream 0 |
| 8. Grammar masks update | GPU stream 3 | 0.05 ms | All other streams |
| 9. LLM continues with results | GPU stream 0 | — (continuous) | — |
| 10. Provenance commit | GPU stream 4 | 0.1 ms | LLM decode on stream 0 |
| 11. Response assembly | CPU | 0.2 ms | — |
| **Total wall-clock** | — | **~2-4 seconds** | (dominated by LLM decode of 210 tokens) |
The primitive execution, KB queries, grammar updates, and provenance logging are all overlapped with LLM decode. Their wall-clock cost is effectively zero because they complete while the LLM is still generating the next token.

---

## Appendix G: Bottleneck Analysis

### G.1: Bottleneck Severity by Workload

| Bottleneck | SRE Incident | Financial Portfolio | Academic Grading | Legal Contract | Code Migration |
|---|---|---|---|---|---|
| LLM forward pass (Q335 cost) | Medium (210 tokens) | Low (600 tokens but mostly command) | High (57K tokens, judgment-dominated) | Medium (1,130 tokens) | Medium-High (6,700 tokens) |
| Active value management | Low (<0.1% spill expected) | Low (simple arithmetic) | Low (statistics on integers) | Low (currency amounts) | Low (no VDR arithmetic) |
| Prolog frontier size | Low (small rule sets) | Low (simple queries) | Low (score queries) | Medium (cross-reference queries) | Low (dependency queries) |
| Host-device sync | Medium (20+ command tokens) | Medium (15+ command tokens) | Low (few commands, mostly judgment) | Medium (15+ command tokens) | High (200+ files, many commands) |
| Memory (arena growth) | Low (small state) | Low (moderate data) | Low (150 student KBs) | Low (document structure) | Medium (200 file KBs) |
### G.2: Mitigation Strategies

| Bottleneck | Strategy | Mechanism | Supplementary Spec Reference |
|---|---|---|---|
| LLM Q335 forward pass cost | Reduce token count further through grammar and primitive coverage | More structural tokens grammar-provided; more operations as primitives | ML1-ML8, GD1-GD4 |
| Active value spill | Q-basis reprojection at declared thresholds | AK6 batch reprojection; keep spill rate below 1% | PF6, AK6 |
| Prolog frontier explosion | Query planning on CPU; scope restriction; predicate indexing | PG7 deterministic ordering; IX1-IX2 indexes; SC2-SC3 scope filters | PG1-PG7, IX1-IX10 |
| Host-device sync | Batch command tokens; overlap with LLM decode | OR1-OR2 concurrent streams; batch lowering | OR1-OR2 |
| Arena memory growth | Periodic compaction; session reset | MM3 compaction; SN4 reset | MM1-MM3, SN1-SN5 |
---

## Appendix H: Implementation Phase Performance Targets

### H.1: Per-Phase Performance Milestones

| Phase | Contents | Target Throughput | Validation |
|---|---|---|---|
| Phase 1 | Q335 arithmetic, dense tensor kernels, surrogate attention, confidence | 1M Q335 muls/sec; surrogate softmax 10K rows/sec at d=512 | Arithmetic correctness vs Python VDR reference; softmax sum-to-one verified |
| Phase 2 | KB metadata + fact tables, scope filtering, interned terms, fact queries | 10M facts/sec scan rate; scope filter <0.1ms for 100K facts | Query correctness vs Python Prolog reference |
| Phase 3 | Frontier unification, rule joins, binding buffers, live-state primitives | 100K unifications/sec; joins <1ms for 1K $\times$ 1K frontiers | Derivation correctness; binding consistency |
| Phase 4 | Active spill arena, normalization, functional remainders | Normalization <10ms for 10K active nodes; fn sqrt at depth 8 <1ms | Normalized forms match Python reference; convergence rates verified |
| Phase 5 | Full command pipeline, grammar decode, provenance, sessions | End-to-end prompt <5sec for 210-token SRE scenario | Full system benchmark against Python prototype |
### H.2: Phase Dependencies

| Phase | Depends On | Enables |
|---|---|---|
| Phase 1 | None (foundation) | All subsequent phases (Q335 is the arithmetic substrate) |
| Phase 2 | Phase 1 (Q335 for fact values, confidence refs) | Phase 3 (Prolog needs KB data on GPU) |
| Phase 3 | Phases 1+2 (arithmetic + KB data) | Phase 5 (command pipeline needs Prolog and live-state) |
| Phase 4 | Phase 1 (arithmetic; extends to active/irregular) | Phase 5 (full system needs active value handling) |
| Phase 5 | All prior phases | Production readiness |
---

## Appendix I: Integer ALU Throughput by GPU Generation

### I.1: Native Integer Operations per Clock per SM

| GPU Architecture | Generation Year | INT32 ops/clock/SM | INT64 ops/clock/SM | Concurrent INT+FP | Notes |
|---|---|---|---|---|---|
| Kepler (GK110) | 2013 | 192 | 64 | No — shared pipeline | INT and FP compete for same ALUs |
| Maxwell (GM204) | 2014 | 128 | 4 | No | INT64 severely limited |
| Pascal (GP100) | 2016 | 64 | 32 | No | Better INT64 but still shared |
| Volta (GV100) | 2017 | 64 | 32 | Yes — separate INT datapath | First concurrent INT+FP execution |
| Turing (TU102) | 2018 | 64 | 16 | Yes | Concurrent INT+FP standard |
| Ampere (GA100) | 2020 | 64 | 32 | Yes | Improved INT64 |
| Ada Lovelace (AD102) | 2022 | 128 | 64 | Yes | Doubled INT throughput |
| Hopper (GH100) | 2022 | 128 | 64 | Yes | Data center focused; strong INT path |
| Blackwell (GB202) | 2024 | 128+ | 64+ | Yes | Latest generation; INT path continues widening |
### I.2: Q335 Operation Throughput Estimates by Architecture

| Architecture | SMs | INT32 ops/sec (peak) | Q335 adds/sec (est.) | Q335 muls/sec (est.) | Q335 muls as % of FP16 tensor peak |
|---|---|---|---|---|---|
| Volta (GV100, 80 SM) | 80 | 7.9T | 360M | 40M | 0.02% |
| Ampere (A100, 108 SM) | 108 | 9.7T | 440M | 50M | 0.016% |
| Hopper (H100, 132 SM) | 132 | 16.9T | 770M | 85M | 0.0085% |
| Ada (RTX 4090, 128 SM) | 128 | 16.4T | 745M | 83M | 0.05% |
| Blackwell (B200, est.) | 160+ | 25T+ | 1.1B+ | 125M+ | ~0.01% |
Q335 addition: ~22 INT32 ops per add. Q335 multiplication: ~200 INT32 ops per multiply (schoolbook). The percentage of FP16 tensor peak is low because tensor cores are specialized fixed-function units. But absolute throughput — 50-125 million Q335 multiplies per second — is sufficient for VDR workloads where the total multiply count per prompt is in the thousands to millions, not trillions.

### I.3: Time to Complete VDR Workload Components (H100 Estimates)

| Workload | Q335 Operations | Time at 85M muls/sec | Conventional Float Equivalent | Notes |
|---|---|---|---|---|
| 500 portfolio multiplications | 500 muls | 0.006 ms | Cannot perform (context overflow) | Instantaneous |
| Correlation matrix (500 $\times$ 500) | 125K muls + 125K adds | 1.5 ms | Cannot perform | Sub-second |
| Sort 500 items by Q335 key | ~4,500 comparisons | 0.05 ms | Hundreds of tokens of generated prose | Instantaneous |
| Sum 500 Q335 values | 500 adds | 0.001 ms | Hundreds of tokens digit accumulation | Instantaneous |
| Softmax surrogate (1000 elements) | 1K muls + 1K adds + 1K divs | 0.04 ms | ~15 ms for transcendental softmax | Faster despite wider operands |
| Softmax surrogate (4 elements, grammar) | 4 muls + 4 adds + 4 divs | 0.0002 ms | ~0.06 ms for full-vocab softmax | 300 $\times$  faster due to candidate reduction |
| Q335 matrix multiply (512 $\times$ 512) | ~134M muls | 1.6 sec | ~0.01 ms on tensor cores | This is the real bottleneck |
| Prolog unification (1000 candidates) | ~5K comparisons | 0.06 ms | N/A — no conventional equivalent | Sub-millisecond |
The 512 $\times$ 512 matrix multiply row shows the honest cost: large matrix operations in Q335 are dramatically slower than tensor core float. The VDR strategy is to minimize how often these occur (fewer LLM tokens) rather than to make them individually competitive.

---

## Appendix J: Memory Bandwidth Analysis

### J.1: Bandwidth Requirements by Operation

| Operation | Bytes Read per Element | Bytes Written per Element | Elements per Typical Call | Total Bandwidth | H100 Bandwidth (3.35 TB/s) Utilization |
|---|---|---|---|---|---|
| Q335 add (11 $\times$ u32) | 88 (two operands) | 44 (one result) | 1,000 (vector add) | 132 KB | 0.004% — entirely compute-bound |
| Q335 mul (11 $\times$ u32) | 88 | 44 + possible 44 (remainder) | 1,000 | 176 KB | 0.005% — compute-bound |
| KB fact scan | 26 per fact (all columns) | 0.125 per fact (bitmask) | 10,000 | 261 KB | 0.008% — trivial |
| Scope filter (bitset) | 4 per fact (kb id) + 8 (bitset word) | 0.125 per fact (result bit) | 10,000 | 41 KB | 0.001% — trivial |
| Term pool lookup | 12 per term (tag + 2 payloads) | 0 (read-only) | 5,000 | 60 KB | 0.002% — trivial |
| LLM embedding lookup (Q335) | 44  $\times$  d model per token | 44  $\times$  d model per token | 1 token | 44  $\times$  4096 = 176 KB | 0.005% — trivial |
| LLM weight matrix row (Q335) | 44  $\times$  d model per row | 44 per output element | d model = 4096 | 176 KB per row | Accumulated over matrix: significant |
| Provenance event append | 0 (write-only) | 32 per event | 50 per turn | 1.6 KB | 0.00005% — invisible |
VDR primitive operations are universally compute-bound, not memory-bound. The memory bandwidth of modern GPUs is vastly underutilized by VDR arithmetic and KB operations. The LLM forward pass is the only component that approaches significant bandwidth utilization, due to weight matrix reads — identical in structure to conventional LLM inference but with wider entries.

### J.2: Working Set Sizes

| Component | Size | Fits in L2 Cache (50 MB on H100)? | Notes |
|---|---|---|---|
| Active session live state | 21 KB typical | Yes | Counters, bitsets, buffers — trivial |
| Session scope chain | 64 bytes (16  $\times$  u32) | Yes | Always in registers or L1 |
| Predicate bucket index | ~4 KB for 1000 predicates | Yes | One u32 offset + u32 count per predicate |
| Fact table for one predicate bucket | 2.6 KB per 100 facts | Yes for most buckets | Hot predicates stay cached |
| Term pool (active subset) | 12 KB per 1000 terms | Yes | Repeatedly accessed during unification |
| Grammar state + candidates | <1 KB | Yes | Tiny; always in fast memory |
| Binding frontier (Prolog) | 64 bytes per binding row  $\times$  frontier size | Yes up to ~750K rows | Moderate frontiers fit; large frontiers spill |
| Q335 tensor row (d=4096) | 176 KB | Partially | Typical matrix row doesn't fit L2; streamed from global |
| Full KB fact store (100K facts) | 2.6 MB | Yes | Entire moderate KB fits in L2 |
| Full KB fact store (1M facts) | 26 MB | Yes on H100 (50 MB L2) | Large KBs fit in L2 on data-center GPUs |
Most VDR data structures fit in GPU L2 cache. The LLM weight matrices do not — they stream from global memory, same as conventional inference. The difference is that VDR's non-LLM operations (KB queries, Prolog, primitives) all operate on cache-resident data, giving them near-peak throughput.

---

## Appendix K: Karatsuba Threshold Analysis

### K.1: Multiplication Algorithm Selection

| Limb Count | Schoolbook Ops | Karatsuba Ops | Toom-3 Ops | Recommended | Reason |
|---|---|---|---|---|---|
| 6 (Q335 u64) | 36 muls + 60 adds | 27 muls + ~90 adds | Not applicable (too small) | Schoolbook | Simpler; no recursion overhead; uniform GPU execution |
| 11 (Q335 u32) | 121 muls + ~200 adds | ~50 muls + ~300 adds | ~40 muls + ~400 adds | Schoolbook or Karatsuba | Karatsuba marginal win; depends on GPU add/mul ratio |
| 22 (Q670, double frame) | 484 muls + ~800 adds | ~120 muls + ~700 adds | ~80 muls + ~900 adds | Karatsuba | Clear win at this size |
| 44+ (very large rational) | 1936+ muls | ~300 muls + ~1500 adds | ~150 muls + ~2000 adds | Toom-3 or Karatsuba | Large operands justify recursive splitting |
### K.2: GPU Considerations for Algorithm Selection

| Factor | Favors Schoolbook | Favors Karatsuba/Toom |
|---|---|---|
| Thread divergence | Schoolbook: all threads do identical work | Karatsuba: recursive splitting causes thread divergence |
| Instruction count | Higher mul count | Higher add count + more complex control |
| Register pressure | Low — simple loop | Higher — intermediate values from splitting |
| Shared memory use | Minimal | May need shared memory for intermediate buffers |
| Warp utilization | 100% — perfectly uniform | 80-95% — depends on recursion balance |
| Operand size ≤11 limbs | Optimal or near-optimal | Marginal improvement doesn't justify complexity |
| Operand size >20 limbs | Increasingly suboptimal | Clearly superior |
For Q335 (11 u32 limbs), schoolbook is recommended for GPU due to perfect uniformity. The supplementary specification's AK2 correctly notes "optional Karatsuba/Toom thresholds for large operands" — meaning the system defaults to schoolbook for Q335 and switches only for larger intermediate values that arise during general rational arithmetic or active value normalization.

---

## Appendix L: Scope Filter Strategy Comparison

### L.1: Strategy Performance by KB Tree Size

| Strategy | Mechanism | Setup Cost | Per-Fact Cost | Best For | GPU Kernel Pattern |
|---|---|---|---|---|---|
| Linear scan | Check each fact's kb id against scope chain array | 0 | O(scope depth) comparisons | Tiny trees (<50 KBs) | Each thread: loop over scope chain |
| Binary search | Sort scope chain; binary search per fact | O(depth  $\times$  log(depth)) sort | O(log(scope depth)) comparisons | Small-medium trees | Each thread: binary search |
| Bitset | Set bits for visible KB IDs in u64 array | O(scope depth) bit-sets | 1 bit-test per fact | Medium trees (<4096 KBs) | Each thread: one AND + zero-test |
| DFS interval | Precomputed in/out interval per KB; interval containment test | O(tree size) DFS precomputation (once) | 2 integer comparisons per fact | Large trees, subtree queries | Each thread: two comparisons |
| Interval + shadow | DFS interval with shadow-resolution pass for mounts | O(tree size) + O(mount count) | 2-4 integer comparisons per fact | Large trees with mounts | Two-pass: interval test then shadow check |
### L.2: Visibility Check Cost in Context

| System Size | KBs | Facts | Scope Depth | Strategy | Filter Time (est. H100) | As % of Prompt Time |
|---|---|---|---|---|---|---|
| Personal session | 5 | 500 | 4 | Linear scan | 0.001 ms | 0.00003% |
| Team workspace | 50 | 5,000 | 6 | Bitset | 0.005 ms | 0.00017% |
| Department | 200 | 50,000 | 6 | Bitset | 0.02 ms | 0.0007% |
| Organization | 2,000 | 500,000 | 8 | DFS interval | 0.1 ms | 0.003% |
| Enterprise (full) | 10,000 | 2,000,000 | 10 | DFS interval + shadow | 0.5 ms | 0.017% |
Structural safety (visibility checking) costs at most 0.017% of total prompt time even for the largest enterprise deployment. This confirms VDR-16's claim that structural safety is computationally free relative to the language model's operating cost.

---

## Appendix M: Prolog Join Strategy Selection

### M.1: Join Strategy Performance Characteristics

| Strategy | Build Cost | Probe Cost per Row | Memory | Best Frontier Size | GPU Efficiency |
|---|---|---|---|---|---|
| Nested loop | 0 | O(N) per probe | 0 extra | <100 rows | Low (thread divergence) |
| Hash join | O(N) build hash table | O(1) avg per probe | O(N) hash table | 100-100K rows | High (parallel build + probe) |
| Sort-merge | O(N log N) sort both sides | O(1) amortized per row | O(1) extra after sort | 10K-1M rows | High (GPU sort is efficient) |
| Bitmap semijoin | O(N) build bitmap | O(1) per probe (bit test) | O(domain/8) bitmap | Any size, when join is filter | Very high (trivial per-element) |
### M.2: Typical VDR Query Join Sizes

| Query Type | Goal Count | Avg Frontier After Goal 1 | After Goal 2 | After Goal 3 | Recommended Strategy |
|---|---|---|---|---|---|
| Simple fact lookup | 1 | 1-10 | N/A | N/A | Direct scan (no join) |
| Scoped predicate query | 1 | 10-100 | N/A | N/A | Direct scan with scope filter |
| Two-goal rule (e.g., parent(X,Y), age(Y,A)) | 2 | 50-500 | 10-100 | N/A | Hash join |
| Session scoring rule | 3 | 5-20 (counter values) | 5-20 | 1-5 | Nested loop (tiny frontiers) |
| Contradiction detection | 2 | 50-200 (findings) | 5-20 (conflicting pairs) | N/A | Hash join |
| Cross-reference resolution | 2 | 100-1000 (connections) | 10-100 (matched) | N/A | Hash join or sort-merge |
| Full audit query | 1-2 | 1K-100K (audit events) | 100-10K (filtered) | N/A | Sort-merge or bitmap |
Most VDR queries produce moderate frontier sizes (10-1000 rows) where hash join is optimal. Pathological frontier explosion (>100K rows) only occurs in broad audit queries, which are infrequent and tolerance of higher latency is acceptable.

### M.3: Join Execution Time Estimates (H100)

| Frontier Sizes | Strategy | Build Time | Probe Time | Total | Notes |
|---|---|---|---|---|---|
| 50  $\times$  50 | Hash join | 0.002 ms | 0.002 ms | 0.004 ms | Trivial |
| 500  $\times$  500 | Hash join | 0.01 ms | 0.01 ms | 0.02 ms | Sub-millisecond |
| 5K  $\times$  5K | Sort-merge | 0.1 ms | 0.05 ms | 0.15 ms | Well within interactive latency |
| 50K  $\times$  50K | Sort-merge | 1 ms | 0.5 ms | 1.5 ms | Acceptable for audit queries |
| 500K  $\times$  500K | Sort-merge | 15 ms | 5 ms | 20 ms | Large audit query; batch acceptable |
---

## Appendix N: Functional Remainder Evaluation Cost

### N.1: Per-Function Evaluation Cost

| Function (fn id) | Algorithm | Ops per Depth Step | Depth for 100 Digits | Total Q335 Ops | Time (est. H100) |
|---|---|---|---|---|---|
| SQRT (Newton) | x {n+1} = (x n + S/x n)/2 | 1 div + 1 add + 1 shift = ~600 ops | 8 | ~4,800 | 0.06 ms |
| EXP (Taylor) | Σ x^n/n! cumulative | 1 mul + 1 div + 1 add = ~600 ops per term | 45 | ~27,000 | 0.3 ms |
| LOG (series + reduction) | ln(1+x) series with argument reduction | 1 mul + 1 div + 1 add per term | 340 (at x near 1; much less with reduction) | ~20,000 with reduction | 0.2 ms |
| SIN (Taylor odd) | Σ (-1)^n x^(2n+1)/(2n+1)! | 2 muls + 1 div + 1 add per term | 45 | ~36,000 | 0.4 ms |
| COS (Taylor even) | Σ (-1)^n x^(2n)/(2n)! | 2 muls + 1 div + 1 add per term | 45 | ~36,000 | 0.4 ms |
| ARCTAN (Taylor + Machin) | Series with identity reduction | 1 mul + 1 div + 1 add per term | 170 (without reduction) | ~15,000 with Machin | 0.2 ms |
| ZETA (Borwein) | Weighted alternating sum with 3^-n convergence | 1 mul + 1 add per term | 210 (for any s≥2) | ~42,000 | 0.5 ms |
### N.2: Batch Evaluation Throughput

| Scenario | Function Calls | Total Q335 Ops | Time (H100, sequential) | Time (H100, batched parallel) | Notes |
|---|---|---|---|---|---|
| Single sqrt evaluation | 1 | 4,800 | 0.06 ms | 0.06 ms | Single thread sufficient |
| DFT twiddle factors (N=1024) | 1024 sin + 1024 cos | 74M | 870 ms sequential | ~7 ms batched (1024 parallel) | Parallelism across twiddle factors |
| Kepler orbit (50 Newton steps) | 50 sqrt-like iterations | 240K | 3 ms | 0.5 ms batched | Pipeline Newton iterations |
| Q335 constant resolution (22 constants) | 22 lookups | ~0 (precomputed) | <0.001 ms | <0.001 ms | Constants stored as Q335 limb vectors |
| Softmax via Taylor exp (1000 elements) | 1000 exp evaluations | 27M | 320 ms sequential | ~0.3 ms batched (1000 parallel) | Why rational surrogate is preferred |
The last row demonstrates why the rational surrogate softmax (ML6) is preferred over Taylor exponential softmax (ML5) for GPU execution. Batched Taylor exp for 1000 elements takes ~0.3 ms. The rational surrogate for the same 1000 elements takes ~0.04 ms — an 8 $\times$  speedup from avoiding transcendental evaluation entirely, with the same sum-to-one guarantee.

---

## Appendix O: Determinism Verification

### O.1: Sources of GPU Nondeterminism and Mitigations

| Source | Where It Occurs | Impact on Correctness | Mitigation | Cost of Mitigation |
|---|---|---|---|---|
| Atomic operation ordering | Counter increments, arena allocation | Counter final value correct; intermediate order varies | Final values deterministic; order canonicalized by (turn, batch seq) | Zero — final values same regardless of order |
| Block execution order | All parallel kernels | Results computed in arbitrary block order | Post-sort by canonical key where ordering matters | One radix sort per kernel with ordering requirement |
| Warp-level reduction order | Sum reductions, max reductions | Floating-point: result varies. Integer: result varies if overflow possible | Q335 addition is associative and commutative for closed values; canonical reduction order for active values | Zero for closed (mathematically identical); sort cost for active |
| Memory allocation order | Arena bump allocation across blocks | Handle assignment order varies | External handles assigned by CPU in canonical order after kernel completion | One sequential pass over kernel outputs |
| Provenance event order | Parallel event emission | Events from same turn may appear in arbitrary order | Post-sort by (turn, batch seq, item seq) | One radix sort per turn's events |
### O.2: Determinism Guarantees by Component

| Component | Deterministic? | Condition | Verification Method |
|---|---|---|---|
| Q335 addition | Yes | Always (integer arithmetic) | Bit-identical output for bit-identical input |
| Q335 multiplication | Yes | Always | Same |
| Q335 comparison | Yes | Always | Same |
| KB fact query result set | Yes | Same scope, same facts | Set equality (order may vary; canonical sort applied) |
| Prolog first-solution | Yes | Canonical candidate ordering imposed | CPU selects from fully-computed parallel results |
| Prolog find-all | Yes (set) | Result set identical; ordering canonical | Sort by canonical key |
| Confidence propagation | Yes | Same formula, same inputs | Exact VDR arithmetic |
| Grammar mask | Yes | Same grammar state, same candidates | Bit-identical mask |
| Provenance event content | Yes | Same operations, same inputs | Content identical; ordering canonicalized |
| Session snapshot | Yes | Same live state | Byte-identical snapshot for same logical state |
| Forward pass output | Yes | Same weights, same input, same token count | Bit-identical — integer arithmetic is platform-independent |
The last row is the fundamental advantage: VDR's forward pass produces bit-identical outputs on any hardware because integer arithmetic has no platform-dependent rounding behavior. Conventional float-based forward passes are not deterministic across platforms.

---

## Appendix P: Power-of-Two Split Detail

### P.1: Q335 Multiplication Split Mechanics

| Step | Operation | Operand Size | Result Size | GPU Implementation |
|---|---|---|---|---|
| 1. Full multiply | A  $\times$  B | 335 bits  $\times$  335 bits | 670 bits | Schoolbook on 11 $\times$ u32 limbs → 22 limbs |
| 2. Extract quotient | Bits [670:335] of product | 335 bits | 335 bits (11 limbs) | Right-shift by 335 bits = skip lower 10.47 limbs → limb-aligned extraction |
| 3. Extract remainder | Bits [334:0] of product | 335 bits | 335 bits (11 limbs) | Mask lower 335 bits → limb-aligned extraction |
| 4. Check remainder | remainder == 0? | 335 bits | 1 bit | OR-reduce all 11 limbs; zero-test on result |
| 5a. If zero | Result is closed Q335 | quotient only | 11 limbs | Store quotient; set tag = QFRAME; set r ref = 0 |
| 5b. If nonzero | Result is active | quotient + remainder | 22 limbs + node | Store quotient as V; allocate AtomicR in arena; store remainder; set tag = ACTIVE |
### P.2: Bit Alignment Within Limbs

| Layout | Limb Width | Limbs for 335 bits | Wasted Bits | Split Position within Limb Array |
|---|---|---|---|---|
| 11  $\times$  u32 | 32 | 11 (352 bits) | 17 | Split at bit 335 falls within limb 10 (bits 320-351); requires intra-limb shift |
| 6  $\times$  u64 | 64 | 6 (384 bits) | 49 | Split at bit 335 falls within limb 5 (bits 320-383); requires intra-limb shift |
The intra-limb shift is one shift + one mask operation per split — trivial cost. The "wasted" bits above 335 in the top limb are always zero in a properly normalized Q335 value. After multiplication, the product occupies up to 670 bits, spread across 22 u32 limbs or 12 u64 limbs. The quotient extraction starts at limb offset ceil(335/32) = 11, and the remainder is the lower 11 limbs with the top limb masked.

---

## Appendix Q: Tensor Core Feasibility Analysis

### Q.1: Why Tensor Cores Cannot Be Used Directly

| Tensor Core Property | Float16/BF16/TF32 | Q335 Integer | Incompatibility |
|---|---|---|---|
| Operand width | 16/16/19 bits | 352 bits | 22 $\times$  wider; doesn't fit tensor core input registers |
| Accumulator width | 32 bits | 704 bits (full product) | 22 $\times$  wider; accumulator overflow |
| Rounding mode | Round-to-nearest-even | Exact (no rounding) | Tensor cores round by design |
| Matrix tile size | 16 $\times$ 16 or 8 $\times$ 8 | Same logical tile | Tiles contain 11 $\times$  more data per element |
| Hardware function | Fused multiply-accumulate | Multi-precision multiply + exact accumulate | Different computational primitive |
### Q.2: Hypothetical Integer Tensor Core Design

| Feature | Description | Benefit for VDR |
|---|---|---|
| Wide integer MAC | Multiply-accumulate on 352-bit operands with 704-bit accumulator | Direct Q335 matrix multiply support |
| Carry-chain hardware | Hardware carry propagation across limb boundaries | Eliminates software carry loop |
| Exact split unit | Fixed-position bit extraction at configurable split point | Hardware Q335 quotient/remainder extraction |
| Multi-precision register file | Registers holding 352+ bit values | Eliminates limb-by-limb register management |
| Estimated speedup over INT32 ALU path | 50-200 $\times$  for matrix operations | Would close the gap with float tensor cores |
This is engineering, not physics. If exact arithmetic workloads create sufficient market demand, GPU vendors can add integer tensor cores. The computational patterns (multiply-accumulate on fixed-width wide integers with exact accumulation) are simpler than the floating-point tensor core patterns (which must handle denormals, infinities, NaN propagation, and multiple rounding modes).

---

## Appendix R: Spill Threshold Decision Tree

### R.1: Active Value Monitoring

| Metric | Measurement | Source | Check Frequency |
|---|---|---|---|
| Active fraction per tensor | count(tag == ACTIVE) / total elements | Per-tensor tag scan | Every tensor operation |
| Arena growth rate | bytes allocated / turns elapsed | Arena bump pointer delta | Every turn |
| Maximum active tree depth | max(depth) across active nodes | VdrNode depth field | Every normalization pass |
| Closed-to-active conversion rate | new active nodes / total operations | Counter on spill events | Every operation batch |
### R.2: Threshold Actions

| Active Fraction | Tensor Class | Action | Performance Impact |
|---|---|---|---|
| 0% | T0 (shared-frame dense) | No action; optimal path | Baseline — highest throughput |
| 0.01% - 0.1% | T0 with sparse spill tags | Tag active entries; process on slow path | Negligible — fast path dominates |
| 0.1% - 1% | T1 (dense + spill tags) | Per-element tag check on operations | 1-5% overhead from tag branching |
| 1% - 5% | T1 with tile-local spill tables | Group active entries per tile; batch process | 5-15% overhead |
| 5% - 10% | T1 transitioning to T2 | Consider reprojection to reduce active count | 15-30% overhead; reprojection may be cheaper |
| >10% | T2 (sparse active) or host intervention | Switch to sparse representation or reproject entire tensor | 30-50% overhead; reprojection strongly recommended |
### R.3: Reprojection Decision

| Trigger | Condition | Action | Error Bound | Provenance |
|---|---|---|---|---|
| Denominator budget exceeded | vdr denom bits(value) > budget bits | B136 vdr reproject qbasis | Exact bound computed and stored | fact(reprojection, value ref, old bits, new bits, error bound, turn) |
| Active fraction exceeded | tensor active fraction > threshold | Batch AK6 reprojection on all active entries | Per-entry exact bound | Batch provenance events |
| Training step checkpoint | Every N training steps | Reproject all parameters to Q335 base | Per-parameter exact bound | Checkpoint provenance |
| Manual trigger | User or system policy | Selective or full reprojection | Exact bound | Policy-driven provenance |
Every reprojection is logged with exact error bounds. No silent precision loss occurs anywhere in the system. This is the fundamental distinction from floating-point: float silently truncates on every operation; VDR reprojection is a declared, auditable, bounded precision decision.

---

## Appendix S: Host-Device Synchronization Cost

### S.1: Synchronization Points per Turn

| Sync Point | Direction | Payload Size | Latency | Frequency per Turn | Overlap Possible |
|---|---|---|---|---|---|
| Scope chain transfer | Host → Device | 64 bytes | 5-10  $\mu$ s | 1 | Yes (during LLM prefill) |
| Command token lowering | Host → Device | ~32 bytes per command | 5-10  $\mu$ s | 5-50 per turn | Yes (during LLM decode) |
| Primitive result retrieval | Device → Host | 4-64 bytes per result | 5-10  $\mu$ s | 5-50 per turn | Yes (buffered, batch retrieved) |
| Grant verification | Host-only | 0 (no transfer) | 1-5  $\mu$ s | 5-50 per turn | Yes (CPU-parallel) |
| Path resolution | Host-only | 0 (no transfer) | 1-10  $\mu$ s per path | 5-50 per turn | Yes (cached after first resolution) |
| Grammar state update | Host → Device | 16 bytes per update | 5-10  $\mu$ s | 10-100 per turn | Yes (during LLM decode) |
| Provenance batch commit | Device → Host (optional) | 1-5 KB per turn | 10-50  $\mu$ s | 1 per turn | Yes (stream 4, overlapped) |
### S.2: Total Synchronization Overhead per Turn

| Scenario | Command Tokens | Sync Events | Total Sync Latency (non-overlapped) | Total Sync Latency (overlapped with LLM decode) | As % of Turn Time |
|---|---|---|---|---|---|
| Simple query (1 command) | 1 | ~5 | 0.05 ms | ~0 ms (fully overlapped) | ~0% |
| SRE investigation turn (10 commands) | 10 | ~25 | 0.25 ms | 0.05 ms (mostly overlapped) | 0.002% |
| Complex analysis (30 commands) | 30 | ~70 | 0.7 ms | 0.15 ms | 0.005% |
| Bulk migration (100 commands) | 100 | ~200 | 2.0 ms | 0.5 ms | 0.02% |
Host-device synchronization is not a significant bottleneck. The concurrent stream model overlaps most synchronization with LLM decode. The residual non-overlapped sync is sub-millisecond even for complex turns.

---

## Appendix T: Comparison with Approximate GPU Approaches

### T.1: VDR vs Quantized Integer Inference

| Aspect | INT8 Quantized Inference | INT4 Quantized Inference | VDR Q335 Integer |
|---|---|---|---|
| Operand width | 8 bits | 4 bits | 352 bits |
| Precision | ~2 decimal digits | ~1 decimal digit | ~100 decimal digits |
| Accuracy loss from quantization | 0.1-2% on benchmarks | 1-5% on benchmarks | 0% (exact) |
| Tensor core compatible | Yes (INT8 tensor cores) | Yes (INT4 on some architectures) | No (too wide) |
| Throughput vs FP16 | 2 $\times$  (8-bit fits 2 $\times$  per register) | 4 $\times$  (4-bit fits 4 $\times$  per register) | 0.005 $\times$  (22 $\times$  wider, no tensor cores) |
| Reproducible across platforms | No (quantization rounding varies) | No | Yes (integer arithmetic is exact) |
| Provenance | None | None | Full — every value traced |
| Suitable for | Production inference (approximate OK) | Edge deployment (approximate OK) | Exact computation with audit requirements |
### T.2: VDR vs Mixed-Precision Training

| Aspect | FP16/FP32 Mixed Precision | BF16/FP32 Mixed Precision | VDR Q335 Exact |
|---|---|---|---|
| Forward pass precision | 16-bit float | 16-bit bfloat | 352-bit integer |
| Accumulation precision | 32-bit float | 32-bit float | 704-bit integer (exact) |
| Loss scaling required | Yes (to prevent underflow) | Less often | No (no underflow possible) |
| Gradient precision | 16-bit (lossy) | 16-bit (lossy) | Exact integer |
| Checkpoint reproducibility | No (platform-dependent) | No | Yes (bit-identical) |
| Training throughput | Baseline | ~Same as FP16 | ~150 $\times$  slower per token |
| Training token count for equivalent work | Baseline | Same | 85-97% fewer tokens needed |
---

## Appendix U: Energy and Cost Estimates

### U.1: Energy per Operation

| Operation | Energy (pJ, estimated) | Source |
|---|---|---|
| FP16 multiply (tensor core) | 0.1-0.3 | Published GPU power analysis |
| INT32 multiply (ALU) | 0.1-0.5 | Comparable to FP32 ALU |
| Q335 multiply (schoolbook, 200 INT32 ops) | 20-100 | 200 $\times$  INT32 single multiply |
| Q335 add (22 INT32 ops) | 2-10 | 22 $\times$  INT32 single add |
| DRAM read (64 bytes, one cache line) | 10-50 | GPU memory subsystem |
| L2 read (64 bytes) | 1-5 | On-chip cache |
### U.2: Energy per Prompt

| System | Tokens | Ops per Token | Energy per Op | Total Energy | Notes |
|---|---|---|---|---|---|
| Conventional (FP16, 7B model) | 3,000 | 14B | 0.2 pJ | 8.4 J | Forward pass dominated |
| VDR (Q335, 7B model) | 210 | 14B  $\times$  150 | 50 pJ avg | 22 J | Higher per-op, fewer tokens |
| VDR primitive + KB ops | — | ~25M int ops | 0.3 pJ | 0.0075 J | Negligible energy cost |
| **Conventional total** | — | — | — | **8.4 J** | — |
| **VDR total** | — | — | — | **~22 J** | — |
VDR uses roughly 2.6 $\times$  more energy per prompt than conventional for a single turn. Over 20 turns where conventional attention cost grows quadratically, VDR's flat energy profile catches up. The energy cost is dominated by the LLM forward pass in both systems. VDR's primitive and KB operations are energetically negligible.

### U.3: Cost per Prompt (Cloud GPU Pricing)

| Configuration | GPU | Cost per Hour | Time per Prompt (SRE single turn) | Cost per Prompt | Notes |
|---|---|---|---|---|---|
| Conventional (FP16, H100) | 1 $\times$  H100 | $3.00 | ~30 sec (3000 tokens) | $0.025 | Standard inference |
| VDR (Q335, H100) | 1 $\times$  H100 | $3.00 | ~4 sec (210 tokens + primitives) | $0.0033 | 7.5 $\times$  cheaper per prompt |
| VDR (Q335, H100, 20-turn) | 1 $\times$  H100 | $3.00 | ~80 sec total | $0.067 | Flat per turn |
| Conventional (20-turn) | 1 $\times$  H100 | $3.00 | ~600 sec total (growing attention) | $0.50 | 7.5 $\times$  more expensive |
The per-prompt cloud cost is lower for VDR despite the per-operation slowdown, because the total GPU-seconds are lower. The token reduction dominates the per-operation cost increase. Over multi-turn interactions, the cost advantage grows because VDR's time is flat per turn while conventional time grows with context.

---

