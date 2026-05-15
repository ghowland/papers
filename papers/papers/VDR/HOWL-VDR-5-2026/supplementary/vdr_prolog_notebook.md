# VDR × Prolog: Exact Arithmetic Meets Logical Provenance
## A Design Notebook for Constraint-Grounded Exact Data Systems

---

## 1. The Problem With Current Data Systems

Every modern data system has the same structural deficiency: values exist without provenance. A number sits in a column. Where did it come from? What computed it? What were the inputs? What constraints must it satisfy? What happens if an upstream value changes?

The answers to these questions live outside the data — in documentation, in code comments, in the memories of engineers. The data itself is inert. It has values but no reasons.

This creates two cascading failures. First, trust is impossible to verify. You cannot look at a value and determine whether it is correct, because correctness is a relationship between a value and its derivation, and the derivation is not stored. Second, error propagation is invisible. When an upstream value changes or is found to be wrong, there is no systematic way to identify everything downstream that depends on it.

Float arithmetic makes this worse. Values are silently rounded at every step. The number you see is not the number that was computed. The number that was computed is not the number that should have been computed. The gap between these three things is unmeasured, unmeasurable, and growing with every operation.

VDR solves the arithmetic problem. Every value is exact. Every operation preserves exactness. Every intermediate result is a specific inspectable fraction. But VDR alone does not solve the provenance problem. A VDR fraction knows what it is. It does not know why it is, or what it depends on, or what constraints it must satisfy.

Prolog solves the provenance problem. Every fact has a derivation. Every derivation is a chain of rules applied to other facts. Every query can explain its answer by producing the proof tree. But Prolog alone does not solve the arithmetic problem. Prolog's native arithmetic is whatever the host language provides — typically floats, with all their silent truncation.

The two systems are complementary in a way that is almost too clean to be accidental.

---

## 2. What Each System Brings

### 2.1 VDR Provides

Exact values. Every number is a fraction p/q with arbitrary-precision integers. No rounding. No drift. No silent truncation.

Exact operations. Addition, multiplication, matrix inversion, discrete calculus, softmax, autodiff — all producing exact fractions.

Structural identity. The remainder slot carries exact information about how a value sits in its denominator frame. Two values with the same scalar projection can be structurally distinct.

Reproducibility. The same computation on any machine produces bit-identical results. Checkpoints restore exactly. There is no platform-dependent rounding.

Transcendental reach. Via functional remainders (arbitrary-precision rational series) and Q335 projection (100-digit constants as integers over 2^335).

A working ML stack. Softmax, autodiff, linear layers, attention, transformers, optimizers, sampling — 24 modules, 705 tests, zero computation errors.

### 2.2 Prolog Provides

Logical provenance. Every derived fact can produce the proof tree that justifies it. The chain of reasoning from axioms to conclusion is inspectable.

Constraint propagation. CLP(Q) — Constraint Logic Programming over rationals — provides exact rational constraint solving natively. Variables can be constrained by linear inequalities, equalities, and arithmetic relationships, and the solver propagates these constraints exactly.

Backtracking search. When a derivation fails, Prolog systematically explores alternatives. This is built-in exhaustive search with pruning.

Rule-based knowledge. Domain knowledge is expressed as logical rules, not imperative code. The rules are declarative — they say what is true, not how to compute it.

Unification. Pattern matching on structured terms. A query unifies with a rule head, binding variables, and the rule body becomes the new goal. This is the mechanism that connects facts to their derivations.

Negation as failure. What is not provable is assumed false. This gives a closed-world assumption that is appropriate for many data systems.

### 2.3 What Neither Has Alone

VDR has exact values but no logical structure connecting them. It does not know that a particular fraction is "the attention weight from token 3 to token 7, derived from the dot product of query vector Q3 and key vector K7, normalized by softmax over the full key set, subject to the constraint that all weights in this row sum to 1."

Prolog has logical structure and constraint reasoning but no exact nonlinear arithmetic. It cannot compute a softmax, invert a Hilbert matrix, or differentiate a computation graph. CLP(Q) handles linear rational constraints. It does not handle the nonlinear operations that VDR provides.

