#!/usr/bin/env python3
"""
HOWL PHYS-52 Diagrams — The Remainder Program
8 figures covering hierarchy levels, cosmological partition, hadron Koide,
nuclear magic numbers, Hill sphere, muon g-2, hierarchy ladder, identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Wedge
import numpy as np
import os


# Light mode
if True:
    # ── Global palette (Kindle / light mode) ──
    BG      = '#ffffff'
    PAN     = '#f0ede8'
    GOLD    = '#a07820'
    SILVER  = '#505860'
    CYAN    = '#1a8a80'
    MAG     = '#a03058'
    BLUE    = '#2855a0'
    GREEN   = '#2a7a3a'
    RED     = '#b82020'
    ORANGE  = '#c06a18'
    WHITE   = '#1a1a22'
    DIM     = '#908e88'
    PURPLE  = '#6040a0'
else:
    # ── Global palette (D7.2) ──
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
    
    

def setup_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=14, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

print("PHYS-52 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: THE SEVEN HIERARCHY LEVELS
# Type: Scale/Landscape
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

levels = [
    ('1. QED', 'sub-fm', r'$\beta^2, \beta^4$', r'$\zeta, K(k), E(k)$', r'$\alpha \approx 1/137$', CYAN),
    ('2. Leptons', 'fm', 'Mass scale M', r'$a^2=2, K=2/3$', r'$\alpha$ at $m_\ell$', BLUE),
    ('3. Hadrons', 'fm', r'$\Lambda_{QCD}$', 'Confinement', r'$\alpha_s \approx 0.12$', PURPLE),
    ('4. Nuclear', 'fm-pm', r'$\hbar\omega$', 'Spin-orbit', r'$\alpha_{nuc} \sim 1$', MAG),
    ('5. Atomic', 'pm-nm', r'$R_\infty$', 'Lamb shift', r'$\alpha \approx 1/137$', GREEN),
    ('6. Planetary', 'km-AU', r'$r_s = 2GM/c^2$', 'Hill sphere', r'$GM/c^2$', ORANGE),
    ('7. Cosmos', 'Mpc+', r'$\beta$ in $\Omega$', r'$\Omega_{DM}, \Omega_b, \Omega_\Lambda$', r'$H_0$', GOLD),
]

y_start = 0.90
dy = 0.115

# Column headers
headers = ['Level', 'Scale', 'Modulus', 'Remainder', 'Coupling']
hx = [0.03, 0.16, 0.28, 0.52, 0.78]
for hdr, x in zip(headers, hx):
    ax.text(x, 0.95, hdr, color=DIM, fontsize=10, fontweight='bold',
            transform=ax.transAxes)

ax.plot([0.02, 0.98], [0.935, 0.935], color=DIM, lw=0.5,
        transform=ax.transAxes, clip_on=False)

for i, (name, scale, modulus, remainder, coupling, color) in enumerate(levels):
    y = y_start - i * dy

    # Color bar on left
    ax.plot([0.01, 0.01], [y - 0.03, y + 0.03], color=color, lw=4,
            transform=ax.transAxes, solid_capstyle='round')

    ax.text(hx[0], y, name, color=color, fontsize=11, fontweight='bold',
            transform=ax.transAxes, va='center')
    ax.text(hx[1], y, scale, color=SILVER, fontsize=9,
            transform=ax.transAxes, va='center')
    ax.text(hx[2], y, modulus, color=WHITE, fontsize=10,
            transform=ax.transAxes, va='center')
    ax.text(hx[3], y, remainder, color=WHITE, fontsize=10,
            transform=ax.transAxes, va='center')
    ax.text(hx[4], y, coupling, color=SILVER, fontsize=9,
            transform=ax.transAxes, va='center')

    # Arrow showing modulus → background
    if i < 6:
        ax.annotate('', xy=(0.25, y - dy * 0.6), xytext=(0.25, y - dy * 0.15),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=0.8),
                    transform=ax.transAxes)

# Bottom annotation
ax.text(0.5, 0.05,
        'Pattern: modulus at level N becomes fixed background at level N+1.\n'
        'Remainder at level N drives the transitions at level N.',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=1.5),
        transform=ax.transAxes)

ax.set_title('The Seven Hierarchy Levels: Modulus and Remainder',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys52_01_hierarchy_levels.png')


# ================================================================
# FIG 2: COSMOLOGICAL INERTIAL PARTITION
# Type: Comparison Bar (horizontal stacked)
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', '')

omega_dm = np.pi / 12
omega_b = 13.0 / 264
omega_lambda = 1 - omega_dm - omega_b

# Stacked horizontal bar
bar_y = 0.5
bar_h = 0.3

ax.barh(bar_y, omega_dm, bar_h, left=0, color=CYAN, alpha=0.7)
ax.barh(bar_y, omega_b, bar_h, left=omega_dm, color=BLUE, alpha=0.7)
ax.barh(bar_y, omega_lambda, bar_h, left=omega_dm + omega_b, color=GOLD, alpha=0.7)

# Labels inside bars
ax.text(omega_dm / 2, bar_y, r'$\Omega_{DM}$' + '\n' + r'$= \pi/12$' + '\n= 26.2%',
        color=BG, fontsize=10, fontweight='bold', ha='center', va='center')
ax.text(omega_dm + omega_b / 2, bar_y + 0.22,
        r'$\Omega_b = 13/264$' + '\n= 4.9%',
        color=BLUE, fontsize=9, fontweight='bold', ha='center', va='center')
ax.text(omega_dm + omega_b + omega_lambda / 2, bar_y,
        r'$\Omega_\Lambda$' + '\n' + r'$= \frac{251 - 22\pi}{264}$' + '\n= 68.9%',
        color=BG, fontsize=10, fontweight='bold', ha='center', va='center')

# Measured comparison
meas_y = 0.1
ax.barh(meas_y, 0.2607, bar_h * 0.5, left=0, color=CYAN, alpha=0.3)
ax.barh(meas_y, 0.0490, bar_h * 0.5, left=0.2607, color=BLUE, alpha=0.3)
ax.barh(meas_y, 0.6847, bar_h * 0.5, left=0.2607 + 0.0490, color=GOLD, alpha=0.3)

ax.text(0.5, meas_y, 'Planck 2018 measured', color=SILVER, fontsize=9,
        ha='center', va='center')

# Miss labels
misses = [
    (omega_dm / 2, 0.82, r'$\Omega_{DM}$: 0.42%', CYAN),
    (omega_dm + omega_b / 2, 0.82, r'$\Omega_b$: 0.49%', BLUE),
    (omega_dm + omega_b + omega_lambda / 2, 0.82, r'$\Omega_\Lambda$: 0.62%', GOLD),
]
for x, y, text, color in misses:
    ax.text(x, y, text, color=color, fontsize=10, fontweight='bold',
            ha='center')

ax.set_xlim(0, 1.05)
ax.set_ylim(-0.1, 1.0)
ax.set_yticks([])

ax.set_title(r'Cosmological Inertial Partition: $\pi/12 + 13/264 + (251-22\pi)/264 = 1$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_02_cosmological_partition.png')


# ================================================================
# FIG 3: HADRON KOIDE TRIPLETS
# Type: Running/Convergence
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Koide K')

triplets = [
    (r'$e, \mu, \tau$', 0.6667, GOLD),
    (r'$\pi, K, D$', 0.5967, ORANGE),
    (r'$\pi, K, \eta$', 0.3867, GREEN),
    (r'$p, n, \Lambda$', 0.3379, CYAN),
    (r'$\Sigma^+, \Xi^0, \Omega^-$', 0.3391, BLUE),
    (r'$\rho, K^*, \phi$', 0.3369, PURPLE),
    (r'$\Sigma^+, \Sigma^0, \Sigma^-$', 0.3333, MAG),
    (r'$W, Z, H$', 0.3363, RED),
]

x_pos = np.arange(len(triplets))

for i, (label, k_val, color) in enumerate(triplets):
    ax.plot(i, k_val, 'o', color=color, markersize=14, zorder=5)
    ax.text(i, k_val + 0.015, '%.4f' % k_val, color=WHITE, fontsize=8,
            ha='center', fontweight='bold')

# Reference lines
ax.axhline(2/3, color=GOLD, lw=2, ls='--', alpha=0.6, label='2/3 = R₃/R₂')
ax.axhline(1/3, color=DIM, lw=1.5, ls='--', alpha=0.4, label='1/3 = 1/N (equal masses)')
ax.axhline(3/5, color=ORANGE, lw=1, ls=':', alpha=0.3, label='3/5')

# Annotations
ax.annotate('ONLY leptons\nmatch 2/3', xy=(0, 0.6667),
            xytext=(2, 0.62), color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.text(5.5, 0.345, 'Near-degenerate\ntriplets cluster\nat 1/3',
        color=DIM, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                  edgecolor=DIM, linewidth=1))

ax.set_xticks(x_pos)
ax.set_xticklabels([t[0] for t in triplets], color=WHITE, fontsize=9,
                    rotation=30, ha='right')
ax.set_ylim(0.28, 0.72)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9,
          loc='upper right')

ax.set_title('Hadron Koide Triplets: Only Leptons Match K = 2/3',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_03_hadron_koide.png')


# ================================================================
# FIG 4: NUCLEAR MAGIC NUMBERS
# Type: Scale/Landscape
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Magic Number', 'Difference from Previous')

magic = [2, 8, 20, 28, 50, 82, 126]
diffs = [6, 12, 8, 22, 32, 44]

x_pos = np.arange(len(diffs))
colors_bars = [DIM, DIM, DIM, GOLD, DIM, GOLD]

bars = ax.bar(x_pos, diffs, 0.6, color=colors_bars, alpha=0.7)

# Labels
for i, (d, m1, m2) in enumerate(zip(diffs, magic[:-1], magic[1:])):
    ax.text(i, d + 1, str(d), color=WHITE, fontsize=12,
            ha='center', fontweight='bold')
    label = '%d→%d' % (m1, m2)
    ax.text(i, -3, label, color=SILVER, fontsize=9, ha='center')

# Highlight 11 multiples
ax.text(3, diffs[3] + 4, '22 = 2 × 11', color=GOLD, fontsize=10,
        ha='center', fontweight='bold')
ax.text(5, diffs[5] + 4, '44 = 4 × 11', color=GOLD, fontsize=10,
        ha='center', fontweight='bold')

# 11 reference
ax.axhline(11, color=GOLD, lw=1, ls=':', alpha=0.3)
ax.axhline(22, color=GOLD, lw=1, ls=':', alpha=0.3)
ax.axhline(44, color=GOLD, lw=1, ls=':', alpha=0.3)
ax.text(5.7, 11, '11', color=GOLD, fontsize=8, alpha=0.5)
ax.text(5.7, 22, '22', color=GOLD, fontsize=8, alpha=0.5)
ax.text(5.7, 44, '44', color=GOLD, fontsize=8, alpha=0.5)

# Verdict
ax.text(2.5, 50,
        '11 = Yang-Mills coefficient appears in differences 22 and 44.\n'
        'Almost certainly coincidental — magic numbers arise from\n'
        'spin-orbit coupling, not gauge theory.',
        color=SILVER, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=DIM, linewidth=1))

ax.set_xticks(x_pos)
ax.set_xticklabels([''] * len(diffs))
ax.set_ylim(-5, 58)

ax.set_title('Nuclear Magic Number Differences: 11-Multiples Likely Coincidental',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_04_nuclear_magic.png')


# ================================================================
# FIG 5: HILL SPHERE AS SOLITON BOUNDARY
# Type: Geometric Cross-Section
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.0, 2.0)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Sun (large, left)
sun = Circle((-1.8, 0), 0.3, facecolor=GOLD, alpha=0.3)
ax.add_patch(sun)
ax.text(-1.8, 0, 'Star\n(M)', color=GOLD, fontsize=10, ha='center',
        va='center', fontweight='bold')

# Planet (small, center)
planet = Circle((0, 0), 0.12, facecolor=CYAN, alpha=0.5)
ax.add_patch(planet)
ax.text(0, 0, 'Planet\n(m)', color=CYAN, fontsize=8, ha='center',
        va='center', fontweight='bold')

# Hill sphere boundary (egg-shaped, approximated as ellipse)
theta = np.linspace(0, 2 * np.pi, 200)
r_h = 0.8  # normalized
# Slight egg shape
r_hill = r_h * (1 + 0.1 * np.cos(theta))
x_hill = r_hill * np.cos(theta)
y_hill = r_hill * np.sin(theta) * 0.85
ax.plot(x_hill, y_hill, color=GREEN, lw=2, ls='--', alpha=0.7)
ax.text(0.9, 0.5, 'Hill sphere\nboundary', color=GREEN, fontsize=9,
        fontweight='bold')

# Orbit line
orbit_theta = np.linspace(-0.3, 0.3, 50)
orbit_r = 1.8
ax.plot(orbit_r * np.cos(orbit_theta + np.pi),
        orbit_r * np.sin(orbit_theta + np.pi) * 3,
        color=DIM, lw=1, ls=':', alpha=0.5)

# Formula
ax.text(0, -1.4,
        r'$\frac{r_H}{a} = \left(\frac{m}{3M}\right)^{1/3}$',
        color=WHITE, fontsize=18, ha='center')

# Decomposition
ax.text(0, -1.75,
        'Modulus: exponent 1/3 (from 3D gravity)\n'
        'Remainder: mass ratio m/M (specific inertia)',
        color=SILVER, fontsize=10, ha='center')

# Labels for L1 and L2 points
ax.plot(r_h, 0, 'x', color=RED, markersize=10, mew=2)
ax.text(r_h + 0.1, 0.1, 'L₁', color=RED, fontsize=10, fontweight='bold')
ax.plot(-r_h * 1.05, 0, 'x', color=RED, markersize=10, mew=2)
ax.text(-r_h * 1.05 - 0.15, 0.1, 'L₂', color=RED, fontsize=10, fontweight='bold')

# Inside vs outside
ax.text(0, 0.35, "Planet's\ngravity\ndominates", color=CYAN, fontsize=8,
        ha='center', alpha=0.7, style='italic')
ax.text(1.5, 1.2, "Star's gravity\ndominates", color=GOLD, fontsize=8,
        ha='center', alpha=0.7, style='italic')

ax.set_title('Hill Sphere as Soliton Boundary: Modulus (1/3) + Remainder (m/M)',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_05_hill_sphere.png')


# ================================================================
# FIG 6: MUON g-2 TOROIDAL CONTRIBUTION
# Type: Threshold/Region
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'Contribution to $a_\mu$ ($\times 10^{-9}$)')

categories = [
    'QED\n(published)', 'Hadronic\nLO', 'Hadronic\nNLO', 'Hadronic\nLBL',
    'EW', 'Toroidal\n4-loop']
values = [11658471.89, 69.31, -9.83, 9.20, 1.54, 1.28]  # in 10^-9 relative scale
# Show only the small contributions (not QED which is huge)
values_small = [69.31, -9.83, 9.20, 1.54, 1.28]
labels_small = ['Hadronic\nLO', 'Hadronic\nNLO', 'Hadronic\nLBL', 'EW',
                'Toroidal\n4-loop']
colors_small = [CYAN, BLUE, PURPLE, GREEN, GOLD]

x_pos = np.arange(len(values_small))

for i, (v, c) in enumerate(zip(values_small, colors_small)):
    ax.bar(i, v, 0.6, color=c, alpha=0.7)
    pos = v + 2 if v > 0 else v - 4
    ax.text(i, pos, '%.2f' % v, color=WHITE, fontsize=10,
            ha='center', fontweight='bold')

# Anomaly band
ax.axhline(0, color=DIM, lw=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels(labels_small, color=WHITE, fontsize=9)
ax.set_ylim(-15, 80)

# Anomaly comparison box
ax.text(3.5, 60,
        'R-ratio anomaly: ~2.5\n'
        'Toroidal 4-loop: 1.28\n'
        'Ratio: 51%\n\n'
        r'Toroidal = $(m_\mu/m_e)^2 \times$'
        '\nelectron 4-loop',
        color=GOLD, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=1.5))

ax.set_title(r'Muon $g-2$: Toroidal 4-Loop Contribution = 51% of R-Ratio Anomaly',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_06_muon_g2_toroidal.png')


# ================================================================
# FIG 7: THE HIERARCHY LADDER
# Type: Running/Convergence
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

levels_ladder = [
    ('QED', r'$\beta = \pi/4$', r'$\alpha$ = number', CYAN),
    ('Leptons', 'Mass scale M', r'$m_e, m_\mu, m_\tau$ = masses', BLUE),
    ('QCD', r'$\Lambda_{QCD}$', r'$m_p$ = 938 MeV', PURPLE),
    ('Nuclear', r'$\hbar\omega$', 'Nuclear masses', MAG),
    ('Atomic', r'$R_\infty$', 'Bond energies', GREEN),
    ('Planetary', r'$r_s = 2GM/c^2$', 'Orbital params', ORANGE),
    ('Cosmos', r'$H_0, \Omega_{tot}$', 'Age of universe', GOLD),
]

n_levels = len(levels_ladder)
x_left = 0.15
x_right = 0.65
y_top = 0.90
y_bot = 0.10
dy = (y_top - y_bot) / (n_levels - 1)

for i, (name, modulus, becomes, color) in enumerate(levels_ladder):
    y = y_top - i * dy

    # Level box
    ax.text(x_left, y, name, color=color, fontsize=12, fontweight='bold',
            ha='center', va='center', transform=ax.transAxes)

    # Modulus at this level
    ax.text(x_left + 0.15, y, 'Modulus: ' + modulus, color=WHITE, fontsize=9,
            ha='left', va='center', transform=ax.transAxes)

    # Arrow to next level showing what it becomes
    if i < n_levels - 1:
        y_next = y_top - (i + 1) * dy
        ax.annotate('', xy=(x_right, y_next + 0.02),
                    xytext=(x_right, y - 0.02),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5),
                    transform=ax.transAxes)
        ax.text(x_right + 0.05, (y + y_next) / 2,
                'becomes:\n' + becomes, color=DIM, fontsize=8,
                ha='left', va='center', transform=ax.transAxes)

    # Horizontal line
    ax.plot([0.05, 0.95], [y - dy / 2, y - dy / 2], color=DIM, lw=0.3,
            alpha=0.3, transform=ax.transAxes)

ax.text(0.5, 0.03,
        'Each level absorbs the modulus from below as fixed background.\n'
        'The remainder at each level is the active physics.',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=1.5),
        transform=ax.transAxes)

ax.set_title('The Hierarchy Ladder: Modulus at N Becomes Background at N+1',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys52_07_hierarchy_ladder.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE REMAINDER PROGRAM
# Type: Identity Card
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Title
ax.text(0.5, 0.96, 'THE REMAINDER PROGRAM', color=GOLD, fontsize=22,
        fontweight='bold', ha='center')
ax.text(0.5, 0.925, 'PHYS-52: Inertial Decomposition at Seven Hierarchy Levels',
        color=SILVER, fontsize=12, ha='center')

# ── Left column: THE CLAIM ──
ax.text(0.02, 0.87, 'THE CLAIM', color=CYAN, fontsize=13, fontweight='bold')

claim_lines = [
    'Remainder = inertia (not metaphor)',
    'Modulus = geometry (boundary conditions)',
    'Mass, energy, entropy, coupling = same thing',
    'Shell jumps when remainder > modulus boundary',
    'Modulus at level N = background at level N+1',
]
for i, line in enumerate(claim_lines):
    ax.text(0.04, 0.82 - i * 0.035, line, color=SILVER, fontsize=9)

# ── Left column: RESULTS BY LEVEL ──
ax.text(0.02, 0.62, 'RESULTS BY LEVEL', color=CYAN, fontsize=13,
        fontweight='bold')

results = [
    ('QED', r'$a_e$ at 0.22 ppb, 3 layers resolved', GREEN, 'PASS'),
    ('Leptons', 'K = R3/R2 at 9.2 ppm, 4-loop toward', GREEN, 'PASS'),
    ('Hadrons', 'Only leptons match 2/3, rest at 1/3', SILVER, 'PARTIAL'),
    ('Nuclear', 'No beta in magic numbers', RED, 'NULL'),
    ('Atomic', 'H 1S-2S at 0.44 ppb (existing)', GREEN, 'PASS'),
    ('Planetary', 'Hill sphere = modulus + remainder', SILVER, 'CONSISTENT'),
    ('Cosmos', 'All 4 densities sub-1%', GREEN, 'PASS'),
]

for i, (level, detail, color, status) in enumerate(results):
    y = 0.57 - i * 0.04
    ax.text(0.04, y, level + ':', color=color, fontsize=9, fontweight='bold')
    ax.text(0.16, y, detail, color=SILVER, fontsize=8)
    ax.text(0.47, y, status, color=color, fontsize=8, fontweight='bold')

# ── Right column: COSMOLOGICAL PARTITION ──
ax.text(0.52, 0.87, 'COSMOLOGICAL PARTITION', color=GOLD, fontsize=13,
        fontweight='bold')

cosmo_lines = [
    (r'$\Omega_{DM} = \pi/12 = 0.262$', '0.42%', CYAN),
    (r'$\Omega_b = 13/264 = 0.049$', '0.49%', BLUE),
    (r'DM/baryon $= 22\pi/13 = 5.317$', '0.064%', GREEN),
    (r'$\Omega_\Lambda = (251-22\pi)/264 = 0.689$', '0.62%', GOLD),
    (r'Sum $= 1$ (exact)', '', WHITE),
]

for i, (expr, miss, color) in enumerate(cosmo_lines):
    y = 0.82 - i * 0.04
    ax.text(0.54, y, expr, color=color, fontsize=9)
    if miss:
        ax.text(0.88, y, 'miss: ' + miss, color=DIM, fontsize=8)

# ── Right column: GAUGE INTEGERS IN Ω_Λ ──
ax.text(0.52, 0.60, r'INTEGERS IN $(251-22\pi)/264$', color=GOLD,
        fontsize=11, fontweight='bold')

int_lines = [
    ('11', 'Yang-Mills coefficient', GOLD),
    ('13', 'Modified SU(2) numerator', GOLD),
    ('8', 'dim(SU(3) adjoint)', GOLD),
    ('3', 'Generations / spatial dim', GOLD),
    ('264 = 8 x 3 x 11', 'Product of gauge dimensions', WHITE),
    ('251 = 264 - 13', 'Remove SU(2) shift', WHITE),
]

for i, (val, meaning, color) in enumerate(int_lines):
    y = 0.55 - i * 0.033
    ax.text(0.54, y, val, color=color, fontsize=9, fontweight='bold')
    ax.text(0.72, y, meaning, color=SILVER, fontsize=8)

# ── Bottom: KILL SWITCHES ──
ax.text(0.02, 0.27, 'KILL SWITCHES', color=RED, fontsize=13,
        fontweight='bold')

kills = [
    r'1. CMB-S4 excludes $\Omega_\Lambda = 0.689$ at $>2\sigma$',
    r'2. Improved Planck excludes DM/baryon $= 22\pi/13$',
    r'3. Muon $g-2$ toroidal has wrong sign',
    r'4. Hadron triplet found with K = 2/3 at $<$100 ppm',
    r'5. $A_5$ cancellation below 99.9% for spherical part',
    r'6. Belle II $\tau$ mass worsens Koide miss beyond 20 ppm',
]

for i, text in enumerate(kills):
    col = i // 3
    row = i % 3
    x = 0.04 + col * 0.48
    y = 0.22 - row * 0.03
    ax.text(x, y, text, color=DIM, fontsize=8)

# ── Bottom center: THE BOTTOM LINE ──
ax.text(0.5, 0.08,
        'Seven levels tested. Four passed. Two partial. One null.\n'
        r'Strongest result: $\Omega_\Lambda = (251-22\pi)/264$ at 0.62% from Planck.',
        color=WHITE, fontsize=10, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=2))

save(fig, 'phys52_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys52_01_hierarchy_levels.png")
print("  phys52_02_cosmological_partition.png")
print("  phys52_03_hadron_koide.png")
print("  phys52_04_nuclear_magic.png")
print("  phys52_05_hill_sphere.png")
print("  phys52_06_muon_g2_toroidal.png")
print("  phys52_07_hierarchy_ladder.png")
print("  phys52_08_identity_card.png")
print("=" * 50)
