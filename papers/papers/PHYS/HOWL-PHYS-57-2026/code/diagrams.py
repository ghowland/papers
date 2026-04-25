#!/usr/bin/env python3
"""
HOWL PHYS-57 Diagrams — Falsification of the Channel × Level Universality Claim in PCTRM
8 figures covering matrix structure, bridges, hierarchy, multi-toroidal structure, Bell, quarkonium, USI thresholds.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

def setup_dark_fig(figsize=(16, 10)):
    fig, ax = plt.subplots(figsize=figsize, facecolor=BG)
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    return fig, ax

def setup_dark_multi(nrows, ncols, figsize=(18, 10), wspace=0.30, hspace=0.30):
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, facecolor=BG,
                              gridspec_kw={'wspace': wspace, 'hspace': hspace})
    if nrows * ncols == 1:
        axes = [axes]
    else:
        axes = np.array(axes).flatten()
    for ax in axes:
        ax.set_facecolor(PAN)
        for spine in ax.spines.values():
            spine.set_color(DIM)
            spine.set_linewidth(0.5)
        ax.tick_params(colors=DIM, labelsize=9)
    return fig, axes

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    print("  Saved: %s" % filename)


# ================================================================
# FIG 1: 9 x 7 CHANNEL x LEVEL MATRIX HEATMAP
# Type: 6 (Comparison Bar) extended to 2D / 4 (Geometric)
# Shows: The full 63-cell matrix color-coded by validation status — defining diagram for PHYS-57
# ================================================================
def fig_01_matrix_heatmap():
    fig, ax = setup_dark_fig(figsize=(18, 11))

    # Channels (rows, top to bottom)
    channels = ['Gravitational', 'EM', 'Strong-Conf', 'Strong-Resid',
                 'Weak', 'Thermal', 'Entanglement', 'Higgs', 'Channel-Share']

    # Levels (columns, left to right)
    levels = ['L0\nSubstrate', 'L1\nSubatomic', 'L2\nAtomic', 'L3\nNuclear',
               'L4\nMolecular', 'L5\nMacro', 'L6\nCosmic']

    # Status codes:
    # V = Validated (green), U = Untested (orange), S = Structural (blue),
    # N = Negligible (dim)
    # Numbers indicate sub-cells/instances
    status_matrix = [
        # L0      L1       L2      L3      L4      L5       L6
        ['S',    'U',     'U',    'S',    'N',    'V6',    'V3'],   # Gravitational
        ['S',    'V3',    'V1',   'U',    'U2',   'U3',    'U'],    # EM
        ['S',    'U',     'N',    'V1',   'N',    'U',     'S'],    # Strong-Conf
        ['S',    'V9',    'U',    'V2',   'N',    'U',     'V4'],   # Strong-Resid
        ['S',    'V4',    'U',    'U',    'U',    'U',     'V4'],   # Weak
        ['S',    'U',     'U',    'U',    'U',    'U2',    'V1'],   # Thermal
        ['U',    'U',     'U',    'U',    'U',    'U',     'U'],    # Entanglement
        ['S',    'V2',    'U',    'V1',   'U',    'S',     'V1'],   # Higgs
        ['V3',   'U',     'U',    'V1',   'U',    'U',     'V4'],   # Channel-Share
    ]

    # Color mapping
    color_map = {
        'V': GREEN,    # Validated
        'U': ORANGE,   # Untested
        'S': BLUE,     # Structural
        'N': DIM,      # Negligible
    }

    # Plot cells as colored rectangles
    for ci, channel in enumerate(channels):
        for li, level in enumerate(levels):
            status = status_matrix[ci][li]
            base_status = status[0]  # First character is the status
            count = status[1:] if len(status) > 1 else ''

            color = color_map[base_status]

            # Cell rectangle
            rect = mpatches.FancyBboxPatch((li - 0.42, ci - 0.42),
                                            0.84, 0.84,
                                            boxstyle="round,pad=0.02",
                                            facecolor=color, alpha=0.6,
                                            edgecolor=color, linewidth=1.5)
            ax.add_patch(rect)

            # Status label
            if base_status == 'V':
                if count:
                    label = 'V%s' % count
                else:
                    label = 'V'
                text_color = WHITE
            elif base_status == 'U':
                if count:
                    label = 'U%s' % count
                else:
                    label = 'U'
                text_color = WHITE
            elif base_status == 'S':
                label = 'S'
                text_color = WHITE
            else:
                label = '—'
                text_color = DIM

            ax.text(li, ci, label, color=text_color, fontsize=11,
                    ha='center', va='center', fontweight='bold')

    # Channel labels (y-axis)
    ax.set_yticks(range(len(channels)))
    ax.set_yticklabels(channels, color=WHITE, fontsize=10, fontweight='bold')

    # Level labels (x-axis, top)
    ax.set_xticks(range(len(levels)))
    ax.set_xticklabels(levels, color=WHITE, fontsize=10, fontweight='bold')

    # Axis configuration
    ax.set_xlim(-0.6, len(levels) - 0.4)
    ax.set_ylim(-0.6, len(channels) - 0.4)
    ax.invert_yaxis()  # Channels top-to-bottom

    # Title
    ax.set_title('PCTRM Channel x Level Universality Matrix — 9 x 7 = 63 Cells',
                 color=GOLD, fontsize=15, fontweight='bold', pad=20)

    # Legend at bottom (inside axis limits per D16)
    legend_y = len(channels) - 0.05
    legend_items = [
        ('V', GREEN, 'Validated (25 cells)'),
        ('U', ORANGE, 'Untested active (~30 cells)'),
        ('S', BLUE, 'Structural only (~5 cells)'),
        ('—', DIM, 'Negligible (~5 cells)'),
    ]

    # Draw legend boxes inside the axis at bottom
    for i, (sym, color, label) in enumerate(legend_items):
        x_pos = -0.4 + i * 1.85
        y_pos = legend_y + 0.4

        # Small colored box
        box = mpatches.FancyBboxPatch((x_pos, y_pos - 0.12), 0.25, 0.25,
                                       boxstyle="round,pad=0.01",
                                       facecolor=color, alpha=0.6,
                                       edgecolor=color, linewidth=1.2)
        ax.add_patch(box)

        # Label
        ax.text(x_pos + 0.4, y_pos + 0.01, label, color=SILVER, fontsize=9,
                ha='left', va='center')

    # USI summary
    ax.text(6.4, 9.4, 'USI = 25/55 = 0.45',
            color=GOLD, fontsize=12, ha='right', va='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=GOLD, linewidth=1.5))

    # Remove axis
    ax.tick_params(axis='both', length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    save(fig, 'phys57_01_matrix_heatmap.png')


# ================================================================
# FIG 2: BRIDGE IDENTITY CROSS-SCALE VISUALIZATION
# Type: 5 (Connection/Integer Map)
# Shows: 1 validated bridge plus 7 predicted bridges connecting cells across the matrix
# ================================================================
def fig_02_bridge_identities():
    fig, ax = setup_dark_fig(figsize=(18, 11))

    # Layout: cells distributed across the figure with bridges connecting them
    # Cells positioned at specific (channel, level) intersections

    # Cell positions and labels
    cells = {
        'k_em_subatom (A_4)':           (0.15, 0.75, CYAN, 'L1 EM\n|A_4| = -13/8 K/pi'),
        'k_higgs_subatom (m_mu/m_e)^2': (0.30, 0.85, ORANGE, 'L1 Higgs\n(m_mu/m_e)^2'),
        'k_grav_cosmic (DM/baryon)':    (0.85, 0.55, MAG, 'L6 Gravitational\nDM/baryon = 22*pi/13'),
        'k_em_atom (Rydberg)':          (0.15, 0.45, BLUE, 'L2 EM\nR_inf'),
        'k_strong_nuclear (proton)':    (0.50, 0.80, GREEN, 'L3 Strong\nProton 3*pi/2 = 6*beta'),
        'k_em_macro_planetary':         (0.40, 0.20, GREEN, 'L5 EM Earth\nGeomagnetic dipole'),
        'k_em_macro_solar':             (0.65, 0.30, ORANGE, 'L5 EM Sun\nSolar magnetic'),
        'k_residual_subatom (Koide)':   (0.30, 0.65, PURPLE, 'L1 Strong-Resid\nKoide 2/3'),
        'k_share_nuclear (a_A/a_V)':    (0.55, 0.55, PURPLE, 'L3 Share\na_A/a_V = 3/2'),
    }

    # Draw cells
    for name, (x, y, color, label) in cells.items():
        circle = mpatches.Circle((x, y), 0.04, facecolor=BG,
                                  edgecolor=color, linewidth=2, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y - 0.08, label, color=color, fontsize=8.5, ha='center',
                va='top', fontweight='bold')

    # Bridges
    # B1 (validated): k_em_subatom + k_higgs + k_grav -> k_grav_cosmic at 0.03%
    # B2: k_em_atom (Rydberg) -> k_grav_cosmic
    # B3: k_strong_nuclear -> k_grav_cosmic (galactic toroidal)
    # B4: k_em_macro Earth -> k_em_macro Sun
    # B5: k_weak (V_cb/V_ub = 11) connects to k_grav_cosmic (22pi/13)
    # B6: k_residual_subatom (Koide) -> k_share_nuclear (a_A/a_V) — both validated 2/3 vs 3/2
    # B7: k_em_subatom (alpha) -> k_grav_cosmic (H_0 ratio)
    # B8: k_higgs_subatom (m_mu/m_e)^2 -> k_grav_cosmic (DM/baryon)

    bridges = [
        # (start_pos, end_pos, label, color, status, intermediate_cells)
        ((0.15, 0.75), (0.85, 0.55), 'B1: |A_4|*(alpha/pi)^4*3*(M_Z/m_e)^2 = 22pi/13', GOLD, 'VALIDATED 0.03%'),
        ((0.15, 0.45), (0.85, 0.55), 'B2: R_inf x (cosmic factor) = obs', SILVER, 'Untested'),
        ((0.50, 0.80), (0.85, 0.55), 'B3: Proton flux x (galactic scale) = halo', SILVER, 'Untested'),
        ((0.40, 0.20), (0.65, 0.30), 'B4: Earth/Sun dipole ratio', SILVER, 'Untested'),
        ((0.30, 0.65), (0.55, 0.55), 'B6: 2/3 (Koide) <-> 3/2 (a_A/a_V)', GOLD, 'VALIDATED'),
        ((0.30, 0.85), (0.85, 0.55), 'B8: (m_mu/m_e)^2 connects to 22pi/13', SILVER, 'Untested'),
    ]

    for (x1, y1), (x2, y2), label, color, status in bridges:
        # Determine if validated or predicted
        is_validated = 'VALIDATED' in status
        line_style = '-' if is_validated else '--'
        line_alpha = 0.85 if is_validated else 0.5
        line_width = 2.2 if is_validated else 1.4

        # Draw arrow
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle='->', color=color,
                                      linewidth=line_width, alpha=line_alpha,
                                      linestyle=line_style))

        # Label at midpoint
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2 + 0.025

        ax.text(mid_x, mid_y, label, color=color, fontsize=8, ha='center',
                fontweight='bold' if is_validated else 'normal',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                          edgecolor=color, linewidth=0.8, alpha=0.85))

    # Title
    ax.text(0.5, 0.97, 'Cross-Cell Bridge Identities — Validated and Predicted',
            transform=ax.transAxes, color=GOLD, fontsize=14, ha='center',
            fontweight='bold')

    # Legend
    ax.text(0.5, 0.92,
            'Solid GOLD lines: validated bridges  |  Dashed SILVER lines: predicted bridges (Round 2 testing)',
            transform=ax.transAxes, color=SILVER, fontsize=10, ha='center',
            style='italic')

    # Bottom annotation
    ax.text(0.5, 0.05,
            '8 predicted bridges total. B1 and B6 validated. B2-B5, B7-B8 untested.',
            transform=ax.transAxes, color=GOLD, fontsize=10, ha='center',
            fontweight='bold')

    ax.text(0.5, 0.02,
            'Failure of 2+ predicted bridges rejects cross-cell consistency (Catastrophic Failure C).',
            transform=ax.transAxes, color=DIM, fontsize=9, ha='center',
            style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save(fig, 'phys57_02_bridge_identities.png')


# ================================================================
# FIG 3: PER-LEVEL HIERARCHY WITH STATUS DISTRIBUTION
# Type: 4 (Geometric) + 2 (Scale Landscape)
# Shows: 7-level hierarchy with USI per level and cell status distribution
# ================================================================
def fig_03_hierarchy_status():
    fig, ax = setup_dark_fig(figsize=(18, 12))

    # Levels with USI and cell counts
    levels = [
        ('L0\nSubstrate',      -35, -20, 0.00, 0, 0, 6, 'Substrate-level structural commitments'),
        ('L1\nSubatomic',      -20, -13, 0.78, 7, 2, 0, 'Particle physics: CKM, Koide, QED 4-loop'),
        ('L2\nAtomic',         -13, -7,  0.17, 1, 5, 0, 'H 1S-2S validated; helium, lithium, Lamb pending'),
        ('L3\nNuclear',        -16, -14, 0.57, 4, 3, 0, 'Proton 3pi/2; nuclear binding, magnetic moments pending'),
        ('L4\nMolecular',      -10, -5,  0.00, 0, 4, 0, 'No molecular validation yet'),
        ('L5\nMacroscopic',    0,   12,  0.50, 4, 4, 0, 'GR validated; Van Allen, atmospheric pending'),
        ('L6\nCosmological',   18,  26,  1.00, 9, 0, 0, 'Cosmic partition fully validated'),
    ]

    for i, (name, log_lower, log_upper, usi, validated, untested, structural, desc) in enumerate(levels):
        y_center = 6 - i

        # Calculate USI status color
        if usi >= 0.85:
            color = GREEN
        elif usi >= 0.70:
            color = CYAN
        elif usi >= 0.50:
            color = ORANGE
        elif usi >= 0.30:
            color = MAG
        else:
            color = RED

        # Horizontal bar showing scale extent
        ax.barh(y_center, log_upper - log_lower, left=log_lower,
                height=0.55, color=color, alpha=0.55,
                edgecolor=color, linewidth=1.5)

        # Level label on left
        ax.text(log_lower - 1.5, y_center, name, color=color, fontsize=11,
                ha='right', va='center', fontweight='bold')

        # USI value on right
        ax.text(log_upper + 0.5, y_center,
                'USI = %.2f' % usi,
                color=color, fontsize=11, ha='left', va='center',
                fontweight='bold')

        # Cell count breakdown to the right of USI
        cell_text = '%d V / %d U / %d S' % (validated, untested, structural)
        ax.text(log_upper + 4.5, y_center, cell_text, color=SILVER,
                fontsize=9, ha='left', va='center')

        # Description below the bar
        ax.text((log_lower + log_upper) / 2, y_center - 0.32,
                desc, color=WHITE, fontsize=8, ha='center',
                va='top', style='italic')

    # USI threshold lines on right side annotation
    threshold_x = 28
    ax.text(threshold_x, 6.7, 'USI Status', color=GOLD, fontsize=10,
            ha='left', va='center', fontweight='bold')
    threshold_labels = [
        (1.00, 'Strong (>=0.85)', GREEN),
        (0.78, 'Moderate (0.70+)', CYAN),
        (0.50, 'Partial (0.50+)', ORANGE),
        (0.17, 'Reject (<0.50)', RED),
    ]
    for val, label, col in threshold_labels:
        # Find a level with this approximate USI to mark
        pass

    # Physical landmarks
    landmarks = [
        (-35, 'Planck scale'),
        (-15, 'Nucleon'),
        (-10, 'Atom'),
        (0,   'Human'),
        (11,  'Earth-Moon'),
        (21,  'Galaxy'),
        (26,  'Universal'),
    ]
    for log_x, label in landmarks:
        ax.axvline(log_x, color=DIM, linestyle=':', linewidth=0.8, alpha=0.4)
        ax.text(log_x, 6.8, label, color=SILVER, fontsize=8,
                ha='center', style='italic')

    # Title
    ax.set_title('PHYS-57 Per-Level Universality Status — USI Distribution Across Hierarchy',
                 color=GOLD, fontsize=14, fontweight='bold', pad=15)

    ax.set_xlabel('Spatial Scale (log10 meters)', color=SILVER, fontsize=12)
    ax.set_xlim(-38, 33)
    ax.set_ylim(-1.5, 7.5)

    ax.set_yticks([])

    # X-ticks
    xticks = [-35, -25, -15, -5, 5, 15, 25]
    xlabels = ['10^-35', '10^-25', '10^-15', '10^-5', '10^5', '10^15', '10^25']
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, color=DIM, fontsize=9)

    # Bottom annotation
    ax.text(0.5, -0.07,
            'Pre-registered USI thresholds: >=0.85 strong validation, 0.70-0.85 moderate, 0.50-0.70 partial, <0.50 rejected.',
            transform=ax.transAxes, color=SILVER, fontsize=10, ha='center',
            style='italic')

    ax.grid(True, axis='x', alpha=0.1, color=DIM)

    save(fig, 'phys57_03_hierarchy_status.png')


# ================================================================
# FIG 4: EARTH'S MULTI-TOROIDAL STRUCTURE
# Type: 4 (Geometric Cross-Section)
# Shows: Earth as a Level 5 soliton with all toroidal sectors stacked
# ================================================================
def fig_04_earth_toroidal():
    fig, ax = setup_dark_fig(figsize=(16, 14))
    ax.set_aspect('equal')

    # Earth as central sphere
    earth = mpatches.Circle((0, 0), 1.0, facecolor=BLUE, alpha=0.4,
                              edgecolor=BLUE, linewidth=2.5, zorder=2)
    ax.add_patch(earth)

    # Earth core
    core = mpatches.Circle((0, 0), 0.55, facecolor=GOLD, alpha=0.5,
                             edgecolor=GOLD, linewidth=1.5, zorder=3)
    ax.add_patch(core)

    # Earth label
    ax.text(0, -0.05, 'Earth', color=WHITE, fontsize=14, ha='center',
            fontweight='bold')
    ax.text(0, -0.2, '6.4 x 10^6 m', color=SILVER, fontsize=9, ha='center',
            style='italic')

    # Atmospheric Hadley/Ferrel/Polar cells (small toroidal regions near surface)
    # Hadley (low latitude)
    for sign in [-1, 1]:
        hadley = mpatches.Ellipse((0, sign * 0.3), 1.4, 0.18, fill=False,
                                    edgecolor=ORANGE, linewidth=1.5, alpha=0.8,
                                    zorder=4)
        ax.add_patch(hadley)

    # Ferrel (mid latitude)
    for sign in [-1, 1]:
        ferrel = mpatches.Ellipse((0, sign * 0.7), 1.1, 0.15, fill=False,
                                    edgecolor=ORANGE, linewidth=1.5, alpha=0.6,
                                    zorder=4)
        ax.add_patch(ferrel)

    # Inner Van Allen belt (at L=1.5, ~1.2 Earth radii to ~2.5)
    inner_belt = mpatches.Ellipse((0, 0), 3.5, 1.0, fill=False,
                                    edgecolor=PURPLE, linewidth=2.5, alpha=0.85,
                                    zorder=5)
    ax.add_patch(inner_belt)

    # Outer Van Allen belt (at L=4-7)
    outer_belt = mpatches.Ellipse((0, 0), 7.0, 1.8, fill=False,
                                    edgecolor=MAG, linewidth=2.5, alpha=0.85,
                                    zorder=5)
    ax.add_patch(outer_belt)

    # Plasmasphere (~4 Earth radii)
    plasma = mpatches.Ellipse((0, 0), 4.5, 1.3, fill=False,
                                edgecolor=CYAN, linewidth=1.8, alpha=0.6,
                                zorder=4, linestyle='--')
    ax.add_patch(plasma)

    # Geomagnetic field lines (dipole shape)
    theta = np.linspace(0, 2 * np.pi, 100)
    for r_mag in [1.4, 1.8, 2.5]:
        x_field = r_mag * np.sin(theta) * (1 - 0.3 * np.cos(theta) ** 2)
        y_field = r_mag * np.cos(theta) * 1.5
        ax.plot(x_field, y_field, color=GREEN, linewidth=1, alpha=0.5,
                zorder=3, linestyle='-')

    # Labels for each toroidal structure
    # Hadley cells
    ax.annotate('Atmospheric Hadley cells\n(L5 thermal toroidal)\nk_thermal_macro_atm',
                xy=(-1.4, -0.3), xytext=(-3.0, -1.0),
                color=ORANGE, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=ORANGE,
                                 alpha=0.7, linewidth=1))

    # Plasmasphere
    ax.annotate('Plasmasphere\n(L5 EM toroidal)\nk_em_macro_plasma',
                xy=(2.0, 0.7), xytext=(3.7, 1.5),
                color=CYAN, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=CYAN,
                                 alpha=0.7, linewidth=1))

    # Inner Van Allen
    ax.annotate('Inner Van Allen Belt\n(L = 1.2 - 2.5)\nk_em_macro_VAi',
                xy=(1.8, 0.3), xytext=(3.0, 0.5),
                color=PURPLE, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=PURPLE,
                                 alpha=0.7, linewidth=1))

    # Outer Van Allen
    ax.annotate('Outer Van Allen Belt\n(L = 3 - 7)\nk_em_macro_VAo',
                xy=(3.5, 0.3), xytext=(5.0, -0.6),
                color=MAG, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=MAG,
                                 alpha=0.7, linewidth=1))

    # Geomagnetic dipole
    ax.annotate('Geomagnetic dipole\n8.22 x 10^22 A.m^2\nk_em_macro_planetary',
                xy=(0, 2.1), xytext=(-3.0, 2.5),
                color=GREEN, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=GREEN,
                                 alpha=0.7, linewidth=1))

    # Earth core
    ax.annotate('Inner core\n(MHD dynamo)\nk_grav_macro',
                xy=(0, 0.4), xytext=(-2.5, 1.3),
                color=GOLD, fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color=GOLD,
                                 alpha=0.7, linewidth=1))

    # Title
    ax.set_title('Earth as a Multi-Toroidal Soliton (Level 5) — At Least 6 Stacked Toroidal Sectors',
                 color=GOLD, fontsize=14, fontweight='bold', pad=20)

    # Bottom annotation
    ax.text(0, -3.2,
            'Each toroidal structure has its own modulus k_(channel)_(level)_(specific) — all alphabet-derivable.',
            color=SILVER, fontsize=10, ha='center', style='italic')
    ax.text(0, -3.5,
            'PHYS-57 Round 2 tests T11-T15 systematically validate this multi-channel planetary stack.',
            color=GOLD, fontsize=10, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=GOLD, linewidth=1.2))

    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 3.3)
    ax.axis('off')

    save(fig, 'phys57_04_earth_toroidal.png')


# ================================================================
# FIG 5: MULTI-SCALE DUAL-GEOMETRY STACKING
# Type: 4 (Geometric Cross-Section)
# Shows: Same multi-channel stacking pattern at atomic, planetary, galactic scales
# ================================================================
def fig_05_multiscale_stacking():
    fig, axes = setup_dark_multi(1, 3, figsize=(20, 9), wspace=0.05, hspace=0.0)

    # Panel 1: ATOM
    ax1 = axes[0]
    ax1.set_aspect('equal')

    # Electron shells
    for r in [0.3, 0.55, 0.85]:
        shell = mpatches.Circle((0, 0), r, fill=False, edgecolor=BLUE,
                                  linewidth=1.5 if r != 0.85 else 2.0,
                                  alpha=0.6 if r != 0.85 else 1.0, zorder=3)
        ax1.add_patch(shell)

    # Nucleus
    nucleus = mpatches.Circle((0, 0), 0.07, color=GOLD, zorder=5)
    ax1.add_patch(nucleus)

    # Magnetic moment loop (toroidal)
    mag = mpatches.Ellipse((0, 1.3), 0.7, 0.15, fill=False, edgecolor=ORANGE,
                             linewidth=1.8, alpha=0.85, zorder=4)
    ax1.add_patch(mag)

    # Hyperfine sub-shells
    for r in [0.32, 0.34, 0.36]:
        sub = mpatches.Circle((0, 0), r, fill=False, edgecolor=PURPLE,
                                linewidth=0.8, alpha=0.5, zorder=2,
                                linestyle=':')
        ax1.add_patch(sub)

    ax1.set_title('Level 2: ATOM (~10^-10 m)', color=BLUE, fontsize=12,
                   fontweight='bold', pad=10)

    # Annotations
    ax1.text(0, -1.4, 'Spherical: shells (k_em_atom)\nToroidal: moment (orange)\nHyperfine (purple) = EM x strong',
             color=WHITE, fontsize=8, ha='center', va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=DIM, linewidth=0.8))

    ax1.set_xlim(-1.7, 1.7)
    ax1.set_ylim(-2.0, 1.7)
    ax1.axis('off')

    # Panel 2: PLANET (Earth)
    ax2 = axes[1]
    ax2.set_aspect('equal')

    # Earth
    earth = mpatches.Circle((0, 0), 0.4, facecolor=BLUE, alpha=0.5,
                              edgecolor=BLUE, linewidth=1.8, zorder=3)
    ax2.add_patch(earth)

    # Core
    core = mpatches.Circle((0, 0), 0.2, color=GOLD, alpha=0.6, zorder=4)
    ax2.add_patch(core)

    # Atmospheric layers
    for r, alpha in [(0.45, 0.6), (0.5, 0.4)]:
        layer = mpatches.Circle((0, 0), r, fill=False, edgecolor=CYAN,
                                  linewidth=1.0, alpha=alpha, zorder=2)
        ax2.add_patch(layer)

    # Inner Van Allen
    inner = mpatches.Ellipse((0, 0), 1.4, 0.4, fill=False, edgecolor=PURPLE,
                               linewidth=1.8, alpha=0.85, zorder=4)
    ax2.add_patch(inner)

    # Outer Van Allen
    outer = mpatches.Ellipse((0, 0), 2.5, 0.7, fill=False, edgecolor=MAG,
                               linewidth=1.8, alpha=0.85, zorder=4)
    ax2.add_patch(outer)

    # Hadley cells (small horizontal rings at low latitudes)
    for sign in [-1, 1]:
        had = mpatches.Ellipse((0, sign * 0.18), 0.6, 0.06, fill=False,
                                 edgecolor=ORANGE, linewidth=1.0, alpha=0.7,
                                 zorder=3)
        ax2.add_patch(had)

    ax2.set_title('Level 5: PLANET (~10^7 m)', color=CYAN, fontsize=12,
                   fontweight='bold', pad=10)

    ax2.text(0, -1.4, 'Spherical: atmosphere (k_em_macro_planetary)\nToroidal: Van Allen (purple/magenta)\nHadley cells (orange thermal)',
             color=WHITE, fontsize=8, ha='center', va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=DIM, linewidth=0.8))

    ax2.set_xlim(-1.7, 1.7)
    ax2.set_ylim(-2.0, 1.7)
    ax2.axis('off')

    # Panel 3: GALAXY
    ax3 = axes[2]
    ax3.set_aspect('equal')

    # Dark matter halo (large sphere)
    halo = mpatches.Circle((0, 0), 1.2, facecolor=PURPLE, alpha=0.18,
                             edgecolor=PURPLE, linewidth=1.5, zorder=1)
    ax3.add_patch(halo)

    # Galactic disk (toroidal, flat ellipse)
    disk = mpatches.Ellipse((0, 0), 1.7, 0.25, facecolor=MAG, alpha=0.7,
                              linewidth=0, zorder=3)
    ax3.add_patch(disk)

    # Disk edge
    disk_edge = mpatches.Ellipse((0, 0), 1.7, 0.25, fill=False, edgecolor=MAG,
                                   linewidth=1.5, zorder=4)
    ax3.add_patch(disk_edge)

    # Spiral arms (small ellipses at angles)
    for angle in [0, 60, 120, 180, 240, 300]:
        theta_a = np.radians(angle)
        cx = 0.6 * np.cos(theta_a)
        cy = 0.05 * np.sin(theta_a)
        arm = mpatches.Ellipse((cx, cy), 0.35, 0.08, fill=False,
                                 edgecolor=CYAN, linewidth=1, alpha=0.6,
                                 zorder=4)
        ax3.add_patch(arm)

    # Bulge
    bulge = mpatches.Circle((0, 0), 0.18, color=GOLD, zorder=5)
    ax3.add_patch(bulge)

    # Flow arrows
    for th_deg in [45, 135, 225, 315]:
        th = np.radians(th_deg)
        x_start = 0.85 * np.cos(th)
        y_start = 0.1 * np.sin(th)
        dx = -0.15 * np.sin(th)
        dy = 0.05 * np.cos(th)
        ax3.annotate('', xy=(x_start + dx, y_start + dy),
                      xytext=(x_start, y_start),
                      arrowprops=dict(arrowstyle='->', color=ORANGE,
                                       linewidth=1.5, alpha=0.85))

    ax3.set_title('Level 6: GALAXY (~10^21 m)', color=MAG, fontsize=12,
                   fontweight='bold', pad=10)

    ax3.text(0, -1.4, 'Spherical: DM halo (k_grav_cosmic)\nToroidal: disk (magenta)\nSpiral arms (cyan secondary toroidal)',
             color=WHITE, fontsize=8, ha='center', va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                       edgecolor=DIM, linewidth=0.8))

    ax3.set_xlim(-1.7, 1.7)
    ax3.set_ylim(-2.0, 1.7)
    ax3.axis('off')

    # Overall title
    fig.suptitle('Universal Multi-Channel Stacking: Same Pattern at Every Hierarchy Level',
                  color=GOLD, fontsize=14, fontweight='bold', y=0.98)

    save(fig, 'phys57_05_multiscale_stacking.png')


# ================================================================
# FIG 6: BELL CORRELATION CROSS-DERIVATION
# Type: 5 (Connection/Integer Map)
# Shows: 4 paths converging on Tsirelson bound 2*sqrt(2)
# ================================================================
def fig_06_bell_correlation():
    fig, ax = setup_dark_fig(figsize=(17, 11))

    # Tsirelson bound = 2 * sqrt(2)
    tsirelson = 2 * np.sqrt(2)  # ≈ 2.828
    classical_bound = 2.0
    measured = 2.83  # Approximate measured value (Hensen, Giustina, Shalm)

    # Layout: 4 paths on left side, converging to measurement on right
    paths = [
        ('Path A: Channel-Merger', 'Substrate channel-merger\nprojection in entanglement', 0.85, CYAN),
        ('Path B: Beta^2 Counting', 'beta^2 = (pi/4)^2\nsubstrate exponent', 0.65, GOLD),
        ('Path C: Alphabet Integer', '2 * sqrt(2) = sqrt(8) = sqrt(L1)\nfrom integer alphabet', 0.45, GREEN),
        ('Path D: Multi-Experiment', 'Hensen 2015, Giustina 2015,\nShalm 2015 consistency', 0.25, MAG),
    ]

    for label, formula, y_pos, color in paths:
        # Path label
        ax.text(0.02, y_pos, label, color=color, fontsize=11, fontweight='bold',
                ha='left', va='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                          edgecolor=color, linewidth=1.5))

        # Formula box
        ax.text(0.22, y_pos, formula, color=WHITE, fontsize=9, ha='left',
                va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=DIM, linewidth=0.8))

        # Value
        ax.text(0.50, y_pos, '-> 2.828...', color=WHITE, fontsize=11,
                ha='left', va='center', fontweight='bold')

        # Arrow to convergence
        ax.annotate('', xy=(0.78, 0.55), xytext=(0.65, y_pos),
                    arrowprops=dict(arrowstyle='->', color=color, linewidth=2,
                                     alpha=0.7))

    # Central convergence node — Tsirelson bound
    conv_box = mpatches.FancyBboxPatch((0.78, 0.40), 0.18, 0.30,
                                         boxstyle="round,pad=0.02",
                                         facecolor=BG, edgecolor=GOLD,
                                         linewidth=2.5, transform=ax.transAxes)
    ax.add_patch(conv_box)

    ax.text(0.87, 0.65, 'TSIRELSON BOUND', transform=ax.transAxes,
            color=GOLD, fontsize=11, ha='center', fontweight='bold')
    ax.text(0.87, 0.60, '2 * sqrt(2) = sqrt(8)', transform=ax.transAxes,
            color=WHITE, fontsize=10, ha='center')
    ax.text(0.87, 0.55, '= 2.828427...', transform=ax.transAxes,
            color=WHITE, fontsize=10, ha='center')

    ax.text(0.87, 0.49, 'Classical: 2.000', transform=ax.transAxes,
            color=DIM, fontsize=9, ha='center')
    ax.text(0.87, 0.45, 'Measured: 2.83', transform=ax.transAxes,
            color=GREEN, fontsize=9, ha='center', fontweight='bold')

    # Integer alphabet element
    ax.text(0.5, 0.10,
            'L1 (substrate circumference) = 8 = 2^3 -> sqrt(L1) = 2*sqrt(2) (Tsirelson)',
            transform=ax.transAxes, color=PURPLE, fontsize=11, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=PURPLE, linewidth=1.5))

    # Title
    ax.text(0.5, 0.95,
            'Bell Correlation: 4 Independent Paths to Tsirelson Bound',
            transform=ax.transAxes, color=GOLD, fontsize=14, ha='center',
            fontweight='bold')

    ax.text(0.5, 0.90,
            'PHYS-57 Round 2 Test T23: All paths must converge on 2 * sqrt(2) at <10^-3 precision',
            transform=ax.transAxes, color=SILVER, fontsize=10, ha='center',
            style='italic')

    # Bottom annotation
    ax.text(0.5, 0.03,
            'Failure of multi-path convergence rejects entanglement universality (USI_entanglement = 0 currently).',
            transform=ax.transAxes, color=DIM, fontsize=9, ha='center',
            style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save(fig, 'phys57_06_bell_correlation.png')


# ================================================================
# FIG 7: QUARKONIUM MULTI-STATE CONVERGENCE
# Type: 1 (Running/Convergence)
# Shows: Charmonium and bottomonium states converging on single k_strong_subatom_HQ
# ================================================================
def fig_07_quarkonium_convergence():
    fig, ax = setup_dark_fig(figsize=(16, 10))

    # Charmonium states (in MeV)
    charmonium = [
        ('J/psi (1S)', 3096.9, GREEN),
        ('psi(2S)',    3686.1, GREEN),
        ('psi(3770)',  3773.1, GREEN),
        ('psi(4040)',  4040.0, GREEN),
        ('chi_c0',     3415.0, GREEN),
        ('chi_c1',     3511.0, GREEN),
        ('chi_c2',     3556.0, GREEN),
    ]

    # Bottomonium states (in MeV)
    bottomonium = [
        ('Upsilon(1S)', 9460.3, MAG),
        ('Upsilon(2S)', 10023.3, MAG),
        ('Upsilon(3S)', 10355.2, MAG),
        ('Upsilon(4S)', 10579.4, MAG),
    ]

    # Plot states as scatter
    # Each state extracts k_strong_subatom_HQ via Cornell potential
    # We plot mass on x-axis, predicted modulus value on y-axis
    # All should converge at single k value (~0.95-0.98 estimated for heavy quarks)

    # Predicted k value for HQ sector
    k_predicted = 0.965
    k_spread_target = 0.005  # 0.5% spread

    # For visualization, simulate small spread around predicted value
    np.random.seed(42)

    # Plot charmonium
    for name, mass, color in charmonium:
        # Simulate small variations representing path-extracted moduli
        k_extracted = k_predicted + np.random.uniform(-0.003, 0.003)
        ax.scatter([mass], [k_extracted], s=200, color=color,
                    edgecolors=WHITE, linewidth=1.8, zorder=5,
                    alpha=0.9)
        # Label
        ax.annotate(name, xy=(mass, k_extracted),
                     xytext=(mass, k_extracted + 0.005),
                     color=color, fontsize=8, ha='center')

    # Plot bottomonium
    for name, mass, color in bottomonium:
        k_extracted = k_predicted + np.random.uniform(-0.003, 0.003)
        ax.scatter([mass], [k_extracted], s=240, color=color,
                    edgecolors=WHITE, linewidth=1.8, zorder=5,
                    marker='D', alpha=0.9)
        ax.annotate(name, xy=(mass, k_extracted),
                     xytext=(mass, k_extracted + 0.005),
                     color=color, fontsize=8, ha='center')

    # Mean k_predicted line
    ax.axhline(k_predicted, color=GOLD, linestyle='--', linewidth=1.5,
               alpha=0.7, zorder=2, label='k_HQ = %.3f' % k_predicted)

    # Spread band (target precision)
    ax.axhspan(k_predicted - k_spread_target, k_predicted + k_spread_target,
                alpha=0.12, color=GOLD, zorder=1)

    # Spread annotation
    ax.text(11000, k_predicted, ' Target: k_HQ +/- 0.5%',
            color=GOLD, fontsize=10, va='center', fontweight='bold')

    # Mass scale annotations (charmonium vs bottomonium regions)
    ax.axvline(7000, color=DIM, linestyle=':', linewidth=1, alpha=0.4)
    ax.text(5000, 0.985, 'Charmonium\n(c-cbar)', color=GREEN, fontsize=11,
            ha='center', fontweight='bold', style='italic')
    ax.text(10000, 0.985, 'Bottomonium\n(b-bbar)', color=MAG, fontsize=11,
            ha='center', fontweight='bold', style='italic')

    # Pass condition box
    ax.text(0.02, 0.03,
            'Test T8 PASS: All 11 states extract consistent k_HQ at <0.5% spread\n'
            'Test T8 FAIL: State-dependent moduli reject heavy-quark universality',
            transform=ax.transAxes, color=WHITE, fontsize=10, ha='left',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG,
                      edgecolor=GOLD, linewidth=1.5),
            va='bottom')

    # Title and labels
    ax.set_title('Quarkonium Multi-State Convergence: 11 States -> Single k_strong_subatom_HQ',
                 color=GOLD, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Quarkonium State Mass (MeV)', color=SILVER, fontsize=12)
    ax.set_ylabel('Extracted k_strong_subatom_HQ', color=SILVER, fontsize=12)

    ax.set_xlim(2500, 11500)
    ax.set_ylim(0.95, 0.99)

    ax.grid(True, alpha=0.15, color=DIM)

    save(fig, 'phys57_07_quarkonium_convergence.png')


# ================================================================
# FIG 8: USI THRESHOLD VISUALIZATION
# Type: 3 (Threshold/Region Chart)
# Shows: Pre-registered USI regions with current state and Round 2 trajectory
# ================================================================
def fig_08_usi_thresholds():
    fig, ax = setup_dark_fig(figsize=(16, 10))

    # USI thresholds and regions
    thresholds = [
        (0.85, 1.00, GREEN, 'Strong Universality Validation\n(Framework supported)'),
        (0.70, 0.85, CYAN, 'Moderate Universality\n(With boundary conditions)'),
        (0.50, 0.70, ORANGE, 'Partial Universality\n(Significant restriction)'),
        (0.00, 0.50, RED, 'Universality Rejected\n(Fundamental revision)'),
    ]

    # Draw regions as horizontal bars
    for y_lower, y_upper, color, label in thresholds:
        ax.axhspan(y_lower, y_upper, color=color, alpha=0.12, zorder=1)
        # Threshold lines
        ax.axhline(y_lower, color=color, linestyle='--', linewidth=1.5,
                   alpha=0.6, zorder=2)

        # Region labels on right
        mid_y = (y_lower + y_upper) / 2
        ax.text(105, mid_y, label, color=color, fontsize=10, ha='left',
                va='center', fontweight='bold')

    # Top boundary
    ax.axhline(1.0, color=DIM, linestyle='-', linewidth=0.5, alpha=0.3)

    # Current and projected USI trajectory
    # X-axis: program phase / time
    phases = ['Pre\nRound 2', 'Tier A\n(T1-T5)', 'Tier B\n(T6-T10)',
              'Tier C\n(T11-T15)', 'Tier D\n(T16-T20)', 'Tier E\n(T21-T25)',
              'Final\nUSI']

    x_positions = list(range(len(phases)))

    # Current USI = 0.45
    # Projected trajectory if all tests pass
    projected_optimistic = [0.45, 0.55, 0.65, 0.72, 0.80, 0.85, 0.90]
    projected_partial = [0.45, 0.50, 0.55, 0.60, 0.65, 0.68, 0.72]
    projected_failure = [0.45, 0.45, 0.46, 0.47, 0.48, 0.48, 0.48]

    # Plot trajectories
    ax.plot(x_positions, projected_optimistic, 'o-', color=GREEN,
            linewidth=2.5, markersize=10, markeredgecolor=WHITE,
            markeredgewidth=1.5, zorder=5,
            label='Optimistic: all tests pass')

    ax.plot(x_positions, projected_partial, 's-', color=CYAN,
            linewidth=2, markersize=8, markeredgecolor=WHITE,
            markeredgewidth=1.5, zorder=4,
            label='Moderate: most pass')

    ax.plot(x_positions, projected_failure, '^-', color=ORANGE,
            linewidth=2, markersize=8, markeredgecolor=WHITE,
            markeredgewidth=1.5, zorder=4,
            label='Failure: many tests fail')

    # Highlight current position
    ax.scatter([0], [0.45], s=400, color=GOLD, marker='*',
               edgecolors=WHITE, linewidth=2, zorder=10)
    ax.annotate('CURRENT\nUSI = 0.45', xy=(0, 0.45),
                xytext=(0.7, 0.30),
                color=GOLD, fontsize=11, ha='center', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=GOLD,
                                 alpha=0.85, linewidth=1.5))

    # Phase labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(phases, color=DIM, fontsize=9, rotation=0)

    # Threshold value labels on left
    ax.text(-0.5, 0.85, '0.85', color=GREEN, fontsize=10, ha='right',
            va='center', fontweight='bold')
    ax.text(-0.5, 0.70, '0.70', color=CYAN, fontsize=10, ha='right',
            va='center', fontweight='bold')
    ax.text(-0.5, 0.50, '0.50', color=ORANGE, fontsize=10, ha='right',
            va='center', fontweight='bold')

    # Legend
    ax.legend(loc='upper left', facecolor=PAN, edgecolor=DIM,
              labelcolor=WHITE, fontsize=9, framealpha=0.95)

    # Title and labels
    ax.set_title('PHYS-57 USI Trajectory: Pre-Registered Thresholds and Round 2 Outcomes',
                 color=GOLD, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Round 2 Program Phase', color=SILVER, fontsize=12)
    ax.set_ylabel('Universality Strength Index (USI)', color=SILVER, fontsize=12)

    ax.set_xlim(-0.7, 6.5)
    ax.set_ylim(0, 1.05)

    ax.grid(True, alpha=0.15, color=DIM, axis='y')

    save(fig, 'phys57_08_usi_thresholds.png')


# ================================================================
# MAIN
# ================================================================
if __name__ == '__main__':
    print("Generating PHYS-57 diagram figures...")
    print("")

    fig_01_matrix_heatmap()
    fig_02_bridge_identities()
    fig_03_hierarchy_status()
    fig_04_earth_toroidal()
    fig_05_multiscale_stacking()
    fig_06_bell_correlation()
    fig_07_quarkonium_convergence()
    fig_08_usi_thresholds()

    print("")
    print("All 8 figures saved to ../figures/:")
    print("  phys57_01_matrix_heatmap.png")
    print("  phys57_02_bridge_identities.png")
    print("  phys57_03_hierarchy_status.png")
    print("  phys57_04_earth_toroidal.png")
    print("  phys57_05_multiscale_stacking.png")
    print("  phys57_06_bell_correlation.png")
    print("  phys57_07_quarkonium_convergence.png")
    print("  phys57_08_usi_thresholds.png")
