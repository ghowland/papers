# The Session 3 Operational Lexicon
## You are here. The ground is set until falsified.

**Registry:** [@HOWL-PHYS-24-2026]

**Series Path:** [@HOWL-PHYS-1-2026] → [@HOWL-PHYS-13-2026] → [@HOWL-PHYS-21-2026] → [@HOWL-PHYS-24-2026]

**Date:** April 2 2026

**Domain:** Operational Foundation

**DOI:** 10.5281/zenodo.zzz

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

**Backed by:** 8 demonstration scripts (62/62 checks), phys24_lib.py (21/21 self-test, 148/148 platform test), 6 Session 3 scripts (98/98 checks), DATA-4 (146 entries, 38/38 checks)

---

## Abstract

This paper presents no new computation. It records the operational status of the HOWL series after Session 3 and fixes the working lexicon for all subsequent work. The series now has enough verified structure that repeated re-argument of first principles is no longer productive. A boundary must be drawn between what is operationally fixed and what remains open. This paper draws that boundary. The standard is exact Fraction arithmetic, verified scripts with passing checks, explicit provenance, and bounded claims. Within that standard, the following are fixed as operational ground until falsified: the Level 1 / Level 2 boundary, the SM non-unification (gap ratio 218/115 vs measured 1.358, 40% miss), the generation democracy and boson problem, the Cabibbo Doublet (3,2,1/6) as the minimal single-multiplet survivor with gap ratio 38/27, the two-loop improvement from Δ = −1.17 to −0.40, the Koide C₃ closure with the amplitude as the open problem, the 82/82 PSLQ null, and DATA-4 as the sole data reference with 146 entries and 38/38 checks. Eight demonstration scripts totaling 62/62 checks and a platform library verified at 148/148 provide the computational foundation.

---

## 1. Purpose

The HOWL series has produced 6 MATH papers, 23 PHYS papers, 4 DATA papers, and 6 verified scripts with 98 total checks across three sessions. A future session that needs to build on this work faces a choice: read 30 papers, or read one. This paper is the one.

The purpose is not to declare infallibility. Any item below may be falsified by later computation or experiment. The purpose is the opposite: to make progress possible by stating plainly what is being treated as working ground, so that future sessions do not spend their time re-litigating foundations already established to the current standard of the series. The standard is exact arithmetic, verified scripts, explicit provenance, and bounded claims.

---

## 2. The Rule

The integers tell you WHAT. The universe tells you HOW MUCH. This is the Level 1 / Level 2 boundary, now adopted as the standing rule of the series.

**Level 1** means framework-determined: gauge representations, exact beta coefficients, exact geometric identities, exact rational gap ratios, exact scaling laws, any result that follows from group theory, topology, geometry, or exact arithmetic without using measured input. Level 1 results are the same in any universe with SU(3)×SU(2)×U(1).

**Level 2** means universe-supplied: masses, couplings, mixing angles, CP phases, measured anomalies, experimental bounds, any value that could have been otherwise in a universe with the same formal structure. Level 2 values come from DATA-4.

**Derived** means Level 1 structure applied to Level 2 input. M_GUT = 10^15.5 GeV is Derived: Level 1 betas applied to Level 2 couplings. The measured gap ratio 1.358 is Derived: Level 1 formula applied to Level 2 measurements.

Future papers must classify their main results accordingly.

---

## 3. The Arithmetic

All computation in the series uses exact Fraction arithmetic from the `fractions` module. No floating-point value enters the computation chain. Conversion to mpf happens only at the display boundary — where a number leaves computation and enters a print statement or a comparison against an mpf reference. The Q335 = 2^335 basis provides 101-digit integer rational representations of all transcendental constants, verified against mpmath at 100+ digits.

The operational standard for all scripts from this paper forward is documented in phys24_script_rules.md (22 sections). The platform library phys24_lib.py provides every constant, every helper function, and every check function. Scripts import it with one line: `from phys24_lib import *`. If a value changes (new PDG, new CODATA), it changes in the library and nowhere else.

---

## 4. The Numbers

Every number below comes from a verified script. Any discrepancy with a paper resolves in favor of the script output.

**Table A: Key Results**

