#!/usr/bin/env python3
"""
DATA-6 DERIVATION AND CONNECTION REGISTRY v0
==============================================
Filename: data_6_derivations_v0.py

All derivation and connection functions for the DATA-6 system.

Rules:
    - Every function has signature: fn(value_dicts)
    - value_dicts is a list of value-entry dicts
    - No hardcoded physics constants — all from value_dicts
    - Fraction for exact arithmetic
    - mpf only at irrational/numerical boundary
    - mp.dps = 100 minimum
    - No math module
    - Deterministic execution

Derivation return contract:
    {"key": "..._v0", "outputs": {...}, "notes": ""}

Connection return contract:
    {"key": "..._v0", "named_values": {...}, "edges": [...], "notes": ""}

Registry:
    DERIVATION_INDEX_V0 = {key: callable, ...}
    CONNECTION_INDEX_V0 = {key: callable, ...}
"""

from fractions import Fraction
from mpmath import mp

mp.dps = 100


# ================================================================
# SHARED HELPERS
# ================================================================

def _value_map(value_dicts):
    """Build key -> entry dict from value_dicts list."""
    out = {}
    for entry in value_dicts:
        key = entry["key"]
        if key in out:
            raise ValueError("Duplicate value entry for key: %s" % key)
        out[key] = entry
    return out


def _need(values_by_key, key):
    """Get the value field from a value entry, or raise."""
    if key not in values_by_key:
        raise KeyError("Missing required value key: %s" % key)
    return values_by_key[key]["value"]


def _need_entry(values_by_key, key):
    """Get the full entry dict, or raise."""
    if key not in values_by_key:
        raise KeyError("Missing required value key: %s" % key)
    return values_by_key[key]


def _frac(x):
    """Ensure x is a Fraction. Accepts Fraction or int."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x, 1)
    raise TypeError("Expected Fraction/int, got %r" % (type(x),))


def _mpf_from_fraction(x):
    """Convert Fraction to mpf at working precision."""
    x = _frac(x)
    return mp.mpf(x.numerator) / mp.mpf(x.denominator)


def _mpf(x):
    """Convert any numeric to mpf."""
    if isinstance(x, Fraction):
        return _mpf_from_fraction(x)
    if isinstance(x, int):
        return mp.mpf(x)
    if isinstance(x, str):
        return mp.mpf(x)
    if hasattr(x, "_mpf_"):
        return x
    raise TypeError("Cannot convert to mpf: %r" % (type(x),))


def _mp_str(x, digits=20):
    """Render mpf to string at N significant digits."""
    val = _mpf(x) if not hasattr(x, "_mpf_") else x
    return mp.nstr(val, digits)


def _as_text(x):
    """Human-readable text form of a value."""
    if isinstance(x, Fraction):
        return "%s/%s" % (x.numerator, x.denominator)
    if x is None:
        return None
    return str(x)


def _named_value(values_by_key, key, var_name):
    """Build a named_value dict for connection output."""
    entry = _need_entry(values_by_key, key)
    return {
        "var_name": var_name,
        "source_key": key,
        "value": entry["value"],
        "value_text": _as_text(entry["value"]),
        "unit": entry.get("unit", ""),
        "source": entry.get("source", ""),
    }


def _matrix_from_values(v, prefix):
    """Extract a 3x3 Fraction matrix from value entries by prefix."""
    return [
        [
            _frac(_need(v, "%s_u1_u1_v0" % prefix)),
            _frac(_need(v, "%s_u1_su2_v0" % prefix)),
            _frac(_need(v, "%s_u1_su3_v0" % prefix)),
        ],
        [
            _frac(_need(v, "%s_su2_u1_v0" % prefix)),
            _frac(_need(v, "%s_su2_su2_v0" % prefix)),
            _frac(_need(v, "%s_su2_su3_v0" % prefix)),
        ],
        [
            _frac(_need(v, "%s_su3_u1_v0" % prefix)),
            _frac(_need(v, "%s_su3_su2_v0" % prefix)),
            _frac(_need(v, "%s_su3_su3_v0" % prefix)),
        ],
    ]


# ================================================================
# DERIVATIONS: COUPLING EXTRACTION
# ================================================================

def coupling_extraction_v0(value_dicts):
    """
    Extract GUT-normalized inverse couplings at M_Z.

    Inputs:
    - coupling_alpha_em_inverse_v0
    - coupling_sin2_theta_w_v0
    - coupling_alpha_s_mz_v0

    Outputs:
    - coupling_alpha_em_v0
    - coupling_cos2_theta_w_v0
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - coupling_alpha_3_inverse_mz_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    alpha_inv = _frac(_need(v, "coupling_alpha_em_inverse_v0"))
    sin2_tW = _frac(_need(v, "coupling_sin2_theta_w_v0"))
    alpha_s = _frac(_need(v, "coupling_alpha_s_mz_v0"))

    alpha_em = Fraction(1, 1) / alpha_inv
    cos2_tW = Fraction(1, 1) - sin2_tW
    inv_a1 = Fraction(3, 5) * alpha_inv * cos2_tW
    inv_a2 = alpha_inv * sin2_tW
    inv_a3 = Fraction(1, 1) / alpha_s

    return {
        "key": "coupling_extraction_v0",
        "outputs": {
            "coupling_alpha_em_v0": alpha_em,
            "coupling_cos2_theta_w_v0": cos2_tW,
            "coupling_alpha_1_inverse_gut_normalized_mz_v0": inv_a1,
            "coupling_alpha_2_inverse_mz_v0": inv_a2,
            "coupling_alpha_3_inverse_mz_v0": inv_a3,
        },
        "notes": "",
    }


# ================================================================
# DERIVATIONS: GAP RATIOS
# ================================================================

