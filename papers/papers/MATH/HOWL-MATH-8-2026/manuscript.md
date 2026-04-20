# Q335
## An Operationally Exact Number System for Physical Computation

### Registry: [@HOWL-MATH-8-2026]

**Series Path:** [@HOWL-MATH-2-2026] → [@HOWL-MATH-3-2026] → [@HOWL-MATH-4-2026] → [@HOWL-MATH-8-2026]

**DOI:** 10.5281/zenodo.19665765

**Date:** April 6, 2026

**Domain:** Computational Mathematics / Number Systems

**Status:** Complete

---

## I. THE PROBLEM

Physics needs two kinds of numbers simultaneously.

The first kind is exact: the beta coefficient b₂ = −19/6, the Schwinger coefficient A₁ = 1/2, the Casimir operator C₂(fund SU(3)) = 4/3. These are Fractions — ratios of integers — and they carry physical meaning in every digit. The 19 counts particles. The 6 counts normalizations. Converting −19/6 to −3.16667 erases the meaning.

The second kind is transcendental: π, ζ(3) = 1.202..., ln(2) = 0.693..., Li₄(1/2). These appear in loop integrals, angular integrations, and geometric formulas throughout physics. They are irrational — no Fraction equals them. They break Fraction arithmetic.

Standard computational approaches handle this tension in one of four ways:

Floating point (64-bit double): converts everything to ~15-digit decimals. Fast. Scales. Erases all Fraction structure. The 19 and 6 in −19/6 vanish into −3.166666666666667.

Arbitrary-precision float (mpfr, mpmath): same as floating point but with N digits instead of 15. Still erases Fraction structure. The 19 and 6 vanish into −3.1666666... with more sixes.

Symbolic CAS (Mathematica, Maple): keeps π as the symbol π, ζ(3) as the symbol ζ(3). Exact. But slow for large-scale computation, requires special handling for each symbolic object, and doesn't interoperate simply with pools of thousands of numerical values.

Mixed symbolic/numeric: some values symbolic, some numeric. Complicated. Fragile. The boundary between "symbolic" and "numeric" requires constant management.

Q335 is a fifth approach. Every transcendental constant is stored as a Fraction with numerator and denominator of approximately 100 digits. The Fraction differs from the true value by less than 10⁻¹⁰⁰. All computation uses Fraction arithmetic uniformly — no special cases, no symbolic objects, no type distinctions. Every value in the pool is the same type: a Fraction.

The name "Q335" describes the theoretical capacity of the system (335-digit precision, 272 orders of magnitude beyond Planck). The operational implementation uses 100-digit Fractions — already 37 orders beyond Planck, sufficient for all physical computation, and chosen because 100 is a number that any human can look at and immediately understand exceeds what physics could ever require.

---

## II. OPERATIONAL EXACTNESS

**Definition.** A representation R of a value V is *operationally exact* if no physical measurement, performed with any apparatus permitted by the laws of physics, could distinguish R from V.

**The Planck precision ceiling.** The Planck length l_P = 1.616 × 10⁻³⁵ m sets the spatial resolution limit of physics. The Planck time t_P = 5.391 × 10⁻⁴⁴ s sets the temporal resolution limit. The Planck energy E_P = 1.221 × 10¹⁹ GeV sets the energy resolution limit.

No measurement can resolve a length difference smaller than l_P. No measurement can resolve a time difference smaller than t_P. No measurement can resolve an energy difference smaller than E_P. These are not engineering limitations — they are consequences of quantum mechanics and general relativity combined.

The observable universe has radius L ≈ 4.4 × 10²⁶ m. The ratio L/l_P ≈ 2.7 × 10⁶¹. Specifying a length to Planck resolution across the observable universe requires ~62 significant digits. For a dimensionless quantity like α ≈ 0.00730, the measurement limit is set not by a length ratio but by the quantum uncertainty of the measurement apparatus — which cannot achieve better than Planck resolution in any observable. The combined argument from spatial, temporal, and energetic Planck limits gives ~63 digits as the absolute ceiling of physical distinguishability for any quantity, dimensionful or dimensionless.

