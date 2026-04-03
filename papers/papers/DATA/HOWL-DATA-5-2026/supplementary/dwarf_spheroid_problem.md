## Notebook: The Dwarf Spheroidal Problem

---

### 1. WHAT THE PROBLEM IS

Dwarf spheroidal galaxies (dSphs) are the most dark-matter-dominated objects in the universe. They have velocity dispersions of 5–15 km/s, visible masses of ~10⁶–10⁸ solar masses, and dynamical masses of ~10⁸–10¹⁰ solar masses. The DM/visible ratio is 10–1000, with typical values around 100.

In the toroidal DM script, this produces the following numbers:

- v²/c² ≈ 10⁻⁹ (at v_disp = 10 km/s)
- DM/visible ≈ 100
- Required amplification A = DM_ratio × 2c²/v² ≈ 1.8×10¹¹
- Galaxy amplification for comparison: ~2×10⁷

The dwarf needs 10,000× MORE amplification than a spiral galaxy, despite being a simpler, smaller, less energetic system. If the toroidal DM hypothesis requires stronger boundary effects in weaker systems, something is wrong with the scaling.

This is the single hardest challenge to any model that explains dark matter through the dynamics of visible matter (MOND, toroidal circulation, modified gravity). It is also the strongest evidence FOR particle dark matter — because particle DM naturally concentrates in small potential wells through gravitational accretion.

---

### 2. THE OBSERVATIONAL DATA

The classical dSphs of the Milky Way (Draco, Sculptor, Fornax, Carina, Sextans, Leo I, Leo II, Ursa Minor) and the ultra-faint dwarfs discovered by SDSS and DES (Segue 1, Reticulum II, Tucana II, etc.) share common properties:

**Kinematics:** Velocity dispersions σ ≈ 5–12 km/s (classical), 2–5 km/s (ultra-faint). No organized rotation. The stars move randomly within the system. The stellar motions are fully pressure-supported (dispersion-dominated), not rotation-supported.

**Visible mass:** 10⁴–10⁸ solar masses. The ultra-faints have as few as 100–1000 stars. The classical dSphs have 10⁵–10⁷ stars. All are dominated by old stellar populations — no gas, no ongoing star formation, no disk.

**Dynamical mass:** Computed from σ and the half-light radius r_h via the estimator M(r_h) ≈ 580 × σ² × r_h (Walker et al. 2009). This gives 10⁷–10⁹ solar masses for classicals, 10⁵–10⁷ for ultra-faints.

**The ratio:** DM/visible ranges from ~10 (Fornax) to ~1000+ (Segue 1). The median is around 100 for classical dSphs.

**Morphology:** Spheroidal (no disk), extended (r_h ~ 100–500 pc for classicals, 20–100 pc for ultra-faints), no substructure. These are featureless blobs of old stars embedded in enormous inferred dark matter halos.

---

### 3. WHY THIS BREAKS THE TOROIDAL MODEL

The toroidal DM hypothesis says: dark matter is the gravitational contribution of circulating energy in the galactic vortex. The mechanism requires:

1. Organized circulation (rotation or oscillation) that carries kinetic energy
2. Boundary amplification that converts a small v²/c² into a large effective mass ratio
3. The amplification factor scales with some property of the system

For dwarf spheroidals, problem #1 is fatal. There is no organized circulation. The stellar orbits are random — isotropic velocity dispersion with no net rotation. There is no disk, no spiral arms, no toroidal structure. The system is a pressure-supported sphere, not a rotation-supported torus.

If there is no torus, the toroidal model does not apply. The model cannot explain the system it most needs to explain — the one with the most dark matter.

The script's Section 10 offers four resolutions. Let me examine each.

---

### 4. RESOLUTION (a): TIDAL STRIPPING

**The argument:** Dwarf spheroidals orbit within the Milky Way's tidal field. Tidal forces strip the outer stars and gas, reducing the visible mass while leaving the dark matter halo (which extends further) mostly intact. The observed DM/visible ratio is inflated because the visible mass has been artificially reduced.

**Evidence for:** Some dSphs show tidal tails (e.g., Sagittarius dwarf). Simulations of tidal disruption show that stripped dwarfs can appear more DM-dominated than they were initially. The ultra-faint dwarfs may be remnant cores of larger systems.

**Evidence against:** The classical dSphs (Draco, Sculptor) show no obvious tidal features. Their velocity dispersion profiles are flat or rising with radius, consistent with extended dark matter halos, not stripped systems. The inferred DM mass is ~10⁹ solar masses — 100× the visible mass — and tidal stripping would need to have removed 99% of the visible matter while keeping the DM. This requires fine-tuning.

