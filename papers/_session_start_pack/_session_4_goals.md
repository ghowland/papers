## Session 4+ Handoff: Goals, Program, and Kill Switches

**For any Claude session starting from PHYS-24.**

**Written by:** Session 4 Review Claude, after reading all 30+ papers, all scripts, all data, building the platform library, and reviewing the complete PHYS-24 paper.

**Date:** April 2 2026

---

### What You Have

You have PHYS-24 (the operational lexicon), phys24_lib.py (the platform library, 21/21 self-test, 148/148 platform test), phys24_lib_test.py, phys24_script_rules.md (22-section computational standard), and 8 template scripts (62/62 checks). That is the complete starting pack. Everything established through Session 3 is encoded in these files.

You do not need to read any earlier paper unless you are working on a specific topic that requires depth beyond what PHYS-24 provides. The lexicon was designed to replace reading 30 papers.

---

### What PHYS-24 Does Not Contain

PHYS-24 records what is fixed, open, and closed. It does not contain the research program going forward. This document does.

---

### The Cabibbo Doublet Lane

This is the strongest research lane by a large margin. It has the sharpest Level 1 result (gap ratio 38/27 from exact Fraction arithmetic), the strongest Level 2 corroboration (three independent anomalies each using a different quantum number), and the clearest experimental future (Hyper-Kamiokande decisive by ~2037). Every other research direction is secondary to this lane until it is either confirmed or killed.

The lane has five sequential stages. Each stage depends on the one before it. Do not skip ahead.

**Stage 1: sin²θ_W from 3/8 (UNBLOCKED, ~10 lines)**

This is the first computation. At the GUT scale, SU(5) gives sin²θ_W = 3/8. Running down to M_Z with one-loop betas gives a prediction for sin²θ_W(M_Z). The key quantity is L_X = ln(M_GUT/M_Z)/(2π), determined by the Cabibbo Doublet modified betas. All inputs are in phys24_lib.py. The coefficient in the running formula should be derived from the betas, not assumed from the parked notebook — verify it.

Success: predicted sin²θ_W consistent with 0.23122 (DATA-4 B11).
Failure: gross inconsistency (more than a few percent) kills the minimal SU(5)-type completion. The CD itself survives but the GUT completion changes.

**Stage 2: α_s prediction from unification**

Same framework as Stage 1. If the three couplings unify at M_GUT with CD betas, that unification condition plus two measured couplings (α⁻¹ and sin²θ_W) predicts the third (α_s). Compare against 0.1180 (DATA-4 B12).

Success: predicted α_s within a few percent of measured.
Failure: same consequence as Stage 1 — completion changes, CD survives.

**Stage 3: VL two-loop b_ij and full two-loop unification**

The current two-loop result (Δ = −0.40, 66% improvement) uses the SM b_ij matrix above the VL threshold. The Cabibbo Doublet modifies the two-loop matrix as well. Computing the VL contribution to b_ij requires the same Dynkin index formulas used for the one-loop shifts, extended to two loops. The normalization conventions between Machacek-Vaughn and the GUT-normalized betas must be resolved cleanly before this computation is trusted.

The computation is: derive the VL two-loop b_ij entries, add them to the SM matrix above M_VL, rerun the coupled RGE, report the new Δ. The existing unification_test.py (Session 3, 6/6 checks) is the reference implementation.

Success: Δ improves further or stays comparable to −0.40.
Failure: Δ gets worse. If |Δ| > 2, the two-loop result is no longer within threshold correction range and the viability envelope shrinks.

**Stage 4: GUT threshold corrections**

The residual Δ after two loops is expected to be closed by GUT threshold corrections — mass splittings among the heavy GUT particles (colored Higgs triplet, X/Y bosons, etc.). This is a parametric computation: express Δ as a function of M_T/M_X splitting in minimal SU(5), then determine what splitting is needed to close the gap.

This is standard GUT phenomenology. The formulas exist in the literature. The computation is: look up the threshold correction formula, express it in Fraction arithmetic using phys24_lib constants, solve for the required splitting, and check whether it is physically reasonable (factor 2-5 between heavy particle masses is normal).

Success: reasonable splitting closes the gap.
Failure: required splitting is unphysically large (factor 100+). This weakens the minimal SU(5) completion but does not kill the CD.

