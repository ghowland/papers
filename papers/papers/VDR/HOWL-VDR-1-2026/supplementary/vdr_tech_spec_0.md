# Terminating VDR — Technical Specification

## 1. What VDR Is

VDR is an exact arithmetic system built on ordered integer triples instead of scalars. Every value in the system is a finite tree of triples. There are no floats, no decimals, no limits, no epsilon tests, and no infinity anywhere inside the system. The system operates on exact integer structure and terminates on every valid input.

The primitive object is:

```
[V, D, R]
```

where V is an integer (the value slot), D is a nonzero integer (the denominator slot), and R is a remainder (the residual slot). R is either an integer or an integer plus a finite list of child VDR triples. Recursion exists only in R — never in V or D. Every valid object is a finite tree.

A closed object has R = 0. It behaves like an exact rational number: `[3, 4, 0]` corresponds to 3/4. An active object has R ≠ 0. It carries exact unresolved state that has not been collapsed into the value slot. The remainder is not error, not noise, not approximation residue. It is exact structure required to complete the object.

## 2. The Triple

The three slots are semantically distinct and irreducible.

**V (value slot):** An integer. The settled numerator-like component in the current denominator frame.

**D (denominator slot):** A nonzero integer. The frame in which V and R are interpreted. Negative denominators are valid in raw form. Normalization may later enforce a positive-denominator convention, but that is canonicality, not validity.

**R (remainder slot):** Either an atomic integer r, or a composite structure `r + X₁ + X₂ + ... + Xₙ` where r is an integer and each Xᵢ is a valid VDR triple. This is the only slot where recursion occurs.

No valid object may have fewer or more than three slots. No VDR triple may appear inside V or D. The tree always branches through R and only through R.

## 3. Validity

A VDR object is valid if and only if:

- It has exactly three slots
- V is an integer
- D is a nonzero integer
- R is a valid remainder (atomic integer, or integer base plus finite list of valid VDR children)
- Every child VDR in R is itself valid (recursive)
- The full recursive expansion is finite: finite depth, finite branching at every node, finite total node count
- The object is exact as written — no hidden continuation, no deferred tail, no limit interpretation

Validity does not require normalization. Both `[2, 4, 0]` and `[1, 2, 0]` are valid. Both `[1, -2, 0]` and `[-1, 2, 0]` are valid. Normalization is a separate layer for canonical comparison, not a condition of existence.

## 4. Closed vs Active

**Closed:** `[V, D, 0]` — the remainder is zero at the top level.

**Globally closed:** The remainder is zero at every level of the recursive tree. No descendant carries unresolved state.

**Active:** `[V, D, R]` with R ≠ 0 — the object carries exact residual structure. Under Path B semantics (chosen for this system), an active object is an exact operation-state object, not an ordinary scalar value. `[2, 5, 1]` is not the same object as `[3, 5, 0]`. The remainder is meaningful native state, not a delayed simplification waiting to be folded into V.

## 5. Equality

The system maintains two working equality relations and reserves a third.

**Structural equality (≡ₛ):** Two objects are structurally equal if and only if every slot matches exactly, recursively and in order. This is identity of representation.

**Normalized value equality (≡ₙ):** Two objects are normalized-value equal if and only if their normalized forms are structurally equal. This captures the idea that `[2, 4, 0]` and `[1, 2, 0]` represent the same canonical object.

For closed objects, value equality can also be checked by cross-multiplication: `[V₁, D₁, 0] ≡ₙ [V₂, D₂, 0]` when `V₁·D₂ = V₂·D₁`.

**Reserved active-state equivalence (≡ₐ):** A future relation for recognizing when two active objects in different denominator frames represent the same native state. Not yet fully defined.

Structural equality implies normalized value equality. The converse does not hold. Two structurally different objects may normalize to the same form. Two active objects with different remainder structures are distinct unless normalization explicitly identifies them.

## 6. Normalization

Normalization transforms a valid object into a canonical form without changing its value. It is required for equality testing, comparison, serialization, and reproducible computation. It is not required for an object to exist.

The normalization rules, applied recursively bottom-up:

