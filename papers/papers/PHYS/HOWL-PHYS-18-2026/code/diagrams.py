#!/usr/bin/env python3
"""
HOWL PHYS-18 Diagrams — The Y = 1/6 Asymmetry
8 figures covering sharp optimum, double action, Venn requirements,
structural dependence, fermion vs scalar, efficiency, identity card.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: GAP RATIO VS Y FOR (3,2,Y) — SHARP OPTIMUM
# Type: Running/comparison
# Shows: Gap ratio rising monotonically from 1.407 at Y=1/6 to
# 2.119 at Y=7/6. The sharp minimum IS the finding.
# ================================================================

fig, ax = dark_fig("Gap Ratio vs Hypercharge Y for (3,2,Y) Vector-Like Fermions",
                   xlabel="Hypercharge Y",
                   ylabel="Modified gap ratio",
                   size=(16, 10))

# Compute gap ratio for a range of Y values
# For (3,2,Y) VL: Db1 = (1/15) * (Y/(1/6))^2 = (1/15) * 36Y^2
# Db2 = 1 (always), Db3 = 1/3 (always)
# Denominator = 9/2 = 4.5 (always)
# Numerator = 109/15 + Db1 - Db2 = 109/15 + 36Y^2/15 - 1 = (109 + 36Y^2 - 15)/15 = (94 + 36Y^2)/15

Y_vals = np.linspace(0.05, 1.4, 200)
gap_vals = np.zeros_like(Y_vals)

for i, Y in enumerate(Y_vals):
    Db1 = (1.0 / 15) * (Y / (1.0 / 6))**2
    # b1 + Db1 = 41/10 + Db1
    b1_mod = 41.0 / 10 + Db1
    b2_mod = -19.0 / 6 + 1  # = -13/6
    b3_mod = -7.0 + 1.0 / 3  # = -20/3
    num = b1_mod - b2_mod
    den = b2_mod - b3_mod
    gap_vals[i] = num / den

curve(ax, Y_vals, gap_vals, 'Gap ratio for (3,2,Y) VL fermion', CYAN, 2.5)

# Mark specific Y values
Y_specific = [1.0 / 6, 1.0 / 3, 0.5, 2.0 / 3, 5.0 / 6, 7.0 / 6]
gap_specific = [38.0 / 27, 196.0 / 135, 206.0 / 135, 44.0 / 27, 238.0 / 135, 286.0 / 135]
labels_Y = ['1/6', '1/3', '1/2', '2/3', '5/6', '7/6']
colors_Y = [GOLD, BLUE, GREEN, ORANGE, DIM, RED]
dists = [0.049, 0.094, 0.168, 0.272, 0.405, 0.760]

for j, (yv, gv, lab, col, dist) in enumerate(zip(Y_specific, gap_specific, labels_Y, colors_Y, dists)):
    data_point(ax, yv, gv, '', col, size=250)
    y_off = 0.06 if j % 2 == 0 else -0.08
    ax.text(yv, gv + y_off, 'Y=%s\nd=%.3f' % (lab, dist), fontsize=8,
            color=col, ha='center', fontweight='bold')

# Highlight the optimum
ax.scatter([1.0 / 6], [38.0 / 27], s=500, facecolors='none', edgecolors=GOLD,
           linewidth=3, zorder=11)
ax.annotate('SHARP OPTIMUM\nY = 1/6\nGap = 38/27 = 1.407\nDistance = 0.049',
            xy=(1.0 / 6, 38.0 / 27), xytext=(0.5, 1.25),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Measured line
ax.plot([0, 1.5], [1.358, 1.358], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.5)
ax.text(1.3, 1.37, 'Measured\n1.358', fontsize=9, color=GOLD)

# SM line
ax.plot([0, 1.5], [218.0 / 115, 218.0 / 115], color=RED, linewidth=1.5,
        linestyle=':', alpha=0.4)
ax.text(1.3, 1.91, 'SM\n218/115', fontsize=8, color=RED)

# Crossover annotation
ax.annotate('Y = 7/6: WORSE\nthan SM!', xy=(7.0 / 6, 286.0 / 135),
            xytext=(1.0, 2.15),
            fontsize=9, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.set_xlim(0, 1.45)
ax.set_ylim(1.15, 2.25)

save_fig(fig, 'phys18_01_gap_vs_hypercharge.png')


# ================================================================
# FIG 2: THE DOUBLE ACTION
# Type: Dual-bar comparison
# Shows: Numerator shrinks 13%, denominator grows 17%.
# Combined effect = 26% gap ratio reduction.
# ================================================================

fig, ax = dark_fig("The Double Action: Numerator Shrinks AND Denominator Grows",
                   xlabel="",
                   ylabel="",
                   size=(16, 10))

# Left: numerator
ax.text(2.5, 9.0, 'NUMERATOR (b\u2081 \u2212 b\u2082)', fontsize=14,
        color=CYAN, ha='center', fontweight='bold')

# Before bar
ax.bar(1.5, 109.0 / 15, color=RED, alpha=0.4, edgecolor=RED,
       linewidth=2, width=0.8, bottom=0)
ax.text(1.5, 109.0 / 15 + 0.2, '109/15\n= 7.267', fontsize=10,
        color=RED, ha='center', fontweight='bold')
ax.text(1.5, -0.5, 'SM\n(before)', fontsize=9, color=SILVER, ha='center')

# After bar
ax.bar(3.5, 19.0 / 3, color=CYAN, alpha=0.4, edgecolor=CYAN,
       linewidth=2, width=0.8, bottom=0)
ax.text(3.5, 19.0 / 3 + 0.2, '19/3\n= 6.333', fontsize=10,
        color=CYAN, ha='center', fontweight='bold')
ax.text(3.5, -0.5, 'SM + CD\n(after)', fontsize=9, color=SILVER, ha='center')

# Shrinkage arrow
ax.annotate('\u221213%', xy=(3.5, 19.0 / 3), xytext=(1.5, 109.0 / 15),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5),
            fontsize=14, color=GREEN, fontweight='bold', ha='center')

# Right: denominator
ax.text(7.5, 9.0, 'DENOMINATOR (b\u2082 \u2212 b\u2083)', fontsize=14,
        color=ORANGE, ha='center', fontweight='bold')

# Before bar
ax.bar(6.5, 23.0 / 6, color=RED, alpha=0.4, edgecolor=RED,
       linewidth=2, width=0.8, bottom=0)
ax.text(6.5, 23.0 / 6 + 0.2, '23/6\n= 3.833', fontsize=10,
        color=RED, ha='center', fontweight='bold')
ax.text(6.5, -0.5, 'SM\n(before)', fontsize=9, color=SILVER, ha='center')

# After bar
ax.bar(8.5, 9.0 / 2, color=ORANGE, alpha=0.4, edgecolor=ORANGE,
       linewidth=2, width=0.8, bottom=0)
ax.text(8.5, 9.0 / 2 + 0.2, '9/2\n= 4.500', fontsize=10,
        color=ORANGE, ha='center', fontweight='bold')
ax.text(8.5, -0.5, 'SM + CD\n(after)', fontsize=9, color=SILVER, ha='center')

# Growth arrow
ax.annotate('+17%', xy=(8.5, 9.0 / 2), xytext=(6.5, 23.0 / 6),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5),
            fontsize=14, color=GREEN, fontweight='bold', ha='center')

# Result at bottom
result_box(ax, 5.0, -2.0,
           'Numerator shrinks (\u0394b\u2082 = 1 overwhelms \u0394b\u2081 = 1/15)\n'
           'Denominator grows (\u0394b\u2082 = 1 exceeds \u0394b\u2083 = 1/3)\n'
           'Combined: gap ratio 1.896 \u2192 1.407 (\u221226%)\n'
           'One particle hits the ratio from BOTH directions.',
           GOLD, 10)

ax.set_xlim(0, 10)
ax.set_ylim(-3.5, 10)
ax.set_xticks([])
ax.set_yticks([])

save_fig(fig, 'phys18_02_double_action.png')


# ================================================================
# FIG 3: SINGLE VS DOUBLE ACTION
# Type: Comparison bar
# Shows: Numerator-only (1.652), denominator-only (1.615),
# double action (1.407). The combined is 5-6x better.
# ================================================================

fig, ax = dark_fig("Single Action vs Double Action: 5\u20136\u00d7 More Effective",
                   xlabel="",
                   ylabel="Gap ratio achieved",
                   size=(16, 10))

actions = [
    ('SM\n(no correction)', 218.0 / 115, RED, '218/115'),
    ('Numerator\nonly', 38.0 / 23, CYAN, '38/23\ndist = 0.294'),
    ('Denominator\nonly', 218.0 / 135, BLUE, '218/135\ndist = 0.257'),
    ('DOUBLE\nACTION', 38.0 / 27, GOLD, '38/27\ndist = 0.049'),
]

for i, (label, gap, color, detail) in enumerate(actions):
    ax.bar(i, gap, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.65)
    ax.text(i, gap + 0.03, detail, fontsize=10, color=color,
            ha='center', fontweight='bold')

ax.set_xticks(range(len(actions)))
ax.set_xticklabels([a[0] for a in actions], fontsize=10, color=SILVER)

# Measured line
ax.plot([-0.5, 3.5], [1.358, 1.358], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.6)
ax.text(3.3, 1.37, 'Measured\n1.358', fontsize=9, color=GOLD,
        fontweight='bold')

# Improvement annotations
ax.annotate('5.6\u00d7\ncloser', xy=(3, 1.42), xytext=(2, 1.55),
            fontsize=11, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# Key insight
result_box(ax, 1, 1.15,
           'The double action achieves 0.049 distance.\n'
           'Single actions achieve 0.257\u20130.294.\n'
           'Both effects together are 5\u20136\u00d7 better\n'
           'than either alone.',
           SILVER, 9)

ax.set_xlim(-0.8, 4.0)
ax.set_ylim(1.05, 2.05)

save_fig(fig, 'phys18_03_single_vs_double.png')


# ================================================================
# FIG 4: THREE REQUIREMENTS AS VENN
# Type: Geometric
# Shows: Three overlapping circles: Color, Weak, Small Y.
# Only the Cabibbo Doublet sits in the triple intersection.
# ================================================================

fig, ax = dark_canvas("Three Requirements: Only (3,2,1/6) Satisfies All",
                      size=(16, 14))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3.5)
ax.set_aspect('equal')

# Three circles
r = 1.6
centers = [(-0.8, 0.5), (0.8, 0.5), (0, -0.8)]
labels = ['COLOR\n(dim(R\u2083) \u2265 3)', 'WEAK CHARGE\n(dim(R\u2082) \u2265 2)', 'SMALL Y\n(Y\u00b2 minimal)']
circle_colors = [RED, GREEN, BLUE]

for (cx, cy), label, color in zip(centers, labels, circle_colors):
    circ = plt.Circle((cx, cy), r, fill=True, facecolor=color,
                        alpha=0.06, edgecolor=color, linewidth=2, zorder=2)
    ax.add_patch(circ)

# Labels outside circles
ax.text(-2.2, 2.0, labels[0], fontsize=11, color=RED, ha='center',
        fontweight='bold')
ax.text(2.2, 2.0, labels[1], fontsize=11, color=GREEN, ha='center',
        fontweight='bold')
ax.text(0, -2.8, labels[2], fontsize=11, color=BLUE, ha='center',
        fontweight='bold')

# Particles in each region
# Color only (no weak, no small Y)
ax.text(-1.8, 0.0, 'VL d\u1d63 (3,1)\nVL u\u1d63 (3,1)\nSc (3,1)\nSc (8,1)',
        fontsize=7, color=DIM, ha='center')

# Weak only (no color, no small Y)
ax.text(1.8, 0.0, 'Sc (1,3,0)\nSc (1,2)',
        fontsize=7, color=DIM, ha='center')

# Small Y only (no color, no weak)
ax.text(0, -1.8, 'VL (1,1,\u22121)',
        fontsize=7, color=DIM, ha='center')

# Color + Weak (no small Y)
ax.text(0, 1.5, 'SU(5) 10+10\u0305\n(Y too large)',
        fontsize=7, color=DIM, ha='center')

# Color + Small Y (no weak)
# (empty in our enumeration at small Y — the (3,1,1/6) doesn't exist with standard charges)

# Weak + Small Y (no color)
ax.text(1.0, -1.0, 'VL (1,2,\u22121/2)',
        fontsize=7, color=DIM, ha='center')

# Triple intersection — THE CABIBBO DOUBLET
ax.text(0, 0.2, '(3, 2, 1/6)', fontsize=16, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                  linewidth=2.5, alpha=0.9))
ax.text(0, -0.3, 'CABIBBO\nDOUBLET', fontsize=10, color=GOLD,
        ha='center', fontweight='bold')

# Also in triple: SU(5) 5+5bar (but effective Y too large)
ax.text(-0.3, 0.8, '5+5\u0305\n(but \u0394b\u2081\ntoo large)',
        fontsize=6, color=ORANGE, ha='center')

# Bottom
ax.text(0, -3.3, 'Color for denominator growth. Weak charge for numerator shrinkage.\n'
        'Small Y for maximum asymmetry (\u0394b\u2082/\u0394b\u2081 = 15).\n'
        'Plus: fermion (not scalar) for sufficient magnitude. Plus: anomaly-free.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys18_04_venn_requirements.png')


# ================================================================
# FIG 5: Y ENTERS ONLY Db1 — STRUCTURAL DEPENDENCE
# Type: Connection/schematic
# Shows: Db1 depends on Y^2 (variable). Db2 and Db3 do not
# depend on Y (fixed). The structural fact IS the mechanism.
# ================================================================

fig, ax = dark_canvas("The Structural Fact: Y Enters Only \u0394b\u2081",
                      size=(16, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Y input on the left
ax.text(1.5, 5.0, 'Y = 1/6', fontsize=22, color=GOLD, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=2.5))
ax.text(1.5, 3.8, 'Hypercharge\n(representation\nquantum number)', fontsize=9,
        color=SILVER, ha='center')

# Three output channels
# Db1: connected to Y
ax.annotate('', xy=(5.5, 7.5), xytext=(2.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=3))
ax.text(5.5, 8.0, '\u0394b\u2081 = 1/15', fontsize=16, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                  linewidth=2))
ax.text(5.5, 7.0, 'Depends on Y\u00b2 = 1/36\n(TINY at Y = 1/6)', fontsize=10,
        color=GOLD, ha='center', fontweight='bold')

# Db2: NOT connected to Y
ax.text(7.5, 5.0, '\u0394b\u2082 = 1', fontsize=16, color=CYAN,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN,
                  linewidth=2))
ax.text(7.5, 4.0, 'Independent of Y\n(from SU(2) \u00d7 SU(3))', fontsize=10,
        color=CYAN, ha='center')

# Big X between Y and Db2
ax.text(4.0, 4.8, '\u2717', fontsize=30, color=RED, ha='center',
        fontweight='bold', alpha=0.6)

# Db3: NOT connected to Y
ax.text(7.5, 2.0, '\u0394b\u2083 = 1/3', fontsize=16, color=GREEN,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN,
                  linewidth=2))
ax.text(7.5, 1.0, 'Independent of Y\n(from SU(3) \u00d7 SU(2))', fontsize=10,
        color=GREEN, ha='center')

# Big X between Y and Db3
ax.text(4.0, 2.5, '\u2717', fontsize=30, color=RED, ha='center',
        fontweight='bold', alpha=0.6)

# The consequence
result_box(ax, 5.0, -0.5,
           'CONSEQUENCE: \u0394b\u2082/\u0394b\u2081 = 1/(1/15) = 15\n'
           'Y\u00b2 is the ONLY handle. Small Y \u2192 small \u0394b\u2081 \u2192 extreme asymmetry.\n'
           'The SU(2) and SU(3) vertices do not involve hypercharge.',
           GOLD, 10)

save_fig(fig, 'phys18_05_structural_dependence.png')


# ================================================================
# FIG 6: FERMION VS SCALAR (3,2,1/6) — SAME RATIO, HALF MAGNITUDE
# Type: Comparison bar (distinct)
# Shows: Both have asymmetry ratio 15. But scalar Db2 = 1/2
# (vs fermion Db2 = 1). Scalar gap = 1.632, fermion gap = 1.407.
# ================================================================

fig, ax = dark_fig("Fermion vs Scalar (3,2,1/6): Same Ratio, Different Magnitude",
                   xlabel="",
                   ylabel="",
                   size=(16, 10))

# Two groups of bars
properties = ['\u0394b\u2082/\u0394b\u2081\nratio', '\u0394b\u2082\nmagnitude', 'Gap ratio\nachieved',
              'Distance\nfrom 1.358']
fermion_vals = [15.0, 1.0, 38.0 / 27, 0.049]
scalar_vals = [15.0, 0.5, 1.632, 0.274]

x_base = np.arange(len(properties))
bar_w = 0.35

for i in range(len(properties)):
    ax.bar(i - bar_w / 2 - 0.02, fermion_vals[i], color=CYAN, alpha=0.6,
           edgecolor=CYAN, linewidth=2, width=bar_w)
    ax.bar(i + bar_w / 2 + 0.02, scalar_vals[i], color=ORANGE, alpha=0.6,
           edgecolor=ORANGE, linewidth=2, width=bar_w)

    ax.text(i - bar_w / 2, fermion_vals[i] + 0.3, '%.3f' % fermion_vals[i] if fermion_vals[i] < 2 else '%d' % fermion_vals[i],
            fontsize=10, color=CYAN, ha='center', fontweight='bold')
    ax.text(i + bar_w / 2, scalar_vals[i] + 0.3, '%.3f' % scalar_vals[i] if scalar_vals[i] < 2 else '%d' % scalar_vals[i],
            fontsize=10, color=ORANGE, ha='center', fontweight='bold')

ax.set_xticks(x_base)
ax.set_xticklabels(properties, fontsize=10, color=SILVER)

# Same / different labels
ax.text(0, 16, 'SAME', fontsize=14, color=GREEN, ha='center',
        fontweight='bold')
ax.text(1, 1.3, '2\u00d7', fontsize=14, color=RED, ha='center',
        fontweight='bold')
ax.text(2, 1.8, '5.6\u00d7\nworse', fontsize=10, color=RED, ha='center',
        fontweight='bold')

# Legend
ax.bar(-1, 0, color=CYAN, alpha=0.6, width=0.01, label='VL Fermion (3,2,1/6)')
ax.bar(-1, 0, color=ORANGE, alpha=0.6, width=0.01, label='Scalar (3,2,1/6)')
legend(ax, loc='upper right')

# The lesson
result_box(ax, 2, -2,
           'The asymmetry ratio is NECESSARY but not SUFFICIENT.\n'
           'The scalar has the right ratio (15) but half the magnitude.\n'
           'Scalar \u0394b\u2082 = 1/2 vs fermion \u0394b\u2082 = 1.\n'
           'Must be a fermion.',
           GOLD, 10)

ax.set_xlim(-0.8, 4.0)
ax.set_ylim(-3.5, 17)

save_fig(fig, 'phys18_06_fermion_vs_scalar.png')


# ================================================================
# FIG 7: PER-FIELD EFFICIENCY — 35x MORE EFFICIENT THAN MSSM
# Type: Comparison bar (distinct)
# Shows: Cabibbo Doublet: 0.012 gap correction per field.
# MSSM: 0.00035 per field. 35x ratio.
# ================================================================

fig, ax = dark_fig("Per-Field Efficiency: 35\u00d7 More Gap Ratio Correction",
                   xlabel="",
                   ylabel="Gap ratio correction per new field",
                   size=(16, 10))

models = [
    ('Cabibbo Doublet\n(4 Weyl fields)', 0.049 / 4, CYAN, '0.049 / 4 fields\n= 0.012 per field'),
    ('MSSM\n(~120 fields)', 0.042 / 120, GREEN, '0.042 / 120 fields\n= 0.00035 per field'),
]

for i, (label, eff, color, detail) in enumerate(models):
    ax.bar(i, eff, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    ax.text(i, eff + 0.0005, detail, fontsize=10, color=color,
            ha='center', fontweight='bold')

ax.set_xticks([0, 1])
ax.set_xticklabels([m[0] for m in models], fontsize=11, color=SILVER)

# Ratio annotation
ax.annotate('35\u00d7', xy=(1, 0.00035), xytext=(0.5, 0.006),
            fontsize=24, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Key insight
result_box(ax, 0.5, -0.005,
           'The Cabibbo Doublet exploits the Y = 1/6 asymmetry:\n'
           'one targeted intervention vs comprehensive restructuring.\n'
           'Surgical precision vs brute force.',
           SILVER, 10)

ax.set_xlim(-0.8, 2.0)
ax.set_ylim(-0.008, 0.016)

save_fig(fig, 'phys18_07_per_field_efficiency.png')


# ================================================================
# FIG 8: PHYS-18 IDENTITY CARD
# Type: Identity card
# Shows: Y=1/6, asymmetry=15, double action, sharp optimum.
# ================================================================

fig, ax = dark_canvas("PHYS-18 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE Y = 1/6 ASYMMETRY', fontsize=20, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'Small hypercharge, large correction.',
        fontsize=12, color=SILVER, ha='center', style='italic')

# The mechanism chain
ax.text(5, 7.5, 'THE MECHANISM', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

chain = [
    ('Y = 1/6', 'Smallest for (3,2,Y) with standard charges', GOLD),
    ('Y\u00b2 = 1/36', 'Enters \u0394b\u2081 only', GOLD),
    ('\u0394b\u2081 = 1/15', 'Tiny hypercharge contribution', CYAN),
    ('\u0394b\u2082 = 1, \u0394b\u2083 = 1/3', 'Independent of Y', GREEN),
    ('\u0394b\u2082/\u0394b\u2081 = 15', 'Maximum asymmetry', ORANGE),
]
for i, (item, detail, color) in enumerate(chain):
    y = 6.8 - i * 0.7
    ax.text(3.5, y, item, fontsize=11, color=color, fontweight='bold')
    ax.text(7.0, y, detail, fontsize=9, color=SILVER)
    if i < len(chain) - 1:
        ax.text(2.5, y - 0.35, '\u2193', fontsize=12, color=DIM, ha='center')

# The double action
ax.plot([0.5, 9.5], [3.5, 3.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 3.0, 'THE DOUBLE ACTION', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

ax.text(2.5, 2.3, 'Numerator (b\u2081\u2212b\u2082):\n109/15 \u2192 19/3\n(\u221213%)',
        fontsize=10, color=CYAN, ha='center', fontweight='bold')
ax.text(7.5, 2.3, 'Denominator (b\u2082\u2212b\u2083):\n23/6 \u2192 9/2\n(+17%)',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold')

# Result
ax.text(5, 1.3, 'Gap ratio: 218/115 \u2192 38/27', fontsize=14,
        color=GOLD, ha='center', fontweight='bold',
        fontfamily='monospace')
ax.text(5, 0.7, '1.896 \u2192 1.407 (distance 0.049 from measured 1.358)',
        fontsize=10, color=SILVER, ha='center')

# Bottom
ax.text(5, 0.1, 'The optimum at Y = 1/6 is SHARP. Increasing Y degrades the correction monotonically.\n'
        'At Y = 7/6, the particle makes unification WORSE. The mechanism is Level 1 mathematics.',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys18_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-18 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys18_01_gap_vs_hypercharge.png',
    'phys18_02_double_action.png',
    'phys18_03_single_vs_double.png',
    'phys18_04_venn_requirements.png',
    'phys18_05_structural_dependence.png',
    'phys18_06_fermion_vs_scalar.png',
    'phys18_07_per_field_efficiency.png',
    'phys18_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    