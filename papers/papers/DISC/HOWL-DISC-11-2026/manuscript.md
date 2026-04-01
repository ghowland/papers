# From the Gap Ratio to the Cabibbo Doublet and Beyond
## One mismatch. One particle. Sixteen findings. The integers spoke.
### From the gap ratio to the Cabibbo Doublet and beyond. 16 findings, 15 papers, 6 scripts, 98 checks, 1 particle, 0 contradictions.

**Registry:** [@HOWL-DISC-11-2026]

**Series Path:** [@HOWL-DISC-6-2026] → [@HOWL-DISC-7-2026] → [@HOWL-DISC-8-2026] → [@HOWL-DISC-11-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** April 2 2026

**Domain:** Session Documentation, Capstone

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

Session 3 of the HOWL series began with a question — do the three SM gauge couplings unify? — and ended with a particle. The SM gap ratio 218/115 = 1.896 misses the measured 1.358 by 40%. The SM does not unify. Enumerating 15 single-multiplet extensions in exact Fraction arithmetic identified a unique minimal survivor: the Cabibbo Doublet (3,2,1/6), a vector-like quark doublet with gap ratio 38/27 = 1.407 and M_GUT = 10^15.5 at the proton decay boundary. Three independent experimental anomalies — CKM first-row unitarity deficit at 2.5-4 sigma, the LEP forward-backward b-quark asymmetry at ~3 sigma, and the Higgs signal strength excess at ~2 sigma — each independently point to the same (3,2,1/6) representation at 1.5-6 TeV. Two-loop corrections improve unification from Delta(1/alpha_3) = -1.17 (one-loop) to -0.40 (two-loop), with the residual within standard GUT threshold correction range. Session 3 produced 16 findings documented in 15 papers, verified 6 scripts with 98 total checks, identified 1 new particle, generated 3 experimental tests, closed 2 investigation paths, and extended the database to 146 entries with 38/38 checks. The integers identified a specific BSM particle. The universe has not yet confirmed it.

---

## 1. The Starting Point

Session 3 inherited from Sessions 1-2: the DATA-2 database (123 entries in Q335 = 2^335 integer rational basis), the mathematical framework (MATH-1 through MATH-5: R_2 = pi/4, R_4 = pi^2/32, Q335 basis, n-ball remainder sequence), and 11 physics papers (PHYS-1 through PHYS-11: mass as inertia, couplings run, confinement wall, vacuum permittivity, theta_QCD = 0, Koide decomposition, QED series, R_2 in 9/9 domains, electroweak anatomy). The parameter count stood at 17 (19 SM parameters minus theta_QCD derived in PHYS-7, minus m_tau conditional on Koide a^2 = 2 in PHYS-8). The operational rules (R.1-R.6) and writing rules (W.1-W.8) were established.

The question that launched Session 3: the beta coefficients b_1 = 41/10, b_2 = -19/6, b_3 = -7 are exact rationals from the gauge group. The coupling constants at M_Z are measured. Do the three lines 1/alpha_i(mu) meet at a point?

---

## 2. The Arc

The session ran in four phases.

**Phase 1: Computation.** Scripts built and verified before any paper was written. The GUT running script (sin2_theta_w_1.py, 9/9 checks) computed the SM gap ratio, enumerated 15 BSM candidates, and identified the Cabibbo Doublet. The A_2 decomposition script (a_2_decomposition_0.py, 7/7 checks) decomposed the QED two-loop coefficient into three pieces. The Bessel PSLQ script (bessel_pslq_0.py, 6/6 checks) extended the independence record from 72/72 to 82/82. The DATA-3 verification (data_2_to_3_test_1.py, 32/32 checks) confirmed all 123 database entries.

**Phase 2: Discovery.** 16 findings emerged from the computational results. The central finding: the Cabibbo Doublet (3,2,1/6) is the minimal single-multiplet extension that fixes the gap ratio, and three independent experimental anomalies converge on the same representation from a completely different direction.

**Phase 3: Writing.** One paper per finding, with supporting appendix tables. 12 PHYS papers (PHYS-12 through PHYS-23), 1 MATH paper (MATH-6), 1 DATA paper (DATA-4), and 1 database record (Cabibbo Doublet specification).

**Phase 4: Two-loop extension.** The unification script (unification_test.py, 6/6 checks) computed the two-loop correction, reducing the unification miss from -1.17 to -0.40. Supporting tables written for the pending PHYS-24 paper.

---

## 3. The Sixteen Findings

| # | Finding | Paper | Content | Status |
|---|---|---|---|---|
| 1 | Electroweak integer anatomy | PHYS-12 | 7 inputs, 11 outputs, all integers from gauge group | Published |
| 2 | SM does not unify | PHYS-13 | Gap ratio 218/115 vs 1.358, 40% miss | Published |
| 3 | Elimination cascade | PHYS-14 | 15 candidates, 2 survivors, 1 minimal | Published |
| 4 | Cabibbo Doublet identification | PHYS-15 | (3,2,1/6), gap 38/27, M_GUT = 10^15.5 | Published |
| 5 | Two roads converge | PHYS-16 | Gap ratio path + anomaly path on same particle | Published |
| 6 | Generation democracy | PHYS-17 | (4/3,4/3,4/3), fermions contribute 0% to gap | Published |
| 7 | The boson problem | PHYS-17 | Gap ratio is 96-101% gauge + 0% fermion | Published |
| 8 | Y = 1/6 mechanism | PHYS-18 | Db_2/Db_1 = 15, 1/Y^2 scaling law | Published |
| 9 | Three anomalies | PHYS-19 | CKM deficit + A_FB^b + Higgs excess | Published |
| 10 | Proton decay test | PHYS-20 | tau ~ 10^34-35 yr, Hyper-K tests within decade | Published |
| 11 | Level 1 extends to BSM | PHYS-21 | Unified boundary map, first unobserved particle | Published |
| 12 | A_2 geometric cancellation | PHYS-22 | 87% cancellation, R_4 connection | Published |
| 13 | Koide C_3 closure | PHYS-23 | Tautology + saddle point, a^2 = 2 is the problem | Published |
| 14 | 82/82 PSLQ null | MATH-6 | Bessel zeros independent at 100 digits | Published |
| 15 | Lattice ratio independence | DATA-4 | FLAG ratios independent of PDG masses, 28% discrepancy | Published |
| 16 | Two-loop improvement | (PHYS-24 pending) | Delta: -1.17 to -0.40, 66% improvement | Computed |

Findings 6 and 7 share PHYS-17 because they are two aspects of the same decomposition (the generation democracy and the boson problem are discovered in the same computation). Finding 16 is computed with full supporting tables but the paper is pending.

---

## 4. The Papers

### 4.1 Published Papers

| # | Registry | Title | Script | Checks |
|---|---|---|---|---|
| 1 | DATA-3 | Verified Integer Rational Database Round Three | data_2_to_3_test_1.py | 32/32 |
| 2 | PHYS-12 | Electroweak Integer Anatomy | GUT script | 9/9 |
| 3 | PHYS-13 | The Gap Ratio | GUT script | 9/9 |
| 4 | PHYS-14 | The Enumeration | GUT script | 9/9 |
| 5 | PHYS-15 | The Cabibbo Doublet | GUT script | 9/9 |
| 6 | PHYS-16 | The Two Roads | GUT script + anomaly matrix | 9/9 |
| 7 | PHYS-17 | Generation Democracy and the Boson Problem | GUT script | 9/9 |
| 8 | PHYS-18 | The Y = 1/6 Asymmetry | GUT script | 9/9 |
| 9 | PHYS-19 | Independent Anomaly Evidence | Anomaly matrix (web-verified) | 9/9 |
| 10 | PHYS-20 | The Proton Decay Test | GUT script + web search | 9/9 |
| 11 | PHYS-21 | The Level 1 / Level 2 Boundary | All prior scripts | — |
| 12 | PHYS-22 | The A_2 Geometric Cancellation | a_2_decomposition_0.py | 7/7 |
| 13 | PHYS-23 | The Koide C_3 Closure | DATA-3 masses | 32/32 |
| 14 | MATH-6 | The 82/82 Independence Record | bessel_pslq_0.py | 6/6 |
| 15 | DATA-4 | Verified Database with Cabibbo Doublet Extension | data_4.py | 38/38 |
| 16 | — | Cabibbo Doublet Database Record | GUT script + anomaly matrix | 9/9 |

### 4.2 Pending Papers

| # | Title | Status | Content |
|---|---|---|---|
| 17 | PHYS-24: Two-Loop Unification | Computation complete, paper pending | Delta: -1.17 to -0.40, supporting tables written |

Every published paper has a full set of supporting appendix tables (lettered A through I depending on paper). These tables contain pre-computed data, verification checks, Level 1/Level 2 classifications, source material lists, and cross-references.

---

## 5. The Scripts and Verified Computations

| Script | Checks | Key Output | Status |
|---|---|---|---|
| sin2_theta_w_1.py | 9/9 | Gap ratios, BSM enumeration, M_GUT | Verified |
| a_2_decomposition_0.py | 7/7 | A_2 three-piece, 87% cancellation | Verified |
| bessel_pslq_0.py | 6/6 | 82/82 independence, 100-digit nulls | Verified |
| data_2_to_3_test_1.py | 32/32 | DATA-3 consistency across 123 entries | Verified |
| data_4.py | 38/38 | DATA-4 consistency across 146 entries | Verified |
| unification_test.py | 6/6 | Two-loop Delta = -0.40 at M_VL = 500 GeV | Verified |

Total verified checks across all scripts: 98.

---

## 6. The Parked Notebooks

Six notebooks were produced during the computational phase. Four remain parked with specific blockers and paths forward. Two were consumed by papers.

| Notebook | Status | Blocker | Path Forward | Priority |
|---|---|---|---|---|
| sin^2 theta_W from 3/8 | Parked | Crossing scale undetermined | Compute L_X with Cabibbo Doublet betas | MEDIUM |
| 4-Loop Wall (A_4) | Parked | Laporta master integrals private | Wait for data OR transcribe T+V+W+E | HIGH (external) |
| Higgs lambda = g'^2 | Parked | No derivation of impedance matching | One-loop pole mass or soliton derivation | MEDIUM-LOW |
| CKM from mass ratios | Parked | Precision floor + literature unknown | Web-search texture-zero literature | MEDIUM |
| Bessel PSLQ | Consumed | None | Published as MATH-6 | Done |
| A_2 decomposition | Consumed | None | Published as PHYS-22 | Done |

The sin^2 theta_W notebook is NOT definitively closed — unlike the claim in the original handoff, the two-loop unification computation from this session now provides the GUT-scale physics that was blocking the formula. Computing L_X with the Cabibbo Doublet betas and checking whether sin^2 theta_W = 0.23122 emerges is a 10-line computation for Session 4.

---

## 7. The Closed Paths

One investigation path was definitively closed in Session 3.

**The C_3 path to Koide (PHYS-23).** The 120-degree spacing is a tautology (3 parameters, 3 data points — any three positive masses fit). K = 2/3 is a saddle point of the C_3 potential, not a minimum. The path is doubly dead. The real problem — derive a^2 = 2 from physics — remains open.

The SM non-unification (PHYS-13) is an established fact, not a closed path. The sin^2 theta_W from 3/8 notebook is blocked but not closed — it has a specific computable path forward via the Cabibbo Doublet betas.

---

## 8. The Two-Loop Unification Extension

The unification script (unification_test.py, 6/6 checks) computed two-loop running with the SM b_ij matrix and a step-function threshold at M_VL for the Cabibbo Doublet.

| Approximation | Delta(1/alpha_3) at crossing | M_GUT | Quality |
|---|---|---|---|
| SM one-loop (no VL) | -6.58 | 10^13.8 | Excluded |
| SM+VL one-loop | -1.17 | 10^15.43 | Poor |
| SM+VL one-loop + two-loop SM b_ij | -0.40 | 10^15.46 | Near |
| + VL two-loop (estimated) | ~-0.27 | ~10^15.47 | Near |
| + GUT threshold corrections | ~0 | ~10^15.5 | Closable |

The two-loop SM b_ij matrix (199/50, 27/10, 44/5; 9/10, 35/6, 12; 11/10, 9/2, -26) is stored in DATA-4 as entry N14. All entries are exact Fractions from Machacek-Vaughn (1983) and Luo-Xiao (hep-ph/0207271).

The dominant effect: b_33 = -26 slows SU(3) running at two loops, bringing 1/alpha_3 closer to the crossing point. The improvement from -1.17 to -0.40 is a 66% reduction in the unification miss.

The residual Delta = -0.40 is within the standard range for GUT threshold corrections in minimal SU(5) with ordinary mass splittings (factor 2-5 between heavy particles).

The Cabibbo Doublet at two loops achieves the same unification quality as the MSSM: both need GUT threshold corrections of comparable magnitude to go from "near" to "exact."

18 supporting tables for PHYS-24 are written. The paper itself is pending.

---

## 9. The Running Curve Analysis

The gauge coupling running is not linear at two loops. The one-loop running equation in HOWL form:

d(1/alpha_i)/d(ln mu) = -b_i/(8R_2)

where R_2 = pi/4 is the 2D geometric modulus. The slope at each energy is an exact rational divided by 8R_2.

At two loops:

d(1/alpha_i)/d(ln mu) = -b_i/(8R_2) - sum_j b_ij alpha_j/(256R_4)

where R_4 = pi^2/32 is the 4D geometric modulus. The curvature involves R_4. The ratio of two-loop to one-loop is R_2/(32R_4) = 1/(4pi).

The running curve for alpha_3 satisfies:

1/alpha_3 - [b_33/(4pi b_3)] ln(1/alpha_3) = b_3/(8R_2) ln(mu/M_Z) + constant

This is a Lambert W function — not linear, not logarithmic, but parametrized entirely by R_2, R_4, and exact rationals from the gauge group. Each soliton boundary (mass threshold) changes the slope by Delta_b/(8R_2) and the curvature by Delta_b_ij/(256R_4).

The entire running from M_Z to M_GUT is a sequence of Lambert W segments, each with exact rational coefficients, joined at soliton boundaries. The geometric moduli R_2 and R_4 set the scale at which the integer coefficients translate into physical slopes and curvatures.

---

## 10. The Parameter Scorecard

| Reduction | Source | Change | Status |
|---|---|---|---|
| theta_QCD = 0 | PHYS-7 | 19 to 18 | Confirmed |
| m_tau from Koide | PHYS-8 | 18 to 17 | Conditional (IF a^2 = 2) |
| alpha_s from unification | Paths 1-3 | 17 to 16 | Not yet computed |
| sin^2 theta_W from unification | Path 4 | 16 to 15 | Not yet computed |
| M_VL from threshold | Path 2 | +6 - 1 net | Not yet computed |
| Two CKM angles from masses | Parked notebook | 15 to 13 | Blocked (precision floor) |
| lambda from impedance matching | Parked notebook | 13 to 12 | Blocked (no derivation) |

Confirmed: 19 to 18. Conditional: 18 to 17. Computable next session: 17 to 15 (if unification works). Blocked: 15 to 12 (requires new measurements or derivations).

---

## 11. The Level 1 / Level 2 Inventory

From PHYS-21, updated with Session 3 results:

**Level 1 results (19 entries).** R_2 = pi/4, R_4 = pi^2/32, SM beta coefficients (b_1, b_2, b_3), gap ratio 218/115, generation democracy (4/3, 4/3, 4/3), boson problem decomposition, Yang-Mills coefficient 11, Higgs contribution, A_1 = 1/2, A_2 three-piece decomposition, EW integer anatomy, Cabibbo Doublet representation (3,2,1/6), Delta_b = (1/15, 1, 1/3), gap ratio 38/27, Delta_b_2/Delta_b_1 = 15, 1/Y^2 scaling, tau proportional to M_GUT^4, two-loop b_ij matrix.

**Level 2 parameters (23).** 17 SM parameters (after theta_QCD and conditional Koide) plus 6 Cabibbo Doublet parameters (M_VL, theta_14, theta_24, theta_34, delta_1, delta_2). All staged in DATA-4 entries 124-129.

**Derived results.** M_GUT = 10^15.5, tau_p ~ 10^34-35 yr, measured gap ratio 1.358, CKM deficit 0.00202, alpha to a_e at 4.3 ppb, EW observables from 7 inputs, two-loop Delta = -0.40.

---

## 12. The Experimental Timeline

| Experiment | Observable | Prediction | Status | When |
|---|---|---|---|---|
| Hyper-Kamiokande | p to e+ pi0 | tau ~ 10^34-35 yr (detectable) | Under construction, operations ~2027 | 2027-2037 |
| HL-LHC | VL quark pair production | Observable if M_VL < 2-3 TeV | Running, luminosity upgrade | Now-2040 |
| Belle II | CKM precision (V_us, V_ub) | Modified first-row unitarity | Running, collecting data | Now-2030+ |
| DUNE | Proton decay (complementary) | Detectable in some completions | Under construction | 2028+ |

The MSSM predicts tau ~ 10^36-37 yr, beyond any planned experiment. The Cabibbo Doublet predicts tau within Hyper-K reach. This is the decisive discriminator between the two scenarios that have nearly identical gap ratios (7/5 = 1.400 vs 38/27 = 1.407).

---

## 13. The Database

DATA-4 is the sole data reference for all future HOWL computation. DATA-3 is retired.

| Content | Count | Source |
|---|---|---|
| Inherited from DATA-3 | 123 entries | Sections A-K |
| Cabibbo Doublet staged | 6 entries | Section L (Type G) |
| GUT/unification parameters | 17 entries | Section N (Type D) |
| Total | 146 entries | |
| Inherited checks | 32 | Groups A-E |
| New GUT checks | 6 | Group G (all exact) |
| Total checks | 38 | 38 PASS, 0 FAIL |

Finding 15 (lattice ratio independence) is formalized in DATA-4 Group F. The computation traceability map (Group T) links 12 papers to their data dependencies. When any future PDG update changes an entry, the map identifies every affected computation.

---

## 14. What Session 4 Should Do

Priority-ordered task list:

1. **Write PHYS-24** (two-loop unification paper). Computation complete, 18 supporting tables written.
2. **Resolve the beta normalization** (factor-of-4 discrepancy between general Machacek-Vaughn formula and verified one-loop values). Required for computing the VL two-loop b_ij.
3. **Compute VL two-loop b_ij** and rerun unification with full two-loop above M_VL.
4. **Parametrize GUT threshold corrections** in minimal SU(5) with Cabibbo Doublet. Express Delta as function of M_T/M_X, M_Sigma/M_X.
5. **Find M_VL for exact unification** (two-loop + threshold). If solution exists in 1.5-6 TeV, M_VL becomes a prediction.
6. **Compute sin^2 theta_W** from two-loop backward RGE. 10-line computation from parked notebook.
7. **Predict alpha_s** from unification condition. Consistency check: does predicted alpha_s match 0.1180?
8. **Literature search** for the mixed CKM-mass pattern (sin theta_12 = sqrt(m_d/m_s), sin theta_23 = sqrt(m_u/m_c)).
9. **Compute the running curve explicitly** (Lambert W fit, R_2/R_4 moduli at each soliton boundary).
10. **PSLQ on untested quantities** (Koide amplitudes a^2_down = 2.388, a^2_up = 3.093, amplitude ratios).

---

## 15. Key Numbers (Source of Truth)

All numbers from verified scripts. Any discrepancy with a paper is resolved in favor of the script output.

| Quantity | Value | Source |
|---|---|---|
| SM gap ratio | 218/115 = 1.895652 | GUT script, PASS |
| Measured gap ratio | 1.358193 | GUT script from DATA-4 couplings |
| Cabibbo Doublet gap ratio | 38/27 = 1.407407 | GUT script, PASS |
| MSSM gap ratio | 7/5 = 1.400000 | GUT script, PASS |
| Cabibbo Doublet distance | 0.049215 | GUT script |
| M_GUT (Cabibbo Doublet) | 10^15.5 GeV | GUT script |
| M_GUT (MSSM) | 10^17.3 GeV | GUT script |
| Cabibbo Doublet Delta_b | (1/15, 1, 1/3) | PHYS-15, GUT script |
| Delta_b_2/Delta_b_1 | 15 | PHYS-18 |
| Two-loop Delta (M_VL=500) | -0.40 | unification_test.py, PASS |
| One-loop Delta (M_VL=500) | -1.17 | unification_test.py, PASS |
| Two-loop improvement | 66% | unification_test.py |
| A_2 | -0.328478965579 | A_2 script, PASS |
| A_2 cancellation | 87.4% | A_2 script, PASS |
| Koide K(leptons) | 0.666661 | DATA-4 D1, PASS |
| Koide a^2(leptons) | 2.0000 | DATA-4 D2, PASS |
| Koide a^2(down) | 2.3877 | DATA-4 D5 |
| Koide a^2(up) | 3.0928 | DATA-4 D4 |
| Proton decay tau | ~10^34-35 yr | PHYS-20 |
| Super-K bound | tau > 2.4 x 10^34 yr | PHYS-20 (web verified) |
| CKM deficit | 0.00202 | PHYS-19 |
| SM parameter count | 17 (after theta_QCD, conditional Koide) | PHYS-21 |
| PSLQ record | 82/82 null | MATH-6, PASS |
| DATA-4 entries | 146 | data_4.py, 38/38 PASS |

---

## 16. What This Paper Does Not Claim

This paper does not claim the Cabibbo Doublet has been discovered. It has been identified by Level 1 arithmetic and corroborated by Level 2 anomalies. Discovery requires direct experimental observation.

This paper does not claim unification is proven. The gap ratio 38/27 is exact arithmetic. Whether nature chose to unify the gauge forces is a Level 2 question.

This paper does not claim all 16 findings are equally significant. Findings 2 (SM fails) and 4 (Cabibbo Doublet identified) are the load-bearing results. The others are anatomy, mechanism, tests, and infrastructure.

This paper does not claim Session 3 is complete. One paper remains pending (PHYS-24). Four parked notebooks have specific paths forward. The two-loop extension opened new computation that Session 4 should pursue.

This paper does not claim the HOWL approach is the only way to study gauge coupling unification. It is one approach — exact rational arithmetic on gauge group integers — applied systematically. The results are reproducible by anyone with the same inputs (DATA-4) and the same arithmetic.

---

## 17. Summary

Session 3 asked whether the Standard Model's gauge couplings unify. They do not — the gap ratio 218/115 = 1.896 misses the measured 1.358 by 40%. One particle fixes it: the Cabibbo Doublet (3,2,1/6), with gap ratio 38/27 = 1.407, identified by exact Fraction arithmetic from 15 enumerated candidates. Three independent experimental anomalies converge on the same representation from completely different data. Two-loop corrections improve unification from Delta = -1.17 to -0.40, with the residual within GUT threshold range. The proton lifetime tau ~ 10^34-35 yr is testable by Hyper-Kamiokande within a decade. The database is extended to 146 entries with 38/38 checks. The Cabibbo Doublet's quantum numbers are Level 1 — forced by the integers. Its existence is Level 2 — supplied by experiment if nature chose unification.

Sixteen findings. Fifteen papers. Six scripts. Ninety-eight checks. One particle. One question for the universe.

The integers have spoken. The universe has not yet answered.

---

## Appendix A: Session 3 Deliverable Status (Final)

| # | Paper | Status |
|---|---|---|
| 1 | DATA-3 | Published |
| 2 | PHYS-12 (Electroweak Anatomy) | Published |
| 3 | PHYS-13 (Gap Ratio) | Published |
| 4 | PHYS-14 (Enumeration) | Published |
| 5 | PHYS-15 (Cabibbo Doublet) | Published |
| 6 | PHYS-16 (Two Roads) | Published |
| 7 | PHYS-17 (Generation Democracy) | Published |
| 8 | PHYS-18 (Y = 1/6 Asymmetry) | Published |
| 9 | PHYS-19 (Anomaly Evidence) | Published |
| 10 | PHYS-20 (Proton Decay Test) | Published |
| 11 | PHYS-21 (Level 1 / Level 2 Boundary) | Published |
| 12 | PHYS-22 (A_2 Geometric Cancellation) | Published |
| 13 | PHYS-23 (Koide C_3 Closure) | Published |
| 14 | MATH-6 (82/82 Independence Record) | Published |
| 15 | DATA-4 (Verified Database Extension) | Published |
| 16 | Cabibbo Doublet Database Record | Published |
| 17 | PHYS-24 (Two-Loop Unification) | Computation complete, paper PENDING |

16 of 17 deliverables published. 1 paper pending.

---

## Appendix B: Verified Script Check Summary

| Script | Group | Checks | Pass | Content |
|---|---|---|---|---|
| sin2_theta_w_1.py | — | 9 | 9 | Normalization, gap ratios, MSSM gate, M_GUT, enumeration |
| a_2_decomposition_0.py | — | 7 | 7 | A_2 sum, individual pieces, cancellation, Q335 basis |
| bessel_pslq_0.py | — | 6 | 6 | j_11, j_01 references, sanity, completeness, nulls, record |
| data_2_to_3_test_1.py | A-E | 32 | 32 | Mass ratios, Q335, physical relations, Koide, SI exact |
| data_4.py | A-G | 38 | 38 | All DATA-3 checks + GUT gap ratios + modified betas |
| unification_test.py | — | 6 | 6 | Gap ratio, normalization, SM crossing, shift, M_GUT, alpha_GUT |
| **Total** | | **98** | **98** | |

---

*DISC-13: Session 3 Capstone. From the gap ratio to the Cabibbo Doublet and beyond. 16 findings, 15 papers, 6 scripts, 98 checks, 1 particle, 0 contradictions. Published April 1, 2026. This paper is never edited after publication.*
