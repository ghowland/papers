## Chapter 4: What Unification Brings

Physics currently has walls.

Particle physics ends at the hadron. Nuclear physics picks up there and ends at the nucleus. Atomic physics picks up there and ends at the atom. Chemistry picks up there and ends at the molecule. Biology picks up there and ends at the organism. Astrophysics picks up at the star. Cosmology picks up at the universe.

Each discipline has its own language, its own approximations, its own textbooks, its own Nobel Prizes. The walls between them are treated as natural, "that's where my field ends and yours begins." But the walls are not in nature. They're in the departments.

Nature doesn't stop at the hadron and start over with new rules at the nucleus. The same physics that confines quarks inside a proton also binds protons and neutrons inside a nucleus, it's the residual strong force leaking through the confinement boundary. The same electromagnetic coupling that determines atomic energy levels also determines molecular bond strengths. The same gravitational reading that holds the Moon in orbit around the Earth also holds stars in orbit around the galaxy.

The walls are not boundaries in physics. They're boundaries in human attention. Unification tears them down.

---

### Omni-Domain Derivation

Here's what unification means in practice: a derivation chain that starts in one domain and ends in another, using nothing but integer transformation laws and standard physics at each step.

We already have chains crossing five domains:

Gauge theory → cosmology → nuclear physics → chemistry. The integers 11 and 13 from the gauge group produce (22/13)π, which gives the baryon density, which gives the baryon-to-photon ratio, which determines how much deuterium the universe contains. Deuterium, heavy hydrogen, the element that enables the nuclear fusion reactions that power the Sun. The amount of fuel available to every star in the universe was set by two integers from the weak force's beta function.

QED → atomic physics → spectroscopy. The electron's magnetic moment, measured in a trap at Harvard, produces α through five loops of quantum electrodynamics, which produces the Rydberg constant through an SI formula, which produces the hydrogen 1S-2S transition frequency through bound-state QED. The frequency at which hydrogen absorbs light, the most precisely measured number in science, determined by one measurement and integer arithmetic.

These chains exist today. They work today. They cross departmental walls as if the walls aren't there, because they aren't.

Now extend the principle. If the gauge integers determine the deuterium abundance, and the deuterium abundance determines the HD/H₂ ratio in primordial gas, and the HD/H₂ ratio determines the cooling efficiency of the first molecular clouds, and the cooling efficiency determines the minimum mass of the first stars, then the gauge integers determine stellar astrophysics.

If the first stars' masses determine which elements they produce in supernovae, and those elements determine the composition of the next generation of stars and planets, and the planetary composition determines the available chemistry, then the gauge integers determine chemistry.

If the chemistry determines which molecules are stable, which reactions are thermodynamically favorable, which polymers can form, then the gauge integers determine biochemistry.

This chain has not been computed. Each link is a separate research program. But the principle is clear: if integer fractions determine the boundary readings at the lowest level, and every higher level is built from the lower levels, then integer fractions determine everything. Not in some vague philosophical sense. In the concrete sense that you could, with enough computation, derive the protein folding energy landscape from the gauge group.

Nobody has done this because nobody had the chain. The chain is now visible. The links remain to be computed.

---

### Engineering from Integers

This isn't just philosophy. Integer-exact derivation has practical consequences.

**Semiconductor physics.** The band gap of silicon is 1.12 eV. This number determines every transistor, every solar cell, every integrated circuit. It is the energy gap that an electron must jump across to move from being stuck in the crystal lattice to being free to carry current. Too small and the material conducts all the time. Too large and it never conducts. Silicon's 1.12 eV sits in the sweet spot that makes modern electronics possible.

The band gap comes from the crystal structure of silicon (a repeating diamond-shaped lattice with atoms spaced 5.431 angstroms apart) and the electronic structure (how the electrons arrange themselves into energy bands inside that lattice). The crystal spacing comes from the silicon-silicon bond length, which comes from how the electron clouds of neighboring atoms overlap, which comes from the atomic wavefunctions, which come from the electromagnetic force strength α and the silicon nuclear charge (14 protons). Every step in that chain is standard physics. Every step uses α as an input.

Today, these computations are done numerically using density functional theory, a computational method that approximates the many-electron problem on a computer. The approximations achieve about 0.1 eV accuracy for band gaps, roughly 10% for silicon. The miss is not from unknown physics. It is from the difficulty of solving the many-body problem: tracking how all the electrons in a crystal interact with each other simultaneously. This is a computational barrier, not a physics barrier. The equations are known. Solving them exactly for a real material with billions of interacting electrons is beyond current methods.

The path from integer fractions to the band gap exists. The α is derived to 12 digits from the QED chain. The crystal geometry is measured to high precision by X-ray diffraction. The quantum mechanics connecting them is standard. The computational chain crossing from QED through atomic physics through solid-state physics to device performance has not been built in exact arithmetic. Building it requires solving the many-body problem at a level that current methods do not reach. The path is real. The computation is hard. Both facts are stated plainly.

