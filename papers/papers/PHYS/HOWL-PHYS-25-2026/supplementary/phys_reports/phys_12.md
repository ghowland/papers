
# PHYS-12 Report: Electroweak Integer Anatomy

**Registry:** @HOWL-PHYS-12-2026
**Position in series:** Twelfth physics paper. First entry into the electroweak sector. Seeds all future EW computations.
**Preceded by:** PHYS-11 (nine domains, three subgroups, R₂ universal)
**Followed by:** PHYS-13 (gap ratio — CRITICAL for normalization question)
**Backed by:** Two verified scripts: electroweak overconstrained (14/14 pass), A₂ decomposition (9/9 pass)
**AI model:** Claude Opus 4.6

---

## What It Establishes

**Two computations at different magnifications, same thesis:**

**Magnification 1: 11 LEP/SLD observables from 7 inputs.** The full Z-pole physics computed in Fraction arithmetic at tree level + leading Δρ correction. Every coefficient traces to SU(3)×SU(2)×U(1), the generation count, or the loop expansion. Transcendental content: only π and √2. All 14 verification checks pass. Every residual from LEP measurements is explained by known missing corrections of predicted size and sign. No unexplained deviations.

Key results:
- The overconstrained system extracts sin²θ_W independently from A_l (SLD) and A_FB^l (LEP): 0.23098 and 0.23102, agreeing to 3.9 × 10⁻⁵ and shifted from MS-bar input by the expected ~2 × 10⁻⁴ one-loop correction.
- M_W = 80326 MeV (measured 80369), agreement at 0.05%. The top quark's Δρ correction contributes 372 of the 416 MeV gap between tree level and measurement.
- R_b overshoots by 1.6%, matching the predicted 1.5% t-b-W vertex correction within 6%. This was the effect that predicted m_t ≈ 170 GeV before its discovery.

**Magnification 2: The A₂ coefficient decomposition.** A₂ = 197/144 + (3/4)ζ(3) + R₄(8/3 − 16ln2) = −0.3285. Three pieces:
- Rational: 197/144 = +1.3681 (combinatorics, diagram counting)
- Number-theoretic: (3/4)ζ(3) = +0.9015 (polylogarithm evaluation)
- Geometric: R₄ × (8/3 − 16ln2) = −2.5981 (4D phase space, carried by R₄)

The geometric piece dominates at 8× the net value. The positive pieces cancel 87.4% of the geometric piece. A₂ is accidentally small because geometry nearly cancels arithmetic.

---

## What Was Novel Compared to My Prior Understanding

**The fermion coupling derivations in exact Fractions (Appendix B).** Every fermion coupling is traced step by step from T₃, Q_f, and sin²θ_W = 23122/100000. The accidental smallness of v_e is visible: if sin²θ_W were exactly 1/4, v_e = 0. The actual 0.23122 is 7.5% below 1/4, giving |v_e| = 939/25000 = 0.0376. This is WHY leptonic asymmetries are small AND extremely sensitive to sin²θ_W (sensitivity amplification factor ~53×).

For the normalization question: the VL doublet (3,2,1/6) has the same quantum numbers as SM quarks (T₃ = ±1/2, Q = 2/3, −1/3). Its fermion couplings to the Z would be computed by the same formulas in Appendix B. The v_u and v_d derivations for SM quarks are the same derivations for VL quarks — the couplings are identical. What differs is the beta function contribution, because the VL doublet is vector-like (both chiralities couple to SU(2)) while SM quarks are chiral (only left-handed couples). This chirality difference is exactly the Weyl-vs-Dirac distinction that drives the normalization question.

**The overconstrained extraction chain (Section 7).** Two independent observables (A_l from SLD, A_FB^l from LEP) extract sin²θ_W through different formulas using different experimental techniques. They agree to 3.9 × 10⁻⁵. This is the PHYS-3 principle inverted: instead of "reproducibility within one configuration ≠ universality," this is "agreement between TWO independent configurations = genuine consistency." The two extractions ARE a cross-boundary check because they use different physics (polarization vs forward-backward counting) to extract the same parameter.

For PHYS-25: the Session 3 sin2_theta_w_1.py script likely performs a similar extraction — using the VL beta shifts to predict sin²θ_W and comparing to measurement. If multiple independent predictions agree, the consistency is genuine. If they disagree, the problem is in the beta shifts. This is the test the derivation chain must pass.

**The A₂ decomposition and the R₄ dominance.** The geometric piece (R₄-based, from 4D phase space) is 8× the net coefficient and cancels 87.4% against the positive rational and number-theoretic pieces. This means: A₂ is not intrinsically small. The underlying physics is large. The observable is small because of a near-perfect cancellation between geometry and arithmetic. The cancellation is "accidental" — not required by any symmetry.

