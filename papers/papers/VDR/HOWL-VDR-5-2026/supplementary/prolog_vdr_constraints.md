## Constraints as First-Class Objects in VDR-Prolog

### What LLMs Actually Lack

Current LLMs have no persistent constraint awareness. They process tokens sequentially, generate responses based on pattern matching against training data, and have no mechanism to track whether they are operating within declared boundaries. Every conversation is a fresh start with no structural memory of what was opened, what was resolved, what rules apply, and what topics are parked.

This is not a training data problem. It is an architecture problem. The model has no place to put constraints, no mechanism to check them, and no way to track conversational state as a structured object rather than as context tokens that eventually scroll out of the window.

VDR-Prolog can fix this because constraints are facts, and facts persist in the knowledge base, and facts are queryable, and facts can trigger rules.

---

### Constraint as a Term Type

Add to the TermType enum:

```
constraint,       // A named constraint with scope, status, and metadata
constraint_set,   // A collection of constraints (enable/disable as a group)
topic,            // A conversational topic with open/closed/parked state
scope,            // A boundary context: legal, operational, project, conversation
```

A constraint is not a boolean flag. It is a structured object:

```
Constraint = struct {
    name: Text,              // "no_medical_advice", "budget_under_10k", "python_38_compat"
    scope: Text,             // "legal", "operational", "project", "conversation"
    status: enum { 
        active,              // currently enforced
        suspended,           // temporarily disabled, tracked
        violated,            // was active, condition breached
        satisfied,           // checked and passing
        parked,              // deferred, not currently relevant
    },
    condition: Fact,         // the logical condition that defines the constraint
    on_violation: Text,      // "warn", "block", "log", "escalate"
    activated_at: i32,       // step/turn when activated
    last_checked: i32,       // step/turn when last verified
    source: Text,            // who/what declared this constraint
};
```

---

### The Four Constraint Domains

#### 1. Operational Rules

These are the rules of the system itself. They exist whether anyone declares them or not.

```
Fact: constraint("vdr_exact", scope("operational"), active,
        condition(all_arithmetic_exact), on_violation("block"),
        source("system")).

Fact: constraint("python_38_compat", scope("operational"), active,
        condition(no_walrus_operator, no_match_statement, no_union_pipe),
        on_violation("block"),
        source("project_config")).

Fact: constraint("30_sec_runtime", scope("operational"), active,
        condition(estimated_runtime_under(30)),
        on_violation("warn"),
        source("user")).
```

These are always on. The system checks them before generating output. "Will this code run on Python 3.8?" is not a style preference — it is a constraint that can be verified by inspecting the generated AST for forbidden constructs.

#### 2. Axioms

These are mathematical or logical invariants that cannot be violated without the system being wrong.

```
Fact: constraint("probability_sums_to_one", scope("axiom"), active,
        condition(forall(distribution(D), sum(D, 1))),
        on_violation("error"),
        source("mathematics")).

Fact: constraint("attention_non_negative", scope("axiom"), active,
        condition(forall(attention_weight(W), W >= 0)),
        on_violation("error"),
        source("mathematics")).

Fact: constraint("gradient_matches_derivation", scope("axiom"), active,
        condition(forall(parameter(P), step(S), 
            value_at(P, S) =:= value_at(P, S-1) - lr * gradient_at(P, S-1))),
        on_violation("error"),
        source("vdr_autodiff")).
```

Axioms cannot be suspended or parked. They can only be active or violated. A violation of an axiom is a bug, not a policy decision.

#### 3. Legal and Policy Constraints

These come from external requirements — regulations, company policies, user preferences, safety rules.

```
Fact: constraint("no_medical_diagnosis", scope("legal"), active,
        condition(output_not_contains(medical_diagnosis)),
        on_violation("block"),
        source("policy")).

Fact: constraint("cite_sources", scope("policy"), active,
        condition(claims_have_citations),
        on_violation("warn"),
        source("user_preference")).

Fact: constraint("gdpr_no_pii_in_logs", scope("legal"), active,
        condition(log_entries_contain_no_pii),
        on_violation("block"),
        source("regulation")).
```

Legal constraints can be activated or deactivated by context. A medical conversation might suspend "no_medical_diagnosis" and activate "medical_disclaimer_required" instead. The transitions are logged as facts in the knowledge base — so there is a record of which constraints were active when, and who changed them.

#### 4. Project Constraints

These are specific to the current work context.

