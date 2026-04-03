# Toroidal Dark Matter Research Program

**Status:** Active investigation, math gate partially passed

**Foundation:** toroidal_dm_test.py (12/12 PASS), beta_unification_test.py (28/28 PASS)

**Connection:** Beta Unification Program (shared integers 44/13), Hubble Tension Program (shared R₂ geometry)

**Platform:** HOWL-PLATFORM-v1

**Rule:** Every claim backed by a script. Every failure documented. The dwarf spheroidal challenge is the hardest test — it is addressed first, not last.

---

## The Thesis

Dark matter is the boundary-amplified inertia of circulation within toroidal solitons. The amplification factor decomposes as A = (44/13)π(c/v)², where 44/13 contains the Yang-Mills integer 11 and the VL-modified SU(2) beta numerator 13 — the same integers that give Ω_DM = 44/169 in the cosmic density framework. The MOND acceleration scale a₀ ≈ cH₀/(8R₂) connects the dark matter phenomenology to the Hubble expansion through the universal geometric constant R₂ = π/4.

The thesis works for spiral galaxies (virial ratio ~3-6, correct order) and for the cosmic average (DM/baryon = (22/13)π, 0.07% match). It fails for dwarf spheroidal galaxies (required amplification 10¹¹, no known mechanism). The research program addresses this failure first because it is the most likely to kill the thesis.

---

## Stage 0: The Dwarf Spheroidal Gate

The dwarf spheroidal problem is the kill-or-cure test. If it cannot be resolved, the toroidal model is at best partial (applies to disks, not to spheroidals). The program addresses this first, not as an afterthought.

### Script 1: dwarf_tidal_stripping.py

**Purpose:** Test whether tidal stripping inflates the dwarf spheroidal DM/visible ratio by removing visible mass while preserving the dynamical signature.

**Method:**
- Published dwarf spheroidal data: Fornax, Sculptor, Draco, Ursa Minor, Sextans, Carina (the classical dwarfs orbiting the Milky Way)
- For each dwarf: current luminous mass M_L, velocity dispersion σ, half-light radius r_h, orbital parameters (pericenter, apocenter), tidal radius r_t
- Compute: tidal stripping factor = M_original / M_current, estimated from the ratio of tidal radius to half-light radius
- If M_original was 10-100× larger than M_current, the original DM/visible ratio was 10-100× smaller — possibly within the virial range
- Key check: does the stripped-mass-corrected DM/visible ratio fall on the (22/13)π = 5.32 line for any reasonable stripping history?

**Data sources:** McConnachie 2012 (dwarf galaxy catalog), Simon 2019 (dark matter in dwarfs review), Errani & Navarro 2021 (tidal stripping models)

**Libraries:** phys24_lib

**Pass condition:** At least 3 of 6 classical dwarfs have stripped-corrected DM/visible ratios within factor 3 of 5.32.

**Kill switch K1:** If ALL dwarfs retain DM/visible > 50 after maximum plausible stripping correction, the tidal explanation fails and the model cannot explain dwarfs.

### Script 2: dwarf_soliton_classification.py

**Purpose:** Test whether dwarf spheroidals are a different soliton type than disk galaxies, with a correspondingly different amplification mechanism.

**Method:**
- Disk galaxies are toroidal solitons (organized poloidal + toroidal circulation)
- Dwarf spheroidals have no disk, no organized rotation — they are pressure-supported (random motions balance gravity)
- Classify dwarfs as spherical solitons rather than toroidal
- For a spherical soliton: the amplification factor may involve R₂ (2D, spherical cross-section) rather than the full toroidal geometry
- Compute: A_sphere vs A_torus for the same boundary integers
- The spherical soliton has a different mode spectrum — all modes are radial rather than a mix of poloidal and toroidal
- For spherical modes: the boundary amplification should scale with the surface-to-volume ratio, which is 3/r for a sphere — larger for smaller systems

**Key hypothesis:** Dwarf amplification = A_galaxy × (R_galaxy/R_dwarf)^n for some power n determined by the soliton mode spectrum. If n ≈ 2, the 10⁴× ratio between galaxy and dwarf amplification factors comes from (15 kpc / 0.3 kpc)² = 2500×. Close to the required 10⁴×.

**Libraries:** phys24_lib, phys24_domain_lib (R₂ geometry), phys24_structure_lib (make_rep for mode analysis)

**Pass condition:** A scaling relation A ∝ R^(-n) with n between 1.5 and 2.5 reproduces the dwarf amplification to within factor 3.

### Script 3: dwarf_alternative_mass.py

**Purpose:** Test whether dwarf spheroidal mass estimates are wrong.

**Method:**
- Standard dwarf mass estimates use the Wolf et al. 2010 estimator: M(r_h) = 4σ²r_h/G
- This assumes dynamical equilibrium and isotropic velocity dispersion
- Test: if the velocity dispersion is anisotropic (tangential bias from tidal interaction), the mass estimate is biased upward
- Compute: for each classical dwarf, the ratio M_Wolf / M_isotropic as a function of anisotropy parameter β
- How much anisotropy is needed to bring M_dynamic down to M_visible × (1 + 5.32)?
- Is this anisotropy consistent with published proper motion measurements (Gaia DR3)?

**Data sources:** Wolf et al. 2010, Gaia DR3 proper motions for dwarf satellites

**Libraries:** phys24_lib

**Pass condition:** Required anisotropy β is within the range measured by Gaia for at least 2 of 6 dwarfs.

---

## Stage 1: The Amplification Derivation

The amplification factor A = (44/13)π(c/v)² is currently algebraic (follows from combining beta unification with the toroidal model). This stage attempts to derive the (44/13) factor from the soliton boundary geometry.

### Script 4: soliton_boundary_energy.py

**Purpose:** Compute the energy stored in a toroidal soliton boundary and test whether it produces an amplification factor of (44/13)π(c/v)².

**Method:**
- A soliton boundary is a region where the field configuration changes rapidly (like a domain wall in condensed matter)
- The boundary has surface energy density σ_boundary (energy per unit area)
- For a torus with major radius R and minor radius r: boundary area = (2π)² × R × r = 64R₂² × R × r
- Boundary energy = σ_boundary × 64R₂² × R × r
- The gravitational effect of the boundary energy adds to the visible mass
- Compute: what σ_boundary gives A = (44/13)π(c/v)²?
- Express σ_boundary in terms of the gauge coupling constants

**Key connection:** In the proton, the QCD string tension σ_QCD ≈ 1 GeV/fm sets the boundary energy. For a galactic soliton, the analogous tension involves the electroweak gauge structure — specifically b₂_mod (the SU(2) running) and b₃_mod (the SU(3) running). The ratio 20/13 = |3b₃_mod|/|b₂_mod_num| may appear naturally in the boundary tension formula.

**Libraries:** phys24_lib, phys24_domain_lib (R₂ geometry), data_4_derivation_lib (beta coefficients)

### Script 5: toroidal_mode_spectrum.py

**Purpose:** Compute the mode spectrum of a toroidal soliton and test whether the circulation modes produce the correct DM profile.

**Method:**
- A torus has two independent circulation modes: toroidal (around the major axis) and poloidal (through the cross-section)
- The mode frequencies are ω_tor = v_rot / R and ω_pol = v_pol / r
- The energy in each mode: E_n = (n + 1/2)ħω_n for quantum modes, or E = (1/2)Mv² for classical modes
- The total circulation energy = sum over all modes weighted by their occupation
- For a Milky Way torus (R = 15 kpc, r = 0.3 kpc, v_rot = 220 km/s, v_pol = 20 km/s):
  - ω_tor / ω_pol = (v_rot/R) / (v_pol/r) = (220/15000) / (20/300) = 0.015/0.067 = 0.22
  - The poloidal mode has ~4.5× higher frequency than the toroidal mode
- The energy ratio E_pol / E_tor depends on the mode occupation, which depends on the equilibrium temperature T_eff of the soliton

**Libraries:** phys24_lib, phys24_domain_lib

**Key test:** Does the mode spectrum predict a FLAT rotation curve (v = const at large r)? This requires the mode energy to increase linearly with r, compensating for the decreasing visible mass density. The mode occupation as a function of r is the critical unknown.

