#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 2, Slides 11-20
10 figures covering: expected vs found, parameter count, three method changes,
two pipelines, wall map, 50-year gap, sin2thetaW prediction,
ppm intuition, CD fan-out, three walls closing frame.
Output: PNG files to ./figures/
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
        edgecolor=color, linewidth=1.5)
    ax.add_patch(box)
    if text:
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
                color=textcolor, fontweight='bold', zorder=10)


# ================================================================
# FIG 11: WHAT EVERYONE WAS LOOKING FOR
# Type: Scale/Landscape
# Shows: sprawling complex theories vs one simple particle
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)

ax.text(8, 9.5, "The Search for Unification: Expected vs Found",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Top row — sprawling failures
ax.text(1.0, 8.3, "What they searched for:", ha='left', va='center',
        fontsize=11, color=RED)

theories = [
    (2.5, 6.8, "Supersymmetry\n+105 parameters", RED, 2.8, 1.8),
    (6.2, 6.8, "String Theory\n+6 dimensions\n" + r"$10^{500}$ vacua", RED, 2.8, 1.8),
    (9.9, 6.8, "Extra Higgs\n+20 parameters", ORANGE, 2.8, 1.8),
    (13.2, 6.8, "Technicolor\n+new force\n+50 parameters", ORANGE, 2.8, 1.8),
]

for tx, ty, tlabel, tcol, tw, th in theories:
    box = mpatches.FancyBboxPatch((tx - tw/2, ty - th/2), tw, th,
        boxstyle="round,pad=0.15", facecolor=tcol, alpha=0.12,
        edgecolor=tcol, linewidth=2)
    ax.add_patch(box)
    ax.text(tx, ty, tlabel, ha='center', va='center', fontsize=9,
            color=tcol, fontweight='bold')

ax.text(14.5, 5.5, "Decades of search.\nBillions of dollars.\nZero confirmed\npredictions.",
        ha='center', va='center', fontsize=9, color=RED, fontstyle='italic')

# Divider
ax.plot([1, 15], [4.5, 4.5], color=DIM, linewidth=1, linestyle='--', alpha=0.4)

# Bottom row — one simple particle
ax.text(1.0, 3.8, "What was found:", ha='left', va='center',
        fontsize=11, color=GOLD)

box_cd = mpatches.FancyBboxPatch((5.5, 1.5), 5.0, 2.0,
    boxstyle="round,pad=0.2", facecolor=GOLD, alpha=0.15,
    edgecolor=GOLD, linewidth=2.5)
ax.add_patch(box_cd)
ax.text(8.0, 2.9, "Cabibbo Doublet", ha='center', va='center',
        fontsize=14, color=GOLD, fontweight='bold')
ax.text(8.0, 2.2, "1 particle.  3 numbers.  (1/15,  1,  1/3)", ha='center', va='center',
        fontsize=11, color=WHITE)
ax.text(8.0, 1.7, "53 derived values.  13 inputs.  Surplus +40.", ha='center', va='center',
        fontsize=9, color=SILVER)

ax.text(8.0, 0.5, "The simplest extension nobody tried\nbecause it looked too simple.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk2_11_expected_vs_found.png")


# ================================================================
# FIG 12: THE PARAMETER COUNT
# Type: Comparison Bar
# Shows: absurd asymmetry — huge bars and one empty bar
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

theories = [
    ("MSSM\n(Supersymmetry)", 105, RED),
    ("Technicolor", 50, ORANGE),
    ("Two Higgs\nDoublet", 7, ORANGE),
    ("Cabibbo Doublet\n(RUM)", 0, GOLD),
]

y = np.arange(len(theories))
values = [t[1] for t in theories]
colors = [t[2] for t in theories]
names = [t[0] for t in theories]

bars = ax.barh(y, values, height=0.55, color=colors, alpha=0.7,
               edgecolor=colors, linewidth=1.5)

for i in range(len(theories)):
    val = values[i]
    if val == 0:
        ax.text(2, y[i], "ZERO new parameters", ha='left', va='center',
                fontsize=11, color=GOLD, fontweight='bold')
    else:
        ax.text(val + 1.5, y[i], str(val), ha='left', va='center',
                fontsize=11, color=colors[i], fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=11, color=WHITE)
ax.set_xlabel("New free parameters required", fontsize=11, color=SILVER)
ax.set_title("New Parameters Required for Unification",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# String theory note at top
ax.text(90, 3.5, "String Theory:\n" + r"$10^{500}$ vacua" + "\n(off the chart)",
        ha='center', va='center', fontsize=9, color=RED, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.6))

ax.text(55, -0.7, "The quantum numbers determine everything.\nNo free parameters to tune.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

ax.set_xlim(0, 120)
ax.set_ylim(-1.2, 4.2)
ax.invert_yaxis()

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk2_12_parameter_count.png")


# ================================================================
# FIG 13: THREE METHOD CHANGES
# Type: Progression/Sequence (before/after panels)
# Shows: three parallel transformations, not a revolution
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 9),
                          gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)
