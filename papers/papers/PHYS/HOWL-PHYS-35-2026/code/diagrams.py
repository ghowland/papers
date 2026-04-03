#!/usr/bin/env python3
"""
HOWL PHYS-35 Diagrams — The No-Threshold Puzzle
8 figures covering the threshold investigation.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import os

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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
    p = os.path.join(outdir, name)
    fig.savefig(p, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % p)

def style_ax(ax):
    ax.set_facecolor(PAN)
    ax.tick_params(colors=DIM, labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)

# ================================================================
# DATA (from phys35_no_threshold_puzzle.py — source of truth)
# ================================================================

alpha_s_meas = 0.1180

# M_VL scan
mvl_data = [
    (200,  0.11597, 1.7225, -0.1436),
    (300,  0.11476, 2.7462, -0.2323),
    (400,  0.11392, 3.4593, -0.2951),
    (500,  0.11327, 4.0050, -0.3438),
    (750,  0.11212, 4.9804, -0.4323),
    (1000, 0.11132, 5.6602, -0.4950),
    (1500, 0.11021, 6.6013, -0.5833),
    (2000, 0.10944, 7.2573, -0.6460),
    (3000, 0.10836, 8.1659, -0.7342),
    (4000, 0.10762, 8.7994, -0.7969),
    (5000, 0.10704, 9.2846, -0.8454),
    (6000, 0.10658, 9.6771, -0.8851),
]

nt_miss = 0.3251
nt_as = 0.11838

# Step sensitivity
nt_steps = [(200, 0.3246), (500, 0.3251), (1000, 0.3253), (2000, 0.3255)]
th_steps = [(200, 4.0049), (500, 4.0050), (1000, 4.0050), (2000, 4.0048)]

# Soft threshold
soft_data = [
    (200,  0.10957, 7.1438),
    (500,  0.10750, 8.9004),
    (1000, 0.10588, 10.2687),
    (2000, 0.10430, 11.6101),
    (4000, 0.10276, 12.9138),
]

# ================================================================
# FIG 1: M_VL SCAN — MISS vs M_VL WITH NO-THRESHOLD LINE
# Type: Running
# Shows: Monotonic degradation, no-threshold as unbeatable baseline
# ================================================================
print("Fig 1: M_VL Scan")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"THE $M_{VL}$ SCAN — Every Threshold Is Worse",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

mvl_x = [d[0] for d in mvl_data]
mvl_miss = [d[2] for d in mvl_data]

ax.plot(mvl_x, mvl_miss, color=CYAN, linewidth=2.5, marker='o',
        markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
        markerfacecolor=CYAN, label='Hard threshold')

# Soft threshold points
soft_x = [d[0] for d in soft_data]
soft_miss = [d[2] for d in soft_data]
ax.plot(soft_x, soft_miss, color=RED, linewidth=2, marker='s',
        markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
        markerfacecolor=RED, linestyle='--', label='Soft threshold')

# No-threshold horizontal line
ax.axhline(y=nt_miss, color=GOLD, linewidth=2.5, linestyle='-',
           label='No threshold: 0.33%%')
ax.fill_between([0, 7000], 0, nt_miss, color=GOLD, alpha=0.04)

# Label the no-threshold region
ax.text(4500, nt_miss + 0.3, 'NO THRESHOLD: 0.33%%',
        fontsize=13, color=GOLD, fontweight='bold')

# Mark the measured 3-sigma band
three_sigma = 0.1180 * 0.009 / 0.1180 * 100  # roughly 0.76%
ax.axhspan(0, three_sigma, color=GREEN, alpha=0.04)
ax.text(5500, three_sigma - 0.3, r'Within 3$\sigma$', fontsize=9,
        color=GREEN, style='italic')

# Annotations
ax.annotate(r'$M_{VL}$ = 200 GeV' + '\nmiss = 1.72%%\n(best hard threshold)',
            xy=(200, 1.7225), xytext=(800, 2.5),
            fontsize=9, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5),
            linespacing=1.3)

ax.text(3000, 11, 'More CD running\n= better prediction',
        fontsize=11, color=WHITE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_xlabel(r'$M_{VL}$ (GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$\alpha_s$ miss from measured (%%)', fontsize=12, color=SILVER)
ax.set_xlim(0, 6500)
ax.set_ylim(0, 14)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys35_01_mvl_scan.png')

# ================================================================
# FIG 2: ENERGY RANGE DIAGRAM — CD ACTIVE REGIONS
# Type: Scale
# Shows: Where the CD contributes for each configuration
# ================================================================
print("Fig 2: Energy Range Diagram")

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("CD ACTIVE RANGE — Where the Cabibbo Doublet Contributes",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

log_MZ = np.log10(91.2)
log_GUT = 15.6

configs = [
    ('No threshold', log_MZ, log_GUT, GOLD, 0.33),
    (r'Hard $M_{VL}$=200', np.log10(200), log_GUT, CYAN, 1.72),
    (r'Hard $M_{VL}$=500', np.log10(500), log_GUT, BLUE, 4.01),
    (r'Hard $M_{VL}$=1000', np.log10(1000), log_GUT, GREEN, 5.66),
    (r'Hard $M_{VL}$=2000', np.log10(2000), log_GUT, ORANGE, 7.26),
    (r'Hard $M_{VL}$=6000', np.log10(6000), log_GUT, RED, 9.68),
]

y_positions = np.arange(len(configs), 0, -1) * 1.2

for i, (name, log_start, log_end, color, miss) in enumerate(configs):
    y = y_positions[i]

    # SM region (before threshold)
    if log_start > log_MZ + 0.01:
        ax.barh(y, log_start - log_MZ, 0.6, left=log_MZ,
                color=DIM, alpha=0.3, edgecolor=DIM, linewidth=1)

    # CD region (after threshold)
    ax.barh(y, log_end - log_start, 0.6, left=log_start,
            color=color, alpha=0.5, edgecolor=color, linewidth=2)

    # Label
    ax.text(log_MZ - 0.3, y, name, fontsize=10, color=color,
            ha='right', va='center', fontweight='bold')

    # Miss label
    ax.text(log_GUT + 0.3, y, 'miss: %.2f%%' % miss,
            fontsize=10, color=color, va='center', fontweight='bold')

# Energy landmarks
for log_e, label in [(log_MZ, r'$M_Z$'), (np.log10(500), '500'),
                      (np.log10(1000), '1 TeV'), (np.log10(6000), '6 TeV'),
                      (log_GUT, r'$M_{GUT}$')]:
    ax.axvline(x=log_e, color=DIM, linewidth=0.5, linestyle=':', alpha=0.5)
    ax.text(log_e, 0.2, label, fontsize=8, color=DIM, ha='center')

# Legend
ax.text(8, 0.8, 'Grey = SM only, Colored = CD active',
        fontsize=10, color=SILVER, ha='center')

ax.set_xlabel(r'$\log_{10}(E$ / GeV)', fontsize=12, color=SILVER)
ax.set_xlim(0, 17)
ax.set_ylim(-0.2, y_positions[0] + 1)
ax.set_yticks([])

save(fig, 'phys35_02_energy_ranges.png')

# ================================================================
# FIG 3: ALPHA_S vs M_VL WITH MEASURED BAND
# Type: Threshold
# Shows: The curve approaching but never reaching measured
# ================================================================
print("Fig 3: Alpha_s vs M_VL")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"$\alpha_s$ PREDICTION vs THRESHOLD POSITION",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

mvl_as = [d[1] for d in mvl_data]

ax.plot(mvl_x, mvl_as, color=CYAN, linewidth=2.5, marker='o',
        markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
        markerfacecolor=CYAN, label='Hard threshold')

# Soft
soft_as = [d[1] for d in soft_data]
ax.plot(soft_x, soft_as, color=RED, linewidth=2, marker='s',
        markersize=8, markeredgecolor=WHITE, markeredgewidth=1.5,
        markerfacecolor=RED, linestyle='--', label='Soft threshold')

# Measured band
ax.axhspan(alpha_s_meas - 0.0009, alpha_s_meas + 0.0009,
           color=MAG, alpha=0.12)
ax.axhline(y=alpha_s_meas, color=MAG, linewidth=2, linestyle='--',
           label=r'Measured $\alpha_s$ = 0.1180')

# No-threshold
ax.axhline(y=nt_as, color=GOLD, linewidth=2.5,
           label='No threshold: 0.11838')

# Label
ax.annotate('No threshold\n(INSIDE 1' + r'$\sigma$' + ')',
            xy=(3000, nt_as), xytext=(4000, nt_as + 0.003),
            fontsize=11, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax.annotate('All thresholds\nUNDERSHOOT',
            xy=(3000, 0.108), xytext=(4500, 0.105),
            fontsize=11, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))

ax.set_xlabel(r'$M_{VL}$ (GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$\alpha_s$ predicted', fontsize=12, color=SILVER)
ax.set_xlim(0, 6500)
ax.set_ylim(0.100, 0.122)
ax.legend(fontsize=9, loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys35_03_alpha_s_vs_mvl.png')

# ================================================================
# FIG 4: STEP SENSITIVITY — FLAT ADVANTAGE RATIO
# Type: Threshold
# Shows: The advantage doesn't change with step count
# ================================================================
print("Fig 4: Step Sensitivity")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.3})
style_ax(ax1)
style_ax(ax2)
fig.suptitle("STEP SENSITIVITY — The Advantage Is Not Numerical",
             fontsize=17, fontweight='bold', color=GOLD, y=0.97)

# Left: miss vs steps for both
steps_x = [d[0] for d in nt_steps]
nt_y = [d[1] for d in nt_steps]
th_y = [d[1] for d in th_steps]

ax1.set_title('Miss from Measured (%)', fontsize=13, color=WHITE,
              fontweight='bold', pad=12)

ax1.plot(steps_x, nt_y, color=GOLD, linewidth=2.5, marker='o',
         markersize=10, markeredgecolor=WHITE, markeredgewidth=2,
         markerfacecolor=GOLD, label='No threshold')
ax1.plot(steps_x, th_y, color=CYAN, linewidth=2.5, marker='s',
         markersize=10, markeredgecolor=WHITE, markeredgewidth=2,
         markerfacecolor=CYAN, label=r'Threshold $M_{VL}$=500')

for i in range(4):
    ax1.text(steps_x[i], nt_y[i] - 0.25, '%.4f' % nt_y[i],
             fontsize=8, color=GOLD, ha='center')
    ax1.text(steps_x[i], th_y[i] + 0.15, '%.4f' % th_y[i],
             fontsize=8, color=CYAN, ha='center')

ax1.set_xlabel('Euler steps', fontsize=11, color=SILVER)
ax1.set_ylabel('Miss (%%)', fontsize=11, color=SILVER)
ax1.set_xlim(0, 2200)
ax1.set_ylim(0, 5)
ax1.legend(fontsize=9, loc='center right', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE)

# Right: advantage ratio
ratios = [th_y[i] / nt_y[i] for i in range(4)]

ax2.set_title('Advantage Ratio (Threshold / No-Threshold)', fontsize=13,
              color=WHITE, fontweight='bold', pad=12)

ax2.plot(steps_x, ratios, color=ORANGE, linewidth=2.5, marker='D',
         markersize=10, markeredgecolor=WHITE, markeredgewidth=2,
         markerfacecolor=ORANGE)

for i in range(4):
    ax2.text(steps_x[i], ratios[i] + 0.3, '%.1f' % ratios[i] + r'$\times$',
             fontsize=12, color=WHITE, ha='center', fontweight='bold')

ax2.axhline(y=12.3, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax2.text(1800, 12.3 + 0.4, 'constant at 12.3' + r'$\times$',
         fontsize=10, color=DIM)

ax2.set_xlabel('Euler steps', fontsize=11, color=SILVER)
ax2.set_ylabel('Ratio', fontsize=11, color=SILVER)
ax2.set_xlim(0, 2200)
ax2.set_ylim(10, 15)

save(fig, 'phys35_04_step_sensitivity.png')

# ================================================================
# FIG 5: SIGMOID vs STEP FUNCTION
# Type: Geometry
# Shows: How the sigmoid provides less CD contribution
# ================================================================
print("Fig 5: Sigmoid vs Step")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THRESHOLD FUNCTIONS — Step vs Sigmoid",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

mu = np.linspace(50, 3000, 500)
M_VL = 500.0

# Step function
f_step = np.where(mu >= M_VL, 1.0, 0.0)

# Sigmoid
f_sig = 1.0 / (1.0 + (M_VL / mu)**2)

# No threshold
f_none = np.ones_like(mu)

ax.plot(mu, f_none, color=GOLD, linewidth=2.5, linestyle='-',
        label='No threshold (f = 1 always)')
ax.plot(mu, f_step, color=CYAN, linewidth=2.5,
        label='Hard threshold (step at 500 GeV)')
ax.plot(mu, f_sig, color=RED, linewidth=2,
        label=r'Soft threshold: $f = 1/(1+(M_{VL}/\mu)^2)$')

# Shade the difference: what sigmoid misses vs step
ax.fill_between(mu, f_sig, f_step, where=(mu >= M_VL),
                color=CYAN, alpha=0.08)
ax.text(1200, 0.6, 'CD contribution\nlost by sigmoid',
        fontsize=10, color=CYAN, ha='center', style='italic',
        linespacing=1.3)

# Shade what step misses vs no-threshold
ax.fill_between(mu, f_step, f_none, where=(mu < M_VL),
                color=GOLD, alpha=0.08)
ax.text(250, 0.6, 'CD contribution\nlost by threshold',
        fontsize=10, color=GOLD, ha='center', style='italic',
        linespacing=1.3)

# Mark M_VL
ax.axvline(x=M_VL, color=WHITE, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(M_VL + 20, 0.05, r'$M_{VL}$ = 500 GeV', fontsize=10,
        color=WHITE, fontweight='bold')

# f = 0.5 mark on sigmoid
ax.scatter([M_VL], [0.5], s=150, color=RED, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(M_VL + 80, 0.45, 'f = 0.5 at ' + r'$M_{VL}$',
        fontsize=9, color=RED)

ax.set_xlabel(r'Energy $\mu$ (GeV)', fontsize=12, color=SILVER)
ax.set_ylabel('CD fraction f(' + r'$\mu$' + ')', fontsize=12, color=SILVER)
ax.set_xlim(50, 3000)
ax.set_ylim(-0.05, 1.15)
ax.legend(fontsize=10, loc='lower right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys35_05_threshold_functions.png')

# ================================================================
# FIG 6: DECOUPLING THEOREM INVERSION
# Type: Comparison
# Shows: What the theorem predicts vs what we observe
# ================================================================
print("Fig 6: Decoupling Inversion")

fig = plt.figure(figsize=(18, 11), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis('off')

fig.suptitle("THE DECOUPLING INVERSION — Every Expectation Reversed",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

def rbox(ax, x, y, w, h, text, color, fs=11, sub=None):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.5",
        facecolor='#0f0f1a', edgecolor=color, linewidth=2))
    if sub:
        ax.text(x+w/2, y+h/2+1.5, text, fontsize=fs,
                fontweight='bold', color=color, ha='center', va='center')
        ax.text(x+w/2, y+h/2-1.5, sub, fontsize=9,
                color=SILVER, ha='center', va='center')
    else:
        ax.text(x+w/2, y+h/2, text, fontsize=fs,
                fontweight='bold', color=color, ha='center', va='center')

rows = [
    ("Heavy particle decouples\nbelow M", "CD contribution needed\nbelow " + r"$M_{VL}$"),
    ("Step function is\nleading-order approx", "Step function is worse\nthan no threshold"),
    ("Smooth threshold is\nbetter approximation", "Smooth threshold is\nthe WORST option"),
    ("Below-threshold corrections\nare " + r"$O(\mu/M)^2$" + " suppressed", "Below-threshold corrections\nappear to be O(1)"),
    ("EFT without CD valid\nbelow " + r"$M_{VL}$", "EFT WITH CD more\naccurate below " + r"$M_{VL}$"),
]

y_start = 50
dy = 9.5

for i, (expect, observe) in enumerate(rows):
    y = y_start - i * dy

    # Expectation
    rbox(ax, 3, y, 30, 7, expect, DIM, 10)

    # Arrow
    ax.annotate('', xy=(38, y+3.5), xytext=(34, y+3.5),
                arrowprops=dict(arrowstyle='->', color=RED, lw=2))

    # Observation
    rbox(ax, 39, y, 30, 7, observe, RED, 10)

    # X mark
    ax.text(72, y+3.5, r'$\times$', fontsize=24, color=RED,
            ha='center', va='center', fontweight='bold')

# Headers
ax.text(18, 56, 'THEOREM PREDICTS', fontsize=14, color=DIM,
        ha='center', fontweight='bold')
ax.text(54, 56, 'WE OBSERVE', fontsize=14, color=RED,
        ha='center', fontweight='bold')
ax.text(72, 56, 'INVERTED?', fontsize=12, color=RED,
        ha='center', fontweight='bold')

# Bottom note
ax.text(50, 1,
        'The theorem is not wrong — the leading-order threshold\n'
        'implementation is a poor approximation for the CD.',
        fontsize=11, color=SILVER, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM),
        linespacing=1.4)

save(fig, 'phys35_06_decoupling_inversion.png')

# ================================================================
# FIG 7: CD FRACTION vs MISS — PERFECT CORRELATION
# Type: Running
# Shows: One variable explains everything
# ================================================================
print("Fig 7: CD Fraction vs Miss")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THE CORRELATION — CD Running Fraction vs Prediction Quality",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Estimate CD fraction for each configuration
# log range: log10(M_GUT/M_Z) = 15.6 - 1.96 = 13.64
total_log = 15.6 - np.log10(91.2)

hard_fracs = [(total_log - (np.log10(d[0]) - np.log10(91.2))) / total_log * 100
              for d in mvl_data]
hard_misses = [d[2] for d in mvl_data]

# Soft fractions (approximate — weighted integral)
# Sigmoid integral is approximately: total_log - M_VL_contribution
# Use approximate effective fraction from the sigmoid integral
soft_fracs = []
for mvl, _, miss in soft_data:
    # Numerical integral of sigmoid over log range
    log_mu = np.linspace(np.log10(91.2), 15.6, 1000)
    mu_vals = 10**log_mu
    f_vals = 1.0 / (1.0 + (float(mvl) / mu_vals)**2)
    frac = np.mean(f_vals) * 100
    soft_fracs.append(frac)
soft_misses = [d[2] for d in soft_data]

# Plot hard threshold
ax.scatter(hard_fracs, hard_misses, s=150, color=CYAN, zorder=5,
           edgecolors=WHITE, linewidth=1.5, label='Hard threshold')

# Plot soft threshold
ax.scatter(soft_fracs, soft_misses, s=150, color=RED, zorder=5,
           marker='s', edgecolors=WHITE, linewidth=1.5, label='Soft threshold')

# No-threshold point
ax.scatter([100], [nt_miss], s=300, color=GOLD, zorder=6,
           edgecolors=WHITE, linewidth=2.5, label='No threshold')
ax.annotate('No threshold\n100%% CD\nmiss = 0.33%%',
            xy=(100, nt_miss), xytext=(94, 2.5),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            linespacing=1.3)

# Trend line through all points
all_fracs = hard_fracs + soft_fracs + [100]
all_misses = hard_misses + soft_misses + [nt_miss]
z = np.polyfit(all_fracs, all_misses, 2)
p = np.poly1d(z)
x_fit = np.linspace(min(all_fracs) - 2, 102, 100)
ax.plot(x_fit, p(x_fit), color=DIM, linewidth=1, linestyle=':', alpha=0.5)

ax.text(80, 10, 'More CD running\n= lower miss',
        fontsize=12, color=WHITE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=DIM))

ax.set_xlabel('Effective CD running fraction (%%)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$\alpha_s$ miss from measured (%%)', fontsize=12, color=SILVER)
ax.set_xlim(55, 103)
ax.set_ylim(0, 14)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys35_07_cd_fraction.png')

# ================================================================
# FIG 8: THREE EXPLANATIONS — DECISION TREE
# Type: Connection
# Shows: Which future tests resolve which explanations
# ================================================================
print("Fig 8: Three Explanations")

fig = plt.figure(figsize=(18, 12), facecolor=BG)
ax = fig.add_axes([0.02, 0.02, 0.96, 0.90])
ax.set_facecolor(BG)
ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis('off')

fig.suptitle("THREE EXPLANATIONS — Future Tests Will Decide",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Top: the finding
rbox(ax, 25, 58, 50, 8, 'No-threshold advantage: 12.3' + r'$\times$',
     GOLD, 14, 'Physical, not numerical (step test)')

# Three branches
explanations = [
    (5, 42, 'A: Virtual Propagation', GREEN,
     'CD loops contribute\nbelow ' + r'$M_{VL}$',
     'RK4: persists\n3-loop: persists'),
    (35, 42, 'B: Effective Resummation', ORANGE,
     'No-thresh captures\nhigher-order effects',
     'RK4: persists\n3-loop: SHRINKS'),
    (65, 42, 'C: Error Cancellation', RED,
     'Threshold error cancels\nmissing correction',
     'RK4: CHANGES\n3-loop: vanishes'),
]

for x, y, title, color, desc, pred in explanations:
    rbox(ax, x, y, 28, 8, title, color, 11, desc)

    # Arrow from top
    ax.annotate('', xy=(x+14, y+8), xytext=(50, 58),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

    # Prediction box below
    rbox(ax, x, y-14, 28, 10, 'Predictions:', color, 10, pred)
    ax.annotate('', xy=(x+14, y-4), xytext=(x+14, y),
                arrowprops=dict(arrowstyle='->', color=DIM, lw=1))

# Decision tests at bottom
rbox(ax, 10, 10, 30, 8, 'PHYS-37: RK4 Integrator', CYAN, 12,
     r'$O(h^4)$ replaces $O(h)$ Euler')
rbox(ax, 55, 10, 35, 8, 'PHYS-38: Three-Loop Estimate', PURPLE, 12,
     'Does 3L change the advantage?')

# Arrows from predictions to tests
ax.annotate('', xy=(25, 18), xytext=(19, 28),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.5))
ax.annotate('', xy=(25, 18), xytext=(49, 28),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.5))
ax.annotate('', xy=(72, 18), xytext=(49, 28),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.5))
ax.annotate('', xy=(72, 18), xytext=(79, 28),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1, alpha=0.5))

# Bottom verdict
ax.text(50, 2,
        'Two future papers will resolve the puzzle.\n'
        'If both show advantage persisting: Explanation A wins (virtual propagation).',
        fontsize=11, color=WHITE, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM),
        linespacing=1.4)

save(fig, 'phys35_08_three_explanations.png')

# ================================================================
print()
print("=" * 70)
print("PHYS-35 DIAGRAMS — 8 FIGURES GENERATED")
print("=" * 70)

filenames = [
    'phys35_01_mvl_scan.png',
    'phys35_02_energy_ranges.png',
    'phys35_03_alpha_s_vs_mvl.png',
    'phys35_04_step_sensitivity.png',
    'phys35_05_threshold_functions.png',
    'phys35_06_decoupling_inversion.png',
    'phys35_07_cd_fraction.png',
    'phys35_08_three_explanations.png',
]

for i, name in enumerate(filenames, 1):
    print("  Fig %d: %s" % (i, name))
    