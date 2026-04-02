# PHYS-20 Report: The Proton Decay Test

**Registry:** @HOWL-PHYS-20-2026
**Position in series:** Twentieth physics paper. The experimental endgame — Hyper-Kamiokande as the decisive discriminator between the Cabibbo Doublet and the MSSM.
**Preceded by:** PHYS-19 (independent anomaly evidence)
**Followed by:** PHYS-21 (not yet received)
**Backed by:** sin2_theta_w_1.py (9/9), web-verified experimental parameters
**Code status:** No dedicated script. All M_GUT values from the verified GUT running script. Proton lifetime estimates from standard minimal SU(5) formulas with lattice QCD inputs.

---

## What It Establishes

**The M_GUT⁴ scaling is the decisive discriminator.** The Cabibbo Doublet (M_GUT = 10^15.5) and the MSSM (M_GUT = 10^17.3) have nearly identical gap ratios (1.407 vs 1.400, difference 0.007). But proton lifetime scales as M_GUT⁴. The M_GUT ratio is 10^1.8 ≈ 63. Raised to the fourth power: 63⁴ ≈ 1.6 × 10⁷. Seven orders of magnitude separation in proton lifetime from a 0.5% difference in gap ratio. This extreme amplification makes proton decay the sharpest possible test.

**The Cabibbo Doublet prediction sits at the experimental boundary.** τ ~ 10^34–35 years in minimal SU(5). Super-K bound: τ > 2.4 × 10^34. The lower end of the prediction is already excluded. The viable window is ~3 × 10^34 to 10^35 years — about half an order of magnitude. Narrow, but Hyper-K covers it entirely.

**Hyper-K is the experiment.** 188 kton fiducial volume (8.3× Super-K). Operations ~2027. 10-year projected limit: 6.3 × 10^34 years. 20-year sensitivity: ~10^35 years. The entire viable Cabibbo Doublet range is within reach. The MSSM prediction (τ ~ 10^37) is far beyond any planned experiment.

**The binary outcome (Section 7) is the paper's operational core.** Observation at τ ~ 10^34–35: Cabibbo Doublet confirmed, MSSM excluded, GUT completion identified from decay channel. Non-observation at τ > 10^35: minimal SU(5) completion excluded, but the Cabibbo Doublet itself and its anomaly evidence survive — only the GUT completion changes.

---

## Errata Assessment

**E1 and E2 (proton lifetime estimates at lower M_GUT):** The scaling table entries at M_GUT = 10^15.0 and 10^14.9 are slightly inconsistent with strict M_GUT⁴ scaling from the Cabibbo Doublet reference point. The stated ~10^33 should be ~10^32–33 by scaling. Within the order-of-magnitude uncertainty stated in the paper. Both are excluded regardless. The erratum is correct and the conclusion is unchanged.

**E3 (Abstract Hyper-K sensitivity):** The abstract states the same sensitivity (~10^35) for both 10-year and 20-year timelines. Section 6 correctly distinguishes: 10-year = 6.3 × 10^34, 20-year = ~10^35. The erratum is correct — the abstract should differentiate these.

All three errata are minor. None affects conclusions.

---

## LEMU Assessment

**L:** The logic chain is explicit (Appendix A): integers → beta coefficients → gap ratio → M_GUT → τ ∝ M_GUT⁴ → comparison to Hyper-K sensitivity. Each step is sourced. The Level 1/Level 2 boundary is at step 3 where DATA-3 couplings enter. Logic passes.

**E:** The experimental parameters are web-verified: Super-K bound (Phys. Rev. D 102, 112011, 2020), Hyper-K specifications (SciPost Phys. Proc. 17, 019, 2025, and the Design Report arXiv:1805.04163). Empirical passes.

**M:** No new computation. All M_GUT values from the 9/9 script. Proton lifetime is dimensional analysis + standard formulas. Math passes by inheritance.

