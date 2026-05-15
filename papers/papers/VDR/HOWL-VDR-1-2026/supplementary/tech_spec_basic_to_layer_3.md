# VDR Technical Specification v1.0

## 1. System Identity

VDR is an exact arithmetic system implemented as a Python library. It represents all values as finite trees of integer triples. There are no floats, no decimals, no limits, no epsilon tests, and no infinity inside the system. Every operation either returns an exact finite result or fails explicitly.

The system replaces approximation-dominant scalar arithmetic with structure-preserving exact computation. It extends beyond rational arithmetic through functional remainders — Python callables embedded in the remainder slot that produce exact structure on demand through recursion, not limits.

The implementation target is Python 3.8+ with no required external dependencies beyond the standard library. mpmath is optional, used only at the lossy decimal export boundary.

## 2. The Triple

The primitive object is an ordered triple:

```
[V, D, R]
```

**V (value slot):** An arbitrary-precision Python integer. The settled numerator component in the current denominator frame.

**D (denominator slot):** A nonzero arbitrary-precision Python integer. The frame in which V and R are interpreted. Negative denominators are valid in raw form. Normalization enforces positive D as a canonicality convention, not a validity requirement.

**R (remainder slot):** One of three forms:

1. **Atomic remainder:** A single integer. Represented internally as `Remainder(base=r, children=[])`.

2. **Composite remainder:** An integer base plus a finite ordered list of child VDR triples. Represented as `Remainder(base=r, children=[X₁, X₂, ..., Xₙ])`. This is the structural form `r + X₁ + X₂ + ... + Xₙ` where each Xᵢ is a valid VDR object.

3. **Functional remainder:** A Python callable that accepts an integer depth parameter and returns a VDR object, plus a name string for inspectability. Represented as `FnRemainder(func, name)`. The callable is finite (it has finite source code). The VDR it produces at any depth is finite and exact. This form enables recursion-as-value without limits.

Recursion exists only in R. V and D are always atomic integers. The tree always branches through R and only through R. Every valid object is a finite tree (or, for functional remainders, a finite specification that produces finite trees on demand).

## 3. Construction

```python
from vdr import VDR, Remainder, FnRemainder

# From integers
VDR(5)                    # [5, 1, 0]
VDR(-3)                   # [-3, 1, 0]

# From rational components
VDR(1, 2)                 # [1, 2, 0]  →  1/2
VDR(22, 7)                # [22, 7, 0] →  22/7

# With atomic remainder
VDR(2, 5, 1)              # [2, 5, 1]  active object

# With composite remainder
VDR(1, 3, Remainder(0, [VDR(1, 6)]))   # [1, 3, [1, 6, 0]]

# From fractions.Fraction
from fractions import Fraction
VDR.from_fraction(Fraction(7, 11))      # [7, 11, 0]

# With functional remainder
fn = FnRemainder(lambda depth: VDR(depth + 1, depth + 2), name="ratio")
VDR(0, 1, fn)             # [0, 1, fn:ratio]
```

Construction validates on creation. Zero denominator raises `ZeroDenominatorError`. Non-integer V or D raises `InvalidStructureError`. Invalid remainder types raise `InvalidStructureError`.

## 4. Validity

A VDR object is valid if and only if:

- It has exactly three slots
- V is a Python int
- D is a nonzero Python int
- R is a valid Remainder (atomic, composite with valid VDR children, or functional with a callable)
- Every child VDR in a composite remainder is itself valid
- The full recursive expansion of any concrete (non-functional) tree is finite: finite depth, finite branching at every node, finite total node count
- The object is exact as written — no hidden continuation, no deferred tail, no limit interpretation

Validity is enforced at construction time. Invalid objects cannot be created through the public API.

## 5. Closed vs Active

**Closed:** `[V, D, 0]` — the remainder is zero at the top level. Projects to V/D as an exact rational.

**Globally closed:** The remainder is zero at every level of the recursive tree. No descendant carries unresolved state.

