#!/usr/bin/env python3
"""
soliton_modulus_superset_diagrams.py

Diagrams for the Modulus Superset concept:
- Soliton boundaries as geometric stages in H₀ running
- Shells within boundaries
- The compound running curve
- Directional dependence
- VP running as prototype

Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch
import numpy as np
import os

OUT = "../figures"
os.makedirs(OUT, exist_ok=True)

# Style constants
BG = '#0d1117'
SPHERE = '#58a6ff'
TORUS = '#f0883e'
WEAK = '#8b949e'
TEXT = '#e6edf3'
ACCENT = '#7ee787'
RED = '#f85149'
PURPLE = '#d2a8ff'
YELLOW = '#ffcc00'


# ================================================================
# FIGURE 1: VP Running as Prototype — the template
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 7), facecolor=BG)
ax.set_facecolor(BG)

# Energy axis (log scale, in MeV)
thresholds = [
    (np.log10(0.511), 'm_e', ACCENT),
    (np.log10(105.66), r'm_$\mu$', ACCENT),
    (np.log10(1777), r'm_$\tau$', ACCENT),
    (np.log10(1273), 'm_c', TORUS),
    (np.log10(4183), 'm_b', TORUS),
    (np.log10(80369), 'M_W', YELLOW),
    (np.log10(172570), 'm_t', RED),
]

# Simulated alpha_em^-1 running (schematic, not exact)
E = np.linspace(-1, 5.5, 500)
alpha_inv = np.ones_like(E) * 137.036

# Piecewise running: each fermion adds a slope change
fermion_thresholds = [
    (np.log10(0.511), 0.30),   # electron
    (np.log10(105.66), 0.30),  # muon
    (np.log10(1273), 0.55),    # charm (3 colors * 4/9)
    (np.log10(1777), 0.30),    # tau
    (np.log10(4183), 0.15),    # bottom (3 colors * 1/9)
    (np.log10(80369), 0.8),    # W threshold (schematic)
    (np.log10(172570), 0.5),   # top
]

for i in range(len(E)):
    correction = 0
    for thresh, slope in fermion_thresholds:
        if E[i] > thresh:
            correction += slope * (E[i] - thresh)
    alpha_inv[i] = 137.036 - correction

ax.plot(E, alpha_inv, color=SPHERE, linewidth=2.5, zorder=5)

# Mark thresholds
for log_e, label, color in thresholds:
    ax.axvline(x=log_e, color=color, linestyle='--', alpha=0.4, linewidth=1)
    ax.text(log_e, 138.0, label, color=color, fontsize=7, ha='center',
            rotation=45)

# Mark the confinement wall
ax.axvspan(np.log10(300), np.log10(2000), alpha=0.15, color=RED)
ax.text(np.log10(800), 136.0, 'CONFINEMENT\nWALL', color=RED,
        fontsize=8, ha='center', fontweight='bold')

# Domain labels
domains = [
    (-0.5, 'Domain 1\ne only'),
    (1.5, 'Domain 2\ne + mu'),
    (3.3, 'Domain 5\n+tau'),
    (4.2, 'Domain 6\n+b'),
    (5.0, 'Domain 10\nFull SM'),
]
for x, label in domains:
    ax.text(x, 133.5, label, color=WEAK, fontsize=6, ha='center')

# Annotations
ax.text(0.5, 137.5, 'EACH DOMAIN = ONE GEOMETRIC STAGE',
        color=TEXT, fontsize=9, fontweight='bold')
ax.text(0.5, 137.0, 'Rule changes at each threshold (boundary)',
        color=WEAK, fontsize=7)
ax.text(0.5, 136.6, 'Running accumulates within each domain',
        color=WEAK, fontsize=7)

# Labels
ax.set_xlabel('log₁₀(Energy / MeV)', color=TEXT, fontsize=11)
ax.set_ylabel(r'$\alpha_{em}^{-1}$', color=TEXT, fontsize=12)
ax.set_title('VP Running as Prototype: Geometric Stages Between Thresholds',
             color=TEXT, fontsize=13, fontweight='bold')
ax.tick_params(colors=WEAK)
for spine in ax.spines.values():
    spine.set_color(WEAK)
ax.set_xlim(-1, 5.5)
ax.set_ylim(127, 138.5)

fig.savefig(os.path.join(OUT, 'modulus_01_vp_prototype.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_01_vp_prototype.png")


# ================================================================
# FIGURE 2: Shells Within a Single Soliton Boundary
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Shells Within a Single Soliton (Galaxy Crossing)',
             color=TEXT, fontsize=14, fontweight='bold', pad=15)

cx, cy = 6, 5

# Outer halo (sphere)
halo = Circle((cx, cy), 3.8, fill=True, facecolor=SPHERE, alpha=0.06,
              edgecolor=SPHERE, linewidth=2)
ax.add_patch(halo)
ax.text(cx, cy + 4.1, 'HALO (Sphere)', color=SPHERE, fontsize=9,
        ha='center', fontweight='bold')
ax.text(cx, cy + 3.7, 'R₂ correction, low density', color=WEAK,
        fontsize=7, ha='center')

# Disk edge (torus region)
disk_outer = Ellipse((cx, cy), 6.0, 1.2, fill=True,
                      facecolor=TORUS, alpha=0.12,
                      edgecolor=TORUS, linewidth=2)
ax.add_patch(disk_outer)
ax.text(cx + 3.3, cy + 0.9, 'DISK EDGE', color=TORUS, fontsize=8,
        fontweight='bold')
ax.text(cx + 3.3, cy + 0.6, 'R₄ transition zone', color=WEAK, fontsize=7)

# Disk midplane (denser)
disk_inner = Ellipse((cx, cy), 4.5, 0.5, fill=True,
                      facecolor=TORUS, alpha=0.25,
                      edgecolor=TORUS, linewidth=1.5)
ax.add_patch(disk_inner)
ax.text(cx, cy - 0.6, 'DISK MIDPLANE', color=TORUS, fontsize=8,
        ha='center', fontweight='bold')
ax.text(cx, cy - 0.9, 'Maximum correction per distance', color=WEAK,
        fontsize=7, ha='center')

# Bulge (sphere within)
bulge = Circle((cx, cy), 0.8, fill=True, facecolor=YELLOW, alpha=0.15,
               edgecolor=YELLOW, linewidth=2)
ax.add_patch(bulge)
ax.text(cx, cy + 0.2, 'BULGE', color=YELLOW, fontsize=8,
        ha='center', fontweight='bold')
ax.text(cx, cy - 0.1, '(sphere)', color=WEAK, fontsize=6, ha='center')

# Central SMBH
ax.scatter([cx], [cy - 0.3], s=30, color=RED, zorder=10)
ax.text(cx + 0.3, cy - 0.4, 'SMBH', color=RED, fontsize=6)

# Light ray crossing the galaxy
ray_y = cy + 0.15
ax.annotate('', xy=(10.5, ray_y), xytext=(1.5, ray_y),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2.5))
ax.text(1.2, ray_y + 0.25, 'LIGHT RAY', color=ACCENT, fontsize=9,
        fontweight='bold')

# Shell correction labels along the ray
shell_data = [
    (2.2, 'Enter halo\nr₁ (R₂)', SPHERE),
    (3.2, 'Enter disk\nr₂ (R₄)', TORUS),
    (4.5, 'Dense disk\nr₃ (R₄)', TORUS),
    (5.2, 'Bulge\nr₄ (R₂)', YELLOW),
    (6.8, 'Exit bulge\nr₅ (R₂)', YELLOW),
    (7.8, 'Dense disk\nr₆ (R₄)', TORUS),
    (8.8, 'Exit disk\nr₇ (R₄)', TORUS),
    (9.8, 'Exit halo\nr₈ (R₂)', SPHERE),
]

for x, label, color in shell_data:
    ax.plot([x, x], [ray_y - 0.15, ray_y + 0.15], color=color,
            linewidth=2, zorder=8)
    ax.text(x, ray_y + 0.4, label, color=color, fontsize=5.5,
            ha='center', va='bottom')

# Bottom formula
ax.text(6, 1.5, 'Total galaxy correction = r₁ × r₂ × r₃ × r₄ × r₅ × r₆ × r₇ × r₈',
        color=TEXT, fontsize=10, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#161b22',
                  edgecolor=ACCENT, linewidth=1.5))
ax.text(6, 0.9, 'Each rᵢ is a rational from the shell geometry (R₂ or R₄)',
        color=WEAK, fontsize=8, ha='center')
ax.text(6, 0.5, 'Product across shells = one galaxy\'s total correction factor',
        color=ACCENT, fontsize=8, ha='center')

fig.savefig(os.path.join(OUT, 'modulus_02_shells_within_boundary.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_02_shells_within_boundary.png")


# ================================================================
# FIGURE 3: The Compound Running Curve — H₀ vs Distance
# ================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 10), facecolor=BG,
                                 gridspec_kw={'height_ratios': [3, 1]})

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    ax.tick_params(colors=WEAK)
    for spine in ax.spines.values():
        spine.set_color(WEAK)

# Top panel: H₀ running curve
data = [
    (10, 73.0, 1.0, 'SH0ES', ACCENT),
    (25, 69.8, 1.7, 'TRGB', SPHERE),
    (80, 73.3, 1.8, 'H0LiCOW', PURPLE),
    (500, 67.4, 1.2, 'DES+BAO', TORUS),
    (3000, 67.4, 0.5, 'Planck', RED),
]

for N, H0, err, label, color in data:
    ax1.errorbar(N, H0, yerr=err, fmt='o', color=color, markersize=8,
                capsize=4, capthick=1.5, elinewidth=1.5, zorder=10)
    ax1.text(N * 1.15, H0 + 0.5, label, color=color, fontsize=8)

# Three model curves
N_curve = np.logspace(0.5, 3.7, 200)

# Model 1: simple exponential (homogeneous boundaries)
r1 = 0.99985
H0_simple = 73.2 * r1**N_curve
ax1.plot(N_curve, H0_simple, '-', color=WEAK, linewidth=1.5, alpha=0.6,
         label='Simple: r^N (homogeneous)')

# Model 2: evolving (more boundaries = smaller correction per boundary)
r2_base = 0.9997
H0_evolving = 73.2 * (r2_base * (1 + 0.00005 * N_curve))**N_curve
# Cap it to avoid going negative
H0_evolving = np.maximum(H0_evolving, 60)
ax1.plot(N_curve, H0_evolving, '-', color=SPHERE, linewidth=2,
         label='Evolving: r(N) varies with epoch')

# Model 3: converging (asymptotes to CMB value)
H0_converge = 67.4 + (73.2 - 67.4) * np.exp(-N_curve / 300)
ax1.plot(N_curve, H0_converge, '-', color=ACCENT, linewidth=2,
         label='Converging: asymptote at 67.4')

ax1.set_xscale('log')
ax1.set_ylabel('H₀ (km/s/Mpc)', color=TEXT, fontsize=11)
ax1.set_title('The Compound Running Curve: H₀ vs Boundary Transit Count',
              color=TEXT, fontsize=13, fontweight='bold')
ax1.set_ylim(64, 76)
ax1.set_xlim(3, 5000)
ax1.legend(facecolor='#161b22', edgecolor=WEAK, labelcolor=TEXT,
           fontsize=8, loc='lower left')

# Annotations on top panel
ax1.axhspan(72, 74, alpha=0.08, color=ACCENT)
ax1.axhspan(66.9, 67.9, alpha=0.08, color=RED)
ax1.text(4, 74.5, 'LOCAL', color=ACCENT, fontsize=8, fontweight='bold')
ax1.text(2000, 66, 'CMB', color=RED, fontsize=8, fontweight='bold')

# Bottom panel: per-transit correction r(N) for each model
ax2.axhline(y=1, color=WEAK, linestyle=':', alpha=0.3)

r_simple = np.ones_like(N_curve) * r1
r_evolving = r2_base * (1 + 0.00005 * N_curve)
r_converge = 1 - (73.2 - 67.4) / (73.2) * np.exp(-N_curve / 300) / N_curve
# Smoothed version
r_converge_smooth = np.ones_like(N_curve) * 0.99985
for i in range(1, len(N_curve)):
    if H0_converge[i] > 0 and H0_converge[i-1] > 0:
        r_converge_smooth[i] = (H0_converge[i] / H0_converge[i-1]) ** (
            1.0 / (N_curve[i] - N_curve[i-1] + 0.01))

ax2.plot(N_curve, r_simple, '-', color=WEAK, linewidth=1.5, alpha=0.6,
         label='Simple: constant r')
ax2.plot(N_curve, np.clip(r_evolving, 0.999, 1.001), '-', color=SPHERE,
         linewidth=2, label='Evolving: r grows with N')

ax2.set_xscale('log')
ax2.set_xlabel('Effective Boundary Transit Count N', color=TEXT, fontsize=11)
ax2.set_ylabel('Per-transit r', color=TEXT, fontsize=10)
ax2.set_ylim(0.9996, 1.0002)
ax2.set_xlim(3, 5000)
ax2.legend(facecolor='#161b22', edgecolor=WEAK, labelcolor=TEXT,
           fontsize=7, loc='upper right')

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'modulus_03_running_curve.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_03_running_curve.png")


# ================================================================
# FIGURE 4: Directional Dependence — Through Hole vs Around Ring
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Directional H₀: Through the Hole vs Around the Ring',
             color=TEXT, fontsize=14, fontweight='bold', pad=15)

# Central observer
cx, cy = 6.5, 4.5
ax.scatter([cx], [cy], s=100, color=YELLOW, zorder=10)
ax.text(cx, cy - 0.35, 'OBSERVER', color=YELLOW, fontsize=8,
        ha='center', fontweight='bold')

# The local galactic torus (top-down view)
outer_r = 3.0
inner_r = 1.5
outer = Circle((cx, cy), outer_r, fill=False, edgecolor=TORUS,
               linewidth=2, alpha=0.6)
inner = Circle((cx, cy), inner_r, fill=False, edgecolor=TORUS,
               linewidth=2, linestyle='--', alpha=0.4)
ax.add_patch(outer)
ax.add_patch(inner)

# Fill the annulus
theta = np.linspace(0, 2 * np.pi, 100)
x_out = cx + outer_r * np.cos(theta)
y_out = cy + outer_r * np.sin(theta)
x_in = cx + inner_r * np.cos(theta)
y_in = cy + inner_r * np.sin(theta)
ax.fill(np.concatenate([x_out, x_in[::-1]]),
        np.concatenate([y_out, y_in[::-1]]),
        color=TORUS, alpha=0.08)

ax.text(cx, cy + outer_r + 0.3, 'GALACTIC DISK (top-down view)',
        color=TORUS, fontsize=10, ha='center', fontweight='bold')

# Direction 1: Through the hole (perpendicular to disk = toward pole)
ax.annotate('', xy=(cx, cy + 4.2), xytext=(cx, cy + 0.3),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=3))
ax.text(cx + 0.3, cy + 2.5, 'THROUGH\nTHE HOLE', color=ACCENT,
        fontsize=10, fontweight='bold')
ax.text(cx + 0.3, cy + 1.8, '(galactic pole)', color=WEAK, fontsize=7)

# Boundary count annotation for pole direction
ax.text(cx + 2.5, cy + 3.8, 'Few boundaries\nN_pole ~ 10-50',
        color=ACCENT, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))
ax.text(cx + 2.5, cy + 3.0, 'H₀(pole) ≈ 73\n(less correction)',
        color=ACCENT, fontsize=8)

# Direction 2: Around the ring (in-plane)
ax.annotate('', xy=(cx + 4.5, cy), xytext=(cx + 0.3, cy),
            arrowprops=dict(arrowstyle='->', color=RED, lw=3))
ax.text(cx + 2.5, cy - 0.5, 'AROUND\nTHE RING', color=RED,
        fontsize=10, fontweight='bold')
ax.text(cx + 2.5, cy - 1.0, '(galactic plane)', color=WEAK, fontsize=7)

# Boundary count for plane direction
ax.text(cx + 4.8, cy + 0.8, 'Many boundaries\nN_plane ~ 500-5000',
        color=RED, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=RED))
ax.text(cx + 4.8, cy + 0.0, 'H₀(plane) ≈ 67\n(more correction)',
        color=RED, fontsize=8)

# Direction 3: Diagonal (intermediate)
angle = np.pi / 4
dx = 3.5 * np.cos(angle)
dy = 3.5 * np.sin(angle)
ax.annotate('', xy=(cx + dx, cy + dy), xytext=(cx + 0.2, cy + 0.2),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2,
                           linestyle='--'))
ax.text(cx + dx + 0.3, cy + dy, 'DIAGONAL\nN ~ 100-500',
        color=PURPLE, fontsize=7)

# Void region (fewer galaxies)
void_cx, void_cy = 2.0, 7.0
void = Circle((void_cx, void_cy), 0.8, fill=True, facecolor=BG,
              edgecolor=WEAK, linewidth=1.5, linestyle=':')
ax.add_patch(void)
ax.text(void_cx, void_cy, 'VOID', color=WEAK, fontsize=8,
        ha='center', fontweight='bold')
ax.text(void_cx, void_cy - 0.3, 'N ≈ 0', color=WEAK, fontsize=7,
        ha='center')

# Filament region (many galaxies)
fil_x = np.array([9.5, 10.0, 10.5, 11.0, 11.5])
fil_y = np.array([7.0, 7.3, 7.1, 7.4, 7.2])
ax.plot(fil_x, fil_y, 'o-', color=SPHERE, markersize=5, linewidth=2,
        alpha=0.6)
ax.text(10.5, 6.5, 'FILAMENT', color=SPHERE, fontsize=8,
        ha='center', fontweight='bold')
ax.text(10.5, 6.2, 'N >> 100', color=WEAK, fontsize=7, ha='center')

# Bottom prediction box
ax.text(6.5, 0.8,
        'PREDICTION: H₀(pole) > H₀(plane) > H₀(filament direction)',
        color=TEXT, fontsize=10, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#161b22',
                  edgecolor=ACCENT, linewidth=1.5))
ax.text(6.5, 0.2,
        'ΔH₀ = (N_plane − N_pole) × (1 − r) × H₀',
        color=WEAK, fontsize=8, ha='center')

fig.savefig(os.path.join(OUT, 'modulus_04_directional.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_04_directional.png")


# ================================================================
# FIGURE 5: The Geometric Stage Sequence — Full Line of Sight
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(14, 6), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Line of Sight: Sequence of Geometric Stages',
             color=TEXT, fontsize=13, fontweight='bold', pad=10)

# Light ray across the figure
ray_y = 3.0
ax.plot([0.5, 13.5], [ray_y, ray_y], color=ACCENT, linewidth=1, alpha=0.3)
ax.annotate('', xy=(13.5, ray_y), xytext=(0.5, ray_y),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))

# Observer on left
ax.scatter([0.8], [ray_y], s=80, color=YELLOW, zorder=10)
ax.text(0.8, ray_y - 0.4, 'HERE', color=YELLOW, fontsize=7,
        ha='center', fontweight='bold')

# CMB on right
ax.scatter([13.2], [ray_y], s=80, color=RED, zorder=10, marker='*')
ax.text(13.2, ray_y - 0.4, 'CMB', color=RED, fontsize=7,
        ha='center', fontweight='bold')

# Soliton stages along the ray
stages = [
    (1.8, 0.6, 'MW\nhalo', SPHERE, 'S'),
    (3.0, 0.4, 'Local\ngroup', SPHERE, 'S'),
    (4.0, 0.8, 'Virgo\ncluster', PURPLE, 'S'),
    (5.2, 1.0, 'VOID', WEAK, '—'),
    (6.5, 0.5, 'Disk\ngalaxy', TORUS, 'T'),
    (7.5, 0.3, 'Dwarf', WEAK, 'S'),
    (8.3, 0.7, 'Cluster', PURPLE, 'S'),
    (9.3, 1.2, 'VOID', WEAK, '—'),
    (10.8, 0.4, 'Galaxy', TORUS, 'T'),
    (11.6, 0.3, 'Galaxy', SPHERE, 'S'),
    (12.4, 0.5, 'Filament', SPHERE, 'S'),
]

for x, w, label, color, geo_type in stages:
    # Draw the stage as a box
    if geo_type == '—':
        # Void: dashed outline
        rect = mpatches.FancyBboxPatch((x - w/2, ray_y - 0.8), w, 1.6,
                                        boxstyle="round,pad=0.05",
                                        facecolor=BG,
                                        edgecolor=color, linewidth=1,
                                        linestyle=':')
    elif geo_type == 'T':
        rect = mpatches.FancyBboxPatch((x - w/2, ray_y - 0.8), w, 1.6,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.12,
                                        edgecolor=color, linewidth=1.5)
    else:
        rect = mpatches.FancyBboxPatch((x - w/2, ray_y - 0.8), w, 1.6,
                                        boxstyle="round,pad=0.05",
                                        facecolor=color, alpha=0.08,
                                        edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, ray_y + 1.1, label, color=color, fontsize=6,
            ha='center', va='bottom')

    # Geometry marker
    if geo_type == 'S':
        ax.text(x, ray_y - 1.1, 'R₂', color=color, fontsize=6,
                ha='center')
    elif geo_type == 'T':
        ax.text(x, ray_y - 1.1, 'R₄', color=color, fontsize=6,
                ha='center')
    elif geo_type == '—':
        ax.text(x, ray_y - 1.1, 'r>1?', color=RED, fontsize=6,
                ha='center')

# Top: cumulative H₀
h0_vals = [73.0, 72.8, 72.5, 71.8, 71.8, 71.2, 71.0, 70.2, 70.2,
           69.5, 69.2, 68.8]
h0_x = [0.8, 1.8, 3.0, 4.0, 5.2, 6.5, 7.5, 8.3, 9.3, 10.8, 11.6, 12.4]
ax.plot(h0_x, [v / 73.0 * 1.5 + 4.2 for v in h0_vals],
        'o-', color=ACCENT, markersize=4, linewidth=1.5)

# H₀ axis labels
ax.text(0.3, 5.7, '73.0', color=ACCENT, fontsize=7)
ax.text(0.3, 4.6, '68.0', color=ACCENT, fontsize=7)
ax.text(0.1, 5.2, 'H₀', color=ACCENT, fontsize=8, fontweight='bold',
        rotation=90)

# Bottom formula
ax.text(7, 0.5,
        'H₀(CMB) = H₀(local) × r_MW × r_LG × r_Virgo × r_void₁ × r_gal₁ × ... × r_N',
        color=TEXT, fontsize=8, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))
ax.text(7, 0.1,
        'Each r is rational from its geometry. Product is transcendental.',
        color=WEAK, fontsize=7, ha='center')

fig.savefig(os.path.join(OUT, 'modulus_05_line_of_sight.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_05_line_of_sight.png")


# ================================================================
# FIGURE 6: The Two-Level Structure — Geometric vs Domain-Specific
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Two-Level Remainder Structure: Nine Domains + Proposed Extensions',
             color=TEXT, fontsize=13, fontweight='bold', pad=10)

# Headers
ax.text(0.5, 7.3, 'DOMAIN', color=TEXT, fontsize=9, fontweight='bold')
ax.text(3.5, 7.3, 'LEVEL 1 (Geometric)', color=SPHERE, fontsize=9,
        fontweight='bold')
ax.text(7.0, 7.3, 'LEVEL 2 (Domain-specific)', color=TORUS, fontsize=9,
        fontweight='bold')
ax.text(10.5, 7.3, 'SUBGROUP', color=WEAK, fontsize=9, fontweight='bold')

ax.plot([0.3, 12.7], [7.1, 7.1], color=WEAK, linewidth=0.5)

# Established domains
established = [
    ('θ vacuum', 'R₂ in 8R₂ modulus', 'θ = 0 (DERIVED)', 'A'),
    ('Bohr-Sommerfeld', 'R₂ in 8R₂ℏ modulus', 'μ/4 = 1/2 (Maslov)', 'A'),
    ('Berry phase', 'R₂ in γ = 4R₂(1−cosθ)', '(1−cosθ)/2', 'A'),
    ('Brillouin zone', 'R₂ in G = 8R₂/a', 'p/N', 'A'),
    ('RG running', 'R₂ in 1/(12R₂) step', 'Accumulated running', 'B'),
    ('Chern-Simons', 'R₄ in 1/(256R₄)', 'CS mod ℤ', 'C'),
    ('Aharonov-Bohm', 'R₂ in 8R₂ modulus', 'Φ/Φ₀ mod 1', 'A'),
    ('Flux quant.', 'R₂ in 8R₂ modulus', '0 (topological)', 'A'),
    ('AC Josephson', 'R₂ in 8R₂ modulus', 't/T_J mod 1', 'A'),
]

y = 6.8
for domain, level1, level2, subgroup in established:
    y -= 0.42
    ax.text(0.5, y, domain, color=TEXT, fontsize=7)
    ax.text(3.5, y, level1, color=SPHERE, fontsize=6.5)
    ax.text(7.0, y, level2, color=TORUS, fontsize=6.5)
    sg_color = ACCENT if subgroup == 'A' else (
        PURPLE if subgroup == 'B' else RED)
    ax.text(10.5, y, subgroup, color=sg_color, fontsize=8,
            fontweight='bold')

# Separator
y -= 0.25
ax.plot([0.3, 12.7], [y, y], color=YELLOW, linewidth=1, linestyle='--')
ax.text(6.5, y + 0.1, 'PROPOSED EXTENSIONS', color=YELLOW, fontsize=8,
        ha='center', fontweight='bold')

# Proposed extensions
proposed = [
    ('Gap ratio', 'R₂ CANCELS (pure rational)', '218/115 vs measured', 'B',
     YELLOW),
    ('A₂ coefficient', 'R₄ dominates (8× net)', 'Net −0.328 after 87% cancel',
     'B*', YELLOW),
    ('H₀ running', 'R₂ or R₄ per transit', 'Cumulative 1 − r^N', 'B',
     YELLOW),
    ('Nebula correction', 'Pure rational? (no R₂?)', 'Irregular boundary',
     'C?', YELLOW),
]

for domain, level1, level2, subgroup, color in proposed:
    y -= 0.42
    ax.text(0.5, y, domain, color=color, fontsize=7)
    ax.text(3.5, y, level1, color=SPHERE, fontsize=6.5)
    ax.text(7.0, y, level2, color=TORUS, fontsize=6.5)
    ax.text(10.5, y, subgroup, color=color, fontsize=8, fontweight='bold')

# Bottom note
ax.text(6.5, 0.4,
        'Level 1 is universal (geometry). Level 2 is domain-specific (physics).',
        color=TEXT, fontsize=9, ha='center')
ax.text(6.5, 0.1,
        'The gap ratio is unique: Level 1 cancels completely → pure rational test.',
        color=ACCENT, fontsize=8, ha='center')

fig.savefig(os.path.join(OUT, 'modulus_06_two_level_structure.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_06_two_level_structure.png")


# ================================================================
# FIGURE 7: The Algorithm — From Galaxy Surveys to H₀ Prediction
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')
ax.set_title('The Algorithm: Galaxy Survey Data → H₀ Prediction',
             color=TEXT, fontsize=14, fontweight='bold', pad=10)

# Step boxes
steps = [
    (1.5, 7.5, 'STEP 1: CENSUS', SPHERE,
     'For each line of sight (θ,φ):\nCount galaxies from survey\nClassify: sphere / disk / irregular'),
    (1.5, 5.8, 'STEP 2: PER-GALAXY r', TORUS,
     'For each galaxy i:\n  Sphere → rᵢ = 1 − ε·R₂·(M/M_ref)\n  Disk → rᵢ = 1 − ε·R₄·(M/M_ref)·f(angle)'),
    (1.5, 4.1, 'STEP 3: CUMULATE', ACCENT,
     'H₀(θ,φ,d) = H₀(local) × Π rᵢ\nProduct over all galaxies with dist < d'),
    (1.5, 2.4, 'STEP 4: CALIBRATE', YELLOW,
     'Fit ε from:\n  H₀(local) = 73 ± 1\n  H₀(CMB) = 67.4 ± 0.5'),
    (1.5, 0.7, 'STEP 5: PREDICT', RED,
     'Predict H₀ for any direction\nTest P1-P5 from notebook'),
]

for x, y, title, color, desc in steps:
    rect = mpatches.FancyBboxPatch((x - 0.3, y - 0.5), 5.0, 1.2,
                                    boxstyle="round,pad=0.15",
                                    facecolor='#161b22',
                                    edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y + 0.45, title, color=color, fontsize=9, fontweight='bold')
    ax.text(x, y - 0.0, desc, color=TEXT, fontsize=7, va='top',
            linespacing=1.4)

# Arrows between steps
for i in range(len(steps) - 1):
    y1 = steps[i][1] - 0.5
    y2 = steps[i+1][1] + 0.7
    ax.annotate('', xy=(3.5, y2), xytext=(3.5, y1),
                arrowprops=dict(arrowstyle='->', color=WEAK, lw=1.5))

# Right column: the unknown
ax.text(8, 7.8, 'THE CRITICAL UNKNOWN', color=RED, fontsize=11,
        fontweight='bold')
ax.text(8, 7.3, 'The per-transit correction ε', color=TEXT, fontsize=9)
ax.text(8, 6.8, 'For VP running: ε = 1/(12R₂)', color=SPHERE, fontsize=8)
ax.text(8, 6.4, 'For H₀ running: ε = ???', color=RED, fontsize=9,
        fontweight='bold')

ax.text(8, 5.6, 'CONSTRAINTS ON ε:', color=TEXT, fontsize=9,
        fontweight='bold')
constraints = [
    'If R₂-based: ε ~ (1−r) ~ 10⁻⁴ per sphere',
    'If R₄-based: ε ~ 10⁻⁴ per torus, direction-dep.',
    'From data: r ≈ 0.9992 for N~100 transits',
    '→ ε ≈ 8×10⁻⁴ per effective transit',
]
for i, c in enumerate(constraints):
    ax.text(8, 5.1 - i * 0.35, c, color=WEAK, fontsize=7)

# Data sources
ax.text(8, 3.5, 'AVAILABLE DATA:', color=TEXT, fontsize=9,
        fontweight='bold')
data_sources = [
    ('SDSS / DESI', 'Galaxy positions + morphologies'),
    ('SH0ES / TRGB', 'Local H₀ calibration'),
    ('Planck', 'CMB H₀ endpoint'),
    ('LIGO/Virgo', 'GW standard sirens (kill test)'),
    ('CMB anomalies', 'Directional fingerprints'),
]
for i, (name, desc) in enumerate(data_sources):
    ax.text(8, 3.0 - i * 0.35, name, color=ACCENT, fontsize=7,
            fontweight='bold')
    ax.text(9.5, 3.0 - i * 0.35, desc, color=WEAK, fontsize=7)

# Math gate status
ax.text(8, 1.0, 'MATH GATE: OPEN', color=RED, fontsize=11,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=RED, linewidth=2))
ax.text(8, 0.5, 'ε not derived. Curve not fitted.\nPredictions not tested.',
        color=WEAK, fontsize=8)

fig.savefig(os.path.join(OUT, 'modulus_07_algorithm.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_07_algorithm.png")


# ================================================================
# FIGURE 8: VP Running ↔ H₀ Running Parallel
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    ax.tick_params(colors=WEAK)
    for spine in ax.spines.values():
        spine.set_color(WEAK)

# Left: VP running (established)
E = np.linspace(-1, 5.5, 300)
alpha_inv = np.ones_like(E) * 137.036
for i in range(len(E)):
    correction = 0
    for thresh, slope in fermion_thresholds:
        if E[i] > thresh:
            correction += slope * (E[i] - thresh)
    alpha_inv[i] = 137.036 - correction

ax1.plot(E, alpha_inv, color=SPHERE, linewidth=2)
ax1.set_xlabel('log₁₀(Energy / MeV)', color=TEXT, fontsize=9)
ax1.set_ylabel(r'$\alpha^{-1}$', color=TEXT, fontsize=10)
ax1.set_title('VP RUNNING (Established)', color=ACCENT, fontsize=11,
              fontweight='bold')
ax1.set_xlim(-1, 5.5)
ax1.set_ylim(127, 138)

# Annotations
ax1.text(0, 137.5, 'Step: 1/(12R₂)', color=SPHERE, fontsize=7)
ax1.text(0, 137, 'Thresholds: m_f', color=TORUS, fontsize=7)
ax1.text(0, 136.5, 'Integer: flavor count', color=ACCENT, fontsize=7)
ax1.text(0, 136, 'Remainder: accumulated', color=PURPLE, fontsize=7)
ax1.text(0, 135.5, 'Subgroup: B', color=PURPLE, fontsize=7,
         fontweight='bold')

# Right: H₀ running (proposed)
N = np.logspace(0.5, 3.5, 200)
H0 = 67.4 + (73.2 - 67.4) * np.exp(-N / 300)
ax2.plot(N, H0, color=TORUS, linewidth=2)
ax2.set_xscale('log')
ax2.set_xlabel('Boundary Transit Count N', color=TEXT, fontsize=9)
ax2.set_ylabel('H₀ (km/s/Mpc)', color=TEXT, fontsize=10)
ax2.set_title('H₀ RUNNING (Proposed)', color=RED, fontsize=11,
              fontweight='bold')
ax2.set_ylim(65, 75)

# Data points
for N_val, H0_val, err, label, color in data:
    ax2.errorbar(N_val, H0_val, yerr=err, fmt='o', color=color,
                markersize=6, capsize=3)

ax2.text(5, 74, 'Step: ε (unknown)', color=TORUS, fontsize=7)
ax2.text(5, 73.3, 'Thresholds: soliton boundaries', color=TORUS,
         fontsize=7)
ax2.text(5, 72.6, 'Integer: boundary count', color=ACCENT, fontsize=7)
ax2.text(5, 71.9, 'Remainder: cumulative corr.', color=PURPLE, fontsize=7)
ax2.text(5, 71.2, 'Subgroup: B', color=PURPLE, fontsize=7,
         fontweight='bold')

fig.suptitle('The Structural Parallel: Same Subgroup B Pattern',
             color=TEXT, fontsize=13, fontweight='bold', y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'modulus_08_parallel.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: modulus_08_parallel.png")


print("\n=== ALL 8 DIAGRAMS SAVED ===")
print("Location: " + OUT + "/modulus_*.png")
