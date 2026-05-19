# TensorProlog Build Turn Plan

## Repository Setup Script

```bash
#!/bin/bash
# TensorProlog repository structure
# Run from project root

mkdir -p src/vdr
mkdir -p src/kb
mkdir -p src/prolog
mkdir -p src/grammar
mkdir -p src/session
mkdir -p src/primitives
mkdir -p src/safety
mkdir -p src/confidence
mkdir -p src/engine
mkdir -p src/llm
mkdir -p src/builtins
mkdir -p src/seed
mkdir -p src/runner
mkdir -p src/server
mkdir -p src/protocol
mkdir -p src/ops
mkdir -p src/config
mkdir -p src/gpu
mkdir -p src/deploy
mkdir -p test
mkdir -p config
mkdir -p models
mkdir -p data/snapshots
mkdir -p data/sessions
mkdir -p data/seed
mkdir -p scripts

# Core types and arithmetic
touch src/vdr/types.zig
touch src/vdr/q16.zig
touch src/vdr/q32.zig
touch src/vdr/q335.zig
touch src/vdr/reproject.zig

# Knowledge base
touch src/kb/types.zig
touch src/kb/store.zig
touch src/kb/fact.zig
touch src/kb/tree.zig
touch src/kb/path_index.zig
touch src/kb/visibility.zig
touch src/kb/text_store.zig

# Prolog
touch src/prolog/types.zig
touch src/prolog/term.zig
touch src/prolog/unify.zig
touch src/prolog/query.zig
touch src/prolog/rule.zig
touch src/prolog/hygiene.zig

# Grammar
touch src/grammar/types.zig
touch src/grammar/compile.zig
touch src/grammar/render.zig
touch src/grammar/validate.zig
touch src/grammar/inherit.zig

# Session
touch src/session/types.zig
touch src/session/lifecycle.zig
touch src/session/cow.zig
touch src/session/snapshot.zig

# Bounded primitives
touch src/primitives/types.zig
touch src/primitives/lru.zig
touch src/primitives/counter.zig
touch src/primitives/lock.zig
touch src/primitives/queue.zig
touch src/primitives/stack.zig
touch src/primitives/ring.zig
touch src/primitives/bitset.zig

# Safety
touch src/safety/types.zig
touch src/safety/grant.zig
touch src/safety/audit.zig

# Confidence
touch src/confidence/types.zig
touch src/confidence/propagate.zig

# Engine (universal cycle)
touch src/engine/cycle.zig
touch src/engine/context.zig
touch src/engine/command_parse.zig
touch src/engine/command_exec.zig
touch src/engine/scratchpad.zig
touch src/engine/auto_resolve.zig
touch src/engine/token_classify.zig
touch src/engine/level_stats.zig

# LLM
touch src/llm/model.zig
touch src/llm/forward.zig
touch src/llm/attention.zig
touch src/llm/softmax.zig
touch src/llm/generate.zig
touch src/llm/kv_cache.zig
touch src/llm/sampling.zig

# Builtins
touch src/builtins/dispatch.zig
touch src/builtins/text.zig
touch src/builtins/collections.zig
touch src/builtins/sets.zig
touch src/builtins/mappings.zig
touch src/builtins/arithmetic.zig
touch src/builtins/conversion.zig
touch src/builtins/linalg.zig
touch src/builtins/stats.zig
touch src/builtins/graph.zig
touch src/builtins/integer_ops.zig
touch src/builtins/time.zig

# Seed
touch src/seed/init.zig
touch src/seed/oso_rules.zig
touch src/seed/hygiene_rules.zig
touch src/seed/confidence_table.zig
touch src/seed/command_vocab.zig

# Runner
touch src/runner/types.zig
touch src/runner/pool.zig
touch src/runner/poller.zig
touch src/runner/processor.zig
touch src/runner/internal.zig
touch src/runner/batch.zig

# Server
touch src/server/types.zig
touch src/server/listener.zig
touch src/server/handler.zig
touch src/server/auth.zig
touch src/server/rate_limit.zig
touch src/server/health.zig
touch src/server/reaper.zig
touch src/server/shutdown.zig

# Protocol
touch src/protocol/http.zig
touch src/protocol/websocket.zig
touch src/protocol/smtp.zig
touch src/protocol/mqtt.zig
touch src/protocol/grammars.zig

# Ops (grant-gated)
touch src/ops/filesystem.zig
touch src/ops/network.zig
touch src/ops/execute.zig
touch src/ops/compile_op.zig
touch src/ops/process.zig

# Config
touch src/config/system_config.zig
touch src/config/cli.zig
touch src/config/config_file.zig

# GPU (Phase 5)
touch src/gpu/device.zig
touch src/gpu/kernel_mac.zig
touch src/gpu/kernel_softmax.zig
touch src/gpu/kernel_attention.zig
touch src/gpu/kernel_layernorm.zig
touch src/gpu/kernel_elementwise.zig
touch src/gpu/kernel_prolog.zig
touch src/gpu/kernel_sort.zig
touch src/gpu/kb_device.zig
touch src/gpu/transfer.zig
touch src/gpu/profiling.zig

# Deploy (Phase 6)
touch src/deploy/gcp_setup.zig
touch src/deploy/multi_device.zig
touch src/deploy/distributed.zig
touch src/deploy/load_balancer.zig
touch src/deploy/monitoring.zig

# Tests
touch test/test_q16.zig
touch test/test_q32.zig
touch test/test_q335.zig
touch test/test_reproject.zig
touch test/test_kb_store.zig
touch test/test_fact_store.zig
touch test/test_tree.zig
touch test/test_path_index.zig
touch test/test_visibility.zig
touch test/test_text_store.zig
touch test/test_prolog_unify.zig
touch test/test_prolog_query.zig
touch test/test_prolog_rules.zig
touch test/test_prolog_hygiene.zig
touch test/test_grammar_compile.zig
touch test/test_grammar_render.zig
touch test/test_grammar_inherit.zig
touch test/test_session_lifecycle.zig
touch test/test_session_snapshot.zig
touch test/test_session_clone.zig
touch test/test_primitives_lru.zig
touch test/test_primitives_counter.zig
touch test/test_primitives_queue.zig
touch test/test_primitives_stack.zig
touch test/test_primitives_ring.zig
touch test/test_primitives_bitset.zig
touch test/test_primitives_lock.zig
touch test/test_grant.zig
touch test/test_audit.zig
touch test/test_confidence.zig
touch test/test_cycle.zig
touch test/test_context.zig
touch test/test_command_parse.zig
touch test/test_command_exec.zig
touch test/test_auto_resolve.zig
touch test/test_forward.zig
touch test/test_softmax.zig
touch test/test_attention.zig
touch test/test_generate.zig
touch test/test_kv_cache.zig
touch test/test_sampling.zig
touch test/test_builtins_text.zig
touch test/test_builtins_collections.zig
touch test/test_builtins_sets.zig
touch test/test_builtins_mappings.zig
touch test/test_builtins_arithmetic.zig
touch test/test_builtins_conversion.zig
touch test/test_builtins_linalg.zig
touch test/test_builtins_stats.zig
touch test/test_builtins_graph.zig
touch test/test_builtins_integer_ops.zig
touch test/test_builtins_time.zig
touch test/test_seed.zig
touch test/test_sre_scenario.zig
touch test/test_runner_poller.zig
touch test/test_runner_processor.zig
touch test/test_runner_batch.zig
touch test/test_server_http.zig
touch test/test_server_websocket.zig
touch test/test_server_auth.zig
touch test/test_server_rate_limit.zig
touch test/test_server_shutdown.zig
touch test/test_ops_filesystem.zig
touch test/test_ops_network.zig
touch test/test_integration_full.zig
touch test/test_determinism.zig
touch test/test_gpu_q16_ops.zig
touch test/test_gpu_softmax.zig
touch test/test_gpu_attention.zig
touch test/test_gpu_determinism.zig
touch test/test_gpu_forward.zig
touch test/test_gpu_prolog.zig
touch test/test_gpu_benchmark.zig
touch test/test_multi_gpu.zig
touch test/test_distributed.zig
touch test/test_load_test.zig
touch test/test_chaos.zig

# Build file
touch build.zig

# Config files
touch config/dev.yaml
touch config/test_local.yaml
touch config/test_gcp.yaml
touch config/production.yaml

# Scripts
touch scripts/setup_gcp.sh
touch scripts/upload_and_test.sh
touch scripts/bench.sh

echo "TensorProlog repository structure created: $(find src -name '*.zig' | wc -l) source files, $(find test -name '*.zig' | wc -l) test files"
```

