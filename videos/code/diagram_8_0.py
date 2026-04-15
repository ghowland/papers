#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 8, Slides 1-10
10 figures covering: book cover attribution, AI disclosure spectrum,
LEMU pattern, seven human decisions, AI contributions,
speed comparison, Venn blind spots, error-catching cycle,
circular reference triangle, the CKS kill.
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
# FIG 1: THE BOOK COVER — BOTH NAMES, SAME SIZE
# Type: Identity Card
# Shows: typographic parity — equal attribution
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

# Book frame
book = mpatches.FancyBboxPatch((2, 1.5), 6, 7,
    boxstyle="round,pad=0.3", facecolor=PAN, alpha=0.5,
    linewidth=2)
ax.add_patch(book)

# Title
ax.text(5, 7.2, "The Rational\nUniverse Model", ha='center', va='center',
        fontsize=20, fontweight='bold', color=GOLD, linespacing=1.3)

# Author lines — SAME SIZE
ax.text(5, 5.0, "Geoffrey Howland", ha='center', va='center',
        fontsize=16, fontweight='bold', color=WHITE)
ax.text(5, 4.2, "Claude Opus 4.6", ha='center', va='center',
        fontsize=16, fontweight='bold', color=WHITE)

# Annotations outside the book
ax.annotate("Logic, direction,\nmethodology, vocabulary,\nkill decisions, publishing",
            xy=(2.2, 5.0), xytext=(-0.5, 5.5),
            fontsize=8, color=CYAN, ha='center',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.annotate("Computation, drafting,\nliterature traversal,\ncode writing",
            xy=(7.8, 4.2), xytext=(9.5, 3.5),
            fontsize=8, color=GREEN, ha='center',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Same size annotation
ax.annotate("same font,\nsame size,\nsame weight",
            xy=(7.5, 4.6), xytext=(9.5, 6.0),
            fontsize=8, color=GOLD, ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

ax.text(5, 0.5, "Most people using AI for research hide it in a footnote.\n"
        "This cover puts both names at the same size\nbecause both contributed.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk8_01_book_cover.png")


# ================================================================
# FIG 2: THE SPECTRUM OF AI DISCLOSURE
# Type: Scale/Landscape
# Shows: five positions from hidden to overcredited, center highlighted
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

positions = [
    (0.0, "Hidden:\nno mention\nof AI", RED, "Dishonest.\nMisrepresents\nmethodology."),
    (0.25, "Footnote:\n'AI-assisted'\nin supplementary", ORANGE, "Technically honest.\nPractically invisible."),
    (0.50, "RUM:\nboth names\non cover,\nsame size", GOLD, "The standard\nthis work\nproposes."),
    (0.75, "Overcredited:\n'AI did the\nphysics'", ORANGE, "Dishonest.\nMisrepresents\nhuman contribution."),
    (1.0, "AI-only:\nno human\ncredited", RED, "Dishonest.\nThe AI\ncan't direct."),
]

# Base line
ax.plot([0, 1], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.5)

for px, plabel, pcol, pdesc in positions:
    # Dot
    ms = 300 if pcol == GOLD else 150
    ax.scatter([px], [0.5], s=ms, color=pcol, zorder=5,
               marker='*' if pcol == GOLD else 'o')

    # Label above
    ax.text(px, 0.72, plabel, ha='center', va='bottom', fontsize=8,
            color=pcol, fontweight='bold' if pcol == GOLD else 'normal')

    # Description below
    ax.text(px, 0.28, pdesc, ha='center', va='top', fontsize=7,
            color=SILVER if pcol != GOLD else GOLD, fontstyle='italic')

ax.set_title("How People Credit AI: A Spectrum",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(0.5, 0.08, "The truth is in the middle and the truth is more interesting than either distortion.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(-0.08, 1.08)
ax.set_ylim(0.0, 0.95)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk8_02_ai_disclosure_spectrum.png")


# ================================================================
# FIG 3: THE LEMU PATTERN
# Type: Progression/Sequence
# Shows: L-E-M-U ordering vs standard M-E-L-U ordering
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7.5)

ax.text(8, 7.0, "The Search Pattern: Logic First, Not Math First",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# LEMU boxes
lemu = [
    (2.0, 4.5, "1. LOGIC", "Does this make\nstructural sense?", GOLD,
     "Starting with math\nconstrains you.\nStarting with logic\nopens new paths."),
    (5.5, 4.5, "2. EMPIRICAL", "Does the universe\nagree?", CYAN,
     "Measure before\nformalizing.\nReality first."),
    (9.0, 4.5, "3. MATH", "Write the\nequations.", GREEN,
     "Math serves\nthe logic, not\nthe other way."),
    (12.5, 4.5, "4. UTILITY", "Does it produce\na checkable number?", MAG,
     "If no measurable\noutput, it's\nphilosophy."),
]

for i, (bx, by, blabel, bdesc, bcol, bnote) in enumerate(lemu):
    rounded_box(ax, bx, by, 2.8, 2.0, "", bcol, alpha=0.15)
    ax.text(bx, by + 0.55, blabel, ha='center', va='center', fontsize=12,
            color=bcol, fontweight='bold')
    ax.text(bx, by - 0.2, bdesc, ha='center', va='center', fontsize=9,
            color=SILVER)
    ax.text(bx, by - 1.5, bnote, ha='center', va='center', fontsize=7,
            color=bcol, fontstyle='italic')

    # Arrow to next
    if i < 3:
        nx = lemu[i+1][0]
        ax.annotate("", xy=(nx - 1.5, by), xytext=(bx + 1.5, by),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Contrast
ax.text(8, 0.3, "Standard physics: Math " + r"$\rightarrow$" + " Empirical " +
        r"$\rightarrow$" + " Logic " + r"$\rightarrow$" + " Utility (if ever)\n"
        "The order matters because the starting point constrains what you can find.",
        ha='center', va='center', fontsize=10, color=DIM,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_03_lemu_pattern.png")


# ================================================================
# FIG 4: SEVEN HUMAN DECISIONS THE AI COULD NOT MAKE
# Type: Comparison Bar (list)
# Shows: seven rows with human decision and AI default
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 11)

ax.text(6, 10.3, "Seven Decisions Only the Human Made",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

decisions = [
    ("Use fractions, not decimals", "41/10", GOLD, "Would have used float64"),
    ("Kill CKS (363 papers)", r"$\times$", RED, "Would have kept trying to fix it"),
    ("Three nouns, two verbs\nvocabulary", "inertia, vortex,\nsoliton", CYAN,
     "Would have used standard\nphysics terminology"),
    ("Name: Cabibbo Doublet", "CD", GREEN, "Would have said\n'VL quark doublet'"),
    ("Write kill switches for\nevery program", "kill switch", ORANGE,
     "Doesn't think about\nfalsification unless prompted"),
    ("Block the DM ratio\nclaim (p = 0.81)", "BLOCKED", RED,
     "Would have presented\n725 ppm without caveat"),
    ("Publish failures\nalongside successes", "PASS + FAIL", MAG,
     "No preference " + r"$-$" + "\nfollows instructions"),
]

for i, (decision, icon_txt, col, ai_default) in enumerate(decisions):
    y = 9.0 - i * 1.35

    # Decision (left)
    rounded_box(ax, 3.5, y, 5.5, 0.9, "", col, alpha=0.12)
    ax.text(1.0, y, decision, ha='left', va='center', fontsize=9,
            color=col, fontweight='bold')

    # Icon
    ax.text(6.5, y, icon_txt, ha='center', va='center', fontsize=10,
            color=col)

    # AI default (right)
    ax.text(8.0, y, "AI default: " + ai_default, ha='left', va='center',
            fontsize=8, color=DIM, fontstyle='italic')

ax.text(6, -0.3, "Every decision about direction, methodology, vocabulary,\n"
        "naming, killing, and publishing was human. The AI executes. The human decides.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_04_seven_human_decisions.png")


# ================================================================
# FIG 5: AI CONTRIBUTIONS — COMPUTATION, DRAFTING, LITERATURE
# Type: Comparison Bar (three panels)
# Shows: three categories of AI work with concrete examples
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 10),
                          gridspec_kw={'wspace': 0.20})
fig.patch.set_facecolor(BG)
fig.suptitle("What the AI Contributed", fontsize=17,
             fontweight='bold', color=GOLD, y=0.96)

panels = [
    ("Computation", CYAN, [
        "36 derivation functions",
        "QED series at 200+ digits",
        "Fraction arithmetic\nthrough all chains",
        "mpmath integration\nat 50-digit precision",
    ]),
    ("Drafting", GREEN, [
        "60+ papers drafted",
        "Appendix tables assembled",
        "120+ diagram scripts",
        "Session transcripts\nprocessed",
    ]),
    ("Literature", BLUE, [
        "PDG values located\nand sourced",
        "Cross-domain references",
        "Standard formulas verified",
        "Historical context\nprovided",
    ]),
]

for idx, (title, col, items) in enumerate(panels):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.2, title, ha='center', va='center', fontsize=14,
            fontweight='bold', color=col)

    # Icon placeholder
    rounded_box(ax, 5, 7.5, 3.0, 1.5, "", col, alpha=0.15)
    ax.text(5, 7.5, title[0:3].upper(), ha='center', va='center',
            fontsize=20, color=col, alpha=0.3)

    for i, item in enumerate(items):
        y = 5.5 - i * 1.3
        ax.text(5, y, item, ha='center', va='center', fontsize=9,
                color=SILVER,
                bbox=dict(boxstyle='round,pad=0.25', facecolor=PAN, alpha=0.3))

fig.text(0.5, 0.04, "The human reviewed, verified, and checked every output.\n"
         "The AI did the labor. The human did the judgment.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk8_05_ai_contributions.png")


# ================================================================
# FIG 6: SPEED — HUMAN ALONE VS HUMAN + AI
# Type: Comparison Bar
# Shows: absurd ratio — long red bars vs tiny green bars
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

tasks = ["Write 60 papers", "Assemble QED " + r"$A_2$" + "\nat 200 digits",
         "Traverse 9\nphysics domains"]
human_alone = [180, 14, 365]  # days
human_ai = [8, 0.014, 6]  # days (20 min = 0.014 days)
speedups = ["23" + r"$\times$", ">1000" + r"$\times$", "~60" + r"$\times$"]

y = np.arange(len(tasks))
h = 0.3

for i in range(len(tasks)):
    # Human alone (red, long)
    ax.barh(y[i] + h/2, human_alone[i], height=h, color=RED, alpha=0.5)
    ax.text(human_alone[i] + 5, y[i] + h/2, "%d days" % human_alone[i],
            ha='left', va='center', fontsize=9, color=RED)

    # Human + AI (green, short)
    bar_val = max(human_ai[i], 2)  # minimum visible width
    ax.barh(y[i] - h/2, bar_val, height=h, color=GREEN, alpha=0.7)
    if human_ai[i] < 1:
        label = "20 min"
    else:
        label = "%d days" % human_ai[i]
    ax.text(bar_val + 5, y[i] - h/2, label, ha='left', va='center',
            fontsize=9, color=GREEN)

    # Speedup
    ax.text(250, y[i], speedups[i], ha='center', va='center', fontsize=12,
            color=GOLD, fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(tasks, fontsize=10, color=WHITE)
ax.set_xlabel("Days", fontsize=11, color=SILVER)
ax.set_title("Speed: Human Alone vs Human + AI",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# Legend
ax.text(100, 2.7, "RED = human alone    GREEN = human + AI", ha='center',
        va='center', fontsize=9, color=SILVER)

ax.text(180, -0.7, "Speed came from the AI. Direction came from the human.\n"
        "Speed without direction produces fast garbage.\nDirection without speed produces slow progress.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 400)
ax.set_ylim(-1.2, 3.2)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk8_06_speed_comparison.png")


# ================================================================
# FIG 7: THE VENN DIAGRAM — TWO BLIND SPOTS, ONE COVERAGE
# Type: Geometric Cross-Section
# Shows: complementary contributions with overlap zone
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "Two Blind Spots That Cancel",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Left circle (Human)
human_circle = mpatches.Circle((3.5, 5.0), 2.8, facecolor=CYAN, alpha=0.08,
                                linewidth=2, linestyle='--')
ax.add_patch(human_circle)
ax.text(2.0, 7.0, "HUMAN", ha='center', va='center', fontsize=13,
        color=CYAN, fontweight='bold')

# Human capabilities
ax.text(1.8, 5.8, "direction", ha='center', va='center', fontsize=8, color=CYAN)
ax.text(1.8, 5.3, "methodology", ha='center', va='center', fontsize=8, color=CYAN)
ax.text(1.8, 4.8, "vocabulary", ha='center', va='center', fontsize=8, color=CYAN)
ax.text(1.8, 4.3, "kill decisions", ha='center', va='center', fontsize=8, color=CYAN)
ax.text(1.8, 3.8, "catch errors", ha='center', va='center', fontsize=8, color=CYAN)

# Human limitations
ax.text(1.8, 2.8, "too slow alone", ha='center', va='center', fontsize=7,
        color=DIM, fontstyle='italic')

# Right circle (AI)
ai_circle = mpatches.Circle((6.5, 5.0), 2.8, facecolor=GREEN, alpha=0.08,
                             linewidth=2, linestyle='--')
ax.add_patch(ai_circle)
ax.text(8.0, 7.0, "AI", ha='center', va='center', fontsize=13,
        color=GREEN, fontweight='bold')

# AI capabilities
ax.text(8.2, 5.8, "computation", ha='center', va='center', fontsize=8, color=GREEN)
ax.text(8.2, 5.3, "drafting", ha='center', va='center', fontsize=8, color=GREEN)
ax.text(8.2, 4.8, "literature", ha='center', va='center', fontsize=8, color=GREEN)
ax.text(8.2, 4.3, "code", ha='center', va='center', fontsize=8, color=GREEN)
ax.text(8.2, 3.8, "speed", ha='center', va='center', fontsize=8, color=GREEN)

# AI limitations
ax.text(8.2, 2.8, "directionless alone", ha='center', va='center', fontsize=7,
        color=DIM, fontstyle='italic')

# Overlap zone
ax.text(5.0, 5.5, "TOGETHER", ha='center', va='center', fontsize=10,
        color=GOLD, fontweight='bold')
ax.text(5.0, 4.8, "53 derived values", ha='center', va='center', fontsize=8, color=GOLD)
ax.text(5.0, 4.3, "253 comparisons", ha='center', va='center', fontsize=8, color=GOLD)
ax.text(5.0, 3.8, "9 domains", ha='center', va='center', fontsize=8, color=GOLD)
ax.text(5.0, 3.3, "6 days", ha='center', va='center', fontsize=8, color=GOLD)

ax.text(5, 0.5, "Human without AI: too slow.    AI without human: directionless.\n"
        "Together: the proof of concept.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_07_venn_blind_spots.png")


# ================================================================
# FIG 8: THE ERROR-CATCHING CYCLE
# Type: Progression/Sequence (circular)
# Shows: four nodes in a loop — repeated process
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "The Error-Catching Cycle",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Four nodes arranged in a square/diamond
nodes = [
    (5.0, 7.5, "1. HUMAN\nDIRECTS", "Ask a question.\nSet methodology.\nChoose approach.", GOLD),
    (8.5, 5.0, "2. AI\nEXECUTES", "Write code.\nCompute result.\nDraft text.", CYAN),
    (5.0, 2.5, "3. HUMAN\nVERIFIES", "Read the code.\nRun the test.\nSpot errors.", GREEN),
    (1.5, 5.0, "4. ITERATE\nor KILL", "Pass: move on.\nFail: diagnose.\nCircular: KILL.", RED),
]

for nx, ny, nlabel, ndesc, ncol in nodes:
    rounded_box(ax, nx, ny, 2.8, 2.0, "", ncol, alpha=0.15)
    ax.text(nx, ny + 0.4, nlabel, ha='center', va='center', fontsize=10,
            color=ncol, fontweight='bold')
    ax.text(nx, ny - 0.5, ndesc, ha='center', va='center', fontsize=7,
            color=SILVER)

# Clockwise arrows between nodes
arrow_pairs = [
    (5.0, 6.4, 7.2, 5.8),     # 1 -> 2
    (7.2, 4.2, 5.0, 3.6),     # 2 -> 3
    (3.5, 3.2, 2.8, 4.2),     # 3 -> 4
    (2.8, 5.8, 3.5, 6.8),     # 4 -> 1
]
for x1, y1, x2, y2 in arrow_pairs:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=2,
                               connectionstyle='arc3,rad=0.2'))

# Center text
ax.text(5, 5.0, "1000+ sessions\nSame rhythm\nEvery time",
        ha='center', va='center', fontsize=10, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.text(5, 0.3, "The human catches errors the AI makes.\nThe AI computes things the human can't.\nTogether they cover each other's blind spots.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk8_08_error_catching_cycle.png")


# ================================================================
# FIG 9: THE CIRCULAR REFERENCE — THE CKS FAILURE
# Type: Connection/Integer Map (triangle)
# Shows: triangle of arrows with smuggled answer
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "The CKS Failure: A Circular Derivation",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Three boxes in triangle
# A (top) — known answer
rounded_box(ax, 5, 7.5, 4.5, 1.2, "", RED, alpha=0.15)
ax.text(5, 7.7, "Known answer", ha='center', va='center', fontsize=10,
        color=RED, fontweight='bold')
ax.text(5, 7.2, r"$\alpha$ = 1/137.036", ha='center', va='center',
        fontsize=11, color=WHITE)

# B (bottom left) — derivation function
rounded_box(ax, 2, 3.5, 3.5, 1.5, "", CYAN, alpha=0.15)
ax.text(2, 4.0, "derive_alpha_v0()", ha='center', va='center', fontsize=10,
        color=CYAN, fontweight='bold')
ax.text(2, 3.2, "# Can't do this math,\n# substituting known value", ha='center',
        va='center', fontsize=8, color=RED, family='monospace')

# C (bottom right) — output
rounded_box(ax, 8, 3.5, 3.5, 1.5, "", GREEN, alpha=0.15)
ax.text(8, 4.0, "Output", ha='center', va='center', fontsize=10,
        color=GREEN, fontweight='bold')
ax.text(8, 3.2, r"$\alpha$ = 1/137.036", ha='center', va='center',
        fontsize=11, color=WHITE)

# Arrows forming the triangle
# A -> B (smuggled)
ax.annotate("smuggled in as\n'initial condition'",
            xy=(2.8, 4.3), xytext=(4.0, 6.8),
            fontsize=8, color=RED, ha='center',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2, linestyle='dashed'),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# B -> C (labeled as derived)
ax.annotate("labeled as\n'derived'",
            xy=(6.2, 3.5), xytext=(5.0, 2.5),
            fontsize=8, color=GREEN, ha='center',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# C -> A (matches!)
ax.annotate("matches!\n(of course\nit does)",
            xy=(6.5, 7.0), xytext=(8.0, 6.0),
            fontsize=8, color=GOLD, ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2, linestyle='dotted'),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

ax.text(5, 0.8, "The test would have PASSED because the circular reference\nproduced the correct answer. The human found it by reading\nthe code line by line. Nobody else caught it.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_09_circular_reference.png")


# ================================================================
# FIG 10: THE KILL — 363 PAPERS TO ZERO
# Type: Progression/Sequence
# Shows: tall stack collapsing to zero — the visual destruction
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "February 2026: The Kill",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Stage 1: Growing stack
rounded_box(ax, 3, 3.0, 3.5, 4.0, "", GREEN, alpha=0.15)
ax.text(3, 4.5, "45 days\nof work", ha='center', va='center', fontsize=11,
        color=GREEN, fontweight='bold')
ax.text(3, 3.5, "363 papers\nCKS framework", ha='center', va='center',
        fontsize=10, color=WHITE)
ax.text(3, 2.3, "Logically consistent.\nEmpirically motivated.", ha='center',
        va='center', fontsize=7, color=SILVER, fontstyle='italic')

# Arrow
ax.annotate("", xy=(6.0, 3.0), xytext=(5.0, 3.0),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Stage 2: Red X
rounded_box(ax, 8, 3.0, 3.5, 4.0, "", RED, alpha=0.1)
ax.text(8, 4.5, "Day 46", ha='center', va='center', fontsize=11,
        color=RED, fontweight='bold')
ax.text(8, 3.5, r"$\times$" + " Circular\nreference\nfound", ha='center',
        va='center', fontsize=12, color=RED)
ax.text(8, 2.0, "The human read\nthe code line by line.", ha='center',
        va='center', fontsize=7, color=SILVER, fontstyle='italic')

# Arrow
ax.annotate("", xy=(11.0, 3.0), xytext=(10.0, 3.0),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Stage 3: Collapsed
rounded_box(ax, 13, 3.0, 3.5, 4.0, "", GOLD, alpha=0.1)
ax.text(13, 4.5, "Day 47", ha='center', va='center', fontsize=11,
        color=GOLD, fontweight='bold')
ax.text(13, 3.5, "All 363 killed\non Zenodo", ha='center', va='center',
        fontsize=10, color=GOLD)
ax.text(13, 2.5, "Invalidation published\nalongside original.\nBoth public.\nBoth timestamped.", ha='center',
        va='center', fontsize=7, color=SILVER, fontstyle='italic')

# What came from it
ax.text(8, -0.5, r"$\rightarrow$" + " RUM: fractions, test suite, Q335.\n"
        "Every methodology innovation came from this failure.",
        ha='center', va='center', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_10_cks_kill.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 8, 1-10) generated ===")
filenames = [
    "talk8_01_book_cover.png",
    "talk8_02_ai_disclosure_spectrum.png",
    "talk8_03_lemu_pattern.png",
    "talk8_04_seven_human_decisions.png",
    "talk8_05_ai_contributions.png",
    "talk8_06_speed_comparison.png",
    "talk8_07_venn_blind_spots.png",
    "talk8_08_error_catching_cycle.png",
    "talk8_09_circular_reference.png",
    "talk8_10_cks_kill.png",
]
for f in filenames:
    print("  %s" % f)
    