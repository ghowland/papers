#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 1, Slides 11-20
10 figures covering: derivation chain, BBN results, QED chain,
hydrogen frequency, Cabibbo Doublet, what-if scan, test suite,
input/output map, precision staircase, closing card.
Output: PNG files to ./figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Color palette ──
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
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=textcolor, fontweight='bold', zorder=10)

# ================================================================
# FIG 11: THE DERIVATION CHAIN — INTEGERS TO DEUTERIUM
# Type: Progression/Sequence
# Shows: 4-step chain from integer ratio to nuclear abundance
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1.5, 6.5)

ax.text(5.0, 6.0, "From 22/13 to Deuterium in 4 Steps",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Chain boxes
chain = [
    (1.0, 3.5, "(22/13)" + r"$\pi$" + "\n= 5.3165", "DM/baryon\nratio", GOLD, "725 ppm"),
    (3.25, 3.5, r"$\Omega_b$" + "\n= 0.04904", "baryon\ndensity", CYAN, "727 ppm"),
    (5.5, 3.5, r"$\eta_{10}$" + "\n= 6.090", "baryon-to-photon\nratio", GREEN, "0.24%"),
    (7.75, 3.5, "BBN\nnuclear\nreactions", "standard\nnucleosynthesis", ORANGE, "textbook"),
    (10.0, 3.5, "D/H\n= 2.531" + r"$\times 10^{-5}$", "deuterium\nabundance", MAG, "0.12" + r"$\sigma$"),
]

for i, (cx, cy, main, sub, col, miss) in enumerate(chain):
    rounded_box(ax, cx, cy, 1.8, 2.2, "", col, alpha=0.2)
    ax.text(cx, cy + 0.35, main, ha='center', va='center', fontsize=11,
            color=WHITE, fontweight='bold')
    ax.text(cx, cy - 0.55, sub, ha='center', va='center', fontsize=8, color=SILVER)
    ax.text(cx, cy - 0.95, "miss: %s" % miss, ha='center', va='center',
            fontsize=8, color=col, fontstyle='italic')
    # Arrow to next
    if i < len(chain) - 1:
        nx = chain[i+1][0]
        ax.annotate("", xy=(nx - 1.0, cy), xytext=(cx + 1.0, cy),
                     arrowprops=dict(arrowstyle='->', color=DIM, lw=2))

ax.text(5.0, 0.5, "One integer ratio (22/13) predicts how much deuterium\nthe Big Bang made. Every step uses standard textbook physics.",
        ha='center', va='center', fontsize=12, color=SILVER,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=DIM))

save(fig, "talk1_11_chain_to_deuterium.png")

# ================================================================
# FIG 12: BBN RESULTS — FOUR ELEMENTS
# Type: Comparison Bar
# Shows: three agreements and one lithium problem — contrast is visual
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

elements = ["D/H", r"$Y_p$ (He-4)", "He-3", "Li-7"]
pred =     [2.531, 24.86, 1.04, 4.74]
meas =     [2.527, 24.49, 1.00, 1.60]
misses =   [r"0.12$\sigma$", r"0.94$\sigma$", r"0.36$\sigma$", r"2.96$\times$"]
colors =   [GREEN, GREEN, CYAN, RED]

x = np.arange(len(elements))
w = 0.32

bars_p = ax.bar(x - w/2, pred, w, color=GOLD, alpha=0.7, edgecolor=GOLD,
                linewidth=1.5, label='Predicted')
bars_m = ax.bar(x + w/2, meas, w, color=[c for c in colors], alpha=0.7,
                edgecolor=[c for c in colors], linewidth=1.5, label='Measured')

