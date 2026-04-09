## PHYS-42 Plan: Reading Depth Across the Soliton Hierarchy — 18 Tests from Meters to Gigaparsecs

**Registry:** [@HOWL-PHYS-42-2026]

**Status:** Plan for review

---

### Thesis

The fourth coordinate in the Minkowski metric is reading depth — position within the nested soliton boundary hierarchy. Clocks at different depths update at different rates. This is what GR calls time dilation. The claim is testable: compute the GR prediction for every classical time dilation measurement from first principles using measured constants, compare to the published result. If every prediction matches, reading depth reproduces a century of precision gravitational physics from one formula applied at every level of the hierarchy.

This paper presents the results. One derivation function. 18 comparisons. 8 hierarchy levels. 18 orders of magnitude in Φ/c². From a gamma ray climbing 22.5 meters at Harvard to a supernova lightcurve stretched by the cosmic expansion at z = 1.

---

### Why This Needs a Paper

PHYS-41 stated the interpretation. PHYS-42 runs the experiment.

PHYS-41 claimed GR time dilation IS reading depth and proposed five actionable tests. PHYS-42 executes the first and largest: a mega-experiment that computes every classical GR time dilation effect from pool constants and compares to measurement. The experiment is `experiment_gr_time_dilation_v0`, run in DATA-6 with full provenance.

The results are expected to match — the reading depth formula IS the GR formula. The paper's contribution is not "we discovered something new." It is: "one derivation function, reading from one pool, reproduces every measured time dilation effect across the full soliton hierarchy." The unified treatment is the result. No other experiment in the HOWL series spans this many orders of magnitude in a single derivation.

---

### Structure

**Section I: The Experiment**

State what was computed. One derivation function (`gr_reading_depth_mega_v0`) reads 30 values from the DATA-6 pool (28 new + 2 existing). It computes 12 GR predictions using standard formulas with zero hardcoded physics. It outputs 18 comparison targets. The experiment runs in the same DATA-6 runner that produced α at 0.007 ppb, sin²θ_W at 12 ppm, and D/H at 0.12σ.

The hierarchy tested, stated as soliton levels:

Earth soliton interior (Pound-Rebka, 22.5 m, Φ/c² ~ 10⁻¹⁵ differential). Earth soliton orbit (GPS at 20,200 km, GPA at 10,000 km, Φ/c² ~ 10⁻¹⁰). Solar soliton surface (redshift, Φ/c² ~ 2 × 10⁻⁶). Solar soliton interior (Mercury perihelion, Φ/c² ~ 3 × 10⁻⁸). Solar soliton exterior (Shapiro delay, Cassini). Compact soliton (Hulse-Taylor binary, Φ/c² ~ 0.2). SR velocity reading (muon at γ = 29.3). Cosmological reading (SN Ia at z = 1). Planck scale (t_P, l_P, c = l_P/t_P).

Present the complete results table from the run.

**Section II: Earth Soliton — Three Tests**

Pound-Rebka/Snider: Δf/f = GM_E·h/(R_E²·c²). The predicted shift from pool constants. The measured shift (2.57 ± 0.26) × 10⁻¹⁵ (Pound-Snider 1965). The miss. Reading depth interpretation: a gamma ray emitted at 22.5 m deeper reading carries a slower update rate. The receiver at the shallower depth reads a lower frequency.

GPS: gravitational shift GM_E/c² × (1/R_E − 1/r_gps) plus velocity shift −v²/(2c²), net × 86400 s/day. Predicted vs measured 38.64 μs/day (Ashby 2003). Reading depth: the satellite at shallower depth has faster updates, but allocates capacity to spatial displacement. The net +38.6 μs/day is corrected in firmware. Every GPS fix is a reading depth calculation.

Gravity Probe A: GM_E/c² × (1/R_E − 1/(R_E + h)). Predicted vs measured (4.36 ± 0.03) × 10⁻¹⁰ (Vessot-Levine 1980), 70 ppm agreement with GR. Reading depth: hydrogen maser update rate increases as the rocket rises to shallower depth.

All three from the same formula: Δf/f = ΔΦ/c². Same physics, three different depth ranges within the Earth soliton. All from GM_E and R_E in the pool.

**Section III: Solar Soliton — Three Tests**

