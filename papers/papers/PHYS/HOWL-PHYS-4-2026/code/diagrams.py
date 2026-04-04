#!/usr/bin/env python3
"""
HOWL PHYS-4 Diagrams — The Boundary Test Program
8 figures covering boundary classification, test program, probe depths, per-transit problem.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: BOUNDARY GEOMETRY GALLERY
# Type: Geometric progression
# Shows: Six geometric boundaries drawn as their actual shapes,
# plus confinement marked as excluded. The classification is
# visual — you SEE which are spheres, which are ellipses.
# ================================================================

fig = plt.figure(figsize=(18, 12), facecolor=BG)

boundaries = [
    ('Earth\nHill Sphere', 'Sphere', 'r \u2248 1.5M km', GREEN, 'geometric', 'Test 1,2,4'),
    ('Electron\nVacuum Cloud', 'Sphere', 'r \u2248 \u03bb_C', CYAN, 'geometric', 'Test 0'),
    ('Proton\nScattering', 'Circle\n(cross-section)', 'r \u2248 0.84 fm', BLUE, 'geometric', 'Test 3'),
    ('Galaxy', 'Oblate\nEllipsoid', 'r \u2248 50 kpc', PURPLE, 'geometric', 'Test 6'),
    ('CMB / Observable\nUniverse', 'Sphere', 'r \u2248 46 Gly', ORANGE, 'geometric', 'Test 5'),
    ('Solar System\nHill Sphere', 'Sphere', 'r \u2248 1-2 ly', BLUE, 'geometric', 'Test 7'),
    ('Hadron\nConfinement', 'Momentum\nspace scale', 'NOT spatial', RED, 'excluded', 'EXCLUDED'),
]

for idx in range(7):
    row = idx // 4
    col = idx % 4
    ax = fig.add_subplot(2, 4, idx + 1, aspect='equal')
    ax.set_facecolor(BG)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')

    name, shape_label, scale, color, status, test = boundaries[idx]

    if status == 'excluded':
        # Red X for excluded
        ax.plot([-0.8, 0.8], [-0.8, 0.8], color=RED, linewidth=4, alpha=0.6)
        ax.plot([-0.8, 0.8], [0.8, -0.8], color=RED, linewidth=4, alpha=0.6)
        ax.text(0, 0, 'NOT\nGEOMETRIC', fontsize=10, color=RED, ha='center',
                va='center', fontweight='bold')
    elif 'Ellipsoid' in shape_label:
        # Oblate ellipse
        ellipse = matplotlib.patches.Ellipse((0, 0), 2.0, 1.0, fill=True,
                    facecolor=color, alpha=0.15, edgecolor=color, linewidth=2)
        ax.add_patch(ellipse)
    else:
        # Circle/sphere
        circle = plt.Circle((0, 0), 0.9, fill=True, facecolor=color,
                              alpha=0.15, edgecolor=color, linewidth=2)
        ax.add_patch(circle)

    # Title above
    ax.text(0, 1.45, name, fontsize=9, color=color, ha='center',
            fontweight='bold')

    # Shape label
    ax.text(0, -1.15, shape_label, fontsize=8, color=SILVER, ha='center')

    # Scale
    ax.text(0, -1.45, scale, fontsize=7, color=DIM, ha='center')

    # Test label
    test_color = RED if status == 'excluded' else GOLD
    ax.text(0, -1.7, test, fontsize=7, color=test_color, ha='center',
            fontweight='bold')

# Use the 8th subplot position for the legend/summary
ax_summary = fig.add_subplot(2, 4, 8)
ax_summary.set_facecolor(BG)
ax_summary.axis('off')
ax_summary.set_xlim(0, 10)
ax_summary.set_ylim(0, 10)
ax_summary.text(5, 8, 'CLASSIFICATION', fontsize=12, color=GOLD,
                ha='center', fontweight='bold')
ax_summary.text(5, 6.5, '6 geometric\n(framework applies)', fontsize=11,
                color=GREEN, ha='center', fontweight='bold')
ax_summary.text(5, 4.5, '1 excluded\n(not spatial)', fontsize=11,
                color=RED, ha='center', fontweight='bold')
ax_summary.text(5, 2.5, 'Documenting where\nthe framework STOPS\nis itself a finding.',
                fontsize=9, color=SILVER, ha='center', style='italic')

fig.suptitle('Boundary Geometry Gallery: Which Boundaries Does MATH-1 Reach?',
             fontsize=16, color=GOLD, fontweight='bold', y=0.98)

path = os.path.join(get_outdir(), 'phys4_01_boundary_gallery.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: phys4_01_boundary_gallery.png")


# ================================================================
# FIG 2: PROTON RADIUS PROBE DEPTH — ELECTRON VS MUON
# Type: Dual-panel geometric
# Shows: Electron at Bohr radius (large cross-section) vs muon
# at a0/207 (small cross-section). The 207x depth difference
# and the corresponding radius measurements.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Electron Probe: Large Cross-Section",
    "Muon Probe: Small Cross-Section (207\u00d7 deeper)",
    size=(18, 9), wspace=0.35)

for a in [ax1, ax2]:
    a.set_xlim(-2.5, 2.5)
    a.set_ylim(-2.5, 2.5)
    a.set_aspect('equal')
    a.set_xticks([])
    a.set_yticks([])

# Proton in both panels
for ax in [ax1, ax2]:
    proton = plt.Circle((0, 0), 0.25, fill=True, facecolor=RED,
                          alpha=0.4, edgecolor=RED, linewidth=2, zorder=5)
    ax.add_patch(proton)
    ax.text(0, 0, 'p', fontsize=12, color=WHITE, ha='center', va='center',
            fontweight='bold', zorder=6)

# Left panel: electron probe
# Large orbital radius
e_orbit = plt.Circle((0, 0), 1.6, fill=False, edgecolor=CYAN,
                       linewidth=2.5, linestyle='--', zorder=3)
ax1.add_patch(e_orbit)

# Cross-section shading
e_cross = plt.Circle((0, 0), 1.6, fill=True, facecolor=CYAN,
                       alpha=0.06, edgecolor='none', zorder=2)
ax1.add_patch(e_cross)

# Electron marker
data_point(ax1, 1.6, 0, '', CYAN, size=200)
ax1.text(1.6, 0.35, 'e\u207b', fontsize=12, color=CYAN, ha='center',
         fontweight='bold')

# Labels
ax1.text(0, -1.9, 'Orbital radius: a\u2080 \u2248 5.3\u00d710\u207b\u00b9\u00b9 m',
         fontsize=9, color=CYAN, ha='center')
ax1.text(0, -2.2, '\u03b2\u00b7d\u00b2 \u2248 8.8\u00d710\u207b\u00b2\u00b9 m\u00b2',
         fontsize=9, color=CYAN, ha='center', fontweight='bold')

# Result
ax1.text(0, 1.9, 'Reads: r_p = 0.877 fm', fontsize=12, color=GOLD,
         ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Right panel: muon probe
# Small orbital radius (207x smaller)
mu_orbit = plt.Circle((0, 0), 0.45, fill=False, edgecolor=ORANGE,
                        linewidth=2.5, linestyle='--', zorder=3)
ax2.add_patch(mu_orbit)

mu_cross = plt.Circle((0, 0), 0.45, fill=True, facecolor=ORANGE,
                        alpha=0.10, edgecolor='none', zorder=2)
ax2.add_patch(mu_cross)

# Muon marker
data_point(ax2, 0.45, 0, '', ORANGE, size=200)
ax2.text(0.45, 0.35, '\u03bc\u207b', fontsize=12, color=ORANGE, ha='center',
         fontweight='bold')

# Labels
ax2.text(0, -1.9, 'Orbital radius: a\u2080/207 \u2248 2.6\u00d710\u207b\u00b9\u00b3 m',
         fontsize=9, color=ORANGE, ha='center')
ax2.text(0, -2.2, '\u03b2\u00b7d\u00b2 \u2248 2.1\u00d710\u207b\u00b2\u2075 m\u00b2',
         fontsize=9, color=ORANGE, ha='center', fontweight='bold')

# Result
ax2.text(0, 1.9, 'Reads: r_p = 0.842 fm', fontsize=12, color=GOLD,
         ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Cross-section ratio annotation
ax2.text(0, -0.8, 'Cross-section ratio:\n42,849\u00d7 smaller',
         fontsize=10, color=RED, ha='center', fontweight='bold')

save_fig(fig, 'phys4_02_proton_probe_depth.png')


# ================================================================
# FIG 3: TEST ACHIEVABILITY TIMELINE
# Type: Scale/landscape
# Shows: Seven tests from "now" to "far future" with data sources
# and the kill switch gate after Tests 0-2.
# ================================================================

fig, ax = dark_canvas("The Test Program: Ordered by Achievability",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 11)

# Timeline axis
ax.plot([1.5, 8.5], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.5)

# Tests positioned along achievability
tests = [
    (1.8, 'Test 0', '\u03b1 calibration', 'Published collider\ndata + QED', GREEN, 8.5),
    (2.8, 'Test 1', 'G geometry', 'Published G\nmeasurements', GREEN, 7.0),
    (3.8, 'Test 2', 'G depth trend', 'Published G +\ngeodesic data', GREEN, 5.5),
    (4.8, 'Test 3', 'Proton radius', 'Published spectroscopy\n+ QED', CYAN, 8.5),
    (5.8, 'Test 4', 'G at L1/L2', 'New instrument\nat Lagrange point', ORANGE, 7.0),
    (6.8, 'Test 5', 'Hubble tension', 'Requires prior\ntheoretical work', RED, 5.5),
    (8.0, 'Test 7', 'Solar system\nboundary', 'Future deep\nspace mission', DIM, 8.5),
]

for x, label, desc, data_src, color, y in tests:
    # Vertical line to timeline
    ax.plot([x, x], [0.5, y - 0.5], color=color, linewidth=1.5, alpha=0.4)
    data_point(ax, x, 0.5, '', color, size=150)

    # Test box
    ax.text(x, y, label, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(x, y - 0.6, desc, fontsize=8, color=WHITE, ha='center')
    ax.text(x, y - 1.2, data_src, fontsize=7, color=DIM, ha='center')

# Timeline labels
ax.text(1.5, 0.0, 'NOW', fontsize=10, color=GREEN, ha='center',
        fontweight='bold')
ax.text(5.8, 0.0, 'ACHIEVABLE', fontsize=10, color=ORANGE, ha='center',
        fontweight='bold')
ax.text(8.0, 0.0, 'FAR FUTURE', fontsize=10, color=DIM, ha='center',
        fontweight='bold')

# Kill switch gate
ax.plot([4.3, 4.3], [1.5, 3.5], color=RED, linewidth=3, linestyle='--')
ax.text(4.3, 3.8, 'KILL SWITCH', fontsize=12, color=RED, ha='center',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))
ax.text(4.3, 2.5, 'If Tests 0,1,2\nALL null:\nSTOP PROGRAM',
        fontsize=9, color=RED, ha='center')

# Data source legend
shaded_region(ax, 1.5, 4.2, GREEN, 0.04)
ax.text(2.8, 10.5, 'EXISTING DATA — no new experiments', fontsize=9,
        color=GREEN, ha='center', fontweight='bold')

save_fig(fig, 'phys4_03_test_timeline.png')


# ================================================================
# FIG 4: PER-TRANSIT CORRECTION MAGNITUDE PROBLEM
# Type: Scale/landscape (log magnitude)
# Shows: beta (0.785) vs required per-transit correction (~0.9999)
# vs boundary count (100-10000). The enormous gap between beta
# and the required correction IS the missing piece.
# ================================================================

fig, ax = dark_fig("The Missing Piece: Per-Transit Correction Must Be Tiny",
                   xlabel="Number of boundaries along CMB line of sight (log scale)",
                   ylabel="Required per-transit correction factor",
                   size=(16, 10))

# x^N = 0.923 => x = 0.923^(1/N)
N_vals = np.logspace(1, 5, 200)
x_required = 0.923 ** (1.0 / N_vals)

curve(ax, N_vals, x_required, 'Required per-transit factor for H\u2080 ratio = 0.923',
      GOLD, 2.5)

# Beta reference
ax.plot([10, 100000], [np.pi / 4, np.pi / 4], color=RED, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(30, np.pi / 4 + 0.015, '\u03b2 = \u03c0/4 \u2248 0.785', fontsize=11,
        color=RED, fontweight='bold')
ax.text(30, np.pi / 4 - 0.025, '(FAR too large \u2014 would destroy signal after 2 transits)',
        fontsize=8, color=RED, style='italic')

# Mark key boundary counts
marks = [
    (100, 'Clusters\n~100', CYAN),
    (1000, 'Filaments\n~1000', BLUE),
    (10000, 'Galaxies\n~10\u2074', PURPLE),
    (100000, 'All structures\n~10\u2075', DIM),
]

for N, label, color in marks:
    x_val = 0.923 ** (1.0 / N)
    data_point(ax, N, x_val, '', color, size=200)
    ax.annotate(label + '\nx = %.6f' % x_val,
                xy=(N, x_val), xytext=(N * 2, x_val - 0.03),
                fontsize=8, color=color, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

# The gap annotation
ax.annotate('', xy=(500, 0.9999), xytext=(500, 0.785),
            arrowprops=dict(arrowstyle='<->', color=MAG, lw=2.5))
ax.text(700, 0.89, 'THE GAP\n\u03b2 is here\nRequired is here\n\nWhat determines\nthe per-transit\ncorrection?',
        fontsize=10, color=MAG, ha='left', fontweight='bold')

ax.set_xscale('log')
ax.set_xlim(50, 200000)
ax.set_ylim(0.75, 1.005)

result_box(ax, 5000, 0.78,
           'Test 5 CANNOT be executed\nuntil this magnitude is derived.\nThe question is well-posed.\nThe answer is unknown.',
           RED, 9)

save_fig(fig, 'phys4_04_per_transit_magnitude.png')


# ================================================================
# FIG 5: ALPHA RUNNING DECOMPOSITION — GEOMETRIC BASELINE
# Type: Running/decomposition
# Shows: Published alpha(E) separated into geometric component
# beta*d^2(E) and QED correction Z(E). The separation IS the
# calibration test.
# ================================================================

fig, ax = dark_fig("Test 0: Decompose the Running of \u03b1 into Geometry + QED",
                   xlabel="Probe energy E (GeV, log scale)",
                   ylabel="",
                   size=(16, 10))

# Schematic alpha running
E = np.logspace(-1, 2, 200)
# alpha^-1 decreasing with energy (approximate)
inv_alpha = 137.036 - 2.0 * np.log(E / 0.0005)
inv_alpha = np.clip(inv_alpha, 126, 138)

# Geometric baseline (smooth)
geo_baseline = 137.036 - 1.8 * np.log(E / 0.0005)
geo_baseline = np.clip(geo_baseline, 127, 138)

# QED correction (difference)
qed_correction = inv_alpha - geo_baseline

curve(ax, E, inv_alpha, '\u03b1\u207b\u00b9(E) measured', WHITE, 2.5)
curve(ax, E, geo_baseline, '\u03b2\u00b7d\u00b2(E) geometric baseline?', CYAN, 2.0,
      style='--')

# Shade the difference
ax.fill_between(E, geo_baseline, inv_alpha, alpha=0.08, color=MAG)
ax.text(20, 130, 'Z(E): QED correction\n(vacuum polarization\n+ vertex)', fontsize=9,
        color=MAG, ha='center', fontweight='bold')

# Key data points
data_points_alpha = [
    (0.001, 137.036, 'Thomson limit', SILVER),
    (1.78, 134, '\u03c4 scale', BLUE),
    (10, 132, '\u03a5 scale', CYAN),
    (91.2, 127.95, 'Z pole', GOLD),
]

for e_val, a_val, label, color in data_points_alpha:
    measured_diamond(ax, e_val, a_val, '', color, size=200)
    ax.text(e_val * 1.5, a_val + 0.8, label, fontsize=8, color=color)

ax.set_xscale('log')
ax.set_xlim(0.0003, 200)
ax.set_ylim(125, 139)

# Three outcomes
result_box(ax, 0.005, 126.5,
           'OUTCOME A: Redundant (reproduces QED, no new structure)\n'
           'OUTCOME B: Informative (reveals geometric baseline)\n'
           'OUTCOME C: Contradictory (conflicts with QED \u2192 kill field-theory tests)',
           GOLD, 9)

ax.set_ylabel('\u03b1\u207b\u00b9(E)', color=SILVER, fontsize=11)

save_fig(fig, 'phys4_05_alpha_decomposition.png')


# ================================================================
# FIG 6: G MEASUREMENT GEOMETRY — FOUR D^2 CANDIDATES
# Type: Geometric cross-section
# Shows: A Cavendish apparatus with four candidate d^2 identifications
# highlighted. Each candidate selects a different geometric element.
# ================================================================

fig, ax = dark_canvas("Test 1: Four Candidates for d\u00b2 in G Measurements",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Simplified Cavendish: source mass (left), test mass (right), separation
# Source mass
source = plt.Circle((3.0, 5.0), 0.8, fill=True, facecolor=BLUE,
                      alpha=0.3, edgecolor=BLUE, linewidth=2, zorder=3)
ax.add_patch(source)
ax.text(3.0, 5.0, 'Source\nmass M', fontsize=10, color=WHITE,
        ha='center', va='center', fontweight='bold', zorder=4)

# Test mass
test = plt.Circle((7.0, 5.0), 0.5, fill=True, facecolor=GREEN,
                    alpha=0.3, edgecolor=GREEN, linewidth=2, zorder=3)
ax.add_patch(test)
ax.text(7.0, 5.0, 'Test\nmass m', fontsize=10, color=WHITE,
        ha='center', va='center', fontweight='bold', zorder=4)

# Separation arrow
ax.annotate('', xy=(6.5, 5.0), xytext=(3.8, 5.0),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=2))
ax.text(5.0, 5.3, 'r', fontsize=14, color=WHITE, ha='center',
        fontweight='bold')

# Four candidates with arrows
candidates = [
    (7.0, 8.5, 'CANDIDATE 1', 'Test mass\ncross-section', GREEN,
     7.0, 5.5, 'G differs by test mass shape\n(sphere vs cylinder vs atom cloud)'),
    (3.0, 8.5, 'CANDIDATE 2', 'Source mass\ncross-section', BLUE,
     3.0, 5.8, 'G differs by source mass shape\n(sphere vs cylinder vs mercury)'),
    (5.0, 1.5, 'CANDIDATE 3', 'Interaction\ngeometry', ORANGE,
     5.0, 4.5, 'G differs by source-test configuration\n(aspect ratio, solid angle)'),
    (9.0, 3.0, 'CANDIDATE 4', 'Gravitational\naperture', MAG,
     7.5, 4.5, 'G differs by effective flux area\n(Poynting analogy from MATH-1)'),
]

for tx, ty, title, desc, color, ax_x, ax_y, prediction in candidates:
    ax.text(tx, ty, title, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(tx, ty - 0.6, desc, fontsize=9, color=SILVER, ha='center')
    ax.text(tx, ty - 1.2, prediction, fontsize=7, color=DIM, ha='center')
    ax.annotate('', xy=(ax_x, ax_y), xytext=(tx, ty - 1.5),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5, alpha=0.6))

# HUST constraint
ax.text(5.0, 0.4, 'HUST CONSTRAINT: Same masses + two methods = two G values.\n'
        'Geometry identical \u2192 disagreement must reside in Z (method impedance).',
        fontsize=9, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys4_06_g_geometry_candidates.png')


# ================================================================
# FIG 7: SENSITIVITY ANALYSIS — WHICH VARIABLES HAVE LEVER ARM
# Type: Comparison/threshold
# Shows: Log-scale bars for altitude, latitude, local g variations
# across G experiments, compared to the G disagreement scale.
# Shows which variables can reach the signal.
# ================================================================

fig, ax = dark_fig("Test 2 Sensitivity: Which Variables Reach the Signal?",
                   xlabel="",
                   ylabel="Relative magnitude (log scale)",
                   size=(16, 10))

variables = [
    ('\u0394\u03a6/c\u00b2\n(altitude)', 5e-14, RED, 'Altitude range:\n10-500 m'),
    ('\u0394\u03a6/c\u00b2\n(latitude)', 3e-12, ORANGE, 'Latitude range:\n30.5\u00b0-51.5\u00b0N'),
    ('\u0394g/g\n(local gravity)', 2e-3, GREEN, 'g range:\n9.793-9.812 m/s\u00b2'),
    ('\u0394G/G\n(disagreement)', 5e-4, GOLD, 'G spread across\nmodern experiments'),
]

x_pos = np.arange(len(variables))

for i, (label, value, color, detail) in enumerate(variables):
    ax.bar(i, value, color=color, alpha=0.7, edgecolor=color,
           linewidth=1.5, width=0.6)
    # Value label
    ax.text(i, value * 2, '%.0e' % value, fontsize=10, color=color,
            ha='center', fontweight='bold')
    ax.text(i, value * 0.3, detail, fontsize=7, color=DIM, ha='center')

# G disagreement threshold line
ax.plot([-0.5, 3.5], [5e-4, 5e-4], color=GOLD, linewidth=2.5,
        linestyle='--', alpha=0.7)
ax.text(3.6, 5e-4, 'G disagreement\nscale', fontsize=9, color=GOLD,
        va='center', fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels([v[0] for v in variables], fontsize=9, color=SILVER)
ax.set_yscale('log')
ax.set_xlim(-0.8, 4.2)
ax.set_ylim(1e-15, 1e-1)

# Annotations
ax.annotate('10\u00b9\u2070\u00d7 too small\nfor altitude', xy=(0, 5e-14),
            xytext=(0.5, 1e-10),
            fontsize=9, color=RED,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.0))

ax.annotate('Within 1 order\nof magnitude!', xy=(2, 2e-3),
            xytext=(2.5, 1e-1),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

result_box(ax, 1.5, 1e-8,
           'Local g variation is the most promising variable.\n'
           'Altitude alone is underpowered by 10\u00b9\u2070.',
           SILVER, 9)

save_fig(fig, 'phys4_07_sensitivity_analysis.png')


# ================================================================
# FIG 8: PHYS-4 IDENTITY CARD
# Type: Identity card
# Shows: Seven tests, kill switch, boundary classification,
# "calibrate before applying." Visual anchor.
# ================================================================

fig, ax = dark_canvas("PHYS-4 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE BOUNDARY TEST PROGRAM', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')

# Left column: the seven tests
ax.text(2.5, 8.2, 'SEVEN TESTS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

test_list = [
    ('Test 0', '\u03b1 calibration', GREEN, 'NOW'),
    ('Test 1', 'G geometry', GREEN, 'NOW'),
    ('Test 2', 'G depth trend', GREEN, 'NOW'),
    ('Test 3', 'Proton radius', CYAN, 'NOW'),
    ('Test 4', 'G at L1/L2', ORANGE, 'NEW INST.'),
    ('Test 5', 'Hubble tension', RED, 'THEORY'),
    ('Test 7', 'Solar boundary', DIM, 'FAR FUTURE'),
]

for i, (label, desc, color, status) in enumerate(test_list):
    y = 7.4 - i * 0.7
    ax.text(1.0, y, label, fontsize=9, color=color, fontweight='bold')
    ax.text(2.3, y, desc, fontsize=9, color=SILVER)
    ax.text(4.0, y, status, fontsize=8, color=color, fontweight='bold')

# Right column: key principles
ax.text(7.5, 8.2, 'KEY PRINCIPLES', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

principles = [
    ('CALIBRATE FIRST', 'Reproduce known results\nbefore testing unknown', GREEN),
    ('KILL SWITCH', 'Tests 0,1,2 all null\n\u2192 program stops', RED),
    ('SCOPE BOUNDARY', '6 geometric boundaries\n1 excluded (confinement)', CYAN),
    ('MISSING PIECE', 'Per-transit correction\nmagnitude unknown', ORANGE),
]

for i, (title, detail, color) in enumerate(principles):
    y = 7.2 - i * 1.3
    ax.text(7.5, y, title, fontsize=10, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(7.5, y - 0.6, detail, fontsize=8, color=SILVER, ha='center')

# The question
ax.plot([0.5, 9.5], [2.5, 2.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

ax.text(5, 2.0, 'THE QUESTION', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 1.2, 'Does Q = F \u00b7 \u03b2 \u00b7 d\u00b2 \u00b7 Z,\n'
        'proven for cross-sections across nine domains,\n'
        'apply to the coherent pattern boundaries\n'
        'where measurement anomalies have been documented?',
        fontsize=10, color=SILVER, ha='center')

# Bottom
ax.text(5, 0.3, 'HOWL-PHYS-4: Seven tests. Three achievable now. '
        'Kill switch at the gate. Calibrate before applying.',
        fontsize=9, color=GOLD, ha='center', style='italic')

save_fig(fig, 'phys4_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-4 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys4_01_boundary_gallery.png',
    'phys4_02_proton_probe_depth.png',
    'phys4_03_test_timeline.png',
    'phys4_04_per_transit_magnitude.png',
    'phys4_05_alpha_decomposition.png',
    'phys4_06_g_geometry_candidates.png',
    'phys4_07_sensitivity_analysis.png',
    'phys4_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    