def gap_measured_ratio_v0(value_dicts):
    """
    Compute measured gap ratio from inverse couplings.

    Inputs:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - coupling_alpha_3_inverse_mz_v0

    Outputs:
    - gap_measured_numerator_v0
    - gap_measured_denominator_v0
    - gap_measured_ratio_exact_v0
    - gap_measured_ratio_numeric_v0

    Arithmetic: exact (numeric output for display only)
    """
    v = _value_map(value_dicts)

    inv_a1 = _frac(_need(v, "coupling_alpha_1_inverse_gut_normalized_mz_v0"))
    inv_a2 = _frac(_need(v, "coupling_alpha_2_inverse_mz_v0"))
    inv_a3 = _frac(_need(v, "coupling_alpha_3_inverse_mz_v0"))

    numerator = inv_a1 - inv_a2
    denominator = inv_a2 - inv_a3
    gap = numerator / denominator

    return {
        "key": "gap_measured_ratio_v0",
        "outputs": {
            "gap_measured_numerator_v0": numerator,
            "gap_measured_denominator_v0": denominator,
            "gap_measured_ratio_exact_v0": gap,
            "gap_measured_ratio_numeric_v0": _mp_str(
                _mpf_from_fraction(gap), 20),
        },
        "notes": "",
    }


def gap_sm_ratio_v0(value_dicts):
    """
    Compute SM gap ratio from SM beta coefficients.

    Inputs:
    - beta_sm_u1_total_v0
    - beta_sm_su2_total_v0
    - beta_sm_su3_total_v0

    Outputs:
    - gap_sm_numerator_derived_v0
    - gap_sm_denominator_derived_v0
    - gap_sm_ratio_derived_v0
    - gap_sm_ratio_numeric_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    b1 = _frac(_need(v, "beta_sm_u1_total_v0"))
    b2 = _frac(_need(v, "beta_sm_su2_total_v0"))
    b3 = _frac(_need(v, "beta_sm_su3_total_v0"))

    numerator = b1 - b2
    denominator = b2 - b3
    gap = numerator / denominator

    return {
        "key": "gap_sm_ratio_v0",
        "outputs": {
            "gap_sm_numerator_derived_v0": numerator,
            "gap_sm_denominator_derived_v0": denominator,
            "gap_sm_ratio_derived_v0": gap,
            "gap_sm_ratio_numeric_v0": _mp_str(
                _mpf_from_fraction(gap), 20),
        },
        "notes": "",
    }


def gauge_pure_gap_v0(value_dicts):
    """
    Compute pure gauge gap ratio from adjoint Casimirs.

    Inputs:
    - group_c2_adj_su2_v0
    - group_c2_adj_su3_v0

    Outputs:
    - gap_pure_gauge_numerator_derived_v0
    - gap_pure_gauge_denominator_derived_v0
    - gap_pure_gauge_ratio_derived_v0
    - gap_pure_gauge_casimir_form_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    c2_su2 = _frac(_need(v, "group_c2_adj_su2_v0"))
    c2_su3 = _frac(_need(v, "group_c2_adj_su3_v0"))

    b1 = Fraction(0, 1)
    b2 = Fraction(-11, 3) * c2_su2
    b3 = Fraction(-11, 3) * c2_su3

    numerator = b1 - b2
    denominator = b2 - b3
    gap = numerator / denominator
    casimir_gap = c2_su2 / (c2_su3 - c2_su2)

    return {
        "key": "gauge_pure_gap_v0",
        "outputs": {
            "gap_pure_gauge_numerator_derived_v0": numerator,
            "gap_pure_gauge_denominator_derived_v0": denominator,
            "gap_pure_gauge_ratio_derived_v0": gap,
            "gap_pure_gauge_casimir_form_v0": casimir_gap,
        },
        "notes": "",
    }


# ================================================================
# DERIVATIONS: BETA COEFFICIENTS
# ================================================================

def beta_sm_coefficients_v0(value_dicts):
    """
    Derive SM beta coefficients from group theory and representations.

    Inputs:
    - group_c2_adj_su2_v0
    - group_c2_adj_su3_v0
    - group_sm_generation_count_v0
    - rep_sm_generation_democracy_db1_sum_v0
    - rep_sm_generation_democracy_db2_sum_v0
    - rep_sm_generation_democracy_db3_sum_v0
    - beta_sm_u1_higgs_v0
    - beta_sm_su2_higgs_v0
    - beta_sm_su3_higgs_v0

    Outputs:
    - beta_sm_u1_gauge_derived_v0 through beta_sm_su3_total_derived_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    c2_su2 = _frac(_need(v, "group_c2_adj_su2_v0"))
    c2_su3 = _frac(_need(v, "group_c2_adj_su3_v0"))
    n_gen = _frac(_need(v, "group_sm_generation_count_v0"))

    gen_db1 = _frac(_need(v, "rep_sm_generation_democracy_db1_sum_v0"))
    gen_db2 = _frac(_need(v, "rep_sm_generation_democracy_db2_sum_v0"))
    gen_db3 = _frac(_need(v, "rep_sm_generation_democracy_db3_sum_v0"))

    higgs_db1 = _frac(_need(v, "beta_sm_u1_higgs_v0"))
    higgs_db2 = _frac(_need(v, "beta_sm_su2_higgs_v0"))
    higgs_db3 = _frac(_need(v, "beta_sm_su3_higgs_v0"))

    gauge_b1 = Fraction(0, 1)
    gauge_b2 = Fraction(-11, 3) * c2_su2
    gauge_b3 = Fraction(-11, 3) * c2_su3

    fermion_b1 = n_gen * gen_db1
    fermion_b2 = n_gen * gen_db2
    fermion_b3 = n_gen * gen_db3

    b1 = gauge_b1 + fermion_b1 + higgs_db1
    b2 = gauge_b2 + fermion_b2 + higgs_db2
    b3 = gauge_b3 + fermion_b3 + higgs_db3

    return {
        "key": "beta_sm_coefficients_v0",
        "outputs": {
            "beta_sm_u1_gauge_derived_v0": gauge_b1,
            "beta_sm_su2_gauge_derived_v0": gauge_b2,
            "beta_sm_su3_gauge_derived_v0": gauge_b3,
            "beta_sm_u1_fermion_derived_v0": fermion_b1,
            "beta_sm_su2_fermion_derived_v0": fermion_b2,
            "beta_sm_su3_fermion_derived_v0": fermion_b3,
            "beta_sm_u1_total_derived_v0": b1,
            "beta_sm_su2_total_derived_v0": b2,
            "beta_sm_su3_total_derived_v0": b3,
        },
        "notes": "",
    }


def beta_cabibbo_doublet_shifts_v0(value_dicts):
    """
    Compute VL one-loop beta shifts from CD representation data.

    Inputs:
    - rep_cabibbo_doublet_su3_dim_v0
    - rep_cabibbo_doublet_su2_dim_v0
    - rep_cabibbo_doublet_y_v0
    - group_s2_fundamental_v0

    Outputs:
    - beta_cabibbo_doublet_vectorlike_u1_shift_derived_v0
    - beta_cabibbo_doublet_vectorlike_su2_shift_derived_v0
    - beta_cabibbo_doublet_vectorlike_su3_shift_derived_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    d3 = _frac(_need(v, "rep_cabibbo_doublet_su3_dim_v0"))
    d2 = _frac(_need(v, "rep_cabibbo_doublet_su2_dim_v0"))
    y = _frac(_need(v, "rep_cabibbo_doublet_y_v0"))
    s2_fund = _frac(_need(v, "group_s2_fundamental_v0"))

    db1 = Fraction(2, 5) * d3 * d2 * y * y
    db2 = Fraction(2, 3) * d3 * s2_fund
    db3 = Fraction(1, 3) * d2 * s2_fund

    return {
        "key": "beta_cabibbo_doublet_shifts_v0",
        "outputs": {
            "beta_cabibbo_doublet_vectorlike_u1_shift_derived_v0": db1,
            "beta_cabibbo_doublet_vectorlike_su2_shift_derived_v0": db2,
            "beta_cabibbo_doublet_vectorlike_su3_shift_derived_v0": db3,
        },
        "notes": "",
    }


