#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 9, Slides 11-20
10 figures covering: sector splitting prediction, five gravity kill switches,
what dies/survives, fourth coordinate, GPS depth interpretation,
clock kill sequence, D/K classification, frozen scan 89%,
prediction timeline, radical vs falsifiable quadrant.
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
# FIG 11: THE SECTOR SPLITTING PREDICTION
# Type: Threshold/Region
# Shows: two clocks, same spot, tiny predicted difference
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1.5, 10)

ax.text(5, 9.3, "The One Prediction That Distinguishes\nThis from Standard GR",
        ha='center', va='center', fontsize=15, fontweight='bold', color=GOLD)

# Two clocks side by side
# Th-229 (nuclear)
rounded_box(ax, 2.5, 6.5, 3.0, 2.5, "", RED, alpha=0.12)
ax.text(2.5, 7.4, "Th-229", ha='center', va='center', fontsize=14,
        color=RED, fontweight='bold')
ax.text(2.5, 6.8, "Nuclear clock", ha='center', va='center', fontsize=9,
        color=SILVER)
ax.text(2.5, 6.1, "probes strong\n+ EM sectors", ha='center', va='center',
        fontsize=8, color=RED)

# Sr-87 (optical)
rounded_box(ax, 7.5, 6.5, 3.0, 2.5, "", CYAN, alpha=0.12)
ax.text(7.5, 7.4, "Sr-87", ha='center', va='center', fontsize=14,
        color=CYAN, fontweight='bold')
ax.text(7.5, 6.8, "Optical clock", ha='center', va='center', fontsize=9,
        color=SILVER)
ax.text(7.5, 6.1, "probes EM\nsector only", ha='center', va='center',
        fontsize=8, color=CYAN)

# Same location label
ax.text(5, 5.0, "Same altitude. Same location. Same " + r"$\Phi$.",
        ha='center', va='center', fontsize=10, color=WHITE)

# Standard GR prediction
rounded_box(ax, 5, 3.5, 8, 1.0, "", GREEN, alpha=0.08)
ax.text(5, 3.5, "Standard GR: both clocks show IDENTICAL dilation. No difference. Period.",
        ha='center', va='center', fontsize=10, color=GREEN)

# Reading depth prediction
rounded_box(ax, 5, 2.0, 8, 1.0, "", GOLD, alpha=0.1)
ax.text(5, 2.0, "Reading depth: " + r"$\varepsilon = \kappa \times |\Delta\beta| \times \Delta\Phi/c^2 \approx 10^{-12}$" +
        ". A tiny split.",
        ha='center', va='center', fontsize=9, color=GOLD)