---

## Turn Plan

Each turn targets ~1,200 lines. Source and tests for a module group ship together. Dependencies flow strictly downward — no turn references code from a later turn.

---

### Turn 1: Foundation Types + Q16 Arithmetic
**Files:** `src/vdr/types.zig`, `src/vdr/q16.zig`, `test/test_q16.zig`
**Lines:** ~800

- All shared type enums (vlp_qbasis, vlp_fact_tag, vlp_source_type, vlp_status, etc.)
- Q16 struct: add, sub, mul, div, compare, eql, fromFraction, toFraction, zero, one, remainderMagnitude, compact, negate, abs, sign, min, max
- Softmax surrogate function (array in, array out, sum verified = D)
- Dot product function
- Test: all arithmetic ops, edge cases, softmax sum invariant, 1000-run determinism

---

### Turn 2: Q32 + Q335 + Reproject
**Files:** `src/vdr/q32.zig`, `src/vdr/q335.zig`, `src/vdr/reproject.zig`, `test/test_q32.zig`, `test/test_q335.zig`, `test/test_reproject.zig`
**Lines:** ~1,100

- Q32 struct: same ops as Q16 but i64 value, two remainder levels
- Q335 struct: limb-based 384-bit arithmetic, 4 fixed remainder levels
- Limb helpers: add_limbs, mul_limbs, shr_limbs, compare_limbs
- Reproject: Q16→Q32, Q32→Q16 (with remainder), Q16→Q335, Q335→Q16
- Tests: Q32 arithmetic, Q335 basic ops, reproject roundtrip, cross-basis comparison

---

### Turn 3: KB Types + Store + Text Store
**Files:** `src/kb/types.zig`, `src/kb/store.zig`, `src/kb/text_store.zig`, `test/test_kb_store.zig`, `test/test_text_store.zig`
**Lines:** ~1,100

