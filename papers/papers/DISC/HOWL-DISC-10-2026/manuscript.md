# The Level 1 / Level 2 Boundary
## Results of R₂ = π/4 appearring in 9 out of 9 physics domains tested

**Registry:** [@HOWL-DISC-10-2026]

**Series Path:** [@HOWL-DISC-6-2026] → Phase 1-4 Execution → [@HOWL-DISC-7-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** April 1 2026

**Domain:** Research Program / Mathematical Physics / SM Parameter Reduction

**Status:** Complete (Retrospective)

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Abstract

This paper documents the boundary between what the HOWL framework determines and what it does not. Twenty-four papers (MATH-1 through MATH-5, PHYS-1 through PHYS-14, DATA-1 through DATA-3, DISC-6 through DISC-8) have established that R₂ = π/4 appears in 9/9 physics domains across three irreducible subgroups, that transformation laws connecting observables are built from integers, and that parameter values are structureless in every basis tested. This paper collects the evidence, states the boundary, and maps every Standard Model parameter to one side or the other.

The boundary: the framework determines structure (which geometric constants appear, what the moduli are, where ground states sit, what the transformation law coefficients are). It does not determine values (couplings, masses, mixing angles). The evidence comes from both sides — positive results that derive structure, and null results that fail to derive values.

---

## 1. What the Framework Determines (Level 1)

Level 1 content is determined by the geometry of the framework — the R₂/R₄ separation, the gauge group structure, and the integer arithmetic of transformation laws. Every Level 1 result has been computed in exact Fraction arithmetic with passing assertions.

### 1.1 Geometric Constants in Physics

R₂ = π/4 appears in 9 out of 9 physics domains tested (PHYS-11). The classification into three irreducible subgroups is:

**Subgroup A (phase-periodic, 7 domains):** Theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone, Aharonov-Bohm, flux quantization, AC Josephson. All share modulus 8R₂ × scale. Ground state at R = 0.

**Subgroup B (monotonic, 1 domain):** Renormalization group running. R₂ in step size 1/(12R₂). Not periodic — proven irreducible by VP closure theorem.

**Subgroup C (topological, 1 domain):** Chern-Simons. Modulus = 1. R₄ in normalization 1/(256R₄).

The doubly-native property (MATH-5): R₂ and R₄ are the only n-ball remainders with pure power-of-2 denominators, making them native to both exact rational and binary arithmetic. This is a mathematical fact about the dimensions physics uses.

### 1.2 Integer Transformation Laws

The electroweak sector (PHYS-12) runs on integer coefficients from three sources:

**Gauge group:** N_c = 3, T₃ = ±1/2, Q_f = 0/±1/±1/3/±2/3. These determine the vector and axial couplings of every fermion.

**Generation count:** 3 neutrinos, 3 charged leptons, 2 up-type quarks (u,c contributing to Γ_Z), 3 down-type quarks. These determine the channel counting.

**Loop expansion:** The 3 and 8 in Δρ = 3G_Fm_t²/(8π²√2). The QCD coefficients 1, 365/24, etc. The 3/4 in A_FB = (3/4)A_eA_f. The 12 in σ⁰_had.

Seven measured inputs (G_F, M_Z, α⁻¹, sin²θ_W, α_s, m_t, m_H) plus these integers produce 11 observables that agree with LEP measurements at 0.05–2.1% (tree + Δρ level). Every residual is explained by known missing one-loop corrections of predicted size and sign.

The beta function coefficients (PHYS-5, PHYS-13) are exact rationals: b₁ = 41/10, b₂ = −19/6, b₃ = −7. These determine the gap ratio 218/115 and the running of all three gauge couplings. The integers trace entirely to the gauge group representation content.

### 1.3 QED Coefficient Anatomy

The 2-loop QED coefficient A₂ = −0.32848 decomposes (PHYS-12) into three pieces with distinct origins:

| Piece | Expression | Value | Origin |
|---|---|---|---|
| Rational | 197/144 | +1.368 | Diagram combinatorics |
| Number-theoretic | (3/4)ζ(3) | +0.902 | Feynman parameter integrals |
| Geometric | R₄ × (8/3 − 16ln2) | −2.598 | 4D phase space × IR regulation |

The geometric piece dominates and has opposite sign. The positive pieces cancel 87.4% of the geometric piece, making A₂ accidentally small. The R₄ content (Level 1 geometry) nearly cancels the rational + number-theoretic content. This separation connects to the Brown-Schnetz program on Galois coaction of multiple zeta values, where the geometric/arithmetic decomposition of Feynman integrals is studied systematically.

### 1.4 Ground States

θ_QCD = 0 (PHYS-7) from energy minimization of −cos(θ) on the 8R₂ periodic domain. The vacuum is defined as the minimum energy state. The minimum of −cos(θ) is θ = 0. This is a Level 1 determination: the ground state follows from the potential shape and the periodicity, both of which are geometric. Parameter count: 19 → 18.

---

## 2. What the Framework Does Not Determine (Level 2)

Level 2 content is supplied by the universe through measurement. The framework provides the equations connecting these values but does not predict them. The evidence for Level 2 status comes from exhaustive failed attempts at derivation.

### 2.1 The PSLQ Record

82 PSLQ tests across six categories, all null (DISC-6 through DISC-8, extended this session):

| Category | Tests | Precision | Result |
|---|---|---|---|
| SM parameters vs transcendental basis | 51 | 4-12 digits | 51/51 null |
| Residual PSLQ on α_s candidate | 5 | 10 digits | 5/5 null |
| Optical clock ratios | 5 | 15 digits | 5/5 null |
| Mass ratios, BCS gap, Feigenbaum | 6 | 8-30 digits | 6/6 null |
| Modular search | ~600 | 4-12 digits | Noise (controlled) |
| Bessel zeros (j₁₁, j₀₁, j₁₂, derived) | 10 | 100 digits | 10/10 null |
| **Total** | **82** | | **82/82 null** |

The Bessel zero tests at 100 digits with maxcoeff 10,000 are the highest-precision PSLQ in the series. The modular search control test showed SM parameters produce hits at exactly the same rate as random numbers. The best candidate (α_s = πζ(3)/32) was killed by formal control — 3.72% of random numbers match equally well.

No measured or analytical constant in the database is a linear combination of the transcendental basis {π, e, ln 2, √2, √3, √5, √7, φ, ζ(3), ζ(5), Li₄(1/2), Catalan, γ, e^π} with integer coefficients up to 10,000.

### 2.2 The Multi-Base Null

The DATA-2 multi-base scan tested all 107 values in 19 bases from 2³³⁵ to 210³⁸. Composite bases (60⁵⁰, 210³⁸) show 13-15 digit average improvement over 2³³⁵ for transcendental constants. The control test with 90 generic irrationals (√primes, ∛primes, ln primes, log ratios, special functions) gives z-scores 0.77 and 1.80 — not significant. The improvement is a generic mathematical property of composite denominators, not specific to physics constants.

No measured constant has a preferred numerical base. The Level 2 parameters are structureless in the rational number system.

### 2.3 The Koide Amplitude

The Koide formula K = 2/3 for charged leptons is equivalent to a single number: the amplitude a² = 2 in the parametrization √m_k = M(1 + a cos(θ₀ + 2πk/3)). The 120° spacing is a tautology — the three-parameter fit to three masses always produces 120° spacing by construction. The sum cos(φ₁) + cos(φ₂) + cos(φ₃) = 0 is a trigonometric identity for 120°-spaced arguments, verified to machine precision in all three fermion sectors.

The amplitude ordering from DATA-3 masses:

| Sector | a | a² | K | K − 2/3 |
|---|---|---|---|---|
| Charged leptons | 1.4142 | 2.0000 | 0.6667 | −6.2 × 10⁻⁶ |
| Down quarks | 1.5452 | 2.3877 | 0.7313 | +6.5 × 10⁻² |
| Up quarks | 1.7586 | 3.0928 | 0.8488 | +1.8 × 10⁻¹ |

The C₃ frustrated potential path was investigated and closed. K = 2/3 is a saddle point under phase perturbation, not a minimum. The direction of quark deviation is not predicted.

All equivalent reformulations of a² = 2 (CV = 1, midpoint of [0,4], critical amplitude, Var = Mean², simplex midpoint in a²) are restatements, not derivations. The Koide amplitude is Level 2. The conditional parameter reduction (18 → 17) from PHYS-8 remains conditional on a derivation of a² = 2 that does not yet exist.

### 2.4 The Unification Gap

The SM gap ratio (b₁−b₂)/(b₂−b₃) = 218/115 = 1.896 is Level 1 — determined entirely by the gauge group representation content. The measured gap ratio from DATA-3 couplings is 1.358 — Level 2. They differ by 36%. The SM does not unify.

The MSSM gives gap = 7/5 = 1.400 (Level 1 given the MSSM particle content), nearly matching the measured 1.358. A single vector-like quark doublet (3,2,1/6) gives gap = 1.407. Which particles exist — if either the MSSM or the VL doublet is correct — is Level 2. The framework identifies what beta function modifications are needed but not which particles provide them.

### 2.5 The Electroweak Extractions

The overconstrained EW system (PHYS-12) extracts sin²θ_W independently from two observables:

| Source | Extracted sin²θ_W | Δ from input |
|---|---|---|
| A_l (SLD) | 0.23098 | −2.4 × 10⁻⁴ |
| A_FB^l (LEP) | 0.23102 | −2.0 × 10⁻⁴ |

The two agree to 3.9 × 10⁻⁵. Both are shifted from the input by the known tree-to-effective sin²θ_W correction. This confirms consistency but does not derive sin²θ_W — the shift is entirely explained by missing one-loop corrections, not by new physics or a structural prediction.

The α_s extraction gives 0.104-0.105 versus the input 0.118 (12% systematic from missing b-quark vertex corrections). Again, consistency, not derivation.

---

## 3. The Boundary Map

Every Standard Model parameter assigned to Level 1 or Level 2, with the evidence and source paper:

| Parameter | Status | Evidence | Source |
|---|---|---|---|
| θ_QCD | **Derived** (= 0) | Energy minimization on 8R₂ domain | PHYS-7 |
| m_τ (given m_e, m_μ) | **Conditional** | Koide a² = 2, match at 0.91σ | PHYS-8 |
| α ↔ a_e | **Transformation** | QED series inversion, 4.3 ppb residual | PHYS-9 |
| R₂ in 9/9 domains | **Level 1** | Three irreducible subgroups | PHYS-11 |
| EW transformation laws | **Level 1** | All integers from gauge group | PHYS-12 |
| A₂ geometric content | **Level 1** | R₄ carries 87% of magnitude | PHYS-12 |
| Beta coefficients | **Level 1** | Exact rationals from representation content | PHYS-13 |
| Gap ratio 218/115 | **Level 1** | Ratio of beta coefficient differences | PHYS-13 |
| α⁻¹ = 137.036... | **Level 2** | 82/82 PSLQ null, structureless in all bases | DATA-3, DISC-8 |
| sin²θ_W = 0.23122 | **Level 2** | EW extraction confirms consistency, not derivation | PHYS-12 |
| α_s = 0.1180 | **Level 2** | EW extraction 12% off (missing corrections) | PHYS-12 |
| All fermion masses | **Level 2** | Structureless in all bases, 82/82 PSLQ null | DATA-3 |
| CKM angles | **Level 2** | No clean mass-mixing relation at available precision | DATA-3 |
| Koide amplitude a² = 2 | **Level 2** | All reformulations are restatements, C₃ path closed | PHYS-8, DATA-3 addendum |
| BSM particle content | **Unknown** | Gap ratio identifies need, enumeration identifies candidates | PHYS-13 |

Parameter count: 19 → 18 (θ_QCD derived), conditionally 18 → 17 (Koide). One transformation (α ↔ a_e, not a reduction). 15-16 parameters remain Level 2.

---

## 4. The Methodological Finding

Derivation beats search.

Three reductions succeeded, all from understanding the physics of a specific domain:
- θ_QCD = 0 from energy minimization (PHYS-7)
- m_τ from the Koide formula given m_e and m_μ (PHYS-8, conditional)
- α from a_e via QED series inversion (PHYS-9, transformation not reduction)

Every scan returned noise:
- 82/82 PSLQ null across all categories
- Modular search indistinguishable from random numbers (controlled)
- Multi-base scan killed by control test (z-scores 0.77, 1.80)
- C₃ frustrated potential closed as tautology
- sin²θ_W from 3/8 + running equivalent to gap ratio test, not independent

The framework is a language for writing physics equations in exact arithmetic. It exposes the integer structure of transformation laws. It is not a theory that generates parameter values from first principles. The integers are determined. The values are not.

---

## 5. The Verified Data Foundation

DATA-3 provides 123 entries (107 original + 16 Koide-derived) verified by 32 internal consistency checks. The physical relations R∞ = α²m_ec/(2h), a₀ = ℏ/(m_ecα), μ₀ = 2αh/(ce²), and m_D = m_p + m_n − E_D all hold to 9.9-11.9 digits. The Q335 basis is internally consistent at 101 digits. All SI defining constants are stored at exact values.

The lattice annotation documents that entries 41-43 (m_c/m_s, m_b/m_c, m_u/m_d from lattice QCD) are independent data not derivable from the individual PDG quark masses by division, due to renormalization scale mismatch. This is a structural finding about the database, not an error.

The entire data foundation — every measured value, every analytical constant, every derived quantity — is available as exact Fractions for any future computation. The platform is verified and ready.

---

## 6. Leads and Open Work

### 6.1 The Koide Amplitude

The amplitude a² = 2 for charged leptons remains the single most important open problem in the series. The C₃ spacing path is closed. The reformulations (CV = 1, midpoint, critical amplitude) are equivalent, not explanatory. The amplitude ordering a_lep < a_down < a_up constrains any future theory — it must explain why leptons sit at the critical value while quarks exceed it, with the ordering correlated to the mass hierarchy spread.

A viable path would need to identify what physical mechanism selects the midpoint of the variance range on the mass simplex, without reducing to a restatement of the Koide formula itself.

### 6.2 The b-Quark Vertex Correction

One Feynman diagram (the t-b-W triangle) added to the PHYS-12 computation would bring R_b from 1.6% agreement to ~0.3%, and the α_s extraction from 12% off to ~3%. The formula is known analytically with rational coefficients times m_t². The Fraction arithmetic infrastructure is ready. This is the highest-yield single improvement to the electroweak computation.

### 6.3 The Full Δr Correction

Replacing Δρ with the full Δr = Δα − (cos²θ/sin²θ)Δρ + remainder would bring M_W from 0.05% to ~0.01%. The Δα part is the running of α from 0 to M_Z, already computed in PHYS-5. Implementation is straightforward but lengthy.

### 6.4 The A₃ Decomposition

The 3-loop QED coefficient A₃ involves ζ(5), Li₄(1/2), products like π²ζ(3), and π⁴ = 1024R₄². Decomposing A₃ into geometric (R₄, R₄²) and arithmetic (ζ(3), ζ(5)) content would extend the A₂ finding to the next order and test whether the large cancellation between geometry and number theory persists. The analytic result (Laporta-Remiddi) is known. The method is demonstrated by the A₂ computation.

### 6.5 The Vector-Like Quark Doublet

The PHYS-13 finding that a single VL quark doublet (3,2,1/6) fixes gauge coupling unification with M_GUT = 10^15.5 is testable by Hyper-Kamiokande through proton decay searches. Further work could add two-loop beta functions and threshold corrections to sharpen the M_GUT prediction. The gap ratio framework is extensible to multi-multiplet extensions and non-minimal scenarios.

### 6.6 The Confinement Wall

PHYS-6 characterized the two faces of confinement: perturbative above ~2 GeV, non-perturbative below. The ratio of measured to perturbative hadronic VP below 2 GeV is approximately 0.61, close to the vena contracta coefficient π/(π+2) = 0.6108. This numerical proximity is likely coincidental (the confinement ratio is approximate and kernel-dependent) but has not been tested at sufficient precision. Future lattice QCD data at higher precision could resolve whether this is coincidence or connection.

### 6.7 Neutrino Mixing

The PMNS mixing angles (sin²θ₁₂ ≈ 0.307, sin²θ₂₃ ≈ 0.545) are close to tribimaximal values (1/3, 1/2). Current precision (2-3 sig figs) is too low for meaningful PSLQ. Future oscillation experiments (DUNE, Hyper-K, JUNO) will push to 4-5 sig figs, enabling the same search protocol applied to CKM angles. The DATA-3 framework is ready to accept updated values.

### 6.8 Higher-Precision Measurements

Belle II will improve m_τ from 6 to 7-8 significant figures. This directly sharpens the Koide test: the CF partial quotient a₄ = 18050 will either grow (K closer to 2/3) or shrink (K diverging). The PHYS-8 conditional depends on this measurement. Updated lattice QCD mass ratios would improve the quark Koide amplitudes from 3 sig figs to 4-5, enabling the first meaningful test of whether the amplitude ordering has fine structure.

---

## 7. Series Status

| Track | Papers | Summary |
|---|---|---|
| MATH | 1-5 | R₂ separation, integer basis, dimensional generalization, Q335, n-ball uniqueness |
| PHYS | 1-14 | 9 domain extractions, α running, θ_QCD, Koide, QED series, remainder framework, three subgroups, EW anatomy, GUT unification |
| DATA | 1-3 | 268 source values, 123 Q335 entries, verified and annotated |
| DISC | 6-9 | Search plan, execution, control tests, this boundary paper |

The geometry is determined. The parameters are measured. The boundary between them is documented. The platform is verified and ready for the next computation.

---

*DISC-9 is the boundary paper of the HOWL series. It documents where the framework's reach ends and where the universe's input begins, based on evidence from 24 papers, 82 PSLQ nulls, 32 database consistency checks, and computations spanning QED, the electroweak sector, and gauge unification. The boundary is the finding.*