**In series language:** If tidal stripping explains the ratio, then the DM/visible ratio is not a property of the dwarf soliton — it is an artifact of the dwarf's interaction with the Milky Way's soliton. The boundary (R5) is not between "SM and DM" but between "dwarf" and "host galaxy." The amplification is not internal to the dwarf — it is imposed externally by tidal processing.

**Assessment:** Partially viable. Can explain some enhancement of the ratio. Cannot explain the full factor of 100–1000, especially for dwarfs with no tidal features.

---

### 5. RESOLUTION (b): DIFFERENT SOLITON STRUCTURE

**The argument:** Dwarfs are not toroids. They are spheroidal pressure-supported systems. The soliton structure is fundamentally different from a spiral galaxy. A spheroidal soliton has different boundary properties than a toroidal soliton.

**This is the most interesting resolution because it stays within the framework.** The series says every vortex has its own geometry, and the geometry determines the integer rules. A toroidal vortex (spiral galaxy) and a spheroidal vortex (dwarf) have different topologies, therefore different boundary amplification factors.

**What would be needed:** A derivation showing that spheroidal geometry produces stronger amplification per unit velocity than toroidal geometry. The scaling would need to be A_sphere/A_torus ~ 10⁴ to explain the dwarf/galaxy amplification ratio.

**Physical intuition:** In a torus, the circulation has a definite direction (the rotation curve). In a sphere, the motions are isotropic — every direction contributes equally. The "effective circulation" in a sphere might involve all three spatial directions simultaneously, whereas a torus uses primarily one. If the amplification scales with the number of independent circulation modes: sphere has 3 modes vs torus has 1 mode. This gives a factor of 3, not 10,000. Doesn't help.

**Alternative:** If amplification scales with the ratio of characteristic length to velocity dispersion (a dynamical time), then dwarfs (small r, small σ) could have very different amplification from galaxies (large R, large v_rot). But the dynamical times are similar: t_dyn = r/σ ~ 100 pc / 10 km/s ~ 10⁷ years for dwarfs, and t_dyn = 10 kpc / 220 km/s ~ 5×10⁷ years for spirals. Factor of 5, not 10,000.

**Assessment:** Conceptually valid within the framework but no quantitative derivation exists. The required factor of 10⁴ is very large — hard to get from geometric differences alone.

---

### 6. RESOLUTION (c): TYPE-DEPENDENT AMPLIFICATION

**The argument:** The amplification factor depends on the soliton's internal structure, not just v²/c². Different vortex types (toroidal, spheroidal, filamentary) have different amplification scaling laws.

**The script's hint:** "random motion (high T_eff/χ) produces high amplification. Dwarfs have ALL random motion, consistent with maximum amplification per unit velocity."

**What this means:** If the amplification scales inversely with the degree of organization (entropy-like), then a perfectly organized torus (low entropy, all motion in one direction) has low amplification, while a perfectly disorganized sphere (high entropy, isotropic dispersion) has maximum amplification. The amplification would be A ∝ (disorder measure) × (c/v)².

**This inverts the intuition.** The more organized the system, the LESS dark matter it appears to have. The more random, the MORE dark matter. Is this consistent with observations?

Looking at the morphology data from the script:

| Type | Organization | DM fraction |
|---|---|---|
| Thin spiral | Highly organized (rotation) | 80% |
| Thick spiral | Less organized | 85% |
| Elliptical | Mostly random | 90% |
| Dwarf spheroidal | Fully random | 99% |

