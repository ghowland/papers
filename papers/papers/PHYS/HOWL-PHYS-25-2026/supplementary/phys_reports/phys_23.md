
# PHYS-23 Report: The Koide C₃ Closure

**Registry:** @HOWL-PHYS-23-2026
**Position in series:** Twenty-third and final pre-manuscript physics paper. Closes the C₃ path to the Koide formula and states the real open problem.
**Preceded by:** PHYS-22 (A₂ geometric cancellation)
**Followed by:** PHYS-24 (the manuscript — integrates everything)
**Backed by:** DATA-3 (32/32), PHYS-8 (Koide parametrization), inline computation
**Code status:** No dedicated script. All values computed inline from DATA-3 lepton and quark masses.

---

## What It Establishes

**The C₃ path to the Koide formula is doubly dead.**

Argument 1 (Tautology): The 120° spacing in the Koide parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3)) is automatic. Three parameters (M, a, θ₀) fitting three data points (m_e, m_μ, m_τ) is an exactly determined system. ANY three positive masses have this form. The C₃ symmetry "explains" something that requires no explanation.

Argument 2 (Saddle point): Even granting the spacing, K = 2/3 is a saddle point — not a minimum — of the Koide ratio on the C₃ phase landscape. Perturbing the phases in the "stretch" direction increases K; in the "compress" direction decreases K. The C₃ potential does not select a² = 2 as preferred.

Either argument alone kills the path. Together they are definitive.

**The real problem is the amplitude: derive a² = 2 from physics.** Every known reformulation (K = 2/3, a = √2, CV(√m) = 1, Var = Mean², midpoint of range, democratic matrix) is algebraically equivalent. None is a derivation. The test: does it contain input beyond the three masses? If not, it's a reformulation.

**The three-sector data constrains any future theory.** a²_lep = 2.000, a²_down = 2.388, a²_up = 3.093. Only charged leptons satisfy K = 2/3. A viable derivation must produce 2 specifically, explain why quarks deviate, and predict the ordering.

**The conditional parameter reduction (18 → 17) is maintained.** IF K = 2/3 is exact, THEN m_τ is predicted from m_e and m_μ (PHYS-8: predicted 1776.97 MeV vs measured 1776.86 ± 0.12 MeV, 0.91σ). The conditional survives the C₃ closure — the derivation path is closed, not the empirical observation.

---

## Errata Assessment

**E2 is significant.** The example in Appendix B.3 claims a² = 3.46 for masses (1, 100, 10000). The correct value is a² = 2.919. The erratum provides the correct computation: K = 10101/12321 = 0.8198, a² = 2(3K − 1) = 2.919. The qualitative point (120° spacing fits arbitrary masses with K ≠ 2/3) is unchanged, but the numerical example was wrong.

**E1 confirms no erratum needed** — the (1 + a²/2)/N identity IS correct for all N ≥ 3.

**E3 confirms** the three-sector a² values are consistent between abstract (rounded) and body (precise).

---

## LEMU Assessment

**L:** The tautology argument is airtight — degree-of-freedom counting is elementary linear algebra. The saddle point argument is qualitative (no numerical δK values given for specific ε) but structurally correct: K increases in one direction and decreases in another, which is the definition of a saddle. Annotation A1 correctly notes that quantitative values would strengthen the argument. Logic passes.

**E:** The Koide ratio K = 0.666661 is Level 2, verified against DATA-3 at 0.91σ from 2/3. The quark sector ratios are Level 2. Empirical passes.

**M:** The key computation is the degree-of-freedom count (3 parameters, 3 equations → exactly determined → tautology). This is trivially correct. The reformulation equivalences are algebraic identities. Math passes.

**U:** Extremely high for time savings. The paper estimates 3–6 hours saved per future session that would otherwise attempt the C₃ path. The reformulation catalog with the "contains new physics?" test is operationally decisive.

---

## What Was Novel

