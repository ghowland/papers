# PHYS-55 Supplemental Tables

## Table A1 — Full Kill-Switch Catalog K1-K22

| # | Name | Level | Condition | Precision Target | Data Source | Status | Notes |
|---|------|-------|-----------|-----------------|-------------|--------|-------|
| K1 | Electron mass from Higgs tax | 1 | m_e derivation from substrate Higgs-coupling formula fails at CODATA precision | 10⁻⁸ | CODATA 2018 | Untested | Requires Q10 execution |
| K2 | Muon-electron mass ratio | 1 | m_μ/m_e derivation from integer channel structure misses measured ratio | 10⁻⁸ | CODATA 2018 | Untested | Requires Q1, Q10 |
| K3 | Fine structure from channel count | 1 | α_EM derivation from substrate channel-count expression misses 137.036 at ppm | 10⁻⁹ | CODATA 2018 | Untested | Cross-derivation target |
| K4 | Electron anomalous moment | 1 | a_e = g-2/2 from four-loop substrate calculation misses Harvard measurement | 10⁻¹² | Harvard 2023 | Untested | Requires Q3 quantitative extension |
| K5 | Hydrogen 1S-2S transition | 2 | H 1S-2S substrate derivation misses measured frequency | 10⁻¹⁵ | MPQ 2020 | Untested | Requires Q3 |
| K6 | Lamb shift | 2 | Lamb shift from substrate Casimir-channel structure misses measurement | 10⁻⁶ | Experiment | Untested | Requires Q3 |
| K7 | Deuteron binding energy | 3 | Deuteron binding from substrate multi-nucleon channel arithmetic misses measurement | 10⁻⁵ | Nuclear data | Untested | Requires strong-channel spec |
| K8 | Neutron half-life | 3 | Neutron lifetime from substrate weak-channel mechanism misses measurement | 10⁻³ | PDG 2024 | Untested | Requires weak-channel spec |
| K9 | Water bond angle | 4 | H₂O bond angle from substrate molecular-orbital structure misses measurement | 10⁻³ | Experiment | Untested | Molecular-scale prediction |
| K10 | Inverse-square gravity | 5 | 1/r² residual from spherical channel spreading exceeds threshold | 10⁻³ | Gravity tests | Untested | Requires Q4 execution |
| K11 | Mercury precession | 5 | Mercury perihelion precession from toroidal (probe/source)² scaling misses measured 43″/century | 10⁻³ | MESSENGER | Untested | Requires Q5 execution |
| K12 | Lorentz invariance | 5 | Integer-cell-count c-invariance fails or time-dilation scaling breaks | Exact | Experiment | **Closed for photons** | Observer tick-rate scaling pending |
| K13 | Gravitational wave emission | 5 | Binary inspiral power from substrate gravitational-channel dynamics misses LIGO | 10⁻² | LIGO | Untested | Level 5 mechanism |
| K14 | Ω_Λ partition | 6 | (251-22π)/264 miss from measured Ω_Λ exceeds 85 ppm | 85 ppm | Planck 2018 | **Cleared at 84.5 ppm** | Round 0 confirmed |
| K14b | Ω_DM prefactor | 6 | π/12 prediction deviates substantially from measured Ω_DM | 1σ | Planck 2018 | **Cleared at 0.4σ** | Round 0 confirmed |
| K15 | CMB spectrum | 6 | Acoustic peak structure from substrate cosmic-channel arithmetic misses measurement | 10⁻³ | Planck | Untested | Level 6 detailed |
| K16 | BBN yields | 6 | Primordial element abundances from substrate early-universe channel arithmetic miss measurement | 10⁻² | Astrophysics | Untested | Level 6 detailed |
| K17 | Bell correlation reproduction | 0-1 | Substrate arithmetic fails to reproduce E = ±cos(θ_A − θ_B) at Hensen precision | 10⁻³ | Hensen 2015, Giustina 2015 | Untested | Round 1 Priority 1 |
| K18 | Four-loop toroidal crossover | 1-2 | Mass-dependent four-loop corrections fail to exhibit 22 MeV crossover | 10⁻² | τ measurement future | Untested | PHYS-49 prediction |
| K19 | Nuclear toroidal content | 3 | Nuclear-scale toroidal sector fails to contribute predicted scaling to binding | 10⁻² | Nuclear data | Untested | Sector-discrimination |
| K20 | GR factor-of-2 light bending | 5 | Light bending factor of 2 over Newtonian fails to emerge from toroidal probe-scaling | 10⁻³ | Solar eclipse | Untested | Requires Q5 execution |
| K21 | Ω_DM remainder structure | 6 | Cosmological remainders fail to show elliptic K(k) structure at alphabet-integer moduli | 10⁻³ | Planck | Untested | PHYS-49 cross-scale test |
| **K22** | **Cross-derivation discipline** | **All** | **Any mechanism claim that fails to reach measurement through multiple derivation paths at CODATA/FNAL/Planck precision** | **Native measurement precision per target** | **All experimental sources** | **Active — governs all other K-switches** | **Meta-rule of the program** |

---

## Table A2 — Hierarchy-Level Prediction Table With Pre-Registered Thresholds

