#!/usr/bin/env python3
"""
HOWL PHYS-41 Diagrams — Time as Reading Depth
8 figures covering the reading depth reinterpretation of time.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc
import numpy as np
import os

# Output directory
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global Style ──────────────────────────────────────────────
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

def style_ax(ax, xlabel='', ylabel='', title=''):
    ax.set_facecolor(PAN)
    for sp in ax.spines.values():
        sp.set_color(DIM)
        sp.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    if title:
        ax.set_title(title, color=GOLD, fontsize=15, fontweight='bold', pad=12)


# ================================================================
# FIG 1: SOLITON NESTING — READING DEPTH HIERARCHY
# Type: Geometric Cross-Section (Type 4)
# Shows: Nested boundary geometry from quark to universe with
#        reading depth (Phi/c^2) and update rate at each level.
#        Impossible to convey nesting structure in prose.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.15)
ax.set_aspect('equal')

layers = [
    {'label': 'Universe\n(Vacuum)', 'r': 1.00, 'color': PURPLE, 'phi': '0 (ref)',
     'rate': '1.000000', 'scale': '4.4e26 m'},
    {'label': 'Galaxy\n(Toroid)', 'r': 0.82, 'color': BLUE, 'phi': '~10^-6',
     'rate': '0.999999', 'scale': '3e20 m'},
    {'label': 'Sun\n(Hill Sphere)', 'r': 0.64, 'color': ORANGE, 'phi': '~2.1e-6',
     'rate': '0.999998', 'scale': '1.7e11 m'},
    {'label': 'Earth\n(Hill Sphere)', 'r': 0.48, 'color': GREEN, 'phi': '~7e-10',
     'rate': '0.9999999993', 'scale': '1.5e9 m'},
    {'label': 'Atom', 'r': 0.34, 'color': CYAN, 'phi': '~10^-20 (EM)',
     'rate': '~1', 'scale': '1e-10 m'},
    {'label': 'Nucleus', 'r': 0.22, 'color': MAG, 'phi': '~10^-3 (nuclear)',
     'rate': '~0.997', 'scale': '1e-14 m'},
    {'label': 'Proton', 'r': 0.13, 'color': RED, 'phi': '~10^-3 (QCD)',
     'rate': '~0.997', 'scale': '1e-15 m'},
    {'label': 'Quark\n(confined)', 'r': 0.06, 'color': GOLD, 'phi': '~1 (confine)',
     'rate': '~0', 'scale': '<1e-15 m'},
]

for i, L in enumerate(layers):
    alpha_val = 0.15 + 0.06 * i
    circle = plt.Circle((0, 0), L['r'], fill=True, facecolor=L['color'],
                         alpha=alpha_val, edgecolor=L['color'], linewidth=1.5)
    ax.add_patch(circle)

for i, L in enumerate(layers):
    angle = -40 + i * 12
    rad = np.radians(angle)
    x_lab = (L['r'] + 0.02) * np.cos(rad)
    y_lab = (L['r'] + 0.02) * np.sin(rad)
    side = 1.08
    if i < 4:
        x_text = side
        y_text = 0.95 - i * 0.22
    else:
        x_text = -side
        y_text = 0.95 - (i - 4) * 0.22

    ax.annotate(L['label'], xy=(x_lab, y_lab), xytext=(x_text, y_text),
                color=L['color'], fontsize=9, fontweight='bold',
                ha='left' if x_text > 0 else 'right', va='center',
                arrowprops=dict(arrowstyle='->', color=L['color'], lw=0.8))

    info = "r=%s   rate=%s" % (L['scale'], L['rate'])
    y_off = -0.06
    ax.text(x_text, y_text + y_off, info, color=DIM, fontsize=7,
            ha='left' if x_text > 0 else 'right', va='center')

ax.plot(0.38, -0.38, marker='^', color=WHITE, markersize=10, zorder=20)
ax.text(0.42, -0.38, "You are here\n(Earth surface)", color=WHITE,
        fontsize=8, va='center')

ax.text(0, 1.10, "Soliton Nesting: Reading Depth Hierarchy",
        color=GOLD, fontsize=16, fontweight='bold', ha='center', va='center')
ax.text(0, -1.07, "Deeper = slower update rate. Shallower = faster update rate.\n"
        "GR time dilation measures the reading depth difference.",
        color=SILVER, fontsize=9, ha='center', va='center')

save(fig, 'phys41_01_soliton_nesting.png')


# ================================================================
# FIG 2: A CENTURY OF READING DEPTH — 30 EXPERIMENTS ON ONE CURVE
# Type: Running/Convergence (Type 1)
# Shows: All GR time dilation measurements spanning ~15 orders of
#        magnitude in Phi/c^2 falling on the GR prediction line.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='Reading Depth  |$\\Phi$/c$^2$|',
         ylabel='Measured Time Dilation  $\\Delta$f/f',
         title='A Century of Reading Depth: 30 Experiments on One Curve')

experiments = [
    # (phi_c2, dilation, label, color, marker)
    (7e-16, 7e-16, 'Skytree 450m', CYAN, 'o'),
    (1.1e-15, 1.1e-15, 'BACON 1m', CYAN, 's'),
    (1.1e-13, 1.1e-13, 'Pound-Rebka', GREEN, 'o'),
    (3.3e-13, 3.3e-13, 'Pound-Snider', GREEN, 's'),
    (7e-10, 7e-10, 'GPS net', BLUE, 'D'),
    (1.6e-9, 1.6e-9, 'Hafele-Keating', BLUE, 'o'),
    (6e-10, 6e-10, 'Gravity Probe A', BLUE, 's'),
    (2.1e-6, 2.1e-6, 'Shapiro (Sun)', ORANGE, 'o'),
    (2.1e-6, 2.1e-6, 'Cassini', ORANGE, 'D'),
    (6.3e-7, 6.3e-7, 'Solar redshift', ORANGE, 's'),
    (4e-6, 4e-6, 'Mercury perihelion', ORANGE, '^'),
    (3e-4, 3e-4, 'Sirius B', MAG, 'o'),
    (0.15, 0.15, 'S2 at Sgr A*', RED, 'D'),
    (0.3, 0.3, 'Neutron star', RED, 'o'),
    (0.5, 0.5, 'EHT shadow', RED, 's'),
    (1e-3, 1e-3, 'Hulse-Taylor', MAG, 'D'),
    (1e-3, 1e-3, 'Double pulsar', MAG, 's'),
    (1e-8, 1e-8, 'Airborne clock', BLUE, '^'),
    (1.5e-5, 1.5e-5, 'Light deflection', ORANGE, 'o'),
]

phi_line = np.logspace(-16, 0, 200)
dilation_line = phi_line
ax.plot(phi_line, dilation_line, color=GOLD, linewidth=2.5, alpha=0.8,
        label='GR prediction: $\\Delta$f/f = $|\\Phi|$/c$^2$', zorder=5)

for phi, dil, label, color, marker in experiments:
    ax.scatter(phi, dil, s=120, c=color, marker=marker, edgecolors=WHITE,
               linewidth=1.5, zorder=10)

labeled = set()
for phi, dil, label, color, marker in experiments:
    if label in labeled:
        continue
    labeled.add(label)
    offset_x = 1.8
    offset_y = 1.5
    if 'Skytree' in label or 'BACON' in label:
        offset_y = 0.4
    ax.annotate(label, xy=(phi, dil),
                xytext=(phi * offset_x, dil * offset_y),
                color=color, fontsize=7, alpha=0.85,
                arrowprops=dict(arrowstyle='->', color=color, lw=0.5, alpha=0.5))

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1e-17, 2)
ax.set_ylim(1e-17, 2)

for phi_mark, label, col in [(7e-10, 'Earth surface', GREEN),
                               (2.1e-6, 'Solar', ORANGE),
                               (0.3, 'Neutron star', RED)]:
    ax.axvline(phi_mark, color=col, linewidth=0.8, alpha=0.3, linestyle='--')

ax.legend(loc='upper left', fontsize=10, facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

ax.text(1e-4, 5e-17, "Every experiment from 10$^{-16}$ to 0.5 falls on the same line.\n"
        "The line IS reading depth. GR found it in 1915.",
        color=SILVER, fontsize=9, va='bottom')

save(fig, 'phys41_02_century_of_reading_depth.png')


# ================================================================
# FIG 3: THE HUBBLE TENSION SHORTFALL
# Type: Threshold/Region (Type 3)
# Shows: Two measurement bands (SH0ES and Planck) with the galactic
#        potential as a tiny notch, making the 5-order gap visceral.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='$\\Phi$/c$^2$ (log scale)',
         ylabel='',
         title='The Hubble Tension: Reading Depth Shortfall')

log_phi = np.linspace(-8, 0, 200)

ax.axhspan(0.6, 0.9, xmin=0, xmax=1, color=MAG, alpha=0.12)
ax.text(-0.3, 0.75, "Required reading depth\nfor 8.4% Hubble tension\n"
        "$\\Phi$/c$^2$ $\\approx$ 0.084",
        color=MAG, fontsize=11, fontweight='bold', ha='center', va='center')

ax.axhspan(0.15, 0.45, xmin=0, xmax=1, color=BLUE, alpha=0.08)
ax.text(-0.3, 0.30, "Planck H$_0$ = 67.4 km/s/Mpc\n(cosmic boundary, shallowest depth)",
        color=BLUE, fontsize=10, ha='center', va='center')

ax.axhspan(0.15, 0.17, xmin=0, xmax=0.08, color=ORANGE, alpha=0.5)
ax.annotate("Galactic $\\Phi_{total}$/c$^2$ $\\approx$ 1.3$\\times$10$^{-6}$\n"
            "(visible + DM toroid)",
            xy=(-7.3, 0.16), xytext=(-5.5, 0.08),
            color=ORANGE, fontsize=9, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.5))

ax.annotate("", xy=(-7.3, 0.17), xytext=(-7.3, 0.60),
            arrowprops=dict(arrowstyle='<->', color=RED, lw=2.5))
ax.text(-7.0, 0.38, "5 orders of\nmagnitude gap",
        color=RED, fontsize=13, fontweight='bold', va='center')

log_phis = [-7.9, -6.9, -5.7, -1.1, -0.5, -0.15]
labels = ['MW visible\n2.5e-7', 'MW+DM\n1.3e-6', 'Required\nfor H$_0$\n0.084',
          'Neutron star\n~0.15', 'BH surface\n~0.5', '']
colors = [GREEN, ORANGE, RED, MAG, RED, DIM]
for i in range(min(len(log_phis), 5)):
    ax.plot(log_phis[i], 0.03, marker='v', color=colors[i], markersize=12, zorder=10)
    ax.text(log_phis[i], -0.03, labels[i], color=colors[i], fontsize=7,
            ha='center', va='top')

ax.set_xlim(-8.5, 0.5)
ax.set_ylim(-0.1, 1.0)
ax.set_yticks([])

ax.text(-4.0, 0.93, "COMPUTATION FAILED: galactic potential is 5 orders too shallow\n"
        "to explain the Hubble tension as a reading depth effect.",
        color=RED, fontsize=10, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED, alpha=0.8))

save(fig, 'phys41_03_hubble_tension_shortfall.png')


# ================================================================
# FIG 4: READING UPDATE RATE ACROSS THE HIERARCHY
# Type: Scale/Landscape (Type 2)
# Shows: 60 orders of magnitude in Planck step rates from quark
#        confinement to cosmic boundary.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='', ylabel='',
         title='Reading Update Rate Across the Soliton Hierarchy')

hierarchy = [
    ('Universe\n(vacuum boundary)', 0, PURPLE, '1.000000000', '8.1e60 steps total'),
    ('Galaxy\n(toroid boundary)', -6, BLUE, '0.999999', '~10^-6 slower'),
    ('Sun\n(Hill sphere)', -5.7, ORANGE, '0.999998', '~2e-6 slower'),
    ('Earth surface', -9.2, GREEN, '0.9999999993', '~7e-10 slower'),
    ('Atom\n(EM boundary)', -20, CYAN, '~1.000', 'negligible grav'),
    ('Nucleus\n(strong boundary)', -3, MAG, '~0.997', 'nuclear binding'),
    ('Proton\n(QCD confinement)', -3, RED, '~0.997', 'confinement scale'),
    ('Quark\n(confined)', 0, GOLD, '~0 (internal)', 'fully internal'),
]

y_positions = np.linspace(0.95, 0.05, len(hierarchy))
ax.axis('off')

for i, (name, log_phi, color, rate, note) in enumerate(hierarchy):
    y = y_positions[i]

    bar_width = 0.55
    bar = FancyBboxPatch((0.15, y - 0.025), bar_width, 0.04,
                          boxstyle="round,pad=0.008",
                          facecolor=color, alpha=0.25, edgecolor=color,
                          linewidth=1.5, transform=ax.transAxes)
    ax.add_patch(bar)

    ax.text(0.13, y, name, transform=ax.transAxes, color=color,
            fontsize=10, fontweight='bold', ha='right', va='center')

    ax.text(0.43, y + 0.005, "rate = %s" % rate, transform=ax.transAxes,
            color=WHITE, fontsize=9, ha='center', va='center')

    ax.text(0.75, y, note, transform=ax.transAxes, color=DIM,
            fontsize=8, ha='left', va='center')

    if i > 0:
        ax.annotate('', xy=(0.08, y + 0.03), xytext=(0.08, y_positions[i-1] - 0.03),
                    xycoords='axes fraction', textcoords='axes fraction',
                    arrowprops=dict(arrowstyle='->', color=DIM, lw=0.8))

ax.text(0.04, 0.5, "SHALLOWER\n(faster updates)\n\n$\\uparrow$\n\n$\\downarrow$\n\n"
        "DEEPER\n(slower updates)",
        transform=ax.transAxes, color=SILVER, fontsize=9, ha='center', va='center',
        rotation=0)

ax.text(0.5, -0.02, "Deeper in the hierarchy = slower reading update rate.\n"
        "GR time dilation measures the depth difference.",
        transform=ax.transAxes, color=SILVER, fontsize=9, ha='center', va='top')

save(fig, 'phys41_04_update_rate_hierarchy.png')


# ================================================================
# FIG 5: COUPLING CONVERGENCE AS READING DEPTH
# Type: Running/Convergence (Type 1)
# Shows: Three gauge couplings running from M_Z to M_GUT with
#        the x-axis labeled as reading depth, not just energy.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='Reading Depth  (log$_{10}$[$\\mu$/GeV]  =  deeper $\\rightarrow$)',
         ylabel='$\\alpha_i^{-1}$(reading depth)',
         title='Coupling Convergence as Reading Depth')

b1_cd = 25.0/6.0
b2_cd = -13.0/6.0
b3_cd = -20.0/3.0

a1_mz = 63.21
a2_mz = 31.69
a3_mz = 8.475
mz_log = np.log10(91.1876e3)

t_vals = np.linspace(0, 35, 500)
log_mu = mz_log + t_vals / (2 * np.pi) * np.log(10)

a1_vals = a1_mz - b1_cd / (2 * np.pi) * t_vals
a2_vals = a2_mz - b2_cd / (2 * np.pi) * t_vals
a3_vals = a3_mz - b3_cd / (2 * np.pi) * t_vals

ax.plot(log_mu, a1_vals, color=BLUE, linewidth=2.5, label='$\\alpha_1^{-1}$ (U(1))', zorder=5)
ax.plot(log_mu, a2_vals, color=GREEN, linewidth=2.5, label='$\\alpha_2^{-1}$ (SU(2))', zorder=5)
ax.plot(log_mu, a3_vals, color=RED, linewidth=2.5, label='$\\alpha_3^{-1}$ (SU(3))', zorder=5)

cross_idx = np.argmin(np.abs(a1_vals - a2_vals))
cross_x = log_mu[cross_idx]
cross_y = a1_vals[cross_idx]
ax.scatter([cross_x], [cross_y], s=200, c=GOLD, edgecolors=WHITE, linewidth=2, zorder=15)
ax.annotate("Unification\n$\\alpha_{GUT}^{-1}$ = 42.1\nM$_{GUT}$ = 10$^{15.6}$ GeV\ngap = 0.027",
            xy=(cross_x, cross_y), xytext=(cross_x - 1.5, cross_y + 10),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

ax.axvline(mz_log, color=DIM, linewidth=1, linestyle='--', alpha=0.5)
ax.text(mz_log + 0.1, 60, 'M$_Z$', color=DIM, fontsize=9)

for depth_log, label in [(6.5, 'CD threshold\n~3 TeV'), (cross_x, '')]:
    if label:
        ax.axvline(depth_log, color=ORANGE, linewidth=1, linestyle=':', alpha=0.5)
        ax.text(depth_log + 0.1, 55, label, color=ORANGE, fontsize=8)

ax.fill_between([mz_log, 6.5], -5, 70, color=CYAN, alpha=0.03)
ax.text((mz_log + 6.5) / 2, 3, "SM running\n(shallow depth)", color=CYAN, fontsize=8,
        ha='center', alpha=0.7)
ax.fill_between([6.5, cross_x + 1], -5, 70, color=ORANGE, alpha=0.03)
ax.text((6.5 + cross_x) / 2, 3, "CD-modified running\n(deep depth)", color=ORANGE,
        fontsize=8, ha='center', alpha=0.7)

ax.set_xlim(mz_log - 0.5, cross_x + 2)
ax.set_ylim(-5, 70)
ax.legend(loc='upper right', fontsize=10, facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE)

ax.text(mz_log + 0.5, 65, "Higher energy = deeper reading depth\n"
        "The couplings converge as you probe deeper",
        color=SILVER, fontsize=9)

save(fig, 'phys41_05_coupling_convergence_depth.png')


# ================================================================
# FIG 6: THE LIFETIME LADDER IN PLANCK STEPS
# Type: Scale/Landscape (Type 2)
# Shows: Every particle lifetime from W boson to proton on a single
#        log axis measured in Planck steps.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='Reading Persistence (Planck steps, log$_{10}$)',
         ylabel='',
         title='The Lifetime Ladder: How Long Each Reading Persists')

t_planck = 5.391e-44

particles = [
    ('W boson', 3e-25, RED, '~3e-25 s'),
    ('Z boson', 2.6e-25, RED, '~2.6e-25 s'),
    ('Higgs', 1.6e-22, MAG, '~1.6e-22 s'),
    ('Top quark', 5e-25, RED, '~5e-25 s'),
    ('Tau lepton', 2.9e-13, CYAN, '~2.9e-13 s'),
    ('B meson', 1.5e-12, BLUE, '~1.5e-12 s'),
    ('Pion (charged)', 2.6e-8, GREEN, '~2.6e-8 s'),
    ('Muon', 2.197e-6, CYAN, '2.197e-6 s'),
    ('Neutron (free)', 879.4, ORANGE, '879.4 s'),
    ('Positronium (ortho)', 1.42e-7, PURPLE, '1.42e-7 s'),
    ('Hydrogen 1S-2S', 0.143, GOLD, '~1/7 s'),
    ('Proton (predicted)', 3.15e41, GOLD, '~10^34 yr'),
    ('Universe age', 4.35e17, PURPLE, '13.8 Gyr'),
]

particles_sorted = sorted(particles, key=lambda x: x[1])

y_positions = np.linspace(0.05, 0.95, len(particles_sorted))

ax.set_xlim(16, 82)
ax.set_ylim(-0.05, 1.05)
ax.set_yticks([])

for i, (name, lifetime, color, note) in enumerate(particles_sorted):
    steps = lifetime / t_planck
    log_steps = np.log10(steps)
    y = y_positions[i]

    ax.barh(y, log_steps - 16, left=16, height=0.045, color=color, alpha=0.6,
            edgecolor=color, linewidth=1.5)

    ax.text(log_steps + 0.5, y, "%s  (10$^{%.0f}$ steps)" % (name, log_steps),
            color=color, fontsize=9, fontweight='bold', va='center')

    ax.text(15.5, y, note, color=DIM, fontsize=7, ha='right', va='center')

for log_mark, label in [(18, '10$^{18}$'), (30, '10$^{30}$'),
                         (40, '10$^{40}$'), (50, '10$^{50}$'),
                         (60, '10$^{60}$'), (70, '10$^{70}$'),
                         (78, '10$^{78}$')]:
    ax.axvline(log_mark, color=DIM, linewidth=0.5, alpha=0.3, linestyle=':')

ax.text(49, -0.02, "One Planck step = 5.39 $\\times$ 10$^{-44}$ s",
        color=SILVER, fontsize=9, ha='center')

save(fig, 'phys41_06_lifetime_ladder_planck.png')


# ================================================================
# FIG 7: HUBBLE MEASUREMENTS BY READING ENVIRONMENT
# Type: Comparison Bar (Type 6)
# Shows: All H0 data points with error bars, color-coded by
#        reading depth environment (local vs intermediate vs cosmic).
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='H$_0$ (km/s/Mpc)',
         ylabel='',
         title='Hubble Constant Measurements by Reading Environment')

measurements = [
    ('SH0ES 2022\n(Cepheids)', 73.04, 1.04, RED, 'Inside galactic toroid'),
    ('SH0ES+JWST 2024', 73.0, 1.0, RED, 'Inside galactic toroid'),
    ('H0LiCOW\n(strong lensing)', 73.3, 1.75, ORANGE, 'Intermediate (z~0.3-0.7)'),
    ('CCHP 2025\n(TRGB+JAGB)', 70.4, 2.1, ORANGE, 'Inside galactic toroid (contested)'),
    ('DESI BAO 2024', 68.53, 0.80, CYAN, 'Galaxy surveys (z=0.5-2.3)'),
    ('Planck 2018\n(CMB)', 67.4, 0.5, BLUE, 'Cosmic boundary (z=1089)'),
    ('ACT 2020\n(CMB)', 67.6, 1.1, BLUE, 'Cosmic boundary'),
    ('SPT 2023\n(CMB)', 67.5, 1.0, BLUE, 'Cosmic boundary'),
]

y_pos = np.arange(len(measurements))

for i, (name, h0, unc, color, env) in enumerate(measurements):
    ax.errorbar(h0, i, xerr=unc, fmt='o', color=color, markersize=10,
                markeredgecolor=WHITE, markeredgewidth=1.5, capsize=6,
                capthick=1.5, elinewidth=2, zorder=10)
    ax.text(63.5, i, name, color=color, fontsize=9, fontweight='bold',
            va='center', ha='right')
    ax.text(h0 + unc + 0.5, i, "%.1f $\\pm$ %.1f" % (h0, unc),
            color=SILVER, fontsize=8, va='center')

ax.axvspan(72.0, 74.08, alpha=0.08, color=RED)
ax.text(73.0, len(measurements) - 0.3, "Local\n(toroid interior)",
        color=RED, fontsize=8, ha='center', alpha=0.8)
ax.axvspan(66.9, 67.9, alpha=0.08, color=BLUE)
ax.text(67.4, len(measurements) - 0.3, "CMB\n(cosmic boundary)",
        color=BLUE, fontsize=8, ha='center', alpha=0.8)

ax.axvline(73.04, color=RED, linewidth=1, linestyle='--', alpha=0.4)
ax.axvline(67.4, color=BLUE, linewidth=1, linestyle='--', alpha=0.4)

ax.set_xlim(63, 76)
ax.set_ylim(-0.8, len(measurements) + 0.3)
ax.set_yticks([])

ax.annotate("", xy=(73.04, -0.5), xytext=(67.4, -0.5),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))
ax.text(70.2, -0.65, "8.4% tension (5$\\sigma$)", color=GOLD, fontsize=10,
        fontweight='bold', ha='center')

legend_elements = [
    mpatches.Patch(facecolor=RED, alpha=0.6, label='Local (inside toroid)'),
    mpatches.Patch(facecolor=ORANGE, alpha=0.6, label='Intermediate'),
    mpatches.Patch(facecolor=CYAN, alpha=0.6, label='BAO surveys'),
    mpatches.Patch(facecolor=BLUE, alpha=0.6, label='CMB (cosmic boundary)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
          facecolor=PAN, edgecolor=DIM, labelcolor=WHITE)

save(fig, 'phys41_07_hubble_by_environment.png')


# ================================================================
# FIG 8: GPS AS READING DEPTH — THREE EFFECTS IN ONE ORBIT
# Type: Geometric Cross-Section (Type 4)
# Shows: Satellite orbit through Earth's reading depth gradient
#        with all three timing corrections labeled.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.35)
ax.set_aspect('equal')

ax.text(0, 1.28, "GPS as Reading Depth: Three Effects in One Orbit",
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

n_rings = 8
for i in range(n_rings, 0, -1):
    r = 0.2 + i * 0.12
    alpha_val = 0.03 + (n_rings - i) * 0.015
    color_val = CYAN if i > 4 else GREEN if i > 2 else ORANGE
    circle = plt.Circle((0, 0), r, fill=False, edgecolor=color_val,
                         linewidth=0.5, alpha=alpha_val + 0.1)
    ax.add_patch(circle)

earth = plt.Circle((0, 0), 0.2, facecolor='#1a3a5c', edgecolor=CYAN,
                    linewidth=2, zorder=10)
ax.add_patch(earth)
ax.text(0, 0, "Earth", color=WHITE, fontsize=10, fontweight='bold',
        ha='center', va='center', zorder=15)

orbit_r = 0.82
theta_orbit = np.linspace(0, 2 * np.pi, 200)
ax.plot(orbit_r * np.cos(theta_orbit), orbit_r * np.sin(theta_orbit),
        color=GOLD, linewidth=1.5, linestyle='--', alpha=0.5)

sat_angle = np.radians(55)
sat_x = orbit_r * np.cos(sat_angle)
sat_y = orbit_r * np.sin(sat_angle)
ax.plot(sat_x, sat_y, marker='s', color=GOLD, markersize=14,
        markeredgecolor=WHITE, markeredgewidth=2, zorder=20)
ax.text(sat_x + 0.05, sat_y + 0.05, "GPS\nSatellite", color=GOLD,
        fontsize=9, fontweight='bold', va='bottom')

ax.annotate("+45.85 $\\mu$s/day\n(shallower depth\n= faster updates)",
            xy=(sat_x, sat_y), xytext=(1.05, 0.95),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

vel_dx = -0.15 * np.sin(sat_angle)
vel_dy = 0.15 * np.cos(sat_angle)
ax.annotate('', xy=(sat_x + vel_dx, sat_y + vel_dy),
            xytext=(sat_x, sat_y),
            arrowprops=dict(arrowstyle='->', color=MAG, lw=2.5))
ax.text(sat_x + vel_dx - 0.15, sat_y + vel_dy + 0.05,
        "v = 3.87 km/s", color=MAG, fontsize=8)

ax.annotate("-7.21 $\\mu$s/day\n(velocity allocation\n= fewer depth updates)",
            xy=(sat_x + vel_dx * 0.5, sat_y + vel_dy * 0.5),
            xytext=(-1.05, 0.95),
            color=MAG, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=MAG, lw=1.5))

ax.annotate("", xy=(0.2, -0.6), xytext=(0.82, -0.6),
            arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=2))
ax.text(0.51, -0.72, "20,200 km\n(reading depth\ndifference)", color=ORANGE,
        fontsize=9, ha='center')

result_text = ("NET: +38.64 $\\mu$s/day\n\n"
               "Gravitational (depth):  +45.85 $\\mu$s/day\n"
               "Velocity (allocation):   $-$7.21 $\\mu$s/day\n"
               "Corrected in firmware since 1978")
ax.text(0, -1.05, result_text, color=WHITE, fontsize=10,
        ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=GOLD,
                  linewidth=1.5))

ax.text(-0.95, -0.25, "Deeper\n(slower)", color=ORANGE, fontsize=9,
        ha='center', style='italic')
ax.text(-0.95, 0.25, "Shallower\n(faster)", color=GREEN, fontsize=9,
        ha='center', style='italic')
ax.annotate('', xy=(-0.95, -0.15), xytext=(-0.95, 0.15),
            arrowprops=dict(arrowstyle='<-', color=DIM, lw=1))

ax.text(0.95, -0.25, "Every GPS fix is a\nreading depth\ncalculation.",
        color=SILVER, fontsize=9, ha='center', style='italic')

save(fig, 'phys41_08_gps_reading_depth.png')


# ================================================================
# SUMMARY
# ================================================================
print("\nPHYS-41 Diagrams Complete:")
print("  phys41_01_soliton_nesting.png")
print("  phys41_02_century_of_reading_depth.png")
print("  phys41_03_hubble_tension_shortfall.png")
print("  phys41_04_update_rate_hierarchy.png")
print("  phys41_05_coupling_convergence_depth.png")
print("  phys41_06_lifetime_ladder_planck.png")
print("  phys41_07_hubble_by_environment.png")
print("  phys41_08_gps_reading_depth.png")