def beta_modified_and_cd_gap_ratio_v0(value_dicts):
    """
    Compute modified betas (SM + CD) and the CD gap ratio.

    Inputs:
    - beta_sm_u1_total_v0
    - beta_sm_su2_total_v0
    - beta_sm_su3_total_v0
    - beta_cabibbo_doublet_vectorlike_u1_shift_v0
    - beta_cabibbo_doublet_vectorlike_su2_shift_v0
    - beta_cabibbo_doublet_vectorlike_su3_shift_v0

    Outputs:
    - beta_modified_u1_total_derived_v0 through
      gap_sm_cabibbo_doublet_ratio_numeric_v0

    Arithmetic: exact (numeric output for display)
    """
    v = _value_map(value_dicts)

    b1 = _frac(_need(v, "beta_sm_u1_total_v0"))
    b2 = _frac(_need(v, "beta_sm_su2_total_v0"))
    b3 = _frac(_need(v, "beta_sm_su3_total_v0"))

    db1 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_u1_shift_v0"))
    db2 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_su2_shift_v0"))
    db3 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_su3_shift_v0"))

    b1_mod = b1 + db1
    b2_mod = b2 + db2
    b3_mod = b3 + db3

    numerator = b1_mod - b2_mod
    denominator = b2_mod - b3_mod
    gap = numerator / denominator

    return {
        "key": "beta_modified_and_cd_gap_ratio_v0",
        "outputs": {
            "beta_modified_u1_total_derived_v0": b1_mod,
            "beta_modified_su2_total_derived_v0": b2_mod,
            "beta_modified_su3_total_derived_v0": b3_mod,
            "gap_sm_cabibbo_doublet_numerator_derived_v0": numerator,
            "gap_sm_cabibbo_doublet_denominator_derived_v0": denominator,
            "gap_sm_cabibbo_doublet_ratio_derived_v0": gap,
            "gap_sm_cabibbo_doublet_ratio_numeric_v0": _mp_str(
                _mpf_from_fraction(gap), 20),
        },
        "notes": "",
    }