**Active:** `[V, D, R]` with R ≠ 0 — the object carries exact residual state. Under the system's semantics, `[2, 5, 1]` is not the same object as `[3, 5, 0]`. The remainder is meaningful native state, not a delayed simplification.

**Functional:** `[V, D, fn]` — the remainder is a callable. The object cannot be projected to a scalar until the function is expanded via `resolve(obj, depth)`. Functional objects are a subclass of active objects.

```python
x = VDR(1, 2)          # x.is_closed → True
y = VDR(2, 5, 1)       # y.is_active → True, y.is_closed → False
z = VDR(0, 1, fn)      # is_functional(z) → True
```

## 6. Equality

Three equality relations exist in the system.

**Structural equality (≡ₛ):** Two objects are structurally equal when every slot matches exactly, recursively and in order. This is identity of representation. Tested via `x.structural_eq(y)`.

**Normalized value equality (≡ₙ):** Two objects are normalized-value equal when their normalized forms are structurally equal. This captures the idea that `[2, 4, 0]` and `[1, 2, 0]` represent the same canonical object. Tested via `x.value_eq(y)` or `x == y`.

For closed objects, value equality can also be checked by cross-multiplication: `[V₁, D₁, 0]` equals `[V₂, D₂, 0]` when `V₁·D₂ = V₂·D₁`.

**Functional equality:** Two functional remainders are structurally equal only if they wrap the same callable object and share the same name. Semantic equality of functions (do they produce the same output?) is undecidable in general and is not attempted. Expand first, then compare the concrete results.

Python's `==` operator uses normalized value equality. Python's `hash()` uses the normalized form, so VDR objects work correctly as dict keys and set members.

```python
VDR(2, 4) == VDR(1, 2)              # True  (value equal)
VDR(2, 4).structural_eq(VDR(1, 2))  # False (different raw form)
VDR(2, 5, 1) == VDR(3, 5)           # False (active ≠ closed)
```

## 7. Normalization

Normalization transforms a valid object into a canonical form without changing its value. Applied by `x.normalize()`. Required for equality testing, serialization, and reproducible computation. Not required for an object to exist.

The normalization procedure, applied recursively bottom-up:

**Sign placement:** D is made positive. If D < 0, negate both V and D.

**GCD reduction on closed nodes:** For `[V, D, 0]`, divide both V and D by `gcd(|V|, |D|)`. For active nodes, GCD reduction applies only if the remainder structure is cleanly divisible by the same factor (checked recursively).

**Atomic remainder consolidation:** At each remainder level, all integer contributions are summed into a single integer base.

**Child normalization:** Every child is normalized before the parent.

**Canonical child ordering:** Immediate remainder children are sorted by `(|D|, D, V, R.base)`.

**Same-denominator child merge:** Globally closed children sharing the same denominator magnitude are added together via closed arithmetic. If the sum is zero, the child is dropped.

**D=1 child absorption:** Globally closed children with D=1 are absorbed into the atomic base of the parent remainder.

**Zero-value child elimination:** Children that are globally closed with V=0 are removed.

**Closed-form preference:** If the entire remainder (including all descendants) normalizes to zero, the object settles to a closed form.

Normalization is deterministic, finite, and idempotent. `normalize(normalize(x))` produces the same result as `normalize(x)`.

## 8. Scalar Projection

Projection maps a VDR object outward into a rational or decimal value. It is external and secondary. It does not define what the object is inside VDR.

**Closed projection:** For `[V, D, 0]`, the scalar projection is `Fraction(V, D)`. Exact and lossless.

**Legacy conversion (additive flattening):** For active objects with concrete (non-functional) remainders:

```
legacy([V, D, 0]) = V/D
legacy([V, D, R]) = V/D + legacy(R)/D
legacy(r) = r                                    (atomic remainder)
legacy(r + X₁ + ... + Xₙ) = r + Σ legacy(Xᵢ)    (composite remainder)
```

Under denominator-sensitive completion semantics, the remainder contributes within the parent's denominator frame. The external comparison schema is:

```
Π([V, D, R]) = (V + ρ_D(R)) / D
```

where ρ_D(R) interprets the remainder as numerator-side completion relative to parent denominator D.

