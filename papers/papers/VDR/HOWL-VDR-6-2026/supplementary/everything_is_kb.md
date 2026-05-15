# VDR-Prolog: KBs All the Way Down
## Everything Is a Knowledge Base, Everything Is Surfaceable, Everything Is Selectable

---

## 1. The Unification

The insight that completes the architecture is that there is no special category of object in the system. Projects are KBs. Conversations are KBs. Tags are KBs. Groups of tags are KBs. Views are KBs. Reminders are KBs. The prompt context itself is assembled from selected KBs. The selection interface is a query over KBs.

There is one data structure. It holds facts, rules, constraints, and working data. It has a parent, children, and a name. It can be activated, deactivated, snapshotted, tagged, grouped, queried, surfaced, and composed with other KBs.

Every operation in the system — from exact arithmetic to conversation tracking to file management to prompt assembly — operates on KBs. The system does not have conversations and also knowledge bases. The conversations are knowledge bases. The system does not have projects and also knowledge bases. The projects are knowledge bases. The system does not have tags and also knowledge bases. The tags are knowledge bases that reference other KBs.

---

## 2. Conversations as KBs

A conversation is a sequence of turns. Each turn has a speaker (user or system), content, timestamp, and associated state (active topic, active constraints, active working data). This is a fact set.

```
Fact: turn(conv("vdr_may16"), turn_num(1), speaker(user), 
        content("not zig, math. read this paper and explain mechanically"),
        timestamp(2026, 5, 16, 9, 0, 0),
        active_topic("vdr_review")).

Fact: turn(conv("vdr_may16"), turn_num(2), speaker(system),
        content_ref(response_kb("vdr_may16_r2")),
        timestamp(2026, 5, 16, 9, 0, 45),
        active_topic("vdr_review")).
```

The conversation KB has:
- Facts: every turn, every topic transition, every constraint activation
- Rules: conversation-specific rules (formatting preferences, response style)
- Constraints: conversation-specific constraints (language, formality, scope)
- Working data: values established during the conversation
- Children: sub-conversations, branches, sidebar discussions

The response content itself can be a reference to another KB rather than inline text. Long responses, code outputs, data tables — these are stored in their own KBs and referenced by address. The conversation KB stays lightweight. The content KBs hold the bulk.

### 2.1 Conversation Selection

Instead of scrolling through a list of conversations titled by their first message (the current UX pattern), you query:

```
?- conversation(C), topic(C, "vdr"), 
   last_active(C, Date), Date > date(2026, 5, 1).
% All VDR conversations active in May 2026

?- conversation(C), contains_pending(C, _).
% All conversations with unresolved pending items

?- conversation(C), contains_binding(C, "bob_age", _).
% All conversations that discussed Bob's age
```

The selection is by content, not by title. You find the conversation you want by querying what it contains, not by remembering what you called it.

### 2.2 Conversation Composition

You can combine conversations. "Take the VDR gym results from conversation A and the prolog design from conversation B and start a new conversation C with both in scope."

```
Action: create_conversation("vdr_prolog_combined")
Action: add_parent("vdr_prolog_combined", "vdr_gym_results")  
Action: add_parent("vdr_prolog_combined", "prolog_design")
```

Conversation C inherits from both A and B. All their facts, bindings, and pending items are visible in C. The scoping rules handle the rest. If both conversations defined "bob_age," the system detects the ambiguity and asks which scope takes priority.

---

## 3. Projects as KBs

A project is a KB with a specific structure:

```
KB: project_vdr
  facts:
    project_name("VDR Exact Arithmetic")
    project_started(2026, 3, 1)
    project_language("python")
    project_repo("/home/alice/projects/vdr/")
  
  constraints:
    python_38_compat, exact_arithmetic, remainder_not_residual
  
  working_data:
    total_modules: 24
    total_tests: 705
    current_priority: "gaussian_elimination"
  
  children:
    [kb_vdr_core, kb_vdr_llm, kb_vdr_gyms, kb_vdr_papers, 
     kb_vdr_math_series, kb_vdr_prolog_spec]
  
  conversations:
    [conv_vdr_may16, conv_vdr_may10, conv_vdr_apr28, ...]
  
  tags: ["exact_arithmetic", "python", "ml", "prolog", "active"]
```

