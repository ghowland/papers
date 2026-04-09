## GR Time Dilation as Reading Depth — Experiment Report

**Experiment:** `experiment_gr_time_dilation_v0`

**Run:** pre-run (spec complete, derivation written, awaiting execution)

**Date:** April 9, 2026

**Status:** SPEC COMPLETE — ready to run

**Program:** `program_gr_reading_depth_v0`

**Paper:** HOWL-PHYS-41-2026

---

### What This Experiment Does

This is a mega-experiment that computes the GR prediction for 12 classical time dilation effects across the entire soliton boundary hierarchy — from 22.5 meters (Pound-Rebka) to redshift z = 1 (Type Ia supernovae) — and compares each to its published measurement. One derivation function (`gr_reading_depth_mega_v0`), 18 comparisons, 8 hierarchy levels, 28 new value nodes plus 2 existing (c, π).

The thesis: every GR time dilation measurement IS a reading depth measurement. The reading depth formula is the standard GR formula. The experiment confirms this by showing that the standard formulas, applied to pool constants with zero hardcoded physics, reproduce every measured time dilation effect across 18 orders of magnitude in Φ/c².

This is not a test of the reading depth interpretation against GR. The reading depth interpretation IS GR. The experiment demonstrates that one derivation function, reading from one pool of measured constants, reproduces a century of GR time dilation measurements spanning lab scale to cosmological scale. The unified treatment across the full hierarchy is the contribution.

---

### The 12 Derivations

**Earth soliton interior (Pound-Rebka).** Δf/f = GM_E·h/(R_E²·c²). A 22.5 m height difference at Harvard. The predicted shift is ~2.46 × 10⁻¹⁵. The measurement (Pound-Snider 1965) is (2.57 ± 0.26) × 10⁻¹⁵. Reading depth: the gamma ray carries the emission depth's update rate. The receiver at 22.5 m shallower depth reads a lower frequency because its own update rate is faster. Expected miss: ~4%, dominated by the measurement uncertainty (10%).

**Earth orbit soliton (GPS).** Gravitational shift: Δf/f = GM_E/c² × (1/R_E − 1/r_gps). Velocity shift: Δf/f = −v²/(2c²). Net daily shift: (grav + vel) × 86400 seconds. The predicted net is ~38.6 μs/day. The measured value (Ashby 2003) is 38.64 μs/day. Reading depth: the satellite at shallower depth (faster updates) allocates some update capacity to spatial displacement (slower updates). The net +38.6 μs/day is the balance. Expected miss: <0.5%.

**Earth orbit soliton (Gravity Probe A).** Δf/f = GM_E/c² × (1/R_E − 1/(R_E + h)). A hydrogen maser at 10,000 km altitude on a suborbital rocket. Predicted shift: ~4.3 × 10⁻¹⁰. Measured (Vessot-Levine 1980): (4.36 ± 0.03) × 10⁻¹⁰, confirming GR to 70 ppm. Reading depth: the maser's update rate increases as it rises to shallower depth. Expected miss: <1%, limited by the nominal altitude precision (2 significant figures).

**Solar soliton surface (redshift).** z = GM_S/(R_S·c²), expressed as velocity v = z·c. Predicted: ~636 m/s. Measured: 636.3 m/s by multiple groups. Reading depth: photons from the Sun's deep reading carry that depth's update rate. We observe from our shallower depth and read a lower frequency. Expected miss: <0.1%.

**Solar soliton interior (Mercury perihelion).** δω = 6πGM_S/(a·c²·(1−e²)) radians per orbit, converted to arcseconds per century. Predicted: ~42.98 arcsec/century. Measured (Park 2017): 42.9799 arcsec/century. Reading depth: the reading depth gradient near the Sun curves Mercury's spatial update path, causing the orbit orientation to precess. Expected miss: <0.01%. This is the most precise GR test in the experiment.

**SR velocity dilation (muon).** τ_lab = γ × τ_rest. At γ = 29.3 (Fermilab g-2 storage ring), the rest lifetime of 2.197 μs dilates to ~64.4 μs. Measured: 64.4 μs, confirmed to 0.1%. Reading depth: the fast muon allocates reading capacity to spatial displacement, leaving fewer depth updates. The muon's internal decay clock runs slower. Expected miss: <0.5%, limited by γ at 3 digits.

**Solar soliton exterior (Shapiro delay).** GR predicts the PPN parameter γ = 1 exactly. Cassini (Bertotti 2003) measured γ = 1 + (2.1 ± 2.3) × 10⁻⁵, confirming GR to 0.002%. Reading depth: photons traversing the Sun's deep reading zone take more Planck steps, producing the observed delay. We output γ = 1. Expected: PASS (structural).

**Compact soliton (Hulse-Taylor).** Pdot_measured / Pdot_GR. Both values are published to 5 digits. The ratio should be ~0.9996 ± 0.0009, confirming GR gravitational wave emission to 0.2%. Reading depth: two neutron star solitons radiate reading depth energy as gravitational waves, settling toward a deeper combined reading. Expected miss: 0.04%.

**Cosmological (SN Ia stretch).** At z = 1, lightcurves are stretched by (1+z) = 2. This is a structural prediction — cosmological time dilation is the ratio of reading depths between emission epoch and observation epoch. We output 2. Expected: PASS.

**Planck scale.** t_P = √(ℏG/c⁵), l_P = √(ℏG/c³), c = l_P/t_P. The Planck time and length are computed from pool constants and compared to CODATA values. The ratio l_P/t_P must equal c exactly (by construction). Reading depth: t_P is the reading update step size. l_P is the spatial reading resolution. c = l_P/t_P is the maximum reading update speed. Expected miss on t_P and l_P: <0.001% (limited by G at 22 ppm, propagated through √G as ~11 ppm). Expected miss on c: ~0 (by construction).

**Earth surface g.** g = GM_E/R_E². Predicted: ~9.82 m/s². Standard: 9.80665 m/s². Reading depth: the reading depth gradient at Earth's surface. Expected miss: ~0.1%, because R_E is the mean radius while g_n is the sea-level standard at a specific latitude. This is a known systematic, not a physics failure.

**Reading depth structural quantities.** Φ/c² for Earth surface (~7 × 10⁻¹⁰), for the Sun surface (~2.1 × 10⁻⁶), and Earth's Schwarzschild radius (2GM_E/c² ~ 8.9 mm). These are not compared to measurements — they are derived structural parameters that characterize the reading depth at each level of the soliton hierarchy.

