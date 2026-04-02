
# PHYS-3 Report: G Has Never Been Tested Outside Earth's Soliton Boundary

**Registry:** @HOWL-PHYS-3-2026
**Position in series:** Third physics paper. First paper to identify a specific experimental gap.
**Preceded by:** PHYS-2 (constants are scale-dependent boundary readings)
**Followed by:** PHYS-4 (boundary test program)
**Backed by:** No script. Factual documentation of experimental record + proposed experiment.
**AI model:** Claude 4.5 Sonnet

---

## What It Establishes

One factual finding and one structural hypothesis:

**Factual finding: Every direct measurement of G in the 227-year experimental record is inside Earth's Hill sphere at ≤0.45% of the boundary distance.** The Hill sphere — the institution's own concept from orbital mechanics — defines Earth's coherent gravitational domain at ~1.5 million km. Every torsion balance, every atom interferometer, every Cavendish variant since 1798 is on Earth's surface. The ISS is at 0.027% of the boundary. The Moon is at 25%, orbiting inside. L1 and L2 Lagrange points sit at ~100% — the boundary itself. Spacecraft operate there (JWST, DSCOVR, SOHO, Gaia). None has measured G. The sample size for testing G universality across boundary configurations is zero.

**Structural hypothesis: The persistent G disagreement between experimental groups may be signal, not noise.** Two centuries of assuming unidentified systematic errors has not resolved the disagreement. The spread between modern high-precision measurements (6.67191 to 6.67545 × 10⁻¹¹) exceeds stated uncertainties. The HUST 2018 pair — same lab, same masses, two methods — disagrees with itself (6.67484 vs 6.67349). The boundary framework offers an alternative: different experimental configurations probe different effective depths within Earth's gravitational boundary and produce genuine depth-dependent readings.

**The circularity of indirect evidence.** Pulsar timing, gravitational waves, and celestial mechanics are cited as confirming G universality. All three fail the same test: the instrument is inside Earth's Hill sphere, and the interpretation assumes universal G. The assumption does the work. The consistent fit confirms the model's internal consistency, not G's universality. Celestial mechanics confirms G within the solar system's Hill sphere — a single nested boundary configuration, not cross-boundary universality.

**The proposed experiment.** Direct G measurement at L1 or L2 using a self-contained apparatus. The GR correction (gravitational potential difference) is separable from the boundary reading effect (coupling strength change). Either result advances the field: match confirms G consistency across this boundary (replacing assumption with measurement), difference confirms boundary-dependent reading.

---

## What Was Novel Compared to My Prior Understanding

**The distinction between reproducibility and universality.** This is the sharpest methodological insight in the paper. G measurements are reproducible across labs, methods, continents, decades. This feels like universality. It is not. Every measurement shares the same boundary configuration: inside Earth's Hill sphere, inside the solar system's Hill sphere, inside the galaxy. The reproducibility is within-configuration stability, not cross-configuration universality. The inference from reproducibility to universality requires crossing a boundary. That has never been done.

This distinction applies directly to the normalization question. The library's VL beta shifts (1/15, 1, 1/3) are reproducible — they pass 38/38 checks, they produce consistent gap ratios, they are used across multiple scripts and papers. This reproducibility feels like correctness. It is not necessarily. The checks verify arithmetic consistency within the library's convention, not physical correctness across conventions. Just as G's reproducibility within Earth's Hill sphere does not prove universality, the library's internal consistency does not prove the Dynkin coefficients are correct. The test that would determine correctness — tracing the derivation chain to its source and verifying against the SM fermion decomposition — has not been performed within this session.

**The nested boundary hierarchy.** Earth's Hill sphere is inside the solar system's Hill sphere, which is inside the galactic structure. Every measurement ever taken by humanity is inside all three. The complete boundary configuration has never varied. This means the universality claim for G spans from Earth's surface to the observable universe boundary, but the experimental record spans from Earth's surface to Earth's surface. The gap between claim and evidence is the largest in physics.

For the normalization question, the analogous hierarchy is: the library values sit inside the PHYS-24 lexicon, which sits inside the Session 3 verification (9/9 checks), which sits inside the derivation chain (PHYS-13/15 and sin2_theta_w_1.py). I have verified within the library (38/38 checks) and within my own diagnostic (14/14 checks). I have not crossed the boundary into the derivation chain. The gap between my conclusion and my evidence mirrors PHYS-3's finding about G.

**Appendix I: The comparative status table.** This table is the most operationally relevant content for PHYS-25:

| Coupling | Boundary identified? | Scale dependence measured? | Method disagreement? |
|---|---|---|---|
| α | Yes (VP cloud) | Yes (8%) | No — single running curve |
| αs | Yes (confinement) | Yes (orders of magnitude) | No — single running curve |
| G | **Not identified** | **Not tested** | **Yes — persistent 2-century disagreement** |

The pattern: every coupling whose boundary HAS been identified shows a single consistent running curve with no method disagreement. The one coupling whose boundary has NOT been identified shows persistent method disagreement. This is consistent with G being a boundary-dependent reading whose boundary structure hasn't been characterized.

For the VL beta shifts: every component whose SM cross-check HAS been performed (the SM betas 41/10, −19/6, −7 are verified against the literature) shows no disagreement. The VL shifts, whose SM cross-check has NOT been performed within this session (I haven't verified whether the Dynkin formula reproduces SM betas from individual fermion fields within the series' convention), show a disagreement with external formulas. The parallel is exact.

