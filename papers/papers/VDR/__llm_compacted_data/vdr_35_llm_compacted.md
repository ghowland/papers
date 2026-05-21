# HOWL-VDR-35-2026 — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: problem → type_system → core_instruction → softmax → kb_on_gpu → prolog_gpu → grammars → sessions → safety → universal_cycle → runners → server → confidence → api → implementation → testing → deployment → comparison → energy

# problem(id|aspect|description)
PR1|float complexity|GPU software stack manages FP4/FP6/FP8/FP16/BF16/TF32/FP32/FP64 hierarchy; Transformer Engine dynamically selects per layer; mixed-precision requires loss scaling, gradient clipping, warmup, NaN recovery
PR2|float failure modes|NaN propagates silently; Inf from overflow; subnormals lose precision; non-associative addition → non-deterministic allreduce; thread-dependent rounding
PR3|integer eliminates all|integers cannot be NaN/Inf/subnormal; addition associative; deterministic across all platforms, thread schedules, reduction topologies

# type_system(id|type|D|struct_size|precision_floor|purpose)
TS1|Q16|2^16=65536|8 bytes (i32 value + i16 remainder + i16 padding)|1.53×10⁻⁵|primary operational: weights, activations, attention scores, gradients, optimizer state
TS2|Q32|2^32|16 bytes (i64 value + i32 R0 + i32 R1)|2.33×10⁻¹⁰|intermediate precision: long-sequence accumulation, values >1.0 at full precision
TS3|Q335|2^335|240 bytes (6×i64 limbs + 4 remainder levels)|~10⁻¹⁰¹|high-precision transcendental computation; remainder depth fixed at 4 (beyond R3 truncated, R3 tells exactly how much left)
# denominator never stored — compile-time constant; compiler tracks Q-basis per register/pointer; no implicit conversions; explicit reproject required

# core_instruction(id|description)
CI1|widening multiply: i16×i16→i32 (Q16); shift right by 16: quotient=new V; mask low 16: remainder=R0
CI2|on H100: INT8 tensor cores deliver 3,958 TOPS vs FP16 1,979 TFLOPS — integer path 2× float on same silicon
CI3|eliminates: entire float pipeline, FP4-FP64 type hierarchy, conversion functions, mixed-precision orchestration, Transformer Engine, SFU for transcendentals, NaN/Inf/subnormal branches, warp divergence from data-dependent special cases

# softmax(id|aspect|description)
SM1|quadratic surrogate|shift logits so min=0, square each, divide by sum of squares; exact VDR fractions summing to D by construction
SM2|verification|Zig toy confirms softmax_sum=65536 every epoch, every forward pass, every generation step; integer equality not tolerance
SM3|SFU elimination|integer multiply+add+divide at full warp throughput; no SFU serialization; no data-dependent divergence
SM4|open question|whether quadratic gradient landscape matches exp-softmax at production scale; FRU makes both available as configuration choice

# kb_on_gpu(id|aspect|description)
KG1|struct|256 bytes padded for cache alignment; 26 fields: identity (name, path, i32 id), persistent (facts, rules, constraints, connections, grammars), live (working data, LRU, counters, locks, queues, stacks, ring buffers, bitsets), structural (parent_id, children_ids, mounts), metadata (visibility, frozen, owner, timestamps)
KG2|memory layout|contiguous GPU global memory; fixed struct size → zero fragmentation; 100K KBs + 10M facts + 100K rules + 10K sessions ≈ 2.2 GB device memory (negligible vs 56 GB for 7B Q16 model)
KG3|shared memory cache|16 KB structs + 512 facts fit in ~24 KB shared memory (H100 has 228 KB/SM); Prolog loads candidates here for parallel unification
KG4|access pattern|small random reads by integer ID (latency-sensitive); opposite of weight-matrix sequential tile loads (bandwidth-sensitive); VDRProlog exposes scheduling hints: MAC kernels vs Prolog kernels vs Primitive kernels

