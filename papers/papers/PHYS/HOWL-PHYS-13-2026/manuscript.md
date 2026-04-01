# Gauge Coupling Unification and Minimal BSM Content
## 218/115 meets the universe.

**Registry:** [@HOWL-PHYS-13-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-6-2026] → [@HOWL-PHYS-7-2026] -> [@HOWL-PHYS-8-2026] -> [@HOWL-PHYS-9-2026] -> [@HOWL-PHYS-10-2026] -> [@HOWL-PHYS-11-2026] -> [@HOWL-PHYS-12-2026] -> [@HOWL-PHYS-13-2026]

**Date:** April 1 2026

**Domain:** Electroweak Physics, QED Coefficient Structure

**DOI:** 10.5281/zenodo.zzz

**Date:** April 1 2026

**Domain:** Gauge Unification, BSM Physics

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

The one-loop beta coefficients of the Standard Model are exact rationals determined by the gauge group and particle content: b₁ = 41/10, b₂ = −19/6, b₃ = −7. From these three numbers, a single rational — the gap ratio (b₁−b₂)/(b₂−b₃) = 218/115 = 1.896 — predicts whether the three gauge couplings converge to a unified value at high energy. The measured gap ratio from DATA-3 couplings is 1.358. The SM overshoots by 40%. The Standard Model does not unify.

A finite enumeration of 15 single-multiplet BSM extensions, verified by reproducing the known MSSM result (gap = 7/5 = 1.400, near-unification at M_GUT = 10^17.3 GeV, Δ(1/α₃) = −0.69), identifies one minimal solution: a vector-like quark doublet in the (3,2,1/6) representation — a single new particle with the quantum numbers of the left-handed quark doublet. Its gap ratio is 1.407 (distance 0.049 from measured), comparable to the full MSSM (distance 0.042), at M_GUT = 10^15.5 GeV on the proton decay boundary testable by Hyper-Kamiokande. No other single multiplet comes within 0.12 of the measured gap ratio.

The MSSM gap ratio 7/5 — a ratio of single-digit integers — is strikingly simpler than the SM's 218/115. This simplification is itself a measure of how much supersymmetry improves the unification structure. But the VL quark doublet achieves comparable unification quality with one new particle instead of dozens, demonstrating that the MSSM's unification success is not unique to supersymmetry.

---

## 1. Purpose

PHYS-5 computed the SM one-loop beta coefficients and noted the gap ratio 218/115. It never ran the couplings to M_GUT, never quantified the unification failure, and never asked what fixes it. PHYS-13 takes the PHYS-5 infrastructure and asks the GUT question for the first time in the series.

This is also the first HOWL paper with a BSM prediction. The vector-like quark doublet at M_GUT = 10^15.5 is testable by proton decay experiments.

---

## 2. The Three Couplings at M_Z

The three SM gauge couplings in the GUT normalization, extracted from DATA-3 Fractions:

α₁ = (5/3) × α_em / cos²θ_W. The 5/3 is the GUT normalization factor from the SU(5) embedding of hypercharge — it ensures that the U(1)_Y generator has the same normalization as the SU(2) and SU(3) generators when embedded in a single simple group.

α₂ = α_em / sin²θ_W. The standard SU(2)_L coupling.

α₃ = α_s. The QCD coupling, already in canonical normalization.

From the DATA-3 Fractions α_em = 1/137035999177 × 10⁹, sin²θ_W = 23122/100000, α_s = 1180/10000:

1/α₁(M_Z) = 63.2103 (U(1)_Y, GUT normalized)
1/α₂(M_Z) = 31.6855 (SU(2)_L)
1/α₃(M_Z) = 8.4746 (SU(3)_c)

Normalization check: sin²θ_W = (3/5)α₁/((3/5)α₁ + α₂) = 0.23122000, matching the input exactly. The GUT normalization is verified.

---

## 3. The Beta Coefficients

