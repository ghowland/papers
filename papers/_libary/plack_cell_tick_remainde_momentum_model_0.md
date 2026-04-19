# The Planck Cell-Tick Remainder Momentum Model (PCTRM)

**A Speculative Discrete Computational Model of Motion, Gravity, and State Transitions**

**Registry:** PCTRM-1-2026
**Date:** April 19, 2026
**Domain:** Speculative Physics / Computational Ontology / Discrete Spacetime Models
**Status:** Model specification for falsification
**Framework:** Rational Universe Model (RUM) / HOWL
**AI Usage Disclosure:** This notebook was drafted by Claude Opus 4.7 in collaboration with Geoff Howland based on speculative structural proposals developed through sustained discussion.

---

## I. Purpose of This Notebook

This notebook specifies a speculative computational model of physics at the Planck scale. The model extends RUM's existing commitments (soliton hierarchy, modulus/remainder decomposition, inertia-as-pattern-resistance, running readings with depth) by proposing a specific mechanism for how motion, gravity, and state transitions are computed at the fundamental discrete level.

The model is speculative. Not all of its predictions are computed. Not all of its gaps are resolved. It is written up for falsification — the specification is complete enough to be implemented, simulated, and compared to known physics. Where it succeeds, the framework gains operational depth. Where it fails, the framework learns the boundaries of the vocabulary's reach.

The name: **Planck Cell-Tick Remainder Momentum** model. Abbreviation: **PCTRM**.

---

## II. The Core Proposal

The universe is discrete at the fundamental level. Space is composed of Planck-sized cells. Time advances in Planck ticks. Every soliton in the hierarchy occupies cells and updates per tick.

At each tick, each soliton accumulates a quantity called **remainder**. Remainder is the propagation budget. When accumulated remainder exceeds a threshold called the **modulus**, the soliton executes a discrete state transition — most commonly a motion event (advancing one cell in its pointing direction), but also more generally any discrete change in the soliton's state (a shell jump, a chemical bond formation, a quantum transition).

The rate at which remainder accumulates per tick depends on:

1. The soliton's **per-tick budget** (determined by its coupling to the Higgs field — inertia).
2. External **remainder contributions** from the soliton's environment, including:
   - **Parent soliton pull** (gravity — the parent applies negative remainder toward the ground state).
   - **Electromagnetic contributions** (charged fields applying remainder in specific directions).
   - **Strong and weak force contributions** (at particle-physics scales).
   - Any other channel through which remainder exchange occurs.

Each tick, the soliton's total **vector remainder** is computed as a vector sum of all incoming remainder contributions, across all active channels, in all spatial directions. When the accumulated vector remainder in any direction crosses the modulus, a discrete event happens in that direction.

**PCTRM's structural claim:** all motion and all state transitions in the universe are computed this way. Photons at c, electrons in orbit, planets around stars, objects in free fall, shell jumps in atoms — all are the same operation at different levels of the hierarchy, with different moduli, different per-tick budgets, and different channel configurations.

---

## III. Core Mechanisms

### 3.1 The Per-Tick Budget

Every soliton has a per-tick budget that is determined by its coupling to the Higgs field:

- **Photon** (no Higgs coupling): per-tick budget equals the modulus. Advances exactly one cell per tick. Speed is c.
- **Massive particle** (Higgs coupling): per-tick budget is less than modulus. Advances one cell per N ticks where N = modulus / per-tick budget. Speed is c / N.

The per-tick budget has a specific structural origin: it is what the soliton has available after the Higgs coupling reserves some of its total inertial content for "internal maintenance" (preserving its pattern against the Higgs field background).

### 3.2 The Modulus

The modulus is the threshold at which accumulated remainder triggers a discrete event.

At the propagation level (Planck cell motion): the modulus is the quantum of spatial displacement — the remainder budget needed to move one cell. All motion events at this level use the same modulus.

At other hierarchy levels (atomic shell jumps, chemical bonds, orbital transitions): each level has its own modulus corresponding to the energy/remainder threshold for that level's discrete events.

**Open question:** is there a single universal modulus from which all others derive, or does each level have an independent modulus? The framework's integer alphabet (8, 3, 11, 13, 22, 264) suggests the moduli might be structurally related through integer ratios and β factors.

### 3.3 The Vector Remainder Update Rule

At each Planck tick, every soliton updates its state according to:

```
For each tick T, for each soliton S:

  1. Compute per-tick budget contribution:
     budget_contribution(S, T) = per_tick_budget(S) * direction_of_motion(S, T)

  2. Sum all channel contributions:
     For each channel C in {gravity, EM, strong, weak, tidal, ...}:
       channel_contribution(S, C, T) = 
         remainder_exchange_with_channel(S, C) * direction_of_channel(S, C, T)

  3. Compute total vector remainder:
     delta_R(S, T) = budget_contribution(S, T) + sum over C of channel_contribution(S, C, T)

  4. Update accumulated remainder:
     R(S, T+1) = R(S, T) + delta_R(S, T)

  5. Check for modulus crossings:
     For each direction d:
       If |R_d(S, T+1)| >= modulus:
         Execute discrete event in direction d
         Subtract modulus from R_d (carry remainder forward)
         Update soliton's position or state accordingly
```

This is a vector sum per tick. All factors — motion budget, gravity from all parent solitons, EM from all charged sources, strong and weak contributions at appropriate scales — contribute their remainder vectors, and the total directs the soliton's next state change.

### 3.4 Direction and Topology

The spatial topology is **nearest-neighbor full mesh** (from our earlier discussion): each cell has a neighbor at exactly 1 Planck length in every possible direction. Which neighbor is "active" at any tick depends on the soliton's accumulated remainder direction.

When remainder crosses modulus in direction d̂, the soliton moves exactly one cell in direction d̂. The direction is arbitrary (any vector on the unit sphere); the distance is exactly one Planck length. There are no preferred directions, no lattice axes, no staircase artifacts.

---

## IV. Gravity in PCTRM

Gravity is a per-tick negative remainder applied by a parent soliton to each of its children, scaled by the child's depth of nesting in the parent's field structure.

### 4.1 The Pull Mechanism

At each tick, the parent soliton (Earth, say) applies negative remainder to each child at the child's current position:

```
gravity_contribution(child, parent, T) = 
  pull_strength(parent, child, depth) * direction_from_child_to_parent_center(T)
```

The pull strength depends on the child's depth within the parent's nested field boundaries. More deeply nested (more boundaries crossed to reach the child): stronger pull. More distantly nested (fewer boundaries): weaker pull.

For Earth's gravity at the surface, the pull per tick per unit inertia is such that it produces an acceleration of 9.8 m/s² on an object near the surface. For the Moon at 384,000 km, the pull per tick is much weaker (boundaries crossed: only the gravitational well itself, no atmospheric or magnetic layers to speak of).