# prolog_gpu(id|aspect|description)
PG1|parallelization|load candidate facts into shared memory (512/SM); distribute across warps (32 threads each handle one candidate); cross-multiply comparison per thread; warp-level vote filters matches; surviving candidates for recursive body evaluation
PG2|structural equivalence|parallel database join where comparison operator is integer equality
PG3|depth-first search|sequential within a branch; independent branches parallel across SMs; depth limit 100

# grammar_gpu(id|aspect|description)
GR1|structural tokens|measured: Python ~40%, JSON ~55%, tables ~65%, prose+data ~30%, pipe-delimited ~80% — all predicted through full forward passes in conventional systems
GR2|replacement|template declares typed slots; grammar fills structural bytes via memcpy + integer-to-string; LLM fills content slots only
GR3|guarantees|syntactic correctness by construction; JSON cannot be malformed; grammars persist in KBs, inherit through tree, zero cost per reuse

# sessions(id|aspect|description)
SS1|isolation|user_id (i32) + visibility (enum) + KB root (i32) + grants + resource limits; VDRProlog stream carries credentials; every kernel inherits them; every KB access checks via integer comparison
SS2|snapshots|atomic capture of all session state: KBs, facts, rules, terms, grammars, live state (7 primitives), grants; contiguous binary blob + CRC32 checksum; bit-identical restore because integers
SS3|clones|COW sharing of parent's persistent KBs; first write copies page to private region; parent never sees clone modifications; clone never sees parent changes
SS4|recycle|snapshot → kill (destroy drift) → clone from snapshot (fresh session with identical knowledge); "snapshot is factory, clones disposable, knowledge persists, drift dies"
SS5|exact reproduction|clone starts bit-identical to snapshot; integer copy is exact; no generational drift from copy-of-copy degradation; hundreds of recycle cycles produce perfect forks

# snapshot_sizes(id|profile|kbs|facts|rules|size|save_time_cpu)
SN1|minimal (single query)|3|50|0|4 KB|~10 μs
SN2|standard SRE (fresh)|25|800|15|52 KB|~100 μs
SN3|standard SRE (mature)|60|4,200|185|245 KB|~500 μs
SN4|heavy document processing|150|20,000|50|1.1 MB|~2 ms
SN5|maximum tested|1,000|200,000|500|11 MB|~20 ms
# scales linearly with fact count (40 bytes/fact); H100 HBM transfers 11 MB in ~3 μs

# safety(id|mechanism|description)
SF1|access control|integer visibility check walks target KB up parent chain; any unreachable ancestor → target invisible; no prompt modifies any integer in any check
SF2|grants|operational primitives require positive credential grant; struct: class, target, remaining_uses (i32), expiry (i32), holder; check: 4 integer comparisons; atomic decrement on use
SF3|grant lifecycle|ACTIVE → EXPIRED (time) / EXHAUSTED (uses=0) / REVOKED (admin); all terminal, permanent; no runner can modify own grants
SF4|audit|every operation produces entry: timestamp, session_id, user_id, action, target, grant_id, result; append-only ring buffer (default 1M entries, 28 bytes each); ~12-80 KB/hour

# universal_cycle(id|phase|description|tokens)
UC1|Phase 0: pre-LLM rule evaluation|fire all matching Prolog rules against current KB state; if fully resolved with confidence above threshold + grammar available → complete without LLM|0 (L3 path; 93% of mature operations)
UC2|Phase 1: context assembly|system prompt (~200 tokens cached), scope reference (~5), scratchpad with auto-fired results (0-50), current input; NO prior turns, data, reasoning, or templates|~350 tokens constant regardless of turn number
UC3|Phase 2: LLM generation + command dispatch|command tokens (~8 per invocation, ~300 known names, ~2 bits entropy) dispatched to system; prose passed to output; kb:// URIs resolved from KB + grammar rendered|variable
UC4|Phase 3: post-cycle|update session counters (turn, tokens, commands, L1/L2/L3 distribution as exact fractions); auto-snapshot if configured; check recycle threshold|0

# execution_levels(id|level|tokens|description)
EL1|L1|50-500|full LLM judgment; may formalize as Prolog rule (25-40 tokens) transitioning pattern to L2
EL2|L2|~8 command + ~10 prose framing|LLM recognizes stored rule applies, emits query, wraps result
EL3|L3|0|Prolog rule fires during Phase 0 without LLM; grammar renders from KB

