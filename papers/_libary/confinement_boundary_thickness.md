# Boundary Thickness as Structural Property: Exploration Notebook

**Status:** Active exploration. First-pass analysis complete. Connections identified. Computations partially executed.

**Date:** April 15, 2026

**Origin:** During the DISC-13 supplementary writing, the sentence "The boundary thickness is 1/|b₃| didn't need explanation" triggered the recognition that this statement was accepted without examination. It *should* need explanation. Why is the thickness the reciprocal of the absolute beta coefficient? What does this quantity physically mean? Does it generalize? What does it predict?

---

## I. THE CLAIM

PHYS-45 defined boundary thickness as 1/|b| for each gauge sector. The values:

| Sector | b (SM) | Thickness SM | b (CD) | Thickness CD |
|---|---|---|---|---|
| SU(3) strong | −7 | 1/7 = 0.14286 | −20/3 | 3/20 = 0.15000 |
| SU(2) weak | −19/6 | 6/19 = 0.31579 | −13/6 | 6/13 = 0.46154 |
| U(1) EM | 41/10 | 10/41 = 0.24390 | 25/6 | 6/25 = 0.24000 |

These were presented as exact fractions, verified by the experiment runner, and accepted as structural properties of the boundaries. The paper stated: "A larger |b₃| means α_s runs faster, meaning the transition from perturbative to non-perturbative is sharper — the boundary is thinner."

The claim is physically intuitive. A coupling that runs fast reaches criticality over a narrow energy range — thin boundary. A coupling that runs slow reaches criticality over a wide energy range — thick boundary. The reciprocal of the running rate gives the width of the transition zone in units of the logarithmic energy scale.

But "physically intuitive" is not a derivation. This notebook examines what 1/|b| actually measures, whether it's the right definition, and what it implies.

---

## II. WHAT 1/|b| ACTUALLY IS

The one-loop running of a gauge coupling is:

α⁻¹(μ₂) = α⁻¹(μ₁) − b/(2π) × ln(μ₂/μ₁)

Rearranging for the energy range over which α⁻¹ changes by one unit:

Δ(ln μ) = 2π/|b|

This is the number of e-foldings (factors of e ≈ 2.718 in energy) required for the inverse coupling to change by 1. It's a logarithmic width.

So 1/|b| is proportional to the energy range (in log space) over which the coupling changes by a fixed amount. Specifically:

- 1/|b| is the change in α⁻¹ per unit of ln(μ)/(2π)
- Or equivalently, 2π/|b| is the change in ln(μ) per unit change in α⁻¹

The factor of 2π is conventional — it comes from the standard normalization of the beta function. The structurally meaningful quantity is 1/|b|, which strips the convention and leaves the pure ratio: how much does the coupling change per logarithmic decade of energy?

This means 1/|b| is not just a label we're attaching to boundaries. It is the actual logarithmic derivative of the inverse coupling:

d(α⁻¹)/d(ln μ / 2π) = −b → the coupling changes at rate |b| per unit of rescaled log energy

The boundary thickness 1/|b| is the reciprocal of this rate. It is the energy scale width (in natural logarithmic units) over which the coupling transitions through one unit of inverse coupling strength.

---

## III. WHAT "THICKNESS" MEANS PHYSICALLY

A soliton boundary is where the coupling transitions from weak (perturbative, calculable) to strong (non-perturbative, confining or symmetry-breaking). The thickness measures how gradually this transition occurs.

**Thin boundary (small 1/|b|, large |b|):** The coupling runs fast. It goes from perturbative to non-perturbative over a narrow energy range. The transition is sharp. Crossing the boundary is abrupt. You're outside, and then suddenly you're inside. The strong force in the SM has thickness 1/7 ≈ 0.143 — the thinnest gauge boundary. Confinement is sharp.

**Thick boundary (large 1/|b|, small |b|):** The coupling runs slowly. The transition from perturbative to non-perturbative is spread over a wide energy range. The boundary is gradual. There's a broad crossover zone where you're neither fully inside nor fully outside. The weak force with CD modification has thickness 6/13 ≈ 0.462 — the thickest gauge boundary. Electroweak symmetry breaking is gradual.

The physical consequences of thickness:

**For confinement (SU(3)):** A thin boundary means quarks go from nearly free to completely confined over a narrow energy window. Perturbation theory works well above the boundary and fails completely below it. The transition zone — where neither perturbative QCD nor hadronic models work perfectly — is narrow. This is why the confinement problem is hard: there's almost no overlap between the two descriptions.

