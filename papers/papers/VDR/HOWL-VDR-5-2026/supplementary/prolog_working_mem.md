## Working Data Sets: Scoped Variable Storage in VDR-Prolog

### The Problem

Current LLMs treat everything as context tokens. When you say "Bob is 32 years old," that fact exists only as tokens in the conversation window. It has no structure, no scope, no persistence beyond the context limit, and no separation from other facts about other Bobs in other stories. If you switch to a different story and come back, the LLM has to re-read the entire conversation to reconstruct who Bob is, and it might confuse the two Bobs because both are just token patterns in the same flat context.

This is not a memory problem. It is a data model problem. The LLM has no place to put structured data that is scoped to a specific topic, persistent within that scope, and isolated from data in other scopes.

### The Solution: Working Data Sets as Scoped Fact Stores

A working data set is a named, scoped collection of variable bindings attached to a topic. It is a nested dictionary where the keys are names, the values are exact VDR fractions or atoms or any Term type, and the scope determines which bindings are visible at any point in the conversation.

```
WorkingDataSet = struct {
    name: Text,              // "story_alice_wonderland", "project_vdr"
    topic: Text,             // which topic this belongs to
    parent: Text,            // parent dataset for inheritance (or "none")
    bindings: HashMap(Text, Term),  // name → value
    created_at: i32,         // turn number
    last_modified: i32,      // turn number
    frozen: bool,            // if true, read-only (snapshot)
};
```

### How Scoping Works

Working data sets form a tree that mirrors the topic tree. When you look up a variable, the system searches the current dataset first, then walks up to the parent, exactly like lexical scoping in a programming language.

```
Fact: dataset("story_bob_adventure", topic("bob_adventure"), parent("root")).
Fact: dataset("story_bob_sequel", topic("bob_sequel"), parent("root")).
Fact: dataset("characters_bob_adventure", topic("bob_adventure"), parent("story_bob_adventure")).

Fact: binding("characters_bob_adventure", "bob_age", number(32)).
Fact: binding("characters_bob_adventure", "bob_name", atom("Bob Harrison")).
Fact: binding("characters_bob_adventure", "bob_hometown", atom("Portland")).

Fact: binding("story_bob_adventure", "setting", atom("Pacific Northwest")).
Fact: binding("story_bob_adventure", "year", number(2024)).
Fact: binding("story_bob_adventure", "genre", atom("mystery")).
```

Now switch to the sequel:

```
Fact: binding("story_bob_sequel", "setting", atom("London")).
Fact: binding("story_bob_sequel", "year", number(2026)).
Fact: binding("story_bob_sequel", "genre", atom("thriller")).

Fact: dataset("characters_bob_sequel", topic("bob_sequel"), parent("story_bob_sequel")).
Fact: binding("characters_bob_sequel", "bob_age", number(34)).
Fact: binding("characters_bob_sequel", "bob_name", atom("Bob Harrison")).
Fact: binding("characters_bob_sequel", "bob_hometown", atom("London")).
Fact: binding("characters_bob_sequel", "sarah_age", number(28)).
Fact: binding("characters_bob_sequel", "sarah_role", atom("detective")).
```

Two different stories. Two different Bobs. Same name, different ages, different contexts. Completely isolated. Switch between them instantly by changing the active topic, and every variable resolves to the correct value in the correct scope.

### Resolution Rules

```
Rule: resolve(Var, Value) :-
    active_topic(Topic),
    active_dataset(Topic, DS),
    resolve_in(Var, DS, Value).

Rule: resolve_in(Var, DS, Value) :-
    binding(DS, Var, Value).

Rule: resolve_in(Var, DS, Value) :-
    not(binding(DS, Var, _)),
    dataset(DS, _, parent(Parent)),
    Parent \= "none",
    resolve_in(Var, Parent, Value).

Rule: resolve_in(Var, DS, unbound) :-
    not(binding(DS, Var, _)),
    dataset(DS, _, parent("none")).
```

When you ask "how old is Bob?" the system resolves `bob_age` in the active dataset. If the active topic is "bob_adventure," the answer is 32. If the active topic is "bob_sequel," the answer is 34. No ambiguity. No confusion. No re-reading context tokens.

### Nested Structure

Working data sets nest naturally because topics nest. A project topic can have sub-topics, each with their own dataset that inherits from the parent.

