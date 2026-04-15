#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 2, Slides 1-10
10 figures covering: gap ratio fraction vs decimal, unification dual view,
precision cliff, Q335 pi digits, four forces vs four readings,
thermometer analogy, five-department chain, citation matrix,
alphabet barrier, person-names vs descriptive names.
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
# FIG 1: THE GAP RATIO — FRACTION VS DECIMAL
# Type: Comparison Bar (side by side panels)
# Shows: rich structure in fraction vs empty gray in decimal
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)
fig.suptitle("The Same Number in Two Languages", fontsize=17,
             fontweight='bold', color=GOLD, y=0.96)

# -- Left panel: fraction --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.2, "As a Fraction", ha='center', va='center',
         fontsize=14, fontweight='bold', color=CYAN)

ax1.text(5, 7.5, "38 / 27", ha='center', va='center',
         fontsize=36, fontweight='bold', color=GOLD)

# Factorization tree for 38
ax1.text(2.5, 5.8, "38", ha='center', va='center', fontsize=16,
         color=GOLD, fontweight='bold')
ax1.plot([2.5, 1.5], [5.5, 4.8], color=DIM, linewidth=1)
ax1.plot([2.5, 3.5], [5.5, 4.8], color=DIM, linewidth=1)
ax1.text(1.5, 4.5, "2", ha='center', va='center', fontsize=14,
         color=CYAN, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor=PAN, edgecolor=CYAN, alpha=0.5))
ax1.text(3.5, 4.5, "19", ha='center', va='center', fontsize=14,
         color=CYAN, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor=PAN, edgecolor=CYAN, alpha=0.5))
ax1.text(1.5, 3.5, "vector-like\n(both hands)", ha='center', va='center',
         fontsize=8, color=GREEN)
ax1.text(3.5, 3.5, "weak force\ncount", ha='center', va='center',
         fontsize=8, color=GREEN)

# Factorization tree for 27
ax1.text(7.5, 5.8, "27", ha='center', va='center', fontsize=16,
         color=GOLD, fontweight='bold')
ax1.plot([7.5, 7.5], [5.5, 4.8], color=DIM, linewidth=1)
ax1.text(7.5, 4.5, r"$3^3$", ha='center', va='center', fontsize=14,
         color=CYAN, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor=PAN, edgecolor=CYAN, alpha=0.5))
ax1.text(7.5, 3.5, "color charges\ncubed", ha='center', va='center',
         fontsize=8, color=GREEN)

ax1.text(5, 2.0, "Every integer has a name.\nEvery factor counts something physical.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

# -- Right panel: decimal --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.2, "As a Decimal", ha='center', va='center',
         fontsize=14, fontweight='bold', color=DIM)

ax2.text(5, 7.5, "1.40741...", ha='center', va='center',
         fontsize=36, fontweight='bold', color=DIM)

ax2.text(5, 5.0, "Counts nothing.\nConnects to nothing.\nFactors into nothing.",
         ha='center', va='center', fontsize=12, color=DIM, fontstyle='italic')

ax2.text(5, 2.0, "The physics is gone.\nThe decimal is a corpse.",
         ha='center', va='center', fontsize=10, color=DIM, fontstyle='italic')

save(fig, "talk2_01_gap_ratio_fraction_vs_decimal.png")


# ================================================================
# FIG 2: UNIFICATION — VISIBLE IN FRACTIONS, INVISIBLE IN DECIMALS
# Type: Running/Convergence (dual panel)
# Shows: same data looking meaningless vs profound
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Unification: Why Decimals Miss It", fontsize=17,
             fontweight='bold', color=GOLD, y=0.96)

log_mz = np.log10(91.2)
log_gut_sm = 13.82
log_gut_cd = 15.61

t_sm = np.linspace(log_mz, log_gut_sm + 1, 200)
t_cd = np.linspace(log_mz, log_gut_cd + 1, 200)

# SM couplings (approximate running for visual)
a1_sm = 59.0 + (t_sm - log_mz) * 0.53
a2_sm = 29.6 - (t_sm - log_mz) * 0.85
a3_sm = 8.5 - (t_sm - log_mz) * 0.70

# CD couplings
a1_cd = 59.0 + (t_cd - log_mz) * 0.46
a2_cd = 29.6 - (t_cd - log_mz) * 0.56
a3_cd = 8.5 - (t_cd - log_mz) * 0.58