- vlp_kb struct (26 fields), vlp_fact struct, vlp_provenance struct
- KBStore: init, createKB, destroyKB, getKB, count, capacity
- Contiguous KB array management, sequential ID assignment
- TextStore: append-only byte store, allocate (returns offset+length), read
- Tests: create/destroy KBs, sequential IDs, text store append/read roundtrip

---

### Turn 4: Fact Store + Tree + Path Index
**Files:** `src/kb/fact.zig`, `src/kb/tree.zig`, `src/kb/path_index.zig`, `test/test_fact_store.zig`, `test/test_tree.zig`, `test/test_path_index.zig`
**Lines:** ~1,100

- FactStore: assert, query, retract, search by tag, scoped search up parent chain
- Tree: addChild, removeChild, getParent, getChildren, ancestorWalk
- PathIndex: open-addressing hash map, insert, lookup, remove, resize
- Tests: fact CRUD, scoped search finds ancestor not sibling, dotted path resolution

---

### Turn 5: Visibility + Safety Types + Grant
**Files:** `src/kb/visibility.zig`, `src/safety/types.zig`, `src/safety/grant.zig`, `test/test_visibility.zig`, `test/test_grant.zig`
**Lines:** ~1,000

- checkAccess: scope walk with integer visibility comparison
- resolveVisibleKBs: enumerate visible KBs, prune subtrees
- vlp_grant struct, vlp_grant_state enum, vlp_grant_class enum
- GrantStore: create, check (4 integer comparisons), revoke, list, cleanup expired
- Tests: PUBLIC/INTERNAL/OWNER_ONLY visibility, nested restriction, grant lifecycle, expiry, exhaustion, revocation

---

### Turn 6: Audit + Confidence
**Files:** `src/safety/audit.zig`, `src/confidence/types.zig`, `src/confidence/propagate.zig`, `test/test_audit.zig`, `test/test_confidence.zig`
**Lines:** ~800

- vlp_audit_entry struct, AuditRing: fixed-capacity ring buffer, write (append-only), query by filter
- Confidence table as const array of Q16 values (11 source types)
- assignFromSource, combineAgreeing, combineConflicting, chain, propagate through derivation
- Tests: audit append/read/overflow, confidence combine/chain exact values from Appendix M worked examples

---

### Turn 7: Prolog Types + Terms + Unification
**Files:** `src/prolog/types.zig`, `src/prolog/term.zig`, `src/prolog/unify.zig`, `test/test_prolog_unify.zig`
**Lines:** ~1,000

- vlp_term_type enum, vlp_term struct (tagged union), vlp_binding, vlp_binding_set
- Term constructors: atom, variable, integer, vdr, text, list, compound
- Term equality, term contains variable (occurs check)
- unify: recursive, depth-limited, all cases (atom-atom, var-anything, VDR cross-multiply, compound, list)
- Tests: all unification cases, occurs check, depth limit, VDR exact comparison

---

### Turn 8: Prolog Query + Rules
**Files:** `src/prolog/query.zig`, `src/prolog/rule.zig`, `test/test_prolog_query.zig`, `test/test_prolog_rules.zig`
**Lines:** ~1,100

- query: depth-first search with backtracking over KB facts, scoped
- Candidate collection from fact store, sequential unification attempts
- Backtrack: undo bindings, try next candidate
- vlp_rule struct, RuleStore: assertRule, retractRule, getRuleStats
- fireAll: evaluate all rules against current facts, return fired list
- fireAndCommit: fireAll + apply assert/retract actions
- Tests: simple query, rule firing, backtracking, multiple solutions, scoped query

---

### Turn 9: Prolog Hygiene + Grammar Types + Compile
**Files:** `src/prolog/hygiene.zig`, `src/grammar/types.zig`, `src/grammar/compile.zig`, `test/test_prolog_hygiene.zig`, `test/test_grammar_compile.zig`
**Lines:** ~900

- hygieneScan: detect stale (>90 days unfired), failing (<20% success), orphaned (revoked grant ref)
- vlp_grammar struct, vlp_grammar_slot struct, vlp_grammar_fill struct, vlp_slot_type enum
- compile: parse template, extract slot markers `{name:type}`, build slot table, validate matching braces
- Tests: hygiene detection for each category, grammar compile simple/multi-slot/enum/nested

---

### Turn 10: Grammar Render + Validate + Inherit
**Files:** `src/grammar/render.zig`, `src/grammar/validate.zig`, `src/grammar/inherit.zig`, `test/test_grammar_render.zig`, `test/test_grammar_inherit.zig`
**Lines:** ~900

- render: walk template, memcpy literals, render fills by type (VDR→decimal, text→copy, int→decimal, enum→copy)
- renderFromKB: fill slots from KB facts by mapping
- validate: check template structural correctness for all valid fills
- inherit: walk KB tree upward looking for grammar at slot
- Tests: render all slot types, JSON template, capacity overflow, inheritance from ancestor

---

### Turn 11: Primitives — LRU + Counter + Lock
**Files:** `src/primitives/types.zig`, `src/primitives/lru.zig`, `src/primitives/counter.zig`, `src/primitives/lock.zig`, `test/test_primitives_lru.zig`, `test/test_primitives_counter.zig`, `test/test_primitives_lock.zig`
**Lines:** ~1,100

