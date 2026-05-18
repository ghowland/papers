# vdr-math Technical Specification

## Package Identity

**PyPI name:** `vdr-math`
**Import name:** `vdr`
**Python:** 3.8+, no required external dependencies (mpmath optional for decimal export)
**License:** TBD
**Tagline:** Exact arithmetic with Value, Denominator, Remainder triples

```
pip install vdr-math
```

```python
from vdr import VDR
from vdr.linalg import Vec, Mat
from vdr.fn import resolve, make_newton_fn
from vdr.export import to_decimal
```

---

## 1. Package Structure

```
vdr-math/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── vdr/
│       ├── __init__.py          # VDR, Remainder, errors re-exported
│       ├── core.py              # VDR, Remainder, normalization, closed arithmetic
│       ├── active.py            # active multiplication and division
│       ├── fn.py                # FnRemainder, resolve, discrete calculus, factories
│       ├── linalg.py            # Vec, Mat, Gaussian elimination
│       ├── export.py            # to_float, to_decimal, to_fraction (lossy boundary)
│       ├── basis.py             # D-frame management, Q335 default, to_qbasis
│       └── _compat.py           # internal coercion helpers
├── tests/
│   ├── test_core.py             # triple construction, normalization, closed arithmetic
│   ├── test_active.py           # active mul/div, cross-terms, divmod rule
│   ├── test_fn.py               # functional remainder, Newton, series, discrete calculus
│   ├── test_linalg.py           # Vec, Mat, det, inv, solve, rank, Gaussian
│   ├── test_export.py           # projection boundary, decimal, float
│   ├── test_basis.py            # D-frame config, Q335, rebase
│   ├── test_normalize.py        # GCD reduction, N7 collapse, large-Q reduction
│   └── gym/                     # ported from existing 23 gym scripts
│       ├── test_gym_01.py
│       ├── ...
│       └── test_gym_23.py
└── examples/
    ├── quickstart.py
    ├── hilbert_inverse.py
    ├── newton_sqrt2.py
    └── q335_constants.py
```

---

## 2. Module Specifications

### 2.1 `vdr.core` (currently `vdr.py`)

The foundation. Everything else imports from here.

**Classes:**

`Remainder(base: int, children: list[VDR])` — the R slot. Atomic when children is empty. Composite otherwise. Never subclassed except by `FnRemainder` in `vdr.fn`.

`VDR(v: int, d: int = 1, r: Remainder | int | None = None)` — the triple. V and D are always integers. D is never zero. R defaults to `Remainder(0)`.

**Errors (all subclass `VDRError`):**

`VDRError`, `ZeroDenominatorError`, `InvalidStructureError`, `RebaseError`, `ArithmeticFailure`

**Closed arithmetic (operators on VDR):**

`+`, `-`, `*`, `/`, `-x`, `abs(x)`, `==`, `!=`, `<`, `<=`, `>`, `>=`, `hash(x)`, `float(x)`

Closed arithmetic is defined directly on VDR. Active cases delegate to `vdr.active` if installed, otherwise raise `ArithmeticFailure`.

**Normalization — the fix list:**

Current normalization performs: sign convention, GCD reduction, child normalization, canonical ordering, same-D merge, closed-form preference (N7).

**New in vdr-math:** when R is zero or value-equivalent to zero (the Newton perfect-square problem), GCD-reduce unconditionally. Specifically: after normalizing R, if `R.is_zero` or if R normalizes such that `legacy_value(R) == 0`, collapse to closed form and GCD-reduce V and D. This fixes the 4/37 VDR-26 failures and the VDR-28 normalization presentation issues where structurally huge fractions like 2k/k should reduce to [2, 1, 0].

**Rebase:**

`VDR.rebase(target_d: int) -> VDR` — change D while preserving exact value. Uses divmod. Mismatch witness in R.

**Lift:**

`VDR._lift_vdr(k: int) -> VDR` — scale V and R by k, preserve child D.

**Structural metrics:**

`depth()`, `size()`, `den_complexity()` — unchanged from current.

**Coercion:**

`_coerce(other)` accepts `VDR`, `int`, `Fraction`. Returns `VDR`. Internal use.

### 2.2 `vdr.active` (currently `active_mul.py`)

