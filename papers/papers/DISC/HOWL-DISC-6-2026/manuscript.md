# The Remainder Extraction Program

## A Four-Phase Plan for SM Parameter Reduction via Exact Integer Arithmetic

**Registry:** [@HOWL-DISC-6-2026]

**Series:** Discovery

**Series Path:** [@HOWL-MATH-1-2026] → [@HOWL-MATH-4-2026] → [@HOWL-PHYS-10-2026] → [@HOWL-MATH-5-2026] → [@HOWL-DISC-6-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 31 2026

**Domain:** Research Program / Mathematical Physics / SM Parameter Reduction

**Status:** Published Plan (not results)

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

This paper publishes a research program, not results. It commits to four phases of computational work using the exact integer arithmetic framework developed in MATH-2 through MATH-5 and the remainder-as-observable principle from PHYS-10, with the goal of reducing the Standard Model free parameter count below 18.

The four phases are: extraction of concrete remainder computations from six physics domains in exact Fraction arithmetic; cross-domain unification searching for shared structure across the extracted equations; synthesis into a minimal framework of moduli, remainders, and transformation laws; and application to unmapped SM parameters using modular rather than linear search strategies.

The program builds on three established results: one confirmed parameter reduction (θ_QCD = 0, PHYS-7), one conditional reduction (m_τ from m_e and m_μ via Koide, PHYS-8, 0.91σ), and one demonstrated transformation law (α from a_e via QED series, PHYS-9, 4.3 ppb). A systematic PSLQ scan returned null for all 17 measured SM parameters against the 34-constant transcendental basis at maxcoeff 10,000, ruling out simple linear transcendental combinations and motivating the shift to modular (quotient-remainder) search strategies.

Each phase has explicit deliverables and produces publishable output regardless of subsequent phases' outcomes. Six falsification criteria are stated, including falsification of the plan itself if it is not executed. Publishing the plan before executing it ensures the methodology is documented before results can bias its description.

---

## II. WHAT HAS BEEN ESTABLISHED

### 2.1 The Foundation Papers

| Paper | Result | Status | Role in Program |
|---|---|---|---|
| MATH-2 | 17 transcendentals as exact integer pairs at 100 digits | Complete | The constants |
| MATH-4 | 22 constants over shared denominator 2³³⁵ | Complete | The arithmetic |
| MATH-5 | R_n separates in n-ball equations; n=2,4 uniquely binary-native | Complete | The geometric structure |
| PHYS-5 | α running in exact Fraction arithmetic, 0.02 ppm | Complete | RG domain partially extracted |
| PHYS-7 | θ_QCD = 0 from ℤ-topology minimization | Complete | First parameter derived |
| PHYS-8 | m_τ from m_e, m_μ via Koide formula | Complete | Second parameter (conditional) |
| PHYS-9 | α from a_e via QED series inversion, 4.3 ppb | Complete | Transformation law demonstrated |
| PHYS-10 | Remainder = observable in 6 domains; PSLQ null on SM constants | Complete | The framework and the null |

### 2.2 Parameter Reduction Status

The SM has 19 free parameters in the traditional counting (3 gauge couplings, 6 quark masses, 3 lepton masses, 3 CKM angles + 1 CP phase, Higgs mass + VEV, θ_QCD).

| Parameter | Derived From | Law | Precision | Status |
|---|---|---|---|---|
| θ_QCD = 0 | None (topological) | E(θ) = E₀ − χ cos(θ), minimum at θ=0 | Exact | **CONFIRMED** |
| m_τ | m_e, m_μ | Koide: (Σm)/(Σ√m)² = 2/3 | 0.91σ | **CONDITIONAL** |
| α from a_e | a_e (one measurement) | QED series A₁–A₄ (integers + transcendentals) | 4.3 ppb | **TRANSFORMATION LAW** |

Confirmed reductions: 19 → 18 (θ_QCD).

Conditional: 18 → 17 (m_τ via Koide, pending deeper derivation of the 2/3 condition).

The α derivation from a_e is not a parameter reduction — it replaces one measured input with another. Its value is demonstrating that the QED series (integers + MATH-4 transcendentals) connects the two, with the transformation law entirely in exact rational arithmetic.

### 2.3 The PSLQ Null

A systematic PSLQ scan tested 20 measured SM dimensionless quantities against the 34-constant transcendental basis (22 from MATH-4 plus 12 extended constants including ζ(7), ζ(9), Li₅–Li₇, elliptic integrals K and E at three arguments, and ln(7)). Three stages: 9-constant pool at maxcoeff 1,000; 20-constant pool at maxcoeff 1,000; full 35-constant pool at maxcoeff 10,000.

Result: all null. No measured SM parameter is a rational linear combination of the transcendental basis with small integer coefficients.

A focused scan on the strongest near-miss (α⁻¹ mod ζ(3) = 114 + 0.00126, where 114 = 2×3×19) ran PSLQ on the residual α⁻¹ − 114ζ(3) = 0.001512 against the full basis at maxcoeff 10,000. Result: null. The residual has no structure in the transcendental basis.

The null constrains the search: if SM parameters connect to the mathematical basis, the connection is not linear. The remainder framework (PHYS-10) proposes modular relationships — quotient plus remainder with a physically determined modulus — as the alternative search space. This has not been tested systematically.

### 2.4 The Extended Basis Status

The MATH-4 basis contains 22 constants at 100 digits over 2³³⁵. The extended basis (computed during this research program) contains 34 constants at 100 digits, plus Cl₂(π/3) at approximately 9 digits (blocked by slow convergence of the direct series, solvable by Bernoulli number acceleration but not yet implemented). The 34 verified constants cover everything needed for QED through 4-loop. Phase 1 may require additional constants not currently in the basis (lattice-specific parameters for Brillouin zone, Bernoulli numbers for Bohr-Sommerfeld). These will be added as needed following the MATH-2/MATH-4 methodology.

### 2.5 Known Blockages from Prior Work

Working notebooks from this research program identified specific blockages for Phase 4 targets:

| Target | Blockage | Source |
|---|---|---|
| sin²θ_W | The RG formula sin²θ_W = 3/8 − (109/72π)α ln(M_Z/M_GUT) has one free parameter (M_GUT) not determined by SM physics alone | sin²θ_W analysis notebook |
| Quark mass ratios | Koide formula fails for quarks. The Koide angle a ≠ √2 for quark triples. Proven structural, not fixable by scale choice | Quark Koide notebook |
| m_μ/m_e | No derivation path identified. Koide gives m_τ from (m_e, m_μ) but does not constrain the ratio itself | Lepton mass analysis |
| V_us (Cabibbo angle) | The relation sin θ_C ≈ √(m_d/m_s) holds at ~0.75% but quark mass uncertainties are ~10%, preventing a clean test | CKS mining DB analysis |

These blockages are stated honestly. They inform which Phase 4 targets are realistic versus aspirational.

---

## III. PHASE 1: DOMAIN EXTRACTION

### 3.1 Goal

For each of the six PHYS-10 domains, compute a concrete example in exact Fraction arithmetic, extracting the integer quotient and fractional remainder explicitly, and producing a verification script where every `assert` passes.

### 3.2 The Six Extractions

| # | Domain | Concrete Example | Integer Part | Remainder | Modulus | Difficulty |
|---|---|---|---|---|---|---|
| 1 | Theta vacuum | E(θ) = E₀ − χ cos(θ), minimum at θ=0 | Instanton number ν | θ mod 2π = 0 | 2π | **Done** (PHYS-7) |
| 2 | RG running | α⁻¹(μ) through lepton thresholds | Number of active flavors | Accumulated running between thresholds | Mass thresholds | **Mostly done** (PHYS-5, PHYS-9) |
| 3 | Bohr-Sommerfeld | Harmonic oscillator: ∮p·dq = 2πℏ(n + ½) | Quantum number n | Maslov correction ½ | 2πℏ | Straightforward |
| 4 | Berry phase | Spin-½ in rotating B field: γ = π(1 − cosθ) | Winding number | γ mod 2π | 2π | Straightforward |
| 5 | Brillouin zone | 1D tight-binding: E(k) = −2t cos(ka) | Zone index | k mod (2π/a) | 2π/a | Medium |
| 6 | Chern-Simons | U(1) CS on S³: level k, invariant CS mod ℤ | Chern number | Fractional CS | 1 | Hard |

### 3.3 Deliverables for Each Extraction

For each domain:

(a) The equation in standard form.

(b) The equation decomposed into integer quotient + remainder.

(c) A Fraction arithmetic computation of a specific numerical example with stated parameters.

(d) Verification against known analytical or numerical results.

(e) Identification of where R_n (the geometric remainder from MATH-5) appears, if it does.

(f) A Python script with `assert`-verified exact identities. This is non-negotiable — it is the standard maintained throughout the series.

### 3.4 Extraction Order

Start with the completed or near-completed domains: theta vacuum (PHYS-7), RG running (PHYS-5/9). Then the straightforward computations: Bohr-Sommerfeld (textbook integrals in Fraction arithmetic), Berry phase (spin-½ system, rational trigonometry). Then the medium-difficulty: Brillouin zone (requires setting up a lattice Hamiltonian as Fractions, computing band structure). Chern-Simons last (requires the most mathematical machinery and the most careful treatment of gauge invariance in discrete arithmetic).

### 3.5 Phase 1 Deliverable

A unified extraction table with one row per domain:

| Domain | Equation | Modulus | Integer Part | Remainder | R_n Content | Script | Status |
|---|---|---|---|---|---|---|---|
| (filled per extraction) | | | | | | | |

This table, backed by six verification scripts, replaces the descriptive PHYS-10 tables with computed, verified entries. It is the data foundation for Phase 2.

### 3.6 Operational Rule

Each extraction must be reviewed and verified before the next begins. No skipping ahead. Each script must run cleanly with all `assert` passing before the extraction is considered complete. This discipline is what makes the program credible — every claim has a script, every script has assertions, every assertion passes.

---

## IV. PHASE 2: CROSS-DOMAIN UNIFICATION

### 4.1 Goal

Search the Phase 1 extracted equations for shared structure across domains that goes beyond what PHYS-10 already states. Produce a cross-domain connection table with verified hits and honest nulls.

### 4.2 Specific Questions

| # | Question | Domains | Method | Prior Knowledge |
|---|---|---|---|---|
| 1 | Can the known Maslov-Berry connection (Robbins 1991, Littlejohn 1992) be expressed as an exact Fraction identity in Q335? | Bohr-Sommerfeld ↔ Berry phase | Compute both for the same system (charged particle in magnetic field) in Fraction arithmetic. Compare the Maslov index to Berry phase / π | The connection is established physics. The task is computing it in exact arithmetic, not discovering it |
| 2 | Does the Brillouin zone boundary share structure with the RG threshold? | Brillouin zone ↔ RG running | Compare the remainder jump at a BZ boundary with the remainder jump at a mass threshold. Same functional form? | Structural parallel noted in PHYS-10 but not computed |
| 3 | Does R₂ appear in the Berry phase formula? | Berry phase ↔ MATH-5 | Berry phase involves integration over S². Area of S² = 4πr² = 16R₂r². Check if R₂ separates in the Berry phase expression | Plausible — the 2-sphere surface area contains R₂ |
| 4 | Does R₄ appear throughout the Chern-Simons computation? | Chern-Simons ↔ MATH-5 | The CS normalization 1/(8π²) = 1/(256R₄) is established (MATH-5). Extract the full CS computation and verify R₄ appears at every step | Partially established in MATH-5 |
| 5 | Is the VP running (PHYS-5) a specific instance of Brillouin zone band structure? | RG running ↔ Brillouin zone | Formalize both as "quantity accumulating modularly with discrete jumps at boundaries." Compare mathematical structure | Strongest candidate for a real finding — we already have VP running in exact arithmetic |
| 6 | Does the θ_QCD = 0 minimization have an analog in the Brillouin zone? | Theta vacuum ↔ Brillouin zone | Both have energy as a periodic function of a parameter. Compare: E(θ) = E₀ − χ cos(θ) vs E(k) = −2t cos(ka). Both minimized at the parameter = 0 | Structural parallel — both are cosine potentials minimized at zero |

### 4.3 Deliverable

A cross-domain connection table. For each pair of domains tested:

| Domains | Connection Found? | What Is It? | Verified Computationally? | Script Reference |
|---|---|---|---|---|
| (filled per question) | YES/NULL | (description) | (status) | (script name) |

Null results are published as nulls. They are as valuable as hits — each null rules out a class of unification and constrains the synthesis in Phase 3.

---

## V. PHASE 3: SYNTHESIS

### 5.1 Goal

Combine the Phase 1 extractions and Phase 2 connections into a minimal framework. Answer the central question: what is the minimal set of {moduli, remainders, transformation laws} that generates all the extracted equations?

### 5.2 Three Possible Outcomes

**(a) Collapse.** All six domains reduce to instances of a single principle with domain-specific moduli. For example: every physical quantity is a phase accumulated on a periodic domain, the integer part is the winding number, and the remainder is the observable. Berry phase, Brillouin zone momentum, Bohr-Sommerfeld action, CS invariant, coupling running, and vacuum angle are all the same mathematical object with different physical interpretations. If this is the case, the synthesis paper states the principle and demonstrates all six domains as instances.

**(b) Partial collapse.** Some domains share deep structure, others are independent. For example: Berry phase, Bohr-Sommerfeld, and theta vacuum might share "phase on a circle" structure; Brillouin zone and RG running might share "accumulation with threshold jumps"; Chern-Simons might be an independent "topological invariant mod ℤ." Three subgroups, not one principle. The synthesis states the subgroup structure and identifies what distinguishes the subgroups.

**(c) No collapse.** The six domains remain six independent instances of the general quotient-remainder pattern, with no deeper structural connection beyond PHYS-10's observation. The synthesis reports this honestly. The PHYS-10 framework (remainder = observable) is the deepest available statement.

### 5.3 Deliverable

A single paper stating whichever of (a), (b), or (c) the evidence supports, including: the complete Phase 1 extraction table, the Phase 2 connection table, and the synthesis result. All supported by verification scripts.

---

## VI. PHASE 4: PARAMETER REDUCTION

### 6.1 Goal

Use the complete remainder framework to attack the remaining SM free parameters. Current confirmed count: 18 (after θ_QCD). Target: reduce below 18.

### 6.2 Search Strategy

The PSLQ null rules out linear transcendental combinations with small coefficients. Phase 4 uses two alternative strategies:

**Strategy A — Nonlinear PSLQ.** Test transformed targets: log(X), X², 1/X, X^(1/2), X^(1/3) for each measured parameter X, against the 34-constant basis. This was identified as a gap in the current search and has not been executed. It must be done before concluding the search space is exhausted.

**Strategy B — Modular search.** For each parameter, search for moduli M such that X mod M produces a clean quotient-remainder split with the remainder being a simple fraction or a small combination of basis constants. This is the remainder framework applied as a computational search, not just an observational principle. The moduli to test include: single basis constants, products of two basis constants, R_n values, and domain-specific moduli identified in Phase 1.

### 6.3 Priority Targets (with Honest Blockage Assessment)

| Parameter | Priority | Candidate Mechanism | Known Blockage | Realistic? |
|---|---|---|---|---|
| sin²θ_W | High | RG running from GUT scale; remainder of 3/8 after running | M_GUT is a free parameter not determined by SM alone | Medium — requires assumption about GUT scale or a way to eliminate it |
| m_μ/m_e | High | Unknown — Koide constrains m_τ from (m_e, m_μ) but not the ratio itself | No derivation path identified | Low without new idea |
| Quark mass ratios | Medium | Koide-type relations for heavy quarks (c, b, t) | Koide fails for light quarks (u, d, s). a ≠ √2 for quarks | Medium for heavy quarks, blocked for light |
| V_us (Cabibbo) | Medium | CKM phases as geometric phases on a circle; unitarity constraints | sin θ_C ≈ √(m_d/m_s) at 0.75% but 10% quark mass uncertainty | Low without better quark masses |
| Higgs mass / VEV | Low | No candidate mechanism identified | No structural lead from this program | Aspirational only |

### 6.4 What Success Looks Like

A parameter reduction takes the form: "Parameter X = f(parameters already known), where f is a transformation law expressed entirely in integers and Q335 transcendentals, derived from a physical principle (symmetry, quantization, minimization, or transformation law), matching measurement within experimental uncertainty."

The transformation law must be derived, not fitted. The physical principle must be stated. The prediction must be verified numerically. The computation must be in exact Fraction arithmetic with a verification script.

### 6.5 What Failure Looks Like

If after completing Phases 1-3, no new parameter reduction is found in Phase 4, the program reports this as a null. The null means: the SM parameters not yet derived are not connected to the transcendental basis through the modular arithmetic framework with the identified moduli and transformation laws. They are either truly independent initial conditions or connected through a mechanism not captured by this framework.

### 6.6 Honest Probability Assessment

Phase 1 will succeed — it is computational work on known physics with known equations.

Phase 2 will produce some connections and some nulls — both are useful and publishable.

Phase 3 will produce one of three outcomes (a), (b), or (c) — all publishable.

Phase 4 is high-risk. The probability of reducing even one more parameter is uncertain. The three existing reductions used specific mechanisms (topological minimization, Koide formula, QED series inversion) that may not generalize. The nonlinear PSLQ scan (Strategy A) is the most likely to produce a result if one exists, because it covers a search space not yet tested. The modular search (Strategy B) is more speculative. The remainder framework provides a new search strategy but new strategies do not guarantee new results.

The program is designed so that Phases 1-3 produce valuable results regardless of Phase 4's outcome. Phase 4 is the reach goal. The foundation is the contribution even if the reach fails.

---

## VII. FALSIFICATION CRITERIA

**F1 (Phase 1).** If any of the six domain extractions cannot be completed in exact Fraction arithmetic — if the equations resist rational representation or the verification scripts fail — that domain is flagged as incompatible with the framework. Each domain is independent; one failure does not invalidate the others.

**F2 (Phase 2).** If no cross-domain connection is found beyond what PHYS-10 already states — if all six questions in Section IV return null — Phase 2 has not advanced the framework. This is reported honestly as a null.

**F3 (Phase 3).** If the synthesis reduces to outcome (c) — no collapse, six independent domains — the framework is descriptive but not explanatory. This is a valid result but a weaker one than outcomes (a) or (b).

**F4 (Phase 4).** If no new SM parameter is reduced after Phases 1-3 are complete and both search strategies (nonlinear PSLQ and modular search) have been executed, the parameter reduction program has not delivered on its primary goal. The framework and infrastructure remain valid but the application has failed.

**F5 (Timeline).** The timeline for execution is to be determined by the research schedule and will be published as an addendum when Phase 1 begins. A plan without execution is a wish, not a commitment. This criterion exists to ensure the plan is followed through.

**F6 (The plan itself).** This paper is a published commitment. If the plan is not executed — if the scripts are not written, the extractions not performed, the results not published — then DISC-6 is falsified as a commitment. Publishing a plan and not following through is worse than not publishing the plan. This is the hardest criterion and the most important.

---

## VIII. CONNECTION TO THE SERIES

| Phase | Produces | Depends On |
|---|---|---|
| Phase 1 (Extraction) | PHYS paper: six domain extractions with scripts | MATH-4 (Q335), PHYS-10 (framework) |
| Phase 2 (Unification) | PHYS paper: cross-domain connection table | Phase 1, MATH-5 (R_n) |
| Phase 3 (Synthesis) | PHYS paper: minimal framework or null | Phase 2, all prior PHYS |
| Phase 4 (Parameters) | PHYS paper(s): reductions or null | Phase 3, PHYS-7/8/9 |

Each phase produces at least one publishable paper regardless of outcome. Null results are published as nulls. Failure at Phase 4 does not invalidate Phases 1-3. The program is structured so that each phase stands on its own.

---

## IX. LIMITATIONS

This is a plan, not a result. Plans can be wrong, incomplete, or impossible to execute.

The specific questions in Phase 2 may be the wrong questions. Better questions may emerge during Phase 1. The plan allows for this — Phase 2 questions are stated as "specific questions to test," not as the only questions worth testing.

The synthesis in Phase 3 may not converge. If the six domains resist unification, the synthesis reports this and the program continues to Phase 4 with a weaker but still functional framework.

The parameter targets in Phase 4 are constrained by known blockages (Section II.5). The program may not produce any new reductions. This possibility is stated in advance so that a null in Phase 4 is a reported result, not a hidden failure.

The extended basis (34 constants) may be insufficient for some domain extractions. Additional constants will be computed as needed using the MATH-2/MATH-4 methodology. The basis is extensible by construction.

The operational rule — verify each phase before starting the next — may slow the program. This is intentional. Speed without verification produces unreliable results. The series maintains exact arithmetic with script-backed assertions throughout, and this standard is not relaxed for any phase of the program.

---

## APPENDIX A: SERIES PUBLICATION RECORD

| Paper | Registry | Key Result | Role in DISC-6 |
|---|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = π/4 separates in 9 domains (2D) | Foundation: 2D geometric invariant |
| MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs | Foundation: the constants |
| MATH-3 | @HOWL-MATH-3-2026 | Extended basis: elliptic integrals + Borwein ζ(5) | Foundation: higher-loop constants |
| MATH-4 | @HOWL-MATH-4-2026 | Universal 2³³⁵ basis: 22 constants, shared denominator | Foundation: the arithmetic |
| MATH-5 | @HOWL-MATH-5-2026 | R_n separates across dimensions; n=2,4 unique | Foundation: geometric structure |
| PHYS-5 | @HOWL-PHYS-5-2026 | α running in exact arithmetic, 0.02 ppm | Phase 1: RG domain (partial) |
| PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0 from ℤ-topology | Phase 1: theta vacuum (complete) |
| PHYS-8 | @HOWL-PHYS-8-2026 | m_τ from Koide, 0.91σ | Parameter reduction (conditional) |
| PHYS-9 | @HOWL-PHYS-9-2026 | α from a_e, QED series, 4.3 ppb | Transformation law demonstrated |
| PHYS-10 | @HOWL-PHYS-10-2026 | Remainder = observable; PSLQ null | Framework and null result |
| **DISC-6** | **@HOWL-DISC-6-2026** | **This plan** | **The program** |

---

**END HOWL-DISC-6-2026**

**Registry:** [@HOWL-DISC-6-2026]
**Status:** Published Plan
**Domain:** Research Program / Mathematical Physics
**Central Commitment:** Four-phase program — extraction, unification, synthesis, parameter reduction — using exact integer arithmetic and the remainder-as-observable framework to attack SM free parameters
**Current Score:** 1 confirmed reduction (θ_QCD), 1 conditional (m_τ), 1 transformation law (α from a_e), 17 measured parameters remaining after confirmed reduction
**What It Commits To:** Six domain extractions with verification scripts (Phase 1), six cross-domain questions tested (Phase 2), synthesis into minimal framework (Phase 3), nonlinear PSLQ and modular search on SM parameters (Phase 4)
**What It Does NOT Commit To:** Specific results in Phase 4. The program is designed to produce valuable output even if parameter reduction fails.
**Falsification:** Six criteria including F6 — the plan itself is falsified if not executed