Together they would have: exact values with full derivation provenance, connected by logical rules, subject to declared constraints, computed by exact arithmetic, with every step inspectable and every result explainable.

---

## 3. Architecture: How They Join

### 3.1 The Interface Layer

The join point is the rational number. VDR produces exact fractions. Prolog's CLP(Q) reasons over exact rationals. The shared data type is the rational p/q. No conversion is needed. No precision is lost at the boundary.

A VDR computation produces a result: the fraction 43545600/59565131. This fraction is asserted into Prolog as a fact with its full provenance:

```prolog
attention_weight(position(0), position(0), 43545600/59565131) :-
    score(position(0), position(0), Score),
    softmax_row(0, Weights),
    nth(0, Weights, 43545600/59565131).
```

The value is exact. The derivation is recorded. The constraint (all weights in row 0 sum to 1) is checkable. If the score changes, Prolog can identify every downstream value that depends on it.

### 3.2 Three Modes of Operation

**Mode 1: VDR computes, Prolog records.** VDR runs a forward pass. Each intermediate result is asserted into Prolog with its derivation chain. Prolog becomes an exact audit log with queryable provenance. You can ask "what depends on embedding vector 3?" and get every downstream value that was computed from it.

**Mode 2: Prolog constrains, VDR solves.** Prolog declares constraints on a system. VDR computes values that satisfy those constraints. If the constraints are linear, CLP(Q) solves them directly. If nonlinear (softmax, matrix inverse), Prolog delegates to VDR and records the result with its constraint relationship.

**Mode 3: Joint reasoning.** Prolog reasons about the structure of a computation (which variables depend on which, what constraints apply, what alternatives exist). VDR executes the arithmetic. The two systems interleave: Prolog selects the next computation to perform based on logical rules, VDR performs it exactly, Prolog records the result and reasons about what to do next.

### 3.3 The Provenance Graph

Every value in the system has a provenance node:

```prolog
value(id(V42), fraction(43545600, 59565131)).
derived_from(id(V42), softmax, [id(V38), id(V39), id(V40)]).
constraint(id(V42), sum_to_one, row(0)).
computed_by(id(V42), vdr_softmax, depth(12)).
timestamp(id(V42), step(17)).
```

This node records: the exact value, how it was derived, what constraint it satisfies, what VDR operation computed it, and when. The provenance graph is itself a Prolog database — queryable, inspectable, and complete.

---

## 4. Concrete Use Cases

### 4.1 Auditable ML Inference

A VDR transformer processes an input. Every intermediate value — every embedding lookup, every attention score, every softmax weight, every feedforward activation, every logit — is asserted into Prolog with its derivation. The final output token probability is an exact fraction with a complete proof tree connecting it back to the input tokens and model parameters.

A regulator asks: "Why did the model assign probability 3/7 to token X?" The system produces the exact derivation: these attention weights (exact fractions, summing to exactly 1) weighted these value vectors (exact fractions) to produce this representation, which was transformed by these feedforward weights (exact fractions) to produce these logits, which were softmax-normalized to produce 3/7.

No "the model is a black box." Every step is an exact fraction with a logical derivation.

### 4.2 Constraint-Driven Training

Instead of just minimizing a loss function, training is subject to declared logical constraints:

```prolog
constraint(all_attention_rows_sum_to_one).
constraint(all_probabilities_nonnegative).
constraint(gradient_norm_bounded_by(10)).
constraint(parameter_denominator_bounded_by(2^64)).
```

Prolog verifies these constraints after each training step. If a constraint is violated, the system can: reject the step, trigger re-projection onto the constraint surface, or flag the violation for human review. The constraint checking is exact — "all attention rows sum to 1" is checked by exact fraction addition, not by tolerance comparison.

### 4.3 Data Pipeline Provenance

