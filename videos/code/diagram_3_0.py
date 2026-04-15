#!/usr/bin/env python3
"""
RUM Video 3 Diagrams — The Physics Stack (Batch 1: V1-V10)
Layers 0-4: Vacuum, Quantum Fields, Stable Patterns, Boundary Readings, Running.
10 figures. Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc, Wedge
import numpy as np
import os

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

print("Video 3 Diagrams — Batch 1 (V1-V10)")
print("=" * 50)


# ================================================================
# V1: THE STILL LAKE — THE VACUUM
# Type: Geometric Cross-Section
# Shows: The vacuum as a trembling surface — not empty, still.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

# Lake surface with trembling
x_surf = np.linspace(0.5, 17.5, 1000)
y_surf = 5.0 + 0.08 * np.sin(x_surf * 12) + 0.05 * np.sin(x_surf * 31) + 0.03 * np.sin(x_surf * 57)
ax.plot(x_surf, y_surf, color=CYAN, lw=2, alpha=0.8)
ax.fill_between(x_surf, 0.5, y_surf, color=CYAN, alpha=0.03)

# Virtual pair fluctuations below surface
np.random.seed(42)
for _ in range(80):
    fx = np.random.uniform(1, 17)
    fy = np.random.uniform(1.0, 4.5)
    angle = np.random.uniform(0, 360)
    dx = 0.15 * np.cos(np.radians(angle))
    dy = 0.15 * np.sin(np.radians(angle))
    ax.annotate('', xy=(fx + dx, fy + dy), xytext=(fx, fy),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=0.5, alpha=0.3))

# Labels
ax.text(9, 8.5, 'The Vacuum: Not Empty, Still',
        color=GOLD, fontsize=18, fontweight='bold', ha='center')

ax.text(9, 7.5, 'Everything else is a pattern in this.',
        color=SILVER, fontsize=12, ha='center', style='italic')

ax.text(14, 5.5, 'The ground state.\nLowest energy.\nNot zero energy.',
        color=CYAN, fontsize=10, ha='left',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, alpha=0.8))

ax.text(3, 2.5, 'Virtual pairs appearing\nand vanishing.\nThe lake trembles.',
        color=DIM, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, alpha=0.6))

ax.text(14, 2.0,
        'Energy density:\n' + r'$5.88 \times 10^{-30}$ g/cm$^3$',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(9, 0.8,
        'The vacuum is the largest soliton\'s ground state reading. '
        'Larger boundary = lower reading. That\'s why it\'s small.',
        color=GOLD, fontsize=10, ha='center', style='italic')

save(fig, 'talk3_01_still_lake.png')


# ================================================================
# V2: THE WORST PREDICTION IN PHYSICS
# Type: Scale/Landscape
# Shows: 120 orders of magnitude between measured and QFT prediction
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}$ (energy density, g/cm$^3$)', '')

# The scale
x_range = np.linspace(-35, 95, 1000)
ax.axhline(0.5, color=DIM, lw=2, alpha=0.2)

# Measured point
ax.plot(-30, 0.5, 'o', color=GOLD, markersize=18,
        linewidth=2, zorder=6)
ax.annotate('Measured:\n' + r'$5.88 \times 10^{-30}$ g/cm$^3$',
            xy=(-30, 0.5), xytext=(-30, 0.8),
            color=GOLD, fontsize=11, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# QFT prediction
ax.plot(90, 0.5, 'o', color=RED, markersize=18,
        linewidth=2, zorder=6)
ax.annotate('QFT prediction:\n' + r'$\sim 10^{90}$ g/cm$^3$',
            xy=(90, 0.5), xytext=(90, 0.8),
            color=RED, fontsize=11, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Gap
ax.fill_between([-30, 90], 0.4, 0.6, color=RED, alpha=0.06)
ax.annotate('', xy=(85, 0.3), xytext=(-25, 0.3),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=2))
ax.text(30, 0.2, r'120 orders of magnitude', color=WHITE,
        fontsize=14, fontweight='bold', ha='center')
ax.text(30, 0.1, 'The worst prediction in the history of science',
        color=RED, fontsize=11, ha='center', style='italic')

# RUM annotation
ax.text(-30, 0.15,
        'RUM: ground state reading\nof outermost boundary.\nNot a mismatch \u2014 a miscount.',
        color=GOLD, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(-40, 100)
ax.set_ylim(0, 1)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

ax.set_title(r'The Cosmological Constant: $10^{120}$ Wrong',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

save(fig, 'talk3_02_worst_prediction.png')


# ================================================================
# V3: THE 17 FIELDS — ORGANIZED BY THE GAUGE GROUP
# Type: Connection/Integer Map
# Shows: 17 field types sorted into three columns by SU(3), SU(2), U(1)
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(9, 11.5, '17 Field Types, Organized by Three Integers',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Column headers
cols = [
    (3, 'SU(3)', 'Color', '3 = three color charges', RED),
    (9, 'SU(2)', 'Weak', '2 = two weak isospin states', GREEN),
    (15, 'U(1)', 'Hypercharge', '1 = one hypercharge axis', BLUE),
]
for cx, name, subtitle, desc, color in cols:
    rect = FancyBboxPatch((cx - 2.3, 10.0), 4.6, 1.2,
                           boxstyle='round,pad=0.15',
                           facecolor=BG, linewidth=2)
    ax.add_patch(rect)
    ax.text(cx, 10.7, name, color=color, fontsize=14,
            fontweight='bold', ha='center')
    ax.text(cx, 10.3, desc, color=color, fontsize=8, ha='center')

# SU(3) column — quarks and gluons
quarks_su3 = ['u', 'd', 'c', 's', 't', 'b']
for i, q in enumerate(quarks_su3):
    y = 9.2 - i * 0.9
    ax.text(3, y, q, color=RED, fontsize=12, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))
ax.text(3, 3.2, '8 gluons', color=RED, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# SU(2) column — left-handed doublets and W/Z
doublets = [r'$(u,d)_L$', r'$(c,s)_L$', r'$(t,b)_L$',
            r'$(\nu_e,e)_L$', r'$(\nu_\mu,\mu)_L$', r'$(\nu_\tau,\tau)_L$']
for i, d in enumerate(doublets):
    y = 9.2 - i * 0.9
    ax.text(9, y, d, color=GREEN, fontsize=10, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))
ax.text(9, 3.2, r'$W^+, W^-, Z$', color=GREEN, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# U(1) column — right-handed singlets and photon
singlets = [r'$u_R$', r'$d_R$', r'$c_R$', r'$s_R$', r'$e_R$', r'$\mu_R$']
for i, s in enumerate(singlets):
    y = 9.2 - i * 0.9
    ax.text(15, y, s, color=BLUE, fontsize=10, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))
ax.text(15, 3.2, r'$\gamma$ (photon)', color=BLUE, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# Higgs spanning SU(2) and U(1)
rect_h = FancyBboxPatch((8, 1.5), 8, 1.0,
                          boxstyle='round,pad=0.15',
                          facecolor=BG, linewidth=2.5)
ax.add_patch(rect_h)
ax.text(12, 2.0, 'Higgs (spans SU(2) and U(1)). Ground state ' + r'$\neq 0$' +
        '. Provides inertia.',
        color=GOLD, fontsize=9, ha='center', fontweight='bold')

# Bottom annotation
ax.text(9, 0.5,
        '3, 2, 1. Three integers. Every fraction in the model traces to how '
        'these 17 fields transform under these three symmetries.',
        color=SILVER, fontsize=10, ha='center', style='italic')

save(fig, 'talk3_03_seventeen_fields.png')


# ================================================================
# V4: THE HIGGS — RESISTANCE, NOT SUBSTANCE
# Type: Geometric Cross-Section (two panels)
# Shows: Same force, different resistance — mass as resistance
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)

# Left panel: without Higgs
ax1.set_facecolor(PAN)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
for spine in ax1.spines.values():
    spine.set_color(CYAN)
    spine.set_linewidth(2)

ax1.set_title('Without Higgs Field', color=CYAN, fontsize=14,
              fontweight='bold', pad=10)

# Flat surface
ax1.plot([1, 9], [3, 3], color=DIM, lw=2)
# Ball moving fast
circle_fast = Circle((3, 4), 0.6, facecolor=CYAN, alpha=0.5,
                       linewidth=2)
ax1.add_patch(circle_fast)
# Force arrow
ax1.annotate('', xy=(5, 4), xytext=(3.8, 4),
             arrowprops=dict(arrowstyle='->', color=WHITE, lw=3))
ax1.text(4.4, 4.5, 'F', color=WHITE, fontsize=14, fontweight='bold')
# Speed arrows
for sx in [6, 7, 8]:
    ax1.annotate('', xy=(sx + 0.5, 4), xytext=(sx, 4),
                 arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, alpha=0.5))

ax1.text(5, 7, 'No resistance.\nNo inertia.\nMassless.\nTravels at c.',
         color=CYAN, fontsize=11, ha='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Right panel: with Higgs
ax2.set_facecolor(PAN)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
for spine in ax2.spines.values():
    spine.set_color(ORANGE)
    spine.set_linewidth(2)

ax2.set_title('With Higgs Field', color=ORANGE, fontsize=14,
              fontweight='bold', pad=10)

# Thick medium (dots)
np.random.seed(99)
for _ in range(200):
    dx = np.random.uniform(1, 9)
    dy = np.random.uniform(1, 6)
    ax2.plot(dx, dy, '.', color=ORANGE, markersize=3, alpha=0.3)

# Ball barely moving
circle_slow = Circle((3, 4), 0.6, facecolor=GOLD, alpha=0.7,
                       linewidth=2)
ax2.add_patch(circle_slow)
# Same force
ax2.annotate('', xy=(4.2, 4), xytext=(3.8, 4),
             arrowprops=dict(arrowstyle='->', color=WHITE, lw=3))
ax2.text(4.0, 4.5, 'F', color=WHITE, fontsize=14, fontweight='bold')

ax2.text(5, 7.5, 'Resistance from the field.\nInertia.\nm = F / a\nThe heavier the particle,\n'
         'the more the field resists.',
         color=ORANGE, fontsize=10, ha='center',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Bottom shared annotation
fig.text(0.5, 0.04,
         'Mass is not stuff. Mass is how hard the Higgs field pushes back '
         'when you try to accelerate something through it.',
         color=GOLD, fontsize=12, ha='center', style='italic')

save(fig, 'talk3_04_higgs_resistance.png')


# ================================================================
# V5: THE THREE SURVIVORS
# Type: Comparison Bar
# Shows: Particle lifetimes — 59 orders of magnitude from W to proton
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Lifetime ($\log_{10}$ seconds)', '')

particles = [
    (r'W boson', -25, RED, 'Dies instantly'),
    (r'Z boson', -25, RED, 'Dies instantly'),
    (r'Top quark', -25, RED, 'Dies instantly'),
    (r'Higgs', -22, ORANGE, 'Dies fast'),
    (r'Muon', -5.66, ORANGE, r'Lives 2.2 $\mu$s'),
    (r'Neutron (free)', 2.94, SILVER, 'Lives 15 min alone'),
    (r'Electron', 28, CYAN, 'Permanent'),
    (r'Proton', 34, GREEN, 'Permanent (probably)'),
    (r'Photon', 40, GOLD, r'Permanent ($\infty$)'),
]

y_positions = range(len(particles))
for i, (name, log_life, color, desc) in enumerate(particles):
    # Normalize bar width: 0 to 1 over the range -25 to 40
    bar_width = (log_life + 25) / 65.0 * 12
    ax.barh(i, max(bar_width, 0.1), height=0.7, color=color, alpha=0.6,
            linewidth=1.5, left=0.5)
    ax.text(0.3, i, name, color=WHITE, fontsize=10, fontweight='bold',
            ha='right', va='center')
    if log_life > 25:
        ax.text(13, i, desc, color=color, fontsize=9, ha='left', va='center')
    else:
        ax.text(max(bar_width, 0.1) + 0.8, i, desc, color=color,
                fontsize=9, ha='left', va='center')

# Scale labels at bottom
for val, label in [(-25, r'$10^{-25}$s'), (-6, r'$\mu$s'),
                    (0, '1 s'), (3, '15 min'), (28, r'$10^{28}$ yr'),
                    (34, r'$10^{34}$ yr')]:
    x_pos = (val + 25) / 65.0 * 12 + 0.5
    ax.text(x_pos, -0.8, label, color=DIM, fontsize=8, ha='center')
    ax.plot([x_pos, x_pos], [-0.4, -0.1], color=DIM, lw=0.5)

ax.set_xlim(-3, 15)
ax.set_ylim(-1.2, len(particles))
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.text(7.5, len(particles) + 0.3 - 0.4,
        'Stability is the exception. The survivors are the building blocks.',
        color=SILVER, fontsize=11, ha='center', style='italic')

ax.set_title('Most Particles Die. Three Survive Forever.',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

save(fig, 'talk3_05_three_survivors.png')


# ================================================================
# V6: THE PROTON — 99% CIRCULATION, 1% QUARKS
# Type: Geometric Cross-Section
# Shows: Toroidal circulation with three tiny quarks inside
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-6, 10)
ax.set_ylim(-5, 7)
ax.axis('off')

ax.text(2, 6.5, 'Inside the Proton: A Donut of Energy',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Outer boundary
boundary = Circle((0, 0), 4, facecolor=RED, alpha=0.06,
                   linewidth=2.5)
ax.add_patch(boundary)

# Toroidal flow arrows (circular paths)
for r, n_arrows in [(2.5, 12), (3.3, 16)]:
    angles = np.linspace(0, 2 * np.pi, n_arrows, endpoint=False)
    for a in angles:
        x1 = r * np.cos(a)
        y1 = r * np.sin(a)
        dx = -0.4 * np.sin(a)
        dy = 0.4 * np.cos(a)
        ax.annotate('', xy=(x1 + dx, y1 + dy), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.2, alpha=0.5))

# Three quarks
quark_data = [(-1.2, 1.0, 'u', CYAN, '2.16 MeV'),
              (1.2, 1.0, 'u', CYAN, '2.16 MeV'),
              (0, -1.2, 'd', GREEN, '4.70 MeV')]
for qx, qy, ql, qc, qm in quark_data:
    ax.plot(qx, qy, 'o', color=qc, markersize=16, 
            linewidth=2, zorder=6)
    ax.text(qx, qy - 0.5, '%s\n%s' % (ql, qm), color=qc, fontsize=8,
            ha='center', va='top')

# Size label
ax.annotate('', xy=(4, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='<->', color=DIM, lw=1))
ax.text(2, -0.4, '0.84 fm', color=DIM, fontsize=9, ha='center')

# Budget on right
budget_x = 6.5
ax.text(budget_x, 3, 'Inertia Budget:', color=WHITE, fontsize=13,
        fontweight='bold')
ax.text(budget_x, 2.2, 'Quarks: 9.02 MeV (1%)', color=CYAN, fontsize=11)

rect_conf = FancyBboxPatch((budget_x - 0.3, 0.3), 3.5, 1.2,
                             boxstyle='round,pad=0.15',
                             facecolor=BG, linewidth=2)
ax.add_patch(rect_conf)
ax.text(budget_x + 1.5, 0.9, 'Circulation:\n929.25 MeV (99%)',
        color=RED, fontsize=11, ha='center', fontweight='bold')

ax.text(budget_x, -0.5, 'Total: 938.27 MeV', color=GOLD, fontsize=12,
        fontweight='bold')

# Bottom
ax.text(2, -4.5,
        'The proton is a donut of energy that happens to contain three quarks.\n'
        'The quarks are passengers. The circulation is the proton.',
        color=GOLD, fontsize=11, ha='center', style='italic')

save(fig, 'talk3_06_proton_donut.png')


# ================================================================
# V7: INSIDE VS OUTSIDE — TWO READINGS, ONE BOUNDARY
# Type: Geometric Cross-Section (three panels)
# Shows: Reading flip at confinement, EW, and unification boundaries
# ================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 10),
                          gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)

panels = [
    ('Confinement', r'$\alpha_s \approx 1$', RED, r'$\alpha_s = 0.118$', CYAN,
     '1 fm', 'Strong force drops 10' + r'$\times$'),
    ('Electroweak', 'One EW force', GREEN, 'EM + Weak\n(two forces)', BLUE,
     r'$10^{-18}$ m', 'One force becomes two'),
    ('Unification', 'One force\nat 1/42', GOLD, 'Three forces\n1/137, 1/30, 0.118', WHITE,
     r'$10^{-32}$ m', 'One force becomes three'),
]

for ax, (title, inside_txt, inside_col, outside_txt, outside_col,
         size_txt, caption) in zip(axes, panels):
    ax.set_facecolor(PAN)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')

    # Boundary circle
    circ = Circle((0, 0), 3, facecolor=inside_col, alpha=0.08,
                   linewidth=2.5)
    ax.add_patch(circ)

    # Inside label
    ax.text(0, 0.5, 'INSIDE', color=inside_col, fontsize=10,
            fontweight='bold', ha='center')
    ax.text(0, -0.3, inside_txt, color=inside_col, fontsize=10, ha='center')

    # Outside labels (four corners)
    for ox, oy in [(-4, 4), (4, 4), (-4, -4), (4, -4)]:
        ax.text(ox, oy, outside_txt, color=outside_col, fontsize=7,
                ha='center', va='center', alpha=0.6)

    # Title and size
    ax.text(0, 4.5, title, color=GOLD, fontsize=13, fontweight='bold',
            ha='center')
    ax.text(0, -4.2, size_txt, color=DIM, fontsize=9, ha='center')
    ax.text(0, -4.7, caption, color=inside_col, fontsize=8, ha='center',
            style='italic')

fig.text(0.5, 0.02,
         'Every boundary: inside reads one thing, outside reads another. '
         'The reading change IS the boundary.',
         color=GOLD, fontsize=12, ha='center', style='italic')

save(fig, 'talk3_07_inside_outside.png')


# ================================================================
# V8: THREE BOUNDARIES ON ONE ENERGY AXIS
# Type: Scale/Landscape
# Shows: Confinement, EW, GUT on a log energy axis with regions
# ================================================================

fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(E / \mathrm{GeV})$', '')

# Scale line
ax.axhline(0.5, color=DIM, lw=2, alpha=0.2)

# Boundaries
boundaries = [
    (-0.7, 'Confinement', r'$\Lambda_{QCD} \approx 200$ MeV', RED),
    (2.4, 'Electroweak', r'$v = 246$ GeV', GREEN),
    (15.5, 'Unification', r'$M_{GUT} = 10^{15.5}$ GeV', GOLD),
]

for x, name, desc, color in boundaries:
    ax.axvline(x, color=color, lw=2.5, alpha=0.7)
    ax.plot(x, 0.5, 'o', color=color, markersize=14,
            linewidth=2, zorder=6)
    ax.text(x, 0.82, name, color=color, fontsize=12,
            fontweight='bold', ha='center')
    ax.text(x, 0.72, desc, color=color, fontsize=9, ha='center')

# Region labels
ax.fill_between([-2, -0.7], 0.35, 0.65, color=RED, alpha=0.05)
ax.text(-1.35, 0.3, 'Nuclear\nphysics', color=RED, fontsize=9,
        ha='center', style='italic', alpha=0.7)

ax.fill_between([-0.7, 2.4], 0.35, 0.65, color=CYAN, alpha=0.04)
ax.text(0.85, 0.3, 'Particle\nphysics', color=CYAN, fontsize=9,
        ha='center', style='italic', alpha=0.7)

ax.fill_between([2.4, 15.5], 0.35, 0.65, color=DIM, alpha=0.03)
ax.text(9, 0.3, 'The Desert\n(13 orders of magnitude of nothing)',
        color=DIM, fontsize=9, ha='center', style='italic')

# Reading changes
ax.text(-1.5, 0.15, r'quarks confined, $\alpha_s \to \infty$',
        color=RED, fontsize=8, ha='center')
ax.text(1.0, 0.15, r'W, Z massive', color=GREEN, fontsize=8, ha='center')
ax.text(13, 0.15, r'three forces', color=SILVER, fontsize=8, ha='center')

ax.set_xlim(-2.5, 17)
ax.set_ylim(0, 1)
ax.set_yticks([])
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

ax.set_title('Three Boundaries, Three Reading Changes',
             color=GOLD, fontsize=16, fontweight='bold', pad=12)

ax.text(7.5, 0.92,
        'Three walls. Cross each one and the physics changes. '
        'The walls are positioned by integer fractions.',
        color=SILVER, fontsize=10, ha='center', style='italic')

save(fig, 'talk3_08_three_boundaries.png')


# ================================================================
# V9: THREE FORCES, THREE RATES, THREE FRACTIONS
# Type: Running/Convergence
# Shows: Coupling unification — three curves meeting at one point
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(\mu / \mathrm{GeV})$',
         r'$\alpha_i^{-1}(\mu)$')

log_mu = np.linspace(np.log10(91.2), 16, 500)
log_mz = np.log10(91.2)
ln_ratio = (log_mu - log_mz) * np.log(10)

# CD-modified betas
b1 = 25.0 / 6.0
b2 = -13.0 / 6.0
b3 = -20.0 / 3.0

# Starting values at M_Z
a1_mz = 59.01
a2_mz = 29.57
a3_mz = 8.47

a1 = a1_mz - b1 * ln_ratio / (2 * np.pi)
a2 = a2_mz - b2 * ln_ratio / (2 * np.pi)
a3 = a3_mz - b3 * ln_ratio / (2 * np.pi)

ax.plot(log_mu, a1, color=BLUE, lw=2.5,
        label=r'$\alpha_1^{-1}$ (EM)  $b_1 = 25/6$, runs UP')
ax.plot(log_mu, a2, color=GREEN, lw=2.5,
        label=r'$\alpha_2^{-1}$ (weak)  $b_2 = -13/6$, runs DOWN')
ax.plot(log_mu, a3, color=RED, lw=2.5,
        label=r'$\alpha_3^{-1}$ (strong)  $b_3 = -20/3$, runs DOWN fastest')

# Crossing point
idx_cross = np.argmin(np.abs(a1 - a2))
ax.plot(log_mu[idx_cross], a1[idx_cross], '*', color=GOLD,
        markersize=22, zorder=6)
ax.annotate('Unification\nAll three read 1/42\n' + r'$M_{GUT} = 10^{15.5}$ GeV',
            xy=(log_mu[idx_cross], a1[idx_cross]),
            xytext=(log_mu[idx_cross] - 3, a1[idx_cross] + 10),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# M_Z marker
ax.axvline(log_mz, color=DIM, lw=1, ls=':', alpha=0.5)
ax.text(log_mz + 0.2, 62, r'$M_Z$', color=DIM, fontsize=10)

ax.set_xlim(1.5, 16.5)
ax.set_ylim(-5, 68)
ax.legend(facecolor=PAN, labelcolor=WHITE, fontsize=10,
          loc='upper right')

ax.set_title('Three Forces Converge: Same Destination, Different Speeds',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

ax.text(9, -3,
        'Three fractions (25/6, ' + r'$-$' + '13/6, ' + r'$-$' + '20/3) determine three speeds. '
        'The speeds determine where they meet. The meeting determines everything.',
        color=SILVER, fontsize=10, ha='center', style='italic')

save(fig, 'talk3_09_coupling_unification.png')


# ================================================================
# V10: WHAT THE 41 IN 41/10 COUNTS
# Type: Connection/Integer Map (tree)
# Shows: Decomposition of the integer 41 into particle contributions
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(9, 11.5, 'Where the Integer 41 Comes From',
        color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Top: b1 = 41/10
rect_top = FancyBboxPatch((6.5, 10.0), 5, 1.2,
                            boxstyle='round,pad=0.15',
                            facecolor=BG,  linewidth=2.5)
ax.add_patch(rect_top)
ax.text(9, 10.6, r'$b_1 = 41/10$', color=GOLD, fontsize=16,
        fontweight='bold', ha='center')

# Three branches
branches = [
    (3, 'Quarks (6 types)', RED, [
        (r'$Q_L$: 2Y$^2$ = 2(1/6)$^2$' + r' $\times$ 3c $\times$ 2', '2/3'),
        (r'$u_R$: 2Y$^2$ = 2(2/3)$^2$' + r' $\times$ 3c', '8/3'),
        (r'$d_R$: 2Y$^2$ = 2(1/3)$^2$' + r' $\times$ 3c', '2/3'),
    ]),
    (9, 'Leptons (6 types)', CYAN, [
        (r'$L_L$: 2Y$^2$ = 2(1/2)$^2$' + r' $\times$ 2', '1'),
        (r'$e_R$: 2Y$^2$ = 2(1)$^2$', '2'),
    ]),
    (15, 'Higgs (1 type)', GOLD, [
        (r'Y$^2$ = (1/2)$^2$', '1/4'),
    ]),
]

for bx, title, color, items in branches:
    # Branch line
    ax.plot([9, bx], [10.0, 8.5], color=color, lw=1.5)

    # Branch title
    ax.text(bx, 8.7, title, color=color, fontsize=11,
            fontweight='bold', ha='center')

    for i, (formula, value) in enumerate(items):
        y = 7.5 - i * 1.2
        rect = FancyBboxPatch((bx - 2.5, y - 0.4), 5, 0.8,
                               boxstyle='round,pad=0.1',
                               facecolor=BG, linewidth=1)
        ax.add_patch(rect)
        ax.text(bx - 2.3, y, formula, color=color, fontsize=8, va='center')
        ax.text(bx + 2.3, y, '= ' + value, color=WHITE, fontsize=9,
                va='center', ha='right', fontweight='bold')

# Per-generation sum
ax.text(3, 4.0, r'Per gen: $\frac{2}{3} + \frac{8}{3} + \frac{2}{3} + 1 + 2 = \frac{20}{3}$',
        color=SILVER, fontsize=9, ha='center')
ax.text(3, 3.4, r'$\times$ 3 generations = 20', color=SILVER, fontsize=9, ha='center')

# Higgs
ax.text(15, 5.5, r'Higgs: $\frac{1}{4} \times 4 = 1$',
        color=GOLD, fontsize=9, ha='center')

# Total
rect_total = FancyBboxPatch((5, 1.5), 8, 1.2,
                              boxstyle='round,pad=0.15',
                              facecolor=BG, linewidth=2)
ax.add_patch(rect_total)
ax.text(9, 2.1,
        'Numerator: 20 + 20 + 1 = 41.   Denominator: 10 (from 3/5 GUT normalization).\n'
        r'$b_1 = 41/10$. Change one particle, change 41. Add the CD: 41 $\to$ 43, and 41/10 $\to$ 25/6.',
        color=WHITE, fontsize=9, ha='center')

# Bottom
ax.text(9, 0.5,
        '41 is not arbitrary. It counts every particle\'s electromagnetic charge contribution.',
        color=GOLD, fontsize=11, ha='center', style='italic')

save(fig, 'talk3_10_what_41_counts.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("Batch 1 complete — 10 figures saved:")
print("  talk3_01_still_lake.png")
print("  talk3_02_worst_prediction.png")
print("  talk3_03_seventeen_fields.png")
print("  talk3_04_higgs_resistance.png")
print("  talk3_05_three_survivors.png")
print("  talk3_06_proton_donut.png")
print("  talk3_07_inside_outside.png")
print("  talk3_08_three_boundaries.png")
print("  talk3_09_coupling_unification.png")
print("  talk3_10_what_41_counts.png")
print("=" * 50)
