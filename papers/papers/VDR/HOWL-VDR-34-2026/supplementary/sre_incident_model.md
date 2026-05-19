## Naive Single-Shot: Conventional LLM

SRE engineer pastes into a chat window: "Service checkout-api is returning 503s at 15% rate, started 20 minutes ago, here are the last 200 lines of logs" followed by 200 lines of raw log text.

The LLM reads the entire log through attention. 200 lines is maybe 8,000 tokens. The LLM generates a response: "Based on the logs, it appears that..." — another 500 tokens of hedged analysis. It identifies some patterns, misses others, gets a timestamp wrong because it's doing arithmetic through token prediction.

The engineer says "check if the database is related." The LLM re-reads the original 8,000 tokens plus its 500-token response plus the new query. 8,600 tokens of attention compute to process a 10-word question. It generates speculation about database connectivity because it has no access to any actual database metrics.

Turn 3: engineer pastes 50 more log lines and a Grafana screenshot description. Now 12,000 tokens of context being re-read. The LLM tries to correlate timestamps across two paste blocks by reading them character by character through attention.

Turn 5: engineer pastes the service dependency graph as text. 16,000 tokens. Attention is quadratic. Quality is degrading. The LLM contradicts something it said in turn 2 because earlier tokens are losing attention weight.

Turn 10: context window is at 35,000 tokens. Half of it is the LLM's own hedged prose being re-read. The engineer is frustrated because the LLM keeps asking for information it was already given. The investigation has produced no durable artifacts. If the session ends, everything is gone.

Total: ~35,000 tokens of attention compute, no persistent findings, no reusable rules, degrading quality, zero exact computations, confidence expressed as "likely" and "appears to" and "it's possible that." Cost: ~$27.58 at standard rates. Duration: ~660 seconds of compute. The engineer did most of the actual reasoning.

---

## VDR-LLM-Prolog Mature Operations System

### The system before the incident

This isn't a blank session. This is a running operational system that has been handling SRE work for months. Here's what exists before any human touches it today.

**Four runner types are active:**

A polling runner (C3) executes every 60 seconds. Fresh LLM every cycle — no attention degradation, ever. It checks the task queue at `root.ops.tasks`, reads counters at `root.ops.metrics.health`, scans directory watch lists at `/vdr/ingress/`. Each cycle costs 10-50 tokens. The poller doesn't analyze anything. It routes. A new file in ingress gets classified by accumulated compaction rules and routed to the correct KB branch. A counter exceeding threshold gets a task enqueued. The poller terminates after each cycle. Knowledge stays at integer addresses.

Three processor runners (C4) maintain persistent connections to data streams. One watches Prometheus metrics via credentialed API connection, compacting incoming metrics into `root.ops.metrics.prometheus`. One watches the deployment pipeline, compacting deploy events into `root.ops.deploys`. One watches the alerting system. Each processor has a respawn threshold — at 200 turns, it snapshots its connection state as KB facts, terminates, and a fresh clone reads the snapshot and re-establishes the connection. The data stream is continuous. The LLM processing it is always fresh. The metrics are exact VDR fractions at integer addresses.

An internal processing runner (C5) executes every 5 minutes. It evaluates KB state: runs consistency checks across the service topology KB, computes derived facts (rolling averages as exact fractions, trend directions as exact comparisons), identifies coverage gaps, updates coverage metrics. Read-broad, write-derived-only. No external access. It can't escalate its own grants. It produces facts like `trend(checkout_api, error_rate, increasing, 14/1000_to_23/1000, last_15_min)` — exact fractions, exact time windows, stored at integer addresses.

**The KB tree that already exists:**

```
root
├── system
│   └── oso (176 Prolog terms: axioms, priorities, knowability)
├── ops
│   ├── services
│   │   ├── checkout_api (facts: endpoints, dependencies, SLA, team)
│   │   ├── payment_service (facts: endpoints, dependencies, SLA)
│   │   ├── inventory_service (...)
│   │   ├── db_primary (facts: connection strings, replica topology)
│   │   └── db_replica_pool (...)
│   ├── metrics
│   │   ├── prometheus (rolling window of compacted metrics)
│   │   ├── health (counters: per-service error rates, latencies)
│   │   └── derived (trend facts from internal processor)
│   ├── deploys (recent deployment facts with provenance)
│   ├── incidents
│   │   ├── templates (5 inference notebook templates from VDR-14)
│   │   └── (past incidents as child KBs, frozen, queryable)
│   ├── rules
│   │   ├── triage (150+ Prolog rules from past investigations)
│   │   ├── correlation (rules linking symptom patterns to causes)
│   │   └── escalation (rules for severity classification)
│   ├── tasks (bounded queue for pending work)
│   ├── scripts (accumulated Python scripts with provenance)
│   └── grammars (SRE-specific output grammars)
└── users
    └── sre_engineer_1 (account KB with grants, preferences)
```

This tree has been accumulating for months. The 150+ triage rules in `root.ops.rules.triage` were formalized during past investigations — each one cost 25-40 tokens to create, each one fires automatically at zero LLM cost on every subsequent matching pattern. The service topology facts were compacted from documentation and config files through the ingress pipeline. The Prometheus metrics are continuously updated by the processor runner. Everything is at integer addresses. Nothing is in any LLM's context window.