fig.suptitle("What Changed: Method, Not Physics", fontsize=17,
             fontweight='bold', color=GOLD, y=0.96)

panels = [
    ("Numbers", "4.10000...", "41/10", "Keep the\nintegers alive",
     DIM, GOLD, "Decimals", "Fractions"),
    ("Scope", "Particle\nPhysics\nonly", "5 departments\nconnected", "Cross every\nboundary",
     DIM, CYAN, "One dept", "All depts"),
    ("Testing", "Manual\nchecking\n(hope for best)", "Automated\nPASS / FAIL\n(every value)", "Test everything\nagainst measurement",
     DIM, GREEN, "Manual", "Automated"),
]

for idx, (title, before_txt, after_txt, bottom, bcol, acol, blabel, alabel) in enumerate(panels):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.3, title, ha='center', va='center', fontsize=14,
            fontweight='bold', color=WHITE)

    # Before box
    ax.text(5, 7.5, blabel, ha='center', va='center', fontsize=9, color=bcol)
    box_b = mpatches.FancyBboxPatch((1.5, 5.8), 7.0, 2.2,
        boxstyle="round,pad=0.2", facecolor=bcol, alpha=0.1,
        edgecolor=bcol, linewidth=1.5)
    ax.add_patch(box_b)
    ax.text(5, 6.9, before_txt, ha='center', va='center', fontsize=11,
            color=bcol)

    # Arrow down
    ax.annotate("", xy=(5, 5.2), xytext=(5, 5.6),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

    # After box
    ax.text(5, 4.8, alabel, ha='center', va='center', fontsize=9, color=acol)
    box_a = mpatches.FancyBboxPatch((1.5, 2.8), 7.0, 2.2,
        boxstyle="round,pad=0.2", facecolor=acol, alpha=0.12,
        edgecolor=acol, linewidth=2)
    ax.add_patch(box_a)
    ax.text(5, 3.9, after_txt, ha='center', va='center', fontsize=12,
            color=acol, fontweight='bold')

    # Bottom label
    ax.text(5, 1.5, bottom, ha='center', va='center', fontsize=9,
            color=SILVER, fontstyle='italic')

save(fig, "talk2_13_three_method_changes.png")


# ================================================================
# FIG 14: TWO PIPELINES — STANDARD VS RUM
# Type: Progression/Sequence (two rows)
# Shows: divergence point at step 2 — decimals vs fractions
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-1, 9)