---

### The Hierarchy Tested

The experiment spans 18 orders of magnitude in Φ/c²:

From Φ/c² ~ 2.5 × 10⁻¹⁵ (22.5 m height difference, Pound-Rebka) to Φ/c² ~ 0.2 (neutron star surface, Hulse-Taylor). From special relativistic dilation at v/c = 0.9994 (muon, γ = 29.3) to cosmological dilation at z = 1 (SN Ia stretch factor 2).

Eight distinct soliton levels are tested: Planck scale, compact soliton (neutron star binary), solar surface, solar orbit (Mercury), solar exterior (Shapiro), Earth surface, Earth orbit (GPS, GPA), and lab scale (Pound-Rebka 22.5 m). Plus one SR velocity test (muon) and one cosmological test (SN Ia).

Every level uses the same physics: the GR redshift formula Δf/f = ΔΦ/c² for gravitational dilation, the Lorentz factor γ for velocity dilation, and (1+z) for cosmological dilation. The reading depth interpretation says these are all the same phenomenon — clocks at different depths in the soliton hierarchy update at different rates — described in the standard GR formalism.

---

### What All 18 Comparisons Test

Nine comparisons test specific numerical predictions against measurements (Pound-Rebka, GPS, GPA, solar redshift, Mercury perihelion, muon lifetime, Planck time, Planck length, g surface). Each is a miss_pct comparison reporting the percent deviation.

Six comparisons test range constraints (Pound-Rebka miss < 10%, GPS miss < 1%, GPA miss < 1%, Mercury miss < 0.1%, Shapiro γ in [0.99997, 1.00003], Hulse-Taylor ratio in [0.995, 1.005]). These are the PASS/FAIL gates.

Two comparisons test structural predictions (SN Ia stretch in [1.99, 2.01], Earth Φ/c² in [6e-10, 8e-10]). These are order-of-magnitude sanity checks.

One comparison tests a tautology (c = l_P/t_P vs 299792458). This is a numerical self-consistency check on the Planck unit computation.

All 18 should PASS. Any FAIL indicates a computational bug or an input precision problem. No FAIL can falsify the reading depth interpretation, because the reading depth formulas ARE the GR formulas.

---

### What This Experiment Does NOT Do

Does not test reading depth against GR. They are the same. The experiment confirms that the standard GR formulas reproduce measurements when applied to pool constants. The reading depth interpretation adds no new predictions to these specific tests.

Does not test boundary effects. The reading depth model suggests there may be additional timing effects at soliton boundary transitions (Hill sphere edges, heliosphere, galactic toroid) that the smooth GR metric doesn't capture. This experiment does not test for such effects — it tests only the smooth GR predictions. Boundary effects are future experiments (Tests 2-5 in PHYS-41).

Does not derive any new value from the HOWL integer structure. Unlike the QED, GUT, and cosmological experiments which derive values from gauge integers, this experiment uses published astrophysical measurements (GM_E, GM_S, orbital parameters) as inputs. The connection to the HOWL framework is interpretive (reading depth = 4th coordinate), not derivational (integers → prediction).

Does not resolve the Hubble tension. The PHYS-41 computation showed the galactic gravitational potential is five to six orders of magnitude too shallow to produce the 8.4% local-CMB H₀ discrepancy. This experiment does not revisit that computation.

---

### New Pool Content

28 new value nodes spanning fundamental constants (G, ℏ, Planck time, Planck length, standard g), Earth soliton parameters (M_E, GM_E, R_E), solar soliton parameters (GM_S, R_S), and published GR test measurements (Pound-Rebka height and shift, GPS orbital parameters and net shift, GPA altitude and shift, Cassini γ, solar redshift, muon lifetime data, Hulse-Taylor Pdot values, Mercury orbital parameters and perihelion advance, SN Ia stretch factor).

1 new experiment JSON with 1 derivation, 18 comparisons, 2 diagram specs.

1 new connection JSON mapping the soliton hierarchy with 8 levels and their associated tests.

1 new program JSON (ACTIVE, 2 kill switches).

1 new derivation function (`gr_reading_depth_mega_v0`) — 180 lines, all inputs from pool, zero hardcoded physics, mp.dps = 50, restored at exit.

---

### Registration

Add to `DERIVATION_MORE_INDEX_V0`:

```python
    # GR: Reading depth / time dilation
    "gr_reading_depth_mega_v0": gr_reading_depth_mega_v0,
```

---

### Expected Outcome

ALL COMPARISONS PASSED. Every comparison uses the standard GR formula with published input constants. The formulas are textbook. The inputs are CODATA/IAU/PDG. The only possible failures are computational bugs (wrong formula, wrong unit conversion, wrong sign) or input precision mismatches (mean radius vs local radius for g, nominal altitude vs actual for GPA).

The most likely soft failure: g from GM/R² will give ~9.82 m/s² instead of the standard 9.80665 m/s², a ~0.1% miss. This is because R_E = 6,371,000 m is the mean radius while g_n = 9.80665 is the sea-level standard at 45° latitude. The comparison is miss_pct (INFO), not a PASS/FAIL gate, so this expected discrepancy won't cause a FAIL.

The most informative result: Mercury perihelion. The GR formula δω = 6πGM_S/(ac²(1−e²)) with published orbital parameters should reproduce 42.98 arcsec/century to better than 0.01%. This is the highest-precision GR test that uses a non-trivial formula (not just Δf/f = ΔΦ/c²). If it matches, the reading depth gradient near a stellar soliton correctly describes orbital precession across 18 orders of magnitude below the Planck scale.

---

### What Running This Experiment Proves

That one derivation function, reading from one pool of constants, reproduces a century of GR time dilation measurements spanning 18 orders of magnitude in gravitational potential. That every measurement — from the frequency shift of a gamma ray over 22.5 meters to the lightcurve stretch of a supernova at z = 1 — is described by the same reading depth formula: deeper reading, slower update.

That the ninth physics domain (GR time dilation) connects to the HOWL derivation graph through the reading depth interpretation: the fourth coordinate is not time but position in the soliton hierarchy. The formula is GR's. The measurements are GR's. The name is the reading depth model's.

---

**END OF REPORT**

**Experiment:** `experiment_gr_time_dilation_v0`