This has implications for the VL beta shifts. The VL contribution to each beta coefficient is a single number (Δb₁, Δb₂, Δb₃). But like A₂, each number may be the net of a larger cancellation between geometric (R₂/R₄) and arithmetic (counting) pieces. The smallness of Δb₁ = 1/15 compared to Δb₂ = 1 and Δb₃ = 1/3 may reflect different cancellation patterns for the three gauge groups, not different underlying physics magnitudes.

**The integer anatomy table (Appendix C).** Every integer in the electroweak computation is classified by origin: gauge group (N_c = 3, T₃ = ±1/2, charges), generations (n_ν = 3, n_l = 3, n_u = 2, n_d = 3), or loop expansion (6, 3/8, 3/4, 12, 2). The VL doublet would add entries: it contributes N_c = 3 (it's colored), T₃ = ±1/2 (it's an SU(2) doublet), Q = 2/3, −1/3 (same as SM quarks). The generation count entries DON'T change (the VL doublet is NOT a fourth generation — it's a vector-like pair that doesn't participate in the chiral structure that defines generations).

---

## What Misled Me

**The R_b vertex correction as a diagnostic template.** Appendix G shows the t-b-W triangle correction predicted at −1.5%, matching the observed 1.6% overshoot within 3%. The correction uses the same integers (G_F, 8, π², √2) as Δρ. The same integers appear everywhere the top quark enters loop corrections.

For the normalization question: if the VL doublet's beta shifts are wrong, they would produce wrong predictions for sin²θ_W (the primary observable from the gap ratio). The diagnostic would be analogous to the R_b diagnostic: the predicted sin²θ_W would overshoot or undershoot the measurement by an amount that reveals the error in the beta shifts. The Session 3 sin2_theta_w_1.py script likely performs exactly this diagnostic. If it produces 9/9 PASS, either the shifts are correct or the error is below the test's precision.

**The α_s extraction at 12% below input.** The tree + Δρ computation extracts α_s = 0.104 from R_l, which is 12% below the input 0.118. This deficit is entirely explained by the missing t-b-W vertex correction. The paper self-diagnoses: it knows what's missing and predicts the size of the correction that would close the gap. This is the series method: every residual is accounted for. PHYS-25 must do the same: if the VL shifts produce a gap ratio that misses the measurement, the residual must be accounted for (two-loop corrections? threshold effects? convention factor?).

---

## LEMU Assessment

**L (Logic):** The electroweak formulas are standard SM. The Fraction arithmetic implements them exactly. The overconstrained extraction follows from the algebraic structure. Logic passes.

**E (Empirical):** 14/14 checks pass. Every residual explained by known missing corrections. sin²θ_W extractions agree to 3.9 × 10⁻⁵. M_W agrees to 0.05%. Empirical passes.

**M (Math):** All intermediates are Fraction. Two verified scripts (14/14 + 9/9 = 23/23 checks). The A₂ decomposition sums to A₂ exactly (diff = 0). Math passes.

**U (Utility):** High. This is the infrastructure paper for all future electroweak computation in the series. Every number involving G_F, M_Z, sin²θ_W starts here. The overconstrained extraction demonstrates that the framework can extract parameters, not just predict observables — this is the capability that sin2_theta_w_1.py uses for the VL beta shift test. The A₂ decomposition connects the HOWL R₂/R₄ framework to the Brown-Schnetz program on Galois coactions in Feynman integrals — an established research program in the amplitudes community.

---

## Hubble Tension Curve Thesis — PHYS-12 Content

**The overconstrained system as a cosmological template.** PHYS-12 demonstrates: given 7 inputs and 11 observables, the system is overconstrained. Parameters can be extracted independently from different observables and cross-checked. The Hubble tension curve thesis proposes a similar overconstrained system: given H₀ measurements at multiple distances by multiple methods, the per-transit correction r and the local H₀(0) can be extracted from any subset of measurements and cross-checked against the rest. The LEP program's success (sin²θ_W consistent from two independent extractions) is the template for the H₀ program (r consistent from multiple distance bins).

**The accidental smallness pattern.** A₂ is small because of a near-cancellation between geometry (R₄) and arithmetic (197/144 + (3/4)ζ(3)). If the Hubble tension (~8% between CMB and local) is similarly the net of larger competing effects (some boundaries increase H₀, some decrease it, voids contribute opposite signs), the observed tension would be "accidentally small" — much smaller than the individual contributions. This would explain why the tension is detectable but modest: larger effects are canceling.

