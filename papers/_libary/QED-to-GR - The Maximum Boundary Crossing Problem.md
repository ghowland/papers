## QED-to-GR: The Maximum Boundary Crossing Problem

**Status:** Active conceptual notebook. Connects the series' deepest structural elements.
**Origin:** Session 4, April 2 2026. Author's concept from an earlier session, restated here.
**Depends on:** PHYS-1 (mass is inertia, boundary readings), PHYS-2 (transformation law fundamental), PHYS-3 (G untested outside Hill sphere), PHYS-5/9 (VP running, electromagnetic chain), PHYS-6 (confinement wall), PHYS-10/11 (remainder framework, Subgroup B), PHYS-14 (domain map, geometric stages), modulus superset notebook, composite soliton hierarchy notebook

---

### 1. THE OBSERVATION

QED and GR are the two most precisely verified theories in physics. QED predicts g-2 to 0.11 ppb (PHYS-9). GR predicts Mercury's precession to 0.01%. Both work spectacularly within their domains.

They cannot be combined. Every attempt to quantize gravity produces infinities that cannot be removed by renormalization. The "quantum gravity problem" has consumed thousands of careers over 70+ years with no resolution.

The standard framing: "gravity is fundamentally different from the other forces" or "we need a new theory that reduces to both QED and GR in appropriate limits" or "the correct description requires string theory / loop quantum gravity / etc."

The soliton framing offers a different diagnosis: QED and GR operate at opposite ends of the soliton hierarchy, and describing one in terms of the other requires running through EVERY boundary layer in between. The failure to combine them is not because they are fundamentally different — it is because the cumulative running through all intermediate boundaries has not been computed.

---

### 2. THE HIERARCHY DISTANCE

QED operates at the subatomic scale. Its natural domain is the electron's VP cloud — a spherical soliton boundary at ~10⁻¹³ m. The coupling α = 1/137 is measured at this scale. The QED perturbative series (A₁, A₂, A₃, A₄) describes the transformation law within this single boundary layer.