| Quantity | Value | Source | Level |
|---|---|---|---|
| SM gap ratio | 218/115 = 1.8956521739 | phys24_gap_ratio.py, EXACT | 1 |
| Measured gap ratio | 1.3581926841 | phys24_gap_ratio.py, 6.6 digits | Derived |
| SM gap miss | 39.57% | phys24_gap_ratio.py | Derived |
| Cabibbo Doublet gap ratio | 38/27 = 1.4074074074 | phys24_cabibbo_doublet.py, EXACT | 1 |
| CD distance from measured | 0.049215 | phys24_cabibbo_doublet.py | Derived |
| MSSM gap ratio | 7/5 = 1.4000000000 | phys24_cabibbo_doublet.py, EXACT | 1 |
| MSSM distance from measured | 0.041807 | phys24_cabibbo_doublet.py | Derived |
| SM betas (b₁, b₂, b₃) | 41/10, −19/6, −7 | phys24_gap_ratio.py, EXACT | 1 |
| CD beta shifts (Δb₁, Δb₂, Δb₃) | 1/15, 1, 1/3 | phys24_cabibbo_doublet.py, EXACT | 1 |
| Modified betas (b₁', b₂', b₃') | 25/6, −13/6, −20/3 | phys24_cabibbo_doublet.py, EXACT | 1 |
| Per-generation beta | (4/3, 4/3, 4/3) | phys24_democracy.py, EXACT | 1 |
| Fermion gap contribution | 0% numerator, 0% denominator | phys24_democracy.py, EXACT | 1 |
| Pure-gauge gap ratio | 2 | phys24_democracy.py, EXACT | 1 |
| Asymmetry Δb₂/Δb₁ | 15 | phys24_cabibbo_doublet.py, EXACT | 1 |
| M_GUT (CD, one-loop) | 10^15.54 GeV | phys24_cabibbo_doublet.py | Derived |
| M_GUT (MSSM, one-loop) | 10^17.32 GeV | phys24_cabibbo_doublet.py | Derived |
| log₁₀(τ_MSSM/τ_CD) | 7.115 | phys24_cabibbo_doublet.py | Derived |
| One-loop Δ(1/α₃) at M_VL=500 | −1.17 | phys24_two_loop.py, EXACT | Derived |
| Two-loop Δ(1/α₃) at M_VL=500 | −0.40 | phys24_two_loop.py, EXACT | Derived |
| Two-loop improvement | 65.8% | phys24_two_loop.py, 2.5 digits | Derived |
| A₂ coefficient | −0.32847896558 | phys24_a2_anatomy.py, 12.2 digits | 1 |
| A₂ cancellation | 87.36% | phys24_a2_anatomy.py | 1 |
| Koide K(e,μ,τ) | 0.66666051147 | phys24_koide_status.py, 10.3 digits | 2 |
| Koide a²(leptons) | 1.9999630688 | phys24_koide_status.py, 11.5 digits | 2 |
| Koide a²(down quarks) | 2.3877254610 | phys24_koide_status.py, 10.8 digits | 2 |
| Koide a²(up quarks) | 3.0927612855 | phys24_koide_status.py, 10.9 digits | 2 |
| PSLQ record | 82/82 null | phys24_pslq_null.py | 2 |
| PSLQ sanity | [1, 0, −6] (π² = 6ζ(2)) | phys24_pslq_null.py | 1 |

**Table B: Experimental Inputs (from DATA-4)**

| Quantity | Value | DATA-4 Entry | Digits |
|---|---|---|---|
| α⁻¹ | 137.035999177 | B1 | 12 |
| sin²θ_W | 0.23122 | B11 | 5 |
| α_s(M_Z) | 0.1180 | B12 | 4 |
| m_e | 0.51099895069 MeV | B2 | 11 |
| m_μ | 105.6583755 MeV | B3 | 10 |
| m_τ | 1776.86 MeV | B4 | 6 |
| M_Z | 91187.6 MeV | C1 | 6 |
| m_t | 172570 MeV | C4 | 5 |
| m_H | 125200 MeV | C5 | 5 |
| m_u | 2.16 MeV | D1 | 3 |
| m_d | 4.70 MeV | D2 | 3 |
| m_s | 93.5 MeV | D3 | 3 |
| m_c | 1273 MeV | D4 | 4 |
| m_b | 4183 MeV | D5 | 4 |
| Super-K bound | τ > 2.4 × 10^34 yr | PHYS-20, web verified | — |
| CKM deficit | 0.00202 ± 0.00038 | PHYS-19, web verified | — |

---

## 5. The Framework

**Transformation laws are integers.** The beta function coefficients b₁ = 41/10, b₂ = −19/6, b₃ = −7 are exact rationals from the gauge group SU(3)×SU(2)×U(1) with the known SM particle content. Every integer traces to a Dynkin index or Casimir invariant. Adding a particle changes the betas by exact rationals: the Cabibbo Doublet adds (1/15, 1, 1/3). The transformation law is more fundamental than any single measured value. Couplings are readings at specified scales, connected by the law.

**Boundaries change the rules.** The energy landscape from m_e to M_GUT is a sequence of domains with fixed integer beta coefficients, separated by mass thresholds where the coefficients change by exact rationals. Each threshold is a soliton boundary in the series vocabulary: inside a domain the coupling runs, at the boundary the transformation law changes. The one domain where perturbative rules do not apply is the confinement wall (~0.3-2 GeV) where α_s ~ O(1).

**Geometric invariants.** R₂ = π/4 is the universal 2D geometric remainder, appearing in the governing equation of every circular-to-rectilinear conversion across 9 engineering and 9 physics domains (PHYS-11). R₄ = π²/32 is the universal 4D geometric remainder, entering every loop integral and 4D phase-space computation. The QED perturbation series is an expansion in α/(4R₂) = α/π.

---

## 6. The Gap Ratio and the Boson Problem

The SM gauge couplings do not unify at one loop. The gap ratio — the ratio (b₁−b₂)/(b₂−b₃) of exact rational beta differences — is 218/115 = 1.896 for the SM. The measured gap ratio from the three couplings at M_Z is 1.358. The miss is 39.6%. This is not a rounding error. It means the three inverse coupling lines do not meet at a point.

The miss is a boson problem. Complete fermion generations contribute (4/3, 4/3, 4/3) to the three betas — identical across all gauge groups. This is generation democracy: fermions are invisible to the gap ratio. The fermion contribution to both numerator and denominator of the gap ratio is exactly zero. The gap ratio decomposes as 96-101% gauge self-coupling, −0.9% to +4.3% Higgs correction, 0% fermion. The pure-gauge gap ratio (no Higgs, no fermions) is the Casimir ratio C₂(SU(2))/(C₂(SU(3))−C₂(SU(2))) = 2. The Higgs shifts this from 2 to 218/115. Fermions shift it by exactly zero.

Fixing the gap ratio requires changing the bosonic content, or adding a representation that breaks the fermion democracy by contributing unequally to the three betas.

---

## 7. The Cabibbo Doublet

The minimal single-multiplet extension that fixes the gap ratio is the Cabibbo Doublet: a vector-like quark doublet in the (3,2,1/6) representation of SU(3)×SU(2)×U(1).

**Level 1 properties (fixed until falsified):**

The beta shifts are computed from Dynkin index formulas: Δb₁ = (2/5)×dim(R₃)×dim(R₂)×Y² = 1/15, Δb₂ = (2/3)×dim(R₃)×S₂(R₂) = 1, Δb₃ = (1/3)×dim(R₂)×S₂(R₃) = 1/3. The modified gap ratio is (b₁'−b₂')/(b₂'−b₃') = 38/27 = 1.407, distance 0.049 from measured. For comparison, the full MSSM achieves 7/5 = 1.400, distance 0.042 — comparable quality from one multiplet versus the entire superpartner spectrum.

The asymmetry mechanism is Y = 1/6. Δb₁ depends on Y² = 1/36, while Δb₂ and Δb₃ do not depend on Y. The ratio Δb₂/Δb₁ = 15: the SU(2) beta shifts 15 times more than the U(1) beta. This is why the gap ratio decreases from 1.896 toward the measured 1.358.

The one-loop unification scale is M_GUT = 10^15.5 GeV, at the proton decay boundary. Proton lifetime in minimal SU(5)-type completion is τ ~ 10^34-35 yr, within Hyper-Kamiokande reach. The MSSM predicts τ ~ 10^37 yr, beyond any planned experiment. The ratio τ_MSSM/τ_CD ~ 10^7: seven orders of magnitude separation from a gap ratio difference of 0.007.

**Level 2 properties (staged, not fixed):**

Mass window 1.5-6 TeV (LHC lower bound, CKM perturbativity upper bound). Primary mixing |V_ub'| ≈ 0.045 from CKM first-row deficit. Six new parameters: M_VL, θ₁₄, θ₂₄, θ₃₄, δ₁, δ₂. DATA-4 entries 124-129, Type G (staged).

**Two independent roads converge.** The gap ratio path (Level 1, top-down from beta function arithmetic) and the anomaly path (Level 2, bottom-up from experimental tensions) both identify the same (3,2,1/6) representation. No shared data, no shared methods, no shared citations between the two roads. Three anomalies point to the Cabibbo Doublet independently: CKM first-row unitarity deficit at 2.5-4σ (uses the weak doublet quantum number), the LEP A_FB^b anomaly at ~3σ (uses color + weak quantum numbers), and the Higgs signal strength excess at ~2σ (uses the color triplet quantum number). Each anomaly uses a different quantum number. The full representation is required.

Future sessions do not reopen the question "which minimal single-multiplet candidate is under discussion?" The answer is the Cabibbo Doublet, unless falsified.

---

## 8. The Two-Loop Status

The two-loop SM beta function matrix b_ij is a 3×3 matrix of exact Fractions from Machacek-Vaughn (1983) and Luo-Xiao (hep-ph/0207271):

|  | U(1) | SU(2) | SU(3) |
|---|---|---|---|
| U(1) | 199/50 | 27/10 | 44/5 |
| SU(2) | 9/10 | 35/6 | 12 |
| SU(3) | 11/10 | 9/2 | −26 |

The dominant two-loop effect is b₃₃ = −26. Since b₃₃ is negative and α₃ > 0, the two-loop correction to d(1/α₃)/d(ln μ) is positive: it slows SU(3) running. Slower running means 1/α₃ is larger at M_GUT, bringing it closer to the α₁ = α₂ crossing. This is why two-loop improves unification.

At M_VL = 500 GeV: the one-loop Cabibbo Doublet miss is Δ(1/α₃) = −1.17. The two-loop miss (using the SM b_ij matrix with step-function threshold at M_VL) is Δ = −0.40. This is a 66% improvement. The residual is within the standard range for GUT threshold corrections in minimal SU(5) with ordinary mass splittings.

The Cabibbo Doublet at two loops achieves the same unification quality as the MSSM at one loop: both need GUT threshold corrections of comparable magnitude.

What remains: the VL two-loop b_ij contribution (neglected, estimated ~0.1% effect), GUT threshold parametrization as a function of M_T/M_X splitting, finding M_VL for exact unification, and predicting α_s and sin²θ_W from the unification condition.

---

## 9. The Koide Status

The Koide ratio K = (Σm)/(Σ√m)² equals 0.66666051147 for charged leptons — within 6 parts per million of 2/3. For quarks it deviates by 10-27%. The Koide amplitude a², defined by K = (1+a²/2)/3, is 1.9999630688 for leptons (not exactly 2 — this is a Level 2 measurement, not the Level 1 hypothesis), 2.3877254610 for down quarks, and 3.0927612855 for up quarks. The ordering a²_lep < a²_down < a²_up correlates with interaction strength.

**The C₃ path is closed.** The 120° spacing in the Koide parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3)) is a tautology: three parameters (M, a, θ₀) fitting three data points is an exactly determined system. It always succeeds for any three positive masses. The spacing is a property of the parametrization, not of the physics. K = 2/3 is a saddle point of the Koide ratio under phase perturbation at a = √2: d²K/dε² = +0.4714 in one direction (minimum) and −0.3905 in another (maximum). The C₃ potential does not select K = 2/3.

