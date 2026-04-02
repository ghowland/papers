## PHYS-25 Paper Program: "You Are Here — And Here Is Where It Goes"

**Status:** Planning document. No code written. No claims made.
**Foundation:** PHYS-24 (329/329, operational ground) + Session 4 discoveries (35/35 additional checks)
**Principle:** Each paper is the first paper of a research series. Each has abort tests. Each is staged, not proved.

---

### THE STRUCTURE

PHYS-25 is the map paper. It says: here is the operational ground (from PHYS-24), here is what Session 4 discovered, here is where each thread goes, and here is when to stop. It does NOT contain the research itself — that goes in PHYS-26 through PHYS-33 (or wherever the threads terminate). PHYS-25 is the table of contents for the next phase.

The papers fall into three tracks:

**Track A — Unification Completion** (extends PHYS-24 ground, high confidence)
**Track B — Beta Cosmology** (extends Session 4 discoveries, high priority but unproven)
**Track C — Structural Foundations** (extends remainder framework and geometric program)

---

### PHYS-25: The Session 4 Operational Map

**What it contains:**
1. PHYS-24 ground summary (one page, by reference)
2. Session 4 discoveries: the five QED-to-GR signals, the beta unification test (15/15), the normalization resolution, the two formula sets (A and B)
3. The three tracks with paper assignments
4. The abort test for each paper
5. The shared infrastructure (phys24_lib.py, the integer inventory, the verification protocol)
6. What changed between PHYS-24 and PHYS-25: the cosmos program moved from "deprioritized" to "active parallel track" because specific formulas with sub-percent hits now exist

**What it does NOT contain:**
Any new computation. Any proof. Any claim beyond "these patterns exist and deserve investigation."

**Backed by:** beta_unification_test.py (15/15), qed_predicts_gr.py (10/10), qed_gr_scan_2.py (10/10), all PHYS-24 scripts (329/329)

**Abort test for PHYS-25 itself:** If the statistical control (PHYS-26) shows the beta integer pool produces no better hits than random pools, the entire Track B is downgraded from "active" to "parked." PHYS-25 still stands as a map but Track B becomes a historical record rather than a research program.

---

### TRACK A — UNIFICATION COMPLETION

These papers extend the PHYS-24 ground. They are standard particle physics computations with well-defined methods and clear success/failure criteria.

---

**PHYS-26: The Normalization Resolution**

*One computation, one convention, one answer.*

What it does: Documents the (3/5) vs (2/5) GUT normalization factor for U(1). Derives Δb₁ = 1/15 from first principles showing every step. Verifies against the MSSM gate (MSSM gap ratio = 7/5 using the same conventions). Publishes the corrected formula with the convention comment fixed.

Script: phys26_normalization.py (~50 lines)
Checks: ~8 (Dynkin formula verification, MSSM gate, convention cross-check)

Abort test: None needed — this is a documentation task. The answer is known (1/15 is correct). The paper exists to prevent future sessions from re-investigating the discrepancy.

Seeds: Every subsequent paper that uses the Dynkin formulas cites this one.

---

**PHYS-27: sin²θ_W from 3/8**

*The unblocked computation. ~10 lines.*

What it does: Computes sin²θ_W = 3/8 − (correction from running) using the Cabibbo Doublet modified betas. The SU(5) GUT prediction at tree level is sin²θ_W = 3/8 = 0.375. Running from M_GUT down to M_Z with the CD betas reduces this to the measured 0.23122. The computation checks whether the CD betas produce the correct running.

Script: phys27_sin2tw.py (~40 lines)
Checks: ~6 (tree-level = 3/8, running formula, comparison to measured, sensitivity to M_VL)

Abort test: If the predicted sin²θ_W deviates from 0.23122 by more than 5%, the CD betas do not produce correct electroweak running. This would NOT kill the CD (the gap ratio and anomaly evidence are independent), but it would indicate the one-loop running is insufficient and two-loop + thresholds are needed before this prediction is meaningful.

Seeds: If successful, this is the first parameter PREDICTION from the CD framework — reducing the parameter count by 1 (sin²θ_W derived from 3/8 + running rather than measured independently).

