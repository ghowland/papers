#!/usr/bin/env python3
"""
HOWL MATH-2 Diagrams — Integer-Pair Representations at Sub-Planck Precision
8 figures covering convergence, precision threshold, tiers, and the integer pair concept.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: CONVERGENCE RATE COMPARISON — 6 SERIES TYPES
# Type: Running/convergence
# Shows: Why some constants are Tier 1 and gamma is Tier 2.
# The curve SHAPES show the convergence classes — supergeometric
# racing ahead, unaccelerated flat. Impossible in text.
# ================================================================

fig, ax = dark_fig("Convergence Classes: Why Some Constants Are Tier 1 and \u03b3 Is Not",
                   xlabel="Number of terms / iterations",
                   ylabel="Correct decimal digits")

n = np.arange(1, 101)

# Supergeometric: e via Taylor. Digits ~ sum(log10(k)) ~ k*log10(k/e)
# Approximate: at term k, error ~ 1/k!, digits ~ log10(k!)
digits_e = np.array([sum(np.log10(np.arange(1, k+1))) if k > 0 else 0
                      for k in range(1, 101)])
digits_e = np.minimum(digits_e, 250)

# Quadratic: Newton sqrt. Digits double each iteration.
n_newton = np.arange(1, 12)
digits_newton = 2.0 ** n_newton
digits_newton = np.minimum(digits_newton, 250)

# Geometric fast: pi via Machin. ~1.4 digits/term
digits_pi = 1.4 * n

# Geometric moderate: zeta(3) via CBC. ~0.6 digits/term
digits_z3 = 0.6 * n

# Accelerated alternating: Catalan via Euler. ~0.3 digits/term
digits_cat = 0.3 * n

# Unaccelerated O(1/n): gamma naive. ~log10(n) digits (practically zero)
digits_gamma = np.log10(n + 1)

curve(ax, n, digits_e, 'Supergeometric (e, Taylor)', GREEN, 2.5)
curve(ax, n, digits_pi, 'Geometric fast (\u03c0, Machin)', CYAN, 2.5)
curve(ax, n, digits_z3, 'Geometric moderate (\u03b6(3), CBC)', BLUE, 2.5)
curve(ax, n, digits_cat, 'Accelerated (Catalan, Euler)', PURPLE, 2.5)
curve(ax, n, digits_gamma, 'Unaccelerated (\u03b3, naive)', RED, 2.5)

# Newton as discrete points (different x-scale)
for i, d in enumerate(digits_newton):
    if i < len(n_newton):
        data_point(ax, n_newton[i], min(d, 240), '', GOLD,
                   size=150 if d < 250 else 100)
ax.text(8, 220, 'Quadratic (\u221a2, Newton)\nDigits double each step',
        fontsize=9, color=GOLD, fontweight='bold')

# 100-digit target line
ax.plot([0, 100], [100, 100], color=ORANGE, linewidth=1.5,
        linestyle='--', alpha=0.6)
ax.text(55, 105, '100-digit target', fontsize=9, color=ORANGE)

# Tier boundary annotation
result_box(ax, 70, 15, 'TIER 2 BOUNDARY\n\u03b3 needs 10\u00b9\u2070\u2070 terms\nat this convergence rate',
           RED, 10)

ax.set_xlim(0, 105)
ax.set_ylim(0, 260)

legend(ax, loc='upper left')

save_fig(fig, 'math2_01_convergence_comparison.png')


# ================================================================
# FIG 2: PRECISION THRESHOLD — PLANCK VS 100 DIGITS
# Type: Scale/landscape
# Shows: The 65-order-of-magnitude gap between the Planck length
# and the first disagreement digit. The visual gap IS the argument.
# ================================================================

fig, ax = dark_fig("The Precision Threshold: 65 Orders Beyond the Planck Length",
                   xlabel="Scale (powers of 10, meters equivalent)",
                   ylabel="", size=(18, 10))

# Log scale from 10^0 down to 10^-110
positions = np.linspace(0, -110, 500)

# Landmark positions
landmarks = [
    (0, 'Human scale\n(1 m)', WHITE, 'left'),
    (-9, 'Atomic scale\n(1 nm)', CYAN, 'left'),
    (-15, 'Nuclear scale\n(1 fm)', GREEN, 'left'),
    (-35, 'PLANCK LENGTH\n(1.6\u00d710\u207b\u00b3\u2075 m)', GOLD, 'left'),
    (-100, 'First disagreement\ndigit of p/q vs \u03c0', MAG, 'left'),
]

# Background gradient regions
shaded_region(ax, -110, -35, GOLD, 0.04, '')
shaded_region(ax, -35, 0, CYAN, 0.03, '')

# The scale line
ax.plot([0, -110], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.5)

for pos, label, color, ha in landmarks:
    ax.plot([pos, pos], [0.2, 0.8], color=color, linewidth=2.5, alpha=0.8)
    data_point(ax, pos, 0.5, '', color, size=200)
    y_text = 1.3 if pos > -50 else 1.3
    ax.text(pos, y_text, label, fontsize=10, color=color,
            ha='center', fontweight='bold')

# The gap annotation
ax.annotate('', xy=(-100, -0.3), xytext=(-35, -0.3),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.5))
ax.text(-67.5, -0.7, '65 orders of magnitude\nNo physics here. No measurement.\nNo detector. No observable.',
        fontsize=12, color=GOLD, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Labels for regions
ax.text(-17, -1.3, 'PHYSICS OPERATES HERE', fontsize=11,
        color=CYAN, ha='center', fontweight='bold', alpha=0.7)
ax.text(-70, -1.3, 'FORMALLY REAL, OPERATIONALLY EMPTY', fontsize=11,
        color=DIM, ha='center', style='italic')

ax.set_xlim(-115, 5)
ax.set_ylim(-2.0, 2.0)
ax.set_yticks([])

save_fig(fig, 'math2_02_precision_threshold.png')


# ================================================================
# FIG 3: EULER ACCELERATION — CATALAN BEFORE/AFTER
# Type: Dual-panel convergence
# Shows: Raw alternating series (left, flat) vs Euler-accelerated
# (right, geometric decay). The transformation IS the method.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Before: Raw Alternating Series",
    "After: Euler Acceleration",
    size=(18, 9), wspace=0.35)

# Left: raw series partial sums for Catalan
# G = sum (-1)^k / (2k+1)^2
catalan_ref = 0.9159655941772190
n_raw = np.arange(1, 201)
partial_sums = np.zeros(len(n_raw))
running = 0.0
for i, k in enumerate(n_raw):
    running += ((-1) ** (k - 1)) / float((2 * (k - 1) + 1) ** 2)
    partial_sums[i] = running

curve(ax1, n_raw, partial_sums, 'Partial sums', CYAN, 2)
ax1.plot([0, 200], [catalan_ref, catalan_ref], color=GOLD,
         linewidth=1.5, linestyle='--', alpha=0.7)
ax1.text(110, catalan_ref + 0.003, 'G = 0.91597...', fontsize=9,
         color=GOLD)
ax1.set_xlabel('Terms', color=SILVER, fontsize=11)
ax1.set_ylabel('Partial sum', color=SILVER, fontsize=11)
ax1.set_xlim(0, 205)
ax1.set_ylim(0.82, 0.98)

note(ax1, 20, 0.84, 'Converges as O(1/n\u00b2)\n200 terms: ~2 correct digits', RED, 10)

# Right: accelerated convergence — digits correct vs terms
n_accel = np.arange(1, 361)
digits_accel = 0.3 * n_accel  # ~0.3 digits/term from the paper

curve(ax2, n_accel, digits_accel, 'Euler-accelerated', GREEN, 2.5)
ax2.plot([0, 360], [100, 100], color=ORANGE, linewidth=1.5,
         linestyle='--', alpha=0.6)
ax2.text(200, 105, '100-digit target', fontsize=9, color=ORANGE)

ax2.set_xlabel('Terms', color=SILVER, fontsize=11)
ax2.set_ylabel('Correct digits', color=SILVER, fontsize=11)
ax2.set_xlim(0, 370)
ax2.set_ylim(0, 130)

result_box(ax2, 180, 50, '350 terms \u2192 100+ digits\nvs 10\u00b9\u2070\u2070 terms naive',
           GOLD, 10)

save_fig(fig, 'math2_03_euler_acceleration.png')


# ================================================================
# FIG 4: PLANCK-PRECISION NUMBER LINE
# Type: Annotated scale
# Shows: 0 to 100+ digits with labeled zones. The reader sees
# WHERE physics lives and where the disagreement hides.
# ================================================================

fig, ax = dark_fig("The Precision Number Line: Where Physics Lives vs Where p/q Disagrees",
                   xlabel="Decimal digit position",
                   ylabel="", size=(18, 8))

# The number line
ax.plot([0, 110], [0.5, 0.5], color=DIM, linewidth=3, alpha=0.5)

# Zones
zones = [
    (0, 16, 'IEEE 754\ndouble', BLUE, 0.10),
    (16, 34, 'Best experiments\n(quadruple precision)', CYAN, 0.08),
    (34, 36, '', GOLD, 0.20),
    (36, 100, 'No physics accesses\nthese digits', DIM, 0.05),
    (100, 110, 'First\ndisagreement', RED, 0.15),
]

for x0, x1, label, color, alpha in zones:
    rect = plt.Rectangle((x0, 0.1), x1 - x0, 0.8,
                          facecolor=color, alpha=alpha, edgecolor='none')
    ax.add_patch(rect)
    if label:
        ax.text((x0 + x1) / 2, 1.25, label, fontsize=9, color=color,
                ha='center', fontweight='bold')

# Key markers
markers = [
    (16, 'IEEE 754 limit\n(~16 digits)', BLUE),
    (35, 'PLANCK FLOOR\n(~35 digits)', GOLD),
    (100, 'p/q \u2260 \u03c0\n(digit 101)', RED),
]

for pos, label, color in markers:
    ax.plot([pos, pos], [0.0, 1.0], color=color, linewidth=2.5, alpha=0.8)
    data_point(ax, pos, 0.5, '', color, size=200)
    y_off = -0.4 if pos == 35 else 1.6
    ax.text(pos, y_off, label, fontsize=10, color=color,
            ha='center', fontweight='bold')

# Gap labels
ax.annotate('', xy=(100, -0.8), xytext=(35, -0.8),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(67.5, -1.1, '65 digits: operationally empty',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

ax.set_xlim(-5, 115)
ax.set_ylim(-1.6, 2.2)
ax.set_yticks([])

save_fig(fig, 'math2_04_precision_numberline.png')


# ================================================================
# FIG 5: MACHIN'S FORMULA GEOMETRY
# Type: Geometric construction
# Shows: arctan(1/5) and arctan(1/239) as angles on the unit circle,
# combined to produce pi/4. The geometric meaning of the series.
# ================================================================

fig, ax = dark_canvas("Machin's Formula: \u03c0/4 = 4\u00b7arctan(1/5) \u2212 arctan(1/239)",
                      size=(14, 14))
ax.set_xlim(-0.3, 1.5)
ax.set_ylim(-0.3, 1.5)
ax.set_aspect('equal')

# Unit square quadrant
ax.plot([0, 1], [0, 0], color=DIM, linewidth=1.5)
ax.plot([0, 0], [0, 1], color=DIM, linewidth=1.5)

# Quarter circle arc
theta = np.linspace(0, np.pi / 2, 200)
ax.plot(np.cos(theta), np.sin(theta), color=DIM, linewidth=1.5,
        linestyle='--', alpha=0.5)

# arctan(1/5) angle
a1 = np.arctan(1.0 / 5.0)
ax.plot([0, 1.1 * np.cos(a1)], [0, 1.1 * np.sin(a1)],
        color=CYAN, linewidth=2.5, zorder=4)
# Arc for angle
arc_a1 = np.linspace(0, a1, 50)
ax.plot(0.4 * np.cos(arc_a1), 0.4 * np.sin(arc_a1),
        color=CYAN, linewidth=2, alpha=0.8)
ax.text(0.5, 0.08, 'arctan(1/5)', fontsize=10, color=CYAN,
        fontweight='bold')

# 4*arctan(1/5) angle
a4 = 4 * a1
ax.plot([0, 0.9 * np.cos(a4)], [0, 0.9 * np.sin(a4)],
        color=GREEN, linewidth=2.5, zorder=4)
arc_a4 = np.linspace(0, a4, 100)
ax.plot(0.6 * np.cos(arc_a4), 0.6 * np.sin(arc_a4),
        color=GREEN, linewidth=2, alpha=0.8)
ax.text(0.25, 0.62, '4\u00b7arctan(1/5)', fontsize=10, color=GREEN,
        fontweight='bold')

# arctan(1/239) — tiny angle to subtract
a239 = np.arctan(1.0 / 239.0)
# Show it as a small wedge near pi/4
ax.plot([0, 0.8 * np.cos(a4)], [0, 0.8 * np.sin(a4)],
        color=GREEN, linewidth=1, alpha=0.5)
ax.plot([0, 0.8 * np.cos(a4 - a239)], [0, 0.8 * np.sin(a4 - a239)],
        color=MAG, linewidth=2, zorder=4)

# pi/4 line (the target: 45 degrees)
pi4 = np.pi / 4
ax.plot([0, 1.1 * np.cos(pi4)], [0, 1.1 * np.sin(pi4)],
        color=GOLD, linewidth=3, zorder=5, alpha=0.8)
ax.text(0.85, 0.95, '\u03c0/4 = 45\u00b0', fontsize=13, color=GOLD,
        fontweight='bold')

# The tiny correction
ax.annotate('arctan(1/239)\n(tiny correction)', xy=(0.65, 0.77),
            xytext=(1.05, 1.1),
            fontsize=9, color=MAG, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

# Right triangle for arctan(1/5)
ax.plot([1, 1], [0, 0.2], color=CYAN, linewidth=1.5, linestyle=':')
ax.plot([0, 1], [0, 0], color=CYAN, linewidth=1.5, linestyle=':')
ax.plot([0, 1], [0, 0.2], color=CYAN, linewidth=1.5, linestyle=':')
ax.text(1.05, 0.1, '1/5', fontsize=9, color=CYAN)
ax.text(0.5, -0.08, '1', fontsize=9, color=CYAN)

# Origin dot
data_point(ax, 0, 0, '', WHITE, size=100)

# Formula
result_box(ax, 0.75, -0.15,
           '4\u00b7arctan(1/5) \u2212 arctan(1/239) = \u03c0/4\n'
           'Gregory series at x=1/5: geometric ratio 1/25\n'
           '80 terms \u2192 100+ correct digits of \u03c0', GOLD, 10)

save_fig(fig, 'math2_05_machin_geometry.png')


# ================================================================
# FIG 6: CONVERGENCE CLASS SCATTER
# Type: Parameter space
# Shows: Each constant plotted by (terms needed, digits/term).
# Clusters reveal convergence classes. The spatial grouping
# is impossible to see in the table.
# ================================================================

fig, ax = dark_fig("Convergence Classes: Constants by Terms and Efficiency",
                   xlabel="Terms / iterations needed for 100 digits",
                   ylabel="Digits per term (or per iteration)")

# Data: (terms, digits_per_term, label, color, convergence_class)
constants = [
    # Supergeometric
    (80, 2.3, 'e', GREEN, 'Supergeometric'),
    (120, 1.5, 'e\u03c0', GREEN, 'Supergeometric'),
    # Quadratic (iterations, not terms — use effective digits/iter)
    (10, 100, '\u221a2', GOLD, 'Quadratic'),
    (10, 100, '\u221a3', GOLD, 'Quadratic'),
    (10, 100, '\u03c6', GOLD, 'Quadratic'),
    # Geometric fast
    (80, 1.4, '\u03c0', CYAN, 'Geometric (fast)'),
    (120, 1.4, 'ln(3)', CYAN, 'Geometric (fast)'),
    (120, 1.9, 'ln(5)', CYAN, 'Geometric (fast)'),
    # Geometric moderate
    (120, 0.95, 'ln(2)', BLUE, 'Geometric (mod)'),
    (180, 0.6, '\u03b6(3)', BLUE, 'Geometric (mod)'),
    # Accelerated
    (350, 0.3, 'Catalan', PURPLE, 'Accelerated'),
    # Unaccelerated (off the chart, represented as arrow)
]

for terms, dpt, label, color, cls in constants:
    data_point(ax, terms, dpt, '', color, size=200)
    # Offset labels to avoid overlap
    dx = 12
    dy = 0.08 if dpt < 5 else 5
    ax.text(terms + dx, dpt + dy, label, fontsize=9, color=color,
            fontweight='bold', va='bottom')

# Gamma as an off-chart arrow
ax.annotate('\u03b3 (naive): 10\u00b9\u2070\u2070 terms\n\u2192 TIER 2', xy=(380, 0.01),
            fontsize=10, color=RED, fontweight='bold', ha='left', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# Quadratic cluster label
ax.text(30, 80, 'QUADRATIC\nDigits double\neach iteration', fontsize=10,
        color=GOLD, fontweight='bold', style='italic', alpha=0.8)

# Class region labels
ax.text(90, 2.8, 'SUPERGEOMETRIC', fontsize=9, color=GREEN,
        fontweight='bold', alpha=0.7)
ax.text(200, 1.6, 'GEOMETRIC', fontsize=9, color=CYAN,
        fontweight='bold', alpha=0.7)
ax.text(320, 0.5, 'ACCELERATED', fontsize=9, color=PURPLE,
        fontweight='bold', alpha=0.7)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(5, 500)
ax.set_ylim(0.1, 200)

save_fig(fig, 'math2_06_convergence_scatter.png')


# ================================================================
# FIG 7: INTEGER PAIR SIZE — LOG BAR CHART
# Type: Comparison bar chart
# Shows: Numerator digit count from e (117) to e^pi (65935).
# The 500x range shows pair size reflects algorithm, not constant.
# ================================================================

fig, ax = dark_fig("Integer Pair Sizes: Algorithm Choice, Not Constant Complexity",
                   xlabel="", ylabel="Numerator digits (log scale)")

pair_data = [
    ('e', 117, GREEN),
    ('ln(2)', 213, BLUE),
    ('\u221a5', 215, CYAN),
    ('\u221a3', 293, CYAN),
    ('\u03b6(3)', 309, PURPLE),
    ('ln(5)', 327, BLUE),
    ('\u221a2', 392, CYAN),
    ('\u221a7', 421, CYAN),
    ('\u03c6', 428, GOLD),
    ('\u03c0', 554, ORANGE),
    ('Catalan', 857, MAG),
    ('\u03b6(2)', 1107, PURPLE),
    ('\u03c0\u00b3', 1660, ORANGE),
    ('e\u03c0', 65935, RED),
]

labels = [d[0] for d in pair_data]
values = [d[1] for d in pair_data]
colors = [d[2] for d in pair_data]

x_pos = np.arange(len(pair_data))
for i in range(len(pair_data)):
    ax.bar(i, values[i], color=colors[i], alpha=0.7,
           edgecolor=colors[i], linewidth=1.5, width=0.7)
    # Value label
    if values[i] < 2000:
        ax.text(i, values[i] * 1.15, str(values[i]), fontsize=8,
                color=WHITE, ha='center', va='bottom', fontweight='bold')
    else:
        ax.text(i, values[i] * 1.15, str(values[i]), fontsize=8,
                color=RED, ha='center', va='bottom', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=8, color=SILVER, rotation=45, ha='right')
ax.set_yscale('log')
ax.set_xlim(-0.8, len(pair_data) - 0.2)
ax.set_ylim(50, 200000)

# Annotation for e^pi
ax.annotate('e\u03c0: \u03c0\u00b9\u00b2\u2070 inside Taylor\nproduces 65k-digit integers',
            xy=(13, 65935), xytext=(9.5, 50000),
            fontsize=10, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

note(ax, 1, 100000, 'All 17 match at 100 digits.\nPair size varies 500\u00d7 — reflects the series, not the constant.',
     SILVER, 10)

save_fig(fig, 'math2_07_pair_sizes.png')


# ================================================================
# FIG 8: MATH-2 IDENTITY CARD
# Type: Identity card
# Shows: The integer pair concept, three tiers, key results.
# Visual anchor for the entire paper.
# ================================================================

fig, ax = dark_canvas("MATH-2 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Central concept: the integer pair
ax.text(3.5, 8.5, 'THE INTEGER PAIR', fontsize=18, color=GOLD,
        ha='center', fontweight='bold')

ax.text(3.5, 7.5, 'p / q', fontsize=40, color=WHITE,
        ha='center', fontweight='bold',
        fontfamily='monospace')

ax.text(3.5, 6.6, 'Two integers. No floats. No epsilon.\n'
        'String comparison, not proximity test.\n'
        'Operationally identical at 100 digits.',
        fontsize=11, color=SILVER, ha='center')

# Example
ax.text(3.5, 5.6, '\u03c0 = p/q  where p has 554 digits, q has 553 digits',
        fontsize=10, color=CYAN, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN))

# Three tiers — right column
tier_y = [8.5, 6.2, 4.0]
tiers = [
    ('TIER 1: DERIVED', '17 constants', '100-digit match, all YES',
     'Series \u2192 Fraction \u2192 verify', GREEN),
    ('TIER 2: BOUNDARY', '5 constants', 'Computable but unimplemented',
     '\u03b3, Feigenbaum \u03b4\u03b1, Khinchin, Glaisher', ORANGE),
    ('TIER 3: MEASURED', '2 constants', 'No formula exists',
     '\u03b1 = 1/137.036..., \u03bc = 1836.153...', RED),
]

for i, (title, count, status, detail, color) in enumerate(tiers):
    y = tier_y[i]
    ax.text(8.0, y, title, fontsize=13, color=color,
            ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color))
    ax.text(8.0, y - 0.55, count, fontsize=11, color=WHITE,
            ha='center', fontweight='bold')
    ax.text(8.0, y - 1.0, status, fontsize=9, color=SILVER, ha='center')
    ax.text(8.0, y - 1.4, detail, fontsize=8, color=DIM, ha='center')

# The structural line
ax.plot([6.2, 9.8], [3.2, 3.2], color=RED, linewidth=2,
        linestyle='--', alpha=0.6)
ax.text(8.0, 2.8, 'ABOVE: mathematics provides digits\n'
        'BELOW: the universe provides digits',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

# Key numbers — bottom left
ax.text(3.5, 3.8, 'KEY NUMBERS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

key_nums = [
    ('100', 'digits matched', GOLD),
    ('65', 'orders below Planck', GOLD),
    ('17/17', 'Tier 1 confirmed', GREEN),
    ('0', 'floats in computation', CYAN),
]

for i, (num, label, color) in enumerate(key_nums):
    y = 3.1 - i * 0.55
    ax.text(2.2, y, num, fontsize=16, color=color,
            ha='right', fontweight='bold')
    ax.text(2.5, y, label, fontsize=10, color=SILVER,
            ha='left', va='center')

# Bottom banner
ax.text(5.0, 0.6, 'HOWL-MATH-2: Integer-Pair Representations at Sub-Planck Precision',
        fontsize=14, color=GOLD, ha='center', fontweight='bold')
ax.text(5.0, 0.15, 'The transcendental barrier to integer-only arithmetic is not fundamental. '
        'It is an artifact of convention.',
        fontsize=9, color=SILVER, ha='center', style='italic')

save_fig(fig, 'math2_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("MATH-2 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'math2_01_convergence_comparison.png',
    'math2_02_precision_threshold.png',
    'math2_03_euler_acceleration.png',
    'math2_04_precision_numberline.png',
    'math2_05_machin_geometry.png',
    'math2_06_convergence_scatter.png',
    'math2_07_pair_sizes.png',
    'math2_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))

    