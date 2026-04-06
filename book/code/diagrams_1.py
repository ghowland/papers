#!/usr/bin/env python3
"""
HOWL Book Diagrams — The Rational Universe (Set 2)
8 figures covering flat/curved dual view, Bessel zeros, alpha-power scaling,
hydrogen two-path, precision landscape, gap comparison, k1 bug, fraction structure.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Arc, Wedge
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global palette (D7.2) ──
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

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)


# ================================================================
# FIG 9: FLAT INSIDE / CURVED OUTSIDE
# Type: Type 4 (Geometric Cross-Section)
# Shows: Same boundary reads flat from inside, curved from outside
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

# LEFT PANEL: Inside view — flat
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)

# Flat grid on the ground
for gx in np.linspace(1, 9, 9):
    ax1.plot([gx, gx], [1.5, 4.5], color=DIM, linewidth=0.6, alpha=0.5)
for gy in np.linspace(1.5, 4.5, 7):
    ax1.plot([1, 9], [gy, gy], color=DIM, linewidth=0.6, alpha=0.5)

# Flat horizon line
ax1.plot([0.5, 9.5], [4.5, 4.5], color=CYAN, linewidth=2, alpha=0.8)

# Sky gradient (subtle)
ax1.axhspan(4.5, 9.5, alpha=0.03, color=BLUE)

# Observer (stick figure)
ax1.plot([5, 5], [2.0, 3.2], color=WHITE, linewidth=2)  # body
ax1.plot([4.5, 5.5], [2.8, 2.8], color=WHITE, linewidth=1.5)  # arms
circle_head = plt.Circle((5, 3.4), 0.2, facecolor=WHITE, edgecolor=WHITE, zorder=5)
ax1.add_patch(circle_head)

# Railroad tracks converging to vanishing point
ax1.plot([3.5, 4.8], [1.5, 4.5], color=SILVER, linewidth=1.2, alpha=0.6)
ax1.plot([6.5, 5.2], [1.5, 4.5], color=SILVER, linewidth=1.2, alpha=0.6)

ax1.text(5, 9, 'INSIDE THE BOUNDARY', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax1.text(5, 8.2, 'Reading: FLAT', color=WHITE, fontsize=12, ha='center')
ax1.text(5, 7.4, 'Flat horizon, flat grid\nLocal physics, Euclidean geometry',
         color=SILVER, fontsize=9, ha='center')
ax1.text(5, 0.8, 'Every soliton boundary looks\nlocally flat from inside',
         color=DIM, fontsize=8, ha='center', fontstyle='italic')

# RIGHT PANEL: Outside view — curved
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)

# Curved sphere
sphere = plt.Circle((5, 4.5), 2.8, fill=False, edgecolor=ORANGE, linewidth=2.5, zorder=3)
ax2.add_patch(sphere)
# Interior shading
sphere_fill = plt.Circle((5, 4.5), 2.8, facecolor=PAN, edgecolor='none', alpha=0.5, zorder=2)
ax2.add_patch(sphere_fill)

# Curved grid lines on sphere surface (latitude lines)
for angle in np.linspace(-60, 60, 5):
    rad = np.radians(angle)
    cy = 4.5 + 2.8 * np.sin(rad)
    half_width = 2.8 * np.cos(rad)
    if half_width > 0.3:
        xs = np.linspace(5 - half_width, 5 + half_width, 50)
        # Slight curve for visual effect
        ys = np.full_like(xs, cy) + 0.1 * np.sin(np.linspace(0, np.pi, 50)) * (half_width / 2.8)
        ax2.plot(xs, ys, color=DIM, linewidth=0.6, alpha=0.5)

# Longitude lines (curved)
for lon_frac in np.linspace(0.2, 0.8, 4):
    x_center = 5 - 2.8 + lon_frac * 5.6
    # Draw as arcs
    ts = np.linspace(-1, 1, 50)
    xs = np.full_like(ts, x_center) + 0.3 * np.sin(ts * np.pi)
    ys = 4.5 + ts * 2.5
    mask = (xs - 5)**2 + (ys - 4.5)**2 <= 2.8**2
    ax2.plot(xs[mask], ys[mask], color=DIM, linewidth=0.6, alpha=0.5)

# Observer outside (small eye icon)
ax2.scatter([8.5], [7.5], color=WHITE, s=100, marker='o', edgecolors=WHITE, linewidth=1.5, zorder=5)
ax2.plot([8.5, 7.0], [7.3, 6.5], color=WHITE, linewidth=1, alpha=0.5)

ax2.text(5, 9, 'OUTSIDE THE BOUNDARY', color=ORANGE, fontsize=14, fontweight='bold', ha='center')
ax2.text(5, 8.2, 'Reading: CURVED', color=WHITE, fontsize=12, ha='center')
ax2.text(5, 7.6, 'Sphere, curvature visible\nGlobal structure, Riemannian geometry',
         color=SILVER, fontsize=9, ha='center')
ax2.text(5, 0.8, 'Every soliton boundary looks\nglobally curved from outside',
         color=DIM, fontsize=8, ha='center', fontstyle='italic')

fig.suptitle('Same Boundary, Two Readings', color=WHITE, fontsize=17, fontweight='bold', y=0.97)

save(fig, 'book_09_flat_curved.png')


# ================================================================
# FIG 10: BESSEL ZEROS → RING GAPS
# Type: Type 1 (Running/Convergence) + Type 4 (Geometric)
# Shows: Bessel function zeros correspond to ring/gap structure in discs
# ================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12), gridspec_kw={'hspace': 0.35, 'height_ratios': [1, 1]})
fig.patch.set_facecolor(BG)

# TOP: Bessel function J0
from scipy.special import j0 as _j0_attempt
# Fallback if scipy not available
try:
    from scipy.special import j0
    has_scipy = True
except ImportError:
    has_scipy = False

x = np.linspace(0, 16, 500)
if has_scipy:
    y = j0(x)
else:
    # Manual J0 approximation using series
    def j0_manual(x_arr):
        result = np.zeros_like(x_arr)
        for k in range(20):
            term = ((-1)**k / (np.math.factorial(k))**2) * (x_arr / 2.0)**(2*k)
            result += term
        return result
    y = j0_manual(x)

style_ax(ax1, title=r'Bessel Function $J_0(x)$ — Zeros Define the Gaps',
         xlabel='x (radial coordinate)', ylabel=r'$J_0(x)$')
ax1.plot(x, y, color=CYAN, linewidth=2.5)
ax1.axhline(y=0, color=DIM, linewidth=1, linestyle='-', alpha=0.4)

# Mark zeros
zeros = [2.4048, 5.5201, 8.6537, 11.7915, 14.9309]
zero_labels = ['2.405', '5.520', '8.654', '11.792', '14.931']
for i, (z, lbl) in enumerate(zip(zeros, zero_labels)):
    ax1.axvline(x=z, color=GOLD, linewidth=1.2, linestyle='--', alpha=0.6)
    ax1.scatter([z], [0], color=GOLD, s=150, zorder=5, edgecolors=WHITE, linewidth=1.5)
    y_offset = 0.25 if i % 2 == 0 else -0.30
    ax1.text(z, y_offset, lbl, color=GOLD, fontsize=9, fontweight='bold', ha='center')

ax1.set_xlim(-0.5, 16.5)
ax1.set_ylim(-0.45, 1.1)
ax1.text(0.5, 0.9, 'At each zero: wave amplitude = 0\nNo stable orbit possible',
         color=SILVER, fontsize=9,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM))

# BOTTOM: Disc with ring gaps
ax2.set_facecolor(BG)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_xlim(-8, 8)
ax2.set_ylim(-5, 5)

# Draw concentric rings with gaps at Bessel zeros (scaled)
scale = 0.45  # scale zeros to fit
max_r = 16 * scale

# Draw filled rings between zeros
ring_colors = [PURPLE, BLUE, CYAN, GREEN, ORANGE]
boundaries = [0] + [z * scale for z in zeros] + [max_r]
for i in range(len(boundaries) - 1):
    r_inner = boundaries[i]
    r_outer = boundaries[i + 1]
    # Draw as annulus
    theta = np.linspace(0, 2 * np.pi, 200)
    # Outer edge
    if i < len(ring_colors):
        col = ring_colors[i]
        alpha = 0.25
    else:
        col = DIM
        alpha = 0.15
    # Fill the annulus
    for r in np.linspace(r_inner + 0.05, r_outer - 0.05, 8):
        circle = plt.Circle((0, 0), r, fill=False, edgecolor=col, linewidth=0.8, alpha=alpha)
        ax2.add_patch(circle)

# Draw gap lines at Bessel zeros
for i, z in enumerate(zeros):
    r = z * scale
    gap_circle = plt.Circle((0, 0), r, fill=False, edgecolor=GOLD,
                            linewidth=2, linestyle='--', alpha=0.8)
    ax2.add_patch(gap_circle)
    # Label
    angle = np.radians(30 + i * 15)
    lx = (r + 0.3) * np.cos(angle)
    ly = (r + 0.3) * np.sin(angle)
    ax2.text(lx, ly, 'Gap %d' % (i + 1), color=GOLD, fontsize=7, fontweight='bold',
             ha='center', rotation=0)

# Central bulge
bulge = plt.Circle((0, 0), 0.4, facecolor=ORANGE, edgecolor=GOLD, linewidth=1, alpha=0.4)
ax2.add_patch(bulge)

ax2.text(0, -4.3, 'Ring gaps at Bessel zeros: Saturn, asteroid belt, galaxy disc',
         color=SILVER, fontsize=10, ha='center')
ax2.text(0, 4.3, 'Disc Cross-Section with Gaps at Bessel Zeros',
         color=GOLD, fontsize=13, fontweight='bold', ha='center')

# Dashed lines connecting top panel zeros to bottom panel gaps
# (implied by vertical alignment — both panels share the same x-scale spirit)

save(fig, 'book_10_bessel_zeros.png')


# ================================================================
# FIG 11: ALPHA-POWER SCALING — SIX SUB-PPB VALUES
# Type: Type 1 (Running/Convergence)
# Shows: Miss doubles exactly when alpha power doubles
# ================================================================

fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor(BG)

# Data: six sub-ppb values
# alpha^1 quantities miss by 0.22 ppb
# alpha^2 quantities miss by 0.44 ppb
values_a1 = [
    (1, 0.22, r'$\alpha^{-1}$ vs CODATA', GOLD),
    (1, 0.22, r'$a_0$', CYAN),
    (1, 0.22, r'$\mu_0$', GREEN),
    (1, 0.22, r'$a_\mu$ (QED shift)', MAG),
]
values_a2 = [
    (2, 0.44, r'$R_\infty$', ORANGE),
    (2, 0.44, 'f(1S-2S)', BLUE),
]

# Offset points slightly to avoid overlap
offsets_a1 = [-0.06, -0.02, 0.02, 0.06]
offsets_a2 = [-0.03, 0.03]

for i, (xv, yv, label, col) in enumerate(values_a1):
    xp = xv + offsets_a1[i]
    ax.scatter([xp], [yv], color=col, s=200, zorder=5, edgecolors=WHITE, linewidth=2)
    ax.annotate(label, xy=(xp, yv), xytext=(xp + 0.15, yv + 0.03),
                color=col, fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=col, lw=1, alpha=0.6))

for i, (xv, yv, label, col) in enumerate(values_a2):
    xp = xv + offsets_a2[i]
    ax.scatter([xp], [yv], color=col, s=200, zorder=5, edgecolors=WHITE, linewidth=2)
    ax.annotate(label, xy=(xp, yv), xytext=(xp + 0.15, yv + 0.03),
                color=col, fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=col, lw=1, alpha=0.6))

# Scaling line: miss = 0.22 * alpha_power
x_line = np.array([0.5, 2.5])
y_line = 0.22 * x_line
ax.plot(x_line, y_line, color=GOLD, linewidth=2, linestyle='--', alpha=0.7,
        label='miss = 0.22 ppb ' + r'$\times$' + ' (power of ' + r'$\alpha$)')

# Horizontal reference lines
ax.axhline(y=0.22, color=DIM, linewidth=0.8, linestyle=':', alpha=0.4)
ax.axhline(y=0.44, color=DIM, linewidth=0.8, linestyle=':', alpha=0.4)
ax.text(2.45, 0.215, '0.22 ppb', color=DIM, fontsize=8, ha='right')
ax.text(2.45, 0.435, '0.44 ppb', color=DIM, fontsize=8, ha='right')

# 2x label
ax.annotate('', xy=(2.35, 0.44), xytext=(2.35, 0.22),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(2.42, 0.33, r'$2\times$', color=GOLD, fontsize=14, fontweight='bold')

style_ax(ax, title=r'$\alpha$-Power Scaling: Miss Doubles When Power Doubles',
         xlabel=r'Power of $\alpha$ in the derived quantity',
         ylabel='Miss from measurement (ppb)')
ax.set_xlim(0.5, 2.7)
ax.set_ylim(0.0, 0.6)
ax.set_xticks([1, 2])
ax.set_xticklabels([r'$\alpha^1$', r'$\alpha^2$'], fontsize=12, color=SILVER)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='upper left')

# Result box
ax.text(1.5, 0.55, 'Every sub-ppb value follows this scaling.\nNo exceptions.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

save(fig, 'book_11_alpha_scaling.png')


# ================================================================
# FIG 12: HYDROGEN TWO-PATH CONVERGENCE
# Type: Type 5 (Connection/Integer Map)
# Shows: Two independent paths both predicting hydrogen, from opposite physics
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

# Central hydrogen atom
hx, hy = 9, 5.5
h_circle = plt.Circle((hx, hy), 1.0, facecolor=PAN, edgecolor=GOLD,
                       linewidth=3, zorder=10)
ax.add_patch(h_circle)
ax.text(hx, hy + 0.15, 'H', color=GOLD, fontsize=28, fontweight='bold',
        ha='center', va='center', zorder=11)
ax.text(hx, hy - 0.4, 'Hydrogen', color=SILVER, fontsize=10,
        ha='center', va='center', zorder=11)

# LEFT PATH: QED → Spectroscopy
left_steps = [
    (2.5, 10.5, r'$a_e$', 'Electron g-2\n(Harvard)', MAG),
    (2.5, 8.5, r'$\alpha$', '5-loop QED\n0.007 ppb', GOLD),
    (2.5, 6.5, r'$R_\infty$', 'Rydberg\n0.44 ppb', CYAN),
    (5.5, 5.5, 'f(1S-2S)', '0.44 ppb\nspectroscopy', ORANGE),
]

for i, (x, y, label, note, col) in enumerate(left_steps):
    box = FancyBboxPatch((x - 1.2, y - 0.55), 2.4, 1.1, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.8, zorder=5)
    ax.add_patch(box)
    ax.text(x, y + 0.15, label, color=col, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=6)
    ax.text(x, y - 0.25, note, color=SILVER, fontsize=7, ha='center', va='center', zorder=6)

# Arrows for left path
arrow_kw = dict(arrowstyle='->', color=CYAN, lw=2)
ax.annotate('', xy=(2.5, 9.05), xytext=(2.5, 9.95), arrowprops=arrow_kw)
ax.annotate('', xy=(2.5, 7.05), xytext=(2.5, 7.95), arrowprops=arrow_kw)
ax.annotate('', xy=(4.3, 5.5), xytext=(3.7, 6.1), arrowprops=arrow_kw)
# Arrow from f(1S-2S) to hydrogen
ax.annotate('', xy=(hx - 1.0, hy), xytext=(6.7, 5.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# RIGHT PATH: Gauge integers → BBN
right_steps = [
    (15.5, 10.5, '11, 13', 'Gauge integers\nSU(2) betas', BLUE),
    (15.5, 8.5, '(22/13)' + r'$\pi$', 'DM ratio\n725 ppm', PURPLE),
    (15.5, 6.5, r'$\eta_{10}$', 'Baryon ratio\n0.24%', GREEN),
    (12.5, 5.5, 'D/H', r'0.12$\sigma$' + '\nBBN abundance', RED),
]

for i, (x, y, label, note, col) in enumerate(right_steps):
    box = FancyBboxPatch((x - 1.2, y - 0.55), 2.4, 1.1, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=1.8, zorder=5)
    ax.add_patch(box)
    ax.text(x, y + 0.15, label, color=col, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=6)
    ax.text(x, y - 0.25, note, color=SILVER, fontsize=7, ha='center', va='center', zorder=6)

# Arrows for right path
ax.annotate('', xy=(15.5, 9.05), xytext=(15.5, 9.95), arrowprops=arrow_kw)
ax.annotate('', xy=(15.5, 7.05), xytext=(15.5, 7.95), arrowprops=arrow_kw)
ax.annotate('', xy=(13.7, 5.5), xytext=(14.3, 6.1), arrowprops=arrow_kw)
# Arrow from D/H to hydrogen
ax.annotate('', xy=(hx + 1.0, hy), xytext=(11.3, 5.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Labels for each path
ax.text(2.5, 11.5, 'QED PATH', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax.text(2.5, 11.0, 'How hydrogen atoms absorb light', color=SILVER, fontsize=9, ha='center')
ax.text(15.5, 11.5, 'BBN PATH', color=BLUE, fontsize=14, fontweight='bold', ha='center')
ax.text(15.5, 11.0, 'How much hydrogen the universe contains', color=SILVER, fontsize=9, ha='center')

# Title
ax.text(9, 11.5, 'Two Paths to Hydrogen', color=GOLD, fontsize=17, fontweight='bold', ha='center')

# Bottom text
ax.text(9, 1.5, 'Same element. Different physics. Different measurements.\n'
        'Both matching. The derivation graph is a web, not a tree.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

# Physics labels on the paths
ax.text(1.0, 7.5, 'QED\nperturbation\ntheory', color=DIM, fontsize=7, ha='center')
ax.text(17.0, 7.5, 'Cosmological\nnucleo-\nsynthesis', color=DIM, fontsize=7, ha='center')

save(fig, 'book_12_hydrogen_two_path.png')


# ================================================================
# FIG 13: PRECISION LANDSCAPE — ALL 53 VALUES
# Type: Type 2 (Scale/Landscape)
# Shows: All derived values on log scale, colored by domain
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)

# Values organized by domain with precision (log10 of miss ratio or ppb)
# Approximate log10(miss) for plotting
domains_data = {
    'QED': ([np.log10(0.007), np.log10(0.22), np.log10(0.22), np.log10(0.22),
             np.log10(0.44), np.log10(0.44)],
            [r'$\alpha^{-1}$', r'$a_0$', r'$\mu_0$', r'$\alpha$ vs CODATA',
             r'$R_\infty$', 'f(1S-2S)'],
            GOLD),
    'EW': ([np.log10(195), np.log10(207), np.log10(264), np.log10(2400), np.log10(2700),
            np.log10(4700), np.log10(5700), np.log10(5800), np.log10(6700),
            np.log10(8100), np.log10(8100), np.log10(8400), np.log10(4020)],
           ['M_W(B)', 'consist.', 'V_ud', 'sin2eff', 'R_l', 'Gztt', 'Gzmm', 'Gz(v1)',
            'Gzee', 'Gz(v2)', 'Gzinv', 'Gzhad', 'M_W(A)'],
           GREEN),
    'GUT': ([np.log10(12), np.log10(3300), np.log10(640)],
            ['sin2tW', 'alpha_s', 'gap'],
            ORANGE),
    'Cosmo': ([np.log10(725), np.log10(727), np.log10(2400), np.log10(2000),
               np.log10(1500), np.log10(4400)],
              ['DM/b', 'Omega_b', 'eta', 'Omega_DE', 'rho_L', 'Omega_m'],
              BLUE),
    'Nuclear': ([1.0, 1.0, 0.5, 4.5],  # sigma-like: use log10(sigma_equiv_ppm)
                ['D/H', 'Y_p', 'He-3', 'Li-7'],
                RED),
    'Muon': ([np.log10(0.22), 4.0],
             ['a_mu(QED)', 'g-2 tension'],
             MAG),
    'Flavor': ([np.log10(264), 1.5],
               ['V_ud', 'CKM def.'],
               PURPLE),
    'Mass': ([np.log10(62)],
             ['m_tau(K)'],
             CYAN),
}

# Plot each domain as a horizontal band
y_pos = 0
domain_names = ['QED', 'GUT', 'Mass', 'EW', 'Cosmo', 'Flavor', 'Nuclear', 'Muon']
y_positions = {}

for dname in domain_names:
    if dname in domains_data:
        vals, labels, col = domains_data[dname]
        n = len(vals)
        ys = [y_pos + 0.3 * j for j in range(n)]
        for j, (v, lbl) in enumerate(zip(vals, labels)):
            ax.scatter([v], [ys[j]], color=col, s=120, zorder=5, edgecolors=WHITE, linewidth=1.2)
        y_positions[dname] = (y_pos, y_pos + 0.3 * (n - 1), col)
        # Domain label
        ax.text(-2.8, (ys[0] + ys[-1]) / 2, dname, color=col, fontsize=10,
                fontweight='bold', ha='right', va='center')
        y_pos += 0.3 * n + 0.8

# Vertical reference lines
for ref_val, ref_label in [(-1, '0.1 ppb'), (0, '1 ppb'), (1, '10 ppb'),
                            (2, '100 ppm'), (3, '0.1%'), (4, '1%')]:
    ax.axvline(x=ref_val, color=DIM, linewidth=0.6, linestyle=':', alpha=0.4)
    ax.text(ref_val, y_pos + 0.3, ref_label, color=DIM, fontsize=7, ha='center')

# Precision bands
ax.axvspan(-2.5, 0.5, alpha=0.04, color=GOLD)
ax.text(-1.0, y_pos + 0.8, 'Sub-ppb', color=GOLD, fontsize=9, ha='center')
ax.axvspan(0.5, 3.0, alpha=0.03, color=GREEN)
ax.text(1.75, y_pos + 0.8, 'Sub-permille', color=GREEN, fontsize=9, ha='center')

style_ax(ax, title='Precision Landscape: 53 Derived Values Across Eight Domains',
         xlabel=r'log$_{10}$(miss) — lower is more precise')
ax.set_xlim(-3, 5.5)
ax.set_ylim(-0.5, y_pos + 1.5)
ax.set_yticks([])

save(fig, 'book_13_precision_landscape.png')


# ================================================================
# FIG 14: GAP RATIO — SM vs MSSM vs CD
# Type: Type 6 (Comparison Bar)
# Shows: Log-scale bars — CD 218x better than SM, 19x better than MSSM
# ================================================================

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor(BG)

models = ['Standard Model', 'MSSM\n(Supersymmetry)', 'Cabibbo Doublet']
gaps = [5.884, 0.5, 0.0269]
colors_bar = [RED, PURPLE, GOLD]
descriptions = ['Gap = 5.88\n13% of coupling', 'Gap ' + r'$\approx$' + ' 0.5\n~1% of coupling',
                'Gap = 0.027\n0.064% of coupling']

bars = ax.barh(range(3), gaps, color=colors_bar, alpha=0.75,
               edgecolor=colors_bar, linewidth=2, height=0.5)

ax.set_xscale('log')
ax.set_xlim(0.005, 20)

# Labels on bars
for i, (model, gap, desc) in enumerate(zip(models, gaps, descriptions)):
    if gap > 1:
        ax.text(gap * 0.35, i, '%.2f' % gap, color=WHITE, fontsize=16,
                fontweight='bold', ha='center', va='center')
    else:
        ax.text(gap * 4, i, '%.4f' % gap if gap < 0.1 else '%.1f' % gap,
                color=colors_bar[i], fontsize=14, fontweight='bold', ha='left', va='center')

# Model names on y-axis
ax.set_yticks(range(3))
ax.set_yticklabels(models, fontsize=11, color=WHITE)

# Improvement arrows
ax.annotate('218' + r'$\times$', xy=(0.15, 2.65), xytext=(0.15, 2.65),
            color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.annotate('', xy=(5.884, 2.45), xytext=(0.0269, 2.45),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2.5))

ax.annotate('19' + r'$\times$', xy=(0.12, 1.65), xytext=(0.12, 1.65),
            color=GOLD, fontsize=13, fontweight='bold', ha='center')
ax.annotate('', xy=(0.5, 1.45), xytext=(0.0269, 1.45),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.8))

# Exact unification reference
ax.axvline(x=0.01, color=GREEN, linewidth=1.2, linestyle=':', alpha=0.5)
ax.text(0.008, 2.8, 'Exact\nunification', color=GREEN, fontsize=8, ha='center', alpha=0.7)

# New parameters comparison
ax.text(8, 2, '3 new\nparameters', color=GOLD, fontsize=9, ha='center')
ax.text(8, 1, '105 new\nparameters', color=PURPLE, fontsize=9, ha='center')
ax.text(8, 0, '0 new\nparameters', color=RED, fontsize=9, ha='center')

style_ax(ax, title=r'Unification Gap at Two-Loop Crossing ($\alpha_2^{-1} - \alpha_3^{-1}$)',
         xlabel='Gap (smaller = better unification)')
ax.set_ylim(-0.7, 3.3)

save(fig, 'book_14_gap_comparison.png')


# ================================================================
# FIG 15: k₁ BUG CASCADE — WRONG vs RIGHT
# Type: Type 7 (Progression/Sequence)
# Shows: One inverted Fraction cascading to 42 orders of magnitude error
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

stages = [
    (r'$k_1$', 'Normalization\nfactor'),
    (r'$\alpha_1^{-1}(M_Z)$', 'U(1) coupling\nat low energy'),
    (r'$M_{GUT}$', 'Unification\nscale'),
    (r'$\alpha_s$', 'Strong coupling\nprediction'),
]

wrong_vals = ['5/3', '175.6', r'$10^{56}$ GeV', 'negative']
right_vals = ['3/5', '63.2', r'$10^{13.8}$ GeV', '0.066']
ratios = [r'$(5/3)^2$' + '\n= 2.78' + r'$\times$',
          '2.78' + r'$\times$',
          r'$10^{42}$' + ' too high',
          r'non-physical $\rightarrow$' + '\nphysical']

x_positions = [2.5, 6.5, 10.5, 14.5]

# Title
ax.text(9, 9.5, r'The $k_1$ Bug: One Inverted Fraction $\rightarrow$ 42 Orders of Magnitude',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

# WRONG row
ax.text(0.3, 7.5, 'WRONG', color=RED, fontsize=13, fontweight='bold', va='center')
for i, (x, (stage, desc), val) in enumerate(zip(x_positions, stages, wrong_vals)):
    box = FancyBboxPatch((x - 1.5, 6.7), 3.0, 1.6, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=RED, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x, 7.8, stage, color=RED, fontsize=11, ha='center', va='center')
    ax.text(x, 7.2, val, color=WHITE, fontsize=13, fontweight='bold', ha='center', va='center')
    if i < len(stages) - 1:
        ax.annotate('', xy=(x_positions[i + 1] - 1.5, 7.5),
                    xytext=(x + 1.5, 7.5),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# RIGHT row
ax.text(0.3, 4.5, 'RIGHT', color=GREEN, fontsize=13, fontweight='bold', va='center')
for i, (x, (stage, desc), val) in enumerate(zip(x_positions, stages, right_vals)):
    box = FancyBboxPatch((x - 1.5, 3.7), 3.0, 1.6, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=GREEN, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x, 4.8, stage, color=GREEN, fontsize=11, ha='center', va='center')
    ax.text(x, 4.2, val, color=WHITE, fontsize=13, fontweight='bold', ha='center', va='center')
    if i < len(stages) - 1:
        ax.annotate('', xy=(x_positions[i + 1] - 1.5, 4.5),
                    xytext=(x + 1.5, 4.5),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

# Ratio labels between rows
for i, (x, ratio) in enumerate(zip(x_positions, ratios)):
    ax.text(x, 6.0, ratio, color=ORANGE, fontsize=9, ha='center', va='center', fontweight='bold')
    ax.annotate('', xy=(x, 6.6), xytext=(x, 5.4),
                arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1.2, alpha=0.6))

# Stage descriptions
for x, (stage, desc) in zip(x_positions, stages):
    ax.text(x, 3.2, desc, color=DIM, fontsize=7, ha='center')

# Discovery note
ax.text(9, 1.3, 'Found by DATA-6 automatic comparison engine:\n'
        'Run 001 (both wrong) ' + r'$\rightarrow$' +
        ' Run 002 (CD fixed, SM wrong) ' + r'$\rightarrow$' +
        ' Run 003 (both fixed, ALL PASS)',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=DIM))

save(fig, 'book_15_k1_bug.png')


# ================================================================
# FIG 16: FRACTION vs DECIMAL — STRUCTURE VISIBILITY
# Type: Type 5 (Connection/Integer Map)
# Shows: Same numbers in decimal (meaningless) vs Fraction (structured)
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10), gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

# LEFT PANEL: Decimal view — three anonymous numbers on a line
ax1.set_facecolor(BG)
ax1.axis('off')
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 10)

ax1.text(4, 9.5, 'DECIMAL VIEW', color=RED, fontsize=16, fontweight='bold', ha='center')
ax1.text(4, 8.7, 'Three numbers on a line', color=SILVER, fontsize=11, ha='center')

# Number line
ax1.plot([1, 7], [6, 6], color=DIM, linewidth=2)
# Tick marks
decimal_vals = [('4.100', 4.3), ('-3.167', 2.2), ('-7.000', 1.0)]
# Map to positions on the line
positions = [5.8, 3.0, 1.3]

for (label, _), pos in zip(decimal_vals, positions):
    ax1.plot([pos, pos], [5.7, 6.3], color=RED, linewidth=2)
    ax1.scatter([pos], [6], color=RED, s=150, zorder=5, edgecolors=WHITE, linewidth=1.5)
    ax1.text(pos, 5.0, label, color=RED, fontsize=14, fontweight='bold', ha='center')

ax1.text(4, 3.5, 'What do these numbers mean?', color=SILVER, fontsize=12, ha='center')
ax1.text(4, 2.8, 'Nothing visible.', color=RED, fontsize=14, fontweight='bold', ha='center')
ax1.text(4, 2.0, 'Three anonymous points.\nNo structure. No physics.\nNo connection to each other.',
         color=DIM, fontsize=9, ha='center')

# RIGHT PANEL: Fraction view — structured, labeled
ax2.set_facecolor(BG)
ax2.axis('off')
ax2.set_xlim(0, 8)
ax2.set_ylim(0, 10)

ax2.text(4, 9.5, 'FRACTION VIEW', color=GREEN, fontsize=16, fontweight='bold', ha='center')
ax2.text(4, 8.7, 'Three Fractions with meaning', color=SILVER, fontsize=11, ha='center')

fractions = [
    (r'$b_1 = \frac{41}{10}$', '41 counts U(1)\ncharge contributions', '10 = GUT\nnormalization',
     BLUE, 7.5),
    (r'$b_2 = -\frac{19}{6}$', '19 counts SU(2)\nparticles - gauge bosons', '6 = SU(2)\nnormalization',
     GREEN, 5.5),
    (r'$b_3 = -\frac{7}{1}$', '7 = 11(Yang-Mills)\n- 4(fermions)', '1 = no\nnormalization',
     RED, 3.5),
]

for frac_label, num_meaning, den_meaning, col, y in fractions:
    # Main fraction
    box = FancyBboxPatch((0.5, y - 0.7), 3.0, 1.4, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=2)
    ax2.add_patch(box)
    ax2.text(2.0, y, frac_label, color=col, fontsize=16, fontweight='bold',
             ha='center', va='center')
    # Numerator meaning
    ax2.text(5.5, y + 0.3, num_meaning, color=SILVER, fontsize=8, ha='center', va='center')
    # Denominator meaning
    ax2.text(5.5, y - 0.3, den_meaning, color=DIM, fontsize=8, ha='center', va='center')
    # Arrow from fraction to meaning
    ax2.annotate('', xy=(4.2, y), xytext=(3.5, y),
                 arrowprops=dict(arrowstyle='->', color=col, lw=1.5))

ax2.text(4, 1.5, 'Every integer has a meaning.\nThe physics is in the Fractions.',
         color=GREEN, fontsize=11, fontweight='bold', ha='center')

fig.suptitle('The Same Three Numbers: Structure Hidden vs Structure Visible',
             color=WHITE, fontsize=17, fontweight='bold', y=0.97)

save(fig, 'book_16_fraction_structure.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "=" * 60)
print("BOOK DIAGRAMS (SET 2) COMPLETE")
print("=" * 60)
fnames = [
    'book_09_flat_curved.png',
    'book_10_bessel_zeros.png',
    'book_11_alpha_scaling.png',
    'book_12_hydrogen_two_path.png',
    'book_13_precision_landscape.png',
    'book_14_gap_comparison.png',
    'book_15_k1_bug.png',
    'book_16_fraction_structure.png',
]
for i, fn in enumerate(fnames):
    print("  Fig %d: %s" % (i + 9, fn))
print("=" * 60)
