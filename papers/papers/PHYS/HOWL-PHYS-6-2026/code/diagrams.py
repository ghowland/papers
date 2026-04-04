#!/usr/bin/env python3
"""
HOWL PHYS-6 Diagrams — The Confinement Boundary in Integer Arithmetic
8 figures covering two faces, kernel dependence, 4-loop wall, muon g-2 tension.
Output: PNG files to ../figures/
Uses: data_5_diagram_lib for boilerplate reduction.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_5_diagram_lib import *

set_outdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures'))


# ================================================================
# FIG 1: PERTURBATIVE R=2 VS PHYSICAL R (RHO RESONANCE)
# Type: Running/comparison
# Shows: Below 2 GeV the perturbative R-ratio is flat at R=2
# while the physical R-ratio has the rho peak at 775 MeV and
# wild oscillations. The shapes are completely unrelated.
# The integrals are related by 0.61.
# ================================================================

fig, ax = dark_fig("Below 2 GeV: Perturbative vs Physical R-Ratio",
                   xlabel="\u221as (MeV)",
                   ylabel="R(s) = \u03c3(e\u207ae\u207b\u2192hadrons) / \u03c3(e\u207ae\u207b\u2192\u03bc\u207a\u03bc\u207b)",
                   size=(16, 10))

# Energy range: 300 MeV to 2000 MeV
E = np.linspace(280, 2000, 1000)

# Perturbative: flat at R = 2 (u,d,s quarks)
R_pert = np.ones_like(E) * 2.0

# Physical: approximate with rho, omega, phi resonances
# rho(770): dominant, broad
# omega(782): narrow
# phi(1020): narrow
def breit_wigner(s, m, gamma, peak):
    return peak * (m * gamma)**2 / ((s - m**2)**2 + (m * gamma)**2)

R_phys = np.ones_like(E) * 0.5  # continuum baseline
# rho(770) - broad, dominates
R_phys += breit_wigner(E**2, 775, 149, 4.5 * 775**2)
# omega(782) - narrow spike
R_phys += breit_wigner(E**2, 782, 8.5, 1.5 * 782**2)
# phi(1020) - narrow
R_phys += breit_wigner(E**2, 1020, 4.3, 1.2 * 1020**2)
# rho' and higher
R_phys += breit_wigner(E**2, 1450, 400, 0.8 * 1450**2)
R_phys += breit_wigner(E**2, 1700, 250, 0.3 * 1700**2)

R_phys = np.clip(R_phys, 0.2, 6.0)

curve(ax, E, R_pert, 'Perturbative: R = N_c \u03a3 Q_f\u00b2 = 2 (flat)', ORANGE, 2.5,
      style='--')
curve(ax, E, R_phys, 'Physical: resonances (\u03c1, \u03c9, \u03c6)', CYAN, 2.5)

# Label resonances
ax.annotate('\u03c1(770)', xy=(775, 5.0), xytext=(900, 5.5),
            fontsize=10, color=CYAN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
ax.annotate('\u03c9(782)', xy=(785, 4.2), xytext=(600, 5.5),
            fontsize=9, color=CYAN,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.0))
ax.annotate('\u03c6(1020)', xy=(1020, 3.0), xytext=(1100, 4.5),
            fontsize=9, color=CYAN,
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.0))

# The finding
result_box(ax, 1500, 5.0,
           'Shapes: completely unrelated.\n'
           'Integrals: related by factor 0.61.\n'
           'Confinement transmits 61% of\n'
           'the perturbative VP to the outside.',
           GOLD, 10)

# Pion threshold
ax.plot([280, 280], [0, 6.5], color=RED, linewidth=2, linestyle=':', alpha=0.5)
ax.text(290, 0.3, '\u03c0\u207a\u03c0\u207b\nthreshold\n280 MeV', fontsize=8,
        color=RED, fontweight='bold')

ax.set_xlim(200, 2100)
ax.set_ylim(0, 6.5)

legend(ax, loc='upper right')

save_fig(fig, 'phys6_01_r_ratio_comparison.png')


# ================================================================
# FIG 2: KERNEL COMPARISON — ALPHA_EM VS MUON G-2 WEIGHTING
# Type: Running/comparison (distinct)
# Shows: The alpha_EM kernel (1/s, gentle) vs muon g-2 kernel
# (m_mu^2/s^2, sharp). The muon kernel crushes onto the
# below-2-GeV region where confinement dominates.
# ================================================================

fig, ax = dark_fig("Kernel Comparison: \u03b1_EM (Gentle) vs Muon g-2 (Sharp)",
                   xlabel="\u221as (GeV)",
                   ylabel="Kernel weight (arbitrary units, normalized)",
                   size=(16, 10))

s_vals = np.linspace(0.3, 10, 500)
s_gev2 = s_vals**2

# alpha_EM kernel: ~ 1/s
K_alpha = 1.0 / s_gev2
K_alpha = K_alpha / np.max(K_alpha)

# Muon g-2 kernel: ~ m_mu^2 / s^2 (approximate large-s behavior)
m_mu_gev = 0.10566
K_muon = m_mu_gev**2 / s_gev2**2
# More accurate: full kernel with threshold behavior
K_muon_full = np.where(s_vals > 2 * m_mu_gev,
                        m_mu_gev**4 / (s_gev2 * (s_gev2 + m_mu_gev**2)),
                        0)
K_muon_full = K_muon_full / np.max(K_muon_full) if np.max(K_muon_full) > 0 else K_muon_full

curve(ax, s_vals, K_alpha, '\u03b1_EM kernel ~ 1/s (gentle)', BLUE, 2.5)
curve(ax, s_vals, K_muon_full, 'Muon g-2 kernel ~ m\u03bc\u00b2/s\u00b2 (sharp)', ORANGE, 2.5)

# 2 GeV boundary
ax.plot([2, 2], [0, 1.1], color=GOLD, linewidth=2.5, linestyle='--', alpha=0.7)
ax.text(2.0, 1.05, 'Confinement\nboundary\n~2 GeV', fontsize=10, color=GOLD,
        ha='center', fontweight='bold')

# Shade regions
shaded_region(ax, 0.2, 2.0, RED, 0.08)
shaded_region(ax, 2.0, 10.5, GREEN, 0.04)

ax.text(1.0, 0.85, 'Below 2 GeV\n(non-perturbative)', fontsize=9,
        color=RED, ha='center', fontweight='bold')
ax.text(6.0, 0.85, 'Above 2 GeV\n(perturbative)', fontsize=9,
        color=GREEN, ha='center', fontweight='bold')

# Key insight
result_box(ax, 6.5, 0.5,
           'The muon kernel crushes onto\nthe non-perturbative region.\n\n'
           '\u03b1_EM sees both faces equally.\n'
           'Muon g-2 sees mostly the inside face.\n\n'
           'The confinement correction\nis KERNEL-DEPENDENT.',
           GOLD, 9)

ax.set_xlim(0.2, 10.5)
ax.set_ylim(0, 1.15)

legend(ax, loc='upper right')

save_fig(fig, 'phys6_02_kernel_comparison.png')


# ================================================================
# FIG 3: 4-LOOP WALL — FIVE TRANSCENDENTALS TO ELLIPTIC
# Type: Scale/threshold
# Shows: Through 3-loop: five MATH-2 constants, fully computable
# in integer arithmetic. At 4-loop: elliptic integrals enter,
# six master integrals known only numerically. The wall.
# ================================================================

fig, ax = dark_canvas("The 4-Loop Wall: Where Integer Arithmetic Stops",
                      size=(18, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Three regions left to right: computable, wall, unknown
# Computable region (1-3 loop)
shaded_region(ax, 0.5, 5.5, GREEN, 0.05)
ax.text(3.0, 9.0, 'COMPUTABLE IN INTEGER ARITHMETIC', fontsize=14,
        color=GREEN, ha='center', fontweight='bold')
ax.text(3.0, 8.3, 'Loops 1-3: Five MATH-2 transcendentals', fontsize=11,
        color=SILVER, ha='center')

# The five transcendentals
constants_data = [
    ('A\u2081 = 1/2', '1-loop', 'Rational only', SILVER, 7.2),
    ('\u03c0\u00b2, \u03b6(3), ln(2)', '2-loop', 'Three new constants', CYAN, 6.2),
    ('\u03c0\u2074, \u03b6(5), Li\u2084(\u00bd)', '3-loop', 'Three more (set closes)', BLUE, 5.2),
]

for const, loop, note_text, color, y in constants_data:
    ax.text(1.5, y, loop, fontsize=10, color=DIM, ha='center')
    ax.text(3.0, y, const, fontsize=12, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(4.8, y, note_text, fontsize=9, color=SILVER, ha='center')

# Total
ax.text(3.0, 4.0, 'Total: 5 constants + rationals\nAll MATH-2 integer pairs\nAll Fraction arithmetic',
        fontsize=10, color=GREEN, ha='center', fontweight='bold')

# THE WALL
ax.plot([5.5, 5.5], [0.5, 9.5], color=RED, linewidth=4, linestyle='-', alpha=0.7)
ax.text(5.5, 9.5, 'THE WALL', fontsize=16, color=RED, ha='center',
        fontweight='bold', rotation=0)

# Unknown region (4+ loop)
shaded_region(ax, 5.5, 9.5, RED, 0.03)
ax.text(7.5, 9.0, 'BEYOND INTEGER ARITHMETIC', fontsize=14,
        color=RED, ha='center', fontweight='bold')
ax.text(7.5, 8.3, '4-loop and beyond', fontsize=11, color=SILVER, ha='center')

new_objects = [
    ('Elliptic integrals K(k)', 'New transcendental class', ORANGE, 7.2),
    ('Harmonic polylogarithms\nat roots of unity', 'Reducible to known basis', MAG, 6.2),
    ('6 master integrals', 'Known ONLY to 4800 digits', RED, 5.2),
    ('A\u2085 = ? (5\u03c3 tension)', 'AHKN vs Volkov disagree', RED, 4.2),
]

for obj, note_text, color, y in new_objects:
    ax.text(7.5, y, obj, fontsize=10, color=color, ha='center',
            fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=color))
    ax.text(7.5, y - 0.5, note_text, fontsize=8, color=DIM, ha='center')

# Bottom
ax.text(5.0, 0.8, 'The integer arithmetic computes everything through 3-loop.\n'
        'At 4-loop, elliptic integrals and unknown master integrals enter.\n'
        'The wall is where measurement begins for the coefficients.',
        fontsize=10, color=GOLD, ha='center', fontweight='bold')

save_fig(fig, 'phys6_03_four_loop_wall.png')


# ================================================================
# FIG 4: BELOW-2-GEV TRANSMISSION — 61% THROUGH CONFINEMENT
# Type: Geometric/flow
# Shows: Perturbative VP (2.44) enters the confinement boundary.
# 1.49 (61%) emerges as measured VP. 0.95 (39%) absorbed by
# binding energy. The boundary is a filter.
# ================================================================

fig, ax = dark_canvas("Confinement Transmission: 61% Passes Through",
                      size=(18, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Left: perturbative VP entering
ax.text(1.5, 7.0, 'PERTURBATIVE VP\n(below 2 GeV)', fontsize=13,
        color=ORANGE, ha='center', fontweight='bold')
ax.text(1.5, 5.8, '2.44', fontsize=28, color=ORANGE, ha='center',
        fontweight='bold', fontfamily='monospace')
ax.text(1.5, 4.8, 'Free quarks u, d, s\nR = 2 (flat)\nThreshold: 4.4 MeV',
        fontsize=9, color=SILVER, ha='center')

# Arrow into boundary
ax.annotate('', xy=(3.5, 6.0), xytext=(2.5, 6.0),
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=3))

# The confinement boundary (thick vertical region)
boundary_rect = plt.Rectangle((3.5, 2.0), 1.5, 6.5,
                                facecolor=RED, alpha=0.12, edgecolor=RED,
                                linewidth=3, zorder=2)
ax.add_patch(boundary_rect)
ax.text(4.25, 8.8, 'CONFINEMENT\nBOUNDARY', fontsize=14, color=RED,
        ha='center', fontweight='bold')
ax.text(4.25, 3.0, 'QCD binding\nenergy absorbed\nhere', fontsize=9,
        color=RED, ha='center', style='italic')

# Absorbed portion (downward arrow inside boundary)
ax.annotate('', xy=(4.25, 2.5), xytext=(4.25, 4.5),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2.5))
ax.text(4.25, 2.0, '0.95 absorbed\n(39%)', fontsize=10, color=RED,
        ha='center', fontweight='bold')

# Arrow out of boundary
ax.annotate('', xy=(6.5, 6.0), xytext=(5.0, 6.0),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))

# Right: measured VP emerging
ax.text(8.0, 7.0, 'MEASURED VP\n(below 2 GeV)', fontsize=13,
        color=GREEN, ha='center', fontweight='bold')
ax.text(8.0, 5.8, '1.49', fontsize=28, color=GREEN, ha='center',
        fontweight='bold', fontfamily='monospace')
ax.text(8.0, 4.8, 'Bound hadrons\n\u03c1, \u03c9, \u03c6 resonances\nThreshold: 280 MeV',
        fontsize=9, color=SILVER, ha='center')

# Transmission ratio
result_box(ax, 5.0, 1.0,
           'Transmission: 1.49 / 2.44 = 0.61\n'
           'The boundary transmits 61% of the perturbative VP.\n'
           '39% goes into binding quarks into hadrons.',
           GOLD, 11)

save_fig(fig, 'phys6_04_confinement_transmission.png')


# ================================================================
# FIG 5: TWO FACES — ABOVE/BELOW 2 GEV DUAL PANEL
# Type: Dual-panel comparison
# Shows: Left: above 2 GeV (perturbative matches, ratio ~1.0).
# Right: below 2 GeV (perturbative fails, ratio ~0.61).
# The confinement boundary has two faces.
# ================================================================

fig, ax1, ax2 = dark_fig_dual(
    "Outside Face (above 2 GeV): Ratio \u2248 1.0",
    "Inside Face (below 2 GeV): Ratio \u2248 0.61",
    size=(18, 9), wspace=0.35)

# Left: above 2 GeV
bar_above = [
    ('Perturbative', 2.92, ORANGE),
    ('Measured', 2.92, GREEN),
]
for i, (label, value, color) in enumerate(bar_above):
    ax1.bar(i, value, color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6)
    ax1.text(i, value + 0.1, '%.2f' % value, fontsize=12, color=color,
             ha='center', fontweight='bold')

ax1.set_xticks([0, 1])
ax1.set_xticklabels(['Perturbative', 'Measured'], fontsize=10, color=SILVER)
ax1.set_ylabel('Contribution to \u03b1\u207b\u00b9 running', color=SILVER, fontsize=11)
ax1.set_ylim(0, 4.0)

ax1.text(0.5, 3.5, 'Ratio: \u2248 1.0', fontsize=14, color=GREEN,
         ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))
ax1.text(0.5, 2.8, 'Quark-hadron duality\nholds. Perturbative\ncalculation is correct.',
         fontsize=9, color=SILVER, ha='center')

# Right: below 2 GeV
bar_below = [
    ('Perturbative', 2.44, ORANGE),
    ('Measured', 1.49, GREEN),
]
for i, (label, value, color) in enumerate(bar_below):
    ax2.bar(i, value, color=color, alpha=0.6, edgecolor=color,
            linewidth=2, width=0.6)
    ax2.text(i, value + 0.1, '%.2f' % value, fontsize=12, color=color,
             ha='center', fontweight='bold')

ax2.set_xticks([0, 1])
ax2.set_xticklabels(['Perturbative', 'Measured'], fontsize=10, color=SILVER)
ax2.set_ylim(0, 4.0)

ax2.text(0.5, 3.5, 'Ratio: \u2248 0.61', fontsize=14, color=RED,
         ha='center', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))
ax2.text(0.5, 2.8, 'Confinement reorganizes\nspectrum. 39% absorbed\nby binding energy.',
         fontsize=9, color=SILVER, ha='center')

# Gap arrow in right panel
ax2.annotate('', xy=(0.3, 1.49), xytext=(0.3, 2.44),
             arrowprops=dict(arrowstyle='<->', color=RED, lw=2))
ax2.text(-0.3, 1.95, '\u22120.95\n(39%)', fontsize=10, color=RED,
         ha='center', fontweight='bold')

save_fig(fig, 'phys6_05_two_faces.png')


# ================================================================
# FIG 6: MUON G-2 DECOMPOSITION — TENSION IN HADRONIC SECTOR
# Type: Waterfall/comparison
# Shows: QED + EW + hadronic VP + HLbL = SM prediction vs
# experiment. The 207 x 10^-11 tension is entirely in the
# hadronic bar.
# ================================================================

fig, ax = dark_fig("Muon g-2: The Tension Lives in the Hadronic Sector",
                   xlabel="",
                   ylabel="a_\u03bc (\u00d710\u207b\u00b9\u00b9)",
                   size=(16, 10))

# Components (offset from QED base for visibility)
# Full values: QED = 116584763, EW = 154, had_VP = 6845, HLbL = 92
# Show as deviations from 116584000 for visibility
base = 116584000

components = [
    ('QED\n(integer)', 763, CYAN, '116,584,763'),
    ('EW', 154, BLUE, '+154'),
    ('Had VP\n(measured)', 6845, RED, '+6,845'),
    ('HLbL', 92, MAG, '+92'),
]

running = base
x_pos = 0
bar_width = 0.65

for i, (label, value, color, val_text) in enumerate(components):
    bottom = running - base
    ax.bar(i, value, bottom=bottom, color=color, alpha=0.6,
           edgecolor=color, linewidth=2, width=bar_width)
    # Connector
    if i > 0:
        ax.plot([i - 0.5, i - bar_width / 2], [bottom, bottom],
                color=DIM, linewidth=1, linestyle=':', alpha=0.5)
    # Value
    if value > 500:
        ax.text(i, bottom + value / 2, val_text, fontsize=8, color=WHITE,
                ha='center', va='center', fontweight='bold')
    else:
        ax.text(i, bottom + value + 100, val_text, fontsize=7, color=color,
                ha='center', fontweight='bold')
    running += value

# SM total
sm_total = running - base
ax.bar(4.5, sm_total, color=GREEN, alpha=0.5, edgecolor=GREEN,
       linewidth=2, width=bar_width)
ax.text(4.5, sm_total + 200, 'SM: %d' % (base + sm_total), fontsize=10,
        color=GREEN, ha='center', fontweight='bold')

# Experiment
exp_val = 116592061 - base
ax.bar(6, exp_val, color=GOLD, alpha=0.5, edgecolor=GOLD,
       linewidth=2, width=bar_width)
ax.text(6, exp_val + 200, 'Exp: 116,592,061', fontsize=10,
        color=GOLD, ha='center', fontweight='bold')

ax.set_xticks([0, 1, 2, 3, 4.5, 6])
ax.set_xticklabels(['QED', 'EW', 'Had VP', 'HLbL', 'SM Total', 'Experiment'],
                    fontsize=9, color=SILVER)

# Tension arrow
ax.annotate('', xy=(6, exp_val), xytext=(4.5, sm_total),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2.5))
ax.text(5.25, (sm_total + exp_val) / 2 + 200,
        '\u0394 = 207\n\u2248 3.5\u03c3', fontsize=12, color=RED,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

# Key insight
result_box(ax, 1.5, 7500,
           'QED sector (integer arithmetic): no tension.\n'
           'EW sector (perturbative): no tension.\n'
           'Hadronic sector (crosses confinement): ALL the tension.',
           GOLD, 9)

ax.set_xlim(-0.8, 7.0)
ax.set_ylim(0, 9000)

save_fig(fig, 'phys6_06_muon_g2_decomposition.png')


# ================================================================
# FIG 7: PERTURBATIVE VS PHYSICAL THRESHOLD
# Type: Scale/comparison
# Shows: Perturbative u-quark threshold at 4.4 MeV vs physical
# pion threshold at 280 MeV. The 64x gap IS the confinement
# effect at the threshold level.
# ================================================================

fig, ax = dark_fig("Confinement at the Threshold: Where Hadrons Begin",
                   xlabel="Energy (MeV, log scale)",
                   ylabel="",
                   size=(16, 10))

# Number line from 1 MeV to 2000 MeV
E_line = np.logspace(0, 3.3, 500)

# Perturbative threshold
u_thresh = 4.4  # 2 * m_u
ax.plot([u_thresh, u_thresh], [0.2, 0.8], color=ORANGE, linewidth=3)
data_point(ax, u_thresh, 0.5, '', ORANGE, size=300)
ax.text(u_thresh, 1.2, 'Perturbative\nu-quark threshold\n2m_u = 4.4 MeV',
        fontsize=11, color=ORANGE, ha='center', fontweight='bold')

# Physical threshold
pi_thresh = 280  # 2 * m_pi
ax.plot([pi_thresh, pi_thresh], [0.2, 0.8], color=GREEN, linewidth=3)
data_point(ax, pi_thresh, 0.5, '', GREEN, size=300)
ax.text(pi_thresh, 1.2, 'Physical\npion threshold\n2m_\u03c0 = 280 MeV',
        fontsize=11, color=GREEN, ha='center', fontweight='bold')

# The gap
ax.annotate('', xy=(u_thresh, -0.3), xytext=(pi_thresh, -0.3),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2.5))
ax.text(np.sqrt(u_thresh * pi_thresh), -0.7,
        '64\u00d7 gap\nThis entire range\ndoes NOT EXIST\nin nature',
        fontsize=12, color=RED, ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=RED))

# Shade the forbidden region
ax.fill_between([u_thresh, pi_thresh], [-0.1, -0.1], [1.1, 1.1],
                alpha=0.06, color=RED)

# Rho resonance
rho = 775
ax.plot([rho, rho], [0.3, 0.7], color=CYAN, linewidth=2, alpha=0.7)
ax.text(rho, 1.0, '\u03c1(770)', fontsize=9, color=CYAN, ha='center')

# Confinement scale
ax.plot([2000, 2000], [0.2, 0.8], color=GOLD, linewidth=2, linestyle='--', alpha=0.7)
ax.text(2000, 1.0, '~2 GeV\nconfinement\nscale', fontsize=9, color=GOLD,
        ha='center')

# The line
ax.plot([2, 2500], [0.5, 0.5], color=DIM, linewidth=2, alpha=0.3)

# Bottom note
note(ax, 30, -1.3,
     'The perturbative calculation includes VP from 4.4 to 280 MeV.\n'
     'This energy range does not exist in the physical hadronic spectrum.\n'
     'For the muon g-2 kernel, this wrong contribution dominates \u2192 factor 1300 failure.',
     SILVER, 9)

ax.set_xscale('log')
ax.set_xlim(2, 3000)
ax.set_ylim(-1.8, 1.8)
ax.set_yticks([])

save_fig(fig, 'phys6_07_threshold_comparison.png')


# ================================================================
# FIG 8: PHYS-6 IDENTITY CARD
# Type: Identity card
# Shows: Two faces, PHYS-5 correction, four observables, wall.
# ================================================================

fig, ax = dark_canvas("PHYS-6 Identity Card", size=(18, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.3, 'THE CONFINEMENT BOUNDARY HAS TWO FACES',
        fontsize=18, color=GOLD, ha='center', fontweight='bold')

# Left column: the two faces
ax.text(2.5, 8.0, 'TWO FACES', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

ax.text(2.5, 7.0, 'OUTSIDE (> 2 GeV)', fontsize=12, color=GREEN,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))
ax.text(2.5, 6.3, 'Ratio: \u2248 1.0\nPerturbative = measured\nInteger arithmetic works',
        fontsize=9, color=SILVER, ha='center')

ax.text(2.5, 5.0, 'INSIDE (< 2 GeV)', fontsize=12, color=RED,
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))
ax.text(2.5, 4.3, 'Ratio: \u2248 0.61\n61% transmitted, 39% absorbed\nMeasurement required',
        fontsize=9, color=SILVER, ha='center')

# Middle: PHYS-5 correction
ax.text(5.0, 3.2, 'PHYS-5 CORRECTION', fontsize=12, color=ORANGE,
        ha='center', fontweight='bold')
ax.text(5.0, 2.5, '5/6 = 0.54 \u00d7 1.0 + 0.46 \u00d7 0.61\n'
        '= kernel-weighted average\nnot universal constant',
        fontsize=9, color=SILVER, ha='center')

# Right column: four observables
ax.text(7.5, 8.0, 'FOUR SM OBSERVABLES', fontsize=14, color=WHITE,
        ha='center', fontweight='bold')

observables = [
    ('\u03b1_EM running', '0.02 ppm (PHYS-5)', GREEN),
    ('Gauge couplings', '11 scales, gap ratio 218/115', CYAN),
    ('Electron g-2', 'A\u2081-A\u2083 in Fraction arithmetic', BLUE),
    ('Muon g-2 QED', '3.5\u03c3 tension = hadronic sector', ORANGE),
]

for i, (obs, detail, color) in enumerate(observables):
    y = 7.0 - i * 0.9
    ax.text(7.5, y, obs, fontsize=10, color=color, ha='center',
            fontweight='bold')
    ax.text(7.5, y - 0.35, detail, fontsize=8, color=DIM, ha='center')

# The wall
ax.plot([0.5, 9.5], [1.5, 1.5], color=RED, linewidth=2, linestyle='--', alpha=0.5)
ax.text(5, 1.0, 'THE 4-LOOP WALL', fontsize=12, color=RED,
        ha='center', fontweight='bold')
ax.text(5, 0.4, 'Through 3-loop: 5 transcendentals, all MATH-2 integer pairs.\n'
        'At 4-loop: elliptic integrals + 6 unknown master integrals.\n'
        'Integer arithmetic computes everything on the outside face.',
        fontsize=9, color=SILVER, ha='center')

save_fig(fig, 'phys6_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print()
print("=" * 60)
print("PHYS-6 DIAGRAMS COMPLETE")
print("=" * 60)
filenames = [
    'phys6_01_r_ratio_comparison.png',
    'phys6_02_kernel_comparison.png',
    'phys6_03_four_loop_wall.png',
    'phys6_04_confinement_transmission.png',
    'phys6_05_two_faces.png',
    'phys6_06_muon_g2_decomposition.png',
    'phys6_07_threshold_comparison.png',
    'phys6_08_identity_card.png',
]
for i, f in enumerate(filenames):
    print("  Fig %d: %s" % (i + 1, f))
    