**Sign placement:** The denominator is made positive in normalized form. If D < 0, negate both V and D. `[1, -2, 0]` normalizes to `[-1, 2, 0]`.

**GCD reduction on closed nodes:** For `[V, D, 0]`, divide both V and D by gcd(|V|, |D|). `[2, 4, 0]` normalizes to `[1, 2, 0]`. For active nodes, GCD reduction applies only if remainder semantics are preserved under the transformed scale.

**Atomic remainder consolidation:** At each remainder level, all integer contributions are summed into a single integer base. `1 + 2 + [X] + [Y]` becomes `3 + [X] + [Y]`.

**Canonical child ordering:** Immediate remainder children are sorted by a fixed deterministic rule — by denominator magnitude, then by value slot, then by remainder structure.

**Same-denominator child merge:** If two immediate children share the same denominator and a merge rule is defined and exact, they are combined into one child.

**Closed-form preference:** If the entire object (including all descendants) normalizes to remainder zero everywhere, it settles to a closed form.

**Child normalization:** Every child is normalized before the parent is normalized.

A normalized object satisfies all of the above simultaneously. Normalization must terminate in finite time on every valid finite input.

## 7. Scalar Projection

Scalar projection maps a VDR object outward into a rational or decimal value for comparison with conventional mathematics. It is external and secondary. It does not define what the object is inside VDR.

**Closed projection:** For `[V, D, 0]`, the scalar projection is `V/D`. This is exact and always defined.

**Legacy conversion (additive flattening):** For active objects, the legacy conversion is defined recursively:

```
legacy([V, D, 0]) = V/D
legacy([V, D, R]) = V/D + legacy(R)
```

where `legacy(r) = r` for atomic integer remainder, and `legacy(r + X₁ + ... + Xₙ) = r + legacy(X₁) + ... + legacy(Xₙ)` for composite remainder.

This flattening is a conversion operation, not a native semantic rule. Inside VDR, the remainder is completion structure, not an additive term. The native reading of `[Q, B, [S, D, 0]]` is "Q/B with exact completion [S, D, 0]", not "Q/B + S/D". The additive form is permitted only when converting out of VDR for comparison purposes.

**Denominator-sensitive completion:** The remainder contributes within the parent's denominator frame. The external comparison schema is:

```
Π([V, D, R]) = (V + ρ_D(R)) / D
```

where ρ_D(R) interprets the remainder as numerator-side completion relative to parent denominator D. For atomic remainder r, ρ_D(r) = r. For composite remainder with children, ρ_D(r + X₁ + ... + Xₙ) = r + Π(X₁) + ... + Π(Xₙ). This schema is what makes active rebasing semantically coherent when projected outward.

## 8. Closed Arithmetic

Closed arithmetic operates on `[V, D, 0]` objects and produces `[V', D', 0]` results. It is standard exact rational arithmetic expressed in triple form.

**Addition:**
```
[V₁, D₁, 0] + [V₂, D₂, 0] = [V₁·D₂ + V₂·D₁, D₁·D₂, 0]
```

**Subtraction:**
```
[V₁, D₁, 0] - [V₂, D₂, 0] = [V₁·D₂ - V₂·D₁, D₁·D₂, 0]
```

**Multiplication:**
```
[V₁, D₁, 0] × [V₂, D₂, 0] = [V₁·V₂, D₁·D₂, 0]
```

**Division (V₂ ≠ 0):**
```
[V₁, D₁, 0] ÷ [V₂, D₂, 0] = [V₁·D₂, D₁·V₂, 0]
```

Division by `[0, D, 0]` is invalid for any D.

All results are subject to normalization. The closed subclass is arithmetically closed under these operations (except division by zero). It satisfies commutativity, associativity, and distributivity under value equality. The additive identity is `[0, 1, 0]`. The multiplicative identity is `[1, 1, 0]`. The additive inverse of `[V, D, 0]` is `[-V, D, 0]`.

Under closed projection, these operations agree exactly with rational arithmetic. This is the verifiable rational core of VDR.

## 9. Active Arithmetic

Active arithmetic extends beyond the closed subclass. It is more constrained and partially provisional.