- Shared primitive types (capacity ranges, overflow behaviors)
- LRU: init(capacity), get(key), put(key, value), evictOldest, size, clear. Doubly-linked list + hash map.
- Counter: init(min, max, initial), get, increment(amount), reset, atBound. Clamp, never wrap.
- Lock: init, acquire→bool, release, query→bool. Non-blocking.
- Tests: LRU eviction at capacity, counter clamping, lock acquire/release semantics

---

### Turn 12: Primitives — Queue + Stack + Ring + Bitset
**Files:** `src/primitives/queue.zig`, `src/primitives/stack.zig`, `src/primitives/ring.zig`, `src/primitives/bitset.zig`, `test/test_primitives_queue.zig`, `test/test_primitives_stack.zig`, `test/test_primitives_ring.zig`, `test/test_primitives_bitset.zig`
**Lines:** ~1,200

- Queue: init(capacity), push→bool, pop→?fact, peek→?fact, size, clear. Circular buffer.
- Stack: init(capacity), push→bool, pop→?fact, peek→?fact, size, clear. Array with top index.
- Ring: init(capacity), write (always succeeds, overwrites oldest), read(index), size, clear.
- Bitset: init(n_bits), set(bit), clear(bit), get(bit)→bool, popcount, clearAll.
- Tests: FIFO/LIFO ordering, bounds enforcement, ring overwrite, bitset popcount

---

### Turn 13: Session Types + Lifecycle + COW
**Files:** `src/session/types.zig`, `src/session/lifecycle.zig`, `src/session/cow.zig`, `test/test_session_lifecycle.zig`, `test/test_session_clone.zig`
**Lines:** ~1,200

- vlp_session struct (all counters, state, device refs, lineage)
- create: allocate session, bind to KB root, init primitives
- destroy: free resources
- clone: create COW page table, share parent persistent KBs
- merge: iterate dirty pages, apply to parent with conflict detection
- kill: immediate free, no snapshot
- COWPageTable: read, writeBegin (copy-on-first-write), dirtyPages, resolve
- Tests: create/destroy, clone independence (modify child, parent unchanged), merge, kill

---

### Turn 14: Snapshot
**Files:** `src/session/snapshot.zig`, `test/test_session_snapshot.zig`
**Lines:** ~800

- vlp_snapshot_header struct (magic, version, region sizes, counts, checksum)
- save: collect all session state (KBs, facts, rules, terms, text, grammars, live state, grants), pack contiguous, CRC32
- restore: validate checksum, overwrite all session state
- saveToFile: write blob to filesystem
- loadFromFile: read blob, validate
- diff: byte-compare regions, report differences
- Tests: save/restore roundtrip (bit-identical memcmp), modify-then-restore reverts, diff detects changes, corrupt checksum → hard fail

---

### Turn 15: Engine — Context + Scratchpad + Token Classify + Level Stats
**Files:** `src/engine/context.zig`, `src/engine/scratchpad.zig`, `src/engine/token_classify.zig`, `src/engine/level_stats.zig`, `test/test_context.zig`
**Lines:** ~900

- context_build: assemble system prompt (from seed KB, cached) + scope ref + scratchpad + user input
- Scratchpad: per-session ring buffer, write_result, write_error, write_denied, clear
- token_classify: given token_id, return COMMAND_START / DIRECT_OUTPUT / END_OF_TURN / PROSE
- LevelStats: l1/l2/l3 counters, update, getAutoTriageRate (exact fraction)
- Tests: context assembly produces bounded size, token classification, level stats fractions

---

### Turn 16: Engine — Command Parse + Command Exec
**Files:** `src/engine/command_parse.zig`, `src/engine/command_exec.zig`, `test/test_command_parse.zig`, `test/test_command_exec.zig`
**Lines:** ~1,100

- vlp_command struct, vlp_command_type enum
- parse: match first token to command type enum, resolve dotted path, parse typed args
- execute: access check → grant check (if operational) → dispatch by type
- Dispatch: KB_ASSERT, KB_QUERY, KB_RETRACT, PROLOG_QUERY, PROLOG_ASSERT_RULE, BUILTIN_CALL, GRAMMAR_RENDER, DIRECT_OUTPUT
- Audit write after each execution
- Tests: parse valid commands, parse invalid → error, execute with access denied, execute with grant denied, execute KB_ASSERT + KB_QUERY roundtrip

---

### Turn 17: Engine — Auto Resolve + Universal Cycle
**Files:** `src/engine/auto_resolve.zig`, `src/engine/cycle.zig`, `test/test_auto_resolve.zig`, `test/test_cycle.zig`
**Lines:** ~1,100

- auto_resolve: check if auto-fired rules fully handle input (grammar ref + confidence threshold + direct output action)
- vlp_cycle: Phase 0 (fire rules) → Phase 1 (context) → Phase 2 (generate + dispatch loop) → Phase 3 (post-cycle)
- The universal cycle function. Everything calls this.
- Tests: auto-resolve with matching rule → zero tokens, auto-resolve below threshold → falls through, cycle end-to-end with mock LLM

---

### Turn 18: LLM — Model + Forward + Softmax
**Files:** `src/llm/model.zig`, `src/llm/forward.zig`, `src/llm/softmax.zig`, `test/test_forward.zig`, `test/test_softmax.zig`
**Lines:** ~1,100

