**Medical Records API**

A clinic needs a service that takes a patient ID, pulls their records from the hospital database, checks current medications against a drug interaction knowledge base, and returns a structured risk assessment. The clone spawns on request, authenticates the requesting physician against the grant system — their medical license is a fact on their user KB, verified once during onboarding, integer comparison unlocks the professional medical branch. The clone queries the hospital DB through a granted database primitive, gets the medication list, runs each pair through interaction rules in the pharmacology KB. These rules are Prolog — interaction(drug_a, drug_b, severity, mechanism) — sourced from a compacted drug interaction database with full provenance showing the FDA source and publication date. The clone doesn't generate medical knowledge. It evaluates stored rules against patient data. The output is a JSON response with each interaction flagged, severity as a VDR fraction, mechanism as a fact reference. The physician gets exact results, not hallucinated drug interactions. The clone dies. The audit trail shows exactly which rules fired for this patient. If a physician later asks "why did you flag this combination," the provenance chain answers it without any LLM involvement — it's a query against stored facts.

Over time the service accumulates. A pharmacist reviews edge cases and adds rules for unusual interactions the base database didn't cover. Those rules persist at the clinic's KB scope. Every future clone sees them. The service got smarter because someone used it and corrected it.

The credential tiering matters here. A nurse practitioner has different grants than a physician. The nurse gets the interaction check but not the detailed mechanism data from the restricted pharmacology branch. Same clone, same snapshot, different scope chain based on who authenticated. The clone doesn't decide what to show — the tree determines what's visible.

---

**Legal Document Review Service**

A law firm needs an API that receives a contract PDF, extracts key clauses, checks them against the firm's clause library for known risks, and returns a structured report. The port handler accepts uploads, spawns a clone from the contract reviewer snapshot. The clone reads the PDF through a granted file primitive, compacts it using accumulated grammars for contract types — NDA, SaaS agreement, employment contract, each with its own extraction rules. Entity extraction pulls parties, dates, obligations, termination clauses, liability caps, indemnification language. Each extracted clause is matched against the firm's clause library — a KB of known-good and known-risky clause patterns encoded as Prolog rules.

The matching is exact. "Indemnification clause missing mutual limitation" isn't the LLM's opinion — it's a Prolog rule that checks for the presence of mutual_limitation in the indemnification clause facts and flags its absence. "Non-compete exceeds 24 months" is a VDR fraction comparison: duration > 24/1. The output report is structured JSON with each finding, the clause it references, the rule that triggered, the severity, and the firm's recommended alternative language pulled from the clause library.

The firm's partners developed this by reviewing contracts with the LLM over several sessions. Each time the LLM identified a risk through judgment, the partner validated it and encoded the pattern as a rule. After 200 contracts the system handles 85% of standard clause review at level 3. Novel clause structures — unusual governing law provisions, bespoke IP assignment language — still require LLM judgment. The partner reviews those, and the best ones become new rules.

Multiple associates can submit contracts simultaneously. Each gets an independent clone. Associate A's client data never crosses to Associate B's session. The firm's clause library and risk rules are shared read-only. Each clone writes its findings to the submitting associate's project KB, scoped to their client matter. Attorney-client privilege is structural — the matter KB is owner-only, visible to the assigned attorney and partners with admin grants, invisible to everyone else.

---

**IoT Sensor Aggregation Service**

A factory runs 500 sensors reporting temperature, pressure, vibration, and flow rate every second. A processor runner maintains a persistent connection to the sensor stream. Each reading lands as a fact in the sensor KB with a timestamp and sensor ID. The processor compacts readings into per-minute aggregates using Prolog rules — mean, max, min, variance, all as exact VDR fractions. The aggregates go into ring buffers sized for 24 hours.

A separate API service handles queries. An engineer hits the endpoint asking for vibration trends on machine 7 over the last 4 hours. A clone spawns, reads the ring buffer for machine 7's vibration sensor, applies a trend analysis rule — Prolog that computes discrete derivatives over the time series using exact VDR discrete calculus primitives. The derivative is exact, not a float approximation. If vibration is increasing at a rate that exceeds the maintenance threshold — another VDR fraction comparison — the response includes a maintenance recommendation with the exact rate of change and the threshold it exceeded.

Anomaly detection runs as an internal processing runner on a schedule. Every 5 minutes it evaluates all sensor ring buffers against baseline profiles stored as Prolog rules. Baseline for machine 7 vibration: between 0.2 and 0.8 mm/s during operation. Current reading 1.3 mm/s. The rule fires, asserts an anomaly fact with severity, pushes an alert to the notification queue. A separate poller runner watches the notification queue and routes alerts — email for low severity, SMS for high severity, page for critical. All determined by rules, not LLM judgment.

