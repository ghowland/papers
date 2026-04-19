geoff@LAPTOP-7TKDV18T:~/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code$ ./data7.py run experiment_giga_remainder_test_v0
======================================================================
DATA-6 RUNNER: experiment_giga_remainder_test_v0
======================================================================

  Source: /mnt/c/Users/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code/data/experiment_giga_remainder_test_v0.json
  Mode:   standard
  Purpose: program_remainder_v0

Loaded 3788 value nodes.

----------------------------------------------------------------------
EXECUTION PLAN: 11 derivations
----------------------------------------------------------------------
  [OK] giga_ckm_from_integers_v0                               16 outputs
  [OK] giga_cosmological_closure_v0                            15 outputs
  [OK] giga_hubble_tension_v0                                   8 outputs
  [OK] giga_hadron_koide_v0                                    37 outputs
  [OK] giga_nuclear_binding_v0                                  5 outputs
  [OK] giga_hill_sphere_v0                                      7 outputs
  [OK] giga_chandrasekhar_v0                                    4 outputs
  [OK] giga_muon_g2_toroidal_v0                                 6 outputs
  [OK] giga_koide_amplitude_map_v0                             10 outputs
  [OK] giga_filling_fraction_ladder_v0                         27 outputs
  [OK] giga_microscopic_cosmic_bridge_v0                        7 outputs

Derivations: 11 OK, 0 errors

WARNING: 3 expected outputs missing:
  - result_koide_leptons_v0
  - result_koide_pnl_v0
  - result_koide_sigma_v0

----------------------------------------------------------------------
COMPARISONS: 10 checks
----------------------------------------------------------------------

  [PASS] G01: |V_us| = 9/40 at sub-10 ppm                   range           in [0, 50]
  [PASS] G02: |V_cb| = 1/24 at sub-1%                       range           in [0, 1]
  [FAIL] G03: |V_ub| = 1/264 at sub-2%                      range           2.79183 not in [0, 2]
  [FAIL] G04: |V_cb/V_ub| = 11 (Yang-Mills)                 range           3.07269 not in [0, 1]
  [PASS] G05: Omega_Lambda = (251-22pi)/264                 range           in [0, 2]
  [PASS] G06: Hubble ratio = 12/11                          range           in [0, 2]
  [PASS] G07: Lepton Koide K = 2/3                          range           in [0, 20]
  [PASS] G08: Nuclear a_A/a_V ~ 3/2                         range           in [0, 1]
  [PASS] G09: Chandrasekhar coeff ~ 15pi/8                  range           in [0, 2]
  [PASS] G10: DM/baryon = 22pi/13                           range           in [0, 1000]

----------------------------------------------------------------------
DIAGRAMS: 1 specs (use 'data6.py diagram' to render)
----------------------------------------------------------------------
  [SPEC] diagram_giga_remainder_v0                          The giga remainder test: 15 chains across 7 hierarchy levels

Result written: result_experiment_giga_remainder_test_v0_run001.json
Values written: values_experiment_giga_remainder_test_v0_run001.json

======================================================================
EXPERIMENT SUMMARY
======================================================================

  Derivations:  11 / 11
  Connections:  0 / 0

  PASS: 8
  FAIL: 2
  INFO: 0
  SKIP: 0

  STATUS: 2 FAILURES

======================================================================
geoff@LAPTOP-7TKDV18T:~/Geoff/work/papers/papers/papers/DATA/HOWL-DATA-7-2026/code$ ./data7.py report experiment_giga_remainder_test_
v0

======================================================================
DATA-6 REPORT: experiment_giga_remainder_test_v0
======================================================================

  Result file:  result_experiment_giga_remainder_test_v0_run001.json
  Timestamp:    2026-04-19T09:28:35Z
  Status:       partial
  Mode:         standard
  Purpose:      program_remainder_v0