A data pipeline transforms raw observations into features. Each transformation is a VDR operation with exact arithmetic. Each result is a Prolog fact with its derivation. When a downstream analysis produces an unexpected result, the analyst queries the provenance graph:

```prolog
?- depends_on(result(R), raw_observation(O)).
```

Prolog traces the dependency chain. Every intermediate transformation is an exact fraction. The analyst can verify each step. If a raw observation is corrected, Prolog identifies every derived value that needs recomputation.

### 4.4 Knowledge-Grounded Computation

Domain knowledge is expressed as Prolog rules:

```prolog
valid_probability(P) :- P >= 0, P =< 1.
valid_distribution(Dist) :- sum_list(Dist, 1), maplist(valid_probability, Dist).
conserved_quantity(energy, System, E) :- 
    kinetic(System, KE), potential(System, PE), E is KE + PE.
```

VDR computations are checked against these rules. If a softmax output violates `valid_distribution`, the system detects it immediately — not through a float tolerance check but through exact fraction verification. If an energy computation violates conservation, the exact point of violation is identified.

### 4.5 Exact Scientific Computation With Logical Bookkeeping

A physics simulation computes trajectories using VDR's exact discrete calculus. Each time step is an exact fraction. Prolog records the derivation of each state from the previous state, the differential equation, and the step size. Conservation laws are expressed as constraints and verified exactly at each step.

When the simulation produces an unexpected result, the physicist queries:

```prolog
?- first_violation(conservation(energy), Step).
```

If the answer is "no violation at any step," the unexpected result is physically meaningful, not a numerical artifact. If there is a violation, the exact step and exact magnitude are reported.

---

## 5. Technical Integration

### 5.1 The Python-Prolog Bridge

SWI-Prolog has a Python interface (pyswip, janus). VDR is Python. The bridge passes exact rationals between the two systems. VDR's `Fraction` objects map directly to Prolog's rational arithmetic (SWI-Prolog supports exact rationals natively via GMP).

```python
# Python side: VDR computes
result = softmax([VDR(1), VDR(2), VDR(3)])
fractions = [x.to_fraction() for x in result]

# Assert into Prolog with provenance
prolog.assertz(
    "softmax_output(step(17), row(0), [%s])" % 
    ", ".join("%d/%d" % (f.numerator, f.denominator) for f in fractions)
)
prolog.assertz(
    "derived_from(softmax_output(step(17), row(0)), "
    "softmax, logits(step(17), row(0)))"
)
```

```prolog
% Prolog side: query provenance
?- softmax_output(step(17), row(0), Weights),
   sum_list(Weights, Sum),
   Sum =:= 1.
% true — exact verification

?- derived_from(softmax_output(step(17), row(0)), Op, Source).
% Op = softmax, Source = logits(step(17), row(0))
```

### 5.2 CLP(Q) for Linear Constraints

SWI-Prolog's CLP(Q) library solves linear constraints over exact rationals. This overlaps with VDR's linear algebra but adds the constraint propagation framework.

```prolog
:- use_module(library(clpq)).

% attention weights must sum to 1
attention_constraint(Weights) :-
    sum_list(Weights, Sum),
    { Sum = 1 },
    maplist(nonneg, Weights).

nonneg(W) :- { W >= 0 }.

% given two weights and the sum constraint, derive the third
?- attention_constraint([1/4, 1/3, W3]).
% W3 = 5/12
```

CLP(Q) can solve for unknown values given constraints — something VDR cannot do alone. VDR computes forward. CLP(Q) reasons bidirectionally.

### 5.3 VDR as Prolog Arithmetic Engine

For nonlinear operations that CLP(Q) cannot handle, Prolog calls VDR as an external arithmetic engine:

```prolog
% Prolog rule: softmax is computed by VDR
softmax_weights(Logits, Weights) :-
    python_call(vdr_softmax, Logits, Weights),
    valid_distribution(Weights).

% Prolog rule: matrix inverse is computed by VDR
inverse(M, MInv) :-
    python_call(vdr_mat_inv, M, MInv),
    python_call(vdr_mat_mul, M, MInv, Product),
    is_identity(Product).
```

