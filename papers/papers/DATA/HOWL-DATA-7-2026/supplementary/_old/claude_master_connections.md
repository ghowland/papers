# HOWL SERIES — MASTER CONNECTION & LAYER TABLES
# ==================================================
# How everything connects to everything else.
# Verified against phys24_lib.py and computation.
# ==================================================


## TABLE C1: THE SOLITON NESTING HIERARCHY (11 LEVELS)

Every level is a ground state within a container. Same principle everywhere.
GM/(rc^2) determines well depth. R2 in every orbital area.

| Level | Name | Size | GM/(rc^2) | Binding Force | Boundary Type | Escape Mechanism |
|-------|------|------|-----------|---------------|---------------|------------------|
| 1 | Proton (QCD) | ~1 fm | 1.5e-39 (grav), ~1 (QCD) | Strong (confinement) | Confinement wall | ~2 GeV (deconfinement) |
| 2 | Atom (EM) | ~0.1 nm | ~10^-8 | Electromagnetic | Ionization energy | 13.6 eV (hydrogen) |
| 3 | Crystal lattice | ~nm - km | ~10^-10 | EM/covalent | Melting point | Phase transition |
| 4 | Geological | ~m - km | ~10^-10 | Material strength | Fracture/yield | Pressure threshold |
| 5 | Human on surface | ~1.7 m | 6.96e-10 | EM normal force | Jump height | ~1 m (muscle energy) |
| 6 | Earth Hill sphere | 1.50e6 km | 6.96e-10 | Gravity | L1 Lagrange point | v_esc = 11.2 km/s |
| 7 | Earth orbit | 1 AU | 9.87e-9 | Gravity (Kepler) | Heliocentric orbit | v_esc = 42 km/s |
| 8 | Solar Hill sphere | ~120 AU | ~10^-6 | Gravity | Voyager boundary | v_esc ~ 0.5 km/s |
| 9 | Galactic disk | ~15 kpc | 1.15e-6 | Gravity + DM | Virial radius | v_circ = 220 km/s |
| 10 | Galaxy cluster | ~3 Mpc | ~10^-5 | Gravity + DM | Virial radius | ~1000 km/s |
| 11 | Cosmological (BAO) | ~150 Mpc | — | Hubble flow | H0 running | N~100 boundaries |


## TABLE C2: THE ENERGY BOUNDARY STACK (HIGH → LOW)

Every boundary where integer rules change. With energy scale, distance scale,
and running distance L = ln(E/M_Z)/(2*pi) from the reference point M_Z.

| Boundary | Energy (MeV) | Distance (m) | L from M_Z | Known | Forces |
|----------|-------------|-------------|------------|-------|--------|
| Planck | 1.221e22 | 1.62e-35 | +6.276 | no | gravity, unified |
| GUT (CD est.) | 3.5e18 | 5.64e-32 | +4.978 | no | all unified |
| CD threshold | ~3e6 | 6.58e-20 | +0.556 | no | strong, weak, EM |
| Top quark | 172570 | 1.14e-18 | +0.102 | yes | strong |
| Higgs boson | 125200 | 1.58e-18 | +0.050 | yes | weak, EM |
| Z boson (ref) | 91187.6 | 2.16e-18 | 0.000 | yes | weak, EM, strong |
| W boson | 80369.2 | 2.46e-18 | -0.020 | yes | weak |
| Bottom quark | 4183 | 4.72e-17 | -0.491 | yes | strong |
| Tau lepton | 1776.86 | 1.11e-16 | -0.627 | yes | EM |
| Confinement upper | ~2000 | 9.87e-17 | -0.608 | approx | strong |
| Charm quark | 1273 | 1.55e-16 | -0.680 | yes | strong |
| Confinement lower | ~300 | 6.58e-16 | -0.910 | approx | strong |
| Strange quark | 93.5 | 2.11e-15 | -1.095 | yes | strong |
| Muon | 105.66 | 1.87e-15 | -1.076 | yes | EM |
| Electron | 0.511 | 3.86e-13 | -1.925 | yes | EM |

Total running from m_e to M_GUT: L = 6.903 (18.8 decades in energy).
Confinement wall width: L = 0.302 (0.82 decades). 4.4% of total running.


