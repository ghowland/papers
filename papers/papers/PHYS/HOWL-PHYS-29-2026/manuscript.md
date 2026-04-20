# GUT Threshold Corrections — The Minimal SU(5) Limit
## The threshold coefficients are too small. Minimal SU(5) is disfavored.

**Registry:** [@HOWL-PHYS-29-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-13-2026] → [@HOWL-PHYS-21-2026] → [@HOWL-PHYS-24-2026] → [@HOWL-PHYS-25-2026] → [@HOWL-PHYS-26-2026] → [@HOWL-PHYS-27-2026] → [@HOWL-PHYS-28-2026] → [@HOWL-PHYS-29-2026]

**Date:** April 2 2026

**Domain:** GUT Completion, Threshold Corrections, Null Result

**DOI:** 10.5281/zenodo.19666420

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

**Backed by:** phys29_gut_thresholds.py (10/11 checks, 1 FAIL is the abort test firing), phys24_lib.py (21/21 self-test, 148/148 platform test)

---

## Abstract

The two-loop running of the gauge couplings with the Cabibbo Doublet modified betas leaves a residual unification miss Delta = −0.40 (PHYS-24, PHYS-28). This paper computes the GUT threshold corrections in minimal SU(5) that could close this residual. In minimal SU(5), the superheavy spectrum has three components: the X,Y gauge bosons defining M_GUT, the colored Higgs triplet T(3,1,−1/3) with beta shift db₃ = 1/12, and the Sigma field remnants — an (8,1,0) color octet with db₃ = 1/2 and a (1,3,0) weak triplet with db₂ = 1/3. The threshold correction to Delta is delta_Delta = −(1/12)ln(M_T/M_X)/(2π) − (1/6)ln(M_Sigma/M_X)/(2π). The combined coefficient C_total = −1/4. All coefficients are exact Fractions from representation theory. To close Delta = −0.40, even the best case (triplet and Sigma at the same mass below M_X) requires M_X/M = 23,228 — a mass splitting far beyond natural. The abort test fires: minimal SU(5) is disfavored as the GUT completion. The Cabibbo Doublet representation (3,2,1/6) and its Level 1 arithmetic survive intact — they are independent of the GUT completion. The proton lifetime prediction (10^34.5 yr) is unchanged.

---

## 1. The Two-Loop Residual

The gauge couplings of the Standard Model — the U(1) hypercharge coupling α₁, the SU(2) weak coupling α₂, and the SU(3) strong coupling α₃ — run with energy under the renormalization group equations. The inverse couplings 1/αᵢ evolve linearly at one loop and receive corrections at two loops from the 3×3 matrix bᵢⱼ. If the three gauge forces unify at a single scale M_GUT, all three inverse couplings meet at one point: 1/α₁ = 1/α₂ = 1/α₃ = 1/α_GUT.

The unification miss Delta = 1/α₃(M_GUT) − 1/α_GUT measures how far α₃ is from the crossing of α₁ and α₂ at M_GUT. Negative Delta means α₃ is too strong at the crossing — 1/α₃ is below the unification value.

The Cabibbo Doublet — a vector-like quark doublet in the (3,2,1/6) representation with modified betas (25/6, −13/6, −20/3) — improves unification at each perturbative order. At one loop with M_VL = 500 GeV, Delta = −1.17 (PHYS-24). At two loops with the SM b_ij matrix, Delta improves to −0.40, a 66% reduction (PHYS-24). Adding the VL two-loop b_ij corrections gives Delta = −0.436, a 63% improvement (PHYS-28).

The remaining Delta ≈ −0.40 must be closed by GUT threshold corrections — the effect of superheavy particles having different masses rather than all sitting exactly at M_GUT.

(Backed by phys29_gut_thresholds.py Section 1: Delta values from library.)

---

## 2. The Minimal SU(5) Heavy Spectrum

In minimal SU(5), the Standard Model gauge group SU(3)×SU(2)×U(1) emerges when SU(5) breaks at the GUT scale. The breaking is accomplished by a Higgs field in the 24-dimensional adjoint representation (the Sigma field) acquiring a vacuum expectation value. The superheavy spectrum has three components.