**What's already happened before the engineer opens a chat:**

The Prometheus processor runner detected checkout-api 503 rate crossing 10% threshold 3 minutes ago. It asserted: `alert(checkout_api, error_rate_high, 152/1000, timestamp_1747612800)` — exact fraction, exact timestamp, integer address.

The polling runner picked this up on its next 60-second cycle. It checked the task queue, found the alert, and evaluated it against triage rules. 47 of the 150 triage rules fired against this pattern. The rules classified it: severity = high (exact comparison: 152/1000 > 100/1000, the SLA threshold stored as exact fraction 1/10). The rules identified candidate causes from the correlation KB: recent deploys (query against `root.ops.deploys`), database health (query against `root.ops.metrics.health`), upstream dependency status. All of this happened through Prolog unification over exact facts. Zero LLM tokens.

The poller enqueued an investigation task and pushed a notification to the review queue. The internal processor, on its next 5-minute cycle, created an inference notebook KB at `root.ops.incidents.inc_2026_0519_001` using the SRE template. It populated the notebook with: the alert fact, the triage results, the candidate causes, the relevant service topology (mounted read-only from `root.ops.services`), and the current metric window (mounted read-only from `root.ops.metrics`).

93% of what a conventional LLM would spend its first 5-10 turns doing — reading logs, identifying the service, checking thresholds, listing possible causes, asking what was deployed recently — is already done. At zero LLM cost. Stored as exact facts at integer addresses.

### The investigation: engineer opens interactive session

**Turn 1:**

The engineer opens a chat. The interactive runner (C2) activates with the engineer's authenticated grants. The system checks for pending notifications. There's one: incident notebook `inc_2026_0519_001` has been created with auto-triage results.

The LLM's context contains: the notification (a few facts from the notebook), the engineer's preferences from their account KB, and the current active scope. Not 8,000 tokens of logs. Not 35,000 tokens of accumulated conversation. A handful of facts at integer addresses.

The LLM generates: "Checkout-api incident detected 3 minutes ago. Auto-triage completed." Then it emits command tokens:

`DIRECT_OUTPUT kb://root.ops.incidents.inc_2026_0519_001.triage_summary`

The rendering layer fetches the triage summary from the integer address, formats it through the SRE triage grammar (pipes, headers, status indicators — all structural tokens from the grammar, zero LLM generation), and injects it into the output stream. The LLM's prose wraps around it: "Three candidate causes ranked by rule confidence. Recent deploy of payment-service 14 minutes ago correlates with onset."

Total LLM tokens: ~40 for judgment and prose. The triage table: ~0 LLM tokens (grammar + KB data). The engineer sees a complete incident summary with ranked causes, exact confidence fractions, and provenance for every claim.

**Turn 2:**

Engineer: "Dig into the payment-service deploy correlation."

The LLM assesses: this is a deductive investigation step. It emits:

```
KB_QUERY root.ops.deploys filter(service=payment_service, timestamp > 1747611600)
KB_QUERY root.ops.metrics.prometheus filter(service=checkout_api, metric=error_rate, timestamp > 1747611600)
```

Two command tokens, ~16 LLM tokens total. The primitive executor resolves the paths to integer IDs, runs Prolog queries against the fact stores, returns results to the LLM's scratchpad (a ring buffer at `root.sessions.active.scratchpad`, VDR-8 DC7).

The scratchpad now contains: deploy facts (version, timestamp, deployer, change description — all exact facts) and error rate time series (exact fractions at exact timestamps). The LLM examines the scratchpad and generates:

```
PURE_FN vdr_compare(deploy_timestamp, error_spike_onset)
```

One command token, ~8 LLM tokens. The primitive computes: deploy at timestamp X, error spike onset at timestamp Y, difference = exact fraction. The LLM judges: "Payment-service deploy preceded error spike by 127 seconds. Temporal correlation: strong."

It formalizes this as a finding:

```
KB_ASSERT root.ops.incidents.inc_2026_0519_001.findings 
  fact(temporal_correlation, payment_deploy_v2_14_3, checkout_api_503_spike, 
       lag_seconds=127, confidence=92/100)
```

The confidence 92/100 is computed from the propagation rules: Prometheus metric source (95/100) × temporal alignment factor (97/100) = 92/100. Exact fractions, declared formula, stored with provenance.

Total turn 2: ~32 LLM tokens. Two KB queries, one arithmetic comparison, one fact assertion. The KB now has a finding with exact provenance. No re-reading of any prior context. The deploy facts were at integer addresses before the engineer asked. The metrics were at integer addresses before the engineer asked. The query accessed them in O(1).

**Turn 3:**

Engineer: "What changed in that deploy?"

The LLM emits:

```
KB_QUERY root.ops.deploys.payment_service_v2_14_3 field(change_description)
```

The deploy KB has the change description as a compacted fact — it was compacted from the deploy pipeline by the processor runner when the deploy happened. If the description references code changes, the LLM might need to look at the diff. It emits:

```
OP_FN fs_read /vdr/deploys/payment_service/v2.14.3/diff.patch 
  grant=sre_engineer_1.filesystem_read
```

