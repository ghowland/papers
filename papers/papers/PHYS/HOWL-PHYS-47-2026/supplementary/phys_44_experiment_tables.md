### Table 1: D/K Classification of All 18 PHYS-42 Tests

| # | Test | Classification | D component | K component | Justification |
|---|---|---|---|---|---|
| 1 | Pound-Rebka | D | Δf/f = gΔh/c² | none | Static potential gradient, no ticking needed |
| 2 | GPS gravitational | D | GM/c² × (1/R_E − 1/r_gps) | none | Static potential difference between altitudes |
| 3 | GPS velocity | K | none | v²/(2c²) | Velocity requires dx/dt, which requires ticks |
| 4 | GPS net | Mixed | gravitational shift (+45.85 μs/day) | velocity shift (−7.21 μs/day) | Sum of D and K components |
| 5 | Gravity Probe A | D | GM/c² × (1/R_E − 1/(R_E+h)) | none | Static potential difference |
| 6 | Solar redshift | D | GM_S/(R_S·c²) | none | Static potential at surface |
| 7 | Mercury perihelion | D | 6πGM/(ac²(1−e²)) per 2π radians | none | Geometric curvature, "per orbit" = per 2π phase |
| 8 | Muon dilation | Mixed (D×K) | γ = 1/√(1−β²) | τ_rest = 2.197 μs | Product of spatial factor and tick budget |
| 9 | Shapiro PPN γ | D | γ_PPN = 1 (spatial curvature = temporal curvature) | none | Structural ratio, no temporal evolution |
| 10 | Hulse-Taylor Pdot | Mixed | Quadrupole formula from orbital geometry | Energy radiated per tick | Instantaneous Pdot is D; cumulative decay is K |
| 11 | SN Ia stretch | K | none | (1+z) = ratio of scale factors at two tick counts | Requires comparing two epochs |
| 12 | Planck time | Structural | — | — | Definition of tick step size |
| 13 | Planck length | Structural | — | — | Definition of spatial resolution |
| 14 | c = l_P/t_P | Structural | — | — | Identity connecting D resolution to K resolution |
| 15 | g surface | D | GM_E/R_E² | none | Static gradient |
| 16 | Earth Φ/c² | D | GM_E/(R_E·c²) | none | Static potential |
| 17 | Sun Φ/c² | D | GM_S/(R_S·c²) | none | Static potential |
| 18 | Earth r_s | D | 2GM_E/c² | none | Static radius |

**Totals:** D = 9, K = 1, Mixed = 3, Structural = 3, Unclassified = 0, Sum = 18 ✓ (errata: original plan estimated ~9 D, ~3 K, ~3 mixed, ~3 structural — confirmed)

### Table 2: Frozen Scan Completeness — Can D Predict K-Required Tests?

| Test | Classification | Frozen scan prediction | What K adds | D-complete? |
|---|---|---|---|---|
| GPS velocity | K | Cannot compute v without dt | The velocity itself | No — velocity IS a K quantity |
| SN Ia stretch | K | Can compute reading at z=0 and z=1 separately | The ratio between epochs | No — ratio requires two tick counts |
| Muon dilation | Mixed D×K | Can compute γ from spatial trajectory | τ_rest (tick budget) | Partial — D gives γ, K gives τ_rest, observation = product |
| GPS net | Mixed | Can compute D component (45.85 μs/day) | K component (−7.21 μs/day) | Partial — D gives 86% of answer |
| Hulse-Taylor | Mixed | Can compute instantaneous Pdot from geometry | Cumulative period change over time | Partial — instantaneous rate is D, accumulation is K |

**Frozen scan coverage:** 9 pure-D + 3 structural = 12 fully covered. 3 mixed = partially covered (D component computable). 2 pure-K = not coverable. Coverage: 12/18 = 67% fully, 15/18 = 83% partially.

### Table 3: D/K Decomposition Ratios at Each Hierarchy Level