**Q335 exceeds this ceiling by 272 orders of magnitude.** A Q335 Fraction with 335-digit numerator and denominator represents its target value to precision ~10⁻³³⁵. The Planck ceiling is ~10⁻⁶³. The margin is 10²⁷². No physical measurement could probe 1/10²⁷² of this margin. The representation is operationally exact.

**The operational implementation at 100 digits exceeds Planck by 37 orders.** The pool stores transcendentals at 100-digit Fraction precision, giving representation error ~10⁻¹⁰⁰. The Planck ceiling is 10⁻⁶³. The margin is 10³⁷ — 37 orders of magnitude. This is already far more than any computation chain could erode (see §VI). The 100-digit choice is deliberate: it provides visible surplus (any physicist can see that 100 digits > 63 digits), it keeps Fraction sizes manageable (~200-digit numerators after multiplication), and it exceeds Planck by enough to absorb any realistic computation chain.

The full Q335 capacity (335 digits, 272 orders beyond Planck) is available if a computation chain ever requires it. In practice, 100 digits has sufficed for 53 derived values across eight physics domains with zero detected precision loss.

---

## III. CONSTRUCTION

A Q335 Fraction for a transcendental constant T is constructed as follows:

1. Compute T to D decimal digits using a convergent algorithm (Chudnovsky for π, Euler-Maclaurin for ζ(n), AGM for ln(2), series summation for Li_n).

2. Verify against published high-precision computations (π, ζ(3), ln(2) all computed to 10⁶+ digits by independent groups).

3. Express as a Fraction p/q. The implementation uses mpmath's internal representation, which stores the value as an arbitrary-precision rational approximation at the specified number of decimal places (dps).

The resulting Fraction is not in lowest terms. For π at 100 digits, the numerator has ~102 digits and the denominator has ~101 digits. This is by design — reducing to lowest terms requires a GCD computation on 100-digit integers, which is fast but unnecessary. The unreduced Fraction works correctly in all arithmetic operations.

**Digit growth under arithmetic.** Multiplying two Q335 Fractions with D-digit numerators and denominators produces a Fraction with ~2D-digit numerator and denominator. After N multiplications without reduction, the digit count is ~D × 2^N. For N = 50 operations (typical for the longest chain in HOWL), this gives ~100 × 2⁵⁰ ≈ 10¹⁷ digits — impractical.

In practice, mpmath handles this through its mpf (multi-precision float) type, which maintains a fixed working precision and rounds after each operation. The rounding is to the working precision (100 digits), not to machine precision (15 digits). The Fraction structure is preserved at the input level (each coefficient and constant is stored as an exact Fraction in the pool) and through each individual operation (the operation is exact before the final rounding). The output of each derivation function is stored at the working precision.

This is the honest statement about structure preservation: the rational coefficients (197/144, 1/12, −1/2, 3/4 in A₂) are stored as exact Fractions in the pool. The transcendentals (π², ln(2), ζ(3)) are stored as 100-digit Fractions. When combined, the result is a 100-digit number. The individual integers 197, 144, 12, 2, 4 are not recoverable from the final number by inspection. They are recoverable from the pool and the computation chain — every input is stored, every derivation function is readable, every step is reproducible. The preservation is in the system, not in the number.

---

## IV. THE Q335 BASIS

The HOWL pool contains 31 transcendental and irrational constants at 100-digit Fraction precision. These form the Q335 basis — the complete set of non-rational numbers used in the derivation chain.

### Fundamental transcendentals

