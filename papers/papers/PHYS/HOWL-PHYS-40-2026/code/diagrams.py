#!/usr/bin/env python3
"""
HOWL PHYS-40 Diagrams — You Are Here (II): The Derivation Map at 53 Values
8 figures covering coupling unification, scale landscape, proton decay,
domain topology, gap comparison, k1 bug cascade, and identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
import os

# ── Output directory ──
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

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

# ── Physics data from DATA-6 pool ──

# One-loop betas
b1_sm, b2_sm, b3_sm = 41.0/10, -19.0/6, -7.0
b1_cd, b2_cd, b3_cd = 25.0/6, -13.0/6, -20.0/3

# Couplings at M_Z
alpha_em_inv = 137.035999177
sin2_tw = 0.23122
alpha_s = 0.1180
k1 = 3.0/5

alpha_1_inv_mz = k1 * (1.0 - sin2_tw) * alpha_em_inv   # 63.210
alpha_2_inv_mz = sin2_tw * alpha_em_inv                  # 31.685
alpha_3_inv_mz = 1.0 / alpha_s                           # 8.475

# Two-loop crossing results (from pool)
t_cross_cd = 31.4299
t_cross_sm = 27.3132
alpha_gut_cd = 42.1350
alpha_gut_sm = 45.1862
gap_cd = 0.0269
gap_sm = 5.884
m_gut_cd_log10 = 15.61
m_gut_sm_log10 = 13.82

# Two-loop b_ij matrices (SM)
bij_sm = np.array([
    [199.0/50, 27.0/10, 44.0/5],
    [9.0/10, 35.0/6, 12.0],
    [11.0/10, 9.0/2, -26.0]
])
# CD shifts
dbij_cd = np.array([
    [7.0/15, 1.0/15, 16.0/135],
    [1.0/30, 15.0/4, 8.0/3],
    [1.0/45, 1.0, 40.0/9]
])
bij_total = bij_sm + dbij_cd

def run_one_loop(alpha_invs, betas, t_max, n_pts=500):
    """One-loop RGE: d(alpha_i^-1)/dt = -b_i/(2pi)"""
    ts = np.linspace(0, t_max, n_pts)
    two_pi = 2.0 * np.pi
    curves = []
    for a_inv, b in zip(alpha_invs, betas):
        curves.append(a_inv - b / two_pi * ts)
    return ts, curves

def run_two_loop(alpha_invs, betas, bij, t_max, n_pts=2000):
    """Two-loop RGE via Euler integration"""
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
# FIG 1: COUPLING RUNNING — SM vs CD AT TWO-LOOP
# Type: Type 1 (Running/Convergence)
# Shows: Three coupling curves converging — SM triangle vs CD near-point
# ================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

a_invs = [alpha_1_inv_mz, alpha_2_inv_mz, alpha_3_inv_mz]
gauge_colors = [BLUE, GREEN, RED]
gauge_labels = [r'$\alpha_1^{-1}$ (U(1))', r'$\alpha_2^{-1}$ (SU(2))', r'$\alpha_3^{-1}$ (SU(3))']

# SM panel
ts_sm, curves_sm = run_two_loop(a_invs, [b1_sm, b2_sm, b3_sm], bij_sm, 35.0)
for i in range(3):
    ax1.plot(ts_sm, curves_sm[i], color=gauge_colors[i], linewidth=2.2, label=gauge_labels[i])
ax1.axvline(x=t_cross_sm, color=DIM, linestyle='--', linewidth=1, alpha=0.6)
ax1.annotate('SM crossing\nt = %.1f' % t_cross_sm, xy=(t_cross_sm, alpha_gut_sm),
             xytext=(t_cross_sm + 2, alpha_gut_sm + 8),
             color=SILVER, fontsize=9,
             arrowprops=dict(arrowstyle='->', color=DIM, lw=1))
# Mark the gap
ax1.annotate('Gap = %.2f' % gap_sm, xy=(t_cross_sm, 39.3), xytext=(t_cross_sm - 8, 35),
             color=RED, fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))
style_ax(ax1, title='SM (no CD)', xlabel='t = ln(E/M_Z)', ylabel=r'$\alpha_i^{-1}$')
ax1.set_xlim(-1, 35)
ax1.set_ylim(0, 70)
ax1.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='lower left')

# CD panel
ts_cd, curves_cd = run_two_loop(a_invs, [b1_cd, b2_cd, b3_cd], bij_total, 38.0)
for i in range(3):
    ax2.plot(ts_cd, curves_cd[i], color=gauge_colors[i], linewidth=2.2, label=gauge_labels[i])
ax2.axvline(x=t_cross_cd, color=DIM, linestyle='--', linewidth=1, alpha=0.6)
ax2.annotate('CD crossing\nt = %.1f' % t_cross_cd, xy=(t_cross_cd, alpha_gut_cd),
             xytext=(t_cross_cd + 2, alpha_gut_cd + 8),
             color=GOLD, fontsize=9,
             arrowprops=dict(arrowstyle='->', color=GOLD, lw=1))
ax2.annotate('Gap = %.3f' % gap_cd, xy=(t_cross_cd, alpha_gut_cd), xytext=(t_cross_cd - 10, 35),
             color=GREEN, fontsize=10, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2))
# 218x label
ax2.text(18, 10, '218x better\nthan SM', color=GOLD, fontsize=12, fontweight='bold',
         ha='center', bbox=dict(boxstyle='round,pad=0.5', facecolor=BG, edgecolor=GOLD, alpha=0.9))
style_ax(ax2, title='SM + Cabibbo Doublet', xlabel='t = ln(E/M_Z)', ylabel=r'$\alpha_i^{-1}$')
ax2.set_xlim(-1, 38)
ax2.set_ylim(0, 70)
ax2.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='lower left')

fig.suptitle('Two-Loop Gauge Coupling Running: SM vs CD', color=WHITE, fontsize=17, fontweight='bold', y=0.98)
save(fig, 'phys40_01_coupling_running.png')


# ================================================================
# FIG 2: SIN2_THETA_W BACKWARD RUN FROM M_GUT
# Type: Type 1 (Running/Convergence)
# Shows: Three couplings diverging from alpha_GUT, predicted sin2_tW at M_Z
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# Run backward: start at crossing, run to M_Z
# Use the CD two-loop crossing: all three start at alpha_gut_cd = 42.135
a_start = [alpha_gut_cd, alpha_gut_cd, alpha_gut_cd]
ts_back, curves_back = run_two_loop(a_start, [b1_cd, b2_cd, b3_cd], bij_total, t_cross_cd, n_pts=2000)
# Reverse so x-axis goes from M_GUT (left) to M_Z (right)
# Actually plot as t going from t_cross down to 0
t_phys = t_cross_cd - ts_back  # t_cross at left, 0 at right

for i in range(3):
    ax.plot(t_phys, curves_back[i], color=gauge_colors[i], linewidth=2.5, label=gauge_labels[i])

# Mark the starting point
ax.scatter([t_cross_cd]*3, [alpha_gut_cd]*3, color=GOLD, s=200, zorder=5, edgecolors=WHITE, linewidth=2)
ax.annotate(r'$\alpha_{GUT}^{-1}$ = %.2f' % alpha_gut_cd, xy=(t_cross_cd, alpha_gut_cd),
            xytext=(t_cross_cd - 5, alpha_gut_cd + 5),
            color=GOLD, fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark predicted values at M_Z (t=0)
# alpha_2_inv predicted = sin2_predicted * alpha_em_inv
sin2_predicted = 0.231223
alpha_s_predicted = 0.11838
a1_pred = k1 * (1 - sin2_predicted) * alpha_em_inv
a2_pred = sin2_predicted * alpha_em_inv
a3_pred = 1.0 / alpha_s_predicted

pred_vals = [a1_pred, a2_pred, a3_pred]
pred_labels = [r'$\alpha_1^{-1}$ = %.2f' % a1_pred,
               r'sin$^2\theta_W$ = %.6f' % sin2_predicted + '\n(12 ppm miss)',
               r'$\alpha_s$ = %.5f' % alpha_s_predicted + '\n(0.33% miss)']

for i, (val, lbl) in enumerate(zip(pred_vals, pred_labels)):
    yoff = [-3, 5, 3][i]
    ax.scatter([0], [val], color=gauge_colors[i], s=180, zorder=5, edgecolors=WHITE, linewidth=2, marker='D')
    ax.annotate(lbl, xy=(0, val), xytext=(3, val + yoff),
                color=gauge_colors[i], fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=gauge_colors[i], lw=1))

# Measurement bands at M_Z
ax.axhspan(alpha_2_inv_mz - 0.05, alpha_2_inv_mz + 0.05, alpha=0.12, color=MAG, zorder=1)
ax.axhspan(alpha_3_inv_mz - 0.1, alpha_3_inv_mz + 0.1, alpha=0.12, color=MAG, zorder=1)

# M_GUT and M_Z labels
ax.text(t_cross_cd, -2, r'$M_{GUT} = 10^{15.6}$ GeV', color=SILVER, fontsize=10, ha='center')
ax.text(0, -2, r'$M_Z$ = 91.2 GeV', color=SILVER, fontsize=10, ha='center')

style_ax(ax, title=r'Backward Run from $M_{GUT}$: Predicting sin$^2\theta_W$ and $\alpha_s$',
         xlabel='t = ln(E/M_Z)', ylabel=r'$\alpha_i^{-1}$')
ax.set_xlim(-3, t_cross_cd + 2)
ax.set_ylim(-4, 70)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='upper right')
save(fig, 'phys40_02_backward_extraction.png')


# ================================================================
# FIG 3: ENERGY SCALE LANDSCAPE
# Type: Type 2 (Scale/Landscape)
# Shows: Log hierarchy from m_e to M_Planck with landmarks
# ================================================================

fig, ax = plt.subplots(figsize=(16, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(PAN)

# Energy landmarks (log10 GeV)
landmarks = [
    (-3.7, r'$m_e$', '0.511 MeV', CYAN),
    (-0.7, r'$\Lambda_{QCD}$', '~200 MeV', RED),
    (0.0, r'$m_p$', '938 MeV', SILVER),
    (1.95, r'$M_Z$', '91.2 GeV', GREEN),
    (1.91, r'$M_W$', '80.4 GeV', GREEN),
    (2.24, r'$m_t$', '173 GeV', CYAN),
    (2.10, r'$m_H$', '125 GeV', CYAN),
    (3.48, r'$M_{CD}$', '1.5-6 TeV', ORANGE),
    (13.82, r'$M_{GUT}^{SM}$', r'$10^{13.8}$ GeV', RED),
    (15.61, r'$M_{GUT}^{CD}$', r'$10^{15.6}$ GeV', GOLD),
    (19.09, r'$M_{Planck}$', r'$10^{19}$ GeV', PURPLE),
]

# Draw vertical scale
ax.set_xlim(0, 10)
ax.set_ylim(-5, 21)

# Central spine
ax.plot([5, 5], [-4.5, 20.5], color=DIM, linewidth=2, zorder=1)

for log_e, name, desc, col in landmarks:
    # Horizontal tick
    ax.plot([4.3, 5.7], [log_e, log_e], color=col, linewidth=1.8, zorder=2)
    # Dot
    ax.scatter([5], [log_e], color=col, s=120, zorder=3, edgecolors=WHITE, linewidth=1.5)
    # Left label (name)
    ax.text(3.8, log_e, name, color=col, fontsize=12, ha='right', va='center', fontweight='bold')
    # Right label (value)
    ax.text(6.2, log_e, desc, color=SILVER, fontsize=10, ha='left', va='center')

# Shaded regions
# Super-K excluded (below 10^15.4)
ax.axhspan(-5, 15.4, xmin=0.35, xmax=0.65, alpha=0.06, color=RED)
ax.text(8.0, 10, 'Super-K\nexcluded', color=RED, fontsize=9, ha='center', alpha=0.7)

# Hyper-K window
ax.axhspan(15.0, 16.0, xmin=0.35, xmax=0.65, alpha=0.10, color=GREEN)
ax.text(8.0, 15.5, 'Hyper-K\nwindow', color=GREEN, fontsize=10, ha='center', fontweight='bold')

# CD mass range
ax.axhspan(3.18, 3.78, xmin=0.35, xmax=0.65, alpha=0.10, color=ORANGE)

# Arrow showing SM M_GUT is excluded
ax.annotate('', xy=(7.0, 13.82), xytext=(7.0, 15.3),
            arrowprops=dict(arrowstyle='->', color=RED, lw=2))
ax.text(7.5, 14.5, 'SM excluded\nby Super-K', color=RED, fontsize=9, ha='left')

# Arrow showing CD M_GUT in window
ax.annotate('', xy=(7.0, 15.61), xytext=(7.0, 16.5),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
ax.text(7.5, 16.5, 'CD testable\nat Hyper-K', color=GREEN, fontsize=9, ha='left')

ax.set_ylabel(r'log$_{10}$(E / GeV)', color=SILVER, fontsize=12)
ax.set_title('Energy Scale Landscape: From Electron Mass to Planck Scale',
             color=GOLD, fontsize=15, fontweight='bold', pad=15)
ax.set_xticks([])
for spine in ['top', 'bottom', 'left', 'right']:
    ax.spines[spine].set_color(DIM)
    ax.spines[spine].set_linewidth(0.5)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(axis='y', colors=DIM, labelsize=9)

save(fig, 'phys40_03_energy_landscape.png')


# ================================================================
# FIG 4: PROTON DECAY — M_GUT vs TAU_P
# Type: Type 3 (Threshold/Region)
# Shows: M_GUT^4 power law with Super-K bound and Hyper-K sensitivity
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)

# tau_p proportional to M_GUT^4 / (alpha_GUT^2 * m_p^5 * |alpha_H|^2)
# We plot the scaling: log10(tau_p) = 4*log10(M_GUT) + const
# Calibrate: at M_GUT = 10^15.6, typical tau_p ~ 10^34.5 for minimal SU(5)
# const = 34.5 - 4*15.6 = 34.5 - 62.4 = -27.9

const_tau = -27.9
mgut_range = np.linspace(13, 17.5, 200)
tau_range = 4.0 * mgut_range + const_tau

ax.plot(mgut_range, tau_range, color=GOLD, linewidth=2.5, label=r'$\tau_p \propto M_{GUT}^4$')

# Super-K bound: tau_p > 1.6 x 10^34 => log10 > 34.2
ax.axhline(y=34.2, color=RED, linewidth=1.5, linestyle='--', alpha=0.7)
ax.axhspan(28, 34.2, alpha=0.06, color=RED)
ax.text(13.3, 33.5, 'Super-K excluded', color=RED, fontsize=10)

# Hyper-K sensitivity: ~10^34.5 to 10^35.5
ax.axhspan(34.5, 35.5, alpha=0.10, color=GREEN)
ax.text(13.3, 35.0, 'Hyper-K sensitivity (2027-2037)', color=GREEN, fontsize=10, fontweight='bold')

# Mark SM M_GUT
tau_sm = 4 * m_gut_sm_log10 + const_tau
ax.scatter([m_gut_sm_log10], [tau_sm], color=RED, s=250, zorder=5, edgecolors=WHITE, linewidth=2, marker='s')
ax.annotate('SM\n(excluded)', xy=(m_gut_sm_log10, tau_sm),
            xytext=(m_gut_sm_log10 + 0.5, tau_sm + 1.5),
            color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))

# Mark CD M_GUT
tau_cd = 4 * m_gut_cd_log10 + const_tau
ax.scatter([m_gut_cd_log10], [tau_cd], color=GOLD, s=250, zorder=5, edgecolors=WHITE, linewidth=2, marker='D')
ax.annotate('CD\n(Hyper-K window)', xy=(m_gut_cd_log10, tau_cd),
            xytext=(m_gut_cd_log10 + 0.5, tau_cd + 1.5),
            color=GOLD, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.5))

# Mark MSSM M_GUT (~10^16.3)
mgut_mssm = 16.3
tau_mssm = 4 * mgut_mssm + const_tau
ax.scatter([mgut_mssm], [tau_mssm], color=PURPLE, s=200, zorder=5, edgecolors=WHITE, linewidth=2, marker='^')
ax.annotate('MSSM', xy=(mgut_mssm, tau_mssm),
            xytext=(mgut_mssm + 0.3, tau_mssm - 2),
            color=PURPLE, fontsize=10,
            arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.2))

style_ax(ax, title=r'Proton Lifetime vs $M_{GUT}$: The Hyper-K Test',
         xlabel=r'log$_{10}$($M_{GUT}$ / GeV)', ylabel=r'log$_{10}$($\tau_p$ / yr)')
ax.set_xlim(12.5, 17.5)
ax.set_ylim(28, 44)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=10, loc='upper left')
save(fig, 'phys40_04_proton_decay.png')


# ================================================================
# FIG 5: EIGHT-DOMAIN GRAPH
# Type: Type 5 (Connection/Integer Map)
# Shows: Topology of 8 domains, 12 crossings, hydrogen at 2 positions
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

# Domain positions (x, y)
domains = {
    'Spectroscopy': (9, 13, CYAN, '1 value\n0.44 ppb'),
    'QED':          (9, 11, GOLD, '6 values\n0.007 ppb'),
    'Muon':         (3, 9, MAG, '3 values\n6.5\u03c3'),
    'EW':           (7, 8, GREEN, '15 values\n195 ppm'),
    'GUT':          (13, 9, ORANGE, '10 values\n12 ppm'),
    'Flavor':       (5, 5.5, PURPLE, '4 values\n0.83\u03c3'),
    'Cosmology':    (12, 5.5, BLUE, '6 values\n725 ppm'),
    'Nuclear':      (12, 3, RED, '5 values\n0.12\u03c3'),
}

# Draw edges first (connections)
edges = [
    ('QED', 'Spectroscopy', '0.44 ppb'),
    ('QED', 'Muon', '0.22 ppb'),
    ('QED', 'EW', 'R\u221e, a\u2080'),
    ('QED', 'GUT', '\u03b1\u2192betas'),
    ('EW', 'Flavor', 'CKM'),
    ('GUT', 'EW', 'sin\u00b2\u03b8'),
    ('GUT', 'Cosmology', '(22/13)\u03c0'),
    ('Cosmology', 'Nuclear', '\u03b7\u2192BBN'),
]

for d1, d2, label in edges:
    x1, y1 = domains[d1][0], domains[d1][1]
    x2, y2 = domains[d2][0], domains[d2][1]
    ax.plot([x1, x2], [y1, y2], color=DIM, linewidth=1.5, zorder=1, alpha=0.6)
    mx, my = (x1+x2)/2, (y1+y2)/2
    ax.text(mx, my + 0.25, label, color=SILVER, fontsize=7, ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=BG, edgecolor='none', alpha=0.8))

# Draw domain nodes
for name, (x, y, col, desc) in domains.items():
    box = FancyBboxPatch((x-1.3, y-0.6), 2.6, 1.2, boxstyle='round,pad=0.15',
                         facecolor=PAN, edgecolor=col, linewidth=2, zorder=3)
    ax.add_patch(box)
    ax.text(x, y + 0.15, name, color=col, fontsize=11, fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(x, y - 0.3, desc, color=SILVER, fontsize=8, ha='center', va='center', zorder=4)

# Koide atoll (disconnected)
kx, ky = 3, 3
box_k = FancyBboxPatch((kx-1.2, ky-0.6), 2.4, 1.2, boxstyle='round,pad=0.15',
                       facecolor=PAN, edgecolor=DIM, linewidth=1.5, linestyle='--', zorder=3)
ax.add_patch(box_k)
ax.text(kx, ky + 0.15, 'Koide (atoll)', color=DIM, fontsize=10, fontweight='bold', ha='center', va='center', zorder=4)
ax.text(kx, ky - 0.3, 'm\u03c4 62 ppm\ndisconnected', color=DIM, fontsize=8, ha='center', va='center', zorder=4)

# Hydrogen markers
ax.text(10.5, 13.3, 'H (1S-2S)', color=CYAN, fontsize=8, fontstyle='italic')
ax.text(13.5, 3.3, 'H (D/H)', color=RED, fontsize=8, fontstyle='italic')
# Dashed line showing hydrogen connects both ends
ax.plot([10.3, 13.5], [13, 3.5], color=WHITE, linewidth=0.8, linestyle=':', alpha=0.3, zorder=1)
ax.text(12.5, 8, 'Hydrogen:\nboth ends', color=WHITE, fontsize=8, ha='center', alpha=0.5, fontstyle='italic')

ax.set_title('The Derivation Graph: 8 Domains, 12 Crossings, Surplus +40',
             color=GOLD, fontsize=16, fontweight='bold', pad=15)
# Summary box
ax.text(2, 1, '53 derived values\n13 measured inputs\nSurplus +40',
        color=GOLD, fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.6', facecolor=BG, edgecolor=GOLD, linewidth=1.5))

save(fig, 'phys40_05_eight_domain_graph.png')


# ================================================================
# FIG 6: GAP IMPROVEMENT — SM vs CD vs MSSM
# Type: Type 6 (Comparison Bar)
# Shows: Log-scale bars — CD 218x better than SM, 19x better than MSSM
# ================================================================

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor(BG)

models = ['SM', 'MSSM', 'CD']
gaps = [5.884, 0.5, 0.0269]
colors_bar = [RED, PURPLE, GOLD]

bars = ax.barh(models, gaps, color=colors_bar, alpha=0.75, edgecolor=[RED, PURPLE, GOLD], linewidth=2, height=0.5)

ax.set_xscale('log')
ax.set_xlim(0.005, 20)

# Labels on bars
for i, (model, gap) in enumerate(zip(models, gaps)):
    if gap > 1:
        ax.text(gap * 0.5, i, '%.2f' % gap, color=WHITE, fontsize=14, fontweight='bold', ha='center', va='center')
    else:
        ax.text(gap * 3, i, '%.4f' % gap, color=colors_bar[i], fontsize=13, fontweight='bold', ha='left', va='center')

# Improvement factors
ax.annotate('218\u00d7', xy=(0.0269, 2), xytext=(0.0269, 2.6),
            color=GOLD, fontsize=16, fontweight='bold', ha='center')
ax.annotate('', xy=(5.884, 2.4), xytext=(0.0269, 2.4),
            arrowprops=dict(arrowstyle='<->', color=GOLD, lw=2))

ax.annotate('19\u00d7', xy=(0.0269, 1), xytext=(0.15, 1.5),
            color=GOLD, fontsize=12, ha='center')

# Exact unification line
ax.axvline(x=0.01, color=GREEN, linewidth=1, linestyle=':', alpha=0.5)
ax.text(0.008, 2.8, 'Exact\nunification', color=GREEN, fontsize=8, ha='center', alpha=0.7)

style_ax(ax, title=r'Unification Gap ($\alpha_2^{-1} - \alpha_3^{-1}$ at crossing)',
         xlabel='Gap at two-loop crossing')
ax.set_ylim(-0.6, 3.2)
save(fig, 'phys40_06_gap_comparison.png')


# ================================================================
# FIG 7: K1 BUG CASCADE
# Type: Type 7 (Progression/Sequence)
# Shows: One inverted factor cascading through computation
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)

# Two rows: wrong (top) and right (bottom)
# Stage columns
stages = [
    (r'$k_1$', 'factor'),
    (r'$\alpha_1^{-1}(M_Z)$', 'coupling'),
    (r'$M_{GUT}$', 'scale'),
    (r'$\alpha_s$', 'prediction'),
]

wrong_vals = ['5/3', '175.6', r'$10^{56}$', 'negative']
right_vals = ['3/5', '63.2', r'$10^{13.8}$', '0.066']

x_positions = [2.5, 6.5, 10.5, 14.5]

# Title
ax.text(9, 9.5, r'The $k_1$ Bug: One Inverted Factor $\rightarrow$ 42 Orders of Magnitude',
        color=GOLD, fontsize=15, fontweight='bold', ha='center')

# Wrong row
ax.text(0.5, 7.5, 'WRONG', color=RED, fontsize=13, fontweight='bold', va='center')
for i, (x, (stage, _), val) in enumerate(zip(x_positions, stages, wrong_vals)):
    box = FancyBboxPatch((x-1.4, 6.8), 2.8, 1.5, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=RED, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 7.8, stage, color=RED, fontsize=11, ha='center', va='center')
    ax.text(x, 7.2, val, color=WHITE, fontsize=13, fontweight='bold', ha='center', va='center')
    if i < len(stages) - 1:
        ax.annotate('', xy=(x_positions[i+1]-1.4, 7.55), xytext=(x+1.4, 7.55),
                    arrowprops=dict(arrowstyle='->', color=RED, lw=2))

# Right row
ax.text(0.5, 4.5, 'RIGHT', color=GREEN, fontsize=13, fontweight='bold', va='center')
for i, (x, (stage, _), val) in enumerate(zip(x_positions, stages, right_vals)):
    box = FancyBboxPatch((x-1.4, 3.8), 2.8, 1.5, boxstyle='round,pad=0.2',
                         facecolor=PAN, edgecolor=GREEN, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 4.8, stage, color=GREEN, fontsize=11, ha='center', va='center')
    ax.text(x, 4.2, val, color=WHITE, fontsize=13, fontweight='bold', ha='center', va='center')
    if i < len(stages) - 1:
        ax.annotate('', xy=(x_positions[i+1]-1.4, 4.55), xytext=(x+1.4, 4.55),
                    arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

# Ratio labels between rows
ratios = [r'$(5/3)^2$' + '\n= 2.78\u00d7', '2.78\u00d7', r'$10^{42}$', r'$-\infty$']
for x, ratio in zip(x_positions, ratios):
    ax.text(x, 6.1, ratio, color=ORANGE, fontsize=9, ha='center', va='center', fontweight='bold')
    ax.annotate('', xy=(x, 6.7), xytext=(x, 5.4),
                arrowprops=dict(arrowstyle='<->', color=ORANGE, lw=1, alpha=0.6))

# Discovery note
ax.text(9, 1.5, 'Found by DATA-6 diagnostic iteration:\nRun 001 (both wrong) \u2192 Run 002 (CD fixed) \u2192 Run 003 (ALL PASS)',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=PAN, edgecolor=DIM))

save(fig, 'phys40_07_k1_bug_cascade.png')


# ================================================================
# FIG 8: IDENTITY CARD — PHYS-40
# Type: Type 8 (Identity Card)
# Shows: Complete state: 53 values, 13 inputs, 8 domains, surplus +40
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
ax.text(8, 10, 'HOWL PHYS-40: You Are Here (II)', color=GOLD, fontsize=18, fontweight='bold', ha='center')
ax.text(8, 9.4, 'The Derivation Map at 53 Values', color=WHITE, fontsize=14, ha='center')

# Left column: Key numbers
ax.text(1.5, 8.3, 'INVENTORY', color=GOLD, fontsize=12, fontweight='bold')
stats = [
    ('Derived values:', '53', GOLD),
    ('Measured inputs:', '13', CYAN),
    ('Surplus:', '+40', GREEN),
    ('Domains:', '8', BLUE),
    ('Crossings:', '12', SILVER),
    ('Experiments:', '~38', SILVER),
    ('Pool nodes:', '2237', DIM),
]
for i, (label, val, col) in enumerate(stats):
    y = 7.5 - i * 0.55
    ax.text(1.5, y, label, color=SILVER, fontsize=10)
    ax.text(5.0, y, val, color=col, fontsize=12, fontweight='bold')

# Right column: Key results
ax.text(8.5, 8.3, 'KEY RESULTS', color=GOLD, fontsize=12, fontweight='bold')
results = [
    (r'$\alpha^{-1}$', '137.035999207', '0.007 ppb vs Rb', GOLD),
    (r'sin$^2\theta_W$', '0.231223', '12 ppm (two-loop)', ORANGE),
    (r'$\alpha_s$', '0.11838', '0.33% (two-loop)', RED),
    ('Gap (CD)', '0.027', '218\u00d7 better than SM', GREEN),
    (r'$M_{GUT}$', r'$10^{15.61}$', 'Hyper-K window', PURPLE),
    ('f(1S-2S)', '0.44 ppb', 'spectroscopy bridge', CYAN),
    ('D/H', r'0.12$\sigma$', 'from gauge integers', BLUE),
]
for i, (name, val, note, col) in enumerate(results):
    y = 7.5 - i * 0.55
    ax.text(8.5, y, name, color=col, fontsize=10, fontweight='bold')
    ax.text(10.8, y, val, color=WHITE, fontsize=10)
    ax.text(13.0, y, note, color=SILVER, fontsize=8)

# CD quantum numbers
ax.text(1.5, 3.5, 'CABIBBO DOUBLET', color=GOLD, fontsize=11, fontweight='bold')
ax.text(1.5, 3.0, '(SU(3), SU(2), U(1)) = (3, 2, 1/6)', color=WHITE, fontsize=10)
ax.text(1.5, 2.5, 'Vector-like quarks at 1.5-6 TeV', color=SILVER, fontsize=9)
ax.text(1.5, 2.0, r'$\Delta b_1 = 1/15$,  $\Delta b_2 = 1$,  $\Delta b_3 = 1/3$', color=CYAN, fontsize=10)

# Falsification
ax.text(8.5, 3.5, 'FALSIFICATION', color=GOLD, fontsize=11, fontweight='bold')
ax.text(8.5, 3.0, '10 criteria: 9 PASS, 1 superseded', color=GREEN, fontsize=10)
ax.text(8.5, 2.5, r'Kill test: sin$^2\theta_W$ shift > 0.1%', color=RED, fontsize=9)
ax.text(8.5, 2.0, r'Kill test: $\tau_p > 10^{36}$ yr (Hyper-K)', color=RED, fontsize=9)

# Bottom: thesis
ax.text(8, 1.0, 'Every physical value is a reading across a soliton boundary,\n'
        'determined by integer transformation laws from the gauge group.',
        color=SILVER, fontsize=10, ha='center', fontstyle='italic')

save(fig, 'phys40_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("\n" + "="*60)
print("PHYS-40 DIAGRAMS COMPLETE")
print("="*60)
fnames = [
    'phys40_01_coupling_running.png',
    'phys40_02_backward_extraction.png',
    'phys40_03_energy_landscape.png',
    'phys40_04_proton_decay.png',
    'phys40_05_eight_domain_graph.png',
    'phys40_06_gap_comparison.png',
    'phys40_07_k1_bug_cascade.png',
    'phys40_08_identity_card.png',
]
for i, fn in enumerate(fnames):
    print("  Fig %d: %s" % (i+1, fn))
print("="*60)