for axp, title, t, a1, a2, a3, log_gut, bright, gap_label in [
    (ax1, "Decimal View", t_sm, a1_sm, a2_sm, a3_sm, log_gut_sm, False, "gap ~ 5.88\ncoincidence?"),
    (ax2, "Fraction View", t_cd, a1_cd, a2_cd, a3_cd, log_gut_cd, True, "gap = 38/27\nexact fraction"),
]:
    axp.set_facecolor(PAN)
    lw = 2.5 if bright else 1.5
    al = 1.0 if bright else 0.4
    b_col = BLUE if bright else DIM
    g_col = GREEN if bright else DIM
    r_col = RED if bright else DIM

    axp.plot(t, a1, color=b_col, linewidth=lw, alpha=al, label=r"$\alpha_1^{-1}$ (U(1))")
    axp.plot(t, a2, color=g_col, linewidth=lw, alpha=al, label=r"$\alpha_2^{-1}$ (SU(2))")
    axp.plot(t, a3, color=r_col, linewidth=lw, alpha=al, label=r"$\alpha_3^{-1}$ (SU(3))")

    axp.set_xlabel("log(E / GeV)", fontsize=10, color=SILVER)
    axp.set_ylabel(r"$\alpha_i^{-1}$", fontsize=10, color=SILVER)
    axp.set_title(title, fontsize=13, fontweight='bold',
                  color=WHITE if bright else DIM, pad=10)

    # Gap annotation
    gap_col = GOLD if bright else DIM
    axp.axvline(x=log_gut, color=gap_col, alpha=0.5, linestyle='--', linewidth=1)
    axp.text(log_gut + 0.3, 45, gap_label, fontsize=9, color=gap_col,
             ha='left', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=gap_col, alpha=0.7))

    if bright:
        axp.scatter([log_gut_cd], [42.1], s=200, color=GOLD, edgecolors=WHITE,
                    linewidth=2, zorder=10, marker='*')

    axp.legend(loc='upper left', fontsize=8, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)
    axp.set_xlim(log_mz - 0.5, 18)
    axp.set_ylim(0, 70)
    for spine in axp.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    axp.tick_params(colors=DIM)

save(fig, "talk2_02_unification_decimal_vs_fraction.png")


# ================================================================
# FIG 3: THE PRECISION CLIFF
# Type: Scale/Landscape
# Shows: Q335 extends 65 digits past the Planck wall
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Segmented bar
segments = [
    (0, 15, CYAN, "float64\n(calculator)", 0.7),
    (15, 25, BLUE, "best\nexperiments", 0.6),
    (25, 35, GREEN, "approaching\nPlanck", 0.5),
    (35, 100, GOLD, "Q335 " + r"$\pi$" + "\n(what we use)", 0.7),
]

for x0, x1, col, label, al in segments:
    ax.barh(0, x1 - x0, left=x0, height=0.5, color=col, alpha=al,
            edgecolor=col, linewidth=1.5)
    ax.text((x0 + x1) / 2, 0, label, ha='center', va='center',
            fontsize=9, color=WHITE, fontweight='bold')

# Planck wall
ax.axvline(x=35, color=RED, linewidth=3, alpha=0.8)
ax.text(35, 0.55, "THE PLANCK WALL", ha='center', va='bottom',
        fontsize=12, fontweight='bold', color=RED)
ax.text(35, 0.45, r"$10^{-35}$ meters", ha='center', va='bottom',
        fontsize=9, color=RED)
ax.text(35, -0.45, "Nothing smaller\nexists in the universe", ha='center', va='top',
        fontsize=9, color=RED, fontstyle='italic')

# Overshoot annotation
ax.annotate("", xy=(100, -0.15), xytext=(35, -0.15),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(67.5, -0.25, "65 digits beyond the wall", ha='center', va='top',
        fontsize=11, color=GOLD, fontweight='bold')

ax.set_xlim(-2, 108)
ax.set_ylim(-0.7, 0.9)
ax.set_xlabel("Number of correct digits", fontsize=11, color=SILVER)
ax.set_title("Beyond the Edge of Measurement", fontsize=16,
             fontweight='bold', color=GOLD, pad=15)

# Tick marks at key positions
ax.set_xticks([0, 15, 25, 35, 50, 75, 100])
ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk2_03_precision_cliff.png")


# ================================================================
# FIG 4: Q335 PI — SPOT THE DIFFERENCE
# Type: Comparison Bar (digit alignment)
# Shows: two rows of identical digits — the identity IS the argument
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 21)
ax.set_ylim(-2, 6)