| Level | Test | D component | K component | D fraction | K fraction | Notes |
|---|---|---|---|---|---|---|
| Lab (22.5 m) | Pound-Rebka | gΔh/c² = 2.46e-15 | 0 | 100% | 0% | Pure geometry |
| Earth orbit (GPS) | GPS net | +45.85 μs/day | −7.21 μs/day | 86.4% | 13.6% | D dominates, K is correction |
| Earth orbit (GPA) | Gravity Probe A | 4.25e-10 | 0 | 100% | 0% | Pure geometry |
| Solar surface | Solar redshift | 636.3 m/s | 0 | 100% | 0% | Pure geometry |
| Solar orbit | Mercury | 42.98 "/century | 0 | 100% | 0% | Pure geometry (per 2π phase) |
| Solar exterior | Shapiro | γ = 1.0 | 0 | 100% | 0% | Structural |
| Compact (NS) | Hulse-Taylor | Pdot formula (D) | GW radiation (K) | ~95% | ~5% | Instantaneous rate is D |
| SR velocity | Muon | γ = 15.8 (D) | τ_rest = 2.2 μs (K) | multiplicative | multiplicative | D×K product |
| Cosmological | SN Ia | reading at z=1 | tick count ratio | 0% | 100% | Pure K (epoch comparison) |

### Table 4: Sector Splitting Predictions — SM vs CD Betas

| Quantity | SM betas | CD betas | Ratio | Pool key |
|---|---|---|---|---|
| β₁ | 41/10 = 4.100 | 25/6 = 4.167 | 1.016 | beta_sm_u1_total_v0 / beta_modified_u1_total_v0 |
| β₂ | −19/6 = −3.167 | −13/6 = −2.167 | 0.684 | beta_sm_su2_total_v0 / beta_modified_su2_total_v0 |
| β₃ | −7/1 = −7.000 | −20/3 = −6.667 | 0.952 | beta_sm_su3_total_v0 / beta_modified_su3_total_v0 |
| \|β₃ − β₁\| | 111/10 = 11.100 | 65/6 = 10.833 | 0.976 | computed |
| \|β₃ − β₂\| | 23/6 = 3.833 | 9/2 = 4.500 | 1.174 | computed |
| \|β₂ − β₁\| | 79/30 = 2.633 | 19/3 = 6.333 | 2.405 | computed |
| ε(3,1) at κ=1, Δh=1000m | 1.21e-12 | 1.18e-12 | 0.976 | derivation output |
| ε(3,2) at κ=1, Δh=1000m | 4.18e-13 | 4.91e-13 | 1.174 | derivation output |
| ε(2,1) at κ=1, Δh=1000m | 2.87e-13 | 6.90e-13 | 2.405 | derivation output |

The (3,1) splitting differs by only 2.4% between SM and CD. The (2,1) splitting differs by a factor of 2.4 — this pair discriminates between SM and CD betas if measured.

### Table 5: WEP Consistency Check Against MICROSCOPE

| Quantity | Value | Source |
|---|---|---|
| MICROSCOPE bound on η(Ti,Pt) | < 1.5 × 10⁻¹⁵ | Touboul et al. 2022 |
| Ti nuclear binding fraction | ~8.8 MeV/nucleon × 48 = 422 MeV of 44650 MeV total | ~0.94% |
| Pt nuclear binding fraction | ~7.9 MeV/nucleon × 195 = 1541 MeV of 181950 MeV total | ~0.85% |
| Binding fraction difference (Ti − Pt) | ~0.09% | composition |
| If gravity couples to sector sum | Δg/g = 0 (sector-blind gravity) | no WEP violation |
| If gravity couples per-sector | Δg/g ~ ε × Δ(binding fraction) ~ ε × 0.001 | possible violation |
| Constraint on ε from MICROSCOPE | ε < 1.5e-15 / 0.001 = 1.5e-12 | κ < ~1.2 at SM betas |
| Constraint on κ from MICROSCOPE (per-sector gravity) | κ < 1.2 | barely constrains κ=1 |
| Constraint on κ from MICROSCOPE (sum gravity) | none | sector-blind gravity has no WEP violation |

**Key finding:** If gravity couples to the SUM of all sector readings (the natural assumption in RUM — total reading depth, not per-sector), there is NO WEP violation and MICROSCOPE does not constrain ε. The sector splitting appears only in clocks (which read individual sectors) not in free fall (which responds to total depth). This is why Test 1 (clock comparison) is the right test, not free fall experiments.