The project KB contains everything about the project: its configuration, its constraints, its state, its sub-components, and its conversation history. Selecting the project activates all of this. Deselecting it hides all of it.

### 3.1 Project Selection

```
User: "/projects"

System surfaces:
  [active] project_vdr — 24 modules, 705 tests, 6 conversations
  [active] project_story_b — 3 characters, 1 chapter, 2 conversations  
  [parked] project_taxes_2025 — filed, archived
  [parked] project_garden — 12 plants tracked, last active March

User clicks: project_vdr
  → activates kb_project_vdr and all children
  → loads constraints
  → loads working data
  → lists recent conversations and pending items
```

No typing. No describing. No "I was working on that exact arithmetic thing, you know the one with the fractions." Click the project. The system loads everything. Every value is exact. Every constraint is active. Every pending item is listed.

---

## 4. Tags as KBs

A tag is a KB whose facts are references to other KBs. It is a named group.

```
KB: tag_active_projects
  facts:
    tagged(project_vdr)
    tagged(project_story_b)
  
  constraints:
    all_tagged_are_projects  // type constraint
  
  rules:
    total_tests(N) :- 
        findall(T, (tagged(P), project_tests(P, T)), Tests),
        sum_list(Tests, N).
```

The tag is itself a KB. It can have its own rules that aggregate across tagged items. "How many tests across all active projects?" is a query against the tag KB.

### 4.1 Tag Nesting

Tags can contain tags. "Machine learning" contains "VDR-LLM" and "transformer experiments." "Active work" contains "machine learning" and "story writing."

```
KB: tag_ml
  tagged(project_vdr_llm)
  tagged(project_transformer_experiments)

KB: tag_active_work
  tagged(tag_ml)
  tagged(tag_story_writing)
```

Querying tag_active_work returns all KBs transitively: project_vdr_llm, project_transformer_experiments, and everything under tag_story_writing. The nesting is arbitrary depth. KBs all the way down.

### 4.2 Tag Operations

```
User: "/tag project_vdr as 'exact_arithmetic' and 'python'"

System:
  kb_assert(tag_exact_arithmetic, tagged(project_vdr))
  kb_assert(tag_python, tagged(project_vdr))

User: "/show tag:exact_arithmetic"

System surfaces:
  tag: exact_arithmetic
    project_vdr — 24 modules, 705 tests
    project_math_series — MATH-3, MATH-4, Q335 basis
    note_fraction_arithmetic — reference notes on exact rationals

User: "/group tag:exact_arithmetic tag:python as tag:exact_python"

System:
  Creates: KB tag_exact_python
  Facts: intersection of tagged items from both source tags
  Result: project_vdr (the only item in both)
```

---

## 5. Views as KBs

A view is a KB that defines a query and presents its results as a virtual fact set. It does not store data. It computes it on demand from other KBs.

```
KB: view_all_pending
  rule: 
    view_fact(pending(Topic, Item)) :-
        topic(Topic, open, _, _),
        pending(Topic, Item).

KB: view_stale_topics
  rule:
    view_fact(stale(Topic, IdleTurns)) :-
        topic(Topic, open, Opened, _),
        current_turn(Now),
        IdleTurns is Now - Opened,
        IdleTurns > 20,
        not(recently_discussed(Topic, 5)).

KB: view_constraint_violations
  rule:
    view_fact(violation(KB, Constraint)) :-
        kb_exists(KB),
        in_scope(KB),
        kb_constraints(KB, Cs),
        member(C, Cs),
        not(constraint_satisfied(C)).

KB: view_denominator_growth
  rule:
    view_fact(large_denom(Param, Step, Denom)) :-
        parameter_value(Param, step(Step), fraction(_, Denom)),
        Denom > 2^32.
```