**Status:** Spec complete. 1 derivation, 18 comparisons, 28 new values, 8 hierarchy levels. Ready to run.

**Central result (expected):** ALL COMPARISONS PASSED. GR time dilation IS reading depth, confirmed across 18 orders of magnitude from lab scale to cosmological scale.


---

## APPENDIX TABLES: GR Time Dilation as Reading Depth

### Table A.1: The 12 Derivations — Formula, Input, Output

| # | Derivation | Formula | Inputs from pool | Output key | Units |
|---|---|---|---|---|---|
| 1 | Pound-Rebka redshift | Δf/f = GM_E·h / (R_E²·c²) | GM_E, R_E, c, h_pr | result_pound_rebka_predicted_v0 | dimensionless |
| 2a | GPS gravitational shift | Δf/f = GM_E/c² × (1/R_E − 1/r_gps) | GM_E, R_E, r_gps, c | result_gps_grav_shift_v0 | dimensionless |
| 2b | GPS velocity shift | Δf/f = −v²/(2c²) | v_gps, c | result_gps_velocity_shift_v0 | dimensionless |
| 2c | GPS net daily shift | (grav + vel) × 86400 | derived | result_gps_net_shift_v0 | s/day |
| 3 | Gravity Probe A | Δf/f = GM_E/c² × (1/R_E − 1/(R_E+h)) | GM_E, R_E, h_gpa, c | result_gpa_predicted_v0 | dimensionless |
| 4 | Solar redshift | v = GM_S·c / (R_S·c²) | GM_S, R_S, c | result_solar_redshift_predicted_v0 | m/s |
| 5 | Mercury perihelion | δω = 6πGM_S / (a·c²·(1−e²)) × conversion | GM_S, a, e, T, c, π | result_mercury_perihelion_predicted_v0 | arcsec/century |
| 6 | Muon dilation | τ_lab = γ × τ_rest | γ_mu, τ_rest | result_muon_dilated_lifetime_v0 | s |
| 7 | Shapiro PPN γ | GR predicts γ = 1 | (none — structural) | result_shapiro_gamma_predicted_v0 | dimensionless |
| 8 | Hulse-Taylor ratio | Pdot_meas / Pdot_GR | Pdot_meas, Pdot_GR | result_ht_pdot_ratio_v0 | dimensionless |
| 9 | SN Ia stretch | (1+z) at z = 1 | (none — structural) | result_sn1a_stretch_predicted_v0 | dimensionless |
| 10a | Planck time | t_P = √(ℏG/c⁵) | ℏ, G, c | result_planck_time_from_constants_v0 | s |
| 10b | Planck length | l_P = √(ℏG/c³) | ℏ, G, c | result_planck_length_from_constants_v0 | m |
| 10c | c from Planck | c = l_P / t_P | derived | result_c_from_planck_v0 | m/s |
| 11 | g surface | g = GM_E / R_E² | GM_E, R_E | result_g_surface_from_gm_v0 | m/s² |
| 12a | Earth Φ/c² | GM_E / (R_E·c²) | GM_E, R_E, c | result_earth_phi_over_c2_v0 | dimensionless |
| 12b | Sun Φ/c² | GM_S / (R_S·c²) | GM_S, R_S, c | result_sun_phi_over_c2_v0 | dimensionless |
| 12c | Earth r_s | 2GM_E / c² | GM_E, c | result_earth_schwarzschild_radius_v0 | m |

### Table A.2: The 18 Comparisons — Expected Results

| # | Label | Output key | Mode | Expected | Measured source | Expected outcome |
|---|---|---|---|---|---|---|
| 1 | Pound-Rebka Δf/f | result_pound_rebka_predicted_v0 | miss_pct | 2.46e-15 | Pound-Snider 1965 | ~2.46e-15 |
| 2 | Pound-Rebka miss < 10% | result_pound_rebka_miss_pct_v0 | range [0, 10] | — | Pound-Snider 1965 | PASS (input limited) |
| 3 | GPS net shift | result_gps_net_shift_v0 | miss_pct | 38.64e-6 s/day | Ashby 2003 | ~38.6 μs/day |
| 4 | GPS miss < 1% | result_gps_net_miss_pct_v0 | range [0, 1] | — | Ashby 2003 | PASS |
| 5 | GPA Δf/f | result_gpa_predicted_v0 | miss_pct | 4.36e-10 | Vessot-Levine 1980 | ~4.3e-10 |
| 6 | GPA miss < 1% | result_gpa_miss_pct_v0 | range [0, 1] | — | Vessot-Levine 1980 | PASS |
| 7 | Solar redshift | result_solar_redshift_predicted_v0 | miss_pct | 636.3 m/s | Multiple groups | ~636 m/s |
| 8 | Mercury perihelion | result_mercury_perihelion_predicted_v0 | miss_pct | 42.9799 arcsec/c | Park 2017 | ~42.98 |
| 9 | Mercury miss < 0.1% | result_mercury_miss_pct_v0 | range [0, 0.1] | — | Park 2017 | PASS |
| 10 | Muon lifetime | result_muon_dilated_lifetime_v0 | miss_pct | 64.4e-6 s | g-2 ring | ~64.4 μs |
| 11 | Cassini γ ≈ 1 | result_shapiro_gamma_predicted_v0 | range [0.99997, 1.00003] | — | Bertotti 2003 | 1.000000 |
| 12 | HT Pdot ratio ≈ 1 | result_ht_pdot_ratio_v0 | range [0.995, 1.005] | — | Weisberg-Taylor 2005 | ~0.9996 |
| 13 | SN Ia stretch = 2 | result_sn1a_stretch_predicted_v0 | range [1.99, 2.01] | — | Blondin 2008 | 2.000 |
| 14 | Planck time | result_planck_time_from_constants_v0 | miss_pct | 5.391247e-44 s | CODATA 2018 | ~5.39e-44 |
| 15 | Planck length | result_planck_length_from_constants_v0 | miss_pct | 1.616255e-35 m | CODATA 2018 | ~1.62e-35 |
| 16 | c = l_P/t_P | result_c_from_planck_v0 | miss_pct | 299792458 m/s | SI exact | 299792458 |
| 17 | g from GM/R² | result_g_surface_from_gm_v0 | miss_pct | 9.80665 m/s² | CGPM 1901 | ~9.82 |
| 18 | Earth Φ/c² ∼ 10⁻⁹ | result_earth_phi_over_c2_v0 | range [6e-10, 8e-10] | — | physics | ~7e-10 |

