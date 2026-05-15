## Knowledge Base Layering: Scoped Search as Default Behavior

### The Core Insight

Current LLMs search their entire context for every query. If you have been discussing story A for 50 turns and story B for 30 turns, and you ask "how old is Bob," the model searches all 80 turns of context and tries to figure out which Bob you mean from positional cues. This is expensive, error-prone, and fundamentally wrong. You are talking about story B. Story A's facts should not be in the search space at all.

The fix is not better disambiguation heuristics. The fix is not searching story A in the first place.

### Knowledge Base as Search Scope

Every topic has a knowledge base. The active topic determines which knowledge bases are in scope. When you query a fact, only the in-scope knowledge bases are searched. Out-of-scope knowledge bases are not searched, not considered, not even visible.

```
Rule: in_scope(KB) :-
    active_topic(Topic),
    kb_belongs_to(KB, Topic).

Rule: in_scope(KB) :-
    active_topic(Topic),
    topic(Topic, _, _, parent(Parent)),
    Parent \= "none",
    kb_belongs_to(KB, Parent).

Rule: in_scope(KB) :-
    kb_belongs_to(KB, "global").
    % Global KB is always in scope (system constraints, axioms)
```

The search order is: current topic's KB first, parent topic's KB second, up to root, global KB last. This is lexical scoping applied to knowledge. The first match wins. Parent facts are visible but shadowed by child facts.

### The Search Function

```
Rule: query(Predicate, Args, Result) :-
    in_scope(KB),
    fact_in(KB, Predicate, Args, Result),
    !.  % Cut: first match in scope order wins

Rule: query(Predicate, Args, not_found) :-
    not((in_scope(KB), fact_in(KB, Predicate, Args, _))).
```

When you ask "how old is Bob" while topic "story_b" is active:

1. Search `kb_story_b` — finds `binding("bob_age", 59)` → returns 59
2. Never searches `kb_story_a` — that KB is not in scope

When you ask "what language are we using" while topic "vdr_linalg" is active:

1. Search `kb_vdr_linalg` — no binding for "language"
2. Search `kb_vdr_core` (parent) — no binding
3. Search `kb_project_vdr` (grandparent) — finds `binding("language", "python")` → returns Python
4. Never searches `kb_story_a` or `kb_story_b` — those are in different branches

### The Knowledge Base Tree

```
kb_global (always in scope)
├── axioms: probability sums to 1, attention non-negative
├── system: operational rules, Python 3.8 compat
│
├── kb_project_vdr
│   ├── language = python
│   ├── python_version = 3.8
│   ├── naming = remainder not residual
│   │
│   ├── kb_vdr_core
│   │   ├── modules = 24, tests = 705, errors = 0
│   │   ├── kb_vdr_linalg
│   │   │   └── det_method = cofactor, needs_gaussian = true
│   │   ├── kb_vdr_llm
│   │   │   ├── has_softmax = true, has_autodiff = true
│   │   │   └── kb_vdr_training
│   │   │       └── lr = 1/10, optimizer = sgd
│   │   └── kb_vdr_gyms
│   │       └── total_gyms = 23, gym16_passed = 19
│   │
│   └── kb_math_series
│       └── q335_exponent = 335, constants = 22
│
├── kb_story_a ("Bob's Adventure")
│   ├── setting = Pacific Northwest, year = 2024
│   ├── kb_characters_a
│   │   ├── bob_age = 32, bob_town = Portland
│   │   └── alice_age = 28, alice_role = detective
│   └── kb_plot_a
│       └── chapter = 3, conflict = missing artifact
│
└── kb_story_b ("Bob in London")
    ├── setting = London, year = 2026
    ├── kb_characters_b
    │   ├── bob_age = 59, bob_town = London
    │   └── margaret_age = 45, margaret_role = spy
    └── kb_plot_b
        └── chapter = 1, conflict = double agent
```

When story_b is active, the entire story_a subtree is invisible. Not deprioritized. Not ranked lower. Invisible. The search function never enters it.

### Automatic Disambiguation

The term "bank" means a financial institution in a business context and a river edge in a geography context. In a flat context window, the LLM has to guess which one you mean from surrounding tokens. With KB layering, there is no ambiguity:

```
kb_finance
├── binding("bank", atom("financial_institution"))
├── binding("bank_operations", list([atom("deposit"), atom("withdraw"), atom("transfer")]))

kb_geography
├── binding("bank", atom("river_edge"))
├── binding("bank_features", list([atom("erosion"), atom("sediment"), atom("flood_plain")]))
```

If the active topic is under `kb_finance`, "bank" resolves to "financial_institution." If the active topic is under `kb_geography`, "bank" resolves to "river_edge." No disambiguation logic. No heuristics. No "I think you might mean..." The scope determines the meaning. The meaning is a fact in the scoped KB.

This extends to every shared term across domains. "Field" means something different in agriculture, physics, computer science, and baseball. "Class" means something different in object-oriented programming, sociology, and biology. "Tree" means something different in botany, graph theory, and genealogy. Each domain's KB has its own binding for the term. The active scope selects the correct one automatically.

