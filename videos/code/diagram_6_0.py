#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 6, Slides 1-10
10 figures covering: test cycle, test suite vs peer review,
experiment JSON anatomy, five match modes, value pool scale,
value node anatomy, five experiments results, terminal output,
GPA fail anatomy, pass/fail ratio.
Output: PNG files to ./figures/

RULES:
- No edgecolor parameter on any element
- No edgecolors parameter on any element
- All text inside axis limits
- Vertical offset to prevent label overlap
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# -- Output directory --
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(outdir, exist_ok=True)

# -- Color palette --
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

def rounded_box(ax, x, y, w, h, text, color, fontsize=10, textcolor=WHITE, alpha=0.25):
    box = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15", facecolor=color, alpha=alpha,
        linewidth=1.5)
    ax.add_patch(box)
    if text:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=textcolor, fontweight='bold', zorder=10)


# ================================================================
# FIG 1: THE TEST CYCLE — WRITE, RUN, COMPARE
# Type: Progression/Sequence
# Shows: three distinct steps — expectation set before computation
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "How a Test Works: Three Steps",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Box 1: WRITE
rounded_box(ax, 3, 3.5, 4.0, 3.5, "", GOLD, alpha=0.15)
ax.text(3, 5.0, "1. WRITE", ha='center', va='center', fontsize=14,
        color=GOLD, fontweight='bold')
checklist = [
    r"Expected: $\alpha^{-1}$ = 137.036...",
    r"Expected: sin$^2\theta_W$ = 0.23122",
    r"Expected: D/H = 2.527 $\times$ 10$^{-5}$",
]
for i, item in enumerate(checklist):
    ax.text(3, 3.8 - i * 0.6, item, ha='center', va='center',
            fontsize=8, color=SILVER)
ax.text(3, 2.2, "Write expectations\nBEFORE computing", ha='center', va='center',
        fontsize=8, color=GOLD, fontstyle='italic')

# Arrow
ax.annotate("", xy=(6.0, 3.5), xytext=(5.2, 3.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))
ax.text(5.6, 4.2, "then", ha='center', va='center', fontsize=9, color=DIM)

# Box 2: RUN
rounded_box(ax, 8, 3.5, 3.0, 3.5, "", CYAN, alpha=0.15)
ax.text(8, 5.0, "2. RUN", ha='center', va='center', fontsize=14,
        color=CYAN, fontweight='bold')
ax.text(8, 3.8, "Execute the\ncomputation.", ha='center', va='center',
        fontsize=10, color=SILVER)
ax.text(8, 2.8, "The computer\ndoesn't know the\nexpected answer.", ha='center', va='center',
        fontsize=8, color=CYAN, fontstyle='italic')

# Arrow
ax.annotate("", xy=(10.8, 3.5), xytext=(9.7, 3.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))
ax.text(10.2, 4.2, "then", ha='center', va='center', fontsize=9, color=DIM)

# Box 3: COMPARE
rounded_box(ax, 13, 3.5, 4.0, 3.5, "", GREEN, alpha=0.15)
ax.text(13, 5.0, "3. COMPARE", ha='center', va='center', fontsize=14,
        color=GREEN, fontweight='bold')
compare_lines = [
    ("Got: 137.036...", "Exp: 137.036...", GREEN, "PASS"),
    ("Got: 0.23122...", "Exp: 0.23122...", GREEN, "PASS"),
    ("Got: 4.74" + r"$\times$" + "10" + r"$^{-10}$", "Exp: 1.60" + r"$\times$" + "10" + r"$^{-10}$", RED, "FAIL"),
]
for i, (got, exp, col, result) in enumerate(compare_lines):
    y = 3.9 - i * 0.7
    ax.text(12.0, y, got, ha='left', va='center', fontsize=7, color=SILVER)
    ax.text(14.3, y, result, ha='center', va='center', fontsize=8,
            color=col, fontweight='bold')

ax.text(13, 2.2, "Match = PASS\nNo match = FAIL\nComputer decides.", ha='center', va='center',
        fontsize=8, color=GREEN, fontstyle='italic')

ax.text(8, -0.5, "The test doesn't care who wrote the code or what department they're in.\n"
        "It cares about one thing: does the number match.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_01_test_cycle.png")