## TABLE C3: BOUNDARY-TO-BOUNDARY RUNNING DISTANCES

How far apart boundaries are in running distance L and energy decades.

| From | To | Delta-L | Decades | What Changes |
|------|----|---------|---------|-------------|
| electron | muon | 0.849 | 2.32 | 2nd gen lepton activates |
| muon | strange | 0.019 | 0.05 | Nearly co-located |
| strange | confinement | 0.186 | 0.51 | Enter non-perturbative zone |
| confinement wall | — | 0.302 | 0.82 | NO INTEGER RULES (blank zone) |
| confinement | charm | 0.230 | 0.63 | 4th flavor activates |
| charm | tau | 0.053 | 0.15 | 3rd gen lepton activates |
| tau | bottom | 0.136 | 0.37 | 3rd gen quark activates |
| bottom | W | 0.470 | 1.28 | Weak bosons resolvable |
| W | Z | 0.020 | 0.05 | Nearly co-located |
| Z | Higgs | 0.050 | 0.14 | Higgs excitation resolvable |
| Higgs | top | 0.051 | 0.14 | Last SM fermion |
| top | CD | 0.455 | 1.24 | RULES CHANGE: betas shift |
| CD | GUT | 4.422 | 12.1 | THREE COUPLINGS MERGE |
| GUT | Planck | 1.298 | 3.54 | Quantum gravity? |

The desert: CD to GUT is 4.422 in L-space, 12.1 decades. 64% of total running.
The SM zone: electron to top is 2.027 in L, 5.53 decades. 29% of total running.


## TABLE C4: COUPLING CONVERGENCE TABLE

How the three couplings are distributed at M_Z and approach each other upward.

| Coupling | 1/alpha at M_Z | Beta (CD) | Running Direction | Role |
|----------|---------------|-----------|-------------------|------|
| 1/alpha_1 (U1) | 63.210 | b1_mod = +25/6 = +4.167 | RISES with energy | EM hypercharge |
| 1/alpha_2 (SU2) | 31.685 | b2_mod = -13/6 = -2.167 | FALLS with energy | Weak force |
| 1/alpha_3 (SU3) | 8.475 | b3_mod = -20/3 = -6.667 | FALLS with energy | Strong force |

Spread at M_Z: 1/a1 - 1/a3 = 54.74 (factor 7.46 between strongest and weakest).
At M_GUT: all three converge to 1/alpha_GUT ~ 37-42.

The crossing point is determined by the gap ratio:
  gap_measured = (1/a1 - 1/a2) / (1/a2 - 1/a3) = 1.3582
  gap_CD = (b1-b2) / (b2-b3) = 38/27 = 1.4074

When gap_model = gap_measured exactly, the three lines cross at one point.
The 3.6% residual is the threshold/two-loop correction.


## TABLE C5: THE GAP RATIO CORRECTION CHAIN

How the gap ratio moves from pure gauge (2.000) to near the target (1.358).

| Step | Gap Before | Correction | Gap After | Distance from 1.358 | % of Total Correction |
|------|-----------|-----------|-----------|---------------------|----------------------|
| Pure gauge | — | Baseline | 2.000 | 0.642 | 0% |
| + Higgs | 2.000 | -0.104 | 1.896 | 0.538 | 16.2% |
| + SM fermions (any N) | 1.896 | 0.000 | 1.896 | 0.538 | 0.0% |
| + Cabibbo Doublet | 1.896 | -0.489 | 1.407 | 0.049 | 76.2% |
| + Threshold + 2-loop | 1.407 | -0.049 | 1.358 | 0.000 | 7.6% |

The CD does 76% of the work from pure gauge to target.
Fermions do exactly 0%. Higgs does 16%. Threshold/2-loop does 8%.


## TABLE C6: THE INTEGER NETWORK — TRACEABILITY

How integers flow from gauge group to cosmological predictions.