ax.text(10, 5.3, r"Q335 $\pi$ vs True $\pi$: Spot the Difference",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

pi_digits = "3.14159265358979323846264338327950288419716939937510"

ax.text(0.0, 3.8, r"True $\pi$:", ha='right', va='center', fontsize=11, color=CYAN)
ax.text(0.0, 2.2, r"Q335 $\pi$:", ha='right', va='center', fontsize=11, color=GOLD)

# Show first 40 digits (fits in the space)
show_digits = pi_digits[:42]
spacing = 0.42

for i, ch in enumerate(show_digits):
    xpos = 0.5 + i * spacing

    # True pi row
    ax.text(xpos, 3.8, ch, ha='center', va='center', fontsize=11, color=WHITE,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.12', facecolor=PAN, edgecolor=GREEN,
                      linewidth=0.8, alpha=0.4) if ch != '.' else
            dict(boxstyle='round,pad=0.12', facecolor=BG, edgecolor=BG))

    # Q335 row — identical
    ax.text(xpos, 2.2, ch, ha='center', va='center', fontsize=11, color=WHITE,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.12', facecolor=PAN, edgecolor=GREEN,
                      linewidth=0.8, alpha=0.4) if ch != '.' else
            dict(boxstyle='round,pad=0.12', facecolor=BG, edgecolor=BG))

# Ellipsis
ax.text(0.5 + 42 * spacing, 3.8, "...", ha='center', va='center',
        fontsize=14, color=DIM)
ax.text(0.5 + 42 * spacing, 2.2, "...", ha='center', va='center',
        fontsize=14, color=DIM)

# Match indicator
ax.text(10, 1.0, "ALL 100 DIGITS MATCH", ha='center', va='center',
        fontsize=14, color=GREEN, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.6))

ax.text(10, 0.1, "First disagreement: digit 101.  No experiment reaches digit 36.",
        ha='center', va='center', fontsize=11, color=SILVER)

ax.text(10, -0.8, r"$\pi$ is transcendental.  Q335 $\pi$ is a fraction."
        "  The difference is " + r"$10^{-101}$." + "\nThe universe cannot tell them apart.",
        ha='center', va='center', fontsize=10, color=DIM)

save(fig, "talk2_04_q335_pi_digits.png")


# ================================================================
# FIG 5: FOUR FORCES OR FOUR READINGS?
# Type: Geometric Cross-Section (two panels)
# Shows: isolated boxes vs one continuous gauge — structural shift
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("Four Separate Things  vs  Four Readings of One Thing",
             fontsize=16, fontweight='bold', color=GOLD, y=0.96)

# -- Left panel: textbook view (isolated boxes) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.2, "Textbook View", ha='center', va='center',
         fontsize=13, fontweight='bold', color=DIM)

forces = [
    (2.5, 7.0, "Electromagnetic\nForce", BLUE),
    (7.5, 7.0, "Weak\nForce", GREEN),
    (2.5, 3.5, "Strong\nForce", RED),
    (7.5, 3.5, "Gravity", PURPLE),
]
for fx, fy, fname, fcol in forces:
    box = mpatches.FancyBboxPatch((fx - 1.8, fy - 1.0), 3.6, 2.0,
        boxstyle="round,pad=0.2", facecolor=fcol, alpha=0.15,
        edgecolor=fcol, linewidth=2)
    ax1.add_patch(box)
    ax1.text(fx, fy, fname, ha='center', va='center', fontsize=11,
             color=fcol, fontweight='bold')

ax1.text(5, 1.0, "Four separate chapters.\nFour separate departments.\nFour separate Nobel Prizes.",
         ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

# -- Right panel: RUM view (one gauge, four readings) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.2, "RUM View", ha='center', va='center',
         fontsize=13, fontweight='bold', color=GOLD)

# Vertical thermometer
therm_x = 4.0
ax2.plot([therm_x, therm_x], [1.5, 8.5], color=SILVER, linewidth=4, alpha=0.3)