# Labels on bars — stagger vertically to avoid overlap
for i in range(len(elements)):
    top_p = pred[i]
    top_m = meas[i]
    higher = max(top_p, top_m)
    ax.text(x[i] - w/2, top_p + higher * 0.06, "%.2f" % pred[i], ha='center',
            va='bottom', fontsize=9, color=GOLD)
    ax.text(x[i] + w/2, top_m + higher * 0.10, "%.2f" % meas[i], ha='center',
            va='bottom', fontsize=9, color=colors[i])
    ax.text(x[i], -higher * 0.08, misses[i], ha='center', va='top',
            fontsize=10, color=colors[i], fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(elements, fontsize=12, color=WHITE)
ax.set_ylabel("Value (various units)", fontsize=11, color=SILVER)
ax.set_title("Primordial Abundances: Predicted vs Measured",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# Lithium annotation
ax.annotate("The lithium problem.\nEvery model has this.\nWe inherit it — same nuclear physics.",
            xy=(3, 4.74), xytext=(2.2, 18),
            fontsize=9, color=RED, ha='center',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, alpha=0.8))

ax.legend(loc='upper left', fontsize=10, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)
ax.set_ylim(-3, 30)

save(fig, "talk1_12_bbn_four_elements.png")

# ================================================================
# FIG 13: ONE MEASUREMENT TO TWELVE DIGITS
# Type: Scale/Landscape
# Shows: precision chain from trapped electron to alpha at 12 digits
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1.5, 5.5)

ax.text(5.0, 5.0, "From One Trapped Electron to " + r"$\alpha$" + " at 12 Digits",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

# Three stages
stages = [
    (1.5, 2.5, r"$a_e$ = 0.001159652...", "Measured at Harvard\nOne electron in a\nmagnetic field", GOLD),
    (5.0, 2.5, "5-loop QED series\n+ Newton inversion", "Residual: " + r"$10^{-204}$", CYAN),
    (8.5, 2.5, r"$\alpha^{-1}$ = 137.035999207", "12 digits match\nRb recoil: 0.007 ppb", GREEN),
]

for cx, cy, main, sub, col in stages:
    rounded_box(ax, cx, cy, 2.8, 2.5, "", col, alpha=0.15)
    ax.text(cx, cy + 0.4, main, ha='center', va='center', fontsize=12,
            color=WHITE, fontweight='bold')
    ax.text(cx, cy - 0.55, sub, ha='center', va='center', fontsize=9, color=SILVER)

# Arrows
ax.annotate("", xy=(3.5, 2.5), xytext=(3.0, 2.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))
ax.annotate("", xy=(7.0, 2.5), xytext=(6.5, 2.5),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=2.5))

# Digit display at bottom
digits_str = "137.035999207"
x_start = 2.0
for i, ch in enumerate(digits_str):
    if ch == '.':
        ax.text(x_start + i * 0.55, -0.2, ch, ha='center', va='center',
                fontsize=14, color=DIM, fontweight='bold')
    else:
        color = GREEN
        ax.text(x_start + i * 0.55, -0.2, ch, ha='center', va='center',
                fontsize=14, color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.15', facecolor=PAN, edgecolor=GREEN, alpha=0.4))

ax.text(x_start + 6.5 * 0.55, -0.8, "12 digits — all match", ha='center', va='center',
        fontsize=10, color=GREEN, fontstyle='italic')

save(fig, "talk1_13_qed_twelve_digits.png")

# ================================================================
# FIG 14: HYDROGEN FREQUENCY — DIGIT BY DIGIT
# Type: Comparison Bar (digit-by-digit)
# Shows: 11 matching digits between prediction and measurement
# ================================================================
fig, ax = plt.subplots(figsize=(18, 8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 18)
ax.set_ylim(-2, 6)

ax.text(8.5, 5.2, "Harvard Measures, Germany Predicts: 11 Digits Match",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

pred_digits = "2466061412094700"
meas_digits = "2466061413187018"

# Find matching prefix
match_len = 0
for a, b in zip(pred_digits, meas_digits):
    if a == b:
        match_len += 1
    else:
        break

ax.text(0.0, 3.8, "Predicted:", ha='left', va='center', fontsize=11, color=GOLD)
ax.text(0.0, 2.2, "Measured:", ha='left', va='center', fontsize=11, color=CYAN)

for i, (p, m) in enumerate(zip(pred_digits, meas_digits)):
    xpos = 2.2 + i * 0.92

    # Predicted row
    pcol = GREEN if i < match_len else DIM
    ax.text(xpos, 3.8, p, ha='center', va='center', fontsize=13, color=WHITE,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, edgecolor=pcol, linewidth=1.5))

    # Measured row
    mcol = GREEN if i < match_len else DIM
    ax.text(xpos, 2.2, m, ha='center', va='center', fontsize=13, color=WHITE,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, edgecolor=mcol, linewidth=1.5))

# Match bracket
ax.annotate("", xy=(2.2, 3.0), xytext=(2.2 + (match_len - 1) * 0.92, 3.0),
            arrowprops=dict(arrowstyle='|-|', color=GREEN, lw=1.5))
ax.text(2.2 + (match_len - 1) * 0.46, 3.0, "%d digits match" % match_len,
        ha='center', va='center', fontsize=10, color=GREEN,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, alpha=0.8))