**Fiber optics.** The attenuation of light in optical fiber, the loss per kilometer that determines how far a signal can travel, comes from two sources: scattering off density fluctuations in the glass (which depends on the fourth power of the wavelength) and absorption by the glass molecules themselves. Both depend on the electronic structure of silicon dioxide, which depends on α and the nuclear charges of silicon (14) and oxygen (8).

The standard telecommunications wavelength is 1550 nanometers, chosen because it sits at the minimum of the attenuation curve for silica fiber. The attenuation at that wavelength is about 0.18 decibels per kilometer. This number determines the maximum distance between optical amplifiers, the power budget of every submarine cable, and the economics of the global internet. It is currently empirical, measured in laboratories, not derived from the electromagnetic force strength. The derivation path from α through atomic structure through glass physics to fiber attenuation has not been computed.

**Channel spacing.** Modern fiber optic systems carry multiple signals on the same fiber at different wavelengths, each signal occupying its own narrow channel. The standard spacing between channels is 100 gigahertz, about 0.8 nanometers at the telecommunications wavelength. Tighter spacing means more channels and more total bandwidth, but risks interference between adjacent signals. The optimal spacing depends on the laser linewidth, the filter characteristics, and the nonlinear response of the glass, all of which trace back to atomic physics and the electromagnetic force strength.

There is a theoretical minimum spacing for zero interference between channels, set by the fundamental constants of the glass and the light. This number, the information-theoretic limit of fiber optic communication, has not been derived from first principles. The path from α to channel spacing crosses from quantum electrodynamics through atomic physics through materials science through optical engineering. Each crossing is standard physics. The full chain has not been built because it crosses too many departmental walls, not because any link is missing.

This is the method of the model. State the path. Identify each link. Note which links have been computed and which have not. Then compute them, test them against measurement, and publish the results regardless of whether they confirm or falsify the prediction. The paths described in this section have not been computed. They are stated here because the inputs are derived, the physics at each link is standard, and the chains are visible. What remains is the work.

---

### Medicine from Integers

The connection to biology is longer but real.

Drug design currently works by trial and error guided by computation. A pharmaceutical company identifies a target protein, screens millions of candidate molecules, selects a few hundred for testing, and advances a handful to clinical trials. The entire process takes 10-15 years and costs $1-2 billion per approved drug. The failure rate is ~90%.

The computational step, predicting whether a candidate molecule will bind to the target protein, is the bottleneck. Current methods (molecular dynamics, docking simulations, machine learning) achieve ~70% accuracy for binding prediction. The 30% error rate comes from approximations in the force fields, the mathematical descriptions of how atoms interact.

The force fields use empirical parameters. The Lennard-Jones potential for van der Waals interactions uses ε (well depth) and σ (collision diameter) fitted to experimental data. The Coulomb potential for electrostatic interactions uses partial charges fitted to quantum mechanical calculations. The bonded interactions (bond stretches, angle bends, torsions) use spring constants fitted to spectroscopic data.

Every one of these parameters traces back to α and the nuclear charges. The van der Waals well depth is determined by the polarizability, which is determined by the electronic structure, which is determined by α and Z. The partial charges are determined by the electron density distribution, which is determined by the same inputs. The spring constants are determined by the potential energy surface, which is determined by the same inputs.

If the force field parameters were derived from integers rather than fitted to data, the accuracy would be limited only by the level of theory used in the derivation, not by the quality of the empirical fit. And if the level of theory is integer-exact QED, the accuracy could in principle reach the ppb level, nine orders of magnitude better than current force fields.

This would not happen overnight. The chain from α to a protein-ligand binding affinity has hundreds of links. But each link uses known physics. Each link could be computed in Fraction arithmetic. Each link that's completed adds precision to every subsequent link.

The endpoint, predicting drug efficacy from gauge integers, is decades away. But the direction is clear. The path is open. The walls between quantum electrodynamics and pharmacology are departmental walls, not physical ones.

---

### Climate from Integers

The absorption spectrum of CO₂ determines how much infrared radiation the atmosphere traps. This spectrum, the specific wavelengths at which CO₂ absorbs light, comes from the vibrational and rotational energy levels of the CO₂ molecule.

The energy levels come from the molecular geometry (linear, O=C=O) and the bond properties (bond length 1.16 Å, bond force constant ~1600 N/m). The bond properties come from the electronic structure of carbon and oxygen. The electronic structure comes from quantum mechanics applied to atoms with Z = 6 (carbon) and Z = 8 (oxygen) interacting through the electromagnetic coupling α.

The greenhouse effect, the warming of the planet by trapped infrared radiation, is determined by α and two integers (6 and 8). Not just influenced by them. Determined by them. The absorption wavelengths are where they are because the C=O bond vibrates at a frequency set by the nuclear charges and the electromagnetic coupling. Move α by 1% and the CO₂ absorption spectrum shifts. Move it by 10% and CO₂ might not absorb infrared at all.