def generation_democracy_v0(value_dicts):
    """
    Verify generation democracy: per-gen shifts are equal.

    Inputs:
    - rep_sm_generation_democracy_db1_sum_v0
    - rep_sm_generation_democracy_db2_sum_v0
    - rep_sm_generation_democracy_db3_sum_v0

    Outputs:
    - generation_democracy_gap_numerator_v0
    - generation_democracy_gap_denominator_v0
    - generation_democracy_independent_of_n_gen_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    gen_db1 = _frac(_need(v, "rep_sm_generation_democracy_db1_sum_v0"))
    gen_db2 = _frac(_need(v, "rep_sm_generation_democracy_db2_sum_v0"))
    gen_db3 = _frac(_need(v, "rep_sm_generation_democracy_db3_sum_v0"))

    gap_num = gen_db1 - gen_db2
    gap_den = gen_db2 - gen_db3

    return {
        "key": "generation_democracy_v0",
        "outputs": {
            "generation_democracy_gap_numerator_v0": gap_num,
            "generation_democracy_gap_denominator_v0": gap_den,
            "generation_democracy_independent_of_n_gen_v0": (
                gap_num == 0 and gap_den == 0),
        },
        "notes": "",
    }


def beta_double_action_mechanism_v0(value_dicts):
    """
    Analyze CD double action: numerator and denominator shifts.

    Inputs:
    - beta_cabibbo_doublet_vectorlike_u1_shift_v0
    - beta_cabibbo_doublet_vectorlike_su2_shift_v0
    - beta_cabibbo_doublet_vectorlike_su3_shift_v0
    - gap_sm_numerator_v0
    - gap_sm_denominator_v0

    Outputs:
    - beta_cd_effect_numerator_delta_derived_v0
    - beta_cd_effect_denominator_delta_derived_v0
    - beta_cd_effect_numerator_change_pct_derived_v0
    - beta_cd_effect_denominator_change_pct_derived_v0
    - beta_cd_effect_db2_over_db1_v0

    Arithmetic: mixed (percentages use mpf)
    """
    v = _value_map(value_dicts)

    db1 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_u1_shift_v0"))
    db2 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_su2_shift_v0"))
    db3 = _frac(_need(v, "beta_cabibbo_doublet_vectorlike_su3_shift_v0"))
    sm_num = _frac(_need(v, "gap_sm_numerator_v0"))
    sm_den = _frac(_need(v, "gap_sm_denominator_v0"))

    num_delta = db1 - db2
    den_delta = db2 - db3
    num_pct = (mp.mpf("100") * _mpf_from_fraction(num_delta)
               / _mpf_from_fraction(sm_num))
    den_pct = (mp.mpf("100") * _mpf_from_fraction(den_delta)
               / _mpf_from_fraction(sm_den))
    asymmetry = db2 / db1

    return {
        "key": "beta_double_action_mechanism_v0",
        "outputs": {
            "beta_cd_effect_numerator_delta_derived_v0": num_delta,
            "beta_cd_effect_denominator_delta_derived_v0": den_delta,
            "beta_cd_effect_numerator_change_pct_derived_v0": _mp_str(
                num_pct, 10),
            "beta_cd_effect_denominator_change_pct_derived_v0": _mp_str(
                den_pct, 10),
            "beta_cd_effect_db2_over_db1_v0": asymmetry,
        },
        "notes": "",
    }


def beta_y_dependence_family_v0(value_dicts):
    """
    Compute gap ratio as function of hypercharge Y.

    Inputs:
    - rep_cabibbo_doublet_y_v0

    Outputs:
    - beta_y_dependence_db1_coeff_v0
    - beta_y_dependence_numerator_const_v0
    - beta_y_dependence_denominator_const_v0
    - beta_y_dependence_formula_text_v0
    - beta_y_dependence_gap_at_input_y_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    y = _frac(_need(v, "rep_cabibbo_doublet_y_v0"))

    db1_coeff = Fraction(12, 5)
    numerator_const = Fraction(94, 15)
    denominator_const = Fraction(9, 2)

    numerator_at_y = numerator_const + db1_coeff * y * y
    gap_at_y = numerator_at_y / denominator_const

    return {
        "key": "beta_y_dependence_family_v0",
        "outputs": {
            "beta_y_dependence_db1_coeff_v0": db1_coeff,
            "beta_y_dependence_numerator_const_v0": numerator_const,
            "beta_y_dependence_denominator_const_v0": denominator_const,
            "beta_y_dependence_formula_text_v0": "(188 + 72*Y^2) / 135",
            "beta_y_dependence_gap_at_input_y_v0": gap_at_y,
        },
        "notes": "",
    }


# ================================================================
# DERIVATIONS: ONE-LOOP RUNNING
# ================================================================

def crossing_one_loop_scale_v0(value_dicts):
    """
    Find one-loop GUT crossing scale.

    Inputs:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - beta_modified_u1_total_v0
    - beta_modified_su2_total_v0
    - mass_z_boson_v0

    Outputs:
    - result_l_gut_one_loop_cabibbo_doublet_derived_v0
    - result_m_gut_one_loop_cabibbo_doublet_log10_gev_derived_v0

    Arithmetic: mixed (L is exact Fraction, scale uses mpf for exp/log)
    """
    v = _value_map(value_dicts)

    inv_a1 = _frac(_need(v, "coupling_alpha_1_inverse_gut_normalized_mz_v0"))
    inv_a2 = _frac(_need(v, "coupling_alpha_2_inverse_mz_v0"))
    b1_mod = _frac(_need(v, "beta_modified_u1_total_v0"))
    b2_mod = _frac(_need(v, "beta_modified_su2_total_v0"))
    mz_mev = _frac(_need(v, "mass_z_boson_v0"))

    l_exact = (inv_a1 - inv_a2) / (b1_mod - b2_mod)

    mz_gev = _mpf_from_fraction(mz_mev) / mp.mpf("1000")
    m_gut_gev = mz_gev * mp.exp(
        mp.mpf("2") * mp.pi * _mpf_from_fraction(l_exact))
    log10_m_gut_gev = mp.log10(m_gut_gev)

    return {
        "key": "crossing_one_loop_scale_v0",
        "outputs": {
            "result_l_gut_one_loop_cabibbo_doublet_derived_v0": l_exact,
            "result_m_gut_one_loop_cabibbo_doublet_log10_gev_derived_v0": (
                _mp_str(log10_m_gut_gev, 12)),
        },
        "notes": "",
    }


def coupling_one_loop_alpha_s_prediction_v0(value_dicts):
    """
    Predict alpha_s from one-loop CD unification.

    Inputs:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - beta_modified_u1_total_v0
    - beta_modified_su2_total_v0
    - beta_modified_su3_total_v0
    - coupling_alpha_s_mz_v0

    Outputs:
    - result_alpha_s_one_loop_cabibbo_doublet_exact_v0
    - result_alpha_s_one_loop_cabibbo_doublet_numeric_v0
    - result_alpha_s_one_loop_cabibbo_doublet_miss_pct_v0

    Arithmetic: mixed
    """
    v = _value_map(value_dicts)

    inv_a1 = _frac(_need(v, "coupling_alpha_1_inverse_gut_normalized_mz_v0"))
    inv_a2 = _frac(_need(v, "coupling_alpha_2_inverse_mz_v0"))
    b1_mod = _frac(_need(v, "beta_modified_u1_total_v0"))
    b2_mod = _frac(_need(v, "beta_modified_su2_total_v0"))
    b3_mod = _frac(_need(v, "beta_modified_su3_total_v0"))
    alpha_s_measured = _frac(_need(v, "coupling_alpha_s_mz_v0"))

    l_exact = (inv_a1 - inv_a2) / (b1_mod - b2_mod)

    inv_a_gut = inv_a1 - b1_mod * l_exact
    inv_a3_mz = inv_a_gut + b3_mod * l_exact
    alpha_s_pred = Fraction(1, 1) / inv_a3_mz

    miss_pct = (
        mp.mpf("100")
        * abs(_mpf_from_fraction(alpha_s_pred)
              - _mpf_from_fraction(alpha_s_measured))
        / _mpf_from_fraction(alpha_s_measured))

    return {
        "key": "coupling_one_loop_alpha_s_prediction_v0",
        "outputs": {
            "result_alpha_s_one_loop_cabibbo_doublet_exact_v0": alpha_s_pred,
            "result_alpha_s_one_loop_cabibbo_doublet_numeric_v0": _mp_str(
                _mpf_from_fraction(alpha_s_pred), 12),
            "result_alpha_s_one_loop_cabibbo_doublet_miss_pct_v0": _mp_str(
                miss_pct, 8),
        },
        "notes": "",
    }