# ================================================================
# FIG 2: TEST SUITE VS PEER REVIEW
# Type: Comparison Bar (two panels)
# Shows: slow/subjective vs fast/objective
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Two Quality Control Systems",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Peer Review --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Peer Review", ha='center', va='center',
         fontsize=14, fontweight='bold', color=DIM)

pr_steps = [
    (5, 7.5, "Submit paper", "social process"),
    (5, 6.3, "Wait 3-6 months", "time cost"),
    (5, 5.1, "2-3 people read it", "limited coverage"),
    (5, 3.9, "Subjective opinion", "influenced by reputation"),
    (5, 2.7, "Accept / Reject", "binary, delayed"),
]
for sx, sy, stxt, snote in pr_steps:
    rounded_box(ax1, sx, sy, 4.5, 0.8, stxt, DIM, fontsize=10, alpha=0.12)
    ax1.text(sx + 2.5, sy, snote, ha='left', va='center', fontsize=7,
             color=DIM, fontstyle='italic')

ax1.text(5, 1.5, "Checks narrative.\nTakes months.\nDoesn't run the code.",
         ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

# -- Right: Test Suite --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Test Suite", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GREEN)

ts_steps = [
    (5, 7.5, "Write comparisons", "computational process"),
    (5, 6.3, "Run (2 seconds)", "instant"),
    (5, 5.1, "253 numbers checked", "exhaustive coverage"),
    (5, 3.9, "Binary PASS/FAIL", "objective, automatic"),
    (5, 2.7, "Output published", "immediate, reproducible"),
]
for sx, sy, stxt, snote in ts_steps:
    rounded_box(ax2, sx, sy, 4.5, 0.8, stxt, GREEN, fontsize=10, alpha=0.15)
    ax2.text(sx + 2.5, sy, snote, ha='left', va='center', fontsize=7,
             color=GREEN, fontstyle='italic')

ax2.text(5, 1.5, "Checks numbers.\nTakes seconds.\nAnyone can run it.",
         ha='center', va='center', fontsize=9, color=GREEN, fontstyle='italic')

fig.text(0.5, 0.04, "Peer review asks: does this seem right?\n"
         "The test suite asks: does this number match that number?",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk6_02_test_vs_peer_review.png")


# ================================================================
# FIG 3: EXPERIMENT JSON — ANATOMY
# Type: Connection/Integer Map
# Shows: six sections of an experiment file as a visual pipeline
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-1, 12)

ax.text(7, 11.3, "Inside an Experiment File",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

sections = [
    (2.5, 9.5, "HEADER", "key, description,\npurpose", SILVER,
     "What this experiment\nis and why"),
    (7.0, 9.5, "DEPENDENCIES", "list of pool keys\nneeded as input", CYAN,
     "What it reads\nfrom the pool"),
    (11.5, 9.5, "EXECUTION\nPLAN", "ordered list of\nderivation functions", GREEN,
     "What to compute\nand in what order"),
    (2.5, 5.5, "EXPECTED\nOUTPUTS", "list of result keys\nthat should appear", BLUE,
     "What the derivations\nshould produce"),
    (7.0, 5.5, "COMPARISONS", "{output, mode,\nexpected, reference}", GOLD,
     "The tests.\nEach one is binary."),
    (11.5, 5.5, "DIAGRAMS", "optional visualization\nspecs", PURPLE,
     "How to draw\nthe results"),
]

for sx, sy, stitle, sdesc, scol, snote in sections:
    rounded_box(ax, sx, sy, 3.5, 2.2, "", scol, alpha=0.15)
    ax.text(sx, sy + 0.6, stitle, ha='center', va='center', fontsize=11,
            color=scol, fontweight='bold')
    ax.text(sx, sy - 0.2, sdesc, ha='center', va='center', fontsize=8,
            color=SILVER)
    ax.text(sx, sy - 0.85, snote, ha='center', va='center', fontsize=7,
            color=scol, fontstyle='italic')

# Flow arrows: dependencies -> execution -> outputs -> comparisons
flow = [(7.0, 9.5, 11.5, 9.5), (11.5, 8.3, 2.5, 6.7),
        (2.5, 5.5, 7.0, 5.5), (7.0, 5.5, 11.5, 5.5)]
labels = ["read", "compute", "produce", "check"]

# Top row arrows
ax.annotate("", xy=(5.0, 9.5), xytext=(4.3, 9.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))
ax.annotate("", xy=(9.5, 9.5), xytext=(8.8, 9.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

# Down from execution to outputs
ax.annotate("", xy=(7, 6.8), xytext=(11.0, 8.3),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2,
                           connectionstyle='arc3,rad=0.3'))

# Bottom row arrows
ax.annotate("", xy=(5.0, 5.5), xytext=(4.3, 5.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))
ax.annotate("", xy=(9.5, 5.5), xytext=(8.8, 5.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

# Pipeline labels
ax.text(4.6, 10.0, "read", ha='center', va='center', fontsize=8, color=DIM)
ax.text(9.1, 10.0, "compute", ha='center', va='center', fontsize=8, color=DIM)
ax.text(4.6, 6.0, "produce", ha='center', va='center', fontsize=8, color=DIM)
ax.text(9.1, 6.0, "check", ha='center', va='center', fontsize=8, color=DIM)

ax.text(7, 2.5, "Everything declared before anything runs.\nThe experiment is a contract: these inputs,\n"
        "these computations, these outputs, these checks.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

ax.text(7, 0.8, "The runner is generic. It doesn't know physics.\n"
        "It knows: load, execute, merge, compare, report.",
        ha='center', va='center', fontsize=10, color=DIM)

save(fig, "talk6_03_experiment_json.png")


# ================================================================
# FIG 4: THE FIVE MATCH MODES
# Type: Comparison Bar
# Shows: five checking mechanisms with concrete examples
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-0.5, 10)

ax.text(7, 9.3, "Five Ways to Check a Number",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

modes = [
    ("exact", r"$-$23/3 == $-$23/3", "PASS", GREEN,
     "Fraction must match exactly.\nFor group theory outputs."),
    ("miss_pct", "42.9800 vs 42.9799\nmiss: 0.0002%", "INFO", SILVER,
     "Reports fractional difference.\nDoesn't gate on its own."),
    ("digits", "137.035999207 vs\n137.035999206\n11 of 12 match", "INFO", SILVER,
     "Counts matching significant\nfigures."),
    ("range", "0.212 in [0.18, 0.25]", "PASS", GREEN,
     "Value falls within bounds.\nFor sanity checks."),
    ("bool", "True == True", "PASS", GREEN,
     "Binary yes/no.\nFor structural checks."),
]

for i, (mode, example, result, rcol, desc) in enumerate(modes):
    y = 7.8 - i * 1.6

    # Mode name
    ax.text(0.5, y, mode, ha='left', va='center', fontsize=13,
            color=GOLD, fontweight='bold')

    # Example
    ax.text(3.5, y, example, ha='left', va='center', fontsize=9,
            color=WHITE,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

    # Result
    ax.text(8.5, y, "[%s]" % result, ha='center', va='center', fontsize=11,
            color=rcol, fontweight='bold')

    # Description
    ax.text(10.5, y, desc, ha='left', va='center', fontsize=8,
            color=SILVER)

ax.text(7, -0.0, "The match mode is chosen per comparison based on what the physics warrants.\n"
        "Exact for integers. Range for order-of-magnitude. Miss for precision.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_04_five_match_modes.png")


# ================================================================
# FIG 5: THE VALUE POOL — 2700+ NODES
# Type: Scale/Landscape (dot clusters)
# Shows: scale of the pool as clusters of colored dots
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1.5, 9)

ax.text(8, 8.3, "2700+ Values: Every Constant, Every Measurement, Every Result",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

clusters = [
    ("Couplings", 20, GOLD, 1.5, 6.0),
    ("Masses", 30, CYAN, 4.0, 6.0),
    ("Beta\ncoefficients", 40, GREEN, 6.5, 6.0),
    ("QED\ncoefficients", 30, BLUE, 9.0, 6.0),
    ("Cosmology", 30, PURPLE, 11.5, 6.0),
    ("Math\nconstants", 40, SILVER, 14.0, 6.0),
    ("GR values", 40, RED, 2.5, 2.5),
    ("Derivation\noutputs", 200, ORANGE, 7.0, 2.5),
    ("Other\n(eng, spec, obs)", 80, DIM, 12.0, 2.5),
]

np.random.seed(42)
for label, count, col, cx, cy in clusters:
    # Draw dots in a cluster
    display_count = min(count, 80)  # cap dots for readability
    for d in range(display_count):
        dx = cx + np.random.normal(0, 0.6)
        dy = cy + np.random.normal(0, 0.4)
        ax.plot(dx, dy, 'o', color=col, markersize=2.5, alpha=0.5)

    # Label below cluster
    ax.text(cx, cy - 1.2, "%s\n(%d)" % (label, count), ha='center', va='center',
            fontsize=7, color=col, fontweight='bold')

ax.text(8, -0.5, "Every dot is a typed, sourced, versioned value.\n"
        "Nothing anonymous. Nothing untyped. Nothing unsourced.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_05_value_pool.png")


# ================================================================
# FIG 6: ANATOMY OF A VALUE NODE
# Type: Identity Card
# Shows: all eight fields of one pool entry
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 12)

ax.text(5, 11.2, "Inside a Value Node: Every Field",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

card = mpatches.FancyBboxPatch((0.3, 0.5), 9.4, 9.5,
    boxstyle="round,pad=0.3", facecolor=PAN, alpha=0.4,
    linewidth=2)
ax.add_patch(card)

fields = [
    ("key:", "coupling_alpha_em_inverse_v0", SILVER, "Unique identifier. Versioned."),
    ("value:", "137035999177 / 1000000000", GOLD, "The number. As an exact Fraction."),
    ("value_type:", "exact_fraction", GREEN, "Is this exact or approximate?"),
    ("unit:", "dimensionless", CYAN, "Physical units."),
    ("source:", "CODATA 2018", SILVER, "Where this number came from."),
    ("digits:", "12", BLUE, "How many digits are meaningful."),
    ("tags:", "[alpha, em, measured]", DIM, "Searchable labels."),
    ("level:", "2 (measured)", PURPLE, "0=math, 1=group, 2=measured, 3=derived."),
]

for i, (label, val, col, desc) in enumerate(fields):
    y = 9.0 - i * 1.05

    ax.text(1.0, y, label, ha='left', va='center', fontsize=10, color=SILVER)
    ax.text(3.0, y, val, ha='left', va='center', fontsize=10, color=col,
            fontweight='bold')

    # Description on right
    ax.text(9.0, y, desc, ha='right', va='center', fontsize=8,
            color=DIM, fontstyle='italic')

ax.text(5, 0.8, "Every value has a return address. Every value knows what it is.\n"
        "The pool is not a spreadsheet " + r"$-$" + " it's a typed, sourced, versioned database.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk6_06_value_node_anatomy.png")


# ================================================================
# FIG 7: FIVE EXPERIMENTS — SIDE BY SIDE RESULTS
# Type: Comparison Bar (grid columns)
# Shows: wall of green with one red dot standing out
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-2, 11)

ax.text(8, 10.3, "Five Experiments, One Run Each",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

experiments = [
    ("QED\nalpha", 6, 6, 0, 0, GOLD,
     r"$\alpha^{-1}$ = 137.036" + "\n0.007 ppb"),
    ("Electroweak\nanatomy", 3, 3, 0, 0, CYAN,
     "pure gauge\ngap = 2 exact"),
    ("BBN\nbridge", 13, 11, 0, 2, GREEN,
     "D/H at 0.12" + r"$\sigma$"),
    ("Proton\ndecay", 2, 2, 0, 0, BLUE,
     r"$M_{GUT}$ at 10$^{15.5}$"),
    ("GR time\ndilation", 18, 7, 1, 10, RED,
     "Mercury\n2.8 ppm"),
]

for i, (name, total, p, f, info, col, key_result) in enumerate(experiments):
    cx = 1.5 + i * 3.0

    # Column header
    ax.text(cx, 9.5, name, ha='center', va='center', fontsize=10,
            color=col, fontweight='bold')

    # Dots for PASS, FAIL, INFO
    dot_y = 8.5
    dot_count = 0
    for d in range(p):
        ax.plot(cx + (dot_count % 3 - 1) * 0.35, dot_y - (dot_count // 3) * 0.4,
                'o', color=GREEN, markersize=8, alpha=0.7)
        dot_count += 1
    for d in range(f):
        ax.plot(cx + (dot_count % 3 - 1) * 0.35, dot_y - (dot_count // 3) * 0.4,
                'o', color=RED, markersize=8, alpha=0.9)
        dot_count += 1
    for d in range(info):
        ax.plot(cx + (dot_count % 3 - 1) * 0.35, dot_y - (dot_count // 3) * 0.4,
                'o', color=SILVER, markersize=6, alpha=0.5)
        dot_count += 1

    # Count summary
    summary_y = dot_y - (dot_count // 3 + 1) * 0.4 - 0.3
    summary = "%dP" % p
    if f > 0:
        summary += " %dF" % f
    if info > 0:
        summary += " %dI" % info
    ax.text(cx, summary_y, summary, ha='center', va='center',
            fontsize=9, color=col)

    # Key result
    ax.text(cx, summary_y - 1.2, key_result, ha='center', va='center',
            fontsize=8, color=SILVER,
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN))

ax.text(8, -0.5, "42 comparisons across five experiments. 41 PASS. 1 FAIL.\n"
        "The FAIL stays visible.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk6_07_five_experiments.png")


# ================================================================
# FIG 8: THE PASS/FAIL OUTPUT — TERMINAL VIEW
# Type: Identity Card (simulated terminal)
# Shows: raw monospace output with color coding
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor('#0d0d18')
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)

ax.text(8, 9.3, "What the Terminal Shows: Raw Output",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Terminal frame
term = mpatches.FancyBboxPatch((0.5, 1.5), 15.0, 7.0,
    boxstyle="round,pad=0.2", facecolor='#0a0a0f', alpha=0.8,
    linewidth=1.5)
ax.add_patch(term)

# Terminal title bar
title_bar = mpatches.FancyBboxPatch((0.5, 8.0), 15.0, 0.5,
    boxstyle="round,pad=0.05", facecolor=DIM, alpha=0.2,
    linewidth=0.5)
ax.add_patch(title_bar)
ax.text(8, 8.25, "experiment_gr_time_dilation_v0 " + r"$-$" + " results",
        ha='center', va='center', fontsize=8, color=SILVER,
        family='monospace')

lines = [
    ("[PASS]", "C01: alpha_inv vs Rb recoil", "digits  15 of 15 match", GREEN),
    ("[PASS]", "C02: alpha_inv vs CODATA", "digits  12 of 12 match", GREEN),
    ("[PASS]", "C03: series recovery 5-loop", "miss    0.000 ppm", GREEN),
    ("[INFO]", "C04: Mercury perihelion", "miss    2.8 ppm", SILVER),
    ("[FAIL]", "C05: Gravity Probe A", "miss    2.47% (gate: <1%)", RED),
    ("[PASS]", "C06: GPS net shift", "miss    0.35%", GREEN),
]

for i, (status, label, detail, col) in enumerate(lines):
    y = 7.3 - i * 0.8
    ax.text(1.2, y, status, ha='left', va='center', fontsize=10,
            color=col, fontweight='bold', family='monospace')
    ax.text(3.5, y, label, ha='left', va='center', fontsize=9,
            color=WHITE, family='monospace')
    ax.text(11.0, y, detail, ha='left', va='center', fontsize=9,
            color=SILVER, family='monospace')

# Summary line
ax.text(1.2, 2.3, "TOTAL:", ha='left', va='center', fontsize=10,
        color=WHITE, fontweight='bold', family='monospace')
ax.text(3.5, 2.3, "4 PASS   1 FAIL   1 INFO", ha='left', va='center',
        fontsize=10, color=WHITE, family='monospace')

ax.text(8, 0.8, "Same formatting. Same font size. PASS and FAIL in the same report.\n"
        "No hiding. No hierarchy. The computer doesn't care about your feelings.",
        ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

save(fig, "talk6_08_terminal_output.png")


# ================================================================
# FIG 9: THE GPA FAIL — ANATOMY OF AN HONEST FAILURE
# Type: Threshold/Region
# Shows: predicted dot outside the gate band
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

measured = 4.36e-10
meas_unc = 0.03e-10
predicted = 4.252e-10

# Measured band
ax.axhspan(measured - meas_unc * 3, measured + meas_unc * 3, color=MAG, alpha=0.05)
ax.axhspan(measured - meas_unc, measured + meas_unc, color=MAG, alpha=0.12)
ax.axhline(y=measured, color=MAG, linewidth=1.5, linestyle='--', alpha=0.6)

# 1% gate
gate_lo = measured * 0.99
gate_hi = measured * 1.01
ax.axhspan(gate_lo, gate_hi, color=GREEN, alpha=0.06)
ax.text(3.5, gate_hi + 0.005e-10, "1% gate", ha='center', va='bottom',
        fontsize=9, color=GREEN, alpha=0.7)

# Measured label
ax.text(3.0, measured + 0.02e-10, "Measured: (4.36 " + r"$\pm$" + " 0.03)" + r"$\times 10^{-10}$",
        ha='center', va='bottom', fontsize=10, color=MAG)
ax.text(3.0, measured - 0.025e-10, "Vessot-Levine 1980\nsuborbital rocket",
        ha='center', va='top', fontsize=8, color=MAG)

# Predicted point (outside gate)
ax.scatter([1.5], [predicted], s=250, color=GOLD, zorder=5, marker='o')
ax.text(1.5, predicted - 0.03e-10, "Predicted: 4.252" + r"$\times 10^{-10}$" +
        "\nUsing h = 10,000 km\n(round number)",
        ha='center', va='top', fontsize=9, color=GOLD)

# Miss arrow
ax.annotate("2.47%\nFAIL", xy=(2.2, measured), xytext=(2.2, predicted),
            fontsize=11, color=RED, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))

# Diagnosis
ax.text(3.0, 4.18e-10, "Diagnosis: round altitude (10,000 km) for a\n"
        "suborbital trajectory. Actual flight spent most\n"
        "time lower. Trajectory integral would close the gap.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.5, 4.5)
ax.set_ylim(4.15e-10, 4.45e-10)
ax.set_ylabel("Fractional frequency shift", fontsize=10, color=SILVER)
ax.set_xticks([])
ax.set_title("Gravity Probe A: The One That Failed",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(3.0, 4.16e-10, "The FAIL is published. The diagnosis is published.\n"
        "Neither is hidden. This is what honest testing looks like.",
        ha='center', va='center', fontsize=9, color=RED, fontstyle='italic')

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk6_09_gpa_fail.png")


# ================================================================
# FIG 10: PASS COUNT VS FAIL COUNT — THE RATIO
# Type: Comparison Bar
# Shows: enormous green bar, tiny red bar — ratio isn't the point
# ================================================================
fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

categories = ["PASS", "FAIL"]
counts = [252, 1]
colors_bar = [GREEN, RED]

bars = ax.bar(categories, counts, width=0.5, color=colors_bar, alpha=0.7)

# Labels on bars
ax.text(0, 252 + 8, "252", ha='center', va='bottom', fontsize=20,
        color=GREEN, fontweight='bold')
ax.text(1, 1 + 8, "1", ha='center', va='bottom', fontsize=20,
        color=RED, fontweight='bold')

# Annotation on FAIL
ax.text(1.3, 30, "GPA at 2.47%.\nUnderstood.\nNot hidden.",
        ha='left', va='center', fontsize=10, color=RED,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Ratio
ax.text(0.5, 200, "252 : 1", ha='center', va='center', fontsize=16,
        color=WHITE, fontweight='bold')

ax.text(0.5, 170, "The ratio isn't the point.\nThe point is that the 1 is there.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

ax.set_ylabel("Count", fontsize=11, color=SILVER)
ax.set_title("252 Pass. 1 Fail. Both Published.",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(0.5, 50, "The institution publishes successes and buries failures.\n"
        "This system publishes both in the same report,\nsame format, same font size.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(0, 290)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk6_10_pass_fail_ratio.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 6, 1-10) generated ===")
filenames = [
    "talk6_01_test_cycle.png",
    "talk6_02_test_vs_peer_review.png",
    "talk6_03_experiment_json.png",
    "talk6_04_five_match_modes.png",
    "talk6_05_value_pool.png",
    "talk6_06_value_node_anatomy.png",
    "talk6_07_five_experiments.png",
    "talk6_08_terminal_output.png",
    "talk6_09_gpa_fail.png",
    "talk6_10_pass_fail_ratio.png",
]
for f in filenames:
    print("  %s" % f)
    