If gravity couples per-sector, MICROSCOPE constrains κ < ~1.2 for the (3,1) pair — barely touching κ = 1. The constraint is weak because Ti and Pt have similar nuclear binding fractions (both heavy nuclei). A lighter element comparison (e.g., hydrogen vs lead) would be more constraining.

### Table 6: Sector Splitting at Multiple κ Values — Full Prediction Table

| κ | Physical meaning | ε(3,1) SM | ε(3,1) CD | Margin over 10⁻¹⁸ | Detectable? |
|---|---|---|---|---|---|
| 1 | Direct mapping | 1.21e-12 | 1.18e-12 | 10⁶ | Yes |
| α_em = 1/137 | One EM loop suppression | 8.83e-15 | 8.61e-15 | 10³·⁹ | Yes |
| α_em² = 1/18800 | Two EM loops | 6.44e-17 | 6.28e-17 | 10¹·⁸ | Yes |
| α_s = 0.118 | One QCD loop | 1.43e-13 | 1.39e-13 | 10⁴·² | Yes |
| Φ_earth/c² = 7e-10 | Gravitational self-suppression | 8.47e-22 | 8.27e-22 | 10⁻³·⁹ | No |
| α_em × Φ/c² | Double suppression | 6.18e-24 | 6.03e-24 | 10⁻⁵·⁸ | No |
| 10⁻⁶ | Threshold for detection | 1.21e-18 | 1.18e-18 | 1 | Barely |
| 10⁻⁷ | Below detection | 1.21e-19 | 1.18e-19 | 0.1 | No |

**Detection window:** κ > 10⁻⁶ is detectable with projected 10⁻¹⁸ sensitivity. κ > 10⁻⁷ is detectable with 10⁻¹⁹ sensitivity. The natural suppression mechanisms (loop factors α, α², α_s) all keep ε above the threshold. Only gravitational self-suppression (κ = Φ/c²) pushes the signal below detection.

### Table 7: Tick Budget — K-Quantities in Planck Units

| Quantity | Value (SI) | Value (Planck ticks) | log₁₀(ticks) | Pool source |
|---|---|---|---|---|
| Muon rest lifetime | 2.197 × 10⁻⁶ s | 4.08 × 10³⁷ | 37.6 | astro_muon_rest_lifetime_v0 |
| Proton lifetime (GUT) | ~10⁴² s | ~1.86 × 10⁸⁵ | 85.3 | gr_proton_lifetime_s_v0 |
| Universe age | 4.35 × 10¹⁷ s | 8.07 × 10⁶⁰ | 60.9 | gr_universe_age_s_v0 |
| Mercury orbital period | 7.60 × 10⁶ s | 1.41 × 10⁵⁰ | 50.1 | gr_mercury_period_days_v0 |
| GPS orbital period | 4.31 × 10⁴ s | 7.99 × 10⁴⁷ | 47.9 | from r_gps |
| Hulse-Taylor orbital period | 2.79 × 10⁴ s | 5.17 × 10⁴⁷ | 47.7 | published |
| Pound-Rebka photon transit | 7.50 × 10⁻⁸ s | 1.39 × 10³⁶ | 36.1 | from h/c |
| SN Ia lookback (z=1) | ~3.1 × 10¹⁷ s | 5.75 × 10⁶⁰ | 60.8 | cosmological |

Everything in the K column requires ticking. Everything in the D column (Tables 1-3) does not. The tick budget ranges from 10³⁶ (photon crossing 22.5 m) to 10⁸⁵ (proton lifetime) — 49 orders of magnitude in tick count.

### Table 8: Experiment Input Map — All Pool Values Used

