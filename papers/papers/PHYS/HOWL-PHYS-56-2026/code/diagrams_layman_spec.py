#!/usr/bin/env python3
"""
HOWL PCTRM Substrate Spec Diagrams — What PCTRM Says Is Going On
8 figures covering the substrate's structural claims.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, Wedge, Arc, Ellipse, FancyArrowPatch
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
    

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)


def style_axes(ax):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    ax.grid(True, color=DIM, alpha=0.15, linewidth=0.5)


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


# ================================================================
# FIG 1: DIRECTION-CONDITIONAL ADJACENCY vs CUBIC LATTICE
# Type: 4 (Geometric cross-section)
# Shows: The topology that makes c-invariance possible and resolves
#        lattice anisotropy — impossible to convey in text.
# ================================================================

def fig1_adjacency():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                    gridspec_kw={'wspace': 0.30})
    fig.patch.set_facecolor(BG)

    # LEFT: Cubic lattice with 6 axis-aligned neighbors
    ax1.set_facecolor(PAN)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Grid
    for x in range(-3, 4):
        ax1.axvline(x, color=DIM, alpha=0.3, linewidth=0.5)
        ax1.axhline(x, color=DIM, alpha=0.3, linewidth=0.5)

    # Central cell
    ax1.add_patch(Circle((0, 0), 0.25, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5))

    # 6 axis-aligned neighbors (showing 4 in 2D; note 6 in 3D)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ax1.add_patch(Circle((dx, dy), 0.2, facecolor=CYAN, edgecolor=WHITE, linewidth=1.5, zorder=4))
        ax1.annotate('', xy=(dx*0.7, dy*0.7), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=CYAN, lw=2))

    # Diagonal direction: staircase artifact
    theta = np.pi / 6  # 30 degrees, an arbitrary direction
    # Show the staircase path to approximate this direction
    staircase_x = [0, 1, 1, 2, 2]
    staircase_y = [0, 0, 0.577, 0.577, 1.155]
    ax1.plot(staircase_x, staircase_y, color=RED, linewidth=2.5, alpha=0.8,
             label='staircase approximation')
    ax1.plot([0, 2.5], [0, 2.5*np.tan(theta)], color=ORANGE, linewidth=1.5,
             linestyle='--', alpha=0.7, label='desired direction')

    ax1.text(0, -2.7, 'CUBIC LATTICE', ha='center', color=WHITE, fontsize=14, fontweight='bold')
    ax1.text(0, -3.0, 'Only axis-aligned neighbors.', ha='center', color=SILVER, fontsize=10)
    ax1.text(0, -3.25, 'Diagonal motion is √2 slower than axial.', ha='center', color=RED, fontsize=10)
    ax1.text(0, -3.5, 'Anisotropy built in. No Lorentz invariance.', ha='center', color=RED, fontsize=10)

    ax1.text(2.8, 2.8, 'staircase\nartifact', color=RED, fontsize=9, ha='center')
    ax1.text(-2.5, 2.5, 'preferred\naxes', color=RED, fontsize=9, ha='center')

    # RIGHT: Direction-conditional adjacency
    ax2.set_facecolor(PAN)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # Central cell
    ax2.add_patch(Circle((0, 0), 0.25, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5))

    # Continuous direction neighbors — arrows radiating at many angles
    n_directions = 16
    for i in range(n_directions):
        angle = 2 * np.pi * i / n_directions
        x = np.cos(angle)
        y = np.sin(angle)
        ax2.add_patch(Circle((x, y), 0.12, facecolor=CYAN, edgecolor=WHITE, linewidth=1, alpha=0.8, zorder=4))
        ax2.annotate('', xy=(x*0.78, y*0.78), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2, alpha=0.7))

    # Dashed unit circle showing all directions are at distance 1
    circle = plt.Circle((0, 0), 1, fill=False, color=GOLD, linewidth=1.5, linestyle='--', alpha=0.6)
    ax2.add_patch(circle)

    # The direction is continuous — arbitrary angle arrow
    theta = np.pi / 6
    ax2.annotate('', xy=(2.5*np.cos(theta), 2.5*np.sin(theta)), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax2.text(2.6*np.cos(theta), 2.6*np.sin(theta) + 0.3,
             'continuous\ndirection', color=GREEN, fontsize=9, ha='left')

    ax2.text(0, -2.7, 'DIRECTION-CONDITIONAL ADJACENCY', ha='center', color=WHITE, fontsize=14, fontweight='bold')
    ax2.text(0, -3.0, 'Position discrete. Direction continuous.', ha='center', color=SILVER, fontsize=10)
    ax2.text(0, -3.25, 'Every neighbor at exactly 1 Planck-length.', ha='center', color=GOLD, fontsize=10)
    ax2.text(0, -3.5, 'Isotropy by construction. c = 1 cell/tick in every direction.', ha='center', color=GREEN, fontsize=10)

    ax2.text(1.3, 1.2, 'all at\ndist = 1', color=GOLD, fontsize=9, ha='center')

    fig.suptitle('The Substrate Topology: Direction-Conditional Unit Adjacency',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    save(fig, 'pctrm_01_direction_conditional_adjacency.png')


# ================================================================
# FIG 2: PHOTON N/N = 1 ARITHMETIC — LORENTZ AS IDENTITY
# Type: 7 (Progression/sequence)
# Shows: c-invariance arises from integer cell count / integer tick count;
#        frame-independence by arithmetic identity, not postulate.
# ================================================================

def fig2_photon_arithmetic():
    fig = plt.figure(figsize=(18, 10))
    fig.patch.set_facecolor(BG)

    gs = fig.add_gridspec(2, 1, height_ratios=[1.2, 1], hspace=0.45)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1])

    # TOP: photon traversing cells 0..N
    ax_top.set_facecolor(PAN)
    N = 10
    ax_top.set_xlim(-0.8, N + 0.8)
    ax_top.set_ylim(-1.2, 1.8)

    # Draw cells along a row
    for i in range(N + 1):
        ax_top.add_patch(Circle((i, 0), 0.22, facecolor=PAN, edgecolor=DIM, linewidth=1, zorder=2))
        ax_top.text(i, -0.55, str(i), color=DIM, fontsize=8, ha='center')

    # Photon trajectory
    photon_x = np.arange(N + 1)
    ax_top.plot(photon_x, np.zeros(N + 1), color=GOLD, linewidth=0.8, alpha=0.3, zorder=1)
    for i in range(N + 1):
        ax_top.add_patch(Circle((i, 0), 0.18, facecolor=GOLD, edgecolor=WHITE, linewidth=1, alpha=0.6, zorder=3))

    # Tick counter above each
    for i in range(N + 1):
        ax_top.text(i, 0.55, "t=%d" % i, color=CYAN, fontsize=8, ha='center')

    # A and B labels
    ax_top.annotate('A\nemission\n(cell 0, tick 0)',
                    xy=(0, -0.25), xytext=(0, -1.0),
                    color=GREEN, fontsize=10, ha='center',
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))
    ax_top.annotate('B\nabsorption\n(cell %d, tick %d)' % (N, N),
                    xy=(N, -0.25), xytext=(N, -1.0),
                    color=RED, fontsize=10, ha='center',
                    arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

    ax_top.text(N/2, 1.3, "Photon advances exactly one cell per tick.",
                color=WHITE, fontsize=11, ha='center', fontweight='bold')
    ax_top.text(N/2, 0.95, "N cells traversed in N ticks.",
                color=GOLD, fontsize=10, ha='center')

    ax_top.axis('off')

    # BOTTOM: Two observers, different frames, same arithmetic
    ax_bot.set_facecolor(PAN)
    ax_bot.set_xlim(0, 10)
    ax_bot.set_ylim(0, 4)
    ax_bot.axis('off')

    # Observer 1 (rest frame)
    ax_bot.add_patch(FancyBboxPatch((0.3, 1.0), 4.4, 2.5,
                                      boxstyle='round,pad=0.15',
                                      facecolor=BG, edgecolor=CYAN, linewidth=2))
    ax_bot.text(2.5, 3.2, 'Observer 1 (rest frame)', color=CYAN, fontsize=12,
                fontweight='bold', ha='center')
    ax_bot.text(2.5, 2.7, 'counts:', color=SILVER, fontsize=10, ha='center')
    ax_bot.text(2.5, 2.2, 'N = 10 cells', color=WHITE, fontsize=11, ha='center')
    ax_bot.text(2.5, 1.75, 'over N = 10 ticks', color=WHITE, fontsize=11, ha='center')
    ax_bot.text(2.5, 1.25, 'speed = N/N = 1 cell/tick = c',
                color=GOLD, fontsize=12, ha='center', fontweight='bold')

    # Observer 2 (boosted frame)
    ax_bot.add_patch(FancyBboxPatch((5.3, 1.0), 4.4, 2.5,
                                      boxstyle='round,pad=0.15',
                                      facecolor=BG, edgecolor=MAG, linewidth=2))
    ax_bot.text(7.5, 3.2, 'Observer 2 (boosted frame)', color=MAG, fontsize=12,
                fontweight='bold', ha='center')
    ax_bot.text(7.5, 2.7, 'counts:', color=SILVER, fontsize=10, ha='center')
    ax_bot.text(7.5, 2.2, "N' cells", color=WHITE, fontsize=11, ha='center')
    ax_bot.text(7.5, 1.75, "over N' ticks", color=WHITE, fontsize=11, ha='center')
    ax_bot.text(7.5, 1.25, "speed = N'/N' = 1 cell/tick = c",
                color=GOLD, fontsize=12, ha='center', fontweight='bold')

    # Central conclusion
    ax_bot.text(5, 0.4, 'c-invariance is an arithmetic identity, not a postulate.  N/N = 1 in any frame.',
                color=GOLD, fontsize=12, ha='center', fontweight='bold', style='italic')

    fig.suptitle('Photon Propagation: Lorentz Invariance as N/N = 1',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    save(fig, 'pctrm_02_photon_nn_arithmetic.png')


# ================================================================
# FIG 3: SIX-LEVEL SOLITON HIERARCHY WITH SCALES
# Type: 2 (Scale/landscape)
# Shows: The 45+ orders of magnitude and the loop-closure of
#        Level 12 back to Level 0 via CMB-as-substrate.
# ================================================================

def fig3_hierarchy():
    fig, ax = plt.subplots(figsize=(16, 11))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    # Log-scale y-axis
    scales = [
        ('Planck cell',       -35,  'Level 0 substrate',    GOLD),
        ('quark / lepton',    -18,  'Level 0',              PURPLE),
        ('nucleon',           -15,  'Level 1',              MAG),
        ('nucleus',           -15,  'Level 2',              MAG),
        ('atom',              -10,  'Level 3',              BLUE),
        ('molecule',           -9,  'Level 4',              CYAN),
        ('macroscopic object', -1,  'Level 5',              GREEN),
        ('planet',              7,  'Level 5',              GREEN),
        ('star',                9,  'Level 5',              ORANGE),
        ('stellar system',     12,  'Level 5',              ORANGE),
        ('galaxy',             21,  'Level 5',              RED),
        ('galaxy cluster',     23,  'Level 5',              RED),
        ('supercluster',       24,  'Level 5',              PURPLE),
        ('observable universe', 27, 'Level 6 universal soliton', GOLD),
    ]

    ax.set_xlim(-2, 14)
    ax.set_ylim(-38, 30)

    # Vertical axis showing log-scale
    ax.axvline(3, color=DIM, linewidth=1, alpha=0.5)

    # PCTRM test levels highlighted in gold
    test_levels = [-18, -15, -10, -9, -1, 27]

    for i, (name, logm, level, color) in enumerate(scales):
        y = logm
        # Cell / soliton representation
        ax.add_patch(Circle((3, y), 0.4, facecolor=color, edgecolor=WHITE,
                           linewidth=1.5, alpha=0.85, zorder=4))

        # Label
        is_test = logm in test_levels
        label_color = GOLD if is_test else WHITE
        weight = 'bold' if is_test else 'normal'
        ax.text(4, y, name, color=label_color, fontsize=11, va='center', fontweight=weight)
        ax.text(11, y, level, color=SILVER, fontsize=9, va='center', style='italic')

        # Scale notation
        ax.text(2, y, "10$^{%d}$ m" % logm, color=DIM, fontsize=9, va='center', ha='right')

    # The LOOP CLOSURE: arrow from Level 6 back to Level 0
    # Curved arrow on the left side
    from matplotlib.patches import FancyArrowPatch
    loop_arrow = FancyArrowPatch((3, 27), (3, -35),
                                  connectionstyle="arc3,rad=-1.2",
                                  arrowstyle='->', color=GOLD,
                                  linewidth=2, alpha=0.7, mutation_scale=20)
    ax.add_patch(loop_arrow)
    ax.text(-0.5, -5, 'CMB as inner\nboundary of\nuniversal soliton\n\n=\n\nsubstrate from\nwhich Level 0\nchildren emerge',
            color=GOLD, fontsize=10, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, linewidth=1))

    # Header annotations
    ax.text(3, 32, 'SOLITON HIERARCHY SCALE',
            color=WHITE, fontsize=12, ha='center', fontweight='bold')
    ax.text(3, -38, 'PLANCK SUBSTRATE',
            color=GOLD, fontsize=11, ha='center', fontweight='bold', style='italic')

    ax.text(11, 32, 'PCTRM LEVEL', color=WHITE, fontsize=10, ha='left', fontweight='bold')

    ax.set_title('Six-Level Soliton Hierarchy: 62 Orders of Magnitude, Closed as a Loop',
                 color=GOLD, fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')

    save(fig, 'pctrm_03_hierarchy_levels_scale.png')


# ================================================================
# FIG 4: DUAL-GEOMETRY AT FOUR SCALES
# Type: 4 (Geometric cross-section)
# Shows: Spherical modulus + toroidal remainder as universal
#        structural decomposition at proton, atom, Earth, galaxy.
# ================================================================

def fig4_dual_geometry():
    fig, axes = plt.subplots(1, 4, figsize=(18, 6))
    fig.patch.set_facecolor(BG)

    scales = [
        {
            'ax': axes[0], 'title': 'PROTON',
            'sphere_r': 1.3, 'sphere_label': 'confinement\nboundary',
            'torus_label': 'gluon\nflux tubes',
            'note': '~10$^{-15}$ m\n99% mass in torus',
            'color_s': BLUE, 'color_t': MAG,
        },
        {
            'ax': axes[1], 'title': 'ATOM',
            'sphere_r': 1.3, 'sphere_label': 'electron\nshells',
            'torus_label': 'magnetic\nmoment',
            'note': '~10$^{-10}$ m',
            'color_s': CYAN, 'color_t': ORANGE,
        },
        {
            'ax': axes[2], 'title': 'EARTH',
            'sphere_r': 1.3, 'sphere_label': 'atmospheric\nlayers',
            'torus_label': 'Van Allen\nbelts',
            'note': '~10$^{7}$ m',
            'color_s': GREEN, 'color_t': GOLD,
        },
        {
            'ax': axes[3], 'title': 'GALAXY',
            'sphere_r': 1.3, 'sphere_label': 'dark-matter\nhalo',
            'torus_label': 'galactic\ndisk',
            'note': '~10$^{21}$ m',
            'color_s': PURPLE, 'color_t': RED,
        },
    ]

    for s in scales:
        ax = s['ax']
        ax.set_facecolor(PAN)
        ax.set_xlim(-2.3, 2.3)
        ax.set_ylim(-2.3, 2.3)
        ax.set_aspect('equal')
        ax.axis('off')

        # Outer sphere (modulus, spherical sector)
        sphere = plt.Circle((0, 0), s['sphere_r'], fill=False,
                            color=s['color_s'], linewidth=2.5, alpha=0.85)
        ax.add_patch(sphere)
        # Translucent sphere fill
        sphere_fill = plt.Circle((0, 0), s['sphere_r'], facecolor=s['color_s'],
                                 alpha=0.1, edgecolor='none')
        ax.add_patch(sphere_fill)

        # Torus (remainder, toroidal sector) — drawn as ellipse with inner cut
        # Outer ellipse of torus
        outer_torus = Ellipse((0, 0), 1.7, 0.6, facecolor='none',
                              edgecolor=s['color_t'], linewidth=2)
        ax.add_patch(outer_torus)
        # Inner ellipse of torus (to suggest hole)
        inner_torus = Ellipse((0, 0), 0.6, 0.2, facecolor='none',
                              edgecolor=s['color_t'], linewidth=1.5, alpha=0.6)
        ax.add_patch(inner_torus)
        # Fill band
        torus_fill = Ellipse((0, 0), 1.7, 0.6, facecolor=s['color_t'],
                             alpha=0.18, edgecolor='none')
        ax.add_patch(torus_fill)

        # Title
        ax.text(0, 2.05, s['title'], color=WHITE, fontsize=14,
                ha='center', fontweight='bold')

        # Labels
        ax.text(0, s['sphere_r'] + 0.25, s['sphere_label'],
                color=s['color_s'], fontsize=9, ha='center', va='bottom')
        ax.text(0, -0.9, s['torus_label'],
                color=s['color_t'], fontsize=9, ha='center', va='top')

        # Scale note
        ax.text(0, -1.9, s['note'], color=SILVER, fontsize=9, ha='center')

        # Sector labels at bottom
        ax.text(-1.9, -2.2, 'sphere: modulus, β²', color=s['color_s'],
                fontsize=8, ha='left', style='italic')
        ax.text(1.9, -2.2, 'torus: remainder, K(k)', color=s['color_t'],
                fontsize=8, ha='right', style='italic')

    fig.suptitle('Dual-Geometry Sectors at Every Scale: Spherical Modulus + Toroidal Remainder',
                 color=GOLD, fontsize=16, fontweight='bold', y=1.02)

    save(fig, 'pctrm_04_dual_geometry_scales.png')


# ================================================================
# FIG 5: CHANNEL-SHARING vs EUCLIDEAN SEPARATION
# Type: 4 (Geometric cross-section)
# Shows: Bell dissolution — entangled particles are graph-neighbors,
#        the Euclidean distance is a projection artifact.
# ================================================================

def fig5_channel_sharing():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                   gridspec_kw={'wspace': 0.25})
    fig.patch.set_facecolor(BG)

    # LEFT: Euclidean view
    ax1.set_facecolor(PAN)
    ax1.set_xlim(-1, 12)
    ax1.set_ylim(-2, 5)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Two particles separated by big distance
    ax1.add_patch(Circle((1, 2), 0.4, facecolor=CYAN, edgecolor=WHITE, linewidth=2, zorder=5))
    ax1.text(1, 2, 'A', color=BG, fontsize=12, ha='center', va='center', fontweight='bold')
    ax1.add_patch(Circle((10, 2), 0.4, facecolor=MAG, edgecolor=WHITE, linewidth=2, zorder=5))
    ax1.text(10, 2, 'B', color=BG, fontsize=12, ha='center', va='center', fontweight='bold')

    # "Intermediate space" shaded — mystery region
    ax1.add_patch(mpatches.Rectangle((1.5, 1.3), 8, 1.4,
                                      facecolor=RED, alpha=0.08, edgecolor='none'))

    # Question marks
    for x in [3, 5, 7, 9]:
        ax1.text(x, 2, '?', color=RED, fontsize=20, ha='center', va='center', alpha=0.6)

    # Distance annotation
    ax1.annotate('', xy=(9.5, 3.5), xytext=(1.5, 3.5),
                 arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
    ax1.text(5.5, 3.75, 'large Euclidean distance', color=SILVER, fontsize=10, ha='center')

    ax1.text(5.5, 0.5, '"spooky action at a distance"',
             color=RED, fontsize=12, ha='center', fontweight='bold', style='italic')
    ax1.text(5.5, 0.0, 'correlation must traverse the intermediate region',
             color=RED, fontsize=10, ha='center')
    ax1.text(5.5, -0.4, 'but Bell says nothing can carry it locally',
             color=RED, fontsize=10, ha='center')

    ax1.text(5.5, 4.4, 'EUCLIDEAN VIEW', color=WHITE, fontsize=14,
             ha='center', fontweight='bold')
    ax1.text(5.5, -1.3, 'Manifold assumed. Distance primitive.',
             color=DIM, fontsize=10, ha='center', style='italic')
    ax1.text(5.5, -1.65, 'The manifold is what makes "distance" real.',
             color=DIM, fontsize=10, ha='center', style='italic')

    # RIGHT: Graph view — one pattern with two handles
    ax2.set_facecolor(PAN)
    ax2.set_xlim(-1, 12)
    ax2.set_ylim(-2, 5)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # The merged channel pattern — a cloud / blob
    from matplotlib.patches import Polygon
    # Abstract shape representing shared channel substrate
    theta = np.linspace(0, 2*np.pi, 80)
    r = 1.1 + 0.25 * np.sin(3*theta) + 0.15 * np.cos(5*theta)
    blob_x = 5.5 + r * np.cos(theta) * 1.2
    blob_y = 2.0 + r * np.sin(theta) * 0.9
    ax2.fill(blob_x, blob_y, color=GOLD, alpha=0.15, edgecolor=GOLD, linewidth=1.5, zorder=2)

    # Two handles on the blob
    ax2.add_patch(Circle((3.5, 2), 0.4, facecolor=CYAN, edgecolor=WHITE, linewidth=2, zorder=5))
    ax2.text(3.5, 2, 'A', color=BG, fontsize=12, ha='center', va='center', fontweight='bold')
    ax2.add_patch(Circle((7.5, 2), 0.4, facecolor=MAG, edgecolor=WHITE, linewidth=2, zorder=5))
    ax2.text(7.5, 2, 'B', color=BG, fontsize=12, ha='center', va='center', fontweight='bold')

    # Graph edge indicating adjacency
    ax2.plot([3.9, 7.1], [2, 2], color=GOLD, linewidth=3, alpha=0.8, zorder=3)
    ax2.text(5.5, 2.35, 'graph-distance = 1', color=GOLD, fontsize=10, ha='center',
             fontweight='bold')

    # Annotation showing the pattern
    ax2.text(5.5, 3.6, 'one shared channel pattern',
             color=GOLD, fontsize=11, ha='center', style='italic')
    ax2.text(5.5, 3.2, 'with two Euclidean handles',
             color=GOLD, fontsize=11, ha='center', style='italic')

    ax2.text(5.5, 0.5, 'A and B are graph-neighbors.',
             color=GREEN, fontsize=12, ha='center', fontweight='bold')
    ax2.text(5.5, 0.0, 'No "intermediate region" exists at the graph level.',
             color=GREEN, fontsize=10, ha='center')
    ax2.text(5.5, -0.4, 'Euclidean "distance" is a projection artifact.',
             color=GREEN, fontsize=10, ha='center')

    ax2.text(5.5, 4.4, 'GRAPH VIEW', color=WHITE, fontsize=14,
             ha='center', fontweight='bold')
    ax2.text(5.5, -1.3, 'Graph primitive. Adjacency primitive.',
             color=DIM, fontsize=10, ha='center', style='italic')
    ax2.text(5.5, -1.65, 'Distance is what you compute when you project.',
             color=DIM, fontsize=10, ha='center', style='italic')

    fig.suptitle('Bell Correlations: Graph-Adjacent, Euclidean-Separated',
                 color=GOLD, fontsize=16, fontweight='bold', y=1.00)

    save(fig, 'pctrm_05_channel_sharing_vs_euclidean.png')


# ================================================================
# FIG 6: BORN RULE FROM UNIT-GRAPH ROUND-TRIP CLOSURE
# Type: 4 (Geometric cross-section)
# Shows: Unity-summation across a complete basis forces |·|².
#        The exponent 2 is the unique exponent producing Σ = 1 automatic.
# ================================================================

def fig6_born_rule():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                   gridspec_kw={'wspace': 0.30, 'width_ratios': [1.1, 1]})
    fig.patch.set_facecolor(BG)

    # LEFT: Unit sphere with state vector and basis, showing round-trip
    ax1.set_facecolor(PAN)
    ax1.set_xlim(-1.8, 1.8)
    ax1.set_ylim(-1.8, 1.8)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # Unit circle (representing S^2 cross-section)
    circle = plt.Circle((0, 0), 1, fill=False, color=GOLD, linewidth=2, alpha=0.8)
    ax1.add_patch(circle)
    ax1.add_patch(plt.Circle((0, 0), 1, facecolor=GOLD, alpha=0.05, edgecolor='none'))

    # Origin
    ax1.plot(0, 0, 'o', color=WHITE, markersize=6, zorder=5)

    # Basis vector |α>
    alpha_angle = np.pi / 3
    ax1.annotate('', xy=(np.cos(alpha_angle), np.sin(alpha_angle)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=CYAN, lw=2.5))
    ax1.text(np.cos(alpha_angle)*1.15, np.sin(alpha_angle)*1.15, '|α⟩',
             color=CYAN, fontsize=14, ha='center', fontweight='bold')

    # State vector |ψ>
    psi_angle = np.pi / 8
    ax1.annotate('', xy=(np.cos(psi_angle), np.sin(psi_angle)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=MAG, lw=2.5))
    ax1.text(np.cos(psi_angle)*1.15, np.sin(psi_angle)*1.15 - 0.1, '|ψ⟩',
             color=MAG, fontsize=14, ha='center', fontweight='bold')

    # Projection of |ψ> onto |α> — show as perpendicular
    proj = np.cos(alpha_angle - psi_angle)
    proj_x = proj * np.cos(alpha_angle)
    proj_y = proj * np.sin(alpha_angle)
    ax1.plot([np.cos(psi_angle), proj_x], [np.sin(psi_angle), proj_y],
             color=DIM, linewidth=1, linestyle=':', alpha=0.6)
    ax1.plot([0, proj_x], [0, proj_y], color=WHITE, linewidth=2.5, alpha=0.9)

    # Label the projection
    ax1.text(proj_x * 0.5 - 0.08, proj_y * 0.5 + 0.12, '⟨α|ψ⟩',
             color=WHITE, fontsize=11, ha='center', fontweight='bold')

    # Round-trip arc (bidirectional)
    arc_r = 0.25
    ax1.annotate('', xy=(proj_x*0.3, proj_y*0.3 + 0.15),
                 xytext=(proj_x*0.7, proj_y*0.7 + 0.15),
                 arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.8,
                                connectionstyle="arc3,rad=0.3"))

    ax1.text(0, -1.35, '|⟨α|ψ⟩|² = ⟨ψ|α⟩⟨α|ψ⟩',
             color=GOLD, fontsize=13, ha='center', fontweight='bold')
    ax1.text(0, -1.58, 'round-trip closure on unit sphere',
             color=SILVER, fontsize=10, ha='center', style='italic')

    ax1.text(0, 1.55, 'STATE SPACE = UNIT VECTORS',
             color=WHITE, fontsize=12, ha='center', fontweight='bold')
    ax1.text(0, 1.3, '(unit distance is the only distance the substrate has)',
             color=DIM, fontsize=9, ha='center', style='italic')

    # RIGHT: Unity summation as forcing condition
    ax2.set_facecolor(PAN)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(-0.5, 10)
    ax2.axis('off')

    ax2.text(5, 9.4, 'WHY THE EXPONENT IS 2', color=WHITE, fontsize=14,
             ha='center', fontweight='bold')

    # The key equation
    ax2.text(5, 8.3, r'$\sum_i |\langle \alpha_i | \psi \rangle|^2 = 1$',
             color=GOLD, fontsize=20, ha='center', fontweight='bold')
    ax2.text(5, 7.5, 'across any complete basis — automatic from Parseval',
             color=GOLD, fontsize=10, ha='center', style='italic')

    # Comparison table
    ax2.text(1.5, 6.5, 'exponent', color=SILVER, fontsize=11, ha='center', fontweight='bold')
    ax2.text(5, 6.5, 'sum over basis', color=SILVER, fontsize=11, ha='center', fontweight='bold')
    ax2.text(8.5, 6.5, 'needs renorm?', color=SILVER, fontsize=11, ha='center', fontweight='bold')

    # Line under headers
    ax2.plot([0.5, 9.5], [6.25, 6.25], color=DIM, linewidth=0.8)

    rows = [
        ('|·|¹', 'Σ ⟨α|ψ⟩  (basis dependent)', 'yes — not a probability', RED),
        ('|·|²', 'Σ |⟨α|ψ⟩|² = 1  (exact)', 'NO — unity is automatic', GREEN),
        ('|·|⁴', 'Σ |⟨α|ψ⟩|⁴ ≠ 1  (ψ-dependent)', 'yes — ψ-dependent', RED),
        ('|·|⁶', 'Σ |⟨α|ψ⟩|⁶ ≠ 1', 'yes', RED),
    ]

    for i, (exp, summ, needs, col) in enumerate(rows):
        y = 5.75 - i * 0.85
        ax2.text(1.5, y, exp, color=col, fontsize=13, ha='center', fontweight='bold')
        ax2.text(5, y, summ, color=WHITE, fontsize=10, ha='center')
        ax2.text(8.5, y, needs, color=col, fontsize=10, ha='center')

    # The forcing condition
    ax2.add_patch(FancyBboxPatch((0.5, 0.3), 9, 1.6,
                                  boxstyle='round,pad=0.2',
                                  facecolor=BG, edgecolor=GOLD, linewidth=2))
    ax2.text(5, 1.5, 'Integer-fraction arithmetic has no infinities to subtract.',
             color=GOLD, fontsize=11, ha='center', fontweight='bold')
    ax2.text(5, 1.05, 'No renormalization is possible. No renormalization is needed.',
             color=GOLD, fontsize=11, ha='center', fontweight='bold')
    ax2.text(5, 0.6, 'Only |·|² works as-is. The Born rule is forced by unity.',
             color=WHITE, fontsize=11, ha='center', style='italic')

    fig.suptitle('The Born Rule: Forced by Unity Summation on a Unit-Adjacency Graph',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.99)

    save(fig, 'pctrm_06_born_rule_unity.png')


# ================================================================
# FIG 7: RENORMALIZATION UNNECESSARY — INTEGER FRACTIONS DON'T DIVERGE
# Type: 1 (Running/convergence)
# Shows: Continuum momentum integral diverges at high k; discrete
#        substrate sum is bounded by Planck cutoff.
# ================================================================

def fig7_renormalization():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                   gridspec_kw={'wspace': 0.28})
    fig.patch.set_facecolor(BG)

    # Common x range (log momentum)
    k = np.logspace(-3, 3, 500)  # k in arbitrary units

    # LEFT: Continuum QFT loop integral
    style_axes(ax1)
    # A simple representative: ∫dk/k^2 accumulating — use running integral
    integrand = 1.0 / k
    cum_integral = np.cumsum(integrand) * (k[1] - k[0]) * 10  # scaling for display
    # Replace with log-like growth
    cum_integral = np.log(k / k[0] + 1) * 0.8

    ax1.plot(k, cum_integral, color=RED, linewidth=2.5,
             label=r'$\int^\Lambda d^4k / k^2$ (continuum loop integral)')

    # Cutoff Λ position
    Lambda_pos = 100
    ax1.axvline(Lambda_pos, color=ORANGE, linewidth=2, linestyle='--', alpha=0.8)
    ax1.text(Lambda_pos * 1.15, 5.5, 'cutoff Λ\n(imposed by hand)',
             color=ORANGE, fontsize=10, ha='left')

    # Divergence arrow
    ax1.annotate('', xy=(600, 7), xytext=(300, 6),
                 arrowprops=dict(arrowstyle='->', color=RED, lw=2))
    ax1.text(500, 7.5, '→ ∞', color=RED, fontsize=16, ha='center', fontweight='bold')

    ax1.set_xscale('log')
    ax1.set_xlim(1e-3, 1e3)
    ax1.set_ylim(-0.5, 8.5)
    ax1.set_xlabel('momentum k (arbitrary units)', color=SILVER, fontsize=11)
    ax1.set_ylabel('accumulated integral contribution', color=SILVER, fontsize=11)
    ax1.set_title('CONTINUUM QFT: divergent without regularization',
                  color=WHITE, fontsize=13, fontweight='bold', pad=15)

    # Shaded "requires renormalization" region
    ax1.axvspan(Lambda_pos, 1e3, alpha=0.08, color=RED)
    ax1.text(300, 1.0, 'divergent region\nabsorbed into\ncounterterms\n(renormalization)',
             color=RED, fontsize=9, ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=RED, linewidth=1))

    ax1.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
               labelcolor=WHITE, fontsize=9)

    # RIGHT: Discrete substrate sum
    style_axes(ax2)
    # Sum over finite graph — bounded at Planck scale
    # Substrate: k maxes out at 1 cell / 1 tick = Planck momentum
    # Use same x-axis scale for comparison
    Planck_k = 500
    # Sum converges to finite value
    k_substrate = k[k <= Planck_k]
    substrate_cumsum = np.log(k_substrate / k_substrate[0] + 1) * 0.8

    ax2.plot(k_substrate, substrate_cumsum, color=GREEN, linewidth=2.5,
             label='Σ over finite graph (substrate sum)')

    # Planck cutoff
    ax2.axvline(Planck_k, color=GOLD, linewidth=2, linestyle='--', alpha=0.9)
    ax2.text(Planck_k * 1.15, 3.5, 'Planck cutoff\n(substrate limit:\n1 cell/tick)',
             color=GOLD, fontsize=10, ha='left')

    # Finite value label
    max_val = substrate_cumsum[-1]
    ax2.axhline(max_val, color=GREEN, linewidth=1, linestyle=':', alpha=0.6)
    ax2.text(1e-2, max_val + 0.3, 'finite (integer fraction)',
             color=GREEN, fontsize=10, ha='left', fontweight='bold')

    # Scatter points: actual graph sum is discrete
    sample_k = np.logspace(-2, np.log10(Planck_k), 30)
    sample_vals = np.log(sample_k / sample_k[0] + 1) * 0.8
    ax2.scatter(sample_k, sample_vals, s=40, facecolor=GREEN,
                edgecolor=WHITE, linewidth=1.2, zorder=5,
                alpha=0.85, label='individual cell contributions')

    ax2.set_xscale('log')
    ax2.set_xlim(1e-3, 1e3)
    ax2.set_ylim(-0.5, 8.5)
    ax2.set_xlabel('momentum k (same units)', color=SILVER, fontsize=11)
    ax2.set_ylabel('accumulated sum', color=SILVER, fontsize=11)
    ax2.set_title('PCTRM SUBSTRATE: finite by construction',
                  color=WHITE, fontsize=13, fontweight='bold', pad=15)

    # Annotation
    ax2.text(1e-2, 7.5, 'Integer fractions cannot diverge.',
             color=GREEN, fontsize=11, ha='left', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=GREEN, linewidth=1))
    ax2.text(1e-2, 6.8, 'No ∞ to subtract. No counterterms.',
             color=GREEN, fontsize=10, ha='left', style='italic')
    ax2.text(1e-2, 6.2, 'No hierarchy problem. No Landau pole.',
             color=GREEN, fontsize=10, ha='left', style='italic')

    ax2.legend(loc='lower right', facecolor=PAN, edgecolor=DIM,
               labelcolor=WHITE, fontsize=9)

    fig.suptitle('Renormalization Is Unnecessary: Discrete Arithmetic Has No Infinities',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    save(fig, 'pctrm_07_renormalization_unnecessary.png')


# ================================================================
# FIG 8: OBSERVATION-AS-ENTANGLEMENT — MERGER DOMINANCE
# Type: 7 (Progression/sequence)
# Shows: Measurement as channel-merger competition. No second dynamics.
#        Observer is just a soliton participating in merger.
# ================================================================

def fig8_observation_as_entanglement():
    fig, axes = plt.subplots(1, 3, figsize=(18, 8), gridspec_kw={'wspace': 0.15})
    fig.patch.set_facecolor(BG)

    titles = [
        'Panel 1: Before Observation',
        'Panel 2: Observer Enters Pool',
        'Panel 3: Merger Dominance',
    ]
    subtitles = [
        'target in channel-shared superposition\n(multiple candidate paths)',
        'observer begins channel-merger\n(competition between mergers)',
        'observer merger dominates\n(single-path outcome registered)',
    ]

    for i, (ax, title, sub) in enumerate(zip(axes, titles, subtitles)):
        ax.set_facecolor(PAN)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        ax.axis('off')

        # Title
        ax.text(0, 2.75, title, color=WHITE, fontsize=12, ha='center', fontweight='bold')
        ax.text(0, 2.4, sub, color=SILVER, fontsize=10, ha='center', style='italic')

        # Panel 1: target with multi-path channel-agreement
        if i == 0:
            # Central target
            ax.add_patch(Circle((0, 0), 0.35, facecolor=CYAN, edgecolor=WHITE,
                               linewidth=2, zorder=5))
            ax.text(0, 0, 'T', color=BG, fontsize=12, ha='center', va='center',
                    fontweight='bold')

            # Multiple candidate channel paths radiating out (superposition)
            n_paths = 6
            for j in range(n_paths):
                angle = 2 * np.pi * j / n_paths
                end_x = 1.7 * np.cos(angle)
                end_y = 1.7 * np.sin(angle)
                # Draw wavy channel indicating superposition
                t = np.linspace(0, 1, 50)
                wave = 0.1 * np.sin(8 * np.pi * t)
                # Perpendicular direction for wave
                perp_x = -np.sin(angle)
                perp_y = np.cos(angle)
                path_x = 0.35 * np.cos(angle) + (end_x - 0.35*np.cos(angle)) * t + wave * perp_x
                path_y = 0.35 * np.sin(angle) + (end_y - 0.35*np.sin(angle)) * t + wave * perp_y
                ax.plot(path_x, path_y, color=CYAN, linewidth=1.5, alpha=0.5)
                # Candidate endpoint
                ax.add_patch(Circle((end_x, end_y), 0.12, facecolor=CYAN,
                                   edgecolor=WHITE, linewidth=0.8, alpha=0.6, zorder=4))

            ax.text(0, -2.5, 'no observer in pool', color=GREEN, fontsize=10,
                    ha='center', fontweight='bold')
            ax.text(0, -2.85, 'channel-agreement holds all paths',
                    color=SILVER, fontsize=9, ha='center')

        # Panel 2: observer enters
        elif i == 1:
            # Target
            ax.add_patch(Circle((0, 0), 0.35, facecolor=CYAN, edgecolor=WHITE,
                               linewidth=2, zorder=5))
            ax.text(0, 0, 'T', color=BG, fontsize=12, ha='center', va='center',
                    fontweight='bold')

            # Observer entering from right — complex soliton
            ax.add_patch(Circle((1.9, 0), 0.5, facecolor=MAG, edgecolor=WHITE,
                               linewidth=2, zorder=5))
            ax.text(1.9, 0, 'O', color=BG, fontsize=13, ha='center', va='center',
                    fontweight='bold')

            # Merger beginning — gold channel forming between T and O
            ax.plot([0.35, 1.4], [0, 0], color=GOLD, linewidth=3.5, alpha=0.85, zorder=4)
            ax.text(0.9, 0.35, 'merger\nforming', color=GOLD, fontsize=9,
                    ha='center', style='italic')

            # Remaining candidate paths (distorting)
            n_paths = 5
            for j in range(n_paths):
                angle = np.pi/2 + 2 * np.pi * (j + 0.5) / n_paths
                if np.cos(angle) > 0.3:  # skip those pointing right (toward observer)
                    continue
                end_x = 1.6 * np.cos(angle)
                end_y = 1.6 * np.sin(angle)
                alpha_val = 0.35
                ax.plot([0.35 * np.cos(angle), end_x], [0.35 * np.sin(angle), end_y],
                        color=CYAN, linewidth=1.2, alpha=alpha_val)
                ax.add_patch(Circle((end_x, end_y), 0.1, facecolor=CYAN,
                                   edgecolor=WHITE, linewidth=0.5,
                                   alpha=alpha_val + 0.1, zorder=4))

            ax.text(0, -2.5, 'observer enters candidate pool',
                    color=ORANGE, fontsize=10, ha='center', fontweight='bold')
            ax.text(0, -2.85, 'merger competes with existing channels',
                    color=SILVER, fontsize=9, ha='center')

        # Panel 3: merger dominates
        else:
            # Target
            ax.add_patch(Circle((0, 0), 0.35, facecolor=CYAN, edgecolor=WHITE,
                               linewidth=2, zorder=5))
            ax.text(0, 0, 'T', color=BG, fontsize=12, ha='center', va='center',
                    fontweight='bold')

            # Observer — now merged
            ax.add_patch(Circle((1.9, 0), 0.5, facecolor=MAG, edgecolor=WHITE,
                               linewidth=2, zorder=5))
            ax.text(1.9, 0, 'O', color=BG, fontsize=13, ha='center', va='center',
                    fontweight='bold')

            # Dominant channel: thick, bright
            ax.plot([0.35, 1.4], [0, 0], color=GOLD, linewidth=5, alpha=1.0, zorder=4)

            # Shared pattern envelope
            theta = np.linspace(0, 2*np.pi, 80)
            r = 0.25 + 0.08 * np.sin(5*theta)
            env_x = 1.0 + (1.35 + r * np.cos(theta)) * np.cos(theta) * 0.3
            env_y = r * np.sin(theta) * 1.2
            # Simpler: ellipse around both
            envelope = Ellipse((0.95, 0), 2.6, 1.0, facecolor=GOLD,
                               alpha=0.12, edgecolor=GOLD, linewidth=1.2, zorder=2)
            ax.add_patch(envelope)

            # Decayed candidates — faded
            n_paths = 4
            for j in range(n_paths):
                angle = np.pi/2 + 2 * np.pi * (j + 0.5) / n_paths
                if np.cos(angle) > 0.3:
                    continue
                end_x = 1.4 * np.cos(angle)
                end_y = 1.4 * np.sin(angle)
                ax.plot([0.35 * np.cos(angle), end_x * 0.7],
                        [0.35 * np.sin(angle), end_y * 0.7],
                        color=DIM, linewidth=0.8, alpha=0.25, linestyle=':')
                ax.add_patch(Circle((end_x * 0.7, end_y * 0.7), 0.08, facecolor=DIM,
                                   edgecolor=DIM, linewidth=0.3, alpha=0.2, zorder=3))

            ax.text(0.95, 1.1, 'one merged pattern',
                    color=GOLD, fontsize=10, ha='center', fontweight='bold')

            ax.text(0, -2.5, 'observer merger dominates',
                    color=GREEN, fontsize=10, ha='center', fontweight='bold')
            ax.text(0, -2.85, '"outcome" = dominant merger, not collapse',
                    color=SILVER, fontsize=9, ha='center')

    # Bottom annotation spanning full width
    fig.text(0.5, 0.02,
             'One dynamics throughout: channel-merger arithmetic. The measurement problem does not exist — it dissolves.',
             color=GOLD, fontsize=13, ha='center', fontweight='bold', style='italic')

    fig.suptitle('Observation-as-Entanglement: Measurement Is Channel-Merger Competition',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    save(fig, 'pctrm_08_observation_as_entanglement.png')


# ================================================================
# MAIN
# ================================================================

def main():
    print("Generating PCTRM substrate spec diagrams...")
    print("Output directory: %s" % outdir)
    print()

    fig1_adjacency()
    fig2_photon_arithmetic()
    fig3_hierarchy()
    fig4_dual_geometry()
    fig5_channel_sharing()
    fig6_born_rule()
    fig7_renormalization()
    fig8_observation_as_entanglement()

    print()
    print("All 8 figures generated:")
    print("  pctrm_01_direction_conditional_adjacency.png")
    print("  pctrm_02_photon_nn_arithmetic.png")
    print("  pctrm_03_hierarchy_levels_scale.png")
    print("  pctrm_04_dual_geometry_scales.png")
    print("  pctrm_05_channel_sharing_vs_euclidean.png")
    print("  pctrm_06_born_rule_unity.png")
    print("  pctrm_07_renormalization_unnecessary.png")
    print("  pctrm_08_observation_as_entanglement.png")


if __name__ == '__main__':
    main()
