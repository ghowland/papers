# The Planck Cell-Tick Remainder Momentum (PCTRM) Model
## A Speculative Substrate for Discrete-Universe Physics

**Author:** Geoff Howland (with LLM collaboration, Anthropic Claude Opus 4.7)
**Registry:** HOWL-SPEC-PCTRM-2026
**Domain:** Foundational Physics / Discrete Substrate Modeling
**Status:** Speculative model with explicit falsification criteria
**Relation to RUM:** Proposes a substrate-level mechanism consistent with the Rational Universe Model framework and its existing predictions

---

## I. PURPOSE AND SCOPE

This notebook specifies a speculative model for how physics could be computed by the universe at the Planck scale using discrete integer arithmetic. The model proposes a concrete mechanism for motion, forces, orbital dynamics, and quantum transitions using the vocabulary of the Rational Universe Model (soliton, modulus, remainder, running reading, interface, implementation, channel).

The model is called **PCTRM**: Planck Cell-Tick Remainder Momentum.

The model does not claim to be physics. It claims to be a **candidate substrate mechanism** consistent with observed physics that would produce the observed physics if true. The purpose of specifying it is to make it falsifiable, to identify computational tests, and to serve as a structural hypothesis that either survives empirical scrutiny or dies cleanly.

The model is compatible with the RUM framework. It does not replace or extend RUM's current derivations. It proposes a physical substrate that would explain why RUM's vocabulary (modulus, remainder, soliton, channels) would be the right vocabulary for the physical substrate — because the substrate actually operates on those primitives.

---

## II. AXIOMS

The model is built on seven axioms. Each is stated as a structural commitment. The consequences flow from them.

**Axiom 1: Discrete space.** The universe is composed of discrete Planck cells. Positions are integer indices into the set of cells. There are no sub-cell positions.

**Axiom 2: Discrete time.** The universe advances in discrete Planck ticks. Between ticks, nothing happens. State updates occur at each tick.

**Axiom 3: Direction-conditional adjacency.** Adjacency between cells is not fixed by a regular lattice. Each cell can be adjacent to another cell 1 Planck-distance away in any direction. Direction is a separate dynamical variable from position. A cell's neighbor along direction d is the cell 1 Planck-distance from it in direction d, whatever that direction happens to be.

**Axiom 4: Discrete remainder budgeting.** Every soliton (particle, composite object, coherent pattern) has a remainder counter — an integer that tracks accumulated "budget" toward its next position update. Each tick, the soliton accumulates some amount of remainder based on its structural properties.