| Derivation | Pool key | Value | Type | Purpose |
|---|---|---|---|---|
| 1 | beta_sm_u1_total_v0 | 41/10 | exact_fraction | EM sector β |
| 1 | beta_sm_su3_total_v0 | −7/1 | exact_fraction | Strong sector β |
| 1 | beta_sm_su2_total_v0 | −19/6 | exact_fraction | Weak sector β |
| 1 | beta_modified_u1_total_v0 | 25/6 | exact_fraction | CD EM sector β |
| 1 | beta_modified_su3_total_v0 | −20/3 | exact_fraction | CD strong sector β |
| 1 | beta_modified_su2_total_v0 | −13/6 | exact_fraction | CD weak sector β |
| 1 | si_speed_of_light_v0 | 299792458 | exact_integer | c for ΔΦ/c² |
| 1 | coupling_alpha_em_inverse_v0 | 137035999177/10⁹ | exact_fraction | α for loop suppression |
| 1 | result_earth_phi_over_c2_v0 | 6.961e-10 | approximate | Earth Φ/c² |
| 1,5 | result_g_surface_from_gm_v0 | 9.820 | approximate | g for ΔΦ computation |
| 2,3,4 | All 18 PHYS-42 result_* keys | various | approximate | Classification inputs |
| 4 | astro_gravitational_constant_v0 | Fraction | exact_fraction | G for hierarchy scan |
| 4 | astro_mass_earth_v0 | Fraction | exact_fraction | M_E |
| 4 | astro_mass_sun_v0 | Fraction | exact_fraction | M_S |
| 4 | astro_radius_earth_v0 | Fraction | exact_fraction | R_E |
| 4 | astro_radius_sun_v0 | Fraction | exact_fraction | R_S |
| 4 | astro_gps_orbit_radius_v0 | Fraction | exact_fraction | r_gps |
| 4 | gr_ns_typical_mass_solar_v0 | 7/5 | exact_fraction | M_NS |
| 4 | gr_ns_typical_radius_m_v0 | 10000/1 | exact_fraction | R_NS |
| 5 | astro_muon_rest_lifetime_v0 | Fraction | exact_fraction | τ_rest (K quantity) |
| 5 | gr_planck_time_s_v0 | approximate | approximate | t_P for tick counting |
| 5 | gr_muon_cosmic_ray_beta_v0 | 499/500 | exact_fraction | β for γ computation |
| 5 | astro_gps_satellite_velocity_v0 | Fraction | exact_fraction | v_gps for K component |
| 5 | gr_universe_age_s_v0 | approximate | approximate | Universe age in ticks |
| 5 | gr_sn1a_redshift_v0 | 1/2 | exact_fraction | z for SN Ia |
| NEW | test_clock_altitude_difference_v0 | 1000 | exact_integer | Reference Δh |
| NEW | test_clock_sensitivity_target_v0 | 0.000000000000000001 | approximate | 10⁻¹⁸ threshold |

**Total pool reads:** 27 existing + 2 new = 29 values. No hardcoded physics.

### Table 9: Comparison Spec — All 20 Comparisons

| # | Derivation | Label | output_key | match_mode | expected | gate |
|---|---|---|---|---|---|---|
| 1 | 1 | β₃−β₁ (SM) | result_sector_beta_diff_sm_v0 | exact | 111/10 | — |
| 2 | 1 | β₃−β₁ (CD) | result_sector_beta_diff_cd_v0 | exact | 65/6 | — |
| 3 | 1 | ε(κ=1) detectable | result_splitting_detectable_kappa_1_v0 | bool | true | — |
| 4 | 1 | ε(κ=α) detectable | result_splitting_detectable_kappa_alpha_v0 | bool | true | — |
| 5 | 1 | max κ for null | result_max_kappa_for_null_v0 | range | [1e-8, 1e-5] | — |
| 6 | 1 | WEP consistent (sum gravity) | result_wep_sum_gravity_ok_v0 | bool | true | — |
| 7 | 2 | D-type count | result_count_static_d_v0 | range | [8, 11] | — |
| 8 | 2 | K-type count | result_count_dynamic_k_v0 | range | [1, 3] | — |
| 9 | 2 | Mixed count | result_count_mixed_v0 | range | [2, 4] | — |
| 10 | 2 | All D tests passed | result_d_tests_all_pass_v0 | bool | true | — |
| 11 | 2 | All K tests passed | result_k_tests_all_pass_v0 | bool | true | — |
| 12 | 3 | Frozen scan coverage | result_frozen_scan_coverage_v0 | range | [0.60, 0.90] | — |
| 13 | 3 | K-required count | result_k_required_count_v0 | range | [1, 4] | — |
| 14 | 3 | Total = 18 | result_classification_total_v0 | exact | 18 | — |
| 15 | 4 | Earth Φ/c² vs PHYS-42 | result_hierarchy_depth_earth_v0 | miss_pct | 0.000000000696 | — |
| 16 | 4 | Sun Φ/c² vs PHYS-42 | result_hierarchy_depth_sun_v0 | miss_pct | 0.00000212 | — |
| 17 | 4 | All frozen readings match | result_hierarchy_matches_phys42_v0 | bool | true | — |
| 18 | 5 | GPS K fraction | result_gps_k_fraction_v0 | range | [0.10, 0.25] | — |
| 19 | 5 | Muon tick budget log₁₀ | result_muon_tick_budget_log10_v0 | range | [36, 39] | — |
| 20 | 5 | K adds information | result_k_adds_information_v0 | bool | true | — |

