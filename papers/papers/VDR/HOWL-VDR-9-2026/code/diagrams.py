
#!/usr/bin/env python3
"""
HOWL VDR-9 Diagrams — Orchestrated Inference
8 figures covering the inference loop, confidence propagation,
evidence convergence, source spectrum, budget management,
threshold regions, notebook nesting, and system identity.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
import os

# ── output directory ──────────────────────────────────────────────
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── colour palette ────────────────────────────────────────────────

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



def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def make_box(ax, x, y, w, h, text, color, fontsize=9, textcolor=WHITE, alpha=0.85, lw=1.8):
    """Draw a rounded box with text centered inside, with generous padding."""
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.15",
                          facecolor=PAN, edgecolor=color,
                          linewidth=lw, alpha=alpha, zorder=2)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=textcolor, zorder=3, fontweight='bold')
    return box

def draw_arrow(ax, x1, y1, x2, y2, color=DIM, lw=1.5, style='->', alpha=0.8):
    """Draw an arrow between two points."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, alpha=alpha),
                zorder=1)


# ================================================================
# FIG 1: VDR-9 IDENTITY CARD
# Type: Type 8 (Identity Card)
# Shows: System overview at VDR-9 — primitives, modes, loop,
#        notebook schema — as a visual anchor for the paper.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# ── title ──
ax.text(50, 96, 'VDR-9: Orchestrated Inference', ha='center', va='top',
        fontsize=20, fontweight='bold', color=GOLD)
ax.text(50, 92, 'Structured Reasoning Through Tool Composition',
        ha='center', va='top', fontsize=12, color=SILVER)

# ── left panel: system counts ──
panel_l = FancyBboxPatch((3, 38), 28, 50, boxstyle="round,pad=0.6",
                          facecolor=PAN, edgecolor=DIM, linewidth=1.2, alpha=0.9)
ax.add_patch(panel_l)
ax.text(17, 85, 'System Totals', ha='center', va='center',
        fontsize=13, fontweight='bold', color=GOLD)

stats = [
    ('Pure Primitives', '289', CYAN),
    ('Operational Primitives', '44', ORANGE),
    ('Total Primitives', '333', GOLD),
    ('', '', BG),
    ('Inference Modes', '4', GREEN),
    ('KB Struct Fields', '24', BLUE),
    ('Modules', '37', PURPLE),
    ('Existing Tests', '705', MAG),
]
for i, (label, val, col) in enumerate(stats):
    yy = 79 - i * 5.2
    if label == '':
        continue
    ax.text(7, yy, label, ha='left', va='center', fontsize=10, color=SILVER)
    ax.text(29, yy, val, ha='right', va='center', fontsize=11,
            fontweight='bold', color=col)

# ── center panel: the loop (small schematic) ──
panel_c = FancyBboxPatch((34, 38), 32, 50, boxstyle="round,pad=0.6",
                          facecolor=PAN, edgecolor=DIM, linewidth=1.2, alpha=0.9)
ax.add_patch(panel_c)
ax.text(50, 85, 'The Inference Loop', ha='center', va='center',
        fontsize=13, fontweight='bold', color=GOLD)

# Draw a small pentagon-ish loop
loop_labels = ['Assess', 'Formalize', 'Execute', 'Store', 'Assess']
loop_colors = [CYAN, BLUE, GREEN, ORANGE, CYAN]
# Positions in a rough circle inside the center panel
cx, cy = 50, 60
r = 10
angles = [90, 162, 234, 306, 378]  # degrees, starting from top
loop_pts = []
for ang in angles:
    rad = np.radians(ang)
    lx = cx + r * np.cos(rad)
    ly = cy + r * np.sin(rad) * 0.85  # slightly compressed vertically
    loop_pts.append((lx, ly))

for i in range(4):
    make_box(ax, loop_pts[i][0], loop_pts[i][1], 9, 3.5,
             loop_labels[i], loop_colors[i], fontsize=8.5)

# Arrows between loop nodes
for i in range(3):
    x1, y1 = loop_pts[i]
    x2, y2 = loop_pts[i+1]
    # offset arrow start/end slightly
    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx*dx + dy*dy)
    ox = dx / dist * 2.5
    oy = dy / dist * 2.0
    draw_arrow(ax, x1 + ox, y1 + oy, x2 - ox, y2 - oy, color=SILVER, lw=1.8)

# Arrow from Store back to Assess (closing the loop)
x1, y1 = loop_pts[3]
x2, y2 = loop_pts[0]
dx = x2 - x1
dy = y2 - y1
dist = np.sqrt(dx*dx + dy*dy)
ox = dx / dist * 2.5
oy = dy / dist * 2.0
draw_arrow(ax, x1 + ox, y1 + oy, x2 - ox, y2 - oy, color=GOLD, lw=2.0)

# Exit paths
ax.text(50, 44.5, 'Conclude', ha='center', va='center', fontsize=8,
        color=GREEN, fontstyle='italic')
ax.text(42, 44.5, 'Backtrack', ha='center', va='center', fontsize=8,
        color=RED, fontstyle='italic')
ax.text(58, 44.5, 'Branch', ha='center', va='center', fontsize=8,
        color=PURPLE, fontstyle='italic')