The pattern: Prolog delegates computation to VDR, receives exact results, and verifies logical constraints on those results. VDR does the arithmetic. Prolog does the reasoning.

### 5.4 Provenance-Aware VDR Objects

A VDR object could be extended with an optional provenance tag:

```python
class ProvenanceVDR(VDR):
    def __init__(self, v, d=1, r=None, provenance=None):
        super().__init__(v, d, r)
        self.provenance = provenance  # Prolog term or None
```

Every arithmetic operation would propagate provenance:

```python
def __add__(self, other):
    result = super().__add__(other)
    result.provenance = ("add", self.provenance, other.provenance)
    return result
```

The provenance tree mirrors the computation graph. When the result is asserted into Prolog, its full derivation is already attached.

---

## 6. The Data Model

### 6.1 Facts

```prolog
% A value with its exact fraction and provenance
value(Id, Numerator, Denominator, Provenance).

% Provenance is a term describing the derivation
% provenance(operation, [input_ids], constraints, metadata)
```

### 6.2 Rules

```prolog
% Transitively depends on
depends_on(X, Y) :- derived_from(X, _, Sources), member(Y, Sources).
depends_on(X, Y) :- derived_from(X, _, Sources), member(Z, Sources), depends_on(Z, Y).

% All values affected by changing input I
affected_by(I, V) :- depends_on(V, I).

% Verify constraint satisfaction
satisfies(V, sum_to_one(Group)) :-
    findall(Val, (member(Id, Group), value(Id, N, D, _), Val is N/D), Vals),
    sum_list(Vals, 1).
```

### 6.3 Queries

```prolog
% What is the exact value of attention weight (3,7)?
?- attention_weight(position(3), position(7), W).

% What computed it?
?- derived_from(attention_weight(position(3), position(7), _), Op, Sources).

% What would change if embedding vector 5 changed?
?- affected_by(embedding(5), V).

% Are all probability distributions valid?
?- forall(
    distribution(Name, Dist),
    valid_distribution(Dist)
   ).
```

---

## 7. What This System Would Look Like

### 7.1 An Exact Auditable LLM Inference

Input: "The cat sat on the"

```
Step 1: Tokenize → [the, cat, sat, on, the]
  Prolog: token(0, "the"), token(1, "cat"), ...
  
Step 2: Embed → 5 exact rational vectors
  Prolog: embedding(0, [3/7, 1/2, ...]), derived_from(embedding(0), lookup, [token(0), embed_table])
  
Step 3: Attention scores → exact QK^T matrix
  Prolog: score(0, 1, 5/12), derived_from(score(0,1), dot_product, [query(0), key(1)])
  
Step 4: Softmax → exact attention weights, each row sums to exactly 1
  Prolog: weight(0, 1, 43545600/59565131), constraint(row(0), sum_to_one, verified)
  
Step 5: Value mixing → exact weighted sums
Step 6: Feedforward → exact linear transforms with exact ReLU
Step 7: Logits → exact scores over vocabulary
Step 8: Output distribution → exact probabilities summing to exactly 1
  
  Next token: "mat" with probability 3/7
  Derivation: complete proof tree from input tokens to output probability
  Constraints: all satisfied exactly
  Reproducibility: bit-identical on any machine
```

### 7.2 An Exact Provenance-Tracked Data Pipeline

