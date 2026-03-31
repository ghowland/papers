# The Koide Constant Decomposes
## Generation Count and Amplitude in the Charged Lepton Mass Relation

**Registry:** [@HOWL-PHYS-8-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-5-2026] → [@HOWL-PHYS-7-2026] → [@HOWL-PHYS-8-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 2026

**Domain:** Foundational Physics / Lepton Mass Structure

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.5 Sonnet. 

---

## I. ABSTRACT

The Koide formula (1981) states that the three charged lepton masses satisfy (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3, confirmed to 0.0009% by current measurements. The constant 2/3 has remained unexplained for 45 years. This paper decomposes it.

For N equally-spaced objects on a circle in √(mass) space with modulation amplitude a, the mass ratio (Σm)/(Σ√m)² = (1 + a²/2)/N. This is a trigonometric identity valid for N ≥ 3, derived from two standard results: N equally-spaced cosines sum to zero, and the sum of their squares equals N/2. The identity is proven in Section III. The N = 2 case is degenerate — the double-angle cosines do not cancel — and the identity does not hold for N = 2.

The Koide constant 2/3 is this identity evaluated at N = 3 and a² = 2: the ratio becomes (1 + 2/2)/3 = 2/3. The denominator 3 is the number of charged lepton generations. The numerator 2 is the amplitude squared. Neither alone produces 2/3. Both contribute.

The amplitude a = √2 is equivalent to the Koide relation. It is not derived from a separate physical principle. The observation that a = √2 allows the parametrization to produce zero mass (when cos = −1/√2) provides physical motivation for why a² = 2 is natural, but this does not constitute an independent derivation. The amplitude carries content equivalent to the formula itself.

What is new in this paper: the general formula (1 + a²/2)/N for arbitrary N ≥ 3 and arbitrary amplitude a, the decomposition of the Koide constant into generation count and amplitude, and the computation of m_τ from m_e and m_μ in controlled-precision rational arithmetic. The predicted m_τ = 1776.97 MeV versus PDG 1776.86 ± 0.12 MeV — a tension of 0.91σ, consistent with the formula being exact.

What is assumed: the Koide formula itself — that the three charged lepton masses are equally spaced on a circle in √(mass) space. This is empirical. It is not derived here. Why √(mass) is the natural space, why the spacing is equal, and what determines the free parameters M and θ₀ remain open questions stated here, not hidden.

In the framework of this series ([@HOWL-PHYS-1-2026]), mass is inertia — resistance of a coherent pattern to disruption, not substance. The Koide formula is a geometric constraint on three vortex soliton inertias at maximum symmetry (120° spacing) on a circle. The free parameter count of the Standard Model reduces from 18 (after [@HOWL-PHYS-7-2026]) to 17, conditional on the formula being exact.

---

## II. THE KOIDE FORMULA

### 2.1 The Relation

Yoshio Koide proposed in 1981 that the three charged lepton masses satisfy:

(m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3

Using current PDG values (m_e = 0.51099895 MeV, m_μ = 105.6583755 MeV, m_τ = 1776.86 ± 0.12 MeV), the left side evaluates to 0.666661, deviating from 2/3 by 0.00092%. This deviation is 0.91σ given the measurement uncertainty on m_τ. The relation is consistent with being exact.

### 2.2 History

The formula has held for 45 years through multiple improvements in the measured value of m_τ. At every stage, the Koide ratio has remained within measurement uncertainty of 2/3. No measured improvement has moved the ratio away from 2/3. It is the most precise empirical mass relation in particle physics.

### 2.3 The Two Open Questions

Two questions have been open since 1981.

First: why does the formula hold? What principle constrains the three charged lepton masses to satisfy this relation? This question remains open. This paper does not answer it.

Second: given that the formula holds, why is the constant 2/3 rather than some other value? This paper answers this question by decomposing 2/3 into two contributions: the generation count (3) and the amplitude (a² = 2).

---

## III. THE GENERAL IDENTITY

### 3.1 The General Parametrization

Consider N objects with masses m_i parametrized as:

√m_i = M(1 + a · cos(θ₀ + 2πi/N))   for i = 0, 1, ..., N−1

where M > 0 is a scale parameter with dimensions of √(mass), a > 0 is a dimensionless modulation amplitude, and θ₀ is an orientation angle. The N objects are equally spaced at angular intervals of 2π/N on a circle in √(mass) space.

For N = 3 and a = √2, this is the standard Koide parametrization.

### 3.2 The Sum of Square Roots

Σ√m_i = M · Σ(1 + a · cos(θ₀ + 2πi/N)) = M · (N + a · Σcos(θ₀ + 2πi/N))

The sum of N equally-spaced cosines on a circle is zero for N ≥ 3:

Σ_{k=0}^{N-1} cos(θ + 2πk/N) = 0   for all N ≥ 3, all θ

This is a standard trigonometric identity. It follows from the fact that N equally-spaced unit vectors on a circle sum to the zero vector, and the cosine sum is the projection onto any axis.

**The N = 2 exclusion.** For N = 2: Σcos(θ + πk) = cos(θ) + cos(θ + π) = cos(θ) − cos(θ) = 0. The cosine identity does hold for N = 2. However, the cos² identity used below does not hold for N = 2, as shown in §3.4. The general formula is valid for N ≥ 3.

Therefore Σ√m_i = NM, and (Σ√m_i)² = N²M².

### 3.3 The Sum of Masses

Σm_i = M² · Σ(1 + a · cos(φ_i))²

where φ_i = θ₀ + 2πi/N. Expanding:

= M² · Σ(1 + 2a · cos(φ_i) + a² · cos²(φ_i))

= M² · (N + 2a · Σcos(φ_i) + a² · Σcos²(φ_i))

The linear cosine sum is zero (for N ≥ 3). The cos² sum requires evaluation.

### 3.4 The Sum of Cosines Squared

Using cos²(x) = (1 + cos(2x))/2:

Σcos²(θ + 2πk/N) = N/2 + (1/2) · Σcos(2θ + 4πk/N)

The second sum is N cosines equally spaced at intervals of 4π/N. For N ≥ 3, these are still equally spaced around the circle (the spacing 4π/N = 2 · (2π/N) corresponds to going around the circle twice, but the N points remain equally spaced modulo 2π). Therefore the sum is zero for N ≥ 3:

Σcos²(θ + 2πk/N) = N/2   for all N ≥ 3, all θ

**The N = 2 failure.** For N = 2: Σcos(2θ + 4πk/2) = cos(2θ) + cos(2θ + 4π) = 2cos(2θ). This does not equal zero — it depends on θ. The cos² identity fails for N = 2. The sum Σcos²(θ + πk) = cos²(θ) + cos²(θ + π) = cos²(θ) + cos²(θ) = 2cos²(θ), which depends on θ and does not equal N/2 = 1 except at θ = π/4. The N = 2 case is degenerate and excluded from the general formula.

### 3.5 The General Ratio

Substituting:

Σm_i = M²(N + 0 + a² · N/2) = M² · N · (1 + a²/2)

The ratio:

**(Σm) / (Σ√m)² = M² · N · (1 + a²/2) / (N²M²) = (1 + a²/2) / N**

This is valid for all N ≥ 3, all a > 0, all θ₀, and all M > 0. The free parameters M and θ₀ cancel completely.

### 3.6 The Koide Evaluation

For the Koide formula: N = 3, a = √2.

(1 + (√2)²/2) / 3 = (1 + 2/2) / 3 = (1 + 1) / 3 = 2/3

The constant decomposes:

- The denominator 3 is the generation count N
- The numerator 2 is 1 + a²/2 = 1 + 1 = 2, determined by the amplitude a = √2
- Together: 2/3

### 3.7 The Amplitude Question

The general ratio is (1 + a²/2)/N. For different amplitudes at N = 3:

| Amplitude a | a² | Ratio | Simplified |
|---|---|---|---|
| 1 | 1 | 3/2 / 3 | 1/2 |
| √2 | 2 | 2/3 | 2/3 ← Koide |
| √3 | 3 | 5/2 / 3 | 5/6 |
| 2 | 4 | 3/3 | 1 |

The value a = √2 is not determined by the generation count. It is an independent input. The general formula shows that 2/3 requires both N = 3 and a² = 2. Attributing 2/3 to the generation count alone would be an overstatement.

The amplitude a = √2 is equivalent to the Koide relation. Setting the ratio equal to 2/3 and solving: (1 + a²/2)/3 = 2/3 gives a² = 2. Conversely, a = √2 in the parametrization produces the Koide relation. The amplitude and the formula are two ways of stating the same constraint.

**Physical motivation for a = √2.** When a = √2, the factor (1 + √2 · cos(φ)) can equal zero — this occurs when cos(φ) = −1/√2, i.e., φ = 3π/4 or 5π/4. This means the parametrization can produce m_i = 0. For a < √2, all masses are strictly positive. For a > √2, some masses become negative (unphysical). The value a = √2 is the boundary between "all masses positive" and "some masses negative." It is the maximum amplitude for which the parametrization produces physical (non-negative) masses.

This is a structural observation about the parametrization's boundary. It explains why a = √2 is special — it is the critical amplitude. It does not constitute a derivation independent of the Koide formula, because the critical-amplitude property and the Koide relation are equivalent statements about the same constraint.

### 3.8 The Generalization Table

For a² = 2 (the Koide amplitude) at various N:

| N | Ratio 2/N | As fraction |
|---|---|---|
| 3 | 2/3 | 0.667 ← Koide (charged leptons) |
| 4 | 2/4 | 0.500 |
| 5 | 2/5 | 0.400 |
| 6 | 2/6 | 0.333 |
| 7 | 2/7 | 0.286 |

If a Koide-type relation (with a² = 2) holds for N species, the constant would be 2/N. This is a prediction conditional on the amplitude a² = 2 persisting for other N, which is not guaranteed.

---

## IV. THE ASSUMPTIONS

### 4.1 N = 3

The Standard Model has three generations of charged leptons. This is empirical. Why there are exactly three generations is an open question in particle physics. The number 3 enters the decomposition as the denominator of the Koide constant.

### 4.2 Equal Spacing

The three lepton masses are equally spaced on a circle — separated by 120° = 2π/3 in the parametrization. This is the maximum-symmetry arrangement for three objects on a circle, the unique arrangement invariant under the S₃ permutation group. The assumption is that nature selects the maximally symmetric configuration. This is plausible but not derived from a deeper principle in this paper.

### 4.3 √(Inertia) Space

The circle lives in √m space. This is empirical — the Koide formula works in √m and does not work in m or ln(m). No geometric or physical argument is provided here for why √(inertia) is the natural variable.

In the inertia framing ([@HOWL-PHYS-1-2026]), mass is inertia — resistance to disruption. The variable √(inertia) may be natural because energy enters quantum mechanical amplitudes as √E in the normalization of states. This is speculation stated as such.

### 4.4 The Amplitude a = √2

The amplitude a = √2 is equivalent to the Koide relation. It is the critical amplitude — the boundary between all masses being non-negative and some becoming unphysical. It contributes the numerator 2 to the Koide constant through (1 + a²/2) = 2.

The amplitude is not derived independently of the formula. It is the formula expressed as an amplitude constraint. Listing it as a separate "assumption" would obscure this equivalence. It is listed here as a component of the decomposition: the Koide formula is the conjunction of N = 3, equal spacing, √m space, and a = √2. The general identity (1 + a²/2)/N isolates what each component contributes.

### 4.5 Honest Summary

| Component | Status | Contributes to 2/3 |
|---|---|---|
| N = 3 | Empirical (generation count) | Denominator: 3 |
| Equal spacing | Assumed (maximum symmetry) | Enables the trigonometric identities |
| √m space | Empirical (formula works here) | Defines the circle on which spacing occurs |
| a = √2 | Equivalent to the formula | Numerator: 1 + a²/2 = 2 |

What is derived: the decomposition of 2/3 into these components and the general formula (1 + a²/2)/N.

What is not derived: why any of these components hold.

---

## V. THE COMPUTATION

### 5.1 The Quadratic

Setting the Koide ratio equal to exactly 2/3 and solving for m_τ:

Let s = √m_τ, A = √m_e + √m_μ, B = m_e + m_μ.

The Koide relation becomes (B + s²)/(A + s)² = 2/3. Cross-multiplying and rearranging:

s² − 4As + (3B − 2A²) = 0

This is a quadratic in s with coefficients determined entirely by m_e and m_μ. The solutions are:

s = 2A ± √(6A² − 3B)

The positive branch gives m_τ ≈ 1776.97 MeV. The negative branch gives m ≈ 3.32 MeV, which does not correspond to any known charged lepton.

### 5.2 Controlled-Precision Rational Arithmetic

The computation is performed in Python's Fraction class with controlled-precision simplification for square root evaluations. Newton's method for √x on Fractions doubles the bit-length at each iteration; simplification every 3 steps caps growth at approximately 40 significant digits.

The computation is controlled-precision rational arithmetic, not exact integer arithmetic. The prediction is exact algebra — m_τ is the root of a quadratic with rational coefficients. The numerical evaluation introduces controlled truncation bounded at 10⁻³⁷ in the Koide ratio (verified by recomputing the ratio with the predicted m_τ). The truncation is six orders of magnitude below the measurement precision.

### 5.3 The Result

| Quantity | Value |
|---|---|
| m_τ (Koide, exact 2/3) | 1776.97 MeV |
| m_τ (PDG) | 1776.86 ± 0.12 MeV |
| Difference | +0.11 MeV |
| Tension | 0.91σ |
| Direction | Prediction is above PDG central value |

The prediction is 0.91σ above the PDG central value. Future m_τ measurements moving upward would close the gap; moving downward would open it. At 0.91σ the prediction is comfortably consistent with measurement.

### 5.4 The Companion Script

The complete computation is provided as `koide_integer.py`, requiring Python 3.8+ with the fractions standard library module and mpmath (for verification only). All intermediate values are Fraction type. The script verifies the Koide ratio with measured masses, solves the quadratic, bounds the truncation error, and reports exploratory comparisons explicitly labeled as non-findings.

---

## VI. THE INERTIA FRAMING

In the framework of [@HOWL-PHYS-1-2026], mass is inertia — the resistance of a coherent pattern to disruption. The electron, muon, and tau are three vortex solitons in the charged lepton field. They share identical quantum numbers — charge, weak isospin, lepton number. They differ only in inertia. They are three copies of the same pattern at different scales.

The Koide formula in this framing is a geometric constraint on three soliton inertias. The constraint says: the three inertias are arranged on a circle in √(inertia) space at equal spacing (120°) with critical amplitude (a = √2). The generation count determines the denominator of the constant. The critical amplitude determines the numerator.

The equal-spacing condition is the maximum-symmetry arrangement for three objects on a circle — the unique arrangement invariant under permutation of the three objects. It is the same geometry as three quarks at 120° in color space inside a baryon. Whether the parallel between lepton inertia spacing and quark color spacing reflects a common geometric origin is an open question.

---

## VII. THE 2/3 IN TWO CONTEXTS

The rational 2/3 appears in two distinct contexts within this series.

**Context 1: The Koide constant.** (Σm)/(Σ√m)² = 2/3. Decomposed here as (1 + a²/2)/N = 2/3 at N = 3, a² = 2.

**Context 2: The subtracted vacuum polarization constant ([@HOWL-PHYS-5-2026] §III).** The Feynman parameter integral for the one-loop vacuum polarization produces the unsubtracted constant −5/3. Subtraction at q² = 0 removes −1, giving the subtracted constant −2/3. The per-fermion boundary constant is (2/3)/2 = 1/3.

Both contexts involve three fermion species. Both produce the rational 2/3. The Koide 2/3 decomposes into generation count and amplitude. The VP 2/3 arises from the Feynman parameter integral ∫₀¹ 6x(1−x)ln[x(1−x)] dx and subtraction.

Whether these share a common geometric origin is an open question. The 2/3 is a small rational — coincidence is plausible. A derivation connecting the Koide decomposition to the VP integral structure would be a significant finding. No such derivation exists. This observation is stated for future investigation, not claimed as a result.

---

## VIII. WHAT THIS PAPER DOES NOT CLAIM

This paper does not derive the Koide formula. The formula — that three charged lepton inertias are equally spaced on a circle in √(inertia) space with critical amplitude — is empirical and unexplained. The paper decomposes the constant within the formula. It does not explain why the formula holds.

This paper does not derive the amplitude a = √2 independently of the Koide relation. The amplitude is equivalent to the formula. The critical-amplitude observation (a = √2 is the boundary of non-negative masses) explains why a = √2 is physically special but does not derive it from a principle independent of the mass relation.

This paper does not claim that 2/3 follows from the generation count alone. The constant decomposes into two contributions: 3 from the generation count and 2 from the amplitude. Both are required. The general formula (1 + a²/2)/N makes this explicit.

This paper does not claim the general identity holds for N = 2. The cos² identity Σcos² = N/2 requires N ≥ 3. The N = 2 case is degenerate — the double-angle cosines do not cancel. The general formula is valid for N ≥ 3.

This paper does not claim the Koide formula applies to quarks. The quark masses do not satisfy the Koide relation as verified by direct computation.

This paper does not claim the near-coincidences M² ≈ m_proton/3 (0.35% off) or θ₀ mod 120° ≈ θ_Cabibbo (0.29° off) are findings. Both are noted as suggestive and explicitly labeled as inconclusive in the companion script.

This paper does not claim the 2/3 connection to the VP constant is explained. It is observed and stated as open.

---

## IX. THE PARAMETER REDUCTION

### 9.1 The Count

[@HOWL-PHYS-7-2026] established that θ_QCD = 0 is the ground state of the QCD vacuum, reducing the Standard Model free parameters from 19 to 18.

The Koide formula, if exact, determines m_τ from m_e, m_μ, and the constant 2/3 = (1 + a²/2)/N at N = 3, a² = 2. This reduces the free parameters from 18 to 17.

The reduction is conditional on the Koide formula being exact, which is an empirical proposition currently supported at 0.91σ. The reduction is falsifiable.

### 9.2 The Scorecard

| Parameter | Status | Paper | Method |
|---|---|---|---|
| θ_QCD | Derived (= 0) | PHYS-7 | Ground state of integer-topological system |
| m_τ | Derived (from m_e, m_μ) | PHYS-8 | Koide with constant (1+a²/2)/N = 2/3 |
| 17 remaining | Measured | — | — |

---

## X. FALSIFICATION CRITERIA

**F1.** If a future measurement of m_τ deviates from the Koide prediction (1776.97 MeV) by more than 3σ, the formula is not exact and the parameter reduction is not valid.

**F2.** If a fourth-generation charged lepton is discovered, the test is twofold. First: does the four-body ratio equal (1 + a²/2)/4? If yes with a² = 2, the generalization holds and the constant is 2/4 = 1/2. If the ratio is 1/2 but a² ≠ 2, the generation count contribution (denominator) generalizes but the amplitude does not. If the ratio is neither 1/2 nor any value of (1 + a²/2)/4, the equal-spacing assumption fails for N = 4.

**F3.** If the Koide formula is shown to follow from a symmetry or dynamical principle that does not involve the parametrization used here, the constant 2/3 may receive an independent derivation. This would not falsify the decomposition but would provide a deeper explanation.

**F4.** If the formula is shown to hold in a space other than √m with a different constant, the specificity of √m space would need revision.

**F5.** If the equal-spacing assumption is derived from a deeper principle — a symmetry of the lepton field, a property of the soliton boundary, or a constraint from the gauge group — the conditional status of the parameter reduction is upgraded to unconditional. This is the target for future work.

---

## XI. CONCLUSION

The Koide constant 2/3 decomposes into two contributions. The denominator 3 is the number of charged lepton generations. The numerator 2 comes from the amplitude a² = 2, which is equivalent to the Koide relation itself. Neither alone produces 2/3. Both are required. The general formula (1 + a²/2)/N, valid for N ≥ 3, makes the decomposition explicit and generalizes the Koide relation to arbitrary generation count and amplitude.

The decomposition resolves the second of the two open questions about the Koide formula. The constant is no longer an unexplained number — it is the generation count and the critical amplitude expressed as a ratio. The first question — why the formula holds, why equal spacing in √(inertia) space — remains open.

In the framework of this series, three charged leptons are three vortex solitons with the same boundary structure but different inertias, arranged at maximum symmetry on a circle. The constant 2/3 is the generation count and the critical amplitude encoded in that geometry. The parameter m_τ is determined by m_e, m_μ, and the structure of the circle: 18 → 17 free parameters, conditional on the formula being exact, currently supported at 0.91σ.

The Koide formula was proposed in 1981. After 45 years, the constant has its decomposition. The formula awaits its derivation.

---

## APPENDIX A: THE GENERAL IDENTITY — PROOF

**Theorem.** For N ≥ 3 objects with masses parametrized as √m_i = M(1 + a·cos(θ₀ + 2πi/N)), the ratio (Σm)/(Σ√m)² = (1 + a²/2)/N.

**Proof.**

Step 1. Σ_{k=0}^{N-1} cos(θ + 2πk/N) = 0 for N ≥ 3.

This follows from the geometric series: Σe^{i(θ + 2πk/N)} = e^{iθ} · (1 − e^{i2π})/(1 − e^{i2π/N}) = 0 since e^{i2π} = 1. The cosine sum is the real part. ∎ (for this step)

Step 2. Σ_{k=0}^{N-1} cos²(θ + 2πk/N) = N/2 for N ≥ 3.

Using cos²(x) = (1 + cos(2x))/2:

Σcos² = N/2 + (1/2)·Σcos(2θ + 4πk/N)

The second sum has terms equally spaced at intervals 4π/N. For N ≥ 3, these N points are equally spaced on the circle (they complete 2 full cycles, but the N points remain distinct and equally spaced modulo 2π when N ≥ 3). By Step 1 applied with angle 2θ and spacing 4π/N, the sum is zero. ∎ (for this step)

Note: For N = 2, the second sum is Σcos(2θ + 2πk) = 2cos(2θ) ≠ 0. The identity fails.

Step 3. Σ√m = M·(N + a·0) = NM. Therefore (Σ√m)² = N²M².

Step 4. Σm = M²·(N + 2a·0 + a²·N/2) = M²·N·(1 + a²/2).

Step 5. Ratio = M²·N·(1+a²/2) / N²M² = (1+a²/2)/N. ∎

**Corollary.** At a² = 2: ratio = 2/N. At N = 3, a² = 2: ratio = 2/3 (Koide). ∎

---

## APPENDIX B: THE AMPLITUDE TABLE

| Amplitude a | a² | Ratio at N=3 | Physical interpretation |
|---|---|---|---|
| 0 | 0 | 1/3 | All masses equal (lower Cauchy-Schwarz bound) |
| 1/√2 | 1/2 | 5/12 | Mild mass splitting |
| 1 | 1 | 1/2 | Moderate mass splitting |
| √2 | 2 | 2/3 | Koide — critical amplitude (masses can reach zero) |
| √3 | 3 | 5/6 | One mass negative (unphysical) |
| 2 | 4 | 1 | Upper bound — one mass dominates |

At a = √2, the parametrization satisfies 1 + a·cos(φ) = 0 when cos(φ) = −1/√2. This is the boundary: for a < √2, all masses are strictly positive; for a > √2, some factors (1 + a·cos) become negative, producing unphysical negative masses. The Koide amplitude a = √2 is the critical value — the maximum amplitude for which all masses are non-negative.

---

## APPENDIX C: THE COMPUTATION RESULTS

| Quantity | Value | Source |
|---|---|---|
| m_e | 0.51099895 MeV | CODATA (8 sig fig) |
| m_μ | 105.6583755 MeV | PDG (10 sig fig) |
| m_τ (PDG) | 1776.86 ± 0.12 MeV | PDG (6 sig fig) |
| m_τ (Koide) | 1776.97 MeV | Quadratic from exact 2/3 |
| Difference | +0.11 MeV | |
| Tension | 0.91σ | Prediction above central value |
| Koide ratio (measured) | 0.666661 | |
| 2/3 | 0.666667 | |
| Deviation | 0.00092% | |
| Truncation error | < 10⁻³⁷ | Controlled-precision bound |

Note on precision asymmetry: m_τ is known to 6 significant figures because the tau lifetime limits spectroscopic precision. m_e and m_μ are known to 8–10 figures. The asymmetry is physical.

---

## APPENDIX D: EXPLORATORY COMPARISONS (NON-FINDINGS)

| Comparison | Values | Proximity | Status |
|---|---|---|---|
| M² vs m_proton/3 | 313.9 vs 312.8 MeV | 0.35% | Suggestive, not exact. NOT A FINDING. |
| θ₀ vs Cabibbo angle | 132.7° vs 13.0° | 119.7° apart | NOT RELATED in standard convention. |
| θ₀ mod 120° vs Cabibbo | 12.7° vs 13.0° | 0.29° (2.2%) | Suggestive under mod 120°. NOT A FINDING. |
| Koide 2/3 vs VP constant 2/3 | Both 2/3 | Identical | Same rational, different contexts. OPEN QUESTION. |
| Second quadratic root | 3.32 MeV | Near light quark scale | No known particle. NOT A FINDING. |

---

## APPENDIX E: CAUCHY-SCHWARZ CONTEXT

For any N positive numbers x_i, the Cauchy-Schwarz inequality gives (Σx_i²)/(Σx_i)² ≥ 1/N, with equality iff all x_i are equal. Setting x_i = √m_i:

(Σm) / (Σ√m)² ∈ [1/N, 1)

For N = 3: the range is [1/3, 1). The Koide value 2/3 sits exactly at the midpoint:

(2/3 − 1/3) / (1 − 1/3) = 1/2

The midpoint of the allowed range. Under the general formula, 2/3 is the midpoint because a² = 2 sets (1 + a²/2) = 2, which maps to the geometric mean of the bounds. Whether the midpoint has significance beyond the amplitude being at the critical value is not established.

---

## APPENDIX F: SERIES PUBLICATION RECORD

| Paper | Registry | Key Result |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = π/4; Q = F · β · d² · Z across nine domains |
| MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs at 100 digits |
| MATH-3 | @HOWL-MATH-3-2026 | Extended basis: elliptic integrals, Borwein ζ(5), hierarchy |
| PHYS-1 | @HOWL-PHYS-1-2026 | Mass is inertia; soliton boundaries; three anomaly correlations |
| PHYS-2 | @HOWL-PHYS-2-2026 | Couplings run; transformation law is fundamental |
| PHYS-3 | @HOWL-PHYS-3-2026 | G never measured outside Earth's Hill sphere |
| PHYS-4 | @HOWL-PHYS-4-2026 | Boundary test program; classification; kill switch |
| PHYS-5 | @HOWL-PHYS-5-2026 | α_EM running in integer arithmetic; 0.02 ppm |
| PHYS-6 | @HOWL-PHYS-6-2026 | Confinement boundary two-face structure; four SM observables |
| PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0; the strong CP problem dissolves |
| **PHYS-8** | **@HOWL-PHYS-8-2026** | **Koide constant decomposes: (1+a²/2)/N; 18 → 17** |

---

**END HOWL-PHYS-8-2026**

**Registry:** [@HOWL-PHYS-8-2026]
**Status:** Complete
**Domain:** Foundational Physics / Lepton Mass Structure
**Central Result:** The Koide constant 2/3 decomposes as (1 + a²/2)/N evaluated at N = 3 (generation count) and a² = 2 (Koide amplitude); the general formula is a trigonometric identity valid for N ≥ 3
**Method:** Trigonometric identity for N equally-spaced objects on a circle; controlled-precision rational arithmetic for m_τ prediction; explicit separation of generation count contribution (denominator) from amplitude contribution (numerator)
**Key Findings:** General formula (1+a²/2)/N for arbitrary N ≥ 3 and amplitude a; the constant decomposes into two contributions neither of which alone produces 2/3; a = √2 is the critical amplitude equivalent to the Koide relation; m_τ predicted at 1776.97 MeV (0.91σ from PDG); parameter count 18 → 17 conditional on formula being exact
**Assumptions:** N = 3 (empirical), equal spacing (maximum symmetry), √(inertia) space (empirical), a = √2 (equivalent to the formula, not independently derived)
**Does Not Claim:** Derivation of the Koide formula itself; independent derivation of a = √2; validity of the identity for N = 2; applicability to quarks; VP 2/3 connection is proven
**Open Questions:** Why equal spacing in √(inertia) space; why √(inertia) and not another power; what determines M and θ₀; whether the VP constant 2/3 shares a common origin with the Koide constant 2/3
**Falsification:** Five specific criteria including m_τ deviation >3σ, fourth-generation test of both 2/N and amplitude persistence, and derivation of equal spacing from deeper principle
