#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 3, Slides 21-30
10 figures covering: CKM matrix deficit, CKM deficit over time,
galaxy toroid, dark matter budget, cosmic budget, flatness,
12-layer stack, vocabulary matrix, self-similarity, closing card.
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
# FIG 21: CKM MATRIX — THE MISSING PROBABILITY
# Type: Connection/Integer Map (grid)
# Shows: 3x3 matrix with deficit, 4th column restores unitarity
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1.5, 10)

ax.text(7, 9.3, "Quark Mixing: The Missing Probability",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column and row headers
col_headers = ["d", "s", "b", "CD?", "Sum"]
row_headers = ["u", "c", "t"]

# CKM squared values (row 1 is the interesting one)
grid = [
    [0.9483, 0.0503, 0.0000146, 0.00152, None],
    [0.0503, 0.9465, 0.00170, None, None],
    [0.0000081, 0.00164, 0.9991, None, None],
]

sums = [0.99848, 0.9985, 1.0007]
sums_with_cd = [1.00000, None, None]

cell_w = 2.2
cell_h = 1.3
x_off = 2.0
y_off = 3.5

# Column headers
for j, ch in enumerate(col_headers):
    cx = x_off + j * cell_w + cell_w / 2
    col_color = GOLD if j == 3 else (GREEN if j < 3 else SILVER)
    ax.text(cx, y_off + 3 * cell_h + 0.5, ch, ha='center', va='center',
            fontsize=12, color=col_color, fontweight='bold')

# Row headers
for i, rh in enumerate(row_headers):
    ry = y_off + (2 - i) * cell_h + cell_h / 2
    ax.text(x_off - 0.5, ry, rh, ha='center', va='center',
            fontsize=12, color=WHITE, fontweight='bold')

# Grid cells
for i in range(3):
    for j in range(5):
        cx = x_off + j * cell_w
        cy = y_off + (2 - i) * cell_h
        val = None

        if j < 3:
            val = grid[i][j]
            cell_col = GREEN
            cell_alpha = 0.12
        elif j == 3:
            if i == 0:
                val = grid[0][3]
                cell_col = GOLD
                cell_alpha = 0.2
            else:
                cell_col = DIM
                cell_alpha = 0.05
                val = None
        elif j == 4:
            if i == 0:
                cell_col = ORANGE
                cell_alpha = 0.15
            else:
                cell_col = GREEN
                cell_alpha = 0.08

        rect = mpatches.FancyBboxPatch((cx, cy), cell_w, cell_h,
            boxstyle="round,pad=0.05", facecolor=cell_col, alpha=cell_alpha,
            linewidth=0.5)
        ax.add_patch(rect)

        tcx = cx + cell_w / 2
        tcy = cy + cell_h / 2

        if j < 3 and val is not None:
            if val < 0.001:
                txt = "%.1e" % val
            else:
                txt = "%.4f" % val
            ax.text(tcx, tcy, txt, ha='center', va='center',
                    fontsize=9, color=WHITE)
        elif j == 3 and i == 0:
            ax.text(tcx, tcy, "0.00152", ha='center', va='center',
                    fontsize=10, color=GOLD, fontweight='bold')
        elif j == 4:
            if i == 0:
                ax.text(tcx, tcy + 0.2, "0.99848", ha='center', va='center',
                        fontsize=9, color=ORANGE)
                ax.text(tcx, tcy - 0.25, r"$\rightarrow$ 1.00000", ha='center', va='center',
                        fontsize=9, color=GREEN, fontweight='bold')
            elif i == 1:
                ax.text(tcx, tcy, "~1.000", ha='center', va='center',
                        fontsize=9, color=GREEN)
            elif i == 2:
                ax.text(tcx, tcy, "~1.000", ha='center', va='center',
                        fontsize=9, color=GREEN)

# Annotations
ax.text(7, 1.5, "The first row has been 2.5" + r"$\sigma$" + " below 1 for over a decade.\n"
        "The CD provides the leak.\n"
        "Required mixing angle: 2.6" + r"$^\circ$" + " " + r"$-$" + " typical, not anomalous.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

# Highlight the deficit
ax.annotate("DEFICIT", xy=(x_off + 4 * cell_w + cell_w/2, y_off + 2*cell_h + cell_h/2),
            xytext=(13, 7.5), fontsize=10, color=ORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

ax.annotate("CD fixes it", xy=(x_off + 3 * cell_w + cell_w/2, y_off + 2*cell_h + cell_h/2),
            xytext=(13, 6.5), fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

save(fig, "talk3_21_ckm_deficit.png")


# ================================================================
# FIG 22: CKM DEFICIT OVER TIME
# Type: Running/Convergence
# Shows: decade of measurements all below unitarity line
# ================================================================
fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Approximate historical values of first-row unitarity sum
years = [2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
values = [0.9990, 0.9986, 0.9985, 0.9984, 0.9985, 0.9984, 0.9985, 0.9984,
          0.9985, 0.9985, 0.9985, 0.9985]
errors = [0.0008, 0.0006, 0.0005, 0.0005, 0.0004, 0.0004, 0.0004, 0.0003,
          0.0003, 0.0003, 0.0003, 0.0002]

# Unitarity line
ax.axhline(y=1.0, color=GOLD, linewidth=2, linestyle='--', alpha=0.6)
ax.text(2024.5, 1.0003, "Unitarity (probability = 1)", ha='right', va='bottom',
        fontsize=10, color=GOLD)

# Data points with error bars
ax.scatter(years, values, s=120, color=ORANGE, zorder=5, marker='o')
for i in range(len(years)):
    ax.plot([years[i], years[i]], [values[i] - errors[i], values[i] + errors[i]],
            color=ORANGE, linewidth=1.5, alpha=0.7)

# Trend band
ax.axhspan(0.9983, 0.9987, color=ORANGE, alpha=0.06)

# CD restoration level
ax.axhline(y=0.99848, color=MAG, linewidth=1, linestyle=':', alpha=0.5)
ax.text(2003, 0.99835, "Measured: 0.99848", ha='left', va='center',
        fontsize=9, color=MAG)

ax.set_xlabel("Year", fontsize=11, color=SILVER)
ax.set_ylabel(r"|V$_{ud}$|$^2$ + |V$_{us}$|$^2$ + |V$_{ub}$|$^2$",
              fontsize=11, color=SILVER)
ax.set_title("The CKM First-Row Deficit: It Never Goes Away",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(2013, 0.9977, "Measured more precisely each year.\n"
        "The deficit persists. It's not going away.\n"
        "The CD explains it: " + r"|V$_{u4}$|$^2$ = 0.00152",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(2000, 2026)
ax.set_ylim(0.9970, 1.0010)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_22_ckm_deficit_timeline.png")


# ================================================================
# FIG 23: THE GALAXY — NOT A SPHERE, A DONUT
# Type: Geometric Cross-Section (two panels)
# Shows: face-on view vs toroidal cross-section
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 12),
                                gridspec_kw={'wspace': 0.25})
fig.patch.set_facecolor(BG)
fig.suptitle("The Milky Way: A Toroid, Not a Sphere",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: face-on spiral --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(-6, 6)
ax1.set_ylim(-6, 6)
ax1.set_aspect('equal')

ax1.text(0, 5.3, "Face-on View", ha='center', va='center',
         fontsize=13, fontweight='bold', color=SILVER)

# Disc
disc = mpatches.Circle((0, 0), 4.0, facecolor=PURPLE, alpha=0.15, linewidth=1)
ax1.add_patch(disc)

# Spiral arms (simplified)
for arm_offset in [0, np.pi/2, np.pi, 3*np.pi/2]:
    theta = np.linspace(0.3, 2.5, 100) + arm_offset
    r = 0.8 + theta * 0.9
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    mask = r < 4.0
    ax1.plot(x[mask], y[mask], color=PURPLE, linewidth=1.5, alpha=0.4)

# Center bulge
bulge = mpatches.Circle((0, 0), 0.6, facecolor=GOLD, alpha=0.3)
ax1.add_patch(bulge)

ax1.text(0, -5.0, "What you see:\na flat disc with spiral arms",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

# -- Right: toroidal cross-section --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(-6, 6)
ax2.set_ylim(-6, 6)
ax2.set_aspect('equal')

ax2.text(0, 5.3, "Cross-Section (Edge-on)", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Toroidal cross-section: two circles (left and right lobes of the donut)
for side in [-1, 1]:
    lobe = mpatches.Circle((side * 2.5, 0), 2.0, facecolor=PURPLE, alpha=0.1,
                            linewidth=1.5, linestyle='--')
    ax2.add_patch(lobe)

    # Flow arrows around each lobe
    angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
    for a in angles:
        ax = 2.5 * side + 1.5 * np.cos(a)
        ay = 1.5 * np.sin(a)
        dx = -0.4 * np.sin(a) * side
        dy = 0.4 * np.cos(a) * side
        ax2.annotate("", xy=(ax + dx, ay + dy), xytext=(ax, ay),
                     arrowprops=dict(arrowstyle='->', color=CYAN, lw=1, alpha=0.5))

# Disc in center (thin horizontal bar)
ax2.plot([-0.8, 0.8], [0, 0], color=GOLD, linewidth=4, alpha=0.6)
ax2.text(0, -0.5, "disc", ha='center', va='center', fontsize=8, color=GOLD)

# Labels
ax2.text(-2.5, -3.5, "halo\n(return flow)", ha='center', va='center',
         fontsize=9, color=CYAN)
ax2.text(2.5, -3.5, "halo\n(return flow)", ha='center', va='center',
         fontsize=9, color=CYAN)

ax2.text(0, -5.0, "What's really there:\na toroidal flow pattern.\nThe halo is the return flow.",
         ha='center', va='center', fontsize=10, color=GOLD, fontstyle='italic')

# Bottom annotation
fig.text(0.5, 0.03, "Dark matter isn't particles. It's the gravitational energy of this circulation.\n"
         "The (22/13)" + r"$\pi$" + " ratio measures how much energy is in the flow vs the disc.",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk3_23_galaxy_toroid.png")


# ================================================================
# FIG 24: THE DARK MATTER BUDGET
# Type: Comparison Bar (stacked)
# Shows: visible 16% vs dark 84%, ratio = (22/13)pi
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Stacked horizontal bar
visible = 15.8
dark = 84.2

ax.barh(1, visible, height=0.5, color=CYAN, alpha=0.7, left=0)
ax.barh(1, dark, height=0.5, color=PURPLE, alpha=0.7, left=visible)

# Labels inside bars
ax.text(visible / 2, 1, "Visible matter\n%.1f%%" % visible, ha='center', va='center',
        fontsize=11, color=WHITE, fontweight='bold')
ax.text(visible + dark / 2, 1, "Dark matter (circulation energy)\n%.1f%%" % dark,
        ha='center', va='center', fontsize=11, color=WHITE, fontweight='bold')

# Ratio annotation
ax.text(50, 0.2, "Ratio: 84.2 / 15.8  " + r"$\approx$" + "  5.32  " + r"$\approx$" +
        "  (22/13)" + r"$\pi$" + "  =  5.317", ha='center', va='center',
        fontsize=13, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

# Decomposition below
ax.barh(-0.3, 1, height=0.3, color=CYAN, alpha=0.5, left=0)
ax.text(0.5, -0.3, "1", ha='center', va='center', fontsize=10, color=WHITE)

ax.barh(-0.3, 5.32, height=0.3, color=PURPLE, alpha=0.5, left=2)
ax.text(2 + 5.32/2, -0.3, "(22/13)" + r"$\pi$" + " = 5.32", ha='center', va='center',
        fontsize=10, color=WHITE)

ax.text(0, -0.8, "Disc: 1 part", ha='left', va='center', fontsize=9, color=CYAN)
ax.text(4, -0.8, "Flow: 5.32 parts", ha='center', va='center', fontsize=9, color=PURPLE)
ax.text(8, -0.8, "Total: 6.32 parts", ha='center', va='center', fontsize=9, color=SILVER)

ax.set_title("Where the Galaxy's Gravity Comes From",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(-1, 105)
ax.set_ylim(-1.2, 1.8)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk3_24_dark_matter_budget.png")


# ================================================================
# FIG 25: COSMIC BUDGET — 4.9 + 26.1 + 69.0 = 100.0
# Type: Comparison Bar (stacked to 100%)
# Shows: three segments summing exactly to 100%
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

segments = [
    (4.9, "Ordinary matter\n4.9%", CYAN, "Atoms, stars,\nplanets, you"),
    (26.1, "Dark matter\n26.1%", PURPLE, "Toroidal\ncirculation energy"),
    (69.0, "Dark energy\n69.0%", ORANGE, "Derived: 69.03%\nMeasured: 68.89%\nMiss: 0.20%"),
]

left = 0
for width, label, col, note in segments:
    ax.barh(1, width, height=0.6, color=col, alpha=0.6, left=left)
    ax.text(left + width / 2, 1, label, ha='center', va='center',
            fontsize=10 if width > 10 else 8, color=WHITE, fontweight='bold')
    ax.text(left + width / 2, 0.3, note, ha='center', va='center',
            fontsize=8, color=SILVER)
    left += width

# Total annotation
ax.text(50, 1.7, "Total: 4.9 + 26.1 + 69.0 = 100.0%", ha='center', va='center',
        fontsize=13, color=GOLD, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.text(50, -0.3, "Flat. Not a coincidence.\n"
        "The inside of a soliton always reads flat.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_title("The Universe's Energy Budget: Exactly 100%",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(-2, 105)
ax.set_ylim(-0.8, 2.2)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax.set_xticklabels(["0%", "", "20%", "", "40%", "50%", "60%", "", "80%", "", "100%"],
                   fontsize=9, color=DIM)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)

save(fig, "talk3_25_cosmic_budget.png")


# ================================================================
# FIG 26: WHY THE UNIVERSE IS FLAT
# Type: Geometric Cross-Section (two panels)
# Shows: "mystery" view vs "obvious once inside" view
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Flat Is Not Fine-Tuned. Flat Is Inside.",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: standard "mystery" view --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Standard View", ha='center', va='center',
         fontsize=13, fontweight='bold', color=DIM)

# Curved surface
curve_x = np.linspace(1, 9, 100)
curve_y = 5.5 + 1.5 * np.sin((curve_x - 5) * 0.5)
ax1.plot(curve_x, curve_y, color=DIM, linewidth=2)
ax1.fill_between(curve_x, curve_y, 4.0, color=DIM, alpha=0.05)

ax1.text(5, 7.5, r"$\Omega$ = 1.0000...", ha='center', va='center',
         fontsize=14, color=DIM, fontweight='bold')

ax1.text(5, 3.5, "Why so precisely 1?", ha='center', va='center',
         fontsize=12, color=RED)
ax1.text(5, 2.5, "Fine-tuning?", ha='center', va='center',
         fontsize=11, color=RED, fontstyle='italic')
ax1.text(5, 1.7, "Inflation?", ha='center', va='center',
         fontsize=11, color=RED, fontstyle='italic')
ax1.text(5, 0.9, "???", ha='center', va='center',
         fontsize=14, color=RED, fontweight='bold')

# -- Right: RUM "obvious" view --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "RUM View", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Sphere with observer inside
sphere = mpatches.Circle((5, 5), 3.5, facecolor=GREEN, alpha=0.06,
                          linewidth=2, linestyle='--')
ax2.add_patch(sphere)

# Flat grid inside
for gx in np.linspace(2, 8, 7):
    ax2.plot([gx, gx], [3.0, 7.0], color=GREEN, linewidth=0.5, alpha=0.3)
for gy in np.linspace(3, 7, 5):
    ax2.plot([2, 8], [gy, gy], color=GREEN, linewidth=0.5, alpha=0.3)

# Observer
ax2.scatter([5], [5], s=100, color=WHITE, zorder=5, marker='o')
ax2.text(5.5, 4.5, "you are\nhere", ha='left', va='center', fontsize=8, color=WHITE)

ax2.text(5, 7.8, "Inside reads FLAT", ha='center', va='center',
         fontsize=12, color=GREEN, fontweight='bold')
ax2.text(5, 2.0, "Outside reads CURVED", ha='center', va='center',
         fontsize=10, color=CYAN)

ax2.text(5, 0.8, "Same as standing on Earth:\nflat. Same as inside an atom:\nflat. Boundaries do this.",
         ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic')

fig.text(0.5, 0.03, "The flatness problem dissolves. It's not a coincidence. It's what boundaries do.",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk3_26_flatness.png")


# ================================================================
# FIG 27: THE COMPLETE 12-LAYER STACK
# Type: Scale/Landscape (vertical)
# Shows: all 12 layers from vacuum to universe in one view
# ================================================================
fig, ax = plt.subplots(figsize=(16, 16))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 14)

ax.text(7, 13.3, "The Physics Stack: Vacuum to Universe",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

layers = [
    ("0. Vacuum", r"$10^{-30}$ g/cm$^3$", "Ground state", DIM),
    ("1. Quantum Fields", "SU(3)" + r"$\times$" + "SU(2)" + r"$\times$" + "U(1)", "17 fields", SILVER),
    ("2. Stable Patterns", "e, p, n", "Permanent vortices", CYAN),
    ("3. Boundary Readings", r"$\alpha_s$=1 inside, 0.118 outside", "Confinement, EW, GUT", GREEN),
    ("4. The Running", r"$\beta$=41/10, $-$19/6, $-$7", "Forces change with scale", BLUE),
    ("5. Cabibbo Doublet", r"$\Delta\beta$=(1/15, 1, 1/3)", "One particle", GOLD),
    ("6. Electroweak", "3 in " + r"$\rightarrow$" + " 15 out", r"$M_W$, $\Gamma_Z$, widths", CYAN),
    ("7. QED Chain", r"$\alpha$ at 12 digits", "H 1S-2S at 11 digits", GREEN),
    ("8. Cosmo Chain", "integers " + r"$\rightarrow$" + " deuterium", "7 steps, 5 domains", PURPLE),
    ("9. Muon", "g-2 tension", "Same answer as SM", ORANGE),
    ("10. Flavor", "CKM deficit", "CD provides the leak", MAG),
    ("11. Galaxy", "(22/13)" + r"$\pi$", "Toroidal DM", PURPLE),
    ("12. Universe", "4.9+26.1+69.0=100", "Flat", GOLD),
]

for i, (name, key_num, desc, col) in enumerate(layers):
    y = 0.3 + i * 0.95
    bar_w = 12.0

    rect = mpatches.FancyBboxPatch((1.0, y), bar_w, 0.7,
        boxstyle="round,pad=0.08", facecolor=col, alpha=0.12,
        linewidth=1)
    ax.add_patch(rect)

    ax.text(1.3, y + 0.35, name, ha='left', va='center', fontsize=9,
            color=col, fontweight='bold')
    ax.text(6.5, y + 0.35, key_num, ha='center', va='center', fontsize=8,
            color=WHITE)
    ax.text(12.5, y + 0.35, desc, ha='right', va='center', fontsize=8,
            color=SILVER)

save(fig, "talk3_27_twelve_layer_stack.png")


# ================================================================
# FIG 28: ONE VOCABULARY, EVERY LAYER
# Type: Comparison Bar (matrix)
# Shows: same three nouns at every layer — repetition IS the point
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 11)

ax.text(7, 10.3, "Same Three Nouns at Every Layer",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Column headers
col_headers = ["Layer", "Inertia\n(resists)", "Vortex\n(circulates)", "Soliton\n(boundary)"]
col_x = [1.5, 5.0, 8.5, 12.0]

for j, (ch, cx) in enumerate(zip(col_headers, col_x)):
    col_col = [WHITE, ORANGE, CYAN, GREEN][j]
    ax.text(cx, 9.5, ch, ha='center', va='center', fontsize=10,
            color=col_col, fontweight='bold')

# Selected layers with concrete examples
rows = [
    ("Proton", "938.3 MeV", "gluon flux", "confinement"),
    ("Atom", "938.8 MeV", "electron orbit", "electron shell"),
    ("Molecule", "~100 amu", "bond vibration", "molecular surface"),
    ("Cell", r"~10$^{-12}$ kg", "metabolism", "membrane"),
    ("Planet", r"6$\times 10^{24}$ kg", "convection", "Hill sphere"),
    ("Star", r"2$\times 10^{30}$ kg", "fusion core", "photosphere"),
    ("Galaxy", r"~10$^{42}$ kg", "toroidal flow", "virial radius"),
    ("Universe", r"~10$^{53}$ kg", "expansion", "particle horizon"),
]

for i, (layer, inertia, vortex, soliton) in enumerate(rows):
    y = 8.3 - i * 1.05
    vals = [layer, inertia, vortex, soliton]
    cols = [WHITE, ORANGE, CYAN, GREEN]

    for j in range(4):
        ax.text(col_x[j], y, vals[j], ha='center', va='center',
                fontsize=9, color=cols[j])

    # Subtle row separator
    ax.plot([0.5, 14], [y - 0.45, y - 0.45], color=DIM, linewidth=0.3, alpha=0.3)

ax.text(7, -0.2, "Three nouns. Eight layers shown. The same vocabulary works everywhere\n"
        "because the same structure repeats everywhere.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk3_28_vocabulary_matrix.png")


# ================================================================
# FIG 29: THE PATTERN — SAME STRUCTURE AT EVERY SCALE
# Type: Geometric Cross-Section
# Shows: four nested circles with identical structure, different scales
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-2, 7)

ax.text(8, 6.3, "The Same Pattern Repeats at Every Scale",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Four circles at different positions, same structure
structures = [
    (2.0, 2.5, 1.8, "Proton", r"$\alpha_s$ changes\nat boundary", r"$10^{-15}$ m", RED),
    (6.0, 2.5, 1.8, "Atom", r"$\alpha_{em}$ sets\nthe reading", r"$10^{-10}$ m", BLUE),
    (10.0, 2.5, 1.8, "Star", r"$\Phi/c^2$ sets\nthe reading", r"$10^{9}$ m", ORANGE),
    (14.0, 2.5, 1.8, "Galaxy", "(22/13)" + r"$\pi$" + "\namplification", r"$10^{21}$ m", PURPLE),
]

for sx, sy, sr, sname, sreading, sscale, scol in structures:
    # Outer boundary
    outer = mpatches.Circle((sx, sy), sr, facecolor=scol, alpha=0.08,
                             linewidth=2, linestyle='--')
    ax.add_patch(outer)

    # Inner region
    inner = mpatches.Circle((sx, sy), sr * 0.4, facecolor=scol, alpha=0.2)
    ax.add_patch(inner)

    # Boundary ring
    ring = mpatches.Circle((sx, sy), sr * 0.7, facecolor='none',
                            linewidth=2, linestyle='-')
    ax.add_patch(ring)

    # Labels
    ax.text(sx, sy + sr + 0.5, sname, ha='center', va='center', fontsize=12,
            color=scol, fontweight='bold')
    ax.text(sx, sy, sreading, ha='center', va='center', fontsize=7,
            color=SILVER)
    ax.text(sx, sy - sr - 0.4, sscale, ha='center', va='center', fontsize=8,
            color=DIM)

# Connecting arrows showing "same pattern"
for i in range(3):
    ax.annotate("", xy=(structures[i+1][0] - 2.0, 2.5),
                xytext=(structures[i][0] + 2.0, 2.5),
                arrowprops=dict(arrowstyle='<->', color=DIM, lw=1, alpha=0.3))

ax.text(8, -1.0, "Why does it repeat? Because soliton boundary mathematics is scale-independent.\n"
        "Same equation at different sizes gives same structure at different readings.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk3_29_self_similarity.png")


# ================================================================
# FIG 30: CHECK THE NUMBERS — CLOSING CARD
# Type: Identity Card
# Shows: complete reference with key numbers and links
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 10)

ax.text(5, 9.2, "The Complete Reference", ha='center', va='center',
        fontsize=20, fontweight='bold', color=GOLD)

# Stats rows
stats = [
    ("13 inputs " + r"$\rightarrow$" + " 53 outputs " + r"$\rightarrow$" +
     " 9 domains " + r"$\rightarrow$" + " 253 comparisons", WHITE),
    (r"Best: $\alpha^{-1}$ at 0.007 ppb.    Worst: DM/baryon at 725 ppm.", SILVER),
    ("Honest failures: lithium (inherited), proton mass (one-loop), Hubble (killed)", SILVER),
    ("Prediction: Cabibbo Doublet. Test: Hyper-K proton decay, 2027+", ORANGE),
    ("Prediction: sector splitting. Test: Th-229 nuclear clock, 2028-2032", ORANGE),
]

for i, (txt, col) in enumerate(stats):
    ax.text(5, 7.5 - i * 0.9, txt, ha='center', va='center',
            fontsize=10, color=col)

# Resource boxes
resources = [
    (2.0, 3.0, "Code", "github.com/ghowland/rum", CYAN),
    (5.0, 3.0, "Papers", "zenodo.org (45+ papers)", GREEN),
    (8.0, 3.0, "Book", "The Rational Universe\namazon.com " + r"$-$" + " $3", GOLD),
]

for rx, ry, rlabel, rdetail, rcol in resources:
    rounded_box(ax, rx, ry, 2.4, 1.2, "", rcol, alpha=0.15)
    ax.text(rx, ry + 0.2, rlabel, ha='center', va='center', fontsize=12,
            color=rcol, fontweight='bold')
    ax.text(rx, ry - 0.25, rdetail, ha='center', va='center', fontsize=8,
            color=SILVER)

# Closing statement
ax.text(5, 1.2, "If the numbers are wrong, the model is wrong.\n"
        "If the numbers are right, the model deserves attention\n"
        "regardless of who produced it.",
        ha='center', va='center', fontsize=12, color=WHITE, fontstyle='italic',
        linespacing=1.6)

ax.text(5, -0.2, "The universe does not care about credentials. It cares about integers.",
        ha='center', va='center', fontsize=10, color=DIM)

save(fig, "talk3_30_closing_card.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 3, 21-30) generated ===")
filenames = [
    "talk3_21_ckm_deficit.png",
    "talk3_22_ckm_deficit_timeline.png",
    "talk3_23_galaxy_toroid.png",
    "talk3_24_dark_matter_budget.png",
    "talk3_25_cosmic_budget.png",
    "talk3_26_flatness.png",
    "talk3_27_twelve_layer_stack.png",
    "talk3_28_vocabulary_matrix.png",
    "talk3_29_self_similarity.png",
    "talk3_30_closing_card.png",
]
for f in filenames:
    print("  %s" % f)
    