**Rename rationale:** `active_mul` is implementation-named. `active` is concept-named. The module handles all active arithmetic.

**Public API:**

`active_mul(a: VDR, b: VDR) -> VDR` — exact multiplication including active operands. Cross-terms V₁·R₂, V₂·R₁, R₁·R₂ captured as remainder structure. Frame is D₁·D₂, closed part is V₁·V₂.

`active_div(a: VDR, b: VDR) -> VDR` — division. By closed: multiply by reciprocal. By active: v1 compromise (project divisor, invert, multiply; divisor remainder structure lost).

`install()` — patches `VDR.__mul__`, `__rmul__`, `__truediv__`, `__rtruediv__` so operators handle active objects.

`uninstall()` — restores original operators.

**Change from current:** `install()` is called automatically by `vdr.__init__` so active arithmetic works out of the box. No manual patching required. `uninstall()` remains available for testing the core in isolation.

### 2.3 `vdr.fn` (stays `fn.py`)

**Classes:**

`FnRemainder(func, name, meta)` — subclass of `Remainder`. Callable stored in R slot. `f(depth: int) -> VDR`. Name string for inspectability.

**Public API:**

`resolve(x: VDR, depth: int) -> VDR` — expand functional remainder at given depth.

`resolve_recursive(x: VDR, depth: int) -> VDR` — resolve all functional remainders in tree.

`is_functional(x: VDR) -> bool` — check if R is `FnRemainder`.

**Factories:**

`make_newton_fn(name, step_fn) -> FnRemainder` — Newton-Raphson iteration. Quadratic convergence. ~8 steps for 100 digits.

`make_series_fn(name, term_fn, initial) -> FnRemainder` — series partial sums. Each depth is exact rational.

`make_iterative_fn(name, step, start) -> FnRemainder` — general iteration.

`make_constant_fn(name, value_func) -> FnRemainder` — named constant.

**Discrete calculus:**

`discrete_derivative(f, h) -> callable` — Dₕf(x) = (f(x+h) − f(x))/h

`discrete_derivative_nth(f, h, order) -> callable` — repeated application.

`discrete_integral(f, a, b, n) -> VDR` — left Riemann sum, exact.

`discrete_integral_trapz(f, a, b, n) -> VDR` — trapezoidal, exact.

**Decorator:**

`@vdr_fn(name)` — marks a function as VDR remainder function.

**Change from current:** `install()` called automatically by `vdr.__init__`. Patches `is_closed`, `is_active`, `to_fraction` to be aware of `FnRemainder`.

### 2.4 `vdr.linalg` (stays `linalg.py`)

**Classes:**

`Vec(data: list[VDR | int])` — exact vector. `+`, `-`, `*` (scalar), `dot`, `==`.

`Mat(rows: list[list | Vec])` — exact matrix. `+`, `-`, `*` (scalar, matrix, vector), `det()`, `inv()`, `solve(b)`, `rank()`, `T`, `trace()`.

**Constructors:**

`Vec.from_ints(ns)`, `Vec.from_fracs(pairs)`, `Vec.zero(n)`

`Mat.from_ints(data)`, `Mat.from_fracs(data)`, `Mat.identity(n)`, `Mat.zero(nrows, ncols)`

**Change from current — Gaussian elimination for det and inv:**

Current `det()` uses cofactor expansion O(n!). Current `inv()` uses adjugate. Current `solve()` uses Cramer's rule. `rank()` already uses Gaussian.

**New in vdr-math:** add `det_gauss()`, `inv_gauss()`, `solve_gauss()` using Gaussian elimination O(n³). Make these the default for n ≥ 5. Keep cofactor methods available as `det_cofactor()`, `inv_adjugate()`, `solve_cramer()` for small matrices and testing. The `det()`, `inv()`, `solve()` methods dispatch automatically based on size.

**Serialization (stays here):**

`parse_vdr(text) -> VDR` — bracket notation parser.

`vdr_to_dict(x) -> dict` / `vdr_from_dict(d) -> VDR` — JSON round-trip.

`vdr_to_latex(x) -> str` — LaTeX export.

### 2.5 `vdr.export` (stays `export.py`)