# runners(id|type|input|behavior|freshness)
RN1|poller|synthetic "poll cycle N" on timer (default 60s)|fires triage rules against KB state; zero LLM if rules handle all|fresh stream each cycle — no attention degradation
RN2|processor|persistent external connection (Prometheus, deploy pipeline, etc.)|compacts data into KB facts; known patterns L3, novel L1; reconnect with exponential backoff 1s→60s cap|recycles at 200-turn threshold: snapshot→kill→clone→restore connection
RN3|internal|scheduled computation (rolling averages, trends, coverage gaps)|KB queries + exact VDR arithmetic + KB assertions; zero LLM unless novel pattern|periodic schedule
RN4|batch|tasks from KB queue|clones parent per task for isolation; merges results back; up to max_concurrent clones|clone-per-task; corrupt task affects only its clone
# all runners scheduled on host thread pool (default: half hardware threads)

# recycle_timing(id|session_size|total_recycle_time|data_gap)
RT1|10 KB minimal|70 μs|~0 (sub-ms)
RT2|50 KB standard SRE|240 μs|~0 (sub-ms)
RT3|250 KB mature SRE|1,020 μs|~1 ms
RT4|3 MB maximum typical|9.6 ms|~10 ms
# at 200-turn/1s interval: recycle every ~3.3 min; 436 recycles/day at 10 ms each = 4.36 seconds = 0.005% overhead

# server(id|aspect|description)
SV1|connection handling|TCP accept → protocol handshake (HTTP/WebSocket/SMTP/MQTT/raw TCP) → authenticate → clone from template snapshot
SV2|credentials|user_id (i32), visibility (i8), pre-resolved grants, issued_at (i32), expires_at (i32); valid = valid_flag AND current_time < expires_at; two integer comparisons per request
SV3|request processing|transform to vlp_input → universal cycle on session-bound stream → transform output via grammar templates
SV4|protocol grammars|HTTP: status line + header + body grammars; every structural byte from grammar; LLM generates content slot values only
SV5|rate limiting|bounded counters per user in auth KB; check: counter >= max? integer comparison; no drift, no false crossings
SV6|lifecycle|stateless (clone destroyed after response) or stateful (session persists across messages); snapshot on disconnect

# confidence(id|aspect|description)
CF1|hierarchy|VDR computation 1/1, Prolog derivation 1/1, DB query 98/100, Prometheus 95/100, script 95/100, REST API 85/100, peer-reviewed 80/100, user 70/100, web search 50/100, LLM content 30/100, unknown 0/1
CF2|propagation|agreeing: 1−∏(1−Cᵢ); conflicting: penalty multiplier; chain of N links at C: Cᴺ; all computed as exact VDR fractions
CF3|provenance|every fact has: source_type, source_kb_id, source_slot_id, confidence, timestamp, derivation_rule_id; chain traceable to original sources

# api_modules(id|module|functions|replaces|new_capability)
AP1|core runtime|36|CUDA Runtime (~120)|session-scoped streams with credentials
AP2|VDR math|17|cuBLAS (~250)|exact arithmetic with remainder monitoring; one GEMM replaces dozens of precision variants
AP3|attention|3|cuDNN attention (~50+)|exact softmax verification (zero violations expected)
AP4|training|10|custom loops + AMP + GradScaler|exact gradients, no loss scaling, no clipping
AP5|knowledge bases|14|— (no equivalent)|persistent data at integer addresses
AP6|KB primitives|30|— (no equivalent)|bounded working memory
AP7|Prolog|8|— (no equivalent)|deterministic deduction with GPU parallelism
AP8|grammar|7|— (no equivalent)|structural token generation bypassing LLM
AP9|runner|8|— (no equivalent)|autonomous background execution
AP10|session|10|— (no equivalent)|exact snapshot/clone/kill lifecycle
AP11|safety|6|guardrail frameworks|integer access control and grant enforcement
AP12|confidence|5|— (no equivalent)|exact provenance propagation
AP13|distributed|10|NCCL (~100)|deterministic allreduce (integer associative)
AP14|transform|4|cuFFT (~80)|exact DFT roundtrip
AP15|linear algebra|8|cuSOLVER (~200)|exact decompositions
AP16|statistics|8|custom code|exact fractions throughout
AP17|number theory|7|custom code|integer-native computation
AP18|functional remainder|8|SFU hardware|software/hardware transcendentals
AP19|builtins|448|LLM token generation|deterministic primitives at KB addresses
AP20|profiling|4|Nsight (simplified)|determinism verification as first-class test
# total: ~580 functions replacing ~4,000+ conventional; ~110 equivalent functions (28.6× reduction from eliminating precision variants) + ~470 new capabilities