The one-loop beta function coefficients for the SM with 3 generations, 1 Higgs doublet, and GUT-normalized U(1):

b₁ = 41/10 = 4.100 (U(1)_Y, not asymptotically free)
b₂ = −19/6 = −3.167 (SU(2)_L, asymptotically free)
b₃ = −7 (SU(3)_c, asymptotically free)

Every integer in these coefficients traces to the gauge group structure and the SM particle content. The 41/10 counts the U(1) charges of all SM fermions and the Higgs doublet, weighted by their representations. The −19/6 counts the SU(2) gauge self-interaction (−22/3, from the Yang-Mills structure with C₂(SU(2)) = 2), the fermion contribution (+4/3 per doublet generation), and the Higgs contribution (+1/6). The −7 counts the SU(3) self-interaction (−11, from 11C₂(SU(3))/3 = 11), plus the quark contribution (+4 from 6 flavors at 2/3 each). These are verified by the MSSM gate check: adding the SUSY partner contributions to the SM betas reproduces the known MSSM values b₁ = 33/5, b₂ = 1, b₃ = −3.

The beta coefficients use the 6-flavor approximation (all quarks active throughout the running). Between M_Z = 91.2 GeV and m_t = 172.6 GeV, only 5 quark flavors are active, changing b₃ from −7 to −23/3. The fractional effect on the total running is approximately (Δb₃ × Δln)/(b₃ × ln_total) = (2/3 × 0.64)/(7 × 27.3) ≈ 0.2%, negligible compared to the 40% gap ratio miss.

---

## 4. The Gap Ratio

The gap ratio is the cleanest formulation of gauge coupling unification: a single rational number from the gauge group compared to a single measured number from the couplings.

**The SM prediction.** The gap ratio is (b₁ − b₂)/(b₂ − b₃):

b₁ − b₂ = 41/10 − (−19/6) = 246/60 + 190/60 = 436/60 = 109/15

b₂ − b₃ = −19/6 − (−7) = −19/6 + 42/6 = 23/6

Gap ratio = (109/15)/(23/6) = (109 × 6)/(15 × 23) = 654/345 = 218/115 = 1.8957

This is a pure rational determined entirely by the gauge group and particle content. No measured quantity enters.

**The measurement.** From the DATA-3 couplings at M_Z:

(1/α₁ − 1/α₂)/(1/α₂ − 1/α₃) = (63.2103 − 31.6855)/(31.6855 − 8.4746) = 31.5249/23.2109 = 1.3582

**The miss.** SM predicts 218/115 = 1.896. Measured: 1.358. The SM overshoots by 1.896/1.358 − 1 = 39.6%. The Standard Model does not unify at one loop.

The gap ratio test is equivalent to asking whether three lines (1/α_i plotted against ln μ) meet at a single point. The gap ratio is the ratio of slopes of the first pair of lines to the second pair. If all three meet, the slope ratio predicted from the beta coefficients must match the slope ratio measured from the coupling values. 218/115 ≠ 1.358 means the three lines do not meet.

---

## 5. Running to M_GUT

The one-loop running equation: 1/α_i(μ) = 1/α_i(M_Z) − b_i/(2π) × ln(μ/M_Z).

The sign convention: b₁ > 0 means α₁ increases with energy (1/α₁ decreases going up — U(1) is not asymptotically free). b₂ < 0 and b₃ < 0 mean α₂ and α₃ decrease with energy (1/α₂ and 1/α₃ increase going up — non-abelian gauge theories are asymptotically free).

**M_GUT from the α₁ = α₂ crossing.** Define M_GUT as the scale where 1/α₁ = 1/α₂:

ln(M_GUT/M_Z) = 2π × (1/α₁ − 1/α₂)/(b₁ − b₂) = 2π × 31.525/(109/15) = 27.258

M_GUT = 10^13.80 GeV.

**The couplings at M_GUT:**