The X,Y gauge bosons: 12 gauge degrees of freedom in the (3,2,5/6) + conjugate representation. These acquire mass from the Sigma field VEV and define the GUT scale: M_X = M_GUT. They mediate proton decay through dimension-6 operators.

The colored Higgs triplet T(3,1,−1/3): a complex scalar from the fundamental 5 of SU(5). The 5 splits into a weak doublet (which becomes the SM Higgs) and a color triplet (which must be superheavy to avoid rapid proton decay). Its one-loop beta shifts are computed from the scalar Dynkin formulas of PHYS-26: db₁ = (1/5)×3×1×(1/9) = 1/15, db₂ = 0 (SU(2) singlet), db₃ = (1/6)×1×(1/2) = 1/12.

The Sigma field remnants: after the 24 adjoint breaks SU(5) → SM, 12 of its 24 real components become the longitudinal modes of the X,Y bosons (eaten by the Higgs mechanism). The remaining 12 components form three massive multiplets. The (8,1,0) color octet is a real scalar with 8 components. Its beta shift for SU(3) is db₃ = (1/6)×1×S₂(adj SU(3)) = (1/6)×1×3 = 1/2, where S₂(adj) = N = 3 for the adjoint of SU(3). The (1,3,0) weak triplet is a real scalar with 3 components. Its beta shift for SU(2) is db₂ = (1/6)×1×S₂(adj SU(2)) = (1/6)×1×2 = 1/3, where S₂(adj) = N = 2 for the adjoint of SU(2). The (1,1,0) singlet has no gauge interactions and contributes nothing to the betas.

(Backed by phys29_gut_thresholds.py S1: db₁_T = 1/15 EXACT, db₂_T = 0 EXACT, db₃_T = 1/12 EXACT.)

---

## 3. The Threshold Correction Formula

When the superheavy particles have different masses, the effective running between the lightest and heaviest superheavy scale uses different betas in different energy intervals, introducing a threshold correction to the unification prediction.

The correction to Delta has the form:

delta_Delta = C_T × ln(M_T/M_X)/(2π) + C_Sigma × ln(M_Sigma/M_X)/(2π)

where M_X is the X boson mass (defining M_GUT), M_T is the colored triplet mass, M_Sigma is the Sigma remnant mass, and C_T and C_Sigma are the effective threshold coefficients.

The triplet coefficient: C_T = −db₃_T = −1/12. The triplet shifts only the α₃ running (db₂_T = 0 means the α₁ = α₂ crossing is unaffected). If M_T < M_X, the triplet is active for a longer range, providing more correction to 1/α₃ at M_GUT.

The Sigma coefficient: C_Sigma = db₂_Sigma − db₃_Sigma = 1/3 − 1/2 = −1/6. This accounts for two effects: the (8,1,0) octet shifts α₃ running by db₃ = 1/2, and the (1,3,0) weak triplet shifts α₂ running by db₂ = 1/3, which shifts the α₁ = α₂ crossing point and hence 1/α_GUT. The net effect on Delta is the difference.

The combined coefficient: C_total = C_T + C_Sigma = −1/12 − 1/6 = −3/12 = −1/4. If both the triplet and the Sigma remnants are at the same mass M below M_X:

delta_Delta = −(1/4) × ln(M/M_X)/(2π)

All three coefficients (−1/12, −1/6, −1/4) are exact Fractions from the representation theory of SU(5). They are Level 1.

(Backed by phys29_gut_thresholds.py S2: C_T = −1/12 EXACT, C_Sigma = −1/6 EXACT, C_total = −1/4 EXACT.)

---

## 4. Closing the Residual — Three Cases

To close the two-loop residual Delta = −0.40, the threshold correction must provide delta_Delta = +0.40. Since all threshold coefficients are negative, this requires ln(M/M_X) < 0, meaning the heavy scalars must be LIGHTER than the X bosons.

**Case 1: Triplet only** (Sigma at M_X). C = −1/12. Required: −(1/12) × ln(M_T/M_X)/(2π) = 0.40. Solving: ln(M_T/M_X) = −0.40 × 24π = −30.2. The ratio M_X/M_T = e^30.2 = 1.25 × 10¹³.

**Case 2: Sigma only** (triplet at M_X). C = −1/6. Required: ln(M_Sigma/M_X) = −0.40 × 12π = −15.1. The ratio M_X/M_Sigma = 3.5 × 10⁶.