The lossy boundary. Loss belongs to the target format.

`to_fraction(x: VDR) -> Fraction` — exact for closed. Legacy-flattened for active.

`to_float(x: VDR) -> float` — lossy IEEE 754.

`to_decimal(x: VDR, digits: int = 50) -> str` — decimal string. Uses mpmath if available, manual long division otherwise.

No changes from current beyond ensuring FnRemainder raises cleanly (resolve first).

### 2.6 `vdr.basis` (currently `basis.py`)

D-frame management. This is where the configurable denominator lives.

**Public API:**

`q_basis_denominator(bits: int) -> int` — returns `2**bits`. Q335 is `q_basis_denominator(335)`.

`to_qbasis(x, bits: int) -> VDR` — project a value onto the `2**bits` grid as `[round(x * 2**bits), 2**bits, 0]`.

`vec_to_qbasis(v, bits) -> Vec` / `mat_to_qbasis(m, bits) -> Mat` — batch projection.

`qb_rebase_add(a, b, bits) -> VDR` — addition staying in basis frame.

`qb_rebase_mul(a, b, bits) -> VDR` — multiplication with divmod back to basis frame. D stays `2**bits`. Overflow in R.

**Default basis:** Q335 (bits=335). Configurable per-call.

**Change from current:** add module-level default:

```python
import vdr.basis
vdr.basis.DEFAULT_BITS = 335  # user can change

# or
vdr.basis.set_default(bits=668)  # 200-digit precision
```

### 2.7 `vdr.__init__`

```python
from vdr.core import VDR, Remainder, VDRError, ZeroDenominatorError, ...
from vdr.linalg import Vec, Mat
from vdr import active
from vdr import fn

# auto-install active arithmetic and fn awareness
active.install()
fn.install()
```

User gets working active arithmetic and functional remainders on import. No manual patching.

### 2.8 `vdr._compat`

Internal module for coercion helpers shared across modules. `_coerce`, `_to_vdr`. Not public API.

---

## 3. The Normalization Fix

**Problem:** Newton iteration on perfect squares (√4, √9, √(1/4)) produces correct values in unreduced form. √4 returns something like [2k, k, 0] for large k instead of [2, 1, 0]. Structural comparison fails. Printing is unwieldy.

**Root cause:** when R normalizes to zero (or value-equivalent to zero), the V/D pair isn't GCD-reduced.

**Fix in `VDR.normalize()`:**

```python
# After normalizing R:
if nr.is_zero or nr.is_globally_zero:
    # Also check: does R have legacy_value == 0?
    # Collapse to closed, then GCD-reduce
    v_total = v  # absorb any remainder base
    if not nr.is_zero and nr.legacy_value() == 0:
        # remainder is structurally nonzero but value-zero
        nr = Remainder(0)
    g = gcd(abs(v_total), abs(d))
    if g > 0:
        v_total, d = v_total // g, d // g
    return VDR(v_total, d, Remainder(0))
```

**Scope:** fixes 4 VDR-26 test failures and normalization presentation issues from VDR-28. Zero arithmetic impact — only display and structural comparison affected.

---

## 4. What Moves Where

| Current file | Destination | Notes |
|---|---|---|
| `vdr/vdr.py` | `src/vdr/core.py` | Rename for clarity |
| `vdr/active_mul.py` | `src/vdr/active.py` | Rename, auto-install |
| `vdr/fn.py` | `src/vdr/fn.py` | Auto-install |
| `vdr/linalg.py` | `src/vdr/linalg.py` | Add Gaussian methods |
| `vdr/export.py` | `src/vdr/export.py` | Unchanged |
| `vdr/basis.py` | `src/vdr/basis.py` | Add DEFAULT_BITS |
| `vdr/__init__.py` | `src/vdr/__init__.py` | Re-exports + auto-install |

**Not in core package (application-layer, separate or examples):**

