Let's trace a concrete scenario. The monitoring watch fires: API latency P99 has exceeded threshold.

**Step 1: Pull Prometheus data.**

The LLM issues an operational command to query Prometheus. This is a net_fetch to the Prometheus HTTP API — it's already covered by VDR-6's network primitives with a grant.

```
CMD: lock_acquire(root.ops.incident_002.investigating, holder: "latency_spike")
CMD: counter_create(root.ops.incident_002.queries_issued)

CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query_range?query=http_request_duration_seconds{quantile='0.99'}&start=2026-05-16T14:00:00Z&end=2026-05-16T15:00:00Z&step=60",
    grant: "monitoring_read")
→ raw JSON stored at root.ops.incident_002.raw_latency
CMD: counter_inc(root.ops.incident_002.queries_issued)
```

**Step 2: Unwrap the JSON into structured data.**

The raw response is Prometheus JSON — nested, with metadata. The LLM uses pure primitives to extract the time series:

```
CMD: PURE_FN parse_json(root.ops.incident_002.raw_latency) 
→ stored at root.ops.incident_002.parsed_latency

CMD: PURE_FN dict_get(root.ops.incident_002.parsed_latency, "data")
→ data_block
CMD: PURE_FN dict_get(data_block, "result")
→ result_list
CMD: PURE_FN list_nth(result_list, 0)
→ first_series
CMD: PURE_FN dict_get(first_series, "values")
→ timestamp_value_pairs

// Store the clean time series
CMD: KB_ASSERT(root.ops.incident_002.timeseries,
    binding("latency_p99", timestamp_value_pairs))
```

**Step 3: Convert to exact VDR fractions for time series analysis.**

The Prometheus values come back as strings. The LLM converts them to exact fractions and stores in a ring buffer for rolling analysis:

```
CMD: ring_create(root.ops.incident_002.latency_window, capacity: 60)

CMD: PURE_FN list_map(timestamp_value_pairs, fn(pair, 
    [to_number(pair[0]), to_fraction(pair[1])])) 
→ exact_series
CMD: KB_ASSERT(root.ops.incident_002.timeseries,
    binding("latency_exact", exact_series))

// Push each data point into the ring buffer for rolling analysis
CMD: PURE_FN for_each(exact_series, fn(point,
    ring_write(root.ops.incident_002.latency_window, point)))
```

**Step 4: Time series operations with builtins.**

Now the LLM does the analysis with pure primitives — no token prediction arithmetic:

```
// Extract just the latency values from the pairs
CMD: PURE_FN list_map(exact_series, fn(pair, pair[1])) → latency_values

// Basic stats
CMD: PURE_FN stat_mean(latency_values) → fraction(4200, 1)    // 4200ms mean
CMD: PURE_FN stat_median(latency_values) → fraction(3800, 1)  // 3800ms median
CMD: PURE_FN stat_percentile(latency_values, fraction(99,100)) → fraction(8200, 1)
CMD: PURE_FN vdr_max(latency_values) → fraction(12400, 1)     // peak at 12.4s

// Store computed stats
CMD: KB_ASSERT(root.ops.incident_002.stats,
    binding("mean_latency_ms", fraction(4200, 1)))
CMD: KB_ASSERT(root.ops.incident_002.stats,
    binding("p99_latency_ms", fraction(8200, 1)))
CMD: KB_ASSERT(root.ops.incident_002.stats,
    binding("max_latency_ms", fraction(12400, 1)))

// Find the spike onset — first point above 2x baseline
CMD: PURE_FN list_filter(exact_series, 
    predicate(fn(pair, pair[1] > fraction(4000, 1)))) → spike_points
CMD: PURE_FN list_head(spike_points) → [timestamp(1747400400), fraction(4100, 1)]
CMD: KB_ASSERT(root.ops.incident_002.stats,
    binding("spike_onset", timestamp(1747400400)))

// Count how many minutes above threshold
CMD: PURE_FN list_length(spike_points) → 38
CMD: KB_ASSERT(root.ops.incident_002.stats,
    binding("minutes_above_threshold", 38))
```

**Step 5: Pull correlated metrics from Prometheus.**

The spike started at a specific time. The LLM now pulls related metrics to correlate:

```
CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query_range?query=node_cpu_seconds_total{mode='user'}&start=2026-05-16T14:00:00Z&end=2026-05-16T15:00:00Z&step=60",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_cpu
CMD: counter_inc(root.ops.incident_002.queries_issued)

CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query_range?query=pg_stat_activity_count&start=2026-05-16T14:00:00Z&end=2026-05-16T15:00:00Z&step=60",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_db_connections
CMD: counter_inc(root.ops.incident_002.queries_issued)

CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query_range?query=rate(http_requests_total[1m])&start=2026-05-16T14:00:00Z&end=2026-05-16T15:00:00Z&step=60",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_request_rate
CMD: counter_inc(root.ops.incident_002.queries_issued)
```

Parse and convert all three the same way:

