#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 7, Slides 1-10
10 figures covering: unification gap 0.027, loop order convergence,
p=0.81 blocked claim, random integer histogram, confinement blank zone,
what lives in the wall, gravity disconnected, G scatter,
Hubble tension, four confidence levels.
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
# FIG 1: THE 0.027 GAP — ALMOST ZERO BUT NOT ZERO
# Type: Threshold/Region
# Shows: three curves nearly meeting — tiny triangle of daylight
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

log_e = np.linspace(14.0, 16.5, 300)

# Approximate coupling running near crossing (CD theory)
a1_inv = 42.1 + (log_e - 15.5) * 0.46
a2_inv = 42.1 - (log_e - 15.5) * 0.56
a3_inv = 42.1 - (log_e - 15.5) * 0.58 - 0.013

ax.plot(log_e, a1_inv, color=BLUE, linewidth=2.5, label=r"$\alpha_1^{-1}$ (U(1))")
ax.plot(log_e, a2_inv, color=GREEN, linewidth=2.5, label=r"$\alpha_2^{-1}$ (SU(2))")
ax.plot(log_e, a3_inv, color=RED, linewidth=2.5, label=r"$\alpha_3^{-1}$ (SU(3))")

# Mark the near-crossing region
cross_x = 15.55
ax.axvline(x=cross_x, color=GOLD, linewidth=1, linestyle=':', alpha=0.4)