- Model struct: weight storage, layer config, load from checkpoint
- forward: embedding lookup → per-layer (layernorm → QKV proj → attention → residual → MLP → residual) → final norm → logit projection
- All using Q16 ops from Turn 1
- softmax: quadratic surrogate, sum = D invariant
- Tests: forward pass on toy model matches VDR-32 reference output, softmax sum = 65536 always, loss decreases over training epochs

---

### Turn 19: LLM — Attention + KV Cache
**Files:** `src/llm/attention.zig`, `src/llm/kv_cache.zig`, `test/test_attention.zig`, `test/test_kv_cache.zig`
**Lines:** ~1,000

- attention: QK^T → scale → causal mask → softmax → AV. Multi-head.
- Causal mask: if col > row, weight = 0. Integer comparison.
- KVCache: init in session KB, append (store K,V at layer+position), load range, truncate
- KV entries are vlp_facts at computed slot IDs in a dedicated KB
- Tests: attention weights sum to D per row, KV cache stores/loads exactly, KV cache survives snapshot/restore

---

### Turn 20: LLM — Generate + Sampling
**Files:** `src/llm/generate.zig`, `src/llm/sampling.zig`, `test/test_generate.zig`, `test/test_sampling.zig`
**Lines:** ~800

- generate_token: forward for last position, softmax, sample
- generate_command: constrained vocabulary mask, generate until end marker, parse
- Sampling: greedy (argmax), top_k (sort top K, normalize, sample), top_p (accumulate sorted probs to threshold), temperature (divide logits by T before softmax)
- Tests: greedy determinism (1000 runs identical), top_k produces valid tokens, temperature=D is identity

---

### Turn 21: Builtins — Dispatch + Text + Arithmetic
**Files:** `src/builtins/dispatch.zig`, `src/builtins/text.zig`, `src/builtins/arithmetic.zig`, `test/test_builtins_text.zig`, `test/test_builtins_arithmetic.zig`
**Lines:** ~1,200

- BuiltinTable: array of 448 function pointers, dispatch by id, IOSE validation
- Text (17): reverse, split, contains, replace, join, trim, upper, lower, startsWith, endsWith, indexOf, substring, repeat, padLeft, padRight, charAt, length
- Arithmetic (25): add, sub, mul, div, pow, reciprocal, compare, equal, min, max, sign, isZero, floor, ceil, round, numerator, denominator, abs, negate, clamp
- Tests: text operations, arithmetic exactness

---

### Turn 22: Builtins — Collections + Sets
**Files:** `src/builtins/collections.zig`, `src/builtins/sets.zig`, `test/test_builtins_collections.zig`, `test/test_builtins_sets.zig`
**Lines:** ~1,200

- Collections (36): sort, sortBy, filter, map, reduce, groupBy, frequencies, distinct, flatten, chunk, zip, unzip, reverse, rotate, takeFirst, takeLast, dropFirst, dropLast, partition, interleave, enumerate, minBy, maxBy, scan, all, any, none, count, findFirst, findLast, findAll, binarySearch, merge, deduplicate, window, cartesianProduct
- Sets (14): union, intersection, difference, symmetricDiff, isSubset, isSuperset, isDisjoint, contains, add, remove, size, equal, powerSet, fromArray
- Tests: sort correctness, set operations, boundary cases

---

### Turn 23: Builtins — Mappings + Conversion
**Files:** `src/builtins/mappings.zig`, `src/builtins/conversion.zig`, `test/test_builtins_mappings.zig`, `test/test_builtins_conversion.zig`
**Lines:** ~1,200

- Mappings (15): get, set, delete, containsKey, keys, values, size, merge, filterKeys, filterValues, mapValues, invert, clear, equal, fromArrays
- Conversion (14): parseJson, parseCsv, parseXml, parseYaml, toJson, toCsv, toFraction, fromFraction, formatNumber, parseNumber, vdrToDecimalString, decimalStringToVdr, baseConvert, timestampToFields
- JSON/CSV parsers are compiled state machines writing to KB facts
- Tests: mapping CRUD, JSON parse→KB→toJson roundtrip, CSV parse

---

### Turn 24: Builtins — LinAlg + Stats
**Files:** `src/builtins/linalg.zig`, `src/builtins/stats.zig`, `test/test_builtins_linalg.zig`, `test/test_builtins_stats.zig`
**Lines:** ~1,200

- LinAlg (24): vec_add, vec_sub, vec_scale, vec_dot, vec_norm, vec_normalize, vec_cross, vec_lerp, vec_distance, mat_mul, mat_add, mat_sub, mat_scale, mat_transpose, mat_inverse, mat_determinant, mat_trace, mat_identity, mat_fromRows, mat_fromCols, mat_getRow, mat_getCol, mat_gramSchmidt, mat_solve
- Stats (16): mean, variance, stddev, median, mode, min, max, range, percentile, covariance, correlation, normalize, histogram, bayes, softmax, entropy
- Tests: matrix inverse roundtrip (A * A_inv = I exact), stats on known distributions

---

### Turn 25: Builtins — Graph + Integer Ops + Time
**Files:** `src/builtins/graph.zig`, `src/builtins/integer_ops.zig`, `src/builtins/time.zig`, `test/test_builtins_graph.zig`, `test/test_builtins_integer_ops.zig`, `test/test_builtins_time.zig`
**Lines:** ~1,200

