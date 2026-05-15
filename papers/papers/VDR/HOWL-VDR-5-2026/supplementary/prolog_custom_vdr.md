## VDR-Prolog: Custom Knowledge Engine for Exact LLM Systems

### The Inversion

The Zig Prolog was built for a game engine — entities, spatial queries, frame-rate performance. The question is not "how do we bolt VDR onto this" but "what would a Prolog look like if it were designed from scratch for VDR-LLM provenance?"

The game Prolog has Terms that carry spatial types (vec2, rect, circle) because the game needs spatial reasoning. A VDR-LLM Prolog needs Terms that carry exact fractions, weight matrices, gradient histories, attention maps, and token sequences — because the LLM needs arithmetic and derivation reasoning.

### What the VDR-LLM System Actually Needs to Track

There are two distinct provenance domains that share the same constraint infrastructure.

**Weight provenance** tracks every parameter in the model: where it was initialized, what gradients updated it, what learning rate was applied, what its exact value is at every checkpoint, what constraint it satisfies (bounded norm, sum-to-one in softmax denominator, non-negative in ReLU-gated paths). The provenance chain for a single weight goes: initialization seed → initial value → gradient at step 1 → update rule → value at step 1 → gradient at step 2 → ... → current value. Every link in this chain is an exact fraction.

**Data provenance** tracks every input: where the raw data came from, what tokenization was applied, what preprocessing transformed it, what embedding lookup produced the input vector, what attention patterns the model computed for it, what output distribution resulted, what token was sampled. The provenance chain for a single output token goes: raw text → tokenization → token ids → embedding vectors → attention scores → softmax weights → value mixing → feedforward → logits → softmax → probability → sample → output token.

Both chains are stored as facts in the same knowledge base. Both are queryable by the same rules. Both are subject to the same constraints.

---

### TermType for VDR-LLM

The game Prolog has atom, variable, number, list, vector2, rectangle, circle, entity, transform, level_data. Here is what the VDR-LLM Prolog needs:

```
TermType = enum {
    // Core Prolog
    atom,           // Named constants: "relu", "softmax", "layer_2", "weight"
    variable,       // Unification variables: ?X, ?Weight, ?Gradient
    
    // VDR Arithmetic
    fraction,       // Exact VDR fraction: p/q as two arbitrary-precision integers
    fraction_vec,   // Exact vector of fractions (embedding, hidden state, logits)
    fraction_mat,   // Exact matrix of fractions (weight matrix, attention scores)
    
    // Q-Basis Compressed
    qbasis,         // Single integer over shared 2^k denominator
    qbasis_vec,     // Vector of Q-basis integers (shared denominator)
    qbasis_mat,     // Matrix of Q-basis integers (shared denominator)
    
    // Structural References
    parameter,      // Reference to a named model parameter by path
    layer,          // Reference to a layer in the model architecture
    token,          // A token id with its vocabulary mapping
    token_seq,      // A sequence of token ids
    
    // Provenance Types  
    derivation,     // A derivation record: operation + input references + output
    constraint,     // A constraint specification: type + bound + scope
    checkpoint,     // A snapshot reference: step number + parameter state
    
    // Computation Graph
    gradient,       // Exact gradient value with respect to a specific parameter
    loss,           // Loss value with derivation
    step,           // Training step number
    
    // List
    list,           // Heterogeneous list of terms
};
```

This is not a minor extension of the game Prolog's term types. It is a redesign around the specific data shapes that flow through an exact LLM.

---

### Term Structure

The game Prolog stores one of each possible value in every Term struct (vec2, rect, number, etc.) and selects by type tag. For VDR-LLM, the values are larger and more varied, so the Term should use a discriminated union more carefully. But the principle is the same: a Term is a tagged value that Prolog can unify, compare, and bind.

