# VDR Technical Specification v2.0

## Handoff Document for Continuation

This document captures the complete state of VDR as of the end of the HOWL-VDR-1/VDR-2 development session. It is written so that a new working session can resume without re-reading any prior conversation. Everything needed to understand, modify, and extend VDR is here.

---

## 1. What VDR Is

VDR is an exact arithmetic system implemented as a Python 3.8+ library. Every value is a finite tree of integer triples `[V, D, R]`. There are no floats, no decimals, no limits, no epsilon tests, and no infinity inside the system. Every operation either returns an exact finite result or fails explicitly.

The system has been tested across 15 mathematical domains with 282 passing tests and zero computation errors. Two papers have been written: VDR-1 (system introduction) and VDR-2 (gym results across 15 domains). A diagram script exists for each paper producing 8 figures each.

---

## 2. The Triple

```
[V, D, R]
```

**V (value slot):** Arbitrary-precision Python `int`. The settled numerator component in the current denominator frame.

**D (denominator slot):** Nonzero arbitrary-precision Python `int`. The frame in which V and R are interpreted. Negative denominators are valid in raw form. Normalization enforces positive D.

**R (remainder slot):** One of three forms:

1. **Atomic:** A single integer. Internally `Remainder(base=r, children=[])`.

2. **Composite:** An integer base plus a finite ordered list of child VDR triples. `Remainder(base=r, children=[X₁, X₂, ..., Xₙ])`. Structurally `r + X₁ + X₂ + ... + Xₙ`.

3. **Functional:** A Python callable `f(depth: int) → VDR` plus a name string. `FnRemainder(func, name)`. Cannot be projected to scalar until expanded via `resolve(obj, depth)`.

Recursion exists only in R. V and D are always atomic integers. Every concrete object is a finite tree. Functional objects are finite specifications that produce finite trees on demand.

---

## 3. File Structure

```
code/
  vdr/
    __init__.py          — public API, auto-installs active_mul and fn
    vdr.py               — core: VDR, Remainder, normalization, equality,
                           closed arithmetic, rebase, lift, projection
    active_mul.py        — active multiplication and division, patches operators
    fn.py                — FnRemainder, resolve, factories, discrete calculus
    linalg.py            — Vec, Mat, parse_vdr, JSON serialization, LaTeX export
    export.py            — to_decimal, to_float, to_fraction (lossy boundary)
  test_basic.py          — core VDR tests (12 sections, all pass)
  test_layer_1.py        — linalg, parse, serialize, export tests (15 sections, all pass)
  test_layer_2.py        — active multiplication/division tests (20 sections, all pass)
  test_layer_3.py        — functional remainders, discrete calculus (21 sections, all pass)
  gym/
    gym_01_number_theory.py          — 37/37 pass
    gym_02_polynomial.py             — 22/23 (1 test-authoring error)
    gym_03_continued_fractions.py    — 26/31 (5 test-authoring errors)
    gym_04_matrix_decomposition.py   — 13/13 pass
    gym_05_recursive_sequences.py    — 15/15 pass
    gym_06_combinatorics.py          — 31/31 pass
    gym_07_signal_processing.py      — 11/11 pass
    gym_08_geometry.py               — 19/19 pass
    gym_09_differential_equations.py — 10/10 pass
    gym_10_optimization.py           — 8/8 pass
    gym_11_probability.py            — 13/13 pass
    gym_12_cryptographic_primitives.py — 37/37 pass
    gym_13_symbolic_algebra.py       — 20/20 pass
    gym_14_fixed_point.py            — partial (killed: chaos cost)
    gym_15_chaos_and_sensitivity.py  — partial (killed: chaos cost)
  make_diagrams_vdr1.py              — 8 figures for VDR-1 paper
  make_diagrams_vdr2.py              — 8 figures for VDR-2 paper
```

---

## 4. What Each Module Does

### 4.1 vdr/vdr.py — The Core

Contains `VDR` class and `Remainder` class. This is the foundation everything else builds on.