**Functional projection:** Blocked. Calling `to_fraction()` on a VDR with a functional remainder raises `VDRError`. The function must be expanded via `resolve(obj, depth)` first, producing a concrete VDR that can then be projected.

**Lossy export:** `to_float()` returns a Python float (64-bit IEEE 754). `to_decimal(x, digits)` renders to a decimal string at the requested precision using mpmath if available, or manual long division as fallback. Loss belongs to the target format, not to VDR.

```python
x = VDR(1, 7)
x.to_fraction()        # Fraction(1, 7) — exact
float(x)               # 0.14285714285714285 — lossy
to_decimal(x, 50)      # "0.14285714285714285714285714285714285714285714285714" — lossy
```

## 9. Closed Arithmetic

Operates on `[V, D, 0]` objects and produces `[V', D', 0]` results. Standard exact rational arithmetic in triple form. All results are normalized after computation.

**Addition:** `[V₁, D₁, 0] + [V₂, D₂, 0] = [V₁·D₂ + V₂·D₁, D₁·D₂, 0]`

**Subtraction:** `[V₁, D₁, 0] - [V₂, D₂, 0] = [V₁·D₂ - V₂·D₁, D₁·D₂, 0]`

**Multiplication:** `[V₁, D₁, 0] × [V₂, D₂, 0] = [V₁·V₂, D₁·D₂, 0]`

**Division:** `[V₁, D₁, 0] ÷ [V₂, D₂, 0] = [V₁·D₂, D₁·V₂, 0]` (V₂ ≠ 0)

Division by `[0, D, 0]` raises `ArithmeticFailure`.

The closed subclass is arithmetically closed under these operations. It satisfies commutativity, associativity, and distributivity under value equality. Additive identity: `[0, 1, 0]`. Multiplicative identity: `[1, 1, 0]`. Additive inverse of `[V, D, 0]` is `[-V, D, 0]`.

Under closed projection, all operations agree exactly with `fractions.Fraction` arithmetic.

```python
VDR(1, 2) + VDR(1, 3)   # [5, 6, 0]
VDR(2, 3) * VDR(3, 5)   # [2, 5, 0]
VDR(2, 3) / VDR(4, 5)   # [5, 6, 0]
```

## 10. Active Arithmetic

### Same-Denominator Addition and Subtraction

When two VDR objects share a denominator:

```
[V₁, D, R₁] + [V₂, D, R₂] = [V₁ + V₂, D, R₁ ⊕ R₂]
[V₁, D, R₁] - [V₂, D, R₂] = [V₁ - V₂, D, R₁ ⊖ R₂]
```

where ⊕ combines remainder structures (sum atomic bases, concatenate child lists) and ⊖ subtracts bases and appends negated children. Results are normalized.

### Different-Denominator Addition and Subtraction

Cross-scaled to a shared frame `D₁·D₂`, with remainder transport via lift:

```
[V₁, D₁, R₁] + [V₂, D₂, R₂] = [V₁·D₂ + V₂·D₁, D₁·D₂, lift(R₁, D₂) + lift(R₂, D₁)]
```

### Remainder Negation

Recursive:

```
-(r) = -r
-(r + X₁ + ... + Xₙ) = -r + (-X₁) + ... + (-Xₙ)
-[V, D, R] = [-V, D, -R]
```

### Active Multiplication

For `[V₁, D₁, R₁] × [V₂, D₂, R₂]`, the product is constructed in denominator frame `D₁·D₂` with closed numerator `V₁·V₂`. The remainder captures three cross-term contributions:

1. **Left cross:** V₁ scales the second operand's remainder → `V₁ · R₂`
2. **Right cross:** V₂ scales the first operand's remainder → `V₂ · R₁`
3. **Remainder cross:** Both remainders interact → `R₁ · R₂` (computed via legacy projection of both remainders, then expressed as VDR remainder structure)

Scaling a remainder by integer k: multiply the base by k, and for each child `[V, D, R]` produce `[kV, D, scaled(R, k)]`.

