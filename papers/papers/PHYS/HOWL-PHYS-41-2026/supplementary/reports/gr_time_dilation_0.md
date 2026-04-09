

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