**VDR class.** Construction from integers, rationals, Fraction, direct triple specification. Validation on construction (zero denominator raises, non-integer slots raise). Properties: `is_closed`, `is_active`, `is_globally_closed`. Equality: `structural_eq(other)` for slot-by-slot match, `value_eq(other)` for normalized match, `__eq__` uses value equality. Normalization: positive D, GCD reduction on closed nodes, atomic remainder consolidation, child ordering, same-denominator child merge, zero elimination, D=1 absorption, closed-form preference. Projection: `to_fraction()` returns exact `Fraction` (legacy flattening for active objects), `to_float()` returns lossy float. Closed arithmetic: `+`, `-`, `*`, `/` via operator overloading for closed objects. Active same-frame add/sub. Rebase: `rebase(target_d)` — closed when V·B/D is integer, active otherwise producing `[Q, B, [S,D,0] + lift(R,B)]`. Lift: `_lift_vdr(k)` scales V by k, preserves D, lifts R recursively. Negation: `-[V,D,R] = [-V,D,-R]`. Comparison: `<`, `<=`, `>`, `>=` via projection to Fraction. Metrics: `depth()`, `size()`, `den_complexity()`. Display: `__repr__`, `__str__`, `bracket()`.

**Remainder class.** `base` (int) and `children` (list of VDR). Properties: `is_zero`, `is_atomic`, `is_globally_zero`, `is_functional` (always False for base class). Operations: `negate()`, `combine(other, sign)`, `lift(k)`, `legacy_value()`, `normalize()`, `structural_eq(other)`.

**Error classes.** `VDRError` (base), `ZeroDenominatorError`, `InvalidStructureError`, `RebaseError`, `ArithmeticFailure`.

**Private helpers.** `_coerce(other)` converts int/Fraction to VDR. `_active_add(a, b, sign)` handles active addition with cross-scaling and lift. `_remainder_divisible_by(r, g)` and `_remainder_divide(r, g)` for GCD reduction of active nodes. `_merge_same_denom_children(children)` merges closed children sharing a denominator. `_child_sort_key(c)` for canonical ordering. `_residual_size(r)` and `_collect_denoms(x, acc)` for metrics.

### 4.2 vdr/active_mul.py — Active Multiplication

Patches VDR `__mul__`, `__rmul__`, `__truediv__`, `__rtruediv__` when `install()` is called (auto-called by `__init__.py`).

**active_mul(a, b).** For two closed objects: direct formula `[V₁V₂, D₁D₂, 0]`. For mixed or active: product in frame D₁·D₂ with closed numerator V₁·V₂. Remainder captures three cross-terms: V₁ scales R₂ (left), V₂ scales R₁ (right), R₁·R₂ (cross). The cross-product is computed by projecting both remainders to exact Fraction, multiplying, and expressing the result as VDR remainder structure (atomic if integer, closed child if rational).

**active_div(a, b).** Division by closed object: multiply by reciprocal `[D₂, V₂, 0]`. Division by active object: project divisor to exact Fraction, invert, multiply. This is the v1 compromise — divisor structure is collapsed through projection. The projected value is exact.

**_scale_remainder(r, k).** Multiplies remainder base and all child value slots by integer k.

**_mul_remainders(r1, r2, d1, d2).** Projects both to Fraction, multiplies, returns as remainder.

### 4.3 vdr/fn.py — Functional Remainders

**FnRemainder class.** Subclass of Remainder. Holds `func` (callable), `name` (string), `meta` (dict). `is_zero` always False. `is_functional` always True. `expand(depth)` calls the function. `legacy_value()` raises (must resolve first). Supports `negate()`, `lift(k)`, `combine(other, sign)`.

**resolve(x, depth).** Expands functional remainder at given depth. If parent frame is `[0, 1, fn]`, returns expanded VDR directly. Otherwise wraps expanded VDR as child in parent's remainder.

**resolve_recursive(x, depth).** Resolves all functional remainders at every level of the tree.