The remainder cross-product is computed by projecting both remainders to exact Fraction, multiplying, and expressing the result as either an atomic integer (if the product is integer) or a closed child VDR (if rational).

All results are normalized. Commutativity, associativity, and distributivity hold under projection. Verified by the test suite across mixed active/closed operand combinations.

### Active Division

Division by a closed object with V ≠ 0 is multiplication by `[D₂, V₂, 0]`. Division by an active object goes through the projection boundary: the divisor is projected to an exact Fraction, inverted, and the quotient is computed via active multiplication. The projected value is exact (no precision loss), but the divisor's structural remainder information is not preserved in the result. This is the v1 compromise. Division by any object projecting to zero raises `ArithmeticFailure`.

```python
VDR(2, 5, 1) * VDR(3, 7, -1)    # projects to 6/35 — exact
VDR(2, 5, 1) / VDR(1, 3, 1)     # projects to 9/10 — exact via projection
```

## 11. Lift

Lift is the remainder transport operator. When a parent's denominator frame is scaled by factor k, lift rewrites the remainder so it contributes correctly in the new frame.

```
lift(r, k)                           = k · r
lift(r + X₁ + ... + Xₙ, k)          = k·r + lift(X₁, k) + ... + lift(Xₙ, k)
lift([V, D, R], k)                   = [k·V, D, lift(R, k)]
lift(FnRemainder(f, name), k)        = FnRemainder(λ depth: f(depth)._lift_vdr(k))
```

The critical design: lift scales V and R of a child but does not touch the child's D. The child keeps its own internal denominator identity. The numerator and remainder absorb the outer frame scaling.

Properties: identity at k=1, negation at k=-1, multiplicative composition `lift(lift(R,a),b) = lift(R,ab)`, distributes over remainder addition, preserves zero, preserves validity.

Lift by zero is invalid and raises `VDRError`.

## 12. Rebase

Rebase changes the top-level denominator of a VDR object while preserving exact value.

**Closed rebase:** For `[V, D, 0]` and target B, succeeds when `V·B/D` is an integer. Result: `[V·B/D, B, 0]`. Fails otherwise.

**Active rebase:** When closed rebase fails, active rebase constructs:

```
N = V · B
N = Q · D + S          (integer division)

rebase([V, D, R], B) = [Q, B, [S, D, 0] + lift(R, B)]
```

The mismatch witness `[S, D, 0]` captures the exact denominator mismatch. `lift(R, B)` transports existing remainder into the new frame. If S = 0 and the lifted remainder resolves to zero, the result collapses to a closed form.

**Same-denominator rebase:** Identity — `rebase(x, x.d)` returns x unchanged.

Rebase preserves value equality, not structural equality. It is deterministic, finite, and exact.

```python
x = VDR(1, 2)
x.rebase(3)    # [1, 3, [1, 2, 0]] — projects to 1/2
x.rebase(4)    # [2, 4, 0] → normalizes to [1, 2, 0]
```

## 13. Functional Remainders

A functional remainder is a Python callable embedded in the R slot. It replaces limits with recursion.

### Construction

```python
from vdr import FnRemainder, make_newton_fn, make_series_fn

# Direct construction
fn = FnRemainder(lambda depth: VDR(depth + 1, depth + 2), name="ratio")
obj = VDR(0, 1, fn)

# Newton-Raphson factory
sqrt2_fn = make_newton_fn("sqrt2", lambda x: (x + VDR(2) / x) / VDR(2))
sqrt2 = VDR(0, 1, sqrt2_fn)

# Series factory
def leibniz_term(n):
    sign = 1 if n % 2 == 0 else -1
    return VDR(sign, 2 * n + 1)
pi4_fn = make_series_fn("leibniz_pi4", leibniz_term)
pi4 = VDR(0, 1, pi4_fn)

# Iterative factory
halving = make_iterative_fn("halving", lambda x: x / VDR(2), VDR(1024))
```

### Expansion

```python
from vdr import resolve, resolve_recursive

resolved = resolve(sqrt2, depth=7)    # 7 Newton steps, exact rational
print(resolved.to_fraction())         # exact fraction ≈ √2

# Recursive resolution of nested functional VDR trees
resolved = resolve_recursive(nested_obj, depth=5)
```

