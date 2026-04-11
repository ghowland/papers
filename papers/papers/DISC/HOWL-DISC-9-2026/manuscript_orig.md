# The Remainder Extraction Program
## What the Framework Determines and What It Doesn't

**Registry:** [@HOWL-DISC-9-2026]

**Series:** Discovery

**Series Path:** [@HOWL-DISC-6-2026] → [@HOWL-DISC-7-2026] → [@HOWL-DISC-8-2026] → [@HOWL-DISC-9-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 31 2026

**Domain:** Methodology / Mathematical Physics / SM Parameter Problem

**Status:** Complete (Program Capstone)

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

The Remainder Extraction Program (DISC-6 through DISC-8) built a framework, executed four phases, ran three search strategies under statistical control, and produced a classification of nine physics domains into three subgroups with one universal constant R₂ = π/4. The program derived no new SM parameter values. This paper identifies why, and argues that the finding is itself the result.

The framework determines Level 1 (geometric) structure: moduli, subgroup classification, which n-ball remainder R_n appears in which domain, and the ground state principle that produces θ_QCD = 0. This structure is universal — it follows from the geometry of circles and spheres and the mathematical properties of periodicity, monotonicity, and gauge invariance. It does not depend on which universe we live in.

The framework does not determine Level 2 (domain-specific) continuous parameters: coupling constants, mass ratios, mixing angles. These are the remainders that populate the geometric framework. Three search strategies — linear PSLQ (17 targets, 35 constants, maxcoeff 10,000), nonlinear PSLQ (8 targets, 10 transforms, maxcoeff 1,000), and synthesis-informed modular search (13 targets, 18 moduli, formally controlled against random numbers) — all returned null. SM parameter values are not simple functions of the transcendental basis under any tested relationship.

The three parameter reductions in the series (θ_QCD = 0, m_τ via Koide, α from a_e) all came from domain-specific physics — energy minimization, an empirical mass formula, QED perturbative series — not from the framework itself. The framework provided the language for expressing these reductions but did not generate them.

The central finding: the geometric structure of physics equations is universal and determined. The specific parameter values that populate this structure are not determined by the structure. The boundary between these — between what the equations' form determines and what the universe's specific constants supply — is where the program arrived, and identifying this boundary precisely is the contribution.

---

## II. WHAT THE FRAMEWORK DETERMINES

### 2.1 The Level 1 Geometric Structure

R₂ = π/4 appears in all nine extracted domains (PHYS-11). The modulus is 8R₂ × (domain scale) in seven of them, R₂ appears in the VP step size in one, and in the Chern-Simons exponential and normalization in the last. R₄ = π²/32 appears wherever 4D geometry or π² is involved — energy eigenvalues from standing-wave quantization, zone-boundary energies, the Chern class normalization, and one-loop integral prefactors.

Eight identities define the framework, all exact Fraction equalities: 2π = 8R₂, π = 4R₂, π/2 = 2R₂, π² = 32R₄, 8π² = 256R₄, 1/(3π) = 1/(12R₂), 1/(8π²) = 1/(256R₄), 4π = 16R₂.

None of this depends on measured constants. A universe with different coupling strengths, different mass ratios, and different mixing angles would have the same R₂, the same eight identities, and the same modular structure. Level 1 is geometry.

### 2.2 The Subgroup Classification

The nine domains fall into three subgroups (PHYS-11 Section III):

Subgroup A (phase-periodic, 7 domains): theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone, Aharonov-Bohm, flux quantization, AC Josephson. All share E(φ) = A − B·cos(φ) on an 8R₂-periodic domain.

Subgroup B (monotonic, 1 domain): RG running. Logarithmic accumulation with R₂ in the step size. Not periodic.

Subgroup C (topological, 1 domain): Chern-Simons. Modulus 1. CS values are pure rationals.

The VP closure theorem (DISC-8) proves this classification is irreducible: no smooth bijection can convert monotonic structure to periodic. The three subgroups are the minimal classification, provably. This too is determined by the mathematics, not by parameter values.

### 2.3 Specific Remainders Determined by Topology or Extremization

The framework determines Level 2 remainders that are forced to specific values by discrete topology or energy minimization:

| Remainder | Value | Mechanism | Determined by |
|---|---|---|---|
| θ_QCD | 0 | Energy minimization of −cos(θ) on 8R₂ domain | Ground state principle |
| Flux quanta | 0 (exact) | Single-valuedness of Cooper pair wavefunction | Topological constraint |
| Maslov correction | μ/4 = 1/2 | Counting soft turning points (μ = 2) | Discrete topology of classical orbit |
| BZ band minimum | k = 0 | Electron filling from energy minimum of −cos(ka) | Ground state principle |

These are all integers, zero, or simple rationals forced by the form of the equations. The ground state principle (minimum of −cos(φ) at φ = 0) produces the first and fourth. Single-valuedness produces the second. Turning-point counting produces the third. In each case, the VALUE of the remainder follows from the FORM of the equation, not from any measured constant.

---

## III. WHAT THE FRAMEWORK DOES NOT DETERMINE

### 3.1 The Level 2 Continuous Parameters

The 18 remaining SM parameters (after θ_QCD; 17 if the conditional Koide m_τ is accepted) are Level 2 remainders: α⁻¹ = 137.036, sin²θ_W = 0.231, α_s = 0.118, m_μ/m_e = 206.77, the CKM angles, the Higgs parameters. The framework says these are remainders living on specific domains (phase-periodic, monotonic, or topological) with specific moduli (8R₂ × scale, mass thresholds, or 1). It does not say what their values are.

The Level 1 structure provides the container. The Level 2 continuous parameters are the content. The framework built in this program determines the container. It does not determine the content.

### 3.2 The Search Nulls

Three search strategies were executed across PHYS-10, DISC-7, and DISC-8:

| Search | Scope | Result | Control |
|---|---|---|---|
| Linear PSLQ | 17 targets, 3 stages (9→20→35 constants), maxcoeff 10,000 | All null | PSLQ internal calibration |
| Nonlinear PSLQ | 8 targets, 10 transforms, 10 constants, maxcoeff 1,000 | All null | PSLQ internal calibration |
| Modular search | 13 targets, 18 moduli, q ≤ 20, threshold 0.05% | 47 SM hits vs 42.3 random mean (0/13 significant at p<0.05) | Formal control: 1000 random numbers per target magnitude |

The modular search specifically: the DISC-8 control test generated 13,000 random numbers at SM-parameter magnitudes and ran them through the identical protocol. Random numbers produce the same hit rate as SM parameters. The discriminating power at the tested threshold is zero.

The α_s = πζ(3)/32 candidate was killed from two independent directions: the control test (3.72% of random numbers near 0.118 produce the same modular signature) and the residual PSLQ (5/5 null at maxcoeff up to 10,000).

The combined null: SM parameters are not connected to the transcendental basis through linear combinations (maxcoeff 10,000), nonlinear transforms (10 types, maxcoeff 1,000), or modular relationships (18 moduli, denominators ≤ 20). The search space is bounded, not exhausted — but the tested region is substantial.

### 3.3 The Koide Midpoint Is a Restatement

The Koide condition a² = 2 was reformulated as the midpoint of the positivity-allowed range [0, 4], equivalently CV² = 1 = midpoint of [0, 2], equivalently Koide = 2/3 = midpoint of [1/3, 1]. These are exact Fraction identities. The frustrated graph mechanism was tested and fails (it controls phase spacing, Koide controls amplitude — structural mismatch proven in DISC-8). The midpoint observation sharpens the question from "why a² = 2?" to "what principle selects the midpoint of the allowed range?" but does not answer it.

---

## IV. THE BOUNDARY

### 4.1 Where It Lies

The framework determines everything that follows from the FORM of the equations:

- The geometry: R₂ = π/4, R₄ = π²/32
- The periodicity structure: modulus 8R₂ × scale
- The classification: three subgroups, irreducible
- The discrete remainders: 0, 1/2, integers (from topology or extremization)

The framework does not determine anything that depends on the SPECIFIC VALUES of measured constants:

- The coupling strengths: α, α_s, sin²θ_W
- The mass ratios: m_μ/m_e, m_τ/m_μ, quark masses
- The mixing angles: CKM parameters, δ_CP
- The Higgs parameters: m_H, v

### 4.2 The Language/Theory Distinction

A language tells you how to express relationships. A theory tells you which relationships hold. The remainder framework is a language: "decompose into integer + remainder on an 8R₂ domain." A theory of the SM parameters would say "the remainder for α_s IS this specific value BECAUSE..." No such theory was produced by this program, and the one candidate (α_s = πζ(3)/32) was noise.

The distinction matters for setting expectations. The framework will not, by itself, derive SM parameters. It will help express derivations that come from physics. The framework provides the postal system — addresses, zip codes, sorting rules. The physics provides the residents.

### 4.3 The Three Reductions Illustrate the Boundary

Every successful parameter reduction in the series used domain-specific physics:

| Reduction | Physical principle used | Framework role |
|---|---|---|
| θ_QCD = 0 | QCD instanton vacuum has cosine energy, minimized at 0 | Says the domain is 8R₂-periodic with cosine energy |
| m_τ from Koide | Empirical mass formula with C₃ symmetry, a = √2 | Says the phases live on an 8R₂ domain |
| α from a_e | QED series A₁-A₄ (Feynman diagram computation) | Provides the transcendental constants in the series |

In every case, the physics came first. The framework organized the result but didn't generate it. Understanding the energy functional (theta vacuum), knowing the empirical formula (Koide), or computing the perturbative series (QED) — these are physics. Expressing the result in remainder language is framework. The boundary is between them.

### 4.4 The Central Finding

The geometric structure of physics equations is universal and determined. The specific parameter values that populate this structure are not determined by the structure.

The geometry is ours. The parameters are the universe's.

This is not a failure of the program. It is the program's finding. The boundary exists, and now its location is documented: Level 1 (geometric) is determined, Level 2 (domain-specific continuous) is not determined by the geometric framework alone. Future parameter reductions will come from understanding specific physical mechanisms that force specific Level 2 values — from physics, expressed in framework language.

---

## V. SPECULATION ON OTHER APPROACHES

The null result of this program applies to the specific searches conducted within the specific framework. Other approaches to the SM parameter problem exist and are not constrained by this null. The following is speculative — no computation or verification is offered — but the program's experience suggests which directions might avoid the boundary identified above.

### 5.1 Bootstrap and Self-Consistency Conditions

The conformal bootstrap program derives operator dimensions and OPE coefficients from consistency conditions (unitarity, crossing symmetry, associativity). These are not "scanning parameter space against a basis" — they derive specific numbers from internal consistency of the theory. If the SM free parameters are constrained by analogous self-consistency conditions at some energy scale, the derivation would come from the theory's structure, not from geometric decomposition. The remainder framework could express the result but could not generate it.

### 5.2 Asymptotic Safety

If gravity is asymptotically safe (non-perturbatively renormalizable), the requirement that RG trajectories reach the UV fixed point may constrain the IR values of SM couplings. This would be a dynamical determination of parameters — Level 2 values forced by the requirement that the RG flow is complete. The framework's Subgroup B (monotonic accumulation, RG running) would be the natural domain, and the determination would come from a boundary condition on the flow, not from geometric structure.

### 5.3 Random Matrix Theory for Mass Matrices

The fermion mass matrices are 3×3 complex matrices. Random matrix theory classifies the statistical properties of eigenvalue distributions. If the lepton mass matrix belongs to a specific random matrix ensemble, its eigenvalue statistics (spacing, ratios) could be predicted. The Koide formula's CV = 1 condition might correspond to a specific ensemble property. This approach would replace "why a = √2?" with "what ensemble has CV = 1 for its eigenvalue square roots?" — a well-posed random matrix question. The lepton-specific nature (quarks don't satisfy CV = 1) would constrain the ensemble.

