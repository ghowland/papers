#!/usr/bin/env python3
"""
DATA-6 DIAGRAM GENERATOR v0.3
===============================
Reads experiment JSON and result JSON from ./data/,
generates PNG diagrams to ./figures/.

Usage (via CLI):
    python data6.py diagram beta_unification_v0
"""

import sys
import os
import json
import glob
import numpy as np

try:
    sys.set_int_max_str_digits(1000000)
except Exception:
    pass

from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_6_diagram_lib import (
    dark_fig, dark_fig_dual, dark_canvas, save_fig, set_outdir,
    to_float, resolve_color, prov, print_provenance,
    bar_chart, measurement_band, threshold_line,
    data_point, measured_diamond, curve, running_curves, legend,
    result_box, note, arrow_label,
    one_loop_run,
    BG, PAN, GOLD, SILVER, CYAN, MAG, BLUE, GREEN, RED, ORANGE,
    WHITE, DIM, PURPLE, GAUGE_COLORS, GAUGE_NAMES, PALETTE,
)


# ================================================================
# LOADERS
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


def load_json(path):
    with open(path) as f:
        return _deserialize(json.load(f))


def find_file(name, directory, prefixes):
    for prefix in prefixes:
        path = os.path.join(directory, "%s%s.json" % (prefix, name))
        if os.path.exists(path):
            return path
    # Also try with run numbers for results
    for prefix in prefixes:
        pattern = os.path.join(directory, "%s%s_run*.json" % (prefix, name))
        matches = sorted(glob.glob(pattern))
        if matches:
            return matches[-1]  # latest run
    return None


def load_all_values(directory):
    values = {}
    pattern = os.path.join(directory, "values_*.json")
    for path in sorted(glob.glob(pattern)):
        with open(path) as f:
            data = _deserialize(json.load(f))
        for node in data.get("nodes", []):
            values[node["key"]] = node["value"]
    return values


def get_output(key, result_outputs, value_pool):
    if key in result_outputs:
        return result_outputs[key]
    if key in value_pool:
        return value_pool[key]
    return None


# ================================================================
# RENDERERS
# ================================================================

def render_bar(spec, result_outputs, value_pool):
    title = spec.get("title", "Bar Chart")
    categories = spec.get("categories", [])
    value_keys = spec.get("values_from", [])
    fig_notes = spec.get("notes", "")

    values = []
    colors = []
    valid_cats = []
    for i, key in enumerate(value_keys):
        v = get_output(key, result_outputs, value_pool)
        if v is not None:
            values.append(to_float(v))
            colors.append(PALETTE[i % len(PALETTE)])
            cat = categories[i] if i < len(categories) else key
            valid_cats.append(cat)
            prov(cat, v, key)
        else:
            print("    WARNING: %s not found, skipping bar" % key)

    if not values:
        print("    ERROR: no values found for bar chart")
        return None

    fig, ax = dark_fig(title, ylabel="Value", size=(16, 10))
    bar_chart(ax, valid_cats, values, colors=colors,
              show_values=True, fmt="%.5f")

    if len(values) >= 2:
        measured_val = values[-1]
        for i in range(len(values) - 1):
            if measured_val != 0:
                miss = abs(values[i] - measured_val) / abs(measured_val) * 100
                y_pos = min(values[i], measured_val) - abs(measured_val) * 0.05
                ax.text(i, y_pos, "miss: %.2f%%" % miss,
                        color=SILVER, fontsize=8, ha='center', va='top')

    if values:
        v_min = min(values)
        v_max = max(values)
        v_range = v_max - v_min if v_max != v_min else abs(v_max) * 0.1
        ax.set_ylim(v_min - v_range * 0.3, v_max + v_range * 0.15)
    ax.set_xlim(-0.5, len(values) - 0.5 + 0.5)

    if fig_notes:
        ax.text(0.5, -0.08, fig_notes, transform=ax.transAxes,
                color=DIM, fontsize=8, ha='center', va='top')

    return fig


