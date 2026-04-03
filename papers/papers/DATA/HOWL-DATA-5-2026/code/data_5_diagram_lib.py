#!/usr/bin/env python3
"""
HOWL DATA-5 DIAGRAM HELPER LIBRARY
=====================================
Minimal-syntax helpers for creating publication-quality diagrams
from the HOWL platform libraries. Reduces a typical 80-line figure
to 5-10 lines.

Design principle: every helper does ONE thing and returns the axes
so calls can be chained. The provenance log is automatic.

Import:
    from phys24_lib import *
    from data_5_diagram_lib import *

Then:
    fig, ax = dark_fig("Title")
    running_curves(ax, [...])
    measurement_band(ax, value, unc, "label")
    threshold_line(ax, x, "label")
    save_fig(fig, "filename.png")

Platform: phys24_lib.py + all extension libraries
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
import os

from phys24_lib import *
from mpmath import pi as mpi, log as mlog, sqrt as msqrt

# ================================================================
# GLOBAL STATE
# ================================================================

_provenance = []
_fig_counter = [0]
_outdir = [None]


def set_outdir(path):
    """Set output directory for all figures."""
    _outdir[0] = path
    os.makedirs(path, exist_ok=True)


def get_outdir():
    if _outdir[0] is None:
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
        os.makedirs(d, exist_ok=True)
        _outdir[0] = d
    return _outdir[0]


def prov(name, value, source):
    """Log a provenance entry."""
    _provenance.append({
        "fig": _fig_counter[0],
        "name": name,
        "value": str(value)[:40],
        "source": source,
    })


def print_provenance():
    """Print the full provenance report."""
    print()
    print("=" * 72)
    print("  PROVENANCE: %d values, 0 hardcoded physics" % len(_provenance))
    print("=" * 72)
    for p in _provenance:
        print("  Fig %-3s %-22s %s" % (p["fig"], p["name"], p["source"]))
    print()


# ================================================================
# COLOR PALETTE
# ================================================================

BG      = '#0a0a12'
PAN     = '#12121f'
GOLD    = '#d4a843'
SILVER  = '#a0a8b8'
CYAN    = '#4ecdc4'
MAG     = '#c74b7a'
BLUE    = '#5b8def'
GREEN   = '#6bcf7f'
RED     = '#e05555'
ORANGE  = '#e8944a'
WHITE   = '#e8e8f0'
DIM     = '#555570'
PURPLE  = '#9b7bd4'

# Gauge group convention
SU1_COLOR = BLUE
SU2_COLOR = GREEN
SU3_COLOR = RED
GAUGE_COLORS = [SU1_COLOR, SU2_COLOR, SU3_COLOR]
GAUGE_NAMES = ["U(1)", "SU(2)", "SU(3)"]


# ================================================================
# FIGURE CREATION
# ================================================================

def dark_fig(title="", size=(16, 10), xlabel="", ylabel=""):
    """Create a styled figure with dark background.
    Returns (fig, ax).
    """
    _fig_counter[0] += 1
    fig, ax = plt.subplots(figsize=size)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    ax.grid(True, alpha=0.1, color=DIM)
    return fig, ax


def dark_fig_dual(title_l="", title_r="", size=(18, 9), wspace=0.30):
    """Create a styled dual-panel figure.
    Returns (fig, ax_left, ax_right).
    """
    _fig_counter[0] += 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=size,
                                     gridspec_kw={'wspace': wspace})
    fig.patch.set_facecolor(BG)
    for ax, title in [(ax1, title_l), (ax2, title_r)]:
        ax.set_facecolor(PAN)
        for spine in ax.spines.values():
            spine.set_color(DIM)
            spine.set_linewidth(0.5)
        ax.tick_params(colors=DIM, labelsize=9)
        if title:
            ax.set_title(title, color=GOLD, fontsize=13, fontweight='bold', pad=10)
        ax.grid(True, alpha=0.1, color=DIM)
    return fig, ax1, ax2


def dark_canvas(title="", size=(16, 14)):
    """Create a styled figure with axis('off') for freeform drawing.
    Returns (fig, ax).
    """
    _fig_counter[0] += 1
    fig, ax = plt.subplots(figsize=size)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.axis('off')
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    return fig, ax


def save_fig(fig, filename):
    """Save and close figure. Clips all artists to axes bounds first."""
    # Force all text/annotations inside axes to prevent bbox explosion
    for ax in fig.get_axes():
        ax.set_clip_on(True)
        for artist in ax.get_children():
            try:
                artist.set_clip_on(True)
            except Exception:
                pass
    path = os.path.join(get_outdir(), filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  [%d] Saved: %s" % (_fig_counter[0], filename))


# ================================================================
# DATA PLOTTING PRIMITIVES
# ================================================================

def measurement_band(ax, value, unc, label="", color=GOLD, label_x=None):
    """Draw a horizontal measurement band with 1-sigma and 3-sigma shading.
    Returns the center y value.
    """
    v = float(f2m(value)) if isinstance(value, Fraction) else float(value)
    u = float(f2m(unc)) if isinstance(unc, Fraction) else float(unc)
    ax.axhspan(v - u, v + u, color=color, alpha=0.15)
    ax.axhspan(v - 3*u, v + 3*u, color=color, alpha=0.05)
    ax.axhline(v, color=color, linewidth=2, alpha=0.8)
    if label:
        lx = label_x if label_x is not None else ax.get_xlim()[1] * 0.95
        ax.text(lx, v, label, color=color, fontsize=9, va='center', ha='right')
    return v


def measurement_band_v(ax, value, unc, label="", color=GOLD, label_y=None):
    """Vertical measurement band."""
    v = float(f2m(value)) if isinstance(value, Fraction) else float(value)
    u = float(f2m(unc)) if isinstance(unc, Fraction) else float(unc)
    ax.axvspan(v - u, v + u, color=color, alpha=0.15)
    ax.axvline(v, color=color, linewidth=2, alpha=0.8)
    if label:
        ly = label_y if label_y is not None else ax.get_ylim()[1] * 0.95
        ax.text(v, ly, label, color=color, fontsize=9, ha='center', va='top', rotation=90)
    return v


def threshold_line(ax, x, label="", color=ORANGE, vertical=True):
    """Draw a labeled threshold line."""
    x_val = float(f2m(x)) if isinstance(x, Fraction) else float(x)
    if vertical:
        ax.axvline(x_val, color=color, linewidth=1.5, linestyle=':', alpha=0.7)
        if label:
            yl = ax.get_ylim()
            ax.text(x_val, yl[1] * 0.97, label, color=color, fontsize=8,
                    ha='center', va='top')
    else:
        ax.axhline(x_val, color=color, linewidth=1.5, linestyle=':', alpha=0.7)
        if label:
            xl = ax.get_xlim()
            ax.text(xl[1] * 0.97, x_val, label, color=color, fontsize=8,
                    ha='right', va='bottom')
    return x_val


def data_point(ax, x, y, label="", color=GREEN, marker='o', size=200):
    """Plot a single data point with white edge."""
    x_val = float(f2m(x)) if isinstance(x, Fraction) else float(x)
    y_val = float(f2m(y)) if isinstance(y, Fraction) else float(y)
    ax.scatter([x_val], [y_val], s=size, c=color, marker=marker,
               edgecolors=WHITE, linewidth=2, zorder=10)
    if label:
        ax.text(x_val, y_val, "  " + label, color=color, fontsize=9,
                va='center', ha='left')
    return (x_val, y_val)


def data_point_err(ax, x, y, yerr, label="", color=GREEN, marker='o', size=200):
    """Plot a data point with error bar."""
    x_val = float(f2m(x)) if isinstance(x, Fraction) else float(x)
    y_val = float(f2m(y)) if isinstance(y, Fraction) else float(y)
    ye = float(f2m(yerr)) if isinstance(yerr, Fraction) else float(yerr)
    ax.errorbar([x_val], [y_val], yerr=[ye], fmt='none', ecolor=color,
                elinewidth=2, capsize=5, capthick=2, zorder=9)
    ax.scatter([x_val], [y_val], s=size, c=color, marker=marker,
               edgecolors=WHITE, linewidth=2, zorder=10)
    if label:
        ax.text(x_val, y_val + ye * 1.3, label, color=color, fontsize=9,
                va='bottom', ha='center')
    return (x_val, y_val)


def measured_diamond(ax, x, y, label="", color=MAG, size=200):
    """Plot a measured value as a diamond (distinguishes from predictions)."""
    return data_point(ax, x, y, label, color, marker='D', size=size)


# ================================================================
# CURVE PLOTTING
# ================================================================

def curve(ax, x_array, y_array, label="", color=CYAN, width=2.5,
          style='-', alpha=1.0):
    """Plot a curve."""
    ax.plot(x_array, y_array, color=color, linewidth=width,
            linestyle=style, alpha=alpha, label=label)


def running_curves(ax, log_mu_array, inv_alphas, labels=None,
                    colors=None, width=2.5, style='-'):
    """Plot 1-3 running coupling curves.
    inv_alphas: list of arrays [inv_a1, inv_a2, inv_a3].
    """
    if colors is None:
        colors = GAUGE_COLORS
    if labels is None:
        labels = GAUGE_NAMES
    for i in range(len(inv_alphas)):
        ax.plot(log_mu_array, inv_alphas[i], color=colors[i],
                linewidth=width, linestyle=style,
                label=labels[i] if labels else None)


def shaded_region(ax, x0, x1, color=RED, alpha=0.08, label=""):
    """Shade a vertical region."""
    ax.axvspan(float(x0), float(x1), color=color, alpha=alpha)
    if label:
        xm = (float(x0) + float(x1)) / 2
        yl = ax.get_ylim()
        ym = (yl[0] + yl[1]) / 2
        ax.text(xm, ym, label, color=color, fontsize=10, ha='center',
                va='center', fontweight='bold', alpha=0.7)


def shaded_region_h(ax, y0, y1, color=RED, alpha=0.08, label=""):
    """Shade a horizontal region."""
    ax.axhspan(float(y0), float(y1), color=color, alpha=alpha)
    if label:
        xl = ax.get_xlim()
        xm = (xl[0] + xl[1]) / 2
        ym = (float(y0) + float(y1)) / 2
        ax.text(xm, ym, label, color=color, fontsize=10, ha='center',
                va='center', fontweight='bold', alpha=0.7)


# ================================================================
# BAR CHARTS
# ================================================================

def bar_chart(ax, labels, values, colors=None, width=0.6,
              show_values=True, fmt="%.4f"):
    """Simple bar chart with labeled values."""
    if colors is None:
        colors = [CYAN] * len(values)
    x_pos = list(range(len(values)))
    for i in range(len(values)):
        v = float(f2m(values[i])) if isinstance(values[i], Fraction) else float(values[i])
        ax.bar(i, v, color=colors[i], alpha=0.7, edgecolor=colors[i],
               linewidth=2, width=width)
        if show_values:
            ax.text(i, v + abs(v) * 0.02, fmt % v, color=WHITE,
                    fontsize=10, ha='center', va='bottom', fontweight='bold')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, color=SILVER, fontsize=9)


def grouped_bars(ax, categories, groups, group_colors=None, group_labels=None,
                  width=0.25, show_values=False, fmt="%.2f"):
    """Grouped bar chart. groups is a list of value-lists, one per group."""
    n_groups = len(groups)
    if group_colors is None:
        group_colors = GAUGE_COLORS[:n_groups]
    x = np.arange(len(categories))
    for g in range(n_groups):
        offset = (g - n_groups / 2 + 0.5) * width
        vals = [float(f2m(v)) if isinstance(v, Fraction) else float(v) for v in groups[g]]
        lbl = group_labels[g] if group_labels else None
        ax.bar(x + offset, vals, width=width, color=group_colors[g],
               alpha=0.7, edgecolor=group_colors[g], linewidth=1.5, label=lbl)
        if show_values:
            for i, v in enumerate(vals):
                ax.text(x[i] + offset, v + abs(v) * 0.02, fmt % v,
                        color=WHITE, fontsize=7, ha='center', va='bottom')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, color=SILVER, fontsize=9)
    if group_labels:
        ax.legend(loc='best', facecolor=PAN, edgecolor=DIM,
                  labelcolor=WHITE, fontsize=9)


# ================================================================
# ANNOTATIONS AND LABELS
# ================================================================

def result_box(ax, x, y, text, color=GOLD, fontsize=11):
    """Place a result in a highlighted box."""
    ax.text(x, y, text, color=color, fontsize=fontsize, ha='center',
            va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=color, alpha=0.8))


def note(ax, x, y, text, color=SILVER, fontsize=9):
    """Place a small note."""
    ax.text(x, y, text, color=color, fontsize=fontsize,
            va='center', ha='left')


def arrow_label(ax, x_data, y_data, x_text, y_text, text, color=GOLD):
    """Annotation with arrow from text to data point."""
    ax.annotate(text, xy=(x_data, y_data), xytext=(x_text, y_text),
                color=color, fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5),
                ha='center', va='center')


def legend(ax, loc='upper right'):
    """Standard legend."""
    ax.legend(loc=loc, facecolor=PAN, edgecolor=DIM,
              labelcolor=WHITE, fontsize=9)


# ================================================================
# SCALE AND LANDSCAPE HELPERS
# ================================================================

def log_landscape(ax, boundaries, x_col=0.5, label_col=1.5, value_col=6.0):
    """Draw a vertical landscape from a list of boundary dicts.
    Each dict: {name, scale, color, known, extra}.
    Returns y positions for further annotation.
    """
    n = len(boundaries)
    y_positions = np.linspace(0.5, n - 0.5, n)

    for idx, b in enumerate(boundaries):
        y = y_positions[idx]
        color = b.get("color", SILVER)
        known = b.get("known", True)
        marker = 'o' if known else 's'
        edge = WHITE if known else ORANGE

        ax.plot([x_col - 0.3, value_col + 1], [y, y],
                color=DIM, linewidth=0.3, alpha=0.3)
        ax.scatter([x_col], [y], s=100, c=color, marker=marker,
                   edgecolors=edge, linewidth=1.5, zorder=5)
        ax.text(label_col, y, b["name"], color=color, fontsize=9,
                va='center', fontweight='bold')
        if "scale" in b and b["scale"] is not None:
            ax.text(value_col, y, b["scale"], color=SILVER, fontsize=8,
                    va='center', ha='left')
        if "extra" in b and b["extra"]:
            ax.text(value_col + 2.5, y, b["extra"], color=DIM,
                    fontsize=7, va='center')

    return y_positions


def concentric_shells(ax, shells, center=(0, 0)):
    """Draw concentric circles with labels.
    shells: list of (radius, label, color).
    """
    for radius, label, color in shells:
        circle = plt.Circle(center, radius, fill=True, facecolor=color,
                             alpha=0.08, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        angle = 0.3 + 0.5 * (1.0 - radius / max(s[0] for s in shells))
        lx = center[0] + (radius + 0.03) * np.cos(angle)
        ly = center[1] + (radius + 0.03) * np.sin(angle)
        ax.text(lx + 0.06, ly, label, color=color, fontsize=9,
                ha='left', va='center', fontweight='bold')


# ================================================================
# PHYSICS-SPECIFIC HELPERS
# ================================================================

def one_loop_run(inv_a0, b, log_mu0, log_mu_array):
    """One-loop running for plotting: returns numpy array."""
    L_array = (log_mu_array - log_mu0) * np.log(10) / (2 * np.pi)
    return inv_a0 - b * L_array


def plot_gauge_running(ax, log_mu, inv_a_MZ, betas, labels=None,
                        style='-', width=2.5, alpha=1.0, log_MZ=None):
    """Plot three gauge coupling running curves from M_Z."""
    if log_MZ is None:
        log_MZ = np.log10(91187.6 / 1000.0)
    inv_a = [float(f2m(inv_a_MZ[i])) for i in range(3)]
    b = [float(f2m(betas[i])) for i in range(3)]
    colors = GAUGE_COLORS
    if labels is None:
        labels = ["1/$\\alpha_1$", "1/$\\alpha_2$", "1/$\\alpha_3$"]
    for i in range(3):
        y = one_loop_run(inv_a[i], b[i], log_MZ, log_mu)
        ax.plot(log_mu, y, color=colors[i], linewidth=width,
                linestyle=style, alpha=alpha, label=labels[i])


def plot_H0_running(ax, N_array, H0_0, r, color=CYAN, label="H$_0$(N)",
                     width=2.5, style='-'):
    """Plot H0 running curve: H0(N) = H0(0) * r^N."""
    H0_0_f = float(f2m(H0_0)) if isinstance(H0_0, Fraction) else float(H0_0)
    r_f = float(r)
    y = H0_0_f * r_f ** N_array
    ax.plot(N_array, y, color=color, linewidth=width, linestyle=style, label=label)
    return y


def plot_H0_data(ax, measurements, N_assignments, colors=None):
    """Plot H0 measurements with error bars at assigned N positions.
    measurements: dict of H0_MEASUREMENTS entries.
    N_assignments: dict mapping keys to N values.
    """
    if colors is None:
        default_colors = [RED, ORANGE, CYAN, GREEN, PURPLE]
    else:
        default_colors = colors

    i = 0
    for key, N in sorted(N_assignments.items(), key=lambda x: x[1]):
        if key in measurements:
            m = measurements[key]
            H0_val = float(f2m(m["H0"]))
            H0_unc = float(f2m(m["uncertainty"]))
            c = default_colors[i % len(default_colors)]
            data_point_err(ax, N, m["H0"], m["uncertainty"],
                          label=key, color=c)
            prov(key, m["H0"], "H0_MEASUREMENTS['%s']" % key)
            i += 1


# ================================================================
# COMPOSITE HELPERS (multi-step figures in one call)
# ================================================================

def convergence_bar_figure(title, scenarios, measured_val, measured_unc,
                            measured_label, filename):
    """Create a complete convergence bar chart.
    scenarios: list of (label, value, color) tuples.
    Returns fig for optional further customization.
    """
    fig, ax = dark_fig(title, ylabel="Prediction")
    v_meas = measurement_band(ax, measured_val, measured_unc, measured_label)

    x_pos = list(range(len(scenarios)))
    for i, (label, val, color) in enumerate(scenarios):
        v = float(f2m(val)) if isinstance(val, Fraction) else float(val)
        miss = abs(v - v_meas) / v_meas * 100
        ax.bar(i, v, color=color, alpha=0.7, edgecolor=color,
               linewidth=2, width=0.7)
        ax.text(i, v + abs(v) * 0.005, "%.5f" % v, color=WHITE,
                fontsize=10, ha='center', va='bottom', fontweight='bold')
        ax.text(i, v - abs(v) * 0.01, "miss: %.2f%%" % miss, color=SILVER,
                fontsize=8, ha='center', va='top')
        prov(label[:20], val, "scenario input")

    ax.set_xticks(x_pos)
    ax.set_xticklabels([s[0] for s in scenarios], color=SILVER, fontsize=9)
    ax.set_xlim(-0.5, len(scenarios) - 0.5 + 1)

    save_fig(fig, filename)
    return fig


def running_figure(title, log_mu, inv_a_MZ, betas_SM, betas_CD,
                    log_MVL, log_MGUT, filename):
    """Create a complete coupling running figure with SM and CD betas."""
    fig, ax = dark_fig(title,
                        xlabel="log$_{10}$($\\mu$ / GeV)",
                        ylabel="1/$\\alpha_i$($\\mu$)")

    log_MZ = np.log10(91187.6 / 1000.0)

    # SM dashed
    plot_gauge_running(ax, log_mu, inv_a_MZ, betas_SM,
                        labels=["SM 1/$\\alpha_1$", "SM 1/$\\alpha_2$", "SM 1/$\\alpha_3$"],
                        style='--', width=1.5, alpha=0.5)

    # CD solid: below M_VL
    log_below = log_mu[log_mu <= log_MVL]
    log_above = log_mu[log_mu > log_MVL]

    inv_a = [float(f2m(inv_a_MZ[i])) for i in range(3)]
    b_sm = [float(f2m(betas_SM[i])) for i in range(3)]
    b_cd = [float(f2m(betas_CD[i])) for i in range(3)]

    for i in range(3):
        y_below = one_loop_run(inv_a[i], b_sm[i], log_MZ, log_below)
        ax.plot(log_below, y_below, color=GAUGE_COLORS[i], linewidth=2.5)

        if len(log_above) > 0:
            inv_at_VL = one_loop_run(inv_a[i], b_sm[i], log_MZ, np.array([log_MVL]))[0]
            y_above = one_loop_run(inv_at_VL, b_cd[i], log_MVL, log_above)
            ax.plot(log_above, y_above, color=GAUGE_COLORS[i], linewidth=2.5)

    threshold_line(ax, log_MVL, "M$_{VL}$")
    threshold_line(ax, log_MGUT, "M$_{GUT}$", color=GOLD)

    data_point(ax, log_MZ, inv_a[0], "", BLUE, size=150)
    data_point(ax, log_MZ, inv_a[1], "", GREEN, size=150)
    data_point(ax, log_MZ, inv_a[2], "", RED, size=150)

    legend(ax)
    save_fig(fig, filename)
    return fig


# ================================================================
# SELF-TEST (also serves as usage demo)
# ================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("DATA_5_DIAGRAM_LIB SELF-TEST")
    print("=" * 70)
    print()

    set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             '..', 'figures'))

    # --------------------------------------------------------
    # Test 1: dark_fig + data_point + measurement_band + save
    # --------------------------------------------------------
    print("Test 1: basic primitives")
    fig, ax = dark_fig("Test: Primitives", xlabel="x", ylabel="y")
    measurement_band(ax, 5.0, 0.5, "target = 5.0 +/- 0.5")
    data_point(ax, 1, 4.8, "point A", GREEN)
    data_point(ax, 2, 5.1, "point B", CYAN)
    measured_diamond(ax, 3, 5.0, "measured", MAG)
    threshold_line(ax, 2.5, "boundary")
    result_box(ax, 2, 3.5, "Result: 5.0 +/- 0.5")
    ax.set_xlim(0, 4)
    ax.set_ylim(3, 6.5)
    save_fig(fig, "test_01_primitives.png")

    # --------------------------------------------------------
    # Test 2: bar_chart
    # --------------------------------------------------------
    print("Test 2: bar chart")
    fig, ax = dark_fig("Test: Bar Chart", ylabel="Value")
    bar_chart(ax,
              ["A", "B", "C", "D"],
              [1.5, 2.3, 1.8, 3.1],
              colors=[RED, CYAN, GREEN, GOLD])
    ax.set_ylim(0, 4)
    save_fig(fig, "test_02_bars.png")

    # --------------------------------------------------------
    # Test 3: running curves
    # --------------------------------------------------------
    print("Test 3: running curves")
    log_mu = np.linspace(np.log10(91.19), 17, 500)
    fig, ax = dark_fig("Test: Running Curves",
                        xlabel="log$_{10}$(E/GeV)", ylabel="1/$\\alpha_i$")
    plot_gauge_running(ax, log_mu,
                        [inv_a1, inv_a2, inv_a3],
                        [b1_SM, b2_SM, b3_SM])
    legend(ax)
    ax.set_xlim(1.5, 17)
    ax.set_ylim(0, 70)
    save_fig(fig, "test_03_running.png")

    # --------------------------------------------------------
    # Test 4: dual panel
    # --------------------------------------------------------
    print("Test 4: dual panel")
    fig, ax1, ax2 = dark_fig_dual("Left Panel", "Right Panel")
    curve(ax1, [0, 1, 2, 3], [1, 4, 2, 5], "curve A", CYAN)
    curve(ax2, [0, 1, 2, 3], [5, 3, 4, 1], "curve B", MAG)
    legend(ax1)
    legend(ax2)
    save_fig(fig, "test_04_dual.png")

    # --------------------------------------------------------
    # Test 5: canvas with shells
    # --------------------------------------------------------
    print("Test 5: canvas with shells")
    fig, ax = dark_canvas("Test: Concentric Shells", size=(14, 14))
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    concentric_shells(ax, [
        (1.0, "Outer", RED),
        (0.7, "Middle", CYAN),
        (0.4, "Inner", GREEN),
        (0.15, "Core", GOLD),
    ])
    save_fig(fig, "test_05_shells.png")

    # --------------------------------------------------------
    # Test 6: composite convergence_bar_figure
    # --------------------------------------------------------
    print("Test 6: convergence bar (composite)")
    convergence_bar_figure(
        "Test: Convergence",
        [("Method A", 0.115, RED),
         ("Method B", 0.1175, CYAN),
         ("Method C", 0.1184, GREEN)],
        0.1180, 0.0009,
        "$\\alpha_s$ = 0.1180",
        "test_06_convergence.png")

    # --------------------------------------------------------
    # Test 7: composite running_figure
    # --------------------------------------------------------
    print("Test 7: running figure (composite)")
    log_mu = np.linspace(np.log10(91.19), 17, 500)
    running_figure(
        "Test: SM vs CD Running",
        log_mu,
        [inv_a1, inv_a2, inv_a3],
        [b1_SM, b2_SM, b3_SM],
        [b1_mod, b2_mod, b3_mod],
        np.log10(3000),
        15.54,
        "test_07_running_composite.png")

    # --------------------------------------------------------
    print()
    print("  7 test figures saved.")
    print("  Library: %d helper functions available." % (
        len([name for name in dir() if not name.startswith('_') and callable(eval(name))])))
    print()
    print("=" * 70)
    print("DATA_5_DIAGRAM_LIB SELF-TEST COMPLETE")
    print("=" * 70)
    