### Explicit Cross-Scope Queries

Sometimes you genuinely need to reach into another scope. The system supports this through qualified queries:

```
Rule: query_in(KB, Predicate, Args, Result) :-
    fact_in(KB, Predicate, Args, Result).
    % Direct query into a specific KB, bypassing scope rules

Rule: query_across(Predicate, Args, Results) :-
    findall(KB-Result, 
        (kb_exists(KB), fact_in(KB, Predicate, Args, Result)), 
        Results).
    % Search ALL KBs, return tagged results
```

"How old is Bob in all my stories?" is a cross-scope query:

```
?- query_across("bob_age", [number(Age)], Results).
% Results = [
%   kb_characters_a - 32,
%   kb_characters_b - 59
% ]
```

The results are tagged with their source KB. No confusion. Both Bobs are found, both are identified by their scope, and the caller knows exactly which is which.

"What does the story_a Bob look like?" while in story_b is a qualified query:

```
?- query_in(kb_characters_a, "bob_age", [number(Age)], Age).
% Age = 32
```

You reached into a specific out-of-scope KB deliberately. The system did not accidentally mix the two Bobs. You explicitly asked for story_a's data.

### KB Activation and Deactivation

When topics change, KBs activate and deactivate:

```
Rule: switch_topic(NewTopic) :-
    active_topic(OldTopic),
    deactivate_kb_tree(OldTopic),
    activate_kb_tree(NewTopic),
    retract(active_topic(OldTopic)),
    assert(active_topic(NewTopic)),
    log(topic_switch(OldTopic, NewTopic)).

Rule: activate_kb_tree(Topic) :-
    kb_belongs_to(KB, Topic),
    assert(kb_active(KB)),
    topic(Topic, _, _, parent(Parent)),
    Parent \= "none",
    activate_kb_tree(Parent).

Rule: deactivate_kb_tree(Topic) :-
    kb_belongs_to(KB, Topic),
    retract(kb_active(KB)),
    forall(topic(Child, _, _, parent(Topic)), deactivate_kb_tree(Child)).
```

Switching from story_a to story_b: deactivate kb_story_a and all its children (kb_characters_a, kb_plot_a), activate kb_story_b and all its children (kb_characters_b, kb_plot_b). The parent chain up to global stays active because both stories share the global KB.

The deactivation does not delete anything. The facts are still there. They are just not in the search scope. Switch back and they reappear instantly, exactly as they were.

### Multi-Topic Queries

Sometimes you are working across multiple topics simultaneously. The system supports explicit multi-scope activation:

```
Rule: also_activate(Topic) :-
    activate_kb_tree(Topic),
    assert(secondary_scope(Topic)).

Rule: in_scope(KB) :-
    secondary_scope(Topic),
    kb_belongs_to(KB, Topic).
```

"I want to compare story_a and story_b side by side" activates both KB trees. Queries now search both, with results tagged by source. Ambiguous terms return multiple results instead of being silently disambiguated. The user sees both and chooses.

```
?- resolve("bob_age", Value).
% Ambiguous: found in kb_characters_a (32) and kb_characters_b (59).
% Active scopes: story_a (secondary), story_b (primary).
% Primary scope value: 59
% Use query_in(kb_characters_a, ...) for the other.
```

### Performance: Skip Entire Buckets

The game Prolog's frame allocator was a performance optimization — don't iterate facts that will be freed anyway. KB layering is the same principle applied to search: don't iterate facts that are out of scope.

In a flat fact store with 10,000 facts across 20 topics, every query scans all 10,000. With KB layering, a query against the active topic's KB scans only the facts in that scope — maybe 500. The other 9,500 are not examined. Not filtered out. Not ranked low. Not searched at all.

This is not just faster. It is semantically correct. The query "how old is Bob" should not even consider facts about Bob in a different story. The performance improvement is a consequence of the semantic improvement, not the goal.

For the VDR-LLM system specifically, this means:

Model architecture facts (layer sizes, activation functions) are in a persistent KB that is always in scope during model work.

Training state facts (parameter values, gradient histories) are in a per-training-run KB that is only in scope when discussing that run.

Inference data facts (input tokens, attention patterns, output distributions) are in a per-batch KB that is in scope during analysis of that batch and invisible otherwise.

A query about "what is the attention weight at position 3" during analysis of batch 42 searches only batch 42's KB. It does not scan the attention weights from batch 41, or the training parameters, or the model architecture, or any story facts. One KB. One search. Exact answer.

### The Layering Principle

The principle is: every piece of knowledge has a home. The home is a KB in a specific place in the topic tree. The search scope at any moment is the path from the current topic up to the root, plus any explicitly activated secondary scopes. Everything else is invisible.

This is how human memory works in conversation. When you are discussing your vacation, you do not mentally search your tax records for the meaning of "return." When you switch to discussing taxes, you do not confuse "return" with "coming home." The context determines the search space. The search space determines the meaning.

VDR-Prolog makes this explicit, exact, and programmable. The scoping rules are Prolog rules. They can be queried, modified, and verified like any other part of the knowledge base. The system knows what it can see, what it cannot see, and why.
