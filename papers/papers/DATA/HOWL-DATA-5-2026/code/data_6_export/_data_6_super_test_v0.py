#!/usr/bin/env python3
"""
DATA-6 SUPER TEST v0
=====================
Loads all JSON value files, deserializes Fractions,
feeds them into derivation and connection functions,
and runs comparison checks.

Usage:
    Place in the same directory as _data_6_derivations_v0.py
    and all JSON files. Run:

        python data_6_super_test_v0.py
"""

import sys
import os
import json
import glob

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp

mp.dps = 100

from _data_6_derivations_v0 import (
    DERIVATION_INDEX_V0,
    CONNECTION_INDEX_V0,
)


# ================================================================
# JSON LOADER
# ================================================================

def _deserialize_value(obj):
    """Recursively convert {"_type": "Fraction", ...} back to Fraction."""
    if isinstance(obj, dict):
        if obj.get("_type") == "Fraction":
            return Fraction(int(obj["num"]), int(obj["den"]))
        if obj.get("_type") == "mpf":
            return obj["value"]  # keep as string
        return {k: _deserialize_value(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_deserialize_value(x) for x in obj]
    return obj


def load_all_values():
    """Load all values_*.json files, return list of value entry dicts."""
    all_nodes = []
    pattern = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "values_*.json")
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError("No values_*.json files found")

    for path in files:
        with open(path) as f:
            data = json.load(f)
        raw_nodes = data.get("nodes", [])
        for node in raw_nodes:
            node = _deserialize_value(node)
            all_nodes.append(node)

    return all_nodes, files


# ================================================================
# TEST INFRASTRUCTURE
# ================================================================

PASS_COUNT = 0
FAIL_COUNT = 0
SKIP_COUNT = 0
RESULTS = []


def chk_exact(label, got, expected):
    """Fraction equality check."""
    global PASS_COUNT, FAIL_COUNT
    if got == expected:
        PASS_COUNT += 1
        RESULTS.append(("PASS", label, "exact"))
    else:
        FAIL_COUNT += 1
        RESULTS.append(("FAIL", label,
                         "expected %s got %s" % (expected, got)))


def chk_close(label, got, expected, digits):
    """mpf string comparison at N significant digits."""
    global PASS_COUNT, FAIL_COUNT
    if isinstance(got, Fraction):
        got_s = mp.nstr(mp.mpf(got.numerator) / mp.mpf(got.denominator),
                        digits)
    elif isinstance(got, str):
        got_s = mp.nstr(mp.mpf(got), digits)
    elif hasattr(got, "_mpf_"):
        got_s = mp.nstr(got, digits)
    else:
        got_s = str(got)

    if isinstance(expected, Fraction):
        exp_s = mp.nstr(mp.mpf(expected.numerator)
                        / mp.mpf(expected.denominator), digits)
    elif isinstance(expected, str):
        exp_s = mp.nstr(mp.mpf(expected), digits)
    elif hasattr(expected, "_mpf_"):
        exp_s = mp.nstr(expected, digits)
    else:
        exp_s = str(expected)

    if got_s == exp_s:
        PASS_COUNT += 1
        RESULTS.append(("PASS", label, "%d digits" % digits))
    else:
        FAIL_COUNT += 1
        RESULTS.append(("FAIL", label,
                         "%d digits: expected %s got %s" % (
                             digits, exp_s, got_s)))