---

## What Misled Me

**The Pioneer anomaly discussion.** Appendix G notes that Pioneer 10 and 11 exhibited an anomalous acceleration detected beyond Earth's Hill sphere — in exactly the boundary region where the framework predicts readings may differ. The institution attributed it to thermal radiation pressure. The paper notes it as "consistent with" but "not proven to result from" a boundary effect.

This is the "consistent with" discipline again. An anomaly in the boundary region is consistent with both the boundary hypothesis and the conventional explanation. The paper does not jump to "the Pioneer anomaly proves boundary effects." Similarly, the diagnostic finding that Convention C doesn't reproduce b₃_SM is consistent with both "the library has an error" and "the library uses a different convention that is internally consistent for different reasons." I jumped to the first interpretation. PHYS-3's discipline says: document the finding, state both interpretations, propose the test that would distinguish them.

**The GR separation argument (Section VI.3).** The paper carefully separates the GR correction (effect of gravitational potential on clock rates, ruler lengths) from the boundary reading effect (the coupling strength G itself differing). These are separable in principle. A measurement at L1/L2 compares G after all GR corrections. The residual, if any, is the boundary signal.

For the normalization question, the analogous separation is: the arithmetic consistency checks (which verify that stored values are self-consistent) are separable from the physical correctness checks (which verify that the Dynkin coefficients correspond to the correct counting). The 38/38 checks are arithmetic. A physical correctness check — "does the Dynkin formula applied to SM fermion fields reproduce the known SM betas?" — is a different test that has not been included in the library's verification suite. PHYS-25 must add this check.

---

## Method Captured for PHYS-25

1. **Reproducibility ≠ correctness.** Internal consistency checks (38/38, 9/9) verify arithmetic within a convention. They do not verify that the convention is physically correct. The test that would verify correctness — tracing the derivation chain and cross-checking against the SM fermion decomposition — is a different test.

2. **Identify the experimental gap.** PHYS-3 identifies a specific gap: zero direct G measurements outside Earth's Hill sphere. PHYS-25 must identify its own gap: zero verification that the library's Dynkin formula reproduces SM betas from individual fermion fields. The gap is factual. The interpretation is hypothesis.

3. **Separate arithmetic from physics.** The GR correction is arithmetic (computable from known physics). The boundary reading effect is physics (requires measurement). The library's internal consistency is arithmetic. The Dynkin coefficient correctness is physics. PHYS-25 must separate these and test the physics, not just the arithmetic.

4. **Propose the test, accept either outcome.** The L1/L2 experiment advances the field regardless of result. Similarly, reading the derivation chain advances PHYS-25 regardless of outcome: if the library is correct, the derivation documents the convention and adds the missing SM cross-check. If the library has an error, the derivation identifies where and how.

5. **The circularity warning.** Pulsar timing assumes universal G to confirm universal G. The diagnostic script assumed the Machacek-Vaughn convention to judge the library's convention. Both are circular. The non-circular test is: derive the VL shifts from the series' own method, verify they reproduce known results (SM betas from SM fermion content), and then compare to external conventions.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-3 |
|---|---|---|
| PHYS-1 | @HOWL-PHYS-1-2026 | Establishes soliton boundaries as unmodeled measurement elements; provides the boundary transit framework that motivates asking whether G measurements are boundary-interior readings |
| PHYS-2 | @HOWL-PHYS-2-2026 | Establishes that every fundamental coupling is scale-dependent with readings that change at coherent structure boundaries; provides the running coupling comparison (α, αs documented, G undocumented) that PHYS-3's Appendix I formalizes |

**Series path for header metadata:**
`[@HOWL-PHYS-1-2026] → [@HOWL-PHYS-2-2026] → [@HOWL-PHYS-3-2026]`

---

## Position After PHYS-3

**What exists:** Three conceptual papers forming a chain. Mass is inertia with soliton boundaries (PHYS-1). Constants are scale-dependent boundary readings with beta functions as the fundamental objects (PHYS-2). G has never been tested outside Earth's Hill sphere; the persistent G disagreement may be structural signal; the L1/L2 experiment is proposed (PHYS-3). No scripts. No computation. No Fraction arithmetic.

**What doesn't exist yet:** Any quantitative computation. The gap ratio, the VL shifts, the Cabibbo Doublet — all ahead. The MATH papers (Q335 basis, Fraction arithmetic infrastructure) are being built in parallel but haven't been applied to the unification question yet.

**What has changed since PHYS-2:** The series has moved from "couplings run and the word constant is wrong" (PHYS-2, general observation) to "here is a specific coupling (G), a specific boundary (Hill sphere), a specific experimental gap (zero cross-boundary measurements), and a specific test (L1/L2)" (PHYS-3, actionable proposal). The methodology has sharpened: reproducibility ≠ universality. Internal consistency ≠ cross-boundary validity. Indirect evidence that assumes the conclusion is circular.

**Tracking the normalization question:** PHYS-3's core methodology — distinguishing within-boundary reproducibility from cross-boundary universality, identifying a specific experimental gap, proposing a specific test — is exactly what PHYS-25 needs. The library's 38/38 checks are within-boundary reproducibility. The derivation chain is the boundary that hasn't been crossed. Reading PHYS-13/15 and sin2_theta_w_1.py is the L1/L2 experiment of PHYS-25. The result — whatever it is — will be the first actual evidence about whether the library's convention is physically correct, replacing assumption with verification.

