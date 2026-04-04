#!/usr/bin/env python3
"""
HOWL PHYS-17 Diagrams — The Generation Democracy and the Boson Problem
8 figures covering SU(5) democracy origin, gap ratio anatomy, guilty/innocent,
pure-gauge waterfall, Higgs doublet multiplicity, Casimir ratio.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: SU(5) ORIGIN OF DEMOCRACY
# Type: Geometric/connection
# Shows: One SM generation fills 5-bar + 10 of SU(5). The anomaly
# cancellation condition forces equal Dynkin indices for all three
# gauge factors, producing (4/3, 4/3, 4/3).
# ================================================================

fig, ax = dark_canvas("SU(5) Origin of the Generation Democracy",
                      size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'Why \u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3 Per Generation',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# The SU(5) multiplets
ax.text(2.5, 8.0, '5\u0305 of SU(5)', fontsize=16, color=CYAN,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN,
                  linewidth=2))

five_bar = [
    ('(1, 2, \u22121/2)', 'Lepton doublet (\u03bd, e)_L', CYAN),
    ('(3\u0305, 1, 1/3)', 'Down antiquark d\u0305_R', GREEN),
]
for i, (rep, name, color) in enumerate(five_bar):
    y = 7.0 - i * 0.7
    ax.text(2.5, y, '%s  \u2192  %s' % (rep, name), fontsize=9,
            color=color, ha='center')

ax.text(7.5, 8.0, '10 of SU(5)', fontsize=16, color=ORANGE,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=ORANGE,
                  linewidth=2))

ten_rep = [
    ('(3, 2, 1/6)', 'Quark doublet (u, d)_L', ORANGE),
    ('(3\u0305, 1, \u22122/3)', 'Up antiquark u\u0305_R', RED),
    ('(1, 1, 1)', 'Positron e\u207a_R', MAG),
]
for i, (rep, name, color) in enumerate(ten_rep):
    y = 7.0 - i * 0.7
    ax.text(7.5, y, '%s  \u2192  %s' % (rep, name), fontsize=9,
            color=color, ha='center')

# Arrow down to the result
ax.annotate('', xy=(5.0, 4.5), xytext=(2.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax.annotate('', xy=(5.0, 4.5), xytext=(7.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

ax.text(5.0, 4.8, 'SU(5) anomaly cancellation', fontsize=12, color=SILVER,
        ha='center', fontweight='bold')
ax.text(5.0, 4.3, 'A(5\u0305) + A(10) = 0', fontsize=11, color=WHITE,
        ha='center', fontfamily='monospace')

# The result
result_rect = plt.Rectangle((2.0, 2.5), 6.0, 1.2, facecolor=GOLD, alpha=0.06,
                              edgecolor=GOLD, linewidth=2.5, zorder=2)
ax.add_patch(result_rect)

ax.text(5.0, 3.3, 'FORCES EQUAL DYNKIN INDICES:', fontsize=12,
        color=WHITE, ha='center', fontweight='bold')
ax.text(5.0, 2.8, '\u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3',
        fontsize=20, color=GOLD, ha='center', fontweight='bold',
        fontfamily='monospace')

# Consequence
ax.text(5.0, 1.5, 'CONSEQUENCE', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(5.0, 0.8, '\u0394(b\u2081 \u2212 b\u2082) = 4/3 \u2212 4/3 = 0\n'
        '\u0394(b\u2082 \u2212 b\u2083) = 4/3 \u2212 4/3 = 0\n'
        'Fermions are INVISIBLE to the gap ratio. For ANY number of generations.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys17_01_su5_democracy.png')


# ================================================================
# FIG 2: GAP RATIO ANATOMY — THREE SOURCES
# Type: Comparison bar
# Shows: Numerator and denominator decomposed into gauge, fermion,
# Higgs contributions. Fermion = 0 in both.
# ================================================================

fig = plt.figure(figsize=(18, 10), facecolor=BG)

# Left: numerator
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_facecolor(BG)

num_sources = [
    ('Gauge\n0 \u2212 (\u221222/3)', 22.0 / 3, CYAN, '100.9%'),
    ('Fermions\n4/3 \u2212 4/3', 0, RED, '0%'),
    ('Higgs\n1/10 \u2212 1/6', -1.0 / 15, ORANGE, '\u22120.9%'),
]

for i, (label, value, color, pct) in enumerate(num_sources):
    ax1.bar(i, max(value, 0.15), color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6, bottom=0 if value >= 0 else value)
    if value == 0:
        ax1.text(i, 0.5, 'ZERO', fontsize=16, color=RED, ha='center',
                 fontweight='bold')
    else:
        y_label = value + 0.3 if value > 0 else value - 0.4
        ax1.text(i, y_label, '%.3f' % value, fontsize=10, color=color,
                 ha='center', fontweight='bold')
    ax1.text(i, -1.2, pct, fontsize=11, color=color, ha='center',
             fontweight='bold')

ax1.set_title('NUMERATOR: b\u2081 \u2212 b\u2082 = 109/15', fontsize=13,
              color=WHITE, fontweight='bold', pad=15)
ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['Gauge', 'Fermions', 'Higgs'], fontsize=10, color=SILVER)
ax1.set_ylabel('Contribution', fontsize=11, color=SILVER)
ax1.set_ylim(-2, 9)
ax1.tick_params(colors=DIM)
for spine in ax1.spines.values():
    spine.set_color(PAN)

# Right: denominator
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_facecolor(BG)

den_sources = [
    ('Gauge\n\u221222/3 \u2212 (\u221211)', 11.0 / 3, CYAN, '95.7%'),
    ('Fermions\n4/3 \u2212 4/3', 0, RED, '0%'),
    ('Higgs\n1/6 \u2212 0', 1.0 / 6, ORANGE, '4.3%'),
]

for i, (label, value, color, pct) in enumerate(den_sources):
    ax2.bar(i, max(value, 0.15), color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6)
    if value == 0:
        ax2.text(i, 0.5, 'ZERO', fontsize=16, color=RED, ha='center',
                 fontweight='bold')
    else:
        ax2.text(i, value + 0.3, '%.3f' % value, fontsize=10, color=color,
                 ha='center', fontweight='bold')
    ax2.text(i, -1.2, pct, fontsize=11, color=color, ha='center',
             fontweight='bold')

ax2.set_title('DENOMINATOR: b\u2082 \u2212 b\u2083 = 23/6', fontsize=13,
              color=WHITE, fontweight='bold', pad=15)
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Gauge', 'Fermions', 'Higgs'], fontsize=10, color=SILVER)
ax2.set_ylim(-2, 9)
ax2.tick_params(colors=DIM)
for spine in ax2.spines.values():
    spine.set_color(PAN)

fig.suptitle('Gap Ratio Anatomy: ~97% Gauge, 0% Fermion, ~3% Higgs',
             fontsize=15, color=GOLD, fontweight='bold', y=0.98)
fig.tight_layout(rect=[0, 0.02, 1, 0.94])

path = os.path.join(get_outdir(), 'phys17_02_gap_ratio_anatomy.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys17_02_gap_ratio_anatomy.png")


# ================================================================
# FIG 3: GUILTY AND INNOCENT — ALL SM PARTICLES
# Type: Dual-panel comparison
# Shows: Left: 12 fermions, all INNOCENT (0% gap ratio contribution).
# Right: gauge bosons + Higgs, GUILTY (100%).
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "INNOCENT: 0% of Gap Ratio",
    "GUILTY: 100% of Gap Ratio",
    size=(18, 9), wspace=0.35)

# Left: innocent fermions
fermions = [
    ('e', CYAN), ('\u03bc', CYAN), ('\u03c4', CYAN),
    ('\u03bd_e', BLUE), ('\u03bd_\u03bc', BLUE), ('\u03bd_\u03c4', BLUE),
    ('u', GREEN), ('c', GREEN), ('t', GREEN),
    ('d', ORANGE), ('s', ORANGE), ('b', ORANGE),
]

for i, (name, color) in enumerate(fermions):
    row = i // 4
    col = i % 4
    x = 0.5 + col * 2.5
    y = 7 - row * 2.5
    data_point(ax1, x, y, '', color, size=250)
    ax1.text(x, y - 0.8, name, fontsize=10, color=color, ha='center',
             fontweight='bold')

# Big INNOCENT stamp
ax1.text(5, 1.0, 'ALL 12 FERMIONS', fontsize=14, color=GREEN,
         ha='center', fontweight='bold')
ax1.text(5, 0.2, '\u0394(b\u2081\u2212b\u2082) = 0\n\u0394(b\u2082\u2212b\u2083) = 0\n'
         'Contribution to gap ratio: ZERO',
         fontsize=10, color=GREEN, ha='center', fontweight='bold')

ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 9)
ax1.set_xticks([])
ax1.set_yticks([])

# Right: guilty bosons
guilty = [
    ('\u03b3 (U(1))', 'b\u2081 = 0\n(abelian)', CYAN, 2.5, 7),
    ('W\u00b1, Z (SU(2))', 'b\u2082 = \u221222/3', GREEN, 7.5, 7),
    ('g \u00d7 8 (SU(3))', 'b\u2083 = \u221211', RED, 5, 4.5),
    ('H (Higgs)', '\u0394b = (1/10, 1/6, 0)', GOLD, 5, 2),
]

for name, detail, color, x, y in guilty:
    data_point(ax2, x, y, '', color, size=400)
    ax2.text(x, y + 0.8, name, fontsize=11, color=color, ha='center',
             fontweight='bold')
    ax2.text(x, y - 0.8, detail, fontsize=8, color=SILVER, ha='center')

ax2.text(5, 0.2, 'GAUGE + HIGGS = 100%\n'
         'The gap ratio 218/115\nis determined entirely here.',
         fontsize=10, color=RED, ha='center', fontweight='bold')

ax2.set_xlim(0, 10)
ax2.set_ylim(-1, 9)
ax2.set_xticks([])
ax2.set_yticks([])

save_fig(fig, 'phys17_03_guilty_innocent.png')


# ================================================================
# FIG 4: PURE GAUGE → HIGGS CORRECTION → TARGET
# Type: Waterfall
# Shows: Start at 2.000 (pure gauge). Higgs correction to 1.896.
# Target at 1.358. The 16% vs 84% split.
# ================================================================

fig, ax = dark_fig("From Pure Gauge to the SM: The Higgs Provides 16%",
                   xlabel="",
                   ylabel="Gap ratio",
                   size=(16, 10))

# Three bars as waterfall
stages = [
    ('Pure gauge\n22/11', 2.000, None, CYAN, 'C\u2082(SU(2))\n/(C\u2082(SU(3))\u2212C\u2082(SU(2)))\n= 2/(3\u22122) = 2'),
    ('Higgs\ncorrection', 1.896, -0.104, ORANGE, '(1/10, 1/6, 0)\nMoves ratio down\nby 0.104 (16%)'),
    ('SM total\n218/115', 1.896, None, RED, 'Still 40% above\nmeasured'),
]

# Pure gauge bar
ax.bar(0, 2.000, color=CYAN, alpha=0.5, edgecolor=CYAN, linewidth=2, width=0.7)
ax.text(0, 2.05, '2.000', fontsize=16, color=CYAN, ha='center', fontweight='bold')
ax.text(0, 2.25, stages[0][4], fontsize=8, color=SILVER, ha='center')

# Higgs correction (negative)
ax.bar(1.2, -0.104, bottom=2.000, color=ORANGE, alpha=0.5, edgecolor=ORANGE,
       linewidth=2, width=0.7)
ax.text(1.2, 1.94, '\u22120.104', fontsize=12, color=ORANGE, ha='center',
        fontweight='bold')
ax.text(1.2, 2.15, 'Higgs\ncorrection', fontsize=10, color=ORANGE,
        ha='center', fontweight='bold')

# Connector line
ax.plot([0.35, 0.85], [2.000, 2.000], color=DIM, linewidth=1.5,
        linestyle=':', alpha=0.5)

# SM result bar
ax.bar(2.4, 1.896, color=RED, alpha=0.5, edgecolor=RED, linewidth=2, width=0.7)
ax.text(2.4, 1.93, '1.896', fontsize=16, color=RED, ha='center', fontweight='bold')
ax.text(2.4, 1.6, 'SM\n218/115', fontsize=10, color=RED, ha='center',
        fontweight='bold')

# Measured target
ax.plot([-0.5, 3.5], [1.358, 1.358], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(3.3, 1.38, 'Measured\n1.358', fontsize=12, color=GOLD, fontweight='bold')

# The 16% vs 84% split
ax.annotate('', xy=(3.2, 1.358), xytext=(3.2, 1.896),
            arrowprops=dict(arrowstyle='<->', color=MAG, lw=2))
ax.text(3.8, 1.63, 'Remaining gap\n0.538 (84%)\n\u2192 BSM needed', fontsize=10,
        color=MAG, fontweight='bold')

ax.annotate('', xy=(1.7, 1.896), xytext=(1.7, 2.000),
            arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2))
ax.text(0.3, 1.0, 'Higgs closes 16%.\nBSM must close 84%.\nFermions close 0%.',
        fontsize=11, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

ax.set_xlim(-0.8, 4.5)
ax.set_ylim(1.0, 2.5)
ax.set_xticks([])

save_fig(fig, 'phys17_04_waterfall.png')


# ================================================================
# FIG 5: GAP RATIO VS NUMBER OF HIGGS DOUBLETS
# Type: Running/comparison
# Shows: Gap ratio decreasing as more Higgs doublets are added.
# Crossover at N_H = 8, where gap = 34/25 = 1.360.
# Not viable but shows the Higgs correction's direction.
# ================================================================

fig, ax = dark_fig("Gap Ratio vs Number of Higgs Doublets",
                   xlabel="Number of Higgs doublets N_H",
                   ylabel="Gap ratio",
                   size=(16, 10))

n_h_vals = np.arange(1, 12)
gap_vals = []

for n_h in n_h_vals:
    num = 22.0 / 3 - n_h / 15.0
    den = 11.0 / 3 + n_h / 6.0
    gap_vals.append(num / den)

gap_vals = np.array(gap_vals)

curve(ax, n_h_vals, gap_vals, 'Gap ratio = (22/3 \u2212 N_H/15) / (11/3 + N_H/6)',
      CYAN, 2.5)

for n_h in n_h_vals:
    color = GREEN if abs(gap_vals[int(n_h) - 1] - 1.358) < 0.05 else DIM
    if n_h <= 3 or n_h == 8 or n_h >= 10:
        data_point(ax, n_h, gap_vals[int(n_h) - 1], '', color, size=150)

# Highlight SM (N_H = 1)
data_point(ax, 1, gap_vals[0], '', RED, size=300)
ax.text(1, gap_vals[0] + 0.03, 'SM\n218/115', fontsize=10, color=RED,
        ha='center', fontweight='bold')

# Highlight crossover (N_H = 8)
data_point(ax, 8, gap_vals[7], '', GOLD, size=300)
ax.annotate('N_H = 8: gap = 34/25 = 1.360\n(closest to measured 1.358)',
            xy=(8, gap_vals[7]), xytext=(5, 1.5),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Measured line
ax.plot([0, 12], [1.358, 1.358], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.6)
ax.text(10.5, 1.37, 'Measured\n1.358', fontsize=9, color=GOLD,
        fontweight='bold')

# Not viable note
note(ax, 6, 1.8,
     '7 extra Higgs doublets would be needed.\n'
     'Not viable: destroys vacuum stability,\n'
     'contradicts Higgs coupling measurements.\n\n'
     'The Cabibbo Doublet achieves 38/27 = 1.407\n'
     'with ONE particle.',
     SILVER, 9)

ax.set_xlim(0, 11.5)
ax.set_ylim(1.1, 2.05)
ax.set_xticks(range(1, 12))

save_fig(fig, 'phys17_05_higgs_multiplicity.png')


# ================================================================
# FIG 6: CASIMIR RATIO — PURE-GAUGE GAP = 2
# Type: Geometric
# Shows: C2(SU(2)) = 2, C2(SU(3)) = 3. The pure-gauge gap ratio
# is C2(SU(2)) / (C2(SU(3)) - C2(SU(2))) = 2/1 = 2.
# The integer 11 cancels.
# ================================================================

fig, ax = dark_canvas("The Pure-Gauge Gap Ratio: A Casimir Ratio",
                      size=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# The two Casimirs as boxes
ax.text(3, 8.0, 'C\u2082(SU(2)) = 2', fontsize=22, color=GREEN,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN,
                  linewidth=2.5))

ax.text(7, 8.0, 'C\u2082(SU(3)) = 3', fontsize=22, color=RED,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED,
                  linewidth=2.5))

# The formula chain
ax.text(5, 6.5, 'Gauge self-coupling: \u221211 \u00d7 C\u2082(G) / 3', fontsize=13,
        color=SILVER, ha='center')

ax.text(5, 5.5, 'Gap ratio (pure gauge):', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

# The fraction
ax.text(5, 4.5, 'C\u2082(SU(2))', fontsize=16, color=GREEN,
        ha='center', fontweight='bold')
ax.plot([3.5, 6.5], [4.1, 4.1], color=WHITE, linewidth=2)
ax.text(5, 3.5, 'C\u2082(SU(3)) \u2212 C\u2082(SU(2))', fontsize=16,
        color=SILVER, ha='center', fontweight='bold')

# The evaluation
ax.text(7.5, 4.0, '=', fontsize=22, color=WHITE, ha='center',
        fontweight='bold')

ax.text(8.5, 4.5, '2', fontsize=22, color=GREEN, ha='center',
        fontweight='bold')
ax.plot([8.0, 9.0], [4.1, 4.1], color=WHITE, linewidth=2)
ax.text(8.5, 3.5, '3 \u2212 2', fontsize=22, color=RED, ha='center',
        fontweight='bold')

ax.text(9.5, 4.0, '= 2', fontsize=28, color=GOLD, ha='center',
        fontweight='bold')

# The key insight
result_box(ax, 5.0, 2.0,
           'The integer 11 CANCELS in the ratio.\n'
           'The pure-gauge gap = 2 depends only on\n'
           'which gauge groups are present (SU(2) and SU(3)),\n'
           'not on the Yang-Mills coefficient.\n\n'
           '11 sets the SCALE of running (how fast).\n'
           'The Casimirs set the RATIO (how unequal).',
           GOLD, 10)

save_fig(fig, 'phys17_06_casimir_ratio.png')


# ================================================================
# FIG 7: THREE MILESTONES — 2.000, 1.896, 1.358
# Type: Scale/comparison
# Shows: Number line with pure gauge (2.000), SM (1.896), and
# measured (1.358). The distances between them.
# ================================================================

fig, ax = dark_fig("Three Milestones on the Gap Ratio Scale",
                   xlabel="Gap ratio",
                   ylabel="",
                   size=(16, 8))

# Number line
ax.plot([1.2, 2.15], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Pure gauge
ax.plot([2.0, 2.0], [0.1, 0.9], color=CYAN, linewidth=3)
data_point(ax, 2.0, 0.5, '', CYAN, size=350)
ax.text(2.0, 1.3, 'Pure gauge\n22/11 = 2.000', fontsize=13, color=CYAN,
        ha='center', fontweight='bold')
ax.text(2.0, -0.3, 'No matter.\nOnly gauge bosons.', fontsize=8,
        color=DIM, ha='center')

# SM
ax.plot([1.896, 1.896], [0.1, 0.9], color=RED, linewidth=3)
data_point(ax, 1.896, 0.5, '', RED, size=350)
ax.text(1.896, -0.5, 'SM\n218/115 = 1.896', fontsize=13, color=RED,
        ha='center', fontweight='bold')
ax.text(1.896, -1.2, 'Gauge + Higgs.\nFermions add nothing.', fontsize=8,
        color=DIM, ha='center')

# Measured
ax.plot([1.358, 1.358], [0.1, 0.9], color=GOLD, linewidth=3)
data_point(ax, 1.358, 0.5, '', GOLD, size=350)
ax.text(1.358, 1.3, 'Measured\n1.358', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')
ax.text(1.358, -0.3, 'From 3 couplings\nat M_Z (DATA-3).', fontsize=8,
        color=DIM, ha='center')

# Distance arrows
ax.annotate('', xy=(1.896, 1.8), xytext=(2.0, 1.8),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(1.948, 2.0, 'Higgs: \u22120.104\n(16%)', fontsize=10, color=ORANGE,
        ha='center', fontweight='bold')

ax.annotate('', xy=(1.358, -1.5), xytext=(1.896, -1.5),
            arrowprops=dict(arrowstyle='<->', color=MAG, lw=2))
ax.text(1.627, -1.8, 'BSM needed: \u22120.538\n(84%)', fontsize=10,
        color=MAG, ha='center', fontweight='bold')

ax.annotate('', xy=(1.358, -2.3), xytext=(2.0, -2.3),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=2))
ax.text(1.679, -2.6, 'Total correction needed: \u22120.642\n(from 2.000 to 1.358)',
        fontsize=10, color=WHITE, ha='center', fontweight='bold')

ax.set_xlim(1.2, 2.15)
ax.set_ylim(-3.0, 2.5)
ax.set_yticks([])

save_fig(fig, 'phys17_07_three_milestones.png')


# ================================================================
# FIG 8: PHYS-17 IDENTITY CARD
# Type: Identity card
# Shows: Generation democracy, boson problem, integer 11.
# ================================================================

fig, ax = dark_canvas("PHYS-17 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE GENERATION DEMOCRACY AND THE BOSON PROBLEM',
        fontsize=16, color=GOLD, ha='center', fontweight='bold')

# Left: the democracy
ax.text(2.5, 8.0, 'THE DEMOCRACY', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')

ax.text(2.5, 7.0, '\u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3',
        fontsize=18, color=GREEN, ha='center', fontweight='bold',
        fontfamily='monospace')
ax.text(2.5, 6.3, 'Per complete SM generation.\nFrom SU(5) anomaly cancellation.\n'
        'Equal for ALL three gauge forces.',
        fontsize=9, color=SILVER, ha='center')

democracy_items = [
    ('12 fermions contribute:', '0%', GREEN),
    ('Gap ratio for N = 0:', '218/115', CYAN),
    ('Gap ratio for N = 3:', '218/115', CYAN),
    ('Gap ratio for N = \u221e:', '218/115', CYAN),
]
for i, (item, val, color) in enumerate(democracy_items):
    y = 5.0 - i * 0.5
    ax.text(1.0, y, item, fontsize=9, color=SILVER)
    ax.text(4.0, y, val, fontsize=10, color=color, fontweight='bold')

# Right: the boson problem
ax.text(7.5, 8.0, 'THE BOSON PROBLEM', fontsize=14, color=RED,
        ha='center', fontweight='bold')

ax.text(7.5, 7.0, 'Gauge: (0, \u221222/3, \u221211)', fontsize=14,
        color=CYAN, ha='center', fontweight='bold', fontfamily='monospace')
ax.text(7.5, 6.3, 'Yang-Mills integer 11 \u00d7 Casimirs.\n'
        'U(1) gets ZERO (abelian).\nMaximally asymmetric.',
        fontsize=9, color=SILVER, ha='center')

boson_items = [
    ('Pure gauge gap ratio:', '22/11 = 2.000', CYAN),
    ('Higgs correction:', '\u22120.104 (16%)', ORANGE),
    ('SM gap ratio:', '218/115 = 1.896', RED),
    ('BSM needed:', '84% of total correction', MAG),
]
for i, (item, val, color) in enumerate(boson_items):
    y = 5.0 - i * 0.5
    ax.text(6.0, y, item, fontsize=9, color=SILVER)
    ax.text(9.0, y, val, fontsize=10, color=color, fontweight='bold')

# Bottom
ax.plot([0.5, 9.5], [2.5, 2.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 1.8, 'THE THESIS', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 0.8, 'The unification failure of the Standard Model is a BOSON problem.\n'
        'The gap ratio 218/115 originates in the gauge self-coupling asymmetry\n'
        '(0 vs \u221222/3 vs \u221211) with a 16% Higgs correction.\n'
        'Every quark, every lepton, every neutrino is innocent.\n'
        'Fixing unification requires BSM content that BREAKS the democracy.',
        fontsize=10, color=SILVER, ha='center')

save_fig(fig, 'phys17_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-17 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys17_01_su5_democracy.png',
    'phys17_02_gap_ratio_anatomy.png',
    'phys17_03_guilty_innocent.png',
    'phys17_04_waterfall.png',
    'phys17_05_higgs_multiplicity.png',
    'phys17_06_casimir_ratio.png',
    'phys17_07_three_milestones.png',
    'phys17_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    