ax.text(50, 41, 'exit paths from Assess phase', ha='center', va='center',
        fontsize=7, color=DIM)

# ── right panel: four modes ──
panel_r = FancyBboxPatch((69, 38), 28, 50, boxstyle="round,pad=0.6",
                          facecolor=PAN, edgecolor=DIM, linewidth=1.2, alpha=0.9)
ax.add_patch(panel_r)
ax.text(83, 85, 'Inference Modes', ha='center', va='center',
        fontsize=13, fontweight='bold', color=GOLD)

modes = [
    ('Deductive', 'premises + rules \u2192 necessary conclusion', CYAN),
    ('Inductive', 'observations \u2192 ranked hypotheses', GREEN),
    ('Abductive', 'symptoms \u2192 best explanation', MAG),
    ('Analogical', 'known domain \u2192 transferred conclusion', PURPLE),
]
for i, (name, desc, col) in enumerate(modes):
    yy = 77 - i * 10
    ax.plot([73, 73], [yy + 2.5, yy - 2.5], color=col, linewidth=3,
            solid_capstyle='round')
    ax.text(75.5, yy + 1.2, name, ha='left', va='center', fontsize=10.5,
            fontweight='bold', color=col)
    ax.text(75.5, yy - 1.8, desc, ha='left', va='center', fontsize=7.5,
            color=SILVER)

# ── bottom banner ──
panel_b = FancyBboxPatch((3, 3), 94, 30, boxstyle="round,pad=0.6",
                          facecolor=PAN, edgecolor=DIM, linewidth=1.2, alpha=0.9)
ax.add_patch(panel_b)
ax.text(50, 30, 'Key Principle', ha='center', va='center',
        fontsize=13, fontweight='bold', color=GOLD)

principle_lines = [
    'The LLM does not reason. It orchestrates tools that compute and deduce.',
    'Prolog handles deduction. Python handles computation. Primitives handle data.',
    'The KB records everything. Provenance traces every conclusion to its evidence.',
    'Confidence is an exact VDR fraction, not a vague label.',
    'Notebooks house investigations. Sessions manage lifecycle. Everything is queryable.',
]
for i, line in enumerate(principle_lines):
    ax.text(50, 25 - i * 4.2, line, ha='center', va='center',
            fontsize=9, color=WHITE if i == 0 else SILVER)

save(fig, 'vdr9_01_identity_card.png')


# ================================================================
# FIG 2: ORCHESTRATED INFERENCE LOOP — STATE MACHINE
# Type: Type 7 (Progression/Sequence)
# Shows: The 5-phase cycle with branch, backtrack, conclude, and
#        halt transitions. The non-trivial topology is spatial.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 97, 'The Orchestrated Inference Loop', ha='center', va='top',
        fontsize=17, fontweight='bold', color=GOLD)
ax.text(50, 93, 'Five phases cycling until termination', ha='center', va='top',
        fontsize=11, color=SILVER)

# Main loop nodes — arranged in a circle
nodes = [
    ('Assess',    CYAN,   50, 78),
    ('Formalize', BLUE,   78, 62),
    ('Execute',   GREEN,  72, 38),
    ('Store',     ORANGE, 28, 38),
]
bw, bh = 13, 5.5  # box width, height

for label, col, x, y in nodes:
    make_box(ax, x, y, bw, bh, label, col, fontsize=12)

# Sub-labels under each box
sub_labels = [
    (50, 73.5, 'pattern matching\nover structured state', CYAN),
    (78, 57.5, 'write Prolog rules,\nPython scripts, primitives', BLUE),
    (72, 33.5, 'tools compute\ndeterministically', GREEN),
    (28, 33.5, 'KB facts, LRU,\ncounters, ring buffers', ORANGE),
]
for x, y, text, col in sub_labels:
    ax.text(x, y, text, ha='center', va='top', fontsize=7.5,
            color=col, alpha=0.7, linespacing=1.4)

# Main loop arrows (assess→formalize→execute→store→assess)
arrow_pairs = [
    (50, 78, 78, 62),    # assess → formalize
    (78, 62, 72, 38),    # formalize → execute
    (72, 38, 28, 38),    # execute → store
    (28, 38, 50, 78),    # store → assess (closing loop)
]
for x1, y1, x2, y2 in arrow_pairs:
    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx*dx + dy*dy)
    ox = dx / dist * 4.5
    oy = dy / dist * 3.5
    is_return = (x1 == 28 and y1 == 38)
    draw_arrow(ax, x1 + ox, y1 + oy, x2 - ox, y2 - oy,
               color=GOLD if is_return else SILVER, lw=2.2 if is_return else 1.8)

# ── exit paths from Assess ──
# Conclude (down-right)
make_box(ax, 83, 83, 11, 4.5, 'Conclude', GREEN, fontsize=10)
draw_arrow(ax, 56, 80, 77, 83, color=GREEN, lw=1.8)
ax.text(67, 83, 'goal\nsatisfied', ha='center', va='center',
        fontsize=7, color=GREEN, alpha=0.7)

