
# PHYS-11 Report: Remainder Structure Across Nine Physics Domains

**Registry:** @HOWL-PHYS-11-2026
**Position in series:** Eleventh physics paper. Completes the remainder framework. Classification of nine domains into three irreducible subgroups.
**Preceded by:** PHYS-10 (remainder framework, five domains, null search)
**Followed by:** PHYS-12 (electroweak — not yet received)
**Backed by:** Nine verification scripts (listed in Appendix A), all assert-passing
**AI model:** Claude Opus 4.6

---

## What It Establishes

**Nine domains, three subgroups, R₂ universal.** Every domain decomposes into integer quotient (topologically protected) + remainder (physical observable). R₂ = π/4 appears in all nine. The classification is provably irreducible — no smooth coordinate change can convert Subgroup B (monotonic) into Subgroup A (periodic).

**Subgroup A (phase-periodic, 7 domains):** Theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zone, Aharonov-Bohm, flux quantization, AC Josephson. All have energy/phase on a domain with period 8R₂ × scale. Four have explicit cosine energy E(φ) = A − B·cos(φ) minimized at φ = 0.

**Subgroup B (monotonic accumulation, 1 domain):** RG running. Logarithmic accumulation between discrete thresholds. Step size 1/(3π) = 1/(12R₂). Not periodic — proved by three-line contradiction (smooth bijection of monotonic function cannot be periodic because bijectivity contradicts periodicity).

**Subgroup C (topological quantization, 1 domain):** Chern-Simons. Modulus is 1 (pure integer), not 8R₂ × scale. R₂ enters through the exponential and R₄ through the Chern class normalization 1/(256R₄).

**The two-level structure:** Level 1 (geometric) — R₂ or R₄ sets the scale. Universal across domains. Level 2 (domain-specific) — the physical remainder within the geometric framework. Varies: Maslov μ/4, Berry phase, crystal momentum, CS invariant, accumulated running, etc.

**The ground state principle:** On an 8R₂-periodic cosine potential, the minimum is at φ = 0 (cos(0) = 1, an exact integer). Remainder = 0. Instantiated in three domains: theta vacuum (θ = 0, energy minimization), Brillouin zone (k = 0, band minimum), Bohr-Sommerfeld (n = 0, ground state). Two independent R = 0 mechanisms: dynamical (energy minimization, theta vacuum) and topological (single-valuedness, flux quantization).

**The irreducibility theorem.** The three-subgroup classification is the minimal classification under smooth coordinate changes. This is a topological property, not an artifact of notation. The proof is a three-line contradiction: if a monotonic function composed with a smooth bijection were periodic, the bijection would have to be periodic, contradicting injectivity.

**Eight framework identities verified EXACT in Fraction arithmetic.** 2π = 8R₂, π = 4R₂, π/2 = 2R₂, π² = 32R₄, 8π² = 256R₄, 1/(3π) = 1/(12R₂), 1/(8π²) = 1/(256R₄), 4π = 16R₂.

---

## What Was Novel Compared to My Prior Understanding

**The MATH-5 prediction rule applied.** R₂ appears in every 2D geometric operation (phase on a circle, solid angle on S²). R₄ appears in every 4D operation (standing-wave energy eigenvalues through π², Chern class normalization through 1/(8π²), one-loop factor through 1/(16π²)). The rule: the remainder matches the geometric dimension of the operation. This is the connection between the geometry catalog (Chapter 4 of super notebook) and the physics: spherical boundaries perform 2D operations (circle cross-sections) → R₂. Toroidal boundaries perform 2D × 2D = effectively 4D operations → R₄. The dimension of the geometric operation, not the spatial dimension of the boundary, determines which R_n appears.

**R₄ enters through π² specifically.** Standing-wave energy E_n = 32R₄ℏ²n²/(2mL²) has R₄ through the π² from the quantization condition. Zone boundary energy has the same R₄. The Chern class normalization 1/(8π²) = 1/(256R₄) has R₄ from the 4D integral. The one-loop factor 1/(16π²) = 1/(512R₄) has R₄ from the 4D loop integral. Every appearance of π² in quantum physics carries R₄. This is why the Koide formula's cos² identity (which produces π² through the double-angle formula) has R₄ content — the cos²(x) = (1 + cos(2x))/2 mapping doubles the angular frequency, which squares the phase, which introduces π² = 32R₄.