```
dataset("project_vdr")
├── binding("language", atom("python"))
├── binding("python_version", atom("3.8"))
├── binding("naming_remainder", atom("remainder"))
├── dataset("vdr_core")
│   ├── binding("modules", number(24))
│   ├── binding("total_tests", number(705))
│   ├── binding("computation_errors", number(0))
│   └── dataset("vdr_linalg")
│       ├── binding("det_method", atom("cofactor"))
│       ├── binding("max_practical_n", number(6))
│       └── binding("needs_gaussian", atom("true"))
├── dataset("vdr_llm")
│   ├── binding("softmax_depth", number(12))
│   ├── binding("has_autodiff", atom("true"))
│   ├── binding("has_transformer", atom("true"))
│   └── dataset("vdr_llm_training")
│       ├── binding("optimizer", atom("sgd"))
│       ├── binding("lr", fraction(1, 10))
│       └── binding("batch_size", number(2))
└── dataset("math_series")
    ├── binding("q335_exponent", number(335))
    ├── binding("constants_count", number(22))
    └── binding("total_digits", number(2238))
```

When working in the `vdr_linalg` subtopic and you ask "what language are we using?" the resolution walks up: `vdr_linalg` → `vdr_core` → `project_vdr` → finds `binding("language", atom("python"))`. The answer is Python. You never declared it in the linalg context because it was inherited.

When you set `binding("max_practical_n", number(50))` in `vdr_linalg` after implementing Gaussian elimination, it shadows the parent's value of 6. The parent still says 6. The linalg context says 50. Both are correct in their scope.

### Operations on Working Data Sets

#### Set a value

```
Rule: set_binding(Var, Value) :-
    active_topic(Topic),
    active_dataset(Topic, DS),
    retract(binding(DS, Var, _)),  % remove old if exists
    assert(binding(DS, Var, Value)),
    assert(binding_history(DS, Var, Value, current_turn)).
```

Every set is logged with its turn number. You can query the history:

```
?- binding_history("characters_bob_adventure", "bob_age", Value, Turn).
% Value = 32, Turn = 5 (when you first said "Bob is 32")
```

#### Get a value

```
Rule: get_binding(Var, Value) :-
    resolve(Var, Value),
    Value \= unbound.

Rule: get_binding(Var, unbound) :-
    resolve(Var, unbound),
    log(unbound_access(Var)).
```

Accessing an unbound variable is logged. The system knows what it doesn't know.

#### List all bindings in scope

```
Rule: visible_bindings(Bindings) :-
    active_dataset(_, DS),
    collect_all_bindings(DS, Bindings).

Rule: collect_all_bindings(DS, Bindings) :-
    findall(Var-Value, binding(DS, Var, Value), Local),
    dataset(DS, _, parent(Parent)),
    (Parent = "none" -> 
        Bindings = Local ;
        collect_all_bindings(Parent, ParentBindings),
        merge_bindings(Local, ParentBindings, Bindings)).

Rule: merge_bindings(Local, Parent, Merged) :-
    % Local shadows Parent for same keys
    findall(K-V, (member(K-V, Local)), LocalPairs),
    findall(K-V, (member(K-V, Parent), not(member(K-_, Local))), InheritedPairs),
    append(LocalPairs, InheritedPairs, Merged).
```

At any point: "show me everything I know in the current context" is a single query that returns every visible binding, with inherited values and local overrides clearly distinguished.

#### Snapshot and restore

```
Rule: snapshot(DS, SnapshotName) :-
    collect_all_bindings(DS, Bindings),
    assert(snapshot_data(SnapshotName, DS, Bindings, current_turn)),
    assert(dataset(SnapshotName, topic(snapshot), parent("none"))),
    forall(member(K-V, Bindings), assert(binding(SnapshotName, K, V))),
    mark_frozen(SnapshotName).

Rule: restore(SnapshotName, TargetDS) :-
    snapshot_data(SnapshotName, _, Bindings, _),
    forall(member(K-V, Bindings), 
        (retract(binding(TargetDS, K, _)) ; true),
        assert(binding(TargetDS, K, V))).
```

Before making a big change to the story, snapshot the character data. If the change doesn't work, restore from the snapshot. Every value is exact. Nothing is lost or approximated.