`resolve(obj, depth)` expands the functional remainder at the given depth. The result is a concrete VDR object with no functional remainders at the top level. If the parent frame is `[0, 1, fn]`, the expanded VDR replaces the object entirely. If the parent frame is non-trivial (V ≠ 0 or D ≠ 1), the expanded VDR becomes a child in the parent's remainder.

`resolve_recursive(obj, depth)` resolves all functional remainders at every level of the tree.

### Semantics

A functional remainder is exact at every finite depth of expansion. Depth 0 produces one exact result. Depth N produces another exact result. Neither is an approximation — each is a complete exact VDR object. The function is a recursive specification, not a convergent series.

Functional remainders cannot be projected to scalars without expansion. Calling `to_fraction()` on a functional VDR raises an error. This is by design — projection requires a concrete structure, and the function must be expanded to a chosen depth first.

Functional remainders support negation (negate the output), lift (scale the output), and combination (compose two functions with addition or subtraction).

### Demonstrated Capabilities

**Newton-Raphson for √2:** At depth 7, produces a fraction with >100 correct digits of √2. Every intermediate step is an exact VDR rational. The squared result differs from 2 by a fraction with a 97-digit denominator. No floats used anywhere in the computation.

**Leibniz series for π/4:** Each partial sum is an exact VDR rational. 101 terms produce π accurate to ~2 decimal places (Leibniz converges slowly). The exact fraction at 101 terms has a 250+ digit numerator and denominator — fully exact, not rounded.

**Basel problem for π²/6:** Exact rational partial sums of 1/n². 101 terms give π accurate to ~1.5 decimal places. Every partial sum is a single exact VDR fraction.

## 14. Discrete Calculus

VDR replaces limits with exact discrete operations. Every evaluation is exact VDR arithmetic. No limit process is used or needed.

### Discrete Derivative

```python
from vdr import discrete_derivative, discrete_derivative_nth

f = lambda x: x * x
df = discrete_derivative(f, VDR(1, 1000))

df(VDR(3))    # exactly 6001/1000 — not a float approximation
```

The discrete derivative of f at x with step size h is:

```
Df(x) = (f(x + h) - f(x)) / h
```

Every term is exact VDR rational arithmetic. The result is exact at the given step size, not an approximation of the analytical derivative. Smaller h gives a result closer to the analytical derivative, but every h gives an exact answer.

Higher-order derivatives by repeated application:

```python
ddf = discrete_derivative_nth(f_x3, VDR(1, 100), order=2)
ddf(VDR(2))   # exact second derivative of x³ at x=2
```

### Discrete Integral

```python
from vdr import discrete_integral, discrete_integral_trapz

# Left Riemann sum — every term exact
result = discrete_integral(lambda x: x*x, VDR(0), VDR(1), 100)

# Trapezoidal rule — more accurate, still exact
result = discrete_integral_trapz(lambda x: x*x, VDR(0), VDR(1), 100)
```

Left Riemann sum: `Σ f(a + k·h) · h` for k = 0 to n-1, where h = (b-a)/n.

Trapezoidal rule: `h/2 · (f(a) + 2·Σf(a+k·h) + f(b))`.

Every term in both sums is exact VDR arithmetic. Increasing n gives finer resolution. Each n gives a fully exact rational answer. The integral of x² from 0 to 1 with n=10 is exactly `57/200`, not `0.285`.

### Finite Difference Table

Exact finite difference tables over VDR-valued functions. Third differences of x³ are exactly 6 at every point. Fourth differences are exactly 0. No floating-point noise. No accumulated error. Exact structural identity.

## 15. Linear Algebra

Exact rational linear algebra over VDR objects. Every operation uses exact VDR arithmetic. Zero drift across any chain of operations.

### Vectors

