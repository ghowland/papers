#!/usr/bin/env python3
"""
HOWL PHYS-48 Diagrams — The beta-zero Frontier
8 figures covering beta budget staircase, cancellation curve,
beta-0 subcategory tree, toroidal scaling, A4 vs measurements,
genus progression, electron/muon sector flip, dual geometry.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Wedge, Ellipse
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

print("PHYS-48 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: BETA BUDGET STAIRCASE — A1 THROUGH A3
# Type: Comparison Bar (D5.6)
# Shows: Three groups of stacked bars showing beta^0/beta^2/beta^4
#        fractions at each loop order. The shift from geometry-
#        dominant (A2) to number-theory-dominant (A3).
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Loop Order', r'Fraction of $|A_n|$ by $\beta$ class')

loops = [1, 2, 3]
x_pos = np.array([0, 1.5, 3.0])
bar_w = 0.8

# Data
beta0_frac = [1.000, 0.466, 0.513]
beta2_frac = [0.000, 0.534, 0.247]
beta4_frac = [0.000, 0.000, 0.240]

# Stacked bars
bars_b0 = ax.bar(x_pos, beta0_frac, bar_w, color=SILVER, alpha=0.7,
                  edgecolor=SILVER, linewidth=2, label=r'$\beta^0$ (number theory)')
bars_b2 = ax.bar(x_pos, beta2_frac, bar_w, bottom=beta0_frac,
                  color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=2,
                  label=r'$\beta^2$ (one angular)')
b4_bottom = [a + b for a, b in zip(beta0_frac, beta2_frac)]
bars_b4 = ax.bar(x_pos, beta4_frac, bar_w, bottom=b4_bottom,
                  color=PURPLE, alpha=0.7, edgecolor=PURPLE, linewidth=2,
                  label=r'$\beta^4$ (two angular)')

# Percentage labels
for i, x in enumerate(x_pos):
    if beta0_frac[i] > 0.05:
        ax.text(x, beta0_frac[i] / 2, '%.1f%%' % (beta0_frac[i] * 100),
                color=WHITE, fontsize=11, ha='center', va='center', fontweight='bold')
    if beta2_frac[i] > 0.05:
        ax.text(x, beta0_frac[i] + beta2_frac[i] / 2,
                '%.1f%%' % (beta2_frac[i] * 100),
                color=WHITE, fontsize=11, ha='center', va='center', fontweight='bold')
    if beta4_frac[i] > 0.05:
        ax.text(x, b4_bottom[i] + beta4_frac[i] / 2,
                '%.1f%%' % (beta4_frac[i] * 100),
                color=WHITE, fontsize=11, ha='center', va='center', fontweight='bold')

# Loop 4 placeholder
ax.bar(4.5, 0.15, bar_w, color=RED, alpha=0.3, edgecolor=RED, linewidth=2)
ax.text(4.5, 0.08, '?', color=RED, fontsize=24, ha='center', va='center',
        fontweight='bold')
ax.text(4.5, -0.08, 'Loop 4\n+ Laporta', color=RED, fontsize=9,
        ha='center', fontweight='bold')

# Labels
ax.set_xticks(list(x_pos) + [4.5])
ax.set_xticklabels([r'$A_1$ (1 loop)', r'$A_2$ (2 loops)',
                     r'$A_3$ (3 loops)', r'$A_4$ (4 loops)'],
                    color=WHITE, fontsize=10)

ax.axhline(1.0, color=DIM, lw=0.5, ls=':', alpha=0.3)

# Cancellation annotation
cancel_data = [(0, '0%'), (1.5, '90.4%'), (3.0, '99.5%'), (4.5, '?')]
for x, c in cancel_data:
    color = GOLD if c != '?' else RED
    ax.text(x, 1.05, 'Cancel: %s' % c, color=color, fontsize=9,
            ha='center', fontweight='bold')

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper right')

ax.set_xlim(-0.7, 5.5)
ax.set_ylim(-0.15, 1.2)

ax.set_title(r'The $\beta$ Budget: From Pure Number Theory to the Toroidal Frontier',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_01_beta_budget_staircase.png')


# ================================================================
# FIG 2: CANCELLATION STAIRCASE — 0% to 99.5% to ?
# Type: Running/Convergence (D5.1)
# Shows: Cancellation percentage vs loop order. The curve rises
#        toward 100% but the question mark at loop 4 marks the
#        breaking point where Laporta constants escape.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Loop Order', 'Cancellation (%)')

loops = [1, 2, 3]
cancel = [0, 90.4, 99.5]

ax.plot(loops, cancel, 'o-', color=CYAN, lw=2.5, markersize=14, zorder=5)

# Labels on each point
for l, c in zip(loops, cancel):
    ax.text(l + 0.12, c - 3, '%.1f%%' % c, color=CYAN, fontsize=12,
            fontweight='bold')

# Loop 4 question mark
ax.plot(4, 99.9, 'o', color=RED, markersize=14, zorder=5)
ax.text(4 + 0.12, 99.9 - 2, '?', color=RED, fontsize=18, fontweight='bold')

# Asymptote at 100%
ax.axhline(100, color=GOLD, lw=1.5, ls='--', alpha=0.5)
ax.text(4.5, 100.3, '100% (exact cancellation)', color=GOLD, fontsize=10)

# The breaking zone
ax.fill_between([3.5, 4.5], 99, 101, color=RED, alpha=0.06)
ax.text(4.0, 96, 'BREAKING\nPOINT', color=RED, fontsize=12,
        ha='center', fontweight='bold', style='italic')

# Annotation: what breaks
ax.text(1.0, 60,
        'Spherical cancellation tightens\n'
        'by ~10 pp per loop order.\n\n'
        'At loop 4, Laporta constants\n'
        'cannot participate in exact\n'
        'cancellation with known constants.',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, linewidth=1))

# Term growth annotation
ax.text(2.5, 30,
        'Largest term per loop:\n'
        r'$A_1$: 0.5   $A_2$: 3.4   $A_3$: 227',
        color=ORANGE, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE, linewidth=1))

ax.set_xlim(0.5, 5)
ax.set_ylim(-5, 105)
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['1 loop', '2 loops', '3 loops', '4 loops'],
                    color=WHITE, fontsize=10)

ax.set_title(r'The Cancellation Staircase: Approaching 100% Until It Breaks',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_02_cancellation_staircase.png')


# ================================================================
# FIG 3: BETA-0 SUBCATEGORY TREE
# Type: Geometric Cross-Section (D5.4)
# Shows: beta^0 splits into number-theoretic (rational, zeta, Li)
#        and toroidal-geometric (Laporta, elliptic). The branch
#        point is the discovery.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Root node
root_x, root_y = 0.5, 0.88
ax.text(root_x, root_y, r'$\beta^0$ (no $\pi$ content)',
        color=WHITE, fontsize=16, fontweight='bold', ha='center',
        transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=WHITE, linewidth=2))

# Left branch: number-theoretic
left_x, left_y = 0.25, 0.65
ax.annotate('', xy=(left_x, left_y + 0.06), xytext=(root_x - 0.05, root_y - 0.05),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2),
            transform=ax.transAxes)
ax.text(left_x, left_y, 'Number-Theoretic', color=CYAN, fontsize=14,
        fontweight='bold', ha='center', transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, linewidth=2))

# Left sub-branches
left_items = [
    (0.08, 0.45, 'Rational\n197/144, 28259/5184', 'Loops 1+'),
    (0.22, 0.45, r'$\zeta$ values' + '\n' + r'$\zeta(3), \zeta(5)$', 'Loops 2+'),
    (0.36, 0.45, 'Polylog / MZV\nLi' + r'$_4(\frac{1}{2})$' + r', $\zeta(3,5)$', 'Loops 3+'),
]
for lx, ly, text, loop_text in left_items:
    ax.annotate('', xy=(lx, ly + 0.06), xytext=(left_x, left_y - 0.04),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
                transform=ax.transAxes)
    ax.text(lx, ly, text, color=CYAN, fontsize=9, ha='center',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1))
    ax.text(lx, ly - 0.08, loop_text, color=DIM, fontsize=8, ha='center',
            transform=ax.transAxes)

# PSLQ exhausted label
ax.text(0.22, 0.30, '24/24 PSLQ NULL\n(exhausted)', color=GREEN,
        fontsize=11, ha='center', transform=ax.transAxes, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, linewidth=1.5))

# Right branch: toroidal-geometric
right_x, right_y = 0.75, 0.65
ax.annotate('', xy=(right_x, right_y + 0.06), xytext=(root_x + 0.05, root_y - 0.05),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5),
            transform=ax.transAxes)
ax.text(right_x, right_y, 'Toroidal-Geometric\n(NEW)', color=GOLD, fontsize=14,
        fontweight='bold', ha='center', transform=ax.transAxes,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2.5))

# Right sub-branches
right_items = [
    (0.62, 0.45, 'Laporta Constants\nC81a-c, C83a-c', 'Loop 4 (first time)'),
    (0.88, 0.45, 'Elliptic Periods?\nK(k), E(k)', 'Attack 3 will test'),
]
for rx, ry, text, note in right_items:
    ax.annotate('', xy=(rx, ry + 0.06), xytext=(right_x, right_y - 0.04),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
                transform=ax.transAxes)
    ax.text(rx, ry, text, color=GOLD, fontsize=10, ha='center',
            transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.5))
    ax.text(rx, ry - 0.08, note, color=RED, fontsize=9, ha='center',
            transform=ax.transAxes, fontweight='bold')

# Evidence summary
ax.text(0.75, 0.28, 'Evidence:', color=WHITE, fontsize=11,
        transform=ax.transAxes, fontweight='bold')
evidence = [
    r'$\bullet$ No $\pi$ content (24/24 null)',
    r'$\bullet$ Not $\zeta$, Li, MZV (24/24 null)',
    r'$\bullet$ Match elliptic forms < 0.006%',
    r'$\bullet$ Mutually independent (11/11 null)',
    r'$\bullet$ Scale as $(m/m_e)^2$ (toroidal)',
]
for i, e in enumerate(evidence):
    ax.text(0.75, 0.24 - i * 0.04, e, color=GOLD, fontsize=9,
            transform=ax.transAxes)

# Sphere vs torus labels at bottom
ax.text(0.22, 0.15, r'SPHERE (genus 0)', color=CYAN, fontsize=13,
        ha='center', transform=ax.transAxes, fontweight='bold')
ax.text(0.22, 0.11, r'Constants carry $\pi = 4\beta$', color=CYAN,
        fontsize=10, ha='center', transform=ax.transAxes)

ax.text(0.75, 0.15, 'TORUS (genus 1)', color=GOLD, fontsize=13,
        ha='center', transform=ax.transAxes, fontweight='bold')
ax.text(0.75, 0.11, 'Constants carry K(k), E(k)', color=GOLD,
        fontsize=10, ha='center', transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title(r'The $\beta^0$ Subcategory Split: Number Theory vs Toroidal Geometry',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys48_03_beta0_subcategory_tree.png')


# ================================================================
# FIG 4: TOROIDAL SCALING CURVE — MASS-DEP FRACTION vs MASS
# Type: Running/Convergence (D5.1)
# Shows: The (m/m_e)^2 curve of toroidal/universal ratio.
#        Electron at bottom left, muon in middle, tau off chart.
#        Crossover at 43 m_e marked.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Lepton mass / $m_e$', 'Toroidal / Universal ratio (%)')

mass_ratio = np.logspace(0, 4, 500)
toroidal_pct = mass_ratio**2 * 0.054  # electron baseline 0.054%

ax.plot(mass_ratio, toroidal_pct, color=GOLD, lw=2.5)

# Key points
points = [
    (1.0, 0.054, 'Electron\n0.054%', CYAN),
    (43, 100, 'Crossover\n43 ' + r'$m_e$' + '\n(~22 MeV)', ORANGE),
    (206.77, 2304, 'Muon\n2304%', MAG),
    (3477, 650000, 'Tau\n650,000%', RED),
]

for m, t, label, color in points:
    if t < 1e6:
        ax.plot(m, t, 'o', color=color, markersize=12, zorder=6)
        y_off = t * 1.8 if t > 10 else t + 0.3
        ax.annotate(label, xy=(m, t), xytext=(m * 1.5, y_off),
                    color=color, fontsize=10, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

# Crossover line
ax.axhline(100, color=ORANGE, lw=1.5, ls='--', alpha=0.5)
ax.text(5000, 130, 'Universal = Toroidal', color=ORANGE, fontsize=9)

# Regions
ax.fill_between(mass_ratio, 0.01, 100, where=mass_ratio < 43,
                color=CYAN, alpha=0.03)
ax.fill_between(mass_ratio, 100, 1e7, where=mass_ratio > 43,
                color=GOLD, alpha=0.03)

ax.text(5, 0.03, 'Spherical sector\ndominates', color=CYAN,
        fontsize=11, style='italic')
ax.text(500, 5e4, 'Toroidal sector\ndominates', color=GOLD,
        fontsize=11, style='italic')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(0.8, 1e4)
ax.set_ylim(0.01, 1e7)

ax.set_title(r'Toroidal Scaling: $(m/m_e)^2$ Amplification of the Non-Spherical Sector',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_04_toroidal_scaling.png')


# ================================================================
# FIG 5: A4 vs HARVARD AND FNAL
# Type: Threshold/Region (D5.3)
# Shows: One A4 contribution bar against two measurement bands.
#        A4 towers above Harvard (electron), sits below FNAL (muon).
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

# Left panel: Electron
setup_ax(ax1, '', '', r'Magnitude ($\times 10^{-12}$)')
ae_a4 = 55.67  # in units of 1e-12
ae_unc = 1.3

ax1.bar(0.5, ae_a4, 0.6, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=2)
ax1.text(0.5, ae_a4 + 2, '%.1f' % ae_a4, color=GOLD, fontsize=14,
         ha='center', fontweight='bold')

ax1.axhspan(0, ae_unc, color=MAG, alpha=0.15)
ax1.axhline(ae_unc, color=MAG, lw=2, ls='--')
ax1.text(1.1, ae_unc + 1, r'Harvard $\pm$%.1f' % ae_unc,
         color=MAG, fontsize=10, fontweight='bold')

ax1.text(0.5, ae_a4 / 2, r'$43\times$' + '\nabove', color=WHITE,
         fontsize=16, ha='center', va='center', fontweight='bold')

ax1.set_xlim(-0.2, 1.5)
ax1.set_ylim(0, 70)
ax1.set_xticks([0.5])
ax1.set_xticklabels(['Electron'], color=WHITE, fontsize=12)
ax1.set_title(r'$A_4$ DOMINATES for electron', color=CYAN,
              fontsize=13, fontweight='bold', pad=10)

# Right panel: Muon
setup_ax(ax2, '', '', r'Magnitude ($\times 10^{-10}$)')
amu_a4 = 0.557  # in units of 1e-10
amu_unc = 2.2    # FNAL unc in 1e-10

ax2.bar(0.5, amu_a4, 0.6, color=GOLD, alpha=0.7, edgecolor=GOLD, linewidth=2)
ax2.text(0.5, amu_a4 + 0.1, '%.2f' % amu_a4, color=GOLD, fontsize=14,
         ha='center', fontweight='bold')

ax2.axhspan(0, amu_unc, color=MAG, alpha=0.15)
ax2.axhline(amu_unc, color=MAG, lw=2, ls='--')
ax2.text(1.1, amu_unc + 0.1, r'FNAL $\pm$%.1f' % amu_unc,
         color=MAG, fontsize=10, fontweight='bold')

ax2.text(0.5, amu_unc / 2, r'$0.25\times$' + '\nbelow', color=WHITE,
         fontsize=16, ha='center', va='center', fontweight='bold')

ax2.set_xlim(-0.2, 1.5)
ax2.set_ylim(0, 3.5)
ax2.set_xticks([0.5])
ax2.set_xticklabels(['Muon'], color=WHITE, fontsize=12)
ax2.set_title(r'$A_4$ INVISIBLE for muon', color=MAG,
              fontsize=13, fontweight='bold', pad=10)

fig.suptitle(r'Same $A_4$, Different Impact: Electron (43$\times$) vs Muon (0.25$\times$)',
             color=GOLD, fontsize=15, fontweight='bold', y=0.98)

save(fig, 'phys48_05_a4_vs_measurements.png')


# ================================================================
# FIG 6: GENUS PROGRESSION — SPHERE to TORUS to ?
# Type: Scale/Landscape (D5.2)
# Shows: Loop 1-3 on spheres, loop 4 on a torus, loop 5+ unknown.
#        Visual progression of topological complexity.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

# Five positions along x
positions = [1.5, 4.5, 7.5, 10.5, 13.5]
labels_top = ['Loop 1', 'Loop 2', 'Loop 3', 'Loop 4', 'Loop 5+']
labels_bot = ['trivial', 'genus 0', 'genus 0', 'genus 0+1', 'genus 0+1+2?']
colors_list = [DIM, CYAN, CYAN, GOLD, RED]

for i, (px, lt, lb, col) in enumerate(zip(positions, labels_top, labels_bot, colors_list)):
    # Draw the shape
    if i == 0:
        # Point
        ax.plot(px, 3, 'o', color=col, markersize=20, zorder=5)
        ax.text(px, 2.2, 'Point', color=col, fontsize=10, ha='center')
    elif i <= 2:
        # Sphere
        circle = Circle((px, 3), 1.0, facecolor=col, alpha=0.12,
                          edgecolor=col, linewidth=2)
        ax.add_patch(circle)
        ax.text(px, 2.2, 'Sphere', color=col, fontsize=10, ha='center')
    elif i == 3:
        # Torus
        outer = Ellipse((px, 3), 2.5, 1.6, facecolor='none',
                          edgecolor=col, linewidth=2.5)
        inner = Ellipse((px, 3.1), 0.8, 0.4, facecolor=PAN,
                          edgecolor=col, linewidth=1.5, linestyle='--')
        ax.add_patch(outer)
        ax.add_patch(inner)
        ax.text(px, 1.8, 'Torus', color=col, fontsize=10,
                ha='center', fontweight='bold')
    else:
        # Question mark — higher genus
        ax.text(px, 3, '?', color=col, fontsize=40, ha='center',
                va='center', fontweight='bold')
        ax.text(px, 1.8, 'Higher genus?', color=col, fontsize=10,
                ha='center', style='italic')

    # Top label
    ax.text(px, 5.2, lt, color=WHITE, fontsize=12, ha='center',
            fontweight='bold')
    # Bottom label
    ax.text(px, 1.0, lb, color=col, fontsize=9, ha='center')

# Arrows between
for i in range(4):
    ax.annotate('', xy=(positions[i+1] - 1.2, 3),
                xytext=(positions[i] + 1.2, 3),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Constants produced labels
const_labels = [
    r'$\frac{1}{2}$',
    r'$\pi, \zeta(3), \ln 2$',
    r'$\pi^4, \zeta(5), \mathrm{Li}_4$',
    'Laporta\nC81, C83',
    '???',
]
const_colors = [DIM, CYAN, CYAN, GOLD, RED]
for px, cl, cc in zip(positions, const_labels, const_colors):
    ax.text(px, 4.3, cl, color=cc, fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                      edgecolor=cc, linewidth=0.8))

# The transition annotation
ax.annotate('GEOMETRIC\nPHASE\nTRANSITION',
            xy=(9, 3), xytext=(9, 5.8),
            color=GOLD, fontsize=11, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.set_xlim(-0.5, 15.5)
ax.set_ylim(0.3, 6.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('The Genus Progression: Each Loop Order Discovers Deeper Topology',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_06_genus_progression.png')


# ================================================================
# FIG 7: ELECTRON vs MUON SECTOR FLIP
# Type: Comparison Bar (D5.6)
# Shows: Two side-by-side stacked bars. Electron: universal huge,
#        mass-dep tiny. Muon: mass-dep huge, universal tiny.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', 'Relative contribution (log scale)')

# Data (normalized: universal = 1.0 for both, mass-dep scaled)
x_e = 0.8
x_mu = 2.2
bar_w = 0.7

# Electron
ax.bar(x_e - 0.18, 1.0, bar_w * 0.45, color=CYAN, alpha=0.7,
       edgecolor=CYAN, linewidth=2, label='Universal (Laporta)')
ax.bar(x_e + 0.18, 0.00054, bar_w * 0.45, color=GOLD, alpha=0.7,
       edgecolor=GOLD, linewidth=2, label='Mass-dependent')

# Muon
ax.bar(x_mu - 0.18, 1.0, bar_w * 0.45, color=CYAN, alpha=0.7,
       edgecolor=CYAN, linewidth=2)
ax.bar(x_mu + 0.18, 23.04, bar_w * 0.45, color=GOLD, alpha=0.7,
       edgecolor=GOLD, linewidth=2)

# Labels
ax.text(x_e - 0.18, 1.3, '1.0', color=CYAN, fontsize=11, ha='center',
        fontweight='bold')
ax.text(x_e + 0.18, 0.003, '0.0005', color=GOLD, fontsize=9, ha='center',
        fontweight='bold')
ax.text(x_e, 0.00015, r'$\times 1800$', color=WHITE, fontsize=10,
        ha='center', fontweight='bold')

ax.text(x_mu - 0.18, 1.3, '1.0', color=CYAN, fontsize=11, ha='center',
        fontweight='bold')
ax.text(x_mu + 0.18, 28, '23.0', color=GOLD, fontsize=11, ha='center',
        fontweight='bold')
ax.text(x_mu, 0.3, r'$\times 23$', color=WHITE, fontsize=10,
        ha='center', fontweight='bold')

# Dominance arrows
ax.annotate('SPHERICAL\nDOMINATES', xy=(x_e - 0.18, 0.6),
            xytext=(x_e - 0.6, 0.1),
            color=CYAN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.annotate('TOROIDAL\nDOMINATES', xy=(x_mu + 0.18, 15),
            xytext=(x_mu + 0.6, 8),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax.set_yscale('log')
ax.set_xlim(0, 3.2)
ax.set_ylim(0.0001, 50)
ax.set_xticks([x_e, x_mu])
ax.set_xticklabels(['Electron\n(0.511 MeV)', 'Muon\n(105.7 MeV)'],
                    color=WHITE, fontsize=11)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper left')

ax.set_title('The Sector Flip: Same Physics, Different Dominant Geometry',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_07_sector_flip.png')


# ================================================================
# FIG 8: DUAL GEOMETRY ON THE PROTON
# Type: Geometric Cross-Section (D5.4)
# Shows: A proton with spherical confinement boundary and
#        toroidal gluon flux tubes. Two geometries on one object.
#        Labels connect to the QED parallel.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

cx, cy = 0, 0

# Spherical confinement boundary
conf = Circle((cx, cy), 3.0, facecolor=CYAN, alpha=0.06,
               edgecolor=CYAN, linewidth=2.5, linestyle='-')
ax.add_patch(conf)

# Inner charge distribution (roughly spherical)
charge = Circle((cx, cy), 1.5, facecolor=CYAN, alpha=0.08,
                  edgecolor=CYAN, linewidth=1.5, linestyle='--')
ax.add_patch(charge)

# Three quarks (as points)
quark_angles = [np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3]
quark_colors = [RED, GREEN, BLUE]
quark_labels = ['u', 'd', 'u']
for angle, qc, ql in zip(quark_angles, quark_colors, quark_labels):
    qx = cx + 0.8 * np.cos(angle)
    qy = cy + 0.8 * np.sin(angle)
    ax.plot(qx, qy, 'o', color=qc, markersize=16, zorder=6)
    ax.text(qx, qy, ql, color=WHITE, fontsize=9, ha='center',
            va='center', fontweight='bold', zorder=7)

# Gluon flux tubes (toroidal — draw as curved lines between quarks)
for i in range(3):
    a1 = quark_angles[i]
    a2 = quark_angles[(i + 1) % 3]
    t = np.linspace(0, 1, 50)
    # Curved path between quarks (bulging outward)
    mid_angle = (a1 + a2) / 2
    r_mid = 1.8
    path_x = cx + (0.8 * np.cos(a1) * (1 - t) + 0.8 * np.cos(a2) * t
                    + 0.5 * np.sin(np.pi * t) * r_mid * np.cos(mid_angle))
    path_y = cy + (0.8 * np.sin(a1) * (1 - t) + 0.8 * np.sin(a2) * t
                    + 0.5 * np.sin(np.pi * t) * r_mid * np.sin(mid_angle))

    # Draw with wavy line (gluon-like)
    wave = 0.08 * np.sin(20 * np.pi * t)
    path_x += wave * np.cos(mid_angle + np.pi/2)
    path_y += wave * np.sin(mid_angle + np.pi/2)

    ax.plot(path_x, path_y, color=GOLD, lw=2, alpha=0.6)

# Labels
ax.text(3.5, 2.5, 'SPHERICAL:', color=CYAN, fontsize=13,
        fontweight='bold')
ax.text(3.5, 2.0, 'Confinement boundary', color=CYAN, fontsize=11)
ax.text(3.5, 1.5, r'$r \approx 0.84$ fm', color=CYAN, fontsize=10)
ax.text(3.5, 1.0, r'Constants: $\pi, \zeta(3)$', color=CYAN, fontsize=10)
ax.text(3.5, 0.5, r'$C = 6\beta = 3\pi/2$', color=CYAN, fontsize=10)
ax.text(3.5, 0.0, r'$\beta$ content: $\beta^2$', color=CYAN, fontsize=10)

ax.text(3.5, -1.5, 'TOROIDAL:', color=GOLD, fontsize=13,
        fontweight='bold')
ax.text(3.5, -2.0, 'Gluon flux tubes', color=GOLD, fontsize=11)
ax.text(3.5, -2.5, 'Color circulation within boundary', color=GOLD,
        fontsize=10)
ax.text(3.5, -3.0, 'Constants: Laporta C81, C83?', color=GOLD,
        fontsize=10)
ax.text(3.5, -3.5, r'$\beta$ content: $\beta^0$ (toroidal)', color=GOLD,
        fontsize=10)

# QED parallel annotation
ax.text(-4.5, -3.5,
        'Same dual geometry in QED:\n'
        r'Angular integrals $\to \pi$ (spherical)' + '\n'
        r'Topology 81/83 $\to$ Laporta (toroidal)',
        color=WHITE, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                  edgecolor=WHITE, linewidth=1.5))

# 99% label
ax.text(cx, cy - 2.2, '99% of proton mass\nis confinement energy\n(toroidal circulation)',
        color=GOLD, fontsize=10, ha='center', style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                  edgecolor=GOLD, linewidth=1))

ax.set_xlim(-5.5, 7.5)
ax.set_ylim(-5, 4.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('Dual Geometry: The Proton Has Both Spherical and Toroidal Structure',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys48_08_dual_geometry_proton.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys48_01_beta_budget_staircase.png")
print("  phys48_02_cancellation_staircase.png")
print("  phys48_03_beta0_subcategory_tree.png")
print("  phys48_04_toroidal_scaling.png")
print("  phys48_05_a4_vs_measurements.png")
print("  phys48_06_genus_progression.png")
print("  phys48_07_sector_flip.png")
print("  phys48_08_dual_geometry_proton.png")
print("=" * 50)
