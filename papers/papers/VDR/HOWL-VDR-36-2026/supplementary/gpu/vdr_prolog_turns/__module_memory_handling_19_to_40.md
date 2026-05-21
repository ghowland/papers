Every module I wrote falls into one of four memory patterns. Here's the complete catalog.

**Pattern 1: Pure stack operations — no allocation at all**

These modules declare fixed-size arrays on the stack or operate entirely on passed-in slices. No allocation call of any kind.

`src/llm/attention.zig` — All buffers (Q/K/V/output/scores_scratch/weights_scratch) are passed in by caller as slices. The function reads and writes through them. No local allocation.

`src/llm/sampling.zig` — SamplingConfig and RNG are value types on stack. **VIOLATION**: sampleTopK and sampleTopP declare `var indices: [65536]i32` on stack — that's 256KB per call. sampleGreedy and applyTemperature are clean.

`src/llm/generate.zig` — GenerateState holds pointers to externally-owned buffers (model, kv_cache, logits_buf, probs_buf, hidden_buf). **VIOLATION**: generateToken declares `var temp_buf: [65536]Q16` on stack — 512KB. generateCommand declares `var cmd_tokens: [32]i32` on stack — 128 bytes, acceptable.

`src/builtins/arithmetic.zig` — All functions take Q16 values and return Q16 values. Pure register/stack arithmetic. Zero allocation.

`src/builtins/integer_ops.zig` — Same. Pure i32 arithmetic. intFactorial uses i64 accumulator on stack.

`src/builtins/text.zig` — Core functions (textReverse, textContains, etc.) operate on passed-in byte slices. Builtin wrappers use BuiltinArgs fields (text_in/text_out) which are caller-owned. No allocation.

`src/builtins/sets.zig` — All functions take sorted Q16 slices passed by caller. setFromArray uses `var scratch: [4096]Q16` on stack — 32KB, within reason for sort scratch. setPowerSet iterates bitmasks without allocation.

`src/builtins/collections.zig` — All functions take slices from caller. collSort uses `var scratch: [4096]Q16` on stack — 32KB for merge sort scratch. All other functions operate on passed-in slices.

`src/builtins/linalg.zig` — matVecMul, transpose, gramSchmidt take passed-in slices. **VIOLATION**: inverse declares `var aug: [4096]Q16` on stack — 32KB. determinant declares `var work: [4096]Q16` on stack — 32KB. eigenvalues (2x2 case) uses stack scalars. svd declares `var AtA: [4096]Q16` plus `var eig_r/eig_i: [64]Q16` on stack.