### Script 6: rotation_curve_from_modes.py

**Purpose:** Compute a galaxy rotation curve from the toroidal soliton mode spectrum and compare to observed curves.

**Method:**
- Use the SPARC database (Spitzer Photometry & Accurate Rotation Curves, Lelli et al. 2016): 175 galaxies with both photometry (visible mass) and rotation curves
- For each galaxy: compute the visible mass contribution to v(r) from the photometry
- Add the circulation energy contribution from the soliton mode spectrum
- Compare the total v(r) to the observed rotation curve
- The soliton parameters (R, r, mode amplitudes) are determined by the visible light distribution — no free DM halo parameters

**Data source:** SPARC database (publicly available)

**Libraries:** phys24_lib, phys24_domain_lib

**Pass condition:** The soliton mode model fits at least 50% of SPARC galaxies with χ²/dof < 2, using only parameters derived from the photometry (no free DM halo parameters).

**Kill switch K2:** If the soliton mode model cannot fit ANY SPARC galaxy without additional free parameters, the toroidal model does not reproduce rotation curves and the central prediction fails.

---

## Stage 2: The MOND Connection

The MOND acceleration a₀ ≈ cH₀/(8R₂) connects dark matter phenomenology to the Hubble rate through R₂. This stage derives a₀ from the soliton boundary framework.

### Script 7: a0_from_boundary_density.py

**Purpose:** Derive the MOND acceleration scale from the average density of soliton boundaries in the universe.

**Method:**
- If soliton boundaries are the source of apparent dark matter, the transition acceleration a₀ is where the boundary contribution equals the Newtonian contribution
- The boundary density (number per unit volume) determines a₀
- From the Hubble running: the average boundary transit rate is ~N/d_Hubble, where d_Hubble = c/H₀
- The boundary contribution to the gravitational field scales as (boundary density) × (energy per boundary)
- At the transition: a₀ = G × (boundary energy density) / (boundary spacing)
- If boundary spacing ~ c/(H₀ × N) and boundary energy involves R₂:
  - a₀ ~ G × (energy) × N × H₀ / c
  - The R₂ factor enters through the circular cross-section of the boundary
- Target: a₀ = cH₀/(8R₂)

**Libraries:** phys24_lib, phys24_domain_lib, phys24_hubble_lib

**Key connection to Hubble program:** The boundary transit count N from the Hubble running program directly determines the boundary density. If N ≈ 100 for the CMB path (from the Hubble program), the average boundary spacing is ~140 Mpc. This is close to the BAO scale (~150 Mpc) — suggesting the soliton boundaries ARE the BAO features.

### Script 8: mond_to_tully_fisher.py

**Purpose:** Derive the baryonic Tully-Fisher relation M ∝ v⁴ from the soliton mode spectrum with a₀ = cH₀/(8R₂).

**Method:**
- In MOND: for a < a₀, the effective gravitational acceleration is √(a_N × a₀) where a_N is the Newtonian acceleration
- For a circular orbit: v²/r = √(GM/r² × a₀) → v⁴ = GMa₀ → M = v⁴/(Ga₀)
- Substituting a₀ = cH₀/(8R₂): M = 8R₂v⁴/(GcH₀)
- Test: does the soliton mode spectrum naturally produce the MOND interpolation function μ(a/a₀) = a/(a + a₀)?
- The interpolation function determines HOW the transition from Newtonian to MONDian behavior occurs
- In the soliton framework: the transition occurs when the boundary amplification energy exceeds the Newtonian gravitational energy at a given radius

**Libraries:** phys24_lib, phys24_domain_lib

**Pass condition:** The soliton mode spectrum reproduces the MOND interpolation function to within 10% across the range a/a₀ = 0.01 to 100.

### Script 9: a0_sensitivity.py

**Purpose:** Test how a₀ = cH₀/(8R₂) depends on the Hubble constant.

**Method:**
- Current: H₀ = 67.4 km/s/Mpc (Planck) → a₀ = 1.042 × 10⁻¹⁰ m/s²
- If H₀ = 73.0 km/s/Mpc (SH0ES) → a₀ = 1.128 × 10⁻¹⁰ m/s²
- Measured a₀ ≈ 1.2 × 10⁻¹⁰ m/s² (empirical, from rotation curve fits)
- Which H₀ gives the best a₀ match?
- If the running curve thesis is correct, the LOCAL H₀ should be used (73.0) because a₀ is measured locally
- Local H₀ gives a₀ = 1.128 × 10⁻¹⁰, closer to measured 1.2 × 10⁻¹⁰ (6% off vs 13% off)
- This is a consistency check between the Hubble running and the MOND connection

**Libraries:** phys24_lib, phys24_hubble_lib

**Key finding expected:** Using H₀_local = 73.0 instead of H₀_CMB = 67.4 should improve the a₀ match from 15% to ~6%. This connects the Hubble running program to the MOND connection through a quantitative prediction.

---

## Stage 3: The Bullet Cluster

The Bullet Cluster (1E 0657-558) is the standard objection to all non-particle dark matter models. The gravitational lensing center is offset from the gas center, suggesting dark matter is a separate substance that passed through the collision while the gas was stripped.

### Script 10: bullet_cluster_circulation.py

**Purpose:** Test whether the toroidal circulation pattern survives a cluster collision while the gas is stripped.

**Method:**
- In a cluster collision: the gas component (baryonic, collisional) is shocked and stripped. The galaxies (collisionless) pass through. The lensing map shows mass centered on the galaxies, not the gas
- In the standard picture: dark matter particles are collisionless (like galaxies), so they pass through. The lensing mass follows the DM, not the gas
- In the toroidal picture: the soliton boundary is a field configuration, not a gas. It should behave collisionlessly — the boundary pattern passes through another boundary pattern without interacting (like two solitons in an integrable system)
- The key question: does the soliton boundary carry the gravitational lensing signal?
- Compute: the gravitational lensing from the boundary energy distribution before, during, and after a head-on collision
- Use N-body + soliton boundary model: galaxies + soliton boundaries are collisionless, gas is collisional

**Libraries:** phys24_lib, phys24_boundary_map_lib (boundary properties)

**Key test:** Does the post-collision lensing map show mass centered on the galaxy + boundary component (displaced from the gas), consistent with the observed Bullet Cluster morphology?

**Pass condition:** The model reproduces the observed lensing-gas offset of ~720 kpc to within factor 2.

**Kill switch K3:** If the soliton boundary model cannot reproduce ANY displacement between lensing and gas centers, the boundary explanation of the Bullet Cluster fails. This does not kill the full program (the Bullet Cluster is one observation) but significantly weakens the thesis.

### Script 11: bullet_soliton_survival.py

**Purpose:** Test whether a toroidal soliton survives a high-velocity collision.

**Method:**
- Soliton collisions in integrable systems: two solitons pass through each other and emerge unchanged (the KdV soliton property)
- In non-integrable systems: solitons can merge, scatter, or destroy each other
- The key parameter: the collision velocity relative to the soliton internal velocity
- For the Bullet Cluster: collision velocity ~ 4700 km/s, internal cluster velocity dispersion ~ 1000 km/s
- The collision velocity is 4.7× the internal velocity — the collision is supersonic in the soliton frame
- Compute: does a toroidal soliton maintain its boundary structure after a supersonic collision?
- Use the analogy to plasma physics: tokamak disruptions occur when the perturbation velocity exceeds the Alfvén speed. What is the analogous speed for a gravitational soliton?

**Libraries:** phys24_lib

### Script 12: cluster_dm_profile.py

**Purpose:** Compare the toroidal model's DM profile prediction to observed cluster DM profiles from gravitational lensing.

**Method:**
- Published cluster DM profiles from lensing: NFW profile fits, concentration parameters
- In the toroidal model: the DM profile follows the circulation energy distribution, which follows the velocity dispersion profile
- For a cluster: the velocity dispersion profile σ(r) is measurable from galaxy redshifts
- Predict: DM(r) ∝ σ(r)² × (boundary amplification at r)
- Compare to NFW fits from Umetsu et al. 2014 (CLASH lensing survey)