**Case 3: Both at same mass.** C = −1/4. Required: ln(M/M_X) = −0.40 × 8π = −10.1. The ratio M_X/M = 23,228.

All three cases require mass ratios far exceeding the naturalness threshold of 10 and far exceeding the fine-tuning threshold of 100. Even the best case (both at the same mass, maximizing the combined coefficient) requires a factor of 23,000 between the X boson mass and the scalar masses.

(Backed by phys29_gut_thresholds.py Section 3: all three cases computed.)

---

## 5. Why the Coefficients Are Small

The fundamental limitation is structural. The threshold coefficients C = −1/12, −1/6, −1/4 are small fractions. They are small because they involve the Dynkin indices of fundamental and adjoint representations of SU(2) and SU(3) — numbers of order 1/2 to 3 — divided by the scalar counting factors (1/6 for real scalars, 1/12 for complex scalars in the effective coefficient). The formula delta_Delta = C × ln(M/M_X)/(2π) divides by an additional factor of 2π ≈ 6.28, giving an effective coefficient C/(2π) ≈ 0.01 to 0.04.

To produce delta_Delta = 0.40 from an effective coefficient of 0.04, the logarithm must be ~10, corresponding to a mass ratio of ~e^10 ≈ 22,000.

This is a property of minimal SU(5) specifically. A GUT completion with larger representations (higher Dynkin indices), more heavy particles (cumulative effect from multiple thresholds), or intermediate-scale breaking (additional running segments) could have larger effective coefficients. The threshold correction scan in the script confirms: even M_X/M = 500 provides only delta_Delta = 0.082 against the required 0.40.

---

## 6. The Null Result

The abort test stated in PHYS-25 was: "If exact unification requires M_T/M_X > 100, the minimal SU(5) completion is disfavored." The best case gives M_X/M = 23,228. The abort test fires.

**Minimal SU(5) is disfavored as the GUT completion for the Cabibbo Doublet framework.**

What survives:

The Cabibbo Doublet (3,2,1/6) and all its Level 1 arithmetic. The beta shifts (1/15, 1, 1/3), the gap ratio 38/27, the modified betas (25/6, −13/6, −20/3), and all integers derived from them (13, 20, 22, etc.) are independent of the GUT completion. They are determined by the representation under SU(3)×SU(2)×U(1), not by the embedding into a larger group.

The two-loop improvement (66%). The SM b_ij matrix is measured and model-independent. The VL b_ij contribution depends only on the CD representation, not on the GUT.

The proton lifetime prediction. The X boson mass M_X = M_GUT ≈ 10^15.4 GeV is set by the coupling crossing, which depends on the CD one-loop betas (Level 1) and the measured couplings (Level 2). It is unchanged by the threshold finding. The proton decay channel p → e⁺π⁰ mediated by X boson exchange gives τ ~ M_X⁴/α_GUT² ~ 10^34.5 yr, above the Super-K bound of 2.4 × 10³⁴ yr and within the Hyper-K 20-year sensitivity of ~10³⁵ yr.

What is disfavored:

The specific claim that minimal SU(5) — with only the 5 (Higgs) and 24 (Sigma) representations breaking SU(5) → SM — can achieve exact unification with natural mass splittings. The residual Delta = −0.40 requires threshold corrections beyond what these representations provide.

(Backed by phys29_gut_thresholds.py S4: abort test fires with M_X/M = 23,228.)

---

## 7. Alternative Pathways

Three classes of alternatives to minimal SU(5) could provide larger threshold corrections:

SO(10) or Pati-Salam intermediate stages: in SO(10), the breaking can proceed through SU(5)×U(1) or SU(4)×SU(2)×SU(2) intermediate groups. The additional heavy particles at the intermediate scale — leptoquarks, right-handed W bosons, additional Higgs multiplets — provide threshold coefficients from higher representations with larger Dynkin indices. The intermediate-scale running also changes the effective one-loop betas between M_intermediate and M_GUT, potentially reducing the residual Delta before thresholds are needed.

Extended Higgs sector: adding heavy scalar representations beyond the minimal 5 + 24 of SU(5) increases the cumulative threshold coefficient. Each additional representation contributes its own C term. A handful of carefully chosen representations could accumulate enough correction with natural mass splittings.