**Same-denominator addition:**
```
[V₁, D, R₁] + [V₂, D, R₂] = [V₁ + V₂, D, R₁ ⊕ R₂]
```

where ⊕ combines remainder structures: atomic bases are summed, child lists are concatenated, then normalization is applied. This is a same-frame state combination, not scalar addition.

**Same-denominator subtraction:**
```
[V₁, D, R₁] - [V₂, D, R₂] = [V₁ - V₂, D, R₁ ⊖ R₂]
```

where ⊖ subtracts atomic bases and appends negated children from the second operand.

**Remainder negation (recursive):**
```
-(r) = -r
-(r + X₁ + ... + Xₙ) = -r + (-X₁) + ... + (-Xₙ)
-[V, D, R] = [-V, D, -R]
```

**Different-denominator addition/subtraction:** Requires rebasing both operands into a shared denominator frame (default: D₁·D₂), then applying same-denominator rules. The remainder must be lifted into the new frame via the lift operator.

The cross-scaled form for different-denominator addition is:

```
[V₁, D₁, R₁] + [V₂, D₂, R₂] = [V₁·D₂ + V₂·D₁, D₁·D₂, lift(R₁, D₂) + lift(R₂, D₁)]
```

**Multiplication and division of active objects:** Semantically constrained but not fully constructively specified. The product must preserve all cross-term active structure. The axioms define placeholder operators (`mul_left`, `mul_right`, `mul_cross`) for the remainder contributions but do not yet give final formulas. If exact finite representation of the result is impossible, the operation fails.

## 10. Lift

Lift is the remainder transport operator. When a parent's denominator frame is scaled by factor k, lift rewrites the remainder structure so that it contributes correctly in the new frame.

**Atomic lift:**
```
lift(r, k) = k·r
```

**Composite remainder lift:**
```
lift(r + X₁ + ... + Xₙ, k) = k·r + lift(X₁, k) + ... + lift(Xₙ, k)
```

**Child VDR lift:**
```
lift([V, D, R], k) = [k·V, D, lift(R, k)]
```

The critical design decision: lift scales V and R of a child, but does not touch the child's D. The child keeps its own internal denominator identity. The numerator and remainder absorb the outer frame scaling. This is because lift is reweighting the child's contribution into a new parent frame, not restructuring the child internally.

Properties of lift:

- `lift(R, 1) = R` — identity
- `lift(R, -1) = -R` — negation
- `lift(lift(R, a), b) = lift(R, a·b)` — multiplicative composition
- `lift(R₁ + R₂, k) = lift(R₁, k) + lift(R₂, k)` — distributes over remainder addition
- `lift(0, k) = 0` — preserves closure
- Preserves validity, finiteness, and equality

Lift is exact integer-structural transport. No approximation, no float conversion, no decimal fitting. It terminates in finite time because every valid VDR object is finite.

## 11. Closed Rebase

Rebase changes the top-level denominator of a VDR object while preserving exact value.

For a closed object `[V, D, 0]` and target denominator B ≠ 0:

**Success condition:** `V·B / D` is an integer.

**Result:** `[V·B/D, B, 0]`

**Same-denominator rebase:** Identity — `rebase([V, D, R], D) = [V, D, R]`.

If `V·B/D` is not an integer, closed rebase fails. This is the trigger for active rebase.

Closed rebase preserves value equality, not structural equality. It changes representation, not value. It is deterministic, finite, and exact.

## 12. Active Rebase

Active rebase handles the case where closed rebase fails — the value cannot be expressed as a closed triple with the target denominator.

**The core algorithm for `[V, D, R]` rebased to denominator B:**

Step 1 — Scale the numerator demand:
```
N = V · B
```

Step 2 — Integer divide by source denominator:
```
N = Q · D + S
```
where Q is the quotient and S is the remainder from integer division.

Step 3 — Build the mismatch witness: `[S, D, 0]` — a closed child capturing the exact denominator mismatch.

Step 4 — Lift the existing remainder into the new frame: `lift(R, B)`.

Step 5 — Combine into the rebased form:
```
rebase([V, D, R], B) = [Q, B, [S, D, 0] + lift(R, B)]
```

Step 6 — Normalize. If S = 0 and lift(R, B) resolves to zero, the result collapses back to a closed form.

