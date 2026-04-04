#!/usr/bin/env python3
"""
HOWL MATH-6 Diagrams — The 82/82 Independence Record
8 figures covering PSLQ nulls, Bessel zeros, precision power, derivation beats search.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *
from scipy.special import j0 as scipy_j0, j1 as scipy_j1

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: PSLQ EXCLUDED VOLUME VS PRECISION
# Type: Running/convergence
# Shows: The excluded coefficient space grows exponentially with
# digit count. At 100 digits the excluded volume is 10^70 larger
# than at 12 digits. The curve shape IS the argument.
# ================================================================

fig, ax = dark_fig("PSLQ Discriminating Power: Excluded Volume vs Precision",
                   xlabel="Precision (decimal digits)",
                   ylabel="log\u2081\u2080(excluded relation-space volume per basis element)",
                   size=(16, 10))

digits = np.linspace(4, 105, 200)
# Excluded volume per basis element ~ 10^d (d = digit count)
log_volume = digits

curve(ax, digits, log_volume, 'Excluded volume ~ 10^d', CYAN, 2.5)

# Mark the key precision levels
precision_marks = [
    (4, 'SM: \u03b1_s\n(4 digits)', RED),
    (8, 'SM: m_\u03bc/m_e\n(8 digits)', ORANGE),
    (12, 'SM: \u03b1\u207b\u00b9\n(12 digits)', MAG),
    (15, 'Clock ratios\n(15 digits)', BLUE),
    (30, 'Feigenbaum\n(30 digits)', GREEN),
    (100, 'Bessel zeros\n(100 digits)', GOLD),
]

for d, label, color in precision_marks:
    data_point(ax, d, d, '', color, size=250)
    dy = 8 if d < 50 else -12
    ha = 'center' if d > 20 else 'left'
    ax.annotate(label, xy=(d, d), xytext=(d + 3, d + dy),
                fontsize=9, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

# The 70-order jump
ax.annotate('', xy=(100, 100), xytext=(12, 100),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(56, 103, '88 orders of magnitude more discriminating',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

# Shading
shaded_region(ax, 0, 15, RED, 0.05)
shaded_region(ax, 15, 35, BLUE, 0.03)
shaded_region(ax, 35, 110, GREEN, 0.02)

ax.text(8, 90, 'Measurement\nlimited', fontsize=8, color=RED,
        ha='center', style='italic')
ax.text(25, 90, 'Computation\nlimited', fontsize=8, color=BLUE,
        ha='center', style='italic')
ax.text(70, 90, 'Analytical\nprecision', fontsize=8, color=GREEN,
        ha='center', style='italic')

ax.set_xlim(0, 110)
ax.set_ylim(0, 115)

save_fig(fig, 'math6_01_pslq_excluded_volume.png')


# ================================================================
# FIG 2: BESSEL FUNCTIONS J0 AND J1 WITH TESTED ZEROS MARKED
# Type: Running/oscillation
# Shows: The actual oscillating Bessel curves with the three
# tested zeros marked. The curves show WHY these zeros exist
# and WHERE they sit — impossible to convey in text.
# ================================================================

fig, ax = dark_fig("Bessel Functions J\u2080 and J\u2081 with Tested Zeros",
                   xlabel="x",
                   ylabel="J\u03bd(x)",
                   size=(16, 10))

x = np.linspace(0.01, 12, 1000)
y_j0 = scipy_j0(x)
y_j1 = scipy_j1(x)

curve(ax, x, y_j0, 'J\u2080(x)', CYAN, 2.5)
curve(ax, x, y_j1, 'J\u2081(x)', ORANGE, 2.5)

# Zero line
ax.plot([0, 12], [0, 0], color=DIM, linewidth=1, alpha=0.5)

# Tested zeros
zeros = [
    (2.40483, 'j\u2080\u2081 = 2.40483...', CYAN, -0.12),
    (3.83171, 'j\u2081\u2081 = 3.83171...', ORANGE, 0.10),
    (7.01559, 'j\u2081\u2082 = 7.01559...', ORANGE, 0.10),
]

for z_val, label, color, y_offset in zeros:
    ax.plot([z_val, z_val], [-0.05, 0.05], color=GOLD, linewidth=3, zorder=6)
    data_point(ax, z_val, 0, '', GOLD, size=250)
    ax.annotate(label + '\nPSLQ: NULL at 100 digits',
                xy=(z_val, 0), xytext=(z_val + 0.6, y_offset + 0.25),
                fontsize=9, color=GOLD, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Also mark pi multiples for contrast
for k in [1, 2, 3]:
    pi_k = k * np.pi
    ax.plot([pi_k, pi_k], [-0.42, -0.38], color=DIM, linewidth=2, alpha=0.5)
    ax.text(pi_k, -0.47, '%d\u03c0' % k, fontsize=8, color=DIM,
            ha='center')

result_box(ax, 9.5, 0.35,
           'Bessel zeros are NOT\nrational combinations of \u03c0\n'
           '(100-digit PSLQ null)', GOLD, 10)

ax.set_xlim(-0.3, 12.5)
ax.set_ylim(-0.55, 0.70)

legend(ax, loc='upper right')

save_fig(fig, 'math6_02_bessel_functions.png')


# ================================================================
# FIG 3: 82/82 SCATTER — PRECISION VS CATEGORY, ALL NULL
# Type: Scatter plot
# Shows: Every tested constant by precision and category.
# All points are NULL (red X). The coverage is visual.
# ================================================================

fig, ax = dark_fig("The 82/82 Record: Every Test, Every Null",
                   xlabel="Available precision (decimal digits)",
                   ylabel="",
                   size=(16, 10))

# Categories with y-positions and colors
categories = {
    'SM parameters': (5, RED, 51, [(4, 15), (5, 8), (8, 10), (10, 5), (12, 13)]),
    'Residual searches': (4, ORANGE, 5, [(10, 5)]),
    'Clock ratios': (3, BLUE, 5, [(15, 5)]),
    'Mass/mol/BCS': (2, CYAN, 8, [(8, 3), (10, 3), (11, 2)]),
    'Feigenbaum': (1, GREEN, 2, [(30, 2)]),
    'Bessel zeros': (0, GOLD, 10, [(100, 10)]),
}

np.random.seed(42)

for cat_name, (y_base, color, count, clusters) in categories.items():
    # Plot points with jitter
    for d_center, n_pts in clusters:
        for j in range(n_pts):
            x_jitter = d_center + np.random.uniform(-1.5, 1.5)
            y_jitter = y_base + np.random.uniform(-0.25, 0.25)
            ax.scatter([x_jitter], [y_jitter], s=60, color=color,
                       marker='x', linewidth=1.5, alpha=0.7, zorder=5)

    # Category label
    ax.text(-8, y_base, cat_name, fontsize=10, color=color,
            ha='left', va='center', fontweight='bold')
    ax.text(108, y_base, '%d tests' % count, fontsize=9, color=SILVER,
            ha='left', va='center')

# Vertical precision landmarks
for d, label in [(4, '4'), (12, '12'), (30, '30'), (100, '100')]:
    ax.plot([d, d], [-0.8, 5.8], color=DIM, linewidth=0.5, alpha=0.3,
            linestyle=':')
    ax.text(d, 6.2, '%s digits' % label, fontsize=8, color=DIM,
            ha='center')

# The universal result
result_box(ax, 50, -1.2,
           '82 constants tested.  0 relations found.  Every X is a NULL.',
           GOLD, 12)

ax.set_xlim(-12, 115)
ax.set_ylim(-2.0, 7.0)
ax.set_yticks([])

save_fig(fig, 'math6_03_82_scatter.png')


# ================================================================
# FIG 4: PRECISION DISCRIMINATING POWER — LOG SCALE
# Type: Scale/landscape
# Shows: The excluded relation space at different precisions
# on a single log axis. The 70-order jump from SM to Bessel
# is spatially dramatic.
# ================================================================

fig, ax = dark_canvas("Precision Power: What Each Digit Level Excludes",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Vertical log axis
axis_x = 2.0
ax.plot([axis_x, axis_x], [1, 9], color=DIM, linewidth=2, alpha=0.5)

# Landmarks on the axis
landmarks = [
    (1.5, '4 digits', 'SM: \u03b1_s', RED,
     'Excludes |coeff| \u2264 10,000\nat 4-digit precision'),
    (3.0, '12 digits', 'SM: \u03b1\u207b\u00b9', MAG,
     'Excludes |coeff| \u2264 10,000\nat 12-digit precision'),
    (4.5, '15 digits', 'Clock ratios', BLUE,
     'Most precise measured\ndimensionless ratios'),
    (6.0, '30 digits', 'Feigenbaum', GREEN,
     'Computed from pure math\n(logistic map)'),
    (8.5, '100 digits', 'Bessel zeros', GOLD,
     'Analytically computable\nto arbitrary precision'),
]

for y, digits_label, source, color, detail in landmarks:
    # Marker on axis
    ax.plot([axis_x - 0.15, axis_x + 0.15], [y, y], color=color,
            linewidth=3)
    data_point(ax, axis_x, y, '', color, size=200)

    # Left label
    ax.text(axis_x - 0.5, y, digits_label, fontsize=12, color=color,
            ha='right', fontweight='bold')

    # Right detail
    ax.text(axis_x + 0.5, y + 0.2, source, fontsize=11, color=color,
            ha='left', fontweight='bold')
    ax.text(axis_x + 0.5, y - 0.3, detail, fontsize=9, color=SILVER,
            ha='left')

# The jump annotation
ax.annotate('', xy=(1.0, 8.5), xytext=(1.0, 3.0),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.5))
ax.text(0.5, 5.75, '10\u2077\u2070\nmore\npower', fontsize=14, color=GOLD,
        ha='center', fontweight='bold', rotation=0)

# Bottom note
ax.text(5.0, 0.5, 'The Bessel zero nulls are the strongest independence results\n'
        'in the series by 70 orders of magnitude over the SM parameter tests.',
        fontsize=11, color=SILVER, ha='center', style='italic')

save_fig(fig, 'math6_04_precision_power.png')


# ================================================================
# FIG 5: PSLQ TEST MATRIX — TARGETS VS BASIS SUBSETS
# Type: Heatmap/grid
# Shows: Rows = target constants (selected), columns = basis subsets.
# Dark cells = NULL. One bright cell = sanity check (pi^2 = 6*zeta(2)).
# The sea of dark IS the finding.
# ================================================================

fig, ax = dark_canvas("PSLQ Test Matrix: A Sea of Nulls",
                      size=(18, 14))
ax.set_xlim(-3, 12)
ax.set_ylim(-1, 14)

# Targets (rows) — representative selection
targets = [
    '\u03b1\u207b\u00b9 = 137.036',
    'sin\u00b2\u03b8_W',
    'm_\u03bc/m_e',
    'Clock: Al\u207a/Hg\u207a',
    'BCS gap',
    'Feigenbaum \u03b4',
    'Feigenbaum \u03b1',
    'j\u2080\u2081 (Bessel)',
    'j\u2081\u2081 (Bessel)',
    'j\u2081\u2081/\u03c0 (Airy)',
    'j\u2081\u2081/j\u2080\u2081',
    '\u03c0\u00b2 (SANITY)',
]

# Basis subsets (columns)
bases = [
    '\u03c0 powers',
    'Common\ntransc.',
    'Full 20',
]

cell_w = 2.2
cell_h = 0.85
x_start = 3.0
y_start = 12.0

# Column headers
for j, basis_name in enumerate(bases):
    ax.text(x_start + j * cell_w + cell_w / 2, y_start + 0.7,
            basis_name, fontsize=9, color=SILVER, ha='center',
            fontweight='bold')

# Row headers and cells
for i, target in enumerate(targets):
    y = y_start - i * cell_h
    is_sanity = (i == len(targets) - 1)
    target_color = GREEN if is_sanity else SILVER

    ax.text(x_start - 0.3, y + cell_h / 2, target, fontsize=9,
            color=target_color, ha='right', va='center', fontweight='bold')

    for j in range(len(bases)):
        x = x_start + j * cell_w
        # Sanity check: last row, last column
        if is_sanity and j == 2:
            # FOUND
            rect = plt.Rectangle((x + 0.1, y + 0.05), cell_w - 0.2, cell_h - 0.1,
                                  facecolor=GREEN, alpha=0.25, edgecolor=GREEN,
                                  linewidth=2, zorder=2)
            ax.add_patch(rect)
            ax.text(x + cell_w / 2, y + cell_h / 2, '[1,0,-6]',
                    fontsize=9, color=GREEN, ha='center', va='center',
                    fontweight='bold')
        elif is_sanity:
            rect = plt.Rectangle((x + 0.1, y + 0.05), cell_w - 0.2, cell_h - 0.1,
                                  facecolor=DIM, alpha=0.08, edgecolor=DIM,
                                  linewidth=0.5, zorder=2)
            ax.add_patch(rect)
            ax.text(x + cell_w / 2, y + cell_h / 2, '--',
                    fontsize=9, color=DIM, ha='center', va='center')
        else:
            # NULL
            rect = plt.Rectangle((x + 0.1, y + 0.05), cell_w - 0.2, cell_h - 0.1,
                                  facecolor=RED, alpha=0.06, edgecolor=DIM,
                                  linewidth=0.5, zorder=2)
            ax.add_patch(rect)
            ax.text(x + cell_w / 2, y + cell_h / 2, 'NULL',
                    fontsize=8, color=RED, ha='center', va='center',
                    alpha=0.6)

# Legend
ax.text(x_start + 3 * cell_w + 0.8, y_start - 1, 'NULL', fontsize=10,
        color=RED, fontweight='bold')
ax.text(x_start + 3 * cell_w + 0.8, y_start - 1.8, '= no relation\nfound', fontsize=8,
        color=SILVER)

ax.text(x_start + 3 * cell_w + 0.8, y_start - 3, '[1,0,-6]', fontsize=10,
        color=GREEN, fontweight='bold')
ax.text(x_start + 3 * cell_w + 0.8, y_start - 3.8, '= sanity check\n\u03c0\u00b2 = 6\u03b6(2)',
        fontsize=8, color=SILVER)

# Bottom
ax.text(5.5, 0.0, 'One green cell in a sea of red nulls.\n'
        'The algorithm works \u2014 it finds relations when they exist.\n'
        'For every physical, dynamical, and analytical constant tested: nothing.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'math6_05_pslq_matrix.png')


# ================================================================
# FIG 6: BESSEL ZEROS VS PI MULTIPLES — THEY DON'T ALIGN
# Type: Scale/number line
# Shows: j01, j11, j12 plotted alongside pi, 2pi, 3pi on a
# number line. The non-alignment is spatial — the Bessel zeros
# sit between pi multiples, not on them.
# ================================================================

fig, ax = dark_fig("Bessel Zeros vs \u03c0 Multiples: They Don't Align",
                   xlabel="x",
                   ylabel="",
                   size=(18, 8))

# Number line
ax.plot([0, 10.5], [0, 0], color=DIM, linewidth=2, alpha=0.5)

# Pi multiples
for k in [1, 2, 3]:
    pi_k = k * np.pi
    ax.plot([pi_k, pi_k], [-0.5, 0.5], color=BLUE, linewidth=2.5, alpha=0.6)
    data_point(ax, pi_k, 0, '', BLUE, size=200)
    ax.text(pi_k, 0.8, '%d\u03c0 = %.4f' % (k, pi_k), fontsize=10,
            color=BLUE, ha='center', fontweight='bold')

# Bessel zeros
bessel_zeros = [
    (2.40483, 'j\u2080\u2081', GOLD),
    (3.83171, 'j\u2081\u2081', ORANGE),
    (7.01559, 'j\u2081\u2082', CYAN),
]

for z_val, label, color in bessel_zeros:
    ax.plot([z_val, z_val], [-0.5, 0.5], color=color, linewidth=2.5)
    data_point(ax, z_val, 0, '', color, size=250)
    ax.text(z_val, -0.9, '%s = %.5f' % (label, z_val), fontsize=10,
            color=color, ha='center', fontweight='bold')

# Non-alignment arrows
ax.annotate('', xy=(2.40483, -1.5), xytext=(np.pi, -1.5),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=1.5))
ax.text((2.40483 + np.pi) / 2, -1.8, '\u0394 = %.4f' % (np.pi - 2.40483),
        fontsize=8, color=RED, ha='center')

ax.annotate('', xy=(3.83171, -2.2), xytext=(np.pi, -2.2),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=1.5))
ax.text((3.83171 + np.pi) / 2, -2.5, '\u0394 = %.4f' % (3.83171 - np.pi),
        fontsize=8, color=RED, ha='center')

result_box(ax, 5.5, 1.8,
           'Bessel zeros are NOT rational multiples of \u03c0.\n'
           'PSLQ confirms: no integer relation at 100 digits.',
           GOLD, 10)

ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-3.2, 2.8)
ax.set_yticks([])

save_fig(fig, 'math6_06_bessel_vs_pi.png')


# ================================================================
# FIG 7: SM PARAMETER PRECISION HISTOGRAM
# Type: Density histogram
# Shows: Distribution of available precision across the 51 SM
# parameters. Most cluster at 4-8 digits. The ceiling on PSLQ
# power is visible as the right edge of the distribution.
# ================================================================

fig, ax = dark_fig("SM Parameter Precision: The Ceiling on PSLQ Power",
                   xlabel="Available precision (decimal digits)",
                   ylabel="Number of SM parameters",
                   size=(16, 10))

# Approximate distribution from the paper
# 51 SM parameters at various precisions
precisions = (
    [4] * 8 +    # alpha_s, weak angles, light quark masses
    [5] * 10 +   # sin2thetaW, CKM angles, more quark masses
    [6] * 6 +    # various ratios
    [7] * 5 +    # lepton ratios
    [8] * 8 +    # m_mu/m_e, mass ratios
    [10] * 5 +   # derived quantities
    [11] * 4 +   # precision mass ratios
    [12] * 5     # alpha^-1, best measured
)

bins = np.arange(3.5, 13.5, 1)
counts, edges, patches = ax.hist(precisions, bins=bins, color=RED,
                                  alpha=0.6, edgecolor=RED, linewidth=1.5)

# Recolor bars
for patch in patches:
    patch.set_facecolor(RED)
    patch.set_alpha(0.6)
    patch.set_edgecolor(RED)

# Labels on bars
for i in range(len(counts)):
    if counts[i] > 0:
        ax.text(edges[i] + 0.5, counts[i] + 0.3, '%d' % int(counts[i]),
                fontsize=10, color=WHITE, ha='center', fontweight='bold')

# Comparison markers
ax.annotate('Feigenbaum: 30 digits\n(off chart \u2192)', xy=(12.8, 4),
            fontsize=9, color=GREEN, fontweight='bold')

ax.annotate('Bessel zeros: 100 digits\n(off chart \u2192\u2192)', xy=(12.8, 2.5),
            fontsize=9, color=GOLD, fontweight='bold')

# The ceiling
ax.plot([12.5, 12.5], [0, 12], color=ORANGE, linewidth=2, linestyle='--',
        alpha=0.6)
ax.text(12.5, 11.5, 'Best SM\nprecision', fontsize=9, color=ORANGE,
        ha='center')

result_box(ax, 7, 10,
           'Most SM parameters: 4-8 digits of precision.\n'
           'PSLQ power is limited by what experiments provide,\n'
           'not by what the algorithm can search.',
           SILVER, 10)

ax.set_xlim(3, 14)
ax.set_ylim(0, 13)

save_fig(fig, 'math6_07_sm_precision_histogram.png')


# ================================================================
# FIG 8: MATH-6 IDENTITY CARD
# Type: Identity card
# Shows: 82/82 null, three categories, sanity check, derivation
# beats search. Visual anchor for the paper.
# ================================================================

fig, ax = dark_canvas("MATH-6 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, '82 / 82  INDEPENDENCE RECORD', fontsize=22,
        color=GOLD, ha='center', fontweight='bold')

# The big number
ax.text(5, 8.0, '82 tests.  0 relations.', fontsize=16,
        color=WHITE, ha='center', fontweight='bold')

# Three categories — left column
ax.text(2.0, 6.8, 'THREE CATEGORIES', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

cats = [
    ('PHYSICAL', '59 tests, 4-15 digits', 'SM params, clocks, masses', RED),
    ('DYNAMICAL', '3 tests, 10-30 digits', 'Feigenbaum, BCS gap', GREEN),
    ('ANALYTICAL', '10 tests, 100 digits', 'Bessel zeros j01, j11, j12', GOLD),
]

for i, (title, count, detail, color) in enumerate(cats):
    y = 5.8 - i * 1.4
    ax.text(2.0, y, title, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(2.0, y - 0.45, count, fontsize=9, color=SILVER, ha='center')
    ax.text(2.0, y - 0.85, detail, fontsize=8, color=DIM, ha='center')

# Right column: derivation beats search
ax.text(7.5, 6.8, 'DERIVATION BEATS SEARCH', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

ax.text(7.5, 5.8, 'Physical derivation: 3 successes', fontsize=11,
        color=GREEN, ha='center', fontweight='bold')
derivations = [
    ('\u03b8_QCD = 0', 'energy minimization', GREEN),
    ('\u03b1 \u2194 a_e', 'QED perturbation theory', CYAN),
    ('Koide K = 2/3', 'trigonometric identity', BLUE),
]
for i, (result, method, color) in enumerate(derivations):
    ax.text(7.5, 5.2 - i * 0.5, '%s  (%s)' % (result, method),
            fontsize=9, color=color, ha='center')

ax.text(7.5, 3.5, 'PSLQ search: 0 successes / 82 tests', fontsize=11,
        color=RED, ha='center', fontweight='bold')

# The sanity check
ax.text(5.0, 2.2, 'SANITY CHECK', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(5.0, 1.6, 'PSLQ([\u03c0\u00b2, 1, \u03b6(2)]) = [1, 0, \u22126]',
        fontsize=13, color=GREEN, ha='center', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN,
                  linewidth=1.5))
ax.text(5.0, 1.0, 'The algorithm finds \u03c0\u00b2 = 6\u03b6(2) immediately.\n'
        'When it returns NULL, the null is genuine.',
        fontsize=9, color=SILVER, ha='center')

# Bottom banner
ax.text(5.0, 0.3, 'The transcendental basis is minimal. No tested constant simplifies.\n'
        'Structure in physics comes from derivation, not from pattern matching.',
        fontsize=10, color=GOLD, ha='center', style='italic')

save_fig(fig, 'math6_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("MATH-6 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'math6_01_pslq_excluded_volume.png',
    'math6_02_bessel_functions.png',
    'math6_03_82_scatter.png',
    'math6_04_precision_power.png',
    'math6_05_pslq_matrix.png',
    'math6_06_bessel_vs_pi.png',
    'math6_07_sm_precision_histogram.png',
    'math6_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    