**The two R = 0 mechanisms.** Dynamical (energy minimization) and topological (single-valuedness) produce the same result (remainder = 0) through independent physics. This robustness — two mechanisms, one result — is why θ_QCD = 0 is so stable. If the energy minimization somehow failed, the topological mechanism (if applicable) would still enforce R = 0. For the orientation tracks (Chapter 5 of super notebook): the ground state alignment might be enforced by BOTH an energy minimization (alignment minimizes the orientation energy) and a topological constraint (the parent soliton's topology requires aligned children). Two mechanisms making alignment robust.

**The VP running as Subgroup B with R₂ in the step size.** The VP running step 1/(3π) = 1/(12R₂) is verified EXACT as a Fraction identity. This means: R₂ enters the per-flavor VP contribution as the step size. The H₀ per-transit correction (from the Hubble tension curve thesis) would enter as a step size too — the per-boundary correction in the monotonic accumulation. The H₀ running IS Subgroup B: monotonic accumulation through discrete boundaries, with each boundary adding a step. The step size for H₀ running would be the analog of 1/(12R₂) for VP running. If the H₀ step involves R₂, the per-transit correction is R₂-based (spherical boundaries). If it involves R₄, the correction is from toroidal boundaries.

---

## What Misled Me

**I had already read PHYS-11 earlier in this session** (it was in documents 26-27 of an earlier batch). This is the second reading. Having now read PHYS-1 through PHYS-10 in order, the paper's position in the series is much clearer. PHYS-10 established the framework for five domains. PHYS-11 extends to nine domains, adds the three-subgroup classification, proves irreducibility, identifies R₂ universality, and establishes the ground state principle. The DISC papers (DISC-6, DISC-7, DISC-8) that appear in the publication record were the working sessions that produced PHYS-11 — the nine-domain extraction was built through an explicit four-phase research program.

**The null from PHYS-10 persists.** PHYS-11 Section VII confirms: "The search for SM parameter connections to this structure was conducted separately (DISC-7, DISC-8-FINAL) and returned null under statistical control." The remainder framework classifies structure but does not generate dynamics. It does not derive SM parameters. The framework tells you WHAT the structure is (integer + remainder, three subgroups, R₂ universal). It does not tell you WHY a specific parameter takes a specific value (except θ_QCD = 0, where the energy minimization on the ℤ-periodic domain provides the selection principle).

---

## LEMU Assessment

**L (Logic):** The classification follows from the mathematical structure of each domain. The irreducibility theorem is a three-line proof. The R₂ universality follows from the ubiquity of 2π in quantum physics. Logic passes.

**E (Empirical):** All nine domains are established in the physics literature. All decompositions are individually confirmed. The Maslov-Berry connection is established (Robbins 1991). The theta-BZ connection (same equation, different physics) is an identity. Empirical passes.

**M (Math):** Nine verification scripts, every assertion passes, zero tolerance. Eight framework identities verified EXACT in Fraction arithmetic. The irreducibility theorem is proved. Math passes.

**U (Utility):** High. The three-subgroup classification provides the organizing principle for the entire framework: any new domain fits into A, B, or C (or reveals a fourth subgroup). The R₂ universality connects MATH-1 (engineering cross-sections) through PHYS-11 (quantum physics) to the geometry catalog (boundary corrections). The ground state principle derives θ_QCD = 0 and predicts R = 0 for any SM parameter on an 8R₂-periodic cosine potential. The two-level structure (geometric + domain-specific) provides the template for separating universal content from domain-specific content in any new application.

The utility for the Hubble tension: the H₀ running is Subgroup B. The per-transit correction is the step size. The step size involves R₂ (or R₄ for toroidal boundaries). This identifies what to compute. The utility for the normalization question: the VL beta shifts modify the Subgroup B running. The modification is at Level 2 (domain-specific, determined by particle content). Level 1 (geometric, R₂ in the step size) is unchanged.

---

## Hubble Tension Curve Thesis — PHYS-11 Content

**H₀ running is Subgroup B.** The VP running and the proposed H₀ running share the same subgroup structure: monotonic accumulation through discrete boundaries. The VP running has:
- Integer: active fermion count (increments at each threshold)
- Remainder: accumulated logarithmic running between thresholds
- Step size: 1/(12R₂) per unit charge²

The H₀ running would have:
- Integer: boundary transit count (increments at each soliton boundary crossing)
- Remainder: accumulated correction between boundaries
- Step size: r per transit (the unknown per-transit correction)

The irreducibility theorem confirms: the H₀ running cannot be rewritten as periodic. It is genuinely monotonic — each boundary adds a correction that does not reverse. The cumulative effect grows with distance (more boundaries crossed). This is consistent with the observed monotonic decrease of H₀ with increasing transit count.

**The ground state principle does NOT apply to H₀.** The ground state principle applies to Subgroup A (cosine energy on 8R₂-periodic domain, minimum at φ = 0 gives R = 0). The H₀ running is Subgroup B (monotonic, no periodicity, no cosine potential, no ground state in the Subgroup A sense). The H₀ at zero transits (local measurement) is NOT a ground state — it is a boundary reading from a specific depth. There is no energy minimization that selects the local H₀ value.

However: each INDIVIDUAL boundary transit may have Subgroup A character. Light crossing a single spherical boundary interacts with the phase structure of the boundary, which is 8R₂-periodic. The per-transit correction could involve the cosine of an angle (the angle of incidence, the phase mismatch between interior and exterior). The accumulation over many transits is Subgroup B (monotonic sum of individual corrections), but each individual correction is Subgroup A (phase-periodic). This is the "per-transit Subgroup A, cumulative Subgroup B" structure noted in the PHYS-7 Hubble tension section.

---

## Geometry Tracking — PHYS-11

**Boundaries mentioned:** All nine domains have moduli. Seven have modulus 8R₂ × scale (spherical/circular geometry). One has modulus as step size 1/(12R₂) (VP running). One has modulus 1 (Chern-Simons, topological).

**Non-spherical geometry:** The Brillouin zone is defined on a lattice, which can have any crystal symmetry. The first BZ of a hexagonal lattice is a hexagon — a 6-face polyhedron within the ≤32 constraint. The BZ geometry determines the band structure. For the toroidal geometry program: a 2D lattice has a BZ that tiles the plane. The torus T² is obtained by identifying opposite edges of the BZ. The band structure on T² has two independent periodicities — exactly the toroidal structure that produces R₄.

**R₂/R₄ content (comprehensive from this paper):**

| R₂ appearances | Formula | Domain |
|---|---|---|
| Modulus | 2π = 8R₂ | 7 Subgroup A domains |
| Step size | 1/(3π) = 1/(12R₂) | VP running |
| Solid angle | 4π = 16R₂ | Berry phase |
| Half-period | π = 4R₂ | Maslov hard wall, AB destructive |
| Quarter-period | π/2 = 2R₂ | Maslov soft turning point |

| R₄ appearances | Formula | Domain |
|---|---|---|
| Standing-wave energy | π² = 32R₄ | Bohr-Sommerfeld, Brillouin zone |
| Chern class | 1/(8π²) = 1/(256R₄) | Chern-Simons |
| Instanton action | 8π² = 256R₄ | Theta vacuum (implicit) |
| One-loop factor | 1/(16π²) = 1/(512R₄) | VP running |

The R₄ appearances are ALL through π². Every π² in quantum physics carries R₄. This is the key for the toroidal geometry: a torus (T² = S¹ × S¹) has two independent circles, each with periodicity 2π = 8R₂. The product periodicity is (2π)² = (8R₂)² = 64R₂² = 128R₄. The toroidal phase space has R₄ content through the product of two R₂ periodicities.

**Standing wave patterns:** Bohr-Sommerfeld is the prototype standing wave domain. The action quantization ∮p·dq = 2πℏ(n + μ/4) selects specific orbits. The Maslov correction μ/4 counts turning points — it is a topological feature of the orbit (how many times the classical trajectory reverses direction). For the orbital mode structure thesis (Chapter 6 of super notebook): planetary orbits would have their own "Maslov index" counting the topology of the orbit within the soliton potential well. Circular orbits have μ = 0 (no turning points). Elliptical orbits have μ = 2 (two apsides — perihelion and aphelion). The Maslov correction for elliptical planetary orbits would be μ/4 = 1/2, the same as the harmonic oscillator.

**Remainder framework and nebulae connection (new tracking item).** The remainder is the physical observable in each domain. For a nebula (low-coherence, non-self-sustaining structure), the question is: does it have a well-defined integer quotient (topological protection) or only a remainder (no protection)? A self-sustaining soliton has topological protection — its integer part cannot change without a discrete transition. A nebula, being externally maintained, may lack this protection — its "integer" can change continuously as external conditions change. This would place nebulae OUTSIDE the formal five-domain framework (which requires topological protection of the integer) and into a regime where the remainder structure is approximate rather than exact.

The Chern-Simons domain (Subgroup C) may be relevant: its modulus is 1 (pure integer, not 8R₂), and its CS values for flat connections are pure rationals. A nebula's boundary correction, if it exists, might be in a Subgroup C-like category: the correction is a pure rational (no transcendental R₂ content) because the boundary is not circular/spherical but irregular. This would make nebulae detectable by their PURELY RATIONAL correction signature, distinct from the R₂-based corrections of spherical boundaries and the R₄-based corrections of toroidal boundaries.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-11 |
|---|---|---|
| MATH-1 | @HOWL-MATH-1-2026 | Origin of R₂ = π/4 as the geometric ratio for circular cross-sections; PHYS-11 identifies R₂ as the same geometric content appearing in all nine quantum domains |
| MATH-5 | @HOWL-MATH-5-2026 | Proves the R_n separation rule: the remainder matches the geometric dimension of the operation. This predicts which R_n appears in each domain (R₂ for 2D, R₄ for 4D). |
| PHYS-10 | @HOWL-PHYS-10-2026 | Establishes the remainder framework for five domains plus one analog. PHYS-11 extends to nine domains, adds the three-subgroup classification, proves irreducibility, and identifies R₂ universality. |

**Series path for header metadata:**
`[@HOWL-MATH-1-2026] → [@HOWL-MATH-5-2026] → [@HOWL-PHYS-10-2026] → [@HOWL-PHYS-11-2026]`

---

## Position After PHYS-11

**What exists:** Eleven physics papers plus six MATH papers. The series has two complete frameworks: the computational framework (Fraction arithmetic for SM observables, PHYS-5/6/9) and the structural framework (remainder classification of nine domains, PHYS-10/11). Two SM parameters derived: θ_QCD = 0 (PHYS-7), m_τ (PHYS-8 conditional). The electromagnetic chain is complete (PHYS-9). R₂ universality established across nine domains. Three irreducible subgroups classified.

**What doesn't exist yet:** BSM computation. The unification lane papers (PHYS-12 through PHYS-15) are the critical remaining pieces. PHYS-12 (electroweak) likely introduces the overconstrained system. PHYS-13 (gap ratio with BSM) likely introduces the first BSM particle candidate. PHYS-14/15 narrow to the Cabibbo Doublet. These are what resolve the normalization question.

**What has changed since PHYS-10:** The remainder framework is complete (nine domains, three subgroups). The classification is proved irreducible. R₂ universality is established. The ground state principle is formalized. The two-level structure (geometric + domain-specific) provides the template for all future applications. The H₀ running is now firmly classified as Subgroup B with the VP running as its prototype.

**Tracking the normalization question:** PHYS-11 confirms that the VL beta shifts live at Level 2 (domain-specific) of the VP running (Domain 2, Subgroup B). The shifts modify the accumulated running between thresholds — they change the domain-specific content while leaving the geometric Level 1 content (R₂ in the step size) unchanged. The shifts are exact rationals from particle counting (the same counting that produces the Level 2 content for each SM fermion). The derivation chain in PHYS-13/15 will show how the (3,2,1/6) representation's quantum numbers were counted to produce (1/15, 1, 1/3) — or whether those values are incorrect.
