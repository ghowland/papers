
# PHYS-4 Report: The Boundary Test Program

**Registry:** @HOWL-PHYS-4-2026
**Position in series:** Fourth physics paper. First structured test program.
**Preceded by:** PHYS-3 (G never tested outside Hill sphere)
**Followed by:** PHYS-5 (α_EM running in integer arithmetic — not yet received)
**Backed by:** No script. Program specification with decision tree.
**AI model:** Claude Opus 4.6

---

## What It Establishes

A structured test program connecting three prior results into a single investigation with a kill switch:

**The connection.** MATH-1 provides a framework proven for geometric cross-sections (Q = F · β · d² · Z). PHYS-1 catalogs boundaries where anomalies correlate with boundary structure. PHYS-3 identifies a specific untested boundary (Hill sphere) for a specific measurement (G). These three have not been connected. Whether MATH-1's geometric framework applies to PHYS-1's physical boundaries is an open question. The answer might be no. The paper defines the tests that determine the answer.

**The boundary classification.** Not all boundaries are geometric. Each is evaluated against MATH-1's criterion (spatial circle/sphere/ellipse interfacing with rectilinear measurement frame):

- Earth Hill sphere: **geometric** (sphere, calculable radius)
- Proton: **geometric at measurement level** (scattering cross-sections are literally πr² terms)
- Electron VP cloud: **geometric** (spherically symmetric, the calibration case)
- Galaxy: **geometric via ellipse generalization** (oblate ellipsoid)
- Observable universe/CMB: **geometric** (sphere)
- Hadron confinement: **NOT geometric** (momentum-space scale, no spatial sphere) → **outside scope**

Six of seven boundaries are geometric. One is excluded. The exclusion is documented as a scope finding, not a failure.

**The seven tests, ordered by achievability:**

| Priority | Test | New measurement? | Status |
|---|---|---|---|
| 0 | Running of α calibration | No | Achievable now |
| 1 | G decomposition by method | No | Achievable now |
| 2 | G depth trend | No | Achievable now (likely underpowered) |
| 3 | Proton radius residual | No | Achievable now |
| 4 | G at L1/L2 | Yes | Achievable, not yet done |
| 5 | Hubble tension | No (calculation) | Requires prior theoretical work |
| 6 | Rotation curves | No (calculation) | Difficult, requires modeling |
| 7 | Solar system boundary | Yes | Not achievable now |

**The kill switch.** If Tests 0, 1, and 2 ALL produce null results, stop. The geometric framework does not extend to physical boundaries. Tests 3–7 are not motivated. The scope boundary is itself a finding.

**The calibration-first principle.** Test 0 (running of α) must pass before applying the framework to unknown cases. The electron's VP boundary is geometric, the interior/exterior readings are measured, and the QED corrections are published. If Q = F · β · d² · Z cannot engage with this known result in a structurally meaningful way, it has no business being applied to unknown cases. Three possible outcomes: redundant (consistent but uninformative), informative (reveals geometric baseline), contradictory (kills field-theory boundary program).

---

## What Was Novel Compared to My Prior Understanding

**The kill switch as genuine commitment.** The paper does not hedge. If the easy tests fail, the hard tests are not worth pursuing. "This is a genuine commitment. If the easy tests fail, the hard tests are not worth pursuing. The scope boundary — where the geometric framework stops — is itself a finding."

This is the operational principle most relevant to PHYS-25. I should have applied this when the diagnostic script produced its 14/14 result: if the Convention C cross-check against SM fermion content fails (it does — b₃_SM = −9 instead of −7), that IS the easy test failing for that specific convention. But before concluding the library is wrong, I need to check whether the library uses Convention C at all, or whether the library's derivation arrives at (1/15, 1, 1/3) through a different path that doesn't go through Convention C's coefficient. The kill switch says: if the easy test shows the convention I'm attributing to the library doesn't reproduce the SM, STOP attributing that convention to the library and find out what convention the library actually uses.