```
Term = struct {
    type: TermType,
    
    // Prolog core
    atom: Text,              // for .atom
    variable: Text,          // for .variable
    
    // VDR values (pointer to heap-allocated exact data)
    fraction_num: BigInt,    // numerator for .fraction
    fraction_den: BigInt,    // denominator for .fraction
    vec_data: []Fraction,    // for .fraction_vec
    mat_data: [][]Fraction,  // for .fraction_mat
    
    // Q-basis (compact)
    qint: BigInt,            // integer over shared denominator for .qbasis
    qvec: []BigInt,          // for .qbasis_vec
    qmat: [][]BigInt,        // for .qbasis_mat
    qexp: i32,              // shared exponent k where denominator = 2^k
    
    // References (indices into model/data tables)
    ref_path: Text,          // "layer.2.weight", "embedding.token.45"
    ref_index: i32,          // numeric index
    ref_step: i32,           // training step number
    
    // Derivation
    operation: Text,         // "matmul", "softmax", "sgd_update", "relu"
    input_refs: []Term,      // references to input terms
    
    // Constraint
    constraint_type: Text,   // "sum_to_one", "non_negative", "norm_bounded"
    constraint_bound: Fraction, // the bound value if applicable
    
    // List
    list: []Term,
};
```

---

### Fact Structure for Weight Provenance

A weight in the model is a fraction. Its provenance is a chain of facts:

```
Fact: parameter_value("layer.1.weight[0][0]", step(0), fraction(1, 4))
  — "at step 0, this weight is exactly 1/4"

Fact: initialized_from("layer.1.weight[0][0]", xavier_rational, seed(42))
  — "this weight was initialized by xavier_rational with seed 42"

Fact: gradient_at("layer.1.weight[0][0]", step(0), fraction(-3, 7))
  — "the gradient of the loss with respect to this weight at step 0 is -3/7"

Fact: updated_by("layer.1.weight[0][0]", step(0), sgd, lr(fraction(1, 10)))
  — "this weight was updated by SGD with learning rate 1/10"

Fact: parameter_value("layer.1.weight[0][0]", step(1), fraction(31, 140))
  — "at step 1, this weight is exactly 31/140 = 1/4 + (1/10)(3/7)"
```

The chain is complete. You can query: "what is the current value?" "what was the value at step 0?" "what gradient caused the change?" "what learning rate was used?" "is the derivation consistent?" — and the answers are exact fractions with logical proofs.

---

### Fact Structure for Data Provenance

An input token's journey through the model:

```
Fact: raw_text(doc(1), "the cat sat")
Fact: tokenized(doc(1), [token(0, "the"), token(1, "cat"), token(2, "sat")])
Fact: token_id(doc(1), pos(0), id(42))
  — "position 0 in document 1 is token id 42"

Fact: embedding(doc(1), pos(0), fraction_vec([3/7, 1/2, ...]))
  — "the embedding for position 0 is this exact vector"
  
Fact: derived_from(embedding(doc(1), pos(0)), lookup, [token_id(doc(1), pos(0)), embed_table])
  — "this embedding came from looking up token 42 in the embedding table"

Fact: attention_score(doc(1), pos(0), pos(1), fraction(5/12))
  — "attention from position 0 to position 1 has score 5/12"

Fact: derived_from(attention_score(doc(1), pos(0), pos(1)), dot_product, 
        [query(doc(1), pos(0)), key(doc(1), pos(1))])

Fact: attention_weight(doc(1), pos(0), pos(1), fraction(43545600, 59565131))
Fact: derived_from(attention_weight(doc(1), pos(0), pos(1)), softmax, 
        [attention_score(doc(1), pos(0), pos(0)), 
         attention_score(doc(1), pos(0), pos(1))])
Fact: satisfies(attention_weight(doc(1), pos(0), _), sum_to_one)

Fact: output_logits(doc(1), pos(2), fraction_vec([...]))
Fact: output_prob(doc(1), pos(2), token(17), fraction(3, 7))
Fact: sampled(doc(1), pos(2), token(17), seed(1234))
```

Every value is an exact fraction. Every derivation step is recorded. Every constraint is declared and verifiable.

---

### Rule Structure

Rules express invariants and relationships that hold across the entire system:

