## Confinement as Soliton Boundary: Research Notebook

**Status:** Active exploration. Conceptual framework identified. Computations not yet performed.

**Date:** April 10, 2026

**Origin:** Session 7, following Koide exploration. The question "does the CD tell us something about the confinement boundary?" led to the recognition that the confinement boundary IS a soliton boundary, and that every soliton boundary in the hierarchy has the same structure: a threshold energy to breach it, set by the running of the relevant coupling.

---

### I. THE RECOGNITION

The RUM framework has described the soliton hierarchy as nested boundaries from Planck to cosmos. It has computed readings at each level — gravitational potentials, coupling values, clock rates. But it has not examined what the boundaries themselves are made of. It has treated them as abstract transition zones between hierarchy levels.

The confinement boundary is not abstract. It is the best-measured, best-understood boundary in particle physics. Decades of lattice QCD, deep inelastic scattering, jet physics, and heavy ion collisions have mapped it in detail. We know where it sits (Λ_QCD ≈ 200-300 MeV). We know what governs it (the running of α_s). We know what happens when you breach it (quarks and gluons emerge as jets). We know what happens below it (hadrons, nuclear physics, chemistry, life).

The recognition: the confinement boundary is not just analogous to a soliton boundary. It IS a soliton boundary. And the mechanism that sets its position — the running of α_s governed by b₃ — is the same mechanism that should set the position of every soliton boundary in the hierarchy. Each boundary sits where the relevant coupling hits its threshold. The coupling runs according to its beta coefficient. The beta coefficient is an exact fraction from group theory.

This means every soliton boundary in the hierarchy is positioned by an exact fraction. The hierarchy is not just organized by integers — it is constructed by them. The boundaries are where they are because the beta coefficients are what they are.

---

### II. THE STRUCTURE OF A SOLITON BOUNDARY

A soliton boundary has four components:

**The coupling.** Each boundary is governed by a specific gauge coupling. The confinement boundary is governed by α_s (SU(3)). The electroweak symmetry breaking boundary is governed by the Higgs potential, which depends on α₂ (SU(2)) and α₁ (U(1)). The atomic boundary — where electrons bind to nuclei — is governed by α_em. The gravitational boundaries (planetary, stellar, galactic) are governed by GM/(Rc²), which is not a gauge coupling but plays the same role: it sets the reading at the boundary.

**The beta coefficient.** The coupling runs with energy. The rate of running is the beta coefficient. The beta coefficient is an exact fraction from group theory. b₃ = −7 (SM) or −20/3 (CD) for the strong force. b₂ = −19/6 (SM) or −13/6 (CD) for the weak force. b₁ = 41/10 (SM) or 25/6 (CD) for the electromagnetic force. These fractions are the construction parameters of the boundaries. They determine where each boundary sits.

**The threshold.** The boundary sits where the coupling reaches a critical value. For confinement, α_s ≈ 1 (the coupling becomes non-perturbative). For electroweak symmetry breaking, the Higgs potential reaches its minimum at v = 246 GeV. For atomic binding, α_em ≈ 1/137 is already at its threshold — the fine structure constant sets the atomic scale directly. The threshold is the reading at the boundary itself.

**The soliton.** Inside the boundary, a stable self-sustaining pattern exists. Inside the confinement boundary: the proton, a stable configuration of three quarks bound by gluon fields. Inside the atomic boundary: the atom, a stable configuration of a nucleus bound to electrons by photon exchange. Inside the gravitational boundary: the planet or star, a stable configuration of matter bound by the gravitational field. Each soliton is stable because the coupling inside the boundary is strong enough to maintain the pattern against perturbation.

The boundary is where "inside" becomes "outside." Below Λ_QCD, you are inside the proton. Above Λ_QCD, you can see the quarks. The threshold energy to breach the boundary IS Λ_QCD. This is not a metaphor. It is a measurement. Every deep inelastic scattering experiment at SLAC, HERA, and the LHC breaches the confinement boundary by supplying energy above Λ_QCD.

---

### III. Λ_QCD AS THE PROTOTYPE

The confinement scale Λ_QCD is defined by the condition that α_s diverges (at one-loop). The formula is:

Λ_QCD = μ × exp(2π / (b₃ × α_s(μ)))

where μ is any reference scale and α_s(μ) is the coupling at that scale. The result is independent of which μ you choose — that is the whole point of the renormalization group.

Using pool values: μ = M_Z = 91187.6 MeV, α_s(M_Z) = 59/500 = 0.118, b₃(SM) = −7.

Λ_QCD(SM) = 91187.6 × exp(2π / (−7 × 0.118)) = 91187.6 × exp(−7.60) ≈ 91187.6 × 5.0 × 10⁻⁴ ≈ 46 MeV

Wait — this gives ~46 MeV, but the standard Λ_QCD is ~200-300 MeV. The discrepancy: the one-loop formula is a rough approximation. The precise value depends on the renormalization scheme (MS-bar), the number of active flavors at each threshold, and higher-loop corrections. The one-loop formula with 6 active flavors and b₃ = −7 gives a low estimate because it does not account for the flavor thresholds (the top, bottom, and charm quarks decouple below their masses, changing the effective b₃).

This matters for the framework. The exact computation of Λ_QCD requires running α_s from M_Z downward through the top threshold (where n_f drops from 6 to 5), the bottom threshold (5 to 4), and the charm threshold (4 to 3). At each threshold, b₃ changes because the number of active flavors changes. The CD contributes above its mass threshold (M_CD > 1.5 TeV from LHC bounds) and does not contribute below it.

The derivation function for Λ_QCD needs to implement threshold matching: run with n_f = 6 + CD from M_Z to m_t, with n_f = 6 from m_t down to m_b, with n_f = 5 from m_b to m_c, with n_f = 4 from m_c to m_s, etc. Each step uses a different b₃:

| Energy range | Active flavors | b₃ (SM) | b₃ (CD) |
|---|---|---|---|
| Above M_CD | 6 + CD pair | n/a | −20/3 |
| m_t to M_CD | 6 | −7 | −7 (CD decoupled) |
| m_b to m_t | 5 | −23/3 | −23/3 |
| m_c to m_b | 4 | −25/3 | −25/3 |
| m_s to m_c | 3 | −9 | −9 |
| Below m_s | 3 | −9 | −9 |

