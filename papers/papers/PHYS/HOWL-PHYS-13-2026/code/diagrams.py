#!/usr/bin/env python3
"""
HOWL PHYS-13 Diagrams — Gauge Coupling Unification and Minimal BSM Content
8 figures covering SM vs MSSM running, proton decay, gap ratio, BSM enumeration,
three-line convergence, VL doublet vs MSSM, M_GUT comparison.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: SM VS MSSM RUNNING — DUAL PANEL
# Type: Dual-panel
# Shows: Left: SM three couplings don't meet (gap = 6.58).
# Right: MSSM three couplings nearly meet (gap = 0.69).
# The contrast IS unification vs failure.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Standard Model: Couplings Do Not Unify",
    "MSSM: Near-Unification",
    size=(18, 9), wspace=0.35)

# Common: log10(mu/GeV) from ~2 to ~17
log_mu = np.linspace(np.log10(91.19), 17.5, 300)
ln_ratio = np.log(10) * (log_mu - np.log10(91.19))  # ln(mu/M_Z)

# Initial values at M_Z
inv_a1 = 63.2103
inv_a2 = 31.6855
inv_a3 = 8.4746

# --- LEFT: SM ---
b1_sm, b2_sm, b3_sm = 41.0 / 10, -19.0 / 6, -7.0

a1_sm = inv_a1 - b1_sm / (2 * np.pi) * ln_ratio
a2_sm = inv_a2 - b2_sm / (2 * np.pi) * ln_ratio
a3_sm = inv_a3 - b3_sm / (2 * np.pi) * ln_ratio

curve(ax1, log_mu, a1_sm, '1/\u03b1\u2081 (U(1))', CYAN, 2.5)
curve(ax1, log_mu, a2_sm, '1/\u03b1\u2082 (SU(2))', GREEN, 2.5)
curve(ax1, log_mu, a3_sm, '1/\u03b1\u2083 (SU(3))', RED, 2.5)

# Mark the crossing and gap
log_gut_sm = 13.80
ax1.plot([log_gut_sm, log_gut_sm], [30, 50], color=GOLD, linewidth=2,
         linestyle='--', alpha=0.5)
ax1.text(log_gut_sm + 0.3, 42, '\u0394 = 6.58\n(40% miss)', fontsize=11,
         color=RED, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

ax1.set_xlabel('log\u2081\u2080(\u03bc / GeV)', color=SILVER, fontsize=11)
ax1.set_ylabel('1/\u03b1_i', color=SILVER, fontsize=11)
ax1.set_xlim(1.5, 17.5)
ax1.set_ylim(0, 70)
legend(ax1, loc='upper right')

# --- RIGHT: MSSM ---
b1_mssm, b2_mssm, b3_mssm = 33.0 / 5, 1.0, -3.0

a1_mssm = inv_a1 - b1_mssm / (2 * np.pi) * ln_ratio
a2_mssm = inv_a2 - b2_mssm / (2 * np.pi) * ln_ratio
a3_mssm = inv_a3 - b3_mssm / (2 * np.pi) * ln_ratio

curve(ax2, log_mu, a1_mssm, '1/\u03b1\u2081', CYAN, 2.5)
curve(ax2, log_mu, a2_mssm, '1/\u03b1\u2082', GREEN, 2.5)
curve(ax2, log_mu, a3_mssm, '1/\u03b1\u2083', RED, 2.5)

log_gut_mssm = 17.32
ax2.plot([log_gut_mssm, log_gut_mssm], [20, 30], color=GOLD, linewidth=2,
         linestyle='--', alpha=0.5)
ax2.text(log_gut_mssm - 2, 28, '\u0394 = 0.69\n(2.7% miss)', fontsize=11,
         color=GREEN, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

# Near-convergence circle
data_point(ax2, log_gut_mssm, 26, '', GOLD, size=350)
ax2.scatter([log_gut_mssm], [26], s=450, facecolors='none', edgecolors=GOLD,
            linewidth=2.5, zorder=11)

ax2.set_xlabel('log\u2081\u2080(\u03bc / GeV)', color=SILVER, fontsize=11)
ax2.set_ylabel('1/\u03b1_i', color=SILVER, fontsize=11)
ax2.set_xlim(1.5, 17.5)
ax2.set_ylim(0, 70)
legend(ax2, loc='upper right')

save_fig(fig, 'phys13_01_sm_vs_mssm_running.png')


# ================================================================
# FIG 2: PROTON DECAY — M_GUT VS EXPERIMENTAL SENSITIVITY
# Type: Scale/threshold
# Shows: M_GUT values for SM, VL doublet, MSSM on a log scale,
# with Super-K current limit and Hyper-K projected reach marked.
# The VL doublet sits right at the testable boundary.
# ================================================================

fig, ax = dark_fig("Proton Decay: Is the VL Quark Doublet Testable?",
                   xlabel="log\u2081\u2080(M_GUT / GeV)",
                   ylabel="",
                   size=(16, 10))

# The scale
log_scale = np.linspace(13, 18, 100)
ax.plot(log_scale, [0.5] * len(log_scale), color=DIM, linewidth=2, alpha=0.3)

# Model positions
models = [
    (13.80, 'SM\n10^{13.8}', RED, -0.5, 'Does not unify'),
    (15.50, 'VL doublet\n10^{15.5}', CYAN, 0.8, 'On the boundary!'),
    (17.32, 'MSSM\n10^{17.3}', GREEN, -0.5, 'Safe from proton decay'),
]

for log_val, label, color, y_offset, note_text in models:
    ax.plot([log_val, log_val], [0.1, 0.9], color=color, linewidth=3)
    data_point(ax, log_val, 0.5, '', color, size=350)
    ax.text(log_val, 0.5 + y_offset, label, fontsize=11, color=color,
            ha='center', fontweight='bold')
    ax.text(log_val, 0.5 + y_offset - 0.25, note_text, fontsize=8,
            color=SILVER, ha='center')

# Super-K current limit
sk_limit = 15.5
ax.fill_between([13, sk_limit], [1.5, 1.5], [2.0, 2.0],
                alpha=0.15, color=RED)
ax.plot([sk_limit, sk_limit], [1.5, 2.0], color=RED, linewidth=2.5)
ax.text((13 + sk_limit) / 2, 1.75, 'EXCLUDED\n(Super-K)', fontsize=11,
        color=RED, ha='center', fontweight='bold')
ax.text(sk_limit + 0.1, 1.75, 'Current limit\n\u03c4_p > 2.4\u00d710\u00b3\u2074 yr',
        fontsize=8, color=RED)

# Hyper-K projected reach
hk_reach = 16.0
ax.fill_between([sk_limit, hk_reach], [-0.5, -0.5], [-1.0, -1.0],
                alpha=0.15, color=GOLD)
ax.plot([hk_reach, hk_reach], [-1.0, -0.5], color=GOLD, linewidth=2.5,
        linestyle='--')
ax.text((sk_limit + hk_reach) / 2, -0.75, 'Hyper-K reach\n(~2027+)',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

# Arrow from VL doublet to Hyper-K zone
ax.annotate('TESTABLE by\nHyper-Kamiokande', xy=(15.5, -0.3),
            xytext=(14.5, -1.5),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_xlim(13, 18)
ax.set_ylim(-2.0, 2.5)
ax.set_yticks([])

save_fig(fig, 'phys13_02_proton_decay.png')


# ================================================================
# FIG 3: GAP RATIO — FOUR VALUES ON A NUMBER LINE
# Type: Scale/comparison
# Shows: SM (218/115 = 1.896), MSSM (7/5 = 1.400), VL doublet
# (38/27 = 1.407), measured (1.358). The clustering near measurement.
# ================================================================

fig, ax = dark_fig("The Gap Ratio: One Rational vs One Measurement",
                   xlabel="Gap ratio = (b\u2081\u2212b\u2082)/(b\u2082\u2212b\u2083)",
                   ylabel="",
                   size=(16, 8))

# Number line
ax.plot([1.2, 2.1], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Measured value (gold band)
measured = 1.358
ax.plot([measured, measured], [0.0, 1.0], color=GOLD, linewidth=3)
data_point(ax, measured, 0.5, '', GOLD, size=400)
ax.text(measured, 1.3, 'Measured\n1.358', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')

# SM
sm_gap = 218.0 / 115
ax.plot([sm_gap, sm_gap], [0.2, 0.8], color=RED, linewidth=3)
data_point(ax, sm_gap, 0.5, '', RED, size=300)
ax.text(sm_gap, -0.3, 'SM\n218/115\n= 1.896', fontsize=11, color=RED,
        ha='center', fontweight='bold')

# MSSM
mssm_gap = 7.0 / 5
ax.plot([mssm_gap, mssm_gap], [0.2, 0.8], color=GREEN, linewidth=3)
data_point(ax, mssm_gap, 0.5, '', GREEN, size=300)
ax.text(mssm_gap, 1.3, 'MSSM\n7/5\n= 1.400', fontsize=11, color=GREEN,
        ha='center', fontweight='bold')

# VL doublet
vl_gap = 38.0 / 27
ax.plot([vl_gap, vl_gap], [0.2, 0.8], color=CYAN, linewidth=3)
data_point(ax, vl_gap, 0.5, '', CYAN, size=300)
ax.text(vl_gap, -0.3, 'VL doublet\n38/27\n= 1.407', fontsize=11, color=CYAN,
        ha='center', fontweight='bold')

# Distance arrows
ax.annotate('', xy=(measured, -0.8), xytext=(sm_gap, -0.8),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text((measured + sm_gap) / 2, -1.1, '40% miss', fontsize=10,
        color=RED, ha='center', fontweight='bold')

ax.annotate('', xy=(measured, -1.5), xytext=(mssm_gap, -1.5),
            arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2))
ax.text((measured + mssm_gap) / 2, -1.8, '3.1%', fontsize=10,
        color=GREEN, ha='center', fontweight='bold')

ax.set_xlim(1.15, 2.1)
ax.set_ylim(-2.3, 2.0)
ax.set_yticks([])

save_fig(fig, 'phys13_03_gap_ratio.png')


# ================================================================
# FIG 4: BSM ENUMERATION — 15 CANDIDATES SORTED BY DISTANCE
# Type: Comparison bar
# Shows: Distance from measured gap ratio for each candidate.
# MSSM and VL doublet dramatically closer than the rest.
# ================================================================

fig, ax = dark_fig("BSM Enumeration: Distance from Measured Gap Ratio",
                   xlabel="",
                   ylabel="Distance from measured gap ratio (1.358)",
                   size=(16, 10))

candidates = [
    ('MSSM', 0.042, GREEN),
    ('VL (3,2,\u215b)', 0.049, CYAN),
    ('5+5\u0305', 0.123, BLUE),
    ('3\u00d7 H', 0.273, DIM),
    ('Sc (3,2)', 0.274, DIM),
    ('Sc (1,3)', 0.306, DIM),
    ('VL (1,2)', 0.354, DIM),
    ('2\u00d7 H', 0.354, DIM),
    ('Sc (1,2)', 0.442, DIM),
    ('VL e\u1d63', 0.642, DIM),
    ('Sc (3,1)', 0.642, DIM),
    ('VL d\u1d63', 0.756, DIM),
    ('Sc (8,1)', 0.822, DIM),
    ('VL u\u1d63', 0.870, DIM),
    ('10+10\u0305', 0.590, DIM),
]

# Sort by distance
candidates.sort(key=lambda x: x[1])
x_pos = np.arange(len(candidates))

for i, (name, dist, color) in enumerate(candidates):
    ax.bar(i, dist, color=color, alpha=0.6, edgecolor=color,
           linewidth=1.5, width=0.7)
    if dist < 0.15:
        ax.text(i, dist + 0.02, '%.3f' % dist, fontsize=9, color=color,
                ha='center', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels([c[0] for c in candidates], fontsize=7, color=SILVER,
                    rotation=45, ha='right')

# The gap between top 2 and rest
ax.plot([-0.5, 14.5], [0.1, 0.1], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.5)
ax.text(10, 0.08, 'Separation', fontsize=9, color=GOLD)

# Annotation for the top two
ax.annotate('Only 2 candidates\nwithin 0.05 of measured', xy=(1, 0.05),
            xytext=(5, 0.35),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_xlim(-0.8, 14.8)
ax.set_ylim(0, 1.0)

save_fig(fig, 'phys13_04_bsm_enumeration.png')


# ================================================================
# FIG 5: THREE-LINE CONVERGENCE — GEOMETRIC INTERPRETATION
# Type: Geometric
# Shows: Three lines (1/alpha_i vs log mu) — if they meet at one
# point, unification. The gap ratio tests slope compatibility.
# ================================================================

fig, ax = dark_canvas("The Gap Ratio Test: Do Three Lines Meet?",
                      size=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Left panel: lines that DON'T meet (SM)
ax.text(2.5, 9.3, 'SM: Lines DON\'T Meet', fontsize=14, color=RED,
        ha='center', fontweight='bold')

# Three lines from left side diverging
x_start = 0.5
x_end_1 = 4.5
# Line 1 (1/alpha_1): starts high, slopes down
ax.plot([x_start, x_end_1], [7.5, 5.5], color=CYAN, linewidth=2.5)
# Line 2 (1/alpha_2): starts mid, slopes up slightly
ax.plot([x_start, x_end_1], [4.5, 5.5], color=GREEN, linewidth=2.5)
# Line 3 (1/alpha_3): starts low, slopes up more
ax.plot([x_start, x_end_1], [2.0, 4.2], color=RED, linewidth=2.5)

# Gap at crossing
ax.annotate('', xy=(4.3, 4.2), xytext=(4.3, 5.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(4.8, 4.85, '\u0394 = 6.58', fontsize=10, color=GOLD, fontweight='bold')

# Right panel: lines that DO meet (MSSM)
ax.text(7.5, 9.3, 'MSSM: Lines Nearly Meet', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')

x_start_r = 5.5
x_end_r = 9.5
# Three lines converging to a point
x_meet = 9.0
y_meet = 4.5

ax.plot([x_start_r, x_end_r], [7.5, y_meet + 0.15], color=CYAN, linewidth=2.5)
ax.plot([x_start_r, x_end_r], [4.5, y_meet], color=GREEN, linewidth=2.5)
ax.plot([x_start_r, x_end_r], [2.0, y_meet - 0.15], color=RED, linewidth=2.5)

# Near-convergence
data_point(ax, x_meet, y_meet, '', GOLD, size=350)
ax.scatter([x_meet], [y_meet], s=450, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)
ax.text(x_meet, y_meet + 0.5, '\u0394 = 0.69', fontsize=10, color=GREEN,
        ha='center', fontweight='bold')

# Labels
ax.text(0.3, 7.8, '1/\u03b1\u2081', fontsize=10, color=CYAN, fontweight='bold')
ax.text(0.3, 4.8, '1/\u03b1\u2082', fontsize=10, color=GREEN, fontweight='bold')
ax.text(0.3, 2.3, '1/\u03b1\u2083', fontsize=10, color=RED, fontweight='bold')

# The gap ratio explanation
ax.text(5.0, 1.5, 'Gap ratio = slope ratio = (b\u2081\u2212b\u2082)/(b\u2082\u2212b\u2083)',
        fontsize=11, color=SILVER, ha='center')
ax.text(5.0, 0.8, 'If slope ratio = intercept ratio \u2192 three lines meet at one point.\n'
        'SM: 218/115 \u2260 1.358. MSSM: 7/5 \u2248 1.358.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

# Axis labels (schematic)
ax.text(2.5, 0.2, 'log \u03bc \u2192', fontsize=10, color=DIM, ha='center')
ax.text(7.5, 0.2, 'log \u03bc \u2192', fontsize=10, color=DIM, ha='center')

save_fig(fig, 'phys13_05_three_line_convergence.png')


# ================================================================
# FIG 6: VL DOUBLET VS MSSM — 1 PARTICLE VS ~30
# Type: Comparison/scale
# Shows: The VL quark doublet achieves comparable unification with
# one new multiplet instead of the MSSM's dozens.
# ================================================================

fig, ax = dark_canvas("Minimal vs Maximal: 1 Particle vs ~30",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Left: VL quark doublet
ax.text(2.5, 8.5, 'VL Quark Doublet', fontsize=16, color=CYAN,
        ha='center', fontweight='bold')
ax.text(2.5, 7.5, '1 new multiplet', fontsize=20, color=CYAN,
        ha='center', fontweight='bold')

# Single particle icon
data_point(ax, 2.5, 5.5, '', CYAN, size=800)
ax.text(2.5, 5.5, '(3,2,\u215b)', fontsize=12, color=BG,
        ha='center', fontweight='bold')

vl_props = [
    ('Gap ratio:', '38/27 = 1.407', CYAN),
    ('Distance:', '0.049', CYAN),
    ('M_GUT:', '10^{15.5} GeV', CYAN),
    ('Proton decay:', 'Testable', GOLD),
    ('Dark matter:', 'No', RED),
]
for i, (prop, val, color) in enumerate(vl_props):
    y = 3.8 - i * 0.55
    ax.text(1.5, y, prop, fontsize=9, color=SILVER)
    ax.text(3.5, y, val, fontsize=10, color=color, fontweight='bold')

# Divider
ax.plot([5, 5], [1, 9], color=DIM, linewidth=2, linestyle=':', alpha=0.4)
ax.text(5, 9.2, 'vs', fontsize=14, color=DIM, ha='center', fontweight='bold')

# Right: MSSM
ax.text(7.5, 8.5, 'MSSM', fontsize=16, color=GREEN,
        ha='center', fontweight='bold')
ax.text(7.5, 7.5, '~30 new particles', fontsize=20, color=GREEN,
        ha='center', fontweight='bold')

# Many particle icons
np.random.seed(42)
for j in range(30):
    px = 6.0 + 3.0 * np.random.random()
    py = 4.5 + 2.5 * np.random.random()
    data_point(ax, px, py, '', GREEN, size=60)

mssm_props = [
    ('Gap ratio:', '7/5 = 1.400', GREEN),
    ('Distance:', '0.042', GREEN),
    ('M_GUT:', '10^{17.3} GeV', GREEN),
    ('Proton decay:', 'Safe', GREEN),
    ('Dark matter:', 'Yes (neutralino)', GREEN),
]
for i, (prop, val, color) in enumerate(mssm_props):
    y = 3.8 - i * 0.55
    ax.text(6.0, y, prop, fontsize=9, color=SILVER)
    ax.text(8.5, y, val, fontsize=10, color=color, fontweight='bold')

# Bottom
ax.text(5.0, 0.5, 'The MSSM\'s unification success is not unique to supersymmetry.\n'
        'One particle achieves comparable gap ratio. But the MSSM solves\n'
        'multiple problems simultaneously (unification + dark matter + hierarchy).',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys13_06_vl_vs_mssm.png')


# ================================================================
# FIG 7: M_GUT COMPARISON — SM, VL DOUBLET, MSSM
# Type: Comparison bar (log)
# Shows: M_GUT values on log scale for the three models.
# The scale separation is visual.
# ================================================================

fig, ax = dark_fig("Unification Scale: Where Do the Couplings Meet?",
                   xlabel="",
                   ylabel="log\u2081\u2080(M_GUT / GeV)",
                   size=(16, 10))

models = [
    ('SM\n(doesn\'t unify)', 13.80, RED, '\u0394 = 6.58\n(40% miss)'),
    ('SM + VL doublet\n(3,2,1/6)', 15.50, CYAN, '\u0394 = 0.69\n(3.6% miss)'),
    ('MSSM\n(full SUSY)', 17.32, GREEN, '\u0394 = 0.69\n(2.7% miss)'),
]

for i, (label, log_gut, color, quality) in enumerate(models):
    ax.bar(i, log_gut, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    ax.text(i, log_gut + 0.3, '10^{%.1f}' % log_gut, fontsize=12,
            color=color, ha='center', fontweight='bold')
    ax.text(i, log_gut - 1.0, quality, fontsize=9, color=SILVER,
            ha='center')

ax.set_xticks([0, 1, 2])
ax.set_xticklabels([m[0] for m in models], fontsize=10, color=SILVER)

# Proton decay boundary
ax.plot([-0.5, 2.5], [15.5, 15.5], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.7)
ax.text(2.6, 15.5, 'Proton decay\nboundary\n(Super-K)', fontsize=9,
        color=GOLD, va='center', fontweight='bold')

# Hyper-K reach
ax.plot([-0.5, 2.5], [16.0, 16.0], color=ORANGE, linewidth=1.5,
        linestyle=':', alpha=0.5)
ax.text(2.6, 16.0, 'Hyper-K\nreach', fontsize=8, color=ORANGE, va='center')

# Scale context
ax.text(-0.5, 12.5, 'M_Z = 91 GeV\n(log\u2081\u2080 = 1.96)', fontsize=8,
        color=DIM)

ax.set_xlim(-0.8, 3.2)
ax.set_ylim(12, 19)

save_fig(fig, 'phys13_07_mgut_comparison.png')


# ================================================================
# FIG 8: PHYS-13 IDENTITY CARD
# Type: Identity card
# Shows: 218/115 vs 1.358, VL doublet, proton decay boundary.
# ================================================================

fig, ax = dark_canvas("PHYS-13 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, '218/115 MEETS THE UNIVERSE', fontsize=20,
        color=GOLD, ha='center', fontweight='bold')

# The gap ratio
ax.text(5, 8.0, 'SM gap ratio: 218/115 = 1.896', fontsize=14,
        color=RED, ha='center', fontweight='bold')
ax.text(5, 7.3, 'Measured: 1.358', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 6.7, '40% miss. The Standard Model does not unify.',
        fontsize=11, color=SILVER, ha='center')

# Left: the finding
ax.text(2.5, 5.5, 'THE FINDING', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

finding_items = [
    ('VL quark doublet (3,2,1/6)', 'Gap = 38/27 = 1.407', CYAN),
    ('Distance from measured', '0.049 (cf. MSSM: 0.042)', CYAN),
    ('M_GUT = 10^{15.5} GeV', 'On proton decay boundary', GOLD),
    ('1 new particle', 'vs MSSM\'s ~30', GREEN),
]
for i, (item, detail, color) in enumerate(finding_items):
    y = 4.7 - i * 0.7
    ax.text(1.0, y, item, fontsize=9, color=color, fontweight='bold')
    ax.text(1.0, y - 0.3, detail, fontsize=8, color=DIM)

# Right: the simplification
ax.text(7.5, 5.5, 'GAP RATIO ANATOMY', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

ratios = [
    ('SM:', '218/115', '3-digit integers', RED),
    ('MSSM:', '7/5', '1-digit integers', GREEN),
    ('VL doublet:', '38/27', '2-digit integers', CYAN),
]
for i, (model, ratio, note_text, color) in enumerate(ratios):
    y = 4.7 - i * 0.8
    ax.text(6.0, y, model, fontsize=10, color=SILVER)
    ax.text(7.5, y, ratio, fontsize=14, color=color, fontweight='bold',
            fontfamily='monospace')
    ax.text(9.0, y, note_text, fontsize=8, color=DIM)

# Bottom
ax.plot([0.5, 9.5], [1.8, 1.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 1.3, 'THE INTEGER ANATOMY', fontsize=12, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 0.7, 'Beta coefficients are exact rationals from the gauge group.\n'
        'The gap ratio is where integer structure meets measured reality.\n'
        '218/115 \u2260 1.358. The integers of the SM are not the integers of the universe above M_Z.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys13_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-13 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys13_01_sm_vs_mssm_running.png',
    'phys13_02_proton_decay.png',
    'phys13_03_gap_ratio.png',
    'phys13_04_bsm_enumeration.png',
    'phys13_05_three_line_convergence.png',
    'phys13_06_vl_vs_mssm.png',
    'phys13_07_mgut_comparison.png',
    'phys13_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    