```
Rule: valid_probability(P) :- P >= 0, P =< 1.

Rule: valid_distribution(Doc, Pos) :- 
    findall(P, output_prob(Doc, Pos, _, P), Probs),
    sum(Probs, 1),
    forall(member(P, Probs), valid_probability(P)).

Rule: weight_consistent(Param, Step) :-
    parameter_value(Param, Step, V1),
    PrevStep is Step - 1,
    parameter_value(Param, PrevStep, V0),
    gradient_at(Param, PrevStep, G),
    updated_by(Param, PrevStep, sgd, lr(LR)),
    V1 =:= V0 - LR * G.

Rule: depends_on(X, Y) :- derived_from(X, _, Sources), member(Y, Sources).
Rule: depends_on(X, Y) :- derived_from(X, _, Sources), member(Z, Sources), depends_on(Z, Y).

Rule: affected_by_parameter(Param, Output) :-
    parameter_value(Param, _, _),
    depends_on(Output, Param).

Rule: attention_valid(Doc, Pos) :-
    findall(W, attention_weight(Doc, Pos, _, W), Weights),
    sum(Weights, 1),
    forall(member(W, Weights), W >= 0).
```

These rules are not decorative documentation. They are executable constraints that the system checks after every computation. `weight_consistent` verifies that the recorded value at step N matches the recorded value at step N-1 updated by the recorded gradient with the recorded learning rate. If it doesn't match, the provenance chain has an error — and the error is detectable exactly, because every value is an exact fraction.

---

### The KnowledgeBase Structure

The game Prolog has one KnowledgeBase per entity. The VDR-LLM Prolog has a hierarchical knowledge base:

```
KnowledgeBase = struct {
    // Model-level facts (architecture, hyperparameters)
    model_facts: FactSet,
    model_rules: RuleSet,
    
    // Parameter-level facts (values, gradients, update history)
    // One FactSet per parameter group, indexed by layer path
    parameter_facts: HashMap(Text, FactSet),
    
    // Data-level facts (inputs, intermediate activations, outputs)
    // One FactSet per document/batch, can be pruned after processing
    data_facts: HashMap(i32, FactSet),
    
    // Constraint registry (invariants that must hold)
    constraints: ConstraintSet,
    
    // Step counter
    current_step: i32,
    
    // Checkpoint index (which steps have full snapshots)
    checkpoints: []i32,
};
```

The separation matters for memory management. Model facts and rules are persistent — they describe the architecture and its invariants. Parameter facts grow with training steps but can be pruned to checkpoints (keep every 100th step, discard intermediate). Data facts are transient — they describe a specific forward pass and can be discarded after the output is verified and the gradients are propagated.

This mirrors the game Prolog's frame allocator strategy. The game discards per-frame facts at frame end. The VDR-LLM discards per-batch data facts after the batch is processed. The pruning is explicit and the pruning policy is a declared rule in the knowledge base itself:

```
Rule: retain_data(Doc) :- flagged_for_audit(Doc).
Rule: retain_data(Doc) :- contains_anomaly(Doc).
Rule: prune_data(Doc) :- not(retain_data(Doc)).

Rule: retain_parameter_history(Param, Step) :- Step mod 100 =:= 0.
Rule: retain_parameter_history(Param, Step) :- constraint_violated_at(Param, Step).
```

---

### Constraint System

The game Prolog does not have an explicit constraint system — spatial queries are just fact lookups. The VDR-LLM Prolog needs constraints as first-class objects because the entire point is to guarantee properties of the computation.

```
ConstraintType = enum {
    sum_to_one,        // probability distribution normalization
    non_negative,      // probability, ReLU output
    bounded_norm,      // gradient clipping, weight regularization
    exact_equality,    // cached value matches recomputed value
    monotonic,         // softmax preserves logit ordering
    denominator_bound, // Q-basis precision control
    derivation_valid,  // recorded derivation matches actual computation
};

Constraint = struct {
    type: ConstraintType,
    scope: Text,          // what it applies to: "attention_weights", "output_probs"
    bound: Fraction,      // the bound value if applicable
    verified_at: i32,     // last step where this was checked
    status: enum { verified, violated, unchecked },
};
```

After every forward pass, the system runs constraint verification:

```
verify_all_constraints(kb, step) {
    for constraint in kb.constraints {
        switch (constraint.type) {
            .sum_to_one => verify_sum_to_one(kb, constraint.scope, step),
            .non_negative => verify_non_negative(kb, constraint.scope, step),
            .derivation_valid => verify_derivations(kb, constraint.scope, step),
            ...
        }
        constraint.verified_at = step;
    }
}
```

