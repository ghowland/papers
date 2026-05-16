# VDR-18 PERFORMANCE — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → claims → concepts → numeric_classes → operations → bottlenecks → gpu_streams → workload_comparisons → relationships → sections

# principles(id|principle|rationale)
P1|Per-prompt cost not per-operation cost|Single Q335 mul is 200× slower than float16 mul; but 93% fewer tokens means total computation is lower
P2|CPU control plane, GPU data plane|CPU handles sequencing, strings, grants, scheduling; GPU handles parallel numeric work, KB scans, Prolog, LLM forward pass
P3|Integer IDs across boundary|All strings interned on host to integer IDs before device transfer; GPU never processes strings
P4|Fixed-frame regularity|Q335 values have identical width and implicit denominator; every operation same shape; peak GPU utilization on uniform workloads
P5|Grammar-constrained decode|Structural tokens decode over tiny candidate sets (2-20) instead of full vocabulary (50K+); orders of magnitude cheaper
P6|Append-only arenas|No malloc on GPU; bump-pointer allocation; no fragmentation; coalesced access by construction
P7|State in KBs not context window|Per-turn cost flat; no quadratic attention growth; turn 20 costs same as turn 1
P8|Structural safety is computationally free|Visibility check is one bit-test per fact; costs at most 0.017% of prompt time even at enterprise scale

# claims(id|claim|type|depends_on)
CL1|Q335 forward pass ~150× slower per token than float16|observation|
CL2|VDR generates 85-97% fewer LLM tokens (from VDR-15)|observation|
CL3|Net forward pass cost ~10× conventional at 95% token reduction|derivation|CL1,CL2
CL4|Primitive GPU computation for entire SRE investigation is 1.5ms total|observation|
CL5|Primitives computationally invisible — total ops equivalent to <0.001 LLM tokens|derivation|CL4
CL6|Wall-clock crossover favors VDR from turn 7-10 onward for 7B model; earlier for larger models|derivation|CL3,P7
CL7|Grammar-constrained decode gives 850-25000× reduction per structural token|derivation|P5
CL8|VDR 73× faster wall-clock on SRE investigation (9 sec vs 660 sec)|observation|
CL9|VDR 71× cheaper per investigation ($0.39 vs $27.58 including human time)|derivation|CL8
CL10|Second run 42% cheaper than first due to accumulated project state|observation|
CL11|VDR uses ~2.6× more energy per single-turn prompt than conventional|observation|CL3
CL12|Over 20 turns VDR energy profile catches up due to flat per-turn cost|derivation|CL11,P7
CL13|Hardware trajectory favors wider integers; integer tensor cores are engineering not physics|observation|
CL14|Most VDR data structures fit GPU L2 cache; non-LLM ops run at near-peak throughput|observation|
CL15|Q335 active spill rate expected below 1%; Q335 frame provides enormous headroom over typical denominator growth|observation|