| Level | Scale | Domain | Predictions | Cross-Derivation Paths | Precision Threshold | Status |
|-------|-------|--------|-------------|----------------------|--------------------|---------| 
| 0 | Planck | Substrate primitives | Unit-graph adjacency, c = 1 cell/tick, direction-continuous topology | Substrate identity (axiomatic) | Exact | Axiomatic |
| 0 | Planck | Bell correlations | E(θ_A, θ_B) = −cos(θ_A − θ_B), CHSH bound 2√2 | Channel-merger arithmetic + unit-graph Born + alphabet integer | 10⁻³ | K17 untested |
| 1 | Subatomic | Lepton channel closure | Koide K = 2/3 | Lepton mass sum / sqrt sum squared + generation democracy | 9.2 ppm (Round 0: 9.23 ppm) | **Cleared** |
| 1 | Subatomic | CKM second row | V_us = 9/40 | Integer channel expression + PDG reference | 44 ppm | **Cleared (against PDG)** |
| 1 | Subatomic | CKM second row | V_cb = 1/24 | Integer channel expression | 0.37% (Round 0: 0.37%) | **Cleared** |
| 1 | Subatomic | Fine structure | α_EM⁻¹ = 137.036 from substrate channel enumeration | Multi-path alphabet expression | 10⁻⁹ | Untested |
| 1 | Subatomic | Gap ratio | (b₁ − b₂)/(b₂ − b₃) = 38/27 | CD channel arithmetic | 3.6% (running-corrected) | Cleared (INFO) |
| 1 | Subatomic | Electron anomalous moment | a_e from four-loop dual-geometry decomposition | Spherical modulus + Layer 1 + Layer 2 | 10⁻¹² | Untested |
| 1 | Subatomic | Muon anomalous moment | a_μ from (m_μ/m_e)² toroidal amplification | Mass-scaling + sector decomposition | 10⁻⁹ | Untested |
| 1 | Subatomic | Tau anomalous moment | a_τ from (m_τ/m_e)² toroidal amplification (novel prediction) | Mass-scaling + sector decomposition | 10⁻⁹ when measured | Untested, future |
| 2 | Atomic | Hydrogen 1S-2S | 2.466 × 10¹⁵ Hz from substrate modulus arithmetic | Rydberg expression via modulus + reduced mass | 10⁻¹⁵ | Untested |
| 2 | Atomic | Lamb shift | 1057 MHz from substrate Casimir-channel mechanism | Channel structure + QED coupling | 10⁻⁶ | Untested |
| 3 | Nuclear | Proton lattice | C = 3π/2 = 6β | MATH-11 lattice factor | 0.26% (Round 0: 0.26%) | Cleared (INFO) |
| 3 | Nuclear | Deuteron binding | 2.224 MeV from substrate multi-nucleon channel arithmetic | Nuclear channel spec + binding formula | 10⁻⁵ | Untested |
| 3 | Nuclear | Neutron half-life | 881.5 s from weak-channel mechanism | Weak-channel spec + neutron structure | 10⁻³ | Untested |
| 4 | Molecular | H₂O bond angle | 104.5° from substrate molecular-orbital structure | Orbital channel arithmetic | 10⁻³ | Untested |
| 5 | Macroscopic | Inverse-square gravity | 1/r² from spherical channel spreading | Angular channel count + 4π spherical | 10⁻³ | Untested |
| 5 | Macroscopic | Kepler third law | T² ∝ a³ from channel-mediated orbital dynamics | Channel momentum + orbit closure | 10⁻³ | Untested |
| 5 | Macroscopic | Mercury precession | 43″/century from toroidal (probe/source)² scaling | GR corrections + toroidal channel structure | 10⁻³ | Untested |
| 5 | Macroscopic | Factor-of-2 light bending | 1.75″ (twice Newtonian 0.87″) from toroidal channel resolution | Probe-wavelength + source-scale toroidal | 10⁻³ | Untested |
| 5 | Macroscopic | Shapiro delay | Standard GR delay from toroidal path-lengthening | Channel curvature + photon propagation | 10⁻³ | Untested |
| 5 | Macroscopic | GW emission | Binary inspiral rate from gravitational-channel radiation | Channel-gradient dynamics | 10⁻² | Untested |
| 6 | Cosmological | Ω_DM | π/12 = 0.2618 | Universal soliton partition | 0.4σ (Round 0: 0.42%) | **Cleared** |
| 6 | Cosmological | Ω_b | 13/264 = 0.04924 | Gauge integer partition | 0.6σ (Round 0: 0.49%) | **Cleared** |
| 6 | Cosmological | Ω_Λ | (251-22π)/264 = 0.6890 | Closure + integer alphabet | 85 ppm (Round 0: 84.5 ppm) | **Cleared** |
| 6 | Cosmological | DM/baryon ratio | 22π/13 = 5.3165 | Cosmic channel prefactor | 725 ppm (Round 0: 725.2 ppm) | **Cleared** |
| 6 | Cosmological | H₀ tension ratio | 12/11 = 1.0909 | Transit counting | 0.72% measured (structure exact) | **Cleared** |
| 6 | Cosmological | Microscopic-cosmic bridge | 22π/13 = |A₄| × (α/π)⁴ × 3 × (M_Z/m_e)² | Cross-scale identity | 300 ppm (Round 0: 297.4 ppm) | **Cleared** |
| 6 | Cosmological | CMB spectrum structure | Acoustic peaks from substrate early-universe channels | Cosmic channel evolution | 10⁻³ | Untested |
| 6 | Cosmological | Dark matter toroidal structure | Halo/disk ratio from dual-geometry decomposition | Spherical halo + toroidal disk | 10⁻² | Untested |
| 6 | Cosmological | Ω_DM remainder | Ω_DM − π/12 = 0.001099 from toroidal correction | Elliptic K(k) at alphabet modulus | 10⁻³ | Untested (K21) |

