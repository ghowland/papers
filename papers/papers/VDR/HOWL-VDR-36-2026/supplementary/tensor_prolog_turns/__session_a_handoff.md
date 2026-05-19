```
TENSORPROLOG_HANDOFF_V1|TURNS_19-40|ZIG_0.15.1|NO_FLOAT|ALL_I32_I64

================================================================
SYSTEM_CONTEXT
================================================================

TensorProlog is a GPU compute stack replacing CUDA with exact integer arithmetic using VDR (Value/Denominator/Remainder) triples. Q16 struct: {v:i32, r0:i16, _pad:i16}, D=65536 implicit. Multiply=widening i64 product, divTrunc by D, remainder=mod D. Softmax=quadratic surrogate (shift-square-divide), last element absorbs rounding, sum=D exactly by integer equality. KB=26-field struct padded to 256 bytes. Fact=40 bytes (tag+Q16 value+28-byte provenance). Prolog=cross-multiply comparison. Grammar=typed slot templates. Session=snapshot/clone/kill with COW. Runners=four autonomous loop types. Server=clone-per-connection with integer credential TTL. Safety=integer comparison before data access. Audit=append-only ring. Confidence=exact VDR fractions from knowability spectrum.

All memory is fixed arena, sized at startup, crashes on exceed. No float anywhere. No heap allocation in hot paths. Every data structure bounded at creation. ArrayList.Managed within fixed arena where needed.

Turns 1-18 were written in a prior session. Turns 19-40 written in this session.

================================================================
DEPENDENCY_CHAIN
================================================================

T19 imports: vdr/types, vdr/q16, kb/types, kb/store, kb/fact, llm/model, llm/forward, llm/softmax
T20 imports: T19 deps + llm/attention, llm/kv_cache, engine/command_parse
T21 imports: vdr/types, vdr/q16, kb/types, kb/store (dispatch table + text + arithmetic builtins)
T22 imports: vdr/q16, builtins/dispatch (collections + sets)
T23 imports: T22 deps + kb/store, kb/fact, kb/types (mappings + conversion)
T24 imports: vdr/q16, builtins/dispatch (linalg + stats)
T25 imports: vdr/q16, vdr/types, builtins/dispatch, builtins/conversion, std.time (graph + integer_ops + time)
T26 imports: vdr/types, vdr/q16, kb/types, kb/store, kb/fact, kb/tree, prolog/types, prolog/rule, confidence/propagate
T27 imports: ALL prior turns (SRE scenario + determinism tests)
T28 imports: vdr/types, vdr/q16, kb/types, kb/store, kb/fact, prolog/rule, engine/level_stats, safety/audit, std.Thread
T29 imports: T28 deps + session/lifecycle, session/snapshot, runner/types, runner/pool
T30 imports: vdr/types, vdr/q16, kb/types, kb/store, kb/fact, std.posix, std.net, std.Thread
T31 imports: T30 deps + server/types, server/listener, server/auth, server/rate_limit
T32 imports: T31 deps + server/health, runner/types, session/snapshot
T33 imports: T32 deps + protocol/http, protocol/websocket, grammar/compile, grammar/render
T34 imports: server/types, server/listener, builtins/dispatch, safety/grant, kb/store, kb/fact, std.fs
T35 imports: ALL prior turns (config + CLI + integration test)
T36 imports: vdr/types, vdr/q16, kb/types, kb/store, std.Thread
T37 imports: vdr/types, vdr/q16 (GPU kernels: gemm, softmax, elementwise, normalize, activation)
T38 imports: T37 deps + prolog/types, gpu/kernels/softmax, gpu/kernels/gemm
T39 imports: T38 deps + gpu/kernels/* (profiling + benchmarks + determinism verification)
T40 imports: ALL prior turns (deploy + distributed + chaos tests)

================================================================
TURN_19: LLM attention + KV cache
================================================================
FILES: src/llm/attention.zig, src/llm/kv_cache.zig
LINES: ~1000

attention.zig:
- fn attention(Q_buf, K_buf, V_buf, config:AttentionConfig, output, scores_scratch, weights_scratch) -> void
- AttentionConfig: {n_heads:i32, d_head:i32, seq_len:i32, causal_mask:bool}
- Per head: compute QK^T as dot product per row/col, divTrunc by D, remainder captured
- Causal mask: if col > row, score=zero (integer comparison, exact zero)
- Call Q16.softmax on active portion of each row, zero-fill masked positions
- Weighted sum of V: widening MAC across seq_len, divTrunc by D
- fn verifySoftmaxSum(weights, seq_len, n_heads) -> i32 violations
- Sum each row, compare to D by integer equality, count mismatches

kv_cache.zig:
- KVCache struct: kb_id, n_layers, max_seq_len, n_heads, d_head, store ptr, current_len
- init: creates KB in store with max_facts = n_layers * max_seq_len * n_heads * 2
- slotIndex: computed as layer*max_seq*heads*2 + position*heads*2 + head*2 + kv_offset
- append: stores K and V per head as VlpFact with tag=vector, provenance=vdr_computation
- loadRange: reads facts back by computed slot, distributes across output arrays
- truncate: retracts all facts beyond position across all layers/heads
- currentLength: returns current_len

DESIGN_NOTES: KV cache stored as KB facts means snapshot includes it, clone shares via COW, kill destroys cleanly. The append stores sum of vector components in fact value (lossy summary for fact storage; full vectors would need vector-typed facts in production).

================================================================
TURN_20: LLM generate + sampling
================================================================
FILES: src/llm/generate.zig, src/llm/sampling.zig
LINES: ~800

generate.zig:
- GenerateState: model ptr, kv_cache ptr, sampling_config, position, max_seq_len, logits/probs/hidden bufs, RNG
- fn prefill(state, input_ids): forward each token through model, advance position
- fn generateToken(state) -> i32: softmax on logits, sample, forward new token, advance position
- fn generateCommand(state, store, command_out, tokens_used) -> VlpStatus: constrained generation loop with maskNonCommandTokens (zero everything above index 300), renormalize to sum=D, greedy sample, parse when command end detected
- fn generateProse(state, max_tokens, output_ids) -> i32: unconstrained generation until end-of-turn
- maskNonCommandTokens: sets probs[300..vocab] to zero
- renormalize: scale remaining probs so sum=D, largest element absorbs rounding remainder
- isCommandEnd: token==299, isEndOfTurn: token==0

sampling.zig:
- SamplingConfig: temperature(Q16), top_k(i32), top_p(Q16), greedy(bool)
- RNG: LCG state i64, init from seed, next() returns i32, nextBounded(bound) returns i32
- fn sampleGreedy(probs) -> i32: argmax by integer comparison
- fn sampleTopK(probs, k, rng) -> i32: partial selection sort for top-k, sum top-k probs, random threshold, cumulative scan
- fn sampleTopP(probs, p_threshold, rng) -> i32: full sort descending, accumulate until threshold fraction of total, random within prefix
- fn applyTemperature(logits, temperature, output): divTrunc(logit*D, temperature_v), remainder tracked

================================================================
TURN_21: Builtins dispatch + text + arithmetic
================================================================
FILES: src/builtins/dispatch.zig, src/builtins/text.zig, src/builtins/arithmetic.zig
LINES: ~1200

dispatch.zig:
- BuiltinFn = *const fn(*BuiltinArgs) BuiltinResult
- BuiltinEntry: {id, name_offset, name_length, fn_ptr, pure, input_count, output_type}
- BuiltinArgs: {store ptr, input_facts[8], input_count, target_kb_id, target_slot_id, text_in[4], text_in_count, text_out slice, text_out_len ptr, int_args[4], int_arg_count}
- BuiltinResult: {status, output_fact, output_kb_id, output_slot_id, output_int, output_bool}
- Helper constructors: emptyResult, factResult, intResult, boolResult, errorResult
- BuiltinTable: entries[512] as ?BuiltinEntry, count, name_buf[16384], name_buf_len
- register(id, name, fn_ptr, pure, input_count, output_type): stores entry at index=id
- dispatch(id, args): lookup + validate input_count + call fn_ptr
- lookup(name): linear scan name_buf for match, return id
- registerAllBuiltins: calls registerArithmeticBuiltins + registerTextBuiltins

text.zig: 17 functions
- textReverse, textSplit, textContains, textReplace, textJoin, textTrim
- textUpper, textLower (in-place ASCII case flip)
- textStartsWith, textEndsWith, textIndexOf, textSubstring
- textRepeat, textPadLeft, textPadRight, textCharAt, textLength
- Each has a builtin wrapper (builtinTextReverse etc) that extracts args and calls core fn

arithmetic.zig: 25 functions
- arithAdd/Sub/Mul/Div: delegate to Q16 methods
- arithPow: binary exponentiation with Q16.mul
- arithReciprocal: Q16.div(one, a)
- arithCompare/Equal/Min/Max/Sign/IsZero: Q16 methods
- arithFloor/Ceil/Round: integer division of v by D with rounding logic
- arithNumerator/Denominator/Abs/Negate: direct field access or Q16 methods
- arithClamp/FromInt/ToInt/Lerp/Midpoint/Distance
- Each has builtin wrapper registered at IDs 0-24

REGISTRATION_IDS: arithmetic=0-24, text=100-116

================================================================
TURN_22: Builtins collections + sets
================================================================
FILES: src/builtins/collections.zig, src/builtins/sets.zig
LINES: ~1200

collections.zig: 36 functions
- collSort: in-place merge sort with 4096-element scratch buffer
- collSortBy: selection sort by separate key array
- collFilter: copy elements where mask[i]==true
- collMap: apply UnaryOp enum (negate/abs/square/double/halve)
- collReduce: fold with BinaryOp enum (add/sub/mul/min/max)
- collGroupBy: count occurrences per integer key
- collFrequencies: count occurrences per Q16 value (exact comparison)
- collDistinct: unique values by Q16.eql
- collFlatten/Chunk/Zip/Unzip/Reverse/Rotate
- collTakeFirst/TakeLast/DropFirst/DropLast
- collPartition: split by predicate into true/false arrays
- collInterleave/Enumerate/MinBy/MaxBy
- collScan: prefix scan with BinaryOp (exact integer accumulation)
- collAll/Any/None/Count: boolean predicate evaluation
- collFindFirst/FindLast/FindAll: Q16.eql search
- collBinarySearch: sorted array binary search by Q16.compare
- collMerge: merge two sorted arrays
- collDeduplicate: remove adjacent duplicates from sorted
- collWindow/CartesianProduct

sets.zig: 14 functions (sorted arrays as sets)
- setUnion/Intersection/Difference/SymmetricDiff: two-pointer merge on sorted Q16 arrays
- setIsSubset/IsSuperset/IsDisjoint: two-pointer with early exit
- setContains: binary search
- setAdd: sorted insert maintaining uniqueness
- setRemove: find and shift
- setEqual: length check + elementwise Q16.eql
- setPowerSet: bitmask enumeration (max 20 elements)
- setFromArray: sort + deduplicate

================================================================
TURN_23: Builtins mappings + conversion
================================================================
FILES: src/builtins/mappings.zig, src/builtins/conversion.zig, src/builtins/register_mappings.zig
LINES: ~1200

mappings.zig: 15 functions
- VlpMap: open-addressing hash table with MapEntry{key:i32, value:VlpFact, occupied:bool}
- init(entries slice): marks all unoccupied, capacity=entries.len
- probe: hash(key)%cap, linear probe for match
- probeInsert: hash%cap, linear probe for empty or match
- mapGet/Set/Delete/ContainsKey/Keys/Values/Size
- mapMerge: copy A then B with VlpMergePolicy (ours/theirs/fail_on_conflict)
- mapFilterKeys: keep entries matching key list
- mapFilterValues: keep entries matching bool predicate array
- mapMapValues: multiply all values by Q16 scalar
- mapInvert: swap key↔value.v
- mapClear/Equal/FromArrays
- Builtin wrappers registered at IDs 200-214

conversion.zig: 14 functions
- parseJson: recursive descent parser, writes VlpFact to KB at sequential slots
  - Objects create child KBs with reference facts
  - Arrays create child KBs
  - Strings stored as text facts via store.text.append
  - Numbers parsed to Q16: integer part * D + fractional part * D / frac_denominator
  - Booleans as tag=boolean, null as tag=empty
  - Handles nested structures, escape sequences in strings, exponent notation (skipped)
- parseCsv: line-by-line, field-by-field, tryParseNumber or store as text
- parseXml: tag extraction, content between tags, skips closing/processing/comment tags
- parseYaml: key:value line parser, comment and document separator handling
- toJson: iterate KB facts, render as JSON object with slot IDs as keys
  - factToJson: switch on tag for value/text/boolean/empty/reference(recursive)
- toCsv: iterate KB facts, delimiter-separated, text/value/boolean rendering
- vdrToDecimal: integer part + fractional digits (up to 6)
- toFraction/fromFraction: Q16 ↔ numerator/denominator pair
- vdrToDecimalString: configurable precision
- decimalStringToVdr: delegates to tryParseNumber
- baseConvert: arbitrary base 2-36 output
- timestampToFields: unix timestamp → year/month/day/hour/minute/second via iterative subtraction with leap year handling

register_mappings.zig: registerMappingBuiltins (IDs 200-214), registerConversionBuiltins (IDs 300-311)

REGISTRATION_IDS: mappings=200-214, conversion=300-311

================================================================
TURN_24: Builtins linalg + stats
================================================================
FILES: src/builtins/linalg.zig, src/builtins/stats.zig, src/builtins/register_linalg.zig
LINES: ~1200

linalg.zig: 8 functions
- matVecMul: y = A*x via widening MAC per row, divTrunc by D
- transpose: data movement only
- gaussianElim: solve Ax=b, pivot for zero avoidance, fraction-free elimination (multiply row by pivot instead of dividing), back-substitution with exact division
- inverse: augmented matrix [A|I], Gauss-Jordan with partial pivoting (max abs value), row operations as cross-multiply to avoid division until final step
- determinant: copy matrix, row reduce with sign tracking, product of pivots
- gramSchmidt: exact orthogonalization, dot products as i64 accumulators, projection = dot_vu/dot_uu * u subtracted from v
- eigenvalues: 1x1 trivial, 2x2 via quadratic formula with intSqrt, general case returns diagonal elements as approximation
- svd: compute A^T*A, eigenvalues of that, singular values as sqrt of eigenvalues, U and Vt as identity (stub for general case)
- intSqrt helper: Newton iteration on i64 until convergence

stats.zig: 8+1 functions
- statsMean: exact sum/n with remainder
- statsVariance: exact sum of squared deviations / n
- statsMedian: selection sort then middle element (or average of two middle)
- statsBayes: posterior = prior*likelihood/evidence per hypothesis, renormalize to sum=D exactly (largest absorbs rounding)
- statsNormalize: divide each by sum, sum=D exactly (largest absorbs)
- statsHistogram: exact bin assignment via Q16.compare against bin edges
- statsCorrelation: exact Pearson via exact dot products of deviations, intSqrt for denominator
- statsCovariance: exact sum of dx*dy / n

register_linalg.zig: registerLinalgBuiltins (IDs 400-407), registerStatsBuiltins (IDs 420-427)

================================================================
TURN_25: Builtins graph + integer ops + time
================================================================
FILES: src/builtins/graph.zig, src/builtins/integer_ops.zig, src/builtins/time_ops.zig, src/builtins/register_graph.zig
LINES: ~1200

graph.zig: 13 functions
- Graph struct: nodes[]/edges[] slices with count/capacity, Edge={from,to,weight:Q16}
- addNode/removeNode (also removes incident edges)/addEdge/removeEdge
- nodeIndex: linear scan for node_id
- bfs: queue-based BFS with 1024-element seen/queue arrays
- dfs: stack-based DFS with 1024-element arrays
- shortestPath: Dijkstra with exact Q16 weights, 1024-element dist/prev/visited arrays, path reconstruction via backtracking prev[]
- topologicalSort: Kahn's algorithm with in-degree counting
- connectedComponents: iterative DFS assigning component IDs (undirected: checks both from and to)
- cycleDetect: DFS coloring (WHITE/GRAY/BLACK), GRAY→GRAY = cycle
- pageRankExact: iterative power method with damping=55705/65536 (~0.85), renormalize to sum=D each iteration, convergence by integer equality
- markovSteady: iterative matrix-vector multiply, renormalize to sum=D, converge by integer equality, max 200 iterations

integer_ops.zig: 21 functions
- intAdd/Sub/Mul: wrapping arithmetic (*%)
- intDiv/Mod: divTrunc/mod with zero check
- intAbs/Sign/Min/Max/Clamp
- intPow: binary exponentiation with wrapping mul
- intFactorial: iterative i64 multiply
- intChoose: iterative n*(n-1)*.../(1*2*...)
- bitAnd/Or/Xor/Not: direct operators
- bitShiftLeft/Right: with bounds check on amount
- bitPopcount: @popCount on u32 bitcast
- bitReverse: @bitReverse on u32 bitcast

time_ops.zig: 10 functions
- timestampNow: std.time.milliTimestamp()/1000
- timestampDiff/Add: wrapping subtract/add
- durationSeconds/Minutes/Hours/Days: multiply by period
- durationCompare: integer comparison
- durationFormat: decompose into d/h/m/s, render as "NdNhNmNs"
- timestampFields: delegates to conversion.timestampToFields

register_graph.zig: registerGraphBuiltins (440-452), registerIntegerOpsBuiltins (460-480), registerTimeBuiltins (490-499)

================================================================
TURN_26: Seed layer
================================================================
FILES: src/seed/seed_init.zig, src/seed/oso_rules.zig, src/seed/confidence_table.zig, src/seed/command_vocab.zig, src/seed/hygiene_rules.zig, src/seed/sentence_templates.zig, src/seed/format_grammars.zig, src/seed/builtin_declarations.zig
LINES: ~1000

seed_init.zig:
- SeedIds struct: root, system, oso, confidence, builtins, command_vocab, hygiene, templates, sentences, formats
- seedInit(store) -> SeedIds: creates KB tree then calls all load functions
- KB tree: root → system → {oso, confidence, builtins, command_vocab, hygiene}, root → templates → {sentences, formats}
- Helper fns: assertTextFact, assertValueFact, assertIntFact (each builds VlpFact with seedProvenance)

oso_rules.zig: 15 engineering principles as text facts (P01:EXACT_ARITHMETIC through P15:NEGATIVE_ACCUMULATION)

confidence_table.zig: 11 Q16 values matching knowability spectrum: 65536, 65536, 64225, 62259, 62259, 55705, 52428, 45875, 32768, 19660, 0

command_vocab.zig: ~300 command names across categories:
- 15 command types (KB_ASSERT through SESSION_CLONE)
- 15 KB operations, 7 Prolog operations, 8 grammar operations
- 31 primitive operations (lru/counter/lock/queue/stack/ring/bitset)
- ~170 builtin names (all registered builtins from turns 21-25)
- 8 output operations (kb://, FINDING, SUMMARY, etc)
- 7 scope operations

hygiene_rules.zig: 3 rule definitions as facts:
- stale_rule_detector: threshold 7776000 seconds (90 days)
- failing_rule_detector: min fires 5, min success rate 20%
- orphan_rule_detector: checks grant state revoked

sentence_templates.zig: 12 grammar templates for SRE domain (finding, triage, correlation, status, alert, remediation, summary, coverage, rule_created, rule_pruned, deploy, rollback)

format_grammars.zig: 18 format templates (json_object, json_result, json_error, csv_row, table_*, kv_line, list_item, metric_line, health_json, http_status, http_header, ws_close, smtp_greeting, smtp_ok, mqtt_connack)

builtin_declarations.zig: 36 representative IOSE declarations as facts (id, name, pure flag) stored 3 slots per declaration

================================================================
TURN_27: SRE scenario + determinism tests
================================================================
FILES: src/test_scenarios/sre_scenario.zig, src/test_scenarios/determinism_tests.zig
LINES: ~1000

sre_scenario.zig:
- SreScenarioResult: {kb_tree_ok, facts_asserted_ok, prolog_fire_ok, confidence_ok, grammar_render_ok, l3_resolution_ok, total_tokens_consumed, total_rules_fired, total_facts}
- runSreScenario(store) -> SreScenarioResult:
  1. seedInit to populate base KB tree
  2. Create ops/services/checkout_api/incidents/rules/grammars KBs
  3. Assert 4 Prometheus-sourced facts (error_rate=45%, latency=2500, throughput=120, service name)
  4. Verify read-back matches exactly by Q16.eql
  5. Test confidence: combineAgreeing on two 95/100 sources, verify ≈99.75%
  6. Test confidence chain: 3 links at 95/100 decreases
  7. Create incident KB, assert service/severity/error_rate/cause facts
  8. Compile and render finding grammar template with 4 fills
  9. Test L1/L2/L3 level stats: 3×L3 + 1×L1 = 75% triage, then add 6×L3 = 90%

determinism_tests.zig:
- DeterminismResult: per-category booleans + total_runs + total_mismatches
- runDeterminismTests(store): 100 runs each category, memcmp via std.mem.sliceAsBytes
- Categories tested:
  - Q16 arithmetic: 8 test values, add/mul/div against reference
  - Softmax: 5 elements, verify sum=D every run, byte-identical output
  - Collections: sort 5 elements, compare to reference
  - Sets: union of two 3-element sets, compare result
  - Linalg: 2x2 determinant, compare to reference
  - Stats: mean and variance of 5 elements
  - Graph: shortest path in 3-node graph with exact Q16 weights
  - KB fact roundtrip: assert Q16.fromFraction(355,113), read back 100×
  - Confidence: combineAgreeing and chain, compare to reference

================================================================
TURN_28: Runner types + pool + poller
================================================================
FILES: src/runner/types.zig, src/runner/pool.zig, src/runner/poller.zig, src/runner/runner_manager.zig
LINES: ~1000

types.zig:
- VlpRunnerType enum: poller/processor/internal/batch
- VlpRunnerState enum: stopped/running/err/recycling
- VlpRunnerAction enum: run_cycle/recycle/stop/kill
- VlpRunner struct (72 bytes): id, type, state, session_id, interval_ms, max_turns_before_recycle, max_consecutive_errors, iteration counters, error counters, recycle counters, KB references (notification/log/compact_rules/task_queue/result_queue), max_concurrent_batch
- Config structs: PollerConfig, ProcessorConfig, InternalConfig, BatchConfig
- RunnerStatus: read-only view of runner state
- defaultRunner(): zero-initialized with sensible defaults

pool.zig:
- ThreadPool: threads[32], n_threads, TaskQueue, shutdown_flag (atomic), active_count (atomic)
- TaskQueue: circular buffer of RunnerTask[256] with mutex + atomic count
- init(n_threads): auto-detect CPU count / 2 if 0
- start(pool, runners): spawns worker threads
- workerMain: pop-blocking loop with 10ms sleep on empty, shutdown flag check
- RunnerTable: runners[64] as RunnerSlot{data:VlpRunner, active:bool}, count
- allocate/release/get/getConst

poller.zig:
- pollerIteration(runner, store, output_buf) -> PollerIterationResult: fires Prolog rules on scope KB, reports rules_fired/tokens/level
- pollerLoop(runner, store, running_flag): timer loop calling pollerIteration, error tracking with consecutive threshold, output routing to notification KB
- writeOutputToKB: appends text fact to KB

runner_manager.zig:
- RunnerManager: table + pool
- init/start/createPoller/startRunner/stopRunner/killRunner/recycleRunner/destroyRunner/getStatus/shutdown/activeRunnerCount

================================================================
TURN_29: Runner processor + internal + batch
================================================================
FILES: src/runner/processor.zig, src/runner/internal.zig, src/runner/batch.zig, src/runner/runner_ops.zig, src/runner/sre_deployment.zig
LINES: ~1200

processor.zig:
- ConnectionState: connected, source_type, reconnect_attempts, bytes/items counters
- SourceType enum: prometheus/deploy_api/alert_stream/custom
- processorIteration: try rule-based compaction first (L3), fall through to LLM (L1), write data as text fact to target KB
- processorRecycle: snapshot → kill → clone → restore (snapshot_buf[65536])
- processorReconnect: exponential backoff 1s→60s cap, 10 attempts
- processorLoop: receive data → iterate → recycle at turn threshold

internal.zig:
- ComputeFn = *const fn(*KBStore, i32) VlpStatus
- internalIteration: call configured compute_fn
- internalLoop: timer loop with error tracking
- Default compute stubs: rollingAverage, trendDetection, coverageGap

batch.zig:
- BatchClone: session_id, task VlpFact, completed flag, result_status, output_buf[4096]
- MAX_BATCH_CONCURRENT = 16
- batchPopTask: read slot 0 from queue KB, retract
- batchWriteResult: assert result fact to result KB
- batchProcessTask: process one task in isolated clone (stub: copies task value as result)
- batchIteration: reap completed clones (write results), spawn new clones up to max_concurrent
- batchLoop: iteration loop with adaptive sleep (100ms idle, 10ms active)

runner_ops.zig: convenience wrappers for RunnerManager (createProcessorRunner, createInternalRunner, createBatchRunner, start variants, recycleProcessor)

sre_deployment.zig:
- SreDeploymentConfig: 4 session IDs + intervals + KB references
- SreDeployment: 4 runner IDs (prometheus processor, deploy processor, triage poller, hygiene internal)
- createSreDeployment: creates all 4 runners with appropriate configs
- startSreDeployment/stopSreDeployment: start/stop all 4
- getSreStatus: collect RunnerStatus for all 4

================================================================
TURN_30: Server types + listener + auth
================================================================
FILES: src/server/types.zig, src/server/listener.zig, src/server/auth.zig
LINES: ~1100

types.zig:
- VlpProtocolType enum: http/websocket/smtp/mqtt/raw_tcp
- VlpConnectionState enum: closed/handshake/authenticating/active/draining
- VlpCloseReason enum: normal/idle_timeout/credential_expired/auth_failed/handshake_failed/protocol_error/shutdown/capacity
- MAX_CONNECTIONS = 256
- ServerCredential: user_id, visibility_level, grants[16] as CredentialGrant, n_grants, issued_at, expires_at, valid
- ServerConnection: fd, session_id, credential, state, timestamps, request counters, read_buf/write_buf[8192]
- ServerConfig: port, address, protocol, max_connections, credential_ttl, timeouts, KB references
- ServerMetrics: atomic counters for accepted/rejected/served/active
- Server struct: config, connections[256], atomic n_active/shutdown_flag, metrics, listen_fd, auth_kb_id, store ptr

listener.zig:
- createListenSocket: socket + setsockopt(REUSEADDR) + bind + listen via std.posix
- acceptConnection: std.posix.accept wrapper
- socketRead/socketWrite: std.posix.read/write wrappers returning {n, status}
- closeSocket: std.posix.close
- findFreeSlot: linear scan for closed connection
- acceptLoop: accept → capacity check → slot allocation → increment active
- closeConnection: close socket, mark closed, decrement active

auth.zig:
- authenticate(store, auth_kb_id, token, ttl) -> AuthResult{status, credential}
  - Hash token via FNV-1a (hashCredential)
  - Scan auth KB for matching hash
  - Layout: user_id*4+0=token_hash, +1=visibility, +2=grant_kb_ref, +3=account_status
  - Check status==1 (active)
  - Load grants from referenced grant KB
- credentialCheck: two integer comparisons (valid flag + timestamp)
- credentialRevoke: set valid=false
- registerUser: write 4 facts per user (hash, visibility, grant ref, status)
- suspendUser/reactivateUser: update status slot

================================================================
TURN_31: Server handler + rate limit
================================================================
FILES: src/server/handler.zig, src/server/rate_limit.zig
LINES: ~1200

handler.zig:
- Request/Response structs with fixed buffers (path[512], body[8192], etc)
- HttpMethod enum, ContentType enum
- handleConnection: read → parse → authenticate → handleRequestLoop
- handleRequestLoop: credential check → read request → rate limit check → processRequest → sendResponse → keepalive decision
- processRequest: route by path (/health, /metrics, /kb/*, /query, 404)
- processHealthRequest/processMetricsRequest: grammar-rendered JSON from integer counters
- processKbRequest: resolve path → read KB info → render JSON
- sendResponse: build HTTP/1.1 response (status line + headers + body)
- sendErrorResponse/sendRateLimitResponse
- parseHttpRequest: state machine parsing method/path/version/headers/body
  - Extracts Content-Length, Connection, Content-Type, Authorization headers
  - Case-insensitive header name comparison

rate_limit.zig:
- RateLimitConfig: window_seconds, max_requests, counter_kb_id
- Global config (module-level var)
- checkRateLimit(store, auth_kb_id, user_id) -> RateLimitResult{allowed, remaining, retry_after}
  - Per-user: counter at slot user_id*2, window_start at user_id*2+1
  - New window if elapsed >= window_seconds: reset counter
  - Check counter >= max: return denied with retry_after
  - Increment counter on allow
- createRateLimitKB/resetRateLimit/getRateLimitStatus

================================================================
TURN_32: Server health + reaper + shutdown
================================================================
FILES: src/server/health.zig, src/server/reaper.zig, src/server/shutdown.zig, src/server/server_main.zig
LINES: ~800

health.zig:
- HealthReport: all integer metrics (connections, requests, sessions, facts, rules, L1/L2/L3 counts, runner states[16])
- collectHealth(server) -> HealthReport: read atomic counters
- renderHealthJson: build JSON string from integer values, no LLM involved

reaper.zig:
- ReaperConfig: idle_timeout, max_session_turns, scan_interval_ms
- reaperScan: iterate connections, three integer comparisons per connection:
  1. idle_seconds >= threshold → close with timeout notice
  2. now >= credential.expires_at → close with expired notice
  3. requests_served >= max_session_turns → mark for recycle
- reaperLoop: periodic scan with configurable sleep

shutdown.zig:
- gracefulShutdown(server) -> ShutdownResult{drained, forced, snapshotted}:
  1. Set shutdown_flag
  2. Close listen socket
  3. Mark all active connections as draining, send shutdown notice
  4. Wait with timeout for connections to close
  5. Force-close remaining (snapshot persistent sessions first)

server_main.zig:
- ServerRuntime: server + reaper_config + accept/reaper threads
- init/start (create listen socket, spawn threads)/stop (graceful shutdown, join threads)
- isRunning/getHealth/getMetrics

================================================================
TURN_33: Protocol HTTP + WebSocket + grammars
================================================================
FILES: src/protocol/http.zig, src/protocol/websocket.zig, src/protocol/grammars.zig, src/protocol/protocol_router.zig
LINES: ~1200

http.zig:
- HttpRequest: method, path, version, headers[32], body, content_length, keepalive, auth_token, upgrade_websocket, ws_key
- HttpResponse: status_code, reason, headers[16], body
- parseRequest: full HTTP/1.1 request parser (request line + headers + body)
  - Extracts Upgrade:websocket and Sec-WebSocket-Key for WS upgrade detection
- buildResponse: assemble HTTP/1.1 response bytes
- sendHttpResponse/sendHttpError

websocket.zig:
- WsOpcode enum: continuation/text/binary/close/ping/pong
- WsFrame: fin, opcode, masked, mask_key[4], payload[8192], payload_len
- wsUpgrade: send 101 Switching Protocols with computed accept key
- wsReadFrame: parse 2-byte header, extended length (126→2 bytes, 127→8 bytes), mask key, payload with unmasking
- wsSendText/wsSendClose/wsSendPong: build and send frame (FIN + opcode + length + payload)
- wsSendFrame: generic frame builder supporting 7-bit, 16-bit, 64-bit length encoding
- wsHandleLoop: credential check → read frame → dispatch by opcode (TEXT→process+respond, BINARY→error, PING→PONG, CLOSE→close with 1000)
- Credential expiry sends close frame with code 4001

grammars.zig:
- Grammar slot constants: HTTP_STATUS=0, HTTP_HEADER=1, CONTENT_TYPE=2, JSON_BODY=3, JSON_ERROR=4, WS_CLOSE=5, HEALTH=6, SMTP_GREETING=7, SMTP_OK=8, MQTT_CONNACK=9
- initProtocolGrammars: stores 10 grammar templates as text facts in grammar KB
- renderHttpResponse: build complete HTTP response from components
- renderJsonResult/renderJsonError: structured JSON construction

protocol_router.zig:
- routeConnection: peek protocol, dispatch to HTTP handler or WebSocket upgrade+loop

================================================================
TURN_34: Protocol SMTP/MQTT stubs + ops
================================================================
FILES: src/protocol/smtp.zig, src/protocol/mqtt.zig, src/ops/filesystem.zig, src/ops/network.zig, src/ops/execute.zig, src/ops/compile_check.zig, src/ops/process.zig, src/ops/ops_dispatch.zig
LINES: ~1200

smtp.zig:
- SmtpState enum, SmtpVerb enum (EHLO/HELO/MAIL/RCPT/DATA/QUIT/RSET/NOOP/AUTH)
- sendGreeting/readCommand/sendResponse
- smtpHandleLoop: state machine (greeting→ehlo→mail_from→rcpt_to→data→ehlo)

mqtt.zig:
- MqttPacketType enum, MqttConnect/MqttPublish structs
- readConnect: parse CONNECT packet header + remaining length
- sendConnack: 4-byte fixed packet
- readPublish: parse topic length + topic + payload
- sendPingresp: 2-byte fixed packet
- mqttHandleLoop: read packet type, dispatch (PUBLISH/PINGREQ/DISCONNECT)

filesystem.zig: grant-gated file operations
- fsRead/fsWrite/fsAppend/fsDelete/fsStat: std.fs wrappers
- fsReadToKB: read file → store.text.append → factAssert with script provenance (confidence 62259)

network.zig:
- netFetch: stub returning placeholder JSON
- netFetchToKB: fetch → store.text.append → factAssert with rest_api provenance (confidence 55705)

execute.zig:
- execRun: stub returning placeholder
- execRunToKB: exec → store → factAssert with script provenance

compile_check.zig:
- compileCheck: balanced delimiter checker ({}, (), [])

process.zig:
- ProcessHandle, procStart (stub), procKill, procStatus

ops_dispatch.zig:
- Builtin wrappers for all ops functions
- registerOpsBuiltins: IDs 500-510 (fs_read/write/append/delete/stat, net_fetch, exec_run, compile_check, proc_start/kill/status)
- All registered with pure=false (operational, grant-gated)

================================================================
TURN_35: Config + CLI + build.zig + integration test
================================================================
FILES: src/config/system_config.zig, src/config/cli.zig, src/config/config_file.zig, src/config/integration_test.zig, src/main.zig, build.zig
LINES: ~1100

system_config.zig:
- SystemConfig struct: device, model (layers/d_model/heads/vocab/mlp/qbasis), memory (max_kbs/facts/rules/terms/text/scratch), sessions, runners, safety, seed path, sampling defaults, server (port/connections/ttl/timeouts), rate limiting
- defaults(): sensible production defaults (port 8080, 64 connections, 100K KBs, 10M facts)

cli.zig:
- CliArgs: config + config_file_path + flags (help/version/test/verbose)
- parseCli(argv): iterate args matching --flag patterns with next-arg value parsing
- printHelp/printVersion

config_file.zig:
- parseConfigFile: read file, parse key=value lines, skip comments (#), apply to SystemConfig via applyConfigValue

integration_test.zig:
- IntegrationResult: 13 boolean checks + total_passed
- runIntegrationTest(config): exercises complete stack:
  1. Seed init → verify KB tree created
  2. KB create/child create → verify IDs positive
  3. Fact assert/query roundtrip → verify Q16.eql
  4. Prolog fireAll → verify status ok
  5. Grammar compile → verify validated
  6. Confidence combineAgreeing → verify combined > source
  7. Auth: createAuthKB + registerUser + authenticate → verify credential valid
  8. Rate limit: 5 allowed + 6th denied
  9. Health check → verify zero counters
  10. Runner creation → verify non-null ID
  11. SRE scenario → verify all sub-checks
  12. Determinism tests → verify zero mismatches
  13. Builtin dispatch → verify table populated

main.zig: entry point, parse CLI, load config file, run tests or print config

build.zig: (commented template) exe + run step + per-phase test steps

================================================================
TURN_36: GPU device + memory + transfer
================================================================
FILES: src/gpu/device.zig, src/gpu/memory.zig, src/gpu/transfer.zig
LINES: ~1000

device.zig:
- DeviceType enum: cpu_fallback/gpu_int8/gpu_int8_fru/gpu_native_qiu
- DeviceProps: all integer fields (compute_units, max_q_basis, has_fru, cache/memory sizes, clock, warp_size, name)
- Global DeviceState: initialized flag, device_count, current_device, props[8]
- deviceInit: creates single CPU fallback device
- deviceGetCount/GetProps/SetCurrent/GetCurrent/Synchronize/Reset
- getErrorString: switch on VlpStatus returning static string

memory.zig:
- DeviceMemoryLayout: 13 regions (model_weights, kb_store, fact_store, rule_store, term_store, text_store, grammar_store, live_state, scratch, audit, grant_store, session_table, path_index) each with base+size, plus capacities and total_bytes
- MemoryConfig: sizing parameters for all regions
- computeLayout: sequential region placement with 256-byte alignment
- DeviceAllocation: host_buf slice + layout + allocated flag (CPU fallback uses host memory)
- allocateDevice/freeDevice/getRegion/getRegionConst

transfer.zig:
- hostToDevice/deviceToHost/deviceToDevice: memcpy within host_buf (CPU fallback)
- transferQ16Array/transferQ16ArrayBack: typed Q16 slice transfer via sliceAsBytes
- mirrorKBStore: copy KB structs + facts + text from KBStore to device allocation
- deviceFactWrite/deviceFactRead: computed offset access (kb_id * facts_per_kb * 40 + slot_id * 40)
- memorySummary: compute MB values for each region

================================================================
TURN_37: GPU MAC + softmax + elementwise kernels
================================================================
FILES: src/gpu/kernels/gemm.zig, src/gpu/kernels/softmax.zig, src/gpu/kernels/elementwise.zig, src/gpu/kernels/normalize.zig, src/gpu/kernels/activation.zig
LINES: ~1200

gemm.zig:
- GemmConfig: m/n/k, trans_a/trans_b, alpha_v/beta_v
- q16Gemm: C = alpha*op(A)*op(B) + beta*C, widening i64 MAC, scaled by alpha/D²
- q16GemmBatched: loop over batch calling q16Gemm
- q16GemmStridedBatched: stride-based offset variant
- q16MatVecMul: y = A*x specialized path

softmax.zig:
- q16Softmax: shift-square-divide surrogate, last element absorbs to guarantee sum=D
- q16SoftmaxBatched: per-row softmax over batch
- verifySoftmaxSum: count rows where sum != D

elementwise.zig:
- q16Add/Sub/Mul/Div/Scale/Dot/Compare: delegate to Q16 methods over arrays
- q16Negate/Abs/Min/Max/Clamp/Fill/Copy/Sum
- q16RemainderMagnitude: abs(r0) per element

normalize.zig:
- q16LayerNorm: exact mean + variance, intSqrt for inv_std, gamma*normalized+beta
- q16RMSNorm: exact mean of squares, intSqrt for inv_rms, gamma*normalized

activation.zig:
- q16ReLU: max(0, x) by integer comparison
- q16GELU: linear sigmoid approximation × input
- q16SiLU: sigmoid approximation × input

================================================================
TURN_38: GPU attention + sort + prolog kernels
================================================================
FILES: src/gpu/kernels/attention.zig, src/gpu/kernels/sort.zig, src/gpu/kernels/prolog_kernel.zig, src/gpu/kernels/reduction.zig
LINES: ~1200

attention.zig:
- AttentionKernelConfig: n_heads, d_head, seq_len, causal_mask, softmax_type
- fusedAttentionForward: per-head QK^T → softmax → AV with 4096-element scratch
- verifySoftmaxSumAllHeads: check all rows across all heads
- fusedAttentionWithKVCache: single query position against cached K/V

sort.zig:
- q16Sort: merge sort with 4096-element scratch
- q16ArgSort: selection sort returning index array (descending)
- q16TopK: partial selection sort for top-k values and indices

prolog_kernel.zig:
- batchUnify: unify query against N candidate terms, return matched[] bitmap
- unifyTerms: structural comparison (atom by id, integer by value, VDR by i64 equality, compound by functor+arity, variable matches anything)
- batchCrossMultiplyCompare: N×M match matrix of Q16 values
- scopeFilter: evaluate visibility for all KBs given session credentials, walk parent chain checking ancestor visibility
- parallelRuleEval: N rules × M facts fire matrix via unifyTerms

reduction.zig:
- q16ReduceSum/Max/Min/ArgMax/ArgMin
- i32ReduceSum
- allReduceSum/allReduceMax: stubs for distributed (single-rank passthrough)

================================================================
TURN_39: GPU profiling + benchmarks + determinism
================================================================
FILES: src/gpu/profiling.zig, src/gpu/benchmarks.zig, src/gpu/determinism.zig
LINES: ~800

profiling.zig:
- KernelStats: kernel_id, elapsed_ns, integer_ops, memory bytes, warp_occupancy (always 100), kb_cache hits/misses, remainder_overflows
- SessionStats: all operational counters + L1/L2/L3 + auto_triage fraction
- Profiler: start/stop, recordKernel, getKernelStats, totalElapsedNs

benchmarks.zig:
- BenchResult: name, total_ns, per_iter_ns, n_iters, ops_per_second
- benchForwardPass/Softmax/Attention/Sort/LayerNorm/PrologUnify/Elementwise/Gemm
- Each: prepare deterministic input, run N iterations, measure nanoTimestamp delta
- runAllBenchmarks: returns [8]BenchResult with default parameters

determinism.zig:
- DeterminismVerifyResult: kernel_name, n_runs, all_identical, first_mismatch_run/byte
- verifyDeterminismSoftmax: run N times, byte-compare via sliceAsBytes
- verifyDeterminismGemm: same pattern
- verifyDeterminismAttention: same pattern
- runFullDeterminismSuite: returns [3]DeterminismVerifyResult
- KEY INVARIANT: all_identical must be true for every kernel. If false on CPU, it's a bug (not drift — integers don't drift)

================================================================
TURN_40: Deploy + distributed + chaos tests
================================================================
FILES: src/deploy/distributed.zig, src/deploy/model_parallel.zig, src/deploy/load_balancer.zig, src/deploy/prometheus_export.zig, src/deploy/chaos.zig, src/deploy/deploy_main.zig
LINES: ~1200

distributed.zig:
- Comm: rank, size, initialized
- allReduceSum/Max/Min: single-rank passthrough (multi-rank requires network layer)
- broadcast/allGather/reduceScatter: single-rank passthrough
- kbSync: copy local to synced (single-rank)
- snapshotBroadcast: copy data (single-rank)
- KEY PROPERTY: integer sum is associative, so allReduceSum produces identical results regardless of reduction topology

model_parallel.zig:
- ModelParallelConfig: n_devices, n_layers, d_model, n_heads, d_head, vocab_size
- DeviceShard: device_id, layer_start/end, n_layers
- ModelParallel: config + shards[8] + hidden/inter buffers[4096]
- init: divide layers evenly across devices, last device gets remainder
- pipelineForward: copy through shards sequentially (stub: passthrough per layer)
- getShardInfo: lookup shard by device_id

load_balancer.zig:
- MAX_BACKENDS = 16
- Backend: id, address, port, healthy, active_connections, total_requests
- LoadBalancer: backends[16], strategy (round_robin/least_connections)
- addBackend/route/releaseBackend/markUnhealthy/markHealthy/removeUnhealthy
- round_robin: skip unhealthy, wrap index
- least_connections: pick healthy backend with min active

prometheus_export.zig:
- exportPrometheus(server, output) -> i32: render all metrics as "metric_name value\n" format

chaos.zig:
- ChaosTestResult: 4 checks + totals
- testSnapshotRecovery: assert → snapshot → corrupt → restore → verify original
- testKillRestart: assert 10 facts → snapshot → restore to new KB → verify all 10 match
- testConcurrentWrite: write 100 sequential facts → read all back → verify exact values
- testDeterminismAfterRestart: run full determinism suite (100 iterations), all must pass

deploy_main.zig:
- DeploymentResult: 6 booleans (integration/chaos/benchmarks/determinism/server/runners)
- deployAndVerify: run integration test → chaos tests → benchmarks → determinism suite
- printDeployResult: formatted output

================================================================
KNOWN_ISSUES_AND_STUBS
================================================================

1. KV cache in T19 stores vector sums as single facts (lossy). Production needs vector-typed facts or dedicated vector store.
2. Builtin wrappers in T23 mappings (builtinMapGet etc) are stubs returning emptyResult — need KB-backed VlpMap integration.
3. eigenvalues in T24 returns diagonal for n>2 (approximation). Full QR iteration needed.
4. SVD in T24 returns identity U/Vt (stub). Full Golub-Kahan needed.
5. netFetch in T34 is a stub. Real HTTP client needs std.http.Client or raw socket.
6. execRun in T34 is a stub. Real subprocess needs std.process.Child.
7. processorRecycle in T29 uses session_id+1000 for new ID (placeholder). Real implementation needs session manager allocation.
8. WebSocket accept key in T33 uses simple hash (placeholder). Real implementation needs SHA-1 + base64.
9. Distributed operations in T40 are single-rank passthroughs. Multi-rank needs TCP/RDMA transport.
10. Model parallel forward in T40 is passthrough. Real pipeline needs cross-device hidden state transfer.
11. GELU/SiLU activations in T37 use linear approximations. FRU-based exact versions would replace these.
12. build.zig in T35 is commented template — needs uncommenting and path adjustment for actual build.

================================================================
BUILTIN_REGISTRATION_MAP
================================================================

IDs 0-24: arithmetic (T21)
IDs 100-116: text (T21)
IDs 200-214: mappings (T23)
IDs 300-311: conversion (T23)
IDs 400-407: linalg (T24)
IDs 420-427: stats (T24)
IDs 440-452: graph (T25)
IDs 460-480: integer_ops (T25)
IDs 490-499: time (T25)
IDs 500-510: ops (T34)

Total registered: ~180 (of 448 spec target — remaining are categories not yet covered: collections/sets builtins need dispatch registration, polynomial, finite field, denominator management, identity, logic)

================================================================
FILE_TREE
================================================================

src/
  vdr/           T1-T2  (types, q16, q32, q335, reproject)
  kb/            T3-T5  (types, store, fact, tree, path_index, text_store, visibility)
  safety/        T5-T6  (grant, audit)
  confidence/    T6     (propagate)
  prolog/        T7-T9  (types, term, unify, query, rule, hygiene)
  grammar/       T9-T10 (compile, render, validate, inherit)
  primitives/    T11-T12 (lru, counter, lock, queue, stack, ring, bitset)
  session/       T13-T14 (lifecycle, cow, snapshot)
  engine/        T15-T17 (context, scratchpad, token_classify, level_stats, command_parse, command_exec, cycle)
  llm/           T18-T20 (model, forward, softmax, attention, kv_cache, generate, sampling)
  builtins/      T21-T25 (dispatch, text, arithmetic, collections, sets, mappings, conversion, linalg, stats, graph, integer_ops, time_ops, register_*)
  seed/          T26    (seed_init, oso_rules, confidence_table, command_vocab, hygiene_rules, sentence_templates, format_grammars, builtin_declarations)
  test_scenarios/ T27   (sre_scenario, determinism_tests)
  runner/        T28-T29 (types, pool, poller, processor, internal, batch, runner_manager, runner_ops, sre_deployment)
  server/        T30-T32 (types, listener, auth, handler, rate_limit, health, reaper, shutdown, server_main)
  protocol/      T33-T34 (http, websocket, grammars, protocol_router, smtp, mqtt)
  ops/           T34    (filesystem, network, execute, compile_check, process, ops_dispatch)
  config/        T35    (system_config, cli, config_file, integration_test)
  gpu/           T36-T39 (device, memory, transfer, profiling, benchmarks, determinism, kernels/{gemm, softmax, elementwise, normalize, activation, attention, sort, prolog_kernel, reduction})
  deploy/        T40    (distributed, model_parallel, load_balancer, prometheus_export, chaos, deploy_main)
  main.zig       T35

================================================================
INVARIANTS_VERIFIED_ACROSS_TURNS
================================================================

INV1: Softmax sum=D → T19 (verifySoftmaxSum), T27 (determinism), T37 (verifySoftmaxSum), T38 (verifySoftmaxSumAllHeads), T39 (verifyDeterminismSoftmax)
INV2: KB facts exact → T27 (kb_fact_roundtrip 100×), T40 (chaos snapshot recovery)
INV3: Bounded primitives → T28 (runner table MAX_RUNNERS=64), T29 (batch MAX_CONCURRENT=16)
INV4: Snapshot bit-identical → T40 (testSnapshotRecovery: assert→snapshot→corrupt→restore→verify)
INV8: Determinism across runs → T27 (100 runs per category), T39 (100 runs softmax/gemm/attention)
INV9: Prolog exact comparison → T38 (batchUnify, batchCrossMultiplyCompare)
INV10: Audit append-only → T28 (poller writes audit), T30 (auth writes audit)
```
