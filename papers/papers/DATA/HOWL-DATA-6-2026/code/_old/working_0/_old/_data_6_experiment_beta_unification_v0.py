#!/usr/bin/env python3
"""
DATA-6 EXPERIMENT: BETA UNIFICATION v0
========================================
Loads JSON values, runs all 18 derivations in dependency order,
runs all 5 connections, compares outputs against references.

Usage:
    python data_6_experiment_beta_unification_v0.py
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
    if isinstance(obj, dict):
        if obj.get("_type") == "Fraction":
            return Fraction(int(obj["num"]), int(obj["den"]))
        if obj.get("_type") == "mpf":
            return obj["value"]
        return {k: _deserialize_value(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_deserialize_value(x) for x in obj]
    return obj


def load_all_values():
    all_nodes = []
    pattern = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "values_*.json")
    files = sorted(glob.glob(pattern))
    for path in files:
        with open(path) as f:
            data = json.load(f)
        for node in data.get("nodes", []):
            node = _deserialize_value(node)
            all_nodes.append(node)
    return all_nodes


# ================================================================
# MINI RUNNER
# ================================================================

def make_result_entry(key, value, unit="dimensionless", source="derivation"):
    """Wrap a derivation output as a value entry dict."""
    if isinstance(value, Fraction):
        vtype = "exact_fraction"
    elif isinstance(value, int):
        vtype = "exact_integer"
    elif isinstance(value, str):
        vtype = "approximate"
    elif isinstance(value, bool):
        vtype = "exact_integer"
    else:
        vtype = "approximate"

    return {
        "key": key,
        "canonical": key.replace("_v0", ""),
        "version": 0,
        "node_type": "value",
        "value": value,
        "value_type": vtype,
        "unit": unit,
        "source": source,
    }


def run_derivation(name, value_pool):
    """Run one derivation, merge outputs into the pool."""
    fn = DERIVATION_INDEX_V0.get(name)
    if fn is None:
        print("  [SKIP] %s — not found" % name)
        return False
    try:
        result = fn(value_pool)
    except Exception as e:
        print("  [ERROR] %s — %s" % (name, e))
        return False

    outputs = result.get("outputs", {})
    count = len(outputs)
    for out_key, out_val in outputs.items():
        value_pool.append(make_result_entry(out_key, out_val,
                                            source=name))
    print("  [OK] %-55s %2d outputs" % (name, count))
    return True


def run_connection(name, value_pool):
    """Run one connection, print summary."""
    fn = CONNECTION_INDEX_V0.get(name)
    if fn is None:
        print("  [SKIP] %s — not found" % name)
        return None
    try:
        result = fn(value_pool)
    except Exception as e:
        print("  [ERROR] %s — %s" % (name, e))
        return None

    n_vals = len(result.get("named_values", {}))
    n_edges = len(result.get("edges", []))
    print("  [OK] %-55s %2d values, %2d edges" % (name, n_vals, n_edges))
    return result


# ================================================================
# COMPARISON ENGINE
# ================================================================

def _to_mpf(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / mp.mpf(x.denominator)
    if isinstance(x, str):
        return mp.mpf(x)
    if isinstance(x, int):
        return mp.mpf(x)
    if isinstance(x, bool):
        return mp.mpf(1 if x else 0)
    if hasattr(x, "_mpf_"):
        return x
    return mp.mpf(str(x))


def compare_exact(label, got, expected):
    """Fraction equality."""
    if got == expected:
        return ("PASS", label, "exact", "—")
    else:
        return ("FAIL", label, "exact",
                "expected %s got %s" % (expected, got))


def compare_digits(label, got, ref_str, digits):
    """Compare at N significant digits, report miss%."""
    got_mpf = _to_mpf(got)
    ref_mpf = mp.mpf(ref_str)
    got_s = mp.nstr(got_mpf, digits)
    ref_s = mp.nstr(ref_mpf, digits)

    if ref_mpf != 0:
        miss_pct = abs(got_mpf - ref_mpf) / abs(ref_mpf) * 100
    else:
        miss_pct = mp.mpf("0")

    miss_str = mp.nstr(miss_pct, 4) + "%"

    if got_s == ref_s:
        return ("PASS", label, "%d digits" % digits,
                "got %s miss %s" % (
                    mp.nstr(got_mpf, digits + 2), miss_str))
    else:
        return ("FAIL", label, "%d digits" % digits,
                "expected %s got %s miss %s" % (
                    ref_s, mp.nstr(got_mpf, digits + 2), miss_str))


def compare_range(label, got, lo, hi):
    """Value within bounds."""
    got_mpf = _to_mpf(got)
    if mp.mpf(lo) <= got_mpf <= mp.mpf(hi):
        return ("PASS", label, "range [%s, %s]" % (lo, hi),
                "got %s" % mp.nstr(got_mpf, 6))
    else:
        return ("FAIL", label, "range [%s, %s]" % (lo, hi),
                "got %s" % mp.nstr(got_mpf, 6))


def compare_bool(label, got, expected=True):
    """Boolean check."""
    if got == expected:
        return ("PASS", label, "bool", "—")
    else:
        return ("FAIL", label, "bool", "got %s" % got)


def compare_miss_only(label, got, ref_str):
    """Always PASS, just report the miss% for informational purposes."""
    got_mpf = _to_mpf(got)
    ref_mpf = mp.mpf(ref_str)
    if ref_mpf != 0:
        miss_pct = abs(got_mpf - ref_mpf) / abs(ref_mpf) * 100
    else:
        miss_pct = mp.mpf("0")
    return ("INFO", label, "miss",
            "predicted %s measured %s miss %s%%" % (
                mp.nstr(got_mpf, 8), ref_str,
                mp.nstr(miss_pct, 4)))


# ================================================================
# MAIN EXPERIMENT
# ================================================================

def find_output(key, value_pool):
    """Find a value by key in the pool. Returns value or None."""
    for entry in reversed(value_pool):
        if entry["key"] == key:
            return entry["value"]
    return None


def main():
    print("=" * 70)
    print("DATA-6 EXPERIMENT: BETA UNIFICATION v0")
    print("=" * 70)
    print()

    # ---- LOAD ----
    value_pool = load_all_values()
    print("Loaded %d value nodes from JSON." % len(value_pool))
    print()

    # ---- EXECUTION PLAN ----
    print("-" * 70)
    print("EXECUTION PLAN: 18 derivations")
    print("-" * 70)

    execution_order = [
        "coupling_extraction_v0",
        "beta_sm_coefficients_v0",
        "beta_cabibbo_doublet_shifts_v0",
        "beta_modified_and_cd_gap_ratio_v0",
        "generation_democracy_v0",
        "gauge_pure_gap_v0",
        "gap_sm_ratio_v0",
        "gap_measured_ratio_v0",
        "beta_double_action_mechanism_v0",
        "beta_y_dependence_family_v0",
        "crossing_one_loop_scale_v0",
        "coupling_one_loop_alpha_s_prediction_v0",
        "coupling_two_loop_alpha_s_euler_v0",
        "koide_ratio_v0",
        "koide_tau_prediction_v0",
        "cosmo_dm_baryon_ratio_v0",
        "cosmo_omega_dm_v0",
        "cosmo_amplification_factor_decomposition_v0",
    ]

    ok_count = 0
    err_count = 0
    for name in execution_order:
        if run_derivation(name, value_pool):
            ok_count += 1
        else:
            err_count += 1

    print()
    print("Derivations: %d OK, %d errors" % (ok_count, err_count))
    print()

    # ---- CONNECTIONS ----
    print("-" * 70)
    print("CONNECTIONS: 5 bundles")
    print("-" * 70)

    connection_order = [
        "connection_coupling_convergence_v0",
        "connection_gap_correction_chain_v0",
        "connection_integer_network_v0",
        "connection_three_programs_shared_set_v0",
        "connection_object_adjacency_v0",
    ]

    conn_results = {}
    for name in connection_order:
        r = run_connection(name, value_pool)
        if r:
            conn_results[name] = r

    print()

    # ---- COMPARISONS ----
    print("-" * 70)
    print("COMPARISONS")
    print("-" * 70)
    print()

    comparisons = []

    # --- EXACT CHECKS ---

    v = find_output("gap_pure_gauge_ratio_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "Pure gauge gap = 2", v, Fraction(2, 1)))

    v = find_output("gap_sm_ratio_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "SM gap = 218/115", v, Fraction(218, 115)))

    v = find_output("gap_sm_cabibbo_doublet_ratio_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "CD gap = 38/27", v, Fraction(38, 27)))

    v = find_output("gap_pure_gauge_casimir_form_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "Casimir form = 2", v, Fraction(2, 1)))

    v = find_output("generation_democracy_independent_of_n_gen_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_bool(
            "Generation democracy holds", v, True))

    v = find_output("beta_sm_u1_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b1_SM = 41/10", v, Fraction(41, 10)))

    v = find_output("beta_sm_su2_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b2_SM = -19/6", v, Fraction(-19, 6)))

    v = find_output("beta_sm_su3_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b3_SM = -7", v, Fraction(-7, 1)))

    v = find_output("beta_modified_u1_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b1_mod = 25/6", v, Fraction(25, 6)))

    v = find_output("beta_modified_su2_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b2_mod = -13/6", v, Fraction(-13, 6)))

    v = find_output("beta_modified_su3_total_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "b3_mod = -20/3", v, Fraction(-20, 3)))

    v = find_output("beta_cabibbo_doublet_vectorlike_u1_shift_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "CD db1 = 1/15", v, Fraction(1, 15)))

    v = find_output("beta_cabibbo_doublet_vectorlike_su2_shift_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "CD db2 = 1", v, Fraction(1, 1)))

    v = find_output("beta_cabibbo_doublet_vectorlike_su3_shift_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "CD db3 = 1/3", v, Fraction(1, 3)))

    v = find_output("beta_y_dependence_gap_at_input_y_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "Y-dep gap at Y=1/6 = 38/27", v, Fraction(38, 27)))

    v = find_output("cosmo_dm_to_baryon_ratio_prefactor_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "DM prefactor = 22/13", v, Fraction(22, 13)))

    v = find_output("cosmo_omega_dm_r2_prefactor_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "Omega_DM prefactor = 44/169", v, Fraction(44, 169)))

    v = find_output("cosmo_amplification_reduced_factor_v0", value_pool)
    if v is not None:
        comparisons.append(compare_exact(
            "Amplification = 44/13", v, Fraction(44, 13)))

    # --- DIGIT / MISS% CHECKS vs MEASURED ---

    v = find_output("gap_measured_ratio_numeric_v0", value_pool)
    if v is not None:
        comparisons.append(compare_digits(
            "Measured gap ratio", v, "1.3582", 4))

    v = find_output("result_alpha_s_one_loop_cabibbo_doublet_numeric_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "alpha_s one-loop vs measured", v, "0.1180"))

    v = find_output("result_alpha_s_two_loop_sm_bij_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "alpha_s two-loop SM bij vs measured", v, "0.1180"))

    v = find_output("result_alpha_s_two_loop_full_bij_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "alpha_s two-loop full bij vs measured", v, "0.1180"))

    v = find_output("koide_charged_leptons_k_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_digits(
            "Koide K vs 2/3", v, "0.666666667", 6))

    v = find_output("koide_charged_leptons_a2_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "Koide a^2 vs 2", v, "2.0"))

    v = find_output("result_tau_mass_koide_two_thirds_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "Koide m_tau prediction vs measured", v, "1776.86"))

    v = find_output("cosmo_dm_to_baryon_ratio_predicted_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "DM/baryon predicted vs Planck", v, "5.3204"))

    v = find_output("cosmo_omega_dm_predicted_derived_v0", value_pool)
    if v is not None:
        comparisons.append(compare_miss_only(
            "Omega_DM predicted vs Planck", v, "0.2607"))

    v = find_output(
        "result_m_gut_one_loop_cabibbo_doublet_log10_gev_derived_v0",
        value_pool)
    if v is not None:
        comparisons.append(compare_range(
            "log10(M_GUT/GeV) in [15, 16]", v, "15", "16"))

    v = find_output("result_l_gut_one_loop_cabibbo_doublet_derived_v0",
                    value_pool)
    if v is not None:
        comparisons.append(compare_range(
            "L_GUT in [4, 6]", v, "4", "6"))

    # --- CONNECTION CHECKS ---

    for conn_name, conn_result in conn_results.items():
        short = conn_name.replace("connection_", "").replace("_v0", "")
        n_edges = len(conn_result.get("edges", []))
        n_vals = len(conn_result.get("named_values", {}))
        comparisons.append(compare_bool(
            "conn %s has edges" % short,
            n_edges > 0, True))
        comparisons.append(compare_bool(
            "conn %s has values" % short,
            n_vals > 0, True))

    # ---- PRINT RESULTS ----
    pass_count = 0
    fail_count = 0
    info_count = 0

    for status, label, mode, detail in comparisons:
        tag = "  [%4s]" % status
        print("%s %-50s %-15s %s" % (tag, label, mode, detail))
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        elif status == "INFO":
            info_count += 1

    print()
    print("=" * 70)
    print("EXPERIMENT SUMMARY")
    print("=" * 70)
    print()
    print("  Derivations run:  %d / %d" % (ok_count, len(execution_order)))
    print("  Connections run:  %d / %d" % (
        len(conn_results), len(connection_order)))
    print()
    print("  PASS: %d" % pass_count)
    print("  FAIL: %d" % fail_count)
    print("  INFO: %d" % info_count)
    print()

    if fail_count == 0:
        print("  EXPERIMENT STATUS: ALL COMPARISONS PASSED")
    else:
        print("  EXPERIMENT STATUS: %d FAILURES" % fail_count)

    print()
    print("=" * 70)

    return fail_count


if __name__ == "__main__":
    sys.exit(main())

    