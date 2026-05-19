# VDR-LLM-Prolog TensorProlog Runtime Engine

## Server Core, Runner Orchestration, Session Flow, Kernel Inner Loop

---

## 1. The Game Loop

Everything in this system reduces to one loop. Runners run it. Servers run it. The interactive session runs it. The polling cycle runs it. The difference is who triggers the next iteration and what the input source is.

```
// The universal execution cycle.
// Every runner type, every server handler, every interactive session
// is an instantiation of this loop with different input/output bindings.

fn vlp_cycle(
    session: vlp_session_handle,
    input: *vlp_input,
    output: *vlp_output_buffer,
    kb_store: *vlp_kb_store,
    llm_engine: *vlp_llm_engine,
    stream: TensorPrologStream_t,
) -> vlp_cycle_result {

    // ── Phase 0: Pre-LLM Rule Evaluation ──
    // Before the LLM sees anything, fire all matching rules.
    // This is the L3 path. Zero tokens. Pure Prolog over integers.
    var n_auto_fired: i32 = 0;
    var auto_results: [256]vlp_prolog_fired = undefined;
    vlp_prolog_fire_rules(kb_store, session.active_scope_kb_id,
        &auto_results, 256, &n_auto_fired, stream);

    // Commit auto-fired results
    if (n_auto_fired > 0) {
        vlp_prolog_apply_actions(kb_store, &auto_results, n_auto_fired, stream);
        vlp_level_stats_update(session, LEVEL_L3, 0);
        // Check: did any auto-fire resolve the entire input?
        // e.g., triage rule already classified the alert, remediation rule
        // already queued the fix. If so, the LLM may have nothing to do.
        var resolved = vlp_check_auto_resolution(session, input, &auto_results,
            n_auto_fired, kb_store);
        if (resolved.fully_handled) {
            // Format auto-resolution output through grammar
            vlp_grammar_render_from_kb(resolved.grammar, kb_store,
                &resolved.mappings, resolved.n_mappings,
                output.buf, output.capacity, &output.len);
            return vlp_cycle_result{
                .status = VLP_OK,
                .tokens_consumed = 0,
                .commands_executed = resolved.n_actions,
                .level = LEVEL_L3,
            };
        }
    }

    // ── Phase 1: Context Assembly ──
    // Build what the LLM actually sees. This is small and constant-sized.
    var context: vlp_context = undefined;
    vlp_context_build(session, input, kb_store, &context);
    // context contains:
    //   .system_prompt    — from seed KB (~200 tokens, cached)
    //   .scope_reference  — active KB path (~5 tokens)
    //   .scratchpad       — results from auto-fired rules (~0-50 tokens)
    //   .user_input       — current turn input tokens
    // context does NOT contain prior turns, data, history, formatting.
    // Total size: bounded, typically 300-600 tokens regardless of turn number.

    // ── Phase 2: LLM Generation + Command Dispatch ──
    // The inner loop: generate token, classify, dispatch or emit.
    var tokens_generated: i32 = 0;
    var commands_executed: i32 = 0;
    var level: vlp_execution_level = LEVEL_L1;

    // Feed context to LLM
    vlp_llm_forward(session, context.token_ids, context.n_tokens,
        context.logits, stream);
    // KV-cache now primed with context

    while (tokens_generated < session.config.max_tokens_per_turn) {

        var next_token = vlp_llm_generate_token(session,
            &session.config.sampling, stream);
        tokens_generated += 1;

        // Classify token
        var token_class = vlp_token_classify(next_token);

        switch (token_class) {

            .COMMAND_START => {
                // LLM is emitting a command. Switch to constrained generation.
                var command: vlp_command = undefined;
                var cmd_tokens: i32 = 0;
                var parse_status = vlp_llm_generate_command(session,
                    &command, &cmd_tokens, stream);
                tokens_generated += cmd_tokens;

                if (parse_status != VLP_OK) {
                    // Malformed command. Log it. Don't crash.
                    // Write parse error to scratchpad so LLM can self-correct.
                    vlp_scratchpad_write_error(session, parse_status);
                    continue;
                }

                // ── Phase 2a: Access Gate ──
                // Integer check. Happens before any data is touched.
                var access = vlp_access_check(session, command.target_kb_id);
                if (!access) {
                    vlp_audit_write(kb_store, session, AUDIT_ACCESS_DENIED,
                        command.target_kb_id, -1, -1);
                    vlp_scratchpad_write_denied(session, command.target_kb_id);
                    continue;
                }

                // ── Phase 2b: Grant Gate (operational commands only) ──
                if (command.grant_required >= 0) {
                    var grant_result = vlp_grant_check(session, kb_store,
                        command.grant_required, command.target_text,
                        command.target_text_len);
                    if (!grant_result.granted) {
                        vlp_audit_write(kb_store, session, AUDIT_GRANT_CHECK,
                            command.target_kb_id, -1, -1);
                        vlp_scratchpad_write_grant_denied(session,
                            command.grant_required);
                        continue;
                    }
                }

                // ── Phase 2c: Execute ──
                var result = vlp_command_execute_inner(session, &command,
                    kb_store, stream);
                commands_executed += 1;

                // Result to scratchpad for LLM inspection
                vlp_scratchpad_write_result(session, &result);

                // Track level: if LLM invoked a stored rule, this is L2
                if (command.type == CMD_PROLOG_QUERY and result.rule_fired) {
                    level = LEVEL_L2;
                }
            },

            .DIRECT_OUTPUT => {
                // LLM references KB data for output. Data never in token stream.
                var ref: vlp_kb_ref = undefined;
                vlp_parse_kb_reference(session, &ref, stream);

                // Access check on referenced KB
                if (!vlp_access_check(session, ref.kb_id)) {
                    vlp_scratchpad_write_denied(session, ref.kb_id);
                    continue;
                }

                // Load data from KB
                var fact: vlp_fact = undefined;
                vlp_kb_store_fact_read(kb_store, ref.kb_id, ref.slot_id, &fact);

                // Find grammar (walk up KB tree)
                var grammar = vlp_grammar_inherit(kb_store, ref.kb_id, 0);
                if (grammar != null) {
                    vlp_grammar_render_fact(grammar, &fact, kb_store,
                        output.buf + output.len,
                        output.capacity - output.len,
                        &rendered_len);
                    output.len += rendered_len;
                } else {
                    vlp_render_fact_plain(&fact, output.buf + output.len,
                        output.capacity - output.len, &rendered_len);
                    output.len += rendered_len;
                }
            },

            .END_OF_TURN => break,

            .PROSE => {
                // LLM judgment and framing. Pass through to output.
                vlp_output_write_token(output, next_token);
            },
        }
    }

    // ── Phase 3: Post-Cycle ──
    session.current_turn += 1;
    session.llm_tokens_consumed += tokens_generated;
    session.command_tokens_consumed += commands_executed * 8;
    vlp_level_stats_update(session, level, tokens_generated);

    // Auto-snapshot check
    if (session.config.auto_snapshot_interval > 0 and
        session.current_turn % session.config.auto_snapshot_interval == 0)
    {
        vlp_session_snapshot(session);
    }

    // Turn budget check (for recyclable runners)
    var should_recycle = (session.config.max_turns > 0 and
        session.current_turn >= session.config.max_turns);

    return vlp_cycle_result{
        .status = VLP_OK,
        .tokens_consumed = tokens_generated,
        .commands_executed = commands_executed,
        .level = level,
        .should_recycle = should_recycle,
    };
}
```

---

## 2. Runner Engine

### 2.1 Runner Thread Pool

```
struct vlp_runner_pool {
    threads: [MAX_RUNNER_THREADS]vlp_runner_thread,
    n_threads: i32,
    task_queue: vlp_bounded_queue(vlp_runner_task, 1024),
    shutdown_flag: atomic_i32,
    active_runners: atomic_i32,
};

struct vlp_runner_thread {
    thread_handle: os_thread_t,
    id: i32,
    current_runner: ?vlp_runner_handle,
    state: atomic_i32,   // 0=idle, 1=running, 2=stopping
};

struct vlp_runner_task {
    runner: vlp_runner_handle,
    action: vlp_runner_action,  // RUN_CYCLE, RECYCLE, STOP, KILL
};

fn vlp_runner_pool_init(config: *vlp_system_config) -> vlp_status {
    var pool: vlp_runner_pool = undefined;
    pool.n_threads = if (config.runner_thread_pool_size > 0)
        config.runner_thread_pool_size
    else
        @divFloor(os_get_cpu_count(), 2);

    // Cap at configured max
    pool.n_threads = @min(pool.n_threads, config.max_runners);

    // Initialize bounded task queue
    vlp_bounded_queue_init(&pool.task_queue);
    pool.shutdown_flag = 0;
    pool.active_runners = 0;

    // Spawn threads
    for (0..pool.n_threads) |i| {
        pool.threads[i].id = @intCast(i);
        pool.threads[i].state = 0;  // idle
        pool.threads[i].current_runner = null;
        os_thread_create(&pool.threads[i].thread_handle,
            vlp_runner_thread_main, &pool.threads[i]);
    }

    return VLP_OK;
}

fn vlp_runner_thread_main(thread: *vlp_runner_thread) -> void {
    while (true) {
        // Block until task available or shutdown
        var task: vlp_runner_task = undefined;
        var got = pool.task_queue.pop_blocking(&task, 1000); // 1s timeout

        if (pool.shutdown_flag != 0) break;
        if (!got) continue; // timeout, check shutdown flag again

        thread.state = 1; // running
        thread.current_runner = task.runner;

        switch (task.action) {
            .RUN_CYCLE => vlp_runner_execute_cycle(task.runner),
            .RECYCLE   => vlp_runner_execute_recycle(task.runner),
            .STOP      => vlp_runner_execute_stop(task.runner),
            .KILL      => vlp_runner_execute_kill(task.runner),
        }

        thread.current_runner = null;
        thread.state = 0; // idle
    }
}
```

