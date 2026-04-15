#!/usr/bin/env python3
"""
HOWL Video Talk Diagrams — Outline 3, Slides 11-20
10 figures covering: CD beta shifts, gap ratio SM vs CD, Z boson decays,
EW fan-out, QED staircase, alpha scaling, cosmological chain,
elemental abundances, muon g-2, muon sensitivity.
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
# FIG 11: ONE PARTICLE, THREE SHIFTS
# Type: Comparison Bar (before/after)
# Shows: relative magnitudes of CD beta shifts across three sectors
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

sectors = ["U(1)", "SU(2)", "SU(3)"]
sm_vals = [4.100, -3.167, -7.000]
cd_vals = [4.167, -2.167, -6.667]
sm_fracs = ["41/10", r"$-$19/6", r"$-$7"]
cd_fracs = ["25/6", r"$-$13/6", r"$-$20/3"]
shifts = ["+1/15", "+1", "+1/3"]
pct_changes = ["+1.6%", "+31.6%", "+4.8%"]
bar_colors = [BLUE, GREEN, RED]

x = np.arange(len(sectors))
w = 0.30

for i in range(len(sectors)):
    sm_h = abs(sm_vals[i])
    cd_h = abs(cd_vals[i])

    ax.bar(x[i] - w/2, sm_h, w, color=DIM, alpha=0.5, label='SM' if i == 0 else None)
    ax.bar(x[i] + w/2, cd_h, w, color=bar_colors[i], alpha=0.7, label='CD' if i == 0 else None)

    # SM fraction label above bar
    ax.text(x[i] - w/2, sm_h + 0.25, sm_fracs[i], ha='center', va='bottom',
            fontsize=10, color=DIM)

    # CD fraction label above bar — offset higher to avoid overlap
    ax.text(x[i] + w/2, cd_h + 0.55, cd_fracs[i], ha='center', va='bottom',
            fontsize=11, color=GOLD, fontweight='bold')

    # Shift label higher still
    ax.text(x[i], max(sm_h, cd_h) + 1.3, "shift: %s" % shifts[i], ha='center',
            va='bottom', fontsize=10, color=bar_colors[i], fontweight='bold')

    # Percentage change at top
    ax.text(x[i], max(sm_h, cd_h) + 1.9, pct_changes[i], ha='center',
            va='bottom', fontsize=9, color=SILVER)

ax.set_xticks(x)
ax.set_xticklabels(sectors, fontsize=13, color=WHITE)
ax.set_ylabel(r"|$\beta$ coefficient|", fontsize=11, color=SILVER)
ax.set_title("Before and After the Cabibbo Doublet", fontsize=16,
             fontweight='bold', color=GOLD, pad=15)

ax.legend(loc='upper right', fontsize=10, facecolor=PAN, labelcolor=WHITE)

ax.text(1.0, 0.5, "Three shifts. Three exact fractions: 1/15, 1, 1/3.\n"
        "Every prediction in the model flows from these.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(0, 10)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_11_cd_three_shifts.png")


# ================================================================
# FIG 12: THE GAP RATIO — SM VS CD
# Type: Connection/Integer Map (two panels)
# Shows: 218/115 looks random, 38/27 looks meaningful
# ================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)
fig.suptitle("The Gap Ratio: Why Only This Particle Works",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# -- Left: SM (dim, random-looking) --
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

ax1.text(5, 9.0, "Standard Model", ha='center', va='center',
         fontsize=14, fontweight='bold', color=DIM)
ax1.text(5, 7.0, "218 / 115", ha='center', va='center',
         fontsize=34, fontweight='bold', color=DIM)
ax1.text(5, 5.5, "= 1.8957...", ha='center', va='center',
         fontsize=16, color=DIM)
ax1.text(5, 4.0, "218 and 115", ha='center', va='center',
         fontsize=12, color=DIM)
ax1.text(5, 3.2, "Large numbers.\nNo obvious structure.\nNo physical meaning visible.",
         ha='center', va='center', fontsize=10, color=DIM, fontstyle='italic')
ax1.text(5, 1.5, "Miss from measurement: 39.6%", ha='center', va='center',
         fontsize=11, color=RED, fontweight='bold')

# -- Right: CD (bright, structured) --
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

ax2.text(5, 9.0, "With Cabibbo Doublet", ha='center', va='center',
         fontsize=14, fontweight='bold', color=GOLD)
ax2.text(5, 7.0, "38 / 27", ha='center', va='center',
         fontsize=34, fontweight='bold', color=GOLD)
ax2.text(5, 5.5, "= 1.4074...", ha='center', va='center',
         fontsize=16, color=WHITE)

# Factorizations
ax2.text(3.0, 4.2, "38 = 2 " + r"$\times$" + " 19", ha='center', va='center',
         fontsize=12, color=CYAN, fontweight='bold')
ax2.text(7.0, 4.2, "27 = 3" + r"$^3$", ha='center', va='center',
         fontsize=12, color=CYAN, fontweight='bold')
ax2.text(3.0, 3.5, "2 = vector-like\n19 = weak count", ha='center', va='center',
         fontsize=9, color=GREEN)
ax2.text(7.0, 3.5, "3 = color charges\ncubed", ha='center', va='center',
         fontsize=9, color=GREEN)
ax2.text(5, 1.5, "Miss from measurement: 3.6%", ha='center', va='center',
         fontsize=11, color=GREEN, fontweight='bold')

# Arrow between panels (use fig coordinates)
fig.text(0.50, 0.50, "add one\nparticle", ha='center', va='center',
         fontsize=10, color=GOLD,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

fig.text(0.50, 0.06, "14 other candidates tested. None produces small meaningful integers.\nThe integers chose the particle.",
         ha='center', va='center', fontsize=11, color=SILVER, fontstyle='italic')

save(fig, "talk3_12_gap_ratio_sm_vs_cd.png")


# ================================================================
# FIG 13: Z BOSON DECAY — FIVE CHANNELS
# Type: Comparison Bar
# Shows: five independent predictions all matching measurement
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

channels = [r"Z $\rightarrow$ e$^+$e$^-$",
            r"Z $\rightarrow$ $\mu^+\mu^-$",
            r"Z $\rightarrow$ $\tau^+\tau^-$",
            r"Z $\rightarrow$ hadrons",
            r"Z $\rightarrow$ invisible ($\nu\bar{\nu}$)"]
predicted = [83.91, 83.91, 83.79, 1744.4, 501.7]
measured =  [83.92, 83.99, 84.08, 1744.4, 499.0]
misses =    ["0.01%", "0.10%", "0.35%", "0.00%", "0.54%"]
chan_colors = [CYAN, GREEN, BLUE, RED, PURPLE]

x = np.arange(len(channels))
w = 0.30

for i in range(len(channels)):
    ax.bar(x[i] - w/2, predicted[i], w, color=GOLD, alpha=0.6)
    ax.bar(x[i] + w/2, measured[i], w, color=chan_colors[i], alpha=0.7)

    top = max(predicted[i], measured[i])
    ax.text(x[i], top + top * 0.04, misses[i], ha='center', va='bottom',
            fontsize=10, color=chan_colors[i], fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(channels, fontsize=10, color=WHITE)
ax.set_ylabel("Partial width (MeV)", fontsize=11, color=SILVER)
ax.set_title("The Z Boson Dies Five Ways " + r"$-$" + " All Predicted",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

# Legend
ax.text(0.5, 1600, "GOLD = predicted    COLOR = measured", ha='left',
        va='center', fontsize=9, color=SILVER)

# Neutrino annotation
ax.annotate("This channel counts\nneutrino types.\nAnswer: exactly 3.",
            xy=(4, 501.7), xytext=(3.0, 1200),
            fontsize=9, color=PURPLE, ha='center',
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(2.0, 100 + 150, "One set of inputs. Five decay channels. Five matches.\n"
        "The Z boson doesn't know which department you work in.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_ylim(0, 1950)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_13_z_boson_five_channels.png")


# ================================================================
# FIG 14: THREE INPUTS, FIFTEEN OUTPUTS
# Type: Connection/Integer Map
# Shows: fan-out from 3 inputs to 15 EW outputs
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 12)

ax.text(6, 11.3, "The Electroweak Fan-Out", ha='center', va='center',
        fontsize=17, fontweight='bold', color=GOLD)

# Three inputs on left
inputs = [
    (1.5, 8.5, r"$\alpha_{em}$ = 1/137", GOLD),
    (1.5, 6.0, r"$M_Z$ = 91188 MeV", CYAN),
    (1.5, 3.5, r"$m_t$ = 172.6 GeV", GREEN),
]

for ix, iy, itxt, icol in inputs:
    rounded_box(ax, ix, iy, 2.5, 1.0, itxt, icol, fontsize=9, alpha=0.2)

# Fifteen outputs on right, in three columns
outputs = [
    r"$M_W$", r"$\Gamma_Z$", r"$\Gamma$(ee)", r"$\Gamma$($\mu\mu$)", r"$\Gamma$($\tau\tau$)",
    r"$\Gamma$(had)", r"$\Gamma$(inv)", r"$R_l$", r"$\sigma_{had}$", r"sin$^2\theta_{eff}$",
    r"$\Delta\rho$", r"$\Delta r$", r"$N_\nu$", r"$\kappa_Z$", r"$A_{FB}$",
]
out_colors = [GREEN]*10 + [CYAN]*5

for i, (otxt) in enumerate(outputs):
    col_idx = i // 5
    row_idx = i % 5
    ox = 7.0 + col_idx * 2.2
    oy = 9.5 - row_idx * 1.5
    ocol = out_colors[i]

    rounded_box(ax, ox, oy, 1.8, 0.8, otxt, ocol, fontsize=8, alpha=0.15)

# Connection lines
for ix, iy, itxt, icol in inputs:
    for i in range(len(outputs)):
        col_idx = i // 5
        row_idx = i % 5
        ox = 7.0 + col_idx * 2.2
        oy = 9.5 - row_idx * 1.5
        ax.plot([ix + 1.3, ox - 1.0], [iy, oy],
                color=DIM, alpha=0.08, linewidth=0.6)

# Surplus annotation
ax.text(6, 0.5, "3 in  " + r"$\rightarrow$" + "  15 out.    Surplus: +12.    No free parameters.",
        ha='center', va='center', fontsize=13, color=WHITE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN))

# Labels
ax.text(1.5, 10.5, "INPUTS", ha='center', va='center', fontsize=10, color=GOLD)
ax.text(9.0, 10.8, "DERIVED OUTPUTS", ha='center', va='center', fontsize=10, color=GREEN)

save(fig, "talk3_14_ew_fanout.png")


# ================================================================
# FIG 15: THE QED PRECISION STAIRCASE
# Type: Scale/Landscape (staircase)
# Shows: each step builds on previous, precision degrades gracefully
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 16)
ax.set_ylim(-1, 11)

ax.text(8, 10.3, "From One Electron to Eleven Digits in Germany",
        ha='center', va='center', fontsize=17, fontweight='bold', color=GOLD)

steps = [
    (1.5, 8.5, r"$a_e$ measured", "Harvard Penning trap", "13 digits", GOLD),
    (4.0, 7.0, r"$\alpha$ extracted", "Newton inversion\nresidual: " + r"$10^{-204}$", "12 digits", CYAN),
    (6.5, 5.5, r"$R_\infty$ derived", "Rydberg constant", "11 digits", GREEN),
    (9.0, 4.0, r"$a_0$ derived", "Bohr radius", "10 digits", BLUE),
    (11.5, 2.5, r"$\mu_0$ derived", "vacuum permeability", "10 digits", PURPLE),
    (14.0, 1.0, "H 1S-2S\npredicted", "laser in Garching\n11 digits match", "11 digits", GOLD),
]

for i, (sx, sy, slabel, sdesc, sprec, scol) in enumerate(steps):
    rounded_box(ax, sx, sy, 2.3, 1.2, "", scol, alpha=0.15)
    ax.text(sx, sy + 0.2, slabel, ha='center', va='center', fontsize=10,
            color=WHITE, fontweight='bold')
    ax.text(sx, sy - 0.3, sdesc, ha='center', va='center', fontsize=7,
            color=SILVER)

    # Precision badge above
    ax.text(sx + 1.0, sy + 0.6, sprec, ha='center', va='center', fontsize=8,
            color=scol, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG))

    # Arrow to next step
    if i < len(steps) - 1:
        nx, ny = steps[i+1][0], steps[i+1][1]
        ax.annotate("", xy=(nx - 1.0, ny + 0.5), xytext=(sx + 1.0, sy - 0.5),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))

# Staircase line behind
stair_x = [s[0] for s in steps]
stair_y = [s[1] for s in steps]
ax.plot(stair_x, stair_y, color=DIM, linewidth=1, linestyle=':', alpha=0.3)

ax.text(8, -0.3, "One measurement on one electron in Massachusetts.\n"
        "Integer arithmetic. Predictions confirmed by a laser in Garching.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic')

save(fig, "talk3_15_qed_staircase.png")


# ================================================================
# FIG 16: THE ALPHA SCALING LAW
# Type: Running/Convergence
# Shows: miss scales linearly with alpha power — systematic, not lucky
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

powers = [1, 2, 3]
misses_ppb = [0.22, 0.44, 0.66]
labels = [r"$\alpha^1$ quantities" + "\n(direct)", r"$\alpha^2$ quantities" + "\n(Rydberg, Bohr)",
          r"$\alpha^3$ projected"]
pt_colors = [GOLD, CYAN, DIM]

# Fit line
ax.plot([0.5, 3.5], [0.11, 0.77], color=GOLD, linewidth=2, linestyle='--', alpha=0.6)

for i in range(len(powers)):
    ax.scatter([powers[i]], [misses_ppb[i]], s=250, color=pt_colors[i], zorder=5,
               marker='o' if i < 2 else 'D')
    ax.text(powers[i] + 0.15, misses_ppb[i] + 0.03, "%.2f ppb" % misses_ppb[i],
            ha='left', va='bottom', fontsize=11, color=pt_colors[i], fontweight='bold')
    ax.text(powers[i] + 0.15, misses_ppb[i] - 0.04, labels[i],
            ha='left', va='top', fontsize=9, color=SILVER)

ax.set_xlabel(r"Power of $\alpha$", fontsize=12, color=SILVER)
ax.set_ylabel("Miss (ppb)", fontsize=12, color=SILVER)
ax.set_title(r"Miss Scales with $\alpha$ Power: 0.22 ppb per Power",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(2.5, 0.15, "Slope = 0.22 ppb / power", ha='center', va='center',
        fontsize=11, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.text(2.0, 0.72, "The uncertainty propagates exactly as\n"
        "mathematics predicts. Systematic, not lucky.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.0, 0.85)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_16_alpha_scaling.png")


# ================================================================
# FIG 17: THE LONGEST CHAIN — INTEGERS TO DEUTERIUM
# Type: Progression/Sequence
# Shows: 7 steps across 5 domains with domain walls
# ================================================================
fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-0.5, 18)
ax.set_ylim(-1.5, 8)

ax.text(9, 7.3, "7 Steps from Gauge Integers to Primordial Chemistry",
        ha='center', va='center', fontsize=16, fontweight='bold', color=GOLD)

# Two rows to fit 7 boxes
row1 = [
    (1.8, 5.0, r"$\beta$: 25/6," + "\n" + r"$-$13/6, $-$20/3", "group theory", GOLD),
    (5.4, 5.0, "integers:\n22, 13", "number theory", CYAN),
    (9.0, 5.0, "(22/13)" + r"$\pi$" + "\n= 5.317", "cosmology\n725 ppm", GREEN),
    (12.6, 5.0, r"$\Omega_b$" + " = 0.0490", "cosmology\n727 ppm", BLUE),
]

row2 = [
    (3.5, 1.8, r"$\eta_{10}$" + " = 6.09", "particle cosmo\n0.24%", PURPLE),
    (8.0, 1.8, "BBN nuclear\nreactions", "nuclear physics\ntextbook", ORANGE),
    (12.5, 1.8, "D/H = 2.531\n" + r"$\times 10^{-5}$", "obs. astronomy\n0.12" + r"$\sigma$", MAG),
]

all_boxes = row1 + row2

for bx, by, blabel, bsub, bcol in all_boxes:
    rounded_box(ax, bx, by, 2.8, 1.4, "", bcol, alpha=0.15)
    ax.text(bx, by + 0.2, blabel, ha='center', va='center', fontsize=9,
            color=WHITE, fontweight='bold')
    ax.text(bx, by - 0.45, bsub, ha='center', va='center', fontsize=7,
            color=bcol)

# Arrows within row1
for i in range(len(row1) - 1):
    ax.annotate("", xy=(row1[i+1][0] - 1.5, row1[i+1][1]),
                xytext=(row1[i][0] + 1.5, row1[i][1]),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2, alpha=0.5))

# Arrow from row1 last to row2 first
ax.annotate("", xy=(row2[0][0] + 0.5, row2[0][1] + 0.7),
            xytext=(row1[-1][0] - 0.5, row1[-1][1] - 0.7),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2, alpha=0.5))

# Arrows within row2
for i in range(len(row2) - 1):
    ax.annotate("", xy=(row2[i+1][0] - 1.5, row2[i+1][1]),
                xytext=(row2[i][0] + 1.5, row2[i][1]),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2, alpha=0.5))

# Domain walls (vertical dashed lines between domains)
walls_x = [3.6, 7.2, 10.8, 5.7, 10.2]
for wx in walls_x:
    ax.plot([wx, wx], [0.8, 6.2], color=RED, linewidth=1, linestyle=':', alpha=0.2)

ax.text(9, -0.5, "Seven steps. Five domains. One chain. Nothing breaks.",
        ha='center', va='center', fontsize=12, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=PAN))

save(fig, "talk3_17_cosmo_chain.png")


# ================================================================
# FIG 18: ELEMENTAL ABUNDANCES — PREDICTED VS OBSERVED
# Type: Comparison Bar
# Shows: three green agreements and one red lithium problem
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

elements = ["Deuterium\n(D/H)", "Helium-4\n(" + r"$Y_p$" + ")", "Helium-3", "Lithium-7"]

# Normalized to ratio of predicted/measured for visual comparison
pred_norm = [1.002, 1.015, 1.04, 2.96]
meas_norm = [1.0, 1.0, 1.0, 1.0]
misses = [r"0.12$\sigma$", r"0.94$\sigma$", r"0.36$\sigma$", r"2.96$\times$"]
elem_colors = [GREEN, GREEN, CYAN, RED]

x = np.arange(len(elements))
w = 0.30

for i in range(len(elements)):
    ax.bar(x[i] - w/2, pred_norm[i], w, color=GOLD, alpha=0.6)
    ax.bar(x[i] + w/2, meas_norm[i], w, color=elem_colors[i], alpha=0.7)

    top = max(pred_norm[i], meas_norm[i])
    ax.text(x[i], top + 0.08, misses[i], ha='center', va='bottom',
            fontsize=12, color=elem_colors[i], fontweight='bold')

ax.axhline(y=1.0, color=SILVER, linewidth=1, linestyle='--', alpha=0.3)

ax.set_xticks(x)
ax.set_xticklabels(elements, fontsize=11, color=WHITE)
ax.set_ylabel("Predicted / Measured ratio", fontsize=11, color=SILVER)
ax.set_title("What the Big Bang Made: Predicted from Integers",
             fontsize=16, fontweight='bold', color=GOLD, pad=15)

ax.text(0.5, 2.7, "GOLD = predicted    COLOR = measured", ha='left',
        va='center', fontsize=9, color=SILVER)

# Lithium annotation
ax.annotate("The lithium problem.\nEvery model has this.\nWe inherit it " + r"$-$" + "\nsame nuclear physics.",
            xy=(3, 2.96), xytext=(2.0, 2.5),
            fontsize=9, color=RED, ha='center',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

ax.set_ylim(0.0, 3.3)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_18_bbn_abundances.png")


# ================================================================
# FIG 19: THE MUON G-2 — EVERYONE GETS THE SAME ANSWER
# Type: Threshold/Region
# Shows: measured band, two theory bands, RUM dot matching standard
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Values (shifted for display: subtract baseline)
baseline = 11659000e-10
measured = 11659206e-10 - baseline  # 206
meas_unc = 4.1e-10
dispersive = 11659181e-10 - baseline  # 181
lattice = 11659200e-10 - baseline  # 200

# Measured band
ax.axhspan(measured - meas_unc * 3, measured + meas_unc * 3, color=MAG, alpha=0.05)
ax.axhspan(measured - meas_unc, measured + meas_unc, color=MAG, alpha=0.12)
ax.axhline(y=measured, color=MAG, linewidth=1.5, linestyle='--', alpha=0.6)

# Theory bands (shown as error bars)
disp_unc = 3.7e-10
latt_unc = 4.0e-10

# Dispersive theory
ax.scatter([1.5], [dispersive], s=200, color=CYAN, zorder=5, marker='s')
ax.plot([1.5, 1.5], [dispersive - disp_unc, dispersive + disp_unc],
        color=CYAN, linewidth=2)
ax.text(2.0, dispersive, "Dispersive\nhadronic\n" + r"6.5$\sigma$ tension",
        ha='left', va='center', fontsize=9, color=CYAN)

# Lattice theory
ax.scatter([3.0], [lattice], s=200, color=GREEN, zorder=5, marker='s')
ax.plot([3.0, 3.0], [lattice - latt_unc, lattice + latt_unc],
        color=GREEN, linewidth=2)
ax.text(3.5, lattice, "Lattice\nhadronic\n" + r"~1$\sigma$ tension",
        ha='left', va='center', fontsize=9, color=GREEN)

# RUM point
ax.scatter([1.5], [dispersive - 0.5e-10], s=150, color=GOLD, zorder=6, marker='*')
ax.text(0.7, dispersive - 2e-10, "RUM prediction\n(matches dispersive\nexactly)",
        ha='center', va='center', fontsize=8, color=GOLD,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG))

# Measured label
ax.text(4.5, measured + 3e-10, "Fermilab\nmeasurement",
        ha='center', va='bottom', fontsize=10, color=MAG, fontweight='bold')

ax.set_xlim(0.3, 5.5)
ax.set_ylim(baseline + 170e-10 - baseline, baseline + 220e-10 - baseline)
ax.set_ylabel(r"$a_\mu \times 10^{10}$ (offset from 11659000)", fontsize=10, color=SILVER)
ax.set_xticks([])
ax.set_title("The Muon Anomaly: Same Answer, Same Dispute",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(3.0, 175e-10, "The dispute is between two methods of computing the\n"
        "hadronic contribution. We get the same answer as everyone else.\n"
        "We inherit the tension. We don't generate it.",
        ha='center', va='center', fontsize=9, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_19_muon_g2.png")


# ================================================================
# FIG 20: HEAVY PARTICLE SENSITIVITY
# Type: Comparison Bar
# Shows: muon bar 207x longer than electron bar — sensitivity ratio
# ================================================================
fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Two bars — electron and muon sensitivity
labels = ["Electron", "Muon"]
sensitivities = [1, 207]
bar_colors_s = [CYAN, ORANGE]

y = np.arange(len(labels))

for i in range(len(labels)):
    ax.barh(y[i], sensitivities[i], height=0.4, color=bar_colors_s[i], alpha=0.7)

# Labels
ax.text(1.5, 0, "Light.  Virtual heavy particles\ncontribute " + r"$\sim 10^{-12}$" + " to g-2.\nBelow measurement precision.",
        ha='left', va='center', fontsize=10, color=CYAN)
ax.text(sensitivities[1] + 3, 1, "207" + r"$\times$" + " heavier.\n"
        "Virtual heavy particles\ncontribute " + r"$\sim 10^{-8}$" + " to g-2.\nMeasurable. The anomaly lives here.",
        ha='left', va='center', fontsize=10, color=ORANGE)

# Scale factor arrow
ax.annotate(r"$\times$ 207", xy=(sensitivities[1], 0.5), xytext=(80, 0.5),
            fontsize=14, color=GOLD, fontweight='bold', ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=13, color=WHITE)
ax.set_xlabel("Relative sensitivity to virtual heavy particles", fontsize=11, color=SILVER)
ax.set_title("Why the Muon Sees What the Electron Doesn't",
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

ax.text(100, -0.6, "Same physics. Same diagrams. Different sensitivity\nbecause of different inertia.",
        ha='center', va='center', fontsize=10, color=SILVER, fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG))

ax.set_xlim(0, 280)
ax.set_ylim(-1.0, 2.0)
for spine in ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
ax.tick_params(colors=DIM)

save(fig, "talk3_20_muon_sensitivity.png")


# ================================================================
# SUMMARY
# ================================================================
print("\n=== All 10 slides (outline 3, 11-20) generated ===")
filenames = [
    "talk3_11_cd_three_shifts.png",
    "talk3_12_gap_ratio_sm_vs_cd.png",
    "talk3_13_z_boson_five_channels.png",
    "talk3_14_ew_fanout.png",
    "talk3_15_qed_staircase.png",
    "talk3_16_alpha_scaling.png",
    "talk3_17_cosmo_chain.png",
    "talk3_18_bbn_abundances.png",
    "talk3_19_muon_g2.png",
    "talk3_20_muon_sensitivity.png",
]
for f in filenames:
    print("  %s" % f)