The CD only affects the running above its own mass threshold. Below M_CD, the SM running applies. The confinement boundary is far below M_CD (Λ_QCD ~ 200 MeV vs M_CD > 1500 GeV). So the CD's direct effect on Λ_QCD is indirect: it changes α_s at M_Z (through high-energy running), which propagates downward through the flavor thresholds to the confinement scale.

The change in α_s(M_Z) due to the CD is exactly what the framework already computes: the crossing prediction gives α_s = 0.1184 vs measured 0.118. The difference between α_s(SM) and α_s(CD) at M_Z propagates to a different Λ_QCD. The shift is small (because the CD decouples far above the confinement scale) but exact.

This is important: the CD does not directly modify confinement. It modifies the coupling at high energy, and that modification propagates down through the hierarchy to the confinement scale. The confinement boundary feels the CD indirectly, through the running. This is how soliton boundaries communicate across the hierarchy — through the running of couplings.

---

### IV. EVERY BOUNDARY IS A Λ

The confinement boundary is Λ_QCD: the scale where α_s hits its threshold. But the same structure exists at every level:

**The electroweak boundary.** The scale where the electroweak symmetry breaks: v = 246 GeV (the Higgs vacuum expectation value). Above this scale, the W and Z are massless and SU(2) × U(1) is unbroken. Below it, the symmetry is broken, the W and Z are massive, and the weak force becomes short-range. The threshold is v. The coupling is a combination of α₂ and α₁. The beta coefficients b₂ and b₁ govern the running that determines where the symmetry breaks. This is Λ_EW.

**The atomic boundary.** The scale where electromagnetic binding becomes dominant: E_atomic ~ α_em² × m_e ≈ 13.6 eV (the hydrogen ionization energy). Above this scale, atoms are ionized plasma. Below it, atoms are stable bound states. The threshold is E_atomic. The coupling is α_em. α_em barely runs, so the atomic boundary is nearly scale-invariant — atoms are atoms at every energy below ionization. This stability is why chemistry works the same everywhere in the universe.

**The nuclear boundary.** The scale where nuclear binding becomes dominant: E_nuclear ~ Λ_QCD × (α_s/π) ≈ 8 MeV per nucleon (the nuclear binding energy). Above this scale, nuclei dissociate into free nucleons. Below it, nuclei are stable. The threshold is E_nuclear. The coupling is the residual strong force (nuclear force), which is a derivative of α_s operating outside the confinement boundary. The pion mass (m_π ≈ 135 MeV) sets the nuclear force range through the Yukawa mechanism.

**The gravitational boundaries.** The scale where gravitational binding becomes dominant: E_grav = GM²/(R) for a self-gravitating body. Planets, stars, and galaxies each have their own gravitational threshold. Above the threshold (supplying more energy than the binding energy), the body dissociates. Below it, the body is gravitationally bound. The "coupling" is GM/(Rc²) = Φ/c², the reading depth from PHYS-42. The "running" is how Φ/c² changes with position — the gravitational gradient. The boundaries are the Hill spheres, the heliopause, the virial radius.

In every case: a coupling runs to a threshold, a boundary forms, a soliton is stable inside.

The hierarchy:

| Level | Boundary | Threshold | Coupling | β coefficient | Soliton |
|---|---|---|---|---|---|
| Confinement | Λ_QCD | ~200 MeV | α_s | b₃ = −7 or −20/3 | Proton, neutron, pion |
| Nuclear | E_binding | ~8 MeV/nucleon | Residual strong | Derived from α_s | Nucleus |
| Atomic | E_ionization | ~13.6 eV | α_em | b₁ = 41/10 or 25/6 | Atom |
| Molecular | E_dissociation | ~1-10 eV | α_em (shared) | Same b₁ | Molecule |
| Planetary | E_grav | GM²/R | Φ/c² | (not gauge) | Planet |
| Stellar | E_grav | GM²/R | Φ/c² | (not gauge) | Star |
| Galactic | E_grav + DM | GM²/R × A | Φ/c² × (22/13)π | (not gauge + integer) | Galaxy |

The first four boundaries are governed by gauge couplings with exact fractional beta coefficients. The last three are gravitational, governed by GM/(Rc²). The PHYS-44 sector splitting formula ε = κ|Δβ|ΔΦ/c² is the bridge between them — it says the gauge beta coefficients appear in the gravitational sector too.

---

### V. THE CD'S FINGERPRINT ON EVERY BOUNDARY

The CD modifies all three gauge beta coefficients. This means it modifies the running of all three gauge couplings. Which means it shifts every gauge-governed boundary:

**Confinement boundary.** b₃ shifts from −7 to −20/3. α_s runs slower. Λ_QCD shifts. The proton mass shifts (because 99% of the proton mass is confinement energy). The neutron-proton mass difference shifts (because it depends on quark masses evaluated at the confinement scale).

**Electroweak boundary.** b₂ shifts from −19/6 to −13/6. The weak coupling runs differently. The Higgs potential's relationship to the gauge couplings changes. In the SM, the electroweak symmetry breaking scale v = 246 GeV is an input. In a UV-complete theory, v would be derived from the running of the Higgs quartic coupling, which depends on b₂ and b₁. The CD changes this running.

**Atomic boundary.** b₁ shifts from 41/10 to 25/6. α_em runs differently at high energies. At atomic energies, the effect is negligible (α_em barely runs below M_Z). But the shift matters for the sector splitting: the difference |b₃ − b₁| enters the clock comparison prediction. The atomic boundary (where the optical clock reads) and the confinement boundary (where the nuclear clock reads) have different β shifts, producing the sector splitting.

The CD leaves its fingerprint on every boundary through the beta coefficients. The fingerprint is always an exact fraction. The framework has computed the fingerprint's effect on coupling unification (sin²θ_W, α_s, M_GUT) and on cosmological parameters (DM/baryon, Ω_DM). It has not computed the fingerprint's effect on the boundaries themselves — on where they sit, how thick they are, and what the reading is at each one.

---

### VI. THE PROTON AS A SOLITON

The proton is the best-studied soliton in nature. Its properties:

