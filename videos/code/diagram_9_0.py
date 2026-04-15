#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 9, Slides 1-10
10 figures covering: four forces as readings, G scatter,
ocean analogy, everything dynamic except G, two interpretations,
soliton hierarchy depth, 18 tests across 60 orders,
precision cascade, GPA fail anatomy, D and K decomposition.
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
# FIG 1: FOUR FORCES, FOUR READINGS — INCLUDING GRAVITY
# Type: Comparison Bar (grid)
# Shows: three running forces + gravity with question marks
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "Four Forces, Four Readings, One Pattern",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column headers
col_heads = ["Force", "Lab scale", "Z boson", "Unification", "Status"]
col_x = [1.5, 4.5, 7.0, 9.5, 12.5]
for ch, cx in zip(col_heads, col_x):
    ax.text(cx, 8.5, ch, ha='center', va='center', fontsize=10,
            color=SILVER, fontweight='bold')

# Separator
ax.plot([0.5, 14], [8.1, 8.1], color=DIM, linewidth=0.5, alpha=0.3)

forces = [
    ("EM", BLUE, "1/137", "1/128", "1/42", "Accepted\nsince 1947"),
    ("Weak", GREEN, r"$10^{-5}$" + "\n(Fermi)", "1/30", "1/42", "Accepted\nsince 1967"),
    ("Strong", RED, "0.118", "~1\n(inside proton)", "1/42", "Accepted\nsince 1973"),
    ("Gravity", GOLD, "6.674" + r"$\times 10^{-11}$", "?", "?", "Measured at\nONE boundary.\nDeclared constant."),
]

for i, (fname, fcol, v1, v2, v3, status) in enumerate(forces):
    y = 7.0 - i * 1.8

    ax.text(col_x[0], y, fname, ha='center', va='center', fontsize=12,
            color=fcol, fontweight='bold')

    for j, val in enumerate([v1, v2, v3]):
        vcol = fcol if val != "?" else DIM
        ax.text(col_x[j+1], y, val, ha='center', va='center', fontsize=9,
                color=vcol,
                bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, alpha=0.3))

    ax.text(col_x[4], y, status, ha='center', va='center', fontsize=7,
            color=SILVER if i < 3 else GOLD, fontstyle='italic')

    # Separator
    ax.plot([0.5, 14], [y - 0.8, y - 0.8], color=DIM, linewidth=0.3, alpha=0.2)

# Bottom question
ax.text(7, -0.3, "Three forces: running is accepted physics.\n"
        "Gravity: running is heresy. But the data is consistent with both.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_01_four_forces_readings.png")


# ================================================================
# FIG 2: THE G MEASUREMENT SCATTER
# Type: Running/Convergence (scatter)
# Shows: 15 dots spread far wider than error bars
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

years = [1982, 1996, 1997, 2000, 2001, 2003, 2005, 2006, 2009, 2010,
         2013, 2014, 2018, 2018, 2022]
g_vals = [6.6726, 6.6729, 6.674, 6.6742, 6.6746, 6.6723, 6.6735,
          6.6743, 6.6738, 6.6730, 6.6745, 6.6755, 6.6749, 6.6726, 6.6743]
g_errs = [0.0005, 0.0005, 0.0007, 0.001, 0.001, 0.0009, 0.0004,
          0.001, 0.0003, 0.0003, 0.0001, 0.0001, 0.0002, 0.0002, 0.0002]
techniques = ['torsion', 'torsion', 'torsion', 'beam', 'beam', 'torsion', 'torsion',
              'beam', 'torsion', 'torsion', 'atom', 'atom', 'torsion', 'beam', 'atom']

tech_colors = {'torsion': CYAN, 'beam': GREEN, 'atom': ORANGE}