```
Fact: constraint("zig_014_syntax", scope("project"), active,
        condition(code_uses_zig_014),
        on_violation("block"),
        source("user")).

Fact: constraint("prefer_i32", scope("project"), active,
        condition(integer_types_are_i32_unless_justified),
        on_violation("warn"),
        source("user")).

Fact: constraint("no_changes_beyond_requested", scope("project"), active,
        condition(diff_only_touches_requested_areas),
        on_violation("block"),
        source("user")).

Fact: constraint("vdr_remainder_not_residual", scope("project"), active,
        condition(naming_uses_remainder_not_residual),
        on_violation("warn"),
        source("vdr_spec")).
```

These are the user preferences and project rules that currently exist only in system prompts and are easily forgotten or inconsistently applied. As Prolog facts, they are persistent, queryable, and checkable.

---

### Set Theory Against Constraints

Constraints form sets. Sets can be combined, intersected, and differenced. This gives the system the ability to reason about groups of constraints as first-class objects.

```
Fact: constraint_set("vdr_project", 
        ["vdr_exact", "python_38_compat", "30_sec_runtime", 
         "vdr_remainder_not_residual", "no_changes_beyond_requested"]).

Fact: constraint_set("safety", 
        ["no_medical_diagnosis", "no_weapons_info", "gdpr_no_pii_in_logs"]).

Fact: constraint_set("math_axioms",
        ["probability_sums_to_one", "attention_non_negative", 
         "gradient_matches_derivation"]).
```

Rules for set operations:

```
Rule: active_constraints(Set, Active) :-
    constraint_set(Set, Members),
    findall(C, (member(C, Members), constraint(C, _, active, _, _, _)), Active).

Rule: all_satisfied(Set) :-
    constraint_set(Set, Members),
    forall(member(C, Members), constraint_satisfied(C)).

Rule: violations_in(Set, Violations) :-
    constraint_set(Set, Members),
    findall(C, (member(C, Members), constraint(C, _, violated, _, _, _)), Violations).

Rule: enable_set(Set) :-
    constraint_set(Set, Members),
    forall(member(C, Members), activate_constraint(C)).

Rule: disable_set(Set) :-
    constraint_set(Set, Members),
    forall(member(C, Members), suspend_constraint(C)).

Rule: constraints_excluding(Base, Exclude, Result) :-
    constraint_set(Base, B),
    constraint_set(Exclude, E),
    subtract(B, E, Result).

Rule: constraints_union(Set1, Set2, Result) :-
    constraint_set(Set1, S1),
    constraint_set(Set2, S2),
    union(S1, S2, Result).
```

Now the system can reason: "enable the VDR project constraints but disable the 30-second runtime limit for this specific task." Or: "what constraints are active in both the safety set and the project set?" Or: "which constraints in the current active set are violated?"

---

### Conversation Tracking

This is where constraints transform from a verification system into a conversation management system.

#### Topics as Structured Objects

```
Topic = struct {
    name: Text,
    status: enum { open, closed, parked, branched },
    opened_at: i32,        // turn number
    closed_at: i32,        // -1 if still open
    parked_at: i32,        // -1 if not parked
    parent: Text,          // parent topic if this is a subtopic
    children: []Text,      // subtopics
    summary: Text,         // what this topic is about
    pending_items: []Text,  // things unresolved within this topic
};
```

Asserted as Prolog facts:

```
Fact: topic("vdr_core", open, turn(1), parent(none)).
Fact: topic("vdr_gym_testing", open, turn(5), parent("vdr_core")).
Fact: topic("transcendental_reach", closed, turn(12), parent("vdr_core")).
Fact: topic("llm_architecture", open, turn(20), parent("vdr_core")).
Fact: topic("prolog_integration", open, turn(30), parent("llm_architecture")).

Fact: pending("vdr_gym_testing", "fix_maxflow_bfs").
Fact: pending("vdr_gym_testing", "fix_gym21_decay_threshold").
Fact: pending("llm_architecture", "gaussian_elimination").
Fact: pending("llm_architecture", "cross_entropy_loss").
```

#### Rules for Conversation State