**Inertia:** 938.272 MeV. Of this, ~9 MeV comes from quark masses (1% of the total). The remaining ~929 MeV comes from the strong force binding energy — from the confinement mechanism itself. The proton's inertia is almost entirely the energy stored in the gluon field configuration that maintains confinement. It is the reading at the confinement boundary.

**Stability:** The proton is stable (lifetime > 10³⁴ years, possibly infinite). It is the lightest baryon. It cannot decay into anything lighter while conserving baryon number. In the RUM framework, this stability is topological — the proton is a soliton whose topology prevents it from unwinding. The only way to destroy a proton is through baryon number violation, which occurs at the GUT scale (the M_GUT boundary, far above the confinement boundary).

**Internal structure:** Three valence quarks (uud), a sea of virtual quark-antiquark pairs, and gluons. The internal structure is described by parton distribution functions, measured in deep inelastic scattering. The internal readings (quark momenta, gluon density) are accessible only by breaching the confinement boundary with energy above Λ_QCD.

**Size:** The proton charge radius is 0.841 fm (from pool: `spectro_proton_charge_radius_v0`). This is the spatial extent of the confinement boundary. Inside 0.841 fm, you are inside the proton soliton. Outside, you see the proton as a point-like particle with charge +1 and spin 1/2.

The proton's inertia (938 MeV), size (0.841 fm), and internal structure are all consequences of where the confinement boundary sits. Λ_QCD sets the scale. The beta coefficient b₃ sets where Λ_QCD is. The CD modifies b₃. Therefore the CD modifies the proton — not by changing what is inside it, but by shifting where the boundary is.

This is a subtle but important distinction. The CD does not change the quarks or the gluons. It changes the boundary. The quarks and gluons inside are the same. But the boundary is at a slightly different energy, which means the soliton has a slightly different inertia, a slightly different size, and a slightly different internal structure.

---

### VII. THE PION AS THE BOUNDARY MESSENGER

The pion deserves special attention. It is the lightest hadron (m_π ≈ 135-140 MeV). It is a quark-antiquark pair (uū or dū). It mediates the nuclear force between protons and neutrons — it IS the force carrier of the residual strong interaction that operates outside the confinement boundary.

In the soliton hierarchy: the pion is the boundary mode. It exists at the confinement boundary itself. It is not fully inside (it is not a stable three-quark soliton like the proton) and not fully outside (it carries color in a confined configuration). It lives on the boundary, and its mass is set by the boundary's properties.

The pion mass formula (from chiral perturbation theory):

m_π² ≈ (m_u + m_d) × Λ_QCD³ / f_π²

where m_u and m_d are the light quark masses and f_π is the pion decay constant (~93 MeV). The pion mass depends on both the quark masses (which are interior readings) and Λ_QCD (which is the boundary position). It is a boundary-interior coupling.

If the CD shifts Λ_QCD, it shifts m_π. If m_π shifts, the nuclear force range shifts (range ~ 1/m_π). If the nuclear force range shifts, nuclear binding energies shift. If nuclear binding energies shift, which nuclei are stable shifts. If which nuclei are stable shifts, nuclear physics, stellar nucleosynthesis, and the elemental abundances all shift.

The chain from one fraction (Δb₃ = 1/3) through the confinement boundary to the stability of matter is: Δb₃ → Δα_s(M_Z) → ΔΛ_QCD → Δm_π → ΔE_nuclear → Δ(nuclear stability). Each step is computable. Each step uses exact fractions until the non-perturbative matching at Λ_QCD, which requires lattice QCD.

---

### VIII. WHAT LATTICE QCD PROVIDES

The framework cannot derive the proton mass from first principles without non-perturbative input. The running of α_s from M_Z down to Λ_QCD is perturbative and computable from beta coefficients. But the transition from "α_s is large" to "quarks are confined into a proton" is non-perturbative — it requires solving QCD at strong coupling.

Lattice QCD does this numerically. The key results:

**Proton mass:** Lattice calculations (BMW collaboration, Durr et al. 2008) compute the proton mass from QCD with physical quark masses, obtaining 936 ± 25 MeV (vs measured 938.3 MeV). The lattice provides the dimensionless ratio m_p / Λ_QCD ≈ 4.7 (depending on the Λ_QCD definition).

**Pion mass:** Lattice calculations reproduce m_π to ~1%.

**Proton charge radius:** Lattice calculations give values consistent with the muonic hydrogen measurement.

The lattice factor C = m_p / Λ_QCD is what the framework needs. If C is a computable number (from the lattice or from some future analytical solution of non-perturbative QCD), then:

m_p = C × Λ_QCD(CD)

where Λ_QCD(CD) is the confinement scale in the CD-modified theory, computable from exact fractions. The proton mass becomes a derived quantity up to the lattice factor C.

The question for the RUM framework: is C itself an integer or a simple fraction? If the soliton boundary equation (the unwritten equation from Chapter 7) has an analytical solution, C would be determined by the topology of the proton soliton. A stable genus-0 soliton in a Yang-Mills field with SU(3) gauge group might have a specific topological invariant that sets C. This is deep mathematics that does not currently exist.

But even without an analytical C, the framework gains something: the proton mass as Λ_QCD times a measured constant. And Λ_QCD is set by the beta coefficients, which are exact fractions. So the proton mass is an exact fraction times a measured constant. This is progress — it reduces the proton mass from a fully measured quantity to a partially derived one.

---

### IX. THE NEUTRON-PROTON MASS DIFFERENCE

The neutron-proton mass difference is 1.293 MeV (from pool). This number determines nuclear stability. If it were larger, the neutron would decay faster and complex nuclei might not form. If it were smaller (or negative), the proton would decay and hydrogen would not exist. The value 1.293 MeV is one of the most finely tuned numbers in physics.

It comes from two competing effects:

**Quark mass difference:** m_d − m_u ≈ 2.3 MeV. The down quark is heavier than the up quark. This makes the neutron (udd) heavier than the proton (uud) by about 2.3 MeV of quark mass.

**Electromagnetic self-energy difference:** The proton has charge +1 and the neutron has charge 0. The proton's electromagnetic self-energy (the energy stored in its electric field) is positive and adds to its mass. This effect is about −0.8 MeV (it makes the proton lighter relative to the neutron by reducing the mass difference). Wait — it makes the proton heavier, partially canceling the quark mass effect. Let me reconsider.