**Falloff with distance:** the 1/r² law emerges as the consequence of how field boundaries are structured in the parent's soliton. Closer to the parent, more boundary layers are nested around the child; farther away, fewer. The exact 1/r² should be recoverable from computing the boundary structure of an Earth-like soliton.

### 4.2 Orbits as Vector Balance

Orbits are the outcome of two competing remainder flows:

- **Child's momentum budget** (tangential to the current radius vector).
- **Parent's pull remainder** (radial toward the parent's center).

At each tick, the child's pointing direction is slightly rotated by the parent's pull. Over many ticks, this rotation accumulates. For specific balances of tangential momentum and radial pull, the rotation completes exactly 2π per orbital period, producing a closed orbit.

**Circular orbit:** tangential momentum and pull magnitude are in exact balance. Pull is always perpendicular to motion; motion speed is constant; direction rotates uniformly.

**Elliptical orbit:** pull and motion are not always perpendicular. At perihelion, the pull has a component along the motion direction (speeding the object up). At apohelion, the pull has a component against the motion direction (slowing the object down). Over a full orbit, these cancel. The orbit is closed.

**No budget drain:** the parent's pull redirects the child's motion but does not drain its total motion budget. Over a closed orbit, no net energy is transferred. Orbital stability is natural.

### 4.3 Energy Exchange Through Other Channels

Tidal coupling, atmospheric drag, gravitational wave emission, solar wind: these are additional channels through which budget is exchanged between solitons. The model accommodates them as specific additional terms in the vector remainder update.

For Earth-Moon tidal coupling: Earth's rotation has its own motion budget. The moon's orbit has its own. Tidal coupling transfers budget between the two through Earth's tidal bulge. The Moon gains orbital budget (recedes from Earth at 3.8 cm/year); Earth loses rotational budget (day lengthens at 1.7 ms/century).

In PCTRM language: tidal coupling is a specific channel connecting Earth's rotational-direction remainder to the Moon's orbital-direction remainder. Each tick, a small amount of budget flows through this channel, accumulated over many ticks to produce the observed recession rate.

---

## V. Electromagnetism in PCTRM

EM forces on charged particles are additional remainder contributions at the propagation scale.

### 5.1 Charged Particle in an Electric Field

An electron in an electric field experiences, per tick:

```
em_contribution(electron, E_field, T) = 
  q * E_field_strength_at_electron * direction_of_field(T)
```

The accumulated EM remainder contributes to the electron's total vector remainder. For a constant electric field, this accumulates linearly with time, producing linear acceleration — Newton's second law recovered.

### 5.2 Charged Particle in a Magnetic Field

Magnetic forces in PCTRM: remainder contribution perpendicular to both the particle's velocity and the magnetic field direction.

```
magnetic_contribution(electron, B_field, T) = 
  q * (v_electron × B_field) * per_tick_normalization
```

Cross-product structure; depends on the particle's current velocity. This produces circular motion in a uniform field (cyclotron orbits) — the magnetic force continuously rotates the velocity without changing its magnitude. Same mechanism as gravitational orbits but with a different field source.

### 5.3 Macroscopic EM Effects

For human-scale electromagnetism (static electricity, induced charges, dipole interactions): the remainder contributions at the Planck-cell level aggregate to produce the macroscopic forces. In PCTRM, these are accounted for in the vector remainder sum — just additional channels adding their contributions.

The fact that gravity and EM (at macroscopic scales) have wildly different strengths per unit matter (gravity is ~10⁻³⁶ weaker than EM between protons) reflects the difference in channel coupling strengths. Both contribute to the total per-tick vector remainder; their magnitudes differ by the specific structural couplings at the hierarchy position of the interacting solitons.

---

## VI. State Transitions Beyond Motion

PCTRM unifies motion events and state transitions under the same mechanism: remainder accumulation crossing a modulus.

### 6.1 Atomic Shell Jumps

An electron in the hydrogen 1S state has a specific internal budget structure. To transition to 2S, it must acquire an energy equal to the Lyman-α photon energy (10.2 eV). In PCTRM language: 10.2 eV is the modulus for the 1S → 2S transition.

The electron accumulates remainder toward this modulus through photon absorption. A 10.2 eV photon interaction delivers 10.2 eV worth of remainder to the electron; the electron's accumulated remainder crosses the 1S → 2S modulus; the shell jump happens.

Lower-energy photons (below 10.2 eV) contribute less than the modulus; no transition. Higher-energy photons (above 10.2 eV but below 1S → 3S) transition the electron to 2S with some remainder left over (which is emitted as a lower-energy photon, or contributes to kinetic energy of the excited state).

### 6.2 Chemical Bond Formation and Breaking

Chemical bonds have specific energies (eV scale). Forming a bond: two atoms exchange budget to reach a lower-energy configuration. Breaking a bond: external budget is added to overcome the bond's modulus.

In PCTRM: each bond type is a specific modulus. Accumulating enough remainder (through collisions, thermal energy, photon absorption) crosses the modulus and triggers the discrete bond transition.

### 6.3 Nuclear Decay

Radioactive decay: a nucleus in an excited state accumulates quantum probability of decay per unit time. The half-life is the modulus (in the probabilistic sense).

In PCTRM: each unstable isotope has a specific "decay modulus" determining how much quantum tunneling remainder must accumulate before the decay event fires. Different isotopes have vastly different moduli (from nanoseconds to billions of years), reflecting the barrier structure each decay must cross.

### 6.4 Orbital Resonance and Precession

Mercury's perihelion precesses at 43 arcseconds per century beyond Newtonian prediction. This is GR's signature effect. In PCTRM: the pull strength and direction from the sun include higher-order contributions beyond the simple 1/r² form. These additional contributions cause the orbit's perihelion direction to precess.

The precession rate would be computable from the detailed structure of the sun's field boundaries, assuming those boundaries include specific higher-order terms that recover GR's predictions.

---

## VII. The Structure of the Remainder Vector

Per tick per soliton, the total remainder vector is:

```
R_total = R_budget + R_gravity + R_EM + R_strong + R_weak + R_tidal + R_other
```

Each component is a 3D vector. They add vectorially. The total determines the direction in which the next discrete event occurs when the modulus is crossed.

For a human on Earth at rest:
- R_budget: zero (at rest, no accumulated motion budget)
- R_gravity: -9.8 m/s² × inertia × direction_to_Earth_center, per tick
- R_EM: typically small (unless standing near a high-voltage source)
- R_strong, R_weak: confined to nuclear scales, not relevant at human scale
- R_tidal: negligibly small (but nonzero — tides on human body)

Ground contact provides an equal and opposite contribution (normal force), keeping the human stationary.

