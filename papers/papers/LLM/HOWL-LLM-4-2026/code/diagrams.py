#!/usr/bin/env python3
"""
HOWL LLM-3 Diagrams — Riding the Rocket: Why LLM Generation Is Ballistic, Not Steerable
8 figures covering ballistic generation model, speed constraints, comprehension costs,
and the honest productivity multiplier.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge, FancyBboxPatch
from matplotlib.lines import Line2D
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
    ax.set_title(title, color=GOLD, fontsize=title_size, fontweight='bold', pad=18)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11, labelpad=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11, labelpad=10)
    ax.tick_params(colors=DIM, labelsize=9, pad=6)
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
# FIG 1: BALLISTIC CONE — GENERATION LANDING ZONE
# Type: Geometric Cross-Section (Type 4)
# Shows: Top-down view of target with concentric deviation cones
#        at different calibration quality levels. At 1200-line
#        distance, even small angular errors produce large
#        positional displacement.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14), facecolor=BG)
setup_ax(ax, 'Ballistic Cone: Where Generation Lands vs. Where You Aimed', title_size=14)
ax.set_aspect('equal')
ax.axis('off')

origin_x, origin_y = 0.0, 0.0
distance = 12.0  # represents 1200 lines scaled

# Label offsets: (x_offset, y_offset) from the computed endpoint position
# Adjust these to fix overlaps
label_offset_no_cal      = (1.5, 0.0)
label_offset_minimal_cal = (1.5, 0.0)
label_offset_moderate_cal = (1.5, 2.5)
label_offset_full_cal    = (1.5, 4.0)

label_offsets = [
    label_offset_no_cal,
    label_offset_minimal_cal,
    label_offset_moderate_cal,
    label_offset_full_cal,
]

# Origin label offset
origin_label_x_off = 0.0
origin_label_y_off = -1.4

# Target label offset
target_label_x_off = 0.8
target_label_y_off = 0.6

# Distance label offset
dist_label_x = -8.0
dist_label_y_center = 6.0

# Draw cones from origin to landing zone at distance
cone_specs = [
    (60, 'No Calibration\n(training weights only)', RED, 0.04),
    (30, 'Minimal Calibration\n(docs loaded, no probing)', ORANGE, 0.05),
    (15, 'Moderate Calibration\n(probed, some correction)', CYAN, 0.06),
    (5, 'Full Calibration\n(verified representations)', GREEN, 0.08),
]

# Draw cones as wedges from origin
for angle_deg, label, color, alpha_val in cone_specs:
    wedge = Wedge(
        (origin_x, origin_y),
        distance * 1.05,
        90 - angle_deg,
        90 + angle_deg,
        facecolor=color,
        alpha=alpha_val,
        edgecolor=color,
        linewidth=1.0,
        zorder=2
    )
    ax.add_patch(wedge)

# Target line (straight up)
ax.plot([origin_x, origin_x], [origin_y, distance], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.7, zorder=5)

# Arc length annotations at the landing distance
for i, (angle_deg, label, color, alpha_val) in enumerate(cone_specs):
    angle_rad = np.radians(angle_deg)
    arc_length = distance * np.tan(angle_rad)

    # Right side endpoint
    end_x = origin_x + distance * np.sin(angle_rad)
    end_y = origin_y + distance * np.cos(angle_rad)

    # Cone edge lines
    ax.plot([origin_x, end_x], [origin_y, end_y], color=color, linewidth=1.2,
            alpha=0.5, zorder=3)
    ax.plot([origin_x, -end_x], [origin_y, end_y], color=color, linewidth=1.2,
            alpha=0.5, zorder=3)

    # Label position: endpoint + offset
    x_off, y_off = label_offsets[i]
    label_x = end_x + x_off
    label_y = end_y + y_off

    arc_lines = int(arc_length * 100)  # scale to lines
    full_label = "%s\n+/-%d degrees\n~%d lines off target" % (label, angle_deg, arc_lines)

    # Arrow from label to endpoint
    ax.annotate(full_label,
                xy=(end_x, end_y),
                xytext=(label_x, label_y),
                color=color, fontsize=8, linespacing=1.5,
                ha='left', va='center',
                arrowprops=dict(arrowstyle='->', color=color, lw=1.0, alpha=0.6),
                bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=color, alpha=0.85))

# Origin marker
ax.scatter([origin_x], [origin_y], s=250, color=GOLD, edgecolors=WHITE,
           linewidth=2, zorder=6)
ax.text(origin_x + origin_label_x_off, origin_y + origin_label_y_off,
        'Prompt\n(launch point)', ha='center', va='top',
        color=GOLD, fontsize=10, fontweight='bold', linespacing=1.4)

# Target marker
ax.scatter([origin_x], [distance], s=250, color=GOLD, edgecolors=WHITE,
           linewidth=2, zorder=6, marker='*')
ax.text(origin_x + target_label_x_off, distance + target_label_y_off,
        'Intended Target', ha='left', va='bottom',
        color=GOLD, fontsize=10, fontweight='bold')

# Distance label
ax.text(dist_label_x, dist_label_y_center, '~1,200 lines\nof generation',
        ha='center', va='center',
        color=SILVER, fontsize=10, rotation=90, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=DIM, alpha=0.85))

ax.set_xlim(-10.0, 18.0)
ax.set_ylim(-3.0, 16.5)

save(fig, 'llm3_01_ballistic_cone.png')

# ================================================================
# FIG 2: SPEED RANGE — NO NAVIGABLE MODE
# Type: Scale/Landscape (Type 2)
# Shows: Horizontal axis from 0 to 1400 lines. Hand-coding zone
#        (0-50, navigable), dead zone (50-400, model won't
#        generate this little), ballistic zone (400-1200).
#        The navigable zone and generation zone do not overlap.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
setup_ax(ax, 'Speed Range: No Navigable Mode Exists', ylabel='')
ax.axis('off')

y_center = 0.5
bar_height = 0.12

# Main axis line
ax.plot([0, 1400], [y_center, y_center], color=SILVER, linewidth=2, zorder=3)

# Zones as shaded regions
# Navigable zone: 0-50
ax.barh(y_center, 50, left=0, height=bar_height, color=GREEN, alpha=0.35,
        edgecolor=GREEN, linewidth=1.5, zorder=4)
ax.text(25, y_center + 0.13, 'Navigable\nZone', ha='center', va='bottom',
        color=GREEN, fontsize=11, fontweight='bold', linespacing=1.4)
ax.text(25, y_center - 0.13, '0-50 lines\nHand-coding:\nyou make every\ndecision as you go',
        ha='center', va='top', color=GREEN, fontsize=8, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN, alpha=0.8))

# Dead zone: 50-400
ax.barh(y_center, 350, left=50, height=bar_height, color=DIM, alpha=0.15,
        edgecolor=DIM, linewidth=1.0, zorder=4)
ax.text(225, y_center + 0.13, 'Dead Zone', ha='center', va='bottom',
        color=DIM, fontsize=11, fontweight='bold', linespacing=1.4)
ax.text(225, y_center - 0.13, '50-400 lines\nModel inflates\npast this range.\nYou cannot request\ngeneration this small.',
        ha='center', va='top', color=DIM, fontsize=8, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.8))

# Ballistic zone: 400-1200
ax.barh(y_center, 800, left=400, height=bar_height, color=CYAN, alpha=0.30,
        edgecolor=CYAN, linewidth=1.5, zorder=4)
ax.text(800, y_center + 0.13, 'Ballistic Zone', ha='center', va='bottom',
        color=CYAN, fontsize=11, fontweight='bold', linespacing=1.4)
ax.text(800, y_center - 0.13, '400-1,200 lines\nLLM generation range.\nNo steering during flight.\nAll decisions made by model.',
        ha='center', va='top', color=CYAN, fontsize=8, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN, alpha=0.8))

# Ceiling marker
ax.plot([1200, 1200], [y_center - 0.08, y_center + 0.08], color=RED, linewidth=2.5, zorder=5)
ax.text(1200, y_center + 0.22, 'Coherence\nCeiling', ha='center', va='bottom',
        color=RED, fontsize=10, fontweight='bold', linespacing=1.4)

# The gap annotation
ax.annotate('', xy=(50, y_center + 0.25), xytext=(400, y_center + 0.25),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(225, y_center + 0.29, 'THE GAP: No mode exists here.\nYou either navigate (0-50) or ride the rocket (400-1200).',
        ha='center', va='bottom', color=ORANGE, fontsize=9, fontweight='bold', linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=ORANGE, alpha=0.9))

# Tick marks
for pos in [0, 50, 100, 200, 400, 600, 800, 1000, 1200, 1400]:
    ax.plot([pos, pos], [y_center - 0.03, y_center + 0.03], color=SILVER, linewidth=1, zorder=3)
    ax.text(pos, y_center - 0.045, str(pos), ha='center', va='top', color=DIM, fontsize=7)

ax.text(700, y_center - 0.42, 'Output Length (lines of real code)', ha='center', va='center',
        color=SILVER, fontsize=11)

ax.set_xlim(-80, 1500)
ax.set_ylim(-0.05, 1.0)

save(fig, 'llm3_02_speed_range.png')


# ================================================================
# FIG 3: EXPANSION BIAS OVER SESSION LENGTH
# Type: Running/Convergence (Type 1)
# Shows: Actual output length vs requested output length over
#        successive prompts within a session. Actual expands
#        toward ceiling; requested stays flat.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Expansion Bias: Output Length Grows With Each Prompt',
         xlabel='Successive Prompts in Session',
         ylabel='Output Length (lines)')

prompts = np.arange(1, 11)

# Requested: stays roughly flat at ~200
requested = np.array([200, 200, 180, 200, 220, 200, 200, 180, 200, 200])

# Actual: starts around 400, trends toward 1200
actual = np.array([420, 480, 550, 640, 720, 810, 890, 980, 1050, 1140])

ax.plot(prompts, requested, color=GREEN, linewidth=2.5, marker='o', markersize=8,
        markeredgecolor=WHITE, markeredgewidth=1.5, label='Requested output size', zorder=5)
ax.plot(prompts, actual, color=MAG, linewidth=2.5, marker='s', markersize=8,
        markeredgecolor=WHITE, markeredgewidth=1.5, label='Actual output produced', zorder=5)

# Fill the gap
ax.fill_between(prompts, requested, actual, alpha=0.08, color=RED, zorder=2)

# Ceiling line
ax.axhline(y=1200, color=RED, linewidth=1.5, linestyle='--', alpha=0.6, zorder=3)
ax.text(10.3, 1200, 'Coherence\nCeiling', ha='left', va='center',
        color=RED, fontsize=9, fontweight='bold', linespacing=1.4)

# Floor line
ax.axhline(y=400, color=ORANGE, linewidth=1.0, linestyle=':', alpha=0.5, zorder=3)
ax.text(10.3, 400, 'Generation\nFloor', ha='left', va='center',
        color=ORANGE, fontsize=9, linespacing=1.4)

# Gap annotation
ax.annotate('Expansion gap:\nmodel produces 2-5x\nwhat was requested',
            xy=(7, (actual[6] + requested[6]) / 2.0),
            xytext=(3.5, 900),
            color=ORANGE, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=ORANGE, alpha=0.9),
            linespacing=1.4)

# Context growth note
ax.text(8.5, 550, 'Context grows with\neach prompt, pushing\nmodel toward longer\noutput', ha='center',
        va='center', color=SILVER, fontsize=9, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.85))

ax.set_xlim(0.3, 11.5)
ax.set_ylim(0, 1400)
ax.set_xticks(prompts)

ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm3_03_expansion_bias.png')


# ================================================================
# FIG 4: JOURNEY VS DESTINATION — UNDERSTANDING ACCUMULATION
# Type: Running/Convergence (Type 1)
# Shows: Two processes producing the same code. Hand-coding:
#        code completion and understanding rise together.
#        LLM generation: code completion jumps instantly,
#        understanding starts near zero, rises slowly through
#        examination. The gap between understanding curves is
#        the comprehension cost.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Journey vs. Destination: Where Understanding Comes From',
         xlabel='Time Invested',
         ylabel='Completion / Understanding (%%)')

t = np.linspace(0, 10, 200)

# Hand-coding: both rise together, roughly linearly with slight curve
hand_code = 100 * (1 - np.exp(-t / 4.0))
hand_understand = 95 * (1 - np.exp(-t / 4.2))  # slightly behind, nearly parallel

# LLM generation: code completion jumps at t=0.5, understanding lags
llm_code = np.where(t < 0.5, t * 20, np.minimum(100, 95 + t * 0.5))
llm_understand = np.where(t < 0.5, 0, 80 * (1 - np.exp(-(t - 0.5) / 5.0)))

# Hand-coding curves
ax.plot(t, hand_code, color=GREEN, linewidth=2.5, label='Hand-coded: code completion', zorder=5)
ax.plot(t, hand_understand, color=GREEN, linewidth=2.5, linestyle='--',
        label='Hand-coded: understanding', zorder=5)

# LLM curves
ax.plot(t, llm_code, color=CYAN, linewidth=2.5, label='LLM: code completion', zorder=5)
ax.plot(t, llm_understand, color=CYAN, linewidth=2.5, linestyle='--',
        label='LLM: understanding', zorder=5)

# Fill the comprehension gap for LLM
ax.fill_between(t, llm_understand, llm_code, alpha=0.06, color=RED, zorder=2)

# Annotations
# The instant jump
ax.annotate('Code appears\ninstantly',
            xy=(0.5, 95), xytext=(1.8, 105),
            color=CYAN, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.3),
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN, alpha=0.85),
            linespacing=1.4)

# The understanding gap
ax.annotate('Comprehension\ncost: the gap\nyou must close\nby examination',
            xy=(5, (llm_code[100] + llm_understand[100]) / 2.0),
            xytext=(6.5, 35),
            color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED, alpha=0.9),
            linespacing=1.4)

# Hand-coding note
ax.text(7.5, 80, 'Hand-coding:\nunderstanding is\na free byproduct\nof the journey',
        ha='center', va='center', color=GREEN, fontsize=9, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN, alpha=0.85))

ax.set_xlim(-0.3, 10.8)
ax.set_ylim(-5, 115)

ax.legend(loc='lower right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9,
          ncol=2)

save(fig, 'llm3_04_journey_vs_destination.png')


# ================================================================
# FIG 5: SPLASH DAMAGE VS DISTANCE GAINED
# Type: Threshold/Region (Type 3)
# Shows: Scatter of task types plotted by distance gained (useful
#        output) vs comprehension cost (hours). Break-even line
#        where comprehension cost equals hand-coding time. Points
#        above are net positive, below are net negative.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Splash Damage vs. Distance Gained',
         xlabel='Useful Output (lines of working code)',
         ylabel='Total Cost Including Comprehension (hours)')

# Break-even line: hand-coding rate ~40 lines/hour
hand_rate = 40.0
x_range = np.linspace(50, 1200, 200)
breakeven = x_range / hand_rate

ax.plot(x_range, breakeven, color=ORANGE, linewidth=2, linestyle='--', zorder=4,
        label='Break-even: hand-coding speed')

# Task clusters
tasks = [
    # (output_lines, total_hours, label, color, marker)
    (100, 0.3, 'Boilerplate\nstruct', GREEN, 'o'),
    (150, 0.5, 'Utility\nfunction', GREEN, 'o'),
    (300, 1.5, 'Data\ntransform', GREEN, 'o'),
    (400, 3.0, 'API\nendpoint', CYAN, 's'),
    (500, 5.0, 'Module\n(known pattern)', CYAN, 's'),
    (600, 7.0, 'New routine\n(moderate)', CYAN, 's'),
    (800, 14.0, 'Complex\nmodule', MAG, 'D'),
    (1000, 22.0, 'System\nintegration', MAG, 'D'),
    (1200, 35.0, 'Multi-concern\nmodule', RED, 'D'),
    (200, 8.0, 'Security-\ncritical', RED, 'D'),
]

for out_lines, hours, label, color, marker in tasks:
    ax.scatter([out_lines], [hours], s=200, color=color, edgecolors=WHITE,
              linewidth=1.5, marker=marker, zorder=6)
    # Offset labels to avoid overlap
    x_off = 35
    y_off = 0.8
    if out_lines >= 800:
        x_off = -45
        y_off = 1.2
    if label.startswith('Security'):
        x_off = 45
        y_off = -0.5
    ax.text(out_lines + x_off, hours + y_off, label, ha='left', va='bottom',
            color=color, fontsize=8, linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color, alpha=0.75))

# Shade regions
ax.fill_between(x_range, 0, breakeven, alpha=0.05, color=GREEN, zorder=1)
ax.fill_between(x_range, breakeven, 40, alpha=0.04, color=RED, zorder=1)

ax.text(900, 5, 'Net Positive:\ngeneration faster\nthan hand-coding', ha='center', va='center',
        color=GREEN, fontsize=10, fontweight='bold', linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GREEN, alpha=0.85))

ax.text(350, 28, 'Net Negative:\ncomprehension cost\nexceeds hand-coding time', ha='center', va='center',
        color=RED, fontsize=10, fontweight='bold', linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED, alpha=0.85))

ax.set_xlim(0, 1350)
ax.set_ylim(0, 40)

ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm3_05_splash_damage_distance.png')


# ================================================================
# FIG 6: ACCUMULATION — COHERENCE DECAY ACROSS MODULE COUNT
# Type: Running/Convergence (Type 1)
# Shows: Cross-module coherence on Y vs module count on X.
#        Hand-coded: slight gradual decline. LLM-generated:
#        steep decline as each module is a separate ballistic
#        landing. Curves diverge with scale.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'Cross-Module Coherence: Hand-Coded vs. LLM-Generated',
         xlabel='Number of Modules in System',
         ylabel='Cross-Module Coherence (%%)')

modules = np.linspace(1, 500, 500)

# Hand-coded: slow, gentle decline — one mind maintaining consistency
hand_coherence = 95 - 12 * np.log10(modules + 1)

# LLM-generated: steeper decline — each module is independent landing
llm_coherence = 95 - 35 * np.log10(modules + 1)
llm_coherence = np.maximum(llm_coherence, 15)

ax.plot(modules, hand_coherence, color=GREEN, linewidth=2.5,
        label='Hand-coded (single engineer)', zorder=5)
ax.plot(modules, llm_coherence, color=MAG, linewidth=2.5,
        label='LLM-generated (separate sessions)', zorder=5)

# Fill the divergence
ax.fill_between(modules, llm_coherence, hand_coherence, alpha=0.06, color=RED, zorder=2)

# Landmark markers
landmarks = [
    (10, 'Tutorial\nproject', CYAN),
    (50, 'Small\nsystem', BLUE),
    (150, 'Medium\nsystem', ORANGE),
    (450, 'Production\ngame engine', GOLD),
]

for mod_count, label, color in landmarks:
    idx = int(mod_count) - 1
    hand_y = hand_coherence[idx]
    llm_y = llm_coherence[idx]

    ax.axvline(x=mod_count, color=DIM, linewidth=0.8, linestyle=':', alpha=0.4, zorder=3)

    ax.scatter([mod_count], [hand_y], s=150, color=GREEN, edgecolors=WHITE,
              linewidth=1.5, zorder=6)
    ax.scatter([mod_count], [llm_y], s=150, color=MAG, edgecolors=WHITE,
              linewidth=1.5, zorder=6)

    gap = hand_y - llm_y
    ax.text(mod_count, hand_y + 5, '%s\ngap: %.0f%%' % (label, gap),
            ha='center', va='bottom', color=color, fontsize=8, linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color, alpha=0.8))

# Divergence annotation
ax.text(300, 55, 'Each LLM-generated module is a\nseparate ballistic landing.\nNo shared decision-making\nproduces no shared coherence.',
        ha='center', va='center', color=SILVER, fontsize=9, linespacing=1.4,
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=DIM, alpha=0.9))

ax.set_xlim(-15, 530)
ax.set_ylim(10, 105)

ax.legend(loc='lower left', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'llm3_06_accumulation_coherence.png')


# ================================================================
# FIG 7: DECISION FRAMEWORK — FIRE VS WALK REGIONS
# Type: Threshold/Region (Type 3)
# Shows: 2D plot with task complexity on X and constraint density
#        on Y. Four quadrants: fire (green), fire with caution
#        (yellow), evaluate (orange), walk (red). Task type
#        labels placed in each region.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12), facecolor=BG)
setup_ax(ax, 'Decision Framework: When to Fire and When to Walk',
         xlabel='Task Complexity',
         ylabel='System Constraint Density')

# Quadrant boundaries
mid_x = 5.0
mid_y = 5.0

# Shade quadrants
# Low complexity, low constraint = FIRE
ax.fill([0, mid_x, mid_x, 0], [0, 0, mid_y, mid_y],
        color=GREEN, alpha=0.08, zorder=1)

# Low complexity, high constraint = FIRE WITH CAUTION
ax.fill([0, mid_x, mid_x, 0], [mid_y, mid_y, 10, 10],
        color=ORANGE, alpha=0.06, zorder=1)

# High complexity, low constraint = EVALUATE
ax.fill([mid_x, 10, 10, mid_x], [0, 0, mid_y, mid_y],
        color=CYAN, alpha=0.06, zorder=1)

# High complexity, high constraint = WALK
ax.fill([mid_x, 10, 10, mid_x], [mid_y, mid_y, 10, 10],
        color=RED, alpha=0.06, zorder=1)

# Boundary lines
ax.axvline(x=mid_x, color=DIM, linewidth=1.5, linestyle='-', alpha=0.4, zorder=3)
ax.axhline(y=mid_y, color=DIM, linewidth=1.5, linestyle='-', alpha=0.4, zorder=3)

# Quadrant labels with large text
quad_labels = [
    (2.5, 2.5, 'FIRE', GREEN, 18),
    (2.5, 7.5, 'FIRE WITH\nCAUTION', ORANGE, 14),
    (7.5, 2.5, 'EVALUATE\nCASE BY CASE', CYAN, 13),
    (7.5, 7.5, 'WALK', RED, 18),
]

for qx, qy, qlabel, qcolor, qsize in quad_labels:
    ax.text(qx, qy, qlabel, ha='center', va='center', color=qcolor,
            fontsize=qsize, fontweight='bold', alpha=0.6, linespacing=1.4)

# Task type examples as scatter points
task_examples = [
    (1.5, 1.0, 'Boilerplate\nstruct', GREEN),
    (2.0, 2.5, 'Utility\nfunction', GREEN),
    (3.0, 1.5, 'Data\ntransform', GREEN),
    (3.5, 3.5, 'Known-pattern\nmodule', GREEN),
    (1.5, 6.5, 'Constrained\nboilerplate', ORANGE),
    (3.0, 7.5, 'Convention-heavy\nmodule', ORANGE),
    (4.0, 8.5, 'Security\nboilerplate', ORANGE),
    (6.5, 2.0, 'Novel\nalgorithm', CYAN),
    (7.5, 3.0, 'Complex\nbusiness logic', CYAN),
    (8.5, 1.5, 'Performance-\ncritical path', CYAN),
    (6.5, 6.5, 'Architectural\ncode', RED),
    (7.5, 8.0, 'Cross-module\nintegration', RED),
    (8.5, 7.5, 'Constraint-surface\ndesign', RED),
    (9.0, 9.0, 'System-wide\nrefactor', RED),
]

for tx, ty, tlabel, tcolor in task_examples:
    ax.scatter([tx], [ty], s=120, color=tcolor, edgecolors=WHITE,
              linewidth=1.5, zorder=6)
    # Offset labels
    x_off = 0.35
    y_off = 0.3
    ha_val = 'left'
    if tx > 8:
        x_off = -0.35
        ha_val = 'right'
    ax.text(tx + x_off, ty + y_off, tlabel, ha=ha_val, va='bottom',
            color=tcolor, fontsize=7, linespacing=1.3,
            bbox=dict(boxstyle='round,pad=0.35', facecolor=BG, edgecolor=tcolor, alpha=0.7))

# Axis labels at extremes
ax.text(0.3, -0.7, 'Low', ha='center', va='center', color=DIM, fontsize=9)
ax.text(9.7, -0.7, 'High', ha='center', va='center', color=DIM, fontsize=9)
ax.text(-0.8, 0.3, 'Low', ha='center', va='center', color=DIM, fontsize=9)
ax.text(-0.8, 9.7, 'High', ha='center', va='center', color=DIM, fontsize=9)

ax.set_xlim(-1.2, 10.5)
ax.set_ylim(-1.2, 10.5)
ax.set_xticks([])
ax.set_yticks([])

save(fig, 'llm3_07_decision_framework.png')


# ================================================================
# FIG 8: HONEST MULTIPLIER BY TASK CATEGORY
# Type: Comparison Bar Chart (Type 6)
# Shows: Three task categories with honest multiplier ranges.
#        Small/isolated: 2-5x. Medium/constrained: 1-2x.
#        Large/complex: 0.5-1x. Break-even at 1x marked.
#        Industry "100x" shown at absurd scale for reference.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
setup_ax(ax, 'The Honest Multiplier by Task Category',
         xlabel='', ylabel='Productivity Multiplier')

categories = ['Small, Isolated\nDisposable', 'Medium, Constrained\nMaintained', 'Large, Complex\nLong-lived']
x_pos = np.array([0, 1.3, 2.6])
bar_width = 0.7

# Multiplier ranges (show as bars from low to high of range)
ranges_low = [2.0, 1.0, 0.5]
ranges_high = [5.0, 2.0, 1.0]
ranges_mid = [(l + h) / 2.0 for l, h in zip(ranges_low, ranges_high)]
bar_colors = [GREEN, CYAN, RED]

for i in range(3):
    # Bar from low to high
    bar_bottom = ranges_low[i]
    bar_h = ranges_high[i] - ranges_low[i]
    ax.bar(x_pos[i], bar_h, bottom=bar_bottom, width=bar_width,
           color=bar_colors[i], alpha=0.65, edgecolor=WHITE, linewidth=1.5, zorder=4)

    # Range label on bar
    ax.text(x_pos[i], ranges_high[i] + 0.25, '%.1fx - %.1fx' % (ranges_low[i], ranges_high[i]),
            ha='center', va='bottom', color=bar_colors[i], fontsize=11, fontweight='bold')

    # Midpoint marker
    ax.scatter([x_pos[i]], [ranges_mid[i]], s=120, color=WHITE, edgecolors=bar_colors[i],
              linewidth=2, zorder=6)

# Break-even line
ax.axhline(y=1.0, color=ORANGE, linewidth=2, linestyle='--', alpha=0.7, zorder=3)
ax.text(3.2, 1.08, 'Break-even (1x)', ha='left', va='bottom',
        color=ORANGE, fontsize=10, fontweight='bold')

# Industry claim reference
ax.annotate('Industry claim:\n"100x"',
            xy=(1.3, 7.0), xytext=(2.8, 6.5),
            color=DIM, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2),
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM, alpha=0.8),
            linespacing=1.4)
ax.text(1.3, 7.3, '100x would be here\n(off chart by 13x)', ha='center', va='bottom',
        color=DIM, fontsize=8, linespacing=1.3)

# Below break-even annotation
ax.text(2.6, 0.35, 'Can go negative:\ncomprehension cost\nexceeds generation\nsavings',
        ha='center', va='center', color=RED, fontsize=8, linespacing=1.3,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED, alpha=0.8))

# Most credible self-report
ax.axhline(y=2.0, color=GOLD, linewidth=1, linestyle=':', alpha=0.4, zorder=3)
ax.text(3.2, 2.08, 'Most credible self-report:\n"about 2x" (selective use)',
        ha='left', va='bottom', color=GOLD, fontsize=9, linespacing=1.3)

ax.set_xticks(x_pos)
ax.set_xticklabels(categories, color=SILVER, fontsize=10)
ax.set_xlim(-0.6, 4.0)
ax.set_ylim(0, 7.8)

save(fig, 'llm3_08_honest_multiplier.png')


# ================================================================
# SUMMARY
# ================================================================

print("\n=== HOWL LLM-3 Diagrams Complete ===")
filenames = [
    'llm3_01_ballistic_cone.png',
    'llm3_02_speed_range.png',
    'llm3_03_expansion_bias.png',
    'llm3_04_journey_vs_destination.png',
    'llm3_05_splash_damage_distance.png',
    'llm3_06_accumulation_coherence.png',
    'llm3_07_decision_framework.png',
    'llm3_08_honest_multiplier.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
print("=== Done ===")