Views are surfaceable like any KB. "/show view:all_pending" runs the query and displays the results. The view does not cache — it recomputes from current state every time. But it can be snapshotted ("snapshot view:all_pending as pending_may16") to freeze the results at a point in time, creating a new KB with the computed facts.

---

## 6. Reminders and Watches as KB Constraints

A reminder is a constraint with a check-every-turn trigger and an acknowledgment requirement.

```
Fact: reminder("check_test_results",
    condition(task("task_001", _, _, _, status(completed), _, _, _)),
    message("Test suite task_001 has completed. Review results."),
    check_frequency(every_turn),
    requires_ack(true),
    created_at(turn(45)),
    acknowledged(false),
    topic("vdr_testing")).
```

Every turn, the system evaluates all active reminders:

```
Rule: pending_reminders(Reminders) :-
    findall(R, 
        (reminder(R, condition(C), _, check_frequency(every_turn), _, _, acknowledged(false), _),
         call(C)),
        Reminders).
```

If the condition is met and the reminder is unacknowledged, the system surfaces it:

```
LLM: [responds to user's question]

---
Reminder (unacknowledged):
  "Test suite task_001 has completed. Review results."
  [Acknowledge] [Snooze 5 turns] [Dismiss]
```

The user must explicitly acknowledge, snooze, or dismiss. Until then, the reminder appears every turn. This is not the LLM remembering to mention something. This is a constraint that fires every turn and produces output until satisfied.

### 6.1 Watches

A watch is a reminder that fires on state change rather than on every turn:

```
Fact: watch("loss_spike",
    condition(loss_at(step(S), L), L > fraction(100, 1)),
    message("Loss exceeded 100 at step {S}: {L}"),
    watch_type(on_change),
    topic("vdr_training")).

Fact: watch("bob_age_changed",
    condition(binding_changed("characters_b", "bob_age")),
    message("Bob's age was modified in story B"),
    watch_type(on_change),
    topic("story_b")).

Fact: watch("new_pending",
    condition(pending(Topic, Item), not(seen_pending(Topic, Item))),
    message("New pending item in {Topic}: {Item}"),
    watch_type(on_change),
    topic("project_vdr")).
```

Watches are more efficient than per-turn reminders for conditions that change rarely. The system only evaluates them when relevant KB facts change.

### 6.2 Prompted Constraints

The user can attach constraints directly to the prompt generation process:

```
User: "/remind me about the maxflow BFS fix whenever we discuss graph theory"

System creates:
  reminder("maxflow_fix",
      condition(active_topic(T), topic_contains(T, "graph")),
      message("Pending: fix maxflow BFS loop termination in gym_16"),
      check_frequency(on_topic_enter),
      requires_ack(true),
      topic("vdr_gyms")).
```

```
User: "/check each turn if any constraint is violated and report it"

System creates:
  watch("constraint_monitor",
      condition(violations(_, Vs), Vs \= []),
      message("Constraint violations detected: {Vs}"),
      watch_type(every_turn),
      topic("global")).
```

```
User: "/when the training loss drops below 0.01, tell me"

System creates:
  watch("loss_target",
      condition(loss_at(step(_), L), L < fraction(1, 100)),
      message("Training loss has dropped below 0.01"),
      watch_type(on_change),
      requires_ack(true),
      topic("vdr_training")).
```

These are not system prompt instructions that the LLM might forget. They are KB facts with trigger conditions that the Prolog engine evaluates mechanically. The LLM does not need to remember them. The constraint system enforces them.

---

## 7. Prompt Assembly From Selected KBs

The prompt sent to the LLM is not a flat text string. It is assembled from the selected KB scope.

### 7.1 Context Assembly

```
Rule: assemble_context(Context) :-
    active_kbs(KBs),
    collect_constraints(KBs, Constraints),
    collect_working_data(KBs, WorkingData),
    collect_pending(KBs, Pending),
    collect_recent_turns(ActiveConversation, 20, RecentTurns),
    collect_reminders(Reminders),
    Context = context(
        constraints: Constraints,
        working_data: WorkingData,
        pending: Pending,
        recent_turns: RecentTurns,
        reminders: Reminders
    ).
```