### 5.4 Discrete Symmetries and Flavor Models

The 120° spacing (C₃ symmetry) in the Koide parameterization could arise from a discrete flavor symmetry group (A₄, S₃, Δ(27), etc.) acting on the three generations. These groups are used extensively in neutrino mass model building. If a specific discrete group forces C₃ symmetric phases AND selects a = √2 through its representation theory, the Koide reduction would become unconditional. The remainder framework would classify the result (Subgroup A, 8R₂ domain, C₃ phases) but the derivation would come from group theory.

### 5.5 The String Landscape (and Its Opposite)

The string landscape approach accepts ~10⁵⁰⁰ vacua and uses anthropic reasoning to constrain parameters. This is the opposite philosophy from parameter derivation — it says the parameters are NOT derivable from first principles but are environmental. The null result of this program is consistent with the landscape picture (parameters are not determined by mathematical structure) but does not support it specifically (the null applies to our specific search, not to all possible derivations).

The opposite view — that a unique vacuum determines all parameters — would require a mechanism not tested in this program. The framework provides the container; the unique-vacuum hypothesis would provide the content.

### 5.6 What the Program's Experience Suggests

The central methodological lesson: derivation beats search. All three reductions came from physical principles, none from scanning. This suggests that the next reduction will come from someone who understands a specific physical mechanism deeply enough to derive a parameter value, not from expanding the search to larger coefficient spaces or more moduli. The framework provides the language for expressing such a derivation and the infrastructure (Q335 basis, exact Fraction arithmetic, verification scripts) for verifying it. The physics is someone else's contribution.

