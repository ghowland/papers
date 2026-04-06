#!/usr/bin/env python3
"""
HOWL PHYS-39 Diagrams — Near-Exact Two-Loop Unification and the Spectroscopy Bridge
8 figures covering two-loop unification, sin2_theta_W extraction, hydrogen two-path,
M_GUT scale, 1S-2S error budget, eight-domain graph, precision landscape, identity card.
Output: PNG files to ../figures/
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
import os

# ── Output directory ───────────────────────────────────────────────
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(outdir, exist_ok=True)

# ── Global style ───────────────────────────────────────────────────
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
    for spine in ax.spines.values():
        spine.set_color(DIM)
        spine.set_linewidth(0.5)
    ax.tick_params(colors=DIM, labelsize=9)
    if xlabel:
        ax.set_xlabel(xlabel, color=SILVER, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=SILVER, fontsize=11)
    if title:
        ax.set_title(title, color=GOLD, fontsize=14, fontweight='bold', pad=12)


# ================================================================
# FIG 1: SM VS CD TWO-LOOP RUNNING (SIDE-BY-SIDE)
# Type: Running/Convergence (Type 1)
# Shows: The SHAPE of convergence vs non-convergence — SM triangle
#        vs CD near-point. The visual difference is immediate.
# ================================================================

def compute_running(log10_e_values, alpha_inv_mz, b_one, b_two, mz_gev=91.1876):
    results = {0: [], 1: [], 2: []}
    two_pi = 2.0 * np.pi
    eight_pi2 = 8.0 * np.pi**2
    for log10_e in log10_e_values:
        e_gev = 10.0**log10_e
        t = np.log(e_gev / mz_gev)
        n_steps = max(500, int(abs(t) * 50))
        dt = t / n_steps if n_steps > 0 else 0.0
        a_inv = list(alpha_inv_mz)
        for step in range(n_steps):
            a = [1.0 / a_inv[i] if a_inv[i] > 0 else 0.0 for i in range(3)]
            da = [0.0] * 3
            for i in range(3):
                da[i] = -b_one[i] / two_pi
                for j in range(3):
                    da[i] -= b_two[i][j] * a[j] / eight_pi2
            for i in range(3):
                a_inv[i] += da[i] * dt
        for i in range(3):
            results[i].append(a_inv[i])
    return results

alpha_1_inv_mz = 0.6 * 0.76878 * 137.036
alpha_2_inv_mz = 0.23122 * 137.036
alpha_3_inv_mz = 1.0 / 0.1180

b_sm = [41.0/10.0, -19.0/6.0, -7.0]
bij_sm = [
    [199.0/50.0, 27.0/10.0, 44.0/5.0],
    [9.0/10.0, 35.0/6.0, 12.0],
    [11.0/10.0, 9.0/2.0, -26.0]
]

b_cd = [25.0/6.0, -13.0/6.0, -20.0/3.0]
bij_cd = [
    [199.0/50.0 + 7.0/15.0,  27.0/10.0 + 1.0/15.0,  44.0/5.0 + 16.0/135.0],
    [9.0/10.0 + 1.0/30.0,    35.0/6.0 + 15.0/4.0,    12.0 + 8.0/3.0],
    [11.0/10.0 + 1.0/45.0,   9.0/2.0 + 1.0,           -26.0 + 40.0/9.0]
]

log10_e = np.linspace(np.log10(91.1876), 16.5, 200)

sm_run = compute_running(log10_e, [alpha_1_inv_mz, alpha_2_inv_mz, alpha_3_inv_mz],
                         b_sm, bij_sm)
cd_run = compute_running(log10_e, [alpha_1_inv_mz, alpha_2_inv_mz, alpha_3_inv_mz],
                         b_cd, bij_cd)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), gridspec_kw={'wspace': 0.30})
fig.patch.set_facecolor(BG)

labels_c = [r'$\alpha_1^{-1}$ (U(1))', r'$\alpha_2^{-1}$ (SU(2))', r'$\alpha_3^{-1}$ (SU(3))']
colors_c = [BLUE, GREEN, RED]

for ax, run_data, ttl, gap_val, mgut_val in [
    (ax1, sm_run, 'Standard Model (no CD)', 5.88, 13.82),
    (ax2, cd_run, 'SM + Cabibbo Doublet', 0.027, 15.61)
]:
    style_ax(ax, xlabel=r'$\log_{10}(E\,/\,\mathrm{GeV})$',
             ylabel=r'$\alpha_i^{-1}$', title=ttl)
    for i in range(3):
        ax.plot(log10_e, run_data[i], color=colors_c[i], linewidth=2.2,
                label=labels_c[i])
    ax.set_ylim(0, 70)
    ax.set_xlim(np.log10(91.1876) - 0.3, 16.5)
    ax.axvline(x=mgut_val, color=GOLD, linestyle='--', alpha=0.5, linewidth=1.2)
    ax.text(mgut_val + 0.15, 65, r'$M_\mathrm{GUT}$' + '\n' + r'$10^{%.1f}$' % mgut_val,
            color=GOLD, fontsize=9, va='top')
    ax.text(mgut_val - 0.15, 5, 'gap = %.3f' % gap_val, color=ORANGE, fontsize=10,
            fontweight='bold', ha='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=ORANGE, alpha=0.8))
    ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='upper right')

fig.text(0.5, 0.02, 'CD gap (0.027) is 218x smaller than SM gap (5.88)',
         color=SILVER, fontsize=11, ha='center')

save(fig, 'phys39_01_two_loop_comparison.png')


# ================================================================
# FIG 2: SIN2_THETA_W BACKWARD EXTRACTION
# Type: Running/Convergence (Type 1)
# Shows: Three couplings starting unified at M_GUT, diverging
#        downward, landing on predicted values at M_Z.
# ================================================================

alpha_gut_inv = 42.135

log10_e_back = np.linspace(15.61, np.log10(91.1876), 200)

back_run = compute_running(log10_e_back,
                           [alpha_gut_inv, alpha_gut_inv, alpha_gut_inv],
                           b_cd, bij_cd, mz_gev=10.0**15.61)

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel=r'$\log_{10}(E\,/\,\mathrm{GeV})$',
         ylabel=r'$\alpha_i^{-1}$',
         title=r'Backward Run: Predict Couplings at $M_Z$ from Unification')

for i in range(3):
    ax.plot(log10_e_back, back_run[i], color=colors_c[i],
            linewidth=2.5, label=labels_c[i])

ax.scatter([15.61]*3, [alpha_gut_inv]*3, color=GOLD, s=200,
           edgecolors=WHITE, linewidth=2, zorder=10)
ax.text(15.45, alpha_gut_inv + 1.5,
        r'$\alpha_\mathrm{GUT}^{-1} = 42.135$' + '\nExact unification',
        color=GOLD, fontsize=10, ha='right')

sin2_pred = 0.231223
alpha_s_pred = 0.11838
a2_pred = sin2_pred * 137.036
a3_pred = 1.0 / alpha_s_pred

mz_log = np.log10(91.1876)
ax.axvline(x=mz_log, color=DIM, linestyle='--', alpha=0.5, linewidth=1)
ax.text(mz_log + 0.15, 60, r'$M_Z$', color=DIM, fontsize=10)

ax.annotate(r'$\sin^2\!\theta_W = 0.231223$' + '\n(12 ppm from measured)',
            xy=(mz_log, a2_pred), xytext=(5.0, a2_pred + 8),
            color=GREEN, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=GREEN))

ax.annotate(r'$\alpha_s = 0.11838$' + '\n(0.33% from measured)',
            xy=(mz_log, a3_pred), xytext=(5.0, a3_pred - 8),
            color=RED, fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=RED))

ax.set_xlim(mz_log - 0.5, 16.2)
ax.set_ylim(0, 70)
ax.legend(facecolor=PAN, edgecolor=DIM, labelcolor=WHITE, fontsize=9, loc='center right')

save(fig, 'phys39_02_sin2_extraction.png')


# ================================================================
# FIG 3: HYDROGEN TWO-PATH DIAGRAM
# Type: Connection/Integer Map (Type 5)
# Shows: Two independent derivation chains converging on hydrogen
#        from opposite ends of physics — QED and BBN.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 12))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 12)

def draw_box(ax, x, y, w, h, text, color, fontsize=9):
    box = FancyBboxPatch((x - w/2.0, y - h/2.0), w, h,
                         boxstyle='round,pad=0.15', facecolor=BG,
                         edgecolor=color, linewidth=1.8)
    ax.add_patch(box)
    ax.text(x, y, text, color=color, fontsize=fontsize,
            ha='center', va='center', fontweight='bold')

def draw_arrow_v(ax, x1, y1, x2, y2, color):
    ax.annotate('', xy=(x2, y2 + 0.3), xytext=(x1, y1 - 0.3),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8))

ax.text(9, 11.7, 'HYDROGEN: Two Independent Paths to the Same Element',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

# QED path (left)
ax.text(4.5, 11.0, 'QED PATH', color=CYAN, fontsize=12, fontweight='bold', ha='center')

draw_box(ax, 4.5, 10.0, 3.8, 0.7,
         r'$a_e = 0.00115965218059$' + '\n(Harvard trap, 0.11 ppb)', CYAN, 8)
draw_arrow_v(ax, 4.5, 9.6, 4.5, 9.0, CYAN)

draw_box(ax, 4.5, 8.5, 3.8, 0.7,
         r'$\alpha^{-1} = 137.035999207$' + '\n(5-loop QED + 7 corrections)', CYAN, 8)
draw_arrow_v(ax, 4.5, 8.1, 4.5, 7.5, CYAN)

draw_box(ax, 4.5, 7.0, 3.8, 0.7,
         r'$R_\infty = 10973731.563$' + ' m' + r'$^{-1}$' + '\n(SI formula, 0.44 ppb)', CYAN, 8)
draw_arrow_v(ax, 4.5, 6.6, 4.5, 6.0, CYAN)

draw_box(ax, 4.5, 5.5, 4.2, 0.7,
         'f(1S-2S) = 2466061412 MHz\n(0.44 ppb from measured)', CYAN, 8)

# BBN path (right)
ax.text(13.5, 11.0, 'BBN PATH', color=GREEN, fontsize=12, fontweight='bold', ha='center')

draw_box(ax, 13.5, 10.0, 3.8, 0.7,
         'Gauge integers: 11, 13\n(Yang-Mills, SU(2) beta)', GREEN, 8)
draw_arrow_v(ax, 13.5, 9.6, 13.5, 9.0, GREEN)

draw_box(ax, 13.5, 8.5, 3.8, 0.7,
         '(22/13)' + r'$\pi$' + ' = 5.3165\n(DM/baryon, 725 ppm)', GREEN, 8)
draw_arrow_v(ax, 13.5, 8.1, 13.5, 7.5, GREEN)

draw_box(ax, 13.5, 7.0, 3.8, 0.7,
         r'$\eta_{10} = 6.090$' + '\n(baryon-to-photon, 0.24%)', GREEN, 8)
draw_arrow_v(ax, 13.5, 6.6, 13.5, 6.0, GREEN)

draw_box(ax, 13.5, 5.5, 4.0, 0.7,
         'D/H = 2.531e-5\n(0.12' + r'$\sigma$' + ' from measured)', GREEN, 8)

# Convergence arrows to hydrogen
ax.annotate('', xy=(9, 3.8), xytext=(4.5, 5.1),
            arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
ax.annotate('', xy=(9, 3.8), xytext=(13.5, 5.1),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# Hydrogen box
h_box = FancyBboxPatch((6.5, 2.7), 5.0, 1.4, boxstyle='round,pad=0.2',
                        facecolor=PAN, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(h_box)
ax.text(9, 3.7, 'HYDROGEN', color=GOLD, fontsize=14, fontweight='bold', ha='center')
ax.text(9, 3.15, 'Internal structure (how atoms work)\n'
        'Cosmic abundance (how much exists)',
        color=SILVER, fontsize=9, ha='center')

ax.text(3.2, 4.5, 'How hydrogen\natoms absorb light', color=CYAN, fontsize=9,
        ha='center', style='italic')
ax.text(14.8, 4.5, 'How much hydrogen\nthe universe contains', color=GREEN, fontsize=9,
        ha='center', style='italic')

ax.text(9, 1.8, 'Same element, predicted from opposite ends of physics, both matching',
        color=SILVER, fontsize=11, ha='center')

save(fig, 'phys39_03_hydrogen_two_path.png')


# ================================================================
# FIG 4: M_GUT SCALE WITH HYPER-K WINDOW
# Type: Threshold/Region (Type 3)
# Shows: Where SM and CD M_GUT sit relative to Super-K bound
#        and Hyper-K sensitivity window.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel=r'$\log_{10}(M_\mathrm{GUT}\,/\,\mathrm{GeV})$',
         ylabel='', title='GUT Scale: CD in the Hyper-K Window')

ax.set_xlim(12, 18)
ax.set_ylim(0, 6)
ax.set_yticks([])

ax.axvspan(12, 15.2, alpha=0.08, color=RED)
ax.axvspan(15.2, 16.0, alpha=0.10, color=GREEN)
ax.axvspan(16.0, 18, alpha=0.05, color=DIM)

ax.text(13.5, 5.5, 'Below Super-K bound\n(excluded)', color=RED, fontsize=11,
        ha='center', fontweight='bold')
ax.text(15.6, 5.5, 'Hyper-K\nwindow', color=GREEN, fontsize=11,
        ha='center', fontweight='bold')
ax.text(17.0, 5.5, 'Beyond\nHyper-K', color=DIM, fontsize=11, ha='center')

ax.axvline(x=15.2, color=RED, linestyle='-', linewidth=2, alpha=0.7)
ax.text(15.25, 4.2, 'Super-K bound\n' + r'$\tau_p > 1.6 \times 10^{34}$ yr',
        color=RED, fontsize=9)

ax.axvline(x=16.0, color=GREEN, linestyle='--', linewidth=1.5, alpha=0.5)
ax.text(16.05, 4.2, 'Hyper-K\nsensitivity\nlimit', color=GREEN, fontsize=8)

ax.scatter([13.80], [3.0], color=MAG, s=300, edgecolors=WHITE, linewidth=2, zorder=10)
ax.text(13.80, 3.6, 'SM one-loop\n' + r'$10^{13.80}$', color=MAG, fontsize=10,
        ha='center', fontweight='bold')

ax.scatter([13.82], [2.0], color=MAG, s=250, edgecolors=WHITE, linewidth=2,
           zorder=10, marker='D')
ax.text(13.82, 1.4, 'SM two-loop\n' + r'$10^{13.82}$', color=MAG, fontsize=9,
        ha='center')

ax.scatter([15.54], [3.0], color=GOLD, s=300, edgecolors=WHITE, linewidth=2, zorder=10)
ax.text(15.54, 3.6, 'CD one-loop\n' + r'$10^{15.54}$', color=GOLD, fontsize=10,
        ha='center', fontweight='bold')

ax.scatter([15.61], [2.0], color=GOLD, s=250, edgecolors=WHITE, linewidth=2,
           zorder=10, marker='D')
ax.text(15.61, 1.4, 'CD two-loop\n' + r'$10^{15.61}$', color=GOLD, fontsize=9,
        ha='center')

ax.text(15.0, 0.6, 'SM: excluded by proton decay bounds\n'
        'CD: testable at Hyper-K within 10 years',
        color=SILVER, fontsize=10, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD, alpha=0.8))

save(fig, 'phys39_04_mgut_scale.png')


# ================================================================
# FIG 5: HYDROGEN 1S-2S ERROR DECOMPOSITION
# Type: Comparison Bar (Type 6)
# Shows: The 64,000x scale difference between R_inf residual
#        and theory-experiment gap.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='Error source', ylabel='Contribution (Hz, log scale)',
         title='f(1S-2S) Error Budget: Why the Miss is Entirely from ' + r'$R_\infty$')

sources = ['R-infinity residual\n(from alpha extraction)', 'Theory-experiment\ngap (QED higher order)']
values = [1092322, 17]
colors_bar = [CYAN, DIM]
fractions = ['99.998%', '0.002%']

bars = ax.bar([0, 1], values, color=colors_bar, edgecolor=[CYAN, DIM],
              linewidth=2, alpha=0.7, width=0.5)

ax.set_yscale('log')
ax.set_ylim(5, 5e6)
ax.set_xlim(-0.5, 1.8)
ax.set_xticks([0, 1])
ax.set_xticklabels(sources, color=SILVER, fontsize=10)

for i in range(len(bars)):
    bar = bars[i]
    val = values[i]
    frac = fractions[i]
    ax.text(bar.get_x() + bar.get_width()/2.0, val * 1.5,
            '%s Hz\n(%s)' % ('{:,}'.format(val), frac),
            ha='center', va='bottom', color=colors_bar[i], fontsize=12, fontweight='bold')

ax.axhline(y=1092322, color=CYAN, linestyle=':', alpha=0.3, linewidth=1)
ax.axhline(y=17, color=DIM, linestyle=':', alpha=0.3, linewidth=1)

ax.text(1.5, 100000, '64,000x\nscale\ndifference',
        color=ORANGE, fontsize=14, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=ORANGE))

ax.text(0.8, 8, 'Total miss: 0.44 ppb -- entirely from alpha extraction precision',
        color=SILVER, fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=BG, edgecolor=DIM))

save(fig, 'phys39_05_1s2s_error_budget.png')


# ================================================================
# FIG 6: EIGHT-DOMAIN DERIVATION GRAPH
# Type: Connection/Integer Map (Type 5)
# Shows: The TOPOLOGY of twelve crossings across eight domains.
#        Hydrogen at top (spectroscopy) and bottom (BBN).
# ================================================================

fig, ax = plt.subplots(figsize=(18, 14))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 18)
ax.set_ylim(0, 14)

ax.text(9, 13.5, 'THE DERIVATION GRAPH: Eight Domains, Twelve Crossings',
        color=GOLD, fontsize=16, fontweight='bold', ha='center')

def domain_box(ax, x, y, w, h, title, values_text, color):
    box = FancyBboxPatch((x - w/2.0, y - h/2.0), w, h,
                         boxstyle='round,pad=0.2', facecolor=PAN,
                         edgecolor=color, linewidth=2.0)
    ax.add_patch(box)
    ax.text(x, y + h/2.0 - 0.25, title, color=color, fontsize=10,
            fontweight='bold', ha='center', va='top')
    ax.text(x, y - 0.1, values_text, color=SILVER, fontsize=7.5,
            ha='center', va='center')

domain_box(ax, 9, 12.2, 3.5, 1.0, 'SPECTROSCOPY',
           'f(1S-2S): 0.44 ppb', PURPLE)

domain_box(ax, 9, 10.5, 4.0, 1.0, 'QED',
           r'$\alpha$: 0.007 ppb, $R_\infty$, $a_0$, $\mu_0$', CYAN)

domain_box(ax, 3.5, 8.5, 3.2, 1.0, 'MUON',
           r'$a_\mu$: 0.22 ppb' + '\n6.5' + r'$\sigma$ anomaly', MAG)

domain_box(ax, 9, 8.5, 3.5, 1.0, 'ELECTROWEAK',
           r'$M_W$: 195 ppm, $\Gamma_Z$' + '\n' + r'$N_\mathrm{gen} = 3$', BLUE)

domain_box(ax, 14.5, 8.5, 3.5, 1.2, 'GUT',
           'gap 0.027 (218x)\n'
           + r'$\sin^2\!\theta_W$: 12 ppm' + '\n'
           + r'$M_\mathrm{GUT} = 10^{15.6}$', GOLD)

domain_box(ax, 3.5, 6.0, 3.0, 1.0, 'FLAVOR',
           r'$V_{ud}$: 264 ppm' + '\nCKM: 0.83' + r'$\sigma$', ORANGE)

domain_box(ax, 9, 6.0, 3.5, 1.0, 'COSMOLOGY',
           r'$\Omega_b$: 725 ppm' + '\n' + r'$\Omega_\mathrm{DE}$: 0.20%', GREEN)

domain_box(ax, 9, 3.8, 3.5, 1.2, 'NUCLEAR (BBN)',
           'D/H: 0.12' + r'$\sigma$' + ', Y_p: 0.94' + r'$\sigma$'
           + '\nHe-3: 0.36' + r'$\sigma$' + ', Li-7: 2.96x', RED)

domain_box(ax, 15.5, 3.8, 2.5, 0.8, 'KOIDE',
           r'$m_\tau$: 62 ppm' + '\n(atoll)', DIM)

connections = [
    (9, 11.7, 9, 11.0, PURPLE),
    (9, 10.0, 9, 9.0, CYAN),
    (7.5, 10.0, 3.5, 9.0, MAG),
    (10.5, 10.0, 14.5, 9.1, GOLD),
    (14.5, 7.9, 9, 6.5, GREEN),
    (14.5, 7.9, 3.5, 6.5, ORANGE),
    (12.5, 8.0, 10.5, 6.5, GREEN),
    (9, 5.5, 9, 4.4, RED),
    (9, 8.0, 9, 6.5, BLUE),
]

for x1, y1, x2, y2, c in connections:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=c, lw=1.5, alpha=0.6))

ax.text(5.5, 12.5, 'H (spectroscopy)', color=PURPLE, fontsize=9,
        ha='center', style='italic')
ax.text(5.5, 3.3, 'H (abundance)', color=RED, fontsize=9,
        ha='center', style='italic')

ax.text(9, 2.3, '48 derived values  |  15 inputs  |  surplus +33  |  12 crossings',
        color=SILVER, fontsize=11, ha='center',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BG, edgecolor=GOLD))

save(fig, 'phys39_06_eight_domains.png')


# ================================================================
# FIG 7: PRECISION LANDSCAPE — 48 VALUES ON LOG SCALE
# Type: Scale/Landscape (Type 2)
# Shows: The SPREAD of 48 values from 0.007 ppb to 2.96x.
# ================================================================

fig, ax = plt.subplots(figsize=(18, 10))
fig.patch.set_facecolor(BG)
style_ax(ax, xlabel='Miss (log scale)', ylabel='',
         title='Precision Landscape: 48 Derived Values Across Eight Domains')

# (miss_ppb_equiv, label, domain_color, is_new)
vdata = [
    (0.007, r'$\alpha^{-1}$ vs Rb', CYAN, False),
    (0.22, r'$a_0$', CYAN, False),
    (0.22, r'$\mu_0$', CYAN, False),
    (0.22, r'$a_\mu$ QED', MAG, False),
    (0.44, r'$R_\infty$', CYAN, False),
    (0.44, 'f(1S-2S)', PURPLE, True),
    (12, r'$\sin^2\!\theta_W$', GOLD, True),
    (62, r'$m_\tau$ (Koide)', DIM, False),
    (195, r'$M_W$ (G_F)', BLUE, False),
    (207, r'$M_W$ cons.', BLUE, False),
    (264, r'$V_{ud}$', ORANGE, False),
    (270, r'$R_l$', BLUE, False),
    (330, r'$\alpha_s$ 2-loop', GOLD, True),
    (360, 'He-3', RED, False),
    (402, r'$M_W$ (sin$^2$)', BLUE, False),
    (640, 'gap CD', GOLD, True),
    (725, 'DM/baryon', GREEN, False),
    (727, r'$\Omega_b$', GREEN, False),
    (940, r'$Y_p$', RED, False),
    (1200, 'D/H', RED, False),
    (1500, r'$\Omega_{DE}$', GREEN, False),
    (2000, r'$\rho_\Lambda$', GREEN, False),
    (5800, r'$\Gamma_Z$', BLUE, False),
    (8100, r'$\Gamma_{had}$', BLUE, False),
    (8740, r'$\alpha_s$ 1L-CD', GOLD, True),
    (29600, 'Li-7 (2.96x)', RED, False),
    (437000, r'$\alpha_s$ SM', GOLD, True),
]

y_pos = np.linspace(len(vdata) - 1, 0, len(vdata))

for idx in range(len(vdata)):
    miss, label, color, is_new = vdata[idx]
    y = y_pos[idx]
    marker = 'D' if is_new else 'o'
    size = 180 if is_new else 120
    edge = GOLD if is_new else WHITE
    ax.scatter([miss], [y], color=color, s=size, edgecolors=edge,
               linewidth=2 if is_new else 1.2, marker=marker, zorder=10)
    ax.text(miss * 1.6, y, '  ' + label, color=color, fontsize=8,
            va='center', ha='left')

ax.set_xscale('log')
ax.set_xlim(0.003, 1e6)
ax.set_ylim(-1, len(vdata))
ax.set_yticks([])

bands = [
    (0.003, 10, 'sub-ppb\n(6 values)', CYAN),
    (10, 1000, 'sub-permille\n(9 values)', GREEN),
    (1000, 10000, 'sub-percent\n(10 values)', BLUE),
    (10000, 1e6, 'percent+\n(anomalies)', RED),
]
for lo, hi, label, c in bands:
    ax.axvspan(lo, hi, alpha=0.04, color=c)
    ax.text(np.sqrt(lo * hi), len(vdata) - 0.5, label,
            color=c, fontsize=8, ha='center', va='bottom', alpha=0.7)

ax.text(0.01, 0.5, 'diamond = new this paper', color=GOLD, fontsize=9)

save(fig, 'phys39_07_precision_landscape.png')


# ================================================================
# FIG 8: IDENTITY CARD
# Type: Identity Card (Type 8)
# Shows: Visual anchor — 48 values, 8 domains, surplus +33,
#        key findings of PHYS-39.
# ================================================================

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.axis('off')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)

border = FancyBboxPatch((0.5, 0.5), 15, 9, boxstyle='round,pad=0.3',
                         facecolor=BG, edgecolor=GOLD, linewidth=2.5)
ax.add_patch(border)

ax.text(8, 9.0, 'HOWL-PHYS-39-2026', color=GOLD, fontsize=18,
        fontweight='bold', ha='center')
ax.text(8, 8.4, 'Near-Exact Two-Loop Unification and the Spectroscopy Bridge',
        color=WHITE, fontsize=12, ha='center')

# Left column
ax.text(1.5, 7.4, 'DERIVATION GRAPH', color=CYAN, fontsize=11, fontweight='bold')
ax.text(1.5, 6.8, '48 derived values', color=WHITE, fontsize=10)
ax.text(1.5, 6.3, '15 measured inputs', color=SILVER, fontsize=10)
ax.text(1.5, 5.8, 'surplus +33', color=GOLD, fontsize=10, fontweight='bold')
ax.text(1.5, 5.3, '8 physics domains', color=WHITE, fontsize=10)
ax.text(1.5, 4.8, '12 domain crossings', color=SILVER, fontsize=10)

# Center column
ax.text(6.0, 7.4, 'KEY RESULTS', color=GOLD, fontsize=11, fontweight='bold')
ax.text(6.0, 6.8, r'$\sin^2\!\theta_W = 0.231223$  (12 ppm)', color=GREEN, fontsize=10)
ax.text(6.0, 6.3, r'$\alpha_s = 0.11838$  (0.33%)', color=RED, fontsize=10)
ax.text(6.0, 5.8, 'Two-loop gap = 0.027  (218x)', color=GOLD, fontsize=10)
ax.text(6.0, 5.3, 'f(1S-2S): 0.44 ppb', color=PURPLE, fontsize=10)
ax.text(6.0, 4.8, r'$\alpha^{-1}$ vs Rb: 0.007 ppb (12 digits)', color=CYAN, fontsize=10)

# Right column
ax.text(11.5, 7.4, 'DOMAINS', color=ORANGE, fontsize=11, fontweight='bold')
domains_list = [
    ('QED', CYAN), ('Electroweak', BLUE), ('GUT', GOLD), ('Cosmology', GREEN),
    ('Nuclear', RED), ('Muon', MAG), ('Flavor', ORANGE), ('Spectroscopy', PURPLE)
]
for i in range(len(domains_list)):
    name, c = domains_list[i]
    y = 6.8 - i * 0.35
    ax.plot([11.3, 11.45], [y, y], color=c, linewidth=3)
    ax.text(11.6, y, name, color=c, fontsize=9, va='center')

# Divider
ax.plot([1.5, 14.5], [3.8, 3.8], color=DIM, linewidth=0.5)

ax.text(8, 3.3, 'SESSION 5-6 ADVANCES', color=GOLD, fontsize=11,
        fontweight='bold', ha='center')
ax.text(8, 2.7,
        'Two-loop gap: 5.88 (SM) -> 0.027 (CD) = 218x improvement',
        color=WHITE, fontsize=10, ha='center')
ax.text(8, 2.2,
        'k1 bug found: 5/3 -> 3/5 (resolved 10-12% alpha_s discrepancy)',
        color=SILVER, fontsize=10, ha='center')
ax.text(8, 1.7,
        'One-loop degeneracy proven: s = s (identity, no information)',
        color=SILVER, fontsize=10, ha='center')
ax.text(8, 1.2,
        'Hydrogen via two paths: QED (0.44 ppb) and BBN (0.12 sigma)',
        color=SILVER, fontsize=10, ha='center')

save(fig, 'phys39_08_identity_card.png')


# ================================================================
# SUMMARY
# ================================================================
print("\nPHYS-39 Diagrams complete. 8 figures saved:")
print("  phys39_01_two_loop_comparison.png")
print("  phys39_02_sin2_extraction.png")
print("  phys39_03_hydrogen_two_path.png")
print("  phys39_04_mgut_scale.png")
print("  phys39_05_1s2s_error_budget.png")
print("  phys39_06_eight_domains.png")
print("  phys39_07_precision_landscape.png")
print("  phys39_08_identity_card.png")

