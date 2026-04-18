======================================================================
DATA-6 RUNNER: experiment_clock_reading_decomposition_v0
======================================================================

  Source: /mnt/c/Users/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code/data/experiment_clock_reading_decomposition_v0.json
  Mode:   standard
  Purpose: program_clock_reading_decomposition_v0

Loaded 2331 value nodes.

----------------------------------------------------------------------
PRE-FLIGHT WARNINGS: 8
----------------------------------------------------------------------
  [WARN] value missing: gr_muon_cosmic_ray_beta_v0
  [WARN] value missing: gr_planck_time_s_v0
  [WARN] value missing: gr_planck_length_m_v0
  [WARN] value missing: gr_ns_typical_mass_solar_v0
  [WARN] value missing: gr_ns_typical_radius_m_v0
  [WARN] value missing: gr_universe_age_s_v0
  [WARN] value missing: gr_sn1a_redshift_v0
  [WARN] value missing: gr_mercury_semi_major_au_v0

----------------------------------------------------------------------
EXECUTION PLAN: 5 derivations
----------------------------------------------------------------------
  [ERROR] sector_splitting_prediction_v0                          'missing value: result_g_surface_from_gm_v0'
  [OK] static_vs_dynamic_classification_v0                      7 outputs
  [OK] frozen_scan_completeness_v0                              6 outputs
  [ERROR] reading_hierarchy_scan_v0                               astro_gravitational_constant_v0 is not Fraction: <class 'str'>
  [ERROR] tick_observable_unique_v0                               astro_gravitational_constant_v0 is not Fraction: <class 'str'>

Derivations: 2 OK, 3 errors

WARNING: 32 expected outputs missing:
  - result_sector_beta_diff_sm_v0
  - result_sector_beta_diff_cd_v0
  - result_sm_cd_ratio_v0
  - result_delta_phi_1000m_v0
  - result_splitting_kappa_1_sm_v0
  - result_splitting_kappa_1_cd_v0
  - result_splitting_kappa_alpha_v0
  - result_splitting_kappa_alpha2_v0
  - result_splitting_kappa_alpha_s_v0
  - result_splitting_kappa_phi_v0
  - result_splitting_detectable_kappa_1_v0
  - result_splitting_detectable_kappa_alpha_v0
  - result_max_kappa_for_null_v0
  - result_wep_sum_gravity_ok_v0
  - result_wep_persector_kappa_limit_v0
  - result_hierarchy_depth_earth_v0
  - result_hierarchy_depth_sun_v0
  - result_hierarchy_depth_mercury_v0
  - result_hierarchy_depth_gps_v0
  - result_hierarchy_depth_ns_v0
  - result_hierarchy_matches_phys42_v0
  - result_frozen_scan_max_miss_v0
  - result_gps_d_component_us_v0
  - result_gps_k_component_us_v0
  - result_gps_k_fraction_v0
  - result_muon_d_factor_v0
  - result_muon_k_budget_s_v0
  - result_muon_tick_budget_v0
  - result_muon_tick_budget_log10_v0
  - result_sn1a_tick_count_v0
  - result_sn1a_tick_count_log10_v0
  - result_k_adds_information_v0

----------------------------------------------------------------------
COMPARISONS: 20 checks
----------------------------------------------------------------------

  [SKIP] C01: beta3-beta1 SM exact                          exact           output not found in pool
  [SKIP] C02: beta3-beta1 CD exact                          exact           output not found in pool
  [SKIP] C03: epsilon(kappa=1) detectable                   bool            output not found in pool
  [SKIP] C04: epsilon(kappa=alpha) detectable               bool            output not found in pool
  [SKIP] C05: max kappa for null                            range           output not found in pool
  [SKIP] C06: WEP consistent (sum gravity)                  bool            output not found in pool
  [PASS] C07: D-type count                                  range           in [8, 11]
  [PASS] C08: K-type count                                  range           in [1, 3]
  [PASS] C09: Mixed count                                   range           in [2, 4]
  [FAIL] C10: All D tests passed in PHYS-42                 bool            expected True got True
  [FAIL] C11: All K tests passed in PHYS-42                 bool            expected True got True
  [PASS] C12: Frozen scan coverage                          range           in [0.60, 0.90]
  [PASS] C13: K-required count                              range           in [1, 4]
  [PASS] C14: Classification total = 18                     exact           exact match
  [SKIP] C15: Earth Phi/c2 vs PHYS-42                       miss_pct        output not found in pool
  [SKIP] C16: Sun Phi/c2 vs PHYS-42                         miss_pct        output not found in pool
  [SKIP] C17: All frozen readings match PHYS-42             bool            output not found in pool
  [SKIP] C18: GPS K fraction                                range           output not found in pool
  [SKIP] C19: Muon tick budget log10                        range           output not found in pool
  [SKIP] C20: K adds information                            bool            output not found in pool

