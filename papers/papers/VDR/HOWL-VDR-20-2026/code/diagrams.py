#!/usr/bin/env python3
"""
VDR-LLM-Prolog Complete System — Mechanical Explanation Diagrams
8 figures covering: VDR triple structure, Q335 arithmetic, token economics,
self-extension accumulation, safety architecture, confidence propagation,
and KB scoping.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

# ── Output directory ──────────────────────────────────────────────
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Color palette ─────────────────────────────────────────────────

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


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

def styled_box(ax, x, y, w, h, text, color, fontsize=10, textcolor=WHITE, alpha=0.85, zorder=3):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                         boxstyle="round,pad=0.15", facecolor=color, edgecolor=WHITE,
                         linewidth=1.5, alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=textcolor, fontweight='bold', zorder=zorder+1)

def styled_arrow(ax, x1, y1, x2, y2, color=SILVER, lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw))


# ================================================================
# FIG 1: VDR TRIPLE NESTING STRUCTURE
# Type: 4 (Geometric Cross-Section)
# Shows: The asymmetric [V,D,R] triple where only R recurses,
#        each child contained within parent's denominator frame.
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

fig.text(0.5, 0.95, 'VDR Triple: Nesting Through Remainder Only',
         ha='center', va='top', fontsize=17, fontweight='bold', color=GOLD)
fig.text(0.5, 0.91, 'V and D are always integers (sealed).  Only R recurses.  '
         'Each child is interpreted within parent\'s denominator frame.',
         ha='center', va='top', fontsize=11, color=SILVER)

# Level 0 — top triple
bw, bh = 18, 10
gap_x = 5
level0_y = 75
cx = 50
v0_x = cx - bw - gap_x
d0_x = cx
r0_x = cx + bw + gap_x

# V slot — sealed
styled_box(ax, v0_x, level0_y, bw, bh, 'V = 847', BLUE, fontsize=14)
ax.text(v0_x, level0_y + bh/2 + 2.5, 'VALUE (integer)', ha='center', va='bottom',
        fontsize=9, color=SILVER, style='italic')
# sealed indicator
ax.plot([v0_x - bw/2, v0_x + bw/2], [level0_y - bh/2 - 1.2, level0_y - bh/2 - 1.2],
        color=DIM, lw=2, solid_capstyle='round')
ax.text(v0_x, level0_y - bh/2 - 3, 'sealed', ha='center', va='top', fontsize=8, color=DIM)

# D slot — sealed
styled_box(ax, d0_x, level0_y, bw, bh, 'D = 1000', GREEN, fontsize=14)
ax.text(d0_x, level0_y + bh/2 + 2.5, 'DENOMINATOR (integer)', ha='center', va='bottom',
        fontsize=9, color=SILVER, style='italic')
ax.plot([d0_x - bw/2, d0_x + bw/2], [level0_y - bh/2 - 1.2, level0_y - bh/2 - 1.2],
        color=DIM, lw=2, solid_capstyle='round')
ax.text(d0_x, level0_y - bh/2 - 3, 'sealed', ha='center', va='top', fontsize=8, color=DIM)

# R slot — open, glowing
r_box = FancyBboxPatch((r0_x - bw/2, level0_y - bh/2), bw, bh,
                        boxstyle="round,pad=0.15", facecolor=ORANGE, edgecolor=GOLD,
                        linewidth=2.5, alpha=0.9, zorder=3)
ax.add_patch(r_box)
ax.text(r0_x, level0_y, 'R (active)', ha='center', va='center', fontsize=14,
        color=WHITE, fontweight='bold', zorder=4)
ax.text(r0_x, level0_y + bh/2 + 2.5, 'REMAINDER (recurses)', ha='center', va='bottom',
        fontsize=9, color=GOLD, style='italic')

# Bounding frame for level 0
frame0 = FancyBboxPatch((v0_x - bw/2 - 4, level0_y - bh/2 - 6), 
                         (r0_x + bw/2 + 4) - (v0_x - bw/2 - 4), bh + 12,
                         boxstyle="round,pad=0.3", facecolor='none', edgecolor=GOLD,
                         linewidth=1.5, linestyle='--', alpha=0.5, zorder=1)
ax.add_patch(frame0)
ax.text(v0_x - bw/2 - 2, level0_y + bh/2 + 6, 'Level 0:  [847, 1000, R]',
        ha='left', va='bottom', fontsize=10, color=GOLD, fontweight='bold')

# Shaft from R down to Level 1
shaft_top = level0_y - bh/2
shaft_bot = 48
ax.plot([r0_x, r0_x], [shaft_top - 1, shaft_bot + 6], color=GOLD, lw=2.5, alpha=0.7)
ax.annotate('', xy=(r0_x, shaft_bot + 6), xytext=(r0_x, shaft_bot + 12),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(r0_x + 3, (shaft_top + shaft_bot + 6) / 2, 'nests\ninto R',
        ha='left', va='center', fontsize=9, color=GOLD, alpha=0.8)

# Level 1 — child triple (smaller)
bw1, bh1 = 14, 8
level1_y = 43
cx1 = r0_x
v1_x = cx1 - bw1 - 3
d1_x = cx1
r1_x = cx1 + bw1 + 3

styled_box(ax, v1_x, level1_y, bw1, bh1, 'V = 3', BLUE, fontsize=12, alpha=0.7)
styled_box(ax, d1_x, level1_y, bw1, bh1, 'D = 7', GREEN, fontsize=12, alpha=0.7)

r1_box = FancyBboxPatch((r1_x - bw1/2, level1_y - bh1/2), bw1, bh1,
                          boxstyle="round,pad=0.15", facecolor=ORANGE, edgecolor=GOLD,
                          linewidth=2, alpha=0.7, zorder=3)
ax.add_patch(r1_box)
ax.text(r1_x, level1_y, 'R (active)', ha='center', va='center', fontsize=12,
        color=WHITE, fontweight='bold', zorder=4)

frame1 = FancyBboxPatch((v1_x - bw1/2 - 3, level1_y - bh1/2 - 4),
                         (r1_x + bw1/2 + 3) - (v1_x - bw1/2 - 3), bh1 + 8,
                         boxstyle="round,pad=0.3", facecolor='none', edgecolor=CYAN,
                         linewidth=1.2, linestyle='--', alpha=0.4, zorder=1)
ax.add_patch(frame1)
ax.text(v1_x - bw1/2 - 1, level1_y + bh1/2 + 4, 'Level 1:  [3, 7, R]',
        ha='left', va='bottom', fontsize=9, color=CYAN, fontweight='bold')
ax.text(v1_x - bw1/2 - 1, level1_y + bh1/2 + 1.5,
        'interpreted within parent D=1000',
        ha='left', va='bottom', fontsize=8, color=DIM, style='italic')

# Shaft from Level 1 R down to Level 2
shaft1_top = level1_y - bh1/2
shaft1_bot = 18
ax.plot([r1_x, r1_x], [shaft1_top - 1, shaft1_bot + 5], color=CYAN, lw=2, alpha=0.6)
ax.annotate('', xy=(r1_x, shaft1_bot + 5), xytext=(r1_x, shaft1_bot + 10),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

# Level 2 — closed (R=0)
bw2, bh2 = 12, 7
level2_y = 15
cx2 = r1_x
v2_x = cx2 - bw2 - 2.5
d2_x = cx2
r2_x = cx2 + bw2 + 2.5

styled_box(ax, v2_x, level2_y, bw2, bh2, 'V = 1', BLUE, fontsize=11, alpha=0.55)
styled_box(ax, d2_x, level2_y, bw2, bh2, 'D = 3', GREEN, fontsize=11, alpha=0.55)

# R=0 — closed, warm amber
r2_box = FancyBboxPatch((r2_x - bw2/2, level2_y - bh2/2), bw2, bh2,
                          boxstyle="round,pad=0.15", facecolor='#8B6914', edgecolor=GOLD,
                          linewidth=1.5, alpha=0.7, zorder=3)
ax.add_patch(r2_box)
ax.text(r2_x, level2_y, 'R = 0', ha='center', va='center', fontsize=11,
        color=WHITE, fontweight='bold', zorder=4)
ax.text(r2_x, level2_y - bh2/2 - 2.5, 'CLOSED', ha='center', va='top',
        fontsize=9, color=GOLD, fontweight='bold')

frame2 = FancyBboxPatch((v2_x - bw2/2 - 2.5, level2_y - bh2/2 - 5),
                         (r2_x + bw2/2 + 2.5) - (v2_x - bw2/2 - 2.5), bh2 + 8,
                         boxstyle="round,pad=0.3", facecolor='none', edgecolor=PURPLE,
                         linewidth=1, linestyle='--', alpha=0.35, zorder=1)
ax.add_patch(frame2)
ax.text(v2_x - bw2/2 - 1, level2_y + bh2/2 + 3, 'Level 2:  [1, 3, 0]  (closed)',
        ha='left', va='bottom', fontsize=9, color=PURPLE)

# Key insight annotation
ax.text(8, 50, 'V and D:\nalways integers\nnever nest\nnever recurse',
        ha='left', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.9))

ax.text(8, 28, 'Only R opens\ndownward.\n\nDepth = structure\nnot error.',
        ha='left', va='center', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax.text(8, 10, 'R=0 at bottom:\nresolved, exact\nrational 1/3',
        ha='left', va='center', fontsize=10, color=PURPLE,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=PURPLE, alpha=0.6))

save(fig, 'vdr_system_01_triple_nesting.png')


# ================================================================
# FIG 2: Q335 MULTIPLICATION — DIVMOD AT BIT 335
# Type: 7 (Progression/Sequence)
# Shows: How multiplication overflow becomes tree depth not
#        denominator growth. The split at bit 335 is the mechanism.
# ================================================================
fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

fig.text(0.5, 0.96, 'Q335 Multiplication: Overflow to Tree Depth, Not Denominator Growth',
         ha='center', va='top', fontsize=16, fontweight='bold', color=GOLD)

# Stage 1: Two Q335 operands
stage_y = 82
styled_box(ax, 25, stage_y, 22, 9, 'Numerator A\n(~102 digits)', BLUE, fontsize=10)
ax.text(25, stage_y + 6.5, 'Q335 operand', ha='center', va='bottom',
        fontsize=8, color=SILVER)
styled_box(ax, 75, stage_y, 22, 9, 'Numerator B\n(~102 digits)', CYAN, fontsize=10)
ax.text(75, stage_y + 6.5, 'Q335 operand', ha='center', va='bottom',
        fontsize=8, color=SILVER)
ax.text(50, stage_y, '\u00d7', ha='center', va='center', fontsize=22, color=GOLD,
        fontweight='bold')

# Arrow down
styled_arrow(ax, 50, stage_y - 5, 50, 67)

# Stage 2: Full product
stage2_y = 62
product_w = 50
product_box = FancyBboxPatch((50 - product_w/2, stage2_y - 5), product_w, 10,
                              boxstyle="round,pad=0.2", facecolor=PAN, edgecolor=ORANGE,
                              linewidth=2, alpha=0.9, zorder=3)
ax.add_patch(product_box)
ax.text(50, stage2_y, 'Full Product A \u00d7 B   (~204 digits,  ~670 bits)',
        ha='center', va='center', fontsize=11, color=ORANGE, fontweight='bold', zorder=4)
ax.text(50, stage2_y + 6.5, 'integer multiply: ~200 int ops (schoolbook 11\u00d711 limbs)',
        ha='center', va='bottom', fontsize=9, color=DIM)

# Arrow down to split
styled_arrow(ax, 50, stage2_y - 5.5, 50, 48)
ax.text(53, 51, 'divmod at\nbit 335', ha='left', va='center', fontsize=10,
        color=GOLD, fontweight='bold')

# Stage 3: The split — the key visual
split_y = 40
split_left = 15
split_right = 85
bit_335 = 50

# Left half (bits above 335) → new V
left_box = FancyBboxPatch((split_left, split_y - 5), bit_335 - split_left - 2, 10,
                           boxstyle="round,pad=0.2", facecolor=BLUE, edgecolor=WHITE,
                           linewidth=1.5, alpha=0.75, zorder=3)
ax.add_patch(left_box)
ax.text((split_left + bit_335 - 2) / 2, split_y,
        'bits above 335\n\u2192 new V (quotient)',
        ha='center', va='center', fontsize=11, color=WHITE, fontweight='bold', zorder=4)

# Right half (bits below 335) → R
right_box = FancyBboxPatch((bit_335 + 2, split_y - 5), split_right - bit_335 - 2, 10,
                            boxstyle="round,pad=0.2", facecolor=ORANGE, edgecolor=GOLD,
                            linewidth=2, alpha=0.75, zorder=3)
ax.add_patch(right_box)
ax.text((bit_335 + 2 + split_right) / 2, split_y,
        'bits below 335\n\u2192 R (remainder)',
        ha='center', va='center', fontsize=11, color=WHITE, fontweight='bold', zorder=4)

# Bit 335 dividing line
ax.plot([bit_335, bit_335], [split_y - 7, split_y + 7], color=GOLD, lw=3, zorder=5)
ax.text(bit_335, split_y + 8.5, 'BIT 335', ha='center', va='bottom',
        fontsize=11, color=GOLD, fontweight='bold')

# Stage 4: Result triple
result_y = 20
styled_box(ax, 25, result_y, 22, 9, 'V = quotient', BLUE, fontsize=11)
styled_box(ax, 50, result_y, 22, 9, 'D = 2\u00b3\u00b3\u2075\n(unchanged)', GREEN, fontsize=10)
r_result = FancyBboxPatch((75 - 11, result_y - 4.5), 22, 9,
                           boxstyle="round,pad=0.15", facecolor=ORANGE, edgecolor=GOLD,
                           linewidth=2, alpha=0.85, zorder=3)
ax.add_patch(r_result)
ax.text(75, result_y, 'R = remainder\n(nests deeper)', ha='center', va='center',
        fontsize=10, color=WHITE, fontweight='bold', zorder=4)

# Arrows from split to result
styled_arrow(ax, 32, split_y - 5.5, 25, result_y + 5)
styled_arrow(ax, 68, split_y - 5.5, 75, result_y + 5)

# Frame around result
result_frame = FancyBboxPatch((10, result_y - 7), 80, 14,
                               boxstyle="round,pad=0.3", facecolor='none', edgecolor=GOLD,
                               linewidth=1.2, linestyle='--', alpha=0.4, zorder=1)
ax.add_patch(result_frame)
ax.text(50, result_y - 8.5, 'Result: [V, 2\u00b3\u00b3\u2075, R]  —  D never grows.  '
        'Overflow \u2192 tree depth.',
        ha='center', va='top', fontsize=11, color=GOLD, fontweight='bold')

# Key insight boxes
ax.text(8, 10, 'Denominator fixed forever.\n'
        'Growth goes to R depth,\nnot D magnitude.',
        ha='left', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN, alpha=0.7))

ax.text(92, 10, '~200 int ops per multiply.\nPerfectly uniform.\nPeak GPU utilization.',
        ha='right', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN, alpha=0.7))

save(fig, 'vdr_system_02_q335_divmod.png')


# ================================================================
# FIG 3: CONVERSATION SCALING — QUADRATIC VS FLAT
# Type: 1 (Running/Convergence Chart)
# Shows: Conventional cumulative cost growing quadratically vs
#        VDR growing linearly. The divergence IS the economic argument.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(PAN)

turns = np.array([1, 5, 10, 20, 50, 100])
conv_cumul = np.array([6000, 60000, 195000, 690000, 3900000, 15300000])
vdr_cumul = np.array([260, 1300, 2600, 5200, 13000, 26000])
ratio = conv_cumul / vdr_cumul

ax.semilogy(turns, conv_cumul, 'o-', color=RED, lw=2.5, markersize=10,
            markeredgecolor=WHITE, markeredgewidth=1.5, label='Conventional (quadratic)',
            zorder=5)
ax.semilogy(turns, vdr_cumul, 's-', color=GREEN, lw=2.5, markersize=10,
             markeredgecolor=WHITE, markeredgewidth=1.5, label='VDR (linear)',
             zorder=5)

# Ratio annotations
offsets_x = [2, 3, 3, 4, 5, 5]
for i in range(len(turns)):
    mid = np.sqrt(conv_cumul[i] * vdr_cumul[i])
    ax.text(turns[i] + offsets_x[i], mid, '%d:1' % int(ratio[i]),
            ha='left', va='center', fontsize=10, color=GOLD, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.7))

# Data labels on curves
conv_offsets_y = [1.8, 1.6, 1.5, 1.5, 1.4, 1.4]
for i in range(len(turns)):
    ax.text(turns[i], conv_cumul[i] * conv_offsets_y[i], '{:,.0f}'.format(conv_cumul[i]),
            ha='center', va='bottom', fontsize=8, color=RED, alpha=0.8)
    ax.text(turns[i], vdr_cumul[i] * 0.5, '{:,.0f}'.format(vdr_cumul[i]),
            ha='center', va='top', fontsize=8, color=GREEN, alpha=0.8)

ax.set_xlabel('Conversation Turn', fontsize=12, color=SILVER)
ax.set_ylabel('Cumulative Tokens (log scale)', fontsize=12, color=SILVER)
ax.set_title('Conversation Cost Scaling: Quadratic vs Linear',
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='upper left')

ax.set_xlim(-3, 108)
ax.set_ylim(100, 50000000)
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.grid(True, alpha=0.15, color=DIM)

# Key insight
ax.text(70, 300, 'VDR: state in KBs at integer addresses.\n'
        'Each turn costs the same.\n'
        'Turn 100 = Turn 1.',
        fontsize=10, color=GREEN, ha='left', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN, alpha=0.7))

ax.text(70, 8000000, 'Conventional: each turn re-reads\n'
        'all prior history through attention.\n'
        'Cost grows quadratically.',
        fontsize=10, color=RED, ha='left', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED, alpha=0.7))

save(fig, 'vdr_system_03_scaling_quadratic_vs_flat.png')


# ================================================================
# FIG 4: SRE ACCUMULATION — TOKENS FALLING, RULES RISING
# Type: 1 (Running/Convergence Chart)
# Shows: The crossing curves of decreasing cost and increasing
#        automated rules — self-extension made visual.
# ================================================================
fig, ax1 = plt.subplots(figsize=(16, 10), facecolor=BG)
ax1.set_facecolor(PAN)

investigations = np.array([1, 2, 5, 10, 20, 50])
tokens_per = np.array([329, 127, 110, 92, 78, 65])
rules_firing = np.array([0, 7, 18, 47, 72, 115])
auto_pct = np.array([0, 25, 45, 65, 78, 88])

color_tok = CYAN
color_rules = ORANGE

ax1.plot(investigations, tokens_per, 'o-', color=color_tok, lw=2.5, markersize=10,
         markeredgecolor=WHITE, markeredgewidth=1.5, label='Tokens per investigation', zorder=5)

for i in range(len(investigations)):
    ax1.text(investigations[i], tokens_per[i] + 12, str(tokens_per[i]),
             ha='center', va='bottom', fontsize=9, color=color_tok, fontweight='bold')

ax1.set_xlabel('Investigation Number', fontsize=12, color=SILVER)
ax1.set_ylabel('Command Tokens per Investigation', fontsize=12, color=color_tok)
ax1.tick_params(axis='y', labelcolor=color_tok, colors=DIM, labelsize=9)
ax1.tick_params(axis='x', colors=DIM, labelsize=9)
ax1.set_xlim(-2, 55)
ax1.set_ylim(0, 400)

ax2 = ax1.twinx()
ax2.plot(investigations, rules_firing, 's-', color=color_rules, lw=2.5, markersize=10,
         markeredgecolor=WHITE, markeredgewidth=1.5, label='Rules firing automatically', zorder=5)

for i in range(len(investigations)):
    y_off = -12 if i > 0 else 8
    va = 'top' if i > 0 else 'bottom'
    ax2.text(investigations[i], rules_firing[i] + y_off, str(rules_firing[i]),
             ha='center', va=va, fontsize=9, color=color_rules, fontweight='bold')

ax2.set_ylabel('Rules Firing Automatically', fontsize=12, color=color_rules)
ax2.tick_params(axis='y', labelcolor=color_rules, colors=DIM, labelsize=9)
ax2.set_ylim(0, 150)

# Auto-triage percentage annotations
for i in range(len(investigations)):
    ax1.text(investigations[i], 380, '%d%% auto' % auto_pct[i],
             ha='center', va='top', fontsize=8, color=GOLD, alpha=0.8)

ax1.set_title('Self-Extension: Tokens Fall as Rules Accumulate',
              fontsize=16, fontweight='bold', color=GOLD, pad=15)

for spine in ax1.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
for spine in ax2.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax1.grid(True, alpha=0.15, color=DIM)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='center right')

# Key insight
ax1.text(30, 300, 'Each session deposits rules and scripts.\n'
         'Known patterns handled by rules.\n'
         'LLM judges only what\'s genuinely new.\n'
         'Usage IS training.',
         fontsize=10, color=SILVER, ha='left', va='top',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.7))

save(fig, 'vdr_system_04_sre_accumulation.png')


# ================================================================
# FIG 5: TOKEN CATEGORY ELIMINATION — SIX TO ZERO
# Type: 6 (Comparison Bar Chart)
# Shows: Six infrastructure token categories collapsing to zero
#        in VDR, leaving only judgment + prose + commands.
# ================================================================
fig, (ax_conv, ax_vdr) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                       gridspec_kw={'wspace': 0.35})

categories = ['State\nReconstruct', 'Computation', 'Deduction', 'Formatting',
              'Hedging', 'Judgment', 'Prose', 'Command\nTokens']
conv_pct = [15, 20, 15, 20, 10, 10, 10, 0]
vdr_pct =  [0,  0,  0,  0,  0, 10, 10, 5]

colors_conv = [RED, RED, RED, RED, RED, GREEN, GREEN, DIM]
colors_vdr =  [DIM, DIM, DIM, DIM, DIM, GREEN, GREEN, CYAN]

# Conventional panel
bars_conv = ax_conv.barh(range(len(categories)), conv_pct, color=colors_conv,
                          alpha=0.7, edgecolor=[c if p > 0 else DIM for c, p in zip(colors_conv, conv_pct)],
                          linewidth=1.5, height=0.65)
ax_conv.set_yticks(range(len(categories)))
ax_conv.set_yticklabels(categories, fontsize=10, color=WHITE)
ax_conv.set_xlabel('% of Generated Tokens', fontsize=11, color=SILVER)
ax_conv.set_title('Conventional LLM', fontsize=14, fontweight='bold', color=RED, pad=12)
ax_conv.set_xlim(0, 28)
ax_conv.set_facecolor(PAN)
ax_conv.tick_params(colors=DIM, labelsize=9)
for spine in ax_conv.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

for i, v in enumerate(conv_pct):
    if v > 0:
        ax_conv.text(v + 0.8, i, '%d%%' % v, ha='left', va='center',
                     fontsize=10, color=colors_conv[i], fontweight='bold')

# Label infrastructure
ax_conv.text(14, 2, 'INFRASTRUCTURE\n80-95% of tokens',
             ha='center', va='center', fontsize=10, color=RED,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.7))

# VDR panel
bars_vdr = ax_vdr.barh(range(len(categories)), vdr_pct, color=colors_vdr,
                         alpha=0.7, edgecolor=[c if p > 0 else DIM for c, p in zip(colors_vdr, vdr_pct)],
                         linewidth=1.5, height=0.65)
ax_vdr.set_yticks(range(len(categories)))
ax_vdr.set_yticklabels(categories, fontsize=10, color=WHITE)
ax_vdr.set_xlabel('% of Generated Tokens', fontsize=11, color=SILVER)
ax_vdr.set_title('VDR-LLM-Prolog', fontsize=14, fontweight='bold', color=GREEN, pad=12)
ax_vdr.set_xlim(0, 28)
ax_vdr.set_facecolor(PAN)
ax_vdr.tick_params(colors=DIM, labelsize=9)
for spine in ax_vdr.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

for i, v in enumerate(vdr_pct):
    if v > 0:
        ax_vdr.text(v + 0.8, i, '%d%%' % v, ha='left', va='center',
                    fontsize=10, color=colors_vdr[i], fontweight='bold')
    else:
        ax_vdr.text(0.8, i, '0', ha='left', va='center',
                    fontsize=9, color=DIM)

# "Eliminated" annotations on zero bars
for i in range(5):
    ax_vdr.text(14, i, 'ELIMINATED', ha='center', va='center',
                fontsize=8, color=DIM, style='italic', alpha=0.6)

# What handles each eliminated category
handlers = ['KB query', 'primitives', 'Prolog', 'grammar', 'exact confidence']
for i in range(5):
    ax_vdr.text(24, i, handlers[i], ha='right', va='center',
                fontsize=8, color=SILVER, alpha=0.7)

fig.suptitle('Token Category Elimination: Infrastructure to Zero',
             fontsize=16, fontweight='bold', color=GOLD, y=0.98)

save(fig, 'vdr_system_05_token_elimination.png')


# ================================================================
# FIG 6: THREE SAFETY LAYERS — CONCENTRIC RINGS
# Type: 4 (Geometric Cross-Section)
# Shows: Defense in depth as nesting geometry. Attacks stop at
#        different rings. LLM contained in center, receiving
#        only pre-filtered data.
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(-60, 60)
ax.set_ylim(-55, 55)
ax.set_aspect('equal')
ax.axis('off')

fig.text(0.5, 0.96, 'Structural Safety: Three Independent Layers',
         ha='center', va='top', fontsize=17, fontweight='bold', color=GOLD)
fig.text(0.5, 0.92, 'All three must fail simultaneously for a breach.  '
         'Each is deterministic integer operations.',
         ha='center', va='top', fontsize=11, color=SILVER)

# Layer 1 — outermost: Input Filtering (visibility + scope)
ring1 = plt.Circle((0, 0), 42, facecolor=BLUE, edgecolor=WHITE,
                    linewidth=2, alpha=0.08, zorder=1)
ax.add_patch(ring1)
ring1_edge = plt.Circle((0, 0), 42, facecolor='none', edgecolor=BLUE,
                          linewidth=2.5, alpha=0.6, zorder=2)
ax.add_patch(ring1_edge)
ax.text(0, 44, 'LAYER 1: INPUT FILTERING', ha='center', va='bottom',
        fontsize=12, color=BLUE, fontweight='bold')
ax.text(0, -44, 'KB visibility (integer comparison) + scope chain (ancestor walk)',
        ha='center', va='top', fontsize=9, color=BLUE, alpha=0.8)

# Layer 2 — middle: Grant System
ring2 = plt.Circle((0, 0), 28, facecolor=GREEN, edgecolor=WHITE,
                    linewidth=2, alpha=0.1, zorder=3)
ax.add_patch(ring2)
ring2_edge = plt.Circle((0, 0), 28, facecolor='none', edgecolor=GREEN,
                          linewidth=2.5, alpha=0.6, zorder=4)
ax.add_patch(ring2_edge)
ax.text(0, 30, 'LAYER 2: GRANTS', ha='center', va='bottom',
        fontsize=11, color=GREEN, fontweight='bold')
ax.text(0, -30, 'Default denial.  Set membership check.',
        ha='center', va='top', fontsize=9, color=GREEN, alpha=0.8)

# Layer 3 — inner: Output Validation
ring3 = plt.Circle((0, 0), 16, facecolor=ORANGE, edgecolor=WHITE,
                    linewidth=2, alpha=0.12, zorder=5)
ax.add_patch(ring3)
ring3_edge = plt.Circle((0, 0), 16, facecolor='none', edgecolor=ORANGE,
                          linewidth=2.5, alpha=0.6, zorder=6)
ax.add_patch(ring3_edge)
ax.text(0, 18, 'LAYER 3: OUTPUT', ha='center', va='bottom',
        fontsize=10, color=ORANGE, fontweight='bold')

# LLM in center
llm_circle = plt.Circle((0, 0), 7, facecolor=PAN, edgecolor=GOLD,
                          linewidth=2.5, alpha=0.95, zorder=7)
ax.add_patch(llm_circle)
ax.text(0, 0, 'LLM\n(untrusted)', ha='center', va='center', fontsize=11,
        color=GOLD, fontweight='bold', zorder=8)

# Attack arrows stopping at different rings
attacks = [
    (52, 25, 'Prompt injection', BLUE, 42),
    (52, 10, 'Role-play attack', BLUE, 42),
    (52, -5, 'Many-shot bypass', BLUE, 42),
    (52, -20, 'Encoding tricks', BLUE, 42),
    (-52, 20, 'Unauthorized op', GREEN, 28),
    (-52, 0, 'No grant = denied', GREEN, 28),
    (-52, -20, 'Training-derived\nharmful content', ORANGE, 16),
]

for atk_x, atk_y, label, color, stop_r in attacks:
    direction = -1 if atk_x > 0 else 1
    angle = np.arctan2(atk_y, direction * 1)
    stop_x = direction * stop_r * np.cos(np.arctan2(atk_y, abs(atk_x)))
    stop_y = stop_r * np.sin(np.arctan2(atk_y, abs(atk_x)))
    norm = np.sqrt(stop_x**2 + stop_y**2)
    if norm > 0:
        stop_x = stop_x / norm * stop_r
        stop_y = stop_y / norm * stop_r

    ax.annotate('', xy=(stop_x * 0.98, stop_y * 0.98),
                xytext=(atk_x, atk_y),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2, alpha=0.6))
    # X mark at stop point
    ax.plot(stop_x, stop_y, 'x', color=RED, markersize=12, markeredgewidth=3, zorder=10)

    # Label
    label_x = atk_x + (3 if atk_x > 0 else -3)
    ax.text(label_x, atk_y, label, ha='left' if atk_x > 0 else 'right',
            va='center', fontsize=9, color=SILVER,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.8))

# Bottom key insight
ax.text(0, -50, 'No prompt modifies any integer in any access check.  '
        'Attack surface does not exist for data access.',
        ha='center', va='top', fontsize=11, color=GOLD, fontweight='bold')

save(fig, 'vdr_system_06_safety_layers.png')


# ================================================================
# FIG 7: CONFIDENCE PROPAGATION CHAIN
# Type: 7 (Progression/Sequence)
# Shows: Exact VDR fractions degrading through a derivation chain
#        with formulas at each step.
# ================================================================
fig, ax = plt.subplots(figsize=(18, 11), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

fig.text(0.5, 0.96, 'Confidence Propagation: Exact VDR Fractions Through Derivation',
         ha='center', va='top', fontsize=16, fontweight='bold', color=GOLD)
fig.text(0.5, 0.92, 'Every step has a declared formula.  '
         'Confidence is computed, not generated as hedging language.',
         ha='center', va='top', fontsize=11, color=SILVER)

# Chain steps going left to right, top row then bottom row
steps = [
    {'x': 12, 'y': 72, 'label': 'Prometheus\nMetric', 'conf': '95/100',
     'color': CYAN, 'formula': 'source default'},
    {'x': 35, 'y': 72, 'label': 'DB Query\nResult', 'conf': '98/100',
     'color': BLUE, 'formula': 'source default'},
    {'x': 58, 'y': 72, 'label': 'Two Sources\nAgree', 'conf': '999/1000',
     'color': GREEN, 'formula': '1-(1-95/100)(1-98/100)'},
    {'x': 81, 'y': 72, 'label': 'Prolog\nDerivation', 'conf': '999/1000',
     'color': GREEN, 'formula': 'min(premises) = 999/1000'},
    {'x': 20, 'y': 38, 'label': 'Python\nScript', 'conf': '949/1000',
     'color': ORANGE, 'formula': 'min(inputs) \u00d7 95/100'},
    {'x': 50, 'y': 38, 'label': 'LLM\nAssessment', 'conf': '30/100',
     'color': MAG, 'formula': '30/100 (fixed floor)'},
    {'x': 80, 'y': 38, 'label': 'Final\nConclusion', 'conf': '30/100',
     'color': GOLD, 'formula': 'min across chain'},
]

bw, bh = 18, 12
for step in steps:
    x, y = step['x'], step['y']
    color = step['color']

    box = FancyBboxPatch((x - bw/2, y - bh/2), bw, bh,
                          boxstyle="round,pad=0.2", facecolor=PAN,
                          edgecolor=color, linewidth=2, alpha=0.9, zorder=3)
    ax.add_patch(box)

    ax.text(x, y + 2, step['label'], ha='center', va='center',
            fontsize=10, color=WHITE, fontweight='bold', zorder=4)
    ax.text(x, y - 3.5, step['conf'], ha='center', va='center',
            fontsize=13, color=color, fontweight='bold', zorder=4)

# Formula labels below each box
formula_y_top = 63
formula_y_bot = 29
for i, step in enumerate(steps):
    fy = formula_y_top if step['y'] > 50 else formula_y_bot
    ax.text(step['x'], fy, step['formula'], ha='center', va='top',
            fontsize=8, color=DIM, style='italic')

# Arrows between steps — top row
for i in range(3):
    x1 = steps[i]['x'] + bw/2 + 0.5
    x2 = steps[i+1]['x'] - bw/2 - 0.5
    y = steps[i]['y']
    styled_arrow(ax, x1, y, x2, y, color=SILVER, lw=1.5)

# Arrow from top row to bottom row
styled_arrow(ax, steps[3]['x'], steps[3]['y'] - bh/2 - 0.5, steps[4]['x'], steps[4]['y'] + bh/2 + 0.5, color=SILVER)

# Arrows bottom row
styled_arrow(ax, steps[4]['x'] + bw/2 + 0.5, steps[4]['y'], steps[5]['x'] - bw/2 - 0.5, steps[5]['y'], color=SILVER)
styled_arrow(ax, steps[5]['x'] + bw/2 + 0.5, steps[5]['y'], steps[6]['x'] - bw/2 - 0.5, steps[6]['y'], color=SILVER)

# Confidence bar at bottom
bar_y = 12
bar_left = 10
bar_right = 90
ax.plot([bar_left, bar_right], [bar_y, bar_y], color=DIM, lw=3, alpha=0.4)

# Confidence thresholds
thresholds = [
    (10, '<40/100', 'Unreliable', RED),
    (30, '40-59', 'Speculative', ORANGE),
    (50, '60-79', 'Low', SILVER),
    (70, '80-94', 'Moderate', CYAN),
    (85, '95-100', 'High', GREEN),
]
for tx, trange, tlabel, tcolor in thresholds:
    ax.plot([tx, tx], [bar_y - 2, bar_y + 2], color=tcolor, lw=2, alpha=0.7)
    ax.text(tx, bar_y + 3.5, tlabel, ha='center', va='bottom',
            fontsize=8, color=tcolor, fontweight='bold')
    ax.text(tx, bar_y - 3.5, trange, ha='center', va='top',
            fontsize=7, color=DIM)

# Mark where final conclusion lands
ax.plot(30, bar_y, 'v', color=GOLD, markersize=15, zorder=10)
ax.text(30, bar_y + 6.5, 'Final: 30/100\n(LLM floor\ndominates chain)',
        ha='center', va='bottom', fontsize=9, color=GOLD, fontweight='bold')

# Key insight
ax.text(5, 20, 'Weakest link\ndetermines chain.\n\nLLM step at 30/100\ncaps everything\ndownstream.',
        ha='left', va='center', fontsize=9, color=MAG,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=MAG, alpha=0.7))

save(fig, 'vdr_system_07_confidence_chain.png')


# ================================================================
# FIG 8: KB TREE SCOPING WITH SIBLING ISOLATION
# Type: 4 (Geometric Cross-Section)
# Shows: The ancestor walk with severed siblings. Why the engineer
#        structurally cannot see HR data.
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

fig.text(0.5, 0.96, 'KB Tree Scoping: Ancestor Walk, Sibling Isolation',
         ha='center', va='top', fontsize=17, fontweight='bold', color=GOLD)
fig.text(0.5, 0.92, 'Query searches active topic \u2192 parent \u2192 root.  '
         'Sibling branches are structurally unreachable.',
         ha='center', va='top', fontsize=11, color=SILVER)

# Tree structure
nodes = {
    'root':       {'x': 50, 'y': 85, 'label': 'root', 'vis': 'public'},
    'org':        {'x': 50, 'y': 72, 'label': 'org.acme', 'vis': 'internal'},
    'engineering':{'x': 30, 'y': 57, 'label': 'engineering', 'vis': 'internal'},
    'hr':         {'x': 70, 'y': 57, 'label': 'hr', 'vis': 'internal'},
    'platform':   {'x': 20, 'y': 42, 'label': 'platform', 'vis': 'internal'},
    'backend':    {'x': 40, 'y': 42, 'label': 'backend', 'vis': 'internal'},
    'recruiting': {'x': 62, 'y': 42, 'label': 'recruiting', 'vis': 'internal'},
    'personnel':  {'x': 78, 'y': 42, 'label': 'personnel', 'vis': 'owner_only'},
}

edges = [
    ('root', 'org'), ('org', 'engineering'), ('org', 'hr'),
    ('engineering', 'platform'), ('engineering', 'backend'),
    ('hr', 'recruiting'), ('hr', 'personnel'),
]

# Which nodes are in the engineer's scope chain
in_scope = {'root', 'org', 'engineering', 'platform'}
user_node = 'platform'

# Draw edges
for parent, child in edges:
    px, py = nodes[parent]['x'], nodes[parent]['y']
    cx, cy = nodes[child]['x'], nodes[child]['y']

    if parent in in_scope and child in in_scope:
        ax.plot([px, cx], [py - 3, cy + 4], color=GREEN, lw=2.5, alpha=0.8, zorder=2)
    else:
        ax.plot([px, cx], [py - 3, cy + 4], color=DIM, lw=1.5, alpha=0.3,
                linestyle='--', zorder=1)

# Draw nodes
for name, node in nodes.items():
    x, y = node['x'], node['y']
    if name in in_scope:
        color = GREEN
        edge = WHITE
        alpha = 0.9
    elif name in ('hr', 'recruiting', 'personnel'):
        color = RED
        edge = RED
        alpha = 0.4
    else:
        color = DIM
        edge = DIM
        alpha = 0.4

    nw, nh = 16, 6.5
    box = FancyBboxPatch((x - nw/2, y - nh/2), nw, nh,
                          boxstyle="round,pad=0.2", facecolor=PAN if name not in in_scope else color,
                          edgecolor=edge, linewidth=2 if name in in_scope else 1,
                          alpha=alpha, zorder=3)
    ax.add_patch(box)

    text_color = WHITE if name in in_scope else DIM
    ax.text(x, y + 0.5, node['label'], ha='center', va='center',
            fontsize=10, color=text_color, fontweight='bold', zorder=4)
    ax.text(x, y - 2, node['vis'], ha='center', va='center',
            fontsize=7, color=SILVER if name in in_scope else DIM, zorder=4)

# User marker
ux, uy = nodes[user_node]['x'], nodes[user_node]['y']
ax.plot(ux, uy - 5, '^', color=GOLD, markersize=18, zorder=10,
        markeredgecolor=WHITE, markeredgewidth=1.5)
ax.text(ux, uy - 8, 'ALICE\n(engineer)', ha='center', va='top',
        fontsize=10, color=GOLD, fontweight='bold')

# Scope chain arrow (upward)
scope_path = ['platform', 'engineering', 'org', 'root']
for i in range(len(scope_path) - 1):
    n1 = nodes[scope_path[i]]
    n2 = nodes[scope_path[i+1]]
    mid_x = (n1['x'] + n2['x']) / 2
    mid_y = (n1['y'] + n2['y']) / 2
    ax.text(mid_x - 9, mid_y, '%d' % (i+1), ha='center', va='center',
            fontsize=12, color=GREEN, fontweight='bold',
            bbox=dict(boxstyle='circle,pad=0.3', facecolor=BG, edgecolor=GREEN))

# Severed connection visual — X marks between engineering and hr
sever_x = 50
sever_y = 57
ax.plot(sever_x, sever_y, 'X', color=RED, markersize=25, markeredgewidth=3, zorder=10)
ax.text(sever_x, sever_y - 5.5, 'SIBLING\nUNREACHABLE',
        ha='center', va='top', fontsize=9, color=RED, fontweight='bold')

# Explanation boxes
# What Alice can see
ax.text(5, 30, "Alice's scope chain:\n"
        "1. platform (own KB)\n"
        "2. engineering (parent)\n"
        "3. org.acme (grandparent)\n"
        "4. root (always)\n\n"
        "Walk goes UP only.\nNever sideways.",
        ha='left', va='top', fontsize=10, color=GREEN,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=GREEN, alpha=0.7))

# What Alice cannot see
ax.text(95, 30, "hr branch:\n"
        "Not deprioritized.\n"
        "Not filtered.\n"
        "Structurally ABSENT.\n\n"
        "Scope walk doesn't\ngo sideways.\n\n"
        "personnel: owner_only\n"
        "\u2192 even HR recruiter\n"
        "   can't see salaries.",
        ha='right', va='top', fontsize=10, color=RED,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=RED, alpha=0.7))

# Bottom: the key invariant
ax.text(50, 5, 'Prompt injection cannot change session_id.  '
        'Role-play cannot change scope chain.  '
        'Both are integer operations in the primitive layer.',
        ha='center', va='bottom', fontsize=10, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.7))

save(fig, 'vdr_system_08_kb_scoping.png')


# ── Summary ───────────────────────────────────────────────────────
print("\n=== VDR System Diagrams Complete ===")
filenames = [
    'vdr_system_01_triple_nesting.png',
    'vdr_system_02_q335_divmod.png',
    'vdr_system_03_scaling_quadratic_vs_flat.png',
    'vdr_system_04_sre_accumulation.png',
    'vdr_system_05_token_elimination.png',
    'vdr_system_06_safety_layers.png',
    'vdr_system_07_confidence_chain.png',
    'vdr_system_08_kb_scoping.png',
]
for f in filenames:
    print("  %s" % f)
print("Total: %d figures" % len(filenames))
