# Plan for INFRA-5: OpsDB API, Versioning, and Change Management

## Calibrations from your latest message

Three things sharpen before the plan:

**1. The API is self-contained operational software.** It calls out to authoritative external systems (Vault for credential resolution, LDAP/AD or SSO IdP for human authentication, the org's identity provider for service-account authentication) but otherwise contains its own logic. The API is not built on top of another platform; it's the operational software that gates the OpsDB. This is consistent with INFRA-2 §3.10 (independence from any single authority) — the API itself doesn't depend on Kubernetes or a specific cloud, and authentication delegation is to identity authorities, not implementation platforms.

**2. Change management *communications* are runner work, not API work.** When a change_set transitions to `pending_approval`, the API does not send notifications. A notification runner polls for pending approval rows, computes who needs to know, and dispatches via the configured channels. The API's job is to record the state transition; the runner's job is to communicate it. This is consistent with INFRA-2 §4.1 (passive substrate) and INFRA-4 §6 (coordination through shared substrate).

**3. Change management *application* to the DB is also runner work.** When a change_set reaches `approved` status, the API does not apply the field changes. A change-set executor runner (INFRA-4 §4.7) polls for approved-not-yet-applied change_sets, applies the field changes through the API, marks the change_set `applied`. The API's job is to validate, route for approval, and accept the executor's apply-writes; the runner's job is to drain the queue.

This third point is the largest revision from my earlier read. The API does not have an "apply" operation that runs automatically when approvals clear. Approval clearing is just a status transition. The actual application is a separate runner reading the OpsDB and writing back through the API. The to-perform queue is OpsDB rows; the executor is what drains it.

This makes the API even simpler than the spec suggested. The API is: validate, authenticate, authorize, route for approval, accept observation/evidence/output writes, accept executor apply-writes, audit everything. Communication, notification, scheduling enforcement, change application — all runner work.

## Plan for INFRA-5

### Title and metadata

**Title.** "OpsDB API Layer: Authentication, Versioning, and Change Management Gating"

Or possibly "The OpsDB API: Governance at the Single Gate" — leaning to the first because it names the three core concerns directly. Will decide on final title at draft time.

**Registry.** [@HOWL-INFRA-5-2026]

**Series path.** Continues from INFRA-4.

**Domain, status, AI usage disclosure.** Match INFRA-2/3/4 boilerplate.

### Abstract (~3 paragraphs, ~200 words)

Three movements:

- **Para 1.** What the API is. Single gate to the OpsDB. Self-contained operational software. Calls out only to authoritative external systems (identity providers for authentication, secret backends for credential resolution). Enforces all governance at this gate: authentication, authorization, validation, change management routing, versioning, audit.

- **Para 2.** What the API does. Get-set surface uniform across all entity types. Search API with filter predicates and named join paths. Field-level versioning bundled per change_set. Five-layer authorization (role, per-entity, per-field, per-runner, policy). Runner report keys gating runner write surfaces. Change_set lifecycle: draft → submitted → validating → pending_approval → approved → applied. Notification dispatch and change_set application are runner concerns, not API concerns.

- **Para 3.** What the API is not. Not an orchestrator (per INFRA-2 §4.1). Not a notification system. Not a change-set applier. Not built on top of any specific platform. Implementation choices (storage engine, wire protocol, deployment topology) are organizational; this paper specifies the API surface and the disciplines it enforces.

### §1 Introduction

**§1.1 The role of the API in the OpsDB design.** Cite INFRA-2's commitments (passive substrate, single gate, governance at the API). The API is where INFRA-2's commitments become operational. INFRA-3 specified what data exists; INFRA-4 specified what acts on it; INFRA-5 specifies how anything reaches it.

**§1.2 The API is self-contained operational software.** It is itself a runner-class component of the OpsDB-coordinated operational reality, but with elevated trust because it is the gate. It calls out only to identity authorities (LDAP/AD, OIDC, SAML providers, secret backends like Vault) for authentication and credential resolution. It does not depend on Kubernetes, on a specific cloud, on a specific orchestrator, or on any system the OpsDB models. Reasons: portability, simplicity, the same architectural-anchor logic that makes the OpsDB durable across the lifetime of the systems it manages.

**§1.3 What this paper specifies and does not specify.** Specifies: API surface, governance enforcement, versioning machinery, change management routing, auth/authz layers, runner report keys, audit. Does not specify: storage engine, wire protocol (REST vs gRPC vs structured RPC over JSON), deployment topology (monolithic vs sharded vs replicated), specific identity provider integration, specific UI design, specific runner implementations.

**§1.4 Document structure.** One-paragraph navigation through §§2–11.

### §2 Conventions

**§2.1 DSNC inheritance.** All schema references use DSNC per INFRA-3.

**§2.2 Underscore-prefix governance fields.** Reference INFRA-3 Appendix B; the API consults these fields during gate processing.

**§2.3 Typed payload pattern.** API validates `*_data_json` against the `*_type` discriminator's registered schema. Reference INFRA-3 §2.4 and §4.4.

**§2.4 Bridge tables for polymorphic relationships.** Reference INFRA-3 §2.5; the API resolves stakeholder identification through bridge walks per entity type, not polymorphic FKs.

**§2.5 The 0/1/N rule applied to API resources.** Cited explicitly. The API does not have "two ways to authenticate" or "two paths to write observation." Where N is genuine, the API supports N. Where 1 is correct, the API enforces 1.

**§2.6 Forthcoming reference: INFRA-6 schema construction.** Brief mention that INFRA-6 will specify how schemas are declared in hierarchical YAML/JSON files with declarative constraints (numeric ranges, enum sets, FK constraints; no regex, no logic). The API's bound validation step (§4) consumes constraints in this form.

### §3 The API surface — uniform get/set across all entity types

**§3.1 Operation shapes.** Small set of operation classes that work uniformly across all entity types. Caller specifies entity type and identifier; the API resolves against the schema and policy.

**§3.2 Read operations.**

- `get_entity` — fetch one row by primary key, returns row + metadata (current version, last_updated_time, freshness annotation for cached observation, governance flags consulted)
- `get_entity_history` — fetch the version chain for one entity
- `get_entity_at_time` — point-in-time query, reconstructs values active at a timestamp
- `search` — filter predicates, named join paths, projection, ordering, pagination, freshness requirements, view modes (standard / with_history / at_time). Detailed in §4.
- `get_dependencies` — substrate walks per INFRA-3's hierarchy (megavisor_instance.parent_megavisor_instance_id, service_connection edges); bounded by depth and cycle detection.
- `resolve_authority_pointer` — typed authority lookup; returns connection details, locator, last_verified_time, pointer metadata.
- `change_set_view` — scoped or full view of a change_set's field changes (for stakeholder review).

**§3.3 Write operations.**

- `write_observation` — direct write for observation-only data (cache tables, runner_job, runner_job_output_var, evidence_record). Authenticated as runner. No change management.
- `submit_change_set` — main write path for change-managed data. Validates, computes required approvals, records as pending. Returns change_set id. Supports `dry_run=true` (returns validation outcome and approval requirements without recording).
- `approve_change_set` / `reject_change_set` / `cancel_change_set` — stakeholder responses on existing change_sets.
- `emergency_apply` — break-glass with reduced approvals, flagged for post-hoc review.
- `bulk_submit_change_set` — large transactions, chunked validation, atomic commit.

**§3.4 What the API does not do.**

Does not invoke runners (passive substrate, INFRA-2 §4.1).
Does not dispatch notifications (runner concern).
Does not apply approved change_sets to the DB (runner concern — the change-set executor handles application).
Does not orchestrate (INFRA-2 §13.5).
Does not push or fire triggers.

The API is request-driven. Every operation is initiated by a caller. The API's role is to gate, validate, route, record, and respond.

**§3.5 The single API gate's enforcement steps.** A short list (~10 steps) walking through what every operation passes through: authentication, authorization, schema validation, bound validation, policy evaluation, versioning preparation, change-management routing, audit logging, execution (or queueing for executor pickup), response. Each step is data-driven; the schema declares structure, policies declare governance, the API enforces both.

This is illustrated by Figure 1 (the API gate's enforcement steps as a Type 7 progression).

### §4 The search API

**§4.1 Search request shape.** Structured request: entity types, filter predicates, join paths, projection, ordering, pagination, freshness requirements, view mode. Wire format is structured JSON tree (default); engines may transport via REST/gRPC/RPC as organizational choice.

**§4.2 Filter predicates.** Equality, inequality, comparison, set membership, pattern matching (anchored or unanchored, no regex), null checks, range, JSON path containment. Compose via AND/OR/NOT. Pattern-matching is bounded per INFRA-6's discipline — simple LIKE-style anchors, no regex (avoiding the perf-attack-vector class).

**§4.3 Join paths.** Named relationships, schema-defined. Examples: `service.host_group`, `service.connections`, `machine.megavisor_instance.parent_chain` (recursive), `entity.audit_log`. The API translates named paths to engine-appropriate operations. New join paths added through schema metadata; runners and humans don't write SQL.

**§4.4 Projection.** Field lists, default views, summary views, full-with-history views.

**§4.5 Result reporting.** Rows + metadata: total count or estimated count, pagination cursor, freshness summary, filtering disclosures (how many rows filtered out by access policy, without revealing which).

**§4.6 Bounds.** Maximum result size, maximum join depth, maximum query time, rate limits per caller. Bounds are policy data per INFRA-3 §12.6, evaluated at the gate.

**§4.7 Pagination.** Cursor-based by default (opaque, survives concurrent inserts, no deep-offset cost). Offset available for results under a configurable threshold (default 10k rows). Cursors carry enough state to resume the exact query position.

**§4.8 What stack-walking enables.** Brief mention that recursive joins through `megavisor_instance.parent_megavisor_instance_id` and similar paths enable the runner behaviors INFRA-4 §9 names (decommission awareness, failure-domain analysis, capacity awareness, dependency-aware change validation, locality-aware deployment). The search API is the surface; the runners use the surface.

### §5 Versioning machinery

**§5.1 Per-field versioning bundled per change_set.** When a change_set commits and updates an entity, the base table reflects the new field values, a row is appended to the entity's `*_version` sibling recording the post-change state (full row state, not just changed fields — point-in-time reconstruction is one row lookup), `change_set_field_change` rows are marked applied with timestamps. Reference INFRA-3 §4.2 directly.

**§5.2 What gets versioned.** Per INFRA-3 Appendix D — change-managed entities have version siblings; observation-only entities do not. Schema metadata (`_schema_*`) is itself versioned through `_schema_change_set` with stricter approval rules per INFRA-2 §4.9.

**§5.3 Version retention.** Per INFRA-3 §12.5 — `retention_policy` rows referenced via `_retention_policy_id` define horizons. The reaper runner (INFRA-4 §4.8) trims past-horizon versions. Compliance-relevant entities typically retain 7+ years; ephemeral configuration may retain 90 days. The API does not reap; the API reads what is and accepts the reaper's writes.

**§5.4 Sharding for high-frequency tables.** Default: one `*_version` table per entity table. For high-velocity entities (services in active organizations), the version sibling can be partitioned (by time range or entity_id range), with the sharding scheme recorded in `_schema_entity_type._schema_field_data_json`. The API handles partitioning transparently. Threshold for sharding is organizational — INFRA-5 specifies the mechanism, not the trigger numbers.

**§5.5 Rollback as change_set.** Never a side-channel operation. Rollback is a change_set whose field changes restore prior version values. Operator (or runner) reads version history, identifies target version, submits change_set restoring those values. The rollback flows through the same approval pipeline, produces its own version row, audited like any other change. Reference INFRA-2 §9.4 and the *reversible changes* principle from INFRA-1 §5.3.

**§5.6 Optimistic concurrency.** Each change_set carries the entity version it was drafted against. On submit, the API checks each touched entity's current version. If any has advanced since drafting, the submit fails with `stale_version` error and lists affected entities. The submitter retrieves current values, reconciles, resubmits. Loud failure at submit time, before approval starts; protects approvers from approving change_sets based on stale state.

### §6 Authentication and authorization

**§6.1 Authentication.** Self-contained API delegating identity verification to authoritative external systems.

- *Humans*: SSO via the org's identity provider (SAML, OIDC). API consumes assertions about identity and group memberships. Maps to `ops_user` rows by external identifier. API does not store passwords. Authentication failures are diagnosed in the IdP, not in the OpsDB API.
- *Runners*: Service-account credentials issued by the secret backend (Vault, AWS Secrets Manager, equivalent). Each `runner_machine` has associated credentials. API validates credentials against the issuing authority. Resolves to `runner_spec` and `runner_machine` rows. The shared OpsDB API client (INFRA-4 §5.1) handles credential acquisition, refresh, and authentication header management.
- *Web-mediated human writes*: Web app authenticates the human via SSO, calls a runner with the verified human identity, runner authenticates with its own credentials, API records both attributions in `audit_log_entry.acting_ops_user_id` (the originating human) and `acting_service_account_id` (the runner that performed the call).

**§6.2 The five-layer authorization model.** Each layer is data, evaluated at the gate.

1. **Standard role/group.** `ops_user_role_member` and `ops_group_member` rows determine baseline access. Roles map to operation classes (read-only, write-observation, propose-change, approve-change, schema-evolve).
2. **Per-entity governance.** Rows with `_requires_group` set restrict access to that group beyond baseline.
3. **Per-field classification.** Fields or tables with `_access_classification` restrict access to callers with sufficient clearance, regardless of baseline role.
4. **Per-runner authority.** Runners have declared `runner_capability` rows and `runner_*_target` bridges. The API verifies a runner's request matches its declared scope before permitting the write. Detailed in §8.
5. **Policy rules.** `policy` rows of type `access_control` impose additional constraints (time-of-day, segregation of duties for approvers, etc.).

All five layers are data. None is hardcoded. Changing access is changing rows.

**§6.3 Decision flow.** Every operation evaluates the five layers in order. First denial fails; all five must pass for the operation to proceed. The denial is recorded in the audit log with which layer denied. Illustrated by Figure 2 (the five-layer authorization decision tree).

**§6.4 Authority delegation principle.** The API does not duplicate identity authority. It does not maintain a parallel user database, parallel password storage, parallel group store. Every identity claim is verified against the authoritative source. This is the "single source of truth" principle (INFRA-1 §5.1) applied to authentication: identity authority is the IdP; the OpsDB stores only what it owns (the operational identity rows that map to external identities).

### §7 Change management as gate function

**§7.1 The gate's role in change management.** The API validates, computes approval requirements, records change_sets and their state, accepts approval and rejection writes, and provides queryable access to all of it. The API does not communicate with stakeholders (notification runner's job per §1). The API does not apply approved change_sets to the database (change-set executor's job per INFRA-4 §4.7).

**§7.2 Change_set lifecycle.** Reference INFRA-3 §18.1's status enum directly: draft → submitted → validating → pending_approval → approved → applied. Exits: rejected, expired, cancelled. Each transition is a data write to the `change_set.change_set_status` field. Illustrated by Figure 3 (the change_set lifecycle as a state machine).

**§7.3 Stakeholder identification.** When a change_set is submitted, the API:

- For each `change_set_field_change`, looks up the target entity.
- Walks ownership and stakeholder bridges (`service_ownership`, `machine_ownership`, `k8s_cluster_ownership`, `cloud_resource_ownership`, and corresponding stakeholder bridges) to find owners and stakeholders for each affected entity.
- Evaluates `policy` rows of type `approval_rule` against the entity, namespace, fields touched, and metadata (classification, security zone, compliance scope).
- Computes a set of `change_set_approval_required` rows — one per (rule, group) combination that needs approval.

A change_set may have multiple approval requirements: service owner approval for the service, security team approval if the change touches a `_security_zone` field, compliance team approval if the entity is in `compliance_scope_service`, schema steward approval if the change touches `_schema_*` tables.

Each requirement is independent. All must be fulfilled before transition to approved. Illustrated by Figure 4 (stakeholder routing — bridges walked, requirements computed).

**§7.4 Stakeholder views.** `change_set_view` operation returns either:

- *Scoped view* — only field changes the viewer's groups have approval authority over.
- *Full view* — all field changes the viewer is permitted to see (subject to `_access_classification` and `_requires_group`).

Plus summary metadata: total field changes, breakdown by entity type, validation results, approvals received and pending. The view is a read; it does not commit anything. Stakeholders use it to decide whether to approve, reject, or request modification.

**§7.5 Approvals and rejections.** `approve_change_set` and `reject_change_set` operations. API verifies caller is in a required approver group for this change_set. Records the action in `change_set_approval` or `change_set_rejection`. Re-evaluates whether the change_set has met all its requirements. Updates `change_set_approval_required.fulfilled_count` and `is_fulfilled`. If all requirements are fulfilled, transitions `change_set.change_set_status` to `approved`. If a required approver rejects (per the rule's rejection semantics), transitions to `rejected`.

**§7.6 Validation pipeline.** Before approval routing, validation runs in `change_set_validation` records:

- *Schema validation* — every field change matches the entity's schema.
- *Bound validation* — numeric ranges, enums, FK existence (INFRA-6 declarative constraints).
- *Semantic validation* — cross-field invariants.
- *Policy validation* — change does not violate active policies.
- *Lint* — organizational style and naming rules.
- *Dependency check* — walking `service_connection` to verify downstream contracts hold.

Failures block. Warnings allow proceeding with explicit acknowledgement recorded in `change_set_validation.validation_data_json`.

**§7.7 The approved-not-yet-applied state.** Approved change_sets sit in OpsDB rows with `change_set_status='approved'` and `applied_time IS NULL`. This is the to-perform queue — itself OpsDB data, not a separate queue system. The change-set executor runner (INFRA-4 §4.7) polls for these rows and applies them through the API. The API's role at this stage is to accept the executor's apply-writes (which are direct writes to entity rows + version siblings + the `applied_status` updates on `change_set_field_change` rows + the `applied_time` on `change_set`). Specialized executors per entity class may also exist for change_sets that require coordinated world-side action (the helm git exporter being the canonical example, INFRA-4 §10).

This is the load-bearing clarification: the API does not "commit" changes when approvals clear. Approval clearing is a status transition. The actual application is a separate runner pass. The decoupling preserves the passive-substrate commitment.

**§7.8 Direct path — no approval required.** Some change_sets auto-approve via policy. The API computes approval requirements; if all rules auto-approve, the change_set transitions through validating → pending_approval → approved without human intervention. The pending_approval state may be skipped entirely for fully-auto-approved change_sets. The change-set executor still picks them up to apply. Same path, different routing.

**§7.9 Emergency changes.** `emergency_apply` operation. Caller has emergency authority per policy. Change_set commits with reduced approvals (typically self-approval by an on-call engineer). Flagged in `change_set.is_emergency=true`. A `change_set_emergency_review` row is created in pending status. After 72 hours without review, an `emergency_review_overdue` finding is filed automatically, and escalation notifications continue every 24 hours until reviewed (notification runner's job). The change is not auto-rolled-back; rollback requires a fresh change_set per the *reversible changes* discipline.

**§7.10 Bulk operations.** `bulk_submit_change_set` for transactions that touch many entities (fleet-wide credential rotation, mass policy application). Validation chunks (default 1000 field changes per chunk) so feedback streams early. The change_set remains coherent as one unit — either all chunks validate and the change_set transitions as one, or it fails as one. Apply phase is similarly chunked, with the change_set in `applying` substate until all chunks complete; failure during apply rolls all chunks. Reference INFRA-2 §9.13 for the use case rationale.

**§7.11 Runner-proposed change_sets.** Runners propose change_sets the same way humans do. The change_set carries `proposed_by_runner_job_id` instead of (or alongside) `proposed_by_ops_user_id`. Approval rules are agnostic to whether the proposer is human or runner. INFRA-2 §9.14 establishes the pattern; INFRA-5 specifies that the API treats the two proposer fields uniformly.

### §8 Runner report keys — gating runner write surfaces

**§8.1 The problem.** Without report-key declarations, a runner that has any write authority to `observation_cache_metric` can write any metric. A compromised or misconfigured runner could write arbitrary keys to arbitrary entities. The audit trail records what was written but cannot verify that the writer was authorized to write that specific key.

**§8.2 The mechanism.** Each runner declares its writable surface in `runner_report_key` rows. The declarations specify, per runner_spec and per target table, which keys the runner is authorized to write. The target tables for which declarations apply are: `observation_cache_metric` (the metric_key), `observation_cache_state` (the state_key), `observation_cache_config` (the config_key), `runner_job_output_var` (the var_name), `evidence_record` (the evidence_record_type).

**§8.3 The schema addition.** This is what INFRA-5 contributes to the schema. A new entity type:

```
runner_report_key
  id
  runner_spec_id
  report_target_table     -- VARCHAR enum
  report_key              -- the authorized key value
  report_key_data_json    -- type, value validation rules
  is_active
  created_time
  updated_time

runner_report_key_version  -- versioning sibling
  ...
```

The table is change-managed. Adoption of INFRA-5 requires a `_schema_change_set` introducing it. Reference INFRA-3 §20.2 for the schema-evolution discipline.

**§8.4 The verification flow.** When a runner submits a write to one of the targeted tables, the API:

1. Looks up the runner's `runner_report_key` rows for the target table.
2. Verifies the submitted key is in the declared set.
3. Validates the value against the declared shape (per INFRA-6 declarative constraints).
4. Rejects writes for keys not in the declared set, with a clear error.

Illustrated by Figure 5 (the runner report key verification flow).

**§8.5 Why this matters.** The runner's writable surface becomes explicit and auditable. A compromised runner with declared keys for `host_cpu_utilization` cannot suddenly start writing `database_credentials` to the metric table. The audit trail strengthens: every metric, evidence record, and output variable has a verifiable origin — not just the runner that wrote it but the change_set that authorized the runner to write that key.

This is the *fail closed* principle (INFRA-1 §5.3) applied to the runner write surface. Without a declaration, the write is rejected. The default is denial; authorization is declarative and change-managed.

**§8.6 Worked example.** A puller for Prometheus host metrics declares allowed keys: `host_cpu_seconds_total`, `host_memory_bytes_total`, `host_disk_bytes_total`. The puller submits writes for these keys; they pass. The puller, due to a misconfiguration, attempts to write `database_credentials_active`; the API rejects with "key not in declared set." The audit log records the rejection with the runner identity. An operator investigating the rejection finds the misconfiguration and corrects it through a change_set. If the legitimate need is to write a new key, the change_set proposes a `runner_report_key` addition; the addition is reviewed and approved or rejected like any other governance change.

### §9 Audit logging

**§9.1 What gets logged.** Every API operation produces an `audit_log_entry`. The entry includes:

- Operation identity (which API endpoint, which method).
- Caller identity (acting_ops_user_id, acting_service_account_id, both for runner-mediated human writes).
- Operation details (target entity type and id, fields touched, before/after summary).
- Result (success, validation_failed, authorization_denied, internal_error, rate_limited).
- Context (client IP, user agent, request ID for correlation, change_set_id if applicable).
- High-precision monotonic timestamp set by the API.
- Optional `_audit_chain_hash` for tamper-evidence regimes.

**§9.2 Append-only enforcement.** DDL-level: no UPDATE or DELETE permission on `audit_log_entry` for any role, including substrate operators. The API is the only writer. This is stricter than other tables (INFRA-3 §19.1).

Even substrate-level maintenance cannot modify audit entries. If entries become corrupted, the response is to mark them in a separate `audit_log_anomaly` table, not to modify the original.

**§9.3 Cryptographic chaining.** Optional, per regime. Each entry includes a hash of the prior entry; modification of historical entries breaks the chain detectably. The API computes the chain hash on write; verification tooling recomputes and detects breaks.

**§9.4 Retention.** Policy-driven via `retention_policy`. Compliance regimes typically require 7+ years; some longer. The reaper runner does not touch audit_log_entry rows past retention without an explicit policy granting it, and even then deletion is logged in a separate audit-of-audit table.

**§9.5 Query access.** Auditors query `audit_log_entry` through the standard search API with their auditor role. Filter by entity type, entity id, time range, caller identity. Cross-cutting queries ("every change touching service X in Q3") resolve through search joins. The auditor reads the same data the operator reads; only the access scope differs (read-only across all entities, no write authority except for filing findings).

### §10 What this API does not do

**§10.1 Boundary discipline.** Reference INFRA-2 §13 directly. The API inherits the OpsDB's boundary commitments. The list, in API-specific form:

- *Not an orchestrator.* The API does not invoke runners, does not push notifications, does not fire triggers. Runners poll, runners react, runners coordinate through OpsDB rows.
- *Not a notification system.* When a change_set transitions to pending_approval, the API does not send notifications. A notification runner reads pending_approval rows and dispatches via configured channels.
- *Not a change-set applier.* When a change_set reaches approved, the API does not apply the field changes. The change-set executor runner reads approved-not-yet-applied rows and applies them through API write operations.
- *Not a workflow engine beyond change management.* Change_set lifecycle is the only workflow. Other workflows (incident response, deployment pipelines, capacity planning) are runner concerns.
- *Not a code distribution path.* The API does not host runner code, package code, or any artifact. Pointers to `runner_image_reference` and `package_data_json` exist; the artifacts live elsewhere.
- *Not a secrets store.* The API resolves authentication credentials from secret backends; it does not store secret values. `k8s_secret_reference` rows and configuration variables of type `secret_reference` are pointers, never values.

**§10.2 Why these boundaries hold.** Each boundary kept makes the API better at what it does. Adding orchestration would compromise the passive-substrate commitment. Adding notification would couple the API to delivery infrastructure. Adding application would couple the API to the world-side action timing of executor runners. The discipline is part of the design.

### §11 Closing

**§11.1 What this paper specified.** The API surface uniform across all entity types. The five-layer authorization model with all layers as data. Field-level versioning bundled per change_set with sharding for high-frequency tables. Optimistic concurrency through version checks at submit. Change_set lifecycle as data, with the to-perform queue as approved-not-yet-applied rows. Runner report keys as the gate on runner write surfaces. Audit logging append-only at DDL level with optional cryptographic chaining. The boundary discipline that keeps the API focused.

**§11.2 What the API enables.** The disciplines INFRA-2 committed to become operational. Every change has a queryable trail composed from OpsDB rows. Every runner's writable surface is explicit. Every approval has attribution. Every rollback is just another change_set. Every read by humans, automation, and auditors goes through the same gate against the same data with scoped access.

**§11.3 The structural claim.** The API is the active layer where governance happens. The substrate is passive; the runners are active in the world; the API is active in governance. The three layers compose. Without the API gate, the disciplines are advisory. With the gate, the disciplines are mechanically enforced.

**§11.4 Forward references.** INFRA-6 will specify the schema construction system that declares constraints in hierarchical YAML/JSON files; the API consumes these constraints in its bound validation step. Future papers may specify specific runner archetypes in detail (the change-set executor, the notification runner, specific puller and verifier patterns), but the API surface specified here is stable across those evolutions.

---

## Appendices

**Appendix A: Operation reference table.** Every API operation with inputs, outputs, governance applied, gating mode.

**Appendix B: Authorization decision flow.** The five layers as a complete decision tree, with example denial cases.

**Appendix C: Change_set lifecycle reference.** Every state, every transition, what triggers each, what data writes occur.

**Appendix D: Validation pipeline reference.** Every validation type, what it checks, fail vs. warning semantics.

**Appendix E: Runner report-key examples.** Concrete declarations for puller, verifier, reconciler runners with realistic keys and constraints.

**Appendix F: Search join path reference.** The named relationships available in the schema, with substrate-walk examples (decommission check, failure-domain check, pod ancestry per INFRA-4 Appendix E).

**Appendix G: Audit log entry structure.** Field-by-field reference for `audit_log_entry`, including the chain hash mechanics.

---

## Figures planned

1. **The API gate's enforcement steps.** Type 7 progression. Auth → authz → schema validation → bound validation → policy evaluation → versioning prep → change-mgmt routing → audit logging → execution → response.

2. **The five-layer authorization decision tree.** Type 7 progression. Each layer evaluated; first denial fails; all-pass proceeds.

3. **Change_set state machine.** Type 5 connection map. Draft → submitted → validating → pending_approval → approved → applied; exits to rejected, expired, cancelled.

4. **Stakeholder routing — bridges walked, requirements computed.** Type 5 connection map. Change_set field changes → entity ownership/stakeholder bridges → approval_rule policies → required approver groups.

5. **Runner report key verification flow.** Type 7 progression. Write submitted → lookup declared keys → verify in set → validate value shape → accept or reject with audit.

6. **Get/set surface across populations.** Type 5 connection map. Humans, automation, auditors approaching one API surface; operations from the same set serve all three.

7. **The to-perform queue as OpsDB data.** Type 4 geometric. Approved-not-yet-applied change_sets sitting as rows; change-set executor runner polling.

8. **Versioning per field bundled per change_set.** Type 4 geometric. Multiple field changes in one change_set producing one version row per affected entity, all atomic on commit.

---

## Word count estimate and pacing

INFRA-2 is approximately 13,000 words. INFRA-3 is approximately 17,000 words (heavy on schema reference). INFRA-4 is approximately 12,000 words.

INFRA-5 should land between INFRA-2 and INFRA-3 in length — perhaps 13,000-15,000 words. The content is dense (governance mechanics, lifecycle states, validation pipeline) but the paper inherits heavily from prior work and can cite by tag rather than re-explain. The new substantive material is the runner_report_key system, the optimistic concurrency model, the search API specifics, the five-layer authorization model in detail, and the clarification that change-set application is a runner concern.

Section 7 (change management) and Section 6 (auth) will be the longest sections; everything else is moderate.

---

## What I'd want before drafting begins

1. **Confirmation of the title.** "OpsDB API Layer: Authentication, Versioning, and Change Management Gating" — or your preference.

2. **Confirmation of the runner_report_key mechanism's specifics.** Particularly that the report_target_table enum is exactly the five tables I named, and that the declaration is at the runner_spec level (not per runner_machine instance).

3. **Confirmation that Approval Rules are policy rows.** I want to be explicit in INFRA-5 that "approval rules" semantically refers to `policy` rows with `policy_type='approval_rule'`, per INFRA-3 §12.6. If INFRA-3 has a different intent, I'll adjust.

4. **Confirmation that no `notification_trigger` table is needed.** The notification runner reads pending_approval change_set rows directly; no separate trigger table.

5. **Any other clarifications about scope.** Specifically: should INFRA-5 address API versioning explicitly (header-versioned, schema additions don't bump API version) or leave that to a future operational concerns paper?

When you're ready, give me the go-ahead and any corrections to the plan, and I'll draft the abstract + §1 + §2 first as the register check.