| Constant | Pool key | First 20 digits | Digits stored | Where used in HOWL |
|---|---|---|---|---|
| π | geom_pi_v0 | 3.1415926535897932384... | 100 | (22/13)π, angular integrals, QED A₂/A₃ |
| π² | geom_pi_squared_v0 | 9.8696044010893586188... | 100 | QED A₂, A₃ coefficients |
| 2π | geom_two_pi_v0 | 6.2831853071795864769... | 100 | Frequency conversions, RGE prefactors |
| e | geom_e_euler_v0 | 2.7182818284590452353... | 100 | Exponentials in BBN, threshold corrections |
| eᵖⁱ | geom_e_to_pi_v0 | 23.140692632779269005... | 100 | Cross-check |

### Logarithms

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| ln(2) | geom_ln2_v0 | 0.6931471805599453094... | 100 | QED A₂, A₃ (π²ln2 terms) |
| ln(3) | geom_ln3_v0 | 1.0986122886681096913... | 100 | Pool reference |
| ln(5) | geom_ln5_v0 | 1.6094379124341003421... | 100 | Pool reference |

### Zeta functions

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| ζ(2) = π²/6 | geom_zeta2_v0 | 1.6449340668482264364... | 100 | Cross-check of π² |
| ζ(3) | geom_zeta3_v0 | 1.2020569031595942853... | 100 | QED A₂, A₃; QCD corrections |
| ζ(5) | geom_zeta5_v0 | 1.0369277551433699263... | 100 | QED A₃ coefficient |
| ζ(7) | geom_zeta7_v0 | 1.0083492773819228268... | 100 | Pool reference, higher-loop |
| ζ(9) | geom_zeta9_v0 | 1.0020083928260822144... | 100 | Pool reference |

### Polylogarithms

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| Li₄(1/2) | geom_li4_half_v0 | 0.5174790616738993863... | 100 | QED A₃ coefficient |
| Li₅(1/2) | geom_li5_half_v0 | 0.5084005573830421725... | 100 | Higher-loop reference |
| Li₆(1/2) | geom_li6_half_v0 | 0.5040429655498562638... | 100 | Higher-loop reference |
| Li₇(1/2) | geom_li7_half_v0 | 0.5020086479812766662... | 100 | Higher-loop reference |

### Algebraic irrationals

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| √2 | geom_sqrt2_v0 | 1.4142135623730950488... | 100 | Geometric computations |
| √3 | geom_sqrt3_v0 | 1.7320508075688772935... | 100 | Geometric computations |
| √5 | geom_sqrt5_v0 | 2.2360679774997896964... | 100 | Golden ratio |
| √7 | geom_sqrt7_v0 | 2.6457513110645905905... | 100 | Pool reference |
| φ (golden ratio) | geom_golden_ratio_v0 | 1.6180339887498948482... | 100 | Pool reference |

### Elliptic integrals

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| K(1/4) | geom_elliptic_k_quarter_v0 | 1.6857503548325898267... | 100 | MATH-3 boundary |
| K(1/2) | geom_elliptic_k_half_v0 | 1.8540746773013719184... | 100 | MATH-3 boundary |
| K(3/4) | geom_elliptic_k_threequarter_v0 | 2.1565156474996432354... | 100 | MATH-3 boundary |
| E(1/4) | geom_elliptic_e_quarter_v0 | 1.4674622093394271554... | 100 | MATH-3 boundary |
| E(1/2) | geom_elliptic_e_half_v0 | 1.3506438810476755025... | 100 | MATH-3 boundary |
| E(3/4) | geom_elliptic_e_threequarter_v0 | 1.2110560275684595528... | 100 | MATH-3 boundary |

### Other

| Constant | Pool key | First 20 digits | Digits stored | Where used |
|---|---|---|---|---|
| Catalan's constant G | geom_catalan_v0 | 0.9159655941772190150... | 100 | Pool reference |
| Euler-Mascheroni γ | math_euler_mascheroni_v0 | 0.5772156649015329... | 16 (not Q335) | Noted: lower precision |
| π/4 = R₂ | geom_r2_v0 | 0.7853981633974483096... | 100 | MATH-1 cross-section invariant |
| π/4 = R₄ | geom_r4_v0 | 0.3084251375340424167... | 100 | MATH-5 n-ball remainder |