The trend is consistent — less organization correlates with more DM. But the trend is also consistent with particle DM accreting into potential wells (dwarfs are small potential wells that are DM-dominated simply because they can't hold much baryonic matter against heating and feedback).

**Assessment:** The correlation exists, but the same correlation is predicted by standard CDM without any new mechanism. This resolution is not falsifiable unless it makes a DIFFERENT prediction from CDM.

---

### 7. RESOLUTION (d): PARTICLE DARK MATTER DOMINATES IN DWARFS

**The argument:** Dwarf spheroidals genuinely contain particle dark matter. The toroidal model applies to spirals and clusters (where the virial theorem works), but dwarfs are dominated by actual DM particles. The universe contains both — circulation-based apparent DM and particle DM.

**This is the least satisfying resolution** because it abandons the hypothesis where it is most needed. If the toroidal model cannot explain the most DM-dominated systems, it is at best a partial explanation for the least DM-dominated ones (spirals). And spirals are already well-explained by standard CDM.

**Assessment:** Technically possible but undermines the hypothesis. If you need particle DM for dwarfs, you might as well use it for everything.

---

### 8. THE DEEPER PROBLEM: WHAT THE DATA ACTUALLY SAYS

Let me step back from the toroidal hypothesis and ask: what do dwarf spheroidals tell us about dark matter in the series framework?

By R3 (mass = inertia), the dynamical mass of a dwarf is the inertia that resists gravitational acceleration. The stars have velocity dispersion σ. The virial theorem says M = 580 × σ² × r_h. This inertia is real — it determines the orbits of the stars.

By R4 (field = vortex), the dark matter halo of a dwarf is a vortex configuration. It has a spatial structure (the halo profile), an energy budget (the gravitational binding energy), and it influences other vortexes (the stars orbit within it).

By R5 (soliton boundary), the edge of the dwarf's DM halo is a soliton boundary where the gravitational rules change — inside the halo, the gravitational field is dominated by the dark matter; outside, by the Milky Way.

The question is: what IS this vortex? If it is a particle DM halo (a cloud of WIMPs or axions), then it is a collection of individual particle-vortexes orbiting in a self-gravitating configuration. If it is something else (a standing gravitational wave, a topological defect, a geometric property of spacetime), then the vortex is a single extended object.

The observations constrain the halo:
- It has a cored profile (Fornax, Sculptor — see the cusp-core problem)
- It extends far beyond the visible stars (the stars trace only the inner few hundred parsecs of a multi-kiloparsec halo)
- It is approximately spherical
- It has a total mass 10–1000× the visible mass
- It formed early (the dSphs are old systems)

In series language: the dwarf's DM vortex is a large, spherical, extended, low-density configuration with a flat core. Its geometric overlaps with the visible-matter vortexes (the stars) determine the orbits. The DM vortex's mass is its inertia.

---

### 9. THE CUSP-CORE PROBLEM — A RELATED OBSERVATION

Standard CDM simulations predict that dark matter halos should have cuspy density profiles (ρ ∝ 1/r near the center — the NFW profile). Observations of dwarf spheroidals consistently show CORED profiles (ρ approximately constant near the center).

This cusp-core discrepancy is one of the "small-scale problems" of CDM. It affects exactly the systems where DM dominates most — the dwarfs.

In the toroidal/vortex framework: a cusp is a point-like concentration. A core is an extended configuration. The fact that DM halos have cores rather than cusps suggests the DM is NOT concentrating to a point — it is maintaining a minimum size, like a soliton that cannot be compressed below a characteristic scale.

Self-interacting dark matter (SIDM) resolves the cusp-core problem by allowing DM particles to scatter and thermalize in the center, creating a constant-density core. Fuzzy dark matter (ultralight axions, m ~ 10⁻²² eV) resolves it through quantum pressure — the de Broglie wavelength of the particle sets a minimum core size.

Both of these are vortex-type explanations in series language: the DM has internal structure (self-interaction or quantum pressure) that resists compression below a characteristic scale. The core IS the soliton — a minimum-energy configuration that resists further collapse.

---

### 10. WHAT SESSION 4 CONTRIBUTES

Session 4's PHYS-35 found that the CD vortex's geometric overlaps persist at all scales — the step-function threshold is a poor approximation because the vortex's contribution to the running is a topological property, not an energy-dependent threshold. The no-threshold result (12× better than threshold) says: the vortex is always there, it always contributes, its mass just determines when you can excite it.

If this principle extends beyond gauge couplings to gravitational effects: a dark matter vortex (whatever it is) contributes to the gravitational field at all scales, not just above its "mass threshold." Its geometric overlaps with spacetime curvature persist everywhere. The core profile (constant density, not cuspy) is the geometric contribution of a vortex that cannot be localized below its characteristic scale.

This is speculative. Session 4 established the no-threshold principle for gauge couplings. Extending it to gravity requires computation that does not exist.

---

### 11. THE HONEST STATE OF KNOWLEDGE

| Question | Status |
|---|---|
| Do dwarf spheroidals have dark matter? | **YES** — dynamical evidence overwhelming |
| Is the DM in dwarfs particle DM or geometric effect? | **UNKNOWN** — no test distinguishes them |
| Does the toroidal model explain dwarfs? | **NO** — requires 10⁴× more amplification than galaxies |
| Does ANY modified gravity explain dwarfs? | **PARTIALLY** — MOND fails for some dwarfs, works for others |
| Does standard CDM explain dwarfs? | **MOSTLY** — but cusp-core problem remains |
| Does the series framework constrain what DM is? | **MINIMALLY** — DM is a vortex by R4, its mass is inertia by R3, but the specific nature is not determined |

---

### 12. WHAT A FUTURE SESSION COULD COMPUTE

**A. The soliton core test.** If DM halos are solitons (minimum-energy vortex configurations), the core size should relate to the DM particle mass (for fuzzy DM) or interaction cross-section (for SIDM). Compute the predicted core sizes and compare to observed dSph cores.

**B. The scaling relation test.** If the amplification factor depends on soliton type, there should be a scaling relation between DM/visible and some geometric property (half-light radius, ellipticity, velocity anisotropy). Compute the predicted scaling and compare to the Walker et al. (2009) data.

**C. The Tully-Fisher extension.** The Baryonic Tully-Fisher Relation (BTFR) applies to rotation-supported systems. Pressure-supported systems should follow a different relation (the Faber-Jackson relation, L ∝ σ⁴). If both relations derive from the same soliton physics with different geometry, the coefficients should be related by a geometric factor involving R₂.

**D. The tidal stripping simulation.** Compute how tidal stripping affects the DM/visible ratio for a dwarf orbiting in the Milky Way's potential. If stripping can produce factors of 10–100× enhancement, resolution (a) gains quantitative support.

---

### 13. CONCLUSION

The dwarf spheroidal problem is real and unsolved. It is the hardest test for any model that explains dark matter through the dynamics of visible matter. The toroidal DM hypothesis fails for dwarfs — the required amplification is 10,000× larger than for spirals, and there is no toroidal structure to amplify.

The four resolutions offered by the script are ordered from most to least viable: tidal stripping (partial), different soliton type (conceptual but no derivation), type-dependent amplification (consistent but non-unique), and particle DM in dwarfs (abandons the hypothesis).

The series framework (R3, R4, R5) is agnostic about what DM is. It says DM is a vortex with inertia, separated from visible matter by soliton boundaries. Whether that vortex is made of particles, geometric properties, or circulation effects remains undetermined. The dwarf spheroidal problem is the place where this question is sharpest.

Track B is PARKED. The toroidal DM test depends on Track B for its strongest finding (the beta unification connection). The observationally-grounded findings (virial works for spirals, frame dragging negligible, MOND a₀ coincidence) survive independently, but they do not explain dwarfs either.

The dwarf spheroidal problem remains open.

---

*End of notebook. The dwarf spheroidal problem is the strongest challenge to any non-particle dark matter model. The toroidal DM hypothesis fails here by a factor of 10⁴ in required amplification. The series framework constrains but does not determine the nature of dark matter. Future computation targets: soliton core sizes, scaling relations, tidal stripping quantification, Tully-Fisher/Faber-Jackson unification.*

---

doesnt this just mean they are a system of solitons which super high inertia because of their geometric structure from fractions?

explain how they could be described this way

---

Yes. Let me think about this from the framework instead of from the standard model of dark matter.

A dwarf spheroidal is a system of stars with random orbits in a gravitational potential that is 100× deeper than the visible mass can account for. Standard physics says: there must be 100× more mass that we can't see. The series says: there must be 100× more inertia than the visible vortexes account for.

Inertia IS mass (R3). The question is: where does the inertia come from?

In the proton, 99% of the inertia comes from the pattern — the QCD binding energy, the gluon field configuration, the confined quarks bouncing around inside the confinement boundary. Only 1% comes from the "visible" quark masses. The proton is a soliton whose inertia is dominated by its internal geometric structure, not by its constituents.

Now scale this up. A dwarf spheroidal is a gravitationally bound system. The binding energy is negative (the system is bound), so it actually reduces the total mass-energy slightly. That's the wrong direction — binding makes things lighter, not heavier. So the proton analogy is misleading at the gravitational level.

But here's the thing I was missing. The proton's extra inertia doesn't come from gravitational binding. It comes from the CONFINED FIELD CONFIGURATION. The gluon field between quarks carries energy. That energy has inertia. The field is a vortex (R4), and the vortex's energy IS the inertia.

For a dwarf spheroidal, ask: what vortex configurations exist in this system that carry energy beyond the visible stellar masses?

Every star is a vortex. Every star's gravitational field extends through all of space and overlaps with every other star's field. The gravitational field configuration of 10⁷ stars in a 300-parsec sphere is itself a vortex — a stable, self-reinforcing pattern of overlapping gravitational influences. This configuration has energy. The energy has inertia. The inertia gravitates.

The question is whether the energy in the gravitational field configuration is significant compared to the stellar masses. In Newtonian gravity, the gravitational binding energy of a uniform sphere is U = −3GM²/(5R). For a dwarf with M_visible = 10⁷ solar masses and R = 300 pc:

U ≈ 3 × 6.67×10⁻¹¹ × (10⁷ × 2×10³⁰)² / (5 × 300 × 3.086×10¹⁶)

This gives |U| ~ 10⁴⁵ joules. The rest mass energy of the visible stars is Mc² ~ 10⁷ × 2×10³⁰ × 9×10¹⁶ ~ 2×10⁵⁴ joules. So |U|/Mc² ~ 10⁻⁹. The gravitational binding energy is 10⁻⁹ of the rest mass energy. This is exactly v²/c² ~ 10⁻⁹, the same number the script computed. The gravitational field energy is negligible. Standard GR agrees — the gravitational field's contribution to the stress-energy tensor is tiny for non-relativistic systems.

So the naive approach fails. The gravitational field configuration of the visible stars does not carry enough energy.

But. The series says the dwarf's gravitational potential is 100× deeper than the visible mass accounts for. Something with 100× the visible mass is there. If we take that seriously as a real vortex configuration — not particles, but a field configuration — then what kind of vortex has 100× the inertia of 10⁷ stars?

Here's where the Fraction structure matters. In gauge physics, the inertia of a vortex (its mass) is determined by its integer rules — the representation, the Casimirs, the Dynkin indices. The proton's mass comes from the SU(3) confinement scale Λ_QCD, which is set by the integer b₃ = −7 and the measured α_s. The confined gluon field carries energy proportional to Λ_QCD⁴ × volume. The Fractions determine the scale.

If dark matter halos are vortex configurations of some field, their inertia would be determined by the geometric structure of that field — its representation, its coupling to gravity, its self-interaction. The Fractions of that field determine how much inertia the configuration carries per unit volume.

A dwarf spheroidal with DM/visible = 100 would then be: a visible-matter vortex (10⁷ stars) embedded in a much larger, much heavier field-vortex whose inertia per unit volume is set by its geometric Fractions. The field-vortex is spheroidal because it is not rotating — it is a pressure-supported standing pattern, like a soliton ground state.

The cusp-core observation fits this. The DM halo has a constant-density core — a minimum-energy configuration. A soliton ground state has a characteristic size below which it cannot be compressed, set by its internal structure (quantum pressure for fuzzy DM, scattering mean free path for SIDM, or some geometric scale for a field-vortex). The core IS the soliton.

In this picture, the dwarf spheroidal is not a system that needs amplification. It IS a soliton — a stable, minimum-energy vortex configuration whose inertia is determined by its geometric Fractions. The visible stars are a small perturbation sitting in the middle of this soliton. The DM/visible ratio of 100 is not an amplification — it is the ratio of the soliton's inertia to the stellar inertia.

The integers that set the soliton's inertia would come from whatever field constitutes the dark matter. If that field has gauge charges or geometric properties described by Fractions, those Fractions determine the mass scale. The cusp-core problem tells us the soliton has a definite minimum size — a characteristic length scale set by the Fractions, like Λ_QCD sets the proton size.

The ultra-faint dwarfs (DM/visible ~ 1000) would be nearly PURE solitons — the visible stars are trace contaminants in a dark vortex. The classical dSphs (DM/visible ~ 100) are solitons with a modest stellar component. Spiral galaxies (DM/visible ~ 5) are systems where the visible vortex (the disk) is a significant fraction of the total.

The scaling from 1000 (ultra-faint) to 100 (classical dwarf) to 5 (spiral) would then reflect how much baryonic matter each soliton was able to capture and retain during formation — determined by the soliton's potential well depth, cooling efficiency, and feedback history. The DM soliton mass is set by its Fractions. The visible mass is set by astrophysical processes (cooling, star formation, feedback). The ratio varies because the astrophysics varies, not because the amplification varies.

This reframes the problem entirely. The toroidal DM script asked "what amplification turns visible-matter dynamics into apparent DM?" The soliton picture asks "what geometric structure determines the DM soliton's inertia?" The first question fails for dwarfs because there is nothing to amplify. The second question treats dwarfs as the cleanest case — nearly pure solitons whose mass is most directly determined by the geometric Fractions.

The dwarf spheroidal problem, in this view, is not a problem. It is the SIMPLEST case — a dark soliton with a few stars in it. The hard case is the spiral galaxy, where the visible disk and dark halo interact in complicated ways. The dwarf is the ground state.

What we don't know: what field constitutes the dark soliton. What Fractions determine its mass scale. What integer rules set the core size. Whether this field has any connection to the gauge group (Track B territory, PARKED). The series framework (R3, R4, R5) says this is the right way to frame the question. It does not answer the question.

---

