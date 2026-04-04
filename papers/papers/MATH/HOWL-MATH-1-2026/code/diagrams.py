#!/usr/bin/env python3
"""
HOWL MATH-1 Diagrams — The Geometric Ratio beta
8 figures covering beta = pi/4 as cross-section invariant across 9 domains.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: CIRCLE IN BOUNDING SQUARE — THE DEFINITION OF BETA
# Type: Geometric cross-section
# Shows: The fundamental ratio beta = pi/4 as shaded area fraction.
# Text says "circle area / square area = pi/4" but the eye needs
# to SEE the gap between circle and square to grasp the ratio.
# ================================================================

fig, ax = dark_canvas("The Geometric Ratio: %s = %s/4 %s 0.7854" % (
    "\u03b2", "\u03c0", "\u2248"), size=(14, 14))
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')

# Bounding square
sq = plt.Rectangle((-1, -1), 2, 2, fill=True, facecolor=BLUE,
                    alpha=0.15, edgecolor=BLUE, linewidth=2.5, zorder=2)
ax.add_patch(sq)

# Circle inscribed
circle = plt.Circle((0, 0), 1, fill=True, facecolor=CYAN,
                      alpha=0.25, edgecolor=CYAN, linewidth=2.5, zorder=3)
ax.add_patch(circle)

# Dimension lines
# Horizontal d
ax.annotate('', xy=(1, -1.25), xytext=(-1, -1.25),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=1.5))
ax.text(0, -1.40, 'd', fontsize=16, color=WHITE, ha='center',
        fontweight='bold')

# Vertical d
ax.annotate('', xy=(1.25, 1), xytext=(1.25, -1),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=1.5))
ax.text(1.40, 0, 'd', fontsize=16, color=WHITE, ha='center',
        fontweight='bold', rotation=90)

# Labels
ax.text(0, 0, '\u03b2 \u00b7 d\u00b2\n= \u03c0d\u00b2/4', fontsize=18,
        color=CYAN, ha='center', va='center', fontweight='bold')

ax.text(-0.75, 0.75, 'd\u00b2', fontsize=16, color=BLUE, ha='center',
        fontweight='bold', alpha=0.8)

# Corner regions — the gap
for sx, sy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    ax.text(sx * 0.82, sy * 0.82, '1\u2212\u03b2', fontsize=10,
            color=DIM, ha='center', va='center', style='italic')

# Result
result_box(ax, 0, -1.65,
           'Square area = d\u00b2     Circle area = \u03b2\u00b7d\u00b2     '
           'Ratio = \u03c0/4 \u2248 0.7854', GOLD, 11)

save_fig(fig, 'math1_01_beta_definition.png')


# ================================================================
# FIG 2: L1 VS L2 STAIRCASE CONSTRUCTION
# Type: Geometric construction
# Shows: Staircase at multiple refinement levels all measuring 4d,
# while the circle measures pi*d. The visual makes the "paradox"
# immediately clear — and immediately dissolved.
# ================================================================

fig, ax = dark_canvas("L1 vs L2: The Staircase Is Not a Paradox",
                      size=(16, 14))
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect('equal')

# The circle
theta = np.linspace(0, 2 * np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), color=CYAN, linewidth=3,
        zorder=4, label='L2 circumference = \u03c0d')

# Staircase level 1: 4 steps
def staircase(n_steps, color, alpha, lw, zorder_val):
    """Draw n_steps staircase approximation to unit circle."""
    pts_x = []
    pts_y = []
    angles = np.linspace(0, 2 * np.pi, 4 * n_steps + 1)
    for i in range(len(angles) - 1):
        a1 = angles[i]
        a2 = angles[i + 1]
        # Project onto circle, then staircase
        x1 = np.cos(a1)
        y1 = np.sin(a1)
        x2 = np.cos(a2)
        y2 = np.sin(a2)
        # Alternate: horizontal then vertical
        if i % 2 == 0:
            pts_x.extend([x1, x2])
            pts_y.extend([y1, y1])
        else:
            pts_x.extend([x1, x1])
            pts_y.extend([y1, y2])
    ax.plot(pts_x, pts_y, color=color, linewidth=lw, alpha=alpha,
            zorder=zorder_val)

# Simple staircase: inscribed square steps
def box_staircase(n, color, alpha, lw, zorder_val, label_text=""):
    """n subdivisions per quadrant."""
    pts_x = [1.0]
    pts_y = [0.0]
    for quadrant in range(4):
        for step in range(n):
            # Current angle range in this quadrant
            a_start = quadrant * np.pi / 2 + step * np.pi / (2 * n)
            a_end = quadrant * np.pi / 2 + (step + 1) * np.pi / (2 * n)
            # Step to next y, then next x
            x_next = np.cos(a_end)
            y_next = np.sin(a_end)
            # Horizontal then vertical
            pts_x.append(x_next)
            pts_y.append(pts_y[-1])
            pts_x.append(x_next)
            pts_y.append(y_next)
    ax.plot(pts_x, pts_y, color=color, linewidth=lw, alpha=alpha,
            zorder=zorder_val, label=label_text)

box_staircase(2, RED, 0.6, 2.0, 2, 'n=2: L1 = 4d')
box_staircase(4, ORANGE, 0.5, 1.5, 3, 'n=4: L1 = 4d')
box_staircase(8, MAG, 0.4, 1.2, 3, 'n=8: L1 = 4d')

# Labels
result_box(ax, 0, 0.15,
           'L1 circumference = 4d  (every refinement level)\n'
           'L2 circumference = \u03c0d  (the circle)\n'
           'Ratio: \u03c0d / 4d = \u03c0/4 = \u03b2', GOLD, 11)

ax.text(0, -1.40, 'The staircase measures L1 distance. It was never measuring L2.\n'
        'No paradox \u2014 two metrics, one geometry.',
        fontsize=10, color=SILVER, ha='center', style='italic')

legend(ax, loc='upper right')

save_fig(fig, 'math1_02_staircase_l1_l2.png')


# ================================================================
# FIG 3: ISOMORPHISM GRID — 9 DOMAINS, BETA*D^2 INVARIANT ROW
# Type: Heatmap/grid
# Shows: The invariant row (beta*d^2) identical across all 9 domains
# while F and Z rows vary. The visual pattern of sameness in one
# row and difference in others is impossible to convey in text.
# ================================================================

fig, ax = dark_canvas("The Isomorphism: Nine Domains, One Skeleton",
                      size=(18, 12))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 6.0)

domains = ['Geometry', 'Pipe', 'Drag', 'Orifice', 'Capacitor',
           'Poynting', 'Antenna', 'Beam', 'Thermal']
rows = ['Q', 'F', '\u03b2\u00b7d\u00b2', 'Z']
row_colors = [WHITE, BLUE, GOLD, MAG]

q_vals = ['Area', 'Vol/t', 'Force', 'Vol/t', 'C', 'Power', 'Power', 'Area', 'Power']
f_vals = ['1', 'v', '\u00bdpv\u00b2', '\u221a(2\u0394P/\u03c1)', '1', 'S', 'I', '1', '\u03c3T\u2074']
beta_vals = ['\u03b2\u00b7d\u00b2'] * 9
z_vals = ['1', 'f', 'C_d', 'C_d', '\u03b5\u2080/t', '1', '\u03b7', '1/M\u00b2', '\u03b5']

all_vals = [q_vals, f_vals, beta_vals, z_vals]

# Grid
cell_w = 1.1
cell_h = 0.9
x_start = 1.2
y_start = 4.2

# Column headers (domains)
for j, dom in enumerate(domains):
    ax.text(x_start + j * cell_w + cell_w / 2, y_start + cell_h + 0.3,
            dom, fontsize=8, color=SILVER, ha='center', va='center',
            fontweight='bold', rotation=35)

# Row headers and cells
for i, (row_label, row_color) in enumerate(zip(rows, row_colors)):
    y = y_start - i * cell_h
    ax.text(0.5, y + cell_h / 2, row_label, fontsize=13, color=row_color,
            ha='center', va='center', fontweight='bold')

    for j in range(9):
        x = x_start + j * cell_w
        val = all_vals[i][j]

        # Beta row gets highlighted background
        if i == 2:
            rect = plt.Rectangle((x + 0.05, y + 0.05), cell_w - 0.1, cell_h - 0.1,
                                  facecolor=GOLD, alpha=0.15, edgecolor=GOLD,
                                  linewidth=1.5, zorder=2)
            ax.add_patch(rect)
            fontsize = 10
            fw = 'bold'
        else:
            rect = plt.Rectangle((x + 0.05, y + 0.05), cell_w - 0.1, cell_h - 0.1,
                                  facecolor=PAN, alpha=0.4, edgecolor=DIM,
                                  linewidth=0.5, zorder=2)
            ax.add_patch(rect)
            fontsize = 9
            fw = 'normal'

        ax.text(x + cell_w / 2, y + cell_h / 2, val,
                fontsize=fontsize, color=row_color, ha='center', va='center',
                fontweight=fw, zorder=3)

# Annotation
ax.text(5.5, 0.5,
        'The \u03b2\u00b7d\u00b2 row is IDENTICAL across all nine domains.\n'
        'F and Z vary. The geometric invariant is the same object under nine names.',
        fontsize=11, color=GOLD, ha='center', style='italic')

# Department row
depts = ['Math', 'Mech.E', 'Aero.E', 'Chem.E', 'Elec.E',
         'Physics', 'RF Eng.', 'Optics', 'Therm.E']
for j, dept in enumerate(depts):
    x = x_start + j * cell_w
    ax.text(x + cell_w / 2, y_start - 4 * cell_h + 0.15, dept,
            fontsize=7, color=DIM, ha='center', va='center')

save_fig(fig, 'math1_03_isomorphism_grid.png')


# ================================================================
# FIG 4: ELLIPSE GENERALIZATION — BETA PRESERVED ACROSS ECCENTRICITIES
# Type: Geometric progression
# Shows: Circle through high-eccentricity ellipses, each in its
# bounding rectangle, all with area ratio = beta. The visual
# shows the invariance that the formula states abstractly.
# ================================================================

fig, ax = dark_canvas("Ellipse Generalization: \u03b2 = \u03c0/4 at Every Eccentricity",
                      size=(18, 10))
ax.set_xlim(-1.0, 17.0)
ax.set_ylim(-2.0, 3.5)

# Series of ellipses with increasing eccentricity
ellipses = [
    (1.0, 1.0, 'e = 0\n(circle)'),
    (1.3, 0.8, 'e = 0.79'),
    (1.6, 0.6, 'e = 0.93'),
    (2.0, 0.45, 'e = 0.97'),
    (2.5, 0.35, 'e = 0.99'),
]

spacing = 3.2
for idx, (a, b, label) in enumerate(ellipses):
    cx = 1.5 + idx * spacing
    cy = 0.8

    # Bounding rectangle
    rect = plt.Rectangle((cx - a, cy - b), 2 * a, 2 * b,
                          fill=True, facecolor=BLUE, alpha=0.10,
                          edgecolor=BLUE, linewidth=1.5, zorder=2)
    ax.add_patch(rect)

    # Ellipse
    ellipse = matplotlib.patches.Ellipse((cx, cy), 2 * a, 2 * b,
                                          fill=True, facecolor=CYAN, alpha=0.25,
                                          edgecolor=CYAN, linewidth=2, zorder=3)
    ax.add_patch(ellipse)

    # Label below
    ax.text(cx, cy - b - 0.45, label, fontsize=9, color=SILVER,
            ha='center', fontweight='bold')

    # Ratio label
    ax.text(cx, cy, '\u03b2', fontsize=16, color=GOLD, ha='center',
            va='center', fontweight='bold')

    # Dimension labels
    ax.text(cx, cy + b + 0.25, '2a=%.1f' % (2 * a), fontsize=7,
            color=DIM, ha='center')
    ax.text(cx + a + 0.15, cy, '2b=%.1f' % (2 * b), fontsize=7,
            color=DIM, ha='left', va='center')

# Bottom result
result_box(ax, 8.0, -1.5,
           '\u03c0ab / (4ab) = \u03c0/4 = \u03b2  for ALL eccentricities.  '
           'The ratio depends only on the geometry, not the shape.',
           GOLD, 11)

save_fig(fig, 'math1_04_ellipse_generalization.png')


# ================================================================
# FIG 5: BUFFON'S NEEDLE — ORIENTATION SPACE PRODUCING PI
# Type: Geometric (probability)
# Shows: Needle at angle theta crossing parallel lines. The
# semicircular orientation space is the circular domain that
# produces pi in the probability formula. Text cannot show
# the geometry of the orientation space.
# ================================================================

fig, ax = dark_canvas("Buffon's Needle: \u03c0 from Circular Orientation Space",
                      size=(18, 10))
ax.set_xlim(-1.0, 11.0)
ax.set_ylim(-1.5, 4.5)

# Left panel: the physical setup
# Parallel lines
for y_line in [0, 1.5, 3.0]:
    ax.plot([-0.5, 4.5], [y_line, y_line], color=DIM, linewidth=1.5)

# Needles at various angles
np.random.seed(42)
for _ in range(12):
    cx = np.random.uniform(0.3, 4.0)
    cy = np.random.uniform(0.2, 2.8)
    ang = np.random.uniform(0, np.pi)
    L = 0.6
    dx = L / 2 * np.cos(ang)
    dy = L / 2 * np.sin(ang)
    # Check if crosses a line
    crosses = False
    for y_line in [0, 1.5, 3.0]:
        if (cy - dy <= y_line <= cy + dy) or (cy + dy <= y_line <= cy - dy):
            crosses = True
    color = RED if crosses else GREEN
    ax.plot([cx - dx, cx + dx], [cy - dy, cy + dy],
            color=color, linewidth=2.5, zorder=4)

ax.text(2.0, 3.8, 'Physical Setup', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(2.0, -0.5, 'P(crossing) = 2L/(\u03c0d)', fontsize=11,
        color=CYAN, ha='center', fontweight='bold')
ax.text(2.0, -1.0, 'Contains 2/\u03c0 = structure of 1/\u03b2',
        fontsize=9, color=SILVER, ha='center', style='italic')

# Line spacing label
ax.annotate('', xy=(4.7, 1.5), xytext=(4.7, 0),
            arrowprops=dict(arrowstyle='<->', color=WHITE, lw=1.5))
ax.text(5.0, 0.75, 'd', fontsize=14, color=WHITE, fontweight='bold')

# Right panel: the orientation space
oc_x, oc_y = 8.5, 1.5
oc_r = 1.5

# Semicircle — the orientation space
theta_semi = np.linspace(0, np.pi, 200)
ax.plot(oc_x + oc_r * np.cos(theta_semi),
        oc_y + oc_r * np.sin(theta_semi),
        color=CYAN, linewidth=2.5, zorder=4)
ax.plot([oc_x - oc_r, oc_x + oc_r], [oc_y, oc_y],
        color=CYAN, linewidth=2.5, zorder=4)

# Shaded semicircle
theta_fill = np.linspace(0, np.pi, 200)
x_fill = np.concatenate([[oc_x - oc_r],
                          oc_x + oc_r * np.cos(theta_fill),
                          [oc_x + oc_r]])
y_fill = np.concatenate([[oc_y],
                          oc_y + oc_r * np.sin(theta_fill),
                          [oc_y]])
ax.fill(x_fill, y_fill, color=CYAN, alpha=0.12, zorder=2)

# Angle lines
for ang in [np.pi / 6, np.pi / 3, np.pi / 2, 2 * np.pi / 3, 5 * np.pi / 6]:
    ax.plot([oc_x, oc_x + oc_r * 0.9 * np.cos(ang)],
            [oc_y, oc_y + oc_r * 0.9 * np.sin(ang)],
            color=DIM, linewidth=1, alpha=0.5, zorder=3)

ax.text(oc_x, oc_y - 0.4, '\u03b8 \u2208 [0, \u03c0]', fontsize=11,
        color=CYAN, ha='center', fontweight='bold')
ax.text(oc_x, 3.8, 'Orientation Space', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(oc_x, -0.5, 'The \u03c0 comes from integrating\nover this semicircle',
        fontsize=10, color=SILVER, ha='center', style='italic')

# Dividing line
ax.plot([5.5, 5.5], [-1.0, 4.0], color=DIM, linewidth=1, alpha=0.3,
        linestyle='--')

save_fig(fig, 'math1_05_buffon_needle.png')


# ================================================================
# FIG 6: STAIRCASE CONVERGENCE — L1 STAYS 4d, L2 STAYS pid, GAP = BETA
# Type: Running/convergence chart
# Shows: As refinement n increases, L1 path length stays constant
# at 4d while L2 circumference is pid. The persistent gap between
# them IS beta. The curve shape shows the invariance.
# ================================================================

fig, ax = dark_fig("Staircase Convergence: The Gap That Never Closes",
                   xlabel="Refinement level n (steps per quadrant)",
                   ylabel="Path length / d")

n_values = np.arange(1, 51)

# L1 = 4d at every refinement (constant)
l1_values = np.ones_like(n_values, dtype=float) * 4.0

# L2 = pi*d (constant, the true circumference)
l2_values = np.ones_like(n_values, dtype=float) * np.pi

curve(ax, n_values, l1_values, 'L1 path length = 4d (staircase)', RED, 2.5)
curve(ax, n_values, l2_values, 'L2 circumference = \u03c0d', CYAN, 2.5)

# Shade the gap
ax.fill_between(n_values, l2_values, l1_values, alpha=0.08, color=GOLD)

# Gap label
ax.annotate('Gap = 4d \u2212 \u03c0d = (4\u2212\u03c0)d\n'
            'Ratio: \u03c0d / 4d = \u03c0/4 = \u03b2',
            xy=(30, (4 + np.pi) / 2), xytext=(38, 3.3),
            fontsize=11, color=GOLD, fontweight='bold',
            ha='center', va='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

# Reference values
threshold_line(ax, 0, '', GOLD, vertical=False)
ax.text(52, 4.05, '4.0000', fontsize=9, color=RED, va='bottom')
ax.text(52, np.pi + 0.05, '%.4f' % np.pi, fontsize=9, color=CYAN, va='bottom')

ax.set_xlim(0, 55)
ax.set_ylim(2.5, 4.5)

legend(ax, loc='lower right')

note(ax, 2, 2.7, 'The staircase never converges to \u03c0d because '
     'it measures L1, not L2. The gap is \u03b2, permanently.', SILVER, 10)

save_fig(fig, 'math1_06_staircase_convergence.png')


# ================================================================
# FIG 7: BETA VS 1/BETA DIRECTIONAL PATTERN
# Type: Connection/direction map
# Shows: beta mediates rectilinear->circular, 1/beta mediates
# circular->rectilinear. Specific equations on each arrow.
# The directional structure is spatial — impossible in text.
# ================================================================

fig, ax = dark_canvas("\u03b2 vs 1/\u03b2: The Directional Pattern",
                      size=(18, 12))
ax.set_xlim(-1.0, 11.0)
ax.set_ylim(-0.5, 8.5)

# Two columns: left = rectilinear, right = circular
rect_x = 1.5
circ_x = 9.0
mid_x = 5.25

# Column headers
ax.text(rect_x, 7.8, 'RECTILINEAR', fontsize=15, color=BLUE,
        ha='center', fontweight='bold')
ax.text(circ_x, 7.8, 'CIRCULAR', fontsize=15, color=CYAN,
        ha='center', fontweight='bold')

# Forward arrows (beta: rect -> circ)
beta_eqs = [
    (6.8, 'Circle area', 'd\u00b2 \u2192 \u03b2d\u00b2'),
    (5.8, 'Pipe flow', 'v \u2192 v\u00b7\u03b2d\u00b2'),
    (4.8, 'Drag', '\u00bdpv\u00b2 \u2192 F\u00b7\u03b2d\u00b2'),
    (3.8, 'Magnetic flux', 'B \u2192 B\u00b7\u03b2d\u00b2'),
    (2.8, 'Leibniz', '1\u22121/3+1/5\u2212... \u2192 \u03b2'),
]

for y, label, formula in beta_eqs:
    ax.annotate('', xy=(circ_x - 1.5, y), xytext=(rect_x + 1.5, y),
                arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
    ax.text(mid_x, y + 0.25, '\u00d7 \u03b2', fontsize=12, color=GOLD,
            ha='center', fontweight='bold')
    ax.text(rect_x, y - 0.05, label, fontsize=9, color=BLUE,
            ha='center', va='top')
    ax.text(mid_x, y - 0.25, formula, fontsize=8, color=SILVER,
            ha='center', style='italic')

# Reverse arrows (1/beta: circ -> rect)
inv_eqs = [
    (1.5, 'Fourier', 'sin basis \u2192 (4/\u03c0)\u00b7square wave'),
    (0.5, 'Beam divergence', 'circular beam \u2192 (4/\u03c0)\u00b7\u03bb/d'),
]

for y, label, formula in inv_eqs:
    ax.annotate('', xy=(rect_x + 1.5, y), xytext=(circ_x - 1.5, y),
                arrowprops=dict(arrowstyle='->', color=MAG, lw=2.5))
    ax.text(mid_x, y + 0.25, '\u00d7 1/\u03b2', fontsize=12, color=MAG,
            ha='center', fontweight='bold')
    ax.text(circ_x, y - 0.05, label, fontsize=9, color=CYAN,
            ha='center', va='top')
    ax.text(mid_x, y - 0.25, formula, fontsize=8, color=SILVER,
            ha='center', style='italic')

# Dividing line
ax.plot([mid_x, mid_x], [-0.2, 7.4], color=DIM, linewidth=1,
        alpha=0.3, linestyle=':')

save_fig(fig, 'math1_07_directional_pattern.png')


# ================================================================
# FIG 8: MATH-1 IDENTITY CARD
# Type: Identity card
# Shows: Visual anchor — beta with the circle/square geometry,
# the skeleton Q = F*beta*d^2*Z, nine domain names, directional
# pattern. One-page reference for the entire paper.
# ================================================================

fig, ax = dark_canvas("MATH-1 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Central geometry: circle in square
gcx, gcy = 3.0, 5.5
gr = 1.3

sq = plt.Rectangle((gcx - gr, gcy - gr), 2 * gr, 2 * gr,
                    fill=True, facecolor=BLUE, alpha=0.12,
                    edgecolor=BLUE, linewidth=2, zorder=2)
ax.add_patch(sq)

circle = plt.Circle((gcx, gcy), gr, fill=True, facecolor=CYAN,
                      alpha=0.20, edgecolor=CYAN, linewidth=2.5, zorder=3)
ax.add_patch(circle)

ax.text(gcx, gcy, '\u03b2 = \u03c0/4\n\u2248 0.7854', fontsize=16,
        color=GOLD, ha='center', va='center', fontweight='bold')

# The skeleton equation
ax.text(3.0, 3.2, 'Q = F \u00b7 \u03b2 \u00b7 d\u00b2 \u00b7 Z',
        fontsize=18, color=WHITE, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                  linewidth=2))

ax.text(3.0, 2.4, 'F = driving term (varies)\n'
        '\u03b2\u00b7d\u00b2 = geometric invariant (same everywhere)\n'
        'Z = domain impedance (varies)',
        fontsize=9, color=SILVER, ha='center')

# Nine domains radiating from right side
domains = [
    'Geometry', 'Pipe Flow', 'Drag', 'Orifice', 'Capacitor',
    'Poynting', 'Antenna', 'Beam Optics', 'Thermal',
]
domain_colors = [CYAN, BLUE, RED, ORANGE, GREEN, PURPLE, MAG, CYAN, ORANGE]

ax.text(7.8, 9.2, 'NINE DOMAINS', fontsize=14, color=GOLD,
        ha='center', fontweight='bold')
ax.text(7.8, 8.7, 'Same \u03b2\u00b7d\u00b2, nine different names',
        fontsize=9, color=SILVER, ha='center')

for i, (dom, col) in enumerate(zip(domains, domain_colors)):
    y = 8.0 - i * 0.75
    ax.text(7.8, y, dom, fontsize=10, color=col, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=col, alpha=0.8))

# Directional pattern summary
ax.text(3.0, 1.2, 'Directional Pattern', fontsize=12, color=WHITE,
        ha='center', fontweight='bold')
ax.text(1.2, 0.6, 'Rect \u2192 Circ: \u00d7\u03b2', fontsize=11,
        color=GOLD, ha='center', fontweight='bold')
ax.text(4.8, 0.6, 'Circ \u2192 Rect: \u00d71/\u03b2', fontsize=11,
        color=MAG, ha='center', fontweight='bold')

# Extensions
ax.text(7.8, 1.5, 'Extensions', fontsize=11, color=WHITE,
        ha='center', fontweight='bold')
exts = [
    ("Buffon's needle", '2/\u03c0', ORANGE),
    ('Fourier square wave', '4/\u03c0 = 1/\u03b2', MAG),
    ('Leibniz series', '\u03c0/4 = \u03b2', GOLD),
]
for i, (name, val, col) in enumerate(exts):
    ax.text(7.8, 1.0 - i * 0.45, '%s: %s' % (name, val),
            fontsize=9, color=col, ha='center')

# Bottom banner
ax.text(5.0, 0.15, 'HOWL-MATH-1: The Geometric Ratio \u03b2 \u2014 '
        '\u03c0/4 as the cross-section invariant between circular and rectilinear measurement',
        fontsize=10, color=SILVER, ha='center', style='italic')

save_fig(fig, 'math1_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("MATH-1 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'math1_01_beta_definition.png',
    'math1_02_staircase_l1_l2.png',
    'math1_03_isomorphism_grid.png',
    'math1_04_ellipse_generalization.png',
    'math1_05_buffon_needle.png',
    'math1_06_staircase_convergence.png',
    'math1_07_directional_pattern.png',
    'math1_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
print()
print("| Fig | Filename | Section |")
print("|-----|----------|---------|")
print("| 1 | math1_01_beta_definition.png | II.1 Fundamental Ratio |")
print("| 2 | math1_02_staircase_l1_l2.png | II.3 Staircase |")
print("| 3 | math1_03_isomorphism_grid.png | V.2 Nine Instances |")
print("| 4 | math1_04_ellipse_generalization.png | III.1 Beyond Circles |")
print("| 5 | math1_05_buffon_needle.png | VII.2 Buffon |")
print("| 6 | math1_06_staircase_convergence.png | II.3 Staircase |")
print("| 7 | math1_07_directional_pattern.png | IX.1 Observation |")
print("| 8 | math1_08_identity_card.png | XII Boundaries |")