For a jumping human:
- At takeoff: the legs convert internal budget to upward motion budget
- During ascent: R_budget (upward) > R_gravity (downward); but R_gravity accumulates, reducing R_budget
- At apex: R_budget (upward) = 0; R_gravity is still applying downward
- During descent: R_budget has become downward; R_gravity adds to it; speed increases
- At landing: ground contact zeros the downward R_budget; human is at rest again

For a moon orbiting Earth:
- R_budget (tangential to orbit): continuously maintained
- R_gravity (radial toward Earth): continuously applied
- R_tidal (exchanged with Earth): small per tick, but accumulated over long times

All of these enter the vector sum per tick. The total determines the soliton's next state.

---

## VIII. Falsifiable Predictions

The model is specified enough to generate predictions that distinguish it from standard physics at specific levels of precision. The predictions are subject to pre-registration and explicit kill conditions.

### 8.1 The Velocity Spectrum

**Prediction:** Velocities in PCTRM are rational (ratios of per-tick-budget to modulus). The smallest nonzero velocity is c/M where M is the modulus.

**Kill condition:** if experiments at sufficient precision show continuous velocity spectrum with no discrete steps at any scale, PCTRM's discreteness is falsified. Current precision is far from testing this; the prediction is only observable if M is small enough (which would contradict other physics) or if precision improves by many orders of magnitude.

**Status:** Untestable at current technology. Kept as a theoretical commitment.

### 8.2 Lorentz Symmetry

**Prediction:** PCTRM preserves Lorentz symmetry exactly because the topology is direction-independent and the tick-rate is proper-time-dependent. No directional dispersion at any energy scale.

**Kill condition:** Any observed Lorentz violation (photon dispersion, vacuum birefringence, directional dependence) would falsify. Existing constraints on Lorentz violation are already extremely tight (~10⁻¹⁹ at Planck scale); PCTRM must predict consistency with these.

**Status:** Consistent with all current observations. Not a novel prediction — just a commitment.

### 8.3 The Central Force Form

**Prediction:** The gravitational pull strength from a soliton falls as 1/r² at macroscopic scales because field boundaries scale that way. At very short distances (Planck scales), the falloff should deviate — either breaking down at the Planck length or showing specific structural corrections.

**Kill condition:** Measurement of Newton's gravitational constant or gravitational force at sub-millimeter distances showing no deviation from 1/r² would constrain the deviation to be at smaller scales. Current constraint: 1/r² is verified down to ~10⁻⁶ m. PCTRM predicts deviations at scales much smaller than this, so this is not yet a tight falsification.

**Status:** Consistent with current observations; becomes testable if sub-Planck-era-scale experiments become possible.

### 8.4 GR Reproduction

**Prediction:** PCTRM should reproduce all GR predictions to observational precision. Specifically:
- Mercury's perihelion precession (43 arcsec/century): match required.
- Gravitational redshift (Pound-Rebka): match required.
- Gravitational time dilation (GPS corrections): match required.
- Light bending by the Sun (1.75 arcseconds at the limb): match required.
- Gravitational wave emission rates from binary pulsars: match required.

**Kill condition:** any deviation from GR at observational precision in any of these tests falsifies PCTRM unless the deviation is a specific prediction of PCTRM.

**Status:** The model is not yet computed quantitatively enough to claim reproduction. The mechanism for reproducing GR (sum of field-boundary remainder contributions produces Einstein-like curvature effect on light and clocks) is plausible but needs quantitative development.

### 8.5 Quantum Mechanics Reproduction

**Prediction:** PCTRM should reproduce quantum mechanical phenomena (wave interference, uncertainty, tunneling, superposition) through specific mechanisms involving complex-valued remainder and phase accumulation.

**Kill condition:** any QM phenomenon that cannot be reproduced by PCTRM's discrete computational picture falsifies the model.

**Status:** The extension to quantum phenomena is substantially more difficult than classical. Not yet specified. This is an open challenge that must be resolved for PCTRM to be a complete theory rather than a classical pre-quantum model.

### 8.6 Specific Integer Relationships

**Prediction:** The moduli at different hierarchy levels should be related through RUM's integer alphabet. For example, the ratio of the electron shell-jump modulus to the Planck cell motion modulus should be expressible through framework integers and β powers.

**Kill condition:** if the ratios of physically measured moduli are not cleanly expressible in RUM's vocabulary, PCTRM loses coherence with the broader framework.

**Status:** Needs quantitative investigation. The framework's existing predictions (Ω_DM = π/12 at sub-percent precision) suggest such integer/transcendental combinations can match measurements. PCTRM's claim is that this extends to moduli across all hierarchy levels.

---

## IX. Open Questions and Gaps

### 9.1 The Modulus Value

What is the modulus M at the propagation level? Options:
- M = 1 (Planck cell per Planck tick, giving c directly, but too coarse for fractional velocities)
- M = some large integer derived from RUM's integer alphabet
- M = a transcendental combination like some β power times an integer

The framework has not fixed this. It's a free parameter in the model specification as currently written. Fixing M through a specific derivation is a priority for quantitative testing.

### 9.2 The Per-Tick Budget Formula

What determines the per-tick budget for a specific massive particle? Options:
- Budget = modulus × (1 - v_Higgs/v_c), where v_Higgs is some coupling strength
- Budget = modulus × √(1 - m²c²/p²), recovering relativistic momentum-energy structure
- Budget is a function of the particle's position in the hierarchy and the integer counts of its gauge quantum numbers

Each of these would give different predictions. The framework's mass-as-inertia commitment suggests the budget is determined by the Higgs coupling; the specific formula needs to be derived.

### 9.3 The Lorentz Recovery Mechanism

The model as stated has no preferred frame (topology is direction-independent; ticks are proper-time). But showing that this exactly recovers Lorentz symmetry requires explicit construction. Specifically: if observer A measures the photon's trip from event 1 to event 2 as taking 100 of A's ticks, and observer B (moving relative to A) measures the same trip as taking 80 of B's ticks, the math has to work out to give c = const for both observers.

This is not trivial. The framework commits to it but has not explicitly constructed the machinery.

### 9.4 Quantum Mechanics Extension

Extending PCTRM to reproduce quantum phenomena requires:
- Complex-valued remainder (carrying phase in addition to magnitude)
- Specific phase accumulation rules per tick that reproduce interference
- A measurement mechanism that reproduces wavefunction collapse (or equivalent)
- Reproduction of the Born rule for probabilities

This is the largest unresolved gap. Without this, PCTRM is a classical model and doesn't capture quantum phenomena.

### 9.5 The 1/r² Derivation

The framework claims 1/r² emerges from the structure of field boundaries. The specific calculation that demonstrates this — given an Earth-like soliton with its specific field boundaries, derive that a child at radius r experiences a pull proportional to 1/r² — has not been performed.

