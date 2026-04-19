# PHYS-54 Supplementary Tables

**Registry:** HOWL-PHYS-54-2026 (Supplementary Material)
**Purpose:** Full reference tables for PHYS-54 paper draft
**Companion:** PCTRM-1-2026 model specification, PHYS-54 paper plan
**Date:** April 19, 2026

---

## Table of Contents

- Table S1: Axiom Reference Guide
- Table S2: Core Vocabulary Glossary
- Table S3: Channel Type Specifications
- Table S4: Soliton Hierarchy with Characteristic Scales
- Table S5: Per-Tick Update Operations by Phase
- Table S6: Level 1 (Subatomic) Predictions and Targets
- Table S7: Level 2 (Atomic) Predictions and Targets
- Table S8: Level 3 (Nuclear) Predictions and Targets
- Table S9: Level 4 (Molecular/Solid-State) Predictions and Targets
- Table S10: Level 5 (Macroscopic/Gravitational) Predictions and Targets
- Table S11: Level 6 (Cosmological) Predictions and Targets
- Table S12: Existing RUM Predictions That PCTRM Must Reproduce
- Table S13: Kill Switch Summary Across All Levels
- Table S14: Open Theoretical Questions with Status and Priority
- Table S15: Worked Examples — Photon in Vacuum
- Table S16: Worked Examples — Electron in Hydrogen 1S State
- Table S17: Worked Examples — Moon in Earth Orbit
- Table S18: Worked Examples — Jumping Human
- Table S19: Worked Examples — Photon in Prism
- Table S20: Computational Complexity and Tractability by Level
- Table S21: Comparison to Other Discrete Substrate Programs
- Table S22: Free Parameters and Candidate Derivations
- Table S23: Isomorphism Map — PCTRM Primitives to SM Observables
- Table S24: Priority Order with Resource Estimates
- Table S25: Falsification Criteria with Precision Thresholds
- Table S26: What PCTRM Claims and Does Not Claim

---

## Table S1: Axiom Reference Guide

| # | Axiom | Statement | Implications |
|---|---|---|---|
| A1 | Discrete space | Universe composed of Planck cells with integer indices | No sub-cell positions; all spatial quantities are integer counts of cells |
| A2 | Discrete time | Universe advances in Planck ticks; state updates at each tick | No sub-tick events; all temporal quantities are integer counts of ticks |
| A3 | Direction-conditional adjacency | Each cell has neighbor at 1 Planck-distance in any direction; direction is continuous | No preferred lattice axes; isotropic propagation; no staircase artifacts |
| A4 | Discrete remainder budgeting | Each soliton has integer remainder counter tracking accumulated propagation budget | Motion requires accumulated budget; state transitions are discrete events |
| A5 | Modulus cost | Moving 1 Planck-cell costs 1 modulus of remainder | Universal threshold for discrete events; same modulus for same event type |
| A6 | Coherence tax | Solitons spend budget maintaining pattern against ambient patterns | Inertia is the tax rate; massless particles have zero tax |
| A7 | Channel-mediated remainder exchange | Solitons interact via discrete channels with specific directions and throughputs | All forces are channel operations; remainder is conserved across interacting solitons |

---

## Table S2: Core Vocabulary Glossary

| Term | Definition | Example |
|---|---|---|
| Soliton | Self-sustaining coherent pattern that persists across ticks | Electron, proton, atom, molecule, planet, galaxy |
| Cell | Discrete unit of space, Planck-sized | Position is integer index into cells |
| Tick | Discrete unit of time, Planck-duration | All state updates occur at ticks |
| Modulus | Integer threshold for discrete event | For Planck-cell motion: the budget required to advance 1 cell |
| Remainder | Accumulated budget toward next discrete event | When remainder ≥ modulus, event fires |
| Per-tick budget | Amount of remainder generated per tick for a soliton | Photon: full modulus; massive particle: less |
| Coherence tax | Fraction of per-tick budget consumed by pattern maintenance | Zero for photons; positive for Higgs-coupled particles |
| Channel | Discrete interaction pathway between solitons | Gravitational, EM, strong, weak, thermal, Higgs |
| Channel throughput | Remainder exchanged per tick through channel | Determined by channel strength and geometry |
| Running reading depth | Number of nested parent solitons a child is inside | Human on Earth surface: high depth; interstellar photon: low |
| Direction | Continuous unit vector indicating soliton's orientation | Not quantized; updated by channel interactions |
| Vector remainder | Sum of all per-tick remainder contributions | Determines direction of next discrete event |
| Ground state | Minimum-energy configuration for soliton in its parent | Electron in 1S, human at rest on ground, moon at stable orbit |
| Excited state | Above-ground configuration, returns to ground over time | Electron in 2S, human mid-jump, etc. |
| Boundary | Transition region between soliton's interior pattern and ambient | Nucleus boundary, atom boundary, Earth's atmosphere |
| Transit | Crossing a soliton boundary | Light transiting multiple nested boundaries |
| Interface | Shared abstract operations across all hierarchy levels | Interior/exterior reading, modulus/remainder, channels |
| Implementation | Level-specific details of how interface operations manifest | Electron's specific channel structure vs. galaxy's |

---

## Table S3: Channel Type Specifications