**Correctness check via legacy conversion:** For a closed source `[V, D, 0]` rebased to `[Q, B, [S, D, 0]]`, the legacy conversion gives:

```
Π([Q, B, [S, D, 0]]) = (Q + S/D) / B = (QD + S) / (BD) = VB / (BD) = V/D
```

which equals the original value. The denominator-sensitive completion semantics are what make this work — the child `[S, D, 0]` contributes through the parent's denominator frame B, not as an external additive term.

**Recursive rebase:** The mismatch child `[S, D, 0]` may itself be rebased into denominator B if that rebase terminates finitely. This can deepen the tree but must terminate. If repeated rebasing of residual children would produce an infinite chain, the target denominator is invalid for this object in terminating VDR.

**The transport problem with pre-existing remainder:** The axiom set defines `R' = [S, D, 0] + lift(R, B)` as the first-pass rule. The repair notes document that this naive rule can fail to preserve the legacy projection when the source is already active. The corrected requirement is that the rebased residual R' must satisfy:

```
(Q + ρ_B(R')) / B = (V + ρ_D(R)) / D
```

For rational sources, the completion operator (Section 14) always provides a correct R', so the practical system works. The general active-to-active case is marked as requiring careful verification.

## 13. Quotient Selection

When rebasing, the choice of Q is not unique. Different values of Q produce different valid rebased forms. Quotient selection is the canonical rule for choosing among them.

**The quotient search bound:** Candidate quotients are drawn from a finite set. For source X and target B, compute the legacy anchor `λ(X) = legacy(X)`. The candidate set is:

```
Q_min = floor(λ(X) · B) - 1
Q_max = ceil(λ(X) · B) + 1
```

This gives at most about 4 integer candidates. Floor and ceiling are used only as search fence generators — they do not define the selection semantics.