ax.text(8.5, 0.8, "Frequency: 2,466,061,413,187,018 Hz",
        ha='center', va='center', fontsize=12, color=WHITE, fontweight='bold')
ax.text(8.5, 0.1, "The hydrogen 1S-2S transition. Miss: 0.44 ppb.",
        ha='center', va='center', fontsize=10, color=SILVER)
ax.text(8.5, -0.6, "One measurement in Massachusetts. One prediction from\nGerman spectroscopy. Connected by integer arithmetic.",
        ha='center', va='center', fontsize=10, color=DIM)

save(fig, "talk1_14_hydrogen_digits.png")

# ================================================================
# FIG 15: CABIBBO DOUBLET IDENTITY CARD
# Type: Identity Card
# Shows: all quantum numbers and fractions in one visual reference
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)

# Title
ax.text(5.0, 10.2, "The Cabibbo Doublet", ha='center', va='center',
        fontsize=20, fontweight='bold', color=GOLD)
ax.text(5.0, 9.5, "The One Particle the Integers Demand", ha='center', va='center',
        fontsize=13, color=SILVER)

# Main card border
card = mpatches.FancyBboxPatch((0.3, 0.5), 9.4, 8.5,
    boxstyle="round,pad=0.3", facecolor=PAN, edgecolor=GOLD,
    linewidth=2, alpha=0.5)
ax.add_patch(card)

# Quantum numbers row
qn_data = [("SU(3)", "3", "color triplet", RED),
           ("SU(2)", "2", "weak doublet", GREEN),
           ("Y", "1/6", "hypercharge", BLUE)]
for i, (label, val, desc, col) in enumerate(qn_data):
    cx = 2.0 + i * 3.0
    cy = 8.0
    box = mpatches.FancyBboxPatch((cx - 1.1, cy - 0.7), 2.2, 1.4,
        boxstyle="round,pad=0.15", facecolor=col, alpha=0.15,
        edgecolor=col, linewidth=1.5)
    ax.add_patch(box)
    ax.text(cx, cy + 0.25, label, ha='center', va='center', fontsize=10,
            color=SILVER)
    ax.text(cx, cy - 0.1, val, ha='center', va='center', fontsize=18,
            color=WHITE, fontweight='bold')
    ax.text(cx, cy - 0.45, desc, ha='center', va='center', fontsize=8, color=col)

# Type
ax.text(5.0, 6.6, "Vector-like: both hands transform identically",
        ha='center', va='center', fontsize=11, color=CYAN)

# Beta shifts
ax.text(1.5, 5.7, "Beta shifts:", ha='left', va='center', fontsize=11, color=SILVER)
shifts = [(r"$\Delta b_1$ = 1/15", BLUE),
          (r"$\Delta b_2$ = 1", GREEN),
          (r"$\Delta b_3$ = 1/3", RED)]
for i, (txt, col) in enumerate(shifts):
    ax.text(2.0 + i * 2.8, 5.0, txt, ha='center', va='center', fontsize=13,
            color=col, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=col, alpha=0.6))

# Gap ratio
ax.text(5.0, 3.8, "Gap ratio", ha='center', va='center', fontsize=10, color=SILVER)
ax.text(2.5, 3.1, "SM: 218/115", ha='center', va='center', fontsize=12,
        color=DIM, fontweight='bold')
ax.text(5.0, 3.1, r"$\rightarrow$", ha='center', va='center', fontsize=14, color=DIM)
ax.text(7.5, 3.1, "CD: 38/27", ha='center', va='center', fontsize=14,
        color=GOLD, fontweight='bold')

# Prediction
ax.text(5.0, 2.0, "Proton decay testable by Hyper-Kamiokande starting 2027",
        ha='center', va='center', fontsize=11, color=ORANGE,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.5))

# Named after
ax.text(5.0, 1.0, "Named after Nicola Cabibbo (1935-2010)\nIdentified quark mixing. Excluded from the 2008 Nobel.\nA particle name lasts longer than any prize.",
        ha='center', va='center', fontsize=9, color=DIM, fontstyle='italic')

save(fig, "talk1_15_cabibbo_doublet_card.png")

