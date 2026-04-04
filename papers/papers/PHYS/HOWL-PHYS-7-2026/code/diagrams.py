#!/usr/bin/env python3
"""
HOWL PHYS-7 Diagrams — The Strong CP Problem Is Not a Problem
8 figures covering energy functional, ground state analogy, instanton landscape,
rephasing invariance, double standard, vacuum identification.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: E(THETA) = E0 - CHI_TOP * COS(THETA)
# Type: Running/convergence
# Shows: The cosine energy functional with its unique minimum
# at theta=0. The ground state IS the minimum. The curve shape
# is the entire argument of the paper.
# ================================================================

fig, ax = dark_fig("E(\u03b8) = E\u2080 \u2212 \u03c7_top \u00b7 cos(\u03b8): The Ground State Is at \u03b8 = 0",
                   xlabel="\u03b8",
                   ylabel="E(\u03b8) \u2212 E\u2080  (units of \u03c7_top)",
                   size=(16, 10))

theta = np.linspace(-np.pi, 3 * np.pi, 500)
E = -np.cos(theta)

curve(ax, theta, E, 'E(\u03b8) = E\u2080 \u2212 \u03c7_top cos(\u03b8)', CYAN, 3)

# Ground state at theta = 0
data_point(ax, 0, -1, '', GOLD, size=400)
ax.scatter([0], [-1], s=500, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)

# Also at 2pi (periodic)
data_point(ax, 2 * np.pi, -1, '', GOLD, size=250)

# Ground state label
ax.annotate('GROUND STATE\n\u03b8 = 0\nE = E\u2080 \u2212 \u03c7_top\n(minimum)',
            xy=(0, -1), xytext=(1.8, -0.3),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Maximum at pi
data_point(ax, np.pi, 1, '', RED, size=200)
ax.text(np.pi, 1.2, '\u03b8 = \u03c0\nmaximum\n(excluded by\nneutron EDM)',
        fontsize=9, color=RED, ha='center')

# Axis labels
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(['0', '\u03c0/2', '\u03c0', '3\u03c0/2', '2\u03c0'],
                    fontsize=11, color=SILVER)

# The argument
result_box(ax, 7.5, 0.5,
           'The vacuum is the minimum energy state.\n'
           'The minimum is at \u03b8 = 0.\n'
           'Therefore the vacuum has \u03b8 = 0.\n\n'
           'This is not a problem.\nIt is the ground state.',
           GOLD, 10)

ax.set_xlim(-0.8, 9.5)
ax.set_ylim(-1.5, 1.8)

save_fig(fig, 'phys7_01_energy_functional.png')


# ================================================================
# FIG 2: E(THETA) + HYDROGEN E(n) DUAL PANEL
# Type: Dual-panel
# Shows: Left: E(theta) with minimum at 0. Right: hydrogen E(n)
# with minimum at n=1. Both are ground states. Neither requires
# a mechanism. The parallel is the argument.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "QCD Vacuum: E(\u03b8) = E\u2080 \u2212 \u03c7 cos(\u03b8)",
    "Hydrogen Atom: E(n) = \u221213.6/n\u00b2 eV",
    size=(18, 9), wspace=0.35)

# Left: E(theta)
theta = np.linspace(-0.5, 2 * np.pi + 0.5, 300)
E_theta = -np.cos(theta)
curve(ax1, theta, E_theta, '', CYAN, 2.5)

data_point(ax1, 0, -1, '', GOLD, size=350)
ax1.scatter([0], [-1], s=400, facecolors='none', edgecolors=GOLD,
            linewidth=2.5, zorder=11)
ax1.text(0, -0.6, 'Ground state\n\u03b8 = 0', fontsize=11, color=GOLD,
         ha='center', fontweight='bold')

ax1.set_xlabel('\u03b8', color=SILVER, fontsize=12)
ax1.set_ylabel('E(\u03b8) / \u03c7_top', color=SILVER, fontsize=11)
ax1.set_xticks([0, np.pi, 2 * np.pi])
ax1.set_xticklabels(['0', '\u03c0', '2\u03c0'], fontsize=10, color=SILVER)
ax1.set_xlim(-0.8, 7.0)
ax1.set_ylim(-1.5, 1.5)

ax1.text(3.5, -1.2, 'Problem declared:\n"Why is \u03b8 = 0?"',
         fontsize=10, color=RED, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# Right: hydrogen E(n)
n_vals = np.arange(1, 8)
E_H = -13.6 / n_vals**2

for i, n in enumerate(n_vals):
    ax2.plot([n - 0.3, n + 0.3], [E_H[i], E_H[i]], color=CYAN,
             linewidth=2.5, zorder=4)

data_point(ax2, 1, -13.6, '', GOLD, size=350)
ax2.scatter([1], [-13.6], s=400, facecolors='none', edgecolors=GOLD,
            linewidth=2.5, zorder=11)
ax2.text(1, -11.5, 'Ground state\nn = 1', fontsize=11, color=GOLD,
         ha='center', fontweight='bold')

# n=47 for the analogy
ax2.text(5, -1.0, 'n = 47 exists\nbut hydrogen\nis not there', fontsize=9,
         color=DIM, ha='center', style='italic')

ax2.set_xlabel('n (principal quantum number)', color=SILVER, fontsize=11)
ax2.set_ylabel('E(n) (eV)', color=SILVER, fontsize=11)
ax2.set_xlim(0, 8)
ax2.set_ylim(-15, 1)

ax2.text(4.5, -13, 'No problem declared.\nNo mechanism demanded.\nIt is the ground state.',
         fontsize=10, color=GREEN, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

save_fig(fig, 'phys7_02_ground_state_parallel.png')


# ================================================================
# FIG 3: INSTANTON LANDSCAPE — BARRIERS BETWEEN INTEGER SECTORS
# Type: Running/landscape
# Shows: Periodic potential with energy barriers between integer
# topological sectors n=-2,-1,0,1,2. Instantons tunnel through
# the barriers. The discrete topology is visible.
# ================================================================

fig, ax = dark_fig("Instanton Landscape: Integer Topological Sectors",
                   xlabel="Gauge field configuration space",
                   ylabel="Energy",
                   size=(16, 10))

# Periodic potential between integer sectors
x = np.linspace(-2.5, 2.5, 500)
# Energy landscape: barriers between integer sectors
V = 1.0 - np.cos(2 * np.pi * x)

curve(ax, x, V, '', CYAN, 2.5)

# Integer sector labels
for n in range(-2, 3):
    # Minimum at each integer
    data_point(ax, n, 0, '', GOLD if n == 0 else SILVER, size=250)
    ax.text(n, -0.35, 'n = %d' % n, fontsize=12,
            color=GOLD if n == 0 else SILVER,
            ha='center', fontweight='bold')

# Highlight ground state
ax.scatter([0], [0], s=400, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)

# Barriers
for n in [-2, -1, 0, 1]:
    mid = n + 0.5
    ax.plot([mid, mid], [1.8, 2.2], color=RED, linewidth=2, alpha=0.5)
    ax.text(mid, 2.3, 'barrier', fontsize=7, color=RED, ha='center',
            rotation=0, alpha=0.7)

# Instanton tunneling arrows
ax.annotate('', xy=(1, 0.2), xytext=(0, 0.2),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2,
                            connectionstyle='arc3,rad=-0.5'))
ax.text(0.5, 0.9, 'instanton\n(tunneling)', fontsize=9, color=ORANGE,
        ha='center', fontweight='bold')

ax.annotate('', xy=(-1, 0.2), xytext=(0, 0.2),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2,
                            connectionstyle='arc3,rad=0.5'))
ax.text(-0.5, 0.9, 'anti-instanton', fontsize=9, color=ORANGE,
        ha='center', fontweight='bold')

# Integer structure note
result_box(ax, 0, -0.9,
           '\u03c0\u2083(SU(3)) = \u2124\n'
           'Winding number is always an integer.\n'
           'This is topology, not physics. It cannot be violated.',
           GOLD, 10)

# The theta vacuum
ax.text(2.2, 1.5, '|\u03b8\u27e9 = \u03a3_n e^(in\u03b8) |n\u27e9\n'
        'Superposition of sectors.\n'
        'Ground state: \u03b8 = 0\n'
        '(minimizes E(\u03b8) = E\u2080 \u2212 \u03c7 cos\u03b8)',
        fontsize=9, color=SILVER, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_xlim(-2.8, 3.0)
ax.set_ylim(-1.3, 2.8)

save_fig(fig, 'phys7_03_instanton_landscape.png')


# ================================================================
# FIG 4: REPHASING INVARIANCE — GAUGE-DEPENDENT PIECES
# Type: Connection map with formulas
# Shows: theta_bare and arg(det M_q) transform oppositely under
# chiral rotation. Their sum theta_phys is invariant. The
# "cancellation" is gauge invariance, not fine-tuning.
# ================================================================

fig, ax = dark_canvas("Rephasing Invariance: The \"Cancellation\" Is Gauge Invariance",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# theta_bare box (left)
ax.text(2.0, 8.0, '\u03b8_bare', fontsize=20, color=ORANGE, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=ORANGE,
                  linewidth=2))
ax.text(2.0, 7.0, 'QCD topological\nterm coefficient', fontsize=9,
        color=SILVER, ha='center')

# arg(det M_q) box (right)
ax.text(8.0, 8.0, 'arg(det M_q)', fontsize=20, color=BLUE, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=BLUE,
                  linewidth=2))
ax.text(8.0, 7.0, 'Quark mass matrix\nphase', fontsize=9,
        color=SILVER, ha='center')

# Chiral rotation effects
ax.text(2.0, 5.8, 'Under q \u2192 e^(i\u03b1\u03b3\u2085)q:', fontsize=10,
        color=DIM, ha='center')
ax.text(2.0, 5.2, '\u03b8_bare \u2192 \u03b8_bare + 2N_f\u03b1', fontsize=12,
        color=ORANGE, ha='center', fontweight='bold')
ax.text(2.0, 4.6, 'CHANGES', fontsize=11, color=RED, ha='center',
        fontweight='bold')
ax.text(2.0, 4.1, 'Not observable\nin isolation', fontsize=9,
        color=RED, ha='center')

ax.text(8.0, 5.8, 'Under q \u2192 e^(i\u03b1\u03b3\u2085)q:', fontsize=10,
        color=DIM, ha='center')
ax.text(8.0, 5.2, 'arg(det M_q) \u2192 arg(det M_q) \u2212 2N_f\u03b1', fontsize=12,
        color=BLUE, ha='center', fontweight='bold')
ax.text(8.0, 4.6, 'CHANGES', fontsize=11, color=RED, ha='center',
        fontweight='bold')
ax.text(8.0, 4.1, 'Not observable\nin isolation', fontsize=9,
        color=RED, ha='center')

# Arrows to sum
ax.annotate('', xy=(5.0, 3.0), xytext=(2.5, 3.8),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
ax.annotate('', xy=(5.0, 3.0), xytext=(7.5, 3.8),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=2))

# theta_phys (center, below)
ax.text(5.0, 2.5, '\u03b8_phys = \u03b8_bare + arg(det M_q)', fontsize=16,
        color=GREEN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN,
                  linewidth=2.5))
ax.text(5.0, 1.6, 'INVARIANT under chiral rotation', fontsize=13,
        color=GREEN, ha='center', fontweight='bold')
ax.text(5.0, 1.0, 'The ONLY observable. Enters neutron EDM, \u03b7\' mass.\n'
        '+2N_f\u03b1 and \u22122N_f\u03b1 cancel BY CONSTRUCTION.\n'
        'This is not fine-tuning. This is gauge invariance.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys7_04_rephasing_invariance.png')


# ================================================================
# FIG 5: THETA-VACUUM SUPERPOSITION — INTEGER SECTORS
# Type: Geometric/progression
# Shows: Integer sectors n = -2,-1,0,1,2 with complex phase
# factors e^(in*theta), combined into the theta-vacuum.
# The integer structure is the topology.
# ================================================================

fig, ax = dark_canvas("The \u03b8-Vacuum: Superposition of Integer Sectors",
                      size=(18, 10))
ax.set_xlim(-1, 11)
ax.set_ylim(-1.5, 4.5)

# Integer sectors as boxes along a line
sectors = [-2, -1, 0, 1, 2]
colors_n = [DIM, SILVER, GOLD, SILVER, DIM]

for i, n in enumerate(sectors):
    x = 1.5 + i * 2.0
    # Sector box
    ax.text(x, 3.0, '|n=%d\u27e9' % n, fontsize=16,
            color=colors_n[i], ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=colors_n[i], linewidth=2))

    # Phase factor above
    if n == 0:
        phase = '1'
    elif n == 1:
        phase = 'e^(i\u03b8)'
    elif n == -1:
        phase = 'e^(\u2212i\u03b8)'
    elif n == 2:
        phase = 'e^(2i\u03b8)'
    else:
        phase = 'e^(\u22122i\u03b8)'
    ax.text(x, 4.0, '\u00d7 %s' % phase, fontsize=11, color=CYAN,
            ha='center')

    # Arrow down to combination
    ax.annotate('', xy=(x, 1.2), xytext=(x, 2.4),
                arrowprops=dict(arrowstyle='->', color=colors_n[i],
                                lw=1.5, alpha=0.5))

# The theta vacuum
ax.text(5.5, 0.5, '|\u03b8\u27e9 = \u03a3_n e^(in\u03b8) |n\u27e9', fontsize=22,
        color=WHITE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=2.5))

# Ground state
ax.text(5.5, -0.5, 'Ground state: \u03b8 = 0  \u2192  |\u03b8=0\u27e9 = \u03a3_n |n\u27e9\n'
        '(equal-weight superposition of ALL integer sectors)',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

# Integer line below sectors
ax.plot([0.5, 10.5], [2.0, 2.0], color=DIM, linewidth=1.5, alpha=0.4)
for i, n in enumerate(sectors):
    x = 1.5 + i * 2.0
    ax.plot([x, x], [1.9, 2.1], color=DIM, linewidth=2, alpha=0.6)

ax.text(10.5, 2.3, 'n \u2208 \u2124', fontsize=12, color=DIM, fontweight='bold')
ax.text(10.5, 1.7, '(integer by\ntopology)', fontsize=8, color=DIM)

# Dots for continuation
ax.text(0.5, 3.0, '\u00b7\u00b7\u00b7', fontsize=20, color=DIM, ha='center')
ax.text(10.5, 3.0, '\u00b7\u00b7\u00b7', fontsize=20, color=DIM, ha='center')

save_fig(fig, 'phys7_05_theta_vacuum.png')


# ================================================================
# FIG 6: DOUBLE STANDARD — ALPHA VS THETA
# Type: Comparison
# Shows: alpha = 1/137.036 (no derivation, no problem) next to
# theta = 0 (ground state, energy minimum, CP-protected, problem
# declared for 50 years). The visual irony IS the argument.
# ================================================================

fig, ax = dark_canvas("The Double Standard: Which Value Is More Mysterious?",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Left: alpha
ax.text(2.5, 8.5, '\u03b1 = 1/137.036', fontsize=22, color=CYAN,
        ha='center', fontweight='bold')

alpha_items = [
    ('Derived from deeper principle?', 'NO', RED),
    ('Energy minimum?', 'NO', RED),
    ('Symmetry protection?', 'NO', RED),
    ('Explained by any theory?', 'NO', RED),
    ('Problem declared?', 'NO', GREEN),
]
for i, (question, answer, color) in enumerate(alpha_items):
    y = 7.2 - i * 0.8
    ax.text(1.0, y, question, fontsize=10, color=SILVER)
    ax.text(4.2, y, answer, fontsize=12, color=color, fontweight='bold')

ax.text(2.5, 3.5, 'Accepted without\ncomment for 100 years.', fontsize=12,
        color=CYAN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN))

# Divider
ax.plot([5, 5], [1, 9.5], color=DIM, linewidth=2, linestyle=':', alpha=0.4)

# Right: theta
ax.text(7.5, 8.5, '\u03b8_QCD = 0', fontsize=22, color=GOLD,
        ha='center', fontweight='bold')

theta_items = [
    ('Derived from deeper principle?', 'YES (ground state)', GREEN),
    ('Energy minimum?', 'YES (cos\u03b8 minimum)', GREEN),
    ('Symmetry protection?', 'YES (CP symmetry)', GREEN),
    ('Confirmed by measurement?', 'YES (< 5\u00d710\u207b\u00b9\u00b9)', GREEN),
    ('Problem declared?', 'YES (for 50 years!)', RED),
]
for i, (question, answer, color) in enumerate(theta_items):
    y = 7.2 - i * 0.8
    ax.text(5.5, y, question, fontsize=10, color=SILVER)
    ax.text(9.2, y, answer, fontsize=12, color=color, fontweight='bold',
            ha='right')

ax.text(7.5, 3.5, 'Declared "problematic"\nfor 50 years.', fontsize=12,
        color=RED, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

# Bottom
ax.text(5.0, 1.5, 'The explained value is declared problematic.\n'
        'The unexplained value is accepted without comment.\n'
        'The priorities are inverted.',
        fontsize=12, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys7_06_double_standard.png')


# ================================================================
# FIG 7: VACUUM IDENTIFICATION ACROSS SM
# Type: Scale/comparison
# Shows: Four SM sectors. Three perform vacuum = minimum without
# comment. The fourth (QCD topological) refuses and declares a
# problem. The anomalous row is the finding.
# ================================================================

fig, ax = dark_canvas("Vacuum = Minimum Energy State: Applied Everywhere Except \u03b8",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

sectors = [
    ('Higgs', 'V(\u03c6) = \u03bc\u00b2|\u03c6|\u00b2 + \u03bb|\u03c6|\u2074',
     'v = 246 GeV', 'YES', 'NO', GREEN, 8.0),
    ('QED', 'H_QED ground state',
     'No real particles', 'YES', 'NO', GREEN, 6.2),
    ('QCD\n(perturbative)', '\u039b_QCD ground state',
     'Confined vacuum', 'YES', 'NO', GREEN, 4.4),
    ('QCD\n(topological)', 'E(\u03b8) = E\u2080 \u2212 \u03c7 cos(\u03b8)',
     '\u03b8 = 0', 'NO \u2014 refused!', 'YES \u2014 for 50 years!', RED, 2.6),
]

# Column headers
headers = ['Sector', 'Energy functional', 'Minimum', 'Vacuum =\nminimum?',
           'Problem\ndeclared?']
header_x = [0.8, 3.0, 5.5, 7.2, 8.8]

for i, h in enumerate(headers):
    ax.text(header_x[i], 9.2, h, fontsize=10, color=SILVER, ha='center',
            fontweight='bold')

ax.plot([0.3, 9.7], [8.8, 8.8], color=DIM, linewidth=1, alpha=0.4)

for sector, functional, minimum, vac_id, problem, color, y in sectors:
    # Row background for the anomalous row
    if color == RED:
        rect = plt.Rectangle((0.3, y - 0.5), 9.4, 1.2, facecolor=RED,
                               alpha=0.05, edgecolor=RED, linewidth=1.5,
                               linestyle='--', zorder=1)
        ax.add_patch(rect)

    ax.text(header_x[0], y, sector, fontsize=10, color=color,
            ha='center', fontweight='bold')
    ax.text(header_x[1], y, functional, fontsize=8, color=SILVER,
            ha='center')
    ax.text(header_x[2], y, minimum, fontsize=10, color=WHITE,
            ha='center', fontweight='bold')
    ax.text(header_x[3], y, vac_id, fontsize=10,
            color=GREEN if 'YES' == vac_id[:3] else RED,
            ha='center', fontweight='bold')
    ax.text(header_x[4], y, problem, fontsize=10,
            color=GREEN if 'NO' == problem[:2] else RED,
            ha='center', fontweight='bold')

# The finding
ax.text(5.0, 1.0, 'The same identification is performed without comment in every row\n'
        'except the last. The refusal to apply it IS the "problem."',
        fontsize=12, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys7_07_vacuum_identification.png')


# ================================================================
# FIG 8: PHYS-7 IDENTITY CARD
# Type: Identity card
# Shows: E(theta) cosine, ground state at 0, integer topology,
# double standard, "not a problem."
# ================================================================

fig, ax = dark_canvas("PHYS-7 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE STRONG CP PROBLEM IS NOT A PROBLEM',
        fontsize=18, color=GOLD, ha='center', fontweight='bold')

# The energy functional — small inset
theta_small = np.linspace(-0.5, 2 * np.pi + 0.5, 200)
E_small = -np.cos(theta_small)
# Scale to fit in card
x_curve = 1.0 + theta_small / (2 * np.pi + 1.0) * 3.5
y_curve = 6.5 + E_small * 0.8

ax.plot(x_curve, y_curve, color=CYAN, linewidth=2.5, zorder=4)
ax.scatter([1.0 + 0.5 / (2 * np.pi + 1.0) * 3.5], [6.5 - 0.8],
           s=200, color=GOLD, edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(2.5, 5.3, 'E(\u03b8) = E\u2080 \u2212 \u03c7 cos(\u03b8)\nMinimum at \u03b8 = 0',
        fontsize=9, color=CYAN, ha='center')

# Right: the argument
ax.text(7.5, 8.0, 'THE ARGUMENT', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

argument_items = [
    ('Vacuum = minimum energy state', GREEN),
    ('E(\u03b8) minimized at \u03b8 = 0', GREEN),
    ('Therefore vacuum has \u03b8 = 0', GREEN),
    ('Same operation as Higgs v = 246 GeV', CYAN),
    ('No mechanism required', GOLD),
    ('No axion required', GOLD),
    ('No fine-tuning (gauge invariance)', GOLD),
]
for i, (item, color) in enumerate(argument_items):
    y = 7.2 - i * 0.55
    ax.text(6.0, y, '\u2022 %s' % item, fontsize=9, color=color)

# Key numbers
ax.text(2.5, 3.8, 'KEY NUMBERS', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
numbers = [
    ('\u03b8_QCD', '= 0', 'The ground state', GOLD),
    ('|\u03b8| bound', '< 5\u00d710\u207b\u00b9\u00b9', 'From neutron EDM', CYAN),
    ('\u03c0\u2083(SU(3))', '= \u2124', 'Integer topology', GREEN),
    ('\u03c7_top', '> 0', 'Lattice confirmed', BLUE),
]
for i, (name, value, note_text, color) in enumerate(numbers):
    y = 3.1 - i * 0.55
    ax.text(1.0, y, name, fontsize=10, color=color, fontweight='bold')
    ax.text(2.5, y, value, fontsize=10, color=WHITE, fontweight='bold')
    ax.text(3.5, y, note_text, fontsize=8, color=DIM)

# The double standard summary
ax.plot([0.5, 9.5], [1.3, 1.3], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5.0, 0.8, '\u03b1 = 1/137.036: no derivation, no problem declared.',
        fontsize=10, color=CYAN, ha='center')
ax.text(5.0, 0.3, '\u03b8 = 0: ground state, energy minimum, CP-protected, '
        '"problem" declared for 50 years.',
        fontsize=10, color=RED, ha='center')

save_fig(fig, 'phys7_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-7 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys7_01_energy_functional.png',
    'phys7_02_ground_state_parallel.png',
    'phys7_03_instanton_landscape.png',
    'phys7_04_rephasing_invariance.png',
    'phys7_05_theta_vacuum.png',
    'phys7_06_double_standard.png',
    'phys7_07_vacuum_identification.png',
    'phys7_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    