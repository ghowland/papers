# Supporting Tables for PHYS-16: The Cabibbo Doublet — Complete Specification

## Purpose

PHYS-16 is the "today I learn about the Cabibbo Doublet" paper. A reader who has never heard of this particle reads PHYS-16 and knows everything: what it is, why it's needed, how it was identified, what anomalies it resolves, what its properties are, how to find it, and what it connects to. Self-contained. No prior HOWL paper required for comprehension.

---

## Table 16.1: Identity Card

| Property | Value | Source |
|---|---|---|
| Series name | Cabibbo Doublet | Named for the Cabibbo angle anomaly it resolves |
| Full designation | Integer-forced Cabibbo Doublet | PHYS-15 identification method |
| Representation | (3, 2, 1/6) under SU(3)×SU(2)×U(1)_Y | Gauge group representation theory |
| Type | Vector-like quark doublet | Both L and R chiralities transform identically |
| Upper component charge | Q = T₃ + Y = +1/2 + 1/6 = +2/3 | Same charge as up, charm, top |
| Lower component charge | Q = T₃ + Y = −1/2 + 1/6 = −1/3 | Same charge as down, strange, bottom |
| SM analogue | Left-handed quark doublet (u_L, d_L) | Identical quantum numbers |
| Spin | 1/2 | Fermion |
| Baryon number | 1/3 | Same as all quarks |
| Lepton number | 0 | Not a lepton |
| Color | Triplet (participates in strong force) | SU(3) fundamental |
| Weak charge | Doublet (participates in weak force) | SU(2) fundamental |
| Hypercharge | Y = 1/6 (smallest nonzero Y for any color triplet doublet) | U(1) assignment |
| Anomaly status | Anomaly-free by construction | Vector-like: L and R cancel all anomalies |
| Bare mass | Allowed without Higgs mechanism | Vector-like property: mass term ψ̄_L ψ_R + h.c. is gauge invariant |
| Number of new fields | 2 Dirac fermions (4 Weyl fermions) | Upper + lower component, each with L and R |

---

## Table 16.2: Why "Vector-Like" Matters