# concepts(id|name|definition|category)
C1|Q335 fixed-frame|Numerator as 11×u32 (352 bits) or 6×u64 (384 bits); implicit denominator 2^335; sign via two's complement|representation
C2|Rational surrogate softmax|Each output = square of shifted input / sum of all squared shifted inputs; exact sum-to-one; zero transcendentals|mechanism
C3|String interning|Every unique string assigned sequential integer ID; lookup table maps back; GPU compares integer IDs only|mechanism
C4|Predicate-major columnar storage|All facts sharing predicate stored contiguously; indexed by predicate ID; enables parallel bucket scan|storage
C5|Scope filter on GPU|User's visible KB IDs in bitset; each thread checks candidate fact's kb_id with one bit-test; or DFS in/out intervals (2 int comparisons)|mechanism
C6|Frontier-based Prolog|Recursive depth-first search transformed to batched joins; candidate retrieval → filter → unify → join body goals; borrowed from GPU database query processing|mechanism
C7|Grammar vocabulary mask|Candidate set from grammar state applied as mask to logit vector before surrogate softmax; zeroes impossible tokens|mechanism
C8|Append-only arena|Contiguous GPU memory with bump pointer; allocation is one atomic increment; no sync, no fragmentation, no free-list|allocation
C9|Concurrent GPU streams|5 streams execute simultaneously: LLM forward/decode, KB query/scan, VDR primitives, grammar mask/prep, provenance compaction|execution
C10|Copy-on-write session clone|Persistent stores shared read-only between clones; live state duplicated; new assertions go to clone's delta arena|mechanism
C11|T0 dense shared-frame tensor|All entries share implicit Q335 denominator; numerators as contiguous limb vector arrays; highest throughput path|storage
C12|T1 spill-tagged tensor|Dense layout preserved for closed entries; active entries reference spill arena; for 1-10% active fraction|storage
C13|T2 sparse active tensor|For >10% active fraction; sparse representation or host escalation|storage
C14|Schoolbook multiplication|11×11 = 121 limb-by-limb multiplies with accumulation; ~200 int ops; recommended for Q335 on GPU due to perfect uniformity|algorithm
C15|Deterministic forward pass|Integer arithmetic is platform-independent; same weights + same input = bit-identical output on any hardware|property
C16|Provenance event log|Append-only structure-of-arrays: event_type, tool_id, subject_ref, input_begin, input_count, output_ref, confidence_ref, turn|storage
C17|Canonical ordering|Events stamped with (turn, batch_sequence, item_sequence); post-sorted by parallel radix sort|mechanism
C18|Power-of-two split|After Q335 multiply, bits above position 335 = quotient (new V), bits below = remainder; fixed-position extraction|mechanism

# numeric_classes(id|class|representation|use_cases|perf_profile)
N1|Small integers|Signed 32/64-bit immediate|KB IDs, counters, bitset words, term payloads|Native GPU int ops; no penalty vs float
N2|Q335 closed|Fixed-width 11×u32 limb vector; implicit 2^335 denominator|Common case for all exact arithmetic|~200 int ops per mul; perfectly regular
N3|General closed rationals|Explicit numerator + denominator limb refs in arena|Values not fitting Q335; external exact fractions|Variable width; arena-allocated
N4|Active VDR values|Triple with nonzero remainder; remainder tag + payload ref|Operations exceeding Q335 frame|Minority case; arena-allocated; normalization needed

# q335_operations(id|operation|int_ops|float16_ops|ratio|gpu_parallelism)
QO1|Addition|~22 (11 limb adds + carries)|1|22×|Full — uniform
QO2|Subtraction|~22|1|22×|Full
QO3|Multiplication|~200 (schoolbook 11×11)|1|200×|Full — uniform
QO4|Comparison|2-22 (fast path to full scan)|1|2-22×|Full
QO5|Division by Q335|~400 (mul + shift + remainder)|1|400×|Full
QO6|Surrogate softmax per element|~220 (sub + square + div)|~15 (exp + div)|15×|Full — no transcendentals, no divergence
QO7|ReLU|2 (compare + conditional copy)|2|1×|Full — identical

# forward_pass_components(id|component|conventional_cost|vdr_cost|ratio|notes)
FP1|Embedding lookup|1 read per dim|11 reads per dim (limb width)|11×|Memory-bound
FP2|Attention QKT|d_k muls per position pair|d_k × 200 int ops per pair|200×|Multiplication dominated
FP3|Softmax/surrogate|~15 ops/element (transcendental)|~220 ops/element (integer)|15×|VDR avoids transcendental divergence
FP4|Value mixing|d_v muls per position|d_v × 200 int ops|200×|Same structure, wider ops
FP5|Feedforward ReLU|2 ops/element|2 ops/element|1×|Identical — piecewise linear
FP6|Feedforward linear|d_ff muls|d_ff × 200 int ops|200×|Multiplication dominated
FP7|Layer norm / rational scaling|~10 ops/element|~25 ops/element|2.5×|VDR avoids sqrt
# Weighted average across components: ~150× per token