The context is structured. It is not "here is everything pasted into a text block." It is:
- These constraints are active (from the selected KBs)
- These bindings are in scope (from working data sets)
- These items are pending (from topic trackers)
- These are the recent turns (from the conversation KB)
- These reminders need attention (from watch/reminder KBs)

### 7.2 User-Controlled Context

The user can explicitly control what is in context:

```
User: "/context add kb_vdr_core"
  → adds vdr_core facts, constraints, and working data to context

User: "/context remove kb_story_b"
  → removes story_b from context (even if topic would include it)

User: "/context only kb_vdr_llm kb_vdr_training"
  → sets context to exactly these two KBs plus global

User: "/context show"
  → surfaces the complete current context assembly:
    Active KBs: [global, project_vdr, vdr_core, vdr_llm, vdr_training]
    Constraints: [exact_arithmetic, python_38, sum_to_one, ...]
    Working data: {total_modules: 24, lr: 1/10, ...}
    Pending: [gaussian_elimination, cross_entropy_loss]
    Reminders: [maxflow_fix (unacked), loss_target (watching)]
    Recent turns: 20 from conv_vdr_may16
```

### 7.3 Context as a KB

The assembled context is itself a KB. It can be snapshotted:

```
User: "/snapshot context as context_before_refactor"

System: creates KB context_before_refactor with all current context facts frozen.
```

It can be restored:

```
User: "/restore context context_before_refactor"

System: sets active KBs, constraints, working data to the snapshot state.
```

It can be shared:

```
User: "/export context as vdr_llm_context.json"

System: serializes the complete context assembly as a portable KB.
```

Another user imports it and has the exact same context: same constraints, same working data, same pending items. The conversation is reproducible because the context is data, not ephemeral token state.

---

## 8. The Selection Interface

The user interface for managing KBs is not a command line. It is a selection panel where KBs are visible, taggable, groupable, and directly activatable.

### 8.1 KB Browser

```
/browse

Projects:
  [●] project_vdr (24 modules, 6 convs)        [tags: exact, python, ml]
  [●] project_story_b (3 chars, 2 convs)        [tags: fiction, active]
  [○] project_taxes (archived)                   [tags: finance, done]
  [○] project_garden (parked)                    [tags: personal, seasonal]

Tags:
  exact_arithmetic (2 items)
  python (3 items)
  active (2 items)
  ml (1 item)

Views:
  all_pending (7 items currently)
  stale_topics (2 items currently)
  constraint_violations (0 — all clear)

Recent conversations:
  conv_vdr_may16 (today, 50 turns, active)
  conv_vdr_may10 (last week, 32 turns, closed)
  conv_story_may14 (2 days ago, 20 turns, parked)

● = active   ○ = inactive
```

Click to activate. Click again to deactivate. Drag to group. Right-click to tag. The selection state is itself a KB (the context KB), so it persists across sessions.

### 8.2 Multi-Select

Select multiple KBs to bring them all into scope:

```
Selected: [project_vdr] + [conv_vdr_may16] + [view_all_pending]

Context now includes:
  - All VDR project facts, constraints, working data
  - The current conversation history
  - A live view of all pending items across all topics
```

### 8.3 Occlude

Deselect KBs to remove them from scope:

```
User: "/occlude kb_story_b"

  → story_b and all its children become invisible
  → No query will reach them
  → No binding from them will resolve
  → No constraint from them will fire
  → They still exist, untouched, ready to reactivate
```

Occlusion is the inverse of selection. It is explicit, logged, and reversible.

### 8.4 Group as KB

```
User: "/group project_vdr project_math_series as group_exact_work"

System creates:
  KB: group_exact_work
    tagged(project_vdr)
    tagged(project_math_series)
    
User: "/activate group_exact_work"
  → Both projects activate
  → All their constraints, working data, and children come into scope
  → The group KB's own constraints (if any) also activate

User: "/deactivate group_exact_work"
  → Both projects deactivate in one action
```

Groups are KBs. Groups can contain groups. The group hierarchy is a KB tree. Activating a group activates everything it contains, recursively.