### 2.2 Poller Runner

```
fn vlp_poller_main(runner: *vlp_runner) -> void {
    // The poller runs vlp_cycle on a timer with synthetic input.
    // Input = "check conditions" — or more precisely, no user input at all.
    // The cycle's Phase 0 (pre-LLM rule evaluation) does all the work.
    // If rules handle everything, LLM never activates. Zero tokens.

    var timer = vlp_timer_create(runner.config.interval_ms);

    while (runner.state == RUNNER_RUNNING) {
        vlp_timer_wait(timer);

        // Build synthetic input: "poll cycle N"
        // This is minimal — just enough for the LLM to know it's a poll
        // if Phase 0 doesn't fully resolve.
        var input: vlp_input = undefined;
        vlp_input_synthetic_poll(&input, runner.iterations_completed);

        var output: vlp_output_buffer = undefined;
        vlp_output_buffer_init(&output, runner.output_buf, POLL_OUTPUT_CAPACITY);

        // Create fresh stream for this cycle
        var stream: TensorPrologStream_t = undefined;
        TensorPrologStreamCreateWithSession(&stream, runner.session);

        // Run the universal cycle
        var result = vlp_cycle(
            runner.session, &input, &output,
            runner.kb_store, runner.llm_engine, stream);

        TensorPrologStreamSynchronize(stream);
        TensorPrologStreamDestroy(stream);

        // Update runner stats
        runner.iterations_completed += 1;
        runner.last_iteration_timestamp = vlp_timestamp_now();

        if (result.status != VLP_OK) {
            runner.errors_consecutive += 1;
            runner.errors_total += 1;
            if (runner.errors_consecutive >= runner.config.max_consecutive_errors) {
                runner.state = RUNNER_ERROR;
                vlp_audit_write(runner.kb_store, runner.session,
                    AUDIT_RUNNER_ERROR_THRESHOLD, runner.id, 0, 0);
                break;
            }
        } else {
            runner.errors_consecutive = 0;
        }

        // Recycle check
        if (result.should_recycle) {
            vlp_runner_execute_recycle(runner);
        }

        // Process output: if the cycle produced findings, route them.
        // For pollers, output typically goes to a notification KB
        // that an interactive session or external system reads.
        if (output.len > 0) {
            vlp_route_output(runner, &output);
        }
    }

    vlp_timer_destroy(timer);
}
```

### 2.3 Processor Runner

```
fn vlp_processor_main(runner: *vlp_runner) -> void {
    // Processor maintains a persistent connection to an external source.
    // Each incoming data item triggers a mini-cycle that compacts
    // the data into KB facts. The LLM is available for judgment
    // but most ingestion is rule-driven after the first few items.

    var connection: vlp_connection = undefined;
    var connect_status = vlp_connection_open(
        &connection, &runner.config.source_config);

    if (connect_status != VLP_OK) {
        runner.state = RUNNER_ERROR;
        return;
    }

    var turn_count: i32 = 0;

    while (runner.state == RUNNER_RUNNING) {

        // Receive next data item from source
        var data: vlp_raw_data = undefined;
        var recv_status = vlp_connection_recv(&connection, &data, 5000); // 5s timeout

        if (recv_status == VLP_TIMEOUT) {
            // No data. Check if connection is still alive.
            if (!vlp_connection_alive(&connection)) {
                vlp_processor_reconnect(runner, &connection);
            }
            continue;
        }

        if (recv_status != VLP_OK) {
            runner.errors_consecutive += 1;
            runner.errors_total += 1;
            if (runner.errors_consecutive >= runner.config.max_consecutive_errors) {
                runner.state = RUNNER_ERROR;
                break;
            }
            vlp_processor_reconnect(runner, &connection);
            continue;
        }

        runner.errors_consecutive = 0;

        // Compact incoming data to KB facts.
        // This is the ingest path — most of it becomes rule-driven quickly.
        //
        // First: try rule-based compaction (L3).
        // Rules like "Prometheus metric with label service=X maps to
        // KB root.ops.services.X.metrics.METRIC_NAME" fire automatically.
        var compact_input: vlp_input = undefined;
        vlp_input_from_raw_data(&compact_input, &data);

        var stream: TensorPrologStream_t = undefined;
        TensorPrologStreamCreateWithSession(&stream, runner.session);

        // Attempt pure-Prolog compaction first
        var n_fired: i32 = 0;
        var compact_results: [64]vlp_prolog_fired = undefined;
        vlp_prolog_fire_rules(runner.kb_store, runner.compact_rules_kb_id,
            &compact_results, 64, &n_fired, stream);

        if (n_fired > 0) {
            // Rules handled it. Apply and move on.
            vlp_prolog_apply_actions(runner.kb_store, &compact_results,
                n_fired, stream);
            vlp_level_stats_update(runner.session, LEVEL_L3, 0);
        } else {
            // No rule matched. Fall through to LLM for judgment.
            // The LLM sees the raw data and decides how to organize it.
            // Then ideally writes a rule so this pattern is handled next time.
            var output: vlp_output_buffer = undefined;
            vlp_output_buffer_init(&output, runner.output_buf, PROC_OUTPUT_CAPACITY);

            vlp_cycle(runner.session, &compact_input, &output,
                runner.kb_store, runner.llm_engine, stream);
        }

        TensorPrologStreamSynchronize(stream);
        TensorPrologStreamDestroy(stream);

        turn_count += 1;
        runner.iterations_completed += 1;
        runner.last_iteration_timestamp = vlp_timestamp_now();

        // ── Recycle at turn threshold ──
        // This is the critical freshness mechanism.
        // The session accumulates attention drift in the KV-cache.
        // Kill it. Reclone. Knowledge persists. Drift dies.
        if (turn_count >= runner.config.max_turns_before_recycle) {
            vlp_processor_recycle(runner, &connection);
            turn_count = 0;
        }
    }

    vlp_connection_close(&connection);
}

fn vlp_processor_recycle(runner: *vlp_runner, connection: *vlp_connection) -> void {
    // The recycle dance:
    // 1. Save connection state (socket descriptors, protocol state, buffers).
    // 2. Snapshot session (KB facts, rules, live state — all exact integers).
    // 3. Kill session (drift dies).
    // 4. Clone from snapshot (fresh session, identical knowledge).
    // 5. Restore connection from saved state.
    // The data stream sees zero interruption. The LLM processing it is always fresh.

    runner.state = RUNNER_RECYCLING;

    // Save connection state
    var conn_state: vlp_connection_state = undefined;
    vlp_connection_save_state(connection, &conn_state);

    // Snapshot the session — captures all accumulated knowledge
    var snapshot: vlp_snapshot_handle = undefined;
    vlp_session_snapshot(runner.session, &snapshot);

    // Kill the old session — live state gone, attention cache gone, drift gone
    vlp_session_kill(runner.session);

    // Create fresh session from snapshot — bit-identical knowledge, fresh LLM
    var new_session: vlp_session_handle = undefined;
    vlp_session_create(&new_session, &runner.session_config);
    vlp_session_restore(new_session, snapshot);

    // The new session has:
    //   - Every KB fact the old session had (exact, integer storage)
    //   - Every Prolog rule (exact, fired on same patterns same way)
    //   - Every grammar (exact, renders identically)
    //   - Fresh live state (counters at initial, caches empty, no drift)
    //   - Fresh KV-cache (no accumulated attention error)

    runner.session = new_session;
    runner.recycle_count += 1;
    runner.last_recycle_timestamp = vlp_timestamp_now();

    // Restore connection
    vlp_connection_restore_state(connection, &conn_state);

    runner.state = RUNNER_RUNNING;

    vlp_audit_write(runner.kb_store, runner.session,
        AUDIT_RUNNER_RECYCLE, runner.id, runner.recycle_count, 0);
}

fn vlp_processor_reconnect(runner: *vlp_runner, connection: *vlp_connection) -> void {
    // Exponential backoff: 1s, 2s, 4s, 8s, 16s, 32s, 60s cap
    var backoff_ms: i32 = 1000;
    var max_attempts: i32 = 10;

    for (0..max_attempts) |attempt| {
        vlp_sleep_ms(backoff_ms);

        var status = vlp_connection_open(connection, &runner.config.source_config);
        if (status == VLP_OK) {
            runner.errors_consecutive = 0;
            vlp_audit_write(runner.kb_store, runner.session,
                AUDIT_RUNNER_RECONNECT, runner.id, @intCast(attempt), 0);
            return;
        }

        backoff_ms = @min(backoff_ms * 2, 60000);
    }

    // Failed to reconnect after max attempts
    runner.state = RUNNER_ERROR;
    vlp_audit_write(runner.kb_store, runner.session,
        AUDIT_RUNNER_RECONNECT_FAILED, runner.id, max_attempts, 0);
}
```