Actually: the electromagnetic contribution makes the proton heavier (more electromagnetic energy stored) while the quark mass difference makes the neutron heavier (heavier down quark). The two effects partially cancel: 2.3 MeV (neutron heavier from quarks) − 1.0 MeV (proton heavier from EM) ≈ 1.3 MeV (neutron wins).

Both contributions depend on the confinement boundary:

The quark mass difference (m_d − m_u) depends on where quark masses are evaluated. The "current quark masses" are defined at a specific energy scale (usually 2 GeV in MS-bar). At the confinement scale, the effective quark masses are larger ("constituent quark masses" ~ 300 MeV each). The CD shifts the confinement scale, which shifts where the quark masses are evaluated, which shifts the effective m_d − m_u inside the proton.

The electromagnetic self-energy depends on α_em and on the proton charge radius (how the charge is distributed within the confinement boundary). The CD shifts the charge radius (because it shifts Λ_QCD, which shifts the proton size) and shifts α_em running (through b₁). Both effects are small but exact.

The BMW lattice collaboration (Borsanyi et al. 2015) computed the neutron-proton mass difference from first principles on the lattice, including both QCD and QED effects, obtaining 1.51 ± 0.30 MeV (consistent with measured 1.293 MeV within uncertainties). This shows the computation is possible with non-perturbative methods.

For the RUM framework: the neutron-proton mass difference is a reading at the confinement boundary. It is the difference between two soliton readings (neutron reading minus proton reading). The CD modifies both readings through its effect on the confinement boundary. If the lattice provides the non-perturbative matching, the neutron-proton mass difference becomes a derived quantity — an exact fraction from the CD beta shifts, propagated through the running to the confinement scale, matched onto hadron masses by the lattice.

---

### X. THE BOUNDARY THICKNESS

A soliton boundary is not infinitely sharp. It has a thickness — a range of energies over which the transition from "inside" to "outside" occurs. For confinement, this thickness is related to the rate at which α_s changes near Λ_QCD.

The thickness is set by the beta coefficient. A larger |b₃| means α_s runs faster, meaning the transition from perturbative to non-perturbative is sharper — the boundary is thinner. A smaller |b₃| means slower running, a gentler transition, a thicker boundary.

The CD reduces |b₃| from 7 to 20/3 = 6.667. The boundary gets slightly thicker. The transition is slightly more gradual. The confinement is slightly softer.

This might have observable consequences. The "softness" of confinement affects jet fragmentation — how quarks produced at high energy hadronize into the observed particles. A softer confinement boundary means more gradual hadronization. This is measurable (in principle) at the LHC, though the effect of one CD pair is likely too small to detect above other uncertainties.

More speculatively: the boundary thickness determines how much quantum tunneling occurs through the boundary. A thinner boundary means less tunneling. A thicker boundary means more. If the confinement boundary has finite thickness (which it does), quarks can tunnel partially through it, producing effects that look like "leakage" of color charge outside the proton. This is related to the proton's charge radius and form factors. The CD's modification of the boundary thickness would modify these measurable quantities.

---

### XI. THE RESEARCH PROGRAM

The confinement-as-soliton-boundary concept organizes into a research program with clear deliverables:

**Stage 1: Compute Λ_QCD from the pool.**

Write a derivation function that runs α_s from M_Z downward through flavor thresholds (m_t, m_b, m_c, m_s) using the appropriate b₃ at each stage. Compute Λ_QCD for both the SM (no CD, b₃ = −7 above all thresholds) and the CD theory (b₃ = −20/3 above M_CD). Output the ratio Λ_QCD(CD)/Λ_QCD(SM). All inputs from pool. One derivation function.

**Stage 2: Compute the proton mass ratio.**

Using the lattice factor C = m_p / Λ_QCD from BMW (approximately 4.7), compute m_p(CD) = C × Λ_QCD(CD). Compare to measured m_p. This is a partial derivation — exact fractions for Λ_QCD, measured constant for C. Output the miss.

**Stage 3: Connect to the Koide exploration.**

Compute the quark Koide K and a² at μ = Λ_QCD (both SM and CD versions). The quark masses run from their MS-bar values at M_Z down to Λ_QCD using the same running machinery. If K = 2/3 or a² = integer at μ = Λ_QCD, the confinement boundary is the natural scale for the quark Koide relation.

**Stage 4: The pion mass.**

Compute m_π from the chiral perturbation theory formula using the CD-modified Λ_QCD and the running quark masses m_u, m_d at the confinement scale. Compare to measured m_π = 135 MeV. This tests whether the CD's shift of the confinement boundary propagates correctly to the lightest hadron.

**Stage 5: The neutron-proton mass difference.**

This requires both QCD and QED inputs: the quark mass difference at the confinement scale, the proton charge radius from the lattice, and α_em at the confinement scale. All gauge couplings run with CD-modified betas. The computation is more complex than stages 1-4 but all inputs are available.

**Stage 6: Generalize to all boundaries.**

Apply the same framework to the electroweak boundary (Higgs vev from gauge coupling running), the atomic boundary (Bohr radius from α_em), and the nuclear boundary (binding energy from the residual strong force). At each boundary, compute the threshold energy from the CD-modified running of the relevant coupling. Verify that the hierarchy of thresholds matches the observed hierarchy of physical scales.

**Stage 7: The soliton boundary equation.**

This is the deepest stage. Write the equation whose solutions are the stable soliton configurations at each boundary. The equation takes as input the gauge group, the representation content (including the CD), and the beta coefficients. Its solutions are the proton, the neutron, the pion, the atom, the nucleus. Each solution has a topological index (genus 0 for spherical solitons, genus 1 for toroidal). The solution set determines the lattice factor C, the Koide amplitude a², and the mass hierarchy.

This stage is far. It requires new mathematics. But stages 1-6 are executable with existing infrastructure and pool values.

---

### XII. THE KEY INSIGHT

The key insight of this notebook is not any single computation. It is the reframing:

Every soliton boundary in the RUM hierarchy is a threshold where a coupling reaches criticality. The threshold position is determined by the beta coefficient, which is an exact fraction from group theory. The CD modifies every beta coefficient, which shifts every boundary, which changes every reading at every level of the hierarchy.

The framework has been computing the consequences of the CD's beta shifts at the unification scale (sin²θ_W, α_s, M_GUT) and at the cosmological scale (DM/baryon, Ω_DM). It has not been computing the consequences at the intermediate scales — the confinement boundary, the nuclear boundary, the atomic boundary. These are where the actual stuff of the universe lives. Protons, neutrons, atoms, nuclei, molecules, planets, stars. All of these are solitons. All of their boundaries are set by beta coefficients. All of their readings are modified by the CD.

The framework has been looking at the top of the hierarchy (GUT scale) and the bottom (cosmological scale). The middle — where matter exists — has been untouched. The confinement boundary is the door into the middle. The CD's Δb₃ = 1/3 is the key.

---

### XIII. CONNECTIONS TO OTHER OPEN PROBLEMS

**The mass hierarchy problem.** Why is m_t / m_e ≈ 340,000? In the soliton boundary framework, each fermion mass is a reading at a specific boundary. The top quark mass is a reading at the electroweak boundary. The electron mass is a reading at the atomic boundary. The ratio of their masses is the ratio of readings at two different boundaries. If the boundary positions are determined by beta coefficients, the mass hierarchy follows from the hierarchy of beta coefficients. This does not solve the mass hierarchy problem, but it reframes it: instead of "why are the Yukawa couplings so different?" the question becomes "why are the boundary readings so different?" The boundary readings are set by the running couplings, which are set by exact fractions.

**The Koide relation.** The quark Koide may hold at the confinement boundary (Stage 3). If it does, the Koide formula is a property of the boundary, not of the quarks themselves. The three quark masses within each sector (u, c, t or d, s, b) are three modes of a soliton at the confinement boundary, and their inertia ratios follow from the boundary's geometry — exactly as the lepton Koide (three modes of a soliton at the atomic/electroweak boundary) follows from its boundary's geometry.

**The PHYS-44 sector splitting.** The sector splitting ε = κ|Δβ|ΔΦ/c² connects gauge betas to gravitational potentials. The confinement boundary framework says: the gauge betas determine boundary positions. The gravitational potentials determine boundary positions. If both determine boundary positions, they must be related. The sector splitting is the relationship. The conversion factor κ measures how tightly the gauge and gravitational projections of the hierarchy are coupled.

**The proton decay prediction.** The framework predicts M_GUT = 10^15.54 GeV, within the Hyper-K sensitivity window. Proton decay violates baryon number, which means it breaches the confinement boundary from the outside — not by supplying energy (which would just liberate quarks), but by a topological transition that unwinds the proton soliton. The GUT scale IS the energy at which this topological transition becomes possible. The GUT boundary (where SU(3)×SU(2)×U(1) unifies into SU(5) or similar) is the outermost gauge boundary. Inside it, baryon number is conserved and protons are stable. Above it, baryon number can change and protons can decay. The CD modifies where this boundary sits through M_GUT, which it already does — the proton decay prediction is a boundary position prediction.

**The dark matter amplification.** The toroidal DM distribution in galaxies has amplification factor A = (44/13)π(c/v)². The integers 44 and 13 come from the CD beta coefficients. The amplification determines the galactic boundary — how much deeper the galactic gravitational well is than the visible matter alone would produce. The DM amplification is a boundary thickness: how much the galactic soliton boundary extends beyond the visible matter. The CD determines this thickness through its integers.

---

### XIV. WHAT THIS NOTEBOOK CHANGES

Before this notebook, the RUM framework treated boundaries as abstract separators between hierarchy levels. The readings at each level were computed, but the boundaries themselves were not characterized.

After this notebook, the boundaries are the central objects. Each boundary is a threshold where a coupling reaches criticality. Each boundary is positioned by exact fractional beta coefficients. Each boundary hosts solitons (stable configurations inside it). Each boundary has a thickness (set by how fast the coupling runs near the threshold). Each boundary communicates with other boundaries through the running of couplings.

The CD is not just a particle that modifies beta coefficients. It is a particle that reshapes every boundary in the hierarchy. Its effect is distributed: a tiny shift in each beta coefficient, propagated through the running to every boundary, shifting every soliton's reading by an exact fraction.

The computation program (Stages 1-6) is clear. The inputs exist in the pool. The first derivation function (Λ_QCD from running α_s through flavor thresholds) is the next concrete step.

---

**Status:** Active. Conceptual framework complete. Stage 1 derivation function next. Connects to PHYS-44 (sector splitting), Koide notebook (quark K at confinement scale), and program_beta_unification (α_s running through thresholds).

---

### Table A.1: The Soliton Hierarchy — Complete Boundary Catalog

| Level | Boundary name | Threshold energy | Governing coupling | β coefficient (SM) | β coefficient (CD) | Soliton inside | Breach method |
|---|---|---|---|---|---|---|---|
| Planck | Quantum gravity | 1.22 × 10¹⁹ GeV | all couplings unify | — | — | spacetime itself | — |
| GUT | Unification | 10¹⁵·⁵⁴ GeV | α_GUT ≈ 1/38 | all merge | all merge | baryon number conservation | proton decay |
| Electroweak | Symmetry breaking | 246 GeV (Higgs vev) | α₂, α₁ | b₂ = −19/6, b₁ = 41/10 | b₂ = −13/6, b₁ = 25/6 | massive W, Z, fermion masses | collider energy > 246 GeV |
| CD threshold | CD pair production | > 1500 GeV | α_s, α₂ | n/a (CD absent) | CD decouples below | CD pair itself | collider energy > M_CD |
| Top threshold | Top decoupling | 172.7 GeV | α_s | b₃: nf=6 → nf=5 | same below M_CD | top quark | collider energy > m_t |
| Bottom threshold | Bottom decoupling | 4.18 GeV | α_s | b₃: nf=5 → nf=4 | same | bottom quark | collider energy > m_b |
| Charm threshold | Charm decoupling | 1.27 GeV | α_s | b₃: nf=4 → nf=3 | same | charm quark | collider energy > m_c |
| Confinement | Color confinement | Λ_QCD ≈ 200-300 MeV | α_s → ∞ | b₃ = −7 (6 flavors) | b₃ = −20/3 (above M_CD) | proton, neutron, pion | DIS energy > Λ_QCD |
| Nuclear | Nuclear binding | ~8 MeV/nucleon | Residual strong (pion) | derived from α_s | derived | nucleus | E > binding energy |
| Atomic | Electron binding | 13.6 eV (hydrogen) | α_em = 1/137 | b₁ = 41/10 | b₁ = 25/6 | atom | E > ionization energy |
| Molecular | Chemical binding | 1-10 eV | α_em (shared) | same b₁ | same | molecule | E > dissociation energy |
| Planetary | Gravitational | GM²/R | Φ/c² ≈ 10⁻¹⁰ | not gauge | not gauge | planet | E > gravitational binding |
| Stellar | Gravitational | GM²/R | Φ/c² ≈ 10⁻⁶ | not gauge | not gauge | star | E > gravitational binding |
| Galactic | Gravitational + DM | GM²/R × A | Φ/c² × (22/13)π | not gauge + integer | not gauge + integer | galaxy | E > virial energy |