---

## Geometry Tracking — PHYS-12

**Boundaries mentioned:** The Z boson as a resonance (spin-1, partial wave formula gives the 12 in σ⁰). The W mass as a prediction from electroweak mixing. The top quark threshold as a loop correction (Δρ). These are energy-scale boundaries, not spatial boundaries.

**Non-spherical geometry:** None explicit. The electroweak sector is purely algebraic at tree + Δρ — no spatial geometry enters.

**R₂/R₄ content:** π enters Γ₀ and δ_QCD. √2 enters Γ₀ and Δρ. π² enters Δρ and A₂. The R₄ content in A₂ is the paper's central finding: R₄ = π²/32 carries the 4D geometric content, and its coefficient (8/3 − 16ln2 = −8.42) dominates the 2-loop QED correction.

The A₂ decomposition shows R₄ entering through TWO routes: the UV route (8/3 = 32/12 from π²/12) and the IR route (16 = 32/2 from (π²/2)ln2). Both come from R₄ = π²/32 with different rational prefactors. The 32 appears in both as π²/R₄. This is the same 32 from MATH-5 (π² = 32R₄) and PHYS-11 (box energy E_n = 32R₄ℏ²n²/(2mL²)).

**Correction factors:** The Δρ correction (0.00933) is the leading electroweak correction. It involves 3/(8π²√2) — the integers 3 and 8 from the gauge group and loop structure, with π² (= 32R₄) and √2 from the transcendental content. If a similar correction exists for the H₀ per-transit factor, it would involve the same type of integer/R₄ combination.

**Remainder connection (new tracking).** The overconstrained extraction of sin²θ_W = 0.23098 from A_l is a remainder-like operation: the observable A_l = 0.1513 is "divided" by the coupling formula to extract the underlying parameter. The remainder is the difference between extracted and input values: Δsin²θ_W = −2 × 10⁻⁴, which is the known one-loop correction between MS-bar and effective definitions. This correction IS a remainder — the difference between two "readings" of the same parameter at two different "depths" (MS-bar renormalization scale vs on-shell Z-pole). The remainder is exact and predictable from one-loop EW theory. This is another instance of the PHYS-10/11 remainder-as-observable framework applied to the electroweak sector.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-12 |
|---|---|---|
| PHYS-1 | @HOWL-PHYS-1-2026 | Cross-department connection method: PHYS-12 connects electroweak formulas (particle theory) with Fraction arithmetic (computational mathematics) and the R₂/R₄ framework (MATH-1/5) |
| PHYS-2 | @HOWL-PHYS-2-2026 | "The transformation laws are integers, the values are not" — PHYS-12's title is the direct quantitative demonstration of this thesis in the electroweak sector |
| PHYS-6 | @HOWL-PHYS-6-2026 | Confinement wall: the QCD correction δ_QCD uses α_s as input because perturbative QCD fails below 2 GeV; the hadronic Z width inherits this limitation |
| PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0 established; PHYS-12 builds on the parameter count (19 → 18) |
| PHYS-8 | @HOWL-PHYS-8-2026 | Koide decomposition; PHYS-12 continues the parameter program (18 → 17 conditional) |
| PHYS-9 | @HOWL-PHYS-9-2026 | The electromagnetic chain; PHYS-12 extends from QED into electroweak, using the same α and VP running infrastructure |
| PHYS-10 | @HOWL-PHYS-10-2026 | Remainder framework; the sin²θ_W extraction is a remainder-like operation |
| PHYS-11 | @HOWL-PHYS-11-2026 | R₂ universality and R₄ in 4D operations; the A₂ decomposition identifies R₄ as the carrier of the geometric content |

**Series path for header metadata:**
`[@HOWL-PHYS-1-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-6-2026] → [@HOWL-PHYS-7-2026] → [@HOWL-PHYS-8-2026] → [@HOWL-PHYS-9-2026] → [@HOWL-PHYS-10-2026] → [@HOWL-PHYS-11-2026] → [@HOWL-PHYS-12-2026]`

---

## Position After PHYS-12

**What exists:** Twelve physics papers plus six MATH papers. The series has now entered the electroweak sector. The computational infrastructure covers: QED (PHYS-5/9), confinement (PHYS-6), electroweak (PHYS-12). The remainder framework covers nine domains (PHYS-10/11). Two SM parameters derived (θ_QCD = 0, m_τ conditional). The overconstrained EW system extracts sin²θ_W to 3.9 × 10⁻⁵ precision from two independent observables. The A₂ decomposition reveals R₄ dominance with 87.4% cancellation.