GR operates at the planetary-to-cosmological scale. Its natural domain is the gravitational field of macroscopic objects — soliton boundaries from ~10⁶ m (Earth) to ~10²⁶ m (observable universe). The coupling G is measured at the terrestrial scale and ASSUMED constant at all other scales (PHYS-3: G has never been tested outside Earth's Hill sphere).

The hierarchy distance between QED and GR spans approximately 40 orders of magnitude in length scale. In the soliton hierarchy, this corresponds to crossing through EVERY intermediate boundary layer:

| Scale | Soliton | Boundary type | R_n content |
|---|---|---|---|
| 10⁻¹³ m | VP cloud | Sphere | R₂ |
| 10⁻¹⁵ m | Proton | Sphere (99% binding energy) | R₂ |
| 10⁻¹⁰ m | Atom | Sphere (electron cloud) | R₂ |
| 10⁻⁹ m | Molecule | Irregular (chemical bonds) | Mixed |
| 10⁻⁶ m | Cell | Irregular (membrane) | Mixed |
| 10⁻² m | Organism | Irregular | Mixed |
| 10⁰ m | Human-scale object | Irregular | Mixed |
| 10³ m | Mountain/structure | Weak coherence | R₂ approx |
| 10⁶ m | Planet | Sphere | R₂ |
| 10⁹ m | Star system | Sphere (Hill sphere) | R₂ |
| 10¹³ m | Solar system disk | Torus | R₄ |
| 10¹⁷ m | Interstellar medium | Nebula-like (diffuse) | Pure rational? |
| 10²⁰ m | Galactic disk | Torus | R₄ |
| 10²¹ m | Galactic halo | Sphere | R₂ |
| 10²³ m | Galaxy cluster | Sphere (virialized) | R₂ |
| 10²⁴ m | Filament | Elongated (cylinder?) | R₂ variant |
| 10²⁵ m | Void | Anti-boundary (r > 1?) | Unknown |
| 10²⁶ m | Observable universe | Sphere (horizon) | R₂ |

That is approximately 20 distinct boundary types across 40 orders of magnitude. To describe GR from QED, the transformation law must run through ALL of these boundaries, accumulating the correction at each crossing. This is the VP running from PHYS-5/9, extended across the entire hierarchy.

---

### 3. WHY QED CANNOT REACH GR IN REALS

The QED perturbative series is discrete. Each coefficient A_n is an exact rational combination of transcendentals (PHYS-9). The series is evaluated at a specific value of α/π ≈ 2.3 × 10⁻³. The series converges because each term is suppressed by (α/π)^n ≈ (2.3 × 10⁻³)^n.

GR is formulated in continuous real-number geometry. The metric g_μν is a smooth tensor field. The Einstein equations are differential equations on a manifold. There is no discrete series, no expansion parameter, no term-by-term structure.

Attempting to describe GR from QED means: take the discrete QED transformation law, run it through 20+ boundary layers (each modifying the coefficients by exact rationals), accumulate the corrections, and arrive at a description that looks like continuous real-number geometry.

The problem: the cumulative product of exact rationals across 20+ boundary layers, each involving different geometric classes (R₂ for spheres, R₄ for tori, pure rationals for irregular boundaries, Bessel zeros for disk modes), produces a number in a transcendental class that no finite combination of known transcendentals can describe (the Bessel zero barrier, 82/82 PSLQ null). Computing in reals — floating-point approximations to this composite transcendental — loses the discrete structure that makes QED work.

This is the diagnosis: QED-to-GR fails not because the theories are incompatible, but because the running between them crosses so many boundaries that the cumulative correction cannot be expressed in any single transcendental class. The computation WOULD work in exact rational arithmetic (every individual correction is a rational), but the PRODUCT of all corrections is a number that real-number arithmetic cannot distinguish from nearby values. The precision required to track the discrete structure through 40 orders of magnitude exceeds what floating-point reals can provide.

The analogy to the A₄ wall from PHYS-9: A₄ is known to 1100 digits but not fully decomposed analytically because the 4-loop Feynman integrals involve elliptic integrals (a new transcendental class). The QED-to-GR computation would involve ALL transcendental classes simultaneously (R₂, R₄, Bessel zeros, elliptic integrals, and potentially classes that haven't been named) because it crosses ALL boundary types. The 4-loop wall is the first hint of what happens at higher boundary count.

---

### 4. THE CONFINEMENT WALL AS THE FIRST OBSTRUCTION

PHYS-6 identified the confinement wall at ~0.3-2 GeV: the domain where perturbative QCD fails and α_s grows to O(1). This is the first boundary that QED cannot cross perturbatively. The VP running (PHYS-5) stops at this wall and must use measured data (the R-ratio) to bridge across.

In the soliton hierarchy, the confinement wall is the boundary between the subatomic domain (quarks as perturbative degrees of freedom) and the hadronic domain (protons, neutrons, pions as composite solitons). It is the FIRST scale transition that QED encounters on its way toward GR.

The fact that the first transition already requires measured data (non-perturbative) rather than computed correction is diagnostic. If the FIRST boundary crossing requires abandoning perturbation theory, the 20th boundary crossing (across the galactic disk, say) is exponentially harder. Each boundary type potentially introduces its own confinement-like obstruction where the correction cannot be computed perturbatively and must be measured.

The confinement wall factor of 64 (between free u-quark threshold at 4.4 MeV and pion threshold at 280 MeV) eliminates one domain of the energy axis. Each subsequent wall eliminates its own domain. The cumulative elimination narrows the range of energies where perturbative computation works. By the time you reach planetary scales, the perturbative range may be exhausted — there may be no energy window where all corrections can be computed rather than measured.

This is why GR looks non-perturbative from the QED perspective: by the time QED's transformation law has been run through all the intermediate walls, the perturbative expansion has broken down so many times that the result looks like a completely different theory. The smooth continuous geometry of GR is the LIMIT of the discrete QED corrections after all perturbative structure has been averaged out by repeated wall crossings.

---

### 5. GR-TO-QED HAS THE SAME PROBLEM IN REVERSE

GR describes smooth spacetime geometry. To reach the QED domain, it must resolve that geometry down to the subatomic scale. This means: take the continuous metric and follow it inward through all the soliton boundaries from cosmological to subatomic.

At each boundary crossing going inward, the continuous description encounters increasing quantum effects. The Heisenberg uncertainty ΔxΔp ≥ ℏ/2 means that below a certain scale, the position uncertainty exceeds the soliton size, and the continuous geometry description breaks down. This is the standard "quantum gravity becomes important at the Planck scale" argument, but the soliton framework localizes the breakdown more precisely: GR breaks down not at a single Planck scale but at EACH boundary crossing where the quantum uncertainty exceeds the boundary thickness.

The first boundary GR encounters going inward is the atomic scale (~10⁻¹⁰ m), where quantum mechanics already dominates. GR cannot describe atomic structure perturbatively. The second is the nuclear scale (~10⁻¹⁵ m), where the strong force dominates. GR cannot describe nuclear structure at all.

The structural parallel is exact: QED going outward hits the confinement wall at the hadronic boundary. GR going inward hits the quantum wall at the atomic boundary. Both encounter their first obstruction within a few orders of magnitude of their natural domain. Both would need to cross through 20+ additional boundary types to reach the other theory's natural domain.

---

### 6. THE CURVE OF EVERY SOLITON RUNNING CROSSING

The author's concept: compute the correction curve at each boundary crossing, including the inner geometric structure (the shells from the modulus superset notebook), and track the total running between QED and GR.

This would require:

**For each boundary type** (VP cloud, proton, atom, molecule, ..., galaxy, cluster, void):

1. The boundary geometry (sphere, torus, irregular → determines R₂/R₄/rational correction type)
2. The internal shell structure (density profile → determines the functional form of the correction within the boundary)
3. The coupling to the electromagnetic field (how much does the EM coupling change on crossing this boundary?)
4. The coupling to the gravitational field (how much does the effective G change on crossing?)

**The key question:** does the gravitational coupling G run through soliton boundaries the way the electromagnetic coupling α runs through VP thresholds?

PHYS-3 established: G has never been measured outside Earth's Hill sphere. The reproducibility of G measurements on Earth does not prove G is universal — it proves G is consistent WITHIN ONE BOUNDARY LAYER. The series proposed an L1/L2 experiment (measure G outside Earth's Hill sphere) to test this.

If G runs: then the QED-to-GR connection is a running curve analogous to α(μ), but running through SPATIAL boundaries rather than energy thresholds. The curve H₀(d) from the Hubble tension is a direct manifestation: H₀ ∝ √(G × ρ) in Friedmann cosmology, so if G runs with distance (boundary count), H₀ runs with distance.

If G does NOT run: then gravity truly is different from the gauge forces, and the soliton boundary picture applies to gauge couplings but not to gravity. This would be a PHYS-4 kill switch outcome for the gravitational extension.

---

### 7. THE FRACTIONAL GEOMETRY COMPUTATION

The inner geometric curves of each soliton boundary are determined by the boundary's mode structure. For a spherical boundary of radius R with density profile ρ(r):

- The electromagnetic correction involves the VP function integrated over the density profile: Δα(crossing) = ∫ (α/(3π)) × (density factor) × (geometric factor) dr
- The geometric factor involves R₂ through the VP step size 1/(12R₂)
- The density profile ρ(r) is determined by the soliton's mode spectrum (Bessel for disk, Legendre for sphere, etc.)

For the TOTAL running from QED domain to GR domain:

α_eff(GR scale) = α(QED scale) × Π_boundaries [1 + Δα(crossing_i)]

G_eff(QED scale) = G(GR scale) × Π_boundaries [1 + ΔG(crossing_i)]

Each product runs over all boundaries between the two scales. Each Δα or ΔG is a rational correction from the boundary's geometry. The product is the "curve of every soliton running crossing" — the total transformation from QED to GR.

The computation is in principle tractable:
1. Enumerate the boundary types between 10⁻¹³ m and 10²⁶ m (approximately 20 types)
2. For each type, compute the per-crossing correction from the boundary geometry
3. For each type, estimate the number of crossings (how many protons, atoms, molecules, planets, galaxies does a photon encounter?)
4. Multiply all corrections

The result would be a number — the ratio α_eff(GR)/α(QED) and G_eff(QED)/G(GR) — that quantifies the running between the two theories. If this number is ~1 (the corrections are tiny and nearly cancel), then QED and GR are approximately compatible as they are. If this number is significantly different from 1, it predicts measurable deviations from either QED or GR at scales where the running has accumulated appreciably.

---

### 8. LEMU ASSESSMENT

**L (Logic):** The logic follows from established premises: couplings run (PHYS-2), boundaries modify running rules (PHYS-14), each boundary type has a specific correction (modulus superset notebook). The extension to the QED-GR connection is a logical extrapolation. BUT: the assumption that G runs through spatial boundaries (rather than only through energy thresholds) is an additional hypothesis not established in the series. Logic passes with this caveat.

**E (Empirical):** G has not been tested outside the Hill sphere (PHYS-3). The Hubble tension may be evidence of running. The Pioneer anomaly (anomalous deceleration of Pioneer 10/11 beyond Saturn's orbit) was a candidate but was explained by thermal radiation pressure in 2012. No direct evidence for G running exists. Empirical gate: OPEN — neither confirmed nor falsified.

**M (Math):** Not computed. The per-boundary corrections for most boundary types (atomic, molecular, planetary, galactic) have not been estimated. The number of boundary crossings per line of sight has not been computed. The product has not been evaluated. Math gate: OPEN.

**U (Utility):** Extremely high IF the math passes. It would: provide a concrete, computable path from QED to GR (instead of an abstract "quantum gravity" problem), predict measurable G running testable by the L1/L2 experiment from PHYS-3, connect the Hubble tension to the quantum gravity problem through the same running framework, explain WHY quantization of gravity fails in perturbation theory (too many wall crossings break perturbation theory before the computation reaches GR's domain), and unify the series' particle physics and cosmological threads.

If the math fails (the corrections are negligibly small, or they cancel exactly, or the product doesn't converge): the QED-GR connection through soliton boundaries is falsified, and the quantum gravity problem remains separate from the soliton framework.

---

### 9. THE SERIES CONNECTIONS

**PHYS-1:** Mass is inertia. The proton gets 99% of its mass from binding energy (pattern maintenance energy). If the gravitational coupling G responds to this pattern energy, then G is sensitive to the soliton structure — it SHOULD run through boundaries where the pattern energy changes.

**PHYS-2:** The transformation law is fundamental. The QED transformation law (the perturbative series) and the GR transformation law (the Einstein equations) are both integer-based. QED: A₁ = 1/2, A₂ = rational × MATH-2, etc. GR: the Einstein tensor G_μν = 8πG T_μν has the integer 8 and π from the geometric content. Both laws are integers. The running between them preserves the integer structure at each step — only the VALUES change.

**PHYS-3:** G untested outside Hill sphere. The L1/L2 experiment is the direct test. If G runs, the running is detectable at L2 (~1.5 million km from Earth, outside the Hill sphere). The predicted running magnitude depends on the per-boundary correction, which is the quantity this notebook aims to compute.

**PHYS-6:** Confinement wall. The first QED → GR obstruction. The wall's characteristic — perturbation theory fails, measurement replaces computation — may repeat at every subsequent boundary type. The number of confinement-like walls between QED and GR determines how much of the total running can be computed vs measured.

**PHYS-11:** R₂ universality. Every boundary involving a circle/sphere has R₂ = π/4 in its correction. Most of the 20 boundary types are approximately spherical (VP cloud, atom, planet, star, halo, cluster). The R₂ dominance means the per-boundary correction has a universal geometric factor, with the specifics encoded in the boundary's mass, radius, and density profile.

**PHYS-12:** The A₂ decomposition. The geometric piece (R₄) dominates at 8× the net value, with 87% cancellation. If the QED-to-GR running has similar cancellations at each boundary (the R₂ correction nearly cancels against the density correction), the NET running could be tiny even though the individual corrections are large. This would explain why G appears constant despite the running existing: the cancellation at each boundary makes the accumulated running small enough to be within current measurement precision.

**PHYS-14:** Fermion generations cancel from the gap ratio. This is the most relevant structural parallel: complete generations contribute nothing to the RATIO of coupling differences. If the soliton hierarchy has analogous "complete sets" of boundary types that cancel from the running ratio, the QED-to-GR running could be much simpler than the full product suggests. The running might depend only on the ASYMMETRIC boundaries (like the VL doublet provides asymmetric beta contributions), not on the total boundary count.

---

### 10. THE PREDICTION

If the soliton running framework applies to the QED-GR connection, then:

**P1.** G should run detectably between Earth's surface and L2 (~1.5 million km). The running magnitude is of order (1 − r_Hill) where r_Hill is the Hill sphere boundary correction. From the Hubble tension curve (r ≈ 0.9992 per ~100 boundaries), a single boundary correction is of order 10⁻⁵ to 10⁻⁴. The L2 G measurement would need precision of ~10⁻⁵ to detect this. Current G measurement precision is ~10⁻⁵ (CODATA 2022: G known to 22 ppm). The prediction is at the edge of current precision — detectable with next-generation experiments.

**P2.** The QED perturbative series should show anomalies at the loop order where the loop momentum traverses a soliton boundary. The 4-loop A₄ already involves elliptic integrals — a new transcendental class associated with toroidal topology. The 5-loop A₅ (where two independent calculations disagree at 5σ — PHYS-9 Section 10.3) might involve boundary-crossing corrections not accounted for in standard QED.

**P3.** The Hubble tension, the G running, and the QED-GR incompatibility are THREE MANIFESTATIONS of the same phenomenon: the cumulative soliton boundary correction across the hierarchy. Solving any one constrains the other two. The per-transit correction ε that resolves the Hubble tension ALSO predicts the G running at L2 and the QED loop correction at high order.

---

**End of notebook. Status: active, highest-level conceptual connection in the series. Links the Hubble tension (cosmological), the gap ratio (particle physics), and the quantum gravity problem (foundational physics) through the common mechanism of soliton boundary running. All three Math gates OPEN — the per-boundary correction formula is the critical unknown. Updated: Session 4, April 2 2026.**