```
CMD: PURE_FN parse_json(root.ops.incident_002.raw_cpu) → ...
// ... extract, convert to exact fractions ...
CMD: KB_ASSERT(root.ops.incident_002.timeseries,
    binding("cpu_user", cpu_exact_series))

CMD: PURE_FN parse_json(root.ops.incident_002.raw_db_connections) → ...
CMD: KB_ASSERT(root.ops.incident_002.timeseries,
    binding("db_connections", db_exact_series))

CMD: PURE_FN parse_json(root.ops.incident_002.raw_request_rate) → ...
CMD: KB_ASSERT(root.ops.incident_002.timeseries,
    binding("request_rate", rps_exact_series))
```

**Step 6: Python for correlation analysis.**

The LLM has four exact time series in the KB. It writes a Python script that reads them and computes cross-correlation to find which metric spiked first:

```
CMD: ENV_UPLOAD(env_analysis, correlate.py, root.ops.scripts.correlate)
// Script:
// - Read all four time series from KB via stdin/args
// - Align timestamps
// - For each pair, compute lag-0 and lag-1 cross-correlation
//   using exact VDR fractions
// - Find which metric's spike onset precedes the latency spike
// - Output the leading indicator and the lag in minutes

CMD: ENV_EXEC(env_analysis, "python3", root.ops.scripts.correlate)
→ {leading_metric: "db_connections",
   lag_minutes: 3,
   correlation_with_latency: fraction(94, 100),
   cpu_correlation: fraction(78, 100),
   request_rate_correlation: fraction(12, 100)}

CMD: KB_ASSERT(root.ops.incident_002.correlation,
    binding("leading_indicator", "db_connections"))
CMD: KB_ASSERT(root.ops.incident_002.correlation,
    binding("lead_time_minutes", 3))
CMD: KB_ASSERT(root.ops.incident_002.correlation,
    binding("correlation_strength", fraction(94, 100)))
```

Database connections spiked 3 minutes before latency went up. Request rate barely correlates — this isn't a traffic spike. CPU correlates moderately — it's a symptom, not the cause.

**Step 7: Prolog deduces from the processed data.**

Now the LLM writes Prolog rules that reason over the stored processed data:

```
CMD: KB_ASSERT(root.ops.incident_002.reasoning,
    rule(primary_cause(db_connection_exhaustion) :-
        binding("leading_indicator", "db_connections"),
        binding("correlation_strength", Corr),
        Corr > fraction(9, 10),
        binding("lead_time_minutes", Lead),
        Lead > 0))

CMD: KB_ASSERT(root.ops.incident_002.reasoning,
    rule(not_traffic_related :-
        binding("request_rate_correlation", RCorr),
        RCorr < fraction(3, 10)))

CMD: KB_ASSERT(root.ops.incident_002.reasoning,
    rule(cause_chain(db_connections_spike, leads_to, cpu_increase, leads_to, latency_spike) :-
        primary_cause(db_connection_exhaustion),
        binding("cpu_correlation", CCorr),
        CCorr > fraction(5, 10)))

CMD: KB_QUERY(root.ops.incident_002.reasoning, primary_cause(X))
→ X = db_connection_exhaustion

CMD: KB_QUERY(root.ops.incident_002.reasoning, not_traffic_related)
→ true

CMD: KB_QUERY(root.ops.incident_002.reasoning, cause_chain(A, _, B, _, C))
→ A = db_connections_spike, B = cpu_increase, C = latency_spike
```

**Step 8: Drill deeper with another Prometheus query.**

The cause is database connections. The LLM pulls the specific database pool metrics:

```
CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query?query=pg_stat_activity_count{state='active'}&time=2026-05-16T14:30:00Z",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_db_active
CMD: counter_inc(root.ops.incident_002.queries_issued)

CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query?query=pg_stat_activity_count{state='idle+in+transaction'}&time=2026-05-16T14:30:00Z",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_db_idle_tx
CMD: counter_inc(root.ops.incident_002.queries_issued)

CMD: PURE_FN parse_json(root.ops.incident_002.raw_db_active) → ...
CMD: PURE_FN parse_json(root.ops.incident_002.raw_db_idle_tx) → ...

CMD: KB_ASSERT(root.ops.incident_002.db_state,
    binding("active_connections", 45))
CMD: KB_ASSERT(root.ops.incident_002.db_state,
    binding("idle_in_transaction", 153))
CMD: KB_ASSERT(root.ops.incident_002.db_state,
    binding("max_connections", 200))

// Compute saturation with exact fractions
CMD: PURE_FN vdr_add(fraction(45, 1), fraction(153, 1)) → fraction(198, 1)
CMD: PURE_FN vdr_div(fraction(198, 1), fraction(200, 1)) → fraction(99, 100)
CMD: KB_ASSERT(root.ops.incident_002.db_state,
    binding("connection_saturation", fraction(99, 100)))

CMD: lru_push(root.ops.incident_002.findings, "db_saturation",
    "99% connection saturation — 153 idle-in-transaction hogging the pool")
```