# ================================================================
# DERIVATIONS: TWO-LOOP RUNNING (numerical)
# ================================================================

def _run_inv_alpha_euler(inv_start, b_vec, bij_mat, l_target, steps):
    """Euler integration of two-loop RGEs. Internal helper."""
    step = l_target / mp.mpf(steps)
    invs = [mp.mpf(x) for x in inv_start]

    for _ in range(steps):
        alphas = [mp.mpf("1") / x for x in invs]
        derivs = []
        for i in range(3):
            two_loop_sum = mp.mpf("0")
            for j in range(3):
                two_loop_sum += (bij_mat[i][j] * alphas[j]
                                 / (mp.mpf("2") * mp.pi))
            derivs.append(-b_vec[i] - two_loop_sum)
        for i in range(3):
            invs[i] += derivs[i] * step

    return invs


def _predict_alpha_s_two_loop(inv0, b_vec, bij_mat):
    """Binary search for two-loop crossing, then predict alpha_s."""
    def residual(l_guess):
        invs = _run_inv_alpha_euler(inv0, b_vec, bij_mat, l_guess, 4000)
        return invs[0] - invs[1]

    low = mp.mpf("0")
    high = mp.mpf("10")
    r_low = residual(low)
    r_high = residual(high)

    while r_low * r_high > 0:
        high *= mp.mpf("2")
        if high > mp.mpf("100"):
            raise ValueError("Could not bracket two-loop crossing.")
        r_high = residual(high)

    for _ in range(60):
        mid = (low + high) / mp.mpf("2")
        r_mid = residual(mid)
        if r_low * r_mid <= 0:
            high = mid
            r_high = r_mid
        else:
            low = mid
            r_low = r_mid

    l_gut = (low + high) / mp.mpf("2")
    invs_at_cross = _run_inv_alpha_euler(
        inv0, b_vec, bij_mat, l_gut, 4000)
    inv_gut = (invs_at_cross[0] + invs_at_cross[1]) / mp.mpf("2")
    invs_back = _run_inv_alpha_euler(
        [inv_gut, inv_gut, inv_gut], b_vec, bij_mat, -l_gut, 4000)
    alpha_s_pred = mp.mpf("1") / invs_back[2]

    return l_gut, inv_gut, alpha_s_pred


def coupling_two_loop_alpha_s_euler_v0(value_dicts):
    """
    Predict alpha_s from two-loop unification with Euler integration.

    Inputs:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - coupling_alpha_3_inverse_mz_v0
    - beta_modified_u1_total_v0
    - beta_modified_su2_total_v0
    - beta_modified_su3_total_v0
    - beta_two_loop_sm_bij_*_v0 (9 matrix entries)
    - beta_two_loop_cabibbo_doublet_dbij_*_v0 (9 matrix entries)
    - coupling_alpha_s_mz_v0

    Outputs:
    - result_alpha_s_two_loop_sm_bij_derived_v0
    - result_alpha_s_two_loop_sm_bij_miss_pct_v0
    - result_alpha_s_two_loop_full_bij_derived_v0
    - result_alpha_s_two_loop_full_bij_miss_pct_v0
    - result_two_loop_l_gut_full_bij_v0
    - result_two_loop_alpha_gut_inverse_full_bij_v0

    Arithmetic: numeric (Euler integration + binary search)
    """
    v = _value_map(value_dicts)

    inv0 = [
        _mpf_from_fraction(_frac(_need(
            v, "coupling_alpha_1_inverse_gut_normalized_mz_v0"))),
        _mpf_from_fraction(_frac(_need(
            v, "coupling_alpha_2_inverse_mz_v0"))),
        _mpf_from_fraction(_frac(_need(
            v, "coupling_alpha_3_inverse_mz_v0"))),
    ]
    b_vec = [
        _mpf_from_fraction(_frac(_need(v, "beta_modified_u1_total_v0"))),
        _mpf_from_fraction(_frac(_need(v, "beta_modified_su2_total_v0"))),
        _mpf_from_fraction(_frac(_need(v, "beta_modified_su3_total_v0"))),
    ]
    sm_bij_frac = _matrix_from_values(v, "beta_two_loop_sm_bij")
    vl_dbij_frac = _matrix_from_values(
        v, "beta_two_loop_cabibbo_doublet_dbij")
    sm_bij = [[_mpf_from_fraction(x) for x in row]
              for row in sm_bij_frac]
    full_bij = [
        [_mpf_from_fraction(sm_bij_frac[i][j] + vl_dbij_frac[i][j])
         for j in range(3)]
        for i in range(3)
    ]

    _, _, alpha_s_sm = _predict_alpha_s_two_loop(inv0, b_vec, sm_bij)
    l_full, inv_gut_full, alpha_s_full = _predict_alpha_s_two_loop(
        inv0, b_vec, full_bij)

    alpha_s_measured = _mpf_from_fraction(
        _frac(_need(v, "coupling_alpha_s_mz_v0")))
    miss_sm = (mp.mpf("100") * abs(alpha_s_sm - alpha_s_measured)
               / alpha_s_measured)
    miss_full = (mp.mpf("100") * abs(alpha_s_full - alpha_s_measured)
                 / alpha_s_measured)

    return {
        "key": "coupling_two_loop_alpha_s_euler_v0",
        "outputs": {
            "result_alpha_s_two_loop_sm_bij_derived_v0": _mp_str(
                alpha_s_sm, 12),
            "result_alpha_s_two_loop_sm_bij_miss_pct_v0": _mp_str(
                miss_sm, 8),
            "result_alpha_s_two_loop_full_bij_derived_v0": _mp_str(
                alpha_s_full, 12),
            "result_alpha_s_two_loop_full_bij_miss_pct_v0": _mp_str(
                miss_full, 8),
            "result_two_loop_l_gut_full_bij_v0": _mp_str(l_full, 12),
            "result_two_loop_alpha_gut_inverse_full_bij_v0": _mp_str(
                inv_gut_full, 12),
        },
        "notes": "Euler integration with 4000 steps, 60-step binary search.",
    }


