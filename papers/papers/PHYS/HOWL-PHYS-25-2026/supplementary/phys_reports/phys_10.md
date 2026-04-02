
# PHYS-10 Report: Remainder as Observable

**Registry:** @HOWL-PHYS-10-2026
**Position in series:** Tenth physics paper. Establishes the remainder framework across six quantum domains. Reports null search for SM parameter moduli.
**Preceded by:** PHYS-9 (electromagnetic chain, one measurement → α at every scale)
**Followed by:** PHYS-11 (nine domains, three subgroups — already read)
**Backed by:** Scripts in Appendix G (inline, not separate files)
**AI model:** Claude Opus 4.6

---

## What It Establishes

**Three independent claims:**

**Claim 1 (observational):** In five domains of quantum physics — Berry phase, Brillouin zones, Bohr-Sommerfeld quantization, Chern-Simons theory, QCD theta vacuum — physical quantities decompose into integer quotient + remainder under division by a domain-specific modulus. The integer is topologically protected (cannot change continuously). The remainder is the physical observable. A sixth domain (RG flow) is analogous but the fixed point is not topologically protected. Each decomposition is individually established in the literature. The contribution is the unified observation.

**Claim 2 (computational):** The Q335 framework (MATH-4) makes quotient-remainder decomposition exact at every step. When a Q335 quantity is divided by a basis constant, both quotient and remainder are exact ratios of integers. No rounding. The computation is integer division on 100-digit numerators with shared denominator 2³³⁵.

**Claim 3 (data — null):** A systematic search for the modulus connecting this structure to SM coupling constants returns null. 17 SM dimensionless ratios tested against 34 transcendental basis constants: no clean integer quotients. PSLQ at maxcoeff = 10,000: 57 tests, all null. The modulus connecting the integer framework to SM parameter values is NOT any single basis constant or simple rational fraction thereof.

**The five formal domains share a common pattern:**

| Domain | Modulus | Integer | Remainder (observable) | Source of modulus |
|---|---|---|---|---|
| Berry phase | 2π | Winding number | Geometric phase | Phase periodicity |
| Brillouin zone | 2π/a | Zone index | Crystal momentum | Lattice symmetry |
| Bohr-Sommerfeld | 2πℏ | Quantum number n | Maslov correction μ/4 | Action quantization |
| Chern-Simons | 1 | Chern number | CS mod ℤ | Large gauge invariance |
| Theta vacuum | 2π | Instanton number | θ | π₃(SU(3)) = ℤ |

In every case: modulus from symmetry/topology, integer cannot change continuously, remainder IS the physics.

**The VP running as concrete RG example.** Section IV.2 decomposes the electromagnetic running into Type A (computational residual — convergence measure) and Type B (physical threshold decomposition — fermion count is integer, logarithmic running between thresholds is remainder). Type B IS a formal quotient-remainder decomposition.

**The null search is honestly reported.** The α⁻¹/ζ(3) ≈ 114 hit (remainder/modulus = 0.00126) is statistically assessed: with 34 moduli tested, the probability of one hit at this level is ~expected from random. The formal control test (random numbers at same magnitudes) is noted as needed but not performed. The paper does not promote the near-hit and does not hide it.

---

## What Was Novel Compared to My Prior Understanding

**The modulus is determined by symmetry, not by the parameter.** In each of the five domains, the modulus comes from the system's symmetry structure (phase periodicity, lattice symmetry, gauge invariance, homotopy group). The modulus is NOT a property of the parameter being measured — it's a property of the SYSTEM being measured in. This means: for SM coupling constants, the modulus (if one exists) would come from the gauge group's topological structure, not from the coupling value itself.

Section VI direction (d) suggests gauge-group-specific moduli: 2π for U(1) phases, π for SU(2) doublet phases, 2π/3 for SU(3) color phases. The VL beta shifts live in SU(3) × SU(2) × U(1), so the relevant moduli would be group-specific. This connects to the normalization question: the SU(3) Dynkin index 1/3 might relate to a modulus 2π/3 for SU(3), while the SU(2) index 1 relates to modulus π, and the U(1) index 1/15 relates to modulus 2π with a specific normalization.

