```
VDRProlog_AS_BUILT_AUDIT_V1|TURNS_19-40_PLUS_EXTRAS|ZIG_0.15.1

================================================================
PURPOSE
================================================================

This document catalogs every module written in this session, compares
each against the original turn plan spec, identifies deviations, and
provides the dependency map needed to repair them. The original spec
is authoritative. Where the implementation diverged, the spec wins.

================================================================
DIRECTORY: src/llm/
================================================================

--- attention.zig (Turn 19) ---
SPEC: Multi-head attention with scores_scratch and weights_scratch passed in,
      causal mask by integer comparison, softmax per active row, weighted V sum.
      verifySoftmaxSum returns violation count.
WROTE: Matches spec structurally. Attention function takes Q/K/V buffers,
       AttentionConfig, output, and two scratch buffers. Per-head loop computes
       QK^T dot products, applies causal mask (col>row→zero), calls Q16.softmax
       on active portion, zero-fills masked, computes weighted V sum.
DEVIATION: None significant. Function signatures match plan.
CONNECTS TO: vdr/q16.zig (Q16 arithmetic), llm/kv_cache.zig (cache stores K/V)

--- kv_cache.zig (Turn 19) ---
SPEC: KVCache struct with kb_id, dimensions, store pointer, current_len.
      slotIndex computed from layer/position/head/kv_offset.
      append stores K and V per head as VlpFact. loadRange reads back.
      truncate retracts beyond position.
WROTE: Matches spec. init creates KB in store. append/loadRange/truncate implemented.
DEVIATION: append stores SUM of vector components as single fact value — this is lossy.
           The spec says store vector reference. Production needs vector-typed facts
           or a dedicated vector store region. The summary-as-fact is a stub.
REPAIR: Replace fact value with actual per-element storage. Either use one fact per
        element (d_head facts per K and per V per position per head per layer) or
        add a vector region to the device memory layout.
CONNECTS TO: kb/store.zig, kb/fact.zig, kb/types.zig

--- generate.zig (Turn 20) ---
SPEC: GenerateState with model/cache/sampling/position/buffers/RNG.
      prefill forwards each token. generateToken does softmax+sample+forward.
      generateCommand masks to first 300 tokens, renormalizes, greedy samples.
      generateProse generates until end-of-turn.
WROTE: Matches spec. maskNonCommandTokens zeros indices 300+. renormalize
       scales remaining so sum=D with largest absorbing remainder.
DEVIATION: temp_buf in generateToken is a 65536-element stack array. This is
           256KB on stack per call. Should be pre-allocated in GenerateState
           or passed as a parameter.
REPAIR: Move temp_buf to GenerateState as a field, or require caller to pass
        scratch buffer. The stack allocation violates the arena-only rule.
CONNECTS TO: llm/model.zig, llm/forward.zig, llm/softmax.zig, llm/kv_cache.zig,
             llm/sampling.zig, engine/command_parse.zig

--- sampling.zig (Turn 20) ---
SPEC: SamplingConfig, RNG (LCG i64), sampleGreedy, sampleTopK, sampleTopP,
      applyTemperature.
WROTE: Matches spec.
DEVIATION: indices array in sampleTopK and sampleTopP is 65536-element stack array.
           Same issue as generate.zig — 256KB+ on stack. Violates arena rule.
REPAIR: Pass index scratch buffer as parameter, or cap at reasonable size and
        require vocab_size <= buffer size.
CONNECTS TO: vdr/q16.zig

================================================================
DIRECTORY: src/builtins/
================================================================

--- dispatch.zig (Turn 21) ---
SPEC: BuiltinTable with 488 entries, BuiltinEntry with id/fn_ptr/input_types/
      output_type/pure. BuiltinArgs with store/input_facts/text_in/text_out/
      int_args. dispatch validates then calls.
WROTE: BuiltinTable has 512 entries (close enough). BuiltinEntry has
       id/name_offset/name_length/fn_ptr/pure/input_count/output_type.
       BuiltinArgs matches spec.
DEVIATION: Entry stores name_offset+name_length into a name_buf[16384] instead
           of input_types array. The spec says input_types:[]vlp_fact_tag for
           type validation. The implementation only checks input_count, not types.
REPAIR: Add input_types field to BuiltinEntry. validateIOSE should check each
        input fact's tag against declared input_types[i].
CONNECTS TO: Every builtin module registers into this table.

--- text.zig (Turn 21) ---
SPEC: 17 text functions with builtin wrappers.
WROTE: 17 functions match spec names. Core functions (textReverse, textContains,
       etc) are standalone. Builtin wrappers extract args and call core.
DEVIATION: textSplit builtin wrapper is a stub (returns emptyResult). The core
           textSplit function exists but the wrapper doesn't call it because
           the return type (array of slices) doesn't map cleanly to BuiltinResult.
REPAIR: textSplit wrapper should write split results as sequential facts to
        target_kb_id, returning fact count in output_int.
CONNECTS TO: dispatch.zig

--- arithmetic.zig (Turn 21) ---
SPEC: 25 arithmetic functions with builtin wrappers.
WROTE: 25 functions match spec. All delegate to Q16 methods.
DEVIATION: arithFromInt and arithToInt wrappers extract the value oddly —
           builtinFromInt divides input by D before calling arithFromInt which
           multiplies by D, producing the original value. This is correct but
           confusing. The spec says fromInt(val) = val * D directly.
REPAIR: builtinFromInt should pass int_args[0] directly to arithFromInt without
        the intermediate division. Currently the double conversion works by
        accident.
CONNECTS TO: dispatch.zig, vdr/q16.zig

--- collections.zig (Turn 22) ---
SPEC: 36 collection functions.
WROTE: 36 functions match spec names and behavior.
DEVIATION: collSort uses a 4096-element scratch buffer on stack for merge sort.
           This is 32KB — acceptable but should be documented as a hard limit
           on sortable array size. The spec's T22 says merge sort O(n log n)
           but doesn't specify the scratch limit.
           collSortBy uses selection sort O(n²) instead of merge sort. Spec
           doesn't specify algorithm for sortBy but merge sort with custom
           comparator would be better.
           No builtin wrappers — these are library functions not registered in
           dispatch table. Spec T22 doesn't explicitly require registration but
           the function spec Module 22 lists them as VDRPrologBuiltinSort etc.
REPAIR: Add builtin wrappers and register in dispatch table. Add a
        registerCollectionBuiltins function. Fix collSortBy to use merge sort
        if performance matters.
CONNECTS TO: vdr/q16.zig (Q16.compare for ordering)

--- sets.zig (Turn 22) ---
SPEC: 14 set functions on sorted Q16 arrays.
WROTE: 14 functions match spec.
DEVIATION: Same as collections — no dispatch table registration. setPowerSet
           uses a 4096-element scratch in setFromArray (via collSort).
REPAIR: Add builtin wrappers and registerSetBuiltins function.
CONNECTS TO: vdr/q16.zig, collections.zig (collSort used by setFromArray)

--- mappings.zig (Turn 23) ---
SPEC: 15 mapping functions. VlpMap as sorted array of {key:i32, value:vlp_fact}
      with binary search.
WROTE: VlpMap as open-addressing hash table with MapEntry{key, value, occupied}.
       15 functions implemented.
DEVIATION: Spec says sorted array with binary search. Implementation uses
           hash table with linear probing. The hash table is functionally
           correct but diverges from spec. mapDelete has a rehash loop to
           fix probe chains after removal — this is correct for open addressing
           but adds complexity the sorted-array approach avoids.
           mapFilterKeys takes []const i32 (key list) instead of []const bool
           (predicate). Spec says filterKeys(pred) with bool predicate.
           mapMapValues takes Q16 scalar instead of UnaryOp enum. Spec says
           mapValues(op:UnaryOp).
           ALL 15 builtin wrappers are stubs returning emptyResult. They don't
           actually bridge between BuiltinArgs and the map functions.
REPAIR: Either rewrite as sorted array per spec, or document hash table as
        intentional divergence. Fix mapFilterKeys signature to match spec.
        Fix mapMapValues to take UnaryOp. Implement all 15 builtin wrappers
        to actually call the map functions using BuiltinArgs fields.
CONNECTS TO: dispatch.zig, kb/types.zig (VlpFact), vdr/q16.zig

--- conversion.zig (Turn 23) ---
SPEC: 14 conversion functions including JSON/CSV/XML/YAML parsers that write
      to KB, and export functions.
WROTE: parseJson (recursive descent), parseCsv, parseXml, parseYaml, toJson,
       toCsv, toFraction, fromFraction, vdrToDecimalString, decimalStringToVdr,
       baseConvert, timestampToFields. Builtin wrappers implemented for all.
DEVIATION: parseJson skips exponent handling — advances past 'e'/'E' digits
           but doesn't apply the exponent to the value. Numbers like 1.5e3
           parse as 1.5 not 1500.
           parseXml is basic — handles opening tags and text content but not
           attributes, CDATA, namespaces, or self-closing tags properly.
           parseYaml is basic — handles key:value lines but not nested
           indentation, multi-line values, lists (- item), or anchors.
           toJson uses slot IDs as keys ("0", "1", "2") not the original
           JSON key names. The original keys are stored as text facts but
           toJson doesn't reconstruct the key-value pairing.
           timestampToFields is duplicated — exists in both conversion.zig
           and time_ops.zig. time_ops delegates to conversion.
REPAIR: Add exponent handling to parseJson. Improve parseXml to handle
        attributes and self-closing tags. Improve parseYaml to handle
        indentation-based nesting. Fix toJson to use stored key names
        instead of slot indices. Remove duplication with time_ops.
CONNECTS TO: kb/store.zig, kb/fact.zig, vdr/q16.zig

--- register_mappings.zig (Turn 23) ---
SPEC: Not a separate file in the turn plan. Registration was supposed to be
      in dispatch.zig's registerAllBuiltins.
WROTE: Separate file with registerMappingBuiltins and registerConversionBuiltins.
DEVIATION: Separate file is fine architecturally but registerAllBuiltins in
           dispatch.zig doesn't call these registration functions. They're
           orphaned — the builtins exist but aren't reachable via dispatch.
REPAIR: Add calls to registerMappingBuiltins and registerConversionBuiltins
        in dispatch.zig's registerAllBuiltins function.
CONNECTS TO: dispatch.zig, mappings.zig, conversion.zig

--- linalg.zig (Turn 24) ---
SPEC: 24 linear algebra functions (vec_add through mat_solve).
WROTE: 8 functions: matVecMul, transpose, gaussianElim, inverse, determinant,
       gramSchmidt, eigenvalues, svd.
DEVIATION: Spec says 24 functions including vec_add, vec_sub, vec_scale,
           vec_dot, vec_norm, vec_normalize, vec_cross, vec_lerp, vec_distance,
           mat_mul, mat_add, mat_sub, mat_scale, mat_trace, mat_identity,
           mat_fromRows, mat_fromCols, mat_getRow, mat_getCol, mat_solve.
           Implementation has 8 of those 24. Missing 16 vector/matrix helpers.
           eigenvalues for n>2 returns diagonal elements (stub).
           svd returns identity U/Vt (stub).
           inverse uses 4096-element stack array for augmented matrix.
           determinant uses 4096-element stack array for work copy.
           Both limit matrix size to ~45x45.
           Builtin wrappers are all stubs returning emptyResult.
REPAIR: Add the 16 missing functions (vec_*, mat_mul, mat_add, etc).
        Implement eigenvalues via QR iteration. Implement SVD via
        Golub-Kahan. Implement builtin wrappers. Consider passing
        scratch buffers instead of stack arrays.
CONNECTS TO: vdr/q16.zig

--- stats.zig (Turn 24) ---
SPEC: 16 statistics functions (mean through entropy).
WROTE: 9 functions: statsMean, statsVariance, statsMedian, statsBayes,
       statsNormalize, statsHistogram, statsCorrelation, statsCovariance,
       plus builtinMean/Variance/Median/Bayes/Normalize/Histogram/Correlation/
       Covariance.
DEVIATION: Spec says 16 including stddev, mode, min, max, range, percentile,
           softmax (delegate), entropy. Implementation has 9 of 16.
           Missing 7: stddev, mode, min, max, range, percentile, entropy.
           statsMedian sorts in-place via selection sort O(n²). Spec doesn't
           prohibit this but merge sort would be better for large arrays.
           builtinMean/Variance/Median extract values from input_facts into
           a 256-element stack array. This limits statistical operations to
           256 data points through the dispatch interface.
REPAIR: Add the 7 missing functions. stddev = intSqrt(variance).
        mode = frequencies + argmax. min/max/range are trivial.
        percentile = sort + index. entropy needs log approximation.
        Consider passing data arrays via KB reference instead of
        input_facts for larger datasets.
CONNECTS TO: vdr/q16.zig, linalg.zig (intSqrt helper used by correlation)

--- register_linalg.zig (Turn 24) ---
SPEC: Not a separate file.
WROTE: registerLinalgBuiltins (IDs 400-407), registerStatsBuiltins (IDs 420-427).
DEVIATION: Same orphan issue as register_mappings.zig — not called from
           dispatch.zig's registerAllBuiltins.
REPAIR: Add calls in registerAllBuiltins.
CONNECTS TO: dispatch.zig

--- graph.zig (Turn 25) ---
SPEC: 13 graph functions with Graph struct.
WROTE: 13 functions match spec names. Graph struct with nodes[]/edges[] slices.
DEVIATION: All use 1024-element stack arrays for BFS queues, DFS stacks,
           Dijkstra distances, component IDs, cycle colors. This limits
           graph operations to 1024 nodes maximum.
           pageRankExact damping value is hardcoded as 55705 (~0.85).
           Spec says configurable. Should be a parameter.
           Builtin wrappers are all stubs returning emptyResult.
REPAIR: Make stack arrays configurable or document the 1024-node limit.
        Add damping parameter to pageRankExact. Implement builtin wrappers.
CONNECTS TO: vdr/q16.zig

--- integer_ops.zig (Turn 25) ---
SPEC: 21 integer/bit operations.
WROTE: 21 functions match spec. All builtin wrappers implemented and functional.
DEVIATION: None significant. intFactorial and intChoose return i64 but
           builtin wrappers truncate to i32 via @intCast. Large factorials
           will overflow the i32 return. The spec says "bounded" which
           implies this is acceptable.
REPAIR: None needed unless large factorial support required.
CONNECTS TO: dispatch.zig

--- time_ops.zig (Turn 25) ---
SPEC: 10 time functions.
WROTE: 10 functions. timestampNow, timestampDiff, timestampAdd, durationSeconds/
       Minutes/Hours/Days, durationCompare, durationFormat, timestampFields.
       All builtin wrappers implemented.
DEVIATION: Spec T25 lists durationFromMs, durationFromSec, durationToMs,
           durationToSec, formatTimestamp, parseTimestamp, sleepMs.
           Implementation has durationSeconds/Minutes/Hours/Days instead of
           durationFromMs/durationFromSec/durationToMs/durationToSec.
           Missing: formatTimestamp, parseTimestamp, sleepMs.
           timestampFields delegates to conversion.timestampToFields (duplication).
REPAIR: The separate src/builtins/time.zig written in the extras turn has
        formatTimestamp, parseTimestamp, sleepMs. Merge time_ops.zig and
        time.zig into one module, keeping the superset of functions.
        Rename duration functions to match spec if needed.
CONNECTS TO: conversion.zig, dispatch.zig

--- time.zig (extras turn) ---
SPEC: This is the corrected version from the turn plan's T25.
WROTE: timestampNow, timestampDiff, timestampAdd, durationFromMs, durationFromSec,
       durationToMs, durationToSec, formatTimestamp (ISO 8601), parseTimestamp
       (ISO 8601), sleepMs. All builtin wrappers.
DEVIATION: Duplicates time_ops.zig. Both exist in the same directory.
REPAIR: Delete time_ops.zig. Keep time.zig. Update register_graph.zig to import
        from time.zig instead of time_ops.zig. Update any other references.
CONNECTS TO: conversion.zig, dispatch.zig

--- register_graph.zig (Turn 25) ---
SPEC: Not a separate file.
WROTE: registerGraphBuiltins (440-452), registerIntegerOpsBuiltins (460-480),
       registerTimeBuiltins (490-499).
DEVIATION: Same orphan issue — not called from registerAllBuiltins.
           Imports time_ops.zig not time.zig.
REPAIR: Add calls in registerAllBuiltins. Switch import to time.zig.
CONNECTS TO: dispatch.zig

================================================================
DIRECTORY: src/seed/
================================================================

--- seed_init.zig (Turn 26) ---
SPEC: seedInit creates KB tree, calls all loaders, returns SeedIds struct.
WROTE: Matches spec. Creates root, system, oso, confidence, builtins,
       command_vocab, hygiene, templates, sentences, formats.
DEVIATION: Helper functions (assertTextFact, assertValueFact, assertIntFact)
           are defined in seed_init.zig but also used by other seed files.
           The other files reference them via @import but the functions are
           not pub in all cases — may cause import errors.
REPAIR: Ensure assertTextFact/assertValueFact/assertIntFact are pub and
        importable by all seed submodules.
CONNECTS TO: All seed submodules, kb/store.zig, kb/fact.zig

--- oso_rules.zig (Turn 26) ---
SPEC: 15 engineering principles as Prolog terms.
WROTE: 15 principles as text facts (not Prolog terms).
DEVIATION: Spec says "Prolog terms at root.system.oso" and T26 says
           "15 engineering principles as ~176 Prolog terms." Implementation
           stores them as plain text facts, not as VlpTerm structures that
           the Prolog engine can query. They're human-readable but not
           machine-queryable via Prolog unification.
REPAIR: Convert each principle to a VlpTerm (compound term with functor
        "principle" and args for id, name, description). Assert as Prolog-
        compatible facts so they can be queried with Prolog.
CONNECTS TO: prolog/types.zig, prolog/rule.zig

--- confidence_table.zig (Turn 26) ---
SPEC: 11 Q16 values stored as KB facts.
WROTE: Matches spec exactly. Values: 65536, 65536, 64225, 62259, 62259,
       55705, 52428, 45875, 32768, 19660, 0.
DEVIATION: None.
CONNECTS TO: confidence/propagate.zig

--- command_vocab.zig (Turn 26) ---
SPEC: ~300 command names as KB facts.
WROTE: ~300 names across categories (commands, KB ops, Prolog ops, grammar ops,
       primitive ops, builtin names, output ops, scope ops).
DEVIATION: Some builtin names don't match actual registered IDs. For example
           "timestamp_fields_ext" is listed but no such builtin exists.
           The vocabulary should exactly match the registered builtin names.
REPAIR: Audit vocabulary against actual registered builtins. Remove names
        that don't correspond to real functions. Add any missing names.
CONNECTS TO: engine/command_parse.zig (constrained generation vocabulary)

--- hygiene_rules.zig (Turn 26) ---
SPEC: 3 self-maintenance rules as Prolog rules.
WROTE: 3 rule definitions as text facts with conditions and actions as text.
DEVIATION: Same issue as oso_rules — stored as text facts, not as VlpRule
           structures that the Prolog engine can fire. The hygiene scanner
           in prolog/hygiene.zig works by scanning rule statistics directly,
           not by firing these "rules." So these facts are documentation,
           not executable logic.
REPAIR: Either convert to actual VlpRule structures that fire via
        prolog/rule.zig fireAll, or document that hygiene detection is
        implemented directly in prolog/hygiene.zig and these facts are
        reference documentation only.
CONNECTS TO: prolog/hygiene.zig, prolog/rule.zig

--- sentence_templates.zig (Turn 26) ---
SPEC: Sentence structure templates for SRE domain.
WROTE: 12 templates as text facts with grammar slot syntax.
DEVIATION: Templates are stored as raw text, not compiled via grammar/compile.zig.
           They need to be compiled at load time or on first use to be
           renderable via grammar/render.zig.
REPAIR: Either compile each template during seedInit and store the compiled
        VlpGrammar, or add lazy compilation on first render request.
CONNECTS TO: grammar/compile.zig, grammar/render.zig

--- format_grammars.zig (Turn 26 + extras turn) ---
SPEC: Format grammar templates for JSON, CSV, table, HTTP, etc.
WROTE: Two versions exist. Turn 26's seed_init.zig calls loadFormatGrammars.
       The extras turn wrote a standalone format_grammars.zig with 24 templates.
       Turn 26's version was inline in seed_init.zig (18 templates).
DEVIATION: Duplicate implementations. The extras version has 24 templates
           (6 more than Turn 26). Same compilation issue as sentence_templates.
REPAIR: Use the extras version (24 templates). Remove inline version from
        seed_init.zig if it exists separately. Compile templates at load time.
CONNECTS TO: grammar/compile.zig, grammar/render.zig

--- builtin_declarations.zig (Turn 26) ---
SPEC: IOSE declarations for all 448 builtins.
WROTE: 36 representative declarations (id, name, pure flag).
DEVIATION: Only 36 of 448 declared. Missing the vast majority of builtins.
           Stored as sequential facts (id at slot N*3, name at N*3+1,
           pure flag at N*3+2) — awkward layout.
REPAIR: Either declare all registered builtins (currently ~180) or generate
        declarations programmatically from the BuiltinTable at init time
        instead of manually listing them.
CONNECTS TO: builtins/dispatch.zig

================================================================
DIRECTORY: src/test_scenarios/
================================================================

--- sre_scenario.zig (Turn 27) ---
SPEC: Scripted replay of paper Section 10.1 SRE investigation with exact
      token counts and KB state verification at each step.
WROTE: SreScenarioResult with 6 boolean checks. Creates KB tree, asserts
       Prometheus facts, tests confidence propagation, creates incident KB,
       compiles and renders grammar, tests level stats progression.
DEVIATION: Does not replay the exact paper scenario. Missing: mock Prometheus
           fetch, dependency topology KBs, correlation computation, first
           Prolog rule creation, pool saturation check (20/20=Q16(65536)),
           exact token count verification (~570 tokens). The implementation
           tests individual components but doesn't chain them as the paper
           describes.
           Level stats test uses manual update calls instead of running
           vlp_cycle — tests the counter but not the cycle.
REPAIR: Add the missing scenario steps: create dependency topology, compute
        correlation, assert Prolog rule, verify pool saturation, count total
        command tokens against paper's ~570 figure. Run vlp_cycle with mock
        LLM to test L3 path end-to-end.
CONNECTS TO: All prior modules (integration test)

--- determinism_tests.zig (Turn 27) ---
SPEC: 100× memcmp across all operation categories.
WROTE: DeterminismResult with per-category booleans. Tests 9 categories:
       arithmetic, softmax, collections, sets, linalg, stats, graph,
       KB facts, confidence.
DEVIATION: Missing categories from spec: forward pass (toy model), Prolog
           query, grammar render, snapshot save+restore, full cycle (mock LLM).
           The spec T27 says "Run 100 iterations of: Q16 add/mul/softmax,
           forward pass(toy model), Prolog query, grammar render, snapshot
           save+restore, full cycle."
REPAIR: Add forward pass determinism (run toy model 100×, memcmp logits).
        Add Prolog query determinism (parent/grandparent 100×, memcmp bindings).
        Add grammar render determinism (JSON template 100×, memcmp output).
        Add snapshot roundtrip determinism (save+restore 100×, memcmp state).
        Add cycle determinism (mock LLM 100×, memcmp output).
CONNECTS TO: All prior modules

================================================================
DIRECTORY: src/runner/
================================================================

--- types.zig (Turn 28) ---
SPEC: VlpRunner 72 bytes, configs, enums.
WROTE: Matches spec. VlpRunner has all fields. Config structs for all 4 types.
DEVIATION: Added notification_kb_id, log_kb_id, compact_rules_kb_id,
           task_queue_kb_id, result_queue_kb_id, max_concurrent_batch to
           VlpRunner struct. These aren't in the spec's 72-byte struct —
           they expand it. Spec puts these in per-type config, not in the
           runner itself.
REPAIR: Move KB references to per-type config structs or accept the expanded
        struct as a simplification. Document the actual struct size.
CONNECTS TO: runner/pool.zig, runner/poller.zig, runner/processor.zig, etc.

--- pool.zig (Turn 28) ---
SPEC: ThreadPool with threads, task queue, shutdown flag, active count.
      RunnerTable with 64 slots.
WROTE: Matches spec structurally. MAX_RUNNERS=64, MAX_POOL_THREADS=32,
       TASK_QUEUE_CAPACITY=256.
DEVIATION: TaskQueue uses std.Thread.Mutex for synchronization. The spec
           says bounded queue with atomic operations. Mutex is heavier
           but correct. The worker main function uses 10ms sleep polling
           instead of condition variable wait — wastes CPU.
           executeTask and runSingleIteration are stubs that don't actually
           call vlp_cycle. They update runner state but don't execute the
           universal cycle.
REPAIR: Either implement condition variable for efficient blocking or
        document the polling approach. Implement runSingleIteration to
        actually call vlp_cycle with the runner's session and KB store.
        This is the critical gap — runners exist but don't run the cycle.
CONNECTS TO: runner/types.zig, engine/cycle.zig (should call vlp_cycle)

--- poller.zig (Turn 28) ---
SPEC: Timer loop calling vlp_cycle with synthetic input.
WROTE: createPoller, startPoller, pollerIteration, pollerLoop.
       pollerIteration calls prolog_rule.fireAll directly.
DEVIATION: pollerIteration calls prolog_rule.fireAll but NOT vlp_cycle.
           The spec says the poller runs the universal cycle. Currently
           it runs only Phase 0 (rule firing) without the full cycle.
           pollerLoop uses std.time.sleep for timing — correct but coarse.
           writeOutputToKB appends text facts but doesn't use the grammar
           engine for structured output.
REPAIR: Replace pollerIteration with a call to vlp_cycle. The cycle's
        Phase 0 handles rule firing. If Phase 0 resolves everything,
        the cycle returns with zero tokens — same behavior but through
        the proper code path.
CONNECTS TO: engine/cycle.zig, prolog/rule.zig, kb/store.zig

--- runner_manager.zig (Turn 28) ---
SPEC: Facade over table + pool.
WROTE: RunnerManager with init/start/createPoller/startRunner/stopRunner/
       killRunner/recycleRunner/destroyRunner/getStatus/shutdown.
DEVIATION: None significant. Clean facade.
CONNECTS TO: pool.zig, poller.zig, types.zig

--- processor.zig (Turn 29) ---
SPEC: Persistent connection, rule-based compaction, recycle at threshold.
WROTE: ConnectionState, processorIteration, processorRecycle, processorReconnect,
       processorLoop.
DEVIATION: processorIteration calls prolog_rule.fireAll directly instead of
           vlp_cycle — same issue as poller.
           processorRecycle uses session_id+1000 for new session ID. This is
           a placeholder. Real implementation needs session manager allocation.
           processorReconnect always returns .ok after first sleep — the
           reconnection is fake. It sets connected=true without actually
           reconnecting to anything.
           processorLoop has data_len hardcoded to 0 — it never actually
           receives data. The receive path is stubbed.
REPAIR: Replace processorIteration with vlp_cycle call. Fix processorRecycle
        to use session manager's allocate function. Implement actual connection
        management (at minimum, document that external data ingestion requires
        a real connection implementation). Remove hardcoded data_len=0.
CONNECTS TO: engine/cycle.zig, session/lifecycle.zig, session/snapshot.zig

--- internal.zig (Turn 29) ---
SPEC: Timer loop calling compute function.
WROTE: ComputeFn type, createInternal, internalIteration, internalLoop.
       Three default compute stubs (rollingAverage, trendDetection, coverageGap).
DEVIATION: Default compute functions are empty stubs returning .ok.
REPAIR: Implement at least one real compute function (e.g., rolling average:
        read last N values from ring buffer, compute exact mean, assert as
        derived fact).
CONNECTS TO: runner/types.zig, kb/store.zig

--- batch.zig (Turn 29) ---
SPEC: Clone-per-task from KB queue.
WROTE: BatchClone, batchPopTask, batchWriteResult, batchProcessTask,
       batchIteration, batchLoop.
DEVIATION: batchProcessTask copies task value as result — doesn't run vlp_cycle.
           batchPopTask reads slot 0 and retracts — this is not a proper queue
           pop. It always reads the first slot regardless of queue state. Should
           use the Queue primitive from primitives/queue.zig.
           batchIteration has a confusing loop condition for spawning new clones
           that references active_count in a way that may not terminate correctly.
REPAIR: Replace batchProcessTask with vlp_cycle call. Use Queue primitive for
        task popping. Fix spawn loop condition.
CONNECTS TO: engine/cycle.zig, primitives/queue.zig, session/lifecycle.zig

--- runner_ops.zig (Turn 29) ---
SPEC: Convenience wrappers.
WROTE: createProcessorRunner, createInternalRunner, createBatchRunner,
       startProcessorRunner, startInternalRunner, startBatchRunner,
       recycleProcessor.
DEVIATION: None significant.
CONNECTS TO: runner_manager.zig

--- sre_deployment.zig (Turn 29) ---
SPEC: 4-runner SRE deployment.
WROTE: SreDeploymentConfig, SreDeployment, createSreDeployment,
       startSreDeployment, stopSreDeployment, getSreStatus.
DEVIATION: Creates all 4 runners but they don't actually do anything because
           the underlying runner loops are stubbed (no vlp_cycle calls).
REPAIR: Depends on fixing poller/processor/internal to call vlp_cycle.
CONNECTS TO: All runner modules

================================================================
DIRECTORY: src/server/
================================================================

--- types.zig (Turn 30) ---
SPEC: Server struct, connection, credential, config types.
WROTE: Matches spec. MAX_CONNECTIONS=256. ServerConnection with read_buf/
       write_buf[8192]. Server with connections array, atomic counters.
DEVIATION: Server struct stores a *KBStore pointer. The spec says server
           owns the store. This is fine — the store is allocated externally
           and passed in.
CONNECTS TO: kb/store.zig

--- listener.zig (Turn 30) ---
SPEC: TCP socket, accept loop, connection management.
WROTE: createListenSocket, acceptConnection, closeSocket, socketRead,
       socketWrite, findFreeSlot, acceptLoop, closeConnection.
DEVIATION: socketRead ignores timeout_ms parameter — reads are blocking
           without timeout. This can hang indefinitely on a slow client.
           acceptLoop runs synchronously in a single thread. The spec
           says submit to thread pool for handling after accept. The
           implementation accepts and initializes the connection but
           doesn't submit the connection to the pool for vlp_cycle handling.
REPAIR: Implement socket timeout via setsockopt SO_RCVTIMEO or poll/select.
        After accepting and initializing the connection in acceptLoop,
        submit to thread pool for handleConnection.
CONNECTS TO: server/types.zig, std.posix

--- auth.zig (Turn 30) ---
SPEC: Authentication via auth KB.
WROTE: authenticate, credentialCheck, credentialRevoke, hashCredential,
       createAuthKB, registerUser, suspendUser, reactivateUser.
DEVIATION: hashCredential uses FNV-1a which is fine for non-crypto hashing.
           Auth KB layout uses user_id*4 + offset for slot addressing.
           This limits to ~256 users in a 1024-fact KB.
           authenticate scans linearly for token hash match — O(n) instead
           of O(1) hash index lookup.
REPAIR: Use PathIndex or a dedicated hash map for O(1) token lookup.
        Document the user limit or make it configurable.
CONNECTS TO: kb/store.zig, kb/fact.zig, server/types.zig

--- handler.zig (Turn 31) ---
SPEC: HTTP request parser, connection handler, request routing.
WROTE: Request/Response structs, parseHttpRequest, handleConnection,
       handleRequestLoop, processRequest (routing), sendResponse,
       sendErrorResponse, sendRateLimitResponse.
DEVIATION: processRequest routes to health/metrics/kb/query endpoints
           but none of these call vlp_cycle. processHealthRequest and
           processMetricsRequest render JSON from server counters directly.
           processKbRequest reads KB info but doesn't run inference.
           processQueryRequest returns a stub response.
           The spec says each request transforms to vlp_input → vlp_cycle →
           grammar-rendered response. The implementation skips vlp_cycle entirely.
REPAIR: processQueryRequest should transform the request body into vlp_input,
        call vlp_cycle, and render the output through grammar. The health and
        metrics endpoints can remain as direct integer renders (they don't
        need LLM inference).
CONNECTS TO: server/types.zig, server/listener.zig, server/auth.zig,
             engine/cycle.zig (should call but doesn't)

--- rate_limit.zig (Turn 31) ---
SPEC: Per-user counter in KB with window-based reset.
WROTE: RateLimitConfig, checkRateLimit, createRateLimitKB, resetRateLimit,
       getRateLimitStatus.
DEVIATION: Uses a global mutable variable (global_rate_config) for configuration.
           This violates the "no global mutable state" rule. Should be passed
           as a parameter or stored on the Server struct.
REPAIR: Move RateLimitConfig to Server struct or pass as parameter to
        checkRateLimit.
CONNECTS TO: kb/store.zig, kb/fact.zig

--- health.zig (Turn 32) ---
SPEC: HealthReport from integer counters, grammar-rendered JSON.
WROTE: HealthReport, collectHealth, renderHealthJson.
DEVIATION: renderHealthJson builds JSON via string concatenation, not via
           grammar engine. The spec says "render report via grammar → every
           brace/colon from template." The implementation uses hardcoded
           string literals for JSON structure.
REPAIR: Load health grammar from protocol grammar KB, render via
        grammar/render.zig. This demonstrates the grammar engine for
        operational output.
CONNECTS TO: server/types.zig, grammar/render.zig (should use but doesn't)

--- reaper.zig (Turn 32) ---
SPEC: Periodic scan, three integer comparisons per connection.
WROTE: reaperScan, reaperLoop, sendTimeoutNotice, sendExpiredNotice.
DEVIATION: None significant. Matches spec behavior.
CONNECTS TO: server/types.zig, server/listener.zig

--- shutdown.zig (Turn 32) ---
SPEC: Graceful shutdown sequence.
WROTE: gracefulShutdown returns ShutdownResult.
DEVIATION: None significant. Matches spec sequence.
CONNECTS TO: server/types.zig, server/listener.zig, session/snapshot.zig

--- server_main.zig (Turn 32) ---
SPEC: ServerRuntime facade.
WROTE: ServerRuntime with init/start/stop/isRunning/getHealth/getMetrics.
DEVIATION: start spawns accept and reaper threads. Does not start any
           runners. The spec says server start should also initialize
           the SRE deployment runners.
REPAIR: Add runner manager initialization and SRE deployment start to
        ServerRuntime.start if configured.
CONNECTS TO: All server modules, runner/runner_manager.zig

================================================================
DIRECTORY: src/protocol/
================================================================

--- http.zig (Turn 33) ---
SPEC: Full HTTP/1.1 request parser with WebSocket upgrade detection.
WROTE: HttpRequest (32 headers, WebSocket fields), parseRequest, buildResponse,
       sendHttpResponse, sendHttpError.
DEVIATION: parseRequest duplicates much of handler.zig's parseHttpRequest.
           Both exist and parse HTTP requests differently. handler.zig parses
           into a simpler Request struct. http.zig parses into a richer
           HttpRequest struct with header array and WebSocket fields.
REPAIR: Use http.zig's parser as the canonical HTTP parser. Have handler.zig
        use HttpRequest from http.zig instead of its own Request struct.
        Remove the duplicate parser.
CONNECTS TO: server/handler.zig, protocol/websocket.zig

--- websocket.zig (Turn 33) ---
SPEC: WebSocket upgrade, frame read/write, message loop.
WROTE: WsOpcode, WsFrame, wsUpgrade, wsReadFrame, wsSendText, wsSendClose,
       wsSendPong, wsSendFrame, wsHandleLoop, processWsMessage.
DEVIATION: wsUpgrade computes accept key via simple hash instead of SHA-1+base64.
           This will fail with real WebSocket clients — the accept key must be
           SHA-1(client_key + magic_guid) base64-encoded per RFC 6455.
           processWsMessage returns a stub JSON response. It doesn't call
           vlp_cycle.
           wsSendFrame length encoding for 64-bit payloads uses a var shift
           that may not compile correctly due to type constraints on the
           shift amount.
REPAIR: Implement proper SHA-1 + base64 for accept key (or use a library).
        Replace processWsMessage with vlp_cycle call. Fix 64-bit frame
        length encoding.
CONNECTS TO: server/types.zig, server/listener.zig, server/auth.zig,
             engine/cycle.zig (should call but doesn't)

--- grammars.zig (Turn 33) ---
SPEC: Protocol grammar templates stored in KB.
WROTE: 10 grammar slot constants, initProtocolGrammars, renderHttpResponse,
       renderJsonResult, renderJsonError.
DEVIATION: initProtocolGrammars stores templates as text facts but doesn't
           compile them via grammar/compile.zig. renderHttpResponse builds
           HTTP response via string concatenation, not grammar rendering.
           The render helpers bypass the grammar engine entirely.
REPAIR: Compile each template via grammar/compile.zig during init.
        Use grammar/render.zig for all rendering.
CONNECTS TO: grammar/compile.zig, grammar/render.zig, kb/store.zig

--- protocol_router.zig (Turn 33) ---
SPEC: Route connections by protocol type.
WROTE: routeConnection function.
DEVIATION: Reads 4 peek bytes but doesn't use them for protocol detection.
           Routes based on server.config.protocol enum. The peek read is
           wasted.
REPAIR: Either remove the peek read or use it for auto-detection (HTTP
        starts with GET/POST/PUT, MQTT starts with 0x10, etc).
CONNECTS TO: server/handler.zig, protocol/http.zig, protocol/websocket.zig

--- smtp.zig (Turn 34) ---
SPEC: SMTP state machine stub.
WROTE: SmtpState, SmtpVerb, sendGreeting, readCommand, sendResponse,
       smtpHandleLoop.
DEVIATION: None significant for a stub. Basic state machine works.
CONNECTS TO: server/types.zig, server/listener.zig

--- mqtt.zig (Turn 34) ---
SPEC: MQTT stub.
WROTE: MqttPacketType, MqttConnect, MqttPublish, readConnect, sendConnack,
       readPublish, sendPingresp, mqttHandleLoop.
DEVIATION: readConnect doesn't parse the CONNECT packet body — it reads
           remaining bytes but discards them. client_id, username, password
           are never populated.
           mqttHandleLoop reads one peek byte for packet type but then calls
           readPublish which reads its own header — double-reading the first
           byte.
REPAIR: Fix double-read issue. Parse CONNECT body to extract client_id
        at minimum.
CONNECTS TO: server/types.zig, server/listener.zig

================================================================
DIRECTORY: src/ops/
================================================================

--- filesystem.zig (Turn 34) ---
SPEC: Grant-gated file operations.
WROTE: fsRead, fsWrite, fsAppend, fsDelete, fsStat, fsReadToKB.
DEVIATION: Does not check grants — the grant check is supposed to happen
           in the command executor before dispatch, but the ops functions
           themselves don't verify. This is correct per the architecture
           (grant check at dispatch level, not at operation level) but
           should be documented.
           fsAppend opens file in write_only mode then seeks to end.
           std.fs doesn't support this combination well. Should use
           .mode = .read_write or create a new file with append flag.
REPAIR: Fix fsAppend to use proper append semantics. Document that
        grant checking happens at dispatch level.
CONNECTS TO: kb/store.zig, builtins/dispatch.zig

--- network.zig (Turn 34) ---
SPEC: HTTP client for fetching data.
WROTE: netFetch (stub returning placeholder JSON), netFetchToKB.
DEVIATION: Complete stub. No actual HTTP client.
REPAIR: Implement using std.http.Client or raw TCP socket with HTTP/1.1
        request construction.
CONNECTS TO: kb/store.zig

--- execute.zig (Turn 34) ---
SPEC: Subprocess execution.
WROTE: execRun (stub returning placeholder), execRunToKB.
DEVIATION: Complete stub. No actual subprocess execution.
REPAIR: Implement using std.process.Child.
CONNECTS TO: kb/store.zig

--- compile_check.zig (Turn 34) ---
SPEC: Syntax validation via balanced delimiters.
WROTE: compileCheck with balanced delimiter checking.
DEVIATION: None for what it does. It's a delimiter checker, not a real
           compiler syntax check.
CONNECTS TO: builtins/dispatch.zig

--- compile_op.zig (extras turn) ---
SPEC: Same as compile_check.zig with enhanced features.
WROTE: CompileResult with brace/paren/bracket depths. compileCheck with
       string literal handling (skips delimiters inside quotes) and
       line comment handling (skips // to newline).
       compileCheckWithLanguage (delegates to compileCheck ignoring language).
DEVIATION: Duplicates compile_check.zig functionality. compile_op.zig is
           more complete (handles strings and comments).
REPAIR: Keep compile_op.zig, delete compile_check.zig. Update ops_dispatch.zig
        to import from compile_op.zig.
CONNECTS TO: builtins/dispatch.zig

--- process.zig (Turn 34) ---
SPEC: Process management.
WROTE: ProcessHandle, procStart (stub), procKill, procStatus.
DEVIATION: Complete stub. procStart returns pid=-1, active=false.
REPAIR: Implement using std.process.Child.
CONNECTS TO: builtins/dispatch.zig

--- ops_dispatch.zig (Turn 34) ---
SPEC: Builtin wrappers for all ops + registration.
WROTE: 11 builtin wrappers, registerOpsBuiltins (IDs 500-510).
DEVIATION: registerOpsBuiltins is not called from dispatch.zig's
           registerAllBuiltins — same orphan issue as other register files.
           builtinCompileCheck imports compile_check.zig not compile_op.zig.
REPAIR: Add call in registerAllBuiltins. Switch import to compile_op.zig.
CONNECTS TO: builtins/dispatch.zig

================================================================
DIRECTORY: src/config/
================================================================

--- system_config.zig (Turn 35) ---
SPEC: SystemConfig struct with all fields from paper Section 18.
WROTE: Matches spec with additional server and rate limit fields.
DEVIATION: None significant.
CONNECTS TO: config/cli.zig, config/config_file.zig

--- cli.zig (Turn 35) ---
SPEC: Minimal CLI parser.
WROTE: CliArgs, parseCli, printHelp, printVersion.
DEVIATION: None significant. Covers all config fields.
CONNECTS TO: config/system_config.zig

--- config_file.zig (Turn 35) ---
SPEC: Key=value config file parser.
WROTE: parseConfigFile with key=value parsing, comment handling.
DEVIATION: Local function name collisions — defines eql and parseI32
           locally which may shadow or conflict with cli.zig if both
           are imported.
REPAIR: Use unique names or make them shared utility functions.
CONNECTS TO: config/system_config.zig

--- integration_test.zig (Turn 35) ---
SPEC: 13-check integration test exercising complete stack.
WROTE: IntegrationResult with 13 checks, runIntegrationTest, printResult.
DEVIATION: Allocates backing buffers on stack: kb_buf[4096], fact_buf[65536],
           text_buf[262144], path_entries[8192]. Total ~2.4MB on stack.
           This may stack overflow on some platforms.
           Tests don't actually start a server or send HTTP requests. The
           spec T35 says "start server on localhost:0 → HTTP POST → verify."
           The implementation tests components individually.
REPAIR: Move backing buffers to heap or static allocation. Add actual
        server start + HTTP request test (even via loopback).
CONNECTS TO: All modules

--- main.zig (Turn 35) ---
SPEC: Entry point.
WROTE: Parses CLI, loads config file, runs tests or prints config.
DEVIATION: Doesn't actually start the server. The main function prints
           config values and "Starting server..." but doesn't call
           ServerRuntime.start().
REPAIR: Add ServerRuntime initialization and start call. Add signal
        handling for graceful shutdown.
CONNECTS TO: config/*.zig, server/server_main.zig

================================================================
DIRECTORY: src/gpu/
================================================================

--- device.zig (Turn 36) ---
SPEC: Device enumeration, GPU init via CUDA interop.
WROTE: CPU fallback only. Global DeviceState. DeviceProps with all integer fields.
DEVIATION: Spec says "CUDA C interop calling cudaGetDeviceCount/cudaSetDevice."
           Implementation is CPU-only with no CUDA calls. This is documented
           and intentional for Phase 1.
           Uses global mutable state (global_device_state) which violates the
           "no global mutable state" rule.
REPAIR: Pass DeviceState as parameter instead of using global. Add CUDA
        interop when GPU hardware available.
CONNECTS TO: gpu/memory.zig, gpu/transfer.zig

--- memory.zig (Turn 36) ---
SPEC: Device memory layout with 13 regions.
WROTE: DeviceMemoryLayout, MemoryConfig, computeLayout, DeviceAllocation.
DEVIATION: DeviceAllocation uses host_buf (host memory) for CPU fallback.
           Actual GPU implementation would use cudaMalloc.
           computeLayout uses sequential placement with 256-byte alignment.
           Matches spec.
CONNECTS TO: gpu/device.zig, gpu/transfer.zig

--- transfer.zig (Turn 36) ---
SPEC: Host-device transfer, KB store mirroring.
WROTE: hostToDevice, deviceToHost, deviceToDevice, transferQ16Array,
       transferQ16ArrayBack, mirrorKBStore, deviceFactWrite, deviceFactRead,
       memorySummary.
DEVIATION: All transfers are memcpy within host_buf for CPU fallback.
           mirrorKBStore calls store.text.readAll() — this function may not
           exist on TextStore. TextStore has append and read(offset,length)
           but not readAll.
REPAIR: Add readAll to TextStore or use read(0, len) in mirrorKBStore.
CONNECTS TO: gpu/memory.zig, kb/store.zig

--- kb_device.zig (extras turn) ---
SPEC: Device-side KB store mirroring host KBStore.
WROTE: DeviceKBStore with factWrite/factRead/kbWrite/kbRead/mirrorFromHost/
       syncToHost.
DEVIATION: Imports VlpStatus from types_op (the ops compile_op module) instead
           of from vdr/types.zig. This is a broken import — will cause
           compilation error.
REPAIR: Change VlpStatus import to @import("../vdr/types.zig").VlpStatus.
CONNECTS TO: gpu/memory.zig, kb/store.zig, kb/fact.zig

--- profiling.zig (Turn 39) ---
SPEC: KernelStats, SessionStats, Profiler.
WROTE: Matches spec. Profiler with start/stop/recordKernel/getKernelStats.
DEVIATION: None significant.
CONNECTS TO: gpu/benchmarks.zig

--- benchmarks.zig (Turn 39) ---
SPEC: 8 benchmarks with nanoTimestamp measurement.
WROTE: 8 benchmarks: forward_pass, softmax, attention, sort, layernorm,
       prolog_unify, elementwise, gemm. runAllBenchmarks returns [8]BenchResult.
DEVIATION: Benchmark inputs are small fixed sizes (4x16 forward, 64 softmax,
           4x1x8 attention, 256 sort, 64 layernorm, 64 prolog, 256 elementwise,
           8x8x8 gemm). These are too small to be meaningful performance
           measurements — they mostly measure function call overhead.
REPAIR: Add configurable size parameters. Add larger default sizes that
        exercise actual compute patterns.
CONNECTS TO: gpu/kernels/*.zig

--- determinism.zig (Turn 39) ---
SPEC: Run kernel N times, byte-compare all outputs.
WROTE: verifyDeterminismSoftmax, verifyDeterminismGemm,
       verifyDeterminismAttention, runFullDeterminismSuite.
DEVIATION: None significant. Correctly tests byte-identical output across runs.
CONNECTS TO: gpu/kernels/*.zig

================================================================
DIRECTORY: src/gpu/kernels/
================================================================

--- gemm.zig (Turn 37) ---
SPEC: Q16 GEMM via integer MMA tiles, CUDA C kernel.
WROTE: CPU implementation. q16Gemm, q16GemmBatched, q16GemmStridedBatched,
       q16MatVecMul.
DEVIATION: Not CUDA — CPU only. The spec says "CUDA C kernel for Q16 GEMM.
           Tiled 128x128." The implementation is a scalar triple loop. This is
           correct for CPU fallback but not a GPU kernel.
           q16Gemm scales by alpha/(D*D) which is correct for the case where
           alpha is a Q16 scalar, but differs from the simpler spec description.
CONNECTS TO: vdr/q16.zig

--- softmax.zig (Turn 37) ---
SPEC: Quadratic surrogate with warp-level reduction.
WROTE: CPU implementation. q16Softmax, q16SoftmaxBatched, verifySoftmaxSum.
DEVIATION: Uses 4096-element stack array for shifted values. Limits softmax
           to 4096 elements. For vocab_size softmax (50K+), this is too small.
           The spec says per-row warp reduce — GPU specific.
REPAIR: For CPU fallback, allocate scratch from caller or use the scratch
        region from DeviceAllocation. For GPU, implement warp-level reduction.
CONNECTS TO: vdr/q16.zig

--- elementwise.zig (Turn 37) ---
SPEC: Per-element Q16 operations.
WROTE: q16Add/Sub/Mul/Div/Scale/Dot/Compare/Negate/Abs/Min/Max/Clamp/Fill/
       Copy/Sum/RemainderMagnitude.
DEVIATION: None significant. Clean delegation to Q16 methods.
CONNECTS TO: vdr/q16.zig

--- normalize.zig (Turn 37) ---
SPEC: LayerNorm and RMSNorm.
WROTE: q16LayerNorm, q16RMSNorm.
DEVIATION: intSqrt is implemented locally (Newton iteration). Same function
           exists in linalg.zig. Should share.
           inv_std computation: divTrunc(D*D, sqrt_result). This produces
           1/sqrt(var) scaled by D. The spec says "rsqrt via Newton iteration
           3-4 steps." The implementation uses full Newton sqrt then inverts.
REPAIR: Extract intSqrt to a shared utility module to avoid duplication.
CONNECTS TO: vdr/q16.zig

--- activation.zig (Turn 37) ---
SPEC: ReLU, GELU, SiLU.
WROTE: q16ReLU, q16GELU, q16SiLU.
DEVIATION: q16GELU uses linear sigmoid approximation. The spec says "quadratic
           activation" for MLP. GELU(x) ≈ x * sigmoid(1.702*x) is the standard
           approximation but the implementation uses a cruder linear version.
           q16SiLU has a confusing sigmoid approximation that may not be
           mathematically correct for all input ranges.
REPAIR: For Phase 1, ReLU is sufficient (the paper uses ReLU as the architecture
        adaptation). GELU and SiLU can be improved later with FRU-based exact
        implementations.
CONNECTS TO: vdr/q16.zig

--- attention.zig (Turn 38) ---
SPEC: Fused attention kernel.
WROTE: fusedAttentionForward, verifySoftmaxSumAllHeads,
       fusedAttentionWithKVCache.
DEVIATION: Duplicates src/llm/attention.zig functionality. Both implement
           multi-head attention. The gpu/kernels version has an additional
           fusedAttentionWithKVCache for single-query against cached K/V.
           The llm/ version uses separate scores_scratch and weights_scratch
           passed by caller. The gpu/kernels version uses internal 4096-element
           stack arrays.
REPAIR: Consolidate. The gpu/kernels version should be the canonical
        implementation. The llm/ version should delegate to it. Or keep
        both: llm/ version for the engine layer API, gpu/kernels version
        for the kernel dispatch layer.
CONNECTS TO: gpu/kernels/softmax.zig

--- sort.zig (Turn 38) ---
SPEC: Bitonic sort for GPU.
WROTE: Merge sort (not bitonic). q16Sort, q16ArgSort, q16TopK.
DEVIATION: Spec says bitonic sort for GPU (work-efficient, no data-dependent
           branching). Implementation uses merge sort (fine for CPU but not
           GPU-friendly). q16ArgSort uses selection sort O(n²).
REPAIR: For GPU, implement bitonic sort. For CPU fallback, merge sort is fine.
CONNECTS TO: vdr/q16.zig

--- prolog_kernel.zig (Turn 38) ---
SPEC: Parallel unification with shared memory, warp vote.
WROTE: batchUnify, batchCrossMultiplyCompare, scopeFilter, parallelRuleEval.
DEVIATION: CPU sequential implementation, not GPU parallel. batchUnify iterates
           candidates sequentially. The spec says "each thread handles one
           candidate, warp vote __ballot_sync to collect matches."
           unifyTerms handles basic cases (atom, integer, VDR, text, compound)
           but doesn't do proper recursive unification for compound terms —
           it only checks functor ID and arg count, not the actual args.
           scopeFilter correctly implements the ancestor walk with visibility
           checking — this is the structural security check.
REPAIR: For GPU, implement warp-parallel unification. Fix unifyTerms to
        recursively unify compound term arguments.
CONNECTS TO: prolog/types.zig

--- reduction.zig (Turn 38) ---
SPEC: Reduce operations and allreduce stubs.
WROTE: q16ReduceSum/Max/Min/ArgMax/ArgMin, i32ReduceSum, allReduceSum/Max stubs.
DEVIATION: None significant. allReduce stubs are placeholders.
CONNECTS TO: vdr/q16.zig

================================================================
DIRECTORY: src/deploy/
================================================================

--- distributed.zig (Turn 40) ---
SPEC: Comm, allreduce, broadcast, etc.
WROTE: Single-rank passthroughs for all operations.
DEVIATION: Complete stubs. No actual multi-rank communication.
           The key property (integer sum is associative → deterministic
           across topologies) is documented but not tested.
REPAIR: For single-machine multi-GPU, implement via shared memory or
        cudaMemcpyPeer. For multi-node, implement TCP transport.
CONNECTS TO: vdr/q16.zig

--- model_parallel.zig (Turn 40) ---
SPEC: Layer sharding, pipeline forward with cross-device transfer.
WROTE: ModelParallelConfig, DeviceShard, ModelParallel with init/pipelineForward/
       getShardInfo.
DEVIATION: pipelineForward is a passthrough — copies input to output without
           running any layers. The per-layer compute is commented as stub.
REPAIR: Integrate with llm/forward.zig to run actual layer computation per shard.
CONNECTS TO: gpu/device.zig, llm/forward.zig

--- multi_device.zig (extras turn) ---
SPEC: Same as model_parallel.zig.
WROTE: MultiDeviceConfig, DeviceShard, MultiDevice with init/getShardForLayer/
       pipelineForward/totalLayers/shardSummary.
DEVIATION: Duplicates model_parallel.zig. Both exist. multi_device.zig has
           additional utility functions (getShardForLayer, totalLayers,
           shardSummary) that model_parallel.zig lacks.
REPAIR: Merge into one module. Keep the superset of functions.
CONNECTS TO: gpu/device.zig, gpu/memory.zig

--- load_balancer.zig (Turn 40) ---
SPEC: Round-robin and least-connections routing.
WROTE: LoadBalancer with 16 backends, addBackend, route, releaseBackend,
       markUnhealthy, markHealthy, removeUnhealthy.
DEVIATION: None significant. Clean implementation.
CONNECTS TO: server/types.zig

--- prometheus_export.zig (Turn 40) ---
SPEC: Prometheus exposition format rendering.
WROTE: exportPrometheus function rendering metrics as "name value\n".
DEVIATION: None significant.
CONNECTS TO: server/health.zig

--- monitoring.zig (extras turn) ---
SPEC: Extended monitoring with configurable prefix and runner details.
WROTE: MonitoringConfig, exportPrometheus (with prefix and runner details),
       exportHealthJson.
DEVIATION: Duplicates prometheus_export.zig and health.zig rendering.
           monitoring.zig is more complete (configurable prefix, labeled
           runner metrics).
REPAIR: Keep monitoring.zig as the canonical monitoring module. Remove or
        thin prometheus_export.zig to delegate to monitoring.zig.
CONNECTS TO: server/health.zig, runner/types.zig

--- chaos.zig (Turn 40) ---
SPEC: 4 chaos tests.
WROTE: testSnapshotRecovery, testKillRestart, testConcurrentWrite,
       testDeterminismAfterRestart.
DEVIATION: testConcurrentWrite writes 100 facts sequentially, not concurrently.
           The name implies concurrent access from multiple threads but the
           test is single-threaded.
REPAIR: Either rename to testSequentialWrite or implement actual concurrent
        write test using multiple threads.
CONNECTS TO: kb/store.zig, session/snapshot.zig, gpu/determinism.zig

--- deploy_main.zig (Turn 40) ---
SPEC: Deployment verification.
WROTE: DeploymentResult, deployAndVerify, printDeployResult.
DEVIATION: server_started and runners_started are hardcoded to true without
           actually starting anything.
REPAIR: Actually start ServerRuntime and runners, then set flags based on
        success.
CONNECTS TO: All modules

--- gcp_setup.zig (extras turn) ---
SPEC: GCloud CLI command builders.
WROTE: GcpInstanceConfig, buildCreateCommand, buildStartCommand,
       buildStopCommand, buildDeleteCommand, buildSshCommand.
DEVIATION: None significant. Builds gcloud CLI command strings.
           Doesn't execute them — just constructs the strings.
CONNECTS TO: Standalone utility

================================================================
DIRECTORY: src/engine/
================================================================

--- scratchpad.zig (extras turn) ---
SPEC: Ring buffer for command results.
WROTE: Scratchpad struct with writeResult/writeError/writeDenied/
       writeGrantDenied/writeFactResult/writeRuleFired/writeCommandResult/
       clear/getContents/isEmpty/remaining.
DEVIATION: Implemented as a simple append buffer, not a ring buffer. When
           capacity is reached, subsequent writes are silently truncated.
           The spec says ring buffer (overwrite oldest). The implementation
           never wraps.
REPAIR: Implement as ring buffer matching AuditRing pattern, or document
        the truncation behavior as intentional (scratchpad is cleared each
        cycle so overflow is unlikely in practice).
CONNECTS TO: engine/cycle.zig, engine/command_exec.zig

================================================================
CRITICAL REPAIR PRIORITIES (ordered by impact)
================================================================

1. RUNNERS DON'T CALL VLP_CYCLE
   poller, processor, batch all bypass vlp_cycle.
   Without this, the L1/L2/L3 progression doesn't work in production.
   Fix: Replace direct prolog_rule.fireAll calls with vlp_cycle calls.

2. SERVER HANDLER DOESN'T CALL VLP_CYCLE
   HTTP handler routes requests but never runs inference.
   Fix: processQueryRequest must call vlp_cycle.

3. DISPATCH TABLE REGISTRATION INCOMPLETE
   registerAllBuiltins only calls arithmetic + text.
   Collections, sets, mappings, conversion, linalg, stats, graph,
   integer_ops, time, ops — all have register functions that are
   never called.
   Fix: Add all register calls to registerAllBuiltins.

4. BUILTIN WRAPPERS ARE STUBS
   mappings (15), linalg (8), graph (13) wrappers return emptyResult.
   Fix: Implement each wrapper to bridge BuiltinArgs to core functions.

5. SEED RULES NOT PROLOG-COMPATIBLE
   OSO principles and hygiene rules stored as text, not VlpTerm.
   Fix: Convert to compound terms queryable via Prolog unification.

6. GRAMMAR ENGINE BYPASSED
   health.zig, grammars.zig, handler.zig all build JSON via string
   concatenation instead of grammar/render.zig.
   Fix: Use grammar engine for all structured output.

7. DUPLICATE MODULES
   time_ops.zig vs time.zig, compile_check.zig vs compile_op.zig,
   model_parallel.zig vs multi_device.zig, prometheus_export.zig vs
   monitoring.zig, http.zig parser vs handler.zig parser.
   Fix: Keep the more complete version, delete the other, update imports.

8. STACK ARRAYS VIOLATE ARENA RULE
   generate.zig temp_buf[65536], sampling.zig indices[65536],
   linalg.zig aug[4096], graph.zig seen/queue/dist[1024],
   softmax.zig shifted[4096].
   Fix: Pass scratch buffers as parameters or pre-allocate in parent struct.

9. BROKEN IMPORT IN kb_device.zig
   Imports VlpStatus from ops/compile_op.zig instead of vdr/types.zig.
   Fix: Change import path.

10. GLOBAL MUTABLE STATE
    gpu/device.zig global_device_state, server/rate_limit.zig global_rate_config.
    Fix: Pass as parameters.
```