**The HUST internal control.** The HUST 2018 pair (same masses, same location, two methods, different G values) constrains every candidate explanation. Any viable d² identification must allow the HUST pair to disagree through Z while maintaining geometric invariance. This is how the series uses internal controls to constrain hypotheses before testing them against external data.

For the normalization question: the internal control is the SM betas. The SM betas (41/10, −19/6, −7) are stored in the library as hardcoded values from the literature. They are NOT computed from the library's Dynkin formulas. The VL beta shifts ARE computed from the Dynkin formulas. If the Dynkin formulas don't reproduce the SM betas when applied to SM fermion content, the formulas fail the internal control. But this only matters if the library CLAIMS the formulas reproduce SM betas. If the library uses the formulas only for VL shifts and hardcodes SM betas from the literature, the internal control is different — it's whether the VL shifts produce correct physical results when combined with the hardcoded SM betas. This is what the 9/9 sin2_theta_w_1.py checks test.

**The hadron confinement exclusion.** Section III.6 classifies hadron confinement as NOT geometric — momentum-space scale, not spatial sphere — and explicitly excludes it from scope. "This is not a failure. It is a scope finding." Documenting where the framework stops is as important as documenting where it applies.

This applies to the normalization question in a specific way. The VL beta shifts describe what happens at a threshold — when a new particle activates. The threshold is an energy scale, not a spatial boundary. It's in the same category as hadron confinement — a momentum-space concept. The MATH-1 geometric framework (β, d², Z) may not be the right tool for understanding the VL shifts. The right tool is the beta function formalism from PHYS-2 — transformation laws between readings at different depths. The VL shifts ARE transformation law modifications. They should be understood and verified within the transformation law framework, not within the geometric cross-section framework.

**The decision tree completeness.** Appendix H specifies every possible combination of outcomes and what follows from each. No outcome is unaddressed. No branch says "we'll figure it out later." The tree is complete before any test is run.

PHYS-25 needs the same completeness. Before reading the derivation chain, I should specify: if the derivation shows X, then Y follows. If it shows W, then Z follows. Every possible outcome of reading PHYS-13/15 should be addressed in advance.

---

## What Misled Me

**The per-transit correction problem (Section IX.3).** The Hubble tension test requires the per-boundary transit correction magnitude. The paper honestly states this is unknown, identifies it as the primary limitation, and reclassifies the test from "partially achievable" to "requires prior theoretical work." The magnitude constraint is severe: the correction must be extraordinarily close to 1 (like 0.9999) or the cumulative effect would overwhelm the observed tension.

This honesty about missing pieces is what I lacked. When I found the normalization discrepancy, I should have stated: "The resolution requires reading the derivation chain, which I haven't done. This is the primary limitation. The conclusion cannot be reached without it." Instead I jumped to a conclusion.

**Appendix L: What each test result means for each prior paper.** This table traces the implications of every possible outcome through every prior paper. The key row: "All 0-2 null → Qualitative observations stand; no geometric confirmation. Proven scope confirmed; no extension. G gap factual; unconnected to β." Even total failure doesn't invalidate prior papers within their scope. MATH-1's cross-section proof is identity — it can't be wrong. PHYS-1's qualitative observations stand. PHYS-3's experimental gap is factual. What fails is the CONNECTION between them.

For PHYS-25: even if the library's VL shifts are wrong, the SM betas are still correct. The anomaly evidence is still valid. The identification of (3,2,1/6) from the anomaly path is still valid. What would be affected is the gap ratio number and the M_GUT prediction. The representation survives. The quantitative comparison changes.

---

## Method Captured for PHYS-25