----------------------------------------------------------------------
DERIVATION OUTPUTS: 140 values
----------------------------------------------------------------------

  giga_hill_sphere_v0
  -------------------
    result_hill_earth_mass_ratio_v0                         3.00251382604324e-6
    result_hill_earth_rh_km_v0                              1496417.73709308
    result_hill_earth_rh_over_a_v0                          0.0100027923602479
    result_hill_moon_rh_km_v0                               61514.0735806905
    result_hill_moon_rh_over_a_v0                           0.160026205985147
    result_modulus_exponent_v0                              1/3 from 3D gravity
    result_remainder_v0                                     mass ratio m/M (specific inertia)

  (unassigned)
  ------------
    result_R2_R1_miss_pct_v0                                0.970257631709563
    result_R2_R1_nearest_v0                                 7/9
    result_R2_R1_ratio_v0                                   0.785398163397448
    result_R2_R1_rational_v0                                False
    result_R3_R2_miss_pct_v0                                0.0
    result_R3_R2_nearest_v0                                 2/3
    result_R3_R2_ratio_v0                                   0.666666666666667
    result_R3_R2_rational_v0                                True
    result_R4_R3_miss_pct_v0                                1.85916357881301
    result_R4_R3_nearest_v0                                 3/5
    result_R4_R3_ratio_v0                                   0.589048622548086
    result_R4_R3_rational_v0                                False
    result_R5_R4_miss_pct_v0                                4.16666666666667
    result_R5_R4_nearest_v0                                 5/9
    result_R5_R4_ratio_v0                                   0.533333333333333
    result_R5_R4_rational_v0                                False
    result_R6_R5_miss_pct_v0                                1.85916357881302
    result_R6_R5_nearest_v0                                 1/2
    result_R6_R5_ratio_v0                                   0.490873852123405
    result_R6_R5_rational_v0                                False
    result_R7_R6_miss_pct_v0                                2.77777777777778
    result_R7_R6_nearest_v0                                 4/9
    result_R7_R6_ratio_v0                                   0.457142857142857
    result_R7_R6_rational_v0                                False
    result_a2_bosons_v0                                     0.0180873849346908
    result_a2_down_quarks_v0                                2.387725461
    result_a2_leptons_miss_from_2_ppm_v0                    18.4656
    result_a2_leptons_v0                                    1.9999630688
    result_a2_up_quarks_v0                                  3.0927612855
    result_amu_anomaly_v0                                   3.181e-9
    result_amu_measured_v0                                  0.00116592059
    result_amu_sm_total_v0                                  0.001165917409
    result_bridge_miss_pct_v0                               0.0297315984938017
    result_bridge_ratio_v0                                  95504463039.3728
    result_chandrasekhar_coeff_v0                           5.836
    result_chandrasekhar_formula_v0                         15*pi/8 = 5.890486 vs Lane-Emden 5.836
    result_chandrasekhar_miss_pct_v0                        0.933622780686469
    result_chandrasekhar_predicted_v0                       5.89048622548086
    result_common_factor_v0                                 8 = dim(SU(3) adjoint)
    result_cosmic_v0                                        5.31654141376734
    result_dm_baryon_measured_v0                            5.3204
    result_dm_baryon_miss_ppm_v0                            725.243634436809
    result_dm_baryon_predicted_v0                           5.31654141376734
    result_h0_cmb_v0                                        67.4
    result_h0_local_predicted_miss_pct_v0                   0.667131335258389
    result_h0_local_predicted_v0                            73.5272727272727
    result_h0_local_v0                                      73.04
    result_hubble_ratio_miss_pct_v0                         0.667131335258389
    result_hubble_ratio_predicted_v0                        1.09090909090909
    result_hubble_ratio_v0                                  1.08367952522255
    result_integer_22_v0                                    22 = 2 * 11 (Yang-Mills doubled)
    result_integer_251_v0                                   251 = 264 - 13
    result_integer_264_v0                                   264 = 8 * 3 * 11
    result_interpretation_v0                                cosmic/micro = 3*(M_Z/m_e)^2: the Z mass bridges scales
    result_k_bosons_v0                                      0.336347897489115
    result_k_down_quarks_v0                                 0.731287576833333
    result_k_leptons_v0                                     0.666660511466667
    result_k_up_quarks_v0                                   0.848793547583333
    result_koide_leptons_e_mu_tau_a2_v0                     1.99996306879313
    result_koide_leptons_e_mu_tau_miss_pct_v0               0.000923288696241085
    result_koide_leptons_e_mu_tau_nearest_v0                2/3
    result_koide_leptons_e_mu_tau_v0                        0.666660511465522
    result_koide_leptons_miss_ppm_v0                        9.23280171701454
    result_koide_pi_k_d_a2_v0                               0.515053514524759
    result_koide_pi_k_d_miss_pct_v0                         2.24150526333692
    result_koide_pi_k_d_nearest_v0                          3/7
    result_koide_pi_k_d_v0                                  0.419175585754126
    result_koide_pi_k_eta_a2_v0                             0.147945688713594
    result_koide_pi_k_eta_miss_pct_v0                       4.75125194378293
    result_koide_pi_k_eta_nearest_v0                        3/8
    result_koide_pi_k_eta_v0                                0.357990948118932
    result_koide_pnl_p_n_lambda_a2_v0                       0.0033989958421679
    result_koide_pnl_p_n_lambda_miss_pct_v0                 0.169661452822044
    result_koide_pnl_p_n_lambda_nearest_v0                  1/3
    result_koide_pnl_p_n_lambda_v0                          0.333899832640361
    result_koide_rho_kstar_phi_a2_v0                        0.00623297568326428
    result_koide_rho_kstar_phi_miss_pct_v0                  0.310680552000275
    result_koide_rho_kstar_phi_nearest_v0                   1/3
    result_koide_rho_kstar_phi_v0                           0.334372162613877
    result_koide_sigma_plus_zero_minus_a2_v0                3.86545547196555e-6
    result_koide_sigma_plus_zero_minus_miss_pct_v0          0.00019327240005911
    result_koide_sigma_plus_zero_minus_nearest_v0           1/3
    result_koide_sigma_plus_zero_minus_v0                   0.333333977575912
    result_koide_sigma_xi_omega_a2_v0                       0.0105409028091753
    result_koide_sigma_xi_omega_miss_pct_v0                 0.524281937982337
    result_koide_sigma_xi_omega_nearest_v0                  1/3
    result_koide_sigma_xi_omega_v0                          0.335090150468196
    result_koide_upsilon_1s_2s_3s_a2_v0                     0.000694110481744517
    result_koide_upsilon_1s_2s_3s_miss_pct_v0               0.0346934835319413
    result_koide_upsilon_1s_2s_3s_nearest_v0                1/3
    result_koide_upsilon_1s_2s_3s_v0                        0.333449018413624
    result_koide_w_z_h_a2_v0                                0.0180873849346908
    result_koide_w_z_h_miss_pct_v0                          0.896263713341448
    result_koide_w_z_h_nearest_v0                           1/3
    result_koide_w_z_h_v0                                   0.336347897489115
    result_mass_ratio_sq_v0                                 42753.1227342086
    result_microscopic_v0                                   5.56679891658627e-11
    result_muon_toroidal_4loop_v0                           1.28259368202626e-9
    result_mz_me_ratio_v0                                   178449.681504961
    result_nuclear_aa_av_interpretation_v0                  a_A/a_V = 1.4968 vs 3/2 = R2/R3 (inverse Koide)
    result_nuclear_aa_av_miss_pct_v0                        0.214224507283633
    result_nuclear_aa_av_ratio_v0                           1.49678663239075
    result_nuclear_ac_av_ratio_v0                           0.0447943444730077
    result_nuclear_as_av_ratio_v0                           1.1073264781491
    result_omega_b_miss_pct_v0                              0.494743351886209
    result_omega_b_predicted_v0                             0.0492424242424242
    result_omega_dm_miss_pct_v0                             0.421706098638065
    result_omega_dm_predicted_v0                            0.261799387799149
    result_omega_lambda_exact_v0                            0.688958187958426
    result_omega_lambda_miss_pct_v0                         0.00844650289248382
    result_omega_lambda_predicted_v0                        0.688958187958426
    result_omega_lambda_symbolic_v0                         (251 - 22*pi)/264
    result_physical_ladder_rational_count_v0                1
    result_physical_ladder_transitions_v0                   2
    result_r3r2_is_unique_physical_v0                       True
    result_sum_check_v0                                     1.0
    result_three_mz_me_sq_v0                                95532866487.6665
    result_toroidal_fraction_of_anomaly_v0                  0.403204552664652
    result_vcb_fraction_v0                                  1/24 = 1/(8*3)
    result_vcb_measured_v0                                  0.04182
    result_vcb_miss_pct_v0                                  0.366650725330783
    result_vcb_predicted_v0                                 0.0416666666666667
    result_vcb_vub_ratio_measured_v0                        11.348710990502
    result_vcb_vub_ratio_miss_pct_v0                        3.0726924916308
    result_vcb_vub_ratio_predicted_v0                       11.0
    result_vub_fraction_v0                                  1/264 = 1/(8*3*11)
    result_vub_measured_v0                                  0.003685
    result_vub_miss_pct_v0                                  2.79182599399696
    result_vub_predicted_v0                                 0.00378787878787879
    result_vus_fraction_v0                                  9/40 = 3^2/(8*5)
    result_vus_measured_v0                                  0.22501
    result_vus_miss_ppm_v0                                  44.4424692235901
    result_vus_predicted_v0                                 0.225