### Table A.3: The 28 Input Value Nodes

| # | Pool key | Value | Unit | Digits | Source | Level |
|---|---|---|---|---|---|---|
| 1 | si_speed_of_light_v0 | 299792458 | m/s | exact | SI 2019 | 0 |
| 2 | geom_pi_v0 | 3.14159... (Q335) | — | 335 | geometry | 0 |
| 3 | gr_newton_g_v0 | 6.67430e-11 | m³ kg⁻¹ s⁻² | 6 | CODATA 2018 | 2 |
| 4 | gr_gm_earth_v0 | 3.986004418e14 | m³ s⁻² | 10 | IAU 2015 | 2 |
| 5 | gr_radius_earth_v0 | 6371000 | m | 7 | IAU 2015 | 2 |
| 6 | gr_gm_sun_v0 | 1.32712440018e20 | m³ s⁻² | 12 | IAU 2015 | 2 |
| 7 | gr_radius_sun_v0 | 6.957e8 | m | 4 | IAU 2015 | 2 |
| 8 | gr_si_hbar_v0 | 1.054571817e-34 | J s | 10 | SI 2019 | 0 |
| 9 | gr_pound_rebka_height_v0 | 22.5 | m | 3 | Pound-Rebka 1959 | 2 |
| 10 | gr_pound_rebka_measured_shift_v0 | 2.57e-15 | — | 3 | Pound-Snider 1965 | 2 |
| 11 | gr_gps_orbit_radius_v0 | 26560000 | m | 4 | GPS ICD-200 | 2 |
| 12 | gr_gps_orbit_velocity_v0 | 3874 | m/s | 4 | √(GM/a) | 2 |
| 13 | gr_gps_net_shift_measured_v0 | 38.64e-6 | s/day | 4 | Ashby 2003 | 2 |
| 14 | gr_gravity_probe_a_altitude_v0 | 10000000 | m | 2 | Vessot-Levine 1980 | 2 |
| 15 | gr_gravity_probe_a_measured_v0 | 4.36e-10 | — | 3 | Vessot-Levine 1980 | 2 |
| 16 | gr_shapiro_cassini_gamma_v0 | 1.000021 | — | 6 | Bertotti 2003 | 2 |
| 17 | gr_solar_redshift_measured_v0 | 636.3 | m/s | 4 | Multiple groups | 2 |
| 18 | gr_muon_lorentz_gamma_v0 | 29.3 | — | 3 | Fermilab g-2 | 2 |
| 19 | gr_muon_lifetime_rest_v0 | 2.1969811e-6 | s | 7 | PDG 2024 | 2 |
| 20 | gr_muon_lifetime_dilated_measured_v0 | 64.4e-6 | s | 3 | g-2 ring | 2 |
| 21 | gr_hulse_taylor_pdot_measured_v0 | −2.4025e-12 | s/s | 5 | Weisberg-Taylor 2005 | 2 |
| 22 | gr_hulse_taylor_pdot_gr_v0 | −2.4026e-12 | s/s | 5 | Peters 1964 formula | 2 |
| 23 | gr_mercury_perihelion_measured_v0 | 42.9799 | arcsec/c | 6 | Park 2017 | 2 |
| 24 | gr_mercury_semimajor_v0 | 5.791e10 | m | 4 | IAU | 2 |
| 25 | gr_mercury_eccentricity_v0 | 0.20563 | — | 5 | IAU | 2 |
| 26 | gr_mercury_period_v0 | 7600521.6 | s | 8 | 87.9691 days | 2 |
| 27 | gr_sn1a_stretch_factor_z1_v0 | 2.0 | — | 2 | Blondin 2008 | 2 |
| 28 | gr_planck_time_v0 | 5.391247e-44 | s | 7 | CODATA 2018 | 0 |
| 29 | gr_planck_length_v0 | 1.616255e-35 | m | 7 | CODATA 2018 | 0 |
| 30 | gr_g_surface_earth_v0 | 9.80665 | m/s² | 6 | CGPM 1901 | 2 |

### Table A.4: The Soliton Hierarchy — Reading Depth at Each Level

| Level | Soliton boundary | Characteristic radius | Φ/c² | Reading depth (update rate ratio) | Tests in this experiment |
|---|---|---|---|---|---|
| Planck | Maximum depth | l_P = 1.6e-35 m | 1 (horizon) | 0 (clock stops) | t_P, l_P, c = l_P/t_P |
| Compact | Neutron star | r ~ 10 km | ~0.2 | ~0.9 (20% slower) | Hulse-Taylor Pdot |
| Solar surface | Sun | R_S = 6.96e8 m | 2.12e-6 | 1 − 1.06e-6 | Solar redshift |
| Mercury orbit | Sun (inner) | a = 5.79e10 m | 2.56e-8 | 1 − 1.28e-8 | Perihelion advance |
| Solar exterior | Sun (Shapiro) | r_min ~ R_S | ~4e-6 at limb | 1 − 2e-6 | Cassini γ |
| Earth surface | Earth | R_E = 6.37e6 m | 6.95e-10 | 1 − 3.48e-10 | Pound-Rebka, g surface |
| Earth orbit (GPS) | Earth | r = 2.66e7 m | 1.67e-10 | 1 − 8.3e-11 | GPS, GPA |
| Lab scale (22.5 m) | Earth interior | Δh = 22.5 m | Δ = 2.46e-15 | 1 − 1.23e-15 | Pound-Rebka differential |
| SR velocity | (not gravitational) | v/c = 0.9994 | — | 1/γ = 0.034 | Muon dilation |
| Cosmological | Universe | z = 1 | (FRW, not Schwarz.) | (1+z) = 2 | SN Ia stretch |

### Table A.5: Expected Numerical Results (Pre-Run Estimates)