| Channel | Always Active | Active When | Direction | Throughput | Drains or Adds | Scale |
|---|---|---|---|---|---|---|
| Higgs coupling | Yes (for Yukawa-coupled particles) | Particle has mass | Isotropic (internal) | Yukawa coupling × per-tick budget | Drains (coherence tax) | All massive particles |
| Gravitational | Yes (between parent and child) | Child inside parent's field | Toward parent's center | 1/r² × channel density | Drains from non-center, adds to center | All hierarchy levels |
| Electromagnetic | Conditionally | Charged particles interacting | EM field gradient | Coulomb strength × charge | Direction of field | Charged particles |
| Strong | Conditionally | Color-charged particles close | Color gradient | Confinement strength | Bidirectional within hadrons | Sub-nucleon |
| Weak | Conditionally | Particle undergoing weak decay | Decay direction | Fermi constant × overlap | Drains (decay) | Sub-nuclear |
| Thermal | Conditionally | Soliton in thermal environment | Statistical | Temperature × Boltzmann | Bidirectional statistical | All levels |
| Tidal | Conditionally | Extended object in gradient field | Tidal gradient | Derivative of main force | Redistributes | Planetary, stellar |

---

## Table S4: Soliton Hierarchy with Characteristic Scales

| Level | Example | Scale (m) | Parent | Dominant Channels | Ground State |
|---|---|---|---|---|---|
| 12 | Observable universe | 10²⁷ | None | All at universal scale | Flat (Ω=1) |
| 11 | Galactic supercluster | 10²⁴ | Universe | Gravitational | Bound cluster |
| 10 | Galaxy cluster | 10²³ | Supercluster | Gravitational | Bound cluster |
| 9 | Galaxy | 10²¹ | Cluster | Gravitational + disk structure | Rotating disk |
| 8 | Stellar system | 10¹² | Galaxy | Gravitational | Stable orbits |
| 7 | Star | 10⁹ | Galaxy | Gravitational + fusion | Hydrostatic equilibrium |
| 6 | Planet | 10⁷ | Star | Gravitational + EM | Rotating body |
| 5 | Macroscopic object | 10⁻¹ | Planet | EM + gravitational | Bound structure |
| 4 | Molecule | 10⁻⁹ | Solid/liquid/gas | EM (chemical bonds) | Minimum energy configuration |
| 3 | Atom | 10⁻¹⁰ | Molecule | EM (electron shells) | Electron in lowest shell |
| 2 | Nucleus | 10⁻¹⁵ | Atom | Strong | Ground nuclear state |
| 1 | Nucleon | 10⁻¹⁵ | Nucleus | Strong (quark confinement) | Quark ground state |
| 0 | Quark/lepton | 10⁻¹⁸ | Universal vacuum | Higgs + gauge | Field configuration |

---

## Table S5: Per-Tick Update Operations by Phase

| Phase | Operation | Inputs | Output | Notes |
|---|---|---|---|---|
| 1 | Budget generation | Soliton type, Higgs coupling | Per-tick budget value | Fixed for each particle type |
| 2 | Coherence tax | Per-tick budget, Higgs coupling | Reduced budget available | Drains fraction for pattern maintenance |
| 3 | Channel enumeration | Soliton position, active interactions | List of active channels | Determined by nesting depth |
| 4 | Channel remainder exchange | Each channel's direction and throughput | Vector contribution per channel | Computed independently per channel |
| 5 | Vector sum | All channel contributions + budget | Total vector remainder | Vectorial addition |
| 6 | Modulus check | Accumulated remainder magnitude in each direction | Events fired or not | Compare to modulus threshold |
| 7 | State update | Events fired, current state | New position, new remainder | Cell advance, remainder decrement |
| 8 | Tick increment | All solitons updated | Universe advances 1 tick | All updates in parallel |

---

## Table S6: Level 1 (Subatomic) Predictions and Targets

| Observable | CODATA Value | Precision | PCTRM Target | Status |
|---|---|---|---|---|
| Electron mass | 0.51099895 MeV | 3×10⁻¹⁰ | From Higgs tax arithmetic | Not yet derived |
| Muon mass | 105.6583745 MeV | 2.4×10⁻⁸ | From Higgs tax × 207 factor | Not yet derived |
| Tau mass | 1776.86 MeV | 8×10⁻⁵ | From Higgs tax × scale ratio | Not yet derived |
| m_μ/m_e ratio | 206.7683 | 2×10⁻⁸ | Integer from channel structure? | Open |
| m_τ/m_e ratio | 3477.15 | 4×10⁻⁵ | Integer from channel structure? | Open |
| α_EM (low E) | 1/137.036 | 1.5×10⁻¹⁰ | From channel count + β structure | RUM has derivation |
| α_s (at Z) | 0.1179 | 8×10⁻⁴ | From channel count at Z scale | Partial |
| Electron g-2 (a_e) | 1.1596521 × 10⁻³ | 3×10⁻¹¹ | From channel structure at loop 4 | RUM has work |
| Muon g-2 (a_μ) | 1.1659208 × 10⁻³ | 2×10⁻⁹ | From channel structure at loop 4 | RUM has work |
| sin²θ_W | 0.23122 | 4×10⁻⁴ | From electroweak channel ratios | Open |
| V_us | 0.22501 | 4×10⁻⁴ | 9/40 from integer channel structure | RUM: 44 ppm match |
| V_cb | 0.0412 | 3×10⁻³ | 1/24 from integer channel structure | RUM: 0.37% match |