### 2.4 Internal Runner

```
fn vlp_internal_main(runner: *vlp_runner) -> void {
    // Internal runner computes derived facts from existing facts.
    // No external connections. No user input. Pure computation.
    // Rolling averages, trend detection, coverage gaps, metric aggregation.

    var timer = vlp_timer_create(runner.config.interval_ms);

    while (runner.state == RUNNER_RUNNING) {
        vlp_timer_wait(timer);

        var stream: TensorPrologStream_t = undefined;
        TensorPrologStreamCreateWithSession(&stream, runner.session);

        // Call the configured compute function.
        // Typical implementations:

        // 1. Rolling average update
        //    Load last N metric values from ring buffer.
        //    Compute exact mean as VDR fraction.
        //    Assert as derived fact with confidence = VDR_COMPUTATION (1/1).
        //
        // 2. Trend detection
        //    Compare current rolling average to previous.
        //    Exact integer comparison: increasing, decreasing, or stable.
        //    Assert trend fact.
        //
        // 3. Coverage gap analysis
        //    Query all service KBs.
        //    Check which have active triage rules.
        //    Compute coverage_ratio = covered_services / total_services.
        //    Exact fraction.
        //
        // All of this is KB queries + exact VDR arithmetic + KB assertions.
        // Zero LLM tokens unless a genuinely novel pattern appears.

        var status = runner.config.compute_fn(runner.session, runner.kb_store, stream);

        TensorPrologStreamSynchronize(stream);
        TensorPrologStreamDestroy(stream);

        runner.iterations_completed += 1;
        runner.last_iteration_timestamp = vlp_timestamp_now();

        if (status != VLP_OK) {
            runner.errors_consecutive += 1;
            runner.errors_total += 1;
            if (runner.errors_consecutive >= runner.config.max_consecutive_errors) {
                runner.state = RUNNER_ERROR;
                break;
            }
        } else {
            runner.errors_consecutive = 0;
        }
    }

    vlp_timer_destroy(timer);
}
```

### 2.5 Batch Runner

```
fn vlp_batch_main(runner: *vlp_runner) -> void {
    // Batch runner pulls tasks from a KB queue and processes each
    // in an isolated clone. Clone-per-task. Results merge back.

    var active_clones: i32 = 0;
    var clone_handles: [MAX_BATCH_CONCURRENT]vlp_batch_clone = undefined;

    while (runner.state == RUNNER_RUNNING) {

        // Reap completed clones
        for (0..active_clones) |i| {
            if (clone_handles[i].completed) {
                // Merge results back to parent session
                vlp_session_merge(runner.session, clone_handles[i].session,
                    VLP_MERGE_THEIRS); // child's results win

                // Kill clone — drift dies, results preserved in parent
                vlp_session_kill(clone_handles[i].session);

                // Compact the array
                clone_handles[i] = clone_handles[active_clones - 1];
                active_clones -= 1;
            }
        }

        // Spawn new clones up to max_concurrent
        while (active_clones < runner.config.max_concurrent) {
            // Pop task from queue
            var task: vlp_fact = undefined;
            var popped: bool = false;
            TensorPrologQueuePop(runner.kb_store, runner.config.task_queue_kb_id,
                runner.config.task_queue_name, &task, &popped);

            if (!popped) break; // queue empty

            // Clone session for isolation
            var clone_session: vlp_session_handle = undefined;
            vlp_session_clone(runner.session, &clone_session,
                &vlp_clone_config{
                    .fresh_live = true,    // clean working state
                    .inherit_rules = true, // inherit parent's rules
                    .max_turns = 100,      // bounded
                });

            // Launch clone processing on a thread
            clone_handles[active_clones] = vlp_batch_clone{
                .session = clone_session,
                .task = task,
                .completed = false,
            };

            // Submit to thread pool
            vlp_runner_pool_submit(&vlp_runner_task{
                .runner = &clone_handles[active_clones],
                .action = .RUN_BATCH_TASK,
            });

            active_clones += 1;
        }

        // Brief sleep if nothing to do
        if (active_clones == 0) {
            vlp_sleep_ms(100);
        } else {
            vlp_sleep_ms(10);
        }

        runner.iterations_completed += 1;
        runner.last_iteration_timestamp = vlp_timestamp_now();
    }

    // Cleanup: kill all active clones
    for (0..active_clones) |i| {
        vlp_session_kill(clone_handles[i].session);
    }
}

fn vlp_batch_task_execute(clone: *vlp_batch_clone) -> void {
    // Process one task in isolated clone session
    var input: vlp_input = undefined;
    vlp_input_from_task(&input, &clone.task);

    var output: vlp_output_buffer = undefined;
    vlp_output_buffer_init(&output, clone.output_buf, BATCH_OUTPUT_CAPACITY);

    var stream: TensorPrologStream_t = undefined;
    TensorPrologStreamCreateWithSession(&stream, clone.session);

    // Run the universal cycle — same code path as everything else
    vlp_cycle(clone.session, &input, &output,
        clone.kb_store, clone.llm_engine, stream);

    TensorPrologStreamSynchronize(stream);
    TensorPrologStreamDestroy(stream);

    clone.completed = true;
}
```

---

## 3. Server Engine

### 3.1 Listener Architecture

```
struct vlp_server {
    // Listener state
    listen_socket: os_socket_t,
    listen_port: i32,
    listen_address: [64]u8,

    // Protocol configuration
    protocol: vlp_protocol_type,  // HTTP, SMTP, MQTT, RAW_TCP, WEBSOCKET
    protocol_grammar_kb_id: i32,  // KB containing protocol grammar templates
    max_concurrent_connections: i32,

    // Session template — the snapshot cloned for each connection
    template_snapshot: vlp_snapshot_handle,
    template_session_config: vlp_session_config,

    // Credential configuration
    auth_kb_id: i32,              // KB containing valid credentials
    credential_ttl_seconds: i32,  // how long a session credential lives
    max_session_turns: i32,       // max turns before force-recycle

    // Connection pool
    connections: [MAX_CONNECTIONS]vlp_server_connection,
    n_active: atomic_i32,

    // Accept thread
    accept_thread: os_thread_t,
    shutdown_flag: atomic_i32,

    // Metrics (all exact integers)
    total_connections_accepted: atomic_i64,
    total_connections_rejected: atomic_i64,
    total_requests_served: atomic_i64,
    active_sessions: atomic_i32,
};

struct vlp_server_connection {
    socket: os_socket_t,
    session: vlp_session_handle,
    stream: TensorPrologStream_t,
    credential: vlp_server_credential,
    state: vlp_connection_state_enum,  // HANDSHAKE, ACTIVE, DRAINING, CLOSED
    created_at: i32,
    last_active: i32,
    requests_served: i32,
    bytes_received: i64,
    bytes_sent: i64,
};

struct vlp_server_credential {
    user_id: i32,
    visibility_level: i8,
    grants: [16]vlp_grant,          // pre-resolved grants for this session
    n_grants: i32,
    issued_at: i32,                 // timestamp
    expires_at: i32,                // timestamp
    valid: bool,                    // false after expiry or revocation
};
```

### 3.2 Server Initialization and Accept Loop

```
fn vlp_server_init(config: *vlp_server_config) -> *vlp_server {
    var server: vlp_server = undefined;

    server.listen_port = config.port;
    @memcpy(&server.listen_address, config.address);
    server.protocol = config.protocol;
    server.max_concurrent_connections = config.max_connections;
    server.credential_ttl_seconds = config.credential_ttl;
    server.max_session_turns = config.max_session_turns;

    // Load protocol grammar from KB
    // HTTP: status lines, headers, content-type, chunked encoding markers
    // SMTP: EHLO responses, mail headers, envelope delimiters
    // MQTT: fixed headers, variable headers, property fields
    // Every structural byte comes from grammar. LLM only generates content.
    server.protocol_grammar_kb_id = config.protocol_grammar_kb_id;

    // Load or create the template session snapshot.
    // This is the factory. Every incoming connection clones from this.
    if (config.template_snapshot_path[0] != 0) {
        server.template_snapshot = vlp_snapshot_load(config.template_snapshot_path);
    } else {
        // Create a template session with configured KB tree
        var template_session: vlp_session_handle = undefined;
        vlp_session_create(&template_session, &config.template_session_config);
        // Load domain-specific KBs, rules, grammars into template
        vlp_load_domain_kb(template_session, config.domain_kb_path);
        // Snapshot it
        vlp_session_snapshot(template_session, &server.template_snapshot);
        // Kill the template session — the snapshot is the factory
        vlp_session_kill(template_session);
    }

    server.auth_kb_id = config.auth_kb_id;
    server.n_active = 0;
    server.shutdown_flag = 0;

    // Bind and listen
    server.listen_socket = os_socket_create(AF_INET, SOCK_STREAM, 0);
    os_socket_bind(server.listen_socket, server.listen_address, server.listen_port);
    os_socket_listen(server.listen_socket, config.backlog);

    // Start accept thread
    os_thread_create(&server.accept_thread, vlp_server_accept_loop, &server);

    return &server;
}

fn vlp_server_accept_loop(server: *vlp_server) -> void {

    while (server.shutdown_flag == 0) {

        // Accept incoming connection
        var client_socket: os_socket_t = undefined;
        var client_addr: os_sockaddr = undefined;
        var accept_status = os_socket_accept(server.listen_socket,
            &client_socket, &client_addr);

        if (accept_status != 0) continue;

        // Capacity check
        if (server.n_active >= server.max_concurrent_connections) {
            // Reject with protocol-appropriate response
            vlp_server_reject_overloaded(server, client_socket);
            os_socket_close(client_socket);
            server.total_connections_rejected += 1;
            continue;
        }

        // Find free connection slot
        var slot: ?*vlp_server_connection = null;
        for (&server.connections) |*conn| {
            if (conn.state == .CLOSED) {
                slot = conn;
                break;
            }
        }

        if (slot == null) {
            vlp_server_reject_overloaded(server, client_socket);
            os_socket_close(client_socket);
            server.total_connections_rejected += 1;
            continue;
        }

        // Initialize connection
        slot.socket = client_socket;
        slot.state = .HANDSHAKE;
        slot.created_at = vlp_timestamp_now();
        slot.last_active = slot.created_at;
        slot.requests_served = 0;
        slot.bytes_received = 0;
        slot.bytes_sent = 0;

        _ = @atomicRmw(i32, &server.n_active, .Add, 1, .SeqCst);
        server.total_connections_accepted += 1;

        // Submit to thread pool for handshake + session creation
        vlp_runner_pool_submit(&vlp_runner_task{
            .runner = slot,
            .action = .HANDLE_CONNECTION,
        });
    }
}
```