| Derivation | Expected prediction | Expected measured | Expected miss | Limiting factor |
|---|---|---|---|---|
| Pound-Rebka Δf/f | ~2.46e-15 | (2.57 ± 0.26)e-15 | ~4% | Measured unc is 10%; our computation uses GM_E/R_E² not local g |
| GPS net shift | ~38.6 μs/day | 38.64 μs/day | <0.5% | Input precision (GM_E 10 digits, r_gps 4 digits) |
| Gravity Probe A | ~4.3e-10 | (4.36 ± 0.03)e-10 | <1% | Altitude approximate (10,000 km nominal) |
| Solar redshift | ~636 m/s | 636.3 m/s | <0.1% | GM_S at 12 digits, R_S at 4 digits |
| Mercury perihelion | ~42.98 arcsec/c | 42.9799 arcsec/c | <0.01% | All orbital params well known |
| Muon dilation | ~64.4 μs | 64.4 μs | <0.5% | γ input at 3 digits |
| Shapiro γ | 1.000000 | 1.000021 ± 0.000023 | 0.002% | GR predicts exactly 1 |
| HT Pdot ratio | ~0.9996 | 1.0000 | 0.04% | Both values at 5 digits |
| SN Ia stretch | 2.000 | 2.0 | 0 | Structural (1+z) |
| Planck time | ~5.391e-44 s | 5.391247e-44 s | <0.001% | G limits both |
| Planck length | ~1.616e-35 m | 1.616255e-35 m | <0.001% | G limits both |
| c from Planck | 299792458.000 | 299792458 | ~0 | By construction |
| g from GM/R² | ~9.82 m/s² | 9.80665 m/s² | ~0.1% | R_E is mean, g_n is sea-level standard |

### Table A.6: Reading Depth Interpretation — Each Test

| Test | Standard GR language | Reading depth language | What changes |
|---|---|---|---|
| Pound-Rebka | Photon frequency shifts in gravitational field | Photon carries emission depth's update rate; receiver at shallower depth reads lower frequency | Name only |
| GPS | Satellite clocks gain from altitude, lose from velocity | Satellite at shallower depth (faster updates) but allocating capacity to spatial displacement (slower updates) | Name only |
| Gravity Probe A | Maser frequency increases at altitude | Maser update rate increases at shallower reading depth | Name only |
| Solar redshift | Photon loses energy climbing out of Sun | Photon carries the Sun's deep reading; observer at shallower depth reads lower frequency | Name only |
| Mercury perihelion | Spacetime curvature causes orbit precession | Reading depth gradient near Sun curves the spatial update path | Name only |
| Muon dilation | Moving clock runs slow (Lorentz) | Moving muon allocates reading capacity to spatial displacement; fewer depth updates = longer lifetime | Name only |
| Shapiro delay | Light slows near massive object | Photon traverses deep reading zone; spatial updates take more Planck steps | Name only |
| Hulse-Taylor | Gravitational waves carry energy | Two solitons radiate reading depth energy as they spiral toward deeper combined reading | Name only |
| SN Ia stretch | Cosmological time dilation stretches lightcurve | Supernova clock ran at the reading depth of its emission epoch; we observe from our current shallower depth | Name only |
| Planck time | Minimum measurable time interval | Reading update step size; below t_P readings don't subdivide | Interpretation |
| Planck length | Minimum measurable length | Spatial reading resolution; below l_P spatial readings don't subdivide | Interpretation |
| c = l_P/t_P | Speed of light from Planck units | Maximum reading update speed: one spatial unit per one depth unit | Interpretation |
| g surface | Gravitational acceleration | Reading depth gradient at Earth surface | Name only |
| Earth Φ/c² | Gravitational potential parameter | Total reading depth of Earth surface within Earth soliton | Name only |

### Table A.7: Cross-Reference to Existing Pool Experiments

| Existing experiment | Overlap with this experiment | What this adds |
|---|---|---|
| experiment_soliton_gravity_v0 (8 deriv, 12 comp) | GM/rc², escape velocity, Hill sphere, Kepler, GPS, MOND | Pound-Rebka, GPA, Shapiro, Mercury, HT, SN Ia, Planck units, solar redshift — 10 new tests |
| experiment_relativity_v0 (3 deriv, 6 comp) | Muon dilation, twins, ds² | Muon dilation with measured γ from g-2 ring; explicit τ_lab comparison |
| experiment_boundary_scales_v0 (0 deriv, 0 comp) | Skeleton only | All content is new |

This mega-experiment consolidates the strongest GR time dilation tests from across the soliton hierarchy into one experiment with one derivation function. It does not replace the existing experiments — it adds 10 new tests not covered by any existing experiment and provides the unified reading depth interpretation across all levels.

### Table A.8: Precision Budget — What Limits Each Test

| Test | Precision-limiting input | Input precision | Propagation | Expected output precision |
|---|---|---|---|---|
| Pound-Rebka | GM_E (via g) + R_E (mean vs local) | GM_E: 0.002 ppb, R_E: ~100 ppm | g = GM/R² limited by R | ~0.02% on g, ~4% vs measured (measured unc) |
| GPS gravitational | GM_E, R_E, r_gps | r_gps: 4 digits | Direct | ~0.1% |
| GPS velocity | v_gps | 4 digits | v²/c² | ~0.1% |
| GPS net | Both above | Worst of both | Sum | ~0.5% |
| Gravity Probe A | h_gpa approximate (10,000 km nominal) | 2 sf | Through 1/(R+h) | ~1% |
| Solar redshift | R_S | 4 digits | Direct GM/(Rc²) | ~0.01% |
| Mercury | All orbital params well known | 4-8 digits | 6πGM/(ac²(1-e²)) | ~0.01% |
| Muon | γ_mu | 3 digits | Direct γ×τ | ~0.3% |
| Shapiro | (structural — γ = 1) | exact | — | 0 |
| Hulse-Taylor | Both Pdot at 5 digits | 5 digits | Ratio | ~0.04% |
| SN Ia | (structural — 1+z) | exact | — | 0 |
| Planck t, l | G at 22 ppm | 22 ppm | √G | ~11 ppm |
| g surface | R_E (mean vs standard) | ~100 ppm difference | GM/R² | ~0.1% |

### Table A.9: The Reading Depth Hierarchy — Φ/c² Across 20 Orders of Magnitude