| Current file | Disposition |
|---|---|
| `vdr/softmax.py` | Separate package or examples |
| `vdr/exp.py` | Separate package or examples |
| `vdr/logarithm.py` | Separate package or examples |
| `vdr/attention.py` | Separate package or examples |
| `vdr/autodiff.py` | Separate package or examples |
| `vdr/nn.py` | Separate package or examples |
| `vdr/optim.py` | Separate package or examples |
| `vdr/trainer.py` | Separate package or examples |
| `vdr/transformer.py` | Separate package or examples |
| `vdr/tensor.py` | Separate package or examples |
| `vdr/sampling.py` | Separate package or examples |
| `vdr/init.py` | Separate package or examples |
| `vdr/rng.py` | Separate package or examples |
| `vdr/datasets.py` | Separate package or examples |
| `vdr/losses.py` | Separate package or examples |
| `vdr/metrics.py` | Separate package or examples |
| `vdr/checkpoint.py` | Separate package or examples |
| `diffusion_*.py` | Separate package or examples |
| `universal_compaction.py` | Separate project |
| All `test_*.py` | `tests/` directory, ported to pytest |
| All `gym/gym_*.py` | `tests/gym/`, ported to pytest |

---

## 5. Test Strategy

**Framework:** pytest

**Core tests (must pass before any release):**

`test_core.py` — construction, normalization (including the fix), sign convention, GCD reduction, N7 collapse, closed arithmetic (add/sub/mul/div), rebase, lift, equality (structural and value), hash, comparison operators, coercion from int and Fraction.

`test_active.py` — active add (same-D, different-D), active mul (closed×closed, closed×active, active×active), cross-term structure, active div (by closed, by active with projection), negation of active objects.

`test_fn.py` — FnRemainder construction, resolve at multiple depths, Newton √2 (verify residual < 10⁻⁵⁰ at depth 10), make_series_fn, make_newton_fn, discrete derivative (x² at x=3 h=1/1000 = 6001/1000), discrete integral (∫x² [0,1] n=10 = 57/200), finite difference tables (Δ³(x³) = [6,6], Δ⁴(x³) = [0]).

`test_linalg.py` — Vec arithmetic, Mat arithmetic, det (cofactor and Gaussian agree), inv (Hilbert 3×3, 4×4, 5×5 residual = exactly 0), solve, rank (full rank and deficient), identity properties, Gaussian elimination correctness.

`test_export.py` — to_fraction roundtrip, to_float lossy, to_decimal at various digit counts, mpmath path and fallback path.

`test_basis.py` — Q335 construction, to_qbasis roundtrip, qb_rebase_mul divmod rule (D stays 2³³⁵, overflow in R), DEFAULT_BITS configuration, non-Q335 bases (D=7, D=2¹⁶).

`test_normalize.py` — the specific fix: √4 Newton reduces to [2, 1, 0], √9 to [3, 1, 0], √(1/4) to [1, 2, 0], large unreduced fractions collapse, value-zero remainders collapse.

**Gym tests (ported, run as integration suite):**

23 gym scripts ported to pytest. Each becomes `tests/gym/test_gym_NN.py`. Assert counts match original pass counts. These validate VDR across all proven domains.

---

## 6. `pyproject.toml`

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "vdr-math"
version = "0.1.0"
description = "Exact arithmetic with Value, Denominator, Remainder triples"
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
authors = [{ name = "..." }]
keywords = ["exact-arithmetic", "rational", "remainder", "VDR"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Programming Language :: Python :: 3",
]

[project.optional-dependencies]
decimal = ["mpmath"]
dev = ["pytest", "mpmath"]

[tool.hatch.build.targets.wheel]
packages = ["src/vdr"]
```

---

## 7. Public API Summary

```python
# Core triple
from vdr import VDR, Remainder, VDRError

x = VDR(1, 3)           # 1/3 exact
y = VDR(2, 7)           # 2/7 exact
z = x + y               # exact, normalized
z = x * y               # active mul, auto-installed

# Linear algebra
from vdr.linalg import Vec, Mat

v = Vec.from_ints([1, 2, 3])
m = Mat.from_ints([[1, 2], [3, 4]])
d = m.det()              # exact
m_inv = m.inv()          # exact

# Functional remainder
from vdr.fn import resolve, make_newton_fn

sqrt2 = make_newton_fn("sqrt2", lambda x: (x + VDR(2)/x) / VDR(2))
obj = VDR(0, 1, sqrt2)
val = resolve(obj, depth=10)  # exact rational, >100 correct digits

