
#!/usr/bin/env python3
"""
HOWL VDR-34 Diagrams — Why Exact Integer Arithmetic Changes Everything
8 figures covering compound performance gains across five axes.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
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



outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)


def style_ax(ax, title, xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=18)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=10)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


# ================================================================
# FIG 1: TOKEN COST SCALING BY DATA SIZE
# Type: Running/Convergence Chart
# Shows: The divergence between conventional quadratic token cost
#        and VDR flat cost as data size grows from 64B to 1GB.
#        The curve shape communicates the capability boundary.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Token Cost Scaling by Data Size',
         xlabel='Data Size', ylabel='LLM Tokens Required')

data_bytes = [64, 256, 1024, 4096, 16384, 65536,
              262144, 1048576, 4194304, 16777216,
              67108864, 268435456, 1073741824]
labels_short = ['64B', '256B', '1KB', '4KB', '16KB', '64KB',
                '256KB', '1MB', '4MB', '16MB', '64MB', '256MB', '1GB']

conv_tokens = [d * 4 for d in data_bytes]  # ~4 tokens per byte
vdr_tokens = [8] * len(data_bytes)

x = np.arange(len(data_bytes))

ax.semilogy(x, conv_tokens, color=RED, linewidth=2.5, marker='o',
            markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='Conventional LLM', zorder=5)
ax.semilogy(x, vdr_tokens, color=GREEN, linewidth=2.5, marker='s',
            markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
            label='VDR-LLM-Prolog', zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(labels_short, rotation=35, ha='right', fontsize=8)
ax.set_ylim(3, 8e9)
ax.set_xlim(-0.5, len(data_bytes) - 0.5)

# Impossible region
impossible_start = 7  # 1MB index
ax.axvspan(impossible_start - 0.5, len(data_bytes) - 0.5,
           alpha=0.06, color=RED, zorder=1)
ax.text(8.5, 3e8, 'IMPOSSIBLE\nvia token stream',
        color=RED, fontsize=11, ha='center', va='center',
        fontstyle='italic', alpha=0.8)

# Ratio annotations
for i in [0, 4, 7, 12]:
    ratio = conv_tokens[i] / vdr_tokens[i]
    if ratio >= 1e6:
        rtxt = '%.0fM:1' % (ratio / 1e6)
    elif ratio >= 1000:
        rtxt = '%.0fK:1' % (ratio / 1000)
    else:
        rtxt = '%.0f:1' % ratio
    y_mid = np.sqrt(conv_tokens[i] * vdr_tokens[i])
    ax.annotate(rtxt, xy=(i, y_mid), fontsize=9, color=GOLD,
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=GOLD, alpha=0.9))

ax.axhline(y=128000, color=ORANGE, linestyle='--', linewidth=1.2, alpha=0.6)
ax.text(0.3, 180000, 'Typical 128K context window', color=ORANGE,
        fontsize=8, alpha=0.7)

ax.axhline(y=2000000, color=ORANGE, linestyle=':', linewidth=1.0, alpha=0.4)
ax.text(0.3, 2800000, 'Max 2M context window', color=ORANGE,
        fontsize=8, alpha=0.5)

legend = ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=10)
legend.get_frame().set_alpha(0.9)

ax.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr34_01_token_cost_scaling.png')


# ================================================================
# FIG 2: ENERGY PER OPERATION ACROSS FIVE IMPLEMENTATIONS
# Type: Scale/Landscape Diagram
# Shows: Log-scale energy per Q335 multiply from Python (~500uJ)
#        to ASIC (~39pJ). The spacing communicates the 10M:1 range
#        that flat numbers cannot.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Energy Per Q335 Multiply Across Five Implementations',
         xlabel='', ylabel='Energy (Joules, log scale)')

platforms = ['Python\n(CPython)', 'Zig\n(Host CPU)', 'FPGA\n(Zynq 150MHz)',
             'GPU\n(H100 int)', 'ASIC\n(VDR-Q335)']
energies = [500e-6, 13e-9, 114e-12, 82e-12, 39e-12]
colors_bar = [DIM, BLUE, CYAN, ORANGE, GREEN]
bar_labels = ['~500 \u00b5J', '~13 nJ', '~114 pJ', '~82 pJ', '~39 pJ']

x = np.arange(len(platforms))
bars = ax.bar(x, energies, width=0.55, color=colors_bar, alpha=0.75,
              edgecolor=WHITE, linewidth=1.5, zorder=5)

ax.set_yscale('log')
ax.set_ylim(1e-12, 2e-3)
ax.set_xlim(-0.8, len(platforms) - 0.2)
ax.set_xticks(x)
ax.set_xticklabels(platforms, fontsize=10, color=SILVER)

# Value labels above bars
for i, (b, lbl) in enumerate(zip(bars, bar_labels)):
    ax.text(i, energies[i] * 2.5, lbl, ha='center', va='bottom',
            color=colors_bar[i], fontsize=11, fontweight='bold')

# Speedup annotations between adjacent bars
pairs = [(0, 1, '38,000\u00d7'), (1, 2, '114\u00d7'),
         (2, 3, '1.4\u00d7'), (3, 4, '2.1\u00d7')]
for (a, b, txt) in pairs:
    ymid = np.sqrt(energies[a] * energies[b])
    xmid = (a + b) / 2.0
    ax.annotate('', xy=(b, energies[b] * 1.3), xytext=(a, energies[a] * 0.7),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5,
                                connectionstyle='arc3,rad=-0.15'))
    ax.text(xmid, ymid, txt, ha='center', va='center', color=GOLD,
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=GOLD, alpha=0.85))

# Total range annotation
ax.text(2.0, 5e-4, 'Total range: ~12,800,000\u00d7',
        ha='center', va='center', color=WHITE, fontsize=12,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN,
                  edgecolor=GOLD, linewidth=1.5))

# SHR335 note
ax.text(4.0, 5e-12, 'SHR335 divmod: 0 pJ\n(wire routing)',
        ha='center', va='top', color=GREEN, fontsize=9,
        fontstyle='italic')

ax.grid(True, axis='y', alpha=0.08, color=DIM)

save(fig, 'vdr34_02_energy_landscape.png')


# ================================================================
# FIG 3: SRE ACCUMULATION — TOKENS PER INVESTIGATION
# Type: Running/Convergence Chart
# Shows: Token cost dropping from 329 to 55 over 100 investigations
#        with auto-triage percentage rising. The curve shape shows
#        solved problems staying solved.
# ================================================================

fig, ax1 = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax1, 'SRE Accumulation: Cost Per Investigation Drops as Rules Accumulate',
         xlabel='Investigation Number', ylabel='LLM Command Tokens')

inv_nums = [1, 2, 5, 10, 20, 50, 100]
cmd_tokens = [329, 127, 110, 92, 78, 65, 55]
auto_triage = [0, 25, 45, 65, 78, 88, 93]
auto_rules = [0, 7, 18, 47, 72, 115, 150]

color_tok = CYAN
color_tri = GREEN
color_rul = ORANGE

ax1.plot(inv_nums, cmd_tokens, color=color_tok, linewidth=2.5,
         marker='o', markersize=10, markeredgecolor=WHITE,
         markeredgewidth=1.5, label='Command tokens', zorder=5)

for i, (ix, ct) in enumerate(zip(inv_nums, cmd_tokens)):
    offset_y = 18 if i != 1 else -22
    ax1.text(ix, ct + offset_y, str(ct), ha='center', va='bottom' if offset_y > 0 else 'top',
             color=color_tok, fontsize=9, fontweight='bold')

ax1.set_xlim(-5, 108)
ax1.set_ylim(0, 400)
ax1.set_xlabel('Investigation Number', color=SILVER, fontsize=11, labelpad=10)
ax1.set_ylabel('LLM Command Tokens', color=color_tok, fontsize=11, labelpad=10)
ax1.tick_params(axis='y', colors=color_tok)

ax2 = ax1.twinx()
ax2.set_facecolor('none')
ax2.plot(inv_nums, auto_triage, color=color_tri, linewidth=2.5,
         marker='s', markersize=9, markeredgecolor=WHITE,
         markeredgewidth=1.5, linestyle='--', label='Auto-triage %', zorder=4)

for i, (ix, at) in enumerate(zip(inv_nums, auto_triage)):
    offset_y = -4 if i > 0 else 3
    ax2.text(ix, at + offset_y, '%d%%' % at, ha='center',
             va='top' if offset_y < 0 else 'bottom',
             color=color_tri, fontsize=9)

ax2.set_ylim(-5, 105)
ax2.set_ylabel('Auto-Triage %', color=color_tri, fontsize=11, labelpad=10)
ax2.tick_params(axis='y', colors=color_tri)
for spine in ax2.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

# Rules annotation bar at bottom
for i, (ix, ar) in enumerate(zip(inv_nums, auto_rules)):
    ax1.bar(ix, 15, bottom=5, width=3, color=color_rul, alpha=0.4, zorder=2)
    ax1.text(ix, 12, '%d' % ar, ha='center', va='center',
             color=color_rul, fontsize=7)
ax1.text(55, 12, 'auto-firing rules', ha='left', va='center',
         color=color_rul, fontsize=8, fontstyle='italic')

# 83% reduction annotation
ax1.annotate('83% reduction', xy=(100, 55), xytext=(75, 200),
             color=GOLD, fontsize=11, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=GOLD, alpha=0.9))

# Break-even note
ax1.text(15, 370, 'Rule cost: 25-40 tokens once\nReplaces 150-300 tokens per reuse',
         color=SILVER, fontsize=9, fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN,
                   edgecolor=DIM, alpha=0.8))

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
legend = ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right',
                    facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

ax1.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr34_03_sre_accumulation.png')


# ================================================================
# FIG 4: COMPOUND PERFORMANCE WATERFALL
# Type: Progression/Sequence Diagram
# Shows: Five independent axes multiplying from 1x to ~8,000x.
#        Each stage labeled with source and mechanism.
#        The visual shows how independent factors compound.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, 'Compound Performance: Five Independent Axes Multiply', xlabel='', ylabel='')
ax.axis('off')

stages = [
    ('Baseline', '1\u00d7', '', DIM),
    ('Hardware\n(INT8 native)', '2\u00d7', '\u00d72', BLUE),
    ('Token\nElimination', '66\u00d7', '\u00d733', CYAN),
    ('Linear\nScaling', '462\u00d7', '\u00d77', GREEN),
    ('Rule\nAccumulation', '2,772\u00d7', '\u00d76', ORANGE),
    ('Engineering\nDeterminism', '~8,000\u00d7', '\u00d73', GOLD),
]

n = len(stages)
box_w = 0.11
box_h = 0.55
gap = 0.035
start_x = 0.06
y_center = 0.5

for i, (label, value, mult, color) in enumerate(stages):
    cx = start_x + i * (box_w + gap)
    bx = cx - box_w / 2
    by = y_center - box_h / 2

    rect = patches.FancyBboxPatch(
        (bx, by), box_w, box_h,
        boxstyle='round,pad=0.015',
        facecolor=PAN, edgecolor=color, linewidth=2.0,
        transform=ax.transAxes, zorder=5)
    ax.add_patch(rect)

    # Stage label
    ax.text(cx, y_center + 0.17, label, transform=ax.transAxes,
            ha='center', va='center', color=WHITE, fontsize=10,
            fontweight='bold', zorder=6)

    # Cumulative value
    ax.text(cx, y_center - 0.02, value, transform=ax.transAxes,
            ha='center', va='center', color=color, fontsize=16,
            fontweight='bold', zorder=6)

    # Multiplier below
    if mult:
        ax.text(cx, y_center - 0.17, mult, transform=ax.transAxes,
                ha='center', va='center', color=SILVER, fontsize=11,
                zorder=6)

    # Arrow to next
    if i < n - 1:
        ax_start = cx + box_w / 2 + 0.005
        ax_end = cx + box_w / 2 + gap - 0.005
        ax.annotate('', xy=(ax_end, y_center), xytext=(ax_start, y_center),
                    xycoords='axes fraction', textcoords='axes fraction',
                    arrowprops=dict(arrowstyle='->', color=GOLD,
                                    lw=2, mutation_scale=15),
                    zorder=4)

# Source labels below boxes
sources = ['', 'Nvidia INT8\nspec (published)', '769 vs 25,100\ntokens (measured)',
           'O(1) vs O(n\u00b2)\n(structural)', 'L1\u2192L3\n(projected)',
           'Bit-identical\n(structural)']
for i, src in enumerate(sources):
    if src:
        cx = start_x + i * (box_w + gap)
        ax.text(cx, y_center - box_h / 2 - 0.08, src,
                transform=ax.transAxes, ha='center', va='top',
                color=DIM, fontsize=7, fontstyle='italic', zorder=6)

# Bottom summary
ax.text(0.5, 0.04, 'Each axis independently measured or projected  \u2022  '
        'Conservative: 30\u00d7 blended datacenter  \u2022  '
        'All pre-optimization baselines',
        transform=ax.transAxes, ha='center', va='center',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN,
                  edgecolor=DIM, alpha=0.8))

save(fig, 'vdr34_04_compound_waterfall.png')


# ================================================================
# FIG 5: L1 -> L2 -> L3 EXECUTION LEVEL SHIFT
# Type: Threshold/Region Chart
# Shows: Over 100 investigations, the proportion of work at L1
#        (full LLM judgment), L2 (LLM invokes rule), L3 (pure Prolog)
#        shifts dramatically. The stacked regions show maturity.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Execution Level Shift: LLM Judgment \u2192 Automated Rules',
         xlabel='Investigation Number',
         ylabel='Proportion of Operations (%)')

inv = np.array([1, 2, 5, 10, 20, 50, 100])

# L3: pure Prolog, zero tokens
l3_pct = np.array([0, 10, 25, 40, 55, 72, 80])
# L2: LLM invokes stored rule, 8 tokens
l2_pct = np.array([0, 15, 20, 25, 23, 16, 13])
# L1: full LLM judgment, 50-500 tokens
l1_pct = 100 - l3_pct - l2_pct

inv_smooth = np.linspace(1, 100, 200)
l3_s = np.interp(inv_smooth, inv, l3_pct)
l2_s = np.interp(inv_smooth, inv, l2_pct)
l1_s = np.interp(inv_smooth, inv, l1_pct)

ax.fill_between(inv_smooth, 0, l3_s, color=GREEN, alpha=0.35,
                label='L3: Pure Prolog (0 tokens)', zorder=3)
ax.fill_between(inv_smooth, l3_s, l3_s + l2_s, color=CYAN, alpha=0.35,
                label='L2: LLM invokes rule (8 tokens)', zorder=3)
ax.fill_between(inv_smooth, l3_s + l2_s, 100, color=RED, alpha=0.25,
                label='L1: Full LLM judgment (50-500 tokens)', zorder=3)

ax.plot(inv_smooth, l3_s, color=GREEN, linewidth=2, zorder=4)
ax.plot(inv_smooth, l3_s + l2_s, color=CYAN, linewidth=2, zorder=4)

# Boundary labels
ax.text(85, 40, 'L3: Pure Prolog\n0 LLM tokens', color=GREEN,
        fontsize=11, fontweight='bold', ha='center', va='center')
ax.text(60, 84, 'L2: Rule invocation\n8 tokens each', color=CYAN,
        fontsize=10, ha='center', va='center')
ax.text(15, 85, 'L1: Full judgment\n50-500 tokens', color=RED,
        fontsize=10, ha='center', va='center')

# Key data points
for i_idx, (ix, l3v) in enumerate(zip(inv, l3_pct)):
    ax.plot(ix, l3v, 'o', color=GREEN, markersize=7,
            markeredgecolor=WHITE, markeredgewidth=1.2, zorder=6)

# Investigation milestones
milestones = [(1, 'Day 1:\n100% LLM'), (10, '65% auto-triage'),
              (50, '88% auto-triage'), (100, '93% auto-triage')]
ms_ys = [95, 60, 20, 10]
for (mx, mtxt), my in zip(milestones, ms_ys):
    ax.annotate(mtxt, xy=(mx, my), fontsize=8, color=GOLD,
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=GOLD, alpha=0.85))

ax.set_xlim(0, 105)
ax.set_ylim(0, 100)

legend = ax.legend(loc='center right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)
ax.grid(True, alpha=0.08, color=DIM)

save(fig, 'vdr34_05_l1_l2_l3_shift.png')


# ================================================================
# FIG 6: CONFIDENCE PROPAGATION CHAIN
# Type: Progression/Sequence Diagram
# Shows: Data flowing from sources through propagation formulas
#        to final confidence as exact VDR fractions. Each stage
#        has its formula and computed value.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, 'Confidence Propagation: Exact Fractions, Not Hedging Language',
         xlabel='', ylabel='')
ax.axis('off')

# Chain: Source -> Derivation -> Agreement -> Final
chain = [
    {
        'label': 'Prometheus\nMetric',
        'conf': '95/100',
        'color': CYAN,
        'x': 0.06,
        'note': 'Controlled system\nknown collection lag'
    },
    {
        'label': 'Deploy API\nResponse',
        'conf': '85/100',
        'color': BLUE,
        'x': 0.06,
        'note': 'External system\nnot under control'
    },
    {
        'label': 'Config Diff\n(Filesystem)',
        'conf': '95/100',
        'color': CYAN,
        'x': 0.06,
        'note': 'Controlled system\ngrant-verified read'
    },
]

# Source boxes (left column, stacked)
src_ys = [0.78, 0.50, 0.22]
bw, bh = 0.13, 0.18

for src, sy in zip(chain, src_ys):
    rect = patches.FancyBboxPatch(
        (src['x'], sy - bh / 2), bw, bh,
        boxstyle='round,pad=0.015',
        facecolor=PAN, edgecolor=src['color'], linewidth=1.8,
        transform=ax.transAxes, zorder=5)
    ax.add_patch(rect)
    ax.text(src['x'] + bw / 2, sy + 0.035, src['label'],
            transform=ax.transAxes, ha='center', va='center',
            color=WHITE, fontsize=9, fontweight='bold', zorder=6)
    ax.text(src['x'] + bw / 2, sy - 0.04, src['conf'],
            transform=ax.transAxes, ha='center', va='center',
            color=src['color'], fontsize=13, fontweight='bold', zorder=6)
    ax.text(src['x'] + bw / 2, sy - bh / 2 - 0.03, src['note'],
            transform=ax.transAxes, ha='center', va='top',
            color=DIM, fontsize=7, fontstyle='italic', zorder=6)

# Prolog derivation box (middle-left)
px, py = 0.30, 0.65
rect = patches.FancyBboxPatch(
    (px, py - 0.09), 0.16, 0.18,
    boxstyle='round,pad=0.015',
    facecolor=PAN, edgecolor=GREEN, linewidth=1.8,
    transform=ax.transAxes, zorder=5)
ax.add_patch(rect)
ax.text(px + 0.08, py + 0.05, 'Prolog\nDerivation',
        transform=ax.transAxes, ha='center', va='center',
        color=WHITE, fontsize=10, fontweight='bold', zorder=6)
ax.text(px + 0.08, py - 0.03, 'min(C\u1d62)',
        transform=ax.transAxes, ha='center', va='center',
        color=GREEN, fontsize=11, zorder=6)

# Temporal correlation box (middle-left lower)
tx, ty = 0.30, 0.35
rect = patches.FancyBboxPatch(
    (tx, ty - 0.09), 0.16, 0.18,
    boxstyle='round,pad=0.015',
    facecolor=PAN, edgecolor=ORANGE, linewidth=1.8,
    transform=ax.transAxes, zorder=5)
ax.add_patch(rect)
ax.text(tx + 0.08, ty + 0.05, 'Temporal\nCorrelation',
        transform=ax.transAxes, ha='center', va='center',
        color=WHITE, fontsize=10, fontweight='bold', zorder=6)
ax.text(tx + 0.08, ty - 0.03, 'LLM: 30/100',
        transform=ax.transAxes, ha='center', va='center',
        color=ORANGE, fontsize=11, zorder=6)

# Agreement box (middle-right)
agx, agy = 0.56, 0.50
rect = patches.FancyBboxPatch(
    (agx, agy - 0.11), 0.18, 0.22,
    boxstyle='round,pad=0.015',
    facecolor=PAN, edgecolor=GOLD, linewidth=2.0,
    transform=ax.transAxes, zorder=5)
ax.add_patch(rect)
ax.text(agx + 0.09, agy + 0.06, 'Multiple Sources\nAgree',
        transform=ax.transAxes, ha='center', va='center',
        color=WHITE, fontsize=10, fontweight='bold', zorder=6)
ax.text(agx + 0.09, agy - 0.01, '1\u2212\u220f(1\u2212C\u1d62)',
        transform=ax.transAxes, ha='center', va='center',
        color=GOLD, fontsize=12, fontweight='bold', zorder=6)

# Final confidence (right)
fx, fy = 0.82, 0.50
rect = patches.FancyBboxPatch(
    (fx, fy - 0.11), 0.14, 0.22,
    boxstyle='round,pad=0.015',
    facecolor=PAN, edgecolor=GOLD, linewidth=2.5,
    transform=ax.transAxes, zorder=5)
ax.add_patch(rect)
ax.text(fx + 0.07, fy + 0.06, 'Final\nConfidence',
        transform=ax.transAxes, ha='center', va='center',
        color=WHITE, fontsize=10, fontweight='bold', zorder=6)
ax.text(fx + 0.07, fy - 0.02, '94/100',
        transform=ax.transAxes, ha='center', va='center',
        color=GOLD, fontsize=18, fontweight='bold', zorder=6)

# Arrows: sources to derivation/correlation
for sy, target_y in [(0.78, 0.68), (0.50, 0.65)]:
    ax.annotate('', xy=(0.30, target_y), xytext=(0.19, sy),
                xycoords='axes fraction', textcoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
                zorder=4)

ax.annotate('', xy=(0.30, 0.37), xytext=(0.19, 0.22),
            xycoords='axes fraction', textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
            zorder=4)

# Derivation/correlation to agreement
ax.annotate('', xy=(0.56, 0.54), xytext=(0.46, 0.65),
            xycoords='axes fraction', textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
            zorder=4)
ax.annotate('', xy=(0.56, 0.46), xytext=(0.46, 0.35),
            xycoords='axes fraction', textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
            zorder=4)

# Agreement to final
ax.annotate('', xy=(0.82, 0.50), xytext=(0.74, 0.50),
            xycoords='axes fraction', textcoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.0),
            zorder=4)

# Bottom comparison
ax.text(0.50, 0.04,
        'Conventional LLM: "it appears likely"  (0 bits of information)\n'
        'VDR-LLM-Prolog: 94/100  (exact fraction, computed, auditable)',
        transform=ax.transAxes, ha='center', va='center',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN,
                  edgecolor=DIM, alpha=0.8))

save(fig, 'vdr34_06_confidence_chain.png')


# ================================================================
# FIG 7: THREE-LAYER NON-DEGRADATION ARCHITECTURE
# Type: Geometric Cross-Section
# Shows: Three concentric regions: data layer (KB at integer
#        addresses), working memory (bounded primitives),
#        computation (exact integer attention). Each labeled with
#        its invariant. Shows WHY sessions cannot degrade.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12), facecolor=BG)
style_ax(ax, 'Three-Layer Non-Degradation: Each Layer Cannot Degrade',
         xlabel='', ylabel='')
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect('equal')
ax.axis('off')

# Outer layer: Data (KB at integer addresses)
outer = plt.Circle((0, 0), 1.35, facecolor='none', edgecolor=BLUE,
                    linewidth=2.5, linestyle='-', zorder=3)
outer_fill = plt.Circle((0, 0), 1.35, facecolor=BLUE, alpha=0.06, zorder=2)
ax.add_patch(outer)
ax.add_patch(outer_fill)

# Middle layer: Working memory (bounded primitives)
middle = plt.Circle((0, 0), 0.90, facecolor='none', edgecolor=GREEN,
                     linewidth=2.5, linestyle='-', zorder=4)
middle_fill = plt.Circle((0, 0), 0.90, facecolor=GREEN, alpha=0.08, zorder=3)
ax.add_patch(middle)
ax.add_patch(middle_fill)

# Inner layer: Computation (exact integer attention)
inner = plt.Circle((0, 0), 0.45, facecolor='none', edgecolor=GOLD,
                    linewidth=2.5, linestyle='-', zorder=5)
inner_fill = plt.Circle((0, 0), 0.45, facecolor=GOLD, alpha=0.10, zorder=4)
ax.add_patch(inner)
ax.add_patch(inner_fill)

# Layer labels with invariant properties
# Outer
ax.text(0, 1.15, 'DATA LAYER', ha='center', va='center',
        color=BLUE, fontsize=13, fontweight='bold', zorder=6)
ax.text(0, 1.0, 'KB facts at integer addresses\nO(1) lookup, never re-read',
        ha='center', va='center', color=SILVER, fontsize=9, zorder=6)

# Middle
ax.text(0, 0.72, 'WORKING MEMORY', ha='center', va='center',
        color=GREEN, fontsize=12, fontweight='bold', zorder=6)
ax.text(0, 0.58, 'Bounded primitives\nCannot overflow by construction',
        ha='center', va='center', color=SILVER, fontsize=9, zorder=6)

# Inner
ax.text(0, 0.15, 'COMPUTATION', ha='center', va='center',
        color=GOLD, fontsize=12, fontweight='bold', zorder=6)
ax.text(0, 0.0, 'Exact integer\nattention', ha='center', va='center',
        color=GOLD, fontsize=10, zorder=6)
ax.text(0, -0.15, '\u2211 weights = 1/1', ha='center', va='center',
        color=GOLD, fontsize=11, fontweight='bold', zorder=6)

# Invariant callouts (outside the circles)
callouts = [
    (1.15, -0.75, 'Integer storage\ndoes not degrade', BLUE,
     0.85, -0.55),
    (-1.15, -0.55, 'Capacity bounded\nat creation', GREEN,
     -0.65, -0.45),
    (1.15, 0.55, 'Fact #47 at address 47\nturn 1 = turn 1,000,000', BLUE,
     0.85, 0.45),
    (-1.15, 0.75, 'LRU, queue, counter\nfixed-size forever', GREEN,
     -0.65, 0.55),
]

for (tx, ty, txt, col, ax_x, ax_y) in callouts:
    ax.annotate(txt, xy=(ax_x, ax_y), xytext=(tx, ty),
                fontsize=8, color=col, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                          edgecolor=col, alpha=0.85),
                arrowprops=dict(arrowstyle='->', color=col, lw=1.2),
                zorder=7)

# Conventional comparison at bottom
ax.text(0, -1.42, 'Conventional: all three layers degrade simultaneously\n'
        'Context fills (capacity) \u2022 Attention drifts (quality) \u2022 '
        'Hallucinations compound (reliability)',
        ha='center', va='center', color=RED, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN,
                  edgecolor=RED, alpha=0.7, linewidth=1.2),
        zorder=7)

save(fig, 'vdr34_07_non_degradation.png')


# ================================================================
# FIG 8: TOKEN ELIMINATION — WHERE 25,100 CONVENTIONAL TOKENS GO
# Type: Comparison Bar Chart
# Shows: The ~25,100 conventional tokens decomposed by function,
#        with VDR elimination mechanism for each. The visual
#        makes the 97% elimination concrete.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, 'Where Do 25,100 Conventional LLM Tokens Go?',
         xlabel='Token Count', ylabel='')

categories = [
    'State reconstruction\n(re-reading prior turns)',
    'Formatting &\nstructural tokens',
    'Arithmetic &\ndata transformation',
    'Deductive reasoning\n(chains as prose)',
    'Hedging &\nconfidence language',
    'Judgment &\nprose framing'
]

conv_counts = [10040, 6275, 3765, 2510, 1757, 753]
vdr_counts = [0, 0, 0, 0, 0, 769]

mechanisms = [
    'KB addressing\nO(1) integer lookup',
    'Grammar templates\n100% correct, 0 cost',
    'Exact primitives\n0 error rate',
    'Prolog unification\ndeterministic',
    'Exact fractions\nfrom formulas',
    'RETAINED\n(LLM judgment)'
]

colors_conv = [RED, RED, RED, RED, RED, GREEN]
colors_vdr = [GREEN, GREEN, GREEN, GREEN, GREEN, GREEN]

y = np.arange(len(categories))
bar_h = 0.35

# Conventional bars
bars_conv = ax.barh(y + bar_h / 2 + 0.02, conv_counts, height=bar_h,
                     color=RED, alpha=0.6, edgecolor=RED, linewidth=1.5,
                     label='Conventional LLM', zorder=4)

# VDR bars
bars_vdr = ax.barh(y - bar_h / 2 - 0.02, vdr_counts, height=bar_h,
                    color=GREEN, alpha=0.6, edgecolor=GREEN, linewidth=1.5,
                    label='VDR-LLM-Prolog', zorder=4)

ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=9, color=SILVER)
ax.set_xlim(0, 13000)

# Value labels on bars
for i, v in enumerate(conv_counts):
    ax.text(v + 150, i + bar_h / 2 + 0.02, '{:,}'.format(v),
            va='center', ha='left', color=RED, fontsize=9, fontweight='bold')

# VDR label only on last bar (judgment)
ax.text(769 + 150, len(categories) - 1 - bar_h / 2 - 0.02, '769',
        va='center', ha='left', color=GREEN, fontsize=9, fontweight='bold')

# Zero labels for eliminated categories
for i in range(5):
    ax.text(150, i - bar_h / 2 - 0.02, '0',
            va='center', ha='left', color=GREEN, fontsize=9, fontweight='bold')

# Mechanism labels (right side)
for i, mech in enumerate(mechanisms):
    color = CYAN if i < 5 else GOLD
    ax.text(12800, i, mech, va='center', ha='right',
            color=color, fontsize=8, fontstyle='italic')

# Summary box
ax.text(7000, 5.6, 'Eliminated: 24,331 tokens (96.9%)\n'
        'Retained: 769 tokens (3.1%) \u2014 judgment only',
        ha='center', va='center', color=WHITE, fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN,
                  edgecolor=GOLD, linewidth=1.5))

legend = ax.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
                   labelcolor=WHITE, fontsize=9)
legend.get_frame().set_alpha(0.9)

ax.grid(True, axis='x', alpha=0.08, color=DIM)

save(fig, 'vdr34_08_token_elimination.png')


# ================================================================
# SUMMARY
# ================================================================

print("\nVDR-34 Diagrams Complete:")
print("  vdr34_01_token_cost_scaling.png")
print("  vdr34_02_energy_landscape.png")
print("  vdr34_03_sre_accumulation.png")
print("  vdr34_04_compound_waterfall.png")
print("  vdr34_05_l1_l2_l3_shift.png")
print("  vdr34_06_confidence_chain.png")
print("  vdr34_07_non_degradation.png")
print("  vdr34_08_token_elimination.png")
