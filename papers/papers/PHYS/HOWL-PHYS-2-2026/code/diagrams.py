#!/usr/bin/env python3
"""
HOWL PHYS-2 Diagrams — There Are No Constants
8 figures covering running couplings, boundaries, scale dependence, G disagreements.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: THREE COUPLINGS RUNNING TOWARD GRAND UNIFICATION
# Type: Running/convergence
# Shows: alpha_1^-1, alpha_2^-1, alpha_3^-1 from M_Z to 10^16 GeV.
# The convergence (or near-convergence) IS the unification argument.
# The three "constants" visually becoming one.
# ================================================================

fig, ax = dark_fig("Three \"Constants\" Running Toward One Value",
                   xlabel="log\u2081\u2080(E / GeV)",
                   ylabel="1/\u03b1_i (inverse coupling strength)",
                   size=(16, 10))

log_E = np.linspace(np.log10(91.19), 16.5, 500)
log_MZ = np.log10(91.19)

# SM one-loop running (approximate)
# inv_alpha_1(MZ) ~ 59.0, b1 = 41/10
# inv_alpha_2(MZ) ~ 29.6, b2 = -19/6
# inv_alpha_3(MZ) ~ 8.5,  b3 = -7
inv_a1_MZ = 59.0
inv_a2_MZ = 29.6
inv_a3_MZ = 8.5

b1_sm = 41.0 / 10.0
b2_sm = -19.0 / 6.0
b3_sm = -7.0

def run_coupling(inv_a0, b, log_mu0, log_mu):
    L = (log_mu - log_mu0) * np.log(10) / (2 * np.pi)
    return inv_a0 - b * L

inv_a1 = run_coupling(inv_a1_MZ, b1_sm, log_MZ, log_E)
inv_a2 = run_coupling(inv_a2_MZ, b2_sm, log_MZ, log_E)
inv_a3 = run_coupling(inv_a3_MZ, b3_sm, log_MZ, log_E)

curve(ax, log_E, inv_a1, 'U(1): 1/\u03b1\u2081', BLUE, 2.5)
curve(ax, log_E, inv_a2, 'SU(2): 1/\u03b1\u2082', GREEN, 2.5)
curve(ax, log_E, inv_a3, 'SU(3): 1/\u03b1\u2083', RED, 2.5)

# M_Z marker
ax.plot([log_MZ, log_MZ], [0, 65], color=DIM, linewidth=1, linestyle=':', alpha=0.4)
ax.text(log_MZ + 0.2, 62, 'M_Z', fontsize=9, color=DIM)

# GUT region
shaded_region(ax, 15, 16.5, GOLD, 0.06)
ax.text(15.7, 55, 'GUT\nregion', fontsize=10, color=GOLD, ha='center',
        fontweight='bold')

# Measured values at M_Z
data_point(ax, log_MZ, inv_a1_MZ, '', BLUE, size=200)
data_point(ax, log_MZ, inv_a2_MZ, '', GREEN, size=200)
data_point(ax, log_MZ, inv_a3_MZ, '', RED, size=200)

# Near-miss annotation
ax.annotate('SM: near-miss\nMSSM: convergence\nimproves significantly',
            xy=(15.5, 38), xytext=(12, 48),
            fontsize=10, color=GOLD, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

result_box(ax, 8, 8,
           'Three "constants" \u2192 three readings of ONE value\n'
           'at three different boundary depths',
           GOLD, 10)

ax.set_xlim(1.5, 17)
ax.set_ylim(0, 70)

legend(ax, loc='upper right')

save_fig(fig, 'phys2_01_gut_running.png')


# ================================================================
# FIG 2: FLAVOR THRESHOLDS — ALPHA_S WITH KINKS AT QUARK MASSES
# Type: Running/threshold
# Shows: alpha_s running with visible slope changes at charm,
# bottom, and top thresholds. Each kink is a boundary crossing.
# ================================================================

fig, ax = dark_fig("\u03b1_s Running with Flavor Thresholds: Kinks at Each Boundary",
                   xlabel="log\u2081\u2080(E / GeV)",
                   ylabel="\u03b1_s(E)",
                   size=(16, 10))

# Approximate alpha_s running through thresholds
# Using simplified 1-loop: alpha_s(mu) = alpha_s(MZ) / (1 + b*alpha_s(MZ)/(2pi) * ln(mu/MZ))
alpha_s_MZ = 0.1179

# Segments with different nf
thresholds = [
    (np.log10(1.0), np.log10(1.27), 3, 'n_f = 3'),      # below charm
    (np.log10(1.27), np.log10(4.18), 4, 'n_f = 4'),      # charm to bottom
    (np.log10(4.18), np.log10(173.0), 5, 'n_f = 5'),     # bottom to top
    (np.log10(173.0), np.log10(1000.0), 6, 'n_f = 6'),   # above top
]

colors_nf = [RED, ORANGE, CYAN, GREEN]

# Simple model: alpha_s(mu) decreasing with energy, different slopes per nf
# beta_0 = (33 - 2*nf) / (12*pi)
for i, (log_lo, log_hi, nf, label) in enumerate(thresholds):
    log_mu = np.linspace(log_lo, log_hi, 200)
    beta0 = (33.0 - 2.0 * nf) / (12.0 * np.pi)
    # Match to alpha_s at M_Z for nf=5 segment
    if nf == 5:
        alpha_s_vals = alpha_s_MZ / (1.0 + beta0 * alpha_s_MZ * 2 * np.pi * (log_mu - log_MZ) * np.log(10))
    elif nf == 6:
        # Match at top threshold
        alpha_s_top = alpha_s_MZ / (1.0 + ((33 - 10) / (12 * np.pi)) * alpha_s_MZ * 2 * np.pi * (np.log10(173) - log_MZ) * np.log(10))
        beta0_6 = (33 - 12) / (12 * np.pi)
        alpha_s_vals = alpha_s_top / (1.0 + beta0_6 * alpha_s_top * 2 * np.pi * (log_mu - np.log10(173)) * np.log(10))
    elif nf == 4:
        # Match at charm threshold from nf=5 side
        beta0_5 = (33 - 10) / (12 * np.pi)
        alpha_s_charm = alpha_s_MZ / (1.0 + beta0_5 * alpha_s_MZ * 2 * np.pi * (np.log10(1.27) - log_MZ) * np.log(10))
        alpha_s_vals = alpha_s_charm / (1.0 + beta0 * alpha_s_charm * 2 * np.pi * (log_mu - np.log10(1.27)) * np.log(10))
    elif nf == 3:
        beta0_5 = (33 - 10) / (12 * np.pi)
        alpha_s_charm = alpha_s_MZ / (1.0 + beta0_5 * alpha_s_MZ * 2 * np.pi * (np.log10(1.27) - log_MZ) * np.log(10))
        beta0_4 = (33 - 8) / (12 * np.pi)
        alpha_s_1gev = alpha_s_charm / (1.0 + beta0_4 * alpha_s_charm * 2 * np.pi * (np.log10(1.0) - np.log10(1.27)) * np.log(10))
        alpha_s_vals = alpha_s_1gev / (1.0 + beta0 * alpha_s_1gev * 2 * np.pi * (log_mu - np.log10(1.0)) * np.log(10))

    alpha_s_vals = np.clip(alpha_s_vals, 0.05, 0.5)
    curve(ax, log_mu, alpha_s_vals, label if i == 0 else '', colors_nf[i], 2.5)

    # Label nf
    mid_log = (log_lo + log_hi) / 2
    mid_alpha = np.interp(mid_log, log_mu, alpha_s_vals)
    ax.text(mid_log, mid_alpha + 0.025, label, fontsize=8, color=colors_nf[i],
            ha='center', fontweight='bold')

# Threshold markers
quark_thresholds = [
    (np.log10(1.27), 'm_c', ORANGE),
    (np.log10(4.18), 'm_b', CYAN),
    (np.log10(173.0), 'm_t', GREEN),
]

for log_m, label, color in quark_thresholds:
    ax.plot([log_m, log_m], [0.05, 0.45], color=color, linewidth=2,
            linestyle='--', alpha=0.5)
    ax.text(log_m, 0.47, label, fontsize=10, color=color, ha='center',
            fontweight='bold')

# Measured value at M_Z
measured_diamond(ax, log_MZ, alpha_s_MZ, '', MAG, size=250)
ax.annotate('\u03b1_s(M_Z) = 0.1179\n(measured)', xy=(log_MZ, alpha_s_MZ),
            xytext=(log_MZ + 0.5, alpha_s_MZ + 0.08),
            fontsize=9, color=MAG, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

result_box(ax, 1.8, 0.12,
           'Each kink = a boundary crossing.\n'
           'The slope changes because\na new structure becomes active.',
           GOLD, 9)

ax.set_xlim(-0.1, 3.2)
ax.set_ylim(0.05, 0.55)

save_fig(fig, 'phys2_02_flavor_thresholds.png')


# ================================================================
# FIG 3: COSMOLOGICAL CONSTANT SCALE SEPARATION
# Type: Scale/landscape
# Shows: Log scale from Planck to cosmological, with boundary
# layers marked. The 10^120 gap spans the full hierarchy.
# ================================================================

fig, ax = dark_canvas("The Cosmological Constant: 10\u00b9\u00b2\u2070 Across the Full Hierarchy",
                      size=(16, 16))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 14)

# Vertical energy axis
axis_x = 3.0

levels = [
    (12.5, '10\u00b9\u2079 GeV', 'Planck scale', RED,
     'QFT vacuum prediction\nstarts here'),
    (11.0, '10\u00b9\u2076 GeV', 'GUT scale', ORANGE,
     'Grand unification\n(hypothetical)'),
    (9.0, '10\u00b2 GeV', 'Electroweak', MAG,
     'W/Z bosons, Higgs,\ntop quark'),
    (7.0, '1 GeV', 'Hadronic', BLUE,
     'Protons, neutrons,\nconfinement'),
    (5.0, '10\u207b\u00b2 eV', 'Atomic', CYAN,
     'Atoms, electron shells,\nchemistry'),
    (3.0, 'Gravitational', 'Stellar/Galactic', GREEN,
     'Stars, galaxies,\ndark matter halos'),
    (1.0, '10\u207b\u00b3\u00b3 eV', 'Cosmological', PURPLE,
     'Observable universe\nMeasured \u039b here'),
]

# Draw axis
ax.plot([axis_x, axis_x], [0.5, 13], color=DIM, linewidth=2, alpha=0.5)

for y, energy, name, color, detail in levels:
    ax.plot([axis_x - 0.2, axis_x + 0.2], [y, y], color=color, linewidth=3)
    data_point(ax, axis_x, y, '', color, size=180)

    # Left: energy
    ax.text(axis_x - 0.6, y, energy, fontsize=9, color=SILVER,
            ha='right', va='center')

    # Right: name and detail
    ax.text(axis_x + 0.6, y + 0.2, name, fontsize=11, color=color,
            ha='left', fontweight='bold')
    ax.text(axis_x + 0.6, y - 0.3, detail, fontsize=8, color=DIM,
            ha='left')

# The 10^120 gap
ax.annotate('', xy=(1.5, 1.0), xytext=(1.5, 12.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=3))
ax.text(0.8, 6.75, '10\u00b9\u00b2\u2070', fontsize=24, color=GOLD,
        ha='center', fontweight='bold', rotation=90)

# Labels for the two measurements
ax.text(7.0, 12.5, 'QFT PREDICTION', fontsize=13, color=RED,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))
ax.text(7.0, 11.7, 'Sum vacuum fluctuations\nfrom inside the hierarchy\n= enormous value',
        fontsize=9, color=SILVER, ha='center')

ax.text(7.0, 1.0, 'COSMOLOGICAL MEASUREMENT', fontsize=13, color=PURPLE,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=PURPLE))
ax.text(7.0, 0.2, 'Observe accelerating expansion\nfrom outside the hierarchy\n= tiny value',
        fontsize=9, color=SILVER, ha='center')

# Bottom note
ax.text(5.5, -0.5, 'Not the worst prediction in physics.\n'
        'The most dramatic demonstration of cumulative boundary effects.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys2_03_cosmological_scale.png')


# ================================================================
# FIG 4: SCREENING VS ANTI-SCREENING — QED AND QCD
# Type: Dual-panel geometric
# Shows: Left: QED virtual pairs screen charge (alpha increases
# inward). Right: QCD gluon anti-screening (alpha_s decreases
# inward). Opposite mechanisms, opposite running.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "QED: Screening (\u03b1 increases inward)",
    "QCD: Anti-Screening (\u03b1_s decreases inward)",
    size=(18, 9), wspace=0.35)

for a in [ax1, ax2]:
    a.set_xlim(-2.5, 2.5)
    a.set_ylim(-2.5, 2.5)
    a.set_aspect('equal')
    a.set_xticks([])
    a.set_yticks([])

# QED panel — screening
# Central charge
charge_qed = plt.Circle((0, 0), 0.3, fill=True, facecolor=BLUE,
                          alpha=0.5, edgecolor=BLUE, linewidth=2, zorder=5)
ax1.add_patch(charge_qed)
ax1.text(0, 0, 'e\u207b', fontsize=14, color=WHITE, ha='center',
         va='center', fontweight='bold', zorder=6)

# Virtual pair cloud — concentric rings getting fainter outward
for r in [0.6, 0.9, 1.2, 1.5, 1.8]:
    alpha_ring = 0.25 - r * 0.1
    ring = plt.Circle((0, 0), r, fill=False, edgecolor=CYAN,
                       linewidth=1.5, alpha=max(0.05, alpha_ring), zorder=3)
    ax1.add_patch(ring)

# Virtual pairs (+ and - symbols)
np.random.seed(42)
for _ in range(12):
    angle = np.random.uniform(0, 2 * np.pi)
    r = np.random.uniform(0.5, 1.6)
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    ax1.text(x - 0.1, y, '+', fontsize=8, color=RED, ha='center', alpha=0.5)
    ax1.text(x + 0.1, y, '\u2212', fontsize=8, color=BLUE, ha='center', alpha=0.5)

# Arrows showing probe penetration
ax1.annotate('', xy=(0.4, 0), xytext=(2.2, 0),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax1.text(2.2, 0.3, 'Probe', fontsize=9, color=GOLD, ha='right')

# Readings
ax1.text(2.0, -1.5, 'Outside:\n\u03b1 = 1/137\n(screened)', fontsize=10,
         color=CYAN, ha='center', fontweight='bold')
ax1.text(0, -2.0, 'Inside:\n\u03b1 = 1/127\n(less screened)', fontsize=10,
         color=GOLD, ha='center', fontweight='bold')

# QCD panel — anti-screening
# Central quarks
for dx, dy, label in [(-0.2, 0.15, 'q'), (0.2, 0.15, 'q'), (0, -0.2, 'q')]:
    ax2.text(dx, dy, label, fontsize=10, color=GREEN, ha='center',
             fontweight='bold', zorder=6)

hadron = plt.Circle((0, 0), 0.5, fill=True, facecolor=RED,
                      alpha=0.15, edgecolor=RED, linewidth=2.5, zorder=3)
ax2.add_patch(hadron)

# Gluon field lines — getting stronger outward
for r in [0.7, 1.0, 1.3, 1.6, 1.9]:
    alpha_ring = 0.05 + r * 0.08
    ring = plt.Circle((0, 0), r, fill=False, edgecolor=RED,
                       linewidth=1.5 + r * 0.5, alpha=min(0.4, alpha_ring), zorder=2)
    ax2.add_patch(ring)

# Gluon symbols
for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    for r in [0.8, 1.3]:
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        ax2.text(x, y, 'g', fontsize=7, color=ORANGE, ha='center',
                 alpha=0.4 + r * 0.15, fontweight='bold')

# Probe arrow
ax2.annotate('', xy=(0.6, 0), xytext=(2.2, 0),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax2.text(2.2, 0.3, 'Probe', fontsize=9, color=GOLD, ha='right')

# Readings
ax2.text(2.0, -1.5, 'Outside:\n\u03b1_s ~ O(1)\n(confined)', fontsize=10,
         color=RED, ha='center', fontweight='bold')
ax2.text(0, -2.0, 'Inside:\n\u03b1_s = 0.118\n(free quarks)', fontsize=10,
         color=GREEN, ha='center', fontweight='bold')

save_fig(fig, 'phys2_04_screening_mechanisms.png')


# ================================================================
# FIG 5: COUPLING VALUES AT MEASURED SCALES — ENERGY LADDER
# Type: Scale/ladder
# Shows: Vertical energy axis with measured alpha and alpha_s values
# at each scale. The readings change at each rung.
# ================================================================

fig, ax = dark_canvas("The Energy Ladder: Readings Change at Every Scale",
                      size=(16, 14))
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 12)

# Rungs
rungs = [
    (1.0, '~0 eV\n(atomic)', '\u03b1 = 1/137.036', '\u03b1_s: confined',
     SILVER, BLUE, RED),
    (3.0, '~1 GeV\n(hadronic)', '\u03b1 \u2248 1/137', '\u03b1_s \u2248 0.5',
     SILVER, BLUE, RED),
    (5.0, '~5 GeV\n(m_b)', '\u03b1 \u2248 1/136', '\u03b1_s \u2248 0.21',
     CYAN, BLUE, ORANGE),
    (7.0, '~90 GeV\n(M_Z)', '\u03b1 \u2248 1/127', '\u03b1_s = 0.1179',
     MAG, BLUE, GREEN),
    (9.0, '~173 GeV\n(m_t)', '\u03b1 \u2248 1/127', '\u03b1_s \u2248 0.108',
     GREEN, BLUE, GREEN),
    (11.0, '~246 GeV\n(EW unif.)', '\u03b1 \u2248 \u03b1_weak', '\u03b1_s \u2248 0.10',
     GOLD, GOLD, GREEN),
]

# Ladder rails
ax.plot([2.5, 2.5], [0.5, 11.5], color=DIM, linewidth=3, alpha=0.4)
ax.plot([8.0, 8.0], [0.5, 11.5], color=DIM, linewidth=3, alpha=0.4)

for y, energy, alpha_val, alphas_val, rung_color, a_color, as_color in rungs:
    # Rung
    ax.plot([2.5, 8.0], [y, y], color=rung_color, linewidth=2, alpha=0.5)

    # Energy label (left)
    ax.text(1.8, y, energy, fontsize=9, color=rung_color, ha='right',
            va='center', fontweight='bold')

    # Alpha value (center-left)
    ax.text(4.0, y + 0.3, alpha_val, fontsize=10, color=a_color,
            ha='center', fontweight='bold')

    # Alpha_s value (center-right)
    ax.text(6.5, y + 0.3, alphas_val, fontsize=10, color=as_color,
            ha='center', fontweight='bold')

# Column headers
ax.text(4.0, 11.8, 'Electromagnetic \u03b1', fontsize=12, color=BLUE,
        ha='center', fontweight='bold')
ax.text(6.5, 11.8, 'Strong \u03b1_s', fontsize=12, color=RED,
        ha='center', fontweight='bold')

# Direction arrows
ax.annotate('', xy=(4.0, 11.3), xytext=(4.0, 0.5),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5, linestyle='--'))
ax.text(3.2, 6, '\u03b1 increases\nwith energy', fontsize=8, color=BLUE,
        ha='center', rotation=90, style='italic')

ax.annotate('', xy=(6.5, 0.5), xytext=(6.5, 11.3),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5, linestyle='--'))
ax.text(7.3, 6, '\u03b1_s decreases\nwith energy', fontsize=8, color=RED,
        ha='center', rotation=90, style='italic')

# Bottom note
ax.text(5.0, -0.2, 'Same quantity. Different readings at every rung.\nNot constants \u2014 scale-dependent boundary readings.',
        fontsize=11, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys2_05_energy_ladder.png')


# ================================================================
# FIG 6: VACUUM POLARIZATION BOUNDARY — INSIDE VS OUTSIDE
# Type: Geometric cross-section
# Shows: Electron bare charge at center, virtual pair cloud,
# probe at two depths reading different alpha values.
# ================================================================

fig, ax = dark_canvas("Vacuum Polarization: The Electron's Boundary",
                      size=(14, 14))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')

# Bare charge at center
core = plt.Circle((0, 0), 0.25, fill=True, facecolor=GOLD,
                    alpha=0.6, edgecolor=GOLD, linewidth=2, zorder=5)
ax.add_patch(core)
ax.text(0, 0, 'e\u207b\nbare', fontsize=9, color=WHITE, ha='center',
        va='center', fontweight='bold', zorder=6)

# Virtual pair cloud — gradient
n_rings = 20
for i in range(n_rings, 0, -1):
    r = 1.6 * (i / float(n_rings))
    alpha_val = 0.02 + 0.10 * (1.0 - i / float(n_rings))
    ring = plt.Circle((0, 0), r, fill=True, facecolor=CYAN,
                       alpha=alpha_val, edgecolor='none', zorder=2)
    ax.add_patch(ring)

# Boundary circle
boundary = plt.Circle((0, 0), 1.6, fill=False, edgecolor=CYAN,
                        linewidth=2, linestyle='--', zorder=3)
ax.add_patch(boundary)
ax.text(0, 1.85, 'Virtual pair cloud boundary', fontsize=9, color=CYAN,
        ha='center', fontweight='bold')

# Low-energy probe (outside)
ax.annotate('', xy=(1.7, 0.8), xytext=(2.3, 1.5),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=2.5))
ax.text(2.3, 1.8, 'Low-energy probe\n(outside cloud)', fontsize=9,
        color=BLUE, ha='center', fontweight='bold')
ax.text(2.3, 1.2, 'Reads: \u03b1 = 1/137\n(fully screened)', fontsize=10,
        color=BLUE, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=BLUE))

# High-energy probe (inside)
ax.annotate('', xy=(0.4, -0.3), xytext=(2.0, -1.5),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))
ax.text(2.0, -1.8, 'High-energy probe\n(inside cloud)', fontsize=9,
        color=GOLD, ha='center', fontweight='bold')
ax.text(2.0, -2.3, 'Reads: \u03b1 = 1/127\n(less screened)', fontsize=10,
        color=GOLD, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

# Labels
ax.text(-2.0, -2.0, 'OUTSIDE:\nscreened charge\n\u03b1 appears weaker',
        fontsize=9, color=SILVER, ha='center')
ax.text(-2.0, 0.5, 'INSIDE:\nbare charge exposed\n\u03b1 appears stronger',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys2_06_vacuum_polarization.png')


# ================================================================
# FIG 7: G MEASUREMENT DISAGREEMENTS
# Type: Comparison/scatter
# Shows: G measurements from different groups with error bars,
# disagreeing beyond stated uncertainties. The scatter IS the data.
# ================================================================

fig, ax = dark_fig("G Measurements: Disagreement Beyond Stated Uncertainties",
                   xlabel="",
                   ylabel="G  (\u00d710\u207b\u00b9\u00b9 m\u00b3 kg\u207b\u00b9 s\u207b\u00b2)",
                   size=(16, 10))

# Data from Appendix G
experiments = [
    ('BIPM\n2014', 6.67545, 0.00018, 'Torsion balance\n(servo)', CYAN),
    ('LENS\n2014', 6.67191, 0.00099, 'Atom\ninterferometry', GREEN),
    ('Zurich\n2006', 6.67425, 0.00012, 'Beam\nbalance', BLUE),
    ('HUST-a\n2018', 6.67484, 0.00012, 'Torsion\n(method 1)', ORANGE),
    ('HUST-b\n2018', 6.67349, 0.00018, 'Torsion\n(method 2)', ORANGE),
    ('CODATA\n2018', 6.67430, 0.00015, 'Weighted\naverage', GOLD),
]

x_pos = np.arange(len(experiments))

for i, (name, g_val, g_err, method, color) in enumerate(experiments):
    is_codata = (i == len(experiments) - 1)
    marker_fn = measured_diamond if not is_codata else data_point
    marker_fn(ax, i, g_val, '', color, size=250)
    ax.errorbar([i], [g_val], yerr=[g_err], fmt='none', ecolor=color,
                elinewidth=2, capsize=6, capthick=2, zorder=9)

    # Method label above
    ax.text(i, g_val + 0.0015, method, fontsize=7, color=DIM,
            ha='center', va='bottom')

# CODATA band
codata_g = 6.67430
codata_err = 0.00015
measurement_band(ax, codata_g, codata_err, '', GOLD)

# X labels
ax.set_xticks(x_pos)
ax.set_xticklabels([e[0] for e in experiments], fontsize=9, color=SILVER)

# Spread annotation
g_max = 6.67545
g_min = 6.67191
ax.annotate('', xy=(0, g_max + 0.0003), xytext=(1, g_min - 0.0003),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax.text(3.5, 6.6762, 'Spread: %.5f\n= %.0f ppm' % (g_max - g_min, (g_max - g_min) / codata_g * 1e6),
        fontsize=10, color=RED, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

result_box(ax, 3.5, 6.6710,
           'Different methods, different configurations,\n'
           'different readings \u2014 beyond stated uncertainties.\n'
           'Systematic errors? Or scale-dependent readings?',
           SILVER, 9)

ax.set_xlim(-0.8, 5.8)
ax.set_ylim(6.6700, 6.6770)

save_fig(fig, 'phys2_07_g_disagreements.png')


# ================================================================
# FIG 8: PHYS-2 IDENTITY CARD
# Type: Identity card
# Shows: Running couplings schematic, three boundary types,
# "there are no constants." Visual anchor.
# ================================================================

fig, ax = dark_canvas("PHYS-2 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THERE ARE NO CONSTANTS', fontsize=22,
        color=GOLD, ha='center', fontweight='bold')

ax.text(5, 8.5, 'Every fundamental coupling varies with measurement scale.\n'
        'The word "constant" contradicts the institution\'s own data.',
        fontsize=11, color=SILVER, ha='center')

# Three couplings summary — left
ax.text(2.0, 7.2, 'THE DATA', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

couplings = [
    ('\u03b1 (electromagnetic)', '1/137 \u2192 1/127', '8% variation', BLUE),
    ('\u03b1_s (strong)', 'O(1) \u2192 0.118', '>10\u00d7 variation', RED),
    ('Weak coupling', 'Suppressed \u2192 comparable to \u03b1', 'Qualitative change', GREEN),
    ('G (gravitational)', 'Disagreement between groups', 'Beyond uncertainties', ORANGE),
    ('\u039b (cosmological)', 'QFT vs measured', '10\u00b9\u00b2\u2070 discrepancy', PURPLE),
]

for i, (name, variation, magnitude, color) in enumerate(couplings):
    y = 6.2 - i * 1.0
    ax.text(0.3, y, name, fontsize=9, color=color, fontweight='bold')
    ax.text(2.5, y, variation, fontsize=8, color=SILVER)
    ax.text(2.5, y - 0.35, magnitude, fontsize=8, color=DIM, style='italic')

# Three boundaries — right
ax.text(7.5, 7.2, 'THREE BOUNDARIES', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

boundaries = [
    ('SCREENING', 'Virtual pairs around electron\n\u03b1: weaker outside, stronger inside', CYAN),
    ('CONFINEMENT', 'Gluon field around hadron\n\u03b1_s: stronger outside, weaker inside', RED),
    ('THRESHOLD', 'Quark mass boundaries\nRunning rate changes at each crossing', ORANGE),
]

for i, (name, detail, color) in enumerate(boundaries):
    y = 6.2 - i * 1.5
    ax.text(7.5, y, name, fontsize=11, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(7.5, y - 0.6, detail, fontsize=8, color=SILVER, ha='center')

# The deeper object
ax.plot([0.5, 9.5], [2.5, 2.5], color=DIM, linewidth=1, linestyle=':', alpha=0.4)

ax.text(5, 2.0, 'THE DEEPER OBJECT', fontsize=13, color=GOLD,
        ha='center', fontweight='bold')
ax.text(5, 1.2, 'Not the values \u2014 the transformation laws between them.\n'
        'The beta functions are more fundamental than the couplings.\n'
        'The coupling is the reading. The beta function is the law.',
        fontsize=10, color=SILVER, ha='center')

# Bottom
ax.text(5, 0.3, 'HOWL-PHYS-2: The data says "scale-dependent reading." '
        'The label says "constant." The data will win.',
        fontsize=10, color=GOLD, ha='center', style='italic')

save_fig(fig, 'phys2_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-2 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys2_01_gut_running.png',
    'phys2_02_flavor_thresholds.png',
    'phys2_03_cosmological_scale.png',
    'phys2_04_screening_mechanisms.png',
    'phys2_05_energy_ladder.png',
    'phys2_06_vacuum_polarization.png',
    'phys2_07_g_disagreements.png',
    'phys2_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    