The grant system checks: does `sre_engineer_1` have a filesystem_read grant covering `/vdr/deploys/`? Yes — it's in their account KB, issued by admin, currently valid, uses remaining > 0. The grant is decremented. The file is read. The content lands in the scratchpad, not the token stream.

The diff is 2,000 lines. In conventional LLM: stuffed into context, 8,000 tokens, re-read on every subsequent turn. In VDR-LLM-Prolog: it's in the scratchpad ring buffer. The LLM needs to find the relevant changes. It emits:

```
PURE_FN string_filter(scratchpad.diff, contains="connection_pool")
PURE_FN string_filter(scratchpad.diff, contains="timeout")
PURE_FN string_filter(scratchpad.diff, contains="retry")
```

Three pure primitive calls, ~24 LLM tokens. The primitives scan the 2,000-line diff at compiled code speed and return matching lines. Maybe 15 lines match. Those 15 lines are what the LLM actually reads through attention. Not 2,000 lines. Not 8,000 tokens. 15 lines, ~60 tokens.

The LLM judges: "Connection pool max size reduced from 50 to 20 in payment-service v2.14.3. This would cause connection exhaustion under load, manifesting as 503s on downstream checkout-api."

It formalizes:

```
KB_ASSERT root.ops.incidents.inc_2026_0519_001.findings
  fact(root_cause_candidate, connection_pool_reduction, 
       service=payment_service, version=v2_14_3, 
       parameter=max_pool_size, old_value=50, new_value=20,
       confidence=88/100)
```

And writes a Prolog rule:

```
KB_ASSERT root.ops.rules.correlation
  rule(connection_pool_change_causes_downstream_503,
       [deploy_changes_pool_size(Service, _, NewSize), 
        NewSize < 30,
        downstream(Service, Downstream),
        error_rate_high(Downstream)],
       root_cause(connection_pool_undersized, Service))
```

That rule cost ~35 tokens to formalize. Next time any service has a deploy that changes connection pool size below 30 and a downstream service starts throwing 503s, this rule fires automatically. L3. Zero LLM tokens. Forever.

Total turn 3: ~80 LLM tokens. A filesystem read (grant-gated, logged), three string filters (pure, exact, nanoseconds), judgment on 15 lines not 2,000, a finding stored with exact confidence, a reusable rule created.

**Turn 4:**

Engineer: "Verify — show me checkout-api's dependency on payment-service and current connection metrics."

The LLM emits:

```
KB_QUERY root.ops.services.checkout_api field(dependencies)
KB_QUERY root.ops.metrics.prometheus 
  filter(service=payment_service, metric=active_connections)
KB_QUERY root.ops.metrics.prometheus 
  filter(service=payment_service, metric=connection_pool_exhaustion)
```

Three queries, ~24 LLM tokens. The dependency graph is a fact in the service KB — it was compacted from service documentation months ago. The connection metrics are exact fractions continuously updated by the Prometheus processor runner.