# Halt (up-right)
make_box(ax, 83, 92, 11, 4.5, 'Halt', RED, fontsize=10)
draw_arrow(ax, 56, 80.5, 77, 92, color=RED, lw=1.8)
ax.text(64.5, 88.5, 'budget\nexhausted', ha='center', va='center',
        fontsize=7, color=RED, alpha=0.7)

# Branch (left from assess)
make_box(ax, 17, 78, 11, 4.5, 'Branch', PURPLE, fontsize=10)
draw_arrow(ax, 44, 78, 23, 78, color=PURPLE, lw=1.8)
ax.text(33.5, 80.5, 'sub-problem\nidentified', ha='center', va='center',
        fontsize=7, color=PURPLE, alpha=0.7)

# Child loop from Branch
ax.text(17, 72.5, 'child\nnotebook', ha='center', va='center',
        fontsize=7.5, color=PURPLE, alpha=0.7)
draw_arrow(ax, 17, 75.5, 17, 72, color=PURPLE, lw=1.2, style='->')
draw_arrow(ax, 20, 72, 44, 76, color=PURPLE, lw=1.2, style='->')
ax.text(30, 72.5, 'result\nreturns', ha='center', va='center',
        fontsize=6.5, color=PURPLE, alpha=0.6)

# Backtrack (from execute or formalize back to assess)
make_box(ax, 17, 55, 13, 4.5, 'Backtrack', RED, fontsize=10)
# Arrow from execute area to backtrack
draw_arrow(ax, 65, 38, 24, 52.5, color=RED, lw=1.5, style='->')
ax.text(48, 43.5, 'execution\nfails', ha='center', va='center',
        fontsize=7, color=RED, alpha=0.7)
# Arrow from backtrack back to assess
draw_arrow(ax, 17, 57.5, 44, 76, color=RED, lw=1.5, style='->')
ax.text(25, 67, 'pop stack,\ntry alternative', ha='center', va='center',
        fontsize=7, color=RED, alpha=0.7)

# ── budget box ──
bpanel = FancyBboxPatch((3, 5), 94, 18, boxstyle="round,pad=0.5",
                          facecolor=PAN, edgecolor=DIM, linewidth=1, alpha=0.8)
ax.add_patch(bpanel)
ax.text(50, 20.5, 'Loop Invariants (checked every Assess)', ha='center', va='center',
        fontsize=10, fontweight='bold', color=GOLD)
invariants = [
    'steps_executed < max_steps',
    'queries_issued < max_queries',
    'steps_since_evidence < stall_threshold',
    'investigation_path.depth < max_depth',
    'lru_contains(attempted_steps, current) = false',
]
for i, inv in enumerate(invariants):
    col = [CYAN, ORANGE, MAG, PURPLE, BLUE][i]
    xx = 10 + (i % 3) * 32
    yy = 15 if i < 3 else 9
    ax.text(xx, yy, inv, ha='left', va='center', fontsize=8, color=col,
            family='monospace')

save(fig, 'vdr9_02_inference_loop.png')


# ================================================================
# FIG 3: CONFIDENCE PROPAGATION THROUGH MULTI-MODE CHAIN
# Type: Type 7 (Progression/Sequence)
# Shows: Confidence values degrading through a realistic chain
#        of inference steps with exact VDR fractions at each stage.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.set_facecolor(BG)
ax.set_facecolor(PAN)

ax.text(0.5, 1.06, 'Confidence Propagation Through a Multi-Mode Inference Chain',
        ha='center', va='center', transform=ax.transAxes,
        fontsize=15, fontweight='bold', color=GOLD)

# Chain stages with confidence values
stages = [
    ('Prometheus\nfetch', 'acquire', 95, ORANGE),
    ('parse_json\nextract', 'parse', 95, BLUE),
    ('to_fraction\nconvert', 'convert', 95, CYAN),
    ('Python\ncorrelation', 'script', 90, GREEN),
    ('KB_ASSERT\nevidence', 'store', 90, ORANGE),
    ('Prolog\ndeduction', 'deduce', 90, CYAN),
    ('LLM\nassessment', 'assess', 30, MAG),
    ('Prolog\nre-query', 'verify', 30, CYAN),
    ('Conclude', 'conclude', 30, GOLD),
]

n = len(stages)
x_positions = np.linspace(0.5, n - 0.5, n)
confidences = [s[2] for s in stages]

# Plot confidence as a step/bar chart
bar_colors = [s[3] for s in stages]
bars = ax.bar(x_positions, confidences, width=0.7, color=bar_colors,
              edgecolor=[c for c in bar_colors], linewidth=1.5, alpha=0.75, zorder=3)

# Confidence values on top of bars
for i, (x, conf) in enumerate(zip(x_positions, confidences)):
    ax.text(x, conf + 2.5, '%d/100' % conf, ha='center', va='bottom',
            fontsize=10, fontweight='bold', color=WHITE, zorder=4)

# Stage labels below
for i, (label, _, _, col) in enumerate(stages):
    ax.text(x_positions[i], -8, label, ha='center', va='top',
            fontsize=8.5, color=col, linespacing=1.3)

# Connecting arrows showing flow
for i in range(n - 1):
    ax.annotate('', xy=(x_positions[i+1] - 0.35, confidences[i+1] / 2),
                xytext=(x_positions[i] + 0.35, confidences[i] / 2),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1.2, alpha=0.5))