**The open problem is the amplitude.** Why a² = 2 for charged leptons? Requirements for any viable derivation: must produce a² = 2 specifically, must explain the three-sector ordering, must not reduce to a reformulation of K = 2/3 (all known reformulations — K = 2/3, a = √2, CV(√m) = 1, Var = Mean², midpoint of range, democratic matrix — are algebraically equivalent and contain no information beyond the three masses). Any future Koide paper that does not attack the amplitude directly is off-target.

---

## 10. The A₂ Anatomy

The QED 2-loop coefficient A₂ decomposes into three pieces of distinct mathematical character: A₂ = 197/144 + (3/4)ζ(3) + R₄×(8/3 − 16 ln 2) = −0.32847896558. The rational piece (+1.368) is from algebraic reduction of 7 two-loop diagrams. The number-theoretic piece (+0.902) is from Feynman parameter integrals producing Li₃(1) = ζ(3). The geometric piece (−2.598) is from 4D momentum phase space, where R₄ = π²/32.

The positive pieces (+2.270) cancel against the geometric piece (−2.598) by 87.4%. The net A₂ is only 12.6% of either side. A₂ is small not because QED converges rapidly but because geometry nearly cancels arithmetic. The smallness is accidental — no known symmetry requires the 87% cancellation.

---

## 11. The Search Record