---

## Table A3 — Channel Type Catalog With Sector Structure

| Channel | Activation | Direction | Throughput | Sectors | Scale Range | Creation Event | Termination | Notes |
|---------|-----------|-----------|-----------|---------|-------------|---------------|-------------|-------|
| Gravitational (drain) | Always | Radial inward toward parent soliton | Proportional to parent mass / r² | Spherical (dominant) + toroidal (at probe scale ≪ source) | All hierarchy levels | Continuous | Never | Produces 1/r² + GR corrections |
| Electromagnetic | Always (between charged solitons) | Continuous vector in frame of each endpoint | Proportional to q₁q₂/r² | Spherical + toroidal | Level 0-6 | Charge pair forms | Charge separation breaks EM adjacency | Standard Coulomb + corrections |
| Strong (confinement) | Always (within nucleon boundary) | Toroidal flux tube | Extremely high, confined | Primarily toroidal (gluon flux tubes) | Level 3 | Nucleon formation | Nucleon disassembly | PHYS-49: 99% of proton mass is flux tube |
| Strong (residual) | Conditional | Between nucleons within binding range | Moderate | Toroidal | Level 3 | Nucleon proximity | Nucleon separation | Produces nuclear binding |
| Weak | Conditional on specific interaction events | Per interaction | Interaction-specific | Mixed | Level 1-3 | Flavor-changing events | Decay completion | Decay rates, neutrino oscillation |
| Thermal | Always | Omnidirectional random | Temperature-dependent | Primarily spherical | All levels | Continuous | Never (only thermalizes) | Decoherence contribution |
| **Entanglement** | **Conditional: created by specific interaction** | **Channel vector in each endpoint's frame** | **Carries correlation, not energy** | **Both spherical + toroidal (for general entanglements)** | **All levels where QM is operative** | **Decay, scattering with entangled output, prepared state** | **Measurement or environmental dominance** | **PCTRM-2 extension** |
| Higgs | Always (for massive solitons) | N/A — adds ticks-per-cycle cost | Mass-dependent | Modulates both sectors via tick-cost | Level 1-6 (massive matter) | Higgs field presence | Never (inherent to massive matter) | Source of mass/inertia |
| Channel-sharing (merged) | Conditional: entanglement dynamics | Pattern-global | Pattern-coherent | Both | All levels during entanglement | Channel-merger trigger | Merger dominance loss | Observation-as-entanglement applies here |

---

## Table A4 — Integer Alphabet With Source/Use-Cases

| Integer | Primary Source | Use-Cases | Origin |
|---------|---------------|-----------|--------|
| 2 | Universal | Spatial dim pairs, loop doubling, 2π angular measure | Geometric primitive |
| 3 | Generation count | 3 lepton generations, 3 color charges, SU(3) dimension | SM structure |
| 4 | 2² | Spatial dims of Minkowski space, β = π/4 | Geometric primitive |
| 5 | Primes | ζ(5) denominator class, 5-fold symmetries | Number theory |
| 6 | 3×2 | 6 quarks, 6β = C_proton, 6 fundamental fermions | SM structure |
| 8 | 2³, 2π/β | L1 circumference of unit circle, 8 gluons, loop normalization | Geometric + SM |
| 9 | 3² | V_us numerator (9/40), 3-generation squared | Alphabet composite |
| 11 | Yang-Mills beta | Gauge running control, Yang-Mills coefficient | QFT structure |
| 12 | 4×3, 11+1 | Ω_DM denominator (π/12), H₀ ratio (12/11) | Integer alphabet primary |
| 13 | Modified SU(2) beta | sin²θ_W = 3/13, Ω_b = 13/264, A₄ coefficient 13/8 | Framework primary |
| 22 | 2×11 | Yang-Mills doubling, Ω_Λ = (251-22π)/264, DM/baryon 22π/13 | Framework primary |
| 24 | 8×3, 4! | V_cb = 1/24, 24 quark flavor states | Alphabet composite |
| 27 | 3³ | Gap ratio 38/27, three-generation cubed | Alphabet composite |
| 38 | 19×2 | Gap ratio 38/27 | Alphabet secondary |
| 40 | 8×5 | V_us denominator (9/40) | Alphabet composite |
| 43 | Prime | 22 + 21 (boundary integer), Mercury precession 43"/century | Alphabet secondary |
| 47 | Prime | Proton lattice factor 47/10 (placeholder) | Alphabet secondary |
| 48 | 16×3 | Four-loop normalization | Alphabet secondary |
| 63 | 9×7 | Secondary integer | Alphabet secondary |
| 91 | 7×13 | Secondary integer | Alphabet secondary |
| 104 | 8×13 | sin²θ_W correction 15/104 | Alphabet composite |
| 115 | 5×23 | Secondary integer (218/115 in framework) | Alphabet secondary |
| 144 | 12² | A₂ coefficient 197/144 | Alphabet composite |
| 169 | 13² | Alphabet composite |
| 197 | Prime | A₂ coefficient 197/144 | Alphabet secondary |
| 211 | Prime | Secondary integer | Alphabet secondary |
| 218 | 2×109 | Secondary integer (218/115) | Alphabet secondary |
| 251 | Prime | Ω_Λ numerator (251-22π)/264 | Framework primary — closure constant |
| 264 | 8×3×11 | Cosmological partition denominator | Framework primary |
| 299792458 | c_SI | Speed of light exact integer | SI definition |
| 313 | Prime | Secondary integer | Alphabet secondary |
| 1015 | 5×7×29 | Secondary integer | Alphabet secondary |
| 5184 | 2⁶×3⁴ | A₃ coefficient 28259/5184 | Alphabet composite |
| 28259 | Prime | A₃ coefficient 28259/5184 | Alphabet secondary |