### 3.3 Connection Handler — Clone, Authenticate, Serve

```
fn vlp_server_handle_connection(server: *vlp_server, conn: *vlp_server_connection) -> void {

    // ── Step 1: Protocol Handshake ──
    // Read initial bytes. Determine protocol variant.
    // For HTTP: read request line + headers.
    // For SMTP: send greeting.
    // For MQTT: read CONNECT packet.
    // For WebSocket: HTTP upgrade handshake.
    // All structural bytes parsed by compiled parser, not LLM.

    var handshake_result = vlp_protocol_handshake(
        server.protocol, conn.socket, &conn.handshake_data);

    if (handshake_result != VLP_OK) {
        vlp_server_close_connection(server, conn, .HANDSHAKE_FAILED);
        return;
    }

    conn.state = .AUTHENTICATING;

    // ── Step 2: Authenticate and Issue Credential ──
    // Extract credentials from handshake data.
    // HTTP: Authorization header (Bearer token, Basic auth, API key).
    // SMTP: AUTH command.
    // MQTT: username/password in CONNECT.
    // All parsed by protocol parser. Token/key is bytes, not LLM judgment.

    var auth_data: vlp_auth_data = undefined;
    vlp_protocol_extract_auth(server.protocol, &conn.handshake_data, &auth_data);

    // Validate against auth KB.
    // Auth KB contains: user_id → hashed_token, grants, visibility_level.
    // Lookup is KB fact query by token hash. O(1) integer index.
    var credential: vlp_server_credential = undefined;
    var auth_status = vlp_server_authenticate(server, &auth_data, &credential);

    if (auth_status != VLP_OK) {
        vlp_protocol_send_auth_failure(server.protocol, conn.socket);
        vlp_server_close_connection(server, conn, .AUTH_FAILED);
        vlp_audit_write(server.kb_store, null, AUDIT_ACCESS_DENIED,
            server.auth_kb_id, 0, 0);
        return;
    }

    // Set credential expiry
    credential.issued_at = vlp_timestamp_now();
    credential.expires_at = credential.issued_at + server.credential_ttl_seconds;
    credential.valid = true;
    conn.credential = credential;

    // ── Step 3: Clone Session from Template ──
    // The template snapshot is the factory.
    // Every connection gets a fresh clone. Bit-identical starting state.
    // But each clone has: unique user_id, unique grants, unique visibility.

    var session_config = server.template_session_config;
    session_config.user_id = credential.user_id;
    session_config.visibility_level = credential.visibility_level;
    session_config.max_turns = server.max_session_turns;

    var session: vlp_session_handle = undefined;
    vlp_session_create(&session, &session_config);
    vlp_session_restore(session, server.template_snapshot);

    // Inject credential grants into session's grant store
    for (0..credential.n_grants) |i| {
        vlp_grant_inject(session, &credential.grants[i]);
    }

    // Create session-bound stream
    var stream: TensorPrologStream_t = undefined;
    TensorPrologStreamCreateWithSession(&stream, session);

    conn.session = session;
    conn.stream = stream;
    conn.state = .ACTIVE;

    vlp_audit_write(server.kb_store, session, AUDIT_SESSION_CREATE,
        session.kb_root_id, credential.user_id, 0);

    // ── Step 4: Request Loop ──
    // For stateless protocols (HTTP): one request per iteration.
    // For stateful protocols (SMTP, MQTT, WebSocket): continuous.
    // Both run the same universal cycle.

    while (conn.state == .ACTIVE) {

        // Check credential expiry — integer comparison
        var now = vlp_timestamp_now();
        if (now >= conn.credential.expires_at) {
            conn.credential.valid = false;
            vlp_protocol_send_credential_expired(server.protocol, conn.socket);
            conn.state = .DRAINING;
            break;
        }

        // Read request from socket
        var request: vlp_protocol_request = undefined;
        var read_status = vlp_protocol_read_request(
            server.protocol, conn.socket, &request, 30000); // 30s timeout

        if (read_status == VLP_TIMEOUT) {
            // Idle timeout — check if keepalive or close
            if (server.protocol == .HTTP) {
                conn.state = .DRAINING;
                break;
            }
            continue; // stateful protocols: keep waiting
        }

        if (read_status == VLP_CONNECTION_CLOSED) {
            conn.state = .DRAINING;
            break;
        }

        if (read_status != VLP_OK) {
            // Protocol error — send error response and close
            vlp_protocol_send_error(server.protocol, conn.socket, read_status);
            conn.state = .DRAINING;
            break;
        }

        conn.last_active = now;
        conn.bytes_received += request.raw_bytes_len;

        // ── Step 5: Request → Cycle Input ──
        // Transform protocol request into vlp_input for the universal cycle.
        // Protocol-specific parsing extracts the meaningful content.
        // HTTP: body, query params, path → input tokens.
        // SMTP: mail data → input tokens.
        // MQTT: payload → input tokens.
        var input: vlp_input = undefined;
        vlp_protocol_to_input(server.protocol, &request, &input);

        // ── Step 6: Run the Universal Cycle ──
        var output: vlp_output_buffer = undefined;
        vlp_output_buffer_init(&output, conn.output_buf, CONN_OUTPUT_CAPACITY);

        var result = vlp_cycle(
            conn.session, &input, &output,
            server.kb_store, server.llm_engine, conn.stream);

        // ── Step 7: Cycle Output → Protocol Response ──
        // Transform cycle output into protocol response.
        // Grammar handles all structural bytes.
        // HTTP: status line + headers from grammar, body from output.
        // SMTP: response codes from grammar, content from output.
        // MQTT: packet structure from grammar, payload from output.

        var response: vlp_protocol_response = undefined;
        vlp_protocol_from_output(server.protocol, &output, &request,
            server.protocol_grammar_kb_id, server.kb_store, &response);

        var send_status = vlp_protocol_send_response(
            server.protocol, conn.socket, &response);

        if (send_status != VLP_OK) {
            conn.state = .DRAINING;
            break;
        }

        conn.bytes_sent += response.raw_bytes_len;
        conn.requests_served += 1;
        server.total_requests_served += 1;

        // ── Step 8: Per-Request Lifecycle Decisions ──

        // Recycle check (turn budget)
        if (result.should_recycle) {
            // Snapshot session, kill, reclone from template.
            // But preserve accumulated facts from this connection.
            var conn_snapshot: vlp_snapshot_handle = undefined;
            vlp_session_snapshot(conn.session, &conn_snapshot);
            vlp_session_kill(conn.session);

            var new_session: vlp_session_handle = undefined;
            vlp_session_create(&new_session, &session_config);
            vlp_session_restore(new_session, conn_snapshot);

            TensorPrologStreamDestroy(conn.stream);
            TensorPrologStreamCreateWithSession(&conn.stream, new_session);
            conn.session = new_session;
        }

        // HTTP stateless: close after response (unless keepalive)
        if (server.protocol == .HTTP and !request.keepalive) {
            conn.state = .DRAINING;
            break;
        }
    }

    // ── Cleanup ──
    vlp_server_close_connection(server, conn, .NORMAL);
}

fn vlp_server_close_connection(server: *vlp_server, conn: *vlp_server_connection, reason: vlp_close_reason) -> void {

    // Protocol-level close
    vlp_protocol_send_close(server.protocol, conn.socket);
    os_socket_close(conn.socket);

    // Session cleanup
    if (conn.session.id >= 0) {
        // Option A: stateless — kill session, discard everything
        // Option B: persistent — snapshot session for future restoration
        if (server.config.persistent_sessions) {
            vlp_session_snapshot(conn.session, &snapshot);
            vlp_snapshot_save(&snapshot,
                vlp_session_snapshot_path(conn.credential.user_id));
        }
        vlp_session_kill(conn.session);
    }

    if (conn.stream.id >= 0) {
        TensorPrologStreamDestroy(conn.stream);
    }

    // Log
    vlp_audit_write(server.kb_store, null, AUDIT_SESSION_DESTROY,
        conn.credential.user_id, conn.requests_served,
        @intCast(reason));

    conn.state = .CLOSED;
    _ = @atomicRmw(i32, &server.n_active, .Sub, 1, .SeqCst);
}
```

