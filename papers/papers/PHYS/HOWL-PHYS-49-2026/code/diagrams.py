#!/usr/bin/env python3
"""
HOWL PHYS-49 Diagrams — The Complete Decomposition
8 figures covering three-layer stacked bars, subtraction improvement,
A2 waterfall, framework bridge, A4 on K/pi curve, K/pi divergence,
dual geometry at four scales, and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, Arc
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

print("PHYS-49 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: THREE-LAYER STACKED BARS — A1 THROUGH A4
# Type: Comparison Bar (D5.6)
# Shows: At each loop order, the three layers as stacked bars.
#        Layer 2 (toroidal) is zero at loops 1-3 and appears at loop 4.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Loop Order', 'Absolute magnitude of each layer')

x_pos = np.array([0, 1.5, 3.0, 4.5])
bar_w = 0.8

# Data: absolute values of each layer
modulus  = [0, 2.598, 21.833, 0.841]      # spherical
layer1   = [0.500, 2.270, 23.015, 1.071]  # number-theoretic
layer2   = [0, 0, 0, 0.5]                  # toroidal (estimated, illustrative)

ax.bar(x_pos, modulus, bar_w, color=CYAN, alpha=0.7,
       edgecolor=CYAN, linewidth=2, label='Modulus (spherical ' + r'$\beta^{2+}$)')
ax.bar(x_pos, layer1, bar_w, bottom=modulus, color=SILVER, alpha=0.7,
       edgecolor=SILVER, linewidth=2, label=r'Layer 1 (number-theoretic $\beta^0$)')
l2_bottom = [a + b for a, b in zip(modulus, layer1)]
ax.bar(x_pos, layer2, bar_w, bottom=l2_bottom, color=GOLD, alpha=0.8,
       edgecolor=GOLD, linewidth=2.5, label=r'Layer 2 (toroidal $\beta^0$) — NEW')

# Labels
for i, x in enumerate(x_pos):
    total = modulus[i] + layer1[i] + layer2[i]
    if modulus[i] > 0.3:
        ax.text(x, modulus[i] / 2, '%.1f' % modulus[i], color=WHITE,
                fontsize=10, ha='center', va='center', fontweight='bold')
    if layer1[i] > 0.3:
        ax.text(x, modulus[i] + layer1[i] / 2, '%.1f' % layer1[i],
                color=WHITE, fontsize=10, ha='center', va='center', fontweight='bold')
    if layer2[i] > 0.1:
        ax.text(x, l2_bottom[i] + layer2[i] / 2, '?',
                color=WHITE, fontsize=14, ha='center', va='center', fontweight='bold')

# Net value annotations
nets = ['+0.500', '-0.328', '+1.181', '-1.912']
for i, (x, n) in enumerate(zip(x_pos, nets)):
    total = modulus[i] + layer1[i] + layer2[i]
    ax.text(x, total + 1.2, 'Net: %s' % n, color=GOLD, fontsize=10,
            ha='center', fontweight='bold')

# Arrow to layer 2
ax.annotate('FIRST\nAPPEARANCE',
            xy=(4.5, l2_bottom[3] + 0.25), xytext=(5.5, 15),
            color=GOLD, fontsize=12, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.set_xticks(x_pos)
ax.set_xticklabels([r'$A_1$ (1 loop)', r'$A_2$ (2 loops)',
                     r'$A_3$ (3 loops)', r'$A_4$ (4 loops)'],
                    color=WHITE, fontsize=10)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper left')
ax.set_xlim(-0.7, 6.5)
ax.set_ylim(0, 50)

ax.set_title('The Three-Layer Decomposition: Toroidal Layer Appears at Loop 4',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_01_three_layer_bars.png')


# ================================================================
# FIG 2: SUBTRACTION IMPROVEMENT — 6 PAIRS RAW vs POST-SUB
# Type: Comparison Bar (D5.6)
# Shows: Six pairs of bars. Raw miss (taller) vs post-subtraction
#        miss (shorter). Every pair drops. The unanimity is visual.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'Elliptic match miss (%)')

labels = ['C81a', 'C81b', 'C81c', 'C83a', 'C83b', 'C83c']
raw_miss = [0.01771, 0.00311, 0.00156, 0.00133, 0.00267, 0.000826]
sub_miss = [0.00121, 0.0000117, 0.0000208, 0.000200, 0.0000163, 0.0000226]
improvements = [r/s if s > 0 else 0 for r, s in zip(raw_miss, sub_miss)]

x_pos = np.arange(len(labels))
bar_w = 0.35

bars_raw = ax.bar(x_pos - 0.2, raw_miss, bar_w, color=RED, alpha=0.6,
                   edgecolor=RED, linewidth=2, label='Raw scan')
bars_sub = ax.bar(x_pos + 0.2, sub_miss, bar_w, color=GREEN, alpha=0.7,
                   edgecolor=GREEN, linewidth=2, label=r'After $\zeta$ subtraction')

# Improvement labels
for i, (x, imp) in enumerate(zip(x_pos, improvements)):
    ax.text(x, raw_miss[i] * 1.5, '%.0f' % imp + r'$\times$',
            color=GOLD, fontsize=11, ha='center', fontweight='bold')

# Subtraction detail
sub_details = [r'+2$\zeta(3)$', r'-5$\zeta(5)$', r'+2$\zeta(5)$',
               r'-3$\zeta(3)$', r'+4$\zeta(3)$', r'-2$\zeta(5)$']
for i, (x, d) in enumerate(zip(x_pos, sub_details)):
    ax.text(x + 0.2, sub_miss[i] * 0.3 if sub_miss[i] > 0.0001 else 0.000005,
            d, color=GREEN, fontsize=8, ha='center', rotation=0)

ax.set_yscale('log')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, color=WHITE, fontsize=11)
ax.set_ylim(5e-6, 0.05)

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper right')

ax.text(2.5, 0.03, '6/6 improved. Average: 94' + r'$\times$',
        color=GOLD, fontsize=13, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=2))

ax.set_title(r'Subtracting $\zeta$ Content Reveals Elliptic Structure in Every Integral',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_02_subtraction_improvement.png')


# ================================================================
# FIG 3: A2 WATERFALL DECOMPOSITION
# Type: Running/Convergence (D5.1)
# Shows: Starting at 0, each term adds or subtracts. The waterfall
#        shape shows which terms build and which destroy. Final
#        value -0.328 is the tiny residual.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'Cumulative value of $A_2$')

terms = [
    ('197/144', +1.368, SILVER),
    (r'$(3/4)\zeta(3)$', +0.902, SILVER),
    (r'$(1/12)\pi^2$', +0.822, CYAN),
    (r'$-(1/2)\pi^2\ln 2$', -3.421, CYAN),
]

cumulative = [0]
for _, val, _ in terms:
    cumulative.append(cumulative[-1] + val)

x_pos = np.arange(len(terms))
for i, (label, val, color) in enumerate(terms):
    bottom = cumulative[i]
    height = val
    ax.bar(i, height, 0.7, bottom=bottom, color=color, alpha=0.6,
           edgecolor=color, linewidth=2)

    # Value label
    mid = bottom + height / 2
    ax.text(i, mid, '%+.3f' % val, color=WHITE, fontsize=11,
            ha='center', va='center', fontweight='bold')

    # Term label
    ax.text(i, bottom + height + (0.15 if val > 0 else -0.25),
            label, color=color, fontsize=9, ha='center',
            va='bottom' if val > 0 else 'top')

# Connecting lines
for i in range(len(terms) - 1):
    ax.plot([i + 0.35, i + 0.65], [cumulative[i + 1], cumulative[i + 1]],
            color=DIM, lw=1, ls='--', alpha=0.5)

# Final value line
ax.axhline(cumulative[-1], color=GOLD, lw=2, ls='--')
ax.text(len(terms) - 0.3, cumulative[-1] + 0.15,
        r'$A_2$ = %.3f' % cumulative[-1],
        color=GOLD, fontsize=14, fontweight='bold')

# Zero line
ax.axhline(0, color=DIM, lw=0.5, alpha=0.3)

# Layer annotations
ax.text(-0.6, 1.5, r'$\beta^0$' + '\n(Layer 1)', color=SILVER,
        fontsize=10, fontweight='bold')
ax.text(2.5, -2.0, r'$\beta^2$' + '\n(Modulus)', color=CYAN,
        fontsize=10, fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(['Term 1', 'Term 2', 'Term 3', 'Term 4'],
                    color=DIM, fontsize=9)
ax.set_xlim(-0.8, 4.5)
ax.set_ylim(-2.5, 3.5)

ax.set_title(r'$A_2$ Waterfall: $\beta^0$ Builds, $\beta^2$ Destroys, Residual = $-0.328$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_03_a2_waterfall.png')


# ================================================================
# FIG 4: SESSIONS 1-4 → SESSION 8 BRIDGE
# Type: Geometric Cross-Section (D5.4)
# Shows: Left: parked state (modulus known, remainder opaque).
#        Right: resolved state (modulus=spherical, remainder=L1+L2).
#        Arrow between showing the resolution.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Left panel: Sessions 1-4 (parked)
ax.text(0.15, 0.92, 'SESSIONS 1-4', color=DIM, fontsize=14,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.15, 0.87, 'PARKED', color=RED, fontsize=12,
        ha='center', transform=ax.transAxes, style='italic')

# Modulus box (known)
modulus_box = FancyBboxPatch((0.03, 0.55), 0.24, 0.25,
                              boxstyle='round,pad=0.02',
                              facecolor=CYAN, alpha=0.15,
                              edgecolor=CYAN, linewidth=2,
                              transform=ax.transAxes)
ax.add_patch(modulus_box)
ax.text(0.15, 0.73, 'MODULUS', color=CYAN, fontsize=13,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.15, 0.67, r'$R_2 = \pi/4 = \beta$', color=CYAN, fontsize=11,
        ha='center', transform=ax.transAxes)
ax.text(0.15, 0.62, '22+ domains', color=CYAN, fontsize=10,
        ha='center', transform=ax.transAxes)
ax.text(0.15, 0.57, 'UNDERSTOOD', color=GREEN, fontsize=10,
        ha='center', transform=ax.transAxes, fontweight='bold')

# Remainder box (opaque)
remainder_box = FancyBboxPatch((0.03, 0.20), 0.24, 0.25,
                                boxstyle='round,pad=0.02',
                                facecolor=DIM, alpha=0.15,
                                edgecolor=DIM, linewidth=2,
                                transform=ax.transAxes)
ax.add_patch(remainder_box)
ax.text(0.15, 0.38, 'REMAINDER', color=DIM, fontsize=13,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.15, 0.32, '197/144, ' + r'$\zeta(3)$' + ', Li' + r'$_4$' + '...',
        color=DIM, fontsize=10, ha='center', transform=ax.transAxes)
ax.text(0.15, 0.27, 'No geometric interpretation',
        color=DIM, fontsize=10, ha='center', transform=ax.transAxes)
ax.text(0.15, 0.22, 'OPAQUE', color=RED, fontsize=10,
        ha='center', transform=ax.transAxes, fontweight='bold')

# Arrow
ax.annotate('', xy=(0.55, 0.55), xytext=(0.35, 0.55),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=3),
            transform=ax.transAxes)
ax.text(0.45, 0.58, 'Laporta\nanalysis', color=GOLD, fontsize=11,
        ha='center', transform=ax.transAxes, fontweight='bold')

# Right panel: Session 8 (resolved)
ax.text(0.75, 0.92, 'SESSION 8', color=GOLD, fontsize=14,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.75, 0.87, 'RESOLVED', color=GREEN, fontsize=12,
        ha='center', transform=ax.transAxes, style='italic')

# Modulus = Spherical
sph_box = FancyBboxPatch((0.58, 0.65), 0.34, 0.18,
                           boxstyle='round,pad=0.02',
                           facecolor=CYAN, alpha=0.15,
                           edgecolor=CYAN, linewidth=2,
                           transform=ax.transAxes)
ax.add_patch(sph_box)
ax.text(0.75, 0.78, 'MODULUS = SPHERICAL', color=CYAN, fontsize=12,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.75, 0.73, r'$\beta^2, \beta^4$ from angular integrations',
        color=CYAN, fontsize=10, ha='center', transform=ax.transAxes)
ax.text(0.75, 0.68, 'Analytical, all loops', color=GREEN, fontsize=10,
        ha='center', transform=ax.transAxes)

# Layer 1 = Number-theoretic
l1_box = FancyBboxPatch((0.58, 0.40), 0.34, 0.18,
                          boxstyle='round,pad=0.02',
                          facecolor=SILVER, alpha=0.15,
                          edgecolor=SILVER, linewidth=2,
                          transform=ax.transAxes)
ax.add_patch(l1_box)
ax.text(0.75, 0.53, 'LAYER 1 = NUMBER THEORY', color=SILVER, fontsize=12,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.75, 0.48, r'Rational, $\zeta(n)$, Li$_n$, MZV',
        color=SILVER, fontsize=10, ha='center', transform=ax.transAxes)
ax.text(0.75, 0.43, 'Known, all loops', color=GREEN, fontsize=10,
        ha='center', transform=ax.transAxes)

# Layer 2 = Toroidal
l2_box = FancyBboxPatch((0.58, 0.15), 0.34, 0.18,
                          boxstyle='round,pad=0.02',
                          facecolor=GOLD, alpha=0.15,
                          edgecolor=GOLD, linewidth=2.5,
                          transform=ax.transAxes)
ax.add_patch(l2_box)
ax.text(0.75, 0.28, 'LAYER 2 = TOROIDAL', color=GOLD, fontsize=12,
        fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.75, 0.23, 'Laporta K(k), E(k)', color=GOLD, fontsize=10,
        ha='center', transform=ax.transAxes)
ax.text(0.75, 0.18, 'NEW — loop 4 only', color=RED, fontsize=10,
        ha='center', transform=ax.transAxes, fontweight='bold')

# Brace for "remainder"
ax.plot([0.55, 0.55], [0.17, 0.60], color=DIM, lw=1.5, ls='-',
        transform=ax.transAxes)
ax.text(0.53, 0.38, 'R\nE\nM\nA\nI\nN\nD\nE\nR', color=DIM,
        fontsize=7, ha='center', transform=ax.transAxes, linespacing=0.8)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('The Parked Framework Un-Parked: Sessions 1-4 to Session 8',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys49_04_framework_bridge.png')


# ================================================================
# FIG 5: A4 ON THE K(k)/pi CURVE
# Type: Running/Convergence (D5.1)
# Shows: K(k)/pi as a function of k. A4/(-13/8) marked as a
#        horizontal line. Intersection at k = 0.995.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Modulus $k$', r'$K(k) / \pi$')

from mpmath import mp, ellipk, pi as mpi, mpf
mp.dps = 30

k_vals = np.linspace(0.01, 0.999, 500)
kpi_vals = []
for k in k_vals:
    K_val = float(ellipk(mpf(str(k))**2))
    kpi_vals.append(K_val / float(mpi))

ax.plot(k_vals, kpi_vals, color=CYAN, lw=2.5, label=r'$K(k)/\pi$')

# A4 target line
a4_target = abs(-1.912) / (13.0/8.0)  # |A4| / (13/8) = what K/pi should equal
ax.axhline(a4_target, color=GOLD, lw=2, ls='--',
           label=r'$|A_4| / (13/8)$ = %.4f' % a4_target)

# Intersection
k_intersect = 0.995
ax.plot(k_intersect, a4_target, 'o', color=GOLD, markersize=14, zorder=6)
ax.annotate('k = 0.995\n' + r'$A_4 \approx -(13/8) \times K/\pi$',
            xy=(k_intersect, a4_target),
            xytext=(0.7, a4_target + 0.8),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Divergence annotation
ax.text(0.85, 3.5, r'$K(k) \to \infty$' + '\nas ' + r'$k \to 1$',
        color=RED, fontsize=11, style='italic')
ax.text(0.85, 2.8, 'Torus becomes\ninfinitely elongated',
        color=RED, fontsize=9, style='italic')

# The 13/8 annotation
ax.text(0.1, a4_target + 0.15,
        r'$13 = |b_2^\prime|$ numerator' + '\n' + r'$8 = 2\pi/\beta$',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, linewidth=1))

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper left')
ax.set_xlim(0, 1.01)
ax.set_ylim(0.4, 5)

ax.set_title(r'$A_4 \approx -(13/8) \times K(0.995)/\pi$: The Toroidal/Spherical Ratio',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_05_a4_on_kpi_curve.png')


# ================================================================
# FIG 6: K(k)/pi DIVERGENCE WITH A3 AND A4 MARKED
# Type: Threshold/Region (D5.3)
# Shows: K(k)/pi rising toward infinity near k=1.
#        A3 remainder at k=0.99 and A4 at k=0.995 both near the
#        divergence. The approach to the toroidal singularity.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'Modulus $k$', r'$K(k)/\pi$')

k_fine = np.linspace(0.9, 0.9999, 500)
kpi_fine = []
for k in k_fine:
    K_val = float(ellipk(mpf(str(k))**2))
    kpi_fine.append(K_val / float(mpi))

ax.plot(k_fine, kpi_fine, color=CYAN, lw=2.5)

# Shade the divergence region
ax.fill_between(k_fine, 0, kpi_fine, where=np.array(k_fine) > 0.995,
                color=RED, alpha=0.05)

# A3 remainder point
a3_k = 0.99
a3_kpi = float(ellipk(mpf(str(a3_k))**2)) / float(mpi)
a3_target = 23.015 / (20.0/3.0)
ax.plot(a3_k, a3_kpi, 'o', color=GREEN, markersize=12, zorder=6)
ax.annotate(r'$A_3$ remainder' + '\n' + r'$k = 0.99$' + '\nmiss: 1.8 ppm',
            xy=(a3_k, a3_kpi), xytext=(0.92, a3_kpi + 1.5),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# A4 point
a4_k = 0.995
a4_kpi = float(ellipk(mpf(str(a4_k))**2)) / float(mpi)
ax.plot(a4_k, a4_kpi, 'o', color=GOLD, markersize=12, zorder=6)
ax.annotate(r'$A_4$ total' + '\n' + r'$k = 0.995$' + '\nmiss: 12.5 ppm',
            xy=(a4_k, a4_kpi), xytext=(0.96, a4_kpi - 2),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Divergence label
ax.text(0.998, 8, r'$k \to 1$' + '\n' + r'$K \to \infty$',
        color=RED, fontsize=12, fontweight='bold')

# Annotation: approaching the toroidal singularity
ax.text(0.91, 1.5,
        'Both QED coefficients sit\nnear the elliptic divergence.\n'
        'The perturbation series is\napproaching the toroidal\nsingularity.',
        color=WHITE, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=WHITE, linewidth=1))

ax.set_xlim(0.9, 1.001)
ax.set_ylim(0.5, 10)

ax.set_title(r'Near the Divergence: $A_3$ at $k=0.99$, $A_4$ at $k=0.995$',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_06_kpi_divergence.png')


# ================================================================
# FIG 7: DUAL GEOMETRY AT FOUR SCALES
# Type: Scale/Landscape (D5.2)
# Shows: Proton, Earth, Galaxy, QED — each with modulus (spherical)
#        and remainder (toroidal) labeled with actual values.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

scales = [
    ('Proton', r'$10^{-15}$ m',
     r'Confinement: $C = 6\beta$', 'Flux tubes: 99% mass'),
    ('Earth', r'$10^{7}$ m',
     'Atmosphere: 7 shells', 'Van Allen: 2 belts'),
    ('Galaxy', r'$10^{21}$ m',
     r'Halo: $\Omega_{DM} = \beta/3$', r'Disk: DM/b = $\frac{22}{13} 4\beta$'),
    ('QED 4-loop', 'virtual',
     r'$\beta^2$: $\pi$ terms', r'$\beta^0$: Laporta'),
]

x_positions = [1, 4, 7, 10]

for i, (name, scale, mod_text, rem_text) in enumerate(scales):
    x = x_positions[i]

    # Object label
    ax.text(x, 5.5, name, color=WHITE, fontsize=14, fontweight='bold',
            ha='center')
    ax.text(x, 5.0, scale, color=DIM, fontsize=9, ha='center')

    # Sphere (modulus)
    circle = Circle((x - 0.5, 3.2), 0.6, facecolor=CYAN, alpha=0.12,
                      edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(circle)
    ax.text(x - 0.5, 2.2, mod_text, color=CYAN, fontsize=8,
            ha='center')
    ax.text(x - 0.5, 1.8, 'MODULUS', color=CYAN, fontsize=7,
            ha='center', fontweight='bold')

    # Torus (remainder)
    torus_outer = Ellipse((x + 0.5, 3.2), 1.3, 0.8, facecolor='none',
                            edgecolor=GOLD, linewidth=1.5)
    torus_inner = Ellipse((x + 0.5, 3.25), 0.4, 0.2, facecolor=PAN,
                            edgecolor=GOLD, linewidth=1, linestyle='--')
    ax.add_patch(torus_outer)
    ax.add_patch(torus_inner)
    ax.text(x + 0.5, 2.2, rem_text, color=GOLD, fontsize=8,
            ha='center')
    ax.text(x + 0.5, 1.8, 'REMAINDER', color=GOLD, fontsize=7,
            ha='center', fontweight='bold')

    # Equals sign
    ax.text(x, 3.2, '+', color=WHITE, fontsize=16, ha='center',
            va='center', fontweight='bold')

# Bottom summary
ax.text(5.5, 0.8,
        'At every scale: MODULUS = spherical (analytical, understood)'
        '     REMAINDER = toroidal (harder, deeper)',
        color=WHITE, fontsize=11, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2))

ax.set_xlim(-0.5, 12)
ax.set_ylim(0.3, 6.3)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('The Dual Geometry at Every Scale: Spherical Modulus + Toroidal Remainder',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys49_07_dual_geometry_scales.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE COMPLETE DECOMPOSITION
# Type: Identity Card (D5.8)
# Shows: A1 through A4 each decomposed into three layers with
#        numerical values. The un-parking resolution.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Title
ax.text(0.02, 0.95, 'THE COMPLETE DECOMPOSITION', color=GOLD,
        fontsize=18, fontweight='bold', transform=ax.transAxes)
ax.text(0.02, 0.91, 'Every QED coefficient = Spherical Modulus + '
        'Number-Theoretic Remainder + Toroidal Remainder',
        color=SILVER, fontsize=10, transform=ax.transAxes)

# Column headers
headers = [('Coeff', 0.02), ('Net', 0.10), ('Modulus', 0.22),
           ('Layer 1', 0.42), ('Layer 2', 0.62), ('Cancel', 0.82)]
y_head = 0.84
for text, hx in headers:
    ax.text(hx, y_head, text, color=DIM, fontsize=10, fontweight='bold',
            transform=ax.transAxes)

ax.plot([0.02, 0.95], [y_head - 0.015, y_head - 0.015],
        color=DIM, lw=0.5, transform=ax.transAxes, clip_on=False)

# Data rows
rows = [
    (r'$A_1$', '+0.500', '0', r'+$\frac{1}{2}$ (rational)', '0', '0%'),
    (r'$A_2$', r'$-$0.328', r'$-$2.598 ($\beta^2$)', r'+2.270 ($\zeta$+rat)', '0', '90.4%'),
    (r'$A_3$', '+1.181', r'$-$21.83 ($\beta^{2,4}$)', r'+23.02 ($\zeta$+Li)', '0', '99.5%'),
    (r'$A_4$', r'$-$1.912', '~' + r'$-$0.84 (est)', '~' + r'$-$1.07 ($\zeta$)', 'Laporta!', '?'),
]
row_colors = [DIM, CYAN, GREEN, GOLD]

y_start = 0.76
y_step = 0.12

for i, (coeff, net, mod, l1, l2, cancel) in enumerate(rows):
    y = y_start - i * y_step
    color = row_colors[i]

    ax.text(0.02, y, coeff, color=color, fontsize=14, fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.10, y, net, color=WHITE, fontsize=11, transform=ax.transAxes)
    ax.text(0.22, y, mod, color=CYAN, fontsize=10, transform=ax.transAxes)
    ax.text(0.42, y, l1, color=SILVER, fontsize=10, transform=ax.transAxes)

    l2_color = GOLD if l2 != '0' else DIM
    l2_weight = 'bold' if l2 != '0' else 'normal'
    ax.text(0.62, y, l2, color=l2_color, fontsize=10, fontweight=l2_weight,
            transform=ax.transAxes)
    ax.text(0.82, y, cancel, color=WHITE, fontsize=10, transform=ax.transAxes)

# The resolution box
y_box = 0.22
ax.text(0.02, y_box, 'THE RESOLUTION', color=GOLD, fontsize=14,
        fontweight='bold', transform=ax.transAxes)

resolution_lines = [
    ('Sessions 1-4:', 'Modulus (known) + Remainder (parked)'),
    ('Session 8:', 'Modulus (spherical) + Layer 1 (number theory) + Layer 2 (toroidal)'),
    ('Evidence:', 'Control ratio 2.05, subtraction 6/6, 24/24 PSLQ null'),
    ('Key number:', r'$A_4 \approx -(13/8) \times K(0.995)/\pi$'),
    ('Experiments:', '7 experiments, 316 outputs, 65 PASS'),
]
for j, (key, val) in enumerate(resolution_lines):
    y_line = y_box - (j + 1) * 0.04
    ax.text(0.04, y_line, key, color=SILVER, fontsize=10,
            transform=ax.transAxes)
    ax.text(0.25, y_line, val, color=WHITE, fontsize=10,
            transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

save(fig, 'phys49_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys49_01_three_layer_bars.png")
print("  phys49_02_subtraction_improvement.png")
print("  phys49_03_a2_waterfall.png")
print("  phys49_04_framework_bridge.png")
print("  phys49_05_a4_on_kpi_curve.png")
print("  phys49_06_kpi_divergence.png")
print("  phys49_07_dual_geometry_scales.png")
print("  phys49_08_identity_card.png")
print("=" * 50)