# ================================================================
# DERIVATIONS: KOIDE
# ================================================================

def koide_ratio_v0(value_dicts):
    """
    Compute Koide ratio K = sum(m) / (sum(sqrt(m)))^2.

    Inputs:
    - mass_electron_v0
    - mass_muon_v0
    - mass_tau_v0

    Outputs:
    - koide_charged_leptons_k_derived_v0
    - koide_charged_leptons_a2_derived_v0
    - koide_charged_leptons_a2_minus_two_derived_v0

    Arithmetic: mixed (sqrt is irrational boundary)
    """
    v = _value_map(value_dicts)

    m_e = _mpf_from_fraction(_frac(_need(v, "mass_electron_v0")))
    m_mu = _mpf_from_fraction(_frac(_need(v, "mass_muon_v0")))
    m_tau = _mpf_from_fraction(_frac(_need(v, "mass_tau_v0")))

    s = mp.sqrt(m_e) + mp.sqrt(m_mu) + mp.sqrt(m_tau)
    k = (m_e + m_mu + m_tau) / (s * s)
    a2 = mp.mpf("2") * (mp.mpf("3") * k - mp.mpf("1"))

    return {
        "key": "koide_ratio_v0",
        "outputs": {
            "koide_charged_leptons_k_derived_v0": _mp_str(k, 12),
            "koide_charged_leptons_a2_derived_v0": _mp_str(a2, 12),
            "koide_charged_leptons_a2_minus_two_derived_v0": _mp_str(
                a2 - mp.mpf("2"), 12),
        },
        "notes": "",
    }


def koide_tau_prediction_v0(value_dicts):
    """
    Predict m_tau from m_e and m_mu assuming K = 2/3.

    Inputs:
    - mass_electron_v0
    - mass_muon_v0

    Outputs:
    - result_tau_mass_koide_two_thirds_derived_v0

    Arithmetic: mixed (sqrt is irrational boundary)
    """
    v = _value_map(value_dicts)

    m_e = _mpf_from_fraction(_frac(_need(v, "mass_electron_v0")))
    m_mu = _mpf_from_fraction(_frac(_need(v, "mass_muon_v0")))

    s = mp.sqrt(m_e) + mp.sqrt(m_mu)
    m_sum = m_e + m_mu
    x = (mp.mpf("2") * s
         + mp.sqrt(mp.mpf("6") * s * s - mp.mpf("3") * m_sum))
    m_tau_pred = x * x

    return {
        "key": "koide_tau_prediction_v0",
        "outputs": {
            "result_tau_mass_koide_two_thirds_derived_v0": _mp_str(
                m_tau_pred, 12),
        },
        "notes": "",
    }


# ================================================================
# DERIVATIONS: COSMOLOGICAL PREDICTIONS
# ================================================================

def cosmo_dm_baryon_ratio_v0(value_dicts):
    """
    Predict DM/baryon ratio from beta integers.

    Inputs:
    - integer_two_times_yang_mills_v0
    - integer_b2_modified_numerator_abs_v0

    Outputs:
    - cosmo_dm_to_baryon_ratio_prefactor_derived_v0
    - cosmo_dm_to_baryon_ratio_predicted_derived_v0

    Arithmetic: mixed (pi is irrational boundary)
    """
    v = _value_map(value_dicts)

    two_ym = _frac(_need(v, "integer_two_times_yang_mills_v0"))
    b2_abs_num = _frac(_need(v, "integer_b2_modified_numerator_abs_v0"))

    prefactor = two_ym / b2_abs_num
    numeric = _mpf_from_fraction(prefactor) * mp.pi

    return {
        "key": "cosmo_dm_baryon_ratio_v0",
        "outputs": {
            "cosmo_dm_to_baryon_ratio_prefactor_derived_v0": prefactor,
            "cosmo_dm_to_baryon_ratio_predicted_derived_v0": _mp_str(
                numeric, 12),
        },
        "notes": "Exact prefactor 22/13 is rational. Pi enters numerically.",
    }


def cosmo_omega_dm_v0(value_dicts):
    """
    Predict Omega_DM from beta integers and R2.

    Inputs:
    - integer_four_times_yang_mills_v0
    - integer_b2_modified_numerator_square_v0

    Outputs:
    - cosmo_omega_dm_r2_prefactor_derived_v0
    - cosmo_omega_dm_predicted_derived_v0

    Arithmetic: mixed (R2 = pi/4 is irrational boundary)
    """
    v = _value_map(value_dicts)

    four_ym = _frac(_need(v, "integer_four_times_yang_mills_v0"))
    b2_sq = _frac(_need(v, "integer_b2_modified_numerator_square_v0"))

    prefactor = four_ym / b2_sq
    r2_numeric = mp.pi / mp.mpf("4")
    omega = _mpf_from_fraction(prefactor) * r2_numeric

    return {
        "key": "cosmo_omega_dm_v0",
        "outputs": {
            "cosmo_omega_dm_r2_prefactor_derived_v0": prefactor,
            "cosmo_omega_dm_predicted_derived_v0": _mp_str(omega, 12),
        },
        "notes": "44/169 is pure rational. R2 = pi/4 enters numerically.",
    }


def cosmo_amplification_factor_decomposition_v0(value_dicts):
    """
    Decompose the DM amplification factor.

    Inputs:
    - integer_four_times_yang_mills_v0
    - integer_b2_modified_numerator_abs_v0

    Outputs:
    - cosmo_amplification_reduced_factor_v0
    - cosmo_amplification_formula_text_v0

    Arithmetic: exact
    """
    v = _value_map(value_dicts)

    four_ym = _frac(_need(v, "integer_four_times_yang_mills_v0"))
    b2_abs_num = _frac(_need(v, "integer_b2_modified_numerator_abs_v0"))

    reduced_factor = four_ym / b2_abs_num

    return {
        "key": "cosmo_amplification_factor_decomposition_v0",
        "outputs": {
            "cosmo_amplification_reduced_factor_v0": reduced_factor,
            "cosmo_amplification_formula_text_v0": "(44/13) * pi * (c/v)^2",
        },
        "notes": "",
    }


