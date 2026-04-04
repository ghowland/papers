#!/usr/bin/env python3
"""
HOWL PHYS-11 Diagrams — Remainder Structure Across Nine Physics Domains
8 figures covering cosine instances, R=0 mechanisms, subgroup classification,
R2 universality, irreducibility proof.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: FOUR COSINE INSTANCES ON 8R2 DOMAIN
# Type: Running/comparison
# Shows: E(phi) = A - B*cos(phi) for theta vacuum, Brillouin zone,
# Bohr-Sommerfeld, and Aharonov-Bohm. All share the same shape,
# all minimized at phi=0. The shared shape IS the finding.
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12), facecolor=BG)

phi = np.linspace(-0.5, 2 * np.pi + 0.5, 300)

instances = [
    (axes[0, 0], 'Theta Vacuum', 'E(\u03b8) = E\u2080 \u2212 \u03c7cos(\u03b8)',
     '\u03b8', 'E(\u03b8)', CYAN, 1.0, 1.0),
    (axes[0, 1], 'Brillouin Zone', 'E(k) = \u22122t cos(ka)',
     'ka', 'E(k)', BLUE, 0.0, 2.0),
    (axes[1, 0], 'Bohr-Sommerfeld', 'V(\u03c6) = V\u2080(1 \u2212 cos\u03c6)',
     '\u03c6', 'V(\u03c6)', GREEN, 1.0, 1.0),
    (axes[1, 1], 'Aharonov-Bohm', '\u0394\u03c6 = 8R\u2082 \u00b7 \u03a6/\u03a6\u2080',
     '\u03a6/\u03a6\u2080 \u00d7 2\u03c0', 'cos(\u0394\u03c6)', ORANGE, 0.0, 1.0),
]

for ax, title, formula, xlabel, ylabel, color, offset, amplitude in instances:
    ax.set_facecolor(BG)
    E = offset - amplitude * np.cos(phi)
    ax.plot(phi, E, color=color, linewidth=2.5, zorder=4)

    # Ground state at phi = 0
    min_val = offset - amplitude
    ax.scatter([0], [min_val], s=300, color=GOLD, edgecolors=WHITE,
               linewidth=2, zorder=5)
    ax.text(0.3, min_val + 0.1, 'R = 0\n(ground state)', fontsize=9,
            color=GOLD, fontweight='bold')

    # Period markers
    ax.plot([0, 0], [min_val - 0.2, offset + amplitude + 0.2], color=DIM,
            linewidth=1, linestyle=':', alpha=0.4)
    ax.plot([2 * np.pi, 2 * np.pi], [min_val - 0.2, offset + amplitude + 0.2],
            color=DIM, linewidth=1, linestyle=':', alpha=0.4)

    ax.set_title(title, fontsize=13, color=color, fontweight='bold', pad=10)
    ax.text(np.pi, offset + amplitude + 0.3, formula, fontsize=10,
            color=SILVER, ha='center', fontfamily='monospace')

    ax.set_xlabel(xlabel, fontsize=10, color=SILVER)
    ax.set_ylabel(ylabel, fontsize=10, color=SILVER)
    ax.set_xlim(-0.5, 7.0)
    ax.tick_params(colors=DIM, labelsize=8)
    for spine in ax.spines.values():
        spine.set_color(PAN)

    # Period label
    ax.annotate('', xy=(2 * np.pi, min_val - 0.15), xytext=(0, min_val - 0.15),
                arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))
    ax.text(np.pi, min_val - 0.35, '8R\u2082', fontsize=10, color=GOLD,
            ha='center', fontweight='bold')

fig.suptitle('Four Cosines on an 8R\u2082-Periodic Domain: Same Shape, Same Minimum',
             fontsize=16, color=GOLD, fontweight='bold', y=0.98)
fig.tight_layout(rect=[0, 0.02, 1, 0.95])

path = os.path.join(get_outdir(), 'phys11_01_four_cosines.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys11_01_four_cosines.png")


# ================================================================
# FIG 2: TWO R=0 MECHANISMS
# Type: Dual-panel geometric
# Shows: Left: energy minimization (theta vacuum, dynamical).
# Right: topological single-valuedness (flux quantization).
# Same result R=0, different physics.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Dynamical: Energy Minimization",
    "Topological: Single-Valuedness",
    size=(18, 9), wspace=0.35)

# Left: E(theta) with minimum at 0
theta = np.linspace(-0.5, 2 * np.pi + 0.5, 300)
E = 1 - np.cos(theta)
curve(ax1, theta, E, 'E(\u03b8) = E\u2080 \u2212 \u03c7cos(\u03b8)', CYAN, 2.5)

data_point(ax1, 0, 0, '', GOLD, size=350)
ax1.scatter([0], [0], s=450, facecolors='none', edgecolors=GOLD,
            linewidth=2.5, zorder=11)

ax1.text(0.5, 0.3, 'R = 0\n\u03b8_QCD = 0\n(minimum energy)', fontsize=11,
         color=GOLD, fontweight='bold')
ax1.text(np.pi, 2.3, 'Mechanism:\nE(0) < E(\u03b8) for all \u03b8 \u2260 0\nVacuum selects lowest energy',
         fontsize=9, color=SILVER, ha='center')
ax1.text(np.pi, -0.5, 'PHYS-7 derivation', fontsize=9, color=GREEN,
         ha='center', fontweight='bold')

ax1.set_xlabel('\u03b8', color=SILVER, fontsize=11)
ax1.set_ylabel('E(\u03b8)', color=SILVER, fontsize=11)
ax1.set_xlim(-0.8, 7.0)
ax1.set_ylim(-0.8, 2.8)

# Right: wavefunction single-valuedness
# Show a ring with winding
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.set_xticks([])
ax2.set_yticks([])

ring = plt.Circle((0, 0), 1.2, fill=False, edgecolor=CYAN,
                    linewidth=2.5, zorder=3)
ax2.add_patch(ring)

# Phase arrows around the ring showing single-valuedness
n_arrows = 8
for i in range(n_arrows):
    angle = 2 * np.pi * i / n_arrows
    next_angle = 2 * np.pi * (i + 1) / n_arrows
    x1 = 1.2 * np.cos(angle)
    y1 = 1.2 * np.sin(angle)
    x2 = 1.2 * np.cos(next_angle)
    y2 = 1.2 * np.sin(next_angle)
    ax2.annotate('', xy=(x2, y2), xytext=(x1, y1),
                 arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5,
                                 connectionstyle='arc3,rad=0.3'))

# Start = end point (single-valued)
data_point(ax2, 1.2, 0, '', GOLD, size=350)
ax2.scatter([1.2], [0], s=450, facecolors='none', edgecolors=GOLD,
            linewidth=2.5, zorder=11)

ax2.text(1.5, 0.3, 'Start = End\n\u222b\u2207\u03b8\u00b7dl = 2\u03c0n', fontsize=10,
         color=GOLD, fontweight='bold')

ax2.text(0, 0, 'R = 0\n(exact)', fontsize=14, color=GOLD, ha='center',
         fontweight='bold')

ax2.text(0, -1.7, 'Mechanism:\n\u03c8 must be single-valued\n\u2192 phase = integer \u00d7 2\u03c0\n\u2192 remainder = 0 (topological)',
         fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys11_02_two_r0_mechanisms.png')


# ================================================================
# FIG 3: THETA-BZ CONNECTION — SAME EQUATION, DIFFERENT PHYSICS
# Type: Dual-panel
# Shows: E(theta) = E0 - chi*cos(theta) and E(k) = -2t*cos(ka)
# side by side. Same mathematics, different physics.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "QCD Vacuum: E(\u03b8) = E\u2080 \u2212 \u03c7cos(\u03b8)",
    "Crystal: E(k) = \u22122t cos(ka)",
    size=(18, 9), wspace=0.35)

phi = np.linspace(-0.5, 2 * np.pi + 0.5, 300)

# Left: theta vacuum
E_theta = 1 - np.cos(phi)
curve(ax1, phi, E_theta, '', CYAN, 2.5)
data_point(ax1, 0, 0, '', GOLD, size=300)

ax1.text(np.pi, 2.3, '\u03b8 = vacuum angle\n\u03c7 = topological susceptibility\n'
         'Period = 2\u03c0 = 8R\u2082', fontsize=10, color=SILVER, ha='center')
ax1.text(0.3, 0.2, 'Ground state\n\u03b8 = 0', fontsize=10, color=GOLD,
         fontweight='bold')

ax1.set_xlabel('\u03b8', color=SILVER, fontsize=12)
ax1.set_ylabel('Energy', color=SILVER, fontsize=12)
ax1.set_xlim(-0.8, 7.0)
ax1.set_ylim(-0.5, 2.8)

# Highlights: same period
ax1.annotate('', xy=(2 * np.pi, -0.3), xytext=(0, -0.3),
             arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax1.text(np.pi, -0.5, '8R\u2082', fontsize=12, color=GOLD,
         ha='center', fontweight='bold')

# Right: Brillouin zone
E_bz = -2 * np.cos(phi)
curve(ax2, phi, E_bz, '', BLUE, 2.5)
data_point(ax2, 0, -2, '', GOLD, size=300)

ax2.text(np.pi, 2.3, 'k = crystal momentum\nt = hopping parameter\n'
         'Period = 2\u03c0/a = 8R\u2082/a', fontsize=10, color=SILVER, ha='center')
ax2.text(0.3, -1.7, 'Band minimum\nk = 0', fontsize=10, color=GOLD,
         fontweight='bold')

ax2.set_xlabel('ka', color=SILVER, fontsize=12)
ax2.set_ylabel('Energy', color=SILVER, fontsize=12)
ax2.set_xlim(-0.8, 7.0)
ax2.set_ylim(-2.8, 2.8)

ax2.annotate('', xy=(2 * np.pi, -2.5), xytext=(0, -2.5),
             arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax2.text(np.pi, -2.7, '8R\u2082/a', fontsize=12, color=GOLD,
         ha='center', fontweight='bold')

save_fig(fig, 'phys11_03_theta_bz_connection.png')


# ================================================================
# FIG 4: R2 = PI/4 CIRCLE-IN-SQUARE RADIATING TO NINE DOMAINS
# Type: Geometric
# Shows: The circle inscribed in its bounding square (the definition
# of R2) at center, with lines radiating to all nine domain names.
# The single geometric fact underlying everything.
# ================================================================

fig, ax = dark_canvas("R\u2082 = \u03c0/4: The Universal Geometric Content",
                      size=(16, 16))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Central circle in square
sq = plt.Rectangle((-0.8, -0.8), 1.6, 1.6, fill=True, facecolor=BLUE,
                    alpha=0.10, edgecolor=BLUE, linewidth=2, zorder=2)
ax.add_patch(sq)
circ = plt.Circle((0, 0), 0.8, fill=True, facecolor=CYAN,
                    alpha=0.20, edgecolor=CYAN, linewidth=2.5, zorder=3)
ax.add_patch(circ)
ax.text(0, 0, 'R\u2082 = \u03c0/4\n\u2248 0.785', fontsize=12, color=GOLD,
        ha='center', va='center', fontweight='bold', zorder=4)

# Nine domains radiating outward
domains = [
    (0, '\u03b8 Vacuum', 'mod 8R\u2082', CYAN),
    (40, 'RG Running', 'step 1/(12R\u2082)', RED),
    (80, 'Bohr-Sommerfeld', 'mod 8R\u2082\u0127', GREEN),
    (120, 'Berry Phase', '\u03b3 = 4R\u2082(1\u2212cos\u03b8)', BLUE),
    (160, 'Brillouin Zone', 'G = 8R\u2082/a', PURPLE),
    (200, 'Chern-Simons', 'exp(i\u00b78R\u2082\u00b7k\u00b7CS)', ORANGE),
    (240, 'Aharonov-Bohm', '\u03b4\u03c6 = 8R\u2082\u03a6/\u03a6\u2080', MAG),
    (280, 'Flux Quant.', '\u222e\u2207\u03b8 = 8R\u2082n', SILVER),
    (320, 'AC Josephson', 'd\u03c6/dt = 8R\u2082f_J', DIM),
]

for angle_deg, name, role, color in domains:
    angle = np.radians(angle_deg)
    r_inner = 1.2
    r_outer = 2.8
    x_inner = r_inner * np.cos(angle)
    y_inner = r_inner * np.sin(angle)
    x_outer = r_outer * np.cos(angle)
    y_outer = r_outer * np.sin(angle)

    ax.plot([x_inner, x_outer], [y_inner, y_outer], color=color,
            linewidth=1.5, alpha=0.5, zorder=2)

    ax.text(x_outer * 1.15, y_outer * 1.15, name, fontsize=10, color=color,
            ha='center', va='center', fontweight='bold')
    ax.text(x_outer * 1.15, y_outer * 1.15 - 0.35, role, fontsize=7,
            color=SILVER, ha='center')

# Bottom label
ax.text(0, -3.7, '9 / 9 domains contain R\u2082 = \u03c0/4.\n'
        'Every factor of 2\u03c0 is 8R\u2082. Every factor of \u03c0 is 4R\u2082.\n'
        'The geometric remainder of circle-in-square is universal.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys11_04_r2_universal.png')


# ================================================================
# FIG 5: VP RUNNING AS MONOTONIC STAIRCASE — SUBGROUP B
# Type: Running/threshold
# Shows: alpha^-1(mu) accumulating logarithmically with discrete
# threshold jumps. The step size 1/(12R2) labeled. Non-periodic,
# contrasting with Subgroup A's cosine periodicity.
# ================================================================

fig, ax = dark_fig("Subgroup B: Monotonic Accumulation (Not Periodic)",
                   xlabel="Energy scale \u03bc (GeV, log scale)",
                   ylabel="\u03b1\u207b\u00b9(\u03bc) \u2212 \u03b1\u207b\u00b9(M_Z)")

# Schematic running from MZ downward
E = np.logspace(-3, 2, 500)

running = np.zeros_like(E)
for i, e in enumerate(E):
    if e > 91.19:
        running[i] = 0
    elif e > 1.777:
        running[i] = 0.8 * np.log(91.19 / e)
    elif e > 0.1057:
        running[i] = 0.8 * np.log(91.19 / 1.777) + 0.6 * np.log(1.777 / e)
    else:
        running[i] = 0.8 * np.log(91.19 / 1.777) + 0.6 * np.log(1.777 / 0.1057) + 0.4 * np.log(0.1057 / max(e, 0.001))

curve(ax, E, running, '\u03b1\u207b\u00b9 running (logarithmic, monotonic)', ORANGE, 2.5)

# Threshold markers
for mass, label, color in [(0.000511, 'm_e', CYAN), (0.1057, 'm_\u03bc', BLUE),
                            (1.777, 'm_\u03c4', ORANGE)]:
    ax.plot([mass, mass], [0, 12], color=color, linewidth=2,
            linestyle='--', alpha=0.5)
    ax.text(mass * 1.5, 11, label, fontsize=10, color=color, fontweight='bold')

# Step size annotation
ax.text(0.01, 4, 'Step size per flavor:\nQ\u00b2/(12R\u2082)\n= Q\u00b2/(3\u03c0)',
        fontsize=11, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Contrast with Subgroup A
result_box(ax, 30, 1.5,
           'NOT PERIODIC\nMonotonic accumulation.\nThresholds are unequal.\n'
           'No smooth bijection makes\nthis periodic (irreducibility\ntheorem, Fig 7).',
           RED, 9)

ax.set_xscale('log')
ax.set_xlim(0.0003, 200)
ax.set_ylim(0, 13)

save_fig(fig, 'phys11_05_monotonic_staircase.png')


# ================================================================
# FIG 6: THREE-SUBGROUP CLASSIFICATION
# Type: Geometric/comparison
# Shows: Three regions: A (7 domains, periodic cosine), B (1 domain,
# monotonic log), C (1 domain, topological mod Z). The grouping
# IS the classification.
# ================================================================

fig, ax = dark_canvas("Three Subgroups: The Irreducible Classification",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Subgroup A — largest, left-center
rect_a = plt.Rectangle((0.5, 3.5), 5.5, 5.5, facecolor=CYAN,
                         alpha=0.05, edgecolor=CYAN, linewidth=2.5, zorder=2)
ax.add_patch(rect_a)
ax.text(3.25, 8.5, 'SUBGROUP A: Phase-Periodic', fontsize=14, color=CYAN,
        ha='center', fontweight='bold')
ax.text(3.25, 7.8, '7 domains \u2014 cosine on 8R\u2082-periodic domain',
        fontsize=10, color=SILVER, ha='center')

# Small cosine curve inside A
phi_small = np.linspace(0, 2 * np.pi, 100)
x_cos = 1.5 + phi_small / (2 * np.pi) * 3.5
y_cos = 6.5 - 0.5 * np.cos(phi_small)
ax.plot(x_cos, y_cos, color=CYAN, linewidth=2, zorder=3)
ax.scatter([1.5], [6.0], s=100, color=GOLD, zorder=4)

a_domains = ['\u03b8 vacuum', 'Bohr-Sommerfeld', 'Berry phase',
             'Brillouin zone', 'Aharonov-Bohm', 'Flux quant.', 'AC Josephson']
for i, name in enumerate(a_domains):
    row = i // 4
    col = i % 4
    x = 1.0 + col * 1.3
    y = 5.0 - row * 0.6
    ax.text(x, y, name, fontsize=8, color=CYAN, fontweight='bold')

# Subgroup B — right, middle
rect_b = plt.Rectangle((6.5, 5.5), 3.0, 3.5, facecolor=ORANGE,
                         alpha=0.05, edgecolor=ORANGE, linewidth=2.5, zorder=2)
ax.add_patch(rect_b)
ax.text(8.0, 8.5, 'SUBGROUP B:\nMonotonic', fontsize=13, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(8.0, 7.5, '1 domain', fontsize=10, color=SILVER, ha='center')

# Small log curve inside B
x_log = np.linspace(7.0, 9.3, 50)
y_log = 6.5 + 0.3 * np.log(1 + (x_log - 7.0) * 3)
ax.plot(x_log, y_log, color=ORANGE, linewidth=2, zorder=3)

ax.text(8.0, 6.0, 'RG running', fontsize=9, color=ORANGE, ha='center',
        fontweight='bold')

# Subgroup C — right, bottom
rect_c = plt.Rectangle((6.5, 3.5), 3.0, 1.5, facecolor=MAG,
                         alpha=0.05, edgecolor=MAG, linewidth=2.5, zorder=2)
ax.add_patch(rect_c)
ax.text(8.0, 4.7, 'SUBGROUP C:\nTopological', fontsize=13, color=MAG,
        ha='center', fontweight='bold')
ax.text(8.0, 3.8, '1 domain: Chern-Simons\nmod \u2124 (modulus = 1)',
        fontsize=9, color=SILVER, ha='center')

# Key properties
properties = [
    (3.25, 2.5, 'A: Period = 8R\u2082 \u00d7 scale\nEnergy = \u2212cos(\u03c6)\nGround state at R = 0', CYAN),
    (6.5, 2.5, 'B: Step = 1/(12R\u2082)\nLogarithmic running\nNot periodic', ORANGE),
    (9.0, 2.5, 'C: mod \u2124 (pure integer)\nR\u2082 in exponential\nR\u2084 in normalization', MAG),
]

for x, y, text, color in properties:
    ax.text(x, y, text, fontsize=8, color=color, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8))

# Bottom
ax.text(5.0, 0.8, 'Classification is provably irreducible:\n'
        'no smooth bijection converts monotonic (B) into periodic (A).\n'
        'Three subgroups under smooth coordinate changes.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys11_06_three_subgroups.png')


# ================================================================
# FIG 7: IRREDUCIBILITY — MONOTONIC CANNOT BECOME PERIODIC
# Type: Dual-panel comparison
# Shows: A monotonic function (left) and a periodic function (right).
# No smooth bijection maps one to the other. The shapes are
# topologically incompatible.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Monotonic (Subgroup B)",
    "Periodic (Subgroup A)",
    size=(18, 9), wspace=0.35)

# Left: monotonic — VP running between thresholds
x_mono = np.linspace(0, 5, 200)
y_mono = 1.5 * np.log(1 + x_mono)
curve(ax1, x_mono, y_mono, 'f(x) = a + c\u00b7ln(1+x)', ORANGE, 2.5)

ax1.text(2.5, 3.0, 'MONOTONIC\n(always increasing)', fontsize=12,
         color=ORANGE, ha='center', fontweight='bold')
ax1.text(2.5, 0.5, 'Injective: f(x\u2081) \u2260 f(x\u2082)\nif x\u2081 \u2260 x\u2082',
         fontsize=10, color=SILVER, ha='center')

ax1.set_xlabel('x', color=SILVER, fontsize=11)
ax1.set_ylabel('f(x)', color=SILVER, fontsize=11)
ax1.set_xlim(-0.3, 5.5)
ax1.set_ylim(-0.5, 4.0)

# Right: periodic — cosine
x_per = np.linspace(0, 4 * np.pi, 200)
y_per = np.cos(x_per)
curve(ax2, x_per, y_per, 'g(x) = cos(x)', CYAN, 2.5)

ax2.text(2 * np.pi, 1.3, 'PERIODIC\ng(x) = g(x + 2\u03c0)', fontsize=12,
         color=CYAN, ha='center', fontweight='bold')
ax2.text(2 * np.pi, -1.5, 'NOT injective: g(0) = g(2\u03c0)\n\u2192 contradicts bijectivity',
         fontsize=10, color=RED, ha='center', fontweight='bold')

# Mark the period
for p in [0, 2 * np.pi, 4 * np.pi]:
    ax2.plot([p, p], [-1.2, 1.2], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

ax2.set_xlabel('x', color=SILVER, fontsize=11)
ax2.set_ylabel('g(x)', color=SILVER, fontsize=11)
ax2.set_xlim(-0.5, 13.0)
ax2.set_ylim(-1.8, 1.8)

# Central X
fig.text(0.5, 0.5, '\u2717', fontsize=50, color=RED, ha='center', va='center',
         fontweight='bold', transform=fig.transFigure)
fig.text(0.5, 0.42, 'No smooth bijection', fontsize=12, color=RED,
         ha='center', fontweight='bold', transform=fig.transFigure)

save_fig(fig, 'phys11_07_irreducibility.png')


# ================================================================
# FIG 8: PHYS-11 IDENTITY CARD
# Type: Identity card
# Shows: Nine domains, three subgroups, R2 universal, irreducibility,
# ground state principle. Visual anchor.
# ================================================================

fig, ax = dark_canvas("PHYS-11 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'NINE DOMAINS, THREE SUBGROUPS, ONE CONSTANT',
        fontsize=18, color=GOLD, ha='center', fontweight='bold')

# Left: the constant
ax.text(2.5, 7.8, 'R\u2082 = \u03c0/4', fontsize=24, color=GOLD,
        ha='center', fontweight='bold')
ax.text(2.5, 7.0, 'Present in 9/9 domains\n\n'
        'Period: 8R\u2082 \u00d7 scale\nStep: Q\u00b2/(12R\u2082)\n'
        'Normalization: 1/(256R\u2084)',
        fontsize=9, color=SILVER, ha='center')

# Circle in square (small)
sq = plt.Rectangle((1.8, 4.8), 1.4, 1.4, fill=True, facecolor=BLUE,
                    alpha=0.08, edgecolor=BLUE, linewidth=1.5, zorder=2)
ax.add_patch(sq)
circ = plt.Circle((2.5, 5.5), 0.7, fill=True, facecolor=CYAN,
                    alpha=0.15, edgecolor=CYAN, linewidth=2, zorder=3)
ax.add_patch(circ)

# Right: the classification
ax.text(7.5, 7.8, 'THREE SUBGROUPS', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

subgroups = [
    ('A: Phase-Periodic', '7 domains', 'Cosine on 8R\u2082', CYAN),
    ('B: Monotonic', '1 domain', 'Log staircase', ORANGE),
    ('C: Topological', '1 domain', 'mod \u2124', MAG),
]
for i, (name, count, desc, color) in enumerate(subgroups):
    y = 7.0 - i * 1.0
    ax.text(7.5, y, name, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(7.5, y - 0.4, '%s \u2014 %s' % (count, desc), fontsize=8,
            color=SILVER, ha='center')

# Key findings — bottom
ax.plot([0.5, 9.5], [3.5, 3.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

ax.text(5, 3.0, 'KEY FINDINGS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

findings = [
    ('R\u2082 universal', '9/9 domains', GREEN),
    ('Classification irreducible', 'Proven: monotonic \u2260 periodic', CYAN),
    ('Two R=0 mechanisms', 'Energy minimization + topological', GOLD),
    ('Two-level structure', 'Geometric (R\u2082) + domain-specific', BLUE),
    ('Ground state principle', 'min(\u2212cos) on 8R\u2082 \u2192 R = 0', ORANGE),
]
for i, (finding, detail, color) in enumerate(findings):
    y = 2.3 - i * 0.45
    ax.text(3.5, y, finding, fontsize=9, color=color, fontweight='bold')
    ax.text(7.0, y, detail, fontsize=8, color=DIM)

save_fig(fig, 'phys11_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-11 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys11_01_four_cosines.png',
    'phys11_02_two_r0_mechanisms.png',
    'phys11_03_theta_bz_connection.png',
    'phys11_04_r2_universal.png',
    'phys11_05_monotonic_staircase.png',
    'phys11_06_three_subgroups.png',
    'phys11_07_irreducibility.png',
    'phys11_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    