Higher perturbative orders: the three-loop beta function provides additional correction comparable in magnitude to the two-loop VL effect (~5% of one-loop Delta, per PHYS-28). If the three-loop correction goes in the right direction, it reduces the residual that the thresholds must close, easing the naturalness requirement.

This paper does not pursue these alternatives. They are staged for future investigation. The finding is that minimal SU(5) is insufficient. The alternatives are stated, not computed.

---

## 8. What This Paper Does Not Claim

This paper does not claim the Cabibbo Doublet is wrong. The CD is Level 1 arithmetic — its beta shifts, gap ratio, and derived integers are representation theory, not GUT model-building. The null result is about the GUT completion, not about the CD.

This paper does not claim gauge coupling unification is impossible. It claims exact unification in MINIMAL SU(5) requires unnatural mass splittings. Non-minimal completions with more heavy particles or intermediate-scale breaking may achieve natural unification.

This paper does not claim the threshold formulas are exact. The perturbative threshold correction is a leading-order result. Higher-order threshold corrections, the running of heavy particle masses, and Yukawa coupling effects introduce corrections at the few-percent level.

This paper does not claim the two-loop residual is precisely −0.40. This value comes from the PHYS-24 higher-order integrator. The PHYS-28 Euler integration gives −0.436. A more precise residual would change the required mass ratio but not the structural conclusion — the threshold coefficients are too small for natural splittings regardless of whether the residual is −0.35 or −0.45.

---

## 9. What This Paper Seeds

The null result redirects the unification completion program:

PHYS-30 (α_s prediction) proceeds unchanged. The α_s prediction uses the two-loop running with the threshold uncertainty as a systematic, not as a tuned parameter.

A future paper on SO(10) intermediate-scale breaking would compute the threshold coefficients for the extended heavy spectrum and test whether they achieve natural unification. This is the most promising alternative.

A future paper on the extended Higgs sector would enumerate heavy scalar additions to minimal SU(5) and compute cumulative thresholds.

The exact Fraction threshold coefficients (C_T = −1/12, C_Sigma = −1/6, C_total = −1/4) are published for any future computation requiring them. The Sigma remnant beta shifts (db₃ = 1/2 for the octet, db₂ = 1/3 for the weak triplet) are new results not in the PHYS-24 library and should be added to the platform for future use.

---

*PHYS-29: GUT Threshold Corrections. The minimal SU(5) limit. C_total = −1/4. M_X/M = 23,228. Abort test fires. 10/11 checks (1 FAIL is the abort test). Published April 2, 2026. This paper is never edited after publication.*

---

## Appendix A: The Minimal SU(5) Heavy Spectrum

| Particle | Representation | Type | DOF | db₁ | db₂ | db₃ | Role |
|---|---|---|---|---|---|---|---|
| X,Y bosons | (3,2,5/6) + conj | Vector | 12 | — | — | — | Define M_GUT |
| Triplet T | (3,1,−1/3) | Complex scalar | 6 | 1/15 | 0 | 1/12 | Higgs sector |
| Sigma (8,1,0) | Adjoint of SU(3) | Real scalar | 8 | 0 | 0 | 1/2 | Sigma remnant |
| Sigma (1,3,0) | Adjoint of SU(2) | Real scalar | 3 | 0 | 1/3 | 0 | Sigma remnant |
| Sigma (1,1,0) | Singlet | Real scalar | 1 | 0 | 0 | 0 | Sigma remnant |

---

## Appendix B: The Threshold Coefficients

| Coefficient | Formula | Value | Origin |
|---|---|---|---|
| C_T | −db₃_T | −1/12 | Triplet shifts α₃ only (db₂_T = 0) |
| C_Sigma | db₂_Sigma − db₃_Sigma | 1/3 − 1/2 = −1/6 | Octet shifts α₃, weak triplet shifts crossing |
| C_total | C_T + C_Sigma | −1/12 − 1/6 = −1/4 | Combined |
| C_T/(2π) | effective coefficient | −0.013 | Per unit ln(M_T/M_X) |
| C_Sigma/(2π) | effective coefficient | −0.027 | Per unit ln(M_Sigma/M_X) |
| C_total/(2π) | effective coefficient | −0.040 | Per unit ln(M/M_X) |

