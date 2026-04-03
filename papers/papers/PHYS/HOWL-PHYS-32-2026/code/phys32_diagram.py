#!/usr/bin/env python3
"""
HOWL PHYS-32 Diagrams — The A3 Decomposition
8 figures covering the SU(3) beta structure.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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

def save(fig, name):
    p = os.path.join(outdir, name)
    fig.savefig(p, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % p)

def style_ax(ax):
    ax.set_facecolor(PAN)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# ================================================================
# DATA (from phys32_a3_decomposition.py — source of truth)
# ================================================================

# SU(3) decomposition
b3_gauge = -11.0
b3_fermion = 4.0
b3_higgs = 0.0
b3_cd = 1.0 / 3.0
b3_SM = -7.0
b3_mod = -20.0 / 3.0

# SU(2) decomposition
b2_gauge = -22.0 / 3.0
b2_fermion = 4.0
b2_higgs = 1.0 / 6.0
b2_cd = 1.0
b2_SM = -19.0 / 6.0
b2_mod = -13.0 / 6.0

# U(1) — partial (no gauge term for abelian)
b1_higgs = 0.1
b1_cd = 1.0 / 15.0
b1_SM = 41.0 / 10.0
b1_mod = 25.0 / 6.0

# Numerator decomposition over denom 3
num_gauge = -33
num_fermion = 12
num_higgs = 0
num_cd = 1

# ================================================================
# FIG 1: ALL THREE BETAS DECOMPOSED SIDE BY SIDE
# Type: Comparison
# Shows: The pattern — fermion=+4 for both SU(2) and SU(3),
#        Higgs only enters SU(2), gauge dominates differently
# ================================================================
print("Fig 1: Three Betas Decomposed")

fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
style_ax(ax)
fig.suptitle("THREE GAUGE BETAS DECOMPOSED — Gauge, Fermion, Higgs, CD",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

groups = [r"$b_1'$ (U(1)) = 25/6", r"$b_2'$ (SU(2)) = $-$13/6",
          r"$b_3'$ (SU(3)) = $-$20/3"]
x = np.array([0, 1.5, 3.0])
width = 0.3

# Gauge contributions
gauge_vals = [0, b2_gauge, b3_gauge]
# Fermion contributions (approximate b1_fermion for display)
b1_fermion_approx = b1_SM - b1_higgs  # ~4.0 (complex, but approximate)
fermion_vals = [b1_fermion_approx, b2_fermion, b3_fermion]
# Higgs
higgs_vals = [b1_higgs, b2_higgs, b3_higgs]
# CD
cd_vals = [b1_cd, b2_cd, b3_cd]

ax.bar(x - 1.5*width, gauge_vals, width, color=RED, alpha=0.7,
       edgecolor=RED, linewidth=2, label='Gauge')
ax.bar(x - 0.5*width, fermion_vals, width, color=GREEN, alpha=0.7,
       edgecolor=GREEN, linewidth=2, label='Fermion (3 gen)')
ax.bar(x + 0.5*width, higgs_vals, width, color=BLUE, alpha=0.7,
       edgecolor=BLUE, linewidth=2, label='Higgs')
ax.bar(x + 1.5*width, cd_vals, width, color=GOLD, alpha=0.7,
       edgecolor=GOLD, linewidth=2, label='Cabibbo Doublet')

# Labels on bars
for i in range(3):
    vals = [gauge_vals[i], fermion_vals[i], higgs_vals[i], cd_vals[i]]
    offsets = [-1.5, -0.5, 0.5, 1.5]
    for j, v in enumerate(vals):
        if abs(v) > 0.05:
            y_off = 0.3 if v > 0 else -0.6
            ax.text(x[i] + offsets[j]*width, v + y_off,
                    '%.2f' % v, fontsize=8, color=WHITE,
                    ha='center', fontweight='bold')

# Total lines
totals = [b1_mod, b2_mod, b3_mod]
for i in range(3):
    ax.plot([x[i] - 2.2*width, x[i] + 2.2*width],
            [totals[i], totals[i]], color=WHITE, linewidth=2,
            linestyle='--')
    ax.text(x[i] + 2.5*width, totals[i],
            '= %.3f' % totals[i], fontsize=10, color=WHITE,
            fontweight='bold', va='center')

ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=12, color=SILVER)
ax.set_ylabel('Contribution to beta coefficient', fontsize=12, color=SILVER)
ax.set_xlim(-0.8, 4.2)
ax.set_ylim(-12, 6)
ax.axhline(y=0, color=DIM, linewidth=0.5)
ax.legend(fontsize=10, loc='lower left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, ncol=2)

# Annotation: fermion coincidence
ax.annotate('Fermion = +4\nfor BOTH\nSU(2) and SU(3)',
            xy=(2.25, 4), xytext=(3.5, 5),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

save(fig, 'phys32_01_three_betas.png')

# ================================================================
# FIG 2: WATERFALL CHART — NUMERATOR TO -20
# Type: Progression
# Shows: Each piece adds, building to -20
# ================================================================
print("Fig 2: Waterfall to -20")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THE NUMERATOR — Building $-$20 Step by Step",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

labels = ['Start', 'Gauge\n($-$33)', 'Fermion\n(+12)', 'Higgs\n(0)',
          'CD\n(+1)', 'Total']
running = [0, -33, -33+12, -33+12+0, -33+12+0+1, -33+12+0+1]
steps = [0, -33, 12, 0, 1, 0]
colors_w = [DIM, RED, GREEN, BLUE, GOLD, WHITE]

x_pos = np.arange(len(labels))

# Draw waterfall bars
for i in range(1, len(labels)-1):
    bottom = running[i-1]
    height = steps[i]
    if height == 0:
        # Draw a thin line for zero contribution
        ax.plot([x_pos[i]-0.3, x_pos[i]+0.3], [bottom, bottom],
                color=BLUE, linewidth=3, alpha=0.5)
        ax.text(x_pos[i], bottom + 1.5, '0', fontsize=12,
                color=BLUE, ha='center', fontweight='bold')
    else:
        ax.bar(x_pos[i], height, 0.6, bottom=bottom,
               color=colors_w[i], alpha=0.6,
               edgecolor=colors_w[i], linewidth=2)
        y_label = bottom + height/2
        ax.text(x_pos[i], y_label, '%+d' % height,
                fontsize=14, color=WHITE, ha='center',
                fontweight='bold', va='center')

# Connecting lines between steps
for i in range(1, len(labels)-1):
    ax.plot([x_pos[i]+0.35, x_pos[i+1]-0.35],
            [running[i], running[i]],
            color=DIM, linewidth=1, linestyle=':')

# Start marker
ax.scatter([x_pos[0]], [0], s=200, color=DIM, zorder=5,
           edgecolors=WHITE, linewidth=2)

# Total bar
ax.bar(x_pos[-1], running[-1], 0.6, color=GOLD, alpha=0.7,
       edgecolor=GOLD, linewidth=2)
ax.text(x_pos[-1], running[-1]/2, '%d' % running[-1],
        fontsize=18, color=WHITE, ha='center',
        fontweight='bold', va='center')

# Running total annotations
for i in range(1, len(labels)):
    ax.text(x_pos[i], running[i] - 2.5,
            'sum = %d' % running[i], fontsize=9,
            color=SILVER, ha='center', style='italic')

ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=11, color=SILVER)
ax.set_ylabel('Numerator value (over denominator 3)', fontsize=12,
              color=SILVER)
ax.set_xlim(-0.8, 5.8)
ax.set_ylim(-40, 18)
ax.axhline(y=0, color=DIM, linewidth=0.5)

ax.text(3, 12, r"$b_3' = -20/3$" + '\n= ($-$33 + 12 + 0 + 1) / 3',
        fontsize=13, color=GOLD, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD))

save(fig, 'phys32_02_waterfall.png')

# ================================================================
# FIG 3: INTEGER 20 TRACEABILITY GENEALOGY
# Type: Connection
# Shows: 20 traced backward through its constituents to physics
# ================================================================
print("Fig 3: Integer 20 Genealogy")

fig = plt.figure(figsize=(18, 12), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

fig.suptitle("THE INTEGER 20 — Complete Genealogy",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

def rbox(ax, x, y, w, h, text, color, fs=11, sub=None, sc=None):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.5",
        facecolor='#0f0f1a', edgecolor=color, linewidth=2))
    if sub:
        ax.text(x+w/2, y+h/2+1.5, text, fontsize=fs,
                fontweight='bold', color=color, ha='center', va='center')
        ax.text(x+w/2, y+h/2-1.5, sub, fontsize=9,
                color=sc or SILVER, ha='center', va='center')
    else:
        ax.text(x+w/2, y+h/2, text, fontsize=fs,
                fontweight='bold', color=color, ha='center', va='center')

def arrow(ax, x1, y1, x2, y2, color=SILVER, lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))

# Top: the result
rbox(ax, 35, 60, 30, 7, r"$b_3'$ = $-$20/3", GOLD, 16,
     'The modified SU(3) beta', SILVER)

# Second level: numerator
rbox(ax, 35, 48, 30, 7, '$-$20 = $-$33 + 12 + 0 + 1', WHITE, 12,
     'Numerator over denominator 3', SILVER)

arrow(ax, 50, 60, 50, 55, GOLD, 2)

# Third level: four pieces
rbox(ax, 2, 34, 20, 8, '$-$33', RED, 14, 'Gauge', RED)
rbox(ax, 27, 34, 20, 8, '+12', GREEN, 14, 'Fermion (SM)', GREEN)
rbox(ax, 52, 34, 20, 8, '0', BLUE, 14, 'Higgs', BLUE)
rbox(ax, 77, 34, 20, 8, '+1', GOLD, 14, 'CD', GOLD)

arrow(ax, 42, 48, 12, 42, WHITE, 1.5)
arrow(ax, 47, 48, 37, 42, WHITE, 1.5)
arrow(ax, 53, 48, 62, 42, WHITE, 1.5)
arrow(ax, 58, 48, 87, 42, WHITE, 1.5)

# Fourth level: physics origins
rbox(ax, 0, 20, 24, 8, '(11/3) $\\times$ 3 = 11', RED, 11,
     r'$C_2$(adj SU(3)) = 3', SILVER)
rbox(ax, 26, 20, 22, 8, '3 gen $\\times$ 4/3 = 4', GREEN, 11,
     '12 Weyl triplets', SILVER)
rbox(ax, 51, 20, 22, 8, r'$S_2$(singlet) = 0', BLUE, 11,
     'Color singlet (1,2,1/2)', SILVER)
rbox(ax, 76, 20, 22, 8, '(1/3)$\\times$2$\\times$1/2', GOLD, 11,
     'VL Dynkin formula', SILVER)

arrow(ax, 12, 34, 12, 28, RED, 1.5)
arrow(ax, 37, 34, 37, 28, GREEN, 1.5)
arrow(ax, 62, 34, 62, 28, BLUE, 1.5)
arrow(ax, 87, 34, 87, 28, GOLD, 1.5)

# Fifth level: fundamental constants
rbox(ax, 0, 6, 24, 8, 'N = 3 for SU(3)', RED, 10,
     'Adjoint Casimir = N', SILVER)
rbox(ax, 26, 6, 22, 8, r'4 Weyl $\times$ $S_2$ = 1/2', GREEN, 10,
     'Q_L(2) + u_R(1) + d_R(1)', SILVER)
rbox(ax, 76, 6, 22, 8, r'dim$(R_2)$ = 2, $S_2$ = 1/2', GOLD, 10,
     'Same S_2 as SM quarks', SILVER)

arrow(ax, 12, 20, 12, 14, RED, 1)
arrow(ax, 37, 20, 37, 14, GREEN, 1)
arrow(ax, 87, 20, 87, 14, GOLD, 1)

save(fig, 'phys32_03_integer_genealogy.png')

# ================================================================
# FIG 4: WEYL FERMION CENSUS — WHICH QUARKS CONTRIBUTE
# Type: Geometry
# Shows: One generation with color-charge visibility
# ================================================================
print("Fig 4: Weyl Fermion Census")

fig = plt.figure(figsize=(18, 11), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

fig.suptitle("WEYL FERMION CENSUS — One Generation, SU(3) Contributions",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Draw each multiplet as a box with color indicators
def particle_box(ax, x, y, name, rep, colored, n_weyl, contrib, color):
    w, h = 16, 12
    ec = color if colored else DIM
    fc = '#0f0f1a' if colored else '#08080f'
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.4",
        facecolor=fc, edgecolor=ec, linewidth=2.5 if colored else 1))
    ax.text(x+w/2, y+h-2, name, fontsize=12, fontweight='bold',
            color=color, ha='center')
    ax.text(x+w/2, y+h-4.5, rep, fontsize=9, color=SILVER, ha='center')
    if colored:
        # Draw color triplet indicators
        colors_rgb = [RED, GREEN, BLUE]
        for ci in range(3):
            cx = x + 3 + ci * 4
            ax.add_patch(plt.Circle((cx, y+3.5), 1.2,
                         facecolor=colors_rgb[ci], alpha=0.5,
                         edgecolor=colors_rgb[ci]))
        ax.text(x+w/2, y+1, '%d Weyl $\\rightarrow$ %s' % (n_weyl, contrib),
                fontsize=9, color=WHITE, ha='center', fontweight='bold')
    else:
        ax.text(x+w/2, y+3, 'SU(3) singlet', fontsize=9,
                color=DIM, ha='center')
        ax.text(x+w/2, y+1, r'$b_3$ = 0', fontsize=9,
                color=DIM, ha='center')

# Quarks (colored) — top row
particle_box(ax, 2, 36, r'$Q_L$', '(3, 2, 1/6)', True, 2, '2/3', GREEN)
particle_box(ax, 22, 36, r'$u_R$', '(3, 1, 2/3)', True, 1, '1/3', CYAN)
particle_box(ax, 42, 36, r'$d_R$', r'(3, 1, $-$1/3)', True, 1, '1/3', CYAN)

# Leptons (not colored) — bottom row
particle_box(ax, 62, 36, r'$L_L$', r'(1, 2, $-$1/2)', False, 0, '0', DIM)
particle_box(ax, 82, 36, r'$e_R$', '(1, 1, $-$1)', False, 0, '0', DIM)

# Dividing line
ax.plot([60, 60], [34, 50], color=ORANGE, linewidth=2, linestyle='--')
ax.text(60, 51, 'COLORED          COLORLESS', fontsize=11,
        color=ORANGE, ha='center', fontweight='bold')

# Sum bar at bottom
ax.add_patch(mpatches.FancyBboxPatch(
    (5, 18), 52, 10, boxstyle="round,pad=0.5",
    facecolor='#0a150a', edgecolor=GREEN, linewidth=2))

ax.text(31, 25, 'TOTAL per generation:', fontsize=12,
        color=WHITE, ha='center', fontweight='bold')
ax.text(31, 21, '4 Weyl triplets $\\times$ (2/3)(1/2) = 4/3',
        fontsize=13, color=GREEN, ha='center', fontweight='bold')

# Three generations
ax.add_patch(mpatches.FancyBboxPatch(
    (5, 4), 90, 10, boxstyle="round,pad=0.5",
    facecolor='#0a0a15', edgecolor=GOLD, linewidth=2))

ax.text(50, 11, '3 GENERATIONS:', fontsize=12,
        color=WHITE, ha='center', fontweight='bold')
ax.text(50, 7, '3 $\\times$ 4/3 = 4       '
        r'($b_3$ fermion contribution)',
        fontsize=13, color=GOLD, ha='center', fontweight='bold')

save(fig, 'phys32_04_weyl_census.png')

# ================================================================
# FIG 5: ASYMPTOTIC FREEDOM BALANCE
# Type: Scale
# Shows: Where SM and CD sit relative to the AF threshold
# ================================================================
print("Fig 5: Asymptotic Freedom Balance")

fig, ax = plt.subplots(figsize=(18, 9), facecolor=BG)
style_ax(ax)
fig.suptitle("ASYMPTOTIC FREEDOM — Gauge vs Matter Balance",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Number line from -12 to +2
y_line = 0.5
ax.axhline(y=y_line, color=DIM, linewidth=1)
ax.axvline(x=0, color=WHITE, linewidth=1.5, linestyle='--', alpha=0.5)

# Gauge contribution
ax.annotate('', xy=(-11, y_line), xytext=(0, y_line),
            arrowprops=dict(arrowstyle='<-', color=RED, lw=4))
ax.text(-5.5, y_line + 0.35, 'GAUGE: $-$11', fontsize=14,
        color=RED, ha='center', fontweight='bold')
ax.text(-5.5, y_line + 0.15, '(asymptotic freedom)', fontsize=9,
        color=RED, ha='center')

# SM fermion contribution
ax.annotate('', xy=(-11+4, y_line-0.05), xytext=(-11, y_line-0.05),
            arrowprops=dict(arrowstyle='<-', color=GREEN, lw=4))
ax.text(-9, y_line - 0.25, 'SM quarks: +4', fontsize=12,
        color=GREEN, ha='center', fontweight='bold')

# SM total marker
ax.scatter([-7], [y_line], s=300, color=WHITE, zorder=5,
           edgecolors=CYAN, linewidth=3)
ax.text(-7, y_line + 0.35, r'$b_3^{SM}$ = $-$7', fontsize=13,
        color=CYAN, ha='center', fontweight='bold')

# CD contribution
ax.annotate('', xy=(-7 + 1.0/3, y_line+0.05), xytext=(-7, y_line+0.05),
            arrowprops=dict(arrowstyle='<-', color=GOLD, lw=3))
ax.text(-6.5, y_line + 0.55, 'CD: +1/3', fontsize=11,
        color=GOLD, ha='center', fontweight='bold')

# Modified total marker
ax.scatter([-20.0/3], [y_line], s=250, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(-20.0/3, y_line - 0.3, r"$b_3'$ = $-$20/3", fontsize=12,
        color=GOLD, ha='center', fontweight='bold')

# Critical threshold
n_crit = 33.0 / 4.0  # 8.25 Dirac quarks -> b3 = -11 + (4/3)*8.25 = 0
ax.axvline(x=0, color=ORANGE, linewidth=2, linestyle='-', alpha=0.7)
ax.text(0.3, y_line + 0.5, 'b = 0\n(AF lost)', fontsize=11,
        color=ORANGE, fontweight='bold')

# Shade AF region
ax.axvspan(-12, 0, color=GREEN, alpha=0.04)
ax.axvspan(0, 2, color=RED, alpha=0.06)
ax.text(-9, y_line - 0.55, 'ASYMPTOTICALLY FREE', fontsize=11,
        color=GREEN, ha='center', fontweight='bold', alpha=0.6)
ax.text(1, y_line - 0.55, 'NOT\nAF', fontsize=10,
        color=RED, ha='center', fontweight='bold', alpha=0.6)

# Info box
ax.text(1.5, y_line + 0.3,
        'AF breaks at\n%.2f Dirac quarks\nSM has 6\nCD adds ~0.25' % n_crit,
        fontsize=10, color=SILVER, ha='left',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_xlim(-12.5, 3)
ax.set_ylim(-0.8, 1.2)
ax.set_xlabel(r'$b_3$ value (dimensionless)', fontsize=12, color=SILVER)
ax.set_yticks([])

save(fig, 'phys32_05_af_balance.png')

# ================================================================
# FIG 6: CRITICAL FLAVOR NUMBER — b3 vs n_f
# Type: Running
# Shows: The curve crossing zero — how many quarks break AF
# ================================================================
print("Fig 6: Critical Flavor Number")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"ASYMPTOTIC FREEDOM THRESHOLD — $b_3$ vs Number of Dirac Quarks",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

n_f = np.linspace(0, 12, 200)
b3_curve = -11 + (4.0/3.0) * n_f

ax.plot(n_f, b3_curve, color=CYAN, linewidth=2.5)
ax.axhline(y=0, color=ORANGE, linewidth=2, linestyle='--', alpha=0.7)
ax.fill_between(n_f, b3_curve, 0, where=(b3_curve < 0),
                color=GREEN, alpha=0.05)
ax.fill_between(n_f, b3_curve, 0, where=(b3_curve > 0),
                color=RED, alpha=0.05)

# Mark SM (6 Dirac quarks)
b3_at_6 = -11 + (4.0/3.0) * 6
ax.scatter([6], [b3_at_6], s=250, color=WHITE, zorder=5,
           edgecolors=GREEN, linewidth=2.5)
ax.annotate('SM: 6 quarks\n' + r'$b_3$ = $-$7',
            xy=(6, b3_at_6),
            xytext=(7.5, b3_at_6 - 1.5),
            fontsize=11, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# Mark SM + CD (effectively ~6.25)
n_cd_eff = 6 + 0.25  # approximate
b3_at_cd = -11 + (4.0/3.0) * n_cd_eff
ax.scatter([n_cd_eff], [b3_at_cd], s=250, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate('SM + CD\n' + r"$b_3'$ = $-$20/3",
            xy=(n_cd_eff, b3_at_cd),
            xytext=(8, b3_at_cd + 1),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark critical point
n_crit = 33.0 / 4.0
ax.scatter([n_crit], [0], s=300, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2.5)
ax.annotate(r'$n_f^{crit}$ = 33/4 = 8.25' + '\nAF breaks here',
            xy=(n_crit, 0),
            xytext=(n_crit + 0.8, 2),
            fontsize=11, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Labels
ax.text(3, 3, 'NOT ASYMPTOTICALLY\nFREE', fontsize=12,
        color=RED, ha='center', alpha=0.5, fontweight='bold')
ax.text(3, -5, 'ASYMPTOTICALLY\nFREE', fontsize=12,
        color=GREEN, ha='center', alpha=0.5, fontweight='bold')

ax.set_xlabel('Number of Dirac quark flavors ' + r'$n_f$', fontsize=12,
              color=SILVER)
ax.set_ylabel(r'$b_3$ (one-loop SU(3) beta coefficient)', fontsize=12,
              color=SILVER)
ax.set_xlim(-0.5, 12)
ax.set_ylim(-12, 6)

save(fig, 'phys32_06_critical_nf.png')

# ================================================================
# FIG 7: GAP RATIO SHIFT FROM Db3 = 1/3
# Type: Running
# Shows: How the CD changes the gap ratio toward measured
# ================================================================
print("Fig 7: Gap Ratio Shift")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"GAP RATIO SHIFT — How $\Delta b_3 = 1/3$ Moves the Denominator",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# The gap ratio = (b1' - b2') / (b2' - b3')
# Numerator is fixed at 38/6 (from b1' and b2')
# Denominator changes with b3'

b3_range = np.linspace(-8, -5, 200)
gap_num = 38.0 / 6.0
gap_den = (-13.0/6.0) - b3_range
gap_ratio = gap_num / gap_den

ax.plot(b3_range, gap_ratio, color=CYAN, linewidth=2.5,
        label='Gap ratio vs ' + r'$b_3$')

# Measured gap ratio
measured_gap = 1.358
ax.axhline(y=measured_gap, color=MAG, linewidth=2, linestyle='--',
           label='Measured: 1.358')
ax.axhspan(measured_gap * 0.95, measured_gap * 1.05, color=MAG, alpha=0.06)

# SM point
gap_sm = 38.0 / 29.0  # b2_SM - b3_SM = -19/6 + 7 = 23/6... 
# Actually: SM gap = (b1_SM - b2_SM)/(b2_SM - b3_SM)
# = (41/10 + 19/6) / (-19/6 + 7) = (41/10+19/6)/(23/6)
# Using CD betas for numerator but SM for denominator:
# With SM: numerator = 38/6 (using b1_mod, b2_mod), denom = b2_mod - b3_SM
# Wait — the gap ratio uses the SAME betas throughout.
# SM gap = (b1_SM - b2_SM)/(b2_SM - b3_SM) = (41/10+19/6)/(-19/6+7)
# = (246+190)/(60) / (42-19)/(6) = 436/60 / 23/6 = 218/115
sm_gap = 218.0 / 115.0
cd_gap = 38.0 / 27.0

ax.scatter([-7], [sm_gap], s=250, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate('SM: ' + r'$b_3$ = $-$7' + '\ngap = 218/115 = %.3f\nmiss: 40%%' % sm_gap,
            xy=(-7, sm_gap),
            xytext=(-7.5, sm_gap + 0.15),
            fontsize=10, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.scatter([-20.0/3], [cd_gap], s=250, color=GOLD, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate("CD: " + r"$b_3'$ = $-$20/3" + '\ngap = 38/27 = %.3f\nmiss: 3.6%%' % cd_gap,
            xy=(-20.0/3, cd_gap),
            xytext=(-6.2, cd_gap - 0.12),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Arrow showing the shift
ax.annotate('', xy=(-20.0/3, cd_gap), xytext=(-7, sm_gap),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=3, alpha=0.5))
ax.text(-6.85, (sm_gap+cd_gap)/2 + 0.03, r'$\Delta b_3$ = +1/3',
        fontsize=12, color=GREEN, fontweight='bold', ha='center')

ax.set_xlabel(r'$b_3$ value', fontsize=12, color=SILVER)
ax.set_ylabel('Gap ratio ' + r'$(b_1 - b_2)/(b_2 - b_3)$',
              fontsize=12, color=SILVER)
ax.set_xlim(-8.2, -5)
ax.set_ylim(1.1, 2.2)
ax.legend(fontsize=10, loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys32_07_gap_shift.png')

# ================================================================
# FIG 8: ONE-LOOP TO TWO-LOOP SHARED S2
# Type: Connection
# Shows: The same S2=1/2 feeds both perturbative orders
# ================================================================
print("Fig 8: One-Loop to Two-Loop Connection")

fig = plt.figure(figsize=(18, 11), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

fig.suptitle(r"SHARED GROUP THEORY — $S_2(fund) = 1/2$ Feeds Both Orders",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Central node: S2 = 1/2
ax.add_patch(plt.Circle((50, 35), 8, facecolor='#0f0f1a',
             edgecolor=GOLD, linewidth=3))
ax.text(50, 37, r'$S_2(fund)$', fontsize=14, fontweight='bold',
        color=GOLD, ha='center')
ax.text(50, 33, '= 1/2', fontsize=16, fontweight='bold',
        color=WHITE, ha='center')

# Left: One-loop
rbox(ax, 5, 48, 30, 8, 'ONE-LOOP', CYAN, 14,
     r'$\Delta b_3 = (1/3) \times 2 \times S_2$', CYAN)
rbox(ax, 5, 8, 30, 8, r'$\Delta b_3 = 1/3$', CYAN, 16,
     'Controls coupling running', SILVER)

arrow(ax, 42, 35, 35, 52, CYAN, 2)
arrow(ax, 20, 48, 20, 16, CYAN, 2)

# Additional one-loop details
rbox(ax, 5, 28, 30, 8, 'SM fermions', GREEN, 11,
     r'$b_3^{ferm}$ = 12 $\times$ (2/3) $\times$ $S_2$ = 4', GREEN)
arrow(ax, 42, 33, 35, 32, GREEN, 1.5)

# Right: Two-loop
rbox(ax, 65, 48, 30, 8, 'TWO-LOOP', ORANGE, 14,
     r'$db_{33} = (10/3) \times S_2 \times 2 \times C_2$', ORANGE)
rbox(ax, 65, 8, 30, 8, r'$db_{33} = 40/9$', ORANGE, 16,
     'Controls coupling mixing', SILVER)

arrow(ax, 58, 35, 65, 52, ORANGE, 2)
arrow(ax, 80, 48, 80, 16, ORANGE, 2)

# Additional two-loop detail
rbox(ax, 65, 28, 30, 8, r'+ Casimir $C_2 = 4/3$', RED, 11,
     'Two-loop needs more group theory', SILVER)
arrow(ax, 58, 37, 65, 32, RED, 1.5)

# Bottom connection
ax.text(50, 3, r'$S_2(fund) = 1/2$ is the single group theory constant' +
        '\nthat connects one-loop running to two-loop mixing.',
        fontsize=12, color=WHITE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

save(fig, 'phys32_08_oneloop_twoloop.png')

# ================================================================
print()
print("=" * 70)
print("PHYS-32 DIAGRAMS — 8 FIGURES GENERATED")
print("=" * 70)

filenames = [
    'phys32_01_three_betas.png',
    'phys32_02_waterfall.png',
    'phys32_03_integer_genealogy.png',
    'phys32_04_weyl_census.png',
    'phys32_05_af_balance.png',
    'phys32_06_critical_nf.png',
    'phys32_07_gap_shift.png',
    'phys32_08_oneloop_twoloop.png',
]

for i, name in enumerate(filenames, 1):
    print("  Fig %d: %s" % (i, name))
    