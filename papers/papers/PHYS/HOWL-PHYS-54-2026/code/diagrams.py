#!/usr/bin/env python3
"""
HOWL PHYS-54 Diagrams — The PCTRM Program
8 figures covering the falsification program specification.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, Wedge, Arc, Ellipse, FancyArrowPatch, Rectangle
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

def setup_ax(ax):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_edgecolor(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    ax.grid(True, alpha=0.1, color=DIM, linewidth=0.5)

def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)

# ================================================================
# FIG 1: THE SOLITON HIERARCHY SCALE LANDSCAPE
# Type: Scale/Landscape (Type 2)
# Shows: 45 orders of magnitude with six test levels highlighted
# ================================================================

def fig1_hierarchy_levels():
    fig, ax = plt.subplots(figsize=(16, 12))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    levels = [
        (0,  -18, "Quark / lepton",           "Level 0",  "Higgs + gauge",           True,  1),
        (1,  -15, "Nucleon",                  "Level 1",  "Strong (confinement)",    True,  1),
        (2,  -15, "Nucleus",                  "Level 2",  "Strong",                  False, None),
        (3,  -10, "Atom",                     "Level 3",  "EM (shells)",             True,  2),
        (4,  -9,  "Molecule",                 "Level 4",  "EM (chemical)",           True,  4),
        (5,  -1,  "Macroscopic object",       "Level 5",  "EM + gravitational",      True,  5),
        (6,   7,  "Planet",                   "Level 6",  "Gravitational + EM",      False, None),
        (7,   9,  "Star",                     "Level 7",  "Gravitational + fusion",  False, None),
        (8,   12, "Stellar system",           "Level 8",  "Gravitational",           False, None),
        (9,   21, "Galaxy",                   "Level 9",  "Grav + disk structure",   False, None),
        (10,  23, "Galaxy cluster",           "Level 10", "Gravitational",           False, None),
        (11,  24, "Supercluster",             "Level 11", "Gravitational",           False, None),
        (12,  27, "Observable universe",      "Level 12", "All at universal scale",  True,  6),
    ]

    ax.set_xlim(-22, 30)
    ax.set_ylim(-1, 14)

    # Main scale axis (horizontal log axis at y=1)
    for exp in range(-20, 30, 2):
        ax.axvline(x=exp, ymin=0.05, ymax=0.08, color=DIM, linewidth=0.5, alpha=0.5)

    # Main horizontal scale line
    ax.plot([-20, 28], [1, 1], color=SILVER, linewidth=1.5, alpha=0.7)
    # Labels at major landmarks on the axis
    for exp in [-18, -15, -10, -5, 0, 5, 10, 15, 20, 25]:
        ax.text(exp, 0.55, "10$^{%d}$ m" % exp, color=DIM, fontsize=8,
                ha='center', va='center')

    # Plot each hierarchy level as a marker at its scale
    for level_num, scale_exp, name, level_label, channels, is_test, test_num in levels:
        y_pos = 2 + level_num * 0.85

        # Line from scale axis to the level
        ax.plot([scale_exp, scale_exp], [1, y_pos], color=DIM, linewidth=0.8,
                alpha=0.5, linestyle=':')

        # Level marker
        if is_test:
            # Test level: GOLD filled
            color_fill = GOLD
            color_edge = WHITE
            box_color = GOLD
            alpha_fill = 0.3
            text_color = GOLD
        else:
            color_fill = PAN
            color_edge = DIM
            box_color = SILVER
            alpha_fill = 0.2
            text_color = SILVER

        # Marker
        ax.scatter([scale_exp], [y_pos], s=180, c=color_fill,
                   edgecolors=color_edge, linewidth=1.8, zorder=5)

        # Box with info to the side
        if scale_exp < 5:
            x_text = scale_exp + 1
            ha = 'left'
        else:
            x_text = scale_exp - 1
            ha = 'right'

        # Level name and scale
        ax.text(x_text, y_pos, name, color=WHITE, fontsize=10,
                ha=ha, va='center', fontweight='bold')
        ax.text(x_text, y_pos - 0.3, level_label, color=text_color, fontsize=8,
                ha=ha, va='center')

        # For test levels: show "TEST N" badge
        if is_test:
            badge_x = x_text + (4 if ha == 'left' else -4)
            ax.text(badge_x, y_pos, "TEST %d" % test_num, color=BG, fontsize=8,
                    ha='center', va='center', fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor=GOLD, edgecolor=GOLD))

    # Title
    ax.text(4, 13.3, "The Soliton Hierarchy: 45 Orders of Magnitude, Six Test Levels",
            color=GOLD, fontsize=15, ha='center', va='center', fontweight='bold')

    # Subtitle
    ax.text(4, 12.7, "PCTRM Falsification Program spans from Level 0 (10$^{-18}$ m) to Level 12 (10$^{27}$ m)",
            color=SILVER, fontsize=10, ha='center', va='center')

    # Legend
    legend_x = -18
    legend_y = 12.5
    ax.scatter([legend_x], [legend_y], s=180, c=GOLD, edgecolors=WHITE, linewidth=1.8)
    ax.text(legend_x + 1.2, legend_y, "Test level (1-6)", color=GOLD, fontsize=9,
            ha='left', va='center')
    ax.scatter([legend_x], [legend_y - 0.7], s=180, c=PAN, edgecolors=DIM, linewidth=1.8)
    ax.text(legend_x + 1.2, legend_y - 0.7, "Intermediate level", color=SILVER, fontsize=9,
            ha='left', va='center')

    # Bottom note
    ax.text(4, 0.0, "The six PCTRM test levels span from subatomic to cosmological. Each level is independently testable.",
            color=DIM, fontsize=9, ha='center', va='center', style='italic')

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, 'phys54_01_hierarchy_levels.png')


# ================================================================
# FIG 2: PARALLEL ISOMORPHISM — SM TO PCTRM
# Type: Connection/Integer Map (Type 5)
# Shows: Same observables arising from different primitives
# ================================================================

def fig2_isomorphism_map():
    fig, ax = plt.subplots(figsize=(18, 12))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)

    # Title
    ax.text(9, 11.5, "Parallel Isomorphism: SM and PCTRM Produce the Same Observables",
            color=GOLD, fontsize=15, ha='center', va='center', fontweight='bold')
    ax.text(9, 11.0, "Different primitives. Same physics.",
            color=SILVER, fontsize=11, ha='center', va='center', style='italic')

    # Column headers
    ax.text(2.5, 10.2, "Standard Model", color=BLUE, fontsize=13, ha='center',
            fontweight='bold')
    ax.text(2.5, 9.85, "(field-theoretic)", color=BLUE, fontsize=9, ha='center')

    ax.text(9, 10.2, "Shared Observables", color=GOLD, fontsize=13, ha='center',
            fontweight='bold')
    ax.text(9, 9.85, "(measured by CODATA)", color=GOLD, fontsize=9, ha='center')

    ax.text(15.5, 10.2, "PCTRM Substrate", color=CYAN, fontsize=13, ha='center',
            fontweight='bold')
    ax.text(15.5, 9.85, "(discrete computational)", color=CYAN, fontsize=9, ha='center')

    # SM primitives (left)
    sm_items = [
        (8.7, "Quantum fields ψ(x)"),
        (7.6, "Dirac operators iγ^μ∂_μ"),
        (6.5, "Gauge couplings g₁, g₂, g₃"),
        (5.4, "Loop integrals ∫d⁴k"),
        (4.3, "Yukawa terms yψ̄Hψ"),
        (3.2, "CKM matrix V_ij"),
        (2.1, "Einstein field equations"),
    ]

    for y, text in sm_items:
        box = FancyBboxPatch((0.3, y - 0.35), 4.4, 0.7,
                              boxstyle="round,pad=0.1",
                              facecolor=PAN, edgecolor=BLUE, linewidth=1.3)
        ax.add_patch(box)
        ax.text(2.5, y, text, color=WHITE, fontsize=9.5, ha='center', va='center')

    # Shared observables (middle)
    observables = [
        (8.7, "m_e = 0.511 MeV",    "m_e"),
        (7.6, "α_EM = 1/137.036",   "α_EM"),
        (6.5, "V_us = 9/40 at 44 ppm", "V_us"),
        (5.4, "H 1S-2S transition", "H 1S-2S"),
        (4.3, "Koide K = 2/3 at 9.2 ppm", "Koide"),
        (3.2, "Mercury precession 43\"/cy", "Δφ"),
        (2.1, "Ω_Λ at 85 ppm",      "Ω_Λ"),
    ]

    for y, full_text, short_text in observables:
        box = FancyBboxPatch((6.8, y - 0.35), 4.4, 0.7,
                              boxstyle="round,pad=0.1",
                              facecolor=BG, edgecolor=GOLD, linewidth=1.8)
        ax.add_patch(box)
        ax.text(9, y, full_text, color=GOLD, fontsize=9.5, ha='center', va='center',
                fontweight='bold')

    # PCTRM primitives (right)
    pctrm_items = [
        (8.7, "Coherence tax rate"),
        (7.6, "Channel count × β struct"),
        (6.5, "Integer channel ratios"),
        (5.4, "Orbital closure modulus"),
        (4.3, "Lepton channel R₃/R₂"),
        (3.2, "Higher-order channel grad."),
        (2.1, "Universal soliton partition"),
    ]

    for y, text in pctrm_items:
        box = FancyBboxPatch((13.3, y - 0.35), 4.4, 0.7,
                              boxstyle="round,pad=0.1",
                              facecolor=PAN, edgecolor=CYAN, linewidth=1.3)
        ax.add_patch(box)
        ax.text(15.5, y, text, color=WHITE, fontsize=9.5, ha='center', va='center')

    # Arrows from SM to observables
    for y, _ in sm_items:
        arrow = FancyArrowPatch((4.75, y), (6.75, y),
                                 color=BLUE, arrowstyle='->',
                                 mutation_scale=12, linewidth=1.2, alpha=0.7)
        ax.add_patch(arrow)

    # Arrows from PCTRM to observables
    for y, _ in pctrm_items:
        arrow = FancyArrowPatch((13.25, y), (11.25, y),
                                 color=CYAN, arrowstyle='->',
                                 mutation_scale=12, linewidth=1.2, alpha=0.7)
        ax.add_patch(arrow)

    # Bottom note
    ax.text(9, 1.0, "For each observable: SM computes via field theory, PCTRM derives via substrate arithmetic.",
            color=SILVER, fontsize=10, ha='center', va='center', style='italic')
    ax.text(9, 0.5, "PCTRM passes ONLY if all observables agree with CODATA at their measurement precision.",
            color=WHITE, fontsize=10, ha='center', va='center', fontweight='bold')

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, 'phys54_02_isomorphism_map.png')


# ================================================================
# FIG 3: DIRECTION-CONDITIONAL TOPOLOGY VS STANDARD LATTICE
# Type: Geometric Cross-Section (Type 4)
# Shows: Staircase problem vs full-mesh solution
# ================================================================

def fig3_topology_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.30})
    fig.patch.set_facecolor(BG)
    ax1.set_facecolor(PAN)
    ax2.set_facecolor(PAN)

    # LEFT: Standard cubic lattice
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 9)

    # Draw lattice grid
    for i in range(11):
        ax1.axvline(x=i, color=DIM, linewidth=0.5, alpha=0.3)
    for j in range(9):
        ax1.axhline(y=j, color=DIM, linewidth=0.5, alpha=0.3)

    # Draw lattice points
    for i in range(11):
        for j in range(9):
            ax1.scatter([i], [j], s=15, c=DIM, alpha=0.4, zorder=2)

    # Intended direction (30 degrees)
    theta = np.radians(30)
    x_end = 10 * np.cos(theta)
    y_end = 10 * np.sin(theta)

    # Staircase path from (0,0) to target
    steps_x = []
    steps_y = []
    cx, cy = 0, 0
    steps_x.append(cx)
    steps_y.append(cy)
    target_x = 10 * np.cos(theta)
    target_y = 10 * np.sin(theta)
    dx_total = target_x
    dy_total = target_y
    slope = dy_total / dx_total
    accumulated_y = 0.0
    for i in range(10):
        cx += 1
        accumulated_y += slope
        steps_x.append(cx)
        steps_y.append(cy)
        while cy + 1 <= accumulated_y + 0.001:
            cy += 1
            steps_x.append(cx)
            steps_y.append(cy)

    ax1.plot(steps_x, steps_y, color=RED, linewidth=2.2, alpha=0.9,
             label='Lattice path (L1, 10+ cells)')

    # Intended straight path
    ax1.plot([0, x_end], [0, y_end], color=CYAN, linewidth=2.2,
             linestyle='--', alpha=0.8, label='Intended direction (30°)')

    # Start and end markers
    ax1.scatter([0], [0], s=220, c=GREEN, edgecolors=WHITE, linewidth=2, zorder=6)
    ax1.scatter([x_end], [y_end], s=220, c=GOLD, edgecolors=WHITE, linewidth=2, zorder=6)

    ax1.text(0, -0.5, "Start", color=GREEN, fontsize=10, ha='center', fontweight='bold')
    ax1.text(x_end, y_end + 0.4, "Target", color=GOLD, fontsize=10, ha='center', fontweight='bold')

    ax1.set_title("Standard Cubic Lattice (6 neighbors)", color=RED, fontsize=13,
                  fontweight='bold', pad=15)

    ax1.legend(loc='lower right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE,
               fontsize=9)

    ax1.text(5, -0.9, "Staircase artifact: path length ≠ Euclidean distance. Preferred axes break isotropy.",
             color=SILVER, fontsize=9, ha='center', style='italic')

    ax1.set_xticks([])
    ax1.set_yticks([])

    # RIGHT: Direction-conditional full mesh
    ax2.set_xlim(-1, 11)
    ax2.set_ylim(-1, 9)

    # Draw a sparse grid hint
    for i in range(11):
        ax2.axvline(x=i, color=DIM, linewidth=0.3, alpha=0.15)
    for j in range(9):
        ax2.axhline(y=j, color=DIM, linewidth=0.3, alpha=0.15)

    # Dots at integer positions to show cells exist
    for i in range(11):
        for j in range(9):
            ax2.scatter([i], [j], s=10, c=DIM, alpha=0.25, zorder=2)

    # Show the full-mesh: cell at (0,0) has neighbors in ANY direction
    center_x, center_y = 0, 0
    num_arrows = 16
    for k in range(num_arrows):
        angle = 2 * np.pi * k / num_arrows
        dx = np.cos(angle)
        dy = np.sin(angle)
        ax2.arrow(center_x, center_y, dx * 0.75, dy * 0.75, head_width=0.12,
                  head_length=0.15, fc=DIM, ec=DIM, alpha=0.4)

    # Highlight the 30-degree direction
    dx30 = np.cos(theta)
    dy30 = np.sin(theta)
    ax2.arrow(center_x, center_y, dx30 * 0.75, dy30 * 0.75, head_width=0.15,
              head_length=0.2, fc=GOLD, ec=GOLD, alpha=0.9, linewidth=2)

    # Direct path at 30 degrees — photon traverses in 10 cells exactly
    n_steps = 10
    for step in range(1, n_steps + 1):
        px = step * dx30
        py = step * dy30
        if step < n_steps:
            ax2.scatter([px], [py], s=60, c=CYAN, edgecolors=WHITE,
                        linewidth=1, alpha=0.8, zorder=5)

    ax2.plot([0, x_end], [0, y_end], color=CYAN, linewidth=2.5, alpha=0.9,
             label='Full-mesh path (10 cells, exactly 30°)')

    # Start and end markers
    ax2.scatter([0], [0], s=220, c=GREEN, edgecolors=WHITE, linewidth=2, zorder=6)
    ax2.scatter([x_end], [y_end], s=220, c=GOLD, edgecolors=WHITE, linewidth=2, zorder=6)

    ax2.text(0, -0.5, "Start", color=GREEN, fontsize=10, ha='center', fontweight='bold')
    ax2.text(x_end, y_end + 0.4, "Target", color=GOLD, fontsize=10, ha='center', fontweight='bold')

    ax2.set_title("Direction-Conditional Full-Mesh Topology", color=CYAN,
                  fontsize=13, fontweight='bold', pad=15)

    ax2.legend(loc='lower right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE,
               fontsize=9)

    ax2.text(5, -0.9, "Any direction → neighbor at 1 Planck-distance. Path length = Euclidean distance. Isotropic.",
             color=SILVER, fontsize=9, ha='center', style='italic')

    ax2.set_xticks([])
    ax2.set_yticks([])

    for ax in [ax1, ax2]:
        for spine in ax.spines.values():
            spine.set_edgecolor(DIM)
            spine.set_linewidth(0.5)

    fig.suptitle("Direction-Conditional Full-Mesh vs Standard Lattice Topology",
                 color=GOLD, fontsize=15, fontweight='bold', y=1.01)

    plt.tight_layout()
    save(fig, 'phys54_03_topology_comparison.png')


# ================================================================
# FIG 4: 1/r² GRAVITY FROM SPHERICAL CHANNEL SPREADING
# Type: Running/Convergence (Type 1)
# Shows: Channel density vs distance producing 1/r² law
# ================================================================

def fig4_gravity_channel_spread():
    fig, ax = plt.subplots(figsize=(16, 10))
    fig.patch.set_facecolor(BG)
    setup_ax(ax)

    # X: log distance from Earth center (in meters)
    # Y: log channel density (arbitrary units) and log gravitational acceleration

    r_vals = np.logspace(6.3, 8.6, 100)  # from near Earth surface to past Moon
    R_earth = 6.371e6
    g_surface = 9.81

    # Channel density model: N/(4π r²)
    N = 1.0  # arbitrary normalization
    channel_density = N / (4 * np.pi * r_vals**2)
    # Scale so at r=R_earth, value equals g_surface
    scale_factor = g_surface / (N / (4 * np.pi * R_earth**2))
    g_predicted = scale_factor * channel_density

    # Measured g values at specific altitudes
    landmarks = [
        (R_earth, 9.81, "Earth surface", ORANGE),
        (6.671e6, 8.87, "300 km (ISS)", GREEN),
        (2.657e7, 0.56, "GPS orbit (20,200 km)", BLUE),
        (4.216e7, 0.224, "Geostationary (35,786 km)", PURPLE),
        (3.844e8, 0.00272, "Moon (384,400 km)", MAG),
    ]

    # Plot predicted curve
    ax.loglog(r_vals, g_predicted, color=CYAN, linewidth=2.5,
              label='PCTRM prediction: g = N·scale/(4π r²)', zorder=3)

    # Plot measured points
    for r, g, name, color in landmarks:
        ax.scatter([r], [g], s=220, c=color, edgecolors=WHITE, linewidth=1.8,
                   zorder=5)
        # Offset label
        if r < 1e7:
            ax.annotate(name, xy=(r, g), xytext=(r * 1.4, g * 1.6),
                        color=color, fontsize=10, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=color, alpha=0.5))
        else:
            ax.annotate(name, xy=(r, g), xytext=(r * 0.35, g * 2.5),
                        color=color, fontsize=10, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=color, alpha=0.5))

    # Slope indicator
    ax.text(5e7, 0.02, "Slope = -2", color=GOLD, fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD,
                      linewidth=1.5))

    # Physical interpretation box
    interp_text = ("Channels from Earth's soliton spread over\n"
                   "sphere of radius r (surface area 4πr²).\n"
                   "Channel density ∝ 1/r²  →  g ∝ 1/r².\n"
                   "\n"
                   "Measurements match prediction at\n"
                   "experimental precision (Priority test P1).")
    ax.text(0.04, 0.14, interp_text, transform=ax.transAxes,
            color=WHITE, fontsize=10, ha='left', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN,
                      linewidth=1.5))

    ax.set_xlabel('Distance r from Earth center (m)', color=SILVER, fontsize=12)
    ax.set_ylabel('Gravitational acceleration g (m/s²)', color=SILVER, fontsize=12)
    ax.set_title('1/r² Gravity from Spherical Channel Spreading',
                 color=GOLD, fontsize=15, fontweight='bold', pad=15)

    ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM, labelcolor=WHITE,
              fontsize=10)

    ax.set_xlim(3e6, 8e8)
    ax.set_ylim(1e-3, 1e2)

    plt.tight_layout()
    save(fig, 'phys54_04_gravity_channel_spread.png')


# ================================================================
# FIG 5: ORBITAL CLOSURE PRODUCES ATOMIC SHELLS
# Type: Geometric Cross-Section (Type 4)
# Shows: Closed orbits at integer-multiple-of-modulus accumulation
# ================================================================

def fig5_shell_closure():
    fig, ax = plt.subplots(figsize=(16, 12))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')

    # Nucleus at center
    nucleus = Circle((0, 0), 0.25, color=GOLD, zorder=10)
    ax.add_patch(nucleus)
    ax.text(0, -0.55, "Proton", color=GOLD, fontsize=10, ha='center',
            fontweight='bold')

    # Three closing orbits: n=1, n=2, n=3
    orbits = [
        (1.0, 1, "n=1 (1S)", "1·M", GREEN, "-13.6 eV"),
        (2.2, 2, "n=2 (2S)", "4·M", BLUE, "-3.4 eV"),
        (3.8, 3, "n=3 (3S)", "9·M", PURPLE, "-1.51 eV"),
    ]

    for radius, n, label, modulus_label, color, energy in orbits:
        # Draw closed orbit
        circle = Circle((0, 0), radius, fill=False, edgecolor=color, linewidth=2,
                        alpha=0.9, zorder=4)
        ax.add_patch(circle)

        # Electron at an angle on this orbit
        theta_e = np.pi / 4 + (n - 1) * np.pi / 6
        ex = radius * np.cos(theta_e)
        ey = radius * np.sin(theta_e)
        ax.scatter([ex], [ey], s=200, c=color, edgecolors=WHITE, linewidth=1.8,
                   zorder=6)

        # Label the orbit (right side)
        lx = radius * np.cos(np.pi / 6)
        ly = radius * np.sin(np.pi / 6)
        ax.annotate("%s\nRemainder/orbit = %s\nE = %s" % (label, modulus_label, energy),
                    xy=(lx, ly), xytext=(radius + 1, radius * 0.2),
                    color=color, fontsize=10, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=color, alpha=0.6),
                    bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                              edgecolor=color, linewidth=1.3))

    # Forbidden (non-closing) orbit — dashed
    forbidden_radius = 1.6
    forbidden_circle = Circle((0, 0), forbidden_radius, fill=False,
                               edgecolor=RED, linewidth=1.5, linestyle='--',
                               alpha=0.6, zorder=3)
    ax.add_patch(forbidden_circle)
    ax.annotate("Non-integer closure\n(forbidden: 2.3·M)",
                xy=(-forbidden_radius, 0), xytext=(-5.3, -1.5),
                color=RED, fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RED, alpha=0.6))

    # Show arrow going around one orbit to indicate accumulation
    arrow_r = 1.0
    arrow_start_angle = 0
    arrow_end_angle = 300
    theta_arrow = np.linspace(np.radians(arrow_start_angle), np.radians(arrow_end_angle), 30)
    arc_x = arrow_r * np.cos(theta_arrow)
    arc_y = arrow_r * np.sin(theta_arrow)
    ax.plot(arc_x, arc_y, color=CYAN, linewidth=1.5, alpha=0.5)
    # Arrowhead at the end of this partial arc
    end_dx = -arrow_r * np.sin(np.radians(arrow_end_angle)) * 0.15
    end_dy = arrow_r * np.cos(np.radians(arrow_end_angle)) * 0.15
    ax.arrow(arc_x[-1], arc_y[-1], end_dx, end_dy,
             head_width=0.12, head_length=0.1, fc=CYAN, ec=CYAN, alpha=0.8)

    # Title
    ax.text(0, 5.4, "Orbital Closure Produces Atomic Shells",
            color=GOLD, fontsize=15, ha='center', fontweight='bold')
    ax.text(0, 4.9, "Remainder accumulated per orbit must equal N·M for closure (N integer).",
            color=SILVER, fontsize=10, ha='center', style='italic')

    # Legend / explanation box
    explanation = ("Closure condition:\n"
                   "  ∮ (remainder/tick) dt = N · Modulus\n"
                   "  N = 1, 2, 3, ...  → shells\n"
                   "\n"
                   "Non-integer N: orbit does not close,\n"
                   "electron does not stabilize at that radius.")
    ax.text(-5.5, 3.8, explanation, color=WHITE, fontsize=9.5,
            ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD,
                      linewidth=1.3))

    ax.text(0, -5.5, "Shell energies emerge from integer N². Bohr radius is smallest closure (N=1).",
            color=DIM, fontsize=10, ha='center', style='italic')

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, 'phys54_05_shell_closure.png')


# ================================================================
# FIG 6: COHERENCE TAX — PHOTON VS MASSIVE PARTICLE
# Type: Progression/Sequence (Type 7)
# Shows: Budget flow per tick determines velocity
# ================================================================

def fig6_coherence_tax():
    fig, ax = plt.subplots(figsize=(18, 10))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    ax.set_xlim(0, 22)
    ax.set_ylim(-1, 10)

    # Title
    ax.text(11, 9.3, "Coherence Tax: How Higgs Coupling Sets Particle Velocity",
            color=GOLD, fontsize=15, ha='center', va='center', fontweight='bold')

    # =========== PHOTON ROW ===========
    photon_y = 7
    ax.text(1, photon_y + 0.7, "PHOTON", color=CYAN, fontsize=13, ha='left',
            fontweight='bold')
    ax.text(1, photon_y + 0.3, "(Higgs coupling = 0, coherence tax = 0)",
            color=CYAN, fontsize=9, ha='left')

    # Photon ticks — each cell advances by 1
    n_photon_ticks = 10
    tick_width = 1.8
    for i in range(n_photon_ticks):
        tx = 1.5 + i * tick_width
        # Full budget bar (green) — full modulus
        bar = FancyBboxPatch((tx, photon_y - 0.25), tick_width - 0.3, 0.5,
                              boxstyle="round,pad=0.02",
                              facecolor=CYAN, edgecolor=WHITE, linewidth=1,
                              alpha=0.7)
        ax.add_patch(bar)
        # Show M inside
        ax.text(tx + (tick_width - 0.3) / 2, photon_y, "M",
                color=BG, fontsize=9, ha='center', va='center', fontweight='bold')
        # Cell advance marker below
        ax.text(tx + (tick_width - 0.3) / 2, photon_y - 0.55, "→ 1 cell",
                color=WHITE, fontsize=7, ha='center')
        # Tick number above
        ax.text(tx + (tick_width - 0.3) / 2, photon_y + 0.5, "t=%d" % i,
                color=DIM, fontsize=7, ha='center')

    # Photon result
    ax.text(20, photon_y, "v = c\n(1 cell/tick)", color=CYAN, fontsize=11,
            ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN,
                      linewidth=1.5))

    # =========== ELECTRON ROW ===========
    electron_y = 3
    ax.text(1, electron_y + 0.7, "ELECTRON", color=MAG, fontsize=13, ha='left',
            fontweight='bold')
    ax.text(1, electron_y + 0.3, "(Higgs coupling active, tax drains 95% of budget)",
            color=MAG, fontsize=9, ha='left')

    # Show 20 ticks for electron, small accumulation per tick
    n_electron_ticks = 20
    tick_width_e = 0.9
    for i in range(n_electron_ticks):
        tx = 1.5 + i * tick_width_e
        # Show small portion of budget remaining after tax
        # Budget = 0.05M per tick (95% tax applied)
        avail_h = 0.1  # small available
        tax_h = 0.4  # large taxed portion

        # Total budget rectangle (taxed portion in red, available in green)
        # Taxed portion (bottom, larger)
        tax_bar = FancyBboxPatch((tx, electron_y - 0.3), tick_width_e - 0.1, tax_h,
                                  boxstyle="round,pad=0.01",
                                  facecolor=RED, edgecolor=DIM, linewidth=0.5,
                                  alpha=0.55)
        ax.add_patch(tax_bar)
        # Available portion (top, smaller)
        avail_bar = FancyBboxPatch((tx, electron_y + 0.1), tick_width_e - 0.1, avail_h,
                                    boxstyle="round,pad=0.01",
                                    facecolor=MAG, edgecolor=WHITE, linewidth=0.5,
                                    alpha=0.9)
        ax.add_patch(avail_bar)

    # Cell advance happens only once after 20 ticks
    advance_x = 1.5 + n_electron_ticks * tick_width_e + 0.3
    ax.annotate('Accumulated\nremainder = M\n↓\n1 cell advance',
                xy=(advance_x - 0.5, electron_y), xytext=(advance_x + 1.5, electron_y),
                color=WHITE, fontsize=9, ha='center', va='center',
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=MAG,
                          linewidth=1.3),
                arrowprops=dict(arrowstyle='->', color=MAG, linewidth=1.5))

    # Electron result
    ax.text(20, electron_y, "v = 0.05 c\n(1 cell / 20 ticks)", color=MAG, fontsize=11,
            ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG,
                      linewidth=1.5))

    # =========== LEGEND / EXPLANATION ===========
    # Color legend
    ax.add_patch(FancyBboxPatch((0.8, 0.5), 0.6, 0.3, boxstyle="round,pad=0.02",
                                  facecolor=CYAN, edgecolor=WHITE, linewidth=0.8,
                                  alpha=0.7))
    ax.text(1.55, 0.65, "Full modulus M (photon)", color=WHITE, fontsize=9, va='center')

    ax.add_patch(FancyBboxPatch((6.5, 0.5), 0.6, 0.3, boxstyle="round,pad=0.02",
                                  facecolor=MAG, edgecolor=WHITE, linewidth=0.8,
                                  alpha=0.9))
    ax.text(7.3, 0.65, "Available (post-tax)", color=WHITE, fontsize=9, va='center')

    ax.add_patch(FancyBboxPatch((11.5, 0.5), 0.6, 0.3, boxstyle="round,pad=0.02",
                                  facecolor=RED, edgecolor=DIM, linewidth=0.8,
                                  alpha=0.55))
    ax.text(12.3, 0.65, "Coherence tax (pattern maintenance)", color=WHITE, fontsize=9,
            va='center')

    # Key insight box
    ax.text(11, -0.55,
            "Velocity = (per-tick budget available) / modulus.  Higgs coupling → coherence tax → reduced budget → lower velocity.",
            color=GOLD, fontsize=10, ha='center', va='center', fontweight='bold',
            style='italic')

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, 'phys54_06_coherence_tax.png')


# ================================================================
# FIG 7: THE FALSIFICATION PROGRAM GRID
# Type: Threshold/Region (Type 3)
# Shows: Six levels and sixteen kill switches with precision thresholds
# ================================================================

def fig7_kill_switch_map():
    fig, ax = plt.subplots(figsize=(17, 11))
    fig.patch.set_facecolor(BG)
    setup_ax(ax)

    # Each kill switch: (label, level, required_precision_log10, priority_color)
    # precision as negative log10 (e.g. -3 for 10^-3)
    # Colors: GOLD=Critical, ORANGE=High, SILVER=Medium
    kill_switches = [
        ("K1: m_e from Higgs tax",        1, -3, GOLD),
        ("K2: m_μ/m_e ratio",             1, -3, GOLD),
        ("K3: α_EM low E",                1, -6, GOLD),
        ("K4: a_e anomalous moment",      1, -9, GOLD),
        ("K5: H 1S→2S transition",        2, -9, GOLD),
        ("K6: Lamb shift",                2, -4, ORANGE),
        ("K7: Deuteron binding",          3, -2, ORANGE),
        ("K8: Neutron half-life",         3, -2, ORANGE),
        ("K9: H₂O bond angle",            4, -2, SILVER),
        ("K10: Newtonian 1/r²",           5, -6, GOLD),
        ("K11: Mercury precession",       5, -1, ORANGE),
        ("K12: Lorentz invariance",       5, -19, GOLD),
        ("K13: GW emission rate",         5, -2, ORANGE),
        ("K14: Ω_Λ reproduction (RUM)",   6, -4.07, GOLD),  # 85 ppm
        ("K15: CMB spectrum",             6, -2, ORANGE),
        ("K16: QM phenomena",             0, -5, GOLD),  # Put at Level 0 as cross-cutting
    ]

    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(-21, 0)

    # Shaded regions for precision classes
    ax.axhspan(-21, -9, facecolor=MAG, alpha=0.06, zorder=1)
    ax.text(0.7, -14, "Sub-ppb regime\n(strictest)", color=MAG, fontsize=9, fontweight='bold',
            va='center', rotation=90)

    ax.axhspan(-9, -4, facecolor=ORANGE, alpha=0.06, zorder=1)
    ax.text(0.7, -6.5, "ppm – ppb regime", color=ORANGE, fontsize=9, fontweight='bold',
            va='center', rotation=90)

    ax.axhspan(-4, -1, facecolor=GREEN, alpha=0.06, zorder=1)
    ax.text(0.7, -2.5, "Standard\nmeasurement\nprecision", color=GREEN, fontsize=9,
            fontweight='bold', va='center', rotation=90)

    # Draw kill switches
    for label, level, precision, color in kill_switches:
        # Use jitter to avoid overlap at same (level, precision)
        ax.scatter([level], [precision], s=320, c=color, edgecolors=WHITE,
                   linewidth=1.8, zorder=6, alpha=0.95)

        # Offset labels to avoid collisions
        if "K1" == label.split(":")[0]:
            offset = (0.15, 0.3)
        elif "K2" == label.split(":")[0]:
            offset = (0.15, -0.6)
        elif "K3" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K4" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K5" == label.split(":")[0]:
            offset = (0.15, 0.3)
        elif "K6" == label.split(":")[0]:
            offset = (0.15, -0.3)
        elif "K7" == label.split(":")[0]:
            offset = (0.15, 0.3)
        elif "K8" == label.split(":")[0]:
            offset = (0.15, -0.6)
        elif "K9" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K10" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K11" == label.split(":")[0]:
            offset = (0.15, 0.4)
        elif "K12" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K13" == label.split(":")[0]:
            offset = (0.15, -0.3)
        elif "K14" == label.split(":")[0]:
            offset = (0.15, 0)
        elif "K15" == label.split(":")[0]:
            offset = (0.15, 0.3)
        elif "K16" == label.split(":")[0]:
            offset = (0.15, 0)
        else:
            offset = (0.15, 0)

        ax.annotate(label, xy=(level, precision),
                    xytext=(level + offset[0], precision + offset[1]),
                    color=color, fontsize=9, ha='left', va='center',
                    fontweight='bold')

    # Level labels on x-axis
    level_names = {
        0: "Cross-cutting\n(K16)",
        1: "Level 1\nSubatomic",
        2: "Level 2\nAtomic",
        3: "Level 3\nNuclear",
        4: "Level 4\nMolecular",
        5: "Level 5\nMacroscopic/GR",
        6: "Level 6\nCosmological",
    }
    for lvl, name in level_names.items():
        ax.text(lvl, -20.3, name, color=SILVER, fontsize=10,
                ha='center', va='center', fontweight='bold')

    # Precision axis labels
    y_major_ticks = [0, -3, -6, -9, -12, -15, -18, -21]
    y_major_labels = ["10⁰", "10⁻³", "10⁻⁶", "10⁻⁹", "10⁻¹²", "10⁻¹⁵", "10⁻¹⁸", "10⁻²¹"]
    ax.set_yticks(y_major_ticks)
    ax.set_yticklabels(y_major_labels)

    ax.set_xticks([])
    ax.set_xlim(-0.5, 6.8)
    ax.set_ylim(-21, 0)

    # Legend for priority colors
    legend_elements = [
        plt.scatter([], [], s=200, c=GOLD, edgecolors=WHITE, linewidth=1.8,
                    label='Critical (must fire or revise framework)'),
        plt.scatter([], [], s=200, c=ORANGE, edgecolors=WHITE, linewidth=1.8,
                    label='High priority'),
        plt.scatter([], [], s=200, c=SILVER, edgecolors=WHITE, linewidth=1.8,
                    label='Medium priority'),
    ]
    ax.legend(handles=legend_elements, loc='lower right',
              facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

    ax.set_ylabel('Required Precision', color=SILVER, fontsize=12)
    ax.set_title('The Falsification Program: Six Levels, Sixteen Kill Switches',
                 color=GOLD, fontsize=15, fontweight='bold', pad=15)

    # Bottom explanation
    ax.text(3, -20.7,
            "Each kill switch fires if PCTRM cannot reproduce its observable at the required precision.",
            color=DIM, fontsize=9, ha='center', style='italic')

    plt.tight_layout()
    save(fig, 'phys54_07_kill_switch_map.png')


# ================================================================
# FIG 8: THE UNIVERSAL SOLITON — CMB AS VACUUM AND EXPANSION
# Type: Geometric Cross-Section (Type 4)
# Shows: Same surface read from two positions
# ================================================================

def fig8_universal_double_boundary():
    fig, ax = plt.subplots(figsize=(16, 13))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(PAN)

    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal')

    # Draw the universal soliton as a large circle with gradient-like fill
    # Multiple concentric circles to suggest depth
    outer_r = 6.5
    for i, r in enumerate(np.linspace(outer_r, outer_r - 0.5, 6)):
        alpha = 0.15 - i * 0.02
        ring = Circle((0, 0), r, fill=False, edgecolor=PURPLE, linewidth=3,
                      alpha=alpha, zorder=3)
        ax.add_patch(ring)
    # Main boundary
    main_boundary = Circle((0, 0), outer_r, fill=False, edgecolor=PURPLE,
                            linewidth=2.5, alpha=0.95, zorder=4)
    ax.add_patch(main_boundary)

    # Inside fill to suggest CMB/vacuum
    inner_fill = Circle((0, 0), outer_r, facecolor=MAG, alpha=0.06, zorder=2)
    ax.add_patch(inner_fill)

    # Observer inside
    obs_x, obs_y = 1.2, -0.8
    ax.scatter([obs_x], [obs_y], s=250, c=GOLD, edgecolors=WHITE, linewidth=2,
               zorder=10)
    ax.text(obs_x, obs_y - 0.45, "Observer", color=GOLD, fontsize=10,
            ha='center', fontweight='bold')

    # Arrow: observer looking INWARD (toward CMB as vacuum)
    # This arrow points into the substrate
    inward_arrow = FancyArrowPatch((obs_x, obs_y), (obs_x - 2.0, obs_y + 1.5),
                                    color=MAG, arrowstyle='->',
                                    mutation_scale=25, linewidth=2.5)
    ax.add_patch(inward_arrow)
    ax.text(obs_x - 2.5, obs_y + 2.2, "Look inward:\nCMB = Vacuum",
            color=MAG, fontsize=11, ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=MAG,
                      linewidth=1.5))

    # Arrow: observer looking OUTWARD (toward expansion)
    outward_arrow = FancyArrowPatch((obs_x, obs_y), (obs_x + 3.5, obs_y + 3.0),
                                     color=CYAN, arrowstyle='->',
                                     mutation_scale=25, linewidth=2.5)
    ax.add_patch(outward_arrow)
    ax.text(obs_x + 4.0, obs_y + 3.8, "Look outward:\nExpansion",
            color=CYAN, fontsize=11, ha='center', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=CYAN,
                      linewidth=1.5))

    # Child solitons being "born" from the vacuum
    children = [
        (-3.2, 2.5, 0.2, "galaxy", GREEN),
        (-4.2, -1.5, 0.18, "star", ORANGE),
        (2.5, -3.5, 0.15, "atom", BLUE),
        (3.8, -0.5, 0.12, "particle", SILVER),
        (-1.5, 4.0, 0.16, "cluster", PURPLE),
        (-4.5, 0.5, 0.14, "photon", WHITE),
    ]
    for cx, cy, cr, name, color in children:
        child = Circle((cx, cy), cr, facecolor=color, edgecolor=WHITE,
                       linewidth=1, alpha=0.8, zorder=8)
        ax.add_patch(child)
        ax.text(cx, cy - cr - 0.35, name, color=color, fontsize=8,
                ha='center', va='top')

    # Outer labels: two readings of the same surface
    # Inward reading label (below left)
    ax.text(-6.5, -6.8,
            "VACUUM (Layer 0)\nCMB temperature = 2.7255 K\nSubstrate from which\nchildren emerge",
            color=MAG, fontsize=10, ha='left', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=MAG,
                      linewidth=1.5))

    # Outward reading label (below right)
    ax.text(6.5, -6.8,
            "EXPANSION (Layer 12)\nΩ_Λ = (251-22π)/264\nOuter boundary of\nuniversal soliton",
            color=CYAN, fontsize=10, ha='right', va='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=CYAN,
                      linewidth=1.5))

    # Arrow across the bottom showing these are the SAME surface
    ax.annotate("", xy=(4.8, -6.8), xytext=(-4.8, -6.8),
                arrowprops=dict(arrowstyle='<->', color=GOLD, linewidth=2.5))
    ax.text(0, -7.3, "Same surface, two readings from inside",
            color=GOLD, fontsize=11, ha='center', va='center', fontweight='bold',
            style='italic')

    # Title
    ax.text(0, 7.3, "The Universal Soliton: CMB as Vacuum, Expansion as Outer Boundary",
            color=GOLD, fontsize=14, ha='center', fontweight='bold')
    ax.text(0, 6.85,
            "The outermost soliton's inner and outer boundaries are the same surface viewed from two positions.",
            color=SILVER, fontsize=10, ha='center', style='italic')

    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    save(fig, 'phys54_08_universal_double_boundary.png')


# ================================================================
# MAIN
# ================================================================

if __name__ == '__main__':
    print("Generating PHYS-54 figures...")
    print("Output directory: %s" % outdir)
    print()

    fig1_hierarchy_levels()
    fig2_isomorphism_map()
    fig3_topology_comparison()
    fig4_gravity_channel_spread()
    fig5_shell_closure()
    fig6_coherence_tax()
    fig7_kill_switch_map()
    fig8_universal_double_boundary()

    print()
    print("Generated 8 figures:")
    print("  phys54_01_hierarchy_levels.png")
    print("  phys54_02_isomorphism_map.png")
    print("  phys54_03_topology_comparison.png")
    print("  phys54_04_gravity_channel_spread.png")
    print("  phys54_05_shell_closure.png")
    print("  phys54_06_coherence_tax.png")
    print("  phys54_07_kill_switch_map.png")
    print("  phys54_08_universal_double_boundary.png")
