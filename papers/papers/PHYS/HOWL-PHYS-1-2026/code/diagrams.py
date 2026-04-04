#!/usr/bin/env python3
"""
HOWL PHYS-1 Diagrams — The Inertial Vortex
8 figures covering mass-is-inertia, soliton boundaries, anomaly correlations.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: H0 VS BOUNDARY TRANSIT COUNT
# Type: Running/Convergence (Type 1)
# Shows: The downward trend — more boundary transits, lower H0.
# ================================================================

fig, ax = dark_fig("Hubble Constant vs. Boundary Transit Count",
                   xlabel="Relative Boundary Transit Count  \u2192  more crossings",
                   ylabel="H\u2080  (km/s/Mpc)")

data = [
    (1.0, 73.0, 1.0, 'Local Distance Ladder\n(SH0ES)', ORANGE),
    (1.5, 73.3, 1.8, 'Lensing Time Delays\n(H0LiCOW)', CYAN),
    (2.5, 69.8, 1.7, 'Tip of Red Giant\nBranch (CCHP)', GREEN),
    (4.0, 67.4, 0.5, 'CMB\n(Planck)', BLUE),
]

for x, h0, err, label, color in data:
    data_point_err(ax, x, h0, err, "", color, size=250)
    ax.annotate(label, xy=(x, h0), xytext=(x + 0.35, h0 + 0.3),
                fontsize=10, color=color, fontweight='bold',
                va='center', ha='left',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

xs = np.array([d[0] for d in data])
ys = np.array([d[1] for d in data])
z = np.polyfit(xs, ys, 1)
xfit = np.linspace(0.5, 4.5, 100)
yfit = np.polyval(z, xfit)
curve(ax, xfit, yfit, "", GOLD, width=2, style='--', alpha=0.5)

shaded_region_h(ax, 66.9, 68.0, BLUE, 0.08)
shaded_region_h(ax, 72.0, 74.0, ORANGE, 0.08)

result_box(ax, 2.7, 70.4, 'Tension: ~9%\n(>4\u03c3)')

ax.set_xlim(0.3, 5.5)
ax.set_ylim(64, 77)

note(ax, 4.2, 65.0, 'More transits \u2192 lower H\u2080', DIM, 10)

save_fig(fig, 'phys1_01_h0_transit_correlation.png')


# ================================================================
# FIG 2: SOLITON BOUNDARY NESTING
# Type: Geometric Cross-Section (Type 4)
# Shows: Concentric nesting from particle to observable universe.
# ================================================================

fig, ax = dark_canvas("Soliton Boundary Nesting: Every Measurement Crosses All Layers",
                      size=(16, 16))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

shells = [
    (1.10, 'Observable Universe  (~4.4e26 m)', PURPLE),
    (0.92, 'Galaxy Cluster  (~1e23 m)', BLUE),
    (0.74, 'Galaxy (Milky Way)  (~1e21 m)', CYAN),
    (0.56, 'Star (Sun)  (~7e8 m)', ORANGE),
    (0.40, 'Planet (Earth)  (~6.4e6 m)', GREEN),
    (0.24, 'Atom  (~1e-10 m)', MAG),
    (0.12, 'Nucleus  (~1e-15 m)', RED),
    (0.05, 'Particle (Vortex)', GOLD),
]

concentric_shells(ax, shells)

arrow_label(ax, 0.0, -0.30, -0.85, -1.05, 'Observer (here)', WHITE)

save_fig(fig, 'phys1_02_soliton_nesting.png')


# ================================================================
# FIG 3: PROTON RADIUS VS PROBE INERTIA
# Type: Running/Convergence (Type 1)
# Shows: Depth-dependent trend with tau prediction.
# ================================================================

fig, ax = dark_fig("Proton Radius vs. Probe Inertia: Depth-Dependent Reading",
                   xlabel="Probe Inertia (MeV/c\u00b2)",
                   ylabel="Measured Proton Charge Radius (fm)")

# Measured points
probes = [
    (0.511, 0.877, 0.005, 'Electron (historical)', MAG),
    (0.511, 0.841, 0.005, 'Electron (recent)', ORANGE),
    (105.7, 0.842, 0.001, 'Muon', CYAN),
]

for mass, radius, err, label, color in probes:
    data_point_err(ax, mass, radius, err, "", color, size=220)
    dy = 0.014 if radius > 0.86 else -0.016
    ax.annotate(label, xy=(mass, radius),
                xytext=(mass * 2.2, radius + dy),
                fontsize=10, color=color, fontweight='bold', va='center',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

# Tau prediction
tau_center = 0.82
ax.axhspan(tau_center - 0.02, tau_center + 0.02,
           xmin=0.80, xmax=0.98, alpha=0.15, color=GOLD, zorder=2)
measured_diamond(ax, 1776.9, tau_center, "", GOLD, size=220)
arrow_label(ax, 1776.9, tau_center, 350, 0.803,
            'Tau (predicted)\nSmaller than muon', GOLD)

# Trend line
x_log = np.log10([0.511, 105.7])
y_vals = [0.860, 0.842]
z = np.polyfit(x_log, y_vals, 1)
x_ext = np.linspace(np.log10(0.3), np.log10(3000), 200)
y_ext = np.polyval(z, x_ext)
curve(ax, 10**x_ext, y_ext, "", DIM, width=1.5, style='--', alpha=0.6)

ax.set_xscale('log')
ax.set_xlim(0.2, 6000)
ax.set_ylim(0.78, 0.91)

note(ax, 0.5, 0.90, 'Higher inertia \u2192 deeper interaction \u2192 smaller radius',
     DIM, 10)

save_fig(fig, 'phys1_03_proton_radius_depth.png')


# ================================================================
# FIG 4: PROBE DEPTH INTO PROTON (GEOMETRIC)
# Type: Geometric Cross-Section (Type 4)
# Shows: Electron vs muon orbit depths inside proton boundary.
# ================================================================

fig, ax = dark_canvas("Proton as Structured Vortex: Probe Depth Determines Reading",
                      size=(16, 14))
ax.set_xlim(-1.5, 1.8)
ax.set_ylim(-1.3, 1.4)
ax.set_aspect('equal')

cx, cy = 0.0, 0.0

# Proton radial gradient
n_rings = 30
for i in range(n_rings, 0, -1):
    r = 0.70 * (i / float(n_rings))
    alpha_val = 0.03 + 0.12 * (1.0 - i / float(n_rings))
    if i > n_rings * 0.6:
        cmix = RED
    elif i > n_rings * 0.3:
        cmix = ORANGE
    else:
        cmix = GOLD
    circle = plt.Circle((cx, cy), r, fill=True, facecolor=cmix,
                         alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(circle)

# Proton boundary
proton_b = plt.Circle((cx, cy), 0.70, fill=False,
                       edgecolor=RED, linewidth=2.5, linestyle='--', zorder=3)
ax.add_patch(proton_b)
ax.text(0.0, 1.05, 'Proton Boundary\n(form factor transition)',
        fontsize=11, color=RED, fontweight='bold', ha='center')

# Electron orbit — large, shallow
theta = np.linspace(0, 2 * np.pi, 200)
e_r = 0.90
ex = cx + e_r * np.cos(theta)
ey = cy + e_r * np.sin(theta) * 0.25 + 0.12
ax.plot(ex, ey, color=MAG, linewidth=2.5, zorder=4, alpha=0.8)
ax.scatter([cx + e_r], [cy + 0.12], s=120, color=MAG,
           edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(1.15, 0.45, 'Electron orbit\n(shallow interaction)\nr \u2248 0.877 fm reading',
        fontsize=10, color=MAG, fontweight='bold', ha='left')

# Muon orbit — small, deep
mu_r = 0.25
mx = cx + mu_r * np.cos(theta)
my = cy + mu_r * np.sin(theta) * 0.25
ax.plot(mx, my, color=CYAN, linewidth=2.5, zorder=4, alpha=0.8)
ax.scatter([cx + mu_r], [cy], s=120, color=CYAN,
           edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(0.45, -0.30, 'Muon orbit\n(deep interaction)\nr \u2248 0.842 fm reading',
        fontsize=10, color=CYAN, fontweight='bold', ha='left')

# Tau prediction
tau_r = 0.08
tx = cx + tau_r * np.cos(theta)
ty = cy + tau_r * np.sin(theta) * 0.25
ax.plot(tx, ty, color=GOLD, linewidth=2, linestyle='--', zorder=4, alpha=0.6)
ax.text(0.20, -0.18, 'Tau orbit (predicted)\nr < 0.842 fm',
        fontsize=9, color=GOLD, fontweight='bold', ha='left')

# Depth arrow
ax.annotate('', xy=(0, 0), xytext=(0, 0.72),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2, linestyle='--'))
ax.text(-0.15, 0.50, 'Interaction\nDepth', fontsize=10, color=WHITE,
        ha='center', rotation=90, style='italic')

# Region labels
ax.text(0.0, -0.95, 'INTERIOR: coherence dominates  (quarks asymptotically free)',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold', alpha=0.8)
ax.text(0.0, -1.15, 'EXTERIOR: confinement dominates  (proton appears as point particle)',
        fontsize=10, color=DIM, ha='center')

save_fig(fig, 'phys1_04_proton_probe_depth.png')


# ================================================================
# FIG 5: MASS-IS-INERTIA PRECISION HISTORY
# Type: Scale/Landscape (Type 2)
# Shows: Century of convergence from 10^-8 to 10^-15.
# ================================================================

fig, ax = dark_fig("The Equivalence Principle: A Century of Confirming Identity",
                   size=(16, 10),
                   xlabel="Year",
                   ylabel="Precision: agreement to 10^-n")

experiments = [
    (1922, 8,  'Eotvos experiment', ORANGE),
    (1964, 11, 'Roll, Krotkov & Dicke', CYAN),
    (1999, 13, 'Baessler et al.', GREEN),
    (2012, 13, 'LLR (Lunar Ranging)', BLUE),
    (2022, 15, 'MICROSCOPE satellite', GOLD),
]

years = [e[0] for e in experiments]
precs = [e[1] for e in experiments]
curve(ax, years, precs, "", DIM, width=1.5, style='-', alpha=0.5)

for year, prec, label, color in experiments:
    data_point(ax, year, prec, "", color, size=250)
    dy = 1.0 if prec < 14 else -1.2
    va_val = 'bottom' if dy > 0 else 'top'
    ax.annotate(label, xy=(year, prec),
                xytext=(year + 3, prec + dy),
                fontsize=10, color=color, fontweight='bold',
                ha='left', va=va_val,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

# Horizontal precision grid
for p in [8, 10, 12, 14]:
    ax.plot([1910, 2040], [p, p], color=DIM, linewidth=0.5, alpha=0.3, linestyle=':')

# Identity asymptote
ax.plot([1910, 2040], [16.5, 16.5], color=GOLD, linewidth=1.5, alpha=0.4, linestyle='--')
ax.text(2020, 17.0, 'Identity: m_grav \u2261 m_inertial', fontsize=11,
        color=GOLD, ha='right', style='italic', fontweight='bold')

# Convergence arrow
ax.annotate('', xy=(2032, 16.2), xytext=(2032, 8.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
ax.text(2034, 12.5, 'Converging\ntoward\nidentity', fontsize=10,
        color=WHITE, ha='left', va='center', style='italic')

ax.set_xlim(1910, 2045)
ax.set_ylim(6, 18)
ax.set_yticks([8, 10, 12, 14, 16])
ax.set_yticklabels(['10^-8', '10^-10', '10^-12', '10^-14', '10^-16'])

result_box(ax, 1960, 7.0, 'No deviation found at any precision.\nOne property, two labels.',
           SILVER, 11)

save_fig(fig, 'phys1_05_equivalence_precision.png')


# ================================================================
# FIG 6: BOUNDARY TRANSIT LIGHT PATH
# Type: Progression/Sequence (Type 7)
# Shows: CMB photon path through multiple boundaries to detector.
# ================================================================

fig, ax = dark_canvas("Boundary Transit Paths: CMB vs. Local Measurements",
                      size=(18, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

stages = [
    ('Source\n(CMB / SN)', PURPLE, 0.6),
    ('Source\nGalaxy', BLUE, 1.8),
    ('Cluster\nBoundary', CYAN, 3.0),
    ('Intergalactic\nVoid', DIM, 4.2),
    ('Our Galaxy\nBoundary', GREEN, 5.4),
    ('Solar System\nBoundary', ORANGE, 6.6),
    ('Earth\nBoundary', MAG, 7.8),
    ('Detector', GOLD, 9.2),
]

# Draw boundary walls
for label, color, x in stages:
    if label not in ('Intergalactic\nVoid', 'Detector', 'Source\n(CMB / SN)'):
        ax.plot([x, x], [2.0, 7.8], color=color, linewidth=3, alpha=0.6, zorder=3)
        for offset in [-0.04, 0.04]:
            ax.plot([x + offset, x + offset], [2.0, 7.8], color=color,
                    linewidth=1.5, alpha=0.2, zorder=2)

    ax.text(x, 8.8, label, fontsize=10, color=color, ha='center',
            va='center', fontweight='bold')

# CMB path (long, many boundaries)
y_cmb = 6.2
ax.annotate('', xy=(9.1, y_cmb), xytext=(0.7, y_cmb),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2.5))
ax.text(5.0, y_cmb + 0.6, 'CMB photon: crosses ALL boundaries \u2192 H\u2080 = 67.4',
        fontsize=10, color=PURPLE, ha='center', fontweight='bold')

# Local path (short, few boundaries)
y_local = 3.8
ax.annotate('', xy=(9.1, y_local), xytext=(5.5, y_local),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))
ax.text(7.3, y_local - 0.7, 'Local SN photon: crosses FEW boundaries \u2192 H\u2080 = 73.0',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold')

# Crossing markers
for label, color, x in stages:
    if x > 0.6 and x < 9.2 and color != DIM:
        ax.scatter([x], [y_cmb], s=80, color=PURPLE, edgecolors=WHITE,
                   linewidth=1.5, zorder=6)

for label, color, x in stages:
    if x > 5.4 and x < 9.2 and color != DIM:
        ax.scatter([x], [y_local], s=80, color=ORANGE, edgecolors=WHITE,
                   linewidth=1.5, zorder=6)

ax.text(5.0, 1.0, 'Each boundary crossing is an unmodeled transformation.\n'
        'More crossings \u2192 more cumulative effect \u2192 lower measured H\u2080.',
        fontsize=11, color=SILVER, ha='center', style='italic')

save_fig(fig, 'phys1_06_transit_light_path.png')


# ================================================================
# FIG 7: VORTEX CROSS-SECTION
# Type: Geometric Cross-Section (Type 4)
# Shows: 3D field vortex in cross-section: interior, boundary, exterior.
# ================================================================

fig, ax = dark_canvas("3D Field Vortex: Cross-Section of a Particle",
                      size=(14, 14))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Exterior — ambient field radial lines
for angle in np.linspace(0, 2 * np.pi, 24, endpoint=False):
    r0, r1 = 0.85, 1.10
    ax.plot([r0 * np.cos(angle), r1 * np.cos(angle)],
            [r0 * np.sin(angle), r1 * np.sin(angle)],
            color=DIM, linewidth=0.8, alpha=0.4, zorder=1)

# Interior — standing wave rings
n_rings = 40
for i in range(n_rings, 0, -1):
    r = 0.70 * (i / float(n_rings))
    wave = 0.5 + 0.5 * np.sin(i * np.pi / 4.0)
    alpha_val = 0.02 + 0.08 * wave * (1.0 - i / float(n_rings))
    color = CYAN if wave > 0.5 else BLUE
    circle = plt.Circle((0, 0), r, fill=True, facecolor=color,
                         alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(circle)

# Boundary ring with glow
boundary = plt.Circle((0, 0), 0.70, fill=False, edgecolor=GOLD,
                       linewidth=3, zorder=4)
ax.add_patch(boundary)
for dr in [0.015, 0.030, 0.045]:
    for sign in [1, -1]:
        ring = plt.Circle((0, 0), 0.70 + sign * dr, fill=False, edgecolor=GOLD,
                           linewidth=1, alpha=max(0.05, 0.3 - dr * 6), zorder=3)
        ax.add_patch(ring)

# Circulation arrows
for angle_start in [0, np.pi / 2, np.pi, 3 * np.pi / 2]:
    arc_r = 0.38
    theta_arr = np.linspace(angle_start, angle_start + np.pi / 3, 50)
    xa = arc_r * np.cos(theta_arr)
    ya = arc_r * np.sin(theta_arr)
    ax.plot(xa, ya, color=CYAN, linewidth=2, alpha=0.6, zorder=5)
    ax.annotate('', xy=(xa[-1], ya[-1]), xytext=(xa[-3], ya[-3]),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# Labels — well spaced
ax.text(0, 0, 'INTERIOR\nCoherence\ndominates', fontsize=12, color=CYAN,
        ha='center', va='center', fontweight='bold')

ax.text(0, 1.00, 'BOUNDARY  (soliton wall)', fontsize=11, color=GOLD,
        ha='center', fontweight='bold')

ax.text(0, -1.30, 'EXTERIOR: Ambient field dominates.\n'
        'Measurements from outside see different values than from inside.',
        fontsize=10, color=SILVER, ha='center', style='italic')

# Property boxes — corners, well away from geometry
props = [
    (-1.20, 1.25, 'Inertia = pattern\nresistance to disruption', MAG),
    (1.20, 1.25, 'Harmonic modes\n\u2192 quantum numbers', GREEN),
    (-1.20, -1.00, 'Spin = rotational\nmode of vortex', ORANGE),
    (1.20, -1.00, 'Boundary = where\nreadings diverge', GOLD),
]

for x, y, text, color in props:
    ax.text(x, y, text, fontsize=9, color=color, ha='center', va='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color, alpha=0.8))

save_fig(fig, 'phys1_07_vortex_cross_section.png')


# ================================================================
# FIG 8: PHYS-1 IDENTITY CARD
# Type: Identity Card (Type 8)
# Shows: Visual anchor — vortex + properties + three anomalies.
# ================================================================

fig, ax = dark_canvas("PHYS-1 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Central vortex
vcx, vcy = 3.0, 5.5
vr = 1.2

n_v = 20
for i in range(n_v, 0, -1):
    r = vr * (i / float(n_v))
    wave = 0.5 + 0.5 * np.sin(i * np.pi / 3.0)
    alpha_val = 0.03 + 0.10 * wave * (1.0 - i / float(n_v))
    color = CYAN if wave > 0.5 else BLUE
    circle = plt.Circle((vcx, vcy), r, fill=True, facecolor=color,
                         alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(circle)

boundary = plt.Circle((vcx, vcy), vr, fill=False, edgecolor=GOLD,
                       linewidth=3, zorder=4)
ax.add_patch(boundary)

ax.text(vcx, vcy, 'Coherent\nField\nVortex', fontsize=13, color=WHITE,
        ha='center', va='center', fontweight='bold')

# Properties — four quadrants, well spaced from vortex edge
connections = [
    (0.6, 8.5,  'MASS = INERTIA',    'Pattern resistance to disruption',
     'F = ma defines inertia\nm_grav = m_inertial to 10^-15', MAG),
    (5.2, 8.5,  'QUANTUM NUMBERS',   'Harmonic modes of standing wave',
     'Discrete, integer-indexed\nShell structure follows', GREEN),
    (0.4, 2.2,  'BOUNDARY',          'Inside \u2260 Outside readings',
     'GR: equivalence principle\nQCD: confinement\nQED: running \u03b1', GOLD),
    (5.2, 2.2,  'TRANSIT',           'Light crossing boundaries',
     'Hubble tension: 9%\nMore transits \u2192 lower H\u2080', PURPLE),
]

for px, py, title, subtitle, detail, color in connections:
    angle = np.arctan2(py - vcy, px - vcx)
    edge_x = vcx + vr * np.cos(angle) * 1.15
    edge_y = vcy + vr * np.sin(angle) * 1.15
    ax.annotate('', xy=(px + 0.5, py - 0.2), xytext=(edge_x, edge_y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    ax.text(px, py, '%s\n%s' % (title, subtitle), fontsize=10,
            color=color, ha='left', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=color, alpha=0.9))
    ax.text(px, py - 1.1, detail, fontsize=8, color=SILVER, ha='left', va='top')

# Right column — three anomalies
ax.text(8.2, 9.3, 'THREE ANOMALIES', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(8.2, 8.8, 'Each correlates with boundary\ndepth or transit count',
        fontsize=9, color=SILVER, ha='center')

anomalies = [
    (8.2, 7.4, 'HUBBLE TENSION',   '67.4 vs 73.0 km/s/Mpc\nTransit count difference', PURPLE),
    (8.2, 5.5, 'PROTON RADIUS',    '0.842 vs 0.877 fm\nProbe depth difference', CYAN),
    (8.2, 3.6, 'MUON g\u22122',    '~4.2\u03c3 discrepancy\nVacuum interaction depth', MAG),
]

for ax_x, ax_y, title, detail, color in anomalies:
    ax.text(ax_x, ax_y, title, fontsize=12, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color))
    ax.text(ax_x, ax_y - 0.75, detail, fontsize=9, color=SILVER, ha='center')

# Bottom banner
ax.text(5.0, 0.7, 'HOWL-PHYS-1: The Inertial Vortex', fontsize=17,
        color=GOLD, ha='center', fontweight='bold')
ax.text(5.0, 0.15, 'Current physics is incomplete at one point: '
        'the coherent vortex boundary as an unmodeled measurement element.',
        fontsize=10, color=SILVER, ha='center', style='italic')

save_fig(fig, 'phys1_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-1 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys1_01_h0_transit_correlation.png',
    'phys1_02_soliton_nesting.png',
    'phys1_03_proton_radius_depth.png',
    'phys1_04_proton_probe_depth.png',
    'phys1_05_equivalence_precision.png',
    'phys1_06_transit_light_path.png',
    'phys1_07_vortex_cross_section.png',
    'phys1_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
print()
print("| Fig | Filename | Section |")
print("|-----|----------|---------|")
print("| 1 | phys1_01_h0_transit_correlation.png | VI.1 Hubble Tension |")
print("| 2 | phys1_02_soliton_nesting.png | IV.1 Structural Principle |")
print("| 3 | phys1_03_proton_radius_depth.png | VI.2 Proton Radius |")
print("| 4 | phys1_04_proton_probe_depth.png | VI.2 Proton Radius |")
print("| 5 | phys1_05_equivalence_precision.png | II.2 The Connection |")
print("| 6 | phys1_06_transit_light_path.png | V.2 Structural Observation |")
print("| 7 | phys1_07_vortex_cross_section.png | III.2 Three-Dimensional Case |")
print("| 8 | phys1_08_identity_card.png | XI. Conclusion |")