---

## Appendix C: The Three Cases — Closing Delta = −0.40

| Case | Active particle | C | Required ln | Required ratio M_X/M | Natural? |
|---|---|---|---|---|---|
| 1: Triplet only | T(3,1,−1/3) | −1/12 | −30.2 | 1.25 × 10¹³ | No |
| 2: Sigma only | (8,1,0) + (1,3,0) | −1/6 | −15.1 | 3.5 × 10⁶ | No |
| 3: Both at same mass | All | −1/4 | −10.1 | 23,228 | No |

Naturalness threshold: M_X/M < 10. Fine-tuning threshold: M_X/M > 100. All three cases exceed the fine-tuning threshold.

---

## Appendix D: Threshold Correction Scan

| M_X/M_T | ln(M_T/M_X) | delta_Delta | Delta_total |
|---|---|---|---|
| 1 | 0.000 | 0.000 | −1.172 |
| 2 | −0.693 | 0.009 | −1.163 |
| 3 | −1.099 | 0.015 | −1.157 |
| 5 | −1.609 | 0.021 | −1.150 |
| 10 | −2.303 | 0.031 | −1.141 |
| 20 | −2.996 | 0.040 | −1.132 |
| 50 | −3.912 | 0.052 | −1.120 |
| 100 | −4.605 | 0.061 | −1.111 |
| 200 | −5.298 | 0.070 | −1.102 |
| 500 | −6.215 | 0.082 | −1.089 |

Even M_X/M_T = 500 shifts Delta by only 0.082, from −1.172 to −1.089. The two-loop correction (shifting Delta from −1.17 to −0.40) does far more work than any natural threshold correction.

---

## Appendix E: What Survives and What Is Disfavored

| Item | Status | Reason |
|---|---|---|
| CD representation (3,2,1/6) | **Survives** | Level 1 arithmetic, independent of GUT |
| Beta shifts (1/15, 1, 1/3) | **Survives** | Dynkin formulas, independent of GUT |
| Gap ratio 38/27 | **Survives** | Exact Fraction, independent of GUT |
| Integers 13, 20, 22 | **Survive** | From modified betas, independent of GUT |
| Two-loop improvement (66%) | **Survives** | SM b_ij is model-independent |
| VL two-loop improvement (+4.6%) | **Survives** | From CD representation theory |
| M_GUT ≈ 10^15.4 GeV | **Survives** | From coupling crossing |
| τ_proton ~ 10^34.5 yr | **Survives** | From M_X⁴ scaling |
| Cosmological formulas | **Survive** | From integers 13, 20, independent of GUT |
| sin²θ_W ≈ 3/13 | **Survives** | From running, independent of GUT completion |
| Minimal SU(5) completion | **Disfavored** | M_X/M = 23,228 required |
| Natural GUT thresholds in min SU(5) | **Disfavored** | Coefficients too small |

---

## Appendix F: Verification Summary

| Check | Description | Status |
|---|---|---|
| S1 | Triplet db₁ = 1/15 | PASS (EXACT) |
| S1 | Triplet db₂ = 0 | PASS (EXACT) |
| S1 | Triplet db₃ = 1/12 | PASS (EXACT) |
| S2 | C_T = −1/12 | PASS (EXACT) |
| S2 | C_Sigma = −1/6 | PASS (EXACT) |
| S2 | C_total = −1/4 | PASS (EXACT) |
| S3 | Triplet-only needs M_T < M_X | PASS |
| S3 | Both-at-same-mass needs M < M_X | PASS |
| S4 | **Abort test: M_X/M < 100** | **FAIL (M_X/M = 23,228)** |
| S5 | M_GUT > 10¹⁵ | PASS |
| S5 | Proton lifetime above Super-K | PASS |
| **Total** | | **10 PASS, 1 FAIL** |

The single FAIL is the abort test firing — a physics result, not a script bug. The abort test was designed to fire when minimal SU(5) requires unnatural mass splittings. It fires correctly.

---

*Supporting appendices A through F for PHYS-29. Every threshold coefficient is exact. The null result is documented with full numerical support. The Cabibbo Doublet and all Level 1 arithmetic survive. Grand total across all scripts: 466/467 (1 FAIL is the PHYS-29 abort test).*

---