**For electroweak symmetry breaking (SU(2)):** A thicker boundary means the transition from unbroken SU(2) to broken electroweak is more gradual. The energy range where both the symmetric and broken descriptions are partially valid is wider. This is why electroweak corrections are perturbatively calculable — the boundary is thick enough that you never fully leave the perturbative regime.

**For electromagnetism (U(1)):** The EM coupling runs in the opposite direction (b₁ is positive — the coupling gets stronger at higher energy, not weaker). The thickness 10/41 ≈ 0.244 measures how gradually the screening of electric charge by virtual particle-antiparticle pairs increases as you zoom in. The EM "boundary" is not a confinement boundary — it's a screening boundary. It's the rate at which the vacuum polarization reveals the bare charge.

---

## IV. THE CD CHANGES EVERY THICKNESS

The CD shifts all three beta coefficients, which shifts all three thicknesses. The shifts are not uniform:

| Sector | Δb | |b| SM | |b| CD | Thickness change | Why this magnitude |
|---|---|---|---|---|---|
| SU(3) | +1/3 | 7 | 20/3 | +5.0% thicker | Small Δb relative to large |b| |
| SU(2) | +1 | 19/6 | 13/6 | +46.2% thicker | Large Δb (full unit) relative to moderate |b| |
| U(1) | +1/15 | 41/10 | 25/6 | −1.6% thinner | Tiny Δb relative to large |b| |

The hierarchy of changes mirrors the CD's quantum numbers. The CD is an SU(2) doublet — it transforms as a 2 under the weak force, giving the largest beta shift (+1). It's an SU(3) triplet with a vector-like pair — moderate shift (+1/3). It has hypercharge 1/6 — the smallest quantum number in the SM quantization, giving a tiny shift (+1/15).

The weak boundary getting 46% thicker is the largest structural change the CD produces. This is worth examining. A 46% thicker electroweak boundary means the transition from unbroken to broken electroweak symmetry is substantially more gradual. This affects:

- The electroweak phase transition in the early universe (was it first-order or crossover?)
- Electroweak baryogenesis (can the matter-antimatter asymmetry be generated at the EW scale?)
- The Higgs potential's running (how quickly does the quartic coupling change near the EW scale?)

Each of these is a major open question in particle physics. The CD's effect on the EW boundary thickness — 46% thicker — may be relevant to all of them.

---

## V. THICKNESS RATIOS

The ratios between thicknesses are themselves exact fractions.

**SM thickness ratios:**

| Pair | Ratio | Fraction | Decimal |
|---|---|---|---|
| SU(2)/SU(3) | (6/19)/(1/7) | 42/19 | 2.2105 |
| U(1)/SU(3) | (10/41)/(1/7) | 70/41 | 1.7073 |
| U(1)/SU(2) | (10/41)/(6/19) | 190/246 = 95/123 | 0.7724 |

**CD thickness ratios:**

| Pair | Ratio | Fraction | Decimal |
|---|---|---|---|
| SU(2)/SU(3) | (6/13)/(3/20) | 120/39 = 40/13 | 3.0769 |
| U(1)/SU(3) | (6/25)/(3/20) | 120/75 = 8/5 | 1.6000 |
| U(1)/SU(2) | (6/25)/(6/13) | 78/150 = 13/25 | 0.5200 |

Every ratio is an exact fraction. The CD changes every ratio. The SU(2)/SU(3) ratio goes from 42/19 ≈ 2.21 to 40/13 ≈ 3.08 — the weak boundary becomes 39% thicker relative to the strong boundary. The U(1)/SU(3) ratio goes from 70/41 ≈ 1.71 to 8/5 = 1.60 — the EM boundary becomes 6% thinner relative to the strong boundary.

The CD ratio 8/5 for U(1)/SU(3) is notable. 8/5 is a simple fraction. 70/41 is not. The CD simplifies this ratio. Whether this simplification has physical meaning — whether the CD makes the relationship between electromagnetic screening and strong confinement structurally cleaner — is an open question.

---

## VI. THICKNESS AND THE SECTOR SPLITTING

PHYS-44 predicted sector splitting: a nuclear clock and an optical clock at different altitudes should disagree because different force sectors have different beta coefficients. The splitting formula is:

ε = κ|Δβ|ΔΦ/c²

where Δβ is the difference between beta coefficients for the two sectors, ΔΦ/c² is the gravitational potential difference, and κ is the conversion factor between the energy-scale hierarchy and the gravitational hierarchy.