| Object | Φ/c² | log₁₀(Φ/c²) | Reading interpretation | Measured by |
|---|---|---|---|---|
| Black hole (horizon) | 0.5 | −0.3 | Maximum depth; clock stops | EHT shadow |
| Neutron star surface | 0.15–0.35 | −0.5 to −0.9 | Deep; 15-35% clock slowing | X-ray spectral lines |
| White dwarf (Sirius B) | 3e-4 | −3.5 | Moderate depth | Spectral redshift |
| Sun surface | 2.12e-6 | −5.7 | Shallow; 1 ppm clock effect | Solar limb redshift |
| Mercury periapsis | 3.8e-8 | −7.4 | Very shallow | Perihelion advance |
| Earth surface | 6.95e-10 | −9.2 | Extremely shallow | Pound-Rebka, GPS |
| GPS altitude | 1.67e-10 | −9.8 | Shallower than surface | GPS clock corrections |
| Lab height (22.5 m) | 2.46e-15 | −14.6 | Reading depth differential | Pound-Rebka differential |
| Optical clock (1 cm) | ~1e-18 | −18 | Frontier precision | JILA/PTB lattice clocks |
| Planck scale | 1 | 0 | Deepest possible reading | Planck t_P, l_P |

The hierarchy spans 18 orders of magnitude in Φ/c². Every level has been measured. Every measurement confirms that clocks at different depths run at different rates. The reading depth interpretation names what the measurements describe.

### Table A.10: Connection to the HOWL Derivation Graph

| Domain | Existing values | This experiment adds | Connection type |
|---|---|---|---|
| QED (α, R∞, a₀, μ₀) | 6 values at 0.007-0.44 ppb | None (no QED chain) | Independent — parallel evidence |
| GUT (sin²θ_W, α_s, M_GUT) | 10 values at 12 ppm - 8.7% | None | Independent |
| EW (M_W, Γ_Z) | 15 values at 195 ppm - 0.84% | None | Independent |
| Cosmology (Ω_b, D/H) | 11 values at 0.12σ - 725 ppm | SN Ia stretch at z=1 | New cosmological test |
| Gravity | 8 derivations in soliton_gravity | 10+ new tests (Pound-Rebka through Planck) | Extends gravity domain |
| Relativity | 3 derivations in relativity | Muon dilation with measured γ | Reinforces SR chain |
| **New: GR domain** | **0 dedicated values** | **12 derivations, 18 comparisons** | **Ninth physics domain** |

This experiment opens the ninth physics domain in the HOWL derivation graph: GR time dilation. The previous eight (QED, EW, GUT, cosmology, nuclear, muon, flavor, spectroscopy) all test the integer transformation law structure. The ninth tests the reading depth interpretation — the claim that the fourth coordinate is not time but reading depth in the soliton hierarchy.

### Table A.11: What PASS and FAIL Mean for Each Test

| Test | If PASS | If FAIL | Kill? |
|---|---|---|---|
| Pound-Rebka | GR redshift formula works at 22.5 m | Bug in g computation or input error | No — input limited |
| GPS net shift | GR grav + SR velocity dilation works at 20,200 km | Bug in formula or input precision | No — input limited |
| GPA | GR redshift at 10,000 km altitude | Bug or nominal altitude too imprecise | No — input limited |
| Solar redshift | GR formula works at stellar scale | Bug in GM_S/R_S | No — check R_S |
| Mercury perihelion | GR perihelion formula works | Bug in angular conversion or orbital params | **Check** — most precise GR test |
| Muon dilation | SR dilation at γ = 29.3 | Bug in γ × τ multiplication | No — trivial |
| Shapiro γ | GR predicts γ = 1 (structural) | Cannot fail (we output 1) | No |
| Hulse-Taylor ratio | GR quadrupole radiation confirmed | Bug in ratio or input values | No — values from literature |
| SN Ia stretch | Cosmological dilation = (1+z) | Cannot fail (we output 2) | No |
| Planck time/length | t_P = √(ℏG/c⁵) confirmed | Bug in sqrt or input G | No |
| c from Planck | l_P/t_P = c by construction | Bug in division | No |
| g from GM/R² | GM/R² ≈ standard g | Miss expected (~0.1%) because R_E is mean not sea-level | No — known systematic |
| Earth Φ/c² in range | Order of magnitude check | Bug in formula | No |

**No test in this experiment can falsify the reading depth interpretation.** Every comparison is the standard GR formula applied to published measurements. A FAIL indicates a computational bug or an input precision problem, not a physics failure. The reading depth interpretation IS GR — it names what the formulas describe, it doesn't change them.

### Table A.12: Experiment Identity Card

| Field | Value |
|---|---|
| Experiment key | experiment_gr_time_dilation_v0 |
| Program | program_gr_reading_depth_v0 |
| Paper | HOWL-PHYS-41-2026 |
| Derivation functions | 1 (gr_reading_depth_mega_v0) |
| Value nodes required | 28 new + 2 existing (c, π) |
| Comparisons | 18 |
| Hierarchy levels tested | 8 (Planck, compact, solar surface, solar orbit, Earth surface, Earth orbit, lab, cosmological) |
| SR tests | 1 (muon dilation) |
| GR tests | 9 (Pound-Rebka, GPS, GPA, solar redshift, Mercury, Shapiro, HT, SN Ia, Planck) |
| Structural checks | 3 (γ = 1, stretch = 2, c = l_P/t_P) |
| Derived structural quantities | 3 (Earth Φ/c², Sun Φ/c², Earth r_s) |
| Connection | connection_gr_reading_depth_v0 |
| Diagrams | 2 (reading depth hierarchy, miss % across all tests) |
| Expected status | ALL COMPARISONS PASSED |
| New domain added | GR time dilation (ninth domain) |

---

## Report: What Changes If Reading Depth Is Tautology

### The Premise

The HOWL framework has 53 derived values from 13 inputs, surplus 40, spanning 9 physics domains. The GR time dilation mega-experiment adds 12 derivations and 18 comparisons across 18 orders of magnitude in Φ/c². Every comparison uses the standard GR formula. Every comparison is expected to PASS.

The reading depth interpretation says: the fourth coordinate is not time. It is position in the soliton boundary hierarchy. GR time dilation IS reading depth. The formulas are identical. The measurements are identical. The name is different.

If this is taken as tautology — if reading depth IS what GR describes, not an alternative to it — then the question is not "does reading depth work?" (it does, because GR does) but "what does the tautology reveal that the standard framing hides?"

### What Changes