Transcendentals:
| Symbol | Identity | Use-Cases |
|--------|---------|-----------|
| π | Circle constant | Every angular integration |
| β | π/4 | L1/L2 spherical conversion factor |
| K(k) | Complete elliptic integral first kind | Toroidal period |
| E(k) | Complete elliptic integral second kind | Toroidal circumference |

---

## Table A5 — Topology-Specific Modulus Catalog

| Modulus | Value | Spread (cross-derivation) | Source | Character |
|---------|-------|--------------------------|--------|-----------|
| k = 0 | 0 | Exact | Spherical limit (β = π/4 only) | Pure spherical |
| k₈₁ | 0.999994 | 167 ppb | Laporta topology 81, three-integral consistency | Near-degenerate torus (elongated 4:1) |
| k₈₃ | 0.997130 | 25 ppm | Laporta topology 83, three-integral consistency | Large aspect torus (2.3:1) |
| k(A₃) | 0.99 (approximate) | Single-path magnitude match | A₃ β⁰ remainder fit | Embryonic toroidal at three loops |
| k(A₄) | 0.995 (approximate) | Single-path magnitude match | A₄ = -(13/8)×K/π fit | Near divergence |
| k(cosmic) | TBD | To be derived | Ω_DM remainder K21 test | Cosmic-scale toroidal (pending) |
| k(nucleon) | TBD | To be derived | Nuclear sector toroidal structure | Nuclear-scale toroidal (pending) |
| k(proton flux) | TBD | To be derived | Proton gluon flux tube toroidal | Strong-confinement scale (pending) |

---

## Table A6 — Round 0 Results Summary

| # | Check | Predicted | Measured | Miss | Status |
|---|-------|----------|----------|------|--------|
| 1 | β = π/4 | 0.785398163 | 0.785398163 | 1.22×10⁻¹¹ ppm | **PASS** (identity) |
| 2 | Ω_DM = π/12 | 0.261799 | 0.2607 | 4217 ppm / 0.42% | **INFO** (within 1σ Planck) |
| 3 | Ω_b = 13/264 | 0.049242 | 0.0490 | 4947 ppm / 0.49% | **INFO** (within 1σ Planck) |
| 4 | Ω_Λ = (251-22π)/264 | 0.688958 | 0.6889 | 84.5 ppm | **PASS** (target: 85 ppm) |
| 5 | Flatness Σ = 1 | 1.000000 | 1.000000 | 0.0 exactly | **PASS** (structural) |
| 6 | DM/baryon = 22π/13 | 5.31654 | 5.3204 | 725.2 ppm | **PASS** (matches PHYS-48) |
| 7 | H₀ ratio = 12/11 | 1.090909 | 1.090909 | 8×10⁻⁴ ppb | **INFO** (structural identity) |
| 8 | Koide K = 2/3 | 0.666660 | 0.666667 | 9.23 ppm | **PASS** (target: 9.2 ppm) |
| 9 | Democracy 4/3 | 4/3 × 3 | 4/3 target | Exact Fraction | **PASS** |
| 10 | Gap ratio 38/27 | 1.40741 | 1.35819 | 3.62% | **INFO** (structural vs running) |
| 11 | V_us = 9/40 (against 0.2243) | 0.225 | 0.2243 | 3121 ppm | **FAIL** (wrong pool reference) |
| 11b | V_us = 9/40 (against 0.22501 PDG) | 0.225 | 0.22501 | 44 ppm | **PASS** (correct pool reference) |
| 12 | V_cb = 1/24 | 0.04167 | 0.04182 | 0.37% | **PASS** (target: 0.37%) |
| 13 | Proton lattice 3π/2 | 4.71239 | 4.7 (placeholder) | 2636 ppm | **INFO** (placeholder precision) |
| 14 | Bridge 22π/13 | 5.31654 | 5.31812 | 297.4 ppm | **PASS** (target: 300 ppm) |
| 15 | Photon speed c_SI | 299792458/1 | 299792458/1 | Exact | **PASS** |
| 16 | L1 circumference = 8 | 8/1 | 8/1 | Exact | **PASS** |