# Highlight the LLM assessment drop
ax.annotate('LLM assessment\ndegrades confidence\nto 30/100',
            xy=(x_positions[6], 30), xytext=(x_positions[6] + 0.8, 62),
            fontsize=8.5, color=MAG, ha='center',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

# Propagation rule annotations
ax.text(x_positions[2], 85, 'weakest link rule:\nmin(95, 95, 95) = 95/100',
        ha='center', va='center', fontsize=7.5, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

ax.text(x_positions[3] + 0.5, 80, 'script penalty:\n95 \u00d7 95/100 = 90/100',
        ha='center', va='center', fontsize=7.5, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

ax.text(x_positions[6] - 0.7, 50, 'LLM floor:\nfixed at 30/100',
        ha='center', va='center', fontsize=7.5, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM, alpha=0.8))

# Threshold bands
ax.axhspan(80, 100, color=GREEN, alpha=0.06, zorder=0)
ax.axhspan(60, 80, color=CYAN, alpha=0.04, zorder=0)
ax.axhspan(40, 60, color=ORANGE, alpha=0.04, zorder=0)
ax.axhspan(0, 40, color=RED, alpha=0.04, zorder=0)

ax.text(n + 0.1, 90, 'High', fontsize=8, color=GREEN, va='center')
ax.text(n + 0.1, 70, 'Moderate', fontsize=8, color=CYAN, va='center')
ax.text(n + 0.1, 50, 'Low', fontsize=8, color=ORANGE, va='center')
ax.text(n + 0.1, 20, 'Unreliable', fontsize=8, color=RED, va='center')

ax.set_xlim(-0.3, n + 1.5)
ax.set_ylim(-15, 108)
ax.set_ylabel('Confidence (exact VDR fraction)', fontsize=11, color=SILVER)
ax.set_xticks([])
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, 'vdr9_03_confidence_propagation.png')


# ================================================================
# FIG 4: SRE INVESTIGATION CONVERGENCE
# Type: Type 1 (Running/Convergence Chart)
# Shows: Evidence count rising, hypothesis count falling,
#        confidence rising over 7 iterations. Three curves
#        converging to resolution. Shape IS the finding.
# ================================================================

fig, ax1 = plt.subplots(figsize=(16, 10))
fig.set_facecolor(BG)
ax1.set_facecolor(PAN)

ax1.text(0.5, 1.06, 'SRE Incident Investigation — Convergence to Root Cause',
         ha='center', va='center', transform=ax1.transAxes,
         fontsize=15, fontweight='bold', color=GOLD)

iterations = np.arange(0, 8)

# Data from the worked example
evidence_count = [0, 1, 4, 5, 6, 7, 8, 8]
hypothesis_count = [0, 0, 0, 2, 2, 3, 3, 1]
confidence = [0, 0, 0, 0, 40, 55, 72, 89.3]

# Evidence count (left axis)
line1 = ax1.plot(iterations, evidence_count, 'o-', color=CYAN, linewidth=2.5,
                 markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
                 label='Evidence count', zorder=4)
ax1.fill_between(iterations, 0, evidence_count, color=CYAN, alpha=0.08)

# Hypothesis count (left axis)
line2 = ax1.plot(iterations, hypothesis_count, 's-', color=MAG, linewidth=2.5,
                 markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
                 label='Active hypotheses', zorder=4)

ax1.set_xlabel('Loop Iteration', fontsize=12, color=SILVER)
ax1.set_ylabel('Count', fontsize=12, color=SILVER)
ax1.set_xlim(-0.5, 8)
ax1.set_ylim(-0.8, 12)
ax1.tick_params(colors=DIM, labelsize=9)
for spine in ax1.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

# Confidence (right axis)
ax2 = ax1.twinx()
line3 = ax2.plot(iterations, confidence, 'D-', color=GOLD, linewidth=2.5,
                 markersize=10, markeredgecolor=WHITE, markeredgewidth=1.5,
                 label='Confidence (/100)', zorder=4)
ax2.fill_between(iterations, 0, confidence, color=GOLD, alpha=0.06)
ax2.set_ylabel('Confidence (exact fraction /100)', fontsize=12, color=GOLD)
ax2.set_ylim(-5, 120)
ax2.tick_params(colors=GOLD, labelsize=9)
ax2.spines['right'].set_color(GOLD)
ax2.spines['right'].set_linewidth(0.8)
for sp in ['top', 'left', 'bottom']:
    ax2.spines[sp].set_color(DIM)
    ax2.spines[sp].set_linewidth(0.5)

# Goal threshold
ax2.axhline(y=80, color=GREEN, linestyle='--', linewidth=1.5, alpha=0.6)
ax2.text(7.8, 82, 'Goal: 80/100', fontsize=9, color=GREEN, ha='right', va='bottom')

# Iteration labels
iter_labels = [
    'Start',
    'Pull\nlatency',
    'Pull CPU,\nDB, RPS',
    'Check\ndeploys',
    'Formalize\nhypotheses',
    'Cross-\ncorrelation',
    'Targeted\nDB probe',
    'Confirm\nroot cause',
]
for i, label in enumerate(iter_labels):
    ax1.text(i, -1.8, label, ha='center', va='top', fontsize=7,
             color=SILVER, linespacing=1.3)

# Annotations
ax1.annotate('3 Prometheus queries\nadd 4 evidence facts',
             xy=(2, 4), xytext=(3.5, 9.5),
             fontsize=8, color=CYAN, ha='center',
             arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2))

