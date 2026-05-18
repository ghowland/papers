# vdr-math Module Function & Global Specification

## Convention Key

**IOSE** = Input, Output, Side-effects, Errors
**Globals** = module-level constants available on import
**All functions operate on VDR unless noted. All outputs are exact.**

---

## 1. `vdr.core`

### Globals

```python
ZERO = VDR(0, 1)        # additive identity
ONE = VDR(1, 1)          # multiplicative identity
NEG_ONE = VDR(-1, 1)
```

### Classes

**`Remainder(base: int, children: list[VDR] = [])`**

| Method | Input | Output | Errors |
|---|---|---|---|
| `is_zero` | — | bool | — |
| `is_atomic` | — | bool | — |
| `is_globally_zero` | — | bool (recursive) | — |
| `structural_eq(other)` | Remainder | bool | — |
| `negate()` | — | Remainder | — |
| `combine(other, sign=1)` | Remainder, ±1 | Remainder | — |
| `lift(k)` | int (nonzero) | Remainder | VDRError if k=0 |
| `legacy_value()` | — | Fraction | — |
| `normalize()` | — | Remainder | — |

**`VDR(v: int, d: int = 1, r: Remainder | int | None = None)`**

| Method | Input | Output | Errors |
|---|---|---|---|
| `is_closed` | — | bool | — |
| `is_active` | — | bool | — |
| `is_globally_closed` | — | bool | — |
| `structural_eq(other)` | VDR | bool | — |
| `value_eq(other)` | VDR | bool | — |
| `normalize()` | — | VDR (canonical) | — |
| `to_fraction()` | — | Fraction | VDRError if functional R |
| `to_float()` | — | float (lossy) | — |
| `rebase(target_d)` | int (nonzero) | VDR | RebaseError |
| `negate()` | — | VDR | — |
| `depth()` | — | int | — |
| `size()` | — | int | — |
| `den_complexity()` | — | tuple(int,int,int) | — |
| `bracket()` | — | str | — |
| `from_fraction(frac)` | Fraction | VDR (classmethod) | — |
| `from_int(n)` | int | VDR (classmethod) | — |

**Operators:** `+`, `-`, `*`, `/`, `-x`, `+x`, `abs(x)`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `hash`, `float`, `__repr__`, `__str__`

**Normalization rules (in order):**
1. Sign convention (D > 0)
2. GCD reduction on V, D
3. Child normalization (bottom-up)
4. Atomic remainder consolidation
5. Canonical child ordering (|D| asc, V asc, R structure)
6. Same-denominator child merge
7. Closed-form preference (N7): if R value-equivalent to zero, collapse and GCD-reduce
8. **NEW:** unconditional GCD-reduce when R is zero after collapse (fixes Newton perfect-square issue)

---

## 2. `vdr.active`

### Functions

**`active_mul(a: VDR, b: VDR) -> VDR`**
- I: two VDR objects, either or both may be active
- O: exact product. Frame D₁·D₂, closed part V₁·V₂, cross-terms V₁·R₂ + V₂·R₁ + R₁·R₂ in remainder
- S: none
- E: ArithmeticFailure on structural impossibility

**`active_div(a: VDR, b: VDR) -> VDR`**
- I: two VDR objects, b nonzero
- O: exact quotient. By closed: multiply by reciprocal. By active: project divisor, invert, multiply (v1 compromise — divisor R structure lost)
- S: none
- E: ArithmeticFailure if divisor is zero

**`install()`**
- I: none
- O: none
- S: patches VDR `__mul__`, `__rmul__`, `__truediv__`, `__rtruediv__`
- E: none

**`uninstall()`**
- I: none
- O: none
- S: restores original VDR operators
- E: none

---

## 3. `vdr.fn`

### Classes

**`FnRemainder(func: Callable[[int], VDR], name: str = None, meta: dict = None)`**
- Subclass of Remainder
- `expand(depth)` → VDR
- `is_zero` → always False
- `is_functional` → always True
- `negate()` → FnRemainder wrapping negated call
- `lift(k)` → FnRemainder wrapping lifted call
- `combine(other, sign)` → FnRemainder if both functional, else hybrid

### Functions

**`resolve(x: VDR, depth: int = 1) -> VDR`**
- I: VDR with possibly functional R, depth ≥ 0
- O: concrete VDR with R expanded at given depth
- S: none
- E: VDRError if depth < 0 or func returns non-VDR

**`resolve_recursive(x: VDR, depth: int = 1) -> VDR`**
- I: VDR tree with possibly multiple functional Rs
- O: fully resolved concrete VDR
- S: none
- E: same as resolve

**`is_functional(x: VDR) -> bool`**

**`make_newton_fn(name: str, step_fn: Callable[[VDR], VDR], start: VDR = VDR(1)) -> FnRemainder`**
- I: name, iteration function, starting value
- O: FnRemainder. At depth N applies step_fn N times to start
- Quadratic convergence: digits double per step

**`make_series_fn(name: str, term_fn: Callable[[int], VDR], initial: VDR = VDR(0)) -> FnRemainder`**
- I: name, term function, optional initial sum
- O: FnRemainder. At depth N returns sum of terms 0..N plus initial

**`make_iterative_fn(name: str, step: Callable[[VDR], VDR], start: VDR) -> FnRemainder`**
- I: name, step function, starting value
- O: FnRemainder. General iteration

**`make_constant_fn(name: str, value_func: Callable[[], VDR]) -> FnRemainder`**

**`discrete_derivative(f: Callable, h: VDR) -> Callable`**
- I: function VDR→VDR, step size h
- O: function computing Dₕf(x) = (f(x+h) − f(x))/h

**`discrete_derivative_nth(f: Callable, h: VDR, order: int = 1) -> Callable`**

**`discrete_integral(f: Callable, a: VDR, b: VDR, n: int) -> VDR`**
- Left Riemann sum, exact

**`discrete_integral_trapz(f: Callable, a: VDR, b: VDR, n: int) -> VDR`**
- Trapezoidal rule, exact

**`@vdr_fn(name: str)` decorator**

**`install()` / `uninstall()`**
- Patches VDR `is_closed`, `is_active`, `to_fraction` for FnRemainder awareness

---

## 4. `vdr.linalg`

### Classes

**`Vec(data: list[VDR | int])`**

| Method | Input | Output | Notes |
|---|---|---|---|
| `from_ints(ns)` | list[int] | Vec | classmethod |
| `from_fracs(pairs)` | list[tuple] | Vec | classmethod |
| `zero(n)` | int | Vec | classmethod |
| `dim` | — | int | property |
| `__add__`, `__sub__` | Vec | Vec | same dim required |
| `__neg__` | — | Vec | — |
| `scale(s)` / `__mul__` | VDR or int | Vec | — |
| `dot(other)` | Vec | VDR | exact |
| `norm_sq()` | — | VDR | v·v, no sqrt |
| `to_fractions()` | — | list[Fraction] | — |

**`Mat(rows: list[list | Vec])`**