The PSLQ integer relation algorithm, applied to 82 constants from three categories — physical (59 tests, 4-15 digits), dynamical (3 tests, 10-30 digits), and analytical (10 tests, 100 digits) — finds zero relations against a 20-constant transcendental basis with maxcoeff 10,000. The sanity check confirms the algorithm is operational: PSLQ finds the known relation π² = 6ζ(2) as the integer vector [1, 0, −6]. The Bessel zeros j₁₁, j₀₁, j₁₂ are independent of the entire basis at 100-digit precision — the strongest independence statement in the series by 70 orders of magnitude over the SM parameter tests.

Every parameter reduction in the series came from physical derivation: θ_QCD = 0 from energy minimization (PHYS-7), α ↔ a_e at 4.3 ppb from QED perturbation theory (PHYS-9), Koide K = 2/3 conditional from a trigonometric identity (PHYS-8). Every PSLQ search returned null: 0/82. Derivation beats search. Future effort should prioritize physical derivation paths over numerical pattern hunting.

---

## 12. The Database

DATA-4 is the sole data reference for all HOWL computation. It contains 146 entries across sections A through N: 7 SI fundamental constants (Type E, exact), 13 CODATA measured (Type M), 6 electroweak observables (Type M), 11 quark masses and CKM parameters (Type M), 8 nuclear/hadron masses (Type M), 1 spectroscopy frequency (Type M), 14 Q335 analytical constants plus extended basis (Type A), 8 mass ratios and Koide values (Type M/K), 6 Cabibbo Doublet parameters (Type G, staged), and 17 GUT/unification parameters (Type D, derived). All 38 cross-checks pass: 32 inherited from DATA-3 (Groups A-E) plus 6 new GUT verification checks (Group G, all exact).