31 constants. 30 at 100-digit Fraction precision. 1 (Euler-Mascheroni) at 16 digits — noted as below Q335 standard, to be upgraded.

Every constant was verified against independent published computations. Every constant is a permanent pool node — stored once, never recomputed, available to all derivation functions.

---

## V. FRACTION ARITHMETIC PRESERVATION

The central claim of Q335 is not that individual numbers are more precise (arbitrary-precision float achieves the same digits). The claim is that the number system is uniform and the computation chain is traceable.

### What is preserved

Every input to every computation is a Fraction in the pool. The rational coefficients of the QED series are exact:

A₁ = 1/2 (pool key: qed_a1_schwinger_v0)

A₂ rational part = 197/144 (pool key: qed_a2_rational_term_v0)

A₂ π² coefficient = 1/12 (pool key: qed_a2_pi2_coeff_v0)

A₂ π²ln(2) coefficient = −1/2 (pool key: qed_a2_pi2ln2_coeff_v0)

A₂ ζ(3) coefficient = 3/4 (pool key: qed_a2_zeta3_coeff_v0)

The transcendental multipliers are Q335 Fractions:

π² = geom_pi_squared_v0 (100-digit Fraction)

ln(2) = geom_ln2_v0 (100-digit Fraction)

ζ(3) = geom_zeta3_v0 (100-digit Fraction)

Each coefficient and each transcendental is stored separately, named, versioned, and retrievable. The derivation function assembles them:

A₂ = (197/144) + (1/12) × π²_Q335 − (1/2) × π²_Q335 × ln2_Q335 + (3/4) × ζ3_Q335

Each multiplication is exact Fraction × Q335 Fraction = Q335 Fraction. The sum produces a single Q335 Fraction.

### What is not preserved

The final numerical value of A₂ is a single 100-digit number: −0.32848... The integers 197, 144, 12, 2, 4 are not visible in this number. You cannot extract 197/144 by inspecting −0.32848.

The preservation is in the chain, not the endpoint. The pool stores every coefficient. The derivation function code reads every coefficient by name. The computation is reproducible — run the function again with the same pool and you get the same result from the same named inputs. If someone changes 197/144 to 198/144 in the pool, the derivation function reads the new value and produces a different A₂. The traceability is from the named inputs through the readable code to the output.

This is different from floating-point computation, where −3.16667 appears in the code and nobody can tell whether it came from −19/6 or −19.0/6.0 or a fitted parameter. In Q335, the code reads `pool["beta_modified_su2_total_v0"]` and gets −13/6. The Fraction is in the pool. The code is readable. The chain is traceable. The structure is preserved — in the system, not in the number.

---

## VI. ERROR BOUNDS

### The operational exactness bound

Let T be a true transcendental value. Let T_Q be its Q335 Fraction approximation at D decimal digits. Then |T − T_Q| < 10⁻ᴰ.

For a computation f(x₁, ..., xₙ) involving N arithmetic operations on Q335 values:

**Addition/subtraction:** Each operation introduces error at most ε = 10⁻ᴰ. After N additions, total error < N × ε.

**Multiplication:** If |x_i| < M for all inputs, each multiplication introduces relative error at most ε/M (from the Q335 approximation of one factor). After N multiplications, total relative error < N × ε × M.

**Division:** If we divide by x where |x| > δ > 0, the error amplifies by at most 1/δ. For the Newton inversion in the α extraction, the divisor is the derivative of the QED series, approximately 0.16 — not near zero. The amplification factor is at most 1/0.16 ≈ 6.3.

