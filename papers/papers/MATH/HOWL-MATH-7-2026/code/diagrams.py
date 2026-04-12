#!/usr/bin/env python3
"""
HOWL MATH-7 Diagrams — The alpha-Power Scaling Law
8 figures covering derived constant tree, scaling line, geographic independence,
diagnostic scenarios, m_e threshold, extraction pipeline, Rb cross-check, identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global palette (D7.2) ──
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


def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
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

# ── Physics data from DATA-6 pool ──
delta_alpha = 0.219      # ppb, base miss vs CODATA
delta_me = 0.03          # ppb, m_e uncertainty
alpha_inv_ours = 137.035999207
alpha_inv_rb = 137.035999206
alpha_inv_codata = 137.035999084
miss_rb = 0.007          # ppb
miss_codata = 0.219      # ppb

# Verified values
verified = [
    (r'$\alpha^{-1}$ vs CODATA', 1, 0.219, GOLD, 'BASE'),
    (r'$a_0$ (Bohr radius)', 1, 0.219, CYAN, 'Verified'),
    (r'$\mu_0$ (vac. perm.)', 1, 0.219, GREEN, 'Verified'),
    (r'$R_\infty$ (Rydberg)', 2, 0.437, ORANGE, 'Verified'),
    ('f(1S-2S) (hydrogen)', 2, 0.443, BLUE, 'Verified'),
]

# Predicted values
predicted = [
    (r'$r_e$ (class. e radius)', 1, 0.222, MAG),
    (r'$E_h$ (Hartree)', 2, 0.441, PURPLE),
    (r'$\sigma_0$ (Bohr x-sec)', 2, 0.444, RED),
    (r'$\sigma_T$ (Thomson)', 2, 0.446, ORANGE),  # pending formula resolution
]

# Seven corrections in extraction pipeline
corrections = [
    ('Hadronic VP\n(2-loop)', 1.718, PURPLE),
    ('Hadronic VP\n(3-loop)', 0.081, PURPLE),
    ('Hadronic LbL', 0.536, MAG),
    ('Electroweak\n(2-loop)', 0.030, BLUE),
    ('Mass-dep\n(2-loop)', 1.096, CYAN),
    ('Mass-dep\n(3-loop)', 0.276, GREEN),
    ('Mass-dep\n(4-loop)', 0.034, DIM),
]


# ================================================================
# FIG 1: DERIVED CONSTANT TREE
# Type: Type 5 (Connection/Integer Map)
# Shows: One root (alpha) branching to nine constants via integer powers
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

# Title
ax.text(9, 13.5, r'The Derived Constant Tree: One Measurement $\rightarrow$ One Parameter $\rightarrow$ Nine Constants',
        color=GOLD, fontsize=15, fontweight='bold', ha='center')

# Root: a_e measurement
ax.text(9, 12.3, r'$a_e$ = 0.00115965218059', color=MAG, fontsize=10, ha='center')
ax.text(9, 11.8, '(Fan et al., Harvard, 2023)', color=DIM, fontsize=8, ha='center')
root_box = FancyBboxPatch((6.5, 11.4), 5, 1.2, boxstyle='round,pad=0.2',
                          facecolor=PAN, edgecolor=MAG, linewidth=2)
ax.add_patch(root_box)

# Arrow to alpha
ax.annotate('', xy=(9, 10.3), xytext=(9, 11.4),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(9.5, 10.8, '5-loop QED\n+ 7 corrections', color=SILVER, fontsize=7, ha='left')

# Alpha node
alpha_box = FancyBboxPatch((6.8, 9.4), 4.4, 0.9, boxstyle='round,pad=0.2',
                           facecolor=PAN, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(alpha_box)
ax.text(9, 9.9, r'$\alpha^{-1}$ = 137.035999207', color=GOLD, fontsize=12,
        fontweight='bold', ha='center')

# n=1 branch (left)
n1_constants = [
    (3.0, 7.0, r'$a_0$', '0.219 ppb', CYAN, True),
    (6.0, 7.0, r'$\mu_0$', '0.219 ppb', GREEN, True),
    (9.0, 7.0, r'$r_e$', '0.222 ppb*', MAG, False),
]

# n=2 branch (right-center)
n2_constants = [
    (12.0, 7.0, r'$R_\infty$', '0.437 ppb', ORANGE, True),
    (15.0, 7.0, r'$E_h$', '0.441 ppb*', PURPLE, False),
]

# n=2 via R_infty
n2_via = [
    (12.0, 4.5, 'f(1S-2S)', '0.443 ppb', BLUE, True),
    (15.0, 4.5, r'$\sigma_0$', '0.444 ppb*', RED, False),
]

# n=2 via r_e -> sigma_T
sigma_t = (9.0, 4.5, r'$\sigma_T$', '0.446 ppb*', ORANGE, False)

# Draw n=1 branches
for x, y, label, miss, col, is_verified in n1_constants:
    ax.annotate('', xy=(x, y + 0.9), xytext=(9, 9.4),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8, alpha=0.7))
    ls = '-' if is_verified else '--'
    box = FancyBboxPatch((x - 1.2, y), 2.4, 0.8, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.5, linestyle=ls)
    ax.add_patch(box)
    ax.text(x, y + 0.5, label, color=col, fontsize=11, fontweight='bold', ha='center')
    ax.text(x, y + 0.15, miss, color=SILVER, fontsize=8, ha='center')

# Power label for n=1
ax.text(4.5, 8.5, 'n = 1', color=WHITE, fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=WHITE, alpha=0.5))

# Draw n=2 branches from alpha
for x, y, label, miss, col, is_verified in n2_constants:
    ax.annotate('', xy=(x, y + 0.9), xytext=(9, 9.4),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8, alpha=0.7))
    ls = '-' if is_verified else '--'
    box = FancyBboxPatch((x - 1.2, y), 2.4, 0.8, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.5, linestyle=ls)
    ax.add_patch(box)
    ax.text(x, y + 0.5, label, color=col, fontsize=11, fontweight='bold', ha='center')
    ax.text(x, y + 0.15, miss, color=SILVER, fontsize=8, ha='center')

# Power label for n=2
ax.text(13.5, 8.5, 'n = 2', color=WHITE, fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=WHITE, alpha=0.5))

# Draw n=2 via R_infty
for x, y, label, miss, col, is_verified in n2_via:
    parent_x = 12.0 if x == 12.0 else 12.0
    ax.annotate('', xy=(x, y + 0.9), xytext=(parent_x, 7.0),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.5, alpha=0.6))
    ls = '-' if is_verified else '--'
    box = FancyBboxPatch((x - 1.2, y), 2.4, 0.8, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.5, linestyle=ls)
    ax.add_patch(box)
    ax.text(x, y + 0.5, label, color=col, fontsize=11, fontweight='bold', ha='center')
    ax.text(x, y + 0.15, miss, color=SILVER, fontsize=8, ha='center')

# sigma_T from r_e
x, y, label, miss, col, is_verified = sigma_t
ax.annotate('', xy=(x, y + 0.9), xytext=(9.0, 7.0),
            arrowprops=dict(arrowstyle='->', color=col, lw=1.5, alpha=0.6))
box = FancyBboxPatch((x - 1.2, y), 2.4, 0.8, boxstyle='round,pad=0.15',
                     facecolor=PAN, edgecolor=col, linewidth=1.5, linestyle='--')
ax.add_patch(box)
ax.text(x, y + 0.5, label, color=col, fontsize=11, fontweight='bold', ha='center')
ax.text(x, y + 0.15, miss, color=SILVER, fontsize=8, ha='center')

# Legend
ax.plot([1.5, 2.5], [2.5, 2.5], color=GOLD, linewidth=2, linestyle='-')
ax.text(3.0, 2.5, 'Verified (5 constants)', color=SILVER, fontsize=9, va='center')
ax.plot([1.5, 2.5], [1.8, 1.8], color=GOLD, linewidth=2, linestyle='--')
ax.text(3.0, 1.8, 'Predicted (4 constants) *', color=SILVER, fontsize=9, va='center')

ax.text(9, 1.0, 'One measurement. One parameter. Nine constants. The tree moves as one.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'math7_01_constant_tree.png')


# ================================================================
# FIG 2: ALPHA-POWER SCALING LINE
# Type: Type 1 (Running/Convergence)
# Shows: miss = n x 0.219 ppb verified at n=1,2 and predicted at n=2,4
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# Scaling line
n_line = np.linspace(0, 4.5, 100)
miss_line = delta_alpha * n_line
ax.plot(n_line, miss_line, color=GOLD, linewidth=2.5, linestyle='--', alpha=0.7,
        label='miss = n ' + r'$\times$' + ' 0.219 ppb')

# Verified points — n=1
v1_labels = [r'$\alpha^{-1}$', r'$a_0$', r'$\mu_0$']
v1_offsets = [-0.08, 0.0, 0.08]
for i, (lbl, off) in enumerate(zip(v1_labels, v1_offsets)):
    ax.scatter([1 + off], [0.219], color=[GOLD, CYAN, GREEN][i], s=200,
               zorder=5, edgecolors=WHITE, linewidth=2)
    ax.annotate(lbl, xy=(1 + off, 0.219),
                xytext=(0.3 + i * 0.35, 0.32 + i * 0.04),
                color=[GOLD, CYAN, GREEN][i], fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=[GOLD, CYAN, GREEN][i], lw=1, alpha=0.6))

# Verified points — n=2
v2_data = [(r'$R_\infty$', 2 - 0.05, 0.437, ORANGE), ('f(1S-2S)', 2 + 0.05, 0.443, BLUE)]
for lbl, xp, yp, col in v2_data:
    ax.scatter([xp], [yp], color=col, s=200, zorder=5, edgecolors=WHITE, linewidth=2)
    yoff = 0.06 if lbl == 'f(1S-2S)' else -0.06
    ax.annotate(lbl, xy=(xp, yp), xytext=(xp + 0.2, yp + yoff),
                color=col, fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=col, lw=1, alpha=0.6))

# Predicted points — open circles
pred_data = [
    (r'$r_e$', 1.15, 0.222, MAG),
    (r'$E_h$', 2.15, 0.441, PURPLE),
    (r'$\sigma_0$', 2.25, 0.444, RED),
    (r'$\sigma_T$*', 2.35, 0.446, ORANGE),
]
for lbl, xp, yp, col in pred_data:
    ax.scatter([xp], [yp], color='none', s=200, zorder=5, edgecolors=col, linewidth=2.5)
    ax.annotate(lbl, xy=(xp, yp), xytext=(xp + 0.2, yp + 0.04),
                color=col, fontsize=9,
                arrowprops=dict(arrowstyle='->', color=col, lw=1, alpha=0.5))

# Reference lines
ax.axhline(y=0.219, color=DIM, linewidth=0.8, linestyle=':', alpha=0.4)
ax.axhline(y=0.437, color=DIM, linewidth=0.8, linestyle=':', alpha=0.4)
ax.text(4.3, 0.21, '0.219 ppb', color=DIM, fontsize=8)
ax.text(4.3, 0.43, '0.437 ppb', color=DIM, fontsize=8)

# Measurement band at n=2
ax.axhspan(0.43, 0.45, alpha=0.06, color=MAG)

# 2x arrow
ax.annotate('', xy=(4.1, 0.437), xytext=(4.1, 0.219),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(4.2, 0.328, r'$2\times$', color=GOLD, fontsize=14, fontweight='bold')

style_ax(ax, title=r'$\alpha$-Power Scaling: miss = n $\times$ 0.219 ppb',
         xlabel=r'Power of $\alpha$ in defining formula (n)',
         ylabel='Miss from measurement (ppb)')
ax.set_xlim(-0.3, 4.7)
ax.set_ylim(-0.05, 1.1)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['0', '1', '2', '3', '4'], fontsize=11, color=SILVER)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='upper left')

# Note
ax.text(2.5, 0.95, r'$\bullet$ Filled = verified    $\circ$ Open = predicted',
        color=SILVER, fontsize=9, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM))
ax.text(2.5, 0.04, r'*$\sigma_T$ $\alpha$-power pending formula resolution (n=2 or n=4)',
        color=DIM, fontsize=7, ha='center')

save(fig, 'math7_02_scaling_line.png')


# ================================================================
# FIG 3: FIVE GROUPS, THREE CONTINENTS
# Type: Type 4 (Geometric Cross-Section)
# Shows: Geographic independence of the five verification measurements
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

ax.text(9, 9.5, 'Five Independent Groups, Three Continents, One Scaling Law',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

# Central alpha symbol
alpha_circle = plt.Circle((9, 5), 1.2, facecolor=PAN, edgecolor=GOLD,
                          linewidth=3, zorder=10)
ax.add_patch(alpha_circle)
ax.text(9, 5.15, r'$\alpha^{-1}$', color=GOLD, fontsize=24, fontweight='bold',
        ha='center', va='center', zorder=11)
ax.text(9, 4.5, '137.036', color=SILVER, fontsize=10, ha='center', zorder=11)

# Five groups arranged around the center
groups = [
    (2.5, 8, 'Harvard', 'Fan et al. 2023', r'$a_e$ (Penning trap)', '0.11 ppb', MAG,
     'North America'),
    (15.5, 8, 'Paris (LKB)', 'Morel et al. 2020', r'$\alpha$ (Rb recoil)', '0.08 ppb', CYAN,
     'Europe'),
    (2.5, 2, 'Paris (BIPM)', 'SI 2019', r'$a_0$, $\mu_0$ (SI def.)', 'exact inputs', GREEN,
     'Europe'),
    (15.5, 2, 'Garching (MPQ)', 'Parthey et al. 2011', 'f(1S-2S) (laser)', '4.2e-15', BLUE,
     'Europe'),
    (9, 1.2, 'CODATA', 'Task Group 2018', r'$R_\infty$ (adjustment)', 'multi-input', ORANGE,
     'International'),
]

for x, y, name, ref, what, prec, col, continent in groups:
    # Box
    box = FancyBboxPatch((x - 2.0, y - 0.7), 4.0, 1.4, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.8, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + 0.3, name, color=col, fontsize=11, fontweight='bold', ha='center', zorder=4)
    ax.text(x, y - 0.05, what, color=WHITE, fontsize=8, ha='center', zorder=4)
    ax.text(x, y - 0.35, ref + '  |  ' + prec, color=DIM, fontsize=7, ha='center', zorder=4)

    # Line to center
    ax.plot([x, 9], [y, 5], color=col, linewidth=1.2, alpha=0.4, zorder=1)

    # Continent label
    ax.text(x, y + 0.85, continent, color=DIM, fontsize=7, ha='center', fontstyle='italic')

# Arrows from groups to alpha (on top of lines)
for x, y, _, _, _, _, col, _ in groups:
    dx = 9 - x
    dy = 5 - y
    dist = np.sqrt(dx**2 + dy**2)
    # Shorten arrow to stop at circle edge
    frac = 1.3 / dist
    ax.annotate('', xy=(9 - dx * frac, 5 - dy * frac),
                xytext=(x + dx * 0.15, y + dy * 0.15),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8, alpha=0.7))

save(fig, 'math7_03_five_groups.png')


# ================================================================
# FIG 4: DIAGNOSTIC SCENARIOS — FOUR DEVIATION PATTERNS
# Type: Type 3 (Threshold/Region)
# Shows: What different deviations from scaling would mean
# ================================================================

fig, axes = plt.subplots(2, 2, figsize=(18, 12), gridspec_kw={'hspace': 0.35, 'wspace': 0.30})
fig.patch.set_facecolor(BG)

scenarios = [
    (axes[0, 0], r'$R_\infty$ deviates, $a_0$ agrees',
     'Bound-state QED or nuclear size?',
     [(1, 0.219, CYAN, True), (2, 0.50, RED, True)],  # a0 on line, R_infty off
     True),
    (axes[0, 1], 'All constants shift together',
     r'New $a_e$ measurement shifts $\alpha$',
     [(1, 0.17, CYAN, True), (2, 0.34, ORANGE, True)],  # both shifted but on line
     False),
    (axes[1, 0], r'$m_e$ becomes visible at n=2',
     r'$\delta\alpha$ drops below 0.05 ppb',
     [(1, 0.05, CYAN, True), (2, 0.11, ORANGE, True)],  # R_infty slightly above line due to m_e
     True),
    (axes[1, 1], r'$\sigma_T$ tests n=4 (or n=2)',
     'Highest-power extrapolation',
     [(1, 0.219, CYAN, True), (2, 0.437, ORANGE, True), (4, 0.88, PURPLE, True)],
     False),
]

for ax_s, title, subtitle, points, show_deviation in scenarios:
    style_ax(ax_s, title=title, xlabel='n', ylabel='miss (ppb)')

    # Scaling line
    ns = np.linspace(0, 4.5, 100)
    if 'shift' in subtitle.lower():
        base = 0.17
    elif 'drops' in subtitle.lower():
        base = 0.05
    else:
        base = delta_alpha
    ax_s.plot(ns, base * ns, color=GOLD, linewidth=2, linestyle='--', alpha=0.6)

    # Points
    for n, miss, col, _ in points:
        on_line = abs(miss - base * n) < 0.02
        marker = 'o' if on_line else 'D'
        ax_s.scatter([n], [miss], color=col, s=180, zorder=5,
                     edgecolors=WHITE, linewidth=2, marker=marker)

    # Highlight deviation
    if show_deviation and len(points) >= 2:
        n_dev = points[-1][0]
        miss_dev = points[-1][1]
        miss_expected = base * n_dev
        if abs(miss_dev - miss_expected) > 0.02:
            ax_s.annotate('', xy=(n_dev + 0.15, miss_dev),
                          xytext=(n_dev + 0.15, miss_expected),
                          arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
            ax_s.text(n_dev + 0.35, (miss_dev + miss_expected) / 2,
                      'Signal!', color=RED, fontsize=10, fontweight='bold', va='center')

    ax_s.text(0.3, max(p[1] for p in points) * 0.85, subtitle,
              color=SILVER, fontsize=8, fontstyle='italic',
              bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.8))

    max_y = max(p[1] for p in points) * 1.3
    ax_s.set_xlim(-0.3, 4.8)
    ax_s.set_ylim(-0.02, max(max_y, 0.6))

fig.suptitle('Diagnostic Scenarios: What Deviations From Scaling Would Mean',
             color=WHITE, fontsize=16, fontweight='bold', y=0.98)

save(fig, 'math7_04_diagnostic_scenarios.png')


# ================================================================
# FIG 5: m_e DETECTABILITY THRESHOLD
# Type: Type 3 (Threshold/Region)
# Shows: When m_e contribution emerges from noise as delta_alpha decreases
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# X-axis: base delta_alpha (ppb), decreasing left to right
da_range = np.linspace(0.01, 0.35, 200)
# At n=2: full miss = sqrt((2*da)^2 + (1*0.03)^2)
# Pure alpha miss = 2*da
# m_e fraction = (full - pure) / full ... or better: m_e_contribution / full
# m_e contribution at n=2, m=1: 0.03 ppb
# Ratio = delta_me / (2*da) as fraction of the n=2 miss
me_fraction = delta_me / (2 * da_range) * 100  # percentage

ax.plot(da_range, me_fraction, color=CYAN, linewidth=2.5,
        label=r'$m_e$ contribution as % of $R_\infty$ miss')

# Threshold at 10% (detectable)
ax.axhline(y=10, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(0.33, 11, '10% (detectable)', color=GOLD, fontsize=10)

# Threshold at 50% (dominant)
ax.axhline(y=50, color=ORANGE, linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(0.33, 51, '50% (comparable)', color=ORANGE, fontsize=10)

# Threshold at 100% (m_e dominates)
ax.axhline(y=100, color=RED, linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(0.33, 101, '100% (m_e dominates)', color=RED, fontsize=10)

# Shade regions
ax.axhspan(0, 10, alpha=0.04, color=GREEN)
ax.axhspan(10, 50, alpha=0.04, color=GOLD)
ax.axhspan(50, 100, alpha=0.04, color=ORANGE)
ax.axhspan(100, 200, alpha=0.04, color=RED)

# Mark current position
current_frac = delta_me / (2 * delta_alpha) * 100
ax.scatter([delta_alpha], [current_frac], color=GOLD, s=250, zorder=5,
           edgecolors=WHITE, linewidth=2, marker='D')
ax.annotate('Current\n' + r'$\delta\alpha$ = 0.219 ppb' + '\n%.1f%%' % current_frac,
            xy=(delta_alpha, current_frac),
            xytext=(delta_alpha + 0.04, current_frac + 25),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark future scenarios
scenarios_me = [
    (0.14, 'New a_e\n(0.01 ppb)', CYAN),
    (0.05, 'Improved\nhadronic LbL', ORANGE),
    (0.02, 'All\nimproved', RED),
]
for da_s, label, col in scenarios_me:
    frac_s = delta_me / (2 * da_s) * 100
    ax.scatter([da_s], [frac_s], color=col, s=200, zorder=5,
               edgecolors=WHITE, linewidth=2, marker='o')
    ax.annotate(label, xy=(da_s, frac_s),
                xytext=(da_s + 0.03, frac_s + 15),
                color=col, fontsize=9,
                arrowprops=dict(arrowstyle='->', color=col, lw=1.2))

# Region labels
ax.text(0.28, 3, 'Single-parameter (pure ' + r'$\alpha$)', color=GREEN, fontsize=9)
ax.text(0.05, 3, 'Two-parameter\n(' + r'$\alpha + m_e$)', color=ORANGE, fontsize=9)

style_ax(ax, title=r'When Does $m_e$ Become Detectable in the Scaling Law?',
         xlabel=r'Base miss $\delta\alpha$ (ppb) — improving $\rightarrow$',
         ylabel=r'$m_e$ contribution as % of $R_\infty$ miss')
ax.set_xlim(0.005, 0.38)
ax.set_ylim(0, 180)
ax.invert_xaxis()  # decreasing delta_alpha = improving precision

save(fig, 'math7_05_me_threshold.png')


# ================================================================
# FIG 6: ALPHA EXTRACTION PIPELINE — SEVEN CORRECTIONS
# Type: Type 7 (Progression/Sequence)
# Shows: Seven corrections narrowing the miss from 3.99 to 0.219 ppb
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

ax.text(9, 9.5, r'The $\alpha$ Extraction Pipeline: Seven Corrections Narrow the Miss',
        color=GOLD, fontsize=15, fontweight='bold', ha='center')

# Start: uncorrected
start_miss = 3.99  # ppb
cumulative = start_miss
positions = np.linspace(1.5, 16.5, 9)  # start + 7 corrections + final

# Start box
ax.text(positions[0], 7.5, 'Uncorrected', color=MAG, fontsize=9, fontweight='bold', ha='center')
ax.text(positions[0], 7.0, '%.2f ppb' % start_miss, color=WHITE, fontsize=11,
        fontweight='bold', ha='center')
box_s = FancyBboxPatch((positions[0] - 0.8, 6.5), 1.6, 1.3, boxstyle='round,pad=0.15',
                       facecolor=PAN, edgecolor=MAG, linewidth=1.5)
ax.add_patch(box_s)

# Apply corrections sequentially
running_miss = start_miss
for i, (name, magnitude, col) in enumerate(corrections):
    running_miss -= magnitude
    x = positions[i + 1]
    # Correction arrow
    ax.annotate('', xy=(x - 0.3, 7.1), xytext=(positions[i] + 0.8, 7.1),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.8))
    # Correction label above
    ax.text((x + positions[i]) / 2, 8.3, name, color=col, fontsize=7, ha='center')
    ax.text((x + positions[i]) / 2, 7.8, '-%.3f' % magnitude, color=col, fontsize=8,
            fontweight='bold', ha='center')

    # Result box
    box_c = FancyBboxPatch((x - 0.8, 6.5), 1.6, 1.3, boxstyle='round,pad=0.15',
                           facecolor=PAN, edgecolor=col if i < 6 else GOLD, linewidth=1.5)
    ax.add_patch(box_c)
    ax.text(x, 7.0, '%.3f' % abs(running_miss), color=WHITE, fontsize=9,
            fontweight='bold', ha='center')

# Final result
x_final = positions[-1]
box_f = FancyBboxPatch((x_final - 0.8, 6.5), 1.6, 1.3, boxstyle='round,pad=0.15',
                       facecolor=PAN, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(box_f)
ax.text(x_final, 7.5, 'FINAL', color=GOLD, fontsize=9, fontweight='bold', ha='center')
ax.text(x_final, 7.0, '0.219 ppb', color=GOLD, fontsize=11, fontweight='bold', ha='center')

# Descending staircase visualization below
stair_y = 4.5
stair_h = 2.5
ax.text(0.5, stair_y + stair_h * 0.5, 'Miss\n(ppb)', color=SILVER, fontsize=9, ha='center')

# Draw staircase
cumulative = start_miss
stair_points_x = [positions[0]]
stair_points_y = [stair_y + stair_h * (cumulative / start_miss)]
for i, (name, magnitude, col) in enumerate(corrections):
    cumulative -= magnitude
    x_next = positions[i + 1]
    # Horizontal
    stair_points_x.append(x_next)
    stair_points_y.append(stair_points_y[-1])
    # Vertical drop
    new_y = stair_y + stair_h * max(cumulative / start_miss, 0.05)
    stair_points_x.append(x_next)
    stair_points_y.append(new_y)

ax.plot(stair_points_x, stair_points_y, color=GOLD, linewidth=2.5, zorder=3)

# Labels on staircase
ax.text(positions[0] - 0.3, stair_y + stair_h + 0.2, '3.99', color=MAG, fontsize=8)
ax.text(positions[-1] + 0.3, stair_y + stair_h * 0.06, '0.219', color=GOLD, fontsize=9,
        fontweight='bold')

# Baseline
ax.plot([positions[0] - 0.5, positions[-1] + 0.5], [stair_y, stair_y],
        color=DIM, linewidth=0.8, linestyle=':', alpha=0.4)
ax.text(0.5, stair_y - 0.3, '0 ppb', color=DIM, fontsize=7)

# Shaded area showing improvement
ax.fill_between([positions[0], positions[-1]],
                [stair_y + stair_h, stair_y + stair_h * 0.06],
                [stair_y + stair_h * 0.06, stair_y + stair_h * 0.06],
                alpha=0.05, color=GOLD)

ax.text(9, 1.5, 'Total improvement: 3.77 ppb from seven published corrections\n'
        'Bottleneck: hadronic light-by-light (0.536 ppb)',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN, edgecolor=DIM))

save(fig, 'math7_06_extraction_pipeline.png')


# ================================================================
# FIG 7: Rb CROSS-CHECK NUMBER LINE
# Type: Type 2 (Scale/Landscape)
# Shows: Two comparisons on one scale — Rb agreement vs CODATA base
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# We'll plot on a ppb scale centered on our extraction
# Our value = 0, Rb = -0.007, CODATA = -219 (in ppb offset)
# Use a broken or dual-zoom approach

# Main axis: full scale showing all three
positions = {'ours': 0, 'rb': -0.007, 'codata': -219}

# Plot two zones: zoomed-in (ours vs Rb) and full scale (all three)
# Use a single axis with a break indicator

# Full scale
ax.scatter([0], [2], color=GOLD, s=250, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='D')
ax.scatter([-0.007], [2], color=CYAN, s=250, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='o')
ax.scatter([-219], [2], color=ORANGE, s=200, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='s')

# Number line
ax.plot([-250, 30], [2, 2], color=DIM, linewidth=1.5, alpha=0.5)

# Labels
ax.annotate('Our extraction\n137.035999207', xy=(0, 2),
            xytext=(10, 3.5), color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))
ax.annotate('Rb recoil (Morel)\n137.035999206', xy=(-0.007, 2),
            xytext=(-60, 3.5), color=CYAN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
ax.annotate('CODATA 2018\n137.035999084', xy=(-219, 2),
            xytext=(-220, 3.5), color=ORANGE, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

# Gap annotations
# Us vs Rb gap
ax.annotate('', xy=(0, 1.3), xytext=(-0.007, 1.3),
            arrowprops=dict(arrowstyle='<->', color=CYAN, lw=2))
ax.text(-0.003, 0.8, '0.007 ppb\n(validates extraction)', color=CYAN, fontsize=10,
        fontweight='bold', ha='center')

# Us vs CODATA gap
ax.annotate('', xy=(0, 0.5), xytext=(-219, 0.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.5))
ax.text(-110, 0.0, '0.219 ppb\n(BASE of scaling law)', color=GOLD, fontsize=12,
        fontweight='bold', ha='center')

# Scale ratio
ax.text(-110, -0.8, 'The CODATA gap is 31' + r'$\times$' + ' the Rb gap',
        color=SILVER, fontsize=10, ha='center')
ax.text(-110, -1.3, 'Rb validates the extraction. CODATA provides the scaling base.\nThey test different things.',
        color=DIM, fontsize=9, ha='center')

style_ax(ax, title=r'Two Comparisons for $\alpha^{-1}$: Rb Cross-Check vs CODATA Base',
         xlabel=r'Offset from our extraction (ppb)')
ax.set_xlim(-260, 50)
ax.set_ylim(-2, 5)
ax.set_yticks([])
ax.spines['left'].set_visible(False)

save(fig, 'math7_07_rb_crosscheck.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE SCALING LAW
# Type: Type 8 (Identity Card)
# Shows: Complete scaling law result in one image
# ================================================================

fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)

# Main border
main_box = FancyBboxPatch((0.5, 0.5), 15, 10, boxstyle='round,pad=0.3',
                          facecolor=PAN, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(main_box)

# Title
ax.text(8, 10, r'MATH-7: The $\alpha$-Power Scaling Law', color=GOLD,
        fontsize=18, fontweight='bold', ha='center')

# Central equation
ax.text(8, 9, r'miss = n $\times$ 0.219 ppb', color=WHITE, fontsize=22,
        fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=2))

# Left column: verified
ax.text(1.5, 7.7, 'VERIFIED (5 constants)', color=GREEN, fontsize=11, fontweight='bold')
v_entries = [
    (r'$\alpha^{-1}$ vs CODATA', 'n=1', '0.219 ppb', GOLD),
    (r'$a_0$ (Bohr radius)', 'n=1', '0.219 ppb', CYAN),
    (r'$\mu_0$ (vac. perm.)', 'n=1', '0.219 ppb', GREEN),
    (r'$R_\infty$ (Rydberg)', 'n=2', '0.437 ppb', ORANGE),
    ('f(1S-2S) (hydrogen)', 'n=2', '0.443 ppb', BLUE),
]
for i, (name, power, miss, col) in enumerate(v_entries):
    y = 7.0 - i * 0.5
    ax.text(1.5, y, name, color=col, fontsize=9)
    ax.text(5.5, y, power, color=SILVER, fontsize=9)
    ax.text(6.5, y, miss, color=WHITE, fontsize=9, fontweight='bold')

# Right column: predicted
ax.text(9, 7.7, 'PREDICTED (4 constants)', color=ORANGE, fontsize=11, fontweight='bold')
p_entries = [
    (r'$r_e$ (classical e radius)', 'n=1', '0.222 ppb', MAG),
    (r'$E_h$ (Hartree energy)', 'n=2', '0.441 ppb', PURPLE),
    (r'$\sigma_0$ (Bohr x-sec)', 'n=2', '0.444 ppb', RED),
    (r'$\sigma_T$ (Thomson)', 'n=2*', '0.446 ppb*', ORANGE),
]
for i, (name, power, miss, col) in enumerate(p_entries):
    y = 7.0 - i * 0.5
    ax.text(9, y, name, color=col, fontsize=9)
    ax.text(13, y, power, color=SILVER, fontsize=9)
    ax.text(14, y, miss, color=WHITE, fontsize=9, fontweight='bold')

# Key facts
ax.text(1.5, 4.3, 'KEY FACTS', color=GOLD, fontsize=11, fontweight='bold')
facts = [
    ('Base miss:', r'$\delta\alpha$ = 0.219 ppb vs CODATA', GOLD),
    ('Rb cross-check:', '0.007 ppb (31' + r'$\times$' + ' tighter)', CYAN),
    ('Groups:', '5 independent, 3 continents', GREEN),
    ('SI 2019:', 'h, c, e exact ' + r'$\rightarrow$' + ' tree is single-parameter', SILVER),
    (r'$m_e$ threshold:', 'detectable when ' + r'$\delta\alpha$' + ' < 0.05 ppb', ORANGE),
]
for i, (label, val, col) in enumerate(facts):
    y = 3.7 - i * 0.45
    ax.text(1.5, y, label, color=SILVER, fontsize=9)
    ax.text(4.5, y, val, color=col, fontsize=9)

# Structural claim
ax.text(9, 4.3, 'STRUCTURAL CLAIM', color=GOLD, fontsize=11, fontweight='bold')
ax.text(9, 3.7, 'CODATA publishes four separate entries:', color=SILVER, fontsize=9)
ax.text(9, 3.3, r'$\alpha^{-1}$, $R_\infty$, $a_0$, $\mu_0$', color=WHITE, fontsize=10)
ax.text(9, 2.8, 'They are one entry raised to integer powers.', color=GOLD, fontsize=10,
        fontweight='bold')
ax.text(9, 2.3, 'The tree is a single-parameter family in ' + r'$\alpha$.',
        color=SILVER, fontsize=9)

# Bottom: the thesis
ax.text(8, 1.2, 'Every derived constant is ' + r'$\alpha^n$' +
        ' times exact numbers. The miss is n ' + r'$\times$' + ' ' + r'$\delta\alpha$' +
        '. The tree moves as one.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'math7_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "=" * 60)
print("MATH-7 DIAGRAMS COMPLETE")
print("=" * 60)
fnames = [
    'math7_01_constant_tree.png',
    'math7_02_scaling_line.png',
    'math7_03_five_groups.png',
    'math7_04_diagnostic_scenarios.png',
    'math7_05_me_threshold.png',
    'math7_06_extraction_pipeline.png',
    'math7_07_rb_crosscheck.png',
    'math7_08_identity_card.png',
]
for i, fn in enumerate(fnames):
    print("  Fig %d: %s" % (i + 1, fn))
print("=" * 60)