| Method | Input | Output | Notes |
|---|---|---|---|
| `from_ints`, `from_fracs` | nested lists | Mat | classmethod |
| `identity(n)`, `zero(nr,nc)` | int(s) | Mat | classmethod |
| `nrows`, `ncols`, `shape`, `is_square` | — | int/tuple/bool | properties |
| `row(i)`, `col(j)` | int | Vec | — |
| `__add__`, `__sub__`, `__neg__` | Mat | Mat | same shape |
| `scale(s)` | VDR or int | Mat | — |
| `matmul(other)` | Mat | Mat | compatible shapes |
| `matvec(v)` | Vec | Vec | — |
| `T` | — | Mat | transpose, property |
| `trace()` | — | VDR | square required |
| `det()` | — | VDR | dispatches: cofactor ≤4, Gaussian ≥5 |
| `det_cofactor()` | — | VDR | O(n!) explicit |
| `det_gauss()` | — | VDR | O(n³) |
| `inv()` | — | Mat | dispatches similarly |
| `inv_adjugate()` | — | Mat | via adj/det |
| `inv_gauss()` | — | Mat | via Gaussian |
| `solve(b)` | Vec | Vec | dispatches |
| `solve_cramer(b)` | Vec | Vec | explicit |
| `solve_gauss(b)` | Vec | Vec | O(n³) |
| `rank()` | — | int | Gaussian, exact |
| `rref()` | — | Mat | reduced row echelon |
| `pretty()` | — | str | formatted display |
| `to_fractions()` | — | list[list[Fraction]] | — |

### Functions

**`parse_vdr(text: str) -> VDR`** — bracket notation parser

**`vdr_to_dict(x) -> dict`** / **`vdr_from_dict(d) -> VDR`** — JSON serialization

**`vdr_to_latex(x) -> str`** — LaTeX export

---

## 5. `vdr.export`

### Functions

**`to_fraction(x: VDR) -> Fraction`**
- Exact for closed. Legacy-flattened for active. Error on functional.

**`to_float(x: VDR) -> float`**
- Lossy. Loss belongs to target format.

**`to_decimal(x: VDR, digits: int = 50) -> str`**
- Uses mpmath if available, manual long division otherwise.

---

## 6. `vdr.basis`

### Globals

```python
DEFAULT_BITS = 335
Q335 = 2 ** 335    # the default denominator frame
```

### Functions

**`set_default(bits: int)`**
- I: bit width
- O: none
- S: sets module-level DEFAULT_BITS
- E: ValueError if bits < 1

**`get_default() -> int`**
- Returns current DEFAULT_BITS

**`q_basis_denominator(bits: int = None) -> int`**
- I: optional bits (uses DEFAULT_BITS if None)
- O: 2**bits as Python int

**`to_qbasis(x, bits: int = None) -> VDR`**
- I: VDR, int, float, or Fraction; optional bits
- O: VDR as [round(x × 2^bits), 2^bits, 0]

**`vec_to_qbasis(v: Vec, bits: int = None) -> Vec`**

**`mat_to_qbasis(m: Mat, bits: int = None) -> Mat`**

**`qb_add(a: VDR, b: VDR, bits: int = None) -> VDR`**
- Addition staying in basis frame

**`qb_mul(a: VDR, b: VDR, bits: int = None) -> VDR`**
- Multiplication with divmod. D stays 2^bits. Overflow in R. Zero loss.

**`qb_div(a: VDR, b: VDR, bits: int = None) -> VDR`**
- Division with divmod back to basis frame

---

## 7. `vdr.math.number_theory`

### Globals

None (all computed on demand).

### Functions

**`vdr_gcd(a: VDR, b: VDR) -> VDR`**
- I: two closed VDR integers (D=1)
- O: GCD as VDR
- E: ValueError if not integer VDR

**`vdr_lcm(a: VDR, b: VDR) -> VDR`**

**`egyptian_fractions(v: int, d: int, max_terms: int = 20) -> list[VDR]`**
- I: fraction v/d, maximum unit fractions
- O: list of unit fractions [1/a₁, 1/a₂, ...] summing to v/d

**`stern_brocot(depth: int) -> list[VDR]`**
- I: tree depth
- O: ordered list of Stern-Brocot fractions at that depth

**`farey(n: int) -> list[VDR]`**
- I: order n
- O: Farey sequence F_n, all fractions p/q with 0 ≤ p/q ≤ 1 and q ≤ n

**`euler_totient(n: int) -> int`**
- I: positive integer
- O: φ(n)

**`harmonic(n: int) -> VDR`**
- I: positive integer
- O: H_n = 1 + 1/2 + ... + 1/n as exact VDR

**`vdr_pow(base: VDR, exp: int) -> VDR`**
- I: base VDR, non-negative integer exponent
- O: base^exp exact

**`vdr_mod(a: VDR, m: int) -> VDR`**
- I: integer VDR, modulus
- O: a mod m as VDR

**`convergents(cf_coeffs: list[int]) -> list[VDR]`**
- I: continued fraction coefficients
- O: list of convergents p_n/q_n as VDR

**`e_cf(n: int) -> list[int]`**
- I: number of CF coefficients
- O: first n coefficients of e = [2; 1, 2, 1, 1, 4, ...]

---

## 8. `vdr.math.polynomial`

### Functions

**`poly_eval(p: list[VDR], x: VDR) -> VDR`**
- I: coefficients [a₀, a₁, ...aₙ] (constant first), evaluation point
- O: p(x) via Horner, exact

**`poly_add(p: list[VDR], q: list[VDR]) -> list[VDR]`**

**`poly_sub(p: list[VDR], q: list[VDR]) -> list[VDR]`**

**`poly_mul(p: list[VDR], q: list[VDR]) -> list[VDR]`**

**`poly_scale(p: list[VDR], s: VDR) -> list[VDR]`**

**`poly_neg(p: list[VDR]) -> list[VDR]`**

**`poly_divmod(p: list[VDR], q: list[VDR]) -> tuple[list[VDR], list[VDR]]`**
- O: (quotient, remainder) polynomials

**`poly_gcd(p: list[VDR], q: list[VDR]) -> list[VDR]`**
- Euclidean algorithm. Exact zero-testing at each step.

**`poly_degree(p: list[VDR]) -> int`**

**`rational_roots(p: list[VDR]) -> list[VDR]`**
- Rational root theorem: test ±(factors of a₀)/(factors of aₙ)

**`lagrange_interpolate(points: list[tuple[VDR, VDR]]) -> list[VDR]`**
- I: list of (x, y) pairs
- O: unique interpolating polynomial coefficients

**`char_poly_2x2(m: Mat) -> list[VDR]`**
- I: 2×2 Mat
- O: characteristic polynomial coefficients

**`poly_derivative(p: list[VDR]) -> list[VDR]`**
- Symbolic differentiation

**`poly_integral(p: list[VDR], c: VDR = VDR(0)) -> list[VDR]`**
- Symbolic antiderivative with constant c

**`definite_integral(p: list[VDR], a: VDR, b: VDR) -> VDR`**
- Exact ∫_a^b p(x)dx via antiderivative evaluation

**`poly_str(p: list[VDR]) -> str`**
- Pretty-print polynomial

---

## 9. `vdr.math.continued_fractions`

### Functions

**`to_cf(v: int, d: int) -> list[int]`**
- I: fraction v/d
- O: continued fraction coefficients [a₀; a₁, a₂, ...]