Because every value is an exact VDR fraction, constraint checking is exact. "Sum to one" means the fractions sum to exactly 1/1, not to 0.99999997. "Non-negative" means the fraction is ≥ 0/1, not ≥ -1e-15. There is no tolerance. There is no epsilon. The constraint either holds or it doesn't.

---

### Unification With Exact Fractions

The game Prolog unifies atoms by string comparison and numbers by float equality. The VDR-LLM Prolog unifies fractions by exact rational comparison.

```
unify(term1, term2, bindings) {
    // Variable binds to anything
    if (term1.type == .variable) {
        bindings.bind(term1.variable, term2);
        return true;
    }
    if (term2.type == .variable) {
        bindings.bind(term2.variable, term1);
        return true;
    }
    
    // Same type: compare by type
    if (term1.type != term2.type) return false;
    
    switch (term1.type) {
        .atom => return term1.atom.equals(term2.atom),
        .fraction => return (term1.fraction_num * term2.fraction_den == 
                            term2.fraction_num * term1.fraction_den),
        .fraction_vec => return vecs_equal_exact(term1.vec_data, term2.vec_data),
        .qbasis => return (term1.qint == term2.qint and term1.qexp == term2.qexp),
        ...
    }
}
```

Fraction equality is checked by cross-multiplication, which is exact integer arithmetic. No float comparison. No epsilon. Two fractions are equal if and only if they represent the same rational number.

This means queries like "find all parameters whose value at step 100 equals their value at step 0" are exact. In a float system, this query is meaningless because float equality after 100 update steps is essentially random. In VDR-Prolog, it is a precise question with a precise answer.

---

### Query Examples

**Weight archaeology:**
```
?- parameter_value("layer.1.weight[0][0]", step(S), fraction(1, 4)).
% "At which steps was this weight exactly 1/4?"
% Answer: S = 0 (and maybe S = 347 if it returned to that value)

?- parameter_value("layer.1.weight[0][0]", step(100), V),
   parameter_value("layer.1.weight[0][0]", step(0), V).
% "Is this weight the same at step 100 as at step 0?"
% Exact answer, not tolerance-based.
```

**Data lineage:**
```
?- output_prob(doc(42), pos(7), token(T), P), P > fraction(1, 2).
% "Which tokens have probability > 1/2 at position 7 of document 42?"

?- depends_on(output_prob(doc(42), pos(7), token(17), _), 
              embedding(doc(42), pos(Pos))).
% "Which input positions influenced the output at position 7?"
% Answer: all positions that attention attended to.

?- affected_by_parameter("layer.1.weight[0][0]", 
                         output_prob(doc(42), pos(7), token(T), P)).
% "Does changing this weight affect the output at this position?"
```

**Constraint verification:**
```
?- attention_valid(doc(42), Pos).
% "At which positions are attention weights valid (non-negative, sum to 1)?"
% Should return all positions. If any fails, the exact violation is reported.

?- weight_consistent("layer.1.weight[0][0]", Step).
% "At which steps is the weight update derivation consistent?"
% Checks that V_new = V_old - lr * gradient exactly.
```

**Anomaly detection:**
```
?- parameter_value(Param, step(S), V), 
   denominator(V, D), D > 2^64.
% "Which parameters have denominators exceeding 2^64?"
% This is the denominator growth monitor — a VDR-specific diagnostic.

?- gradient_at(Param, step(S), G), abs(G) > fraction(100, 1).
% "Which gradients exceed 100 in absolute value?"
% Exact gradient explosion detection.
```

---

### The Memory Model

The game Prolog uses a frame allocator — facts allocated per frame, freed at frame end. The VDR-LLM Prolog needs a tiered memory model:

**Tier 1: Persistent.** Model architecture, rules, constraints, hyperparameters. Never freed. Small.

**Tier 2: Checkpoint.** Parameter values at checkpoint steps. Retained long-term. Grows linearly with checkpoint count. Each checkpoint is a set of exact fractions — the full model state, reproducible to the last digit.

**Tier 3: Training step.** Gradients, update details, intermediate activations for the current step. Retained until the step is committed and the checkpoint policy decides whether to keep it. Most steps are pruned — only the parameter delta matters.

**Tier 4: Batch transient.** Per-batch data provenance — tokenization, embeddings, attention maps, output distributions for the current batch. Retained only if flagged for audit or anomaly. Most batches are pruned after gradient propagation.

