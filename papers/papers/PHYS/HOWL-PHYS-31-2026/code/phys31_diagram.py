#!/usr/bin/env python3
"""
HOWL PHYS-31 Diagrams — Statistical Control
8 figures covering the null result and its meaning.
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

# ================================================================
# GLOBAL STYLE
# ================================================================
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
# DATA (from phys31_statistical_control.py — source of truth)
# ================================================================

PI = math.pi
ALPHA = 1.0 / 137.035999177
PI_POWERS = [1.0/(PI*PI), 1.0/PI, 1.0, PI, PI*PI]
PI_LABELS = [r'$\pi^{-2}$', r'$\pi^{-1}$', r'$\pi^0$', r'$\pi^1$', r'$\pi^2$']

beta_pool = [1, 3, 5, 6, 7, 10, 13, 15, 19, 20, 22, 25, 27, 38, 41]

targets = [
    ("DM/baryon",     5.320,  0.5),
    (r"$\Omega_b$",   4.93,   1.0),
    (r"$\Omega_{DM}$",26.4,   1.0),
    (r"$H_0$ ratio",  0.9189, 1.0),
    (r"$\sin^2\theta_W$", 0.23122, 0.5),
    (r"$n_s$",        0.965,  0.5),
    (r"$\log\Lambda$",-121.54, 0.3),
    (r"$\alpha_s$",   0.1180, 1.0),
]

hits_info = [
    (0, "(22/13)"+r"$\pi$",     5.317, 0.065),
    (1, r"$(1/2)\pi^2$",        4.935, 0.097),
    (2, r"$(25/3)\pi$",         26.18, 0.834),
    (3, r"$(38/3)\pi^2\alpha$", 0.9123, 0.721),
    (4, "3/13",                 0.2308, 0.195),
    (7, r"$(10/27)\pi^{-1}$",  0.1179, 0.091),
]

# Monte Carlo results
score_dist = {3: 22, 4: 275, 5: 1575, 6: 3987, 7: 4141}
n_trials = 10000
beta_score = 6
p_value = 0.8128
mean_random = 6.195
std_random = 0.814

# ================================================================
# FIG 1: FORMULA SPACE TILING
# Type: Scale
# Shows: How (p/q)*pi^b candidates tile the number line densely
# ================================================================
print("Fig 1: Formula Space Tiling")

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THE FORMULA SPACE — Why Random Integers Hit Targets",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Generate all candidate values from the beta pool
candidates = []
for i in range(len(beta_pool)):
    p = beta_pool[i]
    for j in range(len(beta_pool)):
        if i == j:
            continue
        q = beta_pool[j]
        ratio = float(p) / float(q)
        for pw in PI_POWERS:
            candidates.append(ratio * pw)
            candidates.append(ratio * pw * ALPHA)
    for pw in PI_POWERS:
        candidates.append(float(p) * pw)
        candidates.append(float(p) * pw * ALPHA)

# Filter to positive values in plottable range
cands_pos = [c for c in candidates if 0.01 < c < 200]

# Plot as vertical ticks on log scale
log_cands = np.log10(cands_pos)
ax.scatter(log_cands, np.zeros_like(log_cands) + 3,
           marker='|', s=80, color=CYAN, alpha=0.15, linewidths=0.5)

# Mark the targets
target_colors = [GREEN, GREEN, GREEN, GREEN, GOLD, ORANGE, RED, GOLD]
for ti, (name, val, tol) in enumerate(targets):
    if val > 0:
        lv = np.log10(val)
        tol_lo = np.log10(val * (1 - tol/100))
        tol_hi = np.log10(val * (1 + tol/100))
    else:
        lv = np.log10(abs(val))
        tol_lo = np.log10(abs(val) * (1 - tol/100))
        tol_hi = np.log10(abs(val) * (1 + tol/100))

    color = target_colors[ti]
    hit = ti in [h[0] for h in hits_info]

    y_pos = 6 + ti * 2.5
    ax.plot([tol_lo, tol_hi], [y_pos, y_pos], color=color,
            linewidth=6, alpha=0.4, solid_capstyle='round')
    ax.scatter([lv], [y_pos], s=120, color=color, zorder=5,
              edgecolors=WHITE, linewidth=1.5)
    marker = r'$\checkmark$' if hit else r'$\times$'
    ax.text(lv + 0.08, y_pos + 0.5, '%s %s' % (name, marker),
            fontsize=9, color=color, fontweight='bold', va='bottom')

# Label the candidate band
ax.text(0.5, 1, '~2,250 candidate values from 15 integers',
        fontsize=11, color=CYAN, ha='center', style='italic')

ax.set_xlabel(r'$\log_{10}$(value)', fontsize=12, color=SILVER)
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1, 28)
ax.set_yticks([])

# Annotation
ax.text(1.8, 25, 'Candidates tile the\nnumber line so densely\nthat hits are EXPECTED,\nnot special.',
        fontsize=12, color=WHITE, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

save(fig, 'phys31_01_formula_space.png')

# ================================================================
# FIG 2: TRACK A vs TRACK B — DYNAMICS vs NUMEROLOGY
# Type: Running + Comparison
# Shows: The structural difference between validated and parked
# ================================================================
print("Fig 2: Track A vs Track B")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                 gridspec_kw={'wspace': 0.35})
style_ax(ax1)
style_ax(ax2)

fig.suptitle("DYNAMICS vs NUMEROLOGY — Why Track A Survives and Track B Doesn't",
             fontsize=16, fontweight='bold', color=GOLD, y=0.97)

# Left: Track A — coupling running
ax1.set_title('TRACK A: Coupling Running\n(Validated)', fontsize=13,
              color=GREEN, fontweight='bold', pad=15)

log_E = np.linspace(2.0, 16, 400)
L = (log_E - np.log10(91.2)) * np.log(10) / (2 * PI)

b1_CD = 25.0/6
b2_CD = -13.0/6
b3_CD = -20.0/3

inv_a1 = 63.210 - b1_CD * L
inv_a2 = 31.685 - b2_CD * L
inv_a3 = 8.475 - b3_CD * L

ax1.plot(log_E, inv_a1, color=BLUE, linewidth=2.5, label=r'$1/\alpha_1$')
ax1.plot(log_E, inv_a2, color=GREEN, linewidth=2.5, label=r'$1/\alpha_2$')
ax1.plot(log_E, inv_a3, color=RED, linewidth=2.5, label=r'$1/\alpha_3$')

ax1.text(9, 15, r'$\alpha_s$ = 0.1184' + '\nmiss: 0.33%\nwithin ' + r'1$\sigma$',
         fontsize=11, color=GOLD, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

ax1.set_xlabel(r'$\log_{10}(E$/GeV)', fontsize=11, color=SILVER)
ax1.set_ylabel(r'$1/\alpha_i$', fontsize=11, color=SILVER)
ax1.set_xlim(1.5, 16.5)
ax1.set_ylim(-2, 70)
ax1.legend(fontsize=9, loc='upper left', facecolor=PAN, edgecolor=DIM,
           labelcolor=WHITE)

ax1.text(9, 62, 'ONE prediction per observable\nZERO free parameters\nTests the RUNNING',
         fontsize=9, color=GREEN, ha='center', va='top')

# Right: Track B — formula scatter
ax2.set_title('TRACK B: Formula Scan\n(Parked: p = 0.81)', fontsize=13,
              color=RED, fontweight='bold', pad=15)

# Scatter random formula values
np.random.seed(2026)
n_scatter = 300
scatter_x = np.random.uniform(-2, 2.2, n_scatter)
scatter_y = np.random.uniform(0.5, 8.5, n_scatter)

ax2.scatter(scatter_x, scatter_y, s=15, color=DIM, alpha=0.3, marker='.')

# Mark the 6 beta pool hits
hit_vals = [5.317, 4.935, 26.18, 0.9123, 0.2308, 0.1179]
hit_labels = ['DM/b', r'$\Omega_b$', r'$\Omega_{DM}$',
              r'$H_0$', r'$\sin^2\theta_W$', r'$\alpha_s$']
hit_y = [1, 2, 3, 4, 5, 6]

for i in range(6):
    lv = np.log10(hit_vals[i]) if hit_vals[i] > 0 else 0
    ax2.scatter([lv], [hit_y[i]], s=200, color=ORANGE, zorder=5,
                edgecolors=WHITE, linewidth=2)
    ax2.text(lv + 0.15, hit_y[i], hit_labels[i], fontsize=9,
             color=ORANGE, fontweight='bold', va='center')

# Target regions
for ti, (name, val, tol) in enumerate(targets[:6]):
    if val > 0:
        ax2.axvline(x=np.log10(val), color=DIM, linewidth=0.5,
                    linestyle=':', alpha=0.3)

ax2.set_xlabel(r'$\log_{10}$(formula value)', fontsize=11, color=SILVER)
ax2.set_ylabel('Target index', fontsize=11, color=SILVER)
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-0.5, 9)

ax2.text(0, 8, '~2,250 formulas scanned\n6/8 hits — but 81% of\nrandom pools do the same',
         fontsize=9, color=RED, ha='center', va='top')

ax2.text(0, -0.3, 'THOUSANDS of candidates per target',
         fontsize=10, color=RED, ha='center', fontweight='bold')

save(fig, 'phys31_02_dynamics_vs_numerology.png')

# ================================================================
# FIG 3: SCORE DISTRIBUTION WITH BETA POOL MARKED
# Type: Comparison
# Shows: Where the beta pool sits — dead center in the distribution
# ================================================================
print("Fig 3: Score Distribution")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("RANDOM SCORE DISTRIBUTION — Beta Pool Is Average",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

scores = sorted(score_dist.keys())
counts = [score_dist[s] for s in scores]
fracs = [c / n_trials * 100 for c in counts]

bars = ax.bar(scores, fracs, 0.7, color=DIM, alpha=0.6,
              edgecolor=SILVER, linewidth=1.5)

# Color the beta pool score bar
beta_idx = scores.index(beta_score)
bars[beta_idx].set_facecolor(ORANGE)
bars[beta_idx].set_edgecolor(ORANGE)
bars[beta_idx].set_alpha(0.8)

# Labels on bars
for i, s in enumerate(scores):
    ax.text(s, fracs[i] + 1.2, '%.1f%%' % fracs[i], fontsize=12,
            color=WHITE, ha='center', fontweight='bold')
    ax.text(s, fracs[i] + 4, '%d' % counts[i], fontsize=9,
            color=SILVER, ha='center')

# Beta pool marker
ax.annotate('BETA POOL\nscore = 6\n' + r'$-$0.24$\sigma$',
            xy=(6, fracs[beta_idx]),
            xytext=(4.2, 35),
            fontsize=12, color=ORANGE, fontweight='bold',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

# Mean line
ax.axvline(x=mean_random, color=CYAN, linewidth=2, linestyle='--',
           label='Random mean = %.2f' % mean_random)
ax.text(mean_random + 0.1, 43, 'mean = %.2f' % mean_random,
        fontsize=10, color=CYAN, fontweight='bold')

# p-value region
ax.axvspan(5.5, 7.5, ymin=0, ymax=1, color=RED, alpha=0.04)
ax.text(7.3, 38, 'p = 0.81\n81% of pools\nscore ' + r'$\geq$ 6',
        fontsize=11, color=RED, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

ax.set_xlabel('Number of targets hit (out of 8)', fontsize=12, color=SILVER)
ax.set_ylabel('Fraction of random pools (%)', fontsize=12, color=SILVER)
ax.set_xlim(2, 8)
ax.set_ylim(0, 48)
ax.legend(fontsize=10, loc='upper left', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys31_03_score_distribution.png')

# ================================================================
# FIG 4: CUMULATIVE P-VALUE WITH GATE THRESHOLD
# Type: Threshold/Region
# Shows: The gate line at p=0.05 that the curve never approaches
# ================================================================
print("Fig 4: Cumulative P-Value")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THE GATE — p-value Never Approaches 0.05",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Cumulative from the score distribution
scores_sorted = sorted(score_dist.keys(), reverse=True)
cumulative = {}
running = 0
for s in scores_sorted:
    running += score_dist[s]
    cumulative[s] = running / n_trials

# Plot cumulative >= score
score_x = sorted(cumulative.keys())
cum_y = [cumulative[s] for s in score_x]

ax.bar(score_x, [c * 100 for c in cum_y], 0.7,
       color=CYAN, alpha=0.4, edgecolor=CYAN, linewidth=1.5)

for i, s in enumerate(score_x):
    ax.text(s, cum_y[i] * 100 + 2, '%.1f%%' % (cum_y[i] * 100),
            fontsize=11, color=WHITE, ha='center', fontweight='bold')

# Mark beta pool score
ax.scatter([beta_score], [cumulative[beta_score] * 100], s=300,
           color=ORANGE, zorder=5, edgecolors=WHITE, linewidth=2.5)
ax.annotate('Beta pool: score = %d\np = %.1f%%' % (beta_score, p_value * 100),
            xy=(beta_score, p_value * 100),
            xytext=(beta_score - 1.3, p_value * 100 - 15),
            fontsize=12, color=ORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))

# Gate threshold lines
ax.axhline(y=5, color=RED, linewidth=2.5, linestyle='--',
           label='Gate: p < 5% (Track B survives)')
ax.axhline(y=1, color=MAG, linewidth=1.5, linestyle=':',
           label='High confidence: p < 1%')

ax.fill_between([2.5, 8.5], 0, 5, color=GREEN, alpha=0.05)
ax.text(3.5, 2.5, 'TRACK B SURVIVES\n(p < 5%)', fontsize=10,
        color=GREEN, fontweight='bold', ha='center')

ax.fill_between([2.5, 8.5], 5, 100, color=RED, alpha=0.03)
ax.text(3.5, 55, 'TRACK B PARKED\n(p > 5%)', fontsize=13,
        color=RED, fontweight='bold', ha='center')

ax.set_xlabel(r'Minimum score (hits $\geq$ N)', fontsize=12, color=SILVER)
ax.set_ylabel('Fraction of random pools (%)', fontsize=12, color=SILVER)
ax.set_xlim(2.5, 8)
ax.set_ylim(0, 108)
ax.legend(fontsize=10, loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys31_04_gate_threshold.png')

# ================================================================
# FIG 5: SIX HITS ON LOG SCALE WITH TOLERANCE BANDS
# Type: Threshold/Region
# Shows: Each hit's quality — formula vs measured with error band
# ================================================================
print("Fig 5: Six Hits Quality")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("THE SIX HITS — Formula vs Measured with Tolerance Bands",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

hit_names = ['DM/baryon', r'$\Omega_b \times 100$', r'$\Omega_{DM} \times 100$',
             r'$H_0$ ratio', r'$\sin^2\theta_W$', r'$\alpha_s$']
hit_measured = [5.320, 4.93, 26.4, 0.9189, 0.23122, 0.1180]
hit_formula_val = [5.317, 4.935, 26.18, 0.9123, 0.2308, 0.1179]
hit_formula_str = [r'$\frac{22}{13}\pi$', r'$\frac{1}{2}\pi^2$',
                   r'$\frac{25}{3}\pi$', r'$\frac{38}{3}\pi^2\alpha$',
                   r'$\frac{3}{13}$', r'$\frac{10}{27\pi}$']
hit_tol = [0.5, 1.0, 1.0, 1.0, 0.5, 1.0]
hit_miss = [0.065, 0.097, 0.834, 0.721, 0.195, 0.091]

y_pos = np.arange(len(hit_names))
colors_h = [GREEN, GREEN, ORANGE, ORANGE, GOLD, GOLD]

for i in range(len(hit_names)):
    meas = hit_measured[i]
    form = hit_formula_val[i]
    tol_abs = meas * hit_tol[i] / 100

    # Tolerance band
    ax.barh(y_pos[i], 2 * tol_abs, 0.4, left=meas - tol_abs,
            color=colors_h[i], alpha=0.15, edgecolor=colors_h[i], linewidth=1)

    # Measured value
    ax.scatter([meas], [y_pos[i]], s=180, color=MAG, zorder=5,
               marker='D', edgecolors=WHITE, linewidth=1.5)

    # Formula value
    ax.scatter([form], [y_pos[i]], s=180, color=colors_h[i], zorder=5,
               edgecolors=WHITE, linewidth=1.5)

    # Label
    ax.text(meas + tol_abs * 1.5, y_pos[i] + 0.15,
            '%s  miss: %.3f%%' % (hit_formula_str[i], hit_miss[i]),
            fontsize=10, color=colors_h[i], fontweight='bold', va='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(hit_names, fontsize=11, color=SILVER)
ax.set_xlabel('Value (linear scale per target)', fontsize=12, color=SILVER)
ax.set_ylim(-0.8, 6.2)

# Since values span different ranges, we use broken axis effect
# by just labeling clearly
ax.text(0.5, 0.02, r'Magenta $\diamond$ = measured, colored $\bullet$ = formula, band = tolerance',
        fontsize=10, color=SILVER, ha='center',
        transform=ax.transAxes)

# Note: different x ranges per target make a single linear x-axis awkward
# Use normalized miss instead
ax2 = ax.twiny()
style_ax(ax2)
ax2.set_xlabel('', fontsize=1, color=BG)  # hide
ax2.set_xticks([])

save(fig, 'phys31_05_six_hits.png')

# ================================================================
# FIG 6: CANDIDATE DENSITY HISTOGRAM
# Type: Scale
# Shows: The sheer density of formula values — why hits happen
# ================================================================
print("Fig 6: Candidate Density")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("CANDIDATE DENSITY — 2,250 Formula Values from 15 Integers",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Histogram of log10(|candidates|)
log_cands_all = []
for c in candidates:
    if abs(c) > 1e-4:
        log_cands_all.append(np.log10(abs(c)))

ax.hist(log_cands_all, bins=80, range=(-3.5, 3.5), color=CYAN, alpha=0.5,
        edgecolor=CYAN, linewidth=0.5)

# Mark target positions
for ti, (name, val, tol) in enumerate(targets):
    lv = np.log10(abs(val))
    hit = ti in [h[0] for h in hits_info]
    color = GREEN if hit else RED
    ax.axvline(x=lv, color=color, linewidth=2, linestyle='-', alpha=0.8)
    y_label = 95 + ti * 12
    ax.text(lv + 0.05, y_label, name, fontsize=9, color=color,
            fontweight='bold', rotation=0, va='bottom')

ax.set_xlabel(r'$\log_{10}$(|formula value|)', fontsize=12, color=SILVER)
ax.set_ylabel('Number of candidates in bin', fontsize=12, color=SILVER)
ax.set_xlim(-3.5, 3.5)

# Annotation
ax.text(2.5, ax.get_ylim()[1] * 0.85,
        'Green = HIT\nRed = MISS\n\nEvery target sits\nin a dense region\nof candidates',
        fontsize=11, color=WHITE, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=DIM))

save(fig, 'phys31_06_candidate_density.png')

# ================================================================
# FIG 7: sin2_tW — RUNNING vs FORMULA
# Type: Running
# Shows: The two mechanisms producing similar values
# ================================================================
print("Fig 7: sin2_tW Two Mechanisms")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle(r"$\sin^2\theta_W$: Two Paths to the Same Number",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# The running: sin2_tW evolves from 3/8 at M_GUT to 0.228 at M_Z
log_E = np.linspace(2, 16, 400)
# Simple model: linear interpolation from 0.375 at GUT to 0.228 at M_Z
sin2_running = 0.375 - (0.375 - 0.228) * (16 - log_E) / (16 - 2)

ax.plot(log_E, sin2_running, color=GREEN, linewidth=2.5,
        label='Track A: RGE running from 3/8')

# Mark tree level
ax.scatter([15.4], [0.375], s=200, color=DIM, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.text(15.4, 0.38, '3/8 = 0.375\n(tree level)', fontsize=10,
        color=DIM, fontweight='bold', ha='right')

# Mark the Track A prediction at M_Z
ax.scatter([np.log10(91.2)], [0.228], s=200, color=GREEN, zorder=5,
           edgecolors=WHITE, linewidth=2)
ax.annotate('Track A prediction\n0.22845 (miss 1.2%)',
            xy=(np.log10(91.2), 0.228),
            xytext=(4, 0.21),
            fontsize=10, color=GREEN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# Track B: the formula 3/13
ax.axhline(y=3.0/13.0, color=ORANGE, linewidth=2, linestyle='--',
           label='Track B: 3/13 = 0.2308')
ax.text(12, 3.0/13.0 + 0.004, '3/13 = 0.2308 (formula scan)',
        fontsize=10, color=ORANGE, fontweight='bold')

# Measured value band
ax.axhspan(0.23118, 0.23126, color=MAG, alpha=0.25)
ax.axhline(y=0.23122, color=MAG, linewidth=2,
           label='Measured: 0.23122')
ax.text(12, 0.23122 - 0.005, 'measured', fontsize=10, color=MAG)

# The distinction box
ax.text(8, 0.32,
        'Track A: solves differential equation\n'
        '   Input: two couplings + CD betas\n'
        '   Output: ONE number (unique prediction)\n'
        '   Survives statistical test\n\n'
        'Track B: integer ratio from formula scan\n'
        '   Input: 15 integers, ~2,250 formulas\n'
        '   Output: BEST MATCH (selected from many)\n'
        '   p = 0.81 — not significant',
        fontsize=10, color=WHITE, fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=DIM),
        linespacing=1.4)

ax.set_xlabel(r'$\log_{10}(E$/GeV)', fontsize=12, color=SILVER)
ax.set_ylabel(r'$\sin^2\theta_W$', fontsize=12, color=SILVER)
ax.set_xlim(1.5, 16.5)
ax.set_ylim(0.19, 0.40)
ax.legend(fontsize=10, loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

save(fig, 'phys31_07_sin2tw_two_paths.png')

# ================================================================
# FIG 8: PER-TARGET HIT RATES ACROSS RANDOM POOLS
# Type: Comparison
# Shows: Which targets are easy, which are hard — for everyone
# ================================================================
print("Fig 8: Per-Target Hit Rates")

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax)
fig.suptitle("PER-TARGET HIT RATES — Some Targets Are Easy for Everyone",
             fontsize=17, fontweight='bold', color=GOLD, y=0.96)

# Estimate per-target hit rates from the expected calculation
# Based on formula density and tolerances
target_names = ['DM/baryon', r'$\Omega_b$', r'$\Omega_{DM}$',
                r'$H_0$ ratio', r'$\sin^2\theta_W$',
                r'$n_s$', r'$\log\Lambda$', r'$\alpha_s$']

# Estimated hit rates (from the back-of-envelope in Table 31.3)
est_hit_rates = [95, 99, 99, 95, 60, 85, 50, 85]

# Beta pool hit/miss
beta_hit = [True, True, True, True, True, False, False, True]

y_pos = np.arange(len(target_names))
colors_bar = []
for i in range(len(target_names)):
    if beta_hit[i]:
        colors_bar.append(GREEN)
    else:
        colors_bar.append(RED)

bars = ax.barh(y_pos, est_hit_rates, 0.6, color=colors_bar, alpha=0.5,
               edgecolor=colors_bar, linewidth=2)

for i in range(len(target_names)):
    ax.text(est_hit_rates[i] + 2, y_pos[i],
            '~%d%%' % est_hit_rates[i], fontsize=11,
            color=WHITE, va='center', fontweight='bold')

    status = r'$\checkmark$ beta' if beta_hit[i] else r'$\times$ beta'
    ax.text(3, y_pos[i], status, fontsize=10,
            color=GREEN if beta_hit[i] else RED,
            va='center', fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(target_names, fontsize=11, color=SILVER)
ax.set_xlabel('Estimated hit rate for random pools (%)', fontsize=12,
              color=SILVER)
ax.set_xlim(0, 110)
ax.set_ylim(-0.8, 8.2)

# Difficulty regions
ax.axvline(x=80, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(82, 7.5, 'EASY\n(>80%)', fontsize=10, color=DIM, va='top')
ax.text(55, 7.5, 'MEDIUM', fontsize=10, color=DIM, va='top')
ax.axvline(x=60, color=DIM, linewidth=1, linestyle=':', alpha=0.5)
ax.text(35, 7.5, 'HARD\n(<60%)', fontsize=10, color=DIM, va='top')

ax.text(50, -0.6,
        'The beta pool misses the two HARDEST targets — the same ones most random pools miss.',
        fontsize=10, color=SILVER, ha='center', style='italic')

save(fig, 'phys31_08_per_target_rates.png')

# ================================================================
print()
print("=" * 70)
print("PHYS-31 DIAGRAMS — 8 FIGURES GENERATED")
print("=" * 70)

filenames = [
    'phys31_01_formula_space.png',
    'phys31_02_dynamics_vs_numerology.png',
    'phys31_03_score_distribution.png',
    'phys31_04_gate_threshold.png',
    'phys31_05_six_hits.png',
    'phys31_06_candidate_density.png',
    'phys31_07_sin2tw_two_paths.png',
    'phys31_08_per_target_rates.png',
]

for i, name in enumerate(filenames, 1):
    print("  Fig %d: %s" % (i, name))
    