- Graph (13): create, addNode, addEdge, removeNode, removeEdge, bfs, dfs, shortestPath, topologicalSort, connectedComponents, cycleDetect, pageRankExact, markovSteady
- IntegerOps (21): int_add through int_choose (13), bit_and through bit_reverse (8)
- Time (10): timestampNow, timestampDiff, timestampAdd, durationFromMs, durationFromSec, durationToMs, durationToSec, formatTimestamp, parseTimestamp, sleep
- Tests: graph algorithms on known graphs, bit operations, time arithmetic

---

### Turn 26: Seed Layer
**Files:** `src/seed/init.zig`, `src/seed/oso_rules.zig`, `src/seed/hygiene_rules.zig`, `src/seed/confidence_table.zig`, `src/seed/command_vocab.zig`, `test/test_seed.zig`
**Lines:** ~1,000

- init: create root KB tree (root, root.system, root.system.oso, root.system.confidence, root.system.builtins, root.system.hygiene, root.templates, root.templates.formats)
- oso_rules: 15 engineering principles as Prolog terms
- hygiene_rules: 3 self-maintenance rules (stale, failing, orphan)
- confidence_table: 11 source-type confidence values as KB facts
- command_vocab: ~300 command names as KB facts for constrained generation
- Tests: seed init creates expected KB structure, rules queryable, confidence table values match spec

---

### Turn 27: SRE Scenario Test + Determinism Test
**Files:** `test/test_sre_scenario.zig`, `test/test_determinism.zig`
**Lines:** ~1,000

- SRE scenario: scripted replay of paper Section 10.1 fresh investigation
  - Create incident KB, assert facts, fetch mock Prometheus data, parse JSON, compute correlation, write Prolog rule, render findings via grammar, verify confidence propagation
  - Assert exact token counts match paper claims
  - Assert all KB state correct at each step
- Determinism: run every operation (arithmetic, forward pass, prolog query, grammar render, snapshot roundtrip, full cycle) 100 times, memcmp all outputs
- These are the two most important tests in the system

---

### Turn 28: Runner — Types + Pool + Poller
**Files:** `src/runner/types.zig`, `src/runner/pool.zig`, `src/runner/poller.zig`, `test/test_runner_poller.zig`
**Lines:** ~1,000

- vlp_runner struct, vlp_runner_type/state enums, vlp_runner_task
- ThreadPool: init, submit, shutdown. Fixed-size worker thread array. Bounded task queue.
- Worker thread main: pop task, execute, mark idle.
- Poller: timer loop, synthetic input, run vlp_cycle, route output to notification KB, error tracking, recycle check
- Tests: poller fires rules on schedule, zero LLM tokens for known patterns, error threshold stops runner

---

### Turn 29: Runner — Processor + Internal + Batch
**Files:** `src/runner/processor.zig`, `src/runner/internal.zig`, `src/runner/batch.zig`, `test/test_runner_processor.zig`, `test/test_runner_batch.zig`
**Lines:** ~1,200

- Processor: connection management, ingest loop, compact to KB, recycle (snapshot→kill→clone→restore connection), exponential backoff reconnect
- Internal: timer loop, compute_fn callback, KB-only computation
- Batch: task queue consumer, clone-per-task, merge results, kill clone, max_concurrent management
- Tests: processor recycle preserves knowledge, batch clone isolation, merge results back

---

### Turn 30: Server — Types + Listener + Auth
**Files:** `src/server/types.zig`, `src/server/listener.zig`, `src/server/auth.zig`, `test/test_server_auth.zig`
**Lines:** ~1,100

- vlp_server struct, vlp_server_connection, vlp_server_credential
- Listener: socket bind/listen, accept loop, capacity check, slot allocation
- Auth: hash credential, lookup in auth KB, load visibility/grants/status, issue credential with TTL, check (2 integer comparisons), revoke
- Tests: valid auth → credential issued, invalid token → rejected, expired credential → denied, revoked → denied

---

### Turn 31: Server — Handler + Rate Limit
**Files:** `src/server/handler.zig`, `src/server/rate_limit.zig`, `test/test_server_http.zig`, `test/test_server_rate_limit.zig`
**Lines:** ~1,200

- Handler: handshake → authenticate → clone from template → credential inject → request loop (check credential → read request → input transform → vlp_cycle → output transform → send response) → cleanup
- Session recycle at turn threshold within connection
- RateLimiter: counter per user in auth KB, window check (integer comparison), increment, reset on new window
- Tests: HTTP request/response cycle, credential expiry mid-session, rate limit enforcement, exact remaining count

---

### Turn 32: Server — Health + Reaper + Shutdown
**Files:** `src/server/health.zig`, `src/server/reaper.zig`, `src/server/shutdown.zig`, `test/test_server_shutdown.zig`
**Lines:** ~800

- Health: collect all integer metrics (connections, requests, level distribution, KB/rule/fact counts, runner states), render via grammar
- Reaper: scan connections, kill idle (integer timestamp comparison), kill expired credentials, recycle turn-budget sessions
- Shutdown: signal flag, stop accepting, stop runners, drain connections (with timeout), force-close, snapshot persistent sessions, save state, shutdown pool
- Tests: graceful shutdown preserves session snapshots, reaper kills idle connections

---

