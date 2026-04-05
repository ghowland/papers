#!/usr/bin/env python3
"""
DATA-6 EXPERIMENT RUNNER v0.3
==============================
Generic runner that loads an experiment JSON from ./data/,
executes it against the value pool and derivation registry,
and writes a result JSON to ./data/.

Pre-flight validation, connection outputs into pool,
result run counter (never overwrites).
"""

import sys
import os
import json
import glob
import datetime

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction
from mpmath import mp

mp.dps = 100

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _data_6_derivations_v0 import (
    DERIVATION_INDEX_V0,
    CONNECTION_INDEX_V0,
)


from _data_6_derivations_more_v0 import (
    DERIVATION_MORE_INDEX_V0,
    CONNECTION_MORE_INDEX_V0,
)

# After the existing imports, merge:
DERIVATION_INDEX_V0.update(DERIVATION_MORE_INDEX_V0)
CONNECTION_INDEX_V0.update(CONNECTION_MORE_INDEX_V0)


# ================================================================
# JSON LOADER / SERIALIZER
# ================================================================

def _deserialize(obj):
    if isinstance(obj, dict):
        if obj.get("_type") == "Fraction":
            return Fraction(int(obj["num"]), int(obj["den"]))
        if obj.get("_type") == "mpf":
            return obj["value"]
        return {k: _deserialize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_deserialize(x) for x in obj]
    return obj


def _serialize_default(obj):
    if isinstance(obj, Fraction):
        return {"_type": "Fraction", "num": str(obj.numerator),
                "den": str(obj.denominator)}
    return str(obj)


def load_all_values(data_dir):
    nodes = []
    pattern = os.path.join(data_dir, "values_*.json")
    for path in sorted(glob.glob(pattern)):
        with open(path) as f:
            data = json.load(f)
        for node in data.get("nodes", []):
            nodes.append(_deserialize(node))
    return nodes


def load_experiment(name, data_dir):
    candidates = [
        os.path.join(data_dir, "experiment_%s.json" % name),
        os.path.join(data_dir, "%s.json" % name),
    ]
    if name.startswith("experiment_"):
        candidates.insert(0, os.path.join(data_dir, "%s.json" % name))

    for path in candidates:
        if os.path.exists(path):
            with open(path) as f:
                return _deserialize(json.load(f)), path
    raise FileNotFoundError(
        "No experiment file found for '%s'. Tried:\n  %s" % (
            name, "\n  ".join(candidates)))


# ================================================================
# VALUE POOL HELPERS
# ================================================================

def make_result_entry(key, value, source="derivation"):
    if isinstance(value, Fraction):
        vtype = "exact_fraction"
    elif isinstance(value, int):
        vtype = "exact_integer"
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
        "unit": "dimensionless",
        "source": source,
    }


def find_output(key, pool):
    for entry in reversed(pool):
        if entry["key"] == key:
            return entry["value"]
    return None


# ================================================================
# PRE-FLIGHT VALIDATION
# ================================================================

def preflight(experiment, pool, data_dir):
    """Check dependencies exist before execution. Warn, don't abort."""
    warnings = []

    by_key = {}
    for entry in pool:
        by_key[entry["key"]] = True

    deps = experiment.get("dependencies", {})

    for canonical, version in deps.get("values", {}).items():
        versioned = "%s_v%d" % (canonical, version)
        if versioned not in by_key:
            warnings.append("value missing: %s" % versioned)

    for deriv_key in experiment.get("execution_plan", []):
        if deriv_key not in DERIVATION_INDEX_V0:
            warnings.append("derivation missing: %s" % deriv_key)

    for conn_key in experiment.get("connections", []):
        if conn_key not in CONNECTION_INDEX_V0:
            warnings.append("connection missing: %s" % conn_key)

    return warnings


# ================================================================
# COMPARISON ENGINE
# ================================================================

