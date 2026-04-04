#!/usr/bin/env python3
"""
HOWL MATH-5 Diagrams — The n-Ball Remainder Sequence
8 figures covering R_n decay, uniqueness proof, 4D decomposition, instanton skeleton.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: R_n SEQUENCE DECAY — LOG SCALE, n=2 AND n=4 HIGHLIGHTED
# Type: Running/convergence
# Shows: R_n shrinking toward zero as dimension increases. The
# doubly-native n=2 and n=4 are marked. The shape shows how
# quickly higher dimensions waste bounding-cube space.
# ================================================================

fig, ax = dark_fig("The n-Ball Remainder Sequence: R_n Shrinks with Dimension",
                   xlabel="Dimension n",
                   ylabel="R_n = V(n-ball) / V(bounding n-cube)",
                   size=(16, 10))

# Data from math_5_verify.py
n_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r_vals = [1.0, 0.7853981634, 0.5235987756, 0.3084251375,
          0.1644934067, 0.0807455122, 0.0369122341,
          0.0158543442, 0.0064424002, 0.0024903946]

# Main curve
curve(ax, n_vals, r_vals, 'R_n', DIM, 2, style='-', alpha=0.5)

# All points
for i in range(len(n_vals)):
    n = n_vals[i]
    r = r_vals[i]
    if n == 2 or n == 4:
        data_point(ax, n, r, '', GOLD, size=350)
        # Highlight ring
        ax.scatter([n], [r], s=500, facecolors='none', edgecolors=GOLD,
                   linewidth=2.5, zorder=11)
    else:
        data_point(ax, n, r, '', CYAN, size=150)

# Labels for n=2 and n=4
ax.annotate('R\u2082 = \u03c0/4 \u2248 0.785\n(MATH-1: \u03b2)\nDenom: 4 = 2\u00b2\nDOUBLY NATIVE',
            xy=(2, 0.7854), xytext=(4.2, 0.85),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

ax.annotate('R\u2084 = \u03c0\u00b2/32 \u2248 0.308\n(QFT loop integrals)\nDenom: 32 = 2\u2075\nDOUBLY NATIVE',
            xy=(4, 0.3084), xytext=(6.5, 0.45),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# R3 label
ax.annotate('R\u2083 = \u03c0/6\nDenom: 6 = 2\u00d73\nnot doubly native',
            xy=(3, 0.5236), xytext=(0.5, 0.35),
            fontsize=9, color=SILVER,
            arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.0))

# Trend annotation
note(ax, 6, 0.02, 'Higher dimensions: n-ball fills\nless and less of its bounding n-cube',
     DIM, 10)

ax.set_xlim(0.5, 10.8)
ax.set_ylim(-0.05, 1.05)

save_fig(fig, 'math5_01_rn_sequence_decay.png')


# ================================================================
# FIG 2: m! POWER-OF-TWO TEST — THE PROOF VISUALIZED
# Type: Scale/threshold
# Shows: m! on log scale for m=0..15. m=0,1,2 are powers of 2.
# m>=3 all have odd factor 3. The boundary at m=3 IS the proof.
# ================================================================

fig, ax = dark_fig("The Proof: m! is a Power of 2 Only for m \u2264 2",
                   xlabel="m  (dimension n = 2m)",
                   ylabel="m!  (log scale)",
                   size=(16, 10))

m_vals = list(range(0, 16))
factorials = [1]
for i in range(1, 16):
    factorials.append(factorials[-1] * i)

# Plot all
for m in m_vals:
    if m <= 2:
        data_point(ax, m, factorials[m], '', GOLD, size=300)

        if m == 0:
            label = '0! = 1 = 2\u2070'
        elif m == 1:
            label = '1! = 1 = 2\u2070'
        else:
            label = '2! = 2 = 2\u00b9'

        # label = '%d! = %d = 2\u207%s' % (m, factorials[m],
        #         ['0', '0', '\u00b9'][m])
        
        ax.text(m + 0.4, factorials[m] * 1.5, label,
                fontsize=10, color=GOLD, fontweight='bold')
    else:
        data_point(ax, m, factorials[m], '', RED, size=150)

# Connect
curve(ax, m_vals, factorials, '', DIM, 1.5, alpha=0.4)

# The boundary
ax.plot([2.5, 2.5], [0.5, factorials[15] * 2], color=GOLD,
        linewidth=2.5, linestyle='--', alpha=0.6)
ax.text(2.5, factorials[15] * 0.5, 'BOUNDARY', fontsize=12, color=GOLD,
        ha='center', fontweight='bold', rotation=90)

# Odd factor annotation
ax.annotate('m \u2265 3: 3 divides m!\n\u2192 odd factor present\n\u2192 NOT pure 2-power',
            xy=(5, factorials[5]), xytext=(8, factorials[3]),
            fontsize=11, color=RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

# Shade the regions
shaded_region(ax, -0.5, 2.5, GREEN, 0.06)
shaded_region(ax, 2.5, 15.5, RED, 0.03)

ax.text(1.0, 0.25, 'Pure 2-power\n(R_n doubly native)', fontsize=9,
        color=GREEN, ha='center', fontweight='bold')
ax.text(9.0, 0.25, 'Has odd factors\n(R_n needs hybrid arithmetic)', fontsize=9,
        color=RED, ha='center', fontweight='bold')

ax.set_yscale('log')
ax.set_xlim(-0.5, 15.5)
ax.set_ylim(0.1, factorials[15] * 5)

# The conclusion
result_box(ax, 7.5, 0.5,
           'Only n = 2 (m=1) and n = 4 (m=2)\nhave R_n with pure power-of-two denominator.\nProof: three lines. QED.',
           GOLD, 11)

save_fig(fig, 'math5_02_factorial_proof.png')


# ================================================================
# FIG 3: N x R4 LADDER — EACH RUNG IS A QFT EXPRESSION
# Type: Scale/ladder
# Shows: R4, 32R4, 64R4, 128R4, 256R4, 512R4 as rungs of a ladder,
# each labeled with its QFT meaning. R4 is the atomic unit.
# ================================================================

fig, ax = dark_canvas("The R\u2084 Ladder: Every \u03c0\u00b2 in QFT is 32R\u2084",
                      size=(16, 14))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)

rungs = [
    (1, 'R\u2084 = \u03c0\u00b2/32', '0.3084', 'Atomic unit of 4D geometry', CYAN, 1),
    (3, '\u03c0\u00b2 = 32\u00b7R\u2084', '9.8696', 'The fundamental identity', GOLD, 32),
    (5, '\u03a9\u2084 = 2\u03c0\u00b2 = 64\u00b7R\u2084', '19.739', 'Surface area of unit S\u00b3', BLUE, 64),
    (7, '4\u03c0\u00b2 = 128\u00b7R\u2084', '39.478', '4D Coulomb law', GREEN, 128),
    (9, '8\u03c0\u00b2 = 256\u00b7R\u2084', '78.957', 'Instanton action / Chern class', ORANGE, 256),
]

# Ladder rails
ax.plot([2.0, 2.0], [0, 10.5], color=DIM, linewidth=3, alpha=0.4)
ax.plot([8.5, 8.5], [0, 10.5], color=DIM, linewidth=3, alpha=0.4)

for y, formula, value, meaning, color, N in rungs:
    # Rung
    ax.plot([2.0, 8.5], [y, y], color=color, linewidth=3, alpha=0.6)

    # Left: formula
    ax.text(1.5, y + 0.4, formula, fontsize=13, color=color,
            ha='right', fontweight='bold')

    # Center: N value
    ax.text(5.25, y + 0.4, 'N = %d' % N, fontsize=12, color=WHITE,
            ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))

    # Right: meaning
    ax.text(9.0, y + 0.4, meaning, fontsize=10, color=SILVER,
            ha='left')

    # Value below rung
    ax.text(5.25, y - 0.4, '= %s' % value, fontsize=10, color=DIM,
            ha='center', fontfamily='monospace')

# Top: 1/(16pi^2) = 1/(512 R4)
ax.text(5.25, 10.5, '1/(16\u03c0\u00b2) = 1/(512\u00b7R\u2084)',
        fontsize=12, color=MAG, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG))
ax.text(5.25, 10.0, 'The QFT loop factor \u2014 geometry hidden inside convention',
        fontsize=9, color=SILVER, ha='center', style='italic')

# Bottom
ax.text(5.25, -0.5, 'Every factor of \u03c0\u00b2 in 4D physics is 32\u00b7R\u2084.\n'
        'R\u2084 is the atomic unit of four-dimensional geometric content.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'math5_03_r4_ladder.png')


# ================================================================
# FIG 4: n-BALL IN n-CUBE FOR n=2, 3, 4
# Type: Geometric progression
# Shows: Circle in square, sphere cross-section in cube face,
# 4-ball schematic. The shrinking fill fraction is visible.
# ================================================================

fig = plt.figure(figsize=(18, 8), facecolor=BG)

for panel_idx, (n, r_val, formula, color) in enumerate([
    (2, 0.7854, 'R\u2082 = \u03c0/4', CYAN),
    (3, 0.5236, 'R\u2083 = \u03c0/6', BLUE),
    (4, 0.3084, 'R\u2084 = \u03c0\u00b2/32', ORANGE),
]):
    ax = fig.add_subplot(1, 3, panel_idx + 1, aspect='equal')
    ax.set_facecolor(BG)
    ax.axis('off')
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.8, 1.8)

    # Bounding square/cube face
    sq = plt.Rectangle((-1, -1), 2, 2, fill=True, facecolor=color,
                        alpha=0.08, edgecolor=color, linewidth=2, zorder=2)
    ax.add_patch(sq)

    # n-ball representation
    if n == 2:
        ball = plt.Circle((0, 0), 1, fill=True, facecolor=color,
                           alpha=0.25, edgecolor=color, linewidth=2.5, zorder=3)
        ax.add_patch(ball)
    elif n == 3:
        # Sphere as shaded circle with depth cues
        ball = plt.Circle((0, 0), 1, fill=True, facecolor=color,
                           alpha=0.20, edgecolor=color, linewidth=2.5, zorder=3)
        ax.add_patch(ball)
        # Equator ellipse for 3D feel
        theta = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.cos(theta), 0.25 * np.sin(theta), color=color,
                linewidth=1.5, alpha=0.4, zorder=4)
        # Meridian
        ax.plot(0.25 * np.cos(theta), np.sin(theta), color=color,
                linewidth=1.5, alpha=0.4, zorder=4)
    elif n == 4:
        # 4-ball: nested circles suggesting higher dimension
        for r_ring in [1.0, 0.75, 0.5, 0.25]:
            alpha_ring = 0.08 + 0.12 * (1.0 - r_ring)
            ring = plt.Circle((0, 0), r_ring, fill=True, facecolor=color,
                               alpha=alpha_ring, edgecolor=color,
                               linewidth=1.5, zorder=3)
            ax.add_patch(ring)
        # Suggestion of extra dimension: dashed inner structures
        for angle in [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]:
            ax.plot([0, 0.6 * np.cos(angle)], [0, 0.6 * np.sin(angle)],
                    color=color, linewidth=1, alpha=0.3, linestyle='--', zorder=4)

    # Title
    ax.text(0, 1.45, 'n = %d' % n, fontsize=16, color=WHITE,
            ha='center', fontweight='bold')

    # Formula and value
    ax.text(0, -1.35, formula, fontsize=14, color=color,
            ha='center', fontweight='bold')
    ax.text(0, -1.65, '\u2248 %.1f%%' % (r_val * 100), fontsize=11,
            color=SILVER, ha='center')

    # Doubly native marker
    if n in [2, 4]:
        ax.text(0, -1.85, 'DOUBLY NATIVE', fontsize=9, color=GOLD,
                ha='center', fontweight='bold')

fig.suptitle('n-Ball Fill Fraction: Shrinking with Dimension',
             fontsize=16, color=GOLD, fontweight='bold', y=0.98)

path = os.path.join(get_outdir(), 'math5_04_nball_in_ncube.png')
fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
plt.close(fig)
print("  Saved: math5_04_nball_in_ncube.png")


# ================================================================
# FIG 5: PI^2 = 32*R4 PROPAGATION TREE
# Type: Connection/tree map
# Shows: The single identity pi^2 = 32R4 branching into five
# QFT consequences. Each branch carries specific numbers.
# ================================================================

fig, ax = dark_canvas("\u03c0\u00b2 = 32R\u2084: One Identity, Five QFT Consequences",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Root
root_x, root_y = 5.0, 8.5
ax.text(root_x, root_y, '\u03c0\u00b2 = 32 R\u2084', fontsize=20, color=GOLD,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=2.5))

# Five branches
branches = [
    (1.0, 5.0, '\u03a9\u2084 = 2\u03c0\u00b2\n= 64R\u2084', 'Unit 3-sphere\nsurface area', CYAN),
    (3.2, 5.0, '8\u03c0\u00b2\n= 256R\u2084', 'Instanton action\nChern class', ORANGE),
    (5.0, 5.0, '1/(16\u03c0\u00b2)\n= 1/(512R\u2084)', 'QFT loop factor\n(every textbook)', MAG),
    (6.8, 5.0, '4\u03c0\u00b2\n= 128R\u2084', '4D Coulomb\npotential', GREEN),
    (9.0, 5.0, '16\u03c0\u00b2\n= 512R\u2084', 'One-loop\nnormalization', BLUE),
]

for bx, by, formula, meaning, color in branches:
    # Arrow from root to branch
    ax.annotate('', xy=(bx, by + 1.0), xytext=(root_x, root_y - 0.6),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

    # Branch box
    ax.text(bx, by, formula, fontsize=11, color=color, ha='center',
            va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=color,
                      linewidth=1.5))

    # Meaning below
    ax.text(bx, by - 1.3, meaning, fontsize=9, color=SILVER, ha='center')

# Directional pattern at bottom
ax.text(2.0, 1.5, 'R\u2084 direction:', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(2.0, 0.8, 'Topological \u2192 Physical\n(instanton: c\u2082 \u2192 S)',
        fontsize=10, color=ORANGE, ha='center')
ax.text(8.0, 1.5, '1/R\u2084 direction:', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(8.0, 0.8, 'Rectilinear \u2192 Topological\n(Chern: \u222bTr(F\u2227F) \u2192 c\u2082)',
        fontsize=10, color=MAG, ha='center')

# Central note
ax.text(5.0, 1.5, 'Same directional\npattern as MATH-1\n(\u03b2 vs 1/\u03b2 in 2D)',
        fontsize=9, color=DIM, ha='center', style='italic')

save_fig(fig, 'math5_05_pi2_propagation_tree.png')


# ================================================================
# FIG 6: INSTANTON ACTION AS Q = F * R4 * Z SKELETON
# Type: Connection map with numbers
# Shows: S = 256 R4 * c2 / g^2 decomposed into the MATH-1
# skeleton. Each component labeled with its role and value.
# ================================================================

fig, ax = dark_canvas("Instanton Action: The MATH-1 Skeleton in 4D",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# The skeleton equation
ax.text(5.0, 9.0, 'S = 256 \u00b7 R\u2084 \u00b7 c\u2082 / g\u00b2',
        fontsize=22, color=WHITE, ha='center', fontweight='bold',
        fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, linewidth=2.5))

# Four components as boxes with arrows down
components = [
    (1.5, 5.5, '256', '= 8 \u00d7 32', 'F: normalization\n\n8 = topological\n(ensures c\u2082 \u2208 \u2124)\n\n32 = 2\u2075 = dimensional\n(4-ball \u2192 4-cube)', GREEN),
    (4.0, 5.5, 'R\u2084', '= \u03c0\u00b2/32', 'R: geometric remainder\n\n4-ball fill fraction\nof bounding 4-cube\n\nDoubly native:\nFraction exact + Q335 bit-shift', GOLD),
    (6.5, 5.5, 'c\u2082', '\u2208 \u2124', 'Integer: topological\nquantum number\n\nInstanton winding\nnumber\n\nAlways an integer', CYAN),
    (9.0, 5.5, '1/g\u00b2', '= coupling', 'Z: impedance\n\nCoupling strength\nof gauge field\n\nDomain-specific\n(like Z in MATH-1)', MAG),
]

for cx, cy, symbol, value, description, color in components:
    # Arrow from equation
    ax.annotate('', xy=(cx, cy + 1.5), xytext=(cx, 8.3),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

    # Symbol
    ax.text(cx, cy + 1.5, symbol, fontsize=18, color=color,
            ha='center', fontweight='bold')
    ax.text(cx, cy + 0.9, value, fontsize=10, color=SILVER,
            ha='center', fontfamily='monospace')

    # Description
    ax.text(cx, cy - 0.3, description, fontsize=8, color=SILVER,
            ha='center', va='top')

# MATH-1 comparison
ax.plot([0.5, 9.5], [1.5, 1.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(5.0, 1.0, 'MATH-1 analog (2D):  Q = F \u00b7 \u03b2 \u00b7 d\u00b2 \u00b7 Z',
        fontsize=12, color=DIM, ha='center', fontfamily='monospace')
ax.text(5.0, 0.4, 'Same skeleton. Different dimension. R\u2082 \u2192 R\u2084. The pattern holds.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'math5_06_instanton_skeleton.png')


# ================================================================
# FIG 7: FOURIER MIXING — 1/(16pi^2) SPLITS INTO TWO SOURCES
# Type: Split/decomposition
# Shows: The textbook factor 1/(16pi^2) is a mixture of geometric
# content (Omega_4 = 64R4) and Fourier convention ((2pi)^4).
# Separating them reveals R4 as the geometric content.
# ================================================================

fig, ax = dark_canvas("The Fourier Mixing: Two Sources of \u03c0 in 1/(16\u03c0\u00b2)",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# The mixed factor at top
ax.text(5.0, 9.0, '1 / (16\u03c0\u00b2)', fontsize=28, color=WHITE,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=WHITE, linewidth=2))
ax.text(5.0, 8.0, 'appears in EVERY QFT loop calculation', fontsize=10,
        color=SILVER, ha='center', style='italic')

# Split arrows
ax.annotate('', xy=(2.5, 6.0), xytext=(4.2, 7.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))
ax.annotate('', xy=(7.5, 6.0), xytext=(5.8, 7.5),
            arrowprops=dict(arrowstyle='->', color=MAG, lw=2.5))

ax.text(3.5, 7.2, 'SPLIT', fontsize=12, color=GOLD, ha='center',
        fontweight='bold')

# Left: geometric source
ax.text(2.5, 5.5, 'GEOMETRIC', fontsize=14, color=CYAN, ha='center',
        fontweight='bold')
ax.text(2.5, 4.5, '\u03a9\u2084 = 2\u03c0\u00b2 = 64R\u2084', fontsize=14,
        color=CYAN, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, linewidth=1.5))
ax.text(2.5, 3.3, 'Surface area of unit S\u00b3\n(boundary of 4-ball)\n\n'
        'Arises from the geometry\nof 4D momentum space\n\n'
        'This is R\u2084 \u2014 the n-ball\nremainder at n = 4',
        fontsize=9, color=SILVER, ha='center')

# Right: conventional source
ax.text(7.5, 5.5, 'CONVENTIONAL', fontsize=14, color=MAG, ha='center',
        fontweight='bold')
ax.text(7.5, 4.5, '(2\u03c0)\u2074 = 16\u03c0\u2074', fontsize=14,
        color=MAG, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG, linewidth=1.5))
ax.text(7.5, 3.3, 'Four copies of 2\u03c0\n(one per spacetime dimension)\n\n'
        'Fourier transform definition\nfor S-matrix normalization\n\n'
        'Physical content but not\ngeometric \u2014 it is a convention',
        fontsize=9, color=SILVER, ha='center')

# Recombination
ax.text(5.0, 1.5, '\u03a9\u2084 / (2\u03c0)\u2074  =  64R\u2084 / 16\u03c0\u2074  =  '
        '32R\u2084 / (16\u03c0\u2074)  =  \u03c0\u00b2/(16\u03c0\u2074)  =  1/(16\u03c0\u00b2)',
        fontsize=11, color=WHITE, ha='center', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

ax.text(5.0, 0.5, 'The textbook hides R\u2084 inside. Separating the sources makes it visible.\n'
        'This paper does NOT recommend changing the convention.',
        fontsize=10, color=DIM, ha='center', style='italic')

save_fig(fig, 'math5_07_fourier_mixing.png')


# ================================================================
# FIG 8: MATH-5 IDENTITY CARD
# Type: Identity card
# Shows: R_n sequence, n=2,4 uniqueness, pi^2=32R4, four claims.
# Visual anchor for the paper.
# ================================================================

fig, ax = dark_canvas("MATH-5 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5.0, 9.4, 'THE n-BALL REMAINDER SEQUENCE', fontsize=18,
        color=GOLD, ha='center', fontweight='bold')

# Left column: R_n values
ax.text(2.0, 8.2, 'THE SEQUENCE', fontsize=13, color=CYAN,
        ha='center', fontweight='bold')

rn_display = [
    ('R\u2081 = 1', '1.000', DIM),
    ('R\u2082 = \u03c0/4', '0.785', GOLD),
    ('R\u2083 = \u03c0/6', '0.524', SILVER),
    ('R\u2084 = \u03c0\u00b2/32', '0.308', GOLD),
    ('R\u2085 = \u03c0\u00b2/60', '0.164', SILVER),
    ('R\u2086 = \u03c0\u00b3/384', '0.081', DIM),
]

for i, (formula, value, color) in enumerate(rn_display):
    y = 7.4 - i * 0.55
    marker = '\u2605 ' if 'GOLD' in str(color) and color == GOLD else '  '
    ax.text(1.0, y, '%s%s' % (marker, formula), fontsize=10, color=color,
            fontweight='bold')
    ax.text(3.2, y, value, fontsize=10, color=DIM,
            fontfamily='monospace')

# Middle column: the four claims
ax.text(5.5, 8.2, 'FOUR CLAIMS', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')

claims = [
    ('CLAIM 1', 'n=2, 4 uniqueness', 'Pure 2-power denom\nonly at n=2 and n=4', GREEN),
    ('CLAIM 2', '3D survey: 10/10', 'R\u2083 in volume, R\u2082\nin cross-section', CYAN),
    ('CLAIM 3', '\u03c0\u00b2 = 32R\u2084', 'R\u2084 separates in\nQFT one-loop integral', GOLD),
    ('CLAIM 4', 'S = 256R\u2084c\u2082/g\u00b2', 'Instanton as\nQ = F\u00b7R\u00b7Z skeleton', ORANGE),
]

for i, (label, title, detail, color) in enumerate(claims):
    y = 7.4 - i * 1.5
    ax.text(4.5, y, label, fontsize=10, color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor=color))
    ax.text(5.8, y, title, fontsize=10, color=WHITE, fontweight='bold')
    ax.text(5.8, y - 0.5, detail, fontsize=8, color=SILVER)

# Right column: key results
ax.text(8.5, 8.2, 'KEY RESULTS', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')

results = [
    ('\u03c0\u00b2 = 32R\u2084', 'The identity', GOLD),
    ('\u03a9\u2084 = 64R\u2084', '4D solid angle', CYAN),
    ('8\u03c0\u00b2 = 256R\u2084', 'Instanton', ORANGE),
    ('1/(16\u03c0\u00b2) = 1/(512R\u2084)', 'Loop factor', MAG),
    ('R\u2082: 2-bit shift', 'Q335 native', GREEN),
    ('R\u2084: 5-bit shift', 'Q335 native', GREEN),
]

for i, (formula, meaning, color) in enumerate(results):
    y = 7.4 - i * 0.7
    ax.text(8.5, y, formula, fontsize=9, color=color, ha='center',
            fontweight='bold')
    ax.text(8.5, y - 0.3, meaning, fontsize=8, color=DIM, ha='center')

# Bottom: the physical coincidence
ax.text(5.0, 1.2, 'THE PHYSICAL COINCIDENCE', fontsize=13, color=WHITE,
        ha='center', fontweight='bold')
ax.text(5.0, 0.6, 'n = 2 (cross-sections) and n = 4 (spacetime) are the only\n'
        'dimensions where R_n is doubly native. Physics uses exactly these two.\n'
        'Stated as mathematical fact with physical coincidence. No causal claim.',
        fontsize=10, color=SILVER, ha='center', style='italic')

save_fig(fig, 'math5_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("MATH-5 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'math5_01_rn_sequence_decay.png',
    'math5_02_factorial_proof.png',
    'math5_03_r4_ladder.png',
    'math5_04_nball_in_ncube.png',
    'math5_05_pi2_propagation_tree.png',
    'math5_06_instanton_skeleton.png',
    'math5_07_fourier_mixing.png',
    'math5_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
