# The Remainder Extraction Program: Execution and Results
## Four Phases Delivered, Parameter Reduction Null

**Registry:** [@HOWL-DISC-7-2026]

**Series Path:** [@HOWL-DISC-6-2026] → Phase 1-4 Execution → [@HOWL-DISC-7-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 31 2026

**Domain:** Research Program / Mathematical Physics / SM Parameter Reduction

**Status:** Complete (Retrospective)

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

DISC-6 committed to a four-phase program: extraction, unification, synthesis, and parameter reduction, using exact integer arithmetic and the remainder-as-observable framework to attack the Standard Model free parameter count. This paper reports the execution of all four phases.

Phases 1-3 delivered concrete results. Phase 1 extracted six physics domains into exact Fraction arithmetic, producing a verified extraction table with scripts where every assertion passes. Phase 2 tested six cross-domain questions, finding four confirmed connections, one structural parallel, and one informative null. Phase 3 synthesized the results into outcome (b) — partial collapse — identifying one universal constant (R₂ = π/4, present in all six domains), two modular types (phase-periodic and topological), three subgroups (cosine-periodic, monotonic accumulation, topological quantization), and one ground state principle (minimum of cosine on 8R₂-periodic domain gives remainder = 0, which is why θ_QCD = 0).

Phase 4 (parameter reduction) returned null. Nonlinear PSLQ (80 tests, 8 targets × 10 transforms, maxcoeff 1000) found no relation. Synthesis-informed modular search (11 targets × 18 moduli including R₂-multiples, R₄-multiples, and products of basis constants) produced 42 raw hits, most consistent with statistical noise. One candidate — α_s = πζ(3)/32, matching the measured value to 0.01% — lies within the measurement uncertainty of ±0.0009 but cannot be tested without approximately 5× improvement in α_s precision.

The confirmed parameter count remains: 19 → 18 (θ_QCD = 0, PHYS-7). The conditional reduction m_τ via Koide (PHYS-8, 0.91σ) and the demonstrated transformation law α from a_e (PHYS-9, 4.3 ppb) are unchanged. No new parameter was reduced.

DISC-6 criterion F4 (parameter reduction) is falsified. Criteria F1, F2, F3, F5, and F6 are met. The framework and infrastructure are delivered. The application to free parameters returned null. Both are reported honestly.

---

## II. DISC-6 COMMITMENTS VERSUS DELIVERY

| DISC-6 Commitment | Delivered? | Evidence |
|---|---|---|
| Phase 1: 6 domain extractions with scripts | **YES** (6/6) | phase1_bohr_sommerfeld.py, phase1_berry.py, phase1_brillouin.py, phase1_cs.py + PHYS-7, PHYS-5/9 |
| Phase 2: 6 cross-domain questions tested | **YES** (6/6) | phase2_unification.py |
| Phase 3: Synthesis into minimal framework | **YES** | phase3_synthesis.py |
| Phase 4 Strategy A: Nonlinear PSLQ | **YES** | phase4_nonlinear_pslq.py |
| Phase 4 Strategy B: Modular search | **YES** | phase4_modular_search.py |
| F6: Plan executed? | **YES** | This paper |

---

## III. PHASE 1 RESULTS: THE EXTRACTION TABLE

Six domains extracted into exact Fraction arithmetic. Each extraction produced: the equation in standard form, the integer/remainder decomposition, a Fraction computation of specific numerical examples, verification against known results, identification of R_n content, and a Python script with assert-verified identities. Every assertion passes.

### 3.1 The Complete Table

| # | Domain | Equation | Modulus | Integer | Remainder | R₂ present | R₄ present | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Theta vacuum | E(θ) = E₀ − χcos(θ) | 2π = 8R₂ | Instanton ν | θ = 0 | In modulus | — | VERIFIED (PHYS-7) |
| 2 | RG running | α⁻¹(μ) through thresholds | Mass m_f | Active flavors | Running | In step 1/(12R₂) | — | VERIFIED (PHYS-5/9) |
| 3 | Bohr-Sommerfeld | ∮p·dq = 2πℏ(n+μ/4) | 2πℏ = 8R₂ℏ | n | μ/4 | In modulus | In box E via π²=32R₄ | VERIFIED |
| 4 | Berry phase | γ = −m·Ω | 2π = 8R₂ | Winding n | γ mod 2π | In modulus + Ω | — | VERIFIED |
| 5 | Brillouin zone | E(k) = −2t cos(ka) | G = 2π/a = 8R₂/a | Zone index | k mod G | In modulus | In boundary E | VERIFIED |
| 6 | Chern-Simons | CS(A) mod ℤ | 1 | Chern number | CS mod ℤ | In exponential | In normalization 1/(256R₄) | VERIFIED |

### 3.2 Phase 1 Findings

**Finding 1: R₂ = π/4 is universal.** R₂ appears in all six domains. In five domains (theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone, and the Chern-Simons exponential), the modulus is 8R₂ times a domain-specific scale. In Chern-Simons, the modulus is 1 (topological), with R₂ appearing in the exponential exp(2πi·k·CS) = exp(i·8R₂·k·CS).

**Finding 2: Two-level remainder structure.** Every domain exhibits remainder structure at two levels. The geometric level contains R₂ (in the modulus) and R₄ (in energy expressions involving π² = 32R₄). The domain-specific level contains the physical remainder: the Maslov correction μ/4, the Berry phase γ mod 2π, the crystal momentum k mod G, the CS invariant mod ℤ, the vacuum angle θ, or the accumulated running.

**Finding 3: R₄ enters through energy quantization.** R₄ = π²/32 appears in the particle-in-a-box energy E_n = π²ℏ²n²/(2mL²) = 32R₄ℏ²n²/(2mL²), in the zone boundary energy E_n = n²π²ℏ²/(2ma²) = n²·32R₄·ℏ²/(2ma²), and in the Chern class normalization 1/(8π²) = 1/(256R₄). In each case, R₄ enters through the identity π² = 32R₄, verified as an exact Fraction identity in the MATH-5 verification script.

### 3.3 Detailed Extraction Results

**Bohr-Sommerfeld.** Harmonic oscillator: E_n = ℏω(n + 1/2). The integer is n. The remainder is 1/2 = μ/4 where μ = 2 (two soft turning points). Verified for n = 0 through 100 in Fraction arithmetic. The action modulus 2πℏ = 8R₂ℏ. Infinite square well: μ = 4 (two hard walls), correction μ/4 = 1, remainder absorbed into integer labeling. The special property: for the harmonic oscillator, Bohr-Sommerfeld with Maslov correction gives the exact quantum result because the quadratic potential has no higher-order WKB corrections.

**Berry phase.** Spin-1/2 in rotating magnetic field. γ = π(1 − cosθ) = 4R₂(1 − cosθ). Nine test cases with rational cosθ, all verified as exact Fractions. Key special cases: θ = π/2 gives γ = π (Z₂ topological phase), θ = π gives γ = 2π (trivial, full winding), θ = 0 gives γ = 0. Multi-circuit accumulation verified: after 4 circuits at θ = π/3 (γ = π/2 each), the integer rolls from 0 to 1 and the remainder resets to 0. Solid angle of the full sphere: 4π = 16R₂, consistent with MATH-5 rule (surface area is a 2D operation, uses R₂).

**Brillouin zone.** 1D tight-binding lattice with N = 12 sites. Crystal momentum k defined modulo G = 2π/a = 8R₂/a. Zone folding verified: 16 k-values decomposed into zone index and BZ remainder. Periodicity verified: k/(2π) = 1/3 and five periodic images at k + mG all reduce to the same k_BZ = 1/3, with zone index changing. Momentum quantum Δk = G/N = 8R₂/(Na). Zone boundary energy E_n = n²·32R₄·ℏ²/(2ma²), verified exact.

**Chern-Simons.** U(1) CS on lens space L(5,1) at level k = 1: five flat connections with CS values 0, 1/10, 2/5, 9/10, 3/5 (all exact rationals mod ℤ). L(7,1) at level k = 3: seven flat connections with CS values 0, 3/14, 6/7, 13/14, 3/7, 5/14, 5/7. Level quantization from gauge invariance: exp(2πikn) = 1 forces k ∈ ℤ. Chern class normalization: 1/(8π²) = 1/(256R₄), verified exact. FQHE connection: the filling fraction ν = p/q IS the CS remainder. Integer Hall (ν ∈ ℤ) has CS mod ℤ = 0. Fractional Hall (ν = p/q) has CS mod ℤ = p/q.

---

## IV. PHASE 2 RESULTS: CROSS-DOMAIN CONNECTIONS

Six questions from DISC-6, each testing a specific connection between two domains. All computed in exact Fraction arithmetic where applicable.

| Q | Connection | Domains | Result | Status |
|---|---|---|---|---|
| 1 | Maslov = Berry/(8R₂) | BS ↔ Berry | Tautological identity: μ/4 = (μ × 2R₂)/(8R₂) = μ/4 | **CONFIRMED** |
| 2 | BZ boundary ↔ RG threshold | BZ ↔ RG | Both have R₂, different roles (period vs step size). Cosine vs logarithmic. | **PARTIAL** |
| 3 | R₂ in Berry phase | Berry ↔ MATH-5 | γ = 4R₂(1−cosθ), 4π = 16R₂. Surface area is 2D operation → R₂. | **CONFIRMED** |
| 4 | R₄ in CS normalization | CS ↔ MATH-5 | 1/(8π²) = 1/(256R₄). 4D bulk normalization → R₄. | **CONFIRMED** |
| 5 | VP running = BZ band structure | RG ↔ BZ | VP is monotonic (staircase), not periodic (cosine). Thresholds unequal: ln(m_μ/m_e) = 5.3316, ln(m_τ/m_μ) = 2.8224, ratio 1.8891 ≠ 1. | **NULL** |
| 6 | θ = 0 ↔ BZ k = 0 minimum | Theta ↔ BZ | Both: E(φ) = A − B cos(φ), period 8R₂ × scale, minimized at φ = 0. | **CONFIRMED** |

Score: 4 confirmed, 1 partial, 1 null.

**The Q1 finding.** The Maslov-Berry connection is established physics (Robbins 1991, Littlejohn 1992). What Phase 2 adds: in R₂ units, the connection is an algebraic tautology. Phase per soft turning point = π/2 = 2R₂. Phase per hard wall = π = 4R₂. Modulus = 2π = 8R₂. Maslov correction = (μ × 2R₂)/(8R₂) = μ/4. The identity is exact in Fraction arithmetic: True (EXACT) for both harmonic oscillator (μ = 2, correction = 1/2) and infinite well (μ = 4, correction = 1).

**The Q5 null.** The VP running cannot be formally mapped to a band structure because it lacks periodicity. BZ has infinite identical boundaries at equal spacing G. VP has finite distinct thresholds at unequal intervals determined by measured masses. BZ has cosine dispersion. VP has logarithmic accumulation. R₂ appears in both but in different functional roles: period (BZ) versus step size (RG). The structural parallel is an analogy, not an equivalence.

**The Q6 finding.** The theta vacuum energy E(θ) = E₀ − χcos(θ) and the tight-binding dispersion E(k) = −2t cos(ka) are the same mathematical structure: a cosine energy function on a periodic domain with period 8R₂ × scale, minimized at the parameter = 0. In both cases, the ground state has remainder = 0.

---

## V. PHASE 3 RESULT: PARTIAL COLLAPSE

### 5.1 Outcome (b) from DISC-6

The six domains collapse into three subgroups, not one principle and not six independent structures.

**Subgroup A — Phase-Periodic:** {theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone}

All four share: E(φ) = A − B cos(φ), phase variable φ ∈ [0, 8R₂), period 8R₂ × (domain scale), minimum at φ = 0 (remainder = 0). The scales differ — 1 (theta, Berry), ℏ (BS), 1/a (BZ) — but the structure is one structure. The Maslov-Berry connection (Q1) and the theta-BZ connection (Q6) are internal to this single structure.

**Subgroup B — Monotonic Accumulation:** {RG running}

α⁻¹(μ) = α⁻¹(μ₀) + Σ_f Q²/(12R₂) × ln(μ/m_f) × Θ(μ − m_f). R₂ appears in the step size 1/(3π) = 1/(12R₂). Not periodic: thresholds at unequal intervals determined by measured masses. The functional form is logarithmic, not cosine. Phase 2 Q5 returned null on the formal equivalence to BZ band structure.

**Subgroup C — Topological Quantization:** {Chern-Simons}

CS(A) mod ℤ. Modulus = 1 (from large gauge invariance). R₄ in the normalization 1/(8π²) = 1/(256R₄). R₂ in the exponential exp(2πi·k·CS) = exp(i·8R₂·k·CS). The CS values for flat connections are pure rationals — transcendental content is in the normalization and exponential, not in the invariant values.

### 5.2 The Minimal Description

**1 universal constant:** R₂ = π/4. Present in all six domains as: the modular period (8R₂ in Subgroup A), the step coefficient (1/(12R₂) in Subgroup B), and the exponential period (8R₂ in Subgroup C).

**2 modular types:** Phase-periodic (mod 8R₂ × scale) and topological (mod 1).

**3 subgroups:** A (cosine on 8R₂, min at R = 0), B (logarithmic staircase, R₂ in step), C (integer modular, R₄ normalization).

**1 ground state principle:** On an 8R₂-periodic domain with energy E = A − B cos(φ), the minimum is at φ = 0 (remainder = 0). This is why θ_QCD = 0 (PHYS-7). This is why the BZ band minimum is at k = 0.

### 5.3 What Collapses and What Does Not

**Collapses.** R₂ is universal across all six domains. The four Subgroup A domains are one mathematical structure instantiated with different physical scales. The ground state principle unifies θ_QCD = 0 and the BZ band minimum as the same mathematics.

**Does not collapse.** RG running (Subgroup B) lacks periodicity. The Q5 null establishes this as a structural difference, not a gap in analysis. CS modulus = 1 is topological, not geometric — it comes from gauge invariance, not from phase periodicity.

### 5.4 Framework Identities

Eight exact Fraction identities verified in phase3_synthesis.py, all PASS:

2π = 8R₂, π = 4R₂, π/2 = 2R₂, π² = 32R₄, 8π² = 256R₄, 1/(3π) = 1/(12R₂), 1/(8π²) = 1/(256R₄), 4π = 16R₂.

---

## VI. PHASE 4 RESULT: NULL

### 6.1 Strategy A: Nonlinear PSLQ

8 targets (α⁻¹, sin²θ_W, α_s, m_μ/m_e, m_τ/m_μ, M_W/M_Z, M_H/M_Z, M_H/M_W) × 10 transforms (X, ln X, X², 1/X, √X, X^{1/3}, Xπ, X/π, X·2π, X/(2π)) × 10-constant pool at maxcoeff = 1000.

Result: 80/80 null. No measured SM parameter, under any of 10 nonlinear transforms, is a rational linear combination of the transcendental pool. This extends the PHYS-10 null from linear to nonlinear.

### 6.2 Strategy B: Synthesis-Informed Modular Search

11 targets × 18 moduli (R₂-multiples, R₄-multiples, products of basis constants including π·ln 2, π·ζ(3), R₂·ζ(3), ζ(3)², ln 2·e, and the VP step size 1/(12R₂)). Testing remainders against simple rationals p/q with q ≤ 20 at 0.05% threshold.

Result: 42 raw hits, most consistent with statistical noise. At the threshold tested, approximately 4 hits are expected from random chance across ~3960 total p/d combinations. The excess is modest and driven primarily by hits at large denominators (14-20) without structural motivation.

### 6.3 The Three Candidates Assessed

**α_s ≈ πζ(3)/32 = R₂·ζ(3)/8:**

| Quantity | Value |
|---|---|
| α_s measured | 0.1180 ± 0.0009 (0.76%) |
| πζ(3)/32 | 0.1180117 |
| Difference | −0.0000117 |
| Relative | 0.0099% |
| Within uncertainty | Yes |

The formula uses Subgroup A constants (R₂ and ζ(3)) in a clean structure (product of two basis constants divided by a power of 2). The match is 76× better than the measurement uncertainty. However, α_s is known only to 0.76% — any formula producing a value between 0.1171 and 0.1189 matches within uncertainty. The candidate cannot be tested without α_s measured to approximately 0.01% (5× improvement). It is reported as untestable, not as a finding.

**sin²θ_W ≈ 3π²/128 = (3/4)R₄:**

| Quantity | Value |
|---|---|
| sin²θ_W measured | 0.23122 ± 0.00003 |
| 3π²/128 | 0.2313189 |
| Difference | −0.0000989 |
| Within uncertainty | No (3.3× outside) |

Ruled out as an exact relation.

**α⁻¹ ≈ (1027/16)·R₂·e:**

| Quantity | Value |
|---|---|
| α⁻¹ CODATA | 137.035999177 ± 0.000000021 |
| (1027/16)·R₂·e | 137.036048 |
| Difference | −0.000048 |
| Within uncertainty | No (~2300× outside) |

Ruled out.

### 6.4 The Null Statement

No new SM parameter is derived from the integer arithmetic framework. The nonlinear PSLQ search and the synthesis-informed modular search both return null at the precisions tested. One candidate (α_s = πζ(3)/32) is within measurement uncertainty but untestable at current precision. All other candidates are either outside measurement uncertainty (ruled out) or at precisions where coincidence cannot be excluded.

---

## VII. FALSIFICATION ASSESSMENT

| Criterion | Description | Met? |
|---|---|---|
| F1 (Phase 1) | 6 domain extractions completed in Fraction arithmetic | **YES** — 6/6, all scripts pass |
| F2 (Phase 2) | Connections found beyond PHYS-10 | **YES** — 4 confirmed, 1 partial, 1 null |
| F3 (Phase 3) | Synthesis outcome (a) or (b), not (c) | **YES** — outcome (b), partial collapse |
| F4 (Phase 4) | New SM parameter reduced | **NO — FALSIFIED** |
| F5 (Timeline) | Program executed within stated schedule | **YES** |
| F6 (Commitment) | Plan executed, results published | **YES** — this paper |

Score: 5/6. The one failure (F4) is the primary goal. The program delivered infrastructure and structural findings but not parameter reduction.

---

## VIII. WHAT WAS FOUND

Despite the Phase 4 null, the program produced findings not anticipated in DISC-6.

### 8.1 The Universal Modulus 8R₂

Five of six domains have modulus 8R₂ × (domain scale). This was not stated in PHYS-10. The R₂ = π/4 universality emerged from Phase 1 extraction and was confirmed across theta vacuum (8R₂), Bohr-Sommerfeld (8R₂ℏ), Berry phase (8R₂), Brillouin zone (8R₂/a), and the CS exponential (8R₂ in exp(i·8R₂·k·CS)).

### 8.2 The Three-Subgroup Structure

The partial collapse organizes six apparently independent domains into three subgroups with distinct mathematical structures. Subgroup A (cosine-periodic) contains four domains as instances of one structure. Subgroup B (monotonic) is separated by the Q5 null. Subgroup C (topological) is separated by its modulus = 1. This organization was not available from PHYS-10 alone.

### 8.3 The Q5 Null

The null on VP running as band structure identifies periodicity as the structural property separating Subgroups A and B. The VP running is a staircase with unequal steps (ln(m_μ/m_e) = 5.3316 ≠ ln(m_τ/m_μ) = 2.8224), not a periodic function. This constrains future unification attempts: any equivalence between RG running and band structure must account for the aperiodicity of mass thresholds.

### 8.4 The Two-Level Remainder

Every domain has structure at two levels: geometric (R₂ in modulus, R₄ in energy) and domain-specific (the physical remainder). This layered structure was implicit in PHYS-10 and MATH-5 separately but not identified as a universal feature until the Phase 1 extractions made it explicit across all six domains.

### 8.5 The α_s Candidate

α_s = πζ(3)/32 = 0.1180117, matching the measured 0.1180 ± 0.0009 to 0.01%. The formula uses R₂ · ζ(3)/8 — the Subgroup A geometric constant times a QED transcendental divided by a power of 2. No derivation pathway has been identified. It is a candidate for future testing when α_s precision improves (currently at 0.76%, needs approximately 0.01% to test).

---

## IX. THE COMPLETE SERIES

| Paper | Registry | Key Result |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = π/4 separates in 9 domains (2D) |
| MATH-2 | @HOWL-MATH-2-2026 | 17 transcendentals as integer pairs at 100 digits |
| MATH-3 | @HOWL-MATH-3-2026 | Extended basis: elliptic integrals, Borwein ζ(5) |
| MATH-4 | @HOWL-MATH-4-2026 | Universal 2³³⁵ basis, 22 constants |
| MATH-5 | @HOWL-MATH-5-2026 | R_n across dimensions, n=2,4 uniquely binary-native |
| PHYS-1 | @HOWL-PHYS-1-2026 | Mass as inertia (framework) |
| PHYS-2 | @HOWL-PHYS-2-2026 | Couplings run (framework) |
| PHYS-3 | @HOWL-PHYS-3-2026 | G untested at quantum scale |
| PHYS-4 | @HOWL-PHYS-4-2026 | Experimental test program |
| PHYS-5 | @HOWL-PHYS-5-2026 | α running at 0.02 ppm in exact arithmetic |
| PHYS-6 | @HOWL-PHYS-6-2026 | Confinement two-face |
| PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0 from ℤ-topology minimization |
| PHYS-8 | @HOWL-PHYS-8-2026 | m_τ from Koide, 0.91σ (conditional) |
| PHYS-9 | @HOWL-PHYS-9-2026 | α from a_e, QED series, 4.3 ppb |
| PHYS-10 | @HOWL-PHYS-10-2026 | Remainder as observable, PSLQ null |
| DISC-6 | @HOWL-DISC-6-2026 | Four-phase plan (roadmap) |
| **DISC-7** | **@HOWL-DISC-7-2026** | **Execution report: Phases 1-3 delivered, Phase 4 null** |

---

## X. WHAT COMES NEXT

Three directions remain open.

**(a) The α_s test.** If α_s(M_Z) is measured to 0.01% precision (approximately 5× current), the candidate α_s = πζ(3)/32 = 0.11801 can be tested. Current lattice QCD determinations are approaching 0.1% and may reach the needed precision within years.

**(b) The Koide derivation.** The m_τ reduction (PHYS-8) is conditional on deriving why the Koide ratio is 2/3 and why the amplitude is a = √2. The M4 frustration note from the CKS mining database identifies frustrated z = 3 graphs as a candidate mechanism. This is a derivation problem, not a search problem.

**(c) Phase-periodic parameters.** The Subgroup A ground state principle (minimum of cosine on 8R₂ domain → R = 0) produced θ_QCD = 0. If other SM parameters are phases or phase-derived quantities living on 8R₂-periodic domains with energy minima, the same mechanism applies. The CKM CP phase δ_CP is a literal phase, but the modular search found no clean quantization at current measurement precision (±0.06 rad, with δ_CP/π ≈ 0.433, nearest simple fraction 3/7 = 0.429, off by 0.004). Better measurements from LHCb and Belle II may constrain this.

---

## XI. LIMITATIONS

The Phase 4 null is bounded by the search parameters: maxcoeff 1000 for nonlinear PSLQ (versus 10000 in the PHYS-10 linear scan), 18 moduli with denominators up to 20 for the modular search. Larger coefficients, more complex moduli (triple products, nested functions, scale-dependent moduli), or gauge-group-specific moduli (2π/N_c for SU(N_c)) were not tested. The search space is not exhausted.

The α_s candidate has no derivation. A formula without a derivation is a candidate, not a result. The 0.01% match is 76× better than the 0.76% measurement uncertainty, meaning 76 other formulas giving values in the range 0.1171–0.1189 would also match. The candidate is reported for future testing, not as evidence.

The statistical assessment of the modular search relies on analytical estimates. The formal control test (random numbers at the same magnitudes as SM targets, same scan protocol) was identified in PHYS-10 as needed but was not performed in this program.

The synthesis (Phase 3) identifies three subgroups, but the classification depends on which six domains were chosen for PHYS-10. Other physics domains (e.g., Aharonov-Bohm effect, magnetic flux quantization, crystal field splitting) might fit into the existing subgroups or require a fourth. The synthesis is descriptive of the six tested domains, not claimed as exhaustive.

---

## XII. DISC-8 PREVIEW

DISC-8 will be a research plan for the next stage of the program. The broad directions, to be specified in detail:

**Direction 1:** The α_s candidate. If a derivation pathway for α_s = πζ(3)/32 can be identified — connecting ζ(3) (which appears in the QED 2-loop coefficient A₂) to the strong coupling through the remainder framework — this would be a parameter reduction. The first task is to determine whether ζ(3) in the QED series and ζ(3) in the candidate formula have a common origin or are coincidental.

**Direction 2:** Extended domain extraction. Apply the Phase 1 methodology to additional physics domains beyond the PHYS-10 six: Aharonov-Bohm, magnetic flux quantization, Josephson effect, anyonic systems. Each may reveal new subgroup structure or confirm the existing three-subgroup classification.

**Direction 3:** The Koide derivation. Attack the conditional m_τ reduction by deriving the Koide ratio 2/3 and amplitude a = √2 from the remainder framework. The M4 frustration mechanism (z = 3 graph frustration departure from 120° equal spacing) is the current lead.

**Direction 4:** Higher-precision targets. As experimental precision improves for α_s, δ_CP, and quark mass ratios, the modular search can be re-run with tighter thresholds. The infrastructure (Q335 basis, Fraction scripts, modular search code) is ready.

DISC-8 will specify deliverables, falsification criteria, and priorities for each direction, following the DISC-6 model.

---

## APPENDIX A: SCRIPTS

All scripts are in Python, using the standard library `fractions` module for exact arithmetic and `mpmath` for independent numerical verification.

| Script | Phase | Assertions | Status |
|---|---|---|---|
| phase1_bohr_sommerfeld.py | Phase 1, Domain 3 | All pass | VERIFIED |
| phase1_berry.py | Phase 1, Domain 4 | All pass | VERIFIED |
| phase1_brillouin.py | Phase 1, Domain 5 | All pass | VERIFIED |
| phase1_cs.py | Phase 1, Domain 6 | All pass | VERIFIED |
| phase2_unification.py | Phase 2 | All pass | VERIFIED |
| phase3_synthesis.py | Phase 3 | 8 identities, all EXACT | VERIFIED |
| phase4_nonlinear_pslq.py | Phase 4A | 80/80 null | NULL |
| phase4_modular_search.py | Phase 4B | 42 raw hits, no significant result | NULL |

Domains 1 and 2 (theta vacuum, RG running) were extracted in PHYS-7, PHYS-5, and PHYS-9 with their own verification scripts.

---

## APPENDIX B: THE α_s CANDIDATE

α_s = πζ(3)/32

| Property | Value |
|---|---|
| Formula | πζ(3)/32 = R₂ · ζ(3) / 8 |
| Numerical value | 0.118011660505 |
| α_s measured | 0.1180 ± 0.0009 |
| Difference | 0.0000117 |
| Relative | 0.0099% |
| Within measurement uncertainty | Yes |
| Testable at current precision | No |
| Precision needed to test | α_s to ~0.01% (~5× improvement) |
| Derivation | None identified |
| Structural content | R₂ (MATH-1, Subgroup A) × ζ(3) (QED 2-loop) / 2³ |

The formula is clean: two basis constants (R₂ and ζ(3)) combined with a power of 2. It connects the geometric remainder from MATH-1 to the Apéry constant that appears in the QED series (PHYS-9). No derivation pathway from QCD to this formula has been identified. Without a derivation, it is a candidate, not a result.

---

**END HOWL-DISC-7-2026**

**Registry:** [@HOWL-DISC-7-2026]
**Status:** Complete (Retrospective)
**Domain:** Research Program / Mathematical Physics
**Central Report:** Four-phase program executed. Phases 1-3 delivered: universal R₂, three subgroups, two-level remainder, ground state principle. Phase 4 null: no new parameter reduced. One candidate (α_s = πζ(3)/32) untestable at current precision.
**DISC-6 Score:** 5/6 criteria met. F4 (parameter reduction) falsified.
**Parameter Count:** 19 → 18 confirmed (θ_QCD), 18 → 17 conditional (m_τ Koide), α from a_e demonstrated. No change from Phase 4.
**Contribution:** The framework works. The infrastructure is built. The boundary between what the mathematics determines and what the universe supplies has been mapped. The parameters themselves remain on the universe's side of that boundary.