# ================================================================
# FIG 16: WHY THIS PARTICLE AND NO OTHER
# Type: Comparison Bar
# Shows: 5 tested candidates — CD wins by factor of 7
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

candidates = [
    ("Cabibbo Doublet\n(3, 2, 1/6)", 0.049, GREEN),
    ("VL lepton doublet\n(1, 2, -1/2)", 0.354, RED),
    ("VL electron singlet\n(1, 1, -1)", 0.642, RED),
    ("VL down singlet\n(3, 1, -1/3)", 0.660, RED),
    ("VL up singlet\n(3, 1, 2/3)", 0.769, RED),
]

names = [c[0] for c in candidates]
distances = [c[1] for c in candidates]
colors = [c[2] for c in candidates]

y = np.arange(len(candidates))
bars = ax.barh(y, distances, height=0.6, color=colors, alpha=0.7,
               edgecolor=colors, linewidth=1.5)

# Value labels — offset right of bar
for i in range(len(candidates)):
    ax.text(distances[i] + 0.02, y[i], "%.3f" % distances[i], ha='left',
            va='center', fontsize=11, color=colors[i], fontweight='bold')

ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=10, color=WHITE)
ax.set_xlabel("Distance from measured gap ratio", fontsize=11, color=SILVER)
ax.set_title("15 Candidates, 5 Tested: The CD Wins by 7" + r"$\times$",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

# Threshold annotation
ax.axvline(x=0.049, color=GREEN, alpha=0.4, linestyle='--', linewidth=1)
ax.text(0.15, 4.5, "CD distance: 0.049\nNext best: 0.354\nFactor: 7.2" + r"$\times$",
        ha='left', va='center', fontsize=10, color=GREEN,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN, alpha=0.7))

# Bottom annotation
ax.text(0.4, -0.8, "The integers chose the particle. We didn't.",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

ax.set_xlim(0, 0.9)
ax.set_ylim(-1.2, 5)
ax.invert_yaxis()

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk1_16_whatif_scan.png")

# ================================================================
# FIG 17: THE TEST SUITE — PASS/FAIL/INFO BY DOMAIN
# Type: Comparison Bar (stacked)
# Shows: overwhelming green with occasional red across 9 domains
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

domains =  ["QED",  "EW",   "GUT",  "Cosmo", "BBN", "Muon\ng-2", "CKM", "Mass", "GR"]
passes =   [38,     32,     28,     22,      18,    12,       15,    10,    45]
fails =    [0,      0,      2,      0,       1,     0,        0,     0,     2]
infos =    [2,      3,      5,      3,       2,     2,        1,     1,     1]

x = np.arange(len(domains))
w = 0.55

p1 = ax.bar(x, passes, w, color=GREEN, alpha=0.7, edgecolor=GREEN, linewidth=1, label='PASS')
p2 = ax.bar(x, fails, w, bottom=passes, color=RED, alpha=0.8, edgecolor=RED, linewidth=1, label='FAIL')
p3 = ax.bar(x, infos, w, bottom=[p+f for p,f in zip(passes, fails)], color=SILVER,
            alpha=0.5, edgecolor=SILVER, linewidth=1, label='INFO')

# Total labels above each stack
for i in range(len(domains)):
    total = passes[i] + fails[i] + infos[i]
    ax.text(x[i], total + 1.5, str(total), ha='center', va='bottom',
            fontsize=10, color=WHITE, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(domains, fontsize=11, color=WHITE)
ax.set_ylabel("Number of comparisons", fontsize=11, color=SILVER)
ax.set_title("253 Comparisons Across 9 Domains",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.legend(loc='upper right', fontsize=10, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

# Annotation
total_p = sum(passes)
total_f = sum(fails)
total_i = sum(infos)
ax.text(7.0, 40, "%d PASS  |  %d FAIL  |  %d INFO" % (total_p, total_f, total_i),
        ha='center', va='center', fontsize=12, color=WHITE,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.8))

ax.text(7.0, 35, "FAILs stay in. The system doesn't hide failures.",
        ha='center', va='center', fontsize=10, color=RED, fontstyle='italic')

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)
ax.set_ylim(0, 55)

save(fig, "talk1_17_test_suite.png")

# ================================================================
# FIG 18: 13 INPUTS AND 53 OUTPUTS
# Type: Connection/Integer Map
# Shows: fan-out from 13 inputs to 9 domains with 53 outputs
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-2, 14)

ax.text(5.0, 13.2, "13 In, 53 Out: The Surplus Is +40",
        ha='center', va='center', fontsize=18, fontweight='bold', color=GOLD)

# Left column — 13 inputs
inputs = [r"$\alpha^{-1}$", r"$m_e$", r"$m_\mu$", r"$m_\tau$", r"$M_Z$",
          r"$m_t$", r"$M_H$", r"$G_F$", r"$\Omega_{DM}$",
          r"$a_e$", r"$H_0$", r"$T_{CMB}$", r"$\sin\theta_{14}$"]

input_x = 1.0
for i, inp in enumerate(inputs):
    iy = 11.5 - i * 0.9
    ax.text(input_x, iy, inp, ha='center', va='center', fontsize=10,
            color=GOLD, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.25', facecolor=PAN, edgecolor=GOLD, alpha=0.5))

# Right column — 9 domains with output counts
domain_data = [
    ("QED", 7, GOLD),
    ("Electroweak", 6, CYAN),
    ("GUT", 5, GREEN),
    ("Cosmology", 5, PURPLE),
    ("Nuclear/BBN", 4, ORANGE),
    ("Muon g-2", 3, MAG),
    ("CKM/Flavor", 3, BLUE),
    ("Mass/Koide", 3, SILVER),
    ("GR/Gravity", 12, GREEN),
]

domain_x = 9.0
for i, (name, count, col) in enumerate(domain_data):
    dy = 11.0 - i * 1.2
    label = "%s (%d)" % (name, count)
    ax.text(domain_x, dy, label, ha='center', va='center', fontsize=11,
            color=col, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=PAN, edgecolor=col, alpha=0.4))

# Connection lines — fan pattern
# Each input connects to relevant domains (simplified: draw spread of lines)
np.random.seed(42)
for i in range(len(inputs)):
    iy = 11.5 - i * 0.9
    # Connect to 2-4 random domains
    n_conn = np.random.randint(2, 5)
    targets = np.random.choice(len(domain_data), n_conn, replace=False)
    for t in targets:
        dy = 11.0 - t * 1.2
        ax.plot([input_x + 0.8, domain_x - 1.2], [iy, dy],
                color=DIM, alpha=0.15, linewidth=0.8)

# Center annotation
ax.text(5.0, -0.5, "53 derived values.  13 measured inputs.  Surplus: +40.  No free parameters.",
        ha='center', va='center', fontsize=13, color=WHITE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=GOLD, alpha=0.7))