# build_phases(id|phase|depends_on|scope|lines|test_env|tests)
BP1|Phase 1: Arithmetic + KB|nothing|Q16 type+ops, KB store, fact CRUD, tree, path index, visibility, text store|~2,500|local, any machine|119
BP2|Phase 2: Prolog + Grammar + Session|Phase 1|Prolog engine, grammar engine, session lifecycle (snapshot/clone/COW/merge/kill), 7 data primitives, grants, audit, confidence|~5,500|local|+151 (270)
BP3|Phase 3: Inference + Builtins|Phases 1-2|universal cycle, context builder, command parser/dispatcher, LLM engine (forward/attention/softmax/generate/KV-cache/sampling), ~200 builtins, seed layer|~7,000|local (toy model)|+207 (477)
BP4|Phase 4: Runners + Server|Phases 1-3|thread pool, 4 runner types, HTTP/WebSocket server (auth, credentials, rate limiting, health, reaper, shutdown), grant-gated ops (fs/net/exec/compile/process), config|~6,000|local|+55 (532)
BP5|Phase 5: GPU Kernels|Phases 1-4|device init, GPU kernels (MAC, softmax, attention, layernorm, elementwise, Prolog unification, sort), KB on device, host-device transfer, profiling|~6,000|GCP T4/H100|+60 (592)
BP6|Phase 6: Production|Phases 1-5|multi-device parallelism, deterministic allreduce, KB replication, load balancing, monitoring, full protocols (SMTP, MQTT, DNS)|~3,000|GCP multi-GPU|+20 (612)
# total: ~30,000 lines code + ~5,000 lines tests across 168 files; Zig 0.14; zero external dependencies Phases 1-4

# file_structure(id|directory|files|lines|purpose)
FS1|src/vdr/|5|~800|Q16, Q32, Q335 types and operations
FS2|src/kb/|7|~1,700|store, fact, tree, path_index, visibility, text_store
FS3|src/prolog/|6|~1,500|term, unify, query, rule, hygiene
FS4|src/grammar/|5|~900|compile, render, validate, inherit
FS5|src/session/|4|~1,200|lifecycle, COW, snapshot
FS6|src/primitives/|8|~1,400|LRU, counter, lock, queue, stack, ring, bitset
FS7|src/safety/|3|~600|grant, audit
FS8|src/confidence/|2|~300|propagate
FS9|src/engine/|8|~2,000|cycle, context, command_parse/exec, scratchpad, auto_resolve, token_classify, level_stats
FS10|src/llm/|7|~1,800|model, forward, attention, softmax, generate, kv_cache, sampling
FS11|src/builtins/|12|~4,000|dispatch + 11 category files
FS12|src/seed/|5|~800|init, oso_rules, hygiene_rules, confidence_table, command_vocab
FS13|src/runner/|6|~2,000|pool, poller, processor, internal, batch
FS14|src/server/|8|~2,500|listener, handler, auth, rate_limit, health, reaper, shutdown
FS15|src/protocol/|5|~1,500|HTTP, WebSocket, SMTP, MQTT, grammars
FS16|src/ops/|5|~1,000|filesystem, network, execute, compile, process
FS17|src/config/|3|~500|system_config, cli, config_file
FS18|src/gpu/|11|~6,000|device, 7 kernel types, kb_device, transfer, profiling
FS19|src/deploy/|5|~1,500|gcp_setup, multi_device, distributed, load_balancer, monitoring
FS20|test/|~50|~5,000|all modules