# bottlenecks(id|bottleneck|severity|description|mitigation)
BN1|LLM forward pass Q335 cost|Primary|100-500× slower per element than float16; 150× weighted average per token|85-97% fewer tokens; grammar-constrained decode; net ~10× at 95% reduction
BN2|Active value management|Secondary|Arena growth, normalization passes, irregular remainder structures when values exceed Q335|Keep spill rate below 1% via Q335 frame sizing and Q-basis reprojection
BN3|Large Prolog frontiers|Tertiary|Frontier explosion on unrestricted cross-scope scans with variable predicates|Query planning on CPU; scope restriction; predicate indexing; typical queries moderate frontier
BN4|Host-device synchronization|Tertiary|Round trip at each command token boundary for path resolution, grant verify, opcode lowering|Overlap LLM decode with primitive execution via concurrent streams; batch command lowering

# gpu_streams(id|stream|resources|memory_accessed|overlaps_with)
GS0|LLM forward/decode|Tensor ALUs, shared memory|Weight tensors, activation buffers|GS1, GS3, GS4
GS1|KB query/scan|Integer ALUs, global memory|Fact tables, term pool, indexes|GS0, GS2, GS3
GS2|VDR primitives|Integer ALUs, global memory|Value arenas, live-state arrays|GS0, GS3, GS4
GS3|Grammar mask/prep|Integer ALUs, shared memory|Grammar state, candidate buffers|GS0, GS1, GS2
GS4|Provenance compact|Memory copy engines (DMA)|Provenance arena, event buffers|All (uses DMA not ALUs)

# scope_filter_strategies(id|strategy|setup_cost|per_fact_cost|best_for)
SF1|Linear scan|0|O(scope_depth) comparisons|Tiny trees (<50 KBs)
SF2|Binary search|O(depth × log depth)|O(log scope_depth)|Small-medium trees
SF3|Bitset|O(scope_depth) bit-sets|1 bit-test|Medium trees (<4096 KBs)
SF4|DFS interval|O(tree_size) DFS precomputation once|2 int comparisons|Large trees, subtree queries
SF5|Interval + shadow|O(tree_size) + O(mount_count)|2-4 int comparisons|Large trees with mounts

# prolog_join_strategies(id|strategy|build_cost|probe_cost|best_frontier_size|gpu_efficiency)
PJ1|Nested loop|0|O(N) per probe|<100 rows|Low (divergence)
PJ2|Hash join|O(N) build|O(1) avg per probe|100-100K rows|High
PJ3|Sort-merge|O(N log N) sort|O(1) amortized|10K-1M rows|High
PJ4|Bitmap semijoin|O(N) build bitmap|O(1) bit test|Any size, filter joins|Very high

# live_state_gpu(id|type|gpu_implementation|cost)
LS1|Counters|Dense signed int arrays; one atomic add per increment; one comparison per bound check|1 atomic op per increment
LS2|Bitsets|Packed 64-bit words; OR/AND-NOT/AND for set/clear/test|1 bitwise op per operation
LS3|Ring buffers|Fixed-capacity array + atomic write position; contiguous read = 1 coalesced transaction|1 atomic + 1 write per append
LS4|Queues/stacks|Batched push/pop; prefix-sum for offsets + bulk copy; single-item contention host-assisted|Efficient in batches; contended singles expensive
LS5|LRU caches|Host-managed exact LRU for correctness-critical; device-side approximate LRU for high-throughput|Most complex; host-managed recommended

# spill_thresholds(id|active_fraction|tensor_class|action|overhead)
SP1|0%|T0 shared-frame dense|No action; optimal path|Baseline
SP2|0.01-0.1%|T0 + sparse spill tags|Tag active entries; slow path|Negligible
SP3|0.1-1%|T1 dense + spill tags|Per-element tag check|1-5%
SP4|1-5%|T1 + tile-local spill tables|Group active per tile; batch|5-15%
SP5|5-10%|T1 → T2 transition|Consider reprojection|15-30%
SP6|>10%|T2 sparse or host intervention|Sparse repr or reproject entire tensor|30-50%; reprojection recommended

# functional_remainder_costs(id|function|algorithm|ops_per_depth|depth_100_digits|total_q335_ops|time_h100)
FR1|SQRT|Newton iteration|~600|8|~4,800|0.06 ms
FR2|EXP|Taylor series|~600/term|45|~27,000|0.3 ms
FR3|LOG|Series + argument reduction|~600/term|~33 (with reduction)|~20,000|0.2 ms
FR4|SIN|Taylor odd terms|~800/term|45|~36,000|0.4 ms
FR5|COS|Taylor even terms|~800/term|45|~36,000|0.4 ms
FR6|ARCTAN|Taylor + Machin identity|~600/term|~25 (with Machin)|~15,000|0.2 ms
FR7|ZETA|Borwein method|~200/term|210|~42,000|0.5 ms