**`from_cf(coeffs: list[int]) -> VDR`**
- I: CF coefficients
- O: rational as VDR

**`convergents_from_cf(coeffs: list[int]) -> list[VDR]`**
- O: list of convergent fractions

**`sb_path(p: int, q: int) -> str`**
- I: fraction p/q
- O: Stern-Brocot path string (e.g. "LRRL")

**`sqrt_cf_period(n: int) -> tuple[int, list[int]]`**
- I: non-square positive integer
- O: (integer part, periodic block) of √n CF

**`best_rational(x: VDR, max_denom: int) -> VDR`**
- I: target value, maximum denominator
- O: best rational approximation via CF convergents

---

## 10. `vdr.math.combinatorics`

### Functions

**`binom(n: int, k: int) -> VDR`** — C(n,k) exact

**`stirling2(n: int, k: int) -> VDR`** — Stirling numbers of second kind

**`bell(n: int) -> VDR`** — Bell numbers

**`derangement(n: int) -> VDR`** — D(n) subfactorials

**`catalan(n: int) -> VDR`** — Catalan numbers

**`catalan_gf(x: VDR, terms: int) -> VDR`** — generating function partial sum

**`multinomial(n: int, ks: list[int]) -> VDR`** — multinomial coefficient

**`factorial(n: int) -> VDR`** — n! as VDR

**`falling_factorial(n: VDR, k: int) -> VDR`** — n(n-1)...(n-k+1)

---

## 11. `vdr.math.sequences`

### Globals

```python
BERNOULLI_CACHE = {}  # populated on demand
```

### Functions

**`fibonacci(n: int) -> VDR`** — F(n) via matrix power or recursion

**`fibonacci_seq(n: int) -> list[VDR]`** — F(0) through F(n)

**`lucas(n: int) -> VDR`** — L(n)

**`lucas_seq(n: int) -> list[VDR]`**

**`catalan_seq(n: int) -> list[VDR]`**

**`bernoulli(n: int) -> VDR`**
- O: B_n exact. B₁₂ = VDR(-691, 2730). Cached.

**`tribonacci(n: int) -> VDR`**

**`tribonacci_seq(n: int) -> list[VDR]`**

**`rational_recurrence(coeffs: list[VDR], initial: list[VDR], n: int) -> list[VDR]`**
- I: recurrence coefficients, initial values, number of terms
- O: sequence through n terms

---

## 12. `vdr.math.probability`

### Functions

**`binom_pmf(n: int, k: int, p: VDR) -> VDR`**
- I: trials, successes, success probability
- O: P(X=k) exact. Sum over all k equals exactly 1.

**`binom_pmf_full(n: int, p: VDR) -> list[VDR]`**
- O: full PMF vector, sums to exactly 1

**`bayes_update(prior: VDR, likelihood_ratio: VDR) -> VDR`**
- I: prior probability, likelihood ratio
- O: posterior probability, exact

**`bayes_sequential(prior: VDR, likelihood_ratios: list[VDR]) -> list[VDR]`**
- O: list of posteriors after each update

**`markov_steady_state(transition: Mat) -> Vec`**
- I: row-stochastic transition matrix
- O: steady-state vector, sums to exactly 1. Via Cramer's rule or Gaussian.

**`gamblers_ruin(k: int, n: int) -> VDR`**
- I: starting capital k, total capital n (fair game)
- O: ruin probability P(k) = (N-k)/N exact

**`expected_value(values: list[VDR], probs: list[VDR]) -> VDR`**

**`variance(values: list[VDR], probs: list[VDR]) -> VDR`**

---

## 13. `vdr.math.symbolic`

### Functions

**`partial_fractions_simple(numerator: list[VDR], roots: list[VDR]) -> list[tuple[VDR, VDR]]`**
- I: numerator polynomial, list of denominator roots
- O: list of (coefficient, root) pairs: Σ cᵢ/(x - rᵢ)

**`ratfun_add(pq1: tuple, pq2: tuple) -> tuple`**
- I: two rational functions as (numerator_poly, denominator_poly)
- O: sum as rational function

**`ratfun_mul(pq1: tuple, pq2: tuple) -> tuple`**

**`ratfun_eval(pq: tuple, x: VDR) -> VDR`**

**`power_sum(k: int, n: int) -> VDR`**
- O: 1^k + 2^k + ... + n^k exact

---

## 14. `vdr.math.optimization`

### Functions

**`newton_optimize(f_prime: Callable, f_double_prime: Callable, x0: VDR, n_steps: int) -> VDR`**
- Newton's method for optimization (finding f'(x)=0)

**`gradient_descent_2d(grad: Callable, x0: VDR, y0: VDR, lr: VDR, steps: int) -> tuple[VDR, VDR]`**

**`simplex_2d(c: list[VDR], A: Mat, b: Vec) -> Vec`**
- Exact rational simplex method for 2D LP

**`bisection(f: Callable, a: VDR, b: VDR, n_steps: int) -> VDR`**
- O: midpoint after n bisection steps, exact rational

---

## 15. `vdr.math.graph`

### Functions

**`dijkstra(adj: dict, src: int) -> dict[int, VDR]`**
- I: adjacency dict {node: [(neighbor, weight_VDR), ...]}, source
- O: shortest distances from source, all exact

**`bellman_ford(n: int, edges: list[tuple], src: int) -> list[VDR]`**
- Handles negative rational weights

**`prim_mst(n: int, adj: dict) -> list[tuple]`**
- O: MST edges with exact weights

**`floyd_warshall(n: int, dist: Mat) -> Mat`**
- O: all-pairs shortest paths, exact

**`pagerank(adj: Mat, damping: VDR = VDR(85, 100)) -> Vec`**
- O: PageRank vector via linear system solve, sums to exactly 1

**`max_flow(n: int, cap: Mat, s: int, t: int) -> VDR`**
- Ford-Fulkerson with BFS augmenting paths, exact rational capacities

---

## 16. `vdr.math.game_theory`

### Functions

**`minimax_2x2(payoff: Mat) -> tuple[VDR, VDR, VDR]`**
- O: (p_star, q_star, game_value) for 2×2 zero-sum

**`nash_2x2(payoff_a: Mat, payoff_b: Mat) -> tuple`**
- O: Nash equilibrium mixed strategies

**`shapley_values(v_func: Callable, n: int) -> Vec`**
- I: characteristic function v(S) -> VDR, number of players
- O: Shapley value vector, sums to exactly v(N)

**`dominated_elimination(payoff: Mat) -> Mat`**
- O: reduced game after removing dominated strategies

**`cournot_duopoly(a: VDR, b: VDR, c1: VDR, c2: VDR) -> tuple`**
- I: demand intercept, slope, marginal costs
- O: (q1_star, q2_star, profit1, profit2) exact

---

## 17. `vdr.math.coding_theory`

### Functions

**`gf_add(a: int, b: int, p: int) -> int`** — Galois field addition

**`gf_mul(a: int, b: int, p: int) -> int`** — Galois field multiplication

**`gf_inv(a: int, p: int) -> int`** — multiplicative inverse in GF(p)