readings = [
    (8.0, "1/42", "unification", GOLD),
    (6.3, "1/30", "weak scale", GREEN),
    (4.6, "1/137", "atomic scale", BLUE),
    (2.5, "~1", "confinement", RED),
]
for ry, rval, rdesc, rcol in readings:
    # Tick mark
    ax2.plot([therm_x - 0.3, therm_x + 0.3], [ry, ry], color=rcol, linewidth=2.5)
    # Reading value
    ax2.text(therm_x + 1.0, ry + 0.2, rval, ha='left', va='center', fontsize=14,
             color=rcol, fontweight='bold')
    ax2.text(therm_x + 1.0, ry - 0.25, rdesc, ha='left', va='center',
             fontsize=9, color=SILVER)
    # Dot on thermometer
    ax2.scatter([therm_x], [ry], s=100, color=rcol, edgecolors=WHITE,
                linewidth=1.5, zorder=5)

ax2.text(5, 1.0, "Same instrument.\nDifferent depths.\nDifferent readings.",
         ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk2_05_four_forces_vs_four_readings.png")


# ================================================================
# FIG 6: THE THERMOMETER ANALOGY
# Type: Geometric Cross-Section
# Shows: continuous gradient — "different forces" are same field
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)

ax.text(5, 11.5, "Same Ocean, Different Depths, Different Readings",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Ocean gradient — vertical rectangle with color gradient
n_bands = 40
for i in range(n_bands):
    y_bot = 1.5 + i * (8.0 / n_bands)
    y_top = y_bot + (8.0 / n_bands)
    frac = i / float(n_bands)
    # Warm at top (orange) -> cold at bottom (blue)
    r_val = 0.9 * (1 - frac) + 0.2 * frac
    g_val = 0.5 * (1 - frac) + 0.3 * frac
    b_val = 0.3 * (1 - frac) + 0.9 * frac
    col = (r_val, g_val, b_val, 0.3)
    rect = mpatches.Rectangle((1.5, y_bot), 4.0, y_top - y_bot,
                               facecolor=col, edgecolor='none')
    ax.add_patch(rect)

# Border
border = mpatches.FancyBboxPatch((1.5, 1.5), 4.0, 8.0,
    boxstyle="round,pad=0", facecolor='none', edgecolor=SILVER,
    linewidth=1.5)
ax.add_patch(border)

# Depth labels and readings
depths = [
    (8.8, "Surface", "Lab scale", r"$\alpha_{em}$ = 1/137,  $\alpha_s$ = 0.118", ORANGE),
    (6.0, "Middle", "Z boson scale", r"$\alpha_{em}$ = 1/128,  $\alpha_s$ = 0.118", CYAN),
    (2.8, "Deep", "GUT scale", r"$\alpha_1 = \alpha_2 = \alpha_3$ = 1/42", BLUE),
]

for dy, dlabel, dscale, dreading, dcol in depths:
    # Horizontal line across ocean
    ax.plot([1.5, 5.5], [dy, dy], color=dcol, linewidth=1.5, linestyle='--', alpha=0.6)
    # Reading on right
    ax.text(6.0, dy + 0.25, dscale, ha='left', va='center', fontsize=10,
            color=dcol, fontweight='bold')
    ax.text(6.0, dy - 0.25, dreading, ha='left', va='center', fontsize=9,
            color=SILVER)
    # Depth label on left
    ax.text(1.2, dy, dlabel, ha='right', va='center', fontsize=9, color=dcol)

# Bottom annotation
ax.text(5, 0.7, "Nobody says the ocean has four different temperatures.\n"
        "It has one temperature field read at four depths.",
        ha='center', va='center', fontsize=11, color=WHITE, fontstyle='italic')

save(fig, "talk2_06_thermometer_analogy.png")


# ================================================================
# FIG 7: THE FIVE-DEPARTMENT CHAIN
# Type: Progression/Sequence
# Shows: one chain crossing five departmental walls
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16.5)
ax.set_ylim(-1.5, 7)