### Table A.2: Beta Coefficients Through Flavor Thresholds

| Energy range | Active flavors n_f | b₃ (SM) | b₃ formula | Numerical |
|---|---|---|---|---|
| Above M_CD (> 1500 GeV) | 6 + CD pair | −20/3 | −11 + 2n_f/3 + 1/3 | −6.667 |
| m_t to M_CD (173–1500 GeV) | 6 | −7 | −11 + 2(6)/3 | −7.000 |
| m_b to m_t (4.2–173 GeV) | 5 | −23/3 | −11 + 2(5)/3 | −7.667 |
| m_c to m_b (1.3–4.2 GeV) | 4 | −25/3 | −11 + 2(4)/3 | −8.333 |
| m_s to m_c (0.1–1.3 GeV) | 3 | −9 | −11 + 2(3)/3 | −9.000 |
| Below m_s (< 100 MeV) | 3 (light quarks) | −9 | same | −9.000 |

The CD contributes only above its mass threshold. Below M_CD, the SM running applies at every stage. The confinement scale Λ_QCD is reached far below M_CD, so the CD affects Λ_QCD indirectly: it changes α_s at high energies, which propagates downward through all the flavor thresholds.

### Table A.3: The Proton — Soliton Properties

| Property | Value | Source | What determines it |
|---|---|---|---|
| Inertia (mass) | 938.272 MeV | pool: mass_proton_v0 = 93827208943/100000000 | 99% from confinement energy |
| Quark content | uud | Standard Model | SU(3) representation |
| Valence quark mass contribution | ~9 MeV (u+u+d) | pool: mass_up_quark + mass_down_quark | ~1% of total inertia |
| Confinement energy contribution | ~929 MeV | Difference | ~99% of total inertia |
| Charge radius | 0.841 fm | pool: spectro_proton_charge_radius_v0 | Spatial extent of confinement boundary |
| Spin | 1/2 | Standard Model | Quark spin + orbital angular momentum |
| Lifetime | > 10³⁴ years | SuperK bound | Topological stability of soliton |
| Predicted decay mode | p → e⁺π⁰ | GUT (SU(5)) | Baryon number violation at GUT boundary |
| Lattice mass computation | 936 ± 25 MeV | BMW 2008 | Non-perturbative QCD |
| Lattice factor C = m_p/Λ_QCD | ~4.7 | Lattice estimate | Soliton topology (uncomputed analytically) |

### Table A.4: The Neutron-Proton Mass Difference — Budget

| Contribution | Value | Sign | Coupling involved | CD effect |
|---|---|---|---|---|
| Down-up quark mass difference | +2.3 MeV | neutron heavier | Yukawa / Higgs | Indirect via EW boundary |
| EM self-energy of proton | −1.0 MeV | proton heavier | α_em | Indirect via b₁ running |
| Net mass difference | +1.293 MeV | neutron heavier | Both | Both modified |
| Pool value | 129333251/100000000 MeV | | mass_neutron_proton_diff_v0 | |
| Lattice computation | 1.51 ± 0.30 MeV | | BMW 2015 | Consistent with measurement |
| Sensitivity to quark mass ratio | Δ(m_n−m_p)/Δ(m_d−m_u) ≈ 1 | | | 1:1 propagation |
| Sensitivity to α_em | Δ(m_n−m_p)/Δα ≈ −7 MeV | | | Strong leverage |

### Table A.5: CD Effect Propagation Chain

| Step | What changes | Changed by | Magnitude of change | Exact fraction? |
|---|---|---|---|---|
| 1. β coefficients | b₁, b₂, b₃ | CD representation content | Δb = (1/15, 1/3, 1/3) | Yes — group theory |
| 2. Coupling running | α₁(μ), α₂(μ), α₃(μ) | Modified betas | ~1% per decade in log μ | Yes — RGE is exact at one-loop |
| 3. Unification scale | M_GUT | Modified crossing | 10¹⁵·⁵⁴ GeV | Yes — from crossing equation |
| 4. α_s at M_Z | α_s(M_Z) | Running from M_GUT | 0.1184 vs measured 0.118 | Yes — 0.33% miss |
| 5. Confinement scale | Λ_QCD | α_s running through thresholds | ~5% shift (estimate) | Yes — through exact b₃ fractions |
| 6. Proton mass | m_p = C × Λ_QCD | Shifted Λ_QCD | ~5% × C (estimate) | Partially — C from lattice |
| 7. Pion mass | m_π ~ √(m_q × Λ_QCD) | Shifted Λ_QCD and running m_q | ~2.5% (estimate, sqrt) | Partially — ChPT formula |
| 8. Nuclear force range | r ~ 1/m_π | Shifted m_π | ~2.5% inverse | Partially |
| 9. Nuclear binding | E_B ~ f(m_π, Λ_QCD) | Multiple shifts | complex | Requires nuclear calculation |
| 10. Neutron-proton difference | m_n − m_p | Shifted m_q and α_em at Λ_QCD | small | Partially |

### Table A.6: All Solitons — Classified by Boundary