def _to_mpf(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / mp.mpf(x.denominator)
    if isinstance(x, (int, str)):
        return mp.mpf(x)
    if isinstance(x, bool):
        return mp.mpf(1 if x else 0)
    if hasattr(x, "_mpf_"):
        return x
    return mp.mpf(str(x))


def _miss_pct(got_mpf, ref_mpf):
    if ref_mpf != 0:
        return abs(got_mpf - ref_mpf) / abs(ref_mpf) * 100
    return mp.mpf("0")


def run_comparison(spec, pool):
    output_key = spec["output_key"]
    mode = spec["match_mode"]
    label = spec.get("label", output_key)
    ref_source = spec.get("reference_source", "")

    got = find_output(output_key, pool)
    if got is None:
        return {
            "label": label, "output_key": output_key,
            "match_mode": mode, "status": "SKIP",
            "detail": "output not found in pool",
        }

    result = {
        "label": label, "output_key": output_key,
        "match_mode": mode, "reference_source": ref_source,
    }

    if mode == "exact":
        expected = spec["expected"]
        if got == expected:
            result["status"] = "PASS"
            result["detail"] = "exact match"
        else:
            result["status"] = "FAIL"
            result["detail"] = "expected %s got %s" % (expected, got)
        result["expected"] = str(expected)
        result["got"] = str(got)

    elif mode == "digits":
        expected_str = str(spec["expected"])
        digits = spec["digits"]
        got_mpf = _to_mpf(got)
        ref_mpf = mp.mpf(expected_str)
        got_s = mp.nstr(got_mpf, digits)
        ref_s = mp.nstr(ref_mpf, digits)
        miss = _miss_pct(got_mpf, ref_mpf)
        result["expected"] = expected_str
        result["got"] = mp.nstr(got_mpf, digits + 2)
        result["digits"] = digits
        result["miss_pct"] = mp.nstr(miss, 4)
        if got_s == ref_s:
            result["status"] = "PASS"
            result["detail"] = "%d-digit match, miss %s%%" % (
                digits, result["miss_pct"])
        else:
            result["status"] = "FAIL"
            result["detail"] = "%d digits: expected %s got %s miss %s%%" % (
                digits, ref_s, got_s, result["miss_pct"])

    elif mode == "range":
        lo = mp.mpf(str(spec["lo"]))
        hi = mp.mpf(str(spec["hi"]))
        got_mpf = _to_mpf(got)
        result["got"] = mp.nstr(got_mpf, 6)
        result["lo"] = str(spec["lo"])
        result["hi"] = str(spec["hi"])
        if lo <= got_mpf <= hi:
            result["status"] = "PASS"
            result["detail"] = "in [%s, %s]" % (spec["lo"], spec["hi"])
        else:
            result["status"] = "FAIL"
            result["detail"] = "%s not in [%s, %s]" % (
                result["got"], spec["lo"], spec["hi"])

    elif mode == "miss_pct":
        ref_str = str(spec["expected"])
        got_mpf = _to_mpf(got)
        ref_mpf = mp.mpf(ref_str)
        miss = _miss_pct(got_mpf, ref_mpf)
        result["status"] = "INFO"
        result["expected"] = ref_str
        result["got"] = mp.nstr(got_mpf, 8)
        result["miss_pct"] = mp.nstr(miss, 4)
        result["detail"] = "predicted %s ref %s miss %s%%" % (
            result["got"], ref_str, result["miss_pct"])

    elif mode == "bool":
        expected = spec["expected"]
        result["got"] = str(got)
        if got == expected:
            result["status"] = "PASS"
            result["detail"] = "bool match"
        else:
            result["status"] = "FAIL"
            result["detail"] = "expected %s got %s" % (expected, got)

    else:
        result["status"] = "SKIP"
        result["detail"] = "unknown match_mode: %s" % mode

    return result


# ================================================================
# RESULT FILE NAMING
# ================================================================

def next_result_path(exp_key, data_dir):
    """Find next available run number for result file."""
    run = 1
    while True:
        filename = "result_%s_run%03d.json" % (exp_key, run)
        path = os.path.join(data_dir, filename)
        if not os.path.exists(path):
            return path, filename
        run += 1


# ================================================================
# MAIN RUNNER
# ================================================================

def run_experiment(name, data_dir):
    experiment, exp_path = load_experiment(name, data_dir)
    exp_key = experiment["key"]

    print("=" * 70)
    print("DATA-6 RUNNER: %s" % exp_key)
    print("=" * 70)
    print()
    print("  Source: %s" % exp_path)
    print("  Mode:   %s" % experiment.get("experiment_mode", "standard"))
    print("  Purpose: %s" % experiment.get("purpose", ""))
    print()

    # ---- LOAD VALUES ----
    pool = load_all_values(data_dir)
    print("Loaded %d value nodes." % len(pool))
    print()

    # ---- PRE-FLIGHT ----
    warnings = preflight(experiment, pool, data_dir)
    if warnings:
        print("-" * 70)
        print("PRE-FLIGHT WARNINGS: %d" % len(warnings))
        print("-" * 70)
        for w in warnings:
            print("  [WARN] %s" % w)
        print()

    # ---- EXECUTION PLAN ----
    plan = experiment.get("execution_plan", [])
    print("-" * 70)
    print("EXECUTION PLAN: %d derivations" % len(plan))
    print("-" * 70)

    execution_log = []
    deriv_ok = 0
    deriv_err = 0

    for deriv_key in plan:
        fn = DERIVATION_INDEX_V0.get(deriv_key)
        if fn is None:
            print("  [SKIP] %-55s not found" % deriv_key)
            execution_log.append({"key": deriv_key, "status": "skip"})
            deriv_err += 1
            continue
        try:
            result = fn(pool)
        except Exception as e:
            print("  [ERROR] %-55s %s" % (deriv_key, e))
            execution_log.append({"key": deriv_key, "status": "error",
                                  "error": str(e)})
            deriv_err += 1
            continue

        outputs = result.get("outputs", {})
        for out_key, out_val in outputs.items():
            pool.append(make_result_entry(out_key, out_val,
                                          source=deriv_key))
        print("  [OK] %-55s %2d outputs" % (deriv_key, len(outputs)))
        execution_log.append({"key": deriv_key, "status": "ok",
                              "output_count": len(outputs)})
        deriv_ok += 1

    print()
    print("Derivations: %d OK, %d errors" % (deriv_ok, deriv_err))
    print()

    # ---- CONNECTIONS ----
    conn_keys = experiment.get("connections", [])
    conn_results_list = []

    if conn_keys:
        print("-" * 70)
        print("CONNECTIONS: %d bundles" % len(conn_keys))
        print("-" * 70)

        for conn_key in conn_keys:
            fn = CONNECTION_INDEX_V0.get(conn_key)
            if fn is None:
                print("  [SKIP] %-55s not found" % conn_key)
                continue
            try:
                cr = fn(pool)
            except Exception as e:
                print("  [ERROR] %-55s %s" % (conn_key, e))
                continue

            n_v = len(cr.get("named_values", {}))
            n_e = len(cr.get("edges", []))
            print("  [OK] %-55s %2d values, %2d edges" % (
                conn_key, n_v, n_e))
            conn_results_list.append(conn_key)

            # Merge connection named_values into pool
            for local_name, nv in cr.get("named_values", {}).items():
                source_key = nv.get("source_key", "")
                if source_key and find_output(source_key, pool) is None:
                    pool.append(make_result_entry(
                        source_key, nv.get("value"),
                        source=conn_key))

        print()

    # ---- EXPECTED OUTPUTS CHECK ----
    expected = experiment.get("expected_outputs", [])
    missing_outputs = []
    for eo in expected:
        eo_key = eo if eo.endswith("_v0") else eo + "_v0"
        if find_output(eo_key, pool) is None:
            missing_outputs.append(eo_key)

    if missing_outputs:
        print("WARNING: %d expected outputs missing:" % len(missing_outputs))
        for mo in missing_outputs:
            print("  - %s" % mo)
        print()

    # ---- COMPARISONS ----
    comp_specs = experiment.get("comparisons", [])
    comp_results = []

    if comp_specs:
        print("-" * 70)
        print("COMPARISONS: %d checks" % len(comp_specs))
        print("-" * 70)
        print()

        for spec in comp_specs:
            cr = run_comparison(spec, pool)
            comp_results.append(cr)
            tag = "  [%4s]" % cr["status"]
            print("%s %-50s %-15s %s" % (
                tag, cr["label"], cr["match_mode"], cr["detail"]))

        print()

    # ---- DIAGRAMS ----
    diagrams = experiment.get("diagrams", [])
    if diagrams:
        print("-" * 70)
        print("DIAGRAMS: %d specs (use 'data6.py diagram' to render)" % (
            len(diagrams)))
        print("-" * 70)
        for d in diagrams:
            print("  [SPEC] %-50s %s" % (
                d.get("key", "?"), d.get("title", "")))
        print()

    # ---- BUILD RESULT ----
    pass_count = sum(1 for c in comp_results if c["status"] == "PASS")
    fail_count = sum(1 for c in comp_results if c["status"] == "FAIL")
    info_count = sum(1 for c in comp_results if c["status"] == "INFO")
    skip_count = sum(1 for c in comp_results if c["status"] == "SKIP")

    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    all_outputs = {}
    for entry in pool:
        src = entry.get("source", "")
        if src in DERIVATION_INDEX_V0:
            all_outputs[entry["key"]] = entry["value"]

    result_node = {
        "key": "result_%s" % exp_key,
        "node_type": "result",
        "experiment_key": exp_key,
        "timestamp": timestamp,
        "status": "complete" if fail_count == 0 else "partial",
        "execution_log": execution_log,
        "connections_resolved": conn_results_list,
        "diagrams_produced": [],
        "comparison_results": comp_results,
        "outputs": all_outputs,
        "summary": {
            "derivations_ok": deriv_ok,
            "derivations_err": deriv_err,
            "comparisons_pass": pass_count,
            "comparisons_fail": fail_count,
            "comparisons_info": info_count,
            "comparisons_skip": skip_count,
        },
    }

    # ---- WRITE RESULT JSON (never overwrite) ----
    result_path, result_filename = next_result_path(exp_key, data_dir)
    with open(result_path, "w") as f:
        json.dump(result_node, f, indent=2, default=_serialize_default)
    print("Result written: %s" % result_filename)
    print()

    # ---- SUMMARY ----
    print("=" * 70)
    print("EXPERIMENT SUMMARY")
    print("=" * 70)
    print()
    print("  Derivations:  %d / %d" % (deriv_ok, len(plan)))
    print("  Connections:  %d / %d" % (len(conn_results_list), len(conn_keys)))
    print()
    print("  PASS: %d" % pass_count)
    print("  FAIL: %d" % fail_count)
    print("  INFO: %d" % info_count)
    print("  SKIP: %d" % skip_count)
    print()

    if fail_count == 0:
        print("  STATUS: ALL COMPARISONS PASSED")
    else:
        print("  STATUS: %d FAILURES" % fail_count)

    print()
    print("=" * 70)

    return fail_count