1/α₁(M_GUT) = 1/α₂(M_GUT) = 45.423 (by construction)

1/α₃(M_GUT) = 38.843

Δ(1/α₃) = 1/α₃(M_GUT) − 1/α₁(M_GUT) = −6.581

α₃ is too strong at M_GUT. It hasn't weakened enough during the running to match the electroweak couplings. The strong coupling meets the energy scale where α₁ = α₂ with 1/α₃ still 6.58 units below 1/α₁ = 1/α₂. The three couplings fail to converge.

---

## 6. The sin²θ_W Prediction from 3/8

In SU(5) grand unification, sin²θ_W = 3/8 at M_GUT. This follows from the embedding of the SM gauge groups into SU(5): the ratio of U(1) to SU(2) generators gives sin²θ_W = 3/(3+5) = 3/8. The 3 and 5 are the dimensions of the SU(3) and SU(2) representations in the fundamental 5 of SU(5).

Running sin²θ_W from 3/8 at M_GUT down to M_Z with SM beta functions gives sin²θ_W(M_Z) ≈ 0.208 (the textbook result from the forced-unification computation). The measured value is 0.23122. The miss is approximately 10%.

This test is equivalent to the gap ratio test, not independent of it. Both ask whether three lines meet at a point. The gap ratio tests the slopes. The sin²θ_W prediction tests the intercepts. If one fails by 40%, the other fails by ~10%. The gap ratio is the cleaner formulation: a ratio of exact rationals (218/115) compared to a measured number (1.358), with no correction terms obscuring the integer content.

The relation between the two tests is made explicit by the linear formula (from the sin²θ_W notebook):

sin²θ_W(M_Z) = 3/8 − (109/72) × L_X / α_EM⁻¹(M_Z)

where L_X = ln(μ_X/M_Z)/(2π) and μ_X is the α₁ = α₂ crossing scale. The integer 109 appears as b₁ − b₂ in natural units (109/15 = b₁ − b₂) — the same integer that enters the gap ratio numerator as 218 = 2 × 109. The running of sin²θ_W from 3/8 and the gap ratio are controlled by the same integer.

---

## 7. MSSM Verification

Before enumerating general BSM content, the computation is verified against the known MSSM result.

The MSSM beta coefficients: b₁ = 33/5 = 6.600, b₂ = 1, b₃ = −3. These are known exact values from the complete SUSY partner spectrum (every SM fermion gets a scalar partner, every gauge boson gets a fermion partner, plus an additional Higgs doublet).

**MSSM gap ratio** = (33/5 − 1)/(1 + 3) = (28/5)/4 = 7/5 = 1.400. An exact rational. The simplification from the SM's 218/115 to the MSSM's 7/5 is striking — from a ratio of three-digit integers to a ratio of single-digit integers. This is itself a measure of how much supersymmetry simplifies the unification structure.

**MSSM running** (with SUSY threshold at M_Z as a simplifying approximation):

M_GUT = 10^17.32 GeV. ln(M_GUT/M_Z) = 35.37.

1/α₁(M_GUT) = 1/α₂(M_GUT) = 26.056. 1/α₃(M_GUT) = 25.363.

Δ(1/α₃) = −0.693. Unification quality: |Δ|/|1/α₁| = 2.66% miss.

This is the known result: the MSSM nearly unifies, with the remaining 2.7% closed by threshold corrections at M_GUT from the GUT-scale particles. The gate passes. The infrastructure reproduces established results.

---

## 8. The BSM Enumeration

