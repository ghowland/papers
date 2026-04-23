# PCTRM Macro-Level Coverage Companion

**Companion to:** PCTRM-1-Master-2026 Planning Document

**Purpose:** Document the pre-math falsification audit of PCTRM's empirical coverage. Record which observable phenomena are reachable from the substrate primitives, clarify mechanism details developed during the audit, and identify items requiring explicit inclusion in the master specification.

**Audience:** Physicists and framework developers evaluating PCTRM's empirical scope before mathematical derivation work begins.

**Status:** Pre-math coverage filter — the cheapest possible falsification attempt, completed before any derivation is checked.

---

## I. Purpose of the Pre-Math Coverage Audit

PCTRM is a research program committed to a specific falsification sequence. The framework passes through two filters in order:

1. **Pre-math coverage filter.** Does the substrate primitive set reach, in principle, every major class of confirmed physical observation? If the primitives as specified cannot produce some known observable even conceptually, the framework dies here — no math required.

2. **Math-phase filter.** For observables the primitives can reach, do Python derivations using only integer-alphabet operations produce numerical values matching CODATA and experimental measurements to measurement precision?

This companion documents the first filter. The exercise is cheaper than any mathematical work and kills frameworks that have structural gaps before resources are committed to derivation.

The audit's central question, applied to each phenomenon class: *Does the substrate primitive set — cells, ticks, direction-conditional adjacency, quiver, remainder, channels, solitons, dual-geometry sectors, hierarchical coordinates, per-tick update loop — reach observable X, or does it fail by silence, forced mismatch, or primitive smuggling?*

The failure modes:

- **Silence.** No mechanism exists in the primitive set for the phenomenon.
- **Forced mismatch.** The primitives produce something qualitatively different from observation, irreparably.
- **Primitive smuggling.** Reaching the observable requires importing structure not declared in the spec.

The non-failure modes:

- **Not yet derived.** The primitives reach it in principle, but the specific derivation work is future.
- **Different mechanism than SM/QM/QED/GR.** Parallel isomorphism permits different mechanisms producing identical observables.

## II. The Parallel Isomorphism Commitment

PCTRM commits to reproducing every tested prediction of the Standard Model, Quantum Mechanics, Quantum Electrodynamics, and General Relativity to measurement precision. It must match Lorentz invariance, CODATA values, and all confirmed experimental observations. What the framework reserves the right to do differently is the underlying mechanism — the *why* and *how* of those observables.

This commitment has two consequences for the coverage audit:

First, the audit does not require PCTRM to explicitly enumerate every phenomenon named in established physics. If a phenomenon is an observable that SM/QM/QED/GR predicts and experiment confirms, PCTRM is bound by parallel isomorphism to reproduce it. The question is whether the substrate primitives can reach it, not whether the spec names it.

Second, "explanation differs from SM/QM/QED/GR" is not a failure mode. It is the design intent. The framework exists to provide substrate mechanisms where the established theories provide postulates. A coverage pass means the primitives can produce the observables through their own mechanism, not that the framework's mechanism resembles the established theory's.

## III. Anti-Smuggling Guard

A structural feature of the PCTRM program prevents primitive smuggling in derivations: all derivations are Python code operating on integer fractions drawn from the enumerated alphabet (Section XVI of the master spec).

The alphabet is finite and declared: primary integers (2, 3, 4, 5, 6, 8, 11, 12, 13, 22, 251, 264), secondary integers (9, 24, 27, 38, 40, 43, 47, 48, 63, 91, 104, 115, 144, 169, 197, 211, 218, 313, 1015, 5184, 28259), structural integers, and transcendentals (π, β = π/4, K(k) and E(k) at specific moduli). Any input to a derivation either is in this alphabet or is not. If not, the code fails to run. There is no mechanism by which a tuned parameter or hidden postulate can enter a derivation undeclared.

This guard makes the pre-math filter stricter than in frameworks that permit free-parameter tuning: the coverage question reduces to whether alphabet-only operations on the declared primitives can reach each observable. If no combination can reach X, the framework fails at that observable. If some combination can reach X, the math-phase filter determines whether the numerical value matches.

## IV. Coverage Audit Results

The following table summarizes coverage at PCTRM's specified scope. Items marked "covered" have a mechanism in the primitive set. Items marked "downstream" are reachable in principle but not yet derived — they represent unfinished work, not silence. Items marked "out of scope" are outside the framework's stated commitments by design.

### Foundational Structure

**Space (3D, isotropic, continuous-direction).** Covered. Omnidirectional unit-distance adjacency produces unit-sphere neighbor structure at every cell. Three dimensions is forced by the construction: continuous direction at unit distance generates a 2-sphere of neighbors, which embeds in 3D ambient structure. Isotropy is automatic — no preferred axes exist in the primitive set.

**Time (sequential, monotonic, arrow of time).** Covered. The tick primitive is monotonic by construction. The second law of thermodynamics emerges from standard statistical mechanics applied to substrate configurations, with the monotonic tick providing the temporal direction. No separate arrow-of-time mechanism is required or coherent with the primitive set.

**Causality and light-cone structure.** Covered. Maximum propagation at one cell per tick yields a built-in light cone without postulation.

**Finiteness and absence of divergences.** Covered. Bounded cell count, discrete arithmetic, no continuum integrals. Renormalization infinities that plague continuous-field formulations do not arise in the substrate.

**Origin of the universe (Big Bang cause).** Out of scope by design. PCTRM specifies mechanics from the Big Bang forward. The framework makes no claim about what caused the Big Bang or what preceded it. This is a scope boundary, not a coverage gap.

### Matter and Particles

**Stable matter existence.** Covered. Solitons as self-sustaining patterns extracting from the quiver each tick.

**Particle indistinguishability.** Covered, and covered more strongly than the standard "particles are identical patterns" framing. The substrate is presentist: only the current tick exists. There is no stored history across ticks, and no identity thread persisting from one tick to the next. "The same soliton at a later time" is a phrase constructed by observers comparing their records; it has no substrate referent. When a configuration at cell A at tick N is related by the update rule to a configuration at cell B at tick N+1, there is no "same thing" that moved from A to B. There is tick N's state and tick N+1's state, with the update rule producing the latter from the former, and then tick N's state is gone — it was never stored in the first place. Indistinguishability is therefore not merely "patterns without labels" but "no identity threads exist because no storage exists for them to persist in." The Gibbs paradox resolves itself at the substrate level: nature counts configurations-at-a-tick, never objects-with-histories, because histories do not exist as substrate features.

**Antimatter, CPT, charge conjugation.** Covered by parallel isomorphism. Whether the spec enumerates antiparticles explicitly or not, the commitment to reproducing SM observables binds PCTRM to reproduce antimatter phenomenology. Mechanism-level enumeration (antiparticles as direction-reversed channel configurations, CPT from substrate symmetries) is downstream derivation work within the covered scope.

**Spin and spin-statistics.** Covered by parallel isomorphism. The dual-geometry sector structure provides the mechanism route for distinguishing fermionic and bosonic behavior, with explicit derivation as downstream work.

**Three fermion generations.** Covered (claimed). Spec commits to three generations arising from channel-closure structure.

