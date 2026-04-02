#!/usr/bin/env python3
"""
HOWL Session 4 Complete Diagram Atlas — howl_session4_atlas.py
===============================================================
Visualizes every major finding from PHYS-25 through PHYS-29.
10 figures covering the full research program.

Output: PNG files to ./figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(outdir, exist_ok=True)

# Global style
BG = '#0a0a12'
PAN = '#12121f'
GOLD = '#d4a843'
SILVER = '#a0a8b8'
CYAN = '#4ecdc4'
MAG = '#c74b7a'
BLUE = '#5b8def'
GREEN = '#6bcf7f'
RED = '#e05555'
ORANGE = '#e8944a'
WHITE = '#e8e8f0'
DIM = '#555570'
PURPLE = '#9b7bd4'

def sfig(size=(18, 11), title=""):
    fig = plt.figure(figsize=size, facecolor=BG)
    if title:
        fig.suptitle(title, fontsize=17, fontweight='bold', color=GOLD, y=0.97)
    return fig

def sax(fig, rect):
    ax = fig.add_axes(rect, facecolor=BG)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    return ax

def save(fig, name):
    p = os.path.join(outdir, name)
    fig.savefig(p, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % p)

def box(ax, x, y, w, h, text, color, fontsize=10, subtext=None, subtextcolor=None):
    ax.add_patch(mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4",
                 facecolor='#0f0f1a', edgecolor=color, linewidth=1.5))
    ax.text(x + w/2, y + h/2 + (1.2 if subtext else 0), text,
            fontsize=fontsize, fontweight='bold', color=color, ha='center', va='center')
    if subtext:
        ax.text(x + w/2, y + h/2 - 1.5, subtext, fontsize=8,
                color=subtextcolor or SILVER, ha='center', va='center')

def arrow(ax, x1, y1, x2, y2, color=SILVER, lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# ================================================================
# FIG 1: THE COMPLETE RESEARCH PROGRAM
# ================================================================
print("Fig 1: Research Program Map")

fig = sfig((20, 13), "THE RESEARCH PROGRAM — PHYS-25 through PHYS-40")
ax = sax(fig, [0.02, 0.03, 0.96, 0.88])

# PHYS-25 at top
box(ax, 35, 52, 30, 6, 'PHYS-25: Operational Map', GOLD, 12,
    '47/47 — the direction is set')

# Three tracks
# Track A
ax.text(15, 47, 'TRACK A: Unification', fontsize=12, fontweight='bold',
        color=CYAN, ha='center')
track_a = [
    (2, 38, 'PHYS-26', 'Normalization', '20/20 ALL EXACT', GREEN),
    (2, 30, 'PHYS-27', 'sin²θ_W from 3/8', '13/13  miss=1.2%', CYAN),
    (2, 22, 'PHYS-28', 'VL Two-Loop b_ij', '11/11  +4.6%', CYAN),
    (2, 14, 'PHYS-29', 'GUT Thresholds', '10/11  ABORT FIRES', RED),
    (2, 6, 'PHYS-30', 'α_s Prediction', 'NEXT', DIM),
]
for x, y, num, title, status, color in track_a:
    box(ax, x, y, 26, 6, '%s: %s' % (num, title), color, 9, status)

# Arrows
for i in range(len(track_a) - 1):
    arrow(ax, 15, track_a[i][1], 15, track_a[i+1][1] + 6, CYAN)

# Track B
ax.text(52, 47, 'TRACK B: Cosmology', fontsize=12, fontweight='bold',
        color=GREEN, ha='center')
track_b = [
    (38, 38, 'PHYS-31', 'Statistical Control', 'GATE — next', ORANGE),
    (38, 30, 'PHYS-32', 'Set B Omegas', 'gated', DIM),
    (38, 22, 'PHYS-33', 'Λ Interpolation', 'gated', DIM),
    (38, 14, 'PHYS-34', 'Per-Transit Mechanism', 'gated', DIM),
    (38, 6, 'PHYS-35', 'Boundary Count', 'gated', DIM),
]
for x, y, num, title, status, color in track_b:
    box(ax, x, y, 26, 6, '%s: %s' % (num, title), color, 9, status)

for i in range(len(track_b) - 1):
    arrow(ax, 51, track_b[i][1], 51, track_b[i+1][1] + 6, GREEN)

# Track C
ax.text(85, 47, 'TRACK C: Structure', fontsize=12, fontweight='bold',
        color=PURPLE, ha='center')
track_c = [
    (72, 38, 'PHYS-36', 'A₃ Decomposition', 'independent', DIM),
    (72, 30, 'PHYS-37', 'Koide Amplitude', 'independent', DIM),
    (72, 22, 'PHYS-38', 'Loop Expansion', 'independent', DIM),
    (72, 14, 'PHYS-39', 'Ω Remainder Domain', 'independent', DIM),
    (72, 6, 'PHYS-40', 'sin²θ_W = 3/13 Test', 'needs PHYS-27,28', DIM),
]
for x, y, num, title, status, color in track_c:
    box(ax, x, y, 26, 6, '%s: %s' % (num, title), color, 9, status)

# From PHYS-25 down to tracks
arrow(ax, 42, 52, 15, 44, CYAN, 2)
arrow(ax, 50, 52, 51, 44, GREEN, 2)
arrow(ax, 58, 52, 85, 44, PURPLE, 2)

# Gate indicator on PHYS-31
ax.text(65, 40, 'GATE', fontsize=14, fontweight='bold', color=RED,
        ha='center', rotation=0,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a0a0a', edgecolor=RED))
arrow(ax, 64, 39, 64, 36, RED, 2)
ax.text(66, 36, 'p<0.05?\nTrack B\nparked', fontsize=7, color=RED, ha='center')

save(fig, 'session4_01_program_map.png')

# ================================================================
# FIG 2: THE DELTA IMPROVEMENT CHAIN
# ================================================================
print("Fig 2: Delta Improvement Chain")

fig = sfig((16, 10), "THE UNIFICATION MISS — From SM to Threshold")
ax = fig.add_axes([0.12, 0.15, 0.82, 0.75], facecolor=PAN)

stages = ['SM\n(no CD)', 'CD\none-loop', 'CD\ntwo-loop\n(SM b_ij)', 'CD\ntwo-loop\n(+VL b_ij)',
          'GUT\nthreshold\n(best case)']
deltas = [6.58, 1.17, 0.40, 0.436, 0.0]
colors = [RED, ORANGE, CYAN, GREEN, GOLD]
x = [0, 1, 2, 3, 4.3]

for i in range(len(stages)):
    ax.bar(x[i], deltas[i], 0.65, color=colors[i], alpha=0.7,
           edgecolor=colors[i], linewidth=2)
    ax.text(x[i], deltas[i] + 0.15, '%.2f' % deltas[i] if deltas[i] > 0 else '0.00',
            fontsize=13, fontweight='bold', color=WHITE, ha='center')
    ax.text(x[i], -0.6, stages[i], fontsize=8, color=SILVER, ha='center',
            va='top', linespacing=1.2)

# Improvement arrows
improvements = [
    (0, 1, '82%'),
    (1, 2, '66%'),
    (2, 3, '+4.6%'),
]
for i1, i2, text in improvements:
    mid_y = (deltas[i1] + deltas[i2]) / 2 + 0.3
    ax.annotate(text, xy=((x[i1]+x[i2])/2, mid_y), fontsize=10,
                color=WHITE, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=DIM))

# Red X on threshold
ax.text(4.3, 3.5, 'M_X/M = 23,228\nFINE-TUNED', fontsize=10,
        color=RED, ha='center', fontweight='bold')
ax.plot([3.95, 4.65], [2.8, 3.2], color=RED, linewidth=3)
ax.plot([3.95, 4.65], [3.2, 2.8], color=RED, linewidth=3)

ax.set_ylabel('|Delta(1/α₃)| (dimensionless)', fontsize=11, color=SILVER)
ax.set_xlim(-0.5, 5.2)
ax.set_ylim(-1.0, 7.5)
ax.set_xticks([])
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, 'session4_02_delta_chain.png')

# ================================================================
# FIG 3: THE sin²θ_W CONVERGENCE
# ================================================================
print("Fig 3: sin²θ_W Convergence")

fig = sfig((16, 10), "sin²θ_W — From 3/8 to 3/13")
ax = fig.add_axes([0.12, 0.15, 0.82, 0.75], facecolor=PAN)

labels = ['Tree\n(3/8)', 'Threshold\nM_VL=500', 'No thresh\n(best 1L)', '2-loop\nestimate',
          '3/13', 'Measured']
values = [0.375, 0.22722, 0.22845, 0.23028, 0.23077, 0.23122]
colors_s = [DIM, ORANGE, CYAN, GREEN, GOLD, MAG]
x = np.arange(len(labels))

ax.barh(x, values, 0.6, color=[c for c in colors_s], alpha=0.7,
        edgecolor=[c for c in colors_s], linewidth=1.5)

for i in range(len(labels)):
    ax.text(values[i] + 0.003, x[i], '%.5f' % values[i], fontsize=10,
            color=WHITE, va='center', fontweight='bold')

ax.set_yticks(x)
ax.set_yticklabels(labels, fontsize=9, color=SILVER)
ax.set_xlabel('sin²θ_W (dimensionless)', fontsize=11, color=SILVER)
ax.set_xlim(0.20, 0.40)

# Highlight the 3/13 region
ax.axvline(x=0.23077, color=GOLD, linewidth=1, linestyle='--', alpha=0.5)
ax.axvline(x=0.23122, color=MAG, linewidth=1, linestyle='--', alpha=0.5)

ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.text(0.35, 5.5, '3/8 = 0.375\n(tree level)', fontsize=9, color=DIM,
        ha='center', style='italic')

save(fig, 'session4_03_sin2tw_convergence.png')

# ================================================================
# FIG 4: THE VL TWO-LOOP b_ij MATRIX HEATMAP
# ================================================================
print("Fig 4: VL b_ij Heatmap")

fig = sfig((14, 10), "THE VL TWO-LOOP b_ij MATRIX — Magnitudes and Ratios")

# SM matrix
sm = np.array([[3.98, 2.7, 8.8],
               [0.9, 5.833, 12.0],
               [1.1, 4.5, -26.0]])

vl = np.array([[0.467, 0.067, 0.119],
               [0.033, 3.75, 2.667],
               [0.022, 1.0, 4.444]])

# Heatmap of VL/SM ratio
ax1 = fig.add_axes([0.08, 0.12, 0.38, 0.75], facecolor=PAN)
ax1.set_title('VL/SM Ratio (%)', fontsize=12, fontweight='bold', color=WHITE, pad=10)

ratio = np.abs(vl / sm) * 100
im = ax1.imshow(ratio, cmap='YlOrRd', vmin=0, vmax=70, aspect='auto')
for i in range(3):
    for j in range(3):
        color = 'black' if ratio[i, j] > 40 else WHITE
        ax1.text(j, i, '%.1f%%' % ratio[i, j], ha='center', va='center',
                fontsize=12, fontweight='bold', color=color)

ax1.set_xticks([0, 1, 2])
ax1.set_xticklabels(['U(1)', 'SU(2)', 'SU(3)'], fontsize=10, color=SILVER)
ax1.set_yticks([0, 1, 2])
ax1.set_yticklabels(['U(1)', 'SU(2)', 'SU(3)'], fontsize=10, color=SILVER)
ax1.tick_params(colors=DIM)

# VL matrix values
ax2 = fig.add_axes([0.55, 0.12, 0.38, 0.75], facecolor=PAN)
ax2.set_title('VL b_ij (exact Fractions)', fontsize=12, fontweight='bold',
              color=WHITE, pad=10)

fracs = [['7/15', '1/15', '16/135'],
         ['1/30', '15/4', '8/3'],
         ['1/45', '1', '40/9']]

ax2.imshow(vl, cmap='Blues', vmin=0, vmax=5, aspect='auto')
for i in range(3):
    for j in range(3):
        ax2.text(j, i, fracs[i][j], ha='center', va='center',
                fontsize=13, fontweight='bold', color=WHITE)

ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['U(1)', 'SU(2)', 'SU(3)'], fontsize=10, color=SILVER)
ax2.set_yticks([0, 1, 2])
ax2.set_yticklabels(['U(1)', 'SU(2)', 'SU(3)'], fontsize=10, color=SILVER)
ax2.tick_params(colors=DIM)

save(fig, 'session4_04_bij_heatmap.png')

# ================================================================
# FIG 5: THE THRESHOLD CORRECTION PROBLEM
# ================================================================
print("Fig 5: Threshold Correction Problem")

fig = sfig((16, 10), "GUT THRESHOLD CORRECTIONS — Why Minimal SU(5) Fails")
ax = fig.add_axes([0.12, 0.15, 0.82, 0.75], facecolor=PAN)

# The scan: M_X/M vs delta_Delta for C_total = -1/4
ratios_log = np.linspace(0, 5, 200)
ratios = 10**ratios_log
ln_vals = -np.log(ratios)
delta_delta = 0.25 * (-ln_vals) / (2 * np.pi)

ax.plot(ratios_log, delta_delta, color=CYAN, linewidth=2.5, label='C_total = -1/4')

# Target line
ax.axhline(y=0.40, color=GOLD, linewidth=1.5, linestyle='--', label='Target: Delta = 0.40')

# Naturalness region
ax.axvspan(0, 1, color=GREEN, alpha=0.08)
ax.text(0.5, 0.37, 'Natural\n(M_X/M<10)', fontsize=9, color=GREEN, ha='center')

# Fine-tuning region
ax.axvspan(2, 5, color=RED, alpha=0.05)
ax.text(3.5, 0.37, 'Fine-tuned\n(M_X/M>100)', fontsize=9, color=RED, ha='center')

# Mark the solution point
sol_log = np.log10(23228)
ax.scatter([sol_log], [0.40], s=200, color=RED, zorder=5, edgecolors=WHITE, linewidth=2)
ax.text(sol_log + 0.15, 0.42, 'M_X/M = 23,228\nΔ = 0', fontsize=10,
        color=RED, fontweight='bold')

# Also show triplet-only curve
delta_T = (1.0/12) * (-ln_vals) / (2 * np.pi)
ax.plot(ratios_log, delta_T, color=ORANGE, linewidth=1.5, linestyle='--',
        label='C_T = -1/12 (triplet only)')

ax.set_xlabel('log₁₀(M_X / M)', fontsize=11, color=SILVER)
ax.set_ylabel('Threshold correction δΔ (dimensionless)', fontsize=11, color=SILVER)
ax.set_xlim(0, 5)
ax.set_ylim(0, 0.55)
ax.legend(fontsize=9, loc='lower right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, 'session4_05_threshold_problem.png')

# ================================================================
# FIG 6: THE INTEGER TRACEABILITY CHAIN (from PHYS-26)
# ================================================================
print("Fig 6: Integer Traceability Chain")

fig = sfig((18, 12), "THE INTEGER TRACEABILITY CHAIN — Seven Links")
ax = sax(fig, [0.02, 0.03, 0.96, 0.88])

links = [
    (50, 55, 'Tr(Y²)=10/3, Tr(T₃²)=2', 'SU(5) embedding', GOLD),
    (50, 48, 'k₁ = 3/5', 'GUT normalization', GOLD),
    (50, 41, 'C₁=2/5, C₂=2/3, C₃=1/3', 'Dynkin coefficients', CYAN),
    (50, 34, 'Δb = (1/15, 1, 1/3)', 'CD beta shifts', GREEN),
    (30, 26, "b₂' = −13/6 → 13", 'SU(2) modified', CYAN),
    (70, 26, "b₃' = −20/3 → 20", 'SU(3) modified', CYAN),
]

for x, y, text, sub, color in links:
    box(ax, x-16, y-2.5, 32, 5, text, color, 10, sub)

# Arrows between links
for i in range(3):
    arrow(ax, 50, links[i][1]-2.5, 50, links[i+1][1]+2.5, GOLD, 2)

arrow(ax, 50, links[3][1]-2.5, 30, links[4][1]+2.5, GREEN, 2)
arrow(ax, 50, links[3][1]-2.5, 70, links[5][1]+2.5, GREEN, 2)

# Cosmological formulas branching from 13 and 20
formulas_13 = [
    (5, 15, 'Λ: 39=3×13', PURPLE),
    (5, 9, 'DM: (22/13)π', PURPLE),
    (5, 3, 'Ω_b: 2/(13π)', PURPLE),
    (30, 15, 'Ω_DM: 44/13²', PURPLE),
    (30, 9, 'sin²θ_W: 3/13', PURPLE),
    (30, 3, 'H₀: 20/13', PURPLE),
]

for x, y, text, color in formulas_13:
    box(ax, x, y-2, 22, 4, text, color, 9)

arrow(ax, 30, 23.5, 16, 17, CYAN)
arrow(ax, 30, 23.5, 41, 17, CYAN)

# 20 arrow to H0
arrow(ax, 70, 23.5, 41, 5, CYAN)

# Note about k1 independence
ax.add_patch(mpatches.FancyBboxPatch((55, 3), 40, 8, boxstyle="round,pad=0.4",
             facecolor='#0a150a', edgecolor=GREEN, linewidth=1.5, linestyle='--'))
ax.text(75, 8.5, 'C₂ and C₃ do NOT contain k₁', fontsize=10,
        fontweight='bold', color=GREEN, ha='center')
ax.text(75, 5.5, 'Track B (cosmology) is independent\nof GUT normalization',
        fontsize=9, color=SILVER, ha='center', linespacing=1.3)

save(fig, 'session4_06_integer_chain.png')

# ================================================================
# FIG 7: THE FOUR-VALUE sin²θ_W ORDERING
# ================================================================
print("Fig 7: sin²θ_W Ordering")

fig = sfig((18, 8), "THE sin²θ_W ORDERING — Every Refinement Moves Right")
ax = fig.add_axes([0.06, 0.2, 0.90, 0.65], facecolor=PAN)

points = [
    (0.22722, 'threshold\n(M_VL=500)', ORANGE, -20),
    (0.22845, 'no-threshold\n(best 1L)', CYAN, 20),
    (0.23028, '2-loop\nestimate', GREEN, -20),
    (0.23077, '3/13', GOLD, 20),
    (0.23122, 'measured', MAG, -20),
]

for val, label, color, offset in points:
    ax.scatter([val], [0], s=250, color=color, zorder=5, edgecolors=WHITE, linewidth=2)
    ax.annotate(label, xy=(val, 0), xytext=(val, offset * 0.015),
                fontsize=9, color=color, ha='center', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=color, lw=1),
                linespacing=1.3)
    ax.text(val, -0.025, '%.5f' % val, fontsize=8, color=SILVER,
            ha='center', rotation=45)

# Direction arrow
ax.annotate('', xy=(0.232, 0.03), xytext=(0.226, 0.03),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))
ax.text(0.229, 0.035, 'refinement direction', fontsize=10, color=WHITE,
        ha='center', style='italic')

ax.set_xlim(0.225, 0.234)
ax.set_ylim(-0.05, 0.05)
ax.set_xlabel('sin²θ_W (dimensionless)', fontsize=11, color=SILVER)
ax.set_yticks([])
ax.tick_params(colors=DIM, labelsize=9)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color(DIM)

save(fig, 'session4_07_sin2tw_ordering.png')

# ================================================================
# FIG 8: THE CORRECTION FRACTION 15/104
# ================================================================
print("Fig 8: The Correction 15/104")

fig = sfig((16, 10), "THE CORRECTION FRACTION — 3/8 → 3/13 requires 15/104")
ax = sax(fig, [0.02, 0.03, 0.96, 0.88])

# Tree level box
box(ax, 5, 42, 20, 10, '3/8', GOLD, 28, 'Tree level\nSU(5)', SILVER)

# Target box
box(ax, 75, 42, 20, 10, '3/13', CYAN, 28, 'Target\nN_gen/|b₂\'|', SILVER)

# Correction arrow
ax.annotate('', xy=(75, 47), xytext=(25, 47),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=3))
ax.text(50, 50, '− 15/104', fontsize=18, fontweight='bold', color=WHITE,
        ha='center')

# Factorization
box(ax, 15, 22, 70, 14, '', DIM, 10)
ax.text(50, 33, 'FACTORIZATION: 15/104 = 15 / (8 × 13)', fontsize=14,
        fontweight='bold', color=WHITE, ha='center')

factors = [
    (25, 24, '15', 'Δb₂/Δb₁\nasymmetry', ORANGE),
    (50, 24, '8', 'from 3/8\ntree denom', GOLD),
    (75, 24, '13', '|b₂\' num|\nCD integer', CYAN),
]

for x, y, num, sub, color in factors:
    ax.text(x, y + 3, num, fontsize=22, fontweight='bold', color=color, ha='center')
    ax.text(x, y, sub, fontsize=9, color=SILVER, ha='center', linespacing=1.3)

# Current status
box(ax, 10, 4, 80, 12, '', DIM, 10)
ax.text(50, 13, 'One-loop overcorrects by 1.6%: actual correction = 0.14655 vs needed 0.14423',
        fontsize=10, color=SILVER, ha='center')
ax.text(50, 9, 'Two-loop estimate: correction ~ 0.14472 → within 0.3% of 15/104',
        fontsize=10, color=GREEN, ha='center')
ax.text(50, 5, 'PHYS-40 will test: does the exact two-loop result equal 15/104?',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save(fig, 'session4_08_correction_15_104.png')

# ================================================================
# FIG 9: THE NULL RESULT — WHAT SURVIVES
# ================================================================
print("Fig 9: What Survives the Null Result")

fig = sfig((18, 12), "THE PHYS-29 NULL RESULT — What Survives, What Is Disfavored")
ax = sax(fig, [0.02, 0.03, 0.96, 0.88])

# Survives column
ax.add_patch(mpatches.FancyBboxPatch((2, 5), 44, 50, boxstyle="round,pad=0.5",
             facecolor='#0a150a', edgecolor=GREEN, linewidth=2))
ax.text(24, 53, 'SURVIVES', fontsize=16, fontweight='bold', color=GREEN, ha='center')

survives = [
    'CD representation (3,2,1/6)',
    'Beta shifts (1/15, 1, 1/3)',
    'Gap ratio 38/27',
    'Integers 13, 20, 22',
    'Two-loop improvement (66%)',
    'VL b_ij (+4.6%)',
    'M_GUT ≈ 10^15.4 GeV',
    'τ_proton ~ 10^34.5 yr',
    'sin²θ_W ordering',
    'All cosmological formulas',
    'Track B program',
]

for i, item in enumerate(survives):
    ax.text(24, 49 - i * 3.8, item, fontsize=9, color=GREEN, ha='center')

# Disfavored column
ax.add_patch(mpatches.FancyBboxPatch((54, 28), 44, 27, boxstyle="round,pad=0.5",
             facecolor='#1a0a0a', edgecolor=RED, linewidth=2))
ax.text(76, 53, 'DISFAVORED', fontsize=16, fontweight='bold', color=RED, ha='center')

disfavored = [
    'Minimal SU(5) completion',
    'Natural GUT thresholds (C=-1/4)',
    'Specific M_T prediction',
]

for i, item in enumerate(disfavored):
    ax.text(76, 49 - i * 3.8, item, fontsize=10, color=RED, ha='center')

# Alternative pathways
ax.add_patch(mpatches.FancyBboxPatch((54, 5), 44, 18, boxstyle="round,pad=0.5",
             facecolor='#0a0a15', edgecolor=ORANGE, linewidth=1.5, linestyle='--'))
ax.text(76, 21, 'ALTERNATIVE PATHWAYS', fontsize=11, fontweight='bold',
        color=ORANGE, ha='center')

alternatives = [
    'SO(10) intermediate scale',
    'Extended Higgs sector',
    'Three-loop corrections',
    'Non-minimal SU(5)',
]

for i, item in enumerate(alternatives):
    ax.text(76, 17 - i * 3.5, item, fontsize=9, color=ORANGE, ha='center')

# The key point
ax.text(50, 1.5, 'The Cabibbo Doublet is Level 1 arithmetic. '
        'It is INDEPENDENT of the GUT completion.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold', style='italic')

save(fig, 'session4_09_null_survives.png')

# ================================================================
# FIG 10: THE VERIFICATION LEDGER
# ================================================================
print("Fig 10: Verification Ledger")

fig = sfig((16, 12), "THE COMPLETE VERIFICATION LEDGER — 466/467")
ax = sax(fig, [0.02, 0.03, 0.96, 0.88])

scripts = [
    ('phys29_gut_thresholds.py', 10, 11, RED, 'PHYS-29 (1 abort)'),
    ('phys28_vl_twoloop.py', 11, 11, GREEN, 'PHYS-28'),
    ('phys27_sin2tw.py', 13, 13, GREEN, 'PHYS-27'),
    ('phys26_normalization.py', 20, 20, CYAN, 'PHYS-26 (ALL EXACT)'),
    ('phys25_platform.py', 47, 47, GREEN, 'PHYS-25'),
    ('beta_unification_test.py', 15, 15, GREEN, 'Beta cosmos'),
    ('qed_predicts_gr.py + scan2', 20, 20, GREEN, 'QED-to-GR'),
    ('phys24_lib + test', 169, 169, CYAN, 'Platform'),
    ('PHYS-24 demo scripts', 62, 62, GREEN, '8 scripts'),
    ('Session 3 scripts', 98, 98, GREEN, '6 scripts'),
]

y_start = 54
bar_max = 60

for i, (name, passed, total, color, label) in enumerate(scripts):
    y = y_start - i * 5.2
    w = passed / 169 * bar_max  # normalize to max
    ax.add_patch(mpatches.FancyBboxPatch((2, y-1.5), w, 3.5,
                 boxstyle="round,pad=0.2", facecolor=color, edgecolor=color,
                 linewidth=0, alpha=0.3))
    ax.add_patch(mpatches.FancyBboxPatch((2, y-1.5), w, 3.5,
                 boxstyle="round,pad=0.2", facecolor='none', edgecolor=color,
                 linewidth=1.5))
    ax.text(w + 4, y, '%d/%d' % (passed, total), fontsize=11,
            color=color, va='center', fontweight='bold')
    ax.text(1, y, label, fontsize=9, color=WHITE, va='center', ha='left')
    ax.text(w + 12, y, name, fontsize=8, color=DIM, va='center')

# Total
ax.text(50, 2, '466 / 467  —  ONE INTENTIONAL FAIL (abort test)',
        fontsize=14, fontweight='bold', color=GOLD, ha='center')
ax.text(50, -1, 'The abort test is a FEATURE: it fires when minimal SU(5) '
        'requires unnatural mass splitting.',
        fontsize=9, color=DIM, ha='center', style='italic')

save(fig, 'session4_10_verification_ledger.png')

# ================================================================
print()
print("=" * 70)
print("SESSION 4 DIAGRAM ATLAS — 10 FIGURES GENERATED")
print("=" * 70)
for i, name in enumerate([
    'session4_01_program_map.png',
    'session4_02_delta_chain.png',
    'session4_03_sin2tw_convergence.png',
    'session4_04_bij_heatmap.png',
    'session4_05_threshold_problem.png',
    'session4_06_integer_chain.png',
    'session4_07_sin2tw_ordering.png',
    'session4_08_correction_15_104.png',
    'session4_09_null_survives.png',
    'session4_10_verification_ledger.png',
], 1):
    print("  Fig %d: %s" % (i, name))
    