### Table 10: Expected Outputs — All Derivation Return Keys

| Derivation | Output key | Expected value | Type |
|---|---|---|---|
| 1 | result_sector_beta_diff_sm_v0 | 111/10 | Fraction |
| 1 | result_sector_beta_diff_cd_v0 | 65/6 | Fraction |
| 1 | result_sm_cd_ratio_v0 | ~1.025 | approximate |
| 1 | result_delta_phi_1000m_v0 | ~1.09e-13 | approximate |
| 1 | result_splitting_kappa_1_sm_v0 | ~1.21e-12 | approximate |
| 1 | result_splitting_kappa_1_cd_v0 | ~1.18e-12 | approximate |
| 1 | result_splitting_kappa_alpha_v0 | ~8.83e-15 | approximate |
| 1 | result_splitting_kappa_alpha2_v0 | ~6.44e-17 | approximate |
| 1 | result_splitting_kappa_alpha_s_v0 | ~1.43e-13 | approximate |
| 1 | result_splitting_kappa_phi_v0 | ~8.47e-22 | approximate |
| 1 | result_splitting_detectable_kappa_1_v0 | True | bool |
| 1 | result_splitting_detectable_kappa_alpha_v0 | True | bool |
| 1 | result_max_kappa_for_null_v0 | ~1e-6 | approximate |
| 1 | result_wep_sum_gravity_ok_v0 | True | bool |
| 1 | result_wep_persector_kappa_limit_v0 | ~1.2 | approximate |
| 2 | result_count_static_d_v0 | 9 | integer |
| 2 | result_count_dynamic_k_v0 | 1 | integer |
| 2 | result_count_mixed_v0 | 3 | integer |
| 2 | result_count_structural_v0 | 3 | integer |
| 2 | result_classification_total_v0 | 18 | integer |
| 2 | result_d_tests_all_pass_v0 | True | bool |
| 2 | result_k_tests_all_pass_v0 | True | bool |
| 3 | result_d_complete_count_v0 | 12 | integer |
| 3 | result_k_required_count_v0 | 2 | integer |
| 3 | result_mixed_partial_count_v0 | 3 | integer |
| 3 | result_frozen_scan_coverage_v0 | ~0.83 | approximate |
| 4 | result_hierarchy_depth_earth_v0 | ~6.96e-10 | approximate |
| 4 | result_hierarchy_depth_sun_v0 | ~2.12e-6 | approximate |
| 4 | result_hierarchy_depth_mercury_v0 | ~2.6e-8 | approximate |
| 4 | result_hierarchy_depth_gps_v0 | ~1.7e-10 | approximate |
| 4 | result_hierarchy_depth_ns_v0 | ~0.21 | approximate |
| 4 | result_hierarchy_matches_phys42_v0 | True | bool |
| 4 | result_frozen_scan_max_miss_v0 | ~0 | approximate |
| 5 | result_gps_d_component_us_v0 | ~45.85 | approximate |
| 5 | result_gps_k_component_us_v0 | ~7.21 | approximate |
| 5 | result_gps_k_fraction_v0 | ~0.136 | approximate |
| 5 | result_muon_d_factor_v0 | ~15.8 | approximate |
| 5 | result_muon_k_budget_s_v0 | ~2.197e-6 | approximate |
| 5 | result_muon_tick_budget_v0 | ~4.08e37 | approximate |
| 5 | result_muon_tick_budget_log10_v0 | ~37.6 | approximate |
| 5 | result_sn1a_tick_count_v0 | ~5.75e60 | approximate |
| 5 | result_sn1a_tick_count_log10_v0 | ~60.8 | approximate |
| 5 | result_k_adds_information_v0 | True | bool |

**Total outputs:** 42 values from 5 derivations. 20 comparisons test a subset of these.