# gcp_costs(id|resource|phase|hours|cost_per_hour|total)
GC1|T4 instance (n1-standard-8)|Phase 5 dev|~40|$0.35|$14
GC2|H100 instance (a3-highgpu-1g)|Phase 5 bench|~8|$12|$96
GC3|H100 8× (a3-highgpu-8g)|Phase 6 multi-GPU|~20|$100|$2,000
GC4|T4 sustained test|Phase 5-6|~48|$0.35|$17
GC5|total|||—|~$2,127

# invariants(id|invariant|verification)
IV1|softmax sum = D exactly|VDRPrologAttentionVerifySoftmaxSum; zero violations
IV2|KB facts at integer addresses are exact|assert-query roundtrip, byte comparison
IV3|bounded primitives respect declared capacity|push at capacity returns false / evicts oldest
IV4|snapshot restore is bit-identical|save, modify, restore, memcmp entire state
IV5|clone COW invisible to parent|modify clone, verify parent unchanged
IV6|access-denied data is absent not filtered|query from unauthorized session returns zero results
IV7|grant denial precedes execution|deny grant, verify no side effect
IV8|arithmetic deterministic across devices|100 runs on GPU, memcmp all outputs
IV9|Prolog unification uses exact comparison|cross-multiply, no tolerance parameter
IV10|audit log append-only and complete|count entries, match to operation count

# eliminated_components(id|component|reason|replacement)
EL_1|cuBLAS precision variants|one integer type per Q-basis|VDRPrologVdrGemm with Q-basis param
EL_2|cuDNN mixed-precision layers|no precision mixing|VDRPrologAttentionForward
EL_3|TensorRT quantization calibration|model is integer natively|not needed
EL_4|NCCL non-deterministic allreduce|integer sum associative|VDRPrologDistAllReduce (deterministic)
EL_5|loss scaling (GradScaler)|integers cannot overflow to Inf|not needed
EL_6|gradient clipping|exact gradients don't explode|not needed
EL_7|NaN detection and recovery|integers cannot be NaN|not needed
EL_8|warmup schedules|no early-training float instability|not needed
EL_9|epsilon parameters|exact division; zero-denom detectable|not needed
EL_10|rounding mode selection|integers don't round|not needed
EL_11|subnormal handling|no subnormals|not needed
EL_12|Transformer Engine FP8/FP16 switching|one type, no switching|not needed
EL_13|mixed-precision conversion functions|no implicit conversion|explicit reproject only
EL_14|tolerance-based testing|exact comparison|byte-identical comparison

# warp_divergence(id|source|float_frequency|VDRProlog_frequency|impact)
WD1|NaN check|every operation|never|2-5% warp idle
WD2|Inf check|every accumulation|never|1-3%
WD3|subnormal handling|occasional|never|1-2%
WD4|mixed-precision conversion|per-layer|never|3-8%
WD5|SFU serialization|every softmax/activation|never|10-30% on attention layers
WD6|epsilon comparison|every LayerNorm/Adam|never|1-2%
WD7|loss scale overflow|every backward|never|1-2%
WD8|gradient clip branch|every param update|never|1-3%
WD9|dynamic precision selection|per-tensor|never|3-5%
# cumulative float loss: 15-40%; VDRProlog: zero arithmetic divergence; remaining divergence only from algorithmic control flow

# instruction_latency(id|operation|cpu_zig_ns|t4_ns|h100_ns|h100_theoretical_ns)
IL1|Q16 add|2|~4|~2|~0.5
IL2|Q16 multiply|4|~8|~3|~1.0
IL3|Q16 MAC fused|5|~8|~3|~1.0
IL4|Q16 divmod (SHR16)|1|~2|~1|~0.5
IL5|Q16 softmax (100 logits)|800|~200|~50|~10
IL6|Q16 dot product (d=64)|400|~100|~25|~8
IL7|Q16 GEMM (128×128)|~500,000|~5,000|~800|~200
IL8|Q335 multiply|200|~400|~80|~20
IL9|Prolog unify (VDR-VDR)|6|~12|~4|~1.5
IL10|Prolog query (200 facts)|4,000|~400|~100|~20
IL11|Grammar render (5 slots)|500|~500|~500|~500
IL12|KB fact read (by id)|50|~20|~8|~4
IL13|Session snapshot (100 KB)|50,000|~50,000|~50,000|~50,000

