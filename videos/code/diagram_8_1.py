#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 8, Slides 11-20
10 figures covering: typical session rhythm, confident wrongness,
institutional bias loop, five overrides, AI disclosure template,
honest vs dishonest disclosure, 10x multiplier, future division,
numbers don't change, CKS to RUM timeline.
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
# FIG 11: A TYPICAL SESSION — THE RHYTHM
# Type: Progression/Sequence (timeline)
# Shows: 7 steps with roles and durations — disciplined process
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 8)

ax.text(8, 7.3, "A Typical Session: 60-90 Minutes",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

steps = [
    (1.0, 5.0, "0 min", "HUMAN\narrives with\na question", GOLD, "Can we derive\nsin" + r"$^2\theta_W$?"),
    (3.3, 5.0, "5 min", "HUMAN\ndescribes\nin plain lang.", GOLD, "Run couplings\nfrom " + r"$M_{GUT}$"),
    (5.6, 5.0, "15 min", "AI\nwrites\ncode", CYAN, "def sin2_from_\ncrossing_v0():"),
    (7.9, 5.0, "20 min", "HUMAN\nreviews\ncode", GREEN, "Line 47: computing\nor copying?"),
    (10.2, 5.0, "25 min", "HUMAN\nruns\ncode", GREEN, "python data7.py\nrun experiment_..."),
    (12.5, 5.0, "30 min", "CHECK\nresults vs\nmeasurement", MAG, "[PASS] 12 ppm"),
    (14.8, 5.0, "35+ min", "ITERATE\nor next\nquestion", GOLD, "Next: derive\n" + r"$\alpha_s$"),
]

for i, (sx, sy, stime, slabel, scol, sexample) in enumerate(steps):
    rounded_box(ax, sx, sy, 1.9, 2.5, "", scol, alpha=0.12)
    ax.text(sx, sy + 0.9, stime, ha='center', va='center', fontsize=8,
            color=DIM)
    ax.text(sx, sy + 0.3, slabel, ha='center', va='center', fontsize=7,
            color=scol, fontweight='bold')
    ax.text(sx, sy - 0.7, sexample, ha='center', va='center', fontsize=6,
            color=SILVER, family='monospace')

    if i < len(steps) - 1:
        nx = steps[i+1][0]
        ax.annotate("", xy=(nx - 1.05, sy), xytext=(sx + 1.05, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Role color key
ax.text(3.0, 1.5, "GOLD = human decides", ha='center', va='center',
        fontsize=9, color=GOLD)
ax.text(7.0, 1.5, "CYAN = AI executes", ha='center', va='center',
        fontsize=9, color=CYAN)
ax.text(11.0, 1.5, "GREEN = human verifies", ha='center', va='center',
        fontsize=9, color=GREEN)

ax.text(8, 0.3, "Same rhythm. 1000+ sessions. The human never stops directing.\nThe AI never starts directing.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_11_session_rhythm.png")


# ================================================================
# FIG 12: CONFIDENT WRONGNESS
# Type: Comparison Bar (two panels)
# Shows: obvious error vs deceptive confidence
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The AI's Most Dangerous Failure: Confident and Wrong",
             fontsize=16, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Obvious error --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Obvious Error", ha='center', va='center',
         fontsize=13, fontweight='bold', color=RED)

# Terminal-style error
term1 = mpatches.FancyBboxPatch((0.5, 4.5), 9.0, 3.0,
    boxstyle="round,pad=0.15", facecolor='#0a0a0f', alpha=0.8,
    linewidth=1.5)
ax1.add_patch(term1)
ax1.text(5, 6.5, "Error: division by zero\nat line 34", ha='center', va='center',
         fontsize=12, color=RED, family='monospace')
ax1.text(5, 5.3, "Traceback visible.\nCrash is obvious.", ha='center', va='center',
         fontsize=9, color=SILVER, family='monospace')

ax1.text(5, 3.0, "Easy to catch.\nThe system tells you.", ha='center', va='center',
         fontsize=10, color=GREEN, fontstyle='italic')

ax1.text(5, 1.5, "Caught immediately.", ha='center', va='center',
         fontsize=12, color=GREEN, fontweight='bold')

# -- Right: Confident wrongness --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Confident Wrongness", ha='center', va='center',
         fontsize=13, fontweight='bold', color=ORANGE)

# Looks-correct output with hidden red border
term2 = mpatches.FancyBboxPatch((0.5, 4.5), 9.0, 3.0,
    boxstyle="round,pad=0.15", facecolor='#0a0a0f', alpha=0.8,
    linewidth=1.5)
ax2.add_patch(term2)
# Red border warning
warn = mpatches.FancyBboxPatch((0.3, 4.3), 9.4, 3.4,
    boxstyle="round,pad=0.15", facecolor='none', alpha=0.5,
    linewidth=2.5, linestyle='--')
ax2.add_patch(warn)

ax2.text(5, 6.5, r"sin$^2\theta_W$ = 3/8 at tree level" + "\n= 0.375",
         ha='center', va='center', fontsize=11, color=GREEN, family='monospace')
ax2.text(5, 5.3, "Delivered with full confidence.\nNo hedging. No caveats.",
         ha='center', va='center', fontsize=8, color=SILVER)

ax2.text(5, 3.0, "Looks correct. Sounds confident.\nThe CONTEXT is wrong.\n(tree level " + r"$\neq$" + " measured)",
         ha='center', va='center', fontsize=9, color=ORANGE, fontstyle='italic')

ax2.text(5, 1.5, "Human must know enough\nphysics to catch this.", ha='center', va='center',
         fontsize=10, color=RED, fontweight='bold')

fig.text(0.5, 0.04, "The AI never says 'I'm not sure.' It produces wrong answers\nwith the same confidence as right answers.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk8_12_confident_wrongness.png")


# ================================================================
# FIG 13: INSTITUTIONAL BIAS IN THE TRAINING DATA
# Type: Progression/Sequence (circular)
# Shows: institution -> data -> AI -> human pushback -> better critique
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

ax.text(7, 9.3, "The Institution Trained Its Own Opposition",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Circular nodes
nodes = [
    (2.0, 7.0, "INSTITUTION", "Publishes papers,\ntextbooks, Wikipedia", DIM),
    (7.0, 8.0, "TRAINING\nDATA", "Millions of documents\nencoding assumptions", DIM),
    (12.0, 7.0, "LLM", "Trained on\ninstitutional output.\nDefaults to consensus.", CYAN),
    (12.0, 3.0, "HUMAN", "Pushes back.\nIdentifies biases.\nReframes.", GOLD),
    (7.0, 2.0, "BETTER\nCRITIQUE", "Every bias identified\nmakes the critique\nclearer.", GREEN),
]

for nx, ny, nlabel, ndesc, ncol in nodes:
    rounded_box(ax, nx, ny, 3.0, 1.8, "", ncol, alpha=0.12)
    ax.text(nx, ny + 0.4, nlabel, ha='center', va='center', fontsize=10,
            color=ncol, fontweight='bold')
    ax.text(nx, ny - 0.4, ndesc, ha='center', va='center', fontsize=7,
            color=SILVER)

# Arrows
arrow_chain = [
    (3.5, 7.3, 5.5, 7.8),     # inst -> data
    (8.5, 7.8, 10.5, 7.3),    # data -> LLM
    (12.0, 6.0, 12.0, 4.0),   # LLM -> human
    (10.5, 2.7, 8.5, 2.3),    # human -> critique
    (5.5, 2.5, 3.0, 4.5),     # critique -> (loops back)
]
for x1, y1, x2, y2 in arrow_chain:
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=2,
                               connectionstyle='arc3,rad=0.15'))