**Libraries:** phys24_lib

**Pass condition:** The σ(r)-based DM profile matches the NFW fit to within 20% in the radial range 0.1-2 Mpc for at least 5 of 20 CLASH clusters.

---

## Stage 4: The Cosmological Connection

Connecting the galactic-scale toroidal model to the cosmic-scale beta unification results.

### Script 13: cosmic_dm_from_galaxy_census.py

**Purpose:** Test whether the cosmic DM/baryon ratio (22/13)π can be derived from a census of galaxy types weighted by their individual amplification factors.

**Method:**
- The cosmic DM/baryon ratio is the volume-weighted average of individual galaxy DM/baryon ratios
- Galaxy luminosity function: φ(L) gives the number density of galaxies per luminosity bin
- Each galaxy type has a characteristic DM fraction (from Script 5's morphology analysis)
- Compute: <DM/baryon>_cosmic = Σ (galaxy type fraction × DM/baryon per type)
- Does the volume-weighted average give (22/13)π = 5.317?

**Libraries:** phys24_lib

**Key test:** The cosmic ratio is a population average, not a universal constant. If the toroidal model gives different DM/baryon for different galaxy types but the census-weighted average matches (22/13)π, the model is self-consistent.

### Script 14: omega_chain_from_amplification.py

**Purpose:** Derive the full Omega chain (Ω_b, Ω_DM, Ω_matter, Ω_DE) from the amplification factor.

**Method:**
- From beta unification Set B: Ω_b = 2/(13π), Ω_DM = 44/169
- From the toroidal model: Ω_DM = Ω_b × (22/13)π, where (22/13) is the amplification ratio and π is the geometry
- Test: does the amplification decomposition A = (44/13)π(c/v)² at the cosmic average velocity reproduce Ω_DM = 44/169?
- What is the "cosmic average velocity" v_cosmic that satisfies A × v² / (2c²) × Ω_b = Ω_DM?
- Solve: v_cosmic = c × √(2 × Ω_DM / (A × Ω_b)) — but this is circular if A depends on v
- The resolution: at the cosmic level, A × v²/(2c²) = (22/13)π is a constant. The cosmic average IS the formula, not a derived quantity

**Libraries:** phys24_lib

### Script 15: bao_as_soliton_boundaries.py

**Purpose:** Test whether the BAO scale (~150 Mpc) corresponds to the average soliton boundary spacing inferred from the Hubble running.

**Method:**
- From the Hubble running: if N ≈ 100 boundaries over the CMB distance (~14 Gpc comoving), the average spacing is ~140 Mpc
- The BAO scale is ~150 Mpc (the sound horizon at recombination)
- The near-coincidence (140 vs 150 Mpc, 7% difference) may indicate that soliton boundaries form at the BAO scale
- Test: does the BAO peak position in the galaxy correlation function correspond to the soliton boundary spacing?
- Compute: if boundary spacing = c/(H₀ × N), what N gives 150 Mpc? Answer: N = c/(H₀ × 150 Mpc) ≈ 93
- Compare to the N ≈ 100 from the Hubble running (which gives r matching α²π²(20/13))

**Libraries:** phys24_lib, phys24_hubble_lib

**Key finding expected:** N ≈ 93-100 from two independent routes (Hubble running and BAO spacing). If they agree, the soliton boundaries are the BAO features.

---

## Stage 5: The Orientation Track Connection

From the notebook: the T_eff/χ ratio that determines galaxy morphology also determines the circulation energy, predicting three regimes of dark matter fraction.

### Script 16: orientation_track_dm.py

**Purpose:** Map the three orientation tracks to three DM fraction regimes.

**Method:**
- Track 1 (locked, low T_eff/χ): compact objects, maximum boundary amplification per unit mass. Neutron stars, white dwarfs. DM fraction: negligible (self-gravity dominates, no extended circulation)
- Track 2 (aligned, moderate T_eff/χ): disk galaxies, organized circulation. DM fraction: ~80-90%. The toroidal model applies directly
- Track 3 (random, high T_eff/χ): spheroidals and clusters, random motions. DM fraction: 85-99%. The spherical soliton model from Script 2 applies
- For each track: compute the predicted DM fraction from the amplification model
- Compare to observed morphology-DM correlation (Table from the experiment script Section 5)

**Libraries:** phys24_lib

### Script 17: thickness_dm_correlation.py

**Purpose:** Test the specific prediction P1 from the notebook: DM fraction correlates with disk thickness.

**Method:**
- Use the DiskMass Survey (Bershady et al. 2010): measurements of disk scale height and DM fraction for ~30 face-on spirals
- For each galaxy: disk scale height h, disk scale length R_d, ratio h/R_d (flatness parameter)
- Plot: DM fraction within 2.2 scale lengths vs h/R_d
- Test: is there a statistically significant correlation?
- The model predicts: thinner disks (lower h/R_d) → less circulation energy → less DM in the inner region

**Data source:** DiskMass Survey, Bershady et al. 2010

**Libraries:** phys24_lib

**Pass condition:** Pearson correlation coefficient r > 0.3 (positive correlation between thickness and DM fraction) at p < 0.05.

---

## Stage 6: Cross-Validation

### Script 18: sparc_radial_acceleration.py

**Purpose:** Test the Radial Acceleration Relation (RAR) from the toroidal model.

**Method:**
- The RAR (McGaugh et al. 2016): the observed gravitational acceleration g_obs correlates tightly with the baryonic acceleration g_bar across 2693 data points from 153 SPARC galaxies
- The relation is g_obs = g_bar / (1 - exp(-√(g_bar/a₀))) — the MOND interpolation function
- In the toroidal model: g_obs = g_bar + g_circulation, where g_circulation is the boundary-amplified circulation energy contribution
- Test: does g_circulation = A(r) × v(r)²/(2c²) × g_bar reproduce the RAR?
- The key: A(r) must vary with radius to produce the correct interpolation function

**Libraries:** phys24_lib, phys24_domain_lib

**Pass condition:** The soliton model reproduces the RAR scatter of 0.13 dex (the observed intrinsic scatter from McGaugh et al.).

### Script 19: pioneer_anomaly.py

**Purpose:** Test whether the Pioneer anomaly (anomalous deceleration of Pioneer 10/11 spacecraft) is consistent with the local soliton boundary.

**Method:**
- The Pioneer anomaly: an unexplained sunward acceleration of (8.74 ± 1.33) × 10⁻¹⁰ m/s² detected in Pioneer 10/11 tracking data beyond 20 AU
- This was ultimately attributed to thermal radiation pressure in 2012 (Turyshev et al.)
- However: the anomaly magnitude is remarkably close to a₀ ≈ 1.2 × 10⁻¹⁰ m/s² and to cH₀/(8R₂) ≈ 1.04 × 10⁻¹⁰ m/s²
- The notebook (Section 9) suggested this could be the local manifestation of the solar system soliton boundary
- Test: does the soliton boundary model predict an acceleration at ~20 AU that matches the Pioneer anomaly magnitude, even though the anomaly is now attributed to thermal effects?
- If the soliton boundary contribution is ~10⁻¹⁰ m/s², it is within the thermal recoil uncertainty and would be undetectable against the thermal background

**Libraries:** phys24_lib

**Note:** This is a historical curiosity, not a primary test. The Pioneer anomaly is considered resolved. But the magnitude coincidence with a₀ is worth documenting.

### Script 20: dm_detection_null_consistency.py

**Purpose:** Test whether 40+ years of null dark matter particle detection results are consistent with the toroidal model.

**Method:**
- Compile null detection results: LUX, XENON1T, XENONnT, PandaX-4T, LZ, SuperCDMS, DAMA/LIBRA (contested), COSINE-100
- For each experiment: the upper limit on DM-nucleon cross-section σ as a function of DM particle mass m_χ
- In the standard picture: these limits constrain the mass and coupling of DM particles
- In the toroidal picture: there ARE no DM particles. All null results are expected
- Test: is the toroidal model consistent with ALL null results simultaneously? (Yes, trivially — no particles means no detection)
- More interestingly: are there any positive signals (DAMA annual modulation, XENON1T electron recoil excess) that the toroidal model would need to explain as non-DM physics?

**Libraries:** phys24_lib

---

## Stage 7: Integration and Publication

### Script 21: toroidal_dm_consolidated.py

**Purpose:** The reference script. Everything computed, everything checked, full provenance.

**Libraries:** All platform libraries

### Script 22: toroidal_dm_diagrams_expanded.py

**Purpose:** Expand the 20-figure diagram set to 30+ figures covering all findings from Stages 0-6.

**Additional figures:**
- Dwarf tidal stripping correction curves
- Soliton mode spectrum for MW torus
- Rotation curve fit from modes vs observed (SPARC sample)
- a₀ vs H₀ sensitivity curve
- Bullet Cluster lensing map (model prediction)
- BAO scale vs soliton boundary spacing
- Orientation track → DM fraction mapping
- Thickness-DM correlation scatter plot
- RAR from soliton model vs observed
- Pioneer anomaly magnitude comparison
- DM detection null result summary

**Libraries:** data_5_diagram_lib, all platform libraries

---

## Kill Switches

| ID | Condition | Script | Impact | Recovery |
|---|---|---|---|---|
| K1 | Tidal stripping cannot bring dwarfs below DM/visible = 50 | 1 | Dwarf explanation fails | Try soliton classification (Script 2) |
| K2 | Soliton mode model cannot fit ANY SPARC galaxy | 6 | Rotation curve prediction fails | Model is wrong for disks |
| K3 | Bullet Cluster lensing offset not reproducible | 10 | Bullet Cluster explanation fails | Model is partial (not universal) |
| K4 | Thickness-DM correlation not found (r < 0.1) | 17 | P1 prediction fails | Morphology connection severed |
| K5 | RAR scatter from soliton model > 0.3 dex (2× observed) | 18 | Model too imprecise | Need better mode spectrum |
| K6 | DM particles detected with matching cross-section | 20 | Particle DM exists | Toroidal may coexist with particles |
| K7 | a₀ = cH₀/(8R₂) fails by >50% with improved H₀ data | 9 | MOND-R₂ connection breaks | Coincidence, not structure |

---

## Falsification Targets

| Observable | Model Prediction | Current Data | Excluded at 2σ if | Key Experiment |
|---|---|---|---|---|
| DM/visible vs thickness | Positive correlation | Qualitative match | No correlation (p > 0.2) | DiskMass Survey |
| Rotation curve shape | From soliton modes only | SPARC: 175 galaxies | χ²/dof > 3 for all galaxies | SPARC fits |
| a₀ | cH₀/(8R₂) = 1.04-1.13 × 10⁻¹⁰ | 1.2 ± 0.2 × 10⁻¹⁰ | a₀ outside [0.7, 1.7] × 10⁻¹⁰ | Rotation curve analysis |
| Bullet Cluster offset | ~500-1000 kpc | ~720 kpc observed | Offset < 200 kpc from model | Lensing reanalysis |
| DM particle detection | None (no particles) | Null at all experiments | Any confirmed detection | LZ, XENONnT, next-gen |
| BAO = soliton spacing | ~140 Mpc if N=100 | BAO = 150 ± 2 Mpc | N < 80 or N > 130 | DESI BAO |
| Cosmic DM/baryon | (22/13)π = 5.317 | 5.320 ± 0.065 | Outside [5.19, 5.45] | Planck reanalysis |
| Dwarf DM after stripping | < 50 | Currently 10-1000 | > 50 for all dwarfs after max strip | Gaia DR4 orbits |

---

## Script Inventory

| # | Script Name | Stage | Lines (est) | Libraries | Blocking? |
|---|---|---|---|---|---|
| 1 | dwarf_tidal_stripping.py | 0 | 120 | phys24_lib | YES (K1) |
| 2 | dwarf_soliton_classification.py | 0 | 100 | phys24_lib, domain_lib, structure_lib | No |
| 3 | dwarf_alternative_mass.py | 0 | 100 | phys24_lib | No |
| 4 | soliton_boundary_energy.py | 1 | 120 | phys24_lib, domain_lib, derivation_lib | No |
| 5 | toroidal_mode_spectrum.py | 1 | 150 | phys24_lib, domain_lib | No |
| 6 | rotation_curve_from_modes.py | 1 | 200 | phys24_lib, domain_lib | K2 |
| 7 | a0_from_boundary_density.py | 2 | 100 | phys24_lib, domain_lib, hubble_lib | No |
| 8 | mond_to_tully_fisher.py | 2 | 100 | phys24_lib, domain_lib | No |
| 9 | a0_sensitivity.py | 2 | 80 | phys24_lib, hubble_lib | No |
| 10 | bullet_cluster_circulation.py | 3 | 150 | phys24_lib, boundary_lib | K3 |
| 11 | bullet_soliton_survival.py | 3 | 120 | phys24_lib | No |
| 12 | cluster_dm_profile.py | 3 | 120 | phys24_lib | No |
| 13 | cosmic_dm_from_galaxy_census.py | 4 | 100 | phys24_lib | No |
| 14 | omega_chain_from_amplification.py | 4 | 80 | phys24_lib | No |
| 15 | bao_as_soliton_boundaries.py | 4 | 100 | phys24_lib, hubble_lib | No |
| 16 | orientation_track_dm.py | 5 | 100 | phys24_lib | No |
| 17 | thickness_dm_correlation.py | 5 | 120 | phys24_lib | K4 |
| 18 | sparc_radial_acceleration.py | 6 | 150 | phys24_lib, domain_lib | K5 |
| 19 | pioneer_anomaly.py | 6 | 80 | phys24_lib | No |
| 20 | dm_detection_null_consistency.py | 6 | 80 | phys24_lib | No |
| 21 | toroidal_dm_consolidated.py | 7 | 200 | all libraries | No |
| 22 | toroidal_dm_diagrams_expanded.py | 7 | 500 | all libraries + diagram_lib | No |

**Total estimated lines:** ~2,970 across 22 scripts.

---

## Connection to Other Programs

| This Program | Other Program | Shared Element |
|---|---|---|
| A = (44/13)π(c/v)² | Beta Unification | Integer ratio 44/13 |
| a₀ = cH₀/(8R₂) | Hubble Tension | H₀ value and R₂ geometry |
| N ≈ 100 boundary transits | Hubble Tension | Boundary transit count |
| BAO = soliton boundary spacing | Hubble Tension | 140-150 Mpc scale |
| (1−r) = α²π²(20/13) | Beta Unification Stage 1 | Per-transit correction |
| Soliton mode spectrum | Boundary Map Library | Boundary stack infrastructure |
| R₂ in amplification | Domain Library | R₂ across 15+ domains |

Three programs share the integer 13 (|b₂_mod_num|), the constant R₂ = π/4, and the boundary transit count N ≈ 100. If all three programs succeed, they describe a single unified picture: gauge group integers determine the boundary structure, boundaries determine both the Hubble running and the dark matter amplification, and the universal geometry R₂ appears in the connection between them.

---

## Papers This Program Would Produce

**If Stage 0 resolves dwarfs + Stage 1 derives amplification:**
- PHYS-XX: "Toroidal Dark Matter: Circulation Inertia with Boundary Amplification from Gauge Group Integers" — the full paper with derivation, rotation curves, and dwarf resolution.

**If Stage 0 resolves dwarfs but Stage 1 fails:**
- PHYS-XX: "Dark Matter as Circulation Inertia: Virial Evidence and the (22/13)π Formula" — empirical paper documenting the virial success and the beta unification connection without a derivation.

**If Stage 3 resolves the Bullet Cluster:**
- PHYS-XX: "Soliton Boundary Survival in Cluster Collisions: The Bullet Cluster as a Boundary-Dynamics Test" — the Bullet Cluster paper.

**If Stage 0 fails (dwarfs unexplainable):**
- DISC-XX: "Toroidal Dark Matter: Virial Success for Disks, Failure for Spheroidals" — honest partial result documenting where the model works and where it doesn't.

**If K2 triggers (rotation curves fail):**
- DISC-XX: "The Toroidal Soliton Mode Spectrum: Why It Cannot Reproduce Flat Rotation Curves" — null result paper.

**If K6 triggers (DM particles detected):**
- DISC-XX: "Dark Matter Particles and Toroidal Circulation: Coexistence or Replacement?" — reassessment paper.

Every outcome produces a paper. No work is wasted.

---

## Null Result Registry

| Potential Null | Script | What It Would Mean | Status |
|---|---|---|---|
| Tidal stripping cannot fix dwarfs | 1 | Toroidal model is partial (disks only) | UNTESTED |
| Soliton scaling cannot explain dwarf A | 2 | No single mechanism spans all morphologies | UNTESTED |
| Mass estimates are robust against anisotropy | 3 | Dwarf DM fractions are real, not artifacts | UNTESTED |
| Boundary energy gives wrong A | 4 | First-principles derivation fails | UNTESTED |
| Mode spectrum cannot produce flat v(r) | 6 | Central prediction fails (K2) | UNTESTED |
| Bullet Cluster offset not reproducible | 10 | Model fails standard test (K3) | UNTESTED |
| No thickness-DM correlation | 17 | Prediction P1 fails (K4) | UNTESTED |
| RAR scatter too large | 18 | Model too imprecise (K5) | UNTESTED |
| DM particles detected | 20 | Particle DM exists (K6) | 40 years of null results |
| a₀ ≠ cH₀/(8R₂) with improved data | 9 | MOND-R₂ coincidence, not structure (K7) | Current: 15% match |
| Virial theorem fails for spirals | — | Already tested: works (ratio ~2.8) | TESTED — PASSES |
| Frame dragging sufficient | — | Already tested: negligible (10⁻¹³) | TESTED — FAILS |

---

## Timeline

| Stage | Scripts | Sessions | Blocking Dependencies |
|---|---|---|---|
| 0: Dwarf spheroidal gate | 1, 2, 3 | 1-2 | None (address first) |
| 1: Amplification derivation | 4, 5, 6 | 2-3 | Stage 0 (need to know if dwarfs are fatal) |
| 2: MOND connection | 7, 8, 9 | 1 | Independent of Stage 0 |
| 3: Bullet Cluster | 10, 11, 12 | 1-2 | Independent |
| 4: Cosmological connection | 13, 14, 15 | 1 | Stages 1-2 (need amplification model) |
| 5: Orientation tracks | 16, 17 | 1 | Stage 0 (need morphology model) |
| 6: Cross-validation | 18, 19, 20 | 1-2 | Stages 1-2 (need full model) |
| 7: Integration | 21, 22 | 1-2 | Stages 0-6 (partial results OK) |
| **Total** | **22 scripts** | **7-13 sessions** | **Stage 0 first** |

---

*Toroidal Dark Matter Research Program. 22 scripts, 7 stages, 7 kill switches. Stage 0 (dwarf spheroidal gate) addressed first. Connected to Beta Unification via 44/13 and to Hubble Tension via R₂ and boundary count N. Every outcome produces a paper. The dwarf spheroidal challenge is the strongest objection and is tested first, not last. April 3, 2026.*

---

# Toroidal Dark Matter Research Program — Supporting Tables

**Companion to:** Toroidal Dark Matter Research Program

**Date:** April 3, 2026

---

## Table 1: The Integer Pool (from Beta Unification)

Every integer appearing in the toroidal DM framework, with its derivation chain.

| Integer | Symbol | Derivation | Fraction Source | Appears In |
|---|---|---|---|---|
| 11 | YM | Yang-Mills: −(11/3)C₂(G) | Group theory | A decomposition (as 44 = 4×11), Ω_DM |
| 13 | \|b₂_mod_num\| | b₂_SM + Δb₂_CD = −19/6 + 1 = −13/6 | b2_mod from phys24_lib | A decomposition, Ω_b, Ω_DM, DM/baryon |
| 22 | 2×YM | 2 × 11 | Derived | DM/baryon = (22/13)π |
| 44 | 4×YM | 4 × 11. Also 2×22 | Derived | A = (44/13)π(c/v)², Ω_DM = 44/169 |
| 169 | 13² | \|b₂_mod_num\|² | Derived | Ω_DM = 44/169 |
| 20 | \|3b₃_mod\| | b₃_mod = −20/3 | b3_mod from phys24_lib | H₀ correction (20/13 ratio) |

---

## Table 2: The Amplification Factor

| Component | Value | Origin | Library Source |
|---|---|---|---|
| 44/13 | 3.3846... | (4×YM) / \|b₂_mod_num\| | b2_mod from phys24_lib, YM = 11 |
| π | 3.14159... | Circular geometry = 4R₂ | R2_f from phys24_lib |
| (c/v)² at 220 km/s | 1.856 × 10⁶ | Relativistic factor | c = 299792458 m/s |
| A at 220 km/s | 1.974 × 10⁷ | Full product | Computed |
| (c/v)² at 1000 km/s | 8.987 × 10⁴ | Cluster velocity | Computed |
| A at 1000 km/s | 9.563 × 10⁵ | Cluster amplification | Computed |
| (c/v)² at 10 km/s | 8.987 × 10⁸ | Dwarf velocity | Computed |
| A at 10 km/s | 9.563 × 10⁹ | Dwarf amplification (if model held) | Computed |
| A_required for dwarfs | 1.80 × 10¹¹ | From DM/visible = 100 | Computed |

**Key identity:** A × v²/(2c²) = (44/13)π(c/v)² × v²/(2c²) = (44/13)π/2 = (22/13)π = 5.317. The product is velocity-independent. The DM/baryon ratio is a universal constant in this framework.

---

## Table 3: Velocity and Kinetic Energy Across Scales

| System | v (km/s) | v²/c² | Naive m_eff/M | Required A | A/A_proton |
|---|---|---|---|---|---|
| Earth orbit | 30 | 1.00 × 10⁻⁸ | 5.01 × 10⁻⁹ | 2.13 × 10⁹ | 2.15 × 10⁷ |
| Solar orbit | 220 | 5.39 × 10⁻⁷ | 2.69 × 10⁻⁷ | 1.97 × 10⁷ | 2.00 × 10⁵ |
| Vertical oscillation | 20 | 4.45 × 10⁻⁹ | 2.23 × 10⁻⁹ | 2.39 × 10⁹ | 2.41 × 10⁷ |
| Cluster dispersion | 1000 | 1.11 × 10⁻⁵ | 5.56 × 10⁻⁶ | 9.56 × 10⁵ | 9.66 × 10³ |
| Dwarf dispersion | 10 | 1.11 × 10⁻⁹ | 5.56 × 10⁻¹⁰ | 1.80 × 10¹¹ | 1.82 × 10⁹ |
| Proton (QCD, reference) | — | — | — | 99 | 1 |

**Pattern:** Required A scales as 1/v² because A × v²/(2c²) = constant = (22/13)π.

---

## Table 4: Galaxy Morphology and Dark Matter

| Type | v_rot (km/s) | σ (km/s) | v_total (km/s) | v²/c² | DM Fraction | DM/Visible | Virial Works? |
|---|---|---|---|---|---|---|---|
| Thin spiral (Sb/Sc) | 220 | 20 | 221 | 5.43 × 10⁻⁷ | 0.80 | 4.0 | Yes |
| Thick spiral (Sa) | 200 | 40 | 204 | 4.63 × 10⁻⁷ | 0.85 | 5.7 | Yes |
| Elliptical (E) | 50 | 200 | 206 | 4.73 × 10⁻⁷ | 0.90 | 9.0 | Marginal |
| Galaxy cluster | 0 | 1000 | 1000 | 1.11 × 10⁻⁵ | 0.85 | 5.7 | Yes |
| Dwarf spheroidal | 0 | 10 | 10 | 1.11 × 10⁻⁹ | 0.99 | 99 | NO |

**Prediction P1:** DM fraction correlates with disk thickness (proxy for circulation amplitude). Thin disks → lower DM fraction in inner regions. Thick disks and spheroidals → higher DM fraction.

**Challenge:** Dwarf spheroidals have the lowest velocity but the highest DM fraction. The correlation is non-monotonic.

---

## Table 5: Virial Theorem Results

| System | M_visible (M_☉) | R (kpc) | v (km/s) | M_virial (M_☉) | Virial/Visible | Expected | Match? |
|---|---|---|---|---|---|---|---|
| Milky Way | 6 × 10¹⁰ | 15 | 220 | 1.69 × 10¹¹ | 2.81 | ~6.25 | Order correct |
| M31 | 1 × 10¹¹ | 20 | 250 | 2.89 × 10¹¹ | 2.89 | ~6 | Order correct |
| Typical cluster | 5 × 10¹³ | 3000 | 1000 | 6.96 × 10¹⁴ | 13.9 | ~6 | High (known) |
| Fornax dSph | 2 × 10⁷ | 0.7 | 12 | 2.39 × 10⁸ | 11.9 | ~100 | FAILS (10×) |
| Draco dSph | 3 × 10⁵ | 0.3 | 9 | 5.64 × 10⁷ | 188 | ~300 | Order correct* |

*Draco virial ratio is closer to observed because it is the most DM-dominated system. The virial mass is mostly kinetic energy of random motions.

---

## Table 6: The MOND Connection

| Quantity | Value | Source | Library |
|---|---|---|---|
| a₀ (MOND empirical) | 1.2 × 10⁻¹⁰ m/s² | Begeman et al. 1991, McGaugh 2004 | — |
| cH₀/(2π) with H₀ = 67.4 | 1.042 × 10⁻¹⁰ m/s² | Planck CMB | phys24_lib |
| cH₀/(8R₂) with H₀ = 67.4 | 1.042 × 10⁻¹⁰ m/s² | Same (8R₂ = 2π) | phys24_lib |
| cH₀/(2π) with H₀ = 73.0 | 1.128 × 10⁻¹⁰ m/s² | SH0ES local | phys24_lib |
| Ratio a₀/[cH₀/(2π)] at 67.4 | 1.152 | 15.2% off | Computed |
| Ratio a₀/[cH₀/(2π)] at 73.0 | 1.064 | 6.4% off | Computed |

**Key finding:** Using H₀_local (73.0) instead of H₀_CMB (67.4) improves the a₀ match from 15% to 6%. This is consistent with the Hubble running program: a₀ is measured locally, so the local H₀ should be used.

**R₂ form:** a₀ = cH₀/(8R₂). Since 8R₂ = 2π, this is algebraically identical to a₀ = cH₀/(2π). The R₂ form makes the connection to the 15-domain geometry explicit.

---

## Table 7: The Tully-Fisher Relation

| Galaxy | v_flat (km/s) | M_baryon (M_☉) observed | M_baryon from v⁴/(Ga₀) | Match? |
|---|---|---|---|---|
| DDO 154 (dwarf) | 50 | ~5 × 10⁸ | 4.7 × 10⁸ | Yes |
| NGC 2403 (Sc) | 130 | ~8 × 10⁹ | 2.2 × 10¹⁰ | Factor 3 |
| Milky Way | 220 | ~6 × 10¹⁰ | 1.8 × 10¹¹ | Factor 3 |
| UGC 2885 (Sb) | 300 | ~4 × 10¹¹ | 6.1 × 10¹¹ | Factor 1.5 |

**Note:** The v⁴/(Ga₀) formula using a₀ = 1.2 × 10⁻¹⁰ systematically overpredicts by factor 2-3 for intermediate galaxies. The correct baryonic TF relation uses a normalization constant that absorbs this factor. The v⁴ SCALING is the prediction, not the normalization.

**R₂ form:** M = 8R₂v⁴/(GcH₀). The R₂ connects mass to velocity through the universal circular geometry.

---

## Table 8: Frame Dragging Magnitude

| System | v_rot (km/s) | M (M_☉) | R (kpc) | R_S (m) | R_S/R | v²/c² | Frame drag / Newton |
|---|---|---|---|---|---|---|---|
| Earth | 0.465 | 3.0 × 10⁻⁶ | — | 0.0089 | ~10⁻²⁶ | 2.4 × 10⁻¹² | ~10⁻³⁸ |
| Milky Way | 220 | 6 × 10¹⁰ | 15 | 1.77 × 10¹⁴ | 3.83 × 10⁻⁷ | 5.39 × 10⁻⁷ | 2.06 × 10⁻¹³ |
| Galaxy cluster | 1000 | 5 × 10¹⁴ | 3000 | 1.48 × 10¹⁸ | 1.60 × 10⁻⁵ | 1.11 × 10⁻⁵ | 1.78 × 10⁻¹⁰ |

**Conclusion:** Frame dragging is negligible at ALL astrophysical scales. It cannot produce dark matter effects. The boundary amplification mechanism, if it exists, operates through a channel other than GR frame dragging.

---

## Table 9: Geometric Ratios

| Geometry | Formula | Thin Disk (R/r=50) | Thick Disk (R/r=15) | Cosmic DM/baryon |
|---|---|---|---|---|
| V_sphere/V_torus | 2(R/r)²/(3π) | 530.5 | 47.7 | 5.32 |
| Surface ratio | 4(R/r)/π | 63.7 | 19.1 | — |
| Aspect ratio | R/r | 50 | 15 | — |
| V_torus/V_sphere | 3π/(2(R/r)²) | 0.00189 | 0.0209 | — |

**Finding:** Pure V_sphere/V_torus overshoots for thin disks (530 vs 5.3) but is closer for thick disks (48 vs 5.3). The geometric ratio alone does not explain the DM/baryon ratio — but it sets the right order of magnitude for thick systems.

**Required effective aspect ratio for DM/baryon = 5.32:** R/r = √(5.32 × 3π/2) = √(25.07) = 5.0. A torus with aspect ratio 5 would give the correct geometric DM/baryon ratio. This is a very fat torus — more like a ring than a disk.

---

## Table 10: Proton Parallel

| Property | Proton | Galaxy (spiral) | Ratio |
|---|---|---|---|
| Total mass | 938.3 MeV | ~3.6 × 10¹¹ M_☉ (virial) | — |
| Constituent mass | ~9 MeV (quarks) | ~6 × 10¹⁰ M_☉ (visible) | — |
| Pattern energy | ~929 MeV (QCD binding) | ~3 × 10¹¹ M_☉ (DM) | — |
| Pattern fraction | 99% | ~84% | — |
| Amplification factor | 99 | 1.97 × 10⁷ | 2 × 10⁵ |
| Binding mechanism | QCD confinement | Toroidal circulation (proposed) | Different |
| Scale | 1 fm | 30 kpc | 3 × 10²² |
| Verified? | Yes (QCD lattice) | No (proposed) | — |

**The parallel is structural, not numerical.** Both systems have mass dominated by pattern energy rather than constituent mass. The mechanisms are entirely different (QCD vs toroidal geometry). The amplification factors differ by 5 orders of magnitude. The conceptual point is that "mass from pattern" is already established physics — the proton demonstrates it.

---

## Table 11: Dwarf Spheroidal Data

| Dwarf | M_L (M_☉) | σ (km/s) | r_h (pc) | M_dyn (M_☉) | DM/Visible | Distance (kpc) | Tidal? |
|---|---|---|---|---|---|---|---|
| Fornax | 2 × 10⁷ | 11.7 | 710 | 1.6 × 10⁸ | 7 | 147 | Weak |
| Sculptor | 2.3 × 10⁶ | 9.2 | 283 | 7.0 × 10⁷ | 30 | 86 | Moderate |
| Draco | 2.9 × 10⁵ | 9.1 | 221 | 5.4 × 10⁷ | 186 | 76 | Strong |
| Ursa Minor | 2.9 × 10⁵ | 9.5 | 181 | 4.8 × 10⁷ | 166 | 78 | Strong |
| Carina | 3.8 × 10⁵ | 6.6 | 250 | 3.2 × 10⁷ | 84 | 105 | Strong |
| Sextans | 4.4 × 10⁵ | 7.9 | 695 | 1.3 × 10⁸ | 295 | 86 | Moderate |

**Sources:** Walker et al. 2009, Wolf et al. 2010, McConnachie 2012.

**Pattern:** The most tidally affected dwarfs (Draco, Ursa Minor, Sextans) have the highest DM/visible ratios. This is consistent with tidal stripping inflating the ratio by removing visible mass — but the effect may not be large enough.

**Tidal stripping estimate:** For Draco (strongest tidal interaction, DM/vis = 186), if tidal stripping removed 90% of original visible mass, the original ratio was 186 × 0.1 = 18.6. Still much larger than the cosmic 5.32. To reach 5.32: need stripping factor of 186/5.32 = 35×. Original M_L = 35 × 2.9 × 10⁵ = 1 × 10⁷ M_☉. This is plausible for a pre-stripping dwarf but requires strong stripping.

---

## Table 12: Bullet Cluster Parameters

| Parameter | Value | Source |
|---|---|---|
| Collision velocity | ~4700 km/s | Markevitch et al. 2004 |
| Main cluster mass | ~1.5 × 10¹⁵ M_☉ | Lensing |
| Sub-cluster mass | ~1.5 × 10¹⁴ M_☉ | Lensing |
| Gas-lensing offset | ~720 kpc | Clowe et al. 2006 |
| Gas fraction (main) | ~15% | X-ray |
| DM fraction (main) | ~85% | Lensing − gas |
| Collision v / v_disp | ~4.7 | Supersonic in cluster frame |

**The challenge:** In the standard picture, DM particles are collisionless and pass through. Gas is collisional and gets shocked. The lensing follows the DM, displaced from the gas. In the toroidal picture: the soliton boundary must also be effectively collisionless — it must pass through the other cluster's boundary without disruption. This is the soliton survival question (Script 11).

**Analogy:** In the KdV equation (integrable system), two solitons pass through each other and emerge unchanged. In non-integrable systems, soliton collisions can be destructive. Whether gravitational solitons are closer to KdV (survive) or to non-integrable (disrupted) determines whether the Bullet Cluster is compatible with the toroidal model.

---

## Table 13: BAO Scale vs Soliton Boundary Spacing

| Method | Spacing (Mpc) | Source | N implied |
|---|---|---|---|
| BAO measurement | 150 ± 2 | Planck 2018, DESI 2024 | — |
| Hubble running N=93 | 150 | c/(H₀ × 93) | 93 |
| Hubble running N=100 | 140 | c/(H₀ × 100) | 100 |
| Hubble running N=80 | 175 | c/(H₀ × 80) | 80 |
| Average void size (SDSS) | 30-80 | Sutter et al. 2012 | — |
| Average filament spacing | 50-100 | Cautun et al. 2014 | — |
| Average cluster spacing | 50-100 | Abell catalog | — |

**Finding:** The BAO scale (150 Mpc) matches the soliton boundary spacing at N ≈ 93, close to the N ≈ 100 implied by the theoretical r from beta unification. The individual structure scales (voids, filaments, clusters at 30-100 Mpc) are smaller than the BAO scale, suggesting that "soliton boundary" corresponds to the BAO feature (the imprint of the sound horizon at recombination), not to individual voids or filaments.

**If BAO = soliton boundary:** The soliton boundaries formed at recombination (z ≈ 1100) when the universe transitioned from plasma to neutral gas. The boundaries are fossil structures — they are where the sound waves froze. The dark matter amplification occurs at these frozen boundaries because the density contrast creates the field configuration change that amplifies circulation inertia.

---

## Table 14: The R₂ Budget

Where R₂ = π/4 appears in the toroidal DM framework.

| Appearance | Formula | Role | Connection |
|---|---|---|---|
| Amplification factor | A = (44/13) × 4R₂ × (c/v)² | π = 4R₂ geometric factor | domain_lib: 15+ domains |
| MOND acceleration | a₀ = cH₀/(8R₂) | Circular geometry normalization | domain_lib: circular domains |
| Tully-Fisher | M = 8R₂v⁴/(GcH₀) | Mass-velocity scaling | domain_lib: pipe flow analog |
| Toroidal cross-section | A_cross = R₂ × d² | Disk cross-section area | domain_lib: beam, pipe, wire |
| Toroidal volume | V = 8R₂² × R × r² | Torus volume via R₂ | domain_lib: geometric |
| Cosmic Ω_b | Ω_b = 2/(13 × 4R₂) | Baryon density normalization | beta unification Set B |
| DM/baryon π cancellation | (22/13) × 4R₂ × 2/(13 × 4R₂) = 44/169 | R₂ cancels in Ω_DM product | beta unification |
| H₀ per-transit correction | (1−r) = α² × (4R₂)² × (20/13) | 4D geometry via (4R₂)² = π² | hubble_lib |

**R₂ cancellation in Ω_DM:** The R₂ that enters through DM/baryon = (22/13)×4R₂ cancels the R₂ that enters through Ω_b = 2/(13×4R₂). The dark matter density Ω_DM = 44/169 is R₂-free. This mirrors the R₂ cancellation registry in phys24_domain_lib.py: R₂ appears in both factors of a product and cancels, just as it does in the wire resistance × capacitance product and in K_J × R_K = 2/e.

---

## Table 15: Falsification Test Detail

| Test | Prediction | Observable | Current Status | Measurement Needed | Sensitivity |
|---|---|---|---|---|---|
| F1 | No DM particles | DM-nucleon cross-section | Null at 10⁻⁴⁷ cm² | Continued null at 10⁻⁴⁹ | Next-gen detectors |
| F2a | Virial ratio ~5 for spirals | M_virial/M_visible | MW: 2.8 (within factor 2) | Better MW mass model | Factor 2 |
| F2b | Virial fails for dwarfs | A_required > 10¹⁰ | 10¹¹ (confirmed failure) | Tidal correction | Factor 10 |
| F3 | DM ∝ kinematics | RAR scatter | 0.13 dex (tight) | Soliton model scatter | 0.3 dex threshold |
| F4 | Bullet lensing offset | Gas-lensing separation | 720 kpc observed | Soliton survival model | Factor 2 |
| P1 | DM ∝ thickness | DM vs h/R_d | Qualitative match | DiskMass Survey analysis | r > 0.3 |
| P2 | v(r) from modes only | Rotation curve shape | Not tested | SPARC fits | χ²/dof < 2 |
| P3 | Clusters: max DM | DM fraction ~85% | Confirmed | Already consistent | — |
| P4 | Tully-Fisher from R₂ | v⁴ scaling | Confirmed (v⁴) | Normalization test | Factor 2 |

---

## Table 16: Script Dependency Map

| Script | Requires | Provides To |
|---|---|---|
| 1 (dwarf_tidal) | None | 2, 3, 16, 21 |
| 2 (dwarf_soliton) | None | 16, 21 |
| 3 (dwarf_mass) | None | 21 |
| 4 (boundary_energy) | None | 5, 6, 21 |
| 5 (mode_spectrum) | 4 | 6, 8, 18 |
| 6 (rotation_curve) | 5 | 13, 18, 21 |
| 7 (a0_boundary) | None (parallel) | 8, 9, 15 |
| 8 (mond_TF) | 5, 7 | 21 |
| 9 (a0_sensitivity) | 7 | 21 |
| 10 (bullet_circulation) | None | 11, 21 |
| 11 (bullet_survival) | 10 | 12, 21 |
| 12 (cluster_profile) | 11 | 21 |
| 13 (cosmic_census) | 6 | 14, 21 |
| 14 (omega_chain) | 13 | 21 |
| 15 (bao_boundary) | 7 | 21 |
| 16 (orientation_track) | 1, 2 | 17, 21 |
| 17 (thickness_dm) | 16 | 21 |
| 18 (sparc_rar) | 5, 6 | 21 |
| 19 (pioneer) | None | 21 |
| 20 (null_detections) | None | 21 |
| 21 (consolidated) | All above | 22 |
| 22 (diagrams) | 21 | Publication |

---

## Table 17: Library Usage Map

| Script | phys24_lib | derivation_lib | structure_lib | boundary_lib | domain_lib | hubble_lib | diagram_lib |
|---|---|---|---|---|---|---|---|
| 1 | × | | | | | | |
| 2 | × | | × | | × | | |
| 3 | × | | | | | | |
| 4 | × | × | | | × | | |
| 5 | × | | | | × | | |
| 6 | × | | | | × | | |
| 7 | × | | | | × | × | |
| 8 | × | | | | × | | |
| 9 | × | | | | | × | |
| 10 | × | | | × | | | |
| 11 | × | | | | | | |
| 12 | × | | | | | | |
| 13 | × | | | | | | |
| 14 | × | | | | | | |
| 15 | × | | | | | × | |
| 16 | × | | | | | | |
| 17 | × | | | | | | |
| 18 | × | | | | × | | |
| 19 | × | | | | | | |
| 20 | × | | | | | | |
| 21 | × | × | × | × | × | × | |
| 22 | × | × | × | × | × | × | × |

**phys24_lib used in all 22 scripts.** phys24_domain_lib used in 7 scripts (amplification geometry, mode spectrum, R₂ connections). phys24_hubble_lib used in 3 scripts (a₀ sensitivity, BAO connection).

---

## Table 18: Cross-Program Connection Map

| Element | Toroidal DM | Beta Unification | Hubble Tension |
|---|---|---|---|
| Integer 11 (YM) | A = (44/13)... | Ω_DM = 44/169, DM/baryon = (22/13)π | — |
| Integer 13 (\|b₂_mod\|) | A = (44/13)..., a₀ | Ω_b, Ω_DM, DM/baryon, Λ | (1−r) = α²π²(20/13) |
| Integer 20 (\|3b₃_mod\|) | — | (1−r) = α²π²(20/13) | (1−r) = α²π²(20/13) |
| R₂ = π/4 | a₀ = cH₀/(8R₂), TF, cross-section | Ω_b = 2/(13π), π = 4R₂ | VP step = 1/(12R₂) |
| H₀ | a₀ = cH₀/(8R₂) | Λ predictions use α | Running curve H₀(N) |
| N ≈ 100 | BAO = boundary spacing | — | Per-transit r^N |
| α | — | All Λ formulas, (1−r) | (1−r) = α²π²(20/13) |
| Boundary concept | Boundary amplification | — | Boundary transit count |
| Soliton structure | Toroidal soliton | — | Soliton boundary hierarchy |

**The integer 13 appears in all three programs.** It is the single most connected quantity across the research portfolio: cosmic density (Ω_DM = 44/13²), Hubble running ((1−r) uses 20/13), and galactic DM (A = (44/13)π(c/v)²).

---

## Table 19: Kill Switch Decision Matrix

| Kill Switch | Trigger Condition | Detection Script | Impact | Recovery Path |
|---|---|---|---|---|
| K1 | All dwarfs retain DM/vis > 50 after max stripping | 1 | Dwarf explanation fails | Try soliton classification (Script 2) |
| K2 | No SPARC galaxy fits with χ²/dof < 2 | 6 | Rotation curve prediction fails | Model cannot explain flat curves |
| K3 | Bullet Cluster offset not reproducible (< 200 kpc) | 10 | Bullet Cluster test fails | Model is partial, not universal |
| K4 | Thickness-DM correlation r < 0.1 | 17 | P1 prediction falsified | Morphology connection severed |
| K5 | RAR scatter from model > 0.3 dex | 18 | Model too imprecise for data | Need better mode spectrum |
| K6 | DM particles detected with matching properties | 20 | Particle DM exists | May coexist with boundary effect |
| K7 | a₀ ≠ cH₀/(8R₂) by > 50% with improved data | 9 | MOND-R₂ connection breaks | Coincidence, not structure |

**Cascade logic:** K1 triggers → try K1 recovery (Script 2) → if Script 2 fails → dwarf problem unsolved → model is partial. K2 triggers → model fundamentally wrong for disks → program halted. K6 triggers → particle DM confirmed → toroidal model may coexist as secondary effect or be unnecessary.

---

## Table 20: Paper Outcomes by Stage Result

| Stage 0 (Dwarfs) | Stage 1 (Amplification) | Stage 3 (Bullet) | Stage 6 (Cross-val) | Paper |
|---|---|---|---|---|
| Resolved | Derived | Compatible | RAR fits | Full theory paper |
| Resolved | Derived | Compatible | RAR fails | Theory + empirical limits |
| Resolved | Not derived | Compatible | RAR fits | Empirical paper (no mechanism) |
| Resolved | Not derived | Incompatible | — | Partial model (disks only) |
| Unresolved | Any | Any | Any | Honest partial result paper |
| — | — | — | — | |
| Any | Any | Any | DM particles found | Reassessment paper |

**Every combination produces a paper.** The worst case (dwarfs unresolved, no derivation, Bullet fails) produces "Toroidal DM: What Works and What Doesn't" — an honest null result documenting the virial success for spirals and the connection to beta unification integers.

---

## Table 21: Null Result Registry

| Potential Null | Script | What It Would Mean | Status |
|---|---|---|---|
| Tidal stripping insufficient for dwarfs | 1 | Model cannot explain highest-DM systems | UNTESTED |
| Soliton scaling law A ∝ R^(-n) fails | 2 | No universal amplification formula | UNTESTED |
| Mass estimates robust against anisotropy | 3 | Dwarf DM fractions are real, not artifacts | UNTESTED |
| Boundary energy gives wrong A | 4 | Cannot derive amplification from first principles | UNTESTED |
| Mode spectrum cannot produce flat v(r) | 6 | Central rotation curve prediction fails (K2) | UNTESTED |
| a₀ ≠ cH₀/(8R₂) with improved H₀ | 9 | MOND-R₂ coincidence | Current: 15% match |
| Bullet Cluster offset not reproduced | 10 | Soliton boundaries don't survive collisions | UNTESTED |
| No thickness-DM correlation | 17 | P1 prediction falsified | UNTESTED |
| RAR scatter too large from model | 18 | Model too imprecise | UNTESTED |
| DM particles detected | 20 | Particle DM exists (may coexist) | 40+ years null |
| Virial insufficient for spirals | — | TESTED: virial ratio = 2.8 (works) | PASSES |
| Frame dragging sufficient | — | TESTED: O(10⁻¹³) (negligible) | FAILS |
| Naive v²/c² sufficient | — | TESTED: O(10⁻⁷) (insufficient) | FAILS |

---

## Table 22: Timeline and Resource Estimate

| Stage | Scripts | Est. Lines | Sessions | External Data | Blocking |
|---|---|---|---|---|---|
| 0: Dwarf gate | 1, 2, 3 | 320 | 1-2 | Dwarf data (published) | Address first |
| 1: Amplification | 4, 5, 6 | 470 | 2-3 | SPARC database | K2 possible |
| 2: MOND | 7, 8, 9 | 280 | 1 | None (theoretical) | Independent |
| 3: Bullet Cluster | 10, 11, 12 | 390 | 1-2 | Cluster lensing data | K3 possible |
| 4: Cosmological | 13, 14, 15 | 280 | 1 | Galaxy luminosity function | Needs Stages 1-2 |
| 5: Orientation | 16, 17 | 220 | 1 | DiskMass Survey | Needs Stage 0 |
| 6: Cross-validation | 18, 19, 20 | 310 | 1-2 | SPARC RAR data | Needs Stages 1-2 |
| 7: Integration | 21, 22 | 700 | 1-2 | None | Partial results OK |
| **Total** | **22 scripts** | **~2,970** | **7-13** | **Stages 0, 1, 3, 5** | **Stage 0 first** |

---

*Supporting Tables for the Toroidal Dark Matter Research Program. 22 tables covering integers, amplification, velocities, morphology, virial results, MOND connection, Tully-Fisher, frame dragging, geometry, proton parallel, dwarf data, Bullet Cluster, BAO scale, R₂ budget, falsification, dependencies, library usage, cross-program connections, kill switches, paper outcomes, null results, and timeline. Every entry traceable to phys24_lib.py, phys24_domain_lib.py, or the experiment script. April 3, 2026.*