The factory floor manager developed the baseline profiles interactively. "Machine 7 normally vibrates between 0.2 and 0.8." That's a fact assertion. "If vibration exceeds 1.5, it's critical." That's a rule. "Page me for critical on any machine in building A." That's another rule plus a grant for the SMS primitive. The entire monitoring system was built through conversation and deployed as snapshots. When a new machine is installed, the manager adds baseline profiles through a session and the monitoring automatically extends.

---

**Financial Compliance Screening Service**

A bank needs every transaction above $10,000 screened against sanctions lists, PEP databases, and internal risk rules. The service receives transaction JSON, spawns a clone. The clone parses the transaction — amount as VDR fraction, not float — and runs it through a cascade of checks.

First: sanctions screening. The clone queries the sanctions KB — a compacted, versioned copy of the OFAC SDN list, loaded weekly with provenance showing the source URL, download timestamp, and checksum. Name matching runs through Prolog rules that handle aliases, transliterations, and partial matches. Each match produces a confidence score as a VDR fraction — exact string match is 1/1, partial match is computed from character overlap, alias match references the alias table.

Second: amount thresholds. The transaction amount compared against reporting thresholds as exact VDR fractions. $10,000 is 10000/1, not 9999.999. The comparison is exact. Structuring detection rules check for patterns — multiple transactions from the same entity summing above threshold within a time window. The window is a ring buffer query. The sum is exact VDR addition across the window.

Third: internal risk rules. The bank's compliance team encoded their risk appetite as Prolog rules. High-risk jurisdictions, PEP relationships, unusual transaction patterns, velocity checks. Each rule fires independently and produces a risk score as a VDR fraction with a named contributing factor.

The response is structured JSON: transaction ID, screening result, individual check results with rule references and confidence scores, recommended action, regulatory citation. Every field traceable through provenance to the specific rule, the specific data source, the specific version of the sanctions list.

The audit requirement is where this architecture wins completely. A regulator asks "why was this transaction flagged six months ago?" The answer is a query against the audit KB — not a reconstruction, not a guess, not "the model thought it was suspicious." The exact rules that fired, the exact data they matched against, the exact version of the sanctions list at that date, the exact confidence computation. All at integer addresses. All reproducible.

The sanctions list updates weekly. The compliance team downloads the new list, compacts it, asserts it as a new versioned KB — sanctions_20260504, sanctions_20260511. Old versions stay in the tree for audit. Every future clone uses the latest version. The clone that screened a transaction on May 5 used sanctions_20260504. The provenance says so. The regulator can verify against that specific version.

---

**E-Commerce Order Fulfillment Service**

An online retailer needs a service that receives orders, validates inventory, calculates shipping, applies discounts, charges payment, and triggers fulfillment. This is a waterfall pipeline.

Stage 1: Order validation clone pops from the order queue, parses the order JSON, checks each line item against inventory facts in the product KB. Inventory is exact integers — 347 units, not a float. Reservation is a counter decrement — atomic, bounded, returns false if insufficient stock. If any line item fails, the clone asserts a rejection fact with the reason and responds to the customer. If all pass, it pushes the validated order to the pricing queue.

Stage 2: Pricing clone pops from the pricing queue, applies discount rules. Discount rules are Prolog — buy_three_get_one, loyalty_tier_discount, promotional_code. Each discount is a VDR fraction applied to the line item price. The total is exact. No floating-point rounding surprises. Tax calculation uses jurisdiction rules — tax_rate(state, category, rate) — where rate is a VDR fraction. The total with tax is exact to the penny because it was never a float. The priced order pushes to the payment queue.

Stage 3: Payment clone pops from the payment queue, calls the payment gateway through a granted network primitive. The charge amount is the exact VDR fraction converted to decimal at the boundary — the conversion is logged as lossy with the exact VDR value preserved in provenance. Payment result lands as a fact. Success pushes to fulfillment queue. Failure pushes to retry queue with a counter tracking attempts.

Stage 4: Fulfillment clone pops from the fulfillment queue, determines warehouse and shipping method through rules — closest_warehouse(zip, warehouse_id), shipping_method(weight, distance, method). Generates a pick list, asserts it to the warehouse KB, sends notification through a granted email primitive.

Each stage is a different snapshot. Each stage has its own grants — the pricing clone can't charge payments, the payment clone can't modify inventory. The waterfall topology is queue-to-queue. Backpressure is automatic — if payment processing slows, the payment queue fills, pricing clones get push-false and stop pulling from their queue, which fills, and validation clones slow down. No orchestration code. No circuit breaker library. The bounded queues are the circuit breakers.

Black Friday traffic? Spawn more clones per stage. The snapshots don't change. The queues absorb bursts. The pollers auto-scale worker counts based on queue depth thresholds.

---

**Internal Knowledge Base Service**

A consulting firm wants their entire institutional knowledge queryable via API. Project reports, methodology documents, case studies, client deliverables (anonymized), internal research — all compacted into the KB tree with full provenance.