### 3.4 Authentication

```
fn vlp_server_authenticate(server: *vlp_server, auth_data: *vlp_auth_data, credential: *vlp_server_credential) -> vlp_status {

    // Hash the provided token/key — deterministic integer hash
    var token_hash: i32 = vlp_hash_credential(auth_data.token, auth_data.token_len);

    // Look up in auth KB by hash
    // Auth KB structure:
    //   slot 0: token_hash → user_id mapping
    //   slot 1: user_id → visibility_level
    //   slot 2: user_id → grant_list reference
    //   slot 3: user_id → account_status (active/suspended/revoked)

    var user_fact: vlp_fact = undefined;
    var found: bool = false;

    // Scan auth KB for matching token hash
    // In production: hash index for O(1). Here: linear scan for clarity.
    vlp_kb_fact_search_by_value(server.kb_store, server.auth_kb_id,
        TAG_INTEGER, token_hash, &user_fact, &found);

    if (!found) return VLP_ERR_AUTH_INVALID_TOKEN;

    var user_id: i32 = user_fact.provenance.source_slot_id; // user_id stored in provenance

    // Check account status
    var status_fact: vlp_fact = undefined;
    vlp_kb_store_fact_read(server.kb_store, server.auth_kb_id,
        user_id * 4 + 3, &status_fact); // slot layout: user_id*4 + offset
    if (status_fact.value.v != 1) { // 1 = active
        return VLP_ERR_AUTH_ACCOUNT_SUSPENDED;
    }

    // Load visibility level
    var vis_fact: vlp_fact = undefined;
    vlp_kb_store_fact_read(server.kb_store, server.auth_kb_id,
        user_id * 4 + 1, &vis_fact);
    credential.visibility_level = @intCast(vis_fact.value.v);

    // Load grants
    var grant_ref_fact: vlp_fact = undefined;
    vlp_kb_store_fact_read(server.kb_store, server.auth_kb_id,
        user_id * 4 + 2, &grant_ref_fact);
    var grant_kb_id: i32 = grant_ref_fact.value.v;

    // Read grants from grant KB
    credential.n_grants = 0;
    var grant_facts: [16]vlp_fact = undefined;
    var n_found: i32 = 0;
    vlp_kb_fact_search(server.kb_store, grant_kb_id, TAG_VALUE,
        &grant_facts, 16, &n_found);

    for (0..@intCast(n_found)) |i| {
        vlp_grant_from_fact(&grant_facts[i], &credential.grants[credential.n_grants]);
        credential.n_grants += 1;
    }

    credential.user_id = user_id;
    credential.valid = true;

    return VLP_OK;
}
```

### 3.5 Protocol Grammars

```
// Protocol grammars live in a KB. Loaded at server init.
// Every protocol has structural bytes that never need LLM judgment.

fn vlp_protocol_grammar_init(server: *vlp_server) -> vlp_status {
    // HTTP grammars
    if (server.protocol == .HTTP) {
        // Response line grammar: "HTTP/1.1 {status_code:integer} {reason:text}\r\n"
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_STATUS_LINE,
            "HTTP/1.1 {status_code:integer} {reason:text}\r\n");

        // Header grammar: "{name:text}: {value:text}\r\n"
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_HEADER,
            "{name:text}: {value:text}\r\n");

        // Content-Type header: "Content-Type: {mime:enum(application/json|text/plain|text/html)}\r\n"
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_CONTENT_TYPE,
            "Content-Type: {mime:enum(application/json|text/plain|text/html)}\r\n");

        // JSON response body grammar: '{"result": {data:text}, "confidence": {confidence:vdr_value}}'
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_JSON_BODY,
            "{{\"result\": {data:text}, \"confidence\": {confidence:vdr_value}}}");

        // Every { } in the HTTP response comes from these grammars.
        // The LLM never generates "HTTP/1.1 " or "Content-Type:" or any brace.
        // The grammar generates them. 100% correct. Zero forward passes.
    }

    if (server.protocol == .SMTP) {
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_SMTP_GREETING,
            "220 {hostname:text} ESMTP VDR-LLM-Prolog\r\n");

        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_SMTP_OK,
            "250 {message:text}\r\n");

        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_SMTP_HEADER,
            "{name:text}: {value:text}\r\n");
    }

    if (server.protocol == .MQTT) {
        // MQTT packet grammars encode fixed header, variable header, payload structure.
        // Binary protocol — grammar produces exact byte sequences.
        vlp_grammar_create_and_store(server.kb_store,
            server.protocol_grammar_kb_id, GRAMMAR_SLOT_MQTT_CONNACK,
            // Binary template: connect ack flags + return code
            "\x20\x02{session_present:integer}{return_code:integer}");
    }

    return VLP_OK;
}

fn vlp_protocol_from_output(
    protocol: vlp_protocol_type,
    output: *vlp_output_buffer,
    request: *vlp_protocol_request,
    grammar_kb_id: i32,
    kb_store: *vlp_kb_store,
    response: *vlp_protocol_response,
) -> vlp_status {

    switch (protocol) {
        .HTTP => {
            // Assemble HTTP response from grammar-rendered parts

            var status_grammar: vlp_grammar = undefined;
            vlp_grammar_load_from_kb(kb_store, grammar_kb_id,
                GRAMMAR_SLOT_STATUS_LINE, &status_grammar);

            var content_type_grammar: vlp_grammar = undefined;
            vlp_grammar_load_from_kb(kb_store, grammar_kb_id,
                GRAMMAR_SLOT_CONTENT_TYPE, &content_type_grammar);

            // Render status line
            var status_fills = [_]vlp_grammar_fill{
                .{ .slot_index = 0, .int_value = 200 },
                .{ .slot_index = 1, .text = "OK", .text_len = 2 },
            };
            vlp_grammar_render(&status_grammar, &status_fills, 2,
                response.buf, response.capacity, &response.len);

            // Render content-type header
            var ct_fills = [_]vlp_grammar_fill{
                .{ .slot_index = 0, .enum_index = 0 }, // application/json
            };
            vlp_grammar_render(&content_type_grammar, &ct_fills, 1,
                response.buf + response.len,
                response.capacity - response.len, &rendered);
            response.len += rendered;

            // Content-Length header (computed from output length)
            var cl_header = "Content-Length: ";
            @memcpy(response.buf + response.len, cl_header);
            response.len += cl_header.len;
            response.len += vlp_i32_to_ascii(
                @intCast(output.len),
                response.buf + response.len);
            @memcpy(response.buf + response.len, "\r\n\r\n");
            response.len += 4;

            // Body: the cycle output
            @memcpy(response.buf + response.len, output.buf[0..output.len]);
            response.len += output.len;

            response.raw_bytes_len = response.len;
        },

        .SMTP => {
            // SMTP response is simpler: status code + message
            var ok_grammar: vlp_grammar = undefined;
            vlp_grammar_load_from_kb(kb_store, grammar_kb_id,
                GRAMMAR_SLOT_SMTP_OK, &ok_grammar);

            var fills = [_]vlp_grammar_fill{
                .{ .slot_index = 0, .text = output.buf, .text_len = output.len },
            };
            vlp_grammar_render(&ok_grammar, &fills, 1,
                response.buf, response.capacity, &response.len);
            response.raw_bytes_len = response.len;
        },

        .MQTT => {
            // MQTT: binary packet assembly from grammar
            // Publish packet: fixed header + topic + payload
            vlp_mqtt_assemble_publish(kb_store, grammar_kb_id,
                request.mqtt_topic, output, response);
        },

        .WEBSOCKET => {
            // WebSocket: frame header (grammar) + payload (output)
            vlp_websocket_frame(output.buf, output.len, response);
        },

        .RAW_TCP => {
            // Raw: output bytes go directly to socket
            @memcpy(response.buf, output.buf[0..output.len]);
            response.len = output.len;
            response.raw_bytes_len = response.len;
        },
    }

    return VLP_OK;
}
```

---

## 4. Credential Lifecycle

