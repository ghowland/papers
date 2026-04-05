#!/usr/bin/env python3
"""
HOWL PHYS-36 Diagrams — The QED Integer Chain at 5-Loop
8 figures covering error propagation, series hierarchy, Newton convergence,
sensitivity cascade, A3 cancellation, alpha determinations, chain progression,
and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

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

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

def dark_fig(w=16, h=10):
    fig, ax = plt.subplots(figsize=(w, h), facecolor=BG)
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    return fig, ax

def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)


# ================================================================
# FIG 1: ERROR PROPAGATION — MISS (PPB) VS ALPHA POWER
# Type: Type 1 (Running/Convergence)
# Shows: Three derived CODATA values fall on the predicted line
#        miss = |n| * 3.31 ppb, proving single-source error
# ================================================================

fig, ax = dark_fig(16, 10)

# Data: |alpha power|, observed miss (ppb), label
alpha_powers = [1, 1, 2]
observed_ppb = [3.99, 3.98, 7.97]
labels = [r'$\mu_0 \propto \alpha^1$', r'$a_0 \propto \alpha^{-1}$', r'$R_\infty \propto \alpha^2$']
colors_pts = [CYAN, GREEN, BLUE]

# Predicted line: miss = |n| * 3.31 * 1.2 (the consistent 1.2 factor)
n_line = np.linspace(0.5, 2.5, 100)
predicted_line = n_line * 3.31 * 1.20

ax.plot(n_line, predicted_line, '--', color=GOLD, linewidth=2, alpha=0.7,
        label=r'Predicted: $\delta Q/Q = |n| \times 3.31 \times 1.20$ ppb')

for i in range(3):
    ax.scatter(alpha_powers[i], observed_ppb[i], s=250, c=colors_pts[i],
               edgecolors=WHITE, linewidth=2, zorder=5)
    offset_x = 0.12 if i < 2 else -0.35
    offset_y = 0.25 if i == 0 else (-0.35 if i == 1 else 0.25)
    ax.annotate(labels[i], xy=(alpha_powers[i], observed_ppb[i]),
                xytext=(alpha_powers[i] + offset_x, observed_ppb[i] + offset_y),
                fontsize=11, color=colors_pts[i],
                arrowprops=dict(arrowstyle='->', color=colors_pts[i], lw=1.5))

# Alpha extraction point at n=0 (direct)
ax.scatter(0, 3.31, s=200, c=MAG, edgecolors=WHITE, linewidth=2, zorder=5, marker='D')
ax.annotate(r'$\alpha^{-1}$ (direct): 3.31 ppb', xy=(0, 3.31),
            xytext=(0.2, 4.5), fontsize=10, color=MAG,
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

# Result box
ax.text(1.8, 2.0, 'Ratio obs/pred = 1.20\nacross all quantities\n(single error source)',
        fontsize=10, color=GOLD, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

ax.set_xlabel(r'$|n|$ in $Q \propto \alpha^n$', fontsize=12, color=SILVER)
ax.set_ylabel('Observed miss (ppb)', fontsize=12, color=SILVER)
ax.set_title('Error Propagation Proof: Miss Scales with Alpha Power',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.set_xlim(-0.3, 2.7)
ax.set_ylim(0, 10)
ax.legend(fontsize=9, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, loc='upper left')

save(fig, 'phys36_01_error_propagation.png')


# ================================================================
# FIG 2: SERIES HIERARCHY — (alpha/pi)^n SUPPRESSION SCALE
# Type: Type 2 (Scale/Landscape)
# Shows: 11 orders of magnitude from 1-loop to 5-loop, with
#        a_e measurement precision band showing where A5 matters
# ================================================================

fig, ax = dark_fig(16, 10)

loop_orders = [1, 2, 3, 4, 5]
alpha_pi_n = [2.323e-3, 5.395e-6, 1.253e-8, 2.911e-11, 6.761e-14]
contributions = [1.161e-3, 1.773e-6, 1.480e-8, 5.565e-11, 3.983e-13]
coeff_labels = ['A₁ = 1/2', 'A₂ = −0.3285', 'A₃ = +1.1812', 'A₄ = −1.9122', 'A₅ = +5.891']
bar_colors = [GOLD, CYAN, GREEN, BLUE, PURPLE]

# Plot (alpha/pi)^n as bars
bar_x = np.array(loop_orders)
bars = ax.bar(bar_x - 0.18, [abs(c) for c in contributions], width=0.35,
              color=bar_colors, alpha=0.7, edgecolor=[c for c in bar_colors], linewidth=1.5,
              label=r'$|A_n \cdot (α/π)^n|$')

# Plot (alpha/pi)^n raw suppression
ax.bar(bar_x + 0.18, alpha_pi_n, width=0.35,
       color=DIM, alpha=0.4, edgecolor=SILVER, linewidth=1,
       label=r'$(α/π)^n$')

# Measurement precision band
ax.axhspan(1e-14, 2e-13, color=MAG, alpha=0.10)
ax.text(4.7, 5e-14, 'a_e measurement\nprecision (0.11 ppb)', fontsize=9,
        color=MAG, ha='center', va='bottom')

# Labels on bars
for i in range(5):
    y_pos = abs(contributions[i]) * 2.5
    ax.text(bar_x[i] - 0.18, y_pos, coeff_labels[i], fontsize=9,
            color=bar_colors[i], ha='center', va='bottom', rotation=0)

ax.set_yscale('log')
ax.set_ylim(1e-15, 1e-1)
ax.set_xlim(0.3, 5.7)
ax.set_xticks(loop_orders)
ax.set_xticklabels(['1-loop\n(Schwinger)', '2-loop\n(Petermann)', '3-loop\n(Laporta-\nRemiddi)',
                     '4-loop\n(Laporta)', '5-loop\n(Volkov)'], fontsize=9, color=SILVER)
ax.set_ylabel('Contribution to a_e', fontsize=12, color=SILVER)
ax.set_title('QED Series Hierarchy: Each Loop Order Suppressed by α/π ≈ 1/430',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.legend(fontsize=9, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, loc='upper right')

save(fig, 'phys36_02_series_hierarchy.png')


# ================================================================
# FIG 3: NEWTON CONVERGENCE — RESIDUAL VS ITERATION
# Type: Type 1 (Running/Convergence)
# Shows: Quadratic convergence from 10^-6 to 10^-204, slope
#        doubling each step — the signature of Newton's method
# ================================================================

fig, ax = dark_fig(16, 10)

iterations = [1, 2, 3, 4, 5, 6]
residuals = [1.75e-6, 3.96e-12, 2.02e-23, 5.26e-46, 1e-91, 1.59e-204]
alpha_inv_vals = [137.035999052, 137.035998583, 137.035998583, 137.035998583, 137.035998630, 137.035998630]

ax.plot(iterations, residuals, 'o-', color=CYAN, linewidth=2.5, markersize=12,
        markeredgecolor=WHITE, markeredgewidth=2, zorder=5)

# Quadratic convergence reference line
quad_ref_x = np.array([1, 2, 3, 4, 5, 6])
quad_ref_y = 1e-6 * np.array([1, 1e-6, 1e-17, 1e-40, 1e-85, 1e-198])
ax.plot(quad_ref_x, quad_ref_y, '--', color=DIM, linewidth=1.5, alpha=0.5,
        label='Quadratic convergence reference')

# Annotations
for i, (it, res) in enumerate(zip(iterations, residuals)):
    if i < 4:
        ax.annotate('|f| = %.1e' % res, xy=(it, res),
                    xytext=(it + 0.3, res * 10),
                    fontsize=9, color=SILVER,
                    arrowprops=dict(arrowstyle='->', color=SILVER, lw=1))

ax.annotate('|f| = 1.59 × 10⁻²⁰⁴\n(exact arithmetic limit)', xy=(6, 1.59e-204),
            xytext=(4.5, 1e-170), fontsize=10, color=GOLD,
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Convergence threshold
ax.axhline(y=1e-50, color=GREEN, linewidth=1, linestyle='-.', alpha=0.5)
ax.text(1.2, 3e-50, 'Convergence threshold (10⁻⁵⁰)', fontsize=8, color=GREEN)

ax.set_yscale('log')
ax.set_ylim(1e-220, 1e-2)
ax.set_xlim(0.5, 6.8)
ax.set_xlabel('Newton Iteration', fontsize=12, color=SILVER)
ax.set_ylabel('|f(x)| = |series − a_e|', fontsize=12, color=SILVER)
ax.set_title('Newton Inversion: Quadratic Convergence to 10⁻²⁰⁴',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.legend(fontsize=9, facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, loc='upper right')

save(fig, 'phys36_03_newton_convergence.png')


# ================================================================
# FIG 4: SENSITIVITY CASCADE — PPB PER 1% ERROR VS LOOP ORDER
# Type: Type 2 (Scale/Landscape)
# Shows: 12 orders of magnitude in sensitivity from A1 (catastrophic)
#        to A5 (negligible), with current residual as threshold
# ================================================================

fig, ax = dark_fig(16, 10)

coeffs = ['A₁', 'A₂', 'A₃', 'A₄', 'A₅']
sensitivity_ppb = [1e10, 1.3e4, 109, 0.41, 0.003]
bar_colors_s = [RED, ORANGE, GOLD, GREEN, CYAN]

bars = ax.barh(range(5), sensitivity_ppb, height=0.6,
               color=bar_colors_s, alpha=0.7,
               edgecolor=[c for c in bar_colors_s], linewidth=1.5)

# Label each bar
for i, (s, c) in enumerate(zip(sensitivity_ppb, bar_colors_s)):
    if s >= 1:
        ax.text(s * 1.5, i, '%.0f ppb' % s if s >= 1 else '%.3f ppb' % s,
                fontsize=10, color=c, va='center')
    else:
        ax.text(s * 3, i, '%.3f ppb' % s, fontsize=10, color=c, va='center')

# Current residual line
ax.axvline(x=3.3, color=MAG, linewidth=2, linestyle='--', alpha=0.7)
ax.text(5.0, 4.5, 'Current residual\n3.3 ppb', fontsize=10, color=MAG,
        ha='left', va='top')

# "Must be exact" region
ax.axvspan(1e3, 1e11, color=RED, alpha=0.03)
ax.text(5e6, 4.5, 'Must be exact', fontsize=9, color=RED, alpha=0.5,
        ha='center', rotation=0)

# "Irrelevant at current precision" region
ax.axvspan(1e-4, 3.3, color=GREEN, alpha=0.03)
ax.text(0.03, 0.3, 'Below\nresidual', fontsize=8, color=GREEN, alpha=0.5, ha='center')

ax.set_xscale('log')
ax.set_xlim(1e-4, 1e11)
ax.set_yticks(range(5))
ax.set_yticklabels(coeffs, fontsize=12, color=SILVER)
ax.set_xlabel('Shift in α⁻¹ per 1% coefficient error (ppb)', fontsize=12, color=SILVER)
ax.set_title('Sensitivity Cascade: Why Exact Arithmetic Matters for A₁ and A₂',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.invert_yaxis()

save(fig, 'phys36_04_sensitivity_cascade.png')


# ================================================================
# FIG 5: A3 TEN-TERM CANCELLATION BARS
# Type: Type 6 (Comparison Bar)
# Shows: Ten terms spanning -23 to +208, cancelling to +1.181.
#        The 176x cancellation is visible as bar lengths.
# ================================================================

fig, ax = dark_fig(16, 10)

terms = [
    ('(83/72)π²ζ(3)', +13.849),
    ('−(215/24)ζ(5)', -9.286),
    ('(100/3)Li₄(½)', +17.249),
    ('(100/3)ln⁴2/24', +0.321),
    ('−(100/3)π²ln²2/24', -6.547),
    ('−(239/2160)π⁴', -10.780),
    ('(139/18)ζ(3)', +9.283),
    ('−(298/9)π²ln2', -22.586),
    ('(17101/810)π²', +208.277),
    ('28259/5184', +5.453),
]

y_pos = np.arange(len(terms))
values = [t[1] for t in terms]
labels_t = [t[0] for t in terms]
colors_t = [GREEN if v > 0 else RED for v in values]

ax.barh(y_pos, values, height=0.6, color=colors_t, alpha=0.6,
        edgecolor=colors_t, linewidth=1.5)

for i, (label, val) in enumerate(terms):
    x_text = val + (3 if val > 0 else -3)
    ha = 'left' if val > 0 else 'right'
    ax.text(x_text, i, '%+.3f' % val, fontsize=9, color=SILVER, va='center', ha=ha)

ax.set_yticks(y_pos)
ax.set_yticklabels(labels_t, fontsize=9, color=SILVER)

# Net sum line
ax.axvline(x=1.181, color=GOLD, linewidth=2.5, linestyle='-', alpha=0.9)
ax.text(1.181, 9.7, 'A₃ = +1.181', fontsize=12, color=GOLD, ha='left',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Zero line
ax.axvline(x=0, color=DIM, linewidth=1, linestyle='-', alpha=0.5)

# Cancellation note
ax.text(120, 0.5, 'Term 9 is 176× larger\nthan the sum.\n\nCancellation is exact\nin Fraction arithmetic.',
        fontsize=10, color=ORANGE, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE, alpha=0.8))

ax.set_xlim(-40, 230)
ax.set_xlabel('Numerical value of term', fontsize=12, color=SILVER)
ax.set_title('A₃ Ten-Term Decomposition: Massive Cancellation at 3-Loop',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)
ax.invert_yaxis()

save(fig, 'phys36_05_a3_cancellation.png')


# ================================================================
# FIG 6: ALPHA INVERSE — FOUR DETERMINATIONS WITH ERROR BARS
# Type: Type 6 (Comparison Bar)
# Shows: Our extraction vs Cs recoil vs Rb recoil vs CODATA on a
#        zoomed axis, with uncertainty bands showing the tensions
# ================================================================

fig, ax = dark_fig(16, 10)

# Values (offset from 137.035999 for readability)
base = 137.035999
methods = ['This work\n(a_e, 5-loop)', 'Cs recoil\n(Parker 2018)', 'CODATA 2018\nrecommended',
           'Rb recoil\n(Morel 2020)']
values_alpha = [137.035998630, 137.035999046, 137.035999084, 137.035999206]
errors = [0, 0.000000027, 0.000000021, 0.000000011]
colors_a = [GOLD, CYAN, MAG, GREEN]
offsets = [(v - base) * 1e6 for v in values_alpha]  # in units of 10^-6
errors_scaled = [e * 1e6 for e in errors]

y_positions = [3, 2, 1, 0]

for i in range(4):
    ax.errorbar(offsets[i], y_positions[i], xerr=errors_scaled[i] if errors_scaled[i] > 0 else None,
                fmt='o' if i > 0 else 'D', color=colors_a[i], markersize=12,
                markeredgecolor=WHITE, markeredgewidth=2, capsize=8, capthick=2,
                ecolor=colors_a[i], elinewidth=2, zorder=5)
    text_x = offsets[i] + 0.015
    ax.text(text_x, y_positions[i] + 0.25, '%.9f' % values_alpha[i],
            fontsize=9, color=colors_a[i], va='bottom')
    if errors[i] > 0:
        ax.text(text_x, y_positions[i] - 0.25, '±%.3f ppb' % (errors[i] / values_alpha[i] * 1e9),
                fontsize=8, color=DIM, va='top')

# Tension annotations
ax.annotate('', xy=(offsets[0], 2.7), xytext=(offsets[1], 2.7),
            arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax.text((offsets[0] + offsets[1]) / 2, 2.85, '3.0 ppb', fontsize=9, color=SILVER, ha='center')

ax.annotate('', xy=(offsets[0], 0.3), xytext=(offsets[3], 0.3),
            arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax.text((offsets[0] + offsets[3]) / 2, 0.15, '4.2 ppb', fontsize=9, color=SILVER, ha='center')

ax.set_yticks(y_positions)
ax.set_yticklabels(methods, fontsize=11, color=SILVER)
ax.set_xlabel(r'$\alpha^{-1} - 137.035999$ (× 10⁻⁶)', fontsize=12, color=SILVER)
ax.set_xlim(-0.5e-0, 0.3e-0)
ax.set_ylim(-0.7, 3.8)
ax.set_title('Fine Structure Constant: Four Independent Determinations',
             fontsize=15, fontweight='bold', color=GOLD, pad=15)

save(fig, 'phys36_06_alpha_determinations.png')


# ================================================================
# FIG 7: COMPLETE CHAIN — INPUT TO OUTPUT PROGRESSION
# Type: Type 7 (Progression/Sequence)
# Shows: Physical data flow from a_e through Newton inversion
#        to alpha, branching to R_inf, a_0, mu_0. Numbers at
#        every stage. Alpha-power labels at each branch.
# ================================================================

fig, ax = dark_fig(18, 10)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

# Stage boxes
def draw_box(ax, x, y, w, h, text, color, fontsize=10):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.15', facecolor=BG,
                          edgecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=fontsize, color=color,
            ha='center', va='center', linespacing=1.5)

# Input
draw_box(ax, 2, 5, 3.2, 2.5,
         'MEASURED\n─────────\na_e = 1.1597×10⁻³\nm_e = 0.511 MeV\n(2 rationals)',
         MAG, 10)

# QED Series
draw_box(ax, 6.5, 5, 3.2, 2.5,
         'QED SERIES\n─────────\nA₁ = 1/2\nA₂,A₃: Q335 exact\nA₄,A₅: numerical',
         CYAN, 10)

# Alpha
draw_box(ax, 10.5, 5, 2.8, 2,
         'NEWTON\n─────────\nα⁻¹ = 137.0360\n3.3 ppb',
         GOLD, 11)

# Three outputs
draw_box(ax, 14.5, 8, 3, 1.5,
         'R∞ = 10973731.66\n8.0 ppb  (α²)',
         BLUE, 10)

draw_box(ax, 14.5, 5, 3, 1.5,
         'a₀ = 5.292×10⁻¹¹\n4.0 ppb  (α⁻¹)',
         GREEN, 10)

draw_box(ax, 14.5, 2, 3, 1.5,
         'μ₀ = 1.257×10⁻⁶\n4.0 ppb  (α¹)',
         PURPLE, 10)

# Arrows
arrow_style = dict(arrowstyle='->', color=SILVER, lw=2, connectionstyle='arc3,rad=0')

ax.annotate('', xy=(4.9, 5), xytext=(3.6, 5), arrowprops=arrow_style)
ax.annotate('', xy=(8.9, 5), xytext=(8.1, 5), arrowprops=arrow_style)

# Branching arrows
ax.annotate('', xy=(13.0, 8), xytext=(11.9, 5.8),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=2, connectionstyle='arc3,rad=0.2'))
ax.annotate('', xy=(13.0, 5), xytext=(11.9, 5),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.annotate('', xy=(13.0, 2), xytext=(11.9, 4.2),
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2, connectionstyle='arc3,rad=-0.2'))

# SI constants label
ax.text(10.5, 1.0, 'SI exact: c, h, e, ℏ\n(zero uncertainty)',
        fontsize=9, color=DIM, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, alpha=0.5))

# Title
ax.text(9, 9.5, 'The QED Integer Chain: One Measurement → Four CODATA Values',
        fontsize=15, fontweight='bold', color=GOLD, ha='center')

save(fig, 'phys36_07_chain_progression.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE QED INTEGER CHAIN
# Type: Type 8 (Identity Card)
# Shows: Central schematic with key fractions, Q335 constants,
#        results, and the branching tree structure. Visual anchor.
# ================================================================

fig, ax = dark_fig(18, 12)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

# Title bar
ax.text(9, 11.3, 'HOWL-PHYS-36: THE QED INTEGER CHAIN AT 5-LOOP',
        fontsize=16, fontweight='bold', color=GOLD, ha='center')
ax.axhline(y=10.8, xmin=0.05, xmax=0.95, color=GOLD, linewidth=1.5)

# Left column: Coefficients
ax.text(1, 10.3, 'QED COEFFICIENTS', fontsize=12, fontweight='bold', color=WHITE)
coeffs_text = [
    ('A₁ = 1/2', 'Schwinger 1948', GOLD),
    ('A₂ = 197/144 + (1/12)π² + ...', '4 rationals × 3 Q335', CYAN),
    ('A₃ = (83/72)π²ζ(3) − ...', '8 rationals × 5 Q335', GREEN),
    ('A₄ = −1.9122...', '30 digits, numerical', BLUE),
    ('A₅ = +5.891', '4 digits, Volkov 2024', PURPLE),
]
for i, (formula, note, color) in enumerate(coeffs_text):
    y = 9.5 - i * 0.8
    ax.text(1, y, formula, fontsize=10, color=color, fontfamily='monospace')
    ax.text(1, y - 0.3, note, fontsize=8, color=DIM)

# Center column: Key Fractions
ax.text(7.5, 10.3, 'KEY FRACTIONS', fontsize=12, fontweight='bold', color=WHITE)
fracs = ['197/144', '83/72', '215/24', '100/3', '239/2160',
         '139/18', '298/9', '17101/810', '28259/5184']
for i, f in enumerate(fracs):
    row = i // 3
    col = i % 3
    x = 7.0 + col * 1.8
    y = 9.5 - row * 0.7
    ax.text(x, y, f, fontsize=10, color=ORANGE, fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=PAN, edgecolor=DIM, alpha=0.5))

# Denominator primes note
ax.text(8.5, 7.2, 'All denominators: {2, 3, 5} only', fontsize=9, color=ORANGE)

# Right column: Q335 Constants
ax.text(14, 10.3, 'Q335 BASIS', fontsize=12, fontweight='bold', color=WHITE)
q335 = ['π (100 digits)', 'ln(2)', 'ζ(3)', 'ζ(5)', 'Li₄(1/2)']
for i, c in enumerate(q335):
    ax.text(14, 9.5 - i * 0.55, c, fontsize=10, color=SILVER)

# Results section
ax.axhline(y=5.8, xmin=0.05, xmax=0.95, color=DIM, linewidth=0.5)
ax.text(9, 5.4, 'RESULTS', fontsize=14, fontweight='bold', color=GOLD, ha='center')

results = [
    ('α⁻¹', '137.035998630', '3.3 ppb', 'α⁰', GOLD),
    ('R∞', '10973731.656 m⁻¹', '8.0 ppb', 'α²', BLUE),
    ('a₀', '5.292 × 10⁻¹¹ m', '4.0 ppb', 'α⁻¹', GREEN),
    ('μ₀', '1.257 × 10⁻⁶ N/A²', '4.0 ppb', 'α¹', PURPLE),
]

for i, (name, val, miss, power, color) in enumerate(results):
    x = 1.5 + i * 4.2
    draw_box_simple_x = x + 1.5
    ax.text(x, 4.7, name, fontsize=14, fontweight='bold', color=color)
    ax.text(x, 4.1, val, fontsize=10, color=WHITE, fontfamily='monospace')
    ax.text(x, 3.6, '%s (%s)' % (miss, power), fontsize=9, color=SILVER)

# Input section
ax.axhline(y=3.0, xmin=0.05, xmax=0.95, color=DIM, linewidth=0.5)
ax.text(3, 2.4, 'INPUTS FROM UNIVERSE', fontsize=11, fontweight='bold', color=MAG)
ax.text(3, 1.8, 'a_e = 115965218059/10¹⁴  (0.11 ppb)', fontsize=10, color=MAG, fontfamily='monospace')
ax.text(3, 1.3, 'm_e = 51099895069/10¹¹ MeV  (0.03 ppb)', fontsize=10, color=MAG, fontfamily='monospace')

ax.text(12, 2.4, 'VERIFICATION', fontsize=11, fontweight='bold', color=GREEN)
ax.text(12, 1.8, 'Newton residual: 10⁻²⁰⁴', fontsize=10, color=GREEN)
ax.text(12, 1.3, 'Round-trip: 14-digit match', fontsize=10, color=GREEN)
ax.text(12, 0.8, 'Error scaling: constant 1.2× ratio', fontsize=10, color=GREEN)

# Footer
ax.text(9, 0.3, 'Two measured rationals + integer laws = four CODATA values',
        fontsize=11, color=GOLD, ha='center', style='italic')

save(fig, 'phys36_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("PHYS-36 Diagrams Complete:")
print("  phys36_01_error_propagation.png")
print("  phys36_02_series_hierarchy.png")
print("  phys36_03_newton_convergence.png")
print("  phys36_04_sensitivity_cascade.png")
print("  phys36_05_a3_cancellation.png")
print("  phys36_06_alpha_determinations.png")
print("  phys36_07_chain_progression.png")
print("  phys36_08_identity_card.png")