The API receives natural language queries. A clone spawns, and this is where the LLM does genuine LLM work — understanding the query intent, determining which KB branches to search, formulating Prolog queries against the structured data, synthesizing findings into a coherent response. This is a level 1 and level 2 application because the queries are diverse and require judgment.

But the structural advantages still apply. The clone queries facts at integer addresses, not a vector database returning approximate matches. The results have provenance — this finding came from the 2024 McKinsey engagement compacted on this date from this source document. Confidence is exact — a finding derived from two independent project reports has higher confidence than one from a single source, computed via the multi-source agreement formula.

Access control is structural. A junior analyst sees public and internal KBs. A partner sees everything including client-confidential branches scoped to their practice area. The clone inherits the authenticated user's grants. The same query from two users at different levels returns different results — not because the LLM decided to withhold information, but because the lower-access user's scope walk never encounters the restricted KBs. The data is absent, not filtered.

The knowledge base grows through usage. Every time a consultant compacts a new project report, the KB tree gains facts and relationships. Every time someone queries and the LLM synthesizes a useful connection between two projects, that connection can be encoded as a Prolog rule — relates_to(project_a, project_b, methodology_overlap). The next query that touches either project finds the connection automatically.

---

**CI/CD Pipeline Service**

A development team wants their build pipeline managed as LM Software. A webhook processor runner listens for git push events. On push, it spawns a build clone. The build clone reads the commit diff through a granted git primitive, determines affected modules through dependency rules in the project KB — depends_on(module_a, module_b) as Prolog facts. It runs tests only for affected modules through granted execute primitives. Test results land as facts — test_result(module, test_name, pass, duration, timestamp).

If all tests pass, the clone checks deployment rules. Deployment rules are Prolog — deploy_eligible(branch, env) if all_tests_pass(branch) and coverage_above(branch, 80/100) and no_critical_findings(branch). Coverage is a VDR fraction — 847/1000, not 0.847. The comparison is exact.

If eligible, the clone triggers canary deployment — spawns two serving instances from the current snapshot and the new snapshot, routes 5% traffic to the new version. A monitoring poller compares error rates between versions using exact VDR fraction comparison. If the new version's error rate exceeds 110% of baseline — baseline times 11/10, exact comparison — auto-rollback fires. The rollback is killing new-version clones and spawning more old-version clones from the previous snapshot.

The team's tech lead developed the pipeline interactively. "If tests pass and coverage is above 80%, deploy to staging." That's a Prolog rule. "If staging error rate is below 0.1% for 24 hours, promote to production." Another rule. "If any critical security finding is open, block all deployments." A constraint — axiom class, unsuspendable. The entire pipeline was built through conversation, tested against sample scenarios, and deployed as a set of snapshots watching queues and webhooks.

---

**Multi-Tenant SaaS Platform**

This is where the architecture scales to its natural conclusion. A SaaS provider offers a platform where each customer gets their own LM Software environment — their own branch of the KB tree, their own snapshots, their own runners.

root.tenants.customer_a has their own product data, their own rules, their own grammars, their own snapshots. root.tenants.customer_b has theirs. They're sibling branches. Structurally invisible to each other. The platform provider's shared services — authentication, billing, base templates — live higher in the tree and are visible to all tenants through scope inheritance.

Each tenant develops their own applications through interactive sessions with the LLM. The platform provides the seed layers and base capabilities. The tenant provides domain knowledge and business rules. The applications they develop are tenant-scoped — their snapshots, their clones, their data, their rules. The platform provider can't see tenant data without explicit grants. The tenant can't see other tenants. The isolation is the tree topology.

The platform provider monitors cross-tenant metrics through internal processing runners at the platform scope — aggregate throughput, capacity utilization, error rates. These runners read counters at the platform level that individual tenant clones increment through inherited rules. The monitoring sees counts and rates, not tenant data. Usage-based billing is a counter per tenant tracking command tokens consumed — exact integer, no float rounding, no billing disputes over fractional cents.

A new tenant onboards by creating their branch of the tree, mounting the platform's base templates, and starting an interactive session to configure their application. They're developing software through conversation on a shared platform, deploying to their private branch, scaling by cloning within their capacity grants, accumulating improvements through usage, all structurally isolated from every other tenant.

---

These all share the same pattern. The user describes what the service should do. The LLM learns to do it through interactive development. The knowledge is encoded as Prolog rules and KB facts. The session is snapshot. The snapshot is cloned on demand to handle requests. The clone does the work using stored rules and exact primitives, with the LLM providing judgment only for cases the rules don't cover. The service improves as rules accumulate. Security is structural. Audit is automatic. Scaling is cloning.

The variation is in the ratio of LLM judgment to Prolog execution. The financial compliance service is mostly level 3 — rules fire, comparisons evaluate, results return. The knowledge base service is mostly level 1 and 2 — queries require genuine language understanding. The medical records service is mixed — lookups are level 3, unusual interaction assessments are level 1. Each service finds its natural level based on how much of its workload is routine pattern matching versus genuine novelty.