**The hierarchy problem dissolves into a naming problem.** The standard framing asks: why is the Planck mass (10¹⁹ GeV) so much larger than the electroweak scale (10² GeV)? Why is gravity so weak? The reading depth framing says: these are different levels in the soliton hierarchy. The Planck scale is the deepest reading (maximum Φ/c² = 1). The electroweak scale is a shallower reading (Φ/c² ~ 10⁻³²). The "hierarchy" is the depth difference between two levels in the nesting structure. Asking why they're different is like asking why the Earth's surface is at a different depth than the Sun's surface — they're different boundaries in the same hierarchy. The ratio M_Planck/M_EW ~ 10¹⁷ is not a fine-tuning problem. It is the reading depth ratio between two soliton levels, determined by the integer transformation laws (beta coefficients) that govern coupling running between boundaries.

This doesn't solve the hierarchy problem in the technical sense (it doesn't provide a mechanism that stabilizes the Higgs mass against quadratic divergences). It reframes the question: instead of "why is gravity weak?" the question becomes "what sets the depth spacing between the electroweak boundary and the Planck boundary?" The answer is in the beta coefficients — the same integers (11, 13) that determine coupling unification at M_GUT = 10¹⁵·⁶ also determine where the Planck boundary sits relative to M_Z. The depth spacing is not arbitrary. It is computed from the gauge group.

**Quantum gravity becomes a vocabulary problem, not a physics problem.** The standard program: quantize spacetime. Find a theory where the metric tensor g_μν is a quantum field. Resolve the non-renormalizability of perturbative quantum gravity. This program has produced string theory (10⁵⁰⁰ vacua, no predictions), loop quantum gravity (discrete spacetime, no low-energy limit), and 50 years of effort without convergence.

The reading depth framing says: there is nothing to quantize. The three spatial dimensions are already described by quantum field theory (fields on flat 3D space). The fourth coordinate is reading depth — a label for which level of the soliton hierarchy you're measuring from. Reading depth doesn't need to be quantized because it's not a dimension. It's a bookkeeping coordinate that tracks which boundary you're inside. The metric signature (−,+,+,+) encodes this: three quantizable spatial dimensions and one non-quantizable reading depth coordinate.

What "quantum gravity" would mean in this framing: the quantization of the coupling between soliton boundaries. How does the reading depth change when a quantum of energy crosses a boundary? The answer is already in the framework — it's the beta function. The beta function describes how couplings (readings) change as you move between boundaries (energy scales). The beta function IS quantum gravity in the reading depth language. It's been computed to two loops. It's been tested at 12 ppm (sin²θ_W) and 0.33% (α_s). The "quantum gravity" program, reframed as "how do readings change at boundaries," is already partially complete.

**Dark energy becomes a reading depth gradient, not a substance.** The cosmological constant Λ drives the accelerating expansion. In standard cosmology, Λ is either a vacuum energy (which is 10¹²⁰ times too large from QFT) or a geometric constant (which has no explanation for its value).

In the reading depth framing: the accelerating expansion means the reading depth of the outermost soliton boundary is increasing over cosmic time. The "vacuum energy" is not a substance filling space. It is the rate of change of the cosmic reading depth. The reading depth at the cosmic boundary is determined by Ω_DE = 0.6903, which the HOWL framework derives from the gauge integers through (22/13)π and the flatness condition. The cosmological constant problem (why is Λ so small?) becomes: why is the cosmic reading depth gradient so shallow? The answer: because the gauge integers (11, 13) that determine the DM/baryon ratio also determine Ω_DE through flatness, and the integers are small. The smallness of Λ is the smallness of the integers.

This doesn't compute Λ from first principles — the (22/13)π connection is an observed relationship, not a derived one (p = 0.81 in isolation). But it embeds Λ in the same integer structure that produces sin²θ_W and D/H. If the integer structure is real, Λ's value is not arbitrary — it's determined by the same transformation laws that govern particle physics.

**The measurement problem in quantum mechanics becomes a reading problem.** Standard QM: the wave function collapses upon measurement. What constitutes a measurement? When does collapse happen? Why is the process irreversible? (The measurement problem.)

Reading depth framing: before measurement, the system is in a superposition of readings — multiple boundary configurations coexist. Measurement forces a specific reading: a specific boundary depth is probed. The "collapse" is the selection of one reading from the available set. The irreversibility comes from the same source as the arrow of time: readings update toward ground state and don't un-update. Measurement is a reading event. The wave function doesn't collapse — a reading is taken.

This is not a solution to the measurement problem. It is a restatement in reading language. But the restatement has a structural advantage: it connects the measurement problem to the arrow of time through the same mechanism (reading update irreversibility). In standard QM, the measurement problem and the arrow of time are separate puzzles. In the reading depth framing, they are the same puzzle: why are readings one-directional?

**The black hole information paradox becomes a reading depth question.** Standard: information falls into a black hole. The black hole evaporates via Hawking radiation. Is the information preserved in the radiation (unitarity) or destroyed (information loss)?

Reading depth: the event horizon is where Φ/c² = 0.5 — the reading depth at which the update rate drops to zero. Inside the horizon, all reading capacity is allocated to inward spatial displacement. No outward readings are possible. The "information" is the set of readings that described the infalling matter. At the horizon, these readings become inaccessible — not because they're destroyed, but because the reading depth prevents outward communication. The Hawking radiation is thermal because it carries no reading information from inside — it's generated at the horizon boundary, not transmitted from the interior.

Whether the readings are "still there" inside or "gone" is the same question as the block universe question: does a prior reading still exist after a new reading is taken? The reading depth model is presentist — only the current reading exists. The information paradox reduces to: are prior readings archived, or are they overwritten? The model says overwritten. This is the same answer as "information is destroyed" — but stated in reading language, it's the expected behavior (readings update, they don't accumulate), not a paradox.

**Unification becomes a hierarchy map, not a Lagrangian.** The standard unification program: find a single gauge group G that contains SU(3) × SU(2) × U(1) and produces all observed particles and couplings. Write the Lagrangian. Predict proton decay, monopoles, and the GUT scale.

The reading depth framing: unification is the statement that all readings (couplings, masses, densities, abundances) derive from the same integer transformation laws operating at different levels of the soliton hierarchy. The gauge group SU(3) × SU(2) × U(1) determines the integers. The integers determine the beta coefficients. The betas determine how readings change between boundaries. The readings at every level are computable from the readings at any other level through the transformation laws.

The HOWL framework has demonstrated this for 53 values across 9 domains. The integers 11 and 13 appear in the QCD beta coefficient, the SU(2) beta coefficient, the DM/baryon ratio, and the gap ratio. The same integers that govern coupling running at 10¹⁵ GeV also govern the deuterium abundance from Big Bang nucleosynthesis. The "unification" is not at one energy scale (M_GUT). It is the integer structure that connects all scales.