---

## VI. WHAT THE PROGRAM PRODUCED

### 6.1 Infrastructure

The Q335 basis (MATH-4): 22 transcendental constants as integers over 2³³⁵, verified at 100 digits. Extended to 34 constants for QED higher-loop work. Exact Fraction arithmetic for nine physics domains. Verification scripts for every claim in the series. All reusable.

### 6.2 Classification

Nine domains, three subgroups, R₂ universal, R₄ in 4D contexts. The classification is proven irreducible (VP closure theorem). This is a permanent result — it does not depend on future measurements or on parameter values.

### 6.3 The Ground State Principle

Minimum of −cos(φ) on an 8R₂-periodic domain gives R = 0. This produces θ_QCD = 0 (PHYS-7). A second R = 0 mechanism (topological single-valuedness) produces flux quantization. Both operate within Subgroup A through different physics.

### 6.4 The Search Boundary

Linear, nonlinear, and modular searches all null under statistical control. This bounds the space of possible connections between SM parameters and the transcendental basis. The boundary is documented precisely: coefficients ≤ 10,000 for linear, ≤ 1,000 for nonlinear transforms, 18 moduli with denominators ≤ 20 for modular. What lies beyond these bounds is untested.

### 6.5 The Koide Question, Sharpened

a² = 2 = midpoint of [0, 4]. CV = 1. Quarks don't satisfy it. The frustrated graph path is closed (structural mismatch). The question is open, precisely stated, and constrained.