# implementation_phases(id|phase|contents|target_throughput|validation)
IP1|Phase 1|Q335 arithmetic, dense tensor kernels, surrogate attention, confidence|1M Q335 muls/sec; surrogate softmax 10K rows/sec at d=512|Correctness vs Python reference; sum-to-one verified
IP2|Phase 2|KB metadata + fact tables, scope filtering, interned terms, fact queries|10M facts/sec scan; scope filter <0.1ms for 100K facts|Query correctness vs Python Prolog reference
IP3|Phase 3|Frontier unification, rule joins, binding buffers, live-state primitives|100K unifications/sec; joins <1ms for 1K×1K|Derivation correctness; binding consistency
IP4|Phase 4|Active spill arena, normalization, functional remainders|Normalization <10ms for 10K active nodes; fn_sqrt depth 8 <1ms|Normalized forms match reference; convergence verified
IP5|Phase 5|Full command pipeline, grammar decode, provenance, sessions|End-to-end <5sec for 210-token SRE scenario|Full system benchmark vs Python prototype
# Dependencies: IP1→IP2→IP3→IP5; IP1→IP4→IP5

# gpu_utilization(id|operation|conventional|vdr|reason)
GU1|Matrix multiply|85-95% (tensor core)|60-80% (integer, general ALUs)|Hardware optimization gap
GU2|Softmax|40-60% (transcendental divergence)|80-95% (integer surrogate, uniform)|No transcendentals
GU3|KB scan|N/A|90%+ (columnar, coalesced)|Standard GPU database operation
GU4|Scope filter|N/A|95%+ (bitset test)|One bit op per element
GU5|Prolog unification|N/A|70-85% (minor divergence on term types)|Frontier-based; mostly uniform
GU6|Grammar-constrained decode|N/A (always full vocab)|95%+ (tiny candidate set)|Orders of magnitude less work
GU7|Provenance append|N/A|90%+ (atomic bump, bulk copy)|Minimal sync
GU8|Counter/bitset ops|N/A|95%+ (atomic int)|Single instruction per element

# workload_comparison(id|workload_type|conventional_advantage|vdr_advantage|net_winner)
WC1|Free-text generation (novel, poem)|Faster forward pass; dominates|Grammar provides little benefit|Conventional
WC2|Structured data + computation (SRE, portfolio)|N/A|85-97% fewer tokens; primitive offload; exact results|VDR
WC3|Multi-turn reasoning|N/A|Flat per-turn cost; no quadratic attention growth|VDR (from turn 7-10+)
WC4|KB operations|Attention-based "search" through context|Indexed GPU scan at millions of facts/sec|VDR
WC5|Logical deduction|Token prediction; unreliable at chain depth|Frontier Prolog; exact; scales with frontier not depth|VDR
WC6|Decode (structural tokens)|Full-vocab softmax every token|Grammar-constrained; 850-25000× cheaper per structural token|VDR
WC7|Decode (free text)|Standard softmax|Surrogate ~15× more expensive per element|Conventional per-token
WC8|Arithmetic|Digit-by-digit token prediction; inaccurate|GPU-parallel Q335; exact; milliseconds for thousands of ops|VDR

# sre_case_study(phase|description|conv_tokens|vdr_tokens|vdr_gpu_ops|vdr_wall_ms|conv_data_coverage|vdr_data_coverage)
CS1|Data acquisition|200 gen + 12K context|72|1.2M|750|25% (50/200 endpoints)|100%
CS2|Filtering + threshold|2,000|38|29K|300|~85% accuracy on 25%|100% accuracy on 100%
CS3|Deployment correlation|3,000 gen + 3K context|108|54K|930|Moderate accuracy, 25%|Exact, 100%
CS4|Statistics + ranking|2,500|44|5K|440|Errors in arithmetic, 25%|Exact, 100%
CS5|Complex transform (Python)|700|92|75K|985|Manual by user|Automated sandbox
CS6|Versioned project storage|200|183|20K|300|Nothing saved|Full versioned project + comparison rule
CS7|Formatted output + export|1,500|232|86K|2,010|Prose with errors, no export|Grammar-perfect tables, CSV+JSON export
# Totals: Conventional 10,100 gen + 15,000 context = 25,100 tokens; VDR 769 tokens (92.4% reduction)
# VDR total GPU primitive time: 1.5ms. Wall-clock: 9 sec vs 660 sec (73× faster). Cost: $0.39 vs $27.58 (71× cheaper)