```python
from vdr import Vec

v = Vec([VDR(1, 2), VDR(1, 3), VDR(1, 7)])
w = Vec.from_ints([1, 2, 3])
z = Vec.zero(3)

v + w          # element-wise exact addition
v - w          # element-wise exact subtraction
v * VDR(2)     # exact scalar multiplication
v.dot(w)       # exact dot product
-v             # exact negation
```

### Matrices

```python
from vdr import Mat

m = Mat.from_ints([[1, 2], [3, 4]])
I = Mat.identity(2)

m + n          # element-wise exact addition
m - n          # element-wise exact subtraction
m * n          # exact matrix multiplication (Σ aᵢₖ·bₖⱼ)
m * v          # exact matrix-vector product
m * VDR(1, 2)  # exact scalar multiplication
m.T            # transpose
m.det()        # exact determinant (cofactor expansion)
m.inv()        # exact inverse (adjugate/determinant method)
m.trace()      # exact trace
m.rank()       # exact rank (Gaussian elimination)
m.solve(b)     # exact solve via Cramer's rule
```

### Exact Matrix Inverse

The inverse is computed via the adjugate method: `A⁻¹ = adj(A) / det(A)`. Every element of the cofactor matrix is an exact VDR determinant. The final division is exact VDR division. The result is exactly correct — `A × A⁻¹` produces exactly the identity matrix with no rounding error.

### Demonstrated Capability: Hilbert Matrix

The 4×4 Hilbert matrix H[i,j] = 1/(i+j+1) is notoriously ill-conditioned. Float systems lose all precision on inversion. VDR inverts it exactly:

- `H × H⁻¹ = I` — exactly, every element
- `inv(inv(H)) = H` — exactly, every element
- 40 matrix operations (multiply by B, multiply by B⁻¹, repeated 20 times) produce exactly the original matrix

No float system can do this. This is the practical demonstration that VDR matters.

## 16. Parsing and Serialization

### Bracket Notation Parser

```python
from vdr import parse_vdr

parse_vdr("[1, 2, 0]")                    # VDR(1, 2)
parse_vdr("[1, 3, [1, 6, 0]]")            # VDR with child remainder
parse_vdr("[2, 5, 1 + [1, 3, 0] + [1, 7, 0]]")  # composite remainder
```

### JSON Serialization

```python
from vdr import vdr_to_dict, vdr_from_dict
import json

d = vdr_to_dict(x)        # VDR → dict
j = json.dumps(d)         # dict → JSON string
x2 = vdr_from_dict(json.loads(j))  # JSON string → VDR
x.structural_eq(x2)       # True — lossless roundtrip
```

Format:
```json
{
  "v": 1,
  "d": 3,
  "r": {
    "base": 0,
    "children": [{"v": 1, "d": 6, "r": {"base": 0, "children": []}}]
  }
}
```

### LaTeX Export

```python
from vdr import vdr_to_latex

vdr_to_latex(VDR(1, 2))    # "\\frac{1}{2}"
vdr_to_latex(VDR(5))        # "5"
```

Active objects render the remainder in braces: `\frac{1}{3}\left\{\frac{1}{6}\right\}`.

## 17. Structural Metrics

Three metrics characterize the structural complexity of a VDR object.

**Depth:** Maximum nesting depth of the tree. `depth([V,D,0]) = 0`. A single-child active object has depth 1.

**Structural size:** Counts one unit per VDR node plus one unit per atomic remainder base. Independent of numeric magnitude. `size([V,D,0]) = 2` for all closed objects regardless of how large V and D are.

**Denominator complexity:** A tuple `(u, s, m)` where u is the number of distinct denominator magnitudes in the tree, s is the sum of all |D| values, and m is the total count of denominator-bearing nodes. Compared lexicographically. Rewards denominator unification over raw smallness.

```python
x = VDR(1, 2).rebase(3)
x.depth()            # 1
x.size()             # 4
x.den_complexity()   # (2, 5, 2)
```

## 18. Module Architecture