**The "reformulation test" (Section 7)** is the paper's sharpest contribution to methodology. "Does it contain any input beyond the three masses? If not, it is a reformulation." This one-sentence test eliminates entire categories of proposed "derivations." Applied to the catalog of seven known reformulations: all fail. None contains physics beyond the masses.

**The three-sector amplitude ordering** (a²_lep = 2.000 < a²_down = 2.388 < a²_up = 3.093) is documented with the correction from Annotation A2: the ordering does NOT correlate with the mass ratio m_heaviest/m_lightest (which goes leptons > up > down). The amplitude measures spread in √m space relative to the mean of √m, which is a different quantity.

**The "double kill" framing** (Section 6) is rhetorically effective: the C₃ path succeeds on the tautological part and fails on the non-trivial part. Its success is uninformative and its failure is where it matters.

---

## Connections to Active Research

**The Koide amplitude a² = 2 and the integer 2.** In the QED-to-GR scan, the integer 2 appears as: 22 = 2 × 11 in the DM ratio (22/13)π, 2 as the pure-gauge gap ratio C₂(SU(2))/(C₂(SU(3)) − C₂(SU(2))), and 2 as the Koide amplitude squared. Whether these appearances of 2 are connected is completely unknown. The Koide 2 is a Level 2 observation (measured from masses). The gap ratio 2 is Level 1 (from Casimir ratios). The DM 22 is a Level 2 numerical observation. No derivation connects them. This is noted for the record, not claimed as a finding.

**The conditional parameter reduction connects to the PHYS-7 θ_QCD derivation.** Both reduce the SM parameter count by 1. PHYS-7: θ_QCD = 0 from energy minimization (18 → 17, unconditional). PHYS-8/23: m_τ from Koide (17 → 16, conditional on a² = 2 being exact). If both hold: 16 free parameters. The gap ratio analysis (PHYS-13–15) does not depend on either reduction — it uses all three couplings as independent Level 2 inputs regardless.

**The quark sector deviations** (a²_down = 2.388, a²_up = 3.093) connect to the Cabibbo Doublet through the down-type quark sector. The Cabibbo Doublet adds a fourth down-type quark (the b' at 1.5–6 TeV). If K = 2/3 held for charged leptons because of some property of the three-mass system, would adding a fourth mass to the down sector change the Koide ratio? For four masses, the parametrization would be √m_k = M(1 + a cos(θ₀ + 2πk/4)) with k = 0,1,2,3. Four parameters, four masses — still exactly determined (tautology for N = 4). The K = 2/4 = 1/2 condition would be a² = 2 again (since (1 + a²/2)/4 = 1/2 gives a² = 2). Whether the four down-type quarks (d, s, b, b') satisfy K = 1/2 cannot be tested until the Cabibbo Doublet mass is measured.

---

## Remainder Framework Update

**The Koide amplitude a² = 2 as a remainder.** The allowed range for K is [1/N, 1) from Cauchy-Schwarz. For N = 3: [1/3, 1). The midpoint is 2/3. In the remainder framework: modulus = range width = 1 − 1/3 = 2/3. K's position within the range: (K − 1/3)/(2/3) = (2/3 − 1/3)/(2/3) = 1/2. The Koide ratio sits at exactly the MIDPOINT of the allowed range. The "remainder" is 1/2 — the most symmetric possible position.