**Stage 5: M_VL for exact unification**

Combine Stages 3 and 4. Scan M_VL across the 1.5-6 TeV window. For each M_VL, compute the full two-loop running with VL contributions and GUT thresholds. Find the M_VL value (if any) that gives exact unification with reasonable threshold corrections.

Success: a value of M_VL in the 1.5-6 TeV window produces exact unification.
Failure: no M_VL in the window works. This is a serious problem for the CD as a unification candidate, though the anomaly evidence and gap ratio arithmetic remain valid.

---

### The Electroweak Precision Lane

This is the second priority lane. It tests whether the Cabibbo Doublet is consistent with precision electroweak measurements, not just unification.

**Stage 6: S, T oblique parameters**

A vector-like quark doublet contributes to the Peskin-Takeuchi S and T parameters. The contribution depends on the mass splitting between the upper and lower components and on the mixing angles. Compute S and T as functions of M_VL and the mass splitting. Compare against the measured S-T ellipse.

This requires electroweak loop integrals. The infrastructure from PHYS-12 (electroweak integer anatomy) provides the framework. The computation is standard — it appears in any BSM textbook.

Success: the CD contribution is inside the measured S-T ellipse for reasonable mass splittings.
Failure: the CD is excluded by oblique corrections. This would be a serious blow.

**Stage 7: Z-b-b vertex correction**

The LEP A_FB^b anomaly (~3σ, persistent for 25+ years) is one of the three anomalies pointing to the CD. The CD resolves it through VL-b mixing modifying the Z-b-b vertex. Compute the vertex correction as a function of θ₃₄ (the VL-b mixing angle).

Success: the correction brings A_FB^b into agreement with SM prediction for a reasonable θ₃₄.
Failure: no θ₃₄ value works, or the required value conflicts with other constraints.

**Stage 8: CKM extension consistency**

The CD extends the 3×3 CKM matrix to 3×4. The CKM first-row deficit (0.00202 ± 0.00038) is absorbed as |V_ub'|². Parametrize the extended CKM with θ₁₄, θ₂₄, θ₃₄, δ₁, δ₂. Check that kaon constraints (θ₂₄), B-physics constraints (δ₂), neutron EDM constraints (δ₁), and the A_FB^b fit (θ₃₄) are simultaneously satisfiable.

Success: a consistent region exists in the 6-parameter space.
Failure: constraints are mutually exclusive. This would weaken the anomaly convergence argument significantly.

---

### The Boundary-Law Program (Exploratory)

This is a new exploratory direction discussed in Session 4 planning. It is lower priority than the Cabibbo Doublet lane and the electroweak precision lane.

The idea: measured running curves (α_EM(q), α_s(q), running masses) are currently described by standard piecewise-logarithmic RG evolution with thresholds. The question is whether re-expressing this running in terms of discrete shell/boundary transitions reveals additional structure — stable integer shell indices, rational step patterns, or universal boundary laws that hold across sectors.

This is NOT free-form curve fitting. It is NOT PSLQ pattern hunting. It is a structured test program with explicit kill switches.

**Phase A: Define law families before fitting anything.** Five candidates: L0 (standard piecewise-log, the control), L1 (piecewise-log with integer shell labels), L2 (rational-step shell law), L3 (quadratic shell law), L4 (mixed log-shell law), L5 (null — no useful shell structure). All must be formally defined before any data is touched.

**Phase B: Calibrate on α_EM first.** This is the best-understood running. Thresholds are known. The PHYS-5 and PHYS-9 infrastructure exists. If shell reinterpretation yields no stable nontrivial structure beyond standard thresholds, kill that law family for all later sectors. This is the most important kill switch in the program.

**Phase C: If α_EM passes, test on perturbative α_s.** Same shell formalism, different sector. If it works only in one sector and collapses in the other, it is not universal.

**Phase D: If both pass, cautiously extend to running quark masses.** Lower priority, weaker data. Park if precision is inadequate rather than over-fitting.

---

### What Is Closed (Do Not Reopen)

These paths have been tested and killed. Do not spend time on them.