# Gap annotation — arrow into the triangle
ax.annotate("gap = 0.027\n= 0.064% of 42.135",
            xy=(cross_x, 42.1), xytext=(14.5, 43.5),
            fontsize=10, color=ORANGE, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Shade the tiny gap triangle
triangle_x = [15.45, 15.65, 15.55]
triangle_y = [42.15, 42.15, 42.05]
ax.fill(triangle_x, triangle_y, color=ORANGE, alpha=0.15)

ax.legend(loc='upper left', fontsize=10, facecolor=PAN, labelcolor=WHITE)
ax.set_xlabel(r"log$_{10}$(E / GeV)", fontsize=11, color=SILVER)
ax.set_ylabel(r"$\alpha_i^{-1}$", fontsize=11, color=SILVER)
ax.set_title("The Unification Gap: 0.027 out of 42.135",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Three possibilities
possibilities = [
    (14.3, 40.5, "1. Three-loop closes it\n   (not yet computed)", GREEN),
    (14.3, 40.0, "2. GUT threshold corrections\n   close it (not yet computed)", CYAN),
    (14.3, 39.5, "3. Irreducible\n   (minimal unification incomplete)", RED),
]
for px, py, ptxt, pcol in possibilities:
    ax.text(px, py, ptxt, ha='left', va='center', fontsize=8, color=pcol)

ax.text(15.2, 39.2, "I don't know which.\nThe framework says so explicitly.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(14.0, 16.5)
ax.set_ylim(39.0, 44.0)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_01_unification_gap.png")


# ================================================================
# FIG 2: ONE-LOOP VS TWO-LOOP VS THREE-LOOP
# Type: Comparison Bar
# Shows: gap shrinking 20x, third bar missing with question mark
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

loop_labels = ["One-loop", "Two-loop", "Three-loop"]
gap_values = [0.5, 0.027, None]
bar_colors = [ORANGE, CYAN, DIM]

x = np.arange(3)

for i in range(3):
    if gap_values[i] is not None:
        ax.bar(x[i], gap_values[i], width=0.5, color=bar_colors[i], alpha=0.7)
        ax.text(x[i], gap_values[i] + 0.02, "%.3f" % gap_values[i], ha='center',
                va='bottom', fontsize=14, color=bar_colors[i], fontweight='bold')
    else:
        # Missing bar with question mark
        ax.bar(x[i], 0.02, width=0.5, color=DIM, alpha=0.2)
        ax.text(x[i], 0.15, "?", ha='center', va='center', fontsize=36,
                color=DIM, fontweight='bold')

# Descriptions under bars
descs = [
    "Computed.\nGap exists.",
    "Computed.\nGap shrinks 20" + r"$\times$.",
    "Not computed.\nNobody has done\nthis calculation.",
]
for i, desc in enumerate(descs):
    ax.text(x[i], -0.08, descs[i], ha='center', va='top', fontsize=8,
            color=SILVER)

# Extrapolation line
ax.plot([0, 1, 2], [0.5, 0.027, 0.0], color=GOLD, linewidth=2, linestyle='--',
        alpha=0.5)
ax.text(1.8, 0.05, "extrapolation\ncrosses zero", ha='center', va='center',
        fontsize=8, color=GOLD, fontstyle='italic')

# 20x annotation
ax.annotate("20" + r"$\times$" + " smaller", xy=(0.5, 0.25), xytext=(0.5, 0.4),
            fontsize=10, color=SILVER, ha='center',
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5))

ax.set_xticks(x)
ax.set_xticklabels(loop_labels, fontsize=12, color=WHITE)
ax.set_ylabel("Gap (unification miss)", fontsize=11, color=SILVER)
ax.set_title("How the Gap Changes with Precision",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(1, 0.52, "The trend is promising. But an extrapolation\nis not a calculation. The calculation hasn't been done.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(-0.15, 0.6)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_02_loop_order_convergence.png")


# ================================================================
# FIG 3: p = 0.81 — THE BLOCKED CLAIM
# Type: Threshold/Region
# Shows: own system blocking own claim — dot in red zone
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Zones
ax.axvspan(0, 0.1, color=GREEN, alpha=0.08)
ax.axvspan(0.1, 1.0, color=RED, alpha=0.06)

# Threshold
ax.axvline(x=0.1, color=GREEN, linewidth=2.5, linestyle='--', alpha=0.7)
ax.text(0.1, 0.88, "threshold\np = 0.1", ha='center', va='center',
        fontsize=10, color=GREEN, fontweight='bold')

# Zone labels
ax.text(0.05, 0.70, "CLEAR\nclaim can\nadvance", ha='center', va='center',
        fontsize=10, color=GREEN, fontstyle='italic')
ax.text(0.55, 0.70, "BLOCKED\nclaim cannot advance\nuntil statistics resolved",
        ha='center', va='center', fontsize=11, color=RED, fontstyle='italic')

# The claim text
ax.text(0.5, 0.92, "Claim: DM/baryon = (22/13)" + r"$\pi$" +
        " = 5.317 vs measured 5.320. Miss: 725 ppm.",
        ha='center', va='center', fontsize=9, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Measured p dot
ax.scatter([0.81], [0.45], s=400, color=RED, zorder=5, marker='o')
ax.text(0.81, 0.55, "p = 0.81", ha='center', va='bottom', fontsize=14,
        color=RED, fontweight='bold')
ax.text(0.81, 0.35, "Random integers match\n81% of the time", ha='center',
        va='top', fontsize=9, color=SILVER)

# Status
ax.text(0.5, 0.12, "STATUS: BLOCKING", ha='center', va='center',
        fontsize=20, color=RED, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_title("The Gate I Built Against Myself",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.set_xlabel("p-value (probability of coincidence)", fontsize=11, color=SILVER)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0.0, 0.98)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_03_p081_blocked.png")


# ================================================================
# FIG 4: RANDOM INTEGER HITS — WHY 725 PPM ISN'T SPECIAL ENOUGH
# Type: Running/Convergence (histogram)
# Shows: 725 ppm mark sitting among many random hits
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Generate random (a/b)*pi misses vs 5.320
np.random.seed(42)
target = 5.320
hits = []
for a in range(1, 31):
    for b in range(1, 31):
        if a != b:
            val = (a / b) * np.pi
            miss_ppm = abs(val - target) / target * 1e6
            if miss_ppm < 5000:
                hits.append(miss_ppm)

bins = np.linspace(0, 5000, 50)
ax.hist(hits, bins=bins, color=DIM, alpha=0.5)

# 725 ppm marker
ax.axvline(x=725, color=GOLD, linewidth=2.5, alpha=0.8)
ax.text(725 + 100, ax.get_ylim()[1] * 0.85, "(22/13)" + r"$\pi$" + "\n725 ppm",
        ha='left', va='center', fontsize=12, color=GOLD, fontweight='bold')

# Count how many are closer
closer = sum(1 for h in hits if h <= 725)
ax.text(2500, ax.get_ylim()[1] * 0.7,
        "%d random pairs\nachieve " % closer + r"$\leq$" + " 725 ppm",
        ha='center', va='center', fontsize=11, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlabel("Miss from 5.320 (ppm)", fontsize=11, color=SILVER)
ax.set_ylabel("Count of random (a/b)" + r"$\pi$" + " pairs", fontsize=11, color=SILVER)
ax.set_title("How Often Random Integers Land This Close",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(2500, ax.get_ylim()[1] * 0.3,
        "With integers from 1 to 30: ~400 pairs.\n"
        "Many produce (a/b)" + r"$\pi$" + " near 5.320.\n"
        "The hit isn't rare enough to exclude coincidence.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_04_random_integer_hits.png")


# ================================================================
# FIG 5: THE BLANK ZONE — 300 MEV TO 2 GEV
# Type: Threshold/Region
# Shows: hatched region where computation stops
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Energy axis (log scale)
log_e = np.linspace(-1, 2.5, 300)  # 100 MeV to ~300 GeV

# Alpha_s curve (approximate)
alpha_s = 0.118 * (1 + 0.7 * (2.0 - log_e))
alpha_s = np.clip(alpha_s, 0.1, 5.0)

ax.plot(10**log_e / 1000, alpha_s, color=RED, linewidth=2.5, label=r"$\alpha_s$")

# Zones
# Confined zone (left)
ax.axvspan(0.1, 0.3, color=RED, alpha=0.08)
ax.text(0.15, 4.5, "CONFINED\n" + r"$\alpha_s \rightarrow \infty$" + "\nQuarks trapped",
        ha='center', va='center', fontsize=9, color=RED)

# Blank zone
ax.axvspan(0.3, 2.0, color=DIM, alpha=0.1)
# Diagonal hatching (manual)
for hx in np.arange(0.3, 2.0, 0.15):
    ax.plot([hx, hx + 0.1], [0.5, 4.5], color=DIM, linewidth=0.5, alpha=0.3)

ax.text(0.8, 3.5, "THE BLANK ZONE\n" + r"$\alpha_s \approx 1$" +
        "\nNeither perturbative\nnor fully confined",
        ha='center', va='center', fontsize=11, color=WHITE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(0.8, 1.5, "Lattice QCD works here\non supercomputers.\nNobody can do it\nanalytically.",
        ha='center', va='center', fontsize=8, color=DIM, fontstyle='italic')

# Perturbative zone (right)
ax.axvspan(2.0, 300, color=GREEN, alpha=0.04)
ax.text(20, 0.8, "PERTURBATIVE\n" + r"$\alpha_s < 1$" + "\nComputation works",
        ha='center', va='center', fontsize=9, color=GREEN)

# Hadronic VP marker
ax.scatter([1.0], [2.5], s=200, color=ORANGE, zorder=5, marker='D')
ax.text(1.5, 2.8, "Hadronic VP " + r"$\Delta$" + "\n= 220393/50000\nLimits " + r"$\alpha$" + " to " + r"$\pm$73 ppm",
        ha='left', va='center', fontsize=8, color=ORANGE,
        bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

# Boundary markers
ax.scatter([0.3], [3.0], s=100, color=RED, zorder=5, marker='|')
ax.text(0.3, 0.4, "lower face\n300 MeV", ha='center', va='center', fontsize=7, color=RED)
ax.scatter([2.0], [1.2], s=100, color=GREEN, zorder=5, marker='|')
ax.text(2.0, 0.4, "upper face\n2 GeV", ha='center', va='center', fontsize=7, color=GREEN)

ax.set_xscale('log')
ax.set_xlabel("Energy (GeV)", fontsize=11, color=SILVER)
ax.set_ylabel(r"$\alpha_s$ (approximate)", fontsize=11, color=SILVER)
ax.set_title("The Confinement Wall: Where Computation Stops",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(0.1, 300)
ax.set_ylim(0.2, 5.0)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_05_confinement_blank_zone.png")


# ================================================================
# FIG 6: WHAT LIVES IN THE WALL
# Type: Scale/Landscape
# Shows: crucial quantities all sharing the same limitation
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 10)

ax.text(6, 9.3, "Inside the Confinement Wall: What We Can't Compute",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

items = [
    ("Proton mass", "938.3 MeV", "99% confinement energy", RED,
     "Lattice: ~3%", "Analytical: no"),
    ("Pion mass", "139.6 MeV", "ChPT gives leading order", ORANGE,
     "Lattice: yes", "Analytical: leading only"),
    ("Hadronic VP", r"$\Delta\alpha_{had}$", "Two methods disagree", MAG,
     "Lattice: disputed", "Analytical: no"),
    ("Nuclear force range", "1.41 fm", "Set by pion mass", GREEN,
     "Lattice: indirect", "Analytical: no"),
    ("n-p mass difference", "1.293 MeV", "Determines nuclear stability", CYAN,
     "Lattice: yes", "Analytical: no"),
]

for i, (name, value, note, col, lattice, analytical) in enumerate(items):
    y = 7.8 - i * 1.5

    # Item bar
    rounded_box(ax, 3.5, y, 6.0, 1.0, "", col, alpha=0.12)

    # Name and value
    ax.text(1.0, y + 0.15, name, ha='left', va='center', fontsize=11,
            color=col, fontweight='bold')
    ax.text(1.0, y - 0.2, value, ha='left', va='center', fontsize=9,
            color=SILVER)

    # Note
    ax.text(5.0, y + 0.15, note, ha='left', va='center', fontsize=9,
            color=WHITE)

    # Lattice / Analytical status
    ax.text(9.5, y + 0.15, lattice, ha='left', va='center', fontsize=8,
            color=GREEN if "yes" in lattice.lower() else ORANGE)
    ax.text(9.5, y - 0.2, analytical, ha='left', va='center', fontsize=8,
            color=RED)

# Column headers
ax.text(9.5, 8.8, "Status", ha='left', va='center', fontsize=9,
        color=SILVER, fontweight='bold')

ax.text(6, 0.5, "Everything that makes matter exist lives inside this wall.\n"
        "The wall is the most important unsolved problem in the model.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk7_06_inside_the_wall.png")


# ================================================================
# FIG 7: GRAVITY — THE DISCONNECTED DOMAIN
# Type: Connection/Integer Map
# Shows: two connected clusters with a gap between them
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 17)
ax.set_ylim(-1.5, 8)

ax.text(8, 7.3, "Gravity: Confirmed but Not Connected",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Left cluster: Gauge integers
gauge_nodes = [
    (1.5, 5.0, r"$\beta$ coefficients", GREEN),
    (4.0, 5.0, "gap 38/27", CYAN),
    (1.5, 3.0, r"sin$^2\theta_W$", GREEN),
    (4.0, 3.0, r"$\alpha_s$", GREEN),
    (2.75, 1.5, "DM/baryon\n(22/13)" + r"$\pi$", PURPLE),
]

for nx, ny, ntxt, ncol in gauge_nodes:
    rounded_box(ax, nx, ny, 2.2, 1.0, ntxt, ncol, fontsize=8, alpha=0.15)

# Internal connections (left cluster)
gauge_pairs = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
for a, b in gauge_pairs:
    ax.plot([gauge_nodes[a][0], gauge_nodes[b][0]],
            [gauge_nodes[a][1], gauge_nodes[b][1]],
            color=GREEN, linewidth=1, alpha=0.3)

ax.text(2.75, 6.3, "GAUGE INTEGERS\nConnected. Every node\nderives from the integers.",
        ha='center', va='center', fontsize=9, color=GREEN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Right cluster: Gravity
grav_nodes = [
    (12.0, 5.0, r"$\Phi/c^2$", CYAN),
    (14.5, 5.0, "Mercury\n2.8 ppm", CYAN),
    (12.0, 3.0, "GPS\n0.35%", CYAN),
    (14.5, 3.0, "Hulse-Taylor\n42 ppm", CYAN),
    (13.25, 1.5, "Solar redshift\n16 ppm", CYAN),
]

for nx, ny, ntxt, ncol in grav_nodes:
    rounded_box(ax, nx, ny, 2.2, 1.0, ntxt, ncol, fontsize=8, alpha=0.15)

# Internal connections (right cluster)
grav_pairs = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
for a, b in grav_pairs:
    ax.plot([grav_nodes[a][0], grav_nodes[b][0]],
            [grav_nodes[a][1], grav_nodes[b][1]],
            color=CYAN, linewidth=1, alpha=0.3)

ax.text(13.25, 6.3, "GRAVITY\nConfirmed at 18 orders.\n17/18 tests pass.",
        ha='center', va='center', fontsize=9, color=CYAN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# THE GAP
ax.plot([6, 6], [1.0, 5.5], color=RED, linewidth=2, linestyle=':', alpha=0.4)
ax.plot([10, 10], [1.0, 5.5], color=RED, linewidth=2, linestyle=':', alpha=0.4)

ax.text(8, 4.5, "?", ha='center', va='center', fontsize=40, color=RED, alpha=0.3)
ax.text(8, 3.0, "NO DERIVATION\nCHAIN connects\nthese two clusters",
        ha='center', va='center', fontsize=10, color=RED,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(8, -0.5, "The GR formula works. The interpretation matches.\n"
        "But the computation linking gauge integers to G has not been done.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk7_07_gravity_disconnected.png")


# ================================================================
# FIG 8: G SCATTER — 15 MEASUREMENTS, 500 PPM SCATTER
# Type: Running/Convergence (scatter)
# Shows: dots spread far wider than error bars
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Approximate G measurements (in units of 10^-11)
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

# Data points
for i in range(len(years)):
    tc = tech_colors[techniques[i]]
    ax.scatter([years[i]], [g_vals[i]], s=80, color=tc, zorder=5, marker='o')
    ax.plot([years[i], years[i]], [g_vals[i] - g_errs[i], g_vals[i] + g_errs[i]],
            color=tc, linewidth=1.5, alpha=0.7)

# Legend
for tech, tcol in tech_colors.items():
    ax.scatter([], [], color=tcol, label=tech, s=60)
ax.legend(loc='lower left', fontsize=9, facecolor=PAN, labelcolor=WHITE)

ax.set_xlabel("Year", fontsize=11, color=SILVER)
ax.set_ylabel(r"G ($\times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$)", fontsize=10, color=SILVER)
ax.set_title("Newton's G: 15 Measurements, 500 PPM Scatter",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(2000, 6.676, "Scatter exceeds individual\nuncertainties by 17" + r"$\times$" + ".\n\n"
        "Standard: underestimated systematics.\n"
        "Alternative: G is a boundary reading\nthat varies with lab environment.",
        ha='center', va='center', fontsize=9, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(1978, 2026)
ax.set_ylim(6.670, 6.678)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_08_g_scatter.png")


# ================================================================
# FIG 9: TWO NUMBERS THAT SHOULD AGREE BUT DON'T
# Type: Threshold/Region
# Shows: non-overlapping Hubble measurement bands
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# SH0ES band
shoes_val = 73.04
shoes_unc = 1.04
ax.axhspan(shoes_val - shoes_unc, shoes_val + shoes_unc, color=MAG, alpha=0.12)
ax.axhline(y=shoes_val, color=MAG, linewidth=1.5, linestyle='--', alpha=0.6)

# Planck band
planck_val = 67.4
planck_unc = 0.5
ax.axhspan(planck_val - planck_unc, planck_val + planck_unc, color=CYAN, alpha=0.12)
ax.axhline(y=planck_val, color=CYAN, linewidth=1.5, linestyle='--', alpha=0.6)

# Labels
ax.text(2.5, shoes_val + 1.5, "SH0ES (local, supernovae)\n73.04 " + r"$\pm$" + " 1.04",
        ha='center', va='bottom', fontsize=11, color=MAG, fontweight='bold')
ax.text(2.5, planck_val - 1.5, "Planck (CMB, early universe)\n67.4 " + r"$\pm$" + " 0.5",
        ha='center', va='top', fontsize=11, color=CYAN, fontweight='bold')

# Gap
mid = (shoes_val + planck_val) / 2
ax.annotate("5" + r"$\sigma$" + " tension\n8.4% disagreement",
            xy=(4.0, mid), xytext=(4.0, mid),
            fontsize=12, color=RED, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

# RUM note
ax.text(4.0, 64.5, "The boundary reading framework suggests:\n"
        "different boundaries give different readings.\n"
        "But this has not been computed. Not been compared.\n"
        "Status: SPECULATIVE.",
        ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.5, 5.5)
ax.set_ylim(63, 77)
ax.set_ylabel(r"$H_0$ (km/s/Mpc)", fontsize=12, color=SILVER)
ax.set_xticks([])
ax.set_title("The Hubble Tension: 73 vs 67.4",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk7_09_hubble_tension.png")


# ================================================================
# FIG 10: FOUR LEVELS OF CONFIDENCE
# Type: Comparison Bar
# Shows: decreasing visual solidity from confirmed to speculative
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 10)

ax.text(6, 9.3, "Four Levels of Confidence",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

levels = [
    ("CONFIRMED", GREEN, 1.0,
     r"$\alpha^{-1}$ = 137.036 (0.007 ppb)" + "\nAutomated test passes. Published measurement matches.",
     "solid"),
    ("ACTIVE", CYAN, 0.7,
     "Sector splitting prediction.\nDerivation complete. Test awaiting hardware (Th-229, 2028-2032).",
     "solid"),
    ("PROPOSED", ORANGE, 0.4,
     "Reading depth = GR dilation.\nFormula identical. Interpretation untestable with current data.",
     "dashed"),
    ("SPECULATIVE", DIM, 0.2,
     "Hubble tension from boundary readings.\nNot computed. Not compared. Might be calibration.",
     "dotted"),
]

for i, (status, col, alpha_val, example, style) in enumerate(levels):
    y = 7.5 - i * 2.0

    # Status bar with varying solidity
    bar_w = 10.0
    if style == "solid":
        rect = mpatches.FancyBboxPatch((0.5, y - 0.5), bar_w, 1.0,
            boxstyle="round,pad=0.1", facecolor=col, alpha=alpha_val * 0.3,
            linewidth=2)
        ax.add_patch(rect)
    elif style == "dashed":
        rect = mpatches.FancyBboxPatch((0.5, y - 0.5), bar_w, 1.0,
            boxstyle="round,pad=0.1", facecolor=col, alpha=alpha_val * 0.2,
            linewidth=2, linestyle='--')
        ax.add_patch(rect)
    elif style == "dotted":
        rect = mpatches.FancyBboxPatch((0.5, y - 0.5), bar_w, 1.0,
            boxstyle="round,pad=0.1", facecolor=col, alpha=alpha_val * 0.15,
            linewidth=2, linestyle=':')
        ax.add_patch(rect)

    # Status label
    ax.text(1.2, y + 0.2, status, ha='left', va='center', fontsize=13,
            color=col, fontweight='bold')

    # Example
    ax.text(4.0, y - 0.1, example, ha='left', va='center', fontsize=8,
            color=SILVER)

ax.text(6, -0.2, "The model labels its own confidence level.\n"
        "CONFIRMED means tested and passing. SPECULATIVE means noted and not resolved.\n"
        "The label travels with the claim.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk7_10_four_confidence_levels.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 7, 1-10) generated ===")
filenames = [
    "talk7_01_unification_gap.png",
    "talk7_02_loop_order_convergence.png",
    "talk7_03_p081_blocked.png",
    "talk7_04_random_integer_hits.png",
    "talk7_05_confinement_blank_zone.png",
    "talk7_06_inside_the_wall.png",
    "talk7_07_gravity_disconnected.png",
    "talk7_08_g_scatter.png",
    "talk7_09_hubble_tension.png",
    "talk7_10_four_confidence_levels.png",
]
for f in filenames:
    print("  %s" % f)
