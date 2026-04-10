#!/usr/bin/env python3
"""
HOWL PHYS-43 Diagrams — Separating Clock from Reading
8 figures covering the T/R decomposition, sector splitting prediction,
detection thresholds, EP test landscape, integer chain, and soliton hierarchy.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

# ================================================================
# GLOBAL STYLE
# ================================================================

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

print("PHYS-43 Diagram Script")
print("=" * 50)


# ================================================================
# FIG 1: THE D-K DECOMPOSITION PLANE
# Type: Geometric Cross-Section (D5.4)
# Shows: The two components (Depth D and tick K) as orthogonal axes,
#        the GR dilation as a diagonal vector, and the five tests
#        as projection measurements onto each axis.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-0.5, 10.5)
ax.axis('off')

# Draw axes
ax.annotate('', xy=(10, 0.3), xytext=(0.5, 0.3),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))
ax.annotate('', xy=(0.5, 10), xytext=(0.5, 0.3),
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=2.5))

ax.text(10.2, 0.3, 'Depth Component (D)', color=CYAN, fontsize=13,
        fontweight='bold', va='center')
ax.text(0.5, 10.2, 'Tick Component (K)', color=ORANGE, fontsize=13,
        fontweight='bold', va='bottom', ha='center')

# The GR diagonal vector
ax.annotate('', xy=(8, 8), xytext=(0.8, 0.8),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=3.5))
ax.text(5.5, 5.5, r'GR dilation: $d\tau/dt = \sqrt{1 - 2\Phi/c^2}$',
        color=GOLD, fontsize=12, fontweight='bold', rotation=42,
        ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD, alpha=0.9))

# Projections - dashed lines from GR vector tip to axes
ax.plot([8, 8], [8, 0.3], '--', color=CYAN, lw=1.5, alpha=0.6)
ax.plot([8, 0.5], [8, 8], '--', color=ORANGE, lw=1.5, alpha=0.6)

# Projection labels on axes
ax.plot(8, 0.3, 'o', color=CYAN, markersize=12, zorder=5)
ax.text(8, -0.1, 'D contribution', color=CYAN, fontsize=10, ha='center')
ax.plot(0.5, 8, 'o', color=ORANGE, markersize=12, zorder=5)
ax.text(0.1, 8, 'K contribution', color=ORANGE, fontsize=10, ha='right')

# Five tests as arrows showing what they measure
tests = [
    (1, 'Test 1: Nuclear vs Optical', 7.5, 1.5, 0.85, CYAN,
     'Measures D\nsector dependence'),
    (2, 'Test 2: Pulsar Timing', 6.0, 3.5, 0.6, GREEN,
     'Measures D boundary\nstructure or K density'),
    (3, 'Test 3: Voyager', 5.5, 2.0, 0.75, BLUE,
     'Measures D\nboundary step'),
    (4, 'Test 4: G Scatter', 6.5, 1.0, 0.9, MAG,
     'Measures D\ndepth variation'),
    (5, 'Test 5: Alpha Drift', 1.5, 7.0, 0.15, PURPLE,
     'Measures K\ngeometric tick'),
]

for tnum, label, tx, ty, angle_frac, color, desc in tests:
    # angle_frac: 0 = pure K (vertical), 1 = pure D (horizontal)
    length = 2.0
    angle = angle_frac * np.pi / 2.0
    dx = length * np.sin(angle)
    dy = length * np.cos(angle)
    ax.annotate('', xy=(tx + dx * 0.5, ty + dy * 0.5),
                xytext=(tx - dx * 0.5, ty - dy * 0.5),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
    ax.text(tx + dx * 0.5 + 0.3, ty + dy * 0.5 + 0.15, label,
            color=color, fontsize=9, fontweight='bold', va='bottom')
    ax.text(tx + dx * 0.5 + 0.3, ty + dy * 0.5 - 0.2, desc,
            color=color, fontsize=7, va='top', alpha=0.8)

# Scenario labels in corners
ax.text(9.0, 0.8, 'D-sector\n(all D, no K)', color=CYAN, fontsize=9,
        ha='center', style='italic', alpha=0.7)
ax.text(1.0, 9.0, 'K-local\n(all K, no D)', color=ORANGE, fontsize=9,
        ha='center', style='italic', alpha=0.7)

# Title
ax.text(5.5, 10.0, 'The D-K Decomposition of Time Dilation',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.text(5.5, 9.5,
        'GR measures the diagonal. Five tests project onto each axis.',
        color=SILVER, fontsize=10, ha='center')

save(fig, 'phys43_01_dk_decomposition.png')


# ================================================================
# FIG 2: THE READING DEPTH PROFILE (PHYS-42 FOUNDATION)
# Type: Running/Convergence (D5.1)
# Shows: 18 orders of magnitude of confirmed GR dilation on one
#        plot — all points on ratio=1.0 line. The premise for
#        asking "what hides inside the formula?"
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\Phi/c^2$ or equivalent depth parameter', 'Predicted / Measured')

# Data from PHYS-42 results
names = [
    'Pound-\nRebka', 'GPS\nnet', 'Gravity\nProbe A',
    'Solar\nredshift', 'Mercury\nperihelion', 'Shapiro\n(Cassini)',
    'Hulse-\nTaylor', 'Muon\ndilation', 'SN Ia\nz=1',
    'Planck\nlength', 'Planck\ntime', 'c = lP/tP'
]
phi_values = [
    2.46e-15, 4.5e-10, 4.3e-10,
    2.12e-6, 2.6e-8, 4e-6,
    0.2, 0.9994, 0.5,
    1e-35, 1e-44, 1.0
]
# Use log spacing for x position
x_pos = np.array([
    -15, -9.3, -9.4,
    -5.7, -7.6, -5.4,
    -0.7, -0.0003, -0.3,
    -35, -44, 0
])
# Ratio predicted/measured (all near 1.0)
ratios = [
    2.458e-15/2.57e-15,   # PR: 0.956
    38.50/38.64,           # GPS: 0.996
    4.252e-10/4.36e-10,    # GPA: 0.975
    636.31/636.3,          # Solar: 1.00002
    42.9800/42.9799,       # Mercury: 1.000000023
    1.0/1.000021,          # Cassini: 0.999979
    0.999958,              # HT
    1.0 - 0.00044,         # Muon: 0.99956
    2.0/2.0,               # SN Ia: 1.0
    1.61626e-35/1.616255e-35,  # l_P
    5.39125e-44/5.391247e-44,  # t_P
    1.0                     # c
]
miss_pct = [4.34, 0.35, 2.47, 0.0016, 0.00000278, 0.002,
            0.0042, 0.044, 0.0, 0.00000148, 0.00001026, 0.0]

# Sort by a meaningful x coordinate (log of characteristic depth)
x_sorted = np.linspace(0.5, 11.5, len(names))

colors_pts = [MAG, GREEN, RED, CYAN, GOLD, BLUE,
              PURPLE, ORANGE, PURPLE, SILVER, SILVER, GOLD]

ax.axhline(y=1.0, color=GOLD, lw=1.5, alpha=0.4, ls='--')
ax.axhspan(0.99, 1.01, color=GOLD, alpha=0.05)
ax.axhspan(0.95, 1.05, color=DIM, alpha=0.03)

for i in range(len(names)):
    ax.scatter(x_sorted[i], ratios[i], s=200, color=colors_pts[i],
               linewidth=1.8, zorder=5)
    # Label with miss
    if miss_pct[i] > 0.001:
        label_txt = '%s\n%.2g%%' % (names[i], miss_pct[i])
    elif miss_pct[i] > 0:
        label_txt = '%s\n%.1g ppb' % (names[i], miss_pct[i] * 1e7)
    else:
        label_txt = '%s\n0.0%%' % names[i]
    yoff = 0.012 if i % 2 == 0 else -0.018
    ax.text(x_sorted[i], ratios[i] + yoff, label_txt,
            color=colors_pts[i], fontsize=7, ha='center',
            va='bottom' if yoff > 0 else 'top')

ax.set_xlim(-0.2, 12.5)
ax.set_ylim(0.93, 1.07)
ax.set_xticks([])
ax.set_xlabel('Tests ordered by characteristic depth  (shallow \u2192 deep)',
              color=SILVER, fontsize=11)
ax.set_ylabel('Predicted / Measured', color=SILVER, fontsize=11)

ax.text(6.0, 1.063, 'The Reading Depth Profile \u2014 PHYS-42 Foundation',
        color=GOLD, fontsize=15, fontweight='bold', ha='center')
ax.text(6.0, 1.055,
        '18 orders of magnitude. All on the line. What hides inside the formula?',
        color=SILVER, fontsize=10, ha='center')

# Bands
ax.text(12.2, 1.01, '\u00b11%', color=DIM, fontsize=8, va='center')
ax.text(12.2, 1.05, '\u00b15%', color=DIM, fontsize=8, va='center')

save(fig, 'phys43_02_reading_depth_profile.png')


# ================================================================
# FIG 3: COUPLING RUNNING WITH SECTOR SPLITTING INSET
# Type: Running/Convergence (D5.1)
# Shows: The three gauge couplings running from M_Z to M_GUT with
#        CD-modified betas. An inset magnifies the sector splitting
#        that the beta coefficient differences predict at Earth's Phi/c^2.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(\mu / \mathrm{GeV})$',
         r'$\alpha_i^{-1}(\mu)$')

# One-loop running with CD betas
log_mu = np.linspace(np.log10(91.2), 16, 500)
alpha_em_inv = 137.036
sin2 = 0.23122
k1_inv = 5.0 / 3.0
alpha_1_inv_mz = k1_inv * (1.0 - sin2) * alpha_em_inv  # ~59.01
alpha_2_inv_mz = sin2 * alpha_em_inv                     # ~31.69
alpha_3_inv_mz = 1.0 / 0.118                             # ~8.47

b1 = 25.0 / 6.0
b2 = -13.0 / 6.0
b3 = -20.0 / 3.0

log_mz = np.log10(91.2)
t = log_mu - log_mz

alpha_1 = alpha_1_inv_mz - b1 / (2 * np.pi) * t * 2 * np.pi * np.log(10)
alpha_2 = alpha_2_inv_mz - b2 / (2 * np.pi) * t * 2 * np.pi * np.log(10)
alpha_3 = alpha_3_inv_mz - b3 / (2 * np.pi) * t * 2 * np.pi * np.log(10)

# Simpler: alpha_i^-1(mu) = alpha_i^-1(MZ) - b_i * ln(mu/MZ) / (2*pi)
ln_ratio = t * np.log(10)
alpha_1 = alpha_1_inv_mz - b1 * ln_ratio / (2 * np.pi)
alpha_2 = alpha_2_inv_mz - b2 * ln_ratio / (2 * np.pi)
alpha_3 = alpha_3_inv_mz - b3 * ln_ratio / (2 * np.pi)

ax.plot(log_mu, alpha_1, color=BLUE, lw=2.5, label=r'$\alpha_1^{-1}$ (U(1))')
ax.plot(log_mu, alpha_2, color=GREEN, lw=2.5, label=r'$\alpha_2^{-1}$ (SU(2))')
ax.plot(log_mu, alpha_3, color=RED, lw=2.5, label=r'$\alpha_3^{-1}$ (SU(3))')

# Find crossing
idx_cross = np.argmin(np.abs(alpha_1 - alpha_2))
ax.plot(log_mu[idx_cross], alpha_1[idx_cross], '*', color=GOLD,
        markersize=18, zorder=6)
ax.annotate(r'$M_{GUT} = 10^{15.5}$ GeV', xy=(log_mu[idx_cross], alpha_1[idx_cross]),
            xytext=(log_mu[idx_cross] - 2.5, alpha_1[idx_cross] + 8),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Landmarks
for lm, label in [(np.log10(91.2), r'$M_Z$'), (np.log10(172.7), r'$m_t$')]:
    ax.axvline(lm, color=DIM, lw=1, ls=':', alpha=0.5)
    ax.text(lm, 62, label, color=DIM, fontsize=9, ha='center')

ax.set_xlim(1.5, 16.5)
ax.set_ylim(-5, 68)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper right')

# Title
ax.set_title('Gauge Coupling Unification with CD-Modified Betas',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

# INSET: sector splitting at Earth's potential
ax_inset = fig.add_axes([0.18, 0.18, 0.32, 0.30])
ax_inset.set_facecolor(BG)
for spine in ax_inset.spines.values():
    spine.set_color(GOLD)
    spine.set_linewidth(1.5)
ax_inset.tick_params(colors=DIM, labelsize=8)

# Show the three beta differences as horizontal bars
pairs = [
    (r'$|b_3 - b_1| = 65/6$', 65.0/6.0, CYAN),
    (r'$|b_2 - b_1| = 19/3$', 19.0/3.0, GREEN),
    (r'$|b_3 - b_2| = 9/2$', 9.0/2.0, MAG),
]
y_pos_inset = [2, 1, 0]
for i, (label, val, color) in enumerate(pairs):
    ax_inset.barh(y_pos_inset[i], val, height=0.6, color=color,
                  alpha=0.7, edgecolor=color, linewidth=1.5)
    ax_inset.text(val + 0.2, y_pos_inset[i], label, color=color,
                  fontsize=8, va='center')

ax_inset.set_xlim(0, 14)
ax_inset.set_ylim(-0.5, 3.5)
ax_inset.set_yticks([])
ax_inset.set_xlabel(r'$|\Delta b_{ij}|$ (sector splitting coefficient)',
                     color=SILVER, fontsize=8)
ax_inset.set_title('Sector Splitting from Beta Differences',
                    color=GOLD, fontsize=10, fontweight='bold')
ax_inset.text(7, 3.0,
              r'$\epsilon_{ij} = \kappa \times |\Delta b_{ij}| \times \Delta\Phi/c^2$',
              color=GOLD, fontsize=10, ha='center',
              bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GOLD))

save(fig, 'phys43_03_coupling_running_splitting.png')


# ================================================================
# FIG 4: NUCLEAR VS OPTICAL CLOCK — SPLITTING VS ALTITUDE
# Type: Threshold/Region (D5.3)
# Shows: The predicted frequency ratio change between Th-229 and
#        Sr-87 as a function of altitude, for different kappa values.
#        Detection threshold bands. The margin is the finding.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Altitude above sea level (m)',
         r'$\Delta(f_{Th}/f_{Sr}) / (f_{Th}/f_{Sr})$')

altitudes = np.linspace(0, 3000, 500)
g = 9.82
c2 = (2.998e8)**2
delta_phi = g * altitudes / c2
db_31 = 65.0 / 6.0  # |b3 - b1|

kappa_values = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
colors_k = [GOLD, ORANGE, CYAN, GREEN, BLUE, PURPLE, MAG]
labels_k = [r'$\kappa = 1$', r'$\kappa = 10^{-1}$', r'$\kappa = 10^{-2}$',
            r'$\kappa = 10^{-3}$', r'$\kappa = 10^{-4}$',
            r'$\kappa = 10^{-5}$', r'$\kappa = 10^{-6}$']

for i, (kap, col, lab) in enumerate(zip(kappa_values, colors_k, labels_k)):
    epsilon = kap * db_31 * delta_phi
    ax.semilogy(altitudes, epsilon, color=col, lw=2.0, label=lab,
                alpha=0.9 if i < 4 else 0.7)

# Detection thresholds
ax.axhspan(1e-21, 1e-18, color=GREEN, alpha=0.08)
ax.axhspan(1e-21, 1e-19, color=CYAN, alpha=0.06)
ax.text(2800, 1.5e-18, 'Current optical clock\nprecision ($10^{-18}$)',
        color=GREEN, fontsize=9, ha='right', va='bottom')
ax.text(2800, 1.5e-19, 'Projected Th-229\nprecision ($10^{-19}$)',
        color=CYAN, fontsize=9, ha='right', va='bottom')
ax.axhline(1e-18, color=GREEN, lw=1.5, ls='--', alpha=0.5)
ax.axhline(1e-19, color=CYAN, lw=1.5, ls='--', alpha=0.5)

ax.set_xlim(0, 3100)
ax.set_ylim(1e-21, 1e-8)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9,
          loc='lower right', ncol=2)

ax.set_title('Nuclear vs Optical Clock: Predicted Sector Splitting',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

# Annotation for the margin
ax.annotate(r'$10^6 \times$ margin at $\kappa = 1$',
            xy=(1500, 1e-12), xytext=(500, 1e-10),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

save(fig, 'phys43_04_clock_splitting_altitude.png')


# ================================================================
# FIG 5: KAPPA SWEEP — DETECTION THRESHOLD FOR THREE SECTOR PAIRS
# Type: Threshold/Region (D5.3)
# Shows: log(epsilon) vs log(kappa) for three sector pairs.
#        Three horizontal thresholds. 13 orders of margin visible.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', r'$\log_{10}(\kappa)$',
         r'$\log_{10}(\epsilon_{ij})$ at $\Delta h = 1000$ m')

log_kappa = np.linspace(-9, 1, 500)
delta_phi_1000 = 9.82 * 1000 / (2.998e8)**2  # ~1.09e-13

pairs_data = [
    (r'Strong \u2013 EM: $|\Delta b| = 65/6$', 65.0/6.0, CYAN),
    (r'Weak \u2013 EM: $|\Delta b| = 19/3$', 19.0/3.0, GREEN),
    (r'Strong \u2013 Weak: $|\Delta b| = 9/2$', 9.0/2.0, MAG),
]

for label, db, color in pairs_data:
    log_eps = log_kappa + np.log10(db * delta_phi_1000)
    ax.plot(log_kappa, log_eps, color=color, lw=2.5, label=label)

# Threshold lines
thresholds = [
    (-18, 'Current optical ($10^{-18}$)', GREEN, '--'),
    (-19, 'Projected Th-229 ($10^{-19}$)', CYAN, '--'),
    (-21, 'Space clocks ($10^{-21}$)', PURPLE, ':'),
]
for val, label, color, ls in thresholds:
    ax.axhline(val, color=color, lw=1.5, ls=ls, alpha=0.6)
    ax.text(0.8, val + 0.3, label, color=color, fontsize=9, ha='right')

# Detectable region
ax.fill_between(log_kappa, -18, -8, color=GREEN, alpha=0.04)
ax.text(-4, -9, 'DETECTABLE', color=GREEN, fontsize=14,
        fontweight='bold', ha='center', alpha=0.4)
ax.fill_between(log_kappa, -22, -18, color=RED, alpha=0.03)
ax.text(-4, -20, 'BELOW THRESHOLD', color=RED, fontsize=11,
        ha='center', alpha=0.3)

ax.set_xlim(-9.5, 1.5)
ax.set_ylim(-22, -8)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10,
          loc='upper left')

ax.set_title(r'Sector Splitting vs $\kappa$: Detection Threshold for Three Pairs',
             color=GOLD, fontsize=15, fontweight='bold', pad=12)

# Mark kappa=1 prediction
for label, db, color in pairs_data:
    log_eps_k1 = np.log10(db * delta_phi_1000)
    ax.plot(0, log_eps_k1, 'o', color=color, markersize=10,
            linewidth=1.5, zorder=5)

ax.text(0.3, -11.5, r'$\kappa = 1$ predictions', color=WHITE, fontsize=10)

save(fig, 'phys43_05_kappa_sweep.png')


# ================================================================
# FIG 6: EP TEST LANDSCAPE — CENTURY OF TESTS + CROSS-SECTOR LEAP
# Type: Scale/Landscape (D5.2)
# Shows: 100 years of equivalence principle tests on a log sensitivity
#        axis. All prior tests are same-sector. Test 1 is the first
#        cross-sector. The trend and the novelty are both in the shape.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
setup_ax(ax, '', 'Year', r'Sensitivity $|\eta|$ or fractional precision')

# Historical EP tests (all same-sector)
tests_hist = [
    (1922, 1e-9, u'E\u00f6tv\u00f6s', 'Torsion balance\n(same sector)', DIM),
    (1964, 3e-11, 'Roll-Krotkov-Dicke', 'Torsion balance\n(same sector)', DIM),
    (1969, 1e-12, 'Lunar Laser Ranging', 'Earth-Moon\n(same sector)', SILVER),
    (1999, 1e-13, u'Baessler', 'Torsion balance\n(same sector)', SILVER),
    (2008, 1e-13, 'Atom interferometry', 'Rb-87 vs Rb-85\n(same sector)', BLUE),
    (2012, 1e-13, 'Williams LLR', 'Nordtvedt effect\n(same sector)', SILVER),
    (2017, 1e-14, 'MICROSCOPE', 'Ti vs Pt free fall\n(same sector)', CYAN),
    (2022, 1e-15, 'MICROSCOPE final', 'Ti vs Pt\n(same sector)', CYAN),
    (2022, 1e-18, 'Optical clocks', 'Sr vs Sr at \u0394h\n(same sector)', GREEN),
]

# The cross-sector leap
test_new = (2030, 1e-19, 'PHYS-43 Test 1', 'Th-229 vs Sr-87\nCROSS-SECTOR', GOLD)

years_h = [t[0] for t in tests_hist]
sens_h = [t[1] for t in tests_hist]
colors_h = [t[4] for t in tests_hist]

for yr, sens, name, desc, col in tests_hist:
    ax.scatter(yr, sens, s=180, color=col, linewidth=1.5, zorder=5)
    # Alternate label positions
    yoff_factor = 2.5 if tests_hist.index((yr, sens, name, desc, col)) % 2 == 0 else 0.4
    ax.annotate('%s\n%s' % (name, desc), xy=(yr, sens),
                xytext=(yr, sens * yoff_factor),
                color=col, fontsize=7, ha='center', va='bottom',
                arrowprops=dict(arrowstyle='->', color=col, lw=0.8, alpha=0.5)
                if yoff_factor > 2 else None)

# Cross-sector test — emphasized
yr, sens, name, desc, col = test_new
ax.scatter(yr, sens, s=350, color=col, linewidth=2.5,
           zorder=6, marker='*')
ax.annotate('%s\n%s' % (name, desc), xy=(yr, sens),
            xytext=(yr - 8, sens * 0.01),
            color=col, fontsize=10, fontweight='bold', ha='center',
            arrowprops=dict(arrowstyle='->', color=col, lw=2))

# Trend line through same-sector tests
from numpy.polynomial import polynomial as P
log_sens = np.log10(sens_h)
coeffs = np.polyfit(years_h, log_sens, 1)
trend_years = np.linspace(1920, 2025, 100)
trend_log = np.polyval(coeffs, trend_years)
ax.plot(trend_years, 10**trend_log, '--', color=DIM, lw=1.5, alpha=0.5)

# Dividing annotation
ax.axvline(2025, color=GOLD, lw=1, ls=':', alpha=0.4)
ax.text(1970, 1e-20, 'Same-Sector Tests\n(100 years)', color=SILVER,
        fontsize=12, ha='center', style='italic')
ax.text(2032, 1e-13, 'Cross-Sector\nLeap', color=GOLD,
        fontsize=14, ha='center', fontweight='bold')

ax.set_xlim(1915, 2040)
ax.set_ylim(1e-21, 1e-7)
ax.set_yscale('log')

ax.set_title('Equivalence Principle Tests: A Century of Same-Sector, Then Cross-Sector',
             color=GOLD, fontsize=14, fontweight='bold', pad=12)

save(fig, 'phys43_06_ep_landscape.png')


# ================================================================
# FIG 7: INTEGER CHAIN THROUGH SECTOR SPLITTING
# Type: Connection/Integer Map (D5.5)
# Shows: The beta coefficients that predict sin2_tW and alpha_s
#        also predict epsilon_sector. Each box has a specific Fraction.
#        Arrows carry mathematical relationships.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.axis('off')

def draw_box(ax, x, y, w, h, text, color, fontsize=9, text_color=None):
    rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15',
                           facecolor=BG, edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    tc = text_color if text_color else color
    ax.text(x + w/2, y + h/2, text, color=tc, fontsize=fontsize,
            ha='center', va='center', linespacing=1.4)

def draw_arrow(ax, x1, y1, x2, y2, color, label='', label_pos=0.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    if label:
        mx = x1 + (x2 - x1) * label_pos
        my = y1 + (y2 - y1) * label_pos
        ax.text(mx, my + 0.25, label, color=color, fontsize=8,
                ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.15', facecolor=BG,
                          edgecolor=color, alpha=0.8))

# Central box: Cabibbo Doublet
draw_box(ax, 6.5, 9.5, 5, 1.5, 'Cabibbo Doublet\n(2, 1/3)\nVector-like fermion pair',
         GOLD, fontsize=11)

# Beta coefficients
draw_box(ax, 0.5, 6.5, 3.5, 2,
         r'$b_1^\prime = 25/6$' + '\n' + r'$b_2^\prime = -13/6$' + '\n' + r'$b_3^\prime = -20/3$',
         CYAN, fontsize=11)
draw_arrow(ax, 9, 9.5, 2.5, 8.5, CYAN, r'$\Delta b = (1/15, 1/3, 1/3)$')

# sin2_tW prediction
draw_box(ax, 0.5, 3.5, 3.5, 2,
         r'$\sin^2\theta_W$' + '\n' + r'$= 0.2312$' + '\n12 ppm',
         GREEN, fontsize=10)
draw_arrow(ax, 2.25, 6.5, 2.25, 5.5, GREEN, r'$3/8 - \frac{5\alpha}{12\pi}(b_1-b_2)\ln\frac{M_{GUT}}{M_Z}$')

# alpha_s prediction
draw_box(ax, 0.5, 0.5, 3.5, 2,
         r'$\alpha_s(M_Z)$' + '\n' + r'$= 0.1184$' + '\n0.33%',
         RED, fontsize=10)
draw_arrow(ax, 2.25, 3.5, 2.25, 2.5, RED, 'crossing')

# Beta differences (center column)
draw_box(ax, 6.5, 6.5, 5, 2,
         r'$|b_3 - b_1| = 65/6$' + '\n' +
         r'$|b_2 - b_1| = 19/3$' + '\n' +
         r'$|b_3 - b_2| = 9/2$',
         ORANGE, fontsize=11)
draw_arrow(ax, 4, 7.5, 6.5, 7.5, ORANGE, 'differences')

# Gravitational potential (right column, from GR domain)
draw_box(ax, 13.5, 6.5, 4, 2,
         r'$\Phi_{Earth}/c^2$' + '\n' + r'$= 6.96 \times 10^{-10}$' + '\nfrom PHYS-42',
         MAG, fontsize=10)

# SECTOR SPLITTING (bottom center) — the new prediction
draw_box(ax, 5.5, 1.5, 7, 2.5,
         r'$\epsilon_{sector} = \kappa \times |\Delta b_{ij}| \times \Delta\Phi/c^2$'
         + '\n\n'
         + r'Strong\u2013EM: $\kappa \times (65/6) \times 1.09 \times 10^{-13}$'
         + '\n'
         + r'$= \kappa \times 1.18 \times 10^{-12}$',
         GOLD, fontsize=10)

# Arrows into sector splitting
draw_arrow(ax, 9, 6.5, 9, 4.0, ORANGE, r'$|\Delta b_{ij}|$')
draw_arrow(ax, 15.5, 6.5, 10.5, 4.0, MAG, r'$\Delta\Phi/c^2$')

# Cosmology branch (right side)
draw_box(ax, 13.5, 3.5, 4, 2,
         'DM/baryon\n' + r'$= (22/13)\pi$' + '\n725 ppm',
         PURPLE, fontsize=10)
draw_arrow(ax, 4, 7.0, 6.5, 7.0, PURPLE, '')
draw_arrow(ax, 11.5, 7.0, 13.5, 4.5, PURPLE, 'integers\n22, 13')

# Title
ax.text(9, 11.5, 'Integer Chain Through Sector Splitting',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.text(9, 11.0,
        r'Same $\beta$ coefficients predict $\sin^2\theta_W$, $\alpha_s$, AND clock splitting',
        color=SILVER, fontsize=10, ha='center')

save(fig, 'phys43_07_integer_chain.png')


# ================================================================
# FIG 8: SOLITON HIERARCHY WITH FIVE TEST LOCATIONS
# Type: Geometric Cross-Section (D5.4)
# Shows: Nested soliton boundaries from Planck to cosmos, with
#        physical scales at each level and markers for where each
#        of the five tests probes the hierarchy.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.axis('off')

# Nested circles representing soliton levels
levels = [
    (7.0, 'Cosmos', r'$\Phi/c^2 \sim (1+z)$', PURPLE, 0.12),
    (5.8, 'Galaxy', r'$\Phi/c^2 \sim 10^{-6}$', DIM, 0.18),
    (4.6, 'Heliosphere', r'$\Phi/c^2 \sim 10^{-8}$', BLUE, 0.22),
    (3.4, 'Star (Sun)', r'$\Phi/c^2 = 2.12 \times 10^{-6}$', ORANGE, 0.28),
    (2.2, 'Planet (Earth)', r'$\Phi/c^2 = 6.96 \times 10^{-10}$', GREEN, 0.35),
    (1.3, 'Laboratory', r'$\Delta\Phi/c^2 \sim 10^{-13}$/km', CYAN, 0.45),
    (0.7, 'Atom', r'$\alpha_{em} = 1/137.036$', SILVER, 0.55),
    (0.25, 'Nucleus', r'$\alpha_s = 0.118$', RED, 0.70),
]

for radius, name, phi_label, color, alpha in levels:
    circle = Circle((0, 0), radius, facecolor=color, alpha=alpha * 0.15,
                     edgecolor=color, linewidth=1.5, linestyle='-')
    ax.add_patch(circle)
    # Label at top of circle
    ax.text(0, radius + 0.15, name, color=color, fontsize=10,
            fontweight='bold', ha='center', va='bottom')
    # Scale label at right
    ax.text(radius + 0.2, 0, phi_label, color=color, fontsize=8,
            ha='left', va='center', alpha=0.8)

# Test markers — placed at the hierarchy level they probe
test_markers = [
    (1, 'Test 1:\nNuclear vs\nOptical', 0.5, 0.97, GOLD, 'Nuclear/Atomic\nboundary'),
    (2, 'Test 2:\nPulsar\nTiming', -4.5, 4.5, GREEN, 'Galactic\nstructure'),
    (3, 'Test 3:\nVoyager', 3.5, 3.2, BLUE, 'Heliospheric\nboundary'),
    (4, 'Test 4:\nG Scatter', -1.8, -1.8, MAG, 'Lab/Planetary\nscale'),
    (5, 'Test 5:\n' + r'$\alpha$ Drift', -5.5, -5.5, PURPLE, 'Cosmological\nscale'),
]

for tnum, label, tx, ty, color, desc in test_markers:
    ax.plot(tx, ty, '*', color=color, markersize=20, zorder=6)
    ax.text(tx, ty - 0.5, label, color=color, fontsize=9,
            fontweight='bold', ha='center', va='top')
    ax.text(tx, ty - 1.2, desc, color=color, fontsize=7,
            ha='center', va='top', alpha=0.7)

# Arrows from tests to the hierarchy levels they probe
# Test 1 -> nuclear/atomic boundary
ax.annotate('', xy=(0.25, 0.5), xytext=(0.5, 0.85),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5, alpha=0.5))
# Test 3 -> heliosphere boundary
ax.annotate('', xy=(3.2, 2.8), xytext=(3.4, 3.1),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5, alpha=0.5))

# Center label
ax.text(0, -0.05, 'Planck\n' + r'$\Phi/c^2 = 1$',
        color=GOLD, fontsize=8, ha='center', va='center', fontweight='bold')

# Title
ax.text(0, 7.7, 'The Soliton Hierarchy: Where Each Test Probes',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.text(0, 7.2,
        'Nested boundaries from Planck to Cosmos. Five tests at five levels.',
        color=SILVER, fontsize=10, ha='center')

# Scale bar
ax.plot([-7, -7], [-7, -4], '-', color=DIM, lw=1)
ax.text(-6.8, -5.5, '18 orders\nof magnitude\nin ' + r'$\Phi/c^2$',
        color=DIM, fontsize=8, va='center')

save(fig, 'phys43_08_soliton_hierarchy.png')


# ================================================================
# SUMMARY
# ================================================================
print("=" * 50)
print("All 8 figures saved:")
print("  phys43_01_dk_decomposition.png")
print("  phys43_02_reading_depth_profile.png")
print("  phys43_03_coupling_running_splitting.png")
print("  phys43_04_clock_splitting_altitude.png")
print("  phys43_05_kappa_sweep.png")
print("  phys43_06_ep_landscape.png")
print("  phys43_07_integer_chain.png")
print("  phys43_08_soliton_hierarchy.png")
print("=" * 50)