**`gf_poly_eval(coeffs: list[int], x: int, p: int) -> int`**

**`hamming74_encode(data: list[int]) -> list[int]`**
- I: 4-bit data word
- O: 7-bit Hamming codeword

**`hamming74_syndrome(received: list[int]) -> int`**

**`hamming74_correct(received: list[int]) -> list[int]`**
- O: corrected codeword

**`hamming_distance(a: list[int], b: list[int]) -> int`**

**`hamming_weight(a: list[int]) -> int`**

**`repetition_decode(bits: list[int], n: int) -> int`**
- Majority-vote decoding

---

## 18. `vdr.math.topology`

### Functions

**`boundary_matrix(simplices_k: list, simplices_k_minus_1: list) -> Mat`**
- I: k-simplices and (k-1)-simplices as sorted tuples
- O: boundary operator matrix with entries ±1 and 0

**`verify_d_squared_zero(d1: Mat, d0: Mat) -> bool`**
- O: True if d1 · d0 is the exact zero matrix

**`betti_numbers(boundary_matrices: list[Mat]) -> list[int]`**
- I: sequence of boundary matrices [d₁, d₂, ...]
- O: Betti numbers [β₀, β₁, ...] via exact rank computation

**`euler_characteristic(betti: list[int]) -> int`**
- O: χ = Σ(-1)^k β_k

---

## 19. `vdr.math.tropical`

### Globals

```python
TROPICAL_INF = None  # represents +∞ in min-plus algebra
```

### Functions

**`trop_add(a, b) -> VDR | None`** — min(a, b) in tropical

**`trop_mul(a, b) -> VDR | None`** — a + b in tropical

**`trop_mat_mul(A: list, B: list, n: int) -> list`** — tropical matrix multiplication

**`trop_det(M: list, n: int) -> VDR`** — tropical determinant (min-weight perfect matching)

**`gram_matrix(vectors: list[Vec]) -> Mat`** — Gram matrix vᵢ·vⱼ

**`gram_schmidt_exact(vectors: list[Vec]) -> tuple[list[Vec], Mat]`**
- O: (orthogonalized vectors, μ coefficient matrix), all exact

**`lovasz_condition(mu: Mat, B_star_norms: list[VDR], i: int, delta: VDR = VDR(3,4)) -> bool`**
- O: exact rational comparison, no float rounding

**`lll_reduce(basis: list[Vec], delta: VDR = VDR(3,4)) -> list[Vec]`**
- O: LLL-reduced basis, exact Lovász checks throughout

---

## 20. `vdr.math.control`

### Functions

**`state_evolve(A: Mat, B: Mat, x0: Vec, inputs: list[Vec]) -> list[Vec]`**
- I: system matrices, initial state, input sequence
- O: exact state trajectory, zero drift

**`controllability_matrix(A: Mat, B: Mat) -> Mat`**
- O: [B, AB, A²B, ..., Aⁿ⁻¹B]

**`observability_matrix(A: Mat, C: Mat) -> Mat`**
- O: [C; CA; CA²; ...; CAⁿ⁻¹]

**`is_controllable(A: Mat, B: Mat) -> bool`**
- O: True if controllability matrix has full rank (exact)

**`is_observable(A: Mat, C: Mat) -> bool`**

**`transfer_function_eval(num: list[VDR], den: list[VDR], s: VDR) -> VDR`**
- I: numerator/denominator polynomial coefficients, complex frequency s
- O: H(s) = N(s)/D(s) exact

**`cayley_hamilton_verify(A: Mat) -> Mat`**
- O: p(A) where p is characteristic polynomial. Should be exact zero matrix.

**`controllability_gramian(A: Mat, B: Mat, steps: int) -> Mat`**
- Discrete-time Gramian via exact matrix power sums

---

## 21. `vdr.math.wavelets`

### Functions

**`haar_forward(signal: list[VDR]) -> tuple[list[VDR], list[VDR]]`**
- I: signal (length power of 2)
- O: (averages, details)

**`haar_inverse(avgs: list[VDR], dets: list[VDR]) -> list[VDR]`**
- O: reconstructed signal, exact. haar_inverse(haar_forward(x)) == x

**`haar_multilevel(signal: list[VDR], levels: int) -> list[tuple]`**
- O: list of (averages, details) per level

**`haar_reconstruct_multilevel(decomposition: list[tuple]) -> list[VDR]`**
- O: perfect reconstruction

**`energy(signal: list[VDR]) -> VDR`**
- O: Σ|x[n]|² exact

**`parseval_verify(signal: list[VDR], decomposition) -> bool`**
- O: True if energy is preserved exactly

**`threshold(details: list[VDR], thresh: VDR) -> list[VDR]`**
- Hard thresholding for denoising

---

## 22. `vdr.math.transcendental`

### Globals — Named Constants as FnRemainder

Each constant is available both as a FnRemainder (arbitrary depth) and as a Q335 precomputed value.

```python
# Functional remainders — resolve to any depth
PI_FN       # make_series_fn: Machin arctan formula
E_FN        # make_series_fn: exp(1) Taylor
LN2_FN      # make_series_fn: 2·arctanh(1/3)
SQRT2_FN    # make_newton_fn: x -> (x + 2/x) / 2
SQRT3_FN    # make_newton_fn: x -> (x + 3/x) / 2
SQRT5_FN    # make_newton_fn: x -> (x + 5/x) / 2
SQRT7_FN    # make_newton_fn: x -> (x + 7/x) / 2
PHI_FN      # make_newton_fn: (1 + √5) / 2
ZETA3_FN    # make_series_fn: central binomial or Borwein
ZETA5_FN    # make_series_fn: Borwein accelerated
ZETA7_FN    # make_series_fn: Borwein accelerated
ZETA9_FN    # make_series_fn: Borwein accelerated
CATALAN_FN  # make_series_fn: Borwein accelerated

# Q335 precomputed (100-digit precision, ready to use)
PI          = VDR(219886425873..., 2**335)   # π
E           = VDR(190258044782..., 2**335)   # e
LN2         = VDR(485147735379..., 2**335)   # ln(2)
SQRT2       = VDR(989836684575..., 2**335)   # √2
PHI         = VDR(113249472467..., 2**335)   # φ = (1+√5)/2
PI_SQ       = VDR(690793580147..., 2**335)   # π²
PI_CU       = VDR(217019203653..., 2**335)   # π³
PI_QU       = VDR(681785935886..., 2**335)   # π⁴
E_PI        = VDR(161966389545..., 2**335)   # eᵖ
LN2_SQ      = VDR(336278784933..., 2**335)   # ln²(2)
LN2_QU      = VDR(161566155737..., 2**335)   # ln⁴(2)
LN3         = VDR(768940967886..., 2**335)   # ln(3)
LN5         = VDR(112647815694..., 2**335)   # ln(5)
LN10        = VDR(161162589232..., 2**335)   # ln(10)
SQRT3       = VDR(121229740294..., 2**335)   # √3
SQRT5       = VDR(156506921742..., 2**335)   # √5
SQRT7       = VDR(185181487127..., 2**335)   # √7
ZETA2       = VDR(115132263357..., 2**335)   # ζ(2) = π²/6
ZETA3       = VDR(841343946453..., 2**335)   # ζ(3)
ZETA5       = VDR(725766714875..., 2**335)   # ζ(5)
LI4_HALF    = VDR(362194064866..., 2**335)   # Li₄(1/2)
CATALAN     = VDR(641102851116..., 2**335)   # Catalan's G
```