Whether this midpoint property has physical content or is itself a reformulation (it is algebraically equivalent to K = 2/3) is the open question. The paper correctly classifies it as a reformulation (#6 in the catalog).

---

## Position After PHYS-23

Twenty-three papers read. All physics papers PHYS-1 through PHYS-23 are now processed. The final paper is PHYS-24 — the manuscript that integrates everything. Per the operational procedure change, for PHYS-24 we read the paper first, then the code.

**The series arc is complete through PHYS-23:**
- PHYS-1–4: Foundation (mass as inertia, transformation laws, G untested, calibration)
- PHYS-5–6: VP running and confinement wall
- PHYS-7: θ_QCD derivation (18 → 17 parameters)
- PHYS-8: Koide decomposition (conditional 17 → 16)
- PHYS-9: QED chain (α ↔ a_e at 4.3 ppb)
- PHYS-10–11: Remainder framework (nine domains, three subgroups, R₂ universal)
- PHYS-12: Electroweak anatomy (7 → 11, overconstrained)
- PHYS-13–15: Gap ratio → elimination cascade → two survivors
- PHYS-16–20: Cabibbo Doublet pentalogy (spec, democracy, mechanism, evidence, proton decay)
- PHYS-21: Level 1/Level 2 boundary
- PHYS-22: A₂ geometric cancellation
- PHYS-23: Koide C₃ closure

Ready for PHYS-24 (the manuscript).

---

## Plan for "You Are Here" Super Notebook — From Current Context

**Purpose:** Map everything I know from 23 physics papers, 6 math papers, the QED-to-GR exploratory scans, and the active research notebooks. Written BEFORE reading PHYS-24 so we can compare my understanding to the manuscript's presentation.

---

### SECTION 1: THE FOUNDATION — WHAT THE SERIES PROVED

**1a. The Transformation Laws Are Integers**

The SM's structure is built from exact rationals traceable to the gauge group SU(3)×SU(2)×U(1). Every beta coefficient, every Dynkin index, every gap ratio is a ratio of small integers. The series computed these in Fraction arithmetic at 100-digit precision. No floating point enters the computation chain. The values are not approximations — they are theorems.

Key numbers: b₁ = 41/10, b₂ = −19/6, b₃ = −7. Gap ratio 218/115. Per-generation contribution (4/3, 4/3, 4/3). Pure-gauge gap 22/11 = 2. These are Level 1 — the same in any universe with the same gauge group.

**1b. The Geometric Constants R₂ and R₄**

R₂ = π/4 (2-ball in 2-cube) appears in 9/9 physics domains tested. R₄ = π²/32 (4-ball in 4-cube) appears in the QED two-loop coefficient and the Chern-Simons normalization. These are the atomic units of geometric content in 2D and 4D respectively. The Q335 basis provides exact Fraction arithmetic for all transcendentals.

**1c. The Remainder Framework**

Nine formal domains across three irreducible subgroups. Subgroup A (7 domains, periodic, R₂ in the modulus). Subgroup B (1 domain, monotonic accumulation through thresholds — the VP running). Subgroup C (1 domain, topological, R₄ in the normalization). R₂ universal across all nine. Two independent R = 0 mechanisms (dynamical and topological). Ground state principle: R = 0 from energy minimization on 8R₂-periodic domains.

82/82 PSLQ null: no SM parameter is a rational linear combination of the Q335 basis. The null is the signature of hierarchical composition — composite soliton boundaries produce transcendentals outside any single class.

**1d. The QED Chain**

One measurement (a_e) plus the integer QED series (A₁ = 1/2, A₂ = −0.329, A₃ = +1.181, A₄ = −1.912) inverts to give α at every scale. α⁻¹ = 137.035998583, 4.3 ppb from CODATA. Round-trip residual < 10⁻⁴⁶. NOT a parameter reduction (relabeling), but the most precise test of QED.

A₂ decomposes into three pieces: rational (197/144 = +1.368), number-theoretic ((3/4)ζ(3) = +0.902), geometric (R₄ × (8/3 − 16 ln 2) = −2.598). 87% cancellation. The smallness is accidental. The sign is from IR dominance. The R₄ power counting: R₄^(n−1) at n loops. MATH-3 wall at four loops (elliptic integrals).

**1e. The Electroweak Overconstrained System**

Seven Level 2 inputs determine eleven observables through integer coefficients from the gauge group. 14/14 checks pass. R_b overshoots by 1.6% (diagnosed: missing t-b-W vertex correction). sin²θ_W extracted independently from A_l and A_FB^l, agreeing to 3.9 × 10⁻⁵.

---

### SECTION 2: THE GAP RATIO AND THE CABIBBO DOUBLET

**2a. The Unification Failure Is a Boson Problem**

Gap ratio 218/115 = 1.896 vs measured 1.358. 40% miss. SM does not unify. The miss comes from the gauge self-coupling asymmetry (0, −22/3, −11) — U(1) is abelian, gets zero. Fermions contribute EXACTLY zero (generation democracy: 4/3 = 4/3 = 4/3 cancels in the ratio). The Higgs provides 16% of the needed correction. The remaining 84% requires BSM physics.

**2b. The Elimination Cascade**

15 single-multiplet candidates enumerated in exact Fraction arithmetic. Stage 1 (gap ratio within 0.15): 12 eliminated, 3 survive. Stage 2 (proton decay M_GUT > 10^15.5): SU(5) 5+5̄ eliminated. Two survivors: MSSM (7/5 = 1.400) and VL quark doublet (38/27 = 1.407). Stable across thresholds 0.05–0.20.

**2c. The Cabibbo Doublet**

Vector-like quark doublet (3,2,1/6). Upper Q = +2/3, lower Q = −1/3. Beta shifts (1/15, 1, 1/3). Asymmetry ratio Δb₂/Δb₁ = 15 — highest of any candidate. Y = 1/6 is the smallest hypercharge for standard quark charges, giving 1/Y² scaling: Δb₂/Δb₁ ∝ 1/Y². The double action: numerator shrinks 13%, denominator grows 17%, combined 26% reduction. Gap ratio 38/27. Distance 0.049 from measured. 35× more efficient per field than the MSSM.

**2d. Two Roads Converge**

Gap ratio path (this series, 2026): three couplings → beta coefficients → gap ratio → elimination cascade → (3,2,1/6). Determines representation and M_GUT = 10^15.5.

Anomaly path (literature, 2019–2024): CKM unitarity deficit (2.5–4σ), A_FB^b (~3σ), Higgs μ (~2σ) → global fit → VL quark doublet. Determines mass (1.5–6 TeV) and mixing (|V_ub'| ≈ 0.045).

Neither knew about the other. Each anomaly uses a different quantum number: CKM needs SU(2), A_FB^b needs SU(3)×SU(2), Higgs needs SU(3). The full (3,2,1/6) is required.

**2e. The Proton Decay Test**

M_GUT = 10^15.5 → τ ~ 10^34–35 years (minimal SU(5)). Super-K bound: τ > 2.4 × 10^34. Viable range: ~3 × 10^34 to 10^35. Hyper-K (2027–2037): covers the entire range. 10-year limit 6.3 × 10^34, 20-year ~10^35. MSSM predicts τ ~ 10^37 (unreachable). The M_GUT⁴ scaling amplifies a factor-63 difference in M_GUT to a factor-10⁷ in lifetime.

---

### SECTION 3: THE PARAMETER REDUCTIONS

**3a. θ_QCD = 0 (unconditional)**

PHYS-7. Energy minimization on the QCD vacuum with the measured quark mass matrix gives θ = 0. Parameter count 18 → 17. This is a derivation, not a measurement.

**3b. m_τ from Koide (conditional)**

PHYS-8. IF K = 2/3 is exact, THEN m_τ = 1776.97 MeV (0.91σ from measured). Parameter count 17 → 16 conditional. The C₃ path to deriving a² = 2 is closed (tautology + saddle point, PHYS-23). The conditional survives but the derivation is unknown.

---

### SECTION 4: THE NORMALIZATION RESOLUTION

The convention discrepancy from sin2_theta_w_0.py ("VL = 4× scalar") is resolved. The library values (1/15, 1, 1/3) are correct. The GUT normalization factor for U(1) is (3/5), not (2/5) as written in PHYS-16 Appendix C — but the result 1/15 is correct either way when the formula is done right. PHYS-25 should document: correct formula with (3/5), MSSM gate verification, Y = 1/6 minimality argument, and convention comment correction.

---

### SECTION 5: THE QED-TO-GR EXPLORATORY PROGRAM

**5a. The Five Signals**

From qed_predicts_gr.py (10/10) and qed_gr_scan_2.py (10/10):

1. **VP step connection:** At N=100 boundary transits, (1−r)/[α/(3π)] = 1.045 (4.5% from k=1). The Hubble tension is ~100 VP-step-units of correction.

2. **Cosmological constant from α^57:** α^57 = 10^−121.80 vs Λ_Planck = 10^−121.54 (miss 0.26 decades). 57 = 3 × 19, where 19 = |b₂_SM numerator|.

3. **Dark matter ratio:** DM/baryon ≈ (22/13)π = 5.317 vs measured 5.320 (0.07% hit). 22 = 2×11 (Yang-Mills), 13 = |b₂_mod numerator|.

4. **Product form hit:** α²π²(20/13) = 0.000809 matches (1−r) at N=100 to 0.08%. The 20 = 3|b₃_mod| since b₃_mod = −20/3.

5. **The exact identity:** 57/39 = 19/13 = |b₂_SM_num|/|b₂_VL_num|. Verified exact in Fraction arithmetic. The ratio of cosmological constant exponents equals the ratio of SU(2) beta numerators.

**5b. The Integer 13 Pattern**

Appears in four independent results: b₂_mod numerator (−13/6), DM ratio denominator (22/13), Λ exponent factor (3×13 = 39), product form denominator (20/13). All trace to b₂_mod = b₂_SM + Δb₂ = −19/6 + 1 = −13/6, where the +1 comes from the Cabibbo Doublet.

**5c. Status**

All signals are PROPOSED, not confirmed. The QED-to-GR research program tech spec (qed_to_gr_program.md) specifies eight scripts across four phases, with a decision tree producing one of three outcomes (A: confirmation, B: null, C: partial). Phase 1 priority: phys25_lambda_from_b2.py and phys25_product_form_verify.py.

---

### SECTION 6: THE CONCEPTUAL NOTEBOOKS

**6a. Soliton Hierarchy as Composite Objects**

Soliton boundaries at every scale from VP clouds (10⁻¹³ m) to the observable universe (10²⁶ m). ~20 distinct boundary types across ~40 orders of magnitude. Each boundary has shells (density profile → functional form of correction within the boundary). Each shell contributes a rational correction from its geometry (R₂ for spheres, R₄ for tori). The product across shells and boundaries is transcendental (PSLQ null) even though each factor is rational.

**6b. The Hubble Tension as VP Running**

H₀ local (73) vs CMB (67.4). Modeled as cumulative VP-like correction over ~100 soliton boundary crossings. Per-transit correction ≈ α/(3π). Total correction ≈ 100 × α/(3π) ≈ 0.077 vs ln(H₀_CMB/H₀_local) ≈ −0.081. Directional H₀ predicted: more boundaries = lower H₀.

**6c. The QED-to-GR Maximum Boundary Crossing**

QED and GR operate at opposite ends of the soliton hierarchy. Describing one from the other requires running through every boundary layer. The confinement wall is the first obstruction. Each subsequent boundary type potentially introduces its own perturbative breakdown. GR's smooth geometry is the LIMIT of discrete QED corrections after all perturbative structure has been averaged out.

**6d. The Bessel Zero Barrier**

82/82 PSLQ null extended to Bessel zeros. Bessel zeros are transcendentals independent of Q335. Composite soliton hierarchy produces transcendentals outside any single class. This is why PSLQ finds nothing — the measured constants are composites across geometric classes.

---

### SECTION 7: THE LEVEL 1 / LEVEL 2 BOUNDARY

Level 1: determined by the gauge group — representations, beta coefficients, gap ratios, scaling laws. The same in any universe with SU(3)×SU(2)×U(1).

Level 2: supplied by the universe — masses, couplings, mixing angles, existence of particles. Could have been different.

Derived: Level 1 applied to Level 2 — M_GUT, τ_proton, a_e from α.

The Cabibbo Doublet is the first entity where Level 1 identification precedes Level 2 confirmation. Historical precedent: charm (4 yr gap), W/Z (16 yr), Higgs (48 yr). Also: monopoles (95 yr, not found), axions (49 yr, not found). Level 1 identification is necessary but not sufficient.

Six explicit false claims documented: Level 1 does NOT determine the mass, the mixing angles, the existence, prove unification, determine the GUT group, or predict τ precisely.

---

### SECTION 8: WHAT IS OPEN

**Computations not yet done:**
- Two-loop correction to the 57 and 39 exponents (does it close the 0.26-decade gap?)
- Statistical control on (22/13)π for DM ratio (is the 0.07% hit significant?)
- The 20/13 = (3|b₃_mod|)/|b₂_mod_num| identity verification
- Galaxy survey boundary count (what is the real N for a CMB line of sight?)
- Three-parameter H₀ fit (r_sphere, r_torus, r_void)
- A₃ decomposition (does the 87% cancellation pattern persist?)

**Questions not yet answered:**
- Why a² = 2 for charged leptons (Koide derivation unknown)
- What physical mechanism makes a soliton boundary crossing produce α/(3π) correction to H₀
- Whether G runs through soliton boundaries (testable at L2 outside Hill sphere)
- Whether the 19/13 connection to Λ is physics or numerology
- Whether the Cabibbo Doublet exists (Hyper-K 2027–2037, HL-LHC through 2040)

**Parked research:**
- QED-to-GR program (tech spec written, Phase 1 ready to execute)
- Toroidal rotation as dark matter
- Modulus superset (boundary shells as geometric stages)
- Remainder framework staged across all 23 papers

---

### SECTION 9: THE DATA INFRASTRUCTURE

**phys24_lib.py:** 148/148 platform test. All constants as Fractions. 100-digit precision. Q335 exact arithmetic. No float in the computation chain.

**DATA-4:** 146 entries, 38/38 checks. Seven categories: SI exact (A), measured fundamental (B), EW/Higgs (C), quark/CKM (D), hadronic (E), neutrino/cosmo (F), geometric/derived (G).

**Scripts verified:** sin2_theta_w_0.py (9/9), sin2_theta_w_1.py (9/9), electro_weak.py (14/14), a_2_decomposition_0.py (7/7 or 9/9), phys24_democracy.py (10/10), qed_predicts_gr.py (10/10), qed_gr_scan_2.py (10/10). Plus Session 3 scripts: 98/98 total.

---

### SECTION 10: THE SERIES PATH

PHYS-1 (mass) → PHYS-2 (transformation laws) → PHYS-3 (G untested) → PHYS-4 (calibration) → PHYS-5 (VP running) → PHYS-6 (confinement) → PHYS-7 (θ=0) → PHYS-8 (Koide) → PHYS-9 (QED chain) → PHYS-10 (remainder) → PHYS-11 (nine domains) → PHYS-12 (EW anatomy) → PHYS-13 (gap ratio) → PHYS-14 (unified map) → PHYS-15 (elimination cascade) → PHYS-16 (Cabibbo Doublet) → PHYS-17 (democracy) → PHYS-18 (Y=1/6) → PHYS-19 (anomaly evidence) → PHYS-20 (proton decay) → PHYS-21 (L1/L2 boundary) → PHYS-22 (A₂ cancellation) → PHYS-23 (Koide closure)

Six MATH papers: MATH-1 (R₂), MATH-2 (Q335), MATH-3 (PSLQ), MATH-4 (engineering), MATH-5 (R₄), MATH-6 (Bessel barrier)

Total: 29 papers. One manuscript (PHYS-24) to integrate them all.

---

**This is my understanding of "everything" before reading PHYS-24. The differences between this map and the manuscript's presentation will reveal what the author emphasizes differently, what I may have missed, and what the manuscript adds beyond compilation.**