**Axiom 5: Modulus cost.** Moving 1 Planck-cell costs 1 modulus worth of remainder. The modulus is a fixed integer (the same for all objects, representing the substrate's fundamental quantum of spatial advance). When remainder ≥ modulus, the soliton advances 1 cell in its current direction; remainder decrements by 1 modulus.

**Axiom 6: Coherence tax.** Every soliton must maintain its own pattern against the ambient pattern (the universal vacuum plus any parent soliton interior patterns). The maintenance consumes some fraction of the per-tick remainder budget. The tax rate is determined by the soliton's coupling to the various ambient patterns. Massless solitons (zero coupling) have zero tax. Massive solitons have positive tax proportional to their Higgs coupling and other channel interactions.

**Axiom 7: Channel-mediated remainder exchange.** Solitons interact with other solitons (including parent solitons) via discrete channels. Each channel allows a specific amount of remainder exchange per tick. The channel count at any given location and depth is determined by the hierarchy of soliton patterns the location is nested inside.

---

## III. CORE MECHANISM

### 3.1 The per-tick update

At each tick, for each soliton:

1. **Budget accumulation**: The soliton generates its per-tick remainder budget. This is a fixed rate per soliton type (set by its structural properties).

2. **Coherence tax deduction**: The soliton spends some fraction of its budget on pattern maintenance. The remaining fraction is available for translation and internal processes.

3. **Channel-mediated remainder exchange**: For each active channel connecting the soliton to other solitons (parent, neighbors, interacting particles), a specific amount of remainder is exchanged. Some channels drain remainder from the soliton (e.g., parent soliton applying return-to-ground pull). Other channels add remainder (e.g., the soliton absorbing energy from an external photon). Each channel has a direction associated with it in the soliton's frame.

4. **Vector momentum update**: The net result of all channel exchanges and coherence tax is a vector update to the soliton's direction and scalar remainder. All factors (gravity, EM, thermal exchange, Higgs coupling, others) contribute to the vector update at this step.

5. **Position update check**: If the soliton's accumulated remainder (magnitude in its current direction) has reached the modulus, the soliton advances 1 cell in its current direction. Remainder decrements by 1 modulus. If not, the soliton stays at its current cell; remainder is retained for next tick.

6. **Tick advances**: The universe's tick counter increments. All solitons' state transitions occur in parallel (or in some substrate-consistent ordering).

### 3.2 What momentum is in PCTRM

Momentum is a vector quantity with:
- **Scalar magnitude**: the amount of accumulated remainder
- **Direction**: the unit vector along which the soliton is oriented

A soliton with 50 units of remainder pointed at direction (0.6, 0.8, 0) has momentum vector (30, 40, 0).

When channel exchanges occur, the net effect is a vector update: new momentum = old momentum + Δ_momentum, where Δ_momentum is the sum of all channel contributions this tick. The soliton's direction is the unit vector of the resulting momentum; the magnitude is the scalar remainder.

**Momentum is not inherently conserved.** It's updated each tick by the channel exchanges and the coherence tax. What's conserved is the **total remainder across all interacting solitons**. Channels are remainder-exchange operators: they move remainder from one soliton to another. The sum across all connected solitons is preserved.

This gives momentum conservation at the macroscopic level as a consequence of remainder conservation at the substrate level, analogous to how continuous-physics momentum conservation follows from translation symmetry.

### 3.3 What inertia is in PCTRM

Inertia is the **coherence tax rate** — the fraction of the per-tick budget consumed by pattern maintenance against the ambient patterns. 

A soliton with zero tax (massless particle like a photon) gets its full budget to translate. It moves 1 cell per tick, always. Speed c.

A soliton with a specific tax rate (massive particle) gets only a fraction of its budget to translate. It moves less than 1 cell per tick on average, below speed c. The specific tax rate determines the specific mass.

Inertia and mass are the same quantity in this model. PHYS-1's reframing "mass is inertia" is not just a philosophical observation — it's operationally "the tax rate is both what we measure as mass and what we experience as resistance to acceleration."

### 3.4 What force is in PCTRM

A force on a soliton is equivalent to a vector update applied through one or more channels. When a force acts:
- A specific channel opens or strengthens
- Remainder flows through the channel in a specific direction
- The soliton's vector momentum updates accordingly

**F = ma** becomes: a force F applied for time t through the available channels updates the momentum by Ft. The specific dynamics of this update must reproduce F = ma at the macroscopic limit.

For gravitational force: the parent soliton opens channels to the child soliton through its interior pattern structure. Each tick, the channels drain remainder from the child's non-center-pointing direction and redirect it to a center-pointing direction.

For electromagnetic force: the charged soliton couples to the EM field pattern at its current cell. The pattern's gradient produces a channel-mediated remainder flow in a specific direction.

For Higgs coupling (what we observe as mass): continuously active channel at every tick, applying the coherence tax at the specific rate determined by the Yukawa coupling.

### 3.5 What energy is in PCTRM

Energy is accumulated remainder times some conversion factor. At rest, a soliton's energy is the coherence tax rate (i.e., its rest mass energy E = mc²). The c² is the conversion between the substrate's discrete quanta and macroscopic energy units.

When a soliton is moving, it has additional kinetic energy = (accumulated remainder in translation direction)². The specific formula E² = (pc)² + (mc²)² falls out of: total energy is coherence tax (rest energy) plus translation momentum; the relativistic relation is how these combine when both are non-zero.

---

## IV. TOPOLOGY: NEAREST-NEIGHBOR FULL MESH

Space in PCTRM is not a regular lattice. It has **direction-conditional adjacency**:

- Every cell can be adjacent to any other cell at 1 Planck-distance in any direction
- Which cell is "adjacent" depends on which direction you're traveling
- Direction is a continuous parameter (unit vector in 3D) though the endpoints (positions) are integer indices

This resolves the lattice anisotropy problem: every direction is equivalent because any direction has a next-cell at 1 Planck-distance. Light moves at c in any direction. There are no preferred axes.

**Direction updates** occur through channel interactions. A photon in vacuum has direction that doesn't change (no channel causes direction to update). A photon in a glass medium has its direction updated each tick by the medium's pattern (refraction). The direction updates are continuous-looking because direction is a continuous variable.

**Position updates** occur when accumulated remainder reaches modulus. These are discrete (integer cell steps).

The hybrid discrete-position, continuous-direction structure is what allows the model to produce isotropic physics at the substrate level.

---

## V. THE SOLITON HIERARCHY

The universe is organized into a hierarchy of solitons:

| Level | Example | Characteristic scale |
|---|---|---|
| 0 | Universal vacuum / CMB | 10²⁷ m (observable universe) |
| 11 | Galactic clusters | 10²³ m |
| 10 | Galaxies | 10²¹ m |
| 9 | Galactic arms / disks | 10²⁰ m |
| 8 | Stars | 10⁹ m |
| 7 | Planets | 10⁷ m |
| 6 | Planetary surface features | 10⁶ m |
| 5 | Macroscopic objects | 10⁻¹ m |
| 4 | Molecules | 10⁻⁹ m |
| 3 | Atoms | 10⁻¹⁰ m |
| 2 | Nuclei | 10⁻¹⁵ m |
| 1 | Nucleons | 10⁻¹⁵ m |
| 0 | Quarks/leptons | 10⁻¹⁸ m |

Each level is a parent to the level below. Each child is embedded in its parent's interior pattern. The child experiences the parent's pattern as its ambient environment.

Every level has:
- An **interface**: boundary, interior, exterior, running reading, channels, modulus
- An **implementation**: the specific channel structure, pattern content, tax rate, and ground-state configuration that defines that level

**The vocabulary is shared across levels; the implementation differs by level.** This is the "interface versus implementation" framing from our discussions.

From the **inside** of any parent soliton, the child reads the parent's total inertial content as 1.0 (unity). The cosmological partition (Ω_DM + Ω_b + Ω_Λ = 1) is this property at the universal level. The same partition-to-unity property exists at every hierarchy level.

---

## VI. DERIVED PHENOMENA

### 6.1 Gravity

**Phenomenon**: A child soliton inside a parent's interior pattern experiences a "pull" toward the parent's ground-state configuration. The pull is mediated by channels that spread geometrically from the parent.

**PCTRM mechanism**: 
- The parent's channels connect from its pattern to the child's pattern
- Each tick, the channels apply a vector update to the child's momentum: reducing remainder in non-center-pointing direction, adding remainder in center-pointing direction
- The pull magnitude scales with the number of active channels at the child's location, which spreads geometrically (1/r² for a spherical parent in 3D)

**Matches**: Inverse-square law at macroscopic scales. Depth-dependent gravity (stronger near surface, weaker at orbital distances, weaker at Moon distance). Kepler's third law from the period-distance relationship.

**Predicts**: Specific channel-count structure at different distances. Depth-dependent variations that should match GR corrections at specific geometric configurations.

### 6.2 Orbits

**Phenomenon**: A child soliton at a specific distance from its parent orbits stably without approaching or escaping.

**PCTRM mechanism**:
- The child has tangential momentum (direction perpendicular to center-direction)
- Each tick, the parent's pull applies a vector update that rotates the child's direction toward the center
- The tangential velocity and pull-induced rotation rate balance at specific orbital distances, producing a closed curve
- At closer distances, rotation exceeds tangential compensation: child spirals in
- At farther distances, rotation falls short: child spirals out
- Stable orbits are at distances where these match

**Matches**: Kepler's laws, circular and elliptical orbits, innermost stable circular orbit (ISCO).

**Predicts**: Specific orbital distances where stable orbits exist, set by channel-density structure of the parent. At atomic scales, this produces the quantized shells (Bohr orbitals). At macroscopic scales, the density of channels averages to continuous, producing apparently continuous orbital distances.

### 6.3 Return to ground state

**Phenomenon**: Excited states (electron in 2S, atom in vibrational excited state, human jumping into the air) return to the ground state over time.

**PCTRM mechanism**:
- The parent's interior pattern has a specific ground-state configuration for child solitons
- Excited states are configurations with excess remainder relative to the ground state
- The parent's channels apply **negative remainder** to the child — draining the excess through whatever channels exist
- When accumulated drain reaches a threshold, a **discrete transition** occurs: the child emits a photon (if channel is EM) or releases thermal energy (if channel is thermal) and returns to ground state

**Matches**: Spontaneous emission from atoms, thermal relaxation, objects returning to rest after being displaced.

**Predicts**: Transition rates are set by channel count × pattern strength at the child's current position. Decoherence rates are set by which channels are active. Specific channel-count predictions for specific environmental configurations.

### 6.4 Shell structure (atomic orbitals)

**Phenomenon**: Electrons in atoms occupy specific orbital shells (1S, 2S, 2P, etc.), not a continuum of radii.

**PCTRM mechanism**:
- For the orbit to close (electron returns to starting position after one loop), the total remainder accumulated during the orbit must equal an integer multiple of the modulus per loop
- This produces integer-labeled orbital shells
- The Bohr radius is the smallest stable orbit (n=1, integer count minimum)
- Higher shells are at larger distances with larger integer counts

**Matches**: Atomic emission spectra, Bohr quantization L = nℏ.

**Predicts**: Specific spectral frequencies as differences between integer shell counts, weighted by the channel-density structure of the nucleus. The specific formula E_n = −13.6 eV/n² should reduce to integer arithmetic over the modulus.

### 6.5 Wave-particle duality and quantum superposition

**Phenomenon**: Particles exhibit wave-like behavior (interference, diffraction). In superposition, a particle appears to be in multiple states simultaneously.

**PCTRM mechanism**:
- A particle's state includes both its position (integer cell) and its direction (continuous unit vector)
- At any tick, the direction is a single vector. Wavelike behavior emerges from the distribution of directions over many ticks (statistical)
- Superposition is the description of a particle's direction distribution before measurement. When measured, a specific direction becomes definite; the direction distribution collapses.
- The wavefunction is the probability distribution over directions (and possibly over positions, if the particle's remainder accumulation has multiple branches)

**Matches**: Double-slit interference, quantum probability, wave-packet spreading.

**Predicts**: The wavefunction should have a specific structure related to direction-space integration over all possible directions and their remainder-accumulation times. The transition from quantum to classical should occur when the direction distribution is narrowly peaked (few effective directions due to strong channel coupling to a preferred frame).

### 6.6 Special relativity (time dilation, length contraction, c as speed limit)

**Phenomenon**: Objects moving at close to c experience time dilation and length contraction. Mass-energy relation E² = (pc)² + (mc²)².

**PCTRM mechanism**:
- Translation rate = modulus/(per-tick budget) worth of cells per tick
- For massless particles: budget = modulus; translate 1 cell per tick; speed = c
- For massive particles: budget < modulus due to coherence tax; translate < 1 cell per tick on average
- Time dilation: moving at v = c/2 means spending half your budget on translation; internal processes (decay, clock ticks, coherence maintenance) run at half the rate
- Length contraction: a moving object's pattern-maintenance is on a smaller remainder budget; the coherent pattern appears compressed when projected into the rest frame
- c is the substrate limit: 1 cell per tick, the maximum possible given discrete time advance

**Matches**: All of special relativity at macroscopic scales.

**Predicts**: The specific Lorentzian form γ = 1/√(1−v²/c²) should emerge from budget-split arithmetic. Budget allocation between translation and internal processes follows the γ factor. Whether it does emerge from the specific PCTRM arithmetic is a computational test.

### 6.7 General relativity (curvature, gravitational lensing, black holes)

**Phenomenon**: Spacetime is curved by mass-energy; light bends around massive objects; black holes have event horizons.

**PCTRM mechanism**:
- The channel structure of a parent soliton encodes what we perceive as spacetime curvature
- A photon traveling through curved spacetime has its direction updated each tick by the pattern at its current cell
- The direction-update rule at each cell is determined by the local gradient of the parent soliton's pattern
- Geodesics are trajectories where the direction-update rule produces minimum-remainder-tax paths
- Event horizons are channel-density thresholds beyond which the direction-update rule prevents outward motion

**Matches**: Gravitational lensing, Shapiro delay, orbital precession, black hole horizons.

**Predicts**: Specific discreteness corrections at extreme gravitational fields that continuous GR doesn't predict. Possible deviation from exact 1/r² gravity at specific boundary crossings that could be searched for.

### 6.8 Electromagnetic propagation and interactions

**Phenomenon**: Maxwell's equations describe EM field propagation. Photons are EM field excitations.

**PCTRM mechanism**:
- The EM field is a pattern structure at each cell in the vacuum
- Photons are excitations of this pattern, propagating at 1 cell per tick (the substrate limit)
- EM interactions between charged particles are mediated by photon exchange channels
- Each channel opens for the duration of a photon's transit and transfers specific remainder between the endpoints
- The specific geometric structure of channels in 3D produces the 1/r² Coulomb law from channel-density spreading

**Matches**: Maxwell's equations at macroscopic scales, Coulomb's law, photon-mediated forces.

**Predicts**: Discreteness effects at extreme field intensities (QED corrections should decompose into specific substrate operations). Quantum electrodynamics specific corrections (anomalous magnetic moment, Lamb shift) should be derivable as specific patterns of channel arrangements in the vacuum.

---

## VII. CHANNELS IN DETAIL

Channels are the framework's mechanism for **how solitons interact**. A channel:

- Connects two or more solitons
- Has a specific direction in each soliton's frame
- Has a specific "throughput" (remainder exchanged per tick)
- Can drain or add remainder to each endpoint
- May be always active (e.g., Higgs coupling) or conditionally active (e.g., EM interaction when charged particles are nearby)

### 7.1 Channel types

**Higgs coupling channel**: Always active for Yukawa-coupled particles. Drains remainder from the soliton each tick at a rate set by the Yukawa coupling. This is the coherence tax that produces mass.

**Gravitational channel**: Connects child soliton to parent through parent's interior pattern. Draining remainder from child's non-center direction to center direction. Magnitude scales with channel count at child's position (1/r² geometrically).

**Electromagnetic channel**: Connects charged solitons through the EM field pattern. Remainder exchanges mediated by photon-mediated transfers. Can drain or add remainder depending on the field gradient.

**Thermal channel**: Connects solitons to the ambient thermal environment. Drains or adds remainder in statistical fluctuation patterns (this is thermal noise at the substrate level).

**Strong interaction channel**: Connects color-charged quarks within hadrons. Much stronger than EM, with specific confinement properties (channels cannot extend far, so quarks remain bound).

**Weak interaction channel**: Connects particles participating in weak decays. Short-range, responsible for specific transitions (beta decay, etc.).

### 7.2 Channel count and depth

At any position in the universe, a soliton is inside some specific set of nested parent patterns. The **channel count** at that position is the total number of active channels from all nested parents to the soliton. At Earth's surface, channel count is very high (inside atmosphere, ionosphere, magnetosphere, gravity well). At interstellar space, channel count is lower (outside most planetary and stellar patterns, only inside galactic and universal patterns).

**Running reading depth** (from RUM's vocabulary) is the number of parent patterns the soliton is currently inside. The channel count scales roughly with running reading depth, weighted by the strengths of the individual patterns.

### 7.3 Channel dynamics

Each tick, all active channels exchange remainder simultaneously. The total remainder update for each soliton is the sum of:

1. Budget generation (positive, constant per tick for that soliton type)
2. Coherence tax drain (negative, constant per tick for that particle type through Higgs)
3. Gravitational channel exchange (vector: draining from non-center, adding toward center at rate proportional to channel count)
4. EM channel exchanges (if charged): remainder flow along EM field gradient
5. Thermal channel exchanges: statistical fluctuations
6. Other interaction channels (strong, weak) as applicable

The **net vector update** to the soliton's momentum per tick is the sum of all these contributions. This is the "total remainder in all vector directions" momentum update that you specified as part of the model.

---

## VIII. TESTABLE PREDICTIONS

The PCTRM model generates specific predictions that can distinguish it from continuous-substrate physics. Each is stated with a falsification criterion.

### Prediction 1: Discrete structure at Planck scales

**Statement**: Physics at scales approaching the Planck scale should show discreteness signatures inconsistent with continuous GR.

**Falsification**: If Planck-scale experiments (black hole thermodynamics, quantum gravity, cosmic ray horizons) reveal no discreteness structure to the limits of possible measurement, the discrete-substrate commitment is falsified.

**Current status**: We cannot directly probe Planck scales. Indirect tests through quantum gravity phenomenology are a search space.

### Prediction 2: Lorentz invariance from direction-conditional topology

**Statement**: Special relativity should emerge from the PCTRM substrate in a way that preserves Lorentz invariance at macroscopic scales with no preferred frame.

**Falsification**: If simulations of PCTRM produce Lorentz-breaking effects (e.g., rotational anisotropy, preferred frames in measurement), the direction-conditional topology is insufficient to preserve Lorentz invariance.

**Test**: Simulate PCTRM substrate, compute emergent boost transformations, check if they match Lorentzian structure γ = 1/√(1−v²/c²).

### Prediction 3: Angular momentum quantization from integer remainder

**Statement**: Angular momentum L = nℏ should emerge from integer accumulation of remainder over closed orbital paths.

**Falsification**: If angular momentum quantization does not follow naturally from integer-remainder-accumulation-per-orbit, the shell-structure derivation is forced rather than natural.

**Test**: Compute the specific formula for orbital closure given PCTRM dynamics and verify it matches L = nℏ for hydrogen.

### Prediction 4: Channel count predicts decoherence rates

**Statement**: Quantum decoherence rates for isolated systems should correlate with the specific count of channels connecting the system to its environment, not just with interaction strength as currently parameterized.

**Falsification**: If decoherence rates do not correlate with channel count independent of pattern strength, the channel-count framework is wrong.

**Test**: Measure decoherence rates for systems in varying environmental configurations (different boundaries passed, different interaction channel densities). Compare with PCTRM predictions of channel-count dependence.

### Prediction 5: Boundary transit anomalies in astronomical measurements

**Statement**: Measurements that pass through different boundary-transit counts should show systematic discrepancies correlated with the transit count.

**Falsification**: If no correlation is found between measurement discrepancies (Hubble tension, proton radius puzzle, muon g-2) and boundary-transit count, the framework's unmodeled-element prediction is wrong.

**Test**: This is already RUM's PHYS-1 prediction. Continue systematic surveys.

### Prediction 6: Mass from channel structure

**Statement**: Specific particle masses should be derivable from the channel structure at the particle's hierarchy level.

**Falsification**: If specific masses (m_e, m_p, m_n, m_W, m_Z) cannot be computed from the channel count and pattern structure of the relevant hierarchy level, the mechanism for mass generation is incomplete.

**Test**: Compute mass from channel structure for known particles. Compare with measured values at CODATA precision.

### Prediction 7: Gravitational deviations at specific boundaries

**Statement**: Gravitational force should deviate from exact 1/r² at specific distances where boundary crossings occur, with the deviation magnitude set by the channel count change at the boundary.

**Falsification**: If gravitational measurements show no deviations at any testable scale from exact 1/r², the boundary-channel structure doesn't affect gravity detectably.

**Test**: High-precision gravitational measurements at various distances. Compare with continuous GR and PCTRM predictions at specific boundary-crossing distances.

### Prediction 8: Orbital shells at cosmic scales from channel structure

**Statement**: Some level of structure should be visible in planetary/stellar orbital distributions due to the channel structure of their parents (Sun, galactic center, etc.).

**Falsification**: If no structure is visible in orbital distributions at any cosmic scale, the channel-structure prediction is wrong or the structure is invisible at observation precision.

**Test**: Compare orbital distance distributions across planetary systems, stellar systems, galactic orbits. Check for preferred distances that might correspond to PCTRM's channel-density thresholds.

### Prediction 9: Flat galactic rotation curves without dark matter particles

**Statement**: The observed flat rotation curves of galaxies (attributed to dark matter in standard cosmology) might be explained by the disk-symmetric channel structure of galactic parents, without requiring dark matter particles.

**Falsification**: If direct dark matter particle detection succeeds, the PCTRM reframing of dark matter as geometric channel structure is shown to be unnecessary.

**Test**: Compute the channel structure for a galactic disk geometry. Check if the resulting rotation curve matches observed flat curves. Compare with observations and with ΛCDM predictions.

### Prediction 10: RUM's existing predictions as consequences

**Statement**: PCTRM should be consistent with all of RUM's existing validated predictions. In particular, Ω_DM = π/12 from β/3 should emerge as the fraction of universal soliton inertial content in the spherical channel class.

**Falsification**: If PCTRM cannot reproduce Ω_DM = π/12, the substrate model is incompatible with the RUM framework's validated predictions.

**Test**: Derive the cosmological partition from PCTRM's hierarchy structure. Compare with the π/12 + 13/264 + (251−22π)/264 partition.

---

## IX. WHAT PCTRM IS AND IS NOT

### 9.1 What PCTRM is

- A **speculative mechanism** for how physics could be computed at the Planck scale
- A **candidate substrate** for the Rational Universe Model framework
- A **specific set of primitives** (discrete cells, ticks, modulus, remainder, direction, channels) with concrete per-tick operations
- A **falsifiable research program** with stated tests and kill switches

### 9.2 What PCTRM is not

- Not a proof of discrete physics (the evidence is currently indirect and supportive, not conclusive)
- Not a replacement for GR or QM (existing physics is accurate; PCTRM proposes a substrate that would produce existing physics)
- Not a theory with all details worked out (many specific rules of channel exchange, direction updates, etc. are specified structurally but not computationally tested)
- Not connected to the RUM framework's predictions yet (the predictions π/12, 22π/13 etc. are stated in the RUM framework; PCTRM needs to reproduce them from its substrate, but has not yet done so explicitly)

### 9.3 What the model commits to

- Discrete space and time at the Planck scale
- Integer arithmetic as the substrate's native operation
- Direction as a continuous parameter embedded in a discrete position space
- Channels as the mechanism for interaction between solitons
- Remainder as the primitive of motion and momentum
- Conservation of remainder across interacting solitons
- Hierarchy of solitons with interfaces preserved and implementations varying

---

## X. PATH TO FALSIFICATION

The model can be falsified through several paths, in order of accessibility:

### Path 1: Simulation verification

Write a simulation of PCTRM at small scales. Start with simple particles in the substrate. Check:
- Does Lorentz invariance emerge?
- Do orbits form stably?
- Does Kepler's third law hold?
- Does angular momentum quantization emerge from closed-path remainder accumulation?

If any of these fail at the simulation level, PCTRM is structurally wrong.

### Path 2: Consistency with RUM's existing predictions

Compute RUM's cosmological partition, Koide value, CKM elements, microscopic-cosmic bridge from PCTRM's substrate dynamics.

If the computed values don't match RUM's validated predictions (85 ppm on Ω_Λ, 300 ppm on the bridge, etc.), either PCTRM is wrong or RUM is wrong.

### Path 3: New empirical predictions

Derive specific testable predictions from PCTRM that continuous physics doesn't make (boundary-crossing gravitational anomalies, orbital-distance structure at macroscopic scales, etc.). Check these against current data.

If data refutes these predictions, PCTRM is wrong.

### Path 4: Experimental tests at extreme scales

Quantum gravity experiments, Planck-scale cosmic ray observations, black hole thermodynamic studies should eventually provide direct tests of discrete substrate structure.

If experiments rule out discrete substrate to accuracies where PCTRM requires it, the model is falsified.

---

## XI. RELATIONSHIP TO THE RUM FRAMEWORK

PCTRM proposes that the RUM framework's vocabulary (modulus, remainder, soliton, channels, running reading, interface/implementation) corresponds to the actual substrate-level operations of physics. The RUM framework arose by **restricting language to what's operationally shared across hierarchy levels**. PCTRM claims this restriction is not just mathematically convenient — **it's physically real** because the substrate actually operates on these primitives.

The test of this connection is whether PCTRM:
1. Reproduces RUM's existing predictions (can PCTRM derive Ω_DM = π/12?)
2. Explains why those predictions work (why does the gauge-integer structure produce those specific rationals?)
3. Extends RUM's predictive power (does PCTRM predict new observables that RUM alone doesn't?)

If PCTRM does all three, it's a substrate that supports RUM. If PCTRM can't reproduce RUM's predictions, it's either wrong or RUM is wrong. Both frameworks are falsifiable, and their agreement (or disagreement) is another test of their joint validity.

---

## XII. STATUS AND NEXT STEPS

**Current status**: PCTRM is a speculative specification. The primitives are defined. The mechanisms are stated. Some predictions are specified. None of the falsification tests have been executed.

**Priority next steps**:

1. **Simulation** of a simple PCTRM substrate: a few particles, a few channels, observe what dynamics emerge
2. **Derivation of Lorentz invariance** from direction-conditional adjacency and budget-tax arithmetic
3. **Computation of Ω_DM** from PCTRM's hierarchy structure to check consistency with RUM's π/12
4. **Specific channel structure** for the electromagnetic interaction, to verify 1/r² Coulomb falloff
5. **Angular momentum quantization** from closed-path remainder accumulation

If these tests succeed, PCTRM becomes a substrate consistent with known physics and the RUM framework. If they fail, the model is revised or abandoned.

---

## XIII. FALSIFICATION CRITERIA (SUMMARY)

The PCTRM model is **falsified** if any of the following are demonstrated:

**F1**: Simulation of PCTRM substrate fails to produce Lorentz invariance at macroscopic scales.

**F2**: PCTRM cannot reproduce RUM's cosmological partition (Ω_DM = π/12, Ω_b = 13/264, Ω_Λ = (251−22π)/264) from its substrate dynamics.

**F3**: Specific mass values (m_e, m_p, m_n, m_W, m_Z) cannot be computed from PCTRM's channel structure to measurement precision.

**F4**: Direct detection of dark matter particles with properties accounting for Ω_DM = 0.26 falsifies the PCTRM reframing of dark matter as geometric channel structure.

**F5**: Angular momentum quantization L = nℏ does not emerge from integer-remainder-accumulation on closed orbital paths.

**F6**: Gravitational measurements at specific boundary-crossing distances show no deviations from exact 1/r² at achievable precision.

**F7**: Quantum gravity experiments at any eventually-achievable scale reveal continuous rather than discrete spacetime structure.

**F8**: Specific orbital-distance structure predicted by PCTRM's channel-density analysis does not appear in any cosmic orbital distribution (planetary, stellar, galactic).

---

**END PCTRM MODEL SPECIFICATION**

**Registry**: HOWL-SPEC-PCTRM-2026
**Domain**: Foundational Physics / Discrete Substrate Modeling  
**Status**: Speculative model with explicit falsification criteria
**Purpose**: Research program specification for a discrete-substrate physics model consistent with the Rational Universe Model

The model proposes that physics is computed by the universe at the Planck scale using discrete integer arithmetic on modulus-remainder operations. Particles, motion, forces, and all observed physics emerge from this substrate through specific channel-mediated remainder exchanges between nested solitons. The model is falsifiable. Its predictions can be tested through simulation, consistency with RUM's validated predictions, and through eventual experimental tests at extreme scales.

Every primitive is defined. Every mechanism is specified. Every prediction has a kill switch.