```
Rule: should_close(Topic) :-
    topic(Topic, open, _, _),
    not(pending(Topic, _)),
    not(topic(Child, open, _, parent(Topic))).
    % A topic should close when it has no pending items and no open children.

Rule: should_park(Topic) :-
    topic(Topic, open, OpenedAt, _),
    current_turn(Now),
    Now - OpenedAt > 20,
    not(recently_discussed(Topic, 5)).
    % A topic should be parked if it's been open for 20+ turns with no recent activity.

Rule: recently_discussed(Topic, Window) :-
    current_turn(Now),
    last_mentioned(Topic, Turn),
    Now - Turn =< Window.

Rule: dangling_topics(Topics) :-
    findall(T, (topic(T, open, _, _), should_park(T)), Topics).

Rule: topic_depth(Topic, 0) :- topic(Topic, _, _, parent(none)).
Rule: topic_depth(Topic, D) :- 
    topic(Topic, _, _, parent(P)), 
    topic_depth(P, PD), 
    D is PD + 1.

Rule: deepest_open(Topic) :-
    topic(Topic, open, _, _),
    topic_depth(Topic, D),
    not((topic(Other, open, _, _), topic_depth(Other, D2), D2 > D)).
```

#### Functions Triggered by Topic State

The conversation tracker is not passive. It triggers actions:

```
Rule: on_topic_open(Topic) :-
    load_relevant_constraints(Topic),
    activate_constraint_set(Topic).

Rule: on_topic_close(Topic) :-
    verify_all_pending_resolved(Topic),
    summarize_topic(Topic),
    deactivate_constraint_set(Topic).

Rule: on_topic_park(Topic) :-
    snapshot_topic_state(Topic),
    log_park_reason(Topic),
    deactivate_constraint_set(Topic).

Rule: on_topic_resume(Topic) :-
    restore_topic_state(Topic),
    activate_constraint_set(Topic),
    list_pending_items(Topic).
```

When the user says "let's go back to the gym testing," the system:
1. Queries: `topic("vdr_gym_testing", parked, _, _)` — finds it parked
2. Fires: `on_topic_resume("vdr_gym_testing")`
3. Restores the constraint set for that topic
4. Lists pending items: "fix maxflow BFS, fix gym21 decay threshold"
5. The conversation continues from where it was parked, with full context

---

### The Wrap/Unwrap Pattern

Topics have a lifecycle: open → (work) → close, or open → (interrupted) → park → (resumed) → (work) → close. The system tracks this explicitly.

```
Rule: wrap(Topic) :-
    topic(Topic, open, _, _),
    summarize_current_state(Topic, Summary),
    assert(topic_summary(Topic, Summary)),
    retract(topic(Topic, open, _, _)),
    assert(topic(Topic, parked, _, _)),
    log(wrapped(Topic, Summary)).

Rule: unwrap(Topic) :-
    topic(Topic, parked, _, _),
    topic_summary(Topic, Summary),
    retract(topic(Topic, parked, _, _)),
    assert(topic(Topic, open, _, _)),
    present(Summary),
    list_pending(Topic),
    log(unwrapped(Topic)).
```

At any point the user (or the system) can ask:

```
?- dangling_topics(T).
% "What topics are open but seem stale?"

?- findall(P, pending(_, P), AllPending).
% "What items are pending across all topics?"

?- topic(T, open, _, parent("vdr_core")), pending(T, Item).
% "What's pending in the VDR subtopics?"
```

---

### How This All Connects

The VDR-LLM system now has three layers:

**Layer 1: Exact arithmetic.** VDR provides exact fractions for every value. Zero drift. Zero silent truncation. Every number is what it is.

**Layer 2: Logical provenance.** Prolog records how every value was derived, what it depends on, and what constraints it satisfies. Every value has a reason.

**Layer 3: Constraint and conversation management.** Constraints are first-class objects that can be activated, suspended, grouped, queried, and verified. Topics are tracked objects with lifecycle state. Pending items are persistent. Nothing is forgotten unless explicitly pruned by a declared policy.

The three layers reinforce each other. Layer 1 ensures that constraint checking is exact (not approximate). Layer 2 ensures that constraint violations can be traced to their root cause. Layer 3 ensures that the system maintains awareness of what rules apply, what topics are active, and what work remains.

An LLM running on this stack would not just generate tokens. It would generate tokens within declared constraints, with full provenance for every intermediate computation, with explicit tracking of what was asked, what was answered, what was deferred, and what remains open. And every number in every computation would be an exact fraction that the system can prove is correct by producing its derivation chain.

That is what a constrained, provenance-aware, exact-arithmetic language model looks like. Not a float-based pattern matcher with a system prompt. A logical system that knows what it knows, knows why it knows it, knows what rules it is operating under, and can prove all three.