# Magnitude context
ax.text(5, 0.8, "Predicted split: " + r"$\sim 10^{-12}$" +
        ".    Current clock precision: " + r"$10^{-18}$" +
        ".\nSix orders of magnitude above detection threshold.",
        ha='center', va='center', fontsize=9, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

ax.text(5, -0.5, "If clocks agree: sector splitting is dead, park the interpretation.\n"
        "If they disagree: new physics. The fourth coordinate is depth.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

save(fig, "talk9_11_sector_splitting.png")


# ================================================================
# FIG 12: FIVE KILL SWITCHES — THE GRAVITY PROGRAM'S DEATH CONDITIONS
# Type: Identity Card
# Shows: five specific kill conditions with named experiments
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 13)

ax.text(5, 12.2, "Five Ways to Kill the Gravity Interpretation",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

switches = [
    ("Nuclear vs optical clock",
     "Th-229 and Sr-87 show same\ndilation at " + r"$\geq$" + "2 potentials",
     "PTB / JILA 2028-2032"),
    ("NANOGrav pulsar timing",
     "Residuals show no correlation\nwith galactocentric radius",
     "NANOGrav 15-yr + extensions"),
    ("Hubble tension resolved",
     "Systematic error found\nin SH0ES or Planck",
     "JWST calibrations"),
    ("G measurement scatter",
     "Published G values show no\ncorrelation with lab environment",
     "NIST / PTB / BIPM meta-analysis"),
    ("Voyager Doppler",
     "Voyager data at heliopause\nshows exact GR, no anomaly",
     "JPL tracking data"),
]

for i, (name, condition, source) in enumerate(switches):
    y = 10.5 - i * 2.0

    card = mpatches.FancyBboxPatch((0.3, y - 0.8), 9.4, 1.6,
        boxstyle="round,pad=0.15", facecolor=BG, alpha=0.8,
        linewidth=1.5)
    ax.add_patch(card)

    # Red left border
    ax.plot([0.3, 0.3], [y - 0.8, y + 0.8], color=RED, linewidth=4, alpha=0.7)

    # Kill icon
    ax.text(1.2, y + 0.3, r"$\times$", ha='center', va='center',
            fontsize=16, color=RED, fontweight='bold')

    ax.text(2.5, y + 0.3, name, ha='left', va='center', fontsize=10,
            color=RED, fontweight='bold')
    ax.text(2.5, y - 0.2, condition, ha='left', va='center', fontsize=8,
            color=WHITE)
    ax.text(7.5, y - 0.2, source, ha='left', va='center', fontsize=8,
            color=CYAN, fontstyle='italic')

ax.text(5, 0.3, "Any one of these could kill the gravity interpretation.\n"
        "The rest of RUM survives because gravity is independent\n"
        "of the QED chain and the BBN chain.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_12_five_gravity_kills.png")


# ================================================================
# FIG 13: WHAT DIES AND WHAT SURVIVES
# Type: Connection/Integer Map
# Shows: firewall between killable and independent pieces
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 9)

ax.text(7, 8.3, "If the Gravity Interpretation Dies",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Left zone: dies
ax.text(3.5, 7.3, "DIES", ha='center', va='center', fontsize=14,
        color=RED, fontweight='bold')

dies = [
    "Reading depth = time\ndilation interpretation",
    "Sector splitting\nprediction",
    "G-scatter\nexplanation",
    "Hubble tension\nboundary framing",
]

for i, item in enumerate(dies):
    y = 6.0 - i * 1.5
    rounded_box(ax, 3.5, y, 4.0, 1.0, item, RED, fontsize=8, alpha=0.1, textcolor=RED)

# FIREWALL
ax.plot([7, 7], [0.5, 7.5], color=GOLD, linewidth=4, alpha=0.6)
ax.text(7, 7.8, "FIREWALL", ha='center', va='center', fontsize=12,
        color=GOLD, fontweight='bold')
ax.text(7, 0.2, "modular design", ha='center', va='center', fontsize=8,
        color=GOLD, fontstyle='italic')

# Right zone: survives
ax.text(10.5, 7.3, "SURVIVES", ha='center', va='center', fontsize=14,
        color=GREEN, fontweight='bold')

survives = [
    "QED chain\n(" + r"$\alpha$" + " at 0.007 ppb)",
    "Electroweak sector\n(" + r"$M_W$" + ", decay channels)",
    "BBN chain\n(D/H at 0.12" + r"$\sigma$" + ")",
    "Beta unification\n(sin" + r"$^2\theta_W$" + " at 12 ppm)",
    "Q335 basis",
    "Koide relation",
    "Confinement boundary",
]

for i, item in enumerate(survives):
    y = 6.3 - i * 0.9
    rounded_box(ax, 10.5, y, 4.0, 0.6, item, GREEN, fontsize=7, alpha=0.12, textcolor=GREEN)

ax.text(7, -0.7, "The framework is modular. Pieces can die independently.\n"
        "4 results die. 7 results survive. Designed for partial falsification.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_13_dies_vs_survives.png")


# ================================================================
# FIG 14: THE FOURTH COORDINATE — DEPTH NOT TIME
# Type: Geometric Cross-Section (two panels)
# Shows: vertical timeline vs radial depth line — incompatible pictures
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Two Views of the Fourth Coordinate",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Standard (time as dimension) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Standard GR", ha='center', va='center',
         fontsize=13, fontweight='bold', color=CYAN)

# Axes
ax1.annotate("", xy=(5, 8.0), xytext=(5, 2.0),
             arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax1.text(5.5, 8.0, "time", ha='left', va='center', fontsize=10, color=CYAN)
ax1.annotate("", xy=(8.5, 2.0), xytext=(1.5, 2.0),
             arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))
ax1.text(8.5, 1.5, "space", ha='center', va='center', fontsize=10, color=CYAN)

# Worldline
ax1.plot([3, 4, 5, 6, 7], [2.5, 4.0, 5.0, 6.0, 7.5], color=WHITE, linewidth=2.5)
ax1.scatter([5], [5], s=100, color=WHITE, zorder=5, marker='o')

ax1.text(5, 1.0, "4th coordinate: 'when'\nYou move through time.",
         ha='center', va='center', fontsize=9, color=CYAN, fontstyle='italic')

# -- Right: Reading depth --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Reading Depth", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Nested circles
for r, al in [(3.5, 0.05), (2.8, 0.07), (2.1, 0.09), (1.4, 0.12), (0.7, 0.18)]:
    circle = mpatches.Circle((5, 5), r, facecolor=GOLD, alpha=al,
                              linewidth=1, linestyle='--')
    ax2.add_patch(circle)

# Radial arrow pointing inward
ax2.annotate("depth", xy=(5, 5), xytext=(8.0, 8.0),
             fontsize=10, color=GOLD, ha='center',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

ax2.scatter([5], [5], s=100, color=WHITE, zorder=5, marker='o')

ax2.text(5, 1.0, "4th coordinate: 'how deep'\nDeeper = slower clock.",
         ha='center', va='center', fontsize=9, color=GOLD, fontstyle='italic')

fig.text(0.5, 0.05, "Both produce: d" + r"$\tau$/dt = $\sqrt{1 - 2\Phi/c^2}$" +
         ". Same formula. Same GPS.\n"
         "The sector splitting experiment tells you which picture is correct.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk9_14_fourth_coordinate.png")


# ================================================================
# FIG 15: GPS — THE DAILY TEST
# Type: Geometric Cross-Section
# Shows: Earth + satellite at different depths, 38 us/day
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')

ax.text(0, 6.3, "GPS: Reading Depth in Your Pocket",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Earth
earth = mpatches.Circle((0, 0), 2.5, facecolor=GREEN, alpha=0.1,
                          linewidth=1.5, linestyle='-')
ax.add_patch(earth)

# Depth boundary circles
for r in [3.5, 4.5]:
    ring = mpatches.Circle((0, 0), r, facecolor='none',
                            linewidth=1, linestyle=':', alpha=0.2)
    ax.add_patch(ring)

# Ground clock
ax.scatter([0], [2.5], s=200, color=GREEN, zorder=5, marker='s')
ax.text(0, 1.5, "Ground clock", ha='center', va='center', fontsize=10,
        color=GREEN, fontweight='bold')
ax.text(0, 0.8, "deeper in hierarchy\nslower by 38 " + r"$\mu$s/day",
        ha='center', va='center', fontsize=8, color=GREEN)

# Satellite clock
ax.scatter([3.5], [3.5], s=200, color=CYAN, zorder=5, marker='^')
ax.text(3.5, 4.5, "GPS satellite\n20,200 km", ha='center', va='center',
        fontsize=10, color=CYAN, fontweight='bold')
ax.text(3.5, 2.8, "shallower\nfaster by\n38 " + r"$\mu$s/day",
        ha='center', va='center', fontsize=8, color=CYAN)

# Correction arrow
ax.annotate("38.64 " + r"$\mu$s/day" + "\ncorrection applied\ncontinuously",
            xy=(1.5, 3.0), xytext=(-3, 4.5),
            fontsize=9, color=GOLD, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Interpretations
ax.text(-4.5, -2.0, "Standard:\nspacetime curvature\ndiffers", ha='center',
        va='center', fontsize=8, color=DIM,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

ax.text(4.5, -2.0, "Reading depth:\nboundary depth\ndiffers", ha='center',
        va='center', fontsize=8, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN))

ax.text(0, -5.5, "Both produce the same 38 " + r"$\mu$s/day" + " correction.\n"
        "Your phone works either way.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_15_gps_depth.png")


# ================================================================
# FIG 16: THE KILL SEQUENCE — WHAT HAPPENS IF CLOCKS AGREE
# Type: Progression/Sequence
# Shows: pre-registered experiment -> result -> kill -> documentation
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "If the Clocks Agree: The Kill Sequence",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

steps = [
    (2.0, 3.5, "THE\nEXPERIMENT", "Th-229 and Sr-87\ncompared at two\npotentials", CYAN),
    (5.5, 3.5, "THE\nMEASUREMENT", "Identical dilation\nwithin " + r"$10^{-18}$" + "\nNo splitting", GREEN),
    (9.0, 3.5, "THE\nCONSEQUENCE", "Kill switch fires.\nSector splitting:\nKILLED.\nReading depth:\nPARKED.", RED),
    (12.5, 3.5, "THE\nAFTERMATH", "Documentation\npublished.\nStatus: KILLED.\nOther RUM programs:\nunaffected.", GOLD),
]

for i, (sx, sy, stitle, sdesc, scol) in enumerate(steps):
    rounded_box(ax, sx, sy, 2.8, 3.5, "", scol, alpha=0.12)
    ax.text(sx, sy + 1.2, stitle, ha='center', va='center', fontsize=10,
            color=scol, fontweight='bold')
    ax.text(sx, sy - 0.3, sdesc, ha='center', va='center', fontsize=8,
            color=SILVER)

    if i < len(steps) - 1:
        nx = steps[i+1][0]
        ax.annotate("", xy=(nx - 1.5, sy), xytext=(sx + 1.5, sy),
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

ax.text(8, 0.3, "The kill is pre-registered. The prediction is on the record\nbefore the experiment runs. That's how science should work.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_16_clock_kill_sequence.png")


# ================================================================
# FIG 17: THE D/K CLASSIFICATION — 10 PURE D, 1 PURE K, 4 MIXED
# Type: Comparison Bar
# Shows: 10-1-4 ratio — D dominates overwhelmingly
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Three groups
categories = ["Pure D\n(Reading)", "Pure K\n(Tick)", "Mixed\nD " + r"$\times$" + " K"]
counts = [10, 1, 4]
bar_cols = [CYAN, ORANGE, PURPLE]

x = np.arange(len(categories))

for i in range(len(categories)):
    ax.bar(x[i], counts[i], width=0.5, color=bar_cols[i], alpha=0.6)
    ax.text(x[i], counts[i] + 0.3, str(counts[i]), ha='center', va='bottom',
            fontsize=18, color=bar_cols[i], fontweight='bold')

# Percentage labels
ax.text(0, 8, "67%", ha='center', va='center', fontsize=12, color=CYAN)
ax.text(1, 8, "7%", ha='center', va='center', fontsize=12, color=ORANGE)
ax.text(2, 8, "26%", ha='center', va='center', fontsize=12, color=PURPLE)

# Example labels inside bars
pure_d = ["Mercury", "solar redshift", "Shapiro delay", "Pound-Rebka",
          "GPS (grav)", "lensing", "frame drag", "Nordtvedt", "geodetic", "perihelion"]
ax.text(0, 5, "\n".join(pure_d), ha='center', va='center', fontsize=6,
        color=SILVER, linespacing=1.2)

ax.text(1, 0.5, "muon\nlifetime", ha='center', va='center', fontsize=7, color=SILVER)

mixed = ["Hulse-Taylor", "grav. waves", "binary inspiral", "time-delay\ninterferometry"]
ax.text(2, 2, "\n".join(mixed), ha='center', va='center', fontsize=7, color=SILVER)

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11, color=WHITE)
ax.set_ylabel("Number of GR effects", fontsize=11, color=SILVER)
ax.set_title("The D/K Classification of GR Effects",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(1, 10.5, "D dominates. The reading IS the physics.\nThe tick just makes it actual.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_ylim(0, 12)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_17_dk_classification.png")


# ================================================================
# FIG 18: THE FROZEN SCAN — 89% COVERAGE
# Type: Scale/Landscape (progress bar)
# Shows: nearly full bar from spatial structure alone
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Main progress bar
ax.barh(1, 89, height=0.6, color=CYAN, alpha=0.5, left=0)
ax.barh(1, 6, height=0.6, color=PURPLE, alpha=0.4, left=89)
ax.barh(1, 5, height=0.6, color=ORANGE, alpha=0.4, left=95)

# Labels inside
ax.text(44.5, 1, "Pure D: 89%\nComputable without time", ha='center', va='center',
        fontsize=11, color=WHITE, fontweight='bold')
ax.text(92, 1, "Mixed\n6%", ha='center', va='center', fontsize=9, color=WHITE)
ax.text(97.5, 1, "K\n5%", ha='center', va='center', fontsize=9, color=WHITE)

# Description below
ax.text(44.5, -0.2, "Freeze time. Compute the spatial structure.\n89% of gravity falls out.",
        ha='center', va='center', fontsize=10, color=CYAN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(92, -0.2, "Partially\nfrozen", ha='center', va='center',
        fontsize=7, color=PURPLE)

ax.text(97.5, -0.2, "Requires\ntime passage", ha='center', va='center',
        fontsize=7, color=ORANGE)

# The question
ax.text(50, 2.2, "If 89% of GR is spatial structure,\nwhy do we call the fourth coordinate 'time'?",
        ha='center', va='center', fontsize=14, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_title("The Frozen Scan: What You Can Compute Without Time",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(50, -1.0, "The frozen scan covers 89% of all GR effects.\n"
        "The fourth coordinate might be telling us about space, not time.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(-2, 105)
ax.set_ylim(-1.5, 2.8)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.set_xticklabels(["0%", "20%", "40%", "60%", "80%", "100%"],
                   fontsize=9, color=DIM)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_18_frozen_scan_89.png")


# ================================================================
# FIG 19: THE PREDICTION TIMELINE
# Type: Progression/Sequence (timeline)
# Shows: prediction BEFORE experiment — genuine prediction
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

ax.plot([2025, 2033], [1.0, 1.0], color=DIM, linewidth=2, alpha=0.5)

events = [
    (2026, "Prediction\npublished:\n" + r"$\varepsilon \approx 10^{-12}$",
     GOLD, '*', 300),
    (2027, "Th-229 clock\nprototype\noperational",
     CYAN, 'o', 120),
    (2029, "Clock comparisons\nat single\npotential",
     GREEN, 'o', 120),
    (2031, "Comparisons at\nmultiple potentials\n(mountain/valley/ISS)",
     GREEN, 'o', 150),
    (2032, "Result:\nsplitting detected\nor null",
     GOLD, 'D', 200),
]

for i, (yr, desc, col, marker, sz) in enumerate(events):
    ax.scatter([yr], [1.0], s=sz, color=col, zorder=5, marker=marker)

    # Alternate above/below
    if i % 2 == 0:
        y_text = 2.0
        va = 'bottom'
    else:
        y_text = 0.0
        va = 'top'

    ax.plot([yr, yr], [1.0, y_text], color=col, linewidth=1, alpha=0.4)
    ax.text(yr, y_text, desc, ha='center', va=va, fontsize=8,
            color=col, fontweight='bold' if marker == '*' else 'normal')

# Pre-registered annotation
ax.annotate("PREDICTION\nBEFORE\nEXPERIMENT", xy=(2026, 1.5), xytext=(2026, 3.0),
            fontsize=9, color=GOLD, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# Outcome fork at 2032
ax.text(2032.5, 2.5, "Detected:\nnew physics!", ha='left', va='center',
        fontsize=8, color=GOLD)
ax.text(2032.5, -0.3, "Null: reading\ndepth killed", ha='left', va='center',
        fontsize=8, color=RED)

ax.set_title("The Prediction Is on the Record",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(2029, -1.3, "Predict then test, not test then explain.\n"
        "The prediction is on the record before the experiment runs.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(2025, 2033.5)
ax.set_ylim(-1.8, 3.8)
ax.set_xticks([2026, 2027, 2028, 2029, 2030, 2031, 2032])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_19_prediction_timeline.png")


# ================================================================
# FIG 20: THE FRONTIER — RADICAL VS FALSIFIABLE QUADRANT
# Type: Scale/Landscape (2D quadrant plot)
# Shows: reading depth in the rare top-right quadrant
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Quadrant labels
ax.text(0.25, 0.85, "Conservative\nTestable\n(standard physics)", ha='center', va='center',
        fontsize=8, color=GREEN, fontstyle='italic')
ax.text(0.75, 0.85, "Radical\nTestable\n(reading depth)", ha='center', va='center',
        fontsize=8, color=GOLD, fontstyle='italic')
ax.text(0.25, 0.15, "Conservative\nUntestable\n(boring)", ha='center', va='center',
        fontsize=8, color=DIM, fontstyle='italic')
ax.text(0.75, 0.15, "Radical\nUntestable\n(string landscape)", ha='center', va='center',
        fontsize=8, color=RED, fontstyle='italic')

# Quadrant lines
ax.axvline(x=0.5, color=DIM, linewidth=1, linestyle=':', alpha=0.3)
ax.axhline(y=0.5, color=DIM, linewidth=1, linestyle=':', alpha=0.3)

# Data points
points = [
    (0.2, 0.85, "QED chain", GREEN, 150),
    (0.35, 0.75, "Beta\nunification", CYAN, 120),
    (0.55, 0.6, "DM ratio\n(p=0.81)", ORANGE, 120),
    (0.75, 0.8, "Reading\ndepth", GOLD, 250),
    (0.85, 0.2, "String\ntheory", RED, 100),
    (0.8, 0.25, "Multiverse", RED, 80),
]

for px, py, plabel, pcol, psz in points:
    ax.scatter([px], [py], s=psz, color=pcol, zorder=5,
               marker='*' if pcol == GOLD else 'o')
    # Offset labels to avoid overlap
    if pcol == GOLD:
        ax.text(px - 0.08, py - 0.07, plabel, ha='center', va='top',
                fontsize=9, color=pcol, fontweight='bold')
    else:
        ax.text(px + 0.05, py - 0.05, plabel, ha='left', va='top',
                fontsize=7, color=pcol)

ax.set_xlabel("How radical " + r"$\rightarrow$", fontsize=11, color=SILVER)
ax.set_ylabel("How falsifiable " + r"$\rightarrow$", fontsize=11, color=SILVER)
ax.set_title("The Gravity Frontier: High Risk, High Information",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(0.5, 0.03, "The most speculative part of the model.\nAlso the most precisely falsifiable.\nThat combination is rare.",
        ha='center', va='bottom', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 0.98)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk9_20_radical_vs_falsifiable.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 9, 11-20) generated ===")
filenames = [
    "talk9_11_sector_splitting.png",
    "talk9_12_five_gravity_kills.png",
    "talk9_13_dies_vs_survives.png",
    "talk9_14_fourth_coordinate.png",
    "talk9_15_gps_depth.png",
    "talk9_16_clock_kill_sequence.png",
    "talk9_17_dk_classification.png",
    "talk9_18_frozen_scan_89.png",
    "talk9_19_prediction_timeline.png",
    "talk9_20_radical_vs_falsifiable.png",
]
for f in filenames:
    print("  %s" % f)
    