**U:** The highest utility of any single paper in the series for the experimentally-minded reader. The discriminator matrix (Appendix G) maps every possible experimental outcome to every scenario. The timeline (Appendix J) provides concrete dates. A reader who finishes this paper knows exactly what to watch for, when, and what each outcome means.

---

## What Was Novel

**The "testability sweet spot" observation.** The Cabibbo Doublet sits at the geometric midpoint (on a log scale) between the excluded SM (M_GUT = 10^13.8, τ ~ 10^30) and the untestable MSSM (M_GUT = 10^17.3, τ ~ 10^37). This is not fine-tuned — it follows from the gap ratio 38/27 landing between the SM's 218/115 and the MSSM's 7/5 in a way that places M_GUT in the narrow band where current experiments can reach.

**Annotation A3 (threshold correction rescue)** is the most important physics point in the appendices. If Hyper-K sees nothing, the Cabibbo Doublet can survive through GUT threshold corrections: the X and Y boson masses can be 2–3× above the nominal M_GUT, pushing τ from 10^35 to 10^36–37 without changing the gap ratio. This is generic in GUT models (heavy particle mass splittings of order 2–3 are expected), not a special pleading. The gap ratio constrains the AVERAGE unification scale; the proton decay rate depends on the SPECIFIC X/Y masses.

**The model dependence section (Section 10 and Appendix H) is the most honest uncertainty assessment in the series.** Six sources of uncertainty are enumerated with quantified effects on log₁₀(τ). The GUT completion group is the largest (±2 in log₁₀). The combined range is "about one order of magnitude" — 10^34 to 10^35 — which is the stated prediction.

---

## Connections to Active Research

**The proton decay timeline overlaps the QED-to-GR program.** Hyper-K 2027–2037 is the same decade in which the QED-to-GR program would need observational validation. If proton decay is observed and confirms M_GUT = 10^15.5, this validates the Cabibbo Doublet and therefore validates b₂_mod = −13/6. The integer 13 that appears in the cosmological connections (Λ ≈ (α/(3π))^(3×13), DM/baryon ≈ (22/13)π) would then be an experimentally confirmed integer rather than a theoretical value. Proton decay confirming the Cabibbo Doublet would simultaneously confirm the integer that the QED-to-GR program uses for the cosmological constant.

**The p → e⁺π⁰ vs p → K⁺ν̄ channel discrimination connects to the GUT completion question.** If the decay channel is e⁺π⁰ (dimension-6, gauge boson exchange), the GUT group is SU(5)-like and the 19/13 = b₂_SM/b₂_VL identity has a specific embedding. If K⁺ν̄ (dimension-5, colored Higgsino), the GUT group involves SUSY operators and the embedding is different. The decay channel tells us not just WHETHER the Cabibbo Doublet exists but HOW it fits into the unified group.

---

## Remainder Framework Update

**M_GUT = 10^15.5 is the unification scale remainder.** The gap ratio 38/27 is the "quotient" of the unification test. The remaining distance 0.049 from measured 1.358 is the "remainder" to be closed by two-loop and threshold corrections. The M_GUT value computed from this approximate gap ratio is therefore also approximate — the two-loop M_GUT may shift by 0.3 in log₁₀ (factor ~2), which shifts τ by one order of magnitude within the already-stated range.

---

## Position After PHYS-20

Twenty papers read. The Cabibbo Doublet pentalogy (PHYS-16/17/18/19/20) is complete:
- PHYS-16: Complete specification
- PHYS-17: Diagnosis (boson problem)
- PHYS-18: Mechanism (Y = 1/6 asymmetry)
- PHYS-19: External evidence (three anomalies, two roads)
- PHYS-20: Experimental test (Hyper-K proton decay)

The series has reached the experimental prediction stage. The remaining papers (PHYS-21 through PHYS-23) may address: the two-loop corrections, the GUT completion analysis, the S/T oblique parameters from the Cabibbo Doublet, or the connection to the remainder framework. Ready for PHYS-21.