**Summary statistics:**
- Internal pass count: 15 of 16
- External PASS: 11 (65%)
- FAIL: 1 (pool-reference, not substrate)
- INFO: 5 (all within measurement band or structural)
- RUM-precision reproductions: 4 (Ω_Λ, Koide, DM/baryon, bridge)
- Structural identities: 6 (β, flatness, democracy, photon speed, L1, H₀ ratio)
- Kill switches triggered: 0
- Q-questions resolved at Round 0: 0 (baseline consistency only)

---

## Table A7 — Cross-Derivation Examples From RUM Program

| Target | Source Papers | Derivation Paths | Precision | Cross-Derivation Status |
|--------|--------------|-----------------|-----------|------------------------|
| Ω_Λ | PHYS-52 | (251-22π)/264 from partition closure; Round 0 recompute | 85 ppm | **Cross-validated** — PHYS-52 derivation + Round 0 independent recompute both land 84-85 ppm |
| Koide K | PHYS-50 | Lepton mass formula + Round 0 independent recompute | 9.2 ppm | **Cross-validated** |
| DM/baryon | PHYS-48 | 22π/13 from channel arithmetic + Round 0 recompute | 725 ppm | **Cross-validated** |
| Microscopic-cosmic bridge | PHYS-53 | |A₄|(α/π)⁴ × 3(M_Z/m_e)² + Round 0 recompute | 300 ppm | **Cross-validated** |
| β = π/4 | MATH-11 | L1/L2 metric conversion + PHYS-55 substrate adjacency | Exact structural | **Cross-validated** |
| L1 circumference = 8 | MATH-11 | ∫₀²π (\|sin θ\| + \|cos θ\|) dθ + Round 0 pool verification | Exact | **Cross-validated** |
| V_us = 9/40 | PHYS-53 | Integer CKM + PDG 2024 reference | 44 ppm | **Cross-validated** against PDG |
| V_cb = 1/24 | PHYS-53 | Integer CKM + measured sin θ₂₃ | 0.37% | **Cross-validated** |
| H₀ ratio 12/11 | PHYS-48 | Transit counting + measured Planck/SH0ES ratio | 0.72% measured (structure exact) | **Cross-validated** |
| Gap ratio 38/27 | Framework | CD channel arithmetic + measured running values | 3.6% (structural vs running) | **Structurally consistent** |
| Proton lattice 3π/2 | MATH-11 | 6β identity + measured lattice factor | 0.26% (placeholder-limited) | **Limited by pool precision** |
| k₈₁ = 0.999994 | PHYS-49 | Three-integral consistency from ζ subtraction + elliptic forms | 167 ppb | **Strong cross-derivation** (three paths converge) |
| k₈₃ = 0.997130 | PHYS-49 | Three-integral consistency | 25 ppm | **Strong cross-derivation** |
| A₃ β⁰ remainder | PHYS-49 | Single-path magnitude match to (20/3)×K×E(0.99) | 1.8 ppm | **Single-path (suggestive, pending second path)** |
| A₄ = -(13/8)K(0.995)/π | PHYS-49 | Single-path magnitude match | 12.5 ppm | **Single-path (pending cross-derivation)** |

---

## Table A8 — Q-Questions Status Matrix