### Functions

**`borwein_zeta(s: int, n: int = 210) -> VDR`**
- I: integer s ≥ 2, number of terms
- O: ζ(s) as exact rational via Borwein acceleration
- Geometric convergence 3⁻ⁿ. n=210 gives 100+ digits for any s.

**`borwein_eta(s: int, n: int = 210) -> VDR`**
- Dirichlet eta function

**`borwein_coefficients(n: int) -> list[VDR]`**
- O: d_k coefficients for Borwein acceleration, all exact rational

**`elliptic_k(k_sq: VDR, terms: int = 500) -> VDR`**
- I: k² as rational, number of hypergeometric terms
- O: K(k) = (π/2) · ₂F₁(1/2, 1/2; 1; k²), exact rational times Q335 π/2

**`elliptic_e(k_sq: VDR, terms: int = 500) -> VDR`**
- E(k) = (π/2) · ₂F₁(-1/2, 1/2; 1; k²)

**`hypergeometric_2f1(a: VDR, b: VDR, c: VDR, z: VDR, terms: int) -> VDR`**
- General ₂F₁ with rational parameters

**`clausen_2(x: VDR, terms: int) -> VDR`** — Cl₂(x)

**`clausen_3(x: VDR, terms: int) -> VDR`** — Cl₃(x)

**`exp_series(x: VDR, depth: int = 16) -> VDR`** — Taylor exp

**`sin_series(x: VDR, depth: int = 16) -> VDR`** — Taylor sin

**`cos_series(x: VDR, depth: int = 16) -> VDR`** — Taylor cos

**`ln_series(x: VDR, depth: int = 16) -> VDR`** — ln via arctanh reduction

**`arctan_series(x: VDR, depth: int = 16) -> VDR`**

**`arcsin_series(x: VDR, depth: int = 16) -> VDR`**

**`sqrt_newton(n: VDR, depth: int = 10, start: VDR = VDR(1)) -> VDR`**
- I: value to take √ of, Newton depth, starting guess
- O: exact rational approximation. Depth 10 = >100 digits.

**`pi_machin(terms: int = 160) -> VDR`**
- Machin's formula, geometric convergence

---

## 23. `vdr.math.chaos`

### Functions

**`tent_map(x: VDR) -> VDR`**
- I: x ∈ [0,1] rational
- O: tent map T(x) = 2x if x < 1/2, 2(1-x) if x ≥ 1/2. Exact.

**`bernoulli_shift(x: VDR) -> VDR`**
- O: 2x mod 1 exact

**`arnold_cat(x: VDR, y: VDR) -> tuple[VDR, VDR]`**
- O: Arnold cat map on torus, exact rational

**`logistic_map(x: VDR, r: VDR) -> VDR`**
- O: r·x·(1-x) exact. Warning: exponential denominator growth for r=4.

**`iterate_map(f: Callable, x0: VDR, steps: int) -> list[VDR]`**
- O: orbit [x₀, f(x₀), f²(x₀), ...] all exact

**`detect_period(orbit: list[VDR]) -> int | None`**
- I: exact orbit
- O: period if periodic, None if not detected within orbit length

**`lyapunov_product(derivatives: list[VDR]) -> VDR`**
- I: list of |f'(xₙ)| values
- O: product, exact

---

## 24. `vdr.math.geometry`

### Functions

**`line_intersect(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> tuple[VDR, VDR]`**
- I: four points as (VDR, VDR) pairs defining two lines
- O: intersection point (x, y), exact

**`polygon_area(vertices: list[tuple]) -> VDR`**
- Shoelace formula, exact

**`barycentric(p: tuple, a: tuple, b: tuple, c: tuple) -> tuple[VDR, VDR, VDR]`**
- O: barycentric coordinates, exact. Sum to exactly 1.

**`point_in_triangle(p: tuple, a: tuple, b: tuple, c: tuple) -> bool`**
- Exact — no epsilon needed

**`dist_sq(p1: tuple, p2: tuple) -> VDR`**
- Squared distance, exact (avoids sqrt)

**`circumcenter(a: tuple, b: tuple, c: tuple) -> tuple[VDR, VDR]`**
- O: circumcenter coordinates, exact

**`shoelace_signed(vertices: list[tuple]) -> VDR`**
- Signed area for orientation detection

---

## 25. `vdr.math.differential_eq`

### Functions

**`euler_solve(f: Callable, y0: VDR, x0: VDR, h: VDR, n_steps: int) -> list[tuple[VDR, VDR]]`**
- I: dy/dx = f(x,y), initial condition, step size, steps
- O: list of (x, y) pairs, all exact

**`rk4_step(f: Callable, x: VDR, y: VDR, h: VDR) -> VDR`**
- O: one RK4 step, exact (Butcher coefficients are 1/6, 1/3, 1/3, 1/6 — all rational)

**`rk4_solve(f: Callable, y0: VDR, x0: VDR, h: VDR, n_steps: int) -> list[tuple[VDR, VDR]]`**

**`mat_exp(A: Mat, t: VDR, terms: int) -> Mat`**
- O: truncated matrix exponential Σ(tA)ⁿ/n!, exact rational

**`picard_iterate(f: Callable, y0: VDR, n_iterations: int) -> Callable`**
- Picard iteration for successive approximations

**`lotka_volterra_step(state: tuple[VDR, VDR], h: VDR, a: VDR, b: VDR, c: VDR, d_param: VDR) -> tuple[VDR, VDR]`**
- One Euler step of Lotka-Volterra, exact

---

## 26. `vdr.math.cryptographic`

### Functions

**`mod_exp(base: int, exp: int, mod: int) -> int`**
- Fast modular exponentiation

**`extended_gcd(a: int, b: int) -> tuple[int, int, int]`**
- O: (gcd, x, y) where a·x + b·y = gcd

**`mod_inverse(a: int, m: int) -> int`**
- O: a⁻¹ mod m
- E: ValueError if gcd(a,m) ≠ 1

**`chinese_remainder(remainders: list[int], moduli: list[int]) -> int`**
- CRT reconstruction

**`rsa_keygen(p: int, q: int, e: int) -> tuple[int, int, int]`**
- O: (n, e, d) where d = e⁻¹ mod φ(n)

**`rsa_encrypt(m: int, e: int, n: int) -> int`**

**`rsa_decrypt(c: int, d: int, n: int) -> int`**

**`baby_giant(g: int, h: int, p: int) -> int`**
- Discrete log: find x where g^x ≡ h (mod p)

---

## 27. `vdr.signal.convolution`

### Functions

**`convolve(a: list[VDR], b: list[VDR]) -> list[VDR]`**
- O: discrete convolution, exact

**`correlate(a: list[VDR], b: list[VDR]) -> list[VDR]`**
- O: cross-correlation, exact

**`toeplitz_mat(h: list[VDR], n: int) -> Mat`**
- O: Toeplitz convolution matrix

