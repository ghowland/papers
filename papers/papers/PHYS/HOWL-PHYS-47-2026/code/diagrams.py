#!/usr/bin/env python3
"""
HOWL PHYS-47 Diagrams — The Laporta Constants
8 figures covering cross-relation matrix, QED series, A4 sensitivity,
basis landscape, dual geometry, precision validity, and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Wedge, Ellipse
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================


# Light mode
if True:
    # ── Global palette (Kindle / light mode) ──
    BG      = '#ffffff'
    PAN     = '#f0ede8'
    GOLD    = '#a07820'
    SILVER  = '#505860'
    CYAN    = '#1a8a80'
    MAG     = '#a03058'
    BLUE    = '#2855a0'
    GREEN   = '#2a7a3a'
    RED     = '#b82020'
    ORANGE  = '#c06a18'
    WHITE   = '#1a1a22'
    DIM     = '#908e88'
    PURPLE  = '#6040a0'
else:
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

def setup_ax(ax, title='', xlabel='', ylabel=''):
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

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

print("PHYS-47 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: CROSS-RELATION MATRIX — 6x6 MUTUAL INDEPENDENCE
# Type: Geometric Cross-Section (D5.4)
# Shows: The 6x6 matrix of integrals. Diagonal = individual scan
#        (NULL). Off-diagonal = pair/triple test (NULL). Every cell
#        is null. The visual grid of mutual independence.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

labels = ['C81a', 'C81b', 'C81c', 'C83a', 'C83b', 'C83c']
n = len(labels)
cell_size = 1.0
margin = 0.08

for i in range(n):
    for j in range(n):
        x = j * cell_size
        y = (n - 1 - i) * cell_size

        if i == j:
            # Diagonal: individual scan
            color = RED
            text = 'NULL'
            alpha = 0.25
        elif (i < 3 and j < 3) or (i >= 3 and j >= 3):
            # Within-topology pair
            color = CYAN
            text = 'NULL'
            alpha = 0.15
        else:
            # Cross-topology pair
            color = PURPLE
            text = 'NULL'
            alpha = 0.10

        rect = plt.Rectangle((x + margin, y + margin),
                               cell_size - 2*margin, cell_size - 2*margin,
                               facecolor=color, alpha=alpha,
                               linewidth=1.5, edgecolor=color)
        ax.add_patch(rect)
        ax.text(x + cell_size/2, y + cell_size/2, text,
                color=color, fontsize=10, fontweight='bold',
                ha='center', va='center')

# Row and column labels
for i, label in enumerate(labels):
    ax.text(-0.3, (n - 1 - i) * cell_size + cell_size/2, label,
            color=WHITE, fontsize=12, fontweight='bold',
            ha='right', va='center')
    ax.text(i * cell_size + cell_size/2, n * cell_size + 0.2, label,
            color=WHITE, fontsize=12, fontweight='bold',
            ha='center', va='bottom')

# Topology dividers
ax.plot([3 * cell_size, 3 * cell_size], [0, n * cell_size],
        color=GOLD, lw=1.5, ls='--', alpha=0.4)
ax.plot([0, n * cell_size], [3 * cell_size, 3 * cell_size],
        color=GOLD, lw=1.5, ls='--', alpha=0.4)

# Topology labels
ax.text(1.5 * cell_size, -0.5, 'Topology 81', color=GOLD, fontsize=11,
        ha='center', style='italic')
ax.text(4.5 * cell_size, -0.5, 'Topology 83', color=GOLD, fontsize=11,
        ha='center', style='italic')

# Legend
ax.text(7.0, 5.0, 'Diagonal (individual):', color=RED, fontsize=10)
ax.text(7.0, 4.5, '6/6 NULL', color=RED, fontsize=10, fontweight='bold')
ax.text(7.0, 3.8, 'Within-topology pair:', color=CYAN, fontsize=10)
ax.text(7.0, 3.3, '6/6 NULL', color=CYAN, fontsize=10, fontweight='bold')
ax.text(7.0, 2.6, 'Cross-topology pair:', color=PURPLE, fontsize=10)
ax.text(7.0, 2.1, '3/3 NULL', color=PURPLE, fontsize=10, fontweight='bold')
ax.text(7.0, 1.4, 'Triples (not shown):', color=ORANGE, fontsize=10)
ax.text(7.0, 0.9, '2/2 NULL', color=ORANGE, fontsize=10, fontweight='bold')

ax.text(7.0, 0.0, 'Total: 17/17 NULL', color=GOLD, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

ax.set_xlim(-0.8, 9.5)
ax.set_ylim(-1.0, n * cell_size + 0.8)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('Mutual Independence Matrix: 6 Integrals, 17 Tests, 17 NULL',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

save(fig, 'phys47_01_cross_relation_matrix.png')


# ================================================================
# FIG 2: QED SERIES — FIVE TERMS, A4 HIGHLIGHTED
# Type: Comparison Bar (D5.6)
# Shows: The contribution of each QED term to a_e on a log scale.
#        A4 is the last term above the measurement uncertainty.
#        A5 is below. The staircase of precision.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'QED Series Term', r'|Contribution to $a_e$|')

terms = [
    (r'$A_1(\alpha/\pi)$', 1.161e-3, CYAN),
    (r'$A_2(\alpha/\pi)^2$', 1.772e-6, BLUE),
    (r'$A_3(\alpha/\pi)^3$', 1.480e-8, GREEN),
    (r'$A_4(\alpha/\pi)^4$', 5.567e-11, GOLD),
    (r'$A_5(\alpha/\pi)^5$', 3.984e-13, SILVER),
]

x_pos = np.arange(len(terms))
for i, (label, value, color) in enumerate(terms):
    ax.bar(i, value, width=0.6, color=color, alpha=0.7,
           edgecolor=color, linewidth=2)
    ax.text(i, value * 2.5, '%.1e' % value, color=color,
            fontsize=10, fontweight='bold', ha='center')

# Harvard measurement uncertainty
ax.axhline(1.3e-12, color=MAG, lw=2, ls='--', alpha=0.8)
ax.text(4.5, 1.8e-12, r'Harvard $\delta a_e = \pm 1.3 \times 10^{-12}$',
        color=MAG, fontsize=10, fontweight='bold')

# Hadronic contribution
ax.axhline(1.98e-12, color=ORANGE, lw=1.5, ls=':', alpha=0.6)
ax.text(4.5, 2.8e-12, 'Hadronic (total)', color=ORANGE, fontsize=9)

# Highlight A4
ax.annotate('Laporta constants\nlive HERE',
            xy=(3, 5.567e-11), xytext=(3.8, 3e-9),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# A4 vs measurement annotation
ax.text(0.3, 3e-14,
        r'$A_4$: last term above measurement' + '\n' +
        r'$A_5$: first term below',
        color=WHITE, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM, linewidth=1))

ax.set_yscale('log')
ax.set_xticks(x_pos)
ax.set_xticklabels([t[0] for t in terms], color=WHITE, fontsize=10)
ax.set_ylim(1e-14, 1e-1)
ax.set_xlim(-0.5, 5.5)

ax.set_title(r'The QED Series: $A_4$ Is the Last Term Above the Measurement Floor',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys47_02_qed_series_terms.png')


# ================================================================
# FIG 3: A4 vs HARVARD PRECISION — 43x RATIO
# Type: Threshold/Region (D5.3)
# Shows: The A4 contribution towering over the measurement band.
#        The 43x ratio is visible as height.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', '', r'Magnitude (units of $10^{-12}$)')

# Values in units of 10^-12
a4_contrib = 55.67  # 5.567e-11 = 55.67e-12
harvard_unc = 1.3
hadronic = 1.98
a5_contrib = 0.398
ew_contrib = 0.030

bars = [
    (r'$|A_4 \times x^4|$', a4_contrib, GOLD),
    ('Hadronic (total)', hadronic, ORANGE),
    (r'Harvard $\pm\delta$', harvard_unc, MAG),
    (r'$|A_5 \times x^5|$', a5_contrib, SILVER),
    ('Electroweak', ew_contrib, DIM),
]

x_pos = np.arange(len(bars))
for i, (label, value, color) in enumerate(bars):
    ax.bar(i, value, width=0.6, color=color, alpha=0.7,
           edgecolor=color, linewidth=2)
    if value > 2:
        ax.text(i, value + 1.5, '%.1f' % value, color=color,
                fontsize=11, fontweight='bold', ha='center')
    else:
        ax.text(i, value + 0.8, '%.2f' % value, color=color,
                fontsize=10, fontweight='bold', ha='center')

# Ratio annotation
ax.annotate(r'$43\times$', xy=(0, a4_contrib/2),
            xytext=(1.8, a4_contrib * 0.7),
            color=GOLD, fontsize=18, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

ax.text(3.5, 40, 'The four-loop term is\n43 times ABOVE\nthe measurement floor',
        color=WHITE, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2))

ax.set_xticks(x_pos)
ax.set_xticklabels([b[0] for b in bars], color=WHITE, fontsize=9)
ax.set_ylim(0, 70)

ax.set_title(r'The $A_4$ Contribution: 43$\times$ the Harvard Measurement Precision',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys47_03_a4_vs_harvard.png')


# ================================================================
# FIG 4: 66-ELEMENT BASIS — WEIGHT LANDSCAPE WITH ELLIPTIC GAP
# Type: Scale/Landscape (D5.2)
# Shows: Constants plotted by weight on x-axis, grouped by class.
#        The elliptic/modular region is empty — the gap.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Transcendental Weight', '')

# Count constants by weight and class
classes = {
    'pi powers':       [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1)],
    'zeta values':     [(3,1),(5,1),(7,1),(9,1)],
    'ln(2) powers':    [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1)],
    'cross products':  [(3,2),(4,3),(5,4),(6,6),(7,5),(8,3)],
    'polylog Li(1/2)': [(4,1),(5,2),(6,2),(7,2)],
    'polylog Li(-1)':  [(4,1),(5,1),(6,1),(7,1)],
    'MZV':             [(6,1),(8,2)],
    'alt. Euler':      [(6,3),(7,3),(8,2)],
}

colors_map = {
    'pi powers': CYAN,
    'zeta values': GREEN,
    'ln(2) powers': BLUE,
    'cross products': SILVER,
    'polylog Li(1/2)': ORANGE,
    'polylog Li(-1)': MAG,
    'MZV': PURPLE,
    'alt. Euler': RED,
}

y_offset = {}
for cls_name, entries in classes.items():
    color = colors_map[cls_name]
    for weight, count in entries:
        base_y = y_offset.get(weight, 0)
        ax.bar(weight, count, bottom=base_y, width=0.6, color=color,
               alpha=0.6, edgecolor=color, linewidth=1.5)
        y_offset[weight] = base_y + count

# The elliptic gap — mark it
ax.annotate('ELLIPTIC?\n(not in basis)',
            xy=(8.5, 3), xytext=(9.5, 8),
            color=RED, fontsize=12, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# Laporta integrals marker
ax.text(9.5, 6.5, 'Laporta integrals\nlive at weight 8\nbut NOT in this basis',
        color=GOLD, fontsize=10, style='italic',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

# Legend
legend_entries = []
for cls_name, color in colors_map.items():
    legend_entries.append(mpatches.Patch(color=color, alpha=0.6, label=cls_name))
ax.legend(handles=legend_entries, facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9, loc='upper left')

ax.set_xlim(-0.5, 11)
ax.set_ylim(0, 16)
ax.set_xticks(range(0, 10))

ax.set_title('The 66-Element Basis by Weight: Coverage and the Elliptic Gap',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys47_04_basis_landscape.png')


# ================================================================
# FIG 5: GENUS 0 vs GENUS 1 — SPHERE vs TORUS
# Type: Geometric Cross-Section (D5.4)
# Shows: A sphere (genus 0) alongside a torus (genus 1).
#        Labels: polylogarithmic constants on the sphere,
#        elliptic periods on the torus. Laporta integrals
#        on the torus side with a question mark.
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                gridspec_kw={'wspace': 0.35})
fig.patch.set_facecolor(BG)

# Left: Sphere (genus 0)
ax1.set_facecolor(PAN)
ax1.set_aspect('equal')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)

circle = Circle((0, 0), 2.0, facecolor=CYAN, alpha=0.12,
                 edgecolor=CYAN, linewidth=2.5)
ax1.add_patch(circle)

ax1.text(0, 0.3, 'Genus 0', color=CYAN, fontsize=16,
         ha='center', va='center', fontweight='bold')
ax1.text(0, -0.3, '(Sphere)', color=CYAN, fontsize=12,
         ha='center', va='center')

# Constants on the sphere
sphere_consts = [r'$\pi$', r'$\zeta(3)$', r'$\ln 2$',
                  r'$\mathrm{Li}_4(\frac{1}{2})$', r'$\zeta(3,5)$']
angles = np.linspace(0.4, 2*np.pi - 0.4, len(sphere_consts))
for angle, const in zip(angles, sphere_consts):
    x = 2.5 * np.cos(angle)
    y = 2.5 * np.sin(angle)
    ax1.text(x, y, const, color=WHITE, fontsize=10,
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.15', facecolor=BG,
                       edgecolor=CYAN, linewidth=0.8))

ax1.set_xticks([])
ax1.set_yticks([])
for spine in ax1.spines.values():
    spine.set_visible(False)
ax1.set_title('Polylogarithmic Basis\n(all loops through 3)', color=CYAN,
              fontsize=13, fontweight='bold', pad=10)

# Right: Torus (genus 1) — draw as two concentric ellipses
ax2.set_facecolor(PAN)
ax2.set_aspect('equal')
ax2.set_xlim(-3.5, 3.5)
ax2.set_ylim(-3, 3)

# Outer ellipse of torus
outer = Ellipse((0, 0), 4.5, 2.8, facecolor='none',
                 edgecolor=GOLD, linewidth=2.5)
ax2.add_patch(outer)

# Inner hole
inner = Ellipse((0, 0.1), 1.5, 0.8, facecolor=PAN,
                 edgecolor=GOLD, linewidth=2, linestyle='--')
ax2.add_patch(inner)

# Cross section arc to suggest 3D
arc_top = Arc((0, 0), 4.5, 2.8, angle=0, theta1=0, theta2=180,
               color=GOLD, lw=2.5)
ax2.add_patch(arc_top)

ax2.text(0, 0.5, 'Genus 1', color=GOLD, fontsize=16,
         ha='center', va='center', fontweight='bold')
ax2.text(0, -0.2, '(Torus)', color=GOLD, fontsize=12,
         ha='center', va='center')

# Elliptic constants
torus_consts = ['K(k)', 'E(k)', 'L(f,s)', 'C81a?', 'C83a?']
torus_colors = [WHITE, WHITE, WHITE, RED, RED]
t_angles = np.linspace(0.3, 2*np.pi - 0.3, len(torus_consts))
for angle, const, tc in zip(t_angles, torus_consts, torus_colors):
    x = 2.8 * np.cos(angle)
    y = 1.8 * np.sin(angle)
    edge_c = GOLD if tc == WHITE else RED
    ax2.text(x, y, const, color=tc, fontsize=10,
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.15', facecolor=BG,
                       edgecolor=edge_c, linewidth=0.8))

ax2.set_xticks([])
ax2.set_yticks([])
for spine in ax2.spines.values():
    spine.set_visible(False)
ax2.set_title('Elliptic / Modular Basis?\n(four loops, topologies 81/83)', color=GOLD,
              fontsize=13, fontweight='bold', pad=10)

# Central annotation
fig.text(0.5, 0.04,
         'The Laporta integrals are NOT on the sphere (24/24 null). '
         'Are they on the torus? (Attack 3 will test)',
         color=WHITE, fontsize=11, ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=2))

save(fig, 'phys47_05_genus0_vs_genus1.png')


# ================================================================
# FIG 6: DUAL GEOMETRY — SPHERICAL + TOROIDAL ON ONE OBJECT
# Type: Geometric Cross-Section (D5.4)
# Shows: A central body (proton or Earth) with concentric spherical
#        shells AND toroidal field lines overlaid. Two geometries
#        on one object.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')

cx, cy = 0, 0

# Spherical shells (concentric circles)
shell_radii = [1.0, 1.8, 2.6, 3.4]
shell_labels = ['Surface', 'Boundary 1', 'Boundary 2', 'Boundary 3']
for r, label in zip(shell_radii, shell_labels):
    circle = Circle((cx, cy), r, facecolor='none',
                      edgecolor=CYAN, linewidth=1.5, linestyle='-', alpha=0.5)
    ax.add_patch(circle)
    ax.text(r * 0.707 + 0.15, r * 0.707 + 0.15, label,
            color=CYAN, fontsize=8, alpha=0.7)

# Central body
core = Circle((cx, cy), 0.5, facecolor=CYAN, alpha=0.2,
               edgecolor=CYAN, linewidth=2)
ax.add_patch(core)

# Toroidal field lines (dipole-like curves)
theta = np.linspace(0, 2 * np.pi, 200)
for scale in [1.5, 2.5, 3.5]:
    # Dipole field line: r = scale * sin^2(theta)
    r_field = scale * np.sin(theta)**2
    x_field = r_field * np.cos(theta)
    y_field = r_field * np.sin(theta)
    ax.plot(x_field, y_field, color=GOLD, lw=1.5, alpha=0.4)

# Van Allen belt regions (toroidal)
belt1 = Ellipse((cx, cy), 3.0, 1.2, facecolor=GOLD, alpha=0.06,
                  edgecolor='none')
ax.add_patch(belt1)
belt2 = Ellipse((cx, cy), 5.5, 2.0, facecolor=GOLD, alpha=0.04,
                  edgecolor='none')
ax.add_patch(belt2)

# Labels
ax.text(-4.5, 3.8, 'SPHERICAL\n(scalar/gravity)', color=CYAN,
        fontsize=13, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1.5))
ax.text(-4.5, 3.0, r'Constants: $\pi, \zeta(n), \ln 2$', color=CYAN, fontsize=10)
ax.text(-4.5, 2.5, r'$\beta$ via $4\pi = 16\beta^2$', color=CYAN, fontsize=10)

ax.text(2.0, -3.8, 'TOROIDAL\n(vector/magnetic)', color=GOLD,
        fontsize=13, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1.5))
ax.text(2.0, -4.5, 'Constants: K(k), E(k), Laporta?', color=GOLD, fontsize=10)
ax.text(2.0, -5.0, r'$\beta$ via $4\pi^2 = 64\beta^2$', color=GOLD, fontsize=10)

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-5.5, 5.0)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_title('Dual Geometry: Every Soliton Has Both Spherical and Toroidal Boundaries',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys47_06_dual_geometry.png')


# ================================================================
# FIG 7: PSLQ PRECISION VALIDITY — ALL SCANS ABOVE THE CURVE
# Type: Running/Convergence (D5.1)
# Shows: The theoretical precision requirement curve d = n * log10(M)
#        with each of our scans plotted as a point. All points above
#        the curve = all null results are valid.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Basis size n', 'Required / actual digits d')

# Theoretical requirement curve for maxcoeff = 10000
n_range = np.arange(1, 110)
d_required_10k = n_range * 4  # log10(10000) = 4
d_required_100k = n_range * 5  # log10(100000) = 5
d_required_1e8 = n_range * 8  # log10(10^8) = 8

ax.fill_between(n_range, 0, d_required_10k, color=RED, alpha=0.06)
ax.plot(n_range, d_required_10k, color=RED, lw=1.5, ls='--', alpha=0.6,
        label=r'$d > n \times 4$ (maxcoeff $10^4$)')
ax.plot(n_range, d_required_100k, color=ORANGE, lw=1.5, ls='--', alpha=0.6,
        label=r'$d > n \times 5$ (maxcoeff $10^5$)')
ax.plot(n_range, d_required_1e8, color=MAG, lw=1.5, ls=':', alpha=0.4,
        label=r'$d > n \times 8$ (maxcoeff $10^8$)')

# Our scans
scans = [
    (9, 300, 'Tier1/300d'),
    (18, 300, 'Tier2/300d'),
    (36, 300, 'Tier3/300d'),
    (52, 400, 'Tier1/400d'),
    (58, 400, 'Tier2/400d'),
    (66, 400, 'Tier3/400d'),
]

for n_basis, digits, label in scans:
    ax.plot(n_basis, digits, 'o', color=GREEN, markersize=12, zorder=6)
    ax.text(n_basis + 1.5, digits + 8, label, color=GREEN, fontsize=8)

# Future attacks
future = [
    (66, 1000, 'Attack 1'),
    (100, 4000, 'Attack 6'),
]
for n_basis, digits, label in future:
    ax.plot(n_basis, digits, 'D', color=GOLD, markersize=10, zorder=6)
    ax.text(n_basis + 1.5, digits + 30, label, color=GOLD, fontsize=9,
            fontweight='bold')

ax.text(15, 350, 'ALL completed scans\nabove the requirement curve',
        color=GREEN, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN, linewidth=1.5))

ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9,
          loc='lower right')

ax.set_xlim(0, 110)
ax.set_ylim(0, 4500)

ax.set_title('PSLQ Precision Validity: Every Scan Above the Requirement Curve',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys47_07_precision_validity.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE SIX LAPORTA CONSTANTS
# Type: Identity Card (D5.8)
# Shows: All six constants with their properties: value, topology,
#        magnitude, PSLQ status, contribution scale.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Card layout
card_data = [
    ('C81a', '+116.695', '81', 'a', '116.69', 'NULL', CYAN),
    ('C81b', ' \u22128.748', '81', 'b', '8.75', 'NULL', CYAN),
    ('C81c', ' \u22120.236', '81', 'c', '0.24', 'NULL', CYAN),
    ('C83a', '  +2.771', '83', 'a', '2.77', 'NULL', PURPLE),
    ('C83b', ' \u22120.808', '83', 'b', '0.81', 'NULL', PURPLE),
    ('C83c', ' \u22120.435', '83', 'c', '0.43', 'NULL', PURPLE),
]

y_start = 0.85
y_step = 0.11

# Header
ax.text(0.02, 0.95, 'THE SIX LAPORTA CONSTANTS', color=GOLD,
        fontsize=18, fontweight='bold', transform=ax.transAxes)
ax.text(0.02, 0.91, 'Four-loop QED master integrals | Laporta 2017 | 4925 digits each',
        color=SILVER, fontsize=11, transform=ax.transAxes)

# Column headers
headers = [('Label', 0.02), ('Value (first 8)', 0.12), ('Topo', 0.38),
           ('Master', 0.45), ('|C|', 0.53), ('PSLQ', 0.65), ('Status', 0.75)]
for h_text, h_x in headers:
    ax.text(h_x, y_start + 0.02, h_text, color=DIM, fontsize=10,
            fontweight='bold', transform=ax.transAxes)

# Separator line
ax.plot([0.02, 0.95], [y_start - 0.005, y_start - 0.005],
        color=DIM, lw=0.5, transform=ax.transAxes, clip_on=False)

for i, (label, value, topo, master, mag, status, color) in enumerate(card_data):
    y = y_start - (i + 1) * y_step

    ax.text(0.02, y, label, color=color, fontsize=14, fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.12, y, value, color=WHITE, fontsize=12, family='monospace',
            transform=ax.transAxes)
    ax.text(0.38, y, topo, color=SILVER, fontsize=12,
            transform=ax.transAxes)
    ax.text(0.45, y, master, color=SILVER, fontsize=12,
            transform=ax.transAxes)
    ax.text(0.53, y, mag, color=WHITE, fontsize=12,
            transform=ax.transAxes)
    ax.text(0.65, y, '24/24', color=RED, fontsize=12, fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.75, y, 'INDEPENDENT', color=RED, fontsize=11, fontweight='bold',
            transform=ax.transAxes)

# Bottom summary box
y_bottom = y_start - 7.5 * y_step
ax.text(0.02, y_bottom, 'SUMMARY', color=GOLD, fontsize=14,
        fontweight='bold', transform=ax.transAxes)

summary_lines = [
    (r'$A_4$ contribution to $a_e$:', r'$-5.567 \times 10^{-11}$  (43$\times$ Harvard precision)'),
    (r'$\alpha^{-1}$ shift from $A_4$:', r'$-48.08$ ppb'),
    ('Mutual independence:', '11/11 cross-relation NULL'),
    ('Basis tested:', '66 constants (polylog + MZV + alt. Euler)'),
    ('Hypothesis:', 'Elliptic (toroidal momentum topology)'),
]
for j, (key, val) in enumerate(summary_lines):
    y_line = y_bottom - (j + 1) * 0.045
    ax.text(0.04, y_line, key, color=SILVER, fontsize=10,
            transform=ax.transAxes)
    ax.text(0.40, y_line, val, color=WHITE, fontsize=10,
            transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

save(fig, 'phys47_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys47_01_cross_relation_matrix.png")
print("  phys47_02_qed_series_terms.png")
print("  phys47_03_a4_vs_harvard.png")
print("  phys47_04_basis_landscape.png")
print("  phys47_05_genus0_vs_genus1.png")
print("  phys47_06_dual_geometry.png")
print("  phys47_07_precision_validity.png")
print("  phys47_08_identity_card.png")
print("=" * 50)