# Institutional defaults listed
defaults = [
    "G is constant",
    "Forces don't unify at one-loop",
    "New physics requires new forces",
    "Entropy dominates",
]
ax.text(2.0, 4.5, "Institutional defaults:", ha='center', va='top',
        fontsize=8, color=RED, fontweight='bold')
for i, d in enumerate(defaults):
    ax.text(2.0, 3.8 - i * 0.5, d, ha='center', va='center',
            fontsize=7, color=RED,
            bbox=dict(boxstyle='round,pad=0.15', facecolor=BG, alpha=0.6))

ax.text(7, 0.3, "The AI is a sparring partner whose biases are the institution's biases.\n"
        "1000+ sessions of pushback sharpened the critique.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_13_institutional_bias.png")


# ================================================================
# FIG 14: FIVE INSTITUTIONAL DEFAULTS THE HUMAN OVERRODE
# Type: Comparison Bar (two columns)
# Shows: DIM defaults -> GOLD overrides, systematic pattern
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

ax.text(7, 9.3, "AI Default vs Human Override",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column headers
ax.text(4.0, 8.3, "AI Default\n(institutional consensus)", ha='center', va='center',
        fontsize=10, color=DIM, fontweight='bold')
ax.text(11.0, 8.3, "Human Override", ha='center', va='center',
        fontsize=10, color=GOLD, fontweight='bold')

overrides = [
    ("Use float64 for\nall computation", "Use Fraction.\nPreserve integers."),
    ("The forces don't\nunify exactly", "They unify if the gap\nis an exact Fraction"),
    ("Dark matter is weakly\ninteracting particles", "Dark matter is toroidal\ncirculation energy"),
    ("Use standard physics\nterminology", "Three nouns, two verbs.\nRectification of Names."),
    ("Present 725 ppm\nmatch as a result", "Block it. p = 0.81.\nNot significant yet."),
]

for i, (default, override) in enumerate(overrides):
    y = 7.0 - i * 1.4

    # Default (dim)
    rounded_box(ax, 4.0, y, 4.5, 1.0, default, DIM, fontsize=8, alpha=0.1, textcolor=DIM)

    # Arrow
    ax.annotate("", xy=(7.5, y), xytext=(6.5, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

    # Override (gold)
    rounded_box(ax, 11.0, y, 4.5, 1.0, override, GOLD, fontsize=8, alpha=0.15, textcolor=GOLD)

ax.text(7, 0.3, "The AI defaults to consensus because consensus is the training data.\n"
        "The human provides independent judgment the training data cannot.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_14_five_overrides.png")


# ================================================================
# FIG 15: AI DISCLOSURE TEMPLATE
# Type: Identity Card
# Shows: the actual disclosure block as it appears on papers
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "Every Paper's AI Disclosure",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Simulated paper header
paper = mpatches.FancyBboxPatch((0.5, 2.5), 9.0, 6.0,
    boxstyle="round,pad=0.2", facecolor=PAN, alpha=0.5,
    linewidth=1.5)
ax.add_patch(paper)

# Paper title
ax.text(5, 7.8, "PHYS-42: Reading Depth Across\nthe Soliton Hierarchy",
        ha='center', va='center', fontsize=13, fontweight='bold', color=GOLD)

# Author line
ax.text(5, 6.7, "Geoffrey Howland  and  Claude Opus 4.6",
        ha='center', va='center', fontsize=11, color=WHITE)

# Disclosure block with cyan border
disc = mpatches.FancyBboxPatch((1.0, 4.0), 8.0, 2.0,
    boxstyle="round,pad=0.15", facecolor=CYAN, alpha=0.08,
    linewidth=2)
ax.add_patch(disc)
# Left cyan border
ax.plot([1.0, 1.0], [4.0, 6.0], color=CYAN, linewidth=4, alpha=0.7)

ax.text(5, 5.3, "AI Usage Disclosure", ha='center', va='center',
        fontsize=10, color=CYAN, fontweight='bold')
ax.text(5, 4.7, "Only the top metadata, figures, refs and final copyright\n"
        "sections were edited by the author. All paper content was\n"
        "LLM-generated using Anthropic's Claude Opus 4.6.",
        ha='center', va='center', fontsize=8, color=SILVER)

# Arrow annotation
ax.annotate("Present on EVERY paper.\nSame wording. Same position.\nNot in fine print.\nFirst thing after the title.",
            xy=(9.3, 5.0), xytext=(10.0, 7.0),
            fontsize=8, color=GOLD, ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(5, 1.5, "This should be the standard, not the exception.\nThe reader knows what they're evaluating.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

save(fig, "talk8_15_disclosure_template.png")


# ================================================================
# FIG 16: HONEST VS DISHONEST DISCLOSURE
# Type: Comparison Bar (three panels)
# Shows: gradient from hidden to visible — visual density of disclosure
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 9),
                          gridspec_kw={'wspace': 0.20})
fig.patch.set_facecolor(BG)
fig.suptitle("Three Levels of AI Disclosure",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

panels = [
    ("Hidden", RED, "No AI mention\nanywhere.\n\nSearched:\n'AI' not found.\n'Claude' not found.\n'Language model'\nnot found.",
     "Reader assumes\nhuman did everything.\nDishonest if AI\ncontributed substantially."),
    ("Footnote", ORANGE, "Footnote 47,\npage 23:\n\n'AI-assisted\nediting'\n\n(4pt font)", "Technically present.\nPractically invisible.\nPlausible deniability."),
    ("RUM Standard", GREEN, "AI disclosure block\nat the top.\nSame size as abstract.\nBoth names on\nauthor line.\n\nImpossible to miss.", "Division of labor\ndocumented.\nReader informed.\nHonest."),
]

for idx, (title, col, content, verdict) in enumerate(panels):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.0, title, ha='center', va='center', fontsize=14,
            fontweight='bold', color=col)

    # Paper mockup
    paper_m = mpatches.FancyBboxPatch((1.0, 3.0), 8.0, 5.0,
        boxstyle="round,pad=0.15", facecolor=PAN, alpha=0.4,
        linewidth=1.5)
    ax.add_patch(paper_m)

    ax.text(5, 5.5, content, ha='center', va='center', fontsize=8,
            color=SILVER)

    ax.text(5, 1.5, verdict, ha='center', va='center', fontsize=8,
            color=col, fontstyle='italic')

fig.text(0.5, 0.04, "If honesty about AI is a reason to be dismissed,\n"
         "the dismissal tells you more about the institution than about the work.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk8_16_disclosure_levels.png")


# ================================================================
# FIG 17: THE 10x MULTIPLIER
# Type: Comparison Bar
# Shows: zero-length AI-alone bar — speed without direction = nothing
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

labels = ["Human alone", "AI alone", "Human + AI"]
values = [1, 0.05, 10]  # relative output
bar_colors = [DIM, RED, GOLD]

y = np.arange(len(labels))

for i in range(len(labels)):
    ax.barh(y[i], values[i], height=0.5, color=bar_colors[i], alpha=0.6)

# Labels
ax.text(1 + 0.3, 0, "1" + r"$\times$" + "\nCorrect direction.\nSlow execution.\nYears per framework.",
        ha='left', va='center', fontsize=9, color=DIM)

ax.text(0.3, 1, "~0" + r"$\times$" + "\nFast execution. No direction.\nComputes all day without\never checking against measurement.",
        ha='left', va='center', fontsize=9, color=RED)

ax.text(10 + 0.3, 2, "10" + r"$\times$" + "\nCorrect direction " + r"$\times$" + " fast execution.\n53 values across 9 domains in 6 days.",
        ha='left', va='center', fontsize=9, color=GOLD)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=12, color=WHITE)
ax.set_xlabel("Relative output", fontsize=11, color=SILVER)
ax.set_title("The Collaboration Multiplier",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(6, -0.7, "The person who figures out how to collaborate effectively with AI\n"
        "will outproduce the person who doesn't by an order of magnitude.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 15)
ax.set_ylim(-1.2, 2.8)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk8_17_10x_multiplier.png")


# ================================================================
# FIG 18: THE FUTURE DIVISION OF LABOR
# Type: Connection/Integer Map
# Shows: five human capabilities paired with five AI capabilities
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 10)

ax.text(7, 9.3, "The Future of Scientific Research",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column headers
ax.text(3.0, 8.3, "HUMAN provides", ha='center', va='center',
        fontsize=12, color=GOLD, fontweight='bold')
ax.text(11.0, 8.3, "AI provides", ha='center', va='center',
        fontsize=12, color=CYAN, fontweight='bold')

human_items = [
    "Direction:\nwhat questions to ask",
    "Values:\nwhat to publish, what to kill",
    "Methodology:\nfractions, test suite, kill switches",
    "Verification:\nread the code, catch errors",
    "Judgment:\ncoincidence or physics?",
]

ai_items = [
    "Computation:\n200-digit precision",
    "Speed:\n60 papers in 8 days",
    "Literature:\n9 domains traversed",
    "Drafting:\npapers, code, specifications",
    "Consistency:\nnever tired, never forgets",
]

for i in range(5):
    y = 7.0 - i * 1.3

    # Human (gold)
    rounded_box(ax, 3.0, y, 4.0, 0.9, human_items[i], GOLD, fontsize=7, alpha=0.15, textcolor=GOLD)

    # Bidirectional arrow
    ax.annotate("", xy=(6.5, y), xytext=(5.2, y),
                arrowprops=dict(arrowstyle='<->', color=DIM, lw=1.5))

    # AI (cyan)
    rounded_box(ax, 11.0, y, 4.0, 0.9, ai_items[i], CYAN, fontsize=7, alpha=0.15, textcolor=CYAN)

ax.text(7, 0.3, "Neither can do what the other does. Both are necessary. Both are credited.\n"
        "Not AI replacing humans. Not humans ignoring AI. Collaboration with honest attribution.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_18_future_division.png")


# ================================================================
# FIG 19: THE NUMBERS DON'T CHANGE
# Type: Identity Card
# Shows: results with attribution — authorship doesn't affect truth
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "The AI on the Cover Doesn't Change the Fractions",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

results = [
    (r"$\alpha^{-1}$ = 137.035999207", "Miss: 0.007 ppb", GOLD),
    (r"sin$^2\theta_W$ = 0.23122", "Miss: 12 ppm", CYAN),
    ("D/H = 2.531 " + r"$\times 10^{-5}$", "Miss: 0.12" + r"$\sigma$", GREEN),
]

for i, (result, miss, col) in enumerate(results):
    y = 7.5 - i * 1.5

    rounded_box(ax, 3.5, y, 5.5, 1.0, "", col, alpha=0.12)
    ax.text(3.5, y + 0.15, result, ha='center', va='center', fontsize=12,
            color=col, fontweight='bold')
    ax.text(3.5, y - 0.25, miss, ha='center', va='center', fontsize=9,
            color=SILVER)

    # Attribution
    ax.text(8.5, y, "Computed by AI.\nDirected by human.\nVerified by measurement.",
            ha='left', va='center', fontsize=7, color=DIM)

# Central message
ax.text(5, 3, "The numbers match or they don't.\nThe AI on the cover doesn't change the fractions.\nThe fractions are checkable regardless\nof who or what produced them.",
        ha='center', va='center', fontsize=13, color=GOLD, fontweight='bold',
        linespacing=1.6)

ax.text(5, 1.0, "Check the numbers. That's all that matters.",
        ha='center', va='center', fontsize=14, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk8_19_numbers_dont_change.png")


# ================================================================
# FIG 20: THE TIMELINE — CKS TO RUM
# Type: Progression/Sequence (timeline)
# Shows: failure as pivot point — CKS kill drives everything
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Timeline base
ax.plot([0.5, 11.5], [1.0, 1.0], color=DIM, linewidth=2, alpha=0.5)

events = [
    (1.0, "Jan 2026", "CKS begins\n45 days, 363 papers", CYAN, 'o', 120),
    (3.5, "Feb 15", "Circular reference\nfound in AI code", RED, 'X', 200),
    (5.0, "Feb 16", "363 papers killed\non Zenodo", RED, 'o', 120),
    (6.5, "Mar 2026", "RUM begins\n6 days: fractions,\nQ335, test suite", GOLD, '*', 250),
    (8.5, "Mar-Apr", "8 sessions\n60+ papers\n253 comparisons\n9 domains", GREEN, 'o', 150),
    (10.5, "Apr 2026", "This video", GOLD, '*', 300),
]

for i, (ex, edate, edesc, ecol, emark, esize) in enumerate(events):
    ax.scatter([ex], [1.0], s=esize, color=ecol, zorder=5, marker=emark)

    # Alternate above and below
    if i % 2 == 0:
        y_text = 2.2 + (i % 3) * 0.3
        va = 'bottom'
    else:
        y_text = -0.2 - (i % 3) * 0.2
        va = 'top'

    ax.plot([ex, ex], [1.0, y_text], color=ecol, linewidth=1, alpha=0.4)
    ax.text(ex, y_text, edate + "\n" + edesc, ha='center', va=va,
            fontsize=8, color=ecol, fontweight='bold' if emark == '*' else 'normal')

# Lesson arrows below
ax.text(4.25, -1.8, "Lesson:\nread the\ncode", ha='center', va='center',
        fontsize=7, color=RED, fontstyle='italic')
ax.text(5.75, -1.8, "Lesson:\nuse\nfractions", ha='center', va='center',
        fontsize=7, color=GOLD, fontstyle='italic')
ax.text(7.5, -1.8, "Lesson:\nautomate\ntesting", ha='center', va='center',
        fontsize=7, color=GREEN, fontstyle='italic')
ax.text(9.5, -1.8, "Lesson:\npublish\nfailures", ha='center', va='center',
        fontsize=7, color=ORANGE, fontstyle='italic')

ax.set_title("From Failure to Framework: The Complete Timeline",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(6, -2.8, "The failure was the teacher. The AI was the tool.\nThe human was the student who learned and changed the methodology.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0.2, 11.8)
ax.set_ylim(-3.2, 4.5)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk8_20_cks_to_rum_timeline.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 8, 11-20) generated ===")
filenames = [
    "talk8_11_session_rhythm.png",
    "talk8_12_confident_wrongness.png",
    "talk8_13_institutional_bias.png",
    "talk8_14_five_overrides.png",
    "talk8_15_disclosure_template.png",
    "talk8_16_disclosure_levels.png",
    "talk8_17_10x_multiplier.png",
    "talk8_18_future_division.png",
    "talk8_19_numbers_dont_change.png",
    "talk8_20_cks_to_rum_timeline.png",
]
for f in filenames:
    print("  %s" % f)
