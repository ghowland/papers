# Soliton Boundary Physics: From Running Curves to Mode Spectra

## A Unified Framework for Boundary-Dependent Measurements Across Scales

**Status:** Active research notebook
**Origin:** HOWL Series Session 4, April 2 2026
**Context:** Emerged during systematic reading of HOWL-PHYS-1 through PHYS-7, PHYS-11, MATH-1 through MATH-6
**Series registry:** Builds on @HOWL-PHYS-1 through @HOWL-PHYS-7, @HOWL-PHYS-11, @HOWL-MATH-1 through @HOWL-MATH-6

---

## READER PREPARATION

This notebook proposes a framework that connects established physics results in ways that cross department boundaries. Every premise comes from the institution's own published, peer-reviewed literature or from the HOWL series papers that organize those premises. No new equations are introduced. No external framework is imported. The contribution is the connection.

A new reader must consciously override three default assumptions before the argument will be legible:

**Override 1: "Constants are constant."** The institution labels α, αs, G as "fundamental constants." The institution's own data shows α varies 8% between atomic and Z-boson scales (LEP confirmed, Nobel Prize context). αs varies by orders of magnitude (Nobel Prize 2004). The word "constant" is the label. The data contradicts the label. This is not disputed — it is taught in every QFT course. The framework in this notebook treats all "constants" as scale-dependent boundary readings, which is what the data shows them to be.

- Logic: a quantity that changes with measurement scale is not constant by the definition of the word.
- Empirical: α = 1/137.036 at atomic scale, α ≈ 1/127 at 91 GeV. Measured at LEP, SLD, LHC by independent groups.
- Math: the running is computed in exact Fraction arithmetic to 0.02 ppm (HOWL-PHYS-5, companion script alpha_EM_final.py).

**Override 2: "Planetary orbits are historical accidents."** The standard treatment computes orbits from initial conditions set during solar system formation. The orbital parameters are not derived from any structural principle — they are measured and simulated backward. This notebook proposes that orbital parameters may be structural properties of the gravitational soliton, derivable from boundary geometry the same way atomic energy levels are derivable from the Coulomb potential. This is a hypothesis, not an established result. The evidence (Titius-Bode, Kepler compact multis, Kirkwood gaps, ring structure) is presented for evaluation.

- Logic: if a system has standing wave modes, the mode spectrum is determined by boundary conditions, not by history. This is proved for every quantum system.
- Empirical: Titius-Bode predicted Ceres and Uranus before discovery. Kepler data shows regular spacing in compact multi-planet systems. Kirkwood gaps fall at resonance positions. Saturn's rings show standing wave density patterns.
- Math: the standing wave condition on a logarithmic potential (appropriate for a self-gravitating disk) produces geometric spacing. The specific derivation for the solar system is a research target, not a completed computation.

**Override 3: "The Hubble tension is two measurements disagreeing."** The standard framing: CMB gives H₀ = 67.4, local gives H₀ = 73.0, and we need to find which is wrong or what new physics resolves the gap. This notebook reframes: there is no gap. There is a continuous running curve H₀(N) parameterized by boundary transit count N. Different measurements sample different points on the curve. The "tension" is the slope of the curve, not an error.

- Logic: if every coupling runs with boundary depth (established for α, αs, weak coupling), H₀ should run with boundary transit count. The question is whether it does, not whether it should.
- Empirical: five H₀ measurements ordered by transit count show monotonic decrease: 73.0 → 73.3 → 69.8 → 67.4 → 67.4.
- Math: H₀(N) = H₀(0) × r^N with r extractable from the data once N is estimated for each method. The extracted r, if rational, identifies the boundary geometry through the R₂/R₄ framework.

---

## CHAPTER 1: THE SERIES FOUNDATION

This chapter extracts the specific results from the HOWL series that this notebook depends on. Each section covers one paper's contribution in the Logic → Empirical → Math format. The reader who absorbs this chapter has the minimum context needed for Chapters 2–9.

### 1.1 Mass Is Inertia; Particles Are Vortices with Boundaries (PHYS-1)

The first paper in the series connects results from six physics departments that have not been connected because no single department holds all the pieces.

Logic: Newton's F = ma defines mass as resistance to acceleration. Resistance to acceleration is the definition of inertia. These are the same definition. The equivalence principle (gravitational mass = inertial mass, confirmed to 10⁻¹⁵ by MICROSCOPE) becomes a tautology: inertia = inertia. QCD lattice calculations show 99% of proton mass is binding energy — the energy of the pattern maintaining itself. Mass is pattern resistance to disruption. The Higgs mechanism determines coupling to the field that resists acceleration — it is an inertia-determination mechanism. Connected: mass is inertia across all operational definitions.

Empirical: MICROSCOPE satellite confirms equivalence to 10⁻¹⁵. LHC confirms Higgs mechanism. Lattice QCD confirms 99% binding energy. Three measurement anomalies — Hubble tension (H₀ = 67.4 vs 73.0), proton radius puzzle (0.842 fm vs 0.877 fm), muon g−2 (4.2σ discrepancy) — correlate with boundary transit count or probe interaction depth. The quantity measured at greater boundary depth or through more boundary transits gives a different reading.

Math: no computation in PHYS-1. Conceptual paper establishing the framework. The computation begins in PHYS-5.

The key concept for this notebook: every coherent self-sustaining structure has a boundary where interior and exterior readings differ. The boundary is the soliton boundary. It is an unmodeled element in the measurement pipeline. The three anomalies correlate with this unmodeled element.

### 1.2 Every "Constant" Runs; The Transformation Law Is Fundamental (PHYS-2)

Logic: α varies from 1/137 to 1/127 depending on probe energy. αs varies by orders of magnitude. The weak coupling varies from apparently weak to comparable to electromagnetic at the electroweak scale. Each variation corresponds to the measurement crossing a coherent structure boundary — the vacuum polarization cloud (QED), the confinement zone (QCD), the mass threshold (weak). The beta functions that describe the running are structural properties of the theory — they depend on the gauge group and particle content, not on where you measure. The coupling is the reading. The beta function is the law connecting readings. The law is more fundamental than any single reading.

Empirical: α running confirmed at LEP/SLD/LHC. αs running confirmed at every hadron collider (Nobel Prize 2004). Electroweak unification confirmed (Nobel Prize 1979). Flavor thresholds modeled precisely with matching conditions at each quark mass. The institution confirms all of this, models it, teaches it, and calls the quantities "constants."

Math: the beta function slopes are exact rationals from particle counting. b₁ = 41/10, b₂ = −19/6, b₃ = −7. These are computed from N_c, Q², T₃, and the gauge self-coupling. No free parameters. The gap ratio (b₁ − b₂)/(b₂ − b₃) = 218/115 = 1.896. The measured gap ratio at M_Z is 1.395. The 36% miss quantifies the SM's incomplete particle content.

The key concept for this notebook: the transformation law (beta function, running curve) is the fundamental object. The "constant" is a reading from a specific depth. This principle extends to H₀: the H₀ running curve is the fundamental object, and 67.4 and 73.0 are readings from different depths.

### 1.3 G Never Tested Outside Earth's Hill Sphere (PHYS-3)

Logic: the Hill sphere is the institution's own concept from orbital mechanics — the boundary of Earth's coherent gravitational domain at ~1.5 million km. Every direct G measurement in the 227-year record is on Earth's surface at ≤0.45% of this boundary distance. The ISS is at 0.027%. The Moon is at 25%, orbiting inside. No direct measurement has been taken at or beyond the boundary. Indirect evidence (pulsar timing, gravitational waves) receives signals inside the boundary and interprets them using models that assume universal G. The assumption does the work. Reproducibility within one boundary configuration is not universality across configurations. The effective sample size for cross-boundary G universality is zero.

Empirical: the persistent disagreement between G measurements (BIPM 6.67545, LENS 6.67191, HUST 6.67484/6.67349 — two values from the same lab) has not been resolved by two centuries of systematic error investigation. L1 and L2 Lagrange points are at the Hill sphere boundary. Spacecraft operate there (JWST, DSCOVR, Gaia). None has measured G. The measurement has not been made because the question has not been framed.

Math: no computation. Factual documentation of experimental record plus proposed experiment.

The key concept for this notebook: reproducibility within one boundary configuration does not prove universality across configurations. Internal consistency checks verify arithmetic, not physics. This applies to every level of the boundary taxonomy in Chapter 3.

### 1.4 The Boundary Test Program (PHYS-4)

Logic: the test program connects MATH-1 (geometric framework Q = F · β · d² · Z), PHYS-1 (boundary catalog), and PHYS-3 (G gap) into seven ordered tests. Boundaries are classified as geometric (sphere, ellipsoid — framework applies) or non-geometric (momentum-space confinement — outside scope). The calibration-first principle: reproduce known results (running of α) before applying to unknown cases. The kill switch: if Tests 0, 1, 2 all produce null results, stop. The decision tree specifies every possible outcome before any test is run.

Empirical: six of seven boundaries are geometric. Hadron confinement is the exception (momentum-space scale, no spatial sphere). Three tests use published data requiring no new experiments. The kill switch is genuine — if easy tests fail, hard tests are not pursued.

Math: decision tree with complete outcome enumeration. Falsification matrix for every test. Sensitivity analysis for the G depth trend test (likely underpowered but costless).

