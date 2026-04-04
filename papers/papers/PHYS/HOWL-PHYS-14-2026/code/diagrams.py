#!/usr/bin/env python3
"""
HOWL PHYS-14 Diagrams — The Unified Transformation Map
8 figures covering complete domain map, fermion cancellation, gauge asymmetry,
gap ratio decomposition, energy axis, boson problem thesis.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: COMPLETE DOMAIN MAP — m_e TO M_GUT
# Type: Connection map/landscape
# Shows: All 10 domains with thresholds, confinement wall,
# EW transition, beta coefficients, and regime labels.
# ================================================================

fig, ax = dark_canvas("The Unified Transformation Map: m_e to M_GUT",
                      size=(20, 12))
ax.set_xlim(-1, 18)
ax.set_ylim(-2, 8)

# Energy axis at bottom
ax.plot([-0.5, 17.5], [0, 0], color=DIM, linewidth=2, alpha=0.5)

# Thresholds with log10 positions (compressed for display)
thresholds = [
    (0.5, 'm_e\n0.511 MeV', SILVER, 'e activates'),
    (2.5, 'm_\u03bc\n106 MeV', SILVER, '\u03bc activates'),
    (4.0, '\u039b_QCD\n~300 MeV', RED, 'CONFINEMENT'),
    (5.5, '~2 GeV', RED, 'Pert. resumes'),
    (6.5, 'm_c\n1.27 GeV', SILVER, 'c activates'),
    (7.5, 'm_\u03c4\n1.78 GeV', SILVER, '\u03c4 activates'),
    (8.5, 'm_b\n4.18 GeV', SILVER, 'b activates'),
    (10.5, 'M_W\n80.4 GeV', GOLD, 'EW TRANSITION'),
    (11.5, 'M_Z\n91.2', DIM, ''),
    (12.0, 'm_H\n125', DIM, ''),
    (13.0, 'm_t\n173 GeV', ORANGE, 'Full SM'),
    (16.5, 'M_GUT\n10\u00b9\u00b3\u00b7\u2078', MAG, 'Unification test'),
]

for x, label, color, note_text in thresholds:
    ax.plot([x, x], [-0.3, 0.3], color=color, linewidth=2)
    ax.text(x, -0.8, label, fontsize=6, color=color, ha='center',
            fontweight='bold')
    if note_text:
        ax.text(x, 0.6, note_text, fontsize=6, color=color, ha='center')

# Confinement wall (shaded)
ax.fill_between([3.5, 5.8], [-0.3, -0.3], [5, 5], alpha=0.06, color=RED)
ax.text(4.65, 4.5, 'CONFINEMENT\nWALL\n(no perturbative\nmap)', fontsize=8,
        color=RED, ha='center', fontweight='bold')

# EW transition (highlighted)
ax.plot([10.5, 10.5], [-0.3, 5.5], color=GOLD, linewidth=3, alpha=0.3)

# Regime labels
ax.text(1.5, 5.5, 'BROKEN PHASE\n\u03b1_em + \u03b1_s\n(2 couplings)', fontsize=10,
        color=CYAN, ha='center', fontweight='bold')
ax.text(14, 5.5, 'SYMMETRIC PHASE\n\u03b1\u2081 + \u03b1\u2082 + \u03b1\u2083\n(3 couplings)',
        fontsize=10, color=GREEN, ha='center', fontweight='bold')

# Beta coefficients in key domains
domains_beta = [
    (1.5, 'b_em = \u22124/3', CYAN, 2.5),
    (7.0, 'b\u2083 = \u221225/3', RED, 2.5),
    (9.5, 'b\u2083 = \u221223/3', RED, 2.0),
    (14.5, 'b\u2081=41/10\nb\u2082=\u221219/6\nb\u2083=\u22127', GREEN, 2.5),
]

for x, beta_text, color, y in domains_beta:
    ax.text(x, y, beta_text, fontsize=7, color=color, ha='center',
            fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color,
                      alpha=0.8))

# Gap ratio result
ax.text(14.5, 7.0, 'Gap ratio = 218/115 = 1.896\n'
        '(invariant under fermion addition!)\n'
        'Measured: 1.358 \u2192 40% miss',
        fontsize=9, color=GOLD, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Domain count
ax.text(8.5, -1.5, '10 domains \u2022 9 thresholds \u2022 1 confinement wall \u2022 1 EW transition',
        fontsize=10, color=SILVER, ha='center')

save_fig(fig, 'phys14_01_domain_map.png')


# ================================================================
# FIG 2: GAP RATIO INVARIANT UNDER FERMION ADDITION
# Type: Running/convergence (flat line)
# Shows: Gap ratio = 218/115 at 0, 1, 2, 3 generations. Flat.
# The invariance IS the finding.
# ================================================================

fig, ax = dark_fig("Gap Ratio vs Number of Fermion Generations: Invariant",
                   xlabel="Number of complete fermion generations",
                   ylabel="Gap ratio (b\u2081\u2212b\u2082)/(b\u2082\u2212b\u2083)",
                   size=(16, 10))

n_gen = [0, 1, 2, 3, 4, 5]
gap_vals = [218.0 / 115] * len(n_gen)

# The flat line
curve(ax, n_gen, gap_vals, 'Gap ratio = 218/115 (constant)', GOLD, 3)

# Data points
for n in n_gen:
    data_point(ax, n, 218.0 / 115, '', GOLD, size=300)
    if n <= 3:
        ax.text(n, 1.93, 'n = %d' % n, fontsize=10, color=SILVER,
                ha='center')

# Highlight the actual SM (n=3)
ax.scatter([3], [218.0 / 115], s=500, facecolors='none', edgecolors=WHITE,
           linewidth=2.5, zorder=11)
ax.text(3, 1.85, 'SM (3 gen)', fontsize=10, color=WHITE, ha='center',
        fontweight='bold')

# Measured value
ax.plot([-0.5, 5.5], [1.358, 1.358], color=RED, linewidth=2,
        linestyle='--', alpha=0.7)
ax.text(4.5, 1.37, 'Measured: 1.358', fontsize=10, color=RED,
        fontweight='bold')

# The explanation
result_box(ax, 2.5, 1.15,
           'Each generation contributes \u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3.\n'
           'Differences b\u2081\u2212b\u2082 and b\u2082\u2212b\u2083 are unchanged.\n'
           'The gap ratio is determined by gauge + Higgs ONLY.\n'
           'Fermions cancel out completely.',
           GOLD, 10)

ax.set_xlim(-0.5, 5.5)
ax.set_ylim(1.0, 2.1)
ax.set_xticks([0, 1, 2, 3, 4, 5])

save_fig(fig, 'phys14_02_gap_ratio_invariant.png')


# ================================================================
# FIG 3: GAP RATIO SOURCES — GAUGE + HIGGS, FERMIONS = 0
# Type: Waterfall/decomposition
# Shows: Numerator b1-b2 decomposed: gauge (+22/3), Higgs (-1/15),
# fermions (0). Denominator b2-b3 decomposed similarly.
# ================================================================

fig = plt.figure(figsize=(18, 10), facecolor=BG)

# Left: numerator b1 - b2
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_facecolor(BG)

sources_num = [
    ('Gauge\n0 \u2212 (\u221222/3)', 22.0 / 3, CYAN, '+7.333'),
    ('Higgs\n1/10 \u2212 1/6', -1.0 / 15, ORANGE, '\u22120.067'),
    ('Fermions\n4/3 \u2212 4/3', 0, DIM, '0.000'),
]

running = 0
for i, (label, value, color, val_text) in enumerate(sources_num):
    ax1.bar(i, value, bottom=running, color=color, alpha=0.6,
            edgecolor=color, linewidth=2, width=0.6)
    if abs(value) > 0.5:
        ax1.text(i, running + value / 2, val_text, fontsize=10, color=WHITE,
                 ha='center', va='center', fontweight='bold')
    elif value == 0:
        ax1.text(i, running + 0.3, 'ZERO', fontsize=12, color=RED,
                 ha='center', fontweight='bold')
    else:
        ax1.text(i, running + value - 0.3, val_text, fontsize=8,
                 color=color, ha='center')
    running += value

# Total
ax1.plot([-0.5, 2.5], [running, running], color=GOLD, linewidth=2,
         linestyle='--')
ax1.text(2.3, running + 0.2, '= 109/15\n= 7.267', fontsize=10,
         color=GOLD, fontweight='bold')

ax1.set_title('NUMERATOR: b\u2081 \u2212 b\u2082', fontsize=13, color=WHITE,
              fontweight='bold', pad=15)
ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['Gauge', 'Higgs', 'Fermions'], fontsize=9, color=SILVER)
ax1.set_ylabel('Contribution', fontsize=11, color=SILVER)
ax1.set_ylim(-1, 9)
ax1.tick_params(colors=DIM)
for spine in ax1.spines.values():
    spine.set_color(PAN)

# Right: denominator b2 - b3
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_facecolor(BG)

sources_den = [
    ('Gauge\n\u221222/3 \u2212 (\u221211)', 11.0 / 3, CYAN, '+3.667'),
    ('Higgs\n1/6 \u2212 0', 1.0 / 6, ORANGE, '+0.167'),
    ('Fermions\n4/3 \u2212 4/3', 0, DIM, '0.000'),
]

running = 0
for i, (label, value, color, val_text) in enumerate(sources_den):
    ax2.bar(i, value, bottom=running, color=color, alpha=0.6,
            edgecolor=color, linewidth=2, width=0.6)
    if abs(value) > 0.5:
        ax2.text(i, running + value / 2, val_text, fontsize=10, color=WHITE,
                 ha='center', va='center', fontweight='bold')
    elif value == 0:
        ax2.text(i, running + 0.3, 'ZERO', fontsize=12, color=RED,
                 ha='center', fontweight='bold')
    else:
        ax2.text(i, running + value + 0.1, val_text, fontsize=8,
                 color=color, ha='center')
    running += value

ax2.plot([-0.5, 2.5], [running, running], color=GOLD, linewidth=2,
         linestyle='--')
ax2.text(2.3, running + 0.2, '= 23/6\n= 3.833', fontsize=10,
         color=GOLD, fontweight='bold')

ax2.set_title('DENOMINATOR: b\u2082 \u2212 b\u2083', fontsize=13, color=WHITE,
              fontweight='bold', pad=15)
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Gauge', 'Higgs', 'Fermions'], fontsize=9, color=SILVER)
ax2.set_ylim(-1, 9)
ax2.tick_params(colors=DIM)
for spine in ax2.spines.values():
    spine.set_color(PAN)

fig.suptitle('Gap Ratio = (109/15) / (23/6) = 218/115: Fermions Contribute Nothing',
             fontsize=14, color=GOLD, fontweight='bold', y=0.98)
fig.tight_layout(rect=[0, 0.02, 1, 0.94])

path = os.path.join(get_outdir(), 'phys14_03_gap_ratio_sources.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys14_03_gap_ratio_sources.png")


# ================================================================
# FIG 4: GAUGE SELF-COUPLING ASYMMETRY
# Type: Comparison bar
# Shows: The maximally asymmetric gauge contributions.
# U(1) = 0 (abelian), SU(2) = -22/3, SU(3) = -11.
# THIS asymmetry IS the gap ratio problem.
# ================================================================

fig, ax = dark_fig("Gauge Self-Coupling: The Maximally Asymmetric Source",
                   xlabel="",
                   ylabel="Gauge self-coupling contribution to b_i",
                   size=(16, 10))

groups = [
    ('U(1)_Y\n(abelian)', 0, CYAN, 'No self-coupling.\nU(1) is abelian.\nb\u2081^gauge = 0'),
    ('SU(2)_L', -22.0 / 3, GREEN, '\u221211 \u00d7 C\u2082(SU(2))/3\n= \u221211 \u00d7 2/3\n= \u221222/3'),
    ('SU(3)_c', -11.0, RED, '\u221211 \u00d7 C\u2082(SU(3))/3\n= \u221211 \u00d7 3/3\n= \u221211'),
]

for i, (label, value, color, formula) in enumerate(groups):
    ax.bar(i, value, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    if value == 0:
        ax.text(i, 0.5, '0', fontsize=18, color=GOLD, ha='center',
                fontweight='bold')
    else:
        ax.text(i, value - 0.5, '%.2f' % value, fontsize=14, color=color,
                ha='center', fontweight='bold')
    ax.text(i, 2.0, formula, fontsize=8, color=SILVER, ha='center')

ax.set_xticks([0, 1, 2])
ax.set_xticklabels([g[0] for g in groups], fontsize=11, color=SILVER)

# The asymmetry annotation
ax.annotate('THIS ASYMMETRY\ndetermines the\ngap ratio 218/115',
            xy=(0, 0), xytext=(1.5, -8),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# The 11
result_box(ax, 0, -11,
           'The integer 11 is universal:\n'
           '\u221211C\u2082(G)/3 for every non-abelian group.\n'
           'It comes from the Yang-Mills Lagrangian.\n'
           'U(1) gets ZERO because it is abelian.',
           SILVER, 9)

ax.set_xlim(-0.8, 3.0)
ax.set_ylim(-13, 4)

save_fig(fig, 'phys14_04_gauge_asymmetry.png')


# ================================================================
# FIG 5: SM VS MSSM VS VL DOUBLET — NUMERATOR AND DENOMINATOR
# Type: Dual comparison
# Shows: Numerator b1-b2 and denominator b2-b3 for three models.
# What changes and what doesn't between models.
# ================================================================

fig, ax = dark_fig("Three Models: Numerator and Denominator of the Gap Ratio",
                   xlabel="",
                   ylabel="Value",
                   size=(16, 10))

models = [
    ('SM', 109.0 / 15, 23.0 / 6, RED, '218/115\n= 1.896'),
    ('SM + VL\ndoublet', 19.0 / 3, 9.0 / 2, CYAN, '38/27\n= 1.407'),
    ('MSSM', 28.0 / 5, 4.0, GREEN, '7/5\n= 1.400'),
]

bar_width = 0.3
x_base = np.arange(len(models))

for i, (label, num, den, color, ratio) in enumerate(models):
    # Numerator bar
    ax.bar(i - bar_width / 2 - 0.02, num, color=color, alpha=0.6,
           edgecolor=color, linewidth=2, width=bar_width)
    ax.text(i - bar_width / 2, num + 0.2, '%.2f' % num, fontsize=10,
            color=color, ha='center', fontweight='bold')

    # Denominator bar
    ax.bar(i + bar_width / 2 + 0.02, den, color=color, alpha=0.3,
           edgecolor=color, linewidth=2, width=bar_width, hatch='//')
    ax.text(i + bar_width / 2, den + 0.2, '%.2f' % den, fontsize=10,
            color=color, ha='center')

    # Ratio
    ax.text(i, -1.0, ratio, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))

ax.set_xticks(x_base)
ax.set_xticklabels([m[0] for m in models], fontsize=10, color=SILVER)

# Legend
ax.bar(-0.5, 0, color=SILVER, alpha=0.6, width=0.01, label='b\u2081\u2212b\u2082 (numerator)')
ax.bar(-0.5, 0, color=SILVER, alpha=0.3, width=0.01, hatch='//',
       label='b\u2082\u2212b\u2083 (denominator)')
legend(ax, loc='upper right')

# What changes
ax.annotate('VL doublet shrinks\nnumerator (large \u0394b\u2082)',
            xy=(1, 19.0 / 3), xytext=(1.8, 7.5),
            fontsize=9, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

# Measured reference
ax.plot([-0.5, 2.5], [1.358, 1.358], color=GOLD, linewidth=1.5,
        linestyle=':', alpha=0.5)
ax.text(2.3, 1.5, 'Measured\nratio', fontsize=7, color=GOLD)

ax.set_xlim(-0.8, 3.0)
ax.set_ylim(-2.0, 9.0)

save_fig(fig, 'phys14_05_three_models_decomposed.png')


# ================================================================
# FIG 6: ENERGY AXIS — ALL THRESHOLDS ON LOG SCALE
# Type: Scale/landscape
# Shows: Every mass threshold from m_e to M_GUT on log10 scale.
# Confinement wall, EW transition, full SM onset marked.
# ================================================================

fig, ax = dark_fig("The Energy Axis: Every Threshold from m_e to M_GUT",
                   xlabel="log\u2081\u2080(E / GeV)",
                   ylabel="",
                   size=(16, 8))

# Log10 positions
particles = [
    (np.log10(0.000511), 'm_e', CYAN, 0.8),
    (np.log10(0.10566), 'm_\u03bc', BLUE, -0.8),
    (np.log10(0.3), '\u039b_QCD', RED, 0.8),
    (np.log10(2.0), '~2 GeV', RED, -0.8),
    (np.log10(1.273), 'm_c', GREEN, 0.8),
    (np.log10(1.777), 'm_\u03c4', ORANGE, -0.8),
    (np.log10(4.183), 'm_b', GREEN, 0.8),
    (np.log10(80.37), 'M_W', GOLD, -1.2),
    (np.log10(91.19), 'M_Z', DIM, 0.8),
    (np.log10(125.2), 'm_H', BLUE, -0.8),
    (np.log10(172.57), 'm_t', ORANGE, 0.8),
    (13.80, 'M_GUT\n(SM)', RED, -0.8),
    (15.50, 'M_GUT\n(+VL)', CYAN, 0.8),
    (17.32, 'M_GUT\n(MSSM)', GREEN, -0.8),
]

# Main axis line
ax.plot([-4, 18], [0, 0], color=DIM, linewidth=2, alpha=0.4)

for log_e, label, color, y_off in particles:
    ax.plot([log_e, log_e], [-0.2, 0.2], color=color, linewidth=2)
    data_point(ax, log_e, 0, '', color, size=80)
    ax.text(log_e, y_off, label, fontsize=7, color=color, ha='center',
            fontweight='bold')

# Confinement wall (shaded)
ax.fill_between([np.log10(0.3), np.log10(2.0)], [-0.4, -0.4], [0.4, 0.4],
                alpha=0.1, color=RED)

# EW transition (highlighted)
ax.plot([np.log10(80.37), np.log10(80.37)], [-1.5, 1.5], color=GOLD,
        linewidth=2.5, alpha=0.3)

# Regime labels
ax.text(-2, -1.8, 'QED + QCD\n(2 couplings)', fontsize=9, color=CYAN,
        ha='center')
ax.text(8, -1.8, '3 couplings\n(gap ratio applies)', fontsize=9,
        color=GREEN, ha='center')

# Scale markers
for log_val in [-3, -2, -1, 0, 1, 2, 3, 5, 10, 15]:
    ax.plot([log_val, log_val], [-0.1, 0.1], color=DIM, linewidth=0.5, alpha=0.3)

ax.set_xlim(-4, 18)
ax.set_ylim(-2.2, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys14_06_energy_axis.png')


# ================================================================
# FIG 7: BOSON PROBLEM, NOT FERMION PROBLEM
# Type: Dual-panel comparison
# Shows: Left — fermions (cancel, zero effect on gap ratio).
# Right — bosons + Higgs (determine gap ratio entirely).
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "FERMIONS: Cancel from Gap Ratio",
    "BOSONS + HIGGS: Determine Gap Ratio",
    size=(18, 9), wspace=0.35)

# Left: fermions — three equal bars, all 4/3
for i, label in enumerate(['\u0394b\u2081', '\u0394b\u2082', '\u0394b\u2083']):
    ax1.bar(i, 4.0 / 3, color=[CYAN, GREEN, RED][i], alpha=0.6,
            edgecolor=[CYAN, GREEN, RED][i], linewidth=2, width=0.6)
    ax1.text(i, 4.0 / 3 + 0.1, '4/3', fontsize=14,
             color=[CYAN, GREEN, RED][i], ha='center', fontweight='bold')

ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['\u0394b\u2081 (U(1))', '\u0394b\u2082 (SU(2))', '\u0394b\u2083 (SU(3))'],
                     fontsize=9, color=SILVER)
ax1.set_ylabel('Per-generation contribution', fontsize=10, color=SILVER)

# The cancellation
ax1.text(1, 2.2, 'ALL EQUAL \u2192 CANCEL', fontsize=14, color=RED,
         ha='center', fontweight='bold')
ax1.text(1, 1.9, '\u0394(b\u2081\u2212b\u2082) = 0\n\u0394(b\u2082\u2212b\u2083) = 0',
         fontsize=11, color=GOLD, ha='center', fontweight='bold')
ax1.text(1, -0.5, 'From SU(5) anomaly cancellation:\n5\u0305 + 10 has equal Dynkin index\nfor all three gauge factors',
         fontsize=8, color=SILVER, ha='center')

ax1.set_xlim(-0.8, 3.0)
ax1.set_ylim(-1.0, 2.8)

# Right: bosons — asymmetric bars
gauge_vals = [0, -22.0 / 3, -11]
higgs_vals = [1.0 / 10, 1.0 / 6, 0]

for i in range(3):
    # Gauge bar
    ax2.bar(i - 0.17, gauge_vals[i], color=[CYAN, GREEN, RED][i], alpha=0.6,
            edgecolor=[CYAN, GREEN, RED][i], linewidth=2, width=0.3)
    # Higgs bar (stacked on top or separate)
    ax2.bar(i + 0.17, higgs_vals[i], color=ORANGE, alpha=0.4,
            edgecolor=ORANGE, linewidth=1.5, width=0.3)

ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['b\u2081 (U(1))', 'b\u2082 (SU(2))', 'b\u2083 (SU(3))'],
                     fontsize=9, color=SILVER)

# Labels
ax2.text(0, 1.0, '0', fontsize=14, color=GOLD, ha='center', fontweight='bold')
ax2.text(1, -22.0 / 3 - 0.5, '\u221222/3', fontsize=10, color=GREEN,
         ha='center', fontweight='bold')
ax2.text(2, -11 - 0.5, '\u221211', fontsize=10, color=RED,
         ha='center', fontweight='bold')

ax2.text(1, 2.2, 'ASYMMETRIC \u2192 DETERMINE', fontsize=14, color=GREEN,
         ha='center', fontweight='bold')
ax2.text(1, 1.7, 'Gap ratio = 218/115\nfrom this asymmetry alone',
         fontsize=10, color=GOLD, ha='center', fontweight='bold')

ax2.set_xlim(-0.8, 3.0)
ax2.set_ylim(-13, 3.5)

save_fig(fig, 'phys14_07_boson_problem.png')


# ================================================================
# FIG 8: PHYS-14 IDENTITY CARD
# Type: Identity card
# Shows: Complete map, fermion cancellation, boson problem.
# ================================================================

fig, ax = dark_canvas("PHYS-14 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE UNIFIED TRANSFORMATION MAP', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')

# Left: the map
ax.text(2.5, 8.0, 'THE MAP', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

map_items = [
    ('10 domains', 'm_e to M_GUT', CYAN),
    ('9 thresholds', 'Each changes beta coefficients', GREEN),
    ('1 confinement wall', 'No perturbative map (~0.3\u20132 GeV)', RED),
    ('1 EW transition', '2 couplings \u2192 3 couplings at M_W', GOLD),
]
for i, (item, detail, color) in enumerate(map_items):
    y = 7.2 - i * 0.7
    ax.text(1.0, y, item, fontsize=10, color=color, fontweight='bold')
    ax.text(1.0, y - 0.3, detail, fontsize=8, color=DIM)

# Right: the finding
ax.text(7.5, 8.0, 'THE FINDING', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

finding_items = [
    ('Fermions CANCEL', '\u0394b\u2081 = \u0394b\u2082 = \u0394b\u2083 = 4/3 per gen', GREEN),
    ('Gap ratio INVARIANT', '218/115 at 0, 1, 2, or 3 generations', GOLD),
    ('BOSON problem', 'Gauge asymmetry (0, \u221222/3, \u221211)', RED),
    ('NOT fermion problem', 'Adding quarks/leptons changes nothing', CYAN),
]
for i, (item, detail, color) in enumerate(finding_items):
    y = 7.2 - i * 0.7
    ax.text(6.0, y, item, fontsize=10, color=color, fontweight='bold')
    ax.text(6.0, y - 0.3, detail, fontsize=8, color=DIM)

# The fix
ax.plot([0.5, 9.5], [3.8, 3.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 3.3, 'TO FIX: Add particles with \u0394b\u2082 > \u0394b\u2081', fontsize=12,
        color=WHITE, ha='center', fontweight='bold')

fix_items = [
    ('MSSM:', '7/5 = 1.400', '~30 particles', GREEN),
    ('VL doublet:', '38/27 = 1.407', '1 particle', CYAN),
    ('Measured:', '1.358', '', GOLD),
]
for i, (model, gap, count, color) in enumerate(fix_items):
    y = 2.5 - i * 0.6
    ax.text(3.0, y, model, fontsize=10, color=SILVER)
    ax.text(5.0, y, gap, fontsize=12, color=color, fontweight='bold',
            fontfamily='monospace')
    ax.text(7.0, y, count, fontsize=9, color=DIM)

# Bottom
ax.text(5, 0.5, 'The SM\'s unification failure is a boson problem, not a fermion problem.\n'
        'The gap ratio 218/115 is set by gauge self-coupling asymmetry (0 vs \u221222/3 vs \u221211)\n'
        'and the Higgs (1/10 vs 1/6 vs 0). Adding or removing fermion generations changes nothing.',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys14_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-14 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys14_01_domain_map.png',
    'phys14_02_gap_ratio_invariant.png',
    'phys14_03_gap_ratio_sources.png',
    'phys14_04_gauge_asymmetry.png',
    'phys14_05_three_models_decomposed.png',
    'phys14_06_energy_axis.png',
    'phys14_07_boson_problem.png',
    'phys14_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    