def render_comparison_table(spec, result_outputs, value_pool):
    title = spec.get("title", "Predictions vs Measurements")
    rows = spec.get("rows", [])
    fig_notes = spec.get("notes", "")

    if not rows:
        print("    ERROR: no rows for comparison table")
        return None

    labels = []
    predicted_vals = []
    measured_vals = []
    miss_pcts = []

    for row in rows:
        pred_key = row.get("predicted", "")
        meas_str = row.get("measured", "0")
        label = row.get("label", pred_key)

        pred = get_output(pred_key, result_outputs, value_pool)
        if pred is None:
            print("    WARNING: %s not found, skipping row" % pred_key)
            continue

        pred_f = to_float(pred)
        meas_f = float(meas_str)

        if meas_f != 0:
            miss = abs(pred_f - meas_f) / abs(meas_f) * 100
        else:
            miss = 0.0

        labels.append(label)
        predicted_vals.append(pred_f)
        measured_vals.append(meas_f)
        miss_pcts.append(miss)
        prov(label, pred, pred_key)

    if not labels:
        print("    ERROR: no valid rows for comparison table")
        return None

    n = len(labels)
    fig_height = max(8, n * 1.2 + 3)
    fig, ax = dark_fig(title, xlabel="Value", size=(16, fig_height))

    y_pos = np.arange(n)
    bar_height = 0.35

    ax.barh(y_pos + bar_height / 2, predicted_vals, bar_height,
            color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=1.5,
            label="Predicted")
    ax.barh(y_pos - bar_height / 2, measured_vals, bar_height,
            color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=1.5,
            label="Measured")

    for i in range(n):
        x_max = max(predicted_vals[i], measured_vals[i])
        ax.text(x_max * 1.02, y_pos[i], "miss: %.3f%%" % miss_pcts[i],
                color=SILVER, fontsize=9, va='center', ha='left')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color=SILVER, fontsize=10)
    ax.invert_yaxis()
    legend(ax, loc='lower right')

    if fig_notes:
        ax.text(0.5, -0.06, fig_notes, transform=ax.transAxes,
                color=DIM, fontsize=8, ha='center', va='top')

    return fig


def render_line(spec, result_outputs, value_pool):
    title = spec.get("title", "Line Chart")
    source_deriv = spec.get("source_derivation", "")

    if "coupling" in source_deriv.lower() or "running" in title.lower():
        return render_coupling_running(spec, result_outputs, value_pool)

    fig_notes = spec.get("notes", "")
    x_axis = spec.get("x_axis", "x")
    y_axis = spec.get("y_axis", "y")
    series_specs = spec.get("series", [])

    fig, ax = dark_fig(title, xlabel=x_axis, ylabel=y_axis)

    for i, s in enumerate(series_specs):
        x_key = s.get("x_data", "")
        y_key = s.get("y_data", "")
        label = s.get("label", "series %d" % i)
        color = resolve_color(s.get("color"), i)

        x_data = get_output(x_key, result_outputs, value_pool)
        y_data = get_output(y_key, result_outputs, value_pool)

        if x_data is not None and y_data is not None:
            curve(ax, x_data, y_data, label=label, color=color)

    legend(ax)

    if fig_notes:
        ax.text(0.5, -0.06, fig_notes, transform=ax.transAxes,
                color=DIM, fontsize=8, ha='center', va='top')

    return fig


def render_coupling_running(spec, result_outputs, value_pool):
    title = spec.get("title", "Gauge Coupling Running")
    fig_notes = spec.get("notes", "")

    inv_a1 = get_output("coupling_alpha_1_inverse_gut_normalized_mz_v0",
                        result_outputs, value_pool)
    inv_a2 = get_output("coupling_alpha_2_inverse_mz_v0",
                        result_outputs, value_pool)
    inv_a3 = get_output("coupling_alpha_3_inverse_mz_v0",
                        result_outputs, value_pool)

    b1_sm = get_output("beta_sm_u1_total_v0", result_outputs, value_pool)
    b2_sm = get_output("beta_sm_su2_total_v0", result_outputs, value_pool)
    b3_sm = get_output("beta_sm_su3_total_v0", result_outputs, value_pool)

    b1_mod = get_output("beta_modified_u1_total_v0",
                        result_outputs, value_pool)
    b2_mod = get_output("beta_modified_su2_total_v0",
                        result_outputs, value_pool)
    b3_mod = get_output("beta_modified_su3_total_v0",
                        result_outputs, value_pool)

    missing = []
    for vname, val in [("inv_a1", inv_a1), ("inv_a2", inv_a2),
                        ("inv_a3", inv_a3),
                        ("b1_sm", b1_sm), ("b2_sm", b2_sm), ("b3_sm", b3_sm),
                        ("b1_mod", b1_mod), ("b2_mod", b2_mod),
                        ("b3_mod", b3_mod)]:
        if val is None:
            missing.append(vname)

    if missing:
        print("    ERROR: missing values for running: %s" % (
            ", ".join(missing)))
        return None

    inv_a = [to_float(inv_a1), to_float(inv_a2), to_float(inv_a3)]
    b_sm = [to_float(b1_sm), to_float(b2_sm), to_float(b3_sm)]
    b_cd = [to_float(b1_mod), to_float(b2_mod), to_float(b3_mod)]

    prov("inv_a1", inv_a1, "value_pool")
    prov("inv_a2", inv_a2, "value_pool")
    prov("inv_a3", inv_a3, "value_pool")

    log_MZ = np.log10(91.1876)
    log_mu = np.linspace(log_MZ, 17, 500)

    log_m_gut = get_output(
        "result_m_gut_one_loop_cabibbo_doublet_log10_gev_derived_v0",
        result_outputs, value_pool)

    log_MVL = np.log10(3000)
    log_MGUT = to_float(log_m_gut) if log_m_gut is not None else 15.5

    fig, ax = dark_fig(title,
                        xlabel="log$_{10}$($\\mu$ / GeV)",
                        ylabel="1/$\\alpha_i$($\\mu$)",
                        size=(16, 10))

    sm_labels = ["SM 1/$\\alpha_1$", "SM 1/$\\alpha_2$",
                 "SM 1/$\\alpha_3$"]
    for i in range(3):
        y = one_loop_run(inv_a[i], b_sm[i], log_MZ, log_mu)
        curve(ax, log_mu, y, label=sm_labels[i],
              color=GAUGE_COLORS[i], width=1.5, style='--', alpha=0.5)

    cd_labels = ["CD 1/$\\alpha_1$", "CD 1/$\\alpha_2$",
                 "CD 1/$\\alpha_3$"]
    log_below = log_mu[log_mu <= log_MVL]
    log_above = log_mu[log_mu > log_MVL]

    for i in range(3):
        y_below = one_loop_run(inv_a[i], b_sm[i], log_MZ, log_below)
        ax.plot(log_below, y_below, color=GAUGE_COLORS[i],
                linewidth=2.5, label=cd_labels[i])

        if len(log_above) > 0:
            inv_at_VL = one_loop_run(inv_a[i], b_sm[i], log_MZ,
                                      np.array([log_MVL]))[0]
            y_above = one_loop_run(inv_at_VL, b_cd[i], log_MVL, log_above)
            ax.plot(log_above, y_above, color=GAUGE_COLORS[i],
                    linewidth=2.5)

    threshold_line(ax, log_MZ, "M$_Z$", color=SILVER)
    threshold_line(ax, log_MVL, "M$_{VL}$", color=ORANGE)
    threshold_line(ax, log_MGUT, "M$_{GUT}$", color=GOLD)

    data_point(ax, log_MZ, inv_a[0], "", BLUE, size=150)
    data_point(ax, log_MZ, inv_a[1], "", GREEN, size=150)
    data_point(ax, log_MZ, inv_a[2], "", RED, size=150)

    ax.set_xlim(log_MZ - 0.5, 17)
    ax.set_ylim(0, 70)
    legend(ax, loc='upper left')

    if fig_notes:
        note(ax, log_MZ + 0.5, 5, fig_notes, color=DIM, fontsize=8)

    return fig