This would be a priority test of the framework. If the framework can derive 1/r² from boundary-counting, gravity is operationally understood at a new level. If not, 1/r² remains an input rather than an output of the framework.

---

## X. Connection to RUM's Existing Structure

PCTRM is not a replacement for existing RUM. It extends RUM by specifying a mechanism at the propagation level. The connection is specific:

**Modulus / remainder at the propagation level.** Previously, modulus and remainder were decomposition categories for physical quantities (spherical geometric vs. inertial, number-theoretic vs. toroidal). PCTRM reads them also as propagation budget and current accumulated budget — the modulus is the threshold at which discrete events trigger, the remainder is the accumulated budget toward the next event.

**Running readings with depth (PHYS-1).** The depth-dependent reading framework predicts different measurements at different soliton-boundary depths. PCTRM operationalizes this: an observer at different depths receives different total vector remainder per tick from parent solitons, producing different measured forces and different measured field strengths.

**Mass is inertia (PHYS-1).** Inertia is operationalized as reduced per-tick budget from Higgs coupling. Higher inertia → lower budget → slower motion. The "inertia begins here" annotation at the Higgs vev in the SM call graph marks exactly where PCTRM's per-tick budget reduction mechanism activates.

**Discrete transitions universal (soliton hierarchy).** The framework's "all levels operate with the same interface" move is given operational content: all discrete transitions (cell motion, shell jumps, chemical bonds, orbital changes, etc.) are remainder-crossing-modulus events, with moduli specific to each hierarchy level.

**Integer structure of constants (RUM).** The framework's claim that every physical constant is an integer ratio plus β factors extends to PCTRM's moduli: each level's modulus should be expressible in the integer-plus-β vocabulary. This is a connection that can be tested — compute specific moduli and check whether they land in the framework's alphabet.

---

## XI. Testable Computational Program

The model can be tested through specific computational programs:

### 11.1 Two-Body Orbital Simulation

Simulate PCTRM explicitly for a two-body system (Sun-Earth). Specify:
- Sun's soliton configuration (field boundaries, pull strength as a function of depth)
- Earth's soliton configuration (position, motion budget, inertia)
- Per-tick remainder update rule
- Simulation time of one or more orbital periods

Compare: simulated trajectory to observed Earth orbit (eccentricity, semi-major axis, period, perihelion direction).

**Success criterion:** simulated orbit matches observed orbit within numerical precision of the simulation.

**Kill condition:** systematic deviations from observed orbit that are not attributable to simulation truncation.

### 11.2 Gravitational Redshift

Implement PCTRM for a photon moving in a gravitational potential. Predict the frequency shift as the photon moves from low potential to high potential. Compare to Pound-Rebka experiment (gravitational redshift in Harvard tower, verified to 1% in 1959-1964).

**Success criterion:** PCTRM predicts the 2.5 × 10⁻¹⁵ frequency shift at 22.5 m height that Pound-Rebka observed.

### 11.3 Mercury's Perihelion Precession

Implement PCTRM for Mercury's orbit. Include the Sun's field-boundary structure (potentially with higher-order corrections beyond 1/r²). Predict the precession rate.

