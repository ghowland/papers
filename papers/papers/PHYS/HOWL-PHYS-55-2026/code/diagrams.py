#!/usr/bin/env python3
"""
HOWL PHYS-55 Diagrams — Planck Cell-Tick Remainder Momentum II
8 figures covering the substrate specification, dual-geometry structure,
Born rule derivation, channel-agreement mechanisms, and cross-domain coherence.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, Wedge, Arc, Ellipse, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D
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
    

plt.rcParams.update({
    'axes.facecolor':     PAN,
    'figure.facecolor':   BG,
    'savefig.facecolor':  BG,
    'axes.edgecolor':     DIM,
    'axes.labelcolor':    SILVER,
    'xtick.color':        DIM,
    'ytick.color':        DIM,
    'grid.color':         DIM,
    'grid.alpha':         0.3,
    'text.color':         WHITE,
    'font.family':        'DejaVu Sans',
    'axes.spines.top':    False,
    'axes.spines.right':  False,
})

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


def style_axes(ax, hide_spines=False):
    if hide_spines:
        ax.axis('off')
        return
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)


# ================================================================
# FIG 1: UNIT-GRAPH ADJACENCY GEOMETRY
# Type: Geometric Cross-Section
# Shows: PCTRM's distinctive direction-conditional unit adjacency
#        vs. standard Cartesian lattice. The topology that produces
#        c-invariance by arithmetic identity and Hilbert unit-sphere
#        structure as substrate consequence.
# ================================================================

def fig1_unit_graph_adjacency():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9),
                                    gridspec_kw={'wspace': 0.30})

    # LEFT PANEL: PCTRM direction-conditional adjacency
    ax1.set_xlim(-1.6, 1.6)
    ax1.set_ylim(-1.6, 1.6)
    ax1.set_aspect('equal')
    style_axes(ax1, hide_spines=True)

    # Central cell
    center = Circle((0, 0), 0.08, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5)
    ax1.add_patch(center)

    # Many neighbors at continuous directions, all at distance 1
    n_neighbors = 36
    angles = np.linspace(0, 2*np.pi, n_neighbors, endpoint=False)
    for theta in angles:
        x = np.cos(theta)
        y = np.sin(theta)
        # line from center to neighbor
        ax1.plot([0, x], [0, y], color=CYAN, linewidth=0.8, alpha=0.5, zorder=2)
        # neighbor cell
        neighbor = Circle((x, y), 0.05, facecolor=CYAN, edgecolor=WHITE,
                           linewidth=1, alpha=0.8, zorder=4)
        ax1.add_patch(neighbor)

    # Unit circle guide
    unit_circle = Circle((0, 0), 1.0, fill=False, edgecolor=SILVER,
                          linewidth=1.2, linestyle='--', alpha=0.6, zorder=1)
    ax1.add_patch(unit_circle)

    # Distance label
    ax1.annotate('1 Planck distance',
                 xy=(0.707, 0.707), xytext=(1.15, 1.25),
                 color=GOLD, fontsize=10,
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2))

    # Direction continuous label
    ax1.text(0, -1.4, 'Any continuous direction',
             ha='center', va='center', color=WHITE, fontsize=11, fontstyle='italic')

    # Panel title
    ax1.text(0, 1.45, 'PCTRM: Direction-Conditional Unit Adjacency',
             ha='center', va='center', color=GOLD, fontsize=13, fontweight='bold')

    # Annotations
    ax1.text(-1.45, 1.15, 'Direction: continuous\nDistance: discrete = 1\nGraph: unit-adjacency',
             ha='left', va='top', color=SILVER, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN, linewidth=1))

    # RIGHT PANEL: Cartesian lattice (contrast)
    ax2.set_xlim(-1.6, 1.6)
    ax2.set_ylim(-1.6, 1.6)
    ax2.set_aspect('equal')
    style_axes(ax2, hide_spines=True)

    # Cartesian grid cells
    grid_range = np.arange(-1, 1.1, 0.5)
    for xg in grid_range:
        for yg in grid_range:
            is_center = (abs(xg) < 0.01 and abs(yg) < 0.01)
            is_neighbor = (abs(xg) + abs(yg) <= 0.5 + 0.01 and not is_center)
            if is_center:
                c = Circle((xg, yg), 0.08, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5)
            elif is_neighbor:
                c = Circle((xg, yg), 0.05, facecolor=RED, edgecolor=WHITE,
                            linewidth=1, alpha=0.8, zorder=4)
            else:
                c = Circle((xg, yg), 0.04, facecolor=DIM, edgecolor=DIM,
                            linewidth=0.5, alpha=0.5, zorder=3)
            ax2.add_patch(c)
            if is_neighbor:
                ax2.plot([0, xg], [0, yg], color=RED, linewidth=1.2, alpha=0.7, zorder=2)

    # Diagonal distance label (showing non-unit)
    diag_dist = np.sqrt(0.5**2 + 0.5**2)
    ax2.plot([0, 0.5], [0, 0.5], color=DIM, linewidth=0.8,
              linestyle=':', alpha=0.6, zorder=1)
    ax2.annotate('diagonal = sqrt(2)\nnon-unit',
                 xy=(0.35, 0.35), xytext=(1.0, 0.8),
                 color=ORANGE, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1))

    # Axis-only directions annotation
    ax2.text(0, -1.4, 'Only 4 axis directions',
             ha='center', va='center', color=WHITE, fontsize=11, fontstyle='italic')

    ax2.text(0, 1.45, 'Standard Cartesian Lattice (contrast)',
             ha='center', va='center', color=SILVER, fontsize=13, fontweight='bold')

    ax2.text(-1.45, 1.15, 'Direction: discrete\nDistance: varies sqrt(2)\nGraph: Euclidean lattice',
             ha='left', va='top', color=SILVER, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED, linewidth=1))

    # Figure title
    fig.suptitle('PCTRM Substrate: The Unit-Adjacency Graph',
                 color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    # Bottom caption inside axis
    fig.text(0.5, 0.02,
             'Every cell has neighbors at exactly 1 Planck distance in any continuous direction. '
             'Photon advances 1 cell per tick in any direction -> c-invariance is substrate arithmetic identity N/N = 1.',
             ha='center', va='bottom', color=SILVER, fontsize=10, fontstyle='italic')

    save(fig, 'phys55_01_unit_graph_adjacency.png')


# ================================================================
# FIG 2: SIX-LEVEL HIERARCHY WITH SCALE
# Type: Scale/Landscape Diagram
# Shows: 61 orders of magnitude spanned by the six-level hierarchy,
#        with solitons at each level and the framework identities
#        that apply. Communicates the scale ambition of the
#        parallel-isomorphism claim.
# ================================================================

def fig2_hierarchy_levels_scale():
    fig, ax = plt.subplots(figsize=(18, 12))

    # X-axis is the log-scale size axis
    ax.set_xlim(-36, 27)
    ax.set_ylim(-0.5, 8)
    style_axes(ax)
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)

    # X-axis ticks at powers of 10
    xticks = list(range(-35, 28, 5))
    ax.set_xticks(xticks)
    ax.set_xticklabels(['$10^{%d}$' % t for t in xticks], fontsize=9, color=SILVER)
    ax.set_xlabel('Length scale (m)', fontsize=12, color=SILVER)

    # Horizontal level bands
    levels = [
        (0, 'Level 0', 'Substrate',          -35, -33, GOLD,   'Unit-graph, c-invariance, Born rule, Bell'),
        (1, 'Level 1', 'Subatomic',          -18, -15, CYAN,   'Koide 2/3, V_us 9/40, V_cb 1/24, alpha_EM'),
        (2, 'Level 2', 'Atomic',             -11, -9,  BLUE,   'H 1S-2S, Lamb shift, bridge identity'),
        (3, 'Level 3', 'Nuclear',            -15, -13, GREEN,  'Proton lattice 3pi/2, binding, confinement'),
        (4, 'Level 4', 'Molecular',          -10, -8,  PURPLE, 'H2O angle, molecular orbitals'),
        (5, 'Level 5', 'Macroscopic',        -3, 13,   ORANGE, '1/r^2, Kepler, Mercury precession, GR factor 2'),
        (6, 'Level 6', 'Cosmological',       20, 27,   MAG,    'Omega_DM=pi/12, Omega_b=13/264, Omega_L=(251-22pi)/264'),
    ]

    for y_pos, level_label, domain, xlo, xhi, color, identities in levels:
        y = y_pos + 0.5
        # Band
        width = xhi - xlo
        ax.add_patch(Rectangle((xlo, y - 0.3), width, 0.6,
                                facecolor=color, alpha=0.25, edgecolor=color,
                                linewidth=1.5, zorder=2))
        # Level label on left side
        ax.text(-36, y, level_label, ha='left', va='center',
                color=color, fontsize=11, fontweight='bold')
        ax.text(-32.5, y, domain, ha='left', va='center',
                color=WHITE, fontsize=10)
        # Identities label on right side
        ax.text(xhi + 0.5, y, identities, ha='left', va='center',
                color=SILVER, fontsize=8.5, fontstyle='italic')

    # Key landmark markers
    landmarks = [
        (-35, 'Planck',     0.5,   GOLD),
        (-15, 'proton',     1.5,   CYAN),
        (-10, 'atom',       2.5,   BLUE),
        (-9,  'molecule',   4.5,   PURPLE),
        (0,   'human',      5.5,   ORANGE),
        (7,   'Earth',      5.5,   ORANGE),
        (11,  'Sun',        5.5,   ORANGE),
        (21,  'galaxy',     6.5,   MAG),
        (26,  'universe',   6.5,   MAG),
    ]

    for xlog, name, yp, color in landmarks:
        y = yp + 0.5
        ax.plot(xlog, y, 'o', markersize=9, color=color,
                 markeredgecolor=WHITE, markeredgewidth=1.5, zorder=6)
        ax.annotate(name, xy=(xlog, y), xytext=(xlog, y + 0.3),
                     ha='center', va='bottom', color=WHITE, fontsize=8.5)

    # Round 0 clearance annotation on Level 6
    ax.text(23.5, 7.25, 'Round 0 PASS\n(4 precision ids)',
             ha='center', va='center', color=GREEN, fontsize=8.5,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=GREEN, linewidth=1))

    # Cross-scale bridge annotation
    ax.annotate('Microscopic-cosmic bridge:\n22pi/13 at 300 ppm',
                 xy=(-15, 1.7), xytext=(-5, 0.2),
                 color=GOLD, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=1, alpha=0.7))
    ax.annotate('',
                 xy=(21, 6.7), xytext=(-5, 0.2),
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=1, alpha=0.7))

    # Title
    ax.set_title('Six-Level Soliton Hierarchy: 61 Orders of Magnitude',
                  color=GOLD, fontsize=16, fontweight='bold', pad=20)

    # Bottom caption inside plot
    ax.text(-4.5, -0.3,
             'Parallel-isomorphism claim: same substrate vocabulary at every scale. '
             'Same integer alphabet {2,3,8,11,12,13,22,251,264} + pi + K(k) produces predictions across all levels.',
             ha='center', va='bottom', color=SILVER, fontsize=9.5, fontstyle='italic')

    save(fig, 'phys55_02_hierarchy_levels_scale.png')


# ================================================================
# FIG 3: DUAL-GEOMETRY AT EVERY SCALE
# Type: Geometric Cross-Section (four-panel)
# Shows: Every soliton has spherical modulus + toroidal remainder.
#        Four scales: proton, atom, Earth, galaxy. Structure
#        recurs universally. PHYS-49 decomposition integrated.
# ================================================================

def fig3_dual_geometry_scales():
    fig, axes = plt.subplots(2, 2, figsize=(18, 14),
                              gridspec_kw={'wspace': 0.25, 'hspace': 0.28})

    # ================ PROTON PANEL ================
    ax = axes[0, 0]
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    style_axes(ax, hide_spines=True)

    # Spherical confinement boundary (modulus)
    proton_boundary = Circle((0, 0), 1.1, fill=False, edgecolor=CYAN,
                              linewidth=2.5, alpha=0.7, zorder=2)
    ax.add_patch(proton_boundary)
    proton_fill = Circle((0, 0), 1.1, facecolor=CYAN, alpha=0.08, zorder=1)
    ax.add_patch(proton_fill)

    # Toroidal gluon flux tubes (remainder)
    # Draw several overlapping tori to suggest flux-tube structure
    thetas = np.linspace(0, 2*np.pi, 60)
    for offset in [-0.35, 0, 0.35]:
        x = 0.55 * np.cos(thetas) + offset * np.cos(thetas * 3)
        y = 0.55 * np.sin(thetas)
        ax.plot(x, y, color=GOLD, linewidth=1.5, alpha=0.6)
    # Small toroidal loop overlays
    for theta_c in [0, 2*np.pi/3, 4*np.pi/3]:
        cx = 0.4 * np.cos(theta_c)
        cy = 0.4 * np.sin(theta_c)
        tor = Ellipse((cx, cy), 0.55, 0.15, angle=np.degrees(theta_c),
                       fill=False, edgecolor=GOLD, linewidth=1.3, alpha=0.8)
        ax.add_patch(tor)

    # Labels
    ax.text(0, 1.25, 'PROTON (Level 3)', ha='center', va='bottom',
             color=WHITE, fontsize=12, fontweight='bold')
    ax.text(-1.35, 0.9, 'Spherical modulus:\nconfinement boundary\n3pi/2 = 6 beta',
             ha='left', va='top', color=CYAN, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1))
    ax.text(1.35, -0.9, 'Toroidal remainder:\ngluon flux tubes\n99% of proton mass',
             ha='right', va='bottom', color=GOLD, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1))
    ax.text(0, -1.3, '~10^{-15} m', ha='center', va='top', color=SILVER, fontsize=9)

    # ================ ATOM PANEL ================
    ax = axes[0, 1]
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    style_axes(ax, hide_spines=True)

    # Nucleus
    nucleus = Circle((0, 0), 0.1, facecolor=GOLD, edgecolor=WHITE,
                      linewidth=1.5, zorder=5)
    ax.add_patch(nucleus)

    # Spherical electron shells (modulus)
    for r, alpha in [(0.4, 0.7), (0.7, 0.5), (1.05, 0.3)]:
        shell = Circle((0, 0), r, fill=False, edgecolor=CYAN,
                        linewidth=1.8, alpha=alpha, linestyle='--', zorder=2)
        ax.add_patch(shell)

    # Toroidal magnetic moment structure (remainder)
    # Figure-8 / magnetic field line pattern
    t = np.linspace(0, 2*np.pi, 100)
    for scale in [0.9, 1.15]:
        # Dipole field lines (figure-eight)
        x_dipole = scale * np.sin(t) * np.cos(t)
        y_dipole = scale * np.sin(t)
        ax.plot(x_dipole, y_dipole, color=GOLD, linewidth=1.2, alpha=0.6)

    # Labels
    ax.text(0, 1.25, 'ATOM (Level 2)', ha='center', va='bottom',
             color=WHITE, fontsize=12, fontweight='bold')
    ax.text(-1.35, 0.9, 'Spherical modulus:\nelectron shells\nradial quantization',
             ha='left', va='top', color=CYAN, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1))
    ax.text(1.35, -0.9, 'Toroidal remainder:\nmagnetic moment\nspin-orbit structure',
             ha='right', va='bottom', color=GOLD, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1))
    ax.text(0, -1.3, '~10^{-10} m', ha='center', va='top', color=SILVER, fontsize=9)

    # ================ EARTH PANEL ================
    ax = axes[1, 0]
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    style_axes(ax, hide_spines=True)

    # Earth
    earth = Circle((0, 0), 0.4, facecolor=BLUE, edgecolor=WHITE,
                    linewidth=1.5, zorder=5)
    ax.add_patch(earth)

    # Spherical atmosphere shells (modulus)
    for r, alpha in [(0.5, 0.6), (0.58, 0.4), (0.66, 0.25)]:
        shell = Circle((0, 0), r, fill=False, edgecolor=CYAN,
                        linewidth=1.5, alpha=alpha, zorder=3)
        ax.add_patch(shell)

    # Toroidal Van Allen belts (remainder) - inner and outer
    for cx_offset, width_e, height_e, alpha_band in [(0.85, 0.45, 0.20, 0.5),
                                                       (1.15, 0.35, 0.14, 0.4)]:
        # Inner belt right
        belt_right = Ellipse((cx_offset, 0), width_e, height_e,
                              fill=True, facecolor=GOLD, alpha=alpha_band*0.4,
                              edgecolor=GOLD, linewidth=1.5, zorder=2)
        ax.add_patch(belt_right)
        # Mirror for left
        belt_left = Ellipse((-cx_offset, 0), width_e, height_e,
                             fill=True, facecolor=GOLD, alpha=alpha_band*0.4,
                             edgecolor=GOLD, linewidth=1.5, zorder=2)
        ax.add_patch(belt_left)

    # Dipole field lines
    t = np.linspace(-np.pi, np.pi, 80)
    for scale in [0.75, 1.0, 1.3]:
        x_line = scale * np.sin(t)
        y_line = scale * np.sin(t) * np.cos(t) * 0.9
        ax.plot(x_line, y_line, color=GOLD, linewidth=0.8, alpha=0.5)

    # Labels
    ax.text(0, 1.25, 'EARTH (Level 5)', ha='center', va='bottom',
             color=WHITE, fontsize=12, fontweight='bold')
    ax.text(-1.55, 1.1, 'Spherical modulus:\natmosphere shells\nradial layering',
             ha='left', va='top', color=CYAN, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1))
    ax.text(1.55, -0.9, 'Toroidal remainder:\nVan Allen belts\nmagnetopause',
             ha='right', va='bottom', color=GOLD, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1))
    ax.text(0, -1.3, '~10^{7} m', ha='center', va='top', color=SILVER, fontsize=9)

    # ================ GALAXY PANEL ================
    ax = axes[1, 1]
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect('equal')
    style_axes(ax, hide_spines=True)

    # Galactic disk (toroidal remainder)
    disk = Ellipse((0, 0), 2.0, 0.35, fill=True, facecolor=GOLD,
                    alpha=0.3, edgecolor=GOLD, linewidth=2, zorder=3)
    ax.add_patch(disk)
    # Bulge
    bulge = Circle((0, 0), 0.25, facecolor=GOLD, edgecolor=GOLD,
                    linewidth=1, alpha=0.7, zorder=4)
    ax.add_patch(bulge)

    # Spiral arms on disk
    t = np.linspace(0.1, 3.2, 50)
    for phase in [0, np.pi]:
        r = t * 0.32
        x = r * np.cos(t + phase)
        y = r * np.sin(t + phase) * 0.18
        ax.plot(x, y, color=GOLD, linewidth=1.3, alpha=0.5)

    # Spherical dark matter halo (modulus)
    halo_outer = Circle((0, 0), 1.2, fill=False, edgecolor=CYAN,
                        linewidth=2, alpha=0.6, linestyle='--', zorder=2)
    halo_inner = Circle((0, 0), 1.2, facecolor=CYAN, alpha=0.10, zorder=1)
    ax.add_patch(halo_outer)
    ax.add_patch(halo_inner)

    # Labels
    ax.text(0, 1.32, 'GALAXY (Level 6)', ha='center', va='bottom',
             color=WHITE, fontsize=12, fontweight='bold')
    ax.text(-1.35, 1.1, 'Spherical modulus:\ndark matter halo\nOmega_DM = pi/12',
             ha='left', va='top', color=CYAN, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=CYAN, linewidth=1))
    ax.text(1.35, -0.9, 'Toroidal remainder:\ngalactic disk\nDM/b = 22pi/13',
             ha='right', va='bottom', color=GOLD, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, linewidth=1))
    ax.text(0, -1.3, '~10^{21} m', ha='center', va='top', color=SILVER, fontsize=9)

    # Figure title
    fig.suptitle('Dual-Geometry at Every Soliton Scale: Spherical Modulus + Toroidal Remainder',
                  color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    fig.text(0.5, 0.02,
              'Same structural decomposition at every hierarchy level. '
              'Cyan = spherical (beta content, L1/L2 conversion). Gold = toroidal (K(k) content, elliptic period).',
              ha='center', va='bottom', color=SILVER, fontsize=10, fontstyle='italic')

    save(fig, 'phys55_03_dual_geometry_scales.png')


# ================================================================
# FIG 4: BORN RULE AS ROUND-TRIP CLOSURE
# Type: Geometric Cross-Section
# Shows: Unit sphere (state manifold from substrate adjacency),
#        state vector |psi>, measurement basis, forward projection,
#        conjugate closure. Why |<alpha|psi>|^2 emerges as two-
#        conversion round-trip geometry.
# ================================================================

def fig4_born_round_trip():
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(-1.7, 1.9)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    style_axes(ax, hide_spines=True)

    # Unit sphere (drawn as circle cross-section)
    unit_sphere = Circle((0, 0), 1.0, fill=False, edgecolor=WHITE,
                          linewidth=2, zorder=2)
    ax.add_patch(unit_sphere)
    # Suggestive of sphere with equator ellipse
    equator = Ellipse((0, 0), 2.0, 0.3, fill=False, edgecolor=DIM,
                       linewidth=1, linestyle=':', alpha=0.6, zorder=1)
    ax.add_patch(equator)
    # Meridian
    meridian = Ellipse((0, 0), 0.3, 2.0, fill=False, edgecolor=DIM,
                        linewidth=1, linestyle=':', alpha=0.6, zorder=1)
    ax.add_patch(meridian)

    # State vector |psi> at 60 degrees
    theta_psi = np.radians(60)
    psi_x = np.cos(theta_psi)
    psi_y = np.sin(theta_psi)
    ax.annotate('', xy=(psi_x, psi_y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=CYAN, lw=3),
                 zorder=5)
    ax.plot(psi_x, psi_y, 'o', markersize=14, color=CYAN,
             markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
    ax.text(psi_x + 0.1, psi_y + 0.1, r'$|\psi\rangle$',
             color=CYAN, fontsize=16, fontweight='bold')

    # Measurement basis |alpha> at 15 degrees
    theta_alpha = np.radians(15)
    alpha_x = np.cos(theta_alpha)
    alpha_y = np.sin(theta_alpha)
    ax.annotate('', xy=(alpha_x, alpha_y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=3),
                 zorder=5)
    ax.plot(alpha_x, alpha_y, 'o', markersize=14, color=GOLD,
             markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
    ax.text(alpha_x + 0.1, alpha_y - 0.1, r'$|\alpha\rangle$',
             color=GOLD, fontsize=16, fontweight='bold')

    # Forward projection drop: from psi down onto alpha direction
    # Projection point on alpha direction
    proj_length = psi_x * alpha_x + psi_y * alpha_y  # <alpha|psi> = cos(theta_psi - theta_alpha)
    proj_x = proj_length * alpha_x
    proj_y = proj_length * alpha_y

    # Forward projection arrow (psi -> proj point)
    ax.plot([psi_x, proj_x], [psi_y, proj_y], color=MAG,
             linewidth=2.5, linestyle='--', alpha=0.85, zorder=4)
    ax.annotate('', xy=(proj_x, proj_y), xytext=(psi_x, psi_y),
                 arrowprops=dict(arrowstyle='->', color=MAG, lw=2.5,
                                 linestyle='--'), zorder=4)

    # Round-trip closure arrow (back up)
    # Draw curved arrow from proj back to psi, suggesting conjugate closure
    arc_center_x = (proj_x + psi_x) / 2 + 0.15
    arc_center_y = (proj_y + psi_y) / 2 + 0.05
    ax.annotate('', xy=(psi_x - 0.05, psi_y),
                 xytext=(proj_x + 0.03, proj_y + 0.05),
                 arrowprops=dict(arrowstyle='->', color=GREEN, lw=2,
                                 connectionstyle="arc3,rad=0.5"),
                 zorder=4)

    # Projection length label
    mid_proj_x = (proj_x + 0) / 2
    mid_proj_y = (proj_y + 0) / 2
    ax.text(mid_proj_x + 0.08, mid_proj_y - 0.12,
             r'$\langle\alpha|\psi\rangle$',
             color=MAG, fontsize=13, fontweight='bold')

    # Round-trip label
    ax.text(0.95, 0.6, r'$\langle\psi|\alpha\rangle\langle\alpha|\psi\rangle = |\langle\alpha|\psi\rangle|^2$',
             color=GREEN, fontsize=13, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=GREEN, linewidth=1.5))

    # Annotation: Unit sphere from substrate
    ax.text(-1.55, 1.3,
             'Unit sphere structure:\nINHERITED from substrate,\nnot postulated',
             ha='left', va='top', color=WHITE, fontsize=10,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=WHITE, linewidth=1.2))
    ax.annotate('', xy=(-0.7, 0.72), xytext=(-1.2, 1.1),
                 arrowprops=dict(arrowstyle='->', color=WHITE, lw=1, alpha=0.7))

    # Exponent counting annotation
    ax.text(1.0, -1.35,
             'The "2" in |.|^2 counts TWO conversions:\n'
             'forward projection (1) + conjugate closure (2).\n'
             'Same exponent pattern as MATH-11 beta^2 \n'
             'in QED angular integrations (PHYS-49).',
             ha='center', va='bottom', color=GOLD, fontsize=10,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=GOLD, linewidth=1.2))

    # Origin marker
    ax.plot(0, 0, 'o', markersize=8, color=WHITE, zorder=7)

    # Title
    ax.set_title('Born Rule as Unit-Graph Round-Trip Closure',
                  color=GOLD, fontsize=16, fontweight='bold', pad=15)

    # Bottom caption
    ax.text(0.1, -1.55,
             'Substrate unit-adjacency -> unit-sphere state manifold -> '
             'round-trip projection required for basis-independent positive-real extraction -> |.|^2 emerges.',
             ha='center', va='bottom', color=SILVER, fontsize=10, fontstyle='italic')

    save(fig, 'phys55_04_born_round_trip.png')


# ================================================================
# FIG 5: MASS-SCALING SECTOR DOMINANCE
# Type: Running/Convergence Chart
# Shows: Spherical and toroidal sector contributions to four-loop
#        corrections as function of lepton mass. Crossover at 22 MeV.
#        Electron (spherical dominance), muon (toroidal dominance),
#        tau prediction. PHYS-49 evidence.
# ================================================================

def fig5_mass_scaling_sectors():
    fig, ax = plt.subplots(figsize=(16, 10))

    # X-axis: lepton mass in MeV (log scale)
    mass_range = np.logspace(-1, 4, 500)  # 0.1 MeV to 10 GeV

    # Sector fractions — use (m/m_e)^2 scaling behavior
    # Spherical fraction: dominates at low mass (long Compton wavelength)
    # Toroidal fraction: grows as (m/m_e)^2
    m_e_MeV = 0.511
    crossover_MeV = 43 * m_e_MeV  # 22 MeV

    # Toroidal-to-universal ratio scales as (m/m_e)^2
    toroidal_ratio = (mass_range / m_e_MeV) ** 2 * 5.4e-4  # normalized so electron = 0.054%
    # Spherical fraction vs toroidal: use sigmoid crossover
    log_ratio = np.log10(toroidal_ratio / 1.0)  # ratio of toroidal to spherical
    spherical_dominance = 1.0 / (1.0 + toroidal_ratio)
    toroidal_dominance = toroidal_ratio / (1.0 + toroidal_ratio)

    ax.semilogx(mass_range, spherical_dominance * 100, color=CYAN, linewidth=2.5,
                 label='Spherical sector (modulus)', zorder=3)
    ax.semilogx(mass_range, toroidal_dominance * 100, color=GOLD, linewidth=2.5,
                 label='Toroidal sector (remainder)', zorder=3)

    # Crossover line
    ax.axvline(crossover_MeV, color=ORANGE, linestyle='--', linewidth=1.5,
                alpha=0.7, zorder=2)
    ax.text(crossover_MeV * 1.15, 78, 'Crossover\n22 MeV',
             color=ORANGE, fontsize=10, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=ORANGE, linewidth=1))

    # Data points for measured leptons
    # Electron
    ax.plot(m_e_MeV, 99.95, 'o', markersize=14, color=CYAN,
             markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
    ax.annotate('ELECTRON\n0.511 MeV\nSpherical dominates\n(toroidal: 0.054%)',
                 xy=(m_e_MeV, 99.95), xytext=(0.15, 75),
                 color=CYAN, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                           edgecolor=CYAN, linewidth=1))

    # Muon
    m_mu_MeV = 105.7
    toroidal_muon = (m_mu_MeV / m_e_MeV)**2 * 5.4e-4
    muon_sph = 100.0 / (1 + toroidal_muon)
    muon_tor = 100.0 - muon_sph
    ax.plot(m_mu_MeV, muon_tor, 'D', markersize=14, color=GOLD,
             markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
    ax.annotate('MUON\n105.7 MeV\nToroidal dominates\n(2304% amplification)',
                 xy=(m_mu_MeV, muon_tor), xytext=(300, 20),
                 color=GOLD, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                           edgecolor=GOLD, linewidth=1))

    # Tau prediction region
    m_tau_MeV = 1777
    toroidal_tau = (m_tau_MeV / m_e_MeV)**2 * 5.4e-4
    tau_tor = 100.0 * toroidal_tau / (1 + toroidal_tau)
    ax.plot(m_tau_MeV, tau_tor, 's', markersize=14, color=MAG,
             markeredgecolor=WHITE, markeredgewidth=2, zorder=6)
    ax.annotate('TAU (prediction)\n1777 MeV\nOverwhelming toroidal\n(~650,000% ratio)',
                 xy=(m_tau_MeV, tau_tor), xytext=(1200, 55),
                 color=MAG, fontsize=9,
                 arrowprops=dict(arrowstyle='->', color=MAG, lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                           edgecolor=MAG, linewidth=1))

    # Axes
    ax.set_xlabel('Lepton mass (MeV)', fontsize=12, color=SILVER)
    ax.set_ylabel('Sector contribution (%)', fontsize=12, color=SILVER)
    ax.set_xlim(0.1, 10000)
    ax.set_ylim(-3, 108)
    ax.grid(True, alpha=0.2, zorder=1)

    # Legend
    leg = ax.legend(loc='center right', facecolor=PAN, edgecolor=DIM,
                     labelcolor=WHITE, fontsize=10)
    leg.get_frame().set_alpha(0.9)

    # Title
    ax.set_title('Probe-Dependent Sector Dominance: Four-Loop QED Mass Scaling',
                  color=GOLD, fontsize=16, fontweight='bold', pad=15)

    # Bottom caption
    ax.text(10, -1.5,
             'PHYS-49 precision evidence: (m/m_e)^2 scaling of mass-dependent four-loop corrections. '
             'Heavier probes resolve toroidal structure. Tau measurement at FNAL precision = pre-registered test (K18).',
             ha='center', va='top', color=SILVER, fontsize=9.5, fontstyle='italic')

    save(fig, 'phys55_05_mass_scaling_sectors.png')


# ================================================================
# FIG 6: CHANNEL-AGREEMENT AT THE DOUBLE SLIT
# Type: Geometric Cross-Section (two-panel)
# Shows: Without observer -> multi-path channel agreement ->
#        interference. With observer -> single-path resolution ->
#        particle pattern. Wave-particle duality dissolved.
# ================================================================

def fig6_channel_agreement_double_slit():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10),
                                    gridspec_kw={'wspace': 0.25})

    # ================ LEFT PANEL: NO OBSERVER ================
    ax1.set_xlim(-0.5, 10)
    ax1.set_ylim(-3, 3)
    ax1.set_aspect('equal')
    style_axes(ax1, hide_spines=True)

    # Source
    source = Circle((0, 0), 0.25, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5)
    ax1.add_patch(source)
    ax1.text(0, -0.6, 'Emission', ha='center', va='top', color=GOLD, fontsize=9)

    # Slits (barrier with two openings)
    barrier_x = 3
    ax1.plot([barrier_x, barrier_x], [-2.8, -0.6], color=WHITE, linewidth=4)
    ax1.plot([barrier_x, barrier_x], [-0.35, 0.35], color=DIM, linewidth=1, alpha=0.3)
    ax1.plot([barrier_x, barrier_x], [0.6, 2.8], color=WHITE, linewidth=4)
    ax1.text(barrier_x, 3.15, 'Slits', ha='center', va='bottom', color=WHITE, fontsize=10)

    # Both paths active - channel agreement across both
    # Path 1 (upper)
    t_path = np.linspace(0, 1, 50)
    x_path1 = 0.25 + t_path * (barrier_x - 0.25)
    y_path1 = t_path * 0.5
    ax1.plot(x_path1, y_path1, color=CYAN, linewidth=2, alpha=0.75, zorder=3)
    # Path 2 (lower)
    x_path2 = 0.25 + t_path * (barrier_x - 0.25)
    y_path2 = -t_path * 0.5
    ax1.plot(x_path2, y_path2, color=CYAN, linewidth=2, alpha=0.75, zorder=3)

    # After slits - diverging to screen
    screen_x = 9
    for y_start, n_waves in [(0.5, 6), (-0.5, 6)]:
        x_after = np.linspace(barrier_x, screen_x, 80)
        y_after = y_start + (x_after - barrier_x) * 0.25 * np.sign(y_start)
        # Add wave ripples
        for offset in np.linspace(0, 2.5, n_waves):
            ax1.plot(x_after, y_after + offset * 0.2 * np.sin(5 * (x_after - barrier_x)),
                      color=CYAN, linewidth=0.6, alpha=0.3)
        ax1.plot(x_after, y_after, color=CYAN, linewidth=1.5, alpha=0.6)

    # Screen
    ax1.plot([screen_x, screen_x], [-2.8, 2.8], color=WHITE, linewidth=2.5)

    # Interference pattern on screen
    y_screen = np.linspace(-2.5, 2.5, 200)
    # Simple double-slit interference
    intensity = (np.cos(3.5 * y_screen) ** 2) * np.exp(-y_screen**2 / 4)
    # Draw as small boxes showing intensity
    for yi, Ii in zip(y_screen[::4], intensity[::4]):
        bar_width = 0.4 * Ii
        if bar_width > 0.02:
            ax1.add_patch(Rectangle((screen_x, yi - 0.03), bar_width, 0.06,
                                     facecolor=MAG, edgecolor=MAG, alpha=0.8, zorder=4))

    ax1.text(screen_x + 0.3, 2.5, 'Interference\npattern',
              color=MAG, fontsize=10, fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                        edgecolor=MAG, linewidth=1))

    # Annotations
    ax1.text(4.8, -2.3,
              'Channel agreement\nresolves across\nBOTH paths',
              ha='center', va='center', color=CYAN, fontsize=10, fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                        edgecolor=CYAN, linewidth=1.2))

    # Title
    ax1.set_title('NO OBSERVER AT SLITS',
                   color=WHITE, fontsize=13, fontweight='bold', pad=15)

    # ================ RIGHT PANEL: OBSERVER AT SLIT ================
    ax2.set_xlim(-0.5, 10)
    ax2.set_ylim(-3, 3)
    ax2.set_aspect('equal')
    style_axes(ax2, hide_spines=True)

    # Source
    source2 = Circle((0, 0), 0.25, facecolor=GOLD, edgecolor=WHITE, linewidth=2, zorder=5)
    ax2.add_patch(source2)
    ax2.text(0, -0.6, 'Emission', ha='center', va='top', color=GOLD, fontsize=9)

    # Slits
    ax2.plot([barrier_x, barrier_x], [-2.8, -0.6], color=WHITE, linewidth=4)
    ax2.plot([barrier_x, barrier_x], [-0.35, 0.35], color=DIM, linewidth=1, alpha=0.3)
    ax2.plot([barrier_x, barrier_x], [0.6, 2.8], color=WHITE, linewidth=4)
    ax2.text(barrier_x, 3.15, 'Slits', ha='center', va='bottom', color=WHITE, fontsize=10)

    # Observer at upper slit
    observer_x = barrier_x + 0.35
    observer_y = 0.5
    obs = Circle((observer_x, observer_y), 0.25, facecolor=ORANGE,
                  edgecolor=WHITE, linewidth=2, zorder=6)
    ax2.add_patch(obs)
    ax2.text(observer_x + 0.4, observer_y, 'Observer',
              color=ORANGE, fontsize=9, va='center')

    # Only ONE path resolved (upper) - observer joins candidate pool
    x_path_full = np.linspace(0.25, observer_x, 80)
    y_path_full = (x_path_full - 0.25) / (observer_x - 0.25) * observer_y
    ax2.plot(x_path_full, y_path_full, color=CYAN, linewidth=2.5, alpha=0.9, zorder=3)

    # After observation - particle propagates along determined path
    x_after_det = np.linspace(observer_x, screen_x, 80)
    y_after_det = observer_y + (x_after_det - observer_x) * 0.2
    ax2.plot(x_after_det, y_after_det, color=CYAN, linewidth=2.5, alpha=0.85, zorder=3)

    # Lower path faded (no photon went there because upper was observed)
    t_lower = np.linspace(0, 1, 30)
    x_lower = 0.25 + t_lower * (barrier_x - 0.25)
    y_lower = -t_lower * 0.5
    ax2.plot(x_lower, y_lower, color=DIM, linewidth=1, alpha=0.3,
              linestyle=':', zorder=2)

    # Screen
    ax2.plot([screen_x, screen_x], [-2.8, 2.8], color=WHITE, linewidth=2.5)

    # Particle pattern - two bands (no interference)
    for y_band, alpha in [(0.7, 0.9), (0.5, 0.7), (0.9, 0.5)]:
        ax2.add_patch(Rectangle((screen_x, y_band - 0.08), 0.35, 0.16,
                                 facecolor=MAG, edgecolor=MAG, alpha=alpha, zorder=4))

    ax2.text(screen_x + 0.3, 2.5, 'Particle\npattern',
              color=MAG, fontsize=10, fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                        edgecolor=MAG, linewidth=1))

    # Annotations
    ax2.text(4.8, -2.3,
              'Observer enters\ncandidate pool ->\nsingle-path resolution',
              ha='center', va='center', color=ORANGE, fontsize=10, fontweight='bold',
              bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                        edgecolor=ORANGE, linewidth=1.2))

    # Title
    ax2.set_title('OBSERVER AT SLIT',
                   color=WHITE, fontsize=13, fontweight='bold', pad=15)

    # Figure title
    fig.suptitle('Channel-Agreement Dynamics: Wave-Particle Duality Dissolved',
                  color=GOLD, fontsize=16, fontweight='bold', y=0.98)

    fig.text(0.5, 0.02,
              'Same substrate mechanism produces both patterns. Observer participation modifies the candidate pool, not the dynamics. '
              'The photon has no mid-flight trajectory to observe; channel resolves at termination.',
              ha='center', va='bottom', color=SILVER, fontsize=10, fontstyle='italic')

    save(fig, 'phys55_06_channel_agreement_slit.png')


# ================================================================
# FIG 7: INTEGER ALPHABET AS PREDICTION GENERATOR
# Type: Connection/Integer Map
# Shows: Small integer alphabet + pi + K(k) produce many
#        precision predictions across domains. Cross-domain
#        coherence made visual.
# ================================================================

def fig7_integer_alphabet_map():
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-7, 7)
    style_axes(ax, hide_spines=True)

    # Central alphabet nodes - integers and transcendentals
    alphabet_nodes = [
        # (x, y, label, color)
        (-4, 2,   '13',    GOLD),
        (-4, 0,   '22',    CYAN),
        (-4, -2,  '264',   MAG),
        (-2, 3,   '11',    BLUE),
        (-2, 1,   '8',     ORANGE),
        (-2, -1,  '12',    PURPLE),
        (-2, -3,  '251',   GREEN),
        (0,  2,   'pi',    WHITE),
        (0,  0,   'beta',  GOLD),
        (0,  -2,  'K(k)',  MAG),
        (-2, 4,   '3',     CYAN),
        (-2, -4.5, '24',   SILVER),
    ]

    for x, y, label, color in alphabet_nodes:
        ax.add_patch(Circle((x, y), 0.4, facecolor=BG, edgecolor=color,
                             linewidth=2, zorder=5))
        ax.text(x, y, label, ha='center', va='center',
                 color=color, fontsize=11, fontweight='bold', zorder=6)

    # Prediction nodes on the right
    predictions = [
        (5, 5,   'Omega_Lambda\n(251-22pi)/264',  '85 ppm',    GOLD),
        (5, 3.5, 'Omega_DM = pi/12',              '0.4 sigma', PURPLE),
        (5, 2,   'Omega_b = 13/264',              '0.5 sigma', MAG),
        (5, 0.5, 'DM/baryon = 22pi/13',           '725 ppm',   CYAN),
        (5, -1,  'H_0 ratio = 12/11',             '0.7%',      ORANGE),
        (5, -2.5, 'Koide K = 2/3',                '9.2 ppm',   BLUE),
        (5, -4,   'V_us = 9/40',                  '44 ppm',    GREEN),
        (5, -5.5, 'A_4 = -(13/8)K(0.995)/pi',     '12.5 ppm',  GOLD),
    ]

    for x, y, label, precision, color in predictions:
        # Prediction box
        ax.add_patch(FancyBboxPatch((x - 0.3, y - 0.45), 4.3, 0.9,
                                      boxstyle='round,pad=0.15',
                                      facecolor=BG, edgecolor=color,
                                      linewidth=1.5, zorder=5))
        ax.text(x + 0.1, y + 0.12, label, ha='left', va='center',
                 color=color, fontsize=10, fontweight='bold')
        ax.text(x + 0.1, y - 0.22, precision, ha='left', va='center',
                 color=SILVER, fontsize=8.5, fontstyle='italic')

    # Connection arrows (source -> prediction)
    connections = [
        # (source_alphabet, prediction_index, alpha)
        ('13',  0, 0.8),   # Omega_Lambda uses 13 via b_2'
        ('22',  0, 0.8),   # Omega_Lambda uses 22
        ('264', 0, 0.8),   # Omega_Lambda uses 264
        ('251', 0, 0.8),   # Omega_Lambda uses 251
        ('pi',  0, 0.6),   # Omega_Lambda uses pi

        ('pi',  1, 0.8),   # Omega_DM uses pi
        ('12',  1, 0.8),   # Omega_DM uses 12

        ('13',  2, 0.8),   # Omega_b uses 13
        ('264', 2, 0.8),   # Omega_b uses 264

        ('22',  3, 0.8),   # DM/b uses 22
        ('pi',  3, 0.6),   # DM/b uses pi
        ('13',  3, 0.6),   # DM/b uses 13

        ('12',  4, 0.8),   # H_0 uses 12
        ('11',  4, 0.8),   # H_0 uses 11

        ('3',   5, 0.7),   # Koide uses 3 (denominator)

        ('9',   6, 0.0),   # Koide... skip (9 not yet drawn)
        ('24',  6, 0.0),

        ('13',  7, 0.8),   # A_4 uses 13
        ('8',   7, 0.8),   # A_4 uses 8
        ('K(k)', 7, 0.8),  # A_4 uses K(k)
        ('pi',   7, 0.6),  # A_4 uses pi
    ]

    alphabet_xy = {label: (x, y) for x, y, label, _ in alphabet_nodes}

    for src_label, pred_idx, alpha in connections:
        if src_label not in alphabet_xy:
            continue
        if alpha == 0:
            continue
        src_x, src_y = alphabet_xy[src_label]
        pred_x, pred_y = predictions[pred_idx][0], predictions[pred_idx][1]
        pred_color = predictions[pred_idx][4]
        # Draw line from source edge to prediction edge
        ax.plot([src_x + 0.4, pred_x - 0.3], [src_y, pred_y],
                 color=pred_color, linewidth=0.8, alpha=alpha * 0.5, zorder=2)

    # Labels for regions
    ax.text(-6, 6, 'INTEGER ALPHABET\n+ transcendentals',
             ha='center', va='center', color=WHITE, fontsize=13, fontweight='bold')
    ax.text(7, 6.3, 'PRECISION PREDICTIONS\n(validated against measurement)',
             ha='center', va='center', color=WHITE, fontsize=13, fontweight='bold')

    # Framework summary
    ax.text(-7, -6.2,
             'Alphabet = prediction generator.\n'
             'Anything not expressible\nin this alphabet is NOT\na framework prediction.',
             ha='center', va='center', color=GOLD, fontsize=10,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=GOLD, linewidth=1.2))

    ax.text(7, -6.2,
             'Round 0: 4 precision reproductions\n'
             'Cross-derivation: 3 paths per value\n'
             'Integer 13 appears in 4 predictions\n'
             'across QED + cosmology + CKM',
             ha='center', va='center', color=SILVER, fontsize=9.5,
             bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                       edgecolor=SILVER, linewidth=1))

    # Title
    ax.set_title('The Integer Alphabet Generates Cross-Domain Predictions',
                  color=GOLD, fontsize=16, fontweight='bold', pad=15)

    save(fig, 'phys55_07_integer_alphabet_map.png')


# ================================================================
# FIG 8: MEASUREMENT AS CHANNEL-MERGER DOMINANCE
# Type: Progression/Sequence Diagram
# Shows: Three-panel time sequence - entangled pair, observer
#        forms merger, new merger dominates. Measurement problem
#        dissolves into channel-merger arithmetic.
# ================================================================

def fig8_measurement_merger_dominance():
    fig, axes = plt.subplots(1, 3, figsize=(18, 9),
                              gridspec_kw={'wspace': 0.20})

    panel_titles = ['t = 0: Entangled pair',
                    't = 1: Observer interacts',
                    't = 2: Merger dominates']

    for idx, ax in enumerate(axes):
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
        style_axes(ax, hide_spines=True)
        ax.set_title(panel_titles[idx], color=GOLD,
                      fontsize=12, fontweight='bold', pad=12)

    # ================ PANEL 1: ENTANGLED PAIR ================
    ax = axes[0]

    # Alice soliton (left)
    alice = Circle((-1.5, 0), 0.45, facecolor=CYAN, edgecolor=WHITE,
                    linewidth=2, zorder=4)
    ax.add_patch(alice)
    ax.text(-1.5, 0, 'A', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)

    # Bob soliton (right)
    bob = Circle((1.5, 0), 0.45, facecolor=CYAN, edgecolor=WHITE,
                  linewidth=2, zorder=4)
    ax.add_patch(bob)
    ax.text(1.5, 0, 'B', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)

    # Shared channel (merged structure) - wavy line between them
    t_ch = np.linspace(-1.05, 1.05, 100)
    y_ch = 0.15 * np.sin(t_ch * 6)
    ax.plot(t_ch, y_ch, color=GOLD, linewidth=3, alpha=0.85, zorder=3)
    ax.plot(t_ch, y_ch, color=GOLD, linewidth=6, alpha=0.25, zorder=2)  # glow

    # Label
    ax.text(0, 0.7, 'Shared channel\nsubstrate',
             ha='center', va='bottom', color=GOLD, fontsize=9, fontweight='bold')

    ax.text(0, -1.5, 'Alice and Bob share\nchannel substrate.\nOne pattern, two handles.',
             ha='center', va='center', color=WHITE, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=GOLD, linewidth=1))

    # ================ PANEL 2: OBSERVER INTERACTS ================
    ax = axes[1]

    # Alice (fading original entanglement)
    alice2 = Circle((-1.5, 0.8), 0.45, facecolor=CYAN, edgecolor=WHITE,
                     linewidth=2, zorder=4)
    ax.add_patch(alice2)
    ax.text(-1.5, 0.8, 'A', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)

    # Bob
    bob2 = Circle((1.5, 0), 0.45, facecolor=CYAN, edgecolor=WHITE,
                   linewidth=2, zorder=4)
    ax.add_patch(bob2)
    ax.text(1.5, 0, 'B', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)

    # Observer (new)
    obs = Circle((-1.5, -0.8), 0.45, facecolor=ORANGE, edgecolor=WHITE,
                  linewidth=2, zorder=4)
    ax.add_patch(obs)
    ax.text(-1.5, -0.8, 'O', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)

    # Original A-B channel (weakening)
    t_ch = np.linspace(-1.05, 1.05, 100)
    y_ch = 0.15 * np.sin(t_ch * 6) + 0.4  # midline between fading A and B
    ax.plot(t_ch, y_ch, color=GOLD, linewidth=2, alpha=0.4, zorder=3,
             linestyle='--')

    # New A-Observer channel (forming strong)
    y_start = 0.35
    y_end = -0.35
    t_ao = np.linspace(0, 1, 50)
    x_ao = np.ones_like(t_ao) * (-1.5) + 0.08 * np.sin(t_ao * 10)
    y_ao = y_start + (y_end - y_start) * t_ao
    ax.plot(x_ao, y_ao, color=MAG, linewidth=3, alpha=0.9, zorder=3)
    ax.plot(x_ao, y_ao, color=MAG, linewidth=7, alpha=0.3, zorder=2)  # glow

    ax.text(-0.6, 0.45, 'A-B channel\n(weakening)',
             ha='center', va='center', color=GOLD, fontsize=8,
             alpha=0.7, fontstyle='italic')
    ax.text(-0.5, -0.5, 'Observer-A\nchannel (forming)',
             ha='center', va='center', color=MAG, fontsize=8, fontweight='bold')

    ax.text(0, -1.9, 'Observer interacts with Alice.\nNew channel-merger forms.\nTwo mergers compete.',
             ha='center', va='center', color=WHITE, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=MAG, linewidth=1))

    # ================ PANEL 3: MERGER DOMINATES ================
    ax = axes[2]

    # Alice merged with Observer (now one merged pattern)
    # Draw as a single larger structure
    merged = FancyBboxPatch((-2.2, -1.2), 1.4, 1.4, boxstyle='round,pad=0.1',
                             facecolor=BG, edgecolor=MAG, linewidth=2.5, zorder=3)
    ax.add_patch(merged)
    # Alice
    alice3 = Circle((-1.75, -0.25), 0.35, facecolor=CYAN, edgecolor=WHITE,
                     linewidth=2, zorder=4)
    ax.add_patch(alice3)
    ax.text(-1.75, -0.25, 'A', ha='center', va='center',
             color=BG, fontsize=11, fontweight='bold', zorder=5)
    # Observer
    obs3 = Circle((-1.25, -0.85), 0.35, facecolor=ORANGE, edgecolor=WHITE,
                   linewidth=2, zorder=4)
    ax.add_patch(obs3)
    ax.text(-1.25, -0.85, 'O', ha='center', va='center',
             color=BG, fontsize=11, fontweight='bold', zorder=5)
    # Merger channel between A and O
    ax.plot([-1.75, -1.25], [-0.25, -0.85], color=MAG, linewidth=3, alpha=0.9, zorder=3)

    ax.text(-1.5, 0.25, 'MERGED', ha='center', va='bottom',
             color=MAG, fontsize=9, fontweight='bold')

    # Bob (now isolated - original channel dissolved)
    bob3 = Circle((1.5, 0), 0.45, facecolor=CYAN, edgecolor=WHITE,
                   linewidth=2, zorder=4)
    ax.add_patch(bob3)
    ax.text(1.5, 0, 'B', ha='center', va='center',
             color=BG, fontsize=14, fontweight='bold', zorder=5)
    ax.text(1.5, 0.7, 'State updated\nvia dissolved\nchannel',
             ha='center', va='bottom', color=CYAN, fontsize=8, fontweight='bold')

    # Dissolved A-B channel (ghost)
    t_ch = np.linspace(-1.05, 1.05, 50)
    y_ch = 0.15 * np.sin(t_ch * 6)
    # Fade out
    for alpha_g in [0.15, 0.08]:
        ax.plot(t_ch, y_ch, color=DIM, linewidth=1, alpha=alpha_g,
                 linestyle=':', zorder=1)

    ax.text(0, -1.9,
             'Observer-Alice merger dominates.\nOriginal A-B entanglement dissolves.\nBob state: updated via fading channel.',
             ha='center', va='center', color=WHITE, fontsize=9,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=MAG, linewidth=1))

    # Figure title
    fig.suptitle('Measurement as Channel-Merger Dominance: The Measurement Problem Dissolves',
                  color=GOLD, fontsize=16, fontweight='bold', y=1.00)

    fig.text(0.5, 0.02,
              'One dynamics: channel-merger arithmetic. What standard QM calls "collapse" is new merger outcompeting prior entanglement. '
              'No second dynamics needed. Observation-as-entanglement resolves Q3d.',
              ha='center', va='bottom', color=SILVER, fontsize=10, fontstyle='italic')

    save(fig, 'phys55_08_measurement_merger_dominance.png')


# ================================================================
# MAIN
# ================================================================

def main():
    print("Generating PHYS-55 diagrams...")
    print("Output directory: %s" % outdir)
    print("")
    fig1_unit_graph_adjacency()
    fig2_hierarchy_levels_scale()
    fig3_dual_geometry_scales()
    fig4_born_round_trip()
    fig5_mass_scaling_sectors()
    fig6_channel_agreement_double_slit()
    fig7_integer_alphabet_map()
    fig8_measurement_merger_dominance()
    print("")
    print("All 8 figures saved to ../figures/:")
    print("  phys55_01_unit_graph_adjacency.png")
    print("  phys55_02_hierarchy_levels_scale.png")
    print("  phys55_03_dual_geometry_scales.png")
    print("  phys55_04_born_round_trip.png")
    print("  phys55_05_mass_scaling_sectors.png")
    print("  phys55_06_channel_agreement_slit.png")
    print("  phys55_07_integer_alphabet_map.png")
    print("  phys55_08_measurement_merger_dominance.png")


if __name__ == '__main__':
    main()