# Discrete calculus
from vdr.fn import discrete_derivative, discrete_integral

df = discrete_derivative(lambda x: x * x, VDR(1, 1000))
area = discrete_integral(lambda x: x * x, VDR(0), VDR(1), 100)

# D-frame / basis
from vdr.basis import to_qbasis, set_default
set_default(bits=335)    # Q335, or any other

# Export (lossy boundary)
from vdr.export import to_decimal, to_float
print(to_decimal(z, digits=50))
```

---

## 8. Build Order

Phase 1: `core.py` with normalization fix, full test suite, all closed arithmetic working.

Phase 2: `active.py` with auto-install, active mul/div tests.

Phase 3: `fn.py` with auto-install, Newton/series/discrete calculus tests.

Phase 4: `linalg.py` with Gaussian elimination added, Hilbert matrix tests.

Phase 5: `export.py` and `basis.py`, Q335 tests.

Phase 6: `__init__.py` wiring, pyproject.toml, README, examples.

Phase 7: gym tests ported to pytest.

Phase 8: PyPI release.

---

## 9. Operational Rules (carried through all code)

**Remainder is first-class.** Never error. Never residue. The R slot carries exact unresolved structure.

**D never explodes.** Multiplication uses divmod. Overflow goes to R. D stays fixed.

**Q335 is default, not definition.** Any D is valid. The library works identically at D=7 or D=2³³⁵.

**No required external dependencies.** mpmath is optional for decimal export. Everything else is stdlib.

**The code is the specification.** Every claim verified by executable tests.

---

# Addendum: All Domains Are Library Modules

The tech spec incorrectly relegated the application-layer modules (LLM, diffusion, math domains) to "examples." They are built-in library components. When you `pip install vdr-math`, you get every domain ready to use.

## Revised Package Structure

```
src/vdr/
├── __init__.py
├── core.py              # VDR, Remainder, normalization, closed arithmetic
├── active.py            # active mul/div
├── fn.py                # FnRemainder, resolve, discrete calculus
├── linalg.py            # Vec, Mat, Gaussian
├── export.py            # lossy boundary
├── basis.py             # D-frame, Q335
├── _compat.py           # internal helpers
│
├── math/                # all proven math domains
│   ├── __init__.py
│   ├── number_theory.py     # GCD, LCM, Egyptian fractions, Stern-Brocot, Farey, totient, harmonics
│   ├── polynomial.py        # eval, add/mul/div, GCD, Lagrange, rational roots, Cayley-Hamilton
│   ├── continued_fractions.py  # to_cf, from_cf, convergents, Stern-Brocot paths, periodic detection
│   ├── combinatorics.py     # binomial, Stirling, Bell, derangements, multinomial, Catalan
│   ├── sequences.py         # Fibonacci, Lucas, Catalan, Bernoulli, Tribonacci, rational recurrences
│   ├── probability.py       # Bayes, Markov steady state, gambler's ruin, binomial PMF, sequential update
│   ├── symbolic.py          # partial fractions, rational functions, power sums, poly differentiation/integration
│   ├── optimization.py      # Newton, gradient descent, simplex, bisection
│   ├── graph.py             # Dijkstra, Bellman-Ford, Prim, Floyd-Warshall, PageRank
│   ├── game_theory.py       # minimax, Nash, Shapley, Cournot, dominated strategies
│   ├── coding_theory.py     # GF(p), Hamming, syndrome decode, checksums
│   ├── topology.py          # simplicial boundary, Betti numbers, Euler characteristic
│   ├── tropical.py          # min-plus, tropical det, lattice Gram-Schmidt, LLL
│   ├── control.py           # state-space, controllability, observability, transfer functions
│   ├── wavelets.py          # Haar forward/inverse, multi-level, Parseval, denoising
│   ├── transcendental.py    # Q335 constants, Borwein zeta, elliptic K/E, series evaluation
│   ├── chaos.py             # tent map, Bernoulli shift, Arnold cat, logistic map, period detection
│   ├── geometry.py          # line intersection, Shoelace, barycentric, circumcenter, point-in-triangle
│   ├── differential_eq.py   # Euler, RK4, Picard, Lotka-Volterra, matrix exponential
│   └── cryptographic.py     # modular exp, extended GCD, CRT, RSA, baby-step giant-step
│
├── signal/              # signal processing domain
│   ├── __init__.py
│   ├── convolution.py       # discrete convolution, cross-correlation, Toeplitz
│   ├── dft.py               # exact DFT/IDFT, Parseval verification
│   ├── filters.py           # IIR, moving average, z-transform
│   └── schedule.py          # noise schedules (linear, cosine)
│
├── physics/             # physical computation domains
│   ├── __init__.py
│   ├── qed.py               # A₂, A₃ coefficients, fine-structure constant
│   ├── quantum.py           # Pauli matrices, spin rotation, measurement, density matrices
│   ├── orbital.py           # Kepler equation, orbit closure, patched conics
│   ├── structural.py        # direct stiffness, equilibrium verification
│   ├── thermo.py            # partition functions, Ising, Boltzmann weights
│   ├── crystallography.py   # point groups, structure factor
│   ├── geodesy.py           # Helmert, coordinate transforms
│   └── optics.py            # ABCD matrices, resonator stability
│
├── ml/                  # machine learning domains
│   ├── __init__.py
│   ├── softmax.py           # exact softmax, logsumexp, sum-to-one guarantee
│   ├── exp.py               # exp series, range-reduced
│   ├── logarithm.py         # log series, log1p
│   ├── attention.py         # exact attention scores, causal mask, weighted sum
│   ├── nn.py                # Linear, ReLU, Sequential, parameters, backward
│   ├── autodiff.py          # Node, backward, chain rule, exact gradients
│   ├── optim.py             # SGD, Momentum, exact parameter updates
│   ├── losses.py            # MSE, L1, hinge, exact loss gradients
│   ├── trainer.py           # train_step, train_epoch, evaluate
│   ├── transformer.py       # Embedding, FFN, TransformerBlock, exact forward
│   ├── sampling.py          # categorical, top-k, nucleus, exact CDF
│   ├── rng.py               # deterministic LCG, exact rational random
│   ├── init.py              # Xavier-like, rational uniform
│   ├── tensor.py            # Tensor3D, batched ops
│   ├── datasets.py          # vocab, tokenization, sliding windows
│   ├── checkpoint.py        # save/load exact parameters
│   └── metrics.py           # accuracy, denominator complexity
│
└── diffusion/           # diffusion model domains
    ├── __init__.py
    ├── schedule.py          # linear/cosine schedule, exact √ᾱ
    ├── forward.py           # forward_sample, forward_trajectory
    ├── reverse.py           # x₀ prediction, posterior mean, DDIM
    └── sampling.py          # roundtrip verification, oracle predictor, drift test