| Soliton | Boundary | Topology | Stable? | Inertia | What sets the inertia |
|---|---|---|---|---|---|
| Proton | Confinement | Sphere (genus 0) | Yes (> 10³⁴ yr) | 938.3 MeV | Λ_QCD × C |
| Neutron | Confinement | Sphere (genus 0) | No (τ = 880 s) | 939.6 MeV | Λ_QCD × C + EM correction |
| Pion (π⁺) | Confinement (boundary mode) | — | No (τ = 26 ns) | 139.6 MeV | √(m_q × Λ_QCD³)/f_π |
| Pion (π⁰) | Confinement (boundary mode) | — | No (τ = 8.4 × 10⁻¹⁷ s) | 135.0 MeV | √(m_q × Λ_QCD³)/f_π |
| Hydrogen atom | Atomic | Sphere | Yes | 938.8 MeV | m_p + m_e − 13.6 eV |
| Helium-4 | Nuclear | Sphere | Yes | 3727.4 MeV | 4 × m_N − 28.3 MeV |
| Deuteron | Nuclear | — | Yes | 1875.6 MeV | m_p + m_n − 2.22 MeV |
| Earth | Planetary gravitational | Sphere | Yes | 5.97 × 10²⁴ kg | Gravitational accretion |
| Sun | Stellar gravitational | Sphere | Yes (5 Gyr remaining) | 1.99 × 10³⁰ kg | Gravitational accretion |
| Milky Way | Galactic gravitational + DM | Toroid (disk + halo) | Yes | ~10⁴² kg | Gravitational + DM amplification |
| Electron | EW / Planck (?) | Sphere | Yes | 0.511 MeV | Unknown — deepest open problem |

### Table A.7: Λ_QCD Computation — Required Pool Values

| Pool key | Value | Role in Λ_QCD computation |
|---|---|---|
| coupling_alpha_s_mz_v0 | 59/500 = 0.118 | Starting coupling at M_Z |
| mass_z_boson_v0 | 455938/5 = 91187.6 MeV | Reference scale μ₀ |
| mass_top_quark_v0 | 172570 MeV | Top threshold (n_f: 6→5) |
| mass_bottom_quark_v0 | 4183 MeV | Bottom threshold (n_f: 5→4) |
| mass_charm_quark_v0 | 1273 MeV | Charm threshold (n_f: 4→3) |
| mass_strange_quark_v0 | 187/2 = 93.5 MeV | Strange threshold (n_f: 3→3 effective) |
| beta_sm_su3_total_v0 | −7 | SM b₃ at n_f = 6 |
| beta_modified_su3_total_v0 | −20/3 | CD b₃ above M_CD |
| cd_mass_lower_bound_v0 | 1500000 MeV = 1500 GeV | CD threshold (n_f: 6→6+CD) |
| cd_mass_reference_v0 | 3000000 MeV = 3000 GeV | CD reference mass |
| geom_pi_v0 | Q335 Fraction | π in running formula |

All values present in pool. The derivation function for Stage 1 reads these 11 values and outputs Λ_QCD(SM), Λ_QCD(CD), and their ratio.

### Table A.8: Boundary Thickness Estimates

| Boundary | Thickness parameter | SM value | CD modification | Physical meaning |
|---|---|---|---|---|
| Confinement | 1/\|b₃\| | 1/7 = 0.143 | 3/20 = 0.150 | Rate of α_s transition from perturbative to non-perturbative |
| Electroweak | 1/\|b₂\| | 6/19 = 0.316 | 6/13 = 0.462 | Rate of SU(2) coupling transition at symmetry breaking |
| EM (high energy) | 1/\|b₁\| | 10/41 = 0.244 | 6/25 = 0.240 | Rate of U(1) coupling running (screening) |
| GUT | 1/\|Δb\| at crossing | depends on pair | depends on pair | Rate of coupling convergence at unification |

Larger thickness = softer boundary = more gradual transition. The CD makes the confinement boundary 5% thicker (0.150 vs 0.143) and the electroweak boundary 46% thicker (0.462 vs 0.316). The EM boundary barely changes (2% thinner).

### Table A.9: What Each Stage of the Research Program Requires

| Stage | Derivation | Pool inputs | Non-pool inputs | Output | Difficulty |
|---|---|---|---|---|---|
| 1. Λ_QCD | Running α_s through thresholds | 11 values (Table A.7) | None | Λ_QCD(SM), Λ_QCD(CD), ratio | Close — one function |
| 2. Proton mass | C × Λ_QCD | Stage 1 output | C ≈ 4.7 from lattice | m_p(predicted), miss | Close — uses Stage 1 |
| 3. Quark Koide at Λ_QCD | Running quark masses to Λ_QCD | Quark masses, α_s | None | K, a² at confinement scale | Close — running machinery exists |
| 4. Pion mass | ChPT formula | m_u, m_d at Λ_QCD, f_π | f_π ≈ 93 MeV (measured) | m_π(predicted), miss | Medium — needs f_π in pool |
| 5. n-p mass difference | QCD + QED at Λ_QCD | Multiple couplings, masses | Lattice EM correction | Δm(predicted), miss | Medium-far — complex matching |
| 6. All boundaries | Generalize Stage 1 | All betas, all thresholds | None | Complete boundary catalog | Medium — systematic |
| 7. Soliton equation | New mathematics | — | — | Analytical C, Koide a², mass hierarchy | Far — unwritten |

### Table A.10: Connections to Existing Framework

| This notebook | Connects to | Through | What it adds |
|---|---|---|---|
| Λ_QCD computation | program_beta_unification | α_s running, b₃ | Extends running below M_Z to confinement |
| Proton mass | PHYS-42 GR results | m_p used in gravitational tests | Partial derivation of a GR input |
| Quark Koide at Λ_QCD | Koide notebook Paths B, E | Running quark masses to specific scale | Identifies the natural scale for quark Koide |
| Boundary thickness | PHYS-44 sector splitting | β differences determine splitting | Thickness = how sharply sectors separate |
| Pion mass | BBN chain | Nuclear rates depend on m_π | Propagation from CD to primordial abundances |
| n-p mass difference | BBN chain | Neutron lifetime, He-4 abundance | Most sensitive BBN parameter |
| All boundaries catalog | PHYS-41 soliton hierarchy | Quantifies each hierarchy level | Boundaries become computed, not assumed |
| Soliton equation | Chapter 7 (book) | The deepest open problem | Would complete the framework |

