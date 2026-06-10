

#!/usr/bin/env python3
"""
HOWL MATH-14 Diagrams — A Mathematical Theory of Processing: Formalizing What Shannon Excluded
8 figures covering the four-state framework, reduction, dissolution, cascade, and the Shannon bridge.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================



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
    
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


def style_ax(ax, xlabel='', ylabel='', title=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=10)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=20)


# ================================================================
# FIG 1: REDUCTION CONVERGENCE CURVE WITH ACTIONABILITY THRESHOLD
# Type: Running/Convergence Chart (Type 1)
# Shows: The SHAPE of reduction — steep early compression, diminishing
#        returns, the crossing point where actionability is reached,
#        and the over-reduction zone below threshold. Text cannot
#        convey that optimality is a crossing point on a curve.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='Reduction Steps (k)', ylabel='Information Volume',
         title='Reduction Convergence and the Actionability Threshold')

steps = np.linspace(0, 14, 300)
info_volume = 100.0 * np.exp(-0.35 * steps) + 5.0 * np.exp(-0.08 * steps)

actionability_upper = 18.0
actionability_lower = 8.0

ax.plot(steps, info_volume, color=CYAN, linewidth=2.5, label='Information volume during reduction')

ax.axhspan(actionability_lower, actionability_upper, color=GREEN, alpha=0.10)
ax.axhline(y=actionability_upper, color=GREEN, linewidth=1.5, linestyle='--', alpha=0.6)
ax.axhline(y=actionability_lower, color=ORANGE, linewidth=1.5, linestyle='--', alpha=0.6)

cross_upper = np.interp(actionability_upper, info_volume[::-1], steps[::-1])
cross_lower = np.interp(actionability_lower, info_volume[::-1], steps[::-1])

ax.fill_between(steps, 0, info_volume, where=(steps < cross_upper),
                color=RED, alpha=0.06)
ax.fill_between(steps, 0, info_volume, where=(steps > cross_lower),
                color=RED, alpha=0.06)

ax.scatter([cross_upper], [actionability_upper], s=200, color=GREEN,
           edgecolors=WHITE, linewidth=2, zorder=5)
ax.scatter([cross_lower], [actionability_lower], s=200, color=ORANGE,
           edgecolors=WHITE, linewidth=2, zorder=5)

ax.annotate('R* — Optimal reduction\n(minimum k for actionability)',
            xy=(cross_upper, actionability_upper),
            xytext=(cross_upper + 2.5, actionability_upper + 22),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

ax.annotate('Over-reduction boundary\n(actionability destroyed)',
            xy=(cross_lower, actionability_lower),
            xytext=(cross_lower + 2.0, actionability_lower + 18),
            color=ORANGE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

ax.text(cross_upper * 0.35, 70, 'INSUFFICIENT\nCannot act —\nstill at N',
        color=RED, fontsize=11, ha='center', alpha=0.8,
        fontstyle='italic')

mid_x = (cross_upper + cross_lower) / 2.0
ax.text(mid_x, 13.0, 'OPTIMAL\nWINDOW',
        color=GREEN, fontsize=12, ha='center', fontweight='bold', alpha=0.9)

ax.text(13.0, 3.5, 'OVER-REDUCED\nInformation lost',
        color=ORANGE, fontsize=10, ha='center', alpha=0.8,
        fontstyle='italic')

ax.annotate('A(r_k, g) = true\n(actionability threshold)',
            xy=(1.0, actionability_upper),
            xytext=(1.0, actionability_upper + 8),
            color=GREEN, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.0))

ax.set_xlim(-0.5, 15)
ax.set_ylim(-2, 115)

legend = ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

save(fig, 'math14_01_reduction_convergence.png')


# ================================================================
# FIG 2: CASCADE SEVERITY — SIMULTANEOUS PROMOTIONS VS PIPELINE
# Type: Progression/Sequence Diagram (Type 7)
# Shows: Elements at 0a before event, the triggering event, simultaneous
#        promotion to 1, and the pipeline constraint of 1. The visual
#        of multiple bars demanding one slot shows overload spatially.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, xlabel='Time', ylabel='',
         title='Cascade Severity: Simultaneous 0a \u2192 1 Promotions Exceed Pipeline Capacity')

elements = ['Lane keeping', 'Steering', 'Speed mgmt', 'Mirror checks', 'Following dist.']
n_elem = len(elements)

event_t = 5.0
pre_start = 0.5
pre_end = event_t
post_start = event_t + 0.15
post_end = 9.5

bar_height = 0.55
y_positions = np.array([i * 1.8 + 1.5 for i in range(n_elem)])

colors_0a = [BLUE, CYAN, GREEN, PURPLE, SILVER]
colors_1 = [RED, RED, RED, RED, DIM]
promoted = [True, True, True, True, False]

for i in range(n_elem):
    y = y_positions[i]
    ax.barh(y, pre_end - pre_start, left=pre_start, height=bar_height,
            color=colors_0a[i], alpha=0.5, edgecolor=colors_0a[i], linewidth=1.5)
    ax.text(pre_start + 0.3, y, '0a', color=WHITE, fontsize=10,
            fontweight='bold', va='center')

    if promoted[i]:
        ax.barh(y, post_end - post_start, left=post_start, height=bar_height,
                color=RED, alpha=0.6, edgecolor=RED, linewidth=1.5)
        ax.text(post_start + 0.3, y, '1', color=WHITE, fontsize=10,
                fontweight='bold', va='center')
    else:
        ax.barh(y, post_end - post_start, left=post_start, height=bar_height,
                color=colors_0a[i], alpha=0.5, edgecolor=colors_0a[i], linewidth=1.5)
        ax.text(post_start + 0.3, y, '0a', color=WHITE, fontsize=10,
                fontweight='bold', va='center')

    ax.text(pre_start - 0.4, y, elements[i], color=SILVER, fontsize=10,
            ha='right', va='center')

ax.axvline(x=event_t, color=ORANGE, linewidth=2.5, linestyle='-', alpha=0.9)
ax.text(event_t, y_positions[-1] + 1.6, 'EVENT: Bee enters car',
        color=ORANGE, fontsize=12, fontweight='bold', ha='center')

pipeline_y = -0.8
ax.barh(pipeline_y, post_end - post_start, left=post_start, height=bar_height,
        color=GOLD, alpha=0.3, edgecolor=GOLD, linewidth=2.0)
ax.text(post_start + 0.3, pipeline_y, 'Pipeline capacity = 1',
        color=GOLD, fontsize=10, fontweight='bold', va='center')
ax.barh(pipeline_y - 1.2, pre_end - pre_start, left=pre_start, height=bar_height,
        color=GOLD, alpha=0.3, edgecolor=GOLD, linewidth=2.0)
ax.text(pre_start + 0.3, pipeline_y - 1.2, 'Pipeline capacity = 1 (idle)',
        color=GOLD, fontsize=10, fontweight='bold', va='center')

result_x = 7.5
result_y = y_positions[-1] + 3.2
ax.text(result_x, result_y,
        'Cascade count = 4    Pipeline capacity = 1    Overload = 4\u00d7',
        color=RED, fontsize=12, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=RED, linewidth=2))

ax.text(result_x, result_y - 1.0,
        'Severity determined by promotion count, NOT event magnitude',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

ax.set_xlim(-4.0, 10.5)
ax.set_ylim(-3.0, y_positions[-1] + 4.5)
ax.set_xticks([])
ax.set_yticks([])

save(fig, 'math14_02_cascade_severity.png')


# ================================================================
# FIG 3: PROCESSING ENTROPY DIFFERENTIAL — TWO PROCESSORS SAME TOKENS
# Type: Running/Convergence Chart (Type 1)
# Shows: Hp for experienced vs novice processor across a shared set
#        of tokens. The GAP between curves IS the T4 communication
#        cost differential. Text cannot show the gap shape.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='Tokens (shared vocabulary)',
         ylabel='Processing Entropy  Hp(x | p, g, c)',
         title='Processing Entropy Differential: Same Tokens, Different Processors')

np.random.seed(42)
n_tokens = 25
token_labels = ['w%d' % (i + 1) for i in range(n_tokens)]
x = np.arange(n_tokens)

hp_novice = np.random.uniform(3.5, 8.5, n_tokens)
hp_novice = np.sort(hp_novice)[::-1]

hp_expert = np.random.uniform(0.0, 0.8, n_tokens)
hp_expert[0:5] = np.random.uniform(0.5, 1.5, 5)
hp_expert = np.sort(hp_expert)[::-1]

ax.fill_between(x, hp_expert, hp_novice, color=PURPLE, alpha=0.10)

ax.plot(x, hp_novice, color=MAG, linewidth=2.5, marker='o', markersize=6,
        markeredgecolor=WHITE, markeredgewidth=1.5, label='Novice processor (high Hp)')
ax.plot(x, hp_expert, color=CYAN, linewidth=2.5, marker='o', markersize=6,
        markeredgecolor=WHITE, markeredgewidth=1.5, label='Expert processor (Hp \u2248 0)')

mid_token = 12
gap_val = hp_novice[mid_token] - hp_expert[mid_token]
ax.annotate('',
            xy=(mid_token, hp_expert[mid_token]),
            xytext=(mid_token, hp_novice[mid_token]),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.0))
ax.text(mid_token + 1.8, (hp_novice[mid_token] + hp_expert[mid_token]) / 2.0,
        '\u0394Hp = %.1f\nCommunication\ncost differential' % gap_val,
        color=GOLD, fontsize=11, fontweight='bold', va='center')

ax.text(n_tokens - 1.5, hp_novice[-1] + 1.2,
        'Same Shannon H\nfor every token',
        color=SILVER, fontsize=10, ha='right', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

ax.text(1, 1.8,
        'Expert: most tokens at 0a\nHp \u2248 0, pipeline free',
        color=CYAN, fontsize=9)

ax.text(1, hp_novice[3] + 0.8,
        'Novice: all tokens at 1\nHp > 0, pipeline saturated',
        color=MAG, fontsize=9)

ax.set_xlim(-1.5, n_tokens + 1)
ax.set_ylim(-0.8, 10.5)
ax.set_xticks([0, 6, 12, 18, 24])
ax.set_xticklabels(['w1', 'w7', 'w13', 'w19', 'w25'], color=DIM)

legend = ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

save(fig, 'math14_03_hp_differential.png')


# ================================================================
# FIG 4: THROUGHPUT BOUND — THROUGHPUT VS ZERO-ABSENT RATIO
# Type: Running/Convergence Chart (Type 1)
# Shows: T1 as a curve — throughput increasing as 0a ratio grows.
#        The shape of the curve (linear? convex?) is the finding.
#        Text states the theorem; the curve shows its behavior.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='Zero-Absent Ratio  |{x : S = 0a}| / |X|',
         ylabel='Effective Throughput  T(p)',
         title='Theorem 1: Throughput Bound by Dissolution Ratio')

ratio = np.linspace(0.0, 0.98, 300)
base_throughput = 1.0
throughput = base_throughput / (1.0 - ratio + 0.02)
throughput = throughput / throughput[0]

ax.plot(ratio, throughput, color=CYAN, linewidth=2.5)

stages = [
    (0.10, 'Immature\n(most at \u221e)', RED),
    (0.40, 'Developing\n(some at 0a)', ORANGE),
    (0.70, 'Mature\n(most at 0a)', GREEN),
    (0.92, 'Wise', GOLD),
]

for r, label, color in stages:
    t_val = np.interp(r, ratio, throughput)
    ax.scatter([r], [t_val], s=200, color=color, edgecolors=WHITE,
              linewidth=2, zorder=5)
    if r < 0.5:
        ax.annotate(label, xy=(r, t_val),
                    xytext=(r + 0.08, t_val + 4),
                    color=color, fontsize=10, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    else:
        ax.annotate(label, xy=(r, t_val),
                    xytext=(r - 0.12, t_val + 6),
                    color=color, fontsize=10, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

ax.fill_between(ratio, 0, throughput, alpha=0.05, color=CYAN)

ax.text(0.55, 3.0,
        'T(p) \u221d 1 / (1 \u2212 M(p,t))\n\n'
        'As dissolution ratio \u2192 1,\n'
        'throughput \u2192 \u221e\n\n'
        'Pipeline freed for\nnovel problems only',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=DIM))

ax.set_xlim(-0.05, 1.02)
ax.set_ylim(-1, 55)

save(fig, 'math14_04_throughput_bound.png')


# ================================================================
# FIG 5: FOUR STATES GRID — CARDINALITY x MANAGEABILITY
# Type: Geometric Cross-Section (Type 4)
# Shows: The paper's core 2x2(+) structure as spatial geometry.
#        Adjacency, permitted transitions, and the prescribed response
#        per cell. The spatial layout shows relationships that the
#        sequential text listing cannot.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 21)
ax.set_ylim(-2, 16)

ax.set_title('The Four Processing States: S(x, p, g, c) \u2192 {\u221e, 1, 0a, 0e}',
             color=GOLD, fontsize=16, fontweight='bold', pad=30)

cells = [
    # (x, y, w, h, color, state, response, label)
    (1, 8.5, 8.5, 5.5, CYAN, '\u221e', 'Manageable \u221e',
     'Reduce: R(g) = r_k \u2218 ... \u2218 r_1\nTerminate at A(r_k, g) = true'),
    (11, 8.5, 8.5, 5.5, GREEN, '1', 'Manageable 1',
     'Execute: act, complete, release\nPromote next from \u221e'),
    (1, 1.5, 8.5, 5.5, BLUE, '0a', 'Manageable 0a',
     'Leave alone: dissolved to structure\nHp = 0, pipeline free\nCan regress to 1 under context change'),
    (11, 1.5, 8.5, 5.5, PURPLE, '0e', 'Unmanageable 0e',
     'Boundary: M(x,p) = false\nNo reduction chain exists\nAct on own architecture in response'),
]

for (x, y, w, h, color, state, label, response) in cells:
    rect = mpatches.FancyBboxPatch((x, y), w, h,
                                    boxstyle='round,pad=0.3',
                                    facecolor=color, alpha=0.12,
                                    edgecolor=color, linewidth=2.5)
    ax.add_patch(rect)

    ax.text(x + w / 2, y + h - 0.9, label,
            color=color, fontsize=14, fontweight='bold',
            ha='center', va='top')

    ax.text(x + w - 0.6, y + h - 0.5, state,
            color=color, fontsize=28, fontweight='bold',
            ha='right', va='top', alpha=0.3)

    ax.text(x + w / 2, y + 1.2, response,
            color=SILVER, fontsize=9, ha='center', va='bottom',
            linespacing=1.6)

ax.annotate('', xy=(10.7, 11.25), xytext=(9.8, 11.25),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(10.25, 12.2, 'R(g)', color=GOLD, fontsize=11, fontweight='bold', ha='center')

ax.annotate('', xy=(5.25, 8.2), xytext=(5.25, 7.3),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
ax.text(6.3, 7.7, 'D(p,t)', color=GREEN, fontsize=11, fontweight='bold', ha='center')

ax.annotate('', xy=(15.25, 8.2), xytext=(15.25, 7.3),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.0, linestyle='dashed'))
ax.text(16.5, 7.7, 'M(x,p)=false', color=DIM, fontsize=9, ha='center')

ax.annotate('', xy=(5.25, 14.3), xytext=(5.25, 15.0),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.0))
ax.text(6.8, 15.0, 'Cascade:\n0a \u2192 1', color=RED, fontsize=9,
        fontweight='bold', ha='center')

ax.text(1, 0.3, 'MANAGEABLE  (M = true)',
        color=SILVER, fontsize=12, fontstyle='italic')
ax.text(11, 0.3, 'UNMANAGEABLE  (M = false)',
        color=SILVER, fontsize=12, fontstyle='italic')

ax.text(-0.5, 11.25, 'ACTION\nSTATES',
        color=SILVER, fontsize=10, ha='center', va='center',
        rotation=90, fontstyle='italic')
ax.text(-0.5, 4.25, 'ZERO\nSTATES',
        color=SILVER, fontsize=10, ha='center', va='center',
        rotation=90, fontstyle='italic')

save(fig, 'math14_05_four_states_grid.png')


# ================================================================
# FIG 6: DISSOLUTION VALIDITY ENVELOPE
# Type: Threshold/Region Chart (Type 3)
# Shows: 2D region representing conditions under which dissolution holds.
#        Operating point inside = 0a maintained. Events push toward boundary.
#        Events that cross boundary trigger cascade. Width = robustness.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='Environmental Variation',
         ylabel='Stimulus Novelty',
         title='Dissolution Validity Envelope: When 0a Holds and When It Breaks')

theta = np.linspace(0, 2 * np.pi, 200)
outer_rx, outer_ry = 5.5, 4.0
inner_rx, inner_ry = 3.5, 2.5

outer_x = 7 + outer_rx * np.cos(theta)
outer_y = 6 + outer_ry * np.sin(theta)
inner_x = 7 + inner_rx * np.cos(theta)
inner_y = 6 + inner_ry * np.sin(theta)

ax.fill(outer_x, outer_y, color=GREEN, alpha=0.06)
ax.fill(inner_x, inner_y, color=GREEN, alpha=0.08)
ax.plot(outer_x, outer_y, color=RED, linewidth=2.5, linestyle='-',
        label='Cascade boundary (dissolution fails)')
ax.plot(inner_x, inner_y, color=GREEN, linewidth=1.5, linestyle='--',
        alpha=0.6, label='High-confidence zone')

ax.scatter([7], [6], s=250, color=GREEN, edgecolors=WHITE, linewidth=2, zorder=5)
ax.text(7, 5.0, 'Nominal\noperating point', color=GREEN, fontsize=10,
        ha='center', fontweight='bold')

events = [
    (3.2, 8.5, 'Bee in car', RED, True),
    (5.5, 7.2, 'Loud noise', ORANGE, False),
    (8.5, 4.0, 'Phone rings', CYAN, False),
    (11.8, 3.5, 'Tire blowout', RED, True),
]

for (ex, ey, elabel, ecolor, breaks) in events:
    ax.scatter([ex], [ey], s=200, color=ecolor, edgecolors=WHITE,
              linewidth=2, zorder=5, marker='*' if breaks else 'D')
    ax.annotate('', xy=(ex, ey), xytext=(7, 6),
                arrowprops=dict(arrowstyle='->', color=ecolor, lw=1.5,
                                linestyle='--', alpha=0.6))

ax.text(3.2, 9.5, 'Bee in car\n(BREAKS envelope)', color=RED, fontsize=9,
        ha='center', fontweight='bold')
ax.text(5.5, 8.2, 'Loud noise\n(absorbed)', color=ORANGE, fontsize=9,
        ha='center')
ax.text(9.5, 3.2, 'Phone rings\n(absorbed)', color=CYAN, fontsize=9,
        ha='center')
ax.text(11.8, 2.3, 'Tire blowout\n(BREAKS envelope)', color=RED, fontsize=9,
        ha='center', fontweight='bold')

ax.annotate('Wider envelope =\nmore robust dissolution\n(deeper training)',
            xy=(7 + outer_rx - 0.5, 6),
            xytext=(14.5, 8.5),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax.fill_between([0.5, 1.5], [0.8, 0.8], [1.6, 1.6], color=GREEN, alpha=0.15)
ax.text(1.8, 1.2, '= 0a maintained', color=GREEN, fontsize=9)
ax.plot([0.5, 1.5], [2.5, 2.5], color=RED, linewidth=2.5)
ax.text(1.8, 2.4, '= cascade boundary', color=RED, fontsize=9)

ax.set_xlim(-0.5, 16)
ax.set_ylim(-0.5, 11.5)

legend = ax.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

save(fig, 'math14_06_validity_envelope.png')


# ================================================================
# FIG 7: OPTIMAL REDUCTION WINDOW
# Type: Threshold/Region Chart (Type 3)
# Shows: Three regions across reduction depth: insufficient (can't act),
#        optimal (minimum sufficient for goal), over-reduced (actionability
#        destroyed). The window between two failure modes.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='Reduction Depth',
         ylabel='Actionability  A(r_k, g)',
         title='Optimal Reduction Window: The Goal-Dependent Sweet Spot')

x = np.linspace(0, 10, 500)
actionability = np.zeros_like(x)
rise_start = 2.5
rise_end = 4.0
fall_start = 7.0
fall_end = 8.5

for i, xi in enumerate(x):
    if xi < rise_start:
        actionability[i] = 0.05
    elif xi < rise_end:
        t = (xi - rise_start) / (rise_end - rise_start)
        actionability[i] = 0.05 + 0.90 * (3 * t * t - 2 * t * t * t)
    elif xi < fall_start:
        actionability[i] = 0.95
    elif xi < fall_end:
        t = (xi - fall_start) / (fall_end - fall_start)
        actionability[i] = 0.95 - 0.85 * (3 * t * t - 2 * t * t * t)
    else:
        actionability[i] = 0.10

ax.fill_between(x, 0, 1.05, where=(x < rise_start),
                color=RED, alpha=0.08)
ax.fill_between(x, 0, 1.05, where=((x >= rise_end) & (x <= fall_start)),
                color=GREEN, alpha=0.10)
ax.fill_between(x, 0, 1.05, where=(x > fall_end),
                color=ORANGE, alpha=0.08)
ax.fill_between(x, 0, 1.05, where=((x >= rise_start) & (x < rise_end)),
                color=DIM, alpha=0.05)
ax.fill_between(x, 0, 1.05, where=((x > fall_start) & (x <= fall_end)),
                color=DIM, alpha=0.05)

ax.plot(x, actionability, color=CYAN, linewidth=2.5)

threshold = 0.5
ax.axhline(y=threshold, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(0.3, threshold + 0.06, 'Actionability threshold', color=GOLD, fontsize=9)

ax.text(1.25, 0.85, 'INSUFFICIENT\n\nStill at \u221e\nCannot act\n\n100M rows\nno summary yet',
        color=RED, fontsize=10, ha='center', va='top', linespacing=1.4)

ax.text(5.5, 0.85, 'OPTIMAL WINDOW\n\nR* lives here\nMin k for A(r_k,g)=true\n\nSummary sufficient\nfor decision',
        color=GREEN, fontsize=10, ha='center', va='top', fontweight='bold', linespacing=1.4)

ax.text(9.2, 0.85, 'OVER-REDUCED\n\nInformation lost\n"Things are fine"\nCan\'t act on that',
        color=ORANGE, fontsize=10, ha='center', va='top', linespacing=1.4)

ax.annotate('R* = argmin k\nA(r_k, g) = true',
            xy=(rise_end, 0.95),
            xytext=(rise_end + 0.2, 0.60),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

ax.set_xlim(-0.3, 10.5)
ax.set_ylim(-0.05, 1.08)
ax.set_xticks([])

save(fig, 'math14_07_optimal_window.png')


# ================================================================
# FIG 8: COMMUNICATION COST COMPOSITION — Hp vs Hs ACROSS SCENARIOS
# Type: Comparison Bar Chart (Type 6)
# Shows: Stacked bars decomposing total communication cost into
#        Hp(sender) + Hs(channel) + Hp(receiver) across four scenarios.
#        Shows when processing cost dominates channel cost.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='', ylabel='Relative Communication Cost',
         title='Theorem 4: Communication Cost = Hp(sender) + Hs(channel) + Hp(receiver)')

scenarios = [
    'Expert \u2192 Expert',
    'Expert \u2192 Novice',
    'Novice \u2192 Expert',
    'Novice \u2192 Novice',
]

hp_sender   = [0.5, 0.5, 6.0, 6.0]
hs_channel  = [2.0, 2.0, 2.0, 2.0]
hp_receiver = [0.5, 7.0, 0.5, 7.0]

x_pos = np.array([0, 1.8, 3.6, 5.4])
bar_width = 1.0

bars_sender = ax.bar(x_pos, hp_sender, bar_width,
                     color=CYAN, alpha=0.7, edgecolor=CYAN, linewidth=1.5,
                     label='Hp(sender)')
bars_channel = ax.bar(x_pos, hs_channel, bar_width,
                      bottom=hp_sender,
                      color=BLUE, alpha=0.7, edgecolor=BLUE, linewidth=1.5,
                      label='Hs(channel) — Shannon')
bottoms_recv = [hp_sender[i] + hs_channel[i] for i in range(4)]
bars_receiver = ax.bar(x_pos, hp_receiver, bar_width,
                       bottom=bottoms_recv,
                       color=MAG, alpha=0.7, edgecolor=MAG, linewidth=1.5,
                       label='Hp(receiver)')

for i in range(4):
    total = hp_sender[i] + hs_channel[i] + hp_receiver[i]
    ax.text(x_pos[i], total + 0.5,
            'Total: %.1f' % total,
            color=WHITE, fontsize=11, fontweight='bold', ha='center')

    mid_s = hp_sender[i] / 2.0
    if hp_sender[i] > 1.0:
        ax.text(x_pos[i], mid_s, '%.1f' % hp_sender[i],
                color=WHITE, fontsize=9, ha='center', va='center')

    mid_c = hp_sender[i] + hs_channel[i] / 2.0
    ax.text(x_pos[i], mid_c, '%.1f' % hs_channel[i],
            color=WHITE, fontsize=9, ha='center', va='center')

    mid_r = bottoms_recv[i] + hp_receiver[i] / 2.0
    if hp_receiver[i] > 1.0:
        ax.text(x_pos[i], mid_r, '%.1f' % hp_receiver[i],
                color=WHITE, fontsize=9, ha='center', va='center')

ax.set_xticks(x_pos)
ax.set_xticklabels(scenarios, color=SILVER, fontsize=10)

ax.axhline(y=2.0, color=BLUE, linewidth=1.0, linestyle=':', alpha=0.4)
ax.text(5.9, 2.3, 'Shannon-only cost\n(Hs = 2.0 for all)',
        color=BLUE, fontsize=9, fontstyle='italic', ha='left')

ax.text(0, 13.0,
        'Shannon optimized the channel (blue).\n'
        'Processing entropy (cyan + magenta) often dominates total cost.',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=DIM))

pct_shannon = [hs_channel[i] / (hp_sender[i] + hs_channel[i] + hp_receiver[i]) * 100
               for i in range(4)]
for i in range(4):
    total = hp_sender[i] + hs_channel[i] + hp_receiver[i]
    ax.text(x_pos[i], -1.2,
            'Hs = %d%% of total' % int(pct_shannon[i]),
            color=BLUE, fontsize=9, ha='center', fontstyle='italic')

ax.set_xlim(-1.0, 7.0)
ax.set_ylim(-2.0, 17.0)

legend = ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

save(fig, 'math14_08_communication_cost.png')


# ================================================================
# SUMMARY
# ================================================================

print("\nMATH-14 Diagram Script Complete. 8 figures generated:")
print("  1. math14_01_reduction_convergence.png")
print("  2. math14_02_cascade_severity.png")
print("  3. math14_03_hp_differential.png")
print("  4. math14_04_throughput_bound.png")
print("  5. math14_05_four_states_grid.png")
print("  6. math14_06_validity_envelope.png")
print("  7. math14_07_optimal_window.png")
print("  8. math14_08_communication_cost.png")