# gpu_arch_throughput(arch|year|sms|int32_ops_sec|q335_adds_sec|q335_muls_sec)
GA1|Volta GV100|2017|80|7.9T|360M|40M
GA2|Ampere A100|2020|108|9.7T|440M|50M
GA3|Hopper H100|2022|132|16.9T|770M|85M
GA4|Ada RTX 4090|2022|128|16.4T|745M|83M
GA5|Blackwell B200|2024|160+|25T+|1.1B+|125M+
# Sufficient for VDR workloads: total mul count per prompt is thousands to millions, not trillions

# energy_and_cost(id|metric|conventional|vdr|ratio|notes)
EC1|Energy per single-turn prompt|8.4 J|22 J|2.6× more (VDR)|Forward pass dominated both systems
EC2|GPU time (SRE single turn)|~30 sec|~4 sec|7.5× less (VDR)|Token reduction dominates
EC3|GPU cost per prompt (H100 $3/hr)|$0.025|$0.0033|7.5× cheaper (VDR)|
EC4|Total cost incl human time (SRE)|$27.58|$0.39|71× cheaper (VDR)|SRE time at $150/hr
EC5|GPU time (20-turn)|~600 sec|~80 sec|7.5× less (VDR)|Conventional grows quadratically; VDR flat

# determinism_guarantees(id|component|deterministic|condition)
DG1|Q335 addition|Yes|Always — integer arithmetic
DG2|Q335 multiplication|Yes|Always
DG3|KB fact query result set|Yes|Canonical sort applied to set
DG4|Prolog first-solution|Yes|Canonical candidate ordering imposed
DG5|Confidence propagation|Yes|Same formula, same inputs
DG6|Grammar mask|Yes|Same grammar state, same candidates
DG7|Forward pass output|Yes|Bit-identical on any hardware — no platform-dependent rounding

# relationships(from|rel|to)
P1|grounds|CL3
P1|opposes|CL1
P2|enables|C3
P2|enables|C9
P3|implements|C3
P4|enables|GU1
P4|enables|C1
P5|enables|CL7
P5|implements|C7
P6|implements|C8
P7|enables|CL6
P7|opposes|BN1
P8|implements|C5
CL1|qualifies|BN1
CL2|enables|CL3
CL2|enables|CL8
CL3|derives_from|CL1
CL3|derives_from|CL2
CL5|derives_from|CL4
CL6|derives_from|CL3
CL6|derives_from|P7
CL7|derives_from|P5
CL8|derives_from|CL2
CL9|derives_from|CL8
CL10|enabled_by|P7
CL13|enables|BN1
CL15|constrains|BN2
C1|enables|QO1
C1|enables|QO3
C1|enables|C11
C2|replaces|FP3
C2|enables|GU2
C4|enables|GU3
C5|enables|GU4
C5|enables|P8
C6|enables|GU5
C6|uses|PJ2
C6|uses|PJ3
C6|uses|PJ4
C7|enables|GU6
C7|enables|CL7
C8|enables|C16
C8|enables|GU7
C9|enables|BN4
C9|implements|GS0
C9|implements|GS1
C9|implements|GS2
C9|implements|GS3
C9|implements|GS4
C10|uses|C8
C11|enables|FP1
C14|implements|QO3
C15|implements|DG7
C16|implements|C17
C18|implements|QO3
N1|subtype_of|C1
N2|instance_of|C1
N3|stored_in|C8
N4|stored_in|C8
N4|triggers|BN2
SP1|uses|C11
SP3|uses|C12
SP6|uses|C13
BN1|mitigated_by|CL2
BN1|mitigated_by|P5
BN2|mitigated_by|SP1
BN3|mitigated_by|C6
BN4|mitigated_by|C9
IP1|enables|IP2
IP1|enables|IP4
IP2|enables|IP3
IP3|enables|IP5
IP4|enables|IP5
WC2|demonstrates|P1
WC3|demonstrates|P7
WC4|demonstrates|C4
WC5|demonstrates|C6
WC6|demonstrates|P5

