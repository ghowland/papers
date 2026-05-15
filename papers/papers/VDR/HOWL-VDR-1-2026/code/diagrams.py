    #!/usr/bin/env python3
"""
HOWL VDR-1-2026 Diagrams — VDR: Exact Finite Arithmetic in Irreducible Triple Form
8 figures covering drift comparison, convergence, matrix exactness,
discrete calculus, tree structure, rebase mechanics, and semantic distinction.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
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



outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# ================================================================
# FIG 1: FLOAT DRIFT VS VDR ZERO
# Type: Convergence chart (Type 1)
# Shows: The SHAPE of float error accumulation vs VDR exact zero.
#   Text can say "float drifts"; the curve shows HOW it grows.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Scalar Drift: Floating-Point vs VDR',
         'Number of Operations (add step, subtract step)',
         'Absolute Error from Original Value')

op_counts = [2, 10, 20, 50, 100, 200, 500, 1000, 2000]
float_errors = []
for n in op_counts:
    x = 1.0 / 7.0
    step = 1.0 / 13.0
    for _ in range(n):
        x = x + step
    for _ in range(n):
        x = x - step
    float_errors.append(abs(x - 1.0 / 7.0))

vdr_errors = [0.0] * len(op_counts)

ax.semilogy(op_counts, float_errors, 'o-', color=RED, linewidth=2.5,
            markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='float64', zorder=5)

# VDR line at a small positive value for visibility on log scale
vdr_display = [1e-20] * len(op_counts)
ax.semilogy(op_counts, vdr_display, 's-', color=GREEN, linewidth=2.5,
            markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='VDR (exact zero)', zorder=5)

ax.axhline(y=1e-15, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.6)
ax.text(op_counts[-1] * 0.95, 1.8e-15, 'machine epsilon',
        color=ORANGE, fontsize=9, ha='right', va='bottom')

ax.set_ylim(1e-21, 1e-13)
ax.set_xlim(0, op_counts[-1] * 1.08)

ax.fill_between([0, op_counts[-1] * 1.08], 1e-21, 1e-20,
                color=GREEN, alpha=0.06)
ax.text(op_counts[-1] * 0.5, 3e-21, 'VDR: exactly zero — no drift at any chain length',
        color=GREEN, fontsize=10, ha='center', va='bottom', fontstyle='italic')

legend = ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10, framealpha=0.9)

ax.text(op_counts[-1] * 0.95, float_errors[-1] * 1.5,
        'error = %.2e' % float_errors[-1],
        color=RED, fontsize=9, ha='right', va='bottom')

save(fig, 'vdr1_01_float_drift_vs_vdr.png')

# ================================================================
# FIG 2: NEWTON-RAPHSON SQRT(2) CONVERGENCE
# Type: Convergence chart (Type 1)
# Shows: Quadratic convergence — correct digits DOUBLING each step.
#   The exponential SHAPE of the curve is the finding.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

# Left panel: correct digits vs depth
depths = list(range(8))
# x_{n+1} = (x + 2/x) / 2, starting x=1
# compute exact fractions
from fractions import Fraction
x_nr = Fraction(1)
fracs = [x_nr]
for _ in range(7):
    x_nr = (x_nr + Fraction(2, 1) / x_nr) / 2
    fracs.append(x_nr)

import math
sqrt2_true = math.sqrt(2)
correct_digits = []
for f in fracs:
    err = abs(float(f) - sqrt2_true)
    if err == 0:
        correct_digits.append(120)  # cap for display
    elif err > 0:
        correct_digits.append(-math.log10(err))
    else:
        correct_digits.append(0)

style_ax(ax1, 'Newton-Raphson for ' + r'$\sqrt{2}$' + ': Convergence',
         'Iteration Depth', 'Correct Digits')

ax1.bar(depths, correct_digits, color=CYAN, alpha=0.7, edgecolor=CYAN,
        linewidth=1.5, width=0.6, zorder=3)

for i, d_val in enumerate(correct_digits):
    label = '>100' if d_val > 100 else '%.0f' % d_val
    y_pos = min(d_val, 100) + 3
    ax1.text(i, y_pos, label, color=WHITE, fontsize=9,
             ha='center', va='bottom', fontweight='bold')

# doubling reference line
ref_x = np.linspace(0, 7, 50)
ref_y = 0.4 * 2 ** ref_x
ax1.plot(ref_x, ref_y, '--', color=GOLD, linewidth=1.5, alpha=0.7,
         label='doubling reference')

ax1.set_ylim(0, 130)
ax1.set_xlim(-0.5, 7.5)
ax1.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE, fontsize=9)

# Right panel: x^2 - 2 error on log scale
x_sq_errors = []
for f in fracs:
    sq = f * f
    err = abs(sq - 2)
    if err == 0:
        x_sq_errors.append(1e-120)
    else:
        x_sq_errors.append(float(err))

style_ax(ax2, r'$x^2 - 2$' + ' Residual (Exact Rational)',
         'Iteration Depth', r'$|x^2 - 2|$')

ax2.semilogy(depths, x_sq_errors, 'o-', color=MAG, linewidth=2.5,
             markersize=12, markeredgecolor=WHITE, markeredgewidth=1.5,
             zorder=5)

for i, err in enumerate(x_sq_errors):
    if err > 1e-100:
        ax2.text(i + 0.15, err * 2, '1/%s' % str(fracs[i] * fracs[i] - 2).split('/')[1]
                 if '/' in str(fracs[i] * fracs[i] - 2) else str(fracs[i]*fracs[i]-2),
                 color=SILVER, fontsize=7, va='bottom')

ax2.set_ylim(1e-110, 1e2)
ax2.set_xlim(-0.5, 7.5)

ax2.axhline(y=1e-15, color=ORANGE, linestyle='--', linewidth=1, alpha=0.5)
ax2.text(7.3, 2e-15, 'float64\nlimit', color=ORANGE, fontsize=8, ha='right')

ax2.text(3.5, 1e-105, 'Every intermediate value is an exact rational.\nNo floats used in the computation.',
         color=GREEN, fontsize=10, ha='center', va='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

save(fig, 'vdr1_02_newton_sqrt2.png')

# ================================================================
# FIG 3: HILBERT MATRIX RESIDUAL
# Type: Convergence/divergence chart (Type 1)
# Shows: Float residual GROWING with matrix size while VDR stays
#   at exact zero. The diverging curves show WHY exact arithmetic matters.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, r'Hilbert Matrix $H \times H^{-1}$ Residual',
         'Matrix Size n', r'Max $|I - H \cdot H^{-1}|$ (off-diagonal)')

sizes = [2, 3, 4, 5, 6, 7, 8]

# compute float residuals using numpy
float_residuals = []
for n in sizes:
    H = np.array([[1.0 / (i + j + 1) for j in range(n)] for i in range(n)])
    try:
        Hi = np.linalg.inv(H)
        product = H @ Hi
        identity = np.eye(n)
        residual = np.max(np.abs(product - identity))
        float_residuals.append(residual)
    except Exception:
        float_residuals.append(1.0)

# VDR residuals are all exactly zero
vdr_residuals_display = [1e-20] * len(sizes)

ax.semilogy(sizes, float_residuals, 'D-', color=RED, linewidth=2.5,
            markersize=12, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='numpy float64', zorder=5)

ax.semilogy(sizes, vdr_residuals_display, 's-', color=GREEN, linewidth=2.5,
            markersize=12, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='VDR (exact zero)', zorder=5)

for i, (n, res) in enumerate(zip(sizes, float_residuals)):
    ax.text(n + 0.12, res * 5.5, '%.1e' % res,
            color=SILVER, fontsize=8, va='bottom')

ax.axhline(y=1e-15, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.6)
ax.text(sizes[-1] - 0.1, 2e-15, 'machine epsilon', color=ORANGE, fontsize=9,
        ha='right', va='bottom')

ax.fill_between([sizes[0] - 0.5, sizes[-1] + 0.5], 1e-21, 1e-19,
                color=GREEN, alpha=0.06)
ax.text(np.mean(sizes), 3e-21, 'VDR: every element of I exactly correct',
        color=GREEN, fontsize=10, ha='center', fontstyle='italic')

ax.set_ylim(1e-22, 1e2)
ax.set_xlim(sizes[0] - 0.5, sizes[-1] + 0.8)
ax.set_xticks(sizes)

legend = ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10)

# annotation for the gap
mid_n = 5
ax.annotate('', xy=(mid_n, float_residuals[sizes.index(mid_n)]),
            xytext=(mid_n, 1e-19),
            arrowprops=dict(arrowstyle='<->', color=GOLD, linewidth=2))
ax.text(mid_n + 0.2, 1e-12, 'gap = exact\nvs approximate',
        color=GOLD, fontsize=10, va='center')

save(fig, 'vdr1_03_hilbert_residual.png')

# ================================================================
# FIG 4: DISCRETE INTEGRAL CONVERGENCE
# Type: Convergence chart (Type 1)
# Shows: Left Riemann O(1/n) vs trapezoidal O(1/n^2) convergence
#   RATE visible from curve shapes. Both exact at every n.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, r'Discrete Integral of $x^2$ from 0 to 1: Convergence to $\frac{1}{3}$',
         'Number of Steps n', r'$|I_n - \frac{1}{3}|$')

ns = [5, 10, 20, 50, 100, 200, 500, 1000]

# left Riemann: sum_{k=0}^{n-1} (k/n)^2 * (1/n) = (n-1)(2n-1) / (6n^2)
# error from 1/3 = |left - 1/3|
left_errors = []
trap_errors = []
for n in ns:
    # exact left Riemann
    left = Fraction(0)
    h = Fraction(1, n)
    for k in range(n):
        xk = Fraction(k, n)
        left += xk * xk * h
    left_errors.append(abs(float(left - Fraction(1, 3))))

    # exact trapezoidal
    trap = Fraction(0) + Fraction(1)  # f(0) + f(1)
    for k in range(1, n):
        xk = Fraction(k, n)
        trap += 2 * xk * xk
    trap = trap * h / 2
    trap_errors.append(abs(float(trap - Fraction(1, 3))))

ax.loglog(ns, left_errors, 'o-', color=BLUE, linewidth=2.5,
          markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
          label='Left Riemann — O(1/n)', zorder=5)

ax.loglog(ns, trap_errors, 's-', color=CYAN, linewidth=2.5,
          markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
          label='Trapezoidal — O(1/n' + r'$^2$' + ')', zorder=5)

# reference slopes
ref_n = np.array([5, 1000])
ref_1n = 0.5 / ref_n
ref_1n2 = 0.02 / ref_n ** 2
ax.loglog(ref_n, ref_1n, '--', color=BLUE, linewidth=1, alpha=0.4)
ax.loglog(ref_n, ref_1n2, '--', color=CYAN, linewidth=1, alpha=0.4)

ax.set_ylim(min(trap_errors) * 0.3, max(left_errors) * 3)
ax.set_xlim(3, 1500)

# annotations for specific exact values
ax.text(12, left_errors[1] * 2.5, 'n=10: exactly 57/200',
        color=BLUE, fontsize=9, va='bottom')
ax.text(120, trap_errors[4] * 3, 'n=100: exactly 6667/20000',
        color=CYAN, fontsize=9, va='bottom')

ax.text(50, 2e-7, 'Every point is an exact VDR rational.\n'
        'Not a float approximation — the exact fraction.',
        color=GREEN, fontsize=10, ha='center', va='top',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

legend = ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10)

save(fig, 'vdr1_04_integral_convergence.png')

# ================================================================
# FIG 5: FINITE DIFFERENCE TABLE
# Type: Connection/integer map (Type 5)
# Shows: The PATTERN of differences collapsing to constants — third
#   differences of x^3 are exactly 6 everywhere, fourth exactly 0.
#   The visual grid shows the triangular structure text cannot convey.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
style_ax(ax, r'Finite Difference Table for $f(x) = x^3$ — Every Entry Exact', '', '')
ax.axis('off')

# data
f_vals = [0, 1, 8, 27, 64]
d1 = [f_vals[i+1] - f_vals[i] for i in range(4)]
d2 = [d1[i+1] - d1[i] for i in range(3)]
d3 = [d2[i+1] - d2[i] for i in range(2)]
d4 = [d3[i+1] - d3[i] for i in range(1)]

columns = [f_vals, d1, d2, d3, d4]
col_labels = ['f(x)', r'$\Delta f$', r'$\Delta^2 f$', r'$\Delta^3 f$', r'$\Delta^4 f$']
col_colors = [SILVER, BLUE, CYAN, GOLD, GREEN]
x_labels = ['x=0', 'x=1', 'x=2', 'x=3', 'x=4']

x_spacing = 2.5
y_spacing = 1.8
x_start = 1.0
y_start = 9.0

# column headers
for j, (label, color) in enumerate(zip(col_labels, col_colors)):
    ax.text(x_start + j * x_spacing, y_start + 1.5, label,
            color=color, fontsize=14, fontweight='bold', ha='center', va='center')

# x labels
for i, xl in enumerate(x_labels):
    ax.text(x_start - 1.5, y_start - i * y_spacing, xl,
            color=DIM, fontsize=11, ha='center', va='center')

# values in triangular grid
for j, (col, color) in enumerate(zip(columns, col_colors)):
    for i, val in enumerate(col):
        x = x_start + j * x_spacing
        y = y_start - (i + j * 0.5) * y_spacing

        # highlight constant differences
        if j == 3:  # delta^3
            box_color = GOLD
            box_alpha = 0.15
        elif j == 4:  # delta^4
            box_color = GREEN
            box_alpha = 0.15
        else:
            box_color = color
            box_alpha = 0.05

        bbox = mpatches.FancyBboxPatch(
            (x - 0.8, y - 0.55), 1.6, 1.1,
            boxstyle='round,pad=0.1',
            facecolor=box_color, edgecolor=color,
            alpha=box_alpha, linewidth=1.5, zorder=2
        )
        ax.add_patch(bbox)

        fontsize = 16 if j >= 3 else 14
        weight = 'bold' if j >= 3 else 'normal'
        ax.text(x, y, str(val), color=color, fontsize=fontsize,
                fontweight=weight, ha='center', va='center', zorder=3)

        # draw connecting lines to show derivation
        if j > 0 and i < len(columns[j-1]) - 1:
            x_prev = x_start + (j - 1) * x_spacing
            y_prev_top = y_start - (i + (j-1) * 0.5) * y_spacing
            y_prev_bot = y_start - (i + 1 + (j-1) * 0.5) * y_spacing
            ax.plot([x_prev + 0.85, x - 0.85], [y_prev_top - 0.2, y + 0.3],
                    color=DIM, linewidth=0.8, alpha=0.4, zorder=1)
            ax.plot([x_prev + 0.85, x - 0.85], [y_prev_bot + 0.2, y - 0.3],
                    color=DIM, linewidth=0.8, alpha=0.4, zorder=1)

# annotations
ax.text(x_start + 3 * x_spacing, y_start - 6.5 * y_spacing,
        r'$\Delta^3(x^3) = 6$ exactly',
        color=GOLD, fontsize=14, fontweight='bold', ha='center')
ax.text(x_start + 4 * x_spacing, y_start - 6.5 * y_spacing,
        r'$\Delta^4(x^3) = 0$ exactly',
        color=GREEN, fontsize=14, fontweight='bold', ha='center')

ax.text(x_start + 1.5 * x_spacing, y_start - 7.5 * y_spacing,
        'In float arithmetic, higher-order differences accumulate rounding error.\n'
        'In VDR, there is no noise floor. Every difference is exact.',
        color=SILVER, fontsize=11, ha='center', va='top')

ax.set_xlim(-1.5, x_start + 5 * x_spacing)
ax.set_ylim(y_start - 8.5 * y_spacing, y_start + 2.5)

save(fig, 'vdr1_05_finite_differences.png')

# ================================================================
# FIG 6: VDR TREE STRUCTURE
# Type: Geometric cross-section (Type 4)
# Shows: The tree NESTING of [1, 3, [1, 6, 0]] — parent node
#   branching through R to a child. Bracket notation cannot show
#   the spatial relationship between parent frame and child frame.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'VDR Object as Finite Tree', '', '')
ax.axis('off')

# draw two examples side by side

# LEFT: closed object [1, 2, 0]
def draw_node(ax, cx, cy, v, d, r_text, color, label=None, size=1.0):
    w = 3.0 * size
    h = 1.8 * size
    box = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle='round,pad=0.15',
        facecolor=PAN, edgecolor=color, linewidth=2, zorder=3
    )
    ax.add_patch(box)

    slot_w = w / 3.2
    slot_positions = [cx - w/3, cx, cx + w/3]
    slot_labels = [str(v), str(d), r_text]
    slot_names = ['V', 'D', 'R']
    slot_colors = [CYAN, BLUE, GOLD if r_text != '0' else DIM]

    for sx, sl, sn, sc in zip(slot_positions, slot_labels, slot_names, slot_colors):
        ax.text(sx, cy + 0.35 * size, sn, color=DIM, fontsize=8, ha='center', va='center')
        ax.text(sx, cy - 0.2 * size, sl, color=sc, fontsize=14 * size,
                fontweight='bold', ha='center', va='center', zorder=4)

    if label:
        ax.text(cx, cy + h/2 + 0.4 * size, label, color=color, fontsize=12,
                fontweight='bold', ha='center', va='bottom')

# LEFT SIDE: closed object
ax.text(4, 9.5, 'Closed Object', color=SILVER, fontsize=14, fontweight='bold', ha='center')
draw_node(ax, 4, 7.5, 1, 2, '0', SILVER, label='[1, 2, 0]')
ax.text(4, 5.5, 'R = 0\nFully settled\nProjects to 1/2', color=DIM, fontsize=10, ha='center')

# RIGHT SIDE: active object with child
ax.text(13, 9.5, 'Active Object with Child', color=SILVER, fontsize=14,
        fontweight='bold', ha='center')
draw_node(ax, 13, 7.5, 1, 3, 'child', GOLD, label='[1, 3, [1, 6, 0]]')

# arrow from R slot down to child
ax.annotate('', xy=(13 + 1.0, 6.6), xytext=(13 + 1.0, 5.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, linewidth=2))
ax.text(14.5, 6.05, 'R branches\nto child', color=GOLD, fontsize=9, ha='left')

# child node
draw_node(ax, 13, 4.2, 1, 6, '0', GREEN, size=0.85)
ax.text(13, 3.0, 'Child: [1, 6, 0]', color=GREEN, fontsize=10, ha='center')

# completion semantics
ax.text(13, 1.5,
        r'$\Pi = \frac{1 + 1/6}{3} = \frac{7/6}{3} = \frac{7}{18}$',
        color=CYAN, fontsize=13, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, alpha=0.8))

# general rule at bottom
ax.text(8.5, 0.2,
        'Recursion exists only in R.  V and D are always integers.  '
        'The tree branches through the third slot only.',
        color=SILVER, fontsize=11, ha='center', fontstyle='italic')

ax.set_xlim(0, 17)
ax.set_ylim(-0.5, 10.5)

save(fig, 'vdr1_06_tree_structure.png')

# ================================================================
# FIG 7: REBASE — DENOMINATOR-SENSITIVE COMPLETION
# Type: Geometric diagram (Type 4)
# Shows: The construction of [1, 3, [1, 2, 0]] from [1, 2, 0]
#   via rebase. The visual shows parent frame, mismatch, and child
#   completion — spatial structure text cannot convey.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, 'Rebase: Denominator-Sensitive Completion', '', '')
ax.axis('off')

# source object on the left
ax.text(2.5, 9.0, 'Source', color=SILVER, fontsize=13, fontweight='bold', ha='center')
draw_node(ax, 2.5, 7.5, 1, 2, '0', SILVER, size=1.0)
ax.text(2.5, 6.0, 'Projects to 1/2', color=DIM, fontsize=10, ha='center')

# big arrow
ax.annotate('', xy=(7.0, 7.5), xytext=(5.0, 7.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, linewidth=3))
ax.text(6.0, 8.2, 'rebase(target=3)', color=GOLD, fontsize=12,
        fontweight='bold', ha='center')

# construction steps in middle
step_x = 6.0
ax.text(9.5, 9.0, 'Construction', color=GOLD, fontsize=13, fontweight='bold', ha='center')

steps = [
    ('N = V ' + r'$\times$' + ' B = 1 ' + r'$\times$' + ' 3 = 3', SILVER),
    ('3 = Q ' + r'$\times$' + ' 2 + S', SILVER),
    ('Q = 1,   S = 1', CYAN),
    ('Mismatch witness: [S, D, 0] = [1, 2, 0]', GOLD),
]
for i, (text, color) in enumerate(steps):
    y = 7.8 - i * 1.0
    ax.text(9.5, y, text, color=color, fontsize=11, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN, edgecolor=DIM, alpha=0.8))

# result on the right
ax.text(15.5, 9.0, 'Result', color=GREEN, fontsize=13, fontweight='bold', ha='center')
draw_node(ax, 15.5, 7.5, 1, 3, 'child', GREEN, size=1.0)

ax.annotate('', xy=(15.5 + 1.0, 6.6), xytext=(15.5 + 1.0, 5.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, linewidth=2))

draw_node(ax, 15.5, 4.2, 1, 2, '0', GOLD, size=0.85)
ax.text(15.5, 3.1, 'Mismatch witness\n[1, 2, 0]', color=GOLD, fontsize=10, ha='center')

# projection verification
ax.text(15.5, 1.8, 'Projection check:', color=SILVER, fontsize=10, ha='center')
ax.text(15.5, 0.8,
        r'$\frac{1 + 1/2}{3} = \frac{3/2}{3} = \frac{1}{2}$' + '  ' + r'$\checkmark$',
        color=GREEN, fontsize=14, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.8))

# arrow from construction to result
ax.annotate('', xy=(13.5, 7.5), xytext=(12.0, 7.5),
            arrowprops=dict(arrowstyle='->', color=GREEN, linewidth=2.5))

ax.set_xlim(0, 18)
ax.set_ylim(0.0, 10.0)

save(fig, 'vdr1_07_rebase_completion.png')

# ================================================================
# FIG 8: ACTIVE VS CLOSED — THE REMAINDER MATTERS
# Type: Progression/distinction (Type 7)
# Shows: [2,5,1] and [3,5,0] as distinct objects despite same
#   scalar projection. The visual separation communicates the
#   semantic commitment that is VDR's key design decision.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'The Remainder Matters: Active ' + r'$\neq$' + ' Closed', '', '')
ax.axis('off')

# LEFT: active object [2, 5, 1]
ax.text(4.5, 9.2, 'Active Object', color=GOLD, fontsize=14, fontweight='bold', ha='center')

box1 = mpatches.FancyBboxPatch(
    (1.5, 5.0), 6.0, 3.5,
    boxstyle='round,pad=0.2',
    facecolor=PAN, edgecolor=GOLD, linewidth=2.5, zorder=2
)
ax.add_patch(box1)

ax.text(4.5, 7.8, '[2, 5, 1]', color=GOLD, fontsize=20, fontweight='bold',
        ha='center', va='center', zorder=3)

# slot breakdown
for i, (label, val, color) in enumerate([('V', '2', CYAN), ('D', '5', BLUE), ('R', '1', GOLD)]):
    x = 2.5 + i * 2.0
    ax.text(x, 6.8, label, color=DIM, fontsize=10, ha='center', zorder=3)
    ax.text(x, 6.0, val, color=color, fontsize=18, fontweight='bold', ha='center', zorder=3)
    rect = mpatches.FancyBboxPatch(
        (x - 0.6, 5.6), 1.2, 1.6,
        boxstyle='round,pad=0.1',
        facecolor=BG, edgecolor=color, linewidth=1.5, alpha=0.5, zorder=2
    )
    ax.add_patch(rect)

ax.text(4.5, 5.3, 'carries remainder state', color=GOLD, fontsize=10,
        ha='center', fontstyle='italic', zorder=3)

# RIGHT: closed object [3, 5, 0]
ax.text(13.5, 9.2, 'Closed Object', color=SILVER, fontsize=14, fontweight='bold', ha='center')

box2 = mpatches.FancyBboxPatch(
    (10.5, 5.0), 6.0, 3.5,
    boxstyle='round,pad=0.2',
    facecolor=PAN, edgecolor=SILVER, linewidth=2.5, zorder=2
)
ax.add_patch(box2)

ax.text(13.5, 7.8, '[3, 5, 0]', color=SILVER, fontsize=20, fontweight='bold',
        ha='center', va='center', zorder=3)

for i, (label, val, color) in enumerate([('V', '3', CYAN), ('D', '5', BLUE), ('R', '0', DIM)]):
    x = 11.5 + i * 2.0
    ax.text(x, 6.8, label, color=DIM, fontsize=10, ha='center', zorder=3)
    ax.text(x, 6.0, val, color=color, fontsize=18, fontweight='bold', ha='center', zorder=3)
    rect = mpatches.FancyBboxPatch(
        (x - 0.6, 5.6), 1.2, 1.6,
        boxstyle='round,pad=0.1',
        facecolor=BG, edgecolor=color if label != 'R' else DIM, linewidth=1.5, alpha=0.5, zorder=2
    )
    ax.add_patch(rect)

ax.text(13.5, 5.3, 'no remainder state', color=DIM, fontsize=10,
        ha='center', fontstyle='italic', zorder=3)

# CENTER: the comparison
ax.text(9.0, 7.0, r'$\neq$', color=RED, fontsize=40, fontweight='bold',
        ha='center', va='center', zorder=5)

# BOTTOM: both project to 3/5
ax.text(4.5, 3.5, r'$\Pi = \frac{2+1}{5} = \frac{3}{5}$',
        color=CYAN, fontsize=14, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, alpha=0.8))

ax.text(13.5, 3.5, r'$\Pi = \frac{3}{5}$',
        color=CYAN, fontsize=14, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, alpha=0.8))

ax.text(9.0, 3.5, 'same scalar\nprojection', color=SILVER, fontsize=11,
        ha='center', va='center')

# bottom message
ax.text(9.0, 1.5,
        'Same projection. Different objects.\n'
        'The remainder is structural state, not a pending simplification.\n'
        'This is the key semantic commitment of VDR.',
        color=WHITE, fontsize=12, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=1.5, alpha=0.9))

ax.set_xlim(0, 18)
ax.set_ylim(0.5, 10.0)

save(fig, 'vdr1_08_active_vs_closed.png')

# ================================================================
# SUMMARY
# ================================================================
print("\nAll figures saved:")
print("  vdr1_01_float_drift_vs_vdr.png")
print("  vdr1_02_newton_sqrt2.png")
print("  vdr1_03_hilbert_residual.png")
print("  vdr1_04_integral_convergence.png")
print("  vdr1_05_finite_differences.png")
print("  vdr1_06_tree_structure.png")
print("  vdr1_07_rebase_completion.png")
print("  vdr1_08_active_vs_closed.png")