# memory_bandwidth_utilization(id|workload|access_pattern|utilization|bottleneck)
MW1|GEMM (forward pass)|sequential tile loads 128×128|85-95%|compute-bound at peak
MW2|attention QK^T|batched sequential per head|70-85%|compute for long sequences
MW3|attention softmax|streaming row-wise|40-60%|latency (row reduction)
MW4|KB fact query (single)|random 40-byte read|5-10%|latency-dominated
MW5|KB fact search (scan)|sequential 40-byte reads|50-70%|bandwidth for large KBs
MW6|Prolog unification batch|random KB reads + compute|20-40%|compute (cross-multiply)
# key: forward pass same pattern as conventional LLM (bandwidth); KB/Prolog operations invert to latency-sensitive; VDRProlog scheduling hints enable overlapping both on different SMs

# clone_cow_faults(id|workload|total_pages|dirtied|fault_rate|private_overhead)
CW1|read-only clone|50|0|0%|0 bytes
CW2|standard investigation|200|12|6%|48 KB
CW3|heavy modification|200|35|17.5%|140 KB
CW4|full fork|200|200|100%|800 KB
# most clones dirty <10% of pages; 10 concurrent standard clones share ~94% memory

# command_token_comparison(id|metric|VDRProlog|conventional_json)
TC1|tokens per invocation|~8|~25-40
TC2|entropy per token|~2 bits|~12-15 bits
TC3|vocabulary|~300 known names|50K+ full vocab
TC4|error rate per invocation|~0.8%|~14%
TC5|structural tokens generated|0|~15-25
TC6|result delivery|KB address (0 output tokens)|serialized into context (~50-200 tokens)
TC7|total round-trip|~8 tokens|~75-240 tokens
# 20-turn session with 5 calls/turn: VDRProlog ~800 command tokens vs conventional ~15,000 tool tokens + quadratic context growth

# builtin_vs_llm_speedup(id|operation|builtin_time_h100|equiv_llm_tokens|llm_time_h100|speedup)
BV1|sort 100 integers|~5 μs|200-500|10-25 ms|2,000-5,000×
BV2|parse 1 KB JSON|~2 μs|250+|12.5+ ms|6,000×
BV3|compare two VDR values|~0.01 μs|5-15|0.25-0.75 ms|25,000-75,000×
BV4|KB fact query by ID|~0.01 μs|20-50 (state reconstruction)|1-2.5 ms|100,000-250,000×
BV5|Prolog rule fire|~0.1 μs|50-200 (reasoning chain)|2.5-10 ms|25,000-100,000×
BV6|exact Bayesian update|~0.1 μs|50-200|2.5-10 ms|25,000-100,000×

# protocol_grammar_coverage(id|protocol|grammar_coverage|llm_produced)
PG1|HTTP JSON|71%|body content values
PG2|HTTP HTML|75%|text content
PG3|SMTP|90%|subject, body text
PG4|MQTT PUBLISH|88%|payload values
PG5|DNS response|94%|IP address bytes (4 bytes)
PG6|WebSocket JSON|70%|content values

# energy_per_operation(id|class|float32_pj|q16_vdr_pj|ratio)
EG1|single multiply|~5.0|~1.5|3.3×
EG2|fused multiply-add|~6.5|~2.0|3.3×
EG3|division (SFU vs integer)|~20.0|~3.0|6.7×
EG4|exp (SFU)|~25.0|0 (surrogate)|∞
EG5|softmax per element|~30.0|~4.0|7.5×
EG6|NaN check|~0.5|0|∞
# 7B forward pass: (5.0−1.5)×14×10⁹ pJ = 49 mJ saved per pass; at 100 tok/s = 4.9 W continuous power reduction per GPU