`src/builtins/stats.zig` — Core functions take slices. statsMedian sorts in-place (caller's array). statsBayes uses passed-in arrays. **VIOLATION**: builtinMean/Variance/Median declare `var data: [256]Q16` on stack — 2KB each, copies from input_facts. This limits stats through dispatch to 256 elements.

`src/builtins/graph.zig` — Graph struct holds slices passed at init (node_buf, edge_buf). Graph doesn't own the memory. **VIOLATION**: bfs, dfs, shortestPath, topologicalSort, connectedComponents, cycleDetect, pageRankExact all declare `[1024]` stack arrays — 4-8KB each. markovSteady declares `var next: [256]Q16` — 2KB.

`src/builtins/time_ops.zig` — Pure i32 arithmetic. durationFormat uses `var buf: [32]u8` on stack.

`src/builtins/time.zig` (extras) — Same. formatTimestamp uses `var digits: [10]u8` on stack. parseTimestamp uses stack scalars only.

`src/ops/compile_check.zig` — Pure stack. Iterates source bytes tracking three i32 depth counters.

`src/ops/compile_op.zig` (extras) — Same pattern plus CompileResult with `error_msg: [256]u8` on stack.

`src/ops/process.zig` — ProcessHandle is a 8-byte value struct. No allocation.

**Pattern 2: Caller provides backing memory via slices**

These modules receive all their storage from the caller. They never allocate. The arena sizing guarantee comes from the caller sizing these slices at startup.

`src/builtins/dispatch.zig` — BuiltinTable has `entries: [512]?BuiltinEntry` and `name_buf: [16384]u8` as inline fixed arrays within the struct. When the caller creates a BuiltinTable (typically on the stack or as a field of a larger struct), these arrays are part of it. register() writes into entries[] and name_buf[] at sequential positions. No allocation call.

`src/builtins/mappings.zig` — VlpMap.init() takes a `[]MapEntry` slice from caller. The map operates within that slice. Capacity = slice.len, fixed forever. mapSet returns err_kb_full if the hash table is full. The caller sizes the backing slice at init.

`src/builtins/conversion.zig` — parseJson/parseCsv/parseXml/parseYaml take a `*KBStore` and write into it via factAssert. The KBStore's fact array is pre-allocated by the KBStore's caller. The text store (for string values) is append-only into a pre-allocated byte slice. toJson/toCsv write into caller-provided output slices. toFraction/fromFraction are pure stack.

`src/llm/kv_cache.zig` — KVCache.init() calls store.createKB() which allocates a KB slot and fact slots from the KBStore's pre-allocated arrays. The KVCache doesn't allocate — it uses the store's existing capacity. append/loadRange/truncate use factAssert/factQuery/factRetract which are O(1) index operations into the pre-allocated fact array.

`src/engine/scratchpad.zig` (extras) — Scratchpad.init() takes a `[]u8` backing slice from caller. All writes append into that slice. When full, writes are silently truncated. clear() resets len to 0.

`src/primitives/*` (turns 11-12, prior session) — LRU, Counter, Lock, Queue, Stack, Ring, Bitset all take backing slices or fixed capacity at init. They never grow.

**Pattern 3: Write into KBStore (the system's arena)**

These modules create KBs and assert facts into the KBStore, which is the system's central pre-allocated arena. The KBStore's backing arrays (kbs[], facts[], text data[]) are sized at startup and never grow.

`src/seed/seed_init.zig` — Calls store.createKB() 10 times (root, system, oso, confidence, builtins, command_vocab, hygiene, templates, sentences, formats). Each createKB() claims the next slot in the KBStore's pre-allocated kb array and a chunk of the fact array. assertTextFact/assertValueFact/assertIntFact call store.text.append() (appends into pre-allocated text byte array) and fact_mod.factAssert() (writes into pre-allocated fact array at computed offset).

`src/seed/oso_rules.zig` — 15 calls to assertTextFact. Each appends text into store.text and writes a fact.

`src/seed/confidence_table.zig` — 11 calls to assertValueFact. Writes Q16 values as facts.

`src/seed/command_vocab.zig` — ~300 calls to assertTextFact. Heaviest seed module in text store usage.

`src/seed/hygiene_rules.zig` — 12 fact assertions.

`src/seed/sentence_templates.zig` — 12 fact assertions with template strings.

`src/seed/format_grammars.zig` (extras) — 24 calls to storeTemplate. Each appends template text and asserts a fact.

`src/seed/builtin_declarations.zig` — 36×3 = 108 fact assertions.

`src/builtins/register_mappings.zig` — Calls table.register() which writes into the BuiltinTable's inline arrays. No KBStore interaction.

`src/builtins/register_linalg.zig` — Same.

`src/builtins/register_graph.zig` — Same.

`src/test_scenarios/sre_scenario.zig` — Creates 6 KBs and asserts ~20 facts via the KBStore. Compiles a grammar (grammar_compile.compile writes into a stack-local VlpGrammar struct). All memory comes from the passed-in KBStore.

`src/test_scenarios/determinism_tests.zig` — Creates 1 KB, asserts 1 fact. All data arrays for testing are stack-local with fixed sizes ([16], [5], [6], [8] Q16 arrays). The reference arrays and run arrays are stack-local.

`src/server/auth.zig` — createAuthKB calls store.createKB(). registerUser writes 4 facts per user. authenticate reads facts. All through KBStore.

`src/server/rate_limit.zig` — createRateLimitKB calls store.createKB(). checkRateLimit reads/writes counter facts. All through KBStore.

`src/protocol/grammars.zig` — initProtocolGrammars stores 10 template strings as text facts in KBStore.

**Pattern 4: Struct with inline fixed arrays**

These modules define structs containing fixed-size arrays. The struct is allocated by the caller (on stack, as a field, or in a pre-allocated array). The fixed arrays are part of the struct's memory footprint.

`src/runner/types.zig` — VlpRunner is 72 bytes of scalar fields. No arrays. defaultRunner() returns a value.

`src/runner/pool.zig` — ThreadPool has `threads: [32]std.Thread` (inline), TaskQueue has `buf: [256]RunnerTask` (inline), RunnerTable has `runners: [64]RunnerSlot` (inline). When the caller creates a ThreadPool or RunnerTable, these arrays are part of the struct. TaskQueue uses std.Thread.Mutex (contains OS-level synchronization primitive, allocated inline). ThreadPool.start() calls std.Thread.spawn() — this is the one place where OS resources are created (thread stacks allocated by the OS, not by our code).

`src/runner/poller.zig` — pollerLoop declares `var output_buf: [4096]u8` on stack — 4KB per poller loop iteration.

`src/runner/processor.zig` — processorLoop declares `var ingest_buf: [8192]u8` on stack — 8KB. processorRecycle declares `var snap_buf: [65536]u8` on stack — 64KB for snapshot. ConnectionState is a small value struct.

`src/runner/internal.zig` — No local arrays. Pure function calls.

`src/runner/batch.zig` — batchLoop declares `var clones: [16]BatchClone` on stack. BatchClone contains `output_buf: [4096]u8`, so that's 16 × ~4KB = 64KB on stack.

`src/runner/runner_manager.zig` — RunnerManager holds RunnerTable and ThreadPool as fields. When the caller creates a RunnerManager, it includes the full RunnerTable (64 × RunnerSlot) and ThreadPool (32 × Thread handle + 256-entry task queue).

`src/runner/sre_deployment.zig` — SreDeployment is 4 × i32 = 16 bytes. SreDeploymentConfig is scalar fields. No arrays.

`src/server/types.zig` — Server has `connections: [256]ServerConnection` inline. Each ServerConnection has `read_buf: [8192]u8` and `write_buf: [8192]u8`. Total: 256 × ~16KB = ~4MB inline in the Server struct. The caller must ensure this is not on a small stack. ServerCredential has `grants: [16]CredentialGrant` inline.

`src/server/listener.zig` — acceptLoop operates on the Server's connections array. No local allocation beyond small stack variables.

`src/server/handler.zig` — handleRequestLoop creates Request and Response structs on stack. Request has `path: [512]u8`, `body: [8192]u8`, `auth_token: [256]u8` — ~9KB. Response has `body: [8192]u8`, `buf: [16384]u8` — ~24KB. Total per-connection handler: ~33KB on stack.

`src/server/health.zig` — HealthReport has `runner_states: [16]RunnerHealth` — ~1KB inline. renderHealthJson writes into caller-provided output slice.

`src/server/reaper.zig` — No allocation. Reads server.connections[] and timestamps.

`src/server/shutdown.zig` — gracefulShutdown declares `var snap_buf: [65536]u8` on stack for session snapshots — 64KB.

`src/server/server_main.zig` — ServerRuntime holds Server as a field (including the 4MB connections array). std.Thread.spawn() for accept and reaper threads.

`src/protocol/http.zig` — HttpRequest has `headers: [32]HttpHeader` where each has `name: [64]u8` + `value: [256]u8` — 32 × 320 = ~10KB. Plus `path: [512]u8`, `body: [8192]u8`, `auth_token: [256]u8`, `host: [128]u8`, `ws_key: [64]u8`. Total HttpRequest: ~19KB on stack when created. HttpResponse has `body: [8192]u8` — ~8KB.

`src/protocol/websocket.zig` — WsFrame has `payload: [8192]u8` — 8KB on stack per frame read. wsUpgrade uses `var resp_buf: [512]u8` and `var combined: [128]u8` on stack.

`src/protocol/smtp.zig` — smtpHandleLoop declares `var line: [512]u8`, `var data_buf: [8192]u8` on stack.

`src/protocol/mqtt.zig` — readConnect declares `var body: [512]u8`. readPublish declares `var body: [4096]u8`. mqttHandleLoop declares `var discard: [256]u8`.

`src/ops/filesystem.zig` — fsReadToKB declares `var buf: [65536]u8` on stack — 64KB. Writes into KBStore via text.append() and factAssert().

`src/ops/network.zig` — netFetchToKB declares `var buf: [65536]u8` on stack — 64KB. Same pattern.

`src/ops/execute.zig` — execRunToKB declares `var buf: [65536]u8` on stack — 64KB. Same pattern.

`src/ops/ops_dispatch.zig` — Builtin wrappers use BuiltinArgs fields. builtinExecRun declares `const empty_args = [_][]const u8{}` — zero size.

`src/config/system_config.zig` — SystemConfig has `model_checkpoint_path: [256]u8` and `seed_snapshot_path: [256]u8` inline. ~700 bytes total.

`src/config/cli.zig` — CliArgs embeds SystemConfig plus `config_file_path: [256]u8`. ~1KB total.

`src/config/config_file.zig` — parseConfigFile declares `var buf: [8192]u8` on stack for file read.

`src/config/integration_test.zig` — **MAJOR VIOLATION**: declares `var kb_buf: [4096]VlpKB` (4096 × 256 = 1MB), `var fact_buf: [65536]VlpFact` (65536 × 40 = 2.5MB), `var text_buf: [262144]u8` (256KB), `var path_entries: [8192]PathEntry` (~64KB). Total: ~3.8MB on stack. This will stack overflow on most platforms.

`src/main.zig` — Declares `var arg_slices: [64][]const u8` on stack — small.

`src/gpu/device.zig` — **VIOLATION**: `var global_device_state` is a module-level mutable variable — global state. DeviceProps has `name: [64]u8` inline.

`src/gpu/memory.zig` — DeviceMemoryLayout is pure scalar fields (~200 bytes). DeviceAllocation holds a `[]u8` slice provided by caller. computeLayout is pure computation returning a value struct.

`src/gpu/transfer.zig` — All functions operate on DeviceAllocation's host_buf slice. No local allocation.

`src/gpu/kb_device.zig` (extras) — DeviceKBStore holds a pointer to DeviceAllocation. All reads/writes go through the allocation's host_buf slice.

`src/gpu/profiling.zig` — Profiler has `kernel_stats: [64]KernelStats` inline — ~4KB.

`src/gpu/benchmarks.zig` — Each bench function declares `[4096]Q16` arrays on stack — 32KB each. benchmarks that run sequentially so only one is active at a time.

`src/gpu/determinism.zig` — Each verify function declares two `[4096]Q16` arrays — 64KB total. Plus input arrays.

`src/gpu/kernels/gemm.zig` — All buffers passed by caller. No local allocation.

`src/gpu/kernels/softmax.zig` — **VIOLATION**: q16Softmax declares `var shifted: [4096]i64` — 32KB on stack.

`src/gpu/kernels/elementwise.zig` — All buffers passed by caller. No local allocation.

`src/gpu/kernels/normalize.zig` — No local arrays. Scalar accumulators only.

`src/gpu/kernels/activation.zig` — No local arrays. Per-element computation.

`src/gpu/kernels/attention.zig` — **VIOLATION**: declares `var scores_buf: [4096]Q16` and `var weights_buf: [4096]Q16` — 64KB on stack.

`src/gpu/kernels/sort.zig` — mergeQ16 declares `var scratch: [4096]Q16` — 32KB. q16ArgSort declares `var indices: [4096]i32` — 16KB. q16TopK declares `var indices: [4096]i32` — 16KB.

`src/gpu/kernels/prolog_kernel.zig` — UnifyBatchResult has `matched: [256]bool` inline. scopeFilter's ScopeFilterResult has `visible: [1024]bool` inline — 1KB.

`src/gpu/kernels/reduction.zig` — No local arrays. Scalar accumulators.

`src/deploy/distributed.zig` — All functions take slices from caller. No local allocation.

`src/deploy/model_parallel.zig` — ModelParallel has `shards: [8]DeviceShard` and `hidden_buf/inter_buf: [4096]Q16` — 64KB inline.

`src/deploy/multi_device.zig` (extras) — MultiDevice has `shards: [8]DeviceShard` and `hidden_transfer_buf: [8192]Q16` — 64KB inline.

`src/deploy/load_balancer.zig` — LoadBalancer has `backends: [16]Backend` where each Backend has `address: [64]u8` — ~2KB total.

`src/deploy/prometheus_export.zig` — Writes into caller-provided output slice.

`src/deploy/monitoring.zig` (extras) — MonitoringConfig has `prometheus_prefix: [32]u8`. exportPrometheus writes into caller-provided output slice.

`src/deploy/chaos.zig` — testSnapshotRecovery and testKillRestart declare `var snap_buf: [65536]u8` — 64KB each on stack.

`src/deploy/deploy_main.zig` — deployAndVerify calls other test functions. No direct allocation.

`src/deploy/gcp_setup.zig` (extras) — GcpInstanceConfig has fixed-size string fields totaling ~350 bytes. Command builders write into caller-provided output slices.

**Summary of arena rule violations requiring repair:**

1. `integration_test.zig` — 3.8MB on stack. Move to static/heap allocation.
2. `generate.zig` temp_buf — 512KB on stack. Move to GenerateState field.
3. `sampling.zig` indices — 256KB on stack. Pass as parameter.
4. `gpu/kernels/attention.zig` scores/weights — 64KB on stack. Pass as parameter.
5. `gpu/kernels/softmax.zig` shifted — 32KB on stack. Pass as parameter.
6. `filesystem.zig`/`network.zig`/`execute.zig` — 64KB each on stack for read buffers. Pass as parameter or use scratch region from DeviceAllocation.
7. `shutdown.zig`/`processor.zig`/`chaos.zig` snap_buf — 64KB on stack. Use pre-allocated snapshot buffer.
8. `handler.zig` Request+Response — 33KB on stack. Acceptable per-connection but large.
9. `http.zig` HttpRequest — 19KB on stack. Acceptable but large.
10. `device.zig` and `rate_limit.zig` — global mutable state. Pass as parameters.