ax.text(9, 8.5, "Two Pipelines, Same Physics, Different Output",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Shared start
rounded_box(ax, 1.5, 5.5, 2.2, 1.2, "Measure\ncouplings", WHITE, fontsize=9,
            textcolor=WHITE, alpha=0.15)

# Top row — standard (dim, fails)
std_steps = [
    (4.5, 7.3, "Convert to\ndecimals", DIM),
    (7.5, 7.3, "Run with\nfloats", DIM),
    (10.5, 7.3, "Gap " + r"$\approx$" + " 0?", DIM),
    (13.0, 7.3, "Add SUSY /\nstrings / etc", RED),
    (15.8, 7.3, "Still doesn't\nwork", RED),
]

ax.text(1.5, 7.8, "Standard:", ha='center', va='center', fontsize=9, color=DIM)

for i, (sx, sy, stxt, scol) in enumerate(std_steps):
    rounded_box(ax, sx, sy, 2.0, 1.0, stxt, scol, fontsize=8, alpha=0.12)
    if i == 0:
        ax.annotate("", xy=(sx - 1.1, sy), xytext=(2.7, 5.8),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))
    if i > 0:
        prev_x = std_steps[i-1][0]
        ax.annotate("", xy=(sx - 1.1, sy), xytext=(prev_x + 1.1, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Dead end X
ax.text(17.0, 7.3, r"$\times$", ha='center', va='center', fontsize=24,
        color=RED, fontweight='bold')

# Bottom row — RUM (bright, succeeds)
rum_steps = [
    (4.5, 3.7, "Store as\nFractions", GOLD),
    (7.5, 3.7, "Run with\nexact arith.", GOLD),
    (10.5, 3.7, "Gap = p/q?", CYAN),
    (13.0, 3.7, "Gap = 38/27\nexact!", GREEN),
    (15.8, 3.7, "53 values\nmatch", GREEN),
]

ax.text(1.5, 3.2, "RUM:", ha='center', va='center', fontsize=9, color=GOLD)

for i, (rx, ry, rtxt, rcol) in enumerate(rum_steps):
    rounded_box(ax, rx, ry, 2.0, 1.0, rtxt, rcol, fontsize=8, alpha=0.15)
    if i == 0:
        ax.annotate("", xy=(rx - 1.1, ry), xytext=(2.7, 5.2),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))
    if i > 0:
        prev_x = rum_steps[i-1][0]
        ax.annotate("", xy=(rx - 1.1, ry), xytext=(prev_x + 1.1, ry),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Success check
ax.text(17.0, 3.7, r"$\checkmark$", ha='center', va='center', fontsize=24,
        color=GREEN, fontweight='bold')

# Divergence annotation
ax.annotate("Paths split here:\ndecimals vs fractions",
            xy=(3.4, 5.5), xytext=(4.5, 5.5),
            fontsize=9, color=GOLD, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax.text(9, 0.3, "Same equations. Same data. Different representation.\nOne digit of difference, 50 years of consequences.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk2_14_two_pipelines.png")


# ================================================================
# FIG 15: THE WALL MAP — EVERY WALL ON THE CHAIN
# Type: Connection/Integer Map
# Shows: full derivation chain with four barriers marked
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 12)

ax.text(8, 11.3, "Every Wall Between Integers and Deuterium",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Chain nodes — zigzag down the page for space
nodes = [
    (2.0, 9.5, r"$\beta$ = 41/10," + "\n" + r"$-$19/6, $-$7", "group theory", GOLD),
    (6.0, 9.5, "gap = 38/27", "CD correction", CYAN),
    (10.0, 9.5, r"sin$^2\theta_W$" + "\n= 0.2312", "12 ppm", GREEN),
    (14.0, 9.5, r"$\alpha_s$" + " = 0.1184", "0.33%", GREEN),
    (3.0, 6.0, "DM/baryon\n= (22/13)" + r"$\pi$", "725 ppm", PURPLE),
    (7.5, 6.0, r"$\Omega_b$" + " = 0.0490", "727 ppm", CYAN),
    (12.0, 6.0, r"$\eta_{10}$" + " = 6.09", "0.24%", ORANGE),
    (12.0, 3.0, "D/H = 2.531\n" + r"$\times 10^{-5}$", "0.12" + r"$\sigma$", MAG),
]

for nx, ny, nlabel, nmiss, ncol in nodes:
    rounded_box(ax, nx, ny, 2.8, 1.5, "", ncol, alpha=0.15)
    ax.text(nx, ny + 0.2, nlabel, ha='center', va='center', fontsize=9,
            color=WHITE, fontweight='bold')
    ax.text(nx, ny - 0.45, nmiss, ha='center', va='center', fontsize=8,
            color=ncol, fontstyle='italic')

# Arrows between chain nodes
chain_connections = [
    (0, 1), (1, 2), (2, 3),  # top row
    (3, 4),  # down to second row (diagonal)
    (4, 5), (5, 6),  # second row
    (6, 7),  # down to result
]

for a, b in chain_connections:
    ax_x, ay = nodes[a][0], nodes[a][1]
    bx_x, by = nodes[b][0], nodes[b][1]
    ax.annotate("", xy=(bx_x, by + 0.8 if by < ay else by),
                xytext=(ax_x, ay - 0.8 if by < ay else ay),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2, alpha=0.6))

# Walls — between specific nodes
walls = [
    (4.0, 9.5, "decimal\nconversion\nwall"),
    (8.5, 7.7, "particle " + r"$\rightarrow$" + "\ncosmology\nwall"),
    (9.8, 4.5, "cosmology " + r"$\rightarrow$" + "\nnuclear\nwall"),
]

for wx, wy, wlabel in walls:
    ax.plot([wx, wx], [wy - 1.2, wy + 1.2], color=RED, linewidth=2.5,
            linestyle=':', alpha=0.6)
    ax.text(wx + 0.3, wy, wlabel, ha='left', va='center', fontsize=7,
            color=RED, alpha=0.8)

ax.text(8, 0.5, "The chain exists in the equations.\nThe walls exist only in institutions.",
        ha='center', va='center', fontsize=12, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=DIM))

save(fig, "talk2_15_wall_map.png")


# ================================================================
# FIG 16: THE 50-YEAR GAP
# Type: Scale/Landscape (timeline)
# Shows: every ingredient was known — assembly was not
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

events = [
    (1973, r"Yang-Mills $\beta$" + "\ncoefficients", GOLD),
    (1974, "Georgi-Glashow\nSU(5)", CYAN),
    (1979, "Weinberg-Salam\nNobel", GREEN),
    (1998, "Dark energy\ndiscovered", PURPLE),
    (2003, "WMAP dark\nmatter ratio", MAG),
    (2015, "Planck final\nDM/b = 5.320", ORANGE),
    (2026, "RUM connects\nthem all", GOLD),
]

years = [e[0] for e in events]
labels = [e[1] for e in events]
colors = [e[2] for e in events]

ax.set_xlim(1968, 2032)
ax.set_ylim(-0.5, 3.5)

# Timeline bar
ax.plot([1970, 2030], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.5)

# Events — alternate vertical positions to avoid overlap
for i, (yr, lbl, col) in enumerate(events):
    # Alternate high and low
    y_dot = 0.5
    y_text = 1.6 + (i % 2) * 0.9

    ax.scatter([yr], [y_dot], s=200 if yr != 2026 else 400,
               color=col, edgecolors=WHITE, linewidth=1.5, zorder=5,
               marker='*' if yr == 2026 else 'o')

    ax.plot([yr, yr], [y_dot + 0.1, y_text - 0.3], color=col,
            linewidth=1, alpha=0.4)

    ax.text(yr, y_text, lbl, ha='center', va='bottom', fontsize=9,
            color=col, fontweight='bold' if yr == 2026 else 'normal')

# Gap shading
ax.axvspan(1973, 2026, alpha=0.03, color=GOLD)

# Duration annotation
ax.annotate("", xy=(1973, 0.15), xytext=(2026, 0.15),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))
ax.text(1999.5, 0.0, "53 years", ha='center', va='center',
        fontsize=11, color=GOLD, fontweight='bold')

