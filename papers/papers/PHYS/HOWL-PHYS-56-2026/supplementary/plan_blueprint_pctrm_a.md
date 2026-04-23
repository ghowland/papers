# PCTRM Master Specification — Planning Document

**Target:** PCTRM-1-Master-2026 (supersedes PCTRM-1-2026 and PCTRM-2-2026)

**Purpose:** Complete blueprint of PCTRM as proposed. Every commitment, mechanism, and structural claim from the program's development, stated without hedging. This is the specification; falsification/testing/program are separate documents.

**Audience:** Physicists and framework developers who need the full technical ontology.

---

## Structural principle for the spec

One document, fifteen sections, each stating what PCTRM commits to at a specific layer of the substrate. Each section declares. No "might work" or "if X then Y." The spec says what PCTRM is.

Sections are ordered from foundation upward: substrate primitives → coordinate system → dynamics → hierarchy → phenomena. Each layer builds on the previous. By the end, the framework has specified everything from Planck cells up through cosmological structure.

---

## Section plan

### Section I — The Substrate Ontology

Opens with the minimal ontology claim. Nothing exists below this level. The substrate is a unit-adjacency graph with direction-conditional continuous neighbors, discrete per-tick arithmetic, and channel-mediated extensions.

**Content:**
- The five primitives enumerated: cells, ticks, direction-conditional adjacency, remainder, channels
- What each primitive is structurally
- What the substrate does per tick
- The minimality claim: no additional structure exists

**Key commitment:** The substrate is complete as specified. The universe is this, and nothing else.

### Section II — Cells and Ticks

Details the cell and tick structure.