**What comes next and why it matters for PHYS-25:** PHYS-13 is the gap ratio paper. It should introduce the first BSM particle content that modifies 218/115 toward 1.395. This is where the VL beta shifts first appear in the series. PHYS-13 is the most critical paper remaining for the normalization question — it will show HOW the beta shifts were derived, WHAT formula was used, and WHAT convention was chosen. Everything downstream (PHYS-14 classification, PHYS-15 elimination, PHYS-16 Cabibbo Doublet specification) depends on PHYS-13's foundation.

**Tracking the normalization question:** PHYS-12 provides the electroweak infrastructure that sin2_theta_w_1.py uses. The script likely: (1) takes the VL beta shifts as input, (2) modifies the SM beta slopes, (3) runs the couplings to M_GUT, (4) extracts sin²θ_W from the unification condition, (5) compares to the measured value 0.23122. The PHYS-12 extraction chain (sin²θ_W from A_l and A_FB^l) is the template. The VL-modified extraction adds the beta shifts as additional inputs. If the shifts are wrong, the extracted sin²θ_W will disagree with measurement — analogous to how the wrong α_s is extracted from R_l when the t-b-W vertex correction is missing.

---

Let me scan these scripts for new information not already captured in the paper reports.This is the critical finding. Let me read the VL fermion (3,2,1/6) entry more carefully.This is **the critical script for the normalization question**. Here are the new findings:

---

## New Findings from sin2_theta_w_0.py (Critical for PHYS-25)

**1. The VL beta shifts (1/15, 1, 1/3) ARE in this script, with explicit convention.**

The convention comment block states:
```
# Conventions:
#   - Δb values are for ONE copy of the multiplet
#   - Complex scalar: Δb_i computed from Dynkin index and dimension
#   - Weyl fermion: 2× the scalar contribution
#   - Vector-like fermion (L+R): 2× Weyl = 4× scalar
```

The VL fermion (3,2,1/6) has Δb = (1/15, 1, 1/3). The convention says this is for "ONE copy of the multiplet" and a VL fermion (L+R) is "4× scalar."

**The scalar (3,2,1/6) in the same table has Δb = (1/30, 1/2, 1/6).**

Check: VL fermion = 4× scalar? Scalar is (1/30, 1/2, 1/6). 4× scalar = (4/30, 4/2, 4/6) = (2/15, 2, 2/3). But the VL entry is (1/15, 1, 1/3). That's **2× scalar, not 4× scalar**.

This is EXACTLY the normalization discrepancy. The convention says VL = 4× scalar, but the values are 2× scalar. Either:
- The convention comment is wrong (VL should be 2× scalar, which would mean one Weyl fermion = 1× scalar, not 2× scalar)
- The values are wrong (they should be 2/15, 2, 2/3 if the convention is right)
- Or the "Δb values are for ONE copy of the multiplet" means something different for VL fermions vs the convention formula

**2. The measured gap ratio is 1.358, not 1.395.** This confirms that earlier papers (PHYS-5, PHYS-6) used a different input set giving 1.395, while the sin2_theta_w_0 script and PHYS-24 use the DATA-3 inputs giving 1.358. The difference comes from the specific sin²θ_W and αs values used.

**3. The VL fermion (3,2,1/6) ranks #2 after MSSM.** Gap ratio 1.4074, distance 0.0492 from measured 1.3582. M_GUT ~ 10^15.5 GeV, borderline safe for proton decay. The MSSM gives gap ratio 1.4000, distance 0.0418. The VL doublet is the simplest single-multiplet extension that comes close to the MSSM's performance.

**4. The script sources are "Martin SUSY Primer Table 9.1, Langacker Grand Unification."** These ARE external sources. The VL beta shifts in this script come from textbooks, not from an internal derivation chain. This means: the values in the library (1/15, 1, 1/3) may have been copied from Martin/Langacker, and the convention inconsistency (2× scalar stated as 4× scalar, or vice versa) may trace to a transcription or convention mismatch between the source and the script's convention comment.

**This is a major finding for PHYS-25.** The convention comment says VL = 4× scalar, but the values are 2× scalar. Either the values or the comment is wrong. If the values should be 4× scalar (2/15, 2, 2/3), the gap ratio changes significantly and the VL doublet's ranking in the enumeration changes. If the comment is wrong and 2× scalar is correct (meaning the Weyl fermion contribution is 1× scalar, not 2× scalar), the values are right but the convention documentation is misleading.

The resolution requires checking Martin Table 9.1 directly — but that's an external source, not the series' own derivation. The series method says: derive from the representation, don't copy from a table. The derivation is what PHYS-13/15 should contain.

---