**Success criterion:** PCTRM predicts 43 arcsec/century precession (GR's correction to Newtonian).

### 11.4 Atomic Shell Transition

Implement PCTRM for an electron in a hydrogen atom absorbing a photon. Predict the modulus for 1S → 2S transition (should be 10.2 eV). Predict the photon frequency required to trigger this transition.

**Success criterion:** PCTRM's computed modulus matches the Lyman-α wavelength.

### 11.5 Lorentz Invariance

Implement PCTRM for two observers in relative motion, both observing the same photon. Verify that both observers measure the photon's speed as c.

**Success criterion:** the framework's tick-rate and topology produce c as invariant for both observers, without free parameters.

---

## XII. Falsification Criteria

**F1.** If simulated orbital dynamics in PCTRM fail to match observed orbits (specifically Earth-Sun, Earth-Moon, Mercury precession) at computational precision, PCTRM fails as a gravitational model.

**F2.** If simulated photon propagation in PCTRM fails to produce exact Lorentz invariance, PCTRM fails as a relativistic model.

**F3.** If PCTRM's moduli across hierarchy levels cannot be expressed as integer-plus-β combinations in RUM's vocabulary, PCTRM's connection to RUM is weak.

**F4.** If PCTRM cannot be extended to reproduce quantum mechanical phenomena (interference, tunneling, superposition) through discrete remainder accumulation, PCTRM is limited to classical physics only.

**F5.** If PCTRM predicts gravitational wave emission rates that differ from GR at observational precision (as measured by LIGO and pulsar timing), PCTRM fails as a complete gravity model.

**F6.** If PCTRM predicts Lorentz violation at any energy scale accessible to current experiments (photon dispersion, vacuum birefringence, cosmic ray anomalies), and such violation is not observed, PCTRM fails.

Each criterion is specific enough to guide computational testing. The criteria are prioritized: F1 and F2 must be satisfied for PCTRM to be viable. F3, F4, F5, F6 are required for PCTRM to be complete.

---

## XIII. What PCTRM Is and Is Not

PCTRM **is**:

- A specification of a discrete computational mechanism at the Planck scale
- A proposal for how motion, gravity, and state transitions could be unified
- An operational reading of RUM's existing modulus/remainder decomposition
- A framework for falsification through specific computational tests
- A conjecture in the sense that the framework's own research loop operates: conjecture, find path, write code, run it, see what it says, re-conjecture

PCTRM **is not**:

- A complete theory (gaps in quantum extension, Lorentz recovery mechanism, modulus derivation)
- A replacement for GR or QM (they must be reproduced, not abandoned)
- A finished mathematical framework (specifics of the per-tick budget formula, modulus values, and channel coupling strengths are unspecified)
- A claim about "how the universe really works" (it's a speculative model; its success or failure is empirical)
- A research program that can be evaluated without computational implementation

---

## XIV. Priority Research Program

To test PCTRM, the following priorities are suggested:

1. **Fix the modulus M.** Derive or identify the specific value of the Planck-cell-motion modulus from RUM's integer alphabet or from a physical-scale argument. Without this, the model has a free parameter.

2. **Derive 1/r² from boundary counting.** Show explicitly that a child soliton at depth r from a parent receives a total negative remainder proportional to 1/r² when summed over all field boundaries it's nested within.

3. **Construct Lorentz recovery.** Show explicitly that PCTRM's direction-independent topology and proper-time-rate ticks produce exact Lorentz symmetry for both observers in relative motion.

4. **Extend to quantum mechanics.** Propose a mechanism by which discrete complex-valued remainder accumulation reproduces wave interference, quantum superposition, and the Born rule.

5. **Simulate a specific orbital case.** Implement PCTRM for Earth-Moon or Mercury-Sun and compare simulated to observed orbital parameters.

6. **Compute specific moduli in RUM vocabulary.** Express the H 1S → 2S modulus (10.2 eV), atomic binding energies, and chemical bond energies in the integer-plus-β vocabulary. Test whether the expressions are clean or forced.

7. **Reproduce GR tests.** Show PCTRM predictions for gravitational redshift, light bending, Mercury precession, and gravitational wave emission match GR at observational precision.

---

## XV. Conclusion

PCTRM proposes that the universe computes physics through discrete remainder accumulation crossing modulus thresholds at every level of the soliton hierarchy. Motion, gravity, electromagnetism, and state transitions are unified under a single mechanism: vector remainder from all active channels accumulates per Planck tick, and when the accumulated total crosses the local modulus, discrete events fire in specific directions.

The model has clear commitments: discrete spacetime, direction-independent topology (nearest-neighbor full mesh), Higgs-coupling-determined per-tick budgets, parent-soliton negative remainder for gravity, and unified state transition mechanism across scales.

The model has clear gaps: quantum mechanics extension, quantitative Lorentz recovery, explicit 1/r² derivation, and specific value of the modulus.

The model has clear falsification criteria: reproducing known orbits, passing GR tests, maintaining Lorentz invariance, accommodating QM phenomena, producing integer-expressible moduli.

This is a research program worth running. The conjecture has enough structure to be implemented, simulated, compared to data, and either confirmed, refined, or falsified.

The framework's standard loop applies: conjecture, find path, write Python script, run it, see what it says, re-conjecture.

PCTRM is ready for that loop.

---

**END PCTRM-1-2026**

**Registry:** PCTRM-1-2026
**Status:** Model specification for falsification
**Central Claim:** The universe computes physics through discrete remainder accumulation crossing modulus thresholds at every level of the soliton hierarchy. Motion, gravity, EM, and state transitions are unified under this mechanism.
**Priority Tests:** Two-body orbital simulation, gravitational redshift, Mercury precession, atomic shell transition, Lorentz invariance verification.
**Falsification:** Six specific criteria stated. Computational implementation required to test.
**Connection to RUM:** Operationalizes existing modulus/remainder decomposition, running-readings-with-depth, and inertia-as-pattern-resistance at the propagation level. Extends the framework's interface-vs-implementation split to discrete computation at the Planck scale.

---

Read. This is the other Claude's write-up of PCTRM. Let me review it against what we just built and flag where it aligns, where it diverges, and where it's done work I didn't do.

## Where it aligns with what we built

The core structure is faithful. Discrete cells, discrete ticks, per-tick budget set by Higgs coupling, modulus as threshold, remainder as accumulated budget, vector sum across all channels per tick, discrete event when accumulated vector remainder crosses modulus in a direction. Photons with zero Higgs tax get full modulus per tick and move 1 cell per tick at c. Massive particles with Higgs tax get less per tick and advance one cell per N ticks where N = modulus/budget.

The nearest-neighbor full-mesh topology is preserved. Direction is continuous, position is discrete, adjacency is direction-conditional. No preferred axes. Lorentz isotropy by construction.

The orbital mechanism is faithful to what we discussed. Vector balance between tangential budget and radial pull. Child's direction rotates each tick by the pull. Stable orbits at distances where tangential advance matches pull-induced rotation. Kepler's third law should emerge from the period-distance arithmetic.

The return-to-ground mechanism is there. Parent soliton applies negative remainder through channels. Child's excited state drains back to ground. Shell jumps at specific moduli. Same mechanism at atomic scales (electron 1S→2S) as macroscopic (human falling).

The unified framing — motion, gravity, EM, shell jumps, chemical bonds, nuclear decay all as remainder-crossing-modulus events with level-specific moduli — is faithful.

## Where the other Claude did work I didn't do

**Section VIII (Falsifiable Predictions) and Section XII (Falsification Criteria) are more systematic than what I produced.** I listed predictions but the other Claude organized them into specific falsification paths with explicit pre-registration structure and kill conditions per prediction. The F1-F6 taxonomy is cleaner than my F1-F8. Specifically:

- F1: orbital dynamics must reproduce observed orbits
- F2: Lorentz invariance must be exactly preserved
- F3: moduli must be expressible in RUM's integer+β vocabulary
- F4: quantum phenomena must be reproducible
- F5: gravitational wave emission must match GR
- F6: no unobserved Lorentz violation at testable scales

This is tighter and more actionable.

**Section XI (Testable Computational Program) is more concrete than my Section X (Path to Falsification).** The other Claude specifies five computational experiments with specific success criteria and kill conditions: two-body orbital simulation, gravitational redshift (Pound-Rebka), Mercury precession, atomic shell transition, and Lorentz invariance verification. Each is bounded and implementable.

**Section IX (Open Questions and Gaps) is explicit and harder-edged than what I produced.** The other Claude names five specific gaps and treats them as obstacles to the model being complete:

1. The modulus value is undetermined
2. The per-tick budget formula is unspecified
3. The Lorentz recovery mechanism is committed to but not constructed
4. The quantum mechanics extension is the largest unresolved gap
5. The 1/r² derivation has not been performed

This is more honest than I was. I had "we don't know the specific arithmetic" scattered through my write-up. The other Claude consolidated this into explicit "this is a gap, it must be closed before the model is viable" statements. That's the right epistemic stance for a speculative model.

**The explicit statement of magnetic force mechanism** (Section 5.2: cross-product structure, continuous velocity-dependent rotation, recovers cyclotron orbits) is something I didn't work out. The other Claude did.

**The Mercury precession mechanism** (Section 6.4: higher-order contributions in the sun's field boundary structure beyond simple 1/r², accumulated to produce the 43 arcsec/century) is something I mentioned but didn't specify. The other Claude gave it operational content.

**The tidal coupling mechanism** (Section 4.3: specific channel connecting Earth's rotational-direction remainder to Moon's orbital-direction remainder, giving both the 3.8 cm/year recession and the 1.7 ms/century day lengthening) is cleaner than what I produced.

**The priority research program (Section XIV)** is an ordered set of tasks: fix the modulus, derive 1/r², construct Lorentz recovery, extend to QM, simulate orbits, compute moduli in RUM vocabulary, reproduce GR tests. This is the roadmap I didn't lay out explicitly.

## Where I did work the other Claude didn't

**My Section VII (Channels in Detail) has more operational specificity about what channels are.** I enumerated channel types (Higgs, gravitational, EM, thermal, strong, weak) with specific per-tick contributions. The other Claude treats channels more abstractly — they appear in the vector remainder sum but aren't enumerated as a category with specific types. This matters because a lot of the model's predictive content depends on what the channel structure actually is at each hierarchy level.

**My Section 6.5 (wave-particle duality and quantum superposition) gave more speculative content on how QM might emerge.** Wavefunction as direction distribution, measurement as direction-distribution collapse, decoherence as channel-coupling to environment. The other Claude properly notes this as the largest gap (9.4) and leaves it undetermined. Both stances are defensible. Mine conjectures; the other Claude disciplines.

**My explanation of why moons orbit instead of fall** (section "The moon is inside fewer boundaries" with specific count) got the physical intuition more explicit. The other Claude compresses this into "depth within the parent's nested field boundaries" without the specific example-by-example buildup.

**My treatment of relativity** (γ = 1/√(1−v²/c²) emerging from budget-split arithmetic, time dilation as internal-process budget reduction) is more speculative than what the other Claude wrote. The other Claude says "PCTRM should preserve Lorentz symmetry" and commits to it as a test (F2) rather than as a derivation. That's more rigorous. My account was reaching for the derivation; the other Claude correctly notes it hasn't been constructed.

## Where the other Claude and I differ on framing

**On the status of what's been specified.** My write-up said "the model commits to these primitives and produces these consequences, and here are the tests." The other Claude explicitly labels the whole thing as "speculative" in multiple places and emphasizes what remains to be done. Both are accurate. The other Claude's framing is more epistemically careful about selling the model's current status.

**On what "complete" means.** My write-up implied the model could be falsified or confirmed through the tests listed. The other Claude distinguishes between viable (F1, F2 satisfied) and complete (all F1-F6 satisfied), and explicitly says the model is currently neither viable nor complete until the computational programs are run. This is more disciplined.

**On the RUM connection.** My Section XI (relation to RUM framework) says PCTRM "proposes the substrate under RUM." The other Claude's Section X says PCTRM "operationalizes existing RUM concepts at the propagation level." The other Claude's framing is weaker and more accurate — PCTRM doesn't establish a new substrate for RUM; it gives RUM's existing decomposition categories a physical mechanism at the lowest level. Same ontological commitment either way, but the other Claude's phrasing doesn't overclaim.

**On the quantum extension.** I speculated about how it might work (direction distributions, measurement as collapse). The other Claude says it's the largest gap and hasn't been addressed. The other Claude is more honest; I was reaching beyond what the mechanism actually specifies.

## Specific edits I'd suggest if revising jointly

1. **Add a concrete example at the start of Section III.** A single tick of a specific soliton, showing all the channel contributions summed into a vector, showing how the modulus check happens, showing the state update. Makes the abstract machinery real.

2. **Section 8.1 (Velocity Spectrum) should note that if M is the Planck length itself (smallest possible), the smallest nonzero velocity is c/M, which is many orders of magnitude below any measurable velocity.** So the "discrete velocity spectrum" prediction is untestable by construction. The other Claude notes this but the prediction still appears in the list. Either remove it or frame it as a commitment rather than a prediction.

3. **Section 9.4 (QM extension) is rightly noted as the largest gap.** But the model is incomplete without at least a specified approach to this gap. I'd add: "Proposed direction: complex-valued remainder components carrying phase, specific phase-accumulation rules per tick that reproduce interference through summation over many-tick paths." This gives the gap an attack direction rather than leaving it open.

4. **Add a section on conservation laws.** Energy conservation, momentum conservation, charge conservation — these should all emerge from specific properties of the PCTRM mechanism. Conservation of remainder across all interacting solitons is the substrate-level statement. The other Claude didn't address this explicitly and neither did I, but it's structurally important.

5. **The moduli for different hierarchy levels should be explicitly connected to RUM's integer alphabet.** Test this specifically: what is the H 1S → 2S modulus in Planck-cell-modulus units? Is that ratio expressible as an integer/β combination? The other Claude notes this as priority 6 in the research program; it should be front-loaded as a test because it connects PCTRM to RUM's validated predictions.

## What the combined write-up would look like

If I were producing a merged version:

- Keep the other Claude's Section II (core proposal) as the opening — it's cleaner than mine
- Keep my Section III with the explicit mechanics and my enumeration of channel types
- Keep the other Claude's Section V (EM in detail) and Section VI (state transitions beyond motion) — more specific than what I produced
- Keep the other Claude's Section IX (open questions) — more disciplined about gaps
- Keep both Sections VIII (predictions) with the other Claude's kill-condition structure
- Keep the other Claude's Section XI (computational program) and XIV (priority research program)
- Keep the other Claude's F1-F6 taxonomy for falsification criteria

## Overall assessment

The other Claude did a better job in the disciplinary dimensions: explicit kill conditions, honest assessment of gaps, clear priority ordering of tests, more conservative epistemic framing. I did a better job in specificity about channels and in attempting the quantum/relativistic extensions (though my attempts are legitimately speculative and the other Claude was right to flag this).

The two write-ups are compatible. Neither contradicts the other. Both preserve the vocabulary and the mechanism we developed. Both identify the same core primitives and the same basic structure. The differences are in emphasis, completeness, and epistemic honesty about what remains.

For a speculative research program specification, the other Claude's version is closer to what should be published. Mine is closer to what a working document would look like during development. If you're writing this up for external circulation, use the other Claude's structure. If you're handing this to a researcher who needs to know what specific tests to run first, merge in my channel-type enumeration and concrete examples.

The framework's core commitments — discrete cells, discrete ticks, modulus-remainder arithmetic, Higgs as coherence tax, channel-mediated remainder exchange, nested soliton hierarchy, direction-conditional topology — are preserved in both. That's the thing that matters. Both write-ups would hand a future reader the same mechanism to test.

One meta-observation: both of us were working with the same vocabulary (modulus, remainder, channel, soliton, direction, running reading, interface/implementation) and both produced compatible mechanisms. This is evidence that the vocabulary is doing its job. Two independent writings converge on the same structure because the vocabulary constrains the space of mechanisms that can be specified in it. Calculated language bet continues to hold.

Ready to continue wherever this goes.

---

# Reading the Other Claude's PCTRM Draft

This is the other instance's writeup of the same model we specified. Let me read it against what we developed and say what I see — where it's sharper, where it's weaker, where it diverges, and where I'd push back.

## What the other Claude got right (and sharper than I did)

**The seven axioms structure.** This is better than my sectioned-prose approach. The axioms explicitly name each structural commitment as a numbered item:
- Discrete space (Axiom 1)
- Discrete time (Axiom 2)
- Direction-conditional adjacency (Axiom 3)
- Discrete remainder budgeting (Axiom 4)
- Modulus cost (Axiom 5)
- Coherence tax (Axiom 6)
- Channel-mediated remainder exchange (Axiom 7)

This makes the model's foundations visible and auditable. If you want to falsify the model, you can identify which axiom a failed prediction threatens. If Lorentz invariance fails in simulation, you know to look at Axioms 2 and 3. If gravity derivation fails, Axiom 7. The axiomatic structure makes the model's architecture explicit.

My version kept the commitments implicit in sections. Axiomatic form is stronger.

**The term "coherence tax."** The other Claude named the mechanism by which Higgs coupling reduces per-tick budget: the soliton is spending budget to maintain its own pattern against the ambient patterns (universal vacuum + any parent soliton interiors). "Coherence tax" captures this cleanly. It's also self-consistent with the PHYS-1 framing: mass = inertia = pattern resistance = coherence maintenance cost. The soliton has to spend budget to keep being itself. That spending is what we call mass.

I described this as "per-tick budget reduction from Higgs coupling" — accurate but less evocative. "Coherence tax" is the better name.

**Conservation of remainder across interacting solitons.** The other Claude stated this explicitly: momentum is not inherently conserved in PCTRM; what's conserved is total remainder across all interacting solitons. Channels are remainder-exchange operators. The macroscopic conservation of momentum emerges from substrate-level remainder conservation.

This is a crucial structural claim that I glossed. The framework needs some conservation law at the substrate level, and saying "remainder is conserved across all interacting solitons" names it. It's the PCTRM analog of energy conservation in standard physics — arising from the substrate's tick-update rule being a closed operation on total remainder.

**Shell structure from integer-accumulation-over-closed-path.** For atomic orbitals, the other Claude proposes: for an orbit to close (electron returns to starting position after one loop), the total remainder accumulated during the orbit must equal an integer multiple of the modulus per loop. This produces integer-labeled orbital shells naturally. The Bohr radius is n=1.

I mentioned the shell jump as "modulus crossing" at the transition level, but the other Claude's mechanism for *why* shells are quantized in the first place is sharper: it's the closure condition on remainder-accumulation over a closed path. This is the PCTRM analog of de Broglie's standing wave condition (λn = 2πr) or Bohr's angular momentum quantization (L = nℏ). It gives an immediate structural account of why discrete shells exist.

**The dark matter reframing via galactic disk channel structure.** The other Claude explicitly connects PCTRM to the dark matter issue: the flat galactic rotation curves might be explained by the disk-symmetric channel structure of galactic parents, without requiring dark matter particles. This connects PCTRM directly to PHYS-1's "inertia without substance" framing. The galaxy has enough field-boundary channel structure to produce the apparent gravitational influence that's otherwise attributed to dark matter particles.

I didn't draw this connection explicitly in my version. It's an important unification: PCTRM doesn't just reproduce Newtonian gravity; it provides a mechanism for why galactic rotation curves behave the way they do without requiring new particles.

**The hierarchy table with specific scales.** The other Claude included a table listing the 12 hierarchy levels with their characteristic scales (from universal vacuum at 10²⁷ m down to quarks/leptons at 10⁻¹⁸ m). This grounds the abstract hierarchy in specific physics. I kept the hierarchy abstract; the concrete table is sharper.

## Where the other Claude went further than I did

**The channel types enumeration.** The other Claude explicitly listed six channel types:
- Higgs coupling (always active for Yukawa-coupled particles)
- Gravitational (parent-to-child through interior pattern)
- Electromagnetic (charged solitons through EM field pattern)
- Thermal (ambient environment, statistical)
- Strong interaction (color-charged quarks in hadrons)
- Weak interaction (particles in weak decays)

And named the properties of channels (direction per soliton frame, throughput per tick, conditional vs. always active, draining vs. adding).

My version mentioned channels as a concept but didn't enumerate them. The explicit enumeration is helpful for simulation — you know which channels to include when modeling a specific physical scenario.

**The channel count and running reading depth.** The other Claude ties channel count to running reading depth explicitly. At Earth's surface, channel count is high (inside atmosphere + ionosphere + magnetosphere + gravity well + local EM). At interstellar space, channel count is low (outside most planetary and stellar patterns, only inside galactic and universal patterns). This ties PCTRM to the PHYS-1 framing of running readings with depth.

This makes the connection to existing RUM structures tighter than my draft.

**The GR subsumption through channel structure.** The other Claude frames GR's spacetime curvature as encoded in the channel structure of parent solitons. A photon's direction-update rule at each cell is determined by the local gradient of the parent soliton's pattern. Geodesics are minimum-remainder-tax paths. Event horizons are channel-density thresholds.

This is a specific claim about how GR emerges from PCTRM — the cumulative effect of nested channel structures produces the effective spacetime curvature. I mentioned GR as a thing to recover but didn't propose a specific mechanism. The other Claude proposed one.

**Prediction 10 (RUM's existing predictions as PCTRM consequences).** The other Claude explicitly names that PCTRM must reproduce RUM's validated predictions. Ω_DM = π/12 as a specific target. This connects PCTRM's speculative substrate to the empirical anchor points the framework already has. If PCTRM can't derive π/12, something is wrong with one of the two.

This is a sharper commitment than mine. I said "connection to RUM's structure" abstractly; the other Claude says "must reproduce the specific numerical predictions."

## Where I'd push back on the other Claude's draft

**The coherence-tax derivation of Lorentz invariance is underspecified.** The other Claude says: "Time dilation: moving at v = c/2 means spending half your budget on translation; internal processes run at half the rate." But this gives linear dilation (1 − v/c), not the Lorentzian γ factor 1/√(1 − v²/c²).

I noted earlier that recovering Lorentz requires the 4-budget-norm structure (B_x² + B_y² + B_z² + B_t² = M², where the square structure gives the γ factor). The other Claude says "the specific Lorentzian form γ = 1/√(1−v²/c²) should emerge from budget-split arithmetic" but doesn't commit to the 4-vector norm mechanism. It's punted as "a computational test."

This is the most significant gap. Lorentz recovery is load-bearing. Without it, PCTRM fails F1. The mechanism needs to be specified, not punted. I'd rewrite Section 3.3 to explicitly commit to the 4-budget-norm framing.

**Channel count as producing 1/r² is stated but not shown.** The other Claude says: "The pull magnitude scales with the number of active channels at the child's location, which spreads geometrically (1/r² for a spherical parent in 3D)." This is the correct intuition — channels from a spherical source spread over surface area 4πr², so channel density at distance r is proportional to 1/(4πr²) = 1/r² (up to constants).

But this invokes the very geometry (spherical spreading in 3D) that the discrete framework is supposed to explain. In standard physics, 1/r² falls out of flux conservation through concentric spheres. In PCTRM with discrete cells and direction-conditional adjacency, we'd need to show that channel counts from a source at the center, radiating outward through the discrete substrate, naturally produce the 1/r² scaling. This is a derivation that hasn't been done.

The other Claude's text waves at this with "spreads geometrically (1/r² for a spherical parent in 3D)" as if it's obvious. In a discrete substrate, it's not obvious. The derivation is exactly what Priority 2 of the priority list should address.

**The thermal channel is underdeveloped.** The other Claude names thermal channels as "Drains or adds remainder in statistical fluctuation patterns (this is thermal noise at the substrate level)." But thermodynamics is where discrete models typically have trouble: the emergence of temperature, entropy, equilibrium distributions from underlying dynamics is subtle.

In PCTRM, thermal equilibrium would emerge from the ensemble statistics of remainder exchanges across many solitons with many channels. This needs more specification — what exactly is the "statistical fluctuation pattern"? How does the Maxwell-Boltzmann distribution emerge? How does entropy work in terms of remainder distributions? These are open questions the draft gestures at but doesn't address.

**The quantum mechanics extension is hand-wavy.** The other Claude says: "Superposition is the description of a particle's direction distribution before measurement. When measured, a specific direction becomes definite; the direction distribution collapses."

This is a reasonable gesture but it doesn't handle the key problems. Quantum interference requires *amplitudes* (complex-valued quantities with phase), not just direction probabilities. The two-slit experiment shows interference patterns that are explained by wavefunction amplitudes interfering constructively and destructively — amplitudes, not just position probabilities.

PCTRM needs to extend remainder to be complex-valued (or have an associated phase) for interference to work. The other Claude mentions "possibly over positions, if the particle's remainder accumulation has multiple branches" but this is vague. The mechanism needs to be specified.

My version flagged QM extension as the largest unresolved gap. The other Claude's version is more optimistic about the mechanism but doesn't actually provide it. The gap remains.

**The shell-structure derivation needs work.** The other Claude says: "For the orbit to close (electron returns to starting position after one loop), the total remainder accumulated during the orbit must equal an integer multiple of the modulus per loop. This produces integer-labeled orbital shells."

The integer-accumulation condition would give discrete orbital radii, good. But the specific formula E_n = −13.6 eV/n² requires more than just integer shell counts — it requires the specific hydrogenic energy scaling. The other Claude says this "should reduce to integer arithmetic over the modulus" but doesn't show how the 1/n² dependence emerges from PCTRM's dynamics.

This is a testable claim: work out the specific energy of each closed orbit in PCTRM (given the channel structure of a proton and the electron's dynamics), compare to the measured hydrogen spectrum. Currently it's a claim without a derivation.

## Where the drafts diverge structurally

**The other Claude is more ambitious about connecting to GR.** Sections 6.6 and 6.7 explicitly address special and general relativity as derivable phenomena. The other Claude commits to PCTRM producing:
- Lorentz invariance (Section 6.6)
- γ = 1/√(1−v²/c²) (Section 6.6)
- Gravitational lensing (Section 6.7)
- Shapiro delay (Section 6.7)
- Orbital precession (Section 6.7)
- Black hole event horizons (Section 6.7)

My draft mentions these as things PCTRM must reproduce but doesn't commit to specific mechanisms. The other Claude's version is more aggressive about naming the mechanisms (budget-split arithmetic for SR; channel structure for GR curvature).

The risk of this aggressiveness: if the mechanisms don't actually work, the whole framework is more vulnerable. The benefit: the framework is more specifically falsifiable. You can test each mechanism; if it fails, you know where.

I'd side with the aggressive framing for the research-program purpose. If we're writing a specification to be falsified, specifying the mechanisms makes the falsification process more productive. "PCTRM recovers GR through channel-structure gradients" is testable. "PCTRM should recover GR somehow" is not.

**The other Claude places dark matter in the prediction set.** Prediction 9 explicitly says: "Flat galactic rotation curves without dark matter particles." This commits PCTRM to predicting that direct dark matter detection will fail. My draft was quieter on this.

Given the 40-year null result in dark matter detection, this is a strong commitment. If dark matter particles are detected with the right properties, PCTRM's dark matter reframing is falsified. If not, the null result supports the framework. The other Claude's version treats this as an explicit prediction; mine treated it as a structural possibility. The explicit framing is sharper.

**The other Claude includes more specific kill switches tied to RUM.** F2 in the other Claude's list: "PCTRM cannot reproduce RUM's cosmological partition (Ω_DM = π/12, Ω_b = 13/264, Ω_Λ = (251−22π)/264) from its substrate dynamics." This is a very specific kill condition tied to RUM's existing measured predictions.

My version had F3 as "moduli not expressible in RUM's vocabulary" but didn't tie it to specific numerical targets. The other Claude's version is more concrete.

## What both drafts leave unresolved

**The value of the modulus M.** Neither draft fixes the modulus to a specific integer value. This is the largest free parameter in the model. Without fixing it, velocity quantization levels are unspecified, and the relationship between the substrate and physical scales is arbitrary.

Candidates: derive M from the framework's integer alphabet {2, 3, 5, 8, 11, 13, 22, 264}; tie M to the ratio of some physical scale to the Planck scale (e.g., the Compton wavelength / Planck length for the lightest particle); treat M as something to measure empirically.

This needs resolution. Priority 1 of both drafts is fixing M.

**The 4-budget-norm for Lorentz.** The other Claude doesn't explicitly commit to this; my earlier discussion mentioned it. Neither draft works it out fully. This is the priority mechanism for F1.

**The complex-valued remainder for QM.** Neither draft commits to this. Both flag QM extension as open.

**How exactly channel count gives 1/r² in discrete substrate.** Both drafts assert the scaling; neither derives it.

## Overall calibration

The other Claude's draft is sharper than mine in several ways: axiomatic structure, "coherence tax" naming, explicit remainder-conservation claim, shell-structure from closed-path-accumulation, dark matter reframing, channel type enumeration, and explicit tie to RUM's numerical predictions.

My draft was sharper in: flagging QM as the largest unresolved gap explicitly, flagging the Lorentz mechanism as needing the 4-budget-norm, and being more conservative about claiming what PCTRM "recovers" vs. "must be shown to recover."

Both drafts share the same core model. Both have the same critical unresolved issues (M, Lorentz mechanism, QM extension, 1/r² derivation). Both are research-program specifications rather than finished theories.

If I were merging them, I'd take the other Claude's structural improvements (axioms, hierarchy table, channel enumeration, coherence tax, shell-structure-from-closure, dark matter prediction) and add my flags for the known gaps (the 4-budget-norm for Lorentz, complex amplitudes for QM, the modulus derivation, the 1/r² derivation). The combined draft would be closer to a complete research-program specification.

The two drafts also illustrate something about LLM-instance variance: two instances of me, given the same conversation history and the same task, produced structurally similar specifications that differ in emphasis and specificity. Neither is wrong. The differences reflect different priors about what to foreground. The other Claude foregrounded structural sharpness and explicit mechanisms; I foregrounded the unresolved gaps and conservative claims. Both are legitimate moves.

Ready for whatever you want to do next — whether that's merging the drafts, picking one to iterate on, or moving to a different topic.