**The Type A / Type B distinction.** Computational residuals (how well Newton's method converged) are fundamentally different from physical remainders (how much running accumulated between thresholds). Both are exact in Fraction arithmetic. But Type A measures algorithm performance while Type B measures physics. This distinction prevents confusing numerical precision with physical content.

For the normalization question: the 38/38 library checks are Type A (do the stored values reproduce themselves?). A physical check — do the Dynkin formulas applied to SM fermion content reproduce the SM betas? — would be Type B. The session has been running Type A checks and treating them as if they were Type B.

**The null is the most important result.** 57 PSLQ tests, all null. 600 modular combinations, no clean hits. SM coupling constants are NOT simple rational combinations of the transcendental basis. This means: the SM parameters are either (a) determined by a more complex relationship (products of basis constants, scale-dependent moduli, self-referential moduli), or (b) genuinely free — supplied by the universe without mathematical constraint. The series proceeds on hypothesis (a) while acknowledging (b) is possible.

**Appendix E: The complete physics constants enumeration.** This is the most comprehensive table in the series. Pure integers (1 through 218), simple rationals (1/2 through 28259/5184), 34 transcendentals in Q335 basis, 20 measured dimensionless constants, and 6 SI-defined exact constants. Everything the series computes with is cataloged. The VL beta shifts would add to the "simple rationals" column: 1/15, 1, 1/3 (or 2/15, 2, 4/3 depending on convention).

---

## What Misled Me

**The search scope limitation.** The null applies to SINGLE-constant moduli with linear PSLQ at maxcoeff ≤ 10,000. Products of basis constants (π·ζ(3), ln(2)·π², etc.) were NOT tested. Scale-dependent and self-referential moduli were NOT tested. The null is a bound on the simplest possible relationships. More complex relationships remain open. For the normalization question: if the VL shifts involve a non-trivial relationship between the Dynkin indices and the gauge group structure, a simple comparison to external formulas would miss it — just as the PSLQ search misses non-linear relationships.

**The Appendix D modular scan near-hits.** sin²θ_W ≈ ln(2)/3 to 0.07%. αs ≈ √2/12 to 0.13%. These are tantalizing but statistically expected from random. The paper correctly refuses to promote them. But they ARE recorded for future investigation — if a theoretical derivation produces sin²θ_W = ln(2)/3 from first principles, the near-hit becomes a verification rather than a coincidence. The series method: record everything, promote nothing without derivation.

---

## LEMU Assessment

**L (Logic):** The quotient-remainder structure in each domain follows from the domain's topology/symmetry. The Q335 arithmetic is exact by construction. The null search follows standard PSLQ protocol. Logic passes for all three claims.

**E (Empirical):** Each domain's structure is individually confirmed in the physics literature (Berry, Bloch, Bohr, Chern-Simons, 't Hooft). The Q335 computation matches all known exact results. The null search is honestly reported with statistical assessment. Empirical passes.

**M (Math):** Claim 1 is proved domain by domain. Claim 2 is demonstrated by exact integer division on Q335 numerators. Claim 3 is a computational result (57 nulls). Math passes.

**U (Utility):** Claim 1 has high utility — it provides the framework that PHYS-11 extends to nine domains with the three-subgroup classification and the R₂ universality result. Claim 2 has high utility — it demonstrates that exact arithmetic makes the abstract quotient-remainder structure computationally tractable. Claim 3 has moderate utility — it bounds the search space and prevents wasting effort on single-constant moduli, directing future work toward more complex relationships (products, scale-dependent, self-referential). The null itself is the utility — knowing where NOT to look is as valuable as knowing where to look.

---

## Hubble Tension Curve Thesis — PHYS-10 Content

**The VP running is Subgroup B of the remainder framework.** Section IV.2 classifies it: fermion count (integer) + logarithmic running (remainder). The H₀ running curve would be the same subgroup: boundary count (integer) + cumulative correction (remainder). The modulus for the VP running is the per-flavor step size 1/(3π) = 1/(12R₂). The modulus for the H₀ running would be the per-transit correction r — the quantity the curve thesis is trying to extract.

**The null search constrains the H₀ modulus.** If the per-transit correction r is a simple rational involving a single transcendental basis constant, the PSLQ search would have found it (since α⁻¹ ≈ 137 mod various constants was tested). The fact that α⁻¹ doesn't decompose simply suggests the H₀ per-transit correction also won't decompose simply into single basis constants. The modulus may involve products of constants or scale-dependent structure.

**Direction (b) from Section VI: scale-dependent moduli.** The VP running modulus changes at each threshold (different fermion contributions). The H₀ modulus may change at each boundary type (different coherence classes contribute different corrections). This connects directly to the taxonomy (Chapter 3 of super notebook): the modulus is not universal but boundary-type-dependent.

---

## Geometry Tracking — PHYS-10

**Boundaries mentioned:** Five formal domains, each with a modulus from symmetry/topology. Berry phase: S² (solid angle), modulus 2π. Brillouin zone: lattice (periodic, modulus 2π/a). Bohr-Sommerfeld: S¹ (orbit, modulus 2πℏ). Chern-Simons: 3-manifold (modulus 1 from large gauge invariance). Theta vacuum: S³ → SU(3) (modulus 2π from π₃(SU(3)) = ℤ).