The key concepts for this notebook: calibrate before extending (Chapter 9 research program). Kill switch at every level (every chapter has its own kill condition). Decision tree before data (Chapter 8 specifies outcomes before computations). Scope boundaries are findings, not failures (Chapter 3 classification of which structures have boundaries and which don't).

### 1.5 α_EM Running in Integer Arithmetic; Gap Ratio 218/115 (PHYS-5)

Logic: the QED running of α_EM from M_Z to atomic scale is a transformation law connecting readings at different boundary depths. The law is determined by particle counting (lepton charges, color factors) and the VP integral structure (boundary constant 1/3 from the subtracted VP, O(m²/q²) coefficients 4 and −6 from the expansion). Seven measured rationals enter. All transcendentals are MATH-2 integer pairs. Every intermediate is a Python Fraction.

Empirical: the result 1/α_EM = 137.0360025 matches CODATA 2022 (137.0359992) to 0.02 ppm. The error decreased by four orders of magnitude across six stages, each from adding boundary structure. No free parameters were tuned. The hadronic VP measurement (±73 ppm) is the floor — the integer arithmetic reached the measurement limit.

Math: companion script alpha_EM_final.py runs in ~60 seconds, produces a Fraction with 28,293-bit numerator. The gap ratio 218/115 is a pure integer prediction: no measured value enters, no transcendental appears. 218 and 115 come entirely from counting particle species and their charges.

The key concepts for this notebook: exact rational arithmetic is achievable for boundary-crossing physics (Chapter 2 proposes the same for H₀). The gap ratio is the primary test for BSM particle content (Chapter 6 proposes orbital parameters as an analogous counting result). The per-flavor contribution 2/3 per quark for b₃ establishes the SM counting convention.

### 1.6 The Confinement Boundary Has Two Faces (PHYS-6)

Logic: the 5/6 confinement correction from PHYS-5 is not universal — it is the α_EM kernel's weighted average of two distinct regions. Above 2 GeV: perturbative correct, ratio ~1.0, R-ratio is exact rational (2, 10/3, 11/3, 5). Below 2 GeV: confinement reorganizes spectrum, ratio ~0.61, spectrum is resonances not free quarks. The muon g−2 kernel weights the below-2-GeV region far more heavily and the perturbative calculation fails qualitatively (factor ~1300). The correction is kernel-dependent, not universal.

Empirical: the perturbative R-ratio above 2 GeV matches e⁺e⁻ → hadrons data within a few percent (quark-hadron duality). Below 2 GeV, the physical spectrum (ρ, ω, φ resonances, pion threshold at 280 MeV) has no perturbative analog. The muon g−2 tension (3.5σ) lives entirely in the hadronic sector — the below-2-GeV region. The QED sector shows no tension.

Math: decomposition: 0.54 × 1.0 + 0.46 × 0.61 = 0.82 ≈ 5/6. The below-2-GeV ratio ~0.61 has ±5% uncertainty. Rational candidates: 3/5 (0.600), 11/18 (0.611), 8/13 (0.615). Precision insufficient to identify exact rational.

The key concept for this notebook: corrections are kernel-dependent. Different measurement methods see the same boundary differently because they weight the boundary's two faces differently. This applies to H₀ measurements (Chapter 2.4) — each method is a different kernel.

### 1.7 θ_QCD = 0 Is the Ground State (PHYS-7)

Logic: the QCD vacuum energy E(θ) = E₀ − χ_top · cos(θ) is minimized at θ = 0. The vacuum is defined as the minimum energy state. Therefore the vacuum has θ = 0. The institution performs this identification (vacuum = energy minimum) for the Higgs vacuum at v = 246 GeV without comment. It refuses to perform it for θ and declares a fifty-year "problem." The basis decomposition θ_phys = θ_bare + arg(det M_q) involves gauge-dependent pieces whose "cancellation" is standard gauge invariance, not fine-tuning. Naturalness has zero confirmed predictions in forty years. The burden of proof is on those who claim the universe is NOT in its ground state.

Empirical: |θ| < 5 × 10⁻¹¹ from neutron EDM bound (Abel et al. 2020). Every measurement is consistent with θ = 0 exactly. No experiment has ever required θ ≠ 0. Axion searches (ADMX, HAYSTAC, CASPEr, ABRACADABRA, CAST, IAXO) have found no axion after forty years.

Math: the topological sectors are integers (π₃(SU(3)) = ℤ). The ground state is at the integer 0. The energy functional −cos(θ) on the 8R₂-periodic domain has minimum at θ = 0 with remainder R = 0 (PHYS-11 Domain 1, Subgroup A).

The key concepts for this notebook: don't declare problems where the answer is internal. The ground state requires no mechanism. The burden of proof reversal: you need a mechanism to explain departures FROM the ground state, not the ground state itself. This applies to the orientation tracks (Chapter 5): aligned orientation is the ground state; misalignment requires a perturbation mechanism.

### 1.8 R₂ = π/4 Is Universal; R₄ = π²/32 Enters Through 4D Operations (PHYS-11, MATH-1, MATH-5)

Logic: MATH-1 proves β = π/4 = R₂ as the geometric invariant across nine engineering domains (Q = F · β · d² · Z). MATH-5 proves the n-ball remainder R_n = π^(n/2)/(2^n · Γ(n/2+1)) separates in every equation performing an n-ball-volume operation. n = 2 and n = 4 are uniquely "doubly native" to binary arithmetic. PHYS-11 shows R₂ appears in all nine physics domains: as the modular period 8R₂ in seven (Subgroup A, phase-periodic), as the step size 1/(12R₂) in one (Subgroup B, monotonic accumulation — the VP running), and in the exponential of the ninth (Subgroup C, Chern-Simons). R₄ enters through energy eigenvalues (π² = 32R₄) and 4D normalizations (1/(8π²) = 1/(256R₄)).

Empirical: the nine physics domains are established: theta vacuum, Bohr-Sommerfeld, Berry phase, Brillouin zones, Aharonov-Bohm, flux quantization, AC Josephson, RG running, Chern-Simons. All decompositions verified as exact Fraction identities. The three-subgroup classification is provably irreducible (no smooth bijection converts monotonic to periodic).

Math: eight framework identities verified in Fraction arithmetic: 2π = 8R₂, π = 4R₂, π/2 = 2R₂, π² = 32R₄, 8π² = 256R₄, 1/(3π) = 1/(12R₂), 1/(8π²) = 1/(256R₄), 4π = 16R₂. All exact.

The key concept for this notebook: R₂ appears in every 2D geometric operation (circles, phases — spherical boundaries). R₄ appears in every 4D operation (loop integrals, energy eigenvalues — and, this notebook proposes, toroidal boundaries where T² = S¹ × S¹ produces R₂² = 2R₄). The geometry of the boundary determines which R_n appears in the correction factor. Spherical → R₂. Toroidal → R₄.

### 1.9 The Arithmetic Infrastructure (MATH-2 through MATH-6)

Logic: MATH-2 represents 17 transcendentals as exact integer pairs at 100+ digits via the Q335 = 2³³⁵ basis. MATH-3 extends to elliptic integrals and Borwein-accelerated ζ(5). MATH-4 establishes the universal denominator 2³³⁵ making addition = integer addition on numerators. MATH-5 proves the n-ball remainder sequence with n = 2, 4 uniquely doubly native. MATH-6 achieves 82/82 PSLQ independence (zero relations found among the basis elements). Two arithmetic tiers: exact Fractions for rationals (beta coefficients, quantum numbers), Q335 integer pairs for transcendentals (π, ln(2), ζ(3), ζ(5), Li₄(1/2)).

Empirical: every assertion passes. Zero tolerance. Verification by string comparison at 100 digits, not epsilon comparison. Three successes from physics derivation, zero from pattern matching ("derivation beats search").

Math: the complete infrastructure is operational. Every computation in this notebook that reaches the Math stage uses this infrastructure: Fraction arithmetic for rationals, MATH-2 integer pairs for transcendentals, assert-verified identities with zero tolerance.

---

## CHAPTER 2: THE HUBBLE TENSION AS RUNNING CURVE

### 2.1 The Data

Five H₀ measurements, ordered by effective soliton boundary transit count along the line of sight:

| Method | H₀ (km/s/Mpc) | Uncertainty | Effective N (relative) | Distance class |
|---|---|---|---|---|
| SH0ES (Type Ia SNe) | 73.0 | ±1.0 | Low | Local galaxies |
| H0LiCOW (lensing) | 73.3 | ±1.8 | Low-medium | Through lens galaxy |
| CCHP (TRGB) | 69.8 | ±1.7 | Medium | Different calibration |
| DES + BAO + BBN | 67.4 | ±1.2 | High | Cosmological scale |
| Planck CMB | 67.4 | ±0.5 | Maximum | Full observable universe |

Logic: PHYS-2 establishes that every coupling runs with boundary depth. The transformation law (running curve) is the fundamental object, not any single reading. If H₀ is a boundary-dependent reading — which it must be if the framework is consistent — then measurements at different boundary depths give different values. The five measurements above are not five attempts to measure one number. They are five points on a curve H₀(N).

Empirical: the trend is monotonic. More boundary transits → lower H₀. No measurement with high transit count gives high H₀. No measurement with low transit count gives low H₀. The intermediate values (69.8, 73.3) fall between the endpoints, consistent with a continuous curve rather than a binary tension or random scatter.

Math: the functional form H₀(N) = H₀(0) × r^N has two free parameters: H₀(0) (the zero-transit local value) and r (the per-transit correction factor). Five data points overdetermine these two parameters. The fit quality (chi-squared per degree of freedom) tests whether the exponential form is correct. If the fit is poor, a more complex form is needed (multiple r values for different boundary types, or a non-exponential accumulation).

### 2.2 The Per-Transit Correction Magnitude

The cumulative correction from local to CMB is 67.4/73.0 = 0.923. If the correction accumulates exponentially: r^N = 0.923, so r = 0.923^(1/N).

Logic: the per-transit correction must be extraordinarily close to 1 for any plausible N, because the total correction is only ~8% while the number of boundaries crossed is large.

Empirical: published large-scale structure catalogs (SDSS, 2dF, Planck lensing) estimate the count and type of structures along typical CMB lines of sight. Galaxy clusters: ~100–200. Filaments: ~1000+. Voids: ~50–100. Individual galaxies: ~10⁴–10⁵.

Math: 

| Effective N | Required r | 1 − r | Interpretation |
|---|---|---|---|
| 10 | 0.9920 | 0.0080 | ~1/125 per transit |
| 100 | 0.99920 | 0.00080 | ~1/1250 per transit |
| 1000 | 0.999920 | 0.000080 | ~1/12500 per transit |
| 10000 | 0.9999920 | 0.0000080 | ~1/125000 per transit |

The common factor: 1 − r ≈ 0.080/N, where 0.080 = ln(73.0/67.4) = 0.0798. Compare to the VP running step size 1/(3π) = 1/(12R₂) ≈ 0.1061. The H₀ per-transit correction is of similar order to the VP step size divided by N. Whether this comparison has structural content (both involving R₂) or is coincidental is an open question.

### 2.3 The Inversion: Extract the Law from the Data

The series approach for α running was top-down: derive the VP formula from QED → compute the running → compare to CODATA. The approach for H₀ running is bottom-up: extract the running curve from measurements → identify the per-transit rational → derive its origin from boundary geometry.

Logic: the bottom-up approach is appropriate when the top-down derivation is not yet available. PHYS-4 Section IX.3 identified the per-transit correction magnitude as the missing theoretical piece. The curve thesis inverts the problem: extract the magnitude empirically, then look for its derivation.

Empirical: the extraction requires (N, H₀) pairs. H₀ is measured. N requires estimation from structure catalogs. The estimation has uncertainty (which structures count as boundaries? what is the effective correction per structure type?). The uncertainty in N propagates to uncertainty in r.

Math: the fit procedure is: (1) estimate N_i for each measurement method i from published structure catalogs. (2) Fit H₀(N) = H₀(0) × r^N to the five data points. (3) Extract r. (4) Express r as a Fraction. (5) Check whether the Fraction has integer content traceable to R₂, R₄, or VP integral constants. If step 5 succeeds, the boundary geometry is identified. If step 5 fails (r is not a recognizable rational), the running curve exists but has no connection to the series' rational framework.

### 2.4 Kernel Dependence

PHYS-6 showed that the confinement boundary correction is kernel-dependent: the α_EM kernel sees ~0.82 overall, the muon g−2 kernel sees qualitative failure. Different H₀ measurement methods may be different kernels.

Logic: each method measures photons (or gravitational waves) that interact differently with soliton boundaries. CMB photons are microwave (~mm). SNe photons are optical (~500 nm). Lensing uses mixed wavelengths. Gravitational waves are non-electromagnetic. If the per-transit correction depends on the wavelength or type of radiation relative to the boundary size (the way the confinement correction depends on the VP kernel relative to the confinement scale), different methods give different curves.

Empirical: current data has insufficient precision to test kernel dependence. The uncertainty bars on intermediate H₀ measurements (TRGB ±1.7, H0LiCOW ±1.8) are too large to distinguish method-dependent curves from a single curve. More precise intermediate measurements, or a larger sample of methods, would test this.

Math: the kernel-dependent model replaces H₀(N) = H₀(0) × r^N with H₀_method(N) = H₀(0) × r_method^N. Each method has its own r_method. The relationship between r values for different methods encodes the kernel dependence. If r_CMB ≠ r_SNe ≠ r_GW, the corrections are kernel-dependent. If all are equal, they're universal (and PHYS-6's lesson doesn't apply at this scale).

### 2.5 Falsification

F1: if intermediate H₀ measurements (TRGB, lensing, BAO) do not fall on a smooth monotonic curve when plotted against estimated N, the running curve thesis is not supported.

F2: if the best-fit r is not a recognizable exact rational with integer content traceable to R₂, R₄, or VP integral constants, the curve exists but has no connection to the series' framework.

F3: if the curve fit requires more than two parameters (H₀(0) and r), the simple exponential running model is insufficient.

F4: if improved measurements at intermediate distances converge to one of the endpoint values rather than maintaining distinct intermediate values, the curve collapses to a step function.

F5: if the Hubble tension resolves through systematic error identification in either CMB or local measurements, the running curve is unnecessary.

---

## CHAPTER 3: THE SOLITON BOUNDARY TAXONOMY

### 3.1 The Coherence Spectrum

Every persistent structure in the universe can be placed on a spectrum from maximum coherence (black hole — the boundary IS the defining feature, 100% absorption) through high coherence (stars, planets — self-sustaining, compact, sharp boundary), medium coherence (clusters, filaments — collectively bound, diffuse boundary), low coherence (nebulae — persistent but not self-sustaining), to anti-coherence (voids — defined by the absence of structure).

The per-transit correction factor r(C) is a function of coherence C. At maximum coherence, r = 0 (nothing escapes). At zero coherence, r = 1 (no correction). Everything between follows a function to be determined.

Logic: the correction must scale with how strongly the boundary separates interior from exterior. A sharp, high-contrast boundary (neutron star surface) produces a larger correction than a diffuse, low-contrast boundary (nebula edge). The limiting cases constrain the function.

Empirical: the complete enumeration by coherence class:

**Maximum coherence (compact, self-gravitating, long-lived):**

| Object | Boundary | Interior vs exterior | Correction expected |
|---|---|---|---|
| Black hole | Event horizon | Maximum possible — information cannot cross | Maximum: r = 0 |
| Neutron star | Neutron surface + magnetosphere | Nuclear density vs vacuum | Very large |
| White dwarf | Degenerate surface | Electron degeneracy vs vacuum | Large |
| Main sequence star | Photosphere + Hill sphere | Fusion dynamics vs stellar wind | Moderate-large |
| Planet | Surface/cloud-top + Hill sphere | Self-gravity dominates vs external field | Moderate |
| Moon/asteroid | Hill sphere | Weak self-gravity | Small |

**Collective coherence (from individually coherent components):**

| Collective | Components | Binding | Geometry | Correction expected |
|---|---|---|---|---|
| Galaxy | ~10¹¹ stars | Self-gravity | Oblate spheroid / thick torus | Large collective |
| Globular cluster | ~10⁵–10⁶ stars | Self-gravity | Sphere | Moderate collective |
| Open cluster | ~10²–10⁴ stars | Weak self-gravity | Irregular, dissolving | Small collective |
| Binary star system | 2 stars | Mutual gravity | Complex Roche geometry | Moderate collective |
| Planetary system | Star + planets | Star's gravity | Disk / nested tori | Moderate collective |
| Saturn's rings | ~10¹⁵ particles | Orbital resonance | Thin torus | Small-moderate collective |
| Asteroid belt | ~10⁶ objects | Orbital resonance (Jupiter) | Sparse torus | Very small collective |

**Low coherence (persistent but not self-sustaining):**

| Structure | Energy source | Self-sustaining? | Boundary exists? | Correction expected |
|---|---|---|---|---|
| Molecular cloud | Self-gravity | Partially | Yes — self-shielding edge | Small |
| Dark nebula | None (absorbing) | No | Absorption edge only | Minimal |
| Planetary nebula | Central white dwarf UV | Decaying | Expanding shell — yes | Small, time-dependent |
| Emission nebula (HII) | External hot star | No | Ionization front — weak | Minimal |
| Supernova remnant | Explosion kinetic energy | Decaying | Shock front — yes initially | Moderate initially, decaying |
| Reflection nebula | Reflected starlight | No | None intrinsic | Zero |

**Standing wave patterns (persistent, not material):**

| Pattern | Mechanism | Material? | Boundary? | Correction expected |
|---|---|---|---|---|
| Galactic spiral arm | Density wave | No — stars move through | Density enhancement edge | Unknown — depends on whether standing waves have soliton boundaries |
| Cosmic filament | Gravitational collapse | Yes — gas and galaxies | Density ridge | Moderate collective |
| Cosmic void wall | Gravitational evacuation | Yes — the boundary of nothing | Sharp density transition | Moderate (possibly opposite sign) |

**Anti-coherence:**

| Structure | Defining feature | Interior | Boundary with | Correction expected |
|---|---|---|---|---|
| Cosmic void | Absence of structure | Near-vacuum | Filament walls | Opposite sign from positive-density boundaries |

Math: the functional form r(C) is to be determined. Candidates: step function (r = r₀ for C > threshold, r = 1 below), power law (r = 1 − ε·C^α), exponential (r = exp(−ε·C)). The form is constrained by the limiting cases and by the data (if the running curve fit from Chapter 2 can be decomposed by boundary type).

### 3.2 Composite Boundary Formation

Logic: PHYS-6 establishes the precedent. Individual quarks have individual boundaries (the outside face, perturbative, ~100% transmission above 2 GeV). Collectively bound into a hadron, they form a qualitatively different boundary (the inside face, non-perturbative, ~61% transmission below 2 GeV). The collective boundary is not the sum of individual boundaries. The question for every collection of gravitationally bound objects is: does the collection form a collective boundary with emergent properties?

Empirical: the known examples form a pattern:

| System | Individual boundaries | Collective boundary | Mechanism |
|---|---|---|---|
| Quarks → hadron | VP clouds per quark | Confinement boundary | Strong force binding |
| Electrons → atom | Wave functions per electron | Electron shell | EM binding |
| Atoms → molecule | Atomic boundaries | Molecular orbital boundary | Covalent/ionic binding |
| Stars → galaxy | Hill spheres per star | Galactic halo/disk boundary | Self-gravity |
| Galaxies → cluster | Halos per galaxy | Cluster virial boundary + ICM | Self-gravity |

The pattern: collective boundaries form when components are in stable configuration maintained by a binding mechanism, and when the components are dense enough that individual boundaries overlap or interact.

The prediction: Saturn's rings (dense, resonance-maintained) form a collective toroidal boundary. The asteroid belt (sparse) does not, or forms only a very weak one. The test: ring occultation data (Cassini) analyzed for residuals beyond particle opacity, compared to asteroid belt transit observations.

Math: the threshold condition for collective boundary formation is an open question. Candidates: individual Hill spheres overlap (density criterion), orbital coherence exceeds a threshold (angular momentum criterion), binding energy exceeds thermal energy (energy criterion). Each candidate produces a different threshold and different predictions for which systems form collectives.

### 3.3 Nebulae in the Framework

Logic: a nebula is a persistent structure that lacks self-sustaining coherence. In Conway's Life terms: a star is a still life or oscillator (internally stable), a nebula is a pattern that exists only with external input or is a transient decaying from an initial impulse. The question is whether persistence without self-sustainability is sufficient for a soliton boundary.

Empirical: nebulae have physical boundaries — ionization fronts, shock fronts, absorption edges, expanding shells. These boundaries produce known effects on light (absorption, emission, scattering). The question is whether they produce ADDITIONAL effects from the soliton boundary mechanism, beyond the known absorption/emission/scattering.

Math: if the correction scales with coherence, nebulae contribute very small corrections (low coherence). The cumulative effect of many nebulae along a line of sight might be detectable if the individual corrections, though small, are numerous. The number of nebulae along a typical CMB line of sight is not well-constrained.

Open question: is there a minimum coherence below which a structure has no soliton boundary at all (hard cutoff), or does every structure contribute some correction however small (soft scaling)?

### 3.4 Voids as Anti-Boundaries

Logic: a void is a region of underdensity. If overdense structures (clusters, filaments) produce corrections that reduce H₀, underdense structures might produce corrections that increase H₀. The void boundary (the filament wall) is a transition from low density (interior) to high density (exterior) — the opposite of a cluster boundary (high density interior, low density exterior). If the correction sign depends on the density gradient direction, voids contribute opposite-sign corrections.

Empirical: the Eridanus supervoid aligns with the CMB cold spot. BAO measurements, which are sensitive to void structure, give H₀ values (67.4) consistent with the CMB rather than local measurements. Lines of sight through more voids would show different net corrections than lines of sight through more clusters.

Math: the net correction along a line of sight is:

correction = Π_clusters r_cluster × Π_filaments r_filament × Π_voids r_void

If r_void > 1 (opposite sign from r_cluster < 1), the void contributions partially cancel the cluster contributions. The net correction is smaller than the cluster-only estimate, which means the per-cluster correction must be LARGER than the simple estimate to produce the same total 0.923 factor.

Falsification: if lines of sight through known voids show the same H₀ as lines of sight through known clusters (at the same total distance), the void anti-correction hypothesis is not supported.

---

## CHAPTER 4: THE GEOMETRY CATALOG

### 4.1 The Constraint

Logic: the series works with exact rationals. Simple geometries produce simple rationals. Complex geometries (high-order polyhedra, exotic topologies) produce complex corrections that may not be expressible as simple rationals. The constraint restricts to curved shapes (sphere, torus, spheroid, disk, shell, cylinder, cone) and polyhedra with ≤32 faces. This excludes Lie group exhaustive classification (which produces thousands of candidates) and focuses on geometries that are physically realized as soliton boundaries.

Empirical: every astrophysical soliton boundary observed so far is one of: sphere (Hill spheres, halos, VP clouds), oblate spheroid (galaxies, rotating stars), disk (protoplanetary disks, galactic disks, accretion disks), torus (rings, belts), or shell (planetary nebulae, supernova remnants). No astrophysical boundary is a dodecahedron or truncated icosahedron. The polyhedral geometries enter for standing wave node structures (quark configurations inside hadrons, crystal structures) rather than macroscopic boundaries.

Math: each geometry has a characteristic ratio — the shape's measure (area, volume, or cross-section) divided by its rectilinear bounding box. This ratio determines the rational correction factor.

### 4.2 Spherical Boundaries: R₂ Content

The sphere is the default geometry. MATH-1 proves β = R₂ = π/4 for the circle-to-square ratio.

| Measure | Formula | R₂ content |
|---|---|---|
| Disk area | πr² | 4R₂ · r² |
| Sphere cross-section | πr² | 4R₂ · r² |
| Sphere surface area | 4πr² | 16R₂ · r² |
| Sphere volume | (4/3)πr³ | (16R₂/3) · r³ |
| Solid angle (full sphere) | 4π | 16R₂ |

Logic: every spherical boundary's correction factor involves R₂ and rational coefficients. The correction is parameterized by the sphere's radius and the ratio of probe wavelength to boundary size. For boundaries much larger than the probe wavelength (Hill spheres crossed by light), the correction reduces to a function of R₂ alone.

Empirical: the VP running step size 1/(3π) = 1/(12R₂) is the established per-flavor correction at the electron's spherical VP boundary. This is the calibration case: the spherical correction IS 1/(12R₂) per boundary crossing for electromagnetic coupling.

Math: for a spherical boundary of radius r_boundary crossed by radiation of wavelength λ, the correction is expected to involve R₂ × f(λ/r_boundary) where f is a function to be determined. In the limit λ ≪ r_boundary (geometric optics), f approaches a constant. In the limit λ ~ r_boundary (wave optics), f has oscillatory structure.

### 4.3 Toroidal Boundaries: R₄ Content

The torus is the key new geometry. It enters for orbital collectives (rings, belts), accretion disks, and potentially for rotating quark configurations inside hadrons.

| Measure | Formula | R₂/R₄ content |
|---|---|---|
| Torus volume | 2π²Rr² | 32R₂² · 2Rr² = 64R₄ · 2Rr² |
| Torus surface area | 4π²Rr | 64R₂² · Rr = 128R₄ · Rr |
| Torus cross-section (along axis) | π(R+r)² − π(R−r)² = 4πRr | 16R₂ · Rr |
| Torus cross-section (perpendicular to axis) | 2 × πr² = 2πr² | 8R₂ · r² |

Logic: the torus has two independent circular factors (S¹ × S¹ = T²). Each S¹ contributes R₂. The product contributes R₂² = π²/16 = 2R₄. Therefore toroidal boundaries produce corrections involving R₄ where spherical boundaries produce corrections involving only R₂. This is the geometric origin of the R₂-to-R₄ transition: the boundary's topology determines which geometric constant appears.

The aspect ratio R/r (ratio of major to minor radius) parameterizes the torus family. At R/r → ∞ (thin ring), the torus degenerates to a circle (1D, R₂ only). At R/r = 1 (maximally fat torus, approaching sphere with hole), the R₄ content is maximal. The correction factor is a function of R₄ and R/r.

Empirical: Saturn's rings have R/r ≈ 136,000 km / 10 km = 13,600 (extremely thin). The asteroid belt has R/r ≈ 2.7 AU / 0.6 AU ≈ 4.5 (moderate). Galaxy disks have R/r ≈ 15 kpc / 0.3 kpc ≈ 50 (moderately thin). The R₄ content varies across these systems, with fatter tori having more R₄.

Math: the toroidal correction factor for a boundary with aspect ratio R/r is:

r_torus(R/r) = function of R₄ and R/r

The specific function is to be derived from the standing wave condition on the toroidal potential. This derivation is one of the primary research targets (Chapter 9).

Connection to PHYS-11: the one-loop factor 1/(16π²) = 1/(512R₄) comes from the 4D loop integral solid angle. The 4D integration over loop momentum is topologically toroidal (a fermion traversing a closed loop in 4D spacetime). The 1/(512R₄) may be the quantum field theory version of the toroidal boundary correction.

### 4.4 Polyhedral Node Structures

Logic: standing wave patterns on spheres produce nodes at specific points. For low mode numbers, the node patterns correspond to the vertices of Platonic solids. Higher modes correspond to Archimedean solids. The node geometry determines the angular structure of the correction factor.

The constraint ≤32 faces admits:

| Polyhedron | Faces | Symmetry | Face-to-box ratio | Where it appears |
|---|---|---|---|---|
| Tetrahedron | 4 | T_d | Pure rational (no π) | sp³ nodes, simplest 3D mode |
| Cube | 6 | O_h | 1 (fills its box) | Crystal lattice, d-orbitals |
| Octahedron | 8 | O_h | Pure rational | d-orbital nodes |
| Dodecahedron | 12 | I_h | Involves φ = (1+√5)/2 | Possible quark geometry |
| Icosahedron | 20 | I_h | Involves φ | Virus capsids, C₆₀ dual |
| Truncated icosahedron | 32 | I_h | Involves φ | C₆₀ (Buckyball), maximum allowed |

Empirical: polyhedral structures appear at the molecular and nuclear scale (crystal symmetries, virus capsids, fullerenes). At astrophysical scales, they do not appear directly — astrophysical boundaries are smooth. However, standing wave patterns INSIDE astrophysical solitons may have polyhedral node structure. The mode structure of a vibrating sphere produces spherical harmonics Y_l^m, whose node patterns for low l correspond to the Platonic solids.

Math: for each polyhedron, the face area divided by the bounding rectangle gives a pure rational (for faces with rational angles) or an algebraic number (for pentagonal faces, involving φ). These rationals are different from the R₂/R₄ rationals of curved shapes. A correction factor from polyhedral node structure would be purely rational (no π), distinguishable from the curved-geometry corrections.

### 4.5 The Quark Geometry Question

Logic: the proton contains three quarks in a color-singlet configuration. The spatial geometry of this configuration is not directly observable — it is inferred from form factor measurements and lattice QCD calculations. Multiple geometries are energetically competitive: Y-junction (three flux tubes meeting at a center), Delta loop (closed triangular loop), and rotating versions of both. A rotating Delta loop sweeps out a toroidal configuration.

Empirical: proton form factor measurements at high Q² show the electric and magnetic form factors differ, implying non-spherical charge distribution. Lattice QCD studies of flux tube geometry show both Y and Delta configurations at different quark separations. The internal geometry is a quantum superposition, but the time-averaged geometry (which determines the form factor) may have dominant toroidal character for the rotating proton.

Math: the VL beta shifts (Δb₁, Δb₂, Δb₃) depend on the representation quantum numbers (color, weak isospin, hypercharge), not on the internal geometry. But the boundary correction for light or other particles crossing a hadron's soliton boundary DOES depend on the internal geometry — spherical vs toroidal interior structure would produce different correction factors (R₂ vs R₄). This could be tested by comparing the proton's form factor (which encodes the boundary structure) to the predictions of spherical vs toroidal models.

### 4.6 Connection to R₂/R₄ Framework

The geometry catalog is organized by which geometric constant appears in the correction:

| Boundary geometry | Correction involves | Source of R_n |
|---|---|---|
| Sphere | R₂ = π/4 | Single circle (S¹) in cross-section |
| Disk | R₂ = π/4 | Single circle (same as sphere cross-section) |
| Torus | R₄ = π²/32 | Two circles (T² = S¹ × S¹) |
| Oblate spheroid | R₂ × eccentricity | Circle deformed by flattening |
| Shell | R₂ × thickness ratio | Two concentric spheres |
| Polyhedron | Pure rationals | No circular content — flat faces |

The R_n value indexes the geometric complexity of the boundary. Simple boundaries (sphere, disk) produce R₂. Compound boundaries (torus) produce R₄. Non-circular boundaries (polyhedra) produce pure rationals without π. This hierarchy constrains the correction: if the empirically extracted per-transit rational involves π² (= 32R₄), the dominant boundary type is toroidal. If it involves only π (= 4R₂), the dominant type is spherical. If it involves no π, the dominant type is polyhedral or non-geometric.

---

## CHAPTER 5: THE THREE ORIENTATION TRACKS

### 5.1 The Exhaustive Classification

Any observed distribution of child soliton orientations within a parent boundary falls into exactly one of three tracks. The partition is exhaustive: either there's a preferred direction (Tracks 1 and 2) or there isn't (Track 3). If there is, either it's exact (Track 1) or approximate with explained deviations (Track 2).

Track 1: Universal alignment. All children share parent's symmetry axis. Prediction: zero scatter around the preferred direction.

Track 2: Preferred alignment with structured deviations. A ground state orientation exists, but perturbations produce a distribution around it. The distribution has a specific shape determined by the ratio of alignment energy to perturbation energy. Prediction: peaked distribution with explained tails.

Track 3: No preferred alignment. Orientations follow some other structural principle, or are random. The else clause. Prediction: not Track 1 or 2.

### 5.2 Track 1 — Universal Alignment

Logic: if the parent boundary imposes an energy minimum at alignment, and perturbations are negligible compared to the alignment energy, all children align exactly. This is the zero-temperature limit of the orientation energy landscape.

Empirical: no known system is perfectly Track 1. The closest is Saturn's rings (particles orbit within ~0.01° of the ring plane) and the inner solar system planets (within ~7° of the invariable plane). Both have small but nonzero scatter, making them technically Track 2 with small perturbations.

Math: Track 1 requires E_alignment ≫ E_perturbation. The alignment energy for a child soliton in a parent's field depends on the parent's geometry. A toroidal parent produces alignment energy proportional to the departure from the torus plane. A spherical parent produces zero alignment energy (no preferred direction). Track 1 is therefore only possible for non-spherical parents.

### 5.3 Track 2 — Preferred Alignment with Structured Deviations

Logic: the theta-vacuum argument from PHYS-7 applied to spatial orientation. The energy landscape is E(θ) = E₀ − χ · cos(θ), where θ is the misalignment angle and χ is the alignment strength determined by the parent geometry. The ground state is θ = 0 (aligned). Perturbations produce a Boltzmann distribution P(θ) ∝ exp(χ · cos(θ) / T_eff), where T_eff is the effective perturbation temperature (kinetic energy from formation, tidal torques, encounters). At low T_eff/χ, the distribution is sharply peaked (near Track 1). At high T_eff/χ, the distribution is nearly uniform (approaching Track 3).

Empirical: Track 2 dominates at every scale where data exists:

| Scale | Objects | Alignment strength | T_eff/χ | Track |
|---|---|---|---|---|
| Planetary orbits (solar system) | 8 planets | Strong (disk potential) | Low (~0.1) | Track 2, near Track 1 |
| Moons around planets | Various | Moderate | Moderate (~0.3) | Track 2, with retrograde exceptions |
| Stars in galactic disk | ~10¹¹ | Moderate (disk potential) | Moderate (~0.3) | Track 2 (disk heating) |
| Galaxy spins in filaments | Statistical | Weak | High (~0.8) | Track 2, approaching Track 3 |
| Galaxy orientations in clusters | Statistical | Very weak | Very high (~0.9) | Borderline Track 2/3 |
| Oort cloud orbits | ~10¹¹ | Zero (spherical parent) | Infinite (χ = 0) | Track 3 by construction |

The pattern: alignment strength decreases and T_eff/χ increases with scale. The effective temperature grows faster than the alignment energy as the system size increases. This is consistent with the alignment energy scaling with the parent's asphericity (which decreases for larger, more relaxed systems) while the perturbation energy scales with the formation violence (which increases for larger systems).

Math: the measurable quantity is the distribution of orientation angles at each scale. The distribution shape determines T_eff/χ. From T_eff/χ and the known T_eff (from velocity dispersions, tidal torque estimates), χ is extracted. From χ and the parent geometry, the alignment energy per unit asphericity is determined. This is a structural property of the soliton boundary — the analog of the topological susceptibility χ_top in the theta vacuum.

### 5.4 Track 3 — No Preferred Alignment

Logic: either the parent boundary is spherical (χ = 0, no preferred direction exists), or the alignment mechanism is something other than parent-axis inheritance, or the distribution is truly random (maximum entropy).

Empirical: the Oort cloud is the clearest Track 3 system — orbits are approximately isotropic, consistent with a spherical parent boundary (the solar system's gravitational Hill sphere is approximately spherical at the Oort cloud distance). Long-period comets arrive from all directions on the sky with no strong directional preference.

Math: for a spherical parent, E(θ) = E₀ (no θ dependence). All orientations are energetically equivalent. The distribution is uniform on S². Any deviation from uniformity at this scale indicates non-spherical parent structure or a non-gravitational alignment mechanism.

### 5.5 The Parent Geometry Determines the Child's Track

This is the key structural result of Chapter 5.

Logic: the alignment energy χ depends on the parent boundary's geometry. Spherical parent → χ = 0 → Track 3. Toroidal parent → χ > 0 proportional to aspect ratio → Track 1 or 2. Oblate spheroid → χ > 0 proportional to eccentricity → Track 2. The parent's shape determines the children's alignment, not any property of the children themselves.

Empirical: inner solar system (disk-like parent potential, Track 2 for planets) vs Oort cloud (spherical parent potential, Track 3 for comets). Milky Way disk (oblate parent, Track 2 for disk stars) vs Milky Way halo (spherical parent, Track 3 for halo stars and globular clusters).

Math: χ(geometry) can be computed from the parent boundary's multipole expansion. The quadrupole moment Q₂ determines the leading alignment energy: χ ∝ Q₂. For a torus, Q₂ ∝ (R² − r²)/(R² + r²). For an oblate spheroid, Q₂ ∝ (a² − c²)/(a² + c²). For a sphere, Q₂ = 0.

---

## CHAPTER 6: ORBITAL PARAMETERS AS SOLITON MODE STRUCTURE

### 6.1 The Reframing

Logic: before quantum mechanics, electron orbits were historical accidents. After quantum mechanics, they are standing wave modes of the Coulomb potential. The mode spectrum is determined by the boundary conditions (potential shape, boundary at infinity), not by how the electron got there. The same reframing applied to planetary orbits: the orbital parameters are standing wave modes of the gravitational soliton potential, determined by the boundary conditions (star mass, disk structure, outer boundary), not by the formation history.

The analogy is structural, not superficial. Both the atom and the planetary system have: a central attractive potential (Coulomb / gravitational), discrete bound states (orbitals / orbits), a mode spectrum determined by the potential shape, and perturbative corrections from inter-particle interactions (electron-electron repulsion / planet-planet gravitational interactions).

The key difference: quantum mechanics REQUIRES standing waves (the wave function must be single-valued). Classical gravity does not. Orbits at any radius are allowed by Newton's laws. The soliton mode proposal adds a constraint: the gravitational soliton has a boundary condition (at the Hill sphere, heliopause, or Oort cloud) that selects specific radii, the same way the atomic boundary condition (wave function → 0 at infinity) selects specific energy levels.

Empirical: the Titius-Bode law, Kepler peas-in-a-pod pattern, Kirkwood gaps, Saturn ring structure, resonant chains (TRAPPIST-1), and the Tully-Fisher relation for galaxies are all consistent with mode structure. None has been derived from a standing wave condition. The derivation is the research target.

Math: the standing wave condition on a potential V(r) selects radii where the "gravitational wave function" (the density or velocity field of the soliton) satisfies boundary conditions. For V(r) = −GM/r (Coulomb-like), the radii go as n² (Bohr). For V(r) ∝ ln(r) (thin disk), the radii go as 2^n (geometric/Titius-Bode). For a general potential, the mode spectrum is determined by the WKB quantization condition or its classical analog.

### 6.2 The Titius-Bode Law

The law: a_n ≈ 0.4 + 0.3 × 2^n AU, where n = −∞ (Mercury), 0 (Venus), 1 (Earth), 2 (Mars), 3 (gap/Ceres), 4 (Jupiter), 5 (Saturn), 6 (Uranus).

| n | Predicted (AU) | Planet | Actual (AU) | Error |
|---|---|---|---|---|
| −∞ | 0.4 | Mercury | 0.387 | 3% |
| 0 | 0.7 | Venus | 0.723 | 3% |
| 1 | 1.0 | Earth | 1.000 | 0% |
| 2 | 1.6 | Mars | 1.524 | 5% |
| 3 | 2.8 | Ceres | 2.767 | 1% |
| 4 | 5.2 | Jupiter | 5.203 | 0.1% |
| 5 | 10.0 | Saturn | 9.537 | 5% |
| 6 | 19.6 | Uranus | 19.19 | 2% |
| 7 | 38.8 | Neptune | 30.07 | 29% — FAILS |

Logic: the geometric progression (factor of 2 between successive orbits) is octave spacing. In standing wave physics, octave spacing means each mode is one octave above the previous — the fundamental frequency and its doublings. This is the mode spectrum of a specific class of potentials: those with logarithmic radial dependence. A self-gravitating thin disk has V(r) ∝ ln(r) at radii larger than the disk scale height. The solar system's protoplanetary disk was a self-gravitating thin disk. The standing wave condition on this potential produces geometric spacing.

The factor of 2 specifically is the most fundamental integer in the series' binary arithmetic framework. MATH-4 shows the universal denominator is 2³³⁵. MATH-5 shows n = 2 and n = 4 are uniquely doubly native to binary arithmetic. The Titius-Bode factor of 2 may be the geometric expression of binary arithmetic at the planetary scale.

The Neptune failure: Neptune at 30.07 AU does not match the n = 7 prediction of 38.8 AU (29% error). In the soliton mode picture, this is a MODE FAMILY TRANSITION. The outer solar system potential changes character around 30 AU (Kuiper belt begins, galactic tide becomes non-negligible). The inner mode family (Titius-Bode, disk potential, logarithmic) gives way to the outer mode family (different potential, different spacing). Neptune is the first member of the outer family, not the eighth member of the inner family.

Prediction: Kuiper belt objects should follow a different spacing law from the inner planets, determined by the outer solar system boundary geometry (more spherical, less disk-like). The known populations (classical belt 42–48 AU, plutinos 39.4 AU, scattered disk beyond 50 AU) may be the outer mode spectrum.

Empirical: Titius-Bode predicted Ceres (discovered 1801 at 2.77 AU, predicted 2.8 AU) and was consistent with Uranus (discovered 1781 at 19.2 AU, predicted 19.6 AU). Two successful predictions of then-unknown objects is unusual for "numerology." The pattern has been observed in exoplanetary systems: Bovaird & Lineweaver (2013) applied Titius-Bode to 68 multi-planet Kepler systems and found that the predicted positions of additional planets correlated with subsequently detected planets.

Math: the derivation program: (1) compute the gravitational potential of a self-gravitating disk with solar-system parameters (mass, radius, scale height). (2) Apply the standing wave (or WKB quantization) condition. (3) Compute the mode spectrum. (4) Compare to the Titius-Bode progression and to the actual planetary distances. If (4) matches, the orbital radii are derived from the potential, not from history.

### 6.3 Exoplanetary Systems

Logic: if orbits are soliton modes, every planetary system has a mode spectrum determined by its boundary parameters (host star mass, disk mass, outer boundary radius). Different boundary parameters produce different mode spectra. The diversity of observed exoplanetary systems (hot Jupiters, compact multis, widely spaced giants, resonant chains) corresponds to different boundary parameters, not different formation histories.

Empirical: Kepler discovered that compact multi-planet systems show regular spacing ("peas in a pod" — adjacent planets have similar sizes and nearly-equal period ratios). TRAPPIST-1 has seven planets in an unbroken resonant chain with period ratios close to small integers (8:5, 5:3, 3:2, 3:2, 4:3, 3:2). In the mode picture, the resonant chain IS the mode spectrum — the integer period ratios are integer relationships between mode numbers.

Math: the test is whether the mode spectrum from the host star's soliton potential reproduces the observed orbital architecture. For each system: (1) estimate the potential from the star's mass and radius. (2) Apply the standing wave condition. (3) Predict the orbital radii and period ratios. (4) Compare to observations. The test is falsifiable per system: if the predicted mode spectrum doesn't match the observed architecture for a specific system, the model fails for that system.

### 6.4 Kirkwood Gaps and Ring Gaps as Standing Wave Nodes

Logic: a standing wave has nodes (zeros) and antinodes (maxima). Objects accumulate at antinodes (stable positions) and are expelled from nodes (unstable positions). The Kirkwood gaps in the asteroid belt are at orbital radii where the period is a simple fraction of Jupiter's period (3:1, 5:2, 7:3, 2:1). In the mode picture, these ratios are the zeros of the standing wave — the nodes of the solar system soliton's mode spectrum, set by Jupiter as the dominant mode.

Empirical: the Kirkwood gaps are precisely located at the predicted resonance positions. The gap widths correlate with the resonance strength (low-order resonances produce wider gaps). Saturn's ring gaps (Cassini division, Encke gap, etc.) show the same structure: gaps at resonance positions with Saturn's moons, gap widths correlated with resonance strength.

Math: the node positions are determined by the mode spectrum. For a dominant mode at frequency ω_J (Jupiter's orbital frequency), the nodes are at radii where ω(r) = (p/q) × ω_J for small integers p, q. The node positions from this condition match the observed Kirkwood gap locations. The match has been known since Kirkwood (1866) — the standard explanation is orbital resonance clearing, which is the same mathematics (resonance = mode relationship) with a different interpretation (clearing by perturbation vs node of standing wave).

### 6.5 Galaxy Rotation Curves

Logic: the flat rotation curve is one of the strongest pieces of evidence for dark matter. The observed rotation velocity stays constant at large radii instead of falling as 1/√r (Keplerian). The standard explanation adds dark matter mass. The soliton mode explanation proposes that the rotation curve IS the mode spectrum of the galactic soliton, and the "missing mass" is the missing boundary correction — the depth-dependent reading of enclosed mass from inside the soliton boundary.

Empirical: the Tully-Fisher relation (luminosity ∝ v⁴, where v is the flat rotation velocity) holds across galaxies spanning orders of magnitude in luminosity. This tight correlation is naturally explained if both luminosity and rotation velocity are determined by the same structural parameter (the galactic soliton's mass/boundary configuration). The relation's tightness (small scatter) is difficult to explain if dark matter halos have independent properties from the visible galaxy.

MOND (Modified Newtonian Dynamics) phenomenology successfully predicts rotation curves from visible matter alone using a single acceleration scale a₀ ≈ 1.2 × 10⁻¹⁰ m/s². In the soliton framework, a₀ would be the acceleration at the galactic soliton boundary — the scale where the boundary correction becomes significant.

Math: derive the rotation curve from the galactic soliton geometry (oblate spheroid or thick torus) and the R₂/R₄ framework. The flat rotation curve requires that the enclosed "effective mass" (including boundary corrections) grows linearly with radius at large r. This constrains the soliton boundary's radial profile. The specific derivation is a primary research target.

### 6.6 The Beta Coefficient Analogy

Logic: the SM beta coefficient b₃ = −7 is derived from counting: 6 quarks × (2/3) − 11 = −7. Nobody says "b₃ = −7 because of the specific history of how the gauge field evolved." The value is determined by WHAT IS THERE (the particle content), not by how it got there. The proposal: orbital parameters are the same type of object. The semi-major axis of Jupiter is determined by the solar system soliton's mode spectrum (what boundary conditions are there), not by the specific history of Jupiter's formation.

Empirical: the SM betas ARE successfully derived from counting. The orbital parameters are currently NOT derived from anything. The research program is to establish the derivation.

Math: the counting for b₃ = (2/3) × n_f − 11. The counting for an orbital radius would be a_n = f(mode quantum numbers, boundary parameters). The function f is the gravitational analog of the beta coefficient formula. Its derivation from the standing wave condition on the soliton potential is the central mathematical challenge.

---

## CHAPTER 7: THE TOROIDAL COSMOLOGY HYPOTHESIS

### 7.1 Looking Through the Donut Hole

Logic: a torus has two fundamentally different direction classes. Through the hole (short path across the void in the center): the line of sight crosses two boundary surfaces with a void between them. Around the ring (long path through the torus body): the line of sight stays inside the torus material. The boundary transit count and the correction factor differ dramatically between these two directions.

Empirical: the observed universe has large voids (KBC void, Eridanus supervoid — hundreds of Mpc across) and dense filaments (the cosmic web). If the large-scale structure has toroidal character, the voids might be views through the hole — directions with less material and fewer boundary transits. The KBC void (~600 Mpc local underdensity) has been proposed as a partial explanation for the Hubble tension through a local outflow effect. In the toroidal picture, it is the geometric signature of the hole.

Math: through-hole correction = r_torus_boundary × r_void(d) × r_torus_boundary, where d is the path through the hole. Around-ring correction = r_torus_body^(N_ring), where N_ring is the number of internal boundaries crossed around the full ring. The ratio of these two corrections determines the maximum directional H₀ variation.

### 7.2 The CMB as Directional Running Curve Map

Logic: if boundary corrections vary by direction (because the line-of-sight boundary structure varies with direction on the sky), the CMB temperature at each point encodes the cumulative correction for that line of sight. The CMB anisotropies would contain a component from the directional boundary correction, superimposed on the primordial acoustic oscillation signal.

Empirical: the CMB has unexplained large-scale anomalies: the hemispherical asymmetry (one half of the sky has slightly more power than the other), the quadrupole-octopole alignment ("axis of evil"), the cold spot (aligned with the Eridanus supervoid), and the lack of large-angle correlations. All of these are consistent with a directional component imposed by large-scale structure along the line of sight. None has been conclusively explained by standard ΛCDM cosmology.

The acoustic peaks in the CMB power spectrum are NOT explained by the boundary framework — they come from baryon acoustic oscillations at recombination and are well-predicted by ΛCDM with specific cosmological parameters. The boundary component would be a SMALL ADDITION to the well-understood acoustic signal, detectable primarily at large angular scales (low multipoles) where the primordial signal is weak and the anomalies reside.

Math: the Planck lensing map measures the projected mass density along each line of sight. The boundary correction map should correlate with the lensing map (more mass = more boundaries = more correction). The cross-correlation between CMB temperature residuals (after removing best-fit ΛCDM) and the lensing map would contain the boundary signal if it exists. This cross-correlation has been measured by Planck — the question is whether the measured signal contains a component beyond standard lensing theory.

Falsification: if CMB temperature residuals show zero correlation with the projected mass density beyond what standard lensing predicts, the directional boundary correction is absent at the CMB's precision.

### 7.3 Nested Boundaries: Torus in Sphere, Torus in Torus

Logic: the correction through the hole of a torus depends on what fills the hole — the outer boundary's interior regime. A torus inside a sphere sees spherical-interior properties through the hole (isotropic, R₂-based correction across the gap). A torus inside another torus sees the outer torus's body or hole depending on relative orientation (anisotropic, R₄-based correction varying with angle).

The nesting hierarchy for our observing position: Earth's Hill sphere (sphere) → solar system disk (torus) → solar system Hill sphere (sphere) → Milky Way disk (torus) → Milky Way halo (sphere) → Local Group (irregular) → Virgo/Laniakea supercluster (flattened) → cosmic web (filaments + voids — toroidal or more complex topology).

Each level contributes its geometry's rational correction factor. The total correction for a specific direction is the product of all factors along that line of sight.

Empirical: we know the geometry at each level (disk, sphere, flattened, etc.) from observations. The nesting structure is observable. What is NOT known is the per-level correction factor. The decomposition of the total observed correction (0.923 from H₀ tension) into per-level factors requires either a top-down derivation (from each geometry's R₂/R₄ content) or a statistical decomposition (fitting the directional H₀ variation to the known nesting geometry).

Math: the total directional correction is:

H₀(θ, φ) = H₀(local) × Π_levels r_level(geometry_level, angle_level(θ,φ), path_length_level(θ,φ))

where (θ, φ) is the sky direction and each level contributes its factor. This is a product of known geometries with unknown per-level correction magnitudes. The fitting problem has as many free parameters as nesting levels (~6–8), which is borderline for the available directional H₀ data. More directional H₀ measurements would overdetermine the fit.

### 7.4 The Expanding Torus

Logic: if the universe (or our local patch) has toroidal structure, "expansion" has richer meaning than for a sphere. A torus can: expand its major radius R (the ring grows), expand its minor radius r (the tube thickens), circulate material through the cross-section (flow around the tube), or do all three simultaneously. What we call "Hubble expansion" is dR/dt. The circulation velocity adds a direction-dependent component to the apparent recession velocity.

Empirical: observed galaxy flows show bulk motion toward the Great Attractor and along filaments. These flows are attributed to gravitational attraction from overdensities. In the toroidal picture, they could also include the circulation component — material flowing through the torus cross-section, which would appear as systematic motion toward/away from specific directions on the sky.

Math: the apparent recession velocity for an object at angle α relative to the torus axis and distance d along the torus body:

v_apparent = H₀ · d + v_circulation · f(α, d)

where f(α, d) is the projection of the circulation velocity onto the line of sight. The circulation component produces a dipole modulation of the Hubble flow aligned with the torus axis. This is observationally similar to the CMB dipole (currently attributed entirely to our peculiar motion). Part of the dipole might be the torus circulation.

Falsification: if the CMB dipole is entirely explained by our measured peculiar velocity (from galaxy surveys), no circulation component exists. If a residual remains after subtracting the peculiar velocity prediction, the residual could be the circulation signal.

---

## CHAPTER 8: THE UNIFIED FRAMEWORK

### 8.1 The Chain of Determination

The five concept threads connect through a single chain:

**The geometry determines the rationals.** Spherical boundaries → R₂ = π/4. Toroidal boundaries → R₄ = π²/32. Polyhedral node structures → pure rationals. The geometry of each soliton boundary determines which correction factor it produces. This is established by MATH-1 for engineering cross-sections and proposed for extension to soliton boundaries.

**The rationals determine the mode spectrum.** The standing wave condition on a potential shaped by the soliton boundary selects specific modes. The mode frequencies and radii are exact rationals (or rationals × R₂/R₄) determined by the boundary geometry. This is established for the atom (Coulomb potential → n² radii) and proposed for gravitational solitons (disk potential → 2^n radii).

**The mode spectrum determines the running curve.** Each boundary has a mode structure. Light crossing the boundary interacts with the mode structure. The per-transit correction depends on the mode density and geometry. The cumulative correction along a line of sight is the running curve. This is established for α running (VP modes → 1/(12R₂) per flavor) and proposed for H₀ running.

**The running curve determines the observables.** H₀(direction), CMB anisotropies, rotation curves, planetary spacing — all derivable from the same framework. Each observable is a measurement through a specific set of soliton boundaries, and the measurement result is the local value modified by the cumulative boundary corrections.

**Everything connects through R₂/R₄.** The geometric constants from MATH-1 and MATH-5 appear at every level. R₂ for spherical/2D operations. R₄ for toroidal/4D operations. The binary arithmetic of MATH-4 (2³³⁵ denominator) provides the computational substrate. The factor of 2 in Titius-Bode is the same factor of 2 that makes n = 2 and n = 4 doubly native to binary arithmetic.

### 8.2 What Is Established vs What Is Proposed

| Element | Status | Evidence level |
|---|---|---|
| α running through boundaries at 0.02 ppm | Established (PHYS-5) | Math verified, empirical confirmed |
| Beta coefficients from particle counting | Established (PHYS-5, gauge_coupling_2.py) | Math verified, empirical confirmed |
| R₂ in all nine physics domains | Established (PHYS-11) | Math verified (Fraction identities), empirical confirmed |
| Confinement two-face structure | Established (PHYS-6) | Empirical confirmed, math approximate (±5%) |
| H₀ running curve | Proposed (this notebook) | Empirical suggestive (monotonic trend), math not yet computed |
| Soliton boundary taxonomy | Proposed (this notebook) | Empirical partial (coherence spectrum observed), math not yet computed |
| Toroidal boundaries → R₄ corrections | Proposed (this notebook) | Logic sound, empirical untested, math to be derived |
| Orbital parameters as mode structure | Proposed (this notebook) | Empirical suggestive (Titius-Bode, Kirkwood), math to be derived |
| Toroidal cosmology | Speculative (this notebook) | Logic consistent, empirical hints (CMB anomalies, voids), math not yet computed |

### 8.3 The Kill Switch Hierarchy

Level 1 (kills everything): if the α running from PHYS-5 is wrong (0.02 ppm result fails independent verification), the entire framework collapses. Status: verified, this gate is passed.

Level 2 (kills Chapters 2, 7): if intermediate H₀ measurements don't fall on any smooth curve, the running curve thesis dies. Chapters 3–6 survive independently.

Level 3 (kills Chapter 6): if the Titius-Bode derivation from standing wave conditions fails (wrong number of modes, wrong radii), the mode structure proposal dies. Chapters 2–5, 7 survive independently.

Level 4 (kills Chapter 4 partially): if the empirically extracted per-transit correction has no rational content (irrational, no R₂/R₄ structure), the geometry catalog loses its predictive power. The taxonomy (Chapter 3) and running curve (Chapter 2) survive without the geometric identification.

Level 5 (kills Chapter 7): if the CMB has no directional H₀ variation correlated with large-scale structure, the toroidal cosmology hypothesis is not supported at CMB precision. All other chapters survive.

---

## CHAPTER 9: THE RESEARCH PROGRAM

### 9.1 Calibration (Priority 1)

These computations reproduce known results using the framework. If they fail, the framework is wrong at the corresponding scale.

**C1: α running.** Already done (PHYS-5, 0.02 ppm). The calibration is passed. This establishes that the boundary framework reproduces the most precisely measured boundary-crossing effect in physics.

**C2: Titius-Bode from standing wave condition.** Compute the gravitational potential of the solar system's self-gravitating disk. Apply the WKB or standing wave quantization condition. Compute the mode spectrum. Compare to actual planetary distances for Mercury through Uranus (the inner mode family).

Kill switch: if the mode spectrum gives the wrong number of modes (not 7–8) or wrong spacing (not approximately geometric with factor ~2), the standing wave proposal fails for the solar system.

**C3: Kirkwood gap positions from mode nodes.** Compute the nodes of the solar system soliton's mode spectrum in the asteroid belt region (2.1–3.3 AU). Compare to the known Kirkwood gap positions (3:1 at 2.50 AU, 5:2 at 2.82 AU, 7:3 at 2.95 AU, 2:1 at 3.27 AU).

Kill switch: if the computed nodes don't match the observed gaps, the mode interpretation of the Kirkwood gaps fails.

**C4: Saturn ring gap positions from mode nodes.** Same computation for Saturn's ring system using Saturn's potential and the known moon resonances. Compare to Cassini division, Encke gap, and other observed ring gaps.

Kill switch: if ring gap positions don't match computed nodes, the mode interpretation fails for ring systems.

### 9.2 Extraction (Priority 2)

These computations extract unknown parameters from existing data.

**E1: H₀ running curve fit.** Estimate effective N for each of the five H₀ measurement methods using published structure catalogs. Fit H₀(N) = H₀(0) × r^N. Extract r. Express r as a Fraction. Check for R₂/R₄ content.

**E2: CMB directional H₀ variation.** Cross-correlate CMB temperature residuals (after removing best-fit ΛCDM) with Planck lensing map. Test for a component beyond standard lensing theory. If detected, fit to the known nesting geometry to extract per-level correction factors.

**E3: Exoplanet spacing fit.** For each Kepler multi-planet system with 4+ detected planets, fit the orbital radii to a mode spectrum. Extract the potential parameters per system. Test whether the extracted parameters correlate with host star properties (mass, radius, rotation rate).

**E4: Galaxy rotation curve fit.** For a sample of well-measured galaxy rotation curves (THINGS survey, SPARC database), fit each curve to the soliton mode prediction. Extract the boundary parameters per galaxy. Test whether the extracted parameters correlate with galaxy morphology and the Tully-Fisher relation.

### 9.3 Prediction (Priority 3)

These computations predict unmeasured quantities before observation.

**P1: H₀ at specific intermediate redshifts.** From the extracted running curve (E1), predict H₀ at redshifts z = 0.1, 0.5, 1.0, 2.0 before future measurements at those redshifts.

**P2: Exoplanet orbital radii for new systems.** From the potential-to-mode-spectrum mapping (E3), predict orbital radii for newly discovered multi-planet systems from host star parameters alone, before the orbits are measured.

**P3: Rotation curve shape from galaxy morphology.** From the soliton mode mapping (E4), predict rotation curves for galaxies with known morphology but unmeasured rotation curves.

**P4: Direction of maximum H₀ on the sky.** From the toroidal cosmology hypothesis (E2), predict which sky direction gives the highest local H₀ (through the "hole") and which gives the lowest (around the "ring"). Test against future directional H₀ measurements.

### 9.4 Falsification Matrix

| Prediction | Test | Falsifying result | Status |
|---|---|---|---|
| H₀ monotonically decreases with N | Plot H₀ vs estimated N | Non-monotonic or flat | Not yet tested |
| r is a recognizable rational | Express fitted r as Fraction | Irrational or no R₂/R₄ content | Not yet tested |
| Titius-Bode from standing wave | Compute mode spectrum | Wrong number or spacing of modes | Not yet tested |
| Kirkwood gaps are mode nodes | Compute node positions | Nodes don't match gaps | Not yet tested |
| Ring gaps are mode nodes | Compute node positions | Nodes don't match gaps | Not yet tested |
| Exoplanet spacing follows mode spectrum | Fit mode model to Kepler systems | Poor fit quality | Not yet tested |
| Rotation curves from soliton modes | Fit soliton model to THINGS/SPARC | Poor fit or no Tully-Fisher correlation | Not yet tested |
| CMB has directional H₀ component | Cross-correlate residuals with lensing | Zero cross-correlation beyond standard lensing | Not yet tested |
| Voids contribute opposite-sign correction | Compare H₀ through voids vs clusters | Same H₀ in both directions | Not yet tested |
| GW and EM H₀ curves diverge at high z | Compare standard siren H₀ to EM H₀ | Identical curves | Not yet tested (insufficient GW events) |
| Orientation tracks follow parent geometry | Measure alignment vs parent asphericity | No correlation | Partially tested (Table in 5.3) |

### 9.5 The Kill Switch Hierarchy (Repeated for Reference)

1. If α running (PHYS-5) fails → everything dies. STATUS: PASSED.
2. If H₀ curve is not monotonic → Chapters 2, 7 die. Others survive.
3. If Titius-Bode derivation fails → Chapter 6 dies. Others survive.
4. If r has no rational content → Chapter 4 loses prediction. Others survive.
5. If no directional CMB variation → Chapter 7 dies. Others survive.

Each chapter can die independently without killing the others, EXCEPT Chapter 1 (the series foundation), which is a dependency for all other chapters.

---

## APPENDIX A: PAPER-BY-PAPER FOUNDATION TABLE

| Chapter | Depends on papers | Specific results used |
|---|---|---|
| Ch. 1 (foundation) | All HOWL papers read | Context transfer |
| Ch. 2 (H₀ curve) | PHYS-1 (anomaly correlation), PHYS-2 (transformation law priority), PHYS-4 (per-transit constraint, Appendix G), PHYS-5 (VP running as template), PHYS-6 (kernel dependence) | Monotonic H₀ trend, 0.923 ratio, structure counts |
| Ch. 3 (taxonomy) | PHYS-1 (boundary catalog), PHYS-3 (Hill sphere), PHYS-6 (two-face structure, composite boundaries) | Coherence spectrum, collective formation conditions |
| Ch. 4 (geometry) | MATH-1 (β = R₂), MATH-5 (R_n sequence), PHYS-11 (nine domains, R₂ universal, R₄ in 4D) | R₂/R₄ framework, geometry-to-rational mapping |
| Ch. 5 (orientation) | PHYS-7 (ground state argument, E(θ) = E₀ − χ·cos(θ)) | Alignment as ground state, perturbation as excitation |
| Ch. 6 (mode structure) | PHYS-5 (beta coefficients from counting), PHYS-11 (phase-periodic domains, Subgroup A), MATH-1 (geometric invariant) | Counting derivation template, standing wave domains |
| Ch. 7 (toroidal cosmology) | PHYS-1 (boundary transit), PHYS-3 (nested hierarchy), PHYS-6 (kernel dependence), PHYS-11 (R₄ from T²) | Directional corrections, nesting products, R₄ from torus |
| Ch. 8 (unified) | All above | Chain of determination |
| Ch. 9 (program) | PHYS-4 (calibration-first, kill switch) | Test methodology |

## APPENDIX B: GEOMETRY CATALOG

| Geometry | Topology | R_n content | Correction type | Physical examples |
|---|---|---|---|---|
| Sphere | S² | R₂ = π/4 | Cross-section: 4R₂r² | Hill spheres, VP clouds, halos, CMB |
| Disk | D² | R₂ = π/4 | Area: 4R₂r² | Protoplanetary, galactic, accretion |
| Torus | T² | R₄ = π²/32 (through R₂²) | Volume: 128R₄Rr² | Rings, belts, disk-with-hole |
| Oblate spheroid | S² deformed | R₂ × e(eccentricity) | Cross-section: 4R₂ac | Galaxies, rotating stars |
| Shell | S² × I | R₂ × (r₂/r₁) | Nested spheres | Planetary nebulae, Oort cloud |
| Cylinder | S¹ × I | R₂ in cross-section | Cross-section: 4R₂r² | Jets, filaments |
| Tetrahedron | 4 faces | Pure rational | 1/3 of bounding box (approx) | sp³ nodes |
| Cube | 6 faces | 1 (fills box) | Trivial | Crystal lattice |
| Octahedron | 8 faces | Pure rational | √2/3 of bounding box | d-orbital nodes |
| Dodecahedron | 12 faces | Involves φ | φ-dependent rational | Possible quark config |
| Icosahedron | 20 faces | Involves φ | φ-dependent rational | Capsids |
| Truncated icosahedron | 32 faces | Involves φ | φ-dependent rational | C₆₀, maximum allowed |

## APPENDIX C: DATA TABLES

### C.1 H₀ Measurements

| Method | H₀ (km/s/Mpc) | ±σ | Effective N (estimated) | Source |
|---|---|---|---|---|
| SH0ES | 73.0 | 1.0 | ~10–50 | Riess et al. 2022 |
| H0LiCOW | 73.3 | 1.8 | ~50–100 | Wong et al. 2020 |
| CCHP (TRGB) | 69.8 | 1.7 | ~10–50 | Freedman et al. 2021 |
| DES+BAO+BBN | 67.4 | 1.2 | ~1000+ | DES Collaboration 2022 |
| Planck CMB | 67.4 | 0.5 | Maximum | Planck Collaboration 2020 |

### C.2 Planetary Distances (Titius-Bode)

| Planet | Actual a (AU) | Titius-Bode a (AU) | Error (%) | Mode number n |
|---|---|---|---|---|
| Mercury | 0.387 | 0.4 | 3.4 | −∞ (offset) |
| Venus | 0.723 | 0.7 | 3.2 | 0 |
| Earth | 1.000 | 1.0 | 0.0 | 1 |
| Mars | 1.524 | 1.6 | 5.0 | 2 |
| Ceres | 2.767 | 2.8 | 1.2 | 3 |
| Jupiter | 5.203 | 5.2 | 0.1 | 4 |
| Saturn | 9.537 | 10.0 | 4.9 | 5 |
| Uranus | 19.19 | 19.6 | 2.1 | 6 |
| Neptune | 30.07 | 38.8 | 29.0 | FAILS — mode family transition |

### C.3 Kirkwood Gap Positions

| Resonance with Jupiter | Gap center (AU) | Orbital period ratio | Node interpretation |
|---|---|---|---|
| 4:1 | 2.06 | 0.250 | Fourth harmonic node |
| 3:1 | 2.50 | 0.333 | Third harmonic node |
| 5:2 | 2.82 | 0.400 | Fifth harmonic, second node |
| 7:3 | 2.95 | 0.429 | Seventh harmonic, third node |
| 2:1 | 3.27 | 0.500 | Second harmonic node |

### C.4 CMB Anomalies Potentially Related to Directional Boundary Corrections

| Anomaly | Angular scale | Description | Possible boundary interpretation |
|---|---|---|---|
| Hemispherical asymmetry | l = 2–600 | One hemisphere has ~7% more power | Asymmetric boundary correction from off-center position in local structure |
| Quadrupole-octopole alignment | l = 2, 3 | Low multipoles aligned along a common axis | Toroidal boundary axis |
| Cold spot | ~10° | Anomalously cold region | Eridanus supervoid — fewer boundary transits in this direction |
| Low quadrupole power | l = 2 | Quadrupole amplitude lower than expected | Boundary correction partially cancels primordial quadrupole |

## APPENDIX D: ORIENTATION TRACKS PER SCALE

| Scale | System | Parent geometry | χ (alignment energy) | T_eff/χ | Track | Evidence |
|---|---|---|---|---|---|---|
| Planetary | Solar system planets | Disk (toroidal) | Strong | ~0.1 | 2 (near 1) | Inclinations 0.3°–7°, Pluto 17° |
| Satellite | Major moons | Planet equatorial bulge | Moderate | ~0.3 | 2 | Most equatorial, some retrograde |
| Stellar | Disk stars | Galactic disk | Moderate | ~0.3 | 2 | Velocity dispersion increases with age |
| Galactic | Galaxy spins in filaments | Filament (cylindrical) | Weak | ~0.8 | 2 (near 3) | Statistical alignment detected |
| Cluster | Galaxy orientations in clusters | Cluster (roughly spherical) | Very weak | ~0.9 | 3 (or weak 2) | Mixed observational results |
| Cometary | Oort cloud orbits | Hill sphere (spherical) | Zero | ∞ | 3 | Isotropic comet arrival directions |

## APPENDIX E: GLOSSARY

| Notebook term | Standard physics term | Series paper where established |
|---|---|---|
| Soliton boundary | Coherent structure boundary / phase boundary | PHYS-1 |
| Running curve | Scale-dependent measurement / RG evolution | PHYS-2 |
| Boundary transit | Measurement through a coherent structure | PHYS-1 |
| Mode spectrum | Standing wave eigenvalues / energy levels | PHYS-11 (domains 3–5) |
| R₂ | π/4, the circle-to-square geometric remainder | MATH-1, MATH-5, PHYS-11 |
| R₄ | π²/32, the 4-ball geometric remainder | MATH-5, PHYS-11 |
| Per-transit correction | Boundary crossing correction factor | PHYS-4 (identified as missing) |
| Kernel dependence | Observable-dependent weighting of boundary faces | PHYS-6 |
| Ground state orientation | Energy-minimizing alignment of nested solitons | PHYS-7 (applied to θ_QCD) |
| Gap ratio | (b₁−b₂)/(b₂−b₃), tests particle content completeness | PHYS-5 |
| Two-face boundary | Boundary with distinct perturbative and non-perturbative regimes | PHYS-6 |
| Coherence class | How strongly a structure's boundary separates interior from exterior | This notebook (Chapter 3) |
| Anti-boundary | Void boundary with opposite-sign correction | This notebook (Chapter 3.4) |
| Mode family transition | Change in standing wave boundary conditions at a structural boundary | This notebook (Chapter 6.2) |

---

**End of super notebook. Status: active research document. All chapters are live. The research program (Chapter 9) specifies the next computations. The kill switch hierarchy (Chapter 8.3) specifies what kills what. Updated: Session 4, April 2 2026.**