### 6.6 Methodological Lessons

| Lesson | Evidence |
|---|---|
| Run the control test first | DISC-7 reported α_s candidate without control; DISC-8 control killed it |
| Derivation beats search | 3/3 reductions from physics; 0/3 from scanning |
| Publish the plan before results | DISC-6 documented methodology before execution |
| Report nulls honestly | DISC-7 F4 triggered, reported |
| Gate high-effort work on low-effort checks | DISC-8 control test gated α_s derivation, preventing wasted effort |
| Verify each phase before the next | DISC-6 operational rule maintained throughout |

---

## VII. WHAT COMES NEXT

### 7.1 The Koide Derivation

The sole remaining high-priority open target. Making m_τ unconditional requires deriving a² = 2 from a physical principle. The frustrated graph path is closed. The midpoint/CV reformulation is available. The lepton-specific nature (quarks fail) constrains the derivation to lepton-sector physics. Possible approaches: discrete flavor symmetry, random matrix ensemble, or a variational principle that selects the midpoint.

### 7.2 Domain-Specific Parameter Physics

The next parameter reduction will come from understanding a specific physical mechanism deeply enough to derive a Level 2 value. The framework provides the language. Candidates: sin²θ_W from GUT-scale running (requires eliminating M_GUT), quark mass ratios from flavor symmetry, CKM angles from geometric constraints on the unitarity triangle. Each requires domain-specific physics, not framework-level scanning.