```
struct vlp_credential_manager {
    // Credentials are exact integers with exact expiry timestamps.
    // No "approximately expired" — expired or not, integer comparison.

    auth_kb_id: i32,
    active_credentials: vlp_bounded_queue(vlp_active_credential, 10000),
    cleanup_interval_ms: i32,
};

struct vlp_active_credential {
    session_id: i32,
    user_id: i32,
    issued_at: i32,
    expires_at: i32,
    connection_id: i32,
};

fn vlp_credential_issue(
    manager: *vlp_credential_manager,
    user_id: i32,
    ttl_seconds: i32,
    grants: []vlp_grant,
) -> vlp_server_credential {

    var now = vlp_timestamp_now();

    var credential = vlp_server_credential{
        .user_id = user_id,
        .issued_at = now,
        .expires_at = now + ttl_seconds,
        .valid = true,
        .n_grants = @intCast(grants.len),
    };

    // Copy grants
    for (grants, 0..) |grant, i| {
        credential.grants[i] = grant;
        // Each grant has its own expiry and use count.
        // If the grant expires before the credential, the grant
        // stops working but the credential stays valid for other grants.
        // If the credential expires, ALL grants stop working regardless
        // of their individual expiry.
    }

    // Track active credential
    manager.active_credentials.push(&vlp_active_credential{
        .session_id = -1, // assigned when session created
        .user_id = user_id,
        .issued_at = now,
        .expires_at = credential.expires_at,
        .connection_id = -1,
    });

    vlp_audit_write_credential_issued(manager, user_id, now, credential.expires_at);

    return credential;
}

fn vlp_credential_check(credential: *vlp_server_credential) -> bool {
    // The check. Two integer comparisons.
    if (!credential.valid) return false;
    var now = vlp_timestamp_now();
    if (now >= credential.expires_at) {
        credential.valid = false;
        return false;
    }
    return true;
}

fn vlp_credential_revoke(credential: *vlp_server_credential) -> void {
    credential.valid = false;
    // All grants in this credential become immediately inoperative.
    // No gradual expiry. No grace period. The integer flips to false.
    // Next grant check reads false. Done.
}

fn vlp_credential_cleanup_runner(manager: *vlp_credential_manager) -> void {
    // Runs as internal runner. Periodically scans active credentials.
    // Removes expired ones from the tracking queue.
    // Reports: n_active, n_expired_this_cycle, oldest_active.

    var now = vlp_timestamp_now();
    var expired_count: i32 = 0;

    // Scan the queue — bounded, so this is bounded work
    var size = manager.active_credentials.size();
    for (0..size) |_| {
        var cred: vlp_active_credential = undefined;
        var popped: bool = false;
        manager.active_credentials.pop(&cred, &popped);
        if (!popped) break;

        if (now < cred.expires_at) {
            // Still valid — re-enqueue
            manager.active_credentials.push(&cred);
        } else {
            // Expired — don't re-enqueue
            expired_count += 1;
        }
    }

    // Log exact counts
    vlp_audit_write_credential_cleanup(manager, expired_count, size - expired_count);
}
```

---

## 5. Context Builder

What the LLM actually sees each cycle.

```
fn vlp_context_build(
    session: vlp_session_handle,
    input: *vlp_input,
    kb_store: *vlp_kb_store,
    context: *vlp_context,
) -> vlp_status {

    var offset: i32 = 0;

    // ── Segment 1: System Prompt ──
    // Loaded from seed KB. Cached after first load.
    // Tells the LLM its role, available commands, active scope.
    // ~200 tokens. Same every cycle (unless scope changes).
    if (session.cached_system_prompt_valid) {
        @memcpy(context.token_ids[offset..], session.cached_system_prompt);
        offset += session.cached_system_prompt_len;
    } else {
        // Load from seed KB
        var prompt_fact: vlp_fact = undefined;
        vlp_kb_store_fact_read(kb_store, session.seed_kb_id,
            SLOT_SYSTEM_PROMPT, &prompt_fact);
        var prompt_tokens = vlp_tokenize_fact(&prompt_fact);
        @memcpy(context.token_ids[offset..], prompt_tokens);
        offset += prompt_tokens.len;
        // Cache it
        @memcpy(session.cached_system_prompt, prompt_tokens);
        session.cached_system_prompt_len = prompt_tokens.len;
        session.cached_system_prompt_valid = true;
    }

    // ── Segment 2: Scope Reference ──
    // The active KB path. Tells the LLM where it is in the KB tree.
    // ~5 tokens. e.g., "SCOPE: root.ops.incidents.inc_047"
    var scope_path: [256]u8 = undefined;
    var scope_len: i32 = 0;
    vlp_kb_get_path(kb_store, session.active_scope_kb_id, &scope_path, &scope_len);
    var scope_tokens = vlp_tokenize_text("SCOPE: ");
    @memcpy(context.token_ids[offset..], scope_tokens);
    offset += scope_tokens.len;
    var path_tokens = vlp_tokenize_bytes(&scope_path, scope_len);
    @memcpy(context.token_ids[offset..], path_tokens);
    offset += path_tokens.len;

    // ── Segment 3: Scratchpad ──
    // Results from auto-fired rules (Phase 0) and any prior commands
    // in this cycle. Gives the LLM immediate context about what just happened.
    // ~0-50 tokens.
    if (session.scratchpad_len > 0) {
        var scratch_tokens = vlp_tokenize_bytes(
            session.scratchpad, session.scratchpad_len);
        @memcpy(context.token_ids[offset..], scratch_tokens);
        offset += scratch_tokens.len;
    }

    // ── Segment 4: Available Summaries ──
    // If KB has summary facts, include them.
    // These are LLM-generated summaries of accumulated state,
    // stored as KB facts. Not re-read from conversation history.
    // ~0-100 tokens.
    var summary_fact: vlp_fact = undefined;
    var has_summary: bool = false;
    vlp_kb_store_fact_read(kb_store, session.active_scope_kb_id,
        SLOT_TURN_SUMMARY, &summary_fact);
    if (summary_fact.tag != TAG_EMPTY) {
        var summary_tokens = vlp_tokenize_fact(&summary_fact);
        @memcpy(context.token_ids[offset..], summary_tokens);
        offset += summary_tokens.len;
    }

    // ── Segment 5: User Input ──
    // The actual input for this cycle.
    @memcpy(context.token_ids[offset..], input.token_ids[0..input.n_tokens]);
    offset += input.n_tokens;

    context.n_tokens = offset;

    // Total context: ~300-600 tokens. Bounded. Constant regardless of turn number.
    // Turn 1: ~350 tokens.
    // Turn 1000: ~350 tokens.
    // The LLM's attention window is never growing.
    // The data is in KBs. The history is in rules. The formatting is in grammars.
    // The context contains only: who am I, where am I, what just happened, what's asked.

    return VLP_OK;
}
```

---

## 6. Auto-Resolution Check

The pre-LLM decision that determines whether the LLM is needed at all.

```
fn vlp_check_auto_resolution(
    session: vlp_session_handle,
    input: *vlp_input,
    auto_results: []vlp_prolog_fired,
    n_fired: i32,
    kb_store: *vlp_kb_store,
) -> vlp_auto_resolution {

    var resolution = vlp_auto_resolution{
        .fully_handled = false,
        .grammar = null,
        .mappings = undefined,
        .n_mappings = 0,
        .n_actions = 0,
    };

    // Check: did any fired rule produce a complete response?
    // A complete response has:
    //   1. An action that asserts a finding or result fact.
    //   2. A grammar reference for rendering.
    //   3. Confidence above auto-response threshold.

    for (auto_results[0..@intCast(n_fired)]) |*fired| {

        // Does this rule's output have a grammar attached?
        var grammar_ref: i32 = -1;
        for (fired.actions[0..fired.n_actions]) |action| {
            if (action.type == ACTION_ASSERT and
                action.tag == TAG_GRAMMAR_REF)
            {
                grammar_ref = action.value.v;
            }
        }

        if (grammar_ref < 0) continue; // no grammar, can't auto-render

        // Check confidence threshold
        var confidence: vlp_q16 = fired.confidence;
        var threshold: vlp_q16 = session.config.auto_response_confidence_threshold;
        // Default threshold: 90/100 (58982 at Q16)
        // Integer comparison: is confidence >= threshold?
        if (confidence.v < threshold.v) continue;

        // Check: does the rule's output cover the input?
        // This is domain-specific. For SRE:
        // Input was an alert. Rule produced triage + root cause + remediation.
        // That's fully handled.
        // For interactive chat:
        // Input was a question. Rule produced a factual answer.
        // That's fully handled.
        // Heuristic: if the rule's action set includes a DIRECT_OUTPUT action,
        // it intends to fully respond.
        var has_output = false;
        for (fired.actions[0..fired.n_actions]) |action| {
            if (action.type == ACTION_DIRECT_OUTPUT) {
                has_output = true;
            }
        }

        if (!has_output) continue;

        // This rule fully handles the input.
        resolution.fully_handled = true;
        resolution.grammar = vlp_grammar_load_by_ref(kb_store, grammar_ref);

        // Build grammar mappings from the rule's output facts
        for (fired.actions[0..fired.n_actions]) |action| {
            if (action.type == ACTION_ASSERT) {
                resolution.mappings[resolution.n_mappings] = vlp_grammar_kb_mapping{
                    .slot_index = resolution.n_mappings,
                    .kb_id = action.target_kb_id,
                    .slot_id = action.target_slot_id,
                };
                resolution.n_mappings += 1;
            }
        }

        resolution.n_actions = fired.n_actions;
        break; // first fully-resolving rule wins
    }

    return resolution;
}
```

---

## 7. Output Routing

Where does output go after the cycle?

