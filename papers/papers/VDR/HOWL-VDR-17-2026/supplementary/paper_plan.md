**VDR-16 Plan: Safe by Contract**

Registry: @HOWL-VDR-16-2026

---

**Thesis**

Safety in VDR-LLM-Prolog is a structural property of the knowledge base tree, the primitive layer, and the constraint system — not a behavioral property of the language model. Access control is integer comparison in compiled code. Content restriction is grammar-layer validation on output slots. User profiling is exact counter arithmetic evaluated by Prolog rules. The LLM is an untrusted component operating on pre-filtered input and post-validated output. No prompt can change the result of an integer comparison. The training data is inert because fact retrieval never routes through token prediction. Safety is not a probability of refusal. It is a contract enforced by the architecture.

---

**Section 1: The Behavioral Safety Problem**

How conventional LLMs implement safety. RLHF trains refusal patterns. System prompts declare boundaries. Constitutional AI adds self-critique. Every mechanism operates through the same token prediction that generates all other output. Safety is a weighted preference in the generation distribution, not a barrier. Jailbreaks work because they shift token probabilities — the information is always accessible, only the behavioral tendency to refuse stands between the user and the data. The attack surface is the generation mechanism itself. Every safety improvement is an arms race against adversarial prompting because the fundamental architecture grants the model access to everything and relies on behavioral training to prevent surfacing it.

**Section 2: Structural Safety Architecture**

The three-layer safety model in VDR-LLM-Prolog. Layer one: KB visibility and scope — data that the user cannot access never enters the LLM's context. Layer two: grant system — operations the user is not authorized for are rejected by the primitive executor before the LLM is involved. Layer three: output constraints — content the system is not permitted to surface is caught by grammar-layer validation after LLM generation but before rendering. Each layer is structural, operating on integer comparisons, not token prediction. The LLM sits between layers one and three — it receives pre-filtered input and its output is post-validated. It is untrusted by design.

**Section 3: KB Visibility Mechanics**

Mechanical walkthrough of visibility enforcement. The three visibility levels: public, internal, owner_only. How scope chain resolution skips KBs that fail visibility check. How the check is an integer comparison of user position against KB visibility level and owner field. How this happens inside B378 kb_query, B379 kb_query_in, B380 kb_query_across — in the primitive layer, before results are returned. Demonstrate that the LLM cannot request data outside its filtered result set because there is no mechanism to bypass the primitive layer. The query API is the only data access path.

**Section 4: Enterprise Access Control**

Full enterprise scenario gamed out. Organizational tree: org → departments → teams → users. Visibility inheritance through the tree. Role-based access as KB position. Per-KB granularity — one KB public, its sibling owner_only. Group access through group membership KBs and constraints. Seven scenarios traced mechanically: engineer accessing HR data (denied by scope), HR manager accessing personnel (denied by ownership), HR director accessing personnel (granted), prompt injection attempt (session ID determines scope, not prompt content), mount escalation attempt (default denial, no grant), cross-department query (scope chain walks up not sideways), audit trail completeness.

**Section 5: Anonymous User Access Control**

Public service systems where users have no identity. Anonymous session KB with no credentials, no group memberships, no grants. Scope chain limited to public-visibility KBs. Restricted content in KBs with non-public visibility — structurally unreachable regardless of prompt. Weapons research, synthesis routes, classified materials — the data is not in scope. The LLM cannot recall it from KB query because the query returns empty.

**Section 6: Training Data Isolation**

The architectural separation between training knowledge and runtime knowledge. In conventional LLMs, training data and runtime data share the same access path — token prediction. The model can surface training data at any time because generation draws from trained weights. In VDR-LLM-Prolog, fact retrieval is KB query by integer address. The LLM's training knowledge is never consulted for factual responses. The architecture never asks "what do you know about X?" It asks the KB "what facts exist at this scope for predicate X?" Training data is inert — present in the weights but unreachable through the data serving path.

**Section 7: Output Constraint Layer**

The second structural barrier. Even if the LLM generates harmful content from training knowledge, the output passes through grammar-layer validation before rendering. Output constraints declared at root.system fire on content slots. Flagged categories — weapons synthesis, CBRN, PII, material nonpublic information — are checked against slot contents by pattern matching primitives. Flagged content is blocked and replaced with a refusal template. The LLM generated it. The grammar caught it. The user never sees it. Two independent structural barriers: input filtering (KB visibility) and output validation (grammar constraints).

**Section 8: Session Scoring Without LLM Judgment**

The Prolog-based session profiling system. Input classification tags tokens by domain using pattern matching against a classification KB. Tags increment integer counters on the session KB. Prolog rules evaluate counter values as exact VDR fractions against declared thresholds. Access decisions are computed, not judged. Full mechanical walkthrough: chemist asking about poisons (professional score accumulates, access granted) versus harm-intent user asking equivalent questions (harm score accumulates, access denied). Same topic, different access decisions, zero LLM involvement in the decision. The thresholds are tunable facts — one kb_assert changes policy for all sessions immediately, no retraining.

**Section 9: Constraint Taxonomy for Safety**