# session_counters(id|counter|type|meaning)
SC1|current_turn|i32|total interaction cycles
SC2|facts_asserted|i32|cumulative facts written
SC3|rules_fired|i64|cumulative rule activations (L2+L3)
SC4|primitive_calls|i64|cumulative builtin invocations
SC5|grammar_renders|i64|cumulative format operations
SC6|llm_tokens_consumed|i64|total LLM forward passes
SC7|command_tokens_consumed|i64|total command generation cost
SC8|l1_count|i64|full-judgment cycles
SC9|l2_count|i64|rule-invoked cycles
SC10|l3_count|i64|fully automated cycles
# derived: auto_triage = l3/(l1+l2+l3); avg_tokens/turn = llm_tokens/current_turn; all as exact fractions; included in snapshots

# error_recovery(id|error|recovery|automated)
ER1|KB_FULL|compact live state (LRU eviction)|yes
ER2|KB_ACCESS_DENIED|log + continue, data absent|yes
ER3|PROLOG_DEPTH_EXCEEDED|simplify query, partial results|yes
ER4|PROLOG_NO_MATCH|fall through to LLM (L1)|yes
ER5|GRAMMAR_TYPE_MISMATCH|report to LLM via scratchpad|yes
ER6|GRANT_DENIED|log + report, no side effect|yes
ER7|GRANT_EXPIRED|request new via admin channel|no
ER8|SNAPSHOT_CORRUPT|hard fail, do not restore, alert|no
ER9|COMMAND_PARSE_ERROR|write to scratchpad, LLM self-corrects|yes
# no entry involves "retry hoping float non-determinism produces different result"

# open_boundaries(id|boundary|description)
OB1|model scale|toy validates at 181 params; scaling to 7B+ requires multi-GPU, KV-cache management, empirical training quality validation
OB2|kernel optimization|Phase 5 = functional correctness baselines, not performance ceilings; cache-aware tiling, warp scheduling, memory coalescing visible only with profiling
OB3|protocol completeness|Phase 4: HTTP + WebSocket; Phase 6: SMTP, MQTT, DNS; grammar-directed architecture validated by HTTP
OB4|active division|dividing by R≠0 projects divisor via scalar projection losing remainder structure; permanent v1 boundary, logged

# sustained_test(id|aspect|description)
ST1|24-hour simulation|simulated SRE workload: 70% known patterns (L3 by hour 2), 20% variants (L2 after first), 10% novel (L1)
ST2|expected outcomes|L3 > 80% after 24 hours; rules grow from seed 15 to 50-80; errors = 0; replay produces byte-identical output

# cross_platform_determinism(id|all_cells_must_be_identical)
XP1|Q16 add, multiply, softmax, forward pass, Prolog query, grammar render, snapshot roundtrip, full cycle (L1/L3), training step: identical across local macOS, local Linux, GCP T4, GCP H100, GCP H100 multi-GPU
XP2|allreduce: identical across ring, tree, butterfly topologies on multi-GPU (integer addition associative)
# any difference is a bug; float systems cannot populate this matrix with "identical"

# relationships(from|rel|to)
PR3|enables|TS1
TS1|defines|CI1
CI1|identical_to_quantized_inference|AP2
CI1|eliminates|EL_1
SM1|eliminates|WD5
SM2|validates|IV1
KG1|enables|KG4
KG3|enables|PG1
PG1|structurally_equivalent_to|parallel_database_join
GR2|eliminates|GR1
SS2|enables|SS4
SS5|guarantees|IV4
SF1|enables|IV6
SF2|enables|IV7
SF3|enforces|SF2
UC1|implements|EL3
UC2|enables|constant_context_size
UC3|dispatches|AP19
RN2|uses|SS4
RN4|uses|SS3
SV1|clones_from|SS2
SV2|enforced_by|SF2
CF2|computes_from|CF1
BP1|baseline_for|BP2
BP2|baseline_for|BP3
BP3|baseline_for|BP4
BP4|baseline_for|BP5
BP5|baseline_for|BP6
IV1|verified_by|SM2
IV8|verified_by|XP1
EL_4|replaced_by|AP13
WD1|eliminated_by|PR3
WD5|eliminated_by|SM1
TC1|cheaper_than|TC7
BV4|demonstrates|KG2

