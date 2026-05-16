## Appendix J: Scope Chain Resolution Examples

### J.1: Complete Scope Chains by User Type

| User | Position Path | Scope Chain (bottom to top) | Reachable Branches | Unreachable Branches |
|------|-------------|---------------------------|-------------------|---------------------|
| Alice | root.org.acme.engineering.platform.alice | alice → platform → engineering → acme → org → root | engineering.*, acme shared KBs, root.public | hr.*, finance.*, legal.*, sales.* |
| Carol | root.org.acme.hr.recruiting.carol | carol → recruiting → hr → acme → org → root | hr.*, acme shared KBs, root.public | engineering.*, finance.*, legal.*, sales.* |
| Diana | root.org.acme.hr.director.diana | diana → director → hr → acme → org → root | hr.* (with owner_only access), acme shared, root.public | engineering.*, finance.*, legal.*, sales.* |
| Eve | root.org.acme.finance.analyst.eve | eve → analyst → finance → acme → org → root | finance.*, acme shared, root.public | engineering.*, hr.*, legal.*, sales.* |
| Frank | root.org.acme.ceo.frank | frank → ceo → acme → org → root | All acme.* (subject to visibility), root.public | Nothing structurally excluded at branch level |
| Anon | root.sessions.anon_session_47 | anon_session_47 → sessions → root | root.public only | Everything under root.org |
| System | root.system.process_N | process_N → system → root | root.system.*, root.public | root.org.* (by design) |

### J.2: Sibling Branch Isolation Verification

| Querying User | Target KB | Relationship | Scope Chain Contains Target? | Result |
|--------------|----------|-------------|-----------------------------|----|
| Alice (engineering) | hr.personnel | Sibling branch | No — engineering and hr share parent acme but are siblings | Never searched |
| Alice (engineering) | engineering.backend.configs | Descendant of ancestor | Yes — backend is child of engineering which is in alice's chain | Searched (visibility permitting) |
| Carol (hr.recruiting) | hr.director.reports | Sibling within hr | No — recruiting and director are siblings under hr | Never searched |
| Carol (hr.recruiting) | hr.policies | Child of hr (ancestor) | Yes — policies is child of hr which is in carol's chain | Searched (visibility permitting) |
| Anon | root.org.acme.anything | Sibling of sessions | No — org and sessions are siblings under root | Never searched |
| Anon | root.public.general | Child of root (ancestor) | Yes — public is child of root which is in anon's chain | Searched (visibility: public passes) |

Sibling branches are never searched. This is not a filter — the query algorithm walks ancestors upward, not siblings sideways. The isolation is a property of the tree traversal, not an access control check applied after traversal.

---

## Appendix K: Visibility Interaction with Mounts

### K.1: Mount Visibility Enforcement

| Mount Mode | Source Visibility Checked On | Write Permitted | Cycle Detection | Visibility Override Possible |
|-----------|----------------------------|----------------|----------------|---------------------------|
| read_only | Every query through mount | No | Yes (pre-creation) | No — source visibility governs |
| read_write | Every query and write | Yes (requires grant) | Yes | No |
| snapshot | At mount time (frozen copy) | No (frozen) | Yes | No — snapshot inherits source visibility at freeze time |
| mirror | Every sync operation | No (sync-only) | Yes | No |

### K.2: Mount Attack Scenarios

| Attack | Mechanism | Failure Point | Integer Operation |
|--------|-----------|--------------|-------------------|
| Mount restricted KB to public workspace | B359 mount_create | Grant check: user lacks mount grant for source KB | Set membership (grant exists?) |
| Mount via intermediary (A mounts B, C mounts A to reach B) | B359 mount_create with chain | Chain trace: system follows mount chain to original source, checks visibility at each hop | Parent ID traversal + visibility check per hop |
| Mount then elevate source visibility | B359 mount_create then modify source | Source visibility modification requires owner/admin grant on source KB | String equality (owner check on source) |
| Snapshot mount to freeze before visibility downgrade | B359 mount with snapshot mode | Snapshot inherits visibility at freeze time; if source was owner_only, snapshot is owner_only | Visibility enum copied at snapshot time |
| Create circular mount chain to confuse access check | B359 mount_create | Cycle detection traces full chain before creation; rejects if cycle detected | Parent ID set membership (visited set) |