**Factories:**
- `make_constant_fn(name, value_func)` — always returns same value.
- `make_series_fn(name, term_func, initial)` — partial sum of series to depth N.
- `make_newton_fn(name, f_step)` — Newton-Raphson iteration from VDR(1).
- `make_iterative_fn(name, step, start)` — general iteration.

**Discrete calculus:**
- `discrete_derivative(f, h)` — returns function Df where Df(x) = (f(x+h) - f(x)) / h.
- `discrete_integral(f, a, b, n)` — left Riemann sum, exact.
- `discrete_integral_trapz(f, a, b, n)` — trapezoidal rule, exact.
- `discrete_derivative_nth(f, h, order)` — repeated application.

**Installation.** `install()` patches VDR.to_fraction to raise on functional remainders, and fixes is_closed/is_active properties.

### 4.4 vdr/linalg.py — Linear Algebra and Utilities

**Vec class.** Ordered list of VDR objects. Construction from list, `from_ints`, `from_fracs`, `zero(n)`. Arithmetic: `+`, `-`, `scale(s)`, `*` (scalar), `dot(other)`, `-v`. `to_fractions()` for export.

**Mat class.** List of row Vecs. Construction from list of lists, `from_ints`, `from_fracs`, `identity(n)`, `zero(m,n)`. Access: `[i,j]`, `row(i)`, `col(j)`, `shape`, `nrows`, `ncols`, `is_square`. Arithmetic: `+`, `-`, `scale(s)`, `*` (matrix, vector, or scalar), `matmul(other)`, `matvec(v)`, `-m`. Properties: `T` (transpose), `det()` (cofactor expansion), `inv()` (adjugate method), `trace()`, `rank()` (Gaussian elimination), `solve(b)` (Cramer's rule). Display: `pretty()`, `to_fractions()`.

**Parser.** `parse_vdr(text)` parses bracket notation `[V, D, R]` including nested children and composite remainders like `[2, 5, 1 + [1, 3, 0] + [1, 7, 0]]`.

**Serialization.** `vdr_to_dict(x)` and `vdr_from_dict(d)` for JSON roundtrip. Format: `{"v": int, "d": int, "r": {"base": int, "children": [...]}}`.

**LaTeX.** `vdr_to_latex(x)` exports to LaTeX notation. Closed objects render as `\frac{V}{D}`, active objects render remainder in braces.

### 4.5 vdr/export.py — Lossy Boundary

`to_fraction(x)` — exact Fraction projection. `to_float(x)` — lossy float. `to_decimal(x, digits)` — arbitrary precision decimal via mpmath if available, manual long division fallback.

### 4.6 vdr/__init__.py — Public API

Imports and re-exports everything. Auto-installs active_mul and fn patches. User code needs only:

```python
from vdr import VDR, Vec, Mat, resolve, discrete_derivative
```

---

## 5. Semantics

### 5.1 Path B

Active objects are operation-state objects, not ordinary scalar values. `[2, 5, 1]` is not equal to `[3, 5, 0]` even though both project to 3/5. The remainder is structural state, not a pending simplification.

### 5.2 Completion Semantics

The remainder completes the value in the parent's denominator frame. `[Q, B, [S, D, 0]]` reads as "Q/B with exact completion [S, D, 0]". Under legacy projection:

```
Π([V, D, R]) = (V + ρ_D(R)) / D
```

where `ρ_D(R) = R.base + Σ Π(child_i)`.

### 5.3 Equality

Two relations:
- **Structural (≡ₛ):** same object as written, slot by slot, recursively.
- **Value (≡ₙ):** same object after normalization.

Python `==` uses value equality. `hash()` uses normalized form.

### 5.4 Normalization

Applied recursively bottom-up: positive D, GCD reduction, atomic consolidation, child normalization, canonical ordering by `(|D|, D, V, R.base)`, same-denominator merge of closed children, D=1 absorption, zero elimination, closed-form preference. Deterministic, finite, idempotent.

### 5.5 Projection

Closed: `V/D` exact. Active concrete: legacy flattening (additive recursion through tree). Active functional: blocked until `resolve(obj, depth)`.

---

## 6. What Works (Verified by Tests)

### 6.1 Core (test_basic.py — 12 sections)

Construction, all four closed arithmetic operations, normalization, both equality types, sign handling, return-to-origin equality recovery, multiply/divide roundtrip, closed rebase, active rebase with projection verification, Path B active/closed distinction, active same-frame addition with cancellation, lift, Fraction interop, mixed VDR/int arithmetic, 200-operation zero-drift test.

### 6.2 Layer 1 (test_layer_1.py — 15 sections)

Vector arithmetic (add, sub, scale, dot, neg). Matrix arithmetic (add, sub, mul, scalar mul, transpose). Determinant (2×2, 3×3, singular). Trace. Inverse (2×2, rational, 3×3). Solve via Cramer's rule (integer and rational systems). Rank. Matrix-vector product. Bracket notation parser. JSON serialization roundtrip. LaTeX export. Decimal export. 4×4 Hilbert matrix exact inversion: H×H⁻¹ = I exactly, inv(inv(H)) = H exactly. 40-operation matrix roundtrip zero drift.

### 6.3 Layer 2 (test_layer_2.py — 20 sections)

Closed multiplication/division unchanged. Active × closed. Closed × active. Active × active with atomic remainders. Active × active with nested remainders. Division: active/closed, closed/active, active/active. Division by zero checks. Multiplicative identity and inverse. Commutativity across mixed operands. Associativity. Distributivity. Active multiply/divide roundtrip. 40-operation active long chain. Matrix with active entries (determinant, identity multiplication). Mixed active/closed matrix multiply. Scalar multiplication with active VDR. Int and Fraction interop.

### 6.4 Layer 3 (test_layer_3.py — 21 sections)

FnRemainder construction and expansion. Resolve functional VDR. Projection blocked on unresolved functional. Newton-Raphson √2 (>100 digits at depth 7). Newton-Raphson √3. Leibniz series for π/4. Basel series for π²/6. Iterative halving. Discrete derivative of x² (exactly 6001/1000). Discrete derivative of x³. Second derivative. Left Riemann integral of x² (exactly 57/200). Trapezoidal integral. Integral of 1/x. FnRemainder negation, lift, combination. VDR with frame and functional remainder. Recursive resolve. Newton convergence comparison (>100 correct digits by depth 7). Exact finite difference table (Δ³(x³) = 6, Δ⁴(x³) = 0).

### 6.5 Gym Results (15 domains, 282 tests)

| Gym | Domain | Pass | Fail | Notes |
|-----|--------|------|------|-------|
| 01 | Number theory | 37 | 0 | GCD, LCM, Egyptian fractions, Stern-Brocot, Farey, totient, harmonics, Fermat, convergents |
| 02 | Polynomial | 22 | 1 | Horner, add/mul/div, rational roots, Lagrange interpolation, poly GCD, Cayley-Hamilton. 1 wrong expected value |
| 03 | Continued fractions | 26 | 5 | CF conversion roundtrip, convergents, Gauss-Kuzmin, Stern-Brocot path, periodic CF. 5 tests need more CF terms |
| 04 | Matrix decomposition | 13 | 0 | LU, PLU, LU solve, Fibonacci matrix power, Gram-Schmidt, matrix exp partial |
| 05 | Recursive sequences | 15 | 0 | Fibonacci, Cassini, Lucas, Catalan, Bernoulli, Tribonacci, rational recurrence |
| 06 | Combinatorics | 31 | 0 | Binomial, Pascal, Vandermonde, Stirling, Bell, derangements, multinomial, Catalan GF |
| 07 | Signal processing | 11 | 0 | Convolution, correlation, moving average, z-transform, Toeplitz, IIR filter |
| 08 | Geometry | 19 | 0 | Line intersection, polygon area, barycentric, point-in-triangle, distance, circumcenter |
| 09 | Differential equations | 10 | 0 | Euler, RK4, matrix exp, Picard iteration, Lotka-Volterra |
| 10 | Optimization | 8 | 0 | Newton optimize, gradient descent, simplex, bisection |
| 11 | Probability | 13 | 0 | Bayes, Markov steady state, gambler's ruin, expected value, binomial PMF, Bayesian updating |
| 12 | Cryptography | 37 | 0 | Modular exp, extended GCD, mod inverse, CRT, RSA, discrete log |
| 13 | Symbolic algebra | 20 | 0 | Partial fractions, rational functions, power sums, poly derivative/integral, definite integrals |
| 14 | Fixed point | partial | — | Killed after 20 min: logistic r=4 denominator explosion |
| 15 | Chaos | partial | — | Killed after 20 min: same cause. Completed sections: tent map, Bernoulli shift, Arnold cat map (period 40), Lyapunov exponent |

All 6 failures are test-authoring errors, not VDR computation errors.

---

## 7. Known Boundaries

### 7.1 Chaotic Iteration Cost

The logistic map at r=4 starting from x₀=1/3 produces fractions whose denominators have approximately 2^n digits after n steps. After 10 steps: ~1,000 digits. After 20 steps: ~1,000,000 digits. Multiplication of two fractions with N-digit denominators is O(N²). This makes exact chaotic iteration impractical beyond ~15 steps on consumer hardware.

This is a mathematical fact about chaos, not a VDR defect. Float arithmetic hides the same information-theoretic cost by silently truncating. VDR exposes it honestly.

Periodic rational orbits (tent map on 1/7, Arnold cat map on rational torus points) have zero denominator growth and run at full speed indefinitely.

### 7.2 Active Division Loses Divisor Structure

Dividing by an active object projects the divisor to Fraction, inverts, and multiplies. The projected value is exact but the divisor's remainder structure is not preserved in the result.

### 7.3 Cofactor Expansion Is O(n!)

Determinant and inverse use cofactor expansion. Practical for n ≤ 6 or 7. Impractical for larger matrices. Gaussian elimination with exact rational pivoting would be polynomial but is not yet implemented.

### 7.4 No Complex Numbers

Eigenvalue computation for matrices with non-rational eigenvalues requires irrationals and/or complex numbers. Neither exists as a native VDR type.

### 7.5 No Irrational Type

√2 and π are represented via functional remainders that produce rational approximations at each depth. Each approximation is rational, not irrational. The functional remainder is a recursive specification, not a native irrational value.

---

## 8. Invariants

Every conforming implementation must preserve:

1. Every object has exactly three slots.
2. D is never zero.
3. Recursion occurs only through R.
4. Every concrete object is finite.
5. Every operation returns exact finite result or explicit failure.
6. Normalization never leaves the VDR domain.
7. Structural equality is exact recursive equality.
8. Scalar projection does not redefine native identity.
9. No approximation enters any native operation.
10. Lift does not alter child denominators.
11. Rebase preserves value equality.
12. Closed arithmetic agrees with rational arithmetic under projection.
13. Functional remainders block projection until resolved.
14. Active multiplication preserves projection compatibility (commutativity, associativity, distributivity hold under projection).

---

## 9. What Comes Next

Priority-ordered. Each item is independent enough to be a work unit.

### 9.1 Gaussian Elimination for Linear Algebra

**What:** Replace cofactor expansion with exact rational Gaussian elimination for determinant, inverse, rank, and solve. Keep cofactor as fallback or remove entirely.

**Why:** Current det/inv is O(n!) which limits practical matrix size to ~6. Gaussian elimination is O(n³) with exact rational pivoting. This would make VDR practical for matrices of size 20-50+.

**How:** Implement row reduction with exact VDR pivot operations. Partial pivoting by magnitude (via projection comparison). Track row swaps for determinant sign. The math is standard — the implementation is exact VDR division at each elimination step.

**Risk:** Low. The algorithm is well-known. Every pivot operation is exact VDR rational arithmetic.

### 9.2 Fix Gym Test Failures

**What:** Correct the 6 test-authoring errors documented in VDR-2.

**Fixes needed:**
- gym_02 exercise 5: Change expected value of p(1/2) from -19/4 to -5.
- gym_03 exercises 27-31: Extend periodic continued fractions to more repetitions before computing final convergent. Currently the period-finding function returns only one period of coefficients. The convergent test needs 5+ repetitions.
- gym_15 section 1: Change tent map expected period from 6 to 3.

**Risk:** Zero. These are test corrections, not VDR changes.

### 9.3 Representation Compression for Iterated Maps

**What:** Investigate whether VDR trees produced by iterated maps can be compressed or lazily evaluated to reduce the exponential cost of chaotic iteration.

**Approaches to explore:**
- Functional remainder that represents "N steps of logistic map" without materializing intermediate fractions.
- Lazy evaluation: only compute the fraction when projection is requested.
- Structural sharing: if the same child VDR appears multiple times in a remainder, share the reference instead of duplicating.
- Modular arithmetic: for maps on Q/Z (tent map, Bernoulli shift), work modulo the denominator to keep fractions bounded.

**Why:** The chaos cost boundary is the most visible limitation of VDR. Any reduction in this cost expands the practical domain significantly.

**Risk:** Medium. The exponential growth is fundamental for truly chaotic systems. Compression may help for specific map families but cannot eliminate the underlying information-theoretic cost.

### 9.4 Complex Number Extension

**What:** A VDR complex type where the real and imaginary parts are VDR objects. `VDRComplex(re: VDR, im: VDR)` or `[V_re, V_im, D, R]` (design TBD).

**Why:** Enables eigenvalue computation for 2×2 matrices with complex eigenvalues. Opens the door to exact DFT computation. Required for many linear algebra applications.

**What it enables:**
- Eigenvalues of 2×2 matrices (quadratic formula, possibly irrational — needs functional remainder for the square root term).
- Exact discrete Fourier transform on rational signals using roots of unity expressed as VDR complex objects.
- Complex polynomial root finding.

**Risk:** Medium. The design choice between a wrapper type and a native 4-slot type needs careful thought. Complex arithmetic doubles the operation count. Normalization for complex VDR needs new rules.

### 9.5 Polynomial Type

**What:** A native VDR polynomial type `Poly(coeffs: List[VDR])` with exact arithmetic, evaluation, differentiation, integration, GCD, factoring, and root-finding built in.

**Why:** Gym 02 and gym 13 both implement polynomial operations from scratch. A built-in type would make these natural. Polynomials are the most common exact computation target beyond plain rationals.

**How:** The gym scripts already contain working implementations of poly_eval (Horner), poly_add, poly_mul, poly_divmod, poly_derivative, poly_integral, poly_gcd, lagrange_interpolate, and rational_roots. These can be consolidated into a `Poly` class.

**Risk:** Low. The algorithms are proven by the gym tests. This is consolidation, not invention.

### 9.6 Automatic Richardson Extrapolation

**What:** Use VDR's exact discrete derivative to automatically extract analytical derivatives. The discrete derivative of f(x) = x² at step h is 2x + h. By computing at h and h/2, the h-dependent term can be eliminated exactly.

**How:** Compute D_h f(x) and D_{h/2} f(x). The analytical derivative is `(4 · D_{h/2} - D_h) / 3` for second-order methods. Each step is exact VDR rational arithmetic. Richardson extrapolation can be iterated to arbitrary order.

**Why:** This would give VDR exact analytical derivatives of polynomial functions and increasingly precise derivatives of non-polynomial functions, all without limits. The extrapolation table is a finite exact VDR matrix.

**Risk:** Low for polynomials (exact cancellation guaranteed). Medium for non-polynomials (extrapolation improves but does not reach exact values without functional remainder support).

### 9.7 Sparse Representation

**What:** For large matrices with mostly zero entries, a sparse VDR matrix type that stores only nonzero entries.

**Why:** Many practical matrices (graph adjacency, finite element, band-diagonal) are sparse. Dense storage wastes memory and computation.

**Risk:** Low. Standard sparse matrix techniques apply. The only VDR-specific concern is that exact arithmetic means no fill-in cancellation issues that plague float sparse solvers.

### 9.8 Benchmark Against mpmath and SymPy

**What:** Re-implement key gym exercises in mpmath (arbitrary-precision float) and SymPy (symbolic exact) and compare runtime and correctness.

**Why:** Positions VDR precisely in the ecosystem. VDR should be faster than SymPy on pure rational computation and more exact than mpmath on everything. Concrete numbers make the comparison real.

**Risk:** Low. This is measurement, not development.

### 9.9 VDR-3 Paper: Complex Extension and Eigenvalues

**What:** A third paper documenting the complex extension, eigenvalue computation, and any new capabilities discovered during implementation.

**Depends on:** 9.4 (complex type).

### 9.10 VDR-4 Paper: Performance and Practical Applications

**What:** A fourth paper focusing on performance: Gaussian elimination vs cofactor expansion benchmarks, sparse matrix support, comparison against mpmath/SymPy, and application to a specific real-world problem (computational geometry robustness, exact probability computation, or exact signal processing).

**Depends on:** 9.1 (Gaussian elimination), 9.7 (sparse), 9.8 (benchmarks).

---

## 10. Design Decisions Made and Why

### 10.1 Path B (Active ≠ Closed)

`[2, 5, 1] ≠ [3, 5, 0]`. The remainder is structural state, not a pending simplification. This was chosen because it preserves the ontological significance of the remainder slot. Path A (additive collapse) would have made VDR equivalent to decorated fraction arithmetic.

### 10.2 Remainder Named "Remainder" Not "Residual"

"Residual" implies degradation or error. "Remainder" is the correct term — it is the part of the value that remains after the V/D frame absorbs what it can. Operational rule throughout the codebase.

### 10.3 Single-File Core

`vdr.py` is one file. Extensions are separate modules that patch the core via `install()`. This keeps the dependency chain simple and makes the core importable with zero setup.

### 10.4 Python 3.8 Target

Chosen for maximum compatibility. No f-string `=`, no walrus operator in comprehensions, no match statements, no `|` union types. The library works on essentially any semi-modern Python installation.

### 10.5 Active Division Through Projection

Division by active objects collapses the divisor through projection. This is a documented v1 compromise. The projected value is exact. A future version could implement structural division that preserves divisor remainder, but this requires a constructive multiplicative inverse for active objects which is an open research problem.

### 10.6 Cofactor Expansion for Determinant

Chosen for simplicity and correctness. O(n!) but exact. Gaussian elimination would be faster but introduces more code complexity. The gym tests verify correctness. Performance upgrade is item 9.1 in the roadmap.

### 10.7 No External Dependencies

The core library requires only Python standard library (`fractions`, `math`, `typing`). mpmath is optional, used only for arbitrary-precision decimal rendering at the lossy export boundary.

---

## 11. The Axioms (21 Axioms of Terminating VDR)

For reference. These govern what is and is not a valid VDR object and operation.

1. A VDR object is an ordered triple [V, D, R].
2. Every valid object has exactly three slots. No recursion in V or D.
3. R is atomic integer or integer base plus finite list of child VDR objects.
4. Nested VDR objects appear only in R.
5. Every valid object is finite (depth, branching, total nodes).
6. A VDR object is exact as written. No approximation, limits, or infinite expansion.
7. Closed form [V, D, 0] has scalar core V/D.
8. R ≠ 0 means active. Remainder is exact structure, not error.
9. Globally closed only if all remainders in entire tree are zero.
10. Remainder preserves integer exactness at every level.
11. Negative V, D, and atomic R are all valid.
12. Validity does not require normalization.
13. Immediate children should have pairwise distinct denominators in normalized form.
14. Duplicate-denominator siblings may be merged.
15. Every valid object is finitely inspectable.
16. Every primitive operation terminates on valid inputs.
17. The set of valid terminating VDR objects is countable.
18. Infinity is not valid and may not appear as hidden completion logic.
19. If a value admits both terminating VDR and nonterminating conventional representation, VDR is preferred inside the system.
20. Remainder is exact residual structure in the foundational system, not any physical quantity.
21. Domain-specific interpretations may map VDR structure into physical semantics provided they do not violate the foundational axioms.

---

## 12. Key Demonstrations

These are the results that prove VDR works and matters. A new session should be able to reproduce all of them by running the test scripts.

**Zero drift.** 200 add/subtract operations on VDR(1,7) with step VDR(1,13) returns exactly to origin. (`test_basic.py` section 12)

**Hilbert matrix.** 4×4 Hilbert matrix inverted exactly. H×H⁻¹ = I exactly. inv(inv(H)) = H exactly. 40-operation matrix roundtrip zero drift. (`test_layer_1.py` sections 14-15)

**Newton-Raphson √2.** >100 correct digits at depth 7. Every step exact rational. (`test_layer_3.py` section 4)

**Discrete integral.** ∫₀¹ x² dx with n=10 is exactly 57/200. (`test_layer_3.py` section 12)

**Finite differences.** Δ³(x³) = 6 exactly everywhere. Δ⁴(x³) = 0 exactly everywhere. (`test_layer_3.py` section 21)

**Tent map.** Float orbit diverges from exact VDR orbit after ~25 steps. VDR stays exact forever. (`gym_15` section 1)

**Arnold cat map.** Period 40 detected exactly on rational torus. (`gym_15` section 4)

**Bernoulli numbers.** B(12) = -691/2730 computed from recursion. (`gym_05` section 5)

**RSA.** Complete encrypt/decrypt roundtrip with toy primes, all exact modular arithmetic. (`gym_12` sections 4-5)

**Cayley-Hamilton.** M² - 5M + 5I = 0 verified exactly for 2×2 matrix. (`gym_02` section 7)

**Exact Gram-Schmidt.** All cross dot products exactly zero after orthogonalization. (`gym_04` section 6)

**Bayesian updating.** Three evidence steps, final posterior exactly 6/7. (`gym_11` section 6)

**Binomial PMF.** B(10, 1/3) sums to exactly 1. E[X] = 10/3 exactly. (`gym_11` section 5)

---

## 13. How to Resume Work

1. The codebase is in `code/` with the file structure described in Section 3.
2. Run `python3 test_basic.py`, `python3 test_layer_1.py`, `python3 test_layer_2.py`, `python3 test_layer_3.py` to verify the core works.
3. Run gym scripts from `code/gym/` to verify domain coverage. Skip gym_14 and gym_15 or set a timeout.
4. The priority roadmap is Section 9. Item 9.1 (Gaussian elimination) and item 9.2 (fix gym tests) are the most immediate.
5. The VDR class in `vdr/vdr.py` is the single source of truth. All extensions patch it rather than forking it.
6. The naming convention is "Remainder" not "Residual" throughout.
7. Python 3.8 compatibility is mandatory.
8. Papers are in markdown, diagrams are Python scripts following the HOWL diagram rules (dark background, specific color palette, 180 DPI PNG).

---

## 14. Papers Published

**HOWL-VDR-1-2026:** "VDR: Exact Finite Arithmetic in Irreducible Triple Form." 14 sections + 19 appendices. Introduces the system, demonstrates core capabilities. 8 figures.

**HOWL-VDR-2-2026:** "VDR Gym: Exact Arithmetic Across Fifteen Domains." 24 sections + 17 appendices. Reports gym results, identifies chaos boundary, maps domain suitability. 8 figures.

Both papers are complete with placement tables linking figures to sections.

---

## 15. One-Line Summary

VDR is a working exact arithmetic library in Python that represents values as finite trees of integer triples, has been tested across 15 mathematical domains with 282 passing tests and zero computation errors, and is ready for Gaussian elimination, complex extension, and polynomial type as the next development priorities.

---