**Content:**
- Cell as substrate position primitive (no internal structure below this)
- Tick as substrate temporal primitive (no finer time division)
- The Planck scale as local configuration (Earth-local values; hierarchy-specific)
- What happens between ticks (nothing) and at ticks (substrate arithmetic runs)
- The finite count of cells in the universe (bounded by construction)
- The distinction between cell structure and the quiver (substrate's per-tick baseline activity)

**Key commitments:**
- No spacetime continuum. Discrete cells and ticks all the way down.
- Planck scale is hierarchy-local, not universal.
- The substrate is finite, producing no divergences.

### Section III — Direction-Conditional Adjacency

Specifies the topology that makes discrete substrate compatible with observed isotropy.

**Content:**
- Each cell has neighbors at exactly one Planck distance in any continuous direction
- Direction is continuous; position is discrete; adjacency is direction-keyed
- The topology is a graph, not a manifold — this is the deepest structural commitment
- How the graph produces isotropy without preferred directions
- Contrast with cubic lattice, hypergraph, and other discrete-substrate approaches
- The unit-sphere structure that emerges automatically from unit-distance adjacency

**Key commitments:**
- Graph, not manifold. This is foundational.
- Unit distance is the only distance that exists at the substrate level.
- Continuous direction + discrete position = unit sphere structure from construction.

### Section IV — The Quiver: Universal Remainder Source

Specifies the substrate's baseline per-tick activity.

**Content:**
- The quiver as substrate's own per-tick arithmetic running continuously at every cell
- What the quiver is (substrate activity) vs what it isn't (a field imposed on substrate)
- How the quiver is the source of all soliton remainder
- The distinction between vacuum (no soliton propagating) and absence (which doesn't exist)
- Connection to quantum vacuum fluctuations, zero-point energy, Casimir effect
- Quiver extraction as the universal remainder-acquisition mechanism
- How all solitons extract from the quiver each tick

**Key commitments:**
- The universe is never empty at the substrate level.
- Vacuum is the substrate being itself, not a container for anything else.
- Every soliton extracts from the quiver each tick to maintain its pattern.

### Section V — Solitons and the Hierarchy

Specifies what solitons are and how the hierarchy is organized.

**Content:**
- Soliton as stable, self-sustaining pattern in substrate arithmetic
- The pattern-not-substance commitment: mass is inertia, not stuff
- The nested hierarchy from Planck cells to universal soliton
- Seven explicit levels: Level 0 (substrate), Level 1 (subatomic), Level 2 (atomic), Level 3 (nuclear), Level 4 (molecular), Level 5 (macroscopic), Level 6 (cosmological)
- Each level's characteristic scale and representative examples
- Interface/implementation: same vocabulary at every level, different implementations
- Parent-child relationships: soliton contains soliton contains soliton
- Sibling relationships at the same hierarchy level
- The universal soliton as the hierarchy's outermost boundary

**Key commitments:**
- Everything is a soliton. Fermions, bosons, atoms, planets, galaxies, the universe.
- Hierarchy is fundamental. No soliton exists without its parent soliton context.
- The substrate produces the hierarchy; the hierarchy produces all observable structure.

### Section VI — Channels

Specifies what channels are and catalogs their types.

**Content:**
- Channel as adjacency extension between solitons
- How channels differ from direct adjacency (cell-to-cell)
- Channel properties: endpoints, direction, throughput, activation state
- Channel types catalog:
  - Gravitational (drain toward parent soliton, always active)
  - Electromagnetic (charge-to-charge, always active between charged solitons)
  - Strong confinement (within nucleon boundary, always active)
  - Strong residual (between nucleons, conditional on proximity)
  - Weak (conditional on specific interaction events)
  - Thermal (omnidirectional, always active)
  - Entanglement (binary activation, triggered by specific interactions)
  - Higgs (always active for massive solitons, modulates tick-cost per cycle)
  - Channel-sharing/merged (dynamic, forms during entanglement-creating interactions)
- Channels as soliton-bound (not cell-bound) — they move with the soliton through cells
- How channels compose when multiple act on the same soliton simultaneously

**Key commitments:**
- Channels are the framework's interaction primitive.
- Channels extend adjacency beyond cell-to-cell.
- All observed forces are channel types with specific rules.

### Section VII — Dual-Geometry Sectors

Specifies the spherical modulus / toroidal remainder decomposition.

**Content:**
- Every soliton has two geometric sectors: spherical (modulus) and toroidal (remainder)
- The spherical sector: angular operations on spherical subspaces, β = π/4 conversion factor
- The toroidal sector: angular operations on topological tori, K(k)/π conversion factor with topology-specific modulus k
- The three-layer decomposition at every scale:
  - Spherical modulus (β² content)
  - Number-theoretic β⁰ remainder (ζ values, polylogarithms, rationals — radial integrations, diagram combinatorics)
  - Toroidal-geometric β⁰ remainder (K(k), E(k), elliptic content — angular integrations on topological tori)
- Dual-geometry manifestations at each hierarchy level:
  - Proton: spherical confinement boundary + toroidal gluon flux tubes (99% of mass)
  - Atom: spherical shells + toroidal magnetic moment structure
  - Planet: spherical atmospheric layers + toroidal belts/fields
  - Galaxy: spherical halo + toroidal disk
  - QED four-loop: spherical π terms + toroidal Laporta constants
- Probe-dependent sector dominance: light probes see spherical, heavy probes see toroidal
- The 22 MeV crossover in QED: electron sees spherical, muon sees toroidal
- Topology-specific moduli catalog: k₈₁, k₈₃, pending per-hierarchy-boundary moduli

**Key commitments:**
- Every soliton has two geometric sectors. This is universal.
- Different probes resolve different sectors.
- The sectors are structural, not optional.

### Section VIII — The Hierarchical Coordinate System

Specifies that coordinates are hierarchy-local, not Euclidean.

**Content:**
- Running reading depth as the primary position coordinate
- No universal Cartesian grid
- Position is defined within each hierarchy level relative to that level's parent
- Distance (Planck cells between A and B) is hierarchy-local
- The distance from Earth to Moon is in Earth's hierarchy; Sun to Earth is in Sun's hierarchy; they are not comparable as Planck cells across hierarchies
- Hill sphere and other soliton boundaries as substrate-level transitions between hierarchies
- Motion through the substrate vs. motion within a soliton's configuration
- How apparent velocities (galactic rotation, cosmic expansion) can exceed c locally without violating c-invariance
- Multi-scale coordinate hierarchy: observations require identifying appropriate hierarchy level

**Key commitments:**
- No universal coordinate system. All coordinates are hierarchical.
- Planck-cell counts are hierarchy-local.
- Transitions between hierarchies happen at substrate-level boundaries (Hill sphere, etc.).
- What appears as high velocity in Euclidean coordinates may be small velocity in hierarchical coordinates.

### Section IX — Planck-Scale Locality

Specifies that Planck length and Planck time vary with soliton configuration.

**Content:**
- Planck length and Planck time as measurements of local substrate configuration
- The values measured on Earth (10⁻³⁵ m, 10⁻⁴⁴ s) are Earth-local
- Different soliton hierarchies have different local cell and tick durations
- What remains universal: cell-per-tick = c, integer alphabet, structural relationships
- What varies: absolute dimensional quantities, coupling constants, "fundamental constants"
- The H₀ tension (12/11 between SH0ES and Planck) as hierarchy-configuration difference
- Gravitational redshift as measurement of local tick rate
- Connection to renormalization group running of coupling constants
- Why dimensionless ratios are preserved across hierarchies

**Key commitments:**
- Planck scale is hierarchy-local.
- c = 1 cell/tick is universal; absolute cell/tick durations are not.
- Integer alphabet is universal; dimensional measurements are hierarchy-specific.
- Coupling constants vary with hierarchy configuration.

### Section X — Photon Propagation and c-Invariance

Specifies how photons work and why c is invariant.

**Content:**
- Photon as pattern-of-coupling extracting from quiver, no Higgs interaction
- Advancing exactly one cell per tick by construction
- N cells between emission and absorption, N ticks elapsed, N/N = 1
- c-invariance for photons as arithmetic identity, not postulate
- Observers as absorbers, not watchers (photons unobservable in flight)
- Why measurement endpoints determine light speed, not flight trajectory
- Gravitational light bending as drain-vector direction modification on the photon's direction vector
- The factor-of-2 GR correction from toroidal content at photon wavelength scale
- Photon frequency as spatial period of the pattern-of-coupling

**Key commitments:**
- c = 1 cell/tick is substrate arithmetic, not postulated
- Photons don't slow in gravity; they rotate direction vectors
- Lorentz invariance for photons is structural

### Section XI — Mass, Inertia, and the Higgs Mechanism

Specifies what mass is and how it arises.

**Content:**
- Mass as remainder drain: parent soliton applying negative remainder to children, directed toward center
- Inertia as resistance to direction change: Higgs pattern reconfiguration cost per update
- Higgs interactions as per-tick cost that reduces quiver extraction's net contribution to direction advance
- Why massless particles (photons, gluons in massless approximation) move at c
- Why massive particles move at less than c
- The pattern-not-substance commitment applied: m = F/a is operational; m has no substance, only pattern resistance
- The 99% pattern-binding-energy + 1% quark-content question resolved: both are Higgs-tick-cost at different scales
- The Higgs pattern as substrate-configuration providing the tick-cost mechanism
- Mass hierarchy arising from per-hierarchy-boundary modulus
- Connection between gravitational mass (drain source magnitude) and inertial mass (direction-change resistance)

**Key commitments:**
- Mass is inertia. Substance is not in the equation.
- Inertia comes from Higgs pattern reconfiguration cost.
- The proton's mass breakdown is not three quarks + flux tubes; it's all Higgs-tick-cost at different layers.

### Section XII — Gravitational Dynamics

Specifies how gravity works at the substrate level.

**Content:**
- Gravitational channel as drain from parent soliton to children
- Drain direction: radially toward parent's center
- Drain magnitude proportional to parent mass (Higgs-tick-cost of parent)
- Parent-child tax hierarchy: children experience only their immediate parent's drain
- Sibling effects at the same hierarchy level (minor compared to parent-child)
- Grandparent effects propagate through intermediate parent (tidal effects)
- 1/r² from spherical channel spreading over surface area
- GR corrections from toroidal sector at probe-scale resolution
- Mercury precession, factor-of-2 light bending, Shapiro delay as toroidal-content mechanisms
- Hill sphere as substrate-level hierarchy boundary
- No N-body problem: gravitational dynamics is strictly hierarchical
- Galactic rotation as toroidal flow, not orbital motion
- Stars at galactic rim as flow-carried within parent soliton frame
- The apparent-faster-than-light rim-star motion dissolved by correct coordinate system
- Dark matter as toroidal-flow Higgs response, not particles
- Dark energy as cosmic-scale quiver activity / universal soliton closure

**Key commitments:**
- Gravity is hierarchical. Each soliton experiences only its immediate parent's drain.
- Dark matter is not particles. It's toroidal-flow Higgs response.
- Dark energy is cosmic-scale substrate activity.
- The N-body problem is a Euclidean-coordinate artifact, not a substrate feature.

### Section XIII — Quantum Mechanics Derivation

Specifies how QM phenomena emerge from substrate structure.

**Content:**
- The measurement problem does not exist; substrate has one dynamics
- Observation is entanglement: observer becomes channel-shared with target
- "Collapse" as new channel-merger outcompeting prior entanglement
- Decoherence as environmental channel-merger dominating target's isolated coherence
- No privileged observer status: any soliton capable of channel-merger can observe
- Entanglement as channel-sharing: solitons merging channel substrate
- Entangled solitons as one pattern with multiple Euclidean handles
- Channel-sharing across arbitrary Euclidean separation (Bell non-locality as graph-local, Euclidean-non-local)
- No-signaling theorem as symmetric channel structure (no sender/receiver asymmetry)
- Monogamy as graph-edge combinatorics
- Multi-particle entanglement (GHZ, W, cluster states) as coordinated channel-sharing
- Single-particle interference via channel-agreement at termination events
- Double-slit: multi-path channel agreement without observer; single-path resolution with observer
- Quantum eraser: termination-context-determined resolution, not retrocausal
- Photons unobservable in flight; observation is termination
- Born rule from unit-graph round-trip closure:
  - Unit-sphere state space from substrate construction
  - Round-trip closure as only basis-independent positive-real extraction
  - Squared magnitude from counting two conversions (forward + conjugate)
  - Exponent counting matching MATH-11/PHYS-49 β² pattern
- Hilbert space as continuous-limit description of unit-adjacency graph
- Complex amplitudes from two-sector (spherical + toroidal) channel state combination
- Wave-particle duality dissolved into channel-agreement dynamics
- The Copenhagen/MWI/Bohmian/QBist debates as irrelevant details about the same substrate event

**Key commitments:**
- One dynamics, not two. Measurement is channel-merger.
- Born rule is derived, not postulated.
- Bell non-locality is graph-local, not spooky.
- Superposition, interference, measurement all reduce to channel arithmetic.

### Section XIV — Standard Model Reduction

Specifies how Standard Model structure arises from substrate.

**Content:**
- Fermion generation count = 3 from substrate channel structure
- Gauge group U(1) × SU(2) × SU(3) from channel type enumeration
- Lepton generation democracy (all db sums = 4/3) from channel closure
- Koide K = 2/3 from lepton channel-closure structure
- CKM matrix elements (V_us = 9/40, V_cb = 1/24) as integer channel ratios
- Gap ratio 38/27 from CD channel arithmetic
- Beta coefficients (b₂' = 13/6, b₃ = -20/3, etc.) as substrate channel-counting
- Higgs mechanism as per-tick tick-cost imposition on massive matter
- Mass hierarchy from per-hierarchy-boundary modulus (level-indexed family)
- Anomalous magnetic moments via dual-geometry decomposition
- Renormalization group running as substrate scale-dependent averaging
- Asymptotic freedom from channel-coupling scaling
- QCD confinement via toroidal gluon flux tubes (99% proton mass as structural toroidal content)
- Neutrino oscillation via weak-channel arithmetic with flavor-mixing
- CP violation as channel-state symmetry breaking
- The parallel-isomorphism commitment: SM and PCTRM produce identical observables from different primitives

**Key commitments:**
- SM structure is derivable from substrate channel enumeration.
- All SM predictions are preserved at measurement precision.
- The substrate provides mechanism where SM provides postulates.

### Section XV — Cosmology

Specifies how cosmological structure arises from substrate.

**Content:**
- The universal soliton as outermost hierarchy level
- The cosmic partition: Ω_DM + Ω_b + Ω_Λ = 1 as partition closure
- Ω_DM = π/12 as spherical sector fraction
- Ω_b = 13/264 as gauge integer fraction
- Ω_Λ = (251 - 22π)/264 as remainder from closure
- DM/baryon ratio 22π/13 as toroidal-flow prefactor × π
- The closure constant 251 and its role
- H₀ tension ratio 12/11 from transit-counting across hierarchy configurations
- Cosmic flatness as structural identity
- Microscopic-cosmic bridge: 22π/13 = |A₄| × (α/π)⁴ × 3 × (M_Z/m_e)²
- CMB spectrum from substrate early-universe channel dynamics
- BBN abundances from substrate nucleosynthesis channel arithmetic
- Dark matter halo structure as spherical channel sector at cosmic scale
- Galactic disk structure as toroidal channel sector at cosmic scale
- Dark energy as cosmic-scale quiver activity closure
- Cosmic horizon from substrate light-cone + integer cell count
- Gravitational wave propagation through quiver at c
- Primordial black hole dynamics via parent-soliton drain capacity
- Black holes as parent solitons with drain exceeding child-maintenance capacity
- Event horizons as drain-threshold boundaries
- Hawking radiation from boundary channel dynamics at drain threshold
- Black hole entropy from channel configuration counting at horizon
- Information in black holes as absorbed into parent pattern, released through Hawking radiation
- Kerr corrections from toroidal sector of rotating black holes

**Key commitments:**
- Cosmological parameters are substrate-structural, not fit.
- Dark matter and dark energy are substrate dynamics, not exotic content.
- Black holes are parent solitons with extreme drain; no geometric singularity.

### Section XVI — The Integer Alphabet and Transcendentals

Specifies the framework's prediction generator.

**Content:**
- The integer alphabet as framework's prediction mechanism
- Enumeration of primary integers: 2, 3, 4, 5, 6, 8, 11, 12, 13, 22, 251, 264
- Enumeration of secondary integers: 9, 24, 27, 38, 40, 43, 47, 48, 63, 91, 104, 115, 144, 169, 197, 211, 218, 313, 1015, 5184, 28259
- Structural integers: 299792458 (c_SI exact), generation count 3, gauge group dimensions {1, 2, 3}
- Transcendentals catalog:
  - π (angular measure)
  - β = π/4 (MATH-11 spherical L1/L2 conversion)
  - K(k) at specific moduli (MATH-12 toroidal period)
  - E(k) at specific moduli (MATH-12 toroidal circumference)
- Topology-specific moduli catalog:
  - k = 0 (spherical limit)
  - k₈₁ = 0.999994 (Laporta topology 81)
  - k₈₃ = 0.997130 (Laporta topology 83)
  - Per-hierarchy-boundary moduli (family pending specification)
- The alphabet expression production rule: all framework predictions must be expressible as combinations of integer alphabet with β and K(k)
- Exponent counting convention: β exponents count spherical conversions, K exponents count toroidal conversions
- Cross-derivation as the framework's validation method (PSLQ-replaced)

**Key commitments:**
- The alphabet is finite and enumerable.
- All framework predictions are expressible in the alphabet.
- Anything not alphabet-expressible is not a framework prediction.

### Section XVII — Dynamics and Update Rules

Specifies the per-tick update mechanism in detail.

**Content:**
- Per-tick update sequence:
  1. Quiver activity at every cell
  2. Channel throughput computation for each soliton
  3. Remainder accumulation from channels + quiver extraction
  4. Modulus crossing detection
  5. Direction vector update
  6. Soliton position update (one cell in direction vector)
- How multiple channels compose at a single soliton
- How Higgs tick-cost is applied before direction update
- How gravitational drain biases the direction update
- How entanglement-channel-merger propagates updates to shared endpoints
- How channel termination events are resolved
- How channel creation events are triggered
- How channel-agreement at multi-path configurations resolves
- The composition rule for direction vectors across multiple channel contributions
- Remainder conservation and redistribution during interactions
- The distinction between Planck-scale arithmetic (exact) and coarse-grained observable predictions (approximated from substrate arithmetic)

**Key commitments:**
- Updates are sequential per tick, not continuous.
- All observable dynamics emerge from this update loop.
- The substrate has one update rule applied uniformly.

---

## How this organization handles the full content

Every commitment from the program is placed in one of 17 sections:

- **Substrate primitives** (Sections I-VI): cells, ticks, adjacency, quiver, solitons, channels
- **Geometry** (Section VII): dual-geometry decomposition
- **Coordinate system** (Sections VIII-IX): hierarchical coordinates, Planck-scale locality
- **Mechanics** (Sections X-XII): photon propagation, mass/inertia, gravity
- **Quantum phenomena** (Section XIII): QM derivation
- **Physics reduction** (Sections XIV-XV): SM and cosmology
- **Predictive machinery** (Section XVI): integer alphabet
- **Dynamics** (Section XVII): per-tick update loop

## Key structural features of the spec

**Declarations, not arguments.** Each section states what PCTRM says, not why it might be right. The framework is committed; the spec documents the commitments.

**Dense but not exhaustive-proving.** Each section states the commitment plainly, names the mechanism, lists the consequences, and moves on. Cross-references between sections handle dependencies.

**No falsification content.** Kill switches, tests, precision targets — all live in PHYS-55 and its successors. The spec is the substrate. Testing is separate.

**Hierarchy as organizational principle.** The spec is structured the same way the substrate is: foundational primitives first, then increasingly emergent layers. Reading from Section I to Section XVII walks from Planck cells to cosmological structure.

**Cross-domain consistency.** Every section references the integer alphabet (Section XVI) as the prediction generator. Every hierarchy level uses the same coordinate system (Section VIII). Every interaction uses channels (Section VI). The spec maintains structural consistency throughout.

## Length estimate

Based on the content density and number of commitments per section: approximately 25,000-35,000 words total, with some sections (XIII on QM, XV on cosmology) being longer and some (II on cells/ticks, III on adjacency) being relatively compact.

Each section would have 1000-3000 words of substantive content plus possible diagrams and reference tables.

## Tables and diagrams

The spec needs several reference tables:

- **Table M1:** Channel type catalog with activation, direction, throughput, sectors, scale ranges
- **Table M2:** Integer alphabet with source and use-cases
- **Table M3:** Topology-specific modulus catalog
- **Table M4:** Hierarchy level enumeration with characteristic scales
- **Table M5:** Dual-geometry manifestations at each hierarchy level
- **Table M6:** Standard Model features with PCTRM mechanism for each
- **Table M7:** Cosmological parameters with substrate derivation
- **Table M8:** Per-tick update sequence

Diagrams needed (referenced but produced separately):

- Direction-conditional adjacency (cubic vs. unit-graph)
- Hierarchy nesting across seven levels
- Dual-geometry sectors at four scales
- Channel-sharing for entangled particles
- Unit-graph round-trip closure for Born rule
- Observation-as-entanglement three-panel merger
- Hierarchical coordinate system
- Black hole as parent soliton with extreme drain

## What this plan does not do

**It does not include falsification.** Kill switches, test programs, pre-registered predictions — these live in PHYS-55 and future test-program documents. The spec is what the framework claims; testing whether the framework is right is a separate layer.

**It does not include comparison with alternatives.** The spec doesn't defend itself against other frameworks. It states what PCTRM is.

**It does not include historical development.** Session-by-session evolution of the framework is in transcripts. The spec is the synthesized result.

**It does not include speculative extensions.** Items like "complex-amplitude derivation from toroidal phase" that the framework has gestured toward but not fully committed are handled at the commitment level — stated if committed, omitted if not.

**It does not hedge.** No "it is proposed that" or "one way to think about this" or "possibly." The framework has crossed the threshold where it states what it is and lets other documents test the claims.

## Writing approach

Each section opens with the commitment in one-to-three paragraphs. Then mechanism details. Then connections to other sections. Then commitments list at the end. Tables and figures referenced but not inline-reproduced in every section.

The tone follows PHYS-55's maximal/expansionist approach. The framework speaks plainly about what it is. The spec is the authoritative reference for "what does PCTRM claim?" — a reader can open the spec, find the relevant section, and get the answer.

## Ready to draft

If the plan is approved, I draft the full specification as PCTRM-1-Master-2026. Estimated output: ~25-35k words across 17 sections plus tables, produced in one coherent document.

Waiting for your review of this plan.
