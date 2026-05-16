Got it. Taking the premise as given, the mechanical question becomes:

- how do you represent VDR, KB, Prolog, primitives, and orchestration on GPU hardware,
- using integer pipelines where possible,
- while keeping the whole thing throughput-oriented and pipelined.

Short answer:

Yes, you can map a large part of this system onto GPUs, but not as “one giant tensor kernel.” You’d map it as a heterogeneous GPU runtime with 6 execution classes:

1. fixed-width integer arithmetic kernels
2. big-integer / limb arithmetic kernels
3. sparse graph / pointer-chasing kernels
4. relational / Prolog unification kernels
5. token/model kernels
6. host-scheduled orchestration and batching

The trick is to treat the GPU not as “a transformer accelerator” but as:
- a wide SIMD/SIMT integer coprocessor,
- plus a few dense linear algebra paths,
- plus a graph engine for batched KB / Prolog operations.

Below is the mechanical mapping.

1. Split the system into GPU-friendly and GPU-hostile parts

Very important first partition.

GPU-friendly:
- fixed-denominator VDR closed arithmetic
- Q-basis arithmetic with shared denominator like \(2^{335}\)
- integer add/mul/divmod over batched values
- batched normalization passes
- vector/matrix ops over fixed-size VDR lanes
- exact attention variants if represented in fixed-limb format
- softmax surrogate with exact integer/rational arithmetic
- bitsets, counters, queues, ring buffers
- graph traversals if laid out compactly
- bulk fact filtering / predicate matching
- batched unification for many candidate facts
- grammar-constrained decoding masks
- confidence propagation arithmetic

GPU-hostile or less GPU-native:
- irregular recursive remainder trees
- arbitrary-depth functional remainders
- KB mount/path mutation with lots of branching
- backtracking-heavy depth-first Prolog at fine granularity
- dynamic allocation-heavy live session mutation
- string-heavy logic
- OS/file/network/process primitives
- environment management
- low-batch tiny control decisions

So the architecture you want is not “everything runs on GPU equally.”
It is:

- host controls control flow and irregular mutation
- GPU executes bulk integer/graph/unification/math batches

2. Use a split runtime model

Best architecture:

- CPU = control plane
- GPU = data plane

CPU responsibilities:
- session orchestration
- path resolution
- grant checking
- scheduling and batching
- launching kernels
- handling branchy backtracking decisions
- external IO
- memory compaction / garbage collection / defragmentation
- rule indexing maintenance

GPU responsibilities:
- VDR arithmetic batches
- exact tensor/math batches
- normalization/reduction
- predicate candidate filtering
- unification over many candidates
- confidence propagation
- KB scans over compact columnar/indexed layouts
- grammar mask generation
- attention/LLM dense compute
- bitset/ring/counter operations in batches

So mechanically:
- do not port “the entire system” to one monolithic GPU kernel
- port the high-volume primitives and query inner loops

3. Number representation for GPU

This is the foundation.

3.1 Closed VDR in GPU memory

For closed values where \(R = 0\), use a packed struct like:

```text
struct VDRClosed {
  sign: i1
  v_limbs[LV]
  d_kind: u8
  d_payload
}
```

But because the spec strongly prefers common denominator frames, especially \(2^{335}\), you should specialize.

For Q335-style values:
- denominator is implicit
- only numerator needs storage
- sign can be folded into numerator

So use:

```text
struct Q335 {
  limbs[6] // 6 x 64 = 384 bits, enough for signed 335-bit numerator + headroom
}
```

Why 6 limbs:
- 335 bits does not fit in 5 x 64 = 320
- 6 limbs gives 384 bits
- align to 32 or 48 bytes depending on packing

This is the sweet spot for GPU.

Then:
- add/sub = limbwise carry chain
- mul = 6x6 schoolbook or Karatsuba thresholded
- divmod by \(2^{335}\) = bit shift/split, very cheap
- compare = lexicographic limb compare
- normalize sign = simple

This is much more GPU-friendly than general rational pairs.

3.2 General closed rational VDR

For non-Q-basis closed rationals:
- store numerator and denominator separately in limb arrays
- small values use tagged immediate fast path
- large values use arena offsets into limb pools

Example layout:

```text
struct ClosedRef {
  tag: u8 // small-int, q335, rational-small, rational-big, active
  a0: u32
  a1: u32
}
```