# ================================================================
# DISPATCHER
# ================================================================

RENDERERS = {
    "bar": render_bar,
    "line": render_line,
    "comparison_table": render_comparison_table,
}


def generate_diagrams(name, data_dir, figures_dir):
    exp_path = find_file(name, data_dir, ["experiment_", ""])
    if exp_path is None:
        print("ERROR: experiment JSON not found for '%s'" % name)
        return 1

    result_path = find_file(name, data_dir,
                            ["result_experiment_", "result_"])
    if result_path is None:
        print("ERROR: result JSON not found for '%s'" % name)
        return 1

    experiment = load_json(exp_path)
    result = load_json(result_path)

    exp_key = experiment.get("key", name)
    diagrams = experiment.get("diagrams", [])

    print("=" * 70)
    print("DATA-6 DIAGRAM GENERATOR")
    print("=" * 70)
    print()
    print("  Experiment: %s" % exp_key)
    print("  Experiment file: %s" % os.path.basename(exp_path))
    print("  Result file: %s" % os.path.basename(result_path))
    print("  Diagrams to render: %d" % len(diagrams))
    print()

    result_outputs = {}
    for key, val in result.get("outputs", {}).items():
        result_outputs[key] = val

    value_pool = load_all_values(data_dir)

    set_outdir(figures_dir)

    print("-" * 70)
    print("RENDERING")
    print("-" * 70)

    rendered = 0
    failed = 0

    for spec in diagrams:
        diagram_key = spec.get("key", "unknown")
        diagram_type = spec.get("type", "unknown")
        diagram_title = spec.get("title", "")

        print()
        print("  [%s] %s" % (diagram_type, diagram_title))

        renderer = RENDERERS.get(diagram_type)
        if renderer is None:
            print("    SKIP: unknown diagram type '%s'" % diagram_type)
            failed += 1
            continue

        try:
            fig = renderer(spec, result_outputs, value_pool)
        except Exception as e:
            print("    ERROR: %s" % e)
            failed += 1
            continue

        if fig is None:
            failed += 1
            continue

        filename = "%s.png" % diagram_key
        save_fig(fig, filename)
        rendered += 1

    print()
    print("=" * 70)
    print("DIAGRAM SUMMARY")
    print("=" * 70)
    print()
    print("  Rendered: %d / %d" % (rendered, len(diagrams)))
    if failed > 0:
        print("  Failed:   %d" % failed)
    print()

    print_provenance()

    print("=" * 70)

    return 0 if failed == 0 else 1