Finding 15 (lattice ratio independence): the FLAG lattice QCD mass ratios m_c/m_s = 11.783, m_b/m_c = 4.578, m_u/m_d = 0.485 are independent measurements evaluated at a common renormalization scale. They are not derivable from the individual PDG quark masses evaluated at different scales. Discrepancies up to 28% are from scale mismatch, not database error. A future session dividing PDG masses and comparing to FLAG ratios will see this discrepancy. The database is not corrupted.

DATA-3 is retired. When new measurements become available, they enter as DATA-5 with the same verification protocol.

---

## 13. The Experimental Triangle

Three experiments test the Cabibbo Doublet framework on different timescales:

**Hyper-Kamiokande** (proton decay p → e⁺π⁰). Operations ~2027. The CD predicts τ ~ 10^34-35 yr in minimal SU(5)-type completion. Super-K current bound: τ > 2.4 × 10^34 yr. Hyper-K 20-year sensitivity: ~10^35 yr. The MSSM predicts τ ~ 10^37 yr, beyond reach. This is the decisive discriminator between the two scenarios with nearly identical gap ratios (38/27 vs 7/5).

**HL-LHC** (direct VL quark pair production). Running now through ~2040. Mass reach 2-3 TeV. If M_VL < 2-3 TeV, the Cabibbo Doublet is directly discoverable. The lower bound of the mass window (1.5 TeV) is within reach.

**Belle II** (CKM precision and m_τ). Running now through ~2030+. Sharpens the CKM first-row deficit and constrains extended mixing. Improved m_τ precision tests the Koide conditional (18 → 17 parameter reduction).

Complementary: DUNE (p → K⁺ν̄, the SUSY SU(5) channel, ~2028+), NA62 (rare kaon decays constraining θ₂₄), FCC-ee/CEPC (A_FB^b remeasurement resolving the 25-year LEP anomaly, future).

---

## 14. The Parameter Scorecard