ax2.annotate('correlation narrows\nto DB connections',
             xy=(5, 55), xytext=(3.5, 75),
             fontsize=8, color=GOLD, ha='center',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))

ax2.annotate('root cause confirmed\n89.3/100 > goal 80/100',
             xy=(7, 89.3), xytext=(5.5, 105),
             fontsize=8.5, color=GOLD, ha='center', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Combined legend
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=9,
           facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

save(fig, 'vdr9_04_sre_convergence.png')


# ================================================================
# FIG 5: EVIDENCE SOURCE CONFIDENCE SPECTRUM
# Type: Type 2 (Scale/Landscape)
# Shows: All source types on a 0–1 confidence axis. The spacing
#        reveals clustering: exact tools at 1.0, monitoring at
#        0.90–0.98, web/LLM at 0.30–0.50. Scale IS the finding.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.set_facecolor(BG)
ax.set_facecolor(PAN)

ax.text(0.5, 1.06, 'Evidence Source Confidence Spectrum',
        ha='center', va='center', transform=ax.transAxes,
        fontsize=15, fontweight='bold', color=GOLD)
ax.text(0.5, 1.02, 'Default provenance weights by source type (exact VDR fractions)',
        ha='center', va='center', transform=ax.transAxes,
        fontsize=10, color=SILVER)

# Sources ordered by confidence
sources = [
    ('Exact VDR\ncomputation',    100, GOLD,   'fraction(1, 1)'),
    ('Prolog\nderivation',        100, CYAN,   'fraction(1, 1)'),
    ('Database\nquery',            98, BLUE,   'fraction(98, 100)'),
    ('Prometheus\n(live)',         95, GREEN,  'fraction(95, 100)'),
    ('Python\nscript',             95, GREEN,  'fraction(95, 100)'),
    ('Prometheus\n(historical)',   90, CYAN,   'fraction(90, 100)'),
    ('REST API\nresponse',         85, BLUE,   'fraction(85, 100)'),
    ('Peer-reviewed\npaper',       80, PURPLE, 'fraction(80, 100)'),
    ('User-stated\nfact',          70, ORANGE, 'fraction(70, 100)'),
    ('Web search\nresult',         50, MAG,    'fraction(50, 100)'),
    ('LLM-generated\ncontent',     30, RED,    'fraction(30, 100)'),
]

n = len(sources)
y_positions = np.arange(n, 0, -1)

for i, (label, conf, col, frac) in enumerate(sources):
    y = y_positions[i]
    # Bar
    ax.barh(y, conf, height=0.6, color=col, alpha=0.65,
            edgecolor=col, linewidth=1.5, zorder=3)
    # Dot at end
    ax.scatter(conf, y, s=180, color=col, edgecolors=WHITE,
               linewidth=1.5, zorder=4)
    # Label left
    ax.text(-2, y, label, ha='right', va='center', fontsize=9,
            color=col, linespacing=1.3)
    # Fraction right
    ax.text(conf + 2, y, frac, ha='left', va='center', fontsize=8.5,
            color=SILVER, family='monospace')

# Confidence bands as background
ax.axvspan(80, 105, color=GREEN, alpha=0.04, zorder=0)
ax.axvspan(60, 80, color=CYAN, alpha=0.03, zorder=0)
ax.axvspan(40, 60, color=ORANGE, alpha=0.03, zorder=0)
ax.axvspan(0, 40, color=RED, alpha=0.03, zorder=0)

# Band labels at top
ax.text(90, n + 0.9, 'HIGH', fontsize=9, fontweight='bold', color=GREEN, ha='center')
ax.text(70, n + 0.9, 'MODERATE', fontsize=9, fontweight='bold', color=CYAN, ha='center')
ax.text(50, n + 0.9, 'LOW', fontsize=9, fontweight='bold', color=ORANGE, ha='center')
ax.text(20, n + 0.9, 'UNRELIABLE', fontsize=9, fontweight='bold', color=RED, ha='center')

# Key insight annotation
ax.text(50, 0.3, 'Exact tools cluster at 95\u2013100%.   LLM assessment is the weakest link at 30%.',
        ha='center', va='center', fontsize=10, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xlim(-25, 115)
ax.set_ylim(-0.3, n + 1.5)
ax.set_xlabel('Confidence (fraction /100)', fontsize=11, color=SILVER)
ax.set_yticks([])
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, 'vdr9_05_source_confidence_spectrum.png')


# ================================================================
# FIG 6: BUDGET CONSUMPTION WITH THRESHOLDS
# Type: Type 1 + Type 3 (Running Chart with Threshold Regions)
# Shows: Three budget counters consumed over iterations with
#        constraint trigger zones. Shape shows resource strategy.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.set_facecolor(BG)
ax.set_facecolor(PAN)

ax.text(0.5, 1.06, 'Inference Budget Consumption Over Loop Iterations',
        ha='center', va='center', transform=ax.transAxes,
        fontsize=15, fontweight='bold', color=GOLD)

iterations = np.arange(0, 26)

# Simulated budget consumption for a typical investigation
steps = np.minimum(iterations, 23)
queries = np.array([0,0,1,1,4,4,4,5,5,6,6,6,7,7,8,8,9,10,10,11,12,12,13,13,14,14])
scripts = np.array([0,0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6])

# Budget limits
max_steps = 50
max_queries = 20
max_scripts = 10

# Plot consumption lines
ax.plot(iterations, steps, 'o-', color=CYAN, linewidth=2.5, markersize=6,
        markeredgecolor=WHITE, markeredgewidth=1, label='Steps executed', zorder=4)
ax.plot(iterations, queries, 's-', color=ORANGE, linewidth=2.5, markersize=6,
        markeredgecolor=WHITE, markeredgewidth=1, label='Queries issued', zorder=4)
ax.plot(iterations, scripts, 'D-', color=MAG, linewidth=2.5, markersize=6,
        markeredgecolor=WHITE, markeredgewidth=1, label='Scripts executed', zorder=4)

# Budget limits as threshold lines
ax.axhline(y=max_steps, color=CYAN, linestyle='--', linewidth=1.5, alpha=0.4)
ax.axhline(y=max_queries, color=ORANGE, linestyle='--', linewidth=1.5, alpha=0.4)
ax.axhline(y=max_scripts, color=MAG, linestyle='--', linewidth=1.5, alpha=0.4)

# Threshold labels
ax.text(25.5, max_steps + 1, 'step limit: 50', fontsize=9, color=CYAN, va='bottom')
ax.text(25.5, max_queries + 1, 'query limit: 20', fontsize=9, color=ORANGE, va='bottom')
ax.text(25.5, max_scripts + 1, 'script limit: 10', fontsize=9, color=MAG, va='bottom')

# Warning zones (80% of budget)
ax.axhspan(max_steps * 0.8, max_steps, color=CYAN, alpha=0.04, zorder=0)
ax.axhspan(max_queries * 0.8, max_queries, color=ORANGE, alpha=0.04, zorder=0)
ax.axhspan(max_scripts * 0.8, max_scripts, color=MAG, alpha=0.04, zorder=0)

# 80% warning labels
ax.text(0.5, max_steps * 0.8, '80%', fontsize=7, color=CYAN, alpha=0.5, va='bottom')
ax.text(0.5, max_queries * 0.8, '80%', fontsize=7, color=ORANGE, alpha=0.5, va='bottom')
ax.text(0.5, max_scripts * 0.8, '80%', fontsize=7, color=MAG, alpha=0.5, va='bottom')

# Annotations for strategy
ax.annotate('burst: 3 Prometheus\nqueries in one step',
            xy=(4, 4), xytext=(7, 12),
            fontsize=8, color=ORANGE, ha='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.2))

ax.annotate('scripts used sparingly\n\u2014 pure primitives preferred',
            xy=(14, 3), xytext=(17, 8),
            fontsize=8, color=MAG, ha='center',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.2))

ax.annotate('step budget is generous\n\u2014 investigation concludes\nwell before limit',
            xy=(23, 23), xytext=(20, 38),
            fontsize=8, color=CYAN, ha='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2))

# Key insight
ax.text(13, 46, 'Budget strategy: steps are cheap, queries are moderate, scripts are expensive.',
        ha='center', va='center', fontsize=9.5, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xlim(-1, 27)
ax.set_ylim(-2, 55)
ax.set_xlabel('Loop Iteration', fontsize=11, color=SILVER)
ax.set_ylabel('Cumulative Count', fontsize=11, color=SILVER)
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

ax.legend(loc='upper left', fontsize=9, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

save(fig, 'vdr9_06_budget_consumption.png')


# ================================================================
# FIG 7: CONFIDENCE THRESHOLD REGIONS
# Type: Type 3 (Threshold/Region Chart)
# Shows: The 0–1 confidence axis with shaded bands and example
#        conclusions placed at their computed confidence values.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.set_facecolor(BG)
ax.set_facecolor(PAN)

ax.text(0.5, 1.06, 'Confidence Regions and Example Conclusions',
        ha='center', va='center', transform=ax.transAxes,
        fontsize=15, fontweight='bold', color=GOLD)

# Regions
regions = [
    (95, 100, 'HIGH\nAct directly', GREEN, 0.12),
    (80, 95, 'MODERATE\nAct with monitoring', CYAN, 0.10),
    (60, 80, 'LOW\nGather more evidence', ORANGE, 0.08),
    (40, 60, 'SPECULATIVE\nPresent as hypothesis', MAG, 0.08),
    (0, 40, 'UNRELIABLE\nDo not present\nas conclusion', RED, 0.08),
]

for lo, hi, label, col, alpha in regions:
    ax.axhspan(lo, hi, color=col, alpha=alpha, zorder=0)
    ax.text(1.5, (lo + hi) / 2, label, ha='left', va='center',
            fontsize=10, color=col, fontweight='bold', linespacing=1.4)

# Region boundary lines
for boundary in [40, 60, 80, 95]:
    ax.axhline(y=boundary, color=DIM, linestyle='-', linewidth=0.8, alpha=0.5)

# Example conclusions scattered across the confidence axis
examples = [
    ('Deductive: DB connection\nexhaustion from deployment', 89.3, GOLD, 14),
    ('Inductive: quantization\nranked #1 by evidence', 72, CYAN, 7.5),
    ('Abductive: cache layer\ncaused latency spike', 92, GREEN, 9),
    ('Analogical: circuit breaker\npattern applies', 76, PURPLE, 14),
    ('Inductive: 7/10 dimensions\nchecked, partial survey', 63, ORANGE, 9),
    ('LLM assessment step\n(fixed floor)', 30, RED, 7),
    ('Two Prometheus sources\nagree independently', 99.75, GOLD, 14),
    ('Single web search\nresult, unverified', 50, MAG, 8),
]

for label, conf, col, xpos in examples:
    # Scatter point
    ax.scatter(xpos, conf, s=200, color=col, edgecolors=WHITE,
               linewidth=1.5, zorder=5)
    # Label with leader line
    ax.annotate(label, xy=(xpos, conf),
                xytext=(xpos + 2.5, conf),
                fontsize=8, color=col, va='center', ha='left',
                arrowprops=dict(arrowstyle='->', color=col, lw=1, alpha=0.6),
                linespacing=1.3)

# Confidence value labels on right
for label, conf, col, xpos in examples:
    frac_text = '%.1f/100' % conf if conf != 99.75 else '399/400'
    ax.text(23, conf, frac_text, ha='left', va='center', fontsize=8,
            color=SILVER, family='monospace')

ax.set_xlim(0, 26)
ax.set_ylim(-3, 105)
ax.set_ylabel('Confidence (exact VDR fraction)', fontsize=11, color=SILVER)
ax.set_xticks([])
ax.tick_params(colors=DIM, labelsize=9)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

# Key insight at bottom
ax.text(13, -1, 'Every confidence score is an exact fraction computed from declared propagation rules \u2014 not a vague label.',
        ha='center', va='top', fontsize=9, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

save(fig, 'vdr9_07_confidence_regions.png')


# ================================================================
# FIG 8: NOTEBOOK KB NESTING
# Type: Type 4 (Geometric Cross-Section / Nesting)
# Shows: The inference notebook as a nested structure within the
#        KB tree, with data primitives, evidence, reasoning, and
#        conclusions visible at their scoping levels.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 97, 'Inference Notebook — KB Nesting Structure', ha='center', va='top',
        fontsize=17, fontweight='bold', color=GOLD)
ax.text(50, 93, 'A notebook is a KB subtree with standard schema and data primitives',
        ha='center', va='top', fontsize=10, color=SILVER)

# ── outermost: root KB tree context ──
outer = FancyBboxPatch((3, 3), 94, 86, boxstyle="round,pad=0.8",
                        facecolor=BG, edgecolor=DIM, linewidth=1.5, alpha=0.4)
ax.add_patch(outer)
ax.text(50, 87, 'root.inference.incident_002', ha='center', va='center',
        fontsize=13, fontweight='bold', color=GOLD)

# ── left column: persistent state ──
persist_box = FancyBboxPatch((5, 32), 28, 52, boxstyle="round,pad=0.5",
                              facecolor=PAN, edgecolor=CYAN, linewidth=1.5, alpha=0.85)
ax.add_patch(persist_box)
ax.text(19, 82, 'PERSISTENT', ha='center', va='center',
        fontsize=11, fontweight='bold', color=CYAN)
ax.text(19, 79, '(survives reset & clone kill)', ha='center', va='center',
        fontsize=7, color=CYAN, alpha=0.7)

# Persistent sub-sections
persist_sections = [
    ('Problem', 'problem_statement(...)\ninference_type(abductive)\ngoal(root_cause(_, C), C > 80/100)', 74, CYAN),
    ('Evidence Facts', 'symptom(latency_p99_elevated)\nrecent_deployment(v2.3.1, 14:15)\ncorrelation(db, latency, 94/100)', 64, GREEN),
    ('Prolog Rules', 'possible_cause(X) :- ...\nleading_indicator(X) :- ...\nroot_cause(X, C) :- ...', 54, BLUE),
    ('Conclusions', 'root_cause(db_exhaustion,\n  confidence(893/1000))\nalternatives([...]) ', 43, GOLD),
    ('Connections', 'evidence_source \u2190 monitoring\ndomain_knowledge \u2190 sre_rules', 35, PURPLE),
]

for name, content, y_top, col in persist_sections:
    inner = FancyBboxPatch((7, y_top - 7.5), 24, 8.5,
                            boxstyle="round,pad=0.3",
                            facecolor=BG, edgecolor=col, linewidth=1, alpha=0.7)
    ax.add_patch(inner)
    ax.text(8.5, y_top - 0.5, name, ha='left', va='top', fontsize=8.5,
            fontweight='bold', color=col)
    ax.text(8.5, y_top - 2.8, content, ha='left', va='top', fontsize=6.5,
            color=SILVER, family='monospace', linespacing=1.3)

# ── center column: live state (data primitives) ──
live_box = FancyBboxPatch((36, 32), 28, 52, boxstyle="round,pad=0.5",
                           facecolor=PAN, edgecolor=ORANGE, linewidth=1.5, alpha=0.85)
ax.add_patch(live_box)
ax.text(50, 82, 'LIVE STATE', ha='center', va='center',
        fontsize=11, fontweight='bold', color=ORANGE)
ax.text(50, 79, '(captured by snapshot, cleared on reset)', ha='center', va='center',
        fontsize=7, color=ORANGE, alpha=0.7)

live_sections = [
    ('Counters', 'steps_executed: 7\nqueries_issued: 6\nhypotheses_tested: 3\nevidence_count: 8', 74, ORANGE),
    ('Queue', 'step_queue: [\n  (empty \u2014 all steps\n   completed)\n]', 62, GREEN),
    ('Stack', 'investigation_path: [\n  "DB connection\n   exhaustion"\n]', 51, BLUE),
    ('LRU Caches', 'findings: [{latency_profile},\n  {correlation}, {db_state}]\nsources: [{prom \u00d76}, {deploy}]', 41, CYAN),
    ('Lock + Bitset', 'investigation_active: released\nevidence_dims: [0,1,2,3,4]\n  (5/8 checked)', 33, MAG),
]

for name, content, y_top, col in live_sections:
    inner = FancyBboxPatch((38, y_top - 8), 24, 9,
                            boxstyle="round,pad=0.3",
                            facecolor=BG, edgecolor=col, linewidth=1, alpha=0.7)
    ax.add_patch(inner)
    ax.text(39.5, y_top - 0.5, name, ha='left', va='top', fontsize=8.5,
            fontweight='bold', color=col)
    ax.text(39.5, y_top - 2.8, content, ha='left', va='top', fontsize=6.5,
            color=SILVER, family='monospace', linespacing=1.3)

# ── right column: children and metadata ──
meta_box = FancyBboxPatch((67, 32), 28, 52, boxstyle="round,pad=0.5",
                           facecolor=PAN, edgecolor=PURPLE, linewidth=1.5, alpha=0.85)
ax.add_patch(meta_box)
ax.text(81, 82, 'STRUCTURE', ha='center', va='center',
        fontsize=11, fontweight='bold', color=PURPLE)
ax.text(81, 79, '(tree position, children, constraints)', ha='center', va='center',
        fontsize=7, color=PURPLE, alpha=0.7)

struct_sections = [
    ('Path & ID', 'path: root.inference.incident_002\nid: 42\nparent_id: 6 (root.inference)', 74, PURPLE),
    ('Constraints', 'step_budget < 50\nquery_budget < 20\nstall_threshold < 5\nmin_evidence >= 3', 63, RED),
    ('Children', 'root.inference.incident_002\n  .correlation_analysis\n  .db_deep_dive', 53, GREEN),
    ('Provenance', 'created_at: turn 47\nconcluded_at: turn 54\nsteps_taken: 7\nbacktracks: 0', 43, GOLD),
    ('Status', 'status: concluded\nconfidence: 893/1000\nmode: abductive', 34, CYAN),
]

for name, content, y_top, col in struct_sections:
    inner = FancyBboxPatch((69, y_top - 7.5), 24, 8.5,
                            boxstyle="round,pad=0.3",
                            facecolor=BG, edgecolor=col, linewidth=1, alpha=0.7)
    ax.add_patch(inner)
    ax.text(70.5, y_top - 0.5, name, ha='left', va='top', fontsize=8.5,
            fontweight='bold', color=col)
    ax.text(70.5, y_top - 2.8, content, ha='left', va='top', fontsize=6.5,
            color=SILVER, family='monospace', linespacing=1.3)

# ── bottom banner: the key point ──
banner = FancyBboxPatch((5, 5), 90, 22, boxstyle="round,pad=0.5",
                          facecolor=PAN, edgecolor=DIM, linewidth=1, alpha=0.85)
ax.add_patch(banner)
ax.text(50, 24, 'Notebook = KB with Standard Schema', ha='center', va='center',
        fontsize=12, fontweight='bold', color=GOLD)

notes = [
    'No new data structures \u2014 uses existing KB struct from VDR-8',
    'Persistent state (facts, rules, constraints) survives session reset and clone kill',
    'Live state (counters, queues, stacks, LRUs, locks, bitsets) captured by session_snapshot',
    'The entire investigation is replayable by walking the notebook KB tree',
]
for i, note in enumerate(notes):
    ax.text(50, 20 - i * 3.8, note, ha='center', va='center',
            fontsize=8.5, color=WHITE if i == 0 else SILVER)

save(fig, 'vdr9_08_notebook_nesting.png')


# ── summary ───────────────────────────────────────────────────────
print("\n=== VDR-9 Diagrams Complete ===")
filenames = [
    'vdr9_01_identity_card.png',
    'vdr9_02_inference_loop.png',
    'vdr9_03_confidence_propagation.png',
    'vdr9_04_sre_convergence.png',
    'vdr9_05_source_confidence_spectrum.png',
    'vdr9_06_budget_consumption.png',
    'vdr9_07_confidence_regions.png',
    'vdr9_08_notebook_nesting.png',
]
for f in filenames:
    print("  %s" % f)
print("\n8 figures saved to %s" % outdir)