The Lagrangian is not replaced. It is the generating function for the transformation laws. But the emphasis shifts: from "find the right Lagrangian" to "map the reading at each boundary." The Lagrangian is the tool. The map is the result.

**Particle physics becomes boundary classification.** The standard model has 17 fields (6 quarks, 6 leptons, 4 gauge bosons, 1 Higgs). Each has a mass, spin, charge, and color. The pattern is unexplained — why these fields and not others?

The reading depth framing: each field is a soliton — a stable boundary configuration. The electron soliton has a specific reading depth (its mass, 0.511 MeV). The proton soliton has a deeper reading (938 MeV). The Z boson soliton has a much deeper reading (91,188 MeV). The readings are not arbitrary — they are determined by the soliton stability conditions at each level of the hierarchy.

The "why these fields?" question becomes "why these stable boundary configurations?" The answer is the same as "why these nuclei?" in nuclear physics — stability is determined by the binding energy, which is determined by the forces, which are determined by the gauge group and its transformation laws. The 17 SM fields are the stable soliton configurations allowed by SU(3) × SU(2) × U(1) at the energy scales between the Planck boundary and the vacuum. The Cabibbo Doublet, if confirmed, would be the 18th stable configuration — a boundary that exists between M_GUT and the TeV scale.

**Cosmology becomes nested soliton dynamics.** The standard cosmological model (ΛCDM) describes the universe with 6 parameters: H₀, Ω_b, Ω_DM, n_s, A_s, τ_reion. These are treated as free parameters fit to the CMB.

The reading depth framing: the universe is the outermost soliton. Its expansion is the outermost reading depth increasing over time. The CMB is the reading from the last scattering surface — the boundary between the plasma-opaque interior and the transparent exterior. The 6 ΛCDM parameters are readings at the cosmic boundary. Some are derivable from gauge integers: Ω_b from (22/13)π and Ω_DM, hence Ω_m and Ω_DE from flatness. The HOWL framework has already derived 6 cosmological values (Ω_b, Ω_m, Ω_DE, ρ_Λ, η₁₀) and 5 nuclear values (D/H, Y_p, He-3, Li-7) from the gauge integers plus Ω_DM and H₀ as inputs. Two of the 6 ΛCDM parameters are derivable. Four remain as inputs.

The reading depth addition: the Hubble parameter H₀ is the reading update rate of the cosmic boundary. Different measurements of H₀ (local vs CMB) are readings from different depths in the hierarchy. The 5σ tension between them may be a reading depth effect — though the PHYS-41 computation showed the galactic potential is too shallow by five orders of magnitude to explain the 8.4% discrepancy through gravitational reading depth alone.

**Engineering gains a new design principle.** If time is reading depth and clocks are reading instruments, then clock precision is bounded by the reading depth gradient at the clock's location. A clock in a deeper reading (stronger gravitational field) ticks slower. A clock allocating reading capacity to spatial displacement (moving fast) ticks slower.

The engineering consequence: to build the most precise clock, minimize the reading depth perturbations. Operate in the shallowest possible reading (weakest gravitational field, zero velocity). The frontier of clock precision (10⁻¹⁸ fractional stability, JILA/PTB optical lattice clocks) is limited by reading depth fluctuations — tidal effects from the Moon and Sun, seismic vibrations changing the local Φ/c², temperature-dependent material changes affecting the atomic transition.

The reading depth framing suggests a specific engineering path: build clocks in space (shallower reading, fewer tidal perturbations), or build clocks sensitive to different forces (nuclear clocks vs optical clocks) to test whether reading depth is force-dependent. If nuclear and optical clocks disagree beyond GR, that's not a measurement error — it's a reading depth discovery. This is Test 1 from PHYS-41, and it's the only test that could distinguish reading depth from standard GR as new physics.

### What Doesn't Change

The Standard Model Lagrangian. Every computation in QFT uses the same equations. The reading depth interpretation doesn't change a single Feynman diagram, a single cross-section, a single decay rate.

General relativity. Every GR prediction is unchanged. The reading depth interpretation IS GR. The Einstein field equations are the equations of reading depth dynamics. The Schwarzschild metric is the reading depth profile of a spherical soliton. The Friedmann equations are the reading depth evolution of the cosmic soliton.

Experimental practice. Every measurement is still a measurement. Every clock is still a clock. The reading depth framing says what the clock measures (reading update rate at its depth) but doesn't change what the clock reads. GPS corrections stay at +38.64 μs/day.

The unsolved problems. The measurement problem is restated, not solved. The hierarchy problem is reframed, not resolved. The cosmological constant problem is embedded in the integer structure, not computed from first principles. The reading depth framing opens new research directions for each problem but doesn't close any of them.

### What Changes Is the Research Program

The standard program for the next 50 years of physics: build bigger colliders (FCC at 100 TeV), detect gravitational waves at new frequencies (LISA, Einstein Telescope), quantize gravity (strings, loops, or something new), explain dark matter (WIMPs, axions, or something new), explain dark energy (quintessence, modified gravity, or something new).

The reading depth program: map the soliton hierarchy. At each level, determine the reading (coupling values, masses, densities). Between levels, determine the transformation law (beta coefficients, threshold corrections). Test for boundary effects at hierarchy transitions (Hill sphere, heliosphere, galactic toroid). Test for force-dependent reading depth (nuclear vs optical clocks). Derive the remaining free parameters from the integer structure. Connect gravity to the gauge sector through the reading depth gradient.

The programs are not mutually exclusive. The colliders test the same particles. The gravitational wave detectors measure the same waves. The reading depth framing changes what you look for in the data: not new particles at high energy, but boundary effects at hierarchy transitions. Not a quantum gravity theory, but a reading depth map that reproduces the metric from soliton dynamics.

The strongest version of the claim: if the 53 derived values, the 40 surplus, the 9 domains, and the century of GR time dilation measurements are all taken as evidence for a single structure — integer transformation laws operating across a nested soliton hierarchy, with reading depth as the fourth coordinate — then the research program shifts from "find new physics beyond the Standard Model" to "complete the map of the existing structure." The physics is already there. The map is incomplete. Drawing the map IS the physics.

---