----------------------------------------------------------------------
COMPARISONS: 10 checks
----------------------------------------------------------------------

  [PASS] G01: |V_us| = 9/40 at sub-10 ppm
    got:      44.4425
    range:    [0, 50]

  [PASS] G02: |V_cb| = 1/24 at sub-1%
    got:      0.366651
    range:    [0, 1]

  [FAIL] G03: |V_ub| = 1/264 at sub-2%
    expected: ?
    got:      2.79183
    diverge:  position 0: '2' vs '?'
    status:   FAIL

  [FAIL] G04: |V_cb/V_ub| = 11 (Yang-Mills)
    expected: ?
    got:      3.07269
    diverge:  position 0: '3' vs '?'
    status:   FAIL

  [PASS] G05: Omega_Lambda = (251-22pi)/264
    got:      0.0084465
    range:    [0, 2]

  [PASS] G06: Hubble ratio = 12/11
    got:      0.667131
    range:    [0, 2]

  [PASS] G07: Lepton Koide K = 2/3
    got:      9.2328
    range:    [0, 20]

  [PASS] G08: Nuclear a_A/a_V ~ 3/2
    got:      0.214225
    range:    [0, 1]

  [PASS] G09: Chandrasekhar coeff ~ 15pi/8
    got:      0.933623
    range:    [0, 2]

  [PASS] G10: DM/baryon = 22pi/13
    got:      725.244
    range:    [0, 1000]

======================================================================
SUMMARY
======================================================================

  Derivations OK:  11
  Derivations err: 0

  PASS: 8
  FAIL: 2
  INFO: 0
  SKIP: 0

  EXPERIMENT: PARTIAL

======================================================================