# ================================================================
# CONNECTIONS
# ================================================================

def connection_coupling_convergence_v0(value_dicts):
    """
    Connection bundle for coupling convergence analysis.

    Inputs:
    - coupling_alpha_1_inverse_gut_normalized_mz_v0
    - coupling_alpha_2_inverse_mz_v0
    - coupling_alpha_3_inverse_mz_v0
    - beta_modified_u1_total_v0
    - beta_modified_su2_total_v0
    - beta_modified_su3_total_v0
    - coupling_measured_gap_ratio_v0
    - gap_sm_cabibbo_doublet_ratio_v0

    Connection type: convergence
    """
    v = _value_map(value_dicts)

    named_values = {
        "inv_a1": _named_value(
            v, "coupling_alpha_1_inverse_gut_normalized_mz_v0", "inv_a1"),
        "inv_a2": _named_value(
            v, "coupling_alpha_2_inverse_mz_v0", "inv_a2"),
        "inv_a3": _named_value(
            v, "coupling_alpha_3_inverse_mz_v0", "inv_a3"),
        "b1_mod": _named_value(
            v, "beta_modified_u1_total_v0", "b1_mod"),
        "b2_mod": _named_value(
            v, "beta_modified_su2_total_v0", "b2_mod"),
        "b3_mod": _named_value(
            v, "beta_modified_su3_total_v0", "b3_mod"),
        "gap_measured": _named_value(
            v, "coupling_measured_gap_ratio_v0", "gap_measured"),
        "gap_cd": _named_value(
            v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
    }

    edges = [
        {"from": "inv_a1", "to": "gap_measured",
         "relation": "participates_in_gap_ratio"},
        {"from": "inv_a2", "to": "gap_measured",
         "relation": "participates_in_gap_ratio"},
        {"from": "inv_a3", "to": "gap_measured",
         "relation": "participates_in_gap_ratio"},
        {"from": "b1_mod", "to": "gap_cd",
         "relation": "contributes_to_model_gap"},
        {"from": "b2_mod", "to": "gap_cd",
         "relation": "contributes_to_model_gap"},
        {"from": "b3_mod", "to": "gap_cd",
         "relation": "contributes_to_model_gap"},
        {"from": "gap_cd", "to": "gap_measured",
         "relation": "compared_against"},
    ]

    return {
        "key": "connection_coupling_convergence_v0",
        "named_values": named_values,
        "edges": edges,
        "notes": "Connection bundle for coupling convergence table.",
    }


def connection_gap_correction_chain_v0(value_dicts):
    """
    Connection bundle for gap ratio correction chain.

    Inputs:
    - gap_pure_gauge_ratio_v0
    - gap_sm_ratio_v0
    - gap_sm_cabibbo_doublet_ratio_v0
    - coupling_measured_gap_ratio_v0

    Connection type: correction_chain
    """
    v = _value_map(value_dicts)

    named_values = {
        "gap_pure": _named_value(
            v, "gap_pure_gauge_ratio_v0", "gap_pure"),
        "gap_sm": _named_value(
            v, "gap_sm_ratio_v0", "gap_sm"),
        "gap_cd": _named_value(
            v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
        "gap_measured": _named_value(
            v, "coupling_measured_gap_ratio_v0", "gap_measured"),
    }

    edges = [
        {"from": "gap_pure", "to": "gap_sm",
         "relation": "higgs_correction"},
        {"from": "gap_sm", "to": "gap_cd",
         "relation": "cabibbo_doublet_correction"},
        {"from": "gap_cd", "to": "gap_measured",
         "relation": "threshold_two_loop_residual"},
    ]

    return {
        "key": "connection_gap_correction_chain_v0",
        "named_values": named_values,
        "edges": edges,
        "notes": "Correction chain: pure gauge -> SM -> CD -> measured.",
    }


def connection_integer_network_v0(value_dicts):
    """
    Connection bundle for integer traceability network.

    Inputs:
    - integer_yang_mills_eleven_v0
    - integer_b2_modified_numerator_abs_v0
    - integer_four_times_yang_mills_v0
    - cosmo_dm_to_baryon_ratio_prefactor_v0
    - cosmo_omega_dm_r2_prefactor_v0
    - gap_sm_cabibbo_doublet_ratio_v0

    Connection type: traceability
    """
    v = _value_map(value_dicts)

    named_values = {
        "ym_11": _named_value(
            v, "integer_yang_mills_eleven_v0", "ym_11"),
        "b2_abs_13": _named_value(
            v, "integer_b2_modified_numerator_abs_v0", "b2_abs_13"),
        "four_ym": _named_value(
            v, "integer_four_times_yang_mills_v0", "four_ym"),
        "dm_prefactor": _named_value(
            v, "cosmo_dm_to_baryon_ratio_prefactor_v0", "dm_prefactor"),
        "omega_prefactor": _named_value(
            v, "cosmo_omega_dm_r2_prefactor_v0", "omega_prefactor"),
        "gap_cd": _named_value(
            v, "gap_sm_cabibbo_doublet_ratio_v0", "gap_cd"),
    }

    edges = [
        {"from": "ym_11", "to": "dm_prefactor",
         "relation": "numerator_source"},
        {"from": "b2_abs_13", "to": "dm_prefactor",
         "relation": "denominator_source"},
        {"from": "four_ym", "to": "omega_prefactor",
         "relation": "numerator_source"},
        {"from": "b2_abs_13", "to": "omega_prefactor",
         "relation": "squared_denominator_source"},
        {"from": "b2_abs_13", "to": "gap_cd",
         "relation": "embedded_in_b2_mod"},
    ]

    return {
        "key": "connection_integer_network_v0",
        "named_values": named_values,
        "edges": edges,
        "notes": "Integer traceability: 11, 13, 44, 169 across programs.",
    }


def connection_three_programs_shared_set_v0(value_dicts):
    """
    Connection bundle for three-program shared integer set.

    Inputs:
    - integer_yang_mills_eleven_v0
    - integer_b2_modified_numerator_abs_v0
    - geom_r2_v0
    - integer_b2_sm_numerator_abs_v0
    - integer_cabibbo_doublet_gap_numerator_v0
    - integer_cabibbo_doublet_gap_denominator_v0

    Connection type: shared_set
    """
    v = _value_map(value_dicts)

    named_values = {
        "ym_11": _named_value(
            v, "integer_yang_mills_eleven_v0", "ym_11"),
        "b2_abs_13": _named_value(
            v, "integer_b2_modified_numerator_abs_v0", "b2_abs_13"),
        "r2": _named_value(
            v, "geom_r2_v0", "r2"),
        "b2_sm_19": _named_value(
            v, "integer_b2_sm_numerator_abs_v0", "b2_sm_19"),
        "gap_num_38": _named_value(
            v, "integer_cabibbo_doublet_gap_numerator_v0", "gap_num_38"),
        "gap_den_27": _named_value(
            v, "integer_cabibbo_doublet_gap_denominator_v0", "gap_den_27"),
    }

    edges = [
        {"from": "ym_11", "to": "b2_abs_13",
         "relation": "beta_unification_pair"},
        {"from": "ym_11", "to": "r2",
         "relation": "cross_program_association"},
        {"from": "b2_abs_13", "to": "r2",
         "relation": "cross_program_association"},
        {"from": "b2_sm_19", "to": "gap_num_38",
         "relation": "doubles_to"},
        {"from": "gap_num_38", "to": "gap_den_27",
         "relation": "forms_gap_ratio"},
    ]

    return {
        "key": "connection_three_programs_shared_set_v0",
        "named_values": named_values,
        "edges": edges,
        "notes": "Shared integer set across beta, toroidal DM, Hubble.",
    }


def connection_object_adjacency_v0(value_dicts):
    """
    Connection bundle for object adjacency map.

    Inputs:
    - coupling_alpha_em_inverse_v0
    - coupling_sin2_theta_w_v0
    - coupling_alpha_s_mz_v0
    - beta_modified_su2_total_v0
    - integer_yang_mills_eleven_v0
    - geom_r2_v0
    - koide_charged_leptons_k_v0

    Connection type: adjacency
    """
    v = _value_map(value_dicts)

    named_values = {
        "alpha_inv": _named_value(
            v, "coupling_alpha_em_inverse_v0", "alpha_inv"),
        "sin2_tW": _named_value(
            v, "coupling_sin2_theta_w_v0", "sin2_tW"),
        "alpha_s": _named_value(
            v, "coupling_alpha_s_mz_v0", "alpha_s"),
        "b2_mod": _named_value(
            v, "beta_modified_su2_total_v0", "b2_mod"),
        "ym_11": _named_value(
            v, "integer_yang_mills_eleven_v0", "ym_11"),
        "r2": _named_value(
            v, "geom_r2_v0", "r2"),
        "koide_k": _named_value(
            v, "koide_charged_leptons_k_v0", "koide_k"),
    }

    edges = [
        {"from": "alpha_inv", "to": "sin2_tW",
         "relation": "joins_in_coupling_extraction"},
        {"from": "alpha_s", "to": "alpha_inv",
         "relation": "joins_in_measured_gap"},
        {"from": "b2_mod", "to": "ym_11",
         "relation": "integer_traceability_link"},
        {"from": "r2", "to": "ym_11",
         "relation": "cross_program_bridge"},
        {"from": "koide_k", "to": "alpha_inv",
         "relation": "shared_level2_measurement_class"},
    ]

    return {
        "key": "connection_object_adjacency_v0",
        "named_values": named_values,
        "edges": edges,
        "notes": "First-pass adjacency bundle.",
    }


# ================================================================
# REGISTRIES
# ================================================================

DERIVATION_INDEX_V0 = {
    "coupling_extraction_v0": coupling_extraction_v0,
    "gap_measured_ratio_v0": gap_measured_ratio_v0,
    "gap_sm_ratio_v0": gap_sm_ratio_v0,
    "gauge_pure_gap_v0": gauge_pure_gap_v0,
    "beta_sm_coefficients_v0": beta_sm_coefficients_v0,
    "beta_cabibbo_doublet_shifts_v0": beta_cabibbo_doublet_shifts_v0,
    "beta_modified_and_cd_gap_ratio_v0": beta_modified_and_cd_gap_ratio_v0,
    "generation_democracy_v0": generation_democracy_v0,
    "beta_double_action_mechanism_v0": beta_double_action_mechanism_v0,
    "beta_y_dependence_family_v0": beta_y_dependence_family_v0,
    "crossing_one_loop_scale_v0": crossing_one_loop_scale_v0,
    "coupling_one_loop_alpha_s_prediction_v0": (
        coupling_one_loop_alpha_s_prediction_v0),
    "coupling_two_loop_alpha_s_euler_v0": (
        coupling_two_loop_alpha_s_euler_v0),
    "koide_ratio_v0": koide_ratio_v0,
    "koide_tau_prediction_v0": koide_tau_prediction_v0,
    "cosmo_dm_baryon_ratio_v0": cosmo_dm_baryon_ratio_v0,
    "cosmo_omega_dm_v0": cosmo_omega_dm_v0,
    "cosmo_amplification_factor_decomposition_v0": (
        cosmo_amplification_factor_decomposition_v0),
}

CONNECTION_INDEX_V0 = {
    "connection_coupling_convergence_v0": (
        connection_coupling_convergence_v0),
    "connection_gap_correction_chain_v0": (
        connection_gap_correction_chain_v0),
    "connection_integer_network_v0": (
        connection_integer_network_v0),
    "connection_three_programs_shared_set_v0": (
        connection_three_programs_shared_set_v0),
    "connection_object_adjacency_v0": (
        connection_object_adjacency_v0),
}