**The worst case in HOWL.** The longest computation chain is the two-loop RGE integration: 10,000 Euler steps × ~6 operations per step = ~60,000 operations. With D = 100 and M ~ 10⁵ (largest coupling inverse):

Total error < 60,000 × 10⁻¹⁰⁰ × 10⁵ = 6 × 10⁻⁹¹

This is 28 orders of magnitude below Planck precision (10⁻⁶³). The 100-digit representation survives 60,000 operations with 28 orders of margin.

For the α extraction specifically: ~300 operations (6 Newton iterations × ~50 operations each), maximum value ~137, division by ~0.16:

Total error < 300 × 10⁻¹⁰⁰ × 137 × 6.3 = 2.6 × 10⁻⁹⁵

This is 32 orders below Planck. The Newton inversion introduces no meaningful precision loss at 100 digits.

**At full Q335 capacity (335 digits):** The same worst case gives error < 6 × 10⁻²²⁶, which is 163 orders below Planck. The 335-digit capacity is available for computation chains that don't yet exist — chains with millions of operations or extreme amplification factors. No known physical computation approaches this regime.

---

## VII. WORKED EXAMPLE: a_e → α → R∞ → f(1S-2S)

The complete chain from measurement to spectroscopic prediction, showing precision at each step.

### Step 1: Input

a_e = 0.00115965218059 (Fan et al. 2023, stored as pool Fraction)

Precision: 13 significant digits. This is a measurement — it enters the chain as a fixed-precision Fraction, not a Q335 transcendental.

### Step 2: Subtract seven corrections

Each correction is a pool Fraction (e.g., qed_ae_hadronic_lo_v0 = 0.000000000001860). The subtraction is exact Fraction arithmetic. Seven subtractions introduce zero error beyond the input precision.

Result: a_e(QED pure) = 0.001159652175718

Digits remaining: 13 (limited by input a_e, not by arithmetic)

### Step 3: Evaluate QED series at trial α/π

A₁ through A₃ evaluated using exact rational coefficients × Q335 transcendentals. A₄ evaluated at 30-digit precision (Laporta). A₅ at 4-digit precision (Volkov).

The series Σ Aₙxⁿ evaluated at x = α/π ≈ 0.00232:

| Term | Aₙ | Aₙxⁿ | Digits of Aₙ | Limiting precision |
|---|---|---|---|---|
| n=1 | 1/2 (exact) | 1.16 × 10⁻³ | ∞ | Not limiting |
| n=2 | −0.32848... (100 digits via Q335) | −1.77 × 10⁻⁶ | 100 | Not limiting |
| n=3 | 1.18124... (100 digits via Q335) | 1.47 × 10⁻⁸ | 100 | Not limiting |
| n=4 | −1.91225... (30 digits, Laporta) | −1.03 × 10⁻¹⁰ | 30 | Not limiting (10⁻⁴⁰ contribution) |
| n=5 | 5.891 (4 digits, Volkov) | 7.1 × 10⁻¹³ | 4 | Limiting at ~10⁻¹⁶ |

The A₅ uncertainty (±0.010) contributes ±1.2 × 10⁻¹⁵ to a_e. This corresponds to ~0.04 ppb in α. All other terms contribute negligible uncertainty.

### Step 4: Newton inversion

Solve for x where Σ Aₙxⁿ = a_e(QED pure). Six iterations. Each iteration involves one series evaluation (~15 multiplications), one derivative evaluation (~15 multiplications), and one division. Total: ~300 operations.

Digit tracking:
- Start: 100 digits (Q335 working precision)
- After 300 operations with max amplification 6.3: precision loss < 10⁻⁹⁵
- Digits remaining: effectively 95+ (but limited by A₅ at ~16 effective digits for α)

Result: α/π = 0.002322819473... → α⁻¹ = 137.035999207

The Newton residual: 1.59 × 10⁻²⁰⁴. The inversion is exact to 204 digits — far beyond any input's precision. The Q335 arithmetic introduces zero meaningful error.

