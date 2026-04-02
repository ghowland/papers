#!/usr/bin/env python3
"""
qed_gr_boundary_crossing_diagrams.py

Diagrams for the QED-to-GR maximum boundary crossing problem:
- The hierarchy distance (40 orders of magnitude)
- The confinement wall as first obstruction
- The running curve through all boundaries
- The cancellation pattern
- The three manifestations (Hubble, G running, QED-GR)
- The VP ↔ gravity parallel

Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
import os

OUT = "../figures"
os.makedirs(OUT, exist_ok=True)

BG = '#0d1117'
SPHERE = '#58a6ff'
TORUS = '#f0883e'
WEAK = '#8b949e'
TEXT = '#e6edf3'
ACCENT = '#7ee787'
RED = '#f85149'
PURPLE = '#d2a8ff'
YELLOW = '#ffcc00'
CYAN = '#79c0ff'


# ================================================================
# FIGURE 1: The Hierarchy Distance — 40 Orders of Magnitude
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(14, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-1, 14)
ax.set_ylim(-1, 9)
ax.axis('off')
ax.set_title('The Hierarchy Distance: QED to GR Through Every Boundary',
             color=TEXT, fontsize=14, fontweight='bold', pad=15)

# Vertical scale axis
ax.plot([1.5, 1.5], [0.5, 8.5], color=WEAK, linewidth=2)
ax.text(0.3, 8.5, 'log₁₀(m)', color=WEAK, fontsize=9, fontweight='bold')

# Boundary layers along the axis
layers = [
    (0.7, -13, 'VP cloud', SPHERE, 'QED DOMAIN', 'α = 1/137'),
    (1.3, -15, 'Proton', SPHERE, '', '99% binding'),
    (1.9, -10, 'Atom', SPHERE, '', 'e⁻ cloud'),
    (2.5, -9, 'Molecule', WEAK, '', 'chemical bonds'),
    (3.1, -6, 'Cell', WEAK, '', 'membrane'),
    (3.7, -2, 'Human', WEAK, '', 'organism soliton'),
    (4.3, 0, 'Object', WEAK, '', '~1 m'),
    (4.9, 6, 'Planet', SPHERE, '', 'Hill sphere'),
    (5.5, 9, 'Star system', SPHERE, '', '☉ dominates'),
    (6.1, 13, 'Solar disk', TORUS, '', 'Bessel modes'),
    (6.7, 20, 'Galaxy disk', TORUS, '', 'R₄ rotation'),
    (7.3, 21, 'Galaxy halo', SPHERE, '', 'dark matter?'),
    (7.9, 23, 'Cluster', PURPLE, 'GR DOMAIN', 'virialized'),
    (8.3, 26, 'Observable\nuniverse', RED, '', 'horizon'),
]

for y, log_scale, name, color, domain_label, note in layers:
    # Tick on axis
    ax.plot([1.3, 1.7], [y, y], color=color, linewidth=2)

    # Scale label
    ax.text(0.5, y, f'10^{log_scale}', color=WEAK, fontsize=7,
            ha='right', va='center')

    # Boundary name and type
    ax.text(2.0, y, name, color=color, fontsize=8, va='center',
            fontweight='bold')

    # Note
    ax.text(4.2, y, note, color=WEAK, fontsize=7, va='center')

    # Domain label (only for QED and GR endpoints)
    if domain_label:
        ax.text(5.8, y, domain_label, color=YELLOW, fontsize=10,
                va='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#161b22',
                          edgecolor=YELLOW))

    # Geometry indicator
    if color == SPHERE:
        ax.text(3.6, y, '○', color=SPHERE, fontsize=10, va='center')
    elif color == TORUS:
        ax.text(3.6, y, '◎', color=TORUS, fontsize=10, va='center')
    elif color == PURPLE:
        ax.text(3.6, y, '○', color=PURPLE, fontsize=10, va='center')
    else:
        ax.text(3.6, y, '◇', color=WEAK, fontsize=10, va='center')

# The confinement wall
wall_y = 1.6
ax.axhspan(wall_y - 0.15, wall_y + 0.15, xmin=0.1, xmax=0.45,
           alpha=0.3, color=RED)
ax.text(6.5, wall_y, 'CONFINEMENT WALL', color=RED, fontsize=9,
        va='center', fontweight='bold')
ax.text(6.5, wall_y - 0.25, '1st obstruction: perturbation theory fails',
        color=RED, fontsize=7, va='center')

# Right column: the running arrows
ax.text(8.5, 8.0, 'QED → GR', color=ACCENT, fontsize=11, fontweight='bold')
ax.annotate('', xy=(8.8, 7.8), xytext=(8.8, 0.7),
            arrowprops=dict(arrowstyle='<->', color=ACCENT, lw=2))
ax.text(9.2, 4.5, '~20 boundary\ntypes crossed\n\n~40 orders of\nmagnitude\n\nEach crossing:\nrational correction\n\nProduct:\ntranscendental\n(PSLQ null)',
        color=TEXT, fontsize=7, va='center')

# Bottom annotation
ax.text(7, 0.0,
        'To describe GR from QED: run the transformation law through EVERY boundary.',
        color=TEXT, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'qed_gr_01_hierarchy_distance.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_01_hierarchy_distance.png")


# ================================================================
# FIGURE 2: The Confinement Wall — First Obstruction
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 7), facecolor=BG)
ax.set_facecolor(BG)

# Energy axis
E = np.linspace(-2, 6, 500)

# Alpha_s running (schematic)
Lambda_QCD = np.log10(300)  # ~300 MeV
alpha_s = np.zeros_like(E)
for i in range(len(E)):
    if E[i] > np.log10(2000):  # above 2 GeV: perturbative
        alpha_s[i] = 0.3 / (1 + 0.15 * (E[i] - np.log10(2000)))
    elif E[i] > Lambda_QCD:  # confinement zone
        alpha_s[i] = 0.3 + 2.0 * (np.log10(2000) - E[i]) / (np.log10(2000) - Lambda_QCD)
    else:
        alpha_s[i] = 3.0  # non-perturbative

# Alpha_em running (schematic)
alpha_em_inv = np.ones_like(E) * 137.036
for i in range(len(E)):
    if E[i] > np.log10(0.511):
        alpha_em_inv[i] -= 0.4 * (E[i] - np.log10(0.511))

ax2 = ax.twinx()

ax.plot(E, alpha_s, color=RED, linewidth=2.5, label=r'$\alpha_s$ (strong)')
ax2.plot(E, alpha_em_inv, color=SPHERE, linewidth=2.5,
         label=r'$\alpha_{em}^{-1}$ (EM)')

# Confinement wall zone
ax.axvspan(np.log10(300), np.log10(2000), alpha=0.2, color=RED)
ax.text(np.log10(800), 2.5, 'CONFINEMENT\nWALL', color=RED,
        fontsize=12, ha='center', fontweight='bold')
ax.text(np.log10(800), 2.0, 'α_s → O(1)\nPerturbation fails',
        color=RED, fontsize=8, ha='center')

# Labels for domains
ax.text(-1.5, 0.5, 'QED\nPERTURBATIVE', color=SPHERE, fontsize=9,
        fontweight='bold')
ax.text(4.5, 0.5, 'QCD + QED\nPERTURBATIVE', color=ACCENT, fontsize=9,
        fontweight='bold')

# Arrow showing "QED must cross this to reach hadronic/gravity"
ax.annotate('', xy=(np.log10(2000), 1.5), xytext=(np.log10(300), 1.5),
            arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=3))
ax.text(np.log10(800), 1.6, 'Factor 64 in energy\nELIMINATED',
        color=YELLOW, fontsize=8, ha='center', fontweight='bold',
        va='bottom')

# Styling
ax.set_xlabel('log₁₀(Energy / MeV)', color=TEXT, fontsize=11)
ax.set_ylabel(r'$\alpha_s$', color=RED, fontsize=12)
ax2.set_ylabel(r'$\alpha_{em}^{-1}$', color=SPHERE, fontsize=12)
ax.set_title('The First Obstruction: Confinement Wall at ~300 MeV — 2 GeV',
             color=TEXT, fontsize=13, fontweight='bold')
ax.tick_params(axis='y', colors=RED)
ax2.tick_params(axis='y', colors=SPHERE)
ax.tick_params(axis='x', colors=WEAK)
ax.spines['bottom'].set_color(WEAK)
ax.spines['left'].set_color(RED)
ax2.spines['right'].set_color(SPHERE)
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.set_xlim(-2, 6)
ax.set_ylim(0, 3.5)
ax2.set_ylim(125, 138)

# Bottom note
ax.text(2, 3.2,
        'If the FIRST boundary crossing breaks perturbation theory,\n'
        'the 20th crossing is exponentially harder.',
        color=TEXT, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=RED))

fig.savefig(os.path.join(OUT, 'qed_gr_02_confinement_wall.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_02_confinement_wall.png")


# ================================================================
# FIGURE 3: The Running Curve Through All Boundaries
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(14, 8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('The Total Running: QED Coupling Through Every Soliton Boundary',
             color=TEXT, fontsize=13, fontweight='bold', pad=12)

# Horizontal "running" line from QED to GR
y_line = 4.0

# Background zones
zones = [
    (0.5, 2.5, 'SUBATOMIC', SPHERE, 0.06),
    (2.5, 4.0, 'CONFINEMENT\nZONE', RED, 0.1),
    (4.0, 6.5, 'MESOSCOPIC', WEAK, 0.04),
    (6.5, 9.5, 'ASTRONOMICAL', TORUS, 0.06),
    (9.5, 13.5, 'COSMOLOGICAL', PURPLE, 0.06),
]

for x1, x2, label, color, alpha in zones:
    ax.axvspan(x1, x2, ymin=0.25, ymax=0.75, alpha=alpha, color=color)
    ax.text((x1 + x2) / 2, 6.5, label, color=color, fontsize=7,
            ha='center', fontweight='bold')

# The running curve (schematic)
x_pts = np.array([0.8, 1.5, 2.0, 2.5, 4.0, 4.5, 5.0, 5.5, 6.0,
                   7.0, 7.5, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 13.0])

# alpha_eff starts at alpha_QED and runs
alpha_eff = np.array([137.0, 136.5, 135.8, 134.0, 131.0, 131.5,
                       131.8, 132.0, 132.1, 131.5, 131.0, 130.5,
                       130.0, 129.8, 129.5, 129.2, 129.0, 128.8])

# Normalize to fit display
y_vals = (alpha_eff - 128) / (137 - 128) * 3 + 2.5

ax.plot(x_pts, y_vals, 'o-', color=ACCENT, linewidth=2, markersize=5,
        zorder=5)

# Boundary crossings marked
boundaries_x = [1.5, 2.0, 4.5, 5.5, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]
boundary_labels = ['Proton', 'Atom', 'Planet', 'Star', 'Solar\ndisk',
                   'Galaxy', 'Halo', 'Cluster', 'Void', 'Filament']
boundary_colors = [SPHERE, SPHERE, SPHERE, SPHERE, TORUS,
                   TORUS, SPHERE, PURPLE, WEAK, SPHERE]

for x, label, color in zip(boundaries_x, boundary_labels, boundary_colors):
    ax.axvline(x=x, ymin=0.3, ymax=0.65, color=color, linestyle=':',
               alpha=0.4, linewidth=1)
    ax.text(x, 1.8, label, color=color, fontsize=5.5, ha='center',
            rotation=60)

# The confinement gap
ax.annotate('', xy=(4.0, y_line + 1.5), xytext=(2.5, y_line + 1.5),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(3.25, y_line + 1.7, 'NON-PERTURBATIVE\nMUST MEASURE',
        color=RED, fontsize=7, ha='center', fontweight='bold')

# Endpoints
ax.text(0.5, y_vals[0] + 0.3, 'α⁻¹ = 137.036\n(QED)', color=ACCENT,
        fontsize=8, fontweight='bold')
ax.text(12.5, y_vals[-1] - 0.5, 'α_eff⁻¹ = ???\n(at GR scale)',
        color=RED, fontsize=8, fontweight='bold')

# Bottom: the key equation
ax.text(7, 0.7,
        'α_eff(GR) = α(QED) × Π [1 + Δα(boundary_i)]    '
        '←  each Δα is rational, product is transcendental',
        color=TEXT, fontsize=8, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'qed_gr_03_running_curve.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_03_running_curve.png")


# ================================================================
# FIGURE 4: The A₂ Cancellation Pattern as Template
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG)

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    ax.tick_params(colors=WEAK)
    for spine in ax.spines.values():
        spine.set_color(WEAK)

# Left: A₂ cancellation (established, from PHYS-12)
pieces = ['Rational\n197/144', 'Number-\ntheoretic\n(3/4)ζ(3)',
          'Geometric\nR₄×c_geom', 'NET A₂']
values = [1.368, 0.902, -2.598, -0.328]
colors_bar = [SPHERE, PURPLE, TORUS, ACCENT]

bars = ax1.bar(range(4), values, color=colors_bar, alpha=0.7,
               edgecolor=colors_bar, linewidth=1.5)
ax1.axhline(y=0, color=WEAK, linewidth=0.5)
ax1.set_xticks(range(4))
ax1.set_xticklabels(pieces, fontsize=7, color=TEXT)
ax1.set_ylabel('Value', color=TEXT, fontsize=10)
ax1.set_title('A₂ Coefficient: 87% Cancellation\n(ESTABLISHED — PHYS-12)',
              color=ACCENT, fontsize=10, fontweight='bold')

for i, v in enumerate(values):
    ax1.text(i, v + (0.1 if v > 0 else -0.2), f'{v:+.3f}',
             color=colors_bar[i], fontsize=8, ha='center',
             fontweight='bold')

ax1.text(2, 1.5, '87% of\ngeometric\ncancelled', color=RED,
         fontsize=9, fontweight='bold', ha='center')

# Right: Proposed per-boundary correction (analogous pattern)
pieces2 = ['R₂ geometric\ncorrection', 'Density\nprofile\ncorrection',
           'Mode\nstructure\ncorrection', 'NET per-\nboundary Δα']
values2 = [0.005, -0.003, -0.0018, 0.0002]
colors2 = [SPHERE, TORUS, PURPLE, ACCENT]

bars2 = ax2.bar(range(4), values2, color=colors2, alpha=0.7,
                edgecolor=colors2, linewidth=1.5)
ax2.axhline(y=0, color=WEAK, linewidth=0.5)
ax2.set_xticks(range(4))
ax2.set_xticklabels(pieces2, fontsize=7, color=TEXT)
ax2.set_ylabel('Correction magnitude', color=TEXT, fontsize=10)
ax2.set_title('Per-Boundary Correction: Analogous Cancellation?\n(PROPOSED — not computed)',
              color=YELLOW, fontsize=10, fontweight='bold')

for i, v in enumerate(values2):
    ax2.text(i, v + (0.0003 if v > 0 else -0.0005), f'{v:+.4f}',
             color=colors2[i], fontsize=8, ha='center',
             fontweight='bold')

ax2.text(2, 0.004, '~96% cancelled?\nNET ~ 10⁻⁴ per crossing',
         color=RED, fontsize=8, fontweight='bold', ha='center')

fig.suptitle('The Cancellation Template: Why G Appears Constant Despite Running',
             color=TEXT, fontsize=12, fontweight='bold', y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'qed_gr_04_cancellation_pattern.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_04_cancellation_pattern.png")


# ================================================================
# FIGURE 5: Three Manifestations of the Same Phenomenon
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 9), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis('off')
ax.set_title('Three Manifestations of Soliton Boundary Running',
             color=TEXT, fontsize=14, fontweight='bold', pad=15)

# Central concept
cx, cy = 6.5, 4.5
central = Circle((cx, cy), 1.2, fill=True, facecolor='#161b22',
                 edgecolor=ACCENT, linewidth=3)
ax.add_patch(central)
ax.text(cx, cy + 0.25, 'SOLITON', color=ACCENT, fontsize=11,
        ha='center', fontweight='bold')
ax.text(cx, cy - 0.15, 'BOUNDARY', color=ACCENT, fontsize=11,
        ha='center', fontweight='bold')
ax.text(cx, cy - 0.55, 'RUNNING', color=ACCENT, fontsize=11,
        ha='center', fontweight='bold')

# Manifestation 1: Hubble Tension (top left)
m1x, m1y = 2.5, 7.5
rect1 = FancyBboxPatch((m1x - 1.8, m1y - 0.8), 3.6, 1.6,
                         boxstyle="round,pad=0.15",
                         facecolor='#161b22', edgecolor=TORUS,
                         linewidth=2)
ax.add_patch(rect1)
ax.text(m1x, m1y + 0.3, 'HUBBLE TENSION', color=TORUS, fontsize=10,
        ha='center', fontweight='bold')
ax.text(m1x, m1y - 0.15, 'H₀ runs from 73 → 67.4', color=TEXT,
        fontsize=7, ha='center')
ax.text(m1x, m1y - 0.45, 'N ~ 100-1000 boundary crossings', color=WEAK,
        fontsize=6, ha='center')
ax.annotate('', xy=(cx - 0.8, cy + 0.8), xytext=(m1x + 0.5, m1y - 0.8),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=2))

# Manifestation 2: G Running (top right)
m2x, m2y = 10.5, 7.5
rect2 = FancyBboxPatch((m2x - 1.8, m2y - 0.8), 3.6, 1.6,
                         boxstyle="round,pad=0.15",
                         facecolor='#161b22', edgecolor=SPHERE,
                         linewidth=2)
ax.add_patch(rect2)
ax.text(m2x, m2y + 0.3, 'G RUNNING', color=SPHERE, fontsize=10,
        ha='center', fontweight='bold')
ax.text(m2x, m2y - 0.15, 'G(Earth) ≠ G(L2)?', color=TEXT,
        fontsize=7, ha='center')
ax.text(m2x, m2y - 0.45, '1 boundary: Hill sphere', color=WEAK,
        fontsize=6, ha='center')
ax.annotate('', xy=(cx + 0.8, cy + 0.8), xytext=(m2x - 0.5, m2y - 0.8),
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=2))

# Manifestation 3: QED-GR incompatibility (bottom)
m3x, m3y = 6.5, 1.2
rect3 = FancyBboxPatch((m3x - 2.5, m3y - 0.8), 5.0, 1.6,
                         boxstyle="round,pad=0.15",
                         facecolor='#161b22', edgecolor=RED,
                         linewidth=2)
ax.add_patch(rect3)
ax.text(m3x, m3y + 0.3, 'QED ↔ GR INCOMPATIBILITY', color=RED,
        fontsize=10, ha='center', fontweight='bold')
ax.text(m3x, m3y - 0.15, 'Running through ALL ~20 boundary types',
        color=TEXT, fontsize=7, ha='center')
ax.text(m3x, m3y - 0.45, 'Perturbation breaks at each confinement wall',
        color=WEAK, fontsize=6, ha='center')
ax.annotate('', xy=(cx, cy - 1.2), xytext=(m3x, m3y + 0.8),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# The key insight
ax.text(6.5, 3.0,
        'Same ε, different N:',
        color=YELLOW, fontsize=10, ha='center', fontweight='bold')
ax.text(6.5, 2.6,
        'Hubble: N ~ 1000, ε ~ 10⁻⁴  →  8% effect over cosmological distance',
        color=TORUS, fontsize=7, ha='center')
ax.text(6.5, 2.3,
        'G at L2: N = 1, ε ~ 10⁻⁴  →  0.01% effect over 1 Hill sphere',
        color=SPHERE, fontsize=7, ha='center')
ax.text(6.5, 2.0,
        'QED→GR: N ~ 20 types, ε compound  →  perturbation breakdown',
        color=RED, fontsize=7, ha='center')

# Side annotations
ax.text(0.5, 5.0, 'SOLVING ONE\nCONSTRAINS\nTHE OTHERS', color=ACCENT,
        fontsize=9, fontweight='bold')
ax.annotate('', xy=(2.5, 6.7), xytext=(1.5, 5.5),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=1.5,
                           linestyle='--'))
ax.annotate('', xy=(4.5, 1.8), xytext=(1.5, 4.5),
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=1.5,
                           linestyle='--'))

ax.text(12, 5.0, 'TESTABLE\nPREDICTIONS', color=ACCENT, fontsize=9,
        fontweight='bold')
ax.text(12, 4.3, 'Hyper-K:\nproton decay', color=TORUS, fontsize=7)
ax.text(12, 3.7, 'L1/L2:\nG measurement', color=SPHERE, fontsize=7)
ax.text(12, 3.1, 'GW sirens:\nkill test', color=RED, fontsize=7)

fig.savefig(os.path.join(OUT, 'qed_gr_05_three_manifestations.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_05_three_manifestations.png")


# ================================================================
# FIGURE 6: The Bidirectional Obstruction — QED↔GR
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(14, 7), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title('Bidirectional Obstruction: Both Directions Hit Walls',
             color=TEXT, fontsize=14, fontweight='bold', pad=12)

# Two arrows: QED→GR and GR→QED
y_top = 5.5
y_bot = 2.0

# QED → GR (top)
ax.text(0.5, y_top + 0.8, 'QED → GR', color=SPHERE, fontsize=14,
        fontweight='bold')
ax.annotate('', xy=(13, y_top), xytext=(1, y_top),
            arrowprops=dict(arrowstyle='->', color=SPHERE, lw=3))

# Walls encountered going QED→GR
walls_qed = [
    (3.0, 'Confinement\nWall', RED, 'α_s → O(1)\nPert. fails'),
    (5.5, 'Mesoscopic\nGap', WEAK, 'No clean theory\nfor ~1m objects'),
    (8.0, 'Gravitational\nOnset', TORUS, 'G becomes\nrelevant'),
    (10.5, 'Cosmological\nHorizon', PURPLE, 'Causal boundary\nlimits info'),
]

for x, name, color, desc in walls_qed:
    ax.plot([x, x], [y_top - 0.5, y_top + 0.5], color=color,
            linewidth=4, zorder=8)
    ax.text(x, y_top + 0.6, name, color=color, fontsize=7,
            ha='center', fontweight='bold')
    ax.text(x + 0.1, y_top - 0.7, desc, color=WEAK, fontsize=5.5,
            ha='center')

# GR → QED (bottom, reversed)
ax.text(12.5, y_bot + 0.8, 'GR → QED', color=TORUS, fontsize=14,
        fontweight='bold')
ax.annotate('', xy=(1, y_bot), xytext=(13, y_bot),
            arrowprops=dict(arrowstyle='->', color=TORUS, lw=3))

# Walls encountered going GR→QED
walls_gr = [
    (10.5, 'Structure\nFormation', PURPLE, 'Nonlinear GR\nno exact solutions'),
    (8.0, 'Mesoscopic\nGap', WEAK, 'Same gap\nfrom other side'),
    (5.5, 'Quantum\nOnset', SPHERE, 'Δx·Δp ≥ ℏ/2\nGeometry uncertain'),
    (3.0, 'Nuclear\nScale', RED, 'Strong force\ndominates'),
]

for x, name, color, desc in walls_gr:
    ax.plot([x, x], [y_bot - 0.5, y_bot + 0.5], color=color,
            linewidth=4, zorder=8)
    ax.text(x, y_bot - 0.8, name, color=color, fontsize=7,
            ha='center', fontweight='bold')
    ax.text(x + 0.1, y_bot + 0.6, desc, color=WEAK, fontsize=5.5,
            ha='center')

# Central observation
ax.text(7, 3.75,
        'BOTH DIRECTIONS HIT THE SAME WALLS',
        color=YELLOW, fontsize=11, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#161b22',
                  edgecolor=YELLOW, linewidth=2))

ax.text(7, 3.2,
        'The mesoscopic gap (~1 μm to ~1 km) is the hardest region:',
        color=TEXT, fontsize=8, ha='center')
ax.text(7, 2.85,
        'Too large for QED, too small for GR, too complex for exact solution.',
        color=WEAK, fontsize=7, ha='center')
ax.text(7, 2.5,
        'This is where biology lives. Soliton hierarchy is densest here.',
        color=ACCENT, fontsize=8, ha='center', fontweight='bold')

# Bottom
ax.text(7, 0.6,
        'Resolution: compute the per-boundary correction ε for each wall type.\n'
        'Run the product through all walls. The composite connects QED to GR.',
        color=TEXT, fontsize=8, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'qed_gr_06_bidirectional.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_06_bidirectional.png")


# ================================================================
# FIGURE 7: The Discrete vs Continuous — Why Reals Lose Structure
# ================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 8), facecolor=BG,
                                 gridspec_kw={'height_ratios': [1, 1]})

for ax in [ax1, ax2]:
    ax.set_facecolor(BG)
    ax.tick_params(colors=WEAK)
    for spine in ax.spines.values():
        spine.set_color(WEAK)

# Top: QED — discrete structure visible
x_qed = np.arange(0, 10, 0.01)
y_qed = np.zeros_like(x_qed)

# A piecewise function with clear rational steps
thresholds_q = [1, 2.5, 3.8, 5, 6.5, 7.8, 9]
slopes = [0.3, 0.5, 0.2, 0.7, 0.4, 0.6, 0.3]
for i in range(len(x_qed)):
    for j, (t, s) in enumerate(zip(thresholds_q, slopes)):
        if x_qed[i] > t:
            y_qed[i] += s * (x_qed[i] - t) * 0.1

# Plot with threshold markers
ax1.plot(x_qed, y_qed, color=SPHERE, linewidth=2)
for t in thresholds_q:
    ax1.axvline(x=t, color=ACCENT, linestyle=':', alpha=0.4)

# Mark the rational slopes
for j, (t, s) in enumerate(zip(thresholds_q[:-1], slopes)):
    mid = (t + thresholds_q[j+1]) / 2
    ax1.text(mid, 0.02, f'b={s}', color=ACCENT, fontsize=6,
             ha='center')

ax1.set_title('QED: Discrete Rational Structure Visible',
              color=SPHERE, fontsize=11, fontweight='bold')
ax1.set_ylabel('Coupling change', color=TEXT, fontsize=9)
ax1.text(0.5, 0.25, 'Each slope is an\nexact rational from\nDynkin indices',
         color=ACCENT, fontsize=8,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='#161b22',
                   edgecolor=ACCENT))

# Bottom: Same curve in reals — structure invisible
x_real = np.linspace(0, 10, 1000)
y_real = np.interp(x_real, x_qed, y_qed)
# Add tiny noise to simulate floating-point loss
np.random.seed(42)
y_real_noisy = y_real + np.random.normal(0, 0.001, len(y_real))

ax2.plot(x_real, y_real_noisy, color=RED, linewidth=1.5, alpha=0.8)
ax2.plot(x_real, y_real, color=WEAK, linewidth=0.5, alpha=0.3)

ax2.set_title('Same Curve in Floating-Point Reals: Rational Structure Lost',
              color=RED, fontsize=11, fontweight='bold')
ax2.set_xlabel('Energy scale (arbitrary)', color=TEXT, fontsize=9)
ax2.set_ylabel('Coupling change', color=TEXT, fontsize=9)
ax2.text(0.5, 0.25,
         'Thresholds blur into\nsmooth curve.\nRationals become\n"arbitrary reals".',
         color=RED, fontsize=8,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='#161b22',
                   edgecolor=RED))

ax2.text(6, 0.25,
         'GR sees THIS:\nsmooth geometry with no\napparent discrete structure.\n\n'
         'The discrete structure is there\nbut invisible in reals.',
         color=YELLOW, fontsize=8,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='#161b22',
                   edgecolor=YELLOW))

fig.tight_layout()
fig.savefig(os.path.join(OUT, 'qed_gr_07_discrete_vs_continuous.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_07_discrete_vs_continuous.png")


# ================================================================
# FIGURE 8: The PHYS-14 Parallel — Fermion Democracy in Both
# ================================================================

fig, ax = plt.subplots(1, 1, figsize=(13, 8), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('The Democracy Parallel: What Cancels from the Running?',
             color=TEXT, fontsize=14, fontweight='bold', pad=12)

# Left column: Gap ratio (established)
lx = 1.5

ax.text(lx, 7.2, 'GAP RATIO (PHYS-14)', color=ACCENT, fontsize=11,
        fontweight='bold')
ax.text(lx, 6.7, 'Complete fermion generations:', color=TEXT, fontsize=8)
ax.text(lx, 6.35, 'Δb₁ = Δb₂ = Δb₃ = 4/3', color=SPHERE, fontsize=9,
        fontweight='bold')
ax.text(lx, 5.9, '→ Cancel from gap ratio entirely', color=ACCENT,
        fontsize=8)
ax.text(lx, 5.5, 'Gap ratio = gauge + Higgs ONLY', color=ACCENT,
        fontsize=8, fontweight='bold')

ax.text(lx, 4.8, 'What FIXES it:', color=TEXT, fontsize=8)
ax.text(lx, 4.4, 'Asymmetric particles (VL doublet)', color=TORUS,
        fontsize=8)
ax.text(lx, 4.0, 'Δb₂/Δb₁ = 15 (maximally asymmetric)', color=TORUS,
        fontsize=8)

# Right column: QED-GR (proposed)
rx = 7.5

ax.text(rx, 7.2, 'QED → GR (PROPOSED)', color=YELLOW, fontsize=11,
        fontweight='bold')
ax.text(rx, 6.7, 'Complete boundary "generations":', color=TEXT,
        fontsize=8)
ax.text(rx, 6.35, 'Sphere types: Δα ≈ Δα for all?', color=SPHERE,
        fontsize=9, fontweight='bold')
ax.text(rx, 5.9, '→ May cancel from the running RATIO', color=YELLOW,
        fontsize=8)
ax.text(rx, 5.5, 'Net running = asymmetric types ONLY?', color=YELLOW,
        fontsize=8, fontweight='bold')

ax.text(rx, 4.8, 'What matters:', color=TEXT, fontsize=8)
ax.text(rx, 4.4, 'Asymmetric boundaries (tori, voids)', color=TORUS,
        fontsize=8)
ax.text(rx, 4.0, 'Direction-dependent correction', color=TORUS,
        fontsize=8)

# Separator
ax.plot([6.3, 6.3], [3.5, 7.5], color=WEAK, linewidth=1, linestyle=':')

# Bottom: the parallel
ax.text(6.5, 2.8, 'THE STRUCTURAL PARALLEL', color=TEXT, fontsize=12,
        ha='center', fontweight='bold')

parallels = [
    ('Symmetric corrections', 'Cancel from ratio', 'Invisible to the test'),
    ('Asymmetric corrections', 'Drive the running', 'Select the physics'),
    ('Gap ratio test', 'H₀ directional test', 'Both select asymmetry'),
]

y = 2.2
for left, right, note in parallels:
    ax.text(2.5, y, left, color=SPHERE, fontsize=8, ha='center')
    ax.text(6.5, y, '↔', color=WEAK, fontsize=10, ha='center')
    ax.text(10.5, y, right, color=TORUS, fontsize=8, ha='center')
    y -= 0.4

ax.text(6.5, 0.6,
        'If spherical boundaries cancel like fermion generations,\n'
        'the QED→GR running depends only on TOROIDAL boundaries.',
        color=ACCENT, fontsize=9, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#161b22',
                  edgecolor=ACCENT))

fig.savefig(os.path.join(OUT, 'qed_gr_08_democracy_parallel.png'),
            dpi=150, bbox_inches='tight', facecolor=BG)
plt.close(fig)
print("Saved: qed_gr_08_democracy_parallel.png")


print("\n=== ALL 8 DIAGRAMS SAVED ===")
print("Location: " + OUT + "/qed_gr_*.png")