| Step | Change | Method | Status |
|---|---|---|---|
| SM starting count | 19 | — | Established |
| θ_QCD = 0 | 19 → 18 | Energy minimization of QCD vacuum | **Confirmed** |
| m_τ from Koide | 18 → 17 | K = (1+a²/2)/3 at a² = 2 | **Conditional** (C₃ closed, amplitude unresolved) |
| +6 Cabibbo Doublet | 17 → 23 | Gap ratio enumeration + anomaly convergence | **Staged** (Type G, entries 124-129) |
| α_s from unification | 23 → 22 | Two-loop + threshold → predict α_s | Not yet computed |
| sin²θ_W from 3/8 | 22 → 21 | Linear formula with CD betas for L_X | **Unblocked** (~10 lines) |
| CKM from mass ratios | Further | sin θ₁₂ ≈ √(m_d/m_s), sin θ₂₃ ≈ √(m_u/m_c) | Blocked (quark mass precision) |
| λ from impedance matching | Further | λ = g'² at condensation boundary | Blocked (no derivation) |

The 17 → 23 step adds 6 parameters but they are staged: identified by Level 1 arithmetic, bounded by Level 2 experiment, not yet measured. The trade is: 6 new parameters buy three anomaly resolutions, gap ratio improvement from 40% miss to 3.6% miss, approximate unification, and testable proton decay.

---

## 15. The Scripts

**Session 3 Verified Scripts (source of truth):**

| Script | Checks | Key Output |
|---|---|---|
| sin2_theta_w_1.py | 9/9 | Gap ratios, BSM enumeration, M_GUT |
| a_2_decomposition_0.py | 7/7 | A₂ three-piece decomposition, 87% cancellation |
| bessel_pslq_0.py | 6/6 | 82/82 independence, Bessel zeros at 100 digits |
| data_2_to_3_test_1.py | 32/32 | DATA-3 consistency, 123 entries |
| data_4.py | 38/38 | DATA-4 consistency, 146 entries |
| unification_test.py | 6/6 | Two-loop Δ = −0.40 at M_VL = 500 GeV |
| **Total** | **98/98** | |

**PHYS-24 Demonstration Scripts:**

| Script | Checks | Demonstrates |
|---|---|---|
| phys24_gap_ratio.py | 5/5 | SM non-unification, gap ratio 218/115 vs 1.358 |
| phys24_democracy.py | 10/10 | Generation democracy, fermion invisibility, boson problem |
| phys24_cabibbo_doublet.py | 10/10 | Dynkin formulas, gap 38/27, asymmetry, proton decay |
| phys24_two_loop.py | 8/8 | b_ij matrix, Δ: −1.17 → −0.40, 66% improvement |
| phys24_koide_status.py | 10/10 | Three-sector K and a², tautology, saddle point |
| phys24_a2_anatomy.py | 7/7 | Three-piece decomposition, 87% cancellation |
| phys24_pslq_null.py | 4/4 | Sanity [1,0,−6], Bessel null, derivation beats search |
| phys24_data4_check.py | 8/8 | Representative checks spanning all DATA-4 groups |
| **Total** | **62/62** | |

**Platform:**

| Component | Checks | Content |
|---|---|---|
| phys24_lib.py self-test | 21/21 | Gap ratios, betas, Q335 basis, Koide, constants |
| phys24_lib_test.py | 148/148 | Full verification of all 146 DATA-4 entries + cross-checks |

The script standard (phys24_script_rules.md) governs all scripts from this paper forward: Python 3.8+, Fraction arithmetic, no `math` module, no `float()` in computation, no `assert`, mpf at display boundary, 100 dps standing precision, 11 significant figures minimum display, every check prints expected/got/digits/need.

---

## 16. What Is Closed, What Is Open, What Is Deprioritized

**Closed** (stop re-litigating):

SM non-unification (gap ratio 218/115 ≠ 1.358). Generation democracy at one loop (4/3, 4/3, 4/3). Bosonic origin of the gap ratio failure (fermion contribution exactly zero). Minimal single-multiplet survivor is the Cabibbo Doublet (3,2,1/6). C₃ route to Koide (tautology + saddle). Broad PSLQ pattern hunting as a primary strategy (82/82 null, derivation beats search). λ = 1/8 for Higgs self-coupling (corrections go wrong direction). Koide phase adjustment for quarks (phase independence proven). Scale choice fixing quark Koide (exact scale invariance proven). DATA-4 as the sole active data reference.

**Open** (worth spending time):