ax.text(1999.5, -0.3, "Every ingredient was public.\nThe recipe was not.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

ax.set_title("Every Piece Was Known. The Chain Was Not.",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.set_xlabel("Year", fontsize=11, color=SILVER)
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk2_16_fifty_year_gap.png")


# ================================================================
# FIG 17: SIN2THETAW PREDICTION — 12 PPM FROM INTEGERS
# Type: Threshold/Region
# Shows: predicted dot sitting inside measured band
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

measured = 0.23122
uncertainty = 0.00004
predicted_cd = 0.231223
predicted_sm = 0.2315  # SM one-loop approximate

# Measured band
ax.axhspan(measured - uncertainty, measured + uncertainty, color=MAG, alpha=0.12)
ax.axhspan(measured - uncertainty*3, measured + uncertainty*3, color=MAG, alpha=0.05)
ax.axhline(y=measured, color=MAG, linewidth=1.5, linestyle='--', alpha=0.6)

# Label the bands
ax.text(3.5, measured + uncertainty * 1.5, r"1$\sigma$ measurement band",
        ha='center', va='bottom', fontsize=9, color=MAG, alpha=0.8)

# Predicted points
ax.scatter([1.5], [predicted_cd], s=300, color=GOLD, edgecolors=WHITE,
           linewidth=2, zorder=10, marker='o')
ax.text(1.5, predicted_cd + 0.00012, "CD prediction\n0.231223\nmiss: 12 ppm",
        ha='center', va='bottom', fontsize=10, color=GOLD, fontweight='bold')

ax.scatter([3.0], [predicted_sm], s=200, color=DIM, edgecolors=WHITE,
           linewidth=1.5, zorder=10, marker='o')
ax.text(3.0, predicted_sm + 0.00012, "SM one-loop\n0.2315\nmiss: 0.12%",
        ha='center', va='bottom', fontsize=9, color=DIM)

# Measured label
ax.text(4.5, measured, "LEP measurement\n0.23122\n(millions of Z bosons)",
        ha='left', va='center', fontsize=10, color=MAG,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG, alpha=0.6))

ax.set_xlim(0.5, 6)
ax.set_ylim(0.2300, 0.2330)
ax.set_ylabel(r"sin$^2\theta_W$", fontsize=12, color=SILVER)
ax.set_xticks([])
ax.set_title(r"sin$^2\theta_W$: Predicted from One Input + Integers",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Bottom annotation
ax.text(3.5, 0.23015, "One measured input (" + r"$\alpha_{em}$"
        + ").  One set of integer betas.\nOutput: 5-digit prediction of an independent observable.",
        ha='center', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk2_17_sin2thetaw_prediction.png")


# ================================================================
# FIG 18: WHAT "PARTS PER MILLION" FEELS LIKE
# Type: Scale/Landscape
# Shows: abstract numbers as spatial/temporal analogies
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)

ax.text(8, 9.5, "Precision Intuition: What These Numbers Mean",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

rows = [
    (r"$\alpha^{-1}$: 0.007 ppb", "7 millimeters in 1,000 kilometers", GOLD, 8.0),
    (r"sin$^2\theta_W$: 12 ppm", "12 seconds in 11.5 days", GREEN, 6.5),
    ("DM/baryon: 725 ppm", "1 meter in 1.38 kilometers", CYAN, 5.0),
    (r"$\alpha_s$: 0.33%", "3.3 meters in 1 kilometer", BLUE, 3.5),
    ("Proton mass: 28.6%", "One-loop approximation. Known fix: two-loop.", RED, 2.0),
]

for label, analogy, col, y in rows:
    # Left: physics value
    ax.text(0.5, y, label, ha='left', va='center', fontsize=12,
            color=col, fontweight='bold')

    # Right: intuition
    ax.text(8.5, y, analogy, ha='left', va='center', fontsize=11,
            color=SILVER)

    # Connecting dots
    ax.plot([7.0, 8.2], [y, y], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

    # Scale bar (proportional, log compressed for visibility)
    bar_widths = {8.0: 0.3, 6.5: 0.8, 5.0: 2.5, 3.5: 4.0, 2.0: 6.5}
    bw = bar_widths.get(y, 1.0)
    bar_y = y - 0.35
    ax.barh(bar_y, bw, left=0.5, height=0.2, color=col, alpha=0.3,
            edgecolor=col, linewidth=1)

ax.text(8, 0.5, "Even the worst prediction (28.6%) has a diagnosed cause\nand a defined fix. The others are extraordinary.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk2_18_ppm_intuition.png")


# ================================================================
# FIG 19: CD FAN-OUT — ONE PARTICLE, NINE DOMAINS
# Type: Connection/Integer Map (radial)
# Shows: one particle radiating into nine domains
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

ax.text(0, 7.3, "One Particle, Three Shifts, Nine Domains",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Center — Cabibbo Doublet
center_box = mpatches.FancyBboxPatch((-2, -1.2), 4, 2.4,
    boxstyle="round,pad=0.3", facecolor=GOLD, alpha=0.15,
    edgecolor=GOLD, linewidth=2.5)
ax.add_patch(center_box)
ax.text(0, 0.4, "Cabibbo Doublet", ha='center', va='center',
        fontsize=14, color=GOLD, fontweight='bold')
ax.text(0, -0.1, "(3, 2, 1/6)", ha='center', va='center',
        fontsize=12, color=WHITE)
ax.text(0, -0.6, r"$\Delta b$ = (1/15, 1, 1/3)", ha='center', va='center',
        fontsize=10, color=SILVER)

# Nine domains arranged in a circle
domains = [
    ("QED\n0.007 ppb", GOLD),
    ("Electroweak\n195 ppm", CYAN),
    ("GUT\n12 ppm", GREEN),
    ("Cosmology\n725 ppm", PURPLE),
    ("Nuclear/BBN\n0.12" + r"$\sigma$", ORANGE),
    ("Muon g-2\n6.5" + r"$\sigma$", MAG),
    ("CKM/Flavor\n0.83" + r"$\sigma$", BLUE),
    ("Mass/Koide\n62 ppm", SILVER),
    ("Confinement\n2% shift", RED),
]

n_dom = len(domains)
radius = 5.5

for i, (dlabel, dcol) in enumerate(domains):
    angle = np.pi/2 + 2 * np.pi * i / n_dom
    dx = radius * np.cos(angle)
    dy = radius * np.sin(angle)

    # Domain box
    box = mpatches.FancyBboxPatch((dx - 1.3, dy - 0.7), 2.6, 1.4,
        boxstyle="round,pad=0.15", facecolor=dcol, alpha=0.12,
        edgecolor=dcol, linewidth=1.5)
    ax.add_patch(box)
    ax.text(dx, dy, dlabel, ha='center', va='center', fontsize=9,
            color=dcol, fontweight='bold')

    # Arrow from center to domain
    arrow_start_x = 1.8 * np.cos(angle)
    arrow_start_y = 1.0 * np.sin(angle)
    arrow_end_x = dx - 1.4 * np.cos(angle)
    arrow_end_y = dy - 0.8 * np.sin(angle)
    ax.annotate("", xy=(arrow_end_x, arrow_end_y),
                xytext=(arrow_start_x, arrow_start_y),
                arrowprops=dict(arrowstyle='->', color=dcol, lw=1.5, alpha=0.5))

save(fig, "talk2_19_cd_fanout.png")


# ================================================================
# FIG 20: THREE WALLS — CLOSING FRAME
# Type: Geometric Cross-Section
# Shows: three walls cracked open, truth visible behind each
# ================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 10),
                          gridspec_kw={'wspace': 0.20})
fig.patch.set_facecolor(BG)
fig.suptitle("Three Walls That Prevented Discovery", fontsize=17,
             fontweight='bold', color=GOLD, y=0.96)

wall_data = [
    ("WRONG\nNUMBERS", "4.1\n3.167\n7.0", "41/10\n" + r"$-$19/6" + "\n" + r"$-$7",
     DIM, GOLD, "Decimals hide\ninteger structure"),
    ("WRONG\nNAMES", r"$\alpha, \beta, \gamma$" + "\n" + r"$\theta, \Omega$",
     "reading\nvortex\nsoliton",
     DIM, GREEN, "Greek letters\nhide plain meaning"),
    ("WRONG\nDEPTS", "Particle\nCosmo\nNuclear", "One connected\nchain through\nall domains",
     DIM, CYAN, "Silos prevent\ncross-domain work"),
]

for idx, (title, wall_txt, behind_txt, wcol, bcol, caption) in enumerate(wall_data):
    ax = axes[idx]
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.text(5, 9.3, title, ha='center', va='center', fontsize=14,
            fontweight='bold', color=RED)

    # Wall (left half)
    wall = mpatches.FancyBboxPatch((0.8, 3.0), 3.5, 4.5,
        boxstyle="round,pad=0.1", facecolor=wcol, alpha=0.2,
        edgecolor=wcol, linewidth=2)
    ax.add_patch(wall)
    ax.text(2.55, 5.25, wall_txt, ha='center', va='center', fontsize=12,
            color=DIM)

    # Crack
    crack_x = [4.3, 4.5, 4.2, 4.6, 4.3, 4.5, 4.3]
    crack_y = [3.0, 4.0, 5.0, 5.5, 6.0, 6.8, 7.5]
    ax.plot(crack_x, crack_y, color=GOLD, linewidth=2.5, alpha=0.8)

    # Behind wall (right half)
    behind = mpatches.FancyBboxPatch((5.0, 3.0), 4.0, 4.5,
        boxstyle="round,pad=0.1", facecolor=bcol, alpha=0.1,
        edgecolor=bcol, linewidth=1.5)
    ax.add_patch(behind)
    ax.text(7.0, 5.25, behind_txt, ha='center', va='center', fontsize=12,
            color=bcol, fontweight='bold')

    # Caption
    ax.text(5, 1.5, caption, ha='center', va='center', fontsize=9,
            color=SILVER, fontstyle='italic')

# Bottom annotation across all panels
fig.text(0.5, 0.03, "None of this is conspiracy. The structure of the academy prevents certain kinds of work.\nThe physics was always there.",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk2_20_three_walls.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 2, 11-20) generated ===")
filenames = [
    "talk2_11_expected_vs_found.png",
    "talk2_12_parameter_count.png",
    "talk2_13_three_method_changes.png",
    "talk2_14_two_pipelines.png",
    "talk2_15_wall_map.png",
    "talk2_16_fifty_year_gap.png",
    "talk2_17_sin2thetaw_prediction.png",
    "talk2_18_ppm_intuition.png",
    "talk2_19_cd_fanout.png",
    "talk2_20_three_walls.png",
]
for f in filenames:
    print("  %s" % f)
    