# Supporting Tables for Bessel Zero PSLQ (Path 4)

## Table 1: The Constants to Test

DATA-3 contains two Bessel zeros at 105 digits:

| Constant | Value (first 30 digits) | Q335 Numerator | Entry |
|---|---|---|---|
| j₁₁ (first zero of J₁) | 3.83170597020751231561443588630... | (no small factors, 102-digit cofactor) | #72 |
| j₀₁ (first zero of J₀) | 2.40482555769577276862163187932... | 2 × 5², 100-digit cofactor | #74 |

j₁₁ appears in every diffraction-limited optical system: the Airy disk radius is 1.22λ/D = (j₁₁/π)λ/D.

j₀₁ appears in cylindrical waveguide cutoff: the TE₀₁ mode cutoff is j₀₁c/(2πa).

Both are transcendental (Siegel 1929). Algebraic independence from π is expected but unproven.

## Table 2: The Transcendental Basis for PSLQ

The DISC-7 protocol tests whether a target constant x satisfies:

n₀x + n₁c₁ + n₂c₂ + ... + nₖcₖ = 0

for integer coefficients |nᵢ| ≤ maxcoeff, where c₁...cₖ are the basis constants. A null means no such relation exists at the tested precision and coefficient bound.

The extended basis from MATH-3/MATH-4 (all available as Q335 numerators):

| # | Constant | Q335 Numerator Available | Weight |
|---|---|---|---|
| 1 | π | Yes | Geometric (circle) |
| 2 | π² | Yes | Geometric (4D) |
| 3 | π³ | Yes | Higher geometric |
| 4 | π⁴ | Yes | Higher geometric |
| 5 | e | Yes | Exponential |
| 6 | ln(2) | Yes | Logarithmic |
| 7 | ln(3) | Yes | Logarithmic |
| 8 | ln(5) | Yes | Logarithmic |
| 9 | √2 | Yes | Algebraic |
| 10 | √3 | Yes | Algebraic |
| 11 | √5 | Yes | Algebraic |
| 12 | √7 | Yes | Algebraic |
| 13 | φ | Yes | Algebraic (= (1+√5)/2) |
| 14 | ζ(3) | Yes | Number-theoretic (weight 3) |
| 15 | ζ(5) | Yes | Number-theoretic (weight 5) |
| 16 | Li₄(1/2) | Yes | Polylogarithmic |
| 17 | Catalan G | Yes | L-function |
| 18 | γ (Euler-Mascheroni) | Yes | Harmonic series |
| 19 | e^π | Yes | Mixed exponential-geometric |
| 20 | 1 | Trivial | Rational offset |

## Table 3: PSLQ Protocol (from DISC-7)

| Parameter | Value | Rationale |
|---|---|---|
| Target precision | 100 digits | Q335 gives 101 digits, leave 1 digit margin |
| maxcoeff | 10,000 | Same as DISC-7, sufficient for non-trivial relations |
| Algorithm | PSLQ (Ferguson-Bailey) | Standard integer relation detection |
| Null criterion | PSLQ returns no relation at 100 digits with maxcoeff 10,000 |
| Positive criterion | PSLQ returns integer vector with max|nᵢ| ≤ 10,000 that zeroes the linear combination to 100 digits |

## Table 4: Tests to Run

| Test ID | Target | Basis | What It Tests |
|---|---|---|---|
| P1 | j₁₁ | {1, π, π², π³, π⁴} | Is j₁₁ a polynomial in π with small integer coefficients? |
| P2 | j₁₁ | {1, π, e, ln2, √2, √3, ζ(3)} | Is j₁₁ a linear combination of common transcendentals? |
| P3 | j₁₁ | Full 20-constant basis | Exhaustive test against the complete HOWL basis |
| P4 | j₀₁ | {1, π, π², π³, π⁴} | Same as P1 for j₀₁ |
| P5 | j₀₁ | {1, π, e, ln2, √2, √3, ζ(3)} | Same as P2 for j₀₁ |
| P6 | j₀₁ | Full 20-constant basis | Same as P3 for j₀₁ |
| P7 | j₁₁/π | {1, π, π², e, ln2, √2, ζ(3)} | Is the Airy constant 1.2197 a known combination? |
| P8 | j₁₁ − j₀₁ | {1, π, π², e, ln2, √2, ζ(3)} | Is the spacing between zeros a known combination? |
| P9 | j₁₁ × j₀₁ | {1, π, π², π³, π⁴, e, ln2, ζ(3)} | Is the product a known combination? |
| P10 | j₁₁² + j₀₁² | {1, π, π², π³, π⁴} | Is the sum of squares a polynomial in π? |