### Table A.11: The 1/3 Shift — Group Theory Origin

| Quantity | Value | Where it comes from |
|---|---|---|
| SU(3) fundamental representation Dynkin index | 1/2 | Group theory of SU(N): T(fund) = 1/2 |
| One Weyl fermion contribution to b₃ | 2/3 × T(fund) × n_colors = 2/3 | Standard formula |
| One Dirac fermion contribution to b₃ | 2 × 2/3 × T(fund) = 2/3 | Dirac = 2 Weyl |
| CD vector-like pair contribution to b₃ | 1/3 | pool: beta_cabibbo_doublet_su3_shift_v0 |
| SM gluon self-interaction | −11/3 × C₂(adj) = −11 | pool: group_gauge_coeff_yang_mills_v0 = −11/3 |
| SM 6 quark flavors contribution | 6 × 2/3 = 4 | 6 Dirac fermions |
| SM total b₃ | −11 + 4 = −7 | pool: beta_sm_su3_total_v0 |
| CD total b₃ | −7 + 1/3 = −20/3 | pool: beta_modified_su3_total_v0 |

### Table A.12: Measurable Consequences of Boundary Shifts

| Observable | Current value | Depends on | CD shifts it through | Measurable? |
|---|---|---|---|---|
| Λ_QCD | 200-300 MeV | b₃, α_s(M_Z) | Δb₃ = 1/3 | Yes — computable from pool |
| Proton mass | 938.3 MeV | Λ_QCD × C | ΔΛ_QCD | Partially — needs lattice C |
| Proton charge radius | 0.841 fm | Λ_QCD, α_s | ΔΛ_QCD | Partially — needs lattice |
| Pion mass | 135-140 MeV | √(m_q × Λ_QCD) | ΔΛ_QCD, Δm_q running | Yes — ChPT formula |
| Nuclear force range | ~1.4 fm | 1/m_π | Δm_π | Yes — from pion mass |
| n-p mass difference | 1.293 MeV | m_d−m_u at Λ_QCD, α_em | Δ(running masses), Δα_em | Partially — complex matching |
| Deuteron binding | 2.224 MeV | Nuclear force from m_π | Δm_π propagated | Far — nuclear calculation |
| BBN He-4 abundance | Y_p = 0.245 | n-p mass diff, neutron lifetime | Δ(m_n − m_p) | Far — chain of dependencies |
| Jet fragmentation | Hadronization parameters | Λ_QCD, boundary thickness | ΔΛ_QCD, Δ(1/b₃) | In principle — LHC data |
| Sector splitting | ε ≈ 10⁻¹² | \|Δβ\| × ΔΦ/c² | β differences set by CD | Yes — Th-229 clock test |

### Table A.13: The Boundary Hierarchy — Threshold Energies Ordered

| Rank | Boundary | Threshold | log₁₀(E/MeV) | Separation from next | What lives between |
|---|---|---|---|---|---|
| 1 | Planck | 1.22 × 10²² MeV | 22.1 | 6.5 decades | Quantum gravity regime |
| 2 | GUT | 10¹⁵·⁵⁴ MeV | 15.5 | 2.7 decades | Desert (no new physics or CD) |
| 3 | CD threshold | ~3 × 10⁶ MeV | 6.5 | 1.1 decades | CD pair, 6-flavor QCD |
| 4 | Electroweak | 246000 MeV | 5.4 | 0.2 decades | Massive W, Z, top |
| 5 | Top threshold | 172700 MeV | 5.2 | 1.4 decades | 5-flavor QCD |
| 6 | Bottom threshold | 4183 MeV | 3.6 | 0.5 decades | 4-flavor QCD |
| 7 | Charm threshold | 1273 MeV | 3.1 | 0.7 decades | 3-flavor QCD |
| 8 | Confinement | ~250 MeV | 2.4 | 1.5 decades | Hadrons (p, n, π) |
| 9 | Nuclear | ~8 MeV | 0.9 | 5.7 decades | Nuclei |
| 10 | Atomic | 0.0000136 MeV | −4.9 | 0.7 decades | Atoms |
| 11 | Molecular | ~0.000001 MeV | −6.0 | 32 decades | Molecules, chemistry, life |
| 12 | Planetary grav | ~10⁻³⁸ MeV equiv | −38 | 6 decades | Planets |
| 13 | Stellar grav | ~10⁻³² MeV equiv | −32 | 6 decades | Stars |
| 14 | Galactic grav | ~10⁻²⁶ MeV equiv | −26 | — | Galaxies |

The hierarchy spans 48 orders of magnitude from molecular binding to the Planck scale in the gauge sector alone. Adding the gravitational boundaries extends it to 60+ orders. Every gauge boundary is positioned by an exact fractional beta coefficient. Every gravitational boundary is positioned by GM/(Rc²). The PHYS-44 sector splitting connects the two.

### Table A.14: Kill Conditions for the Research Program

| Kill condition | What it kills | Data source | Threshold |
|---|---|---|---|
| Computed Λ_QCD(CD) differs from standard Λ_QCD by > 50% | CD propagation to confinement is too large | Stage 1 computation | \|ΔΛ/Λ\| < 0.5 |
| Proton mass from C × Λ_QCD misses measured by > 10% | Lattice factor C is wrong or Λ_QCD computation fails | Stage 2 computation | miss < 10% |
| Quark Koide K ≠ 2/3 at any scale between 1 GeV and Λ_QCD | Quark Koide is not a boundary property | Stage 3 computation | K within 5% of 2/3 at some μ |
| Pion mass from ChPT + CD shifts misses by > 20% | CD propagation through confinement to pion is wrong | Stage 4 computation | miss < 20% |
| LHC finds no CD at any mass up to 6 TeV | CD does not exist (kills entire framework) | LHC Run 3 + HL-LHC | Direct search |
| Hyper-K sees no proton decay at 10³⁵ years | M_GUT prediction wrong (weakens but may not kill) | Hyper-K | τ_p > 10³⁵ yr |

---