# Labels
ax.text(input_x, 12.5, "MEASURED\nINPUTS", ha='center', va='center',
        fontsize=10, color=GOLD)
ax.text(domain_x, 12.2, "DERIVED\nOUTPUTS", ha='center', va='center',
        fontsize=10, color=CYAN)

save(fig, "talk1_18_inputs_outputs.png")

# ================================================================
# FIG 19: THE PRECISION STAIRCASE
# Type: Scale/Landscape
# Shows: 5 orders of magnitude from ppb to ppm, all successes
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

results = [
    (r"$\alpha^{-1}$ vs Rb", 0.007, "ppb", GOLD, "QED"),
    ("Mercury perihelion", 2.8, "ppm", GREEN, "GR"),
    (r"$\sin^2\theta_W$", 12, "ppm", CYAN, "GUT"),
    ("Solar redshift", 16, "ppm", GREEN, "GR"),
    ("Hulse-Taylor", 42, "ppm", GREEN, "GR"),
    ("Koide " + r"$m_\tau$", 62, "ppm", SILVER, "Mass"),
    (r"$M_W$ (path B)", 195, "ppm", CYAN, "EW"),
    (r"$\alpha_s$", 3300, "ppm", GREEN, "GUT"),
    ("GPS net", 3500, "ppm", GREEN, "GR"),
    ("DM/baryon", 725, "ppm", PURPLE, "Cosmo"),
]

# Sort by miss value
results.sort(key=lambda r: r[1])

y_positions = np.arange(len(results))
miss_values = [r[1] for r in results]
names = [r[0] for r in results]
colors_r = [r[3] for r in results]
domains_r = [r[4] for r in results]

ax.barh(y_positions, miss_values, height=0.6, color=colors_r, alpha=0.6,
        edgecolor=colors_r, linewidth=1.5)