---

## 9. Meta-Analysis via KB Queries

Because everything is a KB, you can query across everything:

```
?- kb_exists(KB), kb_type(KB, project), 
   kb_fact_count(KB, N), N > 100.
% Projects with more than 100 facts

?- kb_exists(KB), kb_last_modified(KB, Date), 
   Date < date(2026, 4, 1).
% KBs not modified since April — candidates for archiving

?- tag_contains(Tag, project_vdr), 
   tag_contains(Tag, project_math_series).
% Tags that contain both VDR and math series — shared categories

?- conversation(C), turn_count(C, N), N > 40,
   contains_binding(C, Key, _), 
   not(binding_persisted(Key)).
% Long conversations with bindings that were never saved to a project KB
% (potential data loss candidates)

?- kb_exists(KB), kb_constraint_count(KB, 0), 
   kb_type(KB, project).
% Projects with no constraints — governance gap

?- reminder(R, _, _, _, _, acknowledged(false), _),
   reminder_age(R, Age), Age > 10.
% Unacknowledged reminders older than 10 turns — user attention needed
```

This is system introspection. The system can reason about its own structure. "Am I organized well?" is a query. "What have I forgotten?" is a query. "What is growing without bounds?" is a query. "Which KBs are redundant?" is a query.

---

## 10. The Recursive Structure

The pattern is recursive and complete:

- A **value** is an exact VDR fraction.
- A **fact** is a predicate over values, stored in a KB.
- A **KB** is a collection of facts, rules, constraints, and working data.
- A **tag** is a KB whose facts reference other KBs.
- A **group** is a KB whose facts reference other KBs (same as tag, different semantics).
- A **view** is a KB whose facts are computed from queries over other KBs.
- A **conversation** is a KB whose facts are turns, topics, and state transitions.
- A **project** is a KB with project-specific structure.
- A **user account** is a KB with identity and permissions.
- A **reminder** is a KB fact with a trigger condition and acknowledgment state.
- A **context** is a KB assembled from selected KBs.
- A **snapshot** is a frozen KB copied from another KB at a point in time.
- A **diff** is a KB computed from comparing two KBs.

Every one of these is a KB. Every one is queryable. Every one is surfaceable. Every one is selectable. Every one can contain other KBs. Every one carries its own constraints. Every one has provenance.

This is not a design choice that could have gone another way. It is the consequence of taking the KB abstraction seriously. If a KB is the right structure for storing facts with provenance and constraints, then it is the right structure for everything that has facts with provenance and constraints. And in a system where everything is tracked exactly, everything has facts, everything has provenance, and everything has constraints.

KBs all the way down. Not as a philosophical statement. As an engineering architecture where one data structure, one query language, one constraint system, and one surfacing mechanism handles every object in the system uniformly.

---

## 11. What This Replaces

| Current LLM Pattern | VDR-Prolog Replacement |
|---------------------|----------------------|
| Flat conversation history | Conversation KB with structured turns, topics, bindings |
| System prompt instructions | Constraint facts in account and project KBs |
| "Memory" features (summaries) | Working data sets with exact bindings and history |
| Chat titles for finding conversations | KB queries by content, tags, topics, pending items |
| Context window management | Explicit KB selection and occlusion |
| "Remember this" instructions | Reminder facts with trigger conditions and ack requirements |
| Tool use (external API calls) | Operational primitives with credential gating and async execution |
| Generated responses about data | Direct KB surfacing of exact data with LLM framing |
| Approximate arithmetic | Exact VDR fractions via pure primitives |
| Hoping the model recalls context | Scoped KB resolution with inheritance and shadowing |
| Debugging by re-reading conversation | Provenance queries over derivation facts |
| Manual project organization | KB trees with tags, groups, views, and meta-queries |

Every row in this table replaces something unreliable with something exact, something ephemeral with something persistent, something opaque with something queryable.

That is the complete architecture. One structure. One query language. One constraint system. Everything is a KB. Everything is surfaceable. Everything is selectable. Everything is exact.