```
SU(3) × SU(2) × U(1) gauge group
         │
         ▼
  Yang-Mills: -(11/3) × C2(adj)
         │
    ┌────┴────┐
    ▼         ▼
  b3_SM     b2_SM gauge part
  = -11     = -22/3
    │         │
    │    ┌────┴──── + fermion(4) + higgs(1/6) + CD(1)
    │    ▼
    │  b2_mod = -13/6
    │    │
    │    ├──── |numerator| = 13
    │    │         │
    │    │    ┌────┴────────────────────┐
    │    │    ▼                         ▼
    │    │  DM/baryon                 Omega_DM
    │    │  = (2×11/13)×pi           = (4×11/13²)×R2
    │    │  = (22/13)×pi             = (44/169)×R2
    │    │  = 5.3165                 = 0.2045
    │    │                             │
    │    │                        R2 cancels
    │    │                        44/169 pure rational
    │    │
    │    ├──── b2_mod enters gap ratio
    │    ▼
    │  gap_CD = (b1_mod - b2_mod)/(b2_mod - b3_mod) = 38/27
    │
    └──── b3_mod = -20/3 enters gap ratio denominator

  11 appears: b3 gauge, DM numerator (2×11), Omega numerator (4×11)
  13 appears: b2_mod numerator, DM denominator, Omega denominator (13²)
```


## TABLE C7: R2 CONNECTION MAP — WHERE pi/4 APPEARS

R2 = pi/4. The filling fraction. Same constant across all domains.

| Domain Category | Equation | R2 Role | Z (what varies) |
|----------------|----------|---------|-----------------|
| **Fluid mechanics** | Q = R2*d²*v | Flow area | velocity |
| | F = 0.5*rho*v²*R2*d²*Cd | Drag area | drag coefficient |
| | q = Cd*R2*d²*sqrt(2dP/rho) | Orifice area | discharge coeff |
| | Q = R2*d⁴*dP/(32*mu*L) | H-P pipe | viscosity |
| **Electrical** | R = rho*L/(R2*d²) | Wire cross-section | resistivity |
| | C = eps0*R2*d²/t | Plate area | permittivity |
| **Electromagnetic** | A = eta*R2*D² | Antenna aperture | efficiency |
| | FSPL = (16*R2*d/lam)² | Path loss | distance/wavelength |
| | P = S*R2*d² | Poynting flux | irradiance |
| **Optics** | A = R2*(1.22*lam/NA)² | Airy disc spot | diffraction |
| | A = R2*MFD² | Fiber mode area | mode confinement |
| | A = R2*w0² | Gaussian beam waist | beam parameter |
| **Acoustics** | Sd = R2*d_eff² | Speaker cone area | (pure geometry) |
| | I = P/(16*R2*r²) | Sound spreading | 1/r² |
| | f = (c/(8R2))*sqrt(S/(lV)) | Helmholtz resonance | port geometry |
| **Thermal** | Q = eps*sig*T⁴*R2*d² | Radiation area | emissivity |
| **Semiconductor** | A = R2*D² | Wafer area | (pure geometry) |
| **Orbital mechanics** | T² = 64*R2²*a³/(GM) | Kepler's law | gravity GM |
| **Normalization** | 1/(8R2) = 1/(2pi) | Fourier | (identity) |
| | 1/sqrt(8R2) = 1/sqrt(2pi) | Gaussian | (identity) |
| **Superconductivity** | pi/exp(gamma) = 1.7639 | BCS gap | Euler-Mascheroni |
| **Fluid statics** | pi/(pi+2) = 4R2/(4R2+2) | Vena contracta | Kirchhoff |

All equations: Q = F(Z) × R2 × d² (or power of R2).
Same R2. Different Z. Different domain. Same geometry.


## TABLE C8: R2 CANCELLATION NETWORK

Where R2 enters two quantities and divides out in their product.

| Product | Quantity A (R2 enters) | Quantity B (R2 enters) | Result (R2 gone) | Precision |
|---------|----------------------|----------------------|------------------|-----------|
| K_J × R_K | 2e/h = 2e/(8R2*hbar) | h/e² = 8R2*hbar/e² | 2/e | 10^-8 |
| G_0 × R_K | 2e²/h | h/e² | 2 | exact |
| Wire R × Cap C | rho*L/(R2*d²) | eps0*R2*d²/t | rho*eps0*L/t | 30 digits |
| Rydberg | alpha²*m_e*c/(2h) | h = 8R2*hbar | R2-free ratio | 13 digits |
| a_0 × alpha | hbar/(m_e*c) | — | R2-free ratio | 12 digits |
| Omega_DM product | (44/169)*R2 | R2 factor | 44/169 pure rational | exact |