The boundary thickness connects to sector splitting directly. The thickness IS the reciprocal of the beta coefficient magnitude. The difference in thicknesses between two sectors IS the difference in how gradually the two couplings run. The sector splitting measures whether this difference in running rates produces a measurable difference in clock rates at the same gravitational potential.

Reformulating in terms of thickness:

|Δβ| = |b₃| − |b₁| = 7 − 41/10 = 29/10 (SM)

The corresponding thickness difference:

ΔT = 1/|b₁| − 1/|b₃| = 10/41 − 1/7 = (70 − 41)/287 = 29/287 (SM)

This is not the same as |Δβ|. The relationship is:

ΔT = |Δβ| / (|b₁| × |b₃|)

The thickness difference is the beta difference divided by the product of the absolute betas. This means the sector splitting depends not just on how different the running rates are, but on how fast each sector runs individually. Two sectors with very different betas but both running fast (large |b|) have a small thickness difference. Two sectors with moderately different betas but both running slowly (small |b|) have a large thickness difference.

For the strong-EM pair:

| Quantity | SM | CD |
|---|---|---|
| \|Δβ\| | 29/10 | \|−20/3 − 25/6\| = \|−65/6\| = 65/6 |
| \|b₁\| × \|b₃\| | (41/10)(7) = 287/10 | (25/6)(20/3) = 500/18 = 250/9 |
| ΔT | 29/287 = 0.1011 | (65/6)/(250/9) = (65×9)/(6×250) = 585/1500 = 39/100 = 0.39 |

Wait — this needs checking. The CD changes the sign structure. Let me recompute.

SM: |b₃| = 7, |b₁| = 41/10 = 4.1. Since |b₃| > |b₁|, the strong sector has the thinner boundary.

CD: |b₃| = 20/3 ≈ 6.667, |b₁| = 25/6 ≈ 4.167. Still |b₃| > |b₁|, strong still thinner.

ΔT(SM) = 1/|b₁| − 1/|b₃| = 10/41 − 1/7 = (70 − 41)/(41×7) = 29/287 ≈ 0.1011

ΔT(CD) = 6/25 − 3/20 = (24 − 15)/100 = 9/100 = 0.0900

The CD actually *decreases* the thickness difference between the EM and strong sectors. The boundaries become more similar in thickness. This is because the CD's +1/3 to b₃ makes the strong boundary thicker (closer to the EM boundary's thickness) while the CD's +1/15 to b₁ barely changes the EM boundary.

For the sector splitting prediction, this matters. A smaller thickness difference might mean a smaller splitting signal. The relationship between thickness difference and splitting magnitude depends on the conversion factor κ, which is the unknown. But the direction is clear: the CD makes the strong and EM boundaries more similar in thickness, which should reduce the strong-EM sector splitting.

The weak-EM pair tells a different story:

ΔT(SM) = 6/19 − 10/41 = (246 − 190)/(19×41) = 56/779 ≈ 0.0719

ΔT(CD) = 6/13 − 6/25 = (150 − 78)/(13×25) = 72/325 ≈ 0.2215

The CD *increases* the weak-EM thickness difference by 3×. If the sector splitting depends on thickness difference rather than beta difference directly, the weak-EM pair becomes a much better test than the strong-EM pair in the CD theory.

This might change which clock comparison is the most sensitive test. PHYS-44 proposed thorium-229 (nuclear, probing strong sector) versus strontium-87 (optical, probing EM sector). If the relevant quantity is thickness difference rather than beta difference, a clock probing the weak sector versus an optical clock might give a larger signal. The question is whether any clock directly probes the weak sector. Weak interactions are involved in beta decay — a beta-decay clock (neutron lifetime measurement) versus an optical clock might be the test.

---

## VII. THICKNESS AND THE SEMI-PERTURBATIVE WINDOW

The speculative report preceding PHYS-45 noted that a thicker confinement boundary might widen the semi-perturbative window — the energy range where perturbation theory is failing but not yet completely useless.

This can now be quantified. The semi-perturbative window extends from the scale where α_s becomes "large" (say, α_s > 0.3, where perturbative corrections become comparable to leading-order terms) to the scale where α_s diverges (Λ_QCD).

From the PHYS-45 running table:

| Scale | α_s (SM) | α_s (CD) |
|---|---|---|
| m_c = 1.27 GeV | 0.319 | 0.321 |
| 1 GeV | 0.358 | 0.361 |
| Λ_QCD | ∞ (at 142.5 MeV SM, 145.4 MeV CD) | ∞ |

