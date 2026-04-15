#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 5, Slides 1-10
10 figures covering: fraction vs float objects, error propagation,
grandmother's division, bread-to-physics parallel, gap ratio step by step,
same computation in float, QED A2 anatomy, 87% cancellation,
Q335 spec card, Planck wall.
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
# FIG 1: FRACTION VS FLOAT — TWO OBJECTS, SAME NUMBER
# Type: Comparison Bar (side by side panels)
# Shows: recoverable structure vs irrecoverable location
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Same Number as Two Different Objects",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Fraction (alive) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.2, "Fraction", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GREEN)

ax1.text(5, 7.5, "41 / 10", ha='center', va='center',
         fontsize=36, fontweight='bold', color=GOLD)

# Numerator box
rounded_box(ax1, 3.0, 5.5, 3.0, 1.2, "Numerator: 41", GOLD, fontsize=12, alpha=0.2)
ax1.text(3.0, 4.5, "41 = sum of all particle\ncharge contributions", ha='center',
         va='center', fontsize=9, color=GREEN)

# Denominator box
rounded_box(ax1, 7.0, 5.5, 3.0, 1.2, "Denominator: 10", CYAN, fontsize=12, alpha=0.2)
ax1.text(7.0, 4.5, "10 = 2" + r"$\times$" + "5 from GUT\nnormalization " + r"$k_1$" + " = 3/5",
         ha='center', va='center', fontsize=9, color=GREEN)

ax1.text(5, 3.0, "Both recoverable.\nBoth meaningful.\nBoth carry physics.",
         ha='center', va='center', fontsize=11, color=WHITE, fontstyle='italic')

ax1.text(5, 1.5, "The Fraction remembers\nwhat it's made of.",
         ha='center', va='center', fontsize=10, color=GREEN,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

# -- Right: Float (dead) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.2, "Float", ha='center', va='center',
         fontsize=14, fontweight='bold', color=DIM)

ax2.text(5, 7.5, "4.100000000", ha='center', va='center',
         fontsize=30, fontweight='bold', color=DIM)

# Empty boxes
rounded_box(ax2, 3.0, 5.5, 3.0, 1.2, "Numerator: ???", DIM, fontsize=12, alpha=0.1)
ax2.text(3.0, 4.5, "Not recoverable.\nNot stored.", ha='center',
         va='center', fontsize=9, color=DIM)

rounded_box(ax2, 7.0, 5.5, 3.0, 1.2, "Denominator: ???", DIM, fontsize=12, alpha=0.1)
ax2.text(7.0, 4.5, "The 41 is gone.\nThe 10 is gone.", ha='center',
         va='center', fontsize=9, color=DIM)

ax2.text(5, 3.0, "Not recoverable.\nNot meaningful.\nJust a location on\nthe number line.",
         ha='center', va='center', fontsize=11, color=DIM, fontstyle='italic')