----------------------------------------------------------------------
DIAGRAMS: 3 specs (use 'data6.py diagram' to render)
----------------------------------------------------------------------
  [SPEC] diagram_dk_decomposition_v0                        D/K decomposition of PHYS-42 tests
  [SPEC] diagram_sector_splitting_v0                        Sector splitting: SM vs CD betas
  [SPEC] diagram_gps_decomposition_v0                       GPS net shift: D and K components

Result written: result_experiment_clock_reading_decomposition_v0_run001.json
Values written: values_experiment_clock_reading_decomposition_v0_run001.json

======================================================================
EXPERIMENT SUMMARY
======================================================================

  Derivations:  2 / 5
  Connections:  0 / 0

  PASS: 6
  FAIL: 2
  INFO: 0
  SKIP: 12

  STATUS: 2 FAILURES

======================================================================
geoff@LAPTOP-7TKDV18T:/mnt/c/Users/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code$ ./data7.py report experiment_clock_reading_decomposition_v0

======================================================================
DATA-6 REPORT: experiment_clock_reading_decomposition_v0
======================================================================

  Result file:  result_experiment_clock_reading_decomposition_v0_run001.json
  Timestamp:    2026-04-10T01:39:41Z
  Status:       partial
  Mode:         standard
  Purpose:      program_clock_reading_decomposition_v0

----------------------------------------------------------------------
DERIVATION OUTPUTS: 12 values
----------------------------------------------------------------------

  static_vs_dynamic_classification_v0
  -----------------------------------
    result_classification_total_v0                          18
    result_count_dynamic_k_v0                               1
    result_count_mixed_v0                                   4
    result_count_static_d_v0                                10
    result_count_structural_v0                              3
    result_d_tests_all_pass_v0                              True
    result_k_tests_all_pass_v0                              True

  frozen_scan_completeness_v0
  ---------------------------
    result_d_complete_count_v0                              13
    result_frozen_scan_coverage_v0                          0.888888888888889
    result_frozen_scan_full_v0                              0.722222222222222
    result_k_required_count_v0                              2
    result_mixed_partial_count_v0                           3

----------------------------------------------------------------------
COMPARISONS: 20 checks
----------------------------------------------------------------------

  [SKIP] C01: beta3-beta1 SM exact
    detail:   output not found in pool

  [SKIP] C02: beta3-beta1 CD exact
    detail:   output not found in pool

  [SKIP] C03: epsilon(kappa=1) detectable
    detail:   output not found in pool

  [SKIP] C04: epsilon(kappa=alpha) detectable
    detail:   output not found in pool

  [SKIP] C05: max kappa for null
    detail:   output not found in pool

  [SKIP] C06: WEP consistent (sum gravity)
    detail:   output not found in pool

  [PASS] C07: D-type count
    got:      10.0
    range:    [8, 11]

  [PASS] C08: K-type count
    got:      1.0
    range:    [1, 3]

  [PASS] C09: Mixed count
    got:      4.0
    range:    [2, 4]

  [FAIL] C10: All D tests passed in PHYS-42
    expected: ?
    got:      True
    diverge:  position 0: 'T' vs '?'
    status:   FAIL

  [FAIL] C11: All K tests passed in PHYS-42
    expected: ?
    got:      True
    diverge:  position 0: 'T' vs '?'
    status:   FAIL

  [PASS] C12: Frozen scan coverage
    got:      0.888889
    range:    [0.60, 0.90]

  [PASS] C13: K-required count
    got:      2.0
    range:    [1, 4]

  [PASS] C14: Classification total = 18
    expected: 18
    got:      18
    status:   PASS (exact Fraction match)

  [SKIP] C15: Earth Phi/c2 vs PHYS-42
    detail:   output not found in pool

  [SKIP] C16: Sun Phi/c2 vs PHYS-42
    detail:   output not found in pool

  [SKIP] C17: All frozen readings match PHYS-42
    detail:   output not found in pool

  [SKIP] C18: GPS K fraction
    detail:   output not found in pool

  [SKIP] C19: Muon tick budget log10
    detail:   output not found in pool

  [SKIP] C20: K adds information
    detail:   output not found in pool

======================================================================
SUMMARY
======================================================================

  Derivations OK:  2
  Derivations err: 3

  PASS: 6
  FAIL: 2
  INFO: 0
  SKIP: 12

  EXPERIMENT: PARTIAL

======================================================================