Pattern: R2-free observables → highest precision (10^-8 to 10^-13).
R2-dependent observables → engineering precision (~10^-6).
The modulus is topological. It cancels in symmetric ratios.


## TABLE C9: CROSS-DOMAIN AREA VALUES

Same R2*d² formula, different d, different meaning.

| Object | d | R2*d² | Meaning |
|--------|---|-------|---------|
| Blu-ray spot | 0.581 um | 0.265 um² | Smallest readable feature |
| SMF-28 fiber mode | 10.4 um | 84.95 um² | Light confinement area |
| AWG 12 wire | 2.053 mm | 3.31 mm² | Current-carrying area |
| 1-inch tweeter | 25 mm | 4.91 cm² | Sound radiation area |
| 120mm disc | 120 mm | 113.1 cm² | Data surface area |
| 12-inch woofer | 305 mm | 730.6 cm² | Sound radiation area |
| 300mm wafer | 300 mm | 706.9 cm² | Chip manufacturing area |
| 1m pipe | 1 m | 0.785 m² | Flow cross-section |
| Earth cross-section | 12742 km | 1.275e14 m² | Geometric shadow |


## TABLE C10: SOLITON COUPLING HIERARCHY

How GM/(rc²) connects different levels of the nesting hierarchy.

| System | M (kg) | r (m) | GM/(rc²) | v_esc/c | Level |
|--------|--------|-------|----------|---------|-------|
| Proton (gravitational) | 1.67e-27 | 8.4e-16 | 1.5e-39 | 5.4e-20 | 1 |
| Earth surface | 5.97e24 | 6.37e6 | 6.96e-10 | 3.73e-5 | 5-6 |
| GPS orbit | 5.97e24 | 2.66e7 | 1.67e-10 | 1.83e-5 | 6 |
| Sun-Earth orbit | 1.99e30 | 1.50e11 | 9.87e-9 | 1.40e-4 | 7 |
| Sun surface | 1.99e30 | 6.96e8 | 2.12e-6 | 2.06e-3 | 7 |
| Neutron star | 5.57e30 | 1.1e4 | 0.376 | 0.867 | — |
| Milky Way | 7.16e41 | 4.63e20 | 1.15e-6 | 1.52e-3 | 9 |

GPS correction = difference in coupling between Earth surface and GPS orbit:
  delta_phi = 6.96e-10 - 1.67e-10 = 5.29e-10
  This produces the 38.5 us/day clock correction.


## TABLE C11: HUBBLE RUNNING — DISTANCE LADDER LAYERS

How H0 measurements layer from local to cosmological.

| Layer | Method | H0 (km/s/Mpc) | Distance Class | Boundaries Crossed |
|-------|--------|---------------|----------------|-------------------|
| 1 | SH0ES (Cepheids) | 73.0 ± 1.0 | local | ~0 |
| 2 | H0LiCOW (lensing) | 73.3 ± 1.8 | local-medium | few |
| 3 | CCHP (TRGB) | 69.8 ± 1.7 | medium | several |
| 4 | DES_BAO_BBN | 67.4 ± 1.2 | high-z | many |
| 5 | Planck (CMB) | 67.4 ± 0.5 | maximum | ~100 |

Running hypothesis: H0(N) = H0_local × r^N where N = boundaries crossed.
Required r for N=100: r = (67.4/73.0)^(1/100) = 0.99919
1-r = 8.08e-4. VP step = 1/(12*R2) = 1/(3*pi) = 0.1061.
Status: HYPOTHESIS. All effective_N = None.


## TABLE C12: DWARF SOLITON PURITY SPECTRUM

How DM/visible ratio connects to the soliton hierarchy.