Results come back. The LLM sees: checkout-api depends on payment-service (fact, confidence 1/1 — it's a KB fact, not LLM-generated). Active connections: 20/20 (exact fraction — pool is fully saturated). Connection pool exhaustion events: 847 in last 20 minutes (exact integer counter).

The LLM doesn't need to hedge. It emits:

```
DIRECT_OUTPUT kb://root.ops.incidents.inc_2026_0519_001.findings
```

The findings table — including the temporal correlation from turn 2 and the root cause candidate from turn 3 — is rendered through the SRE findings grammar. Every pipe, every header, every confidence fraction formatted by the grammar. The LLM wraps it: "Root cause confirmed. Payment-service v2.14.3 reduced connection pool from 50 to 20. Pool is 100% saturated (20/20). 847 exhaustion events in 20 minutes. Checkout-api's dependency on payment-service is a documented fact in the service topology."

The engineer sees exact numbers, exact provenance, exact confidence. No "approximately" or "it appears." The JSON dependency data was dumped by the builtin, formatted by the grammar. It cannot be malformed.

Total turn 4: ~30 LLM tokens for queries and judgment. The verification data was already at integer addresses. The queries are Prolog unification over exact facts. The output is grammar-formatted KB data.

**Turn 5:**

Engineer: "Write a remediation script to increase the pool size and a monitoring script to verify recovery."

The LLM exercises judgment — this is L1 work, genuine creative output. It writes a Python script:

```python
# Remediation: update payment-service connection pool
import requests
config = {"max_pool_size": 50}
resp = requests.patch(
    "https://config.internal/payment-service/v2.14.3/pool",
    json=config, headers={"Authorization": f"Bearer {TOKEN}"}
)
print(f"Status: {resp.status_code}")
```

And a monitoring script:

```python
# Verify recovery: poll checkout-api error rate
import time, requests
for i in range(30):
    resp = requests.get("https://metrics.internal/checkout-api/error_rate")
    rate = resp.json()["value"]
    print(f"Minute {i}: error_rate={rate}")
    if float(rate) < 0.01:
        print("Recovery confirmed")
        break
    time.sleep(60)
```

The LLM emits:

```
OP_FN env_upload docker_sre_sandbox /scripts/remediate_pool.py 
  content=<script1> grant=sre_engineer_1.execute
OP_FN env_upload docker_sre_sandbox /scripts/monitor_recovery.py 
  content=<script2> grant=sre_engineer_1.execute
```

The scripts are uploaded to a Docker sandbox environment (EN2 — strong isolation). Not executed yet. The LLM informs the engineer: "Scripts uploaded to sandbox. Remediation script restores pool size to 50. Monitoring script polls error rate for 30 minutes. Execute?"

This is judgment: the LLM decided what scripts to write, what parameters to use, and presented them for human approval before execution. The scripts are stored in the KB with provenance:

```
KB_ASSERT root.ops.scripts
  fact(script, remediate_pool_v2_14_3, 
       path=/scripts/remediate_pool.py,
       author=sre_engineer_1, session=inc_2026_0519_001,
       created_at=turn_5)
```

Total turn 5: ~120 LLM tokens — the most expensive turn because it's genuine creative work. Script writing is judgment. The upload and storage are command tokens.

**Turn 6:**

Engineer: "Execute remediation."

```
OP_FN env_exec docker_sre_sandbox /scripts/remediate_pool.py
  grant=sre_engineer_1.execute await=true
```

One command token, ~8 LLM tokens. The grant system verifies the execute grant. The Docker environment runs the script. Output: "Status: 200". The LLM reports: "Pool size restored to 50. Starting monitoring."

```
OP_FN env_exec docker_sre_sandbox /scripts/monitor_recovery.py
  grant=sre_engineer_1.execute await=false notify=true
```

The monitoring script runs asynchronously. The LLM doesn't wait. It tells the engineer: "Monitoring running in background. I'll notify you when recovery is confirmed or if it fails."

Meanwhile, the Prometheus processor runner is independently updating metrics at `root.ops.metrics.prometheus`. The internal processor is independently computing derived trends. When the error rate drops, these systems will detect it through their normal operation — not because the investigation told them to, but because that's what they do every cycle.

Total turn 6: ~20 LLM tokens.

**Turn 7 (10 minutes later):**

The monitoring script has been pushing output chunks to the task KB. The polling runner detected: monitoring task completed, recovery confirmed at minute 8. It pushed a notification.

The LLM checks notifications on the next turn:

"Recovery confirmed. Error rate dropped below 1% at minute 8 post-remediation. Checkout-api error rate now 3/1000."

3/1000 — exact fraction from the Prometheus processor. Not "approximately 0.3%." The comparison against the SLA threshold: 3/1000 < 1/10. Exact integer comparison. The SLA is met.

The LLM closes the investigation:

```
KB_ASSERT root.ops.incidents.inc_2026_0519_001
  fact(status, resolved, timestamp_1747613520)
  fact(root_cause, connection_pool_reduction, 
       service=payment_service, version=v2_14_3)
  fact(remediation, pool_size_restored, 50)
  fact(time_to_resolution, minutes=12)
  fact(rule_created, connection_pool_change_causes_downstream_503)
```

The investigation notebook is frozen. All facts, findings, rules, scripts persist. The notebook is queryable forever. The rule created in turn 3 is live in `root.ops.rules.correlation` and will fire on the next matching pattern.

Total turn 7: ~25 LLM tokens.

### The full investigation accounting

Seven turns. Total LLM tokens: ~40 + 32 + 80 + 30 + 120 + 20 + 25 = **347 LLM tokens**.

Of those 347 tokens: ~120 were script generation (genuine creative judgment). ~80 were prose framing around KB data. ~100 were command tokens (primitive invocations, KB queries, file operations). ~47 were assessment and formalization.

The system also consumed: ~0 tokens for auto-triage (93% rule-handled). ~0 tokens for metric collection (processor runners). ~0 tokens for trend analysis (internal processor). ~0 tokens for the triage summary formatting (grammar). ~0 tokens for the findings table formatting (grammar). ~0 tokens for the JSON dependency data (DIRECT_OUTPUT from KB).

**What persists after the investigation:**

- One new correlation rule (fires forever at zero cost)
- Two reusable scripts (re-executable at 8 tokens each)
- A complete incident record with exact provenance
- Updated service KB facts if anything was learned about the topology
- The frozen notebook, queryable for future reference

**What happens at investigation 2 with a similar pattern:**

The correlation rule from investigation 1 fires during auto-triage. The poller checks: was there a recent deploy that changed connection pool size? If yes and downstream errors are high, the rule matches. Auto-triage identifies the root cause before the engineer is notified. The engineer's turn 1 says "Auto-triage identified root cause: connection pool change in [service]. Remediation script from incident 001 is available. Execute?"

Investigation 2 might be 3 turns and 50 tokens. The rule did the work.

**What happens at investigation 100:**

150+ rules cover 93% of triage patterns. The internal processor detects the incident, auto-triage identifies the cause, auto-remediation executes the stored script (if the rule's confidence exceeds the auto-execute threshold and the appropriate grant exists), and the engineer gets a notification: "Incident detected, triaged, and remediated. Error rate recovered. Please review."

55 tokens. The engineer spends 30 seconds reviewing instead of 30 minutes investigating.

### Why it never degrades

The session at turn 7 used the same amount of LLM attention as turn 1. The LLM's context window contained: the current turn's query, a handful of facts from the scratchpad, and the active scope chain. Not the accumulated history of 7 turns. Not the 2,000-line diff. Not the logs. Not the previous findings. Those are all at integer addresses in the KB, accessible in O(1), exact, and permanent.

At turn 700, the same. At turn 7,000, the same. The bounded data primitives can't overflow — the LRU pushes old entries out, the queue has a fixed capacity, the counters clamp at bounds. The KB facts are integers at integer addresses — fact 47 at address 47 returns exactly what was asserted, whether it was asserted 1 turn ago or 10,000 turns ago. The Prolog rules don't degrade — they're exact pattern matches over exact facts. The grammars don't degrade — they're structural templates.

The clone drift thresholds (turns < 200, context < 90%, denominator < 2^48, error < 5%) are guardrails that never need to fire for the interactive session because the LLM's context never grows. They exist for the processor runners that maintain persistent connections and might accumulate working state over long periods. When a processor hits 200 turns, it snapshots, dies, and a fresh clone continues. The knowledge survives. The drift dies.

The JSON can never be malformed because the LLM never generates JSON. The grammar generates JSON. The grammar's template was validated at creation. The data values come from KB facts at integer addresses. The grammar fills slots in a syntactically valid template with exact values. There is no path through which a mismatched bracket or missing comma can enter the output. The LLM's contribution is: "I judge that this data should be shown to the user now." The grammar's contribution is: every structural token, correct, every time.

---

## Non-Mature SRE: First Investigation on a Fresh System

No accumulated rules. No processor runners watching streams. No months of compacted service topology. The system was deployed this week. The KB tree has the seed layers from VDR-19 (language templates, format grammars, operational rules, self-maintenance rules — ~23,400 entries, ~1.5MB, loaded in <620ms) and the OSO principles at `root.system.oso` (176 Prolog terms). Nothing else. This is day 3.

The engineer has an account KB at `root.users.sre_eng_1` with grants issued by admin during setup: filesystem read/write on `/vdr/`, execute on docker sandbox, network fetch to internal APIs (Prometheus, deploy pipeline, config service). These are facts in the account KB with expiration, use limits, and provenance.

The KB tree is nearly empty:

```
root
├── system
│   └── oso (seed: 176 Prolog terms)
├── ops
│   └── (empty — no services, no metrics, no rules, no incidents)
└── users
    └── sre_eng_1 (grants, preferences)
```

The engineer gets paged. Checkout-api is returning 503s.

**Turn 1:**

Engineer: "Checkout-api is throwing 503s at about 15% for the last 20 minutes. Help me investigate."

The LLM has no service topology KB. No metrics KB. No triage rules. No prior incidents. It's starting from zero. But it has 448 builtins, grants to reach internal systems, and judgment.

It assesses: I need data. I have no internal state about this service. I need to acquire it. The OSO principles (OP2, knowability spectrum) tell it: Prometheus metrics = 95/100 confidence, direct observation of a controlled system. That's the highest-confidence external source available.

The LLM creates the investigation structure first:

```
KB_ASSERT root.ops fact(kb_type, operations_root)
KB_ASSERT root.ops.incidents fact(kb_type, incidents_root)
KB_ASSERT root.ops.incidents.inc_001 
  fact(service, checkout_api)
  fact(symptom, http_503)
  fact(reported_rate, 15/100)
  fact(onset_minutes_ago, 20)
  fact(status, investigating)
  fact(opened_at, 1747612800)
```

Six KB_ASSERT commands, ~48 LLM tokens. The system now has an incident KB with exact facts. The reported rate is 15/100 — the engineer said "about 15%" and the LLM formalized it as an exact fraction. The "about" is captured by the confidence: this is user-stated (70/100 per knowability spectrum), not measured.

Now it needs real data:

```
OP_FN net_fetch https://prometheus.internal/api/v1/query
  params={"query": "rate(http_responses_total{service='checkout-api',code='503'}[5m])"}
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.prometheus_raw
```

One operational primitive, ~12 LLM tokens. The grant system checks: does sre_eng_1 have a network grant covering `prometheus.internal`? Yes. Grant valid, not expired, uses remaining. Decremented. Logged. The fetch executes. The response — JSON with metric data — lands at the KB address `root.ops.incidents.inc_001.prometheus_raw`. Not in the context window. At an integer address.

The LLM needs to parse the response:

```
PURE_FN parse_json(root.ops.incidents.inc_001.prometheus_raw)
  store_result=root.ops.incidents.inc_001.prometheus_parsed
```

One pure primitive, ~8 LLM tokens. The JSON parser is compiled code. It cannot fail to parse valid JSON. It cannot produce malformed output. The parsed structure lands at another integer address.

Now the LLM reads the parsed metrics from the scratchpad. The actual error rate from Prometheus: 152/1000. The LLM asserts:

```
KB_ASSERT root.ops.incidents.inc_001
  fact(measured_error_rate, 152/1000, source=prometheus, confidence=95/100)
```

The engineer's estimate of 15/100 and the measured 152/1000 are both in the KB. The LLM reports: "Confirmed via Prometheus. Checkout-api 503 rate is 152/1000 over the last 5 minutes. Measured confidence 95/100."

No hedging. No "appears to be." An exact fraction from a known source with declared confidence.

Total turn 1: ~80 LLM tokens. The system went from empty to having an incident KB with measured metrics. Every fact has provenance. The structure was created by the LLM's judgment about what to investigate and how to organize it.

**Turn 2:**

Engineer: "What depends on checkout-api and what does it depend on?"

The LLM has no service topology KB. It needs to acquire this. It judges: the engineer's organization probably has this information somewhere accessible. It could ask the engineer to paste it, but it has network grants. The OSO principle OP4 (personal experience vs hearsay) says: verify personally when possible.

```
OP_FN net_fetch https://config.internal/api/services/checkout-api
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.service_config_raw
PURE_FN parse_json(root.ops.incidents.inc_001.service_config_raw)
  store_result=root.ops.incidents.inc_001.service_config
```

Two commands, ~16 LLM tokens. The config service returns checkout-api's service definition including dependencies. The LLM reads the parsed config from the scratchpad and creates the service KB:

```
KB_ASSERT root.ops.services fact(kb_type, service_registry)
KB_ASSERT root.ops.services.checkout_api
  fact(depends_on, payment_service)
  fact(depends_on, inventory_service)
  fact(depends_on, db_primary)
  fact(depended_on_by, web_frontend)
  fact(depended_on_by, mobile_api)
  fact(sla, 999/1000)
  fact(team, platform_team)
```

Seven assertions, ~56 LLM tokens. This is more expensive than the mature system where this data already exists. That's the cost of day 3. But it only happens once. These facts are now permanent. Next investigation, the service topology is already there.

The LLM also fetches dependency configs for payment-service and inventory-service while it's at it — two more net_fetch + parse_json pairs:

```
OP_FN net_fetch https://config.internal/api/services/payment-service
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.payment_config_raw
PURE_FN parse_json(root.ops.incidents.inc_001.payment_config_raw)
OP_FN net_fetch https://config.internal/api/services/inventory-service  
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.inventory_config_raw
PURE_FN parse_json(root.ops.incidents.inc_001.inventory_config_raw)
```

Four more commands, ~32 LLM tokens. The dependency tree is populating. The LLM creates service KBs for both and reports to the engineer:

"Checkout-api depends on payment-service, inventory-service, and db-primary. It's depended on by web-frontend and mobile-api. SLA is 999/1000. Checking health of all three dependencies now."

Then immediately:

```
OP_FN net_fetch https://prometheus.internal/api/v1/query
  params={"query": "rate(http_responses_total{service='payment-service',code=~'5..'}[5m])"}
  grant=sre_eng_1.network_fetch
OP_FN net_fetch https://prometheus.internal/api/v1/query
  params={"query": "rate(http_responses_total{service='inventory-service',code=~'5..'}[5m])"}
  grant=sre_eng_1.network_fetch
OP_FN net_fetch https://prometheus.internal/api/v1/query
  params={"query": "up{service='db-primary'}"}
  grant=sre_eng_1.network_fetch
```

Three fetches, ~24 LLM tokens. The LLM didn't wait for the engineer to tell it to check dependencies. The OSO principle OP1 (control is foundation) and the seed layer operational rules (~80 primitive selection rules) include a pattern: when investigating a service error, check health of dependencies. This seed rule didn't fire automatically at L3 because the system doesn't have Prolog facts matching the rule's prerequisite pattern yet — it just built the service topology this turn. But the LLM knows the rule exists in the seed layer and follows it as guidance. This is L1: full judgment informed by seed rules.

Results come back. Payment-service: error rate 45/1000. Inventory-service: error rate 2/1000. Database: up.

The LLM judges: payment-service error rate is elevated. Inventory and database are healthy. The correlation is between checkout-api and payment-service.

```
KB_ASSERT root.ops.incidents.inc_001
  fact(dependency_health, payment_service, error_rate=45/1000, status=degraded, confidence=95/100)
  fact(dependency_health, inventory_service, error_rate=2/1000, status=healthy, confidence=95/100)
  fact(dependency_health, db_primary, status=up, confidence=95/100)
  fact(correlation_candidate, payment_service, reason=elevated_errors, confidence=85/100)
```

The confidence on the correlation candidate is 85/100: two Prometheus metrics (95/100 each) combined with temporal alignment (the LLM's assessment of correlation, which as LLM judgment gets 30/100) — but the propagation formula for multiple agreeing sources is 1-∏(1-Cᵢ). Two 95/100 sources agreeing: 1-(1-95/100)² = 1-1/400 = 399/400. The LLM's correlation judgment at 30/100 is a separate factor. Combined: the exact fraction is computed by the confidence propagation builtins, not generated as hedging language.

Total turn 2: ~140 LLM tokens. Expensive — this is day 3, the system is acquiring and organizing data for the first time. A mature system already has this. But every fact asserted here is permanent and exact.

**Turn 3:**

Engineer: "Check recent deploys for payment-service."

```
OP_FN net_fetch https://deploy.internal/api/deployments?service=payment-service&limit=5
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.deploys_raw
PURE_FN parse_json(root.ops.incidents.inc_001.deploys_raw)
  store_result=root.ops.incidents.inc_001.deploys
```

Two commands, ~16 LLM tokens. The deploy API returns recent deployments. The LLM reads the parsed data and finds: payment-service v2.14.3 deployed 34 minutes ago. The change description mentions "optimize connection pool settings."

```
KB_ASSERT root.ops.deploys fact(kb_type, deploy_registry)
KB_ASSERT root.ops.deploys.payment_v2_14_3
  fact(service, payment_service)
  fact(version, v2_14_3)
  fact(deployed_at, 1747611960)
  fact(deployer, dev_engineer_3)
  fact(change_description, "optimize connection pool settings")
PURE_FN vdr_sub(1747612800, 1747611960)
  store_result=root.ops.incidents.inc_001.deploy_lag
```

The subtraction primitive returns: 840. Deploy preceded incident onset by 840 seconds (14 minutes). Exact integer arithmetic. The LLM asserts:

```
KB_ASSERT root.ops.incidents.inc_001
  fact(temporal_correlation, payment_v2_14_3, checkout_api_503, 
       lag_seconds=840, confidence=90/100)
```

The LLM reports: "Payment-service v2.14.3 deployed 14 minutes before incident onset. Change description references connection pool optimization. Strong temporal correlation."

Now it wants to see what actually changed. The deploy API might have a diff endpoint, or the LLM might need to fetch the config diff:

```
OP_FN net_fetch https://config.internal/api/services/payment-service/config/diff
  params={"from": "v2.14.2", "to": "v2.14.3"}
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.config_diff_raw
PURE_FN parse_json(root.ops.incidents.inc_001.config_diff_raw)
  store_result=root.ops.incidents.inc_001.config_diff
```

The diff shows: `max_pool_size: 50 → 20`. The LLM reads this from the scratchpad. 30 tokens of actual content, not 2,000 lines.

```
KB_ASSERT root.ops.incidents.inc_001
  fact(config_change, payment_service, v2_14_3, max_pool_size, old=50, new=20)
  fact(root_cause_candidate, connection_pool_reduction,
       service=payment_service, parameter=max_pool_size,
       old_value=50, new_value=20, confidence=88/100)
```

The LLM generates output for the engineer. It emits:

```
DIRECT_OUTPUT kb://root.ops.incidents.inc_001.findings
```

But wait — there's no findings grammar yet. This is day 3. The system's seed layer SL2 has a generic table grammar. The rendering layer falls back to the generic pipe-delimited format grammar. The output is still structurally valid — the grammar provides pipes and headers — but it's not the polished SRE-specific format the mature system would have.

The LLM notices this and creates one:

```
KB_ASSERT root.ops.grammars
  fact(grammar_rule, sre_findings_table,
       slots=[id, finding, service, evidence, confidence, timestamp],
       template="| {id} | {finding} | {service} | {evidence} | {confidence} | {timestamp} |",
       requires=[has_table(findings)],
       best_when=[incident_investigation])
```

~30 LLM tokens to create the grammar. It now exists at `root.ops.grammars` and will be inherited by all child KBs. Every future investigation's findings table uses this grammar at zero LLM cost. The grammar was created once as an act of judgment. It executes forever as deterministic structure.

Total turn 3: ~110 LLM tokens. Data acquisition, temporal correlation via exact arithmetic, config diff analysis, root cause candidate, and a grammar created for future use.

**Turn 4:**

Engineer: "That's probably it. Can you verify by checking current connection pool utilization on payment-service?"

```
OP_FN net_fetch https://prometheus.internal/api/v1/query
  params={"query": "payment_service_connection_pool_active / payment_service_connection_pool_max"}
  grant=sre_eng_1.network_fetch
  store_result=root.ops.incidents.inc_001.pool_util_raw
PURE_FN parse_json(root.ops.incidents.inc_001.pool_util_raw)
```

Two commands, ~16 LLM tokens. Result: pool utilization is 20/20. Fully saturated. The LLM converts to VDR for exact comparison:

```
PURE_FN vdr_div(20, 20)
```

Result: 1/1. Pool is at 100% capacity. That's not "approximately full" — it's exactly full. The integer comparison 20/20 = 1/1 is exact.

```
KB_ASSERT root.ops.incidents.inc_001
  fact(verification, pool_saturation, payment_service, 
       active=20, max=20, utilization=1/1, confidence=95/100)
```

The LLM upgrades the root cause confidence:

```
KB_ASSERT root.ops.incidents.inc_001
  fact(root_cause, connection_pool_reduction,
       service=payment_service, version=v2_14_3,
       parameter=max_pool_size, old_value=50, new_value=20,
       pool_utilization=1/1, downstream_impact=checkout_api_503,
       confidence=94/100)
```

94/100: Prometheus metric (95/100), temporal correlation (90/100), config change evidence (95/100), pool saturation verification (95/100). Multiple agreeing sources: 1-∏(1-Cᵢ) = 1-(5/100)⁴ = 1-625/100000000 = 99999375/100000000. Capped by the weakest individual link and the LLM's correlation assessment. The exact fraction is computed by builtins, not estimated.

The LLM reports with the findings table rendered through the grammar it created last turn.

Total turn 4: ~35 LLM tokens.

**Turn 5:**

Engineer: "Fix it. Bump the pool back to 50 and write me a monitoring check."

The LLM writes scripts. This is L1 judgment — creative work:

```python
# remediate_pool.py
import requests
resp = requests.patch(
    "https://config.internal/api/services/payment-service/config",
    json={"max_pool_size": 50},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
print(f"Status: {resp.status_code}")
print(f"New config: {resp.json()}")
```

```python
# monitor_recovery.py  
import time, requests
for i in range(20):
    r1 = requests.get("https://prometheus.internal/api/v1/query",
        params={"query": "rate(http_responses_total{service='checkout-api',code='503'}[1m])"})
    rate = r1.json()["data"]["result"][0]["value"][1]
    print(f"Minute {i}: checkout_api_503_rate={rate}")
    if float(rate) < 0.01:
        print("RECOVERED")
        break
    time.sleep(60)
```

```
OP_FN env_upload docker_sre_sandbox /scripts/remediate_pool.py
  content=<script1> grant=sre_eng_1.execute
OP_FN env_upload docker_sre_sandbox /scripts/monitor_recovery.py
  content=<script2> grant=sre_eng_1.execute
```

The LLM also writes the first Prolog rule this system has ever had beyond the seed:

```
KB_ASSERT root.ops.rules fact(kb_type, operational_rules)
KB_ASSERT root.ops.rules.triage
  rule(pool_reduction_causes_downstream_503,
       [config_change(Service, _, max_pool_size, _, NewSize),
        NewSize < OldSize,
        depends_on(Downstream, Service),
        error_rate_high(Downstream, Rate),
        Rate > 1/10],
       [root_cause(connection_pool_undersized, Service),
        severity(high),
        remediation(restore_pool_size, Service, OldSize)])
```

And a Python script stored for reuse:

```
KB_ASSERT root.ops.scripts
  fact(script, remediate_pool_generic,
       path=/scripts/remediate_pool.py,
       parameters=[service, pool_size],
       author=sre_eng_1, investigation=inc_001)
```

Total turn 5: ~150 LLM tokens. The most expensive turn — two scripts, one Prolog rule, KB assertions for all of them. But the rule and scripts are permanent. They're the system's first self-extension beyond the seed.

**Turn 6:**

Engineer: "Run it."

```
OP_FN env_exec docker_sre_sandbox /scripts/remediate_pool.py
  grant=sre_eng_1.execute await=true
```

Output: Status 200, new config confirmed. ~8 LLM tokens.

```
OP_FN env_exec docker_sre_sandbox /scripts/monitor_recovery.py
  grant=sre_eng_1.execute await=false notify=true
```

Monitoring runs async. ~8 LLM tokens. The LLM reports: "Pool restored to 50. Monitoring checkout-api recovery. I'll notify you."

Total turn 6: ~20 LLM tokens.

**Turn 7:**

Monitoring completes. Recovery confirmed at minute 6. The LLM closes the investigation:

```
KB_ASSERT root.ops.incidents.inc_001
  fact(status, resolved, 1747613520)
  fact(resolution, pool_size_restored_to_50)
  fact(time_to_resolution_minutes, 12)
  fact(artifacts_created, rule=pool_reduction_causes_downstream_503,
       script=remediate_pool_generic, script=monitor_recovery,
       grammar=sre_findings_table)
```

The LLM also does something the mature system already had: it suggests creating processor runners.

"This investigation would have been faster with automated metric collection. I can set up a Prometheus polling runner to maintain continuous metrics at `root.ops.metrics`. Want me to configure that?"

This is judgment about system improvement. If the engineer agrees, the next session will have live metrics. The system bootstraps toward the mature state through usage.

Total turn 7: ~35 LLM tokens.

### Non-mature investigation accounting

Seven turns. Total LLM tokens: 80 + 140 + 110 + 35 + 150 + 20 + 35 = **570 LLM tokens**.

More expensive than the mature system's 347. That's correct — the non-mature system is acquiring data, building KB structure, creating its first rule and grammar. It's doing double duty: investigating AND building infrastructure for future investigations.

But compare to conventional: 25,100 tokens for the same investigation, degrading quality, no persistent artifacts, no reusable rules, no exact computations, context window filling up, re-reading everything every turn.

570 vs 25,100. That's 44× on day 3 with no accumulated rules.

**What the system gained from this one investigation:**

- Service topology for checkout-api, payment-service, inventory-service (permanent facts)
- Deploy registry structure (permanent)
- One triage rule (fires forever at zero cost)
- Two reusable scripts (re-executable at 8 tokens each)
- One SRE findings grammar (formats all future findings at zero cost)
- One complete incident record (frozen, queryable)
- A suggestion to create processor runners for continuous monitoring

**Investigation 2, same system, different incident:**

The service topology is already there. The deploy registry structure exists. The findings grammar exists. The triage rule exists. If the next incident involves a pool size change, the rule fires immediately and the engineer's first turn gets "Auto-triage candidate: pool size reduction detected" even without processor runners.

Investigation 2 costs maybe 350 tokens. Investigation 5 costs 200. The system is walking the accumulation curve from VDR-19. By investigation 20, if the engineer has also set up processor runners, the system approaches the mature state described earlier. Not because someone configured it — because it built itself through the process of doing useful work.

The conventional LLM at investigation 20 still costs 25,100 tokens. Still re-reads everything. Still can't find the notes from investigation 1. Still hedges. Still gets arithmetic wrong sometimes. Still generates malformed JSON occasionally. Still can't tell you whether a number is exact or hallucinated.