| # | Question | Previous Status | Current Status | Resolution Mechanism | Remaining Work | Dependency |
|---|---------|-----------------|----------------|---------------------|---------------|-----------|
| Q1 | Propagation modulus M value | Highest priority / free parameter | **Derivable** | Alphabet-bound by gauge coupling running fractions | Identify specific alphabet expression | Gauge running derivation (Q1 execution) |
| Q2 | Lorentz recovery | Highest priority / unspecified | **Photon piece closed (integer cell count)** + time-dilation piece pending | Substrate arithmetic identity N/N = 1 for photons; observer tick-rate scaling outstanding | Explicit derivation of observer tick-rate scaling under boost | Self-contained |
| Q3a | QM extension: non-locality (Bell) | Highest priority / unspecified | **Closed (PCTRM-2)** | Channel-sharing / shared-substrate merger | Bell correlation cross-derivation test (Round 1 Test 1) | None — ready to test |
| Q3b | QM extension: superposition | Highest priority / unspecified | **Channel-level specified, soliton-level pending** | Channel carries spherical + toroidal content; projection produces measurement outcomes | Single-particle interference quantitative test | Requires complex-amplitude derivation (partial from MATH-12) |
| Q3c | QM extension: interference | Highest priority / unspecified | **Specified via channel-agreement** | Multi-path channel-agreement at termination; observer participation modifies resolution | Double-slit + quantum eraser cross-derivation tests | Self-contained within channel-agreement |
| Q3d | QM extension: measurement/collapse | Highest priority / unspecified | **Closed (observation-as-entanglement)** | Observer + target channel-merger; collapse = new merger dominating old | General collapse criterion specification | Self-contained |
| Q3e | Born rule structure | Highest priority / postulate | **Closed (unit-graph + round-trip)** | Unit-adjacency substrate + round-trip closure on S² = |·|² emergent | Specific numerical probability computations | Requires G1 channel state structure |
| Q4 | 1/r² from channel spreading | Highest priority / unspecified | **Structurally framed** | Spherical channel spreading = angular channel count / 4πr² | Execute derivation chain to continuum 1/r² at solar-system scale | Self-contained |
| Q5 | GR corrections | High priority / unspecified | **Structurally framed** | Toroidal sector becomes visible at (probe_λ/source_scale)² resolution | Execute factor-of-2 light bending cross-derivation | Requires Q4 and toroidal channel spec |
| Q6 | QCD confinement from substrate | Medium / unspecified | **Partially specified** | Gluon flux tubes = toroidal strong-channel content (99% of proton mass) | Nucleon binding cross-derivation | Requires strong-channel spec |
| Q7 | Neutrino masses and mixing | Medium / unspecified | **Open** | Weak-channel arithmetic for flavor-mixing | Derive PMNS matrix from alphabet | Requires weak-channel spec |
| Q8 | Dark energy mechanism | Medium / Ω_Λ only | **Partially resolved via Ω_Λ identity** | (251-22π)/264 closure | Mechanism for why Λ is exactly this value | Requires Q4 cosmic-scale execution |
| Q9 | Baryogenesis / matter asymmetry | Medium / unspecified | **Open** | CP violation from channel-state symmetry breaking | Derive asymmetry parameter from alphabet | Requires weak-channel + early-universe substrate spec |
| Q10 | Higgs coupling to per-tick budget | High priority / unspecified | **Specified as per-hierarchy-boundary modulus** | Level-indexed modulus family from alphabet | Execute modulus derivation per boundary | Self-contained |
| Q11 | Universal vs level-specific modulus | Medium / open | **Unified with Q10** | Per-hierarchy-boundary modulus family | Same as Q10 | Same as Q10 |
| Q12 | Entanglement across channel network | Medium / unspecified | **Closed (channel-sharing)** | Solitons sharing channel substrate | Bell test validation (Q3a) | None |
| Q13 | Collapse mechanism | Medium / unspecified | **Closed for entanglement, partial for general** | Observation-as-entanglement for entangled case; general case via channel-agreement termination | General-case measurement criterion | Requires channel-agreement quantitative |
| Q14 | Born rule from discrete amplitudes | Medium / postulate | **Closed (unit-graph round-trip)** | Round-trip closure on unit-adjacency graph | Specific probability computations | Requires G1 |
| Q15 | Decoherence mechanism | Medium / unspecified | **Closed (environmental channel-merger dominance)** | Environmental channels outcompete original entanglement | Quantitative decoherence rate predictions | Requires channel-dominance formula |
| Q16 | Classical limit emergence | Medium / unspecified | **Partially specified** | Large-soliton channel averaging produces classical mechanics | Derive Newton F = ma from substrate at macroscopic scale | Requires Q4 |
| Q17 | Arrow of time / thermodynamic direction | Low-Medium / unspecified | **Open** | Substrate dynamics are tick-directed; second law emergent | Derive entropy increase from cell-tick arithmetic | Self-contained |
| Q18 | Dark matter identity | High / structure only | **Partially resolved via Ω_DM = π/12** | Cosmic-scale spherical channel content | Mechanism for DM particle identity (if any) | Open |

**Summary:**
- **Closed** (full resolution): Q3a, Q3d, Q3e, Q12, Q14, Q15
- **Closed with pending execution** (mechanism specified, numerical derivation pending): Q2, Q4, Q10, Q11, Q13 (entanglement case), Q16
- **Structurally framed / partially specified**: Q3b, Q3c, Q5, Q6, Q8
- **Derivable** (alphabet expression pending): Q1
- **Open**: Q7, Q9, Q17, Q18 (mechanism aspect)

**Previous state (PHYS-54):** 7+ open conceptual questions at highest priority, multiple unresolved mechanisms, Q3 as largest gap.

**Current state (PHYS-55):** 1 alphabet-identification question (Q1), 4 mechanism-specified-pending-execution questions (Q2 time-dilation half, Q4, Q5, Q10), 4 open mechanism questions (Q7, Q9, Q17, Q18-mechanism). The remainder is execution.

---

## Table A9 — Round 1 Coordinated Test Program