| System | M_vis (Msun) | M_total (Msun) | DM/vis | Dark % | Type |
|--------|-------------|---------------|--------|--------|------|
| Segue 1 | 340 | 1.3e6 | 3824 | 99.97% | Ultra-faint |
| Reticulum II | 2600 | 1.0e6 | 385 | 99.74% | Ultra-faint |
| Tucana II | 3000 | 3.6e7 | 12000 | 99.99% | Ultra-faint |
| Draco | 2.9e5 | 5.4e7 | 186 | 99.46% | Classical dSph |
| Sculptor | 2.3e6 | 7.0e7 | 30 | 96.71% | Classical dSph |
| Fornax | 2.0e7 | 1.6e8 | 8 | 87.5% | Classical dSph |
| LMC | ~2e9 | ~1e10 | ~5 | 80% | Irregular |
| Milky Way | ~6e10 | ~3.6e11 | ~6 | 83% | Spiral |
| M87 | ~1e12 | ~6e12 | ~6 | 83% | Giant elliptical |
| Cosmic average | — | — | 5.32 | 84.2% | (22/13)*pi |

The soliton exists first. Baryons load in later.
UF dwarfs: nearly pure dark solitons (99.9%+ dark).
Spirals: significant disk, but still DM-dominated.
Cosmic average matches beta integer prediction.


## TABLE C13: FABER-JACKSON / TULLY-FISHER CONNECTION

Same a0 = cH0/(8R2) connects velocity dispersion to mass at all scales.

| Relation | Formula | a0 Source | Applies To |
|----------|---------|-----------|-----------|
| Faber-Jackson | M = sigma⁴ / (G*a0) | cH0/(8R2) | Ellipticals, dSphs |
| Tully-Fisher | M = v_rot⁴ / (G*a0) | cH0/(8R2) | Disk galaxies |
| MOND transition | r = sqrt(GM/a0) | cH0/(8R2) | All: below r = Newtonian, above = MOND |

a0 = c*H0/(8R2) = c*H0/(2*pi) = 1.042e-10 m/s²
Published MOND a0 ~ 1.2e-10 m/s². Match within ~15%.

Earth MOND radius: r = sqrt(G*M_earth/a0) ~ 6.2e8 m ~ 1.6 R_Hill
Sun MOND radius: r = sqrt(G*M_sun/a0) ~ 1.1e14 m ~ 740 AU

Below r: gravity is Newtonian (GM/r²).
Above r: gravity transitions to MOND regime (sqrt(GM*a0)/r).


## TABLE C14: THE THREE PROGRAMS — SHARED INTEGER SET

How the same integers connect three different physical domains.

| Integer | Beta Unification | Cosmological Parameters | Soliton Gravity |
|---------|-----------------|------------------------|-----------------|
| 11 (YM) | b3_SM gauge = -11 | DM numerator: 2×11=22 | — |
| 13 (|b2_mod|) | b2_mod = -13/6, gap denom | DM denom: 13, Omega: 13²=169 | — |
| R2 = pi/4 | — | 4R2 in DM/baryon, R2 in Omega | Kepler 64R2², GPS, MOND a0 |
| 19 (|b2_SM|) | gap_SM numerator | Dwarf cosmic ratio ~19 | — |
| 38 = 2×19 | gap_CD = 38/27 | — | — |
| 27 = 3³ | gap_CD = 38/27 | — | — |

Program 1 (Beta Unification): 11, 13 → betas → gap ratio → M_GUT → proton decay
Program 2 (Cosmological): 11, 13 → DM/baryon, Omega_DM → cosmological parameters
Program 3 (Soliton Gravity): R2 → Kepler, GPS, MOND, Hill spheres, process rate

The question: is the (11, 13) coincidence between Programs 1 and 2 structural or accidental?
BLOCKING: statistical control script needed to answer this.


## TABLE C15: CONTAINMENT CHAIN — FROM QUARK TO COSMOS

The complete nesting with coupling, boundary type, and scale.