Then payload lives in SoA pools.

Recommendation:
- do not use pointer-rich AoS trees on GPU
- use arena indices into flat buffers

3.3 Active VDR representation

Active VDR needs explicit storage of \(R\).

Use tagged nodes in flat pools:

```text
enum RTag {
  ZERO,
  ATOMIC_INT,
  COMPOSITE,
  FUNCTIONAL
}

struct VDRNode {
  tag: u8
  flags: u8
  depth: u16
  v_ref: u32
  d_ref: u32
  r_ref: u32
}
```

And for composite remainders:

```text
struct CompositeR {
  base_ref: u32
  child_begin: u32
  child_count: u32
}
```

Children stored in contiguous child arrays.

For functional remainders:
- store function ID + parameter refs
- not actual closures

```text
struct FunctionalR {
  fn_id: u16
  arity: u16
  param_begin: u32
  param_count: u32
}
```

Important:
- GPU cannot handle arbitrary heap-closure semantics well
- convert every functional remainder into a compact opcode + arguments record

4. Use structure-of-arrays, not object graphs

The doc is conceptually object-heavy. GPU wants SoA.

Instead of:

- each VDR object points to nested children
- each fact stores boxed terms
- each KB stores maps of vectors of structs

Use:

- node tables
- edge tables
- payload pools
- columnar indexes

For example, facts should not be “Python objects.”
They should be:

```text
fact_predicate_id[]
fact_kb_id[]
fact_turn[]
fact_arity[]
fact_arg_begin[]
fact_derivation_ref[]
```

And terms:

```text
term_tag[]
term_payload0[]
term_payload1[]
```

Then GPU kernels can scan:
- all facts with predicate p
- all terms in argument position i
- all candidate bindings

This is the single most important data-layout conversion.

5. Map VDR arithmetic onto GPU integer hardware

5.1 Integer width reality

GPUs usually have:
- native 32-bit integer ALUs
- decent 64-bit integer support, slower than 32-bit on many architectures
- very poor arbitrary precision directly

So represent big ints in:
- 32-bit limbs if portability matters most
- 64-bit limbs if architecture supports good int64 throughput

Pragmatic choice:
- use 32-bit limbs for portable kernels
- use 64-bit limbs as optimized backend on GPUs with strong int64

For Q335:
- 11 limbs x 32-bit = 352 bits
- or 6 limbs x 64-bit = 384 bits

5.2 Core kernels

You’d want kernels for:

- limb_add
- limb_sub
- limb_mul_schoolbook
- mul_hi_lo
- compare
- shift-left/right
- divmod power-of-two frame
- gcd_small / gcd_limited
- exact reduction for closed nodes
- projection/freeze kernels

For Q335 multiply:
- multiply two limb vectors
- split at bit 335
- high part becomes quotient/current value
- low part becomes remainder payload

This is very suitable for GPU because divmod by \(2^k\) is just bit slicing.

5.3 Warp-level carry propagation

Use warp-synchronous carry chains:
- one lane per limb for small fixed-width values
- or one thread per value for batched values

Two strategies:

Strategy A: one thread handles one 384-bit value
- simpler
- lower coordination
- good if there are many independent values

Strategy B: one warp handles one big value
- higher single-op throughput
- better for very large limb counts
- worse occupancy for smaller sizes

For Q335 and similar sizes, Strategy A is often better unless you’re doing very large matrix multiplies of VDR values.

6. Dense LLM operations on GPU with exact numerics

6.1 Embeddings and linear layers

If weights are exact Q335-like values:
- store numerators in fixed-width limb arrays
- denominator is implicit per tensor/frame

Matrix multiply becomes:
- many integer dot products over multi-limb numbers
- accumulation into larger limb accumulators
- divmod/frame split afterward if needed

This is the hardest expensive part.

Because exact integer GEMM is much more expensive than float GEMM.

Mechanically, you can structure it as:

- tile load A and B numerators into shared memory
- schoolbook limb-multiply for each scalar multiply
- accumulate products in wider accumulators
- periodically normalize / frame-project

But raw throughput will be much lower than tensor core float.

6.2 Better approach for LLM path

Use staged numeric classes:

- Class 0: exact int32/int64 fast path
- Class 1: Q335 fixed-limb path
- Class 2: active/remainder path only when overflow/non-closure occurs

