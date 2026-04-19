#!/usr/bin/env python3
"""
HOWL PHYS-53 Diagrams — The Giga Remainder Test
8 figures covering scoreboard, CKM integers, cosmological partition,
hadron Koide map, microscopic-cosmic bridge, Hubble tension,
soliton hierarchy, and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
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

print("PHYS-53 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: THE SCOREBOARD — 15 results by precision tier
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Miss (log scale)')

results = [
    (r'$\Sigma$ K=1/3',        1.9e-4,   'Hadron',     GREEN),
    (r'Lepton K=2/3',          9.2e-4,   'Lepton',     CYAN),
    (r'$|V_{us}|$=9/40',       4.4e-3,   'Particle',   BLUE),
    (r'$\Omega_\Lambda$',      8.5e-3,   'Cosmos',     GOLD),
    (r'Bridge 3$(M_Z/m_e)^2$', 3.0e-2,   'QED-Cosmos', PURPLE),
    (r'DM/baryon=22$\pi$/13',  7.25e-2,  'Cosmos',     GOLD),
    (r'$a_A/a_V$=3/2',         0.21,     'Nuclear',    GREEN),
    (r'$|V_{cb}|$=1/24',       0.37,     'Particle',   BLUE),
    (r'$\Omega_{DM}=\pi/12$',  0.42,     'Cosmos',     GOLD),
    (r'$\Omega_b$=13/264',     0.49,     'Cosmos',     GOLD),
    (r'$H_0$ ratio=12/11',     0.67,     'Cosmos',     GOLD),
    (r'Chandra=15$\pi$/8',     0.93,     'Stellar',    ORANGE),
    (r'$|V_{ub}|$=1/264',      2.79,     'Particle',   RED),
    (r'$|V_{cb}/V_{ub}|$=11',  3.07,     'Particle',   RED),
    (r'Muon toroidal',         40.3,     'Lepton',     DIM),
]

y_pos = np.arange(len(results))
miss_vals = [r[1] for r in results]
bar_colors = [r[3] for r in results]
labels = [r[0] for r in results]
domains = [r[2] for r in results]

bars = ax.barh(y_pos, miss_vals, 0.6, color=bar_colors, alpha=0.7)

ax.set_xscale('log')
ax.set_xlim(5e-5, 100)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, color=WHITE, fontsize=9)
ax.invert_yaxis()

# Miss labels
for i, (label, miss, domain, color) in enumerate(results):
    if miss < 0.001:
        txt = '%.1f ppm' % (miss * 1e4)
    elif miss < 0.1:
        txt = '%.0f ppm' % (miss * 1e4)
    elif miss < 10:
        txt = '%.2f%%' % miss
    else:
        txt = '%.0f%%' % miss
    x_pos = miss * 1.5
    ax.text(x_pos, i, txt, color=WHITE, fontsize=8, va='center', fontweight='bold')

    # Domain label on right
    ax.text(80, i, domain, color=DIM, fontsize=7, va='center', ha='right')

# Tier dividers
ax.axvline(0.01, color=CYAN, lw=1, ls=':', alpha=0.3)
ax.axvline(0.1, color=GREEN, lw=1, ls=':', alpha=0.3)
ax.axvline(1.0, color=GOLD, lw=1.5, ls='--', alpha=0.4)

ax.text(0.003, -0.8, 'Sub-100 ppm', color=CYAN, fontsize=8, ha='center')
ax.text(0.03, -0.8, 'Sub-0.1%', color=GREEN, fontsize=8, ha='center')
ax.text(0.3, -0.8, 'Sub-1%', color=GOLD, fontsize=8, ha='center')
ax.text(5, -0.8, 'Fail', color=RED, fontsize=8, ha='center')

# Status counts
ax.text(0.0001, 15.5, '8 PASS  |  2 FAIL  |  1 INFO', color=WHITE,
        fontsize=11, fontweight='bold')

ax.set_title('The Giga Remainder Scoreboard: 15 Results Across 7 Levels',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_01_scoreboard.png')


# ================================================================
# FIG 2: CKM ELEMENTS AS GAUGE INTEGER FRACTIONS
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Three CKM elements as fraction diagrams
elements = [
    (r'$|V_{us}|$', '9/40', r'$\frac{3^2}{8 \times 5}$',
     '0.22500', '0.22501', '44 ppm', 0.20, CYAN, True),
    (r'$|V_{cb}|$', '1/24', r'$\frac{1}{8 \times 3}$',
     '0.04167', '0.04182', '0.37%', 0.50, BLUE, True),
    (r'$|V_{ub}|$', '1/264', r'$\frac{1}{8 \times 3 \times 11}$',
     '0.003788', '0.003685', '2.79%', 0.80, RED, False),
]

for name, frac, expr, pred, meas, miss, x_pos, color, passed in elements:
    y_top = 0.85

    ax.text(x_pos, y_top, name, color=color, fontsize=18, fontweight='bold',
            ha='center')
    ax.text(x_pos, y_top - 0.08, '= ' + frac, color=WHITE, fontsize=14,
            ha='center')
    ax.text(x_pos, y_top - 0.16, '= ' + expr, color=WHITE, fontsize=16,
            ha='center')
    ax.text(x_pos, y_top - 0.27, 'predicted: ' + pred, color=SILVER,
            fontsize=10, ha='center')
    ax.text(x_pos, y_top - 0.32, 'measured:  ' + meas, color=SILVER,
            fontsize=10, ha='center')

    status_color = GREEN if passed else RED
    status_text = 'PASS (%s)' % miss if passed else 'FAIL (%s)' % miss
    ax.text(x_pos, y_top - 0.40, status_text, color=status_color,
            fontsize=12, fontweight='bold', ha='center')

# Common factor box
ax.text(0.50, 0.22,
        'Common factor: 8 = dim(SU(3) adjoint)\n\n'
        'Denominators:  40 = 8×5    24 = 8×3    264 = 8×3×11\n\n'
        r'Ratio: $|V_{cb}|/|V_{ub}|$ = 264/24 = 11 (Yang-Mills)',
        color=WHITE, fontsize=11, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                  edgecolor=GOLD, linewidth=1.5))

ax.set_title('CKM Matrix from Gauge-Group Integers',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys53_02_ckm_integers.png')


# ================================================================
# FIG 3: COSMOLOGICAL PARTITION
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', '')

omega_dm = np.pi / 12
omega_b = 13.0 / 264
omega_lambda = 1 - omega_dm - omega_b

bar_y = 0.6
bar_h = 0.25

# Stacked bar
ax.barh(bar_y, omega_dm, bar_h, left=0, color=CYAN, alpha=0.7)
ax.barh(bar_y, omega_b, bar_h, left=omega_dm, color=BLUE, alpha=0.7)
ax.barh(bar_y, omega_lambda, bar_h, left=omega_dm + omega_b, color=GOLD, alpha=0.7)

# Labels
ax.text(omega_dm / 2, bar_y, r'$\Omega_{DM}$' + '\n' + r'$\pi/12$' + '\n26.2%',
        color=BG, fontsize=9, fontweight='bold', ha='center', va='center')
ax.text(omega_dm + omega_b / 2, bar_y + 0.18,
        r'$\Omega_b = 13/264$' + '\n4.9%',
        color=BLUE, fontsize=8, fontweight='bold', ha='center')
ax.text(omega_dm + omega_b + omega_lambda / 2, bar_y,
        r'$\Omega_\Lambda$' + '\n' + r'$\frac{251 - 22\pi}{264}$' + '\n68.9%',
        color=BG, fontsize=9, fontweight='bold', ha='center', va='center')

# Planck comparison
meas_y = 0.25
ax.barh(meas_y, 0.2607, bar_h * 0.5, left=0, color=CYAN, alpha=0.3)
ax.barh(meas_y, 0.0490, bar_h * 0.5, left=0.2607, color=BLUE, alpha=0.3)
ax.barh(meas_y, 0.6889, bar_h * 0.5, left=0.3097, color=GOLD, alpha=0.3)
ax.text(0.5, meas_y, 'Planck 2018', color=SILVER, fontsize=9, ha='center',
        va='center')

# Miss annotations
misses = [
    (omega_dm / 2, 0.88, '0.42%', CYAN),
    (omega_dm + omega_b + omega_lambda / 2, 0.88, '85 ppm', GOLD),
]
for x, y, txt, c in misses:
    ax.text(x, y, txt, color=c, fontsize=11, fontweight='bold', ha='center')

# Integer decomposition
ax.text(0.5, 0.07,
        '264 = 8 × 3 × 11     251 = 264 − 13     22 = 2 × 11',
        color=DIM, fontsize=10, ha='center')

ax.set_xlim(0, 1.05)
ax.set_ylim(0, 1.0)
ax.set_yticks([])

ax.set_title(r'Cosmological Partition: $\pi/12 + 13/264 + (251-22\pi)/264 = 1$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_03_cosmological_partition.png')


# ================================================================
# FIG 4: HADRON KOIDE TWO-POSITION MAP
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$a^2$ (amplitude squared)', 'Koide K')

# Data points
triplets = [
    (r'$e,\mu,\tau$', 2.0000, 0.6667, GOLD, 16),
    (r'$\Sigma^+,\Sigma^0,\Sigma^-$', 0.000004, 0.33333, CYAN, 14),
    (r'$\Upsilon$ 1S,2S,3S', 0.00069, 0.33345, CYAN, 10),
    (r'p,n,$\Lambda$', 0.0034, 0.33390, BLUE, 10),
    (r'$\rho,K^*,\phi$', 0.0062, 0.33437, PURPLE, 10),
    (r'$\Sigma,\Xi,\Omega$', 0.0105, 0.33509, BLUE, 10),
    (r'W,Z,H', 0.0181, 0.33635, ORANGE, 10),
    (r'$\pi,K,\eta$', 0.148, 0.358, DIM, 8),
    (r'$\pi,K,D$', 0.515, 0.419, DIM, 8),
    (r'down quarks', 2.388, 0.731, MAG, 10),
    (r'up quarks', 3.093, 0.849, MAG, 10),
]

# Theoretical curve K = (1 + a2/2)/3
a2_curve = np.linspace(0, 4, 200)
k_curve = (1 + a2_curve / 2) / 3
ax.plot(a2_curve, k_curve, color=DIM, lw=1, ls='--', alpha=0.4)

# Reference lines
ax.axhline(2/3, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.axhline(1/3, color=CYAN, lw=1.5, ls='--', alpha=0.5)
ax.axvline(2.0, color=GOLD, lw=1, ls=':', alpha=0.3)

ax.text(3.8, 2/3 + 0.01, '2/3', color=GOLD, fontsize=12, fontweight='bold')
ax.text(3.8, 1/3 + 0.01, '1/3', color=CYAN, fontsize=12, fontweight='bold')

# Plot points
for label, a2, k, color, size in triplets:
    ax.plot(a2, k, 'o', color=color, markersize=size, zorder=5, alpha=0.8)

# Labels for key points
ax.annotate(r'$e,\mu,\tau$' + '\nK=2/3, 9.2 ppm',
            xy=(2.0, 0.6667), xytext=(2.8, 0.62),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax.annotate(r'$\Sigma$ triplet' + '\nK=1/3, 1.9 ppm',
            xy=(0.0, 0.3333), xytext=(0.5, 0.38),
            color=CYAN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.annotate('quarks\n(beyond critical)',
            xy=(2.7, 0.79), xytext=(3.3, 0.78),
            color=MAG, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1))

# Position labels
ax.text(0.15, 0.30, 'POLE\n(symmetric)', color=CYAN, fontsize=9,
        ha='center', style='italic')
ax.text(2.0, 0.70, 'CRITICAL\n(equator)', color=GOLD, fontsize=9,
        ha='center', style='italic')

ax.set_xlim(-0.2, 4.2)
ax.set_ylim(0.28, 0.90)

ax.set_title('The Two-Position Koide Map: Leptons at 2/3, Everything Else at 1/3',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_04_koide_two_position.png')


# ================================================================
# FIG 5: MICROSCOPIC-COSMIC BRIDGE
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Three nodes: microscopic, bridge, cosmic
nodes = [
    (0.15, 0.5, 'MICROSCOPIC\n(QED 4-loop)', CYAN,
     r'$|A_4| \times (\alpha/\pi)^4$' + '\n= 5.567 × 10⁻¹¹',
     'Laporta constants\nTopology 81, 83'),
    (0.50, 0.5, 'BRIDGE\n(Electroweak)', PURPLE,
     r'$3 \times (M_Z/m_e)^2$' + '\n= 9.553 × 10¹⁰',
     'Z boson mass\n× 3 (dimensions)'),
    (0.85, 0.5, 'COSMIC\n(DM/baryon)', GOLD,
     r'$22\pi/13$' + '\n= 5.317',
     'Planck CMB\nGauge integers'),
]

for x, y, title, color, formula, detail in nodes:
    ax.plot(x, y, 'o', color=color, markersize=30, zorder=5, alpha=0.7)
    ax.text(x, y + 0.15, title, color=color, fontsize=12, fontweight='bold',
            ha='center')
    ax.text(x, y - 0.08, formula, color=WHITE, fontsize=10, ha='center')
    ax.text(x, y - 0.20, detail, color=SILVER, fontsize=8, ha='center')

# Arrows
ax.annotate('', xy=(0.40, 0.5), xytext=(0.24, 0.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))
ax.annotate('', xy=(0.76, 0.5), xytext=(0.60, 0.5),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))

ax.text(0.32, 0.55, r'$\times$', color=WHITE, fontsize=16, ha='center')
ax.text(0.68, 0.55, r'$=$', color=WHITE, fontsize=16, ha='center')

# The formula
ax.text(0.50, 0.18,
        r'$\frac{22\pi}{13} = |A_4| \times \left(\frac{\alpha}{\pi}\right)^4'
        r'\times 3 \times \left(\frac{M_Z}{m_e}\right)^2$',
        color=GOLD, fontsize=18, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                  edgecolor=GOLD, linewidth=2))

# Miss
ax.text(0.50, 0.08, 'Five quantities, three domains, one formula. Miss: 300 ppm.',
        color=SILVER, fontsize=11, ha='center')

ax.set_title(r'The Microscopic-Cosmic Bridge: $A_4 \to 3(M_Z/m_e)^2 \to 22\pi/13$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_05_bridge.png')


# ================================================================
# FIG 6: HUBBLE TENSION AS 12/11
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'$H_0$ (km/s/Mpc)')

# Two measurement bars
ax.barh(1.0, 67.4, 0.3, left=0, color=CYAN, alpha=0.7)
ax.barh(0.5, 73.04, 0.3, left=0, color=ORANGE, alpha=0.7)

# Uncertainty bands
ax.barh(1.0, 1.0, 0.3, left=66.9, color=CYAN, alpha=0.15)
ax.barh(0.5, 2.08, 0.3, left=72.0, color=ORANGE, alpha=0.15)

# Labels
ax.text(67.4, 1.18, 'CMB (Planck): 67.4 ± 0.5', color=CYAN, fontsize=11,
        fontweight='bold')
ax.text(73.04, 0.68, 'Local (SH0ES): 73.04 ± 1.04', color=ORANGE, fontsize=11,
        fontweight='bold')

# Predicted
ax.axvline(73.53, color=GOLD, lw=2, ls='--', alpha=0.7)
ax.text(73.53, 1.5, '67.4 × 12/11\n= 73.53', color=GOLD, fontsize=11,
        fontweight='bold', ha='center')

# The ratio box
ax.text(70, 0.15,
        r'Ratio = $\frac{H_0^{local}}{H_0^{CMB}}$ = 1.084  vs  $\frac{12}{11}$ = 1.091'
        '\n\nMiss: 0.67%\n\n11 = Yang-Mills coefficient',
        color=WHITE, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=1.5))

ax.set_xlim(64, 78)
ax.set_ylim(-0.2, 1.7)
ax.set_yticks([])

ax.set_title('Hubble Tension as 12/11: Not a Discrepancy, a Prediction',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_06_hubble_tension.png')


# ================================================================
# FIG 7: SOLITON HIERARCHY — CMB as vacuum, expansion as boundary
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Concentric circles representing soliton levels
levels = [
    (2.0, GOLD, r'Expansion ($\Omega_\Lambda$ = 68.9%)', 'Soliton boundary'),
    (1.5, CYAN, r'Dark Matter ($\Omega_{DM}$ = 26.2%)', 'Spherical modulus'),
    (1.0, BLUE, r'Baryons ($\Omega_b$ = 4.9%)', 'Gauge integers'),
    (0.5, GREEN, 'Stars, Planets', 'Lower solitons'),
    (0.15, WHITE, 'Atoms, Nuclei', 'Inner hierarchy'),
]

for radius, color, label, sublabel in levels:
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(radius * np.cos(theta), radius * np.sin(theta),
            color=color, lw=2 if radius > 0.3 else 1, alpha=0.6)

# CMB label at inner edge of DM shell
ax.text(0, -1.25, 'CMB\n(soliton vacuum)', color=CYAN, fontsize=10,
        ha='center', fontweight='bold', style='italic')

# Expansion label at outer edge
ax.text(0, 2.2, 'Accelerating Expansion\n(soliton boundary)',
        color=GOLD, fontsize=10, ha='center', fontweight='bold', style='italic')

# Labels on right side
label_x = 2.6
for radius, color, label, sublabel in levels:
    ax.text(label_x, radius - 0.05, label, color=color, fontsize=8,
            va='center')

# Center
ax.plot(0, 0, 'o', color=WHITE, markersize=6, zorder=5)
ax.text(0.15, 0.05, 'QED', color=DIM, fontsize=7)

# Partition annotation
ax.text(0, -2.2,
        r'$\frac{\pi}{12} + \frac{13}{264} + \frac{251-22\pi}{264} = 1$',
        color=GOLD, fontsize=14, fontweight='bold', ha='center')

ax.set_title('The Universal Soliton: CMB = Vacuum, Expansion = Boundary',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys53_07_soliton_hierarchy.png')


# ================================================================
# FIG 8: IDENTITY CARD
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

ax.text(0.5, 0.96, 'THE GIGA REMAINDER TEST', color=GOLD, fontsize=22,
        fontweight='bold', ha='center')
ax.text(0.5, 0.93, 'PHYS-53: 11 Derivations, 140 Outputs, 7 Hierarchy Levels',
        color=SILVER, fontsize=12, ha='center')

# ── Left: TOP 5 RESULTS ──
ax.text(0.02, 0.87, 'TOP 5 BY PRECISION', color=CYAN, fontsize=13,
        fontweight='bold')

top5 = [
    (r'$\Sigma$ K = 1/3', '1.9 ppm', 'Hadron', CYAN),
    ('Lepton K = 2/3', '9.2 ppm', 'Lepton', GOLD),
    (r'$|V_{us}|$ = 9/40', '44 ppm', 'Particle', BLUE),
    (r'$\Omega_\Lambda$ = (251-22$\pi$)/264', '85 ppm', 'Cosmos', GOLD),
    (r'Bridge = 3$(M_Z/m_e)^2$', '300 ppm', 'QED-Cosmos', PURPLE),
]

for i, (name, miss, domain, color) in enumerate(top5):
    y = 0.82 - i * 0.04
    ax.text(0.04, y, name, color=color, fontsize=9, fontweight='bold')
    ax.text(0.38, y, miss, color=WHITE, fontsize=9)
    ax.text(0.46, y, domain, color=DIM, fontsize=8)

# ── Left: NEXT 7 ──
ax.text(0.02, 0.60, 'NEXT 7 (all sub-1%)', color=GREEN, fontsize=11,
        fontweight='bold')

next7 = [
    ('DM/baryon = 22pi/13', '725 ppm'),
    ('a_A/a_V = 3/2 (nuclear)', '0.21%'),
    ('|V_cb| = 1/24', '0.37%'),
    ('Omega_DM = pi/12', '0.42%'),
    ('Omega_b = 13/264', '0.49%'),
    ('H0 ratio = 12/11', '0.67%'),
    ('Chandrasekhar = 15pi/8', '0.93%'),
]

for i, (name, miss) in enumerate(next7):
    y = 0.55 - i * 0.033
    ax.text(0.04, y, name, color=SILVER, fontsize=8)
    ax.text(0.38, y, miss, color=DIM, fontsize=8)

# ── Left: FAILURES ──
ax.text(0.02, 0.30, '2 FAILURES', color=RED, fontsize=11, fontweight='bold')

fails = [
    ('|V_ub| = 1/264', '2.79%', 'Measurement uncertainty high'),
    ('|V_cb/V_ub| = 11', '3.07%', 'Driven by V_ub miss'),
]

for i, (name, miss, note) in enumerate(fails):
    y = 0.25 - i * 0.035
    ax.text(0.04, y, name, color=RED, fontsize=9)
    ax.text(0.25, y, miss, color=RED, fontsize=9)
    ax.text(0.35, y, note, color=DIM, fontsize=8)

# ── Right: KEY DISCOVERIES ──
ax.text(0.52, 0.87, 'KEY DISCOVERIES', color=GOLD, fontsize=13,
        fontweight='bold')

discoveries = [
    (r'$\Omega_\Lambda$ at 85 ppm from gauge integers 8,3,11,13', GOLD),
    (r'Cabibbo angle = $3^2/(8\times5)$ at 44 ppm', CYAN),
    ('Micro-cosmic bridge: Z mass connects QED to cosmos', PURPLE),
    ('Hubble tension = 12/11 (Yang-Mills scale separation)', ORANGE),
    ('Hadrons cluster at K=1/3: two-position Koide map', GREEN),
    (r'Nuclear $a_A/a_V$ = 3/2 = inverse Koide', GREEN),
    ('Chandrasekhar limit from 15pi/8', ORANGE),
    ('Muon toroidal = 40% of g-2 anomaly', BLUE),
]

for i, (text, color) in enumerate(discoveries):
    y = 0.82 - i * 0.038
    ax.text(0.54, y, text, color=color, fontsize=8)
    ax.plot(0.525, y + 0.005, '.', color=color, markersize=6)

# ── Right: THE BRIDGE FORMULA ──
ax.text(0.52, 0.48, 'THE BRIDGE FORMULA', color=PURPLE, fontsize=11,
        fontweight='bold')

ax.text(0.72, 0.42,
        r'$\frac{22\pi}{13} = |A_4| \cdot \left(\frac{\alpha}{\pi}\right)^4'
        r'\cdot 3 \cdot \left(\frac{M_Z}{m_e}\right)^2$',
        color=WHITE, fontsize=12, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                  edgecolor=PURPLE, linewidth=1.5))

ax.text(0.72, 0.35, '5 quantities, 3 domains, 300 ppm',
        color=SILVER, fontsize=9, ha='center')

# ── Bottom: SUMMARY ──
ax.text(0.5, 0.10,
        '8 PASS | 2 FAIL | 7 hierarchy levels | 4 sub-100-ppm matches\n'
        'Four independent predictions below 100 ppm across four scales.\n'
        'The inertial partition is not falsified.',
        color=WHITE, fontsize=10, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=GOLD, linewidth=2))

save(fig, 'phys53_08_identity_card.png')


# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys53_01_scoreboard.png")
print("  phys53_02_ckm_integers.png")
print("  phys53_03_cosmological_partition.png")
print("  phys53_04_koide_two_position.png")
print("  phys53_05_bridge.png")
print("  phys53_06_hubble_tension.png")
print("  phys53_07_soliton_hierarchy.png")
print("  phys53_08_identity_card.png")
print("=" * 50)