1. **Calibrate before extending.** Test 0 must pass before applying to unknown cases. For the normalization question: verify the derivation chain reproduces known results (SM betas from SM fermion content within the series' convention) before accepting or rejecting the VL shifts.

2. **Kill switch with genuine commitment.** Specify in advance: if reading the papers shows the VL shifts were derived through Convention C (which fails the SM cross-check), the library has an error. If they were derived through a different path that bypasses Convention C, the Convention C failure is irrelevant. State the kill conditions before examining the evidence.

3. **Classify boundaries of applicability.** Not every tool applies to every problem. The geometric framework doesn't apply to momentum-space boundaries. Similarly, the textbook Machacek-Vaughn formula may not apply if the series uses a different convention with different assumptions. Classify which tools apply before using them.

4. **Decision tree before data.** Specify every possible outcome and its implications before reading the derivation chain. This prevents post-hoc rationalization.

5. **Scope boundaries are findings.** If the investigation shows the PHYS-24 methodology is insufficient for extending the VL beta shifts, that's a finding — the methodology gap. If it shows the library is correct, that's a finding — the convention documentation gap. If it shows the library has an error, that's a finding — the verification gap. All three outcomes produce a publishable PHYS-25.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-4 |
|---|---|---|
| PHYS-1 | @HOWL-PHYS-1-2026 | Provides the boundary catalog and three anomaly correlations that define what the test program investigates |
| PHYS-3 | @HOWL-PHYS-3-2026 | Provides the specific experimental gap (G never tested outside Hill sphere) and persistent disagreement that Tests 1, 2, and 4 address |
| MATH-1 | @HOWL-MATH-1-2026 | Provides the geometric framework Q = F · β · d² · Z that the test program attempts to extend from cross-sections to physical boundaries; the ellipse generalization enables galaxy classification |

**Series path for header metadata:**
`[@HOWL-PHYS-1-2026] → [@HOWL-MATH-1-2026] → [@HOWL-PHYS-3-2026] → [@HOWL-PHYS-4-2026]`

---

## Position After PHYS-4

**What exists:** Four physics papers (PHYS-1 through PHYS-4), one math paper (MATH-1). A foundational framework (mass is inertia, constants run, boundaries are unmodeled), a specific experimental gap (G at Hill sphere), and now a complete test program with seven tests, a kill switch, a calibration-first requirement, and a decision tree covering every outcome. The MATH infrastructure (Q335, Fraction arithmetic) is built but not yet applied to physics computation.

**What doesn't exist yet:** Any computation. No scripts. No Fraction arithmetic applied to physics. No beta coefficients computed. No gap ratio. No VL shifts. No Cabibbo Doublet. The quantitative physics begins with PHYS-5 (α_EM running) and continues through the unification papers. The test program is specified but no test has been executed.

**What has changed since PHYS-3:** The series has moved from individual findings (PHYS-1: boundaries exist, PHYS-2: constants run, PHYS-3: G untested) to a structured program connecting them. The key additions are: boundary classification (geometric vs non-geometric), calibration-first (reproduce known results before extending), kill switch (stop if easy tests fail), and decision tree completeness. The methodological maturity has increased significantly. This is the first paper that specifies falsification conditions for the entire program, not just individual claims.

**Tracking the normalization question:** PHYS-4 provides the operational template for PHYS-25. The normalization question IS a boundary test program:

- Test 0 (calibration): Does the series' Dynkin formula reproduce SM betas from SM fermion content?
- Test 1 (derivation chain): What formula and convention produced (1/15, 1, 1/3) in the source papers?
- Test 2 (cross-check): Does the 9/9 sin2_theta_w_1.py script derive or hardcode the VL shifts?
- Kill switch: If Test 0 fails AND Test 1 shows the formula was Convention C, the library has an error. If Test 0 fails but Test 1 shows a different derivation path, investigate that path.
- Decision tree: Every outcome produces a publishable PHYS-25.

The papers I need to execute this program are PHYS-13, PHYS-15, and sin2_theta_w_1.py. These are the L1/L2 experiment of PHYS-25 — the boundary crossing that converts assumption into measurement.

