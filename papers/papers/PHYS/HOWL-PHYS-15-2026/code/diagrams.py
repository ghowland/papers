#!/usr/bin/env python3
"""
HOWL PHYS-15 Diagrams — Integer-Forced Identification of the Minimal Unification Extension
8 figures covering elimination cascade, asymmetry ratio, exact rationals,
Hyper-K decision tree, method inversion, number line, beta shifts.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: ELIMINATION CASCADE 15 -> 3 -> 2
# Type: Funnel/flow
# Shows: 15 candidates at top, gap ratio filter removes 12,
# proton decay removes 1, two survivors at bottom.
# ================================================================

fig, ax = dark_canvas("The Elimination Cascade: 15 \u2192 3 \u2192 2",
                      size=(16, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)

# Stage 0: all 15
ax.text(5, 11.5, '15 CANDIDATES', fontsize=18, color=WHITE,
        ha='center', fontweight='bold')
ax.text(5, 10.8, 'Every scalar and VL fermion with dim(SU(3))\u22648,\n'
        'dim(SU(2))\u22644, |Y|\u22642', fontsize=9, color=SILVER, ha='center')

# 15 dots at top
for i in range(15):
    x = 1.5 + i * 0.5
    data_point(ax, x, 10.0, '', DIM, size=80)

# Gate 1
rect1 = plt.Rectangle((1.5, 7.8), 7.0, 1.2, facecolor=RED, alpha=0.06,
                        edgecolor=RED, linewidth=2, zorder=2)
ax.add_patch(rect1)
ax.text(5, 8.6, 'GATE 1: Gap Ratio Arithmetic', fontsize=14, color=RED,
        ha='center', fontweight='bold')
ax.text(5, 8.1, 'Modified gap ratio within \u00b10.15 of measured 1.358?\n'
        '12 candidates have ratios 1.63\u20132.23 \u2192 ELIMINATED',
        fontsize=9, color=SILVER, ha='center')

# Arrows down: 12 eliminated (X marks), 3 pass
for i in range(15):
    x = 1.5 + i * 0.5
    if i not in [0, 6, 10]:  # MSSM=0, VL=6, 5+5bar=10 (approx positions)
        ax.text(x, 9.5, '\u2717', fontsize=12, color=RED, ha='center')
    else:
        ax.annotate('', xy=(x, 7.5), xytext=(x, 9.8),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.6))

# 3 survivors
ax.text(5, 7.0, '3 SURVIVE', fontsize=16, color=GREEN,
        ha='center', fontweight='bold')

survivors_3 = [
    (2.5, 'MSSM\n7/5 = 1.400', GREEN),
    (5.0, 'VL doublet\n38/27 = 1.407', CYAN),
    (7.5, 'SU(5) 5+5\u0305\n40/27 = 1.481', ORANGE),
]
for x, label, color in survivors_3:
    data_point(ax, x, 6.2, '', color, size=250)
    ax.text(x, 5.5, label, fontsize=9, color=color, ha='center',
            fontweight='bold')

# Gate 2
rect2 = plt.Rectangle((1.5, 3.8), 7.0, 1.0, facecolor=GOLD, alpha=0.06,
                        edgecolor=GOLD, linewidth=2, zorder=2)
ax.add_patch(rect2)
ax.text(5, 4.5, 'GATE 2: Proton Decay', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 4.0, 'M_GUT > 10^{15.5} GeV (Super-K bound)?',
        fontsize=9, color=SILVER, ha='center')

# 5+5bar eliminated
ax.text(7.5, 4.8, '\u2717', fontsize=16, color=RED, ha='center')
ax.text(8.5, 4.8, 'M_GUT = 10^{14.9}\n< bound', fontsize=8, color=RED)

# 2 pass
ax.annotate('', xy=(2.5, 3.5), xytext=(2.5, 5.3),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.annotate('', xy=(5.0, 3.5), xytext=(5.0, 5.3),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# 2 survivors
ax.text(5, 2.8, '2 SURVIVE', fontsize=18, color=GOLD,
        ha='center', fontweight='bold')

ax.text(2.5, 1.5, 'MSSM\n7/5 = 1.400\n~30 particles\nM_GUT = 10^{17.3}',
        fontsize=10, color=GREEN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN,
                  linewidth=2))

ax.text(7.5, 1.5, 'VL Doublet (3,2,1/6)\n38/27 = 1.407\n1 particle\nM_GUT = 10^{15.5}',
        fontsize=10, color=CYAN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN,
                  linewidth=2))

# Bottom
ax.text(5, 0.3, 'Stable under threshold variation: same 2 survivors at 0.05, 0.10, 0.15, or 0.20.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys15_01_elimination_cascade.png')


# ================================================================
# FIG 2: ASYMMETRY RATIO Db2/Db1 — VL DOUBLET TOWERS
# Type: Comparison bar
# Shows: Db2/Db1 for candidates with nonzero Db1.
# VL doublet at 15:1 dramatically above all others.
# ================================================================

fig, ax = dark_fig("\u0394b\u2082/\u0394b\u2081 Asymmetry: Why the VL Doublet Works",
                   xlabel="",
                   ylabel="\u0394b\u2082 / \u0394b\u2081 ratio",
                   size=(16, 10))

asymmetry_data = [
    ('VL (3,2,\u215b)', 15.0, CYAN, '1/15 vs 1'),
    ('SU(5) 5+5\u0305', 2.5, BLUE, '2/5 vs 1'),
    ('MSSM', 25.0 / 6 / (5.0 / 2), ORANGE, '5/2 vs 25/6'),
    ('VL (1,2)', 1.67, DIM, '1/5 vs 1/3'),
    ('Sc (3,2)', 15.0, GREEN, '1/30 vs 1/2'),
    ('Sc (1,2)', 5.0 / 3, DIM, '1/10 vs 1/6'),
    ('3\u00d7Sc H', 5.0 / 3, DIM, '3/10 vs 1/2'),
]

# Sort by ratio descending
asymmetry_data.sort(key=lambda x: -x[1])
x_pos = np.arange(len(asymmetry_data))

for i, (label, ratio, color, detail) in enumerate(asymmetry_data):
    ax.bar(i, ratio, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.65)
    ax.text(i, ratio + 0.5, '%.1f' % ratio, fontsize=11, color=color,
            ha='center', fontweight='bold')
    ax.text(i, -1.5, detail, fontsize=7, color=DIM, ha='center',
            rotation=30)

ax.set_xticks(x_pos)
ax.set_xticklabels([d[0] for d in asymmetry_data], fontsize=8,
                    color=SILVER, rotation=20, ha='right')

# Highlight the VL doublet
ax.annotate('15:1 ASYMMETRY\nSmallest Y = 1/6 \u2192\nsmallest \u0394b\u2081 = 1/15\n'
            'Largest \u0394b\u2082/\u0394b\u2081 of any\nsingle multiplet',
            xy=(0, 15), xytext=(3, 13),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Note: scalar (3,2,1/6) also has ratio 15 but Db2 = 1/2 (half of VL)
ax.text(4, 12, 'Scalar (3,2,1/6) also has\nratio 15 but half the\nmagnitude \u2192 gap = 1.632',
        fontsize=8, color=GREEN, ha='center')

ax.set_xlim(-0.8, len(asymmetry_data) - 0.2)
ax.set_ylim(-3, 18)

save_fig(fig, 'phys15_02_asymmetry_ratio.png')


# ================================================================
# FIG 3: ALL 15 CANDIDATES WITH EXACT RATIONALS, COLOR-CODED
# Type: Comparison/progression
# Shows: Each candidate with its exact rational gap ratio.
# Green = survives, red = eliminated by arithmetic,
# orange = eliminated by proton decay.
# ================================================================

fig, ax = dark_fig("15 Candidates: Exact Rational Gap Ratios",
                   xlabel="",
                   ylabel="Gap ratio (exact rational)",
                   size=(18, 10))

candidates = [
    ('MSSM', 7.0 / 5, '7/5', GREEN),
    ('VL (3,2,\u215b)', 38.0 / 27, '38/27', GREEN),
    ('5+5\u0305', 40.0 / 27, '40/27', ORANGE),
    ('3\u00d7H', 1.631, '~1.631', RED),
    ('Sc (3,2)', 1.632, '~1.632', RED),
    ('Sc (1,3)', 1.664, '~1.664', RED),
    ('VL (1,2)', 1.712, '~1.712', RED),
    ('2\u00d7H', 1.712, '~1.712', RED),
    ('Sc (1,2)', 9.0 / 5, '9/5', RED),
    ('10+10\u0305', 1.948, '~1.948', RED),
    ('Sc (3,1)', 2.0, '2', RED),
    ('VL e\u1d63', 2.0, '2', RED),
    ('VL d\u1d63', 2.114, '~2.114', RED),
    ('Sc (8,1)', 2.180, '~2.180', RED),
    ('VL u\u1d63', 2.229, '~2.229', RED),
]

x_pos = np.arange(len(candidates))

for i, (label, gap, rational, color) in enumerate(candidates):
    ax.bar(i, gap, color=color, alpha=0.5, edgecolor=color,
           linewidth=1.5, width=0.7)
    ax.text(i, gap + 0.03, rational, fontsize=7, color=color,
            ha='center', fontweight='bold', rotation=45)

ax.set_xticks(x_pos)
ax.set_xticklabels([c[0] for c in candidates], fontsize=7, color=SILVER,
                    rotation=45, ha='right')

# Measured line
ax.plot([-0.5, 14.5], [1.358, 1.358], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(13, 1.38, 'Measured\n1.358', fontsize=10, color=GOLD,
        fontweight='bold')

# Threshold band
ax.fill_between([-0.5, 14.5], [1.208, 1.208], [1.508, 1.508],
                alpha=0.05, color=GREEN)
ax.text(12, 1.22, '\u00b10.15\nwindow', fontsize=8, color=GREEN)

# Legend
ax.text(10, 2.15, '\u25a0 Survives both gates', fontsize=9,
        color=GREEN, fontweight='bold')
ax.text(10, 2.05, '\u25a0 Eliminated by proton decay', fontsize=9,
        color=ORANGE, fontweight='bold')
ax.text(10, 1.95, '\u25a0 Eliminated by arithmetic', fontsize=9,
        color=RED, fontweight='bold')

ax.set_xlim(-0.8, 14.8)
ax.set_ylim(1.1, 2.35)

save_fig(fig, 'phys15_03_all_candidates_rationals.png')


# ================================================================
# FIG 4: HYPER-K DECISION TREE
# Type: Dual-path flow
# Shows: Two experimental outcomes — proton decay observed
# (VL doublet confirmed) vs nothing seen (VL doublet excluded).
# ================================================================

fig, ax = dark_canvas("The Experimental Discriminator: Hyper-Kamiokande",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# The experiment
ax.text(5, 9.3, 'HYPER-KAMIOKANDE (~2027+)', fontsize=18, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'Proton decay sensitivity: \u03c4 ~ 10\u00b3\u2075 years\n'
        '(10\u00d7 improvement over Super-K)',
        fontsize=11, color=SILVER, ha='center')

# Fork point
data_point(ax, 5, 7.0, '', WHITE, size=350)
ax.text(5, 7.0, '?', fontsize=20, color=BG, ha='center',
        fontweight='bold')

# Left branch: proton decay observed
ax.annotate('', xy=(2.5, 5.5), xytext=(4.5, 6.7),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
ax.text(2.5, 6.5, 'PROTON DECAY\nOBSERVED', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(2.5, 5.8, '\u03c4 ~ 10\u00b3\u2074\u207b\u00b3\u2075 yr', fontsize=10,
        color=GREEN, ha='center')

result_left = [
    ('\u2713 VL doublet (3,2,1/6)', 'M_GUT = 10^{15.5} \u2192 consistent', GREEN),
    ('\u2717 MSSM', 'M_GUT = 10^{17.3} \u2192 predicts \u03c4 ~ 10\u00b3\u2076\u207b\u00b3\u2077', RED),
    ('\u2717 SM (no unification)', 'No prediction', RED),
]
for i, (item, detail, color) in enumerate(result_left):
    y = 4.5 - i * 1.0
    ax.text(2.5, y, item, fontsize=10, color=color, ha='center',
            fontweight='bold')
    ax.text(2.5, y - 0.4, detail, fontsize=8, color=DIM, ha='center')

# Right branch: nothing seen
ax.annotate('', xy=(7.5, 5.5), xytext=(5.5, 6.7),
            arrowprops=dict(arrowstyle='->', color=RED, lw=3))
ax.text(7.5, 6.5, 'NO PROTON DECAY\nAFTER FULL EXPOSURE', fontsize=12,
        color=RED, ha='center', fontweight='bold')
ax.text(7.5, 5.8, '\u03c4 > 10\u00b3\u2075 yr', fontsize=10, color=RED,
        ha='center')

result_right = [
    ('\u2717 VL doublet excluded', 'Minimal single-particle fix ruled out', RED),
    ('\u2713 MSSM still viable', 'M_GUT too high for Hyper-K', GREEN),
    ('? Non-minimal extensions', 'Multi-particle or higher-rep BSM', ORANGE),
]
for i, (item, detail, color) in enumerate(result_right):
    y = 4.5 - i * 1.0
    ax.text(7.5, y, item, fontsize=10, color=color, ha='center',
            fontweight='bold')
    ax.text(7.5, y - 0.4, detail, fontsize=8, color=DIM, ha='center')

# Bottom
ax.text(5, 0.5, 'Either outcome is informative. Proton decay observed: minimal BSM identified.\n'
        'Nothing seen: minimal scenario excluded, search continues.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys15_04_hyper_k_decision.png')


# ================================================================
# FIG 5: METHOD INVERSION — MODEL-FIRST VS CONSTRAINT-FIRST
# Type: Dual-panel
# Shows: Standard approach (choose model, predict, compare) vs
# this analysis (measure, enumerate, eliminate by arithmetic).
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Standard: Model \u2192 Prediction \u2192 Compare",
    "This Analysis: Measurement \u2192 Enumerate \u2192 Eliminate",
    size=(18, 9), wspace=0.35)

# Left: standard approach
steps_standard = [
    (0.5, 'Choose a model', 'SUSY, Pati-Salam, E\u2086, ...', ORANGE),
    (0.4, 'Compute predictions', 'Gap ratio, M_GUT, proton \u03c4', ORANGE),
    (0.3, 'Compare to data', 'Does it work?', ORANGE),
    (0.2, 'If not, try another', 'Model-dependent exploration', RED),
]

for i, (y_frac, step, detail, color) in enumerate(steps_standard):
    y = 8 - i * 1.8
    ax1.text(0.5, y, '%d. %s' % (i + 1, step), fontsize=12, color=color,
             fontweight='bold', transform=ax1.transAxes,
             va='center', ha='center')
    ax1.text(0.5, y - 0.6, detail, fontsize=9, color=DIM,
             ha='center')
    if i < 3:
        ax1.annotate('', xy=(0.5, y - 0.9), xytext=(0.5, y - 0.3),
                     arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

ax1.text(0.5, 1.0, 'Theorist chooses\nthe starting point', fontsize=11,
         color=ORANGE, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE))
ax1.set_xlim(-0.5, 10)
ax1.set_ylim(0, 9)
ax1.set_xticks([])
ax1.set_yticks([])

# Right: this analysis
steps_this = [
    (0.5, 'Measure gap ratio', '1.358 from DATA-3 couplings', CYAN),
    (0.4, 'Enumerate ALL candidates', '15 within bounded scope', CYAN),
    (0.3, 'Eliminate by arithmetic', 'Exact rational gap ratios', GREEN),
    (0.2, 'State survivors', '2 remain: MSSM + VL doublet', GOLD),
]

for i, (y_frac, step, detail, color) in enumerate(steps_this):
    y = 8 - i * 1.8
    ax2.text(0.5, y, '%d. %s' % (i + 1, step), fontsize=12, color=color,
             fontweight='bold', transform=ax2.transAxes,
             va='center', ha='center')
    ax2.text(0.5, y - 0.6, detail, fontsize=9, color=DIM,
             ha='center')
    if i < 3:
        ax2.annotate('', xy=(0.5, y - 0.9), xytext=(0.5, y - 0.3),
                     arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

ax2.text(0.5, 1.0, 'Arithmetic chooses\nthe result', fontsize=11,
         color=GOLD, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))
ax2.set_xlim(-0.5, 10)
ax2.set_ylim(0, 9)
ax2.set_xticks([])
ax2.set_yticks([])

save_fig(fig, 'phys15_05_method_inversion.png')


# ================================================================
# FIG 6: ALL 15 GAP RATIOS ON NUMBER LINE WITH MEASURED
# Type: Scale/landscape
# Shows: All 15 exact rational gap ratios as points on a number line.
# The measured value at 1.358. The clustering and spread visible.
# ================================================================

fig, ax = dark_fig("15 Gap Ratios on One Number Line",
                   xlabel="Gap ratio",
                   ylabel="",
                   size=(16, 8))

all_gaps = [
    ('MSSM', 1.400, GREEN),
    ('VL (3,2)', 1.407, CYAN),
    ('5+5\u0305', 1.481, ORANGE),
    ('3\u00d7H', 1.631, DIM),
    ('Sc (3,2)', 1.632, DIM),
    ('Sc (1,3)', 1.664, DIM),
    ('VL (1,2)', 1.712, DIM),
    ('2\u00d7H', 1.712, DIM),
    ('Sc (1,2)', 1.800, DIM),
    ('10+10\u0305', 1.948, DIM),
    ('Sc (3,1)', 2.000, DIM),
    ('VL e', 2.000, DIM),
    ('VL d', 2.114, DIM),
    ('Sc (8,1)', 2.180, DIM),
    ('VL u', 2.229, DIM),
]

# Main line
ax.plot([1.2, 2.4], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Measured value
ax.plot([1.358, 1.358], [0.0, 1.0], color=GOLD, linewidth=3)
data_point(ax, 1.358, 0.5, '', GOLD, size=400)
ax.text(1.358, 1.3, 'Measured\n1.358', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')

# All candidates
for i, (label, gap, color) in enumerate(all_gaps):
    y_off = 0.15 * ((-1) ** i)  # alternate above/below
    ax.plot([gap, gap], [0.3, 0.7], color=color, linewidth=2)
    data_point(ax, gap, 0.5, '', color, size=100)
    if gap < 1.5 or gap > 2.1:  # label the extremes and survivors
        ax.text(gap, 0.5 + y_off + 0.3 * (1 if y_off > 0 else -1),
                label, fontsize=7, color=color, ha='center',
                fontweight='bold')

# SM gap ratio
ax.plot([218.0 / 115, 218.0 / 115], [0.2, 0.8], color=RED, linewidth=2.5)
ax.text(218.0 / 115, 1.3, 'SM\n218/115', fontsize=10, color=RED,
        ha='center', fontweight='bold')

# Window
ax.fill_between([1.208, 1.508], [0.1, 0.1], [0.9, 0.9],
                alpha=0.06, color=GREEN)

# The desert between survivors and pack
ax.annotate('Gap: 0.15', xy=(1.55, 0.3), xytext=(1.55, -0.3),
            fontsize=9, color=GOLD, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1))

ax.set_xlim(1.2, 2.35)
ax.set_ylim(-0.8, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys15_06_number_line.png')


# ================================================================
# FIG 7: BETA FUNCTION SHIFT — BEFORE AND AFTER VL DOUBLET
# Type: Comparison bar (paired)
# Shows: b_i values before (SM) and after (SM + VL doublet).
# The shift in b2 is dramatic.
# ================================================================

fig, ax = dark_fig("Beta Coefficients: Before and After the VL Doublet",
                   xlabel="",
                   ylabel="Beta coefficient b_i",
                   size=(16, 10))

labels = ['b\u2081 (U(1))', 'b\u2082 (SU(2))', 'b\u2083 (SU(3))']
sm_vals = [41.0 / 10, -19.0 / 6, -7.0]
vl_vals = [25.0 / 6, -13.0 / 6, -20.0 / 3]
delta_vals = [1.0 / 15, 1.0, 1.0 / 3]

bar_width = 0.3
x_pos = np.arange(3)

# SM bars
for i in range(3):
    ax.bar(i - bar_width / 2 - 0.02, sm_vals[i], color=RED, alpha=0.5,
           edgecolor=RED, linewidth=2, width=bar_width)
    ax.text(i - bar_width / 2, sm_vals[i] + (0.3 if sm_vals[i] > 0 else -0.5),
            '%.3f' % sm_vals[i], fontsize=9, color=RED, ha='center',
            fontweight='bold')

# VL bars
for i in range(3):
    ax.bar(i + bar_width / 2 + 0.02, vl_vals[i], color=CYAN, alpha=0.5,
           edgecolor=CYAN, linewidth=2, width=bar_width)
    ax.text(i + bar_width / 2, vl_vals[i] + (0.3 if vl_vals[i] > 0 else -0.5),
            '%.3f' % vl_vals[i], fontsize=9, color=CYAN, ha='center',
            fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=11, color=SILVER)

# Delta annotations
delta_labels = ['\u0394 = 1/15\n(tiny)', '\u0394 = 1\n(LARGE)', '\u0394 = 1/3\n(moderate)']
delta_colors = [DIM, GOLD, SILVER]
for i in range(3):
    mid_y = (sm_vals[i] + vl_vals[i]) / 2
    ax.annotate(delta_labels[i], xy=(i, mid_y),
                xytext=(i + 0.8, mid_y + 1),
                fontsize=9, color=delta_colors[i], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=delta_colors[i], lw=1.5))

# Legend
ax.bar(-1, 0, color=RED, alpha=0.5, width=0.01, label='SM (before)')
ax.bar(-1, 0, color=CYAN, alpha=0.5, width=0.01, label='SM + VL doublet (after)')
legend(ax, loc='lower left')

# The key insight
result_box(ax, 1, -7.5,
           '\u0394b\u2082 = 1 is the dominant shift.\n'
           'It shrinks b\u2081\u2212b\u2082 by 13%\nand grows b\u2082\u2212b\u2083 by 17%.\n'
           'Gap ratio: 218/115 \u2192 38/27\n(1.896 \u2192 1.407)',
           GOLD, 10)

ax.set_xlim(-0.8, 3.5)
ax.set_ylim(-8.5, 6)

save_fig(fig, 'phys15_07_beta_shift.png')


# ================================================================
# FIG 8: PHYS-15 IDENTITY CARD
# Type: Identity card
# Shows: 15 -> 2, 38/27, integers chose it, Hyper-K testable.
# ================================================================

fig, ax = dark_canvas("PHYS-15 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE INTEGERS CHOSE IT', fontsize=20, color=GOLD,
        ha='center', fontweight='bold')

# The cascade summary
ax.text(5, 8.2, '15 candidates \u2192 3 (arithmetic) \u2192 2 (proton decay)',
        fontsize=14, color=WHITE, ha='center', fontweight='bold')

# Left: the survivor
ax.text(2.5, 7.0, 'THE MINIMAL SURVIVOR', fontsize=13, color=CYAN,
        ha='center', fontweight='bold')

vl_items = [
    ('Representation:', '(3, 2, 1/6)', CYAN),
    ('Charges:', '+2/3 and \u22121/3', CYAN),
    ('SM analog:', 'Copy of (u_L, d_L)', SILVER),
    ('Gap ratio:', '38/27 = 1.407', GOLD),
    ('Distance:', '0.049 from measured', GOLD),
    ('M_GUT:', '10^{15.5} GeV', GREEN),
    ('New particles:', '1', GREEN),
]
for i, (prop, val, color) in enumerate(vl_items):
    y = 6.2 - i * 0.55
    ax.text(1.0, y, prop, fontsize=9, color=SILVER)
    ax.text(3.5, y, val, fontsize=10, color=color, fontweight='bold')

# Right: the method
ax.text(7.5, 7.0, 'THE METHOD', fontsize=13, color=GREEN,
        ha='center', fontweight='bold')

method_items = [
    ('Scope:', 'dim(SU(3))\u22648, dim(SU(2))\u22644, |Y|\u22642', SILVER),
    ('Gate 1:', 'Gap ratio within \u00b10.15 of 1.358', RED),
    ('Gate 2:', 'M_GUT > 10^{15.5} (Super-K)', GOLD),
    ('Arithmetic:', 'Exact Fraction (every ratio rational)', GREEN),
    ('Stability:', 'Same 2 survivors at any threshold', GREEN),
]
for i, (prop, val, color) in enumerate(method_items):
    y = 6.2 - i * 0.55
    ax.text(5.5, y, prop, fontsize=9, color=SILVER)
    ax.text(7.0, y, val, fontsize=8, color=color)

# The three rationals
ax.plot([0.5, 9.5], [2.8, 2.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 2.3, 'THREE EXACT RATIONALS', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

rationals = [
    ('SM:', '218/115', '= 1.896', RED, '40% miss'),
    ('VL doublet:', '38/27', '= 1.407', CYAN, '3.6% miss'),
    ('MSSM:', '7/5', '= 1.400', GREEN, '3.1% miss'),
]
for i, (model, frac, dec, color, miss) in enumerate(rationals):
    x = 1.5 + i * 3.0
    ax.text(x, 1.7, model, fontsize=10, color=SILVER, ha='center')
    ax.text(x, 1.1, frac, fontsize=16, color=color, ha='center',
            fontweight='bold', fontfamily='monospace')
    ax.text(x, 0.6, '%s (%s)' % (dec, miss), fontsize=8, color=DIM,
            ha='center')

# Bottom
ax.text(5, 0.1, 'Testable by Hyper-Kamiokande within the next decade.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys15_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-15 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys15_01_elimination_cascade.png',
    'phys15_02_asymmetry_ratio.png',
    'phys15_03_all_candidates_rationals.png',
    'phys15_04_hyper_k_decision.png',
    'phys15_05_method_inversion.png',
    'phys15_06_number_line.png',
    'phys15_07_beta_shift.png',
    'phys15_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))