**`convolve_via_toeplitz(a: list[VDR], b: list[VDR]) -> list[VDR]`**
- Verify convolve == Toeplitz matvec

---

## 28. `vdr.signal.dft`

### Functions

**`exact_dft(x: list[VDR], twiddle_depth: int = 16) -> list[tuple[VDR, VDR]]`**
- I: real rational signal, depth for trig functional remainders
- O: list of (real, imag) VDR pairs per frequency bin

**`exact_idft(X: list[tuple[VDR, VDR]], twiddle_depth: int = 16) -> list[VDR]`**
- O: reconstructed signal. IDFT(DFT(x)) == x exactly.

**`parseval_verify(x: list[VDR], X: list[tuple]) -> bool`**
- O: True if Σ|x[n]|² == (1/N)Σ|X[k]|² exactly

---

## 29. `vdr.signal.filters`

### Functions

**`iir_filter(x: list[VDR], a_coeff: VDR) -> list[VDR]`**
- I: input signal, feedback coefficient
- O: filtered output y[n] = a·y[n-1] + x[n], exact at every step

**`moving_average(signal: list[VDR], window: int) -> list[VDR]`**

**`z_transform(h: list[VDR], z: VDR) -> VDR`**
- Evaluate H(z) = Σ h[n]·z⁻ⁿ

---

## 30. `vdr.signal.schedule`

### Functions

**`linear_schedule(T: int, beta_start: VDR, beta_end: VDR) -> list[VDR]`**
- O: T evenly-spaced β values, all exact rational

**`cosine_schedule(T: int, s: VDR = VDR(8, 1000)) -> list[VDR]`**
- O: cosine noise schedule via rational cos approximation

**`compute_alphas(betas: list[VDR]) -> list[VDR]`**
- O: α = 1 - β for each timestep

**`compute_alpha_bars(alphas: list[VDR]) -> list[VDR]`**
- O: ᾱ = cumulative product, exact

---

## 31. `vdr.physics.qed`

### Globals

```python
ALPHA = VDR(...)  # fine-structure constant α at Q335, 100 digits
A1 = VDR(1, 2)    # 1-loop: exactly 1/2
# A2, A3 computed on demand via functions below
```

### Functions

**`a2_coefficient() -> VDR`**
- O: 197/144 + π²/12 + 3ζ(3)/4 − (π²/2)·ln(2), all Q335 arithmetic

**`a3_coefficient() -> VDR`**
- O: 3-loop coefficient involving ζ(5) and weight-5 products

**`anomalous_moment(n_loops: int = 3) -> VDR`**
- O: a_e through n_loops, evaluated with Q335 α

**`transcendental_weight(constant_name: str) -> int`**
- O: weight assignment (rational=0, π=1, ζ(n)=n, etc.)

---

## 32. `vdr.physics.quantum`

### Globals

```python
SIGMA_X = Mat.from_ints([[0, 1], [1, 0]])
SIGMA_Y  # complex: [[0, -i], [i, 0]] — represented as pairs
SIGMA_Z = Mat.from_ints([[1, 0], [0, -1]])
IDENTITY_2 = Mat.identity(2)
```

### Functions

**`pauli_multiply(a: str, b: str) -> tuple[VDR, str]`**
- I: Pauli labels ("x", "y", "z", "I")
- O: (phase, result_label) e.g. ("x","y") → (i, "z")

**`spin_rotation(axis: Vec, angle_over_pi: VDR, depth: int = 16) -> Mat`**
- I: rotation axis, angle as rational multiple of π, trig depth
- O: 2×2 rotation matrix U, U†U = I exact

**`measurement_probabilities(state: Vec) -> list[VDR]`**
- O: |aᵢ|² for each component. Sums to exactly 1.

**`density_matrix(state: Vec) -> Mat`**
- O: |ψ⟩⟨ψ| outer product

**`verify_unitarity(U: Mat) -> bool`**
- O: True if U†U == I exactly

---

## 33. `vdr.physics.orbital`

### Functions

**`kepler_newton(M: VDR, e: VDR, depth: int = 20) -> VDR`**
- I: mean anomaly, eccentricity, Newton depth
- O: eccentric anomaly E solving M = E - e·sin(E), exact rational

**`kepler_position(a: VDR, e: VDR, E: VDR) -> tuple[VDR, VDR]`**
- O: (x, y) in orbital plane

**`orbit_closure_verify(positions: list[tuple]) -> VDR`**
- O: distance between first and last position. Should be exactly 0 for closed orbit.

---

## 34. `vdr.physics.structural`

### Functions

**`assemble_stiffness(elements: list[tuple], n_dof: int) -> Mat`**
- I: element stiffness contributions, total DOF count
- O: global stiffness matrix K

**`solve_structure(K: Mat, F: Vec) -> Vec`**
- O: displacement vector u = K⁻¹F, exact

**`verify_equilibrium(K: Mat, u: Vec, F: Vec) -> bool`**
- O: True if K@u == F exactly

---

## 35. `vdr.physics.thermo`

### Functions

**`partition_function(energies: list[VDR], beta: VDR, exp_depth: int = 16) -> VDR`**
- O: Z = Σ exp(-β·Eᵢ), each exp as Taylor, exact rational at depth

**`free_energy(Z: VDR, beta: VDR, log_depth: int = 16) -> VDR`**
- O: F = -ln(Z)/β

**`entropy(energies: list[VDR], beta: VDR, depth: int = 16) -> VDR`**
- Via exact discrete calculus on F

**`ising_1d_transfer(J: VDR, h: VDR, beta: VDR, N: int) -> VDR`**
- O: partition function via 2×2 transfer matrix power, exact

---

## 36. `vdr.physics.crystallography`

### Functions

**`point_group_matrix(operation: str) -> Mat`**
- I: named operation ("C4z", "sigma_h", etc.)
- O: 3×3 rotation/reflection matrix, exact integer entries

**`verify_group_closure(matrices: list[Mat]) -> bool`**
- O: True if products of all pairs remain in the set (exact comparison)

**`structure_factor(atoms: list[tuple], hkl: tuple, depth: int = 16) -> tuple[VDR, VDR]`**
- I: list of (f, x, y, z) atom positions, Miller indices
- O: (real, imag) parts of F(hkl)

---

## 37. `vdr.physics.geodesy`

### Functions

**`helmert_forward(coords: Vec, params: dict) -> Vec`**
- I: coordinates, 7-parameter transformation
- O: transformed coordinates, exact

**`helmert_inverse(coords: Vec, params: dict) -> Vec`**

**`helmert_roundtrip_verify(coords: Vec, params: dict) -> bool`**
- O: True if inverse(forward(coords)) == coords exactly

---

## 38. `vdr.physics.optics`

### Globals

```python
def FREE_SPACE(d: VDR) -> Mat:  # [[1, d], [0, 1]]
def THIN_LENS(f: VDR) -> Mat:   # [[1, 0], [-1/f, 1]]
def FLAT_MIRROR() -> Mat:       # [[-1, 0], [0, -1]]  (reflection convention)
```

### Functions

**`system_matrix(elements: list[Mat]) -> Mat`**
- O: product of element ABCD matrices, left-to-right