- SM unification at one loop (gap ratio 218/115 ≠ 1.358, 40% miss)
- C₃ route to Koide (tautology: 3 params, 3 data points, plus saddle point — PHYS-23)
- Broad PSLQ pattern hunting (82/82 null across 3 categories — MATH-6)
- Fermion-only gap ratio fix (generation democracy: fermion contribution exactly zero — PHYS-17)
- λ = 1/8 for Higgs self-coupling (corrections go wrong direction)
- Koide phase adjustment for quarks (K depends on a only, not θ₀ — PHYS-8)
- Scale choice fixing quark Koide (K is exactly scale-invariant)

---

### What Is Parked (Revisit Only If New Input Arrives)

- 4-loop A₄ wall (blocked by private Laporta master integral data)
- CKM from mass ratios (blocked by quark mass precision floor ~10%)
- Higgs λ = g'² impedance matching (blocked by no derivation from soliton framework)
- Koide amplitude a² = 2 derivation (no viable attack path known — the deepest open problem)
- Cosmological boundary transit calculations (need a derived per-transit law first)
- G altitude/latitude trend mining (underpowered with current data)

---

### Kill Switches

These are the global discipline rules. If a kill switch fires, stop work on that direction immediately.

**K1: Calibration failure.** If the boundary-law program fails on α_EM, do not generalize it to weaker sectors.

**K2: Universality failure.** If a candidate shell law works only by ad hoc retuning independently in each sector, do not call it universal.

**K3: Cabibbo viability failure.** If two-loop + threshold + basic phenomenology leaves no viable CD parameter region, downgrade the CD from "primary candidate" to "conditional candidate" and shift effort to damage assessment.

**K4: Underpowered analysis.** If an analysis cannot realistically discriminate among models at available precision, park it. Do not publish weak suggestive fits.

**K5: Parameter inflation.** If a shell-law model gains fit quality only by adding unconstrained parameters, kill it. The law must buy explanatory compression.

---

### Workflow Rules

These are inherited from this session and encoded in phys24_script_rules.md. The new session must follow them.

- Scripts first, paper second. Every number in a paper must come from a passing script.
- One script per prompt. Do not combine scripts to save tokens.
- Scripts in chat as code blocks. The human runs them and pastes back output.
- Papers in chat as markdown. Never docx. Never file attachments during drafting.
- Diagrams as Python scripts. No JavaScript, no widgets, no interactive elements.
- Follow the review → plan → agreement → code workflow. Do not write code until the plan is reviewed and agreed.
- All computation uses Fraction arithmetic. No math module, no float(), no assert. mpf at the display boundary only. 100 dps standing precision.
- Every script imports `from phys24_lib import *`. No hardcoded constants.
- If a value is needed that isn't in the library, add it to the library first, update the self-test, rerun, then use it.

---

### The Priority Stack

In order. Do not skip ahead.

1. sin²θ_W from 3/8 (unblocked, ~10 lines, Stage 1)
2. α_s prediction from unification (Stage 2)
3. VL two-loop b_ij and full two-loop unification (Stage 3)
4. GUT threshold corrections (Stage 4)
5. M_VL for exact unification (Stage 5)
6. S, T oblique parameters (Stage 6)
7. Z-b-b vertex correction (Stage 7)
8. CKM extension consistency (Stage 8)
9. Boundary-law program calibration on α_EM (exploratory, only after 1-5)
10. Targeted PSLQ on Koide amplitudes (optional, only if main lane complete)

---

### What Success Looks Like

At the end of Session 4, the strongest possible outcome is:

- sin²θ_W and α_s predicted from unification, consistent with measurement
- Full two-loop + threshold unification with a specific M_VL in the 1.5-6 TeV window
- S, T, Z-b-b, and CKM constraints simultaneously satisfied
- A clean boundary-law calibration result on α_EM (positive or null — both are informative)
- 3-5 new verified scripts extending the 62/62 foundation
- One or two new PHYS papers (PHYS-25 on sin²θ_W/α_s predictions, PHYS-26 on full CD viability envelope)

The weakest acceptable outcome is:

- sin²θ_W computation complete (even if the result is surprising)
- Two-loop normalization resolved
- At least one new verified script
- Clear documentation of what worked, what failed, and why

---

### One Sentence

The job now is to take the Cabibbo Doublet from "interesting Level 1 candidate with Level 2 corroboration" to "quantitatively viable or cleanly killed" by executing the unification prediction chain, the electroweak precision chain, and the CKM consistency chain, in that order, with kill-switch discipline at every stage.

---

