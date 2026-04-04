#!/usr/bin/env python3
"""
HOWL PHYS-20 Diagrams — The Proton Decay Test
8 figures covering M_GUT^4 scaling, testability sweet spot, Hyper-K timeline,
scenario landscape, amplification chain, decay process, uncertainties.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: TAU VS M_GUT — THE M_GUT^4 SCALING CURVE
# Type: Running/scaling
# Shows: Proton lifetime vs M_GUT on log-log axes. The steep
# fourth-power curve with SM, 5+5bar, CD, MSSM marked.
# Super-K bound and Hyper-K sensitivity as horizontal bands.
# ================================================================

fig, ax = dark_fig("Proton Lifetime vs Unification Scale: The M_GUT\u2074 Scaling",
                   xlabel="log\u2081\u2080(M_GUT / GeV)",
                   ylabel="log\u2081\u2080(\u03c4 / years)",
                   size=(16, 10))

# M_GUT^4 curve (using reference: CD at 10^15.5 gives tau ~ 10^34.5)
# tau proportional to M_GUT^4, so log(tau) = 4*log(M_GUT) + const
# const = 34.5 - 4*15.5 = 34.5 - 62 = -27.5
log_mgut = np.linspace(13.0, 18.0, 200)
log_tau = 4 * log_mgut - 27.5

curve(ax, log_mgut, log_tau, '\u03c4 \u221d M_GUT\u2074 (minimal SU(5))', CYAN, 2.5)

# Mark the four scenarios
scenarios = [
    (13.80, 'SM', RED, '218/115'),
    (14.90, '5+5\u0305', ORANGE, '40/27'),
    (15.50, 'Cabibbo\nDoublet', GOLD, '38/27'),
    (17.32, 'MSSM', GREEN, '7/5'),
]

for log_m, label, color, gap in scenarios:
    log_t = 4 * log_m - 27.5
    data_point(ax, log_m, log_t, '', color, size=300)
    y_off = 1.0 if label != 'MSSM' else -1.5
    x_off = 0.15
    ax.text(log_m + x_off, log_t + y_off,
            '%s\nM = 10^{%.1f}\ngap = %s' % (label, log_m, gap),
            fontsize=8, color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color,
                      alpha=0.8))

# Super-K bound
ax.plot([13.0, 18.0], [np.log10(2.4e34), np.log10(2.4e34)], color=RED,
        linewidth=2.5, linestyle='--', alpha=0.7)
ax.fill_between([13.0, 18.0], [28, 28], [np.log10(2.4e34), np.log10(2.4e34)],
                alpha=0.05, color=RED)
ax.text(17.5, 33.9, 'Super-K bound\n\u03c4 > 2.4\u00d710\u00b3\u2074 yr', fontsize=9,
        color=RED, ha='right', fontweight='bold')
ax.text(15.5, 31, 'EXCLUDED', fontsize=14, color=RED, ha='center',
        alpha=0.3, fontweight='bold')

# Hyper-K sensitivity
ax.plot([13.0, 18.0], [35.0, 35.0], color=MAG, linewidth=2,
        linestyle=':', alpha=0.6)
ax.text(17.5, 35.2, 'Hyper-K reach\n(20 yr)', fontsize=9, color=MAG,
        ha='right', fontweight='bold')

# Hyper-K window shading
ax.fill_between([13.0, 18.0],
                [np.log10(2.4e34), np.log10(2.4e34)],
                [35.0, 35.0],
                alpha=0.04, color=GREEN)
ax.text(14.5, 34.6, 'HYPER-K\nWINDOW', fontsize=10, color=GREEN,
        ha='center', fontweight='bold', alpha=0.5)

ax.set_xlim(13.0, 18.0)
ax.set_ylim(28, 40)

save_fig(fig, 'phys20_01_tau_vs_mgut.png')


# ================================================================
# FIG 2: TESTABILITY SWEET SPOT
# Type: Scale/threshold
# Shows: log10(M_GUT) axis with excluded region (Super-K),
# Hyper-K window, and beyond-reach. CD sits in the window.
# ================================================================

fig, ax = dark_fig("The Testability Sweet Spot",
                   xlabel="log\u2081\u2080(M_GUT / GeV)",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([13, 18], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Excluded region (left)
ax.fill_between([13, 15.35], [0.0, 0.0], [1.0, 1.0], alpha=0.08, color=RED)
ax.plot([15.35, 15.35], [0.0, 1.0], color=RED, linewidth=3)
ax.text(14.2, 0.5, 'EXCLUDED\nby Super-K\n(\u03c4 < 2.4\u00d710\u00b3\u2074)',
        fontsize=10, color=RED, ha='center', fontweight='bold')

# Hyper-K window (middle)
ax.fill_between([15.35, 15.8], [0.15, 0.15], [0.85, 0.85],
                alpha=0.08, color=GREEN)
ax.text(15.57, 1.3, 'HYPER-K\nWINDOW', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')

# Beyond reach (right)
ax.fill_between([15.8, 18], [0.0, 0.0], [1.0, 1.0], alpha=0.04, color=DIM)
ax.text(16.8, 0.5, 'BEYOND\nHYPER-K\nREACH', fontsize=10, color=DIM,
        ha='center', fontweight='bold')

# Scenarios
scenario_marks = [
    (13.80, 'SM\n10\u00b9\u00b3\u00b7\u2078', RED, -0.5),
    (14.90, '5+5\u0305\n10\u00b9\u2074\u00b7\u2079', ORANGE, -0.5),
    (15.50, 'Cabibbo\nDoublet\n10\u00b9\u2075\u00b7\u2075', GOLD, -0.8),
    (17.32, 'MSSM\n10\u00b9\u2077\u00b7\u00b3', GREEN, -0.5),
]

for log_m, label, color, y_off in scenario_marks:
    ax.plot([log_m, log_m], [0.2, 0.8], color=color, linewidth=2.5)
    data_point(ax, log_m, 0.5, '', color, size=250)
    ax.text(log_m, y_off, label, fontsize=9, color=color,
            ha='center', fontweight='bold')

# Highlight CD in the window
ax.scatter([15.50], [0.5], s=600, facecolors='none', edgecolors=GOLD,
           linewidth=3, zorder=11)

result_box(ax, 15.5, -1.6,
           'The Cabibbo Doublet sits in the narrow band:\n'
           'just above the Super-K exclusion,\n'
           'just within Hyper-K reach.\n'
           'This is the testability sweet spot.',
           GOLD, 10)

ax.set_xlim(13, 18)
ax.set_ylim(-2.2, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys20_02_sweet_spot.png')


# ================================================================
# FIG 3: HYPER-K SENSITIVITY GROWING OVER TIME
# Type: Running/timeline
# Shows: Projected proton decay limit improving from 2027 to 2047.
# CD viable range shaded. The overlap shows when the answer comes.
# ================================================================

fig, ax = dark_fig("Hyper-Kamiokande: Sensitivity Growing Into the Prediction Range",
                   xlabel="Year",
                   ylabel="Projected \u03c4 limit (years, log scale)",
                   size=(16, 10))

# Super-K legacy (before 2027)
years_sk = [2020, 2027]
limits_sk = [np.log10(2.4e34), np.log10(2.4e34)]
curve(ax, years_sk, limits_sk, 'Super-K (current bound)', RED, 2, style='--')

# Hyper-K projected limits
years_hk = [2027, 2032, 2037, 2042, 2047]
limits_hk = [np.log10(2.4e34), np.log10(4e34), np.log10(6.3e34),
             np.log10(8e34), 35.0]
curve(ax, years_hk, limits_hk, 'Hyper-K projected limit', CYAN, 3)

for yr, lim in zip(years_hk, limits_hk):
    data_point(ax, yr, lim, '', CYAN, size=150)

# CD viable range
ax.fill_between([2018, 2050], [np.log10(3e34), np.log10(3e34)],
                [35.0, 35.0], alpha=0.06, color=GOLD)
ax.text(2023, 34.8, 'Cabibbo Doublet\nviable range\n(3\u00d710\u00b3\u2074 to 10\u00b3\u2075)',
        fontsize=10, color=GOLD, fontweight='bold')

# Key milestones
ax.text(2032, np.log10(4e34) + 0.12, '5 yr:\n4\u00d710\u00b3\u2074', fontsize=8,
        color=SILVER, ha='center')
ax.text(2037, np.log10(6.3e34) + 0.12, '10 yr:\n6.3\u00d710\u00b3\u2074', fontsize=8,
        color=GREEN, ha='center', fontweight='bold')
ax.text(2047, 35.1, '20 yr:\n10\u00b3\u2075', fontsize=8,
        color=GREEN, ha='center', fontweight='bold')

# "Answer arrives" annotation
ax.annotate('Answer arrives\nin this decade', xy=(2035, np.log10(5.5e34)),
            xytext=(2042, 34.4),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# MSSM prediction (far above)
ax.plot([2018, 2050], [37, 37], color=GREEN, linewidth=1, linestyle=':',
        alpha=0.4)
ax.text(2045, 37.1, 'MSSM: \u03c4 ~ 10\u00b3\u2077\n(far beyond reach)', fontsize=8,
        color=GREEN, alpha=0.5)

ax.set_xlim(2018, 2050)
ax.set_ylim(34.0, 37.5)

save_fig(fig, 'phys20_03_hyper_k_timeline.png')


# ================================================================
# FIG 4: FOUR SCENARIOS ON LOG10(TAU) AXIS
# Type: Scale/landscape
# Shows: SM (~10^30, excluded), 5+5bar (~10^32, excluded),
# CD (~10^34-35, at boundary), MSSM (~10^37, safe).
# Super-K bound and Hyper-K reach marked.
# ================================================================

fig, ax = dark_fig("Four Scenarios on the Proton Lifetime Scale",
                   xlabel="log\u2081\u2080(\u03c4 / years)",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([29, 39], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Scenarios
scenarios_tau = [
    (27.5, 'SM\n(min. SU(5))\n10\u00b3\u2070 yr', RED),
    (32.1, 'SU(5) 5+5\u0305\n10\u00b3\u00b2 yr', ORANGE),
    (34.5, 'Cabibbo\nDoublet\n10\u00b3\u2074\u207b\u00b3\u2075 yr', GOLD),
    (37.0, 'MSSM\n10\u00b3\u2077 yr', GREEN),
]

# Age of universe for reference
ax.plot([np.log10(1.38e10), np.log10(1.38e10)], [0.2, 0.8],
        color=DIM, linewidth=1.5, linestyle=':', alpha=0.4)
ax.text(np.log10(1.38e10), -0.3, 'Age of\nuniverse', fontsize=7,
        color=DIM, ha='center')

for log_t, label, color in scenarios_tau:
    ax.plot([log_t, log_t], [0.1, 0.9], color=color, linewidth=2.5)
    data_point(ax, log_t, 0.5, '', color, size=300)
    ax.text(log_t, -0.5, label, fontsize=9, color=color,
            ha='center', fontweight='bold')

# Super-K bound
ax.plot([np.log10(2.4e34), np.log10(2.4e34)], [0.0, 1.0],
        color=RED, linewidth=3)
ax.fill_between([29, np.log10(2.4e34)], [0.0, 0.0], [1.0, 1.0],
                alpha=0.06, color=RED)
ax.text(np.log10(2.4e34), 1.2, 'Super-K\nbound', fontsize=9,
        color=RED, ha='center', fontweight='bold')

# Hyper-K reach
ax.plot([35.0, 35.0], [0.0, 1.0], color=MAG, linewidth=2.5,
        linestyle='--')
ax.text(35.0, 1.2, 'Hyper-K\nreach\n(20 yr)', fontsize=9,
        color=MAG, ha='center', fontweight='bold')

# Labels
ax.text(32.0, 1.5, 'EXCLUDED', fontsize=12, color=RED,
        ha='center', fontweight='bold', alpha=0.4)
ax.text(36.5, 1.5, 'BEYOND REACH', fontsize=12, color=DIM,
        ha='center', fontweight='bold', alpha=0.4)

ax.set_xlim(29, 39)
ax.set_ylim(-1.2, 2.0)
ax.set_yticks([])

save_fig(fig, 'phys20_04_four_scenarios.png')


# ================================================================
# FIG 5: GAP 0.007 → MGUT FACTOR 63 → TAU FACTOR 10^7
# Type: Comparison/amplification
# Shows: Three-stage amplification. Nearly identical gap ratios
# become enormously different proton lifetimes.
# ================================================================

fig, ax = dark_canvas("The 10\u2077 Amplification: From Gap Ratio to Proton Lifetime",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Stage 1: Gap ratio
ax.text(1.5, 8.5, 'STAGE 1: Gap Ratio', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

ax.text(1.5, 7.3, 'CD: 38/27 = 1.407', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(1.5, 6.6, 'MSSM: 7/5 = 1.400', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(1.5, 5.8, 'Difference: 0.007', fontsize=11, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Arrow 1→2
ax.annotate('Running equations\namplify over\n15 decades', xy=(3.8, 7.0),
            xytext=(2.5, 7.0),
            fontsize=9, color=SILVER,
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Stage 2: M_GUT
ax.text(5.0, 8.5, 'STAGE 2: M_GUT', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

ax.text(5.0, 7.3, 'CD: 10\u00b9\u2075\u00b7\u2075 GeV', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(5.0, 6.6, 'MSSM: 10\u00b9\u2077\u00b7\u00b3 GeV', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(5.0, 5.8, 'Factor: 63\u00d7', fontsize=11, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Arrow 2→3
ax.annotate('\u03c4 \u221d M_GUT\u2074\n(fourth power!)', xy=(7.2, 7.0),
            xytext=(6.0, 7.0),
            fontsize=9, color=SILVER,
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Stage 3: Proton lifetime
ax.text(8.5, 8.5, 'STAGE 3: \u03c4(proton)', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

ax.text(8.5, 7.3, 'CD: ~10\u00b3\u2074\u207b\u00b3\u2075 yr', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(8.5, 6.6, 'MSSM: ~10\u00b3\u2077 yr', fontsize=12, color=GREEN,
        ha='center', fontweight='bold')
ax.text(8.5, 5.8, 'Factor: 10\u2077\u00d7', fontsize=13, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                  linewidth=2))

# Bottom summary
result_box(ax, 5.0, 2.5,
           'Gap ratio difference: 0.007 (0.5%)\n'
           'M_GUT difference: factor 63 (from running amplification)\n'
           'Lifetime difference: 63\u2074 = 1.6 \u00d7 10\u2077 (from \u03c4 \u221d M_GUT\u2074)\n\n'
           'Nearly identical gap ratios produce\n'
           'SEVEN ORDERS OF MAGNITUDE difference in proton lifetime.\n'
           'Hyper-K can tell them apart.',
           GOLD, 10)

# The amplification chain at bottom
ax.text(1.5, 1.0, '0.007', fontsize=16, color=SILVER, ha='center',
        fontweight='bold')
ax.annotate('', xy=(3.5, 1.0), xytext=(2.3, 1.0),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
ax.text(5.0, 1.0, '63\u00d7', fontsize=16, color=ORANGE, ha='center',
        fontweight='bold')
ax.annotate('', xy=(7.0, 1.0), xytext=(5.8, 1.0),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
ax.text(8.5, 1.0, '10\u2077\u00d7', fontsize=20, color=GOLD, ha='center',
        fontweight='bold')

save_fig(fig, 'phys20_05_amplification.png')


# ================================================================
# FIG 6: PROTON DECAY PROCESS p → e+pi0
# Type: Geometric/process
# Shows: Proton (uud) → X boson exchange → positron + pi0 → gamma gamma.
# The three-ring Cherenkov signature.
# ================================================================

fig, ax = dark_canvas("Proton Decay: p \u2192 e\u207a\u03c0\u2070 via X Boson Exchange",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Initial state: proton
ax.text(1.5, 7.5, 'PROTON', fontsize=16, color=RED, ha='center',
        fontweight='bold')

quark_y = [6.8, 6.0, 5.2]
quark_labels = ['u', 'u', 'd']
quark_colors = [CYAN, CYAN, GREEN]

for y, ql, qc in zip(quark_y, quark_labels, quark_colors):
    data_point(ax, 1.5, y, '', qc, size=200)
    ax.text(1.9, y, ql, fontsize=14, color=qc, fontweight='bold')

# Proton circle
proton_circ = plt.Circle((1.5, 6.0), 1.2, fill=False, edgecolor=RED,
                           linewidth=2, linestyle='--', zorder=1)
ax.add_patch(proton_circ)
ax.text(1.5, 4.5, 'uud\nm_p = 938 MeV', fontsize=9, color=SILVER,
        ha='center')

# X boson exchange
ax.annotate('', xy=(4.5, 6.8), xytext=(2.2, 6.8),
            arrowprops=dict(arrowstyle='->', color=MAG, lw=3,
                            linestyle='--'))
ax.annotate('', xy=(4.5, 5.2), xytext=(2.2, 5.2),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

# X boson vertex
ax.text(3.5, 7.5, 'X boson\n(M ~ M_GUT)', fontsize=10, color=MAG,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=MAG))

# Wavy line for X boson
x_wave = np.linspace(2.8, 4.2, 80)
y_wave = 6.0 + 0.15 * np.sin(x_wave * 15)
ax.plot(x_wave, y_wave, color=MAG, linewidth=2, alpha=0.7)

# Final state particles
# Positron
data_point(ax, 5.5, 7.5, '', ORANGE, size=250)
ax.text(5.5, 8.2, 'e\u207a (positron)', fontsize=12, color=ORANGE,
        ha='center', fontweight='bold')
ax.annotate('', xy=(5.5, 7.5), xytext=(4.5, 6.8),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

# Neutral pion
data_point(ax, 5.5, 5.0, '', BLUE, size=250)
ax.text(5.5, 4.3, '\u03c0\u2070 (neutral pion)', fontsize=12, color=BLUE,
        ha='center', fontweight='bold')
ax.annotate('', xy=(5.5, 5.0), xytext=(4.5, 5.2),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=2))

# Pi0 → gamma gamma
ax.annotate('\u03b3', xy=(7.5, 6.0), xytext=(6.0, 5.2),
            fontsize=14, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2,
                            linestyle='--'))
ax.annotate('\u03b3', xy=(7.5, 4.0), xytext=(6.0, 4.8),
            fontsize=14, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2,
                            linestyle='--'))
ax.text(5.5, 5.7, '\u03c4 = 8.5\u00d710\u207b\u00b9\u2077 s', fontsize=7,
        color=DIM, ha='center')

# Cherenkov signature (right side)
ax.text(8.5, 8.5, 'DETECTOR SIGNATURE', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')

rings = [
    ('Ring 1: e\u207a', ORANGE, 0.5),
    ('Ring 2: \u03b3\u2081', GOLD, 0.35),
    ('Ring 3: \u03b3\u2082', GOLD, 0.35),
]

for i, (label, color, r) in enumerate(rings):
    y_c = 6.5 - i * 1.5
    ring = plt.Circle((8.5, y_c), r, fill=False, edgecolor=color,
                        linewidth=2, alpha=0.6, zorder=3)
    ax.add_patch(ring)
    ax.text(9.3, y_c, label, fontsize=9, color=color, fontweight='bold')

ax.text(8.5, 2.5, 'Total energy = 938 MeV\nTotal momentum = 0\nAlmost background-free',
        fontsize=9, color=SILVER, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM))

# Conservation laws at bottom
ax.text(5.0, 1.5, 'B: +1 \u2192 0 (baryon number violated)',
        fontsize=9, color=RED, ha='center')
ax.text(5.0, 0.8, 'B\u2212L: 0 \u2192 0 (conserved)     Q: +1 \u2192 +1 (conserved)',
        fontsize=9, color=GREEN, ha='center')

save_fig(fig, 'phys20_06_decay_process.png')


# ================================================================
# FIG 7: UNCERTAINTY SOURCES — EFFECT ON LOG10(TAU)
# Type: Comparison bar
# Shows: Each uncertainty source and its effect on log10(tau).
# GUT completion dominates. The honest assessment.
# ================================================================

fig, ax = dark_fig("Sources of Uncertainty in the Proton Lifetime Prediction",
                   xlabel="Effect on log\u2081\u2080(\u03c4) (orders of magnitude)",
                   ylabel="",
                   size=(16, 10))

sources = [
    ('GUT completion\ngroup', 2.0, RED, 'SU(5) vs SO(10)\nvs Pati-Salam'),
    ('GUT threshold\ncorrections', 1.0, ORANGE, 'X,Y boson\nmass splitting'),
    ('Cabibbo Doublet\nmass (1.5\u20136 TeV)', 0.5, CYAN, 'Running threshold\nat M_VL'),
    ('Hadronic matrix\nelement', 0.3, GREEN, 'Lattice QCD\nuncertainty'),
    ('Two-loop\nrunning', 0.2, BLUE, 'Perturbative\ncorrection'),
    ('\u03b1_GUT\nuncertainty', 0.1, DIM, 'From coupling\nrunning'),
]

y_pos = np.arange(len(sources))

for i, (label, effect, color, detail) in enumerate(sources):
    # Symmetric error bar representation
    ax.barh(i, effect, color=color, alpha=0.6, edgecolor=color,
            linewidth=2, height=0.6)
    ax.barh(i, -effect, color=color, alpha=0.3, edgecolor=color,
            linewidth=1, height=0.6)
    ax.text(effect + 0.1, i, '\u00b1%.1f' % effect, fontsize=10,
            color=color, fontweight='bold', va='center')
    ax.text(-effect - 0.1, i, detail, fontsize=7, color=DIM,
            va='center', ha='right')

ax.set_yticks(y_pos)
ax.set_yticklabels([s[0] for s in sources], fontsize=9, color=SILVER)

# Zero line
ax.plot([0, 0], [-0.8, 5.8], color=GOLD, linewidth=1.5, alpha=0.5)

# Combined range
ax.text(0, -0.8, 'Combined: log\u2081\u2080(\u03c4) = 34 to 35\n(\u00b10.5 from central)',
        fontsize=10, color=GOLD, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_xlim(-2.8, 3.0)
ax.set_ylim(-1.5, 5.8)

save_fig(fig, 'phys20_07_uncertainties.png')


# ================================================================
# FIG 8: PHYS-20 IDENTITY CARD
# Type: Identity card
# Shows: M_GUT = 10^15.5, tau ~ 10^34-35, Hyper-K 2027-2037.
# One experiment, one decade, one answer.
# ================================================================

fig, ax = dark_canvas("PHYS-20 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE PROTON DECAY TEST', fontsize=22, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'One experiment. One decade. One answer.',
        fontsize=12, color=SILVER, ha='center', style='italic')

# The chain
ax.text(5, 7.5, 'THE CHAIN', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

chain_items = [
    ('Gap ratio:', '38/27 = 1.407', '(PHYS-15, exact Fraction)', CYAN),
    ('M_GUT:', '10\u00b9\u2075\u00b7\u2075 GeV', '(GUT script, 9/9 PASS)', GREEN),
    ('\u03c4(p \u2192 e\u207a\u03c0\u2070):', '~10\u00b3\u2074\u207b\u00b3\u2075 yr', '(minimal SU(5))', GOLD),
    ('Super-K bound:', '> 2.4\u00d710\u00b3\u2074 yr', '(at the boundary)', RED),
    ('Hyper-K reach:', '~10\u00b3\u2075 yr (20 yr)', '(covers full range)', MAG),
]
for i, (prop, val, source, color) in enumerate(chain_items):
    y = 6.8 - i * 0.6
    ax.text(2.0, y, prop, fontsize=10, color=SILVER)
    ax.text(5.0, y, val, fontsize=12, color=color, fontweight='bold')
    ax.text(8.0, y, source, fontsize=8, color=DIM)

# The discriminator
ax.plot([0.5, 9.5], [3.8, 3.8], color=DIM, linewidth=1, linestyle=':',
        alpha=0.4)
ax.text(5, 3.3, 'THE DISCRIMINATOR', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

disc_items = [
    ('Cabibbo Doublet', '\u03c4 ~ 10\u00b3\u2034\u207b\u00b3\u2035 yr', 'Hyper-K SEES it', CYAN),
    ('MSSM', '\u03c4 ~ 10\u00b3\u2037 yr', 'Hyper-K CANNOT see it', GREEN),
    ('Separation:', '10\u2077\u00d7 in lifetime', 'from 0.007 in gap ratio', GOLD),
]
for i, (model, tau_val, verdict, color) in enumerate(disc_items):
    y = 2.6 - i * 0.5
    ax.text(2.0, y, model, fontsize=10, color=color, fontweight='bold')
    ax.text(5.0, y, tau_val, fontsize=10, color=color)
    ax.text(8.0, y, verdict, fontsize=9, color=SILVER)

# Bottom
ax.text(5, 0.5, 'Hyper-Kamiokande begins ~2027. Sensitivity reaches 10\u00b3\u2035 yr by ~2047.\n'
        'If proton decay is observed: M_GUT confirmed, MSSM excluded.\n'
        'If not: minimal SU(5) excluded, Cabibbo Doublet survives via non-minimal GUT.',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys20_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-20 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys20_01_tau_vs_mgut.png',
    'phys20_02_sweet_spot.png',
    'phys20_03_hyper_k_timeline.png',
    'phys20_04_four_scenarios.png',
    'phys20_05_amplification.png',
    'phys20_06_decay_process.png',
    'phys20_07_uncertainties.png',
    'phys20_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    