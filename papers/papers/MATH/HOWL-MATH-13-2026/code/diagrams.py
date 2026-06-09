

#!/usr/bin/env python3
"""
HOWL MATH-13 Diagrams — The Velocity-Dependent Geometric Ratio
8 figures covering beta(v) from rest to light speed.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Ellipse, FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================


# ── Global palette (D7.2) ──
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


def save(fig, filename):
    path = os.path.join(outdir, filename)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % filename)


def style_ax(ax, xlabel='', ylabel='', title=''):
    ax.set_facecolor(PAN)
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=18)


def elliptic_E(e_mod, npts=500):
    """Complete elliptic integral of the second kind via numerical integration."""
    theta = np.linspace(0, np.pi / 2, npts)
    integrand = np.sqrt(1.0 - e_mod**2 * np.sin(theta)**2)
    return np.trapz(integrand, theta)


def elliptic_K(k_mod, npts=500):
    """Complete elliptic integral of the first kind via numerical integration."""
    theta = np.linspace(0, np.pi / 2, npts)
    integrand = 1.0 / np.sqrt(1.0 - k_mod**2 * np.sin(theta)**2)
    return np.trapz(integrand, theta)


def beta_of_v(vc):
    """Beta(v) = E(v/c) / (1 + 1/gamma) where gamma = 1/sqrt(1 - v^2/c^2)."""
    if vc >= 1.0:
        return 1.0
    if vc <= 0.0:
        return np.pi / 4.0
    gamma = 1.0 / np.sqrt(1.0 - vc**2)
    E_val = elliptic_E(vc)
    denom = 1.0 + 1.0 / gamma
    return E_val / denom


# Precompute fine grid
vc_fine = np.linspace(0, 0.9999, 2000)
beta_fine = np.array([beta_of_v(v) for v in vc_fine])
# Append exact endpoint
vc_fine = np.append(vc_fine, 1.0)
beta_fine = np.append(beta_fine, 1.0)


# ================================================================
# FIG 1: CIRCLE-TO-ELLIPSE PROGRESSION
# Type: Geometric Cross-Section (D5 Type 4)
# Shows: The physical shape change at four velocities with
#        L1 bounding rectangle and L2 perimeter labeled
# ================================================================

fig, axes = plt.subplots(1, 4, figsize=(20, 7), facecolor=BG)
fig.suptitle('Circle to Ellipse Under Lorentz Contraction',
             color=GOLD, fontsize=16, fontweight='bold', y=0.97)

velocities = [0.0, 0.5, 0.9, 0.99]
labels_v = ['v = 0', 'v = 0.5c', 'v = 0.9c', 'v = 0.99c']
colors_el = [CYAN, GREEN, ORANGE, MAG]

d = 2.0  # diameter
r = d / 2.0

for idx, (vc, lab, col) in enumerate(zip(velocities, labels_v, colors_el)):
    ax = axes[idx]
    ax.set_facecolor(PAN)
    ax.set_aspect('equal')
    ax.axis('off')

    if vc == 0:
        gamma = 1.0
    else:
        gamma = 1.0 / np.sqrt(1.0 - vc**2)

    a_semi = r           # perpendicular to motion (horizontal)
    b_semi = r / gamma   # along motion (vertical, contracted)

    # Bounding rectangle (L1)
    rect_w = 2 * a_semi
    rect_h = 2 * b_semi
    rect = mpatches.FancyBboxPatch(
        (-a_semi, -b_semi), rect_w, rect_h,
        boxstyle='round,pad=0.02',
        facecolor='none', edgecolor=DIM, linewidth=1.5, linestyle='--'
    )
    ax.add_patch(rect)

    # Ellipse (L2)
    ellipse = Ellipse((0, 0), 2 * a_semi, 2 * b_semi,
                       facecolor='none', edgecolor=col, linewidth=2.5)
    ax.add_patch(ellipse)

    # Compute values
    bv = beta_of_v(vc)
    E_val = elliptic_E(vc) if vc > 0 else np.pi / 2.0
    P_L2 = 2 * d * E_val
    if vc >= 1.0:
        P_L1 = 2 * d
    else:
        P_L1 = 2 * d * (1.0 + 1.0 / gamma)

    # Axis limits with generous padding
    lim = 1.8
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    # Velocity label at top
    ax.text(0, 1.55, lab, color=col, fontsize=13, fontweight='bold',
            ha='center', va='center')

    # Beta value
    ax.text(0, -1.25, r'$\beta$ = %.4f' % bv, color=WHITE, fontsize=10,
            ha='center', va='center')

    # L2 perimeter label
    ax.text(0, -1.50, 'L2 = %.3f d' % (P_L2 / d), color=col, fontsize=9,
            ha='center', va='center')

    # L1 perimeter label
    ax.text(0, -1.70, 'L1 = %.3f d' % (P_L1 / d), color=DIM, fontsize=9,
            ha='center', va='center')

    # Motion arrow for moving cases
    if vc > 0:
        ax.annotate('', xy=(0, b_semi + 0.35), xytext=(0, b_semi + 0.12),
                     arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.5))
        ax.text(0.25, b_semi + 0.28, 'v', color=SILVER, fontsize=9,
                ha='left', va='center')

    # Dimension labels
    # Horizontal diameter
    ax.plot([-a_semi, a_semi], [-b_semi - 0.15, -b_semi - 0.15],
            color=DIM, linewidth=0.8)
    ax.text(0, -b_semi - 0.32, 'd', color=SILVER, fontsize=9,
            ha='center', va='center')
    # Vertical diameter
    ax.plot([a_semi + 0.15, a_semi + 0.15], [-b_semi, b_semi],
            color=DIM, linewidth=0.8)
    ax.text(a_semi + 0.35, 0, 'd/%.1f' % gamma if gamma > 1.01 else 'd',
            color=SILVER, fontsize=8, ha='left', va='center')

fig.subplots_adjust(wspace=0.15, top=0.88, bottom=0.08)
save(fig, 'math13_01_circle_ellipse_progression.png')


# ================================================================
# FIG 2: BETA(V) MAIN CURVE
# Type: Running/Convergence Chart (D5 Type 1)
# Shows: The flatness at low v and steepness near c —
#        the shape IS the physics
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='v / c', ylabel=r'$\beta$(v)',
         title=r'The Velocity-Dependent Geometric Ratio $\beta$(v)')

# Main curve
ax.plot(vc_fine, beta_fine, color=CYAN, linewidth=2.5, zorder=5)

# Horizontal reference lines
ax.axhline(y=np.pi / 4, color=GOLD, linewidth=1.2, linestyle='--', alpha=0.6)
ax.text(0.03, np.pi / 4 + 0.008, r'$\pi$/4 = 0.7854  (rest)',
        color=GOLD, fontsize=10, va='bottom')

ax.axhline(y=1.0, color=MAG, linewidth=1.2, linestyle='--', alpha=0.6)
ax.text(0.03, 1.0 + 0.008, r'$\beta$ = 1  (light speed)',
        color=MAG, fontsize=10, va='bottom')

# Key data points
key_vc = [0.0, 0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 1.0]
key_beta = [beta_of_v(v) for v in key_vc]

ax.scatter(key_vc, key_beta, s=120, color=CYAN, edgecolors=WHITE,
           linewidth=1.5, zorder=10)

# Annotate selected points
annotations = [
    (0.5, beta_of_v(0.5), 'v=0.5c\n' + r'$\beta$=%.4f' % beta_of_v(0.5),
     (0.38, 0.83)),
    (0.9, beta_of_v(0.9), 'v=0.9c\n' + r'$\beta$=%.4f' % beta_of_v(0.9),
     (0.78, 0.87)),
    (0.99, beta_of_v(0.99), 'v=0.99c\n' + r'$\beta$=%.4f' % beta_of_v(0.99),
     (0.87, 0.95)),
]

for xv, yv, txt, xyoff in annotations:
    ax.annotate(txt, xy=(xv, yv), xytext=xyoff,
                color=WHITE, fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color=SILVER, lw=1.0),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                          edgecolor=DIM, alpha=0.9))

# Shaded region: "effectively constant"
ax.axvspan(0, 0.5, color=GREEN, alpha=0.04)
ax.text(0.25, 0.80, 'Effectively constant\n(non-relativistic)',
        color=GREEN, fontsize=9, ha='center', alpha=0.7)

# Shaded region: "rapidly changing"
ax.axvspan(0.9, 1.0, color=RED, alpha=0.04)
ax.text(0.95, 0.82, 'Rapidly\nchanging',
        color=RED, fontsize=9, ha='center', alpha=0.7)

ax.set_xlim(-0.03, 1.05)
ax.set_ylim(0.76, 1.04)
ax.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

save(fig, 'math13_02_beta_v_main_curve.png')


# ================================================================
# FIG 3: NUMERATOR / DENOMINATOR DECOMPOSITION
# Type: Running/Convergence Chart (D5 Type 1)
# Shows: WHY beta increases — denominator falls faster
#        than numerator. Three curves: E(v/c), (1+1/gamma), beta(v)
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='v / c', ylabel='Value',
         title=r'Why $\beta$(v) Increases: Numerator vs Denominator')

# E(v/c) — numerator
E_vals = np.array([elliptic_E(v) if v < 1.0 else 1.0 for v in vc_fine])
ax.plot(vc_fine, E_vals, color=BLUE, linewidth=2.5, label='E(v/c)  [numerator]',
        zorder=5)

# (1 + 1/gamma) — denominator
denom_vals = np.array([
    (1.0 + np.sqrt(1.0 - v**2)) if v < 1.0 else 1.0 for v in vc_fine
])
ax.plot(vc_fine, denom_vals, color=ORANGE, linewidth=2.5,
        label='1 + 1/' + r'$\gamma$' + '  [denominator]', zorder=5)

# beta(v) — ratio
ax.plot(vc_fine, beta_fine, color=CYAN, linewidth=2.5,
        label=r'$\beta$(v) = E / (1+1/$\gamma$)', zorder=5)

# Endpoint markers
for arr, col in [(E_vals, BLUE), (denom_vals, ORANGE), (beta_fine, CYAN)]:
    ax.scatter([0, 1], [arr[0], arr[-1]], s=100, color=col,
               edgecolors=WHITE, linewidth=1.5, zorder=10)

# Endpoint labels — numerator
ax.text(0.06, np.pi / 2 + 0.04, r'E(0) = $\pi$/2', color=BLUE, fontsize=10)
ax.text(0.88, 1.07, 'E(1) = 1', color=BLUE, fontsize=10)

# Endpoint labels — denominator
ax.text(0.06, 2.06, '1 + 1/1 = 2', color=ORANGE, fontsize=10)
ax.text(0.88, 1.17, '1 + 0 = 1', color=ORANGE, fontsize=10)

# Endpoint labels — beta
ax.text(0.06, np.pi / 4 - 0.07, r'$\pi$/4', color=CYAN, fontsize=10)
ax.text(0.88, 0.93, '1', color=CYAN, fontsize=10)

# Key insight annotation
ax.annotate('Denominator falls faster\n' + r'$\Rightarrow$ ratio $\beta$(v) increases',
            xy=(0.75, 1.30), xytext=(0.50, 1.65),
            color=GOLD, fontsize=11, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                      edgecolor=GOLD, alpha=0.9))

ax.set_xlim(-0.03, 1.05)
ax.set_ylim(0.65, 2.20)
ax.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

leg = ax.legend(loc='center right', facecolor=PAN, edgecolor=DIM,
                labelcolor=WHITE, fontsize=10)
leg.get_frame().set_alpha(0.9)

save(fig, 'math13_03_numerator_denominator.png')


# ================================================================
# FIG 4: 4*BETA(V) — OPERATIONAL PI SPECTRUM
# Type: Scale/Landscape Diagram (D5 Type 2)
# Shows: Physical regimes mapped onto the pi-to-4 spectrum
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10), facecolor=BG)
style_ax(ax, xlabel='v / c',
         ylabel=r'4$\beta$(v)  —  Operational circumference ratio',
         title=r'The Operational $\pi$ Spectrum: from $\pi$ at Rest to 4 at Light Speed')

# Main curve
four_beta = 4.0 * beta_fine
ax.plot(vc_fine, four_beta, color=CYAN, linewidth=2.5, zorder=5)

# Reference lines
ax.axhline(y=np.pi, color=GOLD, linewidth=1.2, linestyle='--', alpha=0.6)
ax.text(0.02, np.pi + 0.025, r'$\pi$ = 3.1416  (rest frame)',
        color=GOLD, fontsize=10, va='bottom')

ax.axhline(y=4.0, color=MAG, linewidth=1.2, linestyle='--', alpha=0.6)
ax.text(0.02, 4.0 + 0.025, '4  (rectilinear limit / photon)',
        color=MAG, fontsize=10, va='bottom')

# Physical regime markers
regimes = [
    (1e-6, 'Thermal\nmolecules', GREEN, -0.20),
    (1e-4, 'Orbital\nmechanics', GREEN, -0.20),
    (0.1, 'Fast\nelectrons', BLUE, -0.20),
    (0.5, 'Mid-range\nrelativistic', BLUE, -0.20),
    (0.9, 'Proton\nbeam', ORANGE, 0.15),
    (0.9999, 'LHC\nprotons', RED, 0.15),
    (1.0, 'Photon', MAG, 0.15),
]

for vc_r, label, col, y_off in regimes:
    bval = 4.0 * beta_of_v(vc_r)
    ax.scatter([vc_r], [bval], s=160, color=col, edgecolors=WHITE,
               linewidth=1.5, zorder=10)
    ax.text(vc_r, bval + y_off, label + '\n4' + r'$\beta$=%.4f' % bval,
            color=col, fontsize=8, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.25', facecolor=BG,
                      edgecolor=col, alpha=0.8))

# The gap annotation
ax.annotate('', xy=(1.02, np.pi), xytext=(1.02, 4.0),
            arrowprops=dict(arrowstyle='<->', color=SILVER, lw=1.5))
ax.text(1.04, (np.pi + 4.0) / 2, 'Gap = 4' + r' $-$ $\pi$' + '\n= 0.858',
        color=SILVER, fontsize=9, va='center')

ax.set_xlim(-0.03, 1.12)
ax.set_ylim(2.95, 4.25)
ax.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

save(fig, 'math13_04_operational_pi_spectrum.png')


# ================================================================
# FIG 5: CORRECTION MAGNITUDE WITH THRESHOLDS
# Type: Threshold/Region Chart (D5 Type 3)
# Shows: WHERE the correction exceeds measurement precision
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
style_ax(ax, xlabel='v / c',
         ylabel=r'$|\beta$(v) $-$ $\pi$/4$|$ / ($\pi$/4)  [%]',
         title=r'Correction Magnitude: Where $\beta$(v) Departs from $\pi$/4')

# Percentage deviation
pct_dev = 100.0 * np.abs(beta_fine - np.pi / 4) / (np.pi / 4)

ax.plot(vc_fine, pct_dev, color=CYAN, linewidth=2.5, zorder=5)

# Threshold bands
thresholds = [
    (1.0, 'Precision measurement (1%)', GREEN, 0.12),
    (5.0, 'Standard engineering (5%)', ORANGE, 0.08),
    (10.0, 'Coarse measurement (10%)', RED, 0.05),
]

for thr, lab, col, alpha in thresholds:
    ax.axhline(y=thr, color=col, linewidth=1.5, linestyle='--', alpha=0.7)
    ax.text(0.03, thr + 0.4, lab, color=col, fontsize=9, va='bottom')

# Shade below 1% as "undetectable"
ax.axhspan(0, 1.0, color=GREEN, alpha=0.04)

# Find crossing points
for thr, lab, col, _ in thresholds:
    idx = np.searchsorted(pct_dev, thr)
    if idx < len(vc_fine):
        vc_cross = vc_fine[idx]
        ax.scatter([vc_cross], [thr], s=150, color=col,
                   edgecolors=WHITE, linewidth=1.5, zorder=10)
        ax.annotate('v/c = %.3f' % vc_cross,
                    xy=(vc_cross, thr),
                    xytext=(vc_cross - 0.12, thr + 2.5),
                    color=col, fontsize=9, ha='center',
                    arrowprops=dict(arrowstyle='->', color=col, lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.25', facecolor=BG,
                              edgecolor=col, alpha=0.9))

# Physical systems
systems = [
    (0.2, 'Electron beam\n(10 keV)', BLUE),
    (0.87, 'Proton beam\n(1 GeV)', ORANGE),
    (0.9999, 'LHC protons\n(6.5 TeV)', RED),
]

for vc_s, lab, col in systems:
    dev = 100.0 * abs(beta_of_v(vc_s) - np.pi / 4) / (np.pi / 4)
    ax.scatter([vc_s], [dev], s=140, color=col, edgecolors=WHITE,
               linewidth=1.5, zorder=10, marker='D')

ax.set_xlim(-0.03, 1.05)
ax.set_ylim(-1.0, 30.0)
ax.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=CYAN, linewidth=2, label=r'$\beta$(v) deviation'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor=ORANGE,
           markersize=8, label='Physical systems', linestyle='None'),
]
leg = ax.legend(handles=legend_elements, loc='upper left',
                facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10)
leg.get_frame().set_alpha(0.9)

save(fig, 'math13_05_correction_thresholds.png')


# ================================================================
# FIG 6: ANTENNA BETA MISMATCH
# Type: Geometric Cross-Section (D5 Type 4)
# Shows: Rest-frame circular aperture (beta=pi/4) receiving
#        radiation at c (beta=1). The mismatch IS aperture efficiency.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10), facecolor=BG)
ax.set_facecolor(PAN)
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-4.0, 5.0)

ax.text(0, 4.6, r'Aperture Efficiency as $\beta$ Mismatch',
        color=GOLD, fontsize=16, fontweight='bold', ha='center', va='center')

# --- Left side: incoming radiation (beta = 1, rectilinear) ---
# Draw plane wave as parallel lines
for y_pos in np.linspace(-2.0, 2.0, 9):
    ax.plot([-5.0, -2.2], [y_pos, y_pos], color=MAG, linewidth=1.0, alpha=0.5)
    ax.annotate('', xy=(-2.2, y_pos), xytext=(-3.0, y_pos),
                arrowprops=dict(arrowstyle='->', color=MAG, lw=1.0))

ax.text(-4.0, 3.0, 'Incoming radiation', color=MAG, fontsize=11,
        ha='center', va='center')
ax.text(-4.0, 2.5, r'$\beta$ = 1  (rectilinear)', color=MAG, fontsize=10,
        ha='center', va='center')
ax.text(-4.0, 2.1, 'Fills full bounding area', color=SILVER, fontsize=9,
        ha='center', va='center')

# --- Center: circular aperture ---
# Bounding square (what radiation "sees")
sq_size = 2.0
rect = mpatches.Rectangle((-sq_size, -sq_size), 2 * sq_size, 2 * sq_size,
                           facecolor='none', edgecolor=DIM,
                           linewidth=1.5, linestyle='--')
ax.add_patch(rect)

# Circle aperture
circle = plt.Circle((0, 0), sq_size, facecolor=CYAN, edgecolor=CYAN,
                     linewidth=2.5, alpha=0.15)
ax.add_patch(circle)
circle_edge = plt.Circle((0, 0), sq_size, facecolor='none', edgecolor=CYAN,
                          linewidth=2.5)
ax.add_patch(circle_edge)

ax.text(0, -2.7, 'Circular aperture', color=CYAN, fontsize=11,
        ha='center', va='center')
ax.text(0, -3.1, r'$\beta$ = $\pi$/4 = 0.785', color=CYAN, fontsize=10,
        ha='center', va='center')

# Corner gaps — shade the four corners that radiation can't pass through
theta_arr = np.linspace(0, 2 * np.pi, 200)
cx = sq_size * np.cos(theta_arr)
cy = sq_size * np.sin(theta_arr)

# Top-right corner gap
corner_patches_data = [
    ([0, sq_size, sq_size, 0], [0, 0, sq_size, sq_size]),
    ([0, -sq_size, -sq_size, 0], [0, 0, sq_size, sq_size]),
    ([0, -sq_size, -sq_size, 0], [0, 0, -sq_size, -sq_size]),
    ([0, sq_size, sq_size, 0], [0, 0, -sq_size, -sq_size]),
]

for cx_d, cy_d in corner_patches_data:
    ax.fill(cx_d, cy_d, color=RED, alpha=0.08, zorder=1)

# Label the gap
ax.text(1.65, 1.65, r'Gap', color=RED, fontsize=8, ha='center',
        va='center', alpha=0.8)

# --- Right side: transmitted power ---
# Transmitted rays (fewer, through circle)
for y_pos in np.linspace(-1.6, 1.6, 7):
    ax.plot([2.2, 5.0], [y_pos, y_pos], color=CYAN, linewidth=1.0, alpha=0.5)
    ax.annotate('', xy=(5.0, y_pos), xytext=(4.2, y_pos),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.0))

ax.text(4.0, 3.0, 'Transmitted power', color=CYAN, fontsize=11,
        ha='center', va='center')
ax.text(4.0, 2.5, r'$\eta_{max}$ = $\pi$/4 = 0.785', color=GOLD, fontsize=11,
        ha='center', va='center', fontweight='bold')
ax.text(4.0, 2.1, r'$\beta$ mismatch sets ceiling', color=SILVER, fontsize=9,
        ha='center', va='center')

# Bottom summary box
summary_box = FancyBboxPatch((-3.2, -3.8), 6.4, 0.6,
                              boxstyle='round,pad=0.15',
                              facecolor=BG, edgecolor=GOLD, linewidth=1.5)
ax.add_patch(summary_box)
ax.text(0, -3.5,
        r'Maximum aperture efficiency = $\beta_{rest}$ / $\beta_{light}$'
        r' = ($\pi$/4) / 1 = $\pi$/4 $\approx$ 78.5%',
        color=GOLD, fontsize=10, ha='center', va='center')

save(fig, 'math13_06_antenna_beta_mismatch.png')


# ================================================================
# FIG 7: BETA(V) VS BETA(P) COMPARISON
# Type: Running/Convergence Chart (D5 Type 1)
# Shows: Two independent mechanisms both moving beta from pi/4
#        toward 1, through completely different physics
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), facecolor=BG,
                                gridspec_kw={'wspace': 0.30})

# --- Left panel: beta(v) ---
style_ax(ax1, xlabel='v / c', ylabel=r'$\beta$',
         title=r'$\beta$(v): Velocity Axis')

ax1.plot(vc_fine, beta_fine, color=CYAN, linewidth=2.5, zorder=5)
ax1.axhline(y=np.pi / 4, color=GOLD, linewidth=1.0, linestyle='--', alpha=0.5)
ax1.axhline(y=1.0, color=MAG, linewidth=1.0, linestyle='--', alpha=0.5)

ax1.text(0.05, np.pi / 4 + 0.007, r'$\pi$/4', color=GOLD, fontsize=10)
ax1.text(0.05, 1.007, '1', color=MAG, fontsize=10)

# Key points
key_v = [0.0, 0.5, 0.9, 0.99, 1.0]
key_bv = [beta_of_v(v) for v in key_v]
ax1.scatter(key_v, key_bv, s=100, color=CYAN, edgecolors=WHITE,
            linewidth=1.5, zorder=10)

ax1.text(0.5, 0.77, 'Lorentz contraction\nof a circle\n' +
         r'e = v/c $\rightarrow$ E(v/c)',
         color=SILVER, fontsize=10, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                   edgecolor=DIM, alpha=0.9))

ax1.set_xlim(-0.05, 1.08)
ax1.set_ylim(0.75, 1.05)
ax1.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

# --- Right panel: beta(p) ---
style_ax(ax2, xlabel='Lp norm index p', ylabel=r'$\beta$(p)',
         title=r'$\beta$(p): Metric Axis')

# Compute beta(p) for a range of p values
p_vals = np.linspace(1.0, 6.0, 200)
beta_p_vals = []
for p in p_vals:
    theta = np.linspace(0, 2 * np.pi, 2000)
    integrand = (np.abs(np.sin(theta))**p + np.abs(np.cos(theta))**p)**(1.0 / p)
    Cp = np.trapz(integrand, theta)
    beta_p_vals.append(2 * np.pi / Cp)
beta_p_vals = np.array(beta_p_vals)

ax2.plot(p_vals, beta_p_vals, color=GREEN, linewidth=2.5, zorder=5)
ax2.axhline(y=np.pi / 4, color=GOLD, linewidth=1.0, linestyle='--', alpha=0.5)
ax2.axhline(y=1.0, color=MAG, linewidth=1.0, linestyle='--', alpha=0.5)

ax2.text(1.1, np.pi / 4 + 0.007, r'$\pi$/4', color=GOLD, fontsize=10)
ax2.text(1.1, 1.007, '1', color=MAG, fontsize=10)

# Known points
known_p = [1.0, 2.0]
known_bp = [np.pi / 4, 1.0]
ax2.scatter(known_p, known_bp, s=100, color=GREEN, edgecolors=WHITE,
            linewidth=1.5, zorder=10)

# beta(inf) reference
beta_inf = np.pi * np.sqrt(2) / 4
ax2.axhline(y=beta_inf, color=DIM, linewidth=1.0, linestyle=':', alpha=0.5)
ax2.text(5.5, beta_inf + 0.007, r'$\pi\sqrt{2}$/4', color=DIM, fontsize=9)

ax2.text(3.5, 0.85, 'Changing the\nmeasurement metric\n' +
         r'L1 $\rightarrow$ L2 $\rightarrow$ L$\infty$',
         color=SILVER, fontsize=10, ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor=BG,
                   edgecolor=DIM, alpha=0.9))

ax2.set_xlim(0.8, 6.2)
ax2.set_ylim(0.75, 1.15)
ax2.grid(True, color=DIM, alpha=0.15, linewidth=0.5)

# Shared annotation at top
fig.text(0.5, 0.97,
         r'Two Independent Mechanisms: $\beta$ from $\pi$/4 toward 1',
         color=GOLD, fontsize=15, fontweight='bold', ha='center', va='center')

save(fig, 'math13_07_beta_v_vs_beta_p.png')


# ================================================================
# FIG 8: IDENTITY CARD
# Type: Identity Card (D5 Type 8)
# Shows: Visual anchor — formula, endpoints, three-axis family,
#        connection to MATH-11 and MATH-12
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12), facecolor=BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

# --- Title band ---
title_box = FancyBboxPatch((0.5, 10.5), 17.0, 1.2,
                            boxstyle='round,pad=0.15',
                            facecolor=PAN, edgecolor=GOLD, linewidth=2)
ax.add_patch(title_box)
ax.text(9.0, 11.1, 'MATH-13: The Velocity-Dependent Geometric Ratio',
        color=GOLD, fontsize=17, fontweight='bold', ha='center', va='center')

# --- Central formula ---
formula_box = FancyBboxPatch((2.0, 8.5), 14.0, 1.6,
                              boxstyle='round,pad=0.2',
                              facecolor=PAN, edgecolor=CYAN, linewidth=2)
ax.add_patch(formula_box)
ax.text(9.0, 9.6, r'$\beta$(v)  =  E(v/c)  /  (1 + 1/$\gamma$)',
        color=CYAN, fontsize=20, fontweight='bold', ha='center', va='center',
        family='serif')
ax.text(9.0, 8.9, r'where E is the complete elliptic integral of the 2nd kind'
        r'  and  $\gamma$ = 1/$\sqrt{1 - v^2/c^2}$',
        color=SILVER, fontsize=11, ha='center', va='center')

# --- Endpoints box (left) ---
ep_box = FancyBboxPatch((0.8, 5.8), 5.5, 2.2,
                         boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=GOLD, linewidth=1.5)
ax.add_patch(ep_box)
ax.text(3.55, 7.6, 'Endpoints', color=GOLD, fontsize=13,
        fontweight='bold', ha='center', va='center')
ax.text(3.55, 7.0, r'v = 0  :  $\beta$ = $\pi$/4 = 0.7854',
        color=WHITE, fontsize=11, ha='center', va='center')
ax.text(3.55, 6.5, '         Circular  (maximum curvature)',
        color=SILVER, fontsize=9, ha='center', va='center')
ax.text(3.55, 6.1, r'v = c  :  $\beta$ = 1',
        color=WHITE, fontsize=11, ha='center', va='center')
ax.text(3.55, 5.7, '',  # padding
        color=SILVER, fontsize=9, ha='center', va='center')

# Small annotation under the endpoints box
ax.text(3.55, 5.5, '         Rectilinear  (zero curvature)',
        color=SILVER, fontsize=9, ha='center', va='center')

# --- Three-axis family (center) ---
fam_box = FancyBboxPatch((6.8, 5.2), 4.8, 2.8,
                          boxstyle='round,pad=0.15',
                          facecolor=PAN, edgecolor=PURPLE, linewidth=1.5)
ax.add_patch(fam_box)
ax.text(9.2, 7.6, 'Three-Axis Family', color=PURPLE, fontsize=13,
        fontweight='bold', ha='center', va='center')
ax.text(9.2, 7.0, 'p  (metric)     MATH-11', color=GREEN, fontsize=10,
        ha='center', va='center')
ax.text(9.2, 6.5, 'k  (manifold)   MATH-12', color=BLUE, fontsize=10,
        ha='center', va='center')
ax.text(9.2, 6.0, 'v  (velocity)    MATH-13', color=CYAN, fontsize=10,
        ha='center', va='center')
ax.text(9.2, 5.5, r'$\beta$(p, k, v)  —  one family', color=WHITE, fontsize=10,
        ha='center', va='center')

# --- Key property (right) ---
prop_box = FancyBboxPatch((12.1, 5.8), 5.3, 2.2,
                           boxstyle='round,pad=0.15',
                           facecolor=PAN, edgecolor=GREEN, linewidth=1.5)
ax.add_patch(prop_box)
ax.text(14.75, 7.6, 'Key Properties', color=GREEN, fontsize=13,
        fontweight='bold', ha='center', va='center')
ax.text(14.75, 7.0, 'Monotonically increasing', color=WHITE, fontsize=11,
        ha='center', va='center')
ax.text(14.75, 6.5, r'4$\beta$(v) ranges: $\pi$ $\rightarrow$ 4',
        color=WHITE, fontsize=11, ha='center', va='center')
ax.text(14.75, 6.1, 'Modulus e = v/c exactly', color=WHITE, fontsize=11,
        ha='center', va='center')

# --- Mini beta(v) curve ---
mini_ax = fig.add_axes([0.08, 0.08, 0.38, 0.32])
mini_ax.set_facecolor(PAN)
for spine in mini_ax.spines.values():
    spine.set_color(DIM)
    spine.set_linewidth(0.5)
mini_ax.tick_params(colors=DIM, labelsize=8)

mini_ax.plot(vc_fine, beta_fine, color=CYAN, linewidth=2.0)
mini_ax.axhline(y=np.pi / 4, color=GOLD, linewidth=0.8, linestyle='--', alpha=0.5)
mini_ax.axhline(y=1.0, color=MAG, linewidth=0.8, linestyle='--', alpha=0.5)
mini_ax.set_xlabel('v/c', color=SILVER, fontsize=9)
mini_ax.set_ylabel(r'$\beta$(v)', color=SILVER, fontsize=9)
mini_ax.set_xlim(-0.02, 1.02)
mini_ax.set_ylim(0.76, 1.03)
mini_ax.text(0.5, 0.78, r'$\pi$/4', color=GOLD, fontsize=8)
mini_ax.text(0.5, 1.01, '1', color=MAG, fontsize=8)

# --- Connection chain ---
conn_box = FancyBboxPatch((9.5, 0.6), 7.8, 3.4,
                           boxstyle='round,pad=0.15',
                           facecolor=PAN, edgecolor=DIM, linewidth=1.0)
ax.add_patch(conn_box)
ax.text(13.4, 3.65, 'Series Connections', color=SILVER, fontsize=12,
        fontweight='bold', ha='center', va='center')

connections = [
    (3.1, 'MATH-1', r'Q = F $\cdot$ $\beta$ $\cdot$ d$^2$ $\cdot$ Z',
     'Nine domains at rest', SILVER),
    (2.6, 'MATH-11', r'$\beta$ = $\pi$/4 as L1/L2 conversion',
     'Foundation identity', GREEN),
    (2.1, 'MATH-12', r'k > 0: torus, K(k) replaces $\pi$',
     'Manifold extension', BLUE),
    (1.6, 'MATH-13', r'v > 0: E(v/c), $\beta$ $\rightarrow$ 1 at c',
     'Velocity extension', CYAN),
    (1.1, 'Physics', r'Z as channel $\beta$-mismatch',
     'Separate paper', DIM),
]

for yp, label, formula, note, col in connections:
    ax.text(10.0, yp, label, color=col, fontsize=10, fontweight='bold',
            ha='left', va='center')
    ax.text(12.0, yp, formula, color=WHITE, fontsize=9,
            ha='left', va='center')
    ax.text(16.8, yp, note, color=DIM, fontsize=8,
            ha='right', va='center')

save(fig, 'math13_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n  MATH-13 Diagrams complete. 8 figures saved:")
print("  1. math13_01_circle_ellipse_progression.png")
print("  2. math13_02_beta_v_main_curve.png")
print("  3. math13_03_numerator_denominator.png")
print("  4. math13_04_operational_pi_spectrum.png")
print("  5. math13_05_correction_thresholds.png")
print("  6. math13_06_antenna_beta_mismatch.png")
print("  7. math13_07_beta_v_vs_beta_p.png")
print("  8. math13_08_identity_card.png")