| Property | Chiral Fermion (SM quarks) | Vector-Like Fermion (Cabibbo Doublet) |
|---|---|---|
| Left-handed rep | (3, 2, 1/6) | (3, 2, 1/6) |
| Right-handed rep | (3, 1, 2/3) or (3, 1, −1/3) separately | (3, 2, 1/6) — SAME as left |
| Mass without Higgs | Forbidden (different reps can't form mass term) | Allowed (same rep, direct mass term) |
| Gauge anomaly | Each generation must cancel (nontrivial) | Automatically zero (L and R cancel) |
| Can be added singly | No (must come in complete anomaly-free sets) | Yes (single multiplet is consistent) |
| Mass scale | Set by Higgs VEV (v = 246 GeV) | Free parameter (bare mass, can be any scale) |

This is why the Cabibbo Doublet can exist as a SINGLE new particle without requiring an entire new generation or a new symmetry framework. Vector-like fermions are the simplest anomaly-free extension of the SM.

---

## Table 16.3: How It Was Identified (PHYS-15 Summary)

| Step | Input | Operation | Output |
|---|---|---|---|
| 1 | SU(3)×SU(2)×U(1) gauge group | Representation theory | b₁ = 41/10, b₂ = −19/6, b₃ = −7 |
| 2 | Beta coefficients | Exact rational arithmetic | SM gap ratio = 218/115 = 1.896 |
| 3 | α_em, sin²θ_W, α_s from DATA-3 | GUT normalization | 1/α₁ = 63.210, 1/α₂ = 31.685, 1/α₃ = 8.475 |
| 4 | Three inverse couplings | Ratio | Measured gap ratio = 1.358 |
| 5 | Steps 2 and 4 | Comparison | 218/115 ≠ 1.358 (40% miss — SM does not unify) |
| 6 | All representations within scope | Dynkin index formulas | 15 sets of (Δb₁, Δb₂, Δb₃) |
| 7 | SM betas + each Δb | Rational arithmetic | 15 modified gap ratios (all exact rationals) |
| 8 | Modified ratios vs 1.358 | Distance criterion (0.15) | 3 survive |
| 9 | M_GUT for survivors | Running equation | 1 eliminated (SU(5) 5+5̄: proton decay) |
| 10 | 2 remaining | Co-survivors stated | MSSM (7/5) and Cabibbo Doublet (38/27) |

Scope: single multiplet, SU(3) dim ≤ 8, SU(2) dim ≤ 4, |Y| ≤ 2, scalar or vector-like fermion. Representations beyond these bounds have larger Dynkin indices producing larger beta shifts that overshoot the correction. The search is conservative.

---

## Table 16.4: The Gap Ratio Computation (Exact Fractions)

| Operation | Expression | Result |
|---|---|---|
| b₁ + Δb₁ | 41/10 + 1/15 | 125/30 = 25/6 |
| b₂ + Δb₂ | −19/6 + 1 | −13/6 |
| b₃ + Δb₃ | −7 + 1/3 | −20/3 |
| Numerator: (b₁+Δb₁) − (b₂+Δb₂) | 25/6 − (−13/6) | 38/6 = 19/3 |
| Denominator: (b₂+Δb₂) − (b₃+Δb₃) | −13/6 − (−20/3) | 27/6 = 9/2 |
| Gap ratio | (19/3) / (9/2) | **38/27 = 1.40741** |
| Distance from measured 1.358 | |1.407 − 1.358| | 0.049 |

Every step is exact rational arithmetic on integers and simple fractions. No floating point enters.

---

## Table 16.5: Beta Function Contributions

| Coefficient | Value | As Fraction | Fraction of SM |b_i| | Physical Role |
|---|---|---|---|---|---|
| Δb₁ | 0.0667 | 1/15 | 1.6% of b₁ | Tiny U(1) screening (Y² = 1/36 is very small) |
| Δb₂ | 1.0000 | 1 | 31.6% of |b₂| | Large SU(2) screening (weak doublet × color triplet) |
| Δb₃ | 0.3333 | 1/3 | 4.8% of |b₃| | Moderate SU(3) screening (color triplet × weak doublet) |
| Δb₂/Δb₁ | 15 | 15 | Highest in all 15 candidates | The key asymmetry that fixes the gap ratio |
| Δb₂/Δb₃ | 3 | 3 | — | SU(2) contribution dominates |
| Δb₁/Δb₃ | 0.2 | 1/5 | — | U(1) nearly negligible vs SU(3) |

The Δb₂/Δb₁ = 15 ratio is the highest of any candidate in the enumeration. This extreme asymmetry comes from Y = 1/6 being the smallest nonzero hypercharge for a color triplet weak doublet. Small Y means small Δb₁ (since Δb₁ ∝ Y²). Large Δb₂ comes from the weak doublet × color triplet combination. The asymmetry is what the gap ratio needs: shrink the numerator (b₁ − b₂) without proportionally growing the denominator (b₂ − b₃).

---

## Table 16.6: Comparison with the MSSM (The Other Survivor)

| Property | Cabibbo Doublet | Full MSSM |
|---|---|---|
| New particles | 1 multiplet (2 Dirac fermions) | ~30 multiplets (~120 fields) |
| (Δb₁, Δb₂, Δb₃) | (1/15, 1, 1/3) | (5/2, 25/6, 4) |
| Gap ratio | 38/27 = 1.407 | 7/5 = 1.400 |
| Gap ratio as rational | Two-digit integers | Single-digit integers |
| Distance from measured 1.358 | 0.049 | 0.042 |
| M_GUT | 10^15.5 GeV | 10^17.3 GeV |
| Δ(1/α₃) at M_GUT | ~0.7 | 0.69 |
| Proton lifetime (minimal SU(5)) | 10^34-35 yr (Hyper-K reach) | 10^36-37 yr (beyond Hyper-K) |
| Dark matter candidate | No | Yes (neutralino) |
| Hierarchy stabilization | No | Yes |
| Theoretical framework required | None | Full supersymmetry |
| LHC status | VL quarks: M > 1.5 TeV | No superpartners found |
| Anomaly cancellation | Automatic (vector-like) | Automatic (SUSY) |
| Residual unification gap | Needs threshold corrections | Needs threshold corrections |

---

## Table 16.7: Mass Constraints from All Sources

| Source | Constraint | Type | Reference |
|---|---|---|---|
| LHC pair production (CMS, Run 2) | M > 1.33 TeV | Lower bound | CMS-B2G VLQ search |
| LHC pair production (ATLAS, Run 2) | M > 1.46 TeV | Lower bound | ATLAS-EXOT VLQ search |
| LHC single production (model-dependent) | M > 1.3-2.0 TeV | Lower bound (depends on mixing) | Various CMS/ATLAS |
| CKM unitarity deficit (Berezhiani 2020) | M ≤ ~6 TeV | Upper bound (mixing must be large enough) | Eur. Phys. J. C 80, 149 |
| CKM unitarity (Branco et al. 2021) | M ≤ ~7 TeV | Upper bound (VL up variant) | JHEP 07, 099 |
| Perturbativity of Yukawa coupling | M ≤ ~10 TeV | Upper bound | Generic |
| Gap ratio analysis (PHYS-15) | Not constrained | Free parameter | This series |
| **Combined window** | **1.5 TeV < M < 6 TeV** | **Narrow: less than half a decade** | **LHC + CKM** |

HL-LHC projected pair production reach: ~2-3 TeV. If M is in the lower half of the window, HL-LHC discovers it directly. If M is in the upper half (3-6 TeV), FCC-hh (100 TeV proposed collider) would be needed for pair production, though single production at HL-LHC could probe higher masses if mixing is large enough.

---

## Table 16.8: The Three Independent Anomalies

| Anomaly | Observable | SM Prediction | Measured | Deviation | How Cabibbo Doublet Fixes It |
|---|---|---|---|---|---|
| CKM unitarity | \|V_ud\|²+\|V_us\|²+\|V_ub\|² | 1.00000 | 0.99798 ± 0.00038 | 2.5-4σ deficit | Expands 3×3 CKM to 4×3; missing \|V_ub'\|² fills the gap |
| A_FB^b at LEP | Forward-backward b asymmetry | ~0.1038 | 0.0992 ± 0.0016 | ~3σ low | VL-b mixing modifies right-handed Z-b-b coupling g_bR |
| Higgs signal strength | Overall production × decay rate | 1.000 | ~1.06-1.10 | ~2σ high | VL quark in gg→H loop; b Yukawa reduction from mixing |

### The Key Papers

| Paper | Authors | Journal | Year | Finding |
|---|---|---|---|---|
| arXiv:1906.02714 | Belfatto, Beradze, Berezhiani | Eur. Phys. J. C 80, 149 | 2020 | First: CKM deficit = VL quark signal. M ≤ 6 TeV |
| arXiv:2001.02853 | Cheung, Keung, Lu, Tseng | JHEP 05, 117 | 2020 | Three-anomaly simultaneous fit with VL doublet |
| arXiv:2302.14097 | Belfatto, Trifinopoulos | Phys. Rev. D 108, 035022 | 2023 | "Remarkable role of the vectorlike quark doublet" |
| arXiv:2407.00122 | Kitahara | Int. J. Mod. Phys. A 39 | 2024 | Status review: "prime candidate is VL quark extension" |
| arXiv:2311.00021 | Cirigliano et al. | JHEP 03, 033 | 2024 | Global SMEFT: ~3σ tension confirmed |

---

## Table 16.9: The Two Roads to the Same Particle

| Property | Gap Ratio Path (HOWL PHYS-15) | Anomaly Path (Literature 2019-2024) |
|---|---|---|
| Starting data | α_em, sin²θ_W, α_s (3 couplings at M_Z) | V_ud, V_us, A_FB^b, μ_Higgs (4 observables across MeV-TeV) |
| Method | Exact rational beta coefficient enumeration | Global χ² anomaly fit |
| What determines the representation | Gap ratio 38/27 = unique minimal survivor | Three-anomaly resolution requires (3,2,1/6) |
| What determines the mass | Not constrained (free parameter) | 1.5-6 TeV (LHC + CKM mixing) |
| What determines the mixing | Not constrained | CKM deficit size: \|V_ub'\| ≈ 0.045 |
| First identified | 2026 (this work) | 2019/2020 (Berezhiani; Cheung et al.) |
| Primary test | Proton decay (Hyper-Kamiokande) | Direct production (LHC), CKM precision (Belle II) |
| Connection to other path | Not known to anomaly groups | Not known to HOWL until web search verification |

The two paths are completely independent. Neither group knew about the other's method. The convergence on the same representation from two different directions — top-down (gauge unification integers) and bottom-up (precision anomaly fitting) — is the strongest evidence for the Cabibbo Doublet prior to direct observation.

---

## Table 16.10: Decay Channels at the LHC

| Decay | Branching Ratio (typical) | Final State | Primary Background | Discovery Signature |
|---|---|---|---|---|
| VL_U → Wb | ~50% | Isolated lepton + b-jet + MET, or dijet + b-jet | tt̄ | High-p_T isolated lepton + forward jet |
| VL_U → Zt | ~25% | Dilepton + top reconstruction, or MET + top | tt̄Z | Same-sign dileptons |
| VL_U → Ht | ~25% | bb̄ pair + top reconstruction | tt̄H | Multi-b + high-p_T top |
| VL_D → Wt | ~50% | Isolated lepton + top + MET, or dijet + top | tt̄ | Boosted top + high-p_T W |
| VL_D → Zb | ~25% | Dilepton + b-jet, or MET + b-jet | Zbb̄ | Z mass peak + high-p_T b |
| VL_D → Hb | ~25% | bb̄ pair + b-jet (triple b) | Multi-b QCD | Three b-tags + high mass |

Production at LHC: primarily gg → VL VL̄ (pair production via strong force, depends only on mass and color charge, not mixing angles). Single production qg → VL q' depends on mixing angle and can probe higher masses if mixing is large.

---

## Table 16.11: Extended CKM Matrix Structure

| Property | SM (3×3) | With Cabibbo Doublet |
|---|---|---|
| Matrix dimension | 3×3 unitary | 4×3 (submatrix of 4×4 unitary) |
| First-row unitarity | \|V_ud\|² + \|V_us\|² + \|V_ub\|² = 1 | + \|V_ub'\|² = 1 |
| Unitarity deficit | 0.00202 ± 0.00038 (anomalous) | Absorbed by \|V_ub'\|² |
| \|V_ub'\| | Does not exist | ≈ 0.045 |
| Mixing angles | 3 (θ₁₂, θ₂₃, θ₁₃) | 3 + 3 new (θ₁₄, θ₂₄, θ₃₄) |
| CP phases | 1 (δ_CKM) | 1 + 2 new (δ₁, δ₂) |
| New parameters total | 0 | 6 (M_VL + 3 angles + 2 phases) |
| Right-handed charged currents | Absent | Present (from VL mixing) |
| Tree-level FCNC | Absent | Present (from extended mixing) |

---

## Table 16.12: Unification Parameters

| Parameter | SM | SM + Cabibbo Doublet | MSSM | Target |
|---|---|---|---|---|
| Gap ratio | 218/115 = 1.896 | 38/27 = 1.407 | 7/5 = 1.400 | 1.358 (measured) |
| Distance from measured | 0.538 (40% miss) | 0.049 (3.6% miss) | 0.042 (3.1% miss) | 0 |
| M_GUT (GeV) | 10^13.8 | 10^15.5 | 10^17.3 | — |
| Δ(1/α₃) at M_GUT | −6.58 | ~−0.7 | −0.69 | 0 |
| Proton lifetime (SU(5)) | 10^30 yr (excluded) | 10^34-35 yr | 10^36-37 yr | >2.4×10^34 (Super-K) |
| Proton decay testable? | Already excluded | **YES (Hyper-K 2027-2037)** | Not in current generation | — |

---

## Table 16.13: The Experimental Test Matrix

| Experiment | Observable | Cabibbo Doublet Prediction | MSSM Prediction | SM Prediction | Timeline |
|---|---|---|---|---|---|
| Hyper-Kamiokande | p → e⁺π⁰ lifetime | τ ~ 10^34-35 yr (DETECTABLE) | τ ~ 10^36-37 yr (below sensitivity) | No prediction | 2027-2037 |
| HL-LHC | VL quark pair production | Discovery if M < 2-3 TeV | Superpartner search | Nothing new | Now-2040 |
| HL-LHC | Single VL production | Higher mass reach if mixing large | — | — | Now-2040 |
| Belle II | V_us, V_ub precision | Modified CKM elements | SM CKM | SM CKM | Now-2030+ |
| DUNE | Proton decay (K⁺ν̄ channel) | Detectable in some GUT completions | Detectable (SUSY SU(5)) | No prediction | 2028+ |
| JUNO | Proton decay (complementary) | Detectable | — | No prediction | 2025+ |
| Neutron experiments | V_ud precision | Modified by VL mixing | SM | SM | Ongoing |
| NA62/KOTO | K → πνν̄ | Sensitive to tree-level FCNC from VL | SM rate | SM rate | Now-2030 |
| STCF (proposed) | V_cd, V_cs (2nd row CKM) | Modified if VL mixes with 2nd gen | SM | SM | Future |
| LHCb upgrades | B_s mixing, b→s transitions | Constrained by VL FCNC | SM + SUSY loops | SM | Now-2030+ |

---

## Table 16.14: The 15 Interaction Paths

| # | Path | What the Cabibbo Doublet Does | Connects To | Computable Now? | Priority |
|---|---|---|---|---|---|
| 1 | R_b and A_FB^b | Modifies Z-b-b vertex via VL-b mixing | PHYS-12 EW computation | Yes | Highest |
| 2 | α_s extraction | Changes Γ_had via vertex corrections, shifting extracted α_s | PHYS-12 overconstrained system | Yes | Highest |
| 3 | M_W via T parameter | Mass splitting of VL components contributes to oblique T | PHYS-12 Δρ infrastructure | Yes | High |
| 4 | Threshold in unified map | New boundary at M_VL where beta coefficients change | PHYS-14 domain structure | Yes | High |
| 5 | θ_QCD mass matrix | Extends quark mass matrix from 6 to 8, new CP phases constrained by nEDM | PHYS-7 energy minimization | Yes | High |
| 6 | VP running above M_VL | VL components screen electromagnetic charge above their mass | PHYS-5 α running | Yes (tiny: ~10⁻¹³ on a_e) | Medium |
| 7 | 4-mass Koide (down sector) | Fourth down-type mass breaks 3-mass tautology, new symmetry structure | PHYS-8 Koide decomposition | Yes (when M measured) | Medium |
| 8 | Vacuum stability | VL Yukawa coupling modifies Higgs quartic λ running | New computation | Yes (depends on y_VL) | Medium |
| 9 | GUT completion | Which GUT group (SU(5), SO(10)) contains (3,2,1/6) | PHYS-15 gap ratio framework | Model-dependent | Medium |
| 10 | B meson FCNC | Tree-level flavor-changing Z couplings from extended mixing | DATA-3 B-meson entries | Constrained by data | Medium |
| 11 | LHC search strategy | Pair and single production cross sections, decay signatures | External computation | Computable | Medium |
| 12 | Baryogenesis | Two new CP phases provide additional CP violation for matter-antimatter asymmetry | New computation | Model-dependent | Low |
| 13 | Neutron lifetime | V_ud modification connects to beam/bottle discrepancy (~2.3σ) | DATA-3 neutron data | Indirect | Low |
| 14 | Confinement wall | Modified α_s running above M_VL shifts Λ_QCD by ~1% | PHYS-6 confinement characterization | Small effect | Low |
| 15 | Muon g-2 | VP contribution from VL quark loop | PHYS-9 QED series | Tiny: ~10⁻¹³ | Low |

---

## Table 16.15: Level 1 / Level 2 Assignment

| Property | Level | Evidence | Paper |
|---|---|---|---|
| Representation (3,2,1/6) | **Level 1** | Forced by gap ratio arithmetic from gauge group integers | PHYS-15 |
| Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3 | **Level 1** | Determined by Dynkin index formulas from representation | PHYS-15 |
| Gap ratio 38/27 | **Level 1** | Exact rational from beta coefficient arithmetic | PHYS-15 |
| Δb₂/Δb₁ = 15 asymmetry | **Level 1** | From Y = 1/6 being smallest hypercharge for (3,2,Y) | PHYS-18 |
| M_GUT = 10^15.5 GeV | **Derived** (from Level 1 + Level 2 inputs) | Running equation with DATA-3 couplings | PHYS-15 |
| Mass M_VL | **Level 2** | Free parameter, 1.5-6 TeV from experiments | This paper |
| Mixing angles θ₁₄, θ₂₄, θ₃₄ | **Level 2** | From anomaly fits, not determined by gap ratio | PHYS-19 |
| CP phases δ₁, δ₂ | **Level 2** | From CP violation data | PHYS-19 |
| Existence | **Level 2** | Conditional on unification being a feature of nature | — |

The quantum numbers are Level 1 — determined by the framework. The mass and mixing parameters are Level 2 — supplied by the universe. This is the same pattern as every SM particle: the integers say WHAT exists, the measurements say HOW MUCH.

---

## Table 16.16: Parameter Count Change

| Scenario | Parameters | Anomalies Unresolved | Gap Ratio Miss |
|---|---|---|---|
| SM (after θ_QCD, Koide conditional) | 17 | 3 (CKM 2.5-4σ, A_FB^b 3σ, Higgs 2σ) | 40% |
| SM + Cabibbo Doublet | 17 + 6 = 23 | 0 | 3.6% |
| MSSM | 17 + 105+ | 0 | 3.1% |

The Cabibbo Doublet trades 6 parameters for: resolution of 3 independent multi-sigma anomalies, reduction of the gap ratio miss from 40% to 3.6%, a testable proton decay prediction, and approximate gauge coupling unification. The MSSM achieves similar unification quality but requires 100+ new parameters.

---

## Table 16.17: What PHYS-16 Must Contain for Self-Containment

| Topic | What Must Be Explained From Scratch | Why |
|---|---|---|
| The three gauge couplings | What α₁, α₂, α₃ are and how they're measured | Reader may not know GUT normalization |
| The gap ratio | What it tests and why 218/115 ≠ 1.358 matters | Reader may not know the unification test |
| Beta functions | What they are and why they're exact rationals | Core of the identification method |
| Vector-like fermions | What "vector-like" means and why it's anomaly-free | Reader may not know the distinction from chiral |
| The CKM matrix | What unitarity means and why a deficit is anomalous | Reader may not know flavor physics |
| Proton decay | What it tests and why M_GUT determines the lifetime | Reader may not know GUT phenomenology |
| The Higgs coupling | How VL quarks modify gg→H and bottom Yukawa | Reader may not know loop-level Higgs physics |

Every one of these must be explained in the paper, not referenced to another paper. A reader who has never taken a particle physics course should be able to follow the argument by reading PHYS-16 alone.

---

## Table 16.18: Scripts and Data Required

| Item | Content | Role |
|---|---|---|
| GUT running script + output | Coupling extraction, running, BSM enumeration, 15 candidates | Ground truth for all gap ratio numbers |
| GUT parked notebook | 9 results, 9/9 checks, clean summary | Verified summary |
| Bug diagnosis document | sin²θ_W circularity explanation | Explains why gap ratio formulation was adopted |
| DATA-3 paper | 123 entries, 32/32 consistency checks | Source of truth for all measured values |
| Anomaly web search results | Belfatto, Cheung, Kitahara, Cirigliano papers | Source of truth for anomaly data |
| Cabibbo Doublet database record | Complete internal record from this session | Raw material for the paper |
| PHYS-15 as written | The identification paper | Referenced but not leaned on |

---

*These 18 tables provide the complete specification of the Cabibbo Doublet for PHYS-16. Every number traces to a verified script (9/9 checks), a DATA-3 entry (32/32 checks), or a published reference (verified by web search). The paper is the "today I learn" document for anyone encountering this particle for the first time.*