For each candidate single multiplet in representation (R₃, R₂)_Y with either spin 0 (complex scalar) or spin 1/2 (vector-like fermion pair), the modified beta coefficients b_i + Δb_i are computed and the gap ratio (b₁+Δb₁−b₂−Δb₂)/(b₂+Δb₂−b₃−Δb₃) is compared to the measured 1.358. The beta function contributions Δb_i are hard-coded from published references (Martin's SUSY Primer, Langacker) and verified by the MSSM gate: the sum of all SUSY partner contributions reproduces b₁ = 33/5, b₂ = 1, b₃ = −3.

15 candidates tested. Results sorted by distance from measured gap ratio:

| Rank | Candidate | Gap | Dist | log₁₀ M_GUT | Status |
|---|---|---|---|---|---|
| 1 | Full MSSM | 1.4000 | 0.042 | 17.3 | safe |
| 2 | VL fermion (3,2,1/6) | 1.4074 | 0.049 | 15.5 | safe |
| 3 | SU(5) 5+5̄ fermion | 1.4815 | 0.123 | 14.9 | excluded |
| 4 | 3× Scalar (1,2,1/2) | 1.6308 | 0.273 | 14.1 | excluded |
| 5 | Scalar (3,2,1/6) | 1.6320 | 0.274 | 14.6 | excluded |
| 6 | Scalar (1,3,0) | 1.6640 | 0.306 | 14.4 | excluded |
| 7 | VL fermion (1,2,−1/2) | 1.7120 | 0.354 | 14.0 | excluded |
| 8 | 2× Scalar (1,2,1/2) | 1.7120 | 0.354 | 14.0 | excluded |
| 9 | Scalar (1,2,1/2) | 1.8000 | 0.442 | 13.9 | excluded |
| 10-15 | (remaining) | 1.95-2.27 | 0.59-0.91 | 12.3-13.7 | excluded |

The gap is dramatic. Only two candidates come within 0.05 of the measured ratio. Everything else is more than 2.5× further away. The separation between the top two and the rest is the main structural feature of the enumeration.

The proton decay boundary M_GUT > 10^15.5 GeV comes from Super-Kamiokande's limit on the p → e⁺π⁰ lifetime (τ > 2.4 × 10³⁴ years), which in minimal SU(5) translates to a lower bound on M_GUT. This limit is model-dependent — it assumes specific proton decay operators from the GUT completion, not just the unification scale. The VL quark doublet at M_GUT = 10^15.5 sits right at this boundary.

---

## 9. The Finding

A single vector-like quark doublet in the (3,2,1/6) representation achieves gauge coupling unification quality comparable to the full MSSM spectrum.

The representation (3,2,1/6) means: an SU(3) color triplet, an SU(2) weak doublet, with hypercharge Y = 1/6. The component fields have electric charges Q = T₃ + Y: the upper component has Q = 1/2 + 1/6 = +2/3 and the lower component has Q = −1/2 + 1/6 = −1/3. This is a vector-like copy of the left-handed quark doublet (u_L, d_L) — a particle that LHC searches can constrain directly.

Its beta function contributions: Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3. These shift the gap ratio from 218/115 = 1.896 to 1.407, a distance of 0.049 from the measured 1.358. The MSSM's distance is 0.042. The VL quark doublet is 17% further than the MSSM but achieves this with one new multiplet instead of the MSSM's dozens of particles.

Its M_GUT = 10^15.5 GeV. Hyper-Kamiokande, currently under construction in Japan with projected sensitivity to proton lifetimes of ~10^34.5 years (corresponding to M_GUT ~ 10^16), will test this prediction within its first decade of operation.

This does NOT mean the VL quark doublet is the correct BSM physics. Threshold corrections, two-loop effects, anomaly cancellation constraints, and direct search limits from the LHC all provide additional constraints not included in the one-loop gap ratio analysis. What the enumeration shows is that the MSSM's unification success is not unique to supersymmetry. The same gap ratio can be achieved with far less new content. The question of what nature chose between M_Z and M_GUT remains open — but the space of possibilities is now mapped at one loop.

---

## 10. The Integer Anatomy of Unification

The entire unification test reduces to comparing two rationals:

SM: (b₁ − b₂)/(b₂ − b₃) = 218/115 = 1.896

MSSM: (b₁ − b₂)/(b₂ − b₃) = 7/5 = 1.400

Measured from couplings: 1.358

The beta coefficients are exact rationals from the gauge group. The gap ratio is a ratio of rationals — itself a rational. The measurement is a ratio of inverse couplings. Unification is the statement: rational = measured. It fails for the SM and nearly succeeds for the MSSM.

This is the PHYS-2 thesis at the GUT scale. The transformation laws (beta functions) are integers determined by the gauge group and particle content. The coupling values (α₁, α₂, α₃ at M_Z) are measured numbers from the universe. Whether the integers predict unification depends on which integers — which particle content — nature chose between the electroweak scale and the GUT scale. The gap ratio is where these two classes of information meet: an integer prediction confronted with a measured value. 218/115 ≠ 1.358. The integers of the SM are not the integers of the universe above M_Z.

---

## 11. What PHYS-13 Seeds

Two-loop beta function corrections: known analytically, would shift each gap ratio by 2-5%. Could change the ranking of candidates or sharpen the VL quark doublet prediction.

Threshold corrections: particles entering at intermediate scales between M_Z and M_GUT change the effective beta coefficients in energy-dependent steps. The VL quark doublet's mass (unknown, but constrained by LHC to be above ~1-1.5 TeV) sets one such threshold.

Phenomenological constraints on the VL quark doublet: direct search limits from the LHC (current bounds around 1.3-1.5 TeV depending on decay mode), contributions to the electroweak precision parameters S and T (computable using the PHYS-12 infrastructure), and flavor-changing neutral current bounds.

The sin²θ_W prediction: if the gap ratio problem is solved (complete particle content determined), the linear formula sin²θ_W = 3/8 − (109/72) × L/α_EM⁻¹ immediately gives sin²θ_W as a derived parameter. The crossing scale L is determined by the particle content. This path is blocked by the same wall as the gap ratio — but solving one solves both.

---

## 12. What PHYS-13 Does Not Claim

Does not claim the VL quark doublet exists. The gap ratio at one loop is consistent with one, but threshold corrections, two-loop effects, and direct search constraints provide additional tests not included here.

Does not claim unification is proven. The gap ratio test is necessary but not sufficient. Full unification requires all three couplings to match at a single scale, not just the slope ratio.

Does not claim the MSSM is ruled out. The MSSM remains the best complete framework (gap 7/5 exact, threshold corrections close the 3% gap, dark matter candidate, hierarchy stabilization). The VL quark doublet is the minimal single-multiplet alternative, not a replacement.

Does not derive sin²θ_W. The gap ratio test and sin²θ_W prediction are equivalent. Neither reduces the parameter count from 17.

Does not account for two-loop running (2-5% effect) or the 6-flavor approximation (0.2% effect). Both are noted and smaller than the 40% gap ratio miss.

---

## 13. Summary

The gap ratio (b₁ − b₂)/(b₂ − b₃) distills gauge coupling unification into a comparison between a rational and a measurement. The SM rational is 218/115. The MSSM rational is 7/5. The measured value is 1.358. The SM fails by 40%. The MSSM succeeds to 3%. A single vector-like quark doublet succeeds to 3.6% with one new particle instead of dozens, at M_GUT = 10^15.5 testable by Hyper-Kamiokande.

The beta coefficients are integers from the gauge group. The gap ratio is a rational from those integers. The couplings at M_Z are measured values from the universe. The gap ratio is where integer structure meets measured reality, and the mismatch quantifies exactly how much new physics lies between M_Z and M_GUT.

---

*PHYS-13 is backed by one verified script: the GUT running + BSM enumeration (9/9 checks pass), with an additional sin²θ_W notebook recording the linear formula and its equivalence to the gap ratio. All numbers are sourced from DATA-3 Fractions. The sin²θ_W circularity bug in the original v0 script was identified, diagnosed, and resolved by dropping the circular computation in favor of the gap ratio formulation.*