# section_index(section|title|ids)
1|The Problem|PR1-PR3
2|VDR Arithmetic on GPU|TS1-TS3,CI1-CI3,SM1-SM4
3|Knowledge Bases on GPU|KG1-KG4
4|Prolog on GPU|PG1-PG3
5|Grammar-Directed Token Generation|GR1-GR3
6|Sessions, Snapshots, Clones|SS1-SS5,SN1-SN5
7|Structural Safety|SF1-SF4
8|Universal Execution Cycle|UC1-UC4,EL1-EL3
9|Runners|RN1-RN4,RT1-RT4
10|Server Architecture|SV1-SV6
11|Confidence Propagation|CF1-CF3
12|VDRProlog API Surface|AP1-AP20
13|Implementation|BP1-BP6,FS1-FS20
14|Testing|IV1-IV10,ST1-ST2,XP1-XP2
15|GCP Deployment|GC1-GC5
16|Comparison with Conventional Stack|EL_1-EL_14,WD1-WD9
17|Energy and Hardware|EG1-EG6
18|Open Boundaries|OB1-OB4
A|Module Summary|AP1-AP20
B|Build Phase Dependencies|BP1-BP6
C|GCP Resource Estimates|GC1-GC5
D|Invariant Reference|IV1-IV10
E|Conventional Stack Elimination|EL_1-EL_14
F|File Manifest|FS1-FS20
G|Instruction Latency|IL1-IL13
H|Memory Bandwidth|MW1-MW6
I|Warp Divergence|WD1-WD9
J|Command Token Comparison|TC1-TC7
K|Snapshot Sizes|SN1-SN5
L|Clone COW Faults|CW1-CW4
M|Confidence Examples|CF1-CF3
N|Grant Lifecycle|SF3
O|Protocol Grammar Coverage|PG1-PG6
P|Builtin vs LLM Speedup|BV1-BV6
Q|Session Counters|SC1-SC10
R|Audit Volume|SF4
S|Cross-Platform Determinism|XP1-XP2
T|Runner Recycle Timing|RT1-RT4
U|Error Recovery|ER1-ER9
V|API Function Counts|AP1-AP20
W|Energy Per Operation|EG1-EG6
X|Test Count Summary|BP1-BP6

# decode_legend
# VDRProlog: GPU compute layer for VDR-LLM-Prolog; replaces entire float stack with integer operations + KB + Prolog + grammars + sessions + runners + server
# Q16/Q32/Q335: fixed-denominator VDR types at D=2^16/2^32/2^335; denominator is compile-time constant, never stored
# divmod: shift+mask when D is power-of-two; zero logic gates in silicon
# quadratic softmax surrogate: (shifted)²/Σ(shifted)²; sums to D exactly; integer multiply+divide, no SFU
# SFU: Special Function Unit — GPU transcendental hardware, 32 ops/SM/cycle; eliminated by VDR
# FRU: Functional Remainder Unit — per-QIU sequencer for exact transcendental evaluation on dedicated ASIC
# KB: knowledge base — 256-byte struct at integer address; 26 fields; tree with lexical scoping
# COW: copy-on-write — clone shares parent pages until first write triggers page copy
# L1/L2/L3: execution levels — full LLM (50-500 tok) / LLM+rule (~8 tok) / pure Prolog (0 tok)
# universal cycle: Phase 0 (pre-LLM rules) → Phase 1 (context assembly) → Phase 2 (generation+dispatch) → Phase 3 (post-cycle counters)
# runner: autonomous execution loop; poller (timer), processor (persistent connection+recycle), internal (scheduled compute), batch (clone-per-task)
# grant: positive credential with class/target/uses/expiry; default denial; all terminal states permanent
# MAC kernel / Prolog kernel / Primitive kernel: scheduling hints for latency-vs-bandwidth optimization
# TOPS: tera integer ops/sec; TFLOPS: tera float ops/sec
# invariant: property that must hold at all times on all devices; violation = system bug
# rel_types: enables|defines|identical_to_quantized_inference|eliminates|validates|structurally_equivalent_to|guarantees|enforces|implements|dispatches|uses|clones_from|enforced_by|computes_from|baseline_for|verified_by|replaced_by|eliminated_by|cheaper_than|demonstrates