Tests P1-P6 are the core. P7-P10 probe derived quantities that might have simpler representations than the zeros themselves.

## Table 5: What's Known About Bessel Zeros

| Fact | Reference | Implication |
|---|---|---|
| j_νk is transcendental for all ν ∈ ℤ, k ≥ 1 | Siegel (1929) | Not algebraic |
| No closed form for j_νk in terms of elementary functions | — | Expected PSLQ null |
| McMahon expansion: j_νk ≈ (k + ν/2 − 1/4)π + O(1/k) | McMahon (1894) | j_νk is approximately a half-integer multiple of π for large k |
| j₁₁ ≈ 1.2197π | Numerical | Close to but not exactly a rational multiple of π |
| Rayleigh sum: Σ 1/j²_νk = 1/(4(ν+1)) | Rayleigh | Constraint on the zeros collectively, not individually |

The McMahon expansion shows that Bessel zeros are ASYMPTOTICALLY rational multiples of π (for large zero index k), but the first few zeros deviate significantly from the asymptotic formula. If j₁₁ were exactly a rational multiple of π, PSLQ test P1 would find it. The known value j₁₁/π = 1.2197... has CF = [1; 4, 1, 1, 1, 3, 31, ...] with no anomalous partial quotients (from DATA-2 continued fraction analysis).

## Table 6: Prior PSLQ Results (from DISC-6-8)

| Category | Tests Run | Results | Max Precision |
|---|---|---|---|
| SM parameters vs transcendental basis | 51 | 51/51 null | 4-12 digits |
| Residual PSLQ on α_s candidate | 5 | 5/5 null | 10 digits |
| Modular search | ~600 | Noise (controlled) | 4-12 digits |
| Optical clock ratios | 5 | 5/5 null | 15 digits |
| Mass ratios | 3 | 3/3 null | 8-11 digits |
| BCS gap ratio | 1 | 1/1 null | 10 digits |
| Feigenbaum constants | 2 | 2/2 null | 30 digits |
| **Total prior** | **~672** | **72/72 null** | |
| **Bessel zeros (this test)** | **10** | **?** | **100 digits** |

The Bessel PSLQ at 100 digits with maxcoeff 10,000 would be the highest-precision PSLQ in the series. The prior tests were limited by the measurement precision of the target constants (4-15 digits for SM parameters). The Bessel zeros are analytical constants computed to 105 digits, so PSLQ can run at full Q335 capacity.

## Table 7: Expected Results and What They Mean

| Outcome | Probability | Meaning |
|---|---|---|
| All 10 null | ~99% | Bessel zeros are algebraically independent of the HOWL basis. Extends 72/72 to 82/82. Confirms the basis is complete (no Bessel zero is expressible in terms of the existing constants). |
| One or more positive | ~1% | A new identity relating Bessel zeros to π, ζ values, or other basis constants. Would be a genuine mathematical discovery, publishable independently of HOWL. |

The 1% estimate is generous. No such identity is known or expected. But PSLQ at 100 digits with maxcoeff 10,000 has never been run on these specific targets, so we check.

## Table 8: Implementation Notes

Use mpmath's `pslq` function directly:

```python
from mpmath import pslq, mpf, pi, zeta, log, sqrt, euler, exp

mp.dps = 110  # extra margin beyond 100

# For test P3 (j11 vs full basis):
target = [j11, 1, pi, pi**2, pi**3, pi**4, 
          e, log(2), log(3), log(5),
          sqrt(2), sqrt(3), sqrt(5), sqrt(7),
          (1+sqrt(5))/2, zeta(3), zeta(5),
          catalan, euler, exp(pi)]

result = pslq(target, maxcoeff=10000)
# result is None → NULL (no relation found)
# result is list → POSITIVE (relation found, verify)
```

If any positive result is found, verify independently:
1. Check the claimed relation at 105 digits (not just 100)
2. Check with maxcoeff = 100,000 to see if a simpler relation exists
3. Compute the relation symbolically to confirm it's not a numerical coincidence

---

*These tables provide the protocol, basis constants, known mathematical context, and implementation details for the Bessel zero PSLQ search. 10 tests, ~30 minutes compute time, expected outcome: 10/10 null extending the HOWL independence result to 82/82.*