---

## Table S7: Level 2 (Atomic) Predictions and Targets

| Observable | Measured Value | Precision | PCTRM Target | Kill Threshold |
|---|---|---|---|---|
| H 1S → 2S transition | 2.4661 × 10¹⁵ Hz | 10⁻¹⁵ | Modulus arithmetic at atomic scale | 10⁻⁹ |
| H Rydberg constant | 1.0974 × 10⁷ m⁻¹ | 1.9×10⁻¹² | From m_e, α, ℏ via substrate | 10⁻⁹ |
| Lyman-α wavelength | 1215.67 Å | 10⁻⁸ | Derived from 1S-2S modulus | 10⁻⁸ |
| H Lamb shift | 1057.84 MHz | 10⁻⁵ | From vacuum channel structure | 10⁻⁴ |
| H fine structure | 10.97 GHz | 10⁻⁶ | From l,m channel variations | 10⁻⁴ |
| H hyperfine (21 cm) | 1420.406 MHz | 10⁻¹² | From proton-electron spin channel | 10⁻⁶ |
| He 1¹S₀ ground | -79.0 eV | 10⁻⁶ | Two-electron channel arithmetic | 10⁻⁴ |
| Li ionization energy | 5.392 eV | 10⁻⁵ | Three-electron channel structure | 10⁻⁴ |
| Bohr radius a₀ | 5.292 × 10⁻¹¹ m | 1.5×10⁻¹⁰ | Closure radius from integer arithmetic | 10⁻⁸ |

---

## Table S8: Level 3 (Nuclear) Predictions and Targets

| Observable | Measured Value | Precision | PCTRM Target | Kill Threshold |
|---|---|---|---|---|
| Proton mass | 938.272 MeV | 10⁻¹⁰ | Strong channel arithmetic at nucleon scale | 10⁻³ |
| Neutron mass | 939.565 MeV | 10⁻¹⁰ | Strong + weak channels in nucleon | 10⁻³ |
| m_p - m_n difference | 1.293 MeV | 10⁻⁷ | Weak channel contribution | 10⁻³ |
| Deuteron binding energy | 2.22457 MeV | 10⁻⁵ | Two-nucleon strong channel | 10⁻² |
| Helium-4 binding energy | 28.295 MeV | 10⁻⁴ | Four-nucleon channel arithmetic | 10⁻² |
| Iron-56 binding/nucleon | 8.79 MeV | 10⁻³ | Nuclear shell + channel saturation | 10⁻² |
| Neutron half-life | 878.4 s | 1.4×10⁻³ | Weak decay channel modulus | 10⁻² |
| Pion mass | 139.57 MeV | 10⁻⁵ | Quark-antiquark channel state | 10⁻² |
| Proton charge radius | 0.8414 fm | 10⁻³ | From proton boundary channel | 10⁻² |
| Nuclear magnetic moments | Various | 10⁻⁷ to 10⁻⁴ | From quark spin channel arithmetic | 10⁻² |
| Lambda_QCD | 210 MeV | 5×10⁻² | From integer + β arithmetic | RUM: in progress |

---

## Table S9: Level 4 (Molecular/Solid-State) Predictions and Targets

| Observable | Measured Value | Precision | PCTRM Target | Kill Threshold |
|---|---|---|---|---|
| H₂ bond length | 0.7414 Å | 10⁻⁴ | Two-atom channel closure | 10⁻² |
| H₂ bond energy | 4.478 eV | 10⁻⁴ | EM channel binding arithmetic | 10⁻² |
| H₂O bond angle | 104.5° | 10⁻³ | Multi-atom channel geometry | 10⁻² |
| H₂O bond length | 0.9584 Å | 10⁻⁴ | O-H channel closure | 10⁻² |
| NaCl lattice constant | 5.64 Å | 10⁻⁴ | Ionic channel periodicity | 10⁻² |
| Diamond lattice constant | 3.567 Å | 10⁻⁴ | Covalent channel periodicity | 10⁻² |
| Diamond bond energy | 3.67 eV/bond | 10⁻³ | sp³ channel strength | 10⁻² |
| Silicon bandgap | 1.12 eV | 10⁻³ | Band structure from channel arithmetic | 10⁻¹ |
| Water heat capacity | 4.186 J/g·K | 10⁻⁴ | Statistical channel thermodynamics | 10⁻¹ |
| Ice density | 0.917 g/cm³ | 10⁻³ | Crystal channel arithmetic | 10⁻² |

---

## Table S10: Level 5 (Macroscopic/Gravitational) Predictions and Targets