```

## Usage

```python
# Direct domain use — no setup code needed
from vdr.math.probability import bayes_update, binom_pmf
from vdr.math.game_theory import shapley_3
from vdr.math.transcendental import Q335_PI, borwein_zeta
from vdr.physics.quantum import pauli_x, spin_rotate
from vdr.physics.qed import a2_coefficient
from vdr.ml.softmax import softmax
from vdr.ml.attention import self_attention
from vdr.diffusion.forward import forward_sample
from vdr.math.number_theory import farey, harmonic, euler_totient
from vdr.signal.dft import exact_dft, exact_idft
```

## What Tests Become

Tests don't implement the math — they exercise the built-in modules. The gym scripts become thin test files that call library functions and assert results:

```python
# tests/gym/test_gym_01.py
from vdr.math.number_theory import harmonic, euler_totient, farey
from vdr import VDR

def test_harmonic_10():
    assert harmonic(10) == VDR(7381, 2520)

def test_totient_100():
    assert euler_totient(100) == 40
```

## Build Order Revision

Phases 1–6 unchanged (core, active, fn, linalg, export, basis).

Phase 7: `vdr.math.*` — port all 23 gym implementations into library modules.

Phase 8: `vdr.signal.*` — port signal processing.

Phase 9: `vdr.physics.*` — port physical computation.

Phase 10: `vdr.ml.*` — port ML pipeline.

Phase 11: `vdr.diffusion.*` — port diffusion.

Phase 12: Tests call library modules. Gym tests become thin assertion layers.

Phase 13: PyPI release.

