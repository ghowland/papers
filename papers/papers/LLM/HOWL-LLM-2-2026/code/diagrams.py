#!/usr/bin/env python3
"""
HOWL LLM-2 Diagrams — Calibrate, Extract, Refine: 1-Shot Pseudo-Gold from LLM Chat Sessions
8 figures covering coherence ceiling, system scale, calibration mechanics, and industry claims.
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

def setup_ax(ax, title, xlabel='', ylabel='', title_size=15):
    ax.set_facecolor(PAN)
    ax.set_title(title, color=GOLD, fontsize=title_size, fontweight='bold', pad=14)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

def save(fig, filename):
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


# ================================================================
# FIG 1: SYSTEM SCALE VS MODEL CAPABILITY
# Type: Scale/Landscape (Type 2)
# Shows: Log-scale axis from 1 module to 1000, with landmarks for
#        tutorial projects, vibe-coded projects, model ceiling,
#        and real engineering systems. Shaded regions mark where
#        AI is effective, marginal, and counterproductive.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
setup_ax(ax, 'System Scale vs. Model Capability', ylabel='')
ax.axis('off')

# Log scale axis from 1 to 2000 modules
x_min, x_max = 0.0, 3.35  # log10 scale: 1 to ~2200
y_center = 0.5
bar_height = 0.08

# Draw the main axis line
ax.plot([x_min, x_max], [y_center, y_center], color=SILVER, linewidth=2, zorder=5)

# Tick marks and labels
landmarks = [
    (0.0, '1', 'Single\nFunction', DIM),
    (0.7, '5', 'Tutorial\nProject', CYAN),
    (1.0, '10', 'Typical Vibe-\nCoded Project', BLUE),
    (1.18, '15', 'Max Modules in\nBlow Thread', MAG),
    (1.6, '~40', 'Model Coherence\nCeiling (~1 module)', RED),
    (2.65, '~450', 'Production\nGame Engine', GOLD),
    (3.0, '1000', 'Large-Scale\nSystem', PURPLE),
]

count = 0
for lx, label_num, label_desc, color in landmarks:
    if count % 2 == 0:
        offsetY = -0.01
    else:
        offsetY = 0.015

    ax.plot([lx, lx], [y_center - 0.03, y_center + 0.03], color=color, linewidth=2, zorder=6)
    ax.text(lx, y_center - 0.07, label_num, ha='center', va='top',
            color=color, fontsize=10, fontweight='bold')
    ax.text(lx, y_center + 0.06 + offsetY, label_desc, ha='center', va='bottom',
            color=color, fontsize=9, linespacing=1.3)
    count += 1

# Shaded regions
ax.axvspan(x_min, 1.15, ymin=0.25, ymax=0.42, alpha=0.10, color=GREEN)
ax.text(0.55, y_center - 0.16, 'AI Effective', ha='center', va='center',
        color=GREEN, fontsize=11, fontweight='bold')

ax.axvspan(1.15, 1.7, ymin=0.25, ymax=0.42, alpha=0.08, color=ORANGE)
ax.text(1.42, y_center - 0.16, 'AI Marginal', ha='center', va='center',
        color=ORANGE, fontsize=11, fontweight='bold')

ax.axvspan(1.7, x_max, ymin=0.25, ymax=0.42, alpha=0.06, color=RED)
ax.text(2.5, y_center - 0.16, 'AI Counterproductive', ha='center', va='center',
        color=RED, fontsize=11, fontweight='bold')

# Scale label
ax.text(x_max + 0.05, y_center, 'modules\n(log scale)', ha='left', va='center',
        color=DIM, fontsize=9)

# Key insight annotation
ax.text(1.9, y_center + 0.22,
        'The model failed on 4 modules (< 1%% of a 450-module system).\n'
        'The gap between where AI works and where systems live\n'
        'is over an order of magnitude.',
        ha='left', va='center', color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.9),
        linespacing=1.5)

ax.set_xlim(-0.15, 3.5)
ax.set_ylim(0.15, 0.85)

save(fig, 'llm2_01_system_scale_landscape.png')


# ================================================================
# FIG 2: CEILING STABILITY ACROSS MODEL GENERATIONS
# Type: Running/Convergence (Type 1)
# Shows: Flat coherence ceiling at ~1200 lines over 15 months,
#        with benchmark scores rising as a diverging dotted line.
#        Model release points marked on the timeline.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Coherence Ceiling vs. Benchmark Scores Across Model Generations',
         xlabel='Timeline', ylabel='')

# Timeline: Feb 2025 to May 2026 = ~16 months
months = np.arange(0, 16)
month_labels = ['Feb 25', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                'Oct', 'Nov', 'Dec', 'Jan 26', 'Feb', 'Mar', 'Apr', 'May 26']

# Coherence ceiling: flat at 1200
ceiling = np.ones(16) * 1200

# Benchmark scores: rising from ~60 to ~85 (normalized to same axis via secondary)
bench_raw = np.array([58, 60, 62, 64, 65, 67, 70, 72, 74, 76, 78, 79, 81, 82, 83, 85])

# Model release points (approximate positions)
releases = [
    (0, 'Sonnet 3.5', CYAN),
    (4, 'Opus 3.5', BLUE),
    (8, 'Sonnet 3.6', CYAN),
    (11, 'Opus 4.5', PURPLE),
    (15, 'Opus 4.6', GOLD),
]

# Plot ceiling
ax.plot(months, ceiling, color=RED, linewidth=2.5, linestyle='-', label='Coherence Ceiling (real code)', zorder=5)
ax.fill_between(months, 1100, 1300, alpha=0.06, color=RED)
ax.text(15.3, 1200, '~1,200 lines', va='center', ha='left', color=RED, fontsize=10, fontweight='bold')

# Secondary axis for benchmarks
ax2 = ax.twinx()
ax2.plot(months, bench_raw, color=GREEN, linewidth=2, linestyle='--', label='Benchmark Scores (SWE-bench etc.)', zorder=4)
ax2.set_ylabel('Benchmark Score (normalized)', color=GREEN, fontsize=11)
ax2.tick_params(colors=GREEN, labelsize=9)
ax2.spines['right'].set_color(GREEN)
ax2.spines['right'].set_linewidth(0.5)
for spine_name in ['top', 'left', 'bottom']:
    ax2.spines[spine_name].set_color(DIM)
    ax2.spines[spine_name].set_linewidth(0.5)

# Mark model releases
for pos, name, color in releases:
    ax.axvline(x=pos, color=color, linewidth=1, linestyle=':', alpha=0.5, zorder=3)
    ax.text(pos, 1450, name, ha='center', va='bottom', color=color, fontsize=8,
            rotation=35,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8))

# Divergence annotation
ax.annotate('Benchmarks rise.\nCeiling does not move.',
            xy=(12, 1200), xytext=(8, 1550),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xticks(months)
ax.set_xticklabels(month_labels, rotation=40, ha='right', fontsize=8, color=DIM)
ax.set_xlim(-0.5, 16)
ax.set_ylim(0, 1700)
ax2.set_ylim(50, 95)
ax.set_ylabel('Coherent Output (lines of real code)', color=RED, fontsize=11)

# Combined legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=RED, linewidth=2.5, label='Coherence Ceiling'),
    Line2D([0], [0], color=GREEN, linewidth=2, linestyle='--', label='Benchmark Scores'),
]
ax.legend(handles=legend_elements, loc='lower right',
          facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm2_02_ceiling_stability.png')


# ================================================================
# FIG 3: COHERENCE DEGRADATION CURVE
# Type: Threshold/Region (Type 3)
# Shows: Reliability of output vs. generation length, with gradual
#        degradation and a threshold band marking the engineering
#        trust boundary at ~1200 lines. Shaded regions for
#        "reliable," "degrading," and "unreliable."
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Coherence Degradation vs. Output Length',
         xlabel='Output Length (lines of real code)',
         ylabel='Constraint Coherence (probability of honoring all constraints)')

x = np.linspace(0, 2400, 500)
# Sigmoid-like degradation curve
coherence = 1.0 / (1.0 + np.exp((x - 1000) / 250.0))
coherence = 0.05 + 0.90 * coherence  # floor at 0.05, max at 0.95

ax.plot(x, coherence, color=CYAN, linewidth=2.5, zorder=5)

# Threshold band at ~1200 lines
ax.axvspan(1050, 1350, alpha=0.08, color=ORANGE, zorder=2)
ax.axvline(x=1200, color=ORANGE, linewidth=1.5, linestyle='--', alpha=0.7, zorder=4)
ax.text(1210, 0.88, '~1,200 lines\n(engineering\ntrust boundary)', ha='left', va='top',
        color=ORANGE, fontsize=10, fontweight='bold', linespacing=1.3)

# Shaded regions
ax.axvspan(0, 800, ymin=0, ymax=1, alpha=0.05, color=GREEN, zorder=1)
ax.text(400, 0.12, 'Reliable', ha='center', va='center',
        color=GREEN, fontsize=12, fontweight='bold', alpha=0.8)

ax.axvspan(800, 1350, ymin=0, ymax=1, alpha=0.04, color=ORANGE, zorder=1)
ax.text(1050, 0.12, 'Degrading', ha='center', va='center',
        color=ORANGE, fontsize=12, fontweight='bold', alpha=0.8)

ax.axvspan(1350, 2400, ymin=0, ymax=1, alpha=0.04, color=RED, zorder=1)
ax.text(1850, 0.12, 'Unreliable for\nEngineering', ha='center', va='center',
        color=RED, fontsize=11, fontweight='bold', alpha=0.8, linespacing=1.3)

# Horizontal reference: 50% coherence
y_50 = 0.50
ax.axhline(y=y_50, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(2380, y_50 + 0.03, '50%% coherence', ha='right', va='bottom', color=DIM, fontsize=9)

# Key data point: SiQL module
ax.scatter([1266], [0.48], s=200, color=GOLD, edgecolors=WHITE, linewidth=2, zorder=6)
ax.annotate('SiQL module\n(1,266 lines — one-shot,\ncoherent, at the limit)',
            xy=(1266, 0.48), xytext=(1600, 0.65),
            color=GOLD, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9),
            linespacing=1.3)

ax.set_xlim(-50, 2500)
ax.set_ylim(0.0, 1.02)

save(fig, 'llm2_03_coherence_degradation.png')


# ================================================================
# FIG 4: TRAINING WEIGHT GRAVITY VS CONTEXT STEERING
# Type: Running/Convergence (Type 1)
# Shows: Two probability distributions overlaid — the broad
#        training-weight default and the narrowed post-calibration
#        distribution. The calibrated distribution is tighter and
#        shifted toward the engineer's target.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Effect of Calibration on Output Distribution',
         xlabel='Solution Space (generic ← → system-specific)',
         ylabel='Probability Density')

x = np.linspace(-4, 6, 500)

# Training weight distribution: broad, centered at 0 (generic median)
training_dist = 0.35 * np.exp(-0.5 * (x / 1.4) ** 2)

# Calibrated distribution: narrow, shifted toward system-specific (center at 2.5)
calibrated_dist = 0.75 * np.exp(-0.5 * ((x - 2.5) / 0.6) ** 2)

# Fill under curves
ax.fill_between(x, training_dist, alpha=0.12, color=BLUE, zorder=2)
ax.plot(x, training_dist, color=BLUE, linewidth=2.5, label='Uncalibrated (training weights)', zorder=3)

ax.fill_between(x, calibrated_dist, alpha=0.15, color=GOLD, zorder=4)
ax.plot(x, calibrated_dist, color=GOLD, linewidth=2.5, label='After Calibration (context-steered)', zorder=5)

# Mark the engineer's target
ax.axvline(x=2.5, color=GREEN, linewidth=1.5, linestyle='--', alpha=0.7, zorder=6)
ax.text(2.65, 0.72, "Engineer's\nsystem target", ha='left', va='top',
        color=GREEN, fontsize=10, fontweight='bold', linespacing=1.3)

# Mark the training median
ax.axvline(x=0.0, color=BLUE, linewidth=1.5, linestyle=':', alpha=0.5, zorder=3)
ax.text(-0.15, 0.32, 'Training\nmedian\n(tutorial code)', ha='right', va='top',
        color=BLUE, fontsize=10, linespacing=1.3)

# Annotation: the gap
ax.annotate('', xy=(2.4, 0.04), xytext=(0.1, 0.04),
            arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax.text(1.25, 0.06, 'Calibration closes this gap', ha='center', va='bottom',
        color=SILVER, fontsize=10)

# Leakage annotation
ax.annotate('Training priors\nstill leak through',
            xy=(-0.5, 0.08), xytext=(-2.5, 0.20),
            color=MAG, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG, alpha=0.8),
            linespacing=1.3)

ax.set_xlim(-4.5, 6.5)
ax.set_ylim(0, 0.88)
ax.set_xticks([])

ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm2_04_calibration_distribution.png')


# ================================================================
# FIG 5: CONSTRAINT VIOLATION PROPAGATION COST
# Type: Threshold/Region (Type 3)
# Shows: Two curves — the direct cost of a wrong suggestion
#        (small, constant) vs. the propagation cost of finding
#        and fixing constraint violations across a system (grows
#        with constraint count). Crossover point where "AI help"
#        becomes "AI damage."
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'When AI Help Becomes AI Damage',
         xlabel='System Constraint Count',
         ylabel='Cost (engineer-hours)')

constraints = np.linspace(1, 500, 500)

# Direct cost: time to write the code yourself — modest, grows slowly
direct_cost = 2.0 + 0.008 * constraints

# AI-assisted cost with propagation: starts low (AI saves time on small systems)
# but propagation cost grows superlinearly with constraint count
ai_base_cost = 0.5 + 0.002 * constraints  # AI typing saves time
propagation_cost = 0.00003 * constraints ** 2  # finding violations grows quadratically
ai_total_cost = ai_base_cost + propagation_cost

# Find crossover
cross_idx = np.argmin(np.abs(direct_cost - ai_total_cost))
cross_x = constraints[cross_idx]
cross_y = direct_cost[cross_idx]

ax.plot(constraints, direct_cost, color=CYAN, linewidth=2.5,
        label='Write it yourself', zorder=5)
ax.plot(constraints, ai_total_cost, color=MAG, linewidth=2.5,
        label='AI-assisted (including violation repair)', zorder=5)

# Shaded regions
ax.axvspan(1, cross_x, alpha=0.06, color=GREEN, zorder=1)
ax.text(cross_x * 0.4, 1.0, 'Net Benefit\nfrom AI', ha='center', va='center',
        color=GREEN, fontsize=11, fontweight='bold', linespacing=1.3)

ax.axvspan(cross_x, 500, alpha=0.05, color=RED, zorder=1)
ax.text(cross_x + (500 - cross_x) * 0.5, 1.0, 'Net Damage\nfrom AI', ha='center', va='center',
        color=RED, fontsize=11, fontweight='bold', linespacing=1.3)

# Crossover point
ax.scatter([cross_x], [cross_y], s=250, color=ORANGE, edgecolors=WHITE, linewidth=2, zorder=7)
ax.annotate('Crossover: ~%d constraints\n"Some help" becomes\nactive destruction' % int(cross_x),
            xy=(cross_x, cross_y), xytext=(cross_x + 80, cross_y + 2.5),
            color=ORANGE, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.9),
            linespacing=1.3)

# Reference landmarks
for cx, label in [(15, 'Tutorial\nproject'), (100, 'Moderate\nsystem'), (450, 'Game\nengine')]:
    ax.axvline(x=cx, color=DIM, linewidth=1, linestyle=':', alpha=0.4)
    ylim_top = ax.get_ylim()[1]
    ax.text(cx, ylim_top * 0.92, label, ha='center', va='top', color=DIM, fontsize=8,
            linespacing=1.3)

ax.set_xlim(-10, 520)
y_max = max(np.max(direct_cost), np.max(ai_total_cost)) * 1.1
ax.set_ylim(0, y_max)

ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm2_05_constraint_violation_cost.png')


# ================================================================
# FIG 6: TECHNICAL DEBT ACCUMULATION (SCISSORS)
# Type: Running/Convergence (Type 1)
# Shows: Two diverging curves over time — code volume rising
#        steeply, code quality/maintainability declining.
#        The growing gap between them IS the technical debt.
#        Industry data points annotated.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'The AI Scissors: Volume vs. Quality Over Time',
         xlabel='Months After AI Tool Adoption',
         ylabel='Index (baseline = 100 at adoption)')

months = np.linspace(0, 24, 200)

# Code volume: grows steeply with AI assistance
volume = 100 + 55 * (1 - np.exp(-months / 4.0)) * (1 + months / 20.0)

# Code quality: declines as unreviewed AI code accumulates
quality = 100 - 8 * months ** 0.7

# Ensure quality doesn't go below 25
quality = np.maximum(quality, 25)

ax.plot(months, volume, color=CYAN, linewidth=2.5, label='Code Volume (output rate)', zorder=5)
ax.plot(months, quality, color=MAG, linewidth=2.5, label='Code Quality (maintainability)', zorder=5)

# Fill the gap (technical debt)
ax.fill_between(months, quality, volume, alpha=0.07, color=RED, zorder=2)

# Label the gap
ax.annotate('Growing\nTechnical Debt',
            xy=(16, (volume[133] + quality[133]) / 2.0),
            xytext=(18.5, 120),
            color=RED, fontsize=12, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.9),
            linespacing=1.3)

# Industry data points
data_points = [
    (6, 135, '+30-55%% output\n(McKinsey)', CYAN, 'right'),
    (6, 65, '+30-41%% debt\nin 6 months', MAG, 'right'),
    (12, 55, '1.7x more issues\nin AI-assisted PRs', RED, 'left'),
    (24, 40, '4x maintenance cost\nby year 2', ORANGE, 'left'),
]

for dx, dy, label, color, ha_dir in data_points:
    ax.scatter([dx], [dy], s=180, color=color, edgecolors=WHITE, linewidth=1.5, zorder=6)
    x_offset = -30 if ha_dir == 'right' else 30
    ax.annotate(label, xy=(dx, dy),
                xytext=(dx + (2.0 if ha_dir == 'left' else -2.0), dy + 8),
                color=color, fontsize=9,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8),
                linespacing=1.3)

# 39% churn annotation
ax.text(20, 165, '39%% increase in code churn\n(GitClear, 100M+ lines analyzed)',
        ha='center', va='center', color=SILVER, fontsize=9,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.9),
        linespacing=1.3)

# Baseline
ax.axhline(y=100, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(0.3, 102, 'Baseline at adoption', color=DIM, fontsize=8)

ax.set_xlim(-0.5, 25)
ax.set_ylim(20, 185)

ax.legend(loc='lower left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm2_06_technical_debt_scissors.png')


# ================================================================
# FIG 7: CONTEXT WINDOW COMPOSITION
# Type: Progression/Sequence (Type 7)
# Shows: How the context window fills during a session — system
#        prompt, loaded docs, probe/correction exchanges, and
#        remaining generation budget. Visualized as a horizontal
#        stacked bar showing proportional consumption.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
setup_ax(ax, 'Context Window Budget: Calibration vs. Generation Capacity', ylabel='')

# Three scenarios as horizontal stacked bars
scenarios = ['No Calibration', 'Light Calibration', 'Full Calibration']
y_positions = [2.4, 1.4, 0.4]
bar_h = 0.55

# Components as fractions of total context window
# [system_prompt, loaded_docs, probes, corrections, generation_remaining]
components = [
    [0.05, 0.00, 0.00, 0.00, 0.95],   # No calibration
    [0.05, 0.15, 0.10, 0.05, 0.65],   # Light calibration
    [0.05, 0.25, 0.15, 0.10, 0.45],   # Full calibration
]

colors_bar = [DIM, BLUE, CYAN, MAG, GREEN]
labels_bar = ['System Prompt', 'Loaded Docs', 'Probe Exchanges', 'Corrections', 'Generation Budget']

for idx in range(3):
    left = 0.0
    for comp_idx in range(5):
        width = components[idx][comp_idx]
        if width > 0:
            bar_color = colors_bar[comp_idx]
            alpha_val = 0.7 if comp_idx < 4 else 0.5
            ax.barh(y_positions[idx], width, left=left, height=bar_h,
                    color=bar_color, alpha=alpha_val, edgecolor=WHITE, linewidth=0.5, zorder=3)
            if width >= 0.08:
                ax.text(left + width / 2.0, y_positions[idx], '%d%%' % int(width * 100),
                        ha='center', va='center', color=WHITE, fontsize=9, fontweight='bold')
            left += width

    # Scenario label
    ax.text(-0.03, y_positions[idx], scenarios[idx], ha='right', va='center',
            color=SILVER, fontsize=11, fontweight='bold')

# Quality annotations on the right
quality_notes = [
    (2.4, 'Output: training-weight median\n(uncorrected, generic)', RED),
    (1.4, 'Output: partially aligned\n(major constraints loaded)', ORANGE),
    (0.4, 'Output: calibrated to system\n(verified representations)', GREEN),
]

for y, note, color in quality_notes:
    ax.text(1.03, y, note, ha='left', va='center', color=color, fontsize=9,
            linespacing=1.3)

# Legend
legend_patches = []
for i in range(5):
    legend_patches.append(mpatches.Patch(facecolor=colors_bar[i],
                                          alpha=0.7 if i < 4 else 0.5,
                                          edgecolor=WHITE, linewidth=0.5,
                                          label=labels_bar[i]))
ax.legend(handles=legend_patches, loc='upper right',
          facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9,
          ncol=3)

# Key insight
ax.text(0.5, 3.25,
        'Calibration consumes context budget but improves output quality.\n'
        'The tradeoff: less generation capacity, but what generates is aligned to the system.',
        ha='center', va='center', color=GOLD, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9),
        linespacing=1.4)

ax.set_xlim(-0.35, 1.55)
ax.set_ylim(-0.15, 3.65)
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'], color=DIM, fontsize=9)
ax.set_yticks([])
ax.set_xlabel('Context Window Usage', color=SILVER, fontsize=11)

save(fig, 'llm2_07_context_window_composition.png')


# ================================================================
# FIG 8: INTERFACE CORRECTION CHANNEL COMPARISON
# Type: Comparison Bar Chart (Type 6)
# Shows: Four interfaces with bars showing correction opportunities
#        per generation cycle. Chat is the only bar with meaningful
#        height. Visual elimination: one bar standing.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Correction Opportunities Per Generation Cycle by Interface',
         xlabel='', ylabel='Correction Opportunities')

interfaces = ['Tab\nComplete', 'Agentic\n(Autonomous)', 'Multi-Agent\nOrchestration', 'Chat\n(Interactive)']
opportunities = [0.1, 0.3, 0.1, 8.0]  # Chat gets ~8 correction points per cycle
bar_colors = [RED, RED, RED, GREEN]
bar_x = np.arange(4)

bars = ax.bar(bar_x, opportunities, width=0.55, color=bar_colors, alpha=0.7,
              edgecolor=WHITE, linewidth=1.5, zorder=4)

# Value labels on bars
for i, (bx, val) in enumerate(zip(bar_x, opportunities)):
    label_text = '%.0f' % val if val >= 1 else ('~0' if val <= 0.1 else '~0')
    y_pos = val + 0.25
    ax.text(bx, y_pos, label_text, ha='center', va='bottom',
            color=bar_colors[i], fontsize=12, fontweight='bold')

# Annotations for why each is low/high
annotations = [
    (0, 'Accept or reject.\nNo diagnosis.\nNo correction.', RED),
    (1, 'Agent iterates against\ntest output, not\nconstraint surface.', RED),
    (2, 'Same model, different\npersona prompts.\nNo correction channel.', RED),
    (3, 'Observe. Diagnose.\nCorrect. Verify.\nThen generate.', GREEN),
]

for bx, text, color in annotations:
    y_base = opportunities[bx]
    ax.text(bx, y_base + 1.2, text, ha='center', va='bottom',
            color=color, fontsize=9, linespacing=1.4,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color, alpha=0.8))

# Key insight
ax.text(1.5, 9.0,
        'The correction channel is the feature.\n'
        'Only chat provides it.',
        ha='center', va='center', color=GOLD, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9),
        linespacing=1.4)

ax.set_xticks(bar_x)
ax.set_xticklabels(interfaces, color=SILVER, fontsize=10)
ax.set_xlim(-0.6, 3.6)
ax.set_ylim(0, 10.5)

save(fig, 'llm2_08_correction_channel_comparison.png')


# ================================================================
# SUMMARY
# ================================================================

print("\n=== HOWL LLM-2 Diagrams Complete ===")
filenames = [
    'llm2_01_system_scale_landscape.png',
    'llm2_02_ceiling_stability.png',
    'llm2_03_coherence_degradation.png',
    'llm2_04_calibration_distribution.png',
    'llm2_05_constraint_violation_cost.png',
    'llm2_06_technical_debt_scissors.png',
    'llm2_07_context_window_composition.png',
    'llm2_08_correction_channel_comparison.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
print("=== Done ===")