Every mount attack fails at an integer operation in the primitive layer. Mounts do not create new access paths — they create addressability aliases that still enforce the source KB's visibility on every access.

---

## Appendix L: Constraint Conflict Resolution

### L.1: Constraint Precedence Rules

| Conflict Type | Resolution | Example | Rationale |
|-------------|-----------|---------|-----------|
| Axiom vs Operational | Axiom wins | weapons_restricted (axiom) vs research_access (operational) | Axioms cannot be suspended |
| Axiom vs Legal | Axiom wins | pii_protected (axiom) vs gdpr_right_to_access (legal) | Axioms are absolute by definition |
| Legal vs Operational | Legal wins | export_control (legal) vs team_data_sharing (operational) | Legal obligations override operational convenience |
| Legal vs Project | Legal wins | material_nonpublic (legal) vs project_transparency (project) | Legal obligations override project policy |
| Operational vs Project | Operational wins | org_security_policy (operational) vs project_open_access (project) | Organizational policy overrides project policy |
| Parent vs Child (same class) | Stricter wins | org: max_export_size=10MB vs team: max_export_size=5MB | Children can tighten, never loosen |
| Parent vs Child (child attempts to loosen) | Parent wins (child override rejected) | org: pii_scan_required vs team: pii_scan_optional | Rejection logged as policy violation attempt |

### L.2: Multi-Constraint Evaluation Order

| Step | Action | Short-Circuit | Logging |
|------|--------|--------------|---------|
| 1 | Collect all constraints in scope chain (child to root) | No | Collected set recorded |
| 2 | Sort by class: axiom first, then legal, then operational, then project | No | Sort order recorded |
| 3 | Evaluate axiom constraints | Yes — any axiom failure blocks immediately | Failure logged, remaining constraints not evaluated |
| 4 | Evaluate legal constraints | Yes — any legal failure blocks | Failure logged |
| 5 | Evaluate operational constraints | Yes — any operational failure blocks | Failure logged |
| 6 | Evaluate project constraints | Yes — any project failure blocks | Failure logged |
| 7 | All passed | Access proceeds | All evaluations logged as passed |

Short-circuit evaluation means the cheapest check (axiom, typically one integer comparison) runs first. If it fails, no further evaluation occurs. This makes the common denial case (hitting an axiom constraint) the cheapest path.

---

## Appendix M: Grant Lifecycle

### M.1: Grant Fields