```
fn vlp_route_output(runner: *vlp_runner, output: *vlp_output_buffer) -> void {
    // Different runner types route output differently.

    switch (runner.type) {

        .RUNNER_POLLER => {
            // Poller output goes to notification KB.
            // An interactive session or external webhook reads it.
            if (output.len > 0) {
                var notification_kb = runner.config.notification_kb_id;
                vlp_kb_queue_push(runner.kb_store, notification_kb,
                    "notifications", output.buf, output.len);

                // If external webhook configured, also POST it
                if (runner.config.webhook_url_len > 0) {
                    vlp_http_post(runner.config.webhook_url,
                        runner.config.webhook_url_len,
                        output.buf, output.len);
                }
            }
        },

        .RUNNER_PROCESSOR => {
            // Processor output is typically internal — compacted facts.
            // If the processor's cycle produced prose output (unusual),
            // it goes to a log KB.
            if (output.len > 0) {
                vlp_kb_ring_write(runner.kb_store, runner.config.log_kb_id,
                    "processor_output", output.buf, output.len);
            }
        },

        .RUNNER_INTERNAL => {
            // Internal runner output is derived facts — already in KB.
            // Prose output rare but goes to log.
            if (output.len > 0) {
                vlp_kb_ring_write(runner.kb_store, runner.config.log_kb_id,
                    "internal_output", output.buf, output.len);
            }
        },

        .RUNNER_BATCH => {
            // Batch output goes to result queue in parent session.
            if (output.len > 0) {
                vlp_kb_queue_push(runner.kb_store,
                    runner.config.result_queue_kb_id,
                    "results", output.buf, output.len);
            }
        },
    }
}
```

---

## 8. Server Protocol Handlers

### 8.1 HTTP Handler

```
fn vlp_http_read_request(
    socket: os_socket_t,
    request: *vlp_protocol_request,
    timeout_ms: i32,
) -> vlp_status {

    // Read until \r\n\r\n (header terminator)
    var header_buf: [8192]u8 = undefined;
    var header_len: i32 = 0;
    var read_status = vlp_socket_read_until(
        socket, &header_buf, &header_len, "\r\n\r\n", timeout_ms);

    if (read_status != VLP_OK) return read_status;

    // Parse request line: METHOD SP PATH SP VERSION CRLF
    // Compiled parser — not LLM. Character-by-character state machine.
    var method_end = vlp_find_byte(&header_buf, ' ', header_len);
    if (method_end < 0) return VLP_ERR_PROTOCOL_MALFORMED;

    request.method = vlp_http_parse_method(header_buf[0..@intCast(method_end)]);
    if (request.method == .UNKNOWN) return VLP_ERR_PROTOCOL_MALFORMED;

    var path_start = method_end + 1;
    var path_end = vlp_find_byte(header_buf[@intCast(path_start)..], ' ', header_len - path_start);
    if (path_end < 0) return VLP_ERR_PROTOCOL_MALFORMED;
    path_end += path_start;

    request.path_offset = @intCast(path_start);
    request.path_length = @intCast(path_end - path_start);

    // Parse headers
    // Each header: NAME: VALUE CRLF
    // Compiled parser extracts:
    //   Content-Length (for body read)
    //   Authorization (for auth)
    //   Connection (for keepalive)
    //   Content-Type (for input parsing)
    var header_parser: vlp_http_header_parser = undefined;
    vlp_http_parse_headers(&header_buf, header_len, &header_parser);

    request.content_length = header_parser.content_length;
    request.keepalive = header_parser.connection_keepalive;
    @memcpy(&request.auth_header, header_parser.auth_value[0..header_parser.auth_value_len]);
    request.auth_header_len = header_parser.auth_value_len;

    // Read body if Content-Length > 0
    if (request.content_length > 0) {
        if (request.content_length > MAX_REQUEST_BODY) {
            return VLP_ERR_PROTOCOL_BODY_TOO_LARGE;
        }
        var body_read = vlp_socket_read_exact(
            socket, request.body, request.content_length, timeout_ms);
        if (body_read != VLP_OK) return body_read;
    }

    request.raw_bytes_len = header_len + request.content_length;

    // Parse body based on Content-Type
    // If JSON: parse via builtin (not LLM), store to temp KB
    // If form-urlencoded: parse via compiled parser
    // If text: pass through as-is
    switch (header_parser.content_type) {
        .JSON => {
            request.input_type = .STRUCTURED;
            // Actual JSON parsing happens in vlp_protocol_to_input
        },
        .FORM => {
            request.input_type = .STRUCTURED;
        },
        else => {
            request.input_type = .TEXT;
        },
    }

    return VLP_OK;
}
```

### 8.2 WebSocket Handler

```
fn vlp_websocket_handle(
    server: *vlp_server,
    conn: *vlp_server_connection,
) -> void {

    // WebSocket is a stateful, bidirectional connection.
    // Perfect for interactive sessions.
    // The session persists across messages — KV-cache, KB state, rules.

    while (conn.state == .ACTIVE) {

        // Check credential
        if (!vlp_credential_check(&conn.credential)) {
            vlp_websocket_send_close(conn.socket, 4001, "credential expired");
            conn.state = .DRAINING;
            break;
        }

        // Read WebSocket frame
        var frame: vlp_ws_frame = undefined;
        var read_status = vlp_websocket_read_frame(conn.socket, &frame, 60000);

        if (read_status == VLP_TIMEOUT) continue;
        if (read_status == VLP_CONNECTION_CLOSED) {
            conn.state = .DRAINING;
            break;
        }

        switch (frame.opcode) {
            .TEXT => {
                // Text message — process through universal cycle
                var input: vlp_input = undefined;
                vlp_input_from_text(frame.payload, frame.payload_len, &input);

                var output: vlp_output_buffer = undefined;
                vlp_output_buffer_init(&output, conn.output_buf, CONN_OUTPUT_CAPACITY);

                var result = vlp_cycle(
                    conn.session, &input, &output,
                    server.kb_store, server.llm_engine, conn.stream);

                // Send response as WebSocket text frame
                vlp_websocket_send_text(conn.socket, output.buf, output.len);

                conn.requests_served += 1;
                server.total_requests_served += 1;
            },

            .BINARY => {
                // Binary message — parse to KB directly via builtin
                var temp_kb: i32 = undefined;
                vlp_kb_store_create_kb(server.kb_store, &temp_kb,
                    &vlp_kb_config{ .name = "ws_binary_temp",
                        .parent_id = conn.session.kb_root_id });

                // Attempt to parse as known binary format
                vlp_builtin_dispatch(BUILTIN_PARSE_BINARY,
                    &vlp_builtin_args{
                        .input = frame.payload,
                        .input_len = frame.payload_len,
                        .target_kb_id = temp_kb,
                    });

                // Run cycle with reference to parsed data
                var input: vlp_input = undefined;
                vlp_input_from_kb_ref(temp_kb, &input);

                var output: vlp_output_buffer = undefined;
                vlp_output_buffer_init(&output, conn.output_buf, CONN_OUTPUT_CAPACITY);

                vlp_cycle(conn.session, &input, &output,
                    server.kb_store, server.llm_engine, conn.stream);

                vlp_websocket_send_text(conn.socket, output.buf, output.len);
            },

            .PING => {
                vlp_websocket_send_pong(conn.socket, frame.payload, frame.payload_len);
            },

            .CLOSE => {
                vlp_websocket_send_close(conn.socket, 1000, "normal closure");
                conn.state = .DRAINING;
            },

            else => {},
        }

        conn.last_active = vlp_timestamp_now();
    }
}
```

---

## 9. Rate Limiting

Exact integer accounting. No drift, no false threshold crossings.

```
struct vlp_rate_limiter {
    // Per-user rate limits stored as counters in auth KB
    // Counter: requests in current window
    // Window: fixed time interval
    // Limit: max requests per window
    // All integers. Comparison is exact.

    window_seconds: i32,
    max_requests: i32,
};

fn vlp_rate_limit_check(
    limiter: *vlp_rate_limiter,
    kb_store: *vlp_kb_store,
    user_id: i32,
) -> vlp_rate_limit_result {

    var now = vlp_timestamp_now();

    // Load user's rate limit counter from auth KB
    var counter_name_buf: [32]u8 = undefined;
    var counter_name_len = vlp_format_counter_name(user_id, &counter_name_buf);

    var counter_value: i32 = 0;
    var counter_window_start: i32 = 0;

    TensorPrologCounterGet(kb_store, limiter.counter_kb_id,
        &counter_name_buf, &counter_value);

    // Check window
    var window_fact: vlp_fact = undefined;
    vlp_kb_store_fact_read(kb_store, limiter.counter_kb_id,
        user_id * 2 + 1, &window_fact); // window start timestamp
    counter_window_start = window_fact.value.v;

    // Is current request in the same window?
    if (now - counter_window_start >= limiter.window_seconds) {
        // New window. Reset counter.
        TensorPrologCounterReset(kb_store, limiter.counter_kb_id, &counter_name_buf);
        counter_value = 0;
        // Update window start
        window_fact.value.v = now;
        vlp_kb_store_fact_write(kb_store, limiter.counter_kb_id,
            user_id * 2 + 1, &window_fact);
    }

    // Check limit — exact integer comparison
    if (counter_value >= limiter.max_requests) {
        // Rate limited.
        var remaining_seconds = limiter.window_seconds - (now - counter_window_start);
        return vlp_rate_limit_result{
            .allowed = false,
            .remaining = 0,
            .retry_after_seconds = remaining_seconds,
        };
    }

    // Allow and increment
    TensorPrologCounterIncrement(kb_store, limiter.counter_kb_id,
        &counter_name_buf, 1);

    return vlp_rate_limit_result{
        .allowed = true,
        .remaining = limiter.max_requests - counter_value - 1,
        .retry_after_seconds = 0,
    };
}
```