### 7.3 Experimental Retesting

When α_s reaches 0.1% precision, δ_CP reaches ±0.01 rad, or quark masses improve by factors of 2-3, the search infrastructure can be rerun with tighter thresholds. The DISC-8 control test shows the current threshold (0.05%) has zero discriminating power, so improvements must be substantial.

### 7.4 Additional Domain Extractions

The three-subgroup structure can be tested against further domains. Each either confirms the existing classification or requires revision. Low priority but the methodology is established and the extractions are straightforward.

---

## VIII. LIMITATIONS AND FALSIFICATION

### 8.1 Limitations

The nine domains were selected from quantum mechanics and gauge theory. Classical domains (pipe flow, drag, capacitance from MATH-1) also contain R₂ but were not extracted because PHYS-10 scoped the framework to quantum domains. The classification applies to the tested domains, not claimed as exhaustive.

The null result applies to the specific searches conducted at the specific precisions. Larger coefficients, more complex moduli, or entirely different relationship types are untested. The search space is bounded, not exhausted.

The speculation in Section V is speculation. No computation, derivation, or verification is offered for any of the five approaches discussed. They are listed as directions that might avoid the boundary identified in Section IV, not as proposed solutions.

### 8.2 Falsification

**F1:** If a parameter reduction is found that comes FROM the framework (not from domain-specific physics expressed IN the framework), the language/theory distinction in Section IV.2 is wrong. This would mean the framework is more powerful than this paper claims.

**F2:** If the Koide midpoint is derived from a principle that generalizes to quarks (producing quark mass predictions), the lepton-specific nature stated in Section VI.1 is wrong.

**F3:** If a future modular search at the same 0.05% threshold and same 18 moduli distinguishes SM parameters from random numbers with statistical significance, the DISC-8 control test result must be revisited.

**F4:** If a Level 2 continuous parameter is derived purely from the geometric framework (R₂, R₄, the eight identities, the subgroup structure) without additional domain-specific physics input, the boundary identified in Section IV is in the wrong place.

---

## APPENDIX A: THE COMPLETE SEARCH NULL

| Search | Paper | Targets | Constants/Moduli | Transforms | Maxcoeff/Threshold | Result | Control |
|---|---|---|---|---|---|---|---|
| Linear PSLQ (stage 1) | PHYS-10 | 17 | 9 constants | None | 1,000 | All null | PSLQ internal |
| Linear PSLQ (stage 2) | PHYS-10 | 17 | 20 constants | None | 1,000 | All null | PSLQ internal |
| Linear PSLQ (stage 3) | PHYS-10 | 17 | 35 constants | None | 10,000 | All null | PSLQ internal |
| Nonlinear PSLQ | DISC-7 | 8 | 10 constants | 10 transforms | 1,000 | 80/80 null | PSLQ internal |
| Modular search | DISC-7 | 13 | 18 moduli | None | 0.05%, q≤20 | 47 SM vs 42.3 random | Formal: 13,000 randoms |
| α_s candidate | DISC-7/8 | 1 | R₂·ζ(3) | None | Specific | Killed | Control + residual PSLQ |
| α_s residual PSLQ | DISC-8 | 1 | 10 constants | None | 100/1,000/10,000 | 5/5 null | PSLQ internal |

## APPENDIX B: THE PARAMETER REDUCTION SCORECARD

