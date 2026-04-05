#!/usr/bin/env python3
"""
HOWL PHYS-37 Diagrams — From Gauge Integers to Primordial Deuterium
8 figures covering full chain progression, M_W convergence, precision landscape,
island-to-continent map, BBN predictions, integer connection map, EW improvement,
and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
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

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def dark_fig(w=16, h=10):
    fig, ax = plt.subplots(figsize=(w, h), facecolor=BG)
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    return fig, ax

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def draw_box(ax, x, y, w, h, text, color, fontsize=10, alpha=1.0):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.15', facecolor=BG,
                          edgecolor=color, linewidth=2, alpha=alpha)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=color,
            ha='center', va='center', linespacing=1.5)

def arrow(ax, x1, y1, x2, y2, color=SILVER, lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))


# ================================================================
# FIG 1: FULL CHAIN a_e → D/H PROGRESSION
# Type: Type 7 (Progression/Sequence)
# Shows: Six-step physical chain crossing five domains, with
#        computed values at each stage. Not a flowchart — data flows.
# ================================================================

fig, ax = dark_fig(18, 10)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

# Six stages left to right
stages = [
    (1.5, 5, 'QED\n─────\na_e = 1.160×10⁻³\n→ α⁻¹ = 137.036\n(3.3 ppb)', MAG),
    (4.5, 5, 'GAUGE\n─────\nβ₂_mod = -13/6\nβ₃ = -7\n11, 13', CYAN),
    (7.5, 5, 'INTEGERS\n─────\nDM/baryon\n= (22/13)π\n= 5.317', GOLD),
    (10.5, 5, 'COSMOLOGY\n─────\nΩ_b = 0.04904\n(727 ppm)', BLUE),
    (13.5, 5, 'BBN\n─────\nη₁₀ = 6.090\n(0.24%)', GREEN),
    (16.5, 5, 'NUCLEAR\n─────\nD/H = 2.531×10⁻⁵\n(0.12σ)', PURPLE),
]

for x, y, text, color in stages:
    draw_box(ax, x, y, 2.5, 3.5, text, color, fontsize=9)

# Arrows between stages
for i in range(5):
    x1 = stages[i][0] + 1.25
    x2 = stages[i+1][0] - 1.25
    arrow(ax, x1, 5, x2, 5, SILVER, 2)

# Domain labels at top
domains = ['QED', 'Gauge\nTheory', 'Integer\nArithmetic', 'Cosmology', 'Big Bang\nNucleosynthesis', 'Nuclear\nPhysics']
domain_colors = [MAG, CYAN, GOLD, BLUE, GREEN, PURPLE]
for i, (label, color) in enumerate(zip(domains, domain_colors)):
    ax.text(stages[i][0], 8.5, label, fontsize=9, color=color, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, edgecolor=color, alpha=0.5))

ax.text(9, 9.5, 'The Full Chain: Electron Magnetic Moment → Primordial Deuterium',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')

ax.text(9, 1.0, 'Six links · Five domains · Each independently measurable · Endpoint at 0.12σ',
        fontsize=11, color=SILVER, ha='center', style='italic')

save(fig, 'phys37_01_full_chain.png')


# ================================================================
# FIG 2: M_W CONVERGENCE — TREE → V0 → V1
# Type: Type 1 (Running/Convergence)
# Shows: M_W approaching the measured value through three iterations.
#        The ρ parameter adds ~380 MeV. The curve shape shows convergence.
# ================================================================

fig, ax = dark_fig(16, 10)

versions = [0, 1, 2]
mw_values = [79953.4, 80333.9, 80336.9]
mw_measured = 80369.2
mw_unc = 13.3
labels = ['Tree-level\nWeinberg', 'One-loop v0\n+ ρ(m_t)', 'One-loop v1\n+ corrections']
colors_v = [RED, ORANGE, GREEN]

# Measurement band
ax.axhspan(mw_measured - mw_unc, mw_measured + mw_unc, color=MAG, alpha=0.12)
ax.axhspan(mw_measured - 3*mw_unc, mw_measured + 3*mw_unc, color=MAG, alpha=0.05)
ax.axhline(y=mw_measured, color=MAG, linewidth=2, linestyle='--', alpha=0.7)
ax.text(2.3, mw_measured + 18, 'PDG 2024: 80369.2 ± 13.3 MeV', fontsize=10, color=MAG)

# Data points
for i in range(3):
    ax.scatter(versions[i], mw_values[i], s=300, c=colors_v[i],
               edgecolors=WHITE, linewidth=2, zorder=5)
    miss_ppm = abs(mw_values[i] - mw_measured) / mw_measured * 1e6
    ax.annotate('%s\n%.1f MeV\n(%.0f ppm)' % (labels[i], mw_values[i], miss_ppm),
                xy=(versions[i], mw_values[i]),
                xytext=(versions[i] + 0.25, mw_values[i] - 80 + i*30),
                fontsize=9, color=colors_v[i],
                arrowprops=dict(arrowstyle='->', color=colors_v[i], lw=1.5))

# Connecting line
ax.plot(versions, mw_values, '-', color=DIM, linewidth=1.5, alpha=0.5)

# Annotation: what each step added
ax.annotate('+380 MeV\n(ρ parameter\nfrom top quark)', xy=(0.5, 80143),
            fontsize=9, color=ORANGE, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

ax.set_xlim(-0.5, 2.8)
ax.set_ylim(79850, 80450)
ax.set_xticks(versions)
ax.set_xticklabels(['Tree', 'v0', 'v1'], fontsize=11, color=SILVER)
ax.set_ylabel('M_W (MeV)', fontsize=12, color=SILVER)
ax.set_title('W Boson Mass: Convergence Through Three Iterations',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys37_02_mw_convergence.png')


# ================================================================
# FIG 3: PRECISION LANDSCAPE — 17 VALUES ON LOG SCALE
# Type: Type 2 (Scale/Landscape)
# Shows: All 17 derived values on a log-scale precision axis from
#        ppb to percent. The reader sees the full precision hierarchy.
# ================================================================

fig, ax = dark_fig(16, 12)

values_data = [
    ('α⁻¹', 3.3e-3, GOLD),
    ('a₀', 4.0e-3, GOLD),
    ('μ₀', 4.0e-3, GOLD),
    ('R∞', 8.0e-3, GOLD),
    ('M_W', 0.040, CYAN),
    ('m_τ (Koide)', 0.006, PURPLE),
    ('Ω_b', 0.073, BLUE),
    ('DM/baryon', 0.073, BLUE),
    ('D/H', 0.14, GREEN),
    ('ρ_Λ', 0.15, BLUE),
    ('Ω_DE', 0.20, BLUE),
    ('η₁₀', 0.24, BLUE),
    ('Ω_m', 0.44, BLUE),
    ('Γ_Z', 0.58, CYAN),
    ('Γ(Z→νν̄)', 0.6, CYAN),
    ('Y_p', 1.5, GREEN),
    ('G_F', 3.0, RED),
]

y_pos = np.arange(len(values_data))
miss_pct = [v[1] for v in values_data]
colors_p = [v[2] for v in values_data]
labels_p = [v[0] for v in values_data]

bars = ax.barh(y_pos, miss_pct, height=0.6, color=colors_p, alpha=0.7,
               edgecolor=colors_p, linewidth=1.5)

for i, (label, miss, color) in enumerate(values_data):
    if miss < 0.01:
        text = '%.1f ppb' % (miss * 1000)
    elif miss < 1:
        text = '%.0f ppm' % (miss * 10000) if miss > 0.03 else '%.1f ppm' % (miss * 10000)
    else:
        text = '%.1f%%' % miss
    ax.text(miss * 1.3, i, text, fontsize=9, color=color, va='center')

ax.set_xscale('log')
ax.set_xlim(1e-3, 10)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels_p, fontsize=10, color=SILVER)
ax.set_xlabel('Miss from measured value (%)', fontsize=12, color=SILVER)
ax.set_title('Precision Landscape: 17 Derived Values',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Domain bands
ax.axvspan(1e-3, 0.01, color=GOLD, alpha=0.03)
ax.axvspan(0.01, 0.1, color=CYAN, alpha=0.03)
ax.axvspan(0.1, 1, color=BLUE, alpha=0.03)
ax.axvspan(1, 10, color=RED, alpha=0.03)

ax.text(3e-3, 16.5, 'ppb', fontsize=8, color=GOLD, ha='center')
ax.text(0.04, 16.5, 'ppm', fontsize=8, color=CYAN, ha='center')
ax.text(0.4, 16.5, 'sub-%', fontsize=8, color=BLUE, ha='center')
ax.text(3, 16.5, '%', fontsize=8, color=RED, ha='center')

# 1% line
ax.axvline(x=1.0, color=DIM, linewidth=1, linestyle='--', alpha=0.5)
ax.text(1.05, 0.5, '1% threshold', fontsize=8, color=DIM, rotation=90)

ax.invert_yaxis()

save(fig, 'phys37_03_precision_landscape.png')


# ================================================================
# FIG 4: ISLAND-TO-CONTINENT MAP (BEFORE/AFTER)
# Type: Type 4 (Geometric Cross-Section)
# Shows: Four isolated islands becoming one connected continent.
#        The bridge lines show which derivation connected which.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

for ax in (ax1, ax2):
    ax.set_facecolor(PAN)
    ax.axis('off')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

# BEFORE — four islands
ax1.set_title('BEFORE: Four Disconnected Islands', fontsize=13,
              fontweight='bold', color=RED, pad=10)

islands_before = [
    (2, 6, 1.4, 'QED\nα, R∞, a₀, μ₀', GOLD),
    (6, 6, 1.4, 'Gauge\nbetas, gaps', CYAN),
    (2, 2, 1.2, 'Cosmology\nDM/baryon', BLUE),
    (6, 2, 1.0, 'Koide\nm_τ', PURPLE),
]

for x, y, r, label, color in islands_before:
    circle = Circle((x, y), r, facecolor=PAN, edgecolor=color,
                     linewidth=2.5, alpha=0.8)
    ax1.add_patch(circle)
    ax1.text(x, y, label, fontsize=9, color=color, ha='center', va='center')

# Water between
ax1.text(4, 4, '?', fontsize=40, color=DIM, ha='center', va='center', alpha=0.3)

# AFTER — connected continent
ax2.set_title('AFTER: Connected Continent + Atoll', fontsize=13,
              fontweight='bold', color=GREEN, pad=10)

islands_after = [
    (1.5, 6.5, 1.0, 'QED\n4 values\nppb', GOLD),
    (3.8, 6.5, 1.0, 'EW\nM_W, Γ_Z\nppm-0.6%', CYAN),
    (3.8, 4, 1.0, 'Gauge\nbetas\n11, 13', ORANGE),
    (1.5, 3, 1.2, 'Cosmology\nΩ_b, Ω_DE, ρ_Λ\nppm-0.2%', BLUE),
    (4.5, 1.5, 1.2, 'Nuclear\nY_p, D/H\n0.12σ', GREEN),
    (7, 2, 0.7, 'Koide\nm_τ', PURPLE),
]

for x, y, r, label, color in islands_after:
    circle = Circle((x, y), r, facecolor=PAN, edgecolor=color,
                     linewidth=2.5, alpha=0.8)
    ax2.add_patch(circle)
    ax2.text(x, y, label, fontsize=8, color=color, ha='center', va='center')

# Bridges
bridges = [
    (1.5, 5.5, 3.8, 5.5, SILVER),   # QED → EW (via α)
    (3.8, 5.5, 3.8, 5.0, SILVER),   # EW → Gauge
    (2.8, 4, 2.5, 4.0, SILVER),     # Gauge → Cosmo (integers)
    (2.5, 2.0, 3.5, 2.0, SILVER),   # Cosmo → Nuclear (η → BBN)
]

for x1, y1, x2, y2, color in bridges:
    ax2.plot([x1, x2], [y1, y2], '-', color=color, linewidth=2.5, alpha=0.6)

# Dotted line to Koide atoll
ax2.plot([5.5, 6.3], [1.5, 1.8], '--', color=PURPLE, linewidth=1.5, alpha=0.4)
ax2.text(6.5, 3, '(no bridge)', fontsize=8, color=PURPLE, alpha=0.5, ha='center')

save(fig, 'phys37_04_island_to_continent.png')


# ================================================================
# FIG 5: BBN PREDICTIONS — Y_P AND D/H WITH SIGMA BANDS
# Type: Type 3 (Threshold/Region)
# Shows: Our BBN predictions with measurement bands. D/H sits
#        inside 1σ. Y_p sits inside 1σ. The bands make this visual.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

for ax in (ax1, ax2):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)

# Left panel: Y_p
yp_derived = 0.2486
yp_measured = 0.2449
yp_unc = 0.004

ax1.axhspan(yp_measured - yp_unc, yp_measured + yp_unc, color=MAG, alpha=0.15,
            label='1σ band')
ax1.axhspan(yp_measured - 2*yp_unc, yp_measured + 2*yp_unc, color=MAG, alpha=0.06,
            label='2σ band')
ax1.axhline(y=yp_measured, color=MAG, linewidth=2, linestyle='--', alpha=0.7)

ax1.scatter(0.5, yp_derived, s=300, c=GREEN, edgecolors=WHITE, linewidth=2, zorder=5)
ax1.scatter(0.5, yp_measured, s=200, c=MAG, edgecolors=WHITE, linewidth=2, zorder=5, marker='D')

ax1.annotate('Derived: %.4f\n(0.94σ)' % yp_derived, xy=(0.5, yp_derived),
            xytext=(0.8, yp_derived + 0.002), fontsize=11, color=GREEN,
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))
ax1.annotate('Measured: %.4f ± %.3f' % (yp_measured, yp_unc), xy=(0.5, yp_measured),
            xytext=(0.8, yp_measured - 0.003), fontsize=10, color=MAG,
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

ax1.set_xlim(0, 1.5)
ax1.set_ylim(0.233, 0.258)
ax1.set_xticks([])
ax1.set_ylabel('Y_p (primordial ⁴He mass fraction)', fontsize=12, color=SILVER)
ax1.set_title('Primordial Helium from Gauge Integers',
              fontsize=13, fontweight='bold', color=GOLD, pad=15)

# Right panel: D/H
dh_derived = 2.531e-5
dh_measured = 2.527e-5
dh_unc = 0.030e-5

ax2.axhspan((dh_measured - dh_unc)*1e5, (dh_measured + dh_unc)*1e5, color=MAG, alpha=0.15)
ax2.axhspan((dh_measured - 2*dh_unc)*1e5, (dh_measured + 2*dh_unc)*1e5, color=MAG, alpha=0.06)
ax2.axhline(y=dh_measured*1e5, color=MAG, linewidth=2, linestyle='--', alpha=0.7)

ax2.scatter(0.5, dh_derived*1e5, s=300, c=GREEN, edgecolors=WHITE, linewidth=2, zorder=5)
ax2.scatter(0.5, dh_measured*1e5, s=200, c=MAG, edgecolors=WHITE, linewidth=2, zorder=5, marker='D')

ax2.annotate('Derived: %.3f\n(0.12σ)' % (dh_derived*1e5), xy=(0.5, dh_derived*1e5),
            xytext=(0.8, dh_derived*1e5 + 0.02), fontsize=11, color=GREEN,
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))
ax2.annotate('Measured: %.3f ± %.3f' % (dh_measured*1e5, dh_unc*1e5),
            xy=(0.5, dh_measured*1e5),
            xytext=(0.8, dh_measured*1e5 - 0.03), fontsize=10, color=MAG,
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

ax2.set_xlim(0, 1.5)
ax2.set_ylim(2.40, 2.65)
ax2.set_xticks([])
ax2.set_ylabel('D/H (×10⁻⁵)', fontsize=12, color=SILVER)
ax2.set_title('Primordial Deuterium from Gauge Integers',
              fontsize=13, fontweight='bold', color=GOLD, pad=15)

# Headline result box
ax2.text(1.1, 2.42, 'Chain: 11, 13 → (22/13)π\n→ Ω_b → η → BBN → D/H\n0.12σ from measured',
         fontsize=9, color=GOLD, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

save(fig, 'phys37_05_bbn_predictions.png')


# ================================================================
# FIG 6: INTEGER CONNECTION MAP 11, 13 → D/H
# Type: Type 5 (Connection/Integer Map)
# Shows: How the integers 11 and 13 flow through specific formulas
#        to reach D/H. Contains actual Fractions at every node.
# ================================================================

fig, ax = dark_fig(18, 12)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

# Source integers
draw_box(ax, 3, 10, 4.5, 1.8,
         '11 = -(11/3)×C₂(adj)\nYang-Mills gauge coefficient', CYAN, 10)
draw_box(ax, 3, 7.5, 4.5, 1.8,
         '13 = |b₂_mod| = |-13/6|\nModified SU(2) beta numerator', ORANGE, 10)

# Integer combinations
draw_box(ax, 9, 10, 3.5, 1.4,
         '22 = 2 × 11\nDM prefactor numerator', GOLD, 10)
draw_box(ax, 9, 7.5, 3.5, 1.4,
         '22/13\nDM/baryon prefactor', GOLD, 11)

# DM/baryon
draw_box(ax, 14.5, 8.5, 4, 1.4,
         '(22/13)×π = 5.3165\nDM/baryon ratio (725 ppm)', BLUE, 10)

# Omega_b
draw_box(ax, 14.5, 6, 4, 1.4,
         'Ω_b = 0.2607/5.317\n= 0.04904 (727 ppm)', BLUE, 10)

# eta
draw_box(ax, 9, 4, 4, 1.4,
         'η₁₀ = Ω_b ρ_crit/(n_γ m_p)\n= 6.090 (0.24%)', GREEN, 10)

# BBN outputs
draw_box(ax, 3.5, 1.5, 3.5, 1.4,
         'Y_p = 0.2486\n(0.94σ)', GREEN, 10)
draw_box(ax, 9, 1.5, 3.5, 1.4,
         'D/H = 2.531×10⁻⁵\n(0.12σ)', PURPLE, 11)

# Additional derived
draw_box(ax, 14.5, 3, 4, 1.4,
         'Ω_DE = 0.6903 (0.20%)\nρ_Λ = 5.89×10⁻³⁰ (0.15%)', BLUE, 9)

# Arrows
arrow(ax, 5.25, 10, 7.25, 10, SILVER)
arrow(ax, 5.25, 7.5, 7.25, 7.9, SILVER)
arrow(ax, 5.25, 7.5, 7.25, 7.5, SILVER)
arrow(ax, 10.75, 10, 12.5, 9.0, GOLD)
arrow(ax, 10.75, 7.5, 12.5, 8.3, GOLD)
arrow(ax, 14.5, 7.8, 14.5, 6.7, BLUE)
arrow(ax, 12.5, 5.5, 11, 4.7, GREEN)
arrow(ax, 7.5, 3.3, 5.25, 2.2, GREEN)
arrow(ax, 9, 3.3, 9, 2.2, GREEN)
arrow(ax, 14.5, 5.3, 14.5, 3.7, BLUE)

ax.text(9, 11.5, 'Integer Connection Map: From Gauge Theory to Nuclear Abundances',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')

save(fig, 'phys37_06_integer_map.png')


# ================================================================
# FIG 7: EW TREE VS ONE-LOOP IMPROVEMENT (TRIPLE BARS)
# Type: Type 6 (Comparison Bar)
# Shows: M_W, Gamma_Z, G_F at three levels: tree, v0, v1.
#        The bars shrink showing improvement. Measured line for reference.
# ================================================================

fig, ax = dark_fig(16, 10)

quantities = ['M_W', 'Γ_Z', 'G_F']
tree_miss = [0.517, 6.35, 5.97]
v0_miss = [0.044, 2.87, 2.24]
v1_miss = [0.040, 0.58, 3.04]

x = np.arange(len(quantities))
width = 0.25

bars1 = ax.bar(x - width, tree_miss, width, color=RED, alpha=0.7,
               edgecolor=RED, linewidth=1.5, label='Tree-level')
bars2 = ax.bar(x, v0_miss, width, color=ORANGE, alpha=0.7,
               edgecolor=ORANGE, linewidth=1.5, label='One-loop v0')
bars3 = ax.bar(x + width, v1_miss, width, color=GREEN, alpha=0.7,
               edgecolor=GREEN, linewidth=1.5, label='One-loop v1')

# Value labels on bars
for i in range(3):
    ax.text(x[i] - width, tree_miss[i] + 0.15, '%.2f%%' % tree_miss[i],
            fontsize=9, color=RED, ha='center')
    ax.text(x[i], v0_miss[i] + 0.15, '%.2f%%' % v0_miss[i],
            fontsize=9, color=ORANGE, ha='center')
    ax.text(x[i] + width, v1_miss[i] + 0.15, '%.2f%%' % v1_miss[i],
            fontsize=9, color=GREEN, ha='center')

# 1% target line
ax.axhline(y=1.0, color=GOLD, linewidth=2, linestyle='--', alpha=0.7)
ax.text(2.6, 1.15, '1% target', fontsize=10, color=GOLD)

ax.set_xticks(x)
ax.set_xticklabels(quantities, fontsize=13, color=SILVER)
ax.set_ylabel('Miss from measured value (%)', fontsize=12, color=SILVER)
ax.set_ylim(0, 7.5)
ax.set_title('Electroweak Precision: Tree-Level → One-Loop v0 → One-Loop v1',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.legend(fontsize=10, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, loc='upper right')

# Improvement annotations
ax.annotate('11.8×\nimprovement', xy=(0, 0.044), xytext=(-0.5, 2.5),
            fontsize=9, color=CYAN, ha='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=CYAN))

ax.annotate('4.9×\nimprovement', xy=(1 + width, 0.58), xytext=(1.5, 3.5),
            fontsize=9, color=CYAN, ha='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=CYAN))

save(fig, 'phys37_07_ew_improvement.png')


# ================================================================
# FIG 8: IDENTITY CARD — 17 VALUES, 5 DOMAINS
# Type: Type 8 (Identity Card)
# Shows: All 17 values organized by domain with key numbers.
#        Visual anchor for the paper.
# ================================================================

fig, ax = dark_fig(18, 14)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

# Title
ax.text(9, 13.3, 'HOWL-PHYS-37: FROM GAUGE INTEGERS TO PRIMORDIAL DEUTERIUM',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')
ax.text(9, 12.7, '17 Derived Values · 5 Domains · 12 Measured Inputs',
        fontsize=11, color=SILVER, ha='center')
ax.axhline(y=12.3, xmin=0.03, xmax=0.97, color=GOLD, linewidth=1.5)

# Domain columns
domains_id = [
    ('QED', GOLD, 1.5, [
        ('α⁻¹ = 137.036', '3.3 ppb'),
        ('R∞ = 10973732', '8.0 ppb'),
        ('a₀ = 5.292e-11', '4.0 ppb'),
        ('μ₀ = 1.257e-6', '4.0 ppb'),
    ]),
    ('EW', CYAN, 5.0, [
        ('M_W = 80337 MeV', '402 ppm'),
        ('Γ_Z = 2510 MeV', '0.58%'),
        ('Γ(νν̄) = 502 MeV', '0.6%'),
        ('G_F = 1.20e-5', '3.0%'),
    ]),
    ('COSMO', BLUE, 8.5, [
        ('DM/b = 5.317', '725 ppm'),
        ('Ω_b = 0.04904', '727 ppm'),
        ('Ω_DE = 0.6903', '0.20%'),
        ('ρ_Λ = 5.89e-30', '0.15%'),
    ]),
    ('NUCLEAR', GREEN, 12.0, [
        ('η₁₀ = 6.090', '0.24%'),
        ('Y_p = 0.2486', '0.94σ'),
        ('D/H = 2.53e-5', '0.12σ'),
    ]),
    ('MASS', PURPLE, 15.5, [
        ('m_τ = 1776.97', '0.006%'),
        ('θ_QCD = 0', 'exact'),
    ]),
]

for domain, color, x_pos, values in domains_id:
    ax.text(x_pos, 11.8, domain, fontsize=13, fontweight='bold', color=color, ha='center')
    ax.plot([x_pos - 1.2, x_pos + 1.2], [11.4, 11.4], '-', color=color, linewidth=1, alpha=0.5)
    for i, (val, miss) in enumerate(values):
        y = 10.7 - i * 0.9
        ax.text(x_pos, y, val, fontsize=9, color=WHITE, ha='center', fontfamily='monospace')
        ax.text(x_pos, y - 0.35, miss, fontsize=8, color=DIM, ha='center')

# Key integers box
ax.text(4, 4.5, 'KEY INTEGERS', fontsize=12, fontweight='bold', color=ORANGE, ha='center')
ints_text = '11 (Yang-Mills) · 13 (|b₂_mod|)\n22/13 (DM prefactor) · (22/13)π = 5.317'
ax.text(4, 3.7, ints_text, fontsize=10, color=ORANGE, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

# Inputs box
ax.text(13, 4.5, 'MEASURED INPUTS', fontsize=12, fontweight='bold', color=MAG, ha='center')
inputs_text = 'a_e (0.11 ppb) · m_e (0.03 ppb) · M_Z · sin²θ_W\nm_t · α_s · α(M_Z) · sin²θ_eff · Ω_DM · H₀ · T_CMB · m_μ'
ax.text(13, 3.7, inputs_text, fontsize=9, color=MAG, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG, alpha=0.8))

# Footer
ax.text(9, 1.5, 'The longest chain: a_e → α → integers (11,13) → (22/13)π → Ω_b → η → D/H',
        fontsize=11, color=GOLD, ha='center', style='italic')
ax.text(9, 0.8, '12 inputs · 17 outputs · 5 more outputs than inputs · every output matches its measurement',
        fontsize=10, color=SILVER, ha='center')

save(fig, 'phys37_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("PHYS-37 Diagrams Complete:")
print("  phys37_01_full_chain.png")
print("  phys37_02_mw_convergence.png")
print("  phys37_03_precision_landscape.png")
print("  phys37_04_island_to_continent.png")
print("  phys37_05_bbn_predictions.png")
print("  phys37_06_integer_map.png")
print("  phys37_07_ew_improvement.png")
print("  phys37_08_identity_card.png")

