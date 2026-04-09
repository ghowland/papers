Good next step.

I made these choices in this first-pass naming script:

- first token is always a single-word topic
- every key ends in `_v0`
- all keys are lowercase
- I used longer descriptive names where physics ambiguity exists
- I treated Tables 1–25 as the source set
- I did not encode Tables 26–27 here, because those are better handled later as:
  - verification/status metadata
  - level/taxonomy metadata
- for Q335 basis constants and geometric constants whose exact values were not fully written in your pasted tables, I kept stable names and stored a `ref` to the legacy platform source

Here is one Python script for the whole first-pass registry.

```python
#!/usr/bin/env python3
"""
DATA-5 FIRST-PASS V0 VALUE NAMING REGISTRY
Filename: data_5_v0_master_value_registry.py
===========================================

Purpose:
- Create one stable lowercase topic_varname_v0 key for each physics item
  in the corrected HOWL master tables.
- Keep values in plain Python so they can be exported to JSON later.
- Preserve exact Fractions where supplied.
- Use strings or legacy refs where the pasted tables gave only approximate
  decimal values or platform references.

Notes:
- Tables 1-25 are represented here.
- Tables 26-27 are intentionally excluded from this value registry because
  they are validation/taxonomy metadata rather than physics value entries.
- Q335 basis constants are declared with stable names and legacy refs because
  their full exact numerators were not included in the pasted table excerpt.
"""

from fractions import Fraction


VALUE_INDEX_V0 = {}


def add(key, value=None, unit="", source="", notes="", ref=""):
    """Register one v0 value entry and also bind it into globals()."""
    if key != key.lower():
        raise ValueError("Key must be lowercase: %s" % key)
    if not key.endswith("_v0"):
        raise ValueError("Key must end with _v0: %s" % key)
    if key in VALUE_INDEX_V0:
        raise ValueError("Duplicate key: %s" % key)

    topic = key.split("_")[0]
    term = "_".join(key.split("_")[1:-1])

    globals()[key] = value
    VALUE_INDEX_V0[key] = {
        "key": key,
        "topic": topic,
        "term": term,
        "version": 0,
        "value": value,
        "unit": unit,
        "source": source,
        "notes": notes,
        "ref": ref,
    }


# ================================================================
# TABLE 1: SM BETA COEFFICIENTS
# ================================================================

add(
    "beta_sm_u1_total_v0",
    Fraction(41, 10),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_u1_gauge_v0",
    Fraction(0, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_u1_fermion_three_gen_v0",
    Fraction(4, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_u1_higgs_v0",
    Fraction(1, 10),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)

add(
    "beta_sm_su2_total_v0",
    Fraction(-19, 6),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su2_gauge_v0",
    Fraction(-22, 3),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su2_fermion_three_gen_v0",
    Fraction(4, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su2_higgs_v0",
    Fraction(1, 6),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)

add(
    "beta_sm_su3_total_v0",
    Fraction(-7, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su3_gauge_v0",
    Fraction(-11, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su3_fermion_three_gen_v0",
    Fraction(4, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)
add(
    "beta_sm_su3_higgs_v0",
    Fraction(0, 1),
    unit="dimensionless",
    source="corrected master table 1 / phys24_lib.py",
)

# ================================================================
# TABLE 2: CABIBBO DOUBLET SHIFTS
# ================================================================

add(
    "beta_cabibbo_doublet_vectorlike_u1_shift_v0",
    Fraction(1, 15),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
)
add(
    "beta_cabibbo_doublet_vectorlike_su2_shift_v0",
    Fraction(1, 1),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
)
add(
    "beta_cabibbo_doublet_vectorlike_su3_shift_v0",
    Fraction(1, 3),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
)

add(
    "beta_modified_u1_total_v0",
    Fraction(25, 6),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
    notes="Corrected from erroneous 62/15 in earlier DATA-5 text.",
)
add(
    "beta_modified_su2_total_v0",
    Fraction(-13, 6),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
)
add(
    "beta_modified_su3_total_v0",
    Fraction(-20, 3),
    unit="dimensionless",
    source="corrected master table 2 / phys24_lib.py",
)

# ================================================================
# TABLE 3: GAP RATIOS
# ================================================================

add(
    "gap_pure_gauge_numerator_v0",
    Fraction(22, 3),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_pure_gauge_denominator_v0",
    Fraction(11, 3),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_pure_gauge_ratio_v0",
    Fraction(2, 1),
    unit="dimensionless",
    source="corrected master table 3",
)

add(
    "gap_sm_numerator_v0",
    Fraction(109, 15),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_denominator_v0",
    Fraction(23, 6),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_ratio_v0",
    Fraction(218, 115),
    unit="dimensionless",
    source="corrected master table 3",
)

add(
    "gap_sm_cabibbo_doublet_numerator_v0",
    Fraction(19, 3),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_cabibbo_doublet_denominator_v0",
    Fraction(9, 2),
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_cabibbo_doublet_ratio_v0",
    Fraction(38, 27),
    unit="dimensionless",
    source="corrected master table 3",
)

add(
    "gap_mssm_ratio_v0",
    Fraction(7, 5),
    unit="dimensionless",
    source="corrected master table 3",
    notes="Corrected from erroneous 5/7 in one alignment document.",
)

add(
    "gap_measured_ratio_v0",
    "1.3582",
    unit="dimensionless",
    source="corrected master table 3 / derived from couplings",
)
add(
    "gap_sm_distance_from_measured_v0",
    "0.5375",
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_miss_pct_v0",
    "39.6",
    unit="percent",
    source="corrected master table 3",
)
add(
    "gap_sm_cabibbo_doublet_distance_from_measured_v0",
    "0.0492",
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_sm_cabibbo_doublet_miss_pct_v0",
    "3.6",
    unit="percent",
    source="corrected master table 3",
)
add(
    "gap_mssm_distance_from_measured_v0",
    "0.0418",
    unit="dimensionless",
    source="corrected master table 3",
)
add(
    "gap_mssm_miss_pct_v0",
    "3.1",
    unit="percent",
    source="corrected master table 3",
)

# ================================================================
# TABLE 4: BETA DECOMPOSITION
# ================================================================

add(
    "beta_gap_source_gauge_numerator_delta_v0",
    Fraction(22, 3),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_gauge_numerator_pct_v0",
    "100.9",
    unit="percent",
    source="corrected master table 4",
)
add(
    "beta_gap_source_gauge_denominator_delta_v0",
    Fraction(11, 3),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_gauge_denominator_pct_v0",
    "95.7",
    unit="percent",
    source="corrected master table 4",
)

add(
    "beta_gap_source_fermion_per_generation_delta_numerator_v0",
    Fraction(0, 1),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_fermion_per_generation_numerator_pct_v0",
    "0.0",
    unit="percent",
    source="corrected master table 4",
)
add(
    "beta_gap_source_fermion_per_generation_delta_denominator_v0",
    Fraction(0, 1),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_fermion_per_generation_denominator_pct_v0",
    "0.0",
    unit="percent",
    source="corrected master table 4",
)

add(
    "beta_gap_source_higgs_numerator_delta_v0",
    Fraction(-1, 15),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_higgs_numerator_pct_v0",
    "-0.9",
    unit="percent",
    source="corrected master table 4",
)
add(
    "beta_gap_source_higgs_denominator_delta_v0",
    Fraction(1, 6),
    unit="dimensionless",
    source="corrected master table 4",
)
add(
    "beta_gap_source_higgs_denominator_pct_v0",
    "4.3",
    unit="percent",
    source="corrected master table 4",
)

# ================================================================
# TABLE 5: DOUBLE ACTION (CD EFFECT)
# ================================================================

add(
    "beta_cd_effect_numerator_sm_v0",
    Fraction(109, 15),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_numerator_delta_v0",
    Fraction(-14, 15),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_numerator_modified_v0",
    Fraction(19, 3),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_numerator_change_pct_v0",
    "-12.8",
    unit="percent",
    source="corrected master table 5",
)

add(
    "beta_cd_effect_denominator_sm_v0",
    Fraction(23, 6),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_denominator_delta_v0",
    Fraction(2, 3),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_denominator_modified_v0",
    Fraction(9, 2),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_denominator_change_pct_v0",
    "17.4",
    unit="percent",
    source="corrected master table 5",
)

add(
    "beta_cd_effect_gap_ratio_sm_v0",
    Fraction(218, 115),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_gap_ratio_modified_v0",
    Fraction(38, 27),
    unit="dimensionless",
    source="corrected master table 5",
)
add(
    "beta_cd_effect_gap_ratio_change_pct_v0",
    "-25.8",
    unit="percent",
    source="corrected master table 5",
)

# ================================================================
# TABLE 6: TWO-LOOP SM b_ij MATRIX
# ================================================================

sm_bij = {
    "u1_u1": Fraction(199, 50),
    "u1_su2": Fraction(27, 10),
    "u1_su3": Fraction(44, 5),
    "su2_u1": Fraction(9, 10),
    "su2_su2": Fraction(35, 6),
    "su2_su3": Fraction(12, 1),
    "su3_u1": Fraction(11, 10),
    "su3_su2": Fraction(9, 2),
    "su3_su3": Fraction(-26, 1),
}
for name, value in sm_bij.items():
    add(
        "beta_two_loop_sm_bij_%s_v0" % name,
        value,
        unit="dimensionless",
        source="corrected master table 6 / phys24_lib.py",
    )

# ================================================================
# TABLE 7: TWO-LOOP VL db_ij MATRIX
# ================================================================

vl_dbij = {
    "u1_u1": Fraction(7, 15),
    "u1_su2": Fraction(1, 15),
    "u1_su3": Fraction(16, 135),
    "su2_u1": Fraction(1, 30),
    "su2_su2": Fraction(15, 4),
    "su2_su3": Fraction(8, 3),
    "su3_u1": Fraction(1, 45),
    "su3_su2": Fraction(1, 1),
    "su3_su3": Fraction(40, 9),
}
for name, value in vl_dbij.items():
    add(
        "beta_two_loop_cabibbo_doublet_dbij_%s_v0" % name,
        value,
        unit="dimensionless",
        source="corrected master table 7 / phys24_lib.py",
        notes="su2_su2 = 15/4 is the corrected value, not 39/4.",
    )

# ================================================================
# TABLE 8: REPRESENTATIONS
# ================================================================

rep_rows = {
    "left_quark_doublet": {
        "su3_dim": 3,
        "su2_dim": 2,
        "y": Fraction(1, 6),
        "type": "chiral",
        "db1": Fraction(1, 30),
        "db2": Fraction(1, 1),
        "db3": Fraction(1, 3),
    },
    "right_up_singlet": {
        "su3_dim": 3,
        "su2_dim": 1,
        "y": Fraction(2, 3),
        "type": "chiral",
        "db1": Fraction(8, 15),
        "db2": Fraction(0, 1),
        "db3": Fraction(1, 3),
    },
    "right_down_singlet": {
        "su3_dim": 3,
        "su2_dim": 1,
        "y": Fraction(-1, 3),
        "type": "chiral",
        "db1": Fraction(2, 15),
        "db2": Fraction(0, 1),
        "db3": Fraction(1, 3),
    },
    "left_lepton_doublet": {
        "su3_dim": 1,
        "su2_dim": 2,
        "y": Fraction(-1, 2),
        "type": "chiral",
        "db1": Fraction(1, 6),
        "db2": Fraction(1, 3),
        "db3": Fraction(0, 1),
    },
    "right_electron_singlet": {
        "su3_dim": 1,
        "su2_dim": 1,
        "y": Fraction(-1, 1),
        "type": "chiral",
        "db1": Fraction(2, 5),
        "db2": Fraction(0, 1),
        "db3": Fraction(0, 1),
    },
    "cabibbo_doublet": {
        "su3_dim": 3,
        "su2_dim": 2,
        "y": Fraction(1, 6),
        "type": "vector_like",
        "db1": Fraction(1, 15),
        "db2": Fraction(1, 1),
        "db3": Fraction(1, 3),
    },
}
for rep_name, row in rep_rows.items():
    add(
        "rep_%s_su3_dim_v0" % rep_name,
        row["su3_dim"],
        unit="dimensionless",
        source="corrected master table 8",
    )
    add(
        "rep_%s_su2_dim_v0" % rep_name,
        row["su2_dim"],
        unit="dimensionless",
        source="corrected master table 8",
    )
    add(
        "rep_%s_y_v0" % rep_name,
        row["y"],
        unit="dimensionless",
        source="corrected master table 8",
    )
    add(
        "rep_%s_type_v0" % rep_name,
        row["type"],
        unit="classification",
        source="corrected master table 8",
    )
    add(
        "rep_%s_db1_v0" % rep_name,
        row["db1"],
        unit="dimensionless",
        source="corrected master table 8",
    )
    add(
        "rep_%s_db2_v0" % rep_name,
        row["db2"],
        unit="dimensionless",
        source="corrected master table 8",
    )
    add(
        "rep_%s_db3_v0" % rep_name,
        row["db3"],
        unit="dimensionless",
        source="corrected master table 8",
    )

add(
    "rep_sm_generation_democracy_db1_sum_v0",
    Fraction(4, 3),
    unit="dimensionless",
    source="corrected master table 8 note",
)
add(
    "rep_sm_generation_democracy_db2_sum_v0",
    Fraction(4, 3),
    unit="dimensionless",
    source="corrected master table 8 note",
)
add(
    "rep_sm_generation_democracy_db3_sum_v0",
    Fraction(4, 3),
    unit="dimensionless",
    source="corrected master table 8 note",
)

# ================================================================
# TABLE 9: GROUP THEORY CONSTANTS
# ================================================================

add(
    "group_c2_adj_su3_v0",
    3,
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_c2_adj_su2_v0",
    2,
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_c2_fundamental_su3_v0",
    Fraction(4, 3),
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_c2_fundamental_su2_v0",
    Fraction(3, 4),
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_s2_fundamental_v0",
    Fraction(1, 2),
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_k1_gut_normalization_v0",
    Fraction(3, 5),
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_gauge_coeff_yang_mills_v0",
    Fraction(-11, 3),
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_sm_generation_count_v0",
    3,
    unit="dimensionless",
    source="corrected master table 9",
)
add(
    "group_pure_gauge_gap_v0",
    Fraction(2, 1),
    unit="dimensionless",
    source="corrected master table 9",
)

# ================================================================
# TABLE 10: MEASURED COUPLINGS AT M_Z
# ================================================================

add(
    "coupling_alpha_em_inverse_v0",
    Fraction(137035999177, 10**9),
    unit="dimensionless",
    source="corrected master table 10 / CODATA 2022",
)
add(
    "coupling_sin2_theta_w_v0",
    Fraction(23122, 100000),
    unit="dimensionless",
    source="corrected master table 10 / LEP-SLD",
)
add(
    "coupling_alpha_s_mz_v0",
    Fraction(59, 500),
    unit="dimensionless",
    source="corrected master table 10 / PDG",
)
add(
    "coupling_alpha_1_inverse_gut_normalized_mz_v0",
    Fraction(15802580317094109, 250000000000000),
    unit="dimensionless",
    source="corrected master table 10 / derived",
)
add(
    "coupling_alpha_2_inverse_mz_v0",
    Fraction(1584273186485297, 50000000000000),
    unit="dimensionless",
    source="corrected master table 10 / derived",
)
add(
    "coupling_alpha_3_inverse_mz_v0",
    Fraction(500, 59),
    unit="dimensionless",
    source="corrected master table 10 / derived",
)
add(
    "coupling_measured_gap_ratio_v0",
    "1.3582",
    unit="dimensionless",
    source="corrected master table 10 / derived",
)

# ================================================================
# TABLE 11: MASSES
# ================================================================

mass_rows = {
    "electron": Fraction(51099895069, 10**11),
    "muon": Fraction(1056583755, 10**7),
    "tau": Fraction(177686, 100),
    "up_quark": Fraction(216, 100),
    "down_quark": Fraction(470, 100),
    "strange_quark": Fraction(935, 10),
    "charm_quark": Fraction(1273, 1),
    "bottom_quark": Fraction(4183, 1),
    "top_quark": Fraction(172570, 1),
    "z_boson": Fraction(911876, 10),
    "w_boson": Fraction(803692, 10),
    "higgs_boson": Fraction(125200, 1),
    "proton": Fraction(93827208943, 10**8),
    "neutron": Fraction(93956542194, 10**8),
}
for name, value in mass_rows.items():
    notes = ""
    if name == "w_boson":
        notes = "Corrected master value: 80369.2 MeV, not 80379 MeV."
    add(
        "mass_%s_v0" % name,
        value,
        unit="MeV",
        source="corrected master table 11 / phys24_lib.py",
        notes=notes,
    )

# ================================================================
# TABLE 12: GEOMETRIC CONSTANTS
# ================================================================

add(
    "geom_r2_v0",
    None,
    unit="dimensionless",
    source="corrected master table 12 / phys24_lib.py",
    ref="phys24_lib.R2",
    notes="Exact platform value; identity R2 = pi/4.",
)
add(
    "geom_r4_v0",
    None,
    unit="dimensionless",
    source="corrected master table 12 / phys24_lib.py",
    ref="phys24_lib.R4",
    notes="Exact platform value; identity R4 = pi^2/32.",
)
add(
    "geom_pi_v0",
    None,
    unit="dimensionless",
    source="corrected master table 12 / phys24_lib.py",
    ref="phys24_lib.pi_f",
)
add(
    "geom_two_pi_v0",
    None,
    unit="dimensionless",
    source="corrected master table 12",
    notes="Identity 8*R2 = 2*pi.",
    ref="8*phys24_lib.R2",
)
add(
    "geom_four_pi_squared_v0",
    None,
    unit="dimensionless",
    source="corrected master table 12",
    notes="Identity 64*R2^2 = 4*pi^2.",
    ref="64*(phys24_lib.R2**2)",
)

# ================================================================
# TABLE 13: DERIVATION RESULTS
# ================================================================

add(
    "result_alpha_s_one_loop_cabibbo_doublet_v0",
    "0.10769",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Measured 0.1180; miss 8.74%.",
)
add(
    "result_alpha_s_two_loop_sm_bij_v0",
    "0.11753",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Measured 0.1180; miss 0.397%.",
)
add(
    "result_alpha_s_two_loop_full_bij_v0",
    "0.11838",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Measured 0.1180; miss 0.325%.",
)
add(
    "result_sin2_theta_w_one_loop_cabibbo_doublet_v0",
    "0.22845",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Measured 0.23122; miss 1.199%.",
)
add(
    "result_tau_mass_koide_two_thirds_v0",
    "1776.969",
    unit="MeV",
    source="corrected master table 13",
    notes="Measured 1776.86 MeV; miss 0.00614%.",
)
add(
    "result_m_gut_one_loop_cabibbo_doublet_log10_gev_v0",
    "15.54",
    unit="log10(GeV)",
    source="corrected master table 13",
)
add(
    "result_l_gut_one_loop_cabibbo_doublet_v0",
    "4.978",
    unit="dimensionless",
    source="corrected master table 13",
)
add(
    "result_dm_to_baryon_ratio_beta_integer_v0",
    "5.3165",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Measured 5.3204; miss 0.0725%.",
)
add(
    "result_omega_dm_beta_integer_v0",
    "0.2045",
    unit="dimensionless",
    source="corrected master table 13",
    notes="Compared to Planck 2018 value 0.2607.",
)
add(
    "result_gps_correction_general_relativity_v0",
    "38.5",
    unit="microseconds/day",
    source="corrected master table 13",
    notes="Compared to about 38.6 microseconds/day.",
)
add(
    "result_mond_a0_c_h0_over_eight_r2_v0",
    "1.1e-10",
    unit="m/s^2",
    source="corrected master table 13",
    notes="Compared to about 1.2e-10 m/s^2; miss about 8%.",
)

# ================================================================
# TABLE 14: KOIDE DATA
# ================================================================

add(
    "koide_charged_leptons_k_v0",
    Fraction(6666605115, 10**10),
    unit="dimensionless",
    source="corrected master table 14 / phys24_lib.py",
)
add(
    "koide_charged_leptons_a2_v0",
    Fraction(19999630688, 10**10),
    unit="dimensionless",
    source="corrected master table 14 / phys24_lib.py",
    notes="Near but not exactly 2.",
)
add(
    "koide_charged_leptons_a2_minus_two_v0",
    "-3.7e-5",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_charged_leptons_status_v0",
    "near_k_two_thirds",
    unit="classification",
    source="corrected master table 14",
)

add(
    "koide_down_quarks_k_v0",
    "0.73129",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_down_quarks_a2_v0",
    "2.388",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_down_quarks_a2_minus_two_v0",
    "0.388",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_down_quarks_status_v0",
    "far_from_k_two_thirds",
    unit="classification",
    source="corrected master table 14",
)

add(
    "koide_up_quarks_k_v0",
    "0.84879",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_up_quarks_a2_v0",
    "3.093",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_up_quarks_a2_minus_two_v0",
    "1.093",
    unit="dimensionless",
    source="corrected master table 14",
)
add(
    "koide_up_quarks_status_v0",
    "far_from_k_two_thirds",
    unit="classification",
    source="corrected master table 14",
)

# ================================================================
# TABLE 15: COSMOLOGICAL PARAMETERS FROM BETA INTEGERS
# ================================================================

add(
    "cosmo_dm_to_baryon_ratio_prefactor_v0",
    Fraction(22, 13),
    unit="dimensionless",
    source="corrected master table 15",
    notes="Formula prefactor in (22/13)*pi.",
)
add(
    "cosmo_dm_to_baryon_ratio_predicted_v0",
    "5.3165",
    unit="dimensionless",
    source="corrected master table 15",
)
add(
    "cosmo_dm_to_baryon_ratio_planck2018_v0",
    "5.3204",
    unit="dimensionless",
    source="corrected master table 15",
)
add(
    "cosmo_dm_to_baryon_ratio_miss_pct_v0",
    "0.0725",
    unit="percent",
    source="corrected master table 15",
    notes="Corrected from 0.073% rounded statement in one chunk.",
)

add(
    "cosmo_omega_dm_r2_prefactor_v0",
    Fraction(44, 169),
    unit="dimensionless",
    source="corrected master table 15",
    notes="Pure rational prefactor in (44/169)*R2.",
)
add(
    "cosmo_omega_dm_predicted_v0",
    "0.2045",
    unit="dimensionless",
    source="corrected master table 15",
)
add(
    "cosmo_omega_dm_planck2018_v0",
    "0.2607",
    unit="dimensionless",
    source="corrected master table 15",
)

# ================================================================
# TABLE 16: INTEGER POOL
# ================================================================

add(
    "integer_yang_mills_eleven_v0",
    11,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_b2_modified_numerator_abs_v0",
    13,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_b2_sm_numerator_abs_v0",
    19,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_b3_modified_times_three_abs_v0",
    20,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_two_times_yang_mills_v0",
    22,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_four_times_yang_mills_v0",
    44,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_b2_modified_numerator_square_v0",
    169,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_cabibbo_doublet_gap_numerator_v0",
    38,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_cabibbo_doublet_gap_denominator_v0",
    27,
    unit="dimensionless",
    source="corrected master table 16",
)
add(
    "integer_sm_gap_numerator_v0",
    218,
    unit="dimensionless",
    source="corrected master table 16",
)