| Observable | Measured Value | Precision | PCTRM Target | Kill Threshold |
|---|---|---|---|---|
| g at Earth surface | 9.81 m/s² | 10⁻⁴ | Gravitational channel sum at depth | 10⁻² |
| Kepler third law | T² ∝ a³ | Exact | Orbital balance from channel arithmetic | Deviation at any scale |
| Mercury perihelion precession | 43 arcsec/century | 10⁻² | Higher-order channel corrections | 10⁻¹ |
| Light bending at Sun limb | 1.75 arcsec | 10⁻³ | Photon direction update in channels | 10⁻² |
| Shapiro delay (Venus radar) | 200 μs | 10⁻² | Photon tick count in field | 10⁻¹ |
| GPS time dilation | 38 μs/day | 10⁻⁶ | Budget allocation with depth | 10⁻⁴ |
| Gravitational redshift (Pound-Rebka) | 2.5 × 10⁻¹⁵ | 10⁻² | Photon budget change with potential | 10⁻¹ |
| Earth-Moon recession | 3.8 cm/year | 10⁻² | Tidal channel budget exchange | 10⁻¹ |
| Binary pulsar orbital decay (PSR B1913+16) | -2.4 × 10⁻¹² s/s | 10⁻³ | GW emission from channel oscillation | 10⁻² |
| LIGO GW150914 waveform | Measured chirp | 10⁻² | Merger dynamics from channels | 10⁻¹ |
| Frame dragging (Gravity Probe B) | 37 mas/year | 2×10⁻¹ | Rotating source channel twist | 10⁻¹ |

---

## Table S11: Level 6 (Cosmological) Predictions and Targets

| Observable | Measured Value | Precision | PCTRM Target | Kill Threshold |
|---|---|---|---|---|
| Ω_DM | 0.261 ± 0.002 | 10⁻² | π/12 from universal soliton partition | RUM: 0.4σ |
| Ω_baryon | 0.0490 ± 0.0004 | 10⁻² | 13/264 from gauge integer structure | RUM: 0.6σ |
| Ω_Λ | 0.689 ± 0.004 | 10⁻³ | (251-22π)/264 from closure | RUM: 85 ppm |
| Ω_total (flatness) | 1.000 ± 0.002 | 10⁻³ | Exactly 1 from inside soliton | Must be exact |
| CMB temperature | 2.7255 K | 10⁻⁴ | From universal soliton state | 10⁻² |
| H₀ (CMB) | 67.4 km/s/Mpc | 7×10⁻³ | CMB transit channel count | 10⁻² |
| H₀ (local) | 73.0 km/s/Mpc | 1.4×10⁻² | Local transit channel count | 10⁻² |
| H₀ tension ratio | 12/11 | 5×10⁻³ | Transit-count ratio | 10⁻² |
| DM/baryon ratio | 5.32 | 10⁻³ | (22/13) × 4β | RUM: 725 ppm |
| CMB acoustic peak positions | Specific values | 10⁻³ | From channel structure at recombination | 10⁻² |
| Primordial helium fraction Y_p | 0.2453 | 10⁻³ | BBN from substrate nuclear rates | 10⁻² |
| Baryon-to-photon η | 6.1 × 10⁻¹⁰ | 10⁻² | From universal soliton counts | 10⁻¹ |

---

## Table S12: Existing RUM Predictions That PCTRM Must Reproduce

| Prediction | RUM Paper | Measured Match | PCTRM Reproduction Requirement |
|---|---|---|---|
| Ω_DM = π/12 | MATH-11, PHYS-48 | 0.4σ | Must derive π/12 from substrate |
| Ω_b = 13/264 | MATH-11, PHYS-48 | 0.6σ | Must derive 13/264 from integer counts |
| Ω_Λ = (251-22π)/264 | MATH-11, PHYS-48 | 85 ppm | Must derive from closure at universal level |
| DM/baryon = 22π/13 | PHYS-48 | 725 ppm | Must derive from cosmic channel arithmetic |
| Koide K = 2/3 | PHYS-50 | 9.2 ppm | Must derive from lepton channel closure |
| Σ triplet K = 1/3 | PHYS-53 | 1.9 ppm | Must derive from hadron channel closure |
| V_us = 9/40 | PHYS-53 | 44 ppm | Must derive from CKM channel structure |
| V_cb = 1/24 | PHYS-53 | 0.37% | Must derive from CKM channel structure |
| H₀ ratio = 12/11 | PHYS-48 | 0.67% | Must derive from transit-count ratio |
| Bridge formula 22π/13 = \|A₄\|·(α/π)⁴·3·(M_Z/m_e)² | PHYS-53 | 300 ppm | Must reproduce as substrate-derived identity |
| Proton lattice factor C = 6β | MATH-11 | 0.02σ | Must derive from nucleon channel arithmetic |
| String tension σ^(1/2)/Λ = 2π/3 | MATH-11 | 0.3% | Must derive from QCD channel structure |
| Laporta constants β⁰ classification | MATH-12 | 4925 digits | Must derive from toroidal channel structure |

---

## Table S13: Kill Switch Summary Across All Levels

