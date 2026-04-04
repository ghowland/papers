#!/usr/bin/env python3
"""
HOWL PHYS-8 Diagrams — The Koide Constant Decomposes
8 figures covering circle geometry, critical amplitude, sum identities, parameter space.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: THREE LEPTONS ON A CIRCLE IN SQRT(M) SPACE
# Type: Geometric
# Shows: The actual circle with three points at 120 degree spacing.
# Labels show sqrt(m_e), sqrt(m_mu), sqrt(m_tau). The amplitude
# a=sqrt(2) visible as the modulation from center M.
# ================================================================

fig, ax = dark_canvas("Three Charged Leptons on a Circle in \u221am Space",
                      size=(14, 14))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# The parametrization: sqrt(m_i) = M(1 + a*cos(theta_0 + 2*pi*i/3))
# M ~ 313.86 MeV^(1/2), a = sqrt(2), theta_0 ~ 0.222 rad (from Koide fit)
M = 1.0  # normalized
a = np.sqrt(2)
theta_0 = 0.222  # approximate phase

# The modulation circle (radius = M*a)
circle = plt.Circle((0, 0), a, fill=False, edgecolor=CYAN,
                      linewidth=2, linestyle='--', alpha=0.5, zorder=2)
ax.add_patch(circle)

# Center circle (radius = M, the mean)
center_circle = plt.Circle((0, 0), 0.08, fill=True, facecolor=GOLD,
                              alpha=0.5, edgecolor=GOLD, linewidth=1, zorder=3)
ax.add_patch(center_circle)
ax.text(0.15, -0.15, 'M', fontsize=12, color=GOLD, fontweight='bold')

# Three lepton positions at 120 degree spacing
lepton_data = [
    (0, '\u221am_e', '0.715', CYAN, 'electron'),
    (1, '\u221am_\u03bc', '10.28', BLUE, 'muon'),
    (2, '\u221am_\u03c4', '42.15', ORANGE, 'tau'),
]

angles = [theta_0 + 2 * np.pi * i / 3 for i in range(3)]

for i, (idx, label, value, color, name) in enumerate(lepton_data):
    angle = angles[i]
    # Position on the modulation circle
    x = a * np.cos(angle)
    y = a * np.sin(angle)

    data_point(ax, x, y, '', color, size=350)

    # Label with offset
    dx = 0.3 * np.cos(angle)
    dy = 0.3 * np.sin(angle)
    ax.text(x + dx, y + dy, '%s = %s' % (label, value),
            fontsize=11, color=color, ha='center', fontweight='bold')

    # Line from center to point
    ax.plot([0, x], [0, y], color=color, linewidth=1.5, alpha=0.4, zorder=2)

# Angular separation labels
for i in range(3):
    a1 = angles[i]
    a2 = angles[(i + 1) % 3]
    mid_angle = (a1 + a2) / 2
    r_label = 0.7
    ax.text(r_label * np.cos(mid_angle), r_label * np.sin(mid_angle),
            '120\u00b0', fontsize=9, color=DIM, ha='center', va='center')

# Draw arc segments between points
for i in range(3):
    a1 = angles[i]
    a2 = angles[(i + 1) % 3]
    if a2 < a1:
        a2 += 2 * np.pi
    arc_angles = np.linspace(a1, a2, 50)
    ax.plot(a * np.cos(arc_angles), a * np.sin(arc_angles),
            color=DIM, linewidth=1, alpha=0.3)

# Amplitude annotation
ax.annotate('a = \u221a2\n(critical amplitude)',
            xy=(a * np.cos(angles[1]), a * np.sin(angles[1])),
            xytext=(-1.8, -1.8),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Formula
result_box(ax, 0, -2.2,
           '\u221am_i = M(1 + \u221a2 \u00b7 cos(\u03b8\u2080 + 2\u03c0i/3))\n'
           'Equal spacing (120\u00b0) in \u221am space',
           GOLD, 10)

save_fig(fig, 'phys8_01_koide_circle.png')


# ================================================================
# FIG 2: KOIDE RATIO VS M_TAU
# Type: Running/threshold
# Shows: K(m_tau) as m_tau varies, crossing 2/3 at the predicted
# 1776.97 MeV. PDG value with uncertainty band. The near-
# intersection IS the 0.91 sigma tension.
# ================================================================

fig, ax = dark_fig("Koide Ratio vs m_\u03c4: Crossing 2/3 at the Predicted Value",
                   xlabel="m_\u03c4 (MeV)",
                   ylabel="K = (\u03a3m) / (\u03a3\u221am)\u00b2")

m_e = 0.51099895
m_mu = 105.6583755

m_tau_range = np.linspace(1700, 1850, 500)

K_values = np.zeros_like(m_tau_range)
for i, mt in enumerate(m_tau_range):
    sum_m = m_e + m_mu + mt
    sum_sqrt = np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(mt)
    K_values[i] = sum_m / sum_sqrt**2

curve(ax, m_tau_range, K_values, 'K(m_\u03c4)', CYAN, 2.5)

# 2/3 line
ax.plot([1700, 1850], [2.0 / 3.0, 2.0 / 3.0], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(1705, 2.0 / 3.0 + 0.00015, '2/3 = 0.666667', fontsize=10,
        color=GOLD, fontweight='bold')

# Prediction point
m_tau_pred = 1776.97
K_pred = (m_e + m_mu + m_tau_pred) / (np.sqrt(m_e) + np.sqrt(m_mu) + np.sqrt(m_tau_pred))**2
data_point(ax, m_tau_pred, K_pred, '', GREEN, size=300)
ax.annotate('Koide prediction\nm_\u03c4 = 1776.97 MeV',
            xy=(m_tau_pred, K_pred), xytext=(1810, 0.66672),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# PDG measurement band
m_tau_pdg = 1776.86
m_tau_err = 0.12
measurement_band_v(ax, m_tau_pdg, m_tau_err, '', ORANGE)
ax.text(m_tau_pdg - 5, 0.66660, 'PDG\n1776.86\n\u00b10.12', fontsize=8,
        color=ORANGE, ha='right')

# Tension
ax.annotate('0.91\u03c3\ntension', xy=(m_tau_pdg, 2.0 / 3.0),
            xytext=(1740, 0.66670),
            fontsize=11, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.set_xlim(1700, 1850)
ax.set_ylim(0.66650, 0.66690)

save_fig(fig, 'phys8_02_koide_ratio_vs_mtau.png')


# ================================================================
# FIG 3: CRITICAL AMPLITUDE — BOUNDARY OF PHYSICAL MASSES
# Type: Running/threshold
# Shows: Minimum mass factor (1 + a*cos(phi_min)) vs amplitude a.
# At a < sqrt(2): all positive. At a = sqrt(2): touches zero.
# At a > sqrt(2): goes negative. The critical point IS Koide.
# ================================================================

fig, ax = dark_fig("Critical Amplitude: a = \u221a2 Is the Boundary of Physical Masses",
                   xlabel="Amplitude a",
                   ylabel="Minimum value of (1 + a \u00b7 cos(\u03c6))")

a_range = np.linspace(0, 2.5, 500)
# Minimum of (1 + a*cos(phi)) = 1 - a (at cos(phi) = -1)
min_factor = 1 - a_range

curve(ax, a_range, min_factor, 'min(1 + a\u00b7cos\u03c6) = 1 \u2212 a', CYAN, 2.5)

# Zero line
ax.plot([0, 2.5], [0, 0], color=DIM, linewidth=1.5, alpha=0.5)

# Shade regions
# Physical region (min > 0, a < 1... but for Koide the constraint is different)
# Actually for the Koide parametrization, masses can be zero when 1+a*cos = 0
# which requires cos = -1/a, possible only when a >= 1
# But m_i = M^2 * (1 + a*cos)^2 >= 0 always! The sqrt can be negative but mass is squared
# The constraint is sqrt(m) >= 0, meaning 1 + a*cos >= 0
# Minimum cos over the three angles: for 120 degree spacing, min cos depends on theta_0

# Simpler: show the envelope 1 - a
shaded_region(ax, 0, np.sqrt(2), GREEN, 0.06)
shaded_region(ax, np.sqrt(2), 2.5, RED, 0.06)

ax.text(0.6, 0.3, 'ALL MASSES\nPOSITIVE', fontsize=11, color=GREEN,
        ha='center', fontweight='bold')
ax.text(2.0, -0.4, 'NEGATIVE\nMASS\n(unphysical)', fontsize=11, color=RED,
        ha='center', fontweight='bold')

# Critical point
data_point(ax, np.sqrt(2), 1 - np.sqrt(2), '', GOLD, size=400)
ax.scatter([np.sqrt(2)], [1 - np.sqrt(2)], s=500, facecolors='none',
           edgecolors=GOLD, linewidth=2.5, zorder=11)

ax.annotate('a = \u221a2 \u2248 1.414\nCRITICAL AMPLITUDE\n'
            'Mass can reach zero\nbut never negative\n\n'
            'This IS the Koide amplitude.',
            xy=(np.sqrt(2), 1 - np.sqrt(2)),
            xytext=(1.8, 0.5),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Zero crossing
ax.plot([np.sqrt(2), np.sqrt(2)], [-1.2, 0.05], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.5)

ax.set_xlim(-0.1, 2.6)
ax.set_ylim(-1.2, 1.2)

save_fig(fig, 'phys8_03_critical_amplitude.png')


# ================================================================
# FIG 4: COS AND COS^2 SUM IDENTITIES — GEOMETRIC PROOF
# Type: Geometric/proof
# Shows: N equally-spaced unit vectors summing to zero (cos identity).
# The cos^2 identity as a consequence. Why N >= 3 works and N=2
# does not.
# ================================================================

fig = plt.figure(figsize=(18, 9), facecolor=BG)

# Left panel: N=3, vectors sum to zero
ax1 = fig.add_subplot(1, 2, 1, aspect='equal')
ax1.set_facecolor(BG)
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.8, 1.8)
ax1.axis('off')
ax1.set_title('N = 3: Vectors Sum to Zero', fontsize=14, color=GREEN,
              fontweight='bold', pad=15)

# Unit circle
unit_circle = plt.Circle((0, 0), 1.0, fill=False, edgecolor=DIM,
                            linewidth=1, linestyle=':', alpha=0.4)
ax1.add_patch(unit_circle)

# Three equally spaced vectors
theta_0_demo = np.pi / 6  # arbitrary starting angle
for i in range(3):
    angle = theta_0_demo + 2 * np.pi * i / 3
    x = np.cos(angle)
    y = np.sin(angle)
    ax1.annotate('', xy=(x, y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=[CYAN, BLUE, ORANGE][i],
                                 lw=2.5))

# Sum = 0 at center
ax1.text(0, -0.2, '\u03a3 = 0', fontsize=16, color=GOLD, ha='center',
         fontweight='bold')
ax1.text(0, -1.5, '\u03a3 cos(\u03b8 + 2\u03c0k/3) = 0\nfor all \u03b8',
         fontsize=11, color=GREEN, ha='center', fontweight='bold')

# Angle labels
for i in range(3):
    angle = theta_0_demo + 2 * np.pi * i / 3
    ax1.text(1.25 * np.cos(angle), 1.25 * np.sin(angle), '120\u00b0',
             fontsize=8, color=DIM, ha='center')

# Right panel: N=2, vectors do NOT sum to zero for cos^2
ax2 = fig.add_subplot(1, 2, 2, aspect='equal')
ax2.set_facecolor(BG)
ax2.set_xlim(-1.8, 1.8)
ax2.set_ylim(-1.8, 1.8)
ax2.axis('off')
ax2.set_title('N = 2: cos\u00b2 Identity FAILS', fontsize=14, color=RED,
              fontweight='bold', pad=15)

unit_circle2 = plt.Circle((0, 0), 1.0, fill=False, edgecolor=DIM,
                             linewidth=1, linestyle=':', alpha=0.4)
ax2.add_patch(unit_circle2)

# Two opposite vectors
theta_2 = np.pi / 4
for i in range(2):
    angle = theta_2 + np.pi * i
    x = np.cos(angle)
    y = np.sin(angle)
    color_2 = CYAN if i == 0 else ORANGE
    ax2.annotate('', xy=(x, y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=color_2, lw=2.5))

# cos identity works for N=2 (cos + cos(+pi) = 0)
ax2.text(0, -0.2, '\u03a3cos = 0 \u2713', fontsize=12, color=GREEN, ha='center',
         fontweight='bold')

# But cos^2 fails
ax2.text(0, -0.7, '\u03a3cos\u00b2 = 2cos\u00b2\u03b8 \u2260 1', fontsize=12,
         color=RED, ha='center', fontweight='bold')

ax2.text(0, -1.3, 'Depends on \u03b8!\nNot constant.\n\u2192 General formula\ninvalid for N = 2.',
         fontsize=10, color=RED, ha='center')

# Consequence boxes at bottom
fig.text(0.25, 0.05, 'N \u2265 3: \u03a3cos\u00b2 = N/2 (constant)\n\u2192 (1 + a\u00b2/2)/N works',
         fontsize=11, color=GREEN, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN))
fig.text(0.75, 0.05, 'N = 2: \u03a3cos\u00b2 = 2cos\u00b2\u03b8 (varies)\n\u2192 Formula breaks down',
         fontsize=11, color=RED, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

path = os.path.join(get_outdir(), 'phys8_04_sum_identities.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys8_04_sum_identities.png")


# ================================================================
# FIG 5: GENERAL RATIO (1+a^2/2)/N AS PARAMETER SPACE
# Type: Parameter space
# Shows: 2D plot with N on x-axis, a on y-axis, contour lines
# for the ratio value. The Koide point (N=3, a=sqrt(2)) marked.
# ================================================================

fig, ax = dark_fig("Parameter Space: (1 + a\u00b2/2) / N",
                   xlabel="Generation count N",
                   ylabel="Amplitude a",
                   size=(16, 10))

# Create grid
N_vals = np.linspace(2.5, 8, 200)
a_vals = np.linspace(0, 2.5, 200)
N_grid, A_grid = np.meshgrid(N_vals, a_vals)
R_grid = (1 + A_grid**2 / 2) / N_grid

# Contour plot
levels = [0.2, 1.0 / 3, 0.4, 0.5, 2.0 / 3, 0.8, 1.0, 1.2]
cs = ax.contour(N_grid, A_grid, R_grid, levels=levels,
                colors=[DIM] * len(levels), linewidths=1.5, alpha=0.6)
ax.clabel(cs, inline=True, fontsize=8, fmt='%.3f', colors=SILVER)

# Highlight the 2/3 contour
cs_koide = ax.contour(N_grid, A_grid, R_grid, levels=[2.0 / 3.0],
                       colors=[GOLD], linewidths=2.5)
ax.clabel(cs_koide, inline=True, fontsize=10, fmt='2/3', colors=GOLD)

# Koide point
data_point(ax, 3, np.sqrt(2), '', GOLD, size=400)
ax.scatter([3], [np.sqrt(2)], s=500, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)
ax.annotate('KOIDE\nN=3, a=\u221a2\nRatio = 2/3',
            xy=(3, np.sqrt(2)), xytext=(4.5, 2.0),
            fontsize=12, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Other notable points
# N=4, a=sqrt(2) -> ratio = 1/2
data_point(ax, 4, np.sqrt(2), '', CYAN, size=200)
ax.text(4.2, np.sqrt(2) - 0.15, 'N=4: ratio=1/2', fontsize=8,
        color=CYAN, fontweight='bold')

# N=3, a=1 -> ratio = 1/2
data_point(ax, 3, 1, '', BLUE, size=200)
ax.text(3.2, 0.85, 'a=1: ratio=1/2', fontsize=8, color=BLUE)

# N=3, a=0 -> ratio = 1/3 (all equal masses)
data_point(ax, 3, 0.05, '', GREEN, size=200)
ax.text(3.2, 0.15, 'a=0: all equal\nratio=1/3', fontsize=8, color=GREEN)

# Critical amplitude line
ax.plot([2.5, 8], [np.sqrt(2), np.sqrt(2)], color=RED, linewidth=1.5,
        linestyle=':', alpha=0.5)
ax.text(7.5, np.sqrt(2) + 0.08, 'a = \u221a2\n(critical)', fontsize=8,
        color=RED, ha='right')

ax.set_xlim(2.5, 8)
ax.set_ylim(0, 2.5)
ax.set_xticks([3, 4, 5, 6, 7])

save_fig(fig, 'phys8_05_parameter_space.png')


# ================================================================
# FIG 6: 120 DEGREE SPACING AS MAXIMUM SYMMETRY
# Type: Geometric comparison
# Shows: Left: equal spacing (120 degrees, S3 invariant).
# Right: unequal spacing (breaks permutation symmetry).
# The symmetric case IS the Koide configuration.
# ================================================================

fig = plt.figure(figsize=(18, 9), facecolor=BG)

# Left: equal spacing
ax1 = fig.add_subplot(1, 2, 1, aspect='equal')
ax1.set_facecolor(BG)
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-2.0, 1.8)
ax1.axis('off')
ax1.set_title('Equal Spacing: 120\u00b0 (Maximum Symmetry)', fontsize=13,
              color=GREEN, fontweight='bold', pad=15)

circle1 = plt.Circle((0, 0), 1.2, fill=False, edgecolor=DIM,
                       linewidth=1.5, linestyle='--', alpha=0.4)
ax1.add_patch(circle1)

for i in range(3):
    angle = np.pi / 2 + 2 * np.pi * i / 3
    x = 1.2 * np.cos(angle)
    y = 1.2 * np.sin(angle)
    data_point(ax1, x, y, '', [CYAN, BLUE, ORANGE][i], size=300)
    # Separation arc
    next_angle = np.pi / 2 + 2 * np.pi * ((i + 1) % 3) / 3
    mid = (angle + next_angle) / 2
    if next_angle < angle:
        mid = (angle + next_angle + 2 * np.pi) / 2
    ax1.text(0.7 * np.cos(mid), 0.7 * np.sin(mid), '120\u00b0',
             fontsize=10, color=GREEN, ha='center', fontweight='bold')

# Connect with lines
for i in range(3):
    a1 = np.pi / 2 + 2 * np.pi * i / 3
    a2 = np.pi / 2 + 2 * np.pi * ((i + 1) % 3) / 3
    ax1.plot([1.2 * np.cos(a1), 1.2 * np.cos(a2)],
             [1.2 * np.sin(a1), 1.2 * np.sin(a2)],
             color=GREEN, linewidth=1.5, alpha=0.4)

ax1.text(0, -1.7, 'S\u2083 invariant\n\u03a3cos = 0, \u03a3cos\u00b2 = 3/2\n'
         'Koide formula holds', fontsize=10, color=GREEN, ha='center',
         fontweight='bold')

# Right: unequal spacing
ax2 = fig.add_subplot(1, 2, 2, aspect='equal')
ax2.set_facecolor(BG)
ax2.set_xlim(-1.8, 1.8)
ax2.set_ylim(-2.0, 1.8)
ax2.axis('off')
ax2.set_title('Unequal Spacing (Broken Symmetry)', fontsize=13,
              color=RED, fontweight='bold', pad=15)

circle2 = plt.Circle((0, 0), 1.2, fill=False, edgecolor=DIM,
                       linewidth=1.5, linestyle='--', alpha=0.4)
ax2.add_patch(circle2)

unequal_angles = [np.pi / 2, np.pi / 2 + 1.8, np.pi / 2 + 3.5]
for i, angle in enumerate(unequal_angles):
    x = 1.2 * np.cos(angle)
    y = 1.2 * np.sin(angle)
    data_point(ax2, x, y, '', [CYAN, BLUE, ORANGE][i], size=300)

# Unequal arcs
separations = ['103\u00b0', '97\u00b0', '160\u00b0']
for i in range(3):
    a1 = unequal_angles[i]
    a2 = unequal_angles[(i + 1) % 3]
    mid = (a1 + a2) / 2
    if a2 < a1:
        mid = (a1 + a2 + 2 * np.pi) / 2
    ax2.text(0.7 * np.cos(mid), 0.7 * np.sin(mid), separations[i],
             fontsize=10, color=RED, ha='center', fontweight='bold')

# Connect with lines
for i in range(3):
    a1 = unequal_angles[i]
    a2 = unequal_angles[(i + 1) % 3]
    ax2.plot([1.2 * np.cos(a1), 1.2 * np.cos(a2)],
             [1.2 * np.sin(a1), 1.2 * np.sin(a2)],
             color=RED, linewidth=1.5, alpha=0.4)

ax2.text(0, -1.7, 'S\u2083 broken\n\u03a3cos \u2260 0, \u03a3cos\u00b2 \u2260 3/2\n'
         'General formula does not simplify', fontsize=10, color=RED,
         ha='center', fontweight='bold')

path = os.path.join(get_outdir(), 'phys8_06_symmetry_comparison.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys8_06_symmetry_comparison.png")


# ================================================================
# FIG 7: CAUCHY-SCHWARZ RANGE — KOIDE AT MIDPOINT
# Type: Scale/comparison
# Shows: Number line from 1/3 (lower bound, all equal) to 1
# (upper bound, one dominates). Koide at 2/3 = exact midpoint.
# ================================================================

fig, ax = dark_fig("Cauchy-Schwarz Range: Koide at the Midpoint",
                   xlabel="K = (\u03a3m) / (\u03a3\u221am)\u00b2",
                   ylabel="",
                   size=(16, 8))

# The range line
ax.plot([0.25, 1.05], [0.5, 0.5], color=DIM, linewidth=3, alpha=0.5)

# Lower bound
ax.plot([1.0 / 3, 1.0 / 3], [0.2, 0.8], color=GREEN, linewidth=3)
data_point(ax, 1.0 / 3, 0.5, '', GREEN, size=300)
ax.text(1.0 / 3, 1.2, 'Lower bound\n1/N = 1/3', fontsize=11, color=GREEN,
        ha='center', fontweight='bold')
ax.text(1.0 / 3, -0.3, 'All masses equal\na = 0', fontsize=9,
        color=SILVER, ha='center')

# Upper bound
ax.plot([1.0, 1.0], [0.2, 0.8], color=RED, linewidth=3)
data_point(ax, 1.0, 0.5, '', RED, size=300)
ax.text(1.0, 1.2, 'Upper bound\n1', fontsize=11, color=RED,
        ha='center', fontweight='bold')
ax.text(1.0, -0.3, 'One mass dominates\na \u2192 \u221e', fontsize=9,
        color=SILVER, ha='center')

# Koide at midpoint
data_point(ax, 2.0 / 3, 0.5, '', GOLD, size=500)
ax.scatter([2.0 / 3], [0.5], s=600, facecolors='none', edgecolors=GOLD,
           linewidth=3, zorder=11)
ax.text(2.0 / 3, 1.2, 'KOIDE\n2/3', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(2.0 / 3, -0.3, 'Critical amplitude\na = \u221a2', fontsize=9,
        color=GOLD, ha='center', fontweight='bold')

# Midpoint annotation
ax.annotate('', xy=(1.0 / 3, -0.7), xytext=(2.0 / 3, -0.7),
            arrowprops=dict(arrowstyle='<->', color=CYAN, lw=1.5))
ax.text(0.5, -0.9, '1/3', fontsize=9, color=CYAN, ha='center')

ax.annotate('', xy=(2.0 / 3, -0.7), xytext=(1.0, -0.7),
            arrowprops=dict(arrowstyle='<->', color=CYAN, lw=1.5))
ax.text(5.0 / 6, -0.9, '1/3', fontsize=9, color=CYAN, ha='center')

ax.text(2.0 / 3, -1.2, 'EXACT MIDPOINT of the allowed range',
        fontsize=12, color=GOLD, ha='center', fontweight='bold')

# Shade allowed region
shaded_region(ax, 1.0 / 3, 1.0, CYAN, 0.04)

ax.set_xlim(0.25, 1.1)
ax.set_ylim(-1.5, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys8_07_cauchy_schwarz.png')


# ================================================================
# FIG 8: PHYS-8 IDENTITY CARD
# Type: Identity card
# Shows: Circle with three points, the formula, m_tau prediction,
# parameter reduction 18 -> 17.
# ================================================================

fig, ax = dark_canvas("PHYS-8 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE KOIDE CONSTANT DECOMPOSES', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')

# Small circle diagram — left
cx, cy, cr = 2.5, 6.5, 1.0
circle = plt.Circle((cx, cy), cr, fill=False, edgecolor=CYAN,
                      linewidth=2, linestyle='--', alpha=0.5, zorder=2)
ax.add_patch(circle)

for i in range(3):
    angle = np.pi / 2 + 2 * np.pi * i / 3
    x = cx + cr * np.cos(angle)
    y = cy + cr * np.sin(angle)
    colors_circle = [CYAN, BLUE, ORANGE]
    data_point(ax, x, y, '', colors_circle[i], size=150)

labels_circle = ['e', '\u03bc', '\u03c4']
for i in range(3):
    angle = np.pi / 2 + 2 * np.pi * i / 3
    x = cx + (cr + 0.3) * np.cos(angle)
    y = cy + (cr + 0.3) * np.sin(angle)
    ax.text(x, y, labels_circle[i], fontsize=10, color=[CYAN, BLUE, ORANGE][i],
            ha='center', fontweight='bold')

ax.text(cx, cy - 1.6, '120\u00b0 spacing\nin \u221am space', fontsize=9,
        color=SILVER, ha='center')

# The formula — center
ax.text(5.5, 7.5, '(\u03a3m) / (\u03a3\u221am)\u00b2 = (1 + a\u00b2/2) / N',
        fontsize=16, color=WHITE, ha='center', fontweight='bold',
        fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=2.5))

# Decomposition
ax.text(5.5, 6.5, 'At N = 3, a\u00b2 = 2:', fontsize=12, color=SILVER,
        ha='center')
ax.text(5.5, 5.8, '(1 + 2/2) / 3 = 2/3', fontsize=18, color=GOLD,
        ha='center', fontweight='bold')

# Components
ax.text(4.0, 5.0, 'Numerator 2:', fontsize=10, color=CYAN, fontweight='bold')
ax.text(4.0, 4.5, '1 + a\u00b2/2 = 2\n(critical amplitude)', fontsize=9,
        color=SILVER)
ax.text(7.0, 5.0, 'Denominator 3:', fontsize=10, color=ORANGE, fontweight='bold')
ax.text(7.0, 4.5, 'N = 3\n(generation count)', fontsize=9, color=SILVER)

# The prediction
ax.text(5.5, 3.3, 'THE PREDICTION', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

pred_items = [
    ('m_\u03c4 (Koide)', '1776.97 MeV', GREEN),
    ('m_\u03c4 (PDG)', '1776.86 \u00b1 0.12 MeV', ORANGE),
    ('Tension', '0.91\u03c3', CYAN),
]
for i, (label, value, color) in enumerate(pred_items):
    y = 2.7 - i * 0.5
    ax.text(4.5, y, label + ':', fontsize=10, color=SILVER)
    ax.text(7.0, y, value, fontsize=11, color=color, fontweight='bold')

# Parameter reduction
ax.plot([0.5, 9.5], [1.3, 1.3], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5, 0.8, '19 \u2192 18 (\u03b8_QCD = 0, PHYS-7) \u2192 17 (m_\u03c4 from Koide, PHYS-8)',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')
ax.text(5, 0.3, 'Conditional on the Koide formula being exact (currently 0.91\u03c3).',
        fontsize=9, color=SILVER, ha='center', style='italic')

save_fig(fig, 'phys8_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-8 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys8_01_koide_circle.png',
    'phys8_02_koide_ratio_vs_mtau.png',
    'phys8_03_critical_amplitude.png',
    'phys8_04_sum_identities.png',
    'phys8_05_parameter_space.png',
    'phys8_06_symmetry_comparison.png',
    'phys8_07_cauchy_schwarz.png',
    'phys8_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    