The pruning policy is itself a set of Prolog rules, so it is declarative, inspectable, and modifiable without changing code:

```
Rule: retain_step(Step) :- Step mod checkpoint_interval =:= 0.
Rule: retain_step(Step) :- loss_at(Step, L), L > anomaly_threshold.
Rule: retain_step(Step) :- constraint_violated_at(_, Step).
Rule: retain_batch(Batch) :- contains_token(Batch, unk_token).
Rule: retain_batch(Batch) :- output_contains_anomaly(Batch).
```

---

### How This Differs From the Game Prolog

The game Prolog is optimized for per-frame queries on spatial data — "which entities are within this rectangle?" The unification is simple, the fact sets are small, the rules are few, and everything resets at frame boundaries.

The VDR-LLM Prolog is optimized for provenance chains on exact arithmetic data — "what sequence of exact computations produced this exact value?" The unification includes exact rational comparison, the fact sets grow with training history, the rules encode mathematical invariants, and retention is governed by audit policy.

The structural parallel is exact. Both have Terms, Facts, Rules, FactSets, RuleSets, and KnowledgeBases. Both use the same unification and backtracking machinery. Both separate mutable facts from stable rules. Both have memory management strategies that prune transient data.

The differences are in what the Terms carry (spatial geometry vs exact fractions), what the Rules express (game logic vs mathematical invariants), and what the queries ask (collision detection vs derivation provenance).

---

### What This Enables That Nothing Else Does

**Auditable exact ML.** Every output has a proof tree. Every weight has a history. Every constraint is verified exactly. No other ML system offers this.

**Exact reproducibility with logical explanation.** Not just "the same output" but "the same output for these exact reasons, derived through these exact steps, subject to these exact constraints, all verified."

**Targeted recomputation.** When a parameter is found to be wrong (corrupted checkpoint, buggy gradient), Prolog traces every downstream value that depends on it. Only those values are recomputed. The rest of the model state is known to be unaffected, because the dependency graph is complete.

**Constraint-driven architecture search.** Express desired properties as Prolog constraints (attention weights must be non-negative, no gradient exceeds bound B, denominator complexity stays within budget C). The system can search for architectures or hyperparameters that satisfy all constraints — Prolog's backtracking search explores alternatives when constraints fail.

**Self-documenting models.** The knowledge base is the documentation. "What is this model?" Query the architecture facts. "How was it trained?" Query the parameter history. "What does it do on this input?" Query the data provenance. "Is it correct?" Query the constraint verification. The answers are exact, complete, and machine-readable.

---

### The Implementation Path

**Step 1:** Port the core Prolog structs (Term, Fact, Rule, FactSet, RuleSet, KnowledgeBase) from the game engine Zig code, replacing the spatial term types with VDR fraction term types. Keep the unification and backtracking machinery. This produces a minimal Prolog that can store and query exact fractions.

**Step 2:** Add the constraint verification layer. Define constraint types, implement exact checking against VDR values, integrate checking into the query/assert cycle so constraints are verified as facts are added.

**Step 3:** Instrument the VDR transformer forward pass to assert provenance facts into the knowledge base. Each operation (embedding lookup, matmul, softmax, residual add) asserts its inputs, outputs, and operation type. The result is a complete provenance graph for every forward pass.

**Step 4:** Instrument the backward pass and optimizer similarly. Gradient facts, update facts, parameter value facts at each step. The result is a complete training history in the knowledge base.

**Step 5:** Implement the tiered memory model with Prolog-rule-driven retention policies. Test on actual training runs to verify that pruning works and that retained provenance supports the required queries.

**Step 6:** Build the query interface for the use cases above — weight archaeology, data lineage, constraint verification, anomaly detection. This is where the system becomes useful rather than just correct.

---

### The Bottom Line

The game Prolog shows the pattern works: embed a logic engine into a computational system, use it to reason about the system's state, let the logic layer carry structured types that the computation needs. The VDR-LLM Prolog takes the same pattern and applies it to exact arithmetic and ML provenance.

The result would be a system where data is not just stored — it is grounded. Every value has a reason. Every reason has a derivation. Every derivation is exact. Every constraint is verified. And the whole thing is queryable in a logic language that can explain any result by producing its proof.

That is what data with full provenance looks like.
