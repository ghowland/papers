#!/usr/bin/env python3
"""
HOWL PHYS-23 Diagrams — The Koide C3 Closure
8 figures covering saddle point, amplitude problem, Koide circle,
saddle vs minimum, three-sector comparison, K deviation, allowed range.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: THE SADDLE POINT — K IN TWO PERTURBATION DIRECTIONS
# Type: Running/surface
# Shows: K(epsilon) for stretch and compress modes. K rises in
# one direction, falls in the other. The saddle IS the argument.
# ================================================================

fig, ax = dark_fig("K = 2/3 Is a Saddle Point, Not a Minimum",
                   xlabel="Perturbation \u03b5 (radians)",
                   ylabel="Koide ratio K",
                   size=(16, 10))

# Compute K for perturbations from 120-degree configuration
# Base: phi1=0, phi2=2pi/3, phi3=4pi/3, with a=sqrt(2), M=1
eps_vals = np.linspace(-0.4, 0.4, 200)

# Parameters
a = np.sqrt(2.0)
M = 1.0

def koide_k(phi1, phi2, phi3, a_val, M_val):
    """Compute K from three phases."""
    sqrt_m = np.array([
        M_val * (1 + a_val * np.cos(phi1)),
        M_val * (1 + a_val * np.cos(phi2)),
        M_val * (1 + a_val * np.cos(phi3)),
    ])
    # Ensure positive
    sqrt_m = np.maximum(sqrt_m, 1e-10)
    masses = sqrt_m**2
    return np.sum(masses) / np.sum(sqrt_m)**2

# Stretch mode: phi1 -> eps, phi3 -> 4pi/3 - eps, phi2 fixed
K_stretch = []
for eps in eps_vals:
    k = koide_k(0 + eps, 2 * np.pi / 3, 4 * np.pi / 3 - eps, a, M)
    K_stretch.append(k)
K_stretch = np.array(K_stretch)

# Compress mode: phi2 -> 2pi/3 - eps, phi3 -> 4pi/3 + eps, phi1 fixed
K_compress = []
for eps in eps_vals:
    k = koide_k(0, 2 * np.pi / 3 - eps, 4 * np.pi / 3 + eps, a, M)
    K_compress.append(k)
K_compress = np.array(K_compress)

curve(ax, eps_vals, K_stretch, 'Stretch mode (\u03b4K > 0)', RED, 2.5)
curve(ax, eps_vals, K_compress, 'Compress mode (\u03b4K < 0)', BLUE, 2.5)

# K = 2/3 reference
ax.plot([-0.5, 0.5], [2.0 / 3, 2.0 / 3], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.6)
ax.text(0.35, 2.0 / 3 + 0.003, 'K = 2/3', fontsize=10, color=GOLD,
        fontweight='bold')

# Mark the saddle at epsilon = 0
data_point(ax, 0, 2.0 / 3, '', GOLD, size=300)

# Arrows showing opposite curvature
ax.annotate('K increases\n(stretch)', xy=(0.25, K_stretch[150]),
            xytext=(0.3, 0.72),
            fontsize=10, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.annotate('K decreases\n(compress)', xy=(0.25, K_compress[150]),
            xytext=(0.3, 0.62),
            fontsize=10, color=BLUE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5))

# The finding
result_box(ax, -0.2, 0.58,
           'SADDLE: K increases in one direction,\n'
           'decreases in another.\n'
           'K = 2/3 is NOT selected by C\u2083.\n'
           'A minimum would require K \u2265 2/3\n'
           'in ALL directions.',
           GOLD, 10)

legend(ax, loc='upper right')

ax.set_xlim(-0.45, 0.45)
ax.set_ylim(0.55, 0.78)

save_fig(fig, 'phys23_01_saddle_point.png')


# ================================================================
# FIG 2: THE REAL PROBLEM — AMPLITUDE ON THE CIRCLE
# Type: Geometric
# Shows: Three circles with different radii (a values) for the
# three sectors. The angular spacing is always 120 (tautology).
# The RADIUS is the question: why a = sqrt(2) for leptons?
# ================================================================

fig, ax = dark_canvas("The Real Problem: The Radius, Not the Spacing",
                      size=(18, 12))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')

# Three concentric circles for three sectors
sectors = [
    (np.sqrt(2.0), 'Leptons\na = \u221a2 = 1.414\na\u00b2 = 2.000', GOLD, 2.5),
    (1.545, 'Down quarks\na = 1.545\na\u00b2 = 2.388', ORANGE, 1.5),
    (1.759, 'Up quarks\na = 1.759\na\u00b2 = 3.093', RED, 0.8),
]

theta = np.linspace(0, 2 * np.pi, 200)

for a_val, label, color, alpha_scale in sectors:
    r = a_val  # Use amplitude as radius for visualization
    ax.plot(r * np.cos(theta), r * np.sin(theta), color=color,
            linewidth=2, alpha=0.4)

# Mark 120-degree points on each circle
for a_val, label, color, _ in sectors:
    for k in range(3):
        angle = 0.2222 + 2 * np.pi * k / 3  # theta_0 for leptons approx
        x = a_val * np.cos(angle)
        y = a_val * np.sin(angle)
        data_point(ax, x, y, '', color, size=150)

# Labels for circles (outside)
ax.text(1.5, 2.5, sectors[0][1], fontsize=10, color=GOLD,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))
ax.text(-2.8, -1.0, sectors[1][1], fontsize=10, color=ORANGE,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE))
ax.text(2.0, -2.5, sectors[2][1], fontsize=10, color=RED,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# 120-degree angle marks at center
for k in range(3):
    angle = 0.2222 + 2 * np.pi * k / 3
    ax.plot([0, 0.5 * np.cos(angle)], [0, 0.5 * np.sin(angle)],
            color=DIM, linewidth=1, alpha=0.5)
ax.text(0, 0, '120\u00b0', fontsize=9, color=DIM, ha='center')

# The key insight
ax.text(0, -3.0, 'The spacing is ALWAYS 120\u00b0 (tautology for any 3 masses).\n'
        'The RADIUS differs between sectors.\n'
        'Why is a = \u221a2 for leptons? THIS is the real problem.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

# Radius arrow
ax.annotate('a = \u221a2\n(why?)', xy=(1.0, 0.6), xytext=(2.5, 1.5),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

save_fig(fig, 'phys23_02_amplitude_problem.png')


# ================================================================
# FIG 3: THE KOIDE CIRCLE — LEPTON MASSES AT 120 DEGREES
# Type: Geometric (distinct — specific lepton data)
# Shows: sqrt(m_e), sqrt(m_mu), sqrt(m_tau) placed on a circle
# at 120-degree intervals. The parametrization IS the geometry.
# ================================================================

fig, ax = dark_canvas("The Koide Circle: Charged Leptons in \u221am Space",
                      size=(16, 14))
ax.set_xlim(-55, 55)
ax.set_ylim(-55, 55)
ax.set_aspect('equal')

# Lepton sqrt masses
sqrt_me = 0.71485  # sqrt(0.511)
sqrt_mmu = 10.279  # sqrt(105.66)
sqrt_mtau = 42.153  # sqrt(1776.86)
M = (sqrt_me + sqrt_mmu + sqrt_mtau) / 3  # = 17.716

# The circle has radius M*a where a = sqrt(2)
a = np.sqrt(2.0)
R = M * a  # ~ 25.05

# Draw the circle
theta = np.linspace(0, 2 * np.pi, 200)
ax.plot(R * np.cos(theta), R * np.sin(theta), color=DIM, linewidth=1.5,
        alpha=0.3)

# Center + mean line
data_point(ax, 0, 0, '', DIM, size=80)
ax.text(2, -3, 'Center\nM = 17.72', fontsize=8, color=DIM)

# Mean circle (radius M)
ax.plot(M * np.cos(theta), M * np.sin(theta), color=SILVER, linewidth=1,
        alpha=0.2, linestyle=':')

# Place three leptons at 120-degree intervals
# theta_0 = 0.2222 rad for charged leptons
theta_0 = 0.2222
lepton_data = [
    (0, sqrt_me, 'e\n\u221am = 0.71', MAG),
    (1, sqrt_mmu, '\u03bc\n\u221am = 10.28', CYAN),
    (2, sqrt_mtau, '\u03c4\n\u221am = 42.15', GOLD),
]

for k, sqrt_m, label, color in lepton_data:
    angle = theta_0 + 2 * np.pi * k / 3
    # Distance from center = M + M*a*cos(angle) ... but on the circle
    # Actually the point on circle at this angle
    x = R * np.cos(angle)
    y = R * np.sin(angle)
    data_point(ax, x, y, '', color, size=350)
    # Label offset
    lx = (R + 8) * np.cos(angle)
    ly = (R + 8) * np.sin(angle)
    ax.text(lx, ly, label, fontsize=11, color=color, ha='center',
            fontweight='bold')

# 120-degree arc marks
for k in range(3):
    angle1 = theta_0 + 2 * np.pi * k / 3
    angle2 = theta_0 + 2 * np.pi * (k + 1) / 3
    arc_theta = np.linspace(angle1, angle2, 50)
    arc_r = 12
    ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta),
            color=GREEN, linewidth=1.5, alpha=0.5)
    mid_angle = (angle1 + angle2) / 2
    ax.text(14 * np.cos(mid_angle), 14 * np.sin(mid_angle), '120\u00b0',
            fontsize=9, color=GREEN, ha='center')

# Formula
ax.text(0, -45, '\u221am_k = M(1 + a cos(\u03b8\u2080 + 2\u03c0k/3))\n'
        'M = 17.72    a = \u221a2    \u03b8\u2080 = 0.222\n'
        'K = (1 + a\u00b2/2)/3 = (1 + 1)/3 = 2/3',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys23_03_koide_circle.png')


# ================================================================
# FIG 4: SADDLE VS MINIMUM — SCHEMATIC COMPARISON
# Type: Dual-panel geometric
# Shows: Left = minimum (K increases in ALL directions from 2/3).
# Right = saddle (K increases in one, decreases in other).
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Minimum: K \u2265 2/3 in all directions",
    "Saddle: K rises AND falls from 2/3",
    size=(18, 9), wspace=0.35)

# Left: what a minimum would look like
eps = np.linspace(-0.4, 0.4, 100)
k_min_1 = 2.0 / 3 + 0.3 * eps**2  # Parabola up
k_min_2 = 2.0 / 3 + 0.15 * eps**2  # Shallower parabola up

curve(ax1, eps, k_min_1, 'Direction 1', CYAN, 2.5)
curve(ax1, eps, k_min_2, 'Direction 2', GREEN, 2.5)
ax1.plot([-0.5, 0.5], [2.0 / 3, 2.0 / 3], color=GOLD, linewidth=2,
         linestyle='--', alpha=0.5)
data_point(ax1, 0, 2.0 / 3, '', GOLD, size=300)
ax1.text(0, 0.59, 'K \u2265 2/3 always\n\u2192 2/3 is SELECTED', fontsize=11,
         color=GREEN, ha='center', fontweight='bold')
ax1.text(0, 0.55, '(This does NOT happen)', fontsize=10, color=RED,
         ha='center', fontweight='bold')
ax1.set_xlim(-0.45, 0.45)
ax1.set_ylim(0.52, 0.78)
ax1.set_xlabel('Perturbation \u03b5', fontsize=10, color=SILVER)
ax1.set_ylabel('K', fontsize=10, color=SILVER)

# Right: what actually happens (saddle)
K_str = 2.0 / 3 + 0.3 * eps**2
K_cmp = 2.0 / 3 - 0.15 * eps**2

curve(ax2, eps, K_str, 'Stretch (K rises)', RED, 2.5)
curve(ax2, eps, K_cmp, 'Compress (K falls)', BLUE, 2.5)
ax2.plot([-0.5, 0.5], [2.0 / 3, 2.0 / 3], color=GOLD, linewidth=2,
         linestyle='--', alpha=0.5)
data_point(ax2, 0, 2.0 / 3, '', GOLD, size=300)
ax2.text(0, 0.59, 'K rises AND falls\n\u2192 2/3 is NOT selected', fontsize=11,
         color=RED, ha='center', fontweight='bold')
ax2.text(0, 0.55, '(This IS what happens)', fontsize=10, color=GOLD,
         ha='center', fontweight='bold')
ax2.set_xlim(-0.45, 0.45)
ax2.set_ylim(0.52, 0.78)
ax2.set_xlabel('Perturbation \u03b5', fontsize=10, color=SILVER)

save_fig(fig, 'phys23_04_saddle_vs_minimum.png')


# ================================================================
# FIG 5: THREE-SECTOR A-SQUARED COMPARISON
# Type: Comparison bar
# Shows: a² = 2.000 (leptons), 2.388 (down), 3.093 (up).
# The target a² = 2 as a reference line. The ordering IS the constraint.
# ================================================================

fig, ax = dark_fig("Koide Amplitude a\u00b2 Across Three Sectors",
                   xlabel="",
                   ylabel="a\u00b2 = 2(3K \u2212 1)",
                   size=(16, 10))

sectors = [
    ('Charged\nLeptons\n(e, \u03bc, \u03c4)', 2.000, GOLD, 'K = 0.6667'),
    ('Down\nQuarks\n(d, s, b)', 2.388, ORANGE, 'K = 0.7313'),
    ('Up\nQuarks\n(u, c, t)', 3.093, RED, 'K = 0.8488'),
]

for i, (label, a2, color, k_val) in enumerate(sectors):
    ax.bar(i, a2, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    ax.text(i, a2 + 0.08, 'a\u00b2 = %.3f' % a2, fontsize=12, color=color,
            ha='center', fontweight='bold')
    ax.text(i, a2 - 0.15, k_val, fontsize=8, color=SILVER, ha='center')

ax.set_xticks(range(3))
ax.set_xticklabels([s[0] for s in sectors], fontsize=10, color=SILVER)

# a² = 2 reference line
ax.plot([-0.5, 2.5], [2.0, 2.0], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(2.3, 2.05, 'a\u00b2 = 2\n(K = 2/3)', fontsize=10, color=GOLD,
        fontweight='bold')

# Deviation labels
ax.text(0, 1.7, '\u0394 = 0.000', fontsize=9, color=GREEN, ha='center',
        fontweight='bold')
ax.text(1, 1.7, '\u0394 = +0.388\n(19%)', fontsize=9, color=ORANGE, ha='center',
        fontweight='bold')
ax.text(2, 1.7, '\u0394 = +1.093\n(55%)', fontsize=9, color=RED, ha='center',
        fontweight='bold')

result_box(ax, 1, 3.5,
           'Only charged leptons satisfy a\u00b2 = 2.\n'
           'Down quarks deviate by 19%.\n'
           'Up quarks deviate by 55%.\n'
           'Why this ordering? The open question.',
           GOLD, 10)

ax.set_xlim(-0.8, 3.0)
ax.set_ylim(1.5, 3.8)

save_fig(fig, 'phys23_05_three_sectors.png')


# ================================================================
# FIG 6: K DEVIATION FROM 2/3 — LEPTON BAR INVISIBLE
# Type: Comparison bar (distinct — deviation scale)
# Shows: K - 2/3 for each sector. Lepton bar is 6e-6 — invisible
# at the scale of the quark deviations (0.065, 0.182).
# ================================================================

fig, ax = dark_fig("K \u2212 2/3: The Lepton Deviation Is Invisible at Quark Scale",
                   xlabel="",
                   ylabel="K \u2212 2/3",
                   size=(16, 10))

deviations = [
    ('Charged\nLeptons', -6e-6, GOLD),
    ('Down\nQuarks', 0.065, ORANGE),
    ('Up\nQuarks', 0.182, RED),
]

for i, (label, dev, color) in enumerate(deviations):
    ax.bar(i, dev, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    if abs(dev) > 0.01:
        ax.text(i, dev + 0.008, '%+.3f' % dev, fontsize=14, color=color,
                ha='center', fontweight='bold')
    else:
        # Lepton bar is essentially invisible
        ax.text(i, 0.015, '\u22126 \u00d7 10\u207b\u2076\n(invisible\nat this scale)',
                fontsize=10, color=GOLD, ha='center', fontweight='bold')

ax.set_xticks(range(3))
ax.set_xticklabels([d[0] for d in deviations], fontsize=11, color=SILVER)

# Zero line
ax.plot([-0.5, 2.5], [0, 0], color=DIM, linewidth=1.5, alpha=0.5)

# The finding
result_box(ax, 1, -0.08,
           'The lepton Koide ratio deviates from 2/3\n'
           'by 6 parts per million \u2014 invisible here.\n'
           'Quarks miss by 10% and 27%.\n'
           'Six significant figures of precision for leptons.\n'
           'This IS the mystery.',
           GOLD, 10)

ax.set_xlim(-0.8, 3.0)
ax.set_ylim(-0.12, 0.22)

save_fig(fig, 'phys23_06_k_deviation.png')


# ================================================================
# FIG 7: THE ALLOWED RANGE — K FROM 1/3 TO 1
# Type: Scale/threshold
# Shows: Cauchy-Schwarz bounds 1/3 <= K < 1. K = 2/3 at midpoint.
# Three sectors marked on the scale.
# ================================================================

fig, ax = dark_fig("The Allowed Range: Where Each Sector Sits",
                   xlabel="Koide ratio K",
                   ylabel="",
                   size=(16, 8))

# Main axis
ax.plot([0.3, 1.05], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.4)

# Bounds
ax.plot([1.0 / 3, 1.0 / 3], [0.1, 0.9], color=DIM, linewidth=3)
ax.text(1.0 / 3, -0.3, 'K = 1/3\n(minimum:\nall masses equal)',
        fontsize=9, color=DIM, ha='center')

ax.plot([1.0, 1.0], [0.1, 0.9], color=DIM, linewidth=3)
ax.text(1.0, -0.3, 'K = 1\n(maximum:\none mass\ndominates)',
        fontsize=9, color=DIM, ha='center')

# Allowed region
ax.fill_between([1.0 / 3, 1.0], [0.2, 0.2], [0.8, 0.8],
                alpha=0.04, color=GREEN)

# Midpoint
ax.plot([2.0 / 3, 2.0 / 3], [0.15, 0.85], color=GOLD, linewidth=2.5,
        linestyle='--')
ax.text(2.0 / 3, 1.2, 'K = 2/3\n(midpoint)', fontsize=12, color=GOLD,
        ha='center', fontweight='bold')

# Three sectors
sector_marks = [
    (0.6667, 'Leptons\n0.6667', GOLD, -0.6),
    (0.7313, 'Down quarks\n0.7313', ORANGE, -0.6),
    (0.8488, 'Up quarks\n0.8488', RED, -0.6),
]

for k_val, label, color, y_off in sector_marks:
    ax.plot([k_val, k_val], [0.3, 0.7], color=color, linewidth=2.5)
    data_point(ax, k_val, 0.5, '', color, size=250)
    ax.text(k_val, y_off, label, fontsize=10, color=color,
            ha='center', fontweight='bold')

# a² = 2 equivalence
ax.text(2.0 / 3, -1.2, 'K = 2/3 \u21d4 a\u00b2 = 2\n'
        'Midpoint of the allowed range [1/3, 1).\n'
        'Leptons sit exactly here. Why?',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

ax.set_xlim(0.25, 1.1)
ax.set_ylim(-1.6, 1.6)
ax.set_yticks([])

save_fig(fig, 'phys23_07_allowed_range.png')


# ================================================================
# FIG 8: PHYS-23 IDENTITY CARD
# Type: Identity card
# Shows: Double kill (tautology + saddle), amplitude is the question.
# ================================================================

fig, ax = dark_canvas("PHYS-23 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE KOIDE C\u2083 CLOSURE', fontsize=20, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'The spacing is automatic. The potential is a saddle. '
        'The amplitude is the question.',
        fontsize=10, color=SILVER, ha='center', style='italic')

# The double kill
ax.text(5, 7.5, 'THE DOUBLE KILL', fontsize=14, color=RED,
        ha='center', fontweight='bold')

# Kill 1: Tautology
ax.text(2.5, 6.7, 'KILL 1: TAUTOLOGY', fontsize=12, color=CYAN,
        ha='center', fontweight='bold')
ax.text(2.5, 6.0, '3 parameters (M, a, \u03b8\u2080)\n3 data points (m_e, m_\u03bc, m_\u03c4)\n'
        '= 0 constraints.\n120\u00b0 spacing is AUTOMATIC\nfor ANY three positive masses.',
        fontsize=8, color=SILVER, ha='center')

# Kill 2: Saddle
ax.text(7.5, 6.7, 'KILL 2: SADDLE POINT', fontsize=12, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(7.5, 6.0, 'K = 2/3 at 120\u00b0 is a SADDLE:\nK rises in stretch mode,\n'
        'falls in compress mode.\nC\u2083 does NOT select a\u00b2 = 2.\n'
        'Not a minimum.',
        fontsize=8, color=SILVER, ha='center')

# The real problem
ax.plot([0.5, 9.5], [4.2, 4.2], color=DIM, linewidth=1, linestyle=':',
        alpha=0.4)
ax.text(5, 3.7, 'THE REAL PROBLEM', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')

ax.text(5, 2.8, 'Derive a\u00b2 = 2 from physics.', fontsize=14,
        color=WHITE, ha='center', fontweight='bold')

ax.text(5, 2.0, 'Requirements:\n'
        '\u2022 Produce a\u00b2 = 2 specifically (not "close to 2")\n'
        '\u2022 Explain why quarks deviate (a\u00b2_d = 2.39, a\u00b2_u = 3.09)\n'
        '\u2022 Not reduce to a reformulation of K = 2/3',
        fontsize=9, color=SILVER, ha='center')

# Bottom
ax.text(5, 0.5, 'K = 2/3 holds for charged leptons at 6 significant figures.\n'
        'The formula may be exact. The C\u2083 path to deriving it is dead.\n'
        'The conditional (18 \u2192 17 parameters if K = 2/3 exact) is maintained.',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys23_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-23 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys23_01_saddle_point.png',
    'phys23_02_amplitude_problem.png',
    'phys23_03_koide_circle.png',
    'phys23_04_saddle_vs_minimum.png',
    'phys23_05_three_sectors.png',
    'phys23_06_k_deviation.png',
    'phys23_07_allowed_range.png',
    'phys23_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    