# section_index(section|title|ids)
1|The Performance Objection|P1,CL1,CL2,CL3
2|The GPU Mapping|P2,P3,C3
3|The Numeric Model|N1,N2,N3,N4,C1,SP1-SP6,CL15
4|Q335 Arithmetic on GPU|QO1-QO7,C14,C18
5|Why GPU Utilization Favors VDR|C2,GU1-GU8,P4
6|KB Operations on GPU|C4,C5,SF1-SF5,P8
7|Prolog on GPU|C6,PJ1-PJ4,GU5
8|The Forward Pass|FP1-FP7,C11,C12,C13,C15
9|Grammar-Constrained Decode|P5,C7,CL7,GU6
10|Concurrent Execution|C9,GS0-GS4
11|Memory and Allocation|P6,C8
12|Live State on GPU|LS1-LS5
13|Provenance on GPU|C16,C17,GU7
14|Sessions, Snapshots, Clones|C10
15|The Actual Bottlenecks|BN1-BN4,CL3
16|Comparative Analysis|WC1-WC8
17|Hardware Trajectory|CL13,GA1-GA5
18|Real Workloads|CL8,CL9,CL10,CS1-CS7
A|Q335 Operation Cost|QO1-QO7,FP1-FP7
B|Token Count vs Operation Count|CS1-CS7,CL6
C|Grammar Decode Savings|CL7
D|GPU Utilization Comparison|GU1-GU8
E|Memory Layout|C1,C4,C8
F|Concurrent Stream Execution|GS0-GS4
G|Bottleneck Analysis|BN1-BN4
H|Implementation Phases|IP1-IP5
I|Integer ALU Throughput|GA1-GA5
J|Memory Bandwidth|CL14
K|Karatsuba Threshold|C14
L|Scope Filter Strategies|SF1-SF5
M|Prolog Join Strategies|PJ1-PJ4
N|Functional Remainder Cost|FR1-FR7
O|Determinism Verification|DG1-DG7
P|Power-of-Two Split|C18
Q|Tensor Core Feasibility|CL13
R|Spill Thresholds|SP1-SP6
S|Host-Device Sync Cost|BN4
T|Comparison with Approximate GPU|C15
U|Energy and Cost|EC1-EC5
Addendum|SRE Case Study|CS1-CS7,CL8,CL9,CL10

# decode_legend
format: pipe-delimited tables, ID-based cross-references
claim_types: axiom|observation|derivation
concept_categories: representation|mechanism|storage|allocation|execution|property|algorithm
q335_layout: 11×u32 (352 bits) or 6×u64 (384 bits); implicit denominator 2^335
tensor_classes: T0 (dense shared-frame)|T1 (dense + spill tags)|T2 (sparse active)
numeric_classes: N1 small int|N2 Q335 closed|N3 general rational|N4 active VDR
gpu_streams: GS0-GS4 concurrent; overlap on different memory/ALU units
spill_thresholds: SP1-SP6 by active fraction percentage
join_strategies: PJ1-PJ4 by frontier size
scope_strategies: SF1-SF5 by KB tree size
bottleneck_severity: Primary|Secondary|Tertiary
workload_winners: Conventional (free-text dominated)|VDR (structured/multi-turn/data/logic)
per_token_cost_ratio: ~150× (Q335 vs float16 weighted average across forward pass components)
token_reduction: 85-97% (from VDR-15)
rel_types: grounds|opposes|enables|implements|derives_from|qualifies|uses|replaces|subtype_of|instance_of|stored_in|triggers|mitigated_by|constrains|demonstrates|enabled_by
+standalone: no cross-references to other compact docs
+no_new_primitives: paper introduces no new primitives; analyzes GPU mapping of existing VDR-1 through VDR-16 components