The semi-perturbative window (α_s > 0.3 to α_s → ∞) spans from ~1.3 GeV to ~143 MeV (SM) or ~145 MeV (CD). In log space:

Window(SM) = ln(1273/142.5) = ln(8.93) = 2.189

Window(CD) = ln(1273/145.4) = ln(8.75) = 2.170

The difference is small — the CD barely changes the semi-perturbative window width. The 5% thickness increase translates to a ~1% window change. The speculation that the CD significantly widens the semi-perturbative window is not supported by the numbers.

This is a useful negative result. It means the CD's effect on confinement operates through the coupling value at M_Z (which propagates to a 2% shift in Λ_QCD), not through the transition shape. The boundary is 5% thicker but the window is only 1% wider. The thickness change is real but its practical consequences for calculability are minimal.

---

## VIII. THICKNESS AS SOLITON PROPERTY

The boundary thickness is a property of the boundary, not a reading at the boundary. This distinction is important.

A reading changes across the hierarchy. α_s reads 0.118 at M_Z and ~1 near confinement. The reading depends on where you are. Different observers at different energy scales get different readings. This is the running.

The thickness 1/|b| does not change with energy scale (at one-loop). It is a construction parameter set by the gauge group and the particle content. The confinement boundary has thickness 1/7 whether you measure it at CERN, at Fermilab, or in a neutron star. It is a property of the boundary itself.

This makes thickness fundamentally different from every other quantity in the framework so far. The 53 derived values in the book are all readings — values at specific boundaries or running between boundaries. Thickness is not a reading. It is a property of the object that produces readings. It is a property of the infrastructure, not a property of the measurement.

In the soliton vocabulary: readings are what you get when you measure the pattern. Thickness is a property of the pattern itself. The proton's mass is a reading at the confinement boundary — it depends on Λ_QCD, which depends on where the boundary sits, which depends on the coupling's value at a reference scale. The confinement boundary's thickness is 1/7 regardless of where the boundary sits. Move Λ_QCD up or down (by changing α_s at M_Z, or by adding particles like the CD), and the boundary moves. But its thickness stays 1/7 (SM) or changes to 3/20 (CD) based on the particle content, not on the boundary's position.

This suggests a classification:

| Category | What it is | Changes with | Examples |
|---|---|---|---|
| Reading | Value at a boundary | Position/energy scale | α_s(M_Z) = 0.118, Φ/c² at Earth |
| Running | Rate of change between boundaries | Particle content at that scale | b₃ = −23/3 between m_b and m_t |
| Thickness | Reciprocal of running rate | Particle content only | 1/7 for SU(3) with 6 flavors |
| Topology | Structural property of the soliton | Nothing (?) | Genus 0 for sphere, genus 1 for toroid |

Thickness sits between running (which depends on what particles are active at a given scale) and topology (which depends on nothing known). Thickness depends on particle content — add the CD and it changes — but not on energy scale. It is a structural property that is more stable than a reading but less fundamental than topology.

If the Koide amplitude a² connects to topology (counting stable soliton geometries), and thickness connects to particle content (counting active fields), then the mass hierarchy might involve both: the topology sets the Koide relation (how many modes, what symmetry), and the thickness sets the energy spacing between modes (how far apart the boundaries are in log energy).

---

## IX. THICKNESS AT TWO LOOPS

The one-loop thickness 1/|b| is exact because b is exact. But real couplings run at two loops, three loops, and beyond. At two loops, the running equation becomes:

dα⁻¹/d(ln μ) = −b/(2π) − b'α/(4π²)

where b' is the two-loop coefficient. The effective running rate is now scale-dependent — it changes as α changes. This means the effective thickness is also scale-dependent at two loops.

Near the boundary (where α is large), the two-loop correction term becomes significant. The effective |b_eff| = |b + b'α/(2π)| is larger than |b| alone (for asymptotically free theories where b and b' have the same sign). This means the effective thickness is *thinner* at two loops than at one loop near the boundary — the transition is sharper than the one-loop picture suggests.

Far from the boundary (where α is small), the two-loop correction is negligible and the thickness approaches the one-loop value 1/|b|.

The one-loop thickness 1/|b| is therefore the *asymptotic* thickness — what the boundary looks like from far away. The actual thickness near criticality is thinner. The one-loop value is an upper bound on the transition width.

This means the 5% difference between SM and CD thickness (1/7 vs 3/20) is the difference as seen from high energies. Near the confinement scale itself, the two-loop corrections make both boundaries thinner, and the relative difference may change. Whether the CD's 5% thickness increase survives at two loops depends on the ratio of two-loop corrections, which involves the b_ij matrix elements already in the pool.