**`verify_symplecticity(M: Mat) -> bool`**
- O: True if det(M) == 1 exactly

**`resonator_stability(M: Mat) -> tuple[bool, VDR]`**
- O: (is_stable, |A+D|/2) where stability requires < 1. Exact rational comparison.

**`matrix_power(M: Mat, n: int) -> Mat`**
- O: M^n via repeated squaring, exact

---

## 39. `vdr.ml.softmax`

### Functions

**`softmax(logits: Vec, exp_depth: int = 16) -> Vec`**
- O: probability vector, sums to exactly 1. Uses max-subtraction for numerical stability (exact, no overflow).

**`logsumexp(logits: Vec, exp_depth: int = 16) -> VDR`**

**`softmax_matrix_rows(M: Mat, exp_depth: int = 16) -> Mat`**
- Each row softmaxed independently

**`softmax_surrogate_square(logits: Vec) -> Vec`**
- Polynomial approximation avoiding exp entirely

---

## 40. `vdr.ml.exp`

### Functions

**`exp_series(x: VDR, depth: int = 16) -> VDR`**
- Taylor series Σxⁿ/n!, exact rational

**`exp_range_reduced(x: VDR, depth: int = 16) -> VDR`**
- Range reduction for large |x|: factor out integer part, multiply back

**`exp_neg(x: VDR, depth: int = 16) -> VDR`**
- exp(-|x|) via exp_range_reduced, ensuring positive result

---

## 41. `vdr.ml.logarithm`

### Functions

**`log1p_series(x: VDR, depth: int = 16) -> VDR`**
- ln(1+x) = x - x²/2 + x³/3 - ..., |x| < 1

**`log_series(x: VDR, depth: int = 16) -> VDR`**
- ln(x) for x > 0, via reduction to log1p range
- E: ValueError if x ≤ 0

**`log_ratio_near_one(num: VDR, den: VDR, depth: int = 16) -> VDR`**
- ln(num/den) when num ≈ den, avoiding cancellation

---

## 42. `vdr.ml.attention`

### Functions

**`attention_scores(Q: list[Vec], K: list[Vec]) -> list[Vec]`**
- O: QKᵀ score matrix as list of Vec rows

**`causal_mask(n: int) -> list[list[bool]]`**
- O: lower-triangular True mask

**`apply_boolean_mask(scores: list[Vec], mask: list[list[bool]], fill: VDR) -> list[Vec]`**
- Masked fill for causal attention

**`attention_weights(scores: list[Vec], mask: list[list[bool]] = None, exp_depth: int = 16) -> list[Vec]`**
- O: softmaxed attention weights. Each row sums to exactly 1.

**`weighted_sum(weights: Vec, values: list[Vec]) -> Vec`**

**`attention_mix(weight_rows: list[Vec], V: list[Vec]) -> list[Vec]`**

**`self_attention(Q: list[Vec], K: list[Vec], V: list[Vec], causal: bool = False, exp_depth: int = 16) -> list[Vec]`**
- Full self-attention pipeline

---

## 43. `vdr.ml.nn`

### Classes

**`VecParam(value: Vec, name: str = None)`** — trainable vector parameter with grad

**`MatParam(value: Mat, name: str = None)`** — trainable matrix parameter with grad

**`Module`** — base class with `parameters()`, `zero_grad()`

**`Linear(weight: Mat, bias: Vec)`** — forward: Wx + b, backward: exact gradients

**`ReLU()`** — forward: max(0, x), backward: 0 or 1 per element

**`Sequential(layers: list[Module])`** — forward/backward chain

**`FFN(l1: Linear, act: ReLU, l2: Linear)`** — feed-forward network block

### Functions

**`relu_scalar(x: VDR) -> VDR`** — max(0, x)

**`relu_prime_scalar(x: VDR) -> VDR`** — 0 if x < 0, 1 if x ≥ 0

---

## 44. `vdr.ml.autodiff`

### Classes

**`Node(value: VDR, children, backward_fn)`** — computation graph node

### Functions

**`ensure_node(x) -> Node`**

**`relu(x: Node) -> Node`** — with backward

**`sum_nodes(xs: list[Node]) -> Node`**

**`mean_nodes(xs: list[Node]) -> Node`**

**`mse_loss(pred: list[Node], target: list) -> Node`** — exact MSE with backward

**`dot_nodes(a: list[Node], b: list[Node]) -> Node`**

**`linear_node(weights, xs: list[Node], bias) -> Node`** — Wx + b as graph node

**`zero_grads(nodes: list[Node])`**

**`value_of_vec(nodes: list[Node]) -> Vec`**

**`grad_of_vec(nodes: list[Node]) -> Vec`**

---

## 45. `vdr.ml.optim`

### Classes

**`SGD(params: list, lr: VDR)`**
- `step()`: w ← w - lr·grad, exact
- `zero_grad()`

**`Momentum(params: list, lr: VDR, beta: VDR = VDR(9, 10))`**
- `step()`: v ← β·v + grad; w ← w - lr·v, exact
- `zero_grad()`

---

## 46. `vdr.ml.losses`

### Functions

**`mse(pred: Vec, target: Vec) -> VDR`** — mean squared error, exact

**`l1(pred: Vec, target: Vec) -> VDR`** — mean absolute error

**`hinge_binary(score: VDR, label: int) -> VDR`** — max(0, 1 - label·score)

**`mse_grad(pred: Vec, target: Vec) -> Vec`** — gradient of MSE

---

## 47. `vdr.ml.trainer`

### Functions

**`train_step(model, x: Vec, y: Vec, optimizer) -> VDR`**
- O: loss value after one forward-backward-update cycle

**`train_epoch(model, dataset: list[tuple], optimizer) -> list[VDR]`**
- O: list of per-sample losses

**`evaluate_epoch(model, dataset) -> list[VDR]`**
- O: losses without gradient update

**`predict_class(model, x: Vec) -> int`**
- O: argmax of model output

**`evaluate_classification(model, dataset) -> VDR`**
- O: accuracy as exact rational

---

## 48. `vdr.ml.transformer`

### Classes

**`Embedding(table: list[Vec])`**
- `lookup(idx: int) -> Vec`
- `lookup_many(ids: list[int]) -> list[Vec]`
- `to_qbasis(bits: int) -> Embedding`

**`FFNBlock(l1: Linear, l2: Linear)`** — two-layer FFN with ReLU

**`TransformerBlock(Wq, Wk, Wv, Wo: Mat, ffn: FFNBlock)`**
- `forward(xs: list[Vec]) -> list[Vec]` — self-attention + FFN

**`TransformerLM(embedding, blocks: list[TransformerBlock], output_proj)`**
- `forward_logits(token_ids: list[int]) -> list[Vec]`
- `embed(token_ids) -> list[Vec]`

---

## 49. `vdr.ml.sampling`

### Functions

**`cdf_from_probs(probs: Vec) -> Vec`** — cumulative distribution, exact

**`categorical_sample(probs: Vec, rng) -> int`** — exact rational CDF comparison

**`top_k_probs(probs: Vec, k: int) -> Vec`** — zero out below top-k, renormalize to sum 1