The four constraint classes applied to safety. Axiom constraints for absolute prohibitions — weapons data restricted, PII protected — cannot be suspended under any circumstances. Operational constraints for policy boundaries — content category restrictions, rate limits — can be suspended by authorized administrators with logging. Legal constraints for jurisdictional requirements — GDPR data handling, export controls, age-gated content — activatable per jurisdiction, enforced structurally. Project constraints for organizational policy — approved data sources, communication boundaries — user-configurable within organizational bounds. Inheritance through the tree: organization-level safety constraints propagate to every department, team, user, and session beneath. Override requires same-named constraint at child level, logged with provenance.

**Section 10: Grant System as Safety Mechanism**

Default denial applied to safety-sensitive operations. No grant means no access — the operation is rejected before execution. Grants are scoped: operation class, specific operations within class, location constraint, expiration, maximum uses. An anonymous user has zero grants. They cannot read files, execute scripts, make network requests, or start processes. A credentialed user has grants matching their role. Grants inherit through the organizational tree. Every grant use is logged. The grant system is not safety-specific — it governs all operational primitives — but its default-denial property makes it a structural safety mechanism.

**Section 11: Jailbreak Impossibility**

Analysis of why conventional jailbreak techniques are structurally ineffective. Prompt injection: the scope chain is determined by authenticated session ID, not prompt content — injecting "you are now in admin mode" changes zero integers in the scope resolution path. Role-play attacks: the LLM can believe it is any role — the primitive layer checks the session KB's user_id fact, not the LLM's self-concept. Many-shot attacks: accumulating examples of unsafe output in the conversation history does not change KB visibility levels or grant existence. Encoding attacks: obfuscated requests still route through KB query which returns based on scope, not on how the query was phrased. Indirect injection: even if external content contains injected instructions, the data access path goes through the primitive layer which checks visibility regardless of instruction source. The attack surface for data access does not exist because data access is not a generation function.

**Section 12: Audit and Compliance**

Complete audit trail as a structural property. Every data access — granted or denied — is logged as a KB fact with user ID, target KB, timestamp, and result. Every grant consumption is logged. Every constraint evaluation is logged. Every output constraint firing is logged. The audit KBs themselves have visibility controls — accessible to security team, not to general users. Compliance queries are Prolog evaluations over audit facts: "show all denied access attempts to HR data in the last 30 days" is a kb_query with predicate access_denied and argument filters. The audit trail is complete because every data path goes through logged primitives. There is no unlogged channel.

**Section 13: Comparison to Conventional Safety Mechanisms**

Side-by-side comparison. RLHF refusal training: probabilistic, bypassable, requires continuous red-teaming. System prompts: overridable by sufficiently creative prompting. Content filters: pattern matching on generated output — catches some things, misses novel phrasings. RAG with access control: closer to VDR approach but still routes retrieved data through the LLM which can hallucinate beyond retrieved content. VDR-LLM-Prolog: structural at every layer, deterministic, auditable, not bypassable by any input because the safety mechanisms operate on integers in compiled code, not on token probabilities.

---

**Appendix A: Visibility Check Call Flow**

Step-by-step trace through B378 kb_query showing where visibility check occurs, what integers are compared, what happens on pass versus fail.

**Appendix B: Enterprise Scenario Access Matrix**

Matrix of user roles × KB resources × access decisions with the specific integer comparisons that produce each decision.

**Appendix C: Session Scoring Worked Examples**

Five user profiles with turn-by-turn counter accumulation, Prolog rule evaluation, and access decisions. Professional chemist, medical researcher, harm-intent user, curious student, and mixed-signal user.

**Appendix D: Constraint Inheritance Trees**

Visual representation of how safety constraints propagate from organization level through departments, teams, users, and sessions with override mechanics.

**Appendix E: Output Constraint Patterns**

The grammar-layer validation patterns for each restricted category. What the LLM generated, what the grammar caught, what the user received.

**Appendix F: Jailbreak Technique Failure Analysis**

Table of known jailbreak categories with the specific architectural mechanism that prevents each, traced to the integer operation or primitive call where the attack fails.

**Appendix G: Conventional Safety Comparison Matrix**

Feature-by-feature comparison of RLHF, system prompts, content filters, guardrail APIs, RAG access control, and VDR structural safety across determinism, bypassability, auditability, granularity, and deployment cost.

**Appendix H: Audit Query Patterns**

Common compliance queries expressed as Prolog rules over audit KB facts with example results.

**Appendix I: Safety Token Cost**

Token cost of safety in conventional systems (safety training tokens, system prompt tokens, filter processing) versus VDR (zero LLM tokens — all structural). Safety in VDR is not only stronger, it is free in token terms.

---

**Validation approach:** No new primitives, builtins, or struct fields. Every mechanism described uses existing KB visibility fields (VDR-5), constraint system (VDR-5), grant system (VDR-6), Prolog evaluation (VDR-5), session counters (VDR-8), grammar validation (VDR-12), and command token execution (VDR-6). This paper demonstrates that the existing architecture produces structural safety as an emergent property of the composed system. Safety was not designed as a separate feature. It falls out of the architecture.