```
vdr/
  __init__.py        # Public API, auto-installs active_mul and fn
  vdr.py             # Core: VDR, Remainder, validation, normalization,
                     #   equality, closed arithmetic, rebase, lift, projection
  active_mul.py      # Active multiplication and division, patches VDR operators
  fn.py              # FnRemainder, resolve, factories, discrete calculus
  linalg.py          # Vec, Mat, parse_vdr, JSON serialization, LaTeX export
  export.py          # to_decimal, to_float, to_fraction (lossy boundary)
```

`vdr/__init__.py` imports the public API from all modules and auto-installs the operator patches. User code needs only:

```python
from vdr import VDR, Vec, Mat, resolve, discrete_derivative, discrete_integral
```

## 19. Error Handling

All errors inherit from `VDRError`. Failure is a first-class outcome, not a silent degradation.

- `ZeroDenominatorError` — D = 0 in construction or operation result
- `InvalidStructureError` — wrong types in slots, invalid remainder structure
- `RebaseError` — invalid target denominator or rebase impossible
- `ArithmeticFailure` — division by zero, unsupported operation

No operation silently approximates. No operation silently truncates. No operation silently drops remainder structure. If exact finite representation is impossible, the operation raises.

## 20. Operator Overloading

VDR objects support Python arithmetic operators:

```
+   -   *   /   ==   !=   <   <=   >   >=   -x   +x   abs(x)   float(x)   hash(x)
```

`==` uses normalized value equality. Comparison operators (`<`, `<=`, `>`, `>=`) use projection to Fraction, which means they go through the legacy flattening boundary for active objects and raise for functional objects.

Operators accept VDR, int, and Fraction on both sides via coercion.

## 21. Invariants

Every conforming operation preserves:

1. Every object has exactly three slots
2. D is never zero
3. Recursion occurs only through R
4. Every concrete object is finite
5. Every operation returns exact finite result or explicit failure
6. Normalization never leaves the VDR domain
7. Structural equality is exact recursive equality
8. Scalar projection does not redefine native identity
9. No approximation enters any native operation
10. Lift does not alter child denominators
11. Rebase preserves value equality
12. Closed arithmetic agrees with rational arithmetic under projection
13. Functional remainders block projection until resolved
14. Active multiplication preserves projection compatibility

## 22. Demonstrated Performance

The test suite verifies:

- **Zero drift:** 200 add/subtract operations on VDR(1, 7) with step VDR(1, 13) returns exactly to origin
- **Matrix roundtrip:** 40 matrix multiply/inverse operations return exactly to the original matrix
- **Hilbert matrix:** 4×4 Hilbert matrix inverted exactly, `H × H⁻¹ = I` exactly, `inv(inv(H)) = H` exactly
- **Newton-Raphson √2:** >100 correct digits at depth 7, every step exact rational
- **Discrete integral:** ∫₀¹ x² dx with n=10 gives exactly 57/200
- **Finite differences:** Δ³(x³) = 6 exactly everywhere, Δ⁴(x³) = 0 exactly everywhere
- **Active arithmetic:** Commutativity, associativity, and distributivity verified across mixed active/closed operands

## 23. Current Boundaries

**Working:** Exact rational arithmetic, active add/sub/mul/div, linear algebra (vectors, matrices, determinant, inverse, solve, rank), rebase, lift, functional remainders, Newton-Raphson iteration, series summation, discrete derivative, discrete integral, parsing, JSON serialization, LaTeX export, decimal export.

**Not yet implemented:** Eigenvalue/eigenvector computation (requires irrational/complex support). Complex number type. Symbolic polynomial representation in remainder slot. Optimized algorithms for large matrices (current determinant is O(n!) cofactor expansion). Active rebase with pre-existing remainder (first-pass rule exists, full correctness requires case-by-case verification for non-rational domains).

**By design excluded:** Limits. Epsilon-delta reasoning. Infinite structures. Approximation as a native operation. Silent precision loss. Hidden rounding. Convergence criteria as acceptance tests.

## 24. Dependencies

**Required:** Python 3.8+ standard library (`fractions`, `math`, `typing`).

**Optional:** `mpmath` for arbitrary-precision decimal export via `to_decimal()`. Without mpmath, decimal export falls back to manual long division from Fraction.

No numpy. No sympy. No heavy dependencies.