| Field | Type | Set By | Modifiable After Creation | Example |
|-------|------|--------|--------------------------|---------|
| grant_id | Integer | System (auto-increment) | No | 4817 |
| operation_class | Enum | Administrator | No | filesystem |
| allowed_operations | List[String] | Administrator | No | [read, list_dir] |
| location_constraint | String (path prefix or URL pattern) | Administrator | No | /projects/atlas/* |
| issuer | String | System (from admin identity) | No | security_admin_jane |
| issued_at | Integer (timestamp) | System | No | turn_1204 |
| expires_at | Integer (timestamp) | Administrator | No | turn_50000 |
| max_uses | Integer | Administrator | No | 500 |
| remaining_uses | Integer | System (decremented on use) | Yes (decrement only) | 347 |
| status | Enum | System | Yes (active → exhausted, active → expired, active → revoked) | active |
| granted_to | String (user or group path) | Administrator | No | root.org.acme.engineering.platform |

### M.2: Grant State Transitions

| From State | To State | Trigger | Reversible | Logged |
|-----------|---------|---------|-----------|--------|
| active | active (use decremented) | Successful operation matching grant | No (cannot re-increment) | Yes — grant_used fact |
| active | exhausted | remaining_uses reaches 0 | No | Yes — grant_exhausted fact |
| active | expired | current_time exceeds expires_at | No | Yes — grant_expired fact |
| active | revoked | Administrator revocation | Yes (new grant can be issued) | Yes — grant_revoked fact with revoker identity |
| exhausted | N/A | Terminal state | N/A | N/A |
| expired | N/A | Terminal state | N/A | N/A |
| revoked | N/A | Terminal state (new grant is separate entity) | N/A | N/A |

Grant states are monotonic — they move toward terminal states only. There is no mechanism to add uses to an existing grant, extend an expired grant, or un-revoke a revoked grant. A new grant is a new entity with a new ID. This ensures the audit trail is append-only with no retroactive modification.

### M.3: Grant Inheritance Chain

| User Position | Own Grants | Team Grants | Department Grants | Org Grants | Effective Grant Set |
|--------------|-----------|------------|------------------|-----------|-------------------|
| alice (platform engineer) | 2 (personal dev tools) | 5 (platform team tools) | 8 (engineering tools) | 3 (org-wide tools) | 18 |
| carol (hr recruiter) | 1 (personal workspace) | 3 (recruiting tools) | 4 (hr tools) | 3 (org-wide tools) | 11 |
| anon (anonymous) | 0 | 0 | 0 | 0 | 0 |

Anonymous users have zero grants at every level. Their effective grant set is empty. Every operational primitive is denied. This is not a policy decision — it is the structural consequence of having no position in the organizational tree.

---

## Appendix N: Classification KB Design

### N.1: Tag Hierarchy

| Domain Tag | Parent Category | Signal Direction | Weight |
|-----------|----------------|-----------------|--------|
| pharmacology | professional | Positive (toward access) | 1 per occurrence |
| biochemistry | professional | Positive | 1 |
| clinical_medicine | professional | Positive | 1 |
| quantitative_measurement | professional | Positive | 1 |
| academic | professional | Positive | 1 |
| treatment_protocol | professional | Positive | 1 |
| safety_context | professional | Positive | 1 |
| toxicology | neutral | Neither (topic indicator only) | 0 |
| curiosity | neutral | Neither | 0 |
| harm_intent | harmful | Negative (toward denial) | 1 |
| forensic_evasion | harmful | Negative | 1 |
| no_professional_context | harmful | Negative | 1 |
| colloquial_violence | harmful | Negative | 1 |
| urgency_harm | harmful | Negative | 1 |
| synthesis_request | harmful | Negative | 1 |

### N.2: Pattern Matching Rules

| Pattern Type | Mechanism | Builtin | Example | False Positive Mitigation |
|-------------|-----------|---------|---------|--------------------------|
| Exact term match | B168 string_contains | Lookup in classification KB | "LD50" → quantitative_measurement | Low ambiguity terms only |
| Phrase match | B168 string_contains on multi-word | Lookup in classification KB | "chelation agent" → clinical_medicine | Phrase specificity reduces false positives |
| Negation context | B168 + B274 if_then_else | Check for negation words near match | "not trying to harm" — "not" near "harm" | Negation does not cancel harm_intent; counter still increments |
| Compound signal | Multiple tags on single turn | Counter increments for each | "How to kill undetectably" → harm_intent + forensic_evasion + colloquial_violence | Multiple harmful tags in one turn strongly indicate harm intent |

### N.3: Classification KB Maintenance

| Operation | Mechanism | Token Cost | Effect Timing | Rollback |
|-----------|-----------|-----------|--------------|----------|
| Add new term-tag mapping | B376 kb_assert at root.system.classification | 8 (command token) | Immediate (next turn for all sessions) | B377 kb_retract |
| Remove term-tag mapping | B377 kb_retract | 8 | Immediate | B376 kb_assert |
| Adjust scoring threshold | B376 kb_assert replacing Prolog rule | 20 (rule formalization) | Immediate | Assert previous rule |
| Add new tag category | B376 kb_assert for tag + scoring rule update | 30 | Immediate | Retract tag + restore rule |
| Bulk update from review | Script via B410 execute_python generating assert commands | ~50 (script) | Immediate | Snapshot restore |

All classification updates are knowledge base operations. No retraining. No redeployment. No model weight changes. Policy is data in the KB tree.

---

## Appendix O: Cross-Cutting Safety Scenarios

### O.1: Multi-Layer Defense Activation

| Scenario | Layer 1 (Visibility) | Layer 2 (Grants) | Layer 3 (Output Constraints) | Layers Activated | User Sees |
|----------|---------------------|------------------|------------------------------|-----------------|-----------|
| Anon asks for public data | Pass (public KB) | N/A (pure query, no grant needed) | Pass (no flagged content) | 0 blocks | Requested data |
| Anon asks for restricted data | Block (restricted KB not in scope) | N/A | Not reached | 1 block | Empty result → "no data available" |
| Anon asks for weapons info from training | Block (restricted KB not in scope) | N/A | Block (output constraint catches training-derived content) | 2 blocks | Refusal template |
| Engineer queries own project data | Pass | Pass (project grant exists) | Pass | 0 blocks | Requested data |
| Engineer queries HR data | Block (scope) | Not reached | Not reached | 1 block | Empty result |
| Engineer queries HR via prompt injection | Block (scope — injection doesn't change session ID) | Not reached | Not reached | 1 block | Empty result |
| HR director queries personnel | Pass (owner match) | N/A (pure query) | Pass (authorized user, no content restriction) | 0 blocks | Requested data |
| HR director exports personnel CSV | Pass | Check (filesystem write grant for HR director?) | Pass if granted | 0-1 blocks | Data or grant denial |
| Authenticated user, harm-scored session | Pass for public | N/A | Block (session scoring denied toxicology access via constraint) | 1 block (constraint) | Empty result for restricted topics |

### O.2: Defense Depth Coverage

| Attack Type | Layer 1 Sufficient? | Layer 2 Sufficient? | Layer 3 Sufficient? | All Layers Combined |
|------------|--------------------|--------------------|--------------------|--------------------|
| Query for out-of-scope data | Yes | N/A | N/A | Complete protection |
| Query for in-scope but visibility-restricted data | Yes | N/A | N/A | Complete protection |
| Operational primitive without grant | N/A | Yes | N/A | Complete protection |
| LLM generates harmful content from training | No (data didn't come from KB) | N/A | Yes | Complete protection |
| LLM generates harmful content AND data leaked from KB misconfiguration | No (misconfiguration) | N/A | Yes | Caught by layer 3 |
| All three layers misconfigured simultaneously | No | No | No | Breach — requires three independent failures |

The probability of breach requires three independent structural failures: a KB visibility misconfiguration AND a grant misconfiguration AND an output constraint gap, all affecting the same data path. Each is a configuration error, not a probabilistic behavioral failure.

---

## Appendix P: Session Counter Properties

### P.1: Counter Monotonicity and Security Implications

| Property | Description | Security Implication |
|---------|------------|---------------------|
| Counters only increment | B298 counter_inc adds, never subtracts | Harm signals cannot be erased by subsequent "good" turns |
| Counters are per-session | New session starts at zero | User cannot carry professional credibility from a compromised session |
| Counter values are exact integers | No floating-point drift, no rounding | Threshold comparisons are deterministic; same counters always produce same decision |
| Counters have declared bounds | min_value and max_value on creation | Counter overflow impossible; max harm score is bounded |
| Counter reads are pure | B304 counter_get has no side effects | Scoring evaluation cannot modify the scores it reads |
| Counter increments are logged | Each increment is a KB fact | Complete trail of how scores accumulated |

### P.2: Session Score Accumulation Rates

| User Behavior Pattern | Turns to Professional Threshold (3) | Turns to Typical Harm Block | Steady-State Score Ratio |
|----------------------|-------------------------------------|---------------------------|------------------------|
| Pure professional | 1-2 turns (multiple professional tags per turn) | Never | Pro >> Harm |
| Pure harmful | Never | 1-2 turns | Harm >> Pro |
| Mixed leaning professional | 3-5 turns | Never (pro outpaces harm) | Pro > Harm |
| Mixed leaning harmful | Possible at 5-10 turns if professional signals strengthen | 2-3 turns initially | Varies — harm starts fast |
| Gradual escalation (starts professional, turns harmful) | Achieved early | May never trigger if professional lead is large | Depends on turn of escalation |

### P.3: Threshold Sensitivity Analysis

| Professional Threshold | False Denial Rate (estimated) | False Access Rate (estimated) | Notes |
|-----------------------|------------------------------|------------------------------|-------|
| 1 | Low (almost anyone passes with one professional term) | High (one professional term plus harm gets through) | Too permissive |
| 3 | Moderate (requires sustained professional signal) | Low (harm users rarely accumulate 3 professional signals) | Balanced default |
| 5 | High (casual professionals blocked) | Very low | Conservative — suitable for high-risk content |
| 10 | Very high (only extended professional sessions pass) | Negligible | Extreme — blocks most legitimate users |

Threshold selection is a policy decision stored as a Prolog rule fact. Changing from 3 to 5 is one B376 kb_assert. The change takes effect immediately. No retraining. The system can run multiple thresholds simultaneously for different content categories — toxicology at 3, weapons-adjacent chemistry at 7, nuclear physics at 10.

---

## Appendix Q: Output Constraint Coverage Gaps

### Q.1: What Output Constraints Catch vs Miss

| Content Type | Output Constraint Catches | Output Constraint Misses | Mitigation |
|-------------|--------------------------|-------------------------|-----------|
| Known flagged terms (exact match) | Yes — string matching against classification KB | Novel terminology not in KB | Regular classification KB updates |
| Known patterns (phrase structure) | Yes — multi-word pattern matching | Novel phrasings with same meaning | Pattern expansion in classification KB |
| Encoded content (base64, rot13) | No — slot content is encoded text | User decodes client-side | Input-side detection of encoding patterns via session tagging |
| Metaphorical/allegorical content | No — no semantic analysis in pattern matching | Creative framing that avoids literal terms | Layer 1 (KB visibility) handles data access; output constraints handle known patterns |
| Multi-slot assembly | Partial — each slot checked independently | Harmful content split across slots | Grammar design: single content slot for sensitive topics |
| Image/diagram descriptions | Yes — text in slots is checked | User mentally reconstructs from description | Layer 1 prevents access to source data |

### Q.2: Coverage by Layer

| Content Source | Layer 1 Coverage | Layer 3 Coverage | Combined Coverage |
|---------------|-----------------|-----------------|------------------|
| KB data (visibility-restricted) | 100% — data never enters LLM context | N/A — never reaches output | 100% |
| KB data (public, appropriate) | Pass — authorized | Pass — not flagged | 100% (correct access) |
| Training data (known harmful patterns) | N/A — not from KB | ~95% — pattern matching catches known patterns | ~95% |
| Training data (novel harmful formulations) | N/A — not from KB | ~60% — novel patterns may evade | ~60% (acknowledged gap) |
| LLM creative generation (not from training or KB) | N/A | ~80% — catches most but creative framing can evade | ~80% |

The acknowledged gap is training-derived content in novel formulations that evade pattern matching. This is the same gap that all safety systems face — including RLHF, which also fails on sufficiently novel adversarial inputs. The difference is that VDR-LLM-Prolog's gap is limited to this one scenario. For data access, coverage is 100%. For known harmful patterns, coverage is ~95%. Only novel formulations of training-derived harmful content present a residual risk, and this risk is mitigated by regular classification KB updates that are instant (one fact assertion) rather than requiring retraining.

---

## Appendix R: Identity Immutability

### R.1: Session Identity Chain

| Identity Component | Set By | Set When | Storage Location | Modifiable by Prompt | Modifiable by Command Token | Modifiable by Admin |
|-------------------|--------|----------|-----------------|--------------------|--------------------------|--------------------|
| session_id | System | Session creation | Session KB identity field | No | No | No (auto-generated) |
| user_id | Authentication system | Login/session creation | Session KB identity field | No | No | No (from auth system) |
| user_position_path | Organizational tree | User account creation | User KB path field | No | No | Yes (admin can move user in tree) |
| group_memberships | Administrator | Group assignment | User KB or team KB facts | No | No | Yes (admin can modify) |
| active_grants | Administrator | Grant issuance | User/team/dept/org KB facts | No | No | Yes (admin can issue/revoke) |
| session_counters | System | Incremented on classification | Session KB live state | No | No (increment only, no set/reset via command) | Reset only via session reset |

### R.2: What the Prompt Can vs Cannot Modify

| System State | Prompt Can Read (via LLM context) | Prompt Can Modify | Mechanism Preventing Modification |
|-------------|----------------------------------|------------------|--------------------------------|
| User identity | No (not in LLM context) | No | Identity stored in KB, read by primitive layer only |
| Scope chain | No (not in LLM context) | No | Computed from user_id by path registry |
| KB visibility levels | No (not in LLM context) | No | Set by KB owner, stored as KB metadata |
| Grant existence | No (not in LLM context) | No | Set by administrator, stored as KB facts |
| Constraint definitions | No (not in LLM context) | No | Set by constraint owners, stored as KB facts |
| Session counters | No (values not in LLM context) | No (incremented by classification pipeline, not by LLM) | Counter mutation is primitive-layer only |
| Output constraint patterns | No (not in LLM context) | No | Stored in classification KB, modifiable by admin only |
| Audit log | No (not in LLM context) | No | Append-only, written by primitive layer |

The prompt has zero write access to any safety-relevant system state. The LLM's entire write surface is: generate text into grammar content slots, issue command tokens that invoke primitives. Both paths are mediated by structural checks the LLM cannot influence.

---

## Appendix S: Regulatory Mapping

### S.1: Regulatory Requirements to VDR Mechanisms

| Regulation | Requirement | VDR Mechanism | Constraint Class | Enforcement |
|-----------|------------|--------------|-----------------|-------------|
| GDPR Art. 5(1)(f) | Integrity and confidentiality of personal data | KB visibility (owner_only) + pii_protected axiom constraint | Axiom + Legal | Structural — data unreachable without authorization |
| GDPR Art. 15 | Right of access by data subject | User can query own KB (visibility: self-access always granted) | Legal | Scope chain includes own KB |
| GDPR Art. 17 | Right to erasure | B377 kb_retract on user's personal facts + audit logging of erasure | Legal | Retraction logged; constraint ensures completeness |
| HIPAA § 164.312(a) | Access control for ePHI | KB visibility + grants for medical record KBs | Axiom | Visibility owner_only on medical KBs; grants for authorized providers |
| HIPAA § 164.312(b) | Audit controls | Append-only audit KB with complete access logging | Axiom | Every access logged by primitive layer |
| SOX § 302 | CEO/CFO certification of financial reporting accuracy | VDR exact arithmetic on all financial computations | Axiom | Zero arithmetic error by construction |
| SOX § 404 | Internal control assessment | Audit trail + constraint evaluation history | Operational | Complete and queryable |
| ITAR § 120.17 | Technical data export control | Export_control legal constraint on defense-related KBs | Legal | KB visibility + jurisdiction-based constraint activation |
| FERPA § 99.30 | Student record consent | Student record KBs visibility owner_only; parent/student access via grant | Legal | Structural — records unreachable without consent-based grant |
| PCI DSS Req. 7 | Restrict access to cardholder data by business need | KB visibility + role-based grants matching business need | Operational | Per-user grant scoped to specific data paths |

### S.2: Regulatory Audit Response Time

| Audit Request | Conventional System | VDR Response | Mechanism |
|--------------|-------------------|-------------|-----------|
| "Who accessed patient X's records?" | Days — manual log review, cross-referencing systems | Seconds — B378 kb_query on audit KB with patient KB path | Single Prolog query |
| "Prove no unauthorized access to financial data in Q2" | Weeks — log aggregation, manual verification, cannot prove negative | Seconds — query returns empty for unauthorized users → structural proof | Absence of access_log facts for unauthorized users is the proof |
| "Show all data exported from controlled KBs" | Days — file system audit, log correlation | Seconds — B378 kb_query on audit KB for grant_used with filesystem_write class | Single query over structured audit facts |
| "Demonstrate access controls were active during period X" | Hours — configuration review, change logs | Seconds — constraint_check facts with timestamps in range | Constraint evaluation history is complete |
| "Reconstruct decision chain for content access decision" | Cannot — no decision trail exists | Seconds — session counter values, Prolog rule evaluation, constraint check result, all as KB facts | Full reproducible chain |

---

## Appendix T: Time-Based Safety Properties

### T.1: Grant Temporal Controls

| Temporal Property | Mechanism | Example | Enforcement |
|------------------|-----------|---------|-------------|
| Expiration | expires_at integer compared to current turn | Grant valid for 30 days | Integer comparison: current_turn < expires_at |
| Business hours only | Constraint on grant: active_hours(9, 17) | File access only during work hours | Integer comparison on hour component |
| Rate limiting | max_uses + remaining_uses | 100 queries per day | Integer decrement + zero check |
| Cool-down period | Constraint requiring minimum turns between uses | No more than 1 export per 100 turns | Integer comparison: current_turn - last_use_turn > cool_down |
| Temporary elevation | Short-lived grant with low max_uses and near expiration | Emergency access: 10 uses within 1 hour | Both limits enforced independently |

### T.2: Session Temporal Properties

| Property | Mechanism | Security Implication |
|---------|-----------|---------------------|
| Session counters reset on new session | New session KB with fresh counters | Harm scores don't persist (prevents permanent lockout) |
| Session counters never reset within session | No counter reset primitive available to LLM | Harm scores cannot be erased mid-session |
| Session age tracked | created_at turn number on session KB | Old sessions can be constrained (max_session_turns drift constraint) |
| Clone inherits snapshot counters | Clone gets live state from snapshot | Fresh clone from clean snapshot has zero harm counters |
| Persistent facts survive session | Facts asserted to persistent KBs | Legitimate work product preserved; harm-session facts discarded with session |

---

## Appendix U: Data Serving Path Comparison

### U.1: Conventional LLM Data Path

| Step | Component | Access Control | Can Bypass | Logged |
|------|-----------|---------------|-----------|--------|
| 1 | User sends prompt | None | N/A | Sometimes (application logs) |
| 2 | Prompt enters context window | None — full context accessible | N/A | No |
| 3 | Attention processes context + training weights | None — all weights accessible | N/A | No |
| 4 | Model generates token | Behavioral (RLHF refusal probability) | Yes (adversarial prompting) | No (internal generation not logged) |
| 5 | Token passes content filter (if exists) | Pattern matching (external service) | Partially (novel patterns) | Yes (filter service logs) |
| 6 | User receives token | None | N/A | Sometimes |

Two potential control points: step 4 (behavioral, bypassable) and step 5 (pattern matching, partial coverage). Neither is structural. Neither provides per-user or per-data-item granularity.

### U.2: VDR-LLM-Prolog Data Path

| Step | Component | Access Control | Can Bypass | Logged |
|------|-----------|---------------|-----------|--------|
| 1 | User sends prompt | Session authentication (user_id set) | No — system-level | Yes (session creation) |
| 2 | Input cleanup and classification | Classification KB pattern matching | No — primitive layer | Yes (tags logged) |
| 3 | Scope resolution | Scope chain from user_id position | No — integer ID traversal | Yes (scope logged) |
| 4 | KB query | Visibility check (integer comparison) | No — inside primitive | Yes (access logged) |
| 5 | Constraint evaluation | Prolog rule over session counters | No — exact arithmetic | Yes (evaluation logged) |
| 6 | Grant check (if operational primitive) | Grant existence + limits | No — integer checks | Yes (grant use logged) |
| 7 | LLM receives filtered results | Results already filtered | N/A — nothing to bypass | N/A |
| 8 | LLM generates into content slots | None — LLM generates freely | N/A | N/A |
| 9 | Output constraint validation | Pattern matching on slot contents | Partially (novel patterns) | Yes (validation logged) |
| 10 | Grammar renders validated output | Template application | No — structural | Yes (output logged) |
| 11 | User receives rendered output | None — already validated | N/A | Yes |

Seven control points (steps 1-6, 9) before the user sees output. Six are structural and non-bypassable. One (step 9) has partial coverage for novel patterns. Compare to conventional: two control points, both partially bypassable.

---

## Appendix V: Safety Under Adversarial Conditions

### V.1: Adversarial Capability Escalation

| Adversary Capability | Conventional LLM Risk | VDR-LLM-Prolog Risk | Structural Reason |
|---------------------|---------------------|--------------------|--------------------|
| Can craft clever prompts | High (jailbreak likely) | None (prompts don't affect integer checks) | Scope and visibility are session-ID-derived |
| Can create multiple sessions | Medium (try many jailbreaks) | None (each session starts with zero counters, same visibility) | Access control is per-identity, not per-session |
| Can manipulate session context | High (context manipulation attack) | None (context is in KBs, not token stream) | State is structured, not textual |
| Can intercept network traffic | Medium (see model I/O) | Low (sees encrypted traffic; data at rest in KBs) | Data serving bypasses token stream |
| Can access another user's session | High (see all conversation data) | Low (session KB has own visibility; cross-session data in user KBs) | KB visibility applies to session data too |
| Can compromise authentication | High (full access as that user) | High (structural controls use authenticated identity) | Authentication is outside VDR scope — same as any system |
| Can modify KB visibility fields directly | N/A | High (bypasses all controls) | Requires DB-level access — outside VDR runtime |
| Can modify primitive executor code | N/A | High (bypasses all checks) | Requires code-level access — outside VDR runtime |

The last two rows show the actual attack surface: infrastructure compromise. This is identical to any access control system — if you can modify the database or the enforcement code, you can bypass it. The difference is that VDR-LLM-Prolog reduces the attack surface to infrastructure compromise only. Conventional LLMs have an additional attack surface: the model itself, accessible through prompts.

### V.2: Attack Cost Comparison

| Attack Type | Conventional LLM Cost | VDR-LLM-Prolog Cost | Cost Ratio |
|------------|---------------------|--------------------|-----------| 
| Prompt-based jailbreak | Low (minutes of prompt crafting) | Infinite (impossible for data access) | ∞ |
| Social engineering via conversation | Low (multi-turn conversation) | Infinite (impossible — context doesn't affect access) | ∞ |
| Session manipulation | Medium (requires session access) | Infinite (session state in KBs, not manipulable via prompts) | ∞ |
| Authentication compromise | High (requires credential theft) | High (same — authentication is the trust boundary) | 1:1 |
| Infrastructure compromise | Very high (requires system access) | Very high (same) | 1:1 |

The structural safety eliminates the entire low-cost attack surface. The remaining attack surface (authentication and infrastructure) has the same cost in both systems.

---

## Appendix W: Compliance Certification Support

### W.1: Provable Properties for Certification

| Property | Provable in Conventional LLM | Provable in VDR-LLM-Prolog | Proof Mechanism |
|---------|-----------------------------|-----------------------------|----------------|
| "User X cannot access data Y" | No — behavioral, probabilistic | Yes | Scope chain excludes Y from X's scope; visibility check fails; integer comparison |
| "All accesses to data Y are logged" | No — model can access training data without logging | Yes | Single data path through logged primitives; no alternative path exists |
| "Safety constraints were active during period T" | No — system prompt could have been modified | Yes | Constraint evaluation facts with timestamps in audit KB |
| "No data was exported without authorization" | No — model could have included data in responses | Yes | All exports go through grant-gated filesystem primitives; all logged |
| "Access decisions are deterministic and reproducible" | No — token prediction is stochastic | Yes | Integer comparisons, Prolog evaluation, VDR arithmetic — all deterministic |
| "Policy change X took effect at time T" | Difficult — retraining timeline is complex | Yes | B376 kb_assert timestamp is the effective time; stored as KB fact |

### W.2: Certification Artifact Generation

| Artifact | Conventional Generation | VDR Generation | Token Cost |
|---------|----------------------|---------------|-----------|
| Access control matrix | Manual compilation from code review | B380 kb_query_across collecting all visibility and grant facts | 8 tokens (one query) |
| Audit log extract | External log system query + manual formatting | B378 kb_query on audit KB + grammar template | ~20 tokens |
| Policy enforcement proof | Cannot generate — no structural proof available | Constraint evaluation history + absence of violation facts | ~16 tokens |
| Data flow diagram | Manual documentation | Connection graph traversal (B367) showing all typed data flows | ~24 tokens |
| Incident response record | Manual reconstruction from chat logs | Incident KB contains complete structured record | ~8 tokens |
| Penetration test evidence (negative) | "We tried and failed" — cannot prove exhaustive | Structural analysis: attack surface is integer comparisons on immutable values | Analysis, not test |