```
Raw data: temperature readings [20.5, 21.3, 19.8] 
  → VDR: [VDR(41,2), VDR(213,10), VDR(99,5)]
  → Prolog: raw(sensor(1), time(t1), 41/2), source(file("readings.csv"), line(1))

Transform: Celsius to Kelvin (add 273.15 = 5463/20)
  → VDR: [VDR(5873,20), VDR(10389,20), VDR(6423,20)]  — wait, let me be exact
  → VDR: 41/2 + 5463/20 = 410/20 + 5463/20 = 5873/20
  → Prolog: kelvin(sensor(1), time(t1), 5873/20), 
            derived_from(kelvin(s1,t1), add, [raw(s1,t1), constant(273_15, 5463/20)])

Aggregate: mean temperature
  → VDR: (5873/20 + 5389/10 + 6423/20) / 3  — exact fraction
  → Prolog: mean_kelvin(batch(1), Result), 
            derived_from(mean_kelvin(b1), mean, [kelvin(s1,t1), kelvin(s1,t2), kelvin(s1,t3)])

Query: "What raw readings contributed to the mean?"
  → Prolog: depends_on(mean_kelvin(batch(1)), raw(Sensor, Time))
  → Answer: raw(sensor(1), time(t1)), raw(sensor(1), time(t2)), raw(sensor(1), time(t3))

Correction: raw reading t2 was wrong, should be 21.1 not 21.3
  → Prolog: affected_by(raw(sensor(1), time(t2)), V) 
  → Lists every derived value that needs recomputation
  → VDR recomputes exactly
  → Prolog updates the provenance graph
```

---

## 8. The Design Principles

### 8.1 Values Are Exact

No float anywhere. Every number is a VDR fraction. Every intermediate result is a VDR fraction. The number you see is the number that was computed is the number that should have been computed.

### 8.2 Derivations Are Recorded

No value exists without a provenance record. The record says: what operation produced this value, what were the inputs, what constraints apply, when was it computed. The record is a Prolog fact, queryable and inspectable.

### 8.3 Constraints Are Declared and Verified

Domain constraints are Prolog rules. They are checked after every computation. Violations are detected exactly, reported immediately, and traceable to the specific step that caused them.

### 8.4 Dependencies Are Tracked

The provenance graph is a directed acyclic graph connecting every value to its inputs. When an input changes, the set of affected downstream values is computable by graph traversal. Recomputation is targeted — only affected values are recomputed.

### 8.5 Everything Is Reproducible

Same inputs, same rules, same constraints → same exact outputs on any machine. This follows from VDR's platform-independent exact arithmetic and Prolog's deterministic evaluation order (with declared choice points for nondeterminism).

---

## 9. Implementation Roadmap

### 9.1 Phase 1: Bridge

Build the Python-Prolog bridge for exact rational exchange. Use pyswip or SWI-Prolog's janus interface. Verify that VDR fractions round-trip through Prolog without precision loss. This is the foundation.

### 9.2 Phase 2: Provenance Recording

Wrap VDR operations to automatically assert provenance facts into Prolog. Start with simple arithmetic: addition, multiplication, matrix operations. Each operation produces a Prolog fact recording the operation, inputs, and result. Query the provenance graph to verify it captures the computation structure.

### 9.3 Phase 3: Constraint Layer

Implement CLP(Q) constraints over VDR results. Start with linear constraints: sum-to-one for probability distributions, non-negativity, bounded parameters. Verify that constraint violations are detected exactly. Add nonlinear constraint verification by delegating computation to VDR.

### 9.4 Phase 4: ML Integration

Connect the provenance and constraint system to the VDR transformer. Every forward pass produces a complete provenance graph in Prolog. Every training step is constraint-checked. Every checkpoint includes both VDR parameters (exact fractions) and Prolog provenance (logical derivations).

### 9.5 Phase 5: Query Interface

Build the query layer that lets users ask questions about the data: "Why is this value what it is?" "What depends on this input?" "What constraints does this satisfy?" "What would change if this input changed?" The answers come from Prolog queries over the exact provenance graph.

---

## 10. What This Would Be

A data system where every value is exact, every derivation is recorded, every constraint is verified, every dependency is tracked, and every result is explainable. Not approximately. Not within tolerance. Exactly.

VDR provides the arithmetic. Prolog provides the logic. Together they provide something that no current data system offers: numbers you can trust, with reasons you can inspect, under constraints you can verify, connected by dependencies you can trace.

The current state of data systems is: values without reasons, computed by approximate arithmetic, with invisible dependencies and unverifiable constraints. The proposed state is the exact opposite in every dimension.

That is where this work is headed.