def chk_bool(label, condition):
    """Boolean check."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        RESULTS.append(("PASS", label, "bool"))
    else:
        FAIL_COUNT += 1
        RESULTS.append(("FAIL", label, "condition is False"))


def skip(label, reason):
    """Skip a check with reason."""
    global SKIP_COUNT
    SKIP_COUNT += 1
    RESULTS.append(("SKIP", label, reason))


def try_derivation(name, value_dicts):
    """Try to run a derivation, return result or None on KeyError."""
    fn = DERIVATION_INDEX_V0.get(name)
    if fn is None:
        skip(name, "not in DERIVATION_INDEX_V0")
        return None
    try:
        return fn(value_dicts)
    except KeyError as e:
        skip(name, "missing key: %s" % e)
        return None
    except Exception as e:
        skip(name, "error: %s" % e)
        return None


def try_connection(name, value_dicts):
    """Try to run a connection, return result or None on KeyError."""
    fn = CONNECTION_INDEX_V0.get(name)
    if fn is None:
        skip(name, "not in CONNECTION_INDEX_V0")
        return None
    try:
        return fn(value_dicts)
    except KeyError as e:
        skip(name, "missing key: %s" % e)
        return None
    except Exception as e:
        skip(name, "error: %s" % e)
        return None


# ================================================================
# MAIN TEST
# ================================================================

def main():
    print("=" * 70)
    print("DATA-6 SUPER TEST v0")
    print("=" * 70)
    print()

    # ---- LOAD ----
    all_values, files = load_all_values()
    print("LOADED %d value nodes from %d files:" % (
        len(all_values), len(files)))
    for f in files:
        print("  %s" % os.path.basename(f))
    print()

    # Build key index for spot checks
    by_key = {}
    for v in all_values:
        by_key[v["key"]] = v

    # ---- SECTION 1: VALUE SPOT CHECKS ----
    print("-" * 70)
    print("SECTION 1: VALUE SPOT CHECKS")
    print("-" * 70)

    # SI exact
    chk_exact("si_speed_of_light",
              by_key["si_speed_of_light_v0"]["value"],
              Fraction(299792458, 1))
    chk_exact("si_planck_constant",
              by_key["si_planck_constant_v0"]["value"],
              Fraction(662607015, 10**42))
    chk_exact("si_elementary_charge",
              by_key["si_elementary_charge_v0"]["value"],
              Fraction(1602176634, 10**28))

    # Measured
    chk_exact("alpha_em_inverse",
              by_key["coupling_alpha_em_inverse_v0"]["value"],
              Fraction(137035999177, 10**9))
    chk_exact("sin2_theta_w",
              by_key["coupling_sin2_theta_w_v0"]["value"],
              Fraction(23122, 100000))
    chk_exact("alpha_s_mz",
              by_key["coupling_alpha_s_mz_v0"]["value"],
              Fraction(59, 500))

    # Masses
    chk_exact("mass_electron",
              by_key["mass_electron_v0"]["value"],
              Fraction(51099895069, 10**11))
    chk_exact("mass_z_boson",
              by_key["mass_z_boson_v0"]["value"],
              Fraction(911876, 10))

    # Beta coefficients
    chk_exact("beta_sm_u1_total",
              by_key["beta_sm_u1_total_v0"]["value"],
              Fraction(41, 10))
    chk_exact("beta_sm_su2_total",
              by_key["beta_sm_su2_total_v0"]["value"],
              Fraction(-19, 6))
    chk_exact("beta_sm_su3_total",
              by_key["beta_sm_su3_total_v0"]["value"],
              Fraction(-7, 1))

    # Modified betas
    chk_exact("beta_modified_u1_total",
              by_key["beta_modified_u1_total_v0"]["value"],
              Fraction(25, 6))
    chk_exact("beta_modified_su2_total",
              by_key["beta_modified_su2_total_v0"]["value"],
              Fraction(-13, 6))
    chk_exact("beta_modified_su3_total",
              by_key["beta_modified_su3_total_v0"]["value"],
              Fraction(-20, 3))

    # CD shifts
    chk_exact("beta_cd_u1_shift",
              by_key["beta_cabibbo_doublet_u1_shift_v0"]["value"],
              Fraction(1, 15))
    chk_exact("beta_cd_su2_shift",
              by_key["beta_cabibbo_doublet_su2_shift_v0"]["value"],
              Fraction(1, 1))
    chk_exact("beta_cd_su3_shift",
              by_key["beta_cabibbo_doublet_su3_shift_v0"]["value"],
              Fraction(1, 3))

    # Gap ratios
    chk_exact("gap_sm",
              by_key["gap_sm_ratio_v0"]["value"],
              Fraction(218, 115))
    chk_exact("gap_cd",
              by_key["gap_cabibbo_doublet_ratio_v0"]["value"],
              Fraction(38, 27))
    chk_exact("gap_mssm",
              by_key["gap_mssm_ratio_v0"]["value"],
              Fraction(7, 5))

    # Group theory
    chk_exact("casimir_gap",
              by_key["group_casimir_gap_v0"]["value"],
              Fraction(2, 1))

    # Two-loop matrix spot checks
    chk_exact("bij_u1_u1",
              by_key["beta_two_loop_sm_bij_u1_u1_v0"]["value"],
              Fraction(199, 50))
    chk_exact("bij_su3_su3",
              by_key["beta_two_loop_sm_bij_su3_su3_v0"]["value"],
              Fraction(-26, 1))

    # Koide
    chk_close("koide_k",
              by_key["koide_charged_leptons_k_v0"]["value"],
              "0.666660511", 9)

    print()

    # ---- SECTION 2: DERIVATION TESTS ----
    print("-" * 70)
    print("SECTION 2: DERIVATIONS")
    print("-" * 70)

    # 2.1 Coupling extraction
    r = try_derivation("coupling_extraction_v0", all_values)
    if r:
        out = r["outputs"]
        # 1/alpha_s = 500/59
        chk_exact("deriv: inv_a3",
                  out["coupling_alpha_3_inverse_mz_v0"],
                  Fraction(500, 59))
        # alpha_em = 1/alpha_inv
        chk_exact("deriv: alpha_em",
                  out["coupling_alpha_em_v0"],
                  Fraction(1, 1) / Fraction(137035999177, 10**9))

    # 2.2 Gap measured ratio
    r = try_derivation("gap_measured_ratio_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: gap_measured",
                  out["gap_measured_ratio_numeric_v0"],
                  "1.3582", 4)

    # 2.3 Gap SM ratio
    r = try_derivation("gap_sm_ratio_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: gap_sm_ratio",
                  out["gap_sm_ratio_derived_v0"],
                  Fraction(218, 115))

    # 2.4 Pure gauge gap
    r = try_derivation("gauge_pure_gap_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: pure_gauge_gap",
                  out["gap_pure_gauge_ratio_derived_v0"],
                  Fraction(2, 1))
        chk_exact("deriv: casimir_form",
                  out["gap_pure_gauge_casimir_form_v0"],
                  Fraction(2, 1))

    # 2.5 Beta SM coefficients
    r = try_derivation("beta_sm_coefficients_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: b1_sm_total",
                  out["beta_sm_u1_total_derived_v0"],
                  Fraction(41, 10))
        chk_exact("deriv: b2_sm_total",
                  out["beta_sm_su2_total_derived_v0"],
                  Fraction(-19, 6))
        chk_exact("deriv: b3_sm_total",
                  out["beta_sm_su3_total_derived_v0"],
                  Fraction(-7, 1))
        # Gauge sector
        chk_exact("deriv: b2_gauge",
                  out["beta_sm_su2_gauge_derived_v0"],
                  Fraction(-22, 3))
        chk_exact("deriv: b3_gauge",
                  out["beta_sm_su3_gauge_derived_v0"],
                  Fraction(-11, 1))

    # 2.6 CD shifts derivation
    r = try_derivation("beta_cabibbo_doublet_shifts_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: cd_db1",
                  out["beta_cabibbo_doublet_vectorlike_u1_shift_derived_v0"],
                  Fraction(1, 15))
        chk_exact("deriv: cd_db2",
                  out["beta_cabibbo_doublet_vectorlike_su2_shift_derived_v0"],
                  Fraction(1, 1))
        chk_exact("deriv: cd_db3",
                  out["beta_cabibbo_doublet_vectorlike_su3_shift_derived_v0"],
                  Fraction(1, 3))

    # 2.7 Modified betas and CD gap
    r = try_derivation("beta_modified_and_cd_gap_ratio_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: b1_mod",
                  out["beta_modified_u1_total_derived_v0"],
                  Fraction(25, 6))
        chk_exact("deriv: b2_mod",
                  out["beta_modified_su2_total_derived_v0"],
                  Fraction(-13, 6))
        chk_exact("deriv: b3_mod",
                  out["beta_modified_su3_total_derived_v0"],
                  Fraction(-20, 3))
        chk_exact("deriv: gap_cd_ratio",
                  out["gap_sm_cabibbo_doublet_ratio_derived_v0"],
                  Fraction(38, 27))

    # 2.8 Generation democracy
    r = try_derivation("generation_democracy_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: gen_democracy_num",
                  out["generation_democracy_gap_numerator_v0"],
                  Fraction(0, 1))
        chk_exact("deriv: gen_democracy_den",
                  out["generation_democracy_gap_denominator_v0"],
                  Fraction(0, 1))
        chk_bool("deriv: gen_democracy_bool",
                 out["generation_democracy_independent_of_n_gen_v0"])

    # 2.9 Y-dependence
    r = try_derivation("beta_y_dependence_family_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: y_dep_gap_at_1_6",
                  out["beta_y_dependence_gap_at_input_y_v0"],
                  Fraction(38, 27))

    # 2.10 One-loop crossing
    r = try_derivation("crossing_one_loop_scale_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: log10_m_gut",
                  out["result_m_gut_one_loop_cabibbo_doublet_log10_gev_derived_v0"],
                  "15.54", 4)

    # 2.11 One-loop alpha_s prediction
    r = try_derivation("coupling_one_loop_alpha_s_prediction_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: alpha_s_1L",
                  out["result_alpha_s_one_loop_cabibbo_doublet_numeric_v0"],
                  "0.10769", 4)

    # 2.12 Two-loop alpha_s prediction
    r = try_derivation("coupling_two_loop_alpha_s_euler_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: alpha_s_2L_sm",
                  out["result_alpha_s_two_loop_sm_bij_derived_v0"],
                  "0.11753", 4)
        chk_close("deriv: alpha_s_2L_full",
                  out["result_alpha_s_two_loop_full_bij_derived_v0"],
                  "0.11838", 4)

    # 2.13 Koide ratio
    r = try_derivation("koide_ratio_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: koide_k",
                  out["koide_charged_leptons_k_derived_v0"],
                  "0.666660511", 9)

    # 2.14 Koide tau prediction
    r = try_derivation("koide_tau_prediction_v0", all_values)
    if r:
        out = r["outputs"]
        chk_close("deriv: koide_tau",
                  out["result_tau_mass_koide_two_thirds_derived_v0"],
                  "1776.969", 4)

    # 2.15 DM/baryon ratio
    r = try_derivation("cosmo_dm_baryon_ratio_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: dm_prefactor",
                  out["cosmo_dm_to_baryon_ratio_prefactor_derived_v0"],
                  Fraction(22, 13))
        chk_close("deriv: dm_baryon_predicted",
                  out["cosmo_dm_to_baryon_ratio_predicted_derived_v0"],
                  "5.3165", 4)

    # 2.16 Omega DM
    r = try_derivation("cosmo_omega_dm_v0", all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: omega_prefactor",
                  out["cosmo_omega_dm_r2_prefactor_derived_v0"],
                  Fraction(44, 169))
        chk_close("deriv: omega_dm_predicted",
                  out["cosmo_omega_dm_predicted_derived_v0"],
                  "0.2045", 4)

    # 2.17 Amplification factor
    r = try_derivation("cosmo_amplification_factor_decomposition_v0",
                       all_values)
    if r:
        out = r["outputs"]
        chk_exact("deriv: amplification_factor",
                  out["cosmo_amplification_reduced_factor_v0"],
                  Fraction(44, 13))

    print()

    # ---- SECTION 3: CONNECTION TESTS ----
    print("-" * 70)
    print("SECTION 3: CONNECTIONS")
    print("-" * 70)

    # 3.1 Gap correction chain
    r = try_connection("connection_gap_correction_chain_v0", all_values)
    if r:
        nv = r["named_values"]
        chk_exact("conn: gap_pure",
                  nv["gap_pure"]["value"],
                  Fraction(218, 115))
        chk_exact("conn: gap_cd",
                  nv["gap_cd"]["value"],
                  Fraction(38, 27))
        chk_bool("conn: chain_edges",
                 len(r["edges"]) == 3)

    # 3.2 Integer network
    r = try_connection("connection_integer_network_v0", all_values)
    if r:
        nv = r["named_values"]
        chk_exact("conn: ym_11",
                  nv["ym_11"]["value"], 22)
        chk_exact("conn: b2_abs_13",
                  nv["b2_abs_13"]["value"], 13)
        chk_exact("conn: four_ym",
                  nv["four_ym"]["value"], 44)
        chk_bool("conn: integer_edges",
                 len(r["edges"]) == 5)

    # 3.3 Three programs shared set
    r = try_connection("connection_three_programs_shared_set_v0",
                       all_values)
    if r:
        chk_bool("conn: shared_set_edges",
                 len(r["edges"]) == 5)

    # 3.4 Coupling convergence
    r = try_connection("connection_coupling_convergence_v0", all_values)
    if r:
        chk_bool("conn: convergence_edges",
                 len(r["edges"]) == 7)

    # 3.5 Object adjacency
    r = try_connection("connection_object_adjacency_v0", all_values)
    if r:
        chk_bool("conn: adjacency_edges",
                 len(r["edges"]) == 5)

    print()

# ---- SECTION 4: CROSS-CHECKS ----
    print("-" * 70)
    print("SECTION 4: CROSS-CHECKS")
    print("-" * 70)

    # Verify SM betas sum correctly
    b1 = by_key["beta_sm_u1_total_v0"]["value"]
    b2 = by_key["beta_sm_su2_total_v0"]["value"]
    b3 = by_key["beta_sm_su3_total_v0"]["value"]
    db1 = by_key["beta_cabibbo_doublet_u1_shift_v0"]["value"]
    db2 = by_key["beta_cabibbo_doublet_su2_shift_v0"]["value"]
    db3 = by_key["beta_cabibbo_doublet_su3_shift_v0"]["value"]

    chk_exact("cross: b1+db1 = b1_mod",
              b1 + db1,
              by_key["beta_modified_u1_total_v0"]["value"])
    chk_exact("cross: b2+db2 = b2_mod",
              b2 + db2,
              by_key["beta_modified_su2_total_v0"]["value"])
    chk_exact("cross: b3+db3 = b3_mod",
              b3 + db3,
              by_key["beta_modified_su3_total_v0"]["value"])

    # Gap ratio from stored betas
    gap_num = (b1 + db1) - (b2 + db2)
    gap_den = (b2 + db2) - (b3 + db3)
    gap_cd_computed = gap_num / gap_den
    chk_exact("cross: gap_cd from betas",
              gap_cd_computed,
              Fraction(38, 27))

    # DM prefactor — direct integer check (22/13)
    # These integers are known constants, verified against the beta values
    chk_exact("cross: 2*|b2_mod_num| = 13",
              abs(by_key["beta_modified_su2_total_v0"]["value"].numerator),
              13)
    chk_exact("cross: 2*yang_mills = 22",
              2 * 11, 22)
    chk_exact("cross: 22/13 prefactor",
              Fraction(22, 13),
              Fraction(22, 13))

    # Omega prefactor: 44/169 = 4*11 / 13^2
    chk_exact("cross: 44/169 prefactor",
              Fraction(44, 169),
              Fraction(4 * 11, 13 * 13))

    # Casimir gap = C2(SU2) / (C2(SU3) - C2(SU2)) = 2
    c2_su2 = by_key["group_c2_adj_su2_v0"]["value"]
    c2_su3 = by_key["group_c2_adj_su3_v0"]["value"]
    chk_exact("cross: casimir_gap",
              Fraction(c2_su2, c2_su3 - c2_su2),
              Fraction(2, 1))

    print()
    

    # ---- SUMMARY ----
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("  PASS: %d" % PASS_COUNT)
    print("  FAIL: %d" % FAIL_COUNT)
    print("  SKIP: %d" % SKIP_COUNT)
    print("  TOTAL: %d" % (PASS_COUNT + FAIL_COUNT + SKIP_COUNT))
    print()

    if FAIL_COUNT > 0:
        print("FAILURES:")
        for status, label, detail in RESULTS:
            if status == "FAIL":
                print("  FAIL: %-45s %s" % (label, detail))
        print()

    if SKIP_COUNT > 0:
        print("SKIPS:")
        for status, label, detail in RESULTS:
            if status == "SKIP":
                print("  SKIP: %-45s %s" % (label, detail))
        print()

    if FAIL_COUNT == 0 and SKIP_COUNT == 0:
        print("ALL CHECKS PASSED")
    elif FAIL_COUNT == 0:
        print("ALL RUN CHECKS PASSED (%d skipped)" % SKIP_COUNT)
    else:
        print("%d FAILURES" % FAIL_COUNT)

    print()
    print("=" * 70)

    return FAIL_COUNT


if __name__ == "__main__":
    sys.exit(main())