| # | Level | Observable | Required Precision | Kill Condition | Current Status |
|---|---|---|---|---|---|
| K1 | 1 | m_e from Higgs tax | 10⁻³ | Cannot derive at 1% | Not yet attempted |
| K2 | 1 | m_μ/m_e ratio | 10⁻³ | Cannot reproduce 207 structurally | Open |
| K3 | 1 | α_EM at low energy | 10⁻⁶ | Cannot derive from channel count | Partial (RUM) |
| K4 | 1 | a_e anomalous moment | 10⁻⁹ | Cannot derive from loop-4 toroidal | Partial (RUM) |
| K5 | 2 | H 1S-2S transition | 10⁻⁹ | Cannot reproduce from modulus arithmetic | Not yet attempted |
| K6 | 2 | Lamb shift | 10⁻⁴ | Cannot derive from vacuum channel | Not yet attempted |
| K7 | 3 | Deuteron binding | 10⁻² | Cannot derive from strong channel | Not yet attempted |
| K8 | 3 | Neutron half-life | 10⁻² | Cannot derive from weak channel modulus | Not yet attempted |
| K9 | 4 | H₂O bond angle | 10⁻² | Cannot derive from multi-atom channels | Not yet attempted |
| K10 | 5 | Newtonian 1/r² | Exact (to measurement) | 1/r² not derivable from channel count | Priority test |
| K11 | 5 | Mercury precession | 10⁻¹ | GR corrections not reproducible | Priority test |
| K12 | 5 | Lorentz invariance | Exact (current tests) | Violation detected at any scale | Must be exact |
| K13 | 5 | GW emission rate | 10⁻² | Cannot match binary pulsar | Priority test |
| K14 | 6 | Ω_Λ reproduction | 85 ppm | Cannot derive (251-22π)/264 | Priority test |
| K15 | 6 | CMB spectrum | 10⁻² | Cannot derive from universal soliton | Open |
| K16 | All | QM phenomena | Standard | Cannot extend to complex amplitudes | Major gap |
| K17 | All | RUM predictions | Original precisions | PCTRM inconsistent with RUM | Framework critical |

---

## Table S14: Open Theoretical Questions with Status and Priority

| # | Question | Status | Priority | Required For |
|---|---|---|---|---|
| Q1 | Value of propagation modulus M | Unfixed, free parameter | Highest | All quantitative predictions |
| Q2 | Lorentz recovery from 4-budget norm | Gesture only | Highest | Level 5, 6 all tests |
| Q3 | QM extension via complex remainder | Unspecified mechanism | High | Level 1, 2 all tests |
| Q4 | 1/r² from spherical channel spreading | Intuition only | Highest | Level 5 all tests |
| Q5 | GR corrections from channel gradients | Not derived | High | Level 5 GR tests |
| Q6 | Emergence of QFT at continuum limit | Not addressed | Medium | Connection to SM field theory |
| Q7 | Thermodynamics from channel statistics | Not developed | Medium | Level 4+ statistical predictions |
| Q8 | Why specific integer alphabet {8,3,11,13,22,264} | Not derived from substrate | Medium | Connection to RUM |
| Q9 | Why three generations | Empirical input | Low | Unknown (likely substrate fact) |
| Q10 | How Higgs coupling determines per-tick budget | Structural only | High | Level 1 particle masses |
| Q11 | Whether modulus is universal or level-specific | Open | High | Consistency across levels |
| Q12 | Entanglement across channel network | Unspecified | Medium | Level 2+ QM tests |
| Q13 | Wavefunction collapse mechanism | Unspecified | Medium | Level 2 measurement |
| Q14 | Born rule from discrete amplitudes | Unspecified | Medium | Level 2 QM probabilities |
| Q15 | How direction-continuous maps to discrete cell advance | Mechanism needed | High | Level 5 fine-grained motion |
| Q16 | Black hole horizons from channel density | Gesture only | Low | Level 5 extreme gravity |
| Q17 | Inflation mechanism in PCTRM | Not addressed | Low | Level 6 early universe |
| Q18 | Discreteness signatures at Planck scale | Unknown | Low | Eventual Planck-scale tests |

---

## Table S15: Worked Example — Photon in Vacuum

| Tick | Position | Budget | Coherence Tax | Active Channels | Vector Remainder | Modulus Crossed? | Event |
|---|---|---|---|---|---|---|---|
| 0 | (0,0,0) | M (full modulus) | 0 (massless) | None (vacuum) | (M, 0, 0) along v̂ | Yes | Move to (1,0,0) |
| 1 | (1,0,0) | M | 0 | None | (M, 0, 0) | Yes | Move to (2,0,0) |
| 2 | (2,0,0) | M | 0 | None | (M, 0, 0) | Yes | Move to (3,0,0) |
| ... | ... | ... | ... | ... | ... | ... | ... |
| N | (N,0,0) | M | 0 | None | (M, 0, 0) | Yes | Move to (N+1,0,0) |

**Result:** Photon advances 1 cell per tick in direction v̂ = (1,0,0). Speed = 1 cell/tick = c. No direction change (no active channels in vacuum).

---

## Table S16: Worked Example — Electron in Hydrogen 1S State

| Parameter | Value | Source |
|---|---|---|
| Electron per-tick budget | B_e < M (Higgs tax applied) | Standard electron budget |
| Active channels | Proton EM (Coulomb attraction) | Charged particle in EM field |
| Closure requirement | Total remainder accumulated per orbit = 1 × modulus | Shell quantization |
| Orbital radius | Bohr radius a₀ = 0.529 Å | Integer closure at n=1 |
| Shell energy | -13.6 eV | Binding energy from channel structure |
| Transition 1S→2S | Requires 10.2 eV photon absorption | Modulus for state transition |

**Mechanism:** Electron moves tangentially in closed orbit. Proton EM channel provides radial attraction each tick. Tangential momentum and radial pull balance; orbit closes when integrated remainder per orbit equals integer modulus. Shell n=1 is smallest closure; higher n require more accumulated remainder per orbit.