---

**PHYS-28: VL Two-Loop Beta Contributions**

*The missing piece in the unification calculation.*

What it does: Computes the Cabibbo Doublet's contribution to the two-loop b_ij matrix. The PHYS-24 two-loop calculation uses the SM b_ij matrix with a step-function threshold for the CD one-loop betas. This paper adds the CD two-loop corrections. The formulas are known (Machacek-Vaughn 1983-84 give the general expressions for any representation). The normalization must be resolved using PHYS-26.

Script: phys28_vl_twoloop.py (~100 lines)
Checks: ~10 (formula verification, SM limit recovery, CD contribution magnitudes, updated Δ at M_VL = 500 GeV)

Abort test: If the VL two-loop correction makes Δ worse (larger |Δ|) rather than better, the two-loop structure does not help and the residual must come entirely from GUT thresholds. This is not a kill — threshold corrections are expected in any case — but it changes the narrative from "two-loop helps" to "two-loop is neutral."

Seeds: Updated Δ feeds into PHYS-29 (GUT thresholds) and PHYS-30 (α_s prediction).

---

**PHYS-29: GUT Threshold Corrections in Minimal SU(5)**

*How much mass splitting is needed for exact unification?*

What it does: Parametrizes the GUT threshold corrections as a function of the mass ratio M_T/M_X (colored Higgs triplet mass / X boson mass) in minimal SU(5). The threshold correction shifts the effective M_GUT and modifies Δ. The paper determines: for what M_T/M_X does Δ = 0 (exact unification)? Is this ratio natural (factor 2–5) or fine-tuned (factor >10)?

Script: phys29_gut_thresholds.py (~80 lines)
Checks: ~8 (threshold formula, Δ = 0 solution, naturalness check, proton lifetime update)