Climate science currently treats the absorption spectrum as empirical data, measured in the lab, tabulated in databases (HITRAN), fed into atmospheric models. The derivation from first principles exists (computational quantum chemistry computes molecular spectra routinely) but uses floating-point arithmetic and semi-empirical corrections.

An integer-exact derivation would start from α (from the QED chain), compute the carbon and oxygen electronic structures, compute the CO₂ molecular geometry and force constants, compute the vibrational-rotational spectrum, and from that spectrum compute the greenhouse forcing. Every step uses known physics. The chain is computable.

The practical benefit: validated climate models. If the CO₂ absorption spectrum is derived from integers and matches measurement to high precision, the climate model built on that spectrum has a validated foundation. The derivation chain from gauge group → α → molecular spectra → atmospheric absorption → climate forcing would be fully traceable. Every approximation identified. Every uncertainty quantified from first principles, not from empirical fitting.

---

### The General Principle

The pattern is the same in every application:

1. An engineering or scientific problem depends on a material property or physical constant.
2. That property traces back through atomic/molecular/nuclear physics to the fundamental couplings.
3. The fundamental couplings are derivable from gauge integers.
4. Therefore the property is derivable from integers.

The chain is long. Each link is a research program. But the principle is that no link in the chain requires new physics. Every link uses known equations. Every link uses known mathematics. The only thing missing is the computation, and the willingness to cross departmental walls to perform it.

Unification doesn't mean finding one equation that replaces all of physics. It means connecting all of physics so that a derivation starting from the gauge group can reach any measurable quantity. The connections are the integer fractions. The derivations are standard physics. The result is omni-domain: every domain connected, every reading derivable.

---

### What Changes for Ordinary People

You don't need to derive protein folding from gauge integers to benefit from unification. The benefit comes from the organizational clarity.

**Understanding replaces mystery.** Dark matter is not a mystery if it's toroidal flow predicted by gauge integers at 725 ppm. The Hubble tension is not a crisis if it's a boundary reading effect. The cosmological constant problem is not "the worst prediction in physics" if the vacuum energy is the ground state reading of the outermost soliton. The muon g-2 anomaly is not "evidence of new physics" if it's a hadronic VP measurement dispute.

Every "crisis" in modern physics has the same structure: a measurement doesn't match a prediction, and the response is to propose new particles, new forces, new dimensions. The soliton boundary framework offers a different response: check which boundary you're reading from. The measurement might be correct and the prediction might be correct, and the disagreement might be because they're readings from different boundaries.

This doesn't solve every problem. But it provides a framework for asking the right question. Instead of "what new particle explains the discrepancy?" the question becomes "what boundary crossing produces the discrepancy?" The first question has infinitely many answers (you can always invent a new particle). The second question has a finite answer determined by the nesting structure.

**Education changes.** Instead of teaching four forces and hoping students see the unity later, teach one principle (boundary readings) and show how it produces four different values at four different scales. Instead of teaching quantum mechanics and general relativity as separate subjects, teach them as interior and exterior readings of the same soliton structure. Instead of presenting the Standard Model as a collection of particles and forces, present it as a gauge group, three letters, SU(3) × SU(2) × U(1), from which everything follows by integer arithmetic.

A student who understands soliton, vortex, and inertia can read the physics stack from Layer 0 to Layer 12 and see the universe as one connected system. That student doesn't need to choose between particle physics and cosmology. They're the same subject.

**Technology accelerates.** Every engineering optimization that currently requires empirical measurement, the band gap, the attenuation coefficient, the absorption spectrum, the binding affinity, becomes in principle derivable. Not overnight. Not easily. But derivably. The integer chain provides a path from fundamental constants to material properties that doesn't exist in the departmentalized structure. Following that path even partway, deriving one material property from first principles instead of measuring it, saves experimental effort and provides deeper understanding of why the property has the value it does.

---

### The Promise and the Honest Limit

The promise of unification is omni-domain derivation: start from integers, end anywhere. The honest limit is that most of the chains are long, many links are computationally expensive, and some links haven't been attempted.

We have computed: gauge integers → couplings → cosmological densities → primordial abundances (6 links, 5 domains, works to 0.12σ). We have computed: a_e → α → R∞ → f(1S-2S) (3 links, 4 domains, works to 0.44 ppb). We have computed: gauge integers → sin²θ_W → M_W → Γ_Z (4 links, 3 domains, works to 195 ppm).

We have not computed: gauge integers → silicon band gap. We have not computed: α → CO₂ absorption spectrum. We have not computed: gauge group → protein folding energy. These are future work, years or decades of future work.

But the path is open. Every chain that has been computed works. Every chain uses standard physics. Every chain can be extended. The walls are departmental, not physical. Tearing them down is engineering, not discovery.

The discovery is done. The universe is rational. What remains is computation.
