#!/usr/bin/env python3
"""
DATA-6 DIAGRAM HELPER LIBRARY
===============================
Minimal-syntax helpers for creating publication-quality diagrams
from DATA-6 experiment results. Dark background, HOWL color palette.

No dependency on phys24_lib. All values accepted as Fraction, int,
str, float, or mpf — converted internally.

Import:
    from data_6_diagram_lib import *
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

from fractions import Fraction


# ================================================================
# INTERNAL CONVERTER
# ================================================================

def to_float(x):
    """Convert any numeric type to float for plotting."""
    if isinstance(x, Fraction):
        return float(x.numerator) / float(x.denominator)
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x)
    if hasattr(x, "_mpf_"):
        return float(x)
    return float(str(x))


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
        _outdir[0] = os.getcwd()
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

# Light mode
if True:
    # ── Global palette (Kindle / light mode) ──
    BG      = '#ffffff'
    PAN     = '#f0ede8'
    GOLD    = '#a07820'
    SILVER  = '#505860'
    CYAN    = '#1a8a80'
    MAG     = '#a03058'
    BLUE    = '#2855a0'
    GREEN   = '#2a7a3a'
    RED     = '#b82020'
    ORANGE  = '#c06a18'
    WHITE   = '#1a1a22'
    DIM     = '#908e88'
    PURPLE  = '#6040a0'
else:
    # ── Global palette (D7.2) ──
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


GAUGE_COLORS = [BLUE, GREEN, RED]
GAUGE_NAMES = ["U(1)", "SU(2)", "SU(3)"]

PALETTE = [CYAN, GREEN, BLUE, ORANGE, MAG, RED, PURPLE, GOLD]

COLOR_MAP = {
    "blue": BLUE, "green": GREEN, "red": RED,
    "cyan": CYAN, "gold": GOLD, "orange": ORANGE,
    "magenta": MAG, "mag": MAG, "purple": PURPLE,
    "silver": SILVER, "white": WHITE, "dim": DIM,
}


def resolve_color(name, index=0):
    """Resolve a color name or return palette color by index."""
    if name is None:
        return PALETTE[index % len(PALETTE)]
    if name.startswith("#"):
        return name
    return COLOR_MAP.get(name.lower(), PALETTE[index % len(PALETTE)])


# ================================================================
# FIGURE CREATION
# ================================================================

def dark_fig(title="", size=(16, 10), xlabel="", ylabel=""):
    """Create a styled figure with dark background."""
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
    """Create a styled dual-panel figure."""
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
            ax.set_title(title, color=GOLD, fontsize=13,
                         fontweight='bold', pad=10)
        ax.grid(True, alpha=0.1, color=DIM)
    return fig, ax1, ax2


def dark_canvas(title="", size=(16, 14)):
    """Create a styled figure with axis off for freeform drawing."""
    _fig_counter[0] += 1
    fig, ax = plt.subplots(figsize=size)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.axis('off')
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    return fig, ax


def save_fig(fig, filename):
    """Save and close figure."""
    for ax in fig.get_axes():
        ax.set_clip_on(True)
        for artist in ax.get_children():
            try:
                artist.set_clip_on(True)
            except Exception:
                pass
    path = os.path.join(get_outdir(), filename)
    fig.savefig(path, dpi=180, facecolor=BG,
                bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  [%d] Saved: %s" % (_fig_counter[0], filename))


# ================================================================
# DATA PLOTTING PRIMITIVES
# ================================================================

def measurement_band(ax, value, unc, label="", color=GOLD, label_x=None):
    """Draw a horizontal measurement band with 1-sigma and 3-sigma."""
    v = to_float(value)
    u = to_float(unc)
    ax.axhspan(v - u, v + u, color=color, alpha=0.15)
    ax.axhspan(v - 3*u, v + 3*u, color=color, alpha=0.05)
    ax.axhline(v, color=color, linewidth=2, alpha=0.8)
    if label:
        lx = label_x if label_x is not None else ax.get_xlim()[1] * 0.95
        ax.text(lx, v, label, color=color, fontsize=9,
                va='center', ha='right')
    return v


def measurement_band_v(ax, value, unc, label="", color=GOLD, label_y=None):
    """Vertical measurement band."""
    v = to_float(value)
    u = to_float(unc)
    ax.axvspan(v - u, v + u, color=color, alpha=0.15)
    ax.axvline(v, color=color, linewidth=2, alpha=0.8)
    if label:
        ly = label_y if label_y is not None else ax.get_ylim()[1] * 0.95
        ax.text(v, ly, label, color=color, fontsize=9,
                ha='center', va='top', rotation=90)
    return v


def threshold_line(ax, x, label="", color=ORANGE, vertical=True):
    """Draw a labeled threshold line."""
    x_val = to_float(x)
    if vertical:
        ax.axvline(x_val, color=color, linewidth=1.5,
                   linestyle=':', alpha=0.7)
        if label:
            yl = ax.get_ylim()
            ax.text(x_val, yl[1] * 0.97, label, color=color,
                    fontsize=8, ha='center', va='top')
    else:
        ax.axhline(x_val, color=color, linewidth=1.5,
                   linestyle=':', alpha=0.7)
        if label:
            xl = ax.get_xlim()
            ax.text(xl[1] * 0.97, x_val, label, color=color,
                    fontsize=8, ha='right', va='bottom')
    return x_val


def data_point(ax, x, y, label="", color=GREEN, marker='o', size=200):
    """Plot a single data point with white edge."""
    x_val = to_float(x)
    y_val = to_float(y)
    ax.scatter([x_val], [y_val], s=size, c=color, marker=marker,
               edgecolors=WHITE, linewidth=2, zorder=10)
    if label:
        ax.text(x_val, y_val, "  " + label, color=color, fontsize=9,
                va='center', ha='left')
    return (x_val, y_val)


def data_point_err(ax, x, y, yerr, label="", color=GREEN,
                   marker='o', size=200):
    """Plot a data point with error bar."""
    x_val = to_float(x)
    y_val = to_float(y)
    ye = to_float(yerr)
    ax.errorbar([x_val], [y_val], yerr=[ye], fmt='none', ecolor=color,
                elinewidth=2, capsize=5, capthick=2, zorder=9)
    ax.scatter([x_val], [y_val], s=size, c=color, marker=marker,
               edgecolors=WHITE, linewidth=2, zorder=10)
    if label:
        ax.text(x_val, y_val + ye * 1.3, label, color=color, fontsize=9,
                va='bottom', ha='center')
    return (x_val, y_val)


def measured_diamond(ax, x, y, label="", color=MAG, size=200):
    """Plot a measured value as a diamond."""
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
    """Plot running coupling curves."""
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
        colors = [PALETTE[i % len(PALETTE)] for i in range(len(values))]
    for i in range(len(values)):
        v = to_float(values[i])
        ax.bar(i, v, color=colors[i], alpha=0.7, edgecolor=colors[i],
               linewidth=2, width=width)
        if show_values:
            ax.text(i, v + abs(v) * 0.02, fmt % v, color=WHITE,
                    fontsize=10, ha='center', va='bottom', fontweight='bold')
    ax.set_xticks(list(range(len(values))))
    ax.set_xticklabels(labels, color=SILVER, fontsize=9)


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
# PHYSICS HELPERS
# ================================================================

def one_loop_run(inv_a0, b, log_mu0, log_mu_array):
    """One-loop running: returns numpy array of 1/alpha(mu)."""
    L_array = (log_mu_array - log_mu0) * np.log(10) / (2 * np.pi)
    return inv_a0 - b * L_array


def concentric_shells(ax, shells, center=(0, 0)):
    """Draw concentric circles. shells: list of (radius, label, color)."""
    for radius, label, color in shells:
        circle = plt.Circle(center, radius, fill=True, facecolor=color,
                             alpha=0.08, edgecolor=color, linewidth=2)
        ax.add_patch(circle)
        angle = 0.3 + 0.5 * (1.0 - radius / max(s[0] for s in shells))
        lx = center[0] + (radius + 0.03) * np.cos(angle)
        ly = center[1] + (radius + 0.03) * np.sin(angle)
        ax.text(lx + 0.06, ly, label, color=color, fontsize=9,
                ha='left', va='center', fontweight='bold')
        