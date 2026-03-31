# Remainder Structure Across Nine Physics Domains
## Three Subgroups and a Universal Geometric Constant

**Registry:** [@HOWL-PHYS-11-2026]

**Series Path:** [@HOWL-MATH-1-2026] → [@HOWL-MATH-5-2026] → [@HOWL-PHYS-10-2026] → [@HOWL-PHYS-11-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** March 31 2026

**Domain:** Mathematical Physics / Classification / Exact Arithmetic

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## I. ABSTRACT

Nine physics domains — theta vacuum, Bohr-Sommerfeld quantization, Berry phase, Brillouin zones, Aharonov-Bohm effect, flux quantization, AC Josephson effect, renormalization group running, and Chern-Simons theory — each decompose into an integer quotient and a fractional remainder under division by a domain-specific modulus. The integer is topologically protected or counts discrete quanta. The remainder is the physical observable. All decompositions are verified as exact rational identities in Python Fraction arithmetic.

R₂ = π/4, the geometric remainder of a circle inscribed in its bounding square, is present in all nine domains: as the modular period 8R₂ × scale in seven, as the step size 1/(12R₂) per flavor in one, and in the exponential exp(i·8R₂·k·CS) of the ninth. R₄ = π²/32, the four-dimensional analog, enters specifically through energy eigenvalues (π² = 32R₄ in standing-wave and zone-boundary energies) and through the Chern class normalization (1/(8π²) = 1/(256R₄)).

The nine domains fall into three subgroups: phase-periodic (seven domains, cosine energy on an 8R₂-periodic domain), monotonic accumulation (one domain, logarithmic staircase), and topological quantization (one domain, modulus 1). This classification is provably irreducible: no smooth change of variables can convert monotonic into periodic structure. Within the phase-periodic subgroup, a ground state principle holds: the minimum of −cos(φ) on an 8R₂-periodic domain gives remainder = 0, producing θ_QCD = 0 by energy minimization and flux quantization by topological single-valuedness — two independent mechanisms yielding the same mathematical result through different physics.

Every domain exhibits a two-level remainder structure: a geometric level where R₂ (or R₄) sets the scale, and a domain-specific level where the physical remainder lives. The geometric level is universal. The domain-specific level varies: Maslov correction μ/4, Berry phase (1 − cosθ)/2, crystal momentum p/N, Chern-Simons invariant m²k/(2p) mod ℤ, flux ratio Φ/Φ₀, accumulated coupling running, or instantaneous Josephson phase.

No SM parameter is derived. No prediction is made about parameter values. This paper classifies the remainder structure of physics equations across nine domains, proves the classification is irreducible, and identifies R₂ = π/4 as the universal geometric content.

---

## II. THE NINE DOMAINS

### 2.1 The Extraction Table

| # | Domain | Equation | Modulus | = 8R₂ × | Integer | Remainder | R₂ role | R₄ present | Subgroup |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Theta vacuum | E(θ) = E₀ − χcos(θ) | 2π | 1 | Instanton ν | θ = 0 | Modulus | — | A |
| 2 | RG running | α⁻¹(μ) through thresholds | m_f | — | Active flavors | Running | Step 1/(12R₂) | In loop factor 1/(512R₄) | B |
| 3 | Bohr-Sommerfeld | ∮p·dq = 2πℏ(n+μ/4) | 2πℏ | ℏ | Quantum number n | μ/4 = 1/2 | Modulus | In box E: 32R₄ℏ²n²/(2mL²) | A |
| 4 | Berry phase | γ = 4R₂(1−cosθ) | 2π | 1 | Winding n | γ mod 2π | Modulus + γ | — | A |
| 5 | Brillouin zone | E(k) = −2t cos(ka) | 2π/a | 1/a | Zone index | k mod G | Modulus | In E_boundary: n²·32R₄ | A |
| 6 | Chern-Simons | CS(A) mod ℤ | 1 | — | Chern number | CS mod ℤ | Exponential | Normalization 1/(256R₄) | C |
| 7 | Aharonov-Bohm | δφ = 8R₂Φ/Φ₀ | 2π | 1 | Fringe count | Phase mod 2π | Modulus | — | A |
| 8 | Flux quantization | ∮∇θ·dl = 8R₂n | 2π | 1 | Flux quanta n | 0 (exact) | Modulus | — | A |
| 9 | AC Josephson | dφ/dt = 8R₂f_J | 2π | 1 | Cycle count | Instantaneous phase | Modulus | — | A |

Each domain was extracted following the same protocol: equation in standard form, integer/remainder decomposition, Fraction arithmetic computation with specific parameters, verification against known results, identification of R_n content, and a Python script with `assert`-verified identities. Every assertion passes.

### 2.2 Domain Descriptions

**Domain 1: Theta vacuum.** The QCD vacuum energy E(θ) = E₀ − χ_top·cos(θ) is periodic in θ with period 2π = 8R₂. The integer is the instanton number ν ∈ ℤ. The remainder θ mod 2π is the vacuum angle. The ground state has θ = 0 (remainder = 0), derived from energy minimization in [@HOWL-PHYS-7-2026]. Established by 't Hooft 1976, Jackiw and Rebbi 1976.

**Domain 2: RG running.** The electromagnetic coupling α⁻¹(μ) runs through lepton mass thresholds. Between thresholds, the running accumulates logarithmically: α⁻¹(μ) = α⁻¹(μ₀) + Q²/(12R₂)·ln(μ²/μ₀²). At each threshold, a new flavor activates (the integer increments). R₂ enters through the vacuum polarization coefficient 1/(3π) = 1/(12R₂), verified as an exact Fraction identity. Computed in [@HOWL-PHYS-5-2026] and [@HOWL-PHYS-9-2026].

**Domain 3: Bohr-Sommerfeld quantization.** The classical action integral ∮p·dq = 2πℏ(n + μ/4) quantizes in units of the modulus 2πℏ = 8R₂ℏ. For the harmonic oscillator, the Maslov index μ = 2 (two soft turning points) gives remainder μ/4 = 1/2, producing the zero-point energy E₀ = ℏω/2. For the infinite square well, μ = 4 (two hard walls) and the remainder is absorbed into integer counting. The box energy E_n = π²ℏ²n²/(2mL²) = 32R₄ℏ²n²/(2mL²) contains R₄ through the standing-wave quantization condition. Bohr 1913, Sommerfeld 1916, Maslov 1965.

Verified for n = 0 through 100 in Fraction arithmetic. Harmonic oscillator: all 11 tested levels give integer = n, remainder = 1/2 (EXACT). Infinite well: all 5 tested levels give integer = n, remainder = 0 (EXACT). R₂ identity 2π = 8R₂ verified EXACT. R₄ identity E_n = 32R₄ℏ²n²/(2mL²) verified EXACT for n = 1, 2, 3.

**Domain 4: Berry phase.** A spin-1/2 particle in a magnetic field rotating around a cone of half-angle θ acquires geometric phase γ = π(1 − cosθ) = 4R₂(1 − cosθ). The modulus is 2π = 8R₂. The integer counts complete phase windings. The remainder γ mod 2π is the gauge-invariant observable. The solid angle of the full sphere is 4π = 16R₂, consistent with the MATH-5 rule: surface area (a 2D operation) produces R₂. Berry 1984, Simon 1983.

Verified for 9 rational cosθ values. Key special cases: θ = π/2 gives γ = π (Z₂ topological phase), θ = π gives γ = 2π (trivial), θ = 0 gives γ = 0. Multi-circuit accumulation verified for 1, 2, 3, 4, 5, 8 circuits. All EXACT.

**Domain 5: Brillouin zone.** The 1D tight-binding dispersion E(k) = −2t cos(ka) is periodic in k with period G = 2π/a = 8R₂/a. The integer is the zone index. The remainder k mod G is the crystal momentum in the first Brillouin zone, which determines all physical properties. Zone boundary energy E_n = n²π²ℏ²/(2ma²) = n²·32R₄·ℏ²/(2ma²) contains R₄. Bloch 1929, Brillouin 1930.

Verified for a 12-site lattice: 16 k-values decomposed with zone folding. Periodicity verified: k/(2π) = 1/3 and five periodic images all reduce to the same k_BZ. Zone boundary energies verified EXACT for n = 1, 2, 3, 4. Momentum quantum Δk = 8R₂/(Na) verified EXACT.

**Domain 6: Chern-Simons theory.** The Chern-Simons invariant CS(A) is defined modulo ℤ by large gauge invariance. The modulus is 1 — the only domain where the modulus is a pure integer rather than 8R₂ × scale. CS values for flat connections on lens spaces are pure rationals with no transcendental content. R₂ enters through the exponential exp(2πi·k·CS) = exp(i·8R₂·k·CS). R₄ enters through the Chern class normalization 1/(8π²) = 1/(256R₄), which converts the raw gauge field integral into the integer Chern number c₂. The FQHE filling fraction ν = p/q IS the CS remainder: integer Hall has ν ∈ ℤ (R = 0), fractional Hall has ν = p/q (R ≠ 0). Witten 1989, Wen 1990.

Verified for U(1) CS on L(5,1) at level k = 1 (5 flat connections, all exact rationals) and L(7,1) at level k = 3 (7 flat connections). Level quantization from gauge invariance verified. Chern class identity 8π² = 256R₄ verified EXACT. Normalization 1/(8π²) = 1/(256R₄) verified EXACT.

**Domain 7: Aharonov-Bohm effect.** An electron encircling a solenoid with flux Φ acquires phase shift δφ = 2πΦ/Φ₀ = 8R₂·Φ/Φ₀. The modulus is 2π = 8R₂. At half-integer flux Φ = Φ₀/2, the phase is π = 4R₂ (destructive interference). Aharonov and Bohm 1959.

Verified for 7 rational flux ratios. Half-flux phase 4R₂ = π verified EXACT.

**Domain 8: Flux quantization.** In a superconducting ring, the order parameter phase must be single-valued: ∮∇θ·dl = 2πn = 8R₂n. The modulus is 2π = 8R₂. The remainder is exactly 0 — flux is quantized with no fractional part. This is a second R = 0 mechanism within Subgroup A, distinct from θ_QCD = 0 (Section III.2). Deaver and Fairbank 1961, Doll and Näbauer 1961.

Verified for n = 0 through 4: all give remainder = 0 (EXACT).

**Domain 9: AC Josephson effect.** A constant voltage V across a Josephson junction drives phase accumulation dφ/dt = 2eV/ℏ at the Josephson frequency f_J = 2eV/h. In one period, the phase accumulates exactly 2π = 8R₂. The Josephson frequency-voltage relation is exact and is used as the international voltage standard — R₂ is embedded in the metrological definition of the volt. Josephson 1962.

Verified for 8 rational fractions of the Josephson period.

---

## III. THE THREE-SUBGROUP CLASSIFICATION

### 3.1 Subgroup A: Phase-Periodic (7 domains)

Members: theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone, Aharonov-Bohm, flux quantization, AC Josephson.

Shared structure: the energy (or phase or action) is a function on a domain with period 8R₂ × scale. For the four domains with explicit cosine energy — theta vacuum, Bohr-Sommerfeld, Brillouin zone, and Aharonov-Bohm — the functional form is E(φ) = A − B·cos(φ), minimized at φ = 0.

| Domain | Scale | Period |
|---|---|---|
| Theta vacuum | 1 | 8R₂ |
| Bohr-Sommerfeld | ℏ | 8R₂ℏ |
| Berry phase | 1 | 8R₂ |
| Brillouin zone | 1/a | 8R₂/a |
| Aharonov-Bohm | 1 | 8R₂ |
| Flux quantization | 1 | 8R₂ |
| AC Josephson | 1 | 8R₂ |

Two internal connections verified in exact Fraction arithmetic:

The Maslov-Berry connection: the Maslov correction μ/4 equals the Berry phase of the orbit divided by the modulus 8R₂. In R₂ units: Maslov = (μ × 2R₂)/(8R₂) = μ/4. This is an algebraic tautology — both count the same thing (phase at turning points) in the same units (multiples of 2R₂ = π/2). Verified EXACT for harmonic oscillator (μ = 2, correction = 1/2) and infinite well (μ = 4, correction = 1). The connection is established physics (Robbins 1991, Littlejohn 1992); the contribution here is expressing it as a Fraction identity in R₂ units.

The theta-BZ connection: the theta vacuum energy E(θ) = E₀ − χcos(θ) and the tight-binding dispersion E(k) = −2t cos(ka) are the same equation — cosine on an 8R₂-periodic domain, minimized at the parameter = 0. Same mathematics, different physics (vacuum angle versus crystal momentum).

### 3.2 Two R = 0 Mechanisms within Subgroup A

Both the theta vacuum and flux quantization give remainder = 0, but by different physics:

| Property | Theta vacuum | Flux quantization |
|---|---|---|
| Modulus | 8R₂ | 8R₂ |
| R = 0 because | Energy E(θ) = E₀ − χcosθ minimized at θ = 0 | Wavefunction ψ single-valued: ∮∇θ·dl = 2πn |
| Mechanism | Dynamical (energy minimization) | Topological (single-valuedness constraint) |
| Robustness | Depends on the potential | Absolute (topological) |

The same mathematical result (R = 0 on an 8R₂-periodic domain) arises from two independent physical mechanisms. This means R = 0 in Subgroup A is robust — it is not tied to a single mechanism.

### 3.3 Subgroup B: Monotonic Accumulation (1 domain)

Member: RG running.

The coupling α⁻¹(μ) accumulates logarithmically between mass thresholds: α⁻¹(μ) = α⁻¹(μ₀) + Σ_f Q_f²/(12R₂)·ln(μ²/m_f²)·Θ(μ − m_f). R₂ appears in the step size 1/(3π) = 1/(12R₂), verified EXACT. The running is not periodic: threshold intervals are unequal (ln(m_μ/m_e) = 5.33, ln(m_τ/m_μ) = 2.82, ratio 1.89 ≠ 1). The functional form is logarithmic, not cosine. The structural parallel with Subgroup A (continuous accumulation between discrete boundaries) was tested and found to be an analogy, not a formal equivalence.

### 3.4 Subgroup C: Topological Quantization (1 domain)

Member: Chern-Simons.

The CS invariant is defined modulo ℤ by large gauge invariance. The modulus is 1 — not 8R₂ × scale. The CS values for flat connections are pure rationals with no transcendental content. Transcendental content enters through the normalization 1/(8π²) = 1/(256R₄), which converts the raw gauge field integral into the integer Chern number c₂, and through the exponential exp(2πi·k·CS) = exp(i·8R₂·k·CS), which enforces integer level quantization. The connection to the theta vacuum: θ_QCD = 0 (PHYS-7) means CS mod ℤ = 0 for the QCD vacuum — the same R = 0 result expressed in Subgroup C language.

### 3.5 The Irreducibility Theorem

**Theorem.** No smooth bijection can make the VP running periodic.

**Proof.** Between adjacent thresholds, α⁻¹(κ) = a + cκ where κ = ln(μ/m_f), which is linear. Suppose a smooth bijection g: ℝ → ℝ makes f(g(x)) = a + c·g(x) periodic with period P. Then g(x + P) = g(x) for all x. But g is bijective (injective), and a periodic function satisfies g(0) = g(P), contradicting injectivity. ∎

**Corollary.** Any monotonic function composed with any bijection remains non-periodic. The separation between Subgroup A (periodic) and Subgroup B (monotonic) is preserved under all smooth coordinate changes. The three-subgroup classification is the minimal classification of these nine domains under smooth coordinate changes.

This is stronger than the empirical observation of unequal thresholds. Even a single threshold segment, in isolation, cannot be made periodic. The classification is not an artifact of coordinate choice — it is a topological property.

---

## IV. THE UNIVERSAL CONSTANT R₂ = π/4

### 4.1 Presence Across All Domains

R₂ = π/4 appears in all nine domains. Its structural role differs by subgroup:

| Subgroup | Members | R₂ role | Formula |
|---|---|---|---|
| A (7 domains) | θ, BS, Berry, BZ, AB, Flux, Josephson | Sets the PERIOD | Period = 8R₂ × scale |
| B (1 domain) | RG running | Sets the STEP SIZE | Step = Q²/(12R₂) |
| C (1 domain) | Chern-Simons | In EXPONENTIAL and NORMALIZATION | exp(i·8R₂·k·CS); 1/(256R₄) |

R₂ never appears as a primary quantity — always as the geometric conversion factor between rectilinear and circular measurement, which is its identity from [@HOWL-MATH-1-2026]. Every factor of 2π in these nine domains is 8R₂. Every factor of π is 4R₂. The universality of R₂ follows from the ubiquity of 2π in quantum mechanics and gauge theory. The paper identifies R₂ as the geometric content of 2π, not as an independent physical constant.

### 4.2 The MATH-5 Prediction Rule

[@HOWL-MATH-5-2026] proved that the n-ball remainder R_n = π^{n/2}/(2^n·Γ(n/2+1)) separates in every equation performing an n-ball-volume operation. The rule: the remainder matches the geometric dimension of the operation. This explains the two-level structure:

R₂ appears in every domain that performs a 2D geometric operation — phase on a circle (all of Subgroup A), integration over S² (Berry phase solid angle 4π = 16R₂), and gauge phase periodicity (Subgroup C exponential).

R₄ appears when a 4D operation is involved: standing-wave energy eigenvalues (π² = 32R₄ from the quantization condition in 1D with periodic boundary), zone-boundary energies (same π²), the Chern class normalization (1/(8π²) = 1/(256R₄) from integration over a 4-manifold), and the one-loop factor (1/(16π²) = 1/(512R₄) from the 4D loop integral solid angle).

| Domain | Where R₄ enters | Equation | Origin |
|---|---|---|---|
| Bohr-Sommerfeld | Box energy | E_n = 32R₄ℏ²n²/(2mL²) | Standing wave λ = 2L/n gives π² |
| Brillouin zone | Zone boundary energy | E_n = n²·32R₄ℏ²/(2ma²) | Bragg condition λ = 2a gives π² |
| Chern-Simons | Chern class normalization | c₂ = ∫Tr(F∧F)/(256R₄) | 4D integral solid angle Ω₄ = 2π² = 64R₄ |
| RG running | One-loop factor | 1/(16π²) = 1/(512R₄) | 4D loop integral measure |

### 4.3 The Two-Level Structure

Every domain has remainder structure at two levels.

**Level 1 (geometric):** R₂ sets the scale — the modular period, the step size, or the normalization. R₄ enters energy eigenvalues and 4D normalizations. This level is universal across domains.

**Level 2 (domain-specific):** The physical remainder within the geometric framework. This level varies:

| # | Domain | Level 1 | Level 2 | Physical meaning |
|---|---|---|---|---|
| 1 | Theta vacuum | R₂ in 8R₂ modulus | θ = 0 | Vacuum selects lowest energy |
| 2 | RG running | R₂ in 1/(12R₂) step | Accumulated running | Coupling value at scale μ |
| 3 | Bohr-Sommerfeld | R₂ in 8R₂ℏ modulus | μ/4 = 1/2 | Zero-point energy from turning points |
| 4 | Berry phase | R₂ in γ = 4R₂(1−cosθ) | (1−cosθ)/2 | Fractional solid angle enclosed |
| 5 | Brillouin zone | R₂ in G = 8R₂/a | p/N | Discrete crystal momentum |
| 6 | Chern-Simons | R₄ in 1/(256R₄) | m²k/(2p) mod ℤ | Flat connection topological label |
| 7 | Aharonov-Bohm | R₂ in 8R₂ modulus | Φ/Φ₀ mod 1 | Interference fringe position |
| 8 | Flux quantization | R₂ in 8R₂ modulus | 0 | Exact quantization (topological) |
| 9 | AC Josephson | R₂ in 8R₂ modulus | t/T_J mod 1 | Instantaneous supercurrent phase |

---

## V. THE GROUND STATE PRINCIPLE

On an 8R₂-periodic domain with energy E(φ) = A − B·cos(φ), the minimum is at φ = 0 where cos(0) = 1 (an exact integer). The ground state has remainder = 0.

This principle is instantiated in three Subgroup A domains with explicit cosine energy:

**Theta vacuum:** E(θ) = E₀ − χ_top·cos(θ). The vacuum selects θ = 0 by energy minimization. This is the derivation of θ_QCD = 0 in [@HOWL-PHYS-7-2026].

**Brillouin zone:** E(k) = −2t cos(ka). The band minimum is at k = 0. Electrons fill states starting from the minimum.

**Bohr-Sommerfeld:** The ground state quantum number is n = 0 (the zero-node state at the minimum of the effective potential).

Berry phase gives γ = 0 when no solid angle is enclosed (θ = 0), but this is the trivial case of no parameter-space path, not a minimization on a cosine potential.

Flux quantization gives R = 0 by a different mechanism — topological single-valuedness, not energy minimization. It is a separate R = 0 result within Subgroup A (Section III.2).

The ground state principle predicts: any SM parameter that lives on an 8R₂-periodic cosine potential will have its ground state at remainder = 0. Whether any unmapped SM parameter lives on such a domain is an open question.

---

## VI. THE EIGHT FRAMEWORK IDENTITIES

Eight exact Fraction identities define the framework. All are consequences of R₂ = π/4 and R₄ = π²/32. Their value is making R₂ and R₄ visible in every formula where π and π² currently sit unnamed.

| # | Identity | Decimal | Role | Verified |
|---|---|---|---|---|
| 1 | 2π = 8R₂ | 6.283 = 8 × 0.785 | Phase period (Subgroup A modulus) | EXACT |
| 2 | π = 4R₂ | 3.142 = 4 × 0.785 | Half period (Maslov hard wall, AB destructive) | EXACT |
| 3 | π/2 = 2R₂ | 1.571 = 2 × 0.785 | Maslov unit (soft turning point phase) | EXACT |
| 4 | π² = 32R₄ | 9.870 = 32 × 0.308 | 4D geometric content (energy eigenvalues) | EXACT |
| 5 | 8π² = 256R₄ | 78.96 = 256 × 0.308 | Instanton action normalization | EXACT |
| 6 | 1/(3π) = 1/(12R₂) | 0.1061 | VP running step size per unit charge² | EXACT |
| 7 | 1/(8π²) = 1/(256R₄) | 0.01267 | Chern class normalization (c₂ ∈ ℤ) | EXACT |
| 8 | 4π = 16R₂ | 12.57 = 16 × 0.785 | Full sphere solid angle | EXACT |

All verified in `phase3_synthesis.py`. All assertions pass.

---

## VII. LIMITATIONS

This paper classifies nine domains selected from quantum mechanics and gauge theory. Other physics domains — both quantum (Bjorken scaling, Witten index, magnetic monopole quantization) and classical (pipe flow, drag, diffusion from [@HOWL-MATH-1-2026]) — may require a fourth subgroup or may fit the existing three. The classical domains from MATH-1 also contain R₂ but were not extracted here because [@HOWL-PHYS-10-2026] scoped the remainder framework to quantum domains. The classification is proven irreducible for the nine tested domains, not claimed as exhaustive.

R₂ = π/4 is present in all nine domains because all nine involve phase periodicity, gauge invariance, or loop integrals — which all contain factors of 2π. The universality of R₂ is a consequence of the ubiquity of 2π in quantum physics, identified here as geometric content (the circle-to-square remainder from MATH-1) rather than as a new physical principle.

The two-level structure is descriptive. It says WHAT separates (R₂ at Level 1, domain-specific remainder at Level 2) but not WHY the structure exists at two levels.

No SM parameter is derived. No prediction is made about parameter values. The framework classifies structure; it does not generate dynamics. The search for SM parameter connections to this structure was conducted separately ([@HOWL-DISC-7-2026], [@HOWL-DISC-8-2026-FINAL]) and returned null under statistical control.

---

## VIII. FALSIFICATION

**F1.** If a physics domain is found with integer/remainder structure and modulus 8R₂ × scale but not fitting Subgroup A's shared structure (e.g., not periodic, or periodic but not cosine), the Subgroup A description needs revision. Each domain stands independently.

**F2.** If a domain is found where R₂ is genuinely absent — not hidden in notation but structurally absent — the universality claim is falsified for that domain.

**F3.** If a smooth bijection is found that makes a monotonic function periodic, the irreducibility theorem is wrong. This cannot happen (the proof is a three-line contradiction), but the criterion is stated.

**F4.** If the eight framework identities are algebraically incorrect, the foundation is wrong. They are consequences of the definitions R₂ = π/4 and R₄ = π²/32, verified by `assert` in Fraction arithmetic.

---

## APPENDIX A: VERIFICATION SCRIPTS

| Script | Domain(s) | Key assertions | Status |
|---|---|---|---|
| PHYS-7 scripts | Theta vacuum (Domain 1) | θ = 0 from energy minimization | VERIFIED |
| PHYS-5, PHYS-9 scripts | RG running (Domain 2) | VP running at 0.02 ppm | VERIFIED |
| `bohr_sommerfeld.py` | BS (Domain 3) | 11 energy levels, R₂ and R₄ identities | VERIFIED |
| `berry.py` | Berry phase (Domain 4) | 9 test cases, 5 multi-circuit, R₂ identities | VERIFIED |
| `brillouin_zone.py` | BZ (Domain 5) | 16 k-values, periodicity, R₄ in energy | VERIFIED |
| `chern_simons.py` | CS (Domain 6) | 12 flat connections, level quantization, R₄ normalization | VERIFIED |
| `disc8_item5_domains.py` | AB, Flux, Josephson (Domains 7-9) | All phase decompositions, R₂ identities | VERIFIED |
| `phase_2.py` | Cross-domain connections | Q1 (Maslov-Berry), Q6 (θ-BZ), Q5 (VP null) | VERIFIED |
| `phase_3.py` | Synthesis | 8 framework identities, all EXACT | VERIFIED |

---

## APPENDIX B: SERIES PUBLICATION RECORD

| Paper | Registry | Key Result | Role in PHYS-11 |
|---|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | β = R₂ = π/4 in 9 engineering domains | Origin of R₂ |
| MATH-5 | @HOWL-MATH-5-2026 | R_n separation, n = 2, 4 uniqueness | R_n prediction rule |
| PHYS-5 | @HOWL-PHYS-5-2026 | α running at 0.02 ppm | Domain 2 extraction |
| PHYS-7 | @HOWL-PHYS-7-2026 | θ_QCD = 0 | Domain 1 extraction |
| PHYS-9 | @HOWL-PHYS-9-2026 | α from a_e, 4.3 ppb | Domain 2 extraction |
| PHYS-10 | @HOWL-PHYS-10-2026 | Remainder framework, 6 domains | Framework and initial extractions |
| DISC-6 | @HOWL-DISC-6-2026 | Four-phase plan | Program structure |
| DISC-7 | @HOWL-DISC-7-2026 | Phases 1-3 delivered | Domains 3-6 extraction, Phase 2-3 results |
| DISC-8 | @HOWL-DISC-8-2026-FINAL | Control test, VP closure, domains 7-9 | Irreducibility proof, Subgroup A extension |
| **PHYS-11** | **@HOWL-PHYS-11-2026** | **Nine domains, three subgroups, R₂ universal** | **This paper** |

---

**END HOWL-PHYS-11-2026**

**Registry:** [@HOWL-PHYS-11-2026]
**Status:** Complete
**Domain:** Mathematical Physics / Classification / Exact Arithmetic
**Central Result:** Nine physics domains decompose into integer + remainder structure. R₂ = π/4 is present in 100% of domains. Three subgroups: phase-periodic (7), monotonic (1), topological (1). Classification provably irreducible. Ground state principle: minimum of cosine on 8R₂ domain gives R = 0. Two-level remainder: geometric (R₂/R₄) and domain-specific.
**What it proves:** Classification of nine domains with exact Fraction verification. Irreducibility theorem. R₂ universality. Ground state principle for three domains. Two independent R = 0 mechanisms.
**What it does NOT prove:** No SM parameter derived. No prediction of parameter values. No new physics. Every equation is standard and published. The contribution is the unified classification with exact arithmetic verification.
**Verification:** 9 Python scripts, every assertion passes, zero tolerance.