**Computation needed:** Run the effective thickness at the confinement scale using two-loop b_ij values. All inputs are in the pool. One derivation function.

---

## X. THICKNESS AND PHASE TRANSITIONS

The thickness of a boundary determines whether the phase transition it mediates is sharp or smooth. In thermodynamic language:

- Thin boundary → first-order phase transition (sharp discontinuity, latent heat, bubbles)
- Thick boundary → crossover (smooth, no discontinuity, no latent heat)

The electroweak phase transition is currently believed to be a crossover in the Standard Model — too smooth for electroweak baryogenesis to work. The SM electroweak boundary thickness is 6/19 ≈ 0.316. The CD makes it 6/13 ≈ 0.462 — 46% thicker. This pushes the transition *further from* first-order, making baryogenesis *harder*, not easier.

This is a concrete falsifiable consequence of the thickness. If the CD exists and the electroweak phase transition must be first-order for baryogenesis, the CD makes this harder. Either baryogenesis happens by a different mechanism (leptogenesis, which occurs at higher scales), or the CD's effect on the EW boundary is offset by other contributions (the CD's Yukawa coupling to the Higgs might modify the Higgs potential in ways that counteract the beta shift).

The confinement phase transition is different. QCD with physical quark masses undergoes a crossover (not first-order) from quark-gluon plasma to confined hadrons. The SM confinement thickness 1/7 ≈ 0.143 is thin, yet the transition is still a crossover because the light quark masses explicitly break the chiral symmetry that would make it first-order. The CD's 5% thickening (to 3/20 = 0.150) doesn't change the qualitative nature of the transition.

**Open question:** Is there a critical thickness below which a boundary mediates a first-order transition and above which it mediates a crossover? If so, does this critical thickness depend on the gauge group, the particle content, or the explicit symmetry breaking? The thickness values from PHYS-45 (1/7, 6/19, 10/41 and their CD-modified counterparts) provide six data points for this question.

---

## XI. GENERALIZING BEYOND GAUGE BOUNDARIES

The gauge boundaries have exact fractional thicknesses because their beta coefficients are exact fractions. Can the thickness concept extend to non-gauge boundaries?

**The gravitational boundary.** Gravitational "running" is described by GM/(Rc²) changing with R. The "beta coefficient" analog is dΦ/d(ln R) = −GM/(Rc²). This isn't from group theory — it's from geometry. It depends on M and R, which are specific to each body. Earth's gravitational boundary has a different "thickness" than Jupiter's. The thickness is not a universal construction parameter — it's body-specific.

However, the *ratio* of gravitational thicknesses between two bodies might be universal if it depends only on mass ratios. Earth/Jupiter thickness ratio = (M_J/R_J)/(M_E/R_E) × (R_E/R_J). This involves mass-to-radius ratios, which for gravitationally rounded bodies follow specific scaling relations. Whether these scaling relations produce exact fractions is unknown but testable.

**The atomic boundary.** The atomic binding energy is E_ion = α²m_e/2 = 13.6 eV. The "running" of α_em below M_Z is negligible (~1% total change from M_Z to atomic scales). The atomic boundary has effectively infinite thickness — the coupling barely changes across it. This is why atoms are atoms everywhere. The atomic boundary is not a transition from perturbative to non-perturbative. It's a binding threshold in an essentially constant coupling. The thickness concept doesn't apply in the same way.

**The nuclear boundary.** The nuclear force is mediated by pion exchange, which is a derivative of the confinement boundary. The "running" of the nuclear force is the running of the pion-nucleon coupling, which inherits its scale dependence from α_s through the pion mass. The nuclear boundary thickness is a derived quantity — it inherits the confinement boundary's thickness through the pion. This chain (confinement thickness → pion properties → nuclear force range → nuclear boundary thickness) is computable but has not been computed.

**The biological boundaries.** The soliton hierarchy extends through cellular, tissue, organ, and organism levels. Do these boundaries have a meaningful thickness? The "coupling" at biological scales is not a gauge coupling — it's metabolic rate, signal strength, binding affinity. The "running" is how these quantities change across the boundary. The "thickness" would be the range over which the transition occurs.

For a cell membrane: the transition from inside (cytoplasm) to outside (extracellular fluid) occurs over ~7-8 nm (the lipid bilayer width). This is a physical thickness, not a logarithmic one. Whether it's meaningful to define a dimensionless thickness analogous to 1/|b| for biological boundaries requires identifying what plays the role of the beta coefficient — the rate at which the "coupling" (whatever that is at biological scale) changes across the boundary.