# CODATA band
codata_val = 6.6743
codata_unc = 0.00015
ax.axhspan(codata_val - codata_unc, codata_val + codata_unc, color=GOLD, alpha=0.1)
ax.axhline(y=codata_val, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(2023, codata_val + 0.0003, "CODATA 2022", ha='right', va='bottom',
        fontsize=8, color=GOLD)

for i in range(len(years)):
    tc = tech_colors[techniques[i]]
    ax.scatter([years[i]], [g_vals[i]], s=80, color=tc, zorder=5, marker='o')
    ax.plot([years[i], years[i]], [g_vals[i] - g_errs[i], g_vals[i] + g_errs[i]],
            color=tc, linewidth=1.5, alpha=0.7)

for tech, tcol in tech_colors.items():
    ax.scatter([], [], color=tcol, label=tech, s=60)
ax.legend(loc='lower left', fontsize=9, facecolor=PAN, labelcolor=WHITE)

ax.text(2000, 6.676, "Each lab: " + r"$\pm$15 ppm" + "\nTotal scatter: " + r"$\pm$500 ppm" +
        "\nScatter is 17" + r"$\times$" + " larger\nthan any individual uncertainty",
        ha='center', va='center', fontsize=9, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(2000, 6.671, "Electron g-2: 15 digits, same everywhere.\n"
        "G: 4 digits, different everywhere.",
        ha='center', va='center', fontsize=8, color=GOLD, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlabel("Year", fontsize=11, color=SILVER)
ax.set_ylabel(r"G ($\times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$)", fontsize=10, color=SILVER)
ax.set_title("Newton's G: The Constant That Can't Be Consistently Measured",
             fontsize=14, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(1978, 2026)
ax.set_ylim(6.670, 6.678)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_02_g_scatter.png")


# ================================================================
# FIG 3: MEASURING TEMPERATURE AT ONE DEPTH
# Type: Geometric Cross-Section (two panels)
# Shows: one thermometer vs five — insufficient sampling
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Ocean Analogy: One Depth, One Reading",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: what we do --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "What We Do", ha='center', va='center',
         fontsize=13, fontweight='bold', color=DIM)

# Ocean gradient
for band in range(20):
    y_bot = 1.5 + band * (6.0 / 20)
    frac = band / 20.0
    col = (0.1, 0.2 + 0.3 * (1 - frac), 0.5 + 0.4 * frac, 0.2)
    rect = mpatches.Rectangle((1.5, y_bot), 5.0, 6.0 / 20,
                               facecolor=col)
    ax1.add_patch(rect)

# Single thermometer
ax1.plot([5.0, 5.0], [4.5, 5.5], color=GOLD, linewidth=4)
ax1.scatter([5.0], [5.0], s=200, color=GOLD, zorder=5, marker='o')
ax1.text(6.5, 5.0, r"$G$ = 6.674" + r"$\times 10^{-11}$",
         ha='left', va='center', fontsize=9, color=GOLD, fontweight='bold')

ax1.text(5, 1.0, "One boundary.\nOne reading.\nDeclare it constant.",
         ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

# -- Right: what we'd need --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "What We'd Need", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GREEN)

# Same ocean
for band in range(20):
    y_bot = 1.5 + band * (6.0 / 20)
    frac = band / 20.0
    col = (0.1, 0.2 + 0.3 * (1 - frac), 0.5 + 0.4 * frac, 0.2)
    rect = mpatches.Rectangle((1.5, y_bot), 5.0, 6.0 / 20,
                               facecolor=col)
    ax2.add_patch(rect)

# Five thermometers at different depths
depths = [
    (7.0, "surface", GREEN),
    (6.0, "mid-upper", CYAN),
    (5.0, "middle", BLUE),
    (3.5, "deep", PURPLE),
    (2.5, "abyss", RED),
]
for dy, dlabel, dcol in depths:
    ax2.plot([4.5, 5.5], [dy, dy], color=dcol, linewidth=3)
    ax2.scatter([5.0], [dy], s=120, color=dcol, zorder=5, marker='o')
    ax2.text(6.5, dy, dlabel, ha='left', va='center', fontsize=8, color=dcol)

ax2.text(5, 1.0, "Multiple boundaries.\nMultiple readings.\nTHEN conclude constant\nor running.",
         ha='center', va='center', fontsize=9, color=GREEN, fontstyle='italic')

fig.text(0.5, 0.04, "Declaring G constant from one boundary is an assumption, not a measurement.",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk9_03_ocean_one_depth.png")


# ================================================================
# FIG 4: EVERYTHING DYNAMIC EXCEPT G
# Type: Comparison Bar
# Shows: four green bars (dynamic) + one red bar (fixed)
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

quantities = [r"Metric $g_{\mu\nu}$", r"Curvature $R_{\mu\nu}$",
              r"Energy-momentum $T_{\mu\nu}$", "Geodesics",
              r"$G$ (Newton's constant)"]
status = ["DYNAMIC:\nvaries with mass,\nenergy, motion",
          "DYNAMIC:\nvaries with metric",
          "DYNAMIC:\nvaries with matter",
          "DYNAMIC:\npaths curve",
          "FIXED:\ndeclared constant\neverywhere, always"]
bar_colors = [GREEN, GREEN, GREEN, GREEN, RED]
bar_vals = [1, 1, 1, 1, 1]

y = np.arange(len(quantities))

for i in range(len(quantities)):
    ax.barh(y[i], bar_vals[i], height=0.5, color=bar_colors[i], alpha=0.5)
    ax.text(0.05, y[i], quantities[i], ha='left', va='center',
            fontsize=10, color=WHITE, fontweight='bold')
    ax.text(1.1, y[i], status[i], ha='left', va='center',
            fontsize=8, color=bar_colors[i])

ax.set_title("In GR, Everything Varies Except the Coupling",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(0.7, -0.8, "Every other force resolved this: their couplings run.\n"
        "Gravity's coupling is declared fixed. Why?",
        ha='center', va='center', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 2.5)
ax.set_ylim(-1.3, 4.8)
ax.set_xticks([])
ax.set_yticks([])
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk9_04_everything_dynamic_except_g.png")


# ================================================================
# FIG 5: TWO INTERPRETATIONS OF THE SAME FORMULA
# Type: Comparison Bar (two panels)
# Shows: curved spacetime vs nested boundaries — same equation
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle(r"Same Formula: $\sqrt{1 - 2GM/rc^2}$    Two Meanings",
             fontsize=16, fontweight='bold', color=GOLD, y=0.96)

# -- Left: Standard GR --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Standard GR", ha='center', va='center',
         fontsize=13, fontweight='bold', color=CYAN)

# Curved grid
for gx in np.linspace(1, 9, 9):
    curve_y = np.linspace(3, 7, 50)
    curve_x = gx + 0.3 * np.sin((curve_y - 5) * 0.8) * (1 - abs(gx - 5) / 5)
    ax1.plot(curve_x, curve_y, color=CYAN, linewidth=0.5, alpha=0.3)
for gy in np.linspace(3, 7, 5):
    curve_x = np.linspace(1, 9, 50)
    curve_y2 = gy + 0.3 * np.sin((curve_x - 5) * 0.8) * (1 - abs(gy - 5) / 3)
    ax1.plot(curve_x, curve_y2, color=CYAN, linewidth=0.5, alpha=0.3)

# Clock icon
ax1.scatter([5], [5], s=200, color=WHITE, zorder=5, marker='o')
ax1.text(5, 5, "t", ha='center', va='center', fontsize=10, color=BG)

ax1.text(5, 2.0, "Spacetime is curved.\nClocks tick slower\nin curved regions.\nTime is a dimension.\nCurvature warps it.",
         ha='center', va='center', fontsize=9, color=CYAN, fontstyle='italic')

# -- Right: Reading Depth --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "Reading Depth", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Nested circles
for r, al in [(3.5, 0.06), (2.8, 0.08), (2.1, 0.1), (1.4, 0.15), (0.7, 0.2)]:
    circle = mpatches.Circle((5, 5), r, facecolor=GOLD, alpha=al,
                              linewidth=1, linestyle='--')
    ax2.add_patch(circle)

ax2.scatter([5], [5], s=200, color=WHITE, zorder=5, marker='o')
ax2.text(5, 5, "t", ha='center', va='center', fontsize=10, color=BG)

ax2.text(5, 2.0, "Position in the boundary\nstack determines clock rate.\nDeeper = more boundaries\n= slower reading.\nTime is depth, not dimension.",
         ha='center', va='center', fontsize=9, color=GOLD, fontstyle='italic')

fig.text(0.5, 0.04, "Same formula. Same GPS corrections. Same Mercury. Same Pound-Rebka.\n"
         "The difference: one testable prediction (sector splitting).",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk9_05_two_interpretations.png")


# ================================================================
# FIG 6: THE SOLITON HIERARCHY — DEPTH = CLOCK RATE
# Type: Geometric Cross-Section
# Shows: nested circles with color gradient and clock rates
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')

ax.text(0, 6.3, "Deeper in the Hierarchy = Slower Clock",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

levels = [
    (5.5, "Deep space", "1.000000000", DIM, 0.06),
    (4.5, "Solar system", "0.99999999", PURPLE, 0.08),
    (3.5, "Earth orbit (GPS)", "0.9999999993", BLUE, 0.1),
    (2.5, "Earth surface", "0.9999999986", GREEN, 0.12),
    (1.5, "Underground", "even slower", ORANGE, 0.15),
    (0.6, "Neutron star", "0.76", RED, 0.25),
]

for radius, name, clock_rate, col, al in levels:
    circle = mpatches.Circle((0, 0), radius, facecolor=col, alpha=al,
                              linewidth=1.5, linestyle='--')
    ax.add_patch(circle)

# Labels on right side — stagger vertically to avoid overlap
for i, (radius, name, clock_rate, col, al) in enumerate(levels):
    label_x = 3.5
    label_y = 5.0 - i * 1.5

    ax.text(label_x, label_y + 0.2, name, ha='left', va='center',
            fontsize=10, color=col, fontweight='bold')
    ax.text(label_x, label_y - 0.2, "clock: " + clock_rate, ha='left', va='center',
            fontsize=8, color=SILVER)

    # Leader line from circle edge to label
    edge_x = min(radius * 0.9, 3.2)
    ax.plot([edge_x, label_x - 0.2], [radius * 0.3 if i < 3 else -radius * 0.3, label_y],
            color=col, linewidth=0.5, alpha=0.4)

# GPS annotation
ax.text(-4.5, 2.5, "GPS clocks:\n38 " + r"$\mu$s/day" + "\nfaster than\nground",
        ha='center', va='center', fontsize=8, color=BLUE,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Arrow showing depth direction
ax.annotate("deeper = slower", xy=(0, -0.5), xytext=(0, 3.5),
            fontsize=10, color=GOLD, ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.text(0, -6.0, "Each boundary between you and the outside adds a correction.\n"
        "More boundaries = deeper = slower clock.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk9_06_soliton_depth_clock.png")


# ================================================================
# FIG 7: 18 TESTS ACROSS 60 ORDERS OF MAGNITUDE
# Type: Scale/Landscape
# Shows: comprehensive coverage with one red failure
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

tests = [
    ("Pound-Rebka", 1.35, "22.6 m tower", "0.06%", GREEN),
    ("Hafele-Keating", 4.0, "airplane", "0.02%", GREEN),
    ("Muon dilation", 4.5, "cosmic rays", "0.04%", GREEN),
    ("GPS", 7.3, "20,200 km orbit", "0.35%", GREEN),
    ("GPA", 7.0, "10,000 km sub-orbital", "2.47% FAIL", RED),
    ("Earth surface g", 6.8, "sea level", "0.14%", GREEN),
    ("Solar redshift", 8.7, "Sun surface", "16 ppm", GREEN),
    ("Mercury perihelion", 10.7, "orbit 46-70 Mkm", "2.8 ppm", GREEN),
    ("Cassini Shapiro", 12.0, "Saturn orbit", r"$\gamma$=1 exact", GREEN),
    ("Hulse-Taylor", 20.0, "binary pulsar", "42 ppm", GREEN),
    ("SN Ia redshift", 25.0, "z=0.5", "matches 1+z", GREEN),
    ("Planck length", 26.0, "from constants", "14.8 ppb", GREEN),
    ("c from Planck", 27.0, "fundamental", "0 ppm (9 digits)", GOLD),
]

# Sort by log scale
tests.sort(key=lambda t: t[1])

y_pos = np.arange(len(tests))
scales = [t[1] for t in tests]

for i, (name, scale, desc, miss, col) in enumerate(tests):
    ax.scatter([scale], [y_pos[i]], s=120, color=col, zorder=5, marker='o')
    ax.text(scale + 0.5, y_pos[i] + 0.15, name, ha='left', va='center',
            fontsize=8, color=col, fontweight='bold')
    ax.text(scale + 0.5, y_pos[i] - 0.2, miss, ha='left', va='center',
            fontsize=7, color=SILVER)

ax.set_xlabel(r"log$_{10}$(scale in meters)", fontsize=11, color=SILVER)
ax.set_title("18 GR Tests from a Tower to the Cosmos",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Range annotation
ax.annotate("60 orders of magnitude", xy=(1, -0.5), xytext=(27, -0.5),
            fontsize=10, color=GOLD,
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))

ax.text(15, 1, "One formula.\n17 PASS. 1 FAIL.\nWorks everywhere\nwe've tested.",
        ha='center', va='center', fontsize=10, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_yticks([])
ax.set_xlim(0, 30)
ax.set_ylim(-1.5, len(tests) + 0.5)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_07_18_tests_60_orders.png")


# ================================================================
# FIG 8: THE PRECISION CASCADE — BEST TO WORST
# Type: Comparison Bar
# Shows: smooth descent from ppb to percent with one FAIL
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

results_sorted = [
    ("c from Planck", 0.001, GOLD),
    ("Planck length", 0.015, GREEN),
    ("Mercury", 2.8, GREEN),
    ("Solar redshift", 16, GREEN),
    ("Hulse-Taylor", 42, GREEN),
    ("Muon dilation", 400, CYAN),
    ("Pound-Rebka", 600, CYAN),
    ("Earth g", 1400, CYAN),
    ("GPS", 3500, CYAN),
    ("GPA", 24700, RED),
]

y = np.arange(len(results_sorted))
vals = [r[1] for r in results_sorted]
names_r = [r[0] for r in results_sorted]
colors_r = [r[2] for r in results_sorted]

ax.barh(y, vals, height=0.5, color=colors_r, alpha=0.6)

for i in range(len(results_sorted)):
    val = vals[i]
    if val < 1:
        label = "%.3f ppm" % val
    elif val < 100:
        label = "%.1f ppm" % val
    elif val < 10000:
        label = "%.0f ppm (%.2f%%)" % (val, val / 10000)
    else:
        label = "%.0f ppm (%.1f%%) FAIL" % (val, val / 10000)

    ax.text(0.002, y[i], names_r[i], ha='left', va='center',
            fontsize=9, color=WHITE, fontweight='bold')
    ax.text(val * 1.3 if val > 1 else 0.05, y[i], label, ha='left', va='center',
            fontsize=8, color=colors_r[i])

ax.set_xscale('log')
ax.set_xlabel("Miss (ppm)", fontsize=11, color=SILVER)
ax.set_title("GR Test Precision: From PPB to Percent",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(50, 0.5, "Smooth degradation\nfrom ppb to percent.\nOne failure at the end.",
        ha='center', va='center', fontsize=9, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.0005, 50000)
ax.set_ylim(-0.8, len(results_sorted) - 0.2)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_08_precision_cascade.png")


# ================================================================
# FIG 9: THE GPA FAIL — ANATOMY
# Type: Threshold/Region
# Shows: predicted dot outside gate band — honest failure
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
ax.text(3.5, gate_hi + 0.003e-10, "1% gate", ha='center', va='bottom',
        fontsize=9, color=GREEN, alpha=0.7)

# Labels
ax.text(3.0, measured + 0.015e-10, "Measured: (4.36 " + r"$\pm$" + " 0.03)" + r"$\times 10^{-10}$",
        ha='center', va='bottom', fontsize=10, color=MAG)
ax.text(3.0, measured - 0.02e-10, "Vessot & Levine 1980\nSuborbital rocket, 1h55m",
        ha='center', va='top', fontsize=8, color=MAG)

# Predicted point
ax.scatter([1.5], [predicted], s=250, color=GOLD, zorder=5, marker='o')
ax.text(1.5, predicted - 0.025e-10, "Predicted: 4.252" + r"$\times 10^{-10}$" +
        "\nh = 10,000 km (round)",
        ha='center', va='top', fontsize=9, color=GOLD)

# Miss arrow
ax.annotate("2.47%\nFAIL", xy=(2.2, measured), xytext=(2.2, predicted),
            fontsize=12, color=RED, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))

# Hypotheses
hypotheses = [
    "1. Reference value rounded from 1976 paper",
    "2. Effective altitude was lower (suborbital trajectory)",
    "3. Genuine problem",
]
for i, hyp in enumerate(hypotheses):
    ax.text(3.0, 4.20e-10 - i * 0.015e-10, hyp, ha='center', va='center',
            fontsize=8, color=SILVER)

ax.text(3.0, 4.15e-10, "Don't know which.\n17 passes don't erase 1 failure.",
        ha='center', va='center', fontsize=9, color=RED, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.5, 4.5)
ax.set_ylim(4.14e-10, 4.43e-10)
ax.set_ylabel("Fractional frequency shift", fontsize=10, color=SILVER)
ax.set_xticks([])
ax.set_title("Gravity Probe A: The Unsolved Failure",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk9_09_gpa_fail.png")


# ================================================================
# FIG 10: D AND K — TWO COMPONENTS OF TIME DILATION
# Type: Connection/Integer Map
# Shows: one formula splitting into reading (D) and tick (K)
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 9)

ax.text(7, 8.3, "Separating the Reading from the Tick",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Input box (top center)
rounded_box(ax, 7, 6.5, 6, 1.5, "", GOLD, alpha=0.15)
ax.text(7, 7.0, "Observed time dilation", ha='center', va='center',
        fontsize=10, color=WHITE)
ax.text(7, 6.3, r"$\sqrt{1 - 2\Phi/c^2}$", ha='center', va='center',
        fontsize=16, color=GOLD, fontweight='bold')

# Branch arrows
ax.annotate("", xy=(3.5, 4.8), xytext=(5.5, 5.7),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))
ax.annotate("", xy=(10.5, 4.8), xytext=(8.5, 5.7),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2.5))

# D branch (left)
rounded_box(ax, 3.5, 3.5, 5.0, 2.5, "", CYAN, alpha=0.12)
ax.text(3.5, 4.4, "D (Reading Depth)", ha='center', va='center',
        fontsize=12, color=CYAN, fontweight='bold')
ax.text(3.5, 3.6, "Spatial position in\nthe soliton hierarchy.\nComputable at frozen time.\nHow deep you sit.", ha='center', va='center',
        fontsize=8, color=SILVER)
ax.text(3.5, 2.5, "89% of all GR effects\nare pure D", ha='center', va='center',
        fontsize=9, color=CYAN, fontweight='bold')

# K branch (right)
rounded_box(ax, 10.5, 3.5, 5.0, 2.5, "", ORANGE, alpha=0.12)
ax.text(10.5, 4.4, "K (Tick)", ha='center', va='center',
        fontsize=12, color=ORANGE, fontweight='bold')
ax.text(10.5, 3.6, "The Planck-scale heartbeat.\nMonotonic counter.\nWhat makes things happen.", ha='center', va='center',
        fontsize=8, color=SILVER)
ax.text(10.5, 2.5, "1 observable is pure K:\nthe muon lifetime", ha='center', va='center',
        fontsize=9, color=ORANGE, fontweight='bold')

# Merge note at bottom
ax.text(7, 0.8, "Standard GR: D + K inseparable, one formula.\n"
        "Reading depth: they might be separable.\n"
        "If separable: different forces contribute differently to D.\n"
        "A nuclear clock and an optical clock would show slightly different\ndilation in the same potential.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN))

# Sector splitting callout
ax.text(7, -0.7, "This is the sector splitting prediction. Testable 2028-2032.",
        ha='center', va='center', fontsize=10, color=GOLD, fontweight='bold')

save(fig, "talk9_10_d_and_k_decomposition.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 9, 1-10) generated ===")
filenames = [
    "talk9_01_four_forces_readings.png",
    "talk9_02_g_scatter.png",
    "talk9_03_ocean_one_depth.png",
    "talk9_04_everything_dynamic_except_g.png",
    "talk9_05_two_interpretations.png",
    "talk9_06_soliton_depth_clock.png",
    "talk9_07_18_tests_60_orders.png",
    "talk9_08_precision_cascade.png",
    "talk9_09_gpa_fail.png",
    "talk9_10_d_and_k_decomposition.png",
]
for f in filenames:
    print("  %s" % f)
    