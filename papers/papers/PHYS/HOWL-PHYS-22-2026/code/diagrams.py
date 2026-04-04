#!/usr/bin/env python3
"""
HOWL PHYS-22 Diagrams — The A2 Geometric Cancellation
8 figures covering cancellation waterfall, UV vs IR, QED progression,
87% cancellation, piece magnitudes, R4 power counting, sign chain.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: THE CANCELLATION WATERFALL
# Type: Waterfall
# Shows: Start at 0, add rational (+1.368), add number-theoretic
# (+0.902), subtract geometric (−2.598), arrive at −0.329.
# The near-zero residue IS the finding.
# ================================================================

fig, ax = dark_fig("The A\u2082 Cancellation Waterfall",
                   xlabel="",
                   ylabel="Cumulative value",
                   size=(16, 10))

# Waterfall stages
stages = [
    ('Start', 0, 0, DIM),
    ('Rational\n197/144', 0, 1.3681, CYAN),
    ('Number-\ntheoretic\n(3/4)\u03b6(3)', 1.3681, 0.9015, BLUE),
    ('Geometric\nR\u2084(8/3\u221216ln2)', 2.2696, -2.5981, RED),
    ('Net A\u2082', 0, -0.3285, GOLD),
]

x_pos = [0, 1.5, 3.0, 4.5, 6.5]

for i, (label, base, height, color) in enumerate(stages):
    x = x_pos[i]
    if i == 0:
        data_point(ax, x, 0, '', DIM, size=100)
        continue
    if i == 4:
        # Net result bar
        ax.bar(x, height, bottom=0, color=color, alpha=0.7, edgecolor=color,
               linewidth=2.5, width=0.8)
        ax.text(x, height - 0.15, '%.3f' % height, fontsize=14, color=color,
                ha='center', fontweight='bold')
    else:
        ax.bar(x, height, bottom=base, color=color, alpha=0.5, edgecolor=color,
               linewidth=2, width=0.8)
        top = base + height
        label_y = base + height / 2
        ax.text(x, label_y, '%+.3f' % height, fontsize=11, color=color,
                ha='center', fontweight='bold', va='center')

    # Connector lines between bars
    if 0 < i < 4:
        top = base + height
        ax.plot([x + 0.4, x_pos[i + 1] - 0.4], [top, top], color=DIM,
                linewidth=1.5, linestyle=':', alpha=0.5)

ax.set_xticks(x_pos)
ax.set_xticklabels([s[0] for s in stages], fontsize=9, color=SILVER)

# Running total labels
ax.text(1.5, 1.5, 'Running:\n+1.368', fontsize=8, color=SILVER, ha='center')
ax.text(3.0, 2.4, 'Running:\n+2.270', fontsize=8, color=SILVER, ha='center')
ax.text(4.5, -0.6, 'Running:\n\u22120.329', fontsize=8, color=SILVER, ha='center')

# The finding
result_box(ax, 3.5, -2.0,
           'Three large pieces sum to a small residue.\n'
           'The geometric piece (\u22122.598) cancels\n'
           '87% of the positive content (+2.270).\n'
           'Only 13% survives as the physical A\u2082.',
           GOLD, 10)

ax.set_xlim(-0.8, 7.5)
ax.set_ylim(-3.0, 3.5)

save_fig(fig, 'phys22_01_waterfall.png')


# ================================================================
# FIG 2: UV VS IR WITHIN THE GEOMETRIC COEFFICIENT
# Type: Comparison/decomposition
# Shows: c_geom = 8/3 - 16ln2. UV term (+2.667) vs IR term
# (-11.090). IR overwhelms UV by 4.2x. This determines the sign.
# ================================================================

fig, ax = dark_fig("Inside the Geometric Piece: UV vs IR",
                   xlabel="",
                   ylabel="Contribution to c_geom = 8/3 \u2212 16 ln 2",
                   size=(16, 10))

# Two bars
uv_val = 8.0 / 3  # +2.667
ir_val = -16 * np.log(2)  # -11.090

ax.bar(0, uv_val, color=GREEN, alpha=0.6, edgecolor=GREEN,
       linewidth=2, width=0.7)
ax.text(0, uv_val + 0.3, '+8/3 = +2.667', fontsize=14, color=GREEN,
        ha='center', fontweight='bold')
ax.text(0, uv_val / 2, 'UV phase\nspace\n(4D angular\nvolume)', fontsize=9,
        color=WHITE, ha='center')

ax.bar(1.5, ir_val, color=RED, alpha=0.6, edgecolor=RED,
       linewidth=2, width=0.7)
ax.text(1.5, ir_val - 0.5, '\u221216 ln 2 = \u221211.090', fontsize=14, color=RED,
        ha='center', fontweight='bold')
ax.text(1.5, ir_val / 2, 'IR regulation\n(electron mass\ncuts off\ndivergence)', fontsize=9,
        color=WHITE, ha='center')

# Net
ax.bar(3.5, uv_val + ir_val, color=GOLD, alpha=0.7, edgecolor=GOLD,
       linewidth=2.5, width=0.7)
ax.text(3.5, (uv_val + ir_val) - 0.5, 'c_geom = \u22128.424', fontsize=14,
        color=GOLD, ha='center', fontweight='bold')

ax.set_xticks([0, 1.5, 3.5])
ax.set_xticklabels(['UV (+)', 'IR (\u2212)', 'Net c_geom'], fontsize=11,
                    color=SILVER)

# The ratio
ax.annotate('IR / UV = 4.2\u00d7', xy=(0.75, 0), xytext=(0.75, -5),
            fontsize=12, color=ORANGE, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE))

# Consequence
result_box(ax, 3.5, 2.5,
           'IR dominates UV by 4.2\u00d7.\n'
           'c_geom < 0 \u2192 geometric piece < 0\n'
           '\u2192 |geometric| > |positive| \u2192 A\u2082 < 0.\n\n'
           'The sign of A\u2082 is set by\n'
           'the infrared physics of the electron mass.',
           GOLD, 10)

ax.set_xlim(-0.8, 5.0)
ax.set_ylim(-13, 5)

save_fig(fig, 'phys22_02_uv_vs_ir.png')


# ================================================================
# FIG 3: QED COEFFICIENT PROGRESSION A1 THROUGH A4
# Type: Progression
# Shows: A1 = +0.5, A2 = -0.329, A3 = +1.181, A4 = -1.912.
# Alternating signs. New transcendental types at each order.
# ================================================================

fig, ax = dark_fig("QED Coefficients A\u2081 Through A\u2084: Alternating Signs",
                   xlabel="Loop order n",
                   ylabel="Coefficient A\u2099",
                   size=(16, 10))

loop_orders = [1, 2, 3, 4]
coefficients = [0.5, -0.3285, 1.1812, -1.9122]
colors_a = [GREEN, RED, GREEN, RED]
n_diagrams = [1, 7, 72, 891]

for i, (n, a_n, color, n_diag) in enumerate(zip(loop_orders, coefficients, colors_a, n_diagrams)):
    ax.bar(n, a_n, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.6)
    y_label = a_n + 0.15 if a_n > 0 else a_n - 0.25
    ax.text(n, y_label, 'A_%d = %+.3f' % (n, a_n), fontsize=11,
            color=color, ha='center', fontweight='bold')
    ax.text(n, -2.8 + i * 0.0, '%d diagrams' % n_diag, fontsize=8,
            color=DIM, ha='center')

# Transcendental types at each order
trans_types = [
    (1, 'Rational\nonly', SILVER),
    (2, '+\u03b6(3), R\u2084,\nln 2', CYAN),
    (3, '+\u03b6(5), Li\u2084,\nR\u2084\u00b2', BLUE),
    (4, '+Elliptic\nintegrals\n(MATH-3 wall)', MAG),
]
for n, types, color in trans_types:
    y_pos = 1.8 if n % 2 == 1 else -0.8
    ax.text(n, y_pos, types, fontsize=7, color=color, ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color,
                      alpha=0.8))

# Zero line
ax.plot([0.3, 4.7], [0, 0], color=DIM, linewidth=1, alpha=0.5)

# Alternating sign pattern
ax.text(2.5, 2.5, 'Signs alternate: + \u2212 + \u2212', fontsize=12,
        color=GOLD, ha='center', fontweight='bold')

ax.set_xlim(0.3, 4.7)
ax.set_ylim(-3.2, 3.0)
ax.set_xticks([1, 2, 3, 4])

save_fig(fig, 'phys22_03_coefficient_progression.png')


# ================================================================
# FIG 4: THREE PIECES SHOWING 87% CANCELLATION
# Type: Comparison bar
# Shows: Positive content (+2.270) vs negative content (−2.598)
# with the 87% overlap visible.
# ================================================================

fig, ax = dark_fig("The 87% Cancellation: Positive vs Negative Content",
                   xlabel="",
                   ylabel="Value",
                   size=(16, 10))

# Positive bar (rational + number-theoretic)
ax.bar(0, 2.2696, color=CYAN, alpha=0.6, edgecolor=CYAN,
       linewidth=2, width=0.8)
ax.text(0, 2.35, '+2.270', fontsize=16, color=CYAN, ha='center',
        fontweight='bold')

# Sub-segments within positive
ax.bar(0, 1.3681, color=CYAN, alpha=0.8, edgecolor=WHITE,
       linewidth=1, width=0.8, bottom=0)
ax.text(0, 0.7, 'Rational\n197/144\n+1.368', fontsize=8, color=WHITE,
        ha='center')
ax.bar(0, 0.9015, color=BLUE, alpha=0.6, edgecolor=WHITE,
       linewidth=1, width=0.8, bottom=1.3681)
ax.text(0, 1.8, 'Number-\ntheoretic\n(3/4)\u03b6(3)\n+0.902', fontsize=8,
        color=WHITE, ha='center')

# Negative bar (geometric)
ax.bar(2, -2.5981, color=RED, alpha=0.6, edgecolor=RED,
       linewidth=2, width=0.8)
ax.text(2, -2.75, '\u22122.598', fontsize=16, color=RED, ha='center',
        fontweight='bold')
ax.text(2, -1.3, 'Geometric\nR\u2084(8/3\u221216ln2)', fontsize=9,
        color=WHITE, ha='center')

# Net result
ax.bar(4, -0.3285, color=GOLD, alpha=0.8, edgecolor=GOLD,
       linewidth=3, width=0.8)
ax.text(4, -0.5, 'Net A\u2082\n\u22120.329', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')

ax.set_xticks([0, 2, 4])
ax.set_xticklabels(['Positive\n(rational +\nnumber-theoretic)',
                     'Negative\n(geometric)',
                     'Net A\u2082'], fontsize=10, color=SILVER)

# Overlap bracket
ax.annotate('', xy=(0.5, 2.27), xytext=(0.5, -0.33),
            arrowprops=dict(arrowstyle='<->', color=GREEN, lw=2))
ax.text(0.8, 1.0, '87%\ncancelled', fontsize=14, color=GREEN,
        fontweight='bold')

ax.annotate('', xy=(0.5, -0.33), xytext=(0.5, -2.60),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(0.8, -1.5, '13%\nsurvives', fontsize=14, color=ORANGE,
        fontweight='bold')

# Zero line
ax.plot([-0.8, 5.0], [0, 0], color=DIM, linewidth=1, alpha=0.5)

ax.set_xlim(-1.0, 5.5)
ax.set_ylim(-3.5, 3.5)

save_fig(fig, 'phys22_04_cancellation.png')


# ================================================================
# FIG 5: EACH PIECE RELATIVE TO |A2| — 4.2x, 2.7x, 7.9x
# Type: Comparison bar (distinct — ratio scale)
# Shows: Each piece's magnitude divided by |A2|. The geometric
# piece at 7.9x towers over the net.
# ================================================================

fig, ax = dark_fig("Each Piece Relative to |A\u2082|: The Internal Scale",
                   xlabel="",
                   ylabel="Magnitude / |A\u2082|",
                   size=(16, 10))

pieces = [
    ('Rational\n197/144', 1.3681 / 0.3285, CYAN, '+1.368'),
    ('Number-\ntheoretic\n(3/4)\u03b6(3)', 0.9015 / 0.3285, BLUE, '+0.902'),
    ('Geometric\nR\u2084\u00d7c_geom', 2.5981 / 0.3285, RED, '\u22122.598'),
    ('Net A\u2082', 1.0, GOLD, '\u22120.329'),
]

for i, (label, ratio, color, val) in enumerate(pieces):
    ax.bar(i, ratio, color=color, alpha=0.6, edgecolor=color,
           linewidth=2, width=0.65)
    ax.text(i, ratio + 0.3, '%.1f\u00d7' % ratio, fontsize=14, color=color,
            ha='center', fontweight='bold')
    ax.text(i, -0.8, val, fontsize=9, color=SILVER, ha='center')

ax.set_xticks(range(len(pieces)))
ax.set_xticklabels([p[0] for p in pieces], fontsize=9, color=SILVER)

# Reference line at 1.0
ax.plot([-0.5, 3.5], [1.0, 1.0], color=GOLD, linewidth=2,
        linestyle='--', alpha=0.5)
ax.text(3.3, 1.2, '|A\u2082| = 1\u00d7\n(reference)', fontsize=9, color=GOLD)

# The insight
result_box(ax, 2.0, -2.5,
           'Every individual piece is LARGER than the net result.\n'
           'The geometric piece alone is 7.9\u00d7 the net.\n'
           'A\u2082 is small because of cancellation,\n'
           'not because the pieces are small.',
           GOLD, 10)

ax.set_xlim(-0.8, 4.0)
ax.set_ylim(-4.0, 10)

save_fig(fig, 'phys22_05_piece_ratios.png')


# ================================================================
# FIG 6: R4 POWER COUNTING BY LOOP ORDER
# Type: Progression/scaling
# Shows: Maximum R4 power growing as n-1 at n loops.
# 1-loop: R4^0, 2-loop: R4^1, 3-loop: R4^2, 4-loop: R4^3 + elliptic.
# ================================================================

fig, ax = dark_fig("Geometric Complexity by Loop Order: R\u2084 Power Counting",
                   xlabel="Loop order n",
                   ylabel="Maximum R\u2084 power (= max \u03c0\u00b2 power)",
                   size=(16, 10))

loop_n = [1, 2, 3, 4]
max_r4 = [0, 1, 2, 3]

curve(ax, loop_n, max_r4, 'R\u2084^{n\u22121} maximum', CYAN, 2.5)

for n, r4_max in zip(loop_n, max_r4):
    data_point(ax, n, r4_max, '', CYAN, size=300)

# Labels at each point
labels_r4 = [
    (1, 0, 'A\u2081 = 1/2\n(pure rational)\nNo R\u2084', GREEN),
    (2, 1, 'A\u2082: R\u2084\u00b9\n(\u03c0\u00b2 appears)', GOLD),
    (3, 2, 'A\u2083: R\u2084\u00b9 + R\u2084\u00b2\n(\u03c0\u00b2 and \u03c0\u2074)', ORANGE),
    (4, 3, 'A\u2084: R\u2084\u00b9 + R\u2084\u00b2 + R\u2084\u00b3\n+ ELLIPTIC\n(MATH-3 wall)', RED),
]

for n, r4, label, color in labels_r4:
    x_off = 0.3
    y_off = 0.3 if n != 1 else 0.4
    ax.text(n + x_off, r4 + y_off, label, fontsize=9, color=color,
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color,
                      alpha=0.8))

# MATH-3 wall
ax.plot([3.7, 3.7], [-0.5, 3.8], color=RED, linewidth=2.5,
        linestyle='--', alpha=0.5)
ax.text(3.9, -0.3, 'MATH-3\nwall', fontsize=10, color=RED,
        fontweight='bold')

# The substitution
result_box(ax, 2.5, -1.5,
           'R\u2084 = \u03c0\u00b2/32 (4-ball volume fraction, MATH-5).\n'
           'Every \u03c0\u00b2 in a QED coefficient = one power of R\u2084\n'
           '= one factor of the 4D phase space volume.',
           SILVER, 9)

ax.set_xlim(0.5, 4.8)
ax.set_ylim(-2.5, 4.5)
ax.set_xticks([1, 2, 3, 4])

save_fig(fig, 'phys22_06_r4_power_counting.png')


# ================================================================
# FIG 7: THE SIGN CHAIN — IR DOMINANCE → NEGATIVE A2
# Type: Connection/flow
# Shows: The causal chain from 16ln2 > 8/3 through c_geom < 0,
# geometric piece < 0, |geometric| > positive, A2 < 0.
# ================================================================

fig, ax = dark_canvas("The Sign Chain: How IR Dominance Makes A\u2082 Negative",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Chain of causation, left to right
chain_nodes = [
    (1.0, 5.0, '16 ln 2 > 8/3\n(11.09 > 2.67)', 'IR term\nexceeds\nUV term', RED),
    (3.2, 5.0, 'c_geom < 0\n(\u22128.424)', 'Geometric\ncoefficient\nnegative', ORANGE),
    (5.4, 5.0, 'R\u2084 \u00d7 c_geom\n= \u22122.598', 'Geometric\npiece\nnegative', RED),
    (7.6, 5.0, '|\u22122.598| > +2.270', 'Negative\nexceeds\npositive', MAG),
    (9.2, 5.0, 'A\u2082 < 0\n(\u22120.329)', 'Two-loop\ncorrection\nNEGATIVE', GOLD),
]

for x, y, label, sublabel, color in chain_nodes:
    ax.text(x, y, label, fontsize=10, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color,
                      linewidth=2))
    ax.text(x, y - 1.5, sublabel, fontsize=8, color=SILVER, ha='center')

# Arrows between nodes
for i in range(len(chain_nodes) - 1):
    x1 = chain_nodes[i][0] + 0.7
    x2 = chain_nodes[i + 1][0] - 0.7
    ax.annotate('', xy=(x2, 5.0), xytext=(x1, 5.0),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Top: the physical origin
ax.text(1.0, 8.5, 'PHYSICAL ORIGIN', fontsize=14, color=WHITE,
        fontweight='bold')
ax.text(1.0, 7.5, 'The electron mass\nregulates the IR\ndivergence in\nloop integrals.',
        fontsize=9, color=SILVER)
ax.annotate('', xy=(1.0, 6.0), xytext=(1.0, 7.2),
            arrowprops=dict(arrowstyle='->', color=DIM, lw=1.5))

# Bottom: the physical consequence
ax.text(9.2, 2.0, 'CONSEQUENCE', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(9.2, 1.0, 'The two-loop QED\ncorrection REDUCES\nthe electron g\u22122.',
        fontsize=9, color=SILVER, ha='center')

ax.text(5.0, 1.0, 'The sign of A\u2082 is set by the infrared physics\n'
        'of the electron mass in 4D spacetime.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys22_07_sign_chain.png')


# ================================================================
# FIG 8: PHYS-22 IDENTITY CARD
# Type: Identity card
# Shows: Three pieces, 87%, the smallness is an accident.
# ================================================================

fig, ax = dark_canvas("PHYS-22 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE A\u2082 GEOMETRIC CANCELLATION', fontsize=20, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 8.5, 'Three pieces, 87% cancellation, the smallness is an accident.',
        fontsize=11, color=SILVER, ha='center', style='italic')

# The formula
ax.text(5, 7.3, 'A\u2082 = 197/144 + (3/4)\u03b6(3) + R\u2084(8/3 \u2212 16 ln 2)',
        fontsize=16, color=WHITE, ha='center', fontweight='bold',
        fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=2))

# Three pieces
pieces_card = [
    ('Rational:', '197/144 = +1.368', '4.2\u00d7 |A\u2082|', CYAN),
    ('Number-theoretic:', '(3/4)\u03b6(3) = +0.902', '2.7\u00d7 |A\u2082|', BLUE),
    ('Geometric:', 'R\u2084 \u00d7 c_geom = \u22122.598', '7.9\u00d7 |A\u2082|', RED),
]

for i, (ptype, value, ratio, color) in enumerate(pieces_card):
    y = 6.0 - i * 0.6
    ax.text(1.5, y, ptype, fontsize=10, color=SILVER)
    ax.text(5.0, y, value, fontsize=11, color=color, fontweight='bold')
    ax.text(8.5, y, ratio, fontsize=10, color=DIM)

# The cancellation
ax.plot([0.5, 9.5], [3.8, 3.8], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

ax.text(5, 3.3, 'THE CANCELLATION', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')

cancel_items = [
    ('Positive content:', '+2.270', CYAN),
    ('Negative content:', '\u22122.598', RED),
    ('Cancelled:', '87.4%', ORANGE),
    ('Surviving:', '12.6% \u2192 A\u2082 = \u22120.329', GOLD),
]
for i, (label, val, color) in enumerate(cancel_items):
    y = 2.6 - i * 0.5
    ax.text(3.0, y, label, fontsize=10, color=SILVER)
    ax.text(7.0, y, val, fontsize=11, color=color, fontweight='bold')

# Bottom
ax.text(5, 0.5, 'The smallness of A\u2082 is accidental \u2014 no symmetry requires it.\n'
        'R\u2084 = \u03c0\u00b2/32 makes the 4D origin visible. Every \u03c0\u00b2 = one R\u2084.\n'
        'This is Level 1 structure: it holds in any universe with QED.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys22_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-22 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys22_01_waterfall.png',
    'phys22_02_uv_vs_ir.png',
    'phys22_03_coefficient_progression.png',
    'phys22_04_cancellation.png',
    'phys22_05_piece_ratios.png',
    'phys22_06_r4_power_counting.png',
    'phys22_07_sign_chain.png',
    'phys22_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    