**Transition:** External photon delivers 10.2 eV worth of remainder to electron's internal state counter. When accumulated internal remainder crosses 1S→2S modulus (10.2 eV), electron discretely transitions to 2S state (different closure condition, larger orbit).

---

## Table S17: Worked Example — Moon in Earth Orbit

| Parameter | Value | PCTRM Reading |
|---|---|---|
| Moon mass | 7.35 × 10²² kg | Determines Moon's per-tick budget (with Higgs tax) |
| Orbital radius | 384,400 km | Integer cells at this distance from Earth's center |
| Orbital period | 27.3 days | Ticks required for full orbit closure |
| Orbital speed | 1.022 km/s | v/c = per-tick motion budget / modulus |
| Earth's pull channel | Gravitational | Per-tick negative remainder toward center |
| Pull magnitude | GM_Earth/r² | Channel throughput at Moon's depth |
| Tidal channel | Earth-Moon coupling | Budget exchange, Moon recession 3.8 cm/yr |

**Mechanism (simplified):** 

Each tick:
1. Moon's per-tick budget contributes to tangential direction
2. Earth's gravitational channel applies negative remainder toward Earth's center
3. Vector sum rotates Moon's direction slightly toward center
4. When motion-direction remainder crosses modulus, Moon advances 1 cell in current direction
5. Next tick: direction has rotated, new cell is slightly different angle

Over many ticks, the rotation integrates to 2π per orbital period. Orbit closes.

**Tidal budget exchange:** Small amount of Earth's rotational budget transfers to Moon's orbital budget each tick through tidal coupling channel. Over geological time, Moon gains orbital budget (recedes) and Earth loses rotational budget (day lengthens).

---

## Table S18: Worked Example — Jumping Human

| Phase | Duration | PCTRM Operation |
|---|---|---|
| At rest on ground | Indefinite | Gravity applies negative remainder; ground contact applies equal positive remainder; net zero |
| Takeoff | ~0.1 s | Internal budget converts to upward motion budget; legs spend chemical energy (internal channel) |
| Ascent | ~0.3 s | Gravity applies negative remainder downward each tick; upward motion budget decreases |
| Apex | Instantaneous | Upward motion budget = 0; gravity still applying negative remainder |
| Descent | ~0.4 s | Accumulated downward remainder (from gravity) produces downward motion; speed increases with each tick |
| Landing | ~0.05 s | Ground contact applies upward remainder; absorbs downward motion budget; converts to internal (heat) |
| Back at rest | Steady | Net zero again |

**Key reading:** The human is always "trying to return to ground state." Excess upward budget (from jump) is drained by gravitational channel over time. Return is inevitable because the channel is always active and pulls toward ground state. "Excited states do not last" is the structural description.

---

## Table S19: Worked Example — Photon in Prism

| Phase | PCTRM Operation | Direction Change |
|---|---|---|
| Before prism | Full modulus budget, no active channels, direction constant | None |
| Entering prism | Medium's EM channel structure couples to photon | Direction updates by refraction angle |
| Inside prism | Photon advances 1 cell per tick in new direction; medium's channel maintains modified direction | Constant (but different from vacuum direction) |
| Exiting prism | Medium's channel releases; photon direction updates again (second refraction) | Returns to vacuum-like direction but offset |
| After prism | Full modulus budget, no channels, direction constant | None (but different position than if no prism) |

**Key reading:** Refraction is not "light slowing down" in PCTRM — light is always 1 cell per tick. Refraction is direction change imposed by the medium's channel structure. Different wavelengths couple differently to the medium, producing different direction changes (chromatic dispersion, rainbow).

**Full-mesh topology advantage:** The photon's "new direction" inside the prism is any direction on the unit sphere, not a discrete set of lattice angles. Continuous refraction angles are natural in the topology.

---

## Table S20: Computational Complexity and Tractability by Level

| Level | Scale | Ticks per Second of Physics | Cells per Cubic Meter | Direct Simulation? | Approximation Required |
|---|---|---|---|---|---|
| 1 (Subatomic) | 10⁻¹⁸ m | 10⁴⁴ | 10⁵⁴ | Infeasible | Coarse-grain to many Planck lengths |
| 2 (Atomic) | 10⁻¹⁰ m | 10⁴⁴ | 10²⁵ | Infeasible | Use atomic-scale effective moduli |
| 3 (Nuclear) | 10⁻¹⁵ m | 10⁴⁴ | 10⁴⁵ | Infeasible | Use nucleon-scale effective moduli |
| 4 (Molecular) | 10⁻⁹ m | 10⁴⁴ | 10²⁷ | Infeasible | Use molecular-scale effective moduli |
| 5 (Macroscopic) | 10⁻¹ m | 10⁴⁴ | 10¹ | Infeasible in full | Continuum approximation with discreteness preserved |
| 6 (Cosmological) | 10²⁶ m | 10⁴⁴ | Diluted | Infeasible in full | Statistical/effective computation |

**Conclusion:** Direct Planck-resolution simulation is computationally impossible for any physical system at any level. PCTRM testing must use effective moduli and effective channels at each level's characteristic scale. The substrate claim is that these effective quantities emerge from the Planck-level dynamics; the test is whether the effective dynamics match observations.

