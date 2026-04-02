#!/usr/bin/env python3
"""
HOWL COMPLETE VISUAL ATLAS — howl_atlas_diagrams.py
=====================================================
End-to-end visualization of the HOWL series:
  Fig 1: The Integer Chain — from Yang-Mills 11 to cosmology
  Fig 2: The Gap Ratio Correction Chain — 2.000 → 1.407 → 1.358
  Fig 3: The 19→13 Transformation — what the Cabibbo Doublet changes
  Fig 4: The Beta Unification — 7 cosmological predictions from particle physics
  Fig 5: The Two Roads — gap ratio path meets anomaly path at (3,2,1/6)
  Fig 6: The Energy Landscape — from m_e to M_GUT with boundaries
  Fig 7: The A₂ Cancellation — three pieces, 87% cancellation
  Fig 8: The Remainder Framework — 9 domains, 3 subgroups, R₂ universal
  Fig 9: The Proton Decay Discriminator — CD vs MSSM separated by 10^7
  Fig 10: The Level 1 / Level 2 Boundary Map

Platform: phys24_lib.py
Output: 10 PNGs to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np
import os

from phys24_lib import *
from mpmath import log10 as mlog10, log as mlog, pi as mpi, exp as mexp

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ================================================================
# GLOBAL STYLE
# ================================================================

DARK_BG = '#0a0a12'
PANEL_BG = '#12121f'
GOLD = '#d4a843'
SILVER = '#a0a8b8'
CYAN = '#4ecdc4'
MAGENTA = '#c74b7a'
BLUE = '#5b8def'
GREEN = '#6bcf7f'
RED = '#e05555'
ORANGE = '#e8944a'
WHITE = '#e8e8f0'
DIM = '#555570'
PURPLE = '#9b7bd4'

def setup_fig(figsize=(18, 11), title=""):
    fig = plt.figure(figsize=figsize, facecolor=DARK_BG)
    fig.suptitle(title, fontsize=18, fontweight='bold', color=GOLD, y=0.97)
    return fig

def setup_ax(fig, rect, title="", xlabel="", ylabel=""):
    ax = fig.add_axes(rect, facecolor=PANEL_BG)
    ax.set_title(title, fontsize=13, fontweight='bold', color=WHITE, pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=10, color=SILVER)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=10, color=SILVER)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    return ax

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=DARK_BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % path)

# ================================================================
# FIG 1: THE INTEGER CHAIN
# ================================================================

print("Fig 1: The Integer Chain")

fig = setup_fig((20, 13), "THE INTEGER CHAIN — From Yang-Mills to Cosmology")

ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Source: Yang-Mills 11
ax.add_patch(mpatches.FancyBboxPatch((2, 48), 18, 8, boxstyle="round,pad=0.5",
             facecolor='#1a1a2e', edgecolor=GOLD, linewidth=2.5))
ax.text(11, 52, '11', fontsize=28, fontweight='bold', color=GOLD,
        ha='center', va='center')
ax.text(11, 49.5, 'Yang-Mills', fontsize=9, color=SILVER, ha='center')

# Arrow from 11 to gauge self-coupling
ax.annotate('', xy=(24, 52), xytext=(20, 52),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# Gauge self-coupling box
ax.add_patch(mpatches.FancyBboxPatch((25, 47), 22, 10, boxstyle="round,pad=0.5",
             facecolor='#1a1a2e', edgecolor=CYAN, linewidth=1.5))
ax.text(36, 54, '−(11/3)C₂(G)', fontsize=12, fontweight='bold', color=CYAN,
        ha='center')
ax.text(36, 51, 'b₂_gauge = −22/3', fontsize=10, color=WHITE, ha='center')
ax.text(36, 48.5, 'b₃_gauge = −11', fontsize=10, color=WHITE, ha='center')

# Arrow down to SM betas
ax.annotate('', xy=(36, 43), xytext=(36, 47),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

# + fermions + Higgs box
ax.add_patch(mpatches.FancyBboxPatch((25, 35), 22, 8, boxstyle="round,pad=0.5",
             facecolor='#1a1a2e', edgecolor=BLUE, linewidth=1.5))
ax.text(36, 41, '+ 3 gen (4/3 each)', fontsize=10, color=GREEN, ha='center')
ax.text(36, 38.5, '+ Higgs (1/10, 1/6, 0)', fontsize=10, color=SILVER, ha='center')
ax.text(36, 36, 'SM betas: 41/10, −19/6, −7', fontsize=10, fontweight='bold',
        color=WHITE, ha='center')

# Branch right: SM integers
ax.annotate('', xy=(52, 38), xytext=(47, 38),
            arrowprops=dict(arrowstyle='->', color=MAGENTA, lw=1.5))

# 19 box
ax.add_patch(mpatches.FancyBboxPatch((53, 44), 12, 7, boxstyle="round,pad=0.4",
             facecolor='#2a1525', edgecolor=MAGENTA, linewidth=2))
ax.text(59, 49, '19', fontsize=22, fontweight='bold', color=MAGENTA, ha='center')
ax.text(59, 45.5, '|b₂_SM num|', fontsize=9, color=SILVER, ha='center')

# Arrow down: + Cabibbo Doublet
ax.annotate('', xy=(36, 31), xytext=(36, 35),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

# CD box
ax.add_patch(mpatches.FancyBboxPatch((25, 23), 22, 8, boxstyle="round,pad=0.5",
             facecolor='#152515', edgecolor=GREEN, linewidth=2))
ax.text(36, 29.5, '+ Cabibbo Doublet (3,2,1/6)', fontsize=10, fontweight='bold',
        color=GREEN, ha='center')
ax.text(36, 27, 'Δb = (1/15, 1, 1/3)', fontsize=10, color=WHITE, ha='center')
ax.text(36, 24.5, "b' = 25/6, −13/6, −20/3", fontsize=10, fontweight='bold',
        color=WHITE, ha='center')

# Branch right: VL integers
ax.annotate('', xy=(52, 26), xytext=(47, 26),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

# 13 box
ax.add_patch(mpatches.FancyBboxPatch((53, 32), 12, 7, boxstyle="round,pad=0.4",
             facecolor='#152530', edgecolor=CYAN, linewidth=2))
ax.text(59, 37, '13', fontsize=22, fontweight='bold', color=CYAN, ha='center')
ax.text(59, 33.5, '|b₂_mod num|', fontsize=9, color=SILVER, ha='center')

# 20 box
ax.add_patch(mpatches.FancyBboxPatch((53, 22), 12, 7, boxstyle="round,pad=0.4",
             facecolor='#152530', edgecolor=CYAN, linewidth=2))
ax.text(59, 27, '20', fontsize=22, fontweight='bold', color=CYAN, ha='center')
ax.text(59, 23.5, '|3·b₃_mod|', fontsize=9, color=SILVER, ha='center')

# 22 box (from 11)
ax.add_patch(mpatches.FancyBboxPatch((53, 12), 12, 7, boxstyle="round,pad=0.4",
             facecolor='#251525', edgecolor=GOLD, linewidth=2))
ax.text(59, 17, '22', fontsize=22, fontweight='bold', color=GOLD, ha='center')
ax.text(59, 13.5, '2 × YM', fontsize=9, color=SILVER, ha='center')

# Arrow from 11 down to 22
ax.annotate('', xy=(59, 19), xytext=(11, 48),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2,
                          connectionstyle='arc3,rad=0.3', linestyle='--'))

# Right side: cosmological predictions
right_x = 72

formulas = [
    (49, 'Λ ~ α^(3×19)', '10⁻¹²¹·⁸⁰', MAGENTA),
    (42, 'Λ ~ (α/3π)^(3×13)', '10⁻¹²¹·³³', CYAN),
    (35, 'DM/b = (22/13)π', '5.317 (0.07%)', GOLD),
    (28, '(1−r) = α²π²·20/13', '0.000809', CYAN),
    (21, 'Ω_b = 2/(13π)', '0.04897', CYAN),
    (14, 'H₀ = 73.04 × r¹⁰⁰', '67.364 (0.007%)', GREEN),
    (7, '57/39 = 19/13', 'EXACT', PURPLE),
]

for y, formula, result, color in formulas:
    ax.add_patch(mpatches.FancyBboxPatch((right_x, y-2), 26, 5.5,
                 boxstyle="round,pad=0.3", facecolor='#0f0f1a',
                 edgecolor=color, linewidth=1.2))
    ax.text(right_x + 1, y + 2, formula, fontsize=10, fontweight='bold',
            color=color, va='center')
    ax.text(right_x + 25, y + 2, result, fontsize=9, color=WHITE,
            va='center', ha='right')

# Arrows from integers to formulas
ax.annotate('', xy=(right_x, 51), xytext=(65, 48),
            arrowprops=dict(arrowstyle='->', color=MAGENTA, lw=1))
ax.annotate('', xy=(right_x, 44), xytext=(65, 38),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1))
ax.annotate('', xy=(right_x, 37), xytext=(65, 35),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1))
ax.annotate('', xy=(right_x, 30), xytext=(65, 27),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1))
ax.annotate('', xy=(right_x, 23), xytext=(65, 35),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1))

# Title annotations
ax.text(50, 56, 'PARTICLE PHYSICS', fontsize=11, color=DIM, ha='center',
        style='italic')
ax.text(85, 56, 'COSMOLOGY', fontsize=11, color=DIM, ha='center',
        style='italic')
ax.plot([68, 68], [5, 55], color=DIM, linewidth=0.5, linestyle=':')

# Bottom caption
ax.text(50, 2, 'Every integer traces to the gauge group through the beta coefficients.\n'
        'The Cabibbo Doublet transforms 19→13 and 21→20. These transformed integers\n'
        'appear in every cosmological formula.', fontsize=10, color=DIM,
        ha='center', va='center', style='italic')

save(fig, 'atlas_01_integer_chain.png')

# ================================================================
# FIG 2: THE GAP RATIO CORRECTION CHAIN
# ================================================================

print("Fig 2: The Gap Ratio Correction Chain")

fig = setup_fig((18, 10), "THE GAP RATIO CORRECTION CHAIN")
ax = fig.add_axes([0.08, 0.12, 0.86, 0.78], facecolor=PANEL_BG)

stages = [
    ('Pure Gauge\nC₂(SU2)/(C₂(SU3)−C₂(SU2))', 2.000, GOLD, 'Level 1\nCasimir ratio'),
    ('+ Higgs\n(1,2,1/2)', 1.896, BLUE, 'Level 1\n218/115'),
    ('+ Cabibbo Doublet\n(3,2,1/6)', 1.407, GREEN, 'Level 1\n38/27'),
    ('Measured\n(α, sin²θ_W, α_s)', 1.358, CYAN, 'Derived\nfrom DATA-4'),
]

x_pos = [0.5, 1.5, 2.5, 3.5]
bar_width = 0.6

for i, (label, val, color, note) in enumerate(stages):
    ax.bar(x_pos[i], val, bar_width, color=color, alpha=0.7, edgecolor=color,
           linewidth=2)
    ax.text(x_pos[i], val + 0.04, '%.3f' % val, fontsize=14, fontweight='bold',
            color=WHITE, ha='center')
    ax.text(x_pos[i], -0.15, label, fontsize=9, color=SILVER, ha='center',
            va='top', linespacing=1.4)
    ax.text(x_pos[i], val - 0.12, note, fontsize=8, color=DIM, ha='center',
            va='top', style='italic', linespacing=1.3)

# Arrows showing corrections
corrections = [
    (0.5, 1.5, 2.000, 1.896, '−0.104\n(Higgs: 16%)'),
    (1.5, 2.5, 1.896, 1.407, '−0.489\n(CD: 76%)'),
    (2.5, 3.5, 1.407, 1.358, '−0.049\n(remaining: 8%)'),
]

for x1, x2, y1, y2, text in corrections:
    mid_y = (y1 + y2) / 2 + 0.15
    ax.annotate('', xy=(x2 - 0.15, y2 + 0.03), xytext=(x1 + 0.15, y1 - 0.03),
                arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5,
                              connectionstyle='arc3,rad=-0.2'))
    ax.text((x1 + x2) / 2, mid_y, text, fontsize=9, color=WHITE,
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=DARK_BG, edgecolor=DIM))

# 40% miss line
ax.axhline(y=1.358, color=CYAN, linewidth=0.8, linestyle='--', alpha=0.5)
ax.text(4.1, 1.37, 'Measured = 1.358', fontsize=9, color=CYAN)

ax.set_xlim(-0.1, 4.3)
ax.set_ylim(-0.3, 2.3)
ax.set_ylabel('Gap Ratio', fontsize=12, color=SILVER)
ax.set_xticks([])

# Bottom note
ax.text(2, -0.25, 'The 40% miss (2.000→1.358) is corrected: 16% by the Higgs, '
        '76% by the Cabibbo Doublet, 8% remains (two-loop + thresholds)',
        fontsize=9, color=DIM, ha='center', style='italic')

save(fig, 'atlas_02_gap_ratio_chain.png')

# ================================================================
# FIG 3: THE 19→13 TRANSFORMATION
# ================================================================

print("Fig 3: The 19→13 Transformation")

fig = setup_fig((18, 11), "THE 19 → 13 TRANSFORMATION — One Particle Changes Everything")
ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Left: SM column (19)
ax.text(20, 56, 'STANDARD MODEL', fontsize=13, fontweight='bold', color=MAGENTA,
        ha='center')

sm_items = [
    (50, 'b₂ = −19/6', '|num| = 19'),
    (44, 'b₃ = −7 = −21/3', '|num×3| = 21'),
    (38, 'Λ exponent = 3×19', '= 57'),
    (32, 'Gap ratio = 218/115', '= 1.896'),
    (26, 'M_GUT = 10¹³·⁸', 'EXCLUDED'),
    (20, 'τ_p ~ 10³⁰ yr', 'EXCLUDED'),
]

for y, line1, line2 in sm_items:
    ax.add_patch(mpatches.FancyBboxPatch((4, y-2.5), 32, 5,
                 boxstyle="round,pad=0.3", facecolor='#1a0a15',
                 edgecolor=MAGENTA, linewidth=1, alpha=0.8))
    ax.text(20, y + 1, line1, fontsize=10, color=WHITE, ha='center')
    ax.text(20, y - 1.5, line2, fontsize=9, color=MAGENTA, ha='center',
            fontweight='bold')

# Center: The transformation arrow
ax.add_patch(mpatches.FancyBboxPatch((38, 34), 24, 14, boxstyle="round,pad=0.5",
             facecolor='#152515', edgecolor=GREEN, linewidth=2.5))
ax.text(50, 45, 'CABIBBO DOUBLET', fontsize=11, fontweight='bold', color=GREEN,
        ha='center')
ax.text(50, 42, '(3, 2, 1/6)', fontsize=10, color=WHITE, ha='center')
ax.text(50, 39, 'Δb₂ = +1', fontsize=12, fontweight='bold', color=GOLD,
        ha='center')
ax.text(50, 36.5, '19 − 6 = 13', fontsize=14, fontweight='bold', color=CYAN,
        ha='center')

# Right: VL column (13)
ax.text(80, 56, 'SM + CABIBBO DOUBLET', fontsize=13, fontweight='bold', color=CYAN,
        ha='center')

vl_items = [
    (50, 'b₂ = −13/6', '|num| = 13'),
    (44, 'b₃ = −20/3', '|num×3| = 20'),
    (38, 'Λ exponent = 3×13', '= 39'),
    (32, 'Gap ratio = 38/27', '= 1.407'),
    (26, 'M_GUT = 10¹⁵·⁵', 'VIABLE'),
    (20, 'τ_p ~ 10³⁴⁻³⁵ yr', 'HYPER-K'),
    (14, 'DM/b = (22/13)π', '5.317'),
    (8, 'H₀ = 73.04·r¹⁰⁰', '67.364'),
]

for y, line1, line2 in vl_items:
    ax.add_patch(mpatches.FancyBboxPatch((64, y-2.5), 32, 5,
                 boxstyle="round,pad=0.3", facecolor='#0a1520',
                 edgecolor=CYAN, linewidth=1, alpha=0.8))
    ax.text(80, y + 1, line1, fontsize=10, color=WHITE, ha='center')
    ax.text(80, y - 1.5, line2, fontsize=9, color=CYAN, ha='center',
            fontweight='bold')

# Arrows across
for y in [50, 44, 38, 32, 26, 20]:
    ax.annotate('', xy=(64, y), xytext=(36, y),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2,
                              connectionstyle='arc3,rad=0'))

# New items (cosmological) — highlight
for y in [14, 8]:
    ax.add_patch(mpatches.FancyBboxPatch((64, y-2.5), 32, 5,
                 boxstyle="round,pad=0.3", facecolor='#0a1520',
                 edgecolor=GOLD, linewidth=1.5, alpha=0.8))

ax.text(80, 15, 'Ω_b = 2/(13π)', fontsize=10, color=WHITE, ha='center')
ax.text(80, 12.5, '0.04897 (0.06%)', fontsize=9, color=GOLD, ha='center',
        fontweight='bold')
ax.text(80, 9, 'H₀(CMB) predicted', fontsize=10, color=WHITE, ha='center')
ax.text(80, 6.5, '67.364 (0.007%)', fontsize=9, color=GOLD, ha='center',
        fontweight='bold')

ax.text(50, 3, 'The integer 13 replaces 19 in every formula.\n'
        'New cosmological predictions emerge that did not exist in the SM.',
        fontsize=10, color=DIM, ha='center', style='italic')

save(fig, 'atlas_03_nineteen_to_thirteen.png')

# ================================================================
# FIG 4: THE BETA UNIFICATION — PREDICTION TABLE
# ================================================================

print("Fig 4: The Beta Unification Prediction Table")

fig = setup_fig((18, 12), "THE BETA UNIFICATION — 7 Cosmological Predictions from Particle Physics")
ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

# Input box
ax.add_patch(mpatches.FancyBboxPatch((2, 58), 30, 9, boxstyle="round,pad=0.5",
             facecolor='#1a1a2e', edgecolor=GOLD, linewidth=2))
ax.text(17, 65, 'INPUT (particle physics only)', fontsize=11, fontweight='bold',
        color=GOLD, ha='center')
ax.text(17, 62.5, 'α = 1/137.036', fontsize=10, color=WHITE, ha='center')
ax.text(17, 60, 'β integers: 13, 19, 20, 22', fontsize=10, color=WHITE, ha='center')

ax.add_patch(mpatches.FancyBboxPatch((35, 58), 20, 9, boxstyle="round,pad=0.5",
             facecolor='#1a1a2e', edgecolor=CYAN, linewidth=2))
ax.text(45, 65, 'GEOMETRY', fontsize=11, fontweight='bold', color=CYAN, ha='center')
ax.text(45, 62, 'R₂ = π/4', fontsize=10, color=WHITE, ha='center')
ax.text(45, 59.5, 'R₄ = π²/32', fontsize=10, color=WHITE, ha='center')

# Big "NO COSMOLOGICAL INPUT" banner
ax.add_patch(mpatches.FancyBboxPatch((58, 60), 38, 5, boxstyle="round,pad=0.3",
             facecolor=RED, edgecolor=RED, linewidth=0, alpha=0.15))
ax.text(77, 62.5, 'ZERO COSMOLOGICAL INPUT', fontsize=13, fontweight='bold',
        color=RED, ha='center')

# Arrow down
ax.annotate('', xy=(50, 55), xytext=(50, 58),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Prediction rows
predictions = [
    ('log₁₀(Λ_Pl)', '−121.57', '−121.54', '0.03 dec', '0.02%', 'α^57 & (α/3π)^39'),
    ('DM / baryon', '5.317', '5.320', '0.004', '0.07%', '(22/13)π'),
    ('H₀(CMB)', '67.364', '67.36', '0.004', '0.007%', '73.04 × r¹⁰⁰'),
    ('Ω_baryon', '0.04897', '0.0490', '0.0001', '0.06%', '2/(13π)'),
    ('Ω_DM', '0.2604', '0.2607', '0.0003', '0.13%', '44/169'),
    ('Ω_matter', '0.3093', '0.3097', '0.0004', '0.12%', 'Ω_b + Ω_DM'),
    ('Ω_DE', '0.6907', '0.6903', '0.0004', '0.05%', '1 − Ω_matter'),
]

# Header
y_start = 52
ax.text(5, y_start, 'Observable', fontsize=10, fontweight='bold', color=GOLD)
ax.text(25, y_start, 'Predicted', fontsize=10, fontweight='bold', color=GREEN)
ax.text(40, y_start, 'Measured', fontsize=10, fontweight='bold', color=CYAN)
ax.text(55, y_start, 'Miss', fontsize=10, fontweight='bold', color=SILVER)
ax.text(67, y_start, 'Rel %', fontsize=10, fontweight='bold', color=WHITE)
ax.text(80, y_start, 'Formula', fontsize=10, fontweight='bold', color=PURPLE)
ax.plot([3, 97], [y_start - 1.5, y_start - 1.5], color=DIM, linewidth=0.5)

for i, (obs, pred, meas, miss, rel, formula) in enumerate(predictions):
    y = y_start - 4 - i * 5.5
    # Color the miss by quality
    if float(rel.strip('%')) < 0.1:
        row_color = GREEN
    elif float(rel.strip('%')) < 0.5:
        row_color = CYAN
    else:
        row_color = BLUE

    ax.add_patch(mpatches.FancyBboxPatch((3, y - 2), 94, 4.5,
                 boxstyle="round,pad=0.2", facecolor=PANEL_BG,
                 edgecolor=row_color, linewidth=0.8, alpha=0.5))

    ax.text(5, y, obs, fontsize=11, color=WHITE, va='center', fontweight='bold')
    ax.text(25, y, pred, fontsize=11, color=GREEN, va='center',
            family='monospace')
    ax.text(40, y, meas, fontsize=11, color=CYAN, va='center',
            family='monospace')
    ax.text(55, y, miss, fontsize=10, color=SILVER, va='center',
            family='monospace')
    ax.text(67, y, rel, fontsize=11, color=row_color, va='center',
            fontweight='bold')
    ax.text(80, y, formula, fontsize=10, color=PURPLE, va='center')

# Bottom summary
ax.text(50, 6, '15/15 CHECKS PASS — All predictions within 1% of measured',
        fontsize=13, fontweight='bold', color=GOLD, ha='center')
ax.text(50, 3, 'Every integer traces to SU(3)×SU(2)×U(1) beta coefficients.\n'
        'The Cabibbo Doublet provides 13 and 20. Yang-Mills provides 22.',
        fontsize=10, color=DIM, ha='center', style='italic')

save(fig, 'atlas_04_beta_unification.png')

# ================================================================
# FIG 5: THE TWO ROADS
# ================================================================

print("Fig 5: The Two Roads")

fig = setup_fig((18, 11), "THE TWO ROADS — Independent Paths Converge on (3,2,1/6)")
ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# Left road: Gap Ratio
ax.text(25, 56, 'GAP RATIO PATH', fontsize=14, fontweight='bold', color=GOLD,
        ha='center')
ax.text(25, 53.5, '(top-down, 10¹⁵ GeV)', fontsize=10, color=DIM, ha='center')

gap_steps = [
    (48, 'Three couplings at M_Z', 'α, sin²θ_W, α_s'),
    (42, 'SM gap ratio = 218/115', '40% miss → SM fails'),
    (36, '15 candidates enumerated', 'Exact Fraction arithmetic'),
    (30, '12 eliminated (gap ratio)', '3 eliminated (proton decay)'),
    (24, 'Two survivors', 'MSSM (7/5) + CD (38/27)'),
]

for y, line1, line2 in gap_steps:
    ax.add_patch(mpatches.FancyBboxPatch((4, y-2.5), 42, 5,
                 boxstyle="round,pad=0.3", facecolor='#1a1510',
                 edgecolor=GOLD, linewidth=1))
    ax.text(25, y + 0.5, line1, fontsize=10, color=WHITE, ha='center')
    ax.text(25, y - 1.5, line2, fontsize=9, color=GOLD, ha='center')

# Right road: Anomaly
ax.text(75, 56, 'ANOMALY PATH', fontsize=14, fontweight='bold', color=CYAN,
        ha='center')
ax.text(75, 53.5, '(bottom-up, 10³ GeV)', fontsize=10, color=DIM, ha='center')

anom_steps = [
    (48, 'CKM deficit (2.5–4σ)', 'Needs SU(2) doublet'),
    (42, 'A_FB^b at LEP (~3σ)', 'Needs SU(3)×SU(2)'),
    (36, 'Higgs μ excess (~2σ)', 'Needs SU(3) triplet'),
    (30, 'Global fit (Cheung+ 2020)', 'VL doublet resolves all three'),
    (24, '8 papers, 4 groups', '2019–2024, independent'),
]

for y, line1, line2 in anom_steps:
    ax.add_patch(mpatches.FancyBboxPatch((54, y-2.5), 42, 5,
                 boxstyle="round,pad=0.3", facecolor='#101520',
                 edgecolor=CYAN, linewidth=1))
    ax.text(75, y + 0.5, line1, fontsize=10, color=WHITE, ha='center')
    ax.text(75, y - 1.5, line2, fontsize=9, color=CYAN, ha='center')

# Convergence arrows
ax.annotate('', xy=(50, 14), xytext=(25, 21),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.annotate('', xy=(50, 14), xytext=(75, 21),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))

# Central convergence box
ax.add_patch(mpatches.FancyBboxPatch((30, 5), 40, 10, boxstyle="round,pad=0.5",
             facecolor='#152515', edgecolor=GREEN, linewidth=3))
ax.text(50, 12.5, 'CABIBBO DOUBLET', fontsize=16, fontweight='bold',
        color=GREEN, ha='center')
ax.text(50, 9.5, '(3, 2, 1/6)', fontsize=14, color=WHITE, ha='center')
ax.text(50, 7, 'Same representation from independent data, methods, communities',
        fontsize=9, color=SILVER, ha='center', style='italic')

# What each path provides
ax.text(25, 17, 'Provides: representation\n+ M_GUT + proton decay',
        fontsize=9, color=GOLD, ha='center', style='italic')
ax.text(75, 17, 'Provides: mass window\n+ mixing angles + anomaly resolution',
        fontsize=9, color=CYAN, ha='center', style='italic')

save(fig, 'atlas_05_two_roads.png')

# ================================================================
# FIG 6: THE ENERGY LANDSCAPE
# ================================================================

print("Fig 6: The Energy Landscape")

fig = setup_fig((20, 10), "THE ENERGY LANDSCAPE — From Electron Mass to Grand Unification")
ax = fig.add_axes([0.08, 0.15, 0.88, 0.75], facecolor=PANEL_BG)

# Energy scale (log10 GeV)
log_scales = np.linspace(-4, 18, 1000)

# Inverse couplings (schematic one-loop running)
b1 = float(f2m(b1_SM))
b2 = float(f2m(b2_SM))
b3 = float(f2m(b3_SM))

inv_a1_val = float(f2m(inv_a1))
inv_a2_val = float(f2m(inv_a2))
inv_a3_val = float(f2m(inv_a3))

log_MZ = np.log10(91.2)
L = (log_scales - log_MZ) * np.log(10) / (2 * np.pi)

inv_a1_run = inv_a1_val - b1 * L
inv_a2_run = inv_a2_val - b2 * L
inv_a3_run = inv_a3_val - b3 * L

ax.plot(log_scales, inv_a1_run, color=BLUE, linewidth=2, label='1/α₁ (U(1))')
ax.plot(log_scales, inv_a2_run, color=GREEN, linewidth=2, label='1/α₂ (SU(2))')
ax.plot(log_scales, inv_a3_run, color=RED, linewidth=2, label='1/α₃ (SU(3))')

# Modified running (after CD threshold at ~3 TeV = 10^3.5 GeV)
b1_m = float(f2m(b1_mod))
b2_m = float(f2m(b2_mod))
b3_m = float(f2m(b3_mod))

mask = log_scales > 3.5
L_from_VL = (log_scales[mask] - 3.5) * np.log(10) / (2 * np.pi)

# Values at M_VL
inv_a1_at_VL = inv_a1_val - b1 * (3.5 - log_MZ) * np.log(10) / (2 * np.pi)
inv_a2_at_VL = inv_a2_val - b2 * (3.5 - log_MZ) * np.log(10) / (2 * np.pi)
inv_a3_at_VL = inv_a3_val - b3 * (3.5 - log_MZ) * np.log(10) / (2 * np.pi)

inv_a1_mod = inv_a1_at_VL - b1_m * L_from_VL
inv_a2_mod = inv_a2_at_VL - b2_m * L_from_VL
inv_a3_mod = inv_a3_at_VL - b3_m * L_from_VL

ax.plot(log_scales[mask], inv_a1_mod, color=BLUE, linewidth=2, linestyle='--', alpha=0.7)
ax.plot(log_scales[mask], inv_a2_mod, color=GREEN, linewidth=2, linestyle='--', alpha=0.7)
ax.plot(log_scales[mask], inv_a3_mod, color=RED, linewidth=2, linestyle='--', alpha=0.7)

# Key thresholds
thresholds = [
    (np.log10(0.0005), 'm_e', SILVER),
    (np.log10(0.106), 'm_μ', SILVER),
    (np.log10(1.78), 'm_τ', SILVER),
    (np.log10(91.2), 'M_Z', CYAN),
    (np.log10(172.6), 'm_t', BLUE),
    (3.5, 'M_VL\n(CD)', GREEN),
    (15.5, 'M_GUT', GOLD),
]

for log_e, label, color in thresholds:
    ax.axvline(x=log_e, color=color, linewidth=0.8, linestyle=':', alpha=0.5)
    ax.text(log_e, 67, label, fontsize=8, color=color, ha='center', va='bottom',
            rotation=0)

# Confinement wall
ax.axvspan(np.log10(0.3), np.log10(2), color=RED, alpha=0.08)
ax.text(np.log10(0.8), 5, 'CONFINEMENT\nWALL', fontsize=8, color=RED,
        ha='center', alpha=0.6, fontweight='bold')

# Labels
ax.set_xlabel('log₁₀(Energy / GeV)', fontsize=12, color=SILVER)
ax.set_ylabel('Inverse coupling 1/αᵢ', fontsize=12, color=SILVER)
ax.set_xlim(-4, 18)
ax.set_ylim(0, 70)
ax.legend(fontsize=10, loc='upper left', facecolor=PANEL_BG, edgecolor=DIM,
          labelcolor=WHITE)

# Annotations
ax.annotate('SM running\n(solid lines)', xy=(8, 30), fontsize=9, color=DIM,
            ha='center', style='italic')
ax.annotate('CD modified\n(dashed lines)', xy=(10, 50), fontsize=9, color=DIM,
            ha='center', style='italic')

save(fig, 'atlas_06_energy_landscape.png')

# ================================================================
# FIG 7: THE A₂ CANCELLATION
# ================================================================

print("Fig 7: The A₂ Cancellation")

fig = setup_fig((16, 10), "THE A₂ CANCELLATION — Three Pieces, 87% Cancellation")
ax = fig.add_axes([0.12, 0.12, 0.82, 0.78], facecolor=PANEL_BG)

pieces = [
    ('Rational\n197/144', 1.368, GOLD),
    ('Number-\ntheoretic\n(3/4)ζ(3)', 0.902, PURPLE),
    ('Geometric\nR₄(8/3−16ln2)', -2.598, CYAN),
    ('Net A₂', -0.329, GREEN),
]

x = [0, 1, 2, 3.5]
for i, (label, val, color) in enumerate(pieces):
    ax.bar(x[i], val, 0.7, color=color, alpha=0.7, edgecolor=color, linewidth=2)
    if val > 0:
        ax.text(x[i], val + 0.07, '+%.3f' % val, fontsize=12, fontweight='bold',
                color=WHITE, ha='center')
    else:
        ax.text(x[i], val - 0.15, '%.3f' % val, fontsize=12, fontweight='bold',
                color=WHITE, ha='center')
    ax.text(x[i], -0.5 if val >= 0 else 0.1, label, fontsize=9, color=SILVER,
            ha='center', va='top' if val >= 0 else 'bottom', linespacing=1.3)

# Cancellation annotation
ax.annotate('87% cancellation', xy=(2.7, -1.3), xytext=(3.5, 1.5),
            fontsize=12, fontweight='bold', color=RED,
            arrowprops=dict(arrowstyle='->', color=RED, lw=2),
            ha='center')

# Positive total line
ax.axhline(y=1.368 + 0.902, color=GOLD, linewidth=1, linestyle='--', alpha=0.5)
ax.text(3.8, 2.35, '+2.270', fontsize=10, color=GOLD)

ax.axhline(y=0, color=DIM, linewidth=0.5)
ax.set_xlim(-0.5, 4.3)
ax.set_ylim(-3.0, 2.8)
ax.set_ylabel('Value', fontsize=12, color=SILVER)
ax.set_xticks([])

ax.text(1.75, -2.8, 'A₂ is small (−0.329) because three large pieces nearly cancel.\n'
        'The geometric piece (7.9× the net) is from 4D phase space (R₄).\n'
        'The smallness is accidental — no known symmetry requires the 87% cancellation.',
        fontsize=9, color=DIM, ha='center', style='italic')

save(fig, 'atlas_07_a2_cancellation.png')

# ================================================================
# FIG 8: THE REMAINDER FRAMEWORK
# ================================================================

print("Fig 8: The Remainder Framework")

fig = setup_fig((18, 11), "THE REMAINDER FRAMEWORK — 9 Domains, 3 Subgroups, R₂ Universal")
ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

# R₂ central
ax.add_patch(mpatches.Circle((50, 38), 8, facecolor='#1a1a30',
             edgecolor=GOLD, linewidth=3))
ax.text(50, 40, 'R₂ = π/4', fontsize=14, fontweight='bold', color=GOLD,
        ha='center')
ax.text(50, 36, 'UNIVERSAL', fontsize=10, color=SILVER, ha='center')

# Subgroup A: periodic (7 domains)
a_domains = [
    'θ vacuum\n(8R₂)', 'Bohr-\nSommerfeld', 'Berry\nphase',
    'Brillouin\nzone', 'Aharonov-\nBohm', 'Flux\nquantization', 'AC\nJosephson'
]

for i, name in enumerate(a_domains):
    angle = np.pi/2 + i * 2 * np.pi / 7
    cx = 50 + 22 * np.cos(angle)
    cy = 38 + 18 * np.sin(angle)
    ax.add_patch(mpatches.FancyBboxPatch((cx-7, cy-3), 14, 6,
                 boxstyle="round,pad=0.3", facecolor='#151525',
                 edgecolor=BLUE, linewidth=1))
    ax.text(cx, cy, name, fontsize=7.5, color=WHITE, ha='center', va='center',
            linespacing=1.1)
    # Line to center
    ax.plot([50 + 8 * np.cos(angle), cx], [38 + 8 * np.sin(angle), cy],
            color=BLUE, linewidth=0.8, alpha=0.5)

ax.text(12, 56, 'SUBGROUP A (periodic, 7 domains)', fontsize=11,
        fontweight='bold', color=BLUE)
ax.text(12, 53, 'Modulus: 2π = 8R₂', fontsize=10, color=SILVER)

# Subgroup B: RG running
ax.add_patch(mpatches.FancyBboxPatch((78, 48), 18, 8, boxstyle="round,pad=0.5",
             facecolor='#152015', edgecolor=GREEN, linewidth=1.5))
ax.text(87, 54, 'RG Running', fontsize=10, fontweight='bold', color=GREEN,
        ha='center')
ax.text(87, 51, 'VP step\n1/(12R₂)', fontsize=9, color=WHITE, ha='center',
        linespacing=1.2)
ax.text(87, 48.5, 'SUBGROUP B', fontsize=8, color=GREEN, ha='center')
ax.plot([58, 78], [38, 52], color=GREEN, linewidth=0.8, alpha=0.5)

# Subgroup C: topological
ax.add_patch(mpatches.FancyBboxPatch((78, 22), 18, 8, boxstyle="round,pad=0.5",
             facecolor='#201520', edgecolor=MAGENTA, linewidth=1.5))
ax.text(87, 28, 'Chern-\nSimons', fontsize=10, fontweight='bold', color=MAGENTA,
        ha='center', linespacing=1.2)
ax.text(87, 24, 'R₄ = π²/32', fontsize=9, color=WHITE, ha='center')
ax.text(87, 22.5, 'SUBGROUP C', fontsize=8, color=MAGENTA, ha='center')
ax.plot([58, 78], [38, 26], color=MAGENTA, linewidth=0.8, alpha=0.5)

# PSLQ null
ax.add_patch(mpatches.FancyBboxPatch((2, 2), 96, 7, boxstyle="round,pad=0.3",
             facecolor='#1a0a0a', edgecolor=RED, linewidth=1))
ax.text(50, 7, '82/82 PSLQ NULL — No SM parameter is a simple combination '
        'of the Q335 transcendental basis', fontsize=10, color=RED, ha='center')
ax.text(50, 3.5, 'Composite soliton boundaries produce transcendentals outside '
        'any single class. Derivation beats search.',
        fontsize=9, color=DIM, ha='center', style='italic')

save(fig, 'atlas_08_remainder_framework.png')

# ================================================================
# FIG 9: THE PROTON DECAY DISCRIMINATOR
# ================================================================

print("Fig 9: The Proton Decay Discriminator")

fig = setup_fig((18, 10), "THE PROTON DECAY DISCRIMINATOR — CD vs MSSM: 10⁷ Separation")
ax = fig.add_axes([0.10, 0.15, 0.85, 0.75], facecolor=PANEL_BG)

scenarios = {
    'SM\n(excluded)': (13.8, 30, RED, 'τ ~ 10³⁰'),
    'CD\n(testable)': (15.5, 34.5, GREEN, 'τ ~ 10³⁴⁻³⁵'),
    'MSSM\n(unreachable)': (17.3, 37, BLUE, 'τ ~ 10³⁷'),
}

for name, (log_mgut, log_tau, color, tau_label) in scenarios.items():
    ax.scatter(log_mgut, log_tau, s=300, color=color, zorder=5, edgecolors=WHITE,
               linewidth=1.5)
    ax.text(log_mgut, log_tau + 0.8, name, fontsize=10, color=color,
            ha='center', fontweight='bold', linespacing=1.3)
    ax.text(log_mgut, log_tau - 0.8, tau_label, fontsize=9, color=SILVER,
            ha='center')

# M_GUT^4 scaling line
mgut_range = np.linspace(13, 18, 100)
# tau ~ M_GUT^4, calibrated to CD point
tau_range = 34.5 + 4 * (mgut_range - 15.5)
ax.plot(mgut_range, tau_range, color=GOLD, linewidth=1.5, linestyle='--',
        label='τ ∝ M_GUT⁴', alpha=0.7)

# Experimental bounds
ax.axhspan(34.38, 35, color=GREEN, alpha=0.1)
ax.axhline(y=34.38, color=CYAN, linewidth=1.5, linestyle='-',
           label='Super-K bound (2.4×10³⁴ yr)')
ax.text(18, 34.5, 'Super-K\nbound', fontsize=8, color=CYAN, ha='right')

ax.axhline(y=35, color=GREEN, linewidth=1.5, linestyle='-.',
           label='Hyper-K 20yr sensitivity (~10³⁵ yr)')
ax.text(18, 35.15, 'Hyper-K\n20yr', fontsize=8, color=GREEN, ha='right')

# The 10^7 gap annotation
ax.annotate('', xy=(17.3, 37), xytext=(15.5, 34.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(16.6, 36.2, '10⁷\nseparation', fontsize=12, fontweight='bold',
        color=GOLD, ha='center', linespacing=1.3)

ax.set_xlabel('log₁₀(M_GUT / GeV)', fontsize=12, color=SILVER)
ax.set_ylabel('log₁₀(τ_proton / yr)', fontsize=12, color=SILVER)
ax.set_xlim(13, 18.5)
ax.set_ylim(29, 39)
ax.legend(fontsize=9, loc='lower right', facecolor=PANEL_BG, edgecolor=DIM,
          labelcolor=WHITE)

ax.text(15.8, 29.5, 'Gap ratios differ by 0.007 (38/27 vs 7/5). '
        'Lifetimes differ by 10⁷. M_GUT⁴ scaling amplifies tiny differences.',
        fontsize=9, color=DIM, style='italic')

save(fig, 'atlas_09_proton_decay.png')

# ================================================================
# FIG 10: THE LEVEL 1 / LEVEL 2 BOUNDARY MAP
# ================================================================

print("Fig 10: The Level 1 / Level 2 Boundary Map")

fig = setup_fig((20, 13), "THE LEVEL 1 / LEVEL 2 BOUNDARY MAP")
ax = fig.add_axes([0.02, 0.03, 0.96, 0.88], facecolor=DARK_BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

# Title banner
ax.text(50, 66, 'The integers tell you WHAT.  The universe tells you HOW MUCH.',
        fontsize=14, fontweight='bold', color=GOLD, ha='center', style='italic')

# Level 1 column
ax.add_patch(mpatches.FancyBboxPatch((2, 8), 30, 54, boxstyle="round,pad=0.5",
             facecolor='#12121f', edgecolor=CYAN, linewidth=2))
ax.text(17, 60, 'LEVEL 1', fontsize=14, fontweight='bold', color=CYAN, ha='center')
ax.text(17, 57, '(framework-determined)', fontsize=9, color=DIM, ha='center')

l1_items = [
    'b₁=41/10, b₂=−19/6, b₃=−7',
    'Gap ratio 218/115',
    'Democracy (4/3, 4/3, 4/3)',
    'CD: (3,2,1/6), Δb=(1/15,1,1/3)',
    'Gap 38/27, asymmetry 15',
    'τ ∝ M_GUT⁴',
    'A₂ = 197/144+(3/4)ζ(3)+R₄c',
    '87% cancellation',
    'R₂ = π/4,  R₄ = π²/32',
    'Koide tautology + saddle',
    '82/82 PSLQ null',
]

for i, item in enumerate(l1_items):
    y = 53 - i * 4
    ax.text(17, y, item, fontsize=9, color=CYAN, ha='center')

# Level 2 column
ax.add_patch(mpatches.FancyBboxPatch((68, 8), 30, 54, boxstyle="round,pad=0.5",
             facecolor='#1f1212', edgecolor=MAGENTA, linewidth=2))
ax.text(83, 60, 'LEVEL 2', fontsize=14, fontweight='bold', color=MAGENTA, ha='center')
ax.text(83, 57, '(universe-supplied)', fontsize=9, color=DIM, ha='center')

l2_items = [
    'α⁻¹ = 137.036 (12 digits)',
    'sin²θ_W = 0.23122 (5 digits)',
    'α_s = 0.1180 (4 digits)',
    'CKM deficit = 0.00202',
    'A_FB^b = 0.0992 (LEP)',
    'Higgs μ ~ 1.06–1.10',
    'CD mass: 1.5–6 TeV',
    '|V_ub\'| ≈ 0.045',
    'K(leptons) = 0.666661',
    'a²(leptons) = 1.99996',
    'CD existence: ???',
]

for i, item in enumerate(l2_items):
    y = 53 - i * 4
    ax.text(83, y, item, fontsize=9, color=MAGENTA, ha='center')

# Derived column (center)
ax.add_patch(mpatches.FancyBboxPatch((35, 20), 30, 40, boxstyle="round,pad=0.5",
             facecolor='#151520', edgecolor=GOLD, linewidth=2))
ax.text(50, 58, 'DERIVED', fontsize=14, fontweight='bold', color=GOLD, ha='center')
ax.text(50, 55, '(L1 applied to L2)', fontsize=9, color=DIM, ha='center')

derived_items = [
    'Measured gap = 1.358',
    'M_GUT = 10¹⁵·⁵ GeV',
    'τ_p ~ 10³⁴⁻³⁵ yr',
    'Δ(two-loop) = −0.40',
    'a_e from α (4.3 ppb)',
    '11 EW observables',
    'CKM deficit = 0.002',
]

for i, item in enumerate(derived_items):
    y = 51 - i * 4
    ax.text(50, y, item, fontsize=9, color=GOLD, ha='center')

# Arrows
ax.annotate('', xy=(35, 40), xytext=(32, 40),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
ax.annotate('', xy=(65, 40), xytext=(68, 40),
            arrowprops=dict(arrowstyle='->', color=MAGENTA, lw=1.5))
ax.text(33.5, 42, 'structure', fontsize=8, color=CYAN, ha='center')
ax.text(66.5, 42, 'values', fontsize=8, color=MAGENTA, ha='center')

# Bottom: the confrontation
ax.add_patch(mpatches.FancyBboxPatch((15, 2), 70, 5, boxstyle="round,pad=0.3",
             facecolor='#1a1a10', edgecolor=GOLD, linewidth=1.5))
ax.text(50, 4.5, 'THE CONFRONTATION:  218/115 vs 1.358  →  40% miss  →  '
        'SM does not unify  →  Cabibbo Doublet',
        fontsize=10, fontweight='bold', color=WHITE, ha='center')

# Beta Unification extension (proposed)
ax.add_patch(mpatches.FancyBboxPatch((35, 8), 30, 10, boxstyle="round,pad=0.3",
             facecolor='#10150a', edgecolor=GREEN, linewidth=1, linestyle='--'))
ax.text(50, 16, 'PROPOSED EXTENSION', fontsize=9, fontweight='bold',
        color=GREEN, ha='center')
ax.text(50, 13, 'Beta integers → Λ, DM, H₀, Ω', fontsize=9, color=GREEN,
        ha='center')
ax.text(50, 10, '15/15 pass, all within 1%', fontsize=9, color=DIM,
        ha='center', style='italic')

save(fig, 'atlas_10_level_boundary.png')

# ================================================================
# DONE
# ================================================================

print()
print("=" * 70)
print("HOWL COMPLETE VISUAL ATLAS — 10 FIGURES GENERATED")
print("=" * 70)
print()
print("  Fig 1:  atlas_01_integer_chain.png")
print("  Fig 2:  atlas_02_gap_ratio_chain.png")
print("  Fig 3:  atlas_03_nineteen_to_thirteen.png")
print("  Fig 4:  atlas_04_beta_unification.png")
print("  Fig 5:  atlas_05_two_roads.png")
print("  Fig 6:  atlas_06_energy_landscape.png")
print("  Fig 7:  atlas_07_a2_cancellation.png")
print("  Fig 8:  atlas_08_remainder_framework.png")
print("  Fig 9:  atlas_09_proton_decay.png")
print("  Fig 10: atlas_10_level_boundary.png")
print()
print("  All output to ../figures/")
