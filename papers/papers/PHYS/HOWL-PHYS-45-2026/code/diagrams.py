#!/usr/bin/env python3
"""
HOWL PHYS-45 Diagrams — The Confinement Boundary
8 figures covering alpha_s running, proton inertia, boundary hierarchy,
CD propagation, boundary thickness, pion at boundary, SM vs CD Lambda,
and soliton boundary identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================

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
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
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

print("PHYS-45 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: ALPHA_S RUNNING FROM M_Z TO LAMBDA_QCD
# Type: Running/Convergence (D5.1)
# Shows: alpha_s growing as energy decreases, with step changes
#        in slope at each flavor threshold. The coupling diverges
#        at Lambda_QCD.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Energy $\mu$ (MeV)', r'$\alpha_s(\mu)$')

# Thresholds and b3 values
M_Z = 91187.6
m_t = 172570.0
m_b = 4183.0
m_c = 1273.0
lam_sm = 142.5

# b3 at each range (nf=5,4,3)
b3_nf5 = -23.0/3.0
b3_nf4 = -25.0/3.0
b3_nf3 = -9.0

alpha_inv_mz = 1.0/0.118
two_pi = 2.0 * np.pi

def run_segment(mu_start, mu_end, alpha_inv_start, b3, n=200):
    mus = np.logspace(np.log10(mu_end), np.log10(mu_start), n)
    alpha_inv = alpha_inv_start - b3/two_pi * np.log(mus/mu_start)
    alpha_inv = np.maximum(alpha_inv, 0.01)
    alpha_s = 1.0 / alpha_inv
    return mus, alpha_s, alpha_inv[-1]

# Segment 1: M_Z down to m_b (nf=5)
mus1, as1, ainv_mb = run_segment(M_Z, m_b, alpha_inv_mz, b3_nf5, 300)
ax.plot(mus1, as1, color=CYAN, lw=2.5, label=r'$n_f=5$, $b_3=-23/3$')

# Segment 2: m_b down to m_c (nf=4)
mus2, as2, ainv_mc = run_segment(m_b, m_c, ainv_mb, b3_nf4, 300)
ax.plot(mus2, as2, color=GREEN, lw=2.5, label=r'$n_f=4$, $b_3=-25/3$')

# Segment 3: m_c down to Lambda (nf=3)
mus3, as3, _ = run_segment(m_c, lam_sm + 5, ainv_mc, b3_nf3, 500)
ax.plot(mus3, as3, color=RED, lw=2.5, label=r'$n_f=3$, $b_3=-9$')

# Threshold markers
for mu_val, label, col in [(m_b, r'$m_b = 4.18$ GeV', GREEN),
                             (m_c, r'$m_c = 1.27$ GeV', ORANGE),
                             (lam_sm, r'$\Lambda_{QCD} = 142.5$ MeV', RED)]:
    ax.axvline(mu_val, color=col, lw=1.5, ls='--', alpha=0.5)
    ax.text(mu_val * 1.15, 0.85, label, color=col, fontsize=9, rotation=90,
            va='bottom')

# M_Z marker
ax.axvline(M_Z, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.text(M_Z * 0.85, 0.15, r'$M_Z = 91.2$ GeV', color=GOLD, fontsize=9,
        ha='right')
ax.plot(M_Z, 0.118, '*', color=GOLD, markersize=18, zorder=6)
ax.text(M_Z * 0.7, 0.135, r'$\alpha_s = 0.118$', color=GOLD, fontsize=10)

# Confinement region
ax.axvspan(100, lam_sm + 20, color=RED, alpha=0.05)
ax.text(120, 0.6, 'CONFINEMENT', color=RED, fontsize=12,
        fontweight='bold', alpha=0.4, rotation=90)

ax.set_xscale('log')
ax.set_xlim(120, 200000)
ax.set_ylim(0, 1.0)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper right')

ax.set_title(r'$\alpha_s$ Running from $M_Z$ to $\Lambda_{QCD}$: Three Flavor Thresholds',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys45_01_alpha_s_running.png')


# ================================================================
# FIG 2: PROTON INERTIA BUDGET — 99% BOUNDARY, 1% QUARKS
# Type: Comparison Bar (D5.6)
# Shows: Two bars — valence quarks (9 MeV) vs confinement energy
#        (929 MeV). The confinement bar dominates completely.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Inertia (MeV)')

components = ['Valence quarks\n(u + u + d)', 'Confinement\nenergy']
values = [9.02, 929.25]
colors_bars = [CYAN, RED]

bars = ax.bar(range(2), values, color=colors_bars, alpha=0.7,
              edgecolor=colors_bars, linewidth=2, width=0.55)

# Value labels
ax.text(0, 9.02 + 25, '9.02 MeV\n(0.96%)', color=CYAN, fontsize=14,
        fontweight='bold', ha='center')
ax.text(1, 929.25 + 25, '929.25 MeV\n(99.04%)', color=RED, fontsize=14,
        fontweight='bold', ha='center')

# Total
ax.axhline(938.27, color=GOLD, lw=2, ls='--', alpha=0.6)
ax.text(1.4, 945, r'Total: $m_p = 938.27$ MeV', color=GOLD, fontsize=12,
        fontweight='bold')

# Quark breakdown inside the small bar
ax.text(0, 4.5, r'$2m_u + m_d$', color=BG, fontsize=8, ha='center',
        fontweight='bold')

# Confinement breakdown
ax.text(1, 750, 'Gluon fields\nSea quarks\nKinetic energy', color=BG,
        fontsize=10, ha='center', fontweight='bold', alpha=0.7)

ax.set_xticks(range(2))
ax.set_xticklabels(components, color=WHITE, fontsize=12)
ax.set_ylim(0, 1050)

ax.text(0.5, 1000, 'The proton is 99% boundary',
        color=GOLD, fontsize=16, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

ax.set_title('Proton Inertia Budget: Quarks vs Confinement',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys45_02_proton_inertia.png')


# ================================================================
# FIG 3: BOUNDARY HIERARCHY — LOG ENERGY SCALE
# Type: Scale/Landscape (D5.2)
# Shows: All soliton boundaries from molecular to Planck on a log
#        energy axis, with governing couplings labeled.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(E / \mathrm{MeV})$', '')

boundaries = [
    (-6.0, 'Molecular', r'$\alpha_{em}$, ~eV', SILVER),
    (-4.9, 'Atomic', r'$\alpha_{em}$, 13.6 eV', BLUE),
    (0.9, 'Nuclear', r'Residual strong, ~8 MeV', GREEN),
    (2.15, 'Confinement', r'$\alpha_s \to \infty$, 142.5 MeV', RED),
    (3.1, 'Charm threshold', r'$n_f: 4 \to 3$, 1.27 GeV', DIM),
    (3.6, 'Bottom threshold', r'$n_f: 5 \to 4$, 4.18 GeV', DIM),
    (5.2, 'Top threshold', r'$n_f: 6 \to 5$, 173 GeV', DIM),
    (5.4, 'Electroweak', r'$\alpha_2$, $v = 246$ GeV', CYAN),
    (6.5, 'CD threshold', r'$M_{CD} > 1.5$ TeV', MAG),
    (15.5, 'GUT', r'$\alpha_{GUT}$, $10^{15.5}$ GeV', ORANGE),
    (22.1, 'Planck', r'All couplings, $10^{19}$ GeV', GOLD),
]

ax.axhline(0.5, color=DIM, lw=2, alpha=0.2)

for x, name, desc, color in boundaries:
    ax.plot(x, 0.5, 'o', color=color, markersize=14,
            linewidth=1.8, zorder=5)
    idx = boundaries.index((x, name, desc, color))
    if idx % 2 == 0:
        ax.annotate('%s\n%s' % (name, desc), xy=(x, 0.5),
                    xytext=(x, 0.78),
                    color=color, fontsize=8, fontweight='bold',
                    ha='center', va='bottom',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))
    else:
        ax.annotate('%s\n%s' % (name, desc), xy=(x, 0.5),
                    xytext=(x, 0.22),
                    color=color, fontsize=8, fontweight='bold',
                    ha='center', va='top',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))

# Regime shading
ax.axvspan(-7, 1.5, color=BLUE, alpha=0.03)
ax.axvspan(1.5, 4.0, color=RED, alpha=0.03)
ax.axvspan(4.0, 7.0, color=CYAN, alpha=0.03)
ax.axvspan(7.0, 16, color=ORANGE, alpha=0.03)
ax.axvspan(16, 23, color=GOLD, alpha=0.03)

ax.text(-3, 0.92, 'EM bound\nstates', color=BLUE, fontsize=9,
        ha='center', style='italic', alpha=0.6)
ax.text(2.5, 0.08, 'QCD\nconfinement', color=RED, fontsize=9,
        ha='center', style='italic', alpha=0.6)
ax.text(5.5, 0.92, 'Electroweak', color=CYAN, fontsize=9,
        ha='center', style='italic', alpha=0.6)
ax.text(11, 0.08, 'Desert', color=ORANGE, fontsize=9,
        ha='center', style='italic', alpha=0.6)
ax.text(19, 0.92, 'Quantum\ngravity', color=GOLD, fontsize=9,
        ha='center', style='italic', alpha=0.6)

ax.set_xlim(-7.5, 23.5)
ax.set_ylim(0, 1)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

ax.set_title('The Soliton Boundary Hierarchy: 29 Orders of Magnitude',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys45_03_boundary_hierarchy.png')


# ================================================================
# FIG 4: CD PROPAGATION CHAIN — 1/3 THROUGH 5 DECADES
# Type: Progression/Sequence (D5.7)
# Shows: The exact Fraction 1/3 entering at TeV scale and propagating
#        through threshold after threshold to a 2% shift at confinement.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

def draw_box(ax, x, y, w, h, text, color, fontsize=9):
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, color=color, fontsize=fontsize,
            ha='center', va='center', linespacing=1.4)

def draw_arrow_h(ax, x1, y1, x2, y2, color, label=''):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        ax.text(mx, my + 0.35, label, color=color, fontsize=8,
                ha='center', va='bottom')

# Step 0: CD representation
draw_box(ax, 0.2, 7.5, 3.0, 1.8,
         'Cabibbo Doublet\n(3, 2, 1/6)\nVector-like', GOLD, 10)

# Step 1: Delta b3
draw_box(ax, 4.5, 7.5, 2.5, 1.8,
         r'$\Delta b_3 = +1/3$' + '\nExact Fraction', MAG, 10)
draw_arrow_h(ax, 3.2, 8.4, 4.5, 8.4, GOLD, 'group theory')

# Step 2: alpha_s shift at M_Z
draw_box(ax, 8.2, 7.5, 3.0, 1.8,
         r'$\alpha_s(M_Z)$' + '\n0.1180 ' + r'$\to$' + ' 0.1184\n+0.34%', CYAN, 10)
draw_arrow_h(ax, 7.0, 8.4, 8.2, 8.4, MAG, 'crossing')

# Step 3: Propagation through thresholds
draw_box(ax, 12.5, 7.5, 3.0, 1.8,
         'Through 3 thresholds\n' + r'$m_t, m_b, m_c$' + '\n5 decades', GREEN, 10)
draw_arrow_h(ax, 11.2, 8.4, 12.5, 8.4, CYAN, 'running')

# Step 4: Lambda shift
draw_box(ax, 5.0, 3.5, 3.5, 2.0,
         r'$\Lambda_{QCD}$' + '\n142.5 ' + r'$\to$' + ' 145.4 MeV\n+2.0%', RED, 11)
draw_arrow_h(ax, 14.0, 7.5, 6.75, 5.5, GREEN, 'amplification 6'+r'$\times$')

# Step 5: Proton mass
draw_box(ax, 10.0, 3.5, 3.5, 2.0,
         r'$m_p = C \times \Lambda$' + '\n670 ' + r'$\to$' + ' 684 MeV\n+2.0%', ORANGE, 11)
draw_arrow_h(ax, 8.5, 4.5, 10.0, 4.5, RED, r'$C = 4.7$')

# Step 6: Everything downstream
draw_box(ax, 10.0, 0.8, 3.5, 2.0,
         r'$m_\pi, r_{nuclear}, E_{bind}$' + '\n+3%, +3%, +6%\nAll from 1/3', PURPLE, 10)
draw_arrow_h(ax, 11.75, 3.5, 11.75, 2.8, ORANGE, 'ChPT')

# Title
ax.text(9, 9.7, 'CD Propagation: One Fraction Through Five Decades',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

# Annotation
ax.text(2.5, 1.5,
        'Input: 1/3\n(exact, from group theory)\n\nOutput: 2% shift in\nall hadron masses',
        color=GOLD, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

save(fig, 'phys45_04_cd_propagation.png')


# ================================================================
# FIG 5: BOUNDARY THICKNESS — SM vs CD FOR 3 GAUGE SECTORS
# Type: Comparison Bar (D5.6)
# Shows: Paired bars for each sector. SU(2) change is dramatic.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'Boundary thickness $1/|b|$')

sectors = ['SU(3)\nConfinement', 'SU(2)\nWeak', 'U(1)\nEM']
sm_vals = [1.0/7.0, 6.0/19.0, 10.0/41.0]
cd_vals = [3.0/20.0, 6.0/13.0, 6.0/25.0]
sm_fracs = ['1/7', '6/19', '10/41']
cd_fracs = ['3/20', '6/13', '6/25']
changes = ['+5.0%', '+46.2%', r'$-$1.6%']
change_colors = [GREEN, RED, CYAN]

x = np.array([0, 1.5, 3.0])
w = 0.35

bars_sm = ax.bar(x - w/2 - 0.02, sm_vals, width=w, color=CYAN, alpha=0.7,
                  edgecolor=CYAN, linewidth=1.5, label='SM')
bars_cd = ax.bar(x + w/2 + 0.02, cd_vals, width=w, color=GOLD, alpha=0.7,
                  edgecolor=GOLD, linewidth=1.5, label='CD')

# Labels on bars
for i in range(3):
    ax.text(x[i] - w/2 - 0.02, sm_vals[i] + 0.01, sm_fracs[i],
            color=CYAN, fontsize=11, ha='center', fontweight='bold')
    ax.text(x[i] + w/2 + 0.02, cd_vals[i] + 0.01, cd_fracs[i],
            color=GOLD, fontsize=11, ha='center', fontweight='bold')
    ax.text(x[i], max(sm_vals[i], cd_vals[i]) + 0.04, changes[i],
            color=change_colors[i], fontsize=12, ha='center', fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(sectors, color=WHITE, fontsize=12)
ax.set_ylim(0, 0.6)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=11,
          loc='upper left')

ax.text(1.5, 0.55, 'The CD makes SU(2) 46% thicker, SU(3) 5% thicker, U(1) barely thinner',
        color=SILVER, fontsize=10, ha='center', style='italic')

ax.set_title('Soliton Boundary Thickness: SM vs CD',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys45_05_boundary_thickness.png')


# ================================================================
# FIG 6: PION AT THE BOUNDARY — CONFINEMENT TRANSITION ZONE
# Type: Geometric Cross-Section (D5.4)
# Shows: The confinement boundary as a transition zone. Proton fully
#        inside. Free quarks fully outside. Pion ON the boundary.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Confinement region (left = confined, right = free)
# Gradient from red to blue
for i in range(100):
    x_start = 2 + i * 0.12
    alpha_val = 0.15 * (1 - i/100.0)
    ax.axvspan(x_start, x_start + 0.12, color=RED, alpha=alpha_val)

# Boundary zone
ax.axvspan(6.5, 9.5, color=ORANGE, alpha=0.08)
ax.text(8.0, 9.2, 'BOUNDARY ZONE', color=ORANGE, fontsize=14,
        fontweight='bold', ha='center')
ax.text(8.0, 8.7, r'Thickness = $1/|b_3| = 1/7$', color=ORANGE,
        fontsize=10, ha='center')

# Labels
ax.text(3.5, 9.2, 'CONFINED', color=RED, fontsize=16,
        fontweight='bold', ha='center')
ax.text(3.5, 8.7, r'$\alpha_s > 1$', color=RED, fontsize=11, ha='center')
ax.text(12.5, 9.2, 'FREE', color=CYAN, fontsize=16,
        fontweight='bold', ha='center')
ax.text(12.5, 8.7, r'$\alpha_s < 1$', color=CYAN, fontsize=11, ha='center')

# Proton (fully inside)
circle_p = Circle((3.5, 5), 1.8, facecolor=RED, alpha=0.2,
                   edgecolor=RED, linewidth=2.5)
ax.add_patch(circle_p)
ax.text(3.5, 5, 'PROTON\n938 MeV\n(99% boundary)', color=WHITE,
        fontsize=10, ha='center', va='center', fontweight='bold')

# Three quarks inside proton
for qx, qy, ql in [(2.8, 5.8, 'u'), (4.2, 5.8, 'u'), (3.5, 4.2, 'd')]:
    ax.plot(qx, qy, 'o', color=CYAN, markersize=10,
            linewidth=1.5, zorder=5)
    ax.text(qx, qy - 0.35, ql, color=CYAN, fontsize=9, ha='center')

# Pion (ON the boundary)
circle_pi = Circle((8.0, 5), 1.2, facecolor=ORANGE, alpha=0.2,
                    edgecolor=ORANGE, linewidth=2.5, linestyle='--')
ax.add_patch(circle_pi)
ax.text(8.0, 5, 'PION\n140 MeV\n(boundary mode)', color=WHITE,
        fontsize=10, ha='center', va='center', fontweight='bold')

# Quark-antiquark in pion
ax.plot(7.5, 5.3, 'o', color=CYAN, markersize=8, linewidth=1.5)
ax.plot(8.5, 5.3, 'o', color=MAG, markersize=8,  linewidth=1.5)
ax.text(7.5, 4.7, 'q', color=CYAN, fontsize=8, ha='center')
ax.text(8.5, 4.7, r'$\bar{q}$', color=MAG, fontsize=8, ha='center')

# Free quarks (outside)
for qx, qy in [(11.5, 6), (12.5, 4.5), (13.5, 5.5), (12, 3.5)]:
    ax.plot(qx, qy, 'o', color=CYAN, markersize=8, 
            linewidth=1.5, zorder=5)
ax.text(12.5, 2.5, 'Free quarks\nand gluons', color=CYAN, fontsize=10,
        ha='center', style='italic')

# Energy scale
ax.annotate('', xy=(2, 1.2), xytext=(14, 1.2),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.5))
ax.text(8, 0.7, r'Energy scale $\mu$  (low $\leftarrow$ $\rightarrow$ high)',
        color=DIM, fontsize=10, ha='center')
ax.text(2, 0.7, r'$\mu < \Lambda_{QCD}$', color=RED, fontsize=9, ha='center')
ax.text(14, 0.7, r'$\mu > \Lambda_{QCD}$', color=CYAN, fontsize=9, ha='center')

ax.set_title('The Pion Lives ON the Confinement Boundary',
             color=GOLD, fontsize=15, fontweight='bold', pad=10)

save(fig, 'phys45_06_pion_boundary.png')


# ================================================================
# FIG 7: SM vs CD LAMBDA_QCD — TWO CURVES APPROACHING DIVERGENCE
# Type: Threshold/Region (D5.3)
# Shows: alpha_s^-1 approaching zero for both SM and CD theories.
#        The 2% gap between divergence points is visible.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Energy $\mu$ (MeV)', r'$\alpha_s^{-1}(\mu)$')

# Run both SM and CD from m_c downward with nf=3
mu_range = np.logspace(np.log10(130), np.log10(1300), 500)
b3_3 = -9.0

# SM
ainv_mc_sm = 3.136
ainv_sm = ainv_mc_sm - b3_3/two_pi * np.log(mu_range/m_c)

# CD (slightly different starting point)
ainv_mc_cd = 3.112  # from CD alpha_s = 0.3213 at m_c
ainv_cd = ainv_mc_cd - b3_3/two_pi * np.log(mu_range/m_c)

ax.plot(mu_range, ainv_sm, color=CYAN, lw=2.5, label=r'SM: $\Lambda = 142.5$ MeV')
ax.plot(mu_range, ainv_cd, color=GOLD, lw=2.5, label=r'CD: $\Lambda = 145.4$ MeV')

# Zero line
ax.axhline(0, color=RED, lw=1.5, ls='--', alpha=0.6)
ax.text(135, 0.15, r'$\alpha_s^{-1} = 0$ (confinement)', color=RED, fontsize=10)

# Lambda markers
ax.axvline(142.5, color=CYAN, lw=1.5, ls=':', alpha=0.6)
ax.axvline(145.4, color=GOLD, lw=1.5, ls=':', alpha=0.6)

# Gap annotation
ax.annotate('', xy=(145.4, -0.3), xytext=(142.5, -0.3),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=1.5))
ax.text(144, -0.55, '+2.0%', color=WHITE, fontsize=11, fontweight='bold',
        ha='center')

# Shaded confinement region
ax.axvspan(130, 146, color=RED, alpha=0.05)

ax.set_xscale('log')
ax.set_xlim(130, 1300)
ax.set_ylim(-0.8, 3.5)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=11,
          loc='upper right')

ax.set_title(r'SM vs CD: The 2% Gap at Confinement',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys45_07_sm_cd_lambda.png')


# ================================================================
# FIG 8: SOLITON BOUNDARY IDENTITY CARD
# Type: Identity Card (D5.8)
# Shows: The four components of a soliton boundary as a visual
#        reference card with the confinement boundary as example.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(8, 11.3, 'SOLITON BOUNDARY', color=GOLD, fontsize=20,
        fontweight='bold', ha='center')
ax.text(8, 10.7, 'Four Components — Confinement as Prototype',
        color=SILVER, fontsize=12, ha='center')

# Four quadrants
def card_box(ax, x, y, w, h, title, content, color, num):
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.2',
                           facecolor=BG, edgecolor=color, linewidth=2.5)
    ax.add_patch(rect)
    ax.text(x + 0.3, y + h - 0.4, '%d. %s' % (num, title), color=color,
            fontsize=13, fontweight='bold', va='top')
    ax.text(x + w/2, y + h/2 - 0.3, content, color=WHITE, fontsize=10,
            ha='center', va='center', linespacing=1.5)

# Component 1: Coupling
card_box(ax, 0.5, 5.8, 7, 4.2,
         'THE COUPLING', r'$\alpha_s$ (strong coupling)' + '\n\n' +
         'Small at high energy (free quarks)\n' +
         'Large at low energy (confinement)\n' +
         r'At $M_Z$: $\alpha_s = 0.118$',
         RED, 1)

# Component 2: Beta coefficient
card_box(ax, 8.5, 5.8, 7, 4.2,
         'THE BETA COEFFICIENT',
         r'$b_3 = -11 + \frac{2}{3} n_f$' + '\n\n' +
         'SM: ' + r'$b_3 = -7$' + '   (exact Fraction)\n' +
         'CD: ' + r'$b_3 = -20/3$' + '   (exact Fraction)\n' +
         'Shift: ' + r'$\Delta b_3 = +1/3$',
         MAG, 2)

# Component 3: Threshold
card_box(ax, 0.5, 0.8, 7, 4.2,
         'THE THRESHOLD',
         r'$\Lambda_{QCD}$: where $\alpha_s \to \infty$' + '\n\n' +
         'SM: 142.5 MeV (one-loop)\n' +
         'CD: 145.4 MeV (+2.0%)\n' +
         'Two-loop: ~210 MeV (estimated)',
         ORANGE, 3)

# Component 4: Soliton
card_box(ax, 8.5, 0.8, 7, 4.2,
         'THE SOLITON',
         'Proton: 938.3 MeV (99% boundary)\n' +
         'Neutron: 939.6 MeV (99% boundary)\n' +
         'Pion: 139.6 MeV (boundary mode)\n\n' +
         r'Thickness: SM = $1/7$, CD = $3/20$',
         GREEN, 4)

# Central connection arrows
ax.annotate('', xy=(8.2, 7.9), xytext=(7.7, 7.9),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))
ax.annotate('', xy=(4, 5.6), xytext=(4, 5.1),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))
ax.annotate('', xy=(12, 5.6), xytext=(12, 5.1),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Central label
ax.text(8, 5.35, 'determines', color=DIM, fontsize=9, ha='center')

save(fig, 'phys45_08_boundary_identity.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys45_01_alpha_s_running.png")
print("  phys45_02_proton_inertia.png")
print("  phys45_03_boundary_hierarchy.png")
print("  phys45_04_cd_propagation.png")
print("  phys45_05_boundary_thickness.png")
print("  phys45_06_pion_boundary.png")
print("  phys45_07_sm_cd_lambda.png")
print("  phys45_08_boundary_identity.png")
print("=" * 50)