### Turn 33: Protocol — HTTP + WebSocket
**Files:** `src/protocol/http.zig`, `src/protocol/websocket.zig`, `src/protocol/grammars.zig`, `test/test_server_websocket.zig`
**Lines:** ~1,200

- HTTP: read_request (state machine parser), parse headers (Content-Length, Authorization, Connection, Content-Type), read body, build vlp_input
- Protocol response assembly from grammar-rendered parts (status line grammar, header grammar, body grammar)
- WebSocket: upgrade handshake, frame read/write (text, binary, ping/pong, close), message loop calling vlp_cycle per message
- Protocol grammars: HTTP response templates, WebSocket close frames
- Tests: WebSocket message loop, credential expiry → close frame 4001, ping/pong

---

### Turn 34: Protocol — SMTP + MQTT (stubs) + Ops
**Files:** `src/protocol/smtp.zig`, `src/protocol/mqtt.zig`, `src/ops/filesystem.zig`, `src/ops/network.zig`, `src/ops/execute.zig`, `src/ops/compile_op.zig`, `src/ops/process.zig`, `test/test_ops_filesystem.zig`, `test/test_ops_network.zig`
**Lines:** ~1,200

- SMTP stub: greeting grammar, EHLO response, basic command parsing (full impl is Phase 6)
- MQTT stub: CONNECT/CONNACK grammar, basic packet parsing (full impl is Phase 6)
- Ops (all grant-gated): filesystem (read, write, append, delete, stat), network (HTTP GET/POST, response to KB), execute (subprocess with stdout capture to KB), compile (syntax check), process (start, kill, status)
- Tests: filesystem read/write with grant, without grant → denied, network fetch mock

---

### Turn 35: Config + CLI + Build File + Integration Test
**Files:** `src/config/system_config.zig`, `src/config/cli.zig`, `src/config/config_file.zig`, `build.zig`, `test/test_integration_full.zig`
**Lines:** ~1,100

- vlp_system_config struct with all fields and defaults
- CLI: parse command-line args (--config, --port, --shutdown)
- Config file: simple YAML-like parser using text builtins, populate system_config
- build.zig: Zig build file with targets: test-phase1 through test-phase6, bench, run
- Integration test: start server on localhost, send HTTP requests, verify responses, check metrics endpoint, verify runner status, shutdown gracefully
- Config templates: dev.yaml, test_local.yaml, test_gcp.yaml, production.yaml

---

### Turn 36: GPU — Device + Memory Layout + Transfer
**Files:** `src/gpu/device.zig`, `src/gpu/kb_device.zig`, `src/gpu/transfer.zig`
**Lines:** ~1,000

- Device init: enumerate GPUs, select, allocate memory layout (all regions from spec Section 4)
- Memory layout struct: model_weights, kb_store, fact_store, rule_store, term_store, text_store, grammar_store, live_state, scratch, audit, grant_store, session_table, path_index regions
- KB device store: mirror of CPU KB store on device memory, fact read/write via device pointers
- Transfer: host→device, device→host, typed transfers for VDR arrays and KB structs
- No tests yet — needs GPU hardware. Test files created but marked skip-without-gpu.

---

### Turn 37: GPU — MAC + Softmax + Elementwise Kernels
**Files:** `src/gpu/kernel_mac.zig`, `src/gpu/kernel_softmax.zig`, `src/gpu/kernel_elementwise.zig`, `test/test_gpu_q16_ops.zig`, `test/test_gpu_softmax.zig`
**Lines:** ~1,200

- MAC kernel: Q16 matrix multiply via INT8/INT16 tensor core path (CUDA C kernel called via Zig C interop)
- Tiled GEMM: 128×128 tiles, shared memory staging, widening multiply + shift
- Softmax kernel: shift-square-divide, sum = D. Warp-level reduction for sum.
- Elementwise kernels: add, sub, mul, div, scale, compare. One thread per element.
- Tests (GPU): Q16 ops match CPU reference byte-for-byte, softmax sum = 65536 on GPU

---

### Turn 38: GPU — Attention + LayerNorm + Sort + Prolog Kernels
**Files:** `src/gpu/kernel_attention.zig`, `src/gpu/kernel_layernorm.zig`, `src/gpu/kernel_sort.zig`, `src/gpu/kernel_prolog.zig`, `test/test_gpu_attention.zig`, `test/test_gpu_prolog.zig`
**Lines:** ~1,200

- Attention kernel: fused QK^T → scale → mask → softmax → AV. One thread block per head.
- LayerNorm kernel: exact mean (integer sum / n), exact variance, normalize. Warp reduction for sum.
- Sort kernel: bitonic sort for builtins. Integer comparison.
- Prolog kernel: load facts to shared memory, parallel cross-multiply unification across warp, filter matches, collect.
- Tests (GPU): attention weights match CPU, parallel prolog matches sequential

---

### Turn 39: GPU — Profiling + Benchmarks + Determinism
**Files:** `src/gpu/profiling.zig`, `test/test_gpu_determinism.zig`, `test/test_gpu_forward.zig`, `test/test_gpu_benchmark.zig`
**Lines:** ~800