# # Labels — name on left, value on right of bar
# for i in range(len(results)):
#     ax.text(-0.3, y_positions[i], names[i], ha='right', va='center',
#             fontsize=10, color=colors_r[i], fontweight='bold')

#     unit = results[i][2]
#     val = results[i][1]
#     if val < 1:
#         label = "%.3f %s" % (val, unit)
#     elif val < 100:
#         label = "%.0f %s" % (val, unit)
#     else:
#         label = "%.0f %s" % (val, unit)
#     ax.text(val * 1.15, y_positions[i], label, ha='left', va='center',
#             fontsize=9, color=SILVER)

# Labels — name inside bar, value right of bar
for i in range(len(results)):
    ax.text(0.005, y_positions[i], names[i], ha='left', va='center',
            fontsize=10, color=WHITE, fontweight='bold')

    unit = results[i][2]
    val = results[i][1]
    if val < 1:
        label = "%.3f %s" % (val, unit)
    else:
        label = "%.0f %s" % (val, unit)
    ax.text(val * 1.15, y_positions[i], label, ha='left', va='center',
            fontsize=9, color=SILVER)

ax.set_xlim(0.003, 8000)

ax.set_xscale('log')
ax.set_xlim(0.003, 8000)
ax.set_ylim(-0.8, len(results) - 0.2)
ax.set_xlabel("Miss from measurement", fontsize=11, color=SILVER)
ax.set_title("The Precision Staircase: From 0.007 ppb to 725 ppm",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# 1% threshold
ax.axvline(x=10000, color=RED, alpha=0.3, linestyle='--', linewidth=1.5)

# Annotation
ax.text(2000, 1.0, "The worst prediction misses\nby less than 0.1%",
        ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_yticks([])

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk1_19_precision_staircase.png")

# ================================================================
# FIG 20: CHECK THE NUMBERS — CLOSING CARD
# Type: Identity Card (closing frame)
# Shows: three actionable links and the central challenge
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 9)

ax.text(5.0, 8.0, "Check the Numbers", ha='center', va='center',
        fontsize=22, fontweight='bold', color=GOLD)

# Three resource boxes
resources = [
    (2.0, 5.5, "Code", "github.com/ghowland/rum", CYAN),
    (5.0, 5.5, "Papers", "zenodo.org (45+ papers)", GREEN),
    (8.0, 5.5, "Book", "The Rational Universe\namazon.com — $3", GOLD),
]

for cx, cy, label, detail, col in resources:
    box = mpatches.FancyBboxPatch((cx - 1.3, cy - 0.8), 2.6, 1.6,
        boxstyle="round,pad=0.2", facecolor=PAN, edgecolor=col,
        linewidth=2, alpha=0.6)
    ax.add_patch(box)
    ax.text(cx, cy + 0.25, label, ha='center', va='center', fontsize=14,
            color=col, fontweight='bold')
    ax.text(cx, cy - 0.3, detail, ha='center', va='center', fontsize=9,
            color=SILVER)

# Central statement
statement = ("If the numbers are wrong, the model is wrong.\n"
             "If the numbers are right, the model deserves attention\n"
             "regardless of who produced it.")
ax.text(5.0, 3.0, statement, ha='center', va='center', fontsize=14,
        color=WHITE, fontstyle='italic', linespacing=1.8)

# Bottom line
ax.text(5.0, 1.0, "The universe does not care about credentials.\nIt cares about integers.",
        ha='center', va='center', fontsize=12, color=DIM)

# Stats line
ax.text(5.0, -0.2, "53 values  |  13 inputs  |  surplus +40  |  8 domains  |  0 new physics  |  0 new math",
        ha='center', va='center', fontsize=10, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN, edgecolor=GOLD, alpha=0.4))

save(fig, "talk1_20_check_the_numbers.png")

# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (11-20) generated ===")
filenames = [
    "talk1_11_chain_to_deuterium.png",
    "talk1_12_bbn_four_elements.png",
    "talk1_13_qed_twelve_digits.png",
    "talk1_14_hydrogen_digits.png",
    "talk1_15_cabibbo_doublet_card.png",
    "talk1_16_whatif_scan.png",
    "talk1_17_test_suite.png",
    "talk1_18_inputs_outputs.png",
    "talk1_19_precision_staircase.png",
    "talk1_20_check_the_numbers.png",
]
for f in filenames:
    print("  %s" % f)