| Contains | Contained In | Coupling at Boundary | Boundary Mechanism | Scale |
|----------|-------------|---------------------|-------------------|-------|
| Quark | Proton | alpha_s ~ O(1) | Confinement | ~1 fm |
| Proton | Nucleus | ~8 MeV/nucleon | Nuclear force (residual strong) | ~1-5 fm |
| Nucleus | Atom | 13.6 eV (H) | EM binding (Coulomb) | ~0.05 nm |
| Electron | Atom | 13.6 eV (H) | EM binding (Coulomb) | ~0.05 nm |
| Atom | Crystal | ~0.1-10 eV | Covalent/ionic/metallic | ~0.1-1 nm |
| Crystal | Geological | Yield stress | Pressure + gravity | ~m-km |
| Geological | Earth | Self-gravity | Differentiation | ~6400 km |
| Object | Earth surface | GM/(Rc²) = 7e-10 | EM normal force | 6371 km |
| Moon | Earth Hill sphere | Tidal | L1 Lagrange | 1.5e6 km |
| Earth | Solar orbit | GM_sun/(AU*c²) = 1e-8 | Kepler T² = 64R2²a³/GM | 1 AU |
| Solar | Galaxy | v_circ² / c² ~ 5e-7 | Disk rotation | ~8 kpc |
| Galaxy | Cluster | Virial | DM halo | ~1-3 Mpc |
| Cluster | Cosmological | Hubble flow | BAO | ~150 Mpc |

Re-nesting: if a new scale is discovered between atom and crystal (e.g., a mesoscopic
quantum soliton boundary), a new row is inserted. The others shift. Nothing is deleted.
The containment chain is mutable. The coupling values are not.


## TABLE C16: LAYER CLASSIFICATION — WHAT DETERMINES WHAT

| Layer | Content | Determined By | Can Change? |
|-------|---------|--------------|-------------|
| Level 0 | R2, R4, Q335 constants | Mathematics | No |
| Level 1 | Betas, Casimirs, Dynkin indices, democracy | Gauge group SU(3)×SU(2)×U(1) | No (same gauge group) |
| Level 1 | Gap ratios (218/115, 38/27) | Level 1 betas | No |
| Level 1 | DM/baryon = (22/13)*pi | Level 1 integers | No |
| Level 2 | alpha_inv, sin2_tW, alpha_s | Universe (measurement) | Could be different |
| Level 2 | Masses (m_e through m_t) | Universe (measurement) | Could be different |
| Derived | Measured gap ratio = 1.3582 | L1 formula on L2 inputs | Changes if L2 changes |
| Derived | M_GUT = 10^15.54 | L1 running on L2 couplings | Changes if L2 changes |
| Derived | alpha_s predicted = 0.11838 | L1 running on L2 couplings | Changes if L2 changes |
| Derived | m_tau predicted = 1776.97 | L1 identity on L2 masses | Changes if L2 changes |
| Derived | GPS = 38.5 us/day | L1 formula on L2 astro values | Changes if L2 changes |


## TABLE C17: ADJACENCY MAP — WHAT'S NEXT TO WHAT IN ENERGY

Boundaries that are close together interact strongly during running.

| Cluster | Boundaries | Energy Range | Running Width (L) | Character |
|---------|-----------|-------------|-------------------|-----------| 
| Low-energy EM | electron | 0.5 MeV | — | Isolated (0.85 L to next) |
| Light hadrons | muon, strange | 94-106 MeV | 0.019 | Nearly degenerate |
| Confinement | conf_lower, charm, tau, conf_upper | 300-2000 MeV | 0.30 | Dense cluster, NON-PERTURBATIVE |
| Heavy flavor | bottom | 4.2 GeV | — | Isolated (0.47 L to W) |
| Electroweak | W, Z, Higgs, top | 80-173 GeV | 0.12 | Dense cluster |
| BSM desert | CD → GUT | 3 TeV → 3.5e15 GeV | 4.42 | EMPTY (the desert) |
| Unification | GUT → Planck | 3.5e15 → 1.2e19 GeV | 1.30 | Unknown physics |

The electroweak cluster (W/Z/H/top, L width = 0.12) is where all three couplings
are measured. The BSM desert (L width = 4.42) is where the CD betas do all the work.


## TABLE C18: FORCE DOMAIN MAP

Which forces operate at which scales.