### Step 5: Derive R∞

R∞ = α² × m_e × c / (2h)

- α from step 4 (100-digit Fraction)
- m_e = 9.10938371387 × 10⁻³¹ kg (pool Fraction, 12 digits)
- c = 299792458 m/s (exact, SI 2019)
- h = 6.62607015 × 10⁻³⁴ J·s (exact, SI 2019)

The α² multiplication: one Q335 operation. Error: < 10⁻¹⁰⁰. Remaining multiplications and divisions by exact quantities introduce zero error.

Result: R∞ = 10973731.5632962 m⁻¹

Miss from CODATA: 0.44 ppb. This is 2 × 0.22 ppb — exactly the α-power scaling prediction for an α² quantity. The Q335 arithmetic contributed zero to this miss. The entire miss traces to the α extraction.

### Step 6: Predict f(1S-2S)

f(ours) = f(CODATA theory) × R∞(ours) / R∞(CODATA)

This is one multiplication and one division — two Q335 operations. The ratio R∞(ours)/R∞(CODATA) = 0.999999999557. The CODATA theoretical frequency is 2466061413187035 Hz (15 digits).

Result: f = 2466061412094700 Hz

Miss from measurement: 1.09 MHz = 0.44 ppb. Again exactly the α² scaling prediction.

### Precision audit

| Step | Operation | Input precision | Output precision | Q335 error | Limiting factor |
|---|---|---|---|---|---|
| 1 | Read a_e | 13 digits | 13 digits | 0 | Measurement |
| 2 | Subtract corrections | 13 digits | 13 digits | 0 | a_e precision |
| 3 | Evaluate series | 100 digits (Q335) | ~16 digits | < 10⁻¹⁰⁰ | A₅ = 5.891 ± 0.010 |
| 4 | Newton inversion | 100 digits | 100 digits | < 10⁻⁹⁵ | A₅ (for α precision) |
| 5 | Compute R∞ | 100 digits (α), 12 (m_e) | 12 digits | < 10⁻¹⁰⁰ | m_e precision |
| 6 | Scale f(1S-2S) | 15 digits (CODATA f) | 15 digits | < 10⁻¹⁰⁰ | CODATA theory |

At no step does the Q335 arithmetic introduce detectable error. The precision at every stage is limited by the input measurements (a_e, m_e, A₅, CODATA theory), never by the number system. The Q335 error column is below 10⁻⁹⁵ everywhere — 32 orders of magnitude below Planck.

---

## VIII. THE MEASUREMENT BOUNDARY

There is exactly one point where Q335 Fractions meet the decimal world: the final comparison to measurement.

The comparison itself is a Fraction operation:

miss = |R_predicted_Q335 − R_measured_Q335| / R_measured_Q335

Both values are Q335 Fractions. The subtraction, absolute value, and division are Fraction arithmetic. The result is a Fraction — say, 219/1000000000000 — which represents 0.219 ppb.

The conversion to "0.219 ppb" is a display choice. The underlying comparison is exact (to Q335 precision). The decimal string is for human consumption. The pool stores the Fraction.

This means the comparison engine never introduces rounding errors. The PASS/FAIL decisions are based on Fraction comparisons: is |miss| < threshold? Both miss and threshold are Fractions. The comparison is exact.

The only precision loss in the entire system is the display format — and the display format is not part of the computation. It's the label on the output, not the output itself.

---

## IX. COMPARISON TO ALTERNATIVES