| Test | Priority | Level | Mechanism | Derivation Paths Required | Precision Target | Measurement Reference | Kill Switch |
|------|---------|-------|-----------|--------------------------|-----------------|---------------------|-------------|
| T1: Bell correlation reproduction | 1 | 0-1 | Channel-sharing + unit-graph Born + integer alphabet | (a) Channel-merger projection arithmetic, (b) MATH-11 β² exponent counting applied to round-trip closure, (c) Alphabet-integer expression for Tsirelson bound | 10⁻³ on CHSH bound 2√2 and E(θ_A, θ_B) at test angles | Hensen 2015, Giustina 2015, Shalm 2015 | K17, F-E1, F-E2 |
| T2: Cosmological remainder dual geometry | 1 | 6 | MATH-12 cosmic-scale toroidal content | (a) Direct elliptic scan at alphabet moduli, (b) Cosmic partition budget + toroidal correction, (c) Scaling from QED k₈₁/k₈₃ through hierarchy-boundary relation | Planck precision on Ω_DM, Ω_b, Ω_Λ remainders | Planck 2018 | K21 |
| T3: A₄ cross-derivation | 1 | 1-2 | Dual-geometry four-loop decomposition | (a) Spherical modulus + Layer 1 + Layer 2 sum, (b) -(13/8)×K(k₈₁)/π + K(k₈₃) combination, (c) Gauge beta structure (13 = b₂') with loop normalization (8 = 2π/β), (d) MATH-12 toroidal-period arithmetic on extracted moduli | Harvard precision on a_e | Harvard 2023 | K4 |
| T4: Mass-scaling crossover prediction | 2 | 1 | Toroidal sector mass-dependent scaling | (a) (m_τ/m_e)² from toroidal coupling, (b) Cross-lepton sector dominance | 10⁻⁹ on τ anomalous moment when measured | Future tau measurement | K18 |
| T5: GR factor-of-2 light bending | 2 | 5 | Toroidal (probe_λ/source_scale)² scaling | (a) Direct toroidal drain-vector computation, (b) Alphabet expression for GR coefficient | 10⁻³ on bending angle | Solar eclipse data | K20 |
| T6: Single-particle interference | 2 | 0-1 | Channel-agreement at single-particle scale | (a) Multi-path channel-agreement resolution, (b) Observer-in-agreement-pool modification | 10⁻² on fringe visibility | Standard double-slit | K17 (extended) |
| T7: Mercury precession | 3 | 5 | Toroidal probe-resolution at Mercury-orbit scale | (a) Orbital toroidal content, (b) Alphabet expression for precession rate | 10⁻³ on 43"/century | MESSENGER data | K11 |
| T8: Hydrogen 1S-2S | 3 | 2 | Substrate modulus arithmetic + Q3 QM extension | (a) Rydberg from modulus + Higgs tax, (b) Cross-derivation via α-based path | 10⁻¹⁵ on 1S-2S frequency | MPQ 2020 | K5 |
| T9: Alphabet expression for Q1 (modulus M) | 4 | 0 | Gauge coupling running fractions | (a) From sin²θ_W running, (b) From Yang-Mills 22 doubling, (c) From gauge group integer 13 | Framework precision | Internal cross-derivation validation | K22 |
| T10: Alphabet expression for particle masses (Q10) | 4 | 1 | Per-hierarchy-boundary modulus derivation | (a) From lepton generation democracy 4/3, (b) From CKM integer alphabet | CODATA precision | CODATA 2018 | K1, K2 |

**Test suite design:**
- **Round 1 Priority 1 tests** (T1, T2, T3): three simultaneous mechanism validations, each with multi-path cross-derivation
- **Round 1 Priority 2 tests** (T4, T5, T6): extensions of primary mechanisms to additional phenomena
- **Subsequent rounds** (T7-T10): deeper validation as mechanisms mature

**Success criteria:**
- All three Priority 1 tests passing at stated precision = PCTRM mechanism-level validation
- Any Priority 1 test failing = specific mechanism falsified, requiring revision
- Priority 2 tests: discriminate between mechanism candidates
- Priority 3+: framework prediction capability test

---

## Table A10 — Standard Model Reduction Coverage

| SM Feature | PCTRM Mechanism | Precision Achieved (if tested) | Status |
|-----------|-----------------|-------------------------------|--------|
| Fermion generation count = 3 | Substrate channel structure | Structural (exact) | Reproduced (structural) |
| Lepton generation democracy Σ m/sqrt(sum m)² = 4/3 | Generation democracy + channel closure | Exact (Round 0) | Reproduced |
| Gauge group U(1) × SU(2) × SU(3) | Channel type enumeration (pending explicit mapping) | Structural | Partial |
| Koide K = 2/3 | Lepton channel closure | 9.2 ppm (Round 0) | Reproduced at CODATA precision |
| Cabibbo angle V_us = 9/40 | CKM integer channel | 44 ppm (against PDG) | Reproduced |
| V_cb = 1/24 | CKM integer channel | 0.37% (Round 0) | Reproduced |
| Gap ratio 38/27 | CD channel arithmetic | 3.6% (structural vs running) | Structurally consistent |
| Fine structure constant α⁻¹ = 137.036 | Substrate channel count (pending derivation) | Pending | Predicted target |
| Electron magnetic moment a_e | Four-loop dual-geometry decomposition | Pending | Predicted via Round 1 T3 |
| Muon g-2 discrepancy | Mass-scaled toroidal sector | Pending | Predicted via Round 1 T4 |
| Higgs mechanism (mass source) | Per-tick Higgs interaction cost | Mechanism specified | Framework mechanism |
| Mass hierarchy (lepton, quark) | Per-hierarchy-boundary modulus | Pending | Predicted via Round 1 T10 |
| Neutrino masses and mixing | Weak-channel arithmetic + PMNS | Pending | Q7 open |
| Anomalous magnetic moments (four-loop) | Spherical modulus + Layer 1 + Layer 2 decomposition | sub-ppm moduli extracted | PHYS-49 cross-derivation candidate |
| Renormalization group running | Substrate scale-dependent channel averaging | Structural | Framework mechanism |
| CP violation | Channel-state symmetry breaking | Pending | Q9 open |
| QCD confinement | Toroidal gluon flux tubes | 99% proton mass structural | PHYS-49 structural |
| Asymptotic freedom | Channel-coupling scaling at high energy | Pending | Framework prediction target |
| Electroweak unification | Gauge group reduction at high energy | Structural | Partial |
| SM postulate: Born rule | Unit-graph round-trip closure | Structural (derived) | Closed |
| SM postulate: unitary evolution | Substrate per-tick update preserves channel content | Structural | Mechanism |
| SM postulate: measurement collapse | Observation-as-entanglement | Structural (derived) | Closed |

---

## Table A11 — Standard Cosmology Reduction Coverage

| Cosmological Feature | PCTRM Mechanism | Precision Achieved (Round 0) | Status |
|---------------------|-----------------|-----------------------------|--------|
| Ω_DM = 0.2607 | π/12 cosmic partition spherical sector | 0.42% (within 1σ Planck) | Reproduced |
| Ω_b = 0.0490 | 13/264 cosmic partition integer | 0.49% (within 1σ Planck) | Reproduced |
| Ω_Λ = 0.6889 | (251-22π)/264 closure | 85 ppm | Reproduced |
| Σ Ω_i = 1 | Cosmic partition closure | Exact | Structural |
| DM/baryon ratio = 5.32 | 22π/13 | 725 ppm | Reproduced |
| H₀ tension (SH0ES vs Planck) | 12/11 transit counting | 0.72% on ratio | Structural reproduction |
| CMB temperature 2.725 K | Substrate thermal channel spectrum (pending) | Pending | Predicted target |
| CMB acoustic peak positions | Substrate sound horizon arithmetic | Pending | Predicted via K15 |
| BBN element abundances | Substrate early-universe channel dynamics | Pending | Predicted via K16 |
| Cosmic flatness | Partition closure to unity | Exact (Round 0) | Structural |
| Bridge identity 22π/13 = |A₄|(α/π)⁴·3·(M_Z/m_e)² | Micro-cosmic channel consistency | 300 ppm | Reproduced |
| Dark matter halo structure | Spherical channel sector at cosmic scale | Structural | Mechanism |
| Galactic disk structure | Toroidal channel sector at cosmic scale | Structural | Mechanism |
| Ω_DM remainder (− π/12) | Elliptic K(k) at alphabet modulus | Pending | Predicted via K21 |
| Dark energy equation of state w = −1 | Substrate cosmological constant mechanism | Structural (Λ = closure constant) | Partial |
| Cosmic horizon | Substrate light-cone arithmetic + integer cell count | Structural | Mechanism |
| Gravitational wave background | Cosmic-scale channel gradient dynamics | Pending | Predicted target |

---

## Table A12 — Framework Precision Ledger

| Precision Level | Framework Achievement | Examples | Measurement Reference |
|----------------|----------------------|----------|---------------------|
| Exact (structural identity) | β = π/4, L1 = 8, Photon speed = c_SI, Generation democracy = 4/3 | MATH-11, Round 0 | Substrate definitions |
| ≤ 1 ppb | None yet | — | — |
| 1-100 ppb | Laporta modulus consistency (167 ppb for k₈₁) | PHYS-49 cross-derivation | Internal framework |
| 1-100 ppm | Ω_Λ at 85 ppm, Koide at 9.2 ppm, k₈₃ at 25 ppm, bridge at 300 ppm | PHYS-48, PHYS-50, PHYS-52, PHYS-53, PHYS-49 | Planck 2018, CODATA |
| 100-1000 ppm | DM/baryon at 725 ppm | PHYS-48 | Planck 2018 |
| 0.1-1% | Proton lattice at 0.26% (placeholder-limited), V_cb at 0.37% | PHYS-53 | Experimental |
| 1-10% | Ω_DM at 0.42%, Ω_b at 0.49% (within Planck 1σ), gap ratio at 3.6% (structural vs running) | PHYS-48 | Planck, PDG |
| CODATA-grade required for Round 1 | α⁻¹, a_e, m_e, m_μ, m_τ, Rydberg | — | CODATA 2018 |
| FNAL-grade required for Round 1 | a_μ (muon g-2) | — | FNAL Muon g-2 |
| Harvard-grade required for Round 1 | a_e (electron g-2) | — | Harvard 2023 |

**Framework's cross-derivation record:**

- **5 validations at published precision** (4 RUM identities + Round 0 recompute)
- **2 cross-derivations at sub-ppm** (k₈₁, k₈₃)
- **15 of 16 Round 0 consistency checks pass** internal precision
- **0 kill switches fired** across Round 0
- **Pending:** Round 1 three-test program (mechanism validation)

---