**`nucleus_probs(probs: Vec, threshold: VDR) -> Vec`** — nucleus (top-p) sampling

---

## 50. `vdr.ml.rng`

### Classes

**`VDRRandom(seed: int = 1)`**
- LCG with exact integer arithmetic
- `next_int() -> int`
- `randbelow(n: int) -> int`
- `rand_fraction() -> VDR` — uniform in [0, 1) as exact rational
- `randint(lo: int, hi: int) -> int`
- `shuffle_in_place(xs: list)`
- `permutation(n: int) -> list[int]`

---

## 51. `vdr.ml.init`

### Functions

**`rational_uniform_vec(dim, denom=100, seed=1, lo=-1, hi=1) -> Vec`**

**`rational_uniform_mat(nrows, ncols, denom=100, seed=1, lo=-1, hi=1) -> Mat`**

**`xavier_like_mat(nrows, ncols, denom=100, seed=1) -> Mat`**
- Xavier-like initialization with rational bounds

**`zero_bias(dim: int) -> Vec`**

---

## 52. `vdr.ml.tensor`

### Classes

**`Tensor3D(data: list[list[Vec]])`** — batch × sequence × dimension

### Functions

**`batched_matvec(mats: list[Mat], vecs: list[Vec]) -> list[Vec]`**

**`rowwise_add_bias(rows: list[Vec], bias: Vec) -> list[Vec]`**

**`masked_fill_rows(rows: list[Vec], mask, fill) -> list[Vec]`**

**`reduce_sum_rows(rows: list[Vec]) -> Vec`**

---

## 53. `vdr.ml.datasets`

### Functions

**`build_vocab(tokens: list[str]) -> dict[str, int]`**

**`encode_tokens(tokens: list[str], vocab: dict) -> list[int]`**

**`decode_tokens(ids: list[int], inv_vocab: dict) -> list[str]`**

**`invert_vocab(vocab: dict) -> dict[int, str]`**

**`sliding_windows(ids: list[int], seq_len: int) -> list[tuple]`**

**`one_hot(index: int, size: int) -> Vec`**

**`tiny_text_dataset(text: str, seq_len: int) -> tuple`**
- O: (windows, vocab, inv_vocab) ready for training

---

## 54. `vdr.ml.checkpoint`

### Functions

**`save_parameters(params: list) -> dict`**
- O: JSON-serializable dict of all parameter values as VDR dicts

**`load_parameters(saved: dict) -> list`**
- O: restored parameter values

**`save_model(model) -> dict`**
- O: full model state as serializable dict

---

## 55. `vdr.ml.metrics`

### Functions

**`exact_accuracy(pred_ids: list[int], target_ids: list[int]) -> VDR`**
- O: correct/total as exact rational

**`argmax_vec(v: Vec) -> int`**

**`denominator_complexity_vec(v: Vec) -> tuple`**

**`denominator_complexity_mat(m: Mat) -> tuple`**

**`parameter_denominator_complexity(params: list) -> tuple`**
- O: aggregate denominator complexity across all model parameters

---

## 56. `vdr.diffusion.schedule`

### Functions

**`exact_sqrt(a: VDR, depth: int = 10) -> VDR`**
- Newton √a with caching. Depth 10 = >100 digits.

**`linear_schedule(T: int, beta_start: VDR, beta_end: VDR) -> DiffusionSchedule`**

**`cosine_schedule(T: int, s: VDR = VDR(8, 1000)) -> DiffusionSchedule`**

### Classes

**`DiffusionSchedule(betas: list[VDR], sqrt_depth: int = 10)`**
- Properties: `betas`, `alphas`, `alpha_bars`, `sqrt_alpha_bars`, `sqrt_one_minus_alpha_bars`
- All precomputed, all exact rational (sqrt via Newton)
- `posterior_variance(t: int) -> VDR`

---

## 57. `vdr.diffusion.forward`

### Functions

**`forward_sample(x0: Vec, t: int, schedule: DiffusionSchedule, epsilon: Vec) -> Vec`**
- O: xₜ = √ᾱₜ·x₀ + √(1-ᾱₜ)·ε, exact

**`forward_sample_step(x_prev: Vec, t: int, schedule, epsilon: Vec) -> Vec`**
- One step from x_{t-1} to x_t

**`forward_trajectory(x0: Vec, schedule, epsilons: list[Vec]) -> list[Vec]`**
- O: complete forward path [x₀, x₁, ..., x_T]

---

## 58. `vdr.diffusion.reverse`

### Functions

**`compute_x0_prediction(xt: Vec, t: int, schedule, eps_pred: Vec) -> Vec`**
- O: x₀_pred = (xₜ - √(1-ᾱₜ)·ε_pred) / √ᾱₜ, exact

**`compute_posterior_mean(xt: Vec, t: int, schedule, eps_pred: Vec) -> Vec`**

**`reverse_step(xt: Vec, t: int, schedule, eps_pred: Vec, z: Vec = None) -> Vec`**
- One stochastic reverse step

**`reverse_step_ddim(xt: Vec, t: int, t_prev: int, schedule, eps_pred: Vec, eta: VDR = VDR(0)) -> Vec`**
- DDIM deterministic step. With eta=0: roundtrip error = exactly 0.

**`reverse_sample_loop(xT: Vec, schedule, predict_noise: Callable, noise_vectors: list[Vec] = None) -> Vec`**
- Full reverse chain

---

## 59. `vdr.diffusion.sampling`

### Functions

**`verify_schedule_consistency(schedule) -> bool`**
- O: True if all α = 1-β, ᾱ = cumulative product, etc.

**`verify_snr_monotonic(schedule) -> bool`**
- Exact rational comparison at adjacent pairs

**`verify_coefficient_identity(schedule) -> bool`**
- (√ᾱ)² + (√(1-ᾱ))² residual check

**`make_oracle_predictor(x0: Vec, schedule) -> Callable`**
- O: perfect noise predictor for roundtrip testing

**`verify_forward_reverse_roundtrip(x0: Vec, schedule, epsilon: Vec) -> VDR`**
- O: error magnitude. Should be < 10⁻⁵⁰ or exactly 0 for DDIM.

**`verify_multi_step_drift(x0: Vec, schedule, epsilon: Vec, num_cycles: int = 3) -> list[VDR]`**
- O: per-cycle error. Should not grow. Central result of VDR-26.

---

## 60. Build Phase Mapping

| Phase | Modules | Dependencies |
|---|---|---|
| 1 | `core` | none |
| 2 | `active` | core |
| 3 | `fn` | core |
| 4 | `linalg` | core, active |
| 5 | `export`, `basis` | core |
| 6 | `__init__` wiring | all core |
| 7 | `math.*` (20 modules) | core, active, fn, linalg, basis |
| 8 | `signal.*` (4 modules) | core, active, fn, linalg |
| 9 | `physics.*` (8 modules) | core, active, fn, linalg, basis, math.transcendental |
| 10 | `ml.*` (17 modules) | core, active, fn, linalg, basis, export |
| 11 | `diffusion.*` (4 modules) | core, active, fn, linalg, ml.softmax |
| 12 | All tests, gym ports | all modules |
| 13 | pyproject.toml, README, examples, PyPI release | all |
