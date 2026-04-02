#!/usr/bin/env python3
"""
Soliton Hierarchy Diagrams
===========================
Nested sphere/torus boundary structure from galactic to biological scale.
Output: PNG files to /mnt/user-data/outputs/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch
import numpy as np
import os

OUT = "./"
os.makedirs(OUT, exist_ok=True)

# Style
DARK_BG = '#0d1117'
SPHERE_COLOR = '#58a6ff'
TORUS_COLOR = '#f0883e'
WEAK_COLOR = '#8b949e'
TEXT_COLOR = '#e6edf3'
ACCENT = '#7ee787'
ANTI_COLOR = '#f85149'

def setup_fig(title, figsize=(14, 10)):
    fig, ax = plt.subplots(1, 1, figsize=figsize, facecolor=DARK_BG)
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, color=TEXT_COLOR, fontsize=16, fontweight='bold', pad=15)
    return fig, ax

def draw_sphere(ax, cx, cy, r, label='', color=SPHERE_COLOR, alpha=0.3, lw=2):
    circle = Circle((cx, cy), r, fill=True, facecolor=color, 
                     edgecolor=color, alpha=alpha, linewidth=lw)
    ax.add_patch(circle)
    circle2 = Circle((cx, cy), r, fill=False, edgecolor=color, 
                      linewidth=lw, alpha=0.8)
    ax.add_patch(circle2)
    if label:
        ax.text(cx, cy + r + 0.15, label, ha='center', va='bottom',
                color=color, fontsize=8, fontweight='bold')

def draw_torus_cross(ax, cx, cy, R, r, label='', color=TORUS_COLOR, alpha=0.25):
    """Draw torus as two circles (cross-section view) with connecting arcs."""
    # Left circle of cross-section
    c1 = Circle((cx - R, cy), r, fill=True, facecolor=color, alpha=alpha)
    ax.add_patch(c1)
    c1b = Circle((cx - R, cy), r, fill=False, edgecolor=color, linewidth=2, alpha=0.8)
    ax.add_patch(c1b)
    # Right circle
    c2 = Circle((cx + R, cy), r, fill=True, facecolor=color, alpha=alpha)
    ax.add_patch(c2)
    c2b = Circle((cx + R, cy), r, fill=False, edgecolor=color, linewidth=2, alpha=0.8)
    ax.add_patch(c2b)
    # Connect top and bottom with dashed arcs (suggesting the torus body)
    theta = np.linspace(0, np.pi, 60)
    xt = cx + R * np.cos(theta)
    yt_top = cy + r + 0.15 * np.sin(theta) * R
    yt_bot = cy - r - 0.15 * np.sin(theta) * R
    ax.plot(xt, yt_top, '--', color=color, alpha=0.5, linewidth=1)
    ax.plot(xt, yt_bot, '--', color=color, alpha=0.5, linewidth=1)
    if label:
        ax.text(cx, cy + r + 0.4, label, ha='center', va='bottom',
                color=color, fontsize=8, fontweight='bold')

def draw_torus_topdown(ax, cx, cy, R, r, label='', color=TORUS_COLOR, alpha=0.25):
    """Draw torus from above — two concentric circles (outer and inner edge)."""
    outer = Circle((cx, cy), R + r, fill=False, edgecolor=color, linewidth=2, alpha=0.8)
    inner = Circle((cx, cy), R - r, fill=False, edgecolor=color, linewidth=2, 
                   linestyle='--', alpha=0.5)
    ax.add_patch(outer)
    ax.add_patch(inner)
    # Fill the annulus
    theta = np.linspace(0, 2*np.pi, 100)
    x_out = cx + (R + r) * np.cos(theta)
    y_out = cy + (R + r) * np.sin(theta)
    x_in = cx + (R - r) * np.cos(theta)
    y_in = cy + (R - r) * np.sin(theta)
    ax.fill(np.concatenate([x_out, x_in[::-1]]),
            np.concatenate([y_out, y_in[::-1]]),
            color=color, alpha=alpha)
    if label:
        ax.text(cx, cy + R + r + 0.2, label, ha='center', va='bottom',
                color=color, fontsize=8, fontweight='bold')

def draw_dot(ax, cx, cy, label='', color=TEXT_COLOR, size=30):
    ax.scatter([cx], [cy], s=size, color=color, zorder=10)
    if label:
        ax.text(cx + 0.15, cy, label, ha='left', va='center',
                color=color, fontsize=7)

def draw_arrow(ax, x1, y1, x2, y2, color=WEAK_COLOR):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

def add_legend_box(ax, x, y, items, title=''):
    """items = list of (color, label) tuples"""
    if title:
        ax.text(x, y, title, color=TEXT_COLOR, fontsize=9, fontweight='bold')
        y -= 0.35
    for color, label in items:
        ax.plot([x, x+0.3], [y, y], color=color, linewidth=3)
        ax.text(x + 0.4, y, label, color=TEXT_COLOR, fontsize=7, va='center')
        y -= 0.3


# ================================================================
# DIAGRAM 1: The Full Hierarchy (Overview)
# ================================================================

fig, ax = setup_fig('Soliton Hierarchy: Nested Boundary Structure', figsize=(14, 10))

# Level 0: Galactic halo (sphere) — outermost
draw_sphere(ax, 7, 5, 4.5, 'Galactic Halo (Sphere, R₂)', SPHERE_COLOR, 0.08)

# Level 0b: Galactic disk (torus) — inside halo
draw_torus_topdown(ax, 7, 5, 3.2, 0.6, 'Galactic Disk (Torus, R₄)', TORUS_COLOR, 0.12)

# Level 1: Solar Hill sphere (sphere)
draw_sphere(ax, 7, 5, 2.0, 'Solar Hill Sphere (Sphere, R₂)', SPHERE_COLOR, 0.12)

# Level 2: Solar system disk (torus) — inside Hill sphere
draw_torus_topdown(ax, 7, 5, 1.4, 0.25, 'Solar System Disk (Torus, R₄)', TORUS_COLOR, 0.2)

# Level 3: Sun at center
draw_dot(ax, 7, 5, '☉ Sun', ACCENT, 80)

# Level 4: Planets as dots on the disk
planet_angles = [0.3, 0.8, 1.3, 1.9, 2.8, 3.5, 4.2, 5.0]
planet_radii = [0.4, 0.55, 0.7, 0.9, 1.15, 1.3, 1.45, 1.6]
planet_names = ['Me', 'V', 'E', 'Ma', 'J', 'S', 'U', 'N']
for angle, r, name in zip(planet_angles, planet_radii, planet_names):
    px = 7 + r * np.cos(angle)
    py = 5 + r * np.sin(angle)
    s = 40 if name in ['J', 'S'] else 15
    draw_dot(ax, px, py, name, TEXT_COLOR, s)

# Annotations
ax.text(0.3, 9.2, 'GEOMETRY KEY:', color=TEXT_COLOR, fontsize=10, fontweight='bold')
add_legend_box(ax, 0.3, 8.8, [
    (SPHERE_COLOR, 'Sphere → R₂ = π/4 corrections'),
    (TORUS_COLOR, 'Torus → R₄ = π²/32 corrections'),
    (ACCENT, 'High-coherence soliton (star/planet)'),
    (WEAK_COLOR, 'Low-coherence / diffuse'),
], '')

ax.text(0.3, 6.8, 'NESTING ORDER:', color=TEXT_COLOR, fontsize=9, fontweight='bold')
levels = [
    'L0: Galactic Halo (sphere in cluster)',
    'L0b: Galactic Disk (torus in halo)',
    'L1: Solar Hill Sphere (sphere in disk)',
    'L2: Solar System Disk (torus in Hill sphere)',
    'L3: Sun (sphere at center)',
    'L4: Planets (spheres on disk)',
    'L5: Moons (spheres around planets)',
    'L6: Belts/Rings (tori around planets)',
]
for i, line in enumerate(levels):
    ax.text(0.3, 6.3 - i*0.32, line, color=TEXT_COLOR, fontsize=7)

ax.text(0.3, 3.5, 'Each level contributes its', color=TEXT_COLOR, fontsize=7)
ax.text(0.3, 3.2, 'geometry\'s rational correction.', color=TEXT_COLOR, fontsize=7)
ax.text(0.3, 2.8, 'Composite = product of all levels.', color=ACCENT, fontsize=7, fontweight='bold')
ax.text(0.3, 2.4, 'PSLQ null = composition signature.', color=ANTI_COLOR, fontsize=7, fontweight='bold')

fig.savefig(os.path.join(OUT, 'soliton_01_hierarchy_overview.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_01_hierarchy_overview.png")


# ================================================================
# DIAGRAM 2: Sphere-in-Torus-in-Sphere Nesting (Cross Section)
# ================================================================

fig, ax = setup_fig('Cross-Section: Sphere in Torus in Sphere', figsize=(14, 8))

# Galactic halo (large sphere)
draw_sphere(ax, 7, 4.5, 3.8, '', SPHERE_COLOR, 0.06)
ax.text(7, 8.5, 'GALACTIC HALO', color=SPHERE_COLOR, fontsize=11, 
        ha='center', fontweight='bold')
ax.text(7, 8.1, 'Sphere: modulus 8R₂ × scale', color=SPHERE_COLOR, 
        fontsize=8, ha='center')

# Galactic disk (torus cross-section)
draw_torus_cross(ax, 7, 4.5, 2.5, 0.7, '', TORUS_COLOR, 0.15)
ax.text(7, 5.7, 'GALACTIC DISK', color=TORUS_COLOR, fontsize=10, 
        ha='center', fontweight='bold')
ax.text(7, 5.35, 'Torus: R₄ content through T² = S¹×S¹', color=TORUS_COLOR, 
        fontsize=7, ha='center')

# Solar system Hill sphere (sphere inside left lobe of torus)
draw_sphere(ax, 4.5, 4.5, 0.5, '', ACCENT, 0.2)
ax.text(4.5, 5.15, 'Solar Hill', color=ACCENT, fontsize=7, ha='center')
ax.text(4.5, 4.9, 'Sphere', color=ACCENT, fontsize=7, ha='center')

# Sun dot
draw_dot(ax, 4.5, 4.5, '☉', ACCENT, 40)

# Arrow showing "through the hole"
ax.annotate('', xy=(9.5, 4.5), xytext=(4.5, 4.5),
            arrowprops=dict(arrowstyle='->', color=ANTI_COLOR, lw=2, 
                           linestyle='--'))
ax.text(7, 4.1, 'THROUGH THE HOLE', color=ANTI_COLOR, fontsize=8, 
        ha='center', fontweight='bold')
ax.text(7, 3.8, 'Fewer boundaries → higher H₀', color=ANTI_COLOR, 
        fontsize=7, ha='center')

# Arrow showing "around the ring"
theta_arc = np.linspace(-0.3, np.pi + 0.3, 80)
x_arc = 7 + 3.0 * np.cos(theta_arc)
y_arc = 4.5 + 1.5 * np.sin(theta_arc)
ax.plot(x_arc, y_arc, '--', color=ACCENT, linewidth=2, alpha=0.7)
ax.annotate('', xy=(x_arc[-1], y_arc[-1]), xytext=(x_arc[-2], y_arc[-2]),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))
ax.text(7, 6.3, 'AROUND THE RING', color=ACCENT, fontsize=8, 
        ha='center', fontweight='bold')
ax.text(7, 6.0, 'More boundaries → lower H₀', color=ACCENT, 
        fontsize=7, ha='center')

# R_n annotations
ax.text(11.5, 7.5, 'CORRECTION FACTORS:', color=TEXT_COLOR, fontsize=9, fontweight='bold')
ax.text(11.5, 7.0, 'Sphere → R₂ = π/4', color=SPHERE_COLOR, fontsize=8)
ax.text(11.5, 6.6, 'Torus → R₄ = π²/32', color=TORUS_COLOR, fontsize=8)
ax.text(11.5, 6.2, 'Through hole: r_torus²', color=ANTI_COLOR, fontsize=8)
ax.text(11.5, 5.8, 'Around ring: r_torus^N', color=ACCENT, fontsize=8)
ax.text(11.5, 5.2, 'Hole filled by parent\'s', color=TEXT_COLOR, fontsize=7)
ax.text(11.5, 4.9, 'interior regime (halo field)', color=TEXT_COLOR, fontsize=7)

# Bottom: the nesting formula
ax.text(7, 1.2, 'H₀(direction) = H₀(local) × Π_levels r_level(geometry, angle, path)', 
        color=TEXT_COLOR, fontsize=9, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#161b22', edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'soliton_02_cross_section.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_02_cross_section.png")


# ================================================================
# DIAGRAM 3: The Solar System Mode Structure
# ================================================================

fig, ax = setup_fig('Solar System: Composite Soliton Mode Structure', figsize=(14, 10))

# Central sun
draw_sphere(ax, 7, 5, 0.4, '', '#ffcc00', 0.5)
ax.text(7, 5, '☉', color='#0d1117', fontsize=14, ha='center', va='center', fontweight='bold')

# Planetary orbits as concentric circles with mode labels
orbit_data = [
    (0.8,  'Mercury', 'n=−∞', '#adb5bd'),
    (1.2,  'Venus',   'n=0',   '#adb5bd'),
    (1.6,  'Earth',   'n=1',   '#58a6ff'),
    (2.1,  'Mars',    'n=2',   '#adb5bd'),
    (2.7,  'Ceres*',  'n=3',   WEAK_COLOR),
    (3.4,  'Jupiter', 'n=4',   TORUS_COLOR),
    (4.0,  'Saturn',  'n=5',   TORUS_COLOR),
    (4.5,  'Uranus',  'n=6',   '#adb5bd'),
]

for r, name, mode, color in orbit_data:
    orbit = Circle((7, 5), r, fill=False, edgecolor=color, linewidth=1, 
                   alpha=0.4, linestyle='-')
    ax.add_patch(orbit)
    angle = 0.4 + r * 0.3
    px = 7 + r * np.cos(angle)
    py = 5 + r * np.sin(angle)
    ax.scatter([px], [py], s=20 if name not in ['Jupiter','Saturn'] else 50, 
              color=color, zorder=10)
    ax.text(px + 0.15, py + 0.1, f'{name} ({mode})', color=color, fontsize=7)

# Titius-Bode annotation
ax.text(0.3, 9.3, 'TITIUS-BODE AS MODE SPECTRUM', color=TEXT_COLOR, 
        fontsize=10, fontweight='bold')
ax.text(0.3, 8.8, 'aₙ ≈ 0.4 + 0.3 × 2ⁿ AU', color=ACCENT, fontsize=9)
ax.text(0.3, 8.4, 'Factor of 2 = octave spacing', color=TEXT_COLOR, fontsize=8)
ax.text(0.3, 8.0, 'Same binary arithmetic as MATH-4', color=TEXT_COLOR, fontsize=8)

# Mode structure annotations
ax.text(0.3, 7.2, 'COMPOSITE POTENTIAL:', color=TEXT_COLOR, fontsize=9, fontweight='bold')
components = [
    ('Solar monopole: V ∝ -1/r', ACCENT, '→ n² modes (Bohr-like)'),
    ('Disk potential: V ∝ ln(r)', TORUS_COLOR, '→ 2ⁿ modes (Bessel-like)'),
    ('Hill sphere cutoff: r < r_H', SPHERE_COLOR, '→ modifies outer modes'),
    ('Jupiter perturbation:', TORUS_COLOR, '→ Kirkwood gaps (nodes)'),
    ('Galactic tide:', WEAK_COLOR, '→ outer boundary condition'),
]
for i, (label, color, effect) in enumerate(components):
    ax.text(0.3, 6.7 - i*0.4, label, color=color, fontsize=7)
    ax.text(0.3, 6.45 - i*0.4, '  ' + effect, color=WEAK_COLOR, fontsize=6)

# Kirkwood gaps annotation
ax.text(0.3, 4.3, 'KIRKWOOD GAPS = STANDING WAVE NODES', color=ANTI_COLOR, 
        fontsize=8, fontweight='bold')
gaps = ['3:1 at 2.50 AU', '5:2 at 2.82 AU', '7:3 at 2.95 AU', '2:1 at 3.27 AU']
for i, g in enumerate(gaps):
    ax.text(0.3, 3.9 - i*0.25, f'  {g}', color=ANTI_COLOR, fontsize=7)

# Neptune failure annotation
ax.text(0.3, 2.6, 'NEPTUNE (n=7): 30.1 AU vs predicted 38.8', color=ANTI_COLOR, fontsize=7)
ax.text(0.3, 2.3, '→ MODE FAMILY TRANSITION at Kuiper belt', color=ANTI_COLOR, fontsize=7)
ax.text(0.3, 2.0, '  Inner: disk modes (Bessel)', color=TORUS_COLOR, fontsize=7)
ax.text(0.3, 1.7, '  Outer: spherical modes (Hill sphere)', color=SPHERE_COLOR, fontsize=7)

# Bessel zero note
ax.text(0.3, 1.1, 'BESSEL ZEROS: Independent of Q335 basis', color=WEAK_COLOR, fontsize=7)
ax.text(0.3, 0.8, '82/82 PSLQ null → new transcendental class', color=WEAK_COLOR, fontsize=7)
ax.text(0.3, 0.5, 'Composite modes ≠ any single class', color=ACCENT, fontsize=7, fontweight='bold')

fig.savefig(os.path.join(OUT, 'soliton_03_solar_modes.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_03_solar_modes.png")


# ================================================================
# DIAGRAM 4: The Coherence Spectrum
# ================================================================

fig, ax = setup_fig('Soliton Coherence Spectrum: Maximum to Anti', figsize=(14, 8))

# Horizontal bar showing coherence from left (max) to right (anti)
bar_y = 5
bar_x0, bar_x1 = 1, 13
ax.plot([bar_x0, bar_x1], [bar_y, bar_y], color=WEAK_COLOR, linewidth=3)

# Coherence labels along the bar
categories = [
    (1.5, 'BLACK\nHOLE', ANTI_COLOR, 'r = 0\n(100% absorb)', 10),
    (3.0, 'NEUTRON\nSTAR', '#ff7b72', 'r ≈ 0\n(near-max)', 8),
    (4.5, 'STAR', ACCENT, 'r < 1\n(moderate)', 8),
    (5.8, 'PLANET', SPHERE_COLOR, 'r < 1\n(small)', 8),
    (7.0, 'GALAXY', TORUS_COLOR, 'r < 1\n(collective)', 8),
    (8.3, 'CLUSTER', '#d2a8ff', 'r < 1\n(collective)', 8),
    (9.5, 'NEBULA', WEAK_COLOR, 'r ≈ 1\n(weak)', 8),
    (10.8, 'FILAMENT', WEAK_COLOR, 'r ≈ 1\n(standing\nwave)', 7),
    (12.2, 'VOID', ANTI_COLOR, 'r > 1?\n(anti)', 8),
]

for x, label, color, correction, fs in categories:
    ax.scatter([x], [bar_y], s=100, color=color, zorder=10)
    ax.text(x, bar_y + 0.6, label, color=color, fontsize=fs, 
            ha='center', va='bottom', fontweight='bold')
    ax.text(x, bar_y - 0.5, correction, color=WEAK_COLOR, fontsize=6, 
            ha='center', va='top')

# Arrows
ax.text(1.0, bar_y - 1.5, '← MAXIMUM COHERENCE', color=ACCENT, fontsize=8)
ax.text(10.5, bar_y - 1.5, 'ANTI-COHERENCE →', color=ANTI_COLOR, fontsize=8)
ax.text(6.5, bar_y - 1.5, 'DECREASING', color=WEAK_COLOR, fontsize=8, ha='center')

# Top section: geometry by type
ax.text(1, 7.8, 'BOUNDARY GEOMETRY:', color=TEXT_COLOR, fontsize=10, fontweight='bold')

geom_data = [
    (2, 'Sphere (S²)', SPHERE_COLOR, 'R₂ corrections', '○'),
    (5, 'Torus (T²)', TORUS_COLOR, 'R₄ corrections', '◎'),
    (8, 'Oblate (S² def)', '#d2a8ff', 'R₂ × eccentricity', '⬭'),
    (11, 'Irregular', WEAK_COLOR, 'Pure rational?', '◇'),
]

for x, label, color, rn, symbol in geom_data:
    ax.text(x, 7.3, symbol, color=color, fontsize=16, ha='center')
    ax.text(x, 6.8, label, color=color, fontsize=8, ha='center')
    ax.text(x, 6.5, rn, color=WEAK_COLOR, fontsize=7, ha='center')

# Bottom: the per-transit correction function
ax.text(7, 2.5, 'Per-transit correction r(C) = function of coherence C',
        color=TEXT_COLOR, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22', edgecolor=ACCENT))
ax.text(7, 1.8, 'r(C_max) = 0  |  r(0) = 1  |  r(anti) > 1?',
        color=WEAK_COLOR, fontsize=8, ha='center')
ax.text(7, 1.3, 'Cumulative: H₀(obs) = H₀(local) × Π r(Cᵢ)',
        color=ACCENT, fontsize=9, ha='center', fontweight='bold')

fig.savefig(os.path.join(OUT, 'soliton_04_coherence_spectrum.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_04_coherence_spectrum.png")


# ================================================================
# DIAGRAM 5: The Three Orientation Tracks
# ================================================================

fig, axes = plt.subplots(1, 3, figsize=(14, 5), facecolor=DARK_BG)

for ax in axes:
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

# Track 1: Universal alignment
ax = axes[0]
ax.set_title('Track 1: Universal\nAlignment', color=ACCENT, fontsize=10, fontweight='bold')
# Parent torus (top-down view)
parent = Circle((0, 0), 1.2, fill=False, edgecolor=TORUS_COLOR, linewidth=2, alpha=0.5)
ax.add_patch(parent)
inner = Circle((0, 0), 0.6, fill=False, edgecolor=TORUS_COLOR, linewidth=1, 
               linestyle='--', alpha=0.3)
ax.add_patch(inner)
# Children all aligned (horizontal bars)
for r in [0.7, 0.85, 1.0]:
    for angle in [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3]:
        cx = r * np.cos(angle)
        cy = r * np.sin(angle)
        ax.plot([cx-0.08, cx+0.08], [cy, cy], color=ACCENT, linewidth=2)
ax.text(0, -1.4, 'All orbits parallel\nχ/T_eff → ∞', color=WEAK_COLOR, fontsize=7, ha='center')

# Track 2: Preferred with perturbations
ax = axes[1]
ax.set_title('Track 2: Preferred +\nPerturbations', color=SPHERE_COLOR, fontsize=10, fontweight='bold')
parent = Circle((0, 0), 1.2, fill=False, edgecolor=TORUS_COLOR, linewidth=2, alpha=0.5)
ax.add_patch(parent)
inner = Circle((0, 0), 0.6, fill=False, edgecolor=TORUS_COLOR, linewidth=1, 
               linestyle='--', alpha=0.3)
ax.add_patch(inner)
np.random.seed(42)
for r in [0.7, 0.85, 1.0]:
    for angle in [0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3]:
        cx = r * np.cos(angle)
        cy = r * np.sin(angle)
        tilt = np.random.normal(0, 0.15)  # small random tilt
        dx = 0.08 * np.cos(tilt)
        dy = 0.08 * np.sin(tilt)
        ax.plot([cx-dx, cx+dx], [cy-dy, cy+dy], color=SPHERE_COLOR, linewidth=2)
ax.text(0, -1.4, 'Most aligned, some tilted\nχ/T_eff ~ 1-10', color=WEAK_COLOR, fontsize=7, ha='center')

# Track 3: No preferred alignment
ax = axes[2]
ax.set_title('Track 3: No Preferred\nAlignment', color=ANTI_COLOR, fontsize=10, fontweight='bold')
parent = Circle((0, 0), 1.2, fill=False, edgecolor=SPHERE_COLOR, linewidth=2, alpha=0.5)
ax.add_patch(parent)
# Note: parent is SPHERE (no preferred axis)
np.random.seed(7)
for r in [0.5, 0.7, 0.9]:
    for angle in np.random.uniform(0, 2*np.pi, 5):
        cx = r * np.cos(angle)
        cy = r * np.sin(angle)
        tilt = np.random.uniform(0, np.pi)
        dx = 0.08 * np.cos(tilt)
        dy = 0.08 * np.sin(tilt)
        ax.plot([cx-dx, cx+dx], [cy-dy, cy+dy], color=ANTI_COLOR, linewidth=2)
ax.text(0, -1.4, 'Random orientations\nSpherical parent: χ = 0', color=WEAK_COLOR, fontsize=7, ha='center')

fig.suptitle('The Three Orientation Tracks', color=TEXT_COLOR, fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT, 'soliton_05_orientation_tracks.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_05_orientation_tracks.png")


# ================================================================
# DIAGRAM 6: The Composite Mode Problem (Bessel + Spherical)
# ================================================================

fig, ax = setup_fig('Why PSLQ Fails: Hierarchical Composition of Transcendental Classes', 
                    figsize=(14, 8))

# Left column: individual levels with their transcendental class
levels = [
    ('Level 0: Galactic Disk', 'Bessel functions J_n', TORUS_COLOR, 'R₄ + Bessel zeros'),
    ('Level 1: Hill Sphere', 'Spherical harmonics Y_l^m', SPHERE_COLOR, 'R₂ + integers'),
    ('Level 2: Solar Disk', 'Bessel functions J_n', TORUS_COLOR, 'R₄ + Bessel zeros'),
    ('Level 3: Solar Monopole', '1/r potential → n²', ACCENT, 'R₂ + integers²'),
    ('Level 4: Jupiter', 'Resonance ratios p/q', TORUS_COLOR, 'Pure rationals'),
]

x_left = 1
for i, (level, modes, color, transcendental) in enumerate(levels):
    y = 7.5 - i * 1.3
    ax.text(x_left, y, level, color=color, fontsize=9, fontweight='bold')
    ax.text(x_left + 0.2, y - 0.3, f'Modes: {modes}', color=WEAK_COLOR, fontsize=7)
    ax.text(x_left + 0.2, y - 0.55, f'Content: {transcendental}', color=WEAK_COLOR, fontsize=7)
    # Arrow to composition
    ax.annotate('', xy=(8.5, 4.5), xytext=(5.5, y - 0.2),
                arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.4))

# Right: the composite
ax.text(8.5, 6.5, 'COMPOSITE', color=TEXT_COLOR, fontsize=12, fontweight='bold')
ax.text(8.5, 6.0, 'Product of all levels:', color=TEXT_COLOR, fontsize=9)
ax.text(8.5, 5.5, 'f = Bessel × Spherical × 1/r × Resonance', 
        color=ACCENT, fontsize=8)
ax.text(8.5, 5.0, '= new transcendental class', color=ACCENT, fontsize=9, fontweight='bold')
ax.text(8.5, 4.5, 'NOT in Q335 basis', color=ANTI_COLOR, fontsize=9, fontweight='bold')
ax.text(8.5, 4.0, 'NOT decomposable by PSLQ', color=ANTI_COLOR, fontsize=8)

# Bottom box
ax.text(7, 2.0, 'Each level has exact rational structure (fractions).',
        color=TEXT_COLOR, fontsize=9, ha='center')
ax.text(7, 1.5, 'The COMPOSITION across levels produces a transcendental',
        color=TEXT_COLOR, fontsize=9, ha='center')
ax.text(7, 1.0, 'that no single transcendental class can describe.',
        color=ACCENT, fontsize=9, ha='center', fontweight='bold')
ax.text(7, 0.4, 'This is why 82/82 PSLQ tests return NULL.',
        color=ANTI_COLOR, fontsize=9, ha='center', fontweight='bold')

# Box around the composite
rect = mpatches.FancyBboxPatch((8.2, 3.7), 5, 3.2, 
                                boxstyle="round,pad=0.2",
                                facecolor='#161b22', edgecolor=ACCENT, linewidth=2)
ax.add_patch(rect)

fig.savefig(os.path.join(OUT, 'soliton_06_composite_modes.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_06_composite_modes.png")


# ================================================================
# DIAGRAM 7: R₂ vs R₄ — Which Geometry Produces Which Correction
# ================================================================

fig, ax = setup_fig('Geometry → R_n: Which Boundary Produces Which Correction', figsize=(14, 8))

# Left: Sphere
cx_s, cy_s = 3.5, 5.5
draw_sphere(ax, cx_s, cy_s, 1.8, '', SPHERE_COLOR, 0.15)
ax.text(cx_s, cy_s, 'S²', color=SPHERE_COLOR, fontsize=20, ha='center', va='center',
        fontweight='bold')
ax.text(cx_s, cy_s + 2.3, 'SPHERE', color=SPHERE_COLOR, fontsize=12, 
        ha='center', fontweight='bold')
ax.text(cx_s, cy_s - 2.3, 'Cross-section: πr² = 4R₂r²', color=TEXT_COLOR, 
        fontsize=8, ha='center')
ax.text(cx_s, cy_s - 2.7, 'Modulus: 2π = 8R₂', color=TEXT_COLOR, fontsize=8, ha='center')
ax.text(cx_s, cy_s - 3.1, 'VP step: 1/(3π) = 1/(12R₂)', color=TEXT_COLOR, 
        fontsize=8, ha='center')
ax.text(cx_s, cy_s - 3.6, 'R₂ = π/4 = 0.7854', color=ACCENT, fontsize=10, 
        ha='center', fontweight='bold')

# Right: Torus
cx_t, cy_t = 10.5, 5.5
draw_torus_topdown(ax, cx_t, cy_t, 1.3, 0.5, '', TORUS_COLOR, 0.15)
ax.text(cx_t, cy_t, 'T²', color=TORUS_COLOR, fontsize=20, ha='center', va='center',
        fontweight='bold')
ax.text(cx_t, cy_t + 2.3, 'TORUS', color=TORUS_COLOR, fontsize=12, 
        ha='center', fontweight='bold')
ax.text(cx_t, cy_t - 2.3, 'Volume: 2π²Rr² = 128R₄·Rr²', color=TEXT_COLOR, 
        fontsize=8, ha='center')
ax.text(cx_t, cy_t - 2.7, 'T² = S¹×S¹: two circles', color=TEXT_COLOR, 
        fontsize=8, ha='center')
ax.text(cx_t, cy_t - 3.1, 'R₂² = 2R₄ (product of periodicities)', color=TEXT_COLOR, 
        fontsize=8, ha='center')
ax.text(cx_t, cy_t - 3.6, 'R₄ = π²/32 = 0.3084', color=ACCENT, fontsize=10, 
        ha='center', fontweight='bold')

# Center: arrow showing the relationship
ax.text(7, 7.5, 'MATH-5 RULE', color=TEXT_COLOR, fontsize=10, ha='center', fontweight='bold')
ax.text(7, 7.0, 'R_n matches geometric dimension', color=TEXT_COLOR, fontsize=8, ha='center')
ax.text(7, 6.5, '2D operation → R₂', color=SPHERE_COLOR, fontsize=9, ha='center')
ax.text(7, 6.1, '4D operation → R₄', color=TORUS_COLOR, fontsize=9, ha='center')

# Bottom: examples
ax.text(1, 1.2, 'SPHERICAL BOUNDARIES:', color=SPHERE_COLOR, fontsize=8, fontweight='bold')
ax.text(1, 0.8, 'Hill spheres, VP clouds, halos, CMB', color=WEAK_COLOR, fontsize=7)

ax.text(8, 1.2, 'TOROIDAL BOUNDARIES:', color=TORUS_COLOR, fontsize=8, fontweight='bold')
ax.text(8, 0.8, 'Rings, belts, galactic disks, accretion disks', color=WEAK_COLOR, fontsize=7)

fig.savefig(os.path.join(OUT, 'soliton_07_R2_vs_R4.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_07_R2_vs_R4.png")


# ================================================================
# DIAGRAM 8: The Hubble Tension as Running Curve
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(12, 7), facecolor=DARK_BG)
ax.set_facecolor(DARK_BG)

# Data points
data = [
    (10, 73.0, 1.0, 'SH0ES\n(local SNe)'),
    (30, 73.3, 1.8, 'H0LiCOW\n(lensing)'),
    (100, 69.8, 1.7, 'TRGB'),
    (500, 67.4, 1.2, 'DES+BAO'),
    (2000, 67.4, 0.5, 'Planck CMB'),
]

for N, H0, err, label in data:
    ax.errorbar(N, H0, yerr=err, fmt='o', color=ACCENT, markersize=8, 
                capsize=4, capthick=1.5, elinewidth=1.5, zorder=10)
    ax.text(N * 1.15, H0 + 0.3, label, color=TEXT_COLOR, fontsize=8)

# Proposed running curve
N_curve = np.logspace(0.5, 3.5, 100)
r = 0.9992  # per-transit correction for N~100
H0_local = 73.2
H0_curve = H0_local * r**N_curve
ax.plot(N_curve, H0_curve, '-', color=TORUS_COLOR, linewidth=2, alpha=0.7,
        label='H₀(N) = H₀(0) × r^N')

# Constant lines
ax.axhline(y=73.0, color=ANTI_COLOR, linestyle=':', alpha=0.3, linewidth=1)
ax.axhline(y=67.4, color=SPHERE_COLOR, linestyle=':', alpha=0.3, linewidth=1)

ax.set_xscale('log')
ax.set_xlabel('Effective Boundary Transit Count N', color=TEXT_COLOR, fontsize=11)
ax.set_ylabel('H₀ (km/s/Mpc)', color=TEXT_COLOR, fontsize=11)
ax.set_title('Hubble Tension as Running Curve', color=TEXT_COLOR, fontsize=14, fontweight='bold')
ax.tick_params(colors=WEAK_COLOR)
ax.spines['bottom'].set_color(WEAK_COLOR)
ax.spines['left'].set_color(WEAK_COLOR)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(65, 76)
ax.legend(facecolor='#161b22', edgecolor=WEAK_COLOR, labelcolor=TEXT_COLOR, fontsize=9)

# Annotation
ax.text(3, 75, 'Not a tension between two values.\nA continuous running curve.', 
        color=ACCENT, fontsize=9, fontweight='bold')
ax.text(3, 74, f'Per-transit correction r ≈ {r}\n1 − r ≈ {1-r:.4f} ≈ 1/1250',
        color=WEAK_COLOR, fontsize=8)

fig.savefig(os.path.join(OUT, 'soliton_08_hubble_curve.png'), 
            dpi=150, bbox_inches='tight', facecolor=DARK_BG)
plt.close(fig)
print("Saved: soliton_08_hubble_curve.png")


print("\n=== ALL 8 DIAGRAMS SAVED ===")
print(f"Location: {OUT}/soliton_*.png")