ax2.text(5, 1.5, "The float remembers where.\nNot what.",
         ha='center', va='center', fontsize=10, color=DIM,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk5_01_fraction_vs_float.png")


# ================================================================
# FIG 2: ERROR PROPAGATION — FLOAT GROWS, FRACTION STAYS ZERO
# Type: Running/Convergence
# Shows: diverging curves — one rises, one stays flat at zero
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

steps = np.arange(0, 101)

# Float error: starts at machine epsilon, grows sqrt(N) roughly
float_err = 1e-16 * np.sqrt(1 + steps * 2.0)

# Fraction error: zero everywhere
frac_err = np.ones_like(steps) * 1e-20  # plot floor for log scale

ax.semilogy(steps, float_err, color=RED, linewidth=2.5, label='Float64 accumulated error')
ax.semilogy(steps, frac_err, color=GOLD, linewidth=2.5, linestyle='-', label='Fraction error (zero)')

# Fill between to show growing gap
ax.fill_between(steps, frac_err, float_err, color=RED, alpha=0.05)

# Annotations
ax.annotate("Gap grows with\nevery computation step",
            xy=(60, float_err[60]), xytext=(75, 1e-13),
            fontsize=10, color=SILVER, ha='center',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(50, 3e-21, "Fraction: exact at every step. Zero at step 1. Zero at step 100.",
        ha='center', va='center', fontsize=10, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

# Machine epsilon line
ax.axhline(y=1e-16, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(5, 1.5e-16, "machine epsilon " + r"($10^{-16}$)", ha='left', va='bottom',
        fontsize=8, color=DIM)

ax.set_xlabel("Number of computation steps", fontsize=11, color=SILVER)
ax.set_ylabel("Accumulated error", fontsize=11, color=SILVER)
ax.set_title("Float Error Grows. Fraction Error Stays Zero.",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.legend(loc='upper left', fontsize=10, facecolor=PAN, labelcolor=WHITE)

ax.text(50, 5e-12, "Short computation: negligible difference.\n"
        "QED five-loop chain: the difference is the result.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 100)
ax.set_ylim(1e-21, 1e-11)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk5_02_error_propagation.png")


# ================================================================
# FIG 3: THE GRANDMOTHER'S DIVISION
# Type: Geometric Cross-Section (two panels)
# Shows: integer division (everyone fed) vs decimal division (waste)
# ================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 10),
                                gridspec_kw={'hspace': 0.35})
fig.patch.set_facecolor(BG)
fig.suptitle("The Grandmother vs The Accountant",
             fontsize=17, fontweight='bold', color=GOLD, y=0.97)

# -- Top: Grandmother (integer division) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 16)
ax1.set_ylim(0, 5)

ax1.text(0.5, 4.3, "Grandmother", ha='left', va='center',
         fontsize=13, fontweight='bold', color=GREEN)

# 10 slices
for i in range(10):
    x = 1.0 + i * 1.2
    col = GREEN if i < 9 else GOLD
    rect = mpatches.FancyBboxPatch((x, 2.0), 0.9, 1.5,
        boxstyle="round,pad=0.05", facecolor=col, alpha=0.3, linewidth=1)
    ax1.add_patch(rect)
    if i < 9:
        ax1.text(x + 0.45, 1.5, "mouth\n%d" % (i+1), ha='center', va='center',
                 fontsize=6, color=SILVER)
    else:
        ax1.text(x + 0.45, 1.5, "saved", ha='center', va='center',
                 fontsize=6, color=GOLD)

ax1.text(14.5, 2.75, "10 slices\n9 mouths\n1 saved\n0 waste", ha='center', va='center',
         fontsize=10, color=GREEN, fontweight='bold')
ax1.text(8, 0.6, "Integer division. Everyone fed. Nothing wasted.", ha='center',
         va='center', fontsize=10, color=GREEN, fontstyle='italic')

# -- Bottom: Accountant (decimal division) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 16)
ax2.set_ylim(0, 5)

ax2.text(0.5, 4.3, "Accountant", ha='left', va='center',
         fontsize=13, fontweight='bold', color=RED)

# 9 slices + remainder crumbs
for i in range(9):
    x = 1.0 + i * 1.2
    rect = mpatches.FancyBboxPatch((x, 2.0), 0.9, 1.5,
        boxstyle="round,pad=0.05", facecolor=DIM, alpha=0.2, linewidth=1)
    ax2.add_patch(rect)
    ax2.text(x + 0.45, 2.75, "1.111...", ha='center', va='center',
             fontsize=7, color=DIM)

# Remainder falling
ax2.text(12.5, 3.5, "0.111...", ha='center', va='center',
         fontsize=12, color=RED, fontweight='bold')
ax2.annotate("", xy=(12.5, 1.5), xytext=(12.5, 3.0),
             arrowprops=dict(arrowstyle='->', color=RED, lw=2))
ax2.text(12.5, 1.2, "waste bin", ha='center', va='center',
         fontsize=8, color=RED)

ax2.text(14.5, 2.75, "10/9 each\n= 1.111...\nremainder:\n0.111...", ha='center', va='center',
         fontsize=10, color=RED, fontweight='bold')
ax2.text(8, 0.6, "Decimal division. Who bears the remainder? The decimal creates\n"
         "a problem that doesn't exist in the bread.", ha='center',
         va='center', fontsize=10, color=RED, fontstyle='italic')

save(fig, "talk5_03_grandmother_division.png")


# ================================================================
# FIG 4: BREAD TO PHYSICS — THE PARALLEL
# Type: Connection/Integer Map (two parallel rows)
# Shows: same error in bread and physics, same fix
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-1, 9)

ax.text(7, 8.3, "Same Error, Different Domain",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Row 1: Bread
ax.text(0.5, 6.8, "BREAD", ha='left', va='center', fontsize=12,
        color=ORANGE, fontweight='bold')

rounded_box(ax, 2.5, 5.5, 2.5, 1.2, "10 slices", ORANGE, fontsize=10, alpha=0.15)
ax.annotate("", xy=(4.5, 5.5), xytext=(3.8, 5.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

rounded_box(ax, 5.5, 5.5, 2.0, 1.2, r"$\div$ 9", ORANGE, fontsize=10, alpha=0.15)

# Fork to two paths
ax.plot([6.5, 7.5], [5.9, 6.5], color=GREEN, linewidth=1.5, alpha=0.5)
ax.plot([6.5, 7.5], [5.1, 4.5], color=RED, linewidth=1.5, alpha=0.5)

rounded_box(ax, 9.5, 6.5, 3.5, 0.9, "1 each + 1 saved = exact", GREEN, fontsize=9, alpha=0.15)
rounded_box(ax, 9.5, 4.5, 3.5, 0.9, "1.111... + waste", RED, fontsize=9, alpha=0.1,
            textcolor=RED)

# Row 2: Physics
ax.text(0.5, 3.2, "PHYSICS", ha='left', va='center', fontsize=12,
        color=CYAN, fontweight='bold')

rounded_box(ax, 2.5, 2.0, 2.5, 1.2, "41 charges", CYAN, fontsize=10, alpha=0.15)
ax.annotate("", xy=(4.5, 2.0), xytext=(3.8, 2.0),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

rounded_box(ax, 5.5, 2.0, 2.0, 1.2, r"$\div$ 10", CYAN, fontsize=10, alpha=0.15)

ax.plot([6.5, 7.5], [2.4, 3.0], color=GREEN, linewidth=1.5, alpha=0.5)
ax.plot([6.5, 7.5], [1.6, 1.0], color=RED, linewidth=1.5, alpha=0.5)

rounded_box(ax, 9.5, 3.0, 3.5, 0.9, "41/10: structure visible", GREEN, fontsize=9, alpha=0.15)
rounded_box(ax, 9.5, 1.0, 3.5, 0.9, "4.1: structure invisible", RED, fontsize=9, alpha=0.1,
            textcolor=RED)

# Central connection
ax.text(12.5, 3.75, "Same\nerror.", ha='center', va='center', fontsize=12,
        color=GOLD, fontweight='bold')
ax.text(12.5, 2.75, "Same\nfix.", ha='center', va='center', fontsize=12,
        color=GOLD, fontweight='bold')

ax.text(7, -0.3, "The loss isn't real. It's an artifact of the number system.\n"
        "Physics does it every time it converts 41/10 to 4.1.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk5_04_bread_to_physics.png")


# ================================================================
# FIG 5: GAP RATIO — STEP BY STEP IN FRACTIONS
# Type: Progression/Sequence
# Shows: every step exact, structure visible at the end
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1, 8)

ax.text(8, 7.3, "Computing the Gap Ratio: Every Step Exact",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

steps = [
    (1.5, 4.5, r"$\alpha_1^{-1} - \alpha_3^{-1}$" + "\n= numerator",
     "exact Fraction", CYAN),
    (5.0, 4.5, r"$\alpha_2^{-1} - \alpha_3^{-1}$" + "\n= denominator",
     "exact Fraction", GREEN),
    (8.5, 4.5, "ratio =\nnum / den",
     "exact Fraction", BLUE),
    (11.5, 4.5, "SM: 218/115\n218=2" + r"$\times$" + "109\n115=5" + r"$\times$" + "23",
     "large primes", DIM),
    (14.5, 4.5, "CD: 38/27\n38=2" + r"$\times$" + "19\n27=3" + r"$^3$",
     "structure!", GOLD),
]

for i, (sx, sy, slabel, snote, scol) in enumerate(steps):
    rounded_box(ax, sx, sy, 2.5, 2.5, "", scol, alpha=0.15)
    ax.text(sx, sy + 0.3, slabel, ha='center', va='center', fontsize=9,
            color=WHITE, fontweight='bold')
    ax.text(sx, sy - 0.9, snote, ha='center', va='center', fontsize=8,
            color=scol, fontstyle='italic')

    # "still a Fraction" badge
    if i < 3:
        ax.text(sx, sy + 1.5, "still a Fraction", ha='center', va='center',
                fontsize=7, color=GREEN,
                bbox=dict(boxstyle='round,pad=0.15', facecolor=BG))

    # Arrow to next
    if i < len(steps) - 1:
        nx = steps[i+1][0]
        ax.annotate("", xy=(nx - 1.4, sy), xytext=(sx + 1.4, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Highlight CD result
ax.text(14.5, 2.2, "19 = weak force count\n3" + r"$^3$" + " = color cubed\nStructure!",
        ha='center', va='center', fontsize=9, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(8, 0.3, "Every step is an exact Fraction. The structure at step 5 was present at step 1.\n"
        "Decimals would have destroyed it at step 1.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk5_05_gap_ratio_fractions.png")


# ================================================================
# FIG 6: SAME COMPUTATION IN FLOAT — STRUCTURE LOST
# Type: Progression/Sequence
# Shows: same layout as V5 but all DIM — information is gone
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1, 8)

ax.text(8, 7.3, "Same Computation in Float: Structure Invisible",
        ha='center', va='center', fontsize=16, fontweight='bold', color=DIM)

steps_f = [
    (1.5, 4.5, "59.01... " + r"$-$" + " 8.47...\n= 50.54...", "just a float", DIM),
    (5.0, 4.5, "29.57... " + r"$-$" + " 8.47...\n= 21.10...", "just a float", DIM),
    (8.5, 4.5, "50.54... / 21.10...\n= 2.3957...", "just a float", DIM),
    (11.5, 4.5, "SM: 1.8957...\n\nIs this 218/115?\nCan't tell.", "just a decimal", DIM),
    (14.5, 4.5, "CD: 1.4074...\n\nIs this 38/27?\nCan't tell.", "just a decimal", DIM),
]

for i, (sx, sy, slabel, snote, scol) in enumerate(steps_f):
    rounded_box(ax, sx, sy, 2.5, 2.5, "", scol, alpha=0.08)
    ax.text(sx, sy + 0.3, slabel, ha='center', va='center', fontsize=9,
            color=DIM)
    ax.text(sx, sy - 0.9, snote, ha='center', va='center', fontsize=8,
            color=RED, fontstyle='italic')

    # "just a float" badge
    if i < 3:
        ax.text(sx, sy + 1.5, "just a float", ha='center', va='center',
                fontsize=7, color=RED,
                bbox=dict(boxstyle='round,pad=0.15', facecolor=BG))

    if i < len(steps_f) - 1:
        nx = steps_f[i+1][0]
        ax.annotate("", xy=(nx - 1.4, sy), xytext=(sx + 1.4, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.3))

ax.text(8, 0.3, "Same data. Same computation. Same result numerically.\n"
        "But 38 = 2" + r"$\times$" + "19, 27 = 3" + r"$^3$" +
        " is invisible. You can't find what you can't see.",
        ha='center', va='center', fontsize=10, color=DIM, fontstyle='italic')

save(fig, "talk5_06_gap_ratio_floats.png")


# ================================================================
# FIG 7: QED A2 COEFFICIENT — ANATOMY OF EXACTNESS
# Type: Connection/Integer Map
# Shows: four pieces assembling into one coefficient, all exact
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 11)

ax.text(7, 10.3, "One QED Coefficient, Four Pieces, All Exact",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Central A2 box
rounded_box(ax, 7, 7.5, 3.5, 1.5, r"$A_2$ = $-$0.3285...", WHITE, fontsize=14, alpha=0.2)

# Four branches
branches = [
    (1.5, 4.5, "197/144", "Pure rational.\nExact forever.", GOLD, "+1.368"),
    (5.0, 4.5, r"(1/12)$\pi^2$", "Rational " + r"$\times$" + r" $\pi$." + "\n" + r"$\pi$" + " in Q335.", CYAN, "+0.822"),
    (9.0, 4.5, r"$-(1/2)\pi^2$ln 2", "Rational " + r"$\times$" + " two\ntranscendentals.\nBoth in Q335.", GREEN, r"$-$3.410"),
    (12.5, 4.5, r"(3/4)$\zeta$(3)", "Rational " + r"$\times$" + r" $\zeta$(3)." + "\n" + r"$\zeta$(3) in Q335.", BLUE, "+0.901"),
]

for bx, by, blabel, bdesc, bcol, bval in branches:
    rounded_box(ax, bx, by, 2.5, 2.0, "", bcol, alpha=0.15)
    ax.text(bx, by + 0.5, blabel, ha='center', va='center', fontsize=11,
            color=WHITE, fontweight='bold')
    ax.text(bx, by - 0.2, bdesc, ha='center', va='center', fontsize=7,
            color=SILVER)
    ax.text(bx, by - 0.8, bval, ha='center', va='center', fontsize=9,
            color=bcol, fontweight='bold')

    # Arrow up to A2
    ax.annotate("", xy=(7, 6.7), xytext=(bx, by + 1.1),
                arrowprops=dict(arrowstyle='->', color=bcol, lw=1.5, alpha=0.4))

ax.text(7, 2.0, "In Fraction arithmetic: rational pieces (197/144, 1/12, 1/2, 3/4)\n"
        "are exact at every step. Transcendentals exact to 100 digits.\n"
        "In float arithmetic: everything is approximate from the start.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN))

save(fig, "talk5_07_a2_anatomy.png")


# ================================================================
# FIG 8: THE 87% CANCELLATION
# Type: Comparison Bar (stacked positive/negative)
# Shows: huge pieces nearly cancel, tiny residual IS the physics
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Positive contributions
pos_vals = [1.368, 0.822, 0.901]
pos_labels = ["197/144\n= +1.368", r"(1/12)$\pi^2$" + "\n= +0.822", r"(3/4)$\zeta$(3)" + "\n= +0.901"]
pos_colors = [GOLD, CYAN, BLUE]

# Negative contribution
neg_val = -3.410
neg_label = r"$-(1/2)\pi^2$ln 2" + "\n= " + r"$-$3.410"

# Plot positive stacked
bottom = 0
for i in range(len(pos_vals)):
    ax.bar(0, pos_vals[i], bottom=bottom, width=0.5, color=pos_colors[i], alpha=0.6)
    ax.text(0.4, bottom + pos_vals[i]/2, pos_labels[i], ha='left', va='center',
            fontsize=9, color=pos_colors[i])
    bottom += pos_vals[i]

# Total positive line
ax.axhline(y=bottom, color=SILVER, linewidth=1, linestyle=':', alpha=0.4)
ax.text(0.4, bottom + 0.05, "Total positive: +%.3f" % bottom, ha='left',
        va='bottom', fontsize=9, color=SILVER)

# Negative bar
ax.bar(1.5, abs(neg_val), bottom=0, width=0.5, color=RED, alpha=0.6)
ax.text(1.9, abs(neg_val)/2, neg_label, ha='left', va='center',
        fontsize=9, color=RED)
ax.axhline(y=abs(neg_val), color=SILVER, linewidth=1, linestyle=':', alpha=0.4)
ax.text(1.9, abs(neg_val) + 0.05, "Total negative: " + r"$-$" + "%.3f" % abs(neg_val),
        ha='left', va='bottom', fontsize=9, color=SILVER)

# Net result
net = bottom + neg_val  # positive + negative
ax.bar(3.0, abs(net), bottom=0, width=0.5, color=GREEN, alpha=0.7)
ax.text(3.4, abs(net)/2, r"$A_2$ = $-$0.329" + "\n(tiny residual)", ha='left',
        va='center', fontsize=10, color=GREEN, fontweight='bold')

# Cancellation annotation
cancel_pct = 100 * (1 - abs(net) / bottom)
ax.text(1.5, 3.8, "%.0f%% cancellation" % cancel_pct, ha='center', va='center',
        fontsize=14, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.text(2.9, 2.7, "In float: you see " + r"$-$" + "0.329 and nothing else.\n"
        "In fractions: you see four exact pieces that nearly cancel.\n"
        "The near-cancellation IS the physics.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xticks([0, 1.5, 3.0])
ax.set_xticklabels(["Positive\npieces", "Negative\npiece", "Net\nresult"],
                   fontsize=10, color=WHITE)
ax.set_ylabel("Magnitude", fontsize=11, color=SILVER)
ax.set_title("87% Cancellation: The Structure Decimals Hide",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(0, 4.0)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk5_08_cancellation_87pct.png")


# ================================================================
# FIG 9: Q335 — THE SPECIFICATION CARD
# Type: Identity Card
# Shows: all specs of the Q335 system in one visual reference
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 12)

ax.text(5, 11.2, "Q335: The Number Format",
        ha='center', va='center', fontsize=20, fontweight='bold', color=GOLD)

# Card border
card = mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 10.0,
    boxstyle="round,pad=0.3", facecolor=PAN, alpha=0.4, linewidth=2)
ax.add_patch(card)

specs = [
    ("Name", "Q335", GOLD),
    ("Format", r"integer / $2^{335}$", CYAN),
    ("Decimal precision", "101 digits", GREEN),
    ("Binary precision", "335 bits", GREEN),
    ("Planck threshold", "35 digits (nothing smaller exists)", SILVER),
    ("Excess beyond Planck", "65 digits of free insurance", GOLD),
    ("Division method", "bit shift (free in hardware)", CYAN),
    ("Storage", "one 101-digit integer per constant", SILVER),
    ("Constants stored", "31 total: " + r"$\pi$, $\zeta$(3-9), ln 2-5," + "\n"
     + r"$\sqrt{2-7}$, Catalan, $e$, $e^\pi$, $\phi$," + "\n"
     + r"Li$_4$-Li$_7$(1/2), elliptic $K$, $E$, $\pi^2$, $2\pi$, $R_2$, $R_4$", SILVER),
    ("Verified", "31 constants, all 100+ digits vs mpmath", GREEN),
    ("Innovation", "Engineering, not physics. " + r"$\pi$" + " is still transcendental.", GOLD),
]

for i, (label, value, col) in enumerate(specs):
    y = 9.8 - i * 0.82
    ax.text(1.0, y, label + ":", ha='left', va='center', fontsize=10,
            color=SILVER)
    ax.text(4.5, y, value, ha='left', va='center', fontsize=10,
            color=col, fontweight='bold')

save(fig, "talk5_09_q335_spec.png")


# ================================================================
# FIG 10: THE PLANCK WALL — 65 DIGITS PAST IT
# Type: Scale/Landscape
# Shows: segmented precision bar with wall at digit 35
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Segmented bar
segments = [
    (0, 15, RED, "Float64\n(calculator)", 0.5),
    (15, 35, ORANGE, "Best experiments\never built", 0.5),
    (35, 101, GOLD, "Q335 " + r"$\pi$" + "\n(what we use)", 0.7),
]

for x0, x1, col, label, al in segments:
    ax.barh(0, x1 - x0, left=x0, height=0.5, color=col, alpha=al)
    mid = (x0 + x1) / 2
    ax.text(mid, 0, label, ha='center', va='center',
            fontsize=9, color=WHITE, fontweight='bold')

# Planck wall
ax.axvline(x=35, color=RED, linewidth=4, alpha=0.8)
ax.text(35, 0.55, "THE PLANCK WALL", ha='center', va='bottom',
        fontsize=13, fontweight='bold', color=RED)
ax.text(35, 0.45, r"$10^{-35}$ meters", ha='center', va='bottom',
        fontsize=9, color=RED)
ax.text(35, -0.45, "The pixel size of reality.\nNothing smaller exists.", ha='center',
        va='top', fontsize=9, color=RED, fontstyle='italic')

# Overshoot arrow
ax.annotate("", xy=(101, -0.15), xytext=(35, -0.15),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(68, -0.28, "65 digits beyond the wall", ha='center', va='top',
        fontsize=12, color=GOLD, fontweight='bold')

ax.text(68, 0.7, "This entire golden region is free precision.\n"
        "No experiment theoretically possible could\ndetect the difference from true " + r"$\pi$.",
        ha='center', va='bottom', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_title("65 Digits Beyond the Smallest Thing",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.set_xlabel("Number of correct digits", fontsize=11, color=SILVER)
ax.set_xticks([0, 15, 25, 35, 50, 75, 101])
ax.set_yticks([])
ax.set_xlim(-3, 110)
ax.set_ylim(-0.7, 1.0)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk5_10_planck_wall.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 5, 1-10) generated ===")
filenames = [
    "talk5_01_fraction_vs_float.png",
    "talk5_02_error_propagation.png",
    "talk5_03_grandmother_division.png",
    "talk5_04_bread_to_physics.png",
    "talk5_05_gap_ratio_fractions.png",
    "talk5_06_gap_ratio_floats.png",
    "talk5_07_a2_anatomy.png",
    "talk5_08_cancellation_87pct.png",
    "talk5_09_q335_spec.png",
    "talk5_10_planck_wall.png",
]
for f in filenames:
    print("  %s" % f)