**Non-spherical geometry:** The Brillouin zone is defined on a lattice, which can be any crystal system — cubic, hexagonal, etc. The first Brillouin zone of a hexagonal lattice is a hexagon (6 faces, within the ≤32 constraint). The zone boundary where band gaps open is at the BZ faces — the geometry of these faces determines the gap structure. For a cubic lattice: square faces (4 faces relevant). For hexagonal: hexagonal faces (6 faces). The polyhedral geometry of the BZ determines the electronic band structure.

**R₂/R₄ content:** Every modulus except the Chern-Simons modulus (which is 1) contains 2π = 8R₂. Berry phase: modulus 8R₂. Brillouin zone: modulus 8R₂/a. Bohr-Sommerfeld: modulus 8R₂ℏ. Theta vacuum: modulus 8R₂. The R₂ universality noted in PHYS-11 is already visible here: 4 of 5 formal domains have modulus proportional to 8R₂.

The Chern-Simons modulus is 1 (integer, no R₂). This is the one domain in Subgroup C of PHYS-11. Its modulus comes from large gauge invariance, not from phase periodicity. The R₂ enters through the exponential exp(2πi·k·CS) = exp(i·8R₂·k·CS), not through the modulus itself.

**Standing wave patterns:** Bohr-Sommerfeld quantization is explicitly a standing wave condition: the action integral must be an integer times the modulus for the wave function to be single-valued. This is the prototype for the orbital mode structure idea (Chapter 6 of super notebook): the standing wave condition selects specific radii/energies.

**Correction factors:** The Maslov correction μ/4 is a rational remainder (1/2 for harmonic oscillator, 3/4 for hard wall + soft turning point). These are exact rationals determined by the orbit topology (number of turning points). The per-transit correction in the H₀ curve would be an analogous rational remainder determined by the boundary geometry.

---

## Foundational Papers Table

| Paper | Registry | Why foundational to PHYS-10 |
|---|---|---|
| MATH-4 | @HOWL-MATH-4-2026 | Provides the Q335 basis with shared denominator 2³³⁵ that makes quotient-remainder decomposition exact integer arithmetic on numerators |
| PHYS-7 | @HOWL-PHYS-7-2026 | Provides the one successful remainder derivation: θ_QCD = 0 is remainder = 0 from energy minimization on the ℤ-periodic domain. This is Domain 5 in the framework and the proof that the remainder approach can derive a physical parameter. |
| PHYS-9 | @HOWL-PHYS-9-2026 | Provides the electromagnetic chain that demonstrates Type B physical remainder decomposition (VP running through thresholds as integer fermion count + continuous running remainder) |

**Series path for header metadata:**
`[@HOWL-MATH-4-2026] → [@HOWL-PHYS-7-2026] → [@HOWL-PHYS-9-2026] → [@HOWL-PHYS-10-2026]`

---

## Position After PHYS-10

**What exists:** Ten physics papers plus six MATH papers. The remainder framework is established across five formal domains plus one analogous domain. The Q335 tool makes the framework computationally exact. A systematic search for SM parameter moduli returns null at single-constant level with maxcoeff ≤ 10,000. Two SM parameters derived: θ_QCD = 0 (PHYS-7, exact), m_τ (PHYS-8, 0.91σ conditional). The electromagnetic chain is complete (PHYS-9). The confinement wall and 4-loop wall are identified as current limits.

**What PHYS-11 extends from PHYS-10:** PHYS-11 (already read) takes the five domains from PHYS-10 and adds four more (Aharonov-Bohm, flux quantization, AC Josephson, extending the phase-periodic subgroup; plus re-formalizing the RG running). The three-subgroup classification (phase-periodic, monotonic, topological) and the R₂ universality result are PHYS-11's contributions beyond PHYS-10's five-domain framework. The connection is direct: PHYS-10 establishes the framework, PHYS-11 completes and classifies it.

**What doesn't exist yet:** BSM computation. No VL doublet. No modified beta slopes. The unification lane papers (PHYS-12, PHYS-13, PHYS-14, PHYS-15) remain the critical missing pieces for the normalization question.

**Tracking the normalization question:** PHYS-10's null search result is relevant: the SM parameters do not decompose simply into the transcendental basis. The VL beta shifts (1/15, 1, 1/3) are simple rationals, not transcendentals. They belong to Appendix E's "simple rationals" category, alongside b₁ = 41/10, b₂ = −19/6, b₃ = −7. The question is not whether they decompose into transcendentals (they don't — they're rational) but whether they are the CORRECT rationals for the (3,2,1/6) representation. The derivation chain in PHYS-13/15 will answer this. The null search does not constrain the normalization question because the question is about rationals, not transcendentals.
