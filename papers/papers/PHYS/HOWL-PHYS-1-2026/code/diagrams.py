#!/usr/bin/env python3
"""
HOWL PHYS-1 Diagrams — The Inertial Vortex
8 figures covering mass-is-inertia, soliton boundaries, anomaly correlations.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Arc
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ================================================================
# GLOBAL STYLE
# ================================================================
BG      = '#0a0a12'
PAN     = '#12121f'
GOLD    = '#d4a843'
SILVER  = '#a0a8b8'
CYAN    = '#4ecdc4'
MAG     = '#c74b7a'
BLUE    = '#5b8def'
GREEN   = '#6bcf7f'
RED     = '#e05555'
ORANGE  = '#e8944a'
WHITE   = '#e8e8f0'
DIM     = '#555570'
PURPLE  = '#9b7bd4'

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

# ================================================================
# FIG 1: H0 VS BOUNDARY TRANSIT COUNT
# Type: Running/Convergence (Type 1)
# Shows: The downward trend — more boundary transits, lower H0.
# The shape of the curve IS the central anomaly correlation.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(PAN)

data = [
    (1.0, 73.0, 1.0, 'Local Distance\nLadder (SH0ES)', ORANGE),
    (1.5, 73.3, 1.8, 'Lensing Time\nDelays (H0LiCOW)', CYAN),
    (2.5, 69.8, 1.7, 'Tip of Red\nGiant Branch (CCHP)', GREEN),
    (4.0, 67.4, 0.5, 'CMB\n(Planck)', BLUE),
]

for x, h0, err, label, color in data:
    ax.errorbar(x, h0, yerr=err, fmt='o', color=color, markersize=18,
                markeredgecolor=WHITE, markeredgewidth=2, capsize=8,
                capthick=2, elinewidth=2, ecolor=color, zorder=5)
    ax.annotate(label, xy=(x, h0), xytext=(x + 0.25, h0),
                fontsize=10, color=color, fontweight='bold', va='center', ha='left')

xs = np.array([d[0] for d in data])
ys = np.array([d[1] for d in data])
z = np.polyfit(xs, ys, 1)
xfit = np.linspace(0.5, 4.5, 100)
yfit = np.polyval(z, xfit)
ax.plot(xfit, yfit, '--', color=GOLD, alpha=0.5, linewidth=2, zorder=3)

ax.axhspan(66.9, 68.0, alpha=0.08, color=BLUE, zorder=1)
ax.axhspan(72.0, 74.0, alpha=0.08, color=ORANGE, zorder=1)

ax.annotate('Tension: ~9%\n(>4\u03c3)', xy=(2.7, 70.4),
            fontsize=13, color=GOLD, ha='center', va='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xlabel('Relative Boundary Transit Count  \u2192  more crossings', fontsize=12, color=SILVER)
ax.set_ylabel('H\u2080  (km/s/Mpc)', fontsize=12, color=SILVER)
ax.set_title('Hubble Constant vs. Boundary Transit Count', fontsize=16,
             fontweight='bold', color=GOLD, pad=15)

ax.set_xlim(0.3, 5.2)
ax.set_ylim(64, 77)
ax.tick_params(colors=DIM, labelsize=10)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.text(4.8, 65.0, 'More transits \u2192 lower H\u2080',
        fontsize=10, color=DIM, ha='right', style='italic')

save(fig, 'phys1_01_h0_transit_correlation.png')


# ================================================================
# FIG 2: SOLITON BOUNDARY NESTING
# Type: Geometric Cross-Section (Type 4)
# Shows: Concentric nesting from particle to observable universe
# with physical scales. Impossible to convey in prose.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 16), facecolor=BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.15, 1.15)

layers = [
    (0.95, 'Observable Universe', '~4.4e26 m', PURPLE, 0.10),
    (0.80, 'Galaxy Cluster', '~1e23 m', BLUE, 0.12),
    (0.65, 'Galaxy (Milky Way)', '~1e21 m', CYAN, 0.15),
    (0.50, 'Star (Sun)', '~7e8 m', ORANGE, 0.18),
    (0.35, 'Planet (Earth)', '~6.4e6 m', GREEN, 0.22),
    (0.20, 'Atom', '~1e-10 m', MAG, 0.28),
    (0.10, 'Nucleus', '~1e-15 m', RED, 0.35),
    (0.04, 'Particle\n(Vortex)', '~1e-18 m', GOLD, 0.50),
]

for radius, label, scale, color, alpha in layers:
    circle = plt.Circle((0, 0), radius, fill=True,
                         facecolor=color, alpha=alpha,
                         edgecolor=color, linewidth=1.5, zorder=2)
    ax.add_patch(circle)

for i, (radius, label, scale, color, alpha) in enumerate(layers):
    if i < len(layers) - 1:
        angle = np.pi / 4 + i * np.pi / 14
        cx = radius * np.cos(angle)
        cy = radius * np.sin(angle)
        lx = (radius + 0.12 + i * 0.015) * np.cos(angle)
        ly = (radius + 0.12 + i * 0.015) * np.sin(angle)
        ax.annotate('%s\n%s' % (label, scale),
                    xy=(cx, cy), xytext=(lx, ly),
                    fontsize=8, color=color, fontweight='bold',
                    ha='left', va='center',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
    else:
        ax.text(0, 0, '%s\n%s' % (label, scale),
                fontsize=9, color=color, fontweight='bold',
                ha='center', va='center')

ax.annotate('Observer\n(here)', xy=(0, -0.28),
            xytext=(-0.7, -0.7),
            fontsize=10, color=WHITE, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

ax.set_title('Soliton Boundary Nesting: Every Measurement Crosses All Layers',
             fontsize=15, fontweight='bold', color=GOLD, pad=20)

save(fig, 'phys1_02_soliton_nesting.png')


# ================================================================
# FIG 3: PROTON RADIUS VS PROBE INERTIA
# Type: Running/Convergence (Type 1)
# Shows: Depth-dependent trend with tau prediction.
# The curve shape carries the prediction.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(PAN)

probes = [
    (0.511, 0.877, 0.005, 'Electron\n(historical)', MAG, True),
    (0.511, 0.841, 0.005, 'Electron\n(recent)', ORANGE, True),
    (105.7, 0.842, 0.001, 'Muon', CYAN, True),
]

for mass, radius, err, label, color, measured in probes:
    ax.errorbar(mass, radius, yerr=err, fmt='o', color=color,
                markersize=16, markeredgecolor=WHITE, markeredgewidth=2,
                capsize=6, capthick=2, elinewidth=2, ecolor=color, zorder=5)
    offset_y = 0.008 if radius > 0.86 else -0.012
    ax.annotate(label, xy=(mass, radius), xytext=(mass * 1.8, radius + offset_y),
                fontsize=10, color=color, fontweight='bold', va='center',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

tau_center = 0.82
tau_width = 0.02
ax.axhspan(tau_center - tau_width, tau_center + tau_width,
           xmin=0.82, xmax=0.98, alpha=0.15, color=GOLD, zorder=2)
ax.scatter([1776.9], [tau_center], marker='D', s=200, color=GOLD,
           edgecolors=WHITE, linewidth=2, zorder=5, alpha=0.7)
ax.annotate('Tau (predicted)\nSmaller than muon', xy=(1776.9, tau_center),
            xytext=(400, 0.808),
            fontsize=10, color=GOLD, fontweight='bold', va='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

x_log = np.log10([0.511, 105.7])
y_vals = [0.860, 0.842]
z = np.polyfit(x_log, y_vals, 1)
x_ext = np.linspace(np.log10(0.3), np.log10(3000), 200)
y_ext = np.polyval(z, x_ext)
ax.plot(10**x_ext, y_ext, '--', color=DIM, linewidth=1.5, alpha=0.6, zorder=3)

ax.set_xscale('log')
ax.set_xlabel('Probe Inertia (MeV/c\u00b2)', fontsize=12, color=SILVER)
ax.set_ylabel('Measured Proton Charge Radius (fm)', fontsize=12, color=SILVER)
ax.set_title('Proton Radius vs. Probe Inertia: Depth-Dependent Reading',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.set_xlim(0.2, 5000)
ax.set_ylim(0.79, 0.90)
ax.tick_params(colors=DIM, labelsize=10)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.text(1.0, 0.895, 'Higher inertia probe \u2192 deeper interaction \u2192 smaller radius',
        fontsize=10, color=DIM, style='italic')

save(fig, 'phys1_03_proton_radius_depth.png')


# ================================================================
# FIG 4: PROBE DEPTH INTO PROTON (GEOMETRIC)
# Type: Geometric Cross-Section (Type 4)
# Shows: Electron vs muon orbit depths inside proton boundary.
# Spatial relationship impossible in text.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.0, 1.2)

cx, cy = 0.0, 0.0

# Proton structure — radial gradient
n_rings = 30
for i in range(n_rings, 0, -1):
    r = 0.7 * (i / float(n_rings))
    alpha_val = 0.03 + 0.12 * (1.0 - i / float(n_rings))
    if i > n_rings * 0.6:
        color_mix = RED
    elif i > n_rings * 0.3:
        color_mix = ORANGE
    else:
        color_mix = GOLD
    circle = plt.Circle((cx, cy), r, fill=True, facecolor=color_mix,
                         alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(circle)

# Proton boundary
proton_boundary = plt.Circle((cx, cy), 0.7, fill=False,
                              edgecolor=RED, linewidth=2.5, linestyle='--', zorder=3)
ax.add_patch(proton_boundary)
ax.text(0.0, 0.95, 'Proton Boundary\n(form factor transition)',
        fontsize=11, color=RED, fontweight='bold', ha='center')

# Electron orbit — large, shallow
theta = np.linspace(0, 2 * np.pi, 200)
e_r = 0.88
ex = cx + e_r * np.cos(theta)
ey = cy + e_r * np.sin(theta) * 0.28 + 0.10
ax.plot(ex, ey, color=MAG, linewidth=2.5, linestyle='-', zorder=4, alpha=0.8)
ax.scatter([cx + e_r], [cy + 0.10], s=120, color=MAG,
           edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(1.05, 0.30, 'Electron orbit\n(shallow interaction)\nr \u2248 0.877 fm reading',
        fontsize=10, color=MAG, fontweight='bold', ha='left')

# Muon orbit — small, deep
mu_r_vis = 0.25
mx = cx + mu_r_vis * np.cos(theta)
my = cy + mu_r_vis * np.sin(theta) * 0.28
ax.plot(mx, my, color=CYAN, linewidth=2.5, linestyle='-', zorder=4, alpha=0.8)
ax.scatter([cx + mu_r_vis], [cy], s=120, color=CYAN,
           edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(0.35, -0.20, 'Muon orbit\n(deep interaction)\nr \u2248 0.842 fm reading',
        fontsize=10, color=CYAN, fontweight='bold', ha='left')

# Tau prediction
tau_r_vis = 0.08
tx = cx + tau_r_vis * np.cos(theta)
ty = cy + tau_r_vis * np.sin(theta) * 0.28
ax.plot(tx, ty, color=GOLD, linewidth=2, linestyle='--', zorder=4, alpha=0.6)
ax.text(0.15, -0.12, 'Tau orbit\n(deepest \u2014 predicted)\nr < 0.842 fm',
        fontsize=9, color=GOLD, fontweight='bold', ha='left')

# Depth arrow
ax.annotate('', xy=(0, 0), xytext=(0, 0.72),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2, linestyle='--'))
ax.text(-0.12, 0.45, 'Interaction\nDepth', fontsize=10, color=WHITE,
        ha='center', rotation=90, style='italic')

# Interior / exterior labels
ax.text(0.0, -0.75, 'INTERIOR: coherence dominates\n(quarks asymptotically free)',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold', alpha=0.8)
ax.text(0.0, -0.90, 'EXTERIOR: confinement dominates\n(proton appears as point particle)',
        fontsize=10, color=DIM, ha='center')

ax.set_title('Proton as Structured Vortex: Probe Depth Determines Reading',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys1_04_proton_probe_depth.png')


# ================================================================
# FIG 5: MASS-IS-INERTIA PRECISION HISTORY
# Type: Scale/Landscape (Type 2)
# Shows: Century of convergence from 10^-8 to 10^-15 on log scale.
# The relentless narrowing toward identity.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(PAN)

experiments = [
    (1922, 8,  'Eotvos\nexperiment', ORANGE),
    (1964, 11, 'Roll, Krotkov\n& Dicke', CYAN),
    (1999, 13, 'Baessler\net al.', GREEN),
    (2012, 13, 'LLR\n(Lunar Ranging)', BLUE),
    (2022, 15, 'MICROSCOPE\nsatellite', GOLD),
]

years = [e[0] for e in experiments]
precisions = [e[1] for e in experiments]

ax.plot(years, precisions, '-', color=DIM, linewidth=1.5, alpha=0.5, zorder=2)

for year, prec, label, color in experiments:
    ax.scatter([year], [prec], s=250, color=color,
               edgecolors=WHITE, linewidth=2, zorder=5)
    offset_y = 0.8 if prec < 14 else -1.0
    va_val = 'bottom' if offset_y > 0 else 'top'
    ax.annotate(label, xy=(year, prec),
                xytext=(year, prec + offset_y),
                fontsize=10, color=color, fontweight='bold',
                ha='center', va=va_val,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0))

for p in [8, 10, 12, 14]:
    ax.plot([1910, 2035], [p, p], color=DIM, linewidth=0.5, alpha=0.3, linestyle=':')

ax.plot([1910, 2035], [16.5, 16.5], color=GOLD, linewidth=1.5, alpha=0.4, linestyle='--')
ax.text(2025, 16.8, 'Identity: m_grav \u2261 m_inertial', fontsize=11,
        color=GOLD, ha='right', style='italic', fontweight='bold')

ax.annotate('', xy=(2028, 16.2), xytext=(2028, 8.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
ax.text(2030, 12.5, 'Converging\ntoward\nidentity', fontsize=10,
        color=WHITE, ha='left', va='center', style='italic')

ax.set_xlabel('Year', fontsize=12, color=SILVER)
ax.set_ylabel('Precision: agreement to 10^-n', fontsize=12, color=SILVER)
ax.set_title('The Equivalence Principle: A Century of Confirming Identity',
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.set_xlim(1910, 2040)
ax.set_ylim(6, 17.5)
ax.set_yticks([8, 10, 12, 14, 16])
ax.set_yticklabels(['10^-8', '10^-10', '10^-12', '10^-14', '10^-16'])
ax.tick_params(colors=DIM, labelsize=10)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.text(1960, 7.0, 'No deviation found at any precision.\nOne property, two labels.',
        fontsize=11, color=SILVER, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=SILVER, alpha=0.9))

save(fig, 'phys1_05_equivalence_precision.png')


# ================================================================
# FIG 6: BOUNDARY TRANSIT LIGHT PATH
# Type: Progression/Sequence (Type 7)
# Shows: CMB photon path through multiple boundaries to detector.
# The measurement pipeline as a physical journey.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
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

for label, color, x in stages:
    if label not in ('Intergalactic\nVoid', 'Detector', 'Source\n(CMB / SN)'):
        ax.plot([x, x], [2.5, 7.5], color=color, linewidth=3, alpha=0.6, zorder=3)
        for offset in [-0.03, 0.03]:
            ax.plot([x + offset, x + offset], [2.5, 7.5], color=color,
                    linewidth=1.5, alpha=0.2, zorder=2)

    ax.text(x, 8.3, label, fontsize=10, color=color, ha='center',
            va='center', fontweight='bold')

# CMB path
y_cmb = 5.8
ax.annotate('', xy=(9.1, y_cmb), xytext=(0.7, y_cmb),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2.5))
ax.text(5.0, y_cmb + 0.4, 'CMB photon: crosses ALL boundaries \u2192 H\u2080 = 67.4',
        fontsize=10, color=PURPLE, ha='center', fontweight='bold')

# Local path
y_local = 4.2
ax.annotate('', xy=(9.1, y_local), xytext=(5.5, y_local),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))
ax.text(7.3, y_local - 0.5, 'Local SN photon: crosses FEW boundaries \u2192 H\u2080 = 73.0',
        fontsize=10, color=ORANGE, ha='center', fontweight='bold')

# Crossing markers — CMB
for label, color, x in stages:
    if x > 0.6 and x < 9.2 and color != DIM:
        ax.scatter([x], [y_cmb], s=80, color=PURPLE, edgecolors=WHITE,
                   linewidth=1.5, zorder=6)

# Crossing markers — local
for label, color, x in stages:
    if x > 5.4 and x < 9.2 and color != DIM:
        ax.scatter([x], [y_local], s=80, color=ORANGE, edgecolors=WHITE,
                   linewidth=1.5, zorder=6)

ax.text(5.0, 1.2, 'Each boundary crossing is an unmodeled transformation.\n'
        'More crossings \u2192 more cumulative effect \u2192 lower measured H\u2080.',
        fontsize=11, color=SILVER, ha='center', style='italic')

ax.text(5.0, 9.5, 'Boundary Transit Paths: CMB vs. Local Measurements',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')

save(fig, 'phys1_06_transit_light_path.png')


# ================================================================
# FIG 7: VORTEX CROSS-SECTION
# Type: Geometric Cross-Section (Type 4)
# Shows: What a 3D field vortex looks like in cross-section.
# Interior coherence, boundary transition, exterior ambient.
# ================================================================

fig, ax = plt.subplots(figsize=(14, 14), facecolor=BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)

# Exterior — ambient field radial lines
for angle in np.linspace(0, 2 * np.pi, 24, endpoint=False):
    r_start = 0.85
    r_end = 1.05
    x0 = r_start * np.cos(angle)
    y0 = r_start * np.sin(angle)
    x1 = r_end * np.cos(angle)
    y1 = r_end * np.sin(angle)
    ax.plot([x0, x1], [y0, y1], color=DIM, linewidth=0.8, alpha=0.4, zorder=1)

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

# Boundary ring
boundary = plt.Circle((0, 0), 0.70, fill=False, edgecolor=GOLD,
                       linewidth=3, linestyle='-', zorder=4)
ax.add_patch(boundary)

# Transition zone glow
for dr in [0.01, 0.02, 0.03]:
    ring = plt.Circle((0, 0), 0.70 + dr, fill=False, edgecolor=GOLD,
                       linewidth=1, alpha=0.3 - dr * 8, zorder=3)
    ax.add_patch(ring)
    ring2 = plt.Circle((0, 0), 0.70 - dr, fill=False, edgecolor=GOLD,
                        linewidth=1, alpha=0.3 - dr * 8, zorder=3)
    ax.add_patch(ring2)

# Circulation arrows
for angle_start in [0, np.pi / 2, np.pi, 3 * np.pi / 2]:
    arc_r = 0.38
    theta_arr = np.linspace(angle_start, angle_start + np.pi / 3, 50)
    xa = arc_r * np.cos(theta_arr)
    ya = arc_r * np.sin(theta_arr)
    ax.plot(xa, ya, color=CYAN, linewidth=2, alpha=0.6, zorder=5)
    ax.annotate('', xy=(xa[-1], ya[-1]), xytext=(xa[-3], ya[-3]),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# Labels
ax.text(0, 0, 'INTERIOR\nCoherence\ndominates', fontsize=11, color=CYAN,
        ha='center', va='center', fontweight='bold')

ax.text(0, 0.90, 'BOUNDARY\n(soliton wall)', fontsize=11, color=GOLD,
        ha='center', fontweight='bold')

ax.text(0, -1.15, 'EXTERIOR: Ambient field dominates.\n'
        'Measurements from outside see different values than from inside.',
        fontsize=10, color=SILVER, ha='center', style='italic')

# Property boxes
props = [
    (-1.0, 1.0, 'Inertia = pattern\nresistance to disruption', MAG),
    (1.0, 1.0, 'Harmonic modes\n\u2192 quantum numbers', GREEN),
    (-1.0, -0.85, 'Spin = rotational\nmode of vortex', ORANGE),
    (1.0, -0.85, 'Boundary = where\nreadings diverge', GOLD),
]

for x, y, text, color in props:
    ax.text(x, y, text, fontsize=9, color=color, ha='center', va='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8))

ax.set_title('3D Field Vortex: Cross-Section of a Particle',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys1_07_vortex_cross_section.png')


# ================================================================
# FIG 8: PHYS-1 IDENTITY CARD
# Type: Identity Card (Type 8)
# Shows: Visual anchor — the vortex with key properties,
# connections to anomalies, and the central claim.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Central vortex
vcx, vcy = 3.2, 5.5
vortex_r = 1.4

n_v = 20
for i in range(n_v, 0, -1):
    r = vortex_r * (i / float(n_v))
    wave = 0.5 + 0.5 * np.sin(i * np.pi / 3.0)
    alpha_val = 0.03 + 0.10 * wave * (1.0 - i / float(n_v))
    color = CYAN if wave > 0.5 else BLUE
    circle = plt.Circle((vcx, vcy), r, fill=True, facecolor=color,
                         alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(circle)

boundary = plt.Circle((vcx, vcy), vortex_r, fill=False, edgecolor=GOLD,
                       linewidth=3, zorder=4)
ax.add_patch(boundary)

ax.text(vcx, vcy, 'Coherent\nField\nVortex', fontsize=12, color=WHITE,
        ha='center', va='center', fontweight='bold')

# Properties radiating out
connections = [
    (vcx - 2.0, vcy + 2.0, 'MASS = INERTIA', 'Pattern resistance\nto disruption',
     'F = ma defines inertia\nm_grav = m_inertial to 10^-15', MAG),
    (vcx + 2.0, vcy + 2.0, 'QUANTUM NUMBERS', 'Harmonic modes\nof standing wave',
     'Discrete, integer-indexed\nShell structure follows', GREEN),
    (vcx - 2.2, vcy - 2.2, 'BOUNDARY', 'Inside \u2260 Outside\nreadings',
     'GR: equivalence principle\nQCD: confinement\nQED: running \u03b1', GOLD),
    (vcx + 2.2, vcy - 2.2, 'TRANSIT', 'Light crossing\nboundaries',
     'Hubble tension: 9%\nMore transits \u2192 lower H\u2080', PURPLE),
]

for px, py, title, subtitle, detail, color in connections:
    angle = np.arctan2(py - vcy, px - vcx)
    edge_x = vcx + vortex_r * np.cos(angle) * 1.08
    edge_y = vcy + vortex_r * np.sin(angle) * 1.08
    ax.annotate('', xy=(px, py), xytext=(edge_x, edge_y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    ax.text(px, py, '%s\n%s' % (title, subtitle), fontsize=10,
            color=color, ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color, alpha=0.9))
    ax.text(px, py - 0.9, detail, fontsize=8, color=SILVER, ha='center', va='top')

# Right side — three anomalies
ax.text(8.0, 9.2, 'THREE ANOMALIES', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')
ax.text(8.0, 8.7, 'Each correlates with boundary\ndepth or transit count',
        fontsize=9, color=SILVER, ha='center')

anomalies = [
    (8.0, 7.5, 'HUBBLE TENSION', '67.4 vs 73.0 km/s/Mpc\nTransit count difference', PURPLE),
    (8.0, 5.5, 'PROTON RADIUS', '0.842 vs 0.877 fm\nProbe depth difference', CYAN),
    (8.0, 3.5, 'MUON g\u22122', '~4.2\u03c3 discrepancy\nVacuum interaction depth', MAG),
]

for ax_x, ax_y, title, detail, color in anomalies:
    ax.text(ax_x, ax_y, title, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(ax_x, ax_y - 0.6, detail, fontsize=9, color=SILVER, ha='center')

# Bottom banner
ax.text(5.0, 0.7, 'HOWL-PHYS-1: The Inertial Vortex', fontsize=16,
        color=GOLD, ha='center', fontweight='bold')
ax.text(5.0, 0.2, 'Current physics is incomplete at one point: '
        'the coherent vortex boundary as an unmodeled measurement element.',
        fontsize=10, color=SILVER, ha='center', style='italic')

ax.set_title('PHYS-1 Identity Card', fontsize=15, fontweight='bold',
             color=WHITE, pad=20)

save(fig, 'phys1_08_identity_card.png')


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
print("Placement table:")
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