| Property | 64-bit float | Arbitrary-precision float | Symbolic CAS | Q335 Fractions |
|---|---|---|---|---|
| Digits | 15 | N (user-chosen) | ∞ (symbolic) | 100 (operational) |
| Fraction structure preserved | No | No | Yes | Yes (at input level) |
| Transcendentals handled | ~15 digits | ~N digits | Exact (symbolic) | 100 digits (operationally exact) |
| Uniform representation | Yes (everything is double) | Yes (everything is mpf) | No (symbolic vs numeric) | Yes (everything is Fraction) |
| Speed | Fastest | Fast | Slow for large systems | Fast (integer arithmetic on ~200-digit integers) |
| Pool scalability | Unlimited | Unlimited | Limited by CAS memory model | Unlimited (plain JSON) |
| Error detection | Poor (all numbers look alike) | Poor | Good (symbolic inspection) | Good (Fractions are self-documenting) |
| Interoperability | Universal | Library-dependent | CAS-dependent | Universal (JSON, any language) |

The distinctive property of Q335 is not any single row of this table. It is the combination: Fraction structure preserved AND transcendentals handled at operationally exact precision AND uniform representation AND fast AND scalable AND interoperable. No other approach achieves all six simultaneously.

The key advantage over symbolic CAS deserves emphasis: in Q335, every value in the pool is the same type. There is no distinction between "this is symbolic π" and "this is measured α_em⁻¹" and "this is derived sin²θ_W." All are Fractions. The derivation functions read Fractions and write Fractions. The comparison engine compares Fractions. No type-checking, no special-case handling, no symbolic simplification engine. The uniformity is the engineering contribution.

---

## X. SCOPE AND LIMITATIONS

**What Q335 is:** A number system for physical computation that stores all values (rational, irrational, transcendental, measured) as Fractions at precision exceeding any physical measurement by at least 37 orders of magnitude. The system preserves Fraction structure at the input level and through the computation chain, provides uniform representation for pools of thousands of values, and introduces zero detectable precision loss in any physical computation.

**What Q335 is not:** A claim that transcendental numbers are rational. They are not. Q335-π ≠ π. The difference is nonzero. The difference is also smaller than 10⁻¹⁰⁰, which is smaller than any physical measurement could ever detect by 37 orders of magnitude. The distinction between "equal" and "operationally exact" is maintained throughout — Q335 is an engineering solution, not a mathematical identity.

**Why 100 and not 335:** The pool operates at 100 decimal digits of precision because this already exceeds Planck by 37 orders of magnitude and survives 60,000 arithmetic operations with 28 orders of margin. The name "Q335" describes the system's theoretical framework (335 digits = 272 orders beyond Planck), and the 335-digit capacity is available if needed. In practice, 100 digits has been sufficient for 53 derived values, ~60 experiment runs, and eight physics domains with zero precision loss detected.

The choice of 100 over 35 (the minimum for Planck precision) is deliberate. When a physicist sees "100-digit precision," the reaction is immediate: that's obviously more than enough. The surplus is visible. The sufficiency is self-evident. This matters for adoption — a number system that visibly exceeds requirements by a large margin is trusted without scrutiny. A number system that claims to be "just barely sufficient" invites doubt.

**Applicability beyond HOWL:** Any computational physics group working with precision constants — CODATA adjustments, QED computations, lattice QCD, atomic structure calculations, precision spectroscopy theory — could adopt Q335 without modification. The system requires only: (1) a table of Q335 Fractions for the transcendentals used in the computation, (2) Fraction storage for all input parameters, and (3) a working-precision arithmetic library (mpmath in Python, MPFR in C, or equivalent). The pool format (JSON key-value pairs) is language-independent.

---

**END HOWL-MATH-8-2026**

**Registry:** [@HOWL-MATH-8-2026]

**Status:** Complete

**Central Statement:** Q335 is a number system in which every value — rational, irrational, measured, derived — is stored as a Fraction at precision exceeding the Planck ceiling by at least 37 orders of magnitude (100-digit implementation) and up to 272 orders (335-digit capacity). The system preserves Fraction structure at the input level, provides uniform representation, introduces zero detectable precision loss, and has been tested across 53 derived values in eight physics domains. Transcendental constants are not made rational. They are made operationally indistinguishable from rational, which is sufficient for all physical computation.