**Tractable approach:** Build simulation at level-appropriate scales. Level 1: single-particle effective channels. Level 2: atomic-scale effective modulus for shell transitions. Level 5: continuum dynamics with PCTRM corrections. Etc.

---

## Table S21: Comparison to Other Discrete Substrate Programs

| Program | Primary Commitment | Similarity to PCTRM | Difference from PCTRM |
|---|---|---|---|
| Wolfram hypergraph physics | Discrete graph updated by local rewriting | Graph structure, discrete evolution | No modulus/remainder; no direction-conditional adjacency; no soliton hierarchy |
| Loop quantum gravity | Discrete spacetime via spin networks | Discrete quantum geometry | Focuses on quantum gravity only; no substrate for SM; different primitives |
| Causal dynamical triangulations | Discrete spacetime triangulation | Discrete geometric primitives | Continuum limit focus; no explicit channels or hierarchy |
| Causal sets | Spacetime as partial order of events | Discrete events, causality | Focuses on causality; no direction-conditional topology |
| Spin networks | Discrete angular momentum states | Quantized quantities | No propagation mechanism; no hierarchy |
| Digital physics (Fredkin, Wolfram) | Universe as computation | Discrete computational substrate | No specific mechanism linking to SM observables |
| PCTRM (this work) | Planck cells + ticks + direction-conditional adjacency + modulus/remainder + channels + soliton hierarchy | - | Distinctive: direction as continuous parameter in discrete position space; modulus/remainder as propagation budget; interface/implementation hierarchy |

---

## Table S22: Free Parameters and Candidate Derivations

| Parameter | Current Status | Candidate Derivations |
|---|---|---|
| Propagation modulus M | Free | (a) From RUM integer alphabet {8,3,11,13,22,264}; (b) From Planck scale ratios; (c) Universal vs. level-specific |
| Per-tick budget of each particle | Free (set by Higgs coupling) | From Yukawa couplings; from integer-plus-β expressions |
| Channel throughput per type | Free | From coupling constants (α, α_s, G_F, G_N) in integer-plus-β form |
| Coherence tax rate per particle | Free (equals mass) | From Higgs mechanism in substrate |
| Boundary count per hierarchy level | Free | From soliton structure (PHYS-1 Table J has 12) |
| Channel count at each nesting depth | Free | From integer alphabet structure |
| Direction continuity resolution | Open question | Either continuous to arbitrary precision or has minimum resolution |

---

## Table S23: Isomorphism Map — PCTRM Primitives to SM Observables

| PCTRM Primitive | SM Observable | Mapping Operation |
|---|---|---|
| Per-tick budget | Particle momentum magnitude | p = (budget) × (unit conversion) |
| Direction | Particle momentum direction | v̂ = direction of remainder accumulation |
| Modulus | Planck-scale action quantum | h or ℏ in appropriate convention |
| Coherence tax | Rest mass | m = f(Higgs coupling) |
| Channel count | Coupling constant | α_EM, α_s, etc. emerge from channel density |
| Nesting depth | Gravitational potential | Φ = ∑ depth contributions |
| Vector remainder | Total force | F = d(vector remainder)/d(tick) in continuum limit |
| Modulus crossing event | Discrete state transition | Photon emission, shell jump, decay |
| Soliton | Particle/composite/field configuration | Mapped per hierarchy level |
| Running reading depth | Field potential at location | Computed from hierarchy position |
| Parent-child channel | Gravitational/binding interaction | Channel structure encodes force |
| Ground state | Lowest energy state | Minimum coherence tax configuration |

**Key claim:** Every SM observable has a PCTRM primitive (or combination) that produces it. Every PCTRM primitive has an SM observable (or derived quantity) it corresponds to. The isomorphism is explicit, not metaphorical.

---

## Table S24: Priority Order with Resource Estimates

| Priority | Level | Test | Computational Cost | Development Time | Falsifiability Power |
|---|---|---|---|---|---|
| 1 | 5 | Two-body orbital (Earth-Moon) | ~1 CPU hour | 2-4 weeks | High (Kepler laws) |
| 2 | 5 | Mercury precession | ~1 CPU hour | 2-4 weeks | High (GR correction) |
| 3 | 6 | Ω_Λ reproduction | ~1 CPU day | 4-8 weeks | Highest (RUM consistency) |
| 4 | 2 | H 1S-2S transition | ~1 CPU day | 4-8 weeks | Highest (CODATA precision) |
| 5 | 1 | m_e from Higgs tax | ~1 CPU day | 4-8 weeks | Highest (CODATA precision) |
| 6 | 5 | Lorentz invariance check | ~1 CPU hour | 2-4 weeks | Critical (foundational) |
| 7 | 3 | Deuteron binding | ~1 CPU week | 4-12 weeks | High (nuclear physics) |
| 8 | 2 | Lamb shift | ~1 CPU week | 4-12 weeks | High (QED test) |
| 9 | 5 | Light bending at Sun | ~1 CPU day | 4-8 weeks | High (GR test) |
| 10 | 6 | CMB acoustic peaks | ~1 CPU month | 12-24 weeks | High (cosmology) |
| 11 | 4 | H₂O structure | ~1 CPU week | 4-12 weeks | Medium (chemistry) |
| 12 | 5 | Binary pulsar decay | ~1 CPU week | 8-16 weeks | High (GW emission) |

