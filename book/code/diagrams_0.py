#!/usr/bin/env python3
"""
HOWL Book Diagrams — The Rational Universe
8 figures covering nested soliton hierarchy, toroidal galaxy, coupling running,
QED chain, cosmological chain, proton decay, eight-domain graph, identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Arc, Wedge
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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


def save(fig, name):
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=180, facecolor=BG, bbox_inches='tight', pad_inches=0.3)
    plt.close(fig)
    print("  Saved: %s" % name)

def style_ax(ax, title='', xlabel='', ylabel=''):
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

# ── Physics data ──
alpha_em_inv = 137.035999177
sin2_tw = 0.23122
alpha_s_meas = 0.1180
k1 = 3.0 / 5.0

alpha_1_inv_mz = k1 * (1.0 - sin2_tw) * alpha_em_inv
alpha_2_inv_mz = sin2_tw * alpha_em_inv
alpha_3_inv_mz = 1.0 / alpha_s_meas

# Betas
b1_sm, b2_sm, b3_sm = 41.0/10, -19.0/6, -7.0
b1_cd, b2_cd, b3_cd = 25.0/6, -13.0/6, -20.0/3

# Two-loop b_ij
bij_sm = np.array([
    [199.0/50, 27.0/10, 44.0/5],
    [9.0/10, 35.0/6, 12.0],
    [11.0/10, 9.0/2, -26.0]
])
dbij_cd = np.array([
    [7.0/15, 1.0/15, 16.0/135],
    [1.0/30, 15.0/4, 8.0/3],
    [1.0/45, 1.0, 40.0/9]
])
bij_total = bij_sm + dbij_cd

gauge_colors = [BLUE, GREEN, RED]
gauge_labels = [r'$\alpha_1^{-1}$ (U(1))', r'$\alpha_2^{-1}$ (SU(2))', r'$\alpha_3^{-1}$ (SU(3))']

def run_two_loop(alpha_invs, betas, bij, t_max, n_pts=2000):
    dt = t_max / n_pts
    ts = [0.0]
    a = list(alpha_invs)
    curves = [[a[0]], [a[1]], [a[2]]]
    two_pi = 2.0 * np.pi
    eight_pi2 = 8.0 * np.pi**2
    for _ in range(n_pts):
        alphas = [1.0/ai if ai > 0.1 else 0.0 for ai in a]
        da = [0.0, 0.0, 0.0]
        for i in range(3):
            da[i] = -betas[i] / two_pi
            for j in range(3):
                da[i] -= bij[i][j] * alphas[j] / eight_pi2
        a = [a[i] + da[i] * dt for i in range(3)]
        ts.append(ts[-1] + dt)
        for i in range(3):
            curves[i].append(a[i])
    return np.array(ts), [np.array(c) for c in curves]


# ================================================================
# FIG 1: NESTED SOLITON HIERARCHY — QUARK TO UNIVERSE
# Type: Type 2 (Scale/Landscape) + Type 4 (Geometric Cross-Section)
# Shows: Concentric nesting at log scale with boundary readings
# ================================================================

fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 14)

# Concentric circles representing nesting levels, centered at (8, 7)
cx, cy = 8, 7
levels = [
    (0.4,  'Quark',          r'$\alpha_s \approx 1$',        RED,    '~$10^{-18}$ m'),
    (0.9,  'Proton',         r'$\alpha_s = 0.118$',          ORANGE, '~$10^{-15}$ m'),
    (1.5,  'Atom',           r'$\alpha = 1/137$',            CYAN,   '~$10^{-10}$ m'),
    (2.3,  'Earth',          'G = 6.674e-11',                GREEN,  '~$10^{7}$ m'),
    (3.2,  'Hill Sphere',    'Orbital reading',              BLUE,   '~$10^{9}$ m'),
    (4.2,  'Sun',            'Solar Hill sphere',            GOLD,   '~$10^{13}$ m'),
    (5.3,  'Galaxy (toroid)', 'DM = (22/13)' + r'$\pi$',    PURPLE, '~$10^{21}$ m'),
    (6.2,  'Universe',       r'$\Omega_{total} = 1$',       DIM,    '~$10^{26}$ m'),
]

for i, (r, name, reading, col, scale) in enumerate(levels):
    alpha_val = 0.12 + 0.06 * (len(levels) - i) / len(levels)
    if i == len(levels) - 1:
        # Universe: draw as rectangle filling most of the figure
        rect = FancyBboxPatch((cx - 6.5, cy - 6.5), 13, 13, boxstyle='round,pad=0.3',
                              facecolor=PAN, edgecolor=col, linewidth=1.2, alpha=0.3, zorder=1)
        ax.add_patch(rect)
    elif name == 'Galaxy (toroid)':
        # Draw as an ellipse to suggest toroid cross-section
        ell = Ellipse((cx, cy), width=2*r, height=r*0.7, fill=False,
                      edgecolor=col, linewidth=2, alpha=0.7, zorder=2 + i)
        ax.add_patch(ell)
    else:
        circle = plt.Circle((cx, cy), r, fill=False, edgecolor=col,
                            linewidth=1.8, alpha=0.7, zorder=2 + i)
        ax.add_patch(circle)

    # Labels — spread along right side, one row per level
    lx = cx + max(r, 0.5) + 0.4
    ly = cy - 3.5 + i * 1.1
    if lx > 14.5:
        lx = 14.5
    ax.annotate(name, xy=(cx + r * 0.9, cy), xytext=(lx, ly + 0.25),
                color=col, fontsize=10, fontweight='bold', va='center',
                arrowprops=dict(arrowstyle='-', color=col, lw=0.6, alpha=0.4))
    ax.text(lx, ly - 0.05, reading, color=SILVER, fontsize=8, va='center')
    ax.text(lx, ly - 0.35, scale, color=DIM, fontsize=7, va='center')

# Title
ax.text(8, 13.5, 'Nested Soliton Boundaries: Quark to Universe',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.text(8, 0.5, 'Each boundary separates an inside reading from an outside reading.\n'
        'The same structure at every scale.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'book_01_nested_solitons.png')


# ================================================================
# FIG 2: TOROIDAL GALAXY CROSS-SECTION
# Type: Type 4 (Geometric Cross-Section)
# Shows: Toroidal flow pattern with disc, halo, and circulation arrows
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)

cx, cy = 8, 6

# Outer halo (toroidal envelope) — large ellipse
halo = Ellipse((cx, cy), 12, 8, fill=True, facecolor='#0d0d1a', edgecolor=PURPLE,
               linewidth=1.5, alpha=0.4, zorder=1)
ax.add_patch(halo)

# Toroidal cross-section: two circles (left and right lobes of the torus meridional cut)
lobe_r = 2.5
lobe_offset = 3.0
left_lobe = plt.Circle((cx - lobe_offset, cy), lobe_r, fill=True,
                        facecolor='#15152a', edgecolor=PURPLE, linewidth=1.2, alpha=0.5, zorder=2)
right_lobe = plt.Circle((cx + lobe_offset, cy), lobe_r, fill=True,
                         facecolor='#15152a', edgecolor=PURPLE, linewidth=1.2, alpha=0.5, zorder=2)
ax.add_patch(left_lobe)
ax.add_patch(right_lobe)

# Disc (equatorial plane) — horizontal line through center
ax.plot([cx - 5.5, cx - 0.5], [cy, cy], color=GOLD, linewidth=2.5, zorder=5)
ax.plot([cx + 0.5, cx + 5.5], [cy, cy], color=GOLD, linewidth=2.5, zorder=5)
# Stars on disc
star_x = np.array([-5, -4.2, -3.5, -2.7, -2, -1.2, 1.2, 2, 2.7, 3.5, 4.2, 5])
for sx in star_x:
    ax.scatter([cx + sx], [cy], color=GOLD, s=15, zorder=6, edgecolors='none', alpha=0.8)

# Central bulge
bulge = Ellipse((cx, cy), 1.2, 0.8, facecolor=ORANGE, edgecolor=GOLD,
                linewidth=1, alpha=0.3, zorder=4)
ax.add_patch(bulge)

# Circulation arrows — showing toroidal flow
arrow_style = dict(arrowstyle='->', color=CYAN, lw=1.8, alpha=0.7)
# Up from disc on left
ax.annotate('', xy=(cx - 3, cy + 2.2), xytext=(cx - 4, cy + 0.5), arrowprops=arrow_style)
# Around top
ax.annotate('', xy=(cx, cy + 3.5), xytext=(cx - 2.5, cy + 2.8), arrowprops=arrow_style)
# Down on right
ax.annotate('', xy=(cx + 3, cy + 2.2), xytext=(cx + 1, cy + 3.2), arrowprops=arrow_style)
ax.annotate('', xy=(cx + 4, cy + 0.5), xytext=(cx + 3.5, cy + 2), arrowprops=arrow_style)
# Under (symmetric)
ax.annotate('', xy=(cx - 3, cy - 2.2), xytext=(cx - 4, cy - 0.5), arrowprops=arrow_style)
ax.annotate('', xy=(cx, cy - 3.5), xytext=(cx - 2.5, cy - 2.8), arrowprops=arrow_style)
ax.annotate('', xy=(cx + 3, cy - 2.2), xytext=(cx + 1, cy - 3.2), arrowprops=arrow_style)
ax.annotate('', xy=(cx + 4, cy - 0.5), xytext=(cx + 3.5, cy - 2), arrowprops=arrow_style)
# Through the hole
ax.annotate('', xy=(cx, cy + 0.3), xytext=(cx, cy + 1.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2, alpha=0.9))
ax.annotate('', xy=(cx, cy - 0.3), xytext=(cx, cy - 1.5),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=2, alpha=0.9))

# Labels
ax.text(cx, 11, 'Galaxy Toroidal Cross-Section', color=GOLD, fontsize=16,
        fontweight='bold', ha='center')
ax.text(cx - 5.5, cy + 0.4, 'Visible disc\n(stars)', color=GOLD, fontsize=9, ha='left')
ax.text(cx + 4, cy + 3.2, '"Dark matter"\nhalo = toroidal\nflow', color=PURPLE,
        fontsize=9, ha='left')
ax.text(cx + 0.3, cy + 1.0, 'Flow through\nhole', color=CYAN, fontsize=8, ha='left')
ax.text(cx, 0.8, 'DM/visible ratio = (22/13)' + r'$\pi$' + ' = 5.317   (Planck: 5.320, miss 725 ppm)',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.9))

save(fig, 'book_02_toroidal_galaxy.png')


# ================================================================
# FIG 3: COUPLING RUNNING — SM vs CD AT TWO-LOOP
# Type: Type 1 (Running/Convergence)
# Shows: Three coupling curves — SM triangle vs CD near-point
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

a_invs = [alpha_1_inv_mz, alpha_2_inv_mz, alpha_3_inv_mz]

# SM panel
ts_sm, curves_sm = run_two_loop(a_invs, [b1_sm, b2_sm, b3_sm], bij_sm, 35.0)
for i in range(3):
    ax1.plot(ts_sm, curves_sm[i], color=gauge_colors[i], linewidth=2.2, label=gauge_labels[i])
ax1.axvline(x=27.31, color=DIM, linestyle='--', linewidth=1, alpha=0.6)
ax1.annotate('SM crossing\nt = 27.3', xy=(27.31, 45.19),
             xytext=(29, 53), color=SILVER, fontsize=9,
             arrowprops=dict(arrowstyle='->', color=DIM, lw=1))
ax1.annotate('Gap = 5.88', xy=(27.31, 39.3), xytext=(19, 34),
             color=RED, fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))
style_ax(ax1, title='Standard Model (no CD)', xlabel='t = ln(E/M_Z)', ylabel=r'$\alpha_i^{-1}$')
ax1.set_xlim(-1, 35)
ax1.set_ylim(0, 70)
ax1.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='lower left')

# CD panel
ts_cd, curves_cd = run_two_loop(a_invs, [b1_cd, b2_cd, b3_cd], bij_total, 38.0)
for i in range(3):
    ax2.plot(ts_cd, curves_cd[i], color=gauge_colors[i], linewidth=2.2, label=gauge_labels[i])
ax2.axvline(x=31.43, color=DIM, linestyle='--', linewidth=1, alpha=0.6)
ax2.annotate('CD crossing\nt = 31.4', xy=(31.43, 42.14),
             xytext=(33, 50), color=GOLD, fontsize=9,
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1))
ax2.annotate('Gap = 0.027', xy=(31.43, 42.14), xytext=(22, 34),
             color=GREEN, fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2))
ax2.text(18, 10, '218' + r'$\times$' + ' better\nthan SM', color=GOLD, fontsize=12,
         fontweight='bold', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9))
style_ax(ax2, title='SM + Cabibbo Doublet', xlabel='t = ln(E/M_Z)', ylabel=r'$\alpha_i^{-1}$')
ax2.set_xlim(-1, 38)
ax2.set_ylim(0, 70)
ax2.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='lower left')

fig.suptitle('Two-Loop Gauge Coupling Running: SM vs CD',
             color=WHITE, fontsize=17, fontweight='bold', y=0.98)
save(fig, 'book_03_coupling_running.png')


# ================================================================
# FIG 4: QED CHAIN — a_e TO f(1S-2S)
# Type: Type 7 (Progression/Sequence)
# Shows: Derivation chain from one measurement to spectroscopy prediction
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

# Five stages left to right
stages = [
    ('Measure\na_e', 'Harvard\nPenning trap', '0.11 ppb', MAG, r'$a_e = 0.00115965218059$'),
    ('Extract\n' + r'$\alpha$', '5-loop QED\n+ 7 corrections', '0.007 ppb', GOLD, r'$\alpha^{-1} = 137.035999207$'),
    ('Derive\n' + r'$R_\infty$', 'SI formula\n' + r'$\alpha^2 m_e c / 2h$', '0.44 ppb', CYAN, r'$R_\infty = 10973731.563$'),
    ('Derive\nconstants', r'$a_0$, $\mu_0$' + '\nfrom SI', '0.22 ppb', GREEN, r'$a_0 = 5.2918 \times 10^{-11}$ m'),
    ('Predict\nf(1S-2S)', 'Hydrogen\nspectroscopy', '0.44 ppb', ORANGE,
     '2466061412094700 Hz'),
]

x_positions = [1.5, 5.0, 8.5, 12.0, 15.5]

ax.text(9, 9.5, 'The QED Chain: One Measurement to Eleven Digits',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

for i, (title, method, precision, col, value) in enumerate(stages):
    x = x_positions[i]
    # Main box
    box = FancyBboxPatch((x - 1.3, 4.0), 2.6, 3.5, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=col, linewidth=2, zorder=3)
    ax.add_patch(box)
    # Title
    ax.text(x, 7.0, title, color=col, fontsize=11, fontweight='bold', ha='center', va='center', zorder=4)
    # Method
    ax.text(x, 5.7, method, color=SILVER, fontsize=8, ha='center', va='center', zorder=4)
    # Precision badge
    ax.text(x, 4.7, precision, color=WHITE, fontsize=10, fontweight='bold', ha='center', va='center', zorder=4,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=col, edgecolor='none', alpha=0.3))
    # Value below box
    ax.text(x, 3.2, value, color=SILVER, fontsize=7, ha='center', va='center')
    # Arrow to next
    if i < len(stages) - 1:
        ax.annotate('', xy=(x_positions[i+1] - 1.3, 5.75),
                    xytext=(x + 1.3, 5.75),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=2.5))

# Experimental groups at bottom
groups = [
    ('Fan et al.\nHarvard 2023', 1.5),
    ('Aoyama, Kinoshita\nRIKEN/Cornell 2019', 5.0),
    ('Morel et al.\nParis 2020', 8.5),
    ('BIPM\nSI 2019', 12.0),
    ('Parthey, H\u00e4nsch\nGarching 2011', 15.5),
]
for name, x in groups:
    ax.text(x, 1.8, name, color=DIM, fontsize=7, ha='center', va='center')

ax.text(9, 1.0, 'Five groups, three continents, one derivation chain',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'book_04_qed_chain.png')


# ================================================================
# FIG 5: COSMOLOGICAL CHAIN — INTEGERS TO DEUTERIUM
# Type: Type 7 (Progression/Sequence)
# Shows: Two integers become four primordial abundances
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

# Six links left to right
links = [
    ('Gauge\nIntegers', '11, 13', 'from SU(2)\nbeta function', BLUE),
    ('Ratio', '22/13', r'$2 \times 11 / 13$', CYAN),
    (r'$\times \pi$', '(22/13)' + r'$\pi$' + '\n= 5.317', 'DM/baryon\nratio', GOLD),
    (r'$\Omega_b$', '0.04904', '727 ppm\nfrom Planck', GREEN),
    (r'$\eta_{10}$', '6.090', 'baryon-to-\nphoton ratio', ORANGE),
    ('BBN', 'D/H, Y_p\nHe-3, Li-7', '3 min after\nBig Bang', RED),
]

x_pos = [1.2, 4.0, 6.8, 9.6, 12.4, 15.5]

ax.text(9, 9.5, 'From Gauge Integers to Primordial Chemistry',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

for i, (title, value, note, col) in enumerate(links):
    x = x_pos[i]
    box = FancyBboxPatch((x - 1.1, 4.5), 2.2, 3.0, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=col, linewidth=1.8, zorder=3)
    ax.add_patch(box)
    ax.text(x, 7.0, title, color=col, fontsize=10, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(x, 5.8, value, color=WHITE, fontsize=10, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(x, 5.0, note, color=SILVER, fontsize=7, ha='center', va='center', zorder=4)
    if i < len(links) - 1:
        ax.annotate('', xy=(x_pos[i+1] - 1.1, 6.0),
                    xytext=(x + 1.1, 6.0),
                    arrowprops=dict(arrowstyle='->', color=GOLD, lw=2))

# BBN results at bottom
results = [
    ('D/H', '2.531e-5', '2.527e-5', '0.12' + r'$\sigma$', GREEN),
    ('Y_p (He-4)', '0.2486', '0.2449', '0.94' + r'$\sigma$', GREEN),
    ('He-3/H', '1.03e-5', '1.10e-5', '0.36' + r'$\sigma$', GREEN),
    ('Li-7/H', '4.74e-10', '1.60e-10', '2.96' + r'$\times$', RED),
]

ax.text(9, 3.5, 'Predicted      Measured      Miss', color=SILVER, fontsize=9, ha='center')
for i, (name, pred, meas, miss, col) in enumerate(results):
    y = 2.8 - i * 0.55
    ax.text(4.5, y, name, color=col, fontsize=9, fontweight='bold', ha='right')
    ax.text(7.0, y, pred, color=WHITE, fontsize=9, ha='center')
    ax.text(10.0, y, meas, color=SILVER, fontsize=9, ha='center')
    ax.text(13.0, y, miss, color=col, fontsize=10, fontweight='bold', ha='center')

ax.text(9, 0.5, 'Two integers from the weak force determine the chemical composition of the universe',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'book_05_cosmo_chain.png')


# ================================================================
# FIG 6: PROTON DECAY — M_GUT vs TAU_P
# Type: Type 3 (Threshold/Region)
# Shows: M_GUT^4 power law with experimental bounds and model positions
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# tau_p ~ M_GUT^4 / (alpha_GUT^2 * m_p^5)
# Calibrate: at M_GUT=10^15.6, tau_p ~ 10^34.5
const_tau = -27.9
mgut_range = np.linspace(13, 17.5, 200)
tau_range = 4.0 * mgut_range + const_tau

ax.plot(mgut_range, tau_range, color=GOLD, linewidth=2.5, label=r'$\tau_p \propto M_{GUT}^4$')

# Super-K bound
ax.axhline(y=34.2, color=RED, linewidth=1.5, linestyle='--', alpha=0.7)
ax.axhspan(28, 34.2, alpha=0.06, color=RED)
ax.text(13.3, 33.0, 'Super-K excluded\n' + r'$\tau_p > 1.6 \times 10^{34}$ yr',
        color=RED, fontsize=10)

# Hyper-K sensitivity
ax.axhspan(34.5, 35.5, alpha=0.10, color=GREEN)
ax.text(13.3, 35.0, 'Hyper-K sensitivity\n(2027-2037)', color=GREEN,
        fontsize=10, fontweight='bold')

# SM point
tau_sm = 4 * 13.82 + const_tau
ax.scatter([13.82], [tau_sm], color=RED, s=250, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='s')
ax.annotate('SM\n(excluded)', xy=(13.82, tau_sm),
            xytext=(14.3, tau_sm + 1.5), color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# CD point
tau_cd = 4 * 15.61 + const_tau
ax.scatter([15.61], [tau_cd], color=GOLD, s=250, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='D')
ax.annotate('CD\n(Hyper-K window)', xy=(15.61, tau_cd),
            xytext=(16.0, tau_cd + 1.5), color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# MSSM point
tau_mssm = 4 * 16.3 + const_tau
ax.scatter([16.3], [tau_mssm], color=PURPLE, s=200, zorder=5, edgecolors=WHITE,
           linewidth=2, marker='^')
ax.annotate('MSSM', xy=(16.3, tau_mssm),
            xytext=(16.7, tau_mssm - 2), color=PURPLE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.2))

style_ax(ax, title=r'Proton Lifetime vs $M_{GUT}$: The Hyper-K Test',
         xlabel=r'log$_{10}$($M_{GUT}$ / GeV)',
         ylabel=r'log$_{10}$($\tau_p$ / yr)')
ax.set_xlim(12.5, 17.5)
ax.set_ylim(28, 44)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='upper left')
save(fig, 'book_06_proton_decay.png')


# ================================================================
# FIG 7: EIGHT-DOMAIN GRAPH
# Type: Type 5 (Connection/Integer Map)
# Shows: Topology of 8 domains with crossings and hydrogen at two positions
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

domains = {
    'Spectroscopy': (9, 13, CYAN, '1 value\n0.44 ppb'),
    'QED':          (9, 11, GOLD, '6 values\n0.007 ppb'),
    'Muon':         (3, 9, MAG, '3 values\n6.5\u03c3'),
    'Electroweak':  (7, 8, GREEN, '15 values\n195 ppm'),
    'GUT':          (13, 9, ORANGE, '10 values\n12 ppm'),
    'Flavor':       (5, 5.5, PURPLE, '4 values\n0.83\u03c3'),
    'Cosmology':    (12, 5.5, BLUE, '6 values\n725 ppm'),
    'Nuclear':      (12, 3, RED, '5 values\n0.12\u03c3'),
}

edges = [
    ('QED', 'Spectroscopy', '0.44 ppb'),
    ('QED', 'Muon', '0.22 ppb'),
    ('QED', 'Electroweak', r'$R_\infty$, $a_0$'),
    ('QED', 'GUT', r'$\alpha \rightarrow$ betas'),
    ('Electroweak', 'Flavor', 'CKM'),
    ('GUT', 'Electroweak', r'sin$^2\theta_W$'),
    ('GUT', 'Cosmology', r'(22/13)$\pi$'),
    ('Cosmology', 'Nuclear', r'$\eta \rightarrow$ BBN'),
]

for d1, d2, label in edges:
    x1, y1 = domains[d1][0], domains[d1][1]
    x2, y2 = domains[d2][0], domains[d2][1]
    ax.plot([x1, x2], [y1, y2], color=DIM, linewidth=1.5, zorder=1, alpha=0.6)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(mx, my + 0.3, label, color=SILVER, fontsize=7, ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor='none', alpha=0.8))

for name, (x, y, col, desc) in domains.items():
    box = FancyBboxPatch((x - 1.4, y - 0.65), 2.8, 1.3, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=2, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + 0.2, name, color=col, fontsize=11, fontweight='bold',
            ha='center', va='center', zorder=4)
    ax.text(x, y - 0.3, desc, color=SILVER, fontsize=8, ha='center', va='center', zorder=4)

# Koide atoll
kx, ky = 3, 3
box_k = FancyBboxPatch((kx - 1.3, ky - 0.6), 2.6, 1.2, boxstyle='round,pad=0.15',
                       facecolor=PAN, edgecolor=DIM, linewidth=1.5, linestyle='--', zorder=3)
ax.add_patch(box_k)
ax.text(kx, ky + 0.15, 'Koide (atoll)', color=DIM, fontsize=10, fontweight='bold',
        ha='center', va='center', zorder=4)
ax.text(kx, ky - 0.3, r'm$_\tau$ 62 ppm' + '\ndisconnected', color=DIM, fontsize=8,
        ha='center', va='center', zorder=4)

# Hydrogen markers
ax.text(10.5, 13.3, 'H (1S-2S)', color=CYAN, fontsize=8, fontstyle='italic')
ax.text(13.5, 3.3, 'H (D/H)', color=RED, fontsize=8, fontstyle='italic')
ax.plot([10.3, 13.5], [13, 3.5], color=WHITE, linewidth=0.8, linestyle=':', alpha=0.3, zorder=1)
ax.text(12.5, 8, 'Hydrogen:\nboth ends', color=WHITE, fontsize=8, ha='center',
        alpha=0.5, fontstyle='italic')

ax.set_title('The Derivation Graph: 8 Domains, 12 Crossings, Surplus +40',
             color=GOLD, fontsize=16, fontweight='bold', pad=15)

ax.text(2, 1, '53 derived values\n13 measured inputs\nSurplus +40',
        color=GOLD, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

save(fig, 'book_07_eight_domains.png')


# ================================================================
# FIG 8: IDENTITY CARD — THE BOOK
# Type: Type 8 (Identity Card)
# Shows: Complete state of the model — visual anchor for the book
# ================================================================

fig, ax = plt.subplots(figsize=(16, 11))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)

# Main border
main_box = FancyBboxPatch((0.5, 0.5), 15, 10, boxstyle='round,pad=0.3',
                          facecolor=PAN, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(main_box)

# Title
ax.text(8, 10, 'The Rational Universe', color=GOLD, fontsize=20, fontweight='bold', ha='center')
ax.text(8, 9.4, 'Unification Through Rectification of Names', color=WHITE,
        fontsize=13, ha='center')

# Left: Three words
ax.text(1.5, 8.3, 'THREE WORDS', color=GOLD, fontsize=12, fontweight='bold')
words = [
    ('INERTIA', 'Resistance to change (m = F/a)', CYAN),
    ('VORTEX', 'The pattern that resists', GREEN),
    ('SOLITON', 'The boundary where readings change', ORANGE),
]
for i, (word, desc, col) in enumerate(words):
    y = 7.5 - i * 0.65
    ax.text(1.5, y, word, color=col, fontsize=11, fontweight='bold')
    ax.text(4.0, y, desc, color=SILVER, fontsize=9)

# Left: Key numbers
ax.text(1.5, 5.3, 'KEY NUMBERS', color=GOLD, fontsize=12, fontweight='bold')
stats = [
    ('Derived values:', '53', GOLD),
    ('Measured inputs:', '13', CYAN),
    ('Surplus:', '+40', GREEN),
    ('Domains:', '8', BLUE),
    ('Best precision:', '0.007 ppb', GOLD),
]
for i, (label, val, col) in enumerate(stats):
    y = 4.7 - i * 0.5
    ax.text(1.5, y, label, color=SILVER, fontsize=9)
    ax.text(4.8, y, val, color=col, fontsize=11, fontweight='bold')

# Right: Key results
ax.text(8.5, 8.3, 'KEY RESULTS', color=GOLD, fontsize=12, fontweight='bold')
results = [
    (r'$\alpha^{-1}$', '137.035999207', '0.007 ppb vs Rb', GOLD),
    (r'sin$^2\theta_W$', '0.231223', '12 ppm (two-loop)', ORANGE),
    (r'$\alpha_s$', '0.11838', '0.33% (two-loop)', RED),
    ('Gap (CD)', '0.027', '218' + r'$\times$' + ' better than SM', GREEN),
    (r'$M_{GUT}$', r'$10^{15.61}$', 'Hyper-K window', PURPLE),
    ('DM ratio', '(22/13)' + r'$\pi$', '725 ppm from Planck', BLUE),
    ('f(1S-2S)', '0.44 ppb', 'spectroscopy bridge', CYAN),
    ('D/H', r'0.12$\sigma$', 'from gauge integers', MAG),
]
for i, (name, val, note, col) in enumerate(results):
    y = 7.5 - i * 0.55
    ax.text(8.5, y, name, color=col, fontsize=9, fontweight='bold')
    ax.text(10.8, y, val, color=WHITE, fontsize=9)
    ax.text(13.0, y, note, color=SILVER, fontsize=7)

# Bottom: The thesis
ax.text(8, 1.8, 'Every physical value is a reading across a soliton boundary,',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')
ax.text(8, 1.2, 'determined by integer transformation laws from the gauge group.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

# CD badge
ax.text(1.5, 2.3, 'CABIBBO DOUBLET', color=GOLD, fontsize=10, fontweight='bold')
ax.text(1.5, 1.8, '(3, 2, 1/6) vector-like', color=WHITE, fontsize=9)
ax.text(1.5, 1.3, r'$\Delta b = (1/15,\; 1,\; 1/3)$', color=CYAN, fontsize=9)

save(fig, 'book_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "=" * 60)
print("BOOK DIAGRAMS COMPLETE")
print("=" * 60)
fnames = [
    'book_01_nested_solitons.png',
    'book_02_toroidal_galaxy.png',
    'book_03_coupling_running.png',
    'book_04_qed_chain.png',
    'book_05_cosmo_chain.png',
    'book_06_proton_decay.png',
    'book_07_eight_domains.png',
    'book_08_identity_card.png',
]
for i, fn in enumerate(fnames):
    print("  Fig %d: %s" % (i + 1, fn))
print("=" * 60)