That means:
- most operations stay in fixed-size closed representation
- only exceptional operations spill to active nodes

This is essential for GPU viability.

Otherwise active tree creation will destroy throughput.

6.3 Attention

The most GPU-mappable exact attention is not full transcendental softmax.
Use the document’s rational surrogate.

Pipeline:
- compute exact score matrix in Q-frame
- causal mask
- rowwise shift by row max or fixed stabilizer
- square/cube shifted values
- row sum
- exact normalization by that sum

This is all integer/rational and row-parallel.

Mechanically:
- scores: dense kernel
- mask: elementwise kernel
- square: elementwise kernel
- row reduction: block reduction
- normalization: elementwise division kernel

This maps cleanly.

7. Map KB tree to GPU

The KB tree is really a graph with hierarchical edges and typed payloads.

You should split representation into:

7.1 KB metadata arrays

```text
kb_parent[]
kb_first_child[]
kb_child_count[]
kb_visibility[]
kb_frozen[]
kb_owner[]
kb_created[]
kb_modified[]
```

7.2 Path registry

Path resolution itself is string-heavy and better on CPU.

Recommended:
- resolve dotted paths on CPU
- send integer KB IDs to GPU
- keep GPU pathless

This matches the document’s own runtime idea.

7.3 Fact storage

Store facts in predicate-major columnar format:

```text
predicate_bucket_offsets[predicate_id]
fact_ids_sorted_by_predicate[]
fact_kb_id[]
fact_arg_begin[]
fact_arity[]
fact_turn[]
fact_confidence_ref[]
```

Then a query:
- lookup predicate bucket
- GPU scans candidate facts for active scope mask
- unifies arguments in parallel

7.4 Scope chain

Precompute scope chain on CPU as small integer list.
Send to GPU as:
- short ancestor vector
- or bitmask / interval if KB IDs are subtree-localized

Then kernels can cheaply test:
- candidate fact is visible from scope?

Best case:
- assign subtree intervals via DFS numbering
- then “in subtree” becomes interval containment check

8. Prolog on GPU

This is possible if you reformulate it as batched relational joins plus unification, not recursive pointer-walking.

8.1 GPU-suitable subset

Most GPU-friendly Prolog operations:
- predicate filtering
- fact candidate enumeration
- term tag compatibility checks
- variable binding consistency checking
- simple rule body joins
- transitive closure / graph-style queries
- first-pass search frontier expansion

Least friendly:
- deeply irregular recursive DFS
- lots of tiny branch splits
- per-branch dynamic environment allocation

So use hybrid execution:
- CPU manages search agenda
- GPU evaluates large frontiers

8.2 Term encoding

Use compact term records:

```text
enum TermTag {
  ATOM,
  VAR,
  INT,
  VDR_CLOSED,
  VDR_ACTIVE_REF,
  LIST_REF,
  KB_REF
}
```

Payloads are integer handles.

For atoms:
- intern strings to integer symbols
- never compare strings on GPU if avoidable

For variables:
- local variable IDs within query/rule frame

For lists:
- flatten cons/list representation into ranges in a term pool where possible

8.3 Unification kernel

Given:
- one query pattern
- many candidate facts

Kernel does:
- per candidate fact, compare arity
- per argument:
  - dispatch by term tag
  - atom/integer/KB ref equality
  - fraction equality via cross-mul or canonical ID equality
  - variable binding consistency checks in local scratch
- produce success bitmap
- optional binding output table

This is highly parallel.

8.4 Rule body evaluation as join

A rule body with multiple goals can be implemented as:
- candidate relation for goal 1
- join with candidate relation for goal 2 on shared variables
- etc.

This is basically a GPU relational engine.

So your Prolog runtime on GPU should look more like:
- Datalog / join engine for broad search
than
- classic WAM stack machine

If you insist on classic depth-first Prolog, keep the stack/search control on CPU and offload each candidate matching phase to GPU.

9. Data primitives on GPU

These map well.

9.1 Counters
- atomic integer arrays
- bounded checks in kernels

9.2 Bitsets
- excellent on GPU
- use packed 32/64-bit words
- warp-wide set/test/count

9.3 Ring buffers
- per-session or per-notebook circular arrays
- atomic write index

9.4 Queues/stacks
- batched push/pop with prefix sums
- avoid fine-grained global contention

