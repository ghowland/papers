#!/usr/bin/env python3
"""
HOWL PHYS-42 Diagrams — Reading Depth Across the Soliton Hierarchy
8 figures covering the GR time dilation mega-experiment results.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Wedge
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

outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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
# FIG 1: THE READING DEPTH HIERARCHY
# Type: Type 2 (Scale/Landscape)
# Shows: 18 orders of magnitude in Phi/c^2 with every test placed
#        at its depth — the span IS the result, impossible in text
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='', ylabel='', title='The Reading Depth Hierarchy')

tests = [
    ('Planck horizon',           0,      None,        PURPLE),
    ('Neutron star (HT binary)', -0.7,   '42 ppm',    RED),
    ('Sun surface (redshift)',   -5.67,  '16 ppm',    ORANGE),
    ('Shapiro (solar limb)',     -5.4,   'structural', ORANGE),
    ('Mercury orbit',            -7.42,  '2.8 ppb',   GOLD),
    ('Earth surface',            -9.16,  '0.14%',     CYAN),
    ('GPA (10,000 km)',          -9.4,   '2.47% FAIL', RED),
    ('GPS orbit (20,200 km)',    -9.78,  '0.35%',     GREEN),
    ('Pound-Rebka (22.5 m)',     -14.6,  '4.34%',     BLUE),
    ('Muon SR (gamma=29.3)',     -0.53,  '0.044%',    MAG),
    ('SN Ia (z=1)',              -0.30,  'structural', PURPLE),
]

ax.set_xlim(-0.5, 10)
ax.set_ylim(-16, 1.5)
ax.set_yticks([-15, -12, -9, -6, -3, 0])
ax.set_yticklabels(['$10^{-15}$', '$10^{-12}$', '$10^{-9}$',
                     '$10^{-6}$', '$10^{-3}$', '$10^{0}$'],
                    fontsize=10, color=SILVER)
ax.set_xticks([])
ax.set_ylabel(r'$\Phi/c^2$  (reading depth)', color=SILVER, fontsize=12)

# shaded bands for regimes
ax.axhspan(-16, -12, color=BLUE, alpha=0.04)
ax.axhspan(-12, -6, color=CYAN, alpha=0.04)
ax.axhspan(-6, -1.5, color=ORANGE, alpha=0.04)
ax.axhspan(-1.5, 1.5, color=RED, alpha=0.04)

ax.text(9.5, -14, 'Lab scale', color=DIM, fontsize=8, ha='right', va='center')
ax.text(9.5, -9, 'Earth/orbit', color=DIM, fontsize=8, ha='right', va='center')
ax.text(9.5, -4, 'Stellar', color=DIM, fontsize=8, ha='right', va='center')
ax.text(9.5, -0.2, 'Compact/\ncosmological', color=DIM, fontsize=8,
        ha='right', va='center')

for i, (label, log_phi, miss, color) in enumerate(tests):
    y = log_phi
    x = 1.5
    ax.plot(x, y, 'o', color=color, markersize=12, zorder=5,
            markeredgecolor=WHITE, markeredgewidth=1.5)
    miss_str = '  (%s)' % miss if miss else ''
    ax.text(x + 0.4, y, '%s%s' % (label, miss_str),
            color=color, fontsize=9, va='center', fontweight='bold')

# horizon line
ax.axhline(y=0, color=RED, linewidth=1.5, linestyle='--', alpha=0.5)
ax.text(0.1, 0.3, 'Event horizon: clock stops', color=RED, fontsize=8, alpha=0.7)

# 18 orders annotation
ax.annotate('', xy=(0.5, -14.6), xytext=(0.5, 0),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=1.5))
ax.text(0.15, -7.3, '18 orders\nof magnitude', color=GOLD, fontsize=10,
        ha='center', va='center', rotation=90)

save(fig, 'phys42_01_reading_depth_hierarchy.png')


# ================================================================
# FIG 2: PRECISION VS READING DEPTH
# Type: Type 1 (Chart)
# Shows: correlation (or lack) between depth and measurement
#        precision — reveals input-precision bottleneck pattern
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax,
         xlabel=r'Reading depth  $\log_{10}(\Phi/c^2)$',
         ylabel=r'Miss  $\log_{10}(\mathrm{miss}\;\%)$',
         title='Precision vs Reading Depth')

data = [
    # (label,      log_phi,  log_miss_pct,  color)
    ('Mercury',     -7.42,   np.log10(0.000278),  GOLD),
    ('Planck $l_P$',-0.01,   np.log10(0.00000148),PURPLE),
    ('Solar z',     -5.67,   np.log10(0.0016),    ORANGE),
    ('HT Pdot',    -0.7,    np.log10(0.0042),    RED),
    ('Planck $t_P$',-0.01,   np.log10(0.0000103), PURPLE),
    ('Muon SR',    -0.53,   np.log10(0.044),     MAG),
    ('g surface',  -9.16,   np.log10(0.139),     CYAN),
    ('GPS net',    -9.78,   np.log10(0.35),      GREEN),
    ('GPA',        -9.4,    np.log10(2.47),      RED),
    ('Pound-Rebka',-14.6,   np.log10(4.34),      BLUE),
]

for label, lp, lm, color in data:
    ax.scatter(lp, lm, s=200, color=color, edgecolors=WHITE,
               linewidth=1.5, zorder=5)
    ox = 0.3
    oy = 0.15
    if label == 'Planck $t_P$':
        oy = -0.3
    if label == 'GPA':
        ox = 0.4
        oy = 0.2
    ax.text(lp + ox, lm + oy, label, color=color, fontsize=9,
            fontweight='bold', va='bottom')

# reference bands
ax.axhspan(np.log10(1e-7), np.log10(1e-4), color=GOLD, alpha=0.06)
ax.text(-14, np.log10(3e-6), 'sub-ppm', color=GOLD, fontsize=8, alpha=0.7)
ax.axhspan(np.log10(0.01), np.log10(1.0), color=CYAN, alpha=0.06)
ax.text(-14, np.log10(0.1), 'sub-%', color=CYAN, fontsize=8, alpha=0.7)
ax.axhspan(np.log10(1.0), np.log10(10), color=RED, alpha=0.06)
ax.text(-14, np.log10(3), '>1%', color=RED, fontsize=8, alpha=0.7)

ax.set_xlim(-16, 1.5)
ax.set_ylim(-6, 1.5)

# GPA fail annotation
gpa_x, gpa_y = -9.4, np.log10(2.47)
ax.annotate('FAIL (altitude\napproximation)',
            xy=(gpa_x, gpa_y), xytext=(-6.5, 1.0),
            color=RED, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))

save(fig, 'phys42_02_precision_vs_depth.png')


# ================================================================
# FIG 3: INTEGER-READING DEPTH CONNECTION MAP
# Type: Type 5 (Connection/Integer Map)
# Shows: how the SAME gauge group integers drive both coupling
#        predictions and reading depth measurements — formulas on
#        every arrow, numbers in every box
# ================================================================
fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)
ax.axis('off')

ax.set_title('The Integer\u2013Reading Depth Connection',
             color=GOLD, fontsize=16, fontweight='bold', pad=15)

def draw_box(ax, x, y, w, h, text, color, fontsize=9, textcolor=None):
    tc = textcolor if textcolor else WHITE
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle='round,pad=0.15',
                           facecolor=PAN, edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y, text, color=tc, fontsize=fontsize,
            ha='center', va='center', fontweight='bold')

def draw_arrow(ax, x1, y1, x2, y2, label='', color=DIM, fontsize=8):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx + 0.15, my + 0.15, label, color=color, fontsize=fontsize,
                ha='center', va='bottom')

# Central node: gauge group
draw_box(ax, 9, 10.5, 6.5, 1.0,
         'SU(3) \u00d7 SU(2) \u00d7 U(1)  +  Cabibbo Doublet',
         GOLD, fontsize=11)

# Integer extraction
draw_box(ax, 9, 8.5, 3.5, 0.8,
         'Integers: 11, 13, 22, 38, 27', CYAN, fontsize=10)
draw_arrow(ax, 9, 10.0, 9, 8.9, '', GOLD)

# LEFT BRANCH: Coupling predictions
draw_box(ax, 3.5, 6.8, 3.8, 0.8,
         "b' = (25/6, \u221213/6, \u221220/3)", BLUE, fontsize=9)
draw_arrow(ax, 7.25, 8.3, 5.4, 7.2, 'beta coefficients', BLUE, 8)

draw_box(ax, 2.5, 5.0, 3.2, 0.8,
         'sin\u00b2\u03b8_W = 0.2312\n(12 ppm)', GREEN, fontsize=9)
draw_box(ax, 5.5, 5.0, 2.8, 0.8,
         '\u03b1_s = 0.1184\n(0.33%)', GREEN, fontsize=9)
draw_arrow(ax, 3.0, 6.4, 2.8, 5.4, 'two-loop\ncrossing', GREEN, 7)
draw_arrow(ax, 4.5, 6.4, 5.2, 5.4, 'two-loop\ncrossing', GREEN, 7)

draw_box(ax, 2.5, 3.2, 3.0, 0.8,
         'M_GUT = 10\u00b9\u2075\u00b7\u2076', CYAN, fontsize=9)
draw_arrow(ax, 2.5, 4.6, 2.5, 3.6, '', CYAN)

draw_box(ax, 2.5, 1.5, 3.4, 0.8,
         'DM/baryon = (22/13)\u03c0\n= 5.3165 (725 ppm)', PURPLE, fontsize=9)
draw_arrow(ax, 4.0, 3.2, 3.8, 1.9, '22, 13', PURPLE, 8)

# RIGHT BRANCH: Reading depth hierarchy
draw_box(ax, 14.5, 6.8, 3.5, 0.8,
         'Soliton Hierarchy\n\u03a6/c\u00b2 = GM/(Rc\u00b2)', ORANGE, fontsize=9)
draw_arrow(ax, 10.75, 8.3, 12.75, 7.2, 'reading depth', ORANGE, 8)

draw_box(ax, 12.5, 5.0, 3.0, 0.7,
         'Mercury: 2.8 ppb', GOLD, fontsize=9)
draw_box(ax, 16.0, 5.0, 3.0, 0.7,
         'Solar z: 16 ppm', ORANGE, fontsize=9)
draw_arrow(ax, 13.5, 6.4, 12.8, 5.35, '', GOLD)
draw_arrow(ax, 15.2, 6.4, 15.7, 5.35, '', ORANGE)

draw_box(ax, 12.5, 3.2, 3.0, 0.7,
         'GPS: 0.35%', GREEN, fontsize=9)
draw_box(ax, 16.0, 3.2, 3.0, 0.7,
         'HT: 42 ppm', RED, fontsize=9)
draw_arrow(ax, 12.5, 4.65, 12.5, 3.55, '', GREEN)
draw_arrow(ax, 16.0, 4.65, 16.0, 3.55, '', RED)

draw_box(ax, 14.5, 1.5, 4.0, 0.8,
         'Planck: l_P/t_P = c\n(0.0% miss)', PURPLE, fontsize=9)
draw_arrow(ax, 14.5, 2.8, 14.5, 1.9, '', PURPLE)

# central label
ax.text(9, 7.5, 'same integers\nboth branches',
        color=DIM, fontsize=9, ha='center', va='center',
        style='italic')

save(fig, 'phys42_03_integer_reading_depth_map.png')


# ================================================================
# FIG 4: THE REDSHIFT CURVE — UPDATE RATE VS DEPTH
# Type: Type 1 (Running/Convergence)
# Shows: the Schwarzschild redshift curve shape — linear at
#        shallow depth, bending to zero at horizon. Tests placed
#        on the curve show which regime each probes.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax,
         xlabel=r'Reading depth  $\Phi/c^2$',
         ylabel=r'Update rate  $\sqrt{1 - 2\,\Phi/c^2}$',
         title='The Redshift Curve: Update Rate vs Reading Depth')

phi = np.linspace(0, 0.499, 1000)
update = np.sqrt(1 - 2*phi)
ax.plot(phi, update, color=GOLD, linewidth=2.5, zorder=3)

# linear approximation
linear = 1 - phi
ax.plot(phi[:600], linear[:600], color=DIM, linewidth=1.2, linestyle='--',
        label='Linear approx: 1 \u2212 \u03a6/c\u00b2', zorder=2)

# mark tests on the curve
curve_tests = [
    ('Earth\nsurface',    6.96e-10, GREEN,  0.015, 0.04),
    ('GPS orbit',         1.67e-10, CYAN,   0.015, -0.05),
    ('Solar\nsurface',    2.12e-6,  ORANGE, 0.015, 0.04),
    ('Mercury',           2.6e-8,   GOLD,   0.008, -0.06),
]

# these are too close to zero on linear scale — mark on inset or annotate
# instead mark the strong-field tests that show curvature
strong_tests = [
    ('Neutron star\n(HT binary)', 0.2, RED,    0.02,  0.03),
    ('Planck\nhorizon',           0.48, PURPLE, -0.07, 0.03),
]

for label, phi_val, color, dx, dy in strong_tests:
    u = np.sqrt(1 - 2*phi_val)
    ax.plot(phi_val, u, 'o', color=color, markersize=14,
            markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
    ax.text(phi_val + dx, u + dy, label, color=color, fontsize=9,
            fontweight='bold', va='bottom', ha='center')

# inset for weak-field regime
axins = ax.inset_axes([0.12, 0.12, 0.40, 0.40])
axins.set_facecolor(PAN)
for sp in axins.spines.values():
    sp.set_color(DIM)
    sp.set_linewidth(0.5)
axins.tick_params(colors=DIM, labelsize=7)

phi_weak = np.linspace(0, 5e-6, 500)
update_weak = np.sqrt(1 - 2*phi_weak)
axins.plot(phi_weak, update_weak, color=GOLD, linewidth=2)
axins.plot(phi_weak, 1 - phi_weak, color=DIM, linewidth=1, linestyle='--')

for label, phi_val, color, dx, dy in curve_tests:
    u = np.sqrt(1 - 2*phi_val)
    axins.plot(phi_val, u, 'o', color=color, markersize=10,
               markeredgecolor=WHITE, markeredgewidth=1.5, zorder=5)
    axins.text(phi_val + dx*3e-6, u + dy*2e-6, label, color=color,
               fontsize=7, fontweight='bold', va='bottom', ha='left')

axins.set_xlabel(r'$\Phi/c^2$', color=DIM, fontsize=8)
axins.set_ylabel('Update rate', color=DIM, fontsize=8)
axins.set_title('Weak-field regime (linear)', color=SILVER, fontsize=8)
axins.set_ylim(0.999994, 1.000001)
axins.set_xlim(-1e-7, 5.5e-6)

ax.set_xlim(-0.02, 0.52)
ax.set_ylim(-0.05, 1.08)

# horizon annotation
ax.annotate('Horizon: update rate \u2192 0',
            xy=(0.5, 0), xytext=(0.35, 0.15),
            color=RED, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9)

save(fig, 'phys42_04_redshift_curve.png')


# ================================================================
# FIG 5: MERCURY PERIHELION — READING DEPTH CURVATURE
# Type: Type 4 (Geometric Cross-Section)
# Shows: the rosette orbit pattern from GR precession — what
#        42.98 arcsec/century looks like geometrically. The reading
#        depth gradient near the Sun curves the spatial update path.
# ================================================================
fig, ax = plt.subplots(figsize=(14, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Mercury Perihelion: Reading Depth Curvature',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)

# Solar reading depth gradient as background
for r_frac in np.linspace(0.95, 0.05, 20):
    c_alpha = 0.02 + 0.08 * (1 - r_frac)
    circle = plt.Circle((0, 0), r_frac * 5, color=ORANGE,
                         alpha=c_alpha, linewidth=0)
    ax.add_patch(circle)

# Sun at center
sun = plt.Circle((0, 0), 0.35, color=GOLD, alpha=0.8, zorder=10)
ax.add_patch(sun)
ax.text(0, 0, 'Sun', color=BG, fontsize=10, ha='center', va='center',
        fontweight='bold', zorder=11)

# Draw several orbits with precessing argument of perihelion
# Exaggerate precession to make it visible (actual is 43"/century,
# we show ~15 degrees per orbit for visibility)
a = 3.8   # semi-major axis (plot units)
e = 0.206  # Mercury eccentricity (real)
n_orbits = 8
prec_per_orbit = 15.0  # degrees, EXAGGERATED for visibility

theta = np.linspace(0, 2*np.pi, 500)
for k in range(n_orbits):
    omega = np.radians(k * prec_per_orbit)
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta + omega)
    y = r * np.sin(theta + omega)
    alpha = 0.3 + 0.5 * (k / n_orbits)
    color_orbit = CYAN if k < n_orbits - 1 else WHITE
    lw = 1.0 if k < n_orbits - 1 else 2.0
    ax.plot(x, y, color=color_orbit, linewidth=lw, alpha=alpha)

# Newtonian closed orbit (dashed)
r_newton = a * (1 - e**2) / (1 + e * np.cos(theta))
x_n = r_newton * np.cos(theta)
y_n = r_newton * np.sin(theta)
ax.plot(x_n, y_n, color=DIM, linewidth=1.5, linestyle='--', alpha=0.5,
        label='Newtonian (closed)')

# perihelion markers for first and last orbit
for k in [0, n_orbits - 1]:
    omega = np.radians(k * prec_per_orbit)
    r_peri = a * (1 - e)
    px = r_peri * np.cos(omega)
    py = r_peri * np.sin(omega)
    ax.plot(px, py, 'o', color=GOLD, markersize=8,
            markeredgecolor=WHITE, markeredgewidth=1.5, zorder=15)

# arc showing total precession
total_prec = n_orbits * prec_per_orbit
arc = Wedge((0, 0), 1.5, 0, total_prec, width=0.01,
            color=GOLD, alpha=0.6, zorder=8)
ax.add_patch(arc)
ax.text(1.8, 0.8, '%d\u00b0 shown\n(exaggerated)\n\nActual: 42.98\u2033/century\n'
        'Predicted: 42.9800\u2033/century\nMiss: 2.8 ppb',
        color=GOLD, fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-5.5, 5.5)

ax.text(-4.8, -4.8, 'Reading depth gradient (orange)\ncurves the spatial update path',
        color=ORANGE, fontsize=9, alpha=0.8)
ax.text(-4.8, 4.5, 'Dashed: Newtonian closed orbit\nSolid: GR precessing orbit',
        color=DIM, fontsize=9)

save(fig, 'phys42_05_mercury_perihelion.png')


# ================================================================
# FIG 6: FRAMEWORK PRECISION RANKING — 65 VALUES
# Type: Type 6 (Comparison Bar)
# Shows: all derived values ranked by miss, GR results highlighted
#        — the GR domain contributes 5 of the top 10
# ================================================================
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
style_ax(ax,
         xlabel='Miss (log scale)',
         ylabel='',
         title='Framework Precision Ranking \u2014 65 Derived Values')

# Representative values from the framework (top ~30 shown for readability)
values = [
    # (label, miss_ppm, is_GR)
    (r'$\alpha^{-1}$ vs Rb',         0.007e-3,    False),
    (r'$\alpha^{-1}$ vs CODATA',     0.22e-3,     False),
    ('Mercury perihelion',            0.00278,     True),
    (r'$a_0$ (Bohr radius)',          0.22e-3,     False),
    (r'$\mu_0$ (permeability)',       0.22e-3,     False),
    (r'$R_\infty$ (Rydberg)',         0.44e-3,     False),
    ('Planck length',                 0.0148,      True),
    ('Solar redshift',                16.0,        True),
    ('sin$^2\\theta_W$ (2-loop)',     12.0,        False),
    ('Hulse-Taylor Pdot',             42.0,        True),
    (r'$m_\tau$ (Koide)',             62.0,        False),
    ('Planck time',                   103e-3 * 1e3,True),
    (r'$M_W$ (path B)',               195.0,       False),
    (r'$M_W$ consistency',            207.0,       False),
    ('sin $\\theta_C$ (CD)',          2100.0,      False),
    (r'$R_l$',                        2700.0,      False),
    (r'$V_{ud}$ (4x4)',              264.0,        False),
    ('GPS net shift',                 3500.0,      True),
    (r'$\alpha_s$ (2-loop)',          3300.0,      False),
    ('Muon dilation',                 440.0,       True),
    ('DM/baryon',                     725.0,       False),
    (r'$\Omega_b$',                   727.0,       False),
    ('f(1S-2S)',                       0.44e-3,    False),
    ('g surface',                     1390.0,      True),
    ('D/H',                           1400.0,      False),
    (r'$\Omega_{DE}$',               2000.0,      False),
    ('Pound-Rebka',                   43400.0,     True),
    ('GPA (FAIL)',                     24700.0,    True),
]

# sort by miss
values.sort(key=lambda v: v[1])

n = len(values)
y_pos = np.arange(n)
misses = [v[1] for v in values]
colors = [GOLD if v[2] else CYAN for v in values]
labels = [v[0] for v in values]

bars = ax.barh(y_pos, misses, color=colors, alpha=0.7, height=0.7,
               edgecolor=[GOLD if v[2] else CYAN for v in values],
               linewidth=1.2)

ax.set_xscale('log')
ax.set_xlim(1e-4, 1e5)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=8, color=WHITE)
ax.invert_yaxis()

# regime labels
ax.axvline(x=1, color=DIM, linewidth=0.8, linestyle=':', alpha=0.5)
ax.axvline(x=1000, color=DIM, linewidth=0.8, linestyle=':', alpha=0.5)
ax.text(0.01, -1.5, 'ppb', color=DIM, fontsize=8, ha='center')
ax.text(10, -1.5, 'ppm', color=DIM, fontsize=8, ha='center')
ax.text(10000, -1.5, '%', color=DIM, fontsize=8, ha='center')

# legend
gr_patch = mpatches.Patch(color=GOLD, alpha=0.7, label='GR domain (this paper)')
hw_patch = mpatches.Patch(color=CYAN, alpha=0.7, label='Integer structure domains')
ax.legend(handles=[gr_patch, hw_patch], loc='lower right',
          facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9)

save(fig, 'phys42_06_precision_ranking.png')


# ================================================================
# FIG 7: GRAVITY PROBE A — THE FAIL DIAGNOSIS
# Type: Type 3 (Threshold/Region Chart)
# Shows: the GPA rocket trajectory vs the two-point approximation,
#        the 1% gate, and why the 2.47% miss is an input limitation
# ================================================================
fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax,
         xlabel='Time (minutes)',
         ylabel='Altitude (km)',
         title='Gravity Probe A: Why the Single FAIL')

# Approximate suborbital trajectory (parabolic arc)
# Scout D rocket, ~115 minutes total flight, peak at ~10,000 km
t_total = 115  # minutes
t = np.linspace(0, t_total, 500)
# Parabolic: h(t) = h_max * (1 - ((t - t_peak)/t_peak)^2)
t_peak = t_total / 2
h_max = 10000  # km
altitude = h_max * (1 - ((t - t_peak) / t_peak)**2)
altitude = np.maximum(altitude, 0)

ax.fill_between(t, 0, altitude, color=BLUE, alpha=0.08)
ax.plot(t, altitude, color=BLUE, linewidth=2.5, label='Actual trajectory (approx.)')

# Two-point approximation
ax.axhline(y=h_max, color=ORANGE, linewidth=2, linestyle='--',
           label='Two-point approx. (10,000 km)', alpha=0.8)

# Effective altitude (lower than peak)
h_eff = 7800  # rough effective altitude for trajectory-averaged measurement
ax.axhline(y=h_eff, color=GREEN, linewidth=1.5, linestyle='-.',
           label='Effective altitude (~7,800 km)', alpha=0.7)

# Shaded region: where rocket is below effective altitude
below_mask = altitude < h_eff
ax.fill_between(t, altitude, h_eff, where=(altitude < h_eff) & (altitude > 0),
                color=RED, alpha=0.12)

# Gate annotation on right side (secondary meaning)
ax.text(100, 9200, 'Our prediction:\n\u0394f/f at 10,000 km\n= 4.252 \u00d7 10\u207b\u00b9\u2070',
        color=ORANGE, fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

ax.text(100, 6500, 'Measured (trajectory-\nintegrated):\n= 4.36 \u00d7 10\u207b\u00b9\u2070',
        color=BLUE, fontsize=10, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=BLUE))

# Miss and gate
ax.text(15, 3500,
        'Miss: 2.47%\nGate: < 1%\nResult: FAIL\n\n'
        'Cause: trajectory-integrated\n'
        'measurement vs peak-altitude\n'
        'formula. Rocket spends most\n'
        'of flight below 10,000 km\n'
        '(red shaded region).',
        color=RED, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=RED))

ax.set_xlim(-5, 120)
ax.set_ylim(-500, 11500)

ax.legend(loc='upper right', facecolor=PAN, edgecolor=DIM,
          labelcolor=WHITE, fontsize=9)

# peak label
ax.annotate('Apogee\n~10,000 km', xy=(t_peak, h_max),
            xytext=(t_peak + 12, h_max + 500),
            color=WHITE, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=WHITE, lw=1))

save(fig, 'phys42_07_gpa_fail_diagnosis.png')


# ================================================================
# FIG 8: SOLITON NESTING — THE HIERARCHY CROSS-SECTION
# Type: Type 4 (Geometric Cross-Section)
# Shows: concentric nested solitons from universe to Planck core,
#        with Phi/c^2 at each boundary and tests placed at their
#        corresponding level. Nesting impossible to show in text.
# ================================================================
fig, ax = plt.subplots(figsize=(16, 16))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Soliton Nesting: The Hierarchy Cross-Section',
             color=GOLD, fontsize=16, fontweight='bold', pad=15)

# Nesting levels (outermost to innermost)
levels = [
    ('Universe',       4.8,  PURPLE, 0.06,  'z = 1: SN Ia stretch'),
    ('Galaxy',         4.0,  PURPLE, 0.08,  r'$\Phi/c^2 \sim 10^{-6}$'),
    ('Sun (helio)',    3.2,  ORANGE, 0.10,  'Solar z: 16 ppm'),
    ('Earth (Hill)',   2.4,  CYAN,   0.13,  'GPS: 0.35%'),
    ('Earth surface',  1.6,  GREEN,  0.16,  'P-R: 4.34%'),
    ('Lab (22.5 m)',   0.9,  BLUE,   0.20,  r'$\Delta\Phi/c^2 = 2.5 \times 10^{-15}$'),
    ('Planck core',    0.3,  RED,    0.30,  r'$\Phi/c^2 = 1$'),
]

for label, radius, color, alpha, note in levels:
    circle = plt.Circle((0, 0), radius, facecolor=color, alpha=alpha,
                         edgecolor=color, linewidth=1.5, fill=True)
    ax.add_patch(circle)

# Labels on the right side with leader lines
label_x = 5.5
for i, (label, radius, color, alpha, note) in enumerate(levels):
    y = radius
    ax.plot([radius + 0.05, label_x - 0.3], [y * 0.7, 3.5 - i * 0.95],
            color=color, linewidth=0.8, alpha=0.6)
    ax.text(label_x, 3.5 - i * 0.95,
            '%s\n%s' % (label, note),
            color=color, fontsize=9, fontweight='bold',
            va='center', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG,
                      edgecolor=color, alpha=0.8))

# Tests placed at boundaries (left side)
test_labels = [
    ('Mercury\n2.8 ppb',     3.2, -0.6, GOLD),
    ('HT binary\n42 ppm',    3.8, -2.5, RED),
    ('Muon SR\n0.044%',      2.8, -3.5, MAG),
    ('Shapiro\n\u03b3 = 1',  3.5,  2.5, ORANGE),
]

for label, tx, ty, color in test_labels:
    ax.text(tx * -1, ty, label, color=color, fontsize=9,
            fontweight='bold', ha='right', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG,
                      edgecolor=color, alpha=0.8))

# Reading depth arrow (left side)
ax.annotate('', xy=(0, -4.8), xytext=(0, 4.8),
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))
ax.text(-0.6, -4.5, 'DEEPER\nreading', color=GOLD, fontsize=9,
        ha='center', va='center', fontweight='bold')
ax.text(-0.6, 4.5, 'SHALLOWER\nreading', color=GOLD, fontsize=9,
        ha='center', va='center', fontweight='bold')

# Central core label
ax.text(0, 0, 'Planck\ncore', color=WHITE, fontsize=8,
        ha='center', va='center', fontweight='bold', zorder=20)

ax.set_xlim(-6, 9)
ax.set_ylim(-5.5, 5.5)

save(fig, 'phys42_08_soliton_nesting.png')


# ================================================================
# SUMMARY
# ================================================================
print("\nPHYS-42 Diagrams complete. 8 figures saved:")
print("  phys42_01_reading_depth_hierarchy.png")
print("  phys42_02_precision_vs_depth.png")
print("  phys42_03_integer_reading_depth_map.png")
print("  phys42_04_redshift_curve.png")
print("  phys42_05_mercury_perihelion.png")
print("  phys42_06_precision_ranking.png")
print("  phys42_07_gpa_fail_diagnosis.png")
print("  phys42_08_soliton_nesting.png")