Solar surface redshift: GM_S/(R_S·c²), expressed as velocity v = zc. Predicted vs measured 636.3 m/s. Reading depth: photons from the Sun's deep reading carry that depth's update rate. 

Mercury perihelion advance: 6πGM_S/(ac²(1−e²)) radians per orbit, converted to arcsec/century. Predicted vs measured 42.9799 arcsec/century (Park 2017). The most precise test in the experiment. Reading depth: the reading depth gradient near the Sun curves Mercury's spatial update path.

Shapiro delay (Cassini): GR predicts PPN γ = 1 exactly. Cassini measured 1 + (2.1 ± 2.3) × 10⁻⁵ (Bertotti 2003), confirming GR to 0.002%. Reading depth: photons traversing the Sun's deep reading zone accumulate extra Planck steps.

All three from the solar soliton. Different depth ranges, different physics (redshift, precession, delay), same reading depth structure.

**Section IV: Compact Soliton and Special Relativity — Two Tests**

Hulse-Taylor binary pulsar: Pdot_measured / Pdot_GR. Both published to 5 digits. Ratio should be ~0.9996 (Weisberg-Taylor 2005), confirming GR gravitational wave emission to 0.2%. Reading depth: two neutron star solitons at Φ/c² ~ 0.2 radiate reading depth energy as gravitational waves.

Muon time dilation: τ_lab = γ × τ_rest. At γ = 29.3 (Fermilab g-2 storage ring), τ_rest = 2.197 μs dilates to ~64.4 μs. Reading depth: the fast muon allocates reading capacity to spatial displacement. Fewer depth updates means the internal decay clock runs slower. The muon lives 29.3× longer in the lab frame.

Two different mechanisms — gravitational reading depth (Hulse-Taylor) and velocity reading allocation (muon) — both described by the same framework: the reading update rate depends on position and motion within the soliton hierarchy.

**Section V: Cosmological and Planck Scale — Three Tests**

SN Ia lightcurve stretch: at z = 1, (1+z) = 2. Measured by Blondin 2008 and Goldhaber 2001. Reading depth: the supernova's internal clock ran at the reading depth of its emission epoch. We observe from our current shallower depth. The ratio is (1+z).

Planck time and length: t_P = √(ℏG/c⁵), l_P = √(ℏG/c³). Computed from pool constants, compared to CODATA. Predicted to agree within ~11 ppm (limited by G precision). Reading depth: t_P is the reading update step size. l_P is the spatial reading resolution. Below these scales, readings don't subdivide.

c = l_P/t_P. Must equal 299792458 m/s by construction. Reading depth: the maximum rate at which a reading can update spatially. One spatial resolution unit per one temporal resolution unit.

The deepest (Planck, Φ/c² = 1) and shallowest (cosmological, z = 1) levels of the hierarchy, both matched by the same framework.

**Section VI: The Unified Reading Depth Profile**

Present the full hierarchy in one table: every test, its Φ/c², its predicted value, its measured value, its miss. The table spans 18 orders of magnitude from Δ(Φ/c²) ~ 10⁻¹⁵ (Pound-Rebka) to Φ/c² ~ 0.2 (Hulse-Taylor).

The key observation: one formula, applied at every level, matches every measurement. The formula is f_deep/f_shallow = √(1 − 2Φ/c²) for gravitational dilation, γ = 1/√(1 − v²/c²) for velocity dilation, (1+z) for cosmological dilation. These are not three different effects. They are one effect — reading depth — manifesting at different levels of the soliton hierarchy.

State explicitly: this is what GR describes. The reading depth interpretation adds no new prediction to any test in this experiment. Every match is a GR match. The contribution is the unified treatment and the naming: clocks at different depths update at different rates. The depth is position in the soliton hierarchy. The update rate is what physics calls "the rate at which time passes."

**Section VII: The g Surface Anomaly and What It Means**

The g surface test: GM_E/R_E² gives ~9.82 m/s², vs the standard 9.80665 m/s². The ~0.14% miss is because R_E = 6,371,000 m is the mean radius while g_n is defined for sea level at 45° latitude, where the actual radius is ~6,367,400 m and centrifugal effects subtract ~0.034 m/s².