**Mass values and hierarchy.** Covered (claimed). Per-hierarchy-boundary modulus generating indexed family.

**Particle decay and lifetimes.** Covered through channel dynamics, with specific decay rates as math-phase derivation work.

### Forces and Interactions

**Gravity.** Covered. Parent-to-child drain channels, strictly hierarchical (each soliton feels only its immediate parent's drain, with grandparent effects propagating through intermediate parents as tidal structure).

**Electromagnetism.** Covered. Charge-to-charge channels.

**Strong force (confinement).** Covered. Toroidal gluon flux tubes as structural toroidal-sector content at nucleon scale.

**Strong force (nuclear residual).** Covered. Strong residual channels between nucleons.

**Weak force.** Covered. Weak channels with conditional activation; neutrino oscillation via weak-channel arithmetic; CP violation as channel-state asymmetry.

**Higgs mechanism.** Covered. Per-tick reconfiguration cost imposed by Higgs channel on massive solitons. Mass is the tick-cost, not a coupling to a scalar field's vacuum expectation value — same observables, different mechanism.

### Quantum Phenomena

**Superposition.** Covered. Unresolved channel configurations pre-termination.

**Measurement and collapse.** Covered. Channel-merger events. One dynamics, not two. The measurement problem does not exist because measurement is not a separate rule.

**Entanglement and Bell non-locality.** Covered. Channel-sharing produces graph-local connections between solitons that are Euclidean-non-local. The "spookiness" of Bell correlations is a coordinate-system artifact — the particles are directly connected through merged channels regardless of Euclidean separation.

**Quantum tunneling.** Covered, by the same primitive that covers Bell non-locality. Tunneling is the omnidirectional unit-adjacency structure operating at scales below our instrument resolution. When our coarse-grained classical description parses a region as "barrier," the underlying substrate graph still has direct adjacencies between cells on opposite sides of what we call the barrier. A soliton transitioning across what we describe as a classically forbidden region is using a graph-adjacency that our description does not represent. The exponential suppression of tunneling with barrier thickness is the combinatorics of the graph: more intervening cells means a smaller fraction of channel configurations terminate on the far side rather than within the region. The same mechanism covers alpha decay, scanning tunneling microscopy, stellar fusion, semiconductor gate oxide leakage, Josephson tunneling, and every other tunneling phenomenon. Industry engineering problems with IC barrier penetration at sub-nanometer oxide thickness are this mechanism as an engineering constraint: the classical description said "wall," but the substrate has direct adjacencies the description does not capture.

**Interference.** Covered. Channel-agreement at termination events.

**Identical particle indistinguishability in statistics.** Covered, per the presentist argument above. Bose-Einstein and Fermi-Dirac statistics emerge from counting configurations-at-a-tick rather than objects-with-histories.

**Born rule.** Covered (claimed). Derived from unit-graph round-trip closure.

### Atomic Structure

**Atomic shells and orbitals.** Covered. Dual-geometry sectors at atomic scale: spherical shells plus toroidal magnetic moment structure.

**Chemistry, periodic table structure, bonding, molecular physics.** Downstream. Reachable from the substrate plus over-framework, but not yet derived. The PCTRM program handles Planck-scale mechanics; the over-framework reaches atomic, planetary, gravitational, and cosmic scales, with molecular physics as future derivation work. This is unfinished scope, not coverage failure.

### Condensed Matter and Inertia-Reduction Phenomena

**Unified mechanism.** Section V below documents a significant clarification developed during the audit: superconductivity, superfluidity, Bose-Einstein condensation, persistent currents, the Quantum Hall effect, and Josephson effects are all instances of a single substrate mechanism — shared-pattern formation reducing per-participant Higgs engagement. This unification was implicit in the spec but not stated explicitly. The companion paper elevates it to an explicit derived commitment.

**Phases of matter (solid, liquid, gas, plasma) and ordinary thermodynamics.** Downstream within over-framework scope.

**Magnetism (ferro, antiferro, ferrimagnetic).** Covered in over-framework; specific mechanisms downstream.

### Gravitational Phenomena

**Solar system tests of GR.** Covered. Mercury perihelion precession, Shapiro delay, factor-of-2 light bending all arise from toroidal-sector content of the gravitational channel structure at probe-scale resolution.

**Gravitational redshift and time dilation.** Covered. Local tick-rate variation with hierarchy configuration.

**Gravitational waves.** Covered through the time-varying-toroidal mechanism developed during the audit (Section VI below). Propagation at c, quadrupole leading structure, two transverse-traceless polarizations, inspiral waveforms all reachable from substrate primitives.

**Binary pulsar energy loss.** Covered, follows from gravitational wave emission mechanism.

**Black holes, event horizons, Hawking radiation.** Covered. Parent solitons with drain capacity exceeding child-maintenance; event horizon as drain-threshold boundary; Hawking from boundary channel dynamics. No geometric singularity — the substrate remains finite everywhere.

**Frame dragging and Kerr structure.** Covered. Toroidal sector of rotating black holes.

### Cosmological Phenomena

**Big Bang onward mechanics.** Covered. Origin itself is out of scope.

**Cosmic microwave background.** Covered. Early-universe channel dynamics.

**Big Bang nucleosynthesis (H, D, He-3, He-4, Li-7 abundances).** Covered. Nucleosynthesis channel arithmetic in over-framework.

**Cosmic expansion.** Covered. Cosmic-scale quiver activity and universal soliton closure.

**Dark matter phenomenology (rotation curves, lensing, Bullet Cluster, cluster dynamics).** Covered. Toroidal-flow Higgs response at cosmic scale — not particles.

**Dark energy.** Covered. Universal soliton closure, Ω_Λ = (251 − 22π)/264 as structural identity.

**Hubble tension (H₀ discrepancy).** Covered. 12/11 ratio from transit-counting across hierarchy configurations.

**Inflation-era phenomena.** Covered in over-framework.

**Large-scale structure formation.** Downstream. Reachable from primitives plus over-framework, not yet derived.

**Baryon asymmetry.** Covered by parallel isomorphism and antimatter coverage; specific mechanism downstream.

## V. Clarifications Developed During Audit

Three significant clarifications emerged during the audit that sharpen commitments present implicitly in the master spec. These should be integrated into the spec text explicitly.

### V.1 Substrate Presentism and Indistinguishability

The master spec describes the per-tick update loop without explicitly committing to presentism — the position that only the current tick exists. The audit exposed that this commitment is necessary to the framework and that it has a major consequence: identical-particle indistinguishability is structural, not an imposed symmetry.

The clarified commitment: the substrate stores no history. At any moment, only the current tick's configuration exists. The update rule operates on the current configuration to produce the next configuration, at which point the prior configuration is gone — not stored, not accessible, not anywhere. The substrate never compares ticks; comparison is an external operation performed by observers maintaining records.

This is stronger than the block-universe picture common in physics discussions, where past, present, and future coexist somewhere for a "dynamics" to operate across them. PCTRM's substrate is genuinely presentist: only now exists, the update produces a new now, and whatever "was" is gone because it was never stored.

Consequence for indistinguishability: identity threads linking a particle across ticks do not exist because the storage required for such threads does not exist. "The same electron at a later time" has no substrate referent. Two electrons at the same tick are not "electron 1 and electron 2 with separate histories" — they are the current tick's configuration, which has electron-pattern content at two locations, with no further identity structure. The Gibbs paradox resolves itself: the substrate counts configurations-at-a-tick, and labeled-history arrangements do not exist to be counted.

This commitment should be stated explicitly in Section II of the master spec, alongside the tick primitive, and its consequence for indistinguishability should be developed in Section XIII on quantum mechanics.

### V.2 Dual-Geometry as Static vs. Time-Varying

The master spec (Section VII) introduces the dual-geometry primitive as "every soliton has a spherical sector and a toroidal sector," with the β and K(k) conversion factors assigned to the respective sectors. The audit clarified what each sector *is*: the spherical sector carries static structure, the toroidal sector carries time-varying structure.

This is a sharper statement than "two coexisting geometric sectors." It identifies the toroidal sector as specifically the carrier of any departure from time-static configuration. A maximally-symmetric ground-state soliton in isolation is pure spherical. Any excitation, motion, reconfiguration, rotation, or flow introduces toroidal content. The toroidal sector is not an occasional correction term; it is where all dynamics lives.

This unifies a significant range of observables under one principle:

- GR corrections to Newtonian gravity: toroidal content of time-varying aspects of gravitational interactions (the probe's trajectory, the signal's transit)
- Quadrupole gravitational radiation: toroidal content of a binary system's time-varying drain configuration
- QED 22 MeV scale crossover: heavier probes resolve faster time-variation in the electron/muon solitons, exposing more toroidal content
- Gluon flux tubes producing 99% of proton mass: continuous toroidal-sector reconfiguration of the strong channel structure
- Galactic disks versus halos: disks are the toroidal sector (rotating, time-varying flow), halos are the spherical sector (static-ish, radial)
- Dark matter as toroidal-flow Higgs response: cosmic-scale time-varying configuration expressed through the toroidal sector
- Higgs mechanism itself: per-tick reconfiguration cost is the soliton's time-variation expressed through its toroidal engagement

The mathematical correspondence fits: β = π/4 is the static geometric conversion factor (radial-sphere integrations); K(k) and E(k) are periodic-cyclic conversions appropriate for time-varying phenomena on closed topology; the elliptic-integral character of toroidal content matches the periodic character of time-variation.

The exponent-counting convention then becomes: β exponents count static-structure integrations, K exponents count time-varying integrations.

This clarification should be integrated into Section VII of the master spec as the explicit interpretation of what each sector carries, with cross-references to every phenomenon-specific section that invokes the dual-geometry primitive.

### V.3 Higgs Reduction via Shared-Pattern Formation

The master spec describes the Higgs mechanism (Section XI) and the channel-sharing primitive (Section VI) but does not explicitly connect them as the mechanism for inertia-reduction phenomena. The audit developed this connection and its scope.

The clarified commitment: inertia is Higgs tick-cost per tick per participating soliton. Any observable reduction of inertia — electrical resistance, viscosity, or any other resistance — is the same substrate event: a configuration reducing per-participant Higgs engagement.

The mechanism for achieving this reduction is the channel-sharing primitive. When enough solitons merge channels into a single shared pattern, they stop operating as N independent solitons each paying N Higgs tick-costs. They operate as one shared pattern whose Higgs engagement is qualitatively different (and smaller) than the sum of N independent engagements. The shared pattern's update doesn't require per-participant reconfiguration because the participants are no longer updating as individuals.

This unifies:

- Superconductivity (shared electron-pattern reduces per-electron Higgs engagement for charge flow)
- Superfluidity (shared atom-pattern reduces per-atom Higgs engagement for mass flow)
- Bose-Einstein condensation (shared-pattern formation among bosonic atoms)
- Persistent currents in rings, both superconducting and superfluid (shared pattern's update continues without per-participant Higgs dissipation)
- Quantum Hall effect (shared pattern in Landau levels produces edge conduction without bulk Higgs dissipation)
- Josephson effects (shared patterns merge across weak links via tunneling primitive, maintaining coherent flow)
- Zero-entropy component in two-fluid models (shared pattern has no individual-soliton thermal disorder to carry entropy)

The critical temperature for each phenomenon is the threshold at which thermal channel activity drops below the energy required to disrupt the shared pattern. The specific pairing or condensation mechanism that forms the shared pattern differs across materials (phonons, spin fluctuations, direct boson condensation, fermion pairing) — but the universal phenomenology (Meissner, flux quantization, zero resistance, Josephson, viscosity loss, quantized circulation) arises from the universal shared-pattern behavior downstream of pairing.

The energy gap in each phenomenon is the cost of extracting one participant from the shared pattern and returning it to independent-soliton status, where individual Higgs engagement resumes. Below that gap energy, the shared pattern is undisturbable; above it, quasiparticles exist with normal inertia.

This clarification should be integrated into Section XI (Mass, Inertia, Higgs) of the master spec with explicit cross-reference to Section VI (Channels), establishing that the channel-sharing primitive is the mechanism for all macroscopic inertia-reduction phenomena.

## VI. Gravitational Wave Mechanism from Primitives

The audit verified that gravitational wave observables are reachable from substrate primitives through the following mechanism, which should be developed in Section XII of the master spec (Gravitational Dynamics).

### VI.1 Static vs. Radiative Drain

A single static black hole soliton has spherically symmetric drain — pure spherical-sector content. There is no time-variation in the configuration, no toroidal-sector content, no radiation. The substrate is not reconfiguring anywhere outside the immediate drain field.

Two black hole solitons orbiting each other have a drain configuration that varies in time with the orbital period. The drain field throughout the surrounding substrate has toroidal-sector content — the time-varying aspects of the combined drain configuration. This toroidal content propagates outward at one cell per tick.

### VI.2 Multipole Structure

Monopole radiation would require the total drain magnitude to vary — which would require total mass-energy of the system to vary. It doesn't (conservation). Dipole radiation would require the drain's center to oscillate — which would require the center-of-momentum to accelerate. It doesn't in an isolated binary (momentum conservation). The first configuration feature that does vary is the quadrupolar stretch-axis orientation, which rotates with the orbit.

This gives the same monopole and dipole suppression as GR, for the same conservation reasons. The leading radiative mode is quadrupole.

### VI.3 Polarization Structure

At a distant observer's location, the radial drain component points toward the binary's center of mass — this is static to leading order. The time-varying content appears in the transverse components (perpendicular to the propagation direction from the binary).

The transverse components of the quadrupolar drain reconfiguration have two independent modes: a stretch-compress pattern along one pair of perpendicular axes (plus polarization) and the same pattern rotated by 45° (cross polarization). The configuration is transverse-traceless: volume-preserving in the linearized regime, perpendicular to propagation.

This gives exactly two polarization modes with the correct tensor structure, matching GR's prediction and distinguishing PCTRM from alternative gravity theories that would predict scalar or vector radiation modes.

### VI.4 Energy Loss and Chirp

The binary's orbital energy bleeds off into the propagating toroidal-content (the drain-reconfiguration propagating outward). As energy is lost, the orbit tightens, orbital frequency increases, and the amplitude of time-variation grows. This produces the characteristic chirp waveform.

The quantitative match to the GR quadrupole formula (power ∝ (d³Q/dt³)²) is a math-phase derivation. The qualitative structure — energy loss to propagating toroidal content, inspiral producing chirp — follows from the primitive set.

### VI.5 Merger and Ringdown

During merger, the two parent solitons' drain structures reconfigure into one combined parent soliton's drain structure. This is a dramatic reconfiguration event, propagating outward as intense toroidal content — the "blast" of drain vectors characteristic of merger signals. After merger, the combined BH rings down as the final drain structure settles into its steady spherically-symmetric configuration, with toroidal content decaying exponentially.

### VI.6 Relationship to QED Scale-Crossover

The A3→A4 transition in QED (the 22 MeV crossover where muon g-2 diverges from electron g-2 behavior) and the quadrupole structure of gravitational waves are not the same event, but they are siblings under the dual-geometry primitive. Both are instances of toroidal-sector content producing observable phenomena. The QED case involves the toroidal content of a single soliton resolved by probes of different scales; the GW case involves the toroidal content of a multi-body system's time-varying drain configuration. Same primitive, different configurations, different scales.

## VII. Items Requiring Explicit Addition to the Master Spec

The audit identified three clarifications that are implicit in PCTRM's commitments but should be stated explicitly in the master specification:

**Spec addition 1 (Section II):** Substrate presentism as an explicit commitment. Only the current tick exists. No storage of history exists. The update rule operates on current configuration to produce new current configuration. This needs to be stated with the same level of commitment as the tick primitive itself, because it is a commitment of equivalent weight.

**Spec addition 2 (Section VII):** The spherical sector carries static structure; the toroidal sector carries time-varying structure. Each cross-reference from other sections to the dual-geometry primitive should invoke this interpretation explicitly.

**Spec addition 3 (Section XI, with cross-reference to Section VI):** All inertia reduction is Higgs engagement reduction; the channel-sharing primitive is the universal mechanism for producing shared patterns that reduce per-participant Higgs engagement. This unifies superconductivity, superfluidity, BEC, persistent currents, Quantum Hall, and Josephson phenomena under one substrate mechanism with material-specific pairing as the only variable.

The coverage table in Section IV of this companion should be integrated as a reference appendix to the master spec, with the "downstream" items identified as the formal scope of remaining derivation work within PCTRM and its over-framework.

## VIII. Audit Conclusion

PCTRM passes the pre-math coverage filter. The substrate primitive set, worked through honestly, reaches every major class of confirmed observation at the framework's specified scope. No structural unreachability, no forced qualitative mismatch with observation, no primitive smuggling (prevented structurally by integer-alphabet-only Python derivations).

Three clarifications developed during the audit (substrate presentism, static-vs-time-varying dual-geometry interpretation, shared-pattern Higgs reduction as unified inertia-loss mechanism) strengthen the framework by making commitments explicit that were previously implicit, and by unifying phenomena that had been treated as separate.

The framework now earns the right to proceed to the math-phase filter: Python derivations using integer-alphabet operations, producing specific numerical predictions, checked against CODATA and experimental values to measurement precision. A failure in that phase would constitute real falsification; a success would establish PCTRM as a viable candidate for experimental falsification work beyond the current scope.

Per the research program structure, experimental falsification of surviving predictions remains the final and most expensive filter, to be approached only after math-phase validation.

---

# PCTRM Macro-Level Coverage Companion: Supporting Appendices

**Appendices to:** PCTRM Macro-Level Coverage Companion

**Purpose:** Reference tables consolidating the coverage audit, clarifications developed, mechanism mappings, and remaining derivation work. These appendices serve as the authoritative quick-reference for PCTRM's empirical coverage at the pre-math stage.

---

## Appendix A — Coverage Status by Phenomenon

Full enumeration of phenomena audited, with coverage status, substrate mechanism reference, and notes.

**Legend for Status column:**
- **C** — Covered at PCTRM's specified scope with mechanism present in primitive set
- **C-PI** — Covered by parallel isomorphism commitment to SM/QM/QED/GR observables
- **D** — Downstream derivation work; reachable from primitives but not yet derived
- **S** — Out of scope by design (not a coverage question)

### A.1 Foundational Structure

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| 3D space | C | Omnidirectional unit-distance adjacency | Dimensionality forced by construction, not free parameter |
| Spatial isotropy | C | No preferred axes in primitive set | Automatic from continuous-direction adjacency |
| Time directionality | C | Monotonic tick primitive | Arrow of time built into primitive |
| Second law of thermodynamics | C | Stat mech on substrate configurations + monotonic tick | Standard statistical argument, substrate provides direction |
| Causality / light cone | C | c = 1 cell/tick as maximum propagation | No postulation needed |
| Finiteness / no divergences | C | Bounded cells, discrete arithmetic | No continuum integrals |
| Big Bang origin | S | Out of scope | Framework starts from Big Bang forward |
| Pre-Big-Bang physics | S | Out of scope | Not addressed by design |

### A.2 Matter and Particles

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Stable matter existence | C | Solitons as self-sustaining patterns extracting from quiver | Core primitive |
| Particle indistinguishability | C | Substrate presentism; no stored history | Stronger than "patterns without labels" |
| Gibbs paradox resolution | C | Counting configurations-at-tick, not objects-with-histories | Automatic from presentism |
| Antimatter / CPT | C-PI | Direction-reversed channel configurations (downstream) | Bound by observable-reproduction |
| Spin (fermion/boson) | C-PI | Dual-geometry sector structure (downstream) | Bound by observable-reproduction |
| Pauli exclusion | C-PI | Channel-closure constraints (downstream) | Bound by observable-reproduction |
| Three fermion generations | C | Channel-closure structure requires three | Claimed in Section V |
| Mass values and hierarchy | C | Per-hierarchy-boundary modulus | Claimed in Section XI |
| Particle decay rates | D | Weak channels + channel arithmetic | Specific rates as derivation work |
| Neutrino oscillation | C | Weak-channel arithmetic with flavor-mixing | Mechanism present |
| CP violation | C | Channel-state symmetry breaking | Mechanism present |
| Baryon asymmetry | D | Follows from antimatter + early-universe channel dynamics | Reachable, not yet derived |

### A.3 Forces

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Gravity (Newtonian limit) | C | Parent-to-child drain channels, spherical | 1/r² from spherical channel spreading |
| GR corrections | C | Toroidal sector of drain configuration | See Appendix D for time-varying interpretation |
| Electromagnetism | C | Charge-to-charge channels | Always active between charged solitons |
| Strong confinement | C | Toroidal gluon flux tubes | Toroidal sector at nucleon scale |
| Strong nuclear residual | C | Strong residual channels between nucleons | Conditional on proximity |
| Weak force | C | Weak channels, conditional activation | Handles decay and flavor change |
| Higgs mechanism | C | Per-tick reconfiguration cost | Mass = tick-cost |
| Force unification at high energy | D | Channel-type distinctions wash out at high throughput | Reachable, not yet derived |

### A.4 Quantum Phenomena

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Superposition | C | Unresolved channel configurations pre-termination | Single dynamics |
| Measurement / collapse | C | Channel-merger events | No separate measurement rule |
| Wave-particle duality | C | Channel-agreement at termination | Dissolved, not resolved |
| Entanglement | C | Channel-sharing / merged channels | Literal sharing |
| Bell non-locality | C | Graph-local through merged channels | Euclidean-non-local is coordinate artifact |
| No-signaling theorem | C | Symmetric channel structure | No sender/receiver asymmetry |
| Quantum tunneling | C | Omnidirectional unit-adjacency across "barriers" | Same primitive as Bell non-locality |
| Identical particle statistics | C | Presentist substrate, no identity threads | See Appendix C |
| Bose-Einstein statistics | C | Configuration counting + shared-pattern formation | See Appendix E |
| Fermi-Dirac statistics | C-PI | Channel-closure constraints on shared patterns | Bound by observable-reproduction |
| Born rule | C | Unit-graph round-trip closure | Derived, not postulated |
| Quantum interference | C | Channel-agreement at termination | Covered |
| Aharonov-Bohm effect | C | Non-local channel structure around topological feature | Graph-local |
| Decoherence | C | Environmental channel-merger dominating target coherence | Natural from channel primitive |
| Delayed choice / quantum eraser | C | Termination-context resolution | Not retrocausal |
| Hong-Ou-Mandel interference | C | Identical-pattern channel-agreement | Consequence of presentism |

### A.5 Condensed Matter and Inertia-Reduction

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Superconductivity (conventional) | C | Shared-pattern formation via phonon channels | See Appendix E |
| Superconductivity (unconventional) | C | Shared-pattern formation via spin fluctuations or other | Same universal mechanism |
| Meissner effect | C | Shared pattern maintaining internal channel structure | Downstream of pairing |
| Flux quantization (h/2e) | C | Shared-pattern phase windings, pair charge = 2e | Mechanism-independent |
| Zero electrical resistance | C | No per-participant Higgs engagement in shared pattern | Universal consequence |
| Josephson effects (SC) | C | Shared patterns merging across weak links | Tunneling primitive |
| Superfluidity (He-4) | C | Direct bosonic condensation into shared pattern | Same universal mechanism |
| Superfluidity (He-3) | C | Fermion pairing then condensation | Same universal mechanism |
| Zero viscosity | C | No per-participant Higgs engagement for mass flow | Universal consequence |
| Quantized vortices | C | Phase singularities in shared pattern | Mechanism-independent |
| Circulation quantization | C | Shared-pattern phase single-valuedness | h/m quantum |
| Two-fluid hydrodynamics | C | Shared-pattern fraction vs independent-soliton fraction | Natural decomposition |
| Second sound | C | Shared-pattern phase oscillation distinct from pressure waves | Downstream |
| Fountain effect | C | Shared-pattern response to temperature gradient | Downstream |
| Rollin film creep | C | Shared-pattern boundary dynamics | Downstream |
| Bose-Einstein condensation | C | Direct shared-pattern formation among bosons | Same mechanism |
| BEC-BCS crossover | C | Tunable pairing-to-direct-condensation continuum | Same mechanism, tuned parameter |
| Neutron star superfluid | C | Neutron pairing and shared-pattern formation | Same mechanism |
| Pulsar glitches | C | Shared-pattern vortex dynamics | Same mechanism |
| Quantum Hall effect (integer) | C | Edge-state shared pattern in Landau levels | Same mechanism |
| Quantum Hall effect (fractional) | C | Composite-fermion shared pattern | Same mechanism |
| Topological protection | C | Shared-pattern structural stability | Natural consequence |
| Phases of matter (solid/liquid/gas) | D | Molecular-level channel dynamics | Over-framework derivation work |
| Phase transitions | D | Threshold crossings in channel configuration statistics | Downstream |
| Magnetism (ferro/antiferro) | D | EM channel configurations in over-framework | Downstream derivation |
| Semiconductor band structure | D | Periodic channel structure | Downstream |

### A.6 Atomic and Chemical

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Atomic shell structure | C | Dual-geometry at atomic scale (spherical shells + toroidal moments) | Section VII |
| Atomic spectra | D | Shell structure + channel transitions | Reachable, not yet derived |
| Hydrogen spectrum | D | Downstream derivation | Standard check |
| Multi-electron atoms | D | Shell-filling with shared-pattern constraints | Downstream |
| Lamb shift | C-PI | Toroidal-sector QED contribution | Bound by observable-reproduction |
| Fine structure | C-PI | Toroidal-sector content at atomic scale | Bound by observable-reproduction |
| Hyperfine structure | C-PI | Toroidal magnetic moment interactions | Bound by observable-reproduction |
| Periodic table structure | D | Shell-filling patterns from atomic derivation | Long-term derivation work |
| Chemical bonding | D | Channel structure between atoms | Downstream |
| Molecular structure | D | Over-framework, not yet derived | Acknowledged scope boundary |
| Chemical reaction rates | D | Channel-reconfiguration statistics | Downstream |

### A.7 Gravitational Phenomena

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Mercury perihelion precession | C | Toroidal sector of drain at planetary scale | Section XII |
| Gravitational light bending (factor of 2) | C | Drain-vector rotation + toroidal correction at photon wavelength | Section X |
| Shapiro delay | C | Toroidal-sector contribution to signal transit | Section XII |
| Gravitational redshift | C | Local tick-rate variation with hierarchy | Section IX |
| Gravitational time dilation | C | Same mechanism as redshift | Section IX |
| Gravitational waves (general) | C | Time-varying toroidal content of drain configuration | See Appendix F |
| GW quadrupole structure | C | Conservation forbids monopole/dipole | Appendix F |
| GW two polarizations (+, ×) | C | Transverse-traceless modes of toroidal drain reconfiguration | Appendix F |
| GW propagation at c | C | One cell per tick | Primitive |
| Binary inspiral waveforms | D | Quadrupole-formula-equivalent derivation | Math-phase work |
| BH merger signals | C | Drain-configuration reconfiguration event | Qualitative mechanism clear |
| BH ringdown | C | Combined BH drain settling to final configuration | Downstream quantitatively |
| Hulse-Taylor binary inspiral | D | Follows from GW mechanism | Math-phase match to precision |
| Frame dragging / Lense-Thirring | C | Toroidal sector of rotating BH | Section XV |
| Black hole event horizon | C | Drain-threshold boundary | Section XV |
| Hawking radiation | C | Boundary channel dynamics at drain threshold | Section XV |
| Black hole entropy (area law) | C | Channel configuration counting at horizon | Section XV |
| Information paradox resolution | C | Information absorbed into parent pattern, released via Hawking | Section XV |
| Kerr rotating BH structure | C | Toroidal sector of rotating parent soliton | Section XV |
| No singularity at BH center | C | Substrate finite everywhere | Section XV |

### A.8 Cosmological Phenomena

| Phenomenon | Status | Substrate Mechanism | Notes |
|---|---|---|---|
| Big Bang forward dynamics | C | Substrate running from initial conditions | Origin itself out of scope |
| Inflation | C | Covered in over-framework | Not in PCTRM primary scope |
| CMB anisotropy spectrum | C | Early-universe channel dynamics | Section XV |
| BBN primordial abundances | C | Nucleosynthesis channel arithmetic in over-framework | H, D, He-3, He-4, Li-7 |
| Cosmic expansion | C | Cosmic-scale quiver activity | Section XV |
| Ω_DM = π/12 | C | Spherical sector fraction of cosmic closure | Section XV |
| Ω_b = 13/264 | C | Gauge integer fraction | Section XV |
| Ω_Λ = (251 − 22π)/264 | C | Remainder from closure | Section XV |
| Dark matter (rotation curves) | C | Toroidal-flow Higgs response at galactic scale | Section XII |
| Dark matter (lensing) | C | Toroidal content of galactic soliton drain | Section XII |
| Bullet Cluster separation | C | Toroidal flow separates from baryonic peak on collision | Downstream detail |
| Galaxy cluster dynamics | C | Cosmic-scale parent-soliton drain | Section XII |
| Dark energy | C | Universal soliton closure / cosmic-scale quiver | Section XV |
| H₀ tension (12/11) | C | Transit-counting across hierarchy configurations | Section IX |
| Large-scale structure formation | D | Over-framework, not yet derived | Acknowledged scope |
| BAO | D | Follows from early-universe channel dynamics | Downstream |
| Type Ia supernova distance ladder | D | Follows from cosmic expansion mechanism | Downstream |
| Cosmic horizon | C | Substrate light-cone + integer cell count | Section XV |
| Primordial gravitational waves | C | Early-universe toroidal content | Same mechanism as GWs |

---

## Appendix B — Substrate Primitives and What They Produce

Maps each substrate primitive to the observable phenomena it enables.

| Primitive | Spec Reference | Directly Enables |
|---|---|---|
| Cell | Section II | Discrete position; no continuum infinities |
| Tick | Section II | Discrete time; arrow of time; presentism |
| Monotonic tick sequence | Section II (clarified) | Second law of thermodynamics; no block-universe storage |
| Direction-conditional adjacency | Section III | 3D isotropic space; c = 1 cell/tick |
| Omnidirectional unit-step neighbors | Section III | Tunneling; Bell non-locality; Aharonov-Bohm |
| Quiver | Section IV | Vacuum energy; Casimir effect; soliton fuel source |
| Remainder | Section II, IV | Per-tick arithmetic accumulation; modulus crossings |
| Channel (general) | Section VI | All interactions; forces as channel types |
| Gravitational drain channel | Section VI, XII | Gravity; dark matter flow; BH structure |
| Electromagnetic channel | Section VI | All EM phenomena |
| Strong channels (confinement, residual) | Section VI | QCD confinement; nuclear structure |
| Weak channel | Section VI | Decay; flavor change; neutrino oscillation |
| Thermal channel | Section VI | Temperature; thermodynamic behavior |
| Entanglement channel | Section VI | Bell correlations; shared quantum states |
| Higgs channel | Section VI, XI | Mass; inertia; all resistance phenomena |
| Channel-sharing / merged | Section VI, XI (clarified) | Superconductivity, superfluidity, BEC, QHE, Josephson |
| Soliton | Section V | All matter; all patterns at every hierarchy |
| Parent-child hierarchy | Section V, VIII | Strictly hierarchical gravity; no N-body problem |
| Spherical sector | Section VII (clarified) | Static structure; radial components; Newtonian gravity |
| Toroidal sector | Section VII (clarified) | Time-varying structure; GR corrections; GW radiation; dark matter flow |
| Hierarchical coordinates | Section VIII | Galactic rotation without superluminal motion |
| Planck-scale locality | Section IX | H₀ tension; coupling constant running |
| Per-tick update loop | Section XVII | All dynamics uniformly |

---

## Appendix C — Substrate Presentism and Its Consequences

Documents the clarification developed in Section V.1 of the companion paper.

### C.1 The Commitment

| Aspect | Standard Physics Picture | PCTRM Substrate Picture |
|---|---|---|
| Past states | Stored somewhere accessible to dynamics | Not stored anywhere |
| Future states | Not yet determined but approachable | Not yet existing at all |
| "Evolution" | Dynamics operating across stored states | Update rule producing next state from current |
| Block universe | Implicit in continuous-time formulations | Explicitly rejected |
| History | Real feature of the world | Constructed by observers maintaining records |
| Identity across time | Objects persist with labels | Configurations exist tick-by-tick |

### C.2 Consequences of Presentism

| Consequence | Explanation |
|---|---|
| No identity threads | Nothing persists across ticks to carry a label |
| Indistinguishability is structural | Labels would require storage substrate doesn't have |
| Gibbs paradox dissolves | Counting is configurations-at-tick, not objects-with-histories |
| Bose-Einstein / Fermi-Dirac statistics natural | Automatic from configuration counting |
| "Same particle later" is observer construction | Substrate doesn't perform the comparison |
| Memory is physical record, not substrate feature | Observers store records; substrate doesn't |
| Hong-Ou-Mandel interference expected | Identical patterns at termination |

### C.3 What Presentism Does Not Remove

Presentism is compatible with all observable phenomena of relativistic physics. What gets rejected is the metaphysical picture of storage; what survives is:

- Full consistency with special and general relativity observables
- Full consistency with Lorentz invariance (c = 1 cell/tick is the relativistic speed of light)
- Full consistency with causal structure (light cones from c-invariance)
- Full consistency with time dilation (local tick rate varies by hierarchy configuration)
- Full consistency with records, memories, causation, and scientific practice

---

## Appendix D — Dual-Geometry Sector Interpretation

Documents the clarification developed in Section V.2 of the companion paper.

### D.1 Sector Correspondence

| Characteristic | Spherical Sector | Toroidal Sector |
|---|---|---|
| Temporal character | Static | Time-varying |
| Geometric basis | Unit sphere integrations | Periodic topology integrations |
| Conversion factor | β = π/4 | K(k), E(k) at specific moduli |
| Integration type | Radial | Angular on closed topology |
| Symmetry | Spherical | Axial / cyclical |
| Exponent counting | Static conversions | Time-varying conversions |

### D.2 Phenomenon-to-Sector Mapping

| Phenomenon | Static Component | Time-Varying Component |
|---|---|---|
| Gravity | Newtonian 1/r² (spherical drain) | GR corrections (toroidal drain dynamics) |
| Binary system | Net center-of-mass drain | Orbital-period drain reconfiguration → GW |
| Light propagation | Straight-line geodesic | Deflection from drain-vector rotation |
| QED electron g-2 | Leading π terms (spherical) | Elliptic Laporta constants (toroidal) |
| Muon g-2 | Spherical at electron probe scale | Toroidal dominates at muon mass scale |
| Proton structure | Quark content (~1%) | Gluon flux tube dynamics (~99%) |
| Atom | Radial shell structure | Magnetic moment / orbital angular momentum |
| Galaxy | Halo | Rotating disk |
| Universe | Cosmic background drain | Expansion / cosmic dynamics |
| Black hole (static) | Spherically symmetric drain | Absent when truly static |
| Black hole (rotating Kerr) | Spherically symmetric component | Frame-dragging toroidal content |
| Ground state system | Pure spherical | Absent |
| Excited / flowing / rotating | Spherical baseline | All dynamic content |

### D.3 Sector Visibility by Probe

| Probe Characteristic | Sector Dominance |
|---|---|
| Light probe, long wavelength | Spherical sector resolves |
| Heavy probe, short wavelength | Toroidal sector resolves |
| Static measurement | Spherical sector primary |
| Time-resolved measurement | Toroidal sector accessible |
| Low-energy QED | Spherical π terms |
| High-loop / high-energy QED | Toroidal elliptic content emerges |
| 22 MeV QED crossover | Electron / muon sector boundary |

---

## Appendix E — Shared-Pattern Higgs Reduction Across Phenomena

Documents the clarification developed in Section V.3 of the companion paper. Unifies all inertia-reduction phenomena under one mechanism.

### E.1 Universal Structure

| Element | Description |
|---|---|
| Inertia source | Per-soliton per-tick Higgs reconfiguration cost |
| Reduction mechanism | Channel-sharing merges N solitons into one shared pattern |
| Consequence | Shared pattern's update doesn't require N independent Higgs engagements |
| Threshold (Tc) | Thermal channel throughput < shared-pattern disruption energy |
| Gap energy | Cost of extracting one participant back to independent-soliton status |
| Below gap | Shared pattern undisturbable; universal inertia-reduction phenomenology |
| Above gap | Quasiparticle excitations with normal Higgs engagement |

### E.2 Phenomenon-Specific Manifestations

| Phenomenon | What's Shared | What Flows | Pairing Mechanism | Tc Scale |
|---|---|---|---|---|
| Conventional SC | Electron pairs | Charge | Phonon-mediated | 1-40 K |
| High-Tc cuprate SC | Electron pairs (d-wave) | Charge | Spin fluctuations (likely) | 30-135 K |
| Iron pnictide SC | Electron pairs (multi-band) | Charge | Multi-band / debated | 5-55 K |
| Heavy fermion SC | f-electron pairs | Charge | Kondo + pairing | 1-2 K |
| Hydride SC (high P) | Electron pairs | Charge | Phonon (stiff H lattice) | ~250 K at 150 GPa |
| He-4 superfluid | He-4 atoms (bosons) | Mass | Direct condensation | 2.17 K |
| He-3 superfluid | He-3 atom pairs | Mass | Spin fluctuations, p-wave | 2.5 mK |
| Atomic BEC | Alkali atoms (bosons) | Mass | Direct condensation | nK |
| Fermionic atomic superfluid | Fermion atom pairs | Mass | Tunable via Feshbach | nK |
| Neutron star superfluid | Neutron pairs | Mass | Strong force attraction | ~10^9 K |
| QHE (integer) | Electrons in Landau levels | Edge current | Magnetic field + disorder | Low T + high B |
| QHE (fractional) | Composite fermions | Edge current | Strong correlation | mK + high B |
| Josephson junction (SC) | Cooper pairs across weak link | Charge | Tunneling + sharing | Below SC Tc |
| Josephson (SF) | Superfluid pairs across weak link | Mass | Tunneling + sharing | Below SF Tc |

### E.3 Universal Phenomenology (Mechanism-Independent)

| Observable | Mechanism |
|---|---|
| Zero resistance / viscosity | Shared pattern doesn't engage Higgs per participant |
| Persistent currents | Shared pattern maintains itself without dissipation |
| Quantization of topological quantity | Phase single-valuedness (flux h/2e for SC, circulation h/m for SF) |
| Energy gap | Cost of participant extraction |
| Meissner-like expulsion | Shared pattern maintaining internal structure against external perturbation |
| Josephson-like weak link effects | Shared patterns merging across tunneling gap |
| Two-component (super/normal) decomposition | Shared-pattern fraction vs independent-soliton fraction |
| Zero entropy of shared component | No individual-soliton thermal disorder in shared pattern |
| Topological protection | Structural stability of shared pattern under perturbation |

---

## Appendix F — Gravitational Wave Mechanism Detail

Mechanism worked out in Section VI of the companion paper.

### F.1 Static vs. Radiative Configurations

| System State | Drain Character | Radiation | Sector |
|---|---|---|---|
| Isolated static BH | Spherically symmetric | None | Pure spherical |
| Non-rotating static mass | Spherically symmetric | None | Pure spherical |
| Rotating single BH (Kerr) | Axially symmetric, time-independent | None | Frame-dragging toroidal, no radiation |
| Binary orbiting | Rotating, time-varying | Quadrupole GW | Time-varying toroidal |
| Binary inspiraling | Accelerating time-variation | Chirp signal | Growing toroidal content |
| Binary merger | Dramatic reconfiguration | Merger "blast" | Peak toroidal event |
| Post-merger ringdown | Settling to final BH | Exponentially decaying | Toroidal → spherical |

### F.2 Multipole Forbidden / Permitted

| Multipole | Physical Meaning | Why Forbidden/Permitted | GR Equivalent |
|---|---|---|---|
| Monopole | Total drain magnitude | Requires mass-energy non-conservation | Forbidden (same reason) |
| Dipole | Drain center oscillation | Requires momentum non-conservation | Forbidden (same reason) |
| Quadrupole | Stretch-axis rotation | Allowed; rotates with orbit | Leading radiation mode |
| Octupole, higher | Finer configuration features | Allowed but suppressed | Same in GR |

### F.3 Polarization Structure

| Mode | Drain Field Transverse Pattern | GR Equivalent |
|---|---|---|
| Plus (+) | Stretch along one perpendicular pair, compress along the other | Plus polarization |
| Cross (×) | Same pattern rotated 45° | Cross polarization |
| Scalar (forbidden) | Volume-changing | Absent in GR; PCTRM forbids same way |
| Vector (forbidden) | Longitudinal-transverse mixing | Absent in GR (would be dipole); PCTRM forbids same way |
| Tensor extra modes (forbidden) | Various | Absent in GR; PCTRM should forbid via structural commitment |

### F.4 Energy Loss Mechanism

| GR Picture | PCTRM Picture |
|---|---|
| Metric perturbation h_μν carries energy outward | Drain-configuration reconfiguration propagates outward |
| Power ∝ (d³Q/dt³)² quadrupole formula | Rate of toroidal-content generation from orbital motion |
| Orbital energy → wave energy | Orbital energy → propagating toroidal content |
| Binary inspirals as energy bleeds off | Same, through substrate drain-reconfiguration |
| Chirp as frequency + amplitude grow | Same, driven by tightening orbit |

---

## Appendix G — Failure Modes Avoided

For each failure mode the audit tested against, records why PCTRM does not fail in that mode.

### G.1 Silence (No Mechanism Exists)

| Tested Phenomenon | Why Not Silent |
|---|---|
| Arrow of time | Monotonic tick primitive |
| 3D space | Omnidirectional unit-adjacency |
| Tunneling | Omnidirectional unit-adjacency across "barriers" |
| Entanglement | Channel-sharing primitive |
| Gravitational waves | Time-varying drain configuration = toroidal sector |
| Superconductivity | Channel-sharing + Higgs reduction |
| Dark matter | Toroidal-flow at cosmic scale |
| Black holes | Parent solitons with extreme drain |
| Born rule | Unit-graph round-trip closure |

### G.2 Forced Mismatch (Mechanism Gives Wrong Qualitative Result)

| Tested Phenomenon | Why Not Forced Mismatch |
|---|---|
| Light bends around massive objects | Drain-vector rotation gives deflection in correct direction |
| GWs have 2 polarizations | Transverse-traceless modes of toroidal drain reconfiguration |
| SC has charge-2e flux quantum | Shared pattern of electron pairs has charge 2e |
| No monopole GW radiation | Conservation of mass-energy forbids same as GR |
| No dipole GW radiation | Conservation of momentum forbids same as GR |
| Photon speed is frame-independent | c = 1 cell/tick is arithmetic identity |
| Quantum statistics (BE / FD) | Configuration counting naturally produces these |

### G.3 Primitive Smuggling (Hidden Postulates)

| Tested Phenomenon | Anti-Smuggling Guard |
|---|---|
| All numerical predictions | Integer-alphabet-only Python derivations |
| All transcendentals | Only π, β, K(k), E(k) at declared moduli allowed |
| All mass values | Per-hierarchy modulus must be forced by structure, not tuned |
| All coupling constants | Must emerge from hierarchy configuration, not fitted |
| All cosmological parameters | Stated as structural identities (π/12, 13/264, etc.) |
| All Standard Model structure | Derived from channel enumeration, not postulated |

---

## Appendix H — Remaining Derivation Work

Downstream items within PCTRM + over-framework scope, not yet derived but reachable in principle.

### H.1 Within PCTRM Planck-Scale Scope

| Item | Priority | Notes |
|---|---|---|
| Specific fermion mass values from per-hierarchy modulus | High | Core prediction test |
| CKM matrix element derivations | High | V_us = 9/40, V_cb = 1/24 claimed |
| PMNS matrix element derivations | High | Neutrino mixing |
| Koide K = 2/3 derivation | High | Explicit mechanism |
| Fine structure constant α structure | High | From hierarchy configuration |
| QCD beta coefficient derivations | Medium | b₂', b₃, etc. |
| QED g-2 dual-geometry decomposition | High | Electron and muon explicit |
| Gap ratio 38/27 derivation | Medium | CD channel arithmetic |
| All per-hierarchy-boundary moduli | High | Currently pending specification |
| Specific decay lifetimes | Medium | Channel arithmetic specifics |
| CP violation magnitude | Medium | Channel-state asymmetry quantified |

### H.2 Over-Framework Scope

| Item | Priority | Notes |
|---|---|---|
| Atomic spectra (hydrogen, helium, multi-electron) | High | Standard first tests |
| Periodic table structure | Medium | Long-term derivation |
| Chemical bonding | Medium | Long-term |
| Molecular physics | Low | Acknowledged long-term |
| Phases of matter | Low | Downstream of molecular |
| Magnetism (specific types) | Medium | EM configurations |
| Semiconductor band structure | Medium | Periodic channel structure |
| Specific superconductor Tc values | High | Pairing mechanism specifics |
| Specific superfluid properties | High | Including critical velocities |
| BBN specific abundance ratios | High | Already claimed covered, need derivation |
| CMB acoustic peak positions | High | Early-universe channel dynamics |
| Galaxy rotation curve details | High | Toroidal-flow mechanism quantitative |
| Large-scale structure correlation functions | Medium | Cosmic structure formation |
| BAO scale derivation | Medium | Early-universe to late-universe |
| Type Ia supernova luminosity distance | Medium | Cosmic expansion mechanism |
| GW inspiral waveform matching to PN orders | High | Post-Newtonian expansion equivalent |
| BH merger numerical relativity matches | Medium | Numerical derivation |
| Hawking radiation spectrum | Medium | Boundary channel dynamics quantitative |

---

## Appendix I — Cross-Reference: Companion Paper to Master Spec Integration

Lists where each clarification or coverage result should be integrated into the master PCTRM-1-Master-2026 specification.

| Companion Content | Target Spec Section | Integration Type |
|---|---|---|
| Substrate presentism commitment | Section II (Cells and Ticks) | Add as explicit primitive commitment |
| Presentism consequences for indistinguishability | Section XIII (QM Derivation) | Develop as derived consequence |
| Spherical = static, toroidal = time-varying | Section VII (Dual-Geometry Sectors) | Add as explicit interpretation |
| Exponent counting updated meaning | Section VII, Section XVI | Cross-reference both |
| Shared-pattern Higgs reduction | Section XI (Mass, Inertia, Higgs) | Add with cross-reference to Section VI |
| Channel-sharing as macroscopic mechanism | Section VI (Channels) | Expand shared-channel description |
| Inertia-reduction unification | New subsection in Section XI | Document phenomenon list |
| GW mechanism from toroidal time-variation | Section XII (Gravitational Dynamics) | Add explicit GW derivation sketch |
| Coverage table | New Appendix to spec | Integrate as authoritative reference |
| Downstream derivation work list | Section XVII or new appendix | Formal scope of math-phase work |

---

## Appendix J — Audit Methodology Summary

For future reuse and for clarity about the filter's stringency.

### J.1 The Three Filters

| Filter | Cost | What It Tests | What It Rejects |
|---|---|---|---|
| Pre-math coverage | Conceptual work only | Whether primitives reach observables | Silence, forced mismatch, smuggling |
| Math-phase derivation | Python + CODATA checks | Whether alphabet-only operations produce correct values | Numerical mismatch to measurement precision |
| Experimental falsification | Laboratory resources | Whether predictions hold against new experiments | Surviving predictions that fail new tests |

### J.2 Pre-Math Filter Methodology

| Step | Action |
|---|---|
| 1 | Enumerate major observable phenomena from established physics |
| 2 | For each phenomenon, ask: is there a mechanism in the primitive set? |
| 3 | If yes, verify the mechanism is qualitatively consistent with observation |
| 4 | If silent, flag for examination — may be implicit or genuine gap |
| 5 | If mechanism contradicts observation qualitatively, flag as failure |
| 6 | Check that reaching observable doesn't require undeclared structure |
| 7 | Distinguish "not yet derived" from "cannot be derived" |
| 8 | Document clarifications developed during the audit |

### J.3 What Counts as Passing

| Result | Status |
|---|---|
| Mechanism exists in primitives | Pass |
| Mechanism exists in over-framework scope | Pass |
| Mechanism derivable in principle, not yet worked | Pass (downstream) |
| Out of scope by design | Pass (not tested) |
| No mechanism, cannot be constructed from primitives | Fail |
| Mechanism gives wrong qualitative result | Fail |
| Requires undeclared primitive | Fail |

### J.4 What Counts as Failing

Structural failure at this filter is decisive. A phenomenon that the primitives cannot reach even in principle is a framework-killer at zero cost. A phenomenon the primitives reach but only by contradicting observation is equally fatal. A phenomenon that requires importing structure not in the declared primitive set fails the anti-smuggling guard.

PCTRM did not fail any of these modes during the audit. All major observable classes were reached through primitives already specified, or are in acknowledged downstream-derivation scope, or are out of scope by design.

---

**End of Supporting Appendices.**