**Bottleneck identification:** Highest priority tests (1, 2, 6) are tractable with modest compute. They should be executed first. Tests that require QM extension (Priority 4, 5, 8) may be delayed pending resolution of Q3 (QM extension mechanism). Tests requiring full GR reproduction (Priority 2, 9, 12) may be delayed pending resolution of Q5 (GR corrections from channel gradients).

---

## Table S25: Falsification Criteria with Precision Thresholds

| F# | Criterion | Required Precision | Measurement Source | Implication of Failure |
|---|---|---|---|---|
| F1 | m_e, m_μ, m_τ derivable | 10⁻³ | CODATA | Higgs-tax mechanism wrong |
| F2 | H 1S-2S transition | 10⁻⁹ | Atomic physics | Atomic channel arithmetic wrong |
| F3 | Deuteron binding | 10⁻² | Nuclear physics | Strong channel wrong |
| F4 | Mercury precession + Earth-Moon recession | 10⁻¹ | Observation | Gravitational channel incomplete |
| F5 | Ω_Λ = (251-22π)/264 | 85 ppm | Planck | PCTRM inconsistent with RUM |
| F6 | Lorentz invariance exact | Current limits (~10⁻¹⁹) | High-energy physics | Direction-conditional topology inadequate |
| F7 | QM extension via complex remainder | Standard QM predictions | Quantum experiments | Model limited to classical physics |
| F8 | 1/r² gravity derivation | Exact (at measurement precision) | Gravitational tests | Channel spreading wrong |
| F9 | Koide K = 2/3 | 9.2 ppm | Lepton masses | Lepton channel structure wrong |
| F10 | V_us = 9/40 | 44 ppm | CKM measurements | CKM channel structure wrong |
| F11 | Shell quantization from closure | Standard spectral | Atomic spectra | Closure mechanism wrong |
| F12 | Budget conservation | Exact | All interactions | Remainder exchange not conservation |
| F13 | Modulus universality | Consistency | Cross-level tests | Moduli incompatible across scales |
| F14 | No preferred frame | Exact (at measurement) | Lorentz tests | Topology produces preferred frame |
| F15 | GR weak-field limit | 10⁻¹ | Solar system | PCTRM fails to reproduce GR |
| F16 | Thermodynamic emergence | Standard | Statistical mechanics | No substrate thermodynamics |

---

## Table S26: What PCTRM Claims and Does Not Claim

| Claim Category | Specific Claim | Status |
|---|---|---|
| Ontological | Universe is discrete at Planck scale | Commitment; not proven |
| Ontological | Space has direction-conditional adjacency | Commitment; not proven |
| Ontological | Integers are the substrate's native arithmetic | Commitment; not proven |
| Operational | PCTRM reproduces SM at macroscopic scales | Must be shown via falsification program |
| Operational | PCTRM reproduces GR in classical gravity limit | Must be shown; mechanism gestured |
| Operational | PCTRM reproduces QM | Must be shown; mechanism not yet specified |
| Operational | PCTRM reproduces RUM's existing predictions | Must be shown; substrate-level derivation needed |
| Not claimed | PCTRM replaces SM | Denied; PCTRM is substrate for SM |
| Not claimed | PCTRM is only viable substrate | Denied; one candidate among possible substrates |
| Not claimed | Results of falsification program are known | Denied; program specifies tests, not outcomes |
| Not claimed | All mechanisms are fully worked out | Denied; gaps explicitly listed (Table S14) |
| Not claimed | PCTRM has been computationally verified | Denied; tests pending (Table S24 priority list) |
| Not claimed | Lorentz invariance is proven in PCTRM | Denied; is priority test (F6, Q2) |
| Not claimed | QM extension is proven in PCTRM | Denied; is major gap (Q3, F7) |
| Not claimed | Specific modulus value is known | Denied; is open parameter (Q1) |
| Not claimed | PCTRM explains all physics | Denied; levels not yet all tested |

---

**END SUPPLEMENTARY TABLES**

**Summary:** 26 tables covering the full PCTRM specification, the falsification program across six hierarchy levels, worked examples at different scales, computational feasibility, comparison to other discrete substrate programs, and explicit claims boundary.

**Usage for PHYS-54 drafting:** These tables provide the reference material for writing the full paper. Each section of the paper can pull the relevant tables for its content. The tables are designed to be internally consistent, mutually complementary, and complete enough that the paper author (whether a future Claude instance or another researcher) has everything needed to draft a comprehensive, maximally expansive PHYS-54.

**Notes for the paper author:**
- Table S1-S5 are for the vocabulary and mechanism sections
- Table S6-S11 are for the predictions sections at each level
- Table S12-S13 are for the connection to RUM and falsification
- Table S14-S15-S19 are for honesty about gaps and worked examples
- Table S20-S21 are for feasibility and comparison to other programs
- Table S22-S26 are for theoretical framework structure and claim boundaries

The paper should reference these tables explicitly when making specific claims. The tables are designed so that the PHYS-54 draft can be self-contained while also referencing the fuller model specification in PCTRM-1-2026.