ax.text(8, 6.3, "One Chain, Five Departments, Zero Cross-Hires",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

depts = [
    (1.5, 3.5, "Mathematical\nPhysics", r"$\beta$ = 41/10," + "\n" + r"$-$19/6, $-$7", GOLD),
    (4.7, 3.5, "Particle\nPhysics", r"$\alpha_s$ = 0.118", CYAN),
    (7.9, 3.5, "Cosmology", r"DM/baryon" + "\n= (22/13)" + r"$\pi$", PURPLE),
    (11.1, 3.5, "Nuclear\nPhysics", "D/H, He, Li\nfrom BBN", ORANGE),
    (14.3, 3.5, "Observational\nAstronomy", "quasar\nabsorption\nspectra", GREEN),
]

for i, (dx, dy, dname, dformula, dcol) in enumerate(depts):
    rounded_box(ax, dx, dy, 2.5, 2.8, "", dcol, alpha=0.15)
    ax.text(dx, dy + 0.7, dname, ha='center', va='center', fontsize=10,
            color=dcol, fontweight='bold')
    ax.text(dx, dy - 0.5, dformula, ha='center', va='center', fontsize=8,
            color=SILVER)

    # Arrow and wall to next
    if i < len(depts) - 1:
        nx = depts[i+1][0]
        mid = (dx + nx) / 2
        # Wall
        ax.axvline(x=mid, color=RED, alpha=0.3, linestyle=':', linewidth=2,
                   ymin=0.15, ymax=0.85)
        ax.text(mid, 5.7, "wall", ha='center', va='center', fontsize=7,
                color=RED, alpha=0.6, rotation=90)
        # Arrow over wall
        ax.annotate("", xy=(nx - 1.35, dy), xytext=(dx + 1.35, dy),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=2,
                                   connectionstyle='arc3,rad=-0.15'))

ax.text(8, 0.5, "The chain exists in nature. The walls exist only in institutions.",
        ha='center', va='center', fontsize=12, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=DIM))

save(fig, "talk2_07_five_department_chain.png")


# ================================================================
# FIG 8: WHO READS WHOSE PAPERS?
# Type: Connection/Integer Map (matrix)
# Shows: sparse off-diagonal — nobody reads across departments
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

dept_names = ["Gauge\nTheory", "Particle\nPhysics", "Cosmo-\nlogy", "Nuclear\nPhysics", "Observ.\nAstron."]
n = len(dept_names)

# Build matrix: 2=reads, 1=sometimes, 0=never
matrix = np.array([
    [2, 1, 0, 0, 0],
    [1, 2, 1, 0, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 1, 2, 1],
    [0, 0, 0, 1, 2],
])

color_map = {0: RED, 1: CYAN, 2: GREEN}
label_map = {0: r"$\times$", 1: "~", 2: r"$\checkmark$"}

cell_size = 1.0
x_off = 2.5
y_off = 1.5

for i in range(n):
    for j in range(n):
        val = matrix[i, j]
        cx = x_off + j * cell_size + cell_size / 2
        cy = y_off + (n - 1 - i) * cell_size + cell_size / 2
        col = color_map[val]
        rect = mpatches.Rectangle((x_off + j * cell_size, y_off + (n-1-i) * cell_size),
                                   cell_size, cell_size,
                                   facecolor=col, alpha=0.15 if val == 0 else 0.25,
                                   edgecolor=DIM, linewidth=0.5)
        ax.add_patch(rect)
        ax.text(cx, cy, label_map[val], ha='center', va='center',
                fontsize=14, color=col, fontweight='bold')

# Row labels (left)
for i in range(n):
    ax.text(x_off - 0.2, y_off + (n-1-i) * cell_size + cell_size/2,
            dept_names[i], ha='right', va='center', fontsize=9, color=WHITE)

# Column labels (top) — stagger upward to avoid overlap
for j in range(n):
    ax.text(x_off + j * cell_size + cell_size/2,
            y_off + n * cell_size + 0.3 + (j % 2) * 0.5,
            dept_names[j], ha='center', va='bottom', fontsize=9, color=WHITE)

ax.set_title("The Citation Gap: Who Reads Whom", fontsize=16,
             fontweight='bold', color=GOLD, pad=25)

# Legend
legend_items = [
    (GREEN, r"$\checkmark$ Reads own field"),
    (CYAN, "~ Occasionally reads neighbor"),
    (RED, r"$\times$ Never reads"),
]
for li, (lcol, ltxt) in enumerate(legend_items):
    ax.text(9, 5.5 - li * 0.6, ltxt, ha='left', va='center',
            fontsize=10, color=lcol)

# Key callout
ax.text(9, 3.0, 'Nobody multiplied\n22/13 by ' + r'$\pi$' + '\nand compared to 5.320',
        ha='left', va='center', fontsize=10, color=GOLD, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.7))

ax.set_xlim(-0.5, 13)
ax.set_ylim(0.5, 8)
ax.axis('off')

save(fig, "talk2_08_citation_matrix.png")


# ================================================================
# FIG 9: THE ALPHABET BARRIER
# Type: Comparison Bar (side by side columns)
# Shows: Greek letters vs plain English — the barrier is just font
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(-1, 12)