---

## 10. Health Check and Metrics

The server exposes its own health through exact integer metrics.

```
fn vlp_server_health_check(server: *vlp_server) -> vlp_health_report {

    var report: vlp_health_report = undefined;

    // Connection metrics — exact counts
    report.active_connections = server.n_active;
    report.total_accepted = server.total_connections_accepted;
    report.total_rejected = server.total_connections_rejected;
    report.total_requests = server.total_requests_served;

    // Runner metrics — exact counts per runner
    for (server.runners[0..server.n_runners]) |runner| {
        report.runners[report.n_runners] = vlp_runner_health{
            .id = runner.id,
            .type = runner.type,
            .state = runner.state,
            .iterations = runner.iterations_completed,
            .errors_consecutive = runner.errors_consecutive,
            .errors_total = runner.errors_total,
            .recycle_count = runner.recycle_count,
            .last_iteration_ms = runner.last_iteration_ms,
        };
        report.n_runners += 1;
    }

    // Session metrics
    report.active_sessions = server.session_manager.active_count;
    report.total_facts = server.kb_store.fact_count;
    report.total_rules = server.kb_store.rule_count;

    // Level distribution — exact fractions
    var stats = vlp_level_stats_aggregate(server.session_manager);
    report.l1_percent_num = stats.l1_count;
    report.l1_percent_den = stats.l1_count + stats.l2_count + stats.l3_count;
    report.l2_percent_num = stats.l2_count;
    report.l2_percent_den = report.l1_percent_den;
    report.l3_percent_num = stats.l3_count;
    report.l3_percent_den = report.l1_percent_den;
    // These are exact fractions, not floats.
    // l3_percent = 93/100 means exactly 93% of operations were fully automated.

    // Memory
    report.device_memory_used = vlp_device_memory_used();
    report.device_memory_total = vlp_device_memory_total();

    // Confidence in health report: SOURCE_VDR_COMPUTATION (1/1).
    // These are exact integer counts, not sampled approximations.
    report.confidence = CONFIDENCE_TABLE[SOURCE_VDR_COMPUTATION];

    return report;
}

fn vlp_server_metrics_endpoint(server: *vlp_server, response: *vlp_protocol_response) -> vlp_status {
    // Render health report through grammar — zero LLM tokens.

    var report = vlp_server_health_check(server);

    var metrics_grammar: vlp_grammar = undefined;
    vlp_grammar_load_from_kb(server.kb_store, server.protocol_grammar_kb_id,
        GRAMMAR_SLOT_METRICS, &metrics_grammar);

    // Grammar template:
    // {"active_connections": {conns:integer}, "total_requests": {reqs:integer},
    //  "l3_auto_percent": {l3_num:integer}/{l3_den:integer},
    //  "active_sessions": {sessions:integer}, "rules": {rules:integer},
    //  "facts": {facts:integer}, "runners": [{runner_entries:text}]}

    var fills: [16]vlp_grammar_fill = undefined;
    fills[0] = .{ .slot_index = 0, .int_value = report.active_connections };
    fills[1] = .{ .slot_index = 1, .int_value = @intCast(report.total_requests) };
    fills[2] = .{ .slot_index = 2, .int_value = @intCast(report.l3_percent_num) };
    fills[3] = .{ .slot_index = 3, .int_value = @intCast(report.l3_percent_den) };
    fills[4] = .{ .slot_index = 4, .int_value = report.active_sessions };
    fills[5] = .{ .slot_index = 5, .int_value = report.total_rules };
    fills[6] = .{ .slot_index = 6, .int_value = @intCast(report.total_facts) };

    vlp_grammar_render(&metrics_grammar, &fills, 7,
        response.buf, response.capacity, &response.len);

    // The entire metrics response is grammar-rendered.
    // Every brace, every colon, every comma came from the grammar.
    // The numbers came from exact integer counters.
    // The LLM was not involved. Zero tokens. 100% correct JSON. Always.

    return VLP_OK;
}
```

---

## 11. Idle Connection Reaper

```
fn vlp_server_reaper(server: *vlp_server) -> void {
    // Runs as internal runner. Kills idle connections.

    var now = vlp_timestamp_now();
    var idle_threshold = server.config.idle_timeout_seconds;

    for (&server.connections) |*conn| {
        if (conn.state != .ACTIVE) continue;

        // Check idle — integer comparison
        var idle_seconds = now - conn.last_active;
        if (idle_seconds >= idle_threshold) {
            vlp_protocol_send_timeout(server.protocol, conn.socket);
            vlp_server_close_connection(server, conn, .IDLE_TIMEOUT);
        }

        // Check credential expiry — integer comparison
        if (now >= conn.credential.expires_at) {
            vlp_protocol_send_credential_expired(server.protocol, conn.socket);
            vlp_server_close_connection(server, conn, .CREDENTIAL_EXPIRED);
        }

        // Check turn budget
        if (conn.session.current_turn >= server.max_session_turns) {
            // Don't close — recycle.
            // Snapshot, kill session, clone from template, restore accumulated facts.
            vlp_server_recycle_connection_session(server, conn);
        }
    }
}
```

---

## 12. Graceful Shutdown

```
fn vlp_server_shutdown(server: *vlp_server) -> vlp_status {

    // Signal shutdown
    server.shutdown_flag = 1;

    // Stop accepting new connections
    os_socket_close(server.listen_socket);

    // Stop all runners
    for (server.runners[0..server.n_runners]) |*runner| {
        vlp_runner_stop(runner);
    }

    // Drain active connections
    for (&server.connections) |*conn| {
        if (conn.state == .ACTIVE) {
            conn.state = .DRAINING;
            // Send protocol-appropriate close
            vlp_protocol_send_shutdown(server.protocol, conn.socket);
        }
    }

    // Wait for connections to close (with timeout)
    var deadline = vlp_timestamp_now() + server.config.shutdown_timeout_seconds;
    while (server.n_active > 0 and vlp_timestamp_now() < deadline) {
        vlp_sleep_ms(100);
    }

    // Force-close any remaining
    for (&server.connections) |*conn| {
        if (conn.state != .CLOSED) {
            // Snapshot session for persistence
            if (server.config.persistent_sessions and conn.session.id >= 0) {
                vlp_session_snapshot(conn.session, &snapshot);
                vlp_snapshot_save(&snapshot,
                    vlp_session_snapshot_path(conn.credential.user_id));
            }
            vlp_server_close_connection(server, conn, .SHUTDOWN);
        }
    }

    // Final audit entry
    vlp_audit_write(server.kb_store, null, AUDIT_SERVER_SHUTDOWN,
        0, @intCast(server.total_requests_served), 0);

    // Shutdown thread pool
    vlp_runner_pool_shutdown();

    // Save server state snapshot (accumulated rules, grammars, KB state)
    vlp_snapshot_save(&server.template_snapshot, server.config.state_save_path);

    return VLP_OK;
}
```

---

## 13. The Complete Picture

One loop. The universal cycle. Everything is an instantiation of it.

**Interactive chat:** user types input → cycle runs → output goes to screen. Session persists between turns. KV-cache grows. Snapshot on disconnect.

**Polling runner:** timer fires → cycle runs with synthetic input → Phase 0 fires rules → if fully resolved, zero LLM tokens → output goes to notification KB. Repeats every interval.

**Processor runner:** external data arrives → mini-cycle compacts to KB facts → rules handle known patterns at L3 → LLM handles novel patterns at L1 → LLM writes rules so novel becomes known → recycle at turn threshold. Continuous.

**Internal runner:** timer fires → compute_fn derives facts from existing facts → all exact integer arithmetic → zero LLM tokens. Repeats every interval.

**Batch runner:** task popped from queue → clone session → cycle runs in clone → results merge back → clone killed. Concurrent up to max.

**HTTP server:** request arrives → clone from template snapshot → authenticate → inject grants → cycle runs → grammar renders response → send → close or keepalive.

**WebSocket server:** upgrade → clone from template → authenticate → message loop → each message is a cycle → session persists across messages → credential expires → close.

**SMTP/MQTT/DNS server:** same pattern. Protocol grammar handles wire format. Cycle handles content. Session provides isolation. Grants gate operations.

Every one of these:
- Runs the same `vlp_cycle` function.
- Uses the same KB store, same Prolog engine, same grammar engine, same builtins.
- Has the same access control (integer comparison before data access).
- Has the same grant enforcement (integer comparison before operation).
- Has the same audit trail (append-only ring buffer).
- Has the same determinism guarantee (integers don't drift).
- Has the same recycle mechanism (snapshot → kill → clone → continue).
- Produces the same output given the same input and state. Every time. On every device.

The game loop is the system. Everything else is configuration.