This is speculative. But the question is well-posed: does the 1/|b| structure generalize to non-gauge boundaries, and if so, what plays the role of b?

---

## XII. SUMMARY OF FINDINGS

| Finding | Status | What it means |
|---|---|---|
| 1/\|b\| = logarithmic energy width per unit α⁻¹ change | Derived | Thickness has a precise mathematical meaning, not just intuition |
| All thicknesses are exact fractions | Verified (PHYS-45) | Construction parameters, not readings |
| CD changes SU(2) thickness by 46% | Computed | Largest structural change from the CD |
| CD changes SU(3) thickness by 5% | Computed | Moderate, propagates to hadron properties |
| CD barely changes U(1) thickness (−1.6%) | Computed | Smallest shift, from tiny hypercharge 1/6 |
| Thickness ratios are exact fractions | Computed | CD simplifies U(1)/SU(3) ratio to 8/5 |
| Semi-perturbative window barely changes | Computed (negative result) | CD effect is through coupling value, not transition shape |
| Thickness is a boundary property, not a reading | Structural observation | New category between running and topology |
| Two-loop thickness is scale-dependent | Noted | One-loop thickness is asymptotic upper bound |
| EW thickness increase disfavors first-order phase transition | Physical consequence | Relevant to baryogenesis |
| Sector splitting relates to thickness difference | Connected to PHYS-44 | Weak-EM pair may give larger signal than strong-EM with CD |

---

## XIII. PATHS FORWARD

**Path 1: Two-loop effective thickness.** Compute 1/|b_eff(μ)| at μ = Λ_QCD using the two-loop b_ij matrix entries already in the pool. Determine whether the 5% SM-CD difference survives near the confinement scale. One derivation function.

**Path 2: Thickness and the electroweak phase transition.** Determine whether the CD's 46% thickening of the SU(2) boundary, combined with the CD's Yukawa coupling to the Higgs, strengthens or weakens the first-order nature of the EW phase transition. Requires finite-temperature field theory. Medium difficulty.

**Path 3: Thickness ratios and the clock test.** Reformulate the PHYS-44 sector splitting prediction in terms of thickness difference rather than beta difference. Determine which clock pair gives the largest signal in the CD theory. The weak-EM pair (ΔT = 0.22 with CD) may be more promising than the strong-EM pair (ΔT = 0.09 with CD). Requires identifying a "weak sector clock."

**Path 4: Nuclear boundary thickness.** Derive the nuclear force boundary thickness from the confinement thickness through the pion chain: 1/|b₃| → Λ_QCD → m_π → nuclear force range → nuclear boundary properties. All inputs in pool. Medium difficulty.

**Path 5: Critical thickness for phase transition order.** Determine whether there's a threshold value of 1/|b| that separates first-order transitions from crossovers. Six gauge boundary data points (three SM, three CD) provide initial constraints. Requires finite-temperature field theory and lattice data.

**Path 6: Thickness in the pool.** Add boundary thickness as a standard computed quantity for every gauge boundary. The values are already in PHYS-45 results. Promote them to named pool values (e.g., `boundary_thickness_su3_sm_v0 = Fraction(1,7)`) so future derivations can use them as inputs.

---

## XIV. KILL CONDITIONS

**K1.** If two-loop effective thickness at the confinement scale differs from one-loop thickness by more than a factor of 2, the one-loop thickness is a poor approximation and the PHYS-45 values need qualification.

**K2.** If the thickness difference ΔT between sectors has no computable relationship to the sector splitting magnitude ε, the connection proposed in Section VI is wrong.

**K3.** If the CD's 46% thickening of the SU(2) boundary is shown to have zero effect on the electroweak phase transition order (because the transition order is dominated by the Higgs potential, not the gauge running), the physical relevance of EW thickness is diminished.

**K4.** If thickness at biological boundaries has no meaningful analog to 1/|b| (because there is no identifiable beta coefficient at biological scales), the generalization in Section XI fails.

---

**Status:** Active. Mathematical meaning of 1/|b| established. Physical consequences partially computed. One negative result (semi-perturbative window barely changes). One potentially significant finding (weak-EM pair may be better for sector splitting than strong-EM). Multiple paths identified. Path 6 (add to pool) is immediate. Paths 1 and 3 are close. Paths 2 and 5 require external expertise.