153 idle-in-transaction connections. Something is opening transactions and not closing them.

**Step 9: Python identifies the culprit queries.**

```
CMD: OP_FN net_fetch(
    "http://prometheus:9090/api/v1/query?query=topk(5,+pg_stat_activity_count+by+(query))&time=2026-05-16T14:30:00Z",
    grant: "monitoring_read")
→ stored at root.ops.incident_002.raw_top_queries

CMD: PURE_FN parse_json(root.ops.incident_002.raw_top_queries) → parsed
CMD: PURE_FN dict_get(parsed, "data") → data
CMD: PURE_FN dict_get(data, "result") → query_list

// Write Python to parse the query signatures and group by origin
CMD: ENV_UPLOAD(env_analysis, analyze_queries.py, root.ops.scripts.queries)
// Script: 
// - Extract query text and connection count from Prometheus results
// - Group by query prefix (SELECT, UPDATE, etc.)
// - Identify which application endpoint generates each query pattern
// - Cross-reference with deployment history
CMD: ENV_EXEC(env_analysis, "python3", root.ops.scripts.queries)
→ {top_idle_query: "SELECT * FROM user_sessions WHERE ...",
   connection_count: 148,
   likely_source: "session_cleanup_job",
   started_appearing: "2026-05-16T14:27:00Z",
   matches_deployment: "v2.3.1 deployed at 14:15"}
```

**Step 10: Full causal chain in Prolog, built from Prometheus-derived data.**

```
CMD: KB_ASSERT(root.ops.incident_002.root_cause,
    fact(culprit_query("SELECT * FROM user_sessions WHERE ...",
        source("session_cleanup_job"),
        connections_held(148),
        state("idle_in_transaction"))))

CMD: KB_ASSERT(root.ops.incident_002.root_cause,
    fact(triggered_by(deployment("v2.3.1", at("14:15")))))

CMD: KB_ASSERT(root.ops.incident_002.reasoning,
    rule(full_chain(Deployment, Query, DBSaturation, CPUSpike, LatencySpike) :-
        triggered_by(Deployment),
        culprit_query(Query, source(_), connections_held(N), _),
        N > 100,
        binding("connection_saturation", Sat),
        Sat > fraction(95, 100),
        cause_chain(db_connections_spike, _, cpu_increase, _, latency_spike)))

CMD: KB_QUERY(root.ops.incident_002.reasoning, 
    full_chain(Dep, Query, _, _, _))
→ Dep = deployment("v2.3.1", at("14:15")),
  Query = "SELECT * FROM user_sessions WHERE ..."
```

**Step 11: Store the complete investigation and write prevention rules.**

```
CMD: counter_get(root.ops.incident_002.queries_issued) → 6

CMD: KB_ASSERT(root.ops.incident_002.summary,
    fact(incident(002,
        root_cause("session_cleanup_job in v2.3.1 opens transactions without closing"),
        chain([deployment_v2_3_1, idle_in_transaction_leak, 
               connection_pool_exhaustion, latency_spike]),
        detection_time("14:30"),
        onset_time("14:27"),
        deployment_time("14:15"),
        prometheus_queries_used(6),
        correlation_method("cross-correlation with 3-minute lag detection"))))

// Permanent monitoring rules
CMD: KB_ASSERT(root.ops.sre_rules,
    rule(early_warning(idle_transaction_leak) :-
        prometheus_metric("pg_stat_activity_count", state("idle_in_transaction"), Count),
        Count > 50))

CMD: KB_ASSERT(root.ops.sre_rules,
    rule(auto_investigate_on_deploy :-
        recent_deployment(_, deployed_at(T)),
        prometheus_query_at(T + minutes(15), "pg_stat_activity_count", Count),
        Count > pre_deploy_baseline * fraction(15, 10)))

CMD: lock_release(root.ops.incident_002.investigating)
```

The complete flow was: Prometheus (raw data) → parse_json (structure) → dict/list primitives (extract) → VDR arithmetic (exact time series) → Python (cross-correlation) → store in KB (working memory) → Prolog (causal deduction) → back to Prometheus (drill down) → Python (query analysis) → Prolog (full chain) → permanent rules (prevention).

Six Prometheus queries, each parsed by builtins, converted to exact fractions, analyzed by a mix of pure primitives and Python, stored at KB paths, reasoned over by Prolog. The LLM never did arithmetic. It never guessed at correlations. It orchestrated exact tools in a logical sequence, and every intermediate result — every time series, every correlation coefficient, every connection count — is in the KB at a dotted path, queryable, exact, and traceable.

The trick is that the Prometheus data enters as raw JSON, becomes structured data through command token primitives, becomes exact fractions through VDR conversion, becomes working memory through KB storage, becomes evidence through Prolog assertion, and becomes conclusions through Prolog deduction. Each transformation is one or two command tokens. The data moves through the system getting progressively more structured and meaningful at each stage, and nothing is lost — every intermediate form is at a KB path if you need to inspect it.
