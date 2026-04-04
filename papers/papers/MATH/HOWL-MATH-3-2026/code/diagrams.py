#!/usr/bin/env python3
"""
HOWL MATH-3 Diagrams — The Transcendental Hierarchy
8 figures covering elliptic integrals, Borwein acceleration, loop hierarchy, 4-loop wall.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: TRANSCENDENTAL HIERARCHY — LOOP ORDER VS MAX WEIGHT
# Type: Running/convergence
# Shows: The 2L-1 pattern with 5-loop prediction. The curve shape
# IS the conjecture — linear growth of transcendental complexity.
# ================================================================

fig, ax = dark_fig("Transcendental Hierarchy: Max Weight = 2L \u2212 1",
                   xlabel="Loop order L",
                   ylabel="Maximum transcendental weight")

# Known data points
loops = [1, 2, 3, 4]
weights = [0, 3, 5, 7]
labels_data = [
    'A\u2081 = 1/2\n(rational only)',
    'A\u2082: \u03b6(3), \u03c0\u00b2ln(2)',
    'A\u2083: \u03b6(5), \u03c0\u00b2\u03b6(3)',
    'A\u2084: \u03b6(7), elliptic\n(expected)',
]
colors_data = [GREEN, CYAN, BLUE, ORANGE]

for i in range(4):
    data_point(ax, loops[i], weights[i], '', colors_data[i], size=300)
    dx = 0.35
    dy = 0.6 if i != 0 else -1.0
    ax.text(loops[i] + dx, weights[i] + dy, labels_data[i],
            fontsize=9, color=colors_data[i], fontweight='bold',
            va='center')

# The 2L-1 line
L_ext = np.linspace(0.5, 6.5, 100)
w_ext = 2 * L_ext - 1
curve(ax, L_ext, w_ext, '2L \u2212 1 conjecture', GOLD, 2, style='--', alpha=0.6)

# 5-loop prediction
data_point(ax, 5, 9, '', GOLD, size=250)
ax.scatter([5], [9], s=250, facecolors='none', edgecolors=GOLD,
           linewidth=2.5, zorder=11)
ax.text(5.35, 9.6, '5-loop prediction:\nmax weight = 9\nNo new class expected',
        fontsize=9, color=GOLD, fontweight='bold')

# 6-loop prediction with question
ax.scatter([6], [11], s=200, facecolors='none', edgecolors=RED,
           linewidth=2, linestyle='dashed', zorder=11)
ax.text(5.5, 11.6, '6-loop: weight 11?\nHyperelliptic integrals?\nK3 surfaces?',
        fontsize=8, color=RED, style='italic')

# Shaded regions for transcendental classes
shaded_region_h(ax, -0.5, 0.5, GREEN, 0.06, '')
ax.text(0.15, 0.0, 'Rational', fontsize=8, color=GREEN, alpha=0.7)

shaded_region_h(ax, 0.5, 5.5, CYAN, 0.04, '')
ax.text(0.15, 3.0, '\u03b6 / ln / Li family', fontsize=8, color=CYAN, alpha=0.7)

shaded_region_h(ax, 5.5, 8.5, ORANGE, 0.04, '')
ax.text(0.15, 7.0, '+ elliptic integrals', fontsize=8, color=ORANGE, alpha=0.7)

ax.set_xlim(0, 7)
ax.set_ylim(-1.5, 13)
ax.set_xticks([1, 2, 3, 4, 5, 6])

legend(ax, loc='upper left')

save_fig(fig, 'math3_01_transcendental_hierarchy.png')


# ================================================================
# FIG 2: BORWEIN VS DIRECT ETA FOR ZETA(5)
# Type: Dual convergence
# Shows: Direct eta (flat, useless) vs Borwein (steep, solved).
# The visual contrast IS the bottleneck fix.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Direct Eta: \u03b6(5) the Hard Way",
    "Borwein Acceleration: \u03b6(5) Solved",
    size=(18, 9), wspace=0.35)

# Left: direct eta convergence
n_direct = np.arange(100, 10100, 100)
# Error ~ 1/N^5, digits ~ 5*log10(N)
digits_direct = 5 * np.log10(n_direct)

curve(ax1, n_direct, digits_direct, 'Direct \u03b7(5)', RED, 2.5)
ax1.plot([0, 10500], [100, 100], color=ORANGE, linewidth=1.5,
         linestyle='--', alpha=0.6)
ax1.text(6000, 105, '100-digit target', fontsize=9, color=ORANGE)
ax1.set_xlabel('Terms', color=SILVER, fontsize=11)
ax1.set_ylabel('Correct digits', color=SILVER, fontsize=11)
ax1.set_xlim(0, 10500)
ax1.set_ylim(0, 130)

result_box(ax1, 5000, 50,
           '10,000 terms \u2192 20 digits\n10\u00b2\u2070 terms for 100 digits\nINFEASIBLE',
           RED, 10)

# Right: Borwein convergence
n_borwein = np.arange(1, 220)
# Error ~ 3^(-n), digits ~ n * log10(3) ~ 0.477*n
digits_borwein = 0.477 * n_borwein

curve(ax2, n_borwein, digits_borwein, 'Borwein acceleration', GREEN, 2.5)
ax2.plot([0, 220], [100, 100], color=ORANGE, linewidth=1.5,
         linestyle='--', alpha=0.6)
ax2.text(130, 105, '100-digit target', fontsize=9, color=ORANGE)
ax2.set_xlabel('Parameter n (= number of terms)', color=SILVER, fontsize=11)
ax2.set_ylabel('Correct digits', color=SILVER, fontsize=11)
ax2.set_xlim(0, 225)
ax2.set_ylim(0, 130)

# Mark the solution point
data_point(ax2, 210, 100, '', GOLD, size=250)
ax2.annotate('n = 210\n100+ digits\n~22,000 Fraction ops', xy=(210, 100),
             xytext=(140, 70),
             fontsize=10, color=GOLD, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

result_box(ax2, 100, 25,
           'Same method works for\n\u03b6(7), \u03b6(9), \u03b6(11), ...\nUniversal fix',
           GREEN, 10)

save_fig(fig, 'math3_02_borwein_vs_direct.png')


# ================================================================
# FIG 3: PSLQ CANDIDATE POOL BY TRANSCENDENTAL WEIGHT
# Type: Scale/hierarchy pyramid
# Shows: The weight structure of the candidate pool for PSLQ
# identification of Laporta's master integrals. The pyramid
# shape shows how constants multiply at higher weights.
# ================================================================

fig, ax = dark_canvas("PSLQ Candidate Pool: Organized by Transcendental Weight",
                      size=(16, 14))
ax.set_xlim(-5, 5)
ax.set_ylim(-1.5, 9)

# Weight levels — pyramid structure
levels = [
    (0, ['1'], 'Weight 0: Rational', SILVER),
    (1, ['\u03c0', 'ln(2)', 'K(k)'], 'Weight 1', CYAN),
    (2, ['\u03c0\u00b2', 'ln\u00b2(2)', '\u03c0\u00b7ln(2)', '\u03b6(2)'], 'Weight 2', BLUE),
    (3, ['\u03b6(3)', '\u03c0\u00b3', '\u03c0\u00b2ln(2)', 'Li\u2083(\u00bd)'], 'Weight 3', GREEN),
    (4, ['\u03c0\u2074', '\u03b6(4)', '\u03b6(3)ln(2)', 'Li\u2084(\u00bd)', 'ln\u2074(2)'], 'Weight 4', ORANGE),
    (5, ['\u03b6(5)', '\u03c0\u00b2\u03b6(3)', '\u03c0\u2074ln(2)', '...'], 'Weight 5', MAG),
    (6, ['\u03b6(3)\u00b2', '\u03c0\u00b2\u03b6(4)', '\u03b6(5)ln(2)', '...'], 'Weight 6', PURPLE),
    (7, ['\u03b6(7)', '\u03c0\u00b2\u03b6(5)', '\u03b6(3)\u03b6(4)', '...'], 'Weight 7 (max expected)', RED),
]

for w, constants, label, color in levels:
    y = w
    n = len(constants)
    total_width = min(n * 1.4, 8)
    x_start = -total_width / 2

    # Level background bar
    rect = plt.Rectangle((x_start - 0.3, y - 0.3), total_width + 0.6, 0.6,
                          facecolor=color, alpha=0.08, edgecolor=color,
                          linewidth=1, zorder=2)
    ax.add_patch(rect)

    # Constants
    for i, c in enumerate(constants):
        cx = x_start + i * 1.4 + 0.7
        ax.text(cx, y, c, fontsize=9, color=color, ha='center',
                va='center', fontweight='bold')

    # Label on the right
    ax.text(4.5, y, label, fontsize=8, color=color, ha='left',
            va='center', style='italic')

# Elliptic additions highlighted
ax.text(-4.0, 1.2, 'K(k) entries\n(MATH-3 new)', fontsize=9, color=GOLD,
        fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))
ax.annotate('', xy=(-1.1, 1.0), xytext=(-3.2, 1.0),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Clausen additions
ax.text(-4.0, 2.5, 'Cl\u2082(\u03c0/3)\n(Clausen)', fontsize=8, color=GOLD,
        ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.7))

# Bottom summary
result_box(ax, 0, -0.9,
           '~80 candidate constants after removing algebraic dependencies\n'
           'All computable in Fraction arithmetic to 5000+ digits',
           GOLD, 10)

save_fig(fig, 'math3_03_pslq_weight_pyramid.png')


# ================================================================
# FIG 4: HYPERGEOMETRIC CONVERGENCE FOR K(k) AT THREE MODULI
# Type: Running/convergence
# Shows: Three curves at k^2 = 1/4, 1/2, 3/4. Convergence rate
# directly tracks k^2. The shape shows the feasibility tradeoff.
# ================================================================

fig, ax = dark_fig("Elliptic Integral Convergence: K(k) at Three Rational Moduli",
                   xlabel="Number of hypergeometric terms",
                   ylabel="Correct decimal digits")

n_terms = np.arange(1, 501)

# Digits ~ -n * log10(k^2)
digits_quarter = n_terms * (-np.log10(0.25))   # k^2 = 1/4: ~0.60 digits/term
digits_half = n_terms * (-np.log10(0.50))       # k^2 = 1/2: ~0.30 digits/term
digits_three_q = n_terms * (-np.log10(0.75))    # k^2 = 3/4: ~0.125 digits/term

curve(ax, n_terms, digits_quarter, 'k\u00b2 = 1/4  (~0.60 digits/term)', GREEN, 2.5)
curve(ax, n_terms, digits_half, 'k\u00b2 = 1/2  (~0.30 digits/term)', CYAN, 2.5)
curve(ax, n_terms, digits_three_q, 'k\u00b2 = 3/4  (~0.125 digits/term)', ORANGE, 2.5)

# 100-digit target
ax.plot([0, 510], [100, 100], color=GOLD, linewidth=1.5,
        linestyle='--', alpha=0.6)
ax.text(420, 105, '100-digit target', fontsize=9, color=GOLD)

# Mark where each crosses 100 digits
cross_quarter = int(100 / 0.602)   # ~166
cross_half = int(100 / 0.301)      # ~332
cross_three_q = int(100 / 0.125)   # ~800 (off chart)

data_point(ax, cross_quarter, 100, '', GREEN, size=180)
ax.text(cross_quarter + 15, 108, '%d terms' % cross_quarter,
        fontsize=9, color=GREEN, fontweight='bold')

data_point(ax, cross_half, 100, '', CYAN, size=180)
ax.text(cross_half + 15, 108, '%d terms' % cross_half,
        fontsize=9, color=CYAN, fontweight='bold')

ax.text(460, 68, 'k\u00b2=3/4 needs\n~800 terms\n(off chart)', fontsize=9,
        color=ORANGE, fontweight='bold', ha='center')

# Formula
note(ax, 10, 270, 'K(k) = (\u03c0/2) \u00b7 \u2082F\u2081(1/2, 1/2; 1; k\u00b2)\n'
     'Convergence ratio = k\u00b2 per term\n'
     'Every term is rational at rational k\u00b2', SILVER, 10)

ax.set_xlim(0, 510)
ax.set_ylim(0, 310)

legend(ax, loc='upper left')

save_fig(fig, 'math3_04_elliptic_convergence.png')


# ================================================================
# FIG 5: FEYNMAN TOPOLOGY -> TRANSCENDENTAL CLASS
# Type: Geometric/topological
# Shows: How graph structure determines which transcendentals appear.
# Factorizable -> zeta/ln/Li. Irreducible sunrise -> elliptic.
# ================================================================

fig, ax = dark_canvas("Feynman Topology Determines Transcendental Class",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Left column: factorizable diagrams
ax.text(2.5, 9.2, 'FACTORIZABLE', fontsize=15, color=GREEN,
        ha='center', fontweight='bold')
ax.text(2.5, 8.6, 'Can be cut into subdiagrams', fontsize=9,
        color=SILVER, ha='center')

# Simple factorizable: two loops connected by one line
# Loop 1
c1 = plt.Circle((1.8, 7.0), 0.5, fill=False, edgecolor=GREEN,
                 linewidth=2.5, zorder=4)
ax.add_patch(c1)
# Loop 2
c2 = plt.Circle((3.2, 7.0), 0.5, fill=False, edgecolor=GREEN,
                 linewidth=2.5, zorder=4)
ax.add_patch(c2)
# Connecting propagator
ax.plot([2.3, 2.7], [7.0, 7.0], color=GREEN, linewidth=2.5, zorder=5)
# Cut line
ax.plot([2.5, 2.5], [6.3, 7.7], color=RED, linewidth=2, linestyle='--',
        alpha=0.7, zorder=6)
ax.text(2.5, 6.0, 'CUT HERE', fontsize=8, color=RED, ha='center',
        fontweight='bold')

# Arrow to result
ax.text(2.5, 5.0, 'Produces:', fontsize=10, color=GREEN,
        ha='center', fontweight='bold')
ax.text(2.5, 4.2, '\u03b6(n), ln(2), Li\u2084(\u00bd)\n'
        '\u03c0 powers\nMultiple zeta values',
        fontsize=10, color=GREEN, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN))

ax.text(2.5, 2.8, 'MATH-2 basis sufficient', fontsize=10,
        color=GREEN, ha='center', style='italic')

# Right column: irreducible sunrise
ax.text(7.5, 9.2, 'IRREDUCIBLE (Sunrise)', fontsize=15, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(7.5, 8.6, 'Cannot be cut \u2014 all propagators entangled', fontsize=9,
        color=SILVER, ha='center')

# 4-propagator sunrise: circle with 4 internal lines
sunrise_c = plt.Circle((7.5, 7.0), 0.7, fill=False, edgecolor=ORANGE,
                         linewidth=2.5, zorder=4)
ax.add_patch(sunrise_c)

# Internal propagators (4 lines crossing through)
for angle in [0.4, 1.1, 1.8, 2.5]:
    x0 = 7.5 + 0.7 * np.cos(angle)
    y0 = 7.0 + 0.7 * np.sin(angle)
    x1 = 7.5 + 0.7 * np.cos(angle + np.pi)
    y1 = 7.0 + 0.7 * np.sin(angle + np.pi)
    ax.plot([x0, x1], [y0, y1], color=ORANGE, linewidth=2, alpha=0.7, zorder=5)

# External legs
ax.plot([6.5, 6.8], [7.0, 7.0], color=SILVER, linewidth=2)
ax.plot([8.2, 8.5], [7.0, 7.0], color=SILVER, linewidth=2)

# No cut possible
ax.text(7.5, 6.0, 'NO CUT', fontsize=8, color=RED, ha='center',
        fontweight='bold')

# Arrow to result
ax.text(7.5, 5.0, 'Produces:', fontsize=10, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(7.5, 4.2, 'Complete elliptic\nintegrals K(k), E(k)\nElliptic curve periods',
        fontsize=10, color=ORANGE, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

ax.text(7.5, 2.8, 'MATH-3 extension required', fontsize=10,
        color=ORANGE, ha='center', style='italic')

# Dividing line
ax.plot([5, 5], [2.0, 9.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

# Bottom banner
ax.text(5, 1.5, 'The graph topology determines the transcendental class.\n'
        'Factorizable \u2192 \u03b6/ln/Li (MATH-2).  '
        'Irreducible sunrise \u2192 elliptic (MATH-3).',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'math3_05_topology_transcendental.png')


# ================================================================
# FIG 6: SUNRISE FAMILY ACROSS LOOP ORDERS
# Type: Geometric progression
# Shows: 2-loop sunrise -> 3-loop banana -> 4-loop (elliptic).
# Topological complexity growing with loop order.
# ================================================================

fig, ax = dark_canvas("The Sunrise Family: Increasing Topological Complexity",
                      size=(18, 10))
ax.set_xlim(-0.5, 11)
ax.set_ylim(-1.5, 4.5)

stages = [
    (1.5, '2-Loop Sunrise', 2, CYAN, '\u03b6(2), \u03b6(3)\n(reducible)'),
    (5.0, '3-Loop Banana', 3, BLUE, '\u03b6(5)\n(still \u03b6/Li family)'),
    (8.5, '4-Loop Sunrise', 4, ORANGE, 'Elliptic integrals\nK(k), E(k)\n(NEW CLASS)'),
]

for cx, title, n_props, color, result in stages:
    # Outer circle (the loop)
    outer = plt.Circle((cx, 2.2), 0.9, fill=False, edgecolor=color,
                         linewidth=2.5, zorder=4)
    ax.add_patch(outer)

    # Internal propagators
    for i in range(n_props):
        angle = i * np.pi / (n_props - 1) if n_props > 1 else 0
        # Curve through the middle
        t = np.linspace(-0.85, 0.85, 50)
        x_line = cx + t
        y_line = 2.2 + 0.35 * np.sin(angle + 0.5) * np.sin(np.pi * (t + 0.85) / 1.7)
        ax.plot(x_line, y_line, color=color, linewidth=1.8, alpha=0.6, zorder=5)

    # External legs
    ax.plot([cx - 1.3, cx - 0.9], [2.2, 2.2], color=SILVER, linewidth=2)
    ax.plot([cx + 0.9, cx + 1.3], [2.2, 2.2], color=SILVER, linewidth=2)

    # Title above
    ax.text(cx, 3.7, title, fontsize=12, color=color, ha='center',
            fontweight='bold')
    ax.text(cx, 3.3, '%d propagators' % n_props, fontsize=9, color=DIM,
            ha='center')

    # Result below
    ax.text(cx, 0.6, result, fontsize=10, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8))

# Arrows between stages
ax.annotate('', xy=(3.3, 2.2), xytext=(2.7, 2.2),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))
ax.annotate('', xy=(6.8, 2.2), xytext=(6.2, 2.2),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

# Bottom label
ax.text(5.0, -0.8, 'At 4-loop, the sunrise topology forces elliptic integrals.\n'
        'This is where MATH-2 stalls and MATH-3 extends.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'math3_06_sunrise_family.png')


# ================================================================
# FIG 7: FACTORIZATION BOUNDARY — GRAPH CUT TEST
# Type: Geometric (graph theory)
# Shows: A diagram that CAN be factored (cut one propagator) vs
# one that CANNOT. The cut IS the criterion that separates
# MATH-2 sufficient from MATH-3 required.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Factorizable: One Cut Separates",
    "Irreducible: No Cut Exists",
    size=(18, 9), wspace=0.35)

# Left panel: factorizable graph
# Two blobs connected by one line
for a in [ax1, ax2]:
    a.set_xlim(-2.5, 2.5)
    a.set_ylim(-2.0, 2.5)
    a.set_aspect('equal')

# Left: two subgraphs
blob1 = plt.Circle((-0.8, 0.5), 0.8, fill=True, facecolor=GREEN,
                     alpha=0.12, edgecolor=GREEN, linewidth=2)
ax1.add_patch(blob1)
blob2 = plt.Circle((0.8, 0.5), 0.8, fill=True, facecolor=GREEN,
                     alpha=0.12, edgecolor=GREEN, linewidth=2)
ax1.add_patch(blob2)

# Internal structure suggestions
for angle in [0.5, 1.5, 2.5]:
    ax1.plot([-0.8 + 0.4 * np.cos(angle), -0.8 + 0.4 * np.cos(angle + 1)],
             [0.5 + 0.4 * np.sin(angle), 0.5 + 0.4 * np.sin(angle + 1)],
             color=GREEN, linewidth=1.5, alpha=0.5)
    ax1.plot([0.8 + 0.4 * np.cos(angle), 0.8 + 0.4 * np.cos(angle + 1)],
             [0.5 + 0.4 * np.sin(angle), 0.5 + 0.4 * np.sin(angle + 1)],
             color=GREEN, linewidth=1.5, alpha=0.5)

# Single connecting propagator
ax1.plot([0.0, 0.0], [0.5, 0.5], color=WHITE, linewidth=3, zorder=5)
ax1.plot([-0.01, 0.01], [0.5, 0.5], color=WHITE, linewidth=3, zorder=5)

# Scissors / cut
ax1.plot([0.0, 0.0], [-0.3, 1.3], color=RED, linewidth=3,
         linestyle='--', zorder=6)
ax1.text(0.0, 1.6, 'CUT', fontsize=14, color=RED, ha='center',
         fontweight='bold')

# External legs
ax1.plot([-2.0, -1.6], [0.5, 0.5], color=SILVER, linewidth=2)
ax1.plot([1.6, 2.0], [0.5, 0.5], color=SILVER, linewidth=2)

# Result
ax1.text(0.0, -1.2, 'Result: products of\nlower-loop integrals\n\u2192 \u03b6/ln/Li family',
         fontsize=10, color=GREEN, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN))

# Right: irreducible graph
sunrise = plt.Circle((0, 0.5), 1.0, fill=False, edgecolor=ORANGE,
                       linewidth=2.5, zorder=4)
ax2.add_patch(sunrise)

# Multiple entangled propagators
for i, angle in enumerate([0.3, 1.0, 1.7, 2.4]):
    x0 = 1.0 * np.cos(angle)
    y0 = 0.5 + 1.0 * np.sin(angle)
    x1 = 1.0 * np.cos(angle + np.pi)
    y1 = 0.5 + 1.0 * np.sin(angle + np.pi)
    ax2.plot([x0, x1], [y0, y1], color=ORANGE, linewidth=2, alpha=0.6, zorder=5)

# "No cut" X marks
for angle in [0.6, 1.3, 2.0]:
    cx = 0.5 * np.cos(angle)
    cy = 0.5 + 0.5 * np.sin(angle)
    ax2.text(cx, cy, '\u2717', fontsize=16, color=RED, ha='center',
             va='center', fontweight='bold', zorder=7)

# External legs
ax2.plot([-1.8, -1.0], [0.5, 0.5], color=SILVER, linewidth=2)
ax2.plot([1.0, 1.8], [0.5, 0.5], color=SILVER, linewidth=2)

ax2.text(0.0, 1.8, 'Every cut leaves\nentangled propagators',
         fontsize=9, color=RED, ha='center', style='italic')

# Result
ax2.text(0.0, -1.2, 'Result: elliptic integrals\nK(k), E(k)\n\u2192 MATH-3 required',
         fontsize=10, color=ORANGE, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

save_fig(fig, 'math3_07_factorization_boundary.png')


# ================================================================
# FIG 8: MATH-3 IDENTITY CARD
# Type: Identity card
# Shows: K(k) decomposition, Borwein fix, hierarchy pattern,
# 4-loop wall status. Visual anchor for the paper.
# ================================================================

fig, ax = dark_canvas("MATH-3 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.4, 'THE TRANSCENDENTAL HIERARCHY', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')

# Three columns

# Column 1: Elliptic integrals
ax.text(1.8, 8.2, 'ELLIPTIC INTEGRALS', fontsize=13, color=CYAN,
        ha='center', fontweight='bold')
ax.text(1.8, 7.4, 'K(k) = (\u03c0/2) \u00b7 \u2082F\u2081(\u00bd,\u00bd;1;k\u00b2)',
        fontsize=10, color=WHITE, ha='center',
        fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN))
ax.text(1.8, 6.5, 'Every coefficient rational\nAt rational k\u00b2: integer pair\n'
        'Geometric convergence\nratio = k\u00b2 per term',
        fontsize=9, color=SILVER, ha='center')

ax.text(1.8, 5.3, 'Three moduli computed:', fontsize=9, color=CYAN,
        ha='center', fontweight='bold')
moduli = [
    ('k\u00b2 = 1/4', '~300 digits at 500 terms', GREEN),
    ('k\u00b2 = 1/2', '~150 digits at 500 terms', CYAN),
    ('k\u00b2 = 3/4', '~60 digits at 500 terms', ORANGE),
]
for i, (mod, digits, color) in enumerate(moduli):
    ax.text(1.8, 4.7 - i * 0.5, '%s: %s' % (mod, digits),
            fontsize=8, color=color, ha='center')

# Column 2: Borwein acceleration
ax.text(5.0, 8.2, 'BORWEIN ACCELERATION', fontsize=13, color=GREEN,
        ha='center', fontweight='bold')
ax.text(5.0, 7.4, '\u03b7(s) via d_k coefficients\nError \u223c 3\u207b\u207f',
        fontsize=10, color=WHITE, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GREEN))
ax.text(5.0, 6.5, 'n = 210 \u2192 100+ digits\nAll d_k rational\n'
        '~22,000 Fraction ops\nWorks for any \u03b6(s)',
        fontsize=9, color=SILVER, ha='center')

ax.text(5.0, 5.3, 'Bottleneck resolved:', fontsize=9, color=GREEN,
        ha='center', fontweight='bold')
fixes = [
    ('\u03b6(5): 210 terms (was 10,000)', GREEN),
    ('\u03b6(7): 210 terms (new)', CYAN),
    ('\u03b6(9): 210 terms (new)', BLUE),
]
for i, (fix, color) in enumerate(fixes):
    ax.text(5.0, 4.7 - i * 0.5, fix, fontsize=8, color=color, ha='center')

# Column 3: The hierarchy
ax.text(8.2, 8.2, 'THE HIERARCHY', fontsize=13, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(8.2, 7.4, 'Max weight at L-loop:\n2L \u2212 1',
        fontsize=10, color=WHITE, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

hierarchy = [
    ('1-loop: w=0', 'rational', GREEN),
    ('2-loop: w=3', '\u03b6(3), \u03c0\u00b2', CYAN),
    ('3-loop: w=5', '\u03b6(5), Li\u2084', BLUE),
    ('4-loop: w=7', '\u03b6(7) + ELLIPTIC', ORANGE),
    ('5-loop: w=9', 'predicted', GOLD),
]
for i, (loop, content, color) in enumerate(hierarchy):
    ax.text(8.2, 6.3 - i * 0.6, '%s  %s' % (loop, content),
            fontsize=9, color=color, ha='center', fontweight='bold')

# The 4-loop wall — bottom section
ax.plot([0.5, 9.5], [3.0, 3.0], color=RED, linewidth=2, linestyle='--', alpha=0.5)
ax.text(5.0, 2.5, 'THE 4-LOOP WALL', fontsize=14, color=RED,
        ha='center', fontweight='bold')

wall_items = [
    (1.8, 'Class 1: Polylogarithms\n\u2713 MATH-2 covers', GREEN),
    (5.0, 'Class 2: Elliptic integrals\n\u2713 MATH-3 extends', ORANGE),
    (8.2, 'Class 3: 6 master integrals\n\u2717 Known to 4800 digits only', RED),
]
for x, text, color in wall_items:
    ax.text(x, 1.5, text, fontsize=9, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color, alpha=0.8))

# Bottom banner
ax.text(5.0, 0.4, 'HOWL-MATH-3: Extended basis from 17 to 29 constants. '
        'Borwein fixes \u03b6(5). Elliptic integrals enter at 4-loop.',
        fontsize=10, color=SILVER, ha='center', style='italic')

save_fig(fig, 'math3_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("MATH-3 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'math3_01_transcendental_hierarchy.png',
    'math3_02_borwein_vs_direct.png',
    'math3_03_pslq_weight_pyramid.png',
    'math3_04_elliptic_convergence.png',
    'math3_05_topology_transcendental.png',
    'math3_06_sunrise_family.png',
    'math3_07_factorization_boundary.png',
    'math3_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    