#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 5, Slides 11-20
10 figures covering: PSLQ 82/82 null, derivation vs search,
computation pipeline, exact/approximate boundary, type system,
hadronic VP distinction, 38/27 revelation, three revelations,
grandmother principle applied, summary card.
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
# FIG 11: PSLQ 82/82 NULL — WALL OF RED
# Type: Comparison Bar (grid)
# Shows: 82 squares all red — exhaustive independence
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 10)

ax.text(8, 9.3, "PSLQ Independence Tests: 82/82 Null",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Grid of 82 red squares, 10 per row
cols = 10
rows_needed = 9  # 82 = 8*10 + 2
count = 0
sample_labels = {
    0: r"$\pi$ vs $\zeta(3)$",
    11: r"ln 2 vs $\sqrt{2}$",
    25: r"$\pi^2$ vs $\zeta(5)$",
    40: r"$e$ vs ln 3",
    55: r"$\sqrt{5}$ vs $\phi$",
    70: r"Li$_4$ vs $\zeta(7)$",
}

for row in range(rows_needed):
    for col in range(cols):
        if count >= 82:
            break
        x = 1.0 + col * 1.35
        y = 7.8 - row * 0.85

        rect = mpatches.FancyBboxPatch((x, y), 1.1, 0.65,
            boxstyle="round,pad=0.05", facecolor=RED, alpha=0.25,
            linewidth=0.5)
        ax.add_patch(rect)
        ax.text(x + 0.55, y + 0.33, "null", ha='center', va='center',
                fontsize=6, color=RED, alpha=0.7)

        if count in sample_labels:
            ax.text(x + 0.55, y + 0.55, sample_labels[count], ha='center',
                    va='bottom', fontsize=5, color=SILVER, alpha=0.6)

        count += 1

ax.text(8, -0.0, "82 tests for integer linear relations between transcendental constants.\n"
        "Zero found. The constants are independent.\nNo shortcut. No magic formula. You compute them and store them.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

ax.text(14.5, -0.8, "Published as MATH-6.\nDerivation beats search.",
        ha='center', va='center', fontsize=9, color=GOLD)

save(fig, "talk5_11_pslq_82_null.png")


# ================================================================
# FIG 12: DERIVATION VS SEARCH — TWO PHILOSOPHIES
# Type: Comparison Bar (two panels)
# Shows: passive search finding nothing vs active construction
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Two Philosophies of Mathematical Constants",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Search (PSLQ) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Search (PSLQ)", ha='center', va='center',
         fontsize=14, fontweight='bold', color=RED)

# Magnifying glass shape
circle = mpatches.Circle((4, 5.5), 1.8, facecolor='none',
                          linewidth=3, linestyle='-')
ax1.add_patch(circle)
ax1.plot([5.3, 7.0], [4.2, 2.5], color=DIM, linewidth=3)

# Scattered question marks
for qx, qy in [(2.5, 6.5), (5.5, 6.8), (3.0, 4.5), (5.0, 4.0), (4.0, 7.5)]:
    ax1.text(qx, qy, "?", ha='center', va='center', fontsize=16,
             color=RED, alpha=0.4)

ax1.text(5, 2.0, "Look for hidden relations.\nHope for a shortcut.\n82 tests. Zero relations.\nNo shortcut exists.",
         ha='center', va='center', fontsize=10, color=RED, fontstyle='italic')

# -- Right: Derivation (Q335) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Derivation (Q335)", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GOLD)

# Factory: input arrow → box → output arrow
ax2.annotate("", xy=(3.5, 6.0), xytext=(1.5, 6.0),
             arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax2.text(1.0, 6.0, "series", ha='center', va='center', fontsize=9, color=CYAN)

rounded_box(ax2, 5, 6.0, 2.5, 1.5, "compute\n101 digits", GOLD, fontsize=10, alpha=0.2)

ax2.annotate("", xy=(8.5, 6.0), xytext=(6.5, 6.0),
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax2.text(9.0, 6.0, "exact\nFraction", ha='center', va='center', fontsize=9, color=GREEN)

# Output examples
examples = [r"$\pi$", r"$\zeta(3)$", "ln 2", r"$\sqrt{2}$", r"$e^\pi$"]
for i, ex in enumerate(examples):
    ax2.text(2.0 + i * 1.5, 4.0, ex, ha='center', va='center', fontsize=10,
             color=GOLD, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN))

ax2.text(5, 2.0, "Compute each constant to 101 digits.\nStore as integer / " + r"$2^{335}$." +
         "\nUse exact arithmetic.\nNo relation needed.",
         ha='center', va='center', fontsize=10, color=GOLD, fontstyle='italic')

# Arrow between panels
fig.text(0.50, 0.50, "When search\nfails, derive.", ha='center', va='center',
         fontsize=11, color=WHITE, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

save(fig, "talk5_12_derivation_vs_search.png")


# ================================================================
# FIG 13: THE PIPELINE — INPUT TO OUTPUT WITHOUT A DECIMAL
# Type: Progression/Sequence
# Shows: seven stages, no decimal until the last
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-1.5, 7)

ax.text(9, 6.3, "The Complete Derivation Pipeline",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

stages = [
    (1.0, 3.5, "Pool\ninput", r"$\alpha^{-1}$=137.../10$^9$", GOLD, "exact_fraction"),
    (3.5, 3.5, "Load", "Fraction\npreserved", CYAN, "no float"),
    (6.0, 3.5, "Compute", "multiply, divide\nadd Fractions", GREEN, "still exact"),
    (8.5, 3.5, "Q335\nentry", r"$\pi$ enters as" + "\nint/" + r"$2^{335}$", BLUE, "101 digits"),
    (11.0, 3.5, "Continue", "exact + Q335\nvalues", GREEN, "still exact"),
    (13.5, 3.5, "Final\nresult", "high-precision\nmpf", ORANGE, "50+ digits"),
    (16.0, 3.5, "Compare", "decimal string\nvs measured", MAG, "NOW decimal"),
]

for i, (sx, sy, slabel, sdesc, scol, snote) in enumerate(stages):
    rounded_box(ax, sx, sy, 2.0, 2.0, "", scol, alpha=0.15)
    ax.text(sx, sy + 0.5, slabel, ha='center', va='center', fontsize=9,
            color=WHITE, fontweight='bold')
    ax.text(sx, sy - 0.3, sdesc, ha='center', va='center', fontsize=7,
            color=SILVER)
    ax.text(sx, sy - 0.85, snote, ha='center', va='center', fontsize=7,
            color=scol, fontstyle='italic')

    # Arrow to next
    if i < len(stages) - 1:
        nx = stages[i+1][0]
        ax.annotate("", xy=(nx - 1.1, sy), xytext=(sx + 1.1, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

    # Red X between stages 1-5 (no float here)
    if i < 5:
        mid_x = sx + 1.25
        ax.text(mid_x, sy + 1.3, r"$\times$", ha='center', va='center',
                fontsize=10, color=RED, alpha=0.6)
        ax.text(mid_x, sy + 1.6, "no float", ha='center', va='center',
                fontsize=6, color=RED, alpha=0.5)

# Final annotation
ax.text(9, 0.5, "The decimal is the test. The fraction is the physics.",
        ha='center', va='center', fontsize=13, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk5_13_computation_pipeline.png")


# ================================================================
# FIG 14: WHERE EXACT STOPS AND APPROXIMATE BEGINS
# Type: Running/Convergence (threshold diagram)
# Shows: sharp boundary between pure math and measured input
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-1, 9)

ax.text(7, 8.3, "Where Exact Stops and Approximate Begins",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Exact zone (left)
exact_items = [
    (1.5, 6.5, r"$\beta_1$ = 41/10", GREEN),
    (1.5, 5.5, r"$\beta_2$ = $-$19/6", GREEN),
    (1.5, 4.5, r"$\beta_3$ = $-$7", GREEN),
    (4.0, 6.5, "gap = 38/27", GREEN),
    (4.0, 5.5, r"sin$^2\theta_W$(tree) = 3/8", GREEN),
]

for ex, ey, etxt, ecol in exact_items:
    rounded_box(ax, ex, ey, 2.5, 0.7, etxt, ecol, fontsize=8, alpha=0.15)

# Q335 zone (center-left)
q335_items = [
    (4.0, 4.5, r"$\pi$ (Q335)", GOLD),
    (4.0, 3.5, r"ln($M_{GUT}/M_Z$)", GOLD),
    (4.0, 2.5, r"$\zeta(3)$ in QED", GOLD),
]

for qx, qy, qtxt, qcol in q335_items:
    rounded_box(ax, qx, qy, 2.5, 0.7, qtxt, qcol, fontsize=8, alpha=0.15)

# THE BOUNDARY
ax.plot([6.5, 6.5], [1.5, 7.5], color=RED, linewidth=3, linestyle='--', alpha=0.7)
ax.text(6.5, 7.8, "THE BOUNDARY", ha='center', va='center', fontsize=11,
        color=RED, fontweight='bold')
ax.text(6.5, 1.0, "exact stops here", ha='center', va='center', fontsize=9,
        color=RED, fontstyle='italic')

# Measured zone (right)
meas_items = [
    (9.0, 6.5, r"$\alpha^{-1}$ = 137.036...", ORANGE),
    (9.0, 5.5, r"$M_Z$ = 91188 MeV", ORANGE),
    (9.0, 4.5, r"$\alpha_s$ = 0.118", ORANGE),
]

for mx, my, mtxt, mcol in meas_items:
    rounded_box(ax, mx, my, 2.5, 0.7, mtxt, mcol, fontsize=8, alpha=0.15)

# Derived approximate (far right)
derived_items = [
    (12.0, 6.5, r"sin$^2\theta_W$ = 0.23122", CYAN),
    (12.0, 5.5, r"$M_W$ = 80354 MeV", CYAN),
    (12.0, 4.5, "D/H = 2.531" + r"$\times 10^{-5}$", CYAN),
]

for dx, dy, dtxt, dcol in derived_items:
    rounded_box(ax, dx, dy, 2.8, 0.7, dtxt, dcol, fontsize=8, alpha=0.15)

# Zone labels
ax.text(2.75, 7.8, "INTEGERS\n(exact)", ha='center', va='center',
        fontsize=10, color=GREEN, fontweight='bold')
ax.text(10.5, 7.8, "MEASUREMENTS\n(approximate)", ha='center', va='center',
        fontsize=10, color=ORANGE, fontweight='bold')

# Arrows from measured to derived
for i in range(3):
    ax.annotate("", xy=(10.5, 6.5 - i), xytext=(10.3, 6.5 - i),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.3))

ax.text(7, -0.3, "Everything left of the line is integers. Everything right involves measurement.\n"
        "The line tells you exactly where uncertainty enters.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk5_14_exact_approximate_boundary.png")


# ================================================================
# FIG 15: TWO TYPES — EXACT FRACTION VS APPROXIMATE
# Type: Comparison Bar (side by side)
# Shows: two pool entries with different type labels
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Type System: Every Value Is Labeled",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: exact_fraction --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

card1 = mpatches.FancyBboxPatch((0.5, 1.5), 9.0, 7.0,
    boxstyle="round,pad=0.2", facecolor=PAN, alpha=0.4,
    linewidth=2)
ax1.add_patch(card1)
# Green border line on left
ax1.plot([0.5, 0.5], [1.5, 8.5], color=GREEN, linewidth=4, alpha=0.7)

ax1.text(5, 9.0, "exact_fraction", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GREEN)

fields = [
    ("key:", "beta_sm_su3_total_v0", WHITE),
    ("value:", r"$-$7/1", GOLD),
    ("value_type:", "exact_fraction", GREEN),
    ("level:", "1 (group theory)", CYAN),
    ("source:", "SU(3) representation theory", SILVER),
]
for i, (label, val, col) in enumerate(fields):
    y = 7.5 - i * 1.1
    ax1.text(1.5, y, label, ha='left', va='center', fontsize=10, color=SILVER)
    ax1.text(4.5, y, val, ha='left', va='center', fontsize=10, color=col,
             fontweight='bold')

ax1.text(5, 1.8, "This number is known exactly.\nIt comes from counting, not measuring.",
         ha='center', va='center', fontsize=9, color=GREEN, fontstyle='italic')

# -- Right: approximate --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

card2 = mpatches.FancyBboxPatch((0.5, 1.5), 9.0, 7.0,
    boxstyle="round,pad=0.2", facecolor=PAN, alpha=0.4,
    linewidth=2)
ax2.add_patch(card2)
# Orange border line on left
ax2.plot([0.5, 0.5], [1.5, 8.5], color=ORANGE, linewidth=4, alpha=0.7)

ax2.text(5, 9.0, "approximate", ha='center', va='center',
         fontsize=14, fontweight='bold', color=ORANGE)

fields2 = [
    ("key:", "astro_gravitational_constant_v0", WHITE),
    ("value:", "0.00000000006674", ORANGE),
    ("value_type:", "approximate", ORANGE),
    ("level:", "2 (measured)", CYAN),
    ("source:", "CODATA 2022, 4 digits", SILVER),
]
for i, (label, val, col) in enumerate(fields2):
    y = 7.5 - i * 1.1
    ax2.text(1.5, y, label, ha='left', va='center', fontsize=10, color=SILVER)
    ax2.text(4.5, y, val, ha='left', va='center', fontsize=10, color=col,
             fontweight='bold')

ax2.text(5, 1.8, "This number is measured.\nIts precision is limited by the experiment.",
         ha='center', va='center', fontsize=9, color=ORANGE, fontstyle='italic')

save(fig, "talk5_15_type_system.png")


# ================================================================
# FIG 16: HADRONIC VP DELTA — EXACT CONTAINER, UNCERTAIN CONTENT
# Type: Identity Card
# Shows: subtle distinction between container precision and physics precision
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "Exact Fraction " + r"$\neq$" + " Exact Value",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)
ax.text(5, 8.6, "A Subtle Distinction", ha='center', va='center',
        fontsize=12, color=SILVER)

# Pool entry card
card = mpatches.FancyBboxPatch((0.5, 4.5), 9.0, 3.0,
    boxstyle="round,pad=0.2", facecolor=PAN, alpha=0.4,
    linewidth=2)
ax.add_patch(card)

ax.text(1.5, 7.0, "key:", ha='left', va='center', fontsize=10, color=SILVER)
ax.text(3.5, 7.0, "qed_hadronic_vp_delta_v0", ha='left', va='center',
        fontsize=10, color=WHITE, fontweight='bold')
ax.text(1.5, 6.2, "value:", ha='left', va='center', fontsize=10, color=SILVER)
ax.text(3.5, 6.2, "220393/50000", ha='left', va='center',
        fontsize=10, color=GOLD, fontweight='bold')
ax.text(1.5, 5.4, "type:", ha='left', va='center', fontsize=10, color=SILVER)
ax.text(3.5, 5.4, "exact_fraction", ha='left', va='center',
        fontsize=10, color=GREEN, fontweight='bold')
ax.text(6.5, 5.4, "uncertainty: " + r"$\pm$0.010", ha='left', va='center',
        fontsize=10, color=ORANGE, fontweight='bold')

# Three annotation layers
annotations = [
    (5, 3.5, "The Fraction 220393/50000 is exact.\nIt is exactly this ratio of two integers. No rounding.", GREEN),
    (5, 2.2, "The physics value it represents has uncertainty " + r"$\pm$" + "0.010.\nThe measurement could have been slightly different.", ORANGE),
    (5, 0.8, "The container (Fraction) is exact.\nThe content (physical value) carries uncertainty.\nBoth facts are recorded.", GOLD),
]

for atx, aty, atxt, acol in annotations:
    ax.text(atx, aty, atxt, ha='center', va='center', fontsize=9,
            color=acol,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(5, -0.5, "Most systems store 4.40786 and you can't tell if it's exact or rounded.\nThis system always tells you.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic')

save(fig, "talk5_16_exact_container_uncertain_content.png")


# ================================================================
# FIG 17: THE 38/27 REVELATION — DEAD VS ALIVE
# Type: Comparison Bar (two panels)
# Shows: barren decimal vs rich fraction with physics meanings
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Same Number: Dead vs Alive",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Decimal (dead) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 8.5, "Decimal", ha='center', va='center',
         fontsize=14, fontweight='bold', color=DIM)
ax1.text(5, 6.5, "1.40741...", ha='center', va='center',
         fontsize=36, fontweight='bold', color=DIM)
ax1.text(5, 4.5, "A location on the\nnumber line.", ha='center', va='center',
         fontsize=12, color=DIM)
ax1.text(5, 3.0, "Connects to nothing.\nFactors into nothing.\nCounts nothing.",
         ha='center', va='center', fontsize=11, color=DIM, fontstyle='italic')
ax1.text(5, 1.5, "Dead data.", ha='center', va='center',
         fontsize=14, color=DIM, fontweight='bold')

# -- Right: Fraction (alive) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 8.5, "Fraction", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GOLD)
ax2.text(5, 6.5, "38 / 27", ha='center', va='center',
         fontsize=36, fontweight='bold', color=GOLD)

# Factorizations with meanings
ax2.text(3.0, 5.0, "38 = 2 " + r"$\times$" + " 19", ha='center', va='center',
         fontsize=13, color=CYAN, fontweight='bold')
ax2.text(7.0, 5.0, "27 = 3" + r"$^3$", ha='center', va='center',
         fontsize=13, color=CYAN, fontweight='bold')

# Meaning arrows
ax2.text(2.0, 4.0, "2 = vector-like\n(both hands)", ha='center', va='center',
         fontsize=9, color=GREEN)
ax2.text(4.0, 4.0, "19 = weak\nforce count", ha='center', va='center',
         fontsize=9, color=GREEN)
ax2.text(7.0, 4.0, "3" + r"$^3$" + " = color\ncharges cubed", ha='center', va='center',
         fontsize=9, color=GREEN)

ax2.text(5, 2.5, "Every integer has a name.\nEvery factor counts something physical.",
         ha='center', va='center', fontsize=11, color=WHITE, fontstyle='italic')
ax2.text(5, 1.5, "Alive with physics.", ha='center', va='center',
         fontsize=14, color=GOLD, fontweight='bold')

save(fig, "talk5_17_dead_vs_alive.png")


# ================================================================
# FIG 18: THREE REVELATIONS
# Type: Progression/Sequence (three panels)
# Shows: three independent examples of fraction > decimal
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 10),
                          gridspec_kw={'wspace': 0.20})
fig.patch.set_facecolor(BG)
fig.suptitle("Three Things Only Fractions Can See",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

panels = [
    ("Gap Ratio",
     "1.40741...", "38/27 = (2" + r"$\times$" + "19)/3" + r"$^3$",
     "Unification structure.\n19 = weak force.\n3" + r"$^3$" + " = color cubed.",
     DIM, GOLD),
    ("QED " + r"$A_2$",
     r"$-$0.3285...", "197/144 + (1/12)" + r"$\pi^2$" + "\n" + r"$-$ (1/2)$\pi^2$ln 2" + "\n+ (3/4)" + r"$\zeta(3)$",
     "Four pieces.\n87% cancellation.\nThe structure IS\nthe physics.",
     DIM, CYAN),
    ("Beta coefficients",
     "4.1, " + r"$-$3.17, $-$7.0", "41/10, " + r"$-$19/6, $-$7/1",
     "41 counts charges.\n19 counts weak.\n7 = 11 gluons " + r"$-$" + " 4 quarks.",
     DIM, GREEN),
]

for idx, (title, dec_txt, frac_txt, note, dcol, fcol) in enumerate(panels):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.2, title, ha='center', va='center', fontsize=13,
            fontweight='bold', color=WHITE)

    # Decimal (dim)
    ax.text(5, 7.5, "Decimal:", ha='center', va='center', fontsize=9, color=DIM)
    ax.text(5, 6.7, dec_txt, ha='center', va='center', fontsize=11,
            color=DIM, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

    # Arrow down
    ax.annotate("", xy=(5, 5.6), xytext=(5, 6.1),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
    ax.text(6.5, 5.85, "same\nnumber", ha='center', va='center',
            fontsize=7, color=DIM)

    # Fraction (colored)
    ax.text(5, 5.2, "Fraction:", ha='center', va='center', fontsize=9, color=fcol)
    ax.text(5, 4.2, frac_txt, ha='center', va='center', fontsize=10,
            color=fcol, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

    # Note
    ax.text(5, 2.2, note, ha='center', va='center', fontsize=9,
            color=SILVER, fontstyle='italic')

fig.text(0.5, 0.04, "The number system isn't neutral. It's a lens. Decimals blur. Fractions resolve.",
         ha='center', va='center', fontsize=12, color=SILVER, fontstyle='italic')

save(fig, "talk5_18_three_revelations.png")


# ================================================================
# FIG 19: THE GRANDMOTHER'S PRINCIPLE — APPLIED TO PHYSICS
# Type: Geometric Cross-Section (split screen)
# Shows: bread division parallels physics derivation
# ================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10),
                                gridspec_kw={'hspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Every Crumb Is Bread",
             fontsize=17, fontweight='bold', color=GOLD, y=0.97)

# -- Top: Bread --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 14)
ax1.set_ylim(0, 4)

ax1.text(0.5, 3.3, "Bread", ha='left', va='center', fontsize=12,
         color=ORANGE, fontweight='bold')

# Loaf slices
for i in range(10):
    x = 1.5 + i * 1.0
    col = GREEN if i < 9 else GOLD
    rect = mpatches.FancyBboxPatch((x, 1.2), 0.7, 1.2,
        boxstyle="round,pad=0.05", facecolor=col, alpha=0.3, linewidth=1)
    ax1.add_patch(rect)

ax1.text(12.5, 1.8, "10 slices\n9 mouths\n1 saved\n0 waste", ha='center', va='center',
         fontsize=9, color=GREEN)
ax1.text(7, 0.5, "She counts in integers. Zero waste. Everyone fed.", ha='center',
         va='center', fontsize=10, color=GREEN, fontstyle='italic')

# -- Bottom: Physics --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 14)
ax2.set_ylim(0, 4)

ax2.text(0.5, 3.3, "Physics", ha='left', va='center', fontsize=12,
         color=GOLD, fontweight='bold')

# Pipeline boxes
pipeline = [
    (2.0, 1.8, "41/10", GOLD),
    (5.0, 1.8, "38/27", CYAN),
    (8.0, 1.8, "0.231223...", GREEN),
    (11.0, 1.8, "PASS\n12 ppm", GREEN),
]

for px, py, ptxt, pcol in pipeline:
    rounded_box(ax2, px, py, 2.2, 1.2, ptxt, pcol, fontsize=10, alpha=0.15)

for i in range(len(pipeline) - 1):
    ax2.annotate("", xy=(pipeline[i+1][0] - 1.2, 1.8),
                xytext=(pipeline[i][0] + 1.2, 1.8),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax2.text(7, 0.5, "The model counts in integers. Zero arithmetic loss. Every prediction matches.",
         ha='center', va='center', fontsize=10, color=GOLD, fontstyle='italic')

# Connecting principle
fig.text(0.5, 0.47, "Same principle: don't throw away the remainder.\nThe remainder is the piece someone needs.",
         ha='center', va='center', fontsize=11, color=WHITE,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk5_19_grandmother_principle.png")


# ================================================================
# FIG 20: SUMMARY CARD — ONE INNOVATION, 253 PASSES
# Type: Identity Card
# Shows: complete methodology in one reference frame
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.3, "One Engineering Innovation, 253 Passing Comparisons",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Card border
card = mpatches.FancyBboxPatch((0.3, 0.5), 9.4, 8.0,
    boxstyle="round,pad=0.3", facecolor=PAN, alpha=0.4,
    linewidth=2)
ax.add_patch(card)

rows = [
    ("Innovation:", "Don't convert integers to decimals until the last step.", GOLD),
    ("Transcendentals:", "Q335, 101 digits, 65 beyond Planck.", CYAN),
    ("Type system:", "exact_fraction vs approximate, tracked through every step.", GREEN),
    ("PSLQ:", "82/82 null. No shortcuts. Derive and store.", SILVER),
    ("Pipeline:", "Fraction " + r"$\rightarrow$" + " Fraction " + r"$\rightarrow$" +
     " Q335 " + r"$\rightarrow$" + " ... " + r"$\rightarrow$" + " decimal (compare only).", BLUE),
    ("Result:", "253 comparisons. 13 inputs. 53 outputs. 9 domains.", GOLD),
]

for i, (label, val, col) in enumerate(rows):
    y = 7.8 - i * 1.0
    ax.text(1.0, y, label, ha='left', va='center', fontsize=10, color=SILVER)
    ax.text(3.5, y, val, ha='left', va='center', fontsize=10, color=col,
            fontweight='bold')

# Center quote
ax.text(5, 1.5, "The decimal is the test.\nThe fraction is the physics.",
        ha='center', va='center', fontsize=16, color=GOLD, fontweight='bold',
        linespacing=1.8)

ax.text(5, 0.4, "The grandmother knew. Every crumb is bread.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk5_20_summary_card.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 5, 11-20) generated ===")
filenames = [
    "talk5_11_pslq_82_null.png",
    "talk5_12_derivation_vs_search.png",
    "talk5_13_computation_pipeline.png",
    "talk5_14_exact_approximate_boundary.png",
    "talk5_15_type_system.png",
    "talk5_16_exact_container_uncertain_content.png",
    "talk5_17_dead_vs_alive.png",
    "talk5_18_three_revelations.png",
    "talk5_19_grandmother_principle.png",
    "talk5_20_summary_card.png",
]
for f in filenames:
    print("  %s" % f)
    