| # | Parameter | Derived from | Physical principle | Framework role | Precision | Status |
|---|---|---|---|---|---|---|
| 1 | θ_QCD = 0 | Topological minimization | E(θ) = E₀−χcosθ, min at 0 | 8R₂ domain, ground state principle | Exact | **CONFIRMED** |
| 2 | m_τ | m_e, m_μ via Koide | (Σm)/(Σ√m)² = 2/3, a=√2 | C₃ phases on 8R₂ domain | 0.91σ | **CONDITIONAL** |
| 3 | α from a_e | QED series A₁-A₄ | Perturbative inversion | Q335 transcendentals in series | 4.3 ppb | **TRANSFORMATION LAW** |

Starting count: 19 SM parameters. After confirmed: 18. After conditional: 17. Phase 4 of DISC-7 and all of DISC-8 produced no additional reductions.

## APPENDIX C: SERIES PUBLICATION RECORD

| # | Paper | Registry | Key Result |
|---|---|---|---|
| 1 | MATH-1 | @HOWL-MATH-1-2026 | β = π/4 separates in 9 domains (2D) |
| 2 | MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs at 100 digits |
| 3 | MATH-3 | @HOWL-MATH-3-2026 | Extended basis: elliptic integrals, Borwein ζ(5) |
| 4 | MATH-4 | @HOWL-MATH-4-2026 | Universal 2³³⁵ basis, 22 constants |
| 5 | MATH-5 | @HOWL-MATH-5-2026 | R_n across dimensions, n=2,4 uniquely binary-native |
| 6 | PHYS-1 | @HOWL-PHYS-1-2026 | Mass as inertia (framework) |
| 7 | PHYS-2 | @HOWL-PHYS-2-2026 | Couplings run (framework) |
| 8 | PHYS-3 | @HOWL-PHYS-3-2026 | G untested at quantum scale |
| 9 | PHYS-4 | @HOWL-PHYS-4-2026 | Experimental test program |
| 10 | PHYS-5 | @HOWL-PHYS-5-2026 | α running at 0.02 ppm in exact arithmetic |
| 11 | PHYS-6 | @HOWL-PHYS-6-2026 | Confinement two-face |
| 12 | PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0 from ℤ-topology minimization |
| 13 | PHYS-8 | @HOWL-PHYS-8-2026 | m_τ from Koide, 0.91σ (conditional) |
| 14 | PHYS-9 | @HOWL-PHYS-9-2026 | α from a_e, QED series, 4.3 ppb |
| 15 | PHYS-10 | @HOWL-PHYS-10-2026 | Remainder as observable, PSLQ null |
| 16 | PHYS-11 | @HOWL-PHYS-11-2026 | 9 domains, 3 subgroups, R₂ universal |
| 17 | DISC-6 | @HOWL-DISC-6-2026 | Four-phase plan (roadmap) |
| 18 | DISC-7 | @HOWL-DISC-7-2026 | Execution: Phases 1-3 delivered, Phase 4 null |
| 19 | DISC-8 | @HOWL-DISC-8-2026 | Control test, VP closure, Koide blockage, 9 domains |
| 20 | **DISC-9** | **@HOWL-DISC-9-2026** | **The boundary: geometry determined, parameters not** |

---

**END HOWL-DISC-9-2026**

**Registry:** [@HOWL-DISC-9-2026]
**Status:** Complete (Program Capstone)
**Domain:** Methodology / Mathematical Physics
**Central Finding:** The geometric structure of physics equations (R₂, R₄, moduli, subgroups, ground state principle) is universal and determined by the form of the equations. The specific parameter values that populate this structure (couplings, masses, mixing angles) are not determined by the geometric framework. The boundary between these two — between what the mathematics determines and what the universe supplies — is the program's finding.
**Parameter Count:** 19 → 18 confirmed (θ_QCD). 18 → 17 conditional (Koide m_τ). No change from DISC-7/8.
**Methodological Contribution:** Run the control test first. Derivation beats search. The framework is a language, not a theory. Future reductions require domain-specific physics.
**The program in one sentence:** The geometry is ours; the parameters are the universe's.