| Scale | Strong | EM | Weak | Gravity | Notes |
|-------|--------|----|----|---------|-------|
| > M_GUT | — | — | — | ? | Unified? Single coupling? |
| CD → GUT | ✓ | ✓ | ✓ | negligible | Modified betas (25/6, -13/6, -20/3) |
| top → CD | ✓ | ✓ | ✓ | negligible | SM betas (41/10, -19/6, -7) |
| bottom → top | ✓ | ✓ | ✓ | negligible | SM betas, 5 or 6 flavors |
| confinement | BREAKS | ✓ | ✓ | negligible | alpha_s ~ O(1), no perturbation theory |
| electron → conf | residual | ✓ | ✓ (via exchange) | negligible | Hadrons, nuclear physics |
| < m_e | — | ✓ (classical) | — | negligible | Classical EM only |
| atomic → planetary | — | ✓ (binding) | — | grows | EM binds atoms, gravity grows |
| planetary → cosmic | — | negligible | — | ✓ | Gravity dominates |


## TABLE C19: THE COMPLETE RATIO TABLE

Every important ratio in the system, with its exact value and meaning.

| Ratio | Value | Exact? | Meaning |
|-------|-------|--------|---------|
| gap_SM | 218/115 = 1.8957 | exact | SM coupling convergence rate |
| gap_CD | 38/27 = 1.4074 | exact | CD coupling convergence rate |
| gap_measured | 1.3582 | derived | Actual convergence from data |
| gap_MSSM | 7/5 = 1.4000 | exact | MSSM convergence rate |
| pure_gauge_gap | 22/11 = 2 | exact | Gauge-only convergence |
| DM/baryon | (22/13)*pi = 5.3165 | L1 | Dark matter to baryon ratio |
| Omega_DM/R2 | 44/169 = 0.2604 | exact | DM density (R2 removed) |
| Omega_b/Omega_DM | 13/22 * 1/pi | — | Baryon fraction |
| CD asymmetry | db2/db1 = 15 | exact | Why Y=1/6 is optimal |
| Coupling ratio | (1/a1)/(1/a3) = 7.46 | derived | Spread at M_Z |
| H0 ratio | 674/730 = 337/365 | exact | Far/local Hubble |
| Kepler identity | 64R2² = 4pi² | exact | Orbital geometry |
| BCS gap | pi/exp(gamma) = 1.7639 | exact | Superconducting gap |
| Vena contracta | pi/(pi+2) = 0.6110 | exact | Kirchhoff orifice |
| K_J × R_K | 2/e | exact | Metrological cancellation |
| Koide K | 0.66666 ≈ 2/3 | measured | Lepton mass structure |
| Koide a² | 1.99996 ≈ 2 | measured | Amplitude parameter |


## TABLE C20: WHAT CONNECTS TO WHAT — THE ADJACENCY MATRIX

Which objects directly interact through shared derivations or relationships.

| Object | Directly Connects To | Via |
|--------|---------------------|-----|
| alpha_inv | inv_a1, inv_a2, gap_measured, sin2 prediction | Coupling extraction |
| sin2_tW | inv_a1, inv_a2, gap_measured | Coupling extraction |
| alpha_s | inv_a3, gap_measured, alpha_s prediction | Coupling extraction + running |
| b1_SM/b2_SM/b3_SM | gap_SM, decomposition, democracy | Gap ratio computation |
| db1/db2/db3_VL | b_mod, gap_CD, asymmetry | CD shifts |
| b1_mod/b2_mod/b3_mod | gap_CD, L_GUT, M_GUT, predictions | Modified running |
| b2_mod numerator (13) | DM/baryon, Omega_DM, amplification | Integer extraction |
| YM (11) | b3_SM, DM numerator 22, Omega numerator 44 | Integer extraction |
| R2 | 23 domains, Kepler, GPS, MOND, normalizations | Geometric constant |
| gap_measured | compared to gap_SM, gap_CD, gap_MSSM | The confrontation |
| M_GUT | proton lifetime, M_VL constraints | Running output |
| K_koide | a², m_tau prediction, Koide closure | Mass structure |
| H0 measurements | Hubble running, VP step, MOND a0 | Cosmological |
| GM/(rc²) | GPS, process rate, Hill spheres, escape velocity | Gravity coupling |