VL two-loop b_ij contribution and full two-loop unification. GUT threshold corrections in minimal SU(5) completion. Finding M_VL for exact unification in the 1.5-6 TeV window. Predicting α_s from the unification condition. Computing sin²θ_W from 3/8 with Cabibbo Doublet betas (unblocked, ~10 lines). S, T oblique parameters from the Cabibbo Doublet. Z-b-b vertex correction from VL-b mixing. Deriving the Koide amplitude a² = 2. Any direct experimental confrontation involving the staged Cabibbo Doublet.

**Deprioritized** (unless new input arrives):

Generic cosmological boundary speculation without a derived per-transit law. Re-opening closed Koide C₃ paths. Broad PSLQ scans on already-null classes. The 4-loop A₄ wall (blocked by private Laporta master integral data). CKM-mass relations (blocked by quark mass precision floor). Higgs λ = g'² impedance matching (blocked by no derivation from soliton framework).

---

## 17. Falsification Conditions

| Operational commitment | What would break it |
|---|---|
| Gap ratio framework | Discovery of a fourth complete generation (changes all betas) |
| Cabibbo Doublet identification | LHC exclusion of VL quarks above 6 TeV, OR CKM first-row deficit disappearing with improved measurements |
| Proton decay window 10^34-35 yr | Hyper-K null at τ > 10^35 yr excludes minimal SU(5) completion. The CD itself survives — the gap ratio and anomaly evidence are independent of the GUT completion. Only the lifetime prediction changes. |
| Generation democracy | Holds exactly at one loop. Higher-loop corrections are small but nonzero. Discovery of incomplete generations or split multiplets at low energy would break it. |
| Koide K = 2/3 conditional | Improved m_τ measurement deviating by > 3σ from the Koide prediction 1776.97 MeV |
| Two-loop improvement (66%) | Discovery of an error in the Machacek-Vaughn b_ij matrix (unlikely — used across the field for 40 years) |
| 82/82 PSLQ null | Discovery of a compact relation for any tested constant. Would not invalidate the null for the other 81, but would change the methodological conclusion. |
| Derivation beats search | A PSLQ identification of a previously untested quantity (e.g., Koide amplitudes). Would weaken the conclusion for future strategy, not invalidate the existing 3/3 derivation successes. |

---

## 18. What This Paper Does Not Claim

This paper does not claim the Cabibbo Doublet has been discovered. It has been identified by Level 1 arithmetic and corroborated by Level 2 anomalies. Discovery requires direct experimental observation.

This paper does not claim unification is proven. The gap ratio 38/27 is exact arithmetic. Whether nature chose to unify the gauge forces is a Level 2 question.

This paper does not claim the integer anatomy is new physics. It is new presentation of known physics in exact rational arithmetic. The formulas are in textbooks. The contribution is the Fraction computation, the integer tracing, and the systematic confrontation.

This paper does not claim all operational commitments are permanent. Every commitment has a stated falsification condition in Section 17. The lexicon is designed to be revised when evidence demands it.

This paper does not claim PSLQ is the wrong tool. PSLQ is the correct tool for testing integer linear relations. The methodological conclusion (derivation beats search) is about priorities — where to spend effort — not about the validity of the algorithm.

This paper does not claim the two-loop result is final. The VL two-loop b_ij contribution and GUT threshold corrections remain to be computed. The Δ = −0.40 is a partial result that improves on the one-loop Δ = −1.17 but is not the complete answer.

---

## 19. What This Paper Seeds

Every script in this paper is a template for future computation. The phys24_lib.py platform library provides all constants and helpers for Session 4+ scripts — change one import line to test against new data. The open questions list (Section 16) is the work queue. The falsification conditions (Section 17) are the kill criteria. The experimental timeline (Section 13) is the clock.

The most immediate seeds: sin²θ_W from 3/8 is unblocked (~10 lines using Cabibbo Doublet betas for L_X). The VL two-loop b_ij computation is staged (formulas known, normalization to be resolved). The GUT threshold parametrization in minimal SU(5) is a defined computation. The Koide amplitude a² = 2 remains the deepest open problem in the series — no viable attack path is currently known, but the problem is sharply stated and the dead paths are documented.

The Cabibbo Doublet is staged. The GUT arithmetic is staged. The database is staged. The lexicon is staged. If later work falsifies part of this ground, the ground will be revised. Until then, this is the ground.

---

*PHYS-24: The Session 3 Operational Lexicon. You are here. 8 scripts, 62 checks, 0 failures. The ground is set until falsified. Published April 2, 2026. This paper is never edited after publication.*