**The selection ordering (lexicographic, applied to each candidate's normalized rebased form):**

1. **Exact admissibility** — the candidate must produce a finite exact VDR completion that is value-equal to the source. Non-admissible candidates are discarded.
2. **Minimum recursive depth** — prefer shallower completion trees.
3. **Minimum denominator complexity** — measured as the tuple (number of distinct denominator magnitudes, sum of all denominator magnitudes, total denominator-bearing nodes), compared lexicographically. Rewards shared denominators.
4. **Minimum structural size** — counts one unit per VDR node plus one unit per atomic remainder base.
5. **Minimum |Q|** — smaller absolute quotient magnitude.
6. **Deterministic tie-break** — fixed system-wide rule (e.g., prefer positive Q).

**Zero-completion preference:** If any Q yields remainder zero (closed rebase), that Q must be selected. Closure always wins.

The selection is deterministic, finite, and non-approximative. The same source and target always produce the same canonical rebased form.

## 14. The Completion Operator

The completion operator `complete(L)` takes an exact leftover value L and produces a finite VDR object whose legacy conversion equals L, or fails.

**For L = 0:** Returns 0 (atomic zero remainder).

**For rational L = A/B:** Reduces to lowest terms A'/B', returns `[A', B', 0]`. This always succeeds. Every rational leftover is finitely completable as a closed child.

**For an already-valid VDR object:** Returns its normalized form.

**Otherwise:** Fails. Non-rational leftovers without known finite VDR representations are outside the current system.

This means that for the rational domain — which is the entire working domain of v1 — the rebase algorithm never fails due to completion impossibility. The real question is never "does a rebased form exist?" but "which one is simplest?"

## 15. Completion Semantics

The native reading of a VDR object is completion-based, not additive.

`[Q, B, [S, D, 0]]` reads as "Q/B with exact completion [S, D, 0]" — the child is the exact residual structure that finishes what the top-level frame started. It is not "Q/B plus S/D". The additive reading is valid only in legacy conversion mode, when leaving VDR for scalar comparison.

This distinction is what prevents active VDR from collapsing into decorated fraction arithmetic. The remainder is ontological state, not a pending calculation. Two objects with different remainder structures are natively different objects even if some external projection might map them to the same scalar.

## 16. Denominator Complexity

A structural measure for comparing exact completion candidates. Defined as the tuple:

```
den_complexity(X) = (u(X), s(X), m(X))
```

where:
- u(X) = number of distinct denominator magnitudes in the entire object
- s(X) = sum of all |D| values across every node
- m(X) = total count of denominator-bearing nodes

Compared lexicographically. Rewards denominator unification (fewer distinct values) over raw smallness. A completion with one shared denominator used twice beats one with two different smaller denominators.

## 17. Structural Size

A pure form measure counting representational bulk:

```
size(r) = 1                          (atomic integer)
size(r + X₁ + ... + Xₙ) = 1 + Σ size(Xᵢ)    (composite remainder)
size([V, D, R]) = 1 + size(R)           (VDR node)
```

Independent of numeric magnitude. `[1, 2, 0]` and `[10¹⁰⁰, 7, 0]` both have size 2. A closed object always has size 2. A single-child active object has size 3. Used only as a late tie-breaker after depth and denominator complexity.

## 18. Inbound Construction

External values enter VDR through exact inbound construction.

**Integers:** `in(n) = [n, 1, 0]`

**Rationals:** `in(a/b) = [a, b, 0]` subject to normalization.

**Direct specification:** Any valid triple can be admitted directly if it satisfies all validity rules.

**Rejected:** Approximate decimals, malformed notation artifacts, values requiring infinite structure. A float approximation of π does not become an exact VDR representation of π by being placed into triple syntax. If the intended object is the rational 314159/100000, that is admitted exactly as `[314159, 100000, 0]`. But that is not π.

## 19. The Data Model

The implementation shape is a finite rooted tree.

```
VDR = { v: Int, d: NonZeroInt, r: Remainder }

Remainder = Atomic(Int) | Composite { base: Int, children: List<VDR> }
```

Atomic remainder `r` can be treated as `Composite { base: r, children: [] }` for uniformity. Integers must be arbitrary-precision exact integers. No floats anywhere. No pointer cycles — tree structure only.

Required operations: validate, normalize, structural_equal, value_equal, project_closed, project_legacy, add, sub, mul, div, neg, rebase, lift, parse, serialize. Each operation either returns a valid result or explicit failure. No silent approximation.

## 20. Failure

Failure is a first-class outcome. Operations fail explicitly when:

- Denominator would be zero
- Division by zero object
- Rebase would require infinite recursion
- Active multiplication/division cannot produce finite exact result
- Approximate input presented as exact admission
- Any operation would require non-integer, non-finite, or non-exact structure

Failure is not error in the sense of malfunction. It is the correct answer when exact finite representation is impossible. The system prefers honest failure over silent approximation.

## 21. What the System Can Do Now

The working v1 system handles:

- All integers, exactly
- All rational numbers, exactly
- Exact rational arithmetic (add, sub, mul, div)
- Exact normalization and equality testing
- Exact closed rebasing (when denominator divides cleanly)
- Exact active rebasing (when it doesn't — producing finite completion structure)
- Exact remainder transport via lift
- Canonical quotient selection for rebase
- Exact scalar projection at the boundary
- Active same-frame addition and subtraction
- Recursive remainder negation

## 22. What the System Cannot Do Yet

- Active multiplication and division beyond the closed subclass (semantically constrained, not constructively complete)
- Exact representation of algebraic irrationals (√2, etc.)
- Exact representation of transcendental constants (π, e)
- Full active-state equivalence across denominator frames
- General active rebase with pre-existing remainder (first-pass rule exists, full correctness requires case-by-case verification)
- Exhaustive inbound construction from non-rational external specifications

These are open research frontiers, not failures. The system is designed to grow into them without redesign of the foundation.

## 23. The Invariants

Every conforming implementation must preserve:

1. Every object has exactly three slots
2. D is never zero
3. Recursion occurs only through R
4. Every object is finite
5. Every operation returns exact finite result or explicit failure
6. Normalization never leaves the VDR domain
7. Structural equality is exact recursive equality
8. Scalar projection does not redefine native identity
9. No approximation enters any native operation
10. Lift does not alter child denominators
11. Rebase preserves value equality
12. Closed arithmetic agrees with rational arithmetic under projection