- Profiling: kernel timing (event-based), integer ops count, memory bytes, warp occupancy, KB cache hits/misses
- Determinism verification: run N times, memcmp all outputs
- Forward pass test: toy model on GPU matches CPU bit-for-bit
- Benchmark: GEMM throughput, softmax throughput, attention throughput, prolog query throughput, report TOPS
- Tests (GPU): 100-run determinism, forward pass cross-platform match

---

### Turn 40: Deploy + Multi-Device + Distributed + Scripts
**Files:** `src/deploy/gcp_setup.zig`, `src/deploy/multi_device.zig`, `src/deploy/distributed.zig`, `src/deploy/load_balancer.zig`, `src/deploy/monitoring.zig`, `scripts/setup_gcp.sh`, `scripts/upload_and_test.sh`, `scripts/bench.sh`, `test/test_multi_gpu.zig`, `test/test_distributed.zig`, `test/test_load_test.zig`, `test/test_chaos.zig`
**Lines:** ~1,200

- GCP setup helpers: instance creation, driver install, Zig install
- Multi-device: model shard assignment, pipeline forward across GPUs, KV-cache per device
- Distributed: integer allreduce (associative, deterministic), broadcast, KB sync
- Load balancer: round-robin across instances, health-check based routing
- Monitoring: Prometheus-compatible metrics export (all integer values, grammar-rendered)
- Scripts: bash scripts for GCP setup, upload+test, benchmarking
- Tests (multi-GPU): allreduce determinism, model parallel forward, chaos (kill instance, verify recovery)

---

## Turn Summary

| Turn | Phase | Files | Lines | Module Group |
|:---|:---|:---|:---|:---|
| 1 | 1 | 3 | ~800 | VDR types + Q16 arithmetic |
| 2 | 1 | 6 | ~1,100 | Q32 + Q335 + reproject |
| 3 | 1 | 5 | ~1,100 | KB types + store + text store |
| 4 | 1 | 6 | ~1,100 | Fact store + tree + path index |
| 5 | 1 | 5 | ~1,000 | Visibility + grants |
| 6 | 1–2 | 5 | ~800 | Audit + confidence |
| 7 | 2 | 4 | ~1,000 | Prolog types + terms + unification |
| 8 | 2 | 4 | ~1,100 | Prolog query + rules |
| 9 | 2 | 5 | ~900 | Prolog hygiene + grammar compile |
| 10 | 2 | 5 | ~900 | Grammar render + validate + inherit |
| 11 | 2 | 6 | ~1,100 | Primitives: LRU, counter, lock |
| 12 | 2 | 8 | ~1,200 | Primitives: queue, stack, ring, bitset |
| 13 | 2 | 5 | ~1,200 | Session lifecycle + COW |
| 14 | 2 | 2 | ~800 | Snapshot |
| 15 | 3 | 5 | ~900 | Context + scratchpad + token classify + level stats |
| 16 | 3 | 4 | ~1,100 | Command parse + command exec |
| 17 | 3 | 4 | ~1,100 | Auto resolve + universal cycle |
| 18 | 3 | 5 | ~1,100 | LLM model + forward + softmax |
| 19 | 3 | 4 | ~1,000 | LLM attention + KV cache |
| 20 | 3 | 4 | ~800 | LLM generate + sampling |
| 21 | 3 | 5 | ~1,200 | Builtins: dispatch + text + arithmetic |
| 22 | 3 | 4 | ~1,200 | Builtins: collections + sets |
| 23 | 3 | 4 | ~1,200 | Builtins: mappings + conversion |
| 24 | 3 | 4 | ~1,200 | Builtins: linalg + stats |
| 25 | 3 | 6 | ~1,200 | Builtins: graph + integer ops + time |
| 26 | 3 | 6 | ~1,000 | Seed layer |
| 27 | 3 | 2 | ~1,000 | SRE scenario + determinism tests |
| 28 | 4 | 4 | ~1,000 | Runner types + pool + poller |
| 29 | 4 | 5 | ~1,200 | Runner processor + internal + batch |
| 30 | 4 | 4 | ~1,100 | Server types + listener + auth |
| 31 | 4 | 4 | ~1,200 | Server handler + rate limit |
| 32 | 4 | 5 | ~800 | Server health + reaper + shutdown |
| 33 | 4 | 5 | ~1,200 | Protocol HTTP + WebSocket + grammars |
| 34 | 4 | 9 | ~1,200 | Protocol SMTP/MQTT stubs + ops |
| 35 | 4 | 6 | ~1,100 | Config + CLI + build.zig + integration test |
| 36 | 5 | 3 | ~1,000 | GPU device + memory + transfer |
| 37 | 5 | 5 | ~1,200 | GPU MAC + softmax + elementwise kernels |
| 38 | 5 | 6 | ~1,200 | GPU attention + layernorm + sort + prolog kernels |
| 39 | 5 | 4 | ~800 | GPU profiling + benchmarks + determinism |
| 40 | 6 | 12 | ~1,200 | Deploy + distributed + scripts + chaos tests |
| **Total** | | **~200** | **~42,200** | |

Estimated total is higher than the 35,000-line spec because the turn plan includes config files, scripts, build infrastructure, and comprehensive test coverage that the line count estimate treated as approximate. Actual implementation will vary — some modules will be shorter than planned, some longer. The turn plan provides sufficient slack (12 lines average per turn below the 1,200 ceiling) to absorb variance without restructuring.

40 turns. Sequential. No backtracking. Fix forward in test phase.