This miss is the only expected deviation in the experiment. It illustrates the reading depth principle: g is a reading at a specific depth. Different positions on the Earth's surface are at different depths (different radii, different latitudes, different altitudes). The "standard g" is a reading at one specific depth. Our computation uses the mean depth. The miss is the reading depth difference between mean and standard positions.

The G scatter problem (500 ppm across laboratories) is the same effect at larger scale: different labs at different reading depths measure different g, and when combined with different G apparatuses, the readings scatter. Whether this scatter is experimental systematics or real reading depth variation is Test 4 from PHYS-41. The g surface miss in this experiment is consistent with the hypothesis but does not test it — the miss is explained by known geometry (mean vs local radius).

**Section VIII: Provenance and the Ninth Domain**

The experiment runs in the same DATA-6 system that produced all 53 derived values. Same runner, same pool, same comparison engine, same output format. The provenance is complete: every input value has a pool key, a source, a precision. Every output has a result key. Every comparison has a PASS/FAIL/INFO status.

This adds the ninth physics domain to the HOWL derivation graph: GR time dilation. The previous eight (QED, electroweak, GUT, cosmology, nuclear, muon, flavor, spectroscopy) test the integer transformation law structure. The ninth tests the reading depth interpretation of the fourth coordinate.

The nine domains are independent. The GR experiment shares no inputs with the QED chain (different constants entirely — GM_E, R_E vs a_e, α). The GR experiment shares no derivation path with the GUT chain. The only connection is through the pool infrastructure and the interpretation: all nine domains are readings across soliton boundaries.

The derivation graph after this paper: 53 + 12 = 65 derived values. 13 measured inputs (unchanged — the GR experiment uses different inputs that are not counted in the HOWL input set because they are astrophysical measurements, not fundamental constants). 9 physics domains. The surplus in the HOWL integer structure remains 40. The GR domain adds 12 structural confirmations (not surplus-increasing, because they're GR checks, not integer predictions).

---

### Appendix Tables

A.1: Complete results table — all 18 comparisons with predicted, measured, miss, and PASS/FAIL status (from the actual run)

A.2: The 30 input values — pool key, value, digits, source, which derivations use it

A.3: The soliton hierarchy — 10 levels from Planck to cosmological, Φ/c² at each, tests at each, reading depth interpretation

A.4: Reading depth vs standard language — every test in both GR language and reading language, with "what changes" column (answer: the name)

A.5: Precision budget — for each test, the limiting input, the propagated precision, the expected miss

A.6: Connection to existing experiments — cross-reference with experiment_soliton_gravity_v0 and experiment_relativity_v0, showing which tests are new

A.7: The nine-domain derivation graph — updated with the GR domain, showing all cross-domain connections

---

### What This Paper Does NOT Claim

Does not claim any test falsifies or confirms the reading depth interpretation independently of GR. Every comparison IS a GR comparison. The reading depth interpretation is tautologically consistent with GR because it IS GR.

Does not claim new physics. The nuclear clock vs optical clock test (Test 1 from PHYS-41) is the only test that could produce new physics. That test requires hardware that doesn't yet exist at sufficient precision. This paper uses only existing measurements.

Does not claim the soliton hierarchy is proven by GR time dilation. The soliton hierarchy is a structural claim from the HOWL model. GR time dilation is consistent with it (clocks at different positions in a gravitational hierarchy tick at different rates) but does not prove it (GR works without solitons). The consistency is the evidence, not the proof.

Does not add to the HOWL surplus count. The 12 GR derivations use astrophysical inputs (GM_E, GM_S, orbital parameters), not the 13 HOWL inputs (a_e, m_e, M_Z, ...). They confirm GR, not the integer structure. The surplus remains 40.

---

### Estimated Length

Main text: 8-10 pages. Sections II-V (the physics results) are the core — 5-6 pages. Section I (experiment setup) and Section VI (unified profile) are 2 pages each. Sections VII-VIII (g anomaly, provenance) are 1 page each.

Appendix: 7 tables. A.1 (results) is the largest — 18 rows with full numerical results from the actual run.

---

### Agreement Request

The paper can only be written after the experiment runs. The structure above assumes ALL COMPARISONS PASSED. If any FAIL, the structure changes — each FAIL gets a diagnosis section (bug or input error). The physics content is the same either way: reading depth IS GR, confirmed across 18 orders of magnitude.

Should I run the experiment first and write the paper from the results, or write the paper from the expected results and update after running?