ax.text(8, 11.2, "Same Information, Different Accessibility",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

greek = [r"$\alpha$", r"$\beta$", r"$\lambda$", r"$\mu$",
         r"$\nu$", r"$\sigma$", r"$\theta$", r"$\Omega$"]
english = ["force strength", "running rate", "wavelength", "energy scale",
           "neutrino", "cross-section", "mixing angle", "density fraction"]

ax.text(3.5, 10.2, "Physics Notation", ha='center', va='center',
        fontsize=12, fontweight='bold', color=DIM)
ax.text(12.5, 10.2, "What It Means", ha='center', va='center',
        fontsize=12, fontweight='bold', color=GREEN)

for i in range(len(greek)):
    y = 9.0 - i * 1.15

    # Greek (opaque)
    ax.text(3.5, y, greek[i], ha='center', va='center', fontsize=16,
            color=DIM, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN, edgecolor=DIM,
                      linewidth=1, alpha=0.4))

    # Arrow
    ax.annotate("", xy=(8.5, y), xytext=(5.5, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))

    # English (transparent)
    ax.text(12.5, y, english[i], ha='center', va='center', fontsize=11,
            color=GREEN, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN, edgecolor=GREEN,
                      linewidth=1, alpha=0.3))

ax.text(8, -0.2, "The knowledge isn't hard. The font is unfamiliar.\n"
        "The unfamiliarity is the barrier.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk2_09_alphabet_barrier.png")


# ================================================================
# FIG 10: PERSON-NAMES VS DESCRIPTIVE NAMES
# Type: Comparison Bar (side by side columns)
# Shows: opaque person-name vs transparent description
# ================================================================
fig, ax = plt.subplots(figsize=(18, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(-1, 11)

ax.text(8, 10.3, "What the Name Tells You",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

person_names = [
    "Weinberg angle",
    "Dirac equation",
    u"Schr\u00f6dinger equation",
    "Cabibbo angle",
    r"W$^+$ boson",
]
descriptive = [
    "electroweak mixing angle",
    "relativistic electron\nfield equation",
    "quantum wave\nevolution equation",
    "quark generation\nmixing angle",
    "Electroweak.Messenger\n.Positive.Flash",
]

ax.text(3.5, 9.3, "Standard Name", ha='center', va='center',
        fontsize=12, fontweight='bold', color=DIM)
ax.text(12.5, 9.3, "Descriptive Name", ha='center', va='center',
        fontsize=12, fontweight='bold', color=GREEN)

for i in range(len(person_names)):
    y = 8.0 - i * 1.6

    # Person name (opaque)
    ax.text(3.5, y, person_names[i], ha='center', va='center', fontsize=12,
            color=DIM, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=PAN, edgecolor=DIM,
                      linewidth=1, alpha=0.4))

    # Arrow
    ax.annotate("", xy=(8.5, y), xytext=(5.8, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))

    # Descriptive (transparent)
    ecol = GOLD if i == len(person_names) - 1 else GREEN
    ax.text(12.5, y, descriptive[i], ha='center', va='center', fontsize=11,
            color=ecol, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=PAN, edgecolor=ecol,
                      linewidth=1.5 if i == len(person_names) - 1 else 1, alpha=0.4))

# Highlight callout for W boson
ax.text(12.5, 0.5, "Which one tells a 12-year-old what it does?",
        ha='center', va='center', fontsize=11, color=GOLD, fontstyle='italic')

ax.text(8, -0.4, "Left column: social history.  Right column: physics.\n"
        "Both are useful. Only one teaches.",
        ha='center', va='center', fontsize=10, color=SILVER)

save(fig, "talk2_10_person_vs_descriptive_names.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 2, 1-10) generated ===")
filenames = [
    "talk2_01_gap_ratio_fraction_vs_decimal.png",
    "talk2_02_unification_decimal_vs_fraction.png",
    "talk2_03_precision_cliff.png",
    "talk2_04_q335_pi_digits.png",
    "talk2_05_four_forces_vs_four_readings.png",
    "talk2_06_thermometer_analogy.png",
    "talk2_07_five_department_chain.png",
    "talk2_08_citation_matrix.png",
    "talk2_09_alphabet_barrier.png",
    "talk2_10_person_vs_descriptive_names.png",
]
for f in filenames:
    print("  %s" % f)
    