9.5 LRU caches
- harder
- likely keep on CPU or implement approximate GPU cache
- exact LRU mutation is expensive under contention

So for data primitives:
- counters, bitsets, buffers: GPU-native
- queues/stacks: GPU-usable with batch discipline
- LRU: probably CPU or special-case

10. Grammar system and decoding constraints on GPU

This is actually one of the cleanest GPU mappings.

At decode time:
- grammar tells you valid token classes for current slot
- KB gives valid identifiers/enums
- GPU builds a mask over vocabulary or candidate set

Mechanically:
- maintain per-state grammar automaton state
- per decode step, derive allowed token subset
- apply logit mask on GPU
- sample/argmax within masked set

If you have KB-scoped candidate IDs:
- don’t expose whole vocab
- expose a compact candidate buffer
- decode over candidate buffer

This is ideal for GPU because:
- masking is vectorized
- candidate compaction is parallel
- softmax/sampling over smaller set is cheap

11. A pipeline architecture that matches the document

Here is the practical pipelined decomposition.

Stage A: host-side parse and planning
CPU:
- parse user input
- resolve paths to KB IDs
- determine active scope
- assemble command/query batches

Stage B: GPU retrieval and logic prefilter
GPU:
- scope-filter facts
- predicate bucket scan
- candidate term matching
- confidence fetch
- grammar candidate enumeration

Stage C: GPU exact compute
GPU:
- VDR/Q335 arithmetic kernels
- exact/surrogate attention
- confidence propagation
- normalization
- KB aggregate operations

Stage D: GPU/CPU rule expansion
GPU:
- execute bulk joins/unifications
CPU:
- decide backtracking/frontier expansion/termination

Stage E: LLM decode
GPU:
- standard token forward pass
- grammar-constrained masking
- command token emission

Stage F: execution/store
CPU or GPU depending on primitive:
- pure batch primitives on GPU
- operational primitives on CPU/env worker
- write results back into KB pools
- update provenance indexes

Repeat.

12. Memory hierarchy design

12.1 HBM/global memory
Use for:
- limb pools
- fact tables
- term tables
- rule tables
- embedding/parameter tensors
- confidence arrays
- bitsets and graph edges

12.2 Shared memory
Use for:
- tiled limb operations
- block-local reductions
- candidate binding scratch
- join hash tables for small body joins
- local grammar mask fragments

12.3 Registers
Use for:
- immediate small ints
- fixed small binding maps
- carry state
- local term comparisons

12.4 Constant/texture cache
Use for:
- small opcode tables
- function IDs
- grammar metadata
- relation type tables
- common denominator/frame constants

13. Avoid dynamic allocation inside kernels

Critical design rule.

GPU hates:
- recursive heap allocation
- arbitrary pointer churn

So for active VDR and Prolog results:
- use append-only arenas
- allocate via block-level bump allocators
- compact later
- reference objects by integer offsets

For each batch:
- preallocate output arenas
- produce `(count, offsets)`
- compact if needed after kernel

This is exactly how you should represent:
- new remainder nodes
- new derivation records
- new inferred facts
- clone/session live-state logs

14. Represent provenance as append-only event tables

The document is provenance-heavy.
Good news: provenance is GPU-friendly if append-only.

Use event tables:

```text
event_type[]
event_subject[]
event_tool[]
event_input_begin[]
event_input_count[]
event_output_ref[]
event_confidence_ref[]
event_turn[]
```

Then each kernel appends provenance rows for produced outputs.

Avoid nested provenance objects during compute.
Use flat event logs and reconstruct derivation graph later.

15. Functional remainders on GPU

This needs special treatment.

Do not represent them as arbitrary host-language callables.

Instead represent as:
- opcode
- parameter tuple
- depth argument

Examples:
- `FN_SQRT(value_ref)`
- `FN_EXP(value_ref)`
- `FN_LOG(value_ref)`
- `FN_SERIES(kind, params...)`

Then dispatch to specialized kernels:
- Newton kernels
- Taylor kernels
- Borwein kernels
- recurrence kernels

This gives you deterministic GPU implementations.

For a depth-controlled function:
- launch a kernel that computes the requested depth directly
- or iterates depth steps with checkpointing

16. Mapping exact VDR matrix ops into GPU tensor-like execution

If your target includes training/inference over exact arithmetic, think in 3 execution tiers.

Tier 1: implicit-denominator closed tensors
- tensor entries are fixed-width numerators
- denominator shared by whole tensor/layer
- best GPU throughput

Tier 2: mixed closed tensors with occasional spill
- each entry tagged closed/active
- active entries stored in sparse spill pool
- dense path processes closed entries
- sparse repair kernels process active entries

Tier 3: fully active tensors
- likely too slow for large-scale dense use
- reserve for special computations only

This is probably the most important architectural move if you want practical GPU mapping.

17. Sparse spill architecture for active remainders

A good mechanical design is:

Dense tensor storage:
- main tensor stores fixed-width closed/Q-basis values

Overflow path:
- if op produces active remainder
- main tensor stores tag + base/current value
- spill table stores active remainder descriptor

Then later passes:
- either resolve/project spill entries back to closed form
- or propagate them only where needed

This preserves dense GPU throughput for the majority path.

18. Prolog execution model: frontier engine, not recursive interpreter

Best GPU form:

- compile each query/rule into a sequence of relational ops
- maintain current frontier of partial bindings
- each body literal filters/extends frontier
- use hash join / sort-merge / bitmap filter kernels

So instead of:

- recursive call stack with backtracking

You run:

- frontier0 = initial empty binding
- frontier1 = unify with literal1 candidates
- frontier2 = join literal2
- ...
- emit solutions

For first-solution mode:
- GPU can still produce a solution bitmap
- CPU can select first by deterministic ordering

This is much more GPU-realistic.

19. String handling: intern aggressively

The document has atoms, paths, names, predicates.

On GPU:
- never operate on raw strings if avoidable

Intern everything:
- predicate names -> predicate IDs
- atom text -> atom IDs
- path segments -> segment IDs
- grammar enums -> enum IDs
- primitive names -> opcode IDs

Then nearly everything becomes integer comparison.

This is essential.

20. Session clones on GPU

The document’s session model actually maps well if you use copy-on-write.

Persistent state:
- shared immutable GPU buffers

Live state:
- per-session delta buffers

Clone:
- new session header points to same persistent buffers
- new live-state delta arenas
- inheritance by parent pointer

Reset:
- drop live-state delta arenas
- restore baseline handles

Kill:
- release delta arenas

This is efficient on GPU if sessions are numerous and mostly read-shared.

21. Scheduling model

You want a work scheduler with these queues:

- arithmetic batch queue
- query/unification batch queue
- graph traversal queue
- grammar mask queue
- dense LLM forward queue
- sparse spill-resolution queue
- host IO / operational queue

Scheduler groups work by:
- operation type
- numeric type
- tensor shape
- predicate ID
- scope shape
- session

Then launches large homogeneous batches to GPU.

This is how you recover throughput from an otherwise irregular architecture.

22. Likely kernel families

A practical implementation would probably need kernels in these families:

Arithmetic:
- q335_add/sub
- q335_mul_split
- q335_compare
- q335_reduce
- rational_crossmul_compare
- active_node_merge
- normalize_bottom_up

Dense exact ML:
- exact_embedding_lookup
- exact_matmul_qbasis
- exact_attention_scores
- exact_causal_mask
- surrogate_softmax
- exact_value_mix
- exact_relu
- exact_residual_add
- exact_loss
- exact_backward local kernels

KB/graph:
- scope_filter
- predicate_bucket_scan
- connection_traverse
- ancestor/mount checks
- bitset ops

Prolog:
- unify_candidates
- extend_bindings
- join_frontiers
- derive_facts
- contradiction scan

Grammar:
- grammar_state_step
- enum candidate generation
- kb-id candidate generation
- vocab mask apply

Session/live:
- counter mutate
- ring buffer append
- queue batch push/pop
- snapshot diff/copy
- clone init

23. What to keep on CPU no matter what

I would keep these on CPU first, even if later partially migrated:

- path parsing from strings
- grant verification
- environment/file/network/process ops
- complex mount mutation
- irregular session administration
- global memory compaction
- backtracking policy decisions
- low-volume orchestration
- debug/provenance rendering

Because moving them to GPU gives little benefit and lots of pain.

24. Biggest bottlenecks

If you actually build this, these are the main bottlenecks.

24.1 Exact matrix multiply
The largest raw cost if you insist on exact arithmetic through dense LLM operations.