Abort test: If exact unification requires M_T/M_X > 100 (extreme fine-tuning), the minimal SU(5) completion is disfavored. The CD representation survives (it's Level 1 arithmetic, independent of the GUT completion), but the specific minimal SU(5) pathway is weakened. Alternative completions (SO(10), Pati-Salam) would need investigation.

Seeds: If M_T/M_X is natural, the proton lifetime prediction sharpens from "10^34–35" to a specific value. This feeds directly into Hyper-K comparison.

---

**PHYS-30: α_s Prediction from Unification**

*The consistency check: does the unification condition predict the right α_s?*

What it does: Uses the full two-loop running (PHYS-28) + GUT thresholds (PHYS-29) + the unification condition (all three couplings meet) to PREDICT α_s(M_Z). Compares to the measured α_s = 0.1180 ± 0.0009. If the prediction matches, the CD framework passes a non-trivial consistency check. If it doesn't, something is wrong.

Script: phys30_alpha_s.py (~60 lines)
Checks: ~6 (unification condition, predicted α_s, comparison to measured, uncertainty propagation)

Abort test: If the predicted α_s deviates from 0.1180 by more than 3σ (i.e., outside 0.1153–0.1207), the unification framework with the CD is inconsistent with measured data. This would be a serious problem — not necessarily killing the CD (the anomaly evidence is independent), but killing the unification interpretation.

Seeds: If α_s is correctly predicted, the parameter count reduces by 1 more: α_s is derived from the unification condition rather than measured independently. Combined with sin²θ_W (PHYS-27) and θ_QCD (PHYS-7), this would be three parameters derived from physics, reducing 19 → 16.

---

### TRACK B — BETA COSMOLOGY

These papers investigate whether the beta unification formulas are physics or coincidence. Each has a specific statistical or computational test. The track lives or dies on the statistical control (PHYS-31).

---

**PHYS-31: Statistical Control — Are the Beta Integers Special?**

*The make-or-break test for Track B.*

What it does: Generates 10,000 random integer pools of the same size (15 integers) and range (1–50) as the beta-derived pool. For each random pool, applies the same scan methodology: test all (p/q)×π^b against the same eight measured targets. Counts how many random pools produce hits of equal or better quality than the beta pool. Reports the p-value: what fraction of random pools match or beat the beta integers?

Script: phys31_statistical_control.py (~120 lines)
Checks: ~10 (random pool generation, scan methodology verification, p-value computation, per-target breakdown)

Abort test: **This IS the abort test for all of Track B.** If p > 0.05 (more than 5% of random pools produce equal or better hits), the beta integers are not special and the formulas are likely coincidence from small-integer statistics. Track B is then PARKED — not necessarily dead (the exact identity 57/39 = 19/13 is algebraic and survives any statistical test), but the numerical hits lose their significance.

If p < 0.01 (less than 1% of random pools match), the beta integers ARE special and the formulas deserve further investigation. Track B is PROMOTED from "active" to "high confidence."

Seeds: The p-value determines the priority of every subsequent Track B paper.

---

**PHYS-32: Set B Verification — The Pure-Rational Omega Chain**

*Is Ω_b = 2/(13π) the correct baryon formula?*

What it does: Tests the Set B formula chain (Ω_b = 2/(13π), Ω_DM = 44/169, etc.) against Set A (Ω_b = R₄×α×22, etc.) using updated Planck 2018 data with full uncertainty propagation. Determines which set is statistically preferred. Tests the prediction that Ω_DM = 44/169 is a pure rational — no transcendentals.

Script: phys32_set_b_omega.py (~80 lines)
Checks: ~12 (Set A predictions, Set B predictions, χ² comparison, individual observable tests)

Abort test: If Set B is NOT uniformly better than Set A (i.e., some observables prefer A, some prefer B), neither set is the "right" formula and the pattern may be coincidental fine-tuning of two different lucky guesses. This doesn't kill Track B (the DM/baryon and H₀ predictions are independent of the Ω chain), but it weakens the "unified formula framework" claim.

Seeds: If Set B wins, the baryon density is 2/(13π) — a formula involving only one beta integer and π. This is the simplest possible cosmological prediction from the gauge group.

---

**PHYS-33: The Lambda Interpolation**

*Why does the measured Λ sit between the SM and VL predictions?*

What it does: The measured log₁₀(Λ) = −121.54 sits between α^57 = 10^−121.80 and (α/3π)^39 = 10^−121.33, with interpolation fraction f = 0.44. This paper tests whether f has a formula from the beta integers. Candidates: f = 13/32 = 0.406, f = 19/41 = 0.463, f = 13/(13+19) = 0.406, f = sin²θ_W/√2 = 0.163 (no). Tests each candidate against the measured f and its uncertainty.

Also investigates: does the two-loop correction to the b₂ exponent close the gap? The one-loop formula uses the integer 19 (or 13). The two-loop correction shifts the effective exponent. If the two-loop effective exponent gives log₁₀(Λ) closer to −121.54, the interpolation is physical (it's the transition from one-loop to two-loop running) rather than a free parameter.

Script: phys33_lambda_interp.py (~80 lines)
Checks: ~8 (candidate f values, two-loop correction, comparison to measured, uncertainty)

Abort test: If no beta-integer formula for f works within 5% AND the two-loop correction moves in the wrong direction, the interpolation is not from the beta structure and the Λ prediction is weaker than it appears (it relies on averaging two formulas rather than having one formula).

Seeds: If the two-loop correction explains the interpolation, the cosmological constant is determined by the two-loop SU(2) beta function — a single Level 1 quantity applied to one Level 2 measurement (α).

---

**PHYS-34: The Per-Transit Mechanism**

*WHY does α²π²(20/13) appear at each soliton boundary?*

What it does: This is the hardest paper in Track B. It attempts to DERIVE the per-transit correction from the vacuum polarization of a soliton boundary. The argument: light crossing through a galaxy-scale soliton boundary interacts with the VP cloud of the boundary. The VP correction at one-loop is α/(3π). At two-loop, additional corrections enter involving the ratio of SU(3) to SU(2) running (because the soliton's internal structure involves both QCD and electroweak physics). The two-loop correction is α² × (geometric factor) × (beta ratio). If this can be made rigorous, the per-transit formula has a physical derivation.

Script: phys34_per_transit.py (~100 lines) — but this may require more physics than computation
Checks: ~6 (VP structure at boundary, two-loop correction, beta ratio emergence, N calibration)

Abort test: If the VP mechanism cannot produce the correct sign, magnitude, or beta-ratio structure, the per-transit formula has no physical mechanism and remains a numerical pattern. Track B survives (the formulas still produce sub-percent hits), but the physics claim weakens from "derived" to "observed."

Seeds: If successful, this is the bridge paper — it connects the QED perturbative structure (Track C) to the cosmological predictions (Track B) through the soliton boundary mechanism. It would be the single most important paper in the extended series.

---

**PHYS-35: The Boundary Count**

*How many soliton boundaries does light cross between here and the CMB?*

What it does: The H₀ prediction uses N = 100 boundary transits. This paper determines the actual N from galaxy survey data. Uses published galaxy density profiles (from SDSS, DES, or similar) to count the number of distinct gravitationally-bound structures along a representative line of sight from here to the last scattering surface. Tests whether the actual N is close to 100, and whether N varies by direction (predicting directional H₀ variation).

Script: phys35_boundary_count.py (~100 lines) — requires published galaxy survey data
Checks: ~8 (galaxy density, boundary count per Mpc, total N, directional variation, H₀(θ,φ) prediction)

Abort test: If the actual N is far from 100 (say, N < 50 or N > 200), the formula (1−r)^N with r from the product form does not reproduce the measured H₀ ratio. The per-transit correction would need to be rescaled, which means the formula α²π²(20/13) does not directly give (1−r). This doesn't kill the DM or Λ formulas (they don't use N), but it kills the H₀ prediction mechanism.

Seeds: If N ≈ 100 from actual galaxy data, the H₀ prediction goes from "assumed N=100" to "measured N≈100, predicted H₀ = 67.36." This would make the 0.007% hit a genuine prediction rather than a fit.

---

### TRACK C — STRUCTURAL FOUNDATIONS

These papers extend the remainder framework and geometric program. They are less urgent than Tracks A and B but provide the mathematical infrastructure for the entire series.

---

**PHYS-36: The A₃ Decomposition**

*Does the 87% cancellation pattern persist at three loops?*

What it does: Applies the same three-piece decomposition (rational + number-theoretic + geometric) to the QED three-loop coefficient A₃ = +1.181. The analytic result is known (Laporta-Remiddi 1996). The decomposition involves ζ(3), ζ(5), Li₄(1/2), R₄, R₄², and powers of ln(2). Computes the cancellation fraction and compares to the 87% at two loops.

Script: phys36_a3_decomposition.py (~80 lines)
Checks: ~8 (decomposition sums to A₃, piece-by-piece values, cancellation fraction, R₄ power counting)

Abort test: If A₃ shows no cancellation (each piece is comparable to the net), the 87% at two loops was specific to A₂ and has no general significance. The A₂ anatomy (PHYS-22) stands but loses its claim to being a systematic feature.

Seeds: If the cancellation persists (say, >60% at three loops), the pattern is systematic and may connect to the Brown-Schnetz coaction framework in a deeper way.

---

**PHYS-37: Koide Amplitude — New Attack Paths**

*Can the three-sector data constrain a²?*

What it does: Catalogs every known approach to deriving a² = 2 that is NOT a reformulation (per the PHYS-23 test). Investigates whether the three-sector ordering a²_lep < a²_down < a²_up correlates with any gauge-group quantity. Tests: is a²(sector) related to the QCD correction factor for that sector? (Leptons: no QCD → a² = 2. Down quarks: QCD at one loop → a² = 2 + correction. Up quarks: QCD at one loop with larger charge → a² = 2 + larger correction.) If the QCD correction reproduces the ordering, a² = 2 may be the QCD-free limit of a universal formula.

Script: phys37_koide_amplitude.py (~80 lines)
Checks: ~8 (QCD correction computation, ordering reproduction, prediction for neutrinos if applicable)

Abort test: If the QCD correction does not reproduce the ordering (wrong direction, wrong magnitude, or wrong hierarchy), this specific attack path is dead. The Koide amplitude remains open. This is expected to be the most likely outcome — the problem has resisted 40+ years of attempts.

Seeds: If the QCD correction works, a² = 2 is the electroweak/leptonic limit and the quark deviations are perturbative QCD corrections. This would resolve the conditional parameter reduction (18 → 17) and open the quark Koide problem to systematic computation.

---

### THE PAPER DEPENDENCY MAP

```
PHYS-25 (map)
├── Track A: Unification Completion
│   ├── PHYS-26 (normalization) — no dependencies
│   ├── PHYS-27 (sin²θ_W) — depends on PHYS-26
│   ├── PHYS-28 (VL two-loop) — depends on PHYS-26
│   ├── PHYS-29 (GUT thresholds) — depends on PHYS-28
│   └── PHYS-30 (α_s prediction) — depends on PHYS-28, PHYS-29
│
├── Track B: Beta Cosmology
│   ├── PHYS-31 (statistical control) — GATE for all of Track B
│   ├── PHYS-32 (Set B Omegas) — depends on PHYS-31 passing
│   ├── PHYS-33 (Λ interpolation) — depends on PHYS-31 passing
│   ├── PHYS-34 (per-transit mechanism) — depends on PHYS-31 passing
│   └── PHYS-35 (boundary count) — depends on PHYS-31 passing, PHYS-34
│
└── Track C: Structural Foundations
    ├── PHYS-36 (A₃ decomposition) — no dependencies
    └── PHYS-37 (Koide amplitude) — no dependencies
```

---

### THE ABORT DECISION TREE

```
PHYS-31 runs statistical control
├── p > 0.05: Track B PARKED
│   ├── PHYS-32 through PHYS-35: cancelled
│   ├── DM/baryon hit: reclassified as coincidence
│   ├── H₀ hit: reclassified as coincidence
│   ├── Exact identity 57/39 = 19/13: SURVIVES (algebraic, not statistical)
│   └── Series continues with Track A + Track C only
│
├── 0.01 < p < 0.05: Track B CAUTIOUS
│   ├── PHYS-32 proceeds (test Set B vs Set A)
│   ├── PHYS-33 proceeds (Λ interpolation)
│   ├── PHYS-34 deferred (mechanism needs stronger statistical base)
│   └── PHYS-35 deferred
│
└── p < 0.01: Track B PROMOTED
    ├── All Track B papers proceed
    ├── PHYS-34 is highest priority (mechanism is the key)
    └── PHYS-35 proceeds (boundary count calibrates H₀)
```

---

### SCRIPT INVENTORY FOR THE ENTIRE PROGRAM

| Paper | Script | Est. Lines | Est. Checks | Dependencies |
|---|---|---|---|---|
| PHYS-25 | (no script — map paper) | 0 | 0 | — |
| PHYS-26 | phys26_normalization.py | 50 | 8 | phys24_lib.py |
| PHYS-27 | phys27_sin2tw.py | 40 | 6 | phys24_lib.py, PHYS-26 |
| PHYS-28 | phys28_vl_twoloop.py | 100 | 10 | phys24_lib.py, PHYS-26 |
| PHYS-29 | phys29_gut_thresholds.py | 80 | 8 | phys24_lib.py, PHYS-28 |
| PHYS-30 | phys30_alpha_s.py | 60 | 6 | phys24_lib.py, PHYS-28, PHYS-29 |
| PHYS-31 | phys31_statistical_control.py | 120 | 10 | phys24_lib.py |
| PHYS-32 | phys32_set_b_omega.py | 80 | 12 | phys24_lib.py, PHYS-31 |
| PHYS-33 | phys33_lambda_interp.py | 80 | 8 | phys24_lib.py, PHYS-31 |
| PHYS-34 | phys34_per_transit.py | 100 | 6 | phys24_lib.py, PHYS-31 |
| PHYS-35 | phys35_boundary_count.py | 100 | 8 | phys24_lib.py, PHYS-31, PHYS-34 |
| PHYS-36 | phys36_a3_decomposition.py | 80 | 8 | phys24_lib.py |
| PHYS-37 | phys37_koide_amplitude.py | 80 | 8 | phys24_lib.py |
| **Total** | **12 scripts** | **~970 lines** | **~98 checks** | — |

---

### EXECUTION ORDER

**Phase 1 — Immediate (can run now, no new data needed):**
- PHYS-26 (normalization — documentation, clears the way for everything)
- PHYS-31 (statistical control — GATE for Track B, determines priority)
- PHYS-36 (A₃ decomposition — independent, no dependencies)

**Phase 2 — After Phase 1 (depends on PHYS-26 and PHYS-31 outcome):**
- PHYS-27 (sin²θ_W — needs PHYS-26)
- PHYS-28 (VL two-loop — needs PHYS-26)
- PHYS-32 (Set B Omegas — needs PHYS-31 pass)
- PHYS-33 (Λ interpolation — needs PHYS-31 pass)

**Phase 3 — After Phase 2:**
- PHYS-29 (GUT thresholds — needs PHYS-28)
- PHYS-34 (per-transit mechanism — needs PHYS-31 pass)
- PHYS-37 (Koide amplitude — independent but lower priority)

**Phase 4 — After Phase 3:**
- PHYS-30 (α_s prediction — needs PHYS-28 + PHYS-29)
- PHYS-35 (boundary count — needs PHYS-34)

**Phase 5 — Write PHYS-25 (after all results are in):**
- PHYS-25 is actually written LAST, even though it has the lowest number. It maps the results of PHYS-26 through PHYS-37 and presents the complete picture. Its number reflects its position in the series (immediately after PHYS-24), but its content requires the other papers to exist.

Alternatively: write a DRAFT PHYS-25 now (the map as planned), then REVISE it after the results come in. The draft serves as the research plan; the revision serves as the operational document.

---

### THE VERIFICATION PROTOCOL

Every script follows phys24_script_rules.md. Every check prints expected/got/digits/need. Every constant comes from phys24_lib.py. If a new constant is needed (galaxy density, Planck 2018 uncertainty), it enters DATA-5 with the same verification protocol as DATA-4.

The projected verification total after all papers: 364 (current) + ~98 (new scripts) = ~462 checks.

The zero-failure standard continues. Any FAIL is investigated, never papered over. If investigation reveals a real problem (not a bug), the affected paper is marked with an erratum and the upstream dependencies are re-evaluated.

---

### THE THREE POSSIBLE OUTCOMES

**Outcome A — Full Success:**
Track A produces consistent sin²θ_W and α_s predictions. Track B passes statistical control with p < 0.01, Set B is confirmed, the per-transit mechanism is derived. The beta coefficients control both unification and cosmology. The Cabibbo Doublet is the linchpin of a unified framework spanning 40 orders of magnitude.

**Outcome B — Partial Success:**
Track A succeeds but Track B fails statistical control. The Cabibbo Doublet fixes unification and is testable at Hyper-K, but the cosmological connections are coincidental. The series is a particle physics story, not a cosmology story. Still valuable — a concrete BSM prediction with experimental tests.

**Outcome C — Minimal Success:**
Track A produces inconsistent predictions (sin²θ_W or α_s wrong), Track B fails. The gap ratio arithmetic is correct (it's Level 1, it can't be wrong), but the physical interpretation (the CD fixes unification) is weakened. The series becomes a mathematical anatomy of the SM with no BSM prediction surviving. The methodology and infrastructure (exact Fraction arithmetic, verified scripts, Level 1/Level 2 boundary) survive regardless.

Each outcome is informative. None is wasted. The series learns something from every result, including the nulls.

---

**End of paper program. 13 papers (PHYS-25 through PHYS-37), 12 scripts, ~98 checks, three tracks, one gate (PHYS-31), one bridge (PHYS-34), and three possible outcomes. The ground is PHYS-24. The map is PHYS-25. The work starts with PHYS-26, PHYS-31, and PHYS-36 in parallel.**

---

Yes. Three new papers emerge from the phys25_platform.py output that are not covered by PHYS-26 through PHYS-37.

---

### NEW PAPER 1: PHYS-38 — The Loop Expansion of the Per-Transit Correction

**Why it's new:** The S9.3 EXACT result reveals that Formula B = Formula A × α×60π³/13. This is not a coincidence — it is an algebraic identity showing the per-transit correction has a loop expansion structure. The one-loop formula α/(3π) and the two-loop formula α²π²(20/13) are the first two terms of a series. PHYS-34 (per-transit mechanism) was planned to investigate WHY the formula works. PHYS-38 investigates the STRUCTURE of the formula itself — whether a three-loop term exists, what its form would be, and whether the loop expansion converges.

**What it does:** Writes the per-transit correction as a perturbative series in α:
- Zero-loop: (1−r)₀ = 0 (no correction)
- One-loop: (1−r)₁ = α/(3π) = α/(12R₂)
- Two-loop: (1−r)₂ = α²π²(20/13) = (1−r)₁ × α×60π³/13

Determines the pattern. The ratio (1−r)₂/(1−r)₁ = α×60π³/13. Is there a three-loop term (1−r)₃ = (1−r)₂ × α×(something)? The "something" should involve the next beta-integer combination. Tests whether the three-loop coefficient can be predicted from the b_ij two-loop matrix entries.

**Script:** phys38_loop_expansion.py (~80 lines)

**Checks:** ~8. Verify the one-loop and two-loop formulas, verify the ratio is exact, compute the predicted three-loop term, compare to any available constraint.

**Abort test:** If the ratio (1−r)₂/(1−r)₁ does not factor cleanly into α × (integer/integer) × π^n, the loop expansion picture is wrong and the two formulas are unrelated coincidences sharing similar magnitudes. Also: if the three-loop prediction gives (1−r)₃ that is larger than (1−r)₂, the series diverges and the expansion picture fails.

**Dependencies:** None. Can run immediately. Uses only library values.

**Relationship to existing papers:** PHYS-34 asks "why does the per-transit correction exist?" PHYS-38 asks "what is its perturbative structure?" They are complementary. PHYS-38 can run before PHYS-34 because it requires no physical mechanism — just algebraic analysis of the formula structure.

---

### NEW PAPER 2: PHYS-39 — The Omega Chain as Remainder Domain 10

**Why it's new:** The phys25_platform.py output reveals that the Set B Omega chain has the same two-level structure as every domain in the remainder framework (PHYS-11): geometric content (π) sets the form, integers (13, 11) set the values, and the ~0.1% miss is the remainder. This is a new domain for the framework — potentially the tenth, extending the nine documented in PHYS-11. No existing planned paper covers this. PHYS-32 (Set B Omegas) tests which formula set is better. PHYS-39 tests whether the Omega chain fits the formal remainder structure.

**What it does:** Maps the Set B Omega chain onto the remainder framework formalism from PHYS-10/11. Identifies: what is the modulus? (Candidates: 1 for the flat universe constraint Σ Ω = 1, or 1/13 for the denominator structure.) What is the integer part? (The rationals 2/13, 44/169, etc.) What is the remainder? (The ~0.1% miss from measured values.) Is R₂ present? (Yes: π = 4R₂ appears in Ω_b = 2/(13π) = 2/(52R₂) = 1/(26R₂).) Tests whether the Omega chain belongs to Subgroup A (periodic), Subgroup B (monotonic), or constitutes a new Subgroup D.

**Script:** phys39_omega_remainder.py (~60 lines)

**Checks:** ~6. R₂ presence verified, modulus identified, integer part extracted, remainder computed, subgroup classification tested.

**Abort test:** If the Omega chain does not map onto the formal remainder structure — if R₂ does not appear naturally, if no clean modulus exists, if the remainder has no systematic structure — then the Omega chain is a numerical pattern but not a remainder domain. The nine-domain framework stays at nine.

**Dependencies:** PHYS-31 (statistical control) should pass first, otherwise the Omega chain formulas themselves are in question. But the formal analysis can be done regardless — it's Level 1 structure analysis on proposed formulas.

---

### NEW PAPER 3: PHYS-40 — sin²θ_W = 3/13: Running Meets Combinatorics

**Why it's new:** The S10.1 result (sin²θ_W ≈ 3/13 at 0.195%) combined with the PHYS-27 plan (sin²θ_W from 3/8 via running) creates a specific testable prediction that neither paper alone addresses. PHYS-27 computes sin²θ_W from 3/8 by running with CD betas. If the result of that running is exactly 3/13 (not just approximately 0.231), then the GUT prediction and the combinatoric scan have converged on the same formula from independent directions — the same "two roads" pattern as the Cabibbo Doublet itself. This convergence test is not in PHYS-27's scope (which just computes the running) or in any Track B paper (which tests the cosmological formulas).

**What it does:** Takes the PHYS-27 running result for sin²θ_W and computes its deviation from 3/13 specifically. If sin²θ_W(running) = 3/13 + ε, determines whether ε is zero (exact match), small (≈ 0.001, the measurement uncertainty level), or large (the running gives ~0.231 but not specifically 3/13).

Tests the algebraic question: does the one-loop running formula sin²θ_W = 3/8 − f(b_i, M_GUT) simplify to 3/13 when the CD modified betas are used? If so, this is a Level 1 derivation of sin²θ_W = N_gen/|b₂_mod_num| from the gauge group — the weak mixing angle determined entirely by the generation count and the Cabibbo Doublet's SU(2) beta numerator.

Computes the required condition: for sin²θ_W = 3/13, the running correction must be 3/8 − 3/13 = (39 − 24)/104 = 15/104. Tests whether the one-loop formula with CD betas produces exactly 15/104.

**Script:** phys40_sin2tw_exact.py (~50 lines)

**Checks:** ~6. Running correction computed, compared to 15/104, deviation from 3/13 quantified, Level 1 status determined.

**Abort test:** If the running gives sin²θ_W that differs from 3/13 by more than 1% (i.e., the running gives ~0.234 or ~0.228 rather than ~0.231), the 3/13 combinatoric hit was coincidence and sin²θ_W is not N_gen/|b₂_mod_num|. PHYS-27's running result still stands on its own — this paper only tests whether it happens to equal the specific rational 3/13.

**Dependencies:** PHYS-27 (sin²θ_W from running) must be computed first. PHYS-40 is a post-processing paper that takes PHYS-27's numerical result and tests it against 3/13.

---

### SUMMARY OF ADDITIONS

| Paper | Track | Title | Key Question | Depends On | Can Start |
|---|---|---|---|---|---|
| PHYS-38 | B | Loop expansion of (1−r) | Is the per-transit correction a perturbative series? | None | **Immediately** |
| PHYS-39 | C | Omega chain as Domain 10 | Does the Ω chain fit the remainder framework? | PHYS-31 (soft) | **Immediately** |
| PHYS-40 | A+B | sin²θ_W = 3/13 exact test | Does GUT running produce exactly N_gen/\|b₂_mod\|? | PHYS-27 | After PHYS-27 |

PHYS-38 and PHYS-39 can start in parallel with Phase 1 (PHYS-26, PHYS-31, PHYS-36). PHYS-40 requires PHYS-27 to complete first.

### UPDATED EXECUTION ORDER

**Phase 1 — Immediate (no dependencies):**
- PHYS-26 (normalization — documentation)
- PHYS-31 (statistical control — Track B gate)
- PHYS-36 (A₃ decomposition)
- **PHYS-38 (loop expansion — new)**
- **PHYS-39 (Omega remainder domain — new)**

**Phase 2 — After Phase 1:**
- PHYS-27 (sin²θ_W from 3/8)
- PHYS-28 (VL two-loop)
- PHYS-32 (Set B Omegas)
- PHYS-33 (Λ interpolation)

**Phase 3 — After Phase 2:**
- PHYS-29 (GUT thresholds)
- PHYS-34 (per-transit mechanism)
- PHYS-37 (Koide amplitude)
- **PHYS-40 (sin²θ_W = 3/13 test — new, after PHYS-27)**

**Phase 4 — After Phase 3:**
- PHYS-30 (α_s prediction)
- PHYS-35 (boundary count)

Total program: 16 papers (PHYS-25 through PHYS-40), 15 scripts, ~550 estimated checks.

---