#### Diff between datasets

```
Rule: diff(DS1, DS2, Added, Removed, Changed) :-
    findall(K-V, (binding(DS2, K, V), not(binding(DS1, K, _))), Added),
    findall(K-V, (binding(DS1, K, V), not(binding(DS2, K, _))), Removed),
    findall(K-V1-V2, (binding(DS1, K, V1), binding(DS2, K, V2), V1 \= V2), Changed).
```

"What changed between the adventure and the sequel?" produces a structured diff: Bob's age went from 32 to 34, hometown went from Portland to London, Sarah was added. Exact values, not fuzzy "the model thinks maybe something changed."

### Cross-Dataset Queries

Sometimes you need to query across scopes. The constraint system enables this:

```
Rule: all_bobs(Results) :-
    findall(DS-Age-Town, 
        (binding(DS, "bob_age", number(Age)), 
         binding(DS, "bob_hometown", atom(Town))),
        Results).

% Results = [
%   "characters_bob_adventure" - 32 - "Portland",
%   "characters_bob_sequel" - 34 - "London"
% ]
```

"Tell me about every Bob across all my stories" returns structured results from every dataset that has Bob bindings. Each result is tagged with its source dataset. No confusion about which Bob is which.

### Type Discipline

Working data sets carry exact VDR types, not just strings. This enables type-checked queries and constraint enforcement:

```
Rule: type_of(DS, Var, Type) :-
    binding(DS, Var, Term),
    Term = number(_) -> Type = number ;
    Term = fraction(_, _) -> Type = fraction ;
    Term = atom(_) -> Type = atom ;
    Term = fraction_vec(_) -> Type = vector ;
    Term = fraction_mat(_) -> Type = matrix ;
    Type = unknown.

Rule: type_constraint(DS, Var, ExpectedType) :-
    assert(constraint(type_check(DS, Var), scope("dataset"), active,
        condition(type_of(DS, Var, ExpectedType)),
        on_violation("warn"),
        source("schema"))).
```

You can declare: "bob_age is always a number. bob_name is always an atom. If anything tries to set bob_age to an atom, warn me." Schema enforcement on the working data set, not as an afterthought but as a constraint in the constraint system.

### VDR-Specific Bindings

For the LLM architecture work, the working data set carries VDR-specific values:

```
Fact: binding("vdr_llm_training", "layer1_weight_0_0", fraction(31, 140)).
Fact: binding("vdr_llm_training", "layer1_weight_0_0_step", number(1)).
Fact: binding("vdr_llm_training", "current_loss", fraction(17, 2)).
Fact: binding("vdr_llm_training", "attention_weights_row0", 
        fraction_vec([43545600/59565131, 16019531/59565131])).
```

These are not model parameters stored for inference. These are working values stored for conversation — so when we are discussing training results, the system has the exact values in scope, not approximations reconstructed from context tokens. "What was the loss at step 1?" is answered from the binding, not from scrolling back through conversation history.

### The Integration With Topics and Constraints

The three systems form a closed loop:

**Topics** define scope. "We are working on the VDR LLM training subtopic."

**Working data sets** provide values in that scope. "The current learning rate is 1/10, the loss at step 1 is 17/2, the first weight is 31/140."

**Constraints** enforce invariants on those values. "The learning rate must be positive. The loss must decrease over the training run. All attention weights must sum to 1."

When the topic changes, the working data set changes, and the active constraints change. When a value is set, the relevant constraints are checked. When a constraint is violated, the exact value and exact derivation are available for diagnosis.

When the topic is parked, the working data set is preserved exactly. When the topic is resumed, every value is exactly as it was. No reconstruction from context. No degradation from re-reading. No confusion with other scopes.

### What This Means for LLM Conversations

The LLM is no longer stateless between turns. It has structured, scoped, typed, exact working memory that persists across topic switches, survives parking and resumption, supports inheritance and shadowing, carries full modification history, and is subject to declared constraint verification.

"Bob is 32" is not a token pattern to be matched. It is `binding("characters_bob_adventure", "bob_age", number(32))`, stored in a specific scope, retrievable by exact lookup, overridable by a child scope, diffable against other scopes, and persistent until explicitly changed or pruned.

That is what working data looks like as a first-class feature rather than an emergent property of context window pattern matching.