24.2 Active remainder explosion
If too many values spill from fixed closed frame into active trees, throughput collapses.

24.3 Prolog binding explosion
Rules with many joins or weak predicates can produce huge frontier blowups.

24.4 Memory bandwidth
Limb arrays and term tables are bandwidth-heavy.

24.5 Divergence
Branchy unification and recursive active normalization will cause warp divergence.

25. Main design choices that determine feasibility

If you want this to fit GPUs well, you should commit to these mechanical choices.

Choice 1: fixed denominator frames are first-class
This makes arithmetic much more regular.

Choice 2: active remainders are sparse spill objects
Do not let every value become a fully recursive heap object.

Choice 3: all names are interned to integers
Mandatory for GPU.

Choice 4: KB/facts/rules are stored columnarly
Mandatory for parallel scan/join.

Choice 5: Prolog is compiled into frontier joins
Much better than recursive interpreter model.

Choice 6: CPU is orchestration control plane
Do not over-force GPU control flow.

26. A concrete end-to-end request flow on GPU

Suppose user asks:
- “Given notebook X, compute candidate causes and rank them.”

Mechanically:

CPU:
- resolve notebook path to kb_id
- build scope chain
- choose abductive inference template
- enqueue query batches

GPU:
- scan evidence facts in scope
- unify candidate causal rules against evidence
- produce candidate cause bindings
- aggregate explained symptom counts
- propagate confidence scores
- sort/rank candidates

CPU:
- inspect top candidates
- decide whether more evidence fetch is needed
- maybe enqueue external operation

GPU:
- update notebook counters/bitsets/LRU summaries
- build structured result rows
- generate grammar masks for answer template

GPU/LLM:
- decode small natural-language wrapper around ranked structured result

That is a very natural mapping.

27. If your real aim is “put all of this into one GPU-resident appliance”

Then the best architecture is:

- GPU-resident persistent KB pools
- GPU-resident term/fact/rule tables
- GPU-resident VDR numeric pools
- GPU-resident LLM weights and decode state
- CPU-resident scheduler and OS bridge

So the CPU mostly:
- submits commands
- resolves path strings
- handles external ops
- monitors jobs

Everything else stays on GPU memory to avoid transfers.

That is much better than bouncing KB/query tensors back and forth.

28. If your real aim is “pipeline the LLM with VDR/Prolog ops”

Then you want speculative parallelism.

While token step t is decoding:
- GPU stream 0: LLM forward
- GPU stream 1: grammar/state mask prep for t+1
- GPU stream 2: KB query prefetch for likely command arguments
- GPU stream 3: VDR primitive execution for already emitted commands
- CPU: orchestration and dependency tracking

This overlaps:
- model generation
- exact compute
- knowledge lookup
- formatting constraints

That’s probably the highest-value pipeline idea in your prompt.

29. Recommended first prototype

If I were building this mapping, I would not start with the whole spec.
I would prototype the GPU substrate in this order:

Phase 1:
- Q335 fixed-limb arithmetic kernels
- exact/surrogate attention with shared denominator
- grammar mask generation
- confidence fraction arithmetic

Phase 2:
- KB fact tables in columnar GPU memory
- scope-filter and predicate-scan kernels
- integer-interned terms

Phase 3:
- batched unification kernel
- simple Datalog-style rule joins
- notebook counters/bitsets/ring buffers

Phase 4:
- active remainder spill pool
- normalization kernels
- limited functional remainder opcodes

Phase 5:
- integrated decode loop with command tokens and asynchronous primitive execution

That gets you the essence of the document in GPU form without drowning in the hardest irregular cases first.

30. Bottom-line mapping

Mechanically, this system maps onto GPUs best if you reinterpret it as:

- exact arithmetic engine = fixed-limb integer kernel library
- VDR active structure = sparse spill-tree arena
- KB = columnar graph/relational store in GPU memory
- Prolog = batched unification + join engine
- LLM = planner/decoder with grammar-constrained token masks
- orchestration = CPU scheduler with GPU work queues

That is the correct hardware-shaped form.

If you want, next I can do one of these:

1. propose a concrete GPU memory layout for VDR/KB/terms/facts
2. design CUDA-style kernels for Q335 arithmetic and active spill handling
3. design a GPU Prolog execution model from query to frontier joins
4. sketch a